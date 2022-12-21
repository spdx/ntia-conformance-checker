"""Tests using pytest framework."""

# pylint: disable=missing-function-docstring,import-error

import os

import pytest
from spdx.parsers import parse_anything

import ntia_conformance_checker.cli_tools.check_anything as check_anything  # pylint: disable=consider-using-from-import

dirname = os.path.join(os.path.dirname(__file__), "data", "no_elements_missing")
test_files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", test_files)
def test_checker_no_errors(test_file):
    doc, error = parse_anything.parse_file(test_file)
    print(str(doc.version) == "SPDX-2.1")
    assert not error
    assert not check_anything.check_minimum_elements(test_file).messages


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_author_name")
test_files_missing_author_name = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_author_name)
def test_checker_missing_author_name(test_file):
    doc, error = parse_anything.parse_file(test_file)
    assert not error
    assert check_anything.check_minimum_elements(test_file).messages == [
        str(doc.name) + ": Document has no author."
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_timestamp")
test_files_missing_timestamp = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", test_files_missing_timestamp)
def test_checker_missing_timestamp(test_file):
    doc, error = parse_anything.parse_file(test_file)
    assert error
    assert check_anything.check_minimum_elements(test_file).messages == [
        str(doc.name + ": Errors while parsing: True"),
        str(doc.name + ": Document has no timestamp."),
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "other_tests")
file = [os.path.join(dirname, "SPDXSBOMExample.spdx.yml")]


@pytest.mark.parametrize("test_file", file)
def test_checker_missing_timestamp_(test_file):
    _, error = parse_anything.parse_file(test_file)
    assert error
    assert check_anything.check_minimum_elements(test_file).messages == [
        "xyz-0.1.0: Errors while parsing: True",
        "xyz-0.1.0: Document has no timestamp.",
        "xyz-0.1.0: xyz has no supplier.",
        "xyz-0.1.0: curl has no supplier.",
        "xyz-0.1.0: openssl has no supplier.",
        "xyz-0.1.0: xyz has no identifier.",
        "xyz-0.1.0: curl has no identifier.",
        "xyz-0.1.0: openssl has no identifier.",
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_supplier_name")
test_files_missing_supplier_name = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_supplier_name)
def test_checker_missing_author_name_json(test_file):
    _, error = parse_anything.parse_file(test_file)
    assert not error
    assert check_anything.check_minimum_elements(test_file).messages == [
        "Sample_Document-V2.1: SPDX Translator has no supplier.",
        "Sample_Document-V2.1: SPDX Translator has no identifier.",
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_author_name")
missing_author_name_rdf = [os.path.join(dirname, "SPDXRdfExample.rdf")]


@pytest.mark.parametrize("test_file", missing_author_name_rdf)
def test_checker_missing_author_name_rdf(test_file):
    _, error = parse_anything.parse_file(test_file)
    assert not error
    assert check_anything.check_minimum_elements(test_file).messages == [
        "Sample_Document-V2.1: Document has no author."
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "SPDXSBOMExampleTests")
missing_author_name_yml = [
    os.path.join(dirname, "SPDXSBOMExampleMissingAuthorName.spdx.yml")
]


@pytest.mark.parametrize("test_file", missing_author_name_yml)
def test_checker_missing_author_name_yml(test_file):
    _, error = parse_anything.parse_file(test_file)
    assert not error
    assert check_anything.check_minimum_elements(test_file).messages == [
        "xyz-0.1.0: Document has no author.",
        "xyz-0.1.0: xyz has no supplier.",
        "xyz-0.1.0: curl has no supplier.",
        "xyz-0.1.0: openssl has no supplier.",
        "xyz-0.1.0: xyz has no identifier.",
        "xyz-0.1.0: curl has no identifier.",
        "xyz-0.1.0: openssl has no identifier.",
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_supplier_name")
files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]


@pytest.mark.parametrize("test_file", files)
def test_checker_missing_supplier_name(test_file):
    _, error = parse_anything.parse_file(test_file)
    assert not error
    assert check_anything.check_minimum_elements(test_file).messages == [
        "Sample_Document-V2.1: SPDX Translator has no supplier.",
        "Sample_Document-V2.1: SPDX Translator has no identifier.",
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_author_name")
test_files_missing_author_name = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_author_name)
def test_checker_missing_author_name_simple_tag(test_file):
    _, error = parse_anything.parse_file(test_file)
    assert not error
    assert check_anything.check_minimum_elements(test_file).messages == [
        "Sample_Document-V2.1: Document has no author."
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_component_version")
test_files_missing_component_version = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_component_version)
def test_checker_missing_version_name_simple_tag(test_file):
    doc, error = parse_anything.parse_file(test_file)
    assert not error
    assert check_anything.check_minimum_elements(test_file).messages == [
        doc.name + ": " + doc.packages[0].name + " has no version."
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_unique_identifiers")
test_files_missing_unique_identifiers = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_unique_identifiers)
def test_checker_missing_unique_identifiers(test_file):
    _, _ = parse_anything.parse_file(test_file)
    assert check_anything.check_minimum_elements(test_file).messages == [
        "Sample_Document-V2.1: Errors while parsing: True"
    ]


dirname = os.path.join(
    os.path.dirname(__file__), "data", "missing_dependency_relationships"
)
test_files_missing_dependency_relationships = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_dependency_relationships)
def test_checker_missing_dependency_relationships(test_file):
    doc, error = parse_anything.parse_file(test_file)
    assert not error
    assert check_anything.check_minimum_elements(test_file).messages == [
        str(doc.name) + ": Document has no dependency relationships."
    ]


dirname = os.path.join(os.path.dirname(__file__), "data", "missing_component_name")
test_files_missing_component_names = [
    os.path.join(dirname, fn) for fn in os.listdir(dirname)
]


@pytest.mark.parametrize("test_file", test_files_missing_component_names)
def test_fossology(test_file):
    doc, error = parse_anything.parse_file(test_file)
    assert error
    assert check_anything.check_minimum_elements(test_file).messages == [
        str(doc.name + ": Errors while parsing: True")
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
