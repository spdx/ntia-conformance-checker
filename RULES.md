# Rule registry

This file is the single source of truth for every conformance rule emitted by
`ntia-conformance-checker`.

Each rule has a stable, machine-readable identifier that appears in the
tool's SARIF output (`reportingDescriptor.id`), in textual reports,
and -- eventually -- as the OSCAL control ID when an OSCAL exporter lands.

## Identifier scheme

```text
SBOM-[SPEC]-[CATEGORY]-[NNN]
```

| Segment    | Meaning                                                                                | Example  |
| :--------- | :------------------------------------------------------------------------------------- | :------- |
| `SBOM`     | Fixed namespace prefix shared by every rule id.                                        | `SBOM`   |
| `SPEC`     | `Spec.id` uppercased (hyphen-free, uppercase-safe token).                               | `FSCT3`  |
| `CATEGORY` | Short uppercase code of a category within the spec (`SpecCategory.code`).               | `DF`     |
| `NNN`      | Zero-padded (3-digit) sequence within `(SPEC, CATEGORY)`, in the order the spec lists.  | `001`    |

* The id is derived (`Spec.rule_id`), never stored in the YAML, so it cannot
  drift from `id` / `category.code` / `number`.
* The **edition is part of the `SPEC` segment** (`fsct3` → `FSCT3`), because each
  edition is a distinct standard with its own requirements.  A later edition
  (`fsct4` → `FSCT4`) therefore gets its own rule-id namespace, so rules never
  collide across editions.
* The lowercased rule id is also a valid OSCAL `control-id` token.  Where the
  eventual OSCAL convention diverges, an override is held in
  `SpecRule.oscal_control_id`.
* Each rule also stores the literal spec clause number it derives from
  (`SpecRule.spec_clause_number`, e.g. `2.2.2.7`) and a deep link
  (`SpecRule.spec_clause_uri`) so SARIF `helpUri` / OSCAL `link[rel="reference"]`
  can point at the exact clause.
* This naming convention follows SARIF rule
  [SARIF2009](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/sarif2009)
  ("Adopt uniform naming conventions for rule ids").

## Scope codes

| Code | Section in source spec                | Applies to            |
| :--- | :------------------------------------ | :-------------------- |
| `DF` | NTIA §IV → Data Fields                | per-component + doc   |
| `AS` | NTIA §IV → Automation Support         | document (reserved)   |
| `PP` | NTIA §IV → Practices and Processes    | document (reserved)   |
| `META` | FSCT §2.2.1 SBOM Meta-Information   | document              |
| `COMP` | FSCT §2.2.2 Component Attributes    | per-component         |
| `UNDEC` | FSCT §2.3 Undeclared SBOM Data     | document (reserved)   |

## Conformance model (orthogonal axes + a target)

A rule is governed by three independent fields, plus one runtime knob.  Keep
them distinct:

| Concept | Field / knob | Question it answers | Values |
| :------ | :----------- | :------------------ | :----- |
| **Maturity** | `maturity` (rule) | *at what depth is this required?* | ordinal `0,1,2…` |
| **Target** | runtime | *how strict is this run?* | a chosen level `T` |
| **Provision** | `provision` (rule) | *if it fails, how bad — does it block?* | requirement / recommendation / permission |
| **Status** | `status` (rule) | *is the check wired up / emitted at all?* | active / catalogue-only / tbd |

**Maturity scopes *whether* a rule is evaluated (vs. the target); provision
decides *what its failure means*.**  They compose — don't conflate them.

### Maturity vs. severity

These are deliberately **separate**:

* **Maturity** (`maturity:` -- a universal ordinal, `0` = baseline, higher =
  more depth/completeness) answers *which tier requires this element*.  Each
  spec declares its own `maturity_levels` mapping every ordinal to a
  spec-specific id + title.  "Compliant at level N" = all rules with `maturity <= N`
  pass.  Maturity carries **no severity**.
* **Provision** (`provision:` -- the ISO/IEC Directives provision type) answers
  *how bad it is when missing*, and is what maps to the severity:

| Provision        | Severity  | Blocks? | Meaning                                      |
| :--------------- | :-------- | :-----: | :------------------------------------------- |
| `requirement`    | `error`   |   yes   | hard requirement (default)                   |
| `recommendation` | `warning` |   no    | advisory                                     |
| `permission`     | `none`    |   no    | allowed -- absence is never a finding        |

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

### Maturity levels per spec

Declaring `maturity_levels` is **optional**.  A *flat* spec (e.g. NTIA) omits
it; the loader substitutes a single named baseline (`level 0` / `required`).

| Spec    | Levels (ordinal → id)                                                   |
| :------ | :---------------------------------------------------------------------- |
| NTIA    | `0 → required` (default, flat)                                          |
| FSCT v3 | `0 → minimum`, `1 → recommended`, `2 → aspirational`                   |

A spec may carry several rules for the same `element_id` at increasing levels,
each with its own deeper probe.

### Assessment target

An assessment runs against a **target** maturity ordinal `T`
(`SbomChecker(..., target_maturity=T)` or CLI `-m/--mature T`;
default `0`, must be a level the spec declares).  Scoping is **cumulative**:

* rules with `maturity <= T` are **in scope** -- evaluated, and (on failure)
  reported + counted toward compliance per their provision;
* rules with `maturity > T` are **out of scope** -- neither evaluated nor
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

* `R_a` -- dependencies present at top level -- `maturity 0`, `requirement`
* `R_b` -- dependencies 2 levels deep -- `maturity 1`, `requirement`

For an SBOM that declares only top-level dependencies:

| Target `T` | `R_a` (mat 0) | `R_b` (mat 1) | Output | Verdict |
| :--------: | :------------ | :------------ | :----- | :------ |
| `0` | in scope → pass | out of scope | — | **PASS** |
| `1` | in scope → pass | in scope → fail | `error` | **FAIL** |

The SARIF catalogue still lists every non-TBD rule regardless of `T`; only
*results* are scoped.  The emitted log records the chosen target in
`run.properties.maturityTarget`.

### Not yet implemented (the engine supports it; no rules use it yet)

* **Quality / plausibility rules.**  The `recommendation` (warning) and
  `permission` (none) provisions, and the advisory non-blocking-compliance
  path, exist precisely for *present-but-wrong* checks -- e.g. "the SBOM
  creation timestamp exists but is in the future" (`maturity 0`,
  `provision: recommendation` → `warning`, does not break compliance).  No
  such rule or probe ships yet; adding one needs a value-validating probe (the
  current probes only check presence).
* **Higher maturity tiers.**  The `> 0` maturity ordinals are wired end to end
  (scoping, `-m/--mature`, severity), but every real FSCT rule above the
  baseline is still `status: catalogue-only` -- it appears in the catalogue
  but has no probe, so `-m 1` / `-m 2` currently changes scope without adding
  active checks.  Activating a tier = giving its rules `status: active` and a
  depth-appropriate probe.

## Warning text

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

---

## NTIA -- Minimum Elements for an SBOM (2021)

Source: *The Minimum Elements For a Software Bill of Materials (SBOM)*,
US Department of Commerce / NTIA, July 12 2021.
[NTIA report](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom)

### Data Fields (§IV)

The seven baseline data fields listed in the table on p.9.

| Rule ID         | Slug                            | Warning                                              | Severity | Auto-Fix | Status | Clause             |
| :-------------- | :------------------------------ | :--------------------------------------------------- | :------- | :------: | :----- | :----------------- |
| **SBOM-NTIA-DF-001**  | `ntia-component-supplier-name`            | An SBOM component should have a supplier name.       | `error`  |    ❌    | Active | §IV (Supplier)     |
| **SBOM-NTIA-DF-002**  | `ntia-component-name`           | An SBOM component should have a name.                | `error`  |    ❌    | Active | §IV (Name)         |
| **SBOM-NTIA-DF-003**  | `ntia-component-version`        | An SBOM component should have a version.             | `error`  |    ❌    | Active | §IV (Version)      |
| **SBOM-NTIA-DF-004**  | `ntia-component-identifier`        | An SBOM component should have a unique identifier.   | `error`  |    ❌    | Active | §IV (Identifiers)  |
| **SBOM-NTIA-DF-005**  | `ntia-dependency-relationship`  | An SBOM should declare dependency relationships.     | `error`  |    ❌    | Active | §IV (Dependencies) |
| **SBOM-NTIA-DF-006**  | `ntia-sbom-author`              | An SBOM should have an author name.                  | `error`  |    ❌    | Active | §IV (Author)       |
| **SBOM-NTIA-DF-007**  | `ntia-sbom-timestamp`           | An SBOM should have a creation timestamp.            | `error`  |    ❌    | Active | §IV (Timestamp)    |

### Automation Support (§IV, reserved)

Not yet implemented.  Reserved so future work can enable them without
re-numbering Active rules.

| Rule ID         | Slug                              | Warning                                              | Severity | Auto-Fix | Status | Clause          |
| :-------------- | :-------------------------------- | :--------------------------------------------------- | :------- | :------: | :----- | :-------------- |
| **SBOM-NTIA-AS-001**  | `ntia-machine-readable-format`    | An SBOM should be machine-readable.                  | `error`  |    ❌    | TBD ³  | §IV (Automation) |

### Practices and Processes (§IV, reserved)

Process-level rules from the NTIA "Practices and Processes" subsection.  None
currently implemented -- most require out-of-SBOM evidence (contracts,
distribution channels) and so will likely surface as `note`-level rules.

| Rule ID         | Slug                                | Warning                                                                  | Severity  | Auto-Fix | Status | Clause                |
| :-------------- | :---------------------------------- | :----------------------------------------------------------------------- | :-------- | :------: | :----- | :-------------------- |
| **SBOM-NTIA-PP-001**  | `ntia-frequency`                    | An SBOM should be re-issued when the software is updated.                | `note`    |    ❌    | TBD ³  | §IV (Frequency)       |
| **SBOM-NTIA-PP-002**  | `ntia-depth`                        | An SBOM should enumerate all top-level dependencies.                     | `warning` |    ❌    | TBD ³  | §IV (Depth)           |
| **SBOM-NTIA-PP-003**  | `ntia-known-unknowns`               | An SBOM should distinguish missing data from declared "no value".        | `warning` |    ❌    | TBD ³  | §IV (Known Unknowns)  |
| **SBOM-NTIA-PP-004**  | `ntia-distribution-delivery`        | An SBOM should be distributed in a timely manner.                        | `note`    |    ❌    | TBD ³  | §IV (Distribution)    |
| **SBOM-NTIA-PP-005**  | `ntia-access-control`               | An SBOM should specify its access-control terms.                         | `note`    |    ❌    | TBD ³  | §IV (Access Control)  |
| **SBOM-NTIA-PP-006**  | `ntia-accommodation-of-mistakes`    | An SBOM consumer should tolerate omissions and good-faith corrections.   | `note`    |    ❌    | TBD ³  | §IV (Mistakes)        |

---

## FSCT -- Common SBOM (CISA 2024, Third Edition)

Source: *Framing Software Component Transparency: Establishing a Common
Software Bill of Materials (SBOM) Third Edition*, CISA Tooling and
Implementation Working Group, September 3 2024.
[CISA page](https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024)

Rule numbering matches the §2.2.x attribute order in the spec.  The third
"clause" segment of the spec section (the leaf number) is recorded
verbatim in `SpecRule.spec_clause_number`.

### SBOM Meta-Information (§2.2.1)

| Rule ID           | Slug                       | Warning                                              | Severity | Auto-Fix | Status            | Clause     |
| :---------------- | :------------------------- | :--------------------------------------------------- | :------- | :------: | :---------------- | :--------- |
| **SBOM-FSCT3-META-001**  | `fsct3-author-name`         | An SBOM should have an author name.                  | `error`  |    ❌    | Active            | §2.2.1.1   |
| **SBOM-FSCT3-META-002**  | `fsct3-timestamp`           | An SBOM should have a creation timestamp.            | `error`  |    ❌    | Active            | §2.2.1.2   |
| **SBOM-FSCT3-META-003**  | `fsct3-sbom-type`           | An SBOM should declare its type.                     | `note`   |    ❌    | Catalogue only ¹ | §2.2.1.3   |
| **SBOM-FSCT3-META-004**  | `fsct3-primary-component`   | An SBOM should identify a primary component.         | `error`  |    ❌    | Catalogue only ¹ | §2.2.1.4   |

### Component Attributes (§2.2.2)

| Rule ID           | Slug                         | Warning                                                              | Severity | Auto-Fix | Status            | Clause     |
| :---------------- | :--------------------------- | :------------------------------------------------------------------- | :------- | :------: | :---------------- | :--------- |
| **SBOM-FSCT3-COMP-001**  | `fsct3-component-name`        | An SBOM component should have a name.                                | `error`  |    ❌    | Active            | §2.2.2.1   |
| **SBOM-FSCT3-COMP-002**  | `fsct3-component-version`     | An SBOM component should have a version.                             | `error`  |    ❌    | Active            | §2.2.2.2   |
| **SBOM-FSCT3-COMP-003**  | `fsct3-supplier-name`         | An SBOM component should have a supplier name.                       | `error`  |    ❌    | Active            | §2.2.2.3   |
| **SBOM-FSCT3-COMP-004**  | `fsct3-unique-identifier`     | An SBOM component should have a unique identifier.                   | `error`  |    ❌    | Active            | §2.2.2.4   |
| **SBOM-FSCT3-COMP-005**  | `fsct3-cryptographic-hash`    | An SBOM component should have a cryptographic hash.                  | `error`  |    ❌    | Catalogue only ¹ | §2.2.2.5   |
| **SBOM-FSCT3-COMP-006**  | `fsct3-relationship`          | An SBOM component should declare its relationship and completeness.  | `error`  |    ❌    | Catalogue only ¹ | §2.2.2.6   |
| **SBOM-FSCT3-COMP-007**  | `fsct3-concluded-license`     | An SBOM component should have a concluded license.                   | `error`  |    ❌    | Active            | §2.2.2.7   |
| **SBOM-FSCT3-COMP-008**  | `fsct3-copyright-notice`      | An SBOM component should have a copyright notice.                    | `error`  |    ❌    | Active            | §2.2.2.8   |

`FSCT-UNDEC-*` namespace (§2.3 Undeclared SBOM Data) reserved for future
checks (unknown attributes, redacted components, unknown dependencies).

---

## Footnotes

¹ **Catalogue only** -- the rule appears in the SARIF `tool.driver.rules`
catalogue (so consumers can render the full standard surface) but the checker
does not yet emit results for it.  Either the spec attribute is aspirational
(Type, FSCT §2.2.1.3) or implementation is pending (Primary Component,
Cryptographic Hash, per-component Relationship).  Tracked for follow-up.

² *(reserved)*

³ **TBD** -- namespace and rule id are reserved.  The rule is **not** emitted
in the SARIF catalogue yet -- listing it here only fixes its future identifier
so that adding the check later does not require renumbering existing Active
or Catalogue-only rules.

---

## Auto-Fix legend

| Symbol             | Meaning                                                                |
| :----------------: | :--------------------------------------------------------------------- |
| ❌                  | Not auto-fixable.  SBOM repair requires upstream supplier action.     |
| 💡 *Suggestion*    | Tool can suggest the fix; user must apply.  *Reserved -- not used yet.* |
| 🔧 *Fixable*       | Tool can auto-rewrite the SBOM.  *Reserved -- not used yet.*           |

---

## Adding a new rule

1. Pick the `(SPEC, CATEGORY)` namespace.  Reserve a new category code if the
   rule comes from a section not yet covered.
2. Assign the next free `number` (rendered as `NNN`) within that namespace.
3. Add a row to the relevant table above with slug, warning, severity,
   auto-fix, status, and clause.  Follow the warning-text patterns from the
   "Warning text" section above so users get parallel wording across rules.
4. Add the corresponding `SpecRule` entry to
   `ntia_conformance_checker/rules/<spec>.yaml`, filling `slug`, `element_id`,
   `element_description`, `competency_question`, `warning`,
   `spec_clause_number`, `spec_clause_uri`, `sarif_name`, the `probe`, and
   (only if different) `oscal_control_id`.
5. Add or extend a fixture in `tests/data/` exercising the rule and assert it
   in `tests/test_output_sarif.py`.
