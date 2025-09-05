---
SPDX-FileCopyrightText: 2023 SPDX contributors
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: Apache-2.0
---

# How to Cut a New Release

1. Ensure the version field in the `pyproject.toml` file has been updated to
    the version of the new planned release.
    - Also check other metadata fields such as `requires-python` and
    `dependencies` to ensure they are up to date.
    - Significant changes should be documented in the `CHANGELOG.md` file.
2. After the `pyproject.toml` and `CHANGELOG.md` files has been updated,
    navigate to the [releases page][releases] and click the
    "Draft a new release" button.
    - *Only project maintainers are able to perform this step.*
3. Then enter the new tag in the "Choose a tag" box.
    - The tag should begin with "v", as in, for instance, `v0.5.1`.
    - This project follows [Semantic Versioning 2.0.0][semver].
4. The release title should be the same as the new version tag.
    - For instance, the title could be `v0.5.1`.
5. The click the "Generate release notes" button.
6. You can optionally include any particular thank-you's to contributors or
    reviewers in a note at the bottom of the release.
7. You can then click "Publish release".
8. If the run is successful, then the release will be published on both the
    [GitHub releases page][releases] and also the [Python Package Index][pypi].

[releases]: https://github.com/spdx/ntia-conformance-checker/releases
[semver]: https://semver.org/
[pypi]: https://pypi.org/project/ntia-conformance-checker/
