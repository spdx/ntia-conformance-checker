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

A: A floating component is a package that no root reaches when the checker
walks the relationship graph. It is ignored for compliance, but often means
the SBOM generator left unlinked data. Only packages, the components that
minimum elements apply to, are reported as floating.

**Q: Which relationships connect an element to the tree?**

A: The graph shape is what the SBOM states; the traversal is how the checker
walks it.

*Graph shape.* `A <type> B` is written from A to B: SPDX 2 `spdxElementId` to
`relatedSpdxElement`, SPDX 3 `from` to `to`. Either end can be any element
type ([SPDX 2.3][spdx-2.3] §11.1.1). SPDX 2 also has reverse types, written
from the child's side, such as `CONTAINED_BY` (§11.1 Table 68); SPDX 3 has
none. Missing elements are checked on the graph shape (next question).

*Traversal.* From the roots, the checker goes from parent to child, walking
each followed type along its written direction (A to B) or against it (B to
A). "None" and "no assertion" values (SPDX 2 `NONE`, `NOASSERTION`; SPDX 3
`NoneElement`, `NoAssertionElement`, `NoneLicense`, `NoAssertionLicense`)
are never walked through; `SpdxOrganization` is.

Roots:

- SPDX 2: `SPDXRef-DOCUMENT DESCRIBES A` or `A DESCRIBED_BY SPDXRef-DOCUMENT`
  (§11.1 Table 68); `SPDXRef-DOCUMENT` is accepted even if the document has
  another ID (§6.3).
- SPDX 3: the `SpdxDocument` `rootElement` and the `to` of any relationship
  from it; each collection, such as an `Sbom`, also links to its
  `rootElement`.

Followed relationships:

<!-- markdownlint-disable MD013 -->

| SPDX 3 type | SPDX 2, walked A to B | SPDX 2, walked B to A | Parent to child | Dependency |
| --- | --- | --- | --- | --- |
| `contains` | `CONTAINS` | `CONTAINED_BY` | Whole to part | ✓ |
| `hasOptionalComponent` | | `OPTIONAL_COMPONENT_OF` | Whole to part | |
| `packagedBy` | | `PACKAGE_OF` | Element to its package | |
| `dependsOn` | `DEPENDS_ON` | `DEPENDENCY_OF`, `BUILD_`, `DEV_`, `RUNTIME_`, `TEST_DEPENDENCY_OF` | Dependent to dependency | ✓ |
| `hasOptionalDependency` | | `OPTIONAL_DEPENDENCY_OF` | Dependent to dependency | ✓ |
| `hasProvidedDependency` | | `PROVIDED_DEPENDENCY_OF` | Dependent to dependency | ✓ |
| `hasPrerequisite` | `HAS_PREREQUISITE` | `PREREQUISITE_FOR` | Dependent to prerequisite | ✓ |
| `hasDynamicLink` | `DYNAMIC_LINK` | | Linker to linked | ✓ |
| `hasStaticLink` | `STATIC_LINK` | | Linker to linked | ✓ |
| `trainedOn`, `testedOn` | | | Model to dataset | |
| `usesTool` | | `BUILD_TOOL_OF`, `DEV_TOOL_OF`, `TEST_TOOL_OF` | Product to tool | |
| `generates` (walked B to A) | `GENERATED_FROM` | `GENERATES` | Product to source | |
| (SPDX 2 only) | `DESCRIBES` | `DESCRIBED_BY` | Describer to described | |

<!-- markdownlint-enable MD013 -->

Tools and sources are inputs of a product, so the checker goes from the
product to them, as from a dependent to its dependencies. SPDX 3 writes
`usesTool` from the product ("The `from` Element uses each `to` Element as a
tool") but `generates` from the source ("The `from` Element generates each
`to` Element"; [SPDX 3.0.1][spdx-3.0.1-reltype] `RelationshipType`), so
`generates` is walked against its written direction. It is not a reverse
type, and not walked both ways, or a shared source would link its products.
Following tools and sources is our reading: NTIA 2021 (IV. Minimum Elements >
Data Fields > Dependency Relationship) relates a component "included in"
software, CISA 2026 (Data Fields > Component Data > Component Dependency
Relationship) one "necessary for the operation" of another.

Other types, such as `DESCENDANT_OF`, `FILE_MODIFIED`, `OTHER` or
`hasDataFile`, are not followed.

SPDX 2.3 does not say which end is the parent, so each SPDX 2 type follows
its SPDX 3 translation in the [2.3 to 3.0 translation table][spdx-2.3-to-3.0]
(Using SPDX; formerly SPDX 3.0 Annex A.1), walked the other way when the
table says "Swap to and from? Y". For example, `A BUILD_DEPENDENCY_OF B` is
`B dependsOn A`, so the checker goes from B to A. The one override:
`DESCRIBES` and `DESCRIBED_BY` are followed between any SPDX 2 elements;
SPDX 3 marks roots with `rootElement` instead.

**Q: How does the checker decide "Dependency relationships provided?"?**

A: A reachable component must declare a relationship of a type marked
"Dependency" in the table above, in either SPDX 2 form. Its other end must be
another element that exists (here, or in a declared external or imported
document), or "none" or "no assertion" (SPDX 2 `NONE`, `NOASSERTION`; SPDX 3
`NoneElement`, `NoAssertionElement`). Documents and collections, such as an
`Sbom`, are not components, so `SPDXRef-DOCUMENT DESCRIBES A` alone does not
count. The rule is the same for SPDX 2 and SPDX 3.

This follows NTIA 2021: the Dependency Relationship relates components ("an
upstream component X is included in software Y"; IV. Minimum Elements > Data
Fields > Dependency Relationship), and the author "should affirmatively state
... when a component has no further dependencies", which "is implemented in
the dependency relationship data field" (IV. Minimum Elements > Practices and
Processes > Known Unknowns). So `A DEPENDS_ON NONE` counts. SPDX 2.3.1
Annex L.1.2, which is informative, maps the element to `CONTAINS` and
`DESCRIBES`; the checker is stricter and does not accept `DESCRIBES` alone.

Tools, sources and training data are followed but are not dependency
relationships: they are inputs, not included components.

**Q: The CLI output reports that a relationship points to a missing element.
What does this mean?**

A: A root or a followed relationship refers to an element that the SBOM does
not define. Both ends are checked as written, however the checker walks the
relationship, and each relationship is reported once:

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

- `NONE` and `NOASSERTION` (SPDX 2.3 Table 69) and SPDX 3 individuals such as
  `NoneElement` or `SpdxOrganization`; the other end is still checked.
- An SPDX 2 element in another document, `DocumentRef-<id>:SPDXRef-<idstring>`
  (Table 69), when `DocumentRef-<id>` is declared in an `ExternalDocumentRef`
  (§6.6). The document itself is `DocumentRef-<id>:SPDXRef-DOCUMENT` (§6.3.1).
  An undeclared prefix, a bare `DocumentRef-<id>` or any other form is
  missing.
- An SPDX 3 element in the `externalSpdxId` of an `ExternalMap` in an
  `import`.

External documents are not fetched; the declaration is trusted. External
elements are neither checked for conformance nor reported as floating.

[spdx-2.3]: https://spdx.github.io/spdx-spec/v2.3.1/
[spdx-2.3-to-3.0]: https://github.com/spdx/using/blob/80eba34d23f48e242a54a78b584e7a87ad2b9afa/docs/diff/v2.3-v3.0.md#translating-from-23-to-30-8
[spdx-3.0.1-reltype]: https://spdx.github.io/spdx-spec/v3.0.1/model/Core/Vocabularies/RelationshipType/
