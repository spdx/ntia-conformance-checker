# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""FSCT Common BOM checking functionality."""

from __future__ import annotations

from .base_checker import BaseChecker
from .spec import Spec, SpecCategory, SpecRule

# General URL for the FSCTv3 Common BOM standard.
FSCT3_HELP_URI = (
    "https://www.cisa.gov/resources-tools/resources/"
    "framing-software-component-transparency-2024"
)

# Categories defined by FSCT §2.2 / §2.3.  See RULES.md for the namespace
# plan; ``sbom-meta-information`` and ``component-attributes`` carry active
# rules; ``undeclared-sbom-data`` is reserved for future checks.
FSCT_CATEGORIES: tuple[SpecCategory, ...] = (
    SpecCategory(
        id="sbom-meta-information",
        code="META",
        title="SBOM Meta-Information",
        description="Meta-information about the SBOM itself (§2.2.1).",
    ),
    SpecCategory(
        id="component-attributes",
        code="COMP",
        title="Component Attributes",
        description="Per-component baseline attributes (§2.2.2).",
    ),
    SpecCategory(
        id="undeclared-sbom-data",
        code="UNDEC",
        title="Undeclared SBOM Data",
        description="Handling of unknown / redacted / missing data (§2.3).",
    ),
)

# Meta-information rules (FSCT-META-01..04, §2.2.1).
_FSCT_META_RULES: tuple[SpecRule, ...] = (
    SpecRule(
        category="sbom-meta-information",
        number=1,
        slug="fsct-author-name",
        element_id="author",
        sarif_rule_name="FsctAuthorNameMissing",
        attr="doc_author",
        label="SBOM author name provided?",
        kind="bool",
        description="SBOM author",
        warning="An SBOM should have an author name.",
        ref_section="2.2.1.1",
        ref_title="Author Name",
        ref_url=FSCT3_HELP_URI,
        json_key="authorNameProvided",
    ),
    SpecRule(
        category="sbom-meta-information",
        number=2,
        slug="fsct-timestamp",
        element_id="timestamp",
        sarif_rule_name="FsctTimestampMissing",
        attr="doc_timestamp",
        label="SBOM creation timestamp provided?",
        kind="bool",
        description="SBOM creation timestamp",
        warning="An SBOM should have a creation timestamp.",
        ref_section="2.2.1.2",
        ref_title="Timestamp",
        ref_url=FSCT3_HELP_URI,
        json_key="timestampProvided",
    ),
    SpecRule(
        category="sbom-meta-information",
        number=3,
        slug="fsct-sbom-type",
        element_id="type",
        sarif_rule_name="FsctSbomTypeMissing",
        attr="_fsct_sbom_type",  # not implemented; catalogue-only
        label="SBOM Type provided?",
        kind="bool",
        description="SBOM type",
        warning="An SBOM should declare its type.",
        ref_section="2.2.1.3",
        ref_title="Type",
        ref_url=FSCT3_HELP_URI,
        maturity="aspirational",
        status="catalogue-only",
    ),
    SpecRule(
        category="sbom-meta-information",
        number=4,
        slug="fsct-primary-component",
        element_id="primary_component",
        sarif_rule_name="FsctPrimaryComponentMissing",
        attr="_fsct_primary_component",  # not implemented; catalogue-only
        label="Primary Component (root of dependencies) provided?",
        kind="bool",
        description="primary component (root of dependencies)",
        warning="An SBOM should identify a primary component.",
        ref_section="2.2.1.4",
        ref_title="Primary Component (or Root of Dependencies)",
        ref_url=FSCT3_HELP_URI,
        status="catalogue-only",
    ),
)

# Component-attribute rules (FSCT-COMP-01..08, §2.2.2).
_FSCT_COMP_RULES: tuple[SpecRule, ...] = (
    SpecRule(
        category="component-attributes",
        number=1,
        slug="fsct-component-name",
        element_id="name",
        sarif_rule_name="FsctComponentNameMissing",
        attr="components_without_names",
        label="All component names provided?",
        kind="list",
        description="component name",
        warning="An SBOM component should have a name.",
        ref_section="2.2.2.1",
        ref_title="Component Name",
        ref_url=FSCT3_HELP_URI,
        json_key="componentNames",
    ),
    SpecRule(
        category="component-attributes",
        number=2,
        slug="fsct-component-version",
        element_id="version",
        sarif_rule_name="FsctComponentVersionMissing",
        attr="components_without_versions",
        label="All component versions provided?",
        kind="list",
        description="component version",
        warning="An SBOM component should have a version.",
        ref_section="2.2.2.2",
        ref_title="Version",
        ref_url=FSCT3_HELP_URI,
        json_key="componentVersions",
    ),
    SpecRule(
        category="component-attributes",
        number=3,
        slug="fsct-supplier-name",
        element_id="supplier",
        sarif_rule_name="FsctSupplierNameMissing",
        attr="components_without_suppliers",
        label="All component suppliers provided?",
        kind="list",
        description="component supplier",
        warning="An SBOM component should have a supplier name.",
        ref_section="2.2.2.3",
        ref_title="Supplier Name",
        ref_url=FSCT3_HELP_URI,
        json_key="componentSuppliers",
    ),
    SpecRule(
        category="component-attributes",
        number=4,
        slug="fsct-unique-identifier",
        element_id="identifier",
        sarif_rule_name="FsctUniqueIdentifierMissing",
        attr="components_without_identifiers",
        label="All component identifiers provided?",
        kind="list",
        description="component identifier",
        warning="An SBOM component should have a unique identifier.",
        ref_section="2.2.2.4",
        ref_title="Unique Identifier",
        ref_url=FSCT3_HELP_URI,
        json_key="componentIdentifiers",
    ),
    SpecRule(
        category="component-attributes",
        number=5,
        slug="fsct-cryptographic-hash",
        element_id="cryptographic_hash",
        sarif_rule_name="FsctCryptographicHashMissing",
        attr="_fsct_components_without_hashes",  # not implemented; catalogue-only
        label="All component cryptographic hashes provided?",
        kind="list",
        description="component cryptographic hash",
        warning="An SBOM component should have a cryptographic hash.",
        ref_section="2.2.2.5",
        ref_title="Cryptographic Hash",
        ref_url=FSCT3_HELP_URI,
        status="catalogue-only",
    ),
    SpecRule(
        category="component-attributes",
        number=6,
        slug="fsct-relationship",
        element_id="relationship",
        sarif_rule_name="FsctRelationshipMissing",
        attr="_fsct_components_without_relationships",  # not implemented
        label="All component relationships provided?",
        kind="list",
        description="component relationship and completeness",
        warning="An SBOM component should declare its relationship and completeness.",
        ref_section="2.2.2.6",
        ref_title="Relationship",
        ref_url=FSCT3_HELP_URI,
        status="catalogue-only",
    ),
    SpecRule(
        category="component-attributes",
        number=7,
        slug="fsct-concluded-license",
        element_id="concluded_license",
        sarif_rule_name="FsctConcludedLicenseMissing",
        attr="components_without_concluded_licenses",
        label="All component concluded license provided?",
        kind="list",
        description="component concluded license",
        warning="An SBOM component should have a concluded license.",
        ref_section="2.2.2.7",
        ref_title="License",
        ref_url=FSCT3_HELP_URI,
        json_key="componentConcludedLicenses",
    ),
    SpecRule(
        category="component-attributes",
        number=8,
        slug="fsct-copyright-notice",
        element_id="copyright_text",
        sarif_rule_name="FsctCopyrightNoticeMissing",
        attr="components_without_copyright_texts",
        label="All component copyright notice provided?",
        kind="list",
        description="component copyright text",
        warning="An SBOM component should have a copyright notice.",
        ref_section="2.2.2.8",
        ref_title="Copyright Notice",
        ref_url=FSCT3_HELP_URI,
        json_key="componentCopyrightNotices",
    ),
)

# Full FSCT3 rule catalogue.
FSCT_RULES: tuple[SpecRule, ...] = _FSCT_META_RULES + _FSCT_COMP_RULES


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
        standard_id="fsct3-min",
        spec_code="FSCT",
        title="FSCTv3 Common BOM (Minimum Expected)",
        help_uri=FSCT3_HELP_URI,
        sarif_taxonomy_name="fsct-baseline-attributes",
        sarif_clause_taxonomy_name="fsct-clauses",
        categories=FSCT_CATEGORIES,
        rules=FSCT_RULES,
    )

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
