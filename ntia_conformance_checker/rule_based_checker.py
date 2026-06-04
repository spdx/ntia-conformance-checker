# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Generic rule-based checker.

A :class:`RuleBasedChecker` runs the rules of a single :class:`Spec`
(loaded from a ``rules/*.yaml`` file) against an SBOM.  The spec is named by
the single ``compliance`` argument, which accepts either form:

* a **str** -- a registered spec id (e.g. ``"ntia"``); looked up in the
  registry.  This is how :class:`SbomChecker` dispatches from ``--comply``.
* a **Spec** -- used directly, so a caller can run a custom / ad-hoc spec
  without registering a YAML file.

A named subclass (the shipped :class:`NTIAChecker` / :class:`FSCT3Checker`)
simply defaults ``compliance`` to its pinned :class:`Spec`; no separate
class attribute is needed.

Adding a new standard is therefore just dropping a ``rules/<id>.yaml``
file into the package -- the registry discovers it and ``--comply <id>``
routes to it automatically.
"""

from __future__ import annotations

from .base_checker import BaseChecker
from .registry import get_spec
from .spec import Spec


class RuleBasedChecker(BaseChecker):
    """A :class:`BaseChecker` whose rules come from a :class:`Spec`.

    The active spec is resolved at construction time from the ``compliance``
    argument (a registered spec id, or a :class:`Spec` instance).
    """

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str | Spec = "",
        sbom_spec: str = "spdx2",
    ) -> None:
        spec = self._resolve_spec(compliance)
        super().__init__(
            file=file,
            validate=validate,
            compliance=spec.id,
            sbom_spec=sbom_spec,
        )
        self._spec: Spec = spec

        if self.doc:
            # Probes are maturity-independent; run them once up front so the
            # findings cache is warm.  Maturity is applied later as a view
            # filter by check_compliance / requirement_results / output_*.
            self.run_probes()

    @staticmethod
    def _resolve_spec(compliance: str | Spec) -> Spec:
        """Resolve the ``compliance`` argument to a :class:`Spec`.

        A :class:`Spec` is used directly; a non-empty str is looked up in the
        registry (raising ``ValueError`` for an unknown id).  An empty value
        has no standard to run.
        """
        if isinstance(compliance, Spec):
            return compliance
        if compliance:
            return get_spec(compliance)
        raise ValueError(
            "No compliance standard given; pass compliance=<spec id> or a Spec."
        )

    @property
    def spec(self) -> "Spec":
        """The compliance spec resolved for this instance."""
        return self._spec

    def check_compliance(self, maturity: int = 0) -> bool:
        """Compliant iff every blocking (``requirement``) rule in scope passed
        and validation was clean.  ``recommendation`` / ``permission`` rules are
        advisory: they still emit warning / none findings but do not affect the
        verdict.

        Defaults to ``0`` (the baseline).
        """
        if self.validation_messages:
            return False
        target = self._validate_maturity(maturity)
        if not self.findings:
            self.run_probes()
        return all(
            not self.findings.get(self._spec.rule_id(rule), [])
            for rule in self._spec.blocking_rules(target)
        )
