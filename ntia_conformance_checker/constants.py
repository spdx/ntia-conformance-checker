# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Constants."""

from .registry import descriptions

SUPPORTED_SBOM_SPECS_DESC = {
    "spdx2": "Software Package Data Exchange (SPDX) 2.x",
    "spdx3": "System Package Data Exchange (SPDX) 3.x",
}
DEFAULT_SBOM_SPEC = "spdx2"
SUPPORTED_SBOM_SPECS = set(SUPPORTED_SBOM_SPECS_DESC.keys())

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

# Ids that older releases accepted for a renamed standard -> current id.
DEPRECATED_COMPLIANCE_IDS = {"fsct3-min": "fsct3"}

# Standards defined by rules/*.yaml take their description from the spec title;
# standards implemented in code are listed here.
SUPPORTED_COMPLIANCE_STANDARDS_DESC = {
    "bsi": "BSI TR-03183-2 v2.1.0 Cyber Resilience Requirements for Manufacturers and Products",
    **descriptions(),
}
SUPPORTED_COMPLIANCE_STANDARDS_DESC.update(
    {
        old: SUPPORTED_COMPLIANCE_STANDARDS_DESC[new]
        for old, new in DEPRECATED_COMPLIANCE_IDS.items()
    }
)
DEFAULT_COMPLIANCE_STANDARD = "ntia"
SUPPORTED_COMPLIANCE_STANDARDS = set(SUPPORTED_COMPLIANCE_STANDARDS_DESC.keys())

SUPPORTED_SPDX_VERSIONS = {(2, 2), (2, 3), (3, 0)}  # (Major, Minor)
SUPPORTED_SPDX2_VERSION_STRINGS = {
    f"SPDX-{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 2
}  # e.g. "SPDX-2.2", "SPDX-2.3"
SUPPORTED_SPDX3_VERSION_STRINGS = {
    f"{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 3
}  # e.g. "3.0"
