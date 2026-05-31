# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Probe registry: name -> callable.

Probes are registered with the :func:`probe` decorator at import time and
looked up by name when the rule engine processes a YAML rule's
``probe.name``.

Probe signature (informal -- enforced by convention, not types):

    probe(checker: BaseChecker, **params) -> Iterable[Finding]

* ``checker`` -- the running checker instance.  Probes use the
  presence-oriented accessors on it (:meth:`BaseChecker.components_without`
  and :meth:`BaseChecker.document_has`) rather than poking at private
  attributes, so they stay format-agnostic.
* ``**params`` -- keyword arguments from the rule's ``probe.params`` YAML
  block.  Probes must declare every parameter explicitly (no ``**kwargs``)
  so the loader can validate parameter spelling.
* Returns -- iterable of :class:`Finding`.  Empty iterable means the rule
  passed.  Probes never decide severity, level, or rule id -- those live
  on :class:`SpecRule`.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..base_checker import BaseChecker
    from ..model import Finding

ProbeFn = Callable[..., Iterable["Finding"]]

_PROBES: dict[str, ProbeFn] = {}


def probe(name: str) -> Callable[[ProbeFn], ProbeFn]:
    """Register ``fn`` under ``name`` in the global probe registry.

    Raises ``ValueError`` on duplicate registration so accidental overrides
    fail loudly at import time.
    """

    def deco(fn: ProbeFn) -> ProbeFn:
        if name in _PROBES:
            raise ValueError(
                f"Probe {name!r} already registered as {_PROBES[name].__qualname__}; "
                f"refusing to overwrite with {fn.__qualname__}."
            )
        _PROBES[name] = fn
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


def registered_names() -> tuple[str, ...]:
    """All registered probe names, sorted.  For tests / introspection."""
    return tuple(sorted(_PROBES))


# Convenience re-export so callers don't need a second import.
def run(name: str, checker: "BaseChecker", **params: Any) -> Iterable["Finding"]:
    """Look up ``name`` and call it with ``checker`` + ``params``."""
    return lookup(name)(checker, **params)
