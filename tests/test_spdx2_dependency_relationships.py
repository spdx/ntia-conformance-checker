# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for SPDX 2 dependency relationship checking."""

import json
from datetime import datetime, timezone
from pathlib import Path

import pytest
from spdx_tools.spdx.model.actor import Actor, ActorType
from spdx_tools.spdx.model.checksum import Checksum, ChecksumAlgorithm
from spdx_tools.spdx.model.document import CreationInfo, Document
from spdx_tools.spdx.model.file import File
from spdx_tools.spdx.model.package import Package
from spdx_tools.spdx.model.relationship import Relationship, RelationshipType
from spdx_tools.spdx.model.snippet import Snippet
from spdx_tools.spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx_tools.spdx.model.spdx_none import SpdxNone

from ntia_conformance_checker import NTIAChecker, SbomChecker
from ntia_conformance_checker.adapters.spdx2_adapter import (
    Spdx2Adapter,
    has_spdx2_dependency_relationship,
)


def _build_spdx2_doc(relationships: list[Relationship]) -> Document:
    """Create a minimal SPDX 2.3 Document with two packages and relationships."""
    creation_info = CreationInfo(
        spdx_version="SPDX-2.3",
        spdx_id="SPDXRef-DOCUMENT",
        name="test-spdx2-dependency",
        document_namespace="https://example.com/spdx/test-dependency",
        creators=[Actor(ActorType.ORGANIZATION, "Example Org")],
        created=datetime(2026, 7, 4, 12, 0, 0, tzinfo=timezone.utc),
    )
    pkg_app = Package(
        name="application",
        spdx_id="SPDXRef-Package-App",
        download_location=SpdxNoAssertion(),
        version="1.0.0",
        supplier=Actor(ActorType.ORGANIZATION, "Example Org"),
        files_analyzed=False,
    )
    pkg_lib = Package(
        name="library",
        spdx_id="SPDXRef-Package-Lib",
        download_location=SpdxNoAssertion(),
        version="2.0.0",
        supplier=Actor(ActorType.ORGANIZATION, "Example Org"),
        files_analyzed=False,
    )
    return Document(
        creation_info=creation_info,
        packages=[pkg_app, pkg_lib],
        relationships=relationships,
    )


@pytest.mark.parametrize(
    ("relationship_type", "expected"),
    [
        (RelationshipType.CONTAINS, True),
        (RelationshipType.CONTAINED_BY, True),
        (RelationshipType.DEPENDS_ON, True),
        (RelationshipType.DEPENDENCY_OF, True),
        (RelationshipType.BUILD_DEPENDENCY_OF, True),
        (RelationshipType.DEV_DEPENDENCY_OF, True),
        (RelationshipType.OPTIONAL_DEPENDENCY_OF, True),
        (RelationshipType.PROVIDED_DEPENDENCY_OF, True),
        (RelationshipType.RUNTIME_DEPENDENCY_OF, True),
        (RelationshipType.TEST_DEPENDENCY_OF, True),
        (RelationshipType.DYNAMIC_LINK, True),
        (RelationshipType.STATIC_LINK, True),
        (RelationshipType.DESCRIBES, False),
        (RelationshipType.DESCRIBED_BY, False),
        (RelationshipType.VARIANT_OF, False),
        (RelationshipType.COPY_OF, False),
        (RelationshipType.GENERATED_FROM, False),
        (RelationshipType.OTHER, False),
    ],
)
def test_spdx2_dependency_relationship_types(
    relationship_type: RelationshipType, expected: bool
) -> None:
    """Verify supported and unsupported SPDX 2 dependency relationship types."""
    doc = _build_spdx2_doc(
        [
            Relationship(
                "SPDXRef-DOCUMENT",
                RelationshipType.DESCRIBES,
                "SPDXRef-Package-App",
            ),
            Relationship(
                "SPDXRef-Package-App",
                relationship_type,
                "SPDXRef-Package-Lib",
            ),
        ]
    )
    assert has_spdx2_dependency_relationship(doc) is expected
    assert Spdx2Adapter(doc).check_dependency_relationships() is expected


def test_spdx2_document_level_relationships_do_not_satisfy_dependency() -> None:
    """Document-to-package DESCRIBES or CONTAINS is not a component dependency."""
    doc = _build_spdx2_doc(
        [
            Relationship(
                "SPDXRef-DOCUMENT",
                RelationshipType.DESCRIBES,
                "SPDXRef-Package-App",
            ),
            Relationship(
                "SPDXRef-DOCUMENT",
                RelationshipType.CONTAINS,
                "SPDXRef-Package-App",
            ),
            Relationship(
                "SPDXRef-Package-App",
                RelationshipType.CONTAINED_BY,
                "SPDXRef-DOCUMENT",
            ),
        ]
    )
    assert not has_spdx2_dependency_relationship(doc)


def test_spdx2_dependency_relationship_accepts_file_and_snippet_elements() -> None:
    """Dependency/containment relationships between Package, File, and Snippet pass."""
    doc = _build_spdx2_doc([])
    doc.packages = doc.packages[:1]
    doc.files = [
        File(
            name="./src/main.c",
            spdx_id="SPDXRef-File-Main",
            checksums=[
                Checksum(
                    ChecksumAlgorithm.SHA1,
                    "d6a770ba38583ed4bb4525bd96e50461655d2758",
                )
            ],
        )
    ]
    doc.snippets = [
        Snippet(
            spdx_id="SPDXRef-Snippet-1",
            file_spdx_id="SPDXRef-File-Main",
            byte_range=(1, 10),
        )
    ]
    doc.relationships = [
        Relationship(
            "SPDXRef-Package-App",
            RelationshipType.CONTAINS,
            "SPDXRef-File-Main",
        )
    ]
    assert has_spdx2_dependency_relationship(doc)

    doc.relationships = [
        Relationship(
            "SPDXRef-File-Main",
            RelationshipType.CONTAINS,
            "SPDXRef-Snippet-1",
        )
    ]
    assert has_spdx2_dependency_relationship(doc)


@pytest.mark.parametrize(
    "target",
    [
        SpdxNone(),
        SpdxNoAssertion(),
        "SPDXRef-Missing",
        "SPDXRef-Package-App",
    ],
)
def test_spdx2_dependency_relationship_rejects_invalid_targets(
    target: str | SpdxNone | SpdxNoAssertion,
) -> None:
    """Targets that are NONE, NOASSERTION, missing, or self-referential return False."""
    doc = _build_spdx2_doc(
        [
            Relationship(
                "SPDXRef-Package-App",
                RelationshipType.DEPENDS_ON,
                target,
            )
        ]
    )
    assert not has_spdx2_dependency_relationship(doc)


def test_sbomchecker_spdx2_package_dependency_conformance(tmp_path: Path) -> None:
    """End-to-end check: DESCRIBES-only fails NTIA check; adding DEPENDS_ON passes."""
    sbom_data = {
        "SPDXID": "SPDXRef-DOCUMENT",
        "spdxVersion": "SPDX-2.3",
        "name": "SPDX2-Dependency-Test",
        "dataLicense": "CC0-1.0",
        "documentNamespace": "https://example.com/spdx/dependency-test",
        "creationInfo": {
            "creators": ["Organization: Example Org"],
            "created": "2026-07-04T12:00:00Z",
        },
        "packages": [
            {
                "name": "app",
                "SPDXID": "SPDXRef-App",
                "versionInfo": "1.0.0",
                "supplier": "Organization: Example Org",
                "downloadLocation": "NOASSERTION",
                "filesAnalyzed": False,
            },
            {
                "name": "lib",
                "SPDXID": "SPDXRef-Lib",
                "versionInfo": "2.0.0",
                "supplier": "Organization: Example Org",
                "downloadLocation": "NOASSERTION",
                "filesAnalyzed": False,
            },
        ],
        "relationships": [
            {
                "spdxElementId": "SPDXRef-DOCUMENT",
                "relationshipType": "DESCRIBES",
                "relatedSpdxElement": "SPDXRef-App",
            }
        ],
    }

    describes_only = tmp_path / "describes_only.spdx.json"
    describes_only.write_text(json.dumps(sbom_data), encoding="utf-8")

    checker_without_dep = SbomChecker(str(describes_only))
    assert not checker_without_dep.dependency_relationships
    assert not checker_without_dep.compliant

    sbom_relationships = sbom_data["relationships"]
    assert isinstance(sbom_relationships, list)
    sbom_relationships.append(
        {
            "spdxElementId": "SPDXRef-App",
            "relationshipType": "DEPENDS_ON",
            "relatedSpdxElement": "SPDXRef-Lib",
        }
    )
    with_depends_on = tmp_path / "with_depends_on.spdx.json"
    with_depends_on.write_text(json.dumps(sbom_data), encoding="utf-8")

    checker_with_dep = NTIAChecker(str(with_depends_on))
    assert checker_with_dep.dependency_relationships
    assert checker_with_dep.compliant
