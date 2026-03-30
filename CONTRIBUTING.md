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
pip install -e ".[dev,docs,test]"
```

**Windows users:** Before creating a virtual environment, ensure scripts
can run in PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Create and activate your virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

Then install dependencies:

```powershell
pip install -e ".[dev,docs,test]"
pip install spdx-tools tzdata
```

Or, if you're on a Unix-like system, you can use `make`:

```sh
make install-dev
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

   For every major new functionality added, tests of that functionality should
   be added to an automated test suite. The added tests should be documented in
   the PR description.

   As we use some [`pytest`][pytest] constructs in our test suite, it is needed
   as the test runner:

   In the repo root:

   ```sh
   pytest -vvs
   ```

   [pytest]: https://docs.pytest.org/

6. Lint / static analyse your changes, using [`pylint`][pylint]:

   ```sh
   pylint ntia_conformance_checker/ tests/
   ```

   [pylint]: https://github.com/pylint-dev/pylint

7. Type check your changes:

   Static type analysis is recommended to catch potential bugs and improve code
   quality. We use several type checkers ([`mypy`][mypy], [`pyrefly`][pyrefly],
   and [`pyright`][pyright]) to get different perspectives on the code.

   Run all type checkers:

   ```sh
   make type
   ```

   On Windows, `make` is not available. Run each type checker individually:

   ```powershell
   mypy ntia_conformance_checker/
   pyright ntia_conformance_checker/
   ```

   If you are certain that a line is correct, but the type checker is not able
   to verify it, you may choose to add a relevant `# type: ignore[..]` comment
   with additional explanation to suppress the error.

   [mypy]: https://mypy-lang.org/
   [pyrefly]: https://pyrefly.org/
   [pyright]: https://github.com/microsoft/pyright

9. Format your changes with [`black`][black] and sort import with
    [`isort`][isort]:

   ```sh
   make format
   ```

   On Windows, `make` is not available. Run the formatters directly instead:

   ```powershell
   black ntia_conformance_checker/
   isort ntia_conformance_checker/
   ```

   [black]: https://github.com/psf/black
   [isort]: https://pycqa.github.io/isort/

10. Push the branch to your fork on GitHub:

   ```sh
   git push origin fix-or-improve-something
   ```

11. Make a pull request on GitHub.
12. Continue making more changes and commits on the branch,
    with `git commit --signoff` and `git push`.
13. When done, write a comment on the PR asking for a code review.
14. Some other developer will review your changes and accept your PR.
    The merge should be done with `rebase`, if possible, or with `squash`.
15. The temporary branch on GitHub should be deleted (there is a button for
    deleting it).
16. Delete the local branch as well:

    ```sh
    git checkout master
    git pull -p
    git branch -a
    git branch -d fix-or-improve-something
    ```

## How to run tests

The test framework is using [`pytest`][pytest] as the test runner
and [`Coverage.py`][coverage] to measure code coverage.

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

[coverage]: https://coverage.readthedocs.io/

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

## AI usage policy

### General AI tool policy

AI tools (e.g., LLMs, code assistants, and proofreaders) are permitted as
assistive supplements, not replacements for human judgment.

- **Code review:**
  AI tools may act as a preliminary "peer reviewer" to catch syntax or style
  issues, similar to a non-AI code analysis tool.
  However, a human must perform the final review, validate logic,
  and take full responsibility for all decisions.
- **Automation:**
  AI is acceptable for offloading repetitive, well-understood, and
  time-consuming boilerplate tasks.
- **Verification:**
  All AI-generated suggestions must be manually verified for security,
  performance, and project alignment.

### Special policy for Google Summer of Code (GSoC)

GSoC is a mentorship and learning program.
Over-reliance on AI undermines the educational goals and the evaluation of the
contributor's growth.

- **Writing & proposals:**
  - Prohibited: Generating full proposals, final reports, PR descriptions,
    or substantial parts of those.
  - Permitted: Spell-checking, grammar correction, and feedback on structural
    coherence.
  - Requirement: PR descriptions must be written by the contributor to
    demonstrate a deep understanding of what was changed and why.
  - Note: Your English skills will not be graded; mentors care about your code
    and understanding.
- **Code generation:**
  - Prohibited: Using AI to write entire modules or significant logic blocks.
  - Rationale: The goal of GSoC is your development as a contributor within
    a community. Writing your own code and code comments is essential for
    learning. Furthermore, LLMs often provide inaccurate results for SPDX 3.x,
    as the lack of public datasets for these new standards leads to frequent
    technical hallucinations.
- **Transparency:**
  - Contributors must disclose if AI was used significantly in any part of
    their workflow.
  - Unattributed AI-generated code may be considered a violation of integrity,
    which may result in a failing project evaluation.

All GSoC contributors must adhere to the official
[Guidance for GSoC Contributors using AI tooling in GSoC 2026][gsoc-ai-guidance].

[gsoc-ai-guidance]: https://developers.google.com/open-source/gsoc/resources/ai_guidance#1_always_validate_and_fully_understand_the_code
