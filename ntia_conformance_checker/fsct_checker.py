# SPDX-FileCopyrightText: 2024-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""CISA SBOM Baseline Attributes (Framing Software Component Transparency)
checker.

Thin alias for :class:`RuleBasedChecker` pinned to
:file:`rules/fsct.yaml`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .registry import get_spec
from .rule_based_checker import RuleBasedChecker

if TYPE_CHECKING:
    from .spec import Spec

# Spec is loaded once by the registry (from rules/fsct3.yaml) and shared.
_FSCT_SPEC: Spec = get_spec("fsct3")


class FSCT3Checker(RuleBasedChecker):
    """2024 CISA SBOM Baseline Attributes check.

    A set of Baseline Attributes is defined in Section 2.2 of
    Framing Software Component Transparency: Establishing a Common
    Software Bill of Materials (SBOM) Third Edition.

    Three maturity levels (Minimum Expected, Recommended Practice,
    Aspirational Goal) describe the evolving content of Attribute entries.
    This checker currently only validates the Minimum Expected level.

    See:
        https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024
    """

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: "str | Spec" = _FSCT_SPEC,
        sbom_spec: str = "spdx2",
    ) -> None:
        super().__init__(
            file=file,
            validate=validate,
            compliance=compliance,
            sbom_spec=sbom_spec,
        )
