# ntia-conformance-checker

This 2022 Google Summer of Code project determines whether a [SPDX](https://spdx.dev/) software bill of materials (SBOM) document contains the National Telecommunications and Information Administration (NTIA) ["minimum elements."](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf)

The minimum elements include:
- Supplier Name
- Component Name
- Version of the Component
- Other Unique Identifiers
- Dependency Relationship
- Author of SBOM Data
- Timestamp

As defined by the NTIA, the minimum elements are "the essential pieces that support basic SBOM functionality and will serve as the foundation for an evolving approach to software transparency."

# Installation

Use git to install the `ntia-conformance-checker` tool.

```bash
git clone https://github.com/spdx/ntia-conformance-checker.git
```

Then change directories and install the required Python dependencies using [`pipenv`](https://pipenv.pypa.io/en/latest/).

```bash
cd ntia-conformance-checker
```

```bash
pipenv install
```

Finally, activate the project's virtual environment.

```bash
pipenv shell
```

# Usage

 Navigate to the `cli-tools` directory.

 ```bash
 cd ntia_conformance_checker/cli_tools
 ```

The user can request help via a command-line flag:

```bash
python3 checker.py --help
```

The user can then analyze a particular file:

```bash
python3 checker.py --file sbom.json
```

To make the output machine-readable JSON, run:

```bash
python3 checker.py --output json
```
