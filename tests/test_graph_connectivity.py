# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for graph connectivity analysis"""

# pylint: disable=missing-function-docstring,import-error,consider-using-from-import

import os
from unittest.mock import MagicMock

from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.model.document import Document
from spdx_tools.spdx.model.file import File
from spdx_tools.spdx.model.package import Package
from spdx_tools.spdx.model.relationship import Relationship, RelationshipType
from spdx_tools.spdx.model.snippet import Snippet

import ntia_conformance_checker.sbom_checker as sbom_checker
from ntia_conformance_checker.graph_utils import (
    analyze_graph_connectivity,
    get_reachable_nodes,
)


def test_disconnected_component_spdx3_floating_contains_only_orphan_package() -> None:
    """Test that SPDX 3 non-artifact elements are not marked as floating."""
    test_file = os.path.join(
        os.path.dirname(__file__),
        "data",
        "graph_connectivity",
        "disconnected_component",
        "disconnected_component_spdx3.json",
    )
    sbom = sbom_checker.SbomChecker(test_file, sbom_spec="spdx3")
    assert sbom.floating_component_ids == {
        "https://swinslow.net/spdx-examples/SPDXRef-Package-Orphan"
    }


def test_analyze_graph_connectivity_spdx2_files_and_snippets() -> None:
    """Test that pointing to files and snippets in SPDX 2 does not trigger unknown pointers."""
    doc = MagicMock(spec=Document)
    doc.creation_info = MagicMock()
    doc.creation_info.spdx_id = "SPDXRef-DOCUMENT"

    pkg = MagicMock(spec=Package)
    pkg.spdx_id = "SPDXRef-Package1"
    file_obj = MagicMock(spec=File)
    file_obj.spdx_id = "SPDXRef-File1"
    snippet_obj = MagicMock(spec=Snippet)
    snippet_obj.spdx_id = "SPDXRef-Snippet1"

    doc.packages = [pkg]
    doc.files = [file_obj]
    doc.snippets = [snippet_obj]

    # DOCUMENT describes Package1, Package1 contains File1, File1 contains Snippet1
    rel_describes = Relationship(
        "SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-Package1"
    )
    rel_contains_file = Relationship(
        "SPDXRef-Package1", RelationshipType.CONTAINS, "SPDXRef-File1"
    )
    rel_contains_snippet = Relationship(
        "SPDXRef-File1", RelationshipType.CONTAINS, "SPDXRef-Snippet1"
    )
    doc.relationships = [rel_describes, rel_contains_file, rel_contains_snippet]
    reachable_nodes, _ = get_reachable_nodes("spdx2", doc)
    assert reachable_nodes == {"SPDXRef-Package1", "SPDXRef-File1", "SPDXRef-Snippet1"}

    reachable_components, floating, unknown_edges, has_unknown_pointers = (
        analyze_graph_connectivity("spdx2", doc)
    )

    assert reachable_components == {"SPDXRef-Package1"}
    assert floating == set()
    assert not unknown_edges
    assert has_unknown_pointers is False


def test_get_reachable_nodes_spdx3_missing_doc() -> None:
    """Test get_reachable_nodes returns empty sets when spdx3_doc is missing."""
    doc_set = spdx3.SHACLObjectSet()
    reachable_nodes, connection_map = get_reachable_nodes(
        "spdx3", doc_set, spdx3_doc=None
    )
    assert reachable_nodes == set()
    assert not connection_map

    reachable_components, floating, unknown_edges, has_unknown_pointers = (
        analyze_graph_connectivity("spdx3", doc_set, spdx3_doc=None)
    )
    assert reachable_components == set()
    assert floating == set()
    assert not unknown_edges
    assert has_unknown_pointers is False


def test_build_spdx2_graph_described_by() -> None:
    """Test SPDX 2 root identification when DESCRIBED_BY relationship is used."""
    doc = MagicMock(spec=Document)
    doc.creation_info = MagicMock()
    doc.creation_info.spdx_id = "SPDXRef-DOCUMENT"

    pkg = MagicMock(spec=Package)
    pkg.spdx_id = "SPDXRef-Package1"
    doc.packages = [pkg]
    doc.files = []
    doc.snippets = []

    rel = Relationship(
        "SPDXRef-Package1", RelationshipType.DESCRIBED_BY, "SPDXRef-DOCUMENT"
    )
    doc.relationships = [rel]

    reachable, floating, unknown_edges, has_unknown_pointers = (
        analyze_graph_connectivity("spdx2", doc)
    )
    assert reachable == {"SPDXRef-Package1"}
    assert floating == set()
    assert not unknown_edges
    assert has_unknown_pointers is False
