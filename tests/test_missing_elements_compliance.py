# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests that a link to a missing element blocks compliance in every checker."""

import json
from pathlib import Path

import pytest

from ntia_conformance_checker.sbom_checker import SbomChecker

DATA = Path(__file__).parent / "data"
SPDX2 = DATA / "no_elements_missing" / "SPDXJSONExample-v2.3.spdx.json"
SPDX3 = DATA / "spdx3" / "no_elements_missing.json"
BSI = DATA / "bsi" / "compliant_bsi_spdx3.json"
EXTERNAL = "https://example.org/external"


@pytest.mark.parametrize(
    ("compliance", "base", "target", "compliant"),
    [
        ("ntia", SPDX2, "SPDXRef-Missing", False),
        ("ntia", SPDX3, "https://example.org/missing", False),
        ("fsct3-min", SPDX3, "https://example.org/missing", False),
        ("bsi", BSI, "https://example.org/missing", False),
        ("ntia", SPDX2, "DocumentRef-spdx-tool-1.2:SPDXRef-Other", True),
        ("ntia", SPDX3, EXTERNAL, True),
    ],
)
def test_link_target_compliance(
    tmp_path: Path, compliance: str, base: Path, target: str, compliant: bool
) -> None:
    """A dependency on a missing element fails; on a declared external one, not."""
    data = json.loads(base.read_text(encoding="utf-8"))
    spec = "spdx2" if base == SPDX2 else "spdx3"
    if spec == "spdx2":
        data["relationships"].append(
            {
                "spdxElementId": data["documentDescribes"][0],
                "relationshipType": "DEPENDS_ON",
                "relatedSpdxElement": target,
            }
        )
    else:
        by_type = {e["type"]: e for e in data["@graph"]}
        data["@graph"].append(
            {
                "type": "Relationship",
                "spdxId": "https://example.org/rel-link",
                "creationInfo": by_type["SpdxDocument"]["creationInfo"],
                "relationshipType": "dependsOn",
                "from": by_type["software_Sbom"]["rootElement"][0],
                "to": [target],
                "completeness": "complete",
            }
        )
        by_type["SpdxDocument"]["import"] = [
            {"type": "ExternalMap", "externalSpdxId": EXTERNAL}
        ]
    sbom_file = tmp_path / "sbom.json"
    sbom_file.write_text(json.dumps(data), encoding="utf-8")

    # validate=False: SPDX 2 validation alone would also fail a missing element
    checker = SbomChecker(
        str(sbom_file), validate=False, compliance=compliance, sbom_spec=spec
    )

    assert checker.compliant is compliant
