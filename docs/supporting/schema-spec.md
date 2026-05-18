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
| `type` | string | Currently always `"required"` — hard prerequisite |

Direction convention: `from` depends on `to`. Example: `{ from: "metallurgy", to: "foundations" }` means metallurgy requires foundations.

---

## 3. Tag Taxonomy

### 3.1 Overview

The `tags` field classifies each node along three independent dimensions plus a set of boolean flags. Tags are **additive** — a single node carries multiple tags from different dimensions.

### 3.2 Material Dimension

Classifies the primary physical substances a node produces or transforms.

| Tag | Definition | Example Nodes |
|-----|-----------|---------------|
| `metals` | Metallic elements and alloys | `metallurgy.copper-bronze`, `metallurgy.iron-steel` |
| `silicon` | Silicon and silicon compounds | `silicon.mg-si-production`, `silicon.purification` |
| `glass` | Amorphous silica-based materials | `metallurgy.glass-lime`, `vacuum-optics.glass-advanced` |
| `ceramics` | Crystalline inorganic non-metals | `advanced-materials`, `foundations.kilns-pottery` |
| `polymers` | Organic macromolecular materials | `polymers`, `polymers.thermosets` |
| `chemicals` | Industrial chemicals, acids, alkalis | `chemistry.acids`, `chemistry.alkalis` |
| `wood` | Lumber, timber, wooden implements | `foundations.tools-basic` |
| `stone` | Stone and mineral materials | `foundations.tools-basic` |
| `clay` | Clay and earthen materials | `foundations.kilns-pottery` |
| `fibers` | Natural and synthetic fibers | `textiles`, `polymers.composites` |
| `gases` | Industrial and specialty gases | `specialty-gases`, `specialty-gases.air-separation` |
| `water` | Water supply, purification, hydraulic systems | `health` |
| `biomass` | Plant and animal-derived materials | `foundations.food-agriculture`, `petrochemicals` |

**Rules:**
- Assign the material tag(s) for substances the node **primarily produces**, not all substances it touches.
- A node may have 0-3 material tags. Most have exactly one.
- Domain-level nodes inherit the union of their children's material tags.

### 3.3 Capability Dimension

Classifies the primary functional capability a node provides.

| Tag | Definition | Example Nodes |
|-----|-----------|---------------|
| `energy` | Power generation, conversion, distribution | `energy`, `energy.steam-power`, `energy.electricity` |
| `precision` | Precision manufacturing, metrology | `machine-tools`, `machine-tools.precision-metrology` |
| `computing` | Calculation, automation, data processing | `computing`, `vlsi-scaling.eda-design` |
| `transport` | Movement of materials, people, information | `transport`, `aircraft` |
| `health` | Medical, sanitation, safety | `health` |
| `measurement` | Sensors, instruments, calibration | `metrology`, `vacuum-optics.optics-inspection` |
| `cooling` | Refrigeration, thermal management | `energy-storage` (UPS/thermal) |
| `vacuum` | Vacuum systems, controlled atmospheres | `vacuum-optics.vacuum-systems` |
| `optics` | Lenses, microscopy, lithographic imaging | `vacuum-optics.optics-inspection`, `vlsi-scaling.advanced-lithography` |
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

## 4. Edge Type Classification Rules

### 4.1 Motivation

The current `edges.json` uses a single type: `"required"`. This loses the distinction between edges where the prerequisite provides a **consumed substance** versus a **reusable apparatus**. Adding a `type` field with values `"material"` and `"tool"` enables richer queries and diagram rendering.

### 4.2 Classification Definitions

#### `material`

The prerequisite node provides a **physical substance consumed or transformed** by the dependent node. The substance is used up, incorporated into a product, or chemically altered in the process.

**Test:** Does the prerequisite produce a substance that the dependent node consumes as feedstock, fuel, or reagent?

Examples:

| Edge | Rationale |
|------|-----------|
| `foundations` → `foundations.kilns-pottery` (charcoal consumed in firing) | Charcoal is burned as fuel — consumed |
| `mining` → `metallurgy.iron-steel` (iron ore consumed in smelting) | Ore is reduced to metal — consumed |
| `chemistry.acids` → `silicon.basic-devices` (HF for wafer etching) | Acid chemically reacts — consumed |
| `foundations.kilns-pottery` → `chemistry` (crucibles and vessels) | Refractory vessels wear out and are replaced — consumed over time |

#### `tool`

The prerequisite node provides a **reusable piece of equipment, infrastructure, or capability** that the dependent node employs without consuming it. The tool persists through the process and can be reused.

**Test:** Does the prerequisite provide a reusable apparatus, infrastructure, or enabling capability?

Examples:

| Edge | Rationale |
|------|-----------|
| `foundations` → `metallurgy` (stone tools used for mining) | Tools persist — reusable |
| `machine-tools` → `energy.steam-power` (lathes for cylinder boring) | Lathe is not consumed — reusable |
| `energy.electricity` → `chemistry.distillation-gas-handling` (electric motors) | Motor persists — reusable |
| `metallurgy.iron-steel` → `machine-tools.foundry` (steel for machine castings) | Cast machine frame persists — reusable infrastructure |

### 4.3 Ambiguity Resolution

Some edges are ambiguous — the prerequisite provides both a substance AND a tool. For example:

- `metallurgy.iron-steel` → `energy.steam-power`: Steel is a material consumed to build the boiler, but the boiler becomes reusable infrastructure.
- `foundations.kilns-pottery` → `chemistry.acids`: Kilns produce refractory vessels (tool) but also consume charcoal (material) to fire them.

**Resolution rule: When an edge could be classified as both `material` and `tool`, classify it as `tool`.**

Rationale: The infrastructure aspect dominates in the technology tree context. The enduring capability (the existence of a forge, a lathe, a kiln) matters more for dependency analysis than the consumable inputs. Consumables are tracked through the `outputs` field on nodes.

### 4.4 Edge Schema Change

The `type` field in `edges.json` changes from its current single value:

**Before:**
```json
{ "from": "metallurgy", "to": "foundations", "type": "required" }
```

**After:**
```json
{ "from": "metallurgy", "to": "foundations", "type": "tool" }
```

The `type` field becomes required and takes one of two values:
- `"material"` — prerequisite provides a consumed substance
- `"tool"` — prerequisite provides reusable equipment/infrastructure

The old value `"required"` is **retired**. All edges are implicitly required — the `material`/`tool` distinction refines the nature of the requirement, not its strength.

**Field specifications:**
- `type`: String. Required. One of `"material"` or `"tool"`.
- `from`: String. Node ID of the dependent. Unchanged.
- `to`: String. Node ID of the prerequisite. Unchanged.

### 4.5 Worked Classification Examples

Walk through classification of representative edges from the current data:

**Example 1: `{ from: "energy.steam-power", to: "machine-tools" }`**
- Steam power needs machine tools to build cylinders, pistons, and boilers.
- Machine tools are reusable equipment — the lathe is not consumed.
- Classification: **`tool`**

**Example 2: `{ from: "silicon.mg-si-production", to: "mining" }`**
- MG-Si production needs quartz from mining.
- Quartz is consumed in the carbothermic reduction — it becomes silicon.
- Classification: **`material`**

**Example 3: `{ from: "machine-tools.foundry", to: "metallurgy.iron-steel" }`**
- The foundry needs iron/steel as the material to cast machine parts.
- Iron/steel is the substance being melted and cast — consumed.
- Classification: **`material`**

**Example 4: `{ from: "silicon.basic-devices", to: "vacuum-optics.vacuum-systems" }`**
- Basic devices need vacuum systems for deposition processes.
- The vacuum chamber and pumps are reusable infrastructure.
- Classification: **`tool`**

**Example 5: `{ from: "energy.steam-power", to: "metallurgy.iron-steel" }`**
- Steam power needs iron/steel for boilers, cylinders, and pistons.
- Steel is consumed as construction material (ambiguous — could argue the built boiler becomes a tool).
- Ambiguity rule applies: classify as **`tool`** because the infrastructure aspect (a boiler that lasts decades) dominates.

---

## 5. SIK Placement Test

### 5.1 Definition

**SIK** = Shared Infrastructure & Knowledge. The SIK test determines whether technologies belong in the same domain or should be split into separate domains.

### 5.2 The Test

A set of technologies belongs in the same domain if and only if **all three** of the following conditions hold:

1. **Physical Infrastructure Overlap >50%**: The technologies share more than half of their physical infrastructure (buildings, equipment, utilities, supply chains).
2. **Knowledge Base Overlap >50%**: The practitioners working on these technologies share more than half of their theoretical and practical knowledge (chemistry, physics, engineering principles).
3. **Practitioner Profile Overlap >50%**: The skills, training, and working methods of practitioners are substantially the same. A practitioner trained in one sub-area could transition to another with reasonable retraining (<1 year).

### 5.3 Split Rule

When identifiable subgroups within a domain share **<50%** infrastructure with the rest of the domain, consider splitting:

- Identify the subgroup with the lowest infrastructure overlap to the rest.
- If that subgroup's overlap with the rest of the domain is <50%, it is a split candidate.
- Evaluate whether the subgroup is large enough to constitute its own domain (minimum: 2-3 capabilities with at least 1 process each).
- If the subgroup is too small to standalone, keep it in the parent domain but note the low cohesion.

### 5.4 Internal Organizing Axis

Each domain MUST declare its **internal organizing axis** — the primary principle by which its capabilities are arranged. Common axes:

| Axis | Description | Example Domain |
|------|-------------|---------------|
| Chronological | Capabilities ordered by when they become achievable | `metallurgy` (copper → bronze → iron → steel) |
| Process Chain | Capabilities ordered by material flow | `silicon` (MG-Si → purification → crystal growth → devices) |
| Functional | Capabilities grouped by function | `energy` (coal → steam → electricity → furnaces → ICE) |
| Precision Ladder | Capabilities ordered by increasing precision | `machine-tools` (foundry → bootstrap → metrology → bearings) |
| Complexity | Capabilities ordered by increasing system complexity | `photolithography` (cleanrooms → resists → fab processes) |

The organizing axis is documented in the domain node's `description` or a dedicated `organizing_axis` field (implementation decision for T2+).

### 5.5 Worked SIK Examples

**Example 1: Should `metallurgy.glass-lime` stay in `metallurgy`?**

- Infrastructure overlap: Glass/lime production uses kilns and furnaces similar to smelting. ~60% overlap.
- Knowledge overlap: Glass chemistry is distinct from metal smelting chemistry. ~30% overlap.
- Practitioner overlap: Glass blowers and smelters are different trades. ~20% overlap.

Result: Low knowledge and practitioner overlap. Glass-lime is a **split candidate**. However, it has only 1 capability — too small to standalone. Keep in `metallurgy` but note the low cohesion. In practice, glass advanced already split off to `vacuum-optics.glass-advanced`.

**Example 2: Should `vacuum-optics` be one domain or two (vacuum + optics)?**

- Infrastructure overlap: Vacuum chambers are used for optical coating. Precision grinding equipment is distinct. ~40% overlap.
- Knowledge overlap: Vacuum physics and optical engineering share some physics fundamentals but diverge significantly. ~35% overlap.
- Practitioner overlap: Vacuum engineers and optical engineers are different specialists. ~25% overlap.

Result: Below 50% on all three dimensions. However, vacuum and optics are tightly coupled in semiconductor fab — vacuum is required for deposition, optics is required for lithography. The coupling argument keeps them together despite SIK split candidacy. This is a case where **inter-domain coupling** overrides the SIK test.

**Example 3: Should `polymers.natural-rubber` and `polymers.composites` be in the same domain?**

- Infrastructure overlap: Both use compression molding, both use two-roll mills for compounding. ~55% overlap.
- Knowledge overlap: Polymer chemistry fundamentals are shared. Vulcanization and composite layup are different but share matrix chemistry. ~60% overlap.
- Practitioner overlap: Both are polymer engineers with overlapping training. ~65% overlap.

Result: All dimensions >50%. Confirmed: natural rubber and composites belong in `polymers`.

### 5.6 Override Conditions

The SIK test is the default decision framework, but two conditions can override:

1. **Inter-domain coupling override**: If splitting would create tight circular dependencies between the resulting domains (A depends on B depends on A at the capability level), keep them together despite low SIK overlap.
2. **Bootstrap stage override**: Technologies that are tightly coupled in the bootstrap sequence (one enables the other immediately) may be grouped even with moderate SIK divergence, because the bootstrap narrative demands their co-presentation.

Both overrides must be documented with a justification when applied.

---

## 6. Node Schema Changes — Summary

### 6.1 New `tags` Field

A `tags` object is added to each node with the structure defined in §3.6:

```json
{
  "id": "metallurgy.iron-steel",
  "name": "Iron & Steel Production",
  "level": "capability",
  "parent": "metallurgy",
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

### 6.2 `level` Field — Auto-Derivation

The `level` field remains part of the schema but its value is auto-derived from the node ID:

- 0 dots in ID → `"domain"`
- 1 dot in ID → `"capability"`
- 2+ dots in ID → `"process"`

Supports arbitrary depth: `domain.capability.sub-process.sub-sub-process` is valid. The `level` field value for 2+ dots is always `"process"` regardless of how many levels deep.

### 6.3 `parent` Field — Auto-Derivation

The `parent` field value is auto-derived from the node ID:

- For `domain` nodes: `null`
- For all others: everything before the last dot

Examples:
- `metallurgy.iron-steel` → parent = `"metallurgy"`
- `silicon.crystal-growth.cz-pulling` → parent = `"silicon.crystal-growth"`

### 6.4 Backward Compatibility

The existing top-level boolean fields (`critical`, `early_win`, `pinnacle`) and their `_note` counterparts remain in place. Tooling SHOULD read from both locations during the transition period. Eventually the `_note` fields may be folded into the `tags` object, but this spec does not mandate that migration.

---

## 7. Edge Schema Changes — Summary

### 7.1 `type` Field Redefined

| Property | Before | After |
|----------|--------|-------|
| Allowed values | `["required"]` | `["material", "tool"]` |
| Semantics | Binary dependency exists | Nature of dependency: consumed substance vs. reusable apparatus |
| Required | Yes | Yes |

### 7.2 Migration

Every existing edge with `type: "required"` must be reclassified as either `"material"` or `"tool"` using the rules in §4. There is no `"required"` value in the new schema. This is a breaking change — all consumers of `edges.json` must be updated.

### 7.3 `from` / `to` Semantics

Unchanged. `from` = dependent, `to` = prerequisite. Direction convention: `from` depends on `to`.

---

## 8. Validation Rules

### 8.1 Tag Validation

- Every node MUST have a `tags` object.
- `tags.material` MUST contain only values from §3.2 allowed list.
- `tags.capability` MUST contain only values from §3.3 allowed list.
- `tags.era` MUST be exactly one value from §3.4 allowed list.
- `tags.critical`, `tags.early-win`, `tags.pinnacle` MUST be boolean.
- The values in `tags` booleans MUST match the top-level boolean fields.

### 8.2 Edge Type Validation

- Every edge MUST have a `type` field.
- `type` MUST be exactly `"material"` or `"tool"`.
- The value `"required"` is invalid in the new schema.

### 8.3 Auto-Derivation Validation

- For every node, `level` MUST be consistent with dot count in `id`.
- For every node, `parent` MUST be consistent with `id` (everything before last dot, or null for domains).
- Every `parent` value (when non-null) MUST reference an existing node `id`.

---

## 9. Glossary

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
