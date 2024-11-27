# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Main checking functionality."""

from .base_checker import BaseChecker


class SbomChecker(BaseChecker):
    """
    SBOM checker factory.

    Post-v3.0.2, SbomChecker acts like a factory that returns
    a subclass of BaseChecker based on the given "compliance" argument
    during instantiation.

    Currently there are two compliance standards available:
    - "ntia" (default), returns an instance of NTIAChecker
      - NTIAChecker has the same behavior as the original SbomChecker
    - "fsct3-min", returns an instance of FSCT3Checker
      - FSCT3Checker is a new checker for FSCT 3rd Edition Baseline Attributes

    If "compliance" is not recognized, SbomChecker raises a ValueError.
    """

    # Note that all NTIA-specific functionalities are moved to
    # .ntia_checker.NTIAChecker, and common functionalities that can be shared
    # among checkers of different compliance standards are moved to
    # .base_checker.BaseChecker.

    def __new__(cls, file, validate=True, compliance="ntia"):
        """
        Returns an instance of a specific compliance checker.

        Args:
            file (str): The file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used. Defaults to "ntia".

        Returns:
            BaseChecker: An instance of a specific compliance checker.
        """
        if compliance == "ntia":
            # pylint: disable=import-outside-toplevel
            from .ntia_checker import NTIAChecker

            return NTIAChecker(file, validate)

        if compliance.startswith("fsct3"):
            # pylint: disable=import-outside-toplevel
            from .fsct_checker import FSCT3Checker

            return FSCT3Checker(file, validate)

        raise ValueError(f"Unknown compliance standard: {compliance}")

    def check_compliance(self) -> bool:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def check_doc_version(self) -> bool:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def check_dependency_relationships(self) -> bool:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def print_components_missing_info(self) -> None:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def print_table_output(self) -> None:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def output_json(self) -> dict:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def output_html(self) -> str:
        raise NotImplementedError("This method should be implemented by subclasses.")
