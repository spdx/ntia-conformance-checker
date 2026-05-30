# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Generic per-element and per-standard specification for compliance checkers.

Defines three frozen dataclasses used as the single source of truth for every
output format (text table, JSON, SARIF, future OSCAL):

* :class:`SpecRule` -- one minimum-element check.
  Holds the compliance element id and name, the report label, result kind,
  optional cluster grouping, optional SPDX-3 gating, the checker instance
  attribute and getter, an optional rule-specific help URL, JSON output
  mapping, and SARIF rule identifiers.

* :class:`SpecTaxon` -- one SARIF taxon (group/cluster) entry.
  Holds the taxon id and human-readable name.  Cluster-less standards
  (NTIA) define exactly one :class:`SpecTaxon`; cluster-aware
  standards (FSCT3) define one per cluster.

* :class:`Spec` -- a compliance standard's full rule catalogue.
  Holds the standard id, title, general help URL (used as a fallback when
  a rule has no rule-specific URL), the SARIF taxonomy name, the tuple of
  :class:`SpecTaxon` entries, and the tuple of :class:`SpecRule` entries.

Cluster-less checkers (NTIA) leave :attr:`SpecRule.cluster` empty.
Cluster-aware checkers (FSCT3) set it on every entry; rendering code that
iterates clusters simply skips entries whose ``cluster`` does not match.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


@dataclass(frozen=True, kw_only=True)
class SpecTaxon:
    """One SARIF taxon (group/cluster) within a :class:`Spec` taxonomy.

    Cluster-less standards (NTIA) define one :class:`SpecTaxon`.
    Cluster-aware standards (FSCT3) define one per cluster; each
    :class:`SpecRule` references its taxon via :attr:`SpecRule.cluster`.
    """

    taxon_id: str
    """Taxon ``id`` (for SARIF taxon ``id`` and future OSCAL group ID),
    e.g. ``"minimum-elements"`` or ``"component-attributes"``.
    For cluster-aware specs this must equal the :attr:`SpecRule.cluster`
    value of the rules that belong to this taxon."""

    taxon_name: str
    """Human-readable taxon name, used as SARIF taxon ``name``,
    e.g. ``"Minimum Elements"`` or ``"Component Attributes"``."""


@dataclass(frozen=True, kw_only=True)
# pylint: disable=too-many-instance-attributes
class SpecRule:
    """Per-element check specification, reusable across compliance checkers."""

    # -- Compliance standard ------------

    element_id: str
    """Compliance-standard identifier for this element
    (e.g. ``"supplier"``, ``"doc_author"``)."""

    element_name: str = ""
    """Terse human name for the compliance element,
    used to build result descriptions and SARIF messages
    (e.g. ``"component supplier"``, ``"SBOM author"``)."""

    report_label: str
    """Question-form label shown in text/HTML report tables
    (e.g. ``"All component names provided?"``)."""

    kind: Literal["list", "bool"]
    """``"list"``: attribute is a list of missing items (passes if empty).
    ``"bool"``: attribute is a boolean flag (passes if truthy)."""

    cluster: str = ""
    """Optional cluster name.  Falsy means the rule belongs to no cluster."""

    spdx3_only: bool = False
    """If True, the rule is omitted from cluster tables when the SBOM is
    not SPDX 3.  The attribute still exists with its class-level default."""

    # -- Internal Python ---------

    attr: str
    """Instance attribute on the checker that holds the result."""

    getter: str
    """Name of the ``BaseChecker`` method that populates ``attr``.
    Called during ``__init__`` to compute the check result."""

    # -- Output (JSON / SARIF / OSCAL) ---------

    help_uri: str = ""
    """Rule-specific documentation URL.  When empty, consumers should fall
    back to :attr:`Spec.help_uri` via :meth:`Spec.rule_help_uri`."""

    json_group: str | None = None
    """JSON output group name (e.g. ``"componentAttributes"``).
    ``None`` means the rule, if emitted, lives at the top level of the JSON
    output."""

    json_key: str | None = None
    """JSON output key within ``json_group``.  ``None`` means the rule is
    not emitted in JSON output."""

    sarif_rule_id: str = ""
    """SARIF ``reportingDescriptor.id`` (OSCAL-control-id-shaped, lowercase,
    dotted namespace with kebab segments, e.g. ``ntia.component.supplier``).
    Empty means the rule is not emitted in SARIF output."""

    sarif_rule_name: str = ""
    """SARIF ``reportingDescriptor.name`` (PascalCase short name,
    e.g. ``ComponentSupplierMissing``)."""


@dataclass(frozen=True, kw_only=True)
class Spec:
    """A compliance standard's full rule catalogue.

    Shared metadata at the standard level (general help URL, SARIF taxonomy
    identifiers) lives here; per-rule overrides live on :class:`SpecRule`.
    """

    # -- Standard identity -----------

    standard_short_id: str
    """Tool-internal shorthand for this standard, used as the ``compliance``
    parameter value in the Python API and CLI
    (e.g. ``"ntia"`` or ``"fsct3-min"``).
    Short and unique within this tool, but not guaranteed globally unique."""

    standard_id: str = ""
    """Globally-unique identifier for this standard, used as the SARIF
    taxonomy ``ToolComponent.name`` and future OSCAL catalog id
    (e.g. ``"2021-ntia-sbom-minimum-elements"``)."""

    standard_name: str
    """Human-readable standard name, e.g. ``"NTIA Minimum Elements"``."""

    # -- Content -------

    rules: tuple[SpecRule, ...] = field(default_factory=tuple)
    """The standard's rule catalogue."""

    # -- Output (SARIF / OSCAL) ---------

    help_uri: str = ""
    """General documentation URL for the standard.  Used as the fallback
    when a :class:`SpecRule` does not provide its own ``help_uri``."""

    taxa: tuple[SpecTaxon, ...] = field(default_factory=tuple)
    """Grouping entries (taxa) for this standard.
    Cluster-less standards (NTIA) supply one :class:`SpecTaxon`.
    Cluster-aware standards (FSCT3) supply one per cluster;
    each entry's :attr:`SpecTaxon.taxon_id` must match the
    :attr:`SpecRule.cluster` value of the rules that belong to it."""

    def rule_help_uri(self, rule: SpecRule) -> str:
        """Return the rule-specific URL if set, otherwise the standard URL."""
        return rule.help_uri or self.help_uri

    def taxon_for_rule(self, rule: SpecRule) -> SpecTaxon | None:
        """Return the taxon this rule belongs to.

        For cluster-aware specs (FSCT3), the rule's :attr:`SpecRule.cluster` is
        matched against :attr:`SpecTaxon.taxon_id`.
        For cluster-less specs (NTIA) the single taxon is returned
        unconditionally.
        Returns ``None`` when :attr:`taxa` is empty.
        """
        if not self.taxa:
            return None
        if rule.cluster:
            for taxon in self.taxa:
                if taxon.taxon_id == rule.cluster:
                    return taxon
        return self.taxa[0]

    def rules_for_cluster(self, cluster: str) -> tuple[SpecRule, ...]:
        """Return rules whose :attr:`SpecRule.cluster` matches ``cluster``.

        Useful for cluster-aware checkers (FSCT3) when rendering per-cluster
        tables.
        For cluster-less standards (NTIA) callers usually iterate
        :attr:`rules` directly instead.
        """
        return tuple(r for r in self.rules if r.cluster == cluster)
