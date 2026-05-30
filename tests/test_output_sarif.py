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


# ---- Conformant fixtures -> zero results ----------


@pytest.mark.parametrize("test_file", _fixtures("no_elements_missing"))
def test_sarif_no_elements_missing_ntia(test_file: str) -> None:
    sarif = sbom_checker.SbomChecker(test_file, compliance="ntia").output_sarif()
    run = _run(sarif)
    assert not run["results"]
    assert run["invocations"][0]["executionSuccessful"] is True
    assert run["properties"]["complianceStandard"] == "ntia"
    assert run["tool"]["driver"]["name"] == "ntia-conformance-checker"
    # All NTIA rules present in catalogue regardless of findings.
    rule_ids = {r["id"] for r in run["tool"]["driver"]["rules"]}
    assert {
        "ntia.component.name",
        "ntia.component.version",
        "ntia.component.identifier",
        "ntia.component.supplier",
        "ntia.document.author",
        "ntia.document.timestamp",
        "ntia.document.dependency-relationships",
    } <= rule_ids
    # Taxonomy emitted with single taxon.
    assert run["taxonomies"][0]["name"] == "2021-ntia-sbom-minimum-elements"
    taxa = run["taxonomies"][0]["taxa"]
    assert len(taxa) == 1 and taxa[0]["id"] == "minimum-elements"
    # Every rule references the taxon.
    for rule in run["tool"]["driver"]["rules"]:
        rel = rule["relationships"][0]["target"]
        assert rel["id"] == "minimum-elements"
        assert rel["toolComponent"]["name"] == "2021-ntia-sbom-minimum-elements"


@pytest.mark.parametrize("test_file", _fixtures("no_elements_missing"))
def test_sarif_no_elements_missing_fsct3(test_file: str) -> None:
    sarif = FSCT3Checker(test_file).output_sarif()
    run = _run(sarif)
    assert not run["results"]
    assert run["properties"]["complianceStandard"] == "fsct3-min"
    assert (
        run["taxonomies"][0]["name"] == "2024-cisa-baseline-attributes-minimum-expected"
    )
    # Two taxa: one per FSCT3 section.
    taxa_ids = {t["id"] for t in run["taxonomies"][0]["taxa"]}
    assert taxa_ids == {"sbom-meta-information", "component-attributes"}
    rule_ids = {r["id"] for r in run["tool"]["driver"]["rules"]}
    # FSCT3 catalogue extends NTIA with concluded-license and copyright-text.
    assert "fsct3.component.concluded-license" in rule_ids
    assert "fsct3.component.copyright-text" in rule_ids


# ---- Missing-supplier fixtures -> one result per component --------


@pytest.mark.parametrize("test_file", _fixtures("missing_supplier_name"))
def test_sarif_missing_supplier_one_result_per_component(test_file: str) -> None:
    checker = NTIAChecker(test_file)
    expected_ids = {spdx_id for _name, spdx_id in checker.components_without_suppliers}
    assert expected_ids, "fixture must have at least one missing supplier"

    sarif = checker.output_sarif()
    run = _run(sarif)
    supplier_results = [
        r for r in run["results"] if r["ruleId"] == "ntia.component.supplier"
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


# ---- Missing-concluded-license fixtures (FSCT3 only) ----------


@pytest.mark.parametrize("test_file", _fixtures("missing_concluded_license"))
def test_sarif_missing_concluded_license_fsct3(test_file: str) -> None:
    checker = FSCT3Checker(test_file)
    sarif = checker.output_sarif()
    run = _run(sarif)
    license_results = [
        r for r in run["results"] if r["ruleId"] == "fsct3.component.concluded-license"
    ]
    expected = {spdx_id for _, spdx_id in checker.components_without_concluded_licenses}
    emitted = {
        r["locations"][0]["logicalLocations"][0]["fullyQualifiedName"]
        for r in license_results
    }
    assert emitted == expected


# ---- Doc-level: missing dependency relationships --------------


@pytest.mark.parametrize("test_file", _fixtures("missing_dependency_relationships"))
def test_sarif_missing_dependency_relationships(test_file: str) -> None:
    checker = NTIAChecker(test_file)
    if checker.dependency_relationships:
        pytest.skip("fixture does declare dependency relationships")
    sarif = checker.output_sarif()
    run = _run(sarif)
    doc_results = [
        r
        for r in run["results"]
        if r["ruleId"] == "ntia.document.dependency-relationships"
    ]
    assert len(doc_results) == 1
    loc = doc_results[0]["locations"][0]["logicalLocations"][0]
    assert loc["name"] == "document"
    assert loc["kind"] == "module"


# ---- Round-trip: result is JSON-serialisable --------------


def test_sarif_round_trip_json_serializable() -> None:
    fixture = _fixtures("no_elements_missing")[0]
    sarif = sbom_checker.SbomChecker(fixture).output_sarif()
    # Round-trip through json to catch any non-serialisable types.
    s = json.dumps(sarif)
    parsed = json.loads(s)
    assert parsed["version"] == "2.1.0"
