# Rule registry

This file is the single source of truth for every conformance rule emitted by
`ntia-conformance-checker`.  Each rule has a stable, machine-readable identifier
that appears in the tool's SARIF output (`reportingDescriptor.id`), in textual
reports, and — eventually — as the OSCAL control id when an OSCAL exporter
lands.

## Identifier scheme

```text
[SPEC]-[CATEGORY]-[NN]
```

| Segment    | Meaning                                                                                | Example  |
| :--------- | :------------------------------------------------------------------------------------- | :------- |
| `SPEC`     | Short uppercase identifier of the standard.                                            | `NTIA`   |
| `CATEGORY` | Short uppercase code matching a section heading within the spec (cluster / group).     | `DF`     |
| `NN`       | Zero-padded sequence number within `(SPEC, CATEGORY)`, in the order the spec lists it. | `01`     |

* The edition of a spec (FSCT 3rd edition, NTIA 2021, …) is **not** part of the
  identifier — it lives in `Spec.edition`.  If a future edition adds, renames,
  or removes an attribute, the rule id is appended or retired, not versioned.
* The rule id is also a valid OSCAL `control-id` token.  Where the eventual
  OSCAL convention diverges, an override is held in `SpecRule.oscal_control_id`.
* Each rule also stores the literal spec section number it derives from
  (`SpecRule.ref_section`, e.g. `2.2.2.7`) and a deep link
  (`SpecRule.ref_url`) so SARIF `helpUri` / OSCAL `link[rel="reference"]` can
  point at the exact clause.
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
in the `Status` column below — the current checker only validates Minimum
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

## NTIA — Minimum Elements for an SBOM (2021)

Source: *The Minimum Elements For a Software Bill of Materials (SBOM)*,
US Department of Commerce / NTIA, July 12 2021.
[NTIA report](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom)

### Data Fields (§IV)

The seven baseline data fields listed in the table on p.9.

| Rule ID         | Slug                            | Warning                                              | Severity | Auto-Fix | Status | Clause             |
| :-------------- | :------------------------------ | :--------------------------------------------------- | :------- | :------: | :----- | :----------------- |
| **NTIA-DF-01**  | `ntia-supplier-name`            | An SBOM component should have a supplier name.       | `error`  |    ❌    | Active | §IV (Supplier)     |
| **NTIA-DF-02**  | `ntia-component-name`           | An SBOM component should have a name.                | `error`  |    ❌    | Active | §IV (Name)         |
| **NTIA-DF-03**  | `ntia-component-version`        | An SBOM component should have a version.             | `error`  |    ❌    | Active | §IV (Version)      |
| **NTIA-DF-04**  | `ntia-unique-identifier`        | An SBOM component should have a unique identifier.   | `error`  |    ❌    | Active | §IV (Identifiers)  |
| **NTIA-DF-05**  | `ntia-dependency-relationship`  | An SBOM should declare dependency relationships.     | `error`  |    ❌    | Active | §IV (Dependencies) |
| **NTIA-DF-06**  | `ntia-sbom-author`              | An SBOM should have an author name.                  | `error`  |    ❌    | Active | §IV (Author)       |
| **NTIA-DF-07**  | `ntia-sbom-timestamp`           | An SBOM should have a creation timestamp.            | `error`  |    ❌    | Active | §IV (Timestamp)    |

### Automation Support (§IV, reserved)

Not yet implemented.  Reserved so future work can enable them without
re-numbering Active rules.

| Rule ID         | Slug                              | Warning                                              | Severity | Auto-Fix | Status | Clause          |
| :-------------- | :-------------------------------- | :--------------------------------------------------- | :------- | :------: | :----- | :-------------- |
| **NTIA-AS-01**  | `ntia-machine-readable-format`    | An SBOM should be machine-readable.                  | `error`  |    ❌    | TBD ³  | §IV (Automation) |

### Practices and Processes (§IV, reserved)

Process-level rules from the NTIA "Practices and Processes" subsection.  None
currently implemented — most require out-of-SBOM evidence (contracts,
distribution channels) and so will likely surface as `note`-level rules.

| Rule ID         | Slug                                | Warning                                                                  | Severity  | Auto-Fix | Status | Clause                |
| :-------------- | :---------------------------------- | :----------------------------------------------------------------------- | :-------- | :------: | :----- | :-------------------- |
| **NTIA-PP-01**  | `ntia-frequency`                    | An SBOM should be re-issued when the software is updated.                | `note`    |    ❌    | TBD ³  | §IV (Frequency)       |
| **NTIA-PP-02**  | `ntia-depth`                        | An SBOM should enumerate all top-level dependencies.                     | `warning` |    ❌    | TBD ³  | §IV (Depth)           |
| **NTIA-PP-03**  | `ntia-known-unknowns`               | An SBOM should distinguish missing data from declared "no value".        | `warning` |    ❌    | TBD ³  | §IV (Known Unknowns)  |
| **NTIA-PP-04**  | `ntia-distribution-delivery`        | An SBOM should be distributed in a timely manner.                        | `note`    |    ❌    | TBD ³  | §IV (Distribution)    |
| **NTIA-PP-05**  | `ntia-access-control`               | An SBOM should specify its access-control terms.                         | `note`    |    ❌    | TBD ³  | §IV (Access Control)  |
| **NTIA-PP-06**  | `ntia-accommodation-of-mistakes`    | An SBOM consumer should tolerate omissions and good-faith corrections.   | `note`    |    ❌    | TBD ³  | §IV (Mistakes)        |

---

## FSCT — Common SBOM (CISA 2024, Third Edition)

Source: *Framing Software Component Transparency: Establishing a Common
Software Bill of Materials (SBOM) Third Edition*, CISA Tooling and
Implementation Working Group, September 3 2024.
[CISA page](https://www.cisa.gov/resources-tools/resources/framing-software-component-transparency-2024)

Rule numbering matches the §2.2.x attribute order in the spec.  The third
"clause" segment of the spec section (the leaf number) is recorded
verbatim in `SpecRule.ref_section`.

### SBOM Meta-Information (§2.2.1)

| Rule ID           | Slug                       | Warning                                              | Severity | Auto-Fix | Status            | Clause     |
| :---------------- | :------------------------- | :--------------------------------------------------- | :------- | :------: | :---------------- | :--------- |
| **FSCT-META-01**  | `fsct-author-name`         | An SBOM should have an author name.                  | `error`  |    ❌    | Active            | §2.2.1.1   |
| **FSCT-META-02**  | `fsct-timestamp`           | An SBOM should have a creation timestamp.            | `error`  |    ❌    | Active            | §2.2.1.2   |
| **FSCT-META-03**  | `fsct-sbom-type`           | An SBOM should declare its type.                     | `note`   |    ❌    | Catalogue only ¹ | §2.2.1.3   |
| **FSCT-META-04**  | `fsct-primary-component`   | An SBOM should identify a primary component.         | `error`  |    ❌    | Catalogue only ¹ | §2.2.1.4   |

### Component Attributes (§2.2.2)

| Rule ID           | Slug                         | Warning                                                              | Severity | Auto-Fix | Status            | Clause     |
| :---------------- | :--------------------------- | :------------------------------------------------------------------- | :------- | :------: | :---------------- | :--------- |
| **FSCT-COMP-01**  | `fsct-component-name`        | An SBOM component should have a name.                                | `error`  |    ❌    | Active            | §2.2.2.1   |
| **FSCT-COMP-02**  | `fsct-component-version`     | An SBOM component should have a version.                             | `error`  |    ❌    | Active            | §2.2.2.2   |
| **FSCT-COMP-03**  | `fsct-supplier-name`         | An SBOM component should have a supplier name.                       | `error`  |    ❌    | Active            | §2.2.2.3   |
| **FSCT-COMP-04**  | `fsct-unique-identifier`     | An SBOM component should have a unique identifier.                   | `error`  |    ❌    | Active            | §2.2.2.4   |
| **FSCT-COMP-05**  | `fsct-cryptographic-hash`    | An SBOM component should have a cryptographic hash.                  | `error`  |    ❌    | Catalogue only ¹ | §2.2.2.5   |
| **FSCT-COMP-06**  | `fsct-relationship`          | An SBOM component should declare its relationship and completeness.  | `error`  |    ❌    | Catalogue only ¹ | §2.2.2.6   |
| **FSCT-COMP-07**  | `fsct-concluded-license`     | An SBOM component should have a concluded license.                   | `error`  |    ❌    | Active            | §2.2.2.7   |
| **FSCT-COMP-08**  | `fsct-copyright-notice`      | An SBOM component should have a copyright notice.                    | `error`  |    ❌    | Active            | §2.2.2.8   |

`FSCT-UNDEC-*` namespace (§2.3 Undeclared SBOM Data) reserved for future
checks (unknown attributes, redacted components, unknown dependencies).

---

## Footnotes

¹ **Catalogue only** — the rule appears in the SARIF `tool.driver.rules`
catalogue (so consumers can render the full standard surface) but the checker
does not yet emit results for it.  Either the spec attribute is aspirational
(Type, FSCT §2.2.1.3) or implementation is pending (Primary Component,
Cryptographic Hash, per-component Relationship).  Tracked for follow-up.

² *(reserved)*

³ **TBD** — namespace and rule id are reserved.  The rule is **not** emitted
in the SARIF catalogue yet — listing it here only fixes its future identifier
so that adding the check later does not require renumbering existing Active
or Catalogue-only rules.

---

## Auto-Fix legend

| Symbol             | Meaning                                                                |
| :----------------: | :--------------------------------------------------------------------- |
| ❌                  | Not auto-fixable.  SBOM repair requires upstream supplier action.     |
| 💡 *Suggestion*    | Tool can suggest the fix; user must apply.  *Reserved — not used yet.* |
| 🔧 *Fixable*       | Tool can auto-rewrite the SBOM.  *Reserved — not used yet.*           |

---

## Adding a new rule

1. Pick the `(SPEC, CATEGORY)` namespace.  Reserve a new category code if the
   rule comes from a section not yet covered.
2. Assign the next free `NN` within that namespace.
3. Add a row to the relevant table above with slug, warning, severity,
   auto-fix, status, and clause.  Follow the warning-text patterns from the
   "Warning text" section above so users get parallel wording across rules.
4. Add the corresponding `SpecRule` entry to
   `ntia_conformance_checker/<spec>_checker.py`, filling `slug`, `warning`,
   `ref_section`, `ref_url`, and (only if different) `oscal_control_id`.
5. Add or extend a fixture in `tests/data/` exercising the rule and assert it
   in `tests/test_output_sarif.py`.
