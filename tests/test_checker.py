"""Tests using pytest framework."""

# pylint: disable=missing-function-docstring,import-error,consider-using-from-import

import os

import pytest

import ntia_conformance_checker.sbom_checker as sbom_checker

dirname = os.path.join(os.path.dirname(__file__), "data", "no_elements_missing")
test_files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", test_files)
def test_sbomchecker_no_errors(test_file):
    sbom = sbom_checker.SbomChecker(test_file)
    assert sbom.file == test_file
    assert sbom.doc_version
    assert sbom.doc_author
    assert sbom.doc_timestamp
    assert sbom.dependency_relationships
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    assert not sbom.components_without_suppliers
    assert not sbom.components_without_identifiers
    assert sbom.ntia_mininum_elements_compliant


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_author_name")
test_files_missing_author_name = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_author_name)
def test_sbomchecker_missing_author_name(test_file):
    sbom = sbom_checker.SbomChecker(test_file)
    assert sbom.file == test_file
    assert sbom.doc_version
    assert not sbom.doc_author
    assert sbom.doc_timestamp
    assert sbom.dependency_relationships
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    assert not sbom.components_without_suppliers
    assert not sbom.components_without_identifiers
    assert not sbom.ntia_mininum_elements_compliant


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_timestamp")
test_files_missing_timestamp = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", test_files_missing_timestamp)
def test_sbomchecker_missing_timestamp(test_file):
    sbom = sbom_checker.SbomChecker(test_file)
    assert sbom.file == test_file
    assert sbom.doc_version
    assert sbom.doc_author
    assert not sbom.doc_timestamp
    assert sbom.dependency_relationships
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    assert not sbom.components_without_suppliers
    assert not sbom.components_without_identifiers
    assert not sbom.ntia_mininum_elements_compliant


dirname = os.path.join(
    os.path.dirname(__file__), "data", "missing_dependency_relationships"
)
test_files_missing_dependency_relationships = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_dependency_relationships)
def test_sbomchecker_missing_dependency_relationships(test_file):
    sbom = sbom_checker.SbomChecker(test_file)
    assert sbom.file == test_file
    assert sbom.doc_version
    assert sbom.doc_author
    assert sbom.doc_timestamp
    assert not sbom.dependency_relationships
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    assert not sbom.components_without_suppliers
    assert not sbom.components_without_identifiers
    assert not sbom.ntia_mininum_elements_compliant


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_component_version")
test_files_missing_component_version = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_component_version)
def test_sbomchecker_missing_component_version(test_file):
    sbom = sbom_checker.SbomChecker(test_file)
    assert sbom.file == test_file
    assert sbom.doc_version
    assert sbom.doc_author
    assert sbom.doc_timestamp
    assert sbom.dependency_relationships
    assert not sbom.components_without_names
    assert sbom.components_without_versions in [["glibc"], ["SPDX Translator"]]
    assert not sbom.components_without_suppliers
    assert not sbom.components_without_identifiers
    assert not sbom.ntia_mininum_elements_compliant


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_supplier_name")
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_sbomchecker_missing_supplier_name(test_file):
    sbom = sbom_checker.SbomChecker(test_file)
    assert sbom.file == test_file
    assert sbom.doc_version
    assert sbom.doc_author
    assert sbom.doc_timestamp
    assert sbom.dependency_relationships
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    # this list approach reflects that different formats
    # (e.g. JSON, tag-value, etc) are not identical. this
    # should probably be refactored in the future.
    assert sbom.components_without_suppliers in [
        ["glibc"],
        ["SPDX Translator"],
        ["glibc", "Apache Commons Lang"],
        ["glibc", "Saxon"],
    ]
    assert not sbom.components_without_identifiers
    assert not sbom.ntia_mininum_elements_compliant


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_unique_identifiers")
test_files_missing_unique_identifiers = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_unique_identifiers)
def test_sbomchecker_missing_unique_identifiers(test_file):
    sbom = sbom_checker.SbomChecker(test_file)
    assert sbom.file == test_file
    assert sbom.doc_version
    assert sbom.doc_author
    assert sbom.doc_timestamp
    assert sbom.dependency_relationships
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    assert not sbom.components_without_suppliers
    assert sbom.components_without_identifiers in [["glibc"], ["SPDX Translator"]]
    assert not sbom.ntia_mininum_elements_compliant


def test_sbomchecker_tern_photon_example():
    """Check that SBOM from Tern for Photon has an author."""
    test_file = os.path.join(
        os.path.dirname(__file__), "data", "SPDXSBOMExampleTests", "photon.spdx.tag"
    )
    sbom = sbom_checker.SbomChecker(test_file)
    assert sbom.doc_author


def test_sbomchecker_output_json():
    filepath = os.path.join(
        os.path.dirname(__file__), "data", "other_tests", "SPDXSBOMExample.spdx.yml"
    )
    sbom = sbom_checker.SbomChecker(filepath)
    got = sbom.output_json()
    assert got["sbomName"] == "xyz-0.1.0"
    assert not got["isNtiaConformant"]
    assert got["authorNameProvided"]
    assert not got["timestampProvided"]
    assert got["dependencyRelationshipsProvided"]
    assert got["componentNames"]["allProvided"]
    assert not got["componentNames"]["nonconformantComponents"]
    assert got["componentVersions"]["allProvided"]
    assert not got["componentVersions"]["nonconformantComponents"]
    assert got["componentIdentifiers"]["allProvided"]
    assert not got["componentIdentifiers"]["nonconformantComponents"]
    assert not got["componentSuppliers"]["allProvided"]
    assert got["componentSuppliers"]["nonconformantComponents"] == [
        "xyz",
        "curl",
        "openssl",
    ]
    assert got["totalNumberComponents"] == 3
