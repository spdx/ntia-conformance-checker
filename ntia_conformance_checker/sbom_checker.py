# SPDX-FileCopyrightText: 2024-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Main checking functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from .base_checker import BaseChecker
from .constants import SUPPORTED_SBOM_SPECS

if TYPE_CHECKING:
    from .spec import Spec


@final
class SbomChecker(BaseChecker):
    """
    SBOM checker factory - do not subclass this class.

    Subclass BaseChecker instead to implement a new compliance checker.

    Post-v3.0.2, SbomChecker acts like a factory that returns
    a subclass of BaseChecker based on the given "compliance" argument
    during instantiation.

    Currently supported compliance standards:

    - **"ntia" (default)**: 2021 NTIA SBOM Minimum Elements
    - **"fsct3"**: 2024 CISA SBOM Baseline Attributes (Minimum Expected)

    If "compliance" is not recognized, SbomChecker raises a ValueError.
    """

    def __new__(
        cls,
        file: str,
        validate: bool = True,
        compliance: str = "ntia",
        sbom_spec: str = "spdx2",
    ) -> Any:
        """
        Return an instance of a specific compliance checker.

        Args:
            file (str): The path to the SBOM file to be checked.
            validate (bool): Whether to validate the file before checking.
                Defaults to True.
            compliance (str): The compliance standard to use. Defaults to "ntia".
            sbom_spec (str): The SBOM specification format. Defaults to "spdx2".

        Returns:
            BaseChecker: An instance of the compliance checker configured for
                the requested compliance standard.

        Raises:
            ValueError: If ``sbom_spec`` is not supported or ``compliance`` is
                not recognized.
        """
        if sbom_spec not in SUPPORTED_SBOM_SPECS:
            raise ValueError(f"Unsupported SBOM specification: {sbom_spec}")

        # The registry is the single source of truth for which compliance
        # standards exist; ``get_spec`` raises ValueError for unknown ids.
        # Dispatch is spec-driven -- no per-standard branch here, so adding
        # a new ``rules/<id>.yaml`` is all that is needed to support a new
        # ``--comply`` value.
        # pylint: disable=import-outside-toplevel
        from .registry import get_spec
        from .rule_based_checker import RuleBasedChecker

        spec = get_spec(compliance)
        return RuleBasedChecker(
            file,
            validate,
            compliance=compliance,
            sbom_spec=sbom_spec,
            spec=spec,
        )

    def __init_subclass__(cls, /) -> None:  # prevent subclassing
        raise TypeError(
            "SbomChecker is a factory/dispatcher and must not be subclassed. "
            "Please subclass BaseChecker to implement custom checkers."
        )

    def check_compliance(self) -> bool:
        raise NotImplementedError("This method is not implemented by SbomChecker.")

    @property
    def spec(self) -> "Spec":
        raise NotImplementedError("This property is not implemented by SbomChecker.")
