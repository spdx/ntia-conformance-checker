# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""SPDX 2.x specific data extraction adapter."""

from spdx_tools.spdx.model.document import Document
from spdx_tools.spdx.model.relationship import RelationshipType
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.model.spdx_none import SpdxNone
from spdx_tools.spdx.validation.validation_message import ValidationMessage

from .adapter_interface import SbomAdapter, is_blank_string


def _is_blank(value: object) -> bool:
    """
    Check whether an SPDX 2 field value should be treated as blank.

    Blank means ``None``, ``SpdxNone``, ``SpdxNoAssertion``, or a string that
    is whitespace-only or ``NONE``/``NOASSERTION`` (any case). spdx-tools keeps
    keywords as plain strings in some fields, e.g. ``versionInfo``.

    Args:
        value: The field value to check.

    Returns:
        bool: True if the value is considered blank.
    """
    if value is None or isinstance(value, (SpdxNone, SpdxNoAssertion)):
        return True
    return is_blank_string(value)


class Spdx2Adapter(SbomAdapter):
    """Adapter for extracting data from SPDX 2.x documents."""

    def __init__(self, doc: Document):
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
            if package.spdx_id in reachable_ids and _is_blank(package.supplier)
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
            if package.spdx_id in reachable_ids and _is_blank(package.license_concluded)
        ]

    def get_components_without_copyright_texts(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids and _is_blank(package.copyright_text)
        ]

    def check_dependency_relationships(self) -> bool:
        """In SPDX 2, this checks for a DESCRIBES relationship"""
        if not getattr(self.doc, "relationships", []):
            return False

        describes_relationships = [
            rel
            for rel in self.doc.relationships
            if rel.relationship_type == RelationshipType.DESCRIBES
        ]
        # A set of all package spdx_ids for quick lookup
        spdx_id_set = {package.spdx_id for package in getattr(self.doc, "packages", [])}

        # Check if any of the "DESCRIBES" relationships describe a Package
        describes_package = any(
            rel.related_spdx_element_id in spdx_id_set
            for rel in describes_relationships
        )

        return describes_package

    def get_total_number_components(self) -> int:
        """In SPDX 2, this returns the total count of packages."""
        return len(getattr(self.doc, "packages", []))

    def get_sbom_types(
        self, conformance_messages: list[ValidationMessage]
    ) -> list[str]:
        # SBOM type is only available in SPDX 3
        return []
