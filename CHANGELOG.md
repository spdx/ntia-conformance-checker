---
SPDX-FileCopyrightText: 2025 SPDX contributors
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: Apache-2.0
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keepachangelog]
and this project adheres to [Semantic Versioning][semver].

## [4.0.0] - 2025-09-05

### Added

- Add support of SPDX 3.0 (#284, #290).
  - Using [spdx-python-model][] to parse and deserialize SPDX 3 documents.
  - The SPDX 3 support in v4.0.0 is completed during the [Google Summer of Code
    (GSoC) 2025][gsoc2025] program by @bact with the mentorship and support of
    @jspeed-meyers @goneall @jpewdev @rtgdk and the Linux Foundation.

[gsoc2025]: https://summerofcode.withgoogle.com/programs/2025/projects/CeR3hQTq
[spdx-python-model]: https://github.com/spdx/spdx-python-model/

### Changed

- Print validation context along with validation message (#274, #276).
- Drop support for Python 3.8.
  - spdx-python-model requires Python 3.9+.

### Fixed

- Add components without copyright texts and without concluded licenses in the
  FSCTv3 output report (#288).
- Fix and improve type hints (#272). For example:
  - Fix `BaseChecker.validation_messages` type to `List[ValidationMessage]`.
  - Fix return type of `get_components_without_concluded_licenses`,
    `get_components_without_copyright_texts`, `get_components_without_suppliers`,
    and `get_components_without_versions`
    to honour the `return_tuples` parameter.
  - Note that the next major version may adopt
    [PEP 585](https://peps.python.org/pep-0585/) and
    [PEP 604](https://peps.python.org/pep-0604/) for type hinting,
    which will require Python 3.10.

## [3.2.0] - 2025-03-12

### Added

- Add Sphinx documentation generation support (#237).

## [3.1.0] - 2024-12-31

### Added

- Add FSCTv3 Common SBOM Baseline Attributes checker (#224, #226).

## [0.1.0] - 2023-01-06

First official release.

Special shoutout:

Credit to @linynjosh for bringing this project to life, implementing
an excellent test suite and comprehensive functionality related to checking
for minimum elements.
Thanks to @goneall, @licquia, and @kestewart for mentoring @linynjosh.

### Added

- Initial commit from Google Summer of Code 2022 (#1).

[keepachangelog]: https://keepachangelog.com/en/1.1.0/
[semver]: https://semver.org/spec/v2.0.0.html
[4.0.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v4.0.0
[3.2.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v3.2.0
[3.1.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v3.1.0
[0.1.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v0.1.0
