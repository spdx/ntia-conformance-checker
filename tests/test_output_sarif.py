# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for SARIF output: base log, rule catalogue, results, ontology ids."""

# pylint: disable=missing-function-docstring,protected-access

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pytest
from pytest import CaptureFixture, MonkeyPatch

from ntia_conformance_checker import BSIChecker
from ntia_conformance_checker.main import main
from ntia_conformance_checker.rule_based_checker import RuleBasedChecker
from ntia_conformance_checker.spec import (
    ProbeRef,
    Spec,
    SpecCategory,
    SpecMaturity,
    SpecRule,
)

DATA = Path(__file__).parent / "data"
G7 = DATA / "spdx3" / "g7ai" / "conformant.json"
NTIA_OK = str(DATA / "no_elements_missing" / "SPDXJSONExample-v2.3.spdx.json")
NTIA_NO_SUPPLIER = str(
    DATA / "missing_supplier_name" / "SPDXJSONExample-v2.3.spdx.json"
)
BSI_FILE = next((DATA / "bsi").glob("*.json"))
G7P = "BOM-G7AI2026-"


def _run(checker: Any, **kwargs: Any) -> dict[str, Any]:
    log = checker.output_sarif(**kwargs)
    json.dumps(log)  # serializable
    assert log["version"] == "2.1.0"
    assert len(log["runs"]) == 1
    run: dict[str, Any] = log["runs"][0]
    return run


def _ntia(path: str) -> RuleBasedChecker:
    return RuleBasedChecker(path, compliance="ntia")


def _g7(tmp_path: Path, edit: Any = None) -> RuleBasedChecker:
    doc = json.loads(G7.read_text(encoding="utf-8"))
    if edit:
        edit(doc["@graph"])
    path = tmp_path / "g7.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    return RuleBasedChecker(str(path), compliance="g7ai", sbom_spec="spdx3")


def _drop(name: str, *props: str) -> Any:
    def edit(graph: list[dict[str, Any]]) -> None:
        for el in graph:
            if el.get("spdxId", "").endswith("/" + name):
                for prop in props:
                    el.pop(prop, None)

    return edit


def test_conformant_sbom_has_catalogue_and_no_results() -> None:
    run = _run(_ntia(NTIA_OK))
    assert not run["results"]
    assert [r["id"] for r in run["tool"]["driver"]["rules"]] == sorted(
        f"BOM-NTIA2021-DF-{n:03d}" for n in range(1, 8)
    )
    assert run["properties"]["conformant"] is True
    assert run["properties"]["complianceStandard"] == "ntia"
    assert run["invocations"][0]["executionSuccessful"] is True


def test_missing_element_gives_one_result_per_component() -> None:
    run = _run(_ntia(NTIA_NO_SUPPLIER))
    assert run["properties"]["conformant"] is False
    assert {r["ruleId"] for r in run["results"]} == {"BOM-NTIA2021-DF-001"}
    for result in run["results"]:
        assert result["level"] == "error"
        assert result["locations"][0]["logicalLocations"][0]["kind"] == "package"


def test_sarif_is_self_consistent(tmp_path: Path) -> None:
    run = _run(_g7(tmp_path, _drop("Model1", "verifiedUsing")))
    rule_ids = {r["id"] for r in run["tool"]["driver"]["rules"]}
    taxa = {(t["name"], x["id"]) for t in run["taxonomies"] for x in t["taxa"]}
    assert {r["ruleId"] for r in run["results"]} <= rule_ids
    for rule in run["tool"]["driver"]["rules"]:
        for rel in rule["relationships"]:
            target = rel["target"]
            if "toolComponent" in target:
                assert (target["toolComponent"]["name"], target["id"]) in taxa
            else:
                assert target["id"] in rule_ids


def test_g7ai_failure_uses_ontology_ids(tmp_path: Path) -> None:
    run = _run(_g7(tmp_path, _drop("Model1", "verifiedUsing")))
    assert {r["ruleId"] for r in run["results"]} == {G7P + "MDL-007", G7P + "MDL-008"}
    assert run["properties"]["complianceStandard"] == "g7ai"
    assert [t["name"] for t in run["taxonomies"]] == ["g7ai-sbom-for-ai"]


def test_rollup_reports_once_and_not_its_sub_rules(tmp_path: Path) -> None:
    edit = _drop("Model1", "ai_hyperparameter", "ai_typeOfModel")
    run = _run(_g7(tmp_path, edit))
    assert {r["ruleId"] for r in run["results"]} == {G7P + "MDL-009"}
    rules = {r["id"]: r for r in run["tool"]["driver"]["rules"]}
    assert rules[G7P + "MDL-009"]["properties"]["aggregation"] == "any-of"
    sub = rules[G7P + "MDL-009.1"]["relationships"][-1]
    assert (sub["target"]["id"], sub["kinds"]) == (G7P + "MDL-009", ["subset"])


def test_not_applicable_rules_give_no_results(tmp_path: Path) -> None:
    def edit(graph: list[dict[str, Any]]) -> None:
        graph[:] = [e for e in graph if e.get("type") != "dataset_DatasetPackage"]
        for el in graph:
            if el.get("type") == "Relationship":
                el["to"] = [t for t in el["to"] if not t.endswith("Dataset1")]
        graph[:] = [e for e in graph if e.get("type") != "Relationship" or e["to"]]

    run = _run(_g7(tmp_path, edit))
    assert not [r for r in run["results"] if "-DP-" in r["ruleId"]]


def test_unparsable_file_reports_the_error() -> None:
    run = _run(RuleBasedChecker("no/such/file.json", compliance="ntia"))
    assert run["invocations"][0]["executionSuccessful"] is False
    assert run["invocations"][0]["toolExecutionNotifications"][0]["level"] == "error"
    assert run["properties"]["conformant"] is False


def test_checker_without_rule_outcomes_gets_the_base_log() -> None:
    run = _run(BSIChecker(str(BSI_FILE)))
    assert not run["results"]
    assert "rules" not in run["tool"]["driver"]
    assert run["properties"]["ruleResults"] is False
    assert run["properties"]["complianceStandard"] == "bsi"


def test_embedding_the_sbom() -> None:
    artifact = _run(_ntia(NTIA_OK), embed_sbom=True)["artifacts"][0]
    assert artifact["mimeType"] == "application/spdx+json"
    assert "SPDXRef-DOCUMENT" in artifact["contents"]["text"]
    assert "contents" not in _run(_ntia(NTIA_OK))["artifacts"][0]


def test_unknown_maturity_is_an_error() -> None:
    with pytest.raises(ValueError, match="maturity"):
        _ntia(NTIA_OK).output_sarif(maturity=5)


def test_cli_writes_sarif(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str], tmp_path: Path
) -> None:
    out = tmp_path / "out.sarif"
    argv = ["sbomcheck", "-c", "g7ai", "-r", "sarif", "-o", str(out), str(G7)]
    monkeypatch.setattr(sys, "argv", argv)
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 0
    assert json.loads(out.read_text(encoding="utf-8"))["version"] == "2.1.0"
    assert capsys.readouterr().out == ""


def test_document_level_finding_has_a_document_location() -> None:
    path = str(DATA / "missing_author_name" / "SPDXJSONExample-v2.3.spdx.json")
    run = _run(_ntia(path))
    result = next(r for r in run["results"] if r["ruleId"] == "BOM-NTIA2021-DF-006")
    assert result["locations"][0]["logicalLocations"][0]["name"] == "document"


def test_clause_shared_by_rules_is_a_superset_not_equal() -> None:
    rules = _run(_ntia(NTIA_OK))["tool"]["driver"]["rules"]
    kinds = {
        rel["kinds"][0]
        for rule in rules
        for rel in rule["relationships"]
        if rel["target"].get("toolComponent", {}).get("name") == "ntia-clauses"
    }
    assert kinds == {"superset"}


def test_file_name_is_a_valid_uri_reference(tmp_path: Path) -> None:
    path = tmp_path / "my sbom#1%.json"
    path.write_text(G7.read_text(encoding="utf-8"), encoding="utf-8")
    checker = RuleBasedChecker(str(path), compliance="g7ai", sbom_spec="spdx3")
    uri = _run(checker)["artifacts"][0]["location"]["uri"]
    assert uri == "my%20sbom%231%25.json"


def test_unparsable_file_results_say_so() -> None:
    run = _run(RuleBasedChecker("no/such/file.json", compliance="ntia"))
    assert {r["message"]["text"] for r in run["results"]} == {
        "The SBOM could not be parsed."
    }


def test_rule_outcomes_and_nothing_applies_note() -> None:
    spdx2 = RuleBasedChecker(NTIA_OK, compliance="g7ai", sbom_spec="spdx2")
    run = _run(spdx2)
    outcomes = set(run["properties"]["ruleOutcomes"].values())
    assert outcomes <= {"not-applicable", "out-of-scope"}
    notes = run["invocations"][0]["toolExecutionNotifications"]
    assert [n["descriptor"]["id"] for n in notes] == ["sbom.nothing-applies"]
    assert run["properties"]["conformant"] is False


def test_artifact_index_only_when_the_run_lists_the_artifact() -> None:
    checker = _ntia(NTIA_NO_SUPPLIER)
    loc = _run(checker)["results"][0]["locations"][0]["physicalLocation"]
    assert loc["artifactLocation"]["index"] == 0
    checker.file = ""  # API use without a file
    run = _run(checker)
    assert "artifacts" not in run
    assert (
        "index"
        not in run["results"][0]["locations"][0]["physicalLocation"]["artifactLocation"]
    )


def test_unchecked_sub_rule_is_only_relevant_to_its_parent(tmp_path: Path) -> None:
    rules = _run(_g7(tmp_path))["tool"]["driver"]["rules"]
    unchecked = [
        r for r in rules if "." in r["id"] and r["properties"]["status"] != "active"
    ]
    assert unchecked
    assert all(r["relationships"][-1]["kinds"] == ["relevant"] for r in unchecked)


def _supplier_rule(number: int, **kwargs: Any) -> SpecRule:
    return SpecRule(
        number=number,
        slug=f"adhoc-supplier-{number}-missing",
        spec_category="c",
        element_id="supplier",
        competency_question="Supplier provided?",
        probe=ProbeRef(
            name="require_component_attribute", params={"attribute": "supplier"}
        ),
        **kwargs,
    )


def test_maturity_scopes_results_but_not_the_catalogue() -> None:
    spec = Spec(
        id="adhoc",
        title="Ad Hoc",
        categories=(SpecCategory(id="c", code="C", title="C"),),
        maturity_levels=(
            SpecMaturity(level=0, id="base"),
            SpecMaturity(level=1, id="deep"),
        ),
        rules=(
            _supplier_rule(1, maturity=1),
            _supplier_rule(2, maturity=1, provision="recommendation"),
        ),
    )
    checker = RuleBasedChecker(NTIA_NO_SUPPLIER, compliance=spec)
    base, deep = _run(checker), _run(checker, maturity=1)
    assert not base["results"]
    assert len(base["tool"]["driver"]["rules"]) == 2  # the catalogue is not scoped
    assert base["properties"]["maturityTarget"] == 0
    levels = {r["ruleId"]: r["level"] for r in deep["results"]}
    assert levels == {"SBOM-ADHOC-C-001": "error", "SBOM-ADHOC-C-002": "warning"}
    assert deep["properties"]["conformant"] is False
