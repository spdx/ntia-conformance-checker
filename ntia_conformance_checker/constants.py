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
    How traversal walks a relationship type, from parent to child.

    ``ALONG`` walks it as written, from source (SPDX 2 ``spdxElementId``,
    SPDX 3 ``from``) to target (``relatedSpdxElement``, ``to``); ``AGAINST``
    walks it from target to source. This is the checker's choice, not a
    property of the type: e.g. ``generates`` is not a reverse type.
    """

    ALONG = "along"
    AGAINST = "against"


# SPDX 3 relationship types the traversal follows, with their direction.
# Quotes: SPDX 3.0.1 Core/Vocabularies/RelationshipType.
SPDX3_RELATIONSHIP_TRAVERSAL: dict[str, TraversalDirection] = {
    # Composition
    "contains": TraversalDirection.ALONG,
    "hasOptionalComponent": TraversalDirection.ALONG,
    "packagedBy": TraversalDirection.ALONG,
    # Dependencies
    "dependsOn": TraversalDirection.ALONG,
    "hasDynamicLink": TraversalDirection.ALONG,
    "hasStaticLink": TraversalDirection.ALONG,
    "hasPrerequisite": TraversalDirection.ALONG,
    "hasOptionalDependency": TraversalDirection.ALONG,
    "hasProvidedDependency": TraversalDirection.ALONG,
    # Inputs (tools, sources): walked from the product to the input, as for
    # dependencies. Following them is our reading, not a minimum elements
    # requirement (see FAQ.md).
    # "The from Element uses each to Element as a tool": product first.
    "usesTool": TraversalDirection.ALONG,
    # "The from Element generates each to Element": source first, so walked
    # against. Not both ways, or a shared source would link its products.
    "generates": TraversalDirection.AGAINST,
}

# SPDX 2 type -> (SPDX 3 type, swap to and from?), copied as published from
# Using SPDX, "Differences between V3.0 and V2.3" > Relationship >
# "Translating from 2.3 to 3.0" (non-normative; formerly SPDX 3.0 Annex A.1)
# at spdx/using 80eba34, with the rows corrected in spdx/using#30:
# https://github.com/spdx/using/blob/80eba34d23f48e242a54a78b584e7a87ad2b9afa/docs/diff/v2.3-v3.0.md#translating-from-23-to-30-8
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

# SPDX 2 types not derived from the table. SPDX 2 has no rootElement, so
# DESCRIBES and DESCRIBED_BY mark roots (SPDX 2.3 §11.1 Table 68) and,
# between other elements, are walked from describer to described; SPDX 3
# does not follow describes.
SPDX2_RELATIONSHIP_TRAVERSAL_OVERRIDES: dict[str, TraversalDirection] = {
    "DESCRIBES": TraversalDirection.ALONG,
    "DESCRIBED_BY": TraversalDirection.AGAINST,
}


def _derive_spdx2_relationship_traversal() -> dict[str, TraversalDirection]:
    """
    Derive SPDX 2 traversal directions from their SPDX 3 translations.

    An SPDX 2 type is followed if its SPDX 3 type is, in the same direction,
    flipped when the table swaps ``to`` and ``from``, so SPDX 2 and SPDX 3
    give the same result.

    Returns:
        dict[str, TraversalDirection]: SPDX 2 type name to direction.
    """
    flipped = {
        TraversalDirection.ALONG: TraversalDirection.AGAINST,
        TraversalDirection.AGAINST: TraversalDirection.ALONG,
    }
    traversal: dict[str, TraversalDirection] = {}
    for spdx2_type, (spdx3_type, swap) in SPDX2_TO_SPDX3_RELATIONSHIP_TYPES.items():
        direction = SPDX3_RELATIONSHIP_TRAVERSAL.get(spdx3_type)
        if direction is not None:
            traversal[spdx2_type] = flipped[direction] if swap else direction
    traversal.update(SPDX2_RELATIONSHIP_TRAVERSAL_OVERRIDES)
    return traversal


# SPDX 2 relationship types the traversal follows, with their direction.
SPDX2_RELATIONSHIP_TRAVERSAL: dict[str, TraversalDirection] = (
    _derive_spdx2_relationship_traversal()
)

# Deprecated: the types 6.0.0 followed, unchanged and unused. Use
# SPDX2_RELATIONSHIP_TRAVERSAL and SPDX3_RELATIONSHIP_TRAVERSAL.
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
    # AI and Dataset
    "trainedOn",
    "testedOn",
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
