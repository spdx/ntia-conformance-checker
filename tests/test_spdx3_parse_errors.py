# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests that SPDX 3 content that is not valid SPDX 3 JSON-LD is a parsing
error, and that the SBOM type is read from whichever root is an SBOM."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

from ntia_conformance_checker import main
from ntia_conformance_checker.sbom_checker import SbomChecker

if TYPE_CHECKING:
    from collections.abc import Callable

FIXTURE = Path(__file__).parent / "data" / "spdx3" / "no_elements_missing.json"

Doc = dict[str, Any]


def _load() -> Doc:
    return copy.deepcopy(json.loads(FIXTURE.read_text(encoding="utf-8")))


def _first(doc: Doc, type_: str) -> Doc:
    return next(e for e in doc["@graph"] if e.get("type") == type_)


def _write(tmp_path: Path, doc: Any) -> str:
    path = tmp_path / "sbom.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    return str(path)


DAMAGE: dict[str, Callable[[Doc], None]] = {
    "no spdxId": lambda d: _first(d, "Person").pop("spdxId"),
    "unknown type": lambda d: _first(d, "Person").update(type="NotAnSpdxType"),
    "abstract type": lambda d: _first(d, "software_File").update(
        type="software_SoftwareArtifact"
    ),
    "graph is an object": lambda d: d.update({"@graph": {}}),
    "not JSON-LD": lambda d: d.clear(),
}


@pytest.mark.parametrize("compliance", ["ntia", "fsct3-min", "bsi"])
@pytest.mark.parametrize("damage", DAMAGE.values(), ids=DAMAGE.keys())
def test_bad_spdx3_is_a_parsing_error(
    tmp_path: Path, damage: Callable[[Doc], None], compliance: str
) -> None:
    """The checker reports a parsing error instead of raising."""
    doc = _load()
    damage(doc)
    checker = SbomChecker(
        _write(tmp_path, doc), compliance=compliance, sbom_spec="spdx3"
    )
    assert checker.doc is None
    assert checker.parsing_errors
    assert not checker.compliant


def test_bad_spdx3_cli_exit(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The CLI exits with 1 and a report, not a traceback."""
    doc = _load()
    DAMAGE["abstract type"](doc)
    monkeypatch.setattr(sys, "argv", ["sbomcheck", _write(tmp_path, doc)])
    with pytest.raises(SystemExit) as exc:
        main.main()
    assert exc.value.code == 1


@pytest.mark.parametrize(
    ("roots", "has_type"),
    [
        (["dataset_DatasetPackage", "software_Sbom"], True),
        (["dataset_DatasetPackage"], False),
    ],
    ids=["sbom not first", "no sbom root"],
)
def test_sbom_type_from_any_root(
    tmp_path: Path, roots: list[str], has_type: bool
) -> None:
    """The SBOM type comes from the root that is an SBOM, wherever it is."""
    doc = _load()
    _first(doc, "SpdxDocument")["rootElement"] = [
        _first(doc, type_)["spdxId"] for type_ in roots
    ]
    checker = SbomChecker(_write(tmp_path, doc), sbom_spec="spdx3")
    assert bool(checker.sbom_gen_context) is has_type
    messages = [m.validation_message for m in checker.conformance_messages]
    assert any("SBOM type" in m for m in messages) is not has_type
