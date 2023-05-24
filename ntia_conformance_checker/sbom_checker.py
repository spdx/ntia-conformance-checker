"""Main minimum elements checking functionality."""

# pylint: disable=import-error

import logging
import os
import sys

from spdx_tools.spdx.parser import parse_anything
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.parser.error import SPDXParsingError
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document


# pylint: disable=too-many-instance-attributes
class SbomChecker:
    """SBOM minimum elements check."""

    def __init__(self, file):
        self.file = file
        self.parsing_error = []
        self.doc = self.parse_file()
        if not self.doc:
            self.ntia_mininum_elements_compliant = False
        else:
            self.validation_messages = validate_full_spdx_document(self.doc)
            self.sbom_name = self.doc.creation_info.name
            self.doc_version = self.check_doc_version()
            self.doc_author = True
            self.doc_timestamp = True
            self.dependency_relationships = self.check_dependency_relationships()
            self.components_without_names = self.get_components_without_names()
            self.components_without_versions = self.get_components_without_versions()
            self.components_without_suppliers = self.get_components_without_suppliers()
            self.components_without_identifiers = (
                self.get_components_without_identifiers()
            )
            self.ntia_mininum_elements_compliant = (
                self.check_ntia_minimum_elements_compliance()
            )

    def parse_file(self):
        """Parse SBOM document."""
        # check if file exists
        if not os.path.exists(self.file):
            logging.error("Filename %s not found.", self.file)
            sys.exit(1)
        try:
            doc = parse_anything.parse_file(self.file)
        except SPDXParsingError as err:
            self.parsing_error.extend(err.get_messages())
            return None
        return doc

    def check_doc_version(self):
        """Check for SPDX document version."""
        if str(self.doc.creation_info.spdx_version) not in ["SPDX-2.2", "SPDX-2.3"]:
            return False
        return True

    def check_dependency_relationships(self):
        """Check for existence of any relationships."""
        if len(self.doc.relationships) == 0:
            return False
        return True

    def get_components_without_names(self):
        """Retrieve SPDX ID of components without names."""
        components_without_names = []
        for package in self.doc.packages:
            if not package.name:
                components_without_names.append(package.spdx_id)
        return components_without_names

    def get_components_without_versions(self):
        """Retrieve SPDX ID of components without names."""
        components_without_versions = []
        for package in self.doc.packages:
            if not package.version:
                components_without_versions.append(package.name)
        return components_without_versions

    def get_components_without_suppliers(self):
        """Retrieve name of components without suppliers."""
        components_without_suppliers = []
        for package in self.doc.packages:
            # both package supplier and package originator satisfy the "supplier"
            # requirement
            # https://spdx.github.io/spdx-spec/v2.3/package-information/#76-package-originator-field
            no_package_supplier = package.supplier is None or isinstance(
                package.supplier, SpdxNoAssertion
            )
            no_package_originator = package.originator is None or isinstance(
                package.originator, SpdxNoAssertion
            )
            if no_package_supplier and no_package_originator:
                components_without_suppliers.append(package.name)

        return components_without_suppliers

    def get_components_without_identifiers(self):
        """Retrieve name of components without identifiers."""
        components_without_identifiers = []
        for package in self.doc.packages:
            if not package.spdx_id:
                components_without_identifiers.append(package.name)
        return components_without_identifiers

    def check_ntia_minimum_elements_compliance(self):
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

    def get_total_number_components(self):
        """Retrieve total number of components."""
        return len(self.doc.packages)

    def print_table_output(self):
        """Print element-by-element result table."""
        # pylint: disable=line-too-long
        if self.parsing_error:
            print(
                f"\nIs this SBOM NTIA minimum element conformant? {self.ntia_mininum_elements_compliant}\n"
            )
            print(
                "The provided document couldn't be parsed, check for ntia minimum elements couldn't be performed.\n"
            )
            print("The following SPDXParsingError was raised:\n")
            for error in self.parsing_error:
                print(error)

        else:
            print(
                f"\nIs this SBOM NTIA minimum element conformant? {self.ntia_mininum_elements_compliant}\n"
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
                    f"Components missing a name: {','.join(self.components_without_names)}"
                )
                print()
            if self.components_without_versions:
                print(
                    f"Components missing a version: {','.join(self.components_without_versions)}"
                )
                print()
            if self.components_without_identifiers:
                print(
                    f"Components missing an identifier: "
                    f"{','.join(self.components_without_identifiers)}"
                )
                print()
            if self.components_without_suppliers:
                print(
                    f"Components missing an supplier: {','.join(self.components_without_suppliers)}"
                )
                print()

    def output_json(self):
        """Create a dict of results for outputting to JSON."""
        # instantiate dict and fields that have > 1 level
        result = {}
        if not self.parsing_error:
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
            result["totalNumberComponents"] = self.get_total_number_components()
            if self.validation_messages:
                result["validationMessages"] = self.validation_messages
        else:
            result["parsingError"] = self.parsing_error

        result["isNtiaConformant"] = self.ntia_mininum_elements_compliant

        return result

    def output_html(self):
        """Print HTML of output."""
        if self.doc:
            result = (
                f" <h2>NTIA Conformance Results</h2> "
                f"<h3>Conformant: {self.ntia_mininum_elements_compliant} </h3>"
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
            <h2>NTIA Conformance Results</h2>
            <h3>Conformant: {self.ntia_mininum_elements_compliant} </h3>
            <p>The provided document couldn't be parsed, check for ntia minimum elements couldn't be performed.</p>
            <p>The following SPDXParsingError was raised:<p><ul>"""
            for error in self.parsing_error:
                result += f"""<li>{error}</li>"""

            result += """</ul>"""

        return result
