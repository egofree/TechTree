# SIK Placement Test: Circular Economy Domain

> **Candidate Domain**: `circular-economy`
> **Date**: 2026-05-25
> **Test Framework**: Schema Specification §6 — Shared Infrastructure & Knowledge (SIK) Test
> **Verdict**: **FAIL** — circular-economy is a cross-cutting pattern, not a cohesive domain

---

## 1. Domain Scope Definition

### 1.1 Proposed IN Scope

Resource recovery, material recycling, waste valorization, byproduct utilization, and closed-loop material systems:

- Slag and fly ash valorization (cement replacement, pozzolanic material)
- Scrap metal recycling (steel EAF scrap feed, copper recycling, aluminum can recycling)
- Acid and solvent regeneration (already partially exists as `chemistry.acid-regeneration`)
- Glass cullet recycling
- Ceramic waste and refractory recycling
- Tailings reprocessing (residual metal recovery from mine waste)
- Charcoal ash and biomass ash utilization (alkali source, fertilizer)
- Closed-loop water recycling (already in `chemistry.water-treatment`)
- Byproduct gas utilization (blast furnace gas, coke oven gas)

### 1.2 Explicitly OUT of Scope

- Waste disposal and end-of-pipe treatment → stays in `ehs.waste-management`
- Effluent monitoring and regulatory compliance → stays in `ehs.waste-management`
- Chemical safety and toxicology → stays in `ehs.chemical-safety`
- Emergency spill response → stays in `ehs.emergency-response`

### 1.3 Boundary with ehs/waste-management

The existing `ehs.waste-management` node (218 lines) covers semiconductor-specific waste treatment: HF neutralization, heavy metal precipitation, solvent incineration, TMAH degradation, and effluent monitoring. It is an end-of-pipe disposal document — converting hazardous waste into dischargeable effluent.

The proposed circular-economy scope is fundamentally different: converting industrial byproducts into **feedstock for new products**. The distinction is disposal vs. valorization. Where waste-management asks "how do we make this safe to discard?", circular-economy asks "how do we make this useful again?"

---

## 2. SIK Test — Three-Dimension Evaluation

### 2.1 Internal SIK Analysis

The SIK test evaluates whether technologies within the candidate domain share >50% overlap on each of three dimensions. We test this by comparing the subgroups within circular-economy to each other.

**Identified subgroups within proposed scope:**

| Subgroup | Representative Technologies | Key Equipment | Knowledge Base |
|----------|---------------------------|---------------|----------------|
| A: Metals recycling | Scrap sorting, EAF melting, copper electrolysis | Shredders, magnetic separators, EAF, electrolytic cells | Metallurgy, alloy chemistry |
| B: Slag/ash valorization | BF slag processing, fly ash pozzolan, phosphogypsum | Crushers, ball mills, kilns | Cement chemistry, mineralogy |
| C: Chemical recovery | Acid regeneration, solvent distillation, catalyst recovery | Distillation columns, ion exchange beds, reactors | Organic chemistry, separation science |
| D: Glass/ceramic recycling | Cullet melting, refractory reclamation | Glass furnaces, crushers | Glass science, ceramic engineering |
| E: Tailings reprocessing | Residual leaching, gravity separation, froth flotation | Ball mills, leach tanks, flotation cells | Mineral processing, hydrometallurgy |

#### Dimension 1: Physical Infrastructure Overlap

| Comparison | Shared Infrastructure | Overlap |
|-----------|----------------------|---------|
| A vs B | Crushers (shared); EAF vs kilns (different) | ~35% |
| A vs C | Minimal — smelters vs distillation columns | ~10% |
| A vs D | Furnaces broadly; but steel EAF ≠ glass furnace | ~25% |
| A vs E | Crushers, magnetic separators | ~40% |
| B vs C | Minimal — mills vs reactors | ~15% |
| B vs D | Kilns/furnaces; crushers | ~45% |
| B vs E | Crushers, ball mills | ~50% |
| C vs D | Minimal | ~10% |
| C vs E | Minimal — reactors vs mills | ~10% |
| D vs E | Crushers | ~20% |

**Average pairwise infrastructure overlap: ~26%**

**Verdict: FAIL** (< 50% threshold)

#### Dimension 2: Knowledge Base Overlap

| Comparison | Shared Knowledge | Overlap |
|-----------|-----------------|---------|
| A vs B | Some thermodynamics | ~25% |
| A vs C | Minimal — metallurgy vs organic chemistry | ~10% |
| A vs D | Thermal processing basics | ~20% |
| A vs E | Ore geology, extractive metallurgy | ~55% |
| B vs C | Minimal — cement chemistry vs organic chemistry | ~10% |
| B vs D | Silicate chemistry | ~40% |
| B vs E | Mineralogy | ~35% |
| C vs D | Minimal | ~10% |
| C vs E | Minimal | ~10% |
| D vs E | Minimal | ~15% |

**Average pairwise knowledge overlap: ~23%**

**Verdict: FAIL** (< 50% threshold)

#### Dimension 3: Practitioner Profile Overlap

| Comparison | Shared Skills/Training | Overlap |
|-----------|----------------------|---------|
| A vs B | Some process engineering | ~20% |
| A vs C | Minimal — metalworkers vs chemical engineers | ~10% |
| A vs D | Furnace operators broadly | ~20% |
| A vs E | Mining/metals engineers | ~50% |
| B vs C | Minimal | ~10% |
| B vs D | Materials engineers | ~35% |
| B vs E | Mining engineers | ~30% |
| C vs D | Minimal | ~10% |
| C vs E | Minimal | ~10% |
| D vs E | Minimal | ~10% |

**Average pairwise practitioner overlap: ~21%**

**Verdict: FAIL** (< 50% threshold)

### 2.2 SIK Summary

| Dimension | Score | Threshold | Verdict |
|-----------|-------|-----------|---------|
| Physical Infrastructure Overlap | ~26% | >50% | **FAIL** |
| Knowledge Base Overlap | ~23% | >50% | **FAIL** |
| Practitioner Profile Overlap | ~21% | >50% | **FAIL** |

**All three dimensions fail.** The proposed circular-economy domain lacks internal cohesion because "resource recovery" is not a single technology family — it is a **pattern** that manifests differently across metallurgy, chemistry, glass science, ceramics, and mining. The knowledge, equipment, and practitioner skills vary dramatically depending on which material stream is being recovered.

---

## 3. Split Rule Analysis (§6.3)

The split rule states: if identifiable subgroups share <50% infrastructure with the rest of the domain, consider splitting.

In this case, the SIK analysis reveals that **every subgroup** has <50% overlap with the others. This is not a domain with a single weak subgroup — it is a collection of unrelated subgroups that belong in their parent domains:

| Subgroup | Best Parent Domain | SIK Overlap with Parent |
|----------|-------------------|------------------------|
| Metals recycling | `metals` | ~65% (shares smelters, foundries, metallurgy knowledge) |
| Slag/ash valorization | `metals` or `chemistry.cement` | ~55% with metals, ~50% with chemistry |
| Chemical recovery | `chemistry` | ~70% (shares distillation, reactors, chem eng) |
| Glass/ceramic recycling | `glass` / `ceramics` | ~70% / ~60% (shares furnaces, kilns, materials science) |
| Tailings reprocessing | `mining` | ~65% (shares mills, flotation, mineral processing) |

Each subgroup has **higher** SIK overlap with its natural parent domain than with other circular-economy subgroups. This confirms that splitting is the correct action — and the split destination is the existing parent domains, not new domains.

---

## 4. Override Conditions Evaluation (§6.6)

### 4.1 Inter-Domain Coupling Override

**Question**: Would placing circular-economy capabilities in their parent domains create tight circular dependencies?

**Analysis**: No. The recovery capabilities follow the same dependency patterns as their parent domains:
- Scrap metal recycling requires metals infrastructure → natural `metals` capability
- Slag valorization requires blast furnace output → natural `metals.iron-steel.blast-furnace` child
- Acid regeneration already exists as `chemistry.acid-regeneration` with no circularity issues
- Glass cullet recycling requires glass furnaces → natural `glass` capability

No circular dependencies would result from distributing capabilities to parent domains.

**Override: NOT APPLICABLE**

### 4.2 Bootstrap Stage Override

**Question**: Are circular-economy technologies tightly coupled in the bootstrap sequence?

**Analysis**: No. Circular economy capabilities emerge at different bootstrap stages:
- Charcoal ash as alkali source: stone-age (early)
- Scrap iron re-melting: iron-age (medium)
- Slag cement: industrial (late)
- Solvent recovery: industrial (late)
- Tailings leaching: industrial (late)
- Silicon kerf recycling: semiconductor era (very late)

They are not coupled to each other in the bootstrap narrative. Each emerges when its parent domain matures enough to generate waste streams worth recovering.

**Override: NOT APPLICABLE**

---

## 5. Minimum Domain Size Check

Even if SIK passed, would the domain be large enough? Per §6.3, minimum is 2-3 capabilities with at least 1 process each.

A narrow circular-economy domain (excluding capabilities that clearly belong elsewhere) could have:
- `circular-economy.scrap-recycling` (capability) → with process `circular-economy.scrap-recycling.eaf-scrap-melting`
- `circular-economy.slag-valorization` (capability) → with process `circular-economy.slag-valorization.granulation`

This meets the minimum size but fails SIK — the two capabilities share only ~35% infrastructure and ~25% knowledge.

---

## 6. Differentiation from ehs/waste-management

The existing `ehs/waste-management` covers:

| Aspect | ehs/waste-management | Proposed circular-economy |
|--------|---------------------|--------------------------|
| Goal | Safe disposal, regulatory compliance | Resource recovery, value creation |
| Scale | Semiconductor fab (niche) | All industrial sectors (broad) |
| Outputs | Treated effluent, stabilized sludge | Reusable materials, construction feedstock |
| Knowledge | Environmental engineering, toxicology | Metallurgy, chemistry, materials science |
| Timeline | Years 30-70 (electronic era) | Years 5-200+ (all eras) |
| Edge type | Consumer of chemicals (treatment reagents) | Producer of materials (secondary feedstock) |

These are genuinely different functions. The differentiation is valid — but differentiation alone does not justify a domain. The circular-economy capabilities must still pass SIK internally, which they do not.

---

## 7. Proposed Node List (Hypothetical)

*If the domain were to pass SIK, these 6 nodes would be proposed. Since it fails, these become recommendations for parent-domain placement instead.*

| Proposed Node ID | Name | Level | Recommended Parent | Era |
|-----------------|------|-------|-------------------|-----|
| `circular-economy` | Circular Economy & Resource Recovery | domain | N/A (rejected) | — |
| `circular-economy.scrap-recycling` | Metal Scrap Recycling | capability | `metals` | industrial |
| `circular-economy.scrap-recycling.eaf-scrap` | EAF Scrap Melting | process | `metals.iron-steel` | industrial |
| `circular-economy.slag-valorization` | Slag & Ash Valorization | capability | `metals` or `chemistry.cement` | industrial |
| `circular-economy.slag-valorization.ground-granulated-slag` | Ground Granulated Blast Furnace Slag | process | `metals.iron-steel.blast-furnace` | industrial |
| `circular-economy.tailings-reprocessing` | Tailings Reprocessing | capability | `mining` | industrial |

---

## 8. Proposed Edge List (10+ edges to existing tree)

*These edges show how circular-economy nodes would connect to the existing tree. If distributed to parent domains, the same dependency relationships hold — only the node IDs change.*

### 8.1 Edges FROM circular-economy (what it depends on)

| # | From | To | Type | Rationale |
|---|------|----|------|-----------|
| 1 | `circular-economy.scrap-recycling` | `metals` | tool | Scrap recycling requires metallurgical infrastructure (furnaces, foundries) |
| 2 | `circular-economy.scrap-recycling` | `mining` | tool | Sorting equipment, magnetic separators derived from mining technology |
| 3 | `circular-economy.scrap-recycling.eaf-scrap` | `energy.electric-furnaces` | tool | EAF requires electric arc furnace technology |
| 4 | `circular-economy.scrap-recycling.eaf-scrap` | `chemistry.refractories` | material | Refractory linings consumed in EAF operation |
| 5 | `circular-economy.slag-valorization` | `metals.iron-steel` | tool | Slag is a byproduct of iron/steel production — requires the process to exist |
| 6 | `circular-economy.slag-valorization` | `chemistry` | tool | Chemical processing infrastructure for activation |
| 7 | `circular-economy.slag-valorization.ground-granulated-slag` | `energy.fuels` | material | Energy consumed in grinding and processing |
| 8 | `circular-economy.tailings-reprocessing` | `mining` | tool | Requires mining infrastructure (mills, flotation cells) |
| 9 | `circular-economy.tailings-reprocessing` | `chemistry.acids` | material | Leaching agents consumed in residual metal extraction |
| 10 | `circular-economy.tailings-reprocessing` | `machine-tools` | tool | Crushing and grinding equipment |

### 8.2 Edges TO circular-economy (what it enables)

| # | From | To | Type | Rationale |
|---|------|----|------|-----------|
| 11 | `construction` | `circular-economy.slag-valorization` | material | Slag cement used as construction material (GGBS in concrete) |
| 12 | `metals` | `circular-economy.scrap-recycling` | material | Recycled scrap provides secondary metal feedstock (reduces primary ore demand) |
| 13 | `chemistry.cement` | `circular-economy.slag-valorization` | material | GGBS replaces Portland cement clinker — material input to concrete |
| 14 | `silicon.mg-si-production` | `circular-economy.scrap-recycling` | material | Silicon scrap from wafering can be remelted for MG-Si |

**Total: 14 edges** (10 dependency edges + 4 enabling edges)

---

## 9. Final Verdict

| Criterion | Result |
|-----------|--------|
| Physical Infrastructure Overlap >50% | **FAIL** (~26%) |
| Knowledge Base Overlap >50% | **FAIL** (~23%) |
| Practitioner Profile Overlap >50% | **FAIL** (~21%) |
| Minimum domain size (2-3 capabilities) | PASS (3 capabilities identified) |
| Internal organizing axis definable | PASS (process chain: collect → sort → process → reuse) |
| Differentiation from ehs/waste-management | PASS (disposal vs. valorization) |
| Inter-domain coupling override | NOT APPLICABLE |
| Bootstrap stage override | NOT APPLICABLE |

### Overall: **FAIL**

The circular-economy concept fails the SIK Placement Test on all three primary dimensions. It is a **cross-cutting pattern** (resource recovery) that manifests across multiple existing domains, not a technology family with shared infrastructure, knowledge, and practitioners.

---

## 10. Recommendation

**Do not create a `circular-economy` domain.** Instead, add circular-economy capabilities as nodes within their natural parent domains:

| Capability | Recommended Placement | Rationale |
|-----------|----------------------|-----------|
| Metal scrap recycling | `metals.scrap-recycling` | Shares smelters, foundries, metallurgy with metals domain |
| EAF scrap melting | `metals.iron-steel.eaf-scrap-melting` | Extends existing iron-steel capability |
| Slag valorization | `metals.slag-valorization` | Blast furnace slag is a metals byproduct |
| Ground granulated slag | `metals.iron-steel.blast-furnace.ground-granulated-slag` | Child of blast furnace process |
| Tailings reprocessing | `mining.tailings-reprocessing` | Shares mineral processing infrastructure |
| Glass cullet recycling | `glass.cullet-recycling` | Shares glass furnaces and glass chemistry |
| Solvent recovery | `chemistry.solvent-recovery` | Shares distillation and separation equipment |
| Ash utilization | `chemistry.ash-utilization` or `ceramics.lime` | Ash is an alkali/pozzolanic source |

The existing `chemistry.acid-regeneration` node already demonstrates this pattern — it is correctly placed in `chemistry` rather than in a separate circular-economy domain.

### When to Revisit

If the tree accumulates 10+ scattered recovery nodes across multiple domains, a future SIK re-evaluation could consider whether a "resource-recovery" domain has emerged with sufficient internal cohesion. Currently, with 2-3 meaningful nodes, it is too early and too dispersed.

---

## 11. Appendix — Organizing Axis Analysis

Per §6.4, every domain must declare an organizing axis. If the domain were to pass SIK, the proposed axis would be:

**Axis: Process Chain** (collect → sort → process → reuse)

This mirrors the material flow through recovery systems. However, the "process" step varies so dramatically (smelting for metals, grinding for slag, distillation for solvents) that the axis provides only superficial coherence. A process chain axis works when the underlying transformations are similar (as in `silicon`: MG-Si → purification → crystal growth → devices). Here, the transformations are unrelated.
