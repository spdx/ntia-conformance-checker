# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keepachangelog]
and this project adheres to [Semantic Versioning][semver].

## [Unreleased]

### Changed

- Add type hints and make it stays compatible with Python 3.8 (#272).
  - Note: The next major version may adopt
    [PEP 585](https://www.python.org/dev/peps/pep-0585/) and
    [PEP 604](https://www.python.org/dev/peps/pep-0604/)
    which will require Python 3.9 and Python 3.10.
- Print validation context along with validation message.

### Fixed

- Fix `BaseChecker.validation_messages` type to `List[ValidationMessage]`.
- Fix return type of `get_components_without_concluded_licenses`,
  `get_components_without_copyright_texts`, `get_components_without_suppliers`,
  and `get_components_without_versions`
  to honour the `return_tuples` parameter.

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
[Unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v3.2.0...HEAD
[3.2.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v3.2.0
[3.1.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v3.1.0
[0.1.0]: https://github.com/spdx/ntia-conformance-checker/releases/tag/v0.1.0
