# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""
Report generation functionality.

Some of the code here was originally in the BaseChecker class.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional, Tuple

from .constants import (
    SUPPORTED_COMPLIANCE_STANDARDS,
    SUPPORTED_COMPLIANCE_STANDARDS_DESC,
)

if TYPE_CHECKING:
    from spdx_tools.spdx.validation.validation_message import ValidationMessage


@dataclass
class ReportContext:
    """Context for generating conformance reports."""

    sbom_spec: str = ""
    compliance_standard: str = ""
    compliant: bool = False
    requirement_results: Optional[List[Tuple[str, bool]]] = None
    components_without_info: Optional[List[Tuple[str, List[str]]]] = None
    validation_messages: Optional[List[ValidationMessage]] = None
    parsing_error: Optional[List[str]] = None


def _safe_attr(obj: object, name: str) -> str:
    val = getattr(obj, name, None)
    return str(val) if val not in (None, "") else "N/A"


def print_validation_messages(
    validation_messages: List[ValidationMessage], verbose: bool = False
) -> None:
    """Prints validation messages and optional context details.

    Args:
        validation_messages (List[ValidationMessage]): List of validation messages.
        verbose (bool): If True, include detailed validation context.

    Returns:
        None
    """
    print(get_validation_messages_text(validation_messages, verbose))


def get_validation_messages_text(
    validation_messages: List[ValidationMessage], verbose: bool = False
) -> str:
    """Generates validation messages and optional context details.

    Args:
        validation_messages (List[ValidationMessage]): List of validation messages.
        verbose (bool): If True, include detailed validation context.

    Returns:
        str: Plain-text representation of the validation messages.
    """
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
    """Generates HTML for validation messages and context details.

    Args:
        validation_messages (List[ValidationMessage]): List of validation messages.
        verbose (bool): If True, include detailed validation context.

    Returns:
        str: HTML representation of the validation messages.
    """
    if not validation_messages:
        return ""

    html = "<ul class='conformance-val-list'>\n"
    for msg in validation_messages:
        if not getattr(msg, "validation_message", None):
            continue
        html += "<li>\n"
        html += "<p class='conformance-val-msg-label'>Validation message:</p>\n"
        html += f"<p class='conformance-val-msg'>{msg.validation_message}</p>\n"
        if verbose and getattr(msg, "context", None):
            ctx = msg.context
            if ctx:
                html += "<p class='conformance-val-ctx-label'>Validation context:</p>\n"
                html += "<ul class='conformance-val-ctx'>\n"
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
    """Generates element-by-element result table in plain-text.

    Args:
        rc (ReportContext): Information for generating the report.
        verbose (bool): If True, include detailed validation messages.

    Returns:
        str: Plain-text representation of the results.
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

    # Compliance results
    report.append(
        f"{SUPPORTED_COMPLIANCE_STANDARDS_DESC[rc.compliance_standard]}"
        " Conformance Results\n"
    )
    report.append(f"Conformant: {rc.compliant}\n")
    if rc.requirement_results:
        report.append("Requirement                                    | Status")
        report.append("-------------------------------------------------------")
        for label, value in rc.requirement_results:
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
    """Generates element-by-element result table in HTML.

    Args:
        rc (ReportContext): Information for generating the report.
        verbose (bool): If True, include detailed validation messages.

    Returns:
        str: HTML representation of the results.
    """
    report: List[str] = []

    # Parsing error
    if rc.parsing_error:
        report.append("<div class='conformance-err'>")
        report.append(
            "<p class='conformance-err-label'>"
            "The document couldn't be parsed; check couldn't be performed.<br />"
            "The following parsing errors were raised:"
            "</p>"
        )
        report.append("<ul class='conformance-err-list'>")
        for err in rc.parsing_error:
            report.append(f"<li>{err}</li>")
        report.append("</ul>")
        report.append("</div>")
        return "\n".join(report)

    # Unsupported compliance standard
    if rc.compliance_standard not in SUPPORTED_COMPLIANCE_STANDARDS:
        report.append(
            "<div class='conformance-err'>"
            "<p class='conformance-err-label'>"
            f"Unsupported compliance standard {rc.compliance_standard!r}"
            "</p>"
            "</div>"
        )
        return "\n".join(report)

    # Compliance results
    report.append("<div class='conformance-res'>")
    report.append(
        "<h2 class='conformance-res-title'>"
        f"{SUPPORTED_COMPLIANCE_STANDARDS_DESC[rc.compliance_standard]}"
        " Conformance Results</h2>"
    )
    report.append(f"<h3 class='conformance-res-status'>Conformant: {rc.compliant}</h3>")

    if rc.requirement_results:
        report.append("<table class='conformance-res-tab'>")
        report.append("<thead><tr><th>Requirement</th><th>Conformant</th></tr></thead>")
        report.append("<tbody>")
        for component_name, val in rc.requirement_results:
            report.append(
                "<tr>"
                "<td class='conformance-res-tab-r'>"
                f"{component_name}</td>"
                "<td class='conformance-res-tab-v'>"
                f"{val}</td>"
                "</tr>"
            )
        report.append("</tbody>")
        report.append("</table>")

    report.append("</div>")  # End of conformance-res

    # Components without required information
    if rc.components_without_info:
        report.append("<div class='conformance-mis'>")
        report.append(
            "<p class='conformance-mis-label'>"
            "Missing required information in these components:"
            "</p>"
        )
        report.append("<ul class='conformance-mis-list'>")
        for component_name, components in rc.components_without_info:
            report.append(
                f"<li>{component_name} ({len(components)}): "
                f"{', '.join(components)}</li>"
            )
        report.append("</ul>")
        report.append("</div>")

    # Validation messages
    if rc.validation_messages:
        report.append("<div class='conformance-val'>")
        report.append(
            "<p class='conformance-val-label'>"
            "The document is not valid according to the SBOM specification"
            f' ("{rc.sbom_spec}").<br />'
            "The following violations were found:"
            "</p>"
        )
        report.append(
            get_validation_messages_html(rc.validation_messages, verbose=verbose)
        )
        report.append("</div>")

    return "\n".join(report)
