# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests that the JSON report is sorted and written in a stable form."""

import json
from pathlib import Path

import pytest
import rfc8785

from ntia_conformance_checker.cli_utils import print_output
from ntia_conformance_checker.sbom_checker import SbomChecker

SBOM_FILE = str(
    Path(__file__).parent
    / "data/graph_connectivity/unordered_output/unordered_output_spdx3.json"
)
P = "https://example.com/unordered/"


def test_graph_validation_sorted() -> None:
    """Lists from sets or unordered relationships come out sorted."""
    graph = SbomChecker(SBOM_FILE, sbom_spec="spdx3").output_json()["graphValidation"]
    edges = graph["unknownPointers"]["unknownPointerEdges"]
    assert list(edges.items()) == [
        (f"{P}A", [f"{P}M1", f"{P}M2"]),
        (f"{P}F2", [f"{P}M3"]),
    ]
    assert graph["floatingComponents"]["floatingComponentIds"] == [
        f"{P}F{i}" for i in range(1, 6)
    ]


@pytest.mark.parametrize("to_file", [True, False])
def test_json_output_form(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], to_file: bool
) -> None:
    """A file is RFC 8785 canonical; stdout is indented with sorted keys."""
    out_file = tmp_path / "report.json"
    print_output(
        SbomChecker(SBOM_FILE, sbom_spec="spdx3"),
        output_type="json",
        output_file=str(out_file) if to_file else None,
        verbose=False,
    )
    if to_file:
        data = out_file.read_bytes()
        assert data == rfc8785.dumps(json.loads(data))
    else:
        out = capsys.readouterr().out
        assert out == json.dumps(json.loads(out), indent=2, sort_keys=True) + "\n"
