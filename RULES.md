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
| `SPEC`     | `Spec.spec_id` uppercased (hyphen-free, uppercase-safe token).                          | `FSCT3`  |
| `CATEGORY` | Short uppercase code of a category within the spec (`SpecCategory.code`).               | `DF`     |
| `NNN`      | Zero-padded (3-digit) sequence within `(SPEC, CATEGORY)`, in the order the spec lists.  | `001`    |

* The id is derived (`Spec.rule_id`), never stored in the YAML, so it cannot
  drift from `spec_id` / `category.code` / `number`.
* The **edition is part of the `SPEC` segment** (`fsct3` → `FSCT3`), because each
  edition is a distinct standard with its own requirements.  A later edition
  (`fsct4` → `FSCT4`) therefore gets its own rule-id namespace, so rules never
  collide across editions.
* The lowercased rule id is also a valid OSCAL `control-id` token.  Where the
  eventual OSCAL convention diverges, an override is held in
  `SpecRule.oscal_control_id`.
* Each rule also stores the literal spec clause number it derives from
  (`SpecRule.spec_clause_number`, e.g. `2.2.2.7`) and a deep link
  (`SpecRule.spec_clause_url`) so SARIF `helpUri` / OSCAL `link[rel="reference"]`
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

## Severity

| Maturity level (FSCT) / criticality (NTIA) | Default SARIF level |
| :----------------------------------------- | :------------------ |
| Minimum Expected / Required                | `error`             |
| Recommended Practice                       | `warning`           |
| Aspirational Goal                          | `note`              |

A rule emitted only at higher maturity is included in the catalogue but flagged
in the `Status` column below -- the current checker only validates Minimum
Expected.

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
| **SBOM-FSCT3-META-001**  | `fsct-author-name`         | An SBOM should have an author name.                  | `error`  |    ❌    | Active            | §2.2.1.1   |
| **SBOM-FSCT3-META-002**  | `fsct-timestamp`           | An SBOM should have a creation timestamp.            | `error`  |    ❌    | Active            | §2.2.1.2   |
| **SBOM-FSCT3-META-003**  | `fsct-sbom-type`           | An SBOM should declare its type.                     | `note`   |    ❌    | Catalogue only ¹ | §2.2.1.3   |
| **SBOM-FSCT3-META-004**  | `fsct-primary-component`   | An SBOM should identify a primary component.         | `error`  |    ❌    | Catalogue only ¹ | §2.2.1.4   |

### Component Attributes (§2.2.2)

| Rule ID           | Slug                         | Warning                                                              | Severity | Auto-Fix | Status            | Clause     |
| :---------------- | :--------------------------- | :------------------------------------------------------------------- | :------- | :------: | :---------------- | :--------- |
| **SBOM-FSCT3-COMP-001**  | `fsct-component-name`        | An SBOM component should have a name.                                | `error`  |    ❌    | Active            | §2.2.2.1   |
| **SBOM-FSCT3-COMP-002**  | `fsct-component-version`     | An SBOM component should have a version.                             | `error`  |    ❌    | Active            | §2.2.2.2   |
| **SBOM-FSCT3-COMP-003**  | `fsct-supplier-name`         | An SBOM component should have a supplier name.                       | `error`  |    ❌    | Active            | §2.2.2.3   |
| **SBOM-FSCT3-COMP-004**  | `fsct-unique-identifier`     | An SBOM component should have a unique identifier.                   | `error`  |    ❌    | Active            | §2.2.2.4   |
| **SBOM-FSCT3-COMP-005**  | `fsct-cryptographic-hash`    | An SBOM component should have a cryptographic hash.                  | `error`  |    ❌    | Catalogue only ¹ | §2.2.2.5   |
| **SBOM-FSCT3-COMP-006**  | `fsct-relationship`          | An SBOM component should declare its relationship and completeness.  | `error`  |    ❌    | Catalogue only ¹ | §2.2.2.6   |
| **SBOM-FSCT3-COMP-007**  | `fsct-concluded-license`     | An SBOM component should have a concluded license.                   | `error`  |    ❌    | Active            | §2.2.2.7   |
| **SBOM-FSCT3-COMP-008**  | `fsct-copyright-notice`      | An SBOM component should have a copyright notice.                    | `error`  |    ❌    | Active            | §2.2.2.8   |

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
   `spec_clause_number`, `spec_clause_url`, `sarif_name`, the `probe`, and
   (only if different) `oscal_control_id`.
5. Add or extend a fixture in `tests/data/` exercising the rule and assert it
   in `tests/test_output_sarif.py`.
