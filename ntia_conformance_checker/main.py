# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Entrypoint for CLI."""

from __future__ import annotations

import json
import logging
import sys
from typing import Any, Dict, Optional, Tuple

from .base_checker import SUPPORTED_SBOM_SPECS, SUPPORTED_SPDX_VERSIONS
from .cli_utils import get_parsed_args, get_spdx_version
from .sbom_checker import SbomChecker


def main() -> None:
    """Entrypoint for CLI application."""

    args = get_parsed_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    logging.debug("Checking SBOM: %s", args.file)
    logging.debug("SBOM specification: %s", args.sbom_spec)
    logging.debug("Compliance standard: %s", args.comply)
    logging.debug(
        "SPDX validation: %s", "enabled" if not args.skip_validation else "disabled"
    )

    if args.sbom_spec not in SUPPORTED_SBOM_SPECS:
        logging.error(
            "Unsupported SBOM specification: %s. Supported: %s",
            args.sbom_spec,
            ", ".join(sorted(SUPPORTED_SBOM_SPECS)),
        )
        sys.exit(1)

    spdx_version: Optional[Tuple[int, int]] = get_spdx_version(
        args.file, sbom_spec=args.sbom_spec
    )
    if not spdx_version:
        logging.error("Could not determine SPDX version from SBOM.")
        sys.exit(1)
    logging.debug("Detected SPDX version: %d.%d", spdx_version[0], spdx_version[1])

    if spdx_version not in SUPPORTED_SPDX_VERSIONS:
        logging.error(
            "Unsupported SPDX version: %d.%d. Supported: %s",
            spdx_version[0],
            spdx_version[1],
            ", ".join(f"{maj}.{min}" for maj, min in sorted(SUPPORTED_SPDX_VERSIONS)),
        )
        sys.exit(1)

    sbom = SbomChecker(
        args.file,
        validate=not args.skip_validation,
        compliance=args.comply,
        sbom_spec=args.sbom_spec,
    )

    logging.info("Parsing: %s", "OK" if not sbom.parsing_error else "Failed")
    logging.info("Validation: %s", "OK" if not sbom.validation_messages else "Failed")
    if not sbom.parsing_error:
        logging.info("SBOM name: %s", sbom.sbom_name)

    if args.output == "print":
        sbom.print_table_output(verbose=args.verbose)
        if args.verbose:
            sbom.print_components_missing_info()
    elif args.output == "json":
        result_dict: Dict[str, Any] = sbom.output_json()
        if args.output_file:
            with open(args.output_file, "w", encoding="utf-8") as outfile:
                json.dump(result_dict, outfile)
        else:
            print(json.dumps(result_dict, indent=2))
    elif args.output == "html":
        html_output = sbom.output_html()
        print(html_output)

    sys.exit(0 if sbom.compliant else 1)  # 0 indicates success


if __name__ == "__main__":
    main()
