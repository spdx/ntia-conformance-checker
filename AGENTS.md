# Agent instructions

## 1. Workflow

- Follow existing code style and repository conventions. Write complete
  docstrings. Add tests for new behavior and keep existing tests passing.
- Before committing, format with `black` and fix everything reported by:

  ```bash
  ruff check --fix . && mypy ntia_conformance_checker tests && pylint ntia_conformance_checker tests && pytest -q
  ```

- Update `CHANGELOG.md` for significant changes ([Keep a Changelog] 1.1.0);
  version releases with Semantic Versioning.
- Commit messages explain the why and the what; use conventional commit style
  where appropriate.
- Include SPDX tags in source files where applicable (see repo examples).

## 2. Code style and typing

- PEP 8 and `black`; exact settings are in `pyproject.toml`.
- Keep functions and modules short; split large functions into smaller units.
- Names: US spelling; concise, clear and consistent across submodules.
  Singular for a class that represents one entity; plural only for
  collections and utility modules.
- Complete type annotations for public APIs (functions, classes, module-level
  variables). Put heavy or optional typing-only imports under
  `if TYPE_CHECKING:`. Minimize `Any`; when unavoidable, prefer a narrow cast
  or `# type: ignore[..]` with an inline justification.
- Documentation: sentence case headings; strict Markdown.

## 3. Tests and CI

- Unit tests for new code paths and edge cases; type-focused tests when
  relevant.
- Deterministic and fast; no network I/O unless explicitly testing
  integration. `tests/test_real_world.py` is slow; run it only when necessary.
- If CI fails because of differing dependency versions, pin the tool or add an
  explanatory comment, and raise a PR to align versions.

## 4. Security, APIs and CLI

- Never commit secrets, credentials or tokens; use environment variables or
  CI secret stores.
- Validate and sanitize all external input. No `eval()`, no untrusted
  deserialization.
- Keep public API changes backward compatible; document breaking changes and
  bump the version accordingly.
- Web APIs: appropriate HTTP status codes; follow OpenAPI.
- CLI: Unix philosophy; output and error messages are consistent, predictable
  and parseable.

## 5. Boundaries

- Ask before: large cross-package refactors, heavyweight dependencies, data
  migrations.
- Never: commit secrets, hand-edit generated files when a generator exists,
  run destructive git operations without approval.

## 6. Standards and specifications

Every check, mapping and review comment must trace to the exact text of a
specific edition of a specific document, not to memory, blog posts or another
tool's behavior.

### 6.1 Rules for writing and reviewing code

- **Read the source first.** Open the edition the check claims to implement
  and read the whole clause, with its notes and the definitions it uses.
- **Cite the clause** for every rule, probe, format mapping and non-obvious
  branch:
  - Rule YAML (`ntia_conformance_checker/rules/*.yaml`): `spec_clause_number`,
    `spec_clause_name` and `spec_clause_uri` exactly as in the source.
  - Code, docstrings and tests: `<document> <edition> §<clause> "<title>"`,
    e.g. `BSI TR-03183-2 v2.1.0 §5.2.2`, `FSCT 3rd ed. §2.2.1.1 "Author
    Name"`, `SPDX 2.3 §7.5 "Package supplier field"`,
    `SPDX 3.0.1 Core/Classes/Agent`,
    `SARIF 2.1.0 §3.49 "reportingDescriptor object"`.
  - No numbered clauses: cite the heading path or table, e.g.
    `CISA 2026 Minimum Elements, Data Fields > SBOM Metadata > "SBOM Author"`,
    `CERT-In v2.0 Table 5`.
- **Match provision strength** in the rule `provision`: MUST/SHALL/REQUIRED →
  `requirement`; SHOULD/RECOMMENDED → `recommendation`; MAY/OPTIONAL →
  `permission`. BSI uses [RFC 2119]/[RFC 8174] keywords (all capitals only);
  where a document uses plain "should"/"expected", note in a YAML comment how
  the strength was decided.
- **Keep editions apart**, e.g. CISA 2025 draft vs. 2026, BSI v2.0.0 vs.
  v2.1.0, SPDX 3.0.1 vs. 3.1-dev. A new edition is a new spec id with its own
  rule file.
- **Normative text wins.** Use non-normative sources, notes, examples and
  informative annexes only to interpret it or to build test fixtures; on
  conflict, follow the normative text and flag the conflict in the PR.
- **Do not guess.** If the source is unavailable or a clause is ambiguous, say
  so in the comment or review; never invent clause numbers, field names or
  URLs.
- **Review checklist:** each changed rule or mapping cites a clause, the
  clause says what the code does, and the severity matches the keyword.

### 6.2 Sources

`refs/` holds the edition this project targets: read it first, and use the
official link only to check for errata or a newer edition.
`refs/spdx/README.md` records where and when each model file was fetched.
`MANIFEST.in` keeps `refs/` out of the sdist; it is never shipped.

SBOM formats (normative):

- [SPDX 3.0.1] has clauses 1–6 (§5 Conformance) and Annexes A–E. Model
  pages are `model/<Profile>/<Category>/<Name>/` (Classes, Properties,
  Vocabularies, Individuals, Datatypes), e.g.
  [Core/Classes/Agent][SPDX 3.0.1 Agent]. `refs/spdx/spdx-model-3.0.1.ttl`
  ([online][SPDX 3.0.1 model]) is the ground truth for names, ranges and
  cardinality; JSON-LD [context][SPDX 3.0.1 context].
- [SPDX 3.1-dev], `refs/spdx/spdx-model-3.1-dev-20261114.ttl`: unreleased;
  implement checks against it only when the task says so.
- [SPDX 2.3] has clauses 1–13 and Annexes A–L; fields are numbered per
  clause, e.g. [§7 Package information][SPDX 2.3 §7]. Also [SPDX 2.2].
- [SPDX License List]; license expressions in SPDX 3.0.1 Annex B and SPDX 2.3
  Annex D.
- Package URL: [ECMA-427] 1st edition (December 2025); purl types, schemas
  and tests at [packageurl.org]. VERS (version ranges), hosted there too, is
  not yet an approved standard.

Minimum elements (normative; the id is the `--comply` value):

- `ntia`: [NTIA 2021] Minimum Elements (July 12, 2021),
  `refs/2021-ntia-sbom-minimum-elements.pdf`. Cite section IV, group and
  element, e.g. "IV. Minimum Elements > Data Fields > Supplier Name". SPDX
  mapping: [SPDX 2.3 Annex K.2.2].
- `fsct3-min`: [Framing Software Component Transparency, 3rd ed.][FSCT 3]
  (CISA, September 3, 2024), `refs/2024-cisa-sbom-baseline-attributes.pdf`.
  §2.2.1 SBOM meta-information, §2.2.2 component attributes, §2.3 undeclared
  data; each attribute has Minimum Expected, Recommended Practice and
  Aspirational Goal levels.
- `bsi`: [BSI TR-03183-2 v2.1.0] Part 2: SBOM (2025-08-20;
  [landing page][BSI TR-03183]), `refs/2025-bsi-sbom-content-requirements.pdf`.
  §2 requirements language; required fields §5.2.1 (SBOM) and §5.2.2
  (component); additional §5.2.3–§5.2.4; optional §5.2.5; licence
  expressions §6.1; format mapping §8.2.
- Not yet implemented:
  - [CISA 2026 Minimum Elements][CISA 2026] (v2.1, July 29, 2026;
    [PDF][CISA 2026 PDF]), `refs/2026-sbom-minimum-elements.pdf`; replaces
    NTIA 2021. No numbered clauses: cite "Data Fields > SBOM Metadata",
    "Data Fields > Component Data" or "Practices and Processes" plus the
    element, or Appendix A Table 1.
  - [G7 SBOM for AI: Minimum Elements][G7 SBOM for AI] (2026),
    `refs/2026-g7-sbom-for-ai-minimum-elements.pdf`. Cite the cluster (§2.1
    Metadata to §2.7 Key Performance Indicators) and element; these add to,
    not replace, the general minimum elements.
  - [CERT-In SBOM, QBOM & CBOM, AIBOM and HBOM guidelines v2.0][CERT-In]
    (09.07.2025), `refs/2025-certin-sbom-guidelines.pdf`. Minimum elements:
    §4 Table 5 (SBOM), §8.3 Tables 8–9 (QBOM, CBOM), §9.3 Table 10 (AIBOM),
    §10.3 Table 11 (HBOM).

Report formats (normative):

- [SARIF 2.1.0 incorporating Errata 01][SARIF 2.1.0] ([schema][SARIF schema]):
  the corrected text; use it, not the original 2.1.0 OASIS Standard. Cite
  object and property clauses, e.g. §3.27 "result object", §3.14.8
  "taxonomies property". `spec.py` maps categories and clauses to SARIF taxa.
- [OSCAL] ([model reference][OSCAL Reference]): planned exporter;
  `SpecCategory` maps to an OSCAL `group`. Cite
  `OSCAL <release> <model> > <path>` for the release the exporter targets.

Non-normative (intent, examples, test fixtures; never requirements):

- [Using SPDX] (see [complying with norms][Using SPDX norms]);
  [spdx-examples] (incl. [conformance][spdx-examples conformance]); SPDX 2.3
  informative [Annex K][SPDX 2.3 Annex K] (how to use) and
  [Annex L][SPDX 2.3 Annex L] (regulation compliance).
- [CISA 2025 Minimum Elements draft][CISA 2025 draft] (August 2025),
  `refs/2025-cisa-sbom-minimum-elements.pdf`: superseded by CISA 2026; use it
  only to trace how an element changed, never as the basis for a check.
- [AI BOM with SPDX 3.0][LF AI BOM] (Linux Foundation, October 2024),
  `refs/2024-spdx-ai-bom.pdf`; [Model Openness Framework v1.0][MOF]
  (LF AI & Data, December 17, 2024), `refs/2024-lf-mof.pdf`.
- ENISA [SBOM Landscape Analysis][ENISA analysis] (draft 1.2, December 2025),
  `refs/2025-enisa-sbom-analysis.pdf`; ENISA
  [SBOM Adoption State of Play 2026][ENISA adoption],
  `refs/2026-enisa-sbom-adoption.pdf`.
- [CISA SBOM] hub; OpenSSF [SBOM-Everywhere] catalog and
  [SBOM tools][OpenSSF SBOM tools]; [SARIF tutorials].
- [SPDX on GitHub][SPDX GitHub]; [Python packaging guide][PyPA].

[BSI TR-03183]: https://bsi.bund.de/dok/TR-03183-en
[BSI TR-03183-2 v2.1.0]: https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TR03183/BSI-TR-03183-2_v2_1_0.html
[CERT-In]: https://www.cert-in.org.in/PDF/TechnicalGuidelines-on-SBOM,QBOM&CBOM,AIBOM_and_HBOM_ver2.0.pdf
[CISA 2025 draft]: https://www.cisa.gov/resources-tools/resources/2025-minimum-elements-software-bill-materials-sbom
[CISA 2026]: https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom
[CISA 2026 PDF]: https://www.cisa.gov/sites/default/files/2026-07/2026_cisa_sbom_minimum_elements_508c.pdf
[CISA SBOM]: https://www.cisa.gov/topics/information-communications-technology-supply-chain-security/sbom
[ENISA adoption]: https://www.enisa.europa.eu/publications/sbom-adoption-state-of-play-2026
[ENISA analysis]: https://www.enisa.europa.eu/sites/default/files/2025-12/SBOM%20Analysis%20-%20Towards%20an%20Implementation%20Guide_v1.20-Published.pdf
[FSCT 3]: https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024
[G7 SBOM for AI]: https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/SBOM-for-AI_minimum-elements.pdf
[Keep a Changelog]: https://keepachangelog.com/en/1.1.0/
[LF AI BOM]: https://www.linuxfoundation.org/hubfs/LF%20Research/lfr_spdx_aibom_102524a.pdf
[MOF]: https://lfaidata.foundation/wp-content/uploads/sites/3/2025/01/05_White_paper_MOF_Specification.pdf
[NTIA 2021]: https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
[ECMA-427]: https://ecma-international.org/wp-content/uploads/ECMA-427_1st_edition_december_2025.pdf
[OpenSSF SBOM tools]: https://openssf.org/technical-initiatives/sbom-tools/
[OSCAL]: https://pages.nist.gov/OSCAL/
[OSCAL Reference]: https://pages.nist.gov/OSCAL-Reference/
[packageurl.org]: https://www.packageurl.org/
[PyPA]: https://packaging.python.org/
[RFC 2119]: https://www.rfc-editor.org/rfc/rfc2119
[RFC 8174]: https://www.rfc-editor.org/rfc/rfc8174
[SARIF 2.1.0]: https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html
[SARIF schema]: https://json.schemastore.org/sarif-2.1.0.json
[SARIF tutorials]: https://github.com/microsoft/sarif-tutorials
[SBOM-Everywhere]: https://sbom-catalog.openssf.org/
[SPDX 2.2]: https://spdx.github.io/spdx-spec/v2.2.2/
[SPDX 2.3]: https://spdx.github.io/spdx-spec/v2.3.1/
[SPDX 2.3 §7]: https://spdx.github.io/spdx-spec/v2.3.1/package-information/
[SPDX 2.3 Annex K]: https://spdx.github.io/spdx-spec/v2.3.1/how-to-use/
[SPDX 2.3 Annex K.2.2]: https://spdx.github.io/spdx-spec/v2.3/how-to-use/#k22-mapping-ntia-minimum-elements-to-spdx-fields
[SPDX 2.3 Annex L]: https://spdx.github.io/spdx-spec/v2.3.1/regulations-compliance/
[SPDX 3.0.1]: https://spdx.github.io/spdx-spec/v3.0.1/
[SPDX 3.0.1 Agent]: https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Classes/Agent/
[SPDX 3.0.1 context]: https://spdx.org/rdf/3.0.1/spdx-context.jsonld
[SPDX 3.0.1 model]: https://spdx.org/rdf/3.0.1/spdx-model.ttl
[SPDX 3.1-dev]: https://spdx.github.io/spdx-spec/v3.1-dev/
[SPDX GitHub]: https://github.com/spdx/
[SPDX License List]: https://spdx.org/licenses/
[spdx-examples]: https://github.com/spdx/spdx-examples/
[spdx-examples conformance]: https://github.com/spdx/spdx-examples/tree/master/conformance
[Using SPDX]: https://spdx.github.io/using/
[Using SPDX norms]: https://spdx.github.io/using/comply-with-norms/
