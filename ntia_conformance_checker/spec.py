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
  human-facing meaning (description, competency question, warning), maturity,
  status, the probe that performs the check, and optional output mappings.

* :class:`Spec` -- a compliance standard's full rule catalogue.  Holds the
  standard id/code/title, general help URL (used as a fallback when a rule has
  no rule-specific URL), the categories and rules, and the SARIF taxonomy
  identifiers.

Rule identifiers follow the ``SBOM-[SPEC]-[CATEGORY]-[NNN]`` convention
documented in ``RULES.md``.  ``SPEC`` is the uppercased :attr:`Spec.spec_id`
(e.g. ``NTIA``, ``FSCT3``) -- the edition is part of the id because each
edition is a distinct standard with its own requirements; ``CATEGORY`` is
:attr:`SpecCategory.code` (e.g. ``DF``, ``COMP``); ``NNN`` is
:attr:`SpecRule.number` zero-padded to three digits.
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
    lowercase spec code** to avoid cross-spec collisions.  Example:
    ``"ntia-component-supplier-name"``, ``"fsct-component-name"``."""

    # -- Spec mapping (location in the source spec) -----------------------

    spec_category: str
    """Id of the :class:`SpecCategory` this rule belongs to (matches
    :attr:`SpecCategory.id`).  Determines the ``CATEGORY`` segment of the
    rule id (via the category's ``code``) and the category taxon the rule's
    ``relationships`` point at."""

    spec_clause_number: str = ""
    """Literal clause / section designator from the source spec (e.g. ``"IV"``
    or ``"2.2.2.7"``).  Becomes the id of the rule's clause taxon and -- when
    paired with :attr:`Spec.sarif_clause_taxonomy_name` -- a SARIF taxonomy
    entry."""

    spec_clause_name: str = ""
    """Human-readable clause title (e.g. ``"License"``)."""

    spec_clause_url: str = ""
    """Deep link to the exact spec clause.  When empty, consumers fall back
    to :attr:`Spec.spec_uri` via :meth:`Spec.rule_uri`."""

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

    # -- Maturity / status ------------------------------------------------

    maturity: Maturity = "minimum-expected"
    """Spec-defined maturity level; drives the default SARIF severity."""

    status: Status = "active"
    """Whether the rule is emitted in the catalogue / as results.
    See :data:`Status` for semantics."""

    # -- The check --------------------------------------------------------

    probe: ProbeRef | None = None
    """Probe to run for this rule.  ``None`` for catalogue-only and TBD
    rules (they appear in the catalogue but no probe is invoked)."""

    # -- Output mappings --------------------------------------------------

    sarif_name: str
    """SARIF ``reportingDescriptor.name`` (PascalCase short name,
    e.g. ``NtiaComponentSupplierMissing``)."""

    oscal_control_id: str = ""
    """Optional override for the future OSCAL ``control-id``.  When empty,
    the OSCAL exporter is expected to lowercase the SARIF rule id."""

    json_group: str | None = None
    """JSON output group / key prefix (e.g. ``"aiPackages"``).  ``None`` means
    the rule, if emitted, lives at the top level of the JSON output."""

    json_key: str | None = None
    """JSON output key within ``json_group``.  ``None`` means the rule is
    not emitted in JSON output."""


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

    # -- Identity ---------------------------------------------------------

    spec_id: str
    """Compliance-standard identifier, e.g. ``"ntia"`` / ``"fsct3"``.  Registry
    key, YAML filename, and the value emitted in SARIF
    ``run.properties.complianceStandard``.  Its uppercase form is the ``SPEC``
    segment of every rule id, so it must be a hyphen-free, uppercase-safe
    token (lowercase ASCII letters/digits, starting with a letter)."""

    spec_title: str
    """Human-readable standard name, e.g. ``"2021 NTIA SBOM Minimum
    Elements"``."""

    spec_uri: str = ""
    """General documentation URL for the standard.  Used as the fallback
    when a :class:`SpecRule` does not provide its own ``spec_clause_url``."""

    # -- Content ----------------------------------------------------------

    categories: tuple[SpecCategory, ...] = field(default_factory=tuple)
    """The standard's categories / clusters.  Each becomes a SARIF taxon in
    the category taxonomy."""

    rules: tuple[SpecRule, ...] = field(default_factory=tuple)
    """The standard's rule catalogue.  Rules with ``status == "tbd"`` are
    excluded from SARIF emission entirely; rules with
    ``status == "catalogue-only"`` appear in the catalogue but never as
    results."""

    # -- SARIF taxonomy ---------------------------------------------------

    sarif_category_taxonomy_name: str = ""
    """SARIF ``ToolComponent.name`` of the *category* taxonomy
    (e.g. ``"ntia-minimum-elements"``).  Doubles as the OSCAL catalog id."""

    sarif_clause_taxonomy_name: str = ""
    """SARIF ``ToolComponent.name`` of the *clause* taxonomy
    (e.g. ``"ntia-clauses"``).  Each taxon id is a literal spec clause number
    from :attr:`SpecRule.spec_clause_number`.  Empty disables the clause
    taxonomy and the second ``equal`` relationship on every rule."""

    # -- Derived helpers --------------------------------------------------

    def category(self, category_id: str) -> SpecCategory:
        """Look up a :class:`SpecCategory` by id; raise KeyError if absent."""
        for cat in self.categories:
            if cat.id == category_id:
                return cat
        raise KeyError(f"Spec {self.spec_id!r} has no category {category_id!r}")

    def rule_id(self, rule: SpecRule) -> str:
        """Compose the canonical ``SBOM-[SPEC]-[CAT]-[NNN]`` rule id.

        The ``SPEC`` segment is :attr:`spec_id` uppercased.
        """
        cat = self.category(rule.spec_category)
        return f"SBOM-{self.spec_id.upper()}-{cat.code}-{rule.number:03d}"

    def oscal_control_id(self, rule: SpecRule) -> str:
        """Return the rule's OSCAL control id (override or lowercased rule id)."""
        return rule.oscal_control_id or self.rule_id(rule).lower()

    def sarif_level(self, rule: SpecRule) -> str:
        """SARIF default ``level`` derived from maturity."""
        return _MATURITY_TO_SARIF_LEVEL[rule.maturity]

    def rule_uri(self, rule: SpecRule) -> str:
        """Rule's source-spec clause URL if set, otherwise the standard URL."""
        return rule.spec_clause_url or self.spec_uri

    def emitted_rules(self) -> tuple[SpecRule, ...]:
        """Rules that appear in the SARIF catalogue (everything except TBD)."""
        return tuple(r for r in self.rules if r.status != "tbd")

    def active_rules(self) -> tuple[SpecRule, ...]:
        """Rules whose findings are actually emitted (excludes TBD + catalogue-only)."""
        return tuple(r for r in self.rules if r.status == "active")
