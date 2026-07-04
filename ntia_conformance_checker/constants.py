# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Constants."""

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

SUPPORTED_COMPLIANCE_STANDARDS_DESC = {
    # "cisasbom2025": "2025 CISA SBOM Minimum Elements",
    # https://www.cisa.gov/resources-tools/resources/2025-minimum-elements-software-bill-materials-sbom
    "fsct3-min": "2024 CISA Framing Software Component Transparency (minimum expectation)",
    "ntia": "2021 NTIA SBOM Minimum Elements",
}
DEFAULT_COMPLIANCE_STANDARD = "ntia"
SUPPORTED_COMPLIANCE_STANDARDS = set(SUPPORTED_COMPLIANCE_STANDARDS_DESC.keys())

SUPPORTED_SPDX_VERSIONS = {(2, 2), (2, 3), (3, 0), (3, 1)}  # (Major, Minor)
SUPPORTED_SPDX2_VERSION_STRINGS = {
    f"SPDX-{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 2
}  # e.g. "SPDX-2.2", "SPDX-2.3"
SUPPORTED_SPDX3_VERSION_STRINGS = {
    f"{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 3
}  # e.g. "3.0"
SPDX3_MODEL_BINDINGS_MAP = {
    (3, 0): "v3_0_1",
    (3, 1): "v3_1",
}
