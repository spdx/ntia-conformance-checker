# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Generic per-element and per-standard specification for compliance checkers.

Defines three frozen dataclasses used as the single source of truth for every
output format (text table, JSON, SARIF, future OSCAL):

* :class:`SpecCategory` -- one category / cluster within a standard.  Maps to a
  SARIF taxon in the per-spec *category* taxonomy and to an OSCAL ``group``.

* :class:`SpecRule` -- one minimum-element check.  Holds the element id,
  checker instance attribute, report label, result kind, optional cluster
  grouping (for G7), optional SPDX-3 gating, source-spec reference (clause
  number + URL), maturity, status, and optional JSON output mapping.

* :class:`Spec` -- a compliance standard's full rule catalogue.  Holds the
  standard id, title, general help URL (used as a fallback when a rule has
  no rule-specific URL), SARIF taxonomy/taxon identifiers, and the tuple of
  :class:`SpecRule` entries.

Rule identifiers follow the ``[SPEC]-[CATEGORY]-[NN]`` convention documented
in ``RULES.md``.  ``SPEC`` is :attr:`Spec.spec_code` (e.g. ``NTIA``, ``FSCT``);
``CATEGORY`` is :attr:`SpecCategory.code` (e.g. ``DF``, ``COMP``); ``NN`` is
:attr:`SpecRule.number` zero-padded.

Cluster-less checkers (NTIA, FSCT3) leave :attr:`SpecRule.cluster` empty.
Cluster-aware checkers (G7) set it on every entry; rendering code that
iterates clusters simply skips entries whose ``cluster`` does not match.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Maturity = Literal["minimum-expected", "recommended", "aspirational"]
"""Three maturity levels per FSCT §2.2 / NTIA implicit equivalents."""

Status = Literal["active", "catalogue-only", "tbd"]
"""Per-rule emission status.

* ``active`` -- rule appears in the SARIF rule catalogue *and* results are
  emitted when the check fails.
* ``catalogue-only`` -- rule appears in the catalogue (consumers can show
  the full spec surface) but the checker never emits results for it; either
  the attribute is aspirational or the check is not yet implemented.
* ``tbd`` -- identifier is reserved in :file:`RULES.md` only.  The rule is
  *not* added to the catalogue; it exists so that wiring up the check later
  does not require renumbering existing rules.
"""


@dataclass(frozen=True, kw_only=True)
class ProbeRef:
    """Reference to a registered probe, with bound parameters.

    Loaded from the ``probe:`` block of a YAML rule.  The engine resolves
    ``name`` against :mod:`ntia_conformance_checker.probes._registry` and
    calls the probe with ``params`` as keyword arguments.
    """

    name: str
    """Probe name as registered with :func:`probes.probe`."""

    params: dict[str, Any] = field(default_factory=dict)
    """Keyword arguments passed to the probe.  Probe functions declare
    every accepted parameter explicitly so typos in YAML fail loudly."""


@dataclass(frozen=True, kw_only=True)
class SpecCategory:
    """A grouping within a :class:`Spec` (e.g. NTIA Data Fields).

    Renders as a SARIF taxon in the spec's *category taxonomy* and as an
    OSCAL ``group`` in a future OSCAL exporter.
    """

    id: str
    """Lowercase kebab-case category id (taxon id / OSCAL group id).
    Example: ``"data-fields"`` for NTIA §IV Data Fields."""

    code: str
    """Uppercase short code used as the ``CATEGORY`` segment of a rule id.
    Example: ``"DF"`` -> ``NTIA-DF-01``."""

    title: str
    """Human-readable category title.  Example: ``"Data Fields"``."""

    description: str = ""
    """Optional one-line category description for SARIF taxon
    ``shortDescription.text``."""


@dataclass(frozen=True, kw_only=True)
# pylint: disable=too-many-instance-attributes
class SpecRule:
    """Per-element check specification, reusable across compliance checkers."""

    # -- Rule identity ----------------------------------------------------

    category: str
    """Id of the :class:`SpecCategory` this rule belongs to (matches
    :attr:`SpecCategory.id`).  Determines the ``CATEGORY`` segment of the
    rule id and the category taxon the rule's ``relationships`` point at."""

    number: int
    """Zero-padded sequence number within ``(spec, category)``, in the order
    the spec lists the attribute.  Becomes ``NN`` in the rule id."""

    slug: str
    """Human-readable rule slug, lowercase kebab-case, **prefixed with the
    lowercase spec code** to avoid cross-spec collisions.  Example:
    ``"ntia-component-name"``, ``"fsct-component-name"``."""

    element_id: str = ""
    """Canonical element id from
    :data:`ntia_conformance_checker.model.ELEMENT_IDS` (e.g. ``"name"``,
    ``"supplier"``, ``"creation_timestamp"``).  Carries the semantic key
    that survives across specs -- different specs may give the same
    underlying concept different names (e.g. "Type" vs "Generation
    Context"), but the ``element_id`` matches as long as the probe
    queries the same SBOM-model field."""

    sarif_rule_name: str
    """SARIF ``reportingDescriptor.name`` (PascalCase short name,
    e.g. ``NtiaComponentNameMissing``)."""

    label: str
    """Exact table label used in text/HTML reports."""

    description: str = ""
    """Short noun phrase naming the missing element (e.g. ``"component
    supplier"``).  Used in per-finding result messages.  For the canonical
    user-facing prose, see :attr:`warning`."""

    warning: str = ""
    """Canonical, single-sentence diagnostic prose for the rule, following
    the parallel pattern documented in :file:`RULES.md`:

    * component-level: ``"An SBOM component should have a {X}."``
    * document-level:  ``"An SBOM should {X}."``

    This string is the source of truth for the user-facing warning text
    (analogous to Microsoft's CA-rule "warning" column).  SARIF emits it as
    the rule's ``shortDescription.text``; CLI / HTML / future localisers
    should consume it from here rather than re-inventing wording in code.
    Empty falls back to ``"{description.capitalize()} is missing."``."""

    # -- Source spec reference --------------------------------------------

    ref_section: str = ""
    """Literal section number from the source spec (e.g. ``"2.2.2.7"``).
    Becomes the id of the rule's clause taxon and -- when paired with
    :attr:`Spec.sarif_clause_taxonomy_name` -- a SARIF taxonomy entry."""

    ref_title: str = ""
    """Human-readable clause title (e.g. ``"License"``)."""

    ref_url: str = ""
    """Deep link to the exact spec clause.  When empty, consumers fall back
    to :attr:`Spec.help_uri` via :meth:`Spec.rule_help_uri`."""

    # -- Maturity / status ------------------------------------------------

    maturity: Maturity = "minimum-expected"
    """Spec-defined maturity level; drives the default SARIF severity."""

    status: Status = "active"
    """Whether the rule is emitted in the catalogue / as results.
    See :data:`Status` for semantics."""

    # -- OSCAL output (deferred) ------------------------------------------

    oscal_control_id: str = ""
    """Optional override for the future OSCAL ``control-id``.  When empty,
    the OSCAL exporter is expected to lowercase the SARIF rule id."""

    # -- Cluster / SPDX gating (G7) ---------------------------------------

    cluster: str = ""
    """Optional cluster name.  Falsy means the rule belongs to no cluster."""

    spdx3_only: bool = False
    """If True, the rule is omitted from cluster tables when the SBOM is
    not SPDX 3.  The attribute still exists with its class-level default."""

    # -- JSON output mapping (used by G7-style output_json) ---------------

    json_group: str | None = None
    """JSON output group name (e.g. ``"aiPackages"``).  ``None`` means the
    rule, if emitted, lives at the top level of the JSON output."""

    json_key: str | None = None
    """JSON output key within ``json_group``.  ``None`` means the rule is
    not emitted in JSON output."""

    # -- Rule-based engine ------------------------------------------------

    probe: ProbeRef | None = None
    """Probe to run for this rule.  ``None`` for catalogue-only and TBD
    rules (they appear in the catalogue but no probe is invoked)."""


_MATURITY_TO_SARIF_LEVEL: dict[Maturity, str] = {
    "minimum-expected": "error",
    "recommended": "warning",
    "aspirational": "note",
}


@dataclass(frozen=True, kw_only=True)
class Spec:
    """A compliance standard's full rule catalogue.

    Shared metadata at the standard level (general help URL, SARIF taxonomy
    identifiers) lives here; per-rule overrides live on :class:`SpecRule`.
    """

    standard_id: str
    """Compliance-standard identifier (lowercase), e.g. ``"ntia"`` /
    ``"fsct3-min"``.  Used in machine-to-machine handoffs (e.g. Lumina's
    ``RegulationId``) and in ``run.properties.complianceStandard``."""

    spec_code: str
    """Uppercase short spec code used as the ``SPEC`` segment of rule ids
    (e.g. ``"NTIA"``, ``"FSCT"``).  See ``RULES.md``."""

    title: str
    """Human-readable standard name, e.g. ``"NTIA Minimum Elements"``."""

    help_uri: str = ""
    """General documentation URL for the standard.  Used as the fallback
    when a :class:`SpecRule` does not provide its own ``ref_url``."""

    # -- Category taxonomy ------------------------------------------------

    sarif_taxonomy_name: str = ""
    """SARIF ``ToolComponent.name`` of the *category* taxonomy
    (e.g. ``"ntia-minimum-elements"``).  Doubles as the OSCAL catalog id."""

    categories: tuple[SpecCategory, ...] = field(default_factory=tuple)
    """The standard's categories / clusters.  Each becomes a SARIF taxon in
    the category taxonomy."""

    # -- Clause taxonomy (Phase 2 -- per-clause provenance) ---------------

    sarif_clause_taxonomy_name: str = ""
    """SARIF ``ToolComponent.name`` of the *clause* taxonomy
    (e.g. ``"fsct-clauses"``).  Each taxon id is a literal spec section
    number from :attr:`SpecRule.ref_section`.  Empty disables the clause
    taxonomy and the second ``equal`` relationship on every rule."""

    # -- Rules ------------------------------------------------------------

    rules: tuple[SpecRule, ...] = field(default_factory=tuple)
    """The standard's rule catalogue.  Rules with ``status == "tbd"`` are
    excluded from SARIF emission entirely; rules with
    ``status == "catalogue-only"`` appear in the catalogue but never as
    results."""

    # -- Derived helpers --------------------------------------------------

    def category(self, category_id: str) -> SpecCategory:
        """Look up a :class:`SpecCategory` by id; raise KeyError if absent."""
        for cat in self.categories:
            if cat.id == category_id:
                return cat
        raise KeyError(f"Spec {self.spec_code!r} has no category {category_id!r}")

    def rule_id(self, rule: SpecRule) -> str:
        """Compose the canonical ``[SPEC]-[CAT]-[NN]`` rule id."""
        cat = self.category(rule.category)
        return f"{self.spec_code}-{cat.code}-{rule.number:02d}"

    def oscal_control_id(self, rule: SpecRule) -> str:
        """Return the rule's OSCAL control id (override or lowercased rule id)."""
        return rule.oscal_control_id or self.rule_id(rule).lower()

    def sarif_level(self, rule: SpecRule) -> str:
        """SARIF default ``level`` derived from maturity."""
        return _MATURITY_TO_SARIF_LEVEL[rule.maturity]

    def rule_help_uri(self, rule: SpecRule) -> str:
        """Rule's source-spec URL if set, otherwise the standard URL."""
        return rule.ref_url or self.help_uri

    def rules_for_cluster(self, cluster: str) -> tuple[SpecRule, ...]:
        """Return rules whose :attr:`SpecRule.cluster` matches ``cluster``.

        Useful for cluster-aware checkers (G7) when rendering per-cluster
        tables.  For cluster-less standards (NTIA, FSCT3) callers usually
        iterate :attr:`rules` directly instead.
        """
        return tuple(r for r in self.rules if r.cluster == cluster)

    def emitted_rules(self) -> tuple[SpecRule, ...]:
        """Rules that appear in the SARIF catalogue (everything except TBD)."""
        return tuple(r for r in self.rules if r.status != "tbd")

    def active_rules(self) -> tuple[SpecRule, ...]:
        """Rules whose findings are actually emitted (excludes TBD + catalogue-only)."""
        return tuple(r for r in self.rules if r.status == "active")
