# SPDX-FileCopyrightText: 2024-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Base checking functionality."""

from __future__ import annotations

import json
import logging
import os
import warnings
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, cast

from spdx_python_model import v3_0_1 as spdx3  # type: ignore # import-untyped
from spdx_tools.spdx.model.relationship import RelationshipType
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.parser import parse_anything
from spdx_tools.spdx.parser.error import SPDXParsingError
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document
from spdx_tools.spdx.validation.validation_message import (
    ValidationContext,
    ValidationMessage,
)

from ._deprecated import DeprecatedCheckerMixin
from .constants import DEFAULT_SBOM_SPEC
from .report import (
    ReportContext,
    get_validation_messages_json,
    report_html,
    report_text,
)
from .spdx3_utils import (
    get_boms_from_spdx_document,
    get_packages_from_bom,
    iter_objects_with_property,
    iter_relationships_by_type,
    validate_spdx3_data,
)

if TYPE_CHECKING:
    from spdx_tools.spdx.model.document import Document

    from .model import Finding
    from .spec import Spec


# pylint: disable=too-many-instance-attributes,too-many-public-methods,too-many-lines
class BaseChecker(DeprecatedCheckerMixin, ABC):
    """Base class for all compliance/conformance checkers.

    This base class contains methods for common tasks like file parsing
    and information extractions from the SBOM.

    Any class inheriting from BaseChecker must implement its abstract methods,
    such as `check_compliance` and `output_json`.
    """

    compliance_standard: str = ""  # fsct3, ntia
    sbom_spec: str = ""  # spdx2, spdx3

    # These are detectable by spdx-tools, so not needed for now.
    # file_format: str = ""  # json, rdf-xml, tag-value, yaml, xml

    file: str = ""

    # For SPDX 3, we have to use SHACLObjectSet instead of SpdxDocument,
    # because we need access to relationships and other elements that are not
    # accessible from SpdxDocument.
    doc: Document | spdx3.SHACLObjectSet | None = None
    __spdx3_doc: spdx3.SpdxDocument | None = None  # cached SPDX 3 document

    _parsing_errors: list[str] = []
    _validation_messages: list[ValidationMessage] = []
    _conformance_messages: list[ValidationMessage] = []

    sbom_name: str = ""

    # Document-level values are no longer eagerly stored as instance
    # attributes.  Callers read them via :meth:`document_value` (raw
    # value, cached) or :meth:`document_has` (presence bool).  Each
    # ``get_doc_<element_id>`` extractor is the single source of truth
    # for one element; the cache lives in ``_cache_doc_value``.
    # See https://github.com/spdx/ntia-conformance-checker/issues/392
    # for discussion on dependency relationships and DESCRIBES.

    findings: dict[str, "list[Finding]"]
    """Findings keyed by SARIF rule id, populated by :meth:`run_probes`.
    Empty list = the rule passed; list of :class:`Finding` = failures.
    Initialised to ``{}`` per instance in :meth:`__init__`."""

    @property
    def parsing_errors(self) -> list[str]:
        """Parsing errors encountered during file parsing."""
        return self._parsing_errors

    @property
    def validation_messages(self) -> list[ValidationMessage]:
        """Validation messages from SPDX document validation."""
        return self._validation_messages

    _SPEC: "Spec"
    """Subclass-defined class attribute holding the standard's Spec instance."""

    @property
    def conformance_messages(self) -> list[ValidationMessage]:
        """Conformance messages from compliance/conformance checks."""
        return self._conformance_messages

    @property
    def compliant(self) -> bool:
        """Deprecated: the compliance verdict at the baseline maturity.

        Kept for backwards compatibility.  Equivalent to
        ``check_compliance(maturity=0)``.  Prefer calling
        :meth:`check_compliance` directly -- it lets you pass a maturity
        level and is not tied to any instance default.
        """
        warnings.warn(
            "The 'compliant' attribute is deprecated; call "
            "check_compliance(maturity=...) instead (defaults to maturity 0).",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.check_compliance(maturity=0)

    @property
    def spec(self) -> "Spec":
        """The compliance specification for this checker.

        Defaults to reading the subclass's ``_SPEC`` class attribute.
        Subclasses that need dynamic spec resolution may override this
        property instead of defining ``_SPEC``.
        """
        return self._SPEC

    def components_without(self, element_id: str) -> list[tuple[str, str]]:
        """Components that do not declare ``element_id``.

        Accessor used by probes: reports which components lack the element.

        Returns a list of ``(component_name, spdx_id)`` tuples.  Dispatches
        to ``get_components_without_<element_id>`` on the checker; results
        are cached per element_id so repeat calls cost one full SBOM scan
        per element.  Returns an empty list for unknown ``element_id``
        values so a rule referencing an element this checker doesn't know
        about degrades to a no-op.
        """
        cache = self._cache_components_without
        if element_id in cache:
            return list(cache[element_id])
        method = getattr(self, f"get_components_without_{element_id}", None)
        if not callable(method):
            return []
        # pylint: disable=not-callable
        raw = cast("list[tuple[str, str]]", method())
        result: list[tuple[str, str]] = list(raw) if raw else []
        cache[element_id] = result
        return list(result)

    def document_value(self, element_id: str) -> object:
        """Raw value of the document-level element, or ``None`` if unknown.

        Lazily dispatches to ``get_doc_<element_id>()`` on the checker;
        results are cached in ``_cache_doc_value`` so repeat reads cost
        nothing.  Probes that need the actual value (e.g. timestamp
        format validation) call this; probes that only care about
        presence call :meth:`document_has`.
        """
        cache = self._cache_doc_value
        if element_id in cache:
            return cache[element_id]
        method = getattr(self, f"get_doc_{element_id}", None)
        if not callable(method):
            cache[element_id] = None
            return None
        value = method()  # pylint: disable=not-callable
        cache[element_id] = value
        return value

    def document_has(self, element_id: str) -> bool:
        """True iff the SBOM document declares ``element_id``.

        Truthiness of :meth:`document_value` -- empty string / empty list /
        ``None`` / ``False`` all mean "absent".
        """
        return bool(self.document_value(element_id))

    def _validate_maturity(self, maturity: int) -> int:
        """Validate ``maturity`` against the spec's declared levels.

        Returns it unchanged when valid (``0`` -- the baseline -- always is);
        raises ``ValueError`` otherwise.
        """
        valid = self.spec.maturity_ordinals()
        if maturity not in valid:
            raise ValueError(
                f"maturity {maturity!r} is not a declared maturity level of "
                f"spec {self.spec.id!r}; valid levels: {list(valid)!r}"
            )
        return maturity

    def components_without_info(
        self, maturity: int = 0
    ) -> list[tuple[str, list[tuple[str, str]]]]:
        """Component-level findings grouped by element_id, scoped to ``maturity``.

        Derived on demand from :attr:`findings` (runs probes if needed).
        Used by the text / HTML reporters to render the missing-info
        block ("Missing required information in these components: ...").
        """
        target = self._validate_maturity(maturity)
        if not self.findings:
            self.run_probes()
        out: list[tuple[str, list[tuple[str, str]]]] = []
        for rule in self.spec.active_rules(target):
            probe = rule.probe
            if probe is None or probe.name != "require_component_attribute":
                continue
            findings = self.findings.get(self.spec.rule_id(rule), [])
            if not findings:
                continue
            out.append(
                (
                    rule.element_id,
                    [(f.component_name, f.component_id) for f in findings],
                )
            )
        return out

    @property
    def all_components_without_info(
        self,
    ) -> list[tuple[str, list[tuple[str, str]]]]:
        """Component-level findings grouped by element_id, at the baseline
        maturity (0).  Thin alias for :meth:`components_without_info`."""
        return self.components_without_info()

    def requirement_results(self, maturity: int = 0) -> list[tuple[str, bool]]:
        """Per-rule ``(competency_question, passed)`` rows for ``maturity``.

        Rows follow the spec's active-rule order for the resolved maturity, so
        the text / HTML report tables stay in sync with the YAML without manual
        duplication.  Runs probes on first use.
        """
        target = self._validate_maturity(maturity)
        if not self.findings:
            self.run_probes()
        return [
            (
                rule.competency_question,
                not self.findings.get(self.spec.rule_id(rule), []),
            )
            for rule in self.spec.active_rules(target)
        ]

    def run_probes(self) -> dict[str, list["Finding"]]:
        """Run every active rule's probe once; return findings by rule id.

        Probes are presence checks and so are **maturity-independent**: this
        runs *all* active rules (every maturity tier) and caches the result on
        ``self.findings``.  Maturity is applied later as a pure view filter by
        the verdict / report / output methods, so one checker instance can be
        queried at different maturity levels without re-probing.  Catalogue-only
        and TBD rules are skipped (their ``probe`` is ``None``).
        """
        # Importing lazily so BaseChecker stays cheap to import for
        # callers that only want the SBOM-parsing behaviour.
        # pylint: disable=import-outside-toplevel
        from .probes import lookup

        findings: dict[str, list[Finding]] = {}
        for rule in self.spec.active_rules():
            if rule.probe is None:
                findings[self.spec.rule_id(rule)] = []
                continue
            probe_fn = lookup(rule.probe.name)
            findings[self.spec.rule_id(rule)] = list(
                probe_fn(self, **rule.probe.params)
            )
        self.findings = findings
        return findings

    @abstractmethod
    def check_compliance(self, maturity: int = 0) -> bool:
        """Abstract method to check compliance/conformance at ``maturity``.

        Defaults to ``0`` (the baseline).
        """
        raise NotImplementedError

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str = "",
        sbom_spec: str = DEFAULT_SBOM_SPEC,
    ) -> None:
        """
        Initialize the BaseChecker.

        Args:
            file (str): The name of the file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used.
            sbom_spec (str): The SBOM specification to be used.

        Maturity is *not* an instance setting: probes run for all tiers, and
        the level to assess against is supplied per call to the verdict /
        report / output methods (defaulting to ``0``, the baseline).
        """
        self.compliance_standard = compliance
        self.sbom_spec = sbom_spec
        # self.file_format = ""

        self.file = file

        # Make sure the logs are instance variables and not class variables
        # to avoid shared state between instances.
        self._parsing_errors = []
        self._validation_messages = []
        self._conformance_messages = []
        self.findings = {}
        self._cache_components_without: dict[str, list[tuple[str, str]]] = {}
        self._cache_doc_value: dict[str, object] = {}

        match sbom_spec:
            case "spdx2":
                self.doc = self.parse_file()
            case "spdx3":
                object_set = self.parse_spdx3_file()
                if not object_set:
                    logging.error("Failed to parse the SPDX 3 file.")
                else:
                    self.doc = object_set
                    self.__spdx3_doc, _val_msgs = validate_spdx3_data(object_set)
                    if not self.__spdx3_doc or _val_msgs:
                        logging.error("SpdxDocument not found or invalid.")
                    self._validation_messages.extend(_val_msgs)
            case _:
                # We can add a heuristic to detect the spec from the file content here,
                # in case sbom_spec is not provided or invalid.
                raise ValueError(f"Unsupported SBOM specification: {sbom_spec}")

        if self.doc:
            if validate and sbom_spec == "spdx2":
                self.doc = cast("Document", self.doc)
                self._validation_messages = validate_full_spdx_document(self.doc)

            self.sbom_name = self.get_sbom_name()
            self.sbom_gen_context = self.get_sbom_types()

            # Document-level extractors are *not* called eagerly here.
            # :meth:`document_value` runs them on first read and caches
            # the result in ``_doc_value_cache``; probes / SARIF / JSON
            # all go through that one path.

            # Component-level presence checks are *not* eagerly computed
            # here.  They are evaluated lazily by :meth:`components_without`
            # (cached per element_id) the first time a probe / report /
            # output emitter asks for them.

    # ---- Document-level value extractors --------------------------------
    #
    # Naming convention: ``get_doc_<element_id>()`` returns the *value* of
    # the document-level element, typed naturally for the element (str,
    # list, etc.).  An empty string / empty list is treated as "absent" by
    # :meth:`document_has`.  Each value is cached on ``self.doc_<element_id>``
    # in :meth:`__init__` so probes / SARIF / JSON emitters read the field
    # directly without re-parsing the SBOM.

    def get_doc_author(self) -> str:
        """Return the SBOM author identifier, or ``""`` if none recorded.

        SPDX 2 may have multiple creators; we join them with ``"; "``.
        SPDX 3 returns the first ``createdBy`` identifier.
        """
        if not self.doc:
            return ""

        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            ci = getattr(self.doc, "creation_info", None)
            if ci is None:
                return ""
            creators = getattr(ci, "creators", []) or []
            return "; ".join(str(c) for c in creators)

        if self.sbom_spec == "spdx3" and self.__spdx3_doc is not None:
            ci = getattr(self.__spdx3_doc, "creationInfo", None)
            if ci is None:
                return ""
            created_by = getattr(ci, "createdBy", []) or []
            return str(created_by[0]) if created_by else ""

        return ""

    def get_doc_timestamp(self) -> str:
        """Return the SBOM creation / most-recent-update timestamp string.

        Per the 2025 CISA spec, the Timestamp records "the date and time
        of the most recent update to the SBOM data".  In SPDX 2 / 3 this
        is the ``created`` field on ``creationInfo``.  Returns ``""`` if
        absent.
        """
        if not self.doc:
            return ""

        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            ci = getattr(self.doc, "creation_info", None)
            if ci is None:
                return ""
            created = getattr(ci, "created", None)
            return str(created) if created else ""

        if self.sbom_spec == "spdx3" and self.__spdx3_doc is not None:
            ci = getattr(self.__spdx3_doc, "creationInfo", None)
            if ci is None:
                return ""
            created = getattr(ci, "created", None)
            return str(created) if created else ""

        return ""

    def get_doc_spec_version(self) -> str:
        """Return the SBOM specification version string (e.g. ``"SPDX-2.3"``),
        or ``""`` if absent."""
        if not self.doc:
            return ""

        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            ci = getattr(self.doc, "creation_info", None)
            if ci is None:
                return ""
            return str(getattr(ci, "spdx_version", "") or "")

        if self.sbom_spec == "spdx3" and isinstance(
            self.__spdx3_doc, spdx3.SpdxDocument
        ):
            ci = getattr(self.__spdx3_doc, "creationInfo", None)
            if ci is None:
                return ""
            return str(getattr(ci, "specVersion", "") or "")

        return ""

    def get_doc_dependency_relationship(self) -> list[object]:
        """Return the list of DESCRIBES-style dependency relationships.

        Empty list = no relationships declared (rule fails).  The list
        carries opaque relationship objects so future probes can inspect
        types, completeness, etc.; current probes only check truthiness.
        """
        if not self.doc:
            return []

        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            rels = self.doc.relationships or []
            describes = [
                rel
                for rel in rels
                if rel.relationship_type == RelationshipType.DESCRIBES
            ]
            if not describes:
                return []
            spdx_id_set = {p.spdx_id for p in self.doc.packages}
            return [
                rel for rel in describes if rel.related_spdx_element_id in spdx_id_set
            ]

        if self.sbom_spec == "spdx3":
            boms = get_boms_from_spdx_document(self.__spdx3_doc)
            out: list[object] = []
            for bom in boms or []:
                out.extend(get_packages_from_bom(bom) or [])
            return out

        return []

    def get_sbom_name(self) -> str:
        """Retrieve the name of the SBOM."""
        if not self.doc:
            return ""

        name: str = ""

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            doc_creation_info = getattr(self.doc, "creation_info", None)
            if doc_creation_info:
                name = getattr(doc_creation_info, "name", "")

        # SPDX 3
        elif self.sbom_spec == "spdx3" and isinstance(
            self.__spdx3_doc, spdx3.SpdxDocument
        ):
            name = getattr(self.__spdx3_doc, "name", "")

        return name

    def get_sbom_types(self) -> list[str]:
        """Get SBOM types from the rootElement of the SpdxDocument.

        CISA Framing Software Component Transparency (2024) listed
        "SBOM type" as one of baseline attributes, see Table 1 (p. 22) in:
        https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024

        In SPDX 3, SBOM type is only available in /Software/Sbom class.
        """
        # SBOM type is only available in SPDX 3
        if not self.doc or self.sbom_spec != "spdx3":
            return []

        root_elements: list[spdx3.SHACLObject] = getattr(
            self.__spdx3_doc, "rootElement", []
        )
        if not root_elements:
            return []

        sbom_types: list[str] = []

        # Assuming only one rootElement per document
        root_elem = root_elements[0]
        if not isinstance(root_elem, spdx3.software_Sbom):
            doc_id = getattr(self.__spdx3_doc, "spdxId", None)
            root_elem_id = getattr(root_elem, "spdxId", None)
            error_msg = (
                "To have SBOM type (SBOM generation context) information, "
                "the rootElement of the SpdxDocument shall be of type "
                "/Software/Sbom."
                f"Found: {type(root_elem).__name__!r}"
            )
            context = ValidationContext(parent_id=doc_id, spdx_id=root_elem_id)
            self._conformance_messages.append(ValidationMessage(error_msg, context))
            return []

        sbom_types = [
            type_.strip() for type_ in getattr(root_elem, "software_sbomType", [])
        ]

        return sbom_types

    def get_doc_sbom_type(self) -> list[str]:
        """Return the SBOM type(s) (a.k.a. SBOM generation context), or ``[]``.

        Document-level extractor backing the ``sbom_type`` element id used by
        :meth:`document_value` / :meth:`document_has` and the
        ``require_document_attribute`` probe.  Reuses the value computed once in
        :meth:`__init__` (``self.sbom_gen_context``) so the conformance message
        emitted by :meth:`get_sbom_types` is not duplicated.

        SBOM type is only expressible in SPDX 3 (``/Software/Sbom``); SPDX 2
        SBOMs always return ``[]`` and therefore cannot satisfy an FSCT3
        minimum-expected SBOM-type requirement.
        """
        if not self.doc:
            return []
        return list(getattr(self, "sbom_gen_context", []) or [])

    def get_components_without_concluded_license(self) -> list[tuple[str, str]]:
        """
        Retrieve components missing a concluded license.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """
        # Note: concluded license is mandatory in SPDX-2.2 and SPDX-2.3
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            packages = getattr(self.doc, "packages", [])

            return [
                (package.name or "", package.spdx_id or "")
                for package in packages
                if (
                    package.license_concluded is None
                    or isinstance(package.license_concluded, SpdxNoAssertion)
                    or (
                        isinstance(package.license_concluded, str)
                        and package.license_concluded.strip() == ""
                    )
                )
            ]

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            has_concluded_license_ids: set[str] = {
                from_id
                for from_id, to_id in iter_relationships_by_type(
                    self.doc, "hasConcludedLicense"
                )
                if to_id.strip()
                != spdx3.expandedlicensing_IndividualLicensingInfo.NAMED_INDIVIDUALS[
                    "NoAssertionLicense"
                ]
            }

            return [
                (name or "", spdx_id or "")
                for name, spdx_id, _ in iter_objects_with_property(
                    self.doc,
                    spdx3.software_Package,
                    "spdxId",
                )
                if spdx_id not in has_concluded_license_ids
            ]

        return []

    def get_components_without_copyright_notice(self) -> list[tuple[str, str]]:
        """
        Retrieve components missing a copyright text.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            packages = getattr(self.doc, "packages", [])

            return [
                (package.name or "", package.spdx_id or "")
                for package in packages
                if (
                    package.copyright_text is None
                    or isinstance(package.copyright_text, SpdxNoAssertion)
                    or (
                        isinstance(package.copyright_text, str)
                        and package.copyright_text.strip() == ""
                    )
                )
            ]

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            return [
                (name or "", spdx_id or "")
                for name, spdx_id, copyright_text in iter_objects_with_property(
                    self.doc,
                    spdx3.software_Package,
                    "software_copyrightText",
                )
                if not copyright_text
                or (isinstance(copyright_text, str) and copyright_text.strip() == "")
            ]

        return []

    def get_components_without_unique_identifier(self) -> list[tuple[str, str]]:
        """
        Retrieve components missing unique identifiers (SPDX IDs).

        Note that SPDX 3 requires identifiers for all elements,
        so this should not happen in a valid SPDX 3 document.
        The spdx-python-model JSON deserializer will raise a ValueError
        if any element is missing an identifier.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            packages = getattr(self.doc, "packages", [])

            return [
                (package.name or "", package.spdx_id or "")
                for package in packages
                if (
                    package.spdx_id is None
                    or (
                        isinstance(package.spdx_id, str)
                        and package.spdx_id.strip() == ""
                    )
                )
            ]

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            return [
                (name or "", spdx_id or "")
                for name, _, spdx_id in iter_objects_with_property(
                    self.doc, spdx3.Element, "spdxId"
                )
                if not spdx_id or (isinstance(spdx_id, str) and spdx_id.strip() == "")
            ]

        return []

    def get_components_without_name(self) -> list[tuple[str, str]]:
        """
        Retrieve components missing a name.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            packages = getattr(self.doc, "packages", [])

            return [
                (package.name or "", package.spdx_id or "")
                for package in packages
                if (
                    package.name is None
                    or (isinstance(package.name, str) and package.name.strip() == "")
                )
            ]

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            return [
                (name or "", spdx_id or "")
                for _, spdx_id, name in iter_objects_with_property(
                    self.doc, spdx3.software_Package, "name"
                )
                if not name or (isinstance(name, str) and name.strip() == "")
            ]

        return []

    def get_components_without_supplier(self) -> list[tuple[str, str]]:
        """
        Retrieve components missing supplier information.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            packages = getattr(self.doc, "packages", [])

            return [
                (package.name or "", package.spdx_id or "")
                for package in packages
                if (
                    package.supplier is None
                    or isinstance(package.supplier, SpdxNoAssertion)
                    or (
                        isinstance(package.supplier, str)
                        and package.supplier.strip() == ""
                    )
                )
            ]

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            return [
                (name or "", spdx_id or "")
                for name, spdx_id, supplier in iter_objects_with_property(
                    self.doc, spdx3.software_Package, "suppliedBy"
                )
                if not supplier
                or (
                    supplier.name if hasattr(supplier, "name") else supplier or ""
                ).strip()
                == ""
            ]

        return []

    def get_components_without_version(self) -> list[tuple[str, str]]:
        """
        Retrieve components missing version information.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            packages = getattr(self.doc, "packages", [])

            return [
                (package.name or "", package.spdx_id or "")
                for package in packages
                if (
                    package.version is None
                    or isinstance(package.version, SpdxNoAssertion)
                    or (
                        isinstance(package.version, str)
                        and package.version.strip() == ""
                    )
                )
            ]

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            return [
                (name or "", spdx_id or "")
                for name, spdx_id, package_version in iter_objects_with_property(
                    self.doc, spdx3.software_Package, "software_packageVersion"
                )
                if not package_version
                or (isinstance(package_version, str) and package_version.strip() == "")
            ]

        return []

    def get_total_number_components(self) -> int:
        """
        Retrieve total number of components.

        Returns:
            int: The total number of components.
        """
        if not self.doc:
            return 0

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            if not self.doc.packages:
                return 0
            return len(self.doc.packages)

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)
            objects: set[spdx3.SHACLObject] = getattr(self.doc, "objects", set())
            return len(objects)

        return 0

    def parse_file(self) -> Document | None:
        """
        Parse SPDX 2 SBOM document.

        Returns:
            Document | None: An SPDX 2 SBOM document if successful, otherwise None.
        """
        if not self.file or str(self.file).strip() == "":
            logging.error("No file path provided.")
            return None

        if not os.path.exists(self.file):
            logging.error("File not found: %s", self.file)
            return None

        try:
            # Annotate as `object` to avoid differences between local and CI
            # mypy stubs for `parse_anything.parse_file`. Casting to
            # `Document` below makes the return type explicit for callers.
            doc: object = parse_anything.parse_file(self.file)
        except SPDXParsingError as err:
            # err.get_messages() is untyped in spdx-tools; cast to Any to
            # silence mypy's "no-untyped-call" check in typed contexts.
            self._parsing_errors.extend(cast("Any", err).get_messages())
            return None
        except Exception as err:  # pylint: disable=broad-except
            # Catch any other errors, including BeartypeCallHintParamViolation
            # from the spdx-tools library when parsing invalid SPDX files.
            # The spdx-tools library uses beartype for runtime type checking,
            # which throws exceptions when encountering missing required fields
            # (e.g., missing author, timestamp, or identifiers).
            logging.debug("Error parsing file: %s", err)
            self._parsing_errors.append(
                f"Error parsing file: {type(err).__name__}: {str(err)}"
            )
            return None

        return cast("Document", doc)

    def parse_spdx3_file(self) -> spdx3.SHACLObjectSet | None:
        """
        Parse SPDX 3 SBOM document.

        Returns:
            spdx3.SHACLObjectSet | None: An SHACLObjectSet if successful, otherwise None.
        """
        if not self.file or str(self.file).strip() == "":
            logging.error("No file path provided.")
            return None

        if not os.path.exists(self.file):
            logging.error("File not found: %s", self.file)
            return None

        object_set: spdx3.SHACLObjectSet = spdx3.SHACLObjectSet()
        try:
            with open(self.file, encoding="utf-8") as f:
                spdx3.JSONLDDeserializer().read(f, object_set)
        except (OSError, json.JSONDecodeError) as err:
            logging.warning("SPDX3 deserialization failed: %s", err)
            self._parsing_errors.append(str(err))
            return None

        return object_set

    def print_components_missing_info(self, maturity: int = 0) -> None:
        """
        Print information about components that are missing required details.

        What is considered "missing" is determined by a compliance standard.
        Subclasses may override this method to provide custom behavior.

        Returns:
            None
        """
        # If parsing failed, skip
        if self._parsing_errors:
            return

        components_without_info = self.components_without_info(maturity)
        if not components_without_info:
            return

        print("Missing required information in these components:")
        for info_name, components in components_without_info:
            print(
                f"{info_name} ({len(components)}): "
                f"{', '.join([name for name, _ in components])}"
            )

    def print_table_output(self, verbose: bool = False, maturity: int = 0) -> None:
        """
        Print element-by-element result table.

        Args:
            verbose (bool): If True, print detailed information.
            maturity (int): Maturity level to report against;
                Defaults to ``0`` (the baseline).

        Returns:
            None
        """
        report_context = ReportContext(
            sbom_spec=getattr(self, "sbom_spec", ""),
            compliance_standard=getattr(self, "compliance_standard", ""),
            compliant=self.check_compliance(maturity),
            requirement_results=self.requirement_results(maturity),
            components_without_info=self.components_without_info(maturity),
            validation_messages=self._validation_messages,
            conformance_messages=self._conformance_messages,
            parsing_errors=self._parsing_errors,
        )

        print(report_text(report_context, verbose))

    def output_html(self, maturity: int = 0) -> str:
        """
        Create element-by-element result table in HTML.

        Args:
            maturity (int): Maturity level to report against;
                Defaults to ``0`` (the baseline).

        Returns:
            str: The HTML representation of the results.
        """
        report_context = ReportContext(
            sbom_spec=getattr(self, "sbom_spec", ""),
            compliance_standard=getattr(self, "compliance_standard", ""),
            compliant=self.check_compliance(maturity),
            requirement_results=self.requirement_results(maturity),
            components_without_info=self.components_without_info(maturity),
            validation_messages=self._validation_messages,
            conformance_messages=self._conformance_messages,
            parsing_errors=self._parsing_errors,
        )

        return report_html(report_context, verbose=True)

    def output_json(self, maturity: int = 0) -> dict[str, Any]:
        """
        Create a JSON-serializable result dict.

        Args:
            maturity (int): Maturity level to report against;
                Defaults to ``0`` (the baseline).

        Subclasses may override to provide custom fields.
        """
        target = self._validate_maturity(maturity)
        is_conformant = self.check_compliance(target)
        result: dict[str, Any] = {
            "isConformant": is_conformant,
            "isNtiaConformant": is_conformant,  # backward compatibility
            "complianceStandard": getattr(self, "compliance_standard", ""),
            "sbomSpec": getattr(self, "sbom_spec", ""),
            "validationMessages": get_validation_messages_json(
                self._validation_messages
            ),
            "conformanceMessages": get_validation_messages_json(
                self._conformance_messages
            ),
            "parsingError": self._parsing_errors,
            "sbomName": getattr(self, "sbom_name", ""),
            "specVersionProvided": self.document_has("spec_version"),
            "totalNumberComponents": self.get_total_number_components(),
        }

        # Ensure probes have run before emitting per-rule JSON.
        if not self.findings:
            self.run_probes()

        for rule in self.spec.active_rules(target):
            if not rule.json_key or rule.probe is None:
                continue
            rule_id = self.spec.rule_id(rule)
            findings = self.findings.get(rule_id, [])
            if rule.probe.name == "require_document_attribute":
                # Doc-level: presence bool.  Absent = one Finding emitted.
                result[rule.json_key] = not findings
            else:
                # Component-level: list of non-conformant components.
                # Prefer human-readable name; fall back to SPDX ID.
                nonconformant = [(f.component_name or f.component_id) for f in findings]
                result[rule.json_key] = {
                    "nonconformantComponents": nonconformant,
                    "allProvided": not bool(nonconformant),
                }

        return result

    def output_sarif(
        self, *, embed_sbom: bool = False, maturity: int = 0
    ) -> dict[str, Any]:
        """
        Create a SARIF result log.

        The output uses ``SBOM-[SPEC]-[CATEGORY]-[NNN]`` rule ids (see
        :file:`RULES.md`).  Identifiers are chosen so the same strings can be
        reused by a future OSCAL exporter as ``control`` / ``group`` ids
        without remapping.

        Args:
            embed_sbom: When ``True``, embed the source SBOM file content in
                ``runs[0].artifacts[0].contents`` so downstream SARIF viewers
                can render the artifact alongside results from a single log
                file.  Default is ``False`` (link by URI only) -- embedding
                significantly increases the log size.
            maturity: Maturity level to scope results to; defaults to ``0``
                (the baseline).  The rule catalogue always lists every non-TBD
                rule regardless of maturity; only *results* are scoped.

        Subclasses may override to provide custom fields.
        """
        # Imported lazily so that the SARIF module isn't loaded for
        # tools that only call output_json.
        # pylint: disable=import-outside-toplevel
        from .report_sarif import build_sarif

        return build_sarif(self, embed_sbom=embed_sbom, maturity=maturity)
