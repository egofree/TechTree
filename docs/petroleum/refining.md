# Petroleum Refining

> **Node ID**: petroleum.refining
> **Domain**: [Petroleum Extraction & Refining](./index.md)
> **Dependencies**: [`chemistry.distillation`](../chemistry/distillation.md), `petroleum`, [`petroleum.extraction`](extraction.md)
> **Enables**: [`energy.engine`](../energy/engine.md), [`petroleum.petrochemicals`](petrochemicals.md), `petroleum.refining.cracking`, `petroleum.refining.distillation`
> **Timeline**: Years 15-40
> **Outputs**: gasoline, kerosene, diesel, fuel_oil, lubricating_base_oil, asphalt, lpg, refinery_gas
> **Critical**: No — refining produces optimal fuels and chemical feedstocks but biomass and coal-derived alternatives exist

## Why Refining Matters

Crude oil as extracted from the ground is a complex mixture of thousands of hydrocarbon compounds ranging from C₁ (methane) to C₆₀+ (asphaltenes), along with sulfur, nitrogen, oxygen compounds, and metals (vanadium, nickel). Raw crude has limited direct use — it must be separated into fractions and chemically converted into products with defined properties. Refining transforms crude oil into the fuels (gasoline, diesel, kerosene), lubricants, and chemical feedstocks that drive industrial civilization.

The refining process chain follows a clear progression: separation (distillation) → conversion (cracking, reforming) → finishing (hydrotreating, blending). Each step adds value by converting less useful heavy fractions into more valuable light products.

## Atmospheric Distillation (ADU)

The first and most fundamental refining process. Separates crude oil into fractions by boiling point at near-atmospheric pressure (1-2 bar). The atmospheric distillation unit (ADU) processes the entire crude oil throughput and sets the stage for all downstream units.

### Feed Preparation (Desalting)

Crude oil from the wellhead contains salt water (1-5% water, 50-300 ppm salt), sand, and sediments. Salt causes severe corrosion in downstream equipment (HCl formation at distillation temperatures).

**Electrostatic desalter**: Mix crude with 3-10% fresh water at 120-150°C. Add emulsion-breaking chemicals. Pass through electrostatic coalescer (20-60 kV electric field causes water droplets to merge and separate). Settling tank: water (denser, containing dissolved salts) settles to bottom, desalted crude floats to top. Remove salt to <5 PTB (pounds per thousand barrels). Single stage achieves 90-95% salt removal; two stages in series achieve 98-99%.

### Distillation Conditions & Products

Preheated crude enters the tube-still furnace (fuel-fired, 70-80% thermal efficiency, heat duty 30-80 MW for a 50,000-200,000 bbl/day unit) and is heated to 350-385°C. The hot crude enters the flash zone of the atmospheric column as a partially vaporized mixture (typically 40-60% vaporized at the feed point).

**Column specifications**: 30-50 m tall, 3-8 m diameter, 30-50 actual trays (sieve or valve type), operating at 1-2 bar slight positive pressure.

**Product cuts drawn at different heights**:

| Fraction | Temperature Range | Yield (Arab Light) | Primary Use |
|----------|-------------------|---------------------|-------------|
| Refinery gas (C₁-C₄) | < 40°C | 1-3% | Fuel gas, LPG recovery |
| Light naphtha | 40-90°C | 5-10% | Gasoline blending, petrochemical feedstock |
| Heavy naphtha | 90-180°C | 10-15% | Catalytic reformer feed → high-octane gasoline, BTX aromatics |
| Kerosene | 180-260°C | 10-15% | Jet fuel (Jet A-1), diesel blending, illuminating kerosene |
| Diesel / gas oil | 260-350°C | 15-25% | Diesel fuel (cetane 40-55), heating oil, FCC feedstock |
| Atmospheric residue | > 350°C | 30-45% | Vacuum distillation feed, fuel oil, bitumen |

**Pumparounds**: Liquid side-draws cooled and returned at intermediate heights to remove heat and control vapor load. 2-3 pumparounds typical. Each pumparound condenses rising vapor and controls the internal reflux ratio, reducing condenser load at the top and stabilizing the temperature profile.

**Heat integration**: Crude preheat train — cold crude passes through a series of shell-and-tube heat exchangers connected to hot product streams. Recovers 60-70% of product heat energy before the crude enters the furnace. This is the largest and most complex heat exchanger network in the refinery, typically 10-20 exchangers in series-parallel arrangement. Proper crude preheat design reduces furnace fuel consumption by 30-50%.

### Crude Oil Types & Yield Impact

Different crude oils produce very different product distributions:

| Crude Type | API Gravity | Sulfur | Residue | Naphtha Yield | Diesel Yield |
|------------|-------------|--------|---------|---------------|--------------|
| Light sweet (WTI, Brent) | 35-45° | <0.5% | 15-25% | 25-35% | 20-30% |
| Medium (Arab Light) | 28-34° | 1.5-2.5% | 30-40% | 15-25% | 20-25% |
| Heavy sour (Maya, Venezuelan) | 10-22° | 3-5% | 50-65% | 5-15% | 10-20% |

Light crudes yield more valuable naphtha and middle distillate directly; heavy crudes require more conversion capacity (FCC, hydrocracking) to produce the same products. The choice of crude (and its price differential) is the primary economic variable in refinery operations.

## Vacuum Distillation (VDU)

Atmospheric residue (bp >350°C) cannot be further distilled at atmospheric pressure without thermal cracking (decomposition begins above ~380°C for heavy fractions). The VDU reduces column pressure to 10-30 mmHg absolute, lowering boiling points by 150-200°C and enabling distillation of high-boiling materials at 350-400°C without degradation.

### Column Specifications

- **Pressure**: 10-30 mmHg (absolute) at top, 30-50 mmHg at flash zone
- **Diameter**: 6-12 m (larger than ADU because vapor specific volume expands at low pressure — lower density requires larger cross-section)
- **Internals**: Structured packing (very low pressure drop — critical for vacuum operation) rather than trays. HETP 0.15-0.25 m. Total packing height 6-12 m.
- **Height**: 20-35 m

**Vacuum system**: Multi-stage steam ejectors (3-4 stages with intercondensers). First stage pulls to ~100 mmHg, second to ~25 mmHg, third and fourth to 5-15 mmHg. Steam consumption: 5-15 kg steam per kg of non-condensable gas removed. Alternative: liquid ring vacuum pumps for smaller units.

### Products

| Fraction | Temperature Range (equiv. at 1 atm) | Yield from residue | Primary Use |
|----------|--------------------------------------|---------------------|-------------|
| Light vacuum gas oil (LVGO) | 350-400°C | 10-20% | FCC feedstock, hydrocracker feed |
| Heavy vacuum gas oil (HVGO) | 400-540°C | 20-35% | FCC feedstock, hydrocracker feed |
| Vacuum residue (VR) | > 540°C | 40-60% | Asphalt/bitumen, delayed coking feed, road paving |

**Lubricating oil base stocks**: Premium VDUs produce refined lube base oils from the VGO range. Light neutral (ISO VG 32-46), medium neutral (ISO VG 68-150), and heavy neutral (ISO VG 220-460). These require subsequent solvent extraction (removes aromatics for improved viscosity index) and dewaxing (removes paraffin wax for improved pour point) before becoming finished lubricant base stocks.

## Catalytic Cracking (FCC)

The most important conversion process in modern refining. Converts heavy gas oil (bp 340-550°C, low-value) into gasoline, diesel, and light gases (high-value) using a solid acid catalyst. Produces approximately 40% of all gasoline in the United States.

### Process Description

Preheated gas oil feed (350°C) contacts hot regenerated catalyst (680-720°C) at the bottom of the riser reactor. The catalyst is a fine powder (average particle size ~60 µm) that behaves like a fluid when aerated (fluidized bed). The dramatic temperature increase (feed at 350°C meets catalyst at 700°C) vaporizes the feed and initiates cracking reactions instantly.

**Riser reactor**: The heart of the FCC. Feed and catalyst travel upward together in a vertical pipe (riser, 30-45 m tall, 0.5-1.5 m diameter) at 5-15 m/s velocity. Contact time: only 2-5 seconds. This extremely short contact time is critical — it maximizes selective cracking to gasoline while minimizing secondary reactions (over-cracking to gas and coke).

**Cracking chemistry**: Carbon-carbon bonds in large hydrocarbon molecules break homolytically on acid sites of the zeolite catalyst, producing smaller, more volatile molecules. The reaction is endothermic (heat absorbed), which is why hot catalyst provides the energy. Typical conversions: 70-85% of feed converted to products lighter than the feed.

**Catalyst separation**: At the top of the riser, a cyclone separator (two stages) separates catalyst from product vapor. Catalyst (now deactivated by coke deposited on acid sites, ~1% coke by weight) falls to the stripper section where steam removes entrained hydrocarbons.

**Catalyst regeneration**: Coke-laden catalyst flows to the regenerator — a large fluidized bed vessel where air (not just oxygen — the nitrogen provides fluidization and heat capacity) burns the coke off at 650-720°C. The regenerator is thermally balanced: the exothermic combustion of coke provides all the heat needed for the endothermic cracking reactions. Hot regenerated catalyst flows back to the riser, completing the continuous catalyst circulation loop. Catalyst circulation rate: 20-50 tonnes/minute.

### FCC Yields

| Product | Yield Range | Properties |
|---------|-------------|------------|
| Gasoline (C₅-430°F) | 45-60% | RON 88-93, olefinic, high octane |
| Light cycle oil (LCO) | 15-25% | Diesel-range, high aromatics, low cetane |
| LPG (C₃-C₄) | 10-20% | Propylene valuable as petrochemical feedstock |
| Dry gas (C₁-C₂) | 3-5% | Fuel gas |
| Coke (on catalyst) | 4-7% | Burned in regenerator for process heat |

**FCC gasoline quality**: High research octane number (RON 88-93) but contains olefins and aromatics that may be limited by environmental regulations. FCC gasoline is the largest single component of the US gasoline pool (~35-40% of total).

**Strengths**:
- Highest gasoline yield of any conversion process (45-60% of feed)
- Thermally balanced — coke combustion provides all heat for endothermic cracking
- Continuous catalyst regeneration enables uninterrupted operation for years
- Handles wide range of feedstocks including heavy, high-sulfur gas oils
- Produces valuable propylene byproduct for petrochemical use
- Lower capital cost than hydrocracking per barrel of capacity

**Weaknesses**:
- Maximizes gasoline at the expense of diesel/jet fuel (poor middle distillate selectivity)
- FCC light cycle oil (LCO) has low cetane number (20-35) and high aromatics — requires hydroprocessing before use as diesel
- Gasoline contains olefins subject to environmental regulations
- Catalyst deactivates from metals contamination (vanadium, nickel from feed) and requires continuous makeup (0.5-2 tonnes/day)
- Particulate emissions from catalyst fines require electrostatic precipitators on regenerator flue gas

### FCC Catalyst

Zeolite Y (synthetic faujasite, Na₅₆[(AlO₂)₅₆(SiO₂)₁₃₆]·250H₂O after sodium removal) in an amorphous silica-alumina matrix. Zeolite provides the strong acid sites for cracking; matrix provides macroporosity for pre-cracking large molecules before they enter zeolite pores (pore diameter ~0.74 nm). Catalyst inventory: 100-300 tonnes per unit. Make-up rate: 0.5-2 tonnes/day (catalyst deactivates over time from metals contamination and hydrothermal degradation).

## Hydrocracking

A catalytic process that converts heavy feedstocks (vacuum gas oil, heavy gas oil, atmospheric residue) into high-quality middle distillates (diesel, jet fuel) and naphtha in the presence of hydrogen. Complements FCC: where FCC maximizes gasoline, hydrocracking maximizes diesel and jet fuel.

### Process Conditions

| Parameter | Value |
|-----------|-------|
| Temperature | 350-430°C |
| Pressure | 80-200 bar (7-20 MPa) |
| Hydrogen consumption | 150-400 Nm³/tonne feed |
| Catalyst | Ni-Mo or Ni-W on acidic support (zeolite or amorphous silica-alumina) |
| Liquid hourly space velocity (LHSV) | 0.5-2.0 h⁻¹ |
| Reactor type | Fixed-bed, downflow, trickle-bed (liquid and gas flow concurrently downward over catalyst) |

### Product Yields

| Product | Yield (from VGO) |
|---------|-------------------|
| Naphtha | 15-30% |
| Diesel / jet fuel | 40-65% |
| Unconverted oil (recycle) | 5-15% |

### Advantages over FCC

- **Superior middle distillate quality**: Hydrocracked diesel has cetane number 55-65 (vs. 20-35 for FCC LCO). Hydrocracked jet fuel meets all Jet A-1 specifications directly.
- **Feedstock flexibility**: Handles heavier, higher-sulfur feeds than FCC. Can process coker gas oil, deasphalted oil, and even atmospheric residue.
- **Product flexibility**: Adjusting catalyst and operating conditions can shift yield from gasoline to diesel/jet fuel.
- **Desulfurization**: Hydrogen atmosphere removes sulfur as H₂S (captured in amine units and converted to elemental sulfur in the Claus process).

### Disadvantage

High hydrogen consumption (150-400 Nm³/tonne) requires a dedicated hydrogen production unit (steam methane reformer, ~9 Nm³ H₂ per Nm³ natural gas). High pressure (80-200 bar) demands thick-walled alloy steel reactors — the most expensive single pieces of equipment in a refinery. Capital cost: $3,000-8,000 per daily barrel of capacity.

**Strengths**:
- Best diesel and jet fuel quality of any conversion process (cetane 55-65, meets Jet A-1 directly)
- Flexible product slate — adjustable from gasoline to middle distillate by changing catalyst and conditions
- Handles heaviest, highest-sulfur feeds including coker gas oil and deasphalted oil
- Built-in desulfurization — hydrogen atmosphere removes sulfur as H₂S
- No coke byproduct — all feed converted to liquid products and gases
- Produces high-quality naphtha for petrochemical feedstock

**Weaknesses**:
- Very high hydrogen consumption (150-400 Nm³/tonne) requires dedicated hydrogen plant
- Highest capital cost of any refinery unit ($3,000-8,000 per daily barrel)
- Thick-walled alloy steel reactors (1.25Cr-0.5Mo or 2.25Cr-1Mo) are long-lead procurement items
- High operating pressure (80-200 bar) creates hydrogen embrittlement risk in carbon steel piping
- Catalyst poisoned by nitrogen compounds and metals — feed pretreatment often required
- Lower throughput per unit volume than FCC due to lower space velocity (LHSV 0.5-2.0 h⁻¹)

## Catalytic Reforming

Converts low-octane heavy naphtha (C₆-C₁₀ paraffins and naphthenes, RON 40-60) into high-octane reformate rich in aromatics (RON 95-105) and produces hydrogen as a valuable byproduct.

### Process Conditions

| Parameter | Value |
|-----------|-------|
| Temperature | 490-530°C |
| Pressure | 3-30 bar (low pressure favors aromatics but increases coking) |
| Catalyst | Pt or Pt-Re on chlorided γ-alumina (bifunctional: metal sites for dehydrogenation, acid sites for isomerization and cyclization) |
| LHSV | 1-3 h⁻¹ |
| Hydrogen recycle | 3-6 mol H₂/mol feed (suppresses coking) |

### Key Reactions

1. **Dehydrogenation of naphthenes → aromatics + H₂**: Cyclohexane → benzene + 3H₂ (ΔH = +206 kJ/mol, endothermic). The primary octane-boosting reaction. Produces 3 moles of hydrogen per mole of naphthene converted.
2. **Dehydrocyclization of paraffins → aromatics + H₂**: n-hexane → benzene + 4H₂. Converts linear paraffins (low octane) to aromatics (high octane). Less favorable thermodynamically and slower kinetically than naphthene dehydrogenation.
3. **Isomerization**: n-paraffins → iso-paraffins (modest octane increase, no hydrogen production).
4. **Hydrocracking** (undesired side reaction): C₇+ → C₃-C₄ gases + C₅-C₆ naphtha. Reduces reformate yield. Favored at higher pressure and temperature.

### Products

| Product | Yield | Use |
|---------|-------|-----|
| Reformate (C₅+) | 80-88% of feed | Gasoline blending (RON 95-105), BTX aromatics extraction |
| Hydrogen | 150-300 Nm³/tonne feed | Hydrocracking, hydrotreating hydrogen supply |
| LPG (C₃-C₄) | 5-10% | Fuel gas, petrochemical feedstock |

**BTX aromatics**: The reformate contains 50-70% aromatics: benzene (~6%), toluene (~25%), xylenes (~20%), ethylbenzene (~5%), and higher aromatics. This mixture is the primary source of benzene, toluene, and xylene (BTX) for the petrochemical industry. Separated by solvent extraction (using sulfolane or glycol) followed by fractionation.

## Hydrotreating

Removes sulfur, nitrogen, and metals from petroleum fractions by reaction with hydrogen over a catalyst. Essential for meeting fuel sulfur specifications (ultra-low sulfur diesel <10 ppm S, gasoline <10 ppm S) and protecting downstream catalysts from poisoning.

**Process**: Feed + hydrogen (50-200 Nm³/tonne) pass over Co-Mo/Al₂O₃ or Ni-Mo/Al₂O₃ catalyst at 300-400°C, 30-130 bar. Reactions:

- Desulfurization: R-SR' + 2H₂ → R-H + R'-H + H₂S (sulfur removed as H₂S)
- Denitrogenation: R-NH₂ + 3H₂ → R-H + 2H₂ + NH₃ (nitrogen removed as NH₃)
- Demetallization: Organometallics + H₂ → metals deposit on catalyst + hydrocarbons

H₂S and NH₃ removed from the product stream in a high-pressure separator and stripped in a sour water stripper. H₂S converted to elemental sulfur in the Claus process (2H₂S + O₂ → 2S + 2H₂O over activated alumina catalyst at 250-300°C, 2-3 stages, 95-97% sulfur recovery).

## Product Blending

Refineries produce marketable products by blending components from multiple process units:

### Gasoline Blending

| Component | RON | Typical Blend % |
|-----------|-----|-----------------|
| Light straight-run naphtha | 60-70 | 5-15% |
| Reformate | 95-105 | 25-40% |
| FCC gasoline | 88-93 | 25-35% |
| Hydrocracked naphtha | 80-85 | 5-15% |
| Alkylate | 90-95 | 5-15% |
| Isomerate | 80-88 | 5-10% |
| Ethanol (if blended) | 109 | 0-10% |

**Octane specification**: Regular unleaded RON 91; premium RON 95-98. The blend must meet the target RON while staying within vapor pressure (RVP 60-90 kPa summer, higher winter), benzene (<1%), and sulfur (<10 ppm) specifications.

### Diesel Blending

Blended from straight-run diesel, hydrocracked diesel (highest quality, cetane 55-65), and FCC light cycle oil (lowest quality, cetane 20-35, used in limited quantities). Target: cetane number >50, sulfur <10 ppm, cold filter plugging point below ambient minimum temperature.

## Refinery Configuration & Complexity

### Simple (Hydroskimming) Refinery

ADU + VDU + catalytic reformer + hydrotreaters. Can process light sweet crude into gasoline, diesel, kerosene, fuel oil, and asphalt. Cannot convert heavy residue into lighter products. Minimum ~50,000 bbl/day throughput. Suitable for light crudes.

### Complex (Conversion) Refinery

Adds FCC or hydrocracking + alkylation + coking. Can process heavy sour crudes and convert low-value residue into high-value products. Residual fuel oil yield reduced from 30-40% to 5-10%. This is the configuration that makes economic sense for heavy crudes (which trade at $10-20/barrel discount to light crudes). 100,000+ bbl/day typical.

### Refinery Energy Balance

A refinery consumes 5-10% of its crude oil throughput as fuel (for furnaces, steam generation, hydrogen production). Heat integration (crude preheat train, pumparound heat recovery, cold feed-effluent exchangers) recovers 50-70% of available process heat. The remaining energy is supplied by burning refinery gas (produced internally), fuel oil, and purchased natural gas.

## Safety

**Hydrogen sulfide (H₂S) exposure**: Crude oil and many intermediate streams contain dissolved H₂S. At concentrations above 100 ppm, H₂S paralyzes the olfactory nerve (rotten-egg odor disappears), giving a false sense of safety. At 300 ppm, H₂S causes pulmonary edema; at 700 ppm, rapid unconsciousness and death. Continuous H₂S monitors with alarms at 10 ppm (TWA) and 15 ppm (STEL) are mandatory in all process areas. Emergency SCBA (self-contained breathing apparatus) must be staged within 30 seconds travel time of any H₂S hazard area.

**Hydrocarbon fire and explosion**: Refinery process streams contain flammable hydrocarbons across a wide boiling range. Ethylene (LEL 2.7%, UEL 36%) and hydrogen (LEL 4%, UEL 75%) form explosive mixtures at low concentrations in air. All process equipment handling flammable materials is electrically classified per API 500 (Class I Division 1 or 2). Nitrogen purge before introducing hydrocarbons into any equipment. Firewater system with monitors and foam injection must cover all process areas.

**High-pressure hydrogen embrittlement**: Hydrocracking operates at 80-200 bar with hydrogen-rich gas. Hydrogen diffuses into carbon steel at these conditions, causing embrittlement and sudden brittle fracture. All hydrogen service piping and vessels must use low-alloy Cr-Mo steel (1.25Cr-0.5Mo or 2.25Cr-1Mo) per API 941 (Nelson curves). Inspect welds annually by ultrasonic testing for hydrogen-induced cracking.

**Sulfuric acid and HF alkylation hazards**: Sulfuric acid alkylation units operate with 90-98% H₂SO₄ at 2-10°C. Skin contact causes immediate chemical burns. HF (hydrofluoric acid) alkylation units use 90% HF — HF penetrates skin and attacks bone calcium, causing deep tissue necrosis that may not be immediately painful. Calcium gluconate gel antidote must be available at all HF exposure points. Workers in HF units carry personal calcium gluconate kits.

**Confined space entry**: Vessel entry during turnarounds (planned maintenance shutdowns) requires atmospheric testing (O₂ 19.5-23.5%, LEL <1%, H₂S <10 ppm), rescue plan, and attendant at the entry point. Lockout/tagout all connected piping and energy sources before entry. Hot work permits required for any welding or cutting inside vessels.

## Cross-References

- **Crude oil supply**: [Crude Oil Extraction](extraction.md)
- **Distillation fundamentals**: [Distillation](../chemistry/distillation.md)
- **Fuel end use**: [Fuel Production](../energy/fuels.md), [Heat Engines](../energy/engine.md)
- **Lubricant base stocks**: [Lubricants](../chemistry/lubricants.md)
- **Petrochemical feedstocks**: [Petrochemical Feedstocks](petrochemicals.md)
- **Coal tar alternative**: [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md)

---

*Part of the [Bootciv Tech Tree](../index.md) • [Petroleum Extraction & Refining](./index.md) • [All Domains](../index.md)*
