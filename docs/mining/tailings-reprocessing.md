# Tailings Reprocessing

> **Node ID**: mining.tailings-reprocessing
> **Domain**: [Mining Engineering](./index.md)
> **Dependencies**: [`Mining Extraction`](extraction.md), [`Ore Processing`](processing.md), [`Mineral Acids`](../chemistry/acids.md), [`Machine Tools`](../machine-tools/index.md)
> **Enables**: [`Mining`](./index.md), [`Metals`](../metals/index.md), [`Chemistry`](../chemistry/index.md)
> **Timeline**: Years 25-60+
> **Outputs**: residual_metals, reprocessed_concentrate, backfill_material, construction_sand
> **Critical**: No — improves resource efficiency but does not unlock new capabilities

## 1. Overview

Tailings reprocessing recovers residual metals, minerals, and useful materials from mine waste — the finely ground rock left after initial ore processing. Historical mines often left tailings containing 20–60% of the original metal value because the extraction technology of the day was insufficient to recover it. Modern techniques can extract this stranded value.

Mine tailings are the largest industrial waste stream by volume on Earth. A typical hard-rock mine produces 1–10 tonnes of tailings per tonne of concentrated ore. These tailings piles, impoundments, and slag heaps represent both an environmental liability and a resource opportunity. Reprocessing serves two goals simultaneously: recover valuable materials and reduce the environmental footprint of the tailings deposit.

This capability does not replace primary mining — it supplements it. Reprocessing is economically attractive when:
- The tailings contain metals that have increased in value since original mining
- New extraction technology (e.g., pressure leaching, bioleaching) can recover metals that older methods missed
- Environmental remediation of the tailings deposit is required anyway

The boundary between tailings reprocessing and primary ore processing is that tailings material has already been crushed and ground — the energy-intensive comminution step is already done. This gives tailings a processing cost advantage of 20–40% compared to fresh ore.

## 2. Prerequisites

### Materials

| Material | Specification | Source |
|----------|--------------|--------|
| Mine tailings | Accessible tailings deposit with assay data | Existing mine waste (historical or active) |
| Leaching agents | H₂SO₄, HCl, NaOH, NaCN, or biological culture | [Mineral Acids](../chemistry/acids.md), [Alkalis](../chemistry/alkalis.md) |
| Flocculants and collectors | Xanthates, frothers, anionic polymers | [Chemistry](../chemistry/acids-bases.md) |
| Water | 2–10 m³ per tonne of tailings processed | [Water Treatment](../chemistry/water-treatment.md) |
| Energy | 15–50 kWh per tonne processed | [Energy](../energy/engine.md) |

### Tools & Equipment

| Equipment | Purpose | Source |
|-----------|---------|--------|
| Ball mill or regrind mill | Further size reduction if needed | [Machine Tools](../machine-tools/index.md) |
| Hydrocyclones and classifiers | Size classification | [Ore Processing](processing.md) |
| Flotation cells | Mineral separation by surface chemistry | [Ore Processing](processing.md) |
| Leach tanks (agitated) | Chemical dissolution of metals | [Metals](../metals/index.md) |
| Thickeners and filters | Solid-liquid separation | [Chemistry](../chemistry/acids-bases.md) |
| Solvent extraction or ion exchange | Metal purification from leach solutions | [Chemistry](../chemistry/acids-bases.md) |

### Knowledge

- Assay and characterization of tailings material (grade, mineralogy, particle size distribution)
- Hydrometallurgy: leaching chemistry, solvent extraction, precipitation
- Flotation circuit design for fine particles (tailings are typically finer than run-of-mine ore)
- Tailings dam stability and geotechnical assessment for safe excavation

## 3. Bill of Materials

### BOM: Copper Tailings Leaching (per tonne of tailings at 0.3% Cu)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Copper tailings | 1,000 kg (0.3% Cu = 3 kg Cu) | Mine waste deposit | N/A — feedstock |
| Sulfuric acid (H₂SO₄) | 15–40 kg | [Mineral Acids](../chemistry/acids.md) | Bioleaching (slower, no acid purchase) |
| Oxidant (air/O₂ or Fe³⁺) | 5–15 kg Fe²⁺/tonne recycled | Ferric iron in solution | Hydrogen peroxide (costly) |
| Flocculant | 10–50 g | [Chemistry](../chemistry/acids-bases.md) | Settling pond (slower, larger footprint) |
| Limestone (neutralization) | 20–60 kg | [Lime](../ceramics/lime.md) | Caustic soda (more expensive) |
| Water | 3–8 m³ | [Water Treatment](../chemistry/water-treatment.md) | Recycled process water |
| Electricity | 15–30 kWh | [Energy](../energy/engine.md) | Diesel generator |

### BOM: Gold Tailings Retreatment (per tonne of tailings at 0.8 g/t Au)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Gold tailings | 1,000 kg (0.8 g Au = 0.8 g) | Mine waste deposit | N/A — feedstock |
| Sodium cyanide (NaCN) | 0.2–0.5 kg | [Chemistry](../chemistry/acids-bases.md) | Thiosulfate (less toxic, more expensive) |
| Hydrated lime (pH modifier) | 2–8 kg | [Lime](../ceramics/lime.md) | Caustic soda |
| Activated carbon | 0.5–2.0 kg (regenerable) | [Chemistry](../chemistry/acids-bases.md) | Zinc precipitation (Merrill-Crowe) |
| Oxygen or air | 0.1–0.5 m³ | [Air Separation](../chemistry/air-separation.md) | Compressed air |
| Water | 2–5 m³ | [Water Treatment](../chemistry/water-treatment.md) | Recycled from tailings pore water |

## 4. Process Description

### 4.1 Flotation Retreatment of Sulfide Tailings

1. **Excavate and re-slurry.** Dig tailings from the impoundment using front-end loaders or hydraulic mining (monitors). Slurry with water to 30–40% solids in a sump pump. Screen at 2–5 mm to remove oversized debris and trash.

2. **Deslime.** Remove ultra-fine particles (<10 μm) by hydrocyclone. These slimes consume reagents without floating and reduce concentrate grade. Desliming improves flotation recovery by 10–20 percentage points.

3. **Condition with reagents.** Add collectors (xanthates at 50–200 g/tonne), frothers (MIBC at 20–80 g/tonne), and pH modifier (lime to pH 8–10) in conditioning tanks. Agitate 3–10 minutes for reagent adsorption onto mineral surfaces.

4. **Rougher flotation.** Feed slurry to rougher flotation cells (mechanical agitation, 10–30 cells in series). Air bubbles carry sulfide particles to the surface. Skim froth concentrate. Typical recovery: 60–80% of remaining sulfide minerals.

5. **Cleaner flotation.** Re-grind rougher concentrate to 20–40 μm (liberate locked particles) and float again in cleaner cells. Two to three cleaning stages produce a concentrate at commercial grade.

6. **Dewater and dispatch.** Thicken and filter the final concentrate to 8–12% moisture. Ship to smelter. Process tailings from the flotation circuit are re-deposited in a engineered facility.

**Strengths**:
- Tailings are already crushed and ground — saves 20-40% processing cost vs. primary ore
- Desliming and regrinding improve flotation recovery by 10-20 percentage points over original processing
- Proven circuit design (rougher → scavenger → cleaner) adapts directly from primary flotation practice

**Weaknesses**:
- Fine particles (<10 μm) consume reagents without floating — desliming loses some contained metal
- Tailings impoundment excavation can destabilize the dam structure if not geotechnically engineered
- Recovered concentrate grade may be lower than primary ore due to complex mineral locking

### 4.2 Acid Leaching of Metal-Bearing Tailings

1. **Characterize the tailings.** Assay for target metals (Cu, Zn, Co, Ni, REE). Determine mineralogy (oxide vs. sulfide), acid consumption (carbonate content), and permeability. High carbonate tailings (>5% CaCO₃) consume excessive acid — consider alkaline leaching instead.

2. **Build leach pad or tank leach.** For large volumes (>100,000 tonnes), construct a lined leach pad and heap-leach. For smaller volumes or high-value metals, use agitated tank leaching (2–6 tanks in series, 24–96 hour residence time).

3. **Leach with dilute sulfuric acid.** Pump 5–20 g/L H₂SO₄ solution onto/through the tailings. Maintain pH 1.5–2.5. Add oxidant (air, oxygen, or Fe³⁺) to keep metals in solution. Temperature: ambient to 50°C (heated leach improves kinetics). Leach duration: 30–120 days (heap) or 24–96 hours (tank).

4. **Collect pregnant leach solution (PLS).** Drain leach solution from the pad or tank. Typical PLS concentrations: Cu 1–5 g/L, Zn 2–10 g/L, Co 0.5–3 g/L. Measure metal concentration and pH.

5. **Recover metals from PLS.** Use solvent extraction (SX): mix PLS with organic extractant (LIX reagents for copper), separate loaded organic, strip with concentrated acid. Alternatively, direct electrowinning from PLS. See [Electrolysis](../chemistry/electrolysis.md).

6. **Neutralize spent leach solution.** Raise pH to 8–9 with limestone or lime. Precipitate remaining metals as hydroxides. Discharge clarified solution or recycle to leach circuit.

**Strengths**:
- Dissolves oxide and some sulfide metals at 65-85% recovery with simple chemistry (H₂SO₄ + oxidant)
- Heap leaching handles large volumes (>100,000 tonnes) at low capital cost
- Tank leaching completes in 24-96 hours — fast kinetics for high-value metals

**Weaknesses**:
- High carbonate tailings (>5% CaCO₃) consume excessive acid — may be uneconomic without pre-treatment
- Heap leach cycles run 30-120 days — slow return on capital invested in leach pad construction
- Spent leach solution must be neutralized to pH 8-9 before discharge — continuous limestone consumption

### 4.3 Bioleaching of Sulfide Tailings

1. **Inoculate with bacteria.** Culture iron- and sulfur-oxidizing bacteria (Acidithiobacillus ferrooxidans, Acidithiobacillus thiooxidans). These microorganisms oxidize sulfide minerals, releasing metals into solution. Optimal conditions: pH 1.5–2.5, temperature 30–40°C.

2. **Construct bioleach heap or bioreactor.** Stack tailings on a lined pad with aeration piping (bacteria need oxygen). Irrigate with acidic solution containing the bacterial culture. For faster kinetics, use aerated stirred-tank reactors (50–200 m³).

3. **Maintain biological activity.** Monitor pH, redox potential (Eh >600 mV), temperature, and iron concentration. Add nutrients (NH₄⁺, PO₄³⁻) at trace levels if deficient. Bioleach cycle: 6–24 months (heap) or 3–10 days (tank).

4. **Recover metals from bioleach solution.** Same as acid leaching — solvent extraction, electrowinning, or precipitation.

**Strengths**:
- Bacteria generate their own leaching agent (sulfuric acid) from sulfide minerals — low reagent cost
- Operates at ambient temperature (30-40°C) and atmospheric pressure — no energy-intensive heating
- Recovers metals from low-grade sulfide tailings (0.1-0.5% Cu) that acid leaching cannot process economically

**Weaknesses**:
- Bioleach cycle is slow: 6-24 months for heap leaching vs. 30-120 days for acid heap leach
- Bacteria are sensitive to temperature excursions, toxic metals (As, Hg), and nutrient deficiency
- Requires continuous aeration of heap or reactor — compressor energy cost over months of operation

## 5. Quantitative Parameters

### Typical Recovery Rates from Tailings

| Metal/Mineral | Original Tailings Grade | Reprocessing Recovery | Method | Product |
|---------------|------------------------|----------------------|--------|---------|
| Copper (oxide) | 0.2–0.5% Cu | 65–85% | Acid leach (heap/tank) | Copper cathode (99.99% Cu) |
| Copper (sulfide) | 0.3–0.8% Cu | 50–75% | Flotation retreatment | Copper concentrate (20–30% Cu) |
| Gold | 0.3–1.5 g/t Au | 50–80% | CIL/CIP (cyanide leach) | Gold doré (>80% Au) |
| Iron (magnetite) | 15–40% Fe | 60–80% | Magnetic separation | Iron concentrate (60–65% Fe) |
| Zinc | 1–5% Zn | 70–90% | Acid leach + SX-EW | Zinc metal (99.99% Zn) |
| Rare earths | 0.1–1% REO | 50–70% | Acid leach + solvent extraction | REE concentrate |
| Uranium | 0.01–0.05% U₃O₈ | 60–85% | Acid/alkaline leach | Yellowcake (U₃O₈) |

### Leaching Parameters

| Parameter | Acid Leach | Bioleach | Alkaline Leach |
|-----------|-----------|----------|----------------|
| Reagent | H₂SO₄ (5–50 g/L) | Bacteria + air | NaOH or Na₂CO₃ |
| pH | 1.5–2.5 | 1.5–2.5 | 10–12 |
| Temperature | 25–80°C | 30–45°C | 25–60°C |
| Duration (heap) | 30–180 days | 180–720 days | 30–120 days |
| Duration (tank) | 24–96 hours | 72–240 hours | 24–72 hours |
| Energy | 10–30 kWh/t | 5–15 kWh/t (aeration) | 15–40 kWh/t |
| Acid consumption | 10–80 kg H₂SO₄/t | Self-generating | N/A (alkali) |

### Tailings Deposit Characteristics

| Parameter | Typical Range | Notes |
|-----------|--------------|-------|
| Particle size (D₅₀) | 20–200 μm | Already ground — energy advantage over primary ore |
| Solids content in impoundment | 30–70% | Hydraulic mining feasible at lower solids |
| Pore water pH | 2–9 | Acid mine drainage (pH <4) indicates ongoing sulfide oxidation |
| Residual metal grade | 10–60% of original ore grade | Depends on efficiency of original processing |

## 6. Scaling Notes

**Minimum viable scale**: A small tailings pile of 5,000–50,000 tonnes can be reprocessed by a single leach tank (10–50 m³) or a small leach pad (0.1–0.5 hectare). This is appropriate for a settlement that has been mining for 15–20 years and has accumulated a meaningful waste pile.

**Industrial scale** (1–100 million tonnes): Large tailings reprocessing operations use continuous tank leaching circuits or valley-fill heap leach pads covering 10–100 hectares. Equipment: 5–20 agitated leach tanks of 500–2,000 m³ each, solvent extraction plant, and electrowinning tankhouse.

**Key constraint — tailings characterization**: Before any reprocessing, the tailings deposit must be characterized by drilling, assaying, and mineralogical analysis. This costs $50K–$500K for a preliminary assessment. A reprocessing project cannot proceed without understanding the spatial variability of metal grade and mineralogy within the deposit.

**Environmental remediation bonus**: Reprocessing often doubles as environmental remediation. Removing sulfide minerals from tailings eliminates the source of acid mine drainage. The reprocessed tailings (with metals removed) can be re-deposited in a modern, lined facility or used as construction backfill.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low metal recovery from flotation | Particles too fine (<10 μm) — slime coating prevents bubble attachment | Deslime ahead of flotation; use stronger collectors; consider leaching instead |
| High acid consumption | Carbonate minerals (calcite, dolomite) in tailings neutralize acid | Pre-neutralize with cheaper acid; switch to alkaline leaching; blend with low-carbonate tailings |
| Acid mine drainage from reprocessed tailings | Sulfide minerals not fully removed — residual pyrite oxidizes | Ensure flotation removes >90% sulfides; or neutralize residual with limestone before re-deposition |
| Leach solution percolation too slow | Tailings compacted or clay-rich (low permeability) | Rip and re-stack tailings to improve permeability; add lime to prevent clay dispersion |
| Bioleach stalls (redox drops) | Bacteria killed by temperature excursion, toxic metals (As, Hg), or nutrient limitation | Monitor temperature (keep 30–40°C); dilute toxic metals; add (NH₄)₂SO₄ and K₂HPO₄ nutrients |
| Solvent extraction crud formation | Fine particulates or organic degradation products at organic-aqueous interface | Filter PLS before SX; add crud treatment (clay or centrifuge); replace degraded organic extractant |

## 8. Safety

**Cyanide handling** (gold tailings): Sodium cyanide (NaCN) is acutely toxic — 200–300 mg oral dose is lethal. At pH <9.5, cyanide releases HCN gas (almond odor, lethal at 150 ppm). Always maintain pH >10.5 during leaching. Cyanide detoxification (SO₂/air or hydrogen peroxide) required before tailings discharge. Emergency: cyanide first-aid kit (amyl nitrite, sodium thiosulfate) must be within 30 seconds of leach area.

**Acid mine drainage (AMD)**: Excavating sulfide-bearing tailings exposes fresh sulfide surfaces to air and water, accelerating acid generation. Runoff from excavation faces can have pH <2 and dissolved metal concentrations >1,000 ppm. Contain all excavation runoff in lined ponds. Neutralize with lime before discharge. Monitor pH continuously at discharge point.

**Tailings dam stability**: Excavating material from a tailings impoundment can destabilize the dam structure. Engage a geotechnical engineer to assess stability before excavation begins. Never undercut the dam toe. Monitor piezometric levels and dam displacement during operations.

**Dust exposure**: Dry tailings generate silica-containing dust. Prolonged inhalation causes silicosis (irreversible lung scarring). Wet all excavation surfaces. PPE: half-face respirator with P100 filter when dust is visible.

## 9. Quality Control

### Tailings Feed Assay

| Parameter | Method | Purpose |
|-----------|--------|---------|
| Metal grade (Cu, Au, Zn, etc.) | Fire assay (Au) or ICP-OES (base metals) | Determine economic viability |
| Acid consumption | Bottle roll test with H₂SO₄ titration | Estimate reagent cost |
| Mineralogy | XRD or optical microscopy | Determine extraction method |
| Particle size distribution | Laser diffraction or sieving | Determine if regrinding needed |
| Moisture content | Oven drying at 105°C | Calculate dry tonnage |

### Leach Solution Monitoring

| Parameter | Frequency | Target |
|-----------|-----------|--------|
| pH | Continuous | 1.5–2.5 (acid leach) |
| Redox potential (Eh) | Continuous | >600 mV (vs. Ag/AgCl) |
| Metal concentration | Daily | Track dissolution kinetics |
| Free acid | Daily | 5–20 g/L H₂SO₄ |
| Dissolved oxygen | Continuous (tank leach) | >2 mg/L |

### Product Quality

| Product | Key Specification | Test Method |
|---------|-------------------|-------------|
| Copper cathode | >99.99% Cu | ASTM B115 |
| Gold doré | >80% Au + Ag | Fire assay |
| Copper concentrate | 20–30% Cu, <0.1% As | ICP-OES |
| Iron concentrate | >60% Fe, <0.05% P | XRF |

## 10. Variations and Alternatives

### Tailings Reprocessing Methods Compared

| Method | Target Metals | Recovery | Cost per Tonne | Best For |
|--------|-------------|----------|----------------|----------|
| Flotation retreatment | Cu, Pb, Zn sulfides | 50–75% | $5–15 | Sulfide-rich tailings with coarse liberation |
| Acid leaching (heap) | Cu, Zn, Co, Ni, U | 65–85% | $8–25 | Large volumes, oxide minerals |
| Acid leaching (tank) | Cu, Zn, Co, Ni | 80–95% | $15–40 | High-grade tailings, faster kinetics needed |
| Bioleaching | Cu, Au, Ni, Co | 60–80% | $5–20 | Low-grade sulfides, low capital |
| Cyanide leaching (CIL) | Au, Ag | 50–80% | $10–30 | Gold tailings |
| Magnetic separation | Fe (magnetite) | 60–80% | $3–10 | Iron ore tailings |
| Gravity separation | Au (coarse), Sn, W | 40–70% | $2–8 | Coarse heavy mineral tailings |

### When NOT to Reprocess

- Tailings grade below economic cutoff (varies by metal; Cu <0.1%, Au <0.2 g/t)
- Tailings volume too small for capital investment
- Environmental risk of excavation exceeds benefit
- Access to tailings deposit is difficult (under water, under infrastructure)

## 11. References

- [Mining Extraction](extraction.md) — Primary mining methods
- [Ore Processing](processing.md) — Crushing, grinding, flotation, gravity separation
- [Mineral Acids](../chemistry/acids.md) — Sulfuric acid production for leaching
- [Electrolysis](../chemistry/electrolysis.md) — Electrowinning metals from leach solutions
- [Alkalis](../chemistry/alkalis.md) — Neutralization reagents
- [Lime Production](../ceramics/lime.md) — Neutralization and pH control
- [Metal Recycling](../metals/metal-recycling.md) — Metal recovery from scrap (parallel recovery domain)
- [Waste Management](../ehs/waste-management.md) — Disposal of leach residues and process waste
- [Chemical Recovery](../chemistry/chemical-recovery.md) — Acid and solvent recovery from leaching operations

---

*Part of the [Bootciv Tech Tree](../index.md) • [Mining](./index.md) • [All Domains](../index.md)*
