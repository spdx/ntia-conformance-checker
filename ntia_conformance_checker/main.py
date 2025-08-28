# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Entrypoint for CLI."""

from __future__ import annotations

import json
import logging
import sys
from typing import Any, Dict

from .cli_utils import get_parsed_args, get_spdx_version
from .sbom_checker import SbomChecker

SUPPORTED_SPDX_VERSIONS = {"2.2", "2.3"}


def main() -> None:
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

    if spdx_version_str not in SUPPORTED_SPDX_VERSIONS:
        logging.error(
            "Unsupported SPDX version: %s. Only supports versions: %s",
            spdx_version_str,
            ", ".join(sorted(SUPPORTED_SPDX_VERSIONS)),
        )
        sys.exit(1)

    sbom_spec: str = ""
    if spdx_version[0] == 2:
        sbom_spec = "spdx2"
    elif spdx_version[0] == 3:
        sbom_spec = "spdx3"
    else:
        logging.error("Unsupported SBOM specification")
        sys.exit(1)

    sbom = SbomChecker(
        args.file,
        validate=not args.skip_validation,
        compliance=args.comply,
        sbom_spec=sbom_spec,
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
