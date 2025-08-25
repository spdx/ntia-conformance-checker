# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Entrypoint for CLI."""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from importlib.metadata import version
from typing import Any, Dict, Tuple

from spdx_tools.spdx.parser.error import SPDXParsingError
from spdx_tools.spdx.parser.parse_anything import parse_file as spdx2_parse_file

from .sbom_checker import SbomChecker

SUPPORT_SPDX_VERSIONS = ["2.2", "2.3"]


def get_parsed_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Check if SPDX SBOM complies with NTIA minimum elements/"
        "FSCT Common SBOM baseline attributes",
    )
    parser.add_argument("--file", help="Filepath for SPDX SBOM")
    parser.add_argument(
        "--comply",
        choices=["fsct3-min", "ntia"],
        default="ntia",
        help="Specify which compliance standard to check against",
    )
    parser.add_argument(
        "--output",
        choices=["print", "json", "html", "quiet"],
        default="print",
        help="Specify type of output",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Specify whether output should be verbose",
    )
    parser.add_argument("--output_path", help="Filepath for optionally storing output")
    parser.add_argument(
        "--version",
        action="store_true",
        help="Display version of ntia-conformance-checker",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        default=False,
        help="Specify whether to skip validation",
    )

    args = parser.parse_args()

    if not args.file:
        if args.version:
            print(version("ntia-conformance-checker"))
            sys.exit(0)
        parser.print_help()
        sys.exit(0)

    return args


def get_spdx_version(file_name: str) -> Tuple[int, ...]:
    """
    Check the SPDX version of the SBOM file.

    XLS file format is not supported.

    Args:
        file_name (str): The name of the file to be checked.

    Returns:
        Tuple[int, ...]: The SPDX version of the SBOM. E.g. (2, 3) for version 2.3.
    """
    if file_name.lower().endswith(".xls") or file_name.lower().endswith(".xlsx"):
        logging.debug("Excel file format is not supported")
        return tuple()

    # Try parsing the file with spdx_tools first
    doc = None
    try:
        doc = spdx2_parse_file(file_name)
    except SPDXParsingError as exc:
        logging.debug("spdx_tools parser failed: %s", exc)
        doc = None
    except (ValueError, TypeError, OSError) as exc:
        logging.debug("Unexpected error while parsing with spdx_tools: %s", exc)
        doc = None

    # If parsing was successful, return the version tuple. e.g. (2, 3) for 2.3.
    if doc:
        ver = getattr(doc.creation_info, "spdx_version", None)
        if isinstance(ver, str):
            m = re.search(r"SPDX-(\d+)\.(\d+)", ver)
            if m:
                return (int(m.group(1)), int(m.group(2)))  # Returns (MAJOR, MINOR)

    # Fallback: inspect file content with regular expressions.
    # There are cases of incomplete or invalid SPDX files that spdx_tools cannot parse.
    # This will also cover SPDX 3 format.
    content = ""
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as exc:
        logging.debug("Could not read file: %s", exc)
        return tuple()

    # Match MAJOR.MINOR.PATCH version
    patterns = [
        re.compile(
            r"^\s*SPDXVersion\s*:\s*SPDX-(\d+)\.(\d+)(\.(\d+))?", re.MULTILINE
        ),  # SPDX 2 tag:value # SPDXVersion: SPDX-2.2
        re.compile(
            r"['\"]spdxVersion['\"]\s*:\s*['\"]SPDX-(\d+)\.(\d+)(\.(\d+))?"
        ),  # SPDX 2 JSON # "spdxVersion": "SPDX-2.2.1"
        re.compile(
            r"^\s*spdxVersion\s*:\s*['\"]?SPDX-(\d+)\.(\d+)(\.(\d+))?", re.MULTILINE
        ),  # SPDX 2 YAML # spdxVersion: 'SPDX-2.2' or spdxVersion: SPDX-2.2
        re.compile(
            r"<spdxVersion>\s*SPDX-(\d+)\.(\d+)(\.(\d+))?\s*</spdxVersion>"
        ),  # SPDX 2 XML # <spdxVersion>SPDX-2.2</spdxVersion>
        re.compile(
            r"[:<]specVersion>\s*SPDX-(\d+)\.(\d+)(\.(\d+))?\s*<"
        ),  # SPDX 2 RDF XML # <spdx:specVersion>SPDX-2.2</spdx:specVersion>
        re.compile(
            r"[\'\"]@context[\'\"]\s*:\s*[\'\"]https?://spdx\.org/rdf/(\d+)\.(\d+)(\.(\d+))?/"
        ),  # SPDX 3 JSON-LD # "@context": "https://spdx.org/rdf/3.0/spdx-context.jsonld"
    ]

    for pat in patterns:
        m = pat.search(content)
        if m:
            return (int(m.group(1)), int(m.group(2)))  # Returns (MAJOR, MINOR)

    return tuple()


def main():
    """Entrypoint for CLI application."""

    args = get_parsed_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    logging.info("Compliance standard: %s", args.comply)
    logging.info(
        "SPDX validation: %s", "enabled" if not args.skip_validation else "disabled"
    )
    logging.info("Checking SBOM: %s", args.file)

    spdx_version = get_spdx_version(args.file)
    spdx_version_str = (
        f"{spdx_version[0]}.{spdx_version[1]}" if spdx_version else "Unknown"
    )
    logging.info("Detected SPDX version: %s", spdx_version_str)

    if spdx_version_str not in SUPPORT_SPDX_VERSIONS:
        logging.error(
            "Unsupported SPDX version: %s. Only supports versions: %s",
            spdx_version_str,
            ", ".join(SUPPORT_SPDX_VERSIONS),
        )
        sys.exit(1)

    # Check SPDX 2 SBOM
    sbom = SbomChecker(
        args.file, validate=not args.skip_validation, compliance=args.comply
    )

    logging.info("Parsing: %s", "OK" if not sbom.parsing_error else "Failed")
    logging.info("Validation: %s", "OK" if not sbom.validation_messages else "Failed")
    if not sbom.parsing_error:
        logging.info("SBOM name: %s", sbom.sbom_name)

    if args.output == "print":
        sbom.print_table_output(verbose=args.verbose)
        if args.verbose:
            sbom.print_components_missing_info()
    if args.output == "json":
        result_dict: Dict[str, Any] = sbom.output_json()
        if args.output_path:
            with open(args.output_path, "w", encoding="utf-8") as outfile:
                json.dump(result_dict, outfile)
        else:
            print(json.dumps(result_dict, indent=2))
    if args.output == "html":
        html_output = sbom.output_html()
        print(html_output)
    # 0 indicates success
    sys.exit(0 if sbom.compliant else 1)


if __name__ == "__main__":
    main()
