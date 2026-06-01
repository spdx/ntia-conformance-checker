# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Generic rule-based checker.

A :class:`RuleBasedChecker` runs the rules of a single :class:`Spec`
(loaded from a ``rules/*.yaml`` file) against an SBOM.  The spec can be
supplied two ways:

* **per instance** -- ``RuleBasedChecker(file, spec=some_spec)``.  This is
  how :class:`SbomChecker` dispatches: it looks the spec up in the
  registry by ``--comply`` value and passes it in.  No per-spec Python
  subclass is required.

* **pinned on a subclass** -- a subclass sets the class attribute
  ``_SPEC``.  The shipped :class:`NTIAChecker` / :class:`FSCT3Checker`
  do this purely so ``from ntia_conformance_checker import NTIAChecker``
  keeps working; new standards do **not** need a subclass.

Adding a new standard is therefore just dropping a ``rules/<id>.yaml``
file into the package -- the registry discovers it and ``--comply <id>``
routes to it automatically.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .base_checker import BaseChecker

if TYPE_CHECKING:
    from .spec import Spec


class RuleBasedChecker(BaseChecker):
    """A :class:`BaseChecker` whose rules come from a :class:`Spec`.

    The active spec is resolved at construction time from the ``spec``
    argument, falling back to the class-level ``_SPEC`` if a subclass
    pinned one.  Exactly one of the two must be available.
    """

    # Subclasses may pin a spec here; otherwise pass ``spec=`` to __init__.
    _SPEC: "Spec | None" = None  # type: ignore[assignment]

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self,
        file: str,
        validate: bool = True,
        compliance: str = "",
        sbom_spec: str = "spdx2",
        target_maturity: int = 0,
        *,
        spec: "Spec | None" = None,
    ) -> None:
        super().__init__(
            file=file,
            validate=validate,
            compliance=compliance,
            sbom_spec=sbom_spec,
            target_maturity=target_maturity,
        )

        resolved = spec if spec is not None else type(self)._SPEC
        if resolved is None:
            raise ValueError(
                f"{type(self).__name__} has no spec; pass spec=... to the "
                "constructor or set the _SPEC class attribute."
            )
        self._spec: Spec = resolved

        valid_targets = self._spec.maturity_ordinals()
        if self.target_maturity not in valid_targets:
            raise ValueError(
                f"target_maturity {self.target_maturity!r} is not a declared "
                f"maturity level of spec {self._spec.id!r}; "
                f"valid levels: {list(valid_targets)!r}"
            )

        if self.doc:
            self.run_probes()
            self.compliant = self.check_compliance()

        # Table rows are derived from in-scope active rules in spec order so
        # they stay in sync with the YAML / RULES.md without manual duplication.
        self.table_elements = [
            (
                rule.competency_question,
                not self.findings.get(self._spec.rule_id(rule), []),
            )
            for rule in self._spec.active_rules(self.target_maturity)
        ]

    @property
    def spec(self) -> "Spec":
        """The compliance spec resolved for this instance."""
        return self._spec

    def check_compliance(self) -> bool:
        """Compliant iff every blocking (``requirement``) rule in scope passed
        and validation was clean.  ``recommendation`` / ``permission`` rules are
        advisory: they still emit warning / none findings but do not affect the
        verdict."""
        if self.validation_messages:
            return False
        return all(
            not self.findings.get(self._spec.rule_id(rule), [])
            for rule in self._spec.blocking_rules(self.target_maturity)
        )
