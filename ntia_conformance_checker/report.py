# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Report generation functionality."""
from typing import List

from spdx_tools.spdx.validation.validation_message import ValidationMessage


def _safe_attr(obj: object, name: str) -> str:
    val = getattr(obj, name, None)
    return str(val) if val not in (None, "") else "N/A"


def print_validation_messages(
    validation_messages: List[ValidationMessage], verbose: bool = False
) -> None:
    """Helper to print validation messages and optional context details."""

    for msg in validation_messages:
        if not msg.validation_message:
            continue
        print(msg.validation_message)
        if verbose and getattr(msg, "context", None):
            ctx = msg.context
            print("- SPDX ID:", _safe_attr(ctx, "spdx_id"))
            print("- Parent ID:", _safe_attr(ctx, "parent_id"))
            print("- Element type:", _safe_attr(ctx, "element_type"))
        print()


def get_validation_messages_html(validation_messages: List[ValidationMessage]) -> str:
    """Helper to generate HTML for validation messages and context details."""
    if not validation_messages:
        return ""

    html = "<ul>\n"
    for msg in validation_messages:
        if not getattr(msg, "validation_message", None):
            continue
        html += "<li>\n"
        html += "<p><strong>Validation message:</strong></p>\n"
        html += f"<p>{msg.validation_message}</p>\n"
        ctx = getattr(msg, "context", None)
        if ctx:
            html += "<p><strong>Validation context:</strong></p>\n<ul>\n"
            spdx_id = getattr(ctx, "spdx_id", "N/A")
            parent_id = getattr(ctx, "parent_id", "N/A")
            elem_type = getattr(ctx, "element_type", "N/A")
            html += f"<li>SPDX ID: {spdx_id}</li>\n"
            html += f"<li>Parent ID: {parent_id}</li>\n"
            html += f"<li>Element type: {elem_type}</li>\n"
            html += "</ul>\n"
        html += "</li>\n"
    html += "</ul>"

    return html
