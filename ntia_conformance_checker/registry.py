# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Spec registry: the single source of truth for available standards.

Every ``rules/*.yaml`` file packaged with this library is discovered and
loaded once at import time, indexed by its ``standard_id``.  This makes a
spec's ``standard_id`` the authoritative compliance identifier:

* it is the string the user passes to ``--comply`` / ``compliance=``,
* it keys the dispatch in :class:`SbomChecker`,
* its :attr:`Spec.title` is the human-readable description shown in CLI
  help and report headers.

Adding a new standard is therefore *just dropping a YAML file* into the
``rules/`` directory -- no new Python subclass, no factory edit, no
hardcoded id list to update.  (A named convenience subclass such as
``NTIAChecker`` is optional and only kept for backwards-compatible
imports.)

**Convention:** name each file after its ``standard_id``
(e.g. ``rules/ntia.yaml`` -> ``standard_id: ntia``;
``rules/fsct3-min.yaml`` -> ``standard_id: fsct3-min``).
Discovery keys on the in-file ``standard_id``, not the filename,
so a mismatch is not a hard error -- but matching them keeps the
directory navigable and pre-shapes future siblings
(e.g. ``fsct3-rec.yaml`` for additional FSCTv3 maturity levels).
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from .spec_loader import load_spec

if TYPE_CHECKING:
    from .spec import Spec

_RULES_DIR = Path(__file__).parent / "rules"


def _discover() -> dict[str, Spec]:
    """Load every packaged ``rules/*.yaml`` and index by ``standard_id``."""
    registry: dict[str, Spec] = {}
    for yaml_path in sorted(_RULES_DIR.glob("*.yaml")):
        spec = load_spec(yaml_path)
        if spec.standard_id in registry:
            raise ValueError(
                f"Duplicate standard_id {spec.standard_id!r}: "
                f"{yaml_path.name} collides with an already-loaded spec."
            )
        registry[spec.standard_id] = spec
    return registry


# Loaded once at import.  Keyed by standard_id (e.g. "ntia", "fsct3-min").
_REGISTRY: dict[str, Spec] = _discover()


def get_spec(standard_id: str) -> Spec:
    """Return the :class:`Spec` for ``standard_id``.

    Raises:
        ValueError: ``standard_id`` is not a known standard.  The message
            lists the known ids so the caller can surface a useful error.
    """
    try:
        return _REGISTRY[standard_id]
    except KeyError as exc:
        known = ", ".join(sorted(_REGISTRY))
        raise ValueError(
            f"Unknown compliance standard: {standard_id!r}.  Known: {known}"
        ) from exc


def standard_ids() -> tuple[str, ...]:
    """All known compliance standard ids, sorted."""
    return tuple(sorted(_REGISTRY))


def descriptions() -> dict[str, str]:
    """Map each standard id to its human-readable :attr:`Spec.title`."""
    return {sid: spec.title for sid, spec in _REGISTRY.items()}
