# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for reports when no component is reachable from the SBOM root."""

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest

from ntia_conformance_checker import BSIChecker, NTIAChecker
from ntia_conformance_checker.base_checker import BaseChecker
from ntia_conformance_checker.fsct_checker import FSCT3Checker

DATA = Path(__file__).parent / "data"
SPDX2 = DATA / "no_elements_missing/SPDXJSONExample-v2.3.spdx.json"
SPDX3 = DATA / "spdx3/no_elements_missing.json"
BSI = DATA / "bsi/compliant_bsi_spdx3.json"
NOTE = "component requirements were not evaluated"


def _empty_root(sbom: dict[str, Any]) -> None:
    for obj in sbom["@graph"]:
        if obj["type"] == "software_Sbom":
            obj["rootElement"] = []


def _two_docs(sbom: dict[str, Any]) -> None:
    doc = next(o for o in sbom["@graph"] if o["type"] == "SpdxDocument")
    sbom["@graph"].append({**doc, "spdxId": doc["spdxId"] + "-2"})


def _no_describes(sbom: dict[str, Any]) -> None:
    sbom.pop("documentDescribes", None)
    sbom["relationships"] = [
        r for r in sbom["relationships"] if r["relationshipType"] != "DESCRIBES"
    ]


@pytest.mark.parametrize(
    ("checker_cls", "src", "edit", "evaluated"),
    [
        (NTIAChecker, SPDX3, None, True),
        (NTIAChecker, SPDX3, _empty_root, False),
        (NTIAChecker, SPDX3, _two_docs, False),
        (FSCT3Checker, SPDX3, _empty_root, False),
        (BSIChecker, BSI, _empty_root, False),
        (NTIAChecker, SPDX2, None, True),
        (NTIAChecker, SPDX2, _no_describes, False),
    ],
)
def test_components_evaluated(
    tmp_path: Path,
    checker_cls: type[BaseChecker],
    src: Path,
    edit: Callable[[dict[str, Any]], None] | None,
    evaluated: bool,
) -> None:
    """Nothing reachable is reported as not evaluated, never as compliant."""
    sbom = json.loads(src.read_text())
    if edit:
        edit(sbom)
    test_file = tmp_path / "sbom.json"
    test_file.write_text(json.dumps(sbom))

    spec = "spdx2" if src == SPDX2 else "spdx3"
    checker = checker_cls(str(test_file), sbom_spec=spec)
    result = checker.output_json()

    assert result["componentsEvaluated"] is evaluated
    assert (NOTE in checker.output_html()) is not evaluated
    if not evaluated:
        groups = [
            v["allProvided"]
            for v in result.values()
            if isinstance(v, dict) and "allProvided" in v
        ]
        rows = [
            ok for label, ok in checker.table_elements if "component" in label.lower()
        ]
        assert not checker.compliant
        assert rows and not any(groups + rows)
