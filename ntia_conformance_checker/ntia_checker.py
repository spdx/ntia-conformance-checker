# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""NTIA Minimum Elements checking functionality."""

from __future__ import annotations

import warnings
from typing import Any, Dict

from .base_checker import BaseChecker


class NTIAChecker(BaseChecker):
    """NTIA Minimum Elements check."""

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
            self.sbom_name = self.get_sbom_name()
            self.doc_version = self.check_doc_version()
            self.doc_author = True  # Assume author is present?
            self.doc_timestamp = True  # Assume timestamp is present?
            self.dependency_relationships = self.check_dependency_relationships()
            self.compliant = self.check_compliance()

            # for backward compatibility
            self.ntia_minimum_elements_compliant = self.compliant

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

    def print_components_missing_info(self) -> None:
        """Print detailed info about which components are missing info."""
        if not self.parsing_error:
            if all(
                [
                    not self.components_without_names,
                    not self.components_without_versions,
                    not self.components_without_identifiers,
                    not self.components_without_suppliers,
                ]
            ):
                print("No components with missing information.")
            if self.components_without_names:
                print(
                    f"Components missing a name: {', '.join(self.components_without_names)}"
                )
                print()
            if self.components_without_versions:
                print(
                    f"Components missing a version: {', '.join(self.components_without_versions)}"
                )
                print()
            if self.components_without_identifiers:
                print(
                    f"Components missing an identifier: "
                    f"{', '.join(self.components_without_identifiers)}"
                )
                print()
            if self.components_without_suppliers:
                print(
                    f"Components missing a supplier: {', '.join(self.components_without_suppliers)}"
                )
                print()

    def print_table_output(self, verbose: bool = False) -> None:
        """Print element-by-element result table."""
        # pylint: disable=line-too-long
        if self.parsing_error:
            print(f"\nIs this SBOM NTIA minimum element conformant? {self.compliant}\n")
            print(
                "The provided document couldn't be parsed, check for ntia minimum elements couldn't be performed.\n"
            )
            print("The following SPDXParsingError was raised:\n")
            for error in self.parsing_error:
                print(error)

        else:
            print(f"\nIs this SBOM NTIA minimum element conformant? {self.compliant}\n")
            print("Individual elements                            | Status")
            print("-------------------------------------------------------")
            print(
                f"All component names provided?                  | {not self.components_without_names}"
            )
            print(
                f"All component versions provided?               | {not self.components_without_versions}"
            )
            print(
                f"All component identifiers provided?            | {not self.components_without_identifiers}"
            )
            print(
                f"All component suppliers provided?              | {not self.components_without_suppliers}"
            )
            print(f"SBOM author name provided?                     | {self.doc_author}")
            print(
                f"SBOM creation timestamp provided?              | {self.doc_timestamp}"
            )
            print(
                f"Dependency relationships provided?             | {self.dependency_relationships}\n"
            )
            if self.validation_messages:
                print(
                    "The provided document is not valid according to the SPDX specification. "
                    "The following errors were found:\n"
                )
                for msg in self.validation_messages:
                    if msg.validation_message:
                        print(msg.validation_message)
                        if verbose and msg.context:
                            print(f"- SPDX ID: {msg.context.spdx_id}")
                            print(f"- Parent ID: {msg.context.parent_id}")
                            print(f"- Element type: {msg.context.element_type}")
                        print()

    def output_json(self) -> Dict[str, Any]:
        """Create a dict of results for outputting to JSON."""
        # instantiate dict and fields that have > 1 level
        result: Dict[str, Any] = {}

        result["isConformant"] = self.compliant
        result["isNtiaConformant"] = self.compliant  # for backward compatibility

        result["complianceStandard"] = self.compliance_standard
        result["sbomSpec"] = self.sbom_spec

        result["validationMessages"] = []
        if self.validation_messages:
            result["validationMessages"] = list(map(str, self.validation_messages))

        result["parsingError"] = self.parsing_error

        result["sbomName"] = self.sbom_name
        result["componentNames"] = {}
        result["componentVersions"] = {}
        result["componentIdentifiers"] = {}
        result["componentSuppliers"] = {}
        result["componentConcludedLicenses"] = {}
        result["componentCopyrightTexts"] = {}

        result["specVersionProvided"] = self.doc_version
        result["authorNameProvided"] = self.doc_author
        result["timestampProvided"] = self.doc_timestamp
        result["dependencyRelationshipsProvided"] = self.dependency_relationships

        result["componentNames"][
            "nonconformantComponents"
        ] = self.components_without_names
        result["componentNames"]["allProvided"] = not self.components_without_names

        result["componentVersions"][
            "nonconformantComponents"
        ] = self.components_without_versions
        result["componentVersions"][
            "allProvided"
        ] = not self.components_without_versions

        result["componentIdentifiers"][
            "nonconformantComponents"
        ] = self.components_without_identifiers
        result["componentIdentifiers"][
            "allProvided"
        ] = not self.components_without_identifiers

        result["componentSuppliers"][
            "nonconformantComponents"
        ] = self.components_without_suppliers
        result["componentSuppliers"][
            "allProvided"
        ] = not self.components_without_suppliers

        result["componentConcludedLicenses"][
            "nonconformantComponents"
        ] = self.components_without_concluded_licenses
        result["componentConcludedLicenses"][
            "allProvided"
        ] = not self.components_without_concluded_licenses

        result["componentCopyrightTexts"][
            "nonconformantComponents"
        ] = self.components_without_copyright_texts
        result["componentCopyrightTexts"][
            "allProvided"
        ] = not self.components_without_copyright_texts

        result["totalNumberComponents"] = self.get_total_number_components()

        return result

    def output_html(self) -> str:
        """Create a HTML of results."""
        if self.doc:
            result = (
                f" <h2>NTIA Conformance Results</h2> "
                f"<h3>Conformant: {self.compliant}</h3>"
                f"<table> <tr> "
                f"<th>Individual Elements</th> <th>Conformant</th> </tr> "
                f"<tr> <td>All component names provided</td>"
                f" <td>{not self.components_without_names}</td> </tr> "
                f"<tr> <td>All component versions provided</td>"
                f" <td>{not self.components_without_versions}</td> </tr> "
                f"<tr> <td>All component identifiers provided</td> "
                f"<td>{not self.components_without_identifiers}</td> </tr> "
                f"<tr> <td>All component suppliers provided</td> "
                f"<td>{not self.components_without_suppliers}</td> "
                f"</tr> <tr> <td>SBOM author name provided</td> "
                f"<td>{self.doc_author}</td> </tr> "
                f"<tr> <td>SBOM creation timestamp provided</td> "
                f"<td>{self.doc_timestamp}</td> </tr> "
                f"<tr> <td>Dependency relationships provided?</td> "
                f"<td>{self.dependency_relationships}</td> </tr> "
                f"</table>"
            )

            if self.validation_messages:
                result += (
                    "<p>The provided document is not valid according to the SPDX specification. "
                    "The following errors were found:</p>\n"
                )
                result += "<ul>\n"
                for msg in self.validation_messages:
                    if msg.validation_message:
                        result += "<li>\n"
                        result += "<p><strong>Validation message:</strong></p>\n"
                        result += f"<p>{msg.validation_message}</p>\n"
                        if msg.context:
                            result += "<p><strong>Validation context:</strong></p>\n"
                            result += "<ul>\n"
                            result += f"<li>SPDX ID: {msg.context.spdx_id}</li>\n"
                            result += f"<li>Parent ID: {msg.context.parent_id}</li>\n"
                            result += (
                                f"<li>Element type: {msg.context.element_type}</li>\n"
                            )
                            result += "</ul>\n"
                        result += "</li>\n"
                result += "</ul>\n"
        else:
            result = f"""
            <h2>NTIA Conformance Results</h2>
            <h3>Conformant: {self.compliant}</h3>
            <p>The provided document couldn't be parsed, check for NTIA Minimum Elements couldn't be performed.</p>
            <p>The following SPDXParsingError was raised:<p><ul>"""
            for error in self.parsing_error:
                result += f"""<li>{error}</li>"""

            result += """</ul>"""

        return result
