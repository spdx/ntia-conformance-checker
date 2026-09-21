# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""SPDX 2.x specific data extraction adapter."""

from spdx_tools.spdx.model.document import Document
from spdx_tools.spdx.model.relationship import RelationshipType
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.validation.validation_message import ValidationMessage

from .adapter_interface import SbomAdapter


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
            if package.spdx_id in reachable_ids
            and (
                package.name is None
                or (isinstance(package.name, str) and package.name.strip() == "")
            )
        ]

    def get_components_without_versions(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids
            and (
                package.version is None
                or isinstance(package.version, SpdxNoAssertion)
                or (isinstance(package.version, str) and package.version.strip() == "")
            )
        ]

    def get_components_without_suppliers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids
            and (
                package.supplier is None
                or isinstance(package.supplier, SpdxNoAssertion)
                or (
                    isinstance(package.supplier, str) and package.supplier.strip() == ""
                )
            )
        ]

    def get_components_without_identifiers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id is None
            or (isinstance(package.spdx_id, str) and package.spdx_id.strip() == "")
        ]

    def get_components_without_concluded_licenses(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        # Note: concluded license is mandatory in SPDX-2.2 and SPDX-2.3
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids
            and (
                package.license_concluded is None
                or isinstance(package.license_concluded, SpdxNoAssertion)
                or (
                    isinstance(package.license_concluded, str)
                    and package.license_concluded.strip() == ""
                )
            )
        ]

    def get_components_without_copyright_texts(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return [
            (package.name or "", package.spdx_id or "")
            for package in getattr(self.doc, "packages", [])
            if package.spdx_id in reachable_ids
            and (
                package.copyright_text is None
                or isinstance(package.copyright_text, SpdxNoAssertion)
                or (
                    isinstance(package.copyright_text, str)
                    and package.copyright_text.strip() == ""
                )
            )
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
