# SPDX-FileCopyrightText: 2026 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""BSI Minimum Elements checking functionality."""

from __future__ import annotations

from typing import Any

from spdx_python_model.bindings import v3_0_1 as spdx3

from .base_checker import BaseChecker
from .spdx3_utils import (
    get_dependency_relationships_completeness,
    get_distribution_artifacts_map,
    has_sha512_hash,
    iter_objects_with_property,
    iter_relationships_by_type,
)


# pylint: disable=too-many-instance-attributes
class BSIChecker(BaseChecker):
    """
    BSI Minimum Elements check according to BSI TR-03183-2 v2.1.0.

    See:
        https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TR03183/BSI-TR-03183-2_v2_1_0.html
    """

    MIN_ELEMENTS = [
        "creator",
        "name",
        "version",
        "filename",
        "distribution_licenses",
        "sha512_hash",
        "executable_property",
        "archive_property",
        "structured_property",
    ]

    _COMPONENTS_WITHOUT_INFO = {
        **BaseChecker._COMPONENTS_WITHOUT_INFO,
        "creator": (
            "components_without_creators",
            "Components missing a creator (Email/URL)",
        ),
        "filename": (
            "components_without_filenames",
            "Components missing a distribution filename",
        ),
        "executable_property": (
            "components_without_executable_prop",
            "Components missing executable property",
        ),
        "archive_property": (
            "components_without_archive_prop",
            "Components missing archive property",
        ),
        "structured_property": (
            "components_without_structured_prop",
            "Components missing structured property",
        ),
        "distribution_licenses": (
            "components_without_concluded_licenses",
            "Components missing distribution licenses",
        ),
        "sha512_hash": (
            "components_without_sha512_hashes",
            "Components missing SHA-512 hash",
        ),
    }

    def __init__(
        self,
        file: str,
        validate: bool = True,
        compliance: str = "bsi",
        sbom_spec: str = "spdx3",
    ):
        """
        Initialize the BSI Minimum Element Checker.

        Args:
            file (str): The name of the file to be checked.
            validate (bool): Whether to validate the file.
            compliance (str): The compliance standard to be used.
            sbom_spec (str): The SBOM specification to be used.
        """

        if compliance not in {"bsi"}:
            raise ValueError("Only BSI compliance is supported.")

        self.components_without_creators: list[tuple[str, str]] = []
        self.components_without_filenames: list[tuple[str, str]] = []
        self.components_without_executable_prop: list[tuple[str, str]] = []
        self.components_without_archive_prop: list[tuple[str, str]] = []
        self.components_without_structured_prop: list[tuple[str, str]] = []
        self.components_without_sha512_hashes: list[tuple[str, str]] = []

        # Initialize Additional/Optional lists (Warnings)
        self.components_without_source_code_uris: list[tuple[str, str]] = []
        self.components_without_deployable_uris: list[tuple[str, str]] = []
        self.components_without_unique_identifiers: list[tuple[str, str]] = []
        self.components_without_original_licenses: list[tuple[str, str]] = []
        self.components_without_effective_licenses: list[tuple[str, str]] = []
        self.components_without_source_code_hashes: list[tuple[str, str]] = []
        self.components_without_security_txt: list[tuple[str, str]] = []
        self.components_without_bom_references: list[tuple[str, str]] = []

        self.doc_creator: bool = False
        self.doc_uri: bool = False
        self.dependency_completeness: bool = False

        super().__init__(
            file=file, validate=validate, compliance=compliance, sbom_spec=sbom_spec
        )

        if self.doc:
            self.compliant = self.check_compliance()

        self.table_elements = [
            ("Creator of the SBOM", self.doc_creator),
            ("Timestamp", self.doc_timestamp),
            ("Dependency Completeness", self.dependency_completeness),
            ("Component Names", not bool(self.components_without_names)),
            ("Component Versions", not bool(self.components_without_versions)),
            ("Component Creators", not bool(self.components_without_creators)),
            ("Distribution Filenames", not bool(self.components_without_filenames)),
            (
                "Executable Properties",
                not bool(self.components_without_executable_prop),
            ),
            ("Archive Properties", not bool(self.components_without_archive_prop)),
            (
                "Structured Properties",
                not bool(self.components_without_structured_prop),
            ),
            (
                "Distribution Licenses",
                not bool(self.components_without_concluded_licenses),
            ),
            (
                "Deployable Component Hashes",
                not bool(self.components_without_sha512_hashes),
            ),
            (
                "Source Code URIs (Warning)",
                not bool(self.components_without_source_code_uris),
            ),
            (
                "Deployable Form URIs (Warning)",
                not bool(self.components_without_deployable_uris),
            ),
            (
                "Other Unique Identifiers (Warning)",
                not bool(self.components_without_unique_identifiers),
            ),
            (
                "Original Licenses (Warning)",
                not bool(self.components_without_original_licenses),
            ),
            (
                "Effective Licenses (Optional)",
                not bool(self.components_without_effective_licenses),
            ),
            (
                "Source Code Hashes (Optional)",
                not bool(self.components_without_source_code_hashes),
            ),
            (
                "Security.txt URLs (Optional)",
                not bool(self.components_without_security_txt),
            ),
            (
                "BOM References (Optional)",
                not bool(self.components_without_bom_references),
            ),
        ]

    def check_compliance(self) -> bool:
        """Check overall compliance with BSI minimum elements."""
        # Execute Document-Level Checks
        self.doc_creator = self.check_doc_creator()
        self.doc_uri = self.check_sbom_uri()
        self.doc_timestamp = self.check_timestamp()

        # Execute Component-Level Checks
        self.dependency_completeness = self.check_dependency_completeness()
        self.components_without_names = self.get_components_without_names()
        self.components_without_versions = self.get_components_without_versions()

        # Run BSI-specific overrides and new methods
        self.components_without_concluded_licenses = (
            self.get_components_without_concluded_licenses()
        )
        self.components_without_creators = self.get_components_without_creators()
        self.components_without_filenames = self.get_components_without_filenames()
        self.components_without_executable_prop = (
            self.get_components_without_executable_prop()
        )
        self.components_without_archive_prop = (
            self.get_components_without_archive_prop()
        )
        self.components_without_structured_prop = (
            self.get_components_without_structured_prop()
        )
        self.components_without_sha512_hashes = (
            self.get_components_without_sha512_hashes()
        )

        # Run Additional/Optional checks
        self.components_without_source_code_uris = (
            self.get_components_without_source_code_uris()
        )
        self.components_without_deployable_uris = (
            self.get_components_without_deployable_uris()
        )
        self.components_without_unique_identifiers = (
            self.get_components_without_unique_identifiers()
        )
        self.components_without_original_licenses = (
            self.get_components_without_original_licenses()
        )
        self.components_without_effective_licenses = (
            self.get_components_without_effective_licenses()
        )
        self.components_without_source_code_hashes = (
            self.get_components_without_source_code_hashes()
        )
        self.components_without_security_txt = (
            self.get_components_without_security_txt()
        )
        self.components_without_bom_references = (
            self.get_components_without_bom_references()
        )

        # Refresh the aggregated tracking list used by the base class reporter
        self.all_components_without_info = self._get_all_components_without_info()

        return all(
            [
                self.doc_creator,
                self.doc_timestamp,
                self.doc_uri,
                self.dependency_completeness,
                not bool(self.all_components_without_info),
            ]
        )

    @staticmethod
    def _is_valid_creator(
        creator: Any, doc: spdx3.SHACLObjectSet, url_id_types: tuple[str, ...]
    ) -> bool:
        """Validate if a creator object has a valid email or URL identifier."""
        creator_obj = (
            creator if not isinstance(creator, str) else doc.find_by_id(creator)
        )
        if not isinstance(creator_obj, (spdx3.Person, spdx3.Organization)):
            return False

        for ext_id in getattr(creator_obj, "externalIdentifier", []):
            id_type = str(getattr(ext_id, "externalIdentifierType", "")).lower()
            id_val = getattr(ext_id, "identifier", "")
            if not id_val:
                continue

            if "email" in id_type and "@" in id_val:
                return True
            if any(t in id_type for t in url_id_types) and id_val.startswith(
                ("http://", "https://")
            ):
                return True

        return False

    def check_doc_creator(self) -> bool:
        """
        Check if the document creator has a valid email or URL.
        """
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return False

        spdx3_doc = getattr(self, "_BaseChecker__spdx3_doc", None)
        if not spdx3_doc:
            return False

        creation_info = getattr(spdx3_doc, "creationInfo", None)
        if not creation_info:
            return False

        creators = getattr(creation_info, "createdBy", [])
        if not creators:
            return False

        return any(
            self._is_valid_creator(c, self.doc, ("urlscheme", "other"))
            for c in creators
        )

    def check_sbom_uri(self) -> bool:
        """
        Check if the SBOM-URI exists.
        """
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return False

        spdx3_doc = getattr(self, "_BaseChecker__spdx3_doc", None)
        if not spdx3_doc:
            return False

        root_elements = getattr(spdx3_doc, "rootElement", [])

        for root in root_elements:
            root_obj = root if not isinstance(root, str) else self.doc.find_by_id(root)

            # The rootElement (software_Sbom or software_Package) MUST have a valid spdxId.
            if isinstance(root_obj, (spdx3.software_Sbom, spdx3.software_Package)):
                spdx_id = getattr(root_obj, "spdxId", None)
                if spdx_id and isinstance(spdx_id, str) and spdx_id.strip():
                    return True

        return False

    def get_components_without_creators(self) -> list[tuple[str, str]]:
        """
        Check if each component creator has a valid email or URL.
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        # Iterate through all packages in the reachable graph
        for name, spdx_id, originated_by_list in iter_objects_with_property(
            self.doc,
            spdx3.software_Package,
            "originatedBy",
            self.reachable_component_ids,
        ):
            creators = originated_by_list or []
            has_valid = any(
                self._is_valid_creator(c, self.doc, ("other", "urlscheme"))
                for c in creators
            )
            if not has_valid:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_filenames(self) -> list[tuple[str, str]]:
        """
        Check if each package has a linked software_File with a valid name.
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        artifacts_map = get_distribution_artifacts_map(self.doc)

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            has_filename = False
            linked_files = artifacts_map.get(spdx_id, [])

            for file_obj in linked_files:
                file_name = getattr(file_obj, "name", "")
                if file_name and isinstance(file_name, str) and file_name.strip():
                    has_filename = True
                    break

            if not has_filename:
                missing.append((name, spdx_id))

        return missing

    def check_dependency_completeness(self) -> bool:
        """
        Check if dependency enumerations clearly indicate their completeness.
        """
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return False

        completeness_map = get_dependency_relationships_completeness(self.doc)

        for _, completeness_list in completeness_map.items():
            for completeness_val in completeness_list:
                if completeness_val not in ("complete", "incomplete", "noAssertion"):
                    return False

        return True

    def get_components_without_concluded_licenses(self) -> list[tuple[str, str]]:
        """
        Overrides BaseChecker to enforce BSI document Table 9 and Section 6.1 rules:
        1. Target MUST be simplelicensing_LicenseExpression.
        2. Must use valid SPDX license expressions, Scancode, or custom LicenseRefs.
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        valid_license_ids = set()
        for from_id, to_ids in iter_relationships_by_type(
            self.doc, "hasConcludedLicense"
        ):
            has_valid_expression = False
            for target_id in to_ids:
                obj = self.doc.find_by_id(target_id)
                if obj and isinstance(obj, spdx3.simplelicensing_LicenseExpression):
                    expr = getattr(obj, "simplelicensing_licenseExpression", "")
                    if (
                        expr
                        and isinstance(expr, str)
                        and expr.strip() != "NoAssertionLicense"
                    ):
                        has_valid_expression = True
                        break

            if has_valid_expression:
                valid_license_ids.add(from_id)

        # Check packages against the valid license list
        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            if spdx_id not in valid_license_ids:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_sha512_hashes(self) -> list[tuple[str, str]]:
        """
        Check if the deployable component has a SHA-512 hash.
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        artifacts_map = get_distribution_artifacts_map(self.doc)

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            linked_files = artifacts_map.get(spdx_id, [])

            # If no file is linked, skip file level checks.
            if not linked_files:
                continue

            has_hash = False
            for file_obj in linked_files:
                if has_sha512_hash(file_obj):
                    has_hash = True
                    break

            if not has_hash:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_executable_prop(self) -> list[tuple[str, str]]:
        """
        BSI Requirement: Omit 'executable' if non-executable.
        Since omission represents 'False', a static checker cannot fail a component
        for missing this tag. Always compliant.
        """
        return []

    def get_components_without_archive_prop(self) -> list[tuple[str, str]]:
        """
        BSI Requirement: Omit 'archive' if non-archive.
        Since omission represents 'False', a static checker cannot fail a component
        for missing this tag. Always compliant.
        """
        return []

    def get_components_without_structured_prop(self) -> list[tuple[str, str]]:
        """
        Check if the component declares a structured property.
        BSI Requirement: MUST indicate 'container' (structured) or 'firmware' (unstructured).
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        artifacts_map = get_distribution_artifacts_map(self.doc)

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            linked_files = artifacts_map.get(spdx_id, [])

            # If no file is linked, skip file level checks.
            if not linked_files:
                continue

            has_structured_prop = False
            for file_obj in linked_files:
                purposes = getattr(file_obj, "software_additionalPurpose", [])
                # Convert IRIs/Enums to strings and check for BSI keywords
                purposes_str = [str(p).lower() for p in purposes]

                if any("container" in p or "firmware" in p for p in purposes_str):
                    has_structured_prop = True
                    break

            if not has_structured_prop:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_source_code_uris(self) -> list[tuple[str, str]]:
        """
        Check if the component has a Source code URI.
        BSI Requirement: MUST be included IF it exists (Additional Data Field).
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        valid_package_ids = set()

        for from_id, to_ids in iter_relationships_by_type(self.doc, "generates"):
            is_valid_source = False

            obj = self.doc.find_by_id(from_id)
            if obj and isinstance(
                obj,
                (
                    spdx3.software_SoftwareArtifact,
                    spdx3.software_File,
                    spdx3.software_Package,
                ),
            ):
                raw_purpose = getattr(obj, "software_primaryPurpose", None) or getattr(
                    obj, "primaryPurpose", None
                )
                purposes = (
                    raw_purpose if isinstance(raw_purpose, list) else [raw_purpose]
                )
                purposes_str = [str(p).lower() for p in purposes]

                if any("source" in p for p in purposes_str):
                    if getattr(obj, "externalRef", []):
                        is_valid_source = True

            if is_valid_source:
                for target_id in to_ids:
                    valid_package_ids.add(target_id)

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            if spdx_id not in valid_package_ids:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_deployable_uris(self) -> list[tuple[str, str]]:
        """
        Check if the component has a URI of the deployable form.
        BSI Requirement: MUST be included IF it exists (Additional Data Field).
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        artifacts_map = get_distribution_artifacts_map(self.doc)

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            linked_files = artifacts_map.get(spdx_id, [])
            if not linked_files:
                continue

            has_deployable_uri = False
            for file_obj in linked_files:
                for ext_ref in getattr(file_obj, "externalRef", []):
                    ref_type = str(getattr(ext_ref, "externalRefType", "")).lower()
                    if "binaryartifact" in ref_type:
                        has_deployable_uri = True
                        break
                if has_deployable_uri:
                    break

            if not has_deployable_uri:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_unique_identifiers(self) -> list[tuple[str, str]]:
        """
        Check if the component has additional unique identifiers (CPE, SWID, PURL).
        BSI Requirement: MUST be included IF they exist (Additional Data Field).
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        # Valid BSI external identifier types
        valid_types = {"cpe22", "cpe23", "swid", "packageurl"}

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            has_valid_id = False

            obj = self.doc.find_by_id(spdx_id)
            if obj:
                ext_ids = getattr(obj, "externalIdentifier", [])
                for ext_id in ext_ids:
                    id_type = str(getattr(ext_id, "externalIdentifierType", "")).lower()
                    # Extract the base type name from the IRI/Enum
                    id_type_clean = id_type.rsplit("/", maxsplit=1)[-1]

                    if id_type_clean in valid_types:
                        has_valid_id = True
                        break

            if not has_valid_id:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_original_licenses(self) -> list[tuple[str, str]]:
        """
        Check if original licences are included.
        BSI Requirement: MUST be included IF they exist (Additional Data Field).
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        valid_license_ids = set()

        for from_id, to_ids in iter_relationships_by_type(
            self.doc, "hasDeclaredLicense"
        ):
            has_valid_expression = False
            for target_id in to_ids:
                obj = self.doc.find_by_id(target_id)
                if obj and isinstance(obj, spdx3.simplelicensing_LicenseExpression):
                    expr = getattr(obj, "simplelicensing_licenseExpression", "")
                    if (
                        expr
                        and isinstance(expr, str)
                        and expr.strip() != "NoAssertionLicense"
                    ):
                        has_valid_expression = True
                        break

            if has_valid_expression:
                valid_license_ids.add(from_id)

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            if spdx_id not in valid_license_ids:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_effective_licenses(self) -> list[tuple[str, str]]:
        """
        Check if the effective licence is included.
        BSI Requirement: MAY be included (Optional Data Field).
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        valid_license_ids = set()

        for rel in self.doc.foreach_type(spdx3.Relationship):
            rel_type = getattr(rel, "relationshipType", "")

            if (
                rel_type
                and str(rel_type).rsplit("/", maxsplit=1)[-1].lower() == "other"
            ):
                comment = getattr(rel, "comment", "")

                if comment and "hasEffectiveLicense" in str(comment):
                    from_obj = getattr(rel, "from_", None)
                    from_id = (
                        from_obj
                        if isinstance(from_obj, str)
                        else getattr(from_obj, "spdxId", "")
                    )

                    if from_id:
                        valid_license_ids.add(from_id)

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            if spdx_id not in valid_license_ids:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_source_code_hashes(self) -> list[tuple[str, str]]:
        """
        Check if the source code of the component has a SHA-512 hash.
        BSI Requirement: MAY be included (Optional Data Field).
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        valid_package_ids = set()

        for from_id, to_ids in iter_relationships_by_type(self.doc, "generates"):
            has_hash = False
            obj = self.doc.find_by_id(from_id)
            if obj and isinstance(
                obj,
                (
                    spdx3.software_SoftwareArtifact,
                    spdx3.software_File,
                    spdx3.software_Package,
                ),
            ):
                raw_purpose = getattr(obj, "software_primaryPurpose", None) or getattr(
                    obj, "primaryPurpose", None
                )
                purposes = (
                    raw_purpose if isinstance(raw_purpose, list) else [raw_purpose]
                )
                purposes_str = [str(p).lower() for p in purposes]

                if any("source" in p for p in purposes_str):
                    if has_sha512_hash(obj):
                        has_hash = True

            if has_hash:
                valid_package_ids.update(to_ids)

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            if spdx_id not in valid_package_ids:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_security_txt(self) -> list[tuple[str, str]]:
        """
        Check if the component contains a URL to security.txt.
        BSI Requirement: MAY be included (Optional Data Field).
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            has_security = False
            obj = self.doc.find_by_id(spdx_id)
            if obj:
                for ext_ref in getattr(obj, "externalRef", []):
                    ref_type = str(getattr(ext_ref, "externalRefType", "")).lower()
                    if "securityother" in ref_type:
                        has_security = True
                        break

            if not has_security:
                missing.append((name, spdx_id))

        return missing

    def get_components_without_bom_references(self) -> list[tuple[str, str]]:
        """
        Check if the component references another BOM.
        BSI Requirement: MAY be included (Optional Data Field).
        """
        missing: list[tuple[str, str]] = []
        if not isinstance(self.doc, spdx3.SHACLObjectSet):
            return missing

        valid_package_ids = set()

        for from_id, to_ids in iter_relationships_by_type(self.doc, "describes"):
            has_bom_ref = False
            obj = self.doc.find_by_id(from_id)
            if obj and isinstance(obj, spdx3.software_Sbom):
                for ext_ref in getattr(obj, "externalRef", []):
                    ref_type = str(getattr(ext_ref, "externalRefType", "")).lower()
                    if "buildmeta" in ref_type:
                        has_bom_ref = True
                        break

            if has_bom_ref:
                valid_package_ids.update(to_ids)

        for name, spdx_id, _ in iter_objects_with_property(
            self.doc, spdx3.software_Package, "spdxId", self.reachable_component_ids
        ):
            if spdx_id not in valid_package_ids:
                missing.append((name, spdx_id))

        return missing
