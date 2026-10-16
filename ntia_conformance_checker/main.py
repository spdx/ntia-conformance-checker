# SPDX-FileCopyrightText: 2024 SPDX contributors
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0

"""Entrypoint for CLI."""

from __future__ import annotations

import logging
import sys
import warnings

from .cli_utils import get_parsed_args, get_sbom_spec, print_output
from .constants import DEPRECATED_COMPLIANCE_IDS
from .registry import get_spec, spec_ids
from .sbom_checker import SbomChecker


def main() -> None:
    """Entrypoint for CLI application."""

    args = get_parsed_args()

    # Log floor on the shared severity scale error > warning > note > none:
    #   -q/--quiet  -> error   (errors only)
    #   (default)   -> warning (errors + warnings)
    #   -v          -> note    (+ info)        [logging.INFO]
    #   -vv/--debug -> none    (everything)    [logging.DEBUG]
    if args.quiet:
        log_level = logging.ERROR
    elif args.debug or args.verbose >= 2:
        log_level = logging.DEBUG
    elif args.verbose >= 1:
        log_level = logging.INFO
    else:
        log_level = logging.WARNING
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    # Reports show extra detail (per-component misses) at -v or higher.
    verbose = log_level <= logging.INFO

    logging.debug("Checking SBOM: %s", args.file)
    logging.debug("SBOM specification: %s", args.sbom_spec)
    logging.debug("Compliance standard: %s", args.comply)
    logging.debug(
        "SPDX validation: %s", "enabled" if not args.skip_validation else "disabled"
    )

    spec_id = DEPRECATED_COMPLIANCE_IDS.get(args.comply or "", args.comply or "")
    # Custom checkers (bsi) declare only the baseline.
    levels = get_spec(spec_id).maturity_ordinals() if spec_id in spec_ids() else (0,)
    if args.maturity not in levels:
        logging.error(
            "Unknown maturity level %s for %r; valid levels: %s",
            args.maturity,
            args.comply,
            list(levels),
        )
        sys.exit(2)

    detected_sbom_spec = get_sbom_spec(file=args.file, sbom_spec=args.sbom_spec)
    if not detected_sbom_spec:
        sys.exit(1)

    if args.comply in DEPRECATED_COMPLIANCE_IDS:
        logging.warning(
            "Compliance standard %r is deprecated; use %r.",
            args.comply,
            DEPRECATED_COMPLIANCE_IDS[args.comply],
        )

    with warnings.catch_warnings():
        # The deprecated standard id is already reported through logging above.
        warnings.simplefilter("ignore", DeprecationWarning)
        sbom = SbomChecker(
            args.file,
            validate=not args.skip_validation,
            compliance=args.comply,
            sbom_spec=detected_sbom_spec,
        )

    try:
        # A 6.0.0 subclass defines check_compliance() without a parameter.
        is_compliant = (
            sbom.check_compliance(args.maturity)
            if args.maturity
            else sbom.check_compliance()
        )
    except ValueError as exc:  # e.g. a maturity level the standard lacks
        logging.error("%s", exc)
        sys.exit(2)

    logging.debug("Parsing: %s", "OK" if not sbom.parsing_errors else "Failed")
    if not sbom.parsing_errors:
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
        verbose=verbose,
        maturity=args.maturity,
    )

    sys.exit(0 if is_compliant else 1)  # 0 indicates success


if __name__ == "__main__":
    main()
