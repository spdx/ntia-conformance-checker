# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for the declarative-rules model: rule ids, maturity target
scoping, provision -> severity, blocking compliance, and loader validation."""

# pylint: disable=missing-function-docstring

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from ntia_conformance_checker.registry import get_spec
from ntia_conformance_checker.spec import (
    Spec,
    SpecCategory,
    SpecMaturity,
    SpecRule,
)
from ntia_conformance_checker.spec_loader import SpecLoadError, load_spec

if TYPE_CHECKING:
    from pathlib import Path


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


@pytest.mark.parametrize(
    "mutation",
    [
        ("slug: demo-a", "slug: demo-a\n    provision: shall"),  # bad provision
        ("slug: demo-a", "slug: demo-a\n    status: enabled"),  # bad status
        ("slug: demo-a", "slug: demo-a\n    maturity: 1"),  # undeclared level
        ("id: demo", "id: Demo-3"),  # bad spec id token
    ],
)
def test_loader_rejects_bad_values(tmp_path: Path, mutation: tuple[str, str]) -> None:
    bad = _GOOD.replace(*mutation)
    with pytest.raises(SpecLoadError):
        load_spec(_write(tmp_path, bad))


def test_loader_requires_baseline_level_zero(tmp_path: Path) -> None:
    bad = _GOOD.replace(
        "categories:",
        "maturity_levels:\n  - level: 1\n    id: deep\ncategories:",
    )
    with pytest.raises(SpecLoadError):
        load_spec(_write(tmp_path, bad))
