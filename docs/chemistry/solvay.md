# Solvay Process

> **Node ID**: chemistry.solvay
> **Domain**: Chemistry
> **Timeline**: Years 15-30
> **Outputs**: sodium_carbonate, sodium_bicarbonate, calcium_chloride

## Overview

The Solvay process produces sodium carbonate (soda ash, Na₂CO₃) from brine (NaCl) and limestone (CaCO₃) using ammonia as a recyclable catalyst. Soda ash is the workhorse alkaline chemical for glass making, soap production, water softening, and chemical synthesis. The process superseded the Leblanc method industrially due to lower cost and fewer toxic byproducts.

## Process Chemistry

The overall reaction combines salt and limestone into soda ash and calcium chloride waste:

2NaCl + CaCO₃ → Na₂CO₃ + CaCl₂

This reaction does not proceed directly — it requires ammonia as an intermediate carrier. The Solvay process splits this into a series of steps that are each thermodynamically favorable:

**Step 1 — Ammonia absorption**: NH₃ gas dissolves in saturated brine exothermically (ΔH = -35 kJ/mol). The ammoniated brine also absorbs some CO₂, forming traces of ammonium carbonate.

**Step 2 — Carbonation**: NH₃ + CO₂ + NaCl + H₂O → NaHCO₃↓ + NH₄Cl. Sodium bicarbonate precipitates because it is poorly soluble in the concentrated, cold brine. This is the key reaction — the precipitation drives the equilibrium forward.

**Step 3 — Calcination**: 2NaHCO₃ → Na₂CO₃ + CO₂↑ + H₂O↑ at 160-230°C. The CO₂ is recycled to the carbonation tower. The product is light soda ash (density ~500 kg/m³).

**Step 4 — Ammonia recovery**: 2NH₄Cl + Ca(OH)₂ → 2NH₃↑ + CaCl₂ + 2H₂O. Steam strips NH₃ from the mother liquor. The Ca(OH)₂ comes from slaking CaO, which comes from calcining limestone. The CO₂ from the lime kiln feeds the carbonation tower.

## Detailed Process Steps

### Brine Preparation and Purification

Raw salt solution (from solution mining of underground salt deposits or dissolution of rock salt) contains impurities that must be removed before the process. Saturated brine at 20°C contains ~300 g/L NaCl (26.4% by weight).

**Purification sequence**:
1. Add Na₂CO₃ (from product recycle) to precipitate CaCO₃: Ca²⁺ + CO₃²⁻ → CaCO₃↓. Target: Ca²⁺ <5 mg/L.
2. Add NaOH to precipitate Mg(OH)₂: Mg²⁺ + 2OH⁻ → Mg(OH)₂↓. Target: Mg²⁺ <1 mg/L.
3. Settle in clarifier (2-4 hours detention). Remove precipitate sludge.
4. Filter through sand or leaf filters. Suspended solids <5 mg/L.
5. Some plants add BaCl₂ to precipitate BaSO₄ if sulfate exceeds 5 g/L (sulfate interferes with carbonation).

Impure brine causes scaling in carbonation towers (CaCO₃, Mg(OH)₂ deposits), reduces crystal purity, and increases ammonia losses. Complete purification is essential for efficient operation.

### Ammonia Absorption Tower

Saturated purified brine flows downward through a packed or bubble-cap absorption tower (8-12 m tall, 1.5-3.0 m diameter). NH₃ gas (from the ammonia still) rises countercurrently. The absorption is strongly exothermic — cooling water jackets or internal coils maintain temperature below 30°C (higher temperature reduces NH₃ solubility and shifts equilibrium against carbonation).

Ammoniated brine composition: ~260 g/L NaCl, ~90-100 g/L NH₃, ~20-30 g/L CO₂ (absorbed from ammonia recovery section). The NH₃:NaCl molar ratio is maintained at ~1.1:1 (slight excess NH₃ ensures complete carbonation).

### Carbonation Tower

The carbonation tower is the heart of the Solvay plant: a tall steel vessel (20-30 m tall, 2-3 m diameter) with internal bubble-cap trays or packed sections. The tower operates in two zones:

**Upper zone (precipitation)**: Ammoniated brine enters near the top. CO₂ gas (from the lime kiln, ~35-40% CO₂, and from the calciner, ~90% CO₂) enters at the bottom and bubbles upward through the liquid. Temperature: 15-20°C at the top (optimal for NaHCO₃ crystallization — solubility increases with temperature). Total residence time: 1.5-3 hours.

**Lower zone (saturation)**: Higher CO₂ concentration here. The temperature rises to 25-30°C due to the exothermic carbonation reaction. Sodium bicarbonate crystals nucleate and grow. Crystal size distribution: 100-300 μm, controlled by cooling rate, supersaturation, and seeding.

NaCl conversion efficiency: 72-75%. The remaining 25-28% of NaCl stays in the mother liquor and is recycled. CO₂ absorption efficiency: 80-90%. The unabsorbed CO₂ (tail gas) is scrubbed with fresh ammoniated brine for recovery.

Temperature profile is critical: too cold → slow reaction, fine crystals difficult to filter; too warm → increased NaHCO₃ solubility, reduced yield. The tower is cooled by internal coils or external water jackets at multiple levels.

### Filtration

The NaHCO₃ slurry (30-40% solids) from the carbonation tower bottom is filtered on rotary vacuum filters (2-4 m diameter drum, rotating at 0.5-2.0 RPM) or centrifuges (pusher or peeler type, 800-1500 RPM).

Filter cake composition: ~85% NaHCO₃, ~10% H₂O, ~4% NH₄Cl, ~1% NaCl (as trapped mother liquor). Wash with cold water (5-10°C) to remove adhering NH₄Cl and NaCl — this wash is critical for product purity. Wash water consumption: 0.3-0.5 m³ per tonne NaHCO₃. Excessive washing dissolves the product itself.

Mother liquor (filtrate) composition: ~200 g/L NH₄Cl, ~70 g/L NaCl, some (NH₄)₂CO₃ and NH₄HCO₃. This is the feed for ammonia recovery.

### Calcination (Thermal Decomposition)

Wet NaHCO₃ cake is dried and calcined in a rotary kiln or fluidized-bed calciner.

**Rotary kiln**: Steel shell (2-3 m diameter, 15-25 m long), internally lined with refractory brick, rotating at 2-5 RPM, inclined 2-3°. Wet cake enters at the upper end, product discharges at the lower end. Hot flue gas (from natural gas or coal combustion) flows countercurrently. Temperature profile: inlet gas 600-800°C, product exit 160-200°C, cake inlet 100-150°C. Residence time: 20-40 minutes.

**Fluidized-bed calciner**: More energy-efficient (2.8-3.5 GJ/tonne vs. 3.5-4.5 GJ/tonne for rotary kiln). Hot air fluidizes NaHCO₃ particles at 160-230°C. Smaller footprint, faster heat transfer, but requires finer feed particle size.

**Reaction**: 2NaHCO₃ → Na₂CO₃ + CO₂↑ + H₂O↑. The CO₂ (concentrated, ~90%+ after condensing water vapor) is recycled to the carbonation tower — this is the richest CO₂ stream in the plant. The water vapor is condensed in a scrubbing tower and returned to the process.

**Product**: Light soda ash (Na₂CO₃, density ~500 kg/m³). Convert to dense soda ash (density ~1000 kg/m³) by rehydration (Na₂CO₃ + 10H₂O → Na₂CO₃·10H₂O at 35°C) and recalcination — denser product is easier and cheaper to transport. Dense soda ash flows like sand; light soda ash is fluffy and dusty.

### Ammonia Recovery (Distillation)

The mother liquor from filtration contains valuable NH₃ (as NH₄Cl) that must be recovered. This is the key to the process economics — only 1-2 kg NH₃ makeup is needed per tonne Na₂CO₃ because the NH₃ is continuously recycled.

**Ammonia still (distillation column)**: 15-25 m tall, 1.5-3.0 m diameter, with bubble-cap or sieve trays. Mother liquor enters near the middle. Slaked lime (Ca(OH)₂ slurry, 15-25% solids, from the lime slaker) enters near the top of the regenerating section.

**Reaction in the still**: 2NH₄Cl + Ca(OH)₂ → 2NH₃↑ + CaCl₂ + 2H₂O. Steam injected at the bottom strips NH₃ from the solution. NH₃ gas exits the top of the still at 55-65°C and is recycled to the ammonia absorption tower.

**Still bottom liquor**: Contains CaCl₂ (~10% solution), unreacted NaCl, and traces of Ca(OH)₂. Discharged as waste — this is the main waste stream, ~10 tonnes per tonne Na₂CO₃. CaCl₂ has commercial uses (de-icing roads at eutectic -51°C, dust control, concrete accelerator at 1-2% by weight of cement), but the volume produced far exceeds market demand.

### Lime Kiln and Slaker

**Lime kiln**: Vertical shaft kiln (6-10 m tall, 2-4 m diameter) or rotary kiln (30-60 m long). Feed limestone (CaCO₃, 50-150 mm pieces) and fuel (coke, natural gas, or coal). Temperature: 900-1100°C in the calcination zone. Reaction: CaCO₃ → CaO + CO₂. CO₂ (30-40% concentration in the exit gas, mixed with N₂ from combustion air) is cooled, scrubbed (removes SO₂ and dust), and sent to the carbonation tower.

Lime kiln fuel: 0.08-0.12 tonnes coke per tonne CaO produced. The CO₂ from the lime kiln accounts for roughly half the CO₂ needed for carbonation; the other half comes from the NaHCO₃ calciner. Yield: 56 kg CaO per 100 kg CaCO₃ (theoretical), 90-95% practical.

**Slaker**: CaO + H₂O → Ca(OH)₂, highly exothermic (65 kJ/mol). Add quicklime to water (never water to lime) in a slaking tank at 80-90°C. The resulting milk of lime (15-25% solids) is the feed for ammonia recovery. Excess water controls temperature — the reaction can generate >150°C locally if not well-mixed.

## Material and Energy Balance

Per tonne of Na₂CO₃ produced:

| Input | Quantity | Source |
|-------|----------|--------|
| NaCl | 1.5-1.6 tonnes | Salt mine or seawater evaporation |
| CaCO₃ (limestone) | 1.2-1.4 tonnes | Quarry |
| NH₃ (makeup) | 1-2 kg | [Haber-Bosch](ammonia.md) or coke-oven gas |
| Coke/coal (lime kiln) | 0.08-0.12 tonnes | Coal mine |
| Steam | 1.5-3.0 tonnes | Boiler |
| Cooling water | 50-100 m³ | River or cooling tower |
| Electrical power | 50-100 kWh | Grid |

| Output | Quantity | Destination |
|--------|----------|-------------|
| Na₂CO₃ (soda ash) | 1.0 tonne | Market |
| CaCl₂ waste | 8-10 tonnes solution (10% CaCl₂) | Disposal or sale |
| CO₂ vented | 0.3-0.5 tonnes | Atmosphere (excess from kiln) |
| Total energy | 7-10 GJ | — |

## Product Quality

Smelter-grade soda ash must meet minimum specifications: Na₂CO₃ >98.5%, NaCl <0.5%, Na₂SO₄ <0.05%, Fe₂O₃ <0.004%, insoluble in water <0.1%. Glass-grade soda ash requires even lower iron (<0.002% Fe₂O₃) because iron colors glass green. Heavy ash (dense) is preferred for transport; light ash for chemical feedstock.

Sodium bicarbonate (baking soda, NaHCO₃) is produced by diverting the carbonation precipitate before calcination, washing more thoroughly, and drying at <50°C (to prevent decomposition). Food-grade NaHCO₃ requires additional purification (recrystallization from water at 40-60°C). Purity target: >99.5% NaHCO₃, with heavy metals below 5 ppm.

## Calcium Chloride Byproduct

The CaCl₂ waste stream (~10 tonnes of 10% solution per tonne Na₂CO₃) can be processed into marketable products rather than discharged:

**Concentration**: Evaporate in multiple-effect evaporators to 35-40% CaCl₂ solution. Further concentration to 74-78% produces liquid calcium chloride (density 1.42 g/mL at 35%, freezing point -30°C at 30%).

**Solid production**: Flake or pelletize by cooling concentrated solution on a flaking drum (5-10 mm thick frozen layer, broken into flakes). Anhydrous CaCl₂ (94-97%) produced by evaporating to dryness and drying at 200-300°C. Hygroscopic — absorbs moisture from air (used as desiccant). Heat of solution: -82.8 kJ/mol (used for de-icing — the exothermic dissolution melts snow and ice).

## Comparison with Leblanc Process

| Parameter | Solvay | Leblanc |
|-----------|--------|---------|
| Energy (GJ/tonne Na₂CO₃) | 7-10 | 14-18 |
| Waste per tonne product | 10 t CaCl₂ solution | 4 t CaS + HCl emissions |
| NH₃ required | 1-2 kg/tonne (recycled) | None |
| Capital cost | Higher (towers, stills) | Lower (furnaces) |
| Economical scale | 100+ tonnes/day | Any scale |
| Product purity | >98.5% | 95-97% |
| Environmental impact | CaCl₂ discharge (salinity) | H₂S, HCl emissions |

The Leblanc process is simpler to build at small scale and produces HCl as a valuable byproduct. It may be preferred during early bootstrapping when ammonia is not yet available. Once Haber-Bosch ammonia production is operational, the Solvay process displaces Leblanc due to lower cost and pollution.

## Safety and Environmental Considerations

**Ammonia hazards**: The process handles large volumes of NH₃ under pressure. Leak detection (NH₃ sensors at 25 ppm alarm level), emergency scrubbers (water or dilute H₂SO₄), and evacuation procedures are mandatory. NH₃ is toxic (IDLH 300 ppm), flammable (15-28% in air), and causes severe respiratory and eye irritation. PPE: chemical splash goggles, face shield, rubber gloves, and respiratory protection when entering ammonia-handling areas.

**Lime hazards**: CaO reacts violently with water (temperature can exceed 150°C in bulk slaking). Add lime to water slowly with mixing — never water to lime. Ca(OH)₂ slurry is caustic (pH 12.4) and causes chemical burns.

**CO₂ hazards**: The carbonation tower and lime kiln generate CO₂. In enclosed spaces, CO₂ displaces O₂ (density 1.5× air, accumulates in low areas). Concentrations above 5% cause respiratory distress; above 10%, unconsciousness. Ventilation required in all enclosed process areas.

**CaCl₂ disposal**: The waste CaCl₂ solution (10% concentration) has high salinity. Direct discharge to freshwater causes osmotic stress on aquatic organisms. Discharge to ocean is acceptable at moderate rates. Evaporation ponds (3-5 m deep, lined with clay or HDPE membrane) concentrate the waste to solid CaCl₂ in arid climates.

## Plant Design and Scale

**Minimum economic scale**: 100-200 tonnes Na₂CO₃/day. Below this, capital costs per tonne become prohibitive. The carbonation towers, ammonia stills, lime kiln, and filtration equipment are all capital-intensive, long-lead-time items.

**Major equipment list** for a 500 tonne/day plant:
- Brine purification system: settling tanks, filters, chemical dosing
- Ammonia absorber: steel tower, 12 m tall × 2.5 m diameter, with cooling coils
- Carbonation tower: steel tower, 25 m tall × 2.5 m diameter, with 20-30 bubble-cap trays, cooling water circulation at each level
- Rotary vacuum filters: 3 m diameter drums × 2-3 units
- Calciner: rotary kiln, 2.5 m diameter × 20 m long, refractory-lined
- Ammonia still: steel column, 20 m tall × 2.0 m diameter, with steam injection and lime slurry feed
- Lime kiln: shaft kiln, 8 m tall × 3 m diameter, lined with firebrick, producing 200 tonnes CaO/day
- Slaker: steel tank with agitator, 5 m diameter × 4 m tall
- CO₂ compressors: 2-stage reciprocating, delivering 2-3 atm to carbonation tower
- Steam boiler: 10-15 tonnes/hour at 10-15 bar
- Cooling water system: 2,000-5,000 m³/hour through cooling tower

**Plant layout**: The carbonation tower is typically the tallest structure (25-30 m). The lime kiln requires access for limestone and coke delivery. The calciner needs fuel supply and exhaust stack. The ammonia system must be in a well-ventilated area with emergency scrubbers. Total plant footprint: 2-5 hectares including raw material storage.

## Process Control

**Carbonation tower control**: Monitor CO₂ concentration in the inlet gas (target 35-40% from kiln, 70-90% from calciner). Temperature profile through the tower (15-20°C at top, 25-30°C at bottom). NaHCO₃ crystal size and slurry density at the tower bottom (target 30-40% solids). Adjust CO₂ flow, brine feed rate, and cooling water to maintain optimal conditions.

**Ammonia still control**: Monitor NH₃ concentration in overhead gas (target >95% NH₃). Still bottom pH and CaCl₂ concentration. Steam flow rate adjusted to maintain NH₃ recovery >99%. Lime slurry feed rate matched to NH₄Cl load in mother liquor.

**Calciner control**: Product temperature (160-200°C exit). CO₂ concentration in exit gas (target >90% after water condensation). Product purity (Na₂CO₃ >98.5%). Fuel/air ratio controls temperature and product quality.

## Historical Context

Ernest Solvay patented the ammonia-soda process in 1861 and built the first commercial plant at Couillet, Belgium in 1865, producing 5 tonnes/day. By 1900, Solvay plants produced 1.4 million tonnes/year, having largely displaced the Leblanc process (which peaked at 500,000 tonnes/year in 1890 and declined rapidly thereafter). The Solvay process remains the dominant production method in the 21st century, with global production exceeding 50 million tonnes/year.

The key innovation was the closed ammonia loop — previous attempts at ammonia-soda processes lost too much expensive NH₃ to be economical. Solvay's engineering (carbonation tower design, ammonia recovery still, and heat integration) made the process commercially viable. The family-owned Solvay SA company still exists as a major chemical manufacturer.

## Modified Solvay Processes

**Dual process (Solvay + Hou)**: The Hou (or Hou's) process, developed in China, adds a precipitation step that produces NH₄Cl as a co-product (valuable as nitrogen fertilizer, 25% N) rather than releasing NH₃ and generating CaCl₂ waste. By adding solid NaCl to the mother liquor and cooling to 5-10°C, NH₄Cl precipitates (solubility drops from 40 g/100 mL at 30°C to 29 g/100 mL at 10°C). The remaining liquor returns to the ammonia absorber. This eliminates the lime kiln and CaCl₂ waste stream at the cost of producing lower-value NH₄Cl instead of recycling all NH₃.

**Sesquicarbonate route**: In some natural deposits, sodium sesquicarbonate (Na₂CO₃·NaHCO₃·2H₂O, trona) is mined directly. Trona is calcined at 150-200°C to produce soda ash: 2(Na₂CO₃·NaHCO₃·2H₂O) → 3Na₂CO₃ + 5H₂O + CO₂. The Green River formation in Wyoming (USA) contains an estimated 127 billion tonnes of trona — enough for thousands of years of production at current rates. Trona mining eliminates the need for the Solvay process entirely where deposits exist.

## Cross-Domain Links

- **[Alkali Production](alkalis.md)**: broader context including Leblanc process, causticization, and potash
- **[Ammonia Production](ammonia.md)**: Haber-Bosch process supplying the 1-2 kg/tonne NH₃ makeup
- **[Acids & Bases](./acids-bases.md)**: soda ash as a key industrial base
- **[Lime Chemistry](alkalis.md)**: lime kiln design, slaking, and the lime cycle
- **[Glass Making](../glass/basic.md)**: Na₂CO₃ as flux lowering SiO₂ melting point from 1710°C to ~1000°C
- **[Soap Production](alkalis.md)**: Na₂CO₃ for water softening and as NaOH feedstock
- **[Electrolysis](electrolysis.md)**: alternative route to NaOH via chlor-alkali process

---

*Part of the [Bootciv Tech Tree](../index.md) · [Chemistry](./index.md) · [All Domains](../index.md)*

[← Back to Chemistry](index.md)
