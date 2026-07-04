# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for the CLI option surface (argument parsing + alias handling)."""

# pylint: disable=missing-function-docstring

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

import pytest
from pytest import MonkeyPatch

from ntia_conformance_checker import cli_utils

if TYPE_CHECKING:
    import argparse


def _parse(monkeypatch: MonkeyPatch, argv: list[str]) -> argparse.Namespace:
    monkeypatch.setattr(sys, "argv", ["sbomcheck", *argv])
    return cli_utils.get_parsed_args()


# ---- report output type --------------------------------------------------


def test_output_quiet_aliases_to_none(monkeypatch: MonkeyPatch) -> None:
    assert _parse(monkeypatch, ["f.json", "--output", "quiet"]).output == "none"


def test_output_none_accepted(monkeypatch: MonkeyPatch) -> None:
    assert _parse(monkeypatch, ["f.json", "-r", "none"]).output == "none"


def test_output_invalid_exits(monkeypatch: MonkeyPatch) -> None:
    with pytest.raises(SystemExit):
        _parse(monkeypatch, ["f.json", "--output", "bogus"])


# ---- log verbosity -------------------------------------------------------


def test_verbosity_flags(monkeypatch: MonkeyPatch) -> None:
    assert _parse(monkeypatch, ["f.json"]).verbose == 0
    assert _parse(monkeypatch, ["f.json", "-v"]).verbose == 1
    assert _parse(monkeypatch, ["f.json", "-vv"]).verbose == 2
    assert _parse(monkeypatch, ["f.json", "--debug"]).debug is True
    assert _parse(monkeypatch, ["f.json", "-q"]).quiet is True


def test_skip_validation_shortcut(monkeypatch: MonkeyPatch) -> None:
    assert _parse(monkeypatch, ["f.json", "-k"]).skip_validation is True
