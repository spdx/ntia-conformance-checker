[![Build Status](https://github.com/spdx/ntia-conformance-checker/workflows/build/badge.svg)](https://github.com/spdx/ntia-conformance-checker/actions)

# NTIA Conformance Checker

This tool determines whether a [SPDX](https://spdx.dev/) software bill of materials (SBOM) document contains the National Telecommunications and Information Administration (NTIA) ["minimum elements."](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf) The mapping of the NTIA elements required data fields to the SPDX specification can be found [here](https://spdx.github.io/spdx-spec/v2.3/how-to-use/#k22-mapping-ntia-minimum-elements-to-spdx-fields).

The minimum elements include:
- Supplier Name
- Component Name
- Version of the Component
- Other Unique Identifiers
- Dependency Relationship
- Author of SBOM Data
- Timestamp

As defined by the NTIA, the minimum elements are "the essential pieces that support basic SBOM functionality and will serve as the foundation for an evolving approach to software transparency."

## Installation

To install use the following command:

`pip install ntia-conformance-checker`

Alternatively, just clone the repo and install dependencies using the following commands:

```bash
git clone https://github.com/spdx/ntia-conformance-checker.git
pip install .
```

The tool requires Python 3 (3.8+). It is recommended to use a virtual python environment especially
if you are using different versions of python. `virtualenv` is a tool for setting up virtual python environments which
allows you to have all the dependencies for the tool set up in a single environment, or have different environments set
up for testing using different versions of Python.

## Usage

```
Usage: ntia-checker [OPTIONS]

Options:
  --file TEXT            The file to be parsed
  --output [print|json]  Output format  [default: print]
  -v, --verbose          Use verbose printing
  --output_path TEXT     Filepath for optionally storing output.
  --help                 Show this message and exit.
```

The user can then analyze a particular file:

```bash
ntia-checker --file sbom.json
```

To generare the output in machine-readable JSON, run:

```bash
ntia-checker --file sbom.spdx --output json
```

# History

This is the result of an initial [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/) contribution in 2022 by
[@linynjosh](https://github.com/linynjosh) and is maintained
by a community of SPDX adopters and enthusiasts.

# License

[Apache-2.0](LICENSE)

# Dependencies

* [spdx-tools](https://pypi.org/project/spdx-tools/) used for parsing the SPDX SBOM.
* [click](https://pypi.org/project/click/) for creating the CLI interface.

# Support

* Submit issues, questions or feedback at https://github.com/spdx/ntia-conformance-checker/issues
* Join the discussion on https://lists.spdx.org/g/spdx-tech and https://spdx.dev/participate/tech/

# Contributing

Contributions are very welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md) for instructions on how to contribute to the codebase.

# Further help

Check out the [frequently asked questions](FAQ.md) document.
