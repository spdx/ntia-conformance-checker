# SPDX-FileCopyrightText: 2024-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""FSCT Common BOM checking functionality."""

from __future__ import annotations

from dataclasses import replace

from .base_checker import BaseChecker
from .ntia_checker import NTIA_COMPONENT_RULES, NTIA_DOCUMENT_RULES
from .spec import Spec, SpecRule, SpecTaxon

# URL for the FSCTv3 baseline attributes standard.
FSCT3_HELP_URI = (
    "https://www.cisa.gov/resources-tools/resources/"
    "framing-software-component-transparency-2024"
)

# Component-level rules added by FSCT3 on top of the NTIA baseline.
# These are Component Attributes (section 2.2.2) so they carry that cluster.
FSCT3_EXTRA_COMPONENT_RULES: tuple[SpecRule, ...] = (
    SpecRule(
        element_id="concluded_license",
        element_name="component concluded license",
        report_label="All component concluded license provided?",
        kind="list",
        cluster="component-attributes",
        attr="components_without_concluded_licenses",
        getter="get_components_without_concluded_licenses",
        json_key="componentConcludedLicenses",
        sarif_rule_id="fsct3.component.concluded-license",
        sarif_rule_name="ComponentConcludedLicenseMissing",
    ),
    SpecRule(
        element_id="copyright_text",
        element_name="component copyright text",
        report_label="All component copyright notice provided?",
        kind="list",
        cluster="component-attributes",
        attr="components_without_copyright_texts",
        getter="get_components_without_copyright_texts",
        json_key="componentCopyrightTexts",
        sarif_rule_id="fsct3.component.copyright-text",
        sarif_rule_name="ComponentCopyrightTextMissing",
    ),
)

# FSCT3-specific copies of the shared NTIA rules, tagged with their section cluster.
_FSCT3_COMPONENT_RULES: tuple[SpecRule, ...] = tuple(
    replace(r, cluster="component-attributes") for r in NTIA_COMPONENT_RULES
)
_FSCT3_DOCUMENT_RULES: tuple[SpecRule, ...] = tuple(
    replace(r, cluster="sbom-meta-information") for r in NTIA_DOCUMENT_RULES
)


class FSCT3Checker(BaseChecker):
    """FSCTv3 checker.

    A set of Baseline Attributes is defined in Section 2.2 of
    Framing Software Component Transparency:
    Establishing a Common Software Bill of Materials (SBOM) Third Edition.

    There are three maturity levels (Minimum Expected, Recommended Practice,
    and Aspirational Goal) for content provided in Attribute entries.

    This checker currently only checks for Minimum Expected maturity level.

    See:
        https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024
    """

    MIN_ELEMENTS = [
        "name",
        "version",
        "identifier",
        "supplier",
        "concluded_license",
        "copyright_text",
    ]

    _SPEC: Spec = Spec(
        standard_short_id="fsct3-min",
        standard_id="2024-cisa-baseline-attributes-minimum-expected",
        standard_name=(
            "2024 CISA Framing Software Component Transparency (Minimum Expected)"
        ),
        rules=_FSCT3_DOCUMENT_RULES
        + _FSCT3_COMPONENT_RULES
        + FSCT3_EXTRA_COMPONENT_RULES,
        help_uri=FSCT3_HELP_URI,
        taxa=(
            SpecTaxon(
                taxon_id="sbom-meta-information",
                taxon_name="SBOM Meta-Information",
            ),
            SpecTaxon(
                taxon_id="component-attributes",
                taxon_name="Component Attributes",
            ),
        ),
    )

    @property
    def spec(self) -> Spec:
        """The FSCT3 compliance specification for this checker."""
        return self._SPEC

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str = "fsct3-min",
        sbom_spec: str = "spdx2",
    ):
        """
        Initialize the FSCTv3 checker.

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

        self.table_elements = [
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
        ]

    def check_compliance(self) -> bool:
        """Check overall compliance with FSCTv3 Minimum Expected"""
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
