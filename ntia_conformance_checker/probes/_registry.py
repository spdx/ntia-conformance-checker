# SPDX-FileContributor: Arthit Suriyawongkul
# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Probe registry: name -> callable.

Probes are registered with the :func:`probe` decorator at import time and
looked up by name when the rule engine processes a YAML rule's
``probe.name``.

Probe signature (informal -- enforced by convention, not types):

    probe(checker: CheckerProtocol, **params) -> Iterable[Finding]

* ``checker`` -- the running checker instance.  Probes use the
  presence-oriented accessors on it (:meth:`CheckerProtocol.components_without`
  and :meth:`CheckerProtocol.document_has`) rather than poking at private
  attributes, so they stay format-agnostic.
* ``**params`` -- keyword arguments from the rule's ``probe.params`` YAML
  block.  Probes must declare every parameter explicitly (no ``**kwargs``)
  so the loader can validate parameter spelling.
* Returns -- iterable of :class:`Finding`.  Empty iterable means the rule
  passed.  Probes never decide severity, level, or rule id -- those live
  on :class:`SpecRule`.
"""

from __future__ import annotations

import inspect
from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from ..model import Finding


class CheckerProtocol(Protocol):
    """Structural type for the probe-facing surface of a checker.

    Probes only need these two accessors, so they type-hint against this
    protocol rather than importing the concrete ``BaseChecker`` -- any
    object providing this shape satisfies it.
    """

    def components_without(self, element_id: str) -> list[tuple[str, str]]:
        """Components missing ``element_id``, as ``(name, spdx_id)`` pairs."""
        raise NotImplementedError

    def document_has(self, element_id: str) -> bool:
        """True iff the SBOM document declares ``element_id``."""
        raise NotImplementedError

    def has_components(self, kind: str, reachable_only: bool = True) -> bool:
        """True iff the SBOM has a component of ``kind`` (reachable from the root
        unless ``reachable_only`` is false)."""
        raise NotImplementedError

    def components_without_property(
        self, kind: str, properties: tuple[str, ...]
    ) -> list[tuple[str, str]]:
        """Components of ``kind`` declaring none of ``properties``."""
        raise NotImplementedError

    def components_without_relationship(
        self, kind: str, relationships: tuple[str, ...], direction: str
    ) -> list[tuple[str, str]]:
        """Components of ``kind`` in none of the ``relationships``."""
        raise NotImplementedError

    def document_declares(self, properties: tuple[str, ...]) -> bool:
        """True iff the SBOM document declares any of ``properties``."""
        raise NotImplementedError


ProbeFn = Callable[..., Iterable["Finding"]]

_PROBES: dict[str, ProbeFn] = {}
_ATTRIBUTE_SCOPES: dict[str, frozenset[str]] = {}
_VALIDATORS: dict[str, Callable[[dict[str, Any]], None]] = {}


def probe(
    name: str,
    *,
    attributes: frozenset[str] | None = None,
    validate: Callable[[dict[str, Any]], None] | None = None,
) -> Callable[[ProbeFn], ProbeFn]:
    """Register ``fn`` under ``name`` in the global probe registry.

    ``attributes`` is for a probe taking an ``attribute`` param: the element
    ids it accepts.  The loader then requires a rule's ``attribute`` to be one
    of them and to equal the rule's ``element_id``.

    Raises ``ValueError`` on duplicate registration so accidental overrides
    fail loudly at import time, and on a probe that takes ``*args``/``**kwargs``
    (the loader validates YAML params against explicit parameters) or that is
    given ``attributes`` without an ``attribute`` parameter.

    ``validate`` checks a rule's params when the spec is loaded (so a typo fails
    there, not silently at run time); it raises ``ValueError`` for bad params.
    """

    def deco(fn: ProbeFn) -> ProbeFn:
        params = inspect.signature(fn).parameters
        if any(p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD) for p in params.values()):
            raise ValueError(f"Probe {name!r} must declare its params explicitly.")
        if attributes is not None and "attribute" not in params:
            raise ValueError(f"Probe {name!r} has attributes but no 'attribute' param.")
        if name in _PROBES:
            raise ValueError(
                f"Probe {name!r} already registered as {_PROBES[name].__qualname__}; "
                f"refusing to overwrite with {fn.__qualname__}."
            )
        _PROBES[name] = fn
        if attributes is not None:
            _ATTRIBUTE_SCOPES[name] = attributes
        if validate is not None:
            _VALIDATORS[name] = validate
        return fn

    return deco


def lookup(name: str) -> ProbeFn:
    """Return the probe registered under ``name``; raise ``KeyError`` if absent."""
    try:
        return _PROBES[name]
    except KeyError as exc:
        raise KeyError(
            f"Probe {name!r} not registered.  Known probes: {sorted(_PROBES)!r}"
        ) from exc


def attribute_scope(name: str) -> frozenset[str] | None:
    """Element ids probe ``name`` accepts as ``attribute``; ``None`` if unrestricted."""
    return _ATTRIBUTE_SCOPES.get(name)


def validator(name: str) -> Callable[[dict[str, Any]], None] | None:
    """The load-time params validator of probe ``name``, if it has one."""
    return _VALIDATORS.get(name)


def registered_names() -> tuple[str, ...]:
    """All registered probe names, sorted.  For tests / introspection."""
    return tuple(sorted(_PROBES))
