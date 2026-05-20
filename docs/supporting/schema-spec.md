# Schema Specification: Tag Taxonomy, Edge Types & SIK Placement

> Reference document defining the classification rules for the bootciv technology tree data layer. Governs `nodes.json` tag annotations, `edges.json` type discrimination, and domain boundary decisions.

---

## 1. Purpose

The technology tree currently stores nodes as flat records with boolean flags and edges as untyped dependency links. This specification introduces:

1. A **tag taxonomy** for dimensional classification of nodes (material, capability, era).
2. An **edge type classification** distinguishing material flows from tool/infrastructure dependencies.
3. A **SIK placement test** (Shared Infrastructure & Knowledge) for domain boundary decisions.

These rules are normative. Any automated tooling (validators, diagram generators, query engines) MUST enforce them.

---

## 2. Current Schema (Baseline)

### 2.1 Node Schema

Every node in `nodes.json` has these fields today:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Dotted hierarchical: `domain`, `domain.capability`, or `domain.capability.process` |
| `name` | string | Human-readable display name |
| `level` | string | One of: `domain`, `capability`, `process` |
| `parent` | string \| null | ID of parent node; null for domains |
| `description` | string | 1-3 sentence summary |
| `timeline` | string | Estimated time range (e.g., `"Years 0-10"`) |
| `outputs` | string[] | Product/material/capability tokens produced |
| `critical` | boolean | True if critical-path enabler |
| `critical_note` | string | Present only when `critical=true` |
| `early_win` | boolean | True if high-value early feedback loop |
| `early_win_note` | string | Present only when `early_win=true` |
| `pinnacle` | boolean | True if end-goal requiring mature ecosystem |
| `pinnacle_note` | string | Present only when `pinnacle=true` |

### 2.2 Edge Schema

Every edge in `edges.json` has these fields today:

| Field | Type | Description |
|-------|------|-------------|
| `from` | string | Node ID of the dependent (thing that needs something) |
| `to` | string | Node ID of the prerequisite (thing needed first) |
| `type` | string | `"material"` or `"tool"` — consumed substance vs. reusable infrastructure |

Direction convention: `from` depends on `to`. Example: `{ from: "metals", to: "foundations" }` means metals requires foundations.

---

## 3. Tag Taxonomy

### 3.1 Overview

The `tags` field classifies each node along three independent dimensions plus a set of boolean flags. Tags are **additive** — a single node carries multiple tags from different dimensions.

### 3.2 Material Dimension

Classifies the primary physical substances a node produces or transforms.

| Tag | Definition | Example Nodes |
|-----|-----------|---------------|
| `metals` | Metallic elements and alloys | `metals.copper-bronze`, `metals.iron-steel` |
| `silicon` | Silicon and silicon compounds | `silicon.mg-si-production`, `silicon.purification` |
| `glass` | Amorphous silica-based materials | `glass.basic`, `glass.advanced` |
| `ceramics` | Crystalline inorganic non-metals | `ceramics`, `ceramics.pottery` |
| `polymers` | Organic macromolecular materials | `polymers`, `polymers.thermosets` |
| `chemicals` | Industrial chemicals, acids, alkalis | `chemistry.acids`, `chemistry.alkalis` |
| `wood` | Lumber, timber, wooden implements | `foundations.tools-basic` |
| `stone` | Stone and mineral materials | `foundations.tools-basic` |
| `clay` | Clay and earthen materials | `ceramics.pottery` |
| `fibers` | Natural and synthetic fibers | `textiles`, `polymers.composites` |
| `gases` | Industrial and specialty gases | `gas-handling`, `chemistry.air-separation` |
| `water` | Water supply, purification, hydraulic systems | `health` |
| `biomass` | Plant and animal-derived materials | `foundations.food-agriculture`, `chemistry` |

**Rules:**
- Assign the material tag(s) for substances the node **primarily produces**, not all substances it touches.
- A node may have 0-3 material tags. Most have exactly one.
- Domain-level nodes inherit the union of their children's material tags.

### 3.3 Capability Dimension

Classifies the primary functional capability a node provides.

| Tag | Definition | Example Nodes |
|-----|-----------|---------------|
| `energy` | Power generation, conversion, distribution | `energy`, `energy.steam-power`, `energy.electricity` |
| `precision` | Precision manufacturing, metrology | `machine-tools`, `measurement.precision-metrology` |
| `computing` | Calculation, automation, data processing | `computing`, `vlsi-scaling.eda-design` |
| `transport` | Movement of materials, people, information | `transport`, `transport.aviation` |
| `health` | Medical, sanitation, safety | `health` |
| `measurement` | Sensors, instruments, calibration | `measurement`, `optics.inspection` |
| `cooling` | Refrigeration, thermal management | `energy.storage` (UPS/thermal) |
| `vacuum` | Vacuum systems, controlled atmospheres | `gas-handling.vacuum` |
| `optics` | Lenses, microscopy, lithographic imaging | `optics.inspection`, `vlsi-scaling.advanced-lithography` |
| `construction` | Building, structural engineering | `chemistry.cement`, `transport` (roads/bridges) |

**Rules:**
- Assign the capability tag(s) for the node's **primary functional output**, not secondary benefits.
- A node may have 0-2 capability tags.
- Domain-level nodes may have multiple capability tags reflecting breadth.

### 3.4 Era Dimension

Classifies the historical era a node first becomes achievable.

| Tag | Approximate Period | Characteristic Technologies |
|-----|-------------------|----------------------------|
| `stone-age` | Years 0-5 | Stone tools, fire, charcoal, basic pottery |
| `copper-age` | Years 5-10 | Copper smelting, simple casting |
| `bronze-age` | Years 5-15 | Bronze alloying, improved casting |
| `iron-age` | Years 5-25 | Iron smelting, steel, forge welding |
| `industrial` | Years 15-40 | Steam power, machine tools, bulk chemistry |
| `electronic` | Years 30-70 | Electricity, silicon, basic semiconductors |
| `semiconductor` | Years 40-100 | Photolithography, IC fabrication, VLSI |
| `advanced` | Years 70-200+ | EUV lithography, GPUs, advanced packaging |

**Rules:**
- Each node has exactly one era tag — the earliest era in which it becomes achievable.
- Era tags are assigned at the capability/process level. Domain nodes take the earliest era among their children.
- Era boundaries are approximate, not hard cutoffs.

### 3.5 Boolean Flags (Preserved)

The existing boolean flags remain unchanged and are included in the `tags` object for consolidation:

| Flag | Type | Description |
|------|------|-------------|
| `critical` | boolean | Critical-path enabler; downstream blocked without this |
| `early-win` | boolean | High-value early output creating positive feedback |
| `pinnacle` | boolean | End-goal requiring mature ecosystem + generational refinement |

These are NOT arrays — they remain single booleans as in the current schema.

### 3.6 Tags Object Structure

The new `tags` field is a JSON object:

```json
{
  "tags": {
    "material": ["metals", "chemicals"],
    "capability": ["energy"],
    "era": "industrial",
    "critical": false,
    "early-win": false,
    "pinnacle": false
  }
}
```

**Field specifications:**
- `tags.material`: Array of strings. Allowed values from §3.2. May be empty `[]`.
- `tags.capability`: Array of strings. Allowed values from §3.3. May be empty `[]`.
- `tags.era`: String. Exactly one value from §3.4. Required on all nodes.
- `tags.critical`: Boolean. Preserved from existing `critical` field.
- `tags.early-win`: Boolean. Preserved from existing `early_win` field.
- `tags.pinnacle`: Boolean. Preserved from existing `pinnacle` field.

The top-level `critical`, `early_win`, `pinnacle` fields and their associated `_note` fields remain in place for backward compatibility. The `tags` object duplicates the boolean values for query convenience.

---

## 4. Taxonomy Field

### 4.1 Overview

The `taxonomy` field provides a **hierarchical classification** of nodes by material origin, complementary to the flat tag system defined in §3. Where tags use closed vocabularies with fixed values (§3.2–§3.4), taxonomy uses an open dotted notation that supports deeper categorization within broad material families.

Taxonomy is **optional** on all nodes. Nodes without a `taxonomy` field are valid. When present, `taxonomy` provides additional query and grouping capability without replacing the existing tag system.

### 4.2 Format

The `taxonomy` field is a JSON array of dotted hierarchical strings:

```json
{
  "taxonomy": ["biomass.plant.wood", "biomass.plant.fiber"]
}
```

**Structural rules:**

- Each taxonomy value is a dot-separated string of **two or more segments**: `root.branch`, `root.branch.leaf`, etc.
- Segments use **kebab-case**: lowercase letters, digits, and hyphens. No uppercase, no underscores, no spaces.
- The **first segment** (root) must be one of the three known roots (§4.3).
- Additional segments provide increasingly specific classification. Depth is unbounded.
- Duplicate values within a single node's `taxonomy` array are not allowed.

### 4.3 Root Vocabulary

Three top-level roots are defined:

| Root | Definition | Examples |
|------|-----------|----------|
| `biomass` | Materials derived from living organisms (plants, animals, fungi) | `biomass.plant.wood`, `biomass.animal.meat`, `biomass.plant.fiber` |
| `mineral` | Inorganic materials extracted from the earth | `mineral.ore.iron`, `mineral.stone.flint`, `mineral.clay.kaolin` |
| `synthetic` | Materials produced through industrial processing, not found in nature | `synthetic.polymer.thermoset`, `synthetic.alloy.steel`, `synthetic.semiconductor.silicon` |

**Rules:**

- The root vocabulary is a **closed set**. Only `biomass`, `mineral`, and `synthetic` are valid first segments.
- New branches beneath existing roots may be created as needed without spec changes.
- A node may carry multiple taxonomy values from different roots (e.g., a composite material node might have both `biomass.plant.fiber` and `synthetic.polymer.thermoset`).

### 4.4 Relationship to Tags

Taxonomy and tags are **independent classification systems**:

- **Tags** (§3): Closed vocabularies for material, capability, era dimensions. Required on all nodes.
- **Taxonomy** (§4): Open hierarchical classification by material origin. Optional on all nodes.
- Taxonomy values are NOT validated against tag values. A node may have `tags.material: ["wood"]` and `taxonomy: ["biomass.plant.wood"]` — the systems use independent vocabularies.
- Taxonomy does not replace or deprecate any existing tag. It provides a supplementary dimension for material-origin queries.

### 4.5 Validation Rules

Automated validation (check 16 in `validate.sh`) enforces:

1. If `taxonomy` is present, it must be a non-empty array of strings.
2. Each string must contain at least one dot (≥2 segments).
3. Each segment must match `[a-z][a-z0-9-]*` (kebab-case, lowercase).
4. The first segment must be one of: `biomass`, `mineral`, `synthetic`.
5. No duplicate values within a single node's `taxonomy` array.
6. Nodes without `taxonomy` are valid — no error.

---

## 5. Edge Type Classification Rules

### 5.1 Motivation

The current `edges.json` uses two types: `"material"` and `"tool"`, distinguishing edges where the prerequisite provides a **consumed substance** versus a **reusable apparatus**. This classification enables richer queries and diagram rendering.

### 5.2 Classification Definitions

#### `material`

The prerequisite node provides a **physical substance consumed or transformed** by the dependent node. The substance is used up, incorporated into a product, or chemically altered in the process.

**Test:** Does the prerequisite produce a substance that the dependent node consumes as feedstock, fuel, or reagent?

Examples:

| Edge | Rationale |
|------|-----------|
| `foundations` → `ceramics.pottery` (charcoal consumed in firing) | Charcoal is burned as fuel — consumed |
| `mining` → `metals.iron-steel` (iron ore consumed in smelting) | Ore is reduced to metal — consumed |
| `chemistry.acids` → `silicon.basic-devices` (HF for wafer etching) | Acid chemically reacts — consumed |
| `ceramics.pottery` → `chemistry` (crucibles and vessels) | Refractory vessels wear out and are replaced — consumed over time |

#### `tool`

The prerequisite node provides a **reusable piece of equipment, infrastructure, or capability** that the dependent node employs without consuming it. The tool persists through the process and can be reused.

**Test:** Does the prerequisite provide a reusable apparatus, infrastructure, or enabling capability?

Examples:

| Edge | Rationale |
|------|-----------|
| `foundations` → `metals` (stone tools used for mining) | Tools persist — reusable |
| `machine-tools` → `energy.steam-power` (lathes for cylinder boring) | Lathe is not consumed — reusable |
| `energy.electricity` → `chemistry.distillation` (electric motors) | Motor persists — reusable |
| `metals.iron-steel` → `machine-tools.casting` (steel for machine castings) | Cast machine frame persists — reusable infrastructure |

### 5.3 Ambiguity Resolution

Some edges are ambiguous — the prerequisite provides both a substance AND a tool. For example:

- `metals.iron-steel` → `energy.steam-power`: Steel is a material consumed to build the boiler, but the boiler becomes reusable infrastructure.
- `ceramics.pottery` → `chemistry.acids`: Kilns produce refractory vessels (tool) but also consume charcoal (material) to fire them.

**Resolution rule: When an edge could be classified as both `material` and `tool`, classify it as `tool`.**

Rationale: The infrastructure aspect dominates in the technology tree context. The enduring capability (the existence of a forge, a lathe, a kiln) matters more for dependency analysis than the consumable inputs. Consumables are tracked through the `outputs` field on nodes.

### 5.4 Edge Schema Change

The `type` field in `edges.json` changes from its current single value:

**Before:**
```json
{ "from": "metals", "to": "foundations", "type": "required" }
```

**After:**
```json
{ "from": "metals", "to": "foundations", "type": "tool" }
```

The `type` field becomes required and takes one of two values:
- `"material"` — prerequisite provides a consumed substance
- `"tool"` — prerequisite provides reusable equipment/infrastructure

The old value `"required"` is **retired**. All edges are implicitly required — the `material`/`tool` distinction refines the nature of the requirement, not its strength.

**Field specifications:**
- `type`: String. Required. One of `"material"` or `"tool"`.
- `from`: String. Node ID of the dependent. Unchanged.
- `to`: String. Node ID of the prerequisite. Unchanged.

### 5.5 Worked Classification Examples

Walk through classification of representative edges from the current data:

**Example 1: `{ from: "energy.steam-power", to: "machine-tools" }`**
- Steam power needs machine tools to build cylinders, pistons, and boilers.
- Machine tools are reusable equipment — the lathe is not consumed.
- Classification: **`tool`**

**Example 2: `{ from: "silicon.mg-si-production", to: "mining" }`**
- MG-Si production needs quartz from mining.
- Quartz is consumed in the carbothermic reduction — it becomes silicon.
- Classification: **`material`**

**Example 3: `{ from: "machine-tools.casting", to: "metals.iron-steel" }`**
- The foundry needs iron/steel as the material to cast machine parts.
- Iron/steel is the substance being melted and cast — consumed.
- Classification: **`material`**

**Example 4: `{ from: "silicon.basic-devices", to: "gas-handling.vacuum" }`**
- Basic devices need vacuum systems for deposition processes.
- The vacuum chamber and pumps are reusable infrastructure.
- Classification: **`tool`**

**Example 5: `{ from: "energy.steam-power", to: "metals.iron-steel" }`**
- Steam power needs iron/steel for boilers, cylinders, and pistons.
- Steel is consumed as construction material (ambiguous — could argue the built boiler becomes a tool).
- Ambiguity rule applies: classify as **`tool`** because the infrastructure aspect (a boiler that lasts decades) dominates.

---

## 6. SIK Placement Test

### 6.1 Definition

**SIK** = Shared Infrastructure & Knowledge. The SIK test determines whether technologies belong in the same domain or should be split into separate domains.

### 6.2 The Test

A set of technologies belongs in the same domain if and only if **all three** of the following conditions hold:

1. **Physical Infrastructure Overlap >50%**: The technologies share more than half of their physical infrastructure (buildings, equipment, utilities, supply chains).
2. **Knowledge Base Overlap >50%**: The practitioners working on these technologies share more than half of their theoretical and practical knowledge (chemistry, physics, engineering principles).
3. **Practitioner Profile Overlap >50%**: The skills, training, and working methods of practitioners are substantially the same. A practitioner trained in one sub-area could transition to another with reasonable retraining (<1 year).

### 6.3 Split Rule

When identifiable subgroups within a domain share **<50%** infrastructure with the rest of the domain, consider splitting:

- Identify the subgroup with the lowest infrastructure overlap to the rest.
- If that subgroup's overlap with the rest of the domain is <50%, it is a split candidate.
- Evaluate whether the subgroup is large enough to constitute its own domain (minimum: 2-3 capabilities with at least 1 process each).
- If the subgroup is too small to standalone, keep it in the parent domain but note the low cohesion.

### 6.4 Internal Organizing Axis

Each domain MUST declare its **internal organizing axis** — the primary principle by which its capabilities are arranged. Common axes:

| Axis | Description | Example Domain |
|------|-------------|---------------|
| Chronological | Capabilities ordered by when they become achievable | `metals` (copper → bronze → iron → steel) |
| Process Chain | Capabilities ordered by material flow | `silicon` (MG-Si → purification → crystal growth → devices) |
| Functional | Capabilities grouped by function | `energy` (coal → steam → electricity → furnaces → ICE) |
| Precision Ladder | Capabilities ordered by increasing precision | `machine-tools` (foundry → bootstrap → measurement → bearings) |
| Complexity | Capabilities ordered by increasing system complexity | `photolithography` (cleanrooms → resists → fab processes) |

The organizing axis is documented in the domain node's `description` or a dedicated `organizing_axis` field (implementation decision for T2+).

### 6.5 Worked SIK Examples

**Example 1: Glass production — should it stay in `metals`?**

- Infrastructure overlap: Glass/lime production uses kilns and furnaces similar to smelting. ~60% overlap.
- Knowledge overlap: Glass chemistry is distinct from metal smelting chemistry. ~30% overlap.
- Practitioner overlap: Glass blowers and smelters are different trades. ~20% overlap.

Result: Below 50% on two of three dimensions. The SIK test correctly identified glass as a split candidate. Initially, glass production remained in `metals` because it had only one capability — too small to form its own domain. Later, when glass accumulated a second capability (advanced glass from the dissolved `vacuum-optics` domain), it was promoted to a standalone `glass` domain with `glass.basic` and `glass.advanced`. This demonstrates that the SIK test can identify split candidates early, even if the split is deferred until the subgroup reaches sufficient size.

**Example 2: `vacuum-optics` — should vacuum and optics be separate domains?**

- Infrastructure overlap: Vacuum chambers are used for optical coating. Precision grinding equipment is distinct. ~40% overlap.
- Knowledge overlap: Vacuum physics and optical engineering share some physics fundamentals but diverge significantly. ~35% overlap.
- Practitioner overlap: Vacuum engineers and optical engineers are different specialists. ~25% overlap.

Result: Below 50% on all three dimensions. The inter-domain coupling override was initially considered — semiconductor fab tightly couples vacuum systems and optics (both needed for lithography). However, closer analysis revealed that vacuum belongs with gas manipulation (`gas-handling`) — a bamboo pump proves gas handling is independent of both chemistry and optics. The domain was ultimately dissolved into four standalone domains: `optics` (lenses, microscopy), `gas-handling` (vacuum, gas compression), `glass` (material science), and `measurement` (instruments). This shows the coupling override should be applied conservatively — apparent coupling may reflect shared downstream consumers rather than shared infrastructure or knowledge.

**Example 3: Should `polymers.rubber.natural` and `polymers.composites` be in the same domain?**

- Infrastructure overlap: Both use compression molding, both use two-roll mills for compounding. ~55% overlap.
- Knowledge overlap: Polymer chemistry fundamentals are shared. Vulcanization and composite layup are different but share matrix chemistry. ~60% overlap.
- Practitioner overlap: Both are polymer engineers with overlapping training. ~65% overlap.

Result: All dimensions >50%. Confirmed: natural rubber and composites belong in `polymers`.

**Example 4: Should `plants` be a distinct domain rather than part of `foundations`?**

- Infrastructure overlap with foundations: Plants use gardens, fields, and simple harvesting tools. Foundations uses fire pits, knapping floors, and foraging grounds. ~30% overlap.
- Knowledge overlap with foundations: Botany, cultivation timing, and fiber processing vs. fire-making and stone knapping. ~25% overlap.
- Practitioner overlap with foundations: Farmers and botanists vs. toolmakers and fire-keepers. ~20% overlap.

Result: Below 50% on all three dimensions when compared to `foundations`. Plants is justified as a distinct domain because:

1. **Distinct human needs and processing chains.** The five capability groupings (edible, medicinal, structural, fiber, dye) each map to a fundamentally different human need — food security, health, shelter, clothing, and aesthetics — with independent processing chains (cultivation → harvest → preservation; harvest → preparation → application; fell → season → shape; ret → spin → weave; extract → mordant → dye).

2. **Stone-age Industrial Kit component.** Plants require minimal processing — harvesting, drying, and basic cultivation are achievable from Year 0 with zero tooling. Yet they enable critical capabilities: food surplus (the engine of specialization), structural timber, cordage fibers, and medicinal compounds. This makes plants the quintessential SIK resource: shared knowledge of local flora underpins every subsequent domain.

3. **Sufficient domain size.** With 19 tech-tree nodes across 5 capabilities plus 86 species catalog entries, the plants domain comfortably exceeds the minimum domain size threshold (2-3 capabilities with at least 1 process each). The internal organizing axis is **functional** — capabilities grouped by the human need they serve.

### 6.6 Override Conditions

The SIK test is the default decision framework, but two conditions can override:

1. **Inter-domain coupling override**: If splitting would create tight circular dependencies between the resulting domains (A depends on B depends on A at the capability level), keep them together despite low SIK overlap.
2. **Bootstrap stage override**: Technologies that are tightly coupled in the bootstrap sequence (one enables the other immediately) may be grouped even with moderate SIK divergence, because the bootstrap narrative demands their co-presentation.

Both overrides must be documented with a justification when applied.

---

## 7. Node Schema Changes — Summary

### 7.1 New `tags` Field

A `tags` object is added to each node with the structure defined in §3.6:

```json
{
  "id": "metals.iron-steel",
  "name": "Iron & Steel Production",
  "level": "capability",
  "parent": "metals",
  "description": "...",
  "timeline": "Years 5-15",
  "outputs": ["wrought_iron", "steel", "iron_bloom", "heat_treated_steel"],
  "critical": true,
  "critical_note": "...",
  "early_win": false,
  "pinnacle": false,
  "tags": {
    "material": ["metals"],
    "capability": ["energy"],
    "era": "iron-age",
    "critical": true,
    "early-win": false,
    "pinnacle": false
  }
}
```

### 7.2 `level` Field — Auto-Derivation

The `level` field remains part of the schema but its value is auto-derived from the node ID:

- 0 dots in ID → `"domain"`
- 1 dot in ID → `"capability"`
- 2+ dots in ID → `"process"`

Supports arbitrary depth: `domain.capability.sub-process.sub-sub-process` is valid. The `level` field value for 2+ dots is always `"process"` regardless of how many levels deep.

### 7.3 `parent` Field — Auto-Derivation

The `parent` field value is auto-derived from the node ID:

- For `domain` nodes: `null`
- For all others: everything before the last dot

Examples:
- `metals.iron-steel` → parent = `"metals"`
- `silicon.crystal-growth.cz-pulling` → parent = `"silicon.crystal-growth"`

### 7.4 Backward Compatibility

The existing top-level boolean fields (`critical`, `early_win`, `pinnacle`) and their `_note` counterparts remain in place. Tooling SHOULD read from both locations during the transition period. Eventually the `_note` fields may be folded into the `tags` object, but this spec does not mandate that migration.

---

## 8. Edge Schema Changes — Summary

### 8.1 `type` Field Redefined

| Property | Before | After |
|----------|--------|-------|
| Allowed values | `["required"]` | `["material", "tool"]` |
| Semantics | Binary dependency exists | Nature of dependency: consumed substance vs. reusable apparatus |
| Required | Yes | Yes |

### 8.2 Migration

Every existing edge with `type: "required"` must be reclassified as either `"material"` or `"tool"` using the rules in §5. There is no `"required"` value in the new schema. This is a breaking change — all consumers of `edges.json` must be updated.

### 8.3 `from` / `to` Semantics

Unchanged. `from` = dependent, `to` = prerequisite. Direction convention: `from` depends on `to`.

---

## 9. Validation Rules

### 9.1 Tag Validation

- Every node MUST have a `tags` object.
- `tags.material` MUST contain only values from §3.2 allowed list.
- `tags.capability` MUST contain only values from §3.3 allowed list.
- `tags.era` MUST be exactly one value from §3.4 allowed list.
- `tags.critical`, `tags.early-win`, `tags.pinnacle` MUST be boolean.
- The values in `tags` booleans MUST match the top-level boolean fields.

### 9.2 Edge Type Validation

- Every edge MUST have a `type` field.
- `type` MUST be exactly `"material"` or `"tool"`.
- The value `"required"` is invalid in the new schema.

### 9.3 Auto-Derivation Validation

- For every node, `level` MUST be consistent with dot count in `id`.
- For every node, `parent` MUST be consistent with `id` (everything before last dot, or null for domains).
- Every `parent` value (when non-null) MUST reference an existing node `id`.

### 9.4 Taxonomy Validation

- `taxonomy` is optional. Nodes without it are valid.
- If present, `taxonomy` MUST be a non-empty array of strings.
- Each string MUST contain at least one dot (≥2 segments).
- Each segment MUST be kebab-case: lowercase letters, digits, and hyphens (`[a-z][a-z0-9-]*`).
- The first segment MUST be one of: `biomass`, `mineral`, `synthetic`.
- No duplicate values within a single node's `taxonomy` array.

---

## 10. Glossary

| Term | Definition |
|------|-----------|
| **SIK** | Shared Infrastructure & Knowledge — the three-axis test for domain boundary decisions |
| **Material edge** | Dependency where the prerequisite provides a substance consumed by the dependent |
| **Tool edge** | Dependency where the prerequisite provides reusable equipment or infrastructure |
| **Tag** | A classification label from a controlled vocabulary applied to a node |
| **Domain** | Top-level technology area (0 dots in ID) |
| **Capability** | Major skill or process family within a domain (1 dot in ID) |
| **Process** | Specific technique or operation (2+ dots in ID) |
| **Organizing axis** | The primary principle by which capabilities are arranged within a domain |
