# SPDX-FileContributor: Arthit Suriyawongkul
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
        taxonomies:                              # output-format-agnostic names
            category: ntia-minimum-elements
            clause: ntia-clauses

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
          slug: ntia-component-supplier-missing   # finding-framed; report_name derived
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

import inspect
import re
from dataclasses import MISSING, fields
from pathlib import Path
from typing import Any, get_args, get_type_hints

import yaml

from . import probes
from .model import ELEMENT_IDS
from .spec import (
    DEFAULT_MATURITY_LEVELS,
    Aggregation,
    ProbeRef,
    Provision,
    Spec,
    SpecCategory,
    SpecMaturity,
    SpecRule,
    SpecTaxonomies,
    Status,
)

# ``taxonomies`` is allowed as a key in the ``spec`` block but built manually
# (it is a nested mapping, not a scalar), so it is popped before ``Spec(**...)``.
_SPEC_ALLOWED = {f.name for f in fields(Spec)} - {
    "categories",
    "maturity_levels",
    "rules",
}
_TOP_LEVEL_ALLOWED = {"spec", "categories", "maturity_levels", "rules"}
_CATEGORY_ALLOWED = {f.name for f in fields(SpecCategory)}
_MATURITY_ALLOWED = {f.name for f in fields(SpecMaturity)}
_TAXONOMIES_ALLOWED = {f.name for f in fields(SpecTaxonomies)}
_RULE_ALLOWED = {f.name for f in fields(SpecRule)} - {"probe"}

# Status and Provision are type-hint-only Literals; the dataclass does no
# runtime checking and the loader builds rules via **kwargs, so they must be
# validated here.  Derive the allowed sets from the Literals so this stays a
# single source of truth.  (maturity is spec-defined, validated against the
# spec's own maturity_levels rather than a fixed Literal.)
_STATUS_VALUES: frozenset[str] = frozenset(get_args(Status))
_PROVISION_VALUES: frozenset[str] = frozenset(get_args(Provision))
_AGGREGATION_VALUES: frozenset[str] = frozenset(get_args(Aggregation))
_SBOM_SPEC_VALUES = frozenset({"spdx2", "spdx3"})

# spec_id is uppercased into the SPEC segment of every rule id, so it must be a
# hyphen-free, uppercase-safe token (start with a letter, then letters/digits).
_SPEC_ID_RE = re.compile(r"^[a-z][a-z0-9]*$")
_KEBAB_RE = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")  # category id, rule slug
_CATEGORY_CODE_RE = re.compile(r"^[A-Z][A-Z0-9]*$")  # CATEGORY segment of a rule id
_RULE_PREFIX_RE = re.compile(r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*$")  # e.g. BOM-NTIA2021


def load_spec(path: str | Path) -> Spec:
    """Load and validate a spec YAML file, returning a :class:`Spec` instance.

    Raises:
        FileNotFoundError: ``path`` does not exist.
        SpecLoadError: the file is syntactically valid YAML but does not
            match the expected schema (unknown keys, missing required
            fields, malformed probe reference, etc).
    """
    yaml_path = Path(path)
    try:
        # _UniqueKeyLoader is a yaml.SafeLoader subclass, so this is a safe load.
        raw = yaml.load(  # nosec B506
            yaml_path.read_text(encoding="utf-8"), Loader=_UniqueKeyLoader
        )
    except (yaml.YAMLError, UnicodeDecodeError) as exc:
        raise SpecLoadError(
            f"{yaml_path}: invalid YAML (UTF-8 expected): {exc}"
        ) from exc
    if not isinstance(raw, dict):
        raise SpecLoadError(f"{yaml_path}: top-level must be a mapping")

    _reject_unknown(raw, _TOP_LEVEL_ALLOWED, "top level", yaml_path)
    spec_block = dict(_require_mapping(raw, "spec", yaml_path))
    _reject_unknown(spec_block, _SPEC_ALLOWED, "spec", yaml_path)
    _check_fields(Spec, spec_block, "spec", yaml_path)

    spec_id = spec_block.get("id")
    if not isinstance(spec_id, str) or not _SPEC_ID_RE.fullmatch(spec_id):
        raise SpecLoadError(
            f"{yaml_path}: spec id must match {_SPEC_ID_RE.pattern!r} "
            f"(lowercase, hyphen-free, uppercase-safe for the rule-id SPEC "
            f"segment); got {spec_id!r}"
        )

    taxonomies = _build_taxonomies(spec_block.pop("taxonomies", None), yaml_path)
    spec_block["sbom_specs"] = _build_sbom_specs(
        spec_block.pop("sbom_specs", []), yaml_path
    )
    prefix = spec_block.get("rule_prefix", "")
    if not isinstance(prefix, str) or (
        prefix and not _RULE_PREFIX_RE.fullmatch(prefix)
    ):
        raise SpecLoadError(
            f"{yaml_path}: spec rule_prefix must match {_RULE_PREFIX_RE.pattern!r}; "
            f"got {prefix!r}"
        )
    categories = tuple(
        _build_category(c, yaml_path)
        for c in _require_list(raw, "categories", yaml_path)
    )
    _validate_categories(categories, yaml_path)
    raw_levels = _require_list(raw, "maturity_levels", yaml_path)
    if not raw_levels:  # absent or empty -> flat spec gets the named default
        maturity_levels = DEFAULT_MATURITY_LEVELS
    else:
        maturity_levels = tuple(_build_maturity(m, yaml_path) for m in raw_levels)
    allowed_levels = _validate_maturity_levels(maturity_levels, yaml_path)
    category_ids = frozenset(c.id for c in categories)
    rules = tuple(
        _build_rule(r, allowed_levels, category_ids, yaml_path)
        for r in _require_list(raw, "rules", yaml_path)
    )
    _validate_rules(spec_id, rules, yaml_path)

    return Spec(
        **spec_block,
        taxonomies=taxonomies,
        categories=categories,
        maturity_levels=maturity_levels,
        rules=rules,
    )


# ---- Errors --------------------------------------------------------------


class SpecLoadError(ValueError):
    """Raised when a YAML spec file is not valid YAML or does not match the
    expected schema."""


class _UniqueKeyLoader(yaml.SafeLoader):  # pylint: disable=too-many-ancestors
    """Safe YAML loader that rejects duplicate mapping keys.

    PyYAML keeps the last of two equal keys, which would silently defeat the
    uniqueness checks below.
    """

    def __init__(self, stream: str) -> None:
        super().__init__(stream)
        self._checked: set[int] = set()

    def flatten_mapping(self, node: yaml.MappingNode) -> None:
        """Check ``node``'s own keys once, before merge keys are folded in."""
        if id(node) not in self._checked:
            self._checked.add(id(node))
            keys = [
                self.construct_object(key, deep=True)
                for key, _ in node.value
                if key.tag != "tag:yaml.org,2002:merge"
            ]
            dupes = [k for i, k in enumerate(keys) if k in keys[:i]]
            if dupes:
                raise yaml.constructor.ConstructorError(
                    None, None, f"duplicate key(s) {dupes!r}", node.start_mark
                )
        super().flatten_mapping(node)


# ---- Generic mapping / validation helpers --------------------------------


def _reject_bad_enum(
    data: dict[str, Any], key: str, allowed: frozenset[str], path: Path
) -> None:
    """Validate an optional enum-like rule field against its allowed values."""
    if key not in data:
        return  # omitted -> dataclass default (already a valid value)
    value = data[key]
    if not isinstance(value, str) or value not in allowed:
        raise SpecLoadError(
            f"{path}: rule {key!r} must be one of {sorted(allowed)!r}; got {value!r}"
        )


def _reject_unknown(
    data: dict[str, Any], allowed: set[str], where: str, path: Path
) -> None:
    extras = set(data) - allowed
    if extras:
        raise SpecLoadError(
            f"{path}: unknown key(s) in {where}: {sorted(extras, key=repr)!r} "
            f"(allowed: {sorted(allowed)!r})"
        )


def _require_mapping(data: dict[str, Any], key: str, path: Path) -> dict[str, Any]:
    val = data.get(key)
    if not isinstance(val, dict):
        raise SpecLoadError(
            f"{path}: {key!r} must be a mapping, got {type(val).__name__}"
        )
    return val


def _require_list(data: dict[str, Any], key: str, path: Path) -> list[Any]:
    val = data.get(key)
    if val is None:
        return []
    if not isinstance(val, list):
        raise SpecLoadError(f"{path}: {key!r} must be a list, got {type(val).__name__}")
    return val


# Scalar field types the loader checks (a bool is never accepted as an int).
_SCALAR_TYPES: dict[Any, tuple[type, ...]] = {
    str: (str,),
    str | None: (str, type(None)),
    int: (int,),
}


def _check_fields(cls: type, data: dict[str, Any], where: str, path: Path) -> None:
    """Require ``cls``'s mandatory fields and enforce its scalar field types.

    YAML 1.1 coerces bare scalars (``NO`` -> ``False``, ``1.10`` -> ``1.1``), so
    types are checked rather than trusted.
    """
    hints = get_type_hints(cls)
    for fld in fields(cls):
        if fld.name not in data:
            if fld.default is MISSING and fld.default_factory is MISSING:
                raise SpecLoadError(f"{path}: {where} is missing key {fld.name!r}")
            continue
        value = data[fld.name]
        kind = hints[fld.name]
        allowed = _SCALAR_TYPES.get(kind)
        if allowed and (
            not isinstance(value, allowed)
            or (isinstance(value, bool) and int in allowed)
        ):
            raise SpecLoadError(
                f"{path}: {where}.{fld.name} must be {allowed[0].__name__}"
                f"{' or null' if type(None) in allowed else ''}; got {value!r}"
                f"{' (quote it in YAML)' if str in allowed else ''}"
            )


# ---- Per-section builders (raw mapping -> dataclass) ----------------------


def _build_category(raw: Any, path: Path) -> SpecCategory:
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: each category must be a mapping, got {type(raw).__name__}"
        )
    _reject_unknown(raw, _CATEGORY_ALLOWED, "categories[]", path)
    _check_fields(SpecCategory, raw, "categories[]", path)
    return SpecCategory(**raw)


def _build_maturity(raw: Any, path: Path) -> SpecMaturity:
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: each maturity level must be a mapping, got {type(raw).__name__}"
        )
    _reject_unknown(raw, _MATURITY_ALLOWED, "maturity_levels[]", path)
    _check_fields(SpecMaturity, raw, "maturity_levels[]", path)
    if not raw["id"] or raw["level"] < 0:
        raise SpecLoadError(
            f"{path}: maturity_levels[] needs a non-empty id and level >= 0; "
            f"got {raw!r}"
        )
    return SpecMaturity(**raw)


def _build_probe(raw: Any, path: Path) -> ProbeRef:
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: rule.probe must be a mapping, got {type(raw).__name__}"
        )
    name = raw.get("name")
    if not isinstance(name, str) or not name:
        raise SpecLoadError(f"{path}: rule.probe.name must be a non-empty string")
    if name not in probes.registered_names():
        raise SpecLoadError(
            f"{path}: rule.probe.name {name!r} is not a registered probe; "
            f"known probes: {list(probes.registered_names())!r}"
        )
    params = raw.get("params", {})
    if not isinstance(params, dict):
        raise SpecLoadError(f"{path}: rule.probe.params must be a mapping or omitted")
    extras = set(raw) - {"name", "params"}
    if extras:
        raise SpecLoadError(
            f"{path}: unknown key(s) in rule.probe: {sorted(extras, key=repr)!r}"
        )
    sig = inspect.signature(probes.lookup(name))
    unknown = set(params) - set(sig.parameters)
    if unknown:
        raise SpecLoadError(
            f"{path}: probe {name!r} has no param(s) {sorted(unknown, key=repr)!r}; "
            f"accepts {list(sig.parameters)[1:]!r}"
        )
    try:  # also catches missing params
        sig.bind(None, **params)
    except TypeError as exc:
        raise SpecLoadError(
            f"{path}: rule.probe.params do not fit probe {name!r}: {exc}"
        ) from exc
    check = probes.validator(name)
    if check is not None:
        try:
            check(params)
        except ValueError as exc:
            raise SpecLoadError(f"{path}: probe {name!r}: {exc}") from exc
    return ProbeRef(name=name, params=dict(params))


def _build_rule(
    raw: Any, allowed_levels: frozenset[int], category_ids: frozenset[str], path: Path
) -> SpecRule:
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: each rule must be a mapping, got {type(raw).__name__}"
        )
    data = dict(raw)  # shallow copy so we can pop
    probe_raw = data.pop("probe", None)
    _reject_unknown(data, _RULE_ALLOWED, "rules[]", path)
    _check_fields(SpecRule, data, "rules[]", path)
    if not 1 <= data["number"] <= 999:  # rendered as three digits (NNN)
        raise SpecLoadError(
            f"{path}: rule number must be 1..999; got {data['number']!r}"
        )
    if data["spec_category"] not in category_ids:
        raise SpecLoadError(
            f"{path}: rule spec_category must be one of {sorted(category_ids)!r}; "
            f"got {data['spec_category']!r}"
        )
    # maturity is an optional ordinal (omitted -> 0); when set it must name one
    # of the spec's declared maturity_levels.
    if "maturity" in data and data["maturity"] not in allowed_levels:
        raise SpecLoadError(
            f"{path}: rule maturity must be one of {sorted(allowed_levels)!r} "
            f"(declared in maturity_levels); got {data['maturity']!r}"
        )
    _reject_bad_enum(data, "provision", _PROVISION_VALUES, path)
    _reject_bad_enum(data, "status", _STATUS_VALUES, path)
    _reject_bad_enum(data, "aggregation", _AGGREGATION_VALUES, path)
    if data.get("sub", 0) < 0 or data.get("sub", 0) > 99:
        raise SpecLoadError(f"{path}: rule sub must be 0..99; got {data['sub']!r}")
    if data.get("element_id", "") not in ELEMENT_IDS | {""}:
        raise SpecLoadError(
            f"{path}: rule element_id must be one of {sorted(ELEMENT_IDS)!r}; "
            f"got {data['element_id']!r}"
        )
    if "element_concept_uris" in data:
        uris = data["element_concept_uris"]
        if not isinstance(uris, list) or not all(isinstance(u, str) for u in uris):
            raise SpecLoadError(
                f"{path}: rule element_concept_uris must be a list of strings; "
                f"got {uris!r}"
            )
        data["element_concept_uris"] = tuple(uris)
    return SpecRule(**data, probe=_build_rule_probe(probe_raw, data, path))


def _build_rule_probe(
    probe_raw: Any, data: dict[str, Any], path: Path
) -> ProbeRef | None:
    """Build a rule's probe and check it fits the rule: an active rule needs one
    (else it passes vacuously), a non-active rule must not have one."""
    probe = _build_probe(probe_raw, path) if probe_raw is not None else None
    active = data.get("status", "active") == "active"
    rollup = data.get("aggregation", "") in ("any-of", "all-of")
    if rollup and probe is not None:
        raise SpecLoadError(
            f"{path}: roll-up rule {data['slug']!r} is computed from its "
            f"sub-rules and must not have a probe"
        )
    if active and probe is None and not rollup:
        raise SpecLoadError(
            f"{path}: active rule {data['slug']!r} has no probe, so it would "
            f"pass vacuously; add a probe or set status to catalogue-only/tbd"
        )
    if probe is not None and not active:
        raise SpecLoadError(
            f"{path}: rule {data['slug']!r} is not active, so its probe never runs"
        )
    if probe is not None:
        _check_probe_attribute(probe, data.get("element_id", ""), path)
    return probe


def _check_probe_attribute(probe: ProbeRef, element_id: str, path: Path) -> None:
    """For a probe registered with ``attributes``: the rule must name one of them
    as ``attribute``, and the rule's ``element_id`` (when set) must be the same."""
    scope = probes.attribute_scope(probe.name)
    if scope is None:
        return
    attr = probe.params.get("attribute")
    if not isinstance(attr, str) or attr not in scope:
        raise SpecLoadError(
            f"{path}: probe {probe.name!r} attribute must be one of "
            f"{sorted(scope)!r}; got {attr!r}"
        )
    if element_id and element_id != attr:
        raise SpecLoadError(
            f"{path}: rule element_id {element_id!r} differs from its probe "
            f"attribute {attr!r}"
        )


def _build_sbom_specs(raw: Any, path: Path) -> tuple[str, ...]:
    """Validate the spec's ``sbom_specs`` list (omitted -> any SBOM specification)."""
    if not isinstance(raw, list) or not all(
        isinstance(v, str) and v in _SBOM_SPEC_VALUES for v in raw
    ):
        raise SpecLoadError(
            f"{path}: spec sbom_specs must be a list drawn from "
            f"{sorted(_SBOM_SPEC_VALUES)!r}; got {raw!r}"
        )
    if len(set(raw)) != len(raw):
        raise SpecLoadError(f"{path}: spec sbom_specs has duplicates: {raw!r}")
    return tuple(raw)


def _build_taxonomies(raw: Any, path: Path) -> SpecTaxonomies:
    if raw is None:
        return SpecTaxonomies()
    if not isinstance(raw, dict):
        raise SpecLoadError(
            f"{path}: 'spec.taxonomies' must be a mapping, got {type(raw).__name__}"
        )
    _reject_unknown(raw, _TAXONOMIES_ALLOWED, "spec.taxonomies", path)
    _check_fields(SpecTaxonomies, raw, "spec.taxonomies", path)
    return SpecTaxonomies(**raw)


# ---- Cross-field validation ----------------------------------------------


def _validate_maturity_levels(
    levels: tuple[SpecMaturity, ...], path: Path
) -> frozenset[int]:
    """Cross-check the parsed maturity levels; return the set of valid ordinals.

    Enforces unique ordinals + ids and the presence of the baseline level ``0``
    (the default for rules that omit ``maturity``).  ``load_spec`` always passes
    a non-empty tuple -- it substitutes :data:`DEFAULT_MATURITY_LEVELS` when the
    YAML omits the block -- so the empty case is not handled here.
    """
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


def _validate_categories(categories: tuple[SpecCategory, ...], path: Path) -> None:
    """Check category id/code shape and uniqueness.

    Codes form the ``CATEGORY`` segment of rule ids, so a duplicate code would
    let two categories mint the same rule id.
    """
    for cat in categories:
        if not _KEBAB_RE.fullmatch(cat.id):
            raise SpecLoadError(
                f"{path}: category id must be kebab-case; got {cat.id!r}"
            )
        if not _CATEGORY_CODE_RE.fullmatch(cat.code):
            raise SpecLoadError(
                f"{path}: category code must be uppercase and hyphen-free; "
                f"got {cat.code!r}"
            )
    for attr in ("id", "code"):
        values = [getattr(c, attr) for c in categories]
        if len(set(values)) != len(values):
            raise SpecLoadError(f"{path}: duplicate category {attr} in {values!r}")


def _validate_rules(spec_id: str, rules: tuple[SpecRule, ...], path: Path) -> None:
    """Check slug shape and uniqueness of rule ids, slugs and JSON keys.

    Categories are validated first, so ``(spec_category, number)`` identifies
    the rendered rule id one-to-one.
    """
    for rule in rules:
        if not _KEBAB_RE.fullmatch(rule.slug) or not rule.slug.startswith(
            f"{spec_id}-"
        ):
            raise SpecLoadError(
                f"{path}: rule slug must be kebab-case and start with "
                f"'{spec_id}-'; got {rule.slug!r}"
            )
    keys: dict[str, list[Any]] = {
        "slug": [r.slug for r in rules],
        "number in its category": [(r.spec_category, r.number, r.sub) for r in rules],
        "json_key": [(r.json_group, r.json_key) for r in rules if r.json_key],
    }
    for what, values in keys.items():
        dupes = sorted({str(v) for v in values if values.count(v) > 1})
        if dupes:
            raise SpecLoadError(f"{path}: duplicate rule {what}: {dupes}")
    _validate_composites(rules, path)


def _validate_composites(rules: tuple[SpecRule, ...], path: Path) -> None:
    """Check that sub-rules refine an existing composite rule consistently.

    A sub-rule shares its parent's category and number (its id is the parent's
    plus ``.M``); a roll-up parent needs at least one sub-rule.
    """
    by_slug = {r.slug: r for r in rules}
    for rule in rules:
        if bool(rule.parent) != bool(rule.sub):
            raise SpecLoadError(
                f"{path}: rule {rule.slug!r} needs both parent and sub, or neither"
            )
        if not rule.parent:
            continue
        parent = by_slug.get(rule.parent)
        if parent is None or not parent.aggregation or parent.sub:
            raise SpecLoadError(
                f"{path}: rule {rule.slug!r} parent {rule.parent!r} must be a "
                f"top-level rule with an aggregation"
            )
        if (parent.spec_category, parent.number) != (rule.spec_category, rule.number):
            raise SpecLoadError(
                f"{path}: sub-rule {rule.slug!r} must share its parent's "
                f"category and number"
            )
    for rule in rules:
        if rule.aggregation in ("any-of", "all-of"):
            _validate_rollup(rule, rules, path)


def _validate_rollup(rule: SpecRule, rules: tuple[SpecRule, ...], path: Path) -> None:
    """Check a roll-up rule: active only with active sub-rules of one kind."""
    subs = [r for r in rules if r.parent == rule.slug]
    active = [r for r in subs if r.status == "active"]
    if rule.status != "active":
        if active:
            raise SpecLoadError(
                f"{path}: roll-up rule {rule.slug!r} is not active, so its "
                f"sub-rules cannot be"
            )
        return
    if not active:
        raise SpecLoadError(
            f"{path}: roll-up rule {rule.slug!r} needs an active sub-rule"
        )
    kinds = {r.probe.params.get("kind") for r in active if r.probe}
    if len(kinds) > 1:
        raise SpecLoadError(
            f"{path}: sub-rules of roll-up {rule.slug!r} must share one "
            f"component kind, got {sorted(map(str, kinds))}"
        )
