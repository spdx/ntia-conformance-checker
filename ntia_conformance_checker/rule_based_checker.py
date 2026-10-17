# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Checker driven by a declarative :class:`~ntia_conformance_checker.spec.Spec`.

A :class:`RuleBasedChecker` runs the probes of one spec (a ``rules/*.yaml``
file) against the information :class:`BaseChecker` has already extracted from
the SBOM, so a new standard made of presence checks needs only a YAML file.
"""

from __future__ import annotations

import inspect
import warnings
from typing import Any, ClassVar

from .base_checker import BaseChecker
from .constants import DEFAULT_SBOM_SPEC, DEPRECATED_COMPLIANCE_IDS
from .model import COMPONENT_ELEMENT_IDS, COMPONENT_KINDS, Finding, RuleResult
from .probes import lookup
from .registry import get_spec
from .spec import Spec, SpecRule

# Element id -> (name in BaseChecker.MIN_ELEMENTS, BaseChecker attribute listing
# the components that lack the element).
_COMPONENT_ELEMENTS = {
    "name": ("name", "components_without_names"),
    "version": ("version", "components_without_versions"),
    "unique_identifier": ("identifier", "components_without_identifiers"),
    "supplier": ("supplier", "components_without_suppliers"),
    "concluded_license": (
        "concluded_license",
        "components_without_concluded_licenses",
    ),
    "copyright_notice": ("copyright_text", "components_without_copyright_texts"),
}
_MIN_ELEMENT_TO_ID = {legacy: eid for eid, (legacy, _) in _COMPONENT_ELEMENTS.items()}

# Element id -> BaseChecker attribute that is truthy when the document has it.
_DOCUMENT_ELEMENTS = {
    "author": "doc_author",
    "timestamp": "doc_timestamp",
    "spec_version": "doc_version",
    "dependency_relationship": "dependency_relationships",
    "sbom_type": "sbom_gen_context",
}

_ROLLUPS = ("any-of", "all-of")
_DECIDED = ("present", "missing")

_UNPARSED = Finding(component_id="document", note="The SBOM could not be parsed.")

_NOT_EVALUATED = Finding(
    component_id="document",
    note="No component is reachable from the SBOM root, so none was evaluated.",
)


def _caller_stacklevel() -> int:
    """``warnings.warn`` stacklevel, from the function that called this one,
    of the first frame outside this package, so the warning is attributed to
    (and shown for) the user's code."""
    frame = inspect.currentframe()
    level = 0
    while frame and frame.f_globals.get("__name__", "").startswith(__package__ or ""):
        frame = frame.f_back
        level += 1
    return level


class RuleBasedChecker(BaseChecker):
    """A :class:`BaseChecker` whose rules come from a :class:`Spec`.

    ``compliance`` is a registered spec id or a :class:`Spec`. Report rows are
    ordered by ``MIN_ELEMENTS`` (component rules) then ``DOCUMENT_ORDER``
    (document rules); rules not listed follow in spec order.

    Only the elements in ``_COMPONENT_ELEMENTS`` and ``_DOCUMENT_ELEMENTS`` can
    be evaluated: a spec with an active rule on another element (for example
    ``cryptographic_hash``) raises ``ValueError`` when the checker is created.
    """

    DOCUMENT_ORDER: ClassVar[tuple[str, ...]] = ()

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str | Spec = "",
        sbom_spec: str = DEFAULT_SBOM_SPEC,
    ) -> None:
        self._spec, standard = self._resolve_spec(compliance)
        super().__init__(
            file=file, validate=validate, compliance=standard, sbom_spec=sbom_spec
        )
        self.rule_results()  # fail on an unevaluable rule at construction
        self.table_elements = self._requirement_rows(0)

    @staticmethod
    def _resolve_spec(compliance: str | Spec) -> tuple[Spec, str]:
        """Return the spec and the standard name to report for ``compliance``."""
        if isinstance(compliance, Spec):
            return compliance, compliance.id
        if not compliance:
            raise ValueError("No compliance standard given; pass a spec id or Spec.")
        spec_id = DEPRECATED_COMPLIANCE_IDS.get(compliance, compliance)
        if spec_id != compliance:
            warnings.warn(
                f"Compliance standard {compliance!r} is deprecated; "
                f"use {spec_id!r} instead.",
                DeprecationWarning,
                stacklevel=_caller_stacklevel(),
            )
        return get_spec(spec_id), compliance

    def _min_elements(self) -> list[str]:
        """``MIN_ELEMENTS`` if a subclass sets it, else the spec's component rules."""
        return self.MIN_ELEMENTS or list(
            dict.fromkeys(
                _COMPONENT_ELEMENTS[rule.element_id][0]
                for rule in self._spec.active_rules()
                if rule.element_id in _COMPONENT_ELEMENTS
            )
        )

    @property
    def spec(self) -> Spec:
        """The compliance spec this checker runs."""
        return self._spec

    def maturity_ordinals(self) -> tuple[int, ...]:
        """Maturity levels declared by the spec."""
        return self._spec.maturity_ordinals()

    # ---- Accessors used by probes ------------------------------------------

    def components_without(self, element_id: str) -> list[tuple[str, str]]:
        """Components lacking ``element_id``, as ``(name, spdx_id)`` pairs."""
        if element_id not in _COMPONENT_ELEMENTS:
            raise ValueError(
                f"{self._spec.id}: cannot evaluate component element {element_id!r}"
            )
        return list(getattr(self, _COMPONENT_ELEMENTS[element_id][1]))

    def document_has(self, element_id: str) -> bool:
        """Whether the SBOM document declares ``element_id``."""
        if element_id not in _DOCUMENT_ELEMENTS:
            raise ValueError(
                f"{self._spec.id}: cannot evaluate document element {element_id!r}"
            )
        return bool(getattr(self, _DOCUMENT_ELEMENTS[element_id]))

    def _extra_graph_relationships(self) -> frozenset[str]:
        """Relationships a spec rule reads pointing at the component (a dataset
        reached through ``trainedOn``) also connect elements; lineage and
        license links do not, so a base model or license stays outside."""
        return frozenset(
            name
            for rule in self._spec.active_rules()
            if rule.probe is not None and rule.probe.name == "require_relationship"
            if rule.probe.params.get("direction") == "to"
            for name in rule.probe.params["relationships"]
        )

    def has_components(self, kind: str, reachable_only: bool = True) -> bool:
        """Whether the SBOM has a component of ``kind`` (reachable from the root
        unless ``reachable_only`` is false)."""
        return self.adapter.has_components_of_kind(
            kind, self.reachable_component_ids if reachable_only else None
        )

    def components_without_property(
        self, kind: str, properties: tuple[str, ...]
    ) -> list[tuple[str, str]]:
        """Components of ``kind`` declaring none of the SPDX 3 ``properties``."""
        return self.adapter.get_components_without_properties(
            kind, properties, self.reachable_component_ids
        )

    def components_without_relationship(
        self, kind: str, relationships: tuple[str, ...], direction: str
    ) -> list[tuple[str, str]]:
        """Components of ``kind`` in none of the ``relationships``."""
        return self.adapter.get_components_without_relationships(
            kind, relationships, direction, self.reachable_component_ids
        )

    def document_declares(self, properties: tuple[str, ...]) -> bool:
        """Whether the document declares any of the SPDX 3 ``properties``."""
        return self.adapter.document_declares_any(properties)

    # ---- Running the rules --------------------------------------------------

    def rule_results(self) -> dict[str, RuleResult]:
        """Evaluate every emitted rule and return its result by rule id.

        Probes are maturity-independent; maturity only selects which rules a
        verdict or report considers. Results are computed afresh on each call,
        so they follow the checker's current attributes.
        """
        spec = self._spec
        other_sbom = bool(spec.sbom_specs) and self.sbom_spec not in spec.sbom_specs
        results: dict[str, RuleResult] = {}
        rules = spec.emitted_rules()
        for rule in rules:
            if rule.aggregation in _ROLLUPS:
                continue
            results[spec.rule_id(rule)] = self._probe_result(rule, other_sbom)
        for rule in rules:
            if rule.aggregation in _ROLLUPS:
                results[spec.rule_id(rule)] = self._rollup_result(rule, results)
        return results

    def _probe_result(self, rule: SpecRule, other_sbom: bool) -> RuleResult:
        """Run one rule's probe, unless the rule is inactive or does not apply."""
        rule_id = self._spec.rule_id(rule)
        if rule.status != "active":
            return RuleResult(rule_id=rule_id, outcome="out-of-scope")
        if rule.probe is None:
            raise ValueError(f"{self._spec.id}: active rule {rule.slug!r} has no probe")
        if other_sbom:
            return RuleResult(rule_id=rule_id, outcome="not-applicable")
        params = rule.probe.params
        kind = params.get("kind")
        if kind is not None and kind not in COMPONENT_KINDS:
            raise ValueError(f"{self._spec.id}: unknown component kind {kind!r}")
        if kind is not None and not self.doc:
            return RuleResult(rule_id=rule_id, outcome="missing", findings=(_UNPARSED,))
        component_rule = rule.element_id in COMPONENT_ELEMENT_IDS or kind is not None
        if component_rule and not self.components_evaluated:
            # Nothing to inspect: fail rather than pass over an empty list.
            return RuleResult(
                rule_id=rule_id, outcome="missing", findings=(_NOT_EVALUATED,)
            )
        if kind is not None and kind != "component" and not self.has_components(kind):
            return self._no_component_result(rule_id, kind)
        found = tuple(lookup(rule.probe.name)(self, **params))
        return RuleResult(
            rule_id=rule_id, outcome="missing" if found else "present", findings=found
        )

    def _no_component_result(self, rule_id: str, kind: str) -> RuleResult:
        """Result of a kind-scoped rule when no reachable component has that kind.

        The SBOM always has a system; a component that exists but is not
        reachable is a defect. Only a kind the SBOM has none of does not apply.
        """
        if kind == "system":
            note = "The SBOM does not describe a package."
        elif self.has_components(kind, reachable_only=False):
            note = f"A {kind.replace('_', ' ')} is not reachable from the SBOM root."
        else:
            return RuleResult(rule_id=rule_id, outcome="not-applicable")
        return RuleResult(
            rule_id=rule_id,
            outcome="missing",
            findings=(Finding(component_id="document", note=note),),
        )

    def _rollup_result(
        self, rule: SpecRule, results: dict[str, RuleResult]
    ) -> RuleResult:
        """Derive a composite rule's result from the results of its sub-rules.

        Per component: for *any of*, a component fails when it lacks every
        sub-element; for *all of*, when it lacks any. The findings are those
        components, so the roll-up points at the same elements the sub-rules do.
        """
        rule_id = self._spec.rule_id(rule)
        if rule.status != "active":
            return RuleResult(rule_id=rule_id, outcome="out-of-scope")
        children = [
            results[self._spec.rule_id(sub)]
            for sub in self._spec.rules
            if sub.parent == rule.slug and self._spec.rule_id(sub) in results
        ]
        decided = [c for c in children if c.outcome in _DECIDED]
        if not decided:
            applicable = all(c.outcome != "not-applicable" for c in children)
            return RuleResult(
                rule_id=rule_id,
                outcome="out-of-scope" if applicable else "not-applicable",
            )
        by_child = [{f.component_id: f for f in c.findings} for c in decided]
        if rule.aggregation == "any-of":
            failing = set.intersection(*(set(found) for found in by_child))
        else:
            failing = set.union(*(set(found) for found in by_child))
        findings = tuple(
            next(found[cid] for found in by_child if cid in found)
            for cid in sorted(failing)
        )
        return RuleResult(
            rule_id=rule_id,
            outcome="missing" if findings else "present",
            findings=findings,
        )

    def _under_rollup(self, rule: SpecRule) -> bool:
        """Whether ``rule`` is a sub-rule whose parent rolls it up."""
        parent = next((r for r in self._spec.rules if r.slug == rule.parent), None)
        return parent is not None and parent.aggregation in _ROLLUPS

    def check_compliance(self, maturity: int = 0) -> bool:
        """Whether the SBOM passes every requirement in scope at ``maturity``.

        Recommendations and permissions are advisory and do not affect the
        verdict, nor do rules that do not apply or are not checked. Validation
        messages make the SBOM non-compliant, as does having no rule that
        applies at all (nothing was checked).
        """
        target = self._validate_maturity(maturity)
        if not self.doc or self.validation_messages:
            return False
        results = self.rule_results()

        def outcome(rule: SpecRule) -> str:
            return results[self._spec.rule_id(rule)].outcome

        # Nothing applied: False for now; a tri-state result (True/False/None)
        # is an option if callers need to tell "not checked" from "failed".
        if not any(outcome(r) in _DECIDED for r in self._spec.active_rules(target)):
            return False
        return all(
            outcome(rule) != "missing"
            for rule in self._spec.blocking_rules(target)
            if not self._under_rollup(rule)
        )

    # ---- Report views --------------------------------------------------------

    def _ordered_rules(self, maturity: int) -> list[SpecRule]:
        order = [
            _MIN_ELEMENT_TO_ID[name]
            for name in self._min_elements()
            if name in _MIN_ELEMENT_TO_ID
        ]
        order += self.DOCUMENT_ORDER
        rules = self._spec.active_rules(self._validate_maturity(maturity))
        return sorted(
            rules,
            key=lambda r: order.index(r.element_id) if r.element_id in order else 999,
        )

    def _requirement_rows(self, maturity: int) -> list[tuple[str, bool]]:
        results = self.rule_results()
        return [
            (
                rule.competency_question,
                results[self._spec.rule_id(rule)].outcome == "present",
            )
            for rule in self._ordered_rules(maturity)
            if results[self._spec.rule_id(rule)].outcome in _DECIDED
        ]

    def _standard_title(self) -> str:
        return self._spec.title

    def _failure_messages(self, maturity: int) -> list[str]:
        results = self.rule_results()
        ordered = self._ordered_rules(maturity)
        messages = []
        for rule in ordered:
            res = results[self._spec.rule_id(rule)]
            if (
                res.outcome != "missing"
                or res.findings == (_NOT_EVALUATED,)  # reported separately
                or rule.provision != "requirement"
                or self._under_rollup(rule)
            ):
                continue
            text = rule.element_description or rule.slug
            messages.append(rule.warning or f"{text[:1].upper()}{text[1:]} is missing.")
        if ordered and not any(
            results[self._spec.rule_id(r)].outcome in _DECIDED for r in ordered
        ):
            messages.append(
                f"No requirement of {self._spec.title} applies to this SBOM."
            )
        return messages

    def _missing_info(self, maturity: int) -> list[tuple[str, list[tuple[str, str]]]]:
        ordered = self._ordered_rules(maturity)
        in_scope = {rule.element_id for rule in ordered}
        info = [
            (name, components)
            for name, components in self.all_components_without_info
            if name not in _MIN_ELEMENT_TO_ID or _MIN_ELEMENT_TO_ID[name] in in_scope
        ]
        results = self.rule_results()
        for rule in ordered:  # rules scoped by kind list their components too
            found = results[self._spec.rule_id(rule)].findings
            components = [
                (f.component_name, f.component_id)
                for f in found
                if not f.is_document_level
            ]
            if rule.probe and "kind" in rule.probe.params and components:
                info.append((rule.element_description or rule.slug, components))
        return info

    def _json_extras(self, maturity: int) -> dict[str, Any]:
        """Per-rule outcomes and per-category compliance (``None``: nothing applies)."""
        results = self.rule_results()
        target = self._validate_maturity(maturity)
        rules = [r for r in self._spec.emitted_rules() if r.maturity <= target]
        clusters: dict[str, bool | None] = {}
        invalid = not self.doc or bool(self.validation_messages)
        for cat in self._spec.categories:
            members = [r for r in rules if r.spec_category == cat.id]
            if not members:
                continue
            decided = [
                r for r in members if results[self._spec.rule_id(r)].outcome in _DECIDED
            ]
            blocking = [
                r
                for r in decided
                if r.provision == "requirement" and not self._under_rollup(r)
            ]
            clusters[cat.id] = (
                None
                if not blocking
                else not invalid
                and all(
                    results[self._spec.rule_id(r)].outcome == "present"
                    for r in blocking
                )
            )
        return {
            "ruleResults": [
                {
                    "id": self._spec.rule_id(rule),
                    "category": rule.spec_category,
                    "outcome": results[self._spec.rule_id(rule)].outcome,
                    "provision": rule.provision,
                    "findings": [
                        {"id": f.component_id, "name": f.component_name, "note": f.note}
                        for f in results[self._spec.rule_id(rule)].findings
                    ],
                }
                for rule in rules
            ],
            "clusterCompliance": clusters,
        }
