# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Entrypoint for CLI."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from importlib.metadata import version
from typing import Any, Dict

from .sbom_checker import SbomChecker


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


def detect_spdx_version(file: str) -> str:
    """
    Check the SPDX version of the SBOM file.

    XLS file format is not supported.

    Args:
        file (str): The file to be checked.

    Returns:
        str: The SPDX version of the SBOM.
    """
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Skip comments
            if line.startswith("#") or line.startswith("//"):
                continue
            # SPDX 2.x
            # Can have cases that the SPDX version is in another line,
            # to handle that later with regular expression
            if (
                line.startswith("SPDXVersion:")  # tag:value
                or ('"spdxVersion"' in line)  # JSON
                or ("'spdxVersion'" in line)  # JSON
                or line.startswith("spdxVersion:")  # YAML
            ):
                return line.split(":")[-1].strip().strip("\"',").split("-")[-1]
            # SPDX 2.x XML
            # Can have cases that the SPDX version is in another line,
            # to handle that later with regular expression
            if line.startswith("<spdxVersion>"):
                return (
                    line.split("<spdxVersion>")[-1]
                    .split("</spdxVersion>")[0]
                    .strip()
                    .split("-")[-1]
                )
            # SPDX 2.x RDF XML
            # Can have cases that the SPDX version is in another line,
            # to handle that later with regular expression
            if line.startswith("<spdx:specVersion>"):
                return (
                    line.split("<spdx:specVersion>")[-1]
                    .split("</spdx:specVersion>")[0]
                    .strip()
                    .split("-")[-1]
                )
            # SPDX 3.x JSON-LD
            # Can have cases that the RDF URL is in another line,
            # to handle that later with regular expression
            if "@context" in line and "spdx.org/rdf/3" in line:
                return line.split("spdx.org/rdf/")[-1].split("/")[0]

    return "Unknown"


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

    spdx_version = detect_spdx_version(args.file)
    logging.info("Detected SPDX version: %s", spdx_version)

    # Only support 2.2 and 2.3, check only major and minor version
    v = spdx_version.split(".")
    if len(v) > 2:
        v = f"{v[0]}.{v[1]}"
    else:
        v = spdx_version
    if v not in ["2.2", "2.3", "Unknown"]:  # If unknown, leave it to the checker
        logging.error(
            "Unsupported SPDX version: %s. Only SPDX 2.2 and 2.3 are supported.",
            spdx_version,
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
