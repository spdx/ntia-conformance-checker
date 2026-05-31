# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Built-in presence probes.

Together these two probes cover every active rule in the NTIA and FSCT
catalogues -- rule-id reuse is high because the question being asked is
always the same shape ("is this attribute present?").
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..model import Finding
from ._registry import probe

if TYPE_CHECKING:
    from collections.abc import Iterable

    from ..base_checker import BaseChecker


@probe("require_component_attribute")
def require_component_attribute(
    checker: "BaseChecker", *, attribute: str
) -> Iterable[Finding]:
    """Require every component in the SBOM to declare ``attribute``.

    Yields one :class:`Finding` per component where ``attribute`` is absent
    or empty.  The component's SPDX-style id and human name are surfaced so
    SARIF / JSON / text emitters can locate the failure precisely.

    Args:
        checker: the running checker instance.
        attribute: a canonical element id from
            :data:`ntia_conformance_checker.model.ELEMENT_IDS`
            (component-level subset), e.g. ``"supplier"`` /
            ``"concluded_license"``.
    """
    for comp_name, comp_id in checker.components_without(attribute):
        yield Finding(
            component_id=comp_id or "",
            component_name=comp_name or "",
        )


@probe("require_document_attribute")
def require_document_attribute(
    checker: "BaseChecker", *, attribute: str
) -> Iterable[Finding]:
    """Require the SBOM document to declare ``attribute``.

    Yields a single document-level :class:`Finding` when the attribute is
    absent; yields nothing when present.

    Args:
        checker: the running checker instance.
        attribute: a canonical element id from
            :data:`ntia_conformance_checker.model.ELEMENT_IDS`
            (document-level subset), e.g. ``"author"`` /
            ``"dependency_relationship"``.
    """
    if not checker.document_has(attribute):
        yield Finding(component_id="document", component_name="")
