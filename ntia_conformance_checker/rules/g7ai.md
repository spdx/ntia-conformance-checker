---
SPDX-FileContributor: Arthit Suriyawongkul
SPDX-FileCopyrightText: 2026-present SPDX contributors
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: Apache-2.0
---

# G7 SBOM for AI: what is checked

`-c g7ai` checks an SPDX 3 SBOM against the
[G7 SBOM for AI: Minimum Elements][g7ai] (partial support).
The rules in [`g7ai.yaml`](g7ai.yaml) take their ids, provisions and
composition from the
[SBOM requirements ontology](https://bact.github.io/bom/req/g7ai2026/);
the SPDX fields follow its
[SPDX 3.0.1 mapping](https://bact.github.io/bom/mapping/g7ai2026-to-spdx30.sssom.tsv).

## How the result is reported

Each rule has one of four outcomes (`ruleResults` in the JSON output):

| Outcome | Meaning |
|---|---|
| `present` | The rule applies and the SBOM provides the element. |
| `missing` | The rule applies and the SBOM lacks the element. |
| `not-applicable` | The SBOM has nothing the rule applies to, such as no dataset for a dataset rule, or is not an SPDX 3 SBOM. |
| `out-of-scope` | The checker does not check the rule (see "Not checked" below). |

- Only `requirement` rules can make the SBOM non-conformant;
  `recommendation` rules are reported but do not block.
- If no rule applies, the SBOM is reported as non-conformant:
  nothing was checked.
- `clusterCompliance` gives the result per G7 cluster: `true`, `false`,
  or `null` if no rule of the cluster applies.

## Kinds of component

| Kind | What it is |
|---|---|
| `system` | Each root package the SBOM describes (an SBOM root expands to its root elements). No such package, or a non-package root: the rule fails. System-level properties are AI package properties, so the system must be an AI package. An SBOM or BOM root expands to its root elements. A model or dataset not reachable from the root is ignored when another of its kind is reachable; reachable means linked by `contains`, `dependsOn` or the like, or as the dataset a model was `trainedOn` or `testedOn`. |
| `ai_model` | An AI package whose purpose is `model` or unset. |
| `dataset` | A dataset package. |

An element with several SPDX properties is present if any of them is.

## Composite elements

A G7 element can have sub-elements (rule ids ending `.1`, `.2`, ...).
An *any of* element is present if any sub-element is present; the
sub-elements are reported on their own but do not block.
An element that is checked on its own evidence (`MDL-012`) is
independent of its sub-elements.

## Not checked

25 of 81 elements are not checked: SPDX 3.0.1 has no field for them (marked *gap* below), or their mapping is not yet reviewed (Infrastructure, Key Performance Indicators and some Security Properties elements).

## Metadata

| Rule id | Element | Provision | Checked as | SPDX 3.0.1 (match) | SPDX 3.1-dev, if different |
|---|---|---|---|---|---|
| `MD-001` | SBOM author | requirement | document has `author` | `createdBy` (exact) |  |
| `MD-002` | SBOM version (gap) | requirement | not checked | `amendedBy` (close) | `version` (exact) |
| `MD-003` | SBOM data format name | requirement | document has `spec_version` | `specVersion` (close) |  |
| `MD-004` | SBOM data format version | requirement | document has `spec_version` | `specVersion` (exact) |  |
| `MD-005` | SBOM author signature (gap) | requirement | not checked | `verifiedUsing` (narrow) |  |
| `MD-006` | SBOM tool name | requirement | document has `createdUsing` | `name` (exact) |  |
| `MD-007` | SBOM tool version (gap) | requirement | not checked | `name` (broad) | `version` (exact) |
| `MD-008` | SBOM generation context | requirement | document has `sbom_type` | `sbomType` (close) |  |
| `MD-009` | SBOM timestamp | requirement | document has `timestamp` | `created` (exact) |  |
| `MD-010` | SBOM dependency relationship | requirement | document has `dependency_relationship` | `dependsOn` (exact) |  |

## System Level Properties

| Rule id | Element | Provision | Checked as | SPDX 3.0.1 (match) | SPDX 3.1-dev, if different |
|---|---|---|---|---|---|
| `SLP-001` | System name | requirement | `system` has `name` | `name` (exact) |  |
| `SLP-002` | System components | requirement | `system` has `contains` or `dependsOn` | `contains`, `rootElement` (close) |  |
| `SLP-003` | System producer | requirement | `system` has `originatedBy` | `originatedBy` (exact) |  |
| `SLP-004` | System version | requirement | `system` has `software_packageVersion` | `packageVersion` (exact) | `version` (exact) |
| `SLP-005` | System timestamp | requirement | `system` has `builtTime` or `releaseTime` | `releaseTime`, `builtTime` (close) |  |
| `SLP-006` | System data flow (gap) | requirement | not checked | `informationAboutApplication` (broad) |  |
| `SLP-007` | System data usage | requirement | `system` has `ai_useSensitivePersonalInformation` | `useSensitivePersonalInformation` (close) |  |
| `SLP-008` | System input/output properties (gap) | requirement | any of its sub-elements | `informationAboutApplication` (broad) |  |
| `SLP-008.1` | System input modality (gap) | recommendation | not checked | `informationAboutApplication` (broad) |  |
| `SLP-008.2` | System output modality (gap) | recommendation | not checked | `informationAboutApplication` (broad) |  |
| `SLP-008.3` | System input preprocessing | recommendation | `system` has `ai_informationAboutApplication` | `informationAboutApplication` (close) |  |
| `SLP-009` | Intended application area | requirement | `system` has `ai_domain` | `domain` (close) |  |

## Models

| Rule id | Element | Provision | Checked as | SPDX 3.0.1 (match) | SPDX 3.1-dev, if different |
|---|---|---|---|---|---|
| `MDL-001` | Model name | requirement | `ai_model` has `name` | `name` (exact) |  |
| `MDL-002` | Model identifier | requirement | `ai_model` has `software_packageUrl` or `externalIdentifier` or `software_contentIdentifier` | `packageUrl` (exact) |  |
| `MDL-003` | Model version | requirement | `ai_model` has `software_packageVersion` | `packageVersion` (exact) | `version` (exact) |
| `MDL-004` | Model timestamp | requirement | `ai_model` has `builtTime` or `releaseTime` | `builtTime`, `releaseTime` (close) |  |
| `MDL-005` | Model producer | requirement | `ai_model` has `originatedBy` | `originatedBy` (exact) |  |
| `MDL-006` | Model description | requirement | any of its sub-elements | `description` (exact) |  |
| `MDL-006.1` | Model capability | recommendation | `ai_model` has `summary` | `summary` (close) |  |
| `MDL-006.2` | Model limitation | recommendation | `ai_model` has `ai_limitation` | `limitation` (exact) |  |
| `MDL-006.3` | Model lineage | recommendation | `ai_model` has `descendantOf` | `descendantOf` (exact) |  |
| `MDL-006.4` | Model intended use | recommendation | `ai_model` has `ai_informationAboutApplication` | `informationAboutApplication` (close) | `intendedUse` (exact) |
| `MDL-007` | Model hash value | requirement | `ai_model` has `verifiedUsing` | `hashValue` (exact) |  |
| `MDL-008` | Model hash algorithm | requirement | `ai_model` has `verifiedUsing` | `algorithm` (exact) |  |
| `MDL-009` | Model properties | requirement | any of its sub-elements | `typeOfModel`, `hyperparameter`, `autonomyType` (close) | `typeOfModel`, `hyperparameter`, `isoAutomationLevel` (close) |
| `MDL-009.1` | Model type | recommendation | `ai_model` has `ai_typeOfModel` | `typeOfModel` (close) |  |
| `MDL-009.2` | Model architecture (gap) | recommendation | not checked | `typeOfModel` (broad) |  |
| `MDL-009.3` | Model parameter count (gap) | recommendation | not checked | `hyperparameter` (broad) |  |
| `MDL-009.4` | Model hyperparameters | recommendation | `ai_model` has `ai_hyperparameter` | `hyperparameter` (exact) |  |
| `MDL-010` | Model input/output properties (gap) | requirement | any of its sub-elements | `informationAboutApplication` (broad) |  |
| `MDL-010.1` | Model input modality (gap) | recommendation | not checked | `informationAboutApplication` (broad) |  |
| `MDL-010.2` | Model output modality (gap) | recommendation | not checked | `informationAboutApplication` (broad) |  |
| `MDL-010.3` | Model context length (gap) | recommendation | not checked | `hyperparameter` (broad) |  |
| `MDL-010.4` | Model input preprocessing | recommendation | `ai_model` has `ai_informationAboutApplication` | `informationAboutApplication` (close) |  |
| `MDL-011` | Model training properties | requirement | any of its sub-elements | `informationAboutTraining`, `trainedOn`, `modelDataPreprocessing` (close) |  |
| `MDL-011.1` | Model learning type | recommendation | `ai_model` has `ai_typeOfModel` or `ai_informationAboutTraining` | `typeOfModel`, `informationAboutTraining` (close) |  |
| `MDL-011.2` | Model post-training technique (gap) | recommendation | not checked | `informationAboutTraining` (broad) |  |
| `MDL-012` | Model license | requirement | `ai_model` has `hasDeclaredLicense` | `hasDeclaredLicense` (exact) |  |
| `MDL-012.1` | Model openness category (gap) | recommendation | not checked | `hasDeclaredLicense` (related) |  |
| `MDL-013` | Model external references | requirement | `ai_model` has `externalRef` | `externalRef` (exact) |  |

## Dataset Properties

| Rule id | Element | Provision | Checked as | SPDX 3.0.1 (match) | SPDX 3.1-dev, if different |
|---|---|---|---|---|---|
| `DP-001` | Dataset name | requirement | `dataset` has `name` | `name` (exact) |  |
| `DP-002` | Dataset description | requirement | any of its sub-elements | `description` (close) |  |
| `DP-002.1` | Dataset lifecycle role | recommendation | `dataset` is the target of `trainedOn` or `testedOn` | `trainedOn` (narrow) |  |
| `DP-002.2` | Dataset availability | recommendation | `dataset` has `dataset_datasetAvailability` | `datasetAvailability` (exact) |  |
| `DP-002.3` | Dataset confidentiality level | recommendation | `dataset` has `dataset_confidentialityLevel` | `confidentialityLevel` (exact) |  |
| `DP-003` | Dataset content | requirement | any of its sub-elements | `datasetType` (narrow) |  |
| `DP-003.1` | Dataset domain (gap) | recommendation | not checked | `description` (broad) |  |
| `DP-003.2` | Dataset format (gap) | recommendation | not checked | `contentType` (close) |  |
| `DP-003.3` | Dataset modality | recommendation | `dataset` has `dataset_datasetType` | `datasetType` (exact) |  |
| `DP-004` | Dataset identifier | requirement | `dataset` has `software_packageUrl` or `externalIdentifier` or `software_contentIdentifier` | `packageUrl` (exact) |  |
| `DP-005` | Dataset hash | requirement | `dataset` has `verifiedUsing` | `verifiedUsing` (close) |  |
| `DP-006` | Dataset provenance | requirement | any of its sub-elements | `dataCollectionProcess`, `dataPreprocessing`, `originatedBy` (narrow) |  |
| `DP-006.1` | Dataset source | recommendation | `dataset` has `originatedBy` | `originatedBy` (close) |  |
| `DP-006.2` | Dataset collection method | recommendation | `dataset` has `dataset_dataCollectionProcess` | `dataCollectionProcess` (exact) |  |
| `DP-006.3` | Dataset preprocessing | recommendation | `dataset` has `dataset_dataPreprocessing` | `dataPreprocessing` (exact) |  |
| `DP-006.4` | Dataset synthetic data method (gap) | recommendation | not checked | `dataCollectionProcess` (broad) |  |
| `DP-007` | Dataset statistical properties | requirement | `dataset` has `dataset_datasetSize` or `dataset_knownBias` | `datasetSize`, `knownBias` (close) | `byteSize`, `knownBias` (close) |
| `DP-008` | Dataset sensitivity | requirement | any of its sub-elements | `hasSensitivePersonalInformation`, `confidentialityLevel` (narrow) |  |
| `DP-008.1` | Dataset personal information | recommendation | `dataset` has `dataset_hasSensitivePersonalInformation` or `dataset_anonymizationMethodUsed` | `hasSensitivePersonalInformation`, `anonymizationMethodUsed` (close) |  |
| `DP-008.2` | Dataset copyright status (gap) | recommendation | not checked | `copyrightText`, `hasDeclaredLicense` (related) |  |
| `DP-008.3` | Dataset sensitive data category (gap) | recommendation | not checked | `confidentialityLevel` (related) |  |
| `DP-009` | Dataset dependency relationship | requirement | `dataset` has `dependsOn` or `descendantOf` | `dependsOn`, `descendantOf` (close) |  |
| `DP-010` | Dataset license | requirement | `dataset` has `hasDeclaredLicense` | `hasDeclaredLicense` (exact) |  |

## Infrastructure

| Rule id | Element | Provision | Checked as | SPDX 3.0.1 (match) | SPDX 3.1-dev, if different |
|---|---|---|---|---|---|
| `INF-001` | Infrastructure software | requirement | not checked | `Package`, `dependsOn` (close) |  |
| `INF-002` | Infrastructure hardware (gap) | requirement | not checked | `comment` (broad) | `Hardware` (exact) |

## Security Properties

| Rule id | Element | Provision | Checked as | SPDX 3.0.1 (match) | SPDX 3.1-dev, if different |
|---|---|---|---|---|---|
| `SP-001` | Security controls (gap) | requirement | not checked | `externalRef` (broad) |  |
| `SP-002` | Security compliance | requirement | `system` has `ai_standardCompliance` | `standardCompliance` (exact) | `conformsTo` (exact) |
| `SP-003` | Cybersecurity policy information | requirement | not checked | `ExternalRefType/securityPolicy` (close) | `ExternalRefType/securityPolicy`, `hasContactPoint`, `ContactType/securityVulnerability` (close) |
| `SP-004` | Vulnerability referencing | requirement | not checked | `Vulnerability`, `VexAffectedVulnAssessmentRelationship`, `ExternalRefType/securityAdvisory` (close) |  |

## Key Performance Indicators

| Rule id | Element | Provision | Checked as | SPDX 3.0.1 (match) | SPDX 3.1-dev, if different |
|---|---|---|---|---|---|
| `KPI-001` | Security metrics | requirement | not checked | `metric` (close) |  |
| `KPI-002` | Operational performance KPIs | requirement | not checked | `metric` (close) |  |

[g7ai]: https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/SBOM-for-AI_minimum-elements.pdf
