# Agent instructions

## 1. Contribution workflow

- Follow existing code style and repository conventions.
- Complete docstring.
- Add tests for new behavior and maintain existing tests.
- Run linters and static analysis (`ruff`, `pylint`, `mypy`) and fix reported
  issues before committing.
- Update `CHANGELOG.md` for significant changes, follows Keep a Changelog style
  <https://keepachangelog.com/en/1.1.0/>, and use Semantic Versioning for
  releases.

## 2. Code style & formatting

- Follow PEP 8 for Python; use the project's `pyproject.toml` and tooling for
  exact settings.
- Use `black` formatting rules configured in the repo; run formatters
  before committing.
- Keep functions and modules short and readable; split large functions into
  smaller units.
- Use "Sentence case" for headings in documentation.
  Be strict on Markdown formatting.

## 3. Naming conventions

- US spelling. Concise. Clear. Consistent across submodules.
- Noun number consistency: Maintain strict intentionality regarding singular
  vs. plural forms. Use singular names for classes representing a single entity
  and reserve plural names only for collections or utility modules.

## 4. Typing & static analysis

- Prefer complete type annotations for public APIs (functions, classes,
  module-level variables).
- Use `if TYPE_CHECKING:` for heavy or optional imports used only for typing.
- Minimize use of `Any`. When unavoidable, prefer narrow casts or
  `# type: ignore[..]` with an inline justification.

Recommended local checks to run during development:

```bash
ruff check --fix . && mypy ntia_conformance_checker tests && pylint ntia_conformance_checker tests && pytest -q
```

## 5. Tests & CI

- Add unit tests for new code paths and edge cases; include type-focused tests
  when relevant.
- Keep tests deterministic and fast; avoid network I/O unless explicitly
  testing integration.
- If a CI failure stems from differing dependency versions, prefer pinning
  the tool or adding an explanatory comment and raising a PR to align versions.

## 6. Security & secrets

- Never commit secrets, credentials, or tokens. Use environment variables or
  secrets stores in CI.
- Validate and sanitize all external inputs. Avoid `eval()` and untrusted
  deserialization.

## 7. APIs & backward compatibility

- Design public API changes with backward compatibility in mind.
  Document breaking changes and bump versions accordingly.
- Use appropriate HTTP return codes and follow OpenAPI for web APIs.
- Follow Unix philosophy. Command-line output and error messages must be
  consistent, predictable and parseable.

## 8. Git & commits

- Write clear commit messages that explain the why and what, following
  conventional commit style where appropriate.
- Ask before making large cross-package refactors or adding heavy dependencies.

## 9. File headers & licensing

- Include SPDX tags in source files where applicable (see repo examples).

## 10. Boundaries (what to ask about)

- Ask before: large cross-package refactors, adding heavyweight dependencies,
  or data migrations.
- Never: commit secrets, edit generated files by hand when a generator exists,
  or perform destructive git operations without approval.

## 11. Useful references

- SPDX project code repository: <https://github.com/spdx/>
- Packaging metadata guidelines: <https://packaging.python.org/>
- SBOM-Everywhere: <https://sbom-catalog.openssf.org/>
- 2025 Minimum Elements for SBOM (draft):
  <https://www.cisa.gov/resources-tools/resources/2025-minimum-elements-software-bill-materials-sbom>
