# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests functions in main"""

# pylint: disable=missing-function-docstring

from pathlib import Path
from typing import List, Tuple

import pytest
from beartype.roar import BeartypeCallHintParamViolation

from ntia_conformance_checker.cli_utils import get_sbom_spec, get_spdx_version

spdx2_2_dir = Path(__file__).parent / "data" / "missing_component_name"
spdx2_3_dir = Path(__file__).parent / "data" / "missing_timestamp"
spdx3_0_dir = Path(__file__).parent / "data" / "spdx3"


detect_version_test: List[Tuple[Path, Tuple[int, ...]]] = [
    (spdx2_2_dir / "SPDXJsonExample.json", (2, 2)),
    (spdx2_2_dir / "SPDXXmlExample.xml", (2, 2)),
    (spdx2_2_dir / "SPDXYamlExample.yaml", (2, 2)),
    (spdx2_3_dir / "SPDXJSONExample-v2.3.spdx.json", (2, 3)),
    (spdx2_3_dir / "SPDXRdfExample-v2.3.spdx.rdf.xml", (2, 3)),
    (spdx2_3_dir / "SPDXTagExample-v2.3.spdx", (2, 3)),
    (spdx2_3_dir / "SPDXXMLExample-v2.3.spdx.xml", (2, 3)),
    (spdx2_3_dir / "SPDXYAMLExample-v2.3.spdx.yaml", (2, 3)),
    (spdx3_0_dir / "no_elements_missing.json", (3, 0)),
    (spdx3_0_dir / "has_sbom.json", (3, 0)),
]


def test_detect_spdx_version():
    for file_path, expected_version in detect_version_test:
        try:
            version = get_spdx_version(str(file_path))
            assert (
                version == expected_version
            ), f"Expected {expected_version}, got {version} for {file_path}"
        except BeartypeCallHintParamViolation:
            pytest.xfail(
                "Beartype type violation (assigning None) due to missing field in SPDX document"
            )


detect_sbom_spec_test: List[Tuple[Path, str]] = [
    (spdx2_2_dir / "SPDXJsonExample.json", "spdx2"),
    (spdx2_2_dir / "SPDXXmlExample.xml", "spdx2"),
    (spdx2_2_dir / "SPDXYamlExample.yaml", "spdx2"),
    (spdx2_3_dir / "SPDXJSONExample-v2.3.spdx.json", "spdx2"),
    (spdx2_3_dir / "SPDXRdfExample-v2.3.spdx.rdf.xml", "spdx2"),
    (spdx2_3_dir / "SPDXTagExample-v2.3.spdx", "spdx2"),
    (spdx2_3_dir / "SPDXXMLExample-v2.3.spdx.xml", "spdx2"),
    (spdx2_3_dir / "SPDXYAMLExample-v2.3.spdx.yaml", "spdx2"),
    (spdx3_0_dir / "no_elements_missing.json", "spdx3"),
    (spdx3_0_dir / "has_sbom.json", "spdx3"),
]


def test_detect_sbom_spec():
    for file_path, expected_sbom_spec in detect_sbom_spec_test:
        try:
            sbom_spec = get_sbom_spec(str(file_path), sbom_spec=expected_sbom_spec)
            assert (
                sbom_spec == expected_sbom_spec
            ), f"Expected {expected_sbom_spec}, got {sbom_spec} for {file_path}"
        except BeartypeCallHintParamViolation:
            pytest.xfail(
                "Beartype type violation (assigning None) due to missing field in SPDX document"
            )
