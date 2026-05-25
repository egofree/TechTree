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

## 2026-05-24: Task 15 — Vacuum Technology Domain Creation

### Finding: SIK test clearly separates vacuum from gas-handling
Vacuum and gas-handling share only ~25-30% overlap on infrastructure and knowledge dimensions. Despite both dealing with gas-phase physics, vacuum engineering (gas REMOVAL, controlled atmospheres, UHV) is fundamentally different from gas handling (gas DISTRIBUTION, positive pressure, safety). The SIK test correctly identifies this separation.

### Finding: Existing content can be elevated to a new domain without deletion
The gas-handling/vacuum.md file (215 lines) was not deleted. It remains as a foundational reference. The new vacuum domain adds complementary content at a deeper technical level (UHV pumps, detailed specs tables, chamber design calculations, RGA diagnostics). Cross-references between gas-handling/vacuum.md and vacuum domain files prevent duplication.

### Convention: Edge types for vacuum domain
- vacuum → gas-handling: "tool" (gas distribution infrastructure reused)
- vacuum → energy.electricity: "tool" (power for pumps and instruments reused)
- vacuum → metals: "material" (stainless steel, copper consumed for chambers and gaskets)
- vacuum → measurement: "tool" (calibration infrastructure reused)
- vacuum.pumps → machine-tools: "tool" (precision manufacturing for pump components reused)
- vacuum.chambers → machine-tools: "tool" (precision manufacturing for chamber components reused)
- vacuum.chambers → metals: "material" (stainless steel consumed for chamber construction)
- silicon.basic-devices → vacuum.pumps: "tool" (vacuum systems reused for deposition)
- photolithography.fab-processes → vacuum.pumps: "tool" (vacuum systems reused for fab processes)

### Finding: Content files with specific technical parameters add genuine value
Including specific pressure ranges (Torr, Pa, mbar), pump speeds (CFM, L/s), materials (SS 304L, 316L, OFHC copper), and specifications tables transforms content from descriptive to actionable. This level of detail matches the technical depth of existing domain content files.

## 2026-05-25: Task — Telecommunications Domain Population

### Finding: SIK test clearly separates telecom from transport
Telecommunications and transport share <25% infrastructure overlap. Transport moves physical goods (roads, railways, ships, aircraft); telecom moves information (telegraph, telephone, radio, cables). The only significant intersection is railway block signaling, which is telegraph-based but serves transport safety. Knowledge overlap <15%; practitioner overlap <10%. Result: clearly separate domains.

### Finding: transport.telegraph has deep existing content
transport/telegraph.md is 226 lines covering hardware (keys, sounders, batteries), pole-line construction, Morse code, telephone basics, and wireless telegraphy. The telecom domain should NOT duplicate this content. Solution: telecom.electric-telegraph cross-references transport/telegraph.md and focuses on network architecture (routing, multiplexing, block signaling) rather than hardware.

### Convention: Edge types for telecommunications domain
- telecom → energy.electricity: "tool" (power infrastructure reused)
- telecom → metals: "material" (copper wire consumed)
- telecom → knowledge.writing: "tool" (encoding systems reused)
- telecom → glass: "material" (glass insulators consumed)
- telecom → transport.telegraph: "tool" (existing telegraph infrastructure reused)
- telecom → polymers.rubber.gutta-percha: "material" (cable insulation consumed)
- telecom.submarine-cables → transport.shipping: "tool" (cable-laying ships reused)

### Finding: Directory name must match domain node ID
The validator check 3a expects `docs/{domain_id}/` to match the node ID. The telecom domain node ID is `telecom`, so the content directory is `docs/telecom/` (not `docs/telecommunications/`). The docs/index.md link must also point to `telecom/index.md`.

### Finding: Content files need specific technical parameters at ≥150 lines
All 5 capability files needed ≥150 lines with specific parameters:
- pre-electric: visibility ranges, semaphore station costs, heliograph mirror sizes
- electric-telegraph: multiplexing specs, block circuit parameters, traffic statistics
- telephone: carbon microphone specs, Strowger exchange capacity, loading coil parameters
- submarine-cables: gutta-percha dielectric strength, cable resistance/capacitance per km
- radio: spark-gap power ranges, crystal detector sensitivity, vacuum tube specifications

### Finding: 23 edges added (6 domain-level + 17 capability-level)
Total edges went from 572 to 595. The capability-level edges create a coherent dependency chain: pre-electric → electric-telegraph → telephone, submarine-cables, radio. This mirrors the chronological organizing axis.

### Finding: validate.sh passed 17/17 after all changes
No issues with node IDs, edge references, tag values, hierarchy, or DAG structure. The telecom domain integrates cleanly with the existing tech tree.

## 2026-05-25: Task — Food Processing Domain Population

### Finding: SIK test clearly separates food-processing from foundations.food-agriculture
Food processing and agriculture share <25% infrastructure overlap on all three SIK dimensions. Agriculture uses fields, plows, and irrigation. Food processing uses mills, canneries, and cream separators. Despite both dealing with food, the practitioners, knowledge bases, and physical infrastructure are fundamentally different. Stone-age drying/salting is a food processing technique that depends on (but is separate from) agricultural output.

### Finding: SIK test clearly separates food-processing from chemistry.fermentation
Despite both using fermentation, food processing (brewing, pickling, yogurt) and industrial fermentation chemistry (ethanol/acetone production) share <30% overlap. Food technologists focus on food safety, organoleptic properties, and preservation. Chemical engineers focus on yield, purity, and industrial solvent production. Cross-reference but do not duplicate.

### Finding: chemistry.fermentation node doesn't exist as a standalone
The fermentation content lives under `chemistry.petroleum-alternatives.fermentation` (a process node). When creating edges referencing fermentation, use this full ID, not a hypothetical `chemistry.fermentation`. Always verify node IDs with `jq -r '.nodes[].id' data/nodes.json | grep pattern`.

### Convention: Edge types for food processing
- food-processing → foundations.food-agriculture: "material" (raw food consumed as feedstock)
- food-processing → energy: "tool" (mill power, steam for canning, electricity for refrigeration — reusable infrastructure)
- food-processing → health.sanitation: "tool" (food safety knowledge, hygiene protocols — reusable knowledge)
- food-processing → water: "material" (water consumed in processing)
- food-processing.preservation → ceramics: "material" (storage vessels, jars consumed over time)
- food-processing.preservation → chemistry.petroleum-alternatives.fermentation: "tool" (fermentation knowledge reused)
- food-processing.brewing → chemistry.petroleum-alternatives.fermentation: "tool" (same fermentation knowledge)

### Finding: Content files for food processing need expansion beyond 100 lines
Initial drafts of milling.md (101 lines), preservation.md (115 lines), dairy.md (114 lines), and brewing.md (119 lines) were below the 150-line threshold. Adding sections on equipment construction, byproducts, quality control, and biochemical details brought all files above 150 lines. The content quality bar from chemistry/acids.md (221 lines) should be the aspiration.

### Finding: validate.sh may show transient failures from concurrent writes
The telecom domain showed as having no .md files on first validation run, but files clearly exist. On re-run, 17/17 passed. This suggests concurrent file creation (another task populating telecom) caused a transient check-3 failure. Always re-run validate.sh before concluding there's a real problem.

## 2026-05-25: Task — Marine Domain Population

### Finding: SIK test clearly separates marine from transport.shipping
Marine and transport.shipping share only ~20% SIK overlap. transport.shipping covers operational aspects (navigation, cargo, canals); marine covers engineering/construction (hull design, propulsion machinery, harbor infrastructure, submarine cables). Despite both involving ships, the infrastructure, knowledge, and practitioners are fundamentally different. Key distinction: transport.shipping USES ships; marine BUILDS, DESIGNS, and MAINTAINS them.

### Convention: Edge types for marine domain
- marine → foundations: "tool" (basic tools and fire for earliest boat building)
- marine → metals: "material" (iron/steel consumed for hulls, fasteners, anchors)
- marine → textiles: "material" (sailcloth, rope consumed for rigging)
- marine → energy: "tool" (propulsion systems reused)
- marine → knowledge: "tool" (writing, math for charts and calculations)
- marine → transport.shipping: "tool" (shipping operational knowledge reused)
- marine.shipbuilding → metals.iron-steel: "material" (iron/steel plates consumed for hulls)
- marine.shipbuilding → transport.shipping: "tool" (shipbuilding knowledge reused)
- marine.shipbuilding → machine-tools: "tool" (precision manufacturing reused)
- marine.navigation → knowledge.writing: "tool" (charts and calculations)
- marine.navigation → metals: "material" (metals consumed for instruments)
- marine.propulsion → energy.steam-power: "tool" (steam engine technology reused)
- marine.propulsion → energy.engine: "tool" (IC engine technology reused)
- marine.propulsion → metals.iron-steel: "material" (steel consumed for engines and propellers)
- marine.infrastructure → metals.iron-steel: "material" (steel consumed for construction)
- marine.infrastructure → machine-tools: "tool" (precision manufacturing reused)
- marine.infrastructure → polymers.rubber.gutta-percha: "material" (gutta-percha consumed for cable insulation)

### Finding: Cross-referencing prevents content duplication
The existing transport/shipping.md (251 lines) already covers boat construction, sailing rigs, navigation, harbors, and propulsion in detail. Marine domain content must cross-reference shipping.md for operational content and focus on engineering/construction details not covered there. This approach: (1) avoids duplication, (2) leverages existing content, (3) adds genuinely new information.

### Finding: Concurrent agents may add nodes that temporarily break validation
Other agents added telecom, defense, construction, and food-processing domains concurrently. These nodes temporarily broke check 3 (node-doc correspondence) because the docs directories weren't yet created. Re-running validation after the other agents completed showed 17/17 passing. When multiple agents modify nodes.json simultaneously, there's a window where validation can fail temporarily.

## 2026-05-25: Task — Construction Domain Population

### Finding: SIK test clearly separates construction from ceramics.lime and chemistry.cement
Construction vs ceramics.lime + chemistry.cement: ~17% average overlap across Shared Infrastructure (~25%), Shared Knowledge (~15%), and Shared Practitioner (~10%) dimensions. Well below the 50% threshold. Lime/cement chemistry is a subset of construction knowledge, but structural engineering, timber framing, and building design are fundamentally different domains.

### Finding: Content must cross-reference rather than duplicate cement/lime content
The ceramics/lime.md (261 lines) and chemistry/cement.md (231 lines) already cover mortar and concrete chemistry in detail. The construction domain content files should reference these for mix designs and chemistry, focusing instead on structural application: beam sizing, foundation design, machine foundations, vibration isolation, roofing, and scaffolding.

### Finding: Specific technical parameters are the quality differentiator
Including Euler buckling formulas, beam load tables (steel IPE sections, timber sizes, RC beam sizing), concrete mix ratios for industrial use, rebar specifications, soil bearing capacity values, vibration isolation design examples, and crane runway beam requirements makes the content actionable rather than descriptive.

### Convention: Edge types for construction domain
- construction → foundations: "tool" (basic building knowledge and techniques reused)
- construction → ceramics.lime: "material" (lime for mortar consumed in construction)
- construction → chemistry.cement: "material" (cement for concrete consumed)
- construction → metals: "material" (structural steel consumed)
- construction → textiles.rope-making: "material" (rope for scaffolding/hoisting consumed)
- construction → machine-tools: "tool" (precision cutting equipment reused)
- construction.building-materials → foundations.tools-basic: "tool" (basic tools reused)
- construction.structural-engineering → metals.iron-steel: "material" (steel consumed for structural members)
- construction.industrial-buildings → energy.electricity: "tool" (power infrastructure reused)

### Finding: Directory alias mismatches between node IDs and docs directories
The telecom domain node ID is `telecom` but docs were in `docs/telecommunications/`. Check 3 (node-doc correspondence) fails when non-domain nodes exist under a domain whose directory name doesn't match the node ID. Renaming `docs/telecommunications/` to `docs/telecom/` resolves this. Lesson: always match the docs directory name to the domain node ID exactly.
