# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for the declarative-rules model: rule ids, maturity target
scoping, provision -> severity, blocking compliance, and loader validation."""

# pylint: disable=missing-function-docstring,protected-access

from __future__ import annotations

import copy
import dataclasses
import json
import pickle
from pathlib import Path

import pytest
import yaml

from ntia_conformance_checker import registry
from ntia_conformance_checker.probes import _registry as probe_registry
from ntia_conformance_checker.registry import get_spec, spec_ids
from ntia_conformance_checker.spec import (
    Spec,
    SpecCategory,
    SpecMaturity,
    SpecRule,
)
from ntia_conformance_checker.spec_loader import (
    SpecLoadError,
    _UniqueKeyLoader,
    load_spec,
)

_ONTOLOGY = Path(__file__).parent / "data" / "ontology_rules.json"
_RULES_DIR = Path(registry.__file__).parent / "rules"


def _demo_spec() -> Spec:
    return Spec(
        id="demo",
        title="Demo",
        categories=(SpecCategory(id="c", code="C", title="C"),),
        maturity_levels=(
            SpecMaturity(level=0, id="base"),
            SpecMaturity(level=1, id="deep"),
        ),
        rules=(
            SpecRule(
                number=1,
                slug="demo-a",
                spec_category="c",
                maturity=0,
                provision="requirement",
            ),
            SpecRule(
                number=2,
                slug="demo-b",
                spec_category="c",
                maturity=1,
                provision="requirement",
            ),
            SpecRule(
                number=3,
                slug="demo-c",
                spec_category="c",
                maturity=0,
                provision="recommendation",
            ),
            SpecRule(
                number=4,
                slug="demo-d",
                spec_category="c",
                maturity=0,
                provision="permission",
            ),
            SpecRule(
                number=5,
                slug="demo-e",
                spec_category="c",
                status="catalogue-only",
            ),
        ),
    )


def _ids(spec: Spec, rules: tuple[SpecRule, ...]) -> set[str]:
    return {spec.rule_id(r) for r in rules}


# ---- rule id ------------------------------------------------------------


def test_rule_id_derivation() -> None:
    s = _demo_spec()
    assert s.rule_id(s.rules[0]) == "SBOM-DEMO-C-001"
    assert s.rule_id(s.rules[1]) == "SBOM-DEMO-C-002"


# ---- maturity target scoping --------------------------------------------


def test_active_rules_scoped_by_target() -> None:
    s = _demo_spec()
    # target 0: maturity-0 active rules only (1, 3, 4); excludes mat-1 (2) and
    # catalogue-only (5).
    assert _ids(s, s.active_rules(0)) == {
        "SBOM-DEMO-C-001",
        "SBOM-DEMO-C-003",
        "SBOM-DEMO-C-004",
    }
    # target 1: rule 2 comes into scope.
    assert _ids(s, s.active_rules(1)) == {
        "SBOM-DEMO-C-001",
        "SBOM-DEMO-C-002",
        "SBOM-DEMO-C-003",
        "SBOM-DEMO-C-004",
    }
    # None: no maturity filter (all active rules).
    assert _ids(s, s.active_rules()) == _ids(s, s.active_rules(1))


def test_blocking_rules_requirement_and_in_scope_only() -> None:
    s = _demo_spec()
    # target 0: only requirement + maturity<=0 -> rule 1 (3 recommendation,
    # 4 permission, 2 out of scope).
    assert _ids(s, s.blocking_rules(0)) == {"SBOM-DEMO-C-001"}
    assert _ids(s, s.blocking_rules(1)) == {"SBOM-DEMO-C-001", "SBOM-DEMO-C-002"}


def test_emitted_rules_not_maturity_filtered() -> None:
    s = _demo_spec()
    # Catalogue = every non-TBD rule regardless of tier (all 5 here).
    assert len(s.emitted_rules()) == 5


def test_max_maturity_and_ordinals() -> None:
    s = _demo_spec()
    assert s.max_maturity == 1
    assert s.maturity_ordinals() == (0, 1)


# ---- provision -> severity ----------------------------------------------


def test_provision_severity_mapping() -> None:
    s = _demo_spec()
    sev = {s.rule_id(r): s.severity(r) for r in s.rules}
    assert sev["SBOM-DEMO-C-001"] == "error"  # requirement (default)
    assert sev["SBOM-DEMO-C-003"] == "warning"  # recommendation
    assert sev["SBOM-DEMO-C-004"] == "none"  # permission


def test_default_provision_is_requirement() -> None:
    assert SpecRule(number=1, slug="x", spec_category="c").provision == "requirement"


def test_maturity_id_resolution() -> None:
    s = _demo_spec()
    assert s.maturity_id(s.rules[0]) == "base"  # level 0
    assert s.maturity_id(s.rules[1]) == "deep"  # level 1


# ---- real shipped specs -------------------------------------------------


def test_ntia_is_flat_with_default_required_level() -> None:
    n = get_spec("ntia")
    assert [(m.level, m.id) for m in n.maturity_levels] == [(0, "required")]
    assert n.severity(n.rules[0]) == "error"
    assert all(r.maturity == 0 for r in n.rules)


def test_fsct3_declares_three_levels() -> None:
    f = get_spec("fsct3")
    assert f.maturity_ordinals() == (0, 1, 2)


def test_report_name_derived_from_slug() -> None:
    s = _demo_spec()
    # PascalCase of the kebab slug; no whitespace (SARIF reportingDescriptor.name).
    assert s.report_name(s.rules[0]) == "DemoA"  # slug "demo-a"
    ntia = get_spec("ntia")
    for rule in ntia.rules:
        rn = ntia.report_name(rule)
        assert " " not in rn
        assert rn == "".join(seg.capitalize() for seg in rule.slug.split("-"))


def test_shipped_specs_taxonomy_names() -> None:
    n = get_spec("ntia")
    assert (n.taxonomies.category, n.taxonomies.clause) == (
        "ntia-minimum-elements",
        "ntia-clauses",
    )
    f = get_spec("fsct3")
    assert (f.taxonomies.category, f.taxonomies.clause) == (
        "fsct3-baseline-attributes",
        "fsct3-clauses",
    )


# ---- loader validation --------------------------------------------------


_GOOD = """\
spec:
  id: demo
  title: Demo
categories:
  - id: c
    code: C
    title: C
rules:
  - number: 1
    slug: demo-a
    spec_category: c
    probe: { name: require_document_attribute, params: { attribute: author } }
"""


def _write(tmp_path: Path, text: str) -> Path:
    p = tmp_path / "demo.yaml"
    p.write_text(text, encoding="utf-8")
    return p


def test_loader_flat_spec_gets_default_level(tmp_path: Path) -> None:
    s = load_spec(_write(tmp_path, _GOOD))
    assert [(m.level, m.id) for m in s.maturity_levels] == [(0, "required")]
    assert s.rule_id(s.rules[0]) == "SBOM-DEMO-C-001"


def test_element_concept_uris_defaults_empty_and_round_trips(tmp_path: Path) -> None:
    # Reserved semantic-mapping slot: empty by default, opaque when set.
    assert load_spec(_write(tmp_path, _GOOD)).rules[0].element_concept_uris == ()
    uris = [
        "https://example.org/vocab#doc-author",
        "https://example.org/other-vocab#author",
    ]
    with_uris = _GOOD.replace(
        "spec_category: c",
        f"spec_category: c\n    element_concept_uris: {uris}",
    )
    rule = load_spec(_write(tmp_path, with_uris)).rules[0]
    assert rule.element_concept_uris == tuple(uris)


_PROBE = "probe: { name: require_document_attribute, params: { attribute: author } }"


def _rule(number: int, slug: str, extra: str = "") -> str:
    return (
        f"  - {{ number: {number}, slug: {slug}, spec_category: c, {_PROBE}"
        f"{extra} }}\n"
    )


def _with(extra: str) -> str:  # _GOOD with extra keys on its rule
    return _GOOD.replace("slug: demo-a", f"slug: demo-a\n    {extra}")


_KIND_PROBE = (
    "probe: { name: require_property, params: { kind: KIND, properties: [name] } }"
)
_TWO_LEVELS = "maturity_levels:\n  - {level: 0, id: a}\n  - {level: 1, id: b}\n"
_REJECTED = {
    # enums / references
    "bad provision": _with("provision: shall"),
    "bad status": _with("status: enabled"),
    "undeclared maturity": _with("maturity: 1"),
    "bad spec id token": _GOOD.replace("id: demo", "id: Demo-3"),
    "unknown category": _GOOD.replace("spec_category: c", "spec_category: nope"),
    "unregistered probe": _GOOD.replace("require_document_attribute", "nope"),
    "unknown element_id": _with("element_id: bogus"),
    "concept uris bare string": _with("element_concept_uris: https://example.org/x"),
    # YAML 1.1 coercions and wrong scalar types
    "category code NO -> False": _GOOD.replace("code: C", "code: NO"),
    "unquoted clause 1.10 -> float": _with("spec_clause_number: 1.10"),
    "maturity true == level 1": _with("maturity: true").replace(
        "categories:", _TWO_LEVELS + "categories:"
    ),
    "maturity 0.0 float": _with("maturity: 0.0"),
    "number as string": _GOOD.replace("number: 1", "number: '1'"),
    "number bool": _GOOD.replace("number: 1", "number: true"),
    "title int": _GOOD.replace("title: Demo", "title: 5"),
    "json_key int": _with("json_key: 5"),
    "empty level id": _GOOD.replace(
        "categories:", "maturity_levels:\n  - {level: 0, id: ''}\ncategories:"
    ),
    # unhashable / wrong container
    "maturity list": _with("maturity: [0]"),
    "provision list": _with("provision: [x]"),
    "categories scalar": "spec: { id: demo, title: D }\ncategories: 5\n",
    "rules scalar": _GOOD.split("rules:", maxsplit=1)[0] + "rules: 7\n",
    "levels scalar": _GOOD.replace("categories:", "maturity_levels: 5\ncategories:"),
    "spec id with trailing newline": _GOOD.replace("id: demo", 'id: "demo\\n"'),
    "category code with trailing newline": _GOOD.replace("code: C", 'code: "C\\n"'),
    "unknown top-level key": _GOOD + "rulez: []\n",
    "negative maturity level": _GOOD.replace(
        "categories:",
        "maturity_levels:\n  - {level: 0, id: a}\n  - {level: -1, id: b}\ncategories:",
    ),
    "probe on catalogue-only rule": _with("status: catalogue-only"),
    "mixed-type unknown keys": _GOOD + "1: a\nfoo: b\n",
    "duplicate YAML key": _with("number: 2"),
    "invalid YAML": "spec: [unclosed\n",
    "level false": _GOOD.replace(
        "categories:", "maturity_levels:\n  - {level: false, id: a}\ncategories:"
    ),
    "level string": _GOOD.replace(
        "categories:", "maturity_levels:\n  - {level: '0', id: a}\ncategories:"
    ),
    "concept uri not a string": _with("element_concept_uris: [1]"),
    "concept uris null": _with("element_concept_uris:"),
    # probe wiring
    "probe params as list": _GOOD.replace("{ attribute: author }", "[]"),
    "probe key typo": _GOOD.replace("params:", "parms:"),
    "probe attribute not a string": _GOOD.replace("attribute: author", "attribute: 5"),
    "probe attribute at wrong level": _GOOD.replace(
        "attribute: author", "attribute: supplier"
    ),
    "probe attribute != element_id": _with("element_id: timestamp"),
    # missing required keys
    "spec without title": _GOOD.replace("title: Demo", "uri: u"),
    "category without code": _GOOD.replace("    code: C\n", ""),
    "rule without slug": _GOOD.replace("    slug: demo-a\n", ""),
    # value constraints
    "number zero": _GOOD.replace("number: 1", "number: 0"),
    "number negative": _GOOD.replace("number: 1", "number: -5"),
    "number over 999": _GOOD.replace("number: 1", "number: 1000"),
    "category code not uppercase": _GOOD.replace("code: C", "code: d-f"),
    "slug without spec prefix": _GOOD.replace("demo-a", "other-a"),
    "slug not kebab": _GOOD.replace("demo-a", "demo_A"),
    "active rule without probe": _GOOD.replace(f"    {_PROBE}\n", ""),
    "probe param typo": _GOOD.replace("attribute:", "attribut:"),
    "probe param missing": _GOOD.replace("{ attribute: author }", "{}"),
    "probe param extra": _GOOD.replace("attribute: author", "attribute: author, x: 1"),
    # duplicates that would collide in output
    "same rule number": _GOOD + _rule(1, "demo-b"),
    "same slug": _GOOD + _rule(2, "demo-a"),
    "same json_key": _with("json_key: k") + _rule(2, "demo-b", ", json_key: k"),
    "duplicate sbom_specs": _GOOD.replace(
        "  title: Demo\n", "  title: Demo\n  sbom_specs: [spdx3, spdx3]\n"
    ),
    "roll-up with only inactive sub-rules": _GOOD.replace(
        "    probe:", "    aggregation: any-of\n    probe:"
    ).replace(f"    {_PROBE}\n", "")
    + _rule(1, "demo-b", ", sub: 1, parent: demo-a, status: tbd").replace(
        f"{_PROBE}, ", ""
    ),
    "active sub-rule under inactive roll-up": _GOOD.replace(
        "    probe:", "    aggregation: any-of\n    status: tbd\n    probe:"
    ).replace(f"    {_PROBE}\n", "")
    + _rule(1, "demo-b", ", sub: 1, parent: demo-a"),
    "roll-up over mixed kinds": _GOOD.replace(
        "    probe:", "    aggregation: any-of\n    probe:"
    ).replace(f"    {_PROBE}\n", "")
    + _rule(1, "demo-b", ", sub: 1, parent: demo-a").replace(
        _PROBE, _KIND_PROBE.replace("KIND", "system")
    )
    + _rule(1, "demo-c", ", sub: 2, parent: demo-a").replace(
        _PROBE, _KIND_PROBE.replace("KIND", "dataset")
    ),
    "same category id": _GOOD.replace(
        "    title: C\n", "    title: C\n  - { id: c, code: D, title: D }\n"
    ),
    "same category code -> same rule id": _GOOD.replace(
        "    title: C\n", "    title: C\n  - { id: d, code: C, title: D }\n"
    )
    + _rule(1, "demo-b").replace("spec_category: c", "spec_category: d"),
}


@pytest.mark.parametrize("text", _REJECTED.values(), ids=_REJECTED.keys())
def test_loader_rejects_bad_values(tmp_path: Path, text: str) -> None:
    with pytest.raises(SpecLoadError):  # never a raw TypeError/ValueError
        load_spec(_write(tmp_path, text))


def test_loader_accepts_probeless_tbd_and_catalogue_rules(tmp_path: Path) -> None:
    probeless = _GOOD.replace(f"    {_PROBE}\n", "")
    for status in ("tbd", "catalogue-only"):
        spec = load_spec(
            _write(
                tmp_path,
                probeless.replace(
                    "slug: demo-a", f"slug: demo-a\n    status: {status}"
                ),
            )
        )
        assert spec.rules[0].probe is None


def test_loader_rejects_non_utf8_file(tmp_path: Path) -> None:
    path = tmp_path / "demo.yaml"
    path.write_bytes(b"spec: {id: x\xff}\n")
    with pytest.raises(SpecLoadError):
        load_spec(path)


def test_unique_key_loader_allows_chained_merge_keys() -> None:
    text = "base: &B {x: 1}\nouter:\n  mid: &A {<<: *B, x: 2}\ntop: {<<: *A}\n"
    loaded = yaml.load(text, Loader=_UniqueKeyLoader)  # nosec B506
    assert loaded["top"] == loaded["outer"]["mid"] == {"x": 2}


def test_probe_registration_contract(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(probe_registry, "_PROBES", {})
    scoped = frozenset({"supplier"})
    for fn, attributes in (
        (lambda checker, **kw: [], None),  # **kwargs defeats param validation
        (lambda checker: [], scoped),  # scoped probe without `attribute`
    ):
        with pytest.raises(ValueError):
            probe_registry.probe("p", attributes=attributes)(fn)
    assert not probe_registry.registered_names()


def test_scoped_probe_attribute_must_be_given_explicitly(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def dflt(checker, *, attribute="supplier"):  # type: ignore[no-untyped-def]  # pylint: disable=unused-argument
        return []

    monkeypatch.setitem(probe_registry._PROBES, "dflt", dflt)
    monkeypatch.setitem(
        probe_registry._ATTRIBUTE_SCOPES, "dflt", frozenset({"supplier"})
    )
    text = _GOOD.replace(
        "require_document_attribute, params: { attribute: author }", "dflt"
    )
    with pytest.raises(SpecLoadError):  # default is not enough: no raw KeyError
        load_spec(_write(tmp_path, text))


def test_loaded_spec_survives_copy_and_pickle() -> None:
    spec = get_spec("fsct3")
    assert copy.deepcopy(spec) == spec
    assert pickle.loads(pickle.dumps(spec)) == spec  # nosec B301
    assert dataclasses.asdict(spec)["rules"][0]["slug"] == spec.rules[0].slug


def test_loader_keeps_quoted_scalars_as_strings(tmp_path: Path) -> None:
    text = _with("spec_clause_number: '1.10'").replace("code: C", "code: 'NO'")
    s = load_spec(_write(tmp_path, text))
    assert s.rules[0].spec_clause_number == "1.10"
    assert s.rule_id(s.rules[0]) == "SBOM-DEMO-NO-001"


def test_loader_requires_baseline_level_zero(tmp_path: Path) -> None:
    bad = _GOOD.replace(
        "categories:",
        "maturity_levels:\n  - level: 1\n    id: deep\ncategories:",
    )
    with pytest.raises(SpecLoadError):
        load_spec(_write(tmp_path, bad))


# ---- cross-spec consistency (every packaged rules/*.yaml) ------------------


@pytest.mark.parametrize("spec_id", spec_ids())
def test_rule_ids_unique_per_spec(spec_id: str) -> None:
    spec = get_spec(spec_id)
    ids = [spec.rule_id(r) for r in spec.rules]
    assert len(ids) == len(set(ids)), f"duplicate rule ids in {spec_id!r}: {ids}"


@pytest.mark.parametrize("spec_id", spec_ids())
def test_active_rules_have_a_probe(spec_id: str) -> None:
    spec = get_spec(spec_id)
    missing = [
        spec.rule_id(r)
        for r in spec.rules
        if r.status == "active"
        and r.probe is None
        and r.aggregation not in ("any-of", "all-of")  # rolled up from sub-rules
    ]
    assert not missing, f"{spec_id!r} has active rules with no probe: {missing}"


@pytest.mark.parametrize("spec_id", spec_ids())
def test_shipped_rules_have_filename_and_prose(spec_id: str) -> None:
    spec = get_spec(spec_id)
    assert (_RULES_DIR / f"{spec_id}.yaml").is_file()  # filename == spec id
    for rule in spec.rules:
        assert rule.competency_question and rule.warning, rule.slug
        if spec_id != "g7ai":  # its rules are scoped by probe params, not element ids
            assert rule.element_id, rule.slug


# Rule ids, their elements and status are public contract: changing one is
# deliberate, so it must show up here.
_CATALOGUE = {
    "ntia": "DF-001 supplier, DF-002 name, DF-003 version, DF-004 unique_identifier,"
    " DF-005 dependency_relationship, DF-006 author, DF-007 timestamp",
    "fsct3": "META-001 author, META-002 timestamp, META-003 sbom_type,"
    " META-004 primary_component!, META-005 dependency_relationship,"
    " COMP-001 name, COMP-002 version, COMP-003 supplier, COMP-004 unique_identifier,"
    " COMP-005 cryptographic_hash!, COMP-006 relationship!,"
    " COMP-007 concluded_license, COMP-008 copyright_notice",
}  # "!" = catalogue-only


@pytest.mark.parametrize("spec_id", spec_ids())
def test_shipped_catalogue_is_pinned(spec_id: str) -> None:
    if spec_id not in _CATALOGUE:  # pinned by the ontology snapshot instead
        assert spec_id in json.loads(_ONTOLOGY.read_text(encoding="utf-8"))
        return
    spec = get_spec(spec_id)
    got = [
        f"{spec.rule_id(r).split('-', 2)[2]} {r.element_id}"
        f"{'!' if r.status == 'catalogue-only' else ''}"
        for r in spec.rules
    ]
    assert got == [x.strip() for x in _CATALOGUE[spec_id].split(",")]
