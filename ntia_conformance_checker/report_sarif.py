# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""SARIF 2.1.0 output builder for BaseChecker results.

Reads the checker's ``_SPEC`` (a :class:`Spec` of :class:`SpecRule` entries)
as the single source of truth for the rule catalogue.

The emitted log contains two taxonomies:

1. **Category taxonomy** -- ``ToolComponent`` whose name is
   :attr:`Spec.sarif_category_taxonomy_name` (e.g. ``ntia-minimum-elements``).
   One taxon per :class:`SpecCategory`.  Each rule has a ``relationships``
   entry with ``kinds: ["superset"]`` pointing at its category taxon.

2. **Clause taxonomy** -- ``ToolComponent`` whose name is
   :attr:`Spec.sarif_clause_taxonomy_name` (e.g. ``ntia-clauses``).  One
   taxon per distinct :attr:`SpecRule.spec_clause_number` value.  Each rule
   has a second ``relationships`` entry with ``kinds: ["equal"]`` pointing at
   its clause taxon.  Disabled if the spec leaves the clause taxonomy name
   empty.

Rule and taxon ids are OSCAL-control-id-shaped (see ``RULES.md``) so a future
``output_oscal()`` exporter can reuse them as ``catalog`` / ``group`` /
``control`` ids without remapping.
"""

from __future__ import annotations

import base64
import os
from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .base_checker import BaseChecker
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
    return os.path.basename(path) if path else ""


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


def _logical_location_for_component(name: str, spdx_id: str) -> dict[str, Any]:
    return {
        "name": name if name else spdx_id,
        "fullyQualifiedName": spdx_id if spdx_id else name,
        "kind": "package",
    }


# ---- Rule emission --------------------------------------------------------


def _rule_relationships(spec: "Spec", rule: "SpecRule") -> list[dict[str, Any]]:
    """Build the ``relationships`` list for a rule.

    Always includes a ``superset`` relationship pointing at the rule's
    category taxon.  If the spec defines a clause taxonomy *and* the rule has
    a ``spec_clause_number``, also includes an ``equal`` relationship pointing
    at the clause taxon.
    """
    rels: list[dict[str, Any]] = [
        {
            "target": {
                "id": rule.spec_category,
                "toolComponent": {"name": spec.sarif_category_taxonomy_name},
            },
            "kinds": ["superset"],
        }
    ]
    if spec.sarif_clause_taxonomy_name and rule.spec_clause_number:
        rels.append(
            {
                "target": {
                    "id": rule.spec_clause_number,
                    "toolComponent": {"name": spec.sarif_clause_taxonomy_name},
                },
                "kinds": ["equal"],
            }
        )
    return rels


def _emit_rule(spec: "Spec", rule: "SpecRule") -> dict[str, Any]:
    """Build a SARIF ``reportingDescriptor`` for ``rule``."""
    rule_id = spec.rule_id(rule)
    short_text = rule.warning or f"{rule.element_description.capitalize()} is missing."
    descriptor: dict[str, Any] = {
        "id": rule_id,
        "name": rule.sarif_name,
        "shortDescription": {"text": short_text},
        "fullDescription": {
            "text": (
                f"The SBOM must provide {rule.element_description}.  "
                "A result is emitted for every component (or once at the "
                "document level) where this element is absent."
            )
        },
        "defaultConfiguration": {"level": spec.sarif_level(rule)},
        "helpUri": spec.rule_uri(rule),
        "relationships": _rule_relationships(spec, rule),
        "properties": {
            "slug": rule.slug,
            "elementId": rule.element_id,
            "specCategory": rule.spec_category,
            "maturity": rule.maturity,
            "status": rule.status,
            "specClauseNumber": rule.spec_clause_number,
            "specClauseName": rule.spec_clause_name,
            "oscalControlId": spec.oscal_control_id(rule),
        },
    }
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
                    f"{spec.spec_title} clause {rule.spec_clause_number}"
                    + (f": {rule.spec_clause_name}." if rule.spec_clause_name else ".")
                )
            },
        }
    return list(seen.values())


def _taxonomies(spec: "Spec") -> list[dict[str, Any]]:
    """Build the ``taxonomies`` array (category + optional clause)."""
    category_taxonomy: dict[str, Any] = {
        "name": spec.sarif_category_taxonomy_name,
        "informationUri": spec.spec_uri or TOOL_URI,
        "shortDescription": {
            "text": (
                f"The set of {spec.spec_title} categories (clusters / groups) "
                "this checker emits rules for."
            )
        },
        "taxa": [_category_taxon(c, spec.spec_title) for c in spec.categories],
    }
    taxonomies: list[dict[str, Any]] = [category_taxonomy]

    if spec.sarif_clause_taxonomy_name:
        clause_taxa = _clause_taxa(spec)
        if clause_taxa:
            taxonomies.append(
                {
                    "name": spec.sarif_clause_taxonomy_name,
                    "informationUri": spec.spec_uri or TOOL_URI,
                    "shortDescription": {
                        "text": (
                            f"Individual clauses of {spec.spec_title}; each taxon "
                            "id is a literal spec clause number."
                        )
                    },
                    "taxa": clause_taxa,
                }
            )
    return taxonomies


# ---- Result emission ------------------------------------------------------


# pylint: disable=too-many-arguments,too-many-positional-arguments
def _component_result(
    rule_id: str,
    rule: "SpecRule",
    level: str,
    name: str,
    spdx_id: str,
    artifact_uri: str,
) -> dict[str, Any]:
    label = name if name else spdx_id
    message_text = (
        f"Component '{label}' ({spdx_id}) is missing a {rule.element_description}."
        if spdx_id and name
        else f"Component '{label}' is missing a {rule.element_description}."
    )
    return {
        "ruleId": rule_id,
        "level": level,
        "message": {"text": message_text},
        "locations": [
            {
                "logicalLocations": [_logical_location_for_component(name, spdx_id)],
                "physicalLocation": {
                    "artifactLocation": {"uri": artifact_uri, "index": 0}
                },
            }
        ],
    }


def _document_result(
    rule_id: str, rule: "SpecRule", level: str, artifact_uri: str
) -> dict[str, Any]:
    return {
        "ruleId": rule_id,
        "level": level,
        "message": {"text": f"SBOM document is missing {rule.element_description}."},
        "locations": [
            {
                "logicalLocations": [{"name": "document", "kind": "module"}],
                "physicalLocation": {
                    "artifactLocation": {"uri": artifact_uri, "index": 0}
                },
            }
        ],
    }


def _results_for_rule(
    checker: "BaseChecker", spec: "Spec", rule: "SpecRule", artifact_uri: str
) -> list[dict[str, Any]]:
    """Emit zero or more SARIF results for one rule.

    Reads ``checker.findings[rule_id]`` (populated by
    :meth:`BaseChecker.run_probes`) so the SARIF output reflects exactly
    what the rule's probe produced.  Catalogue-only and TBD rules never
    emit results -- :meth:`BaseChecker.run_probes` skips them, and any
    accidental entry in ``findings`` for them is ignored here too.
    """
    if rule.status != "active":
        return []

    rule_id = spec.rule_id(rule)
    level = spec.sarif_level(rule)
    findings = getattr(checker, "findings", {}).get(rule_id, []) or []

    results: list[dict[str, Any]] = []
    for finding in findings:
        if finding.is_document_level:
            results.append(_document_result(rule_id, rule, level, artifact_uri))
        else:
            results.append(
                _component_result(
                    rule_id,
                    rule,
                    level,
                    finding.component_name or "",
                    finding.component_id or "",
                    artifact_uri,
                )
            )
    return results


# ---- Notifications --------------------------------------------------------


def _notifications(checker: "BaseChecker") -> list[dict[str, Any]]:
    notes: list[dict[str, Any]] = []
    for err in getattr(checker, "_parsing_errors", []) or []:
        notes.append(
            {
                "level": "error",
                "message": {"text": str(err)},
                "descriptor": {"id": "spdx.parsing-error"},
            }
        )
    for msg in getattr(checker, "_validation_messages", []) or []:
        notes.append(
            {
                "level": "warning",
                "message": {"text": str(getattr(msg, "validation_message", msg))},
                "descriptor": {"id": "spdx.validation-message"},
            }
        )
    return notes


# ---- Top-level builder ----------------------------------------------------


def build_sarif(checker: "BaseChecker", *, embed_sbom: bool = False) -> dict[str, Any]:
    """Build a SARIF 2.1.0 log dict for *checker*.

    Walks ``checker._SPEC.emitted_rules()`` to emit the rule catalogue (every
    non-TBD rule, even if zero findings), then one result per
    (active rule, failing component) pair and one per failing document-level
    rule.  Catalogue-only rules appear in the catalogue but never as results.

    Args:
        checker: Checker instance whose ``_SPEC`` and missing-element
            attributes provide the data.
        embed_sbom: When ``True``, read the input SBOM file and place its
            contents in ``runs[0].artifacts[0].contents`` (SARIF §3.24.7).
            This silences SARIF2013 ("This run does not provide embedded
            file content") and lets downstream viewers render the source
            artifact alongside results, at the cost of a larger log file.
            Default is ``False`` (link by URI only).
    """
    spec: Spec | None = getattr(checker, "spec", None)
    if spec is None:  # pragma: no cover -- checkers must expose a spec.
        raise ValueError(
            f"Checker {type(checker).__name__} has no spec; "
            "SARIF output requires a Spec instance."
        )

    # Ensure findings are populated; idempotent if subclasses already
    # called run_probes() in __init__.
    if not getattr(checker, "findings", None):
        checker.run_probes()

    artifact_uri = _artifact_uri(checker)
    emitted = spec.emitted_rules()
    rules_emitted = [_emit_rule(spec, rule) for rule in emitted]
    results = [
        result
        for rule in emitted
        for result in _results_for_rule(checker, spec, rule, artifact_uri)
    ]
    parsing_errors = getattr(checker, "_parsing_errors", [])

    supported_taxonomies = [{"name": spec.sarif_category_taxonomy_name}]
    if spec.sarif_clause_taxonomy_name:
        supported_taxonomies.append({"name": spec.sarif_clause_taxonomy_name})

    run: dict[str, Any] = {
        "tool": {
            "driver": {
                "name": TOOL_NAME,
                "version": _tool_version(),
                "informationUri": TOOL_URI,
                "rules": rules_emitted,
                "supportedTaxonomies": supported_taxonomies,
            }
        },
        "taxonomies": _taxonomies(spec),
        "results": results,
        "invocations": [
            {
                "executionSuccessful": not bool(parsing_errors),
                "toolExecutionNotifications": _notifications(checker),
            }
        ],
        "properties": {
            "sbomSpec": getattr(checker, "sbom_spec", "") or "",
            "sbomName": getattr(checker, "sbom_name", "") or "",
            "complianceStandard": spec.spec_id,
        },
    }

    if artifact_uri:
        artifact: dict[str, Any] = {"location": {"uri": artifact_uri}}
        source_path = getattr(checker, "file", "") or ""
        if embed_sbom and source_path:
            contents = _artifact_contents(source_path)
            if contents is not None:
                sbom_spec_hint = str(getattr(checker, "sbom_spec", "") or "")
                artifact["mimeType"] = _sbom_mime_type(source_path, sbom_spec_hint)
                artifact["contents"] = contents
        run["artifacts"] = [artifact]

    return {
        "version": SARIF_VERSION,
        "$schema": SARIF_SCHEMA,
        "runs": [run],
    }
