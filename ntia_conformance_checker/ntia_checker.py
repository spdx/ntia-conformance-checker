# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""NTIA Minimum Elements checking functionality."""

from __future__ import annotations

import warnings

from .rule_based_checker import RuleBasedChecker


class NTIAChecker(RuleBasedChecker):
    """
    NTIA Minimum Elements check.

    See:
        https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
    """

    MIN_ELEMENTS = ["name", "version", "identifier", "supplier"]
    DOCUMENT_ORDER = ("author", "timestamp", "dependency_relationship")

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str = "ntia",
        sbom_spec: str = "spdx2",
    ) -> None:
        """
        Initialize the NTIA Minimum Element Checker.

        Args:
            file (str): The name of the file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used.
            sbom_spec (str): The SBOM specification to be used.
        """
        if compliance not in {"ntia"}:
            raise ValueError("Only NTIA Minimum Element compliance is supported.")
        super().__init__(
            file=file, validate=validate, compliance=compliance, sbom_spec=sbom_spec
        )

    def check_ntia_minimum_elements_compliance(self) -> bool:
        """Check overall compliance with NTIA minimum elements.

        This method is kept for backward compatibility.
        Please consider using check_compliance() instead."""
        warnings.warn(
            "NTIAChecker.check_ntia_minimum_elements_compliance is deprecated; "
            "use check_compliance() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.check_compliance()
