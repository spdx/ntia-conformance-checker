# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Main checking functionality."""

from __future__ import annotations

from typing import final

from .base_checker import BaseChecker
from .constants import SUPPORTED_SBOM_SPECS


@final
class SbomChecker(BaseChecker):
    """
    SBOM checker factory - do not subclass this class.

    Subclass BaseChecker instead to implement a new compliance checker.

    Post-v3.0.2, SbomChecker acts like a factory that returns
    a subclass of BaseChecker based on the given "compliance" argument
    during instantiation.

    Currently there are two compliance standards available:

    - **"ntia" (default)**, returns an instance of NTIAChecker
      - NTIAChecker has the same behavior as the original SbomChecker
    - **"fsct3-min"**, returns an instance of FSCT3Checker
      - FSCT3Checker is a checker for FSCT 3rd Edition Baseline Attributes

    If "compliance" is not recognized, SbomChecker raises a ValueError.
    """

    # Note that all NTIA-specific functionalities are moved to
    # .ntia_checker.NTIAChecker, and common functionalities that can be shared
    # among checkers of different compliance standards are moved to
    # .base_checker.BaseChecker.

    def __new__(
        cls,
        file: str,
        validate: bool = True,
        compliance: str = "ntia",
        sbom_spec: str = "spdx2",
    ):
        """
        Returns an instance of a specific compliance checker.

        Args:
            file (str): The name of the file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used. Defaults to "ntia".
            sbom_spec (str): The SBOM specification to be used. Defaults to "spdx2".

        Returns:
            BaseChecker: An instance of a specific compliance checker.
        """
        if sbom_spec not in SUPPORTED_SBOM_SPECS:
            raise ValueError(f"Unsupported SBOM specification: {sbom_spec}")

        if compliance == "ntia":
            # pylint: disable=import-outside-toplevel
            from .ntia_checker import NTIAChecker

            return NTIAChecker(file, validate, sbom_spec=sbom_spec)

        if compliance.startswith("fsct3"):
            # pylint: disable=import-outside-toplevel
            from .fsct_checker import FSCT3Checker

            return FSCT3Checker(file, validate, sbom_spec=sbom_spec)

        raise ValueError(f"Unknown compliance standard: {compliance}")

    def __init_subclass__(cls, /):  # prevent subclassing
        raise TypeError(
            "SbomChecker is a factory/dispatcher and must not be subclassed. "
            "Please subclass BaseChecker to implement custom checkers."
        )

    def check_compliance(self) -> bool:
        raise NotImplementedError("This method is not implemented by SbomChecker.")
