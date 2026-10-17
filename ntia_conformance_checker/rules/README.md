---
SPDX-FileContributor: Arthit Suriyawongkul
SPDX-FileCopyrightText: 2026-present SPDX contributors
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: Apache-2.0
---

# Declarative rule files

- Each `*.yaml` in this directory defines one compliance standard loaded by
  `registry.py` at import time;
  - dropping a new `<spec_id>.yaml` here is all that is needed to add
    a standard.
- [`g7ai.md`](g7ai.md) lists what the G7 SBOM for AI rules check.
- Files prefixed with `_` (e.g. [`_example.yaml`](_example.yaml)) are skipped
  by the registry and not shipped.
