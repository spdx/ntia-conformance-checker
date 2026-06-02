# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Generic per-element and per-standard specification for compliance checkers.

Defines three frozen dataclasses used as the single source of truth for every
output format (text table, JSON, SARIF, future OSCAL):

* :class:`SpecCategory` -- one category / cluster within a standard.  Maps to a
  SARIF taxon in the per-spec *category* taxonomy and to an OSCAL ``group``.

* :class:`SpecRule` -- one minimum-element check.  Holds rule identity, its
  location in the source spec (category + clause), the element under test, the
  human-facing meaning (element description, competency question, warning),
  maturity (which tier requires it), provision (how strong the requirement
  is), status, the probe that performs the check, and optional output
  mappings.

* :class:`Spec` -- a compliance standard's full rule catalogue.  Holds the
  standard id/title, general help URL (used as a fallback when a rule has
  no rule-specific URL), the categories and rules, and the taxonomy names.

Rule identifiers follow the ``SBOM-[SPEC]-[CATEGORY]-[NNN]`` convention
documented in ``RULES.md``.  ``SPEC`` is the uppercased :attr:`Spec.id`
(e.g. ``NTIA``, ``FSCT3``) -- the edition is part of the id because each
edition is a distinct standard with its own requirements; ``CATEGORY`` is
:attr:`SpecCategory.code` (e.g. ``DF``, ``COMP``); ``NNN`` is
:attr:`SpecRule.number` zero-padded to three digits.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

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

Severity = Literal["error", "warning", "note", "none"]
"""Unified severity scale, ordered ``error > warning > note > none``.

Shared vocabulary for SARIF ``result.level``, a rule's default severity, and
the CLI log/verbosity threshold.  ``note`` is the informational band (logs and
tool notifications); no rule provision maps to it.
"""

Provision = Literal["requirement", "recommendation", "permission"]
"""ISO/IEC Directives provision type -- the kind of provision a rule states,
independent of its maturity.  Determines severity and whether failure blocks
conformance:

* ``requirement`` -> ``error``, blocks compliance.
* ``recommendation`` -> ``warning``, advisory.
* ``permission`` -> ``none``, advisory (a permission cannot be *violated* by
  absence, so it never produces an actionable finding).

A single maturity level can mix all three.
"""

_PROVISION_TO_SEVERITY: dict[Provision, Severity] = {
    "requirement": "error",
    "recommendation": "warning",
    "permission": "none",
}


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
class SpecMaturity:
    """One maturity level within a :class:`Spec`.

    Declaring maturity levels is **optional** -- a flat spec with no tiers
    simply omits :attr:`Spec.maturity_levels`, and the loader substitutes
    :data:`DEFAULT_MATURITY_LEVELS` (a single ``required`` / level ``0`` /
    ``error`` baseline) so every rule still has a named level.

    When a spec *does* declare levels, :attr:`level` is a **universal ordinal**
    -- ``0`` is the baseline, higher numbers demand more depth / completeness.
    This ordering is shared across specs (level 0 = baseline everywhere), so it
    supports "is this rule within target level N?" and cross-spec comparison.

    The :attr:`id` is a **spec-defined** machine slug for the level (FSCT v3:
    ``minimum`` / ``recommended`` / ``aspirational``; NTIA: ``required``); the
    :attr:`title` is its human label.  Rules still reference the level by its
    integer :attr:`level`; ``id`` is for output and possible name-based
    selection.

    Maturity carries **no severity** -- it only scopes *which* requirements
    apply at a target level.  How bad a missing requirement is comes from the
    rule's :attr:`SpecRule.provision`, an orthogonal axis.
    """

    level: int
    """Universal maturity ordinal (``0`` = baseline; higher = deeper)."""

    id: str
    """Spec-specific machine slug for the level (e.g. ``"minimum"``,
    ``"required"``).  Lowercase, hyphen/underscore-friendly."""

    title: str = ""
    """Optional human-readable label (e.g. ``"Minimum Expected"``)."""

    description: str = ""
    """Optional one-line description of the maturity level."""


DEFAULT_MATURITY_LEVELS: tuple["SpecMaturity", ...] = (
    SpecMaturity(
        level=0,
        id="required",
        title="Required",
        description="A minimum element that the SBOM must provide.",
    ),
)
"""Applied to any spec that does not declare its own ``maturity_levels`` -- a
flat spec then has a single, named baseline level (``required``) instead of an
anonymous one.  Severity comes from each rule's provision, not the tier."""


@dataclass(frozen=True, kw_only=True)
class SpecCategory:
    """A grouping within a :class:`Spec` (e.g. NTIA Data Fields, a G7 cluster).

    Renders as a SARIF taxon in the spec's *category taxonomy* and as an
    OSCAL ``group`` in a future OSCAL exporter.
    """

    id: str
    """Lowercase kebab-case category id (SARIF taxon id / OSCAL group id).
    Example: ``"data-fields"`` for NTIA §IV Data Fields.  Referenced by
    :attr:`SpecRule.spec_category`."""

    code: str
    """Uppercase short, hyphen-free token used as the ``CATEGORY`` segment of
    a rule id.  Example: ``"DF"`` -> ``SBOM-NTIA-DF-001``."""

    title: str
    """Human-readable category title.  Example: ``"Data Fields"``."""

    description: str = ""
    """Optional one-line category description for SARIF taxon
    ``shortDescription.text``."""


@dataclass(frozen=True, kw_only=True)
class SpecTaxonomies:
    """Names of a standard's two taxonomies (output-format agnostic).

    Each taxonomy groups the rules along one axis and is materialised per
    output format -- a SARIF ``ToolComponent`` (``toolComponent.name``) today,
    an OSCAL catalog/group id later.  Despite the SARIF wording these names are
    *not* SARIF-specific, hence no ``sarif_`` prefix.
    """

    category: str = ""
    """Name of the *category* taxonomy (e.g. ``"ntia-minimum-elements"``).

    Named for its **taxa**: each taxon is a :class:`SpecCategory`, and every
    rule has a ``superset`` relationship to its category taxon.  Mind the
    level mismatch -- the field names the taxonomy *by what it contains*
    (categories), but the **taxonomy as a whole is the standard's catalog**,
    so the value is the catalog/standard identifier (``"ntia-minimum-elements"``,
    not ``"ntia-categories"``) and doubles as the OSCAL **catalog** id; the
    categories within are the OSCAL **groups**."""

    clause: str = ""
    """Name of the *clause* taxonomy (e.g. ``"ntia-clauses"``).

    Also named for its **taxa**: each taxon id is a literal spec clause number
    from :attr:`SpecRule.spec_clause_number`, and every rule has an ``equal``
    relationship to its clause taxon.  Here name and taxa line up (both
    clause-flavoured), unlike :attr:`category`.  Empty disables the clause
    taxonomy and the per-rule ``equal`` relationship."""


@dataclass(frozen=True, kw_only=True)
# pylint: disable=too-many-instance-attributes
class SpecRule:
    """Per-element check specification, reusable across compliance checkers."""

    # -- Rule identity ----------------------------------------------------

    number: int
    """Sequence number within ``(spec, category)``, in the order the spec
    lists the attribute.  Zero-padded to three digits as ``NNN`` in the
    rule id."""

    slug: str
    """Human-readable rule slug, lowercase kebab-case, **prefixed with the
    spec id** to avoid cross-spec collisions.

    Frames the *finding* (the rule's failure condition), not the attribute --
    e.g. ``"ntia-component-supplier-missing"``, ``"fsct3-component-name-missing"``.
    Most rules are "...-missing" today, but the framing generalises
    (``"fsct3-timestamp-not-iso-format"``).

    This is the single human-readable identifier for a rule: the PascalCase
    :meth:`Spec.report_name` (SARIF ``reportingDescriptor.name`` etc.) is
    *derived* from it, so the two never drift -- they differ only in casing to
    suit each output format's convention."""

    # -- Spec mapping (location in the source spec) -----------------------

    spec_category: str
    """Id of the :class:`SpecCategory` this rule belongs to (matches
    :attr:`SpecCategory.id`).  Determines the ``CATEGORY`` segment of the
    rule id (via the category's ``code``) and the category taxon the rule's
    ``relationships`` point at."""

    spec_clause_number: str = ""
    """Literal clause / section designator from the source spec (e.g. ``"IV"``
    or ``"2.2.2.7"``).  Becomes the id of the rule's clause taxon and -- when
    paired with :attr:`SpecTaxonomies.clause` -- a clause taxonomy entry."""

    spec_clause_name: str = ""
    """Human-readable clause title (e.g. ``"License"``)."""

    spec_clause_uri: str = ""
    """Deep link to the exact spec clause.  When empty, consumers fall back
    to :attr:`Spec.uri` via :meth:`Spec.rule_uri`."""

    # -- Element & meaning ------------------------------------------------

    element_id: str = ""
    """Canonical element id from
    :data:`ntia_conformance_checker.model.ELEMENT_IDS` (e.g. ``"name"``,
    ``"supplier"``, ``"timestamp"``).  Carries the semantic key that survives
    across specs -- different specs may name the same underlying concept
    differently, but the ``element_id`` matches as long as the probe queries
    the same SBOM-model field."""

    element_description: str = ""
    """Short noun phrase naming the element (e.g. ``"component supplier"``).
    Used in per-finding result messages.  For the canonical user-facing
    prose, see :attr:`warning`."""

    competency_question: str = ""
    """The yes/no competency question the rule answers, used as the label in
    text/HTML report tables (e.g. ``"All component suppliers provided?"``)."""

    warning: str = ""
    """Canonical, single-sentence diagnostic prose for the rule, following
    the parallel pattern documented in :file:`RULES.md`:

    * component-level: ``"An SBOM component should have a {X}."``
    * document-level:  ``"An SBOM should {X}."``

    This string is the source of truth for the user-facing warning text.
    SARIF emits it as the rule's ``shortDescription.text``; CLI / HTML /
    future localisers should consume it from here rather than re-inventing
    wording in code.  Empty falls back to
    ``"{element_description.capitalize()} is missing."``."""

    # -- Maturity / provision / status ------------------------------------

    maturity: int = 0
    """Universal maturity ordinal this rule sits at -- *which* tier requires
    it.  Defaults to ``0`` (the baseline).  Must match one of the owning
    :class:`Spec`'s :attr:`SpecMaturity.level` values -- for a flat spec that
    is the substituted :data:`DEFAULT_MATURITY_LEVELS` (just level ``0``).
    Lets a spec carry several rules for the same ``element_id`` at increasing
    levels (each with its own deeper probe).  Carries **no** severity."""

    provision: Provision = "requirement"
    """ISO provision type -- *how bad* it is when missing.  Maps to severity
    (``requirement`` -> ``error``, ``recommendation`` -> ``warning``,
    ``permission`` -> ``none``) and decides whether failure blocks compliance
    (only ``requirement`` does).  Orthogonal to :attr:`maturity`."""

    status: Status = "active"
    """Whether the rule is emitted in the catalogue / as results.
    See :data:`Status` for semantics."""

    # -- The check --------------------------------------------------------

    probe: ProbeRef | None = None
    """Probe to run for this rule.  ``None`` for catalogue-only and TBD
    rules (they appear in the catalogue but no probe is invoked)."""

    # -- Output mappings --------------------------------------------------

    oscal_control_id: str = ""
    """Optional override for the future OSCAL ``control-id``.  When empty,
    the OSCAL exporter is expected to lowercase the SARIF rule id."""

    json_group: str | None = None
    """JSON output group / key prefix (e.g. ``"aiPackages"``).  ``None`` means
    the rule, if emitted, lives at the top level of the JSON output."""

    json_key: str | None = None
    """JSON output key within ``json_group``.  ``None`` means the rule is
    not emitted in JSON output."""


@dataclass(frozen=True, kw_only=True)
class Spec:
    """A compliance standard's full rule catalogue.

    Shared metadata at the standard level (general help URL, taxonomy
    names) lives here; per-rule overrides live on :class:`SpecRule`.
    """

    # -- Identity ---------------------------------------------------------

    id: str
    """Compliance-standard identifier, e.g. ``"ntia"`` / ``"fsct3"``.  Registry
    key, YAML filename, and the value emitted in SARIF
    ``run.properties.complianceStandard``.  Its uppercase form is the ``SPEC``
    segment of every rule id, so it must be a hyphen-free, uppercase-safe
    token (lowercase ASCII letters/digits, starting with a letter)."""

    title: str
    """Human-readable standard name, e.g. ``"2021 NTIA SBOM Minimum
    Elements"``."""

    uri: str = ""
    """General documentation URL for the standard.  Used as the fallback
    when a :class:`SpecRule` does not provide its own ``spec_clause_uri``."""

    # -- Content ----------------------------------------------------------

    categories: tuple[SpecCategory, ...] = field(default_factory=tuple)
    """The standard's categories / clusters.  Each becomes a SARIF taxon in
    the category taxonomy."""

    maturity_levels: tuple[SpecMaturity, ...] = field(
        default_factory=lambda: DEFAULT_MATURITY_LEVELS
    )
    """The standard's maturity vocabulary, keyed by universal ordinal.
    **Optional in YAML** -- a flat spec omits it and the loader substitutes
    :data:`DEFAULT_MATURITY_LEVELS` (a single ``required`` / level ``0`` /
    ``error`` baseline).  When declared it must include level ``0``."""

    rules: tuple[SpecRule, ...] = field(default_factory=tuple)
    """The standard's rule catalogue.  Rules with ``status == "tbd"`` are
    excluded from SARIF emission entirely; rules with
    ``status == "catalogue-only"`` appear in the catalogue but never as
    results."""

    # -- Taxonomies -------------------------------------------------------

    taxonomies: SpecTaxonomies = field(default_factory=SpecTaxonomies)
    """The standard's :class:`SpecTaxonomies` (category + clause names).
    Output-format agnostic; consumed by the SARIF emitter as
    ``ToolComponent.name`` and by a future OSCAL exporter."""

    # -- Lookups by key ---------------------------------------------------

    def category(self, category_id: str) -> SpecCategory:
        """Look up a :class:`SpecCategory` by id; raise KeyError if absent."""
        for cat in self.categories:
            if cat.id == category_id:
                return cat
        raise KeyError(f"Spec {self.id!r} has no category {category_id!r}")

    def maturity(self, level: int) -> SpecMaturity:
        """Look up a :class:`SpecMaturity` by its ordinal; KeyError if absent."""
        for mat in self.maturity_levels:
            if mat.level == level:
                return mat
        raise KeyError(f"Spec {self.id!r} has no maturity level {level!r}")

    # -- Per-rule derived values ------------------------------------------

    def maturity_id(self, rule: SpecRule) -> str:
        """Spec-specific slug of ``rule``'s maturity level (``""`` if none)."""
        for mat in self.maturity_levels:
            if mat.level == rule.maturity:
                return mat.id
        return ""

    def oscal_control_id(self, rule: SpecRule) -> str:
        """Return the rule's OSCAL control id (override or lowercased rule id)."""
        return rule.oscal_control_id or self.rule_id(rule).lower()

    @staticmethod
    def report_name(rule: SpecRule) -> str:
        """PascalCase reporting name for ``rule``, derived from its slug.

        Used as the SARIF ``reportingDescriptor.name`` (and any other
        output format wanting a whitespace-free, human-readable rule name).
        Derived -- never stored -- so it cannot drift from :attr:`SpecRule.slug`;
        the two differ only in casing.  E.g. ``"ntia-component-supplier-missing"``
        -> ``"NtiaComponentSupplierMissing"``.
        """
        return "".join(seg.capitalize() for seg in rule.slug.split("-"))

    def rule_id(self, rule: SpecRule) -> str:
        """Compose the canonical ``SBOM-[SPEC]-[CAT]-[NNN]`` rule id.

        The ``SPEC`` segment is :attr:`id` uppercased.
        """
        cat = self.category(rule.spec_category)
        return f"SBOM-{self.id.upper()}-{cat.code}-{rule.number:03d}"

    def rule_uri(self, rule: SpecRule) -> str:
        """Rule's source-spec clause URL if set, otherwise the standard URL."""
        return rule.spec_clause_uri or self.uri

    def severity(self, rule: SpecRule) -> Severity:
        """The rule's severity, from its provision (emitted as SARIF ``level``)."""
        return _PROVISION_TO_SEVERITY[rule.provision]

    # -- Maturity levels --------------------------------------------------

    @property
    def max_maturity(self) -> int:
        """Highest declared maturity ordinal (``0`` for a flat spec)."""
        return max((m.level for m in self.maturity_levels), default=0)

    def maturity_ordinals(self) -> tuple[int, ...]:
        """Declared maturity ordinals, ascending -- the valid assessment targets."""
        return tuple(sorted(m.level for m in self.maturity_levels))

    # -- Rule selection ---------------------------------------------------

    @staticmethod
    def _in_scope(rule: SpecRule, target: int | None) -> bool:
        """True if ``rule`` applies when assessing at ``target`` (``maturity <=
        target``).  ``target is None`` means no maturity filter (all tiers)."""
        return target is None or rule.maturity <= target

    def active_rules(self, target: int | None = None) -> tuple[SpecRule, ...]:
        """Active rules in scope for an assessment ``target`` maturity.

        Excludes TBD + catalogue-only.  With ``target`` set, also excludes
        rules above the target (``maturity > target``) -- they are out of scope
        and are neither evaluated nor reported.  ``target is None`` keeps every
        active rule (all tiers).
        """
        return tuple(
            r for r in self.rules if r.status == "active" and self._in_scope(r, target)
        )

    def blocking_rules(self, target: int | None = None) -> tuple[SpecRule, ...]:
        """In-scope active rules whose failure breaks compliance.

        Only ``requirement`` provisions are blocking; ``recommendation`` /
        ``permission`` rules are still emitted as findings (warning / none) but
        are advisory -- a present-but-implausible value, say, is reported
        without making the SBOM non-conformant.  Honours the assessment
        ``target`` the same way as :meth:`active_rules`.
        """
        return tuple(
            r
            for r in self.rules
            if r.status == "active"
            and r.provision == "requirement"
            and self._in_scope(r, target)
        )

    def emitted_rules(self) -> tuple[SpecRule, ...]:
        """Rules that appear in the SARIF catalogue (everything except TBD).

        Not maturity-filtered: the catalogue advertises the full rule surface
        of the spec regardless of the assessment target.
        """
        return tuple(r for r in self.rules if r.status != "tbd")
