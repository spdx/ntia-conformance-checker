# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""FSCT Common BOM checking functionality."""

from __future__ import annotations

from .base_checker import BaseChecker


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

            # for backward compatibility
            self.ntia_minimum_elements_compliant = self.compliant

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

    def output_html(self) -> str:
        """Create a HTML of results."""
        if self.doc:
            result = (
                f"<h2>FSCTv3 Minimum Expected Conformance Results</h2>"
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
                f"<tr> <td>All component concluded license provided</td> "
                f"<td>{not self.components_without_concluded_licenses}</td> "
                f"<tr> <td>All component copyright notice provided</td> "
                f"<td>{not self.components_without_copyright_texts}</td> "
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
            <h2>FSCTv3 Minimum Expected Conformance Results</h2>
            <h3>Conformant: {self.compliant}</h3>
            <p>The provided document couldn't be parsed, check for baseline attributes couldn't be performed.</p>
            <p>The following SPDXParsingError was raised:<p><ul>"""
            for error in self.parsing_error:
                result += f"""<li>{error}</li>"""

            result += """</ul>"""

        return result
