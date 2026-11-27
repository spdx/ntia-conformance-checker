# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for "Dependency relationships provided?" in SPDX 2 and SPDX 3"""

# pylint: disable=missing-function-docstring

import json
from pathlib import Path

import pytest

from ntia_conformance_checker.constants import (
    SPDX2_DEPENDENCY_RELATIONSHIP_TYPES,
    SPDX2_RELATIONSHIP_TRAVERSAL,
    SPDX3_DEPENDENCY_RELATIONSHIP_TYPES,
    SPDX3_RELATIONSHIP_TRAVERSAL,
    TraversalDirection,
)
from ntia_conformance_checker.sbom_checker import SbomChecker

DATA = Path(__file__).parent / "data"
EXT_REF = (
    "ExternalDocumentRef: DocumentRef-other https://example.com/spdxdocs/other-1 "
    "SHA1: 0123456789abcdef0123456789abcdef01234567"
)


def _spdx2_checker(
    tmp_path: Path,
    relationships: list[str],
    packages: tuple[str, ...] = ("App",),
    files: tuple[str, ...] = (),
) -> SbomChecker:
    """Check an SPDX 2 tag-value SBOM that describes the first package."""
    lines = [
        "SPDXVersion: SPDX-2.3",
        "DataLicense: CC0-1.0",
        "SPDXID: SPDXRef-DOCUMENT",
        "DocumentName: test",
        "DocumentNamespace: https://example.com/spdxdocs/test",
        EXT_REF,
        "Creator: Tool: test",
        "Created: 2026-01-01T00:00:00Z",
        "",
        f"Relationship: SPDXRef-DOCUMENT DESCRIBES SPDXRef-{packages[0]}",
        *(f"Relationship: {r}" for r in relationships),
    ]
    for name in files:
        lines += [
            "",
            f"FileName: ./{name}",
            f"SPDXID: SPDXRef-{name}",
            "FileChecksum: SHA1: 0123456789abcdef0123456789abcdef01234567",
        ]
    for name in packages:
        lines += [
            "",
            f"PackageName: {name}",
            f"SPDXID: SPDXRef-{name}",
            "PackageVersion: 1.0",
            "PackageSupplier: Organization: Example",
            "PackageDownloadLocation: NOASSERTION",
            "FilesAnalyzed: false",
        ]
    path = tmp_path / "sbom.spdx"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    checker: SbomChecker = SbomChecker(str(path))
    assert not checker.parsing_errors
    return checker


def test_dependency_types_are_followed_types() -> None:
    assert SPDX3_DEPENDENCY_RELATIONSHIP_TYPES <= set(SPDX3_RELATIONSHIP_TRAVERSAL)
    assert SPDX2_DEPENDENCY_RELATIONSHIP_TYPES <= set(SPDX2_RELATIONSHIP_TRAVERSAL)


@pytest.mark.parametrize("rel_type", sorted(SPDX2_DEPENDENCY_RELATIONSHIP_TYPES))
def test_spdx2_each_dependency_type_counts(tmp_path: Path, rel_type: str) -> None:
    """Each counted type counts when written from App, in its own direction."""
    along = SPDX2_RELATIONSHIP_TRAVERSAL[rel_type] is TraversalDirection.ALONG
    rel = (
        f"SPDXRef-App {rel_type} SPDXRef-Lib"
        if along
        else f"SPDXRef-Lib {rel_type} SPDXRef-App"
    )
    checker = _spdx2_checker(tmp_path, [rel], packages=("App", "Lib"))
    assert checker.dependency_relationships is True


@pytest.mark.parametrize(
    ("relationships", "expected"),
    [
        (["SPDXRef-App DEPENDS_ON NONE"], True),
        (["SPDXRef-App DEPENDS_ON NOASSERTION"], True),
        (["SPDXRef-App DEPENDS_ON DocumentRef-other:SPDXRef-Lib"], True),
        (["DocumentRef-other:SPDXRef-Lib DEPENDENCY_OF SPDXRef-App"], True),
        (["SPDXRef-App DEPENDS_ON DocumentRef-other:SPDXRef-DOCUMENT"], False),
        (["SPDXRef-App DEPENDS_ON DocumentRef-nope:SPDXRef-Lib"], False),
        (["SPDXRef-App DEPENDS_ON SPDXRef-Missing"], False),
        (
            [
                "SPDXRef-DOCUMENT DESCRIBES SPDXRef-Missing",
                "SPDXRef-Missing DEPENDS_ON NONE",
            ],
            False,
        ),
        (["SPDXRef-App DEPENDENCY_OF NONE"], False),
        (["SPDXRef-App DEPENDS_ON SPDXRef-App"], False),
        (["SPDXRef-Tool OPTIONAL_COMPONENT_OF SPDXRef-App"], True),
        (["SPDXRef-DOCUMENT CONTAINS SPDXRef-App"], False),
        (["SPDXRef-Tool BUILD_TOOL_OF SPDXRef-App"], False),
        (["SPDXRef-Tool DEPENDS_ON SPDXRef-App"], False),
        ([], False),
    ],
    ids=[
        "none",
        "noassertion",
        "external",
        "external-reverse",
        "external-document-itself",
        "undeclared-prefix",
        "missing",
        "missing-origin",
        "reverse-to-none",
        "self",
        "optional-component",
        "document",
        "tool-only",
        "unreachable-origin",
        "describes-only",
    ],
)
def test_spdx2_dependency_relationship_rule(
    tmp_path: Path, relationships: list[str], expected: bool
) -> None:
    checker = _spdx2_checker(tmp_path, relationships, packages=("App", "Tool"))
    assert checker.dependency_relationships is expected


@pytest.mark.parametrize(
    "relationships",
    [
        ["SPDXRef-DOCUMENT DESCRIBES SPDXRef-F", "SPDXRef-F DEPENDS_ON SPDXRef-App"],
        ["SPDXRef-App CONTAINS SPDXRef-F"],
    ],
    ids=["from-file", "to-file"],
)
def test_spdx2_dependency_relationship_with_file(
    tmp_path: Path, relationships: list[str]
) -> None:
    """A file is an element that a relationship may link (SPDX 2.3.1 clause 11.1)."""
    checker = _spdx2_checker(tmp_path, relationships, files=("F",))
    assert checker.dependency_relationships is True
    assert checker.floating_component_ids == set()


@pytest.mark.parametrize(
    ("file_path", "dependency", "compliant"),
    [
        ("dependency_relationships/single_package_depends_on_none.spdx", True, True),
        (
            "dependency_relationships/single_package_depends_on_noassertion.spdx",
            True,
            True,
        ),
        ("dependency_relationships/floating_packages_linked_spdx2.json", False, False),
        (
            "dependency_relationships/disconnected_with_dependency_spdx2.json",
            True,
            True,
        ),
        (
            "graph_connectivity/reverse_relationship/issue481_build_dependency_of.spdx",
            True,
            True,
        ),
        (
            "graph_connectivity/external_document_ref/issue482_external_document_ref.spdx",
            True,
            True,
        ),
    ],
    ids=[
        "none",
        "noassertion",
        "floating-pair",
        "floating-orphan",
        "issue-481",
        "issue-482",
    ],
)
def test_spdx2_dependency_relationship_files(
    file_path: str, dependency: bool, compliant: bool
) -> None:
    checker = SbomChecker(str(DATA / file_path))
    assert checker.dependency_relationships is dependency
    assert checker.compliant is compliant


@pytest.mark.parametrize(
    ("from_id", "to_id", "expected"),
    [
        ("APP", "https://spdx.org/rdf/3.0.1/terms/Core/NoneElement", True),
        ("APP", "https://spdx.org/rdf/3.0.1/terms/Core/NoAssertionElement", True),
        ("APP", "https://example.com/imported", True),
        ("APP", "https://example.com/missing", False),
        ("LIB", "APP", False),
    ],
    ids=["none", "noassertion", "imported", "missing", "unreachable-origin"],
)
def test_spdx3_dependency_relationship_rule(
    tmp_path: Path, from_id: str, to_id: str, expected: bool
) -> None:
    """Only the application package is a root; the library is floating."""
    src = DATA / "spdx3" / "package_dependency_relationship.json"
    doc = json.loads(src.read_text(encoding="utf-8"))
    ids = {
        "APP": "https://spdx.org/spdxdocs/Package-application",
        "LIB": "https://spdx.org/spdxdocs/Package-library",
    }
    spdx_doc = next(e for e in doc["@graph"] if e["type"] == "SpdxDocument")
    spdx_doc["import"] = [
        {"type": "ExternalMap", "externalSpdxId": "https://example.com/imported"}
    ]
    relationship = next(e for e in doc["@graph"] if e["type"] == "Relationship")
    relationship["from"] = ids.get(from_id, from_id)
    relationship["to"] = [ids.get(to_id, to_id)]
    path = tmp_path / "sbom.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    checker = SbomChecker(str(path), sbom_spec="spdx3")
    assert checker.dependency_relationships is expected


def test_spdx3_dependency_relationship_id_like_spdx2_document(
    tmp_path: Path,
) -> None:
    """An SPDX 3 ID is any IRI; one ending in :SPDXRef-DOCUMENT is no document."""
    src = DATA / "spdx3" / "package_dependency_relationship.json"
    text = src.read_text(encoding="utf-8").replace(
        "https://spdx.org/spdxdocs/Package-library",
        "urn:example:library:SPDXRef-DOCUMENT",
    )
    path = tmp_path / "sbom.json"
    path.write_text(text, encoding="utf-8")
    checker = SbomChecker(str(path), sbom_spec="spdx3")
    assert checker.dependency_relationships is True


def _spdx3_package_dependency_checker(
    tmp_path: Path, relationship_type: str, from_id: str = "", to_id: str = ""
) -> SbomChecker:
    """Check package_dependency_relationship.json with its relationship changed."""
    test_file = DATA / "spdx3" / "package_dependency_relationship.json"
    doc = json.loads(test_file.read_text(encoding="utf-8"))
    relationship = next(e for e in doc["@graph"] if e["type"] == "Relationship")
    relationship["relationshipType"] = relationship_type
    if from_id:
        relationship["from"] = from_id
    if to_id:
        relationship["to"] = [to_id]
    path = tmp_path / "sbom.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    checker: SbomChecker = SbomChecker(str(path), sbom_spec="spdx3")
    return checker


@pytest.mark.parametrize(
    ("relationship_type", "expected"),
    [
        ("dependsOn", True),
        ("hasDynamicLink", True),
        ("hasStaticLink", True),
        ("contains", True),
        ("hasOptionalComponent", True),
        ("hasOptionalDependency", True),
        ("hasProvidedDependency", True),
        ("hasPrerequisite", True),
        # Followed, but not a dependency relationship
        ("usesTool", False),
        ("trainedOn", False),
        ("generates", False),
        # Not followed
        ("other", False),
    ],
)
def test_spdx3_dependency_relationship_types(
    tmp_path: Path, relationship_type: str, expected: bool
) -> None:
    sbom = _spdx3_package_dependency_checker(tmp_path, relationship_type)
    assert sbom.dependency_relationships is expected


def test_spdx3_dependency_relationship_rejects_collection_endpoints(
    tmp_path: Path,
) -> None:
    """An Sbom is a collection, so "Sbom contains X" does not count."""
    sbom = _spdx3_package_dependency_checker(
        tmp_path,
        "contains",
        from_id="https://spdx.org/spdxdocs/SBOM-package-dependency",
        to_id="https://spdx.org/spdxdocs/Package-library",
    )
    assert sbom.dependency_relationships is False
