# Rule registry

This file is the single source of truth for every conformance rule emitted by
`ntia-conformance-checker`.

Each compliance standard is a `rules/<spec_id>.yaml` file -- pure data, no
Python subclass required.  The engine loads every packaged YAML at import time
and makes it available by spec `id`.  Each rule has a stable, machine-readable
identifier that appears in the tool's SARIF output (`reportingDescriptor.id`),
in textual reports, and -- eventually -- as the OSCAL control ID when an OSCAL
exporter lands.

This document is organised by audience:

- **[Part 1 - Using the rules](#using)** -- read the rule
  catalogue, decode rule ids, and interpret results.
- **[Part 2 - Authoring rules](#authoring)** -- add or modify a
  rule in a `rules/<spec>.yaml` file.
- **[Part 3 - Engine internals](#internals)** -- modify or extend
  the rule engine itself.

---

## Part 1 - Using the rules {#using}

### Rule identifiers

Every rule id follows a uniform scheme so it reads the same in SARIF output,
textual reports, and (eventually) OSCAL:

```text
SBOM-[SPEC]-[CATEGORY]-[NNN]
```

| Segment    | Meaning                                                                                | Example  |
| :--------- | :------------------------------------------------------------------------------------- | :------- |
| `SBOM`     | Fixed namespace prefix shared by every rule id.                                        | `SBOM`   |
| `SPEC`     | `Spec.id` uppercased (hyphen-free, uppercase-safe token).                              | `FSCT3`  |
| `CATEGORY` | Short uppercase code of a category within the spec (`SpecCategory.code`).              | `DF`     |
| `NNN`      | Zero-padded (3-digit) sequence within `(SPEC, CATEGORY)`, in the order the spec lists. | `001`    |

- The **edition is part of the `SPEC` segment** (`fsct3` → `FSCT3`), because each
  edition is a distinct standard with its own requirements.  A later edition
  (`fsct4` → `FSCT4`) gets its own rule-id namespace, so rules never collide
  across editions.
- This naming convention follows SARIF rule
  [SARIF2009](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/sarif2009)
  ("Adopt uniform naming conventions for rule ids").

### Conformance model (orthogonal axes + a target)

A rule is governed by three independent fields, plus one runtime knob.  Keep
them distinct:

| Concept | Field / knob | Question it answers | Values |
| :------ | :----------- | :------------------ | :----- |
| **Maturity** | `maturity` (rule) | *at what depth is this required?* | ordinal `0,1,2…` |
| **Target** | runtime | *how strict is this run?* | a chosen level `T` |
| **Provision** | `provision` (rule) | *if it fails, how bad -- does it block?* | requirement / recommendation / permission |
| **Status** | `status` (rule) | *is the check wired up / emitted at all?* | active / catalogue-only / tbd |

**Maturity scopes *whether* a rule is evaluated (vs. the target); provision
decides *what its failure means*.**  They compose -- don't conflate them.

#### Maturity vs. severity

These are deliberately **separate**:

- **Maturity** (`maturity:` -- a universal ordinal, `0` = baseline, higher =
  more depth/completeness) answers *which tier requires this element*.  Each
  spec declares its own `maturity_levels` mapping every ordinal to a
  spec-specific id + title.  "Compliant at level N" = all rules with `maturity <= N`
  pass.  Maturity carries **no severity**.
- **Provision** (`provision:` -- the ISO/IEC Directives provision type) answers
  *how bad it is when missing*, and is what maps to the severity:

| Provision        | Severity  | Blocks? | Meaning                               |
| :--------------- | :-------- | :-----: | :------------------------------------ |
| `requirement`    | `error`   |   yes   | hard requirement (default)            |
| `recommendation` | `warning` |   no    | advisory                              |
| `permission`     | `none`    |   no    | allowed -- absence is never a finding |

A required element missing *at its maturity level* is an `error` because its
provision is `requirement` -- the tier does not soften it.  A single maturity
level can mix all three provisions.

The severity scale is `error > warning > note > none`, shared by SARIF
`result.level` and the CLI log/verbosity threshold.  **`note` is the
informational band** -- used for logs and tool notifications (parser /
validation messages), *not* for any rule provision.

**Only `requirement` failures break compliance.**  `recommendation` /
`permission` rules still emit findings (warning / none) but are advisory --
e.g. a present-but-implausible value (an SBOM timestamp in the future) is
reported as a `recommendation` → `warning` without making the SBOM
non-conformant to the minimum elements.

#### Maturity levels per spec

Declaring `maturity_levels` is **optional**.  A *flat* spec (e.g. NTIA) omits
it; the loader substitutes a single named baseline (`level 0` / `required`).

| Spec    | Levels (ordinal → id)                                |
| :------ | :--------------------------------------------------- |
| NTIA    | `0 → required` (default, flat)                       |
| FSCT v3 | `0 → minimum`, `1 → recommended`, `2 → aspirational` |

A spec may carry several rules for the same `element_id` at increasing levels,
each with its own deeper probe.

#### Assessment target

An assessment runs against a **target** maturity ordinal `T`, passed per call
(`check_compliance(maturity=T)`, `output_sarif(maturity=T)`, …) or via CLI
`-m/--mature T` (default `0`, must be a level the spec declares).  Scoping is
**cumulative**:

- rules with `maturity <= T` are **in scope** -- evaluated, and (on failure)
  reported + counted toward compliance per their provision;
- rules with `maturity > T` are **out of scope** -- neither evaluated nor
  reported.

The full per-rule evaluation, given a target `T`:

```text
status == tbd            -> not in catalogue, skip
status == catalogue-only -> in catalogue, never emit a result
status == active:
    maturity > T         -> OUT OF SCOPE -> no result
    maturity <= T        -> run probe:
        pass             -> no result
        fail             -> emit at provision->severity
                            (requirement also breaks compliance)
```

**Worked example.**  Two rules for the same element at different depths:

- `R_a` -- dependencies present at top level -- `maturity 0`, `requirement`
- `R_b` -- dependencies 2 levels deep -- `maturity 1`, `requirement`

For an SBOM that declares only top-level dependencies:

| Target `T` | `R_a` (mat 0) | `R_b` (mat 1) | Output | Verdict |
| :--------: | :------------ | :------------ | :----- | :------ |
| `0` | in scope → pass | out of scope | -- | **PASS** |
| `1` | in scope → pass | in scope → fail | `error` | **FAIL** |

The SARIF catalogue still lists every non-TBD rule regardless of `T`; only
*results* are scoped.  The emitted log records the chosen target in
`run.properties.maturityTarget`.

### Rule catalogue

#### NTIA -- Minimum Elements for an SBOM (2021)

Source: *The Minimum Elements For a Software Bill of Materials (SBOM)*,
US Department of Commerce / NTIA, July 12 2021.
[NTIA report](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom)

##### Data Fields (§IV)

The seven baseline data fields listed in the table on p.9.

| Rule ID               | Slug                            | Warning                                              | Severity | Auto-Fix | Status | Clause             |
| :-------------------- | :------------------------------ | :--------------------------------------------------- | :------- | :------: | :----- | :----------------- |
| **SBOM-NTIA-DF-001**  | `ntia-component-supplier-missing`            | An SBOM component should have a supplier name.       | `error`  |    ❌    | Active | §IV (Supplier)     |
| **SBOM-NTIA-DF-002**  | `ntia-component-name-missing`           | An SBOM component should have a name.                | `error`  |    ❌    | Active | §IV (Name)         |
| **SBOM-NTIA-DF-003**  | `ntia-component-version-missing`        | An SBOM component should have a version.             | `error`  |    ❌    | Active | §IV (Version)      |
| **SBOM-NTIA-DF-004**  | `ntia-component-identifier-missing`        | An SBOM component should have a unique identifier.   | `error`  |    ❌    | Active | §IV (Identifiers)  |
| **SBOM-NTIA-DF-005**  | `ntia-dependency-relationships-missing`  | An SBOM should declare dependency relationships.     | `error`  |    ❌    | Active | §IV (Dependencies) |
| **SBOM-NTIA-DF-006**  | `ntia-sbom-author-missing`              | An SBOM should have an author name.                  | `error`  |    ❌    | Active | §IV (Author)       |
| **SBOM-NTIA-DF-007**  | `ntia-sbom-timestamp-missing`           | An SBOM should have a creation timestamp.            | `error`  |    ❌    | Active | §IV (Timestamp)    |

##### Automation Support (§IV, reserved)

Not yet implemented.  Reserved so future work can enable them without
re-numbering Active rules.

| Rule ID               | Slug                              | Warning                                              | Severity | Auto-Fix | Status | Clause          |
| :-------------------- | :-------------------------------- | :--------------------------------------------------- | :------- | :------: | :----- | :-------------- |
| **SBOM-NTIA-AS-001**  | `ntia-machine-readable-format`    | An SBOM should be machine-readable.                  | `error`  |    ❌    | TBD ³  | §IV (Automation) |

##### Practices and Processes (§IV, reserved)

Process-level rules from the NTIA "Practices and Processes" subsection.  None
currently implemented -- most require out-of-SBOM evidence (contracts,
distribution channels) and so will likely surface as `note`-level rules.

| Rule ID               | Slug                                | Warning                                                                  | Severity  | Auto-Fix | Status | Clause                |
| :-------------------- | :---------------------------------- | :----------------------------------------------------------------------- | :-------- | :------: | :----- | :-------------------- |
| **SBOM-NTIA-PP-001**  | `ntia-frequency`                    | An SBOM should be re-issued when the software is updated.                | `note`    |    ❌    | TBD ³  | §IV (Frequency)       |
| **SBOM-NTIA-PP-002**  | `ntia-depth`                        | An SBOM should enumerate all top-level dependencies.                     | `warning` |    ❌    | TBD ³  | §IV (Depth)           |
| **SBOM-NTIA-PP-003**  | `ntia-known-unknowns`               | An SBOM should distinguish missing data from declared "no value".        | `warning` |    ❌    | TBD ³  | §IV (Known Unknowns)  |
| **SBOM-NTIA-PP-004**  | `ntia-distribution-delivery`        | An SBOM should be distributed in a timely manner.                        | `note`    |    ❌    | TBD ³  | §IV (Distribution)    |
| **SBOM-NTIA-PP-005**  | `ntia-access-control`               | An SBOM should specify its access-control terms.                         | `note`    |    ❌    | TBD ³  | §IV (Access Control)  |
| **SBOM-NTIA-PP-006**  | `ntia-accommodation-of-mistakes`    | An SBOM consumer should tolerate omissions and good-faith corrections.   | `note`    |    ❌    | TBD ³  | §IV (Mistakes)        |

#### FSCT3 -- Framing Software Component Transparency (CISA 2024, Third Edition)

Source: *Framing Software Component Transparency: Establishing a Common
Software Bill of Materials (SBOM) Third Edition*, CISA Tooling and
Implementation Working Group, September 3 2024.
[CISA page](https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024)

Rule numbering matches the §2.2.x attribute order in the spec.  The third
"clause" segment of the spec section (the leaf number) is recorded
verbatim in `SpecRule.spec_clause_number`.

##### SBOM Meta-Information (§2.2.1)

| Rule ID                  | Slug                       | Warning                                              | Severity | Auto-Fix | Status            | Clause     |
| :----------------------- | :------------------------- | :--------------------------------------------------- | :------- | :------: | :---------------- | :--------- |
| **SBOM-FSCT3-META-001**  | `fsct3-author-name-missing`         | An SBOM should have an author name.                  | `error`  |    ❌    | Active            | §2.2.1.1   |
| **SBOM-FSCT3-META-002**  | `fsct3-timestamp-missing`           | An SBOM should have a creation timestamp.            | `error`  |    ❌    | Active            | §2.2.1.2   |
| **SBOM-FSCT3-META-003**  | `fsct3-sbom-type-missing`           | An SBOM must declare its type (SBOM generation context). | `error`  |    ❌    | Active            | §2.2.1.3   |
| **SBOM-FSCT3-META-004**  | `fsct3-primary-component-missing`   | An SBOM should identify a primary component.         | `error`  |    ❌    | Catalogue only ¹ | §2.2.1.4   |
| **SBOM-FSCT3-META-005**  | `fsct3-dependency-relationships-missing` | An SBOM should declare dependency relationships.  | `error`  |    ❌    | Active ⁴          | §2.2.2.6   |

##### Component Attributes (§2.2.2)

| Rule ID           | Slug                         | Warning                                                              | Severity | Auto-Fix | Status            | Clause     |
| :---------------- | :--------------------------- | :------------------------------------------------------------------- | :------- | :------: | :---------------- | :--------- |
| **SBOM-FSCT3-COMP-001**  | `fsct3-component-name-missing`        | An SBOM component should have a name.                                | `error`  |    ❌    | Active            | §2.2.2.1   |
| **SBOM-FSCT3-COMP-002**  | `fsct3-component-version-missing`     | An SBOM component should have a version.                             | `error`  |    ❌    | Active            | §2.2.2.2   |
| **SBOM-FSCT3-COMP-003**  | `fsct3-supplier-name-missing`         | An SBOM component should have a supplier name.                       | `error`  |    ❌    | Active            | §2.2.2.3   |
| **SBOM-FSCT3-COMP-004**  | `fsct3-unique-identifier-missing`     | An SBOM component should have a unique identifier.                   | `error`  |    ❌    | Active            | §2.2.2.4   |
| **SBOM-FSCT3-COMP-005**  | `fsct3-cryptographic-hash-missing`    | An SBOM component should have a cryptographic hash.                  | `error`  |    ❌    | Catalogue only ¹ | §2.2.2.5   |
| **SBOM-FSCT3-COMP-006**  | `fsct3-relationship-missing`          | An SBOM component should declare its relationship and completeness.  | `error`  |    ❌    | Catalogue only ¹ | §2.2.2.6   |
| **SBOM-FSCT3-COMP-007**  | `fsct3-concluded-license-missing`     | An SBOM component should have a concluded license.                   | `error`  |    ❌    | Active            | §2.2.2.7   |
| **SBOM-FSCT3-COMP-008**  | `fsct3-copyright-notice-missing`      | An SBOM component should have a copyright notice.                    | `error`  |    ❌    | Active            | §2.2.2.8   |

`FSCT-UNDEC-*` namespace (§2.3 Undeclared SBOM Data) reserved for future
checks (unknown attributes, redacted components, unknown dependencies).

#### Status footnotes

¹ **Catalogue only** -- the rule appears in the SARIF `tool.driver.rules`
catalogue (so consumers can render the full standard surface) but the checker
does not yet emit results for it.  Implementation is pending (Primary Component,
Cryptographic Hash, per-component Relationship).  Tracked for follow-up.

² *(reserved)*

³ **TBD** -- namespace and rule id are reserved.  The rule is **not** emitted
in the SARIF catalogue yet -- listing it here only fixes its future identifier
so that adding the check later does not require renumbering existing Active
or Catalogue-only rules.

⁴ **Stop-gap.**  FSCT §2.2.2.6 ("Relationship") wants a *per-component*
relationship + completeness assertion, tracked as the catalogue-only
`SBOM-FSCT3-COMP-006`.  Until that lands, META-005 falls back to the
NTIA-inherited *document-level* check "the SBOM declares at least one
dependency relationship".  When COMP-006 becomes active, META-005 should be
retired.

#### Auto-Fix legend

| Symbol            | Meaning                                                                 |
| :---------------: | :---------------------------------------------------------------------- |
| ❌                | Not auto-fixable.  SBOM repair requires upstream supplier action.       |
| 💡 *Suggestion*   | Tool can suggest the fix; user must apply.  *Reserved -- not used yet.* |
| 🔧 *Fixable*      | Tool can auto-rewrite the SBOM.  *Reserved -- not used yet.*            |

---

## Part 2 - Authoring rules {#authoring}

This part is for editing a `rules/<spec>.yaml` file.  See
[`rules/_example.yaml`](ntia_conformance_checker/rules/_example.yaml) for an
annotated template covering every field.

### Scope codes

Each `(SPEC, CATEGORY)` pair maps a category `code` to a section of the source
spec:

| Code    | Section in source spec             | Applies to            |
| :------ | :--------------------------------- | :-------------------- |
| `DF`    | NTIA §IV → Data Fields             | per-component + doc   |
| `AS`    | NTIA §IV → Automation Support      | document (reserved)   |
| `PP`    | NTIA §IV → Practices and Processes | document (reserved)   |
| `META`  | FSCT §2.2.1 SBOM Meta-Information  | document              |
| `COMP`  | FSCT §2.2.2 Component Attributes   | per-component         |
| `UNDEC` | FSCT §2.3 Undeclared SBOM Data     | document (reserved)   |

### Identifier derivation

The rule id is **derived** (`Spec.rule_id`), never stored in the YAML, so it
cannot drift from `id` / `category.code` / `number`.  Related fields you *do*
set per rule:

- The lowercased rule id is also a valid OSCAL `control-id` token.  Where the
  eventual OSCAL convention diverges, hold an override in
  `SpecRule.oscal_control_id`.
- Store the literal spec clause number the rule derives from
  (`SpecRule.spec_clause_number`, e.g. `2.2.2.7`) and a deep link
  (`SpecRule.spec_clause_uri`) so SARIF `helpUri` / OSCAL
  `link[rel="reference"]` can point at the exact clause.

### Warning text

Every rule has a canonical, single-sentence **warning** that is the source of
truth for user-facing diagnostic prose (analogous to the *warning* column in
Microsoft's [code analysis rule
catalogue](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/)).
Tools that adopt the same rule id are expected to render the same warning text
so users get a consistent experience across implementations, and so the strings
are localisable from a single place.

Wording follows a small set of parallel patterns:

| Scope                | Pattern                                       |
| :------------------- | :-------------------------------------------- |
| Per-component        | `An SBOM component should have a {X}.`        |
| Per-component (verb) | `An SBOM component should declare {X}.`       |
| Per-document         | `An SBOM should have {X}.`                    |
| Per-document (verb)  | `An SBOM should {verb} {X}.`                  |

Pick the shortest pattern that reads naturally; keep it to one sentence; do not
mention SARIF, the rule id, or implementation details.  In SARIF output the
warning text is emitted as the rule's `shortDescription.text`.

### Adding a new rule

1. Pick the `(SPEC, CATEGORY)` namespace.  Reserve a new category code if the
   rule comes from a section not yet covered.
2. Assign the next free `number` (rendered as `NNN`) within that namespace.
3. Add a row to the relevant catalogue table in Part 1 with slug, warning,
   severity, auto-fix, status, and clause.  Follow the warning-text patterns
   above so users get parallel wording across rules.
4. Add the corresponding `SpecRule` entry to
   `ntia_conformance_checker/rules/<spec>.yaml`, filling `slug` (lowercase
   kebab, **finding-framed**, spec-prefixed -- e.g. `ntia-component-name-missing`),
   `element_id`, `element_description`, `competency_question`, `warning`,
   `spec_clause_number`, `spec_clause_uri`, the `probe`, and (only if different)
   `oscal_control_id`.  The PascalCase report name (SARIF
   `reportingDescriptor.name`) is **derived** from the slug -- do not specify it.
5. Add or extend a fixture in `tests/data/` exercising the rule and assert it
   in `tests/test_output_sarif.py`.

---

## Part 3 - Engine internals {#internals}

This part is for modifying or extending the rule engine itself.

### Architecture

```text
rules/<id>.yaml  --load_spec-->  Spec  --get_spec("<id>")-->  RuleBasedChecker
                                  |                                  |
                                  | run_probes()                     |
                                  v                                  v
                            probe registry  --findings-->  output_json / output_sarif / ...
```

1. **Discovery** -- `registry._discover()` globs `rules/*.yaml` at import,
   skips `_`-prefixed files (templates / docs), and indexes each by `spec.id`.
   `--comply <id>` / `compliance="<id>"` routes to the matching spec.
2. **Load + validate** -- `spec_loader.load_spec()` parses the YAML, rejects
   unknown keys / bad enums, and builds the dataclasses (raises `SpecLoadError`
   on a bad file).
3. **Run** -- a `RuleBasedChecker` resolves its `compliance` argument (id or
   `Spec` object) to a `Spec`, then `run_probes()` executes each rule's probe
   once.  Probes are maturity-independent; maturity filters results at call time.
4. **Report** -- output methods (`check_compliance`, `output_json`,
   `output_sarif`, …) read cached findings filtered by the chosen `maturity`
   level.

### Dataclasses (`spec.py`)

A spec YAML file has four top-level keys -- `spec`, `categories`,
`maturity_levels`, `rules` -- which `load_spec()` assembles into a single
`Spec`:

| Class            | YAML source         | Holds                           |
| :--------------- | :------------------ | :------------------------------ |
| `Spec`           | whole file          | the assembled standard: identity from the `spec:` block, plus the `categories` / `maturity_levels` / `rules` siblings |
| `SpecTaxonomies` | `spec.taxonomies`   | category + clause taxonomy names for SARIF |
| `SpecCategory`   | `categories[]`      | category id / `code` / title    |
| `SpecMaturity`   | `maturity_levels[]` | level ordinal + id (optional; flat = baseline only) |
| `SpecRule`       | `rules[]`           | one check: identity, spec mapping, element, maturity / provision / status, probe, output keys |
| `ProbeRef`       | `rules[].probe`     | probe `name` + `params`         |

`Spec`'s scalar identity (`id`, `title`, `uri`) comes from the `spec:` block;
`maturity_levels` is optional (a flat spec omits it and gets the default
baseline).  Rule ids are derived (`Spec.rule_id`); the PascalCase report name
(`Spec.report_name`) is derived from the rule `slug`.

### Probes (`probes/`)

`rules[].probe.name` is resolved against the probe registry (`probes.lookup`)
and called with `params` as kwargs.  Built-in probes (`probes/presence.py`):

- `require_component_attribute` -- fails per component missing `attribute`.
- `require_document_attribute` -- fails once if the document lacks `attribute`.

`attribute` is a canonical element id from `model.ELEMENT_IDS`.  The checker
resolves it via `components_without(...)` / `document_has(...)`, which dispatch
to `get_components_without_<id>` / `get_doc_<id>` extractors on `BaseChecker`.

### Not yet implemented (the engine supports it; no rules use it yet)

- **Quality / plausibility rules.**  The `recommendation` (warning) and
  `permission` (none) provisions, and the advisory non-blocking-compliance
  path, exist precisely for *present-but-wrong* checks -- e.g. "the SBOM
  creation timestamp exists but is in the future" (`maturity 0`,
  `provision: recommendation` → `warning`, does not break compliance).  No
  such rule or probe ships yet; adding one needs a value-validating probe (the
  current probes only check presence).
- **Higher maturity tiers.**  The `> 0` maturity ordinals are wired end to end
  (scoping, `-m/--mature`, severity), but every real FSCT rule above the
  baseline is still `status: catalogue-only` -- it appears in the catalogue
  but has no probe, so `-m 1` / `-m 2` currently changes scope without adding
  active checks.  Activating a tier = giving its rules `status: active` and a
  depth-appropriate probe.
