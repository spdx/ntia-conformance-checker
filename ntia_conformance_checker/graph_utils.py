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
    SPDX2_DEPENDENCY_RELATIONSHIP_TYPES,
    SPDX2_RELATIONSHIP_TRAVERSAL,
    SPDX3_DEPENDENCY_RELATIONSHIP_TYPES,
    SPDX3_RELATIONSHIP_TRAVERSAL,
    TraversalDirection,
)
from .spdx3_utils import (
    SPDX3_INDIVIDUAL_ELEMENT_IRIS,
    SPDX3_NONE_AND_NOASSERTION_IRIS,
    get_spdx3_element_id,
)

if TYPE_CHECKING:
    from spdx_tools.spdx.model.document import Document


# Values that SPDX 2.3 clause 11.1 (Table 69) allows as the related element
# of a relationship instead of an element: there are no other relationships
# (NONE), or it is not known (NOASSERTION). spdx-tools reads them as
# SpdxNone and SpdxNoAssertion, whose str() is the keyword.
_SPDX2_NO_ELEMENT_VALUES = frozenset({"NONE", "NOASSERTION"})

# SPDX 3.0.1 NoneElement and NoAssertionElement, the element counterparts.
_SPDX3_NO_ELEMENT_VALUES = frozenset(spdx3.IndividualElement.NAMED_INDIVIDUALS.values())

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
    all_known_ids: set[str] = set(SPDX3_INDIVIDUAL_ELEMENT_IRIS)  # NoneElement etc.
    package_ids: set[str] = set()
    for obj in object_set.objects:
        spdx_id = getattr(obj, "spdxId", None)
        if isinstance(spdx_id, str):
            all_known_ids.add(spdx_id)
            if isinstance(obj, spdx3.software_Package):
                package_ids.add(spdx_id)
        for ext_map in getattr(obj, "import_", None) or []:
            external_id = getattr(ext_map, "externalSpdxId", None)
            if isinstance(external_id, str):
                all_known_ids.add(external_id)
    return all_known_ids, package_ids


def _find_unknown_pointer_edges(
    written_relationships: list[tuple[str, str]], is_known: Callable[[str], bool]
) -> tuple[dict[str, list[str]], set[str]]:
    """
    Find relationships, as written, with a missing element at either end.

    This checks the graph shape, not the traversal. Either end can be an
    element ID (SPDX 2.3 §11.1 Table 69), so either can be missing; the
    missing element IDs tell which.

    Args:
        written_relationships: (source ID, target ID) pairs as written.
        is_known: Whether an element ID refers to an element that exists.

    Returns:
        tuple: (unknown_pointer_edges, missing_element_ids), where
            unknown_pointer_edges maps a source ID to its target IDs, each
            listed once, for relationships with a missing end.
    """
    targets_by_source: dict[str, dict[str, None]] = {}
    missing_element_ids: set[str] = set()
    for source_id, target_id in written_relationships:
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
            return (
                element_id in known_ids
                or element_id in _SPDX2_NO_ELEMENT_VALUES
                or _is_spdx2_external_element_id(element_id, external_doc_ref_ids)
            )

        return is_known, package_ids
    if sbom_spec == "spdx3":
        known_ids, package_ids = _collect_spdx3_known_and_package_ids(
            cast("spdx3.SHACLObjectSet", parsed_data)
        )
        return known_ids.__contains__, package_ids
    return lambda _: False, set()


@dataclass
class _Graph:
    """
    A relationship graph built from an SBOM.

    Attributes:
        roots: Root element IDs.
        traversal_edges: How the checker walks the graph, parent to children.
        written_relationships: The graph shape: followed and root
            relationships as written, (source, target), checked for missing
            elements.
        dependency_links: Relationships of a type that counts as a dependency
            relationship, as (parent, child) in walking direction. The child
            may be a none or no-assertion value.
        non_component_ids: Documents and collections, which are never an end
            of a dependency relationship.
    """

    roots: list[str] = field(default_factory=list)
    traversal_edges: dict[str, list[str]] = field(default_factory=dict)
    written_relationships: list[tuple[str, str]] = field(default_factory=list)
    dependency_links: list[tuple[str, str]] = field(default_factory=list)
    non_component_ids: set[str] = field(default_factory=set)

    def add_dependency_link(
        self, source_id: str, target_id: str, direction: TraversalDirection
    ) -> None:
        """Add a dependency relationship written from source to target."""
        if direction is TraversalDirection.ALONG:
            self.dependency_links.append((source_id, target_id))
        else:
            self.dependency_links.append((target_id, source_id))


def _has_dependency_relationship(
    graph: _Graph,
    reachable_node_ids: set[str],
    is_known: Callable[[str], bool],
    no_element_values: frozenset[str],
) -> bool:
    """
    Check whether a reachable element declares a dependency relationship.

    NTIA 2021 (IV. Minimum Elements > Data Fields > Dependency Relationship)
    relates components: "an upstream component X is included in software Y".
    So the parent must be a reachable element that is not a document or a
    collection, and the child a different element that exists, here or in a
    declared external or imported document, and is not a document either.

    The child may also be a none or no-assertion value: NTIA 2021 (IV. Minimum
    Elements > Practices and Processes > Known Unknowns) says the author
    "should affirmatively state ... when a component has no further
    dependencies", and that this "is implemented in the dependency
    relationship data field".

    Args:
        graph: The relationship graph.
        reachable_node_ids: Element IDs reachable from the roots.
        is_known: Whether an element ID refers to an element that exists.
        no_element_values: The none and no-assertion values of the format.

    Returns:
        bool: True if such a relationship exists.
    """

    def is_component(element_id: str) -> bool:
        return (
            element_id not in graph.non_component_ids
            # An external document itself, e.g. DocumentRef-x:SPDXRef-DOCUMENT
            and not element_id.endswith(":SPDXRef-DOCUMENT")
        )

    for parent_id, child_id in graph.dependency_links:
        if parent_id == child_id or parent_id not in reachable_node_ids:
            continue
        if not is_component(parent_id):
            continue
        if child_id in no_element_values or (
            is_known(child_id) and is_component(child_id)
        ):
            return True
    return False


@dataclass(frozen=True)
class GraphConnectivity:
    """
    Result of a graph connectivity analysis.

    Attributes:
        reachable_component_ids: Packages reachable from the roots.
        floating_component_ids: Packages not reachable from the roots.
        unknown_pointer_edges: Relationships with a missing end, as written:
            source ID to target IDs (see ``_find_unknown_pointer_edges``).
        missing_element_ids: IDs of the missing elements, at either end of
            those relationships.
        has_dependency_relationship: Whether a reachable element declares a
            dependency relationship (see ``_has_dependency_relationship``).
    """

    reachable_component_ids: set[str] = field(default_factory=set)
    floating_component_ids: set[str] = field(default_factory=set)
    unknown_pointer_edges: dict[str, list[str]] = field(default_factory=dict)
    missing_element_ids: set[str] = field(default_factory=set)
    has_dependency_relationship: bool = False

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
            missing elements, the missing element IDs, and whether a
            dependency relationship is declared.
    """
    if not parsed_data or (sbom_spec == "spdx3" and not spdx3_doc):
        return GraphConnectivity()

    reachable_node_ids, graph = _reach(sbom_spec, parsed_data, spdx3_doc)

    is_known, all_package_ids = _get_known_predicate_and_package_ids(
        sbom_spec, parsed_data
    )
    unknown_pointer_edges, missing_element_ids = _find_unknown_pointer_edges(
        graph.written_relationships, is_known
    )
    no_element_values = (
        _SPDX2_NO_ELEMENT_VALUES if sbom_spec == "spdx2" else _SPDX3_NO_ELEMENT_VALUES
    )

    reachable_component_ids = reachable_node_ids & all_package_ids
    result = GraphConnectivity(
        reachable_component_ids=reachable_component_ids,
        floating_component_ids=all_package_ids - reachable_component_ids,
        unknown_pointer_edges=unknown_pointer_edges,
        missing_element_ids=missing_element_ids,
        has_dependency_relationship=_has_dependency_relationship(
            graph, reachable_node_ids, is_known, no_element_values
        ),
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
            unknown_pointer_edges maps a source ID to target IDs, for
            relationships with a missing end, as written (see
            ``_find_unknown_pointer_edges``).
    """
    result = analyze_graph(sbom_spec, parsed_data, spdx3_doc)
    return (
        result.reachable_component_ids,
        result.floating_component_ids,
        result.unknown_pointer_edges,
        result.has_unknown_pointers,
    )


def _get_spdx2_root_id(
    rel_type: RelationshipType, source_id: str, target_id: str, doc_ids: set[str]
) -> str | None:
    """
    Return the root that a relationship marks, if any.

    ``SPDXRef-DOCUMENT DESCRIBES A`` marks A, and so does
    ``A DESCRIBED_BY SPDXRef-DOCUMENT``, which is DESCRIBES written from the
    described element's side (SPDX 2.3 clause 11.1, Table 68).
    """
    if rel_type == RelationshipType.DESCRIBES and source_id in doc_ids:
        return target_id
    if rel_type == RelationshipType.DESCRIBED_BY and target_id in doc_ids:
        return source_id
    return None


def _build_spdx2_graph(spdx2_doc: "Document") -> _Graph:
    """
    Build the relationship graph for SPDX 2.

    Roots are the elements that the document describes: ``SPDXRef-DOCUMENT
    DESCRIBES A`` or ``A DESCRIBED_BY SPDXRef-DOCUMENT`` (SPDX 2.3 clause 11.1,
    Table 68; the document ID is from clause 6.3).

    Edges point from parent to child. ``A CONTAINS B`` is walked along its
    written direction and adds an edge from A to B. A reverse relationship
    type, written from the child's side, such as ``B CONTAINED_BY A`` or
    ``B BUILD_DEPENDENCY_OF A``, is walked against it and also adds an edge
    from A to B. ``SPDX2_RELATIONSHIP_TRAVERSAL`` holds the direction of each
    type.

    ``NONE`` and ``NOASSERTION`` state that there are no relationships or
    that it is not known (Table 69). They are not elements, so they add no
    edge, but a followed relationship to them is still a written relationship,
    so that its ``spdxElementId`` is checked, and still a dependency link.

    Returns:
        _Graph: The graph; written relationships are
            (spdxElementId, relatedSpdxElement).
    """
    doc_ids = _get_spdx2_doc_ids(spdx2_doc)
    graph = _Graph(non_component_ids=set(doc_ids))

    for rel in spdx2_doc.relationships or []:
        source_id = rel.spdx_element_id
        target_id = rel.related_spdx_element_id
        rel_name = rel.relationship_type.name
        direction = SPDX2_RELATIONSHIP_TRAVERSAL.get(rel_name)
        is_dependency = rel_name in SPDX2_DEPENDENCY_RELATIONSHIP_TYPES

        # spdx_element_id is always an ID; related_spdx_element_id can also
        # be NONE or NOASSERTION
        if not isinstance(target_id, str):
            # NONE or NOASSERTION: no element to link to, but the source must
            # exist, as in SPDX 3 for a relationship to NoneElement
            if direction is not None:
                graph.written_relationships.append((source_id, str(target_id)))
            # Only "A <type> NONE" walked along says what A depends on
            if is_dependency and direction is TraversalDirection.ALONG:
                graph.dependency_links.append((source_id, str(target_id)))
            continue

        root_id = _get_spdx2_root_id(
            rel.relationship_type, source_id, target_id, doc_ids
        )
        is_root_link = root_id is not None
        if root_id is not None:
            graph.roots.append(root_id)

        # Build the graph connection map
        if direction is TraversalDirection.ALONG:
            graph.traversal_edges.setdefault(source_id, []).append(target_id)
        elif direction is TraversalDirection.AGAINST:
            graph.traversal_edges.setdefault(target_id, []).append(source_id)

        if is_root_link or direction is not None:
            graph.written_relationships.append((source_id, target_id))
        if is_dependency and direction is not None:
            graph.add_dependency_link(source_id, target_id, direction)
    return graph


def _extract_spdx3_relationship_edges(obj: spdx3.Relationship, graph: _Graph) -> None:
    """
    Helper to extract explicit relationship edges.

    The graph gets traversal edges from parent to child (see
    ``SPDX3_RELATIONSHIP_TRAVERSAL``), the relationship as written, ``from``
    to each ``to``, to check for missing elements, and, for a type in
    ``SPDX3_DEPENDENCY_RELATIONSHIP_TYPES``, dependency links.
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

    graph.written_relationships.extend((from_id, to_id) for to_id in to_ids)
    if rel_name in SPDX3_DEPENDENCY_RELATIONSHIP_TYPES:
        for to_id in to_ids:
            graph.add_dependency_link(from_id, to_id, direction)

    # None and no-assertion values (SPDX3_NONE_AND_NOASSERTION_IRIS) are not
    # elements, and unrelated relationships share them, so they get no
    # traversal edges; the written relationship still checks the other end.
    # SpdxOrganization is one real element and stays a node.
    if from_id in SPDX3_NONE_AND_NOASSERTION_IRIS:
        return
    to_ids = [t for t in to_ids if t not in SPDX3_NONE_AND_NOASSERTION_IRIS]
    if direction is TraversalDirection.ALONG:
        graph.traversal_edges.setdefault(from_id, []).extend(to_ids)
    else:
        for to_id in to_ids:
            graph.traversal_edges.setdefault(to_id, []).append(from_id)


def _extract_spdx3_collection_edges(
    obj: spdx3.ElementCollection, graph: _Graph
) -> None:
    """
    Helper to extract implicit collection edges (e.g. Sbom, Document).

    The graph gets a traversal edge from the collection to each of its
    ``rootElement``, the same (collection, root element) pairs as written
    relationships, to check for missing elements, and the collection as a
    non-component.
    """
    col_id = get_spdx3_element_id(obj)
    if not col_id:
        return

    root_ids = [
        r for r in map(get_spdx3_element_id, getattr(obj, "rootElement", [])) if r
    ]
    graph.non_component_ids.add(col_id)
    graph.traversal_edges.setdefault(col_id, []).extend(root_ids)
    graph.written_relationships.extend((col_id, root_id) for root_id in root_ids)


def _build_spdx3_graph(
    object_set: spdx3.SHACLObjectSet, spdx3_doc: spdx3.SpdxDocument | None
) -> _Graph:
    """
    Build the relationship graph for SPDX 3.

    Roots are the ``rootElement`` of the ``SpdxDocument`` and the targets of
    relationships of any type from the ``SpdxDocument``. Each collection,
    such as an ``Sbom``, links to its own ``rootElement``.

    Returns:
        _Graph: The graph; written relationships are the followed
            relationships, the relationships from the document and the
            collection roots, as written: (from, to).
    """
    graph = _Graph()

    doc_id = get_spdx3_element_id(spdx3_doc) if spdx3_doc else ""
    if doc_id:
        graph.non_component_ids.add(doc_id)

    if spdx3_doc and getattr(spdx3_doc, "rootElement", None):
        graph.roots.extend(
            r for r in map(get_spdx3_element_id, spdx3_doc.rootElement) if r
        )

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
                graph.roots.extend(to_ids)
                graph.written_relationships.extend((doc_id, to_id) for to_id in to_ids)

            # Normal relationships between packages build the map
            else:
                _extract_spdx3_relationship_edges(obj, graph)

        # Capture implicit relationships from Collections (like Sbom, Bom, etc.)
        if isinstance(obj, spdx3.ElementCollection):
            _extract_spdx3_collection_edges(obj, graph)

    return graph


def _build_graph(sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None) -> _Graph:
    """
    Build the relationship graph of an SBOM.

    The traversal edges are how the checker walks the graph, from parent to
    child. The written relationships are the graph shape, as the SBOM states
    it, and are checked for missing elements.

    Returns:
        _Graph: The graph; empty for an unsupported specification.
    """
    if sbom_spec == "spdx2":
        return _build_spdx2_graph(parsed_data)
    if sbom_spec == "spdx3":
        return _build_spdx3_graph(parsed_data, spdx3_doc)
    return _Graph()


def _traverse(queue: list[str], traversal_edges: dict[str, list[str]]) -> set[str]:
    """
    Find all nodes reachable from the roots by using Breadth-First Search.

    Args:
        queue: Root node IDs.
        traversal_edges: Edges from parent to children.

    Returns:
        set[str]: Reachable node IDs, roots included.
    """
    reachable_node_ids: set[str] = set(queue)
    pending = deque(queue)
    while pending:
        current_id = pending.popleft()
        for target_id in traversal_edges.get(current_id, []):
            if target_id not in reachable_node_ids:
                reachable_node_ids.add(target_id)
                pending.append(target_id)
    return reachable_node_ids


def _reach(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None
) -> tuple[set[str], _Graph]:
    """
    Build the graph and find all nodes reachable from the roots.

    Returns:
        tuple: (reachable_node_ids, graph); empty when there is no data, or
            no SPDX 3 document.
    """
    if not parsed_data or (sbom_spec == "spdx3" and not spdx3_doc):
        return set(), _Graph()

    graph = _build_graph(sbom_spec, parsed_data, spdx3_doc)
    return _traverse(graph.roots, graph.traversal_edges), graph


def get_reachable_nodes(
    sbom_spec: str, parsed_data: Any, spdx3_doc: Any = None
) -> tuple[set[str], dict[str, list[str]]]:
    """
    Get all nodes connected to the root by using Breadth-First Search.

    Returns:
        tuple: (reachable_node_ids, traversal_edges), where
            traversal_edges holds edges in traversal direction, from
            parent to child. A relationship walked against its written
            direction is an edge from its target to its source, such as
            SPDX 2 ``A CONTAINED_BY B`` or SPDX 3 ``A generates B`` (from B
            to A).
    """
    reachable_node_ids, graph = _reach(sbom_spec, parsed_data, spdx3_doc)
    return reachable_node_ids, graph.traversal_edges
