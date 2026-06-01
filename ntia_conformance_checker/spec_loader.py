# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""YAML -> :class:`Spec` loader for the declarative-rules engine.

Each spec lives in :file:`ntia_conformance_checker/rules/<spec>.yaml` with
the schema:

.. code-block:: yaml

    spec:
        spec_id: ntia                            # machine id; uppercased -> SPEC segment
        spec_title: 2021 NTIA SBOM Minimum Elements
        spec_uri: https://...
        sarif_category_taxonomy_name: ntia-minimum-elements
        sarif_clause_taxonomy_name: ntia-clauses

    categories:
        - id: data-fields
          code: DF
          title: Data Fields
          description: ...

    rules:                                       # id SBOM-NTIA-DF-001 is derived
        - number: 1
          slug: ntia-component-supplier-name
          spec_category: data-fields
          element_id: supplier
          ...
          probe:
            name: require_component_attribute
            params: { attribute: supplier }
"""

from __future__ import annotations

import re
from dataclasses import fields
from pathlib import Path
from typing import Any

import yaml

from .spec import ProbeRef, Spec, SpecCategory, SpecRule

_SPEC_ALLOWED = {f.name for f in fields(Spec)} - {"categories", "rules"}
_CATEGORY_ALLOWED = {f.name for f in fields(SpecCategory)}
_RULE_ALLOWED = {f.name for f in fields(SpecRule)} - {"probe"}

# spec_id is uppercased into the SPEC segment of every rule id, so it must be a
# hyphen-free, uppercase-safe token (start with a letter, then letters/digits).
_SPEC_ID_RE = re.compile(r"^[a-z][a-z0-9]*$")


def load_spec(path: str | Path) -> Spec:
    """Load and validate a spec YAML file, returning a :class:`Spec` instance.

    Raises:
        FileNotFoundError: ``path`` does not exist.
        SpecLoadError: the file is syntactically valid YAML but does not
            match the expected schema (unknown keys, missing required
            fields, malformed probe reference, etc).
    """
    yaml_path = Path(path)
    text = yaml_path.read_text(encoding="utf-8")
    raw = yaml.safe_load(text)
    if not isinstance(raw, dict):
        raise SpecLoadError(f"{yaml_path}: top-level must be a mapping")

    spec_block = _require_mapping(raw, "spec", yaml_path)
    _reject_unknown(spec_block, _SPEC_ALLOWED, "spec", yaml_path)

    spec_id = spec_block.get("spec_id")
    if not isinstance(spec_id, str) or not _SPEC_ID_RE.match(spec_id):
        raise SpecLoadError(
            f"{yaml_path}: spec_id must match {_SPEC_ID_RE.pattern!r} "
            f"(lowercase, hyphen-free, uppercase-safe for the rule-id SPEC "
            f"segment); got {spec_id!r}"
        )

    categories = tuple(
        _build_category(c, yaml_path) for c in (raw.get("categories") or [])
    )
    rules = tuple(_build_rule(r, yaml_path) for r in (raw.get("rules") or []))

    return Spec(**spec_block, categories=categories, rules=rules)


# ---- Internal helpers ----------------------------------------------------


class SpecLoadError(ValueError):
    """Raised when a YAML spec file does not match the expected schema."""


def _require_mapping(data: dict[str, Any], key: str, path: Path) -> dict[str, Any]:
    val = data.get(key)
    if not isinstance(val, dict):
        raise SpecLoadError(
            f"{path}: {key!r} must be a mapping, got {type(val).__name__}"
        )
    return val


def _reject_unknown(
    data: dict[str, Any], allowed: set[str], where: str, path: Path
) -> None:
    extras = set(data) - allowed
    if extras:
        raise SpecLoadError(
            f"{path}: unknown key(s) in {where}: {sorted(extras)!r} "
            f"(allowed: {sorted(allowed)!r})"
        )


def _build_category(raw: Any, path: Path) -> SpecCategory:
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: each category must be a mapping, got {type(raw).__name__}"
        )
    _reject_unknown(raw, _CATEGORY_ALLOWED, "categories[]", path)
    return SpecCategory(**raw)


def _build_rule(raw: Any, path: Path) -> SpecRule:
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: each rule must be a mapping, got {type(raw).__name__}"
        )
    data = dict(raw)  # shallow copy so we can pop
    probe_raw = data.pop("probe", None)
    _reject_unknown(data, _RULE_ALLOWED, "rules[]", path)
    probe = _build_probe(probe_raw, path) if probe_raw is not None else None
    return SpecRule(**data, probe=probe)


def _build_probe(raw: Any, path: Path) -> ProbeRef:
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: rule.probe must be a mapping, got {type(raw).__name__}"
        )
    name = raw.get("name")
    if not isinstance(name, str) or not name:
        raise SpecLoadError(f"{path}: rule.probe.name must be a non-empty string")
    params = raw.get("params") or {}
    if not isinstance(params, dict):
        raise SpecLoadError(f"{path}: rule.probe.params must be a mapping or omitted")
    extras = set(raw) - {"name", "params"}
    if extras:
        raise SpecLoadError(f"{path}: unknown key(s) in rule.probe: {sorted(extras)!r}")
    return ProbeRef(name=name, params=dict(params))
