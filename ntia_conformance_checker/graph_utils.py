# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Graph utilities for SPDX 2 and SPDX 3."""

import logging
import re
from typing import TYPE_CHECKING, Any, cast

from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.model.relationship import RelationshipType

from .constants import (
    VALID_SPDX2_COMPOSITION_RELATIONSHIPS,
    VALID_SPDX2_REVERSE_COMPOSITION_RELATIONSHIPS,
    VALID_SPDX3_COMPOSITION_RELATIONSHIPS,
)
from .spdx3_utils import SPDX3_INDIVIDUAL_ELEMENT_IRIS

if TYPE_CHECKING:
    from spdx_tools.spdx.model.document import Document


# SPDX 2 element ID: "SPDXRef-"[idstring], where idstring has letters,
# numbers, "." and "-" (SPDX 2.3 clauses 7.2, 8.2, 9.1).
_SPDX2_SPDXID_PATTERN = re.compile(r"SPDXRef-[A-Za-z0-9.\-]+")


def _collect_spdx2_external_document_ref_ids(spdx2_doc: "Document") -> set[str]:
    """
    Retrieve the IDs of external documents declared in an SPDX 2 document.

    These are the ``DocumentRef-<idstring>`` values of ``ExternalDocumentRef``
    (SPDX 2.3 clause 6.6, External document references field).

    Returns:
        set[str]: Declared external document reference IDs.
    """
    creation_info = getattr(spdx2_doc, "creation_info", None)
    ext_refs = getattr(creation_info, "external_document_refs", None) or []
    return {
        ref.document_ref_id
        for ref in ext_refs
        if isinstance(getattr(ref, "document_ref_id", None), str)
    }


def _is_spdx2_external_element_id(
    element_id: str, external_doc_ref_ids: set[str]
) -> bool:
    """
    Check whether an SPDX 2 element ID refers to an element in a declared external document.

    SPDX 2.3 clause 11.1 (Table 69) writes an element in another document as
    ``"DocumentRef-"[idstring]":"SPDXID``, where the prefix is "an optional
    reference to an external SPDX Document as described in 6.6". Clause 6.6
    declares the prefix in an ``ExternalDocumentRef``. The element is defined
    in the external document, so it exists when its prefix is declared.

    Args:
        element_id: Element ID used in a relationship.
        external_doc_ref_ids: Declared external document reference IDs.

    Returns:
        bool: True if the ID is ``<declared DocumentRef>:SPDXRef-<idstring>``.
    """
    doc_ref_id, separator, local_id = element_id.partition(":")
    return (
        bool(separator)
        and doc_ref_id in external_doc_ref_ids
        and _SPDX2_SPDXID_PATTERN.fullmatch(local_id) is not None
    )


def _collect_spdx2_external_element_ids(
    spdx2_doc: "Document",
    connection_map: dict[str, list[str]],
    reachable_node_ids: set[str],
) -> set[str]:
    """
    Retrieve the graph nodes that are elements in declared external documents.

    These elements exist, but not in this document; see
    ``_is_spdx2_external_element_id``.

    Args:
        spdx2_doc: Parsed SPDX 2 document.
        connection_map: Edges from parent to children.
        reachable_node_ids: Node IDs reachable from the roots.

    Returns:
        set[str]: External element IDs among the edge targets and the
            reachable nodes.
    """
    external_doc_ref_ids = _collect_spdx2_external_document_ref_ids(spdx2_doc)
    node_ids = reachable_node_ids.union(*connection_map.values())
    return {
        node_id
        for node_id in node_ids
        if _is_spdx2_external_element_id(node_id, external_doc_ref_ids)
    }


def _collect_spdx2_known_and_package_ids(
    spdx2_doc: "Document",
) -> tuple[set[str], set[str]]:
    """
    Retrieve known entity IDs (packages, files, snippets, document) and package IDs for SPDX 2.

    Returns:
        tuple: (all_known_ids, all_package_ids)
    """
    doc_id = "SPDXRef-DOCUMENT"
    if getattr(spdx2_doc, "creation_info", None) and getattr(
        spdx2_doc.creation_info, "spdx_id", None
    ):
        doc_id = spdx2_doc.creation_info.spdx_id

    package_ids = {
        pkg.spdx_id
        for pkg in getattr(spdx2_doc, "packages", [])
        if isinstance(pkg.spdx_id, str)
    }
    file_ids = {
        f.spdx_id for f in getattr(spdx2_doc, "files", []) if isinstance(f.spdx_id, str)
    }
    snippet_ids = {
        s.spdx_id
        for s in getattr(spdx2_doc, "snippets", [])
        if isinstance(s.spdx_id, str)
    }
    all_known_ids = package_ids | file_ids | snippet_ids | {doc_id}
    return all_known_ids, package_ids


def _collect_spdx3_known_and_package_ids(
    object_set: spdx3.SHACLObjectSet,
) -> tuple[set[str], set[str]]:
    """
    Retrieve all known object IDs and package IDs for SPDX 3.

    Known IDs are the objects in the document, the SPDX 3 individuals such as
    ``NoneElement``, and the elements that a collection imports: the
    ``externalSpdxId`` of each ``ExternalMap`` in ``import``.

    Returns:
        tuple: (all_known_ids, all_package_ids)
    """
    all_known_ids = {
        getattr(obj, "spdxId")
        for obj in object_set.objects
        if isinstance(getattr(obj, "spdxId", None), str)
    } | SPDX3_INDIVIDUAL_ELEMENT_IRIS  # NoneElement and the like need no definition
    all_known_ids |= {
        external_id
        for obj in object_set.objects
        for ext_map in getattr(obj, "import_", None) or []
        if isinstance(external_id := getattr(ext_map, "externalSpdxId", None), str)
    }
    package_ids = {
        getattr(obj, "spdxId")
        for obj in object_set.objects
        if isinstance(obj, spdx3.software_Package)
        and isinstance(getattr(obj, "spdxId", None), str)
    }
    return all_known_ids, package_ids


def analyze_graph_connectivity(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None
) -> tuple[set[str], set[str], dict[str, list[str]], bool]:
    """
    Analyze graph connectivity to find reachable components and unknown pointers.

    Connectivity is evaluated at the component (package) level because
    components represent the primary unit of software conformance in
    minimum elements standards.

    Returns:
        tuple: (reachable_component_ids, floating_component_ids,
            unknown_pointer_edges, has_unknown_pointers)
    """
    if not parsed_data or (sbom_spec == "spdx3" and not spdx3_doc):
        return set(), set(), {}, False

    reachable_node_ids, connection_map = get_reachable_nodes(
        sbom_spec, parsed_data, spdx3_doc
    )
    all_known_ids: set[str] = set()
    all_package_ids: set[str] = set()

    if sbom_spec == "spdx2":
        spdx2_doc = cast("Document", parsed_data)
        all_known_ids, all_package_ids = _collect_spdx2_known_and_package_ids(spdx2_doc)
        all_known_ids |= _collect_spdx2_external_element_ids(
            spdx2_doc, connection_map, reachable_node_ids
        )
    elif sbom_spec == "spdx3":
        all_known_ids, all_package_ids = _collect_spdx3_known_and_package_ids(
            cast("spdx3.SHACLObjectSet", parsed_data)
        )

    reachable_component_ids = reachable_node_ids & all_package_ids

    # Find exactly which edges point to unknown nodes
    unknown_pointer_edges: dict[str, list[str]] = {}
    for source_id, target_ids in connection_map.items():
        missing_targets = [t for t in target_ids if t not in all_known_ids]
        if missing_targets:
            unknown_pointer_edges[source_id] = missing_targets

    floating_component_ids = all_package_ids - reachable_component_ids
    has_unknown_pointers = bool(unknown_pointer_edges)

    if not reachable_node_ids.issubset(all_known_ids) and not has_unknown_pointers:
        logging.error(
            "Traversal bug: BFS reached a node absent from all_known_ids, "
            "but unknown_pointer_edges did not record it."
        )

    return (
        reachable_component_ids,
        floating_component_ids,
        unknown_pointer_edges,
        has_unknown_pointers,
    )


def _build_spdx2_graph(spdx2_doc: "Document") -> tuple[list[str], dict[str, list[str]]]:
    """
    Build the initial queue and connection map for SPDX 2.

    Edges point from parent to child. A forward relationship such as
    ``A CONTAINS B`` adds an edge from A to B. A reverse relationship such as
    ``B CONTAINED_BY A`` or ``B BUILD_DEPENDENCY_OF A`` also adds an edge
    from A to B (see ``VALID_SPDX2_REVERSE_COMPOSITION_RELATIONSHIPS``).
    """
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
        # DESCRIBED_BY is a reverse of DESCRIBES
        elif rel.relationship_type == RelationshipType.DESCRIBED_BY and target_id in (
            doc_id,
            "SPDXRef-DOCUMENT",
        ):
            queue.append(source_id)

        # Build the graph connection map
        rel_name = rel.relationship_type.name
        if rel_name in VALID_SPDX2_COMPOSITION_RELATIONSHIPS:
            graph_connection_map.setdefault(source_id, []).append(target_id)
        elif rel_name in VALID_SPDX2_REVERSE_COMPOSITION_RELATIONSHIPS:
            graph_connection_map.setdefault(target_id, []).append(source_id)
    return queue, graph_connection_map


def _extract_spdx3_relationship_edges(
    obj: spdx3.Relationship, graph_connection_map: dict[str, list[str]]
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
    obj: spdx3.ElementCollection, graph_connection_map: dict[str, list[str]]
) -> None:
    """Helper to extract implicit collection edges (e.g. Sbom, Document)."""
    col_id = getattr(obj, "spdxId", None)
    if not col_id:
        return

    if col_id not in graph_connection_map:
        graph_connection_map[col_id] = []

    for elem in getattr(obj, "rootElement", []):
        e_id = elem if isinstance(elem, str) else getattr(elem, "spdxId", "")
        if e_id:
            graph_connection_map[col_id].append(e_id)


def _build_spdx3_graph(
    object_set: spdx3.SHACLObjectSet, spdx3_doc: spdx3.SpdxDocument | None
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
        if isinstance(obj, spdx3.Relationship):
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
        if isinstance(obj, spdx3.ElementCollection):
            _extract_spdx3_collection_edges(obj, graph_connection_map)

    return queue, graph_connection_map


def get_reachable_nodes(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None
) -> tuple[set[str], dict[str, list[str]]]:
    """
    Get all nodes connected to the root by using Breadth-First Search.

    Returns:
        tuple: (reachable_node_ids, graph_connection_map)
    """
    if not parsed_data or (sbom_spec == "spdx3" and not spdx3_doc):
        return set(), {}

    queue: list[str] = []
    graph_connection_map: dict[str, list[str]] = {}

    # SPDX 2
    if sbom_spec == "spdx2":
        queue, graph_connection_map = _build_spdx2_graph(parsed_data)

    # SPDX 3
    if sbom_spec == "spdx3":
        queue, graph_connection_map = _build_spdx3_graph(parsed_data, spdx3_doc)

    reachable_node_ids: set[str] = set(queue)

    # Perform BFS to find all reachable nodes
    while queue:
        current_id = queue.pop(0)

        if current_id in graph_connection_map:
            for target_id in graph_connection_map[current_id]:
                if target_id not in reachable_node_ids:
                    reachable_node_ids.add(target_id)
                    queue.append(target_id)

    return reachable_node_ids, graph_connection_map
