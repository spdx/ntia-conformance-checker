# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests that the JSON report is sorted and written in a stable form."""

import json
import logging
from pathlib import Path
from typing import Any, Callable

import pytest
import rfc8785

from ntia_conformance_checker.cli_utils import print_output
from ntia_conformance_checker.sbom_checker import SbomChecker

SBOM_FILE = (
    Path(__file__).parent
    / "data"
    / "graph_connectivity"
    / "unordered_output"
    / "unordered_output_spdx3.json"
)
P = "https://example.com/unordered/"


def _graph_validation() -> Any:
    """Return the graph validation part of the fixture SBOM's JSON report."""
    checker = SbomChecker(str(SBOM_FILE), sbom_spec="spdx3")
    return checker.output_json()["graphValidation"]


@pytest.mark.parametrize(
    ("group", "key", "expected"),
    [
        (
            "unknownPointers",
            "unknownPointerEdges",
            [
                (f"{P}Package-A", [f"{P}Missing-1", f"{P}Missing-2", f"{P}Missing-3"]),
                (f"{P}Package-F1", [f"{P}Missing-6"]),
                (f"{P}Package-F2", [f"{P}Missing-4", f"{P}Missing-5"]),
            ],
        ),
        (
            "floatingComponents",
            "floatingComponentIds",
            [f"{P}Package-F{i}" for i in range(1, 7)],
        ),
    ],
)
def test_graph_validation_lists_sorted(group: str, key: str, expected: Any) -> None:
    """Lists from sets or unordered relationships come out sorted."""
    value = _graph_validation()[group][key]
    assert (list(value.items()) if isinstance(value, dict) else value) == expected


def _indented(data: Any) -> bytes:
    """Return ``data`` as printed to stdout: indented, with sorted keys."""
    return (json.dumps(data, indent=2, sort_keys=True) + "\n").encode()


@pytest.mark.parametrize(
    ("file_name", "serialize"),
    [
        ("report.json", rfc8785.dumps),
        (None, _indented),
    ],
)
def test_json_output_form(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    file_name: str | None,
    serialize: Callable[[Any], bytes],
) -> None:
    """A file is RFC 8785 canonical; stdout is indented with sorted keys."""
    checker = SbomChecker(str(SBOM_FILE), sbom_spec="spdx3")
    out_file = tmp_path / file_name if file_name else None
    print_output(
        checker,
        output_type="json",
        output_file=str(out_file) if out_file else None,
        verbose=False,
    )
    data = out_file.read_bytes() if out_file else capsys.readouterr().out.encode()
    assert data == serialize(json.loads(data))


def test_json_file_not_written_if_not_canonicalizable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    """A lone surrogate cannot be UTF-8 encoded, so no file is written."""
    checker = SbomChecker(str(SBOM_FILE), sbom_spec="spdx3")
    monkeypatch.setattr(checker, "output_json", lambda: {"sbomName": "\ud800"})
    out_file = tmp_path / "report.json"
    with caplog.at_level(logging.ERROR):
        print_output(
            checker, output_type="json", output_file=str(out_file), verbose=False
        )
    assert not out_file.exists()
    assert "Could not write JSON output file" in caplog.text
