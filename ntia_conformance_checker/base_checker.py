# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Base checking functionality."""

from __future__ import annotations

import json
import logging
import os
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Set, Tuple, Union, cast

from spdx_python_model import v3_0_1 as spdx3  # type: ignore # import-untyped
from spdx_tools.spdx.model.relationship import RelationshipType
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.parser import parse_anything
from spdx_tools.spdx.parser.error import SPDXParsingError
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document

from .constants import DEFAULT_SBOM_SPEC
from .report import ReportContext, report_html, report_text
from .spdx3_utils import (
    get_boms_from_spdx_document,
    get_packages_from_bom,
    iter_objects_with_property,
    iter_relationships_by_type,
    validate_spdx3_data,
)

if TYPE_CHECKING:
    from spdx_tools.spdx.model.document import Document
    from spdx_tools.spdx.validation.validation_message import ValidationMessage


# pylint: disable=too-many-instance-attributes
class BaseChecker(ABC):
    """Base class for all compliance/conformance checkers.

    This base class contains methods for common tasks like file parsing
    and information extractions from the SBOM.

    Any class inheriting from BaseChecker must implement its abstract methods,
    such as `check_compliance` and `output_json`.
    """

    # Minimum elements/baseline attributes required by a compliance standard
    MIN_ELEMENTS: List[str] = []

    # Mapping of components without information
    # SBOM component name: (list containing components missing the info, label)
    _COMPONENTS_WITHOUT_INFO = {
        "name": ("components_without_names", "Components missing a name"),
        "version": ("components_without_versions", "Components missing a version"),
        "identifier": (
            "components_without_identifiers",
            "Components missing an identifier",
        ),
        "supplier": ("components_without_suppliers", "Components missing a supplier"),
        "concluded_license": (
            "components_without_concluded_licenses",
            "Components missing a concluded license",
        ),
        "copyright_text": (
            "components_without_copyright_texts",
            "Components missing a copyright text",
        ),
    }

    compliance_standard: str = ""  # fsct3-min, ntia
    sbom_spec: str = ""  # spdx2, spdx3

    # These are detectable by spdx-tools, so not needed for now.
    # file_format: str = ""  # json, rdf-xml, tag-value, yaml, xml

    file: str = ""
    # For SPDX 3, we have to use SHACLObjectSet instead of SpdxDocument,
    # because we need access to relationships and other elements that are not
    # accessible from SpdxDocument.
    doc: Union[Document, spdx3.SHACLObjectSet, None] = None
    __spdx3_doc: Optional[spdx3.SpdxDocument] = None  # cached SPDX 3 document

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

        # Make sure the logs are instance variables and not class variables
        # to avoid shared state between instances.
        self.parsing_error = []
        self.validation_messages = []

        # SPDX 2
        if sbom_spec == "spdx2":
            self.doc = self.parse_file()
        # SPDX 3
        elif sbom_spec == "spdx3":
            object_set = self.parse_spdx3_file()
            if not object_set:
                logging.error("Failed to parse the SPDX 3 file.")
            else:
                self.doc = object_set
                _doc, _validation_messages = validate_spdx3_data(object_set)
                if not _doc or _validation_messages:
                    logging.error("SpdxDocument not found or invalid.")
                self.__spdx3_doc = _doc  # cache the extracted SpdxDocument
                self.validation_messages.extend(_validation_messages)
        else:
            # We can add a heuristic to detect the spec from the file content here,
            # in case sbom_spec is not provided or invalid.
            raise ValueError(f"Unsupported SBOM specification: {sbom_spec}")

        if self.doc:
            if validate:
                if sbom_spec == "spdx2":
                    self.doc = cast("Document", self.doc)
                    self.validation_messages = validate_full_spdx_document(self.doc)
                else:
                    pass

            self.sbom_name = self.get_sbom_name()

            self.doc_version = self.check_doc_version()
            self.doc_author = self.check_author()
            self.doc_timestamp = self.check_timestamp()
            self.dependency_relationships = self.check_dependency_relationships()

            self.components_without_names = self.get_components_without_names()
            self.components_without_versions = cast(
                "List[str]", self.get_components_without_versions()
            )  # with return_tuples=False, always get List[str]
            self.components_without_suppliers = cast(
                "List[str]", self.get_components_without_suppliers()
            )
            self.components_without_identifiers = (
                self.get_components_without_identifiers()
            )
            self.components_without_concluded_licenses = cast(
                "List[str]", self.get_components_without_concluded_licenses()
            )
            self.components_without_copyright_texts = cast(
                "List[str]", self.get_components_without_copyright_texts()
            )

            self.all_components_without_info: List[Tuple[str, List[str]]] = (
                self._get_all_components_without_info()
            )

        self.table_elements: List[Tuple[str, bool]] = []

    def check_doc_version(self) -> bool:
        """Check if the document's specification version exists."""
        if self.get_doc_spec_version():
            return True
        return False

    def check_author(self) -> bool:
        """Check if the author of SBOM data exists."""
        if not self.doc:
            return False

        # SPDX 2
        if self.sbom_spec == "spdx2":
            # Note that the spdx-tools's parser will raise an SPDXParsingError
            # anyway, if the document does not contain a creator.
            # So in practice, this section should always return True
            self.doc = cast("Document", self.doc)
            doc_creation_info = getattr(self.doc, "creation_info", None)
            if doc_creation_info:
                doc_creators = getattr(doc_creation_info, "creators", [])
                if doc_creators:
                    return True
            return False

        # SPDX 3
        if self.sbom_spec == "spdx3" and self.__spdx3_doc is not None:
            doc_creation_info = getattr(self.__spdx3_doc, "creationInfo", None)
            if doc_creation_info:
                doc_creators = getattr(doc_creation_info, "createdBy", [])
                if doc_creators:
                    return True
            return False

        return False

    def check_dependency_relationships(self) -> bool:
        """Check if the SPDX document DESCRIBES at least one package."""
        if not self.doc:
            return False

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
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
        if self.sbom_spec == "spdx3":
            # If a BOM/an SBOM's rootElement is a /Software/Package (or its subclass),
            # it is considered to have a relationship.
            #
            # Note that if there is neither /Software/Package(s) nor /Core/Bom,
            # a DESCRIBES relationship is not needed; however, this method may still
            # return False, since it is factually considered as "no relationship".

            # There is a BOM and an /Software/Package,
            # check if there is at least one package listed in any BOM/SBOM
            boms = get_boms_from_spdx_document(self.__spdx3_doc)
            if boms:
                for bom in boms:
                    packages = get_packages_from_bom(bom)
                    if packages:
                        return True

        return False

    def check_timestamp(self) -> bool:
        """Check if the SBOM creation timestamp exists."""
        if not self.doc:
            return False

        # SPDX 2
        if self.sbom_spec == "spdx2":
            # Note that the spdx-tools's parser will raise an SPDXParsingError,
            # if the document does not contain a timestamp.
            # So in practice, this section should always return True.
            self.doc = cast("Document", self.doc)
            doc_creation_info = getattr(self.doc, "creation_info", None)
            if doc_creation_info:
                doc_created = getattr(doc_creation_info, "created", None)
                if doc_created:
                    return True
            return False

        # SPDX 3
        if self.sbom_spec == "spdx3" and self.__spdx3_doc is not None:
            doc_creation_info = getattr(self.__spdx3_doc, "creationInfo", None)
            if doc_creation_info:
                doc_created = getattr(doc_creation_info, "created", None)
                if doc_created:
                    return True

        return False

    def get_doc_spec_version(self) -> Optional[str]:
        """Retrieve the document's specification version."""
        if not self.doc:
            return None

        doc_spec_version: Optional[str] = None

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            doc_creation_info = getattr(self.doc, "creation_info", None)
            if doc_creation_info:
                doc_spec_version = getattr(doc_creation_info, "spdx_version", None)

        # SPDX 3
        if self.sbom_spec == "spdx3" and isinstance(
            self.__spdx3_doc, spdx3.SpdxDocument
        ):
            doc_creation_info = getattr(self.__spdx3_doc, "creationInfo", None)
            if doc_creation_info:
                doc_spec_version = getattr(doc_creation_info, "specVersion", None)

        return doc_spec_version

    def get_sbom_name(self) -> str:
        """Retrieve the name of the SBOM."""
        if not self.doc:
            return ""

        name: str = ""

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            doc_creation_info = getattr(self.doc, "creation_info", None)
            if doc_creation_info:
                name = getattr(doc_creation_info, "name", "")

        # SPDX 3
        elif self.sbom_spec == "spdx3" and isinstance(
            self.__spdx3_doc, spdx3.SpdxDocument
        ):
            name = getattr(self.__spdx3_doc, "name", "")

        return name

    # pylint: disable=too-many-branches
    # pylint: disable=too-many-return-statements
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
            self.doc = cast("Document", self.doc)
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
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            has_concluded_license_ids: Set[str] = {
                from_id
                for from_id, to_id in iter_relationships_by_type(
                    self.doc, "hasConcludedLicense"
                )
                if to_id.strip()
                != spdx3.expandedlicensing_IndividualLicensingInfo.NAMED_INDIVIDUALS[
                    "NoAssertionLicense"
                ]
            }

            if return_tuples:
                return [
                    (name, spdx_id)
                    for name, spdx_id, _ in iter_objects_with_property(
                        self.doc,
                        spdx3.software_Package,
                        "spdxId",
                    )
                    if spdx_id not in has_concluded_license_ids
                ]

            return [
                name
                for name, spdx_id, _ in iter_objects_with_property(
                    self.doc,
                    spdx3.software_Package,
                    "spdxId",
                )
                if spdx_id not in has_concluded_license_ids
            ]

        return []

    # pylint: disable=too-many-branches
    # pylint: disable=too-many-return-statements
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
            self.doc = cast("Document", self.doc)
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
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            if return_tuples:
                return [
                    (name, spdx_id)
                    for name, spdx_id, copyright_text in iter_objects_with_property(
                        self.doc,
                        spdx3.software_Package,
                        "software_copyrightText",
                    )
                    if not copyright_text
                    or (
                        isinstance(copyright_text, str) and copyright_text.strip() == ""
                    )
                ]

            return [
                name
                for name, _, copyright_text in iter_objects_with_property(
                    self.doc, spdx3.software_Package, "software_copyrightText"
                )
                if not copyright_text
                or (isinstance(copyright_text, str) and copyright_text.strip() == "")
            ]

        return []

    def get_components_without_identifiers(self) -> List[str]:
        """
        Retrieve name of components without identifiers.

        Note that SPDX 3 requires identifiers for all elements,
        so this should not happen in a valid SPDX 3 document.
        spdx-python-model JSON deserializer will raise a ValueError
        if any element is missing an identifier.

        Returns:
            List[str]: A list of component names.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            if not self.doc.packages:
                return []
            return [
                package.name for package in self.doc.packages if not package.spdx_id
            ]

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            return [
                name
                for name, _, spdx_id in iter_objects_with_property(
                    self.doc, spdx3.Element, "spdxId"
                )
                if not spdx_id or spdx_id.strip() == ""
            ]

        return []

    def get_components_without_names(self) -> List[str]:
        """
        Retrieve SPDX ID of components without names.

        Returns:
            List[str]: A list of component SPDX IDs.
        """
        if not self.doc:
            return []

        # SPDX 2
        if self.sbom_spec == "spdx2":
            self.doc = cast("Document", self.doc)
            if not self.doc.packages:
                return []
            components_without_names: List[str] = []
            for package in self.doc.packages:
                if not package.name:
                    components_without_names.append(package.spdx_id)
            return components_without_names

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            return [
                spdx_id
                for _, spdx_id, name in iter_objects_with_property(
                    self.doc, spdx3.software_Package, "name"
                )
                if not name or name.strip() == ""
            ]

        return []

    # pylint: disable=too-many-branches
    # pylint: disable=too-many-return-statements
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
            self.doc = cast("Document", self.doc)
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
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            if return_tuples:
                return [
                    (name, spdx_id)
                    for name, spdx_id, supplier in iter_objects_with_property(
                        self.doc, spdx3.software_Package, "suppliedBy"
                    )
                    if not supplier or not supplier.name or supplier.name.strip() == ""
                ]

            return [
                name
                for name, _, supplier in iter_objects_with_property(
                    self.doc, spdx3.software_Package, "suppliedBy"
                )
                if not supplier or not supplier.name or supplier.name.strip() == ""
            ]

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
            self.doc = cast("Document", self.doc)
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
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)

            if return_tuples:
                return [
                    (name, spdx_id)
                    for name, spdx_id, package_version in iter_objects_with_property(
                        self.doc, spdx3.software_Package, "software_packageVersion"
                    )
                    if not package_version or package_version.strip() == ""
                ]

            return [
                name
                for name, _, package_version in iter_objects_with_property(
                    self.doc, spdx3.software_Package, "software_packageVersion"
                )
                if not package_version or package_version.strip() == ""
            ]

        return []

    def _get_all_components_without_info(self) -> List[Tuple[str, List[str]]]:
        """Get a list of components missing information for each minimum component."""

        # If all lists are empty, return an empty list
        if all(
            not getattr(self, list_name, [])
            for list_name, _ in self._COMPONENTS_WITHOUT_INFO.values()
        ):
            return []

        res: List[Tuple[str, List[str]]] = []
        for component_name in self.MIN_ELEMENTS:
            if component_name in self._COMPONENTS_WITHOUT_INFO:
                list_name, _ = self._COMPONENTS_WITHOUT_INFO[component_name]
                components_without_info = getattr(self, list_name, [])
                if components_without_info:
                    res.append((component_name, components_without_info))

        return res

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
            self.doc = cast("Document", self.doc)
            if not self.doc.packages:
                return 0
            return len(self.doc.packages)

        # SPDX 3
        if self.sbom_spec == "spdx3":
            self.doc = cast("spdx3.SHACLObjectSet", self.doc)
            objects: Set[spdx3.SHACLObject] = getattr(self.doc, "objects", set())
            return len(objects)

        return 0

    def parse_file(self) -> Optional[Document]:
        """
        Parse SPDX 2 SBOM document.

        Returns:
            Optional[Document]: An SPDX 2 SBOM document if successful,
            otherwise None.
        """
        if not self.file or str(self.file).strip() == "":
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

        return cast("Document", doc)

    def parse_spdx3_file(self) -> Optional[spdx3.SHACLObjectSet]:
        """
        Parse SPDX 3 SBOM document.

        Returns:
            Optional[spdx3.SHACLObjectSet]: An SHACLObjectSet if successful,
            otherwise None.
        """
        if not self.file or str(self.file).strip() == "":
            logging.error("No file path provided.")
            return None

        if not os.path.exists(self.file):
            logging.error("File not found: %s", self.file)
            return None

        object_set: spdx3.SHACLObjectSet = spdx3.SHACLObjectSet()
        try:
            with open(self.file, encoding="utf-8") as f:
                spdx3.JSONLDDeserializer().read(f, object_set)
        except (OSError, json.JSONDecodeError) as err:
            logging.warning("SPDX3 deserialization failed: %s", err)
            self.parsing_error.append(str(err))
            return None

        return object_set

    def print_components_missing_info(self) -> None:
        """
        Print information about components that are missing required details.

        What is considered "missing" is determined by a compliance standard.
        Subclasses may override this method to provide custom behavior.

        Returns:
            None
        """
        # If parsing failed, skip
        if self.parsing_error:
            return

        if not self.all_components_without_info:
            return

        print("Missing required information in these components:")
        for component_name, components in self.all_components_without_info:
            print(f"{component_name} ({len(components)}): " f"{', '.join(components)}")

    def print_table_output(self, verbose: bool = False) -> None:
        """
        Print element-by-element result table.

        Args:
            verbose (bool): If True, print detailed information.

        Returns:
            None
        """
        report_context = ReportContext(
            sbom_spec=self.sbom_spec,
            compliance_standard=self.compliance_standard,
            compliant=self.compliant,
            requirement_results=self.table_elements,
            components_without_info=self.all_components_without_info,
            validation_messages=self.validation_messages,
            parsing_error=self.parsing_error,
        )

        print(report_text(report_context, verbose))

    def output_html(self) -> str:
        """
        Create element-by-element result table in HTML.

        Returns:
            str: The HTML representation of the results.
        """
        report_context = ReportContext(
            sbom_spec=self.sbom_spec,
            compliance_standard=self.compliance_standard,
            compliant=self.compliant,
            requirement_results=self.table_elements,
            components_without_info=self.all_components_without_info,
            validation_messages=self.validation_messages,
            parsing_error=self.parsing_error,
        )

        return report_html(report_context, verbose=True)

    def output_json(self) -> Dict[str, Any]:
        """
        Create a JSON-serializable result dict.

        Subclasses may override to provide custom fields.
        """
        result: Dict[str, Any] = {
            "isConformant": self.compliant,
            "isNtiaConformant": self.compliant,  # backward compatibility
            "complianceStandard": self.compliance_standard,
            "sbomSpec": self.sbom_spec,
            "validationMessages": (
                list(map(str, self.validation_messages))
                if self.validation_messages
                else []
            ),
            "parsingError": self.parsing_error,
            "sbomName": self.sbom_name,
            "specVersionProvided": self.doc_version,
            "authorNameProvided": self.doc_author,
            "timestampProvided": self.doc_timestamp,
            "dependencyRelationshipsProvided": self.dependency_relationships,
            "totalNumberComponents": self.get_total_number_components(),
        }

        _groups = {
            "componentNames": "components_without_names",
            "componentVersions": "components_without_versions",
            "componentIdentifiers": "components_without_identifiers",
            "componentSuppliers": "components_without_suppliers",
            "componentConcludedLicenses": "components_without_concluded_licenses",
            "componentCopyrightTexts": "components_without_copyright_texts",
        }

        for key_, attr in _groups.items():
            components_without_info = getattr(self, attr, [])
            result[key_] = {
                "nonconformantComponents": components_without_info,
                "allProvided": not bool(components_without_info),
            }

        return result
