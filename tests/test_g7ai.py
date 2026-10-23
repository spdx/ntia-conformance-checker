# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for G7 SBOM for AI support: outcomes, kinds, roll-ups, ontology ids."""

# pylint: disable=missing-function-docstring,protected-access

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Callable

import pytest
from pytest import CaptureFixture, MonkeyPatch

from ntia_conformance_checker import probes
from ntia_conformance_checker.main import main
from ntia_conformance_checker.registry import get_spec
from ntia_conformance_checker.rule_based_checker import RuleBasedChecker

DATA = Path(__file__).parent / "data"
G7 = DATA / "spdx3" / "g7ai" / "conformant.json"
SPDX2 = str(DATA / "no_elements_missing" / "SPDXJSONExample-v2.3.spdx.json")
B = "https://spdx.org/spdxdocs/g7ai-tests/"
P = "BOM-G7AI2026-"


def _check(
    tmp_path: Path, edit: Callable[[list[dict[str, Any]]], None]
) -> RuleBasedChecker:
    """Check a copy of the conformant G7 SBOM after ``edit`` changes its graph."""
    doc = json.loads(G7.read_text(encoding="utf-8"))
    graph = copy.deepcopy(doc["@graph"])
    edit(graph)
    doc["@graph"] = graph
    path = tmp_path / "g7.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    return RuleBasedChecker(str(path), compliance="g7ai", sbom_spec="spdx3")


def _el(graph: list[dict[str, Any]], name: str) -> dict[str, Any]:
    return next(e for e in graph if e.get("spdxId") == B + name)


def _drop(name: str, *props: str) -> Callable[[list[dict[str, Any]]], None]:
    def edit(graph: list[dict[str, Any]]) -> None:
        for prop in props:
            _el(graph, name).pop(prop)

    return edit


def _outcomes(checker: RuleBasedChecker) -> dict[str, str]:
    return {k: v.outcome for k, v in checker.rule_results().items()}


def test_conformant_sbom_passes(tmp_path: Path) -> None:
    checker = _check(tmp_path, lambda g: None)
    assert checker.check_compliance() is True
    got = _outcomes(checker)
    assert got[P + "MDL-006.3"] == "missing"  # a recommendation: reported, not blocking
    assert {v for k, v in got.items() if k != P + "MDL-006.3"} == {
        "present",
        "out-of-scope",
    }
    assert got[P + "MDL-006"] == "present"  # roll-up of its present sub-elements


# edit -> (rule, outcome, verdict)
_CASES = {
    "model hash": (_drop("Model1", "verifiedUsing"), "MDL-007", "missing", False),
    "dataset hash": (_drop("Dataset1", "verifiedUsing"), "DP-005", "missing", False),
    "system version": (
        _drop("System1", "software_packageVersion"),
        "SLP-004",
        "missing",
        False,
    ),
    # any-of: one present sub-element is enough
    "one model property": (
        _drop("Model1", "ai_hyperparameter"),
        "MDL-009",
        "present",
        True,
    ),
    "all model properties": (
        _drop("Model1", "ai_hyperparameter", "ai_typeOfModel"),
        "MDL-009",
        "missing",
        False,
    ),
}


@pytest.mark.parametrize("name", _CASES)
def test_missing_information_is_reported(tmp_path: Path, name: str) -> None:
    edit, rule, outcome, verdict = _CASES[name]
    checker = _check(tmp_path, edit)
    assert _outcomes(checker)[P + rule] == outcome
    assert checker.check_compliance() is verdict


def test_tool_name_comes_from_the_creation_info(tmp_path: Path) -> None:
    def edit(graph: list[dict[str, Any]]) -> None:
        graph[0].pop("createdUsing")

    assert _outcomes(_check(tmp_path, edit))[P + "MD-006"] == "missing"


def test_rules_for_an_absent_kind_do_not_apply(tmp_path: Path) -> None:
    def edit(graph: list[dict[str, Any]]) -> None:
        gone = {B + "Dataset1"}
        graph[:] = [
            e
            for e in graph
            if e.get("spdxId") not in gone
            and e.get("from") not in gone
            and set(e.get("to", [])) != gone  # a link only to the dataset
        ]
        _el(graph, "Rel-contains-model")["to"] = [B + "Model1"]

    checker = _check(tmp_path, edit)
    got = _outcomes(checker)
    assert got[P + "DP-001"] == got[P + "DP-002"] == "not-applicable"  # roll-up too
    assert got[P + "MDL-001"] == "present"  # the model still applies
    assert checker.check_compliance() is True
    assert checker.output_json()["clusterCompliance"]["dataset-properties"] is None


def test_core_bom_root_expands_like_an_sbom(tmp_path: Path) -> None:
    def edit(graph: list[dict[str, Any]]) -> None:
        _el(graph, "SBOM1")["type"] = "Bom"
        _el(graph, "SBOM1").pop("software_sbomType")

    checker = _check(tmp_path, edit)
    assert _outcomes(checker)[P + "SLP-001"] == "present"


def test_an_ai_package_with_another_purpose_is_not_a_model(tmp_path: Path) -> None:
    # System1 is an AI package (purpose: application): the system, not a model.
    checker = _check(tmp_path, lambda g: None)
    names = [
        n
        for n, _ in checker.components_without_property(
            "ai_model", ("ai_standardCompliance",)
        )
    ]
    assert names == ["Test AI Model"]


def test_other_sbom_specification_means_nothing_applies(
    capsys: CaptureFixture[str],
) -> None:
    checker = RuleBasedChecker(SPDX2, compliance="g7ai", sbom_spec="spdx2")
    assert set(_outcomes(checker).values()) <= {"not-applicable", "out-of-scope"}
    assert checker.check_compliance() is False  # nothing was checked
    checker.print_table_output()
    assert "No requirement of" in capsys.readouterr().out


def test_unparsable_file_fails_every_applicable_rule() -> None:
    checker = RuleBasedChecker(
        "no/such/file.json", compliance="g7ai", sbom_spec="spdx3"
    )
    got = _outcomes(checker)
    assert got[P + "MDL-001"] == got[P + "DP-001"] == got[P + "SLP-001"] == "missing"
    assert "not-applicable" not in got.values()
    assert checker.check_compliance() is False


def _set(element: str, **fields: Any) -> Callable[[list[dict[str, Any]]], None]:
    def edit(graph: list[dict[str, Any]]) -> None:
        _el(graph, element).update(fields)

    return edit


def _unreach_model(graph: list[dict[str, Any]]) -> None:
    graph[:] = [e for e in graph if e.get("spdxId") != B + "Rel-system-dependsOn"]
    _el(graph, "Rel-contains-model")["from"] = B + "Model1"  # dangling subgraph


def _no_root(graph: list[dict[str, Any]]) -> None:
    _el(graph, "SBOM1")["rootElement"] = []


# edit -> rule that must fail (the verdict must be False too)
_FALSE_PASSES = {
    "no system root": (_no_root, "SLP-001"),
    "unreachable model": (_unreach_model, "MDL-001"),
    "NOASSERTION license": (
        _set("Rel-model-license", to=["NOASSERTION"]),
        "MDL-012",
    ),
    "NOASSERTION originator": (
        _set("Model1", originatedBy=["NOASSERTION"]),
        "MDL-005",
    ),
    "blank list item": (_set("System1", ai_standardCompliance=["  "]), "SP-002"),
    "noAssertion presence": (
        _set(
            "System1",
            ai_useSensitivePersonalInformation=(
                "https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/noAssertion"
            ),
        ),
        "SLP-007",
    ),
    "hash without value": (
        _set(
            "Model1",
            verifiedUsing=[{"type": "Hash", "algorithm": "sha256"}],
        ),
        "MDL-007",
    ),
    "dangling originator": (_set("Model1", originatedBy=[B + "nobody"]), "MDL-005"),
    "blank tool name": (_set("Tool1", name=" "), "MD-006"),
    "email-only identifier": (
        _set(
            "Model1",
            software_packageUrl=None,
            externalIdentifier=[
                {
                    "type": "ExternalIdentifier",
                    "externalIdentifierType": "email",
                    "identifier": "a@b.c",
                }
            ],
        ),
        "MDL-002",
    ),
}


@pytest.mark.parametrize("name", _FALSE_PASSES)
def test_no_false_pass(tmp_path: Path, name: str) -> None:
    edit, rule = _FALSE_PASSES[name]

    def drop_none(graph: list[dict[str, Any]]) -> None:
        edit(graph)
        for el in graph:
            for key in [k for k, v in el.items() if v is None]:
                del el[key]

    checker = _check(tmp_path, drop_none)
    assert _outcomes(checker)[P + rule] == "missing"
    assert checker.check_compliance() is False


def test_dataset_linked_only_by_training_is_reachable(tmp_path: Path) -> None:
    checker = _check(
        tmp_path, _set("Rel-contains-model", to=[B + "Model1"])  # not the dataset
    )
    assert _outcomes(checker)[P + "DP-001"] == "present"  # via Model1 trainedOn
    assert checker.check_compliance() is True


@pytest.mark.parametrize("keep", ["empty", "no document"])
def test_odd_graphs_do_not_crash(tmp_path: Path, keep: str) -> None:
    def edit(graph: list[dict[str, Any]]) -> None:
        graph[:] = (
            [] if keep == "empty" else [e for e in graph if e["type"] != "SpdxDocument"]
        )

    checker = _check(tmp_path, edit)
    assert checker.check_compliance() is False


def test_license_outside_the_document_counts(tmp_path: Path) -> None:
    checker = _check(
        tmp_path,
        _set("Rel-model-license", to=["https://spdx.org/licenses/MIT"]),
    )
    assert _outcomes(checker)[P + "MDL-012"] == "present"
    assert checker.check_compliance() is True


def test_base_model_in_lineage_is_not_a_checked_model(tmp_path: Path) -> None:
    def edit(graph: list[dict[str, Any]]) -> None:
        graph.append(
            {
                "type": "ai_AIPackage",
                "spdxId": B + "Base",
                "creationInfo": "_:g7ai-creationinfo",
                "name": "Base model",
                "software_primaryPurpose": "model",
            }
        )
        graph.append(
            {
                "type": "Relationship",
                "spdxId": B + "Rel-lineage",
                "creationInfo": "_:g7ai-creationinfo",
                "relationshipType": "descendantOf",
                "from": B + "Model1",
                "to": [B + "Base"],
            }
        )

    assert _check(tmp_path, edit).check_compliance() is True


def test_single_valued_reference_property(tmp_path: Path) -> None:
    checker = _check(tmp_path, lambda g: None)
    assert not checker.components_without_property("ai_model", ("suppliedBy",))


def test_cluster_compliance_follows_validity(tmp_path: Path) -> None:
    checker = _check(tmp_path, lambda g: None)
    assert set(checker.output_json()["clusterCompliance"].values()) == {True, None}
    bad = RuleBasedChecker("no/such/file.json", compliance="g7ai", sbom_spec="spdx3")
    assert True not in bad.output_json()["clusterCompliance"].values()


def test_any_of_is_decided_per_model(tmp_path: Path) -> None:
    def edit(graph: list[dict[str, Any]]) -> None:
        model = copy.deepcopy(_el(graph, "Model1"))
        model["spdxId"] = B + "Model2"
        model["name"] = "Second model"
        for prop in ("ai_hyperparameter", "ai_typeOfModel"):
            model.pop(prop)
        graph.append(model)
        _el(graph, "Rel-contains-model")["to"].append(B + "Model2")

    checker = _check(tmp_path, edit)
    assert _outcomes(checker)[P + "MDL-009"] == "missing"  # Model2 has neither
    assert checker.check_compliance() is False


def test_findings_name_the_failing_components(tmp_path: Path) -> None:
    checker = _check(tmp_path, _drop("Model1", "verifiedUsing"))
    entry = next(
        r for r in checker.output_json()["ruleResults"] if r["id"] == P + "MDL-007"
    )
    assert [f["name"] for f in entry["findings"]] == ["Test AI Model"]


def test_unknown_property_and_kind_fail_loudly(tmp_path: Path) -> None:
    checker = _check(tmp_path, lambda g: None)
    with pytest.raises(ValueError, match="Unknown SPDX 3 property"):
        checker.components_without_property("ai_model", ("ai_typeOfModle",))
    with pytest.raises(ValueError, match="Unknown component kind"):
        checker.has_components("modle")


def test_cli_runs_g7ai(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    monkeypatch.setattr(sys, "argv", ["sbomcheck", "-c", "g7ai", "-r", "json", str(G7)])
    with pytest.raises(SystemExit) as exc:
        main()
    out = json.loads(capsys.readouterr().out)
    assert (exc.value.code, out["isConformant"], out["complianceStandard"]) == (
        0,
        True,
        "g7ai",
    )
    assert out["ruleResults"][0] == {
        "id": P + "MD-001",
        "category": "metadata",
        "outcome": "present",
        "provision": "requirement",
        "findings": [],
    }


# ---- ontology as the source of truth for rule ids -------------------------

_ONTOLOGY = json.loads((DATA / "ontology_rules.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("spec_id", ["ntia", "fsct3", "g7ai"])
def test_rules_match_the_ontology_snapshot(spec_id: str) -> None:
    spec = get_spec(spec_id)
    mine = {spec.rule_id(r): (r.provision, r.aggregation) for r in spec.rules}
    onto = {
        k: (v["provision"], v["aggregation"]) for k, v in _ONTOLOGY[spec_id].items()
    }
    assert mine == onto


# probe -> params that must be rejected when the spec is loaded
_BAD_PARAMS: dict[str, tuple[str, dict[str, Any]]] = {
    "empty properties": ("require_property", {"kind": "ai_model", "properties": []}),
    "string properties": (
        "require_property",
        {"kind": "ai_model", "properties": "name"},
    ),
    "unknown property": (
        "require_property",
        {"kind": "dataset", "properties": ["ai_typeOfModle"]},
    ),
    "unknown kind": ("require_property", {"kind": "modle", "properties": ["name"]}),
    "unknown relationship": (
        "require_relationship",
        {"kind": "system", "relationships": ["dependOn"]},
    ),
    "bad direction": (
        "require_relationship",
        {"kind": "system", "relationships": ["contains"], "direction": "up"},
    ),
    "unknown document property": (
        "require_document_property",
        {"properties": ["createdUsin"]},
    ),
}


@pytest.mark.parametrize("name", _BAD_PARAMS)
def test_probe_params_are_validated_at_load(name: str) -> None:
    probe_name, params = _BAD_PARAMS[name]
    check = probes.validator(probe_name)
    assert check is not None
    with pytest.raises(ValueError):
        check(params)
