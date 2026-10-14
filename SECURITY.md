# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 6.x   | :white_check_mark: |
| 5.x   | :white_check_mark: |
| 4.x   | :x: |
| 3.x   | :x: |
| 2.x   | :x: |
| 1.x   | :x: |
| 0.x   | :x: |

## Reporting a Vulnerability

This repository has private reporting enabled. You can follow [these instructions](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability#privately-reporting-a-security-vulnerability) to report a vulnerability to the maintainers of this project. The maintainers will make a best-effort attempt to respond within two weeks.

## Verify release files

Releases after 6.0.0 attach these files to each
[GitHub release](https://github.com/spdx/ntia-conformance-checker/releases):

- the wheel and the source distribution (sdist), as published on PyPI;
- the software bill of materials (SBOM),
  `ntia_conformance_checker-<version>.spdx3.json`, byte-identical to the SBOM
  embedded in the wheel at `.dist-info/sboms/` ([PEP 770]);
- a [Sigstore] bundle (`<file>.sigstore.json`) for each of the three files
  above.

Each of the three files also has a GitHub artifact attestation
(build provenance).

To verify a downloaded file, put `<file>` and `<file>.sigstore.json` in the
same directory, then run:

```sh
WORKFLOW=spdx/ntia-conformance-checker/.github/workflows/python-publish.yml
pip install sigstore
python -m sigstore verify github <file> \
  --cert-identity "https://github.com/${WORKFLOW}@refs/tags/v<version>"
gh attestation verify <file> -R spdx/ntia-conformance-checker \
  --signer-workflow "${WORKFLOW}" \
  --source-ref refs/tags/v<version>
```

`<file>` is the wheel, the sdist, or the SBOM.

Version 6.0.0 and earlier have no release SBOM, signatures or attestations.

[PEP 770]: https://peps.python.org/pep-0770/
[Sigstore]: https://www.sigstore.dev/
