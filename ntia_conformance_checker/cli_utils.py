# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Utilities for CLI."""

from __future__ import annotations

import argparse
import logging
import re
import sys

from importlib.metadata import version
from typing import Tuple
from spdx_tools.spdx.parser.error import SPDXParsingError
from spdx_tools.spdx.parser.parse_anything import parse_file as spdx2_parse_file


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
        "--sbom-spec",
        choices=["spdx2", "spdx3"],
        default="spdx2",
        help="Specify SBOM specification",
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
        help="Display version of sbomcheck",
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


def get_spdx_version(file: str) -> Tuple[int, ...]:
    """
    Detect the SPDX version of the SBOM file.

    XLS file format is not supported.

    Args:
        file (str): The name of the file to be checked.

    Returns:
        Tuple[int, ...]: The SPDX version of the SBOM. E.g. (2, 3) for version 2.3.
    """
    if file.lower().endswith(".xls") or file.lower().endswith(".xlsx"):
        logging.debug("Excel file format is not supported")
        return tuple()

    # Try parsing the file with spdx_tools first
    doc = None
    try:
        doc = spdx2_parse_file(file)
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
        with open(file, "r", encoding="utf-8") as f:
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
