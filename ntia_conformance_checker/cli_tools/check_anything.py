"""Main minimum elements checking functionality."""

# pylint: disable=import-error

import os

import spdx.creationinfo
from spdx.parsers import parse_anything
from spdx.parsers.loggers import ErrorMessages


def check_minimum_elements(file, messages=None):
    """Assess if a SPDX document contains minumum elements.

    The function gathers all the individual minimum elements checks.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        messages (list) - set of messages related to minumum elements check
    """
    if isinstance(messages, list):
        raise TypeError("messages should be None or an instance of ErrorMessages")
    if messages is None:
        messages = ErrorMessages()

    # check if file even exists
    if not os.path.exists(file):
        messages.append(f"Filename {file} not found.")
        return messages

    try:
        doc, error = parse_anything.parse_file(file)
    except:  # pylint: disable=bare-except
        messages.append("Document cannot be parsed.")
        return messages

    messages.push_context(doc.name)
    if error:
        messages.append("Errors while parsing: True")
    check_document_version(doc, messages)
    check_components_names(doc, messages)
    check_components_versions(doc, messages)
    check_sbom_author(doc, messages)
    check_sbom_timestamp(doc, messages)
    check_sbom_dependency_relationships(doc, messages)
    check_components_suppliers(doc, messages)
    check_components_identifiers(doc, messages)
    messages.pop_context()
    return messages


def check_document_version(doc, messages):
    """Check the SPDX document version.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        messages (list) - set of messages related to minumum elements check
    """
    if str(doc.version) != "SPDX-2.2" and str(doc.version) != "SPDX-2.3":
        messages.append("Document  version " + str(doc.version) + " not supported.")
    return messages


def check_components_names(doc, messages):
    """Check that components have names.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        messages (list) - set of messages related to minumum elements check
    """
    for package in doc.packages:
        messages = check_name(package, messages)
    return messages


def check_components_versions(doc, messages):
    """Check that components have versions.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        messages (list) - set of messages related to minumum elements check
    """
    for package in doc.packages:
        if has_version(package) is False:
            messages.append(str(package.name) + " has no version.")


def check_sbom_author(doc, messages):
    """Check that SBOM has an author.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        messages (list) - set of messages related to minumum elements check
    """
    for i, _ in enumerate(doc.creation_info.creators):
        if isinstance(
            doc.creation_info.creators[i],
            (spdx.creationinfo.Person, spdx.creationinfo.Organization),
        ):
            return
    messages.append("Document has no author.")


def check_sbom_timestamp(doc, messages):
    """Check that SBOM has a timestamp.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        messages (list) - set of messages related to minumum elements check
    """
    if doc.creation_info.created is None:
        messages.append("Document has no timestamp.")


def check_sbom_dependency_relationships(doc, messages):
    """Check if SBOM has any dependency relationships.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        messages (list) - set of messages related to minumum elements check
    """
    if len(doc.relationships) == 0:
        messages.append("Document has no dependency relationships.")


def check_components_suppliers(doc, messages):
    """Check for components that have no suppliers.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        messages (list) - set of messages related to minumum elements check
    """
    for package in doc.packages:
        if has_supplier(package) is False:
            messages.append(str(package.name) + " has no supplier.")


def check_components_identifiers(doc, messages):
    """Check that components have identifiers.

    Args:
        file (str) - full filepath
        messages (list) - set of messages related to minumum elements check

    Returns:
        messages (list) - set of messages related to minumum elements check
    """
    for package in doc.packages:
        if has_identifier(package) is False:
            messages.append(str(package.name) + " has no identifier.")


def has_supplier(package):
    """Check that a particular package has a supplier.

    Args:
        package - package name

    Returns:
        bool
    """
    if package.supplier is None:
        return False
    return True


def has_identifier(package):
    """Check that a particular package has an identifier.

    Args:
        package - package name

    Returns:
        bool
    """
    if package.supplier is None:
        return False
    return True


def has_version(package):
    """Check that a particular package has a version.

    Args:
        package - package name

    Returns:
        bool
    """
    if package.version is None:
        return False
    return True


def check_name(package, messages):
    """Check that a particular package has a name.

    Args:
        package - package name

    Returns:
        bool
    """
    if package.name is None:
        messages.append("Package has no name.")
    return messages
