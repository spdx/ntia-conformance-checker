# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Graph utilities for SPDX 2 and SPDX 3."""

import logging
import re
from collections import deque
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Callable, cast

from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.model.relationship import RelationshipType

from .constants import (
    SPDX2_RELATIONSHIP_TRAVERSAL,
    SPDX3_RELATIONSHIP_TRAVERSAL,
    TraversalDirection,
)
from .spdx3_utils import SPDX3_INDIVIDUAL_ELEMENT_IRIS, get_spdx3_element_id

if TYPE_CHECKING:
    from spdx_tools.spdx.model.document import Document


# SPDX 2 element ID: "SPDXRef-"[idstring], where idstring has letters,
# numbers, "." and "-" (SPDX 2.3 clauses 7.2, 8.2, 9.1).
_SPDX2_SPDXID_PATTERN = re.compile(r"SPDXRef-[A-Za-z0-9.\-]+")


def _get_spdx2_doc_id(spdx2_doc: "Document") -> str:
    """Return the SPDX ID of an SPDX 2 document, ``SPDXRef-DOCUMENT`` by default."""
    creation_info = getattr(spdx2_doc, "creation_info", None)
    doc_id = getattr(creation_info, "spdx_id", None)
    return doc_id if isinstance(doc_id, str) and doc_id else "SPDXRef-DOCUMENT"


def _get_spdx2_doc_ids(spdx2_doc: "Document") -> set[str]:
    """Return the IDs that refer to an SPDX 2 document: its own and ``SPDXRef-DOCUMENT``."""
    return {_get_spdx2_doc_id(spdx2_doc), "SPDXRef-DOCUMENT"}


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

    SPDX 2.3 clause 11.1 (Table 69) writes either end of a relationship as
    ``["DocumentRef-"[idstring]":"]SPDXID``, where the optional prefix is
    "an optional reference to an external SPDX Document as described in 6.6".
    Clause 6.6 declares that prefix in an ``ExternalDocumentRef``.
    The element is defined in the external document, not in this one, so it
    exists when its prefix is declared. The external document itself is
    ``DocumentRef-<idstring>:SPDXRef-DOCUMENT``.

    Args:
        element_id: Element ID used in a relationship.
        external_doc_ref_ids: Declared external document reference IDs.

    Returns:
        bool: True if the ID is ``<declared DocumentRef>:<SPDXID>``, where
            SPDXID is ``SPDXRef-<idstring>`` and idstring has only letters,
            numbers, "." and "-" (clause 7.2 and others).
    """
    doc_ref_id, separator, local_id = element_id.partition(":")
    return (
        bool(separator)
        and doc_ref_id in external_doc_ref_ids
        and _SPDX2_SPDXID_PATTERN.fullmatch(local_id) is not None
    )


def _collect_spdx2_known_and_package_ids(
    spdx2_doc: "Document",
) -> tuple[set[str], set[str]]:
    """
    Retrieve known entity IDs (packages, files, snippets, document) and package IDs for SPDX 2.

    The document is known by its own ID and by ``SPDXRef-DOCUMENT``, the ID
    that clause 6.3 requires and that root detection also accepts.

    Returns:
        tuple: (all_known_ids, all_package_ids)
    """

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
    all_known_ids = package_ids | file_ids | snippet_ids | _get_spdx2_doc_ids(spdx2_doc)
    return all_known_ids, package_ids


def _collect_spdx3_known_and_package_ids(
    object_set: spdx3.SHACLObjectSet,
) -> tuple[set[str], set[str]]:
    """
    Retrieve all known object IDs and package IDs for SPDX 3.

    Known IDs are the objects in the document, the SPDX 3 individuals such as
    ``NoneElement``, and the elements that a collection imports: the
    ``externalSpdxId`` of each ``ExternalMap`` in ``import``. An imported
    element is defined elsewhere, as an SPDX 2 element in a declared
    ``ExternalDocumentRef`` is.

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


def _find_unknown_pointer_edges(
    links: list[tuple[str, str]], is_known: Callable[[str], bool]
) -> tuple[dict[str, list[str]], set[str]]:
    """
    Find links that have a missing element at either end.

    A link is a followed relationship, or a root link, as written in the
    document: (source, target). SPDX 2.3 clause 11.1 (Table 69) allows an
    element ID at both ends of a relationship, so either end can be missing.

    Links are kept as written, from source to target, whichever end is
    missing. The missing element IDs tell which end is missing.

    Args:
        links: (source ID, target ID) pairs as written.
        is_known: Whether an element ID refers to an element that exists.

    Returns:
        tuple: (unknown_pointer_edges, missing_element_ids), where
            unknown_pointer_edges maps a source ID to its target IDs, each
            listed once, for links with a missing end.
    """
    targets_by_source: dict[str, dict[str, None]] = {}
    missing_element_ids: set[str] = set()
    for source_id, target_id in links:
        missing_ends = {e for e in (source_id, target_id) if not is_known(e)}
        if missing_ends:
            missing_element_ids |= missing_ends
            targets_by_source.setdefault(source_id, {})[target_id] = None
    unknown_pointer_edges = {
        source_id: list(targets) for source_id, targets in targets_by_source.items()
    }
    return unknown_pointer_edges, missing_element_ids


def _get_known_predicate_and_package_ids(
    sbom_spec: str, parsed_data: Any
) -> tuple[Callable[[str], bool], set[str]]:
    """
    Return whether an element ID refers to an element that exists, and the package IDs.

    For SPDX 2, an element in a declared external document exists, but not in
    this document; see ``_is_spdx2_external_element_id``.

    Returns:
        tuple: (is_known, all_package_ids)
    """
    if sbom_spec == "spdx2":
        spdx2_doc = cast("Document", parsed_data)
        known_ids, package_ids = _collect_spdx2_known_and_package_ids(spdx2_doc)
        external_doc_ref_ids = _collect_spdx2_external_document_ref_ids(spdx2_doc)

        def is_known(element_id: str) -> bool:
            return element_id in known_ids or _is_spdx2_external_element_id(
                element_id, external_doc_ref_ids
            )

        return is_known, package_ids
    if sbom_spec == "spdx3":
        known_ids, package_ids = _collect_spdx3_known_and_package_ids(
            cast("spdx3.SHACLObjectSet", parsed_data)
        )
        return known_ids.__contains__, package_ids
    return lambda _: False, set()


@dataclass(frozen=True)
class GraphConnectivity:
    """
    Result of a graph connectivity analysis.

    Attributes:
        reachable_component_ids: Packages reachable from the roots.
        floating_component_ids: Packages not reachable from the roots.
        unknown_pointer_edges: Links with a missing end, as written: source
            ID to target IDs (see ``_find_unknown_pointer_edges``).
        missing_element_ids: IDs of the missing elements, at either end of
            those links.
    """

    reachable_component_ids: set[str] = field(default_factory=set)
    floating_component_ids: set[str] = field(default_factory=set)
    unknown_pointer_edges: dict[str, list[str]] = field(default_factory=dict)
    missing_element_ids: set[str] = field(default_factory=set)

    @property
    def has_unknown_pointers(self) -> bool:
        """Whether a root or a followed relationship links to a missing element."""
        return bool(self.unknown_pointer_edges)


def analyze_graph(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None
) -> GraphConnectivity:
    """
    Analyze graph connectivity to find reachable components and missing elements.

    Connectivity is evaluated at the component (package) level because
    components represent the primary unit of software conformance in
    minimum elements standards.

    Returns:
        GraphConnectivity: Reachable and floating components, links to
            missing elements and the missing element IDs.
    """
    if not parsed_data or (sbom_spec == "spdx3" and not spdx3_doc):
        return GraphConnectivity()

    reachable_node_ids, _, links = _reach(sbom_spec, parsed_data, spdx3_doc)

    is_known, all_package_ids = _get_known_predicate_and_package_ids(
        sbom_spec, parsed_data
    )
    unknown_pointer_edges, missing_element_ids = _find_unknown_pointer_edges(
        links, is_known
    )

    reachable_component_ids = reachable_node_ids & all_package_ids
    result = GraphConnectivity(
        reachable_component_ids=reachable_component_ids,
        floating_component_ids=all_package_ids - reachable_component_ids,
        unknown_pointer_edges=unknown_pointer_edges,
        missing_element_ids=missing_element_ids,
    )

    if not result.has_unknown_pointers and not all(map(is_known, reachable_node_ids)):
        logging.error(
            "Traversal bug: BFS reached a node that is not known, "
            "but unknown_pointer_edges did not record it."
        )

    return result


def analyze_graph_connectivity(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None
) -> tuple[set[str], set[str], dict[str, list[str]], bool]:
    """
    Analyze graph connectivity to find reachable components and unknown pointers.

    Kept for compatibility; ``analyze_graph`` also returns the missing
    element IDs.

    Returns:
        tuple: (reachable_component_ids, floating_component_ids,
            unknown_pointer_edges, has_unknown_pointers), where
            unknown_pointer_edges maps a source ID to target IDs, for links
            with a missing end, as written (see ``_find_unknown_pointer_edges``).
    """
    result = analyze_graph(sbom_spec, parsed_data, spdx3_doc)
    return (
        result.reachable_component_ids,
        result.floating_component_ids,
        result.unknown_pointer_edges,
        result.has_unknown_pointers,
    )


def _build_spdx2_graph(
    spdx2_doc: "Document",
) -> tuple[list[str], dict[str, list[str]], list[tuple[str, str]]]:
    """
    Build the roots, the traversal map and the links to check for SPDX 2.

    Roots are the elements that the document describes: ``SPDXRef-DOCUMENT
    DESCRIBES A`` or ``A DESCRIBED_BY SPDXRef-DOCUMENT`` (SPDX 2.3 clause 11.1,
    Table 68; the document ID is from clause 6.3).

    Edges point from parent to child. A forward relationship such as
    ``A CONTAINS B`` adds an edge from A to B. A reverse relationship such as
    ``B CONTAINED_BY A`` or ``B BUILD_DEPENDENCY_OF A`` also adds an edge
    from A to B. ``SPDX2_RELATIONSHIP_TRAVERSAL`` holds the direction of each
    type.

    ``NONE`` and ``NOASSERTION`` state that there are no relationships or
    that it is not known (Table 69). They are not elements, so they are
    skipped.

    Returns:
        tuple: (queue, graph_connection_map, links), where links are the
            followed and root relationships as written:
            (spdxElementId, relatedSpdxElement).
    """
    queue: list[str] = []
    graph_connection_map: dict[str, list[str]] = {}
    links: list[tuple[str, str]] = []

    doc_ids = _get_spdx2_doc_ids(spdx2_doc)

    for rel in spdx2_doc.relationships or []:
        source_id = rel.spdx_element_id
        target_id = rel.related_spdx_element_id

        if not isinstance(source_id, str) or not isinstance(target_id, str):
            continue

        # Get the root elements
        is_root_link = False
        if rel.relationship_type == RelationshipType.DESCRIBES and source_id in doc_ids:
            queue.append(target_id)
            is_root_link = True
        # DESCRIBED_BY is a reverse of DESCRIBES
        elif (
            rel.relationship_type == RelationshipType.DESCRIBED_BY
            and target_id in doc_ids
        ):
            queue.append(source_id)
            is_root_link = True

        # Build the graph connection map
        direction = SPDX2_RELATIONSHIP_TRAVERSAL.get(rel.relationship_type.name)
        if direction is TraversalDirection.FORWARD:
            graph_connection_map.setdefault(source_id, []).append(target_id)
        elif direction is TraversalDirection.REVERSE:
            graph_connection_map.setdefault(target_id, []).append(source_id)

        if is_root_link or direction is not None:
            links.append((source_id, target_id))
    return queue, graph_connection_map, links


def _extract_spdx3_relationship_edges(
    obj: spdx3.Relationship,
    graph_connection_map: dict[str, list[str]],
    links: list[tuple[str, str]],
) -> None:
    """
    Helper to extract explicit relationship edges.

    ``graph_connection_map`` gets edges in traversal direction, from parent to
    child (see ``SPDX3_RELATIONSHIP_TRAVERSAL``). ``links`` gets the
    relationship as written, ``from`` to each ``to``, to check for missing
    elements.
    """
    rel_type_iri = getattr(obj, "relationshipType", "")
    if not rel_type_iri:
        return

    # Extract the actual name from the IRI (e.g., ".../contains" -> "contains")
    rel_name = rel_type_iri.split("/")[-1]

    direction = SPDX3_RELATIONSHIP_TRAVERSAL.get(rel_name)
    if direction is None:
        return

    from_id = get_spdx3_element_id(getattr(obj, "from_", None))
    if not from_id:
        return

    to_ids = [t for t in map(get_spdx3_element_id, getattr(obj, "to", [])) if t]

    links.extend((from_id, to_id) for to_id in to_ids)
    if direction is TraversalDirection.FORWARD:
        graph_connection_map.setdefault(from_id, []).extend(to_ids)
    else:
        for to_id in to_ids:
            graph_connection_map.setdefault(to_id, []).append(from_id)


def _extract_spdx3_collection_edges(
    obj: spdx3.ElementCollection,
    graph_connection_map: dict[str, list[str]],
    links: list[tuple[str, str]],
) -> None:
    """
    Helper to extract implicit collection edges (e.g. Sbom, Document).

    ``graph_connection_map`` gets an edge from the collection to each of its
    ``rootElement``. ``links`` gets the same (collection, root element) pairs,
    to check for missing elements.
    """
    col_id = get_spdx3_element_id(obj)
    if not col_id:
        return

    root_ids = [
        r for r in map(get_spdx3_element_id, getattr(obj, "rootElement", [])) if r
    ]
    graph_connection_map.setdefault(col_id, []).extend(root_ids)
    links.extend((col_id, root_id) for root_id in root_ids)


def _build_spdx3_graph(
    object_set: spdx3.SHACLObjectSet, spdx3_doc: spdx3.SpdxDocument | None
) -> tuple[list[str], dict[str, list[str]], list[tuple[str, str]]]:
    """
    Build the roots, the traversal map and the links to check for SPDX 3.

    Roots are the ``rootElement`` of the ``SpdxDocument`` and the targets of
    relationships of any type from the ``SpdxDocument``. Each collection,
    such as an ``Sbom``, links to its own ``rootElement``.

    Returns:
        tuple: (queue, graph_connection_map, links), where links are the
            followed relationships, the relationships from the document and
            the collection root links as written: (from, to).
    """
    queue: list[str] = []
    graph_connection_map: dict[str, list[str]] = {}
    links: list[tuple[str, str]] = []

    doc_id = get_spdx3_element_id(spdx3_doc) if spdx3_doc else ""

    if spdx3_doc and getattr(spdx3_doc, "rootElement", None):
        queue.extend(r for r in map(get_spdx3_element_id, spdx3_doc.rootElement) if r)

    # Build the graph connection map
    for obj in object_set.objects:
        # Capture explicit relationships from Relationship objects
        if isinstance(obj, spdx3.Relationship):
            from_id = get_spdx3_element_id(getattr(obj, "from_", None))

            # If a relationship originates from the Document itself,
            # its targets are treated as Roots.
            if doc_id and from_id == doc_id:
                to_ids = [
                    t for t in map(get_spdx3_element_id, getattr(obj, "to", [])) if t
                ]
                queue.extend(to_ids)
                links.extend((doc_id, to_id) for to_id in to_ids)

            # Normal relationships between packages build the map
            else:
                _extract_spdx3_relationship_edges(obj, graph_connection_map, links)

        # Capture implicit relationships from Collections (like Sbom, Bom, etc.)
        if isinstance(obj, spdx3.ElementCollection):
            _extract_spdx3_collection_edges(obj, graph_connection_map, links)

    return queue, graph_connection_map, links


def _build_graph(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None
) -> tuple[list[str], dict[str, list[str]], list[tuple[str, str]]]:
    """
    Build the roots, the traversal map and the links to check for missing elements.

    Returns:
        tuple: (queue, graph_connection_map, links)
    """
    if sbom_spec == "spdx2":
        return _build_spdx2_graph(parsed_data)
    if sbom_spec == "spdx3":
        return _build_spdx3_graph(parsed_data, spdx3_doc)
    return [], {}, []


def _traverse(queue: list[str], graph_connection_map: dict[str, list[str]]) -> set[str]:
    """
    Find all nodes reachable from the roots by using Breadth-First Search.

    Args:
        queue: Root node IDs.
        graph_connection_map: Edges from parent to children.

    Returns:
        set[str]: Reachable node IDs, roots included.
    """
    reachable_node_ids: set[str] = set(queue)
    pending = deque(queue)
    while pending:
        current_id = pending.popleft()
        for target_id in graph_connection_map.get(current_id, []):
            if target_id not in reachable_node_ids:
                reachable_node_ids.add(target_id)
                pending.append(target_id)
    return reachable_node_ids


def _reach(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None
) -> tuple[set[str], dict[str, list[str]], list[tuple[str, str]]]:
    """
    Build the graph and find all nodes reachable from the roots.

    Returns:
        tuple: (reachable_node_ids, graph_connection_map, links); all empty
            when there is no data, or no SPDX 3 document.
    """
    if not parsed_data or (sbom_spec == "spdx3" and not spdx3_doc):
        return set(), {}, []

    queue, graph_connection_map, links = _build_graph(sbom_spec, parsed_data, spdx3_doc)
    return _traverse(queue, graph_connection_map), graph_connection_map, links


def get_reachable_nodes(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None
) -> tuple[set[str], dict[str, list[str]]]:
    """
    Get all nodes connected to the root by using Breadth-First Search.

    Returns:
        tuple: (reachable_node_ids, graph_connection_map), where
            graph_connection_map holds edges in traversal direction, from
            parent to child. A reverse relationship such as
            ``A CONTAINED_BY B`` is an edge from B to A.
    """
    reachable_node_ids, graph_connection_map, _ = _reach(
        sbom_spec, parsed_data, spdx3_doc
    )
    return reachable_node_ids, graph_connection_map
