# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for the BSI TR-03183-2 conformance checker."""

import os
from unittest import TestCase

import pytest

from ntia_conformance_checker import BSIChecker


def _component_names(tuples_list: list[tuple[str, str]]) -> list[str]:
    """
    Extract first element from list of tuples,
    or second if first is None or empty.
    """
    return [t[0] if t and t[0] not in (None, "") else (t[1] if t else "") for t in tuples_list]


BSI_DATA_DIR = os.path.join(os.path.dirname(__file__), "data", "bsi")


def test_bsichecker_compliant_spdx3() -> None:
    """
    Test that a perfectly formatted BSI SPDX 3 document passes compliance and 
    triggers no warnings.
    """
    test_file = os.path.join(BSI_DATA_DIR, "compliant_bsi_spdx3.json")
    if not os.path.exists(test_file):
        pytest.skip(f"Test file {test_file} not found.")

    sbom = BSIChecker(test_file, compliance="bsi", sbom_spec="spdx3")

    # Overall Compliance
    assert sbom.compliant

    # Document Level (Required)
    assert sbom.doc_creator
    assert sbom.doc_timestamp
    assert sbom.doc_uri
    assert sbom.dependency_completeness

    # Component Level (Required) - should be empty lists
    assert not sbom.components_without_names
    assert not sbom.components_without_versions
    assert not sbom.components_without_creators
    assert not sbom.components_without_filenames
    assert not sbom.components_without_concluded_licenses
    assert not sbom.components_without_sha512_hashes
    assert not sbom.components_without_executable_prop
    assert not sbom.components_without_archive_prop
    assert not sbom.components_without_structured_prop

    # Additional/Optional Level (Warnings)
    assert not sbom.components_without_source_code_uris
    assert not sbom.components_without_deployable_uris
    assert not sbom.components_without_unique_identifiers
    assert not sbom.components_without_original_licenses
    assert not sbom.components_without_effective_licenses
    assert not sbom.components_without_source_code_hashes
    assert not sbom.components_without_security_txt
    assert not sbom.components_without_bom_references


def test_bsichecker_missing_creator() -> None:
    """Test that missing a valid BSI Creator (email/URL) fails compliance."""
    test_file = os.path.join(BSI_DATA_DIR, "missing_bsi_creator.json")
    if not os.path.exists(test_file):
        pytest.skip(f"Test file {test_file} not found.")

    sbom = BSIChecker(test_file, compliance="bsi", sbom_spec="spdx3")

    assert not sbom.compliant
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_creators), ["example-component"]
    )


def test_bsichecker_missing_sha512_hash() -> None:
    """Test that a component using SHA-256 instead of SHA-512 fails compliance."""
    test_file = os.path.join(BSI_DATA_DIR, "missing_sha512_hash.json")
    if not os.path.exists(test_file):
        pytest.skip(f"Test file {test_file} not found.")

    sbom = BSIChecker(test_file, compliance="bsi", sbom_spec="spdx3")

    assert not sbom.compliant
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_sha512_hashes), ["example-component"]
    )


def test_bsichecker_missing_structured_property() -> None:
    """Test that a component missing both 'container' and 'firmware' fails compliance."""
    test_file = os.path.join(BSI_DATA_DIR, "missing_structured_property.json")
    if not os.path.exists(test_file):
        pytest.skip(f"Test file {test_file} not found.")

    sbom = BSIChecker(test_file, compliance="bsi", sbom_spec="spdx3")

    assert not sbom.compliant
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_structured_prop), ["example-component"]
    )


def test_bsichecker_missing_distribution_filename() -> None:
    """Test that a component missing a distribution filename fails compliance."""
    test_file = os.path.join(BSI_DATA_DIR, "missing_distribution_filename.json")
    if not os.path.exists(test_file):
        pytest.skip(f"Test file {test_file} not found.")

    sbom = BSIChecker(test_file, compliance="bsi", sbom_spec="spdx3")

    assert not sbom.compliant
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_filenames), ["example-component"]
    )


def test_bsichecker_missing_concluded_license() -> None:
    """Test that a component missing a concluded license expression fails compliance."""
    test_file = os.path.join(BSI_DATA_DIR, "missing_concluded_license.json")
    if not os.path.exists(test_file):
        pytest.skip(f"Test file {test_file} not found.")

    sbom = BSIChecker(test_file, compliance="bsi", sbom_spec="spdx3")

    assert not sbom.compliant
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_concluded_licenses),
        ["example-component"],
    )


def test_bsichecker_missing_sbom_uri() -> None:
    """Test that a document without a valid SBOM URI fails compliance."""
    test_file = os.path.join(BSI_DATA_DIR, "missing_sbom_uri.json")
    if not os.path.exists(test_file):
        pytest.skip(f"Test file {test_file} not found.")

    sbom = BSIChecker(test_file, compliance="bsi", sbom_spec="spdx3")

    assert not sbom.doc_uri
    assert not sbom.compliant


def test_bsichecker_missing_optional_warnings() -> None:
    """
    Test that missing Additional/Optional fields correctly populates warning lists
    but DOES NOT fail the overall compliance of the document.
    """
    test_file = os.path.join(BSI_DATA_DIR, "missing_optional_warnings.json")
    if not os.path.exists(test_file):
        pytest.skip(f"Test file {test_file} not found.")

    sbom = BSIChecker(test_file, compliance="bsi", sbom_spec="spdx3")

    # The document MUST still be compliant
    assert sbom.compliant

    # However, all warning lists should have exactly 1 missing package
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_source_code_uris),
        ["example-component"],
    )
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_deployable_uris), ["example-component"]
    )
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_unique_identifiers),
        ["example-component"],
    )
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_original_licenses),
        ["example-component"],
    )
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_effective_licenses),
        ["example-component"],
    )
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_source_code_hashes),
        ["example-component"],
    )
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_security_txt), ["example-component"]
    )
    TestCase().assertCountEqual(
        _component_names(sbom.components_without_bom_references), ["example-component"]
    )
