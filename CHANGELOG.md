---
SPDX-FileCopyrightText: 2025 SPDX contributors
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: Apache-2.0
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keepachangelog]
and this project adheres to [Semantic Versioning][semver].

## [4.1.1] - 2025-11-18

This version primarily focused on improving the HTML output.

The HTML output is now organized into four distinct div blocks,
each with a specific CSS class for easy styling and targeting:

- Errors (parsing, etc.): `<div class="conformance-err">`
- Conformance results: `<div class="conformance-res">`
- Components missing required information: `<div class="conformance-mis">`
- Detailed validation information: `<div class="conformance-val">`

Note: Python 3.9 support will be dropped in the next major release.
This is likely the final version supporting it.

### Fixed

- Fix FSCT3Checker that do not report components without required information
  ([#326][])

[#326]: https://github.com/spdx/ntia-conformance-checker/pull/326

## [4.1.0] - 2025-11-17

This version primarily focused on improving the HTML output.

Note: Python 3.9 support will be dropped in the next major release.
This is likely the final version supporting it.

### Added

- Use detected SPDX version if found ([#309][])
- HTML output now has stylesheet classes for easier formatting ([#323][])

### Changed

- Include components without required information in the HTML output ([#323][])

### Fixed

- Make "--output quiet" print nothing except errors ([#308][])
- Write HTML output to file with --output-file option ([#311][])

[#308]: https://github.com/spdx/ntia-conformance-checker/pull/308
[#309]: https://github.com/spdx/ntia-conformance-checker/pull/309
[#311]: https://github.com/spdx/ntia-conformance-checker/pull/311
[#323]: https://github.com/spdx/ntia-conformance-checker/pull/323

## [4.0.0] - 2025-09-05

### Added

- Add support of SPDX 3.0 ([#277][], [#282][] [#284][], [#290][]).
  - Using [spdx-python-model][] to parse and deserialize SPDX 3 documents.
  - The SPDX 3 support in v4.0.0 is completed during the [Google Summer of Code
    (GSoC) 2025][gsoc2025] program by @bact with the mentorship and support of
    @jspeed-meyers @goneall @jpewdev @rtgdk and the Linux Foundation.
- Add Makefile to simplify common development tasks ([#294][])

[#277]: https://github.com/spdx/ntia-conformance-checker/pull/277
[#282]: https://github.com/spdx/ntia-conformance-checker/pull/282
[#284]: https://github.com/spdx/ntia-conformance-checker/pull/284
[#290]: https://github.com/spdx/ntia-conformance-checker/pull/290
[spdx-python-model]: https://github.com/spdx/spdx-python-model/
[gsoc2025]: https://summerofcode.withgoogle.com/programs/2025/projects/CeR3hQTq
[#294]: https://github.com/spdx/ntia-conformance-checker/pull/294

### Changed

- Print validation context along with validation message ([#274][], [#276][]).
- Drop support for Python 3.8.
  - spdx-python-model requires Python 3.9+.

[#274]: https://github.com/spdx/ntia-conformance-checker/pull/274
[#276]: https://github.com/spdx/ntia-conformance-checker/pull/276

### Fixed

- Add components without copyright texts and without concluded licenses in the
  FSCTv3 output report ([#288][]).
- Fix and improve type hints ([#272][], [#281][]). For example:
  - Fix `BaseChecker.validation_messages` type to `List[ValidationMessage]`.
  - Fix return type of `get_components_without_concluded_licenses`,
    `get_components_without_copyright_texts`, `get_components_without_suppliers`,
    and `get_components_without_versions`
    to honour the `return_tuples` parameter.
  - Note that the next major version may adopt [PEP 585][] and [PEP 604][]
    for less verbose type hinting, which will require Python 3.10.

[#288]: https://github.com/spdx/ntia-conformance-checker/pull/288
[#272]: https://github.com/spdx/ntia-conformance-checker/pull/272
[#281]: https://github.com/spdx/ntia-conformance-checker/pull/281
[PEP 585]: https://peps.python.org/pep-0585/
[PEP 604]: https://peps.python.org/pep-0604/

## [3.2.0] - 2025-03-12

### Added

- Add Sphinx documentation generation support ([#237][]).

[#237]: https://github.com/spdx/ntia-conformance-checker/pull/237

## [3.1.0] - 2024-12-31

### Added

- Add FSCTv3 Common SBOM Baseline Attributes checker ([#224][], [#226][]).

[#224]: https://github.com/spdx/ntia-conformance-checker/pull/224
[#226]: https://github.com/spdx/ntia-conformance-checker/pull/226

## [3.0.0] - 2024-08-16

### Changed

- BREAKING CHANGE: Find the DESCRIBES relationship by looking through attached
  packages ([#189][])

[#189]: https://github.com/spdx/ntia-conformance-checker/pull/189

## [2.0.0] - 2024-04-29

### Changed

- BREAKING CHANGE: Fixed spelling of `ntia_mininum_elements_compliant` property
  ([#175][])
- BREAKING CHANGE: Fix logic error in `get_components_without_suppliers`
  ([#176][])
- BREAKING CHANGE: Revise the implementation of
  `check_dependency_relationships` ([#182][])

[#175]: https://github.com/spdx/ntia-conformance-checker/pull/175
[#176]: https://github.com/spdx/ntia-conformance-checker/pull/176
[#182]: https://github.com/spdx/ntia-conformance-checker/pull/182

## [1.1.0] - 2023-12-28

### Changed

- Provide more information in `get_components_without_`* functions ([#169][])

[#169]: https://github.com/spdx/ntia-conformance-checker/pull/169

## [1.0.0] - 2023-11-25

### Added

- Cut v1.0.0 release ([#163][])

[#163]: https://github.com/spdx/ntia-conformance-checker/pull/163

## [0.1.0] - 2023-01-06

First official release.

Special shoutout:

Credit to @linynjosh for bringing this project to life, implementing
an excellent test suite and comprehensive functionality related to checking
for minimum elements.
Thanks to @goneall, @licquia, and @kestewart for mentoring @linynjosh.

### Added

- Initial commit from Google Summer of Code 2022 ([#1][]).

[#1]: https://github.com/spdx/ntia-conformance-checker/pull/1
[keepachangelog]: https://keepachangelog.com/en/1.1.0/
[semver]: https://semver.org/spec/v2.0.0.html
[4.1.1]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v4.1.1
[4.1.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v4.1.0
[4.0.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v4.0.0
[3.2.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v3.2.0
[3.1.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v3.1.0
[3.0.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v3.0.0
[2.0.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v2.0.0
[1.1.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v1.1.0
[1.0.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v1.0.0
[0.1.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v0.1.0
