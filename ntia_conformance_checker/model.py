# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Shared data types for the declarative-rules engine.

* :class:`Finding` -- one occurrence of a rule violation, format-agnostic.
  Probes yield ``Finding`` objects; the SARIF / JSON / text emitters
  convert them to their output shape.

* ``ELEMENT_IDS`` -- the canonical, presence-oriented vocabulary used
  throughout YAML rules, probes, and ``BaseChecker`` accessors.  Singular,
  spec-aligned names.  *Document-level* and *component-level* checks use
  the **same** vocabulary because the rule concept is the same (the
  element must be present).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Finding:
    """One occurrence of a rule violation.

    ``component_id`` is the SPDX-style identifier (e.g. ``"SPDXRef-Pkg-foo"``)
    for component-level findings, or the literal string ``"document"`` for
    document-level findings.

    ``component_name`` is the human-readable name when known (empty string
    for document-level findings or anonymous components).

    ``note`` is an optional, finding-specific message that overrides the
    rule's default warning text.  Most probes leave it empty so the rule's
    :attr:`SpecRule.warning` flows through to output.
    """

    component_id: str
    component_name: str = ""
    note: str = ""

    @property
    def is_document_level(self) -> bool:
        """True if this finding is about the SBOM document, not a component."""
        return self.component_id == "document"


# Canonical element-id vocabulary.  These strings appear verbatim in YAML
# rules, on probe ``params``, and in SARIF ``rule.properties.elementId``.
# Choose them carefully -- they are public contract.
ELEMENT_IDS: frozenset[str] = frozenset(
    {
        # Component-level (presence on each component)
        "name",
        "version",
        "unique_identifier",
        "supplier",
        "concluded_license",
        "copyright_notice",
        "cryptographic_hash",
        "relationship",
        # Document-level (presence on the SBOM as a whole)
        "author",
        "timestamp",
        "spec_version",
        "dependency_relationship",
        "primary_component",
        "sbom_type",
    }
)
