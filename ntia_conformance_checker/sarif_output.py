# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""SARIF output builder for BaseChecker results.

The Static Analysis Results Interchange Format (SARIF) is a standardized,
JSON-based data format used to share and aggregate the outputs of static
analysis tools (like security scanners and linters).
https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html

Reads the checker's ``_SPEC`` (:class:`Spec` of :class:`SpecRule` entries)
as the single source of truth for the rule catalogue.

Rule ids and taxon ids are chosen so they can double as OSCAL
``control`` / ``group`` ids in a future ``output_oscal()`` exporter
without remapping.
"""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any

from .constants import TOOL_NAME, TOOL_URI, TOOL_VERSION

if TYPE_CHECKING:
    from .base_checker import BaseChecker
    from .spec import Spec, SpecRule

SARIF_VERSION = "2.1.0"
SARIF_SCHEMA = "https://json.schemastore.org/sarif-2.1.0.json"


# ---- Helpers --------------------------------------------------------------


def _artifact_uri(checker: "BaseChecker") -> str:
    """Use the input file's basename as the artifact URI."""
    path = getattr(checker, "file", "") or ""
    return os.path.basename(path) if path else ""


def _logical_location_for_component(name: str, spdx_id: str) -> dict[str, Any]:
    return {
        "name": name if name else spdx_id,
        "fullyQualifiedName": spdx_id if spdx_id else name,
        "kind": "package",
    }


# ---- Rule emission --------------------------------------------------------


def _emit_rule(spec: "Spec", rule: "SpecRule") -> dict[str, Any]:
    """Build a SARIF ``reportingDescriptor`` for ``rule``."""
    descriptor: dict[str, Any] = {
        "id": rule.sarif_rule_id,
        "name": rule.sarif_rule_name,
        "shortDescription": {"text": f"{rule.element_name.capitalize()} is missing."},
        "fullDescription": {
            "text": (
                f"The SBOM must provide {rule.element_name}.  "
                "A result is emitted for every component (or once at the "
                "document level) where this element is absent."
            )
        },
        "defaultConfiguration": {"level": "error"},
        "helpUri": spec.rule_help_uri(rule),
        "help": {
            "text": (
                f"{rule.element_name.capitalize()} is required.  "
                f"See {spec.rule_help_uri(rule)}"
            ),
            "markdown": (
                f"**{rule.element_name.capitalize()}** is required.  "
                f"See <{spec.rule_help_uri(rule)}>"
            ),
        },
        "relationships": [
            {
                "target": {
                    "id": (
                        taxon.taxon_id if (taxon := spec.taxon_for_rule(rule)) else ""
                    ),
                    "toolComponent": {"name": spec.standard_id},
                },
                "kinds": ["superset"],
            }
        ],
    }
    return descriptor


# ---- Result emission ------------------------------------------------------


def _component_result(
    rule: "SpecRule",
    name: str,
    spdx_id: str,
    artifact_uri: str,
) -> dict[str, Any]:
    label = name if name else spdx_id
    message_text = (
        f"Component '{label}' ({spdx_id}) is missing a {rule.element_name}."
        if spdx_id and name
        else f"Component '{label}' is missing a {rule.element_name}."
    )
    return {
        "ruleId": rule.sarif_rule_id,
        "level": "error",
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


def _document_result(rule: "SpecRule", artifact_uri: str) -> dict[str, Any]:
    return {
        "ruleId": rule.sarif_rule_id,
        "level": "error",
        "message": {"text": f"SBOM document is missing {rule.element_name}."},
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
    checker: "BaseChecker", rule: "SpecRule", artifact_uri: str
) -> list[dict[str, Any]]:
    """Emit zero or more SARIF results for one rule."""
    if rule.kind == "list":
        missing: list[tuple[str, str]] = getattr(checker, rule.attr, []) or []
        return [
            _component_result(rule, comp_name or "", comp_id or "", artifact_uri)
            for comp_name, comp_id in missing
        ]

    # kind == "bool"
    if bool(getattr(checker, rule.attr, False)):
        return []
    return [_document_result(rule, artifact_uri)]


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


def build_sarif(checker: "BaseChecker") -> dict[str, Any]:
    """Build a SARIF log dict for *checker*.

    Walks ``checker.spec.rules`` to emit the rule catalogue (always, even
    if zero findings), then one result per (rule, failing component) pair
    and one per failing document-level rule.
    """
    spec = checker.spec

    artifact_uri = _artifact_uri(checker)
    rules_emitted = [_emit_rule(spec, rule) for rule in spec.rules]
    results = [
        result
        for rule in spec.rules
        for result in _results_for_rule(checker, rule, artifact_uri)
    ]
    parsing_errors = getattr(checker, "_parsing_errors", [])

    run: dict[str, Any] = {
        "automationDetails": {"id": f"{TOOL_NAME}/{spec.standard_short_id}/"},
        "tool": {
            "driver": {
                "name": TOOL_NAME,
                "fullName": "NTIA Minimum Elements SBOM Conformance Checker",
                "version": TOOL_VERSION,
                "informationUri": TOOL_URI,
                "rules": rules_emitted,
                "supportedTaxonomies": [{"name": spec.standard_id}],
            }
        },
        "taxonomies": [
            {
                "name": spec.standard_id,
                "informationUri": spec.help_uri or TOOL_URI,
                "taxa": [
                    {
                        "id": taxon.taxon_id,
                        "name": taxon.taxon_name,
                        "shortDescription": {
                            "text": (
                                f"The set of required minimum elements for "
                                f"{spec.standard_name} conformance."
                            )
                        },
                    }
                    for taxon in spec.taxa
                ],
            }
        ],
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
            "complianceStandard": spec.standard_short_id,
        },
    }

    if artifact_uri:
        run["artifacts"] = [{"location": {"uri": artifact_uri}}]

    return {
        "version": SARIF_VERSION,
        "$schema": SARIF_SCHEMA,
        "runs": [run],
    }
