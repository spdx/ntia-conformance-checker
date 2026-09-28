# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for blank-value handling in adapters' get_components_without_* methods."""

import json
from collections.abc import Callable
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.model.document import Document
from spdx_tools.spdx.model.package import Package
from spdx_tools.spdx.parser.parse_anything import parse_file

from ntia_conformance_checker.adapters import SbomAdapter, Spdx2Adapter, Spdx3Adapter

PKG_ID = "https://example.com/pkg1"
MIT = "https://spdx.org/licenses/MIT"
EXPR_ID = "https://example.com/expr1"
NONE_ELEMENT = spdx3.IndividualElement.NAMED_INDIVIDUALS["NoneElement"]
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


COMMON = [(None, True), (" \t\n", True), ("valid", False)]

# Only these fields take NONE/NOASSERTION keywords; others are literal.
KEYWORD_FIELDS = {"suppliers", "concluded_licenses", "copyright_texts"}

# method suffix -> SPDX 2 Package attribute
SPDX2_FIELDS = {
    "names": "name",
    "versions": "version",
    "suppliers": "supplier",
    "identifiers": "spdx_id",
    "concluded_licenses": "license_concluded",
    "copyright_texts": "copyright_text",
}

# method suffix -> SPDX 3 software_Package attribute
SPDX3_FIELDS = {
    "names": "name",
    "versions": "software_packageVersion",
    "suppliers": "suppliedBy",
    "identifiers": "spdxId",
    "copyright_texts": "software_copyrightText",
}

SPDX3_SUPPLIERS = [
    (_agent(None), True),
    (_agent("Acme"), False),
    (NONE_ELEMENT, True),
    ("NoAssertionElement", True),  # compact form kept by the deserializer
]

CASES = [
    *[
        pytest.param(_spdx2, method, attr, value, blank, id=f"spdx2-{method}-{value!r}")
        for method, attr in SPDX2_FIELDS.items()
        for value, blank in [*COMMON, ("none", method in KEYWORD_FIELDS)]
    ],
    *[
        pytest.param(_spdx3, method, attr, value, blank, id=f"spdx3-{method}-{value!r}")
        for method, attr in SPDX3_FIELDS.items()
        for value, blank in [
            *COMMON,
            ("none", method in KEYWORD_FIELDS),
            *(SPDX3_SUPPLIERS if method == "suppliers" else []),
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
        pytest.param(["expandedlicensing_NoAssertionLicense"], True, id="compact"),
        pytest.param([NONE_ELEMENT], True, id="NoneElement"),
        pytest.param([MIT], False, id="MIT"),
        pytest.param([NO_ASSERTION_LICENSE, MIT], False, id="mixed"),
        pytest.param([EXPR_ID], True, id="expression-NOASSERTION"),
        pytest.param([EXPR_ID, MIT], False, id="expression-mixed"),
    ],
)
def test_spdx3_concluded_license_individuals(licenses: list[str], blank: bool) -> None:
    """None/NoAssertion individuals and expressions are not a license."""
    adapter = _spdx3("name", "pkg")
    adapter.object_set.add(
        spdx3.simplelicensing_LicenseExpression(
            spdxId=EXPR_ID, simplelicensing_licenseExpression="NOASSERTION"
        )
    )
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


@pytest.mark.parametrize(
    ("key", "value", "method", "missing"),
    [
        ("versionInfo", "NOASSERTION", "versions", False),  # literal str
        ("supplier", "NOASSERTION", "suppliers", True),  # SpdxNoAssertion
        ("copyrightText", "NONE", "copyright_texts", True),  # SpdxNone
        ("copyrightText", "none", "copyright_texts", True),  # str
    ],
)
def test_spdx2_parsed_keywords(
    tmp_path: Path, key: str, value: str, method: str, missing: bool
) -> None:
    """Keywords are missing in keyword fields, whether objects or str."""
    src = Path(__file__).parent / "data/no_elements_missing"
    sbom_json = json.loads((src / "SPDXJSONExample-v2.3.spdx.json").read_text())
    package = sbom_json["packages"][0]
    package[key] = value
    test_file = tmp_path / "sbom.spdx.json"
    test_file.write_text(json.dumps(sbom_json))

    adapter = Spdx2Adapter(parse_file(str(test_file)))
    result = getattr(adapter, f"get_components_without_{method}")({package["SPDXID"]})

    assert bool(result) is missing
