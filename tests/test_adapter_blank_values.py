# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for blank-value handling in adapters' get_components_without_* methods."""

from collections.abc import Callable
from unittest.mock import MagicMock

import pytest
from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.model.document import Document
from spdx_tools.spdx.model.package import Package
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.model.spdx_none import SpdxNone

from ntia_conformance_checker.adapters import SbomAdapter, Spdx2Adapter, Spdx3Adapter

PKG_ID = "https://example.com/pkg1"
MIT = "https://spdx.org/licenses/MIT"
NONE_ELEMENT = spdx3.IndividualElement.NAMED_INDIVIDUALS["NoneElement"]
NO_ASSERTION_ELEMENT = spdx3.IndividualElement.NAMED_INDIVIDUALS["NoAssertionElement"]
_LICENSES = spdx3.expandedlicensing_IndividualLicensingInfo.NAMED_INDIVIDUALS
NONE_LICENSE = _LICENSES["NoneLicense"]
NO_ASSERTION_LICENSE = _LICENSES["NoAssertionLicense"]


def _agent(name: str | None) -> MagicMock:
    agent = MagicMock()
    agent.name = name
    return agent


def _spdx2(attr: str, value: object) -> SbomAdapter:
    pkg = MagicMock(spec=Package, spdx_id=PKG_ID)
    setattr(pkg, attr, value)
    return Spdx2Adapter(MagicMock(spec=Document, packages=[pkg]))


def _spdx3(attr: str, value: object) -> Spdx3Adapter:
    pkg = MagicMock(spec=spdx3.software_Package, spdxId=PKG_ID)
    setattr(pkg, attr, value)
    object_set = spdx3.SHACLObjectSet()
    object_set.add(pkg)
    return Spdx3Adapter(object_set, None)


COMMON = [(None, True), ("", True), (" \t\n", True), ("valid", False)]

# method suffix -> (SPDX 2 Package attribute, SpdxNoAssertion counts as blank)
SPDX2_FIELDS = {
    "names": ("name", False),
    "versions": ("version", True),
    "suppliers": ("supplier", True),
    "identifiers": ("spdx_id", False),
    "concluded_licenses": ("license_concluded", True),
    "copyright_texts": ("copyright_text", True),
}

# method suffix -> SPDX 3 software_Package attribute
SPDX3_FIELDS = {
    "names": "name",
    "versions": "software_packageVersion",
    "suppliers": "suppliedBy",
    "identifiers": "spdxId",
    "copyright_texts": "software_copyrightText",
}

CASES = [
    *[
        pytest.param(_spdx2, method, attr, value, blank, id=f"spdx2-{method}-{value!r}")
        for method, (attr, no_assertion_blank) in SPDX2_FIELDS.items()
        for value, blank in [
            *COMMON,
            (SpdxNone(), False),
            (SpdxNoAssertion(), no_assertion_blank),
        ]
    ],
    *[
        pytest.param(_spdx3, method, attr, value, blank, id=f"spdx3-{method}-{value!r}")
        for method, attr in SPDX3_FIELDS.items()
        for value, blank in COMMON
    ],
    *[
        pytest.param(
            _spdx3,
            "suppliers",
            "suppliedBy",
            _agent(name),
            blank,
            id=f"spdx3-agent-{name!r}",
        )
        for name, blank in [(None, True), ("", True), (" \t\n", True), ("Acme", False)]
    ],
    *[
        pytest.param(
            _spdx3, "suppliers", "suppliedBy", ref, True, id=f"spdx3-ref-{ref}"
        )
        for ref in [
            NONE_ELEMENT,
            NO_ASSERTION_ELEMENT,
            "NoneElement",
            "NoAssertionElement",
        ]
    ],
]


@pytest.mark.parametrize(("build", "method", "attr", "value", "blank"), CASES)
def test_blank_values(
    build: Callable[[str, object], SbomAdapter],
    method: str,
    attr: str,
    value: object,
    blank: bool,
) -> None:
    """Blank values are reported, only for reachable packages."""
    get_missing = getattr(build(attr, value), f"get_components_without_{method}")

    assert bool(get_missing({PKG_ID})) is blank
    if method != "identifiers":  # identifiers ignore reachability
        assert get_missing(set()) == []


@pytest.mark.parametrize(
    ("licenses", "blank"),
    [
        pytest.param([], True, id="no-relationship"),
        pytest.param([NONE_LICENSE], True, id="NoneLicense"),
        pytest.param([NO_ASSERTION_LICENSE], True, id="NoAssertionLicense"),
        pytest.param(["expandedlicensing_NoneLicense"], True, id="compact"),
        pytest.param([NONE_ELEMENT], True, id="NoneElement"),
        pytest.param([NO_ASSERTION_LICENSE, NONE_LICENSE], True, id="all-blank"),
        pytest.param([MIT], False, id="MIT"),
        pytest.param([NO_ASSERTION_LICENSE, MIT], False, id="mixed"),
    ],
)
def test_spdx3_concluded_license_individuals(licenses: list[str], blank: bool) -> None:
    """None/NoAssertion license and element individuals are not a license."""
    adapter = _spdx3("name", "pkg")
    if licenses:
        rel = MagicMock(
            spec=spdx3.Relationship,
            relationshipType="hasConcludedLicense",
            from_=PKG_ID,
            to=licenses,
        )
        adapter.object_set.add(rel)

    missing = adapter.get_components_without_concluded_licenses({PKG_ID})

    assert bool(missing) is blank
