# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for the relationship tables that drive graph traversal"""

# pylint: disable=missing-function-docstring,import-error

import pytest
from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.model.relationship import RelationshipType

from ntia_conformance_checker.constants import (
    SPDX2_RELATIONSHIP_TRAVERSAL,
    SPDX2_TO_SPDX3_RELATIONSHIP_TYPES,
    SPDX3_RELATIONSHIP_TRAVERSAL,
    VALID_SPDX2_COMPOSITION_RELATIONSHIPS,
    VALID_SPDX3_COMPOSITION_RELATIONSHIPS,
    TraversalDirection,
)
from ntia_conformance_checker.spdx3_utils import (
    SPDX3_INDIVIDUAL_ELEMENT_IRIS,
    SPDX3_NONE_AND_NOASSERTION_IRIS,
)


def test_translation_table_covers_every_spdx2_relationship_type() -> None:
    """The translation table has one row for each SPDX 2 relationship type."""
    assert set(SPDX2_TO_SPDX3_RELATIONSHIP_TYPES) == {
        rel_type.name for rel_type in RelationshipType
    }


def test_translation_table_has_spdx_using_30_corrections() -> None:
    """The DYNAMIC_LINK and FILE_MODIFIED rows are as corrected in spdx/using#30."""
    assert SPDX2_TO_SPDX3_RELATIONSHIP_TYPES["DYNAMIC_LINK"] == (
        "hasDynamicLink",
        False,
    )
    assert SPDX2_TO_SPDX3_RELATIONSHIP_TYPES["FILE_MODIFIED"] == ("modifiedBy", True)


def test_translation_table_and_traversal_use_spdx3_relationship_types() -> None:
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
        # From the translation table
        ("CONTAINS", TraversalDirection.ALONG),
        ("CONTAINED_BY", TraversalDirection.AGAINST),
        ("BUILD_TOOL_OF", TraversalDirection.AGAINST),
        ("DEV_TOOL_OF", TraversalDirection.AGAINST),
        ("TEST_TOOL_OF", TraversalDirection.AGAINST),
        ("GENERATED_FROM", TraversalDirection.ALONG),
        ("GENERATES", TraversalDirection.AGAINST),
        ("DYNAMIC_LINK", TraversalDirection.ALONG),  # fixed in spdx/using#30
        # Overrides
        ("DESCRIBES", TraversalDirection.ALONG),
        ("DESCRIBED_BY", TraversalDirection.AGAINST),
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
    for added in ("usesTool", "generates", "trainedOn", "testedOn"):
        assert added not in VALID_SPDX3_COMPOSITION_RELATIONSHIPS


def test_spdx3_none_and_noassertion_iris() -> None:
    """The placeholders are the four none and no-assertion individuals only."""
    assert {iri.rsplit("/", 1)[-1] for iri in SPDX3_NONE_AND_NOASSERTION_IRIS} == {
        "NoneElement",
        "NoAssertionElement",
        "NoneLicense",
        "NoAssertionLicense",
    }
    assert SPDX3_NONE_AND_NOASSERTION_IRIS < SPDX3_INDIVIDUAL_ELEMENT_IRIS
