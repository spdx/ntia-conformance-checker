# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for graph connectivity analysis"""

# pylint: disable=missing-function-docstring,import-error,consider-using-from-import

import json
import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.model.checksum import Checksum, ChecksumAlgorithm
from spdx_tools.spdx.model.document import Document
from spdx_tools.spdx.model.external_document_ref import ExternalDocumentRef
from spdx_tools.spdx.model.file import File
from spdx_tools.spdx.model.package import Package
from spdx_tools.spdx.model.relationship import Relationship, RelationshipType
from spdx_tools.spdx.model.snippet import Snippet

import ntia_conformance_checker.sbom_checker as sbom_checker
from ntia_conformance_checker.constants import (
    VALID_SPDX2_REVERSE_COMPOSITION_RELATIONSHIPS,
)
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
    doc.files = list[File]()
    doc.snippets = list[Snippet]()

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


@pytest.mark.parametrize(
    ("target", "unknown"),
    [
        ("NoneElement", False),  # a dependency list that is complete and empty
        ("NoAssertionElement", False),
        ("https://spdx.org/rdf/3.0.1/terms/ExpandedLicensing/NoneLicense", False),
        ("SpdxOrganization", False),
        ("https://example.com/not-in-the-document", True),
    ],
    ids=["none", "noassertion", "none-license", "spdx-org", "missing"],
)
def test_spdx3_individuals_are_not_unknown_pointers(
    tmp_path: Path, target: str, unknown: bool
) -> None:
    """A relationship to an SPDX individual points to a known element."""
    src = Path(__file__).parent / "data" / "spdx3" / "no_elements_missing.json"
    doc = json.loads(src.read_text(encoding="utf-8"))
    package = next(e for e in doc["@graph"] if e["type"] == "dataset_DatasetPackage")
    doc["@graph"].append(
        {
            "type": "LifecycleScopedRelationship",
            "spdxId": "https://example.com/rel-none",
            "creationInfo": "_:creationinfo",
            "from": package["spdxId"],
            "relationshipType": "dependsOn",
            "to": [target],
            "completeness": "complete",
        }
    )
    path = tmp_path / "sbom.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    sbom = sbom_checker.SbomChecker(str(path), sbom_spec="spdx3")
    assert sbom.has_unknown_pointers is unknown


def _make_spdx2_doc(
    package_ids: list[str],
    relationships: list[tuple[str, RelationshipType, str]],
    external_doc_ref_ids: list[str] | None = None,
) -> MagicMock:
    """Build a mock SPDX 2 document with packages and relationships."""
    doc = MagicMock(spec=Document)
    doc.creation_info = MagicMock()
    doc.creation_info.spdx_id = "SPDXRef-DOCUMENT"
    doc.creation_info.external_document_refs = [
        ExternalDocumentRef(
            ref_id,
            f"https://example.com/spdxdocs/{ref_id}",
            Checksum(
                ChecksumAlgorithm.SHA1, "d6a770ba38583ed4bb4525bd96e50461655d2759"
            ),
        )
        for ref_id in external_doc_ref_ids or []
    ]
    packages = []
    for package_id in package_ids:
        pkg = MagicMock(spec=Package)
        pkg.spdx_id = package_id
        packages.append(pkg)
    doc.packages = packages
    doc.files = list[File]()
    doc.snippets = list[Snippet]()
    doc.relationships = [
        Relationship(source, rel_type, target)
        for source, rel_type, target in relationships
    ]
    return doc


@pytest.mark.parametrize(
    "rel_name", sorted(VALID_SPDX2_REVERSE_COMPOSITION_RELATIONSHIPS)
)
def test_spdx2_reverse_relationship_connects_child(rel_name: str) -> None:
    """A reverse relationship "Child X_OF Parent" links Parent to Child."""
    doc = _make_spdx2_doc(
        ["SPDXRef-Parent", "SPDXRef-Child"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-Parent"),
            ("SPDXRef-Child", RelationshipType[rel_name], "SPDXRef-Parent"),
        ],
    )
    reachable, floating, unknown_edges, has_unknown_pointers = (
        analyze_graph_connectivity("spdx2", doc)
    )
    assert reachable == {"SPDXRef-Parent", "SPDXRef-Child"}
    assert floating == set()
    assert not unknown_edges
    assert has_unknown_pointers is False


def test_spdx2_reverse_relationship_is_followed_only_in_its_direction() -> None:
    """A reverse relationship written the wrong way round connects nothing."""
    doc = _make_spdx2_doc(
        ["SPDXRef-Root", "SPDXRef-Other"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-Root"),
            ("SPDXRef-Root", RelationshipType.DEPENDENCY_OF, "SPDXRef-Other"),
        ],
    )
    reachable, floating, _, _ = analyze_graph_connectivity("spdx2", doc)
    assert reachable == {"SPDXRef-Root"}
    assert floating == {"SPDXRef-Other"}


def test_spdx2_reverse_relationship_to_missing_child() -> None:
    """A reverse relationship from a missing child is an unknown pointer."""
    doc = _make_spdx2_doc(
        ["SPDXRef-A"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-A"),
            ("SPDXRef-Missing", RelationshipType.DEPENDENCY_OF, "SPDXRef-A"),
        ],
    )
    _, _, unknown_edges, has_unknown_pointers = analyze_graph_connectivity("spdx2", doc)
    assert unknown_edges == {"SPDXRef-A": ["SPDXRef-Missing"]}
    assert has_unknown_pointers is True


@pytest.mark.parametrize(
    ("target", "unknown"),
    [
        ("DocumentRef-other:SPDXRef-Package-B", False),
        ("DocumentRef-other:SPDXRef-DOCUMENT", False),
        ("DocumentRef-undeclared:SPDXRef-Package-B", True),
        ("DocumentRef-other", True),  # not ["DocumentRef-"[idstring]":"]SPDXID
        ("DocumentRef-other:", True),
        ("DocumentRef-other:garbage", True),  # not "SPDXRef-"[idstring]
        ("DocumentRef-other:SPDXRef-B:extra", True),
    ],
    ids=[
        "declared-element",
        "declared-document",
        "undeclared",
        "bare",
        "empty",
        "not-spdxid",
        "extra-colon",
    ],
)
def test_spdx2_external_document_ref_elements_are_known(
    caplog: pytest.LogCaptureFixture, target: str, unknown: bool
) -> None:
    """An element in a declared external document is not an unknown pointer."""
    doc = _make_spdx2_doc(
        ["SPDXRef-A"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-A"),
            ("SPDXRef-A", RelationshipType.DEPENDS_ON, target),
        ],
        external_doc_ref_ids=["DocumentRef-other"],
    )
    reachable, floating, unknown_edges, has_unknown_pointers = (
        analyze_graph_connectivity("spdx2", doc)
    )
    assert reachable == {"SPDXRef-A"}
    assert floating == set()
    assert has_unknown_pointers is unknown
    assert unknown_edges == ({"SPDXRef-A": [target]} if unknown else {})
    assert "Traversal bug" not in caplog.text


def test_spdx2_external_element_as_reverse_source(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """A declared external element is known as the child of a reverse relationship."""
    doc = _make_spdx2_doc(
        ["SPDXRef-A"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-A"),
            (
                "DocumentRef-other:SPDXRef-B",
                RelationshipType.DEPENDENCY_OF,
                "SPDXRef-A",
            ),
        ],
        external_doc_ref_ids=["DocumentRef-other"],
    )
    _, floating, unknown_edges, has_unknown_pointers = analyze_graph_connectivity(
        "spdx2", doc
    )
    assert floating == set()
    assert not unknown_edges
    assert has_unknown_pointers is False
    assert "Traversal bug" not in caplog.text


@pytest.mark.parametrize(
    ("relationship_to", "unknown"),
    [
        ("https://example.com/imported-a", False),
        ("https://example.com/missing-b", True),
    ],
    ids=["imported", "not-imported"],
)
def test_spdx3_imported_element_is_known(
    tmp_path: Path, relationship_to: str, unknown: bool
) -> None:
    """An element in an ExternalMap of the SpdxDocument import is not missing."""
    src = Path(__file__).parent / "data" / "spdx3" / "no_elements_missing.json"
    doc = json.loads(src.read_text(encoding="utf-8"))
    spdx_doc = next(e for e in doc["@graph"] if e["type"] == "SpdxDocument")
    spdx_doc["import"] = [
        {"type": "ExternalMap", "externalSpdxId": "https://example.com/imported-a"}
    ]
    package = next(e for e in doc["@graph"] if e["type"] == "dataset_DatasetPackage")
    doc["@graph"].append(
        {
            "type": "Relationship",
            "spdxId": "https://example.com/rel-0",
            "creationInfo": "_:creationinfo",
            "from": package["spdxId"],
            "relationshipType": "dependsOn",
            "to": [relationship_to],
        }
    )
    path = tmp_path / "sbom.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    sbom = sbom_checker.SbomChecker(str(path), sbom_spec="spdx3")
    assert sbom.has_unknown_pointers is unknown


@pytest.mark.parametrize(
    ("file_path", "reachable"),
    [
        (
            Path("reverse_relationship") / "reverse_relationship_spdx2.json",
            {
                "SPDXRef-Package-A",
                "SPDXRef-Package-Tool",
                "SPDXRef-Package-Lib",
                "SPDXRef-Package-Sub",
                "SPDXRef-Package-Test",
            },
        ),
        (
            Path("reverse_relationship") / "issue481_build_dependency_of.spdx",
            {"SPDXRef-Package-App", "SPDXRef-Package-Tool"},
        ),
        (
            Path("external_document_ref") / "external_document_ref_spdx2.json",
            {"SPDXRef-Package-A"},
        ),
        (
            Path("external_document_ref") / "issue482_external_document_ref.spdx",
            {"SPDXRef-Package-App"},
        ),
    ],
    ids=["reverse", "issue-481", "external-document-ref", "issue-482"],
)
def test_spdx2_reverse_and_external_ref_files(
    caplog: pytest.LogCaptureFixture, file_path: Path, reachable: set[str]
) -> None:
    """The test SBOMs and the SBOMs from issues #481 and #482 have no graph problems."""
    test_file = Path(__file__).parent / "data" / "graph_connectivity" / file_path
    sbom = sbom_checker.SbomChecker(str(test_file), sbom_spec="spdx2")
    assert not sbom.parsing_errors
    assert not sbom.validation_messages
    assert sbom.reachable_component_ids == reachable
    assert sbom.floating_component_ids == set()
    assert sbom.has_unknown_pointers is False
    assert not sbom.unknown_pointer_edges
    assert sbom.compliant is True
    assert "floating" not in caplog.text
    assert "missing element" not in caplog.text
