# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Helpers for SPDX 3."""

from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING, Any, Union

from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.validation.validation_message import (
    ValidationContext,
    ValidationMessage,
)

if TYPE_CHECKING:
    from collections.abc import Iterator


#: SPDX 3.0.1 individuals for no value or an unknown value, not an element:
#: Core NoneElement ("a set of Elements with cardinality (number/count) of
#: zero"), NoAssertionElement ("a set of Elements of unknown identify or
#: cardinality (number)"), ExpandedLicensing NoneLicense ("no license is
#: present") and NoAssertionLicense ("no assertion can be made about its
#: actual value").
SPDX3_NONE_AND_NOASSERTION_IRIS: frozenset[str] = frozenset(
    iri
    for cls in (
        spdx3.IndividualElement,
        spdx3.expandedlicensing_IndividualLicensingInfo,
    )
    for iri in cls.NAMED_INDIVIDUALS.values()
)

#: SPDX 3.0.1 individuals a document may refer to without defining them: the
#: none and no-assertion values above, and ``SpdxOrganization``.
SPDX3_INDIVIDUAL_ELEMENT_IRIS: frozenset[str] = (
    SPDX3_NONE_AND_NOASSERTION_IRIS
    | frozenset(spdx3.Organization.NAMED_INDIVIDUALS.values())
)


def get_spdx3_element_id(value: Any) -> str:
    """
    Return the SPDX ID of an SPDX 3 element, or of an element reference.

    A reference to an element may be the element itself or its IRI as a
    string, as in ``Relationship.from_`` and ``Relationship.to``.

    Args:
        value: An SPDX 3 element, an IRI, or None.

    Returns:
        str: The SPDX ID, or an empty string if there is none.
    """
    if isinstance(value, str):
        return value
    spdx_id = getattr(value, "spdxId", "")
    return spdx_id if isinstance(spdx_id, str) else ""


def validate_spdx3_data(
    object_set: spdx3.SHACLObjectSet,
) -> tuple[spdx3.SpdxDocument | None, list[ValidationMessage]]:
    """
    Validate an SHACLObjectSet if it contains a valid SpdxDocument.

    The SPDX 3.0 specification states that "Any instance of serialization of
    SPDX data shall not contain more than one SpdxDocument element definition."

    See: https://spdx.github.io/spdx-spec/latest/model/Core/Classes/SpdxDocument/

    Args:
        object_set (spdx3.SHACLObjectSet): The SHACLObjectSet containing
                                            the SPDX 3 document.
    Returns:
        spdx3.SpdxDocument | None: An SpdxDocument if found, otherwise None.
        list[ValidationMessage]: A list of validation messages. Empty if no errors.

    """
    # Note that we use spdx_tools.spdx.validation.validation_message,
    # which is originally meant for SPDX 2, to report validation errors for
    # SPDX 3 as well, so the print/HTML/JSON output functions can be reused.

    doc: spdx3.SpdxDocument | None = None
    validation_messages: list[ValidationMessage] = []

    spdx_documents: list[spdx3.SpdxDocument] = list(
        object_set.foreach_type(spdx3.SpdxDocument)
    )

    # == SPDX 3 JSON serialization constraint =====

    # Collections of SPDX 3 Elements shall be inside SpdxDocument
    if not spdx_documents:
        error_msg = (
            "No SpdxDocument object found in the SPDX 3 JSON file. "
            "Expected exactly one."
        )
        validation_messages.append(ValidationMessage(error_msg, ValidationContext()))
        return (doc, validation_messages)

    if len(spdx_documents) != 1:
        error_msg = (
            "Multiple SpdxDocument objects found in the SPDX 3 JSON file. "
            "Allows no more than one. "
            "Ref: https://spdx.github.io/spdx-spec/latest/model/Core/Classes/SpdxDocument/"
        )
        validation_messages.append(ValidationMessage(error_msg, ValidationContext()))
        return (doc, validation_messages)

    # == ElementCollection constraint =====
    # SpdxDocument is an ElementCollection.

    doc = spdx_documents[0]
    doc_id = getattr(doc, "spdxId", None)
    elements: spdx3.ListProxy[Union[str, spdx3.Element]] = doc.element
    root_elements: spdx3.ListProxy[Union[str, spdx3.Element]] = doc.rootElement

    # ElementCollection constraint: if there is at least one element,
    # there shall also be at least one rootElement.
    # Ref: https://spdx.github.io/spdx-spec/latest/model/Core/Classes/ElementCollection/
    if elements and not root_elements:
        error_msg = (
            "The SpdxDocument has elements but no rootElement. "
            "An SpdxDocument with at least one element shall also have "
            "at least one rootElement. "
            "Ref: https://spdx.github.io/spdx-spec/latest/model/Core/Classes/ElementCollection/"
        )
        validation_messages.append(
            ValidationMessage(error_msg, ValidationContext(parent_id=doc_id))
        )

    # ElementCollection constraint: element items shall not be of type SpdxDocument.
    # Ref: https://spdx.github.io/spdx-spec/latest/model/Core/Classes/ElementCollection/
    for elem in elements:
        if isinstance(elem, spdx3.SpdxDocument):
            elem_id = getattr(elem, "spdxId", None)
            error_msg = (
                "An SpdxDocument element shall not be of type SpdxDocument. "
                "Ref: https://spdx.github.io/spdx-spec/latest/model/Core/Classes/ElementCollection/"
            )
            context = ValidationContext(parent_id=doc_id, spdx_id=elem_id)
            validation_messages.append(ValidationMessage(error_msg, context))

    # ElementCollection constraint: rootElement items shall not be of type SpdxDocument.
    # Ref: https://spdx.github.io/spdx-spec/latest/model/Core/Classes/ElementCollection/
    for root_elem in root_elements:
        if isinstance(root_elem, spdx3.SpdxDocument):
            root_elem_id = getattr(root_elem, "spdxId", None)
            error_msg = (
                "An SpdxDocument rootElement shall not be of type SpdxDocument. "
                "Ref: https://spdx.github.io/spdx-spec/latest/model/Core/Classes/ElementCollection/"
            )
            context = ValidationContext(parent_id=doc_id, spdx_id=root_elem_id)
            validation_messages.append(ValidationMessage(error_msg, context))

    return (doc, validation_messages)


def get_boms_from_spdx_document(
    spdx_doc: spdx3.SpdxDocument | None,
) -> list[spdx3.Bom]:
    """
    Retrieve the BOMs that are rootElements of an SPDX 3 SpdxDocument.

    Args:
        spdx_doc (spdx3.SpdxDocument | None): The SPDX 3 SpdxDocument.

    Returns:
        list[spdx3.Bom]: A list of BOMs if found, otherwise an empty list.
    """
    if not spdx_doc:
        return []

    return [elem for elem in spdx_doc.rootElement if isinstance(elem, spdx3.Bom)]


def get_packages_from_bom(
    bom: spdx3.Bom | None,
) -> list[spdx3.software_Package]:
    """
    Retrieve the /Software/Packages that are rootElements of an SPDX 3 BOM.

    Args:
        bom (spdx3.Bom | None): The SPDX 3 Bom.

    Returns:
        list[spdx3.software_Package]: A list of packages if found, otherwise an empty list.
    """
    if not bom:
        return []

    return [
        elem for elem in bom.rootElement if isinstance(elem, spdx3.software_Package)
    ]


def iter_objects_with_property(
    object_set: spdx3.SHACLObjectSet,
    typ: type[spdx3.SHACLObject] = spdx3.Artifact,
    property_name: str = "spdxId",
    reachable_ids: set[str] | None = None,
) -> Iterator[tuple[str, str, Any]]:
    """
    Yield (name, spdxId, property) for each SPDX 3 object.

    Objects are yielded sorted by (name, spdxId), as SHACLObjectSet
    iteration order is not stable across runs.

    Args:
        object_set (spdx3.SHACLObjectSet): The SHACLObjectSet to iterate over.
        typ (type[spdx3.SHACLObject]): The type of SPDX3 object
        property_name (str): The property name to retrieve.
        reachable_ids (set[str] | None): A set of reachable SPDX IDs from root.

    Yields:
        Iterator[tuple[str, str, Any]]: A tuple containing the name,
        SPDX ID, and the specified property of the object.
    """

    entries = sorted(
        (
            (
                (getattr(obj, "name", "") or "").strip(),
                (getattr(obj, "spdxId", "") or "").strip(),
                obj,
            )
            for obj in object_set.foreach_type(typ)
        ),
        key=lambda entry: entry[:2],
    )
    for name, spdx_id, obj in entries:
        if reachable_ids is not None and spdx_id not in reachable_ids:
            continue

        property_ = getattr(obj, property_name, None)
        yield name, spdx_id, property_


def iter_relationships_by_type(
    object_set: spdx3.SHACLObjectSet,
    rel_type: str,
) -> Iterator[tuple[str, list[str]]]:
    """
    Yield (from_id, to_ids_list) for each relationship of the specified relationship type.
    """

    for obj in object_set.foreach_type(spdx3.Relationship):
        _rel_type = getattr(obj, "relationshipType", "")
        # Remove the IRI prefix of entry name before compare
        if not _rel_type or _rel_type.split("/")[-1] != rel_type:
            continue
        from_: str | spdx3.Element | None = obj.from_
        to_elements: spdx3.ListProxy[Union[str, spdx3.Element]] = obj.to
        if not from_ or not to_elements:
            continue

        from_id = get_spdx3_element_id(from_)
        to_ids = []
        for to_item in to_elements:
            to_id = get_spdx3_element_id(to_item)
            if to_id:
                to_ids.append(to_id)

        if from_id and to_ids:
            yield from_id, to_ids


def get_all_packages(object_set: spdx3.SHACLObjectSet) -> set[spdx3.software_Package]:
    """
    Retrieve all /Software/Package objects from an SHACLObjectSet.

    This includes instances of software_Package and its subclasses,
    such as ai_AIPackage and dataset_DatasetPackage.
    """
    packages: set[spdx3.software_Package] = set(
        object_set.foreach_type(spdx3.software_Package)
    )
    return packages


def get_all_package_ids(
    object_set: spdx3.SHACLObjectSet, reachable_ids: set[str] | None = None
) -> set[str]:
    """Retrieve spdxId for all /Software/Package objects from an SHACLObjectSet."""
    return {
        spdx_id
        for _name, spdx_id, _ in iter_objects_with_property(
            object_set, spdx3.software_Package, "spdxId", reachable_ids
        )
        if spdx_id
    }


def get_all_element_ids(
    object_set: spdx3.SHACLObjectSet, reachable_ids: set[str] | None = None
) -> set[str]:
    """Retrieve spdxId for all SPDX 3 Element objects from an SHACLObjectSet."""
    return {
        spdx_id
        for _name, spdx_id, _ in iter_objects_with_property(
            object_set, spdx3.Element, "spdxId", reachable_ids
        )
        if spdx_id
    }


def get_distribution_artifacts_map(
    object_set: spdx3.SHACLObjectSet,
) -> dict[str, list[spdx3.software_File]]:
    """
    Create a mapping of package spdxId to their linked software_File distribution artifacts.

    Returns:
        dict[str, list[spdx3.software_File]]: A dictionary mapping package spdxId to a list of
        linked software_File objects.
    """
    artifact_map: dict[str, list[spdx3.software_File]] = {}

    file_map: dict[str, spdx3.software_File] = {}
    for file_obj in object_set.foreach_type(spdx3.software_File):
        file_id = getattr(file_obj, "spdxId", "")
        if file_id:
            file_map[file_id] = file_obj

    for from_id, to_ids in iter_relationships_by_type(
        object_set, "hasDistributionArtifact"
    ):
        files = [file_map[to_id] for to_id in to_ids if to_id in file_map]
        if files:
            artifact_map.setdefault(from_id, []).extend(files)

    return artifact_map


def has_sha512_hash(file_obj: spdx3.SHACLObject) -> bool:
    """
    Check if a software_File has a SHA-512 hash declared in its verifiedUsing property.
    """
    verified_using = getattr(file_obj, "verifiedUsing", [])
    for verification in verified_using:
        if isinstance(verification, spdx3.Hash):
            algorithm = getattr(verification, "algorithm", "")
            hash_value = getattr(verification, "hashValue", "")

            if algorithm and "sha512" in algorithm.lower() and hash_value:
                return True

    return False


def get_dependency_relationships_stated_completeness(
    object_set: spdx3.SHACLObjectSet,
) -> dict[str, list[str | None]]:
    """
    Get the stated completeness of each dependency relationship.

    Dependency relationships are those of type ``contains`` or ``dependsOn``.
    Unlike :func:`get_dependency_relationships_completeness`, an absent
    ``completeness`` is kept as None.

    Args:
        object_set: The SPDX 3 object set.

    Returns:
        dict[str, list[str | None]]: A dictionary mapping each relationship's
        ``from`` SPDX ID to the ``completeness`` of each of its dependency
        relationships (``complete``, ``incomplete`` or ``noAssertion``), or
        None where ``completeness`` is absent.
    """
    completeness_map: dict[str, list[str | None]] = {}

    for obj in object_set.foreach_type(spdx3.Relationship):
        rel_type = getattr(obj, "relationshipType", "")
        if not rel_type:
            continue

        # Remove the IRI prefix of entry name before compare
        rel_type_name = rel_type.rsplit("/", maxsplit=1)[-1]
        if rel_type_name not in ("contains", "dependsOn"):
            continue

        from_id = get_spdx3_element_id(getattr(obj, "from_", None))
        if from_id:
            completeness_iri = getattr(obj, "completeness", None)
            completeness_map.setdefault(from_id, []).append(
                completeness_iri.rsplit("/", maxsplit=1)[-1]
                if completeness_iri
                else None
            )

    return completeness_map


def get_dependency_relationships_completeness(
    object_set: spdx3.SHACLObjectSet,
) -> dict[str, list[str]]:
    """
    Extract the completeness attribute for all dependency
    relationships ('contains', 'dependsOn') in the SPDX 3 document.

    An absent ``completeness`` is reported as ``noAssertion``.

    Args:
        object_set: The SPDX 3 object set.

    Returns:
        dict[str, list[str]]: A dictionary mapping each relationship's
        ``from`` SPDX ID to the ``completeness`` of each of its dependency
        relationships (``complete``, ``incomplete`` or ``noAssertion``).
    """
    return {
        from_id: [value or "noAssertion" for value in values]
        for from_id, values in get_dependency_relationships_stated_completeness(
            object_set
        ).items()
    }


def parse_spdx3_file(file_path: str) -> tuple[spdx3.SHACLObjectSet | None, list[str]]:
    """
    Parse SPDX 3 SBOM document.

    Returns:
        tuple[spdx3.SHACLObjectSet | None, list[str]]: A tuple containing the parsed
            SHACLObjectSet (or None if parsing failed) and a list of parsing error strings.
    """
    parsing_errors: list[str] = []

    if not file_path or file_path.strip() == "":
        logging.error("No file path provided.")
        return None, parsing_errors

    if not os.path.exists(file_path):
        logging.error("File not found: %s", file_path)
        return None, parsing_errors

    object_set: spdx3.SHACLObjectSet = spdx3.SHACLObjectSet()
    try:
        with open(file_path, "rb") as f:
            spdx3.JSONLDDeserializer().read(f, object_set)
    except (
        OSError,
        ValueError,
        KeyError,
        TypeError,
        AttributeError,
        NotImplementedError,
    ) as err:
        # json.JSONDecodeError is a ValueError. JSON that is not SPDX 3 JSON-LD
        # raises the others, e.g. NotImplementedError for an abstract type.
        logging.warning("SPDX3 deserialization failed: %s", err)
        parsing_errors.append(str(err))
        return None, parsing_errors

    return object_set, parsing_errors
