# Silicon Purification

> **Node ID**: silicon.purification
> **Domain**: Silicon
> **Timeline**: Years 30-50
> **Outputs**: purified_silicon, polysilicon, chlorosilanes

### Purification Pathways

#### Option A: Chemical Purification (Siemens-like Process)

This is the standard industrial route to semiconductor-grade polysilicon (99.9999999%+ purity).

**Step 1: Hydrochlorination** — Convert MG-Si powder to trichlorosilane:
- **Reaction**: Si + 3HCl → SiHCl₃ + H₂ (exothermic, ~300°C, Cu catalyst). Also produces SiCl₄, SiH₂Cl₂ as byproducts.
- **Equipment**: Fluidized bed reactor (Si powder suspended in HCl/H₂ gas stream). Copper catalyst (~1% Cu in Si powder). Temperature 280-350°C. Pressure 1-5 bar.
- **Product**: Mixed chlorosilane gases + H₂. Condense at -30 to 0°C to separate liquid chlorosilanes from H₂ gas.

**Step 2: Fractional distillation** — Purify SiHCl₃:
- **Principle**: SiHCl₃ boils at 31.8°C, SiCl₄ at 57.6°C, SiH₂Cl₂ at 8.2°C. Multiple distillation columns separate these. Purity requirement: impurities <1 ppb for electronic grade.
- **Columns**: 10-30 m tall, packed with structured packing or sieve trays. Reflux ratio 10-50:1. Multiple columns in series for progressive purification.
- **Key separations**: Remove boron (BCl₃, bp 12.5°C — very close to SiHCl₃, requires many theoretical plates), phosphorus (PCl₃, bp 76°C), metal chlorides.
- **Number of distillation passes**: 2-5 for solar grade, 5-10+ for electronic grade.

**Step 3: Chemical vapor deposition (CVD)** — Decompose purified SiHCl₃ on heated silicon rods:
- **Reaction**: SiHCl₃ + H₂ → Si (solid) + 3HCl (gas). Temperature 1050-1150°C.
- **Reactor**: Bell jar (quartz or stainless steel) containing inverted-U silicon seed rods (~5 mm diameter). Resistance-heated to ~1100°C by passing current through rods (rods are conductive when hot). H₂ + SiHCl₃ gas flows around rods.
- **Deposition rate**: ~5-10 μm/min. Rods grow from 5 mm to 100-200 mm diameter over 50-100 hours. Final rods weigh 50-200 kg each.
- **Energy**: ~100-200 kWh/kg polysilicon (electricity for heating + H₂ production).
- **Purity**: 9N-11N (99.9999999% - 99.999999999% Si). Electronic grade.

#### Option B: Physical Purification (Zone Refining / Directional Solidification)

Lower purity than Siemens, but much simpler chemistry. Sufficient for solar cells (~5-7N).

**Directional solidification**:
- **Principle**: Impurities preferentially stay in liquid phase. Slowly cool silicon melt from one end → impurities segregate to last-to-freeze region (Segregation coefficient k < 1 for most impurities in Si). Cut off and discard impure tail.
- **Process**: Melt MG-Si in coated quartz or graphite crucible. Cool from bottom at ~1 cm/hour. Total time 10-30 hours depending on ingot size. Ingot diameter 150-300 mm.
- **Effective segregation coefficients**: B: 0.8 (hard to remove — close to 1), P: 0.35, Al: 0.002, Fe: 6.4×10⁻⁶ (easy to remove). Boron is the problematic impurity — it barely segregates.
- **Result**: Solar-grade silicon (~5-6N). Multiple passes improve purity. Not sufficient for electronic devices.

**Zone refining** (for highest purity physical route):
- **Process**: Pass molten zone (narrow band of liquid) along solid silicon rod, repeatedly. Each pass sweeps impurities toward one end. 10-20 passes achieve ~8-9N purity.
- **Equipment**: RF induction coil or focused IR lamp creates moving molten zone. Rod rotates slowly. Under inert atmosphere (Ar) or vacuum. Very slow — ~1-5 cm/hour travel speed.
- **Limitation**: Still cannot remove boron effectively (k ≈ 0.8). Combine with another boron removal step (slag treatment: add CaO-Na₂O flux to molten Si, B partitions into slag).

#### Boron Removal via Slag Treatment

Directional solidification and zone refining effectively remove most metallic impurities (Fe, Al, Ca — segregation coefficients << 1), but **boron** is uniquely difficult because its segregation coefficient in silicon is ~0.8 (close to 1.0). This means boron distributes almost equally between solid and liquid phases during crystallization, making segregation-based methods nearly useless for boron. Since boron is a compensating dopant that degrades solar cell efficiency, dedicated removal is essential for solar-grade silicon.

**Method**: Oxidizing slag treatment — boron is oxidized to B₂O₃ at the silicon–slag interface and dissolves into the slag phase.

**Slag systems**:
- **CaO-SiO₂**: Most common. Weight ratio CaO:SiO₂ = 40:60 to 60:40. Basicity (CaO/SiO₂) ~0.7-1.5. Additives of CaF₂ (5-15 wt%) reduce slag viscosity and improve kinetics. This system requires only lime and silica — both available early in the bootstrap chain.
- **Na₂O-SiO₂**: Alternative. Weight ratio Na₂O:SiO₂ = 20:80 to 40:60. Lower operating temperature but more aggressive toward refractory linings. Requires soda ash (Na₂CO₃), which adds a supply-chain dependency.

**Process**:
- **Temperature**: 1450-1600°C (above silicon melting point of 1414°C). Higher temperature increases boron oxidation rate and slag fluidity but also accelerates refractory erosion.
- **Slag-to-silicon ratio**: 0.5:1 to 2:1 by weight. Higher ratios increase removal but also silicon losses and energy consumption.
- **Atmosphere**: Argon or Ar/O₂ mix (0-5% O₂). Small oxygen partial pressure accelerates boron oxidation. Pure inert atmosphere relies on SiO₂ in the slag as the oxidant.
- **Contact time**: 1-4 hours with stirring (mechanical or gas bubbling). Without stirring, diffusion-limited times extend to 6+ hours.
- **Equipment**: Graphite crucible with SiC coating (resists slag corrosion) or alumina crucible. Induction heating preferred for stirring via electromagnetic forces.

**Reaction**: 2[B in Si] + 3(SiO₂ in slag) → 3Si + 2(B₂O₃ in slag). Boron partitions into slag as B₂O₃. The distribution ratio L_B = (wt% B in slag)/(wt% B in Si) typically reaches 2-5 under optimal conditions.

**Expected removal efficiency**: 70-90% per pass for CaO-SiO₂ systems. Multiple passes (2-3) can reduce boron from ~15-40 ppm in MG-Si to <1 ppm, sufficient for solar-grade silicon. Silicon yield loss to slag entrainment is typically 3-8% per pass.

**Integration with directional solidification**: Slag treatment is performed first on molten MG-Si to remove boron, followed by directional solidification to remove remaining metallic impurities. This two-step sequence produces solar-grade silicon (~5-6N) without requiring the energy-intensive Siemens chemical route.

### Czochralski (CZ) Crystal Growth

See [Crystal Growth & Wafering](crystal-growth.md) for CZ pulling details.

### Hydrogen Sourcing for Trichlorosilane Route

The Siemens process requires large volumes of H₂ for both the hydrochlorination step and the CVD deposition:
- **Electrolysis of water**: H₂O → H₂ + ½O₂. Most common source for high-purity H₂. Requires ~4.5-5.5 kWh per Nm³ H₂ (alkaline electrolysis at 70-80% efficiency). A polysilicon plant producing 1000 tonnes/year needs ~3,000-5,000 Nm³ H₂/hour — a dedicated electrolysis plant.
- **Chlor-alkali byproduct**: NaCl + H₂O → Cl₂ + H₂ + NaOH. The H₂ is a co-product. If a chlor-alkali plant exists (needed for HCl production anyway), its H₂ output can feed the silicon purification line. Synergy: Cl₂ from chlor-alkali is burned with H₂ to make HCl → HCl reacts with MG-Si → trichlorosilane.
- **Storage and delivery**: H₂ stored as compressed gas (200-350 bar) or cryogenic liquid (-253°C). Piping must be stainless steel (H₂ embrittlement of carbon steel is a long-term failure risk).

### SiCl₄ Byproduct Management

The Siemens process generates ~3-5 kg SiCl₄ per kg of polysilicon. This is a significant waste stream that must be managed:
- **Recycle to trichlorosilane**: React SiCl₄ with MG-Si powder and H₂ in a fluidized bed (hydrogenation): 3SiCl₄ + Si + 2H₂ → 4SiHCl₃. Converts low-value SiCl₄ back to useful trichlorosilane. This is the preferred route — most modern plants are closed-loop.
- **Convert to fumed silica**: Burn SiCl₄ in H₂/O₂ flame: SiCl₄ + 2H₂ + O₂ → SiO₂ + 4HCl. Produces fumed silica (Aerosil) — extremely fine amorphous SiO₂ particles (7-40 nm). Used as thickening agent, desiccant, and CMP slurry component. Valuable co-product.
- **Sell as feedstock**: SiCl₄ is used in optical fiber production (SiO₂ deposition) and as a raw material for other silicon chemicals.

### Waste Handling

The chlorosilane purification process generates several hazardous waste streams:
- **HCl neutralization**: Scrubber systems (packed column, caustic recirculation) neutralize HCl gas from CVD reactor exhaust. NaOH or Ca(OH)₂ scrubbing solution absorbs HCl → NaCl or CaCl₂ brine. Brine is disposed as industrial wastewater or evaporated to dry salt.
- **Chlorosilane disposal**: Unreacted or off-spec chlorosilanes cannot be dumped — they react violently with water. Controlled hydrolysis in a dedicated treatment system: spray chlorosilane into a controlled excess of water in a sealed, vented vessel. Products: SiO₂ sludge + HCl solution. Neutralize HCl, filter and dispose SiO₂ sludge as non-hazardous waste.
- **Heavy metal chlorides**: Distillation bottoms contain FeCl₃, AlCl₃, CuCl₂ collected from impurity removal. These are hazardous — treat with caustic to precipitate metal hydroxides, then dispose as hazardous waste. Recover copper from CuCl₂ if economically viable.

### Energy Comparison

Energy consumption varies dramatically across the silicon processing chain. Approximate values per kg of product:

| Process | Product | Energy (kWh/kg) | Notes |
|---------|---------|-----------------|-------|
| Submerged arc furnace | MG-Si (97-99%) | 11-13 | See [mg-si-production.md](mg-si-production.md) |
| Directional solidification | Solar-grade Si (~6N) | 15-25 | Includes melting + controlled cooling |
| Zone refining | High-purity Si (~8-9N) | 50-100 | Many slow passes, low throughput |
| Siemens CVD | Polysilicon (9-11N) | 100-200 | Dominated by rod heating + H₂ production |
| Czochralski pulling | Single crystal ingot | 200-400 | From polysilicon to crystal (see [crystal-growth.md](crystal-growth.md)) |
| Float zone (FZ) | Single crystal ingot | 300-500 | RF heating, slower but no crucible contamination |

The energy intensification from MG-Si to single-crystal wafers is roughly 20-40×. A polysilicon plant is fundamentally an energy conversion facility — cheap, abundant electricity is the primary siting requirement.

### Safety Hazards

Silicon purification involves some of the most dangerous chemicals in semiconductor manufacturing:
- **Pyrophoric SiHCl₃**: Trichlorosilane ignites spontaneously on contact with air (autoignition ~185°C, but can flash at room temperature if warm or in fine mist). All handling must be under inert atmosphere (N₂ or Ar) in sealed systems. Leaks produce dense white HCl/SiO₂ smoke and fire. Firefighting: CO₂ or dry chemical. Do NOT use water — it accelerates decomposition and generates HCl.
- **HCl gas**: Corrosive, causes severe respiratory burns. Concentrations >50 ppm are immediately dangerous. Scrubber systems on all vent lines. HCl monitors with automatic ventilation shutdown. Full-face respirator with acid gas cartridge for emergency entry.
- **H₂ explosion risk**: Hydrogen has an extremely wide flammable range (4-75% in air) and very low ignition energy (0.017 mJ — a static spark is sufficient). All H₂ piping must be purged with N₂ before opening. Explosion-proof electrical equipment in H₂ areas. Hydrogen detectors with automatic shutdown and ventilation.
- **Chlorosilane water reactivity**: All chlorosilanes (SiHCl₃, SiCl₄, SiH₂Cl₂) react violently with water, producing HCl gas and heat. The reaction can be explosive if water contacts bulk liquid chlorosilane. Strict segregation of water lines from chlorosilane lines. Double-walled piping for chlorosilane transfer. Secondary containment for storage tanks.
- **Personal protective equipment**: Chemical splash suit (PVC or butyl rubber), face shield, chemical-resistant gloves, self-contained breathing apparatus (SCBA) for emergency response. Standard PPE is insufficient for a major chlorosilane release — SCBA is mandatory.

---
*Part of the [Bootciv Tech Tree](../) • [Silicon](./) • [All Domains](../)*