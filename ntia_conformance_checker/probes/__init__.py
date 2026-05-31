# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Probe registry and built-in probe implementations.

A *probe* is a small, registered Python function that answers one yes/no
question about a parsed SBOM (e.g. "do all components have a supplier?").
Rules declared in ``rules/*.yaml`` reference probes by name; the engine
calls them and collects :class:`Finding` objects.

Importing :mod:`ntia_conformance_checker.probes` registers every built-in
probe as a side effect.  See :file:`probes/presence.py` for the canonical
two-probe vocabulary that covers all current NTIA + FSCT active rules.
"""

from __future__ import annotations

# Import side-effect: register built-in probes by importing their modules.
from . import presence  # noqa: F401  (registration only)
from ._registry import lookup, probe

__all__ = ["lookup", "probe"]
