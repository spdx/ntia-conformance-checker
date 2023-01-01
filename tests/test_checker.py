"""Tests using pytest framework."""

# pylint: disable=missing-function-docstring,import-error,consider-using-from-import

import os

import pytest
from spdx.parsers import parse_anything

import ntia_conformance_checker.cli_tools.check_anything as check_anything  # pylint: disable=consider-using-from-import
import ntia_conformance_checker.cli_tools.output as output

dirname = os.path.join(os.path.dirname(__file__), "data", "no_elements_missing")
test_files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", test_files)
def test_checker_no_errors(test_file):
    parse_anything.parse_file(test_file)
    assert not check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_author_name")
test_files_missing_author_name = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_author_name)
def test_checker_missing_author_name(test_file):
    doc, _ = parse_anything.parse_file(test_file)
    assert check_anything.check_minimum_elements(test_file).messages == [
        str(doc.name) + ": Document has no author."
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_timestamp")
test_files_missing_timestamp = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", test_files_missing_timestamp)
def test_checker_missing_timestamp(test_file):
    doc, _ = parse_anything.parse_file(test_file)
    assert check_anything.check_minimum_elements(test_file).messages == [
        str(doc.name + ": Errors while parsing: True"),
        str(doc.name + ": Document has no timestamp."),
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_supplier_name")
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_checker_missing_supplier_name(test_file):
    doc, _ = parse_anything.parse_file(test_file)
    assert check_anything.check_minimum_elements(test_file).messages == [
        f"{doc.name}: {doc.packages[0].name} has no supplier."
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_component_version")
test_files_missing_component_version = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_component_version)
def test_checker_missing_component_version(test_file):
    doc, _ = parse_anything.parse_file(test_file)
    assert check_anything.check_minimum_elements(test_file).messages == [
        doc.name + ": " + doc.packages[0].name + " has no version."
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_unique_identifiers")
test_files_missing_unique_identifiers = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_unique_identifiers)
def test_checker_missing_unique_identifiers(test_file):
    # note: it appears to not be possible to check exclusively
    # for a missing unique identifier. the spdx-tools parsing library
    # considers missing unique identifiers to be an error
    doc, _ = parse_anything.parse_file(test_file)
    assert check_anything.check_minimum_elements(test_file).messages == [
        f"{doc.name}: Errors while parsing: True",
        f"{doc.name}: {doc.packages[0].name} has no identifier.",
    ]


dirname = os.path.join(
    os.path.dirname(__file__), "data", "missing_dependency_relationships"
)
test_files_missing_dependency_relationships = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_dependency_relationships)
def test_checker_missing_dependency_relationships(test_file):
    doc, _ = parse_anything.parse_file(test_file)
    assert check_anything.check_minimum_elements(test_file).messages == [
        str(doc.name) + ": Document has no dependency relationships."
    ]


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "FOSSology")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_kubernetes(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "Kubernetes")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_metaeffekt(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "metaeffekt")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_metaspdxscanner(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "MetaSpdxscanner")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_nexb(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "nexB")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_openembedded(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "OpenEmbedded")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_philips(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "Philips")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_rea(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "REA")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_sourceauditor(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "SourceAuditor")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_synopsysblackduck(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "SynopsysBlackDuck")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_synopsys_black_duck(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "Tern")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_tern(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "doc_fest", "ZephyrWest")
file_dict = {}
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_zephyrwest(test_file):
    if test_file not in file_dict:
        file_dict[test_file] = check_anything.check_minimum_elements(test_file).messages


def test_is_document_level_element_present():
    messages = ["Document has no author.", "Document has no timestamp."]
    got = output.is_document_level_element_present(messages, "Document has no author.")
    # because there is an error message that the "document has no author",
    # then that SBOM minimum element is not present, so False
    assert got is False


def test_find_nonconformant_component_level_elements():
    messages = [
        "pkg1 has has no supplier.",
        "Document has no author.",
        "Document has no timestamp.",
        "pkg2 has has no supplier.",
    ]
    got = output.find_nonconformant_component_level_elements(
        messages, "has no supplier."
    )
    assert got == ["pkg1", "pkg2"]


def test_structure_messages():
    messages = [
        "pkg1 has has no supplier.",
        "Document has no author.",
        "Document has no timestamp.",
        "pkg2 has has no supplier.",
    ]
    filepath = os.path.join(
        os.path.dirname(__file__), "data", "other_tests", "SPDXSBOMExample.spdx.yml"
    )
    got = output.structure_messages(filepath, messages)
    assert got == {
        "componentVersions": {"nonconformantComponents": [], "allProvided": True},
        "componentIdentifiers": {"nonconformantComponents": [], "allProvided": True},
        "componentSuppliers": {
            "nonconformantComponents": ["pkg1", "pkg2"],
            "allProvided": False,
        },
        "componentNames": {"numNonconformantComponents": 0, "allProvided": True},
        "authorNameProvided": False,
        "timestampProvided": False,
        "dependencyRelationshipsProvided": True,
        "isNtiaConformant": False,
        "sbomName": "xyz-0.1.0",
    }
