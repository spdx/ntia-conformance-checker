# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Tests for BaseChecker per-instance state when parsing fails."""

from pathlib import Path

import pytest

from ntia_conformance_checker import NTIAChecker
from ntia_conformance_checker.base_checker import BaseChecker
from ntia_conformance_checker.fsct_checker import FSCT3Checker

LIST_ATTRS = [
    "components_without_names",
    "components_without_versions",
    "components_without_suppliers",
    "components_without_identifiers",
    "components_without_concluded_licenses",
    "components_without_copyright_texts",
    "all_components_without_info",
    "sbom_gen_context",
]


@pytest.mark.parametrize("checker_cls", [NTIAChecker, FSCT3Checker])
@pytest.mark.parametrize("sbom_spec", ["spdx2", "spdx3"])
@pytest.mark.parametrize("attr", LIST_ATTRS)
def test_failed_parse_lists_are_per_instance(
    tmp_path: Path, checker_cls: type[BaseChecker], sbom_spec: str, attr: str
) -> None:
    """Result lists must not be shared between checkers when parsing fails."""
    garbage = tmp_path / "garbage.json"
    garbage.write_text("{not json", encoding="utf-8")

    first = checker_cls(str(garbage), sbom_spec=sbom_spec)
    assert first.doc is None
    assert getattr(first, attr) == []

    getattr(first, attr).append(("leaked", "SPDXRef-leaked"))
    second = checker_cls(str(garbage), sbom_spec=sbom_spec)

    assert getattr(second, attr) == []
    assert not getattr(BaseChecker, attr, [])
