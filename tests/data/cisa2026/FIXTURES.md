---
SPDX-FileCopyrightText: 2026 SPDX contributors
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: Apache-2.0
---

# CISA 2026 Minimum Elements test fixtures

Input files for issue #305. They cover three areas that the 2026 edition adds
or changes: SBOM tool name and version, component producer, and component
hash. They are data only. No rule, adapter or test code is included, and
**no file carries an expected pass/fail verdict for the 2026 rules**, because
those rules are not decided yet.

Source of every quote below: CISA et al., *2026 Minimum Elements for a
Software Bill of Materials (SBOM)*, v2.1, July 29, 2026
(`refs/2026-sbom-minimum-elements.pdf`). Page numbers are the printed
"Page N of 23" numbers.

## Design

- Each format has one **baseline** file. Every other file is the baseline with
  exactly one change, so `diff baseline_<fmt>.json <variant>_<fmt>.json` shows
  the single field under test (plus the document name and namespace).
- Three fictional packages: `example-app` 2.1.0 (the described root), which
  depends on `example-json-parser` 1.8.3 and `example-tls-library` 3.2.1.
- Component-level variants change **only** `example-json-parser`
  (`SPDXRef-Package-example-json-parser` in SPDX 2;
  `.../Package-example-json-parser` in SPDX 3). The other two packages keep
  the field.
- `example-json-parser` has a supplier ("Example Distribution Vendor") that
  differs from its originator ("Example Parser Project"), so a test can tell
  which field a rule read.
- Checksum values are well-formed SHA-256 digests of the placeholder string
  `<name>@<version>`. The packages do not exist; the digests are not digests of
  any real artifact.

## Files

| File | What it contains | CISA 2026 element exercised | What it deliberately does not assert |
|-|-|-|-|
| `baseline_spdx2.json` | SPDX 2.3 JSON. Creators `Organization: Example Software Company` and `Tool: ExampleSbomGenerator-1.4.2`; creator comment `Build`; three packages, each with `versionInfo`, `supplier`, `originator`, one `SHA256` entry in `checksums`, `licenseConcluded`, `licenseDeclared`, a purl in `externalRefs`; one `DESCRIBES` and two `DEPENDS_ON` relationships. | The "present" case for all three areas below. | Not claimed to be fully conformant to CISA 2026. SBOM Author Signature (p. 8) is absent: SPDX 2.3.1 Annex L.2.2 says SPDX 2.3.1 has no field for it. |
| `sbom_tool_absent_spdx2.json` | Baseline with the `Tool:` creator removed. The `Organization:` creator remains. | Data Fields > SBOM Metadata > "SBOM Tool Name" (New), p. 9: "The name of the tool used by the SBOM author to generate or amend the SBOM." Also "SBOM Tool Version" (New), p. 10. | Whether a missing tool is a failure or an advisory finding (the document says "should" throughout). |
| `sbom_tool_version_absent_spdx2.json` | Baseline with the tool creator changed to `Tool: ExampleSbomGenerator` (name, no `-version` part). | Data Fields > SBOM Metadata > "SBOM Tool Version" (New), p. 10: "Identifier for the version of the tool identified in the SBOM Tool Name element." and "If no version identifier is available, the SBOM author should indicate that the information is unknown." | This is a **missing** version, not an "explicitly unknown" one. How a rule splits name from version in a `Tool:` entry is left open. |
| `component_producer_absent_spdx2.json` | Baseline with `originator` removed from `example-json-parser`. Its `supplier` is still present and names a different organization. | Data Fields > Component Data > "Component Producer" (Major Update), p. 10: "The name of an entity that creates, defines, and identifies components." | Open question (a): whether producer falls back to `supplier`. With a fallback this package has a producer; without one it does not. The file takes no side. |
| `component_producer_noassertion_spdx2.json` | Baseline with `"originator": "NOASSERTION"` on `example-json-parser`. Its `supplier` is still present. | Same element, p. 11: "If there is no clear indication of component producer, the SBOM author should explicitly indicate that the component is of unknown provenance to acknowledge the lack of traceability." Also Practices and Processes > "Explicitly Identifying Unknown Information" (Major Update), pp. 13-14. | Open question (b): whether `NOASSERTION` is an acceptable explicit unknown. Also (a): whether a fallback to `supplier` applies when `originator` is `NOASSERTION`. |
| `component_hash_absent_spdx2.json` | Baseline with `checksums` removed from `example-json-parser`. | Data Fields > Component Data > "Component Hash Value" (New), p. 11: "The output generated from applying a cryptographic hash algorithm to an executable component artifact." Also "Component Hash Algorithm" (New), pp. 11-12: "The cryptographic algorithm used to compute the Component Hash Value of the software component." | Which algorithms are acceptable; whether a package-level checksum satisfies "executable component artifact"; failure versus advisory. |
| `baseline_spdx3.json` | SPDX 3.0.1 JSON-LD equivalent of the baseline: `CreationInfo` with `createdBy` (an `Organization`) and `createdUsing` (a `Tool` named `ExampleSbomGenerator`); `software_Sbom` with `software_sbomType` `build`; three `software_Package` elements with `suppliedBy`, `originatedBy`, `verifiedUsing` (a `Hash`, `sha256`), `software_packageUrl`; `hasConcludedLicense` and `dependsOn` relationships. | The "present" case for the three SPDX 3 variants. | **Tool version is not present**: the SPDX 3.0.1 model defines no version property on `Tool`, and this file does not invent a convention for it. |
| `sbom_tool_absent_spdx3.json` | SPDX 3 baseline with `createdUsing` and the `Tool` element removed. | "SBOM Tool Name" (New), p. 9 (quoted above). | Same as the SPDX 2 file. |
| `component_producer_absent_spdx3.json` | SPDX 3 baseline with `originatedBy` removed from `example-json-parser`. `suppliedBy` is still present and points to a different organization. | "Component Producer" (Major Update), p. 10 (quoted above). | Open question (a), as for the SPDX 2 file. |
| `component_hash_absent_spdx3.json` | SPDX 3 baseline with `verifiedUsing` removed from `example-json-parser`. | "Component Hash Value" and "Component Hash Algorithm" (New), pp. 11-12 (quoted above). | Whether the hash belongs on the package or on a distribution artifact file (the BSI fixtures in `tests/data/bsi/` use the latter). |

Open question (c), sequencing with the planned `RuleBasedChecker`: the files
are plain inputs and do not depend on any checker class, rule file or adapter
method, so they can be used whichever order the work lands in.

## Cases that are intentionally missing

These "explicitly unknown" files were not created, because the format has no
defined way to say it. Forcing one would have meant inventing a convention.

| Case | Why there is no file |
|-|-|
| SBOM tool unknown, SPDX 2.3 | SPDX 2.3.1 §6.8 "Creator field" defines three forms (`Person:`, `Organization:`, `Tool: toolidentifier-version`) and no `NOASSERTION`. spdx-tools 0.8.5 refuses to parse a bare `NOASSERTION` creator. `Tool: NOASSERTION` parses, but only as a tool literally named "NOASSERTION". |
| Component hash unknown, SPDX 2.3 | SPDX 2.3.1 §7.10 "Package checksum field" defines an algorithm plus lowercase hexadecimal digits and no `NOASSERTION`. spdx-tools 0.8.5 reports a validation error for `"checksumValue": "NOASSERTION"`. |
| Component producer unknown, SPDX 3.0.1 | `originatedBy` has range `Agent` in `refs/spdx/spdx-model-3.0.1.ttl`. `NoAssertionElement` is an `IndividualElement`, not an `Agent`; pointing `originatedBy` at it fails SHACL validation ("Value does not have class ns1:Agent"). |
| SBOM tool version, SPDX 3.0.1 | The model file defines `Tool` as a subclass of `Element` with no version property. |
| Component hash unknown, SPDX 3.0.1 | `Hash` requires `hashValue` (a string). No "unknown" value is defined for it. |

## Format mapping used

SPDX 2.3 field choices follow SPDX 2.3.1 Annex L.2.2 "Mapping 2026 CISA
Minimum Elements to SPDX fields" (informative): SBOM Tool Name and Version to
(6.8) Creator, Tool entry; Component Producer to (7.6) Package Originator;
Component Hash Value and Algorithm to (7.10) Package Checksum. SPDX 3.0.1
property names (`createdUsing`, `originatedBy`, `suppliedBy`, `verifiedUsing`)
are taken from `refs/spdx/spdx-model-3.0.1.ttl`. No official CISA 2026 to
SPDX 3 mapping was found; the SPDX 3 choices are the nearest properties in
the model, not a cited mapping.

## How the files were checked

- SPDX 2: parsed with spdx-tools 0.8.5 (`parse_file`) and validated with
  `validate_full_spdx_document`: 0 messages for all six files.
- SPDX 3: parsed with the repository's `parse_spdx3_file` and
  `validate_spdx3_data` (0 messages), and validated with pyshacl 0.40.2
  against `refs/spdx/spdx-model-3.0.1.ttl` (all four conform).
- Existing checker: `sbomcheck -c ntia` reports all ten files conformant.
  Within a format, the `ntia`, `fsct3-min` and `bsi` reports are identical for
  the baseline and every variant, which is expected: none of the three
  existing standards checks the fields these files vary.
