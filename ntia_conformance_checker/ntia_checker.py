# SPDX-FileCopyrightText: 2024-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""NTIA Minimum Elements checking functionality."""

from __future__ import annotations

import warnings

from .base_checker import BaseChecker
from .spec import Spec, SpecRule, SpecTaxon

# URL for the NTIA Minimum Elements standard.
# Used as the fallback help URL for every rule in the NTIA catalogue.
NTIA_HELP_URI = (
    "https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom"
)

# Document-level rules
# We need a uniform naming convention for rule ids.
# ---
# From https://sarifweb.azurewebsites.net/Validation
# SARIF2009: Adopt uniform naming conventions for rule ids.
# Many tools follow a conventional format for the 'reportingDescriptor.id'
# property: a short string identifying the tool concatenated with a numeric
# rule number, for example, 'CS2001' for a diagnostic from the Roslyn C#
# compiler. For uniformity of experience across tools, we recommend this
# format.
NTIA_DOCUMENT_RULES: tuple[SpecRule, ...] = (
    SpecRule(
        element_id="doc_author",
        element_name="SBOM author",
        report_label="SBOM author name provided?",
        kind="bool",
        attr="doc_author",
        getter="check_author",
        json_key="authorNameProvided",
        sarif_rule_id="ntia.document.author",
        sarif_rule_name="DocumentAuthorMissing",
    ),
    SpecRule(
        element_id="doc_timestamp",
        element_name="SBOM creation timestamp",
        report_label="SBOM creation timestamp provided?",
        kind="bool",
        attr="doc_timestamp",
        getter="check_timestamp",
        json_key="timestampProvided",
        sarif_rule_id="ntia.document.timestamp",
        sarif_rule_name="DocumentTimestampMissing",
    ),
    SpecRule(
        element_id="dependency_relationships",
        element_name="dependency relationships",
        report_label="Dependency relationships provided?",
        kind="bool",
        attr="dependency_relationships",
        getter="check_dependency_relationships",
        json_key="dependencyRelationshipsProvided",
        sarif_rule_id="ntia.document.dependency-relationships",
        sarif_rule_name="DocumentDependencyRelationshipsMissing",
    ),
)

# Component-level rules
NTIA_COMPONENT_RULES: tuple[SpecRule, ...] = (
    SpecRule(
        element_id="name",
        element_name="component name",
        report_label="All component names provided?",
        kind="list",
        attr="components_without_names",
        getter="get_components_without_names",
        json_key="componentNames",
        sarif_rule_id="ntia.component.name",
        sarif_rule_name="ComponentNameMissing",
    ),
    SpecRule(
        element_id="version",
        element_name="component version",
        report_label="All component versions provided?",
        kind="list",
        attr="components_without_versions",
        getter="get_components_without_versions",
        json_key="componentVersions",
        sarif_rule_id="ntia.component.version",
        sarif_rule_name="ComponentVersionMissing",
    ),
    SpecRule(
        element_id="identifier",
        element_name="component identifier",
        report_label="All component identifiers provided?",
        kind="list",
        attr="components_without_identifiers",
        getter="get_components_without_identifiers",
        json_key="componentIdentifiers",
        sarif_rule_id="ntia.component.identifier",
        sarif_rule_name="ComponentIdentifierMissing",
    ),
    SpecRule(
        element_id="supplier",
        element_name="component supplier",
        report_label="All component suppliers provided?",
        kind="list",
        attr="components_without_suppliers",
        getter="get_components_without_suppliers",
        json_key="componentSuppliers",
        sarif_rule_id="ntia.component.supplier",
        sarif_rule_name="ComponentSupplierMissing",
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
        standard_short_id="ntia",
        standard_id="2021-ntia-sbom-minimum-elements",
        standard_name="2021 NTIA SBOM Minimum Elements",
        rules=NTIA_DOCUMENT_RULES + NTIA_COMPONENT_RULES,
        help_uri=NTIA_HELP_URI,
        taxa=(
            SpecTaxon(
                taxon_id="minimum-elements",
                taxon_name="Minimum Elements",
            ),
        ),
    )

    @property
    def spec(self) -> Spec:
        """The NTIA compliance specification for this checker."""
        return self._SPEC

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
