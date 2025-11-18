# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests checkers"""

# pylint: disable=missing-function-docstring,import-error,consider-using-from-import

import os
from pathlib import Path
from unittest import TestCase

import pytest
from beartype.roar import BeartypeCallHintParamViolation
from spdx_python_model import v3_0_1 as spdx3  # type: ignore # import-untyped

import ntia_conformance_checker.sbom_checker as sbom_checker
from ntia_conformance_checker import FSCT3Checker, NTIAChecker
from ntia_conformance_checker.base_checker import validate_spdx3_data

### Test no element missing

dirname = os.path.join(os.path.dirname(__file__), "data", "no_elements_missing")
test_files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", test_files)
def test_sbomchecker_ntia_no_errors(test_file):
    # No compliance argument is given to SbomChecker; Default is "ntia"
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
    assert sbom.compliant
    assert sbom.ntia_minimum_elements_compliant


@pytest.mark.parametrize("test_file", test_files)
def test_sbomchecker_fsct3_no_errors(test_file):
    sbom = sbom_checker.SbomChecker(test_file, compliance="fsct3-min")
    assert sbom.file == test_file
    assert sbom.doc_version
    assert sbom.doc_author
    assert sbom.doc_timestamp
    assert sbom.dependency_relationships
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    assert not sbom.components_without_suppliers
    assert not sbom.components_without_identifiers
    assert not sbom.components_without_concluded_licenses
    assert sbom.compliant


@pytest.mark.parametrize("test_file", test_files)
def test_ntiachecker_no_errors(test_file):
    sbom = NTIAChecker(test_file)
    assert sbom.file == test_file
    assert sbom.doc_version
    assert sbom.doc_author
    assert sbom.doc_timestamp
    assert sbom.dependency_relationships
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    assert not sbom.components_without_suppliers
    assert not sbom.components_without_identifiers
    assert sbom.compliant
    assert sbom.ntia_minimum_elements_compliant


@pytest.mark.parametrize("test_file", test_files)
def test_fsct3checker_no_errors(test_file):
    sbom = FSCT3Checker(test_file)
    assert sbom.file == test_file
    assert sbom.doc_version
    assert sbom.doc_author
    assert sbom.doc_timestamp
    assert sbom.dependency_relationships
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    assert not sbom.components_without_suppliers
    assert not sbom.components_without_identifiers
    assert not sbom.components_without_concluded_licenses
    assert sbom.compliant


### Test missing author name

dirname = os.path.join(os.path.dirname(__file__), "data", "missing_author_name")
test_files_missing_author_name = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_author_name)
def test_sbomchecker_missing_author_name(test_file):
    """The parser from spdx-tools will raise an SPDXParsingError if
    the document does not contain a creator."""
    try:
        sbom_check = sbom_checker.SbomChecker(test_file)

        assert not sbom_check.ntia_minimum_elements_compliant
        assert sbom_check.parsing_error
    except BeartypeCallHintParamViolation:
        pytest.xfail(
            "Beartype type violation (assigning None) due to missing author field"
        )


### Test missing timestamp

dirname = os.path.join(os.path.dirname(__file__), "data", "missing_timestamp")
test_files_missing_timestamp = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", test_files_missing_timestamp)
def test_sbomchecker_missing_timestamp(test_file):
    """The parser from spdx-tools will raise an SPDXParsingError if
    the document does not contain a created date."""
    try:
        sbom_check = sbom_checker.SbomChecker(test_file)

        assert not sbom_check.ntia_minimum_elements_compliant
        assert sbom_check.parsing_error
    except BeartypeCallHintParamViolation:
        pytest.xfail(
            "Beartype type violation (assigning None) due to missing timestamp field"
        )


### Test missing concluded licenses

dirname = os.path.join(os.path.dirname(__file__), "data", "missing_concluded_license")
test_files_missing_concluded_license = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_concluded_license)
def test_sbomchecker_missing_concluded_license(test_file):
    sbom_check = FSCT3Checker(test_file)

    assert sbom_check.components_without_concluded_licenses
    assert not sbom_check.compliant


### Test missing dependency relationships

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
    assert not sbom.compliant
    assert not sbom.ntia_minimum_elements_compliant


### Test missing component version

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
    TestCase().assertCountEqual(sbom.components_without_versions, ["glibc"])
    assert not sbom.components_without_suppliers
    assert not sbom.components_without_identifiers
    assert not sbom.compliant
    assert not sbom.ntia_minimum_elements_compliant


### Test missing supplier name

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
    TestCase().assertCountEqual(
        sbom.components_without_suppliers, ["glibc", "Jena", "Saxon"]
    )
    assert not sbom.components_without_identifiers
    assert not sbom.compliant
    assert not sbom.ntia_minimum_elements_compliant


### Test missing unique identifiers

dirname = os.path.join(os.path.dirname(__file__), "data", "missing_unique_identifiers")
test_files_missing_unique_identifiers = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_unique_identifiers)
def test_sbomchecker_missing_unique_identifiers(test_file):
    """The parser from spdx-tools will raise an SPDXParsingError if
    the document contains an element without SPDXID."""
    try:
        sbom_check = sbom_checker.SbomChecker(test_file)

        assert not sbom_check.compliant
        assert not sbom_check.ntia_minimum_elements_compliant
        assert sbom_check.parsing_error
    except BeartypeCallHintParamViolation:
        pytest.xfail(
            "Beartype type violation (assigning None) due to missing unique identifier field"
        )


### Test SBOM example from various sources


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


def test_sbomchecker_chainguard_example():
    """Check that SBOM for alpine has component with missing version."""
    test_file = os.path.join(
        os.path.dirname(__file__),
        "data",
        "SPDXSBOMExampleTests",
        "chainguard.spdx.json",
    )
    sbom = sbom_checker.SbomChecker(test_file)
    assert sbom.compliant
    assert sbom.ntia_minimum_elements_compliant


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


### Test SPDX 3 SBOM examples


def test_sbomchecker_spdx3_general():
    test_file = Path(__file__).parent / "data" / "spdx3" / "has_no_sbom.json"
    sbom = sbom_checker.SbomChecker(str(test_file), sbom_spec="spdx3")
    assert sbom is not None
    assert sbom.doc is not None
    assert isinstance(sbom.doc, spdx3.SHACLObjectSet)
    assert sbom.sbom_name == "hello"
    spdx3_spdx_document, validation_messages = validate_spdx3_data(sbom.doc)
    assert (
        len(validation_messages) >= 1
    )  # There should be a message about missing /Core/Bom.
    assert isinstance(spdx3_spdx_document, spdx3.SpdxDocument)
    assert getattr(spdx3_spdx_document, "name") == sbom.sbom_name
    assert (
        getattr(spdx3_spdx_document, "spdxId")
        == "https://swinslow.net/spdx-examples/example1/hello-v3-specv3/document0"
    )


def test_sbomchecker_spdx3_no_elements_missing():
    # This file contains no /Software/Package/,
    # but it does contain its subclass /Dataset/DatasetPackage/.
    # It should be treated as a regular software BOM.
    test_file = Path(__file__).parent / "data" / "spdx3" / "no_elements_missing.json"
    sbom = sbom_checker.SbomChecker(str(test_file), sbom_spec="spdx3")
    assert sbom is not None
    assert sbom.doc is not None
    assert isinstance(sbom.doc, spdx3.SHACLObjectSet)
    print(sbom.sbom_name)
    assert len(sbom.parsing_error) == 0
    assert len(sbom.validation_messages) == 0
    assert sbom.sbom_name is not None
    assert len(sbom.components_without_names) == 0
    assert len(sbom.components_without_versions) == 0
    assert len(sbom.components_without_identifiers) == 0
    assert len(sbom.components_without_suppliers) == 0
    assert len(sbom.components_without_concluded_licenses) == 0
    assert len(sbom.components_without_copyright_texts) == 0
    assert sbom.doc_version
    assert sbom.doc_author
    assert sbom.doc_timestamp
    assert sbom.compliant


def test_sbomchecker_fsct3_spdx3_no_elements_missing():
    test_file = Path(__file__).parent / "data" / "spdx3" / "no_elements_missing.json"
    sbom = sbom_checker.SbomChecker(
        str(test_file), sbom_spec="spdx3", compliance="fsct3-min"
    )
    assert sbom is not None
    assert sbom.doc is not None
    assert isinstance(sbom.doc, spdx3.SHACLObjectSet)
    assert sbom.compliant


def test_sbomchecker_spdx3_missing_supplier_name():
    test_file = Path(__file__).parent / "data" / "spdx3" / "missing_supplier_name.json"
    sbom = sbom_checker.SbomChecker(str(test_file), sbom_spec="spdx3")
    assert sbom is not None
    assert sbom.doc is not None
    assert isinstance(sbom.doc, spdx3.SHACLObjectSet)
    assert len(sbom.components_without_suppliers) == 1


def test_sbomchecker_spdx3_missing_version():
    test_file = Path(__file__).parent / "data" / "spdx3" / "missing_version.json"
    sbom = sbom_checker.SbomChecker(str(test_file), sbom_spec="spdx3")
    assert sbom is not None
    assert sbom.doc is not None
    assert isinstance(sbom.doc, spdx3.SHACLObjectSet)
    assert len(sbom.components_without_versions) == 1


def test_sbomchecker_spdx3_missing_unique_identifiers():
    test_file = (
        Path(__file__).parent / "data" / "spdx3" / "missing_unique_identifiers.json"
    )
    # SPDX 3 does not allow any element without a unique identifier,
    # so we expect a ValueError to be raised.
    with pytest.raises(ValueError):
        sbom_checker.SbomChecker(str(test_file), sbom_spec="spdx3")


### Other tests


def test_sbomchecker_output_json():
    filepath = os.path.join(
        os.path.dirname(__file__), "data", "other_tests", "SPDXSBOMExample.spdx.yml"
    )
    sbom = sbom_checker.SbomChecker(filepath)
    got = sbom.output_json()
    assert got["sbomName"] == "xyz-0.1.0"
    assert not got["isNtiaConformant"]
    assert not got["isConformant"]
    assert got["authorNameProvided"]
    assert got["timestampProvided"]
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
    expected = (
        "<div class='conformance-res'>\n"
        "<h2 class='conformance-res-title'>"
        "2021 NTIA SBOM Minimum Elements Conformance Results"
        "</h2>\n"
        "<h3 class='conformance-res-status'>Conformant: False</h3>\n"
        "<table class='conformance-res-tab'>\n"
        "<thead><tr><th>Requirement</th>"
        "<th>Conformant</th></tr></thead>\n"
        "<tbody>\n"
        "<tr><td class='conformance-res-tab-r'>All component names provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>All component versions provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>All component identifiers provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>All component suppliers provided?</td>"
        "<td class='conformance-res-tab-v'>False</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>SBOM author name provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>SBOM creation timestamp provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>Dependency relationships provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "</tbody>\n"
        "</table>\n"
        "</div>\n"
        "<div class='conformance-mis'>\n"
        "<p class='conformance-mis-label'>"
        "Missing required information in these components:</p>\n"
        "<ul class='conformance-mis-list'>\n"
        "<li>supplier (3): xyz, curl, openssl</li>\n"
        "</ul>\n"
        "</div>"
    )

    assert got == expected


def test_sbomchecker_fsct3_output_html():
    filepath = os.path.join(
        os.path.dirname(__file__), "data", "other_tests", "SPDXSBOMExample.spdx.yml"
    )
    sbom = sbom_checker.SbomChecker(filepath, compliance="fsct3-min")

    got = sbom.output_html()
    expected = (
        "<div class='conformance-res'>\n"
        "<h2 class='conformance-res-title'>"
        "2024 CISA Framing Software Component Transparency"
        " (minimum expectation) Conformance Results"
        "</h2>\n"
        "<h3 class='conformance-res-status'>Conformant: False</h3>\n"
        "<table class='conformance-res-tab'>\n"
        "<thead><tr><th>Requirement</th>"
        "<th>Conformant</th></tr></thead>\n"
        "<tbody>\n"
        "<tr><td class='conformance-res-tab-r'>All component names provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>All component versions provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>All component identifiers provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>All component suppliers provided?</td>"
        "<td class='conformance-res-tab-v'>False</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>All component concluded license provided?</td>"
        "<td class='conformance-res-tab-v'>False</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>All component copyright notice provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>SBOM author name provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>SBOM creation timestamp provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "<tr><td class='conformance-res-tab-r'>Dependency relationships provided?</td>"
        "<td class='conformance-res-tab-v'>True</td></tr>\n"
        "</tbody>\n"
        "</table>\n"
        "</div>\n"
        "<div class='conformance-mis'>\n"
        "<p class='conformance-mis-label'>"
        "Missing required information in these components:</p>\n"
        "<ul class='conformance-mis-list'>\n"
        "<li>supplier (3): xyz, curl, openssl</li>\n"
        "<li>concluded_license (3): xyz, curl, openssl</li>\n"
        "</ul>\n"
        "</div>"
    )

    assert got == expected


def test_components_without_functions():
    filepath = os.path.join(
        os.path.dirname(__file__),
        "data",
        "other_tests",
        "test_components_without_functions.spdx",
    )
    sbom = sbom_checker.SbomChecker(filepath)
    components = sbom.get_components_without_names()
    assert components == ["SPDXRef-Package1"]
    components = sbom.get_components_without_versions()
    assert components == ["glibc-no-version-1", "glibc-no-version-2"]
    components = sbom.get_components_without_versions(return_tuples=True)
    assert components == [
        ("glibc-no-version-1", "SPDXRef-Package2"),
        ("glibc-no-version-2", "SPDXRef-Package3"),
    ]
    components = sbom.get_components_without_suppliers()
    assert components == ["glibc-no-supplier"]
    components = sbom.get_components_without_suppliers(return_tuples=True)
    assert components == [("glibc-no-supplier", "SPDXRef-Package4")]
    # Not sure how to test this.
    # If any package misses the SPDXID the whole file seems to be invalid.
    # components = sbom.get_components_without_identifiers()
    # assert components == ["glibc-no-identifier"]
