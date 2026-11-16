# Frequently asked questions

**Q: I am having trouble installing the Python modules. What gives?**

A: It could be due to using an OS package manager (like `apt`) to install
modules rather than using `pip`. Please try using `pip`.

**Q: Why does my SPDX 3 SBOM fail the BSI compliance check for "deployable form
URIs" when I copied the example from the BSI document?**

A: The BSI TR-03183-2 document contains an example where `binaryArtifact` is
used as a direct property on a file. However, the official SPDX 3.0.1
specification strictly defines `binaryArtifact` as an `ExternalRefType`.
To pass compliance, you must define it inside an `externalRef` array.

**Q: I am getting a "NotImplementedError: software_SoftwareArtifact is abstract
and cannot be implemented" when parsing my SPDX 3 SBOM. How do I fix this?**

A: You are likely using `software_SoftwareArtifact` as the `"type"` for
an element in your JSON-LD file (which is sometimes shown in BSI examples for
Source Code URIs). Because it is an abstract class in the SPDX model,
it cannot be instantiated directly. You must change the type to a concrete
subclass, such as `software_File`, `software_Package`, or `software_Snippet`.

**Q: The CLI output warns me that it "Found X disconnected 'floating'
components." What does this mean?**

A: The checker walks the relationship graph from the root elements. A
floating component is a package that no root reaches. It is ignored for
compliance, but it often means the SBOM generator left unlinked data in the
file. Only packages, the components that minimum elements apply to, are
reported as floating.

**Q: Which relationships connect an element to the tree?**

A: The checker follows relationships from parent to child only. In SPDX 2,
`A <type> B` is `spdxElementId` A to `relatedSpdxElement` B; in SPDX 3, it is
`from` A to `to` B. A forward type is followed from A to B, a reverse type
from B to A. Element types at either end are not restricted
([SPDX 2.3][spdx-2.3] clause 11.1.1).

Roots:

- SPDX 2: `SPDXRef-DOCUMENT DESCRIBES A` or `A DESCRIBED_BY SPDXRef-DOCUMENT`
  (clause 11.1, Table 68). `SPDXRef-DOCUMENT` is accepted even if the
  document has another ID (clause 6.3).
- SPDX 3: the `rootElement` of the `SpdxDocument`, and the `to` elements of
  any relationship from it. Each collection, such as an `Sbom`, also links to
  its own `rootElement`.

Followed relationships:

<!-- markdownlint-disable MD013 -->

| SPDX 3 type | SPDX 2 forward | SPDX 2 reverse | Parent to child |
| --- | --- | --- | --- |
| `contains` | `CONTAINS` | `CONTAINED_BY` | Whole to part |
| `hasOptionalComponent` | | `OPTIONAL_COMPONENT_OF` | Whole to part |
| `packagedBy` | | `PACKAGE_OF` | Element to its package |
| `dependsOn` | `DEPENDS_ON` | `DEPENDENCY_OF`, `BUILD_`, `DEV_`, `RUNTIME_`, `TEST_DEPENDENCY_OF` | Dependent to dependency |
| `hasOptionalDependency` | | `OPTIONAL_DEPENDENCY_OF` | Dependent to dependency |
| `hasProvidedDependency` | | `PROVIDED_DEPENDENCY_OF` | Dependent to dependency |
| `hasPrerequisite` | `HAS_PREREQUISITE` | `PREREQUISITE_FOR` | Dependent to prerequisite |
| `hasDynamicLink` | `DYNAMIC_LINK` | | Linker to linked |
| `hasStaticLink` | `STATIC_LINK` | | Linker to linked |
| `usesTool` | | `BUILD_TOOL_OF`, `DEV_TOOL_OF`, `TEST_TOOL_OF` | Product to tool |
| `generates` (reverse) | `GENERATED_FROM` | `GENERATES` | Product to source |
| (SPDX 2 only) | `DESCRIBES` | `DESCRIBED_BY` | Describer to described |

<!-- markdownlint-enable MD013 -->

All SPDX 3 types are forward except `generates`: "The `from` Element
generates each `to` Element", and the checker goes from the product (`to`) to
its source (`from`), as it goes from a product to its tool. Other types, such
as `DESCENDANT_OF`, `FILE_MODIFIED`, `OTHER` or `hasDataFile`, are not
followed.

SPDX 2.3 does not say which end of a relationship is the parent. The checker
derives each SPDX 2 type from its SPDX 3 translation in the
[SPDX 3.0 Annex A.1 table][spdx-3.0-a1]: same direction, reversed when the
table says "Swap to and from? Y". For example, `A BUILD_DEPENDENCY_OF B`
translates to `B dependsOn A`, so the checker goes from B to A. Two overrides:

- `DESCRIBES` and `DESCRIBED_BY` are followed between any elements in SPDX 2.
  SPDX 3 marks roots with `rootElement` instead, so `describes` is not
  followed there.
- `DYNAMIC_LINK` is forward. Annex A.1 marks it as swapped, but Table 68 ("A
  dynamically links to B") and [SPDX 3.0.1][spdx-3.0.1-reltype]
  `hasDynamicLink` ("The `from` Element dynamically links in each `to`
  Element") read the same way. The `FILE_MODIFIED` row has the opposite
  error; it is not followed. Both rows are corrected in
  [spdx/using#30][spdx-using-30].

**Q: The CLI output reports that a relationship points to a missing element.
What does this mean?**

A: A root, or a followed relationship, refers to an element that the SBOM does
not define. Both ends are checked, in SPDX 2 and SPDX 3. Each link is
reported once, as written, with each end labeled:

<!-- markdownlint-disable MD013 -->

| Case | Report line |
| --- | --- |
| `A <type> B`, B missing | `Element 'A' links to missing element 'B'` |
| `A <type> B`, A missing | `Missing element 'A' links to element 'B'` |
| `A <type> B`, both missing | `Missing element 'A' links to missing element 'B'` |
| Root missing | `Element '<document or collection>' links to missing element '<root>'` |

<!-- markdownlint-enable MD013 -->

The JSON output lists every missing ID in
`graphValidation.unknownPointers.missingElementIds`.

Not missing:

- `NONE` and `NOASSERTION` (SPDX 2.3 Table 69), and SPDX 3 individuals such
  as `NoneElement`. The other end of such a relationship is still checked.
- An SPDX 2 element in another document, written
  `DocumentRef-<id>:SPDXRef-<idstring>` (Table 69), when `DocumentRef-<id>`
  is declared in an `ExternalDocumentRef` (clause 6.6). The external document
  itself is `DocumentRef-<id>:SPDXRef-DOCUMENT` (clause 6.3.1). An undeclared
  prefix, a bare `DocumentRef-<id>` or any other form is missing.
- An SPDX 3 element in the `externalSpdxId` of an `ExternalMap` in an
  `import`.

The checker does not fetch external documents; it trusts the declaration.
External elements are neither checked for conformance nor reported as
floating.

[spdx-2.3]: https://spdx.github.io/spdx-spec/v2.3.1/
[spdx-3.0-a1]: https://github.com/spdx/using/blob/10e4b14c9cc5642aa4b4ce629e2b0560b771cf34/docs/diffs-from-previous-editions.md
[spdx-3.0.1-reltype]: https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Vocabularies/RelationshipType/
[spdx-using-30]: https://github.com/spdx/using/pull/30
