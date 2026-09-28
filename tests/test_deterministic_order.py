# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests that SPDX 3 component lists are ordered independent of hash seed."""

import os
import subprocess
import sys
from pathlib import Path

SBOM_FILE = Path(__file__).parent / "data" / "spdx3" / "has_sbom.json"
SCRIPT = (
    "import sys; from ntia_conformance_checker.ntia_checker import NTIAChecker; "
    "c = NTIAChecker(sys.argv[1], sbom_spec='spdx3'); "
    "print([n for n, _ in c.components_without_concluded_licenses])"
)


def test_spdx3_component_order_independent_of_hash_seed() -> None:
    """Component list is sorted and identical under different hash seeds."""
    outputs = {
        subprocess.run(
            [sys.executable, "-c", SCRIPT, str(SBOM_FILE)],
            capture_output=True,
            check=True,
            env={**os.environ, "PYTHONHASHSEED": seed},
            text=True,
        ).stdout
        for seed in ("0", "1", "2")
    }
    assert outputs == {
        "['Acme Application', 'alpine:latest', 'npm-elliptic', 'openssl']\n"
    }
