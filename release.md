---
SPDX-FileCopyrightText: 2023 SPDX contributors
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: Apache-2.0
---

# How to cut a new release

The version comes from the git tag ([setuptools-scm]); `pyproject.toml` has
no version field. This project follows [Semantic Versioning 2.0.0][semver].

## Prepare

1. In `CHANGELOG.md`, move the `[Unreleased]` entries to a new
   `## [X.Y.Z] - YYYY-MM-DD` section, and update the `[Unreleased]` and
   `[X.Y.Z]` links at the end of the file.
2. In `CITATION.cff`, set `version` and `date-released`.
3. Check other metadata in `pyproject.toml`, such as `requires-python` and
   `dependencies`.
4. Merge these changes to `main`.

## Publish

Only project maintainers can do these steps.

1. On the [releases page][releases], click "Draft a new release".
2. Create the tag `vX.Y.Z` (for example `v6.1.1`) on `main`. Use the tag as
   the release title.
3. Write the release notes, or click "Generate release notes".
4. Click "Publish release".

Publishing the release runs the
[`python-publish.yml`](.github/workflows/python-publish.yml) workflow:

1. **Build distribution**: builds the wheel and the sdist, embeds an SPDX 3
   SBOM in the wheel with Pitloom, and fails if the SBOM is invalid.
2. **Publish to PyPI**: uploads the wheel and the sdist to [PyPI][pypi].
3. **Attach files to GitHub Release**: attaches the wheel, the sdist and the
   SBOM.
4. **Sign artifacts and attach provenance**: signs the three files with
   Sigstore, creates build provenance attestations, and attaches the
   `.sigstore.json` bundles.

Steps 3 and 4 run only after the PyPI upload succeeds. See "Verify release
files" in [`SECURITY.md`](SECURITY.md) for how users check these files.

## If a job fails

- Before **Publish to PyPI** succeeds: fix the cause, delete the release and
  the tag, and publish again.
- After **Publish to PyPI** succeeds: PyPI does not accept the same version
  again, and a rebuilt wheel would differ from the one on PyPI.
  - If the failure was transient (for example a network error), use
    "Re-run failed jobs". It reuses the built files while the workflow
    artifacts exist (`dist` for 60 days, `sbom` for the repository's
    default retention). Do not use "Re-run all jobs": it rebuilds the wheel.
  - If the workflow itself is wrong, a re-run uses the same workflow file
    from the tag and fails again. Fix the workflow and release a new patch
    version.

[pypi]: https://pypi.org/project/ntia-conformance-checker/
[releases]: https://github.com/spdx/ntia-conformance-checker/releases
[semver]: https://semver.org/
[setuptools-scm]: https://setuptools-scm.readthedocs.io/
