import os

import pytest

from ntia_conformance_checker.main import SbomChecker

DATA_DIR = os.path.join(os.path.dirname(__file__), "data", "real_world_sboms")


def get_sbom_files():
    """
    Returns a list of all files in tests/data/real_world
    so pytest can generate a test case for each one.
    """
    if not os.path.exists(DATA_DIR):
        return []

    files = [
        f for f in os.listdir(DATA_DIR) if os.path.isfile(os.path.join(DATA_DIR, f))
    ]

    return [f for f in files if not f.startswith(".")]


@pytest.mark.parametrize("filename", get_sbom_files())
def test_real_world_robustness(filename):
    """
    Test that the checker does not CRASH on real-world inputs.
    We do not expect these to be compliant; we just want no unhandled exceptions.
    """
    filepath = os.path.join(DATA_DIR, filename)
    print(f"\nTesting file: {filename}")

    try:
        sbom = SbomChecker(filepath)
        is_compliant = sbom.compliant
        assert isinstance(is_compliant, bool)

    except Exception as e:
        pytest.fail(f"CRASHED on {filename} with error: {e}")
