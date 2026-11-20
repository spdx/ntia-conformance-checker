# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests that a link to a missing element blocks compliance in every checker."""

# pylint: disable=missing-function-docstring

import json
from pathlib import Path
from typing import Any

import pytest

from ntia_conformance_checker.sbom_checker import SbomChecker

DATA = Path(__file__).parent / "data"
SPDX2_BASE = DATA / "no_elements_missing" / "SPDXJSONExample-v2.3.spdx.json"
SPDX3_BASE = DATA / "spdx3" / "no_elements_missing.json"
BSI_BASE = DATA / "bsi" / "compliant_bsi_spdx3.json"

# A link target of each kind, per SBOM spec.
TARGETS = {
    "spdx2": {
        "missing": "SPDXRef-Missing",
        "none": "NONE",
        "external": "DocumentRef-spdx-tool-1.2:SPDXRef-Other",
    },
    "spdx3": {
        "missing": "https://example.org/missing",
        "none": "https://spdx.org/rdf/3.0.1/terms/Core/NoneElement",
        "external": "https://example.org/external",
    },
}


def _link_spdx2(data: dict[str, Any], target: str) -> None:
    """Add a DEPENDS_ON relationship from the described package to target."""
    data["relationships"].append(
        {
            "spdxElementId": data["documentDescribes"][0],
            "relationshipType": "DEPENDS_ON",
            "relatedSpdxElement": target,
        }
    )


def _link_spdx3(data: dict[str, Any], target: str) -> None:
    """Add a dependsOn relationship from the SBOM root to target, and import it."""
    graph = data["@graph"]
    by_type = {e["type"]: e for e in graph}
    source = by_type["software_Sbom"]["rootElement"][0]
    graph.append(
        {
            "type": "Relationship",
            "spdxId": "https://example.org/rel-link",
            "creationInfo": by_type["SpdxDocument"]["creationInfo"],
            "relationshipType": "dependsOn",
            "from": source,
            "to": [target],
            # BSI TR-03183-2 v2.1.0 §5.2.2 requires a stated completeness
            "completeness": "complete",
        }
    )
    if target == TARGETS["spdx3"]["external"]:
        by_type["SpdxDocument"]["import"] = [
            {"type": "ExternalMap", "externalSpdxId": target}
        ]


@pytest.mark.parametrize("kind", ["missing", "none", "external"])
@pytest.mark.parametrize(
    ("compliance", "spec", "base"),
    [
        ("ntia", "spdx2", SPDX2_BASE),
        ("ntia", "spdx3", SPDX3_BASE),
        ("fsct3-min", "spdx3", SPDX3_BASE),
        ("bsi", "spdx3", BSI_BASE),
    ],
    ids=["ntia-spdx2", "ntia-spdx3", "fsct3-spdx3", "bsi-spdx3"],
)
def test_link_target_compliance(
    tmp_path: Path,
    compliance: str,
    spec: str,
    base: Path,
    kind: str,
) -> None:
    compliant = kind != "missing"
    data = json.loads(base.read_text(encoding="utf-8"))
    (_link_spdx2 if spec == "spdx2" else _link_spdx3)(data, TARGETS[spec][kind])
    sbom_file = tmp_path / "sbom.json"
    sbom_file.write_text(json.dumps(data), encoding="utf-8")

    # SPDX 2 validation also reports a missing element; skip it to isolate.
    checker = SbomChecker(
        str(sbom_file), validate=False, compliance=compliance, sbom_spec=spec
    )

    assert checker.has_unknown_pointers is not compliant
    assert checker.compliant is compliant
    assert checker.output_json()["isConformant"] is compliant
