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
        ["Saxon"],
        ["Apache Commons Lang"],
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
    assert sbom.components_without_versions == [
        "5e94941e3961b26645fbfdc71a59d439537b98417546bfdab35fa074f121eb15",
        "bash",
    ]


def test_sbomchecker_bom_alpine_example():
    """Check that SBOM for alpine has component with missing version."""
    test_file = os.path.join(
        os.path.dirname(__file__),
        "data",
        "SPDXSBOMExampleTests",
        "bom-alpine-3.15.spdx.json",
    )
    sbom = sbom_checker.SbomChecker(test_file)
    # currently checking only one component with a missing version
    assert (
        "sha256:850d4aa2c32a30db71a7e54dab7c605f74a4aeabf9418ccd9273b2480fcb6c04"
        in sbom.components_without_versions
    )


def test_sbomchecker_alpine_no_package_supplier_name_example():
    """Check that SBOM for alpine with NOASSERTION for supplier parses."""
    test_file = os.path.join(
        os.path.dirname(__file__),
        "data",
        "SPDXSBOMExampleTests",
        "alpine.spdx",
    )
    sbom = sbom_checker.SbomChecker(test_file)
    got = sbom.output_json()
    assert not got["componentSuppliers"]["allProvided"]


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


def test_sbomchecker_output_html():
    filepath = os.path.join(
        os.path.dirname(__file__), "data", "other_tests", "SPDXSBOMExample.spdx.yml"
    )
    sbom = sbom_checker.SbomChecker(filepath)

    got = sbom.output_html()
    expected = """
        <h2>NTIA Conformance Results</h2>
        <h3>Conformant: False

        <table>
        <tr>
            <th>Individual Elements</th>
            <th>Conformant</th>
        </tr>
        <tr>
            <td>All component names provided</td>
            <td>True</td>
        </tr>
        <tr>
            <td>All component versions provided</td>
            <td>True</td>
        </tr>
        <tr>
            <td>All component identifiers provided</td>
            <td>True</td>
        </tr>
        <tr>
            <td>All component suppliers provided</td>
            <td>False</td>
        </tr>
        <tr>
            <td>SBOM author name provided</td>
            <td>True</td>
        </tr>
        <tr>
            <td>SBOM creation timestamp provided</td>
            <td>False</td>
        </tr>
        <tr>
            <td>Dependency relationships provided?</td>
            <td>True</td>
        </tr>
        </table>
        """

    assert got == expected
