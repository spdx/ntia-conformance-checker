# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for get_all_packages and get_total_number_components"""

# pylint: disable=missing-function-docstring,import-error,consider-using-from-import

import os
from datetime import datetime, timezone
from pathlib import Path

from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.model.document import (
    CreationInfo as SPDX2CreationInfo,
)
from spdx_tools.spdx.model.document import (
    Document,
)

import ntia_conformance_checker.sbom_checker as sbom_checker
from ntia_conformance_checker.adapters import Spdx2Adapter, Spdx3Adapter
from ntia_conformance_checker.ntia_checker import NTIAChecker
from ntia_conformance_checker.spdx3_utils import get_all_packages

SPDX3_RELATIONSHIP_TYPE_BASE = "https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType"

dirname = os.path.join(os.path.dirname(__file__), "data", "no_elements_missing")
test_files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


def _create_test_spdx3_creation_info(
    base_iri: str = "http://example.com/spdx3",
) -> spdx3.CreationInfo:
    """Create a minimal valid SPDX 3 CreationInfo instance for testing."""
    return spdx3.CreationInfo(
        _id=f"{base_iri}/creation-info",
        specVersion="3.0.1",
        created=datetime.now(timezone.utc),
        createdBy=[f"{base_iri}/actor1"],
        createdUsing=[f"{base_iri}/tool1"],
    )


def test_get_all_packages_empty() -> None:
    """Test get_all_packages returns empty set for empty SHACLObjectSet."""
    object_set = spdx3.SHACLObjectSet()
    packages = get_all_packages(object_set)
    assert packages == set()
    assert len(packages) == 0


def test_get_all_packages_non_packages_only() -> None:
    """Test get_all_packages returns empty set for SHACLObjectSet that
    contains only non-package elements."""
    object_set = spdx3.SHACLObjectSet()
    creation_info = _create_test_spdx3_creation_info()

    doc = spdx3.SpdxDocument(
        _id="http://example.com/spdx3/doc",
        creationInfo=creation_info,
        name="test-doc",
    )
    sbom = spdx3.software_Sbom(
        _id="http://example.com/spdx3/sbom",
        creationInfo=creation_info,
        name="test-sbom",
    )
    file = spdx3.software_File(
        _id="http://example.com/spdx3/file",
        creationInfo=creation_info,
        name="test-file",
    )
    agent = spdx3.Agent(
        _id="http://example.com/spdx3/agent",
        creationInfo=creation_info,
        name="test-agent",
    )
    rel = spdx3.Relationship(
        _id="http://example.com/spdx3/rel",
        creationInfo=creation_info,
        relationshipType=f"{SPDX3_RELATIONSHIP_TYPE_BASE}/contains",
        from_="http://example.com/spdx3/doc",
        to=["http://example.com/spdx3/file"],
    )

    object_set.add(doc)
    object_set.add(sbom)
    object_set.add(file)
    object_set.add(agent)
    object_set.add(rel)

    packages = get_all_packages(object_set)
    assert packages == set()


def test_get_all_packages_with_package_and_subclasses() -> None:
    """Test get_all_packages retrieves Package, AIPackage, and DatasetPackage."""
    object_set = spdx3.SHACLObjectSet()
    creation_info = _create_test_spdx3_creation_info()

    pkg = spdx3.software_Package(
        _id="http://example.com/spdx3/pkg1",
        creationInfo=creation_info,
        name="regular-package",
    )
    ai_pkg = spdx3.ai_AIPackage(
        _id="http://example.com/spdx3/ai-pkg1",
        creationInfo=creation_info,
        name="ai-package",
    )
    data_pkg = spdx3.dataset_DatasetPackage(
        _id="http://example.com/spdx3/data-pkg1",
        creationInfo=creation_info,
        name="dataset-package",
    )
    file = spdx3.software_File(
        _id="http://example.com/spdx3/file1",
        creationInfo=creation_info,
        name="file1",
    )

    object_set.add(pkg)
    object_set.add(ai_pkg)
    object_set.add(data_pkg)
    object_set.add(file)

    packages = get_all_packages(object_set)
    assert len(packages) == 3
    package_names = {getattr(p, "name") for p in packages}
    assert package_names == {"regular-package", "ai-package", "dataset-package"}


def test_get_total_number_components_none_or_unknown_spec() -> None:
    """Test get_total_number_components when doc is None or unknown spec."""
    checker = sbom_checker.SbomChecker(test_files[0])
    checker.doc = None
    checker.adapter = None
    assert checker.get_total_number_components() == 0

    checker.doc = spdx3.SHACLObjectSet()
    checker.sbom_spec = "unknown_spec"
    assert checker.get_total_number_components() == 0


def test_get_total_number_components_spdx2() -> None:
    """Test get_total_number_components returns 0 for empty SPDX 2 documents."""
    filepath = os.path.join(
        os.path.dirname(__file__), "data", "other_tests", "SPDXSBOMExample.spdx.yml"
    )
    sbom = sbom_checker.SbomChecker(filepath)
    assert sbom.get_total_number_components() == 3

    creation_info = SPDX2CreationInfo(
        spdx_version="SPDX-2.3",
        spdx_id="SPDXRef-DOCUMENT",
        name="empty-doc",
        document_namespace="https://example.com/spdx/doc",
        created=datetime.now(timezone.utc),
        creators=[],
    )
    doc_empty = Document(creation_info=creation_info, packages=[])
    checker = sbom_checker.SbomChecker(filepath)
    checker.adapter = Spdx2Adapter(doc_empty)
    assert checker.get_total_number_components() == 0


def test_get_total_number_components_spdx3_packages_and_subclasses() -> None:
    """Test get_total_number_components returns 3
    for SPDX 3 with Package, AIPackage, DatasetPackage."""
    object_set = spdx3.SHACLObjectSet()
    creation_info = _create_test_spdx3_creation_info()

    doc = spdx3.SpdxDocument(
        _id="http://example.com/spdx3/doc",
        creationInfo=creation_info,
        name="test-spdx3-doc",
    )
    pkg = spdx3.software_Package(
        _id="http://example.com/spdx3/pkg",
        creationInfo=creation_info,
        name="pkg",
    )
    ai_pkg = spdx3.ai_AIPackage(
        _id="http://example.com/spdx3/aipkg",
        creationInfo=creation_info,
        name="aipkg",
    )
    dataset_pkg = spdx3.dataset_DatasetPackage(
        _id="http://example.com/spdx3/datasetpkg",
        creationInfo=creation_info,
        name="datasetpkg",
    )
    file = spdx3.software_File(
        _id="http://example.com/spdx3/file",
        creationInfo=creation_info,
        name="file",
    )

    object_set.add(doc)
    object_set.add(pkg)
    object_set.add(ai_pkg)
    object_set.add(dataset_pkg)
    object_set.add(file)

    test_file = Path(__file__).parent / "data" / "spdx3" / "has_sbom.json"
    checker = sbom_checker.SbomChecker(str(test_file), sbom_spec="spdx3")
    checker.adapter = Spdx3Adapter(object_set, doc)
    assert checker.get_total_number_components() == 3


def test_get_total_number_components_spdx3_files() -> None:
    """Test get_total_number_components with real SPDX 3 test files."""
    spdx3_files_expected = [
        ("has_sbom.json", 4),
        ("has_no_sbom.json", 1),
        ("no_elements_missing.json", 1),
        ("missing_supplier_name.json", 1),
        ("missing_version.json", 1),
        ("package_dependency_relationship.json", 2),
    ]

    for filename, expected_count in spdx3_files_expected:
        test_file = Path(__file__).parent / "data" / "spdx3" / filename
        sbom = sbom_checker.SbomChecker(str(test_file), sbom_spec="spdx3")
        assert sbom.get_total_number_components() == expected_count, (
            f"Expected {expected_count} components in {filename}, "
            f"got {sbom.get_total_number_components()}"
        )


def test_spdx3_missing_spdxdocument_node_still_initializes_adapter() -> None:
    """
    Test that an SPDX 3 document missing the SpdxDocument node
    still initializes the adapter and evaluates components,
    while correctly logging a validation error.
    """
    filepath = os.path.join(
        os.path.dirname(__file__), "data", "spdx3", "missing_spdxdocument_node.json"
    )

    checker = NTIAChecker(filepath, sbom_spec="spdx3")

    assert checker.adapter is not None
    assert checker.get_total_number_components() == 1

    validation_texts = [msg.validation_message for msg in checker.validation_messages]
    assert any("No SpdxDocument object found" in msg for msg in validation_texts)
