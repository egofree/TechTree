# Bootciv Completeness Learnings

## 2026-05-24: Task 1 — GPU Dependency Chain

- `vlsi-scaling.eda-design` previously had only 1 edge (to `computing`). EDA tools also depend on semiconductor manufacturing: fab processes, silicon devices, and dopant/etch gases.
- Added 3 `tool`-type edges: `→ photolithography.fab-processes`, `→ silicon.basic-devices`, `→ chemistry.dopant-etch-gases`.
- The reachability path via `photolithography.fab-processes → chemistry.dopant-etch-gases → chemistry → metals → mining → foundations` confirms the GPU critical path is now connected.
- validate.sh passed 17/17 after changes.

## 2026-05-24: Task 2 — Stoichiometry Fixes in Chemistry Docs

- `dopant-etch-gases.md` line 11: Ca₃P₂ hydrolysis used 3H₂O instead of 6H₂O — unbalanced equation. Fixed to `Ca₃P₂ + 6H₂O → 2PH₃ + 3Ca(OH)₂`.
- `dopant-etch-gases.md` line 11: KPH₂O is not a valid formula. Fixed to KH₂PO₂ (potassium hypophosphite).
- `acids.md` line 107: H₂SO₄ distillation wording was misleading ("distilled at 337°C under reduced pressure" — 337°C is the atmospheric bp, not the vacuum distillation temperature). Reworded for clarity.
- Lesson: Even high-accuracy domains (9.2/10) need atom-balance verification on every equation.
- validate.sh passed 17/17 after changes.

## 2026-05-24: Water Domain Completeness (Task 7)

### Finding: Domain node descriptions often imply more capabilities than exist
The water domain description mentioned "Water supply, purification, desalination, and hydraulic systems" but only 1 of those 4 areas had a node. Checking domain descriptions against actual capability nodes is a good completeness audit method.

### Finding: Overlap between foundations and domain capabilities
`foundations.water-procurement` already existed as a stone-age capability. Adding `water.procurement` under the water domain is valid — foundations covers the basics, the domain capability covers systematic engineering. But be aware of potential redundancy when adding nodes.

### Finding: Content files can be brief but practical
The 50-line minimum for content files is achievable with practical detail (design parameters, construction methods, safety warnings). Real-world numbers (flow rates, pipe diameters, chemical dosages) add genuine value.

### Convention: Edge types for water infrastructure
- Procurement from raw materials → type: "material" (uses stone, wood, biomass)
- Distribution depending on procurement → type: "tool" (procurement provides infrastructure)
- Treatment depending on procurement → type: "tool" (procurement provides the water to treat)
- Sewage depending on distribution → type: "tool" (uses pipe/channel infrastructure)

## 2026-05-24: Task 4 — Electronics Orphaned Content Resolution

### Finding: SIK test clearly separates electronics from computing
Electronics and computing appear superficially related (both deal with electrons) but share <20% SIK overlap on all three dimensions. PCB assembly technicians and computer architects have fundamentally different training, tools, and knowledge.

### Finding: Domain-level edges should reflect aggregate dependencies
When creating a new domain, add domain-level edges for the most fundamental dependencies (metals, energy, chemistry, machine-tools) plus capability-level edges for specific supply chains (electronics.assembly → silicon.basic-devices, electronics.assembly → glass.fibers).

### Convention: Edge types for electronics
- Electronics → metals: "material" (copper consumed for traces/wire)
- Electronics → machine-tools: "tool" (precision equipment reused)
- Electronics → chemistry: "material" (etchants, flux consumed)
- Electronics → energy.electricity: "tool" (power infrastructure reused)
- electronics.assembly → silicon.basic-devices: "material" (devices consumed/installed)
- electronics.assembly → polymers.thermosets: "material" (FR-4, epoxy consumed)

## 2026-05-24: Task 8 — Gold & Silver Precious Metals Content

### Finding: Task-specified node IDs may not exist
The task specified edges to `metals.smelting`, but no such node exists. Adapted by using `metals` (domain-level) as the tool dependency for smelting infrastructure. Always verify referenced node IDs before adding edges.

### Finding: Precious metals have two distinct supply chains
Gold and silver follow fundamentally different production paths: gold is primarily extracted from dedicated ores via cyanidation, while silver is mainly a byproduct of lead-zinc and copper mining. These should be covered in the same capability node (precious metals) but the content must clearly distinguish the different extraction routes.

### Finding: Non-ferrous.md already covers Parkes process and silver-in-lead
The non-ferrous.md lead section (line 61) covers the Parkes process in detail. Precious-metals.md should reference but NOT duplicate this content. The SIK test confirms <20% overlap — precious metals refining (cyanidation, Wohlwill, Moebius) shares almost no infrastructure/knowledge with base metals smelting.

### Convention: Edge types for precious metals
- metals.precious-metals → metals: "tool" (smelting furnaces, crucibles reused)
- metals.precious-metals → chemistry: "material" (cyanide, acids consumed)
- metals.precious-metals → mining: "material" (ore consumed)
- metals.precious-metals → metals.non-ferrous: "tool" (Parkes process infrastructure reused)

### Finding: Duplicate closing brackets can appear in JSON edits
When editing edges.json near the end of the file, a previous edit left duplicate `]\n}` closings. Always validate JSON with `python3 -c "import json; json.load(open(...))"` after edits.
