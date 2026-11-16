# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for graph connectivity analysis"""

# pylint: disable=missing-function-docstring,import-error,consider-using-from-import

import functools
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
    SPDX2_RELATIONSHIP_TRAVERSAL,
    SPDX2_TO_SPDX3_RELATIONSHIP_TYPES,
    SPDX3_RELATIONSHIP_TRAVERSAL,
    VALID_SPDX2_COMPOSITION_RELATIONSHIPS,
    VALID_SPDX3_COMPOSITION_RELATIONSHIPS,
    TraversalDirection,
)
from ntia_conformance_checker.graph_utils import (
    analyze_graph,
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
    "rel_name",
    sorted(
        name
        for name, direction in SPDX2_RELATIONSHIP_TRAVERSAL.items()
        if direction is TraversalDirection.REVERSE
    ),
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


@pytest.mark.parametrize(
    "rel_name",
    sorted(
        name
        for name, direction in SPDX2_RELATIONSHIP_TRAVERSAL.items()
        if direction is TraversalDirection.FORWARD
    ),
)
def test_spdx2_forward_relationship_connects_child(rel_name: str) -> None:
    """A forward relationship "Parent X Child" links Parent to Child."""
    doc = _make_spdx2_doc(
        ["SPDXRef-Parent", "SPDXRef-Child"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-Parent"),
            ("SPDXRef-Parent", RelationshipType[rel_name], "SPDXRef-Child"),
        ],
    )
    reachable, floating, unknown_edges, has_unknown_pointers = (
        analyze_graph_connectivity("spdx2", doc)
    )
    assert reachable == {"SPDXRef-Parent", "SPDXRef-Child"}
    assert floating == set()
    assert not unknown_edges
    assert has_unknown_pointers is False


@pytest.mark.parametrize(
    ("relationship", "floating_id"),
    [
        # Product BUILD_TOOL_OF Tool: written the wrong way round
        (
            ("SPDXRef-Root", RelationshipType.BUILD_TOOL_OF, "SPDXRef-Other"),
            "SPDXRef-Other",
        ),
        # Source GENERATED_FROM Product: written the wrong way round
        (
            ("SPDXRef-Other", RelationshipType.GENERATED_FROM, "SPDXRef-Root"),
            "SPDXRef-Other",
        ),
        # Product GENERATES Source: written the wrong way round
        (
            ("SPDXRef-Root", RelationshipType.GENERATES, "SPDXRef-Other"),
            "SPDXRef-Other",
        ),
        # OTHER has no direction and is not followed
        (
            ("SPDXRef-Root", RelationshipType.OTHER, "SPDXRef-Other"),
            "SPDXRef-Other",
        ),
    ],
    ids=["build-tool-of", "generated-from", "generates", "other"],
)
def test_spdx2_relationship_is_followed_only_in_its_direction(
    relationship: tuple[str, RelationshipType, str], floating_id: str
) -> None:
    """A relationship links parent to child only, never child to parent."""
    doc = _make_spdx2_doc(
        ["SPDXRef-Root", "SPDXRef-Other"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-Root"),
            relationship,
        ],
    )
    reachable, floating, _, _ = analyze_graph_connectivity("spdx2", doc)
    assert reachable == {"SPDXRef-Root"}
    assert floating == {floating_id}


@pytest.mark.parametrize(
    ("relationship", "expected_unknown_edges"),
    [
        (
            ("SPDXRef-A", RelationshipType.BUILD_DEPENDENCY_OF, "SPDXRef-Missing"),
            {"SPDXRef-A": ["SPDXRef-Missing"]},
        ),
        (
            ("SPDXRef-Missing", RelationshipType.DEPENDENCY_OF, "SPDXRef-A"),
            {"SPDXRef-Missing": ["SPDXRef-A"]},
        ),
        (
            ("SPDXRef-A", RelationshipType.DEPENDS_ON, "SPDXRef-Missing"),
            {"SPDXRef-A": ["SPDXRef-Missing"]},
        ),
    ],
    ids=["reverse-missing-parent", "reverse-missing-child", "forward-missing"],
)
def test_spdx2_relationship_to_missing_element(
    relationship: tuple[str, RelationshipType, str],
    expected_unknown_edges: dict[str, list[str]],
) -> None:
    """A composition relationship with a missing end is an unknown pointer."""
    doc = _make_spdx2_doc(
        ["SPDXRef-A"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-A"),
            relationship,
        ],
    )
    _, _, unknown_edges, has_unknown_pointers = analyze_graph_connectivity("spdx2", doc)
    assert unknown_edges == expected_unknown_edges
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
    target: str, unknown: bool
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


def test_spdx2_reverse_relationship_file() -> None:
    """Packages linked only by reverse relationships are not floating (#481)."""
    test_file = os.path.join(
        os.path.dirname(__file__),
        "data",
        "graph_connectivity",
        "reverse_relationship",
        "reverse_relationship_spdx2.json",
    )
    sbom = sbom_checker.SbomChecker(test_file, sbom_spec="spdx2")
    assert sbom.floating_component_ids == set()
    assert sbom.reachable_component_ids == {
        "SPDXRef-Package-A",
        "SPDXRef-Package-Tool",
        "SPDXRef-Package-Lib",
        "SPDXRef-Package-Sub",
        "SPDXRef-Package-Test",
    }
    assert sbom.has_unknown_pointers is False
    assert sbom.compliant is True


def test_spdx2_external_document_ref_file() -> None:
    """A relationship to an external document element is not missing (#482)."""
    test_file = os.path.join(
        os.path.dirname(__file__),
        "data",
        "graph_connectivity",
        "external_document_ref",
        "external_document_ref_spdx2.json",
    )
    sbom = sbom_checker.SbomChecker(test_file, sbom_spec="spdx2")
    assert not sbom.validation_messages
    assert sbom.has_unknown_pointers is False
    assert not sbom.unknown_pointer_edges
    assert sbom.reachable_component_ids == {"SPDXRef-Package-A"}
    assert sbom.compliant is True


def test_annex_a1_table_covers_every_spdx2_relationship_type() -> None:
    """The Annex A.1 table has one row for each SPDX 2 relationship type."""
    assert set(SPDX2_TO_SPDX3_RELATIONSHIP_TYPES) == {
        rel_type.name for rel_type in RelationshipType
    }


def test_annex_a1_table_and_traversal_use_spdx3_relationship_types() -> None:
    """Every SPDX 3 type in the table and in the traversal exists in SPDX 3."""
    spdx3_types = {
        spdx3_type for spdx3_type, _ in SPDX2_TO_SPDX3_RELATIONSHIP_TYPES.values()
    }
    spdx3_types |= set(SPDX3_RELATIONSHIP_TRAVERSAL)
    for spdx3_type in spdx3_types:
        assert isinstance(getattr(spdx3.RelationshipType, spdx3_type, None), str)


@pytest.mark.parametrize(
    ("spdx2_type", "direction"),
    [
        # From the Annex A.1 table
        ("CONTAINS", TraversalDirection.FORWARD),
        ("CONTAINED_BY", TraversalDirection.REVERSE),
        ("BUILD_TOOL_OF", TraversalDirection.REVERSE),
        ("DEV_TOOL_OF", TraversalDirection.REVERSE),
        ("TEST_TOOL_OF", TraversalDirection.REVERSE),
        ("GENERATED_FROM", TraversalDirection.FORWARD),
        ("GENERATES", TraversalDirection.REVERSE),
        # Overrides
        ("DESCRIBES", TraversalDirection.FORWARD),
        ("DYNAMIC_LINK", TraversalDirection.FORWARD),
        ("DESCRIBED_BY", TraversalDirection.REVERSE),
        # Not followed
        ("FILE_MODIFIED", None),
        ("OTHER", None),
    ],
)
def test_spdx2_traversal_is_derived_from_spdx3(
    spdx2_type: str, direction: TraversalDirection | None
) -> None:
    """SPDX 2 directions follow the SPDX 3 translation, or an override."""
    assert SPDX2_RELATIONSHIP_TRAVERSAL.get(spdx2_type) is direction


_SPDX3_BASE_SBOM = Path(__file__).parent / "data" / "spdx3" / "no_elements_missing.json"


def _spdx3_element_id(name: str) -> str:
    """
    Return the SPDX ID for a test element name in ``_SPDX3_BASE_SBOM``.

    "ROOT" is the root package, "DOC" is the SpdxDocument and any other name
    is ``https://example.com/<name>``.
    """
    return _spdx3_special_ids().get(name, f"https://example.com/{name}")


@functools.cache
def _spdx3_special_ids() -> dict[str, str]:
    """Return the SPDX IDs of the root package and the SpdxDocument of the base SBOM."""
    graph = json.loads(_SPDX3_BASE_SBOM.read_text(encoding="utf-8"))["@graph"]
    types = {"ROOT": "dataset_DatasetPackage", "DOC": "SpdxDocument"}
    return {
        name: str(next(e for e in graph if e["type"] == type_name)["spdxId"])
        for name, type_name in types.items()
    }


def _spdx3_checker_with(
    tmp_path: Path, relationships: list[tuple[str, str, str]]
) -> sbom_checker.SbomChecker:
    """
    Check an SPDX 3 SBOM whose root package has extra packages and relationships.

    Each relationship is (from, relationshipType, to), where "ROOT" is the
    root package, "DOC" is the SpdxDocument and any other name is an extra
    package, or a missing one if it starts with "missing".
    """
    doc = json.loads(_SPDX3_BASE_SBOM.read_text(encoding="utf-8"))
    element_id = _spdx3_element_id

    names = {n for rel in relationships for n in (rel[0], rel[2])}
    for name in sorted(names - {"ROOT", "DOC"}):
        if not name.startswith("missing"):
            doc["@graph"].append(
                {
                    "type": "software_Package",
                    "spdxId": element_id(name),
                    "creationInfo": "_:creationinfo",
                    "name": name,
                }
            )
    for i, (from_name, rel_type, to_name) in enumerate(relationships):
        doc["@graph"].append(
            {
                "type": "Relationship",
                "spdxId": f"https://example.com/rel-{i}",
                "creationInfo": "_:creationinfo",
                "from": element_id(from_name),
                "relationshipType": rel_type,
                "to": [element_id(to_name)],
            }
        )
    path = tmp_path / "sbom.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    checker: sbom_checker.SbomChecker = sbom_checker.SbomChecker(
        str(path), sbom_spec="spdx3"
    )
    return checker


@pytest.mark.parametrize(
    ("relationship", "connected"),
    [
        (("ROOT", "usesTool", "tool"), True),
        (("tool", "usesTool", "ROOT"), False),
        (("source", "generates", "ROOT"), True),
        (("ROOT", "generates", "product"), False),
    ],
    ids=["uses-tool", "uses-tool-reversed", "generates", "generates-reversed"],
)
def test_spdx3_uses_tool_and_generates(
    tmp_path: Path, relationship: tuple[str, str, str], connected: bool
) -> None:
    """usesTool goes from the product to the tool, generates from the product to the source."""
    sbom = _spdx3_checker_with(tmp_path, [relationship])
    other = next(n for n in (relationship[0], relationship[2]) if n != "ROOT")
    other_id = f"https://example.com/{other}"
    assert (other_id in sbom.reachable_component_ids) is connected
    assert (other_id in sbom.floating_component_ids) is not connected
    assert sbom.has_unknown_pointers is False


@pytest.mark.parametrize(
    "relationship",
    [
        ("ROOT", "usesTool", "missing-tool"),
        ("missing-source", "generates", "ROOT"),
        ("source", "generates", "missing-product"),
    ],
    ids=["uses-tool", "generates-missing-from", "generates-missing-to"],
)
def test_spdx3_uses_tool_and_generates_missing_element(
    tmp_path: Path, relationship: tuple[str, str, str]
) -> None:
    """A usesTool or generates relationship with a missing end is reported."""
    sbom = _spdx3_checker_with(tmp_path, [relationship])
    assert sbom.has_unknown_pointers is True


@pytest.mark.parametrize(
    ("relationship", "expected_unknown_edges"),
    [
        (
            ("SPDXRef-Missing", RelationshipType.CONTAINS, "SPDXRef-A"),
            {"SPDXRef-Missing": ["SPDXRef-A"]},
        ),
        (
            ("SPDXRef-Missing", RelationshipType.DESCRIBED_BY, "SPDXRef-DOCUMENT"),
            {"SPDXRef-Missing": ["SPDXRef-DOCUMENT"]},
        ),
        (
            ("SPDXRef-Missing1", RelationshipType.CONTAINS, "SPDXRef-Missing2"),
            {"SPDXRef-Missing1": ["SPDXRef-Missing2"]},
        ),
    ],
    ids=["forward-missing-source", "missing-root", "both-missing"],
)
def test_spdx2_missing_source_or_root(
    caplog: pytest.LogCaptureFixture,
    relationship: tuple[str, RelationshipType, str],
    expected_unknown_edges: dict[str, list[str]],
) -> None:
    """A missing element at either end, or as a root, is reported once."""
    doc = _make_spdx2_doc(
        ["SPDXRef-A"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-A"),
            relationship,
            relationship,  # a duplicate is reported once
        ],
    )
    _, _, unknown_edges, has_unknown_pointers = analyze_graph_connectivity("spdx2", doc)
    assert unknown_edges == expected_unknown_edges
    assert has_unknown_pointers is True
    assert "Traversal bug" not in caplog.text


@pytest.mark.parametrize(
    "relationship",
    [
        ("SPDXRef-A", RelationshipType.DEPENDS_ON, "DocumentRef-other:SPDXRef-B"),
        ("DocumentRef-other:SPDXRef-B", RelationshipType.DEPENDENCY_OF, "SPDXRef-A"),
        ("DocumentRef-other:SPDXRef-B", RelationshipType.CONTAINS, "SPDXRef-A"),
    ],
    ids=["target", "reverse-source", "forward-source"],
)
def test_spdx2_external_element_at_either_end(
    caplog: pytest.LogCaptureFixture, relationship: tuple[str, RelationshipType, str]
) -> None:
    """A declared external element is known at either end, reached or not."""
    doc = _make_spdx2_doc(
        ["SPDXRef-A"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-A"),
            relationship,
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
    ("relationship", "expected_unknown_edges"),
    [
        (
            ("missing-a", "contains", "ROOT"),
            {"missing-a": ["ROOT"]},
        ),
        (
            ("missing-a", "generates", "missing-b"),
            {"missing-a": ["missing-b"]},
        ),
        (
            ("DOC", "describes", "missing-root"),
            {"DOC": ["missing-root"]},
        ),
    ],
    ids=["forward-missing-from", "both-missing", "missing-root"],
)
def test_spdx3_missing_from_or_root(
    tmp_path: Path,
    caplog: pytest.LogCaptureFixture,
    relationship: tuple[str, str, str],
    expected_unknown_edges: dict[str, list[str]],
) -> None:
    """SPDX 3 reports a missing element at either end, or as a root, once."""
    sbom = _spdx3_checker_with(tmp_path, [relationship, relationship])
    element_id = _spdx3_element_id
    assert sbom.unknown_pointer_edges == {
        element_id(k): [element_id(v) for v in vs]
        for k, vs in expected_unknown_edges.items()
    }
    assert "Traversal bug" not in caplog.text


def test_spdx2_document_alias_is_known(caplog: pytest.LogCaptureFixture) -> None:
    """SPDXRef-DOCUMENT is the document even when its ID is different."""
    doc = _make_spdx2_doc(
        ["SPDXRef-A"],
        [("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-A")],
    )
    doc.creation_info.spdx_id = "SPDXRef-DOC"
    reachable, floating, unknown_edges, has_unknown_pointers = (
        analyze_graph_connectivity("spdx2", doc)
    )
    assert reachable == {"SPDXRef-A"}
    assert floating == set()
    assert not unknown_edges
    assert has_unknown_pointers is False
    assert "Traversal bug" not in caplog.text


@pytest.mark.parametrize(
    ("relationship", "unknown"),
    [
        (("imported-a", "dependsOn", "ROOT"), False),
        (("ROOT", "dependsOn", "imported-a"), False),
        (("ROOT", "dependsOn", "missing-b"), True),
    ],
    ids=["imported-from", "imported-to", "not-imported"],
)
def test_spdx3_imported_element_is_known(
    tmp_path: Path, relationship: tuple[str, str, str], unknown: bool
) -> None:
    """An element in an ExternalMap of the SpdxDocument import is not missing."""
    doc = json.loads(_SPDX3_BASE_SBOM.read_text(encoding="utf-8"))
    spdx_doc = next(e for e in doc["@graph"] if e["type"] == "SpdxDocument")
    spdx_doc["import"] = [
        {"type": "ExternalMap", "externalSpdxId": "https://example.com/imported-a"}
    ]
    from_name, rel_type, to_name = relationship
    doc["@graph"].append(
        {
            "type": "Relationship",
            "spdxId": "https://example.com/rel-0",
            "creationInfo": "_:creationinfo",
            "from": _spdx3_element_id(from_name),
            "relationshipType": rel_type,
            "to": [_spdx3_element_id(to_name)],
        }
    )
    path = tmp_path / "sbom.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    sbom = sbom_checker.SbomChecker(str(path), sbom_spec="spdx3")
    assert sbom.has_unknown_pointers is unknown


def test_deprecated_relationship_sets_are_unchanged() -> None:
    """The deprecated sets keep their 6.0.0 values for compatibility."""
    assert VALID_SPDX2_COMPOSITION_RELATIONSHIPS == {
        "DESCRIBES",
        "CONTAINS",
        "DEPENDS_ON",
        "DYNAMIC_LINK",
        "STATIC_LINK",
        "HAS_PREREQUISITE",
    }
    assert "usesTool" not in VALID_SPDX3_COMPOSITION_RELATIONSHIPS
    assert "generates" not in VALID_SPDX3_COMPOSITION_RELATIONSHIPS


@pytest.mark.parametrize(
    ("relationship", "expected_missing"),
    [
        (
            ("SPDXRef-A", RelationshipType.DEPENDS_ON, "SPDXRef-Missing"),
            {"SPDXRef-Missing"},
        ),
        (
            ("SPDXRef-Missing", RelationshipType.DEPENDS_ON, "SPDXRef-A"),
            {"SPDXRef-Missing"},
        ),
        (
            ("SPDXRef-Missing1", RelationshipType.DEPENDS_ON, "SPDXRef-Missing2"),
            {"SPDXRef-Missing1", "SPDXRef-Missing2"},
        ),
    ],
    ids=["target-missing", "source-missing", "both-missing"],
)
def test_analyze_graph_lists_missing_element_ids(
    relationship: tuple[str, RelationshipType, str], expected_missing: set[str]
) -> None:
    """Every missing element is listed, a missing source of a link included."""
    doc = _make_spdx2_doc(
        ["SPDXRef-A"],
        [
            ("SPDXRef-DOCUMENT", RelationshipType.DESCRIBES, "SPDXRef-A"),
            relationship,
        ],
    )
    result = analyze_graph("spdx2", doc)
    assert result.missing_element_ids == expected_missing
    assert result.has_unknown_pointers is True
    assert analyze_graph_connectivity("spdx2", doc) == (
        result.reachable_component_ids,
        result.floating_component_ids,
        result.unknown_pointer_edges,
        True,
    )


def test_missing_source_is_reported_end_to_end(tmp_path: Path) -> None:
    """The checker reports a link with both ends missing as such, in all outputs."""
    src = (
        Path(__file__).parent
        / "data"
        / "graph_connectivity"
        / "reverse_relationship"
        / "reverse_relationship_spdx2.json"
    )
    doc = json.loads(src.read_text(encoding="utf-8"))
    doc["relationships"].append(
        {
            "spdxElementId": "SPDXRef-Ghost1",
            "relationshipType": "DEPENDS_ON",
            "relatedSpdxElement": "SPDXRef-Ghost2",
        }
    )
    path = tmp_path / "sbom.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    sbom = sbom_checker.SbomChecker(str(path), sbom_spec="spdx2")

    assert sbom.missing_element_ids == {"SPDXRef-Ghost1", "SPDXRef-Ghost2"}
    assert sbom.output_json()["graphValidation"]["unknownPointers"][
        "missingElementIds"
    ] == ["SPDXRef-Ghost1", "SPDXRef-Ghost2"]
    assert (
        "Missing element '<b>SPDXRef-Ghost1</b>' links to missing element "
        "'<b>SPDXRef-Ghost2</b>'" in sbom.output_html()
    )


@pytest.mark.parametrize(
    ("file_path", "reachable"),
    [
        (
            Path("reverse_relationship") / "issue481_build_dependency_of.spdx",
            {"SPDXRef-Package-App", "SPDXRef-Package-Tool"},
        ),
        (
            Path("external_document_ref") / "issue482_external_document_ref.spdx",
            {"SPDXRef-Package-App"},
        ),
    ],
    ids=["issue-481", "issue-482"],
)
def test_reported_issue_sboms(
    caplog: pytest.LogCaptureFixture, file_path: Path, reachable: set[str]
) -> None:
    """The tag-value SBOMs from issues #481 and #482 have no graph problems."""
    test_file = Path(__file__).parent / "data" / "graph_connectivity" / file_path
    sbom = sbom_checker.SbomChecker(str(test_file), sbom_spec="spdx2")
    assert not sbom.parsing_errors
    assert sbom.reachable_component_ids == reachable
    assert sbom.floating_component_ids == set()
    assert sbom.has_unknown_pointers is False
    assert not sbom.unknown_pointer_edges
    assert "floating" not in caplog.text
    assert "missing element" not in caplog.text
