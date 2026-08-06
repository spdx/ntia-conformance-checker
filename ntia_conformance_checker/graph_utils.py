# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Graph utilities for SPDX 2 and SPDX 3."""

from typing import TYPE_CHECKING, Any, cast

from spdx_tools.spdx.model.relationship import RelationshipType

from .constants import (
    VALID_SPDX2_COMPOSITION_RELATIONSHIPS,
    VALID_SPDX3_COMPOSITION_RELATIONSHIPS,
)

if TYPE_CHECKING:
    from spdx_python_model.bindings import v3_0_1 as spdx3_types
    from spdx_tools.spdx.model.document import Document


def analyze_graph_connectivity(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None, spdx_module: Any = None
) -> tuple[set[str], set[str], dict[str, list[str]], bool]:
    """
    Analyzes the graph to find reachable nodes, floating nodes, and unknown pointer edges.

    Returns:
        tuple: (reachable_ids, floating_ids, unknown_pointer_edges, has_unknown_pointers)
    """
    reachable_ids, connection_map = get_reachable_components(
        sbom_spec, parsed_data, spdx3_doc, spdx_module
    )
    all_doc_ids: set[str] = set()

    if sbom_spec == "spdx2":
        spdx2_doc = cast("Document", parsed_data)
        all_doc_ids = {
            pkg.spdx_id for pkg in spdx2_doc.packages if isinstance(pkg.spdx_id, str)
        }
    elif sbom_spec == "spdx3":
        spdx3_doc_set = cast("spdx3_types.SHACLObjectSet", parsed_data)
        all_doc_ids = {
            getattr(obj, "spdxId")
            for obj in spdx3_doc_set.objects
            if isinstance(getattr(obj, "spdxId", None), str)
        }

    floating_ids = all_doc_ids - reachable_ids
    has_unknown_pointers = not reachable_ids.issubset(all_doc_ids)

    # Find exactly which edges point to unknown nodes
    unknown_pointer_edges: dict[str, list[str]] = {}
    for source_id, target_ids in connection_map.items():
        missing_targets = [t for t in target_ids if t not in all_doc_ids]
        if missing_targets:
            unknown_pointer_edges[source_id] = missing_targets

    return reachable_ids, floating_ids, unknown_pointer_edges, has_unknown_pointers


def _build_spdx2_graph(spdx2_doc: "Document") -> tuple[list[str], dict[str, list[str]]]:
    """Build the initial queue and connection map for SPDX 2."""
    queue: list[str] = []
    graph_connection_map: dict[str, list[str]] = {}

    if not spdx2_doc.relationships:
        return queue, graph_connection_map

    doc_id = "SPDXRef-DOCUMENT"
    if getattr(spdx2_doc, "creation_info", None) and getattr(
        spdx2_doc.creation_info, "spdx_id", None
    ):
        doc_id = spdx2_doc.creation_info.spdx_id

    for rel in spdx2_doc.relationships:
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
        if rel.relationship_type.name in VALID_SPDX2_COMPOSITION_RELATIONSHIPS:
            if source_id not in graph_connection_map:
                graph_connection_map[source_id] = []
            graph_connection_map[source_id].append(target_id)
    return queue, graph_connection_map


def _extract_spdx3_relationship_edges(
    obj: spdx3_types.Relationship, graph_connection_map: dict[str, list[str]]
) -> None:
    """Helper to extract explicit relationship edges."""
    rel_type_iri = getattr(obj, "relationshipType", "")
    if not rel_type_iri:
        return

    # Extract the actual name from the IRI (e.g., ".../contains" -> "contains")
    rel_name = rel_type_iri.split("/")[-1]

    if rel_name not in VALID_SPDX3_COMPOSITION_RELATIONSHIPS:
        return

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
    obj: spdx3_types.ElementCollection, graph_connection_map: dict[str, list[str]]
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
    object_set: spdx3_types.SHACLObjectSet,
    spdx3_doc: spdx3_types.SpdxDocument | None,
    spdx_module: Any,
) -> tuple[list[str], dict[str, list[str]]]:
    """Build the initial queue and connection map for SPDX 3."""
    queue: list[str] = []
    graph_connection_map: dict[str, list[str]] = {}

    doc_id = getattr(spdx3_doc, "spdxId", None) if spdx3_doc else None

    if spdx3_doc and getattr(spdx3_doc, "rootElement", None):
        for root in spdx3_doc.rootElement:
            root_id = root if isinstance(root, str) else getattr(root, "spdxId", "")
            if root_id:
                queue.append(root_id)

    # Build the graph connection map
    for obj in object_set.objects:
        # Capture explicit relationships from Relationship objects
        if isinstance(obj, spdx_module.Relationship):
            from_ = getattr(obj, "from_", None)
            from_id = (
                from_ if isinstance(from_, str) else getattr(from_, "spdxId", None)
            )

            # If a relationship originates from the Document itself,
            # its targets are treated as Roots.
            if doc_id and from_id == doc_id:
                to_ids = [
                    t if isinstance(t, str) else getattr(t, "spdxId", "")
                    for t in getattr(obj, "to", [])
                ]
                queue.extend([t for t in to_ids if t])

            # Normal relationships between packages build the map
            else:
                _extract_spdx3_relationship_edges(obj, graph_connection_map)

        # Capture implicit relationships from Collections (like Sbom, Bom, etc.)
        if isinstance(obj, spdx_module.ElementCollection):
            _extract_spdx3_collection_edges(obj, graph_connection_map)

    return queue, graph_connection_map


def get_reachable_components(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None, spdx_module: Any = None
) -> tuple[set[str], dict[str, list[str]]]:
    """
    Get all components connected to the root by using Breadth-First Search.

    Returns:
        tuple: (reachable_component_ids, graph_connection_map)
    """

    if not parsed_data:
        return set(), {}

    queue: list[str] = []

    # graph_connection_map: source_id -> list[target_ids]
    graph_connection_map: dict[str, list[str]] = {}

    # SPDX 2
    if sbom_spec == "spdx2":
        queue, graph_connection_map = _build_spdx2_graph(parsed_data)

    # SPDX 3
    if sbom_spec == "spdx3":
        queue, graph_connection_map = _build_spdx3_graph(
            parsed_data, spdx3_doc, spdx_module
        )

    reachable_component_ids: set[str] = set(queue)

    # Perform BFS to find all reachable components
    while queue:
        current_id = queue.pop(0)

        if current_id in graph_connection_map:
            for target_id in graph_connection_map[current_id]:
                if target_id not in reachable_component_ids:
                    reachable_component_ids.add(target_id)
                    queue.append(target_id)

    return reachable_component_ids, graph_connection_map
