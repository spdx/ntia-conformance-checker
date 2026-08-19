# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for SbomChecker.get_components_without_identifiers"""

# pylint: disable=missing-function-docstring,import-error,consider-using-from-import

from datetime import datetime, timezone
from unittest.mock import MagicMock

from spdx_python_model.bindings import v3_0_1 as spdx3

import ntia_conformance_checker.sbom_checker as sbom_checker


def test_get_components_without_identifiers_spdx3() -> None:
    """Test get_components_without_identifiers with SPDX 3 object sets."""
    creation_info = spdx3.CreationInfo(
        _id="http://example.com/spdx3/creation-info",
        specVersion="3.0.1",
        created=datetime.now(timezone.utc),
        createdBy=["http://example.com/spdx3/actor1"],
        createdUsing=["http://example.com/spdx3/tool1"],
    )

    doc_set = spdx3.SHACLObjectSet()
    pkg_valid = spdx3.software_Package(
        _id="http://example.com/spdx3/pkg-valid",
        creationInfo=creation_info,
        name="pkg-valid",
    )
    doc_set.add(pkg_valid)

    # Non-package element that should not be evaluated as a component
    agent = spdx3.Agent(
        _id="http://example.com/spdx3/agent1",
        creationInfo=creation_info,
        name="agent1",
    )
    doc_set.add(agent)

    checker = sbom_checker.SbomChecker("", validate=False, sbom_spec="spdx3")
    checker.doc = doc_set
    checker.reachable_component_ids = {
        "http://example.com/spdx3/pkg-valid",
        "http://example.com/spdx3/agent1",
    }

    # All packages have valid identifiers
    assert checker.get_components_without_identifiers() == []

    # Package with empty identifier
    pkg_no_id = MagicMock(spec=spdx3.software_Package)
    pkg_no_id.name = "pkg-no-id"
    pkg_no_id.spdxId = ""
    doc_set.add(pkg_no_id)
    # reachable_component_ids does NOT contain empty id
    checker.reachable_component_ids = {"http://example.com/spdx3/pkg-valid"}

    assert checker.get_components_without_identifiers() == [("pkg-no-id", "")]


def test_get_components_without_identifiers_spdx2() -> None:
    """Test get_components_without_identifiers with SPDX 2 documents."""
    checker = sbom_checker.SbomChecker("", validate=False, sbom_spec="spdx2")
    doc = MagicMock()
    pkg1 = MagicMock()
    pkg1.name = "pkg1"
    pkg1.spdx_id = "SPDXRef-Package1"

    pkg_no_id = MagicMock()
    pkg_no_id.name = "pkg-no-id"
    pkg_no_id.spdx_id = None

    pkg_empty_id = MagicMock()
    pkg_empty_id.name = "pkg-empty-id"
    pkg_empty_id.spdx_id = "   "

    doc.packages = [pkg1, pkg_no_id, pkg_empty_id]
    checker.doc = doc
    checker.reachable_component_ids = {"SPDXRef-Package1"}

    assert checker.get_components_without_identifiers() == [
        ("pkg-no-id", ""),
        ("pkg-empty-id", "   "),
    ]
