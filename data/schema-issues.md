# Schema Issues Discovered During Hand Conversion

**Date:** 2026-05-27
**Task:** Hand-convert 5 nodes to JSON-LD per-entity files
**Nodes:** foundations, foundations.fire, metals.iron-steel, silicon.mg-si-production, metals.aluminum

---

## Issue 1: `id` / `@id` Collision in JSON-LD Processing

**Severity:** HIGH — Affects all node entity files
**Affected schemas:** domain.schema.json, capability.schema.json, process.schema.json
**Affected files:** All 5 node entities

### Problem

The context maps `id → @id` (line 22 of context.jsonld). When a node entity includes BOTH `@id` and `id` with the same value, pyld raises:

```
JsonLdError: colliding keywords detected — keyword: @id
```

Both `@id: "foundations"` and `id: "foundations"` expand to the same JSON-LD subject IRI. The JSON-LD spec forbids colliding keyword aliases.

### Current Workaround

Node entity files omit `@id` entirely, using only `id` (which maps to `@id` through context). The `@id` property in the schemas is optional, so this passes validation.

### Root Cause

The schemas define both `@id` (optional) and `id` (required) as properties. Since the context maps `id → @id`, including both creates a JSON-LD collision. The schemas should clarify which to use:
- **Option A:** Remove `@id` from node schemas (always use `id` via context mapping)
- **Option B:** Remove the `id → @id` mapping from context (use `@id` directly everywhere)

### Impact on Round-Trip

Node entities (using only `id`) pass pyld expand/compact round-trip successfully.

---

## Issue 2: Product/Edge `@id` Lost in JSON-LD Compact Round-Trip

**Severity:** MEDIUM — Affects product and dependency entities
**Affected schemas:** product.schema.json, dependency.schema.json
**Affected files:** 16 products + 59 edges

### Problem

Product and dependency schemas require `@id` directly (not `id`). The context maps `id → @id`. When pyld compacts expanded JSON-LD, it prefers the shorter mapped term `id` over the keyword `@id`. After expand → compact:

```
Input:  {"@id": "steel", "@type": "Product", ...}
Output: {"id": "steel", "@type": "Product", ...}    ← @id became id
```

The product schema uses `additionalProperties: false`, so the compacted form with `id` instead of `@id` would fail schema validation (since `id` is not a defined property in the product schema).

### Root Cause

Same as Issue 1: the `id → @id` context mapping creates an asymmetry between what schemas expect (`@id`) and what pyld produces after compaction (`id`).

### Impact

Initial files validate correctly against schemas. Round-trip through pyld changes the key name but preserves the SEMANTIC content. The expanded form is always correct. Only the compacted serialization differs.

### Recommended Fix

Add `id` as an allowed property in product and dependency schemas, OR use `id` consistently across all schemas (removing direct `@id` references).

---

## Issue 3: Product `tags.material` maxItems vs Node Inheritance

**Severity:** LOW — Design consideration
**Affected schema:** product.schema.json

### Problem

The product schema limits `tags.material` to `maxItems: 3`. The `foundations` domain node has 4 material tags: `["wood", "stone", "biomass", "water"]`. Products derived from `foundations` outputs inherit all 4 tags, exceeding the limit.

### Workaround Applied

Products from `foundations` were trimmed to the first 3 material tags: `["wood", "stone", "biomass"]`.

### Recommendation

Either:
- Increase product `maxItems` to match nodes (4 or unlimited)
- Or define a clear rule for which material tags products inherit from their source node

---

## Issue 4: `@context` Uses Relative Path — Fails pyld Without baseIRI

**Severity:** LOW — Tooling limitation, not schema issue
**Affected files:** All 80 entity files

### Problem

Entity files use `"@context": "../../context.jsonld"` (relative path). pyld's expand() requires either:
- An absolute URI as `@context`
- A `baseIRI` option to resolve relative paths
- Inline context (embedding the full context object)

### Workaround

For validation, the context was inlined during round-trip testing. This is expected — production JSON-LD processors need a document loader that resolves relative paths.

### Recommendation

Document that per-entity files require a document loader configured with the correct base path. The spec example also uses relative paths (`"context.jsonld"`), confirming this is the intended approach.

---

## Issue 5: No Process-Level Node in the Sample Set

**Severity:** INFO — Not a bug

### Observation

The task specified `silicon.mg-si-production` as a "process node" but the actual data shows it as a capability (1 dot = capability level). All 5 converted nodes are either domain (0 dots) or capability (1 dot) level. The process schema was not validated against real data.

### Recommendation

Include at least one process-level node (2+ dots) in the next conversion batch to validate the process schema.

---

## Summary

| # | Issue | Severity | Schema Change Needed |
|---|-------|----------|---------------------|
| 1 | id/@id collision in nodes | HIGH | Yes — remove @id from node schemas |
| 2 | @id → id in product/edge round-trip | MEDIUM | Yes — add id to product/edge schemas |
| 3 | Product material maxItems too low | LOW | Yes — increase to 4+ |
| 4 | Relative @context paths | LOW | No — tooling config |
| 5 | No process node tested | INFO | No — test coverage |

### Validation Results

- **80 files created** (5 nodes + 16 products + 59 edges)
- **Schema validation:** 80/80 pass
- **PyLD round-trip:** 5/5 nodes pass, 75 products/edges have Issue 2 (semantic content preserved, key name changed)
