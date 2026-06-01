# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""YAML -> :class:`Spec` loader for the declarative-rules engine.

Each spec lives in :file:`ntia_conformance_checker/rules/<spec>.yaml` with
the schema:

.. code-block:: yaml

    spec:
        id: ntia                                 # machine id; uppercased -> SPEC segment
        title: 2021 NTIA SBOM Minimum Elements
        uri: https://...
        sarif_category_taxonomy_name: ntia-minimum-elements
        sarif_clause_taxonomy_name: ntia-clauses

    categories:
        - id: data-fields
          code: DF
          title: Data Fields
          description: ...

    maturity_levels:                             # ordinal 0 = baseline (default)
        - level: 0
          id: required
          title: Required

    rules:                                       # id SBOM-NTIA-DF-001 is derived
        - number: 1
          slug: ntia-component-supplier-name
          spec_category: data-fields
          maturity: 0                            # which tier; omitted -> 0
          provision: requirement                 # severity; omitted -> requirement (error)
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
from typing import Any, get_args

import yaml

from .spec import (
    DEFAULT_MATURITY_LEVELS,
    ProbeRef,
    Provision,
    Spec,
    SpecCategory,
    SpecMaturity,
    SpecRule,
    Status,
)

_SPEC_ALLOWED = {f.name for f in fields(Spec)} - {
    "categories",
    "maturity_levels",
    "rules",
}
_CATEGORY_ALLOWED = {f.name for f in fields(SpecCategory)}
_MATURITY_ALLOWED = {f.name for f in fields(SpecMaturity)}
_RULE_ALLOWED = {f.name for f in fields(SpecRule)} - {"probe"}

# Status and Provision are type-hint-only Literals; the dataclass does no
# runtime checking and the loader builds rules via **kwargs, so they must be
# validated here.  Derive the allowed sets from the Literals so this stays a
# single source of truth.  (maturity is spec-defined, validated against the
# spec's own maturity_levels rather than a fixed Literal.)
_STATUS_VALUES: frozenset[str] = frozenset(get_args(Status))
_PROVISION_VALUES: frozenset[str] = frozenset(get_args(Provision))

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

    spec_id = spec_block.get("id")
    if not isinstance(spec_id, str) or not _SPEC_ID_RE.match(spec_id):
        raise SpecLoadError(
            f"{yaml_path}: spec id must match {_SPEC_ID_RE.pattern!r} "
            f"(lowercase, hyphen-free, uppercase-safe for the rule-id SPEC "
            f"segment); got {spec_id!r}"
        )

    categories = tuple(
        _build_category(c, yaml_path) for c in (raw.get("categories") or [])
    )
    raw_levels = raw.get("maturity_levels")
    if not raw_levels:  # absent or empty -> flat spec gets the named default
        maturity_levels = DEFAULT_MATURITY_LEVELS
    else:
        maturity_levels = tuple(_build_maturity(m, yaml_path) for m in raw_levels)
    allowed_levels = _validate_maturity_levels(maturity_levels, yaml_path)
    rules = tuple(
        _build_rule(r, allowed_levels, yaml_path) for r in (raw.get("rules") or [])
    )

    return Spec(
        **spec_block,
        categories=categories,
        maturity_levels=maturity_levels,
        rules=rules,
    )


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


def _build_maturity(raw: Any, path: Path) -> SpecMaturity:
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: each maturity level must be a mapping, got {type(raw).__name__}"
        )
    _reject_unknown(raw, _MATURITY_ALLOWED, "maturity_levels[]", path)
    level = raw.get("level")
    if not isinstance(level, int) or isinstance(level, bool):
        raise SpecLoadError(
            f"{path}: maturity_levels[].level must be an integer; got {level!r}"
        )
    mat_id = raw.get("id")
    if not isinstance(mat_id, str) or not mat_id:
        raise SpecLoadError(
            f"{path}: maturity_levels[].id must be a non-empty string; got {mat_id!r}"
        )
    return SpecMaturity(**raw)


def _validate_maturity_levels(
    levels: tuple[SpecMaturity, ...], path: Path
) -> frozenset[int]:
    """Cross-check the parsed maturity levels; return the set of valid ordinals.

    Enforces unique ordinals + ids and, when any level is declared, the
    presence of the baseline level ``0`` (the default for rules that omit
    ``maturity``).
    """
    if not levels:
        return frozenset()
    ordinals = [m.level for m in levels]
    ids = [m.id for m in levels]
    if len(set(ordinals)) != len(ordinals):
        raise SpecLoadError(f"{path}: duplicate maturity level ordinals {ordinals!r}")
    if len(set(ids)) != len(ids):
        raise SpecLoadError(f"{path}: duplicate maturity level ids {ids!r}")
    if 0 not in ordinals:
        raise SpecLoadError(
            f"{path}: maturity_levels must declare the baseline level 0; "
            f"got {sorted(ordinals)!r}"
        )
    return frozenset(ordinals)


def _build_rule(raw: Any, allowed_levels: frozenset[int], path: Path) -> SpecRule:
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: each rule must be a mapping, got {type(raw).__name__}"
        )
    data = dict(raw)  # shallow copy so we can pop
    probe_raw = data.pop("probe", None)
    _reject_unknown(data, _RULE_ALLOWED, "rules[]", path)
    # maturity is an optional ordinal (omitted -> 0); when set it must name one
    # of the spec's declared maturity_levels.
    if "maturity" in data and data["maturity"] not in allowed_levels:
        raise SpecLoadError(
            f"{path}: rule maturity must be one of {sorted(allowed_levels)!r} "
            f"(declared in maturity_levels); got {data['maturity']!r}"
        )
    _reject_bad_enum(data, "provision", _PROVISION_VALUES, path)
    _reject_bad_enum(data, "status", _STATUS_VALUES, path)
    probe = _build_probe(probe_raw, path) if probe_raw is not None else None
    return SpecRule(**data, probe=probe)


def _reject_bad_enum(
    data: dict[str, Any], key: str, allowed: frozenset[str], path: Path
) -> None:
    """Validate an optional enum-like rule field against its allowed values."""
    if key not in data:
        return  # omitted -> dataclass default (already a valid value)
    value = data[key]
    if value not in allowed:
        raise SpecLoadError(
            f"{path}: rule {key!r} must be one of {sorted(allowed)!r}; got {value!r}"
        )


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
