"""Parse and format message output."""

from spdx.parsers import parse_anything  # pylint: disable=import-error


def structure_messages(file, messages):
    """Parse messages into well-structured dict.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        result (dict) - structured data on minimum elements conformance
    """

    # instantiate dict and fields that have > 1 level
    result = {}
    result["componentVersions"] = {}
    result["componentIdentifiers"] = {}
    result["componentSuppliers"] = {}
    result["componentNames"] = {}

    result["authorNameProvided"] = is_document_level_element_present(
        messages, "Document has no author."
    )
    result["timestampProvided"] = is_document_level_element_present(
        messages, "Document has no timestamp."
    )
    result["dependencyRelationshipsProvided"] = is_document_level_element_present(
        messages, "Document has no dependency relationships."
    )

    field_match_pairs = [
        ("componentVersions", "has no version"),
        ("componentIdentifiers", "has no identifier"),
        ("componentSuppliers", "has no supplier"),
    ]
    for field, match in field_match_pairs:
        result[field][
            "nonconformantComponents"
        ] = find_nonconformant_component_level_elements(messages, match)
        result[field]["allProvided"] = not result[field]["nonconformantComponents"]

    result["componentNames"]["numNonconformantComponents"] = len(
        find_nonconformant_component_level_elements(messages, "has no version")
    )
    result["componentNames"]["allProvided"] = not result["componentNames"][
        "numNonconformantComponents"
    ]

    result["isNtiaConformant"] = all(
        [
            result["authorNameProvided"],
            result["timestampProvided"],
            result["dependencyRelationshipsProvided"],
            result["componentVersions"]["allProvided"],
            result["componentIdentifiers"]["allProvided"],
            result["componentSuppliers"]["allProvided"],
            result["componentNames"]["allProvided"],
        ]
    )

    doc, _ = parse_anything.parse_file(file)
    result["sbomName"] = doc.name

    return result


def is_document_level_element_present(messages, match):
    """Check for a particular document-level minimum element.

    Checks for existence of an error message (match) and, if error
    exists, then reports that that document-level element is not
    present. A document-level minimum element is one where the
    property is associated with the whole SBOM document, such as
    whether there is an author name or timestamp provided.

    Args:
        messages (list) - set of messages related to minumum elements check
        match (str) - matching string for a particular minimum element

    Returns:
        bool (True if present, false otherwise)
    """
    return not any(match in msg for msg in messages)


def find_nonconformant_component_level_elements(messages, match):
    """List components with nonconformant minimum elements.

    Checks for existence of error messages (match) and, if error
    exists, then collects a list of the names of all components.

    Args:
        messages (list) - set of messages related to minumum elements check
        match (str) - matching string for a particular minimum element

    Returns:
        list - names of non-conformant elements
    """
    nonconformant_components = []
    for msg in messages:
        if match in msg:
            # package-level messages all use the same construct:
            # e.g. "pkgxyz has no identifier.", so grab the first word
            pkg_name = msg.split(" ")[0]
            nonconformant_components.append(pkg_name)
    return nonconformant_components
