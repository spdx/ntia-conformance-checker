# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Adapter for when parsing fails."""

from spdx_tools.spdx.validation.validation_message import ValidationMessage

from .adapter_interface import SbomAdapter


class NullAdapter(SbomAdapter):
    """Adapter returning defaults, used when parsing fails."""

    def get_doc_spec_version(self) -> str | None:
        return None

    def check_author(self) -> bool:
        return False

    def check_timestamp(self) -> bool:
        return False

    def get_sbom_name(self) -> str:
        return ""

    def get_components_without_names(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return []

    def get_components_without_versions(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return []

    def get_components_without_suppliers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return []

    def get_components_without_identifiers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return []

    def get_components_without_concluded_licenses(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return []

    def get_components_without_copyright_texts(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        return []

    def check_dependency_relationships(self) -> bool:
        return False

    def get_total_number_components(self) -> int:
        return 0

    def get_sbom_types(
        self, conformance_messages: list[ValidationMessage]
    ) -> list[str]:
        return []
