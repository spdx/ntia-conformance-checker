# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Graph utilities for SPDX 2 and SPDX 3."""

from typing import TYPE_CHECKING, Any

from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.model.relationship import RelationshipType

from .constants import VALID_SPDX2_RELATIONSHIP_TYPES

if TYPE_CHECKING:
    from spdx_tools.spdx.model.document import Document


def _build_spdx2_graph(doc: "Document") -> tuple[list[str], dict[str, list[str]]]:
    """Build the initial queue and connection map for SPDX 2."""
    queue: list[str] = []
    graph_connection_map: dict[str, list[str]] = {}

    if not doc.relationships:
        return queue, graph_connection_map

    doc_id = "SPDXRef-DOCUMENT"
    if getattr(doc, "creation_info", None) and getattr(
        doc.creation_info, "spdx_id", None
    ):
        doc_id = doc.creation_info.spdx_id

    for rel in doc.relationships:
        source_id = rel.spdx_element_id
        target_id = rel.related_spdx_element_id

        if not isinstance(source_id, str) or not isinstance(target_id, str):
            continue

        # Get the root elements
        if rel.relationship_type == RelationshipType.DESCRIBES and source_id in (
            doc_id,
            "SPDXRef-DOCUMENT",
        ):
            queue.append(target_id)

        # Build the graph connection map
        if rel.relationship_type.name in VALID_SPDX2_RELATIONSHIP_TYPES:
            if source_id not in graph_connection_map:
                graph_connection_map[source_id] = []
            graph_connection_map[source_id].append(target_id)
    return queue, graph_connection_map


def _extract_spdx3_relationship_edges(
    obj: spdx3.Relationship, graph_connection_map: dict[str, list[str]]
) -> None:
    """Helper to extract explicit relationship edges."""
    from_ = getattr(obj, "from_", None)
    from_id = from_ if isinstance(from_, str) else getattr(from_, "spdxId", None)

    if not from_id:
        return

    to_ids = [
        t if isinstance(t, str) else getattr(t, "spdxId", "")
        for t in getattr(obj, "to", [])
    ]

    if from_id not in graph_connection_map:
        graph_connection_map[from_id] = []
    graph_connection_map[from_id].extend([t for t in to_ids if t])


def _extract_spdx3_collection_edges(
    obj: spdx3.ElementCollection, graph_connection_map: dict[str, list[str]]
) -> None:
    """Helper to extract implicit collection edges (e.g. Sbom, Document)."""
    col_id = getattr(obj, "spdxId", None)
    if not col_id:
        return

    if col_id not in graph_connection_map:
        graph_connection_map[col_id] = []

    for attr in ("rootElement", "element"):
        for elem in getattr(obj, attr, []):
            e_id = elem if isinstance(elem, str) else getattr(elem, "spdxId", "")
            if e_id:
                graph_connection_map[col_id].append(e_id)


def _build_spdx3_graph(
    doc: spdx3.SHACLObjectSet, spdx3_doc: spdx3.SpdxDocument | None
) -> tuple[list[str], dict[str, list[str]]]:
    """Build the initial queue and connection map for SPDX 3."""
    queue: list[str] = []
    graph_connection_map: dict[str, list[str]] = {}

    if spdx3_doc and getattr(spdx3_doc, "rootElement", None):
        for root in spdx3_doc.rootElement:
            root_id = root if isinstance(root, str) else getattr(root, "spdxId", "")
            if root_id:
                queue.append(root_id)

    # Build the graph connection map
    for obj in doc.objects:
        # Capture explicit relationships from Relationship objects
        if isinstance(obj, spdx3.Relationship):
            _extract_spdx3_relationship_edges(obj, graph_connection_map)

        # Capture implicit relationships from Collections (like Sbom, Bom, etc.)
        if isinstance(obj, spdx3.ElementCollection):
            _extract_spdx3_collection_edges(obj, graph_connection_map)

    return queue, graph_connection_map


def get_reachable_components(
    sbom_spec: str, doc: Any, spdx3_doc: Any = None
) -> set[str]:
    """
    Get all components connected to the root by using Breadth-First Search.
    """

    if not doc:
        return set()

    queue: list[str] = []

    # graph_connection_map: source_id -> list[target_ids]
    graph_connection_map: dict[str, list[str]] = {}

    # SPDX 2
    if sbom_spec == "spdx2":
        queue, graph_connection_map = _build_spdx2_graph(doc)

    # SPDX 3
    if sbom_spec == "spdx3":
        queue, graph_connection_map = _build_spdx3_graph(doc, spdx3_doc)

    reachable_component_ids: set[str] = set(queue)

    # Perform BFS to find all reachable components
    while queue:
        current_id = queue.pop(0)

        if current_id in graph_connection_map:
            for target_id in graph_connection_map[current_id]:
                if target_id not in reachable_component_ids:
                    reachable_component_ids.add(target_id)
                    queue.append(target_id)

    return reachable_component_ids
