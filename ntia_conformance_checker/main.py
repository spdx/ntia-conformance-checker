# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Entrypoint for CLI."""

from __future__ import annotations

import logging
import sys

from .cli_utils import get_parsed_args, get_sbom_spec, print_output
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

    detected_sbom_spec = get_sbom_spec(file=args.file, sbom_spec=args.sbom_spec)
    if not detected_sbom_spec:
        sys.exit(1)

    sbom = SbomChecker(
        args.file,
        validate=not args.skip_validation,
        compliance=args.comply,
        sbom_spec=detected_sbom_spec,
    )

    logging.debug("Parsing: %s", "OK" if not sbom.parsing_error else "Failed")
    if not sbom.parsing_error:
        if args.skip_validation:
            logging.debug("Validation: skipped")
        else:
            logging.debug(
                "Validation: %s", "OK" if not sbom.validation_messages else "Failed"
            )
        logging.debug("SBOM name: %s", sbom.sbom_name)

    print_output(
        sbom,
        output_type=args.output,
        output_file=args.output_file,
        verbose=args.verbose,
    )

    sys.exit(0 if sbom.compliant else 1)  # 0 indicates success


if __name__ == "__main__":
    main()
