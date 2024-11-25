# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Main checking functionality."""

from .base_checker import BaseChecker


class SbomChecker(BaseChecker):
    """
    SBOM check.
    """

    # Note that all NTIA-specific functionalities are moved to
    # .ntia_checker.NTIAChecker, and common functionalities that can be shared
    # among checkers of different compliance standards are moved to
    # .base_checker.BaseChecker.
    #
    # SbomChecker now acts as a "dispatcher" that returns
    # a subclass of BaseChecker based on the given "compliance" argument
    # during instantiation.

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
            from .ntia_checker import NTIAChecker

            return NTIAChecker(file, validate)
        elif compliance.startswith("fsct"):
            from .fsct_checker import FSCT3Checker

            return FSCT3Checker(file, validate)
        else:
            return super(SbomChecker, cls).__new__(cls)
