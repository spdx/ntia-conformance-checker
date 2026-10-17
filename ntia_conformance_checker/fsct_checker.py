# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""FSCT Common BOM checking functionality."""

from __future__ import annotations

from .rule_based_checker import RuleBasedChecker


class FSCT3Checker(RuleBasedChecker):
    """FSCTv3 checker.

    A set of Baseline Attributes is defined in Section 2.2 of
    Framing Software Component Transparency:
    Establishing a Common Software Bill of Materials (SBOM) Third Edition.

    There are three maturity levels (Minimum Expected, Recommended Practice,
    and Aspirational Goal) for content provided in Attribute entries.

    This checker currently only checks for Minimum Expected maturity level.

    See:
        https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024
    """

    MIN_ELEMENTS = [
        "name",
        "version",
        "identifier",
        "supplier",
        "concluded_license",
        "copyright_text",
    ]
    DOCUMENT_ORDER = ("author", "timestamp", "sbom_type", "dependency_relationship")

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str = "fsct3",
        sbom_spec: str = "spdx2",
    ) -> None:
        """
        Initialize the FSCTv3 checker.

        Args:
            file (str): The name of the file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used; ``fsct3``
                (``fsct3-min`` is a deprecated alias).
            sbom_spec (str): The SBOM specification to be used.
        """
        if compliance not in {"fsct3", "fsct3-min"}:
            raise ValueError("Only FSCTv3 Minimum Expected compliance is supported.")
        super().__init__(
            file=file, validate=validate, compliance=compliance, sbom_spec=sbom_spec
        )
