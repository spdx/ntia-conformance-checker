# SPDX-FileCopyrightText: 2025-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Constants."""

from .registry import descriptions as _descriptions

TOOL_NAME = "ntia-conformance-checker"
TOOL_URI = "https://github.com/spdx/ntia-conformance-checker"

try:
    from ._version import version as _v

    TOOL_VERSION: str = _v
except ImportError:
    TOOL_VERSION = "unknown"

SUPPORTED_SBOM_SPECS_DESC = {
    "spdx2": "Software Package Data Exchange (SPDX) 2.x",
    "spdx3": "System Package Data Exchange (SPDX) 3.x",
}
DEFAULT_SBOM_SPEC = "spdx2"
SUPPORTED_SBOM_SPECS = set(SUPPORTED_SBOM_SPECS_DESC.keys())

# Supported compliance standards are discovered from the packaged
# ``rules/*.yaml`` files by the registry -- each spec's ``id`` is
# the compliance id and its ``title`` is the human description.  Adding a
# new YAML is all that is needed to extend these; no edit here.
SUPPORTED_COMPLIANCE_STANDARDS_DESC = _descriptions()
DEFAULT_COMPLIANCE_STANDARD = "ntia"
SUPPORTED_COMPLIANCE_STANDARDS = set(SUPPORTED_COMPLIANCE_STANDARDS_DESC.keys())

SUPPORTED_SPDX_VERSIONS = {(2, 2), (2, 3), (3, 0)}  # (Major, Minor)
SUPPORTED_SPDX2_VERSION_STRINGS = {
    f"SPDX-{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 2
}  # e.g. "SPDX-2.2", "SPDX-2.3"
SUPPORTED_SPDX3_VERSION_STRINGS = {
    f"{maj}.{min}" for (maj, min) in SUPPORTED_SPDX_VERSIONS if maj == 3
}  # e.g. "3.0"
