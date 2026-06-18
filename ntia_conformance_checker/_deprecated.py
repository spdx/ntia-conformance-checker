# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Deprecated v5 method aliases.

Mixed into :class:`BaseChecker` via :class:`DeprecatedCheckerMixin`.
These wrappers emit :class:`DeprecationWarning` and delegate to the
canonical v6 names.  They will be removed in a future release.
"""

from __future__ import annotations

import warnings


class DeprecatedCheckerMixin:
    """Backwards-compatibility aliases for v5 method names.

    Do **not** use these in new code.  They exist solely so code written
    against v5 continues to run (with warnings) against v6.
    """

    # ---- Deprecated doc-level bool checks --------------------------------

    def check_author(self) -> bool:
        """Deprecated v5 alias; use :meth:`get_doc_author` instead."""
        warnings.warn(
            "check_author() is deprecated in v6; use get_doc_author() "
            "(returns str) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return bool(self.get_doc_author())  # type: ignore[attr-defined]

    def check_timestamp(self) -> bool:
        """Deprecated v5 alias; use :meth:`get_doc_timestamp` instead."""
        warnings.warn(
            "check_timestamp() is deprecated in v6; use get_doc_timestamp() "
            "(returns str) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return bool(self.get_doc_timestamp())  # type: ignore[attr-defined]

    def check_doc_version(self) -> bool:
        """Deprecated v5 alias; use :meth:`get_doc_spec_version` instead."""
        warnings.warn(
            "check_doc_version() is deprecated in v6; use get_doc_spec_version() "
            "(returns str) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return bool(self.get_doc_spec_version())  # type: ignore[attr-defined]

    def check_dependency_relationships(self) -> bool:
        """Deprecated v5 alias; use :meth:`get_doc_dependency_relationship`."""
        warnings.warn(
            "check_dependency_relationships() is deprecated in v6; use "
            "get_doc_dependency_relationship() (returns list) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return bool(self.get_doc_dependency_relationship())  # type: ignore[attr-defined]

    # ---- Deprecated component extractor aliases --------------------------

    def get_components_without_concluded_licenses(self) -> list[tuple[str, str]]:
        """Deprecated v5 alias for :meth:`get_components_without_concluded_license`."""
        warnings.warn(
            "get_components_without_concluded_licenses() is deprecated in v6; "
            "use get_components_without_concluded_license() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        result = self.get_components_without_concluded_license()  # type: ignore[attr-defined]
        return result  # type: ignore[no-any-return]

    def get_components_without_copyright_texts(self) -> list[tuple[str, str]]:
        """Deprecated v5 alias for :meth:`get_components_without_copyright_notice`."""
        warnings.warn(
            "get_components_without_copyright_texts() is deprecated in v6; "
            "use get_components_without_copyright_notice() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        result = self.get_components_without_copyright_notice()  # type: ignore[attr-defined]
        return result  # type: ignore[no-any-return]

    def get_components_without_identifiers(self) -> list[tuple[str, str]]:
        """Deprecated v5 alias for :meth:`get_components_without_unique_identifier`."""
        warnings.warn(
            "get_components_without_identifiers() is deprecated in v6; "
            "use get_components_without_unique_identifier() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        result = self.get_components_without_unique_identifier()  # type: ignore[attr-defined]
        return result  # type: ignore[no-any-return]

    def get_components_without_names(self) -> list[tuple[str, str]]:
        """Deprecated v5 alias for :meth:`get_components_without_name`."""
        warnings.warn(
            "get_components_without_names() is deprecated in v6; "
            "use get_components_without_name() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.get_components_without_name()  # type: ignore[attr-defined,no-any-return]

    def get_components_without_suppliers(self) -> list[tuple[str, str]]:
        """Deprecated v5 alias for :meth:`get_components_without_supplier`."""
        warnings.warn(
            "get_components_without_suppliers() is deprecated in v6; "
            "use get_components_without_supplier() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.get_components_without_supplier()  # type: ignore[attr-defined,no-any-return]

    def get_components_without_versions(self) -> list[tuple[str, str]]:
        """Deprecated v5 alias for :meth:`get_components_without_version`."""
        warnings.warn(
            "get_components_without_versions() is deprecated in v6; "
            "use get_components_without_version() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.get_components_without_version()  # type: ignore[attr-defined,no-any-return]
