# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for the CLI option surface (argument parsing + alias handling) and
the checker's maturity-target validation."""

# pylint: disable=missing-function-docstring

from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from pytest import MonkeyPatch

from ntia_conformance_checker import NTIAChecker, cli_utils

if TYPE_CHECKING:
    import argparse

_FIXTURE = str(
    Path(__file__).parent
    / "data"
    / "no_elements_missing"
    / "SPDXJSONExample-v2.3.spdx.json"
)


def _parse(monkeypatch: MonkeyPatch, argv: list[str]) -> argparse.Namespace:
    monkeypatch.setattr(sys, "argv", ["sbomcheck", *argv])
    return cli_utils.get_parsed_args()


# ---- report output type --------------------------------------------------


def test_output_quiet_aliases_to_none(monkeypatch: MonkeyPatch) -> None:
    assert _parse(monkeypatch, ["f.json", "--output", "quiet"]).output == "none"


def test_output_none_and_sarif_sbom_accepted(monkeypatch: MonkeyPatch) -> None:
    assert _parse(monkeypatch, ["f.json", "-r", "none"]).output == "none"
    assert _parse(monkeypatch, ["f.json", "-r", "sarif-sbom"]).output == "sarif-sbom"


def test_output_invalid_exits(monkeypatch: MonkeyPatch) -> None:
    with pytest.raises(SystemExit):
        _parse(monkeypatch, ["f.json", "--output", "bogus"])


# ---- maturity ------------------------------------------------------------


def test_mature_default_and_value(monkeypatch: MonkeyPatch) -> None:
    assert _parse(monkeypatch, ["f.json"]).maturity == 0
    assert _parse(monkeypatch, ["f.json", "-m", "2"]).maturity == 2
    assert _parse(monkeypatch, ["f.json", "--mature", "1"]).maturity == 1


def test_removed_flags_are_unrecognized(monkeypatch: MonkeyPatch) -> None:
    for argv in (
        ["f.json", "--maturity", "1"],
        ["f.json", "--maturity-level", "1"],
        ["f.json", "--embed-sbom"],
    ):
        with pytest.raises(SystemExit):
            _parse(monkeypatch, argv)


# ---- log verbosity -------------------------------------------------------


def test_verbosity_flags(monkeypatch: MonkeyPatch) -> None:
    assert _parse(monkeypatch, ["f.json"]).verbose == 0
    assert _parse(monkeypatch, ["f.json", "-v"]).verbose == 1
    assert _parse(monkeypatch, ["f.json", "-vv"]).verbose == 2
    assert _parse(monkeypatch, ["f.json", "--debug"]).debug is True
    assert _parse(monkeypatch, ["f.json", "-q"]).quiet is True


def test_skip_validation_shortcut(monkeypatch: MonkeyPatch) -> None:
    assert _parse(monkeypatch, ["f.json", "-k"]).skip_validation is True


# ---- maturity-target validation (checker) --------------------------------


def test_target_within_declared_levels_ok() -> None:
    # NTIA is flat (only level 0); maturity 0 is valid.
    checker = NTIAChecker(_FIXTURE)
    assert isinstance(checker.check_compliance(maturity=0), bool)


def test_target_above_declared_levels_raises() -> None:
    # NTIA is flat (only level 0); maturity 3 is invalid.
    checker = NTIAChecker(_FIXTURE)
    with pytest.raises(ValueError):
        checker.check_compliance(maturity=3)
