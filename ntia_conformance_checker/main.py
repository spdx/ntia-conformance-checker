"""Entrypoint for CLI."""

# pylint: disable=import-error
import json
import sys

import click

from ntia_conformance_checker.sbom_checker import SbomChecker


@click.command(context_settings={"show_default": True})
@click.option("--file", prompt="File name", help="The file to be parsed")
@click.option(
    "--output",
    default="print",
    type=click.Choice(["print", "json", "quiet"]),
    help="Output format",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Use verbose printing",
)
@click.option(
    "--output_path",
    help="Filepath for optionally storing output.",
)
def main(file, output, verbose, output_path):
    """
    COMMAND-LINE TOOL that checks for NTIA's minimum elements within a
    file of RDF, XML, JSON, YAML or XML format.

    For help: run `ntia-checker --help`
    """
    sbom = SbomChecker(file)
    if output == "print":
        sbom.print_table_output()
        if verbose:
            sbom.print_components_missing_info()
    if output == "json":
        result_dict = sbom.output_json()
        if output_path:
            with open(output_path, "w", encoding="utf-8") as outfile:
                json.dump(result_dict, outfile)
        else:
            print(json.dumps(result_dict, indent=2))
    # 0 indicates success
    sys.exit(0 if sbom.ntia_mininum_elements_compliant else 1)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
