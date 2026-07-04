# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Helpers for SPDX 3."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

from spdx_python_model.bindings import v3_0_1 as spdx3
from spdx_tools.spdx.validation.validation_message import (
    ValidationContext,
    ValidationMessage,
)

if TYPE_CHECKING:
    from collections.abc import Iterator


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
) -> list[spdx3.Bom] | None:
    """
    Retrieve the BOMs that are rootElements of an SPDX 3 SpdxDocument.

    Args:
        spdx_doc (spdx3.SpdxDocument | None): The SPDX 3 SpdxDocument.

    Returns:
        list[spdx3.Bom] | None: A list of BOMs if found, otherwise None.
    """
    if not spdx_doc:
        return None

    root_elements: list[spdx3.Bom] = getattr(spdx_doc, "rootElement", [])
    if not root_elements:
        return None

    return root_elements


def get_packages_from_bom(
    bom: spdx3.Bom | None,
) -> list[spdx3.software_Package] | None:
    """
    Retrieve the /Software/Packages that are rootElements of an SPDX 3 BOM.

    Args:
        bom (spdx3.Bom | None): The SPDX 3 Bom.

    Returns:
        list[spdx3.software_Package] | None: A list of packages if found, otherwise None.
    """
    if not bom:
        return None

    root_elements: list[spdx3.software_Package] = getattr(bom, "rootElement", [])
    if not root_elements or len(root_elements) != 1:
        return None

    return root_elements


def iter_objects_with_property(
    object_set: spdx3.SHACLObjectSet,
    typ: type[spdx3.SHACLObject] = spdx3.Artifact,
    property_name: str = "spdxId",
) -> Iterator[tuple[str, str, Any]]:
    """
    Yield (name, spdxId, property) for each SPDX 3 object.

    Args:
        object_set (spdx3.SHACLObjectSet): The SHACLObjectSet to iterate over.
        typ (type[spdx3.SHACLObject]): The type of SPDX3 object
        property_name (str): The property name to retrieve.

    Yields:
        Iterator[tuple[str, str, Any]]: A tuple containing the name,
        SPDX ID, and the specified property of the object.
    """

    for obj in object_set.foreach_type(typ):
        name = (getattr(obj, "name", "") or "").strip()
        spdx_id = (getattr(obj, "spdxId", "") or "").strip()
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

        from_id = from_ if isinstance(from_, str) else getattr(from_, "spdxId", "")
        to_ids = []
        for to_item in to_elements:
            to_id = (
                to_item if isinstance(to_item, str) else getattr(to_item, "spdxId", "")
            )
            if to_id:
                to_ids.append(to_id)

        if from_id and to_ids:
            yield from_id, to_ids


def get_all_packages(object_set: spdx3.SHACLObjectSet) -> set[spdx3.software_Package]:
    """Retrieve all /Software/Package objects from an SHACLObjectSet."""
    packages: set[spdx3.software_Package] = set(
        object_set.foreach_type(spdx3.software_Package)
    )
    return packages
