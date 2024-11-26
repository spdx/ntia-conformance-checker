# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Base checking functionality."""

import logging
import os
import sys
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Union, cast

from spdx_tools.spdx.model import Document
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.parser import parse_anything
from spdx_tools.spdx.parser.error import SPDXParsingError
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document


class BaseChecker(ABC):
    """Base class for all compliance checkers.

    This base class contains methods for common tasks like file loading
    and parsing.

    Any class inheriting from BaseChecker must implement its abstract methods,
    such as `check_compliance` and `output_json`.
    """

    @abstractmethod
    def check_compliance(self) -> bool:
        """Abstract method to check compliance."""

    @abstractmethod
    def check_doc_version(self) -> bool:
        """Abstract method to check SBOM document version."""

    @abstractmethod
    def check_dependency_relationships(self) -> bool:
        """Abstract method to check dependency relationship requirements."""

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

    @abstractmethod
    def print_table_output(self) -> None:
        """
        Abstract method to print element-by-element result table.

        Returns:
            None
        """

    @abstractmethod
    def output_json(self) -> dict:
        """
        Abstract method to create a dict of results for outputting
        to JSON.
        """

    @abstractmethod
    def output_html(self) -> str:
        """Abstract method to create a result in HTML format."""

    def __init__(self, file, validate=True):
        """
        Initialize the BaseChecker.

        Args:
            file (str): The file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used. Defaults to "ntia".
        """
        self.parsing_error = []
        self.validation_messages = ""

        self.file = file
        self.doc = self.parse_file()  # Document or None

        self.doc_version = False
        self.doc_author = False
        self.doc_timestamp = False
        self.dependency_relationships = False
        self.components_without_names = []
        self.components_without_versions = []
        self.components_without_suppliers = []
        self.components_without_identifiers = []
        self.components_without_concluded_licenses = []
        self.components_without_copyright_texts = []

        self.compliant = False

        if self.doc:
            self.doc = cast(Document, self.doc)
            if validate:
                self.validation_messages = validate_full_spdx_document(self.doc)
            self.components_without_names = self.get_components_without_names()
            self.components_without_versions = self.get_components_without_versions()
            self.components_without_suppliers = self.get_components_without_suppliers()
            self.components_without_identifiers = (
                self.get_components_without_identifiers()
            )
            self.components_without_concluded_licenses = (
                self.get_components_without_concluded_licenses()
            )
            self.components_without_copyright_texts = (
                self.get_components_without_copyright_texts()
            )

    def get_components_without_concluded_licenses(
        self, return_tuples=False
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
        if return_tuples:
            components_name_id: List[Tuple[str, str]] = []
            for package in self.doc.packages:
                no_license = package.license_concluded is None or isinstance(
                    package.license_concluded, SpdxNoAssertion
                )
                if no_license:
                    components_name_id.append((package.name, package.spdx_id))
            return components_name_id
        else:
            components_name: List[str] = []
            for package in self.doc.packages:
                no_license = package.license_concluded is None or isinstance(
                    package.license_concluded, SpdxNoAssertion
                )
                if no_license:
                    components_name.append(package.name)
            return components_name

    def get_components_without_copyright_texts(
        self, return_tuples=False
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
        if return_tuples:
            components_name_id: List[Tuple[str, str]] = []
            for package in self.doc.packages:
                no_license = package.copyright_text is None or isinstance(
                    package.copyright_text, SpdxNoAssertion
                )
                if no_license:
                    components_name_id.append((package.name, package.spdx_id))
            return components_name_id
        else:
            components_name: List[str] = []
            for package in self.doc.packages:
                no_license = package.copyright_text is None or isinstance(
                    package.copyright_text, SpdxNoAssertion
                )
                if no_license:
                    components_name.append(package.name)
            return components_name

    def get_components_without_identifiers(self) -> list[str]:
        """
        Retrieve name of components without identifiers.

        Returns:
            List[str]: A list of component names that do not have identifiers.
        """
        return [package.name for package in self.doc.packages if not package.spdx_id]

    def get_components_without_names(self) -> list[str]:
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
        components_without_names = []
        for package in self.doc.packages:
            if not package.name:
                components_without_names.append(package.spdx_id)
        return components_without_names

    def get_components_without_suppliers(
        self, return_tuples=False
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
        if return_tuples:
            components_name_id: List[Tuple[str, str]] = []
            for package in self.doc.packages:
                no_supplier = package.supplier is None or isinstance(
                    package.supplier, SpdxNoAssertion
                )
                if no_supplier:
                    components_name_id.append((package.name, package.spdx_id))
            return components_name_id
        else:
            components_name: List[str] = []
            for package in self.doc.packages:
                no_supplier = package.supplier is None or isinstance(
                    package.supplier, SpdxNoAssertion
                )
                if no_supplier:
                    components_name.append(package.name)
            return components_name

    def get_components_without_versions(
        self, return_tuples=False
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
        if return_tuples:
            components_name_id: List[Tuple[str, str]] = []
            for package in self.doc.packages:
                if not package.version:
                    components_name_id.append((package.name, package.spdx_id))
            return components_name_id
        else:
            components_name: List[str] = []
            for package in self.doc.packages:
                if not package.version:
                    components_name.append(package.name)
            return components_name

    def get_total_number_components(self) -> int:
        """
        Retrieve total number of components.

        Returns:
            int: The total number of components.
        """
        return len(self.doc.packages)

    def parse_file(self) -> Optional[Document]:
        """
        Parse SBOM document.

        Returns:
            Optional[Document]: The parsed SBOM document if successful,
            otherwise None.
        """
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
