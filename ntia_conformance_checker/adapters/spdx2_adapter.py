# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""SPDX 2.x specific data extraction adapter."""

from spdx_tools.spdx.model.document import Document
from spdx_tools.spdx.model.relationship import RelationshipType
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.validation.validation_message import ValidationMessage

from .adapter_interface import SbomAdapter, is_blank_string

SPDX2_DEPENDENCY_RELATIONSHIP_TYPES: frozenset[RelationshipType] = frozenset(
    {
        RelationshipType.CONTAINS,
        RelationshipType.CONTAINED_BY,
        RelationshipType.DEPENDS_ON,
        RelationshipType.DEPENDENCY_OF,
        RelationshipType.BUILD_DEPENDENCY_OF,
        RelationshipType.DEV_DEPENDENCY_OF,
        RelationshipType.OPTIONAL_DEPENDENCY_OF,
        RelationshipType.PROVIDED_DEPENDENCY_OF,
        RelationshipType.RUNTIME_DEPENDENCY_OF,
        RelationshipType.TEST_DEPENDENCY_OF,
        RelationshipType.DYNAMIC_LINK,
        RelationshipType.STATIC_LINK,
    }
)


def _is_blank(value: object, noassertion: bool = False) -> bool:
    """
    Check whether an SPDX 2 field value should be treated as blank.

    Blank means ``None``, ``SpdxNoAssertion``, or a blank string per
    :func:`is_blank_string`. spdx-tools keeps some keywords as plain strings,
    e.g. lowercase ``noassertion`` in ``copyrightText``.

    Args:
        value: The field value to check.
        noassertion: Whether ``NOASSERTION`` strings count as blank.

    Returns:
        bool: True if the value is considered blank.
    """
    if value is None or isinstance(value, SpdxNoAssertion):
        return True
    return is_blank_string(value, noassertion)


def _collect_spdx2_element_ids(doc: Document) -> set[str]:
    """
    Collect non-blank SPDX IDs of content elements (packages, files, snippets).

    The document's own SPDX ID (e.g. ``SPDXRef-DOCUMENT``) is excluded so
    document-level membership relationships are not treated as component
    dependency relationships.
    """
    element_ids: set[str] = set()
    for attr in ("packages", "files", "snippets"):
        for elem in getattr(doc, attr, []):
            spdx_id = getattr(elem, "spdx_id", None)
            if isinstance(spdx_id, str) and not _is_blank(spdx_id):
                element_ids.add(spdx_id)
    return element_ids


def has_spdx2_dependency_relationship(doc: Document) -> bool:
    """Return True if a dependency or containment relationship connects SPDX 2 elements."""
    relationships = getattr(doc, "relationships", [])
    if not relationships:
        return False

    element_ids = _collect_spdx2_element_ids(doc)
    if len(element_ids) < 2:
        return False

    return any(
        rel.relationship_type in SPDX2_DEPENDENCY_RELATIONSHIP_TYPES
        and isinstance(rel.spdx_element_id, str)
        and isinstance(rel.related_spdx_element_id, str)
        and rel.spdx_element_id != rel.related_spdx_element_id
        and rel.spdx_element_id in element_ids
        and rel.related_spdx_element_id in element_ids
        for rel in relationships
    )


class Spdx2Adapter(SbomAdapter):
    """Adapter for extracting data from SPDX 2.x documents."""

    def __init__(self, doc: Document) -> None:
        self.doc = doc

    def get_doc_spec_version(self) -> str | None:
        doc_creation_info = getattr(self.doc, "creation_info", None)
        if doc_creation_info:
            return getattr(doc_creation_info, "spdx_version", None)
        return None

    def check_author(self) -> bool:
        # Note that the spdx-tools's parser will raise an SPDXParsingError
        # anyway, if the document does not contain a creator.
        # So in practice, this section should always return True
        doc_creation_info = getattr(self.doc, "creation_info", None)
        if doc_creation_info:
            return bool(getattr(doc_creation_info, "creators", []))
        return False

    def check_timestamp(self) -> bool:
        # Note that the spdx-tools's parser will raise an SPDXParsingError,
        # if the document does not contain a timestamp.
        # So in practice, this section should always return True.
        doc_creation_info = getattr(self.doc, "creation_info", None)
        if doc_creation_info:
            return bool(getattr(doc_creation_info, "created", None))
        return False

    def get_sbom_name(self) -> str:
        doc_creation_info = getattr(self.doc, "creation_info", None)
        if doc_creation_info:
            return getattr(doc_creation_info, "name", "")
        return ""

    def get_components_without_names(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids and _is_blank(package.name)
        ]

    def get_components_without_versions(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids and _is_blank(package.version)
        ]

    def get_components_without_suppliers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids
            and _is_blank(package.supplier, noassertion=True)
        ]

    def get_components_without_identifiers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if _is_blank(package.spdx_id)
        ]

    def get_components_without_concluded_licenses(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        # Note: concluded license is mandatory in SPDX-2.2 and SPDX-2.3
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids
            and _is_blank(package.license_concluded, noassertion=True)
        ]

    def get_components_without_copyright_texts(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids
            and _is_blank(package.copyright_text, noassertion=True)
        ]

    def check_dependency_relationships(self) -> bool:
        """In SPDX 2, this checks element-level dependency relationships."""
        return has_spdx2_dependency_relationship(self.doc)

    def get_total_number_components(self) -> int:
        """In SPDX 2, this returns the total count of packages."""
        return len(getattr(self.doc, "packages", []))

    def get_sbom_types(
        self, conformance_messages: list[ValidationMessage]
    ) -> list[str]:
        # SBOM type is only available in SPDX 3
        return []
