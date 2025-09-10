# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Report generation functionality."""


def print_validation_messages(validation_messages, verbose: bool = False) -> None:
    """Helper to print validation messages and optional context details."""

    def _safe_attr(obj: object, name: str) -> str:
        val = getattr(obj, name, None)
        return str(val) if val not in (None, "") else "N/A"

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
