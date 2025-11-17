# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Helpers for SPDX 3."""

from __future__ import annotations

from typing import Any, Iterator, List, Optional, Set, Tuple, Type, cast

from spdx_python_model import v3_0_1 as spdx3  # type: ignore # import-untyped
from spdx_tools.spdx.validation.validation_message import (
    ValidationContext,
    ValidationMessage,
)


def validate_spdx3_data(
    object_set: spdx3.SHACLObjectSet,
) -> Tuple[Optional[spdx3.SpdxDocument], List[ValidationMessage]]:
    """
    Validate an SHACLObjectSet if it contains a valid SpdxDocument.

    The SPDX 3.0 specification states that "Any instance of serialization of
    SPDX data MUST NOT contain more than one SpdxDocument element definition."

    See: https://spdx.github.io/spdx-spec/v3.0/model/Core/Classes/SpdxDocument/

    For the purpose of BOM/SBOM application, it also requires that the
    SpdxDocument should have a Bom or Software/Sbom as its rootElement.

    See: https://github.com/spdx/ntia-conformance-checker/issues/268

    Args:
        object_set (spdx3.SHACLObjectSet): The SHACLObjectSet containing
                                            the SPDX 3 document.
    Returns:
        Optional[spdx3.SpdxDocument]: An SpdxDocument if found, otherwise None.
        List[ValidationMessage]: A list of validation messages. Empty if no errors.

    """
    # Note that we use spdx_tools.spdx.validation.validation_message,
    # which is originally meant for SPDX 2, to report validation errors for
    # SPDX 3 as well, so the print/HTML/JSON output functions can be reused.

    doc: Optional[spdx3.SpdxDocument] = None
    validation_messages: List[ValidationMessage] = []

    spdx_documents: List[spdx3.SpdxDocument] = [
        cast("spdx3.SpdxDocument", obj)
        for obj in object_set.foreach_type("SpdxDocument")
    ]

    if not spdx_documents:
        error_msg = (
            "No SpdxDocument object found in the SPDX 3 JSON file. "
            "Expected exactly one."
        )
        validation_messages.append(ValidationMessage(error_msg, ValidationContext()))
        return (doc, validation_messages)

    if len(spdx_documents) != 1:
        error_msg = "Multiple SpdxDocument objects found. Allows exactly one."
        validation_messages.append(ValidationMessage(error_msg, ValidationContext()))
        return (doc, validation_messages)

    doc = spdx_documents[0]
    doc_id = getattr(doc, "spdxId", None)
    root_element = getattr(doc, "rootElement", None)

    if not root_element:
        error_msg = "No rootElement found in the SpdxDocument. Expected exactly one."
        context = ValidationContext(parent_id=doc_id)
        validation_messages.append(ValidationMessage(error_msg, context))
    elif len(root_element) != 1:
        error_msg = "Multiple root elements found in SpdxDocument. Allows exactly one."
        context = ValidationContext(parent_id=doc_id)
        validation_messages.append(ValidationMessage(error_msg, context))
    else:
        root_element = root_element[0]
        if not isinstance(root_element, (spdx3.Bom, spdx3.software_Sbom)):
            error_msg = (
                "The root element must be of type Bom or software_Sbom. "
                f"Found: r{type(root_element)}"
            )
            root_element_id = getattr(root_element, "spdxId", None)
            context = ValidationContext(parent_id=doc_id, spdx_id=root_element_id)
            validation_messages.append(ValidationMessage(error_msg, context))

    return (doc, validation_messages)


def get_boms_from_spdx_document(
    spdx_doc: Optional[spdx3.SpdxDocument],
) -> Optional[List[spdx3.Bom]]:
    """
    Retrieve the BOMs that are rootElements of an SPDX 3 SpdxDocument.

    Args:
        spdx_doc (spdx3.SpdxDocument): The SPDX 3 SpdxDocument.

    Returns:
        Optional[List[spdx3.Bom]]: The Boms if found, otherwise None.
    """
    if not spdx_doc:
        return None

    root_elements: List[spdx3.Bom] = getattr(spdx_doc, "rootElement", [])
    if not root_elements:
        return None

    return root_elements


def get_packages_from_bom(
    bom: Optional[spdx3.Bom],
) -> Optional[List[spdx3.software_Package]]:
    """
    Retrieve the /Software/Packages that are rootElements of an SPDX 3 BOM.

    Args:
        spdx_doc (spdx3.Bom): The SPDX 3 Bom.

    Returns:
        Optional[List[spdx3.software_Package]]: The packages if found, otherwise None.
    """
    if not bom:
        return None

    root_elements: List[spdx3.software_Package] = getattr(bom, "rootElement", [])
    if not root_elements or len(root_elements) != 1:
        return None

    return root_elements


def iter_objects_with_property(
    object_set: spdx3.SHACLObjectSet,
    typ: Type[spdx3.SHACLObject] = spdx3.Artifact,
    property_name: str = "spdxId",
) -> Iterator[Tuple[str, str, Any]]:
    """
    Yield (name, spdxId, property) for each SPDX 3 object.

    Args:
        object_set (spdx3.SHACLObjectSet): The SHACLObjectSet to iterate over.
        typ (Type[spdx3.SHACLObject]): The type of SPDX3 object
        property_name (str): The property name to retrieve.

    Yields:
        Iterator[Tuple[str, str, Any]]: A tuple containing the name,
        SPDX ID, and the specified property of the object.
    """

    for obj in object_set.foreach_type(typ.__name__):
        name = (getattr(obj, "name", "") or "").strip()
        spdx_id = (getattr(obj, "spdxId", "") or "").strip()
        property_ = getattr(obj, property_name, None)
        yield name, spdx_id, property_


def iter_relationships_by_type(
    object_set: spdx3.SHACLObjectSet,
    rel_type: str,
) -> Iterator[Tuple[str, str]]:
    """
    Yield (from_id, to_id) for each relationship of the specified relationship type.
    """

    for obj in object_set.foreach_type("Relationship"):
        _rel_type = getattr(obj, "relationshipType", "")
        # Remove the IRI prefix of entry name before compare
        if not _rel_type or _rel_type.split("/")[-1] != rel_type:
            continue
        from_: Optional[spdx3.Element] = getattr(obj, "from_", None)
        to: Optional[spdx3.Element] = getattr(obj, "to", None)
        if not from_ or not to:
            continue

        from_id = getattr(from_, "spdxId", "")
        to_id = getattr(to, "spdxId", "")

        yield from_id, to_id


def get_all_packages(object_set: spdx3.SHACLObjectSet) -> Set[spdx3.software_Package]:
    """Retrieve all /Software/Package objects from an SHACLObjectSet."""
    packages: Set[spdx3.software_Package] = {
        cast("spdx3.software_Package", obj)
        for obj in object_set.foreach_type("software_Package")
    }
    return packages
