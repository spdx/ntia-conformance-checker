# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Constants."""

from enum import Enum

SUPPORTED_SBOM_SPECS_DESC = {
    "spdx2": "Software Package Data Exchange (SPDX) 2.x",
    "spdx3": "System Package Data Exchange (SPDX) 3.x",
}
DEFAULT_SBOM_SPEC = "spdx2"
SUPPORTED_SBOM_SPECS = set(SUPPORTED_SBOM_SPECS_DESC.keys())


class TraversalDirection(Enum):
    """
    Direction in which graph traversal follows a relationship type.

    Traversal goes from the parent (the element closer to the root) to the
    child. ``FORWARD`` follows a relationship from its source
    (SPDX 2 ``spdxElementId``, SPDX 3 ``from``) to its target
    (SPDX 2 ``relatedSpdxElement``, SPDX 3 ``to``). ``REVERSE`` follows it
    from its target to its source.
    """

    FORWARD = "forward"
    REVERSE = "reverse"


# SPDX 3 relationship types that connect an element to the graph,
# with their traversal direction. Descriptions are from the SPDX 3.0.1
# RelationshipType vocabulary.
SPDX3_RELATIONSHIP_TRAVERSAL: dict[str, TraversalDirection] = {
    # Composition
    "contains": TraversalDirection.FORWARD,
    "hasOptionalComponent": TraversalDirection.FORWARD,
    "packagedBy": TraversalDirection.FORWARD,
    # Dependencies
    "dependsOn": TraversalDirection.FORWARD,
    "hasDynamicLink": TraversalDirection.FORWARD,
    "hasStaticLink": TraversalDirection.FORWARD,
    "hasPrerequisite": TraversalDirection.FORWARD,
    "hasOptionalDependency": TraversalDirection.FORWARD,
    "hasProvidedDependency": TraversalDirection.FORWARD,
    # Tools: "The from Element uses each to Element as a tool".
    # The from Element is the product, so traversal goes from it to the tool.
    "usesTool": TraversalDirection.FORWARD,
    # Provenance: "The from Element generates each to Element".
    # The to Element is the product and the from Element is its source,
    # so traversal goes from the product to the source, against the
    # relationship direction.
    "generates": TraversalDirection.REVERSE,
}

# Translation of SPDX 2.3 relationship types to SPDX 3.0:
# SPDX 2 type -> (SPDX 3 type, swap to and from?). Copied as published from
# Using SPDX, "Differences between V3.0 and V2.3" > Structural Differences >
# Relationship > "Translating from 2.3 to 3.0" (non-normative), at
# spdx/using commit 80eba34, which corrects the DYNAMIC_LINK and
# FILE_MODIFIED rows (spdx/using#30):
# https://github.com/spdx/using/blob/80eba34d23f48e242a54a78b584e7a87ad2b9afa/docs/diff/v2.3-v3.0.md#translating-from-23-to-30-8
# Earlier editions were SPDX 3.0 Annex A.1.
SPDX2_TO_SPDX3_RELATIONSHIP_TYPES: dict[str, tuple[str, bool]] = {
    "AMENDS": ("amendedBy", True),
    "ANCESTOR_OF": ("ancestorOf", False),
    "BUILD_DEPENDENCY_OF": ("dependsOn", True),
    "BUILD_TOOL_OF": ("usesTool", True),
    "CONTAINED_BY": ("contains", True),
    "CONTAINS": ("contains", False),
    "COPY_OF": ("copiedTo", True),
    "DATA_FILE_OF": ("hasDataFile", True),
    "DEPENDENCY_MANIFEST_OF": ("hasDependencyManifest", True),
    "DEPENDENCY_OF": ("dependsOn", True),
    "DEPENDS_ON": ("dependsOn", False),
    "DESCENDANT_OF": ("descendantOf", False),
    "DESCRIBED_BY": ("describes", True),
    "DESCRIBES": ("describes", False),
    "DEV_DEPENDENCY_OF": ("dependsOn", True),
    "DEV_TOOL_OF": ("usesTool", True),
    "DISTRIBUTION_ARTIFACT": ("hasDistributionArtifact", False),
    "DOCUMENTATION_OF": ("hasDocumentation", True),
    "DYNAMIC_LINK": ("hasDynamicLink", False),
    "EXAMPLE_OF": ("hasExample", True),
    "EXPANDED_FROM_ARCHIVE": ("expandsTo", True),
    "FILE_ADDED": ("hasAddedFile", True),
    "FILE_DELETED": ("hasDeletedFile", True),
    "FILE_MODIFIED": ("modifiedBy", True),
    "GENERATED_FROM": ("generates", True),
    "GENERATES": ("generates", False),
    "HAS_PREREQUISITE": ("hasPrerequisite", False),
    "METAFILE_OF": ("hasMetadata", True),
    "OPTIONAL_COMPONENT_OF": ("hasOptionalComponent", True),
    "OPTIONAL_DEPENDENCY_OF": ("hasOptionalDependency", True),
    "OTHER": ("other", False),
    "PACKAGE_OF": ("packagedBy", True),
    "PATCH_FOR": ("patchedBy", True),
    "PATCH_APPLIED": ("patchedBy", True),
    "PREREQUISITE_FOR": ("hasPrerequisite", True),
    "PROVIDED_DEPENDENCY_OF": ("hasProvidedDependency", True),
    "REQUIREMENT_DESCRIPTION_FOR": ("hasRequirement", True),
    "RUNTIME_DEPENDENCY_OF": ("dependsOn", True),
    "SPECIFICATION_FOR": ("hasSpecification", True),
    "STATIC_LINK": ("hasStaticLink", False),
    "TEST_CASE_OF": ("hasTestCase", True),
    "TEST_DEPENDENCY_OF": ("dependsOn", True),
    "TEST_OF": ("hasTest", True),
    "TEST_TOOL_OF": ("usesTool", True),
    "VARIANT_OF": ("hasVariant", True),
}

# SPDX 2 relationship types whose traversal is not derived from
# SPDX2_TO_SPDX3_RELATIONSHIP_TYPES:
# - DESCRIBES and DESCRIBED_BY: SPDX 3 marks roots with rootElement, so
#   describes is not in SPDX3_RELATIONSHIP_TRAVERSAL. SPDX 2 has no
#   rootElement. "SPDXRef-DOCUMENT DESCRIBES SPDXRef-A" and
#   "SPDXRef-A DESCRIBED_BY SPDXRef-DOCUMENT" (Table 68) mark roots, and
#   between other elements they are followed from the describing element to
#   the described one, so either form connects the same elements.
SPDX2_RELATIONSHIP_TRAVERSAL_OVERRIDES: dict[str, TraversalDirection] = {
    "DESCRIBES": TraversalDirection.FORWARD,
    "DESCRIBED_BY": TraversalDirection.REVERSE,
}


def _derive_spdx2_relationship_traversal() -> dict[str, TraversalDirection]:
    """
    Derive SPDX 2 traversal directions from their SPDX 3 translations.

    An SPDX 2 type is followed when its SPDX 3 translation is in
    ``SPDX3_RELATIONSHIP_TRAVERSAL``. Its direction is the SPDX 3 direction,
    flipped when the translation table swaps ``to`` and ``from``. This keeps
    SPDX 2 and
    SPDX 3 results the same for the same SBOM.

    Returns:
        dict[str, TraversalDirection]: SPDX 2 type name to direction.
    """
    flipped = {
        TraversalDirection.FORWARD: TraversalDirection.REVERSE,
        TraversalDirection.REVERSE: TraversalDirection.FORWARD,
    }
    traversal: dict[str, TraversalDirection] = {}
    for spdx2_type, (spdx3_type, swap) in SPDX2_TO_SPDX3_RELATIONSHIP_TYPES.items():
        direction = SPDX3_RELATIONSHIP_TRAVERSAL.get(spdx3_type)
        if direction is not None:
            traversal[spdx2_type] = flipped[direction] if swap else direction
    traversal.update(SPDX2_RELATIONSHIP_TRAVERSAL_OVERRIDES)
    return traversal


# SPDX 2 relationship types that connect an element to the graph,
# with their traversal direction.
SPDX2_RELATIONSHIP_TRAVERSAL: dict[str, TraversalDirection] = (
    _derive_spdx2_relationship_traversal()
)

# Deprecated: the relationship types that version 6.0.0 followed, kept
# unchanged for compatibility. The checker no longer uses them; use
# SPDX2_RELATIONSHIP_TRAVERSAL and SPDX3_RELATIONSHIP_TRAVERSAL to get every
# followed type with its direction.
VALID_SPDX2_COMPOSITION_RELATIONSHIPS = {
    "DESCRIBES",
    "CONTAINS",
    "DEPENDS_ON",
    "DYNAMIC_LINK",
    "STATIC_LINK",
    "HAS_PREREQUISITE",
}
VALID_SPDX3_COMPOSITION_RELATIONSHIPS = {
    # Composition
    "contains",
    "hasOptionalComponent",
    "packagedBy",
    # Dependencies
    "dependsOn",
    "hasDynamicLink",
    "hasStaticLink",
    "hasPrerequisite",
    "hasOptionalDependency",
    "hasProvidedDependency",
}

SUPPORTED_COMPLIANCE_STANDARDS_DESC = {
    # "cisasbom2025": "2025 CISA SBOM Minimum Elements",
    # https://www.cisa.gov/resources-tools/resources/2025-minimum-elements-software-bill-materials-sbom
    "bsi": "BSI TR-03183-2 v2.1.0 Cyber Resilience Requirements for Manufacturers and Products",
    "fsct3-min": "2024 CISA Framing Software Component Transparency (minimum expectation)",
    "ntia": "2021 NTIA SBOM Minimum Elements",
}
DEFAULT_COMPLIANCE_STANDARD = "ntia"
SUPPORTED_COMPLIANCE_STANDARDS = set(SUPPORTED_COMPLIANCE_STANDARDS_DESC.keys())

SUPPORTED_SPDX_VERSIONS = {(2, 2), (2, 3), (3, 0)}  # (Major, Minor)
SUPPORTED_SPDX2_VERSION_STRINGS = {
    f"SPDX-{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 2
}  # e.g. "SPDX-2.2", "SPDX-2.3"
SUPPORTED_SPDX3_VERSION_STRINGS = {
    f"{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 3
}  # e.g. "3.0"
