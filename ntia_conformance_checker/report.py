# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Report generation functionality."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple

from spdx_tools.spdx.validation.validation_message import ValidationMessage

from .constants import SUPPORTED_COMPLIANCE_STANDARDS


@dataclass
class ReportContext:
    """Context for generating conformance reports."""

    sbom_spec: str = ""
    compliance_standard: str = ""
    compliant: bool = False
    title: str = ""
    table_elements: Optional[List[Tuple[str, bool]]] = None
    validation_messages: Optional[List[ValidationMessage]] = None
    parsing_error: Optional[List[str]] = None


def _safe_attr(obj: object, name: str) -> str:
    val = getattr(obj, name, None)
    return str(val) if val not in (None, "") else "N/A"


def print_validation_messages(
    validation_messages: List[ValidationMessage], verbose: bool = False
) -> None:
    """Helper to print validation messages and optional context details."""
    print(get_validation_messages_text(validation_messages, verbose))


def get_validation_messages_text(
    validation_messages: List[ValidationMessage], verbose: bool = False
) -> str:
    """Helper to generate validation messages and optional context details."""
    report: List[str] = []

    for msg in validation_messages:
        if not msg.validation_message:
            continue
        report.append(msg.validation_message)
        if verbose and getattr(msg, "context", None):
            ctx = msg.context
            report.append(f"- SPDX ID: {_safe_attr(ctx, 'spdx_id')}")
            report.append(f"- Parent ID: {_safe_attr(ctx, 'parent_id')}")
            report.append(f"- Element type: {_safe_attr(ctx, 'element_type')}")
        report.append("")

    return "\n".join(report)


def get_validation_messages_html(
    validation_messages: List[ValidationMessage], verbose: bool = False
) -> str:
    """Helper to generate HTML for validation messages and context details."""
    if not validation_messages:
        return ""

    html = "<ul class='conformance-validation-list'>\n"
    for msg in validation_messages:
        if not getattr(msg, "validation_message", None):
            continue
        html += "<li>\n"
        html += "<p class='conformance-validation-msg-label'>Validation message:</p>\n"
        html += f"<p class='conformance-validation-msg'>{msg.validation_message}</p>\n"
        if verbose and getattr(msg, "context", None):
            ctx = msg.context
            if ctx:
                html += "<p class='conformance-validation-context-label'>Validation context:</p>\n"
                html += "<ul class='conformance-validation-context'>\n"
                html += f"<li>SPDX ID: {_safe_attr(ctx, 'spdx_id')}</li>\n"
                html += f"<li>Parent ID: {_safe_attr(ctx, 'parent_id')}</li>\n"
                html += f"<li>Element type: {_safe_attr(ctx, 'element_type')}</li>\n"
                html += "</ul>\n"
        html += "</li>\n"
    html += "</ul>"

    return html


def report_text(
    rc: ReportContext,
    verbose: bool = False,
) -> str:
    """
    Create element-by-element result table in plain-text.

    Args:
        verbose (bool): If True, print detailed information.
        table_elements (Optional[List[Tuple[str, bool]]]): A list of tuples
                        where each tuple contains a label and a boolean
                        value indicating the status of that element.

    Returns:
        None
    """
    report: List[str] = []

    # Parsing error
    if rc.parsing_error:
        report.append("The document couldn't be parsed; check couldn't be performed.\n")
        if rc.parsing_error:
            report.append("The following parsing error(s) were raised:\n")
            for error in rc.parsing_error:
                report.append(error)
        return "\n".join(report)

    # Unsupported compliance standard
    if rc.compliance_standard not in SUPPORTED_COMPLIANCE_STANDARDS:
        report.append(f"Unsupported compliance standard {rc.compliance_standard!r}")
        return "\n".join(report)

    report.append(rc.title)
    report.append(f"Conformant: {rc.compliant}\n")

    if rc.table_elements:
        report.append("Individual elements                            | Status")
        report.append("-------------------------------------------------------")
        for label, value in rc.table_elements:
            report.append(f"{label:<46} | {value}")
        report.append("")

    if rc.validation_messages:
        report.append(
            "\nThe document is not valid according to the SBOM "
            f'specification ("{rc.sbom_spec}"). '
            "The following violations were found:\n"
        )
        print_validation_messages(rc.validation_messages, verbose)

    return "\n".join(report)


def report_html(
    rc: ReportContext,
    verbose: bool = False,
) -> str:
    """
    Create element-by-element result table in HTML.

    Args:
        table_elements (Optional[List[Tuple[str, bool]]]): A list of tuples
                        where each tuple contains a label and a boolean
                        value indicating the status of that element.

    Returns:
        str: The HTML representation of the results.
    """
    report: List[str] = []

    # Parsing error
    if rc.parsing_error:
        report.append(
            "<p class='conformance-error'>"
            "The document couldn't be parsed; check couldn't be performed."
            "</p>"
        )
        if rc.parsing_error:
            report.append(
                "<p class='conformance-error-lead'>"
                "The following parsing errors were raised:"
                "</p>"
            )
            report.append("<ul class='conformance-error-details'>")
            for err in rc.parsing_error:
                report.append(f"<li>{err}</li>")
            report.append("</ul>")
        return "\n".join(report)

    # Unsupported compliance standard
    if rc.compliance_standard not in SUPPORTED_COMPLIANCE_STANDARDS:
        report.append(
            "<p class='conformance-error'>"
            f"Unsupported compliance standard {rc.compliance_standard!r}"
            "</p>"
        )
        return "\n".join(report)

    # Compliance result
    report.append(f"<h2 class='conformance-result-title'>{rc.title}</h2>")
    report.append(
        f"<h3 class='conformance-result-status'>Conformant: {rc.compliant}</h3>"
    )

    if rc.table_elements:
        report.append("<table class='conformance-result-table'>")
        report.append("<tr><th>Individual elements</th><th>Conformant</th></tr>")
        for label, val in rc.table_elements:
            report.append(f"<tr><td>{label}</td><td>{val}</td></tr>")
        report.append("</table>")

    # Validation messages
    if rc.validation_messages:
        report.append(
            "<p class='conformance-validation'>"
            "The document is not valid according to the SBOM specification"
            f' ("{rc.sbom_spec}").'
            "</p>"
        )
        report.append(
            "<p class='conformance-validation-lead'>"
            "The following violations were found:"
            "</p>"
        )
        report.append(
            get_validation_messages_html(rc.validation_messages, verbose=verbose)
        )

    return "\n".join(report)
