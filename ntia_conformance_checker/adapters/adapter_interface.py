# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Blueprint interface for SBOM adapters."""

from abc import ABC, abstractmethod

from spdx_tools.spdx.validation.validation_message import ValidationMessage


class SbomAdapter(ABC):
    """Abstract base class defining the standard interface for all SBOM adapters."""

    @abstractmethod
    def get_doc_spec_version(self) -> str | None:
        """Retrieve the document's specification version."""

    def check_doc_version(self) -> bool:
        """Check if the document's specification version exists."""
        return bool(self.get_doc_spec_version())

    @abstractmethod
    def check_author(self) -> bool:
        """Check if the author of SBOM data exists."""

    @abstractmethod
    def check_timestamp(self) -> bool:
        """Check if the SBOM creation timestamp exists."""

    @abstractmethod
    def get_sbom_name(self) -> str:
        """Retrieve the name of the SBOM."""

    @abstractmethod
    def get_components_without_names(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        """
        Retrieve components missing a name.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """

    @abstractmethod
    def get_components_without_versions(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        """
        Retrieve components missing version information.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """

    @abstractmethod
    def get_components_without_suppliers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        """
        Retrieve components missing supplier information.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """

    @abstractmethod
    def get_components_without_identifiers(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        """
        Retrieve components missing unique identifiers (SPDX IDs).

        Note that SPDX 3 requires identifiers for all elements,
        so this should not happen in a valid SPDX 3 document.
        The spdx-python-model JSON deserializer will raise a ValueError
        if any element is missing an identifier.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """

    @abstractmethod
    def get_components_without_concluded_licenses(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        """
        Retrieve components missing a concluded license.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """

    @abstractmethod
    def get_components_without_copyright_texts(
        self, reachable_ids: set[str]
    ) -> list[tuple[str, str]]:
        """
        Retrieve components missing a copyright text.

        Returns:
            list[tuple[str, str]]: A list of tuples of the form
            (component_name, spdx_id). Consumers should extract the
            preferred value (name or SPDX ID) as needed.
        """

    @abstractmethod
    def check_dependency_relationships(self) -> bool:
        """Check if the SBOM document declares dependency information."""

    @abstractmethod
    def get_total_number_components(self) -> int:
        """
        Retrieve total number of components.

        For SPDX 2, this returns the total count of packages.
        For SPDX 3, this returns the total count of packages and package
        subclasses (including AIPackage and DatasetPackage).

        Returns:
            int: The total number of components.
        """

    @abstractmethod
    def get_sbom_types(
        self, conformance_messages: list[ValidationMessage]
    ) -> list[str]:
        """Get SBOM types from the rootElement of the SpdxDocument.

        CISA Framing Software Component Transparency (2024) listed
        "SBOM type" as one of baseline attributes, see Table 1 (p. 22) in:
        https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024

        In SPDX 3, SBOM type is only available in /Software/Sbom class.
        """
