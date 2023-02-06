"""Main minimum elements checking functionality."""

# pylint: disable=import-error

import logging
import os
import sys

import spdx.creationinfo
from spdx.parsers import parse_anything


# pylint: disable=too-many-instance-attributes
class SbomChecker:
    """SBOM minimum elements check."""

    def __init__(self, file):
        self.file = file
        self.doc = self.parse_file()
        self.sbom_name = self.doc.name
        self.doc_version = self.check_doc_version()
        self.doc_author = self.check_doc_author()
        self.doc_timestamp = self.check_doc_timestamp()
        self.dependency_relationships = self.check_dependency_relationships()
        self.components_without_names = self.get_components_without_names()
        self.components_without_versions = self.get_components_without_versions()
        self.components_without_suppliers = self.get_components_without_suppliers()
        self.components_without_identifiers = self.get_components_without_identifiers()
        self.ntia_mininum_elements_compliant = (
            self.check_ntia_minimum_elements_compliance()
        )

    def parse_file(self):
        """Parse SBOM document."""
        # check if file exists
        if not os.path.exists(self.file):
            logging.error("Filename %s not found.", self.file)
            sys.exit(1)
        doc, err = parse_anything.parse_file(self.file)
        if err:
            logging.error("Document cannot be parsed: %s", err)

        return doc

    def check_doc_version(self):
        """Check for SPDX document version."""
        if str(self.doc.version) not in ["SPDX-2.2", "SPDX-2.3"]:
            return False
        return True

    def check_doc_author(self):
        """Check document author is person, organization, or tool."""
        for i, _ in enumerate(self.doc.creation_info.creators):
            if isinstance(
                self.doc.creation_info.creators[i],
                (
                    spdx.creationinfo.Person,
                    spdx.creationinfo.Organization,
                    spdx.creationinfo.Tool,
                ),
            ):
                return True
        return False

    def check_doc_timestamp(self):
        """Check for document timestamp."""
        if self.doc.creation_info.created is None:
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
            if package.name is None:
                components_without_names.append(package.spdx_id)
        return components_without_names

    def get_components_without_versions(self):
        """Retrieve SPDX ID of components without names."""
        components_without_versions = []
        for package in self.doc.packages:
            if package.version is None:
                components_without_versions.append(package.name)
        return components_without_versions

    def get_components_without_suppliers(self):
        """Retrieve name of components without suppliers."""
        components_without_suppliers = []
        for package in self.doc.packages:
            if package.supplier is None or "NOASSERTION" in package.supplier.name:
                components_without_suppliers.append(package.name)
        return components_without_suppliers

    def get_components_without_identifiers(self):
        """Retrieve name of components without identifiers."""
        components_without_identifiers = []
        for package in self.doc.packages:
            if package.spdx_id is None:
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
            ]
        )

    def get_total_number_components(self):
        """Retrieve total number of components."""
        return len(self.doc.packages)

    def print_table_output(self):
        """Print element-by-element result table."""
        # pylint: disable=line-too-long
        print()
        print(
            f"Is this SBOM NTIA minimum element conformant? {self.ntia_mininum_elements_compliant}"
        )
        print()
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
        print(f"SBOM creation timestamp provided?              | {self.doc_timestamp}")
        print(
            f"Dependency relationships provided?             | {self.dependency_relationships}"
        )
        print()

    def print_components_missing_info(self):
        """Print detailed info about which components are missing info."""
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
                f"Components missing an identifier: {','.join(self.components_without_identifiers)}"
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

        result["isNtiaConformant"] = self.ntia_mininum_elements_compliant

        result["totalNumberComponents"] = self.get_total_number_components()
        return result
