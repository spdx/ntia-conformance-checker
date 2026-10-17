# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""SARIF 2.1.0 output builder.

Every checker gets the base log: tool, artifact, parse/validation/graph
notifications and the run properties (standard, verdict). A checker that has a
:class:`Spec` and per-rule outcomes (``RuleBasedChecker``) also gets the rule
catalogue, the taxonomies and one result per failing component.

* The rule ``id`` is the ontology SARIF rule id (``BOM-NTIA2021-DF-001``,
  ``BOM-G7AI2026-MDL-006.1``), see :meth:`Spec.rule_id`.
* The *category taxonomy* has one taxon per :class:`SpecCategory`; each rule has
  a ``superset`` relationship to its category. The optional *clause taxonomy*
  has one taxon per spec clause, with an ``equal`` relationship for a clause
  of one rule and a ``superset`` one for a clause shared by several.
* Roll-up rules (``any-of`` / ``all-of``) are linked to their sub-rules (see
  :func:`_sub_rule_kinds`). A roll-up reports its failing components itself, so
  its sub-rules emit no results of their own.
* Only ``missing`` outcomes produce results; not-applicable and out-of-scope
  rules appear in the catalogue only.
"""

from __future__ import annotations

import base64
import os
from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

if TYPE_CHECKING:
    from .base_checker import BaseChecker
    from .model import Finding, RuleResult
    from .spec import Spec, SpecCategory, SpecRule

SARIF_VERSION = "2.1.0"
SARIF_SCHEMA = "https://json.schemastore.org/sarif-2.1.0.json"
TOOL_NAME = "ntia-conformance-checker"
TOOL_URI = "https://github.com/spdx/ntia-conformance-checker"


# Fallback MIME type when nothing more specific applies.
_DEFAULT_MIME_TYPE = "application/octet-stream"

# Extension-to-MIME mapping for non-ambiguous SBOM serialisation formats.
# Each entry is (tuple-of-suffixes, mime-type); checked in order so that
# double-extensions like ".rdf.xml" are tested before the shorter ".xml".
_SBOM_EXT_MIME: tuple[tuple[tuple[str, ...], str], ...] = (
    ((".rdf.xml", ".rdf"), "application/rdf+xml"),
    ((".xml",), "application/xml"),
    ((".yaml", ".yml"), "application/yaml"),
    ((".spdx",), "text/plain"),
)


# ---- Helpers --------------------------------------------------------------


def _tool_version() -> str:
    try:
        return version("ntia-conformance-checker")
    except PackageNotFoundError:
        return "0.0.0"


def _artifact_uri(checker: "BaseChecker") -> str:
    """Use the input file's basename as the artifact URI."""
    path = getattr(checker, "file", "") or ""
    return quote(os.path.basename(path)) if path else ""


def _sbom_mime_type(path: str, sbom_spec: str = "") -> str:
    """Return a best-guess MIME type for an SBOM file.

    Uses the file extension and -- when ambiguous -- the ``sbom_spec`` hint
    (``"spdx2"`` or ``"spdx3"``).  The registry situation is uneven:

    * ``application/spdx+json`` is registered with IANA, but **only covers
      SPDX 2.x**.  An ``application/spdx3+json`` registration has been
      submitted but not yet approved, so SPDX 3 JSON-LD falls back to the
      registered generic ``application/ld+json``.
    * SPDX 2 XML (a bespoke XML schema, not RDF) has no registered MIME
      type; ``application/xml`` is the safest accurate value.
    * SPDX 2 RDF/XML (often suffixed ``.rdf.xml``) uses the registered
      ``application/rdf+xml``.
    * Tag-value (``.spdx``) has no registered MIME type; ``text/plain``
      is closest.
    * CycloneDX uses ``application/vnd.cyclonedx+json`` (registered) for
      JSON; unimplemented here since this tool currently only emits SPDX.
    """
    lower = path.lower()
    for exts, mime in _SBOM_EXT_MIME:
        if any(lower.endswith(e) for e in exts):
            return mime
    if lower.endswith(".json"):
        # SPDX 3 is JSON-LD; SPDX 2 has its own registered JSON MIME type.
        return (
            "application/ld+json" if sbom_spec == "spdx3" else "application/spdx+json"
        )
    return _DEFAULT_MIME_TYPE


def _artifact_contents(path: str) -> dict[str, Any] | None:
    """Read ``path`` and return a SARIF ``artifact.contents`` object.

    Tries UTF-8 first (every SPDX serialisation in active use today is text).
    Falls back to base64 binary for anything that does not decode cleanly so
    the embed flag still works for unusual inputs.  Returns ``None`` if the
    file cannot be opened.
    """
    try:
        with open(path, "rb") as handle:
            data = handle.read()
    except OSError:
        return None
    try:
        return {"text": data.decode("utf-8")}
    except UnicodeDecodeError:
        return {"binary": base64.b64encode(data).decode("ascii")}


def _artifact_location(uri: str) -> dict[str, Any]:
    """The artifact location; ``index`` only when the run lists the artifact."""
    return {"uri": uri, "index": 0} if uri else {}


def _logical_location_for_component(name: str, spdx_id: str) -> dict[str, Any]:
    return {
        "name": name if name else spdx_id,
        "fullyQualifiedName": spdx_id if spdx_id else name,
        "kind": "package",
    }


# ---- Rule emission --------------------------------------------------------


def _sub_rules(spec: "Spec", rule: "SpecRule") -> list["SpecRule"]:
    """The emitted sub-rules of ``rule``."""
    return [r for r in spec.rules if r.parent == rule.slug and r.status != "tbd"]


def _parent_rule(spec: "Spec", rule: "SpecRule") -> "SpecRule | None":
    """The emitted parent of a sub-rule, if any."""
    parent = next((r for r in spec.rules if r.slug == rule.parent), None)
    return parent if parent is not None and parent.status != "tbd" else None


def _rule_relationships(spec: "Spec", rule: "SpecRule") -> list[dict[str, Any]]:
    """Build the ``relationships`` list for a rule.

    A ``superset`` relationship to the rule's category taxon; one to its clause
    taxon (``equal`` for a clause of one rule, else ``superset``) when the spec
    has a clause taxonomy and the rule a clause number; then the parent /
    sub-rule links, whose kinds follow the parent's aggregation (see
    :func:`_sub_rule_kinds`).
    """
    rels: list[dict[str, Any]] = []
    if spec.taxonomies.category:
        rels.append(
            {
                "target": {
                    "id": rule.spec_category,
                    "toolComponent": {"name": spec.taxonomies.category},
                },
                "kinds": ["superset"],
            }
        )
    if spec.taxonomies.clause and rule.spec_clause_number:
        shared = sum(
            r.spec_clause_number == rule.spec_clause_number
            for r in spec.emitted_rules()
        )
        rels.append(
            {
                "target": {
                    "id": rule.spec_clause_number,
                    "toolComponent": {"name": spec.taxonomies.clause},
                },
                "kinds": ["superset" if shared > 1 else "equal"],
            }
        )
    to_sub, _ = _sub_rule_kinds(rule)
    for sub in _sub_rules(spec, rule):
        # A sub-rule that is not checked never reports, so no containment holds.
        kind = to_sub if sub.status == "active" else "relevant"
        rels.append({"target": {"id": spec.rule_id(sub)}, "kinds": [kind]})
    parent = _parent_rule(spec, rule)
    if parent is not None:
        _, to_parent = _sub_rule_kinds(parent)
        kind = to_parent if rule.status == "active" else "relevant"
        rels.append({"target": {"id": spec.rule_id(parent)}, "kinds": [kind]})
    return rels


def _sub_rule_kinds(parent: "SpecRule") -> tuple[str, str]:
    """SARIF relationship kinds ``(parent -> sub-rule, sub-rule -> parent)``.

    SARIF 2.1.0 Sec. 3.53.3 reads a kind as the *target's* set of results
    relative to the *source's*:

    * ``any-of`` -- the parent fails on a target only where every sub-rule fails,
      so each sub-rule's results contain the parent's: parent -> sub-rule is
      ``superset``, sub-rule -> parent is ``subset``.
    * ``all-of`` -- the parent fails wherever any sub-rule fails, so its results
      contain each sub-rule's: parent -> sub-rule is ``subset``, sub-rule ->
      parent is ``superset``.
    * no aggregation -- the parent is checked by its own probe and its
      sub-rules only refine it, so their results are unrelated: ``relevant``
      both ways.
    """
    if parent.aggregation == "any-of":
        return "superset", "subset"
    if parent.aggregation == "all-of":
        return "subset", "superset"
    return "relevant", "relevant"


_MODAL = {"requirement": "must", "recommendation": "should", "permission": "may"}


def _emit_rule(spec: "Spec", rule: "SpecRule") -> dict[str, Any]:
    """Build a SARIF ``reportingDescriptor`` for ``rule``."""
    rule_id = spec.rule_id(rule)
    what = rule.element_description or rule.slug
    short_text = rule.warning or f"{what.capitalize()} is missing."
    descriptor: dict[str, Any] = {
        "id": rule_id,
        "name": spec.report_name(rule),
        "shortDescription": {"text": short_text},
        "fullDescription": {
            "text": (
                f"The SBOM {_MODAL[rule.provision]} provide {what}.  "
                "A result is emitted for each component, or for the document, "
                "where this is absent."
            )
        },
        "defaultConfiguration": {"level": spec.severity(rule)},
        "helpUri": spec.rule_uri(rule),
        "relationships": _rule_relationships(spec, rule),
        "properties": {
            "slug": rule.slug,
            "elementId": rule.element_id,
            "specCategory": rule.spec_category,
            "maturityLevel": rule.maturity,
            "maturity": spec.maturity_id(rule),
            "provision": rule.provision,
            "status": rule.status,
            "specClauseNumber": rule.spec_clause_number,
            "specClauseName": rule.spec_clause_name,
            "oscalControlId": spec.oscal_control_id(rule),
        },
    }
    if rule.aggregation:
        descriptor["properties"]["aggregation"] = rule.aggregation
    return descriptor


# ---- Taxonomy emission ----------------------------------------------------


def _category_taxon(category: "SpecCategory", spec_title: str) -> dict[str, Any]:
    """Build a SARIF taxon for a :class:`SpecCategory`."""
    short = category.description or f"{category.title} category of {spec_title}."
    return {
        "id": category.id,
        "name": category.title,
        "shortDescription": {"text": short},
    }


def _clause_taxa(spec: "Spec") -> list[dict[str, Any]]:
    """Build one taxon per distinct spec_clause_number in the emitted rules.

    Order follows the first occurrence of each spec_clause_number in
    :meth:`Spec.emitted_rules`.
    """
    seen: dict[str, dict[str, Any]] = {}
    for rule in spec.emitted_rules():
        if not rule.spec_clause_number or rule.spec_clause_number in seen:
            continue
        seen[rule.spec_clause_number] = {
            "id": rule.spec_clause_number,
            "name": rule.spec_clause_name or rule.spec_clause_number,
            "shortDescription": {
                "text": (
                    f"{spec.title} clause {rule.spec_clause_number}"
                    + (f": {rule.spec_clause_name}." if rule.spec_clause_name else ".")
                )
            },
        }
    return list(seen.values())


def _taxonomies(spec: "Spec") -> list[dict[str, Any]]:
    """Build the ``taxonomies`` array (category + optional clause)."""
    taxonomies: list[dict[str, Any]] = []
    if spec.taxonomies.category:
        taxonomies.append(_category_taxonomy(spec))
    if spec.taxonomies.clause:
        clause_taxa = _clause_taxa(spec)
        if clause_taxa:
            taxonomies.append(_clause_taxonomy(spec, clause_taxa))
    return taxonomies


def _category_taxonomy(spec: "Spec") -> dict[str, Any]:
    """The category taxonomy: one taxon per category."""
    return {
        "name": spec.taxonomies.category,
        "informationUri": spec.uri or TOOL_URI,
        "shortDescription": {
            "text": (
                f"The set of {spec.title} categories (clusters / groups) "
                "this checker emits rules for."
            )
        },
        "taxa": [_category_taxon(c, spec.title) for c in spec.categories],
    }


def _clause_taxonomy(spec: "Spec", taxa: list[dict[str, Any]]) -> dict[str, Any]:
    """The clause taxonomy: one taxon per spec clause."""
    return {
        "name": spec.taxonomies.clause,
        "informationUri": spec.uri or TOOL_URI,
        "shortDescription": {
            "text": (
                f"Individual clauses of {spec.title}; each taxon id is a "
                "literal spec clause number."
            )
        },
        "taxa": taxa,
    }


# ---- Result emission ------------------------------------------------------


def _component_result(
    rule_id: str, severity: str, message: str, finding: "Finding", artifact_uri: str
) -> dict[str, Any]:
    """One result for a failing component."""
    name, spdx_id = finding.component_name or "", finding.component_id or ""
    return {
        "ruleId": rule_id,
        "level": severity,
        "message": {"text": message},
        "locations": [
            {
                "logicalLocations": [_logical_location_for_component(name, spdx_id)],
                "physicalLocation": {
                    "artifactLocation": _artifact_location(artifact_uri)
                },
            }
        ],
    }


def _document_result(
    rule_id: str, severity: str, message: str, artifact_uri: str
) -> dict[str, Any]:
    """One result for the SBOM document itself."""
    return {
        "ruleId": rule_id,
        "level": severity,
        "message": {"text": message},
        "locations": [
            {
                "logicalLocations": [{"name": "document", "kind": "module"}],
                "physicalLocation": {
                    "artifactLocation": _artifact_location(artifact_uri)
                },
            }
        ],
    }


def _finding_message(rule: "SpecRule", finding: "Finding") -> str:
    """The text of a result: the finding's note, else the rule's wording."""
    if finding.note:
        return finding.note
    what = rule.element_description or rule.slug
    if finding.is_document_level:
        return f"SBOM document is missing {what}."
    name = finding.component_name or finding.component_id
    return f"Component '{name}' is missing {what}."


def _is_rolled_up(spec: "Spec", rule: "SpecRule") -> bool:
    """Whether ``rule`` is a sub-rule whose any-of / all-of parent reports for it."""
    parent = next((r for r in spec.rules if r.slug == rule.parent), None)
    return parent is not None and parent.aggregation in ("any-of", "all-of")


def _results_for_rules(
    spec: "Spec",
    outcomes: dict[str, "RuleResult"],
    artifact_uri: str,
    maturity: int,
) -> list[dict[str, Any]]:
    """The results of every in-scope rule whose outcome is ``missing``."""
    results: list[dict[str, Any]] = []
    for rule in spec.active_rules(maturity):
        rule_id = spec.rule_id(rule)
        outcome = outcomes.get(rule_id)
        if outcome is None or outcome.outcome != "missing":
            continue
        if _is_rolled_up(spec, rule):
            continue
        severity = spec.severity(rule)
        for finding in outcome.findings:
            message = _finding_message(rule, finding)
            results.append(
                _document_result(rule_id, severity, message, artifact_uri)
                if finding.is_document_level
                else _component_result(
                    rule_id, severity, message, finding, artifact_uri
                )
            )
    return results


# ---- Notifications --------------------------------------------------------


def _notifications(checker: "BaseChecker") -> list[dict[str, Any]]:
    """Parse, validation and graph problems as tool execution notifications."""
    notes: list[dict[str, Any]] = []

    def add(level: str, text: str, descriptor: str) -> None:
        notes.append(
            {
                "level": level,
                "message": {"text": text},
                "descriptor": {"id": descriptor},
            }
        )

    errors = getattr(checker, "_parsing_errors", []) or []
    for err in errors:
        add("error", str(err), "spdx.parsing-error")
    if not errors and not getattr(checker, "doc", None):
        add("error", "The SBOM could not be read.", "spdx.parsing-error")
    for msg in getattr(checker, "_validation_messages", []) or []:
        add(
            "warning",
            str(getattr(msg, "validation_message", msg)),
            "spdx.validation-message",
        )
    floating = getattr(checker, "floating_component_ids", None) or ()
    if floating:
        add(
            "warning",
            f"{len(floating)} component(s) are not connected to the SBOM root "
            "and were not evaluated.",
            "spdx.floating-component",
        )
    if getattr(checker, "has_unknown_pointers", False):
        add(
            "warning",
            "Some relationships point to elements that are not in the SBOM.",
            "spdx.unknown-pointer",
        )
    return notes


# ---- Top-level builder ----------------------------------------------------


def _spec_of(checker: "BaseChecker") -> "Spec | None":
    """The checker's spec when it reports per-rule outcomes, else ``None``."""
    spec = getattr(checker, "spec", None)
    return spec if spec is not None and hasattr(checker, "rule_results") else None


def _artifact_entry(
    checker: "BaseChecker", artifact_uri: str, embed_sbom: bool
) -> dict[str, Any]:
    """The run's artifact; with ``embed_sbom``, also the input file's contents."""
    artifact: dict[str, Any] = {"location": {"uri": artifact_uri}}
    source_path = getattr(checker, "file", "") or ""
    if embed_sbom and source_path:
        contents = _artifact_contents(source_path)
        if contents is not None:
            hint = str(getattr(checker, "sbom_spec", "") or "")
            artifact["mimeType"] = _sbom_mime_type(source_path, hint)
            artifact["contents"] = contents
    return artifact


def build_sarif(
    checker: "BaseChecker",
    *,
    compliant: bool,
    embed_sbom: bool = False,
    maturity: int = 0,
) -> dict[str, Any]:
    """Build a SARIF 2.1.0 log dict for ``checker``.

    Args:
        checker: The checker whose results to report.
        compliant: The checker's verdict at ``maturity``.
        embed_sbom: Put the input file's contents in ``runs[0].artifacts[0]``
            (SARIF 3.24.7), at the cost of a larger log. Default is a link by URI.
        maturity: Target maturity level; rules above it are out of scope.
    """
    spec = _spec_of(checker)
    artifact_uri = _artifact_uri(checker)
    driver: dict[str, Any] = {
        "name": TOOL_NAME,
        "version": _tool_version(),
        "informationUri": TOOL_URI,
    }
    run: dict[str, Any] = {"tool": {"driver": driver}, "results": []}
    outcomes: dict[str, RuleResult] = {}
    if spec is not None:
        emitted = spec.emitted_rules()
        driver["rules"] = [_emit_rule(spec, rule) for rule in emitted]
        taxonomies = _taxonomies(spec)
        if taxonomies:
            driver["supportedTaxonomies"] = [{"name": t["name"]} for t in taxonomies]
            run["taxonomies"] = taxonomies
        outcomes = getattr(checker, "rule_results")()
        run["results"] = _results_for_rules(spec, outcomes, artifact_uri, maturity)
    notifications = _notifications(checker)
    if spec is not None and not any(
        o.outcome in ("present", "missing") for o in outcomes.values()
    ):
        notifications.append(
            {
                "level": "warning",
                "message": {"text": f"No requirement of {spec.title} applies."},
                "descriptor": {"id": "sbom.nothing-applies"},
            }
        )
    run["invocations"] = [
        {
            "executionSuccessful": bool(getattr(checker, "doc", None)),
            "toolExecutionNotifications": notifications,
        }
    ]
    run["properties"] = {
        "sbomSpec": getattr(checker, "sbom_spec", "") or "",
        "sbomName": getattr(checker, "sbom_name", "") or "",
        "complianceStandard": (
            spec.id if spec is not None else checker.compliance_standard
        ),
        "maturityTarget": maturity,
        "conformant": compliant,
        "componentsEvaluated": bool(getattr(checker, "components_evaluated", False)),
        "ruleResults": spec is not None,
    }
    if spec is not None:
        run["properties"]["ruleOutcomes"] = {k: v.outcome for k, v in outcomes.items()}
    if artifact_uri:
        run["artifacts"] = [_artifact_entry(checker, artifact_uri, embed_sbom)]
    return {"version": SARIF_VERSION, "$schema": SARIF_SCHEMA, "runs": [run]}
