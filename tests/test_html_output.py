# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests that the HTML report escapes SBOM content and that a report write
failure exits with 2."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from spdx_tools.spdx.validation.validation_message import (
    SpdxElementType,
    ValidationContext,
    ValidationMessage,
)

from ntia_conformance_checker import main
from ntia_conformance_checker.cli_utils import print_output
from ntia_conformance_checker.report import ReportContext, report_html
from ntia_conformance_checker.sbom_checker import SbomChecker

BAD = "<script>x</script>"
SAFE = "&lt;script&gt;x&lt;/script&gt;"
SBOM_FILE = str(Path(__file__).parent / "data" / "spdx3" / "no_elements_missing.json")

_MESSAGE = ValidationMessage(
    BAD,
    ValidationContext(spdx_id=BAD, parent_id=BAD, element_type=SpdxElementType.PACKAGE),
)

HTML_CASES: dict[str, ReportContext] = {
    "parsing error": ReportContext(parsing_errors=[BAD]),
    "compliance standard": ReportContext(compliance_standard=BAD),
    "sbom spec": ReportContext(
        compliance_standard="ntia", sbom_spec=BAD, validation_messages=[_MESSAGE]
    ),
    "validation message": ReportContext(
        compliance_standard="ntia", validation_messages=[_MESSAGE]
    ),
    "conformance message": ReportContext(
        compliance_standard="ntia", conformance_messages=[_MESSAGE]
    ),
    "component name": ReportContext(
        compliance_standard="ntia",
        components_without_info=[("Supplier", [(BAD, "id"), ("", BAD)])],
    ),
    "missing link": ReportContext(
        compliance_standard="ntia",
        unknown_pointer_edges={BAD: [BAD]},
        missing_element_ids={BAD},
    ),
    "floating component": ReportContext(
        compliance_standard="ntia", floating_component_ids={BAD}
    ),
}


@pytest.mark.parametrize("rc", HTML_CASES.values(), ids=HTML_CASES.keys())
def test_html_report_escapes(rc: ReportContext) -> None:
    """Text from the SBOM or the command line is escaped."""
    html = report_html(rc, verbose=True)
    assert BAD not in html
    assert SAFE in html


@pytest.mark.parametrize("output_type", ["json", "html"])
def test_report_write_failure(tmp_path: Path, output_type: str) -> None:
    """A report file that cannot be written gives False, and exit code 2."""
    checker = SbomChecker(SBOM_FILE, sbom_spec="spdx3")
    assert not print_output(
        checker, output_type=output_type, output_file=str(tmp_path), verbose=False
    )
    argv = ["sbomcheck", SBOM_FILE, "-r", output_type, "-o", str(tmp_path)]
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(sys, "argv", argv)
        with pytest.raises(SystemExit) as exc:
            main.main()
    assert exc.value.code == 2


def test_html_file_escapes_filename(tmp_path: Path) -> None:
    """The file name in the HTML page is escaped."""
    sbom = tmp_path / "a&b.json"  # no < or >: not allowed in Windows file names
    sbom.write_bytes(Path(SBOM_FILE).read_bytes())
    out = tmp_path / "report.html"
    checker = SbomChecker(str(sbom), sbom_spec="spdx3")
    assert print_output(
        checker, output_type="html", output_file=str(out), verbose=False
    )
    assert "a&amp;b.json" in out.read_text(encoding="utf-8")


def test_html_file_lone_surrogate(tmp_path: Path) -> None:
    """A name that is not valid UTF-8 is written as an escape, not a crash."""
    doc = json.loads(Path(SBOM_FILE).read_text(encoding="utf-8"))
    pkg = next(e for e in doc["@graph"] if e["type"] == "dataset_DatasetPackage")
    pkg["name"] = "\ud800"
    pkg.pop("software_packageVersion", None)
    sbom = tmp_path / "sbom.json"
    sbom.write_text(json.dumps(doc), encoding="utf-8")
    out = tmp_path / "report.html"
    checker = SbomChecker(str(sbom), sbom_spec="spdx3")
    assert print_output(checker, output_type="html", output_file=str(out), verbose=True)
    assert "\\ud800" in out.read_text(encoding="utf-8")
