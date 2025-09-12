# SPDX-FileCopyrightText: 2025 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Utilities for CLI."""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from importlib.metadata import version
from typing import Any, Dict, Optional, Tuple

from spdx_tools.spdx.parser.error import SPDXParsingError
from spdx_tools.spdx.parser.parse_anything import parse_file as parse_spdx2_file

from .constants import (
    DEFAULT_COMPLIANCE_STANDARD,
    DEFAULT_SBOM_SPEC,
    SUPPORTED_COMPLIANCE_STANDARDS,
    SUPPORTED_COMPLIANCE_STANDARDS_DESC,
    SUPPORTED_SBOM_SPECS,
    SUPPORTED_SBOM_SPECS_DESC,
    SUPPORTED_SPDX_VERSIONS,
)
from .sbom_checker import BaseChecker

_OUTPUT_CHOICES = {
    "print": "Print report to console",
    "json": "Report in JSON format",
    "html": "Report in HTML format",
    "quiet": "No output unless there are errors",
}


def get_parsed_args() -> argparse.Namespace:
    """Parse command line arguments."""

    epilog_text = (
        "choices:\n"
        "  SBOM specifications (for --sbom-spec):\n"
        + "\n".join(
            f"    {k:<11} {v}" for k, v in sorted(SUPPORTED_SBOM_SPECS_DESC.items())
        )
        + "\n\n"
        "  Compliance standards (for --comply):\n"
        + "\n".join(
            f"    {k:<11} {v}"
            for k, v in sorted(SUPPORTED_COMPLIANCE_STANDARDS_DESC.items())
        )
        + "\n\n"
        "  Report output types (for --output):\n"
        + "\n".join(f"    {k:<11} {v}" for k, v in sorted(_OUTPUT_CHOICES.items()))
        + "\n\n"
        "Examples:\n"
        "  sbomcheck sbom.spdx\n"
        "  sbomcheck -s spdx3 -c fsct3-min -v sbom.json\n"
        "  sbomcheck sbom.yaml --output json --output-file report.json\n"
    )

    parser = argparse.ArgumentParser(
        description="Check if an SPDX SBOM complies with a compliance standard.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=epilog_text,
    )
    parser.add_argument(
        "file", metavar="PATH", nargs="?", help="Filepath for SBOM input"
    )
    parser.add_argument(
        "--file",  # for backward compatibility
        dest="file_opt",
        help=argparse.SUPPRESS,  # hide from help
    )
    parser.add_argument(
        "-s",
        "--sbom-spec",
        choices=sorted(SUPPORTED_SBOM_SPECS),
        default=DEFAULT_SBOM_SPEC,
        help=(
            "SBOM specification of the input file; see below for details "
            f"[default: {DEFAULT_SBOM_SPEC}]"
        ),
    )
    parser.add_argument(
        "-c",
        "--comply",
        choices=sorted(SUPPORTED_COMPLIANCE_STANDARDS),
        default=DEFAULT_COMPLIANCE_STANDARD,
        help=(
            "Compliance standards to check against; see below for details "
            f"[default: {DEFAULT_COMPLIANCE_STANDARD}]"
        ),
    )
    parser.add_argument(
        "--conform",  # alias of --comply
        dest="comply",
        help=argparse.SUPPRESS,  # hide from help
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        default=False,
        help="Skip validation",
    )
    parser.add_argument(
        "-r",
        "--output",
        choices=sorted(_OUTPUT_CHOICES),
        default="print",
        help="Report output type; see below for details [default: print]",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        metavar="PATH",
        help="Filepath for report output; if omitted, prints to console",
    )
    parser.add_argument(
        "--output_path",  # for backward compatibility
        dest="output_file",
        help=argparse.SUPPRESS,  # hide from help
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print more information (debug)",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="Display version of sbomcheck",
    )

    args = parser.parse_args()

    if getattr(args, "file_opt", None):
        args.file = args.file_opt

    if not args.file:
        if args.version:
            print(version("ntia-conformance-checker"))
            sys.exit(0)
        parser.print_help()
        sys.exit(0)

    return args


def get_spdx_version(file: str, sbom_spec: str = "spdx2") -> Optional[Tuple[int, int]]:
    """
    Detect the SPDX version of the SBOM file.

    XLS file format is not supported.

    Args:
        file (str): The name of the file to be checked.
        sbom_spec (str): The SBOM specification hint, the function will try to
                         use the appropriate parser first.

    Returns:
        Tuple[int, int]: The SPDX major.minor version of the SBOM.
                         E.g. (2, 3) for version 2.3.
    """
    if file.lower().endswith(".xls") or file.lower().endswith(".xlsx"):
        logging.debug("Detect SPDX version: Excel file format is not supported")
        return None

    # Try parsing the file with spdx_tools first
    doc = None
    if sbom_spec == "spdx2":
        try:
            doc = parse_spdx2_file(file)
        except SPDXParsingError as exc:
            logging.debug("Detect SPDX version: spdx_tools parser failed: %s", exc)
            doc = None
        except (ValueError, TypeError, OSError) as exc:
            logging.debug(
                "Detect SPDX version: Unexpected error while parsing with spdx_tools: %s",
                exc,
            )
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
        logging.debug("Detect SPDX version: Could not read file: %s", exc)
        return None

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

    return None


def get_sbom_spec(file: str, sbom_spec: str) -> str:
    """Detect SBOM specification from file content."""
    detected_sbom_spec: str = ""

    if sbom_spec not in SUPPORTED_SBOM_SPECS:
        logging.error(
            "Unsupported SBOM specification: %s. Supported: %s",
            sbom_spec,
            ", ".join(sorted(SUPPORTED_SBOM_SPECS)),
        )
        return ""

    if sbom_spec.startswith("spdx"):
        spdx_version: Optional[Tuple[int, int]] = get_spdx_version(
            file, sbom_spec=sbom_spec
        )
        if not spdx_version:
            logging.error("Could not determine SPDX version from SBOM.")
            return ""
        logging.debug("Detected SPDX version: %d.%d", spdx_version[0], spdx_version[1])

        if spdx_version not in SUPPORTED_SPDX_VERSIONS:
            logging.error(
                "Unsupported SPDX version: %d.%d. Supported: %s",
                spdx_version[0],
                spdx_version[1],
                ", ".join(
                    f"{maj}.{min}" for maj, min in sorted(SUPPORTED_SPDX_VERSIONS)
                ),
            )
            return ""

        if spdx_version[0] == 3:
            detected_sbom_spec = "spdx3"
        elif spdx_version[0] == 2:
            detected_sbom_spec = "spdx2"

    return detected_sbom_spec


def print_output(
    sbom: BaseChecker, *, output_type: str, output_file: str, verbose: bool
) -> None:
    """Print or save the output report."""
    if output_type == "print":
        sbom.print_table_output(verbose=verbose)
        if verbose:
            sbom.print_components_missing_info()
    elif output_type == "json":
        result_dict: Dict[str, Any] = sbom.output_json()
        if output_file:
            with open(output_file, "w", encoding="utf-8") as outfile:
                json.dump(result_dict, outfile)
        else:
            print(json.dumps(result_dict, indent=2))
    elif output_type == "html":
        html_output = sbom.output_html()
        if output_file:
            try:
                with open(output_file, "w", encoding="utf-8") as outfile:
                    # Put a simple HTML wrapper around the HTML report snippet
                    outfile.write(
                        "<!DOCTYPE html>\n"
                        "<html>\n"
                        "<head>\n"
                        "  <title>SBOM Conformance Report</title>\n"
                        '  <meta charset="utf-8" />\n'
                        "</head>\n"
                        "<body>\n"
                        "<h1>SBOM Conformance Report</h1>\n"
                    )
                    outfile.write(f"<p>Filename: {sbom.file}</p>\n")
                    outfile.write(html_output)
                    outfile.write("\n</body>\n</html>\n")
            except OSError as exc:
                logging.error("Could not write HTML output file: %s", exc)
        else:
            print(html_output)

    # do nothing if output_type is "quiet" or unrecognized
