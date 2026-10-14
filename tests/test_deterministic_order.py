# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests that SPDX 3 component lists are ordered the same across runs."""

import subprocess
import sys
from pathlib import Path

SBOM_FILE = Path(__file__).parent / "data" / "spdx3" / "has_sbom.json"
SCRIPT = (
    "import sys; from ntia_conformance_checker.ntia_checker import NTIAChecker; "
    "c = NTIAChecker(sys.argv[1], sbom_spec='spdx3'); "
    "print([n for n, _ in c.components_without_concluded_licenses])"
)


def test_spdx3_component_order_stable_across_runs() -> None:
    """Component list is sorted and identical across separate processes."""
    outputs = {
        subprocess.run(
            [sys.executable, "-c", SCRIPT, str(SBOM_FILE)],
            capture_output=True,
            check=True,
            text=True,
        ).stdout
        for _ in range(3)
    }
    assert outputs == {
        "['Acme Application', 'alpine:latest', 'npm-elliptic', 'openssl']\n"
    }
