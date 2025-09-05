# Contributing

Thank you for your interest in `ntia-conformance-checker`.
The project is open-source software, and bug reports, suggestions, and
most especially patches are welcome.

## Issues

`ntia-conformance-checker` has a [project page on GitHub][project-github]
where you can [create an issue][new-issue] to report a bug, make a suggestion,
or propose a substantial change or improvement.

You may also wish to contact the SPDX working group technical team through its
mailing list, [spdx-tech@lists.spdx.org](mailto:spdx-tech@lists.spdx.org).

If you would like to work on a fix for any issue,
please assign the issue to yourself or write a comment indicating your
intention prior to creating a patch.

[project-github]: https://github.com/spdx/ntia-conformance-checker/
[new-issue]: https://github.com/spdx/ntia-conformance-checker/issues/new

## Development environment setup

It is recommended to use a Python virtual environment for development.

To install development dependencies, run:

```sh
pip install -e ".[dev]"
```

## Development process

We use the GitHub flow that is described here:
<https://guides.github.com/introduction/flow/>

Here's the process to make changes to the codebase:

1. Find or [file an issue](#issues) you'd like to address.
    - Every change should be made to fix or close an issue.
    - Please try to keep issues reasonably small, focusing on one aspect,
      or split off sub-issues if possible.
    - Large pull requests that fix many things at the same time tend to
      cause a lot of conflicts.

2. Review [open pull requests][pr] before committing time to a substantial
   revision. Work along similar lines may already be in progress.

   [pr]: https://github.com/spdx/ntia-conformance-checker/pulls

3. Create a new branch:

   ```sh
   git checkout -b fix-or-improve-something
   ```

4. Make some changes and commit them to the branch:

   ```sh
   git commit --signoff -m 'description of my changes'
   ```

   **Licensing**:

   Please sign off in each of your commits that you license your contributions
   under the terms of [the Developer Certificate of Origin (DCO)][dco].

   Git has utilities for signing off on commits:
   - `git commit -s` or `--signoff` signs a current commit,
   - `git rebase --signoff <revision-range>` retroactively signs a range of
     past commits.

   [dco]: https://developercertificate.org/

5. Test your changes:

   In the repo root:

   ```sh
   python setup.py test
   ```

   You may use other test runners, such as [`pytest`][pytest] or [`nose`][nose]
   at your preference.

   [pytest]: https://docs.pytest.org/
   [nose]: https://nose.readthedocs.io/

6. Type check your changes:

   Static type analysis is recommended to catch potential bugs and improve code
   quality. We use several type checkers ([`mypy`][mypy], [`pyrefly`][pyrefly],
   [`pyright`][pyright], and [`pytype`][pytype]) to get different perspectives
   on the code.

   ```sh
   mypy ntia_conformance_checker
   ```

   ```sh
   pyrefly check ntia_conformance_checker
   ```

   ```sh
   pyright ntia_conformance_checker
   ```

   ```sh
   pytype ntia_conformance_checker
   ```

   If you are certain that a line is correct but the type checker is not able
   to verify it, you may choose to add a `# type: ignore` comment with
   additional explanation at the end of the line to suppress the error.

   [mypy]: https://mypy-lang.org/
   [pyrefly]: https://pyrefly.org/
   [pyright]: https://github.com/microsoft/pyright
   [pytype]: https://github.com/google/pytype

7. Format your changes with [`black`][black] and [`pylint`][pylint]:

   ```sh
   black pylint ntia_conformance_checker/ tests/
   ```

   ```sh
   pylint ntia_conformance_checker/ tests/
   ```

   [black]: https://github.com/psf/black
   [pylint]: https://github.com/pylint-dev/pylint

8. Push the branch to your fork on GitHub:

   ```sh
   git push origin fix-or-improve-something
   ```

9. Make a pull request on GitHub.

10. Continue making more changes and commits on the branch,
    with `git commit --signoff` and `git push`.
11. When done, write a comment on the PR asking for a code review.
12. Some other developer will review your changes and accept your PR.
    The merge should be done with `rebase`, if possible, or with `squash`.
13. The temporary branch on GitHub should be deleted (there is a button for
    deleting it).
14. Delete the local branch as well:

    ```sh
    git checkout master
    git pull -p
    git branch -a
    git branch -d fix-or-improve-something
    ```

## How to run tests

The tests framework is using [pytest][] as the test runner
and [coverage][] to measure code coverage.

Install test dependencies:

```sh
pip install ".[test]"
```

Run tests and show verbose output:

```sh
pytest -vvs
```

Run tests with coverage report and show line numbers of missed lines:

```sh
coverage run -m pytest
coverage report -m
```

## How to generate API documentation

This package uses [Sphinx][] to generate API documentation from
Python docstrings.

Install documentation dependencies:

```sh
pip install ".[docs]"
```

Generate the API documentation and HTML files:

```sh
sphinx-apidoc -o docs/ ntia_conformance_checker/
cd docs
make html
```

[sphinx]: https://www.sphinx-doc.org/
