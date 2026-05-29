# Sewage Collection & Treatment

> **Node ID**: water.sewage
> **Domain**: [Water](./index.md)
> **Dependencies**: [`water.distribution`](distribution.md), [`chemistry.cement`](../chemistry/cement.md)
> **Enables**: [`health.sanitation`](../health/sanitation.md), [`agriculture`](../agriculture/index.md)
> **Timeline**: Years 10-35
> **Outputs**: treated_wastewater, sewage_disposal, biogas
> **Critical**: Yes — cholera epidemics in 19th-century cities demonstrated that sewage management is a prerequisite for urban civilization at any scale

## Overview

Collection, conveyance, and treatment of wastewater and sewage. In any settled community, the volume of wastewater generated (drinking, cooking, washing, latrine flush) rapidly contaminates surface and groundwater sources if not managed. Cholera epidemics in 19th-century cities demonstrated that sewage management is not optional — it is a prerequisite for urban civilization at any scale.

A community of 1,000 people generates approximately 50-200 m³ of wastewater per day (50-200 liters per person per day). This wastewater contains pathogens (cholera, typhoid, E. coli, hepatitis, rotavirus, giardia, cryptosporidium, helminths), organic matter (200-400 mg/L biochemical oxygen demand), suspended solids (200-500 mg/L), and nutrients (nitrogen 20-50 mg/L, phosphorus 5-15 mg/L). Untreated discharge creates disease cycles: sewage contaminates water supply → population sickens → more sewage from sick population.

This capability covers the full range of sewage management from pit latrines (achievable from Year 0) through activated sludge treatment (requiring industrial infrastructure).

## Prerequisites

## Materials
- [Cement and concrete](../chemistry/cement.md) — for tanks, pipes, and treatment structures
- [Clay pipes](../ceramics/kilns.md) or [cast iron pipes](../metals/iron-steel.md) — for sewer networks
- Stone or brick — for tank and basin construction

## Tools
- Surveying instruments for pipe gradient control
- Digging tools for trench excavation
- Concrete forming and pouring tools

## Knowledge
- Basic hydraulics (flow, gradient, friction)
- Understanding of disease transmission pathways
- Anaerobic digestion principles

## Infrastructure
- [Water distribution](distribution.md) system (sewage volume correlates with water supply volume)

## Bill of Materials

| Material | Quantity per 1,000 people | Source | Alternatives |
|----------|--------------------------|--------|-------------|
| Concrete for tanks and basins | 20-100 m³ | [Chemistry: Cement](../chemistry/cement.md) | Stone or brick with mortar |
| Clay or concrete pipe (100-200 mm) | 500-2,000 m | [Ceramics](../ceramics/index.md) | Cast iron (higher pressure rating) |
| Gravel for leach fields | 10-50 m³ | Quarry or river | Crushed stone |
| Sand for filter beds | 20-100 m³ | Quarry or river | No substitute |

## Process Description

## Pit Latrines

The most basic sanitation facility. Achievable from Year 0 with no prerequisites beyond digging tools.

**Prerequisites**: Digging tools, basic construction materials for the shelter.

**Materials**: Timber or stone for the slab, thatch or timber for the shelter, rope for fly screen.

**Construction**:
1. Select site at least 30 m downhill from any water source (well, spring, river). Minimum 15 m from the nearest dwelling.
2. Excavate a pit 2-3 m deep, 1.0-1.5 m in diameter. In unstable soil, line the upper 0.5 m with stone or brick to prevent collapse.
3. Construct a squatting slab from reinforced concrete (preferred) or timber planks. Concrete slab: 1.2 × 1.2 m, 75-100 mm thick, with a 250 × 300 mm drop hole. Reinforce with bamboo or steel bars.
4. Place the slab over the pit, sealed at the edges with compacted earth. The slab must be stable — test by standing on each corner.
5. Construct a privacy shelter from thatch, timber, or corrugated metal.
6. For a VIP (ventilated improved pit) latrine: install a 100-150 mm diameter vent pipe (PVC, clay, or brick) from the pit to above the roofline. Cover the top with fly screen (0.5-1 mm mesh). The vent pipe creates an updraft that draws odors away and traps flies.

**Calibration**: A pit 1.2 m diameter × 3 m deep = 3.4 m³. At 0.06 m³ per person per year (solids accumulation rate), a pit serving a family of 6 fills in approximately 9 years.

**Expected performance**: Properly constructed pit latrines eliminate open defecation, the single most effective intervention for reducing fecal-oral disease transmission. VIP latrines reduce fly breeding by 90-95% and significantly reduce odor. Pathogen containment: effective if groundwater table is >2 m below pit bottom.

**Strengths**:
- Minimal technology — Year 0 capability
- Very low cost ($5-50 per latrine)
- No water required for operation
- Effective pathogen containment

**Weaknesses**:
- Not suitable for high water tables (pit floods)
- Not suitable for very dense settlements (insufficient space for new pits)
- Odor and fly nuisance without VIP design
- Requires periodic relocation or manual emptying
- Does not treat wastewater — only contains solids

## Septic Tanks

On-site treatment for settlements too small or dispersed for sewer networks.

**Prerequisites**: [Concrete construction](../chemistry/cement.md), [pipe materials](../ceramics/index.md), basic plumbing skills.

**Materials**: Concrete or brick for tank construction (2-3 chamber), PVC or clay pipe for inlet/outlet, gravel for leach field.

**Construction**:
1. Size the tank: minimum 1,000 liters per household. For 5 people at 100 L/person/day: 1,500-3,000 liters (1-2 days retention).
2. Construct a 2-3 chamber concrete tank. First chamber: 50% of total volume. Second chamber: 30%. Third chamber (optional): 20%. Internal walls have baffles (submerged ports) to prevent short-circuiting.
3. Install inlet T-pipe (submerged inlet) and outlet T-pipe (draws from 200-300 mm below surface, avoiding floating scum).
4. Connect outlet to a soakaway pit (1-2 m diameter, 2-3 m deep, filled with graded gravel) or leach field (gravel-filled trench with perforated pipe, 0.5-1.0 m wide × 10-30 m long per bedroom).
5. Seal tank cover tightly with concrete slab. Install access manholes over each chamber for desludging.

**Calibration**: After filling with water, check that flow passes through all chambers without short-circuiting. Add a dye tracer to the inlet and observe that it does not appear at the outlet for at least 24 hours.

**Expected performance**: Removes 30-50% of BOD, 50-70% of suspended solids, and 60-80% of pathogens by anaerobic digestion. Effluent still contains 100-250 mg/L BOD — not safe for direct discharge to surface water. Leach field provides additional soil-based treatment. Desludging required every 2-5 years.

**Strengths**:
- On-site treatment — no sewer network required
- Low operating cost (no energy input)
- Produces relatively clear effluent for soil disposal
- Proven technology — used worldwide for 150+ years

**Weaknesses**:
- Requires permeable soil for leach field (fails in clay)
- Not suitable for high water tables (groundwater contamination)
- Requires periodic desludging (tank must be accessible to pump truck or manual labor)
- Nutrient removal minimal — nitrogen and phosphorus pass through

## Simplified Sewerage

Low-cost sewer networks for dense settlements.

**Prerequisites**: [Concrete](../chemistry/cement.md), [clay or plastic pipe](../ceramics/index.md), surveying tools, organized labor force.

**Materials**: 100 mm minimum diameter pipe (clay, concrete, or PVC), cement mortar for joints, concrete for manholes.

**Construction**:
1. Lay pipe at 0.5% minimum gradient. Shallower trenches than conventional sewers reduce excavation cost by 40-60%.
2. Install manholes at junctions, direction changes, and every 50-80 m for inspection and blockage removal. Manholes: 0.6-1.0 m diameter, brick or concrete rings.
3. Seal all joints with cement mortar or rubber ring gaskets to prevent groundwater infiltration and root intrusion.
4. Install vent pipes at building connections and main junctions to prevent sewer gas (hydrogen sulfide) buildup.
5. Connect each building to the main sewer with a 100 mm branch, including a P-trap or U-trap to prevent sewer gas from entering buildings.

**Calibration**: After construction, test by flushing with water from upstream manholes. Verify flow at the downstream end. Check all manholes for standing water (indicates blockage or inadequate gradient).

**Expected performance**: Conveys 50-200 L/person/day of wastewater to a central treatment facility. Pipe design life: 50+ years for clay, 30+ years for PVC. Requires periodic cleaning (every 1-5 years depending on usage).

**Strengths**:
- Serves dense settlements where pit latrines are impractical
- Centralized collection enables central treatment
- Lower cost than conventional sewerage (smaller pipes, shallower trenches)

**Weaknesses**:
- Requires organized construction and maintenance
- Blockages occur if solids or grease are discharged
- Requires downstream treatment facility
- Not gravity-feasible in very flat terrain without lift stations

## Waste Stabilization Ponds

The simplest secondary treatment — large shallow ponds relying on natural biological processes. Ideal for early-stage civilization.

**Prerequisites**: Land area (5-10 m² per person served), [earthworks capability](../construction/index.md), warm climate (most effective above 20°C).

**Materials**: Earth excavation equipment or manual labor, liner (clay or HDPE if soil is permeable), fencing.

**Construction**:
1. Excavate facultative ponds 1-2 m deep. Surface area: 5-10 m² per person served. For 1,000 people: 5,000-10,000 m² (0.5-1.0 hectares).
2. Construct embankments from excavated material, compacted to 95% standard Proctor density. Embankment slope: 1:2 (vertical:horizontal) on inner face, 1:1.5 on outer face.
3. Line the pond bottom with compacted clay (200-300 mm) if native soil is permeable. Target permeability <1 × 10⁻⁷ m/s.
4. Install inlet structure (submerged inlet to prevent short-circuiting) and outlet structure (draws from 200-300 mm below surface).
5. Construct maturation ponds downstream: 0.5-1.0 m deep, 50-100% of facultative pond area. These provide UV disinfection from sunlight.
6. Fence the entire pond area to exclude humans and animals. Post warning signs — pond water is not safe for contact.

**Calibration**: Fill ponds and let them develop biological activity over 4-8 weeks. Test effluent: BOD should be <30 mg/L (from influent 200-400 mg/L). Fecal coliforms should be <1,000 per 100 mL after maturation pond.

**Expected performance**: 80-99% pathogen removal, 70-90% BOD removal, 50-80% suspended solids removal. Residence time: 3-15 days in facultative pond, 5-15 days in maturation pond. Zero energy input (gravity flow). Zero chemical input. Minimal maintenance (annual desilting, embankment repair).

**Strengths**:
- Zero energy — entirely passive treatment
- Zero chemicals required
- Very low maintenance
- Very effective pathogen removal (80-99%)
- Proven at municipal scale in warm climates worldwide

**Weaknesses**:
- Large land area required (5-10 m² per person)
- Less effective in cold climates (biological activity slows below 10°C)
- Algae in effluent increases suspended solids
- Odor from anaerobic zones (setback distance 200+ m from housing)
- Mosquito breeding if embankments are not maintained

## Activated Sludge Process

The most common secondary treatment method in industrialized nations. Requires energy and mechanical equipment.

**Prerequisites**: [Electrical power](../energy/electricity.md), mechanical aerators or blowers, [concrete construction](../chemistry/cement.md).

**Materials**: Concrete for aeration tanks and clarifiers, steel for mechanical equipment, air diffusers or surface aerators.

**Construction and operation**:
1. Construct aeration tank: 4-8 hour hydraulic residence time at design flow. Depth: 3-5 m. Width: 3-10 m.
2. Install aeration equipment: mechanical surface aerators (3-5 kW per 1,000 m³ tank volume) or diffused air blowers with fine-bubble diffusers at the tank bottom.
3. Construct secondary clarifier (settling tank): surface loading rate 15-30 m³/m²/day, depth 3-5 m.
4. Operate by maintaining a mixed liquor suspended solids (MLSS) concentration of 2,000-5,000 mg/L in the aeration tank. Microorganisms consume organic matter; the clarifier settles the biological floc.
5. Return settled sludge (return activated sludge, RAS) to the aeration tank inlet. Waste excess sludge (WAS) to maintain MLSS balance.

**Expected performance**: Removes 85-95% of BOD, 85-95% of suspended solids. Energy: 0.5-1.5 kWh per kg BOD removed. Produces excess sludge requiring separate treatment (anaerobic digestion, dewatering, composting).

**Strengths**:
- High treatment efficiency (85-95% BOD removal)
- Compact footprint (compared to stabilization ponds)
- Well-controlled process adjustable to varying loads
- Proven at all scales from 100 to 1,000,000+ people

**Weaknesses**:
- High energy consumption (aeration is the largest energy user)
- Requires continuous power — shutdown >4 hours kills the biological community
- Mechanically complex — blowers, pumps, and controls need maintenance
- Produces large volumes of waste sludge requiring treatment
- Not feasible without reliable electricity

## Quantitative Parameters

| Parameter | Pit latrine | Septic tank | Stabilization pond | Activated sludge |
|-----------|------------|------------|-------------------|-----------------|
| BOD removal | N/A (containment) | 30-50% | 70-90% | 85-95% |
| Pathogen removal | Containment | 60-80% | 80-99% | 90-99% |
| Energy required | None | None | None | 0.5-1.5 kWh/kg BOD |
| Land area | 2 m² | 5-10 m² | 5-10 m²/person | 0.1-0.5 m²/person |
| Cost per person | $5-50 | $100-500 | $20-100 | $200-1,000 |
| Skill level | Very low | Low | Low | High |
| Scale | Household | Household | Community+ | Town+ |

## Scaling Notes

- **Household scale** (1-10 people): Pit latrine or septic tank. No external infrastructure. Cost: $5-500.
- **Village scale** (50-500 people): Simplified sewerage to stabilization ponds. Requires community organization for construction and maintenance. Cost: $5,000-50,000.
- **Town scale** (2,000-20,000 people**: Sewer network with trickling filter or activated sludge treatment. Requires organized water utility and continuous power. Cost: $500,000-5,000,000.
- **City scale** (100,000+ people): Full sewer network with activated sludge and anaerobic sludge digestion (produces biogas: 60-70% methane). Requires industrial-scale infrastructure.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Septic tank effluent surfacing in yard | Leach field clogged with solids or biomat; high water table; impermeable soil | Pump septic tank to reduce load. Install new leach field in parallel (rest the old one). If soil is impermeable, convert to raised mound system. |
| Sewer blockage | Grease accumulation; root intrusion; debris; inadequate gradient | Rod or jet the blocked section. Remove tree roots. Increase gradient if consistently blocking. Install grease traps at food service connections. |
| Stabilization pond turning septic (black water, foul odor) | Organic overload; inadequate pond depth; poor inlet distribution | Reduce organic loading (pre-treat or divert some flow). Check pond depth — should be 1-2 m (shallower ponds overheat; deeper ponds go fully anaerobic). Redistribute inlet flow. |
| Activated sludge not settling (bulking) | Filamentous bacteria dominating; low food-to-microorganism ratio; low dissolved oxygen | Increase dissolved oxygen to >2 mg/L. Add chlorine or hydrogen peroxide to selectively kill filamentous organisms. Adjust wasting rate to change F/M ratio. |
| Biogas production low from digester | Temperature below 30°C; toxic inhibition (heavy metals, antibiotics); insufficient retention time | Heat digester to 35°C (mesophilic range). Test feed for toxic compounds. Increase retention time to 15-30 days. |
| Sewer gas (H₂S) in buildings | Dry P-trap allowing gas to pass; blocked vent pipe; cracked sewer pipe | Pour water into all drains to refill P-traps. Clear vent pipes on roof. Inspect and repair cracked pipes. H₂S at 100 ppm is immediately dangerous; at 10 ppm causes eye irritation. |

## Safety

- **Hydrogen sulfide (H₂S)**: Sewer gas is a lethal hazard. H₂S paralyzes the olfactory nerve at concentrations above 100 ppm — victims cannot smell it and lose consciousness rapidly. IDLH: 100 ppm. Fatal at 300-500 ppm for 5-10 minutes. Never enter a confined sewer space without testing with a gas detector or lowered candle. Ventilate before entry. Use a safety harness with a surface attendant.
- **Sewage pathogens**: Raw sewage contains 10⁶-10⁸ fecal coliforms per 100 mL. Contact with broken skin or mucous membranes transmits disease. Wear waterproof gloves and boots when handling sewage or maintenance equipment. Wash hands thoroughly after any contact.
- **Methane explosion**: Anaerobic digestion produces biogas (60-70% methane). Methane is explosive at 5-15% concentration in air. Never use open flames or spark-producing tools near digesters or covered tanks without gas testing. Vent all enclosed spaces before entry.
- **Gases in deep manholes**: Carbon dioxide (heavier than air, displaces oxygen), methane (lighter, explosive), and hydrogen sulfide all accumulate in deep manholes. Test atmosphere before entry. If a lowered candle extinguishes, the atmosphere will not support human respiration.
- **Structural collapse**: Deep excavation for sewer trenches and tank construction is subject to cave-in. Shore any trench deeper than 1.5 m. Keep spoil piles at least 0.5 m back from trench edge.

## Quality Control

- **BOD test**: Measure biochemical oxygen demand of influent and effluent. Target: <30 mg/L BOD in effluent (95% reduction from raw sewage at 200-400 mg/L). Standard 5-day BOD test (BOD₅) requires incubation at 20°C for 5 days.
- **Suspended solids**: Target <30 mg/L total suspended solids in effluent. Simple gravimetric test: filter a known volume through a pre-weighed filter paper, dry at 105°C, re-weigh.
- **Fecal coliforms**: Target <1,000 per 100 mL for stabilization pond effluent. Membrane filtration test: filter sample, incubate on selective media at 44.5°C for 24 hours, count colonies.
- **Visual inspection**: Treated effluent should be light green (from algae in ponds) or clear (from activated sludge). Dark grey or black indicates inadequate treatment. Regular checks of pond color, aeration tank foam, and clarifier clarity provide early warning of process upsets.

## Variations and Alternatives

- **Trickling filters**: Lower energy alternative using beds of stone or plastic media. Sewage trickles over the stone surface; biological film consumes organic matter. Removes 70-90% BOD. Energy: only pumping to the top of the filter. Advantage over activated sludge: no aeration blowers. Limitation: less controllable, fly and odor nuisance if overloaded.
- **Anaerobic digestion**: Heated (35°C) enclosed tanks digest primary and waste activated sludge. 15-30 day retention. Produces biogas (60-70% methane) usable for heating and power generation. Reduces sludge volume by 30-50%. Valuable co-product: biogas at 22 MJ/m³ heating value.
- **Constructed wetlands**: Emergent aquatic plants (reed, cattail, bulrush) growing in gravel beds treat wastewater through plant uptake and rhizosphere microbial activity. BOD removal 70-90%, pathogen removal 90-99%. Land area: 2-5 m² per person. Aesthetic and ecological co-benefits.
- **Composting toilets**: Waterless systems that aerobically decompose feces and urine with carbon-rich bulking material (sawdust, straw). Produces compost suitable for non-food agriculture. No water or sewer infrastructure required. Suitable for water-scarce areas.

## References

- [Water Distribution](distribution.md) — pipe and channel construction skills transfer to sewage collection
- [Chemistry: Cement & Concrete](../chemistry/cement.md) — tanks, pipes, and treatment structures
- [Ceramics](../ceramics/index.md) — clay pipes and tank linings
- [Health: Sanitation](../health/sanitation.md) — sewage treatment is the infrastructure backbone of public sanitation
- [Agriculture](../agriculture/index.md) — treated effluent and composted sludge for irrigation and fertilization


[← Back to Water](index.md)
