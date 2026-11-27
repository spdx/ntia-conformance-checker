# SPDX-FileCopyrightText: 2024-2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for SbomChecker.get_components_without_identifiers"""

# pylint: disable=missing-function-docstring,import-error,consider-using-from-import

from datetime import datetime, timezone
from typing import Any
from unittest.mock import MagicMock

import pytest
from spdx_python_model.bindings import v3_0_1 as spdx3

import ntia_conformance_checker.sbom_checker as sbom_checker
from ntia_conformance_checker.adapters import Spdx2Adapter, Spdx3Adapter

_BASE = "http://example.com/spdx3/"
_CREATION_INFO = spdx3.CreationInfo(
    _id=_BASE + "creation-info",
    specVersion="3.0.1",
    created=datetime.now(timezone.utc),
    createdBy=[_BASE + "actor1"],
)


def _ext_id(kind: str, identifier: str) -> spdx3.ExternalIdentifier:
    return spdx3.ExternalIdentifier(
        externalIdentifierType=getattr(spdx3.ExternalIdentifierType, kind),
        identifier=identifier,
    )


def _content_id(value: str) -> spdx3.software_ContentIdentifier:
    return spdx3.software_ContentIdentifier(
        software_contentIdentifierType=spdx3.software_ContentIdentifierType.gitoid,
        software_contentIdentifierValue=value,
    )


# package properties -> does the package have a unique identifier?
SPDX3_CASES: dict[str, tuple[dict[str, Any], bool]] = {
    "package URL": ({"software_packageUrl": "pkg:pypi/a@1"}, True),
    "content identifier": (
        {"software_contentIdentifier": [_content_id("gitoid:b")]},
        True,
    ),
    "packageUrl external identifier": (
        {"externalIdentifier": [_ext_id("packageUrl", "pkg:pypi/a@1")]},
        True,
    ),
    "cpe23 external identifier": (
        {"externalIdentifier": [_ext_id("cpe23", "cpe:2.3:a:x:y:1:*:*:*:*:*:*:*")]},
        True,
    ),
    "cpe22 external identifier": (
        {"externalIdentifier": [_ext_id("cpe22", "cpe:/a:x:y:1")]},
        True,
    ),
    "swid external identifier": (
        {"externalIdentifier": [_ext_id("swid", "swid:example.com-y-1")]},
        True,
    ),
    "swhid external identifier": (
        {"externalIdentifier": [_ext_id("swhid", "swh:1:cnt:" + "0" * 40)]},
        True,
    ),
    "gitoid external identifier": (
        {"externalIdentifier": [_ext_id("gitoid", "gitoid:blob:sha1:" + "0" * 40)]},
        True,
    ),
    "other external identifier (UUID)": (
        {"externalIdentifier": [_ext_id("other", "urn:uuid:" + "0" * 32)]},
        True,
    ),
    "only the spdxId": ({}, False),
    "blank package URL": ({"software_packageUrl": "  "}, False),
    "NOASSERTION package URL": ({"software_packageUrl": "NOASSERTION"}, False),
    "email external identifier": (
        {"externalIdentifier": [_ext_id("email", "a@example.com")]},
        False,
    ),
    "cve external identifier": (
        {"externalIdentifier": [_ext_id("cve", "CVE-2026-0001")]},
        False,
    ),
    "urlScheme external identifier": (
        {"externalIdentifier": [_ext_id("urlScheme", "https://example.com")]},
        False,
    ),
    "blank external identifier": (
        {"externalIdentifier": [_ext_id("packageUrl", " ")]},
        False,
    ),
    "blank content identifier": (
        {"software_contentIdentifier": [_content_id("")]},
        False,
    ),
}


@pytest.mark.parametrize("name", SPDX3_CASES)
def test_spdx3_unique_identifier(name: str) -> None:
    """The spdxId every element has does not count as an identifier."""
    props, identified = SPDX3_CASES[name]
    object_set = spdx3.SHACLObjectSet()
    pkg = spdx3.software_Package(
        _id=_BASE + "pkg", creationInfo=_CREATION_INFO, name="pkg"
    )
    for prop, value in props.items():
        setattr(pkg, prop, value)
    object_set.add(pkg)
    adapter = Spdx3Adapter(object_set, None)

    expected: list[tuple[str, str]] = [] if identified else [("pkg", _BASE + "pkg")]
    assert adapter.get_components_without_identifiers({_BASE + "pkg"}) == expected
    assert adapter.get_components_without_identifiers(set()) == []  # unreachable


@pytest.mark.parametrize("cls", [spdx3.ai_AIPackage, spdx3.dataset_DatasetPackage])
def test_spdx3_unique_identifier_subclass(cls: type[spdx3.software_Package]) -> None:
    """Package subclasses are checked too."""
    object_set = spdx3.SHACLObjectSet()
    for name, purl in (("with", "pkg:pypi/a@1"), ("without", None)):
        pkg = cls(_id=_BASE + name, creationInfo=_CREATION_INFO, name=name)
        if purl:
            pkg.software_packageUrl = purl
        object_set.add(pkg)
    adapter = Spdx3Adapter(object_set, None)
    reachable = {_BASE + "with", _BASE + "without"}
    assert adapter.get_components_without_identifiers(reachable) == [
        ("without", _BASE + "without")
    ]


def test_get_components_without_identifiers_spdx2() -> None:
    """Test get_components_without_identifiers with SPDX 2 documents."""
    checker = sbom_checker.SbomChecker("", validate=False, sbom_spec="spdx2")
    doc = MagicMock()
    pkg1 = MagicMock()
    pkg1.name = "pkg1"
    pkg1.spdx_id = "SPDXRef-Package1"

    pkg_no_id = MagicMock()
    pkg_no_id.name = "pkg-no-id"
    pkg_no_id.spdx_id = None

    pkg_empty_id = MagicMock()
    pkg_empty_id.name = "pkg-empty-id"
    pkg_empty_id.spdx_id = "   "

    doc.packages = [pkg1, pkg_no_id, pkg_empty_id]
    checker.doc = doc
    checker.reachable_component_ids = {"SPDXRef-Package1"}
    checker.adapter = Spdx2Adapter(doc)

    assert checker.get_components_without_identifiers() == [
        ("pkg-no-id", ""),
        ("pkg-empty-id", "   "),
    ]
