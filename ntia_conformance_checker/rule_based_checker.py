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
from typing import ClassVar

from .base_checker import BaseChecker
from .constants import DEFAULT_SBOM_SPEC, DEPRECATED_COMPLIANCE_IDS
from .model import COMPONENT_ELEMENT_IDS, Finding
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
        self.run_probes()
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

    # ---- Running the rules --------------------------------------------------

    def run_probes(self) -> dict[str, list[Finding]]:
        """Run every active rule's probe and return the findings by rule id.

        Probes are maturity-independent; maturity only selects which rules a
        verdict or report considers. Verdicts and reports run them afresh, so
        they follow the checker's current attributes. When no component is reachable from the
        SBOM root, component rules fail rather than pass over an empty list.
        """
        findings: dict[str, list[Finding]] = {}
        for rule in self._spec.active_rules():
            if rule.probe is None:
                raise ValueError(
                    f"{self._spec.id}: active rule {rule.slug!r} has no probe"
                )
            if (
                rule.element_id in COMPONENT_ELEMENT_IDS
                and not self.components_evaluated
            ):
                found = [_NOT_EVALUATED]
            else:
                found = list(lookup(rule.probe.name)(self, **rule.probe.params))
            findings[self._spec.rule_id(rule)] = found
        return findings

    def check_compliance(self, maturity: int = 0) -> bool:
        """Whether the SBOM passes every requirement in scope at ``maturity``.

        Recommendations and permissions are advisory and do not affect the
        verdict. Validation messages make the SBOM non-compliant.
        """
        target = self._validate_maturity(maturity)
        if not self.doc or self.validation_messages:
            return False
        findings = self.run_probes()
        return all(
            not findings[self._spec.rule_id(rule)]
            for rule in self._spec.blocking_rules(target)
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
        findings = self.run_probes()
        return [
            (rule.competency_question, not findings[self._spec.rule_id(rule)])
            for rule in self._ordered_rules(maturity)
        ]

    def _standard_title(self) -> str:
        return self._spec.title

    def _failure_messages(self, maturity: int) -> list[str]:
        messages = []
        findings = self.run_probes()
        for rule in self._ordered_rules(maturity):
            found = findings[self._spec.rule_id(rule)]
            if (
                not found
                or found == [_NOT_EVALUATED]
                or rule.provision != "requirement"
            ):
                continue  # not evaluated is reported separately; advisory rules aside
            text = rule.element_description or rule.slug
            messages.append(rule.warning or f"{text[:1].upper()}{text[1:]} is missing.")
        return messages

    def _missing_info(self, maturity: int) -> list[tuple[str, list[tuple[str, str]]]]:
        in_scope = {rule.element_id for rule in self._ordered_rules(maturity)}
        return [
            (name, components)
            for name, components in self.all_components_without_info
            if name not in _MIN_ELEMENT_TO_ID or _MIN_ELEMENT_TO_ID[name] in in_scope
        ]
