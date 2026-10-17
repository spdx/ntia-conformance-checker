# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""SPDX 3.x specific data extraction adapter."""

from typing import Any, Callable, Union

from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.validation.validation_message import (
    ValidationContext,
    ValidationMessage,
)

from ntia_conformance_checker.spdx3_utils import (
    get_all_packages,
    has_package_dependency_relationship,
    iter_objects_with_property,
    iter_relationships_by_type,
)

from .adapter_interface import SbomAdapter, is_blank_string

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


# Component kind (see model.COMPONENT_KINDS) -> SPDX 3 class; "system" is the root package.
_KIND_TYPES: dict[str, type[spdx3.SHACLObject]] = {
    "component": spdx3.software_Package,
    "ai_model": spdx3.ai_AIPackage,
    "dataset": spdx3.dataset_DatasetPackage,
}


# External identifier types that identify a component (not an email, CVE, ...).
_IDENTIFIER_TYPES = frozenset(
    {"packageUrl", "cpe22", "cpe23", "swid", "swhid", "gitoid", "urlScheme"}
)


# Attribute holding what a value object says (a hash needs its value, not only
# its algorithm).
_CONTENT_ATTRIBUTES = (
    "name",
    "hashValue",
    "software_contentIdentifierValue",
    "key",
    "identifier",
    "locator",
)
# Properties whose string values are element references that must resolve.
_REFERENCE_PROPERTIES = frozenset(
    {"originatedBy", "suppliedBy", "createdBy", "createdUsing"}
)


def _object_present(obj: spdx3.SHACLObject) -> bool:
    """Whether an SPDX 3 object says something: it is not NOASSERTION and, when
    it has a content attribute, that attribute is present."""
    if _is_blank_ref(obj):
        return False
    for attr in _CONTENT_ATTRIBUTES:
        if hasattr(obj, attr):
            return _value_present(getattr(obj, attr))
    return True


def _value_present(value: object) -> bool:
    """Whether an SPDX 3 property value carries information.

    Numbers always do (``0`` is a value). Strings and references do unless
    blank or NOASSERTION; lists do if any item does; objects do unless they have
    a blank name (a nameless agent or tool says nothing).
    """
    if value is None or isinstance(value, bool):
        return value is True
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str):
        no_presence = "/" in value and value.rsplit("/", 1)[-1] == "noAssertion"
        return not (_is_blank_ref(value) or no_presence)  # PresenceType IRI
    if isinstance(value, spdx3.SHACLObject):
        return _object_present(value)
    try:
        return any(_value_present(item) for item in value)  # type: ignore[attr-defined]
    except TypeError:
        return bool(value)


def _property_present(
    obj: object, prop: str, resolves: Callable[[str], bool] | None = None
) -> bool:
    """Whether ``obj`` carries information in SPDX 3 property ``prop``.

    With ``resolves``, an element reference that points to nothing in the
    document does not count.
    """
    value = getattr(obj, prop, None)
    if prop in _REFERENCE_PROPERTIES and resolves is not None:
        items = list(value) if isinstance(value, (list, spdx3.ListProxy)) else [value]
        value = [i for i in items if not isinstance(i, str) or resolves(i)]
    if prop == "externalIdentifier":  # only identifying types count
        value = [
            item
            for item in value or []
            if str(getattr(item, "externalIdentifierType", "")).rsplit("/", 1)[-1]
            in _IDENTIFIER_TYPES
        ]
    return _value_present(value)


def _is_model_purpose(obj: spdx3.SHACLObject) -> bool:
    """Whether an AI package is a model: it declares ``model`` as a purpose, or
    declares none (an AI package with another purpose, such as ``application``,
    is the system around the model)."""
    purposes = [getattr(obj, "software_primaryPurpose", None)]
    purposes += list(getattr(obj, "software_additionalPurpose", None) or [])
    names = {str(p).rsplit("/", 1)[-1] for p in purposes if p}
    return not names or "model" in names


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
        Note that SPDX 3 requires identifiers for all elements,
        so this should not happen in a valid SPDX 3 document.
        The spdx-python-model JSON deserializer will raise a ValueError
        if any element is missing an identifier.
        """
        return [
            (name or "", spdx_id or "")
            for name, spdx_id, _ in iter_objects_with_property(
                self.object_set,
                spdx3.software_Package,
                "spdxId",
                reachable_ids=None,
            )
            if _is_blank(spdx_id)
        ]

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

    def check_dependency_relationships(self) -> bool:
        """In SPDX 3, this checks package-level dependency relationships."""
        return has_package_dependency_relationship(self.object_set)

    # ---- Kind-scoped checks ------------------------------------------------

    def _kind_objects(
        self, kind: str, reachable_ids: set[str] | None
    ) -> list[tuple[str, str, Any]]:
        """``(name, spdx_id, object)`` of ``kind`` (only the reachable ones unless
        ``reachable_ids`` is ``None``), sorted by name and id."""
        objects: list[Any]
        if kind == "system":
            objects = self._system_objects()
        elif kind in _KIND_TYPES:
            objects = list(self.object_set.foreach_type(_KIND_TYPES[kind]))
            if kind == "ai_model":
                objects = [o for o in objects if _is_model_purpose(o)]
        else:
            raise ValueError(f"Unknown component kind {kind!r}")
        entries = [
            ((getattr(o, "name", "") or "").strip(), (o.spdxId or "").strip(), o)
            for o in objects
        ]
        return sorted(
            (e for e in entries if reachable_ids is None or e[1] in reachable_ids),
            key=lambda e: e[:2],
        )

    def _system_objects(self) -> list[Any]:
        """The SBOM's root packages: what the SBOM describes."""
        found: list[Any] = []
        for root in getattr(self.spdx3_doc, "rootElement", []) or []:
            elem = self.object_set.find_by_id(root) if isinstance(root, str) else root
            if isinstance(elem, (spdx3.software_Sbom, spdx3.Bom)):
                inner = getattr(elem, "rootElement", []) or []
                found.extend(
                    self.object_set.find_by_id(r) if isinstance(r, str) else r
                    for r in inner
                )
            elif elem is not None:
                found.append(elem)
        unique = {o.spdxId: o for o in found if o is not None}
        return list(unique.values())

    def has_components_of_kind(self, kind: str, reachable_ids: set[str] | None) -> bool:
        return bool(self._kind_objects(kind, reachable_ids))

    def get_components_without_properties(
        self, kind: str, properties: tuple[str, ...], reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        objects = self._kind_objects(kind, reachable_ids)
        for prop in properties:
            # The system is whatever the SBOM describes, so it has no fixed class.
            if kind in _KIND_TYPES and not hasattr(_KIND_TYPES[kind], prop):
                raise ValueError(f"Unknown SPDX 3 property {prop!r} for kind {kind!r}")
        return [
            (name, spdx_id)
            for name, spdx_id, obj in objects
            if not any(
                _property_present(obj, prop, self._resolves) for prop in properties
            )
        ]

    def get_components_without_relationships(
        self,
        kind: str,
        relationships: tuple[str, ...],
        direction: str,
        reachable_ids: set[str],
    ) -> list[tuple[str, str]]:
        if direction not in ("from", "to"):
            raise ValueError(f"Unknown relationship direction {direction!r}")
        linked: set[str] = set()
        for rel_type in relationships:
            for from_id, to_ids in iter_relationships_by_type(
                self.object_set, rel_type
            ):
                if direction == "to":
                    linked.update(to_ids)
                elif not all(self._is_blank_target(t) for t in to_ids):
                    linked.add(from_id)
        return [
            (name, spdx_id)
            for name, spdx_id, _ in self._kind_objects(kind, reachable_ids)
            if spdx_id not in linked
        ]

    def _is_blank_target(self, spdx_id: str) -> bool:
        """Whether a relationship target says nothing (NOASSERTION)."""
        target = self.object_set.find_by_id(spdx_id)
        return (
            _is_blank_ref(spdx_id)
            or (target is not None and _is_blank_ref(target))
            or is_blank_license_expression(target)
        )

    def _resolves(self, spdx_id: str) -> bool:
        """Whether ``spdx_id`` names an element of the document."""
        return self.object_set.find_by_id(spdx_id) is not None

    def document_declares_any(self, properties: tuple[str, ...]) -> bool:
        holders = (self.spdx3_doc, getattr(self.spdx3_doc, "creationInfo", None))
        return any(
            _property_present(h, prop, self._resolves)
            for prop in properties
            for h in holders
            if h is not None
        )

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
