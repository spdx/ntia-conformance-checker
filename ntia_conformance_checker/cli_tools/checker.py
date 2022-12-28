"""Entrypoint for CLI."""

# pylint: disable=import-error

import json

import click
from check_anything import check_minimum_elements
from output import structure_messages


@click.command(context_settings={"show_default": True})
@click.option("--file", prompt="File name", help="The file to be parsed")
@click.option(
    "--output",
    default="print",
    type=click.Choice(["print", "json"]),
    help="Output format",
)
@click.option(
    "--output_path",
    help="Filepath for optionally storing output.",
)
def main(file, output, output_path):
    """
    COMMAND-LINE TOOL that checks for NTIA's minimum elements within a
    file of RDF, XML, JSON, YAML or XML format.

    For help: run `python3 checker.py --help`
    """
    if output == "print":
        result_list = check_minimum_elements(file).messages
        if output_path:
            with open(output_path, "w", encoding="utf-8") as outfile:
                json.dump(result_list, outfile)
        else:
            print(result_list)
    if output == "json":
        msgs = check_minimum_elements(file).messages
        result_dict = structure_messages(file, msgs)
        if output_path:
            with open(output_path, "w", encoding="utf-8") as outfile:
                json.dump(result_dict, outfile)
        else:
            print(json.dumps(result_dict, indent=2))


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
