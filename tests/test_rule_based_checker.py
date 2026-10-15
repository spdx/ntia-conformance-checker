# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for the rule-based checkers: verdicts, maturity, messages, deprecations."""

# pylint: disable=missing-function-docstring,missing-class-docstring
# pylint: disable=protected-access,arguments-differ

from __future__ import annotations

import json
import sys
import warnings
from dataclasses import replace
from pathlib import Path
from typing import Any

import pytest
from pytest import CaptureFixture, MonkeyPatch

from ntia_conformance_checker import cli_utils, registry
from ntia_conformance_checker.base_checker import BaseChecker
from ntia_conformance_checker.fsct_checker import FSCT3Checker
from ntia_conformance_checker.main import main
from ntia_conformance_checker.ntia_checker import NTIAChecker
from ntia_conformance_checker.registry import get_spec
from ntia_conformance_checker.rule_based_checker import RuleBasedChecker
from ntia_conformance_checker.sbom_checker import SbomChecker
from ntia_conformance_checker.spec import (
    ProbeRef,
    Spec,
    SpecCategory,
    SpecMaturity,
    SpecRule,
)

DATA = Path(__file__).parent / "data"
_JSON = "SPDXJSONExample-v2.3.spdx.json"
OK = str(DATA / "no_elements_missing" / _JSON)
NO_SUPPLIER = str(DATA / "missing_supplier_name" / _JSON)
BSI_OK = str(DATA / "bsi" / "compliant_bsi_spdx3.json")
FSCT_OK = str(DATA / "spdx3" / "no_elements_missing.json")  # SPDX 3: has an SBOM type


def _spec(*rules: SpecRule) -> Spec:
    return Spec(
        id="adhoc",
        title="Ad Hoc Standard",
        categories=(SpecCategory(id="c", code="C", title="C"),),
        maturity_levels=(
            SpecMaturity(level=0, id="base"),
            SpecMaturity(level=1, id="deep"),
        ),
        rules=rules,
    )


def _doc_rule(number: int, element: str, **kwargs: object) -> SpecRule:
    return SpecRule(
        number=number,
        slug=f"adhoc-{element}-missing",
        spec_category="c",
        element_id=element,
        competency_question=f"{element} provided?",
        warning=f"Need the {element}.",
        probe=ProbeRef(
            name="require_document_attribute", params={"attribute": element}
        ),
        **kwargs,  # type: ignore[arg-type]
    )


def _comp_rule(number: int, element: str, **kwargs: object) -> SpecRule:
    return SpecRule(
        number=number,
        slug=f"adhoc-component-{element}-missing",
        spec_category="c",
        element_id=element,
        competency_question=f"All component {element}s provided?",
        warning=f"Components need a {element}.",
        probe=ProbeRef(
            name="require_component_attribute", params={"attribute": element}
        ),
        **kwargs,  # type: ignore[arg-type]
    )


def _text(checker: BaseChecker, capsys: CaptureFixture[str], maturity: int = 0) -> str:
    checker.print_table_output(maturity=maturity)
    return capsys.readouterr().out


# ---- parity with the checkers the engine replaced --------------------------
# golden_verdicts.json: "<file>|<sbom spec>|<standard>" -> "<verdict>:<row bits>",
# recorded from the hand-written checkers before the engine existed.

_GOLDEN = json.loads((DATA / "golden_verdicts.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("case", _GOLDEN)
def test_verdict_and_rows_match_golden(case: str) -> None:
    rel, sbom_spec, standard = case.split("|")
    checker = SbomChecker(str(DATA / rel), compliance=standard, sbom_spec=sbom_spec)
    rows = "".join(str(int(passed)) for _, passed in checker.table_elements)
    assert f"{int(checker.check_compliance())}:{rows}" == _GOLDEN[case]


# ---- deprecations -----------------------------------------------------------


def test_compliant_attribute_is_deprecated() -> None:
    checker = SbomChecker(OK)
    with pytest.warns(DeprecationWarning, match="check_compliance"):
        assert checker.compliant is checker.check_compliance() is True
    with pytest.warns(DeprecationWarning, match="check_compliance"):
        assert checker.ntia_minimum_elements_compliant is True


def test_fsct3_min_is_a_deprecated_alias_of_fsct3() -> None:
    with pytest.warns(DeprecationWarning, match="'fsct3'"):
        old = SbomChecker(NO_SUPPLIER, compliance="fsct3-min")
    with warnings.catch_warnings():
        warnings.simplefilter("error")  # the current id must not warn
        new = SbomChecker(NO_SUPPLIER, compliance="fsct3")
    assert old.table_elements == new.table_elements
    assert (old.compliance_standard, new.compliance_standard) == ("fsct3-min", "fsct3")
    assert old.output_html() == new.output_html()  # same report title


# ---- maturity ---------------------------------------------------------------


@pytest.mark.parametrize(
    ("standard", "file", "maturity", "valid"),
    [
        ("ntia", OK, 0, True),
        ("ntia", OK, 1, False),  # NTIA declares only the baseline
        ("ntia", OK, -1, False),
        ("fsct3", FSCT_OK, 2, True),  # FSCT 3 declares three levels
        ("fsct3", FSCT_OK, 3, False),
        ("bsi", BSI_OK, 1, False),
    ],
)
def test_maturity_must_be_a_declared_level(
    standard: str, file: str, maturity: int, valid: bool
) -> None:
    sbom_spec = "spdx3" if file in (BSI_OK, FSCT_OK) else "spdx2"
    checker = SbomChecker(file, compliance=standard, sbom_spec=sbom_spec)
    if valid:
        assert checker.check_compliance(maturity) is True
    else:
        with pytest.raises(ValueError, match="maturity level"):
            checker.check_compliance(maturity)


def test_maturity_scopes_which_rules_block(capsys: CaptureFixture[str]) -> None:
    # Names are present; suppliers (required at level 1 only) are missing.
    spec = _spec(_comp_rule(1, "name"), _comp_rule(2, "supplier", maturity=1))
    checker = RuleBasedChecker(NO_SUPPLIER, compliance=spec)
    assert checker.check_compliance(0) is True
    assert checker.check_compliance(1) is False
    assert "Components need a supplier." not in _text(checker, capsys, 0)
    assert "- Components need a supplier." in _text(checker, capsys, 1)


def test_recommendation_is_reported_but_does_not_block(
    capsys: CaptureFixture[str],
) -> None:
    spec = _spec(_comp_rule(1, "supplier", provision="recommendation"))
    checker = RuleBasedChecker(NO_SUPPLIER, compliance=spec)
    assert checker.check_compliance() is True
    assert checker.table_elements == [("All component suppliers provided?", False)]
    assert "Unmet requirements" not in _text(checker, capsys)


def test_alias_warning_is_attributed_to_the_caller() -> None:
    # Python shows a DeprecationWarning by default only for the user's own code.
    for make in (
        lambda: SbomChecker(OK, compliance="fsct3-min"),
        lambda: FSCT3Checker(OK, compliance="fsct3-min"),
        lambda: RuleBasedChecker(OK, compliance="fsct3-min"),
    ):
        with pytest.warns(DeprecationWarning) as recorded:
            make()
        assert recorded[0].filename == __file__


def test_6_0_0_style_subclasses_keep_working(capsys: CaptureFixture[str]) -> None:
    class WithoutMaturity(BaseChecker):
        def check_compliance(self) -> bool:  # type: ignore[override]
            return True

    class AssignsVerdict(BaseChecker):
        def __init__(self, file: str) -> None:
            super().__init__(file, compliance="ntia")
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", DeprecationWarning)
                self.compliant = True

        def check_compliance(self) -> bool:  # type: ignore[override]
            return False

    for checker in (WithoutMaturity(OK, compliance="ntia"), AssignsVerdict(OK)):
        assert checker.output_json()["isConformant"] is True
        assert "Conformant: True" in _text(checker, capsys)


def test_active_rule_without_probe_is_rejected() -> None:
    bare = SpecRule(number=1, slug="adhoc-bare", spec_category="c", element_id="name")
    with pytest.raises(ValueError, match="no probe"):  # would pass vacuously
        RuleBasedChecker(OK, compliance=_spec(bare))


def test_several_rules_on_one_element_list_its_missing_info_once() -> None:
    spec = _spec(_comp_rule(1, "supplier"), _comp_rule(2, "supplier", maturity=1))
    checker = RuleBasedChecker(NO_SUPPLIER, compliance=spec)
    assert [name for name, _ in checker.all_components_without_info] == ["supplier"]


@pytest.mark.parametrize(("maturity", "verdict"), [(0, True), (1, False)])
def test_maturity_reaches_every_output_and_the_exit_code(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
    maturity: int,
    verdict: bool,
) -> None:
    spec = _spec(_comp_rule(1, "name"), _comp_rule(2, "supplier", maturity=1))
    monkeypatch.setitem(registry._REGISTRY, "adhoc", spec)
    monkeypatch.setattr(cli_utils, "SUPPORTED_COMPLIANCE_STANDARDS", {"adhoc"})
    checker = SbomChecker(NO_SUPPLIER, compliance="adhoc")

    assert checker.output_json(maturity=maturity)["isConformant"] is verdict
    assert f"Conformant: {verdict}" in _text(checker, capsys, maturity)
    assert f"Conformant: {verdict}" in checker.output_html(maturity)

    argv = ["sbomcheck", "-r", "none", "-c", "adhoc", "-m", str(maturity), NO_SUPPLIER]
    monkeypatch.setattr(sys, "argv", argv)
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == (0 if verdict else 1)


def test_json_reports_whether_an_sbom_type_is_provided() -> None:
    fsct = SbomChecker(FSCT_OK, compliance="fsct3", sbom_spec="spdx3")
    assert fsct.output_json()["sbomTypeProvided"] is True
    assert SbomChecker(OK).output_json()["sbomTypeProvided"] is False  # SPDX 2


def test_6_0_0_style_output_overrides_and_extended_elements(
    capsys: CaptureFixture[str],
) -> None:
    class Custom(NTIAChecker):
        MIN_ELEMENTS = [*NTIAChecker.MIN_ELEMENTS, "checksum"]  # not in the spec

        def output_json(self) -> dict[str, Any]:  # type: ignore[override]
            return {"custom": True}

    checker = Custom(NO_SUPPLIER)  # unknown element must not raise
    cli_utils.print_output(checker, output_type="json", output_file=None, verbose=False)
    assert '"custom": true' in capsys.readouterr().out


def test_unevaluated_and_advisory_rules_are_not_unmet_requirements(
    capsys: CaptureFixture[str],
) -> None:
    advisory = _doc_rule(1, "sbom_type", provision="recommendation")
    out = _text(RuleBasedChecker(OK, compliance=_spec(advisory)), capsys)
    assert "Conformant: True" in out and "Unmet requirements" not in out

    rule = replace(_comp_rule(1, "supplier"), warning="")
    no_text = replace(rule, element_description="SBOM type (SPDX 3)")
    out = _text(RuleBasedChecker(NO_SUPPLIER, compliance=_spec(no_text)), capsys)
    assert "- SBOM type (SPDX 3) is missing." in out


# ---- messages and reports ---------------------------------------------------


def test_failure_messages_come_from_the_yaml(capsys: CaptureFixture[str]) -> None:
    warning = next(
        r.warning for r in get_spec("ntia").rules if r.element_id == "supplier"
    )
    assert warning
    bad = _text(SbomChecker(NO_SUPPLIER), capsys)
    assert f"Unmet requirements:\n- {warning}\n" in bad
    assert "Unmet requirements" not in _text(SbomChecker(OK), capsys)
    assert f"<li>{warning}</li>" in SbomChecker(NO_SUPPLIER).output_html()


def test_message_falls_back_to_the_element_description(
    capsys: CaptureFixture[str],
) -> None:
    rule = _comp_rule(1, "supplier", element_description="supplier name")
    spec = _spec(replace(rule, warning=""))
    assert "- Supplier name is missing." in _text(
        RuleBasedChecker(NO_SUPPLIER, compliance=spec), capsys
    )


def test_adhoc_spec_is_reported_under_its_own_title(
    capsys: CaptureFixture[str],
) -> None:
    out = _text(RuleBasedChecker(OK, compliance=_spec(_doc_rule(1, "author"))), capsys)
    assert "Ad Hoc Standard Conformance Results" in out
    assert "Unsupported" not in out


def test_unparsable_file_is_not_compliant() -> None:
    for standard in ("ntia", "fsct3"):
        checker = SbomChecker("no/such/file.json", compliance=standard)
        assert checker.check_compliance() is False
        assert not any(passed for _, passed in checker.table_elements)


def test_element_the_checker_cannot_evaluate_fails_loudly() -> None:
    rule = SpecRule(
        number=1,
        slug="adhoc-hash-missing",
        spec_category="c",
        element_id="cryptographic_hash",
        probe=ProbeRef(
            name="require_component_attribute",
            params={"attribute": "cryptographic_hash"},
        ),
    )
    with pytest.raises(ValueError, match="cryptographic_hash"):
        RuleBasedChecker(OK, compliance=_spec(rule))


def test_standard_defined_only_by_yaml_is_dispatched(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setitem(registry._REGISTRY, "adhoc", _spec(_doc_rule(1, "author")))
    checker = SbomChecker(OK, compliance="adhoc")
    assert checker.__class__.__name__ == "RuleBasedChecker"
    assert checker.check_compliance() is True


def test_unknown_standard_is_rejected() -> None:
    with pytest.raises(ValueError, match="Unknown compliance standard"):
        SbomChecker(OK, compliance="nope")


# ---- CLI --------------------------------------------------------------------


@pytest.mark.parametrize(
    ("argv", "code"),
    [
        ([OK], 0),
        ([NO_SUPPLIER], 1),
        (["-c", "fsct3", "-m", "2", "-s", "spdx3", FSCT_OK], 0),
        (["-m", "1", OK], 2),  # NTIA has no level 1
    ],
)
def test_exit_code(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str], argv: list[str], code: int
) -> None:
    monkeypatch.setattr(sys, "argv", ["sbomcheck", "-r", "none", *argv])
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == code
    capsys.readouterr()
