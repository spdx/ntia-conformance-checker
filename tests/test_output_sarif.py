# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for SARIF output from BaseChecker."""

# pylint: disable=missing-function-docstring

from __future__ import annotations

import json
import os
from typing import Any, cast

import pytest

from ntia_conformance_checker import FSCT3Checker, NTIAChecker, sbom_checker

_HERE = os.path.dirname(__file__)

# NTIA rule ids per RULES.md (lowercase kebab category = data-fields).
NTIA_DF_COMPONENT_NAME = "SBOM-NTIA-DF-002"
NTIA_DF_COMPONENT_VERSION = "SBOM-NTIA-DF-003"
NTIA_DF_COMPONENT_IDENTIFIER = "SBOM-NTIA-DF-004"
NTIA_DF_COMPONENT_SUPPLIER = "SBOM-NTIA-DF-001"
NTIA_DF_DEPENDENCY = "SBOM-NTIA-DF-005"
NTIA_DF_AUTHOR = "SBOM-NTIA-DF-006"
NTIA_DF_TIMESTAMP = "SBOM-NTIA-DF-007"

# FSCT rule ids per RULES.md.
FSCT_COMP_CONCLUDED_LICENSE = "SBOM-FSCT3-COMP-007"
FSCT_COMP_COPYRIGHT_NOTICE = "SBOM-FSCT3-COMP-008"

NTIA_TAXONOMY_NAME = "ntia-minimum-elements"
NTIA_CLAUSE_TAXONOMY_NAME = "ntia-clauses"
FSCT_TAXONOMY_NAME = "fsct-baseline-attributes"
FSCT_CLAUSE_TAXONOMY_NAME = "fsct-clauses"


def _fixtures(subdir: str) -> list[str]:
    d = os.path.join(_HERE, "data", subdir)
    return [os.path.join(d, fn) for fn in os.listdir(d)]


def _run(sarif: dict[str, Any]) -> dict[str, Any]:
    assert sarif["version"] == "2.1.0"
    assert "$schema" in sarif
    assert len(sarif["runs"]) == 1
    runs = cast("list[dict[str, Any]]", sarif["runs"])
    return runs[0]


def _result_rule_ids(run: dict[str, Any]) -> list[str]:
    return [r["ruleId"] for r in run["results"]]


def _logical_names(run: dict[str, Any], rule_id: str) -> list[str]:
    return [
        r["locations"][0]["logicalLocations"][0]["fullyQualifiedName"]
        for r in run["results"]
        if r["ruleId"] == rule_id
    ]


# ---- Conformant fixtures -> zero results --------------------------------


@pytest.mark.parametrize("test_file", _fixtures("no_elements_missing"))
def test_sarif_no_elements_missing_ntia(test_file: str) -> None:
    sarif = sbom_checker.SbomChecker(test_file, compliance="ntia").output_sarif()
    run = _run(sarif)
    assert not run["results"]
    assert run["invocations"][0]["executionSuccessful"] is True
    assert run["properties"]["complianceStandard"] == "ntia"
    assert run["tool"]["driver"]["name"] == "ntia-conformance-checker"

    # All NTIA-DF rules present in the catalogue regardless of findings.
    rule_ids = {r["id"] for r in run["tool"]["driver"]["rules"]}
    assert {
        NTIA_DF_COMPONENT_SUPPLIER,
        NTIA_DF_COMPONENT_NAME,
        NTIA_DF_COMPONENT_VERSION,
        NTIA_DF_COMPONENT_IDENTIFIER,
        NTIA_DF_DEPENDENCY,
        NTIA_DF_AUTHOR,
        NTIA_DF_TIMESTAMP,
    } <= rule_ids

    # Two taxonomies emitted: categories + clauses.
    tax_names = [t["name"] for t in run["taxonomies"]]
    assert NTIA_TAXONOMY_NAME in tax_names
    assert NTIA_CLAUSE_TAXONOMY_NAME in tax_names

    # Category taxonomy carries every defined NTIA category.
    category_tax = next(t for t in run["taxonomies"] if t["name"] == NTIA_TAXONOMY_NAME)
    cat_ids = {t["id"] for t in category_tax["taxa"]}
    assert {"data-fields", "automation-support", "practices-and-processes"} <= cat_ids

    # Every emitted rule has at least the category-relationship.
    for rule in run["tool"]["driver"]["rules"]:
        kinds_to_targets = {
            tuple(rel["kinds"]): rel["target"] for rel in rule["relationships"]
        }
        # category relationship is mandatory
        assert ("superset",) in kinds_to_targets
        cat_target = kinds_to_targets[("superset",)]
        assert cat_target["toolComponent"]["name"] == NTIA_TAXONOMY_NAME
        assert cat_target["id"] in cat_ids
        # clause relationship is present when the rule has a spec_clause_number
        if rule["properties"]["specClauseNumber"]:
            assert ("equal",) in kinds_to_targets
            clause_target = kinds_to_targets[("equal",)]
            assert clause_target["toolComponent"]["name"] == NTIA_CLAUSE_TAXONOMY_NAME
            assert clause_target["id"] == rule["properties"]["specClauseNumber"]


@pytest.mark.parametrize("test_file", _fixtures("no_elements_missing"))
def test_sarif_no_elements_missing_fsct3(test_file: str) -> None:
    sarif = FSCT3Checker(test_file).output_sarif()
    run = _run(sarif)
    assert not run["results"]
    assert run["properties"]["complianceStandard"] == "fsct3"

    tax_names = [t["name"] for t in run["taxonomies"]]
    assert FSCT_TAXONOMY_NAME in tax_names
    assert FSCT_CLAUSE_TAXONOMY_NAME in tax_names

    category_tax = next(t for t in run["taxonomies"] if t["name"] == FSCT_TAXONOMY_NAME)
    cat_ids = {t["id"] for t in category_tax["taxa"]}
    assert {"sbom-meta-information", "component-attributes"} <= cat_ids

    rule_ids = {r["id"] for r in run["tool"]["driver"]["rules"]}
    # FSCT3 active rules.
    assert FSCT_COMP_CONCLUDED_LICENSE in rule_ids
    assert FSCT_COMP_COPYRIGHT_NOTICE in rule_ids
    # Catalogue-only rules also appear in the catalogue.
    assert "SBOM-FSCT3-META-004" in rule_ids  # Primary Component
    assert "SBOM-FSCT3-COMP-005" in rule_ids  # Cryptographic Hash

    # Clause taxon ids match the §2.2.x section numbers.
    clause_tax = next(
        t for t in run["taxonomies"] if t["name"] == FSCT_CLAUSE_TAXONOMY_NAME
    )
    clause_ids = {t["id"] for t in clause_tax["taxa"]}
    assert {"2.2.1.1", "2.2.2.7", "2.2.2.8"} <= clause_ids


# ---- Missing-supplier fixtures -> one result per component --------------


@pytest.mark.parametrize("test_file", _fixtures("missing_supplier_name"))
def test_sarif_missing_supplier_one_result_per_component(test_file: str) -> None:
    checker = NTIAChecker(test_file)
    expected_ids = {
        spdx_id for _name, spdx_id in checker.components_without("supplier")
    }
    assert expected_ids, "fixture must have at least one missing supplier"

    sarif = checker.output_sarif()
    run = _run(sarif)
    supplier_results = [
        r for r in run["results"] if r["ruleId"] == NTIA_DF_COMPONENT_SUPPLIER
    ]
    assert len(supplier_results) == len(expected_ids)
    emitted_ids = {
        r["locations"][0]["logicalLocations"][0]["fullyQualifiedName"]
        for r in supplier_results
    }
    assert emitted_ids == expected_ids
    # Every supplier result is error-level and references a package location.
    for r in supplier_results:
        assert r["level"] == "error"
        assert r["locations"][0]["logicalLocations"][0]["kind"] == "package"
    # Conformance derived consumer-side: results non-empty => not conformant.
    assert len(run["results"]) > 0


# ---- Missing-concluded-license fixtures (FSCT3 only) --------------------


@pytest.mark.parametrize("test_file", _fixtures("missing_concluded_license"))
def test_sarif_missing_concluded_license_fsct3(test_file: str) -> None:
    checker = FSCT3Checker(test_file)
    sarif = checker.output_sarif()
    run = _run(sarif)
    license_results = [
        r for r in run["results"] if r["ruleId"] == FSCT_COMP_CONCLUDED_LICENSE
    ]
    expected = {
        spdx_id for _, spdx_id in checker.components_without("concluded_license")
    }
    emitted = {
        r["locations"][0]["logicalLocations"][0]["fullyQualifiedName"]
        for r in license_results
    }
    assert emitted == expected


# ---- Doc-level: missing dependency relationships ------------------------


@pytest.mark.parametrize("test_file", _fixtures("missing_dependency_relationships"))
def test_sarif_missing_dependency_relationships(test_file: str) -> None:
    checker = NTIAChecker(test_file)
    if checker.document_value("dependency_relationship"):
        pytest.skip("fixture does declare dependency relationships")
    sarif = checker.output_sarif()
    run = _run(sarif)
    doc_results = [r for r in run["results"] if r["ruleId"] == NTIA_DF_DEPENDENCY]
    assert len(doc_results) == 1
    loc = doc_results[0]["locations"][0]["logicalLocations"][0]
    assert loc["name"] == "document"
    assert loc["kind"] == "module"


# ---- Catalogue-only rules never produce results -------------------------


def test_sarif_catalogue_only_rules_emit_no_results() -> None:
    """Catalogue-only rules appear in tool.driver.rules but never as findings."""
    fixture = _fixtures("no_elements_missing")[0]
    sarif = FSCT3Checker(fixture).output_sarif()
    run = _run(sarif)
    catalogue_only_ids = {
        r["id"]
        for r in run["tool"]["driver"]["rules"]
        if r["properties"]["status"] == "catalogue-only"
    }
    assert catalogue_only_ids, "fixture must produce at least one catalogue-only rule"
    emitted_rule_ids = {r["ruleId"] for r in run["results"]}
    assert emitted_rule_ids.isdisjoint(catalogue_only_ids)


# ---- Embed SBOM (--embed-sbom) ------------------------------------------


def test_sarif_embed_sbom_off_by_default() -> None:
    """Default output links the artifact by URI only; no contents embedded."""
    fixture = _fixtures("no_elements_missing")[0]
    sarif = NTIAChecker(fixture).output_sarif()
    run = _run(sarif)
    artifacts = run.get("artifacts") or []
    assert artifacts, "artifact entry should always be emitted when input file known"
    assert "contents" not in artifacts[0]
    assert "mimeType" not in artifacts[0]


def test_sarif_embed_sbom_inlines_file_contents() -> None:
    """``embed_sbom=True`` writes the source file into artifacts[0].contents."""
    fixture = next(p for p in _fixtures("no_elements_missing") if p.endswith(".json"))
    sarif = NTIAChecker(fixture).output_sarif(embed_sbom=True)
    run = _run(sarif)
    artifact = run["artifacts"][0]
    # SPDX 2 JSON has its own registered MIME type.
    assert artifact["mimeType"] == "application/spdx+json"
    contents = artifact["contents"]
    assert "text" in contents
    # Round-trip: embedded text must equal the file on disk.
    with open(fixture, encoding="utf-8") as fh:
        assert contents["text"] == fh.read()


def test_sarif_mime_type_picker() -> None:
    """Direct unit test for the MIME-type picker; covers SPDX 2 vs SPDX 3 split."""
    # pylint: disable=import-outside-toplevel
    from ntia_conformance_checker.report_sarif import _sbom_mime_type

    # SPDX 2 JSON -- registered.
    assert _sbom_mime_type("foo.spdx.json", "spdx2") == "application/spdx+json"
    # SPDX 3 JSON-LD -- application/spdx3+json not yet IANA-registered,
    # so we fall back to the registered generic JSON-LD type.
    assert _sbom_mime_type("foo.spdx.json", "spdx3") == "application/ld+json"
    # Compound .rdf.xml must be detected as RDF/XML, not bare XML.
    assert _sbom_mime_type("foo.spdx.rdf.xml") == "application/rdf+xml"
    # SPDX 2 XML is *not* RDF -- generic application/xml.
    assert _sbom_mime_type("foo.spdx.xml") == "application/xml"
    # Tag-value -- plain text is the closest registered type.
    assert _sbom_mime_type("foo.spdx") == "text/plain"
    # YAML -- generic registered type (no SPDX-specific MIME).
    assert _sbom_mime_type("foo.spdx.yaml") == "application/yaml"
    assert _sbom_mime_type("foo.spdx.yml") == "application/yaml"
    # Unknown -> octet-stream.
    assert _sbom_mime_type("foo.weird") == "application/octet-stream"


# ---- Round-trip: result is JSON-serialisable ----------------------------


def test_sarif_round_trip_json_serializable() -> None:
    fixture = _fixtures("no_elements_missing")[0]
    sarif = sbom_checker.SbomChecker(fixture).output_sarif()
    # Round-trip through json to catch any non-serialisable types.
    s = json.dumps(sarif)
    parsed = json.loads(s)
    assert parsed["version"] == "2.1.0"
