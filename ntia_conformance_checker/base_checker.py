# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Base checking functionality."""

from __future__ import annotations

import json
import logging
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Tuple, Union, cast

from spdx_python_model import v3_0_1 as spdx3  # type: ignore # import-untyped
from spdx_tools.spdx.model.document import Document
from spdx_tools.spdx.model.relationship import RelationshipType
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.parser import parse_anything
from spdx_tools.spdx.parser.error import SPDXParsingError
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document
from spdx_tools.spdx.validation.validation_message import ValidationMessage


SUPPORTED_SBOM_SPECS_DESC = {
    "spdx2": "Software Package Data Exchange (SPDX) 2.x",
    "spdx3": "System Package Data Exchange (SPDX) 3.x",
}
DEFAULT_SBOM_SPEC = "spdx2"
SUPPORTED_SBOM_SPECS = set(SUPPORTED_SBOM_SPECS_DESC.keys())

SUPPORTED_COMPLIANCE_STANDARDS_DESC = {
    # "cisasbom2025": "2025 CISA SBOM Minimum Elements",
    # https://www.cisa.gov/resources-tools/resources/2025-minimum-elements-software-bill-materials-sbom
    "fsct3-min": "2024 CISA Framing Software Component Transparency (minimum expectation)",
    # https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024
    "ntia": "2021 NTIA SBOM Minimum Elements",
    # https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
}
DEFAULT_COMPLIANCE_STANDARD = "ntia"
SUPPORTED_COMPLIANCE_STANDARDS = set(SUPPORTED_COMPLIANCE_STANDARDS_DESC.keys())

SUPPORTED_SPDX_VERSIONS = {(2, 2), (2, 3), (3, 0)}  # (Major, Minor)
SUPPORTED_SPDX2_VERSIONS = {
    f"SPDX-{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 2
}
SUPPORTED_SPDX3_VERSIONS = {
    f"{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 3
}


# pylint: disable=too-many-instance-attributes
class BaseChecker(ABC):
    """Base class for all compliance/conformance checkers.

    This base class contains methods for common tasks like file loading
    and parsing.

    Any class inheriting from BaseChecker must implement its abstract methods,
    such as `check_compliance` and `output_json`.
    """

    compliance_standard: str = ""  # fsct3-min, ntia
    sbom_spec: str = ""  # spdx2, spdx3
    # file_format: str = ""  # json, rdf-xml, tag-value, yaml, xml

    file: str = ""
    doc: Union[Document, spdx3.SHACLObjectSet, None] = None

    parsing_error: List[str] = []
    validation_messages: List[ValidationMessage] = []

    sbom_name: str = ""
    components_without_names: List[str] = []
    components_without_versions: List[str] = []
    components_without_suppliers: List[str] = []
    components_without_identifiers: List[str] = []
    components_without_concluded_licenses: List[str] = []
    components_without_copyright_texts: List[str] = []

    doc_version: bool = False  # Has SPDX document version?
    doc_author: bool = False  # Has SPDX document author?
    doc_timestamp: bool = False  # Has SPDX document creation timestamp?
    dependency_relationships: bool = False  # Has DESCRIBES relationship?

    compliant: bool = False  # Is SBOM compliant with the chosen standard?

    # An alias of "compliant", for backward compatibility
    ntia_minimum_elements_compliant: bool = compliant

    @abstractmethod
    def check_compliance(self) -> bool:
        """Abstract method to check compliance/conformance."""
        raise NotImplementedError

    @abstractmethod
    def print_components_missing_info(self) -> None:
        """
        Abstract method to print information about components that
        are missing required details.

        What is considered "missing" is determined by a compliance standard
        and the method that implements this abstract method.

        Returns:
            None
        """
        raise NotImplementedError

    @abstractmethod
    def print_table_output(self, verbose: bool = False) -> None:
        """
        Abstract method to print element-by-element result table.

        Returns:
            None
        """
        raise NotImplementedError

    @abstractmethod
    def output_json(self) -> Dict[str, Any]:
        """
        Abstract method to create a dict of results for outputting
        to JSON.
        """
        raise NotImplementedError

    @abstractmethod
    def output_html(self) -> str:
        """Abstract method to create a result in HTML format."""
        raise NotImplementedError

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str = "",
        sbom_spec: str = DEFAULT_SBOM_SPEC,
    ) -> None:
        """
        Initialize the BaseChecker.

        Args:
            file (str): The name of the file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used.
            sbom_spec (str): The SBOM specification to be used.
        """
        self.compliance_standard = compliance
        self.sbom_spec = sbom_spec
        # self.file_format = ""

        self.file = file

        if sbom_spec == "spdx2":
            self.doc = self.parse_file()
        elif sbom_spec == "spdx3":
            # Add SPDX 3 parsing here
            self.doc = None
        else:
            raise ValueError(f"Unsupported SBOM specification: {sbom_spec}")

        if self.doc:
            if validate:
                if sbom_spec == "spdx2":
                    self.validation_messages = validate_full_spdx_document(self.doc)
                else:
                    pass

            self.components_without_names = self.get_components_without_names()
            self.components_without_versions = cast(
                List[str], self.get_components_without_versions()
            )  # with return_tuples=False, always get List[str]
            self.components_without_suppliers = cast(
                List[str], self.get_components_without_suppliers()
            )
            self.components_without_identifiers = (
                self.get_components_without_identifiers()
            )
            self.components_without_concluded_licenses = cast(
                List[str], self.get_components_without_concluded_licenses()
            )
            self.components_without_copyright_texts = cast(
                List[str], self.get_components_without_copyright_texts()
            )

    def check_doc_version(self) -> bool:
        """Check for if the SPDX document version exists."""
        if not self.doc:
            return False

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if (
                not self.doc.creation_info
                or str(self.doc.creation_info.spdx_version)
                not in SUPPORTED_SPDX2_VERSIONS
            ):
                return False

            return True

        # SPDX 3
        # Add code to check document version for SPDX 3 here
        return False

    def check_dependency_relationships(self) -> bool:
        """Check if the SPDX document DESCRIBES at least one package."""
        if not self.doc:
            return False

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if not self.doc.relationships:
                return False

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

        # SPDX 3
        # Add code to check dependency relationships for SPDX 3 here
        return False

    def get_sbom_name(self) -> str:
        """Retrieve the name of the SBOM."""
        if not self.doc:
            return ""

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if self.doc.creation_info and self.doc.creation_info.name:
                return self.doc.creation_info.name
            return ""

        # SPDX 3
        # Add code to retrieve SBOM name for SPDX 3 here
        return ""

    def get_components_without_concluded_licenses(
        self, return_tuples: bool = False
    ) -> Union[List[str], List[Tuple[str, str]]]:
        """
        Retrieve names and/or SPDX IDs of components without concluded licenses.

        Args:
            return_tuples (bool): If True, return a list of tuples with
                                  component names and SPDX IDs.
                                  If False, return a list of component names.

        Returns:
            Union[List[str], List[Tuple[str, str]]]: A list of component names
            or a list of tuples with component names and SPDX IDs.
        """
        # Note: concluded license is mandatory in SPDX-2.2 and SPDX-2.3
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if not self.doc.packages:
                return []

            if return_tuples:
                components_name_id: List[Tuple[str, str]] = []
                for package in self.doc.packages:
                    no_license = (
                        package.license_concluded is None
                        or isinstance(package.license_concluded, SpdxNoAssertion)
                        or (
                            isinstance(package.license_concluded, str)
                            and package.license_concluded.strip() == ""
                        )
                    )
                    if no_license:
                        components_name_id.append((package.name, package.spdx_id))
                return components_name_id

            components_name: List[str] = []
            for package in self.doc.packages:
                no_license = (
                    package.license_concluded is None
                    or isinstance(package.license_concluded, SpdxNoAssertion)
                    or (
                        isinstance(package.license_concluded, str)
                        and package.license_concluded.strip() == ""
                    )
                )
                if no_license:
                    components_name.append(package.name)
            return components_name

        # SPDX 3
        # Add code to retrieve components without concluded licenses for SPDX 3 here

        return []

    def get_components_without_copyright_texts(
        self, return_tuples: bool = False
    ) -> Union[List[str], List[Tuple[str, str]]]:
        """
        Retrieve names and/or SPDX IDs of components without copyright texts.

        Args:
            return_tuples (bool): If True, return a list of tuples with
                                  component names and SPDX IDs.
                                  If False, return a list of component names.

        Returns:
            Union[List[str], List[Tuple[str, str]]]: A list of component names
            or a list of tuples with component names and SPDX IDs.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if not self.doc.packages:
                return []

            if return_tuples:
                components_name_id: List[Tuple[str, str]] = []
                for package in self.doc.packages:
                    no_license = (
                        package.copyright_text is None
                        or isinstance(package.copyright_text, SpdxNoAssertion)
                        or (
                            isinstance(package.copyright_text, str)
                            and package.copyright_text.strip() == ""
                        )
                    )
                    if no_license:
                        components_name_id.append((package.name, package.spdx_id))
                return components_name_id

            components_name: List[str] = []
            for package in self.doc.packages:
                no_license = (
                    package.copyright_text is None
                    or isinstance(package.copyright_text, SpdxNoAssertion)
                    or (
                        isinstance(package.copyright_text, str)
                        and package.copyright_text.strip() == ""
                    )
                )
                if no_license:
                    components_name.append(package.name)
            return components_name

        # SPDX 3
        # Add code to retrieve components without copyright texts for SPDX 3 here
        return []

    def get_components_without_identifiers(self) -> List[str]:
        """
        Retrieve name of components without identifiers.

        Returns:
            List[str]: A list of component names that do not have identifiers.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if not self.doc.packages:
                return []
            return [
                package.name for package in self.doc.packages if not package.spdx_id
            ]

        # SPDX 3
        # Add code to retrieve components without identifiers for SPDX 3 here
        return []

    def get_components_without_names(self) -> List[str]:
        """
        Retrieve SPDX ID of components without names.

        Args:
            return_tuples (bool): If True, return a list of tuples with
                                  component names and SPDX IDs.
                                  If False, return a list of component names.

        Returns:
            Union[List[str], List[Tuple[str, str]]]: A list of component names
            or a list of tuples with component names and SPDX IDs.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if not self.doc.packages:
                return []
            components_without_names: List[str] = []
            for package in self.doc.packages:
                if not package.name:
                    components_without_names.append(package.spdx_id)
            return components_without_names

        # SPDX 3
        # Add code to retrieve components without names for SPDX 3 here
        return []

    def get_components_without_suppliers(
        self, return_tuples: bool = False
    ) -> Union[List[str], List[Tuple[str, str]]]:
        """
        Retrieve names and/or SPDX IDs of components without suppliers.

        Args:
            return_tuples (bool): If True, return a list of tuples with
                                  component names and SPDX IDs.
                                  If False, return a list of component names.

        Returns:
            Union[List[str], List[Tuple[str, str]]]: A list of component names
            or a list of tuples with component names and SPDX IDs.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if not self.doc.packages:
                return []

            if return_tuples:
                components_name_id: List[Tuple[str, str]] = []
                for package in self.doc.packages:
                    no_supplier = package.supplier is None or isinstance(
                        package.supplier, SpdxNoAssertion
                    )
                    if no_supplier:
                        components_name_id.append((package.name, package.spdx_id))
                return components_name_id

            components_name: List[str] = []
            for package in self.doc.packages:
                no_supplier = package.supplier is None or isinstance(
                    package.supplier, SpdxNoAssertion
                )
                if no_supplier:
                    components_name.append(package.name)
            return components_name

        # SPDX 3
        # Add code to retrieve components without suppliers for SPDX 3 here
        return []

    def get_components_without_versions(
        self, return_tuples: bool = False
    ) -> Union[List[str], List[Tuple[str, str]]]:
        """
        Retrieve name and/or SPDX ID of components without versions.

        Args:
            return_tuples (bool): If True, return a list of tuples with
                                  component names and SPDX IDs.
                                  If False, return a list of component names.

        Returns:
            Union[List[str], List[Tuple[str, str]]]: A list of component names
            or a list of tuples with component names and SPDX IDs.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if not self.doc.packages:
                return []

            if return_tuples:
                components_name_id: List[Tuple[str, str]] = []
                for package in self.doc.packages:
                    if not package.version:
                        components_name_id.append((package.name, package.spdx_id))
                return components_name_id

            components_name: List[str] = []
            for package in self.doc.packages:
                if not package.version:
                    components_name.append(package.name)
            return components_name

        # SPDX 3
        # Add code to retrieve components without versions for SPDX 3 here
        return []

    def get_total_number_components(self) -> int:
        """
        Retrieve total number of components.

        Returns:
            int: The total number of components.
        """
        if not self.doc:
            return 0

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast(Document, self.doc)
            if not self.doc.packages:
                return 0
            return len(self.doc.packages)

        # SPDX 3
        # Add code to retrieve total number of components for SPDX 3 here
        return 0

    def parse_file(self) -> Optional[Document]:
        """
        Parse SPDX 2 SBOM document.

        Returns:
            Optional[Document]: The parsed SPDX 2 SBOM document if successful,
            otherwise None.
        """
        if not self.file or self.file.strip() == "":
            logging.error("No file path provided.")
            return None

        if not os.path.exists(self.file):
            logging.error("File not found: %s", self.file)
            return None

        try:
            doc = parse_anything.parse_file(self.file)
        except SPDXParsingError as err:
            self.parsing_error.extend(err.get_messages())
            return None

        return cast(Document, doc)

    def parse_spdx3_file(self) -> Optional[spdx3.SHACLObjectSet]:
        """
        Parse SPDX 3 SBOM document.

        Returns:
            Optional[spdx3.SHACLObjectSet]: A collection of SPDX 3 objects if successful,
            otherwise None.
        """
        if not self.file or self.file.strip() == "":
            logging.error("No file path provided.")
            return None

        if not os.path.exists(self.file):
            logging.error("File not found: %s", self.file)
            return None

        object_set = spdx3.SHACLObjectSet()
        try:
            spdx3.JSONLDDeserializer().read(self.file, object_set)
        except (OSError, json.JSONDecodeError) as err:
            logging.debug("SPDX3 deserialization failed: %s", err)
            self.parsing_error.append(str(err))
            return None

        return object_set
