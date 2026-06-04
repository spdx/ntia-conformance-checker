---
SPDX-FileCopyrightText: 2026-present SPDX contributors
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: Apache-2.0
---

# Declarative rule files

- Each `*.yaml` in this directory defines one compliance standard loaded by
  `RuleBasedChecker` at import time;
  - dropping a new `<spec_id>.yaml` here is all that is needed to add
    a standard.
- Files prefixed with `_` (e.g. [`_example.yaml`](_example.yaml)) are skipped
  by the registry and not shipped.
- For full details -- architecture, field reference, rule ids,
  conformance model, probe registry, and the rule catalogue --
  see [`../../RULES.md`](../../RULES.md).
