# NTIA Conformance Checker

[![Build Status](https://github.com/spdx/ntia-conformance-checker/workflows/build/badge.svg)](https://github.com/spdx/ntia-conformance-checker/actions)
![CodeQL](https://github.com/spdx/ntia-conformance-checker/actions/workflows/codeql.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/ntia-conformance-checker.svg)](https://badge.fury.io/py/ntia-conformance-checker)
[![Pylint Version](https://img.shields.io/badge/linting-pylint-yellow)](https://badge.fury.io/py/ntia-conformance-checker)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/spdx/ntia-conformance-checker/badge)](https://scorecard.dev/viewer/?uri=github.com/spdx/ntia-conformance-checker)

This tool determines whether a [SPDX](https://spdx.dev/) software bill of
materials (SBOM) document contains informational items as required by a
certain specification.

## Conformance

Currently, the only supported specification is the
2021 National Telecommunications and Information Administration (NTIA)
["minimum elements."][ntia]
The mapping of the NTIA elements required data fields to the SPDX 2.3
specification can be found [here][ntia-spdx23].

The minimum elements include:

- Supplier Name
- Component Name
- Version of the Component
- Other Unique Identifiers
- Dependency Relationship
- Author of SBOM Data
- Timestamp

As defined by the NTIA, the minimum elements are
"the essential pieces that support basic SBOM functionality and will serve as
the foundation for an evolving approach to software transparency."

Checking the conformance with 2024 Framing Software Component Transparency
(FSCT3) ["Baseline Attributes"][fsct3] is *experimental and under development*.
The mapping of FSCT3 Baseline Attributes to ISO/IEC 5962:2021 (SPDX 2.2.1) and
SPDX 3.0 can be found at Section 2.5 of the FSCT3 document.

In addition to information similar to NTIA minimum elements,
FSCT3 also requires these Baseline Attributes:

- License
- Copyright Holder

More comparison of SBOM requirements and their mapping to SPDX can be found in
[this slide][sbom-reqs] from Takashi Ninjouji of OpenChain Japan SBOM Sub-WG,
presented at SPDX General Meeting 2024-12-05.

[sbom-reqs]: https://drive.google.com/file/d/14HZGYD7pSSWEmtaHZzWrzPhxCXaCnloJ/view    

## Installation

*Installation Method #1*:
Install from the [Python Package Index (PyPI)][pypi] with `pip`.

`pip install ntia-conformance-checker`

*Installation Method #2*: Install locally.
Clone the repo and install dependencies using the following commands:

```bash
git clone https://github.com/spdx/ntia-conformance-checker.git
cd ntia-conformance-checker
pip install .
```

The tool requires Python 3 (3.8+).
It is recommended to use a virtual python environment especially
if you are using different versions of python.
`virtualenv` is a tool for setting up virtual python environments which
allows you to have all the dependencies for the tool set up in a single
environment, or have different environments set up for testing using different
versions of Python.

## CLI Usage

```text
Usage: sbomcheck [OPTIONS]

Options:
  --file TEXT            The file to be parsed
  --comply [fsct3-min|ntia]
                         Specify which compliance standard to check against
                         - fsct3-min: FSCT3 Baseline Attributes-Minimum Expected
                         - ntia: NTIA minimum elements
                         [default: ntia]
  --output [html|json|print|quiet]
                         Output format  [default: print]
  --output_path TEXT     Filepath for optionally storing output.
  --skip-validation      Specify whether to skip validation
  -v, --verbose          Use verbose printing
  --version              Display version of ntia-conformance-checker
  -h, --help             Show this message and exit.
```

The user can then analyze a particular file:

```bash
sbomcheck --file sbom.json
```

To generate the output in machine-readable JSON, run:

```bash
sbomcheck --file sbom.spdx --output json
```

## Usage as a Library

`ntia-conformance-checker` can also be imported as a library. For example:

```python
from ntia_conformance_checker import SbomChecker

sbom_checker = SbomChecker("SBOM_filepath")

print(sbom_checker.compliant)
```

Additional properties and methods can be found in `BaseChecker` class
at [`base_checker.py`](ntia_conformance_checker/base_checker.py).
Specific properties and methods for a particular specification can be found
at the checker for that specification. For example, `NTIAChecker` class
at [`ntia_checker.py`](ntia_conformance_checker/ntia_checker.py).

## History

This is the result of an initial
[Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/)
contribution in 2022 by
[@linynjosh](https://github.com/linynjosh) and is maintained
by a community of SPDX adopters and enthusiasts.

## License

[Apache-2.0](./LICENSE)

## Dependencies

- [spdx-tools](https://pypi.org/project/spdx-tools/) used for parsing the
  SPDX SBOM.

## Support

- Submit issues, questions or feedback at
  <https://github.com/spdx/ntia-conformance-checker/issues>
- Join the discussion on <https://lists.spdx.org/g/spdx-tech> and
  <https://spdx.dev/participate/tech/>

## Contributing

Contributions are very welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md)
for instructions on how to contribute to the codebase.

## Further help

Check out the [frequently asked questions](./FAQ.md) document.

[ntia]: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
[ntia-spdx23]: https://spdx.github.io/spdx-spec/v2.3/how-to-use/#k22-mapping-ntia-minimum-elements-to-spdx-fields
[fsct3]: https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024
[pypi]: https://pypi.org/project/ntia-conformance-checker/
