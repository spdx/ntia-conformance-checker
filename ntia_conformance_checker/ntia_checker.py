# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""NTIA Minimum Elements checking functionality."""

from __future__ import annotations

import warnings

from .base_checker import BaseChecker
from .spec import Spec, SpecCategory, SpecRule

# General URL for the NTIA Minimum Elements standard.  Used as the fallback
# help URL for every rule in the NTIA catalogue.
NTIA_HELP_URI = (
    "https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom"
)

# Categories defined by NTIA §IV.  See RULES.md for the namespace plan;
# only ``data-fields`` has active rules today.
NTIA_CATEGORIES: tuple[SpecCategory, ...] = (
    SpecCategory(
        id="data-fields",
        code="DF",
        title="Data Fields",
        description="Baseline information about each component that should be tracked.",
    ),
    SpecCategory(
        id="automation-support",
        code="AS",
        title="Automation Support",
        description="Support for automation including machine-readable formats.",
    ),
    SpecCategory(
        id="practices-and-processes",
        code="PP",
        title="Practices and Processes",
        description="Operational practices for SBOM creation, exchange, and consumption.",
    ),
)

# Component-level Data Fields rules (NTIA-DF-01..04).
NTIA_COMPONENT_RULES: tuple[SpecRule, ...] = (
    SpecRule(
        category="data-fields",
        number=1,
        slug="ntia-supplier-name",
        element_id="supplier",
        sarif_rule_name="NtiaComponentSupplierMissing",
        attr="components_without_suppliers",
        label="All component suppliers provided?",
        kind="list",
        description="component supplier",
        warning="An SBOM component should have a supplier name.",
        ref_section="IV",
        ref_title="Data Fields -- Supplier Name",
        ref_url=NTIA_HELP_URI,
        json_key="componentSuppliers",
    ),
    SpecRule(
        category="data-fields",
        number=2,
        slug="ntia-component-name",
        element_id="name",
        sarif_rule_name="NtiaComponentNameMissing",
        attr="components_without_names",
        label="All component names provided?",
        kind="list",
        description="component name",
        warning="An SBOM component should have a name.",
        ref_section="IV",
        ref_title="Data Fields -- Component Name",
        ref_url=NTIA_HELP_URI,
        json_key="componentNames",
    ),
    SpecRule(
        category="data-fields",
        number=3,
        slug="ntia-component-version",
        element_id="version",
        sarif_rule_name="NtiaComponentVersionMissing",
        attr="components_without_versions",
        label="All component versions provided?",
        kind="list",
        description="component version",
        warning="An SBOM component should have a version.",
        ref_section="IV",
        ref_title="Data Fields -- Version of the Component",
        ref_url=NTIA_HELP_URI,
        json_key="componentVersions",
    ),
    SpecRule(
        category="data-fields",
        number=4,
        slug="ntia-unique-identifier",
        element_id="identifier",
        sarif_rule_name="NtiaComponentIdentifierMissing",
        attr="components_without_identifiers",
        label="All component identifiers provided?",
        kind="list",
        description="component identifier",
        warning="An SBOM component should have a unique identifier.",
        ref_section="IV",
        ref_title="Data Fields -- Other Unique Identifiers",
        ref_url=NTIA_HELP_URI,
        json_key="componentIdentifiers",
    ),
)

# Document-level Data Fields rules (NTIA-DF-05..07).
NTIA_DOCUMENT_RULES: tuple[SpecRule, ...] = (
    SpecRule(
        category="data-fields",
        number=5,
        slug="ntia-dependency-relationship",
        element_id="dependency_relationship",
        sarif_rule_name="NtiaDependencyRelationshipsMissing",
        attr="dependency_relationships",
        label="Dependency relationships provided?",
        kind="bool",
        description="dependency relationships",
        warning="An SBOM should declare dependency relationships.",
        ref_section="IV",
        ref_title="Data Fields -- Dependency Relationship",
        ref_url=NTIA_HELP_URI,
        json_key="dependencyRelationshipsProvided",
    ),
    SpecRule(
        category="data-fields",
        number=6,
        slug="ntia-sbom-author",
        element_id="author",
        sarif_rule_name="NtiaSbomAuthorMissing",
        attr="doc_author",
        label="SBOM author name provided?",
        kind="bool",
        description="SBOM author",
        warning="An SBOM should have an author name.",
        ref_section="IV",
        ref_title="Data Fields -- Author of SBOM Data",
        ref_url=NTIA_HELP_URI,
        json_key="authorNameProvided",
    ),
    SpecRule(
        category="data-fields",
        number=7,
        slug="ntia-sbom-timestamp",
        element_id="timestamp",
        sarif_rule_name="NtiaSbomTimestampMissing",
        attr="doc_timestamp",
        label="SBOM creation timestamp provided?",
        kind="bool",
        description="SBOM creation timestamp",
        warning="An SBOM should have a creation timestamp.",
        ref_section="IV",
        ref_title="Data Fields -- Timestamp",
        ref_url=NTIA_HELP_URI,
        json_key="timestampProvided",
    ),
)


class NTIAChecker(BaseChecker):
    """
    NTIA Minimum Elements check.

    See:
        https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
    """

    MIN_ELEMENTS = ["name", "version", "identifier", "supplier"]

    _SPEC: Spec = Spec(
        standard_id="ntia",
        spec_code="NTIA",
        title="NTIA Minimum Elements",
        help_uri=NTIA_HELP_URI,
        sarif_taxonomy_name="ntia-minimum-elements",
        sarif_clause_taxonomy_name="ntia-clauses",
        categories=NTIA_CATEGORIES,
        rules=NTIA_COMPONENT_RULES + NTIA_DOCUMENT_RULES,
    )

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str = "ntia",
        sbom_spec: str = "spdx2",
    ):
        """
        Initialize the NTIA Minimum Element Checker.

        Args:
            file (str): The name of the file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used.
            sbom_spec (str): The SBOM specification to be used.
        """
        super().__init__(
            file=file, validate=validate, compliance=compliance, sbom_spec=sbom_spec
        )

        if compliance not in {"ntia"}:
            raise ValueError("Only NTIA Minimum Element compliance is supported.")

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
            ("SBOM author name provided?", self.doc_author),
            ("SBOM creation timestamp provided?", self.doc_timestamp),
            ("Dependency relationships provided?", self.dependency_relationships),
        ]

    def check_compliance(self) -> bool:
        """Check overall compliance with NTIA minimum elements."""
        return all(
            [
                self.doc_author,
                self.doc_timestamp,
                self.dependency_relationships,
                not self.components_without_names,
                not self.components_without_versions,
                not self.components_without_identifiers,
                not self.components_without_suppliers,
                not self.validation_messages,
            ]
        )

    def check_ntia_minimum_elements_compliance(self) -> bool:
        """Check overall compliance with NTIA minimum elements.

        This method is kept for backward compatibility.
        Please consider using check_compliance() instead."""
        warnings.warn(
            "NTIAChecker.check_ntia_minimum_elements_compliance is deprecated; "
            "use check_compliance() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.check_compliance()
