# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""CISA Framing Software Component Transparency checking functionality."""

from __future__ import annotations

from .base_checker import BaseChecker


class FSCT3Checker(BaseChecker):
    """
    2024 CISA Framing Software Component Transparency (minimum expectation) checker.

    A set of Baseline Attributes is defined in Section 2.2 of
    Framing Software Component Transparency:
    Establishing a Common Software Bill of Materials (SBOM) Third Edition.

    There are three maturity levels (Minimum Expected, Recommended Practice,
    and Aspirational Goal) for content provided in Attribute entries.

    This checker currently only checks for Minimum Expected maturity level.

    See:
        https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024
    """

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str = "fsct3-min",
        sbom_spec: str = "spdx2",
    ):
        """
        Initialize the checker.

        Args:
            file (str): The name of the file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used.
            sbom_spec (str): The SBOM specification to be used.
        """
        super().__init__(
            file=file, validate=validate, compliance=compliance, sbom_spec=sbom_spec
        )

        if compliance not in {"fsct3-min"}:
            raise ValueError("Only FSCTv3 Minimum Expected compliance is supported.")

        if self.doc:
            self.compliant = self.check_compliance()

            # for backward compatibility
            self.ntia_minimum_elements_compliant = self.compliant

    def check_compliance(self) -> bool:
        """Check overall compliance"""
        return all(
            [
                self.doc_author,
                self.doc_timestamp,
                self.dependency_relationships,
                not self.components_without_names,
                not self.components_without_versions,
                not self.components_without_identifiers,
                not self.components_without_suppliers,
                not self.components_without_concluded_licenses,
                not self.components_without_copyright_texts,
                not self.validation_messages,
            ]
        )

    def print_components_missing_info(self, attributes=None) -> None:
        """Print detailed info about which components have missing info."""
        super().print_components_missing_info(
            attributes=[
                "name",
                "version",
                "identifier",
                "supplier",
                "concluded_license",
                "copyright_text",
            ]
        )

    def print_table_output(self, verbose: bool = False, table_elements=None) -> None:
        """Print element-by-element result table."""
        super().print_table_output(
            verbose=verbose,
            table_elements=[
                ("All component names provided?", not self.components_without_names),
                (
                    "All component versions provided?",
                    not self.components_without_versions,
                ),
                (
                    "All component identifiers provided?",
                    not self.components_without_identifiers,
                ),
                (
                    "All component suppliers provided?",
                    not self.components_without_suppliers,
                ),
                (
                    "All component concluded license provided?",
                    not self.components_without_concluded_licenses,
                ),
                (
                    "All component copyright notice provided?",
                    not self.components_without_copyright_texts,
                ),
                ("SBOM author name provided?", self.doc_author),
                ("SBOM creation timestamp provided?", self.doc_timestamp),
                ("Dependency relationships provided?", self.dependency_relationships),
            ],
        )

    def output_html(self, table_elements=None) -> str:
        """Create element-by-element result table in HTML."""
        return super().output_html(
            table_elements=[
                ("All component names provided", not self.components_without_names),
                (
                    "All component versions provided",
                    not self.components_without_versions,
                ),
                (
                    "All component identifiers provided",
                    not self.components_without_identifiers,
                ),
                (
                    "All component suppliers provided",
                    not self.components_without_suppliers,
                ),
                (
                    "All component concluded license provided",
                    not self.components_without_concluded_licenses,
                ),
                (
                    "All component copyright notice provided",
                    not self.components_without_copyright_texts,
                ),
                ("SBOM author name provided", self.doc_author),
                ("SBOM creation timestamp provided", self.doc_timestamp),
                ("Dependency relationships provided", self.dependency_relationships),
            ],
        )
