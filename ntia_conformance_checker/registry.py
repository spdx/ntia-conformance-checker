# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Spec registry: the single source of truth for available standards.

Every ``rules/*.yaml`` file packaged with this library is discovered and
loaded once at import time, indexed by its spec ``id``.  This makes a spec's
``id`` the authoritative compliance identifier:

* it is the string the user passes to ``--comply`` / ``compliance=``,
* it keys the dispatch in :class:`SbomChecker`,
* its :attr:`Spec.title` is the human-readable description shown in CLI
  help and report headers.

Adding a new standard is therefore *just dropping a YAML file* into the
``rules/`` directory -- no new Python subclass, no factory edit, no
hardcoded id list to update.  (A named convenience subclass such as
``NTIAChecker`` is optional and only kept for backwards-compatible
imports.)

**Convention:** name each file after its spec ``id``
(e.g. ``rules/ntia.yaml`` -> ``id: ntia``; ``rules/fsct3.yaml`` -> ``id: fsct3``).
Discovery keys on the in-file ``id``, not the filename, so a mismatch is not a
hard error -- but matching them keeps the directory navigable.  A new edition
is a new spec with its own ``id`` (e.g. a future ``fsct4.yaml`` -> ``id: fsct4``).
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from .spec_loader import load_spec

if TYPE_CHECKING:
    from .spec import Spec

_RULES_DIR = Path(__file__).parent / "rules"


def _discover() -> dict[str, Spec]:
    """Load every packaged ``rules/*.yaml`` and index by spec ``id``."""
    registry: dict[str, Spec] = {}
    for yaml_path in sorted(_RULES_DIR.glob("*.yaml")):
        spec = load_spec(yaml_path)
        if spec.id in registry:
            raise ValueError(
                f"Duplicate spec id {spec.id!r}: "
                f"{yaml_path.name} collides with an already-loaded spec."
            )
        registry[spec.id] = spec
    return registry


# Loaded once at import.  Keyed by spec id (e.g. "ntia", "fsct3").
_REGISTRY: dict[str, Spec] = _discover()


# ---- Public API ----------------------------------------------------------


def descriptions() -> dict[str, str]:
    """Map each spec ``id`` to its human-readable :attr:`Spec.title`."""
    return {spec_id: spec.title for spec_id, spec in _REGISTRY.items()}


def get_spec(spec_id: str) -> Spec:
    """Return the :class:`Spec` for ``spec_id``.

    Raises:
        ValueError: ``spec_id`` is not a known standard.  The message lists the
            known ids so the caller can surface a useful error.
    """
    try:
        return _REGISTRY[spec_id]
    except KeyError as exc:
        known = ", ".join(sorted(_REGISTRY))
        raise ValueError(
            f"Unknown compliance standard: {spec_id!r}.  Known: {known}"
        ) from exc


def spec_ids() -> tuple[str, ...]:
    """All known compliance spec ``id`` values, sorted."""
    return tuple(sorted(_REGISTRY))
