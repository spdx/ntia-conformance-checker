# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""FSCT Common BOM checking functionality."""

from spdx_tools.spdx.model import RelationshipType

from .base_checker import BaseChecker


class FSCT3Checker(BaseChecker):
    """FSCT Common SBOM Third Edition checker.

    A set of Baseline Attributes is defined in Section 2.2 of
    Framing Software Component Transparency:
    Establishing a Common Software Bill of Materials (SBOM) Third Edition.

    There are three maturity levels (Minimum Expected, Recommended Practice,
    and Aspirational Goal) for content provided in Attribute entries.

    See:
    https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024
    """

    def __init__(self, file, validate=True, compliance="fsct3-min"):
        super().__init__(file=file, validate=validate)

        if compliance != "fsct3-min":
            raise ValueError("Only FSCTv3 Minimum Expected compliance is supported.")

        if self.doc:
            self.sbom_name = self.doc.creation_info.name
            self.doc_version = self.check_doc_version()
            self.doc_author = True  # Assume author is present?
            self.doc_timestamp = True  # Assume timestamp is present?
            self.dependency_relationships = self.check_dependency_relationships()
            self.compliant = self.check_compliance()

    def check_doc_version(self):
        """Check for SPDX document version."""
        if str(self.doc.creation_info.spdx_version) not in ["SPDX-2.2", "SPDX-2.3"]:
            return False
        return True

    def check_dependency_relationships(self):
        """Check that the document DESCRIBES at least one package."""
        describes_relationships = [
            rel
            for rel in self.doc.relationships
            if rel.relationship_type == RelationshipType.DESCRIBES
        ]

        # A set of all package spdx_ids for quick lookup
        spdx_id_set = {package.spdx_id for package in self.doc.packages}

        # Check if any of the "DESCRIBES" relationships describe a Package
        describes_package = any(
            rel.related_spdx_element_id in spdx_id_set
            for rel in describes_relationships
        )

        return describes_package

    def check_compliance(self):
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

    def print_components_missing_info(self):
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
                    "Components missing a name: "
                    f"{', '.join(self.components_without_names)}"
                )
                print()
            if self.components_without_versions:
                print(
                    "Components missing a version: "
                    f"{', '.join(self.components_without_versions)}"
                )
                print()
            if self.components_without_identifiers:
                print(
                    "Components missing an identifier: "
                    f"{', '.join(self.components_without_identifiers)}"
                )
                print()
            if self.components_without_suppliers:
                print(
                    "Components missing a supplier: "
                    f"{', '.join(self.components_without_suppliers)}"
                )
                print()
            if self.components_without_concluded_licenses:
                print(
                    "Components missing a license: "
                    f"{', '.join(self.components_without_concluded_licenses)}"
                )
                print()
            if self.components_without_copyright_texts:
                print(
                    "Components missing a copyright notice: "
                    f"{', '.join(self.components_without_copyright_texts)}"
                )
                print()

    def print_table_output(self):
        """Print element-by-element result table."""
        # pylint: disable=line-too-long
        if self.parsing_error:
            print(
                f"\nIs this SBOM FSCTv3 Baseline Attributes conformant? {self.compliant}\n"
            )
            print(
                "The provided document couldn't be parsed, check for FSCTv3 Baseline Attributes couldn't be performed.\n"
            )
            print("The following SPDXParsingError was raised:\n")
            for error in self.parsing_error:
                print(error)

        else:
            print(
                f"\nIs this SBOM FSCTv3 Baseline Attributes conformant? {self.compliant}\n"
            )
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
                for message in self.validation_messages:
                    print(message.validation_message)

    def output_json(self):
        """Create a dict of results for outputting to JSON."""
        # instantiate dict and fields that have > 1 level
        result = {}
        result["complianceStandard"] = self.compliance_standard
        result["parsingError"] = self.parsing_error
        result["isConformant"] = self.compliant

        result["sbomName"] = self.sbom_name
        result["componentNames"] = {}
        result["componentVersions"] = {}
        result["componentIdentifiers"] = {}
        result["componentSuppliers"] = {}

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

        result["componentCopyrightText"][
            "nonconformantComponents"
        ] = self.components_without_copyright_texts
        result["componentCopyrightText"][
            "allProvided"
        ] = not self.components_without_copyright_texts

        result["totalNumberComponents"] = self.get_total_number_components()

        result["validationMessages"] = []
        if self.validation_messages:
            result["validationMessages"] = list(map(str, self.validation_messages))

        return result

    def output_html(self):
        """Create a HTML of results."""
        if self.doc:
            result = (
                f" <h2>FSCTv3-Minimum Expected Conformance Results</h2> "
                f"<h3>Conformant: {self.compliant} </h3>"
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
            for message in self.validation_messages:
                result += f"<p>{message.validation_message}</p>\n"
        else:
            result = f"""
            <h2>FSCTv3-Minimum Expected Conformance Results</h2>
            <h3>Conformant: {self.compliant} </h3>
            <p>The provided document couldn't be parsed, check for minimum elements couldn't be performed.</p>
            <p>The following SPDXParsingError was raised:<p><ul>"""
            for error in self.parsing_error:
                result += f"""<li>{error}</li>"""

            result += """</ul>"""

        return result
