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
from spdx_tools.spdx.model.external_document_ref import ExternalDocumentRef
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
        (RelationshipType.HAS_PREREQUISITE, True),
        (RelationshipType.PREREQUISITE_FOR, True),
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
        "NONE",
        "NOASSERTION",
    ],
)
def test_spdx2_dependency_relationship_accepts_none_and_noassertion(
    target: str | SpdxNone | SpdxNoAssertion,
) -> None:
    """Single-package SBOM stating NONE or NOASSERTION dependency returns True."""
    doc = _build_spdx2_doc(
        [
            Relationship(
                "SPDXRef-Package-App",
                RelationshipType.DEPENDS_ON,
                target,
            )
        ]
    )
    doc.packages = doc.packages[:1]
    assert has_spdx2_dependency_relationship(doc)
    assert has_spdx2_dependency_relationship(doc, reachable_ids={"SPDXRef-Package-App"})


def test_spdx2_dependency_relationship_external_document_ref() -> None:
    """Declared ExternalDocumentRef targets pass; undeclared prefixes fail."""
    doc = _build_spdx2_doc(
        [
            Relationship(
                "SPDXRef-Package-App",
                RelationshipType.DEPENDS_ON,
                "DocumentRef-other:SPDXRef-Package-Lib",
            )
        ]
    )
    doc.packages = doc.packages[:1]
    assert not has_spdx2_dependency_relationship(doc)

    doc.creation_info.external_document_refs = [
        ExternalDocumentRef(
            document_ref_id="DocumentRef-other",
            document_uri="https://example.com/spdx/other",
            checksum=Checksum(
                ChecksumAlgorithm.SHA1,
                "d6a770ba38583ed4bb4525bd96e50461655d2758",
            ),
        )
    ]
    assert has_spdx2_dependency_relationship(doc)
    assert has_spdx2_dependency_relationship(doc, reachable_ids={"SPDXRef-Package-App"})

    doc.relationships = [
        Relationship(
            "DocumentRef-other:SPDXRef-Package-Lib",
            RelationshipType.BUILD_DEPENDENCY_OF,
            "SPDXRef-Package-App",
        )
    ]
    assert has_spdx2_dependency_relationship(doc, reachable_ids={"SPDXRef-Package-App"})


def test_spdx2_dependency_relationship_requires_reachable_origin() -> None:
    """Relationships outside reachable_ids do not satisfy the check."""
    doc = _build_spdx2_doc(
        [
            Relationship(
                "SPDXRef-Package-Lib",
                RelationshipType.DEPENDS_ON,
                SpdxNone(),
            )
        ]
    )
    assert not has_spdx2_dependency_relationship(
        doc, reachable_ids={"SPDXRef-Package-App"}
    )

    doc.relationships = [
        Relationship(
            "SPDXRef-Package-Lib",
            RelationshipType.DEPENDS_ON,
            "SPDXRef-Package-App",
        )
    ]
    assert not has_spdx2_dependency_relationship(
        doc, reachable_ids={"SPDXRef-Package-App"}
    )


@pytest.mark.parametrize(
    "target",
    [
        "SPDXRef-Missing",
        "SPDXRef-Package-App",
    ],
)
def test_spdx2_dependency_relationship_rejects_invalid_targets(
    target: str,
) -> None:
    """Targets that are missing or self-referential return False."""
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


@pytest.mark.parametrize(
    "fixture_name",
    [
        "single_package_depends_on_none.spdx",
        "single_package_depends_on_noassertion.spdx",
    ],
)
def test_spdx2_single_package_no_dependencies_fixtures(fixture_name: str) -> None:
    """Single-package SBOM fixtures stating NONE or NOASSERTION are conformant."""
    fixture = (
        Path(__file__).parent / "data" / "spdx2_dependency_relationships" / fixture_name
    )
    sbom = SbomChecker(str(fixture), sbom_spec="spdx2")
    assert not sbom.parsing_errors
    assert not sbom.validation_messages
    assert sbom.dependency_relationships is True
    assert sbom.compliant is True


def test_spdx2_floating_packages_linked_fixture() -> None:
    """Two floating packages linked to each other do not satisfy dependency check."""
    fixture = (
        Path(__file__).parent
        / "data"
        / "spdx2_dependency_relationships"
        / "floating_packages_linked_spdx2.json"
    )
    sbom = SbomChecker(str(fixture), sbom_spec="spdx2")
    assert not sbom.parsing_errors
    assert not sbom.validation_messages
    assert sbom.reachable_component_ids == {"SPDXRef-Package-Valid"}
    assert sbom.floating_component_ids == {
        "SPDXRef-Package-Float-A",
        "SPDXRef-Package-Float-B",
    }
    assert sbom.dependency_relationships is False
    assert sbom.compliant is False


def test_spdx2_disconnected_with_dependency_fixture() -> None:
    """Floating components do not fail compliance when reachable graph states NONE."""
    fixture = (
        Path(__file__).parent
        / "data"
        / "spdx2_dependency_relationships"
        / "disconnected_with_dependency_spdx2.json"
    )
    sbom = SbomChecker(str(fixture), sbom_spec="spdx2")
    assert not sbom.parsing_errors
    assert not sbom.validation_messages
    assert sbom.reachable_component_ids == {"SPDXRef-Package-Valid"}
    assert sbom.floating_component_ids == {"SPDXRef-Package-Orphan"}
    assert sbom.dependency_relationships is True
    assert sbom.compliant is True


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


def test_spdx2_external_document_id_rejected_as_dependency(tmp_path: Path) -> None:
    """Declared ExternalDocumentRef ending in SPDXRef-DOCUMENT is not a content dep."""
    relationships: list[dict[str, str]] = [
        {
            "spdxElementId": "SPDXRef-DOCUMENT",
            "relationshipType": "DESCRIBES",
            "relatedSpdxElement": "SPDXRef-Package-App",
        },
        {
            "spdxElementId": "SPDXRef-Package-App",
            "relationshipType": "CONTAINS",
            "relatedSpdxElement": "DocumentRef-other:SPDXRef-DOCUMENT",
        },
    ]
    sbom_data: dict[str, object] = {
        "SPDXID": "SPDXRef-DOCUMENT",
        "spdxVersion": "SPDX-2.3",
        "name": "SPDX2-External-Doc-ID-Test",
        "dataLicense": "CC0-1.0",
        "documentNamespace": "https://example.com/spdx/external-doc-id",
        "creationInfo": {
            "creators": ["Organization: Example Org"],
            "created": "2026-07-04T12:00:00Z",
        },
        "externalDocumentRefs": [
            {
                "externalDocumentId": "DocumentRef-other",
                "spdxDocument": "https://example.com/spdx/other",
                "checksum": {
                    "algorithm": "SHA1",
                    "checksumValue": "d6a770ba38583ed4bb4525bd96e50461655d2758",
                },
            }
        ],
        "packages": [
            {
                "name": "app",
                "SPDXID": "SPDXRef-Package-App",
                "versionInfo": "1.0.0",
                "supplier": "Organization: Example Org",
                "downloadLocation": "NOASSERTION",
                "filesAnalyzed": False,
            }
        ],
        "relationships": relationships,
    }

    ext_doc_only = tmp_path / "external_doc_only.spdx.json"
    ext_doc_only.write_text(json.dumps(sbom_data), encoding="utf-8")

    checker = SbomChecker(str(ext_doc_only), sbom_spec="spdx2")
    assert not checker.parsing_errors
    assert not checker.validation_messages
    assert checker.has_unknown_pointers is False
    assert checker.dependency_relationships is False
    assert checker.compliant is False

    # Reverse relationship from external document ID must also fail.
    relationships[1] = {
        "spdxElementId": "DocumentRef-other:SPDXRef-DOCUMENT",
        "relationshipType": "DEPENDENCY_OF",
        "relatedSpdxElement": "SPDXRef-Package-App",
    }
    ext_doc_reverse = tmp_path / "external_doc_reverse.spdx.json"
    ext_doc_reverse.write_text(json.dumps(sbom_data), encoding="utf-8")
    checker_reverse = SbomChecker(str(ext_doc_reverse), sbom_spec="spdx2")
    assert checker_reverse.has_unknown_pointers is False
    assert checker_reverse.dependency_relationships is False


@pytest.mark.parametrize("origin_type", ["file", "snippet"])
def test_sbomchecker_accepts_reachable_file_and_snippet_dependencies(
    tmp_path: Path, origin_type: str
) -> None:
    """Reachable File and Snippet origins satisfy dependency checks in SbomChecker."""
    origin_id = "SPDXRef-File-Main" if origin_type == "file" else "SPDXRef-Snippet-1"
    sbom_data: dict[str, object] = {
        "SPDXID": "SPDXRef-DOCUMENT",
        "spdxVersion": "SPDX-2.3",
        "name": f"SPDX2-{origin_type}-Dependency-Test",
        "dataLicense": "CC0-1.0",
        "documentNamespace": "https://example.com/spdx/file-snippet-dep",
        "creationInfo": {
            "creators": ["Organization: Example Org"],
            "created": "2026-07-04T12:00:00Z",
        },
        "packages": [
            {
                "name": "lib",
                "SPDXID": "SPDXRef-Package-Lib",
                "versionInfo": "1.0.0",
                "supplier": "Organization: Example Org",
                "downloadLocation": "NOASSERTION",
                "filesAnalyzed": False,
            }
        ],
        "files": [
            {
                "fileName": "./src/main.c",
                "SPDXID": "SPDXRef-File-Main",
                "checksums": [
                    {
                        "algorithm": "SHA1",
                        "checksumValue": "d6a770ba38583ed4bb4525bd96e50461655d2758",
                    }
                ],
                "copyrightText": "NOASSERTION",
            }
        ],
        "relationships": [
            {
                "spdxElementId": "SPDXRef-DOCUMENT",
                "relationshipType": "DESCRIBES",
                "relatedSpdxElement": origin_id,
            },
            {
                "spdxElementId": origin_id,
                "relationshipType": "DEPENDS_ON",
                "relatedSpdxElement": "SPDXRef-Package-Lib",
            },
        ],
    }
    if origin_type == "snippet":
        sbom_data["snippets"] = [
            {
                "SPDXID": "SPDXRef-Snippet-1",
                "snippetFromFile": "SPDXRef-File-Main",
                "ranges": [
                    {
                        "startPointer": {
                            "offset": 1,
                            "reference": "SPDXRef-File-Main",
                        },
                        "endPointer": {
                            "offset": 10,
                            "reference": "SPDXRef-File-Main",
                        },
                    }
                ],
                "copyrightText": "NOASSERTION",
            }
        ]

    sbom_path = tmp_path / f"{origin_type}_dep.spdx.json"
    sbom_path.write_text(json.dumps(sbom_data), encoding="utf-8")

    checker = SbomChecker(str(sbom_path), sbom_spec="spdx2")
    assert not checker.parsing_errors
    assert not checker.validation_messages
    assert origin_id in checker.reachable_node_ids
    assert "SPDXRef-Package-Lib" in checker.reachable_component_ids
    assert checker.dependency_relationships is True
    assert checker.compliant is True
