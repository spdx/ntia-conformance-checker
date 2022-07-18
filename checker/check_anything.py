from spdx.parsers.loggers import ErrorMessages
import asyncio
import spdx.creationinfo
from spdx.parsers import parse_anything

def check_minimum_elements(file, messages=None):
    if isinstance(messages, list):
        raise TypeError("messages should be None or an instance of ErrorMessages")
    if messages is None:
        messages = ErrorMessages()
    try:
        doc, error = parse_anything.parse_file(file)
    except:
        messages.append("Document cannot be parsed.")
        return messages
    messages.push_context(doc.name)
    if error:
        messages.append("Parsing errors occurred.")
    check_components_names(doc, messages)
    check_components_versions(doc, messages)
    check_sbom_author(doc, messages)
    check_sbom_timestamp(doc, messages)
    check_sbom_dependency_relationships(doc, messages)
    check_components_suppliers(doc, messages)
    check_components_identifiers(doc, messages)
    messages.pop_context()
    return messages

def check_components_names(doc, messages):
    for package in doc.packages:
        messages = check_name(package, messages)

def check_components_versions(doc, messages):
    for package in doc.packages:
        if has_version(package) == False:
            messages.append(str(package.name) + " has no version.")

def check_sbom_author(doc, messages):
    for i in range(len(doc.creation_info.creators)):
        if type(doc.creation_info.creators[i]) == spdx.creationinfo.Person:
            return
    messages.append("Document has no author.")

def check_sbom_timestamp(doc, messages):
    if doc.creation_info.created is None:
        messages.append("Document has no timestamp.")

def check_sbom_dependency_relationships(doc, messages):
    if len(doc.relationships) == 0:
        messages.append("Document has no dependency relationships.")

def check_components_suppliers(doc, messages):
    for package in doc.packages:
        if has_supplier(package) == False:
            messages.append(str(package.name) + " has no supplier.")

def check_components_identifiers(doc, messages):
    for package in doc.packages:
        if has_supplier(package) == False:
            messages.append(str(package.name) + " has no identifier.")

def has_supplier(package):
    if package.supplier is None:
        return False
    return True

def has_identifier(package):
    if package.supplier is None:
        return False
    return True

def has_version(package):
    if package.version is None:
        return False
    return True

def check_name(package, messages):
    if package.name is None:
        messages.append("Package has no name.")

