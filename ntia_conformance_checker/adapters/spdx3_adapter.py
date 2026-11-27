# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""SPDX 3.x specific data extraction adapter."""

from collections.abc import Callable
from typing import Any, Union

from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.validation.validation_message import (
    ValidationContext,
    ValidationMessage,
)

from ntia_conformance_checker.spdx3_utils import (
    get_all_packages,
    iter_objects_with_property,
    iter_relationships_by_type,
)

from .adapter_interface import SbomAdapter, is_blank_string

# External identifier types that identify a component. FSCT 3rd ed. §2.2.2.4
# "Unique Identifier" gives CPE, PURL, SWID, UUID, SWHID and OmniBOR (gitoid)
# as examples; SPDX 3.0.1 has no UUID type, so a UUID is "other". Not cve,
# email, securityOther or urlScheme: they name a vulnerability, a person or a
# resource, not the component (SPDX 3.0.1 Core/Vocabularies/
# ExternalIdentifierType).
_IDENTIFIER_TYPES = frozenset(
    {"packageUrl", "cpe22", "cpe23", "swid", "swhid", "gitoid", "other"}
)

_ELEMENT_INDIVIDUALS = spdx3.IndividualElement.NAMED_INDIVIDUALS
_LICENSE_INDIVIDUALS = spdx3.expandedlicensing_IndividualLicensingInfo.NAMED_INDIVIDUALS

# NoAssertion individuals, as full IRIs and compact names.
# None individuals state "none", so are not blank.
_BLANK_INDIVIDUALS: frozenset[str] = frozenset(
    {
        _ELEMENT_INDIVIDUALS["NoAssertionElement"],
        _LICENSE_INDIVIDUALS["NoAssertionLicense"],
        "NoAssertionElement",
        "expandedlicensing_NoAssertionLicense",
    }
)


def _is_blank(value: object, noassertion: bool = False) -> bool:
    """
    Check whether an SPDX 3 field value should be treated as blank.

    Blank means falsy (``None``, ``""``, ...) or a blank string per
    :func:`is_blank_string`.

    Args:
        value: The field value to check.
        noassertion: Whether ``NOASSERTION`` strings count as blank.

    Returns:
        bool: True if the value is considered blank.
    """
    return not value or is_blank_string(value, noassertion)


def _is_blank_ref(value: object) -> bool:
    """
    Check whether an SPDX 3 element reference should be treated as blank.

    A reference is blank when it is blank per :func:`_is_blank` (with
    ``noassertion``), or when it points to ``NoAssertionElement`` or
    ``NoAssertionLicense``, as an IRI or an element object.

    Args:
        value: The reference to check (IRI string or element object).

    Returns:
        bool: True if the reference is considered blank.
    """
    ref = getattr(value, "spdxId", value)
    return _is_blank(value, noassertion=True) or (
        isinstance(ref, str) and ref.strip() in _BLANK_INDIVIDUALS
    )


def is_blank_license_expression(obj: object) -> bool:
    """
    Check whether an object is a license expression without license information.

    Args:
        obj: The object to check, e.g. a relationship target.

    Returns:
        bool: True if ``obj`` is a ``simplelicensing_LicenseExpression`` whose
        text is blank, ``NOASSERTION``, or names the
        ``NoAssertionLicense`` individual.
    """
    if not isinstance(obj, spdx3.simplelicensing_LicenseExpression):
        return False
    expr = getattr(obj, "simplelicensing_licenseExpression", "")
    return _is_blank(expr, noassertion=True) or (
        isinstance(expr, str) and expr.strip().upper() == "NOASSERTIONLICENSE"
    )


class Spdx3Adapter(SbomAdapter):
    """Adapter for extracting data from SPDX 3.x documents."""

    def __init__(
        self, object_set: spdx3.SHACLObjectSet, spdx3_doc: spdx3.SpdxDocument | None
    ) -> None:
        self.object_set = object_set
        self.spdx3_doc = spdx3_doc

    def get_doc_spec_version(self) -> str | None:
        doc_creation_info = getattr(self.spdx3_doc, "creationInfo", None)
        if doc_creation_info:
            return getattr(doc_creation_info, "specVersion", None)
        return None

    def check_author(self) -> bool:
        doc_creation_info = getattr(self.spdx3_doc, "creationInfo", None)
        if doc_creation_info:
            return bool(getattr(doc_creation_info, "createdBy", []))
        return False

    def check_timestamp(self) -> bool:
        doc_creation_info = getattr(self.spdx3_doc, "creationInfo", None)
        if doc_creation_info:
            return bool(getattr(doc_creation_info, "created", None))
        return False

    def get_sbom_name(self) -> str:
        return getattr(self.spdx3_doc, "name", "")

    def get_components_without_names(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (name or "", spdx_id or "")
            for _, spdx_id, name in iter_objects_with_property(
                self.object_set,
                spdx3.software_Package,
                "name",
                reachable_ids,
            )
            if _is_blank(name)
        ]

    def get_components_without_versions(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (name or "", spdx_id or "")
            for name, spdx_id, package_version in iter_objects_with_property(
                self.object_set,
                spdx3.software_Package,
                "software_packageVersion",
                reachable_ids,
            )
            if _is_blank(package_version)
        ]

    def get_components_without_suppliers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (name or "", spdx_id or "")
            for name, spdx_id, supplier in iter_objects_with_property(
                self.object_set,
                spdx3.software_Package,
                "suppliedBy",
                reachable_ids,
            )
            # Agent suppliers carry ``name``; bare IRI strings are checked as-is.
            if _is_blank_ref(supplier)
            or _is_blank(getattr(supplier, "name", supplier), noassertion=True)
        ]

    def get_components_without_identifiers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        """
        Reachable packages with no identifier of their own: a package URL,
        a content identifier, or an external identifier of an identifying type.

        The ``spdxId`` every SPDX 3 element has does not count: it references
        the element within the graph, but does not identify the component
        elsewhere. NTIA 2021 (IV. Minimum Elements > Data Fields > Other Unique
        Identifiers): "used to identify a component, or serve as a look-up key
        for relevant databases". FSCT 3rd ed. §2.2.2.4 "Unique Identifier":
        identifiers "provide additional information to help uniquely define a
        Component". SPDX 2.3.1 Annex L.1.2, which is informative, maps the
        NTIA element to the SPDX identifier; the normative text is followed.
        A hash is not counted; FSCT has it as its own attribute (§2.2.2.5).
        """
        identified = self._identified_package_ids()
        return [
            (name or "", spdx_id or "")
            for name, spdx_id, _ in iter_objects_with_property(
                self.object_set,
                spdx3.software_Package,
                "spdxId",
                reachable_ids,
            )
            if spdx_id not in identified
        ]

    def _identified_package_ids(self) -> set[str]:
        """IDs of the packages that carry a package URL, a content identifier
        or an identifying external identifier."""

        # A property value is a string or a list proxy, by property: Any.
        def ids(prop: str, carries: Callable[[Any], bool]) -> set[str]:
            return {
                spdx_id
                for _, spdx_id, value in iter_objects_with_property(
                    self.object_set, spdx3.software_Package, prop
                )
                if carries(value)
            }

        def is_identifying(ext: object) -> bool:
            kind = str(getattr(ext, "externalIdentifierType", ""))
            return kind.rsplit("/", 1)[-1] in _IDENTIFIER_TYPES and not _is_blank(
                getattr(ext, "identifier", None), noassertion=True
            )

        return (
            ids("software_packageUrl", lambda v: not _is_blank(v, noassertion=True))
            | ids(
                "software_contentIdentifier",
                lambda v: any(
                    not _is_blank(
                        getattr(c, "software_contentIdentifierValue", None),
                        noassertion=True,
                    )
                    for c in v or []
                ),
            )
            | ids("externalIdentifier", lambda v: any(map(is_identifying, v or [])))
        )

    def _is_blank_license(self, ref: str) -> bool:
        """Check whether a license reference carries no license information."""
        return _is_blank_ref(ref) or is_blank_license_expression(
            self.object_set.find_by_id(ref)
        )

    def get_components_without_concluded_licenses(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        has_concluded_license_ids: set[str] = {
            from_id
            for from_id, to_ids in iter_relationships_by_type(
                self.object_set, "hasConcludedLicense"
            )
            if any(not self._is_blank_license(to_id) for to_id in to_ids)
        }

        return [
            (name or "", spdx_id or "")
            for name, spdx_id, _ in iter_objects_with_property(
                self.object_set,
                spdx3.software_Package,
                "spdxId",
                reachable_ids,
            )
            if spdx_id not in has_concluded_license_ids
        ]

    def get_components_without_copyright_texts(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (name or "", spdx_id or "")
            for name, spdx_id, copyright_text in iter_objects_with_property(
                self.object_set,
                spdx3.software_Package,
                "software_copyrightText",
                reachable_ids,
            )
            if _is_blank(copyright_text, noassertion=True)
        ]

    def get_total_number_components(self) -> int:
        """
        In SPDX 3, this returns the total count of packages and package
        subclasses (including AIPackage and DatasetPackage).
        """
        return len(get_all_packages(self.object_set))

    def get_sbom_types(
        self, conformance_messages: list[ValidationMessage]
    ) -> list[str]:
        """In SPDX 3, SBOM type is only available in /Software/Sbom class."""
        if not self.spdx3_doc:
            return []

        root_elements: spdx3.ListProxy[Union[str, spdx3.Element]] = (
            self.spdx3_doc.rootElement
        )
        if not root_elements:
            return []

        sbom_types: list[str] = []

        # Assuming only one rootElement per document
        root_elem = root_elements[0]
        if not isinstance(root_elem, spdx3.software_Sbom):
            doc_id = getattr(self.spdx3_doc, "spdxId", None)
            root_elem_id = getattr(root_elem, "spdxId", None)
            error_msg = (
                "To have SBOM type (SBOM generation context) information, "
                "the rootElement of the SpdxDocument shall be of type "
                "/Software/Sbom. "
                f"Found: {type(root_elem).__name__!r}"
            )
            context = ValidationContext(parent_id=doc_id, spdx_id=root_elem_id)
            conformance_messages.append(ValidationMessage(error_msg, context))
            return []

        sbom_types = [
            type_.strip() for type_ in getattr(root_elem, "software_sbomType", [])
        ]

        return sbom_types
