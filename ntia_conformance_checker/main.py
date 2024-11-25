# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Entrypoint for CLI."""

import argparse
import json
import sys
from importlib.metadata import version

from .sbom_checker import SbomChecker


def get_parsed_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Check if SPDX SBOM complies with NTIA minimum elements/CISA common SBOM baseline attributes",
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


def main():
    """Entrypoint for CLI application."""

    args = get_parsed_args()

    sbom = SbomChecker(args.file, validate=not args.skip_validation, compliance=args.comply)
    print(f"Checking SBOM: {args.file}")
    print(f"Compliance standard: {args.comply}")
    print(f"SPDX validation: {'enabled' if not args.skip_validation else 'disabled'}")
    if args.output == "print":
        sbom.print_table_output()
        if args.verbose:
            sbom.print_components_missing_info()
    if args.output == "json":
        result_dict = sbom.output_json()
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
