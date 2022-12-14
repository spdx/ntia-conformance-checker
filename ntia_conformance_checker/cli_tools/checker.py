from check_anything import check_minimum_elements

import click


@click.command()
@click.option("--file", prompt="File name", help="The file to be parsed")
def main(file):
    """
    COMMAND-LINE TOOL that checks for NTIA's minimum elements within a  file of RDF, XML, JSON, YAML and XML format.

    To use : run `python3 checker.py` using terminal or run `python3 checker.py --file <file name>`

    """
    print(check_minimum_elements(file).messages)


if __name__ == "__main__":
    main()
