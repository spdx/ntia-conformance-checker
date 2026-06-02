# SPDX-FileCopyrightText: 2024-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""NTIA SBOM Minimum Elements checker.

Thin alias for :class:`RuleBasedChecker` pinned to
:file:`rules/ntia.yaml`.  The class is kept under the historical name
``NTIAChecker`` so existing imports (``from ntia_conformance_checker
import NTIAChecker``) keep working without change.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .registry import get_spec
from .rule_based_checker import RuleBasedChecker

if TYPE_CHECKING:
    from .spec import Spec

# Spec is loaded once by the registry (from rules/ntia.yaml) and shared.
_NTIA_SPEC: Spec = get_spec("ntia")


class NTIAChecker(RuleBasedChecker):
    """2021 NTIA SBOM Minimum Elements check.

    The Minimum Elements For a Software Bill of Materials (SBOM)
    July 12, 2021

    See:
        https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
    """

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: "str | Spec" = _NTIA_SPEC,
        sbom_spec: str = "spdx2",
    ) -> None:
        super().__init__(
            file=file,
            validate=validate,
            compliance=compliance,
            sbom_spec=sbom_spec,
        )
