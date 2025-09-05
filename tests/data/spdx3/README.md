# SPDX 3 example files used in tests

| Filename | Test-related characteristic | Adapted from source |
|-|-|-|
| [has_no_sbom.json](./has_no_sbom.json) | Has neither `/Core/Bom` nor `/Software/Sbom`. | [software/example1](https://github.com/spdx/spdx-examples/tree/master/software/example1) in spdx-examples. |
| [has_sbom.json](./has_sbom.json) | Has `/Software/Sbom` | [software/example13](https://github.com/spdx/spdx-examples/tree/master/software/example13) in spdx-examples.|
| [no_elements_missing.json](./no_elements_missing.json) | No elements are missing. Note that the SBOM has no `/Software/Package`, but as the SBOM has its subclass `/Dataset/DatasetPackage` it should be treated as a regular SBOM. | [dataset/example01](https://github.com/spdx/spdx-examples/tree/master/dataset/example01) in spdx-examples. |
| [missing_supplier_name.json](./missing_supplier_name.json) | Missing `suppliedBy` property in the `/Dataset/DatasetPackage`. | no_elements_missing.json with `suppliedBy` removed. |
| [missing_version.json](./missing_version.json) | Missing `packageVersion` in the `/Dataset/DatasetPackage`. | no_elements_missing.json with `packageVersion` removed. |
| [missing_unique_identifiers.json](./missing_unique_identifiers.json) | Missing `spdxId` property in the "data.csv" `/Software/File`. | no_elements_missing.json with `spdxId` removed. |
