# Energy Refining

> **Node ID**: energy.refining
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.fuels`](fuels.md), [`mining`](../mining/index.md), [`chemistry`](../chemistry/index.md)
> **Enables**: [`energy.engine`](engine.md), [`petroleum`](../petroleum/index.md)
> **Timeline**: Years 10-25
> **Outputs**: refined_fuel, distilled_oil, cracked_products
> **Critical**: No — refining enables liquid fuels for engines but is not required for the earliest bootstrap stages

## Problem

Energy refining covers the processing of crude fuels into usable forms: fractional distillation of petroleum, coal tar distillation, wood tar processing, and thermal cracking. These refined products power internal combustion engines, gas turbines, and chemical synthesis, and provide feedstocks for the petrochemical industry. Crude petroleum and raw coal tar are not directly usable in engines or chemical processes — they must be separated into fractions with defined boiling ranges and properties.

### Prerequisites

- [Fuels](fuels.md) — raw fuel sources and combustion fundamentals
- [Mining](../mining/index.md) — petroleum and coal extraction
- [Chemistry](../chemistry/index.md) — distillation, cracking, and chemical processing
- [Steel / Metals](../metals/index.md) — pressure vessels, distillation columns, heat exchangers
- [Steam power](steam-power.md) — process heat and steam for distillation

## Petroleum Fractional Distillation

**Strengths**:
- Single column separates crude oil into 6+ useful fractions by boiling point
- Heat integration (feed-product exchange) recovers 60-70% of distillation energy
- Well-understood process — atmospheric distillation has been practiced since the 1850s

**Weaknesses**:
- Requires crude oil supply — a depleting geological resource
- Fired heater consumes 30-40% of crude throughput as fuel gas
- Atmospheric residue (15-30% of crude) needs vacuum distillation for further processing
- Sulfur, nitrogen, and metal contaminants in crude require downstream treatment

Crude petroleum is a complex mixture of hydrocarbons (C₁-C₆₀+) that must be separated into fractions by boiling point. Atmospheric distillation is the primary separation step.

**Atmospheric distillation unit (ADU)**:
- Crude oil preheated to 350-380°C by heat exchange with product streams (recovers 60-70% of distillation heat) and a fired heater (1000-1500°C flame, heats crude to 350-380°C).
- Feed enters the distillation column (30-50 m tall, 3-8 m diameter, 30-50 valve trays) near the bottom. Vapors rise; liquids fall.
- Products drawn off at different heights based on boiling ranges:

| Fraction | Boiling range (°C) | Carbon range | Yield (%) | Uses |
|----------|-------------------|-------------|-----------|------|
| LPG (gases) | <30 | C₃-C₄ | 2-5 | Propane/butane fuel |
| Light naphtha | 30-90 | C₅-C₆ | 5-10 | Gasoline blending, petrochemical feed |
| Heavy naphtha | 90-190 | C₇-C₁₀ | 10-15 | Catalytic reformer feed (→ high-octane gasoline) |
| Kerosene | 190-260 | C₁₀-C₁₄ | 10-15 | Jet fuel, heating oil |
| Light gas oil | 260-340 | C₁₄-C₂₀ | 15-25 | Diesel fuel |
| Heavy gas oil | 340-500 | C₂₀-C₃₅ | 10-20 | Fuel oil, lubricant feed |
| Atmospheric residue | >500 | C₃₅+ | 15-30 | Vacuum distillation feed, asphalt |

- Column overhead temperature: 100-150°C (controlled by reflux ratio). Bottom temperature: 340-360°C. Pressure: 1.0-2.0 bar (slightly above atmospheric).
- Reflux ratio: 3:1 to 8:1 (ratio of condensed overhead liquid returned to column vs. drawn as product). Higher reflux improves separation but increases energy consumption.
- Throughput: 5,000-100,000 barrels/day per column (1 barrel = 159 L).

**Vacuum distillation unit (VDU)**: Atmospheric residue is distilled under vacuum (10-30 mmHg absolute, i.e., 0.013-0.040 bar) to prevent thermal cracking at the high temperatures needed to vaporize heavy fractions. Boiling points drop ~150-200°C under vacuum. Products: vacuum gas oil (VGO, bp 350-550°C atmospheric equivalent, feed for catalytic cracking), vacuum residue (bp >550°C, feed for coking or asphalt production). Column height: 15-25 m, diameter: 5-10 m. Packing (structured packing, not trays) minimizes pressure drop across the column.

## Thermal Cracking

Heavy fractions are cracked (broken into smaller molecules) to increase yield of valuable light products (gasoline, diesel).

**Delayed coking**:
- Heat vacuum residue to 480-500°C in a furnace (residence time 1-3 minutes — short enough to prevent coking in the furnace tubes).
- Transfer to coke drums (10-20 m tall, 5-9 m diameter, two drums alternating on 12-24 hour cycle). Thermal cracking continues in the drum for 12-24 hours.
- Products: gas (C₁-C₄, 10-15%), naphtha (10-15%), gas oil (30-50%), petroleum coke (25-35%).
- Petroleum coke: 85-95% carbon, sulfur 0.5-6.0%, used as fuel or calcined at 1200-1400°C to produce anode-grade coke for [aluminum production](../metals/aluminum.md).
- Decoking: use high-pressure water jets (10,000-20,000 psi, 70-140 MPa) to cut coke out of the drum in 2-4 hours.

**Fluid catalytic cracking (FCC)**: The most important conversion unit in modern refineries:
- Feed: vacuum gas oil (350-550°C boiling range). Catalyst: zeolite (NaY or USY) in silica-alumina matrix, particle size 20-150 μm.
- Reactor: 480-540°C, 1.5-3.0 bar, contact time 1-5 seconds. Hot catalyst (650-700°C from regenerator) contacts feed in the riser (30-40 m tall, 1-1.5 m diameter). Catalyst and oil flow upward together.
- Reactions: C-C bond breaking produces shorter-chain molecules. Yields: gas (15-25%), gasoline (45-55%), light cycle oil (15-25%), heavy cycle oil (5-10%), coke on catalyst (4-7%).
- Regenerator: burn coke off catalyst at 650-720°C with air. Restores catalyst activity. Provides heat for the endothermic cracking reactions (heat balance: exothermic regeneration drives endothermic cracking).
- Catalyst circulation: 20-50 tonnes/minute between reactor and regenerator. Total catalyst inventory: 100-500 tonnes. Catalyst makeup: 1-3 tonnes/day (to replace fines lost to attrition).

## Coal Tar Distillation

Coal carbonization (coke production at 1000-1200°C) produces coal tar as a byproduct (~30-45 L per tonne of coal). Coal tar contains 10,000+ chemical compounds, primarily aromatic hydrocarbons.

**Distillation fractions**:

| Fraction | Boiling range (°C) | Yield (%) | Key products |
|----------|-------------------|-----------|-------------|
| Light oil | <170 | 2-5 | Benzene, toluene, xylene |
| Carbolic oil | 170-230 | 5-10 | Phenol, cresols |
| Naphthalene oil | 230-270 | 8-12 | Naphthalene (crystallized at <80°C) |
| Creosote oil | 270-320 | 15-20 | Creosote wood preservative |
| Anthracene oil | 320-380 | 15-25 | Anthracene, carbazole |
| Coal tar pitch | >380 (residue) | 45-55 | Electrode binder, roofing, road tar |

- Benzene: feedstock for polystyrene, nylon, polyurethane, and synthetic rubber. Production via catalytic reforming of naphtha (modern route) or coal tar distillation (historical).
- Phenol: disinfectant, [Bakelite resin](../polymers/thermosets.md) production, aspirin synthesis.
- Naphthalene: mothballs, phthalic anhydride (plasticizer production), concrete superplasticizer.
- Pitch: binder for carbon electrodes in [aluminum smelting](../metals/aluminum.md) (pitch + coke → anode at 1100-1200°C).

## Wood Tar and Charcoal Production

**Charcoal kiln** (batch):
- Earth kiln: stack wood (5-50 m³) in dome shape, cover with earth and leaves, ignite at bottom, control air supply through adjustable vents. Carbonization temperature: 400-600°C. Duration: 3-14 days. Yield: 20-35% charcoal by weight (fixed carbon 75-90%, calorific value 28-33 MJ/kg). Volatiles (wood tar, acetic acid, methanol) escape through the earth cover or are collected via condensation.
- Brick kiln (improved): rectangular brick chamber (3 × 2 × 2 m), loaded with 5-10 m³ wood. Carbonization in 2-4 days, cooling 2-3 days. Yield: 25-30% charcoal. More consistent quality than earth kiln.

**Wood tar collection**: Pass smoke from charcoal kiln through condenser (series of water-cooled copper or iron pipes at 20-50°C). Condensate separates into three layers: aqueous layer (pyroligneous acid — 5-10% acetic acid, 1-3% methanol), tar layer (wood tar — complex phenolics, used for wood preservation and roofing), and light oil layer (wood spirit, turpentine-like).

**Pyroligneous acid processing**: Neutralize with lime (Ca(OH)₂) → calcium acetate → heat to 500°C → acetone + CaCO₃ (early route to acetone). Or react with ethanol to produce ethyl acetate (solvent). Methanol content: 1-3% (distill at 64.7°C). Pre-industrial methanol production before natural gas reforming.

## Fuel Specifications

**Gasoline**: Octane rating (RON: research octane number; MON: motor octane number; (R+M)/2 = anti-knock index posted on pump). Regular: 87 AKI. Premium: 91-93 AKI. Vapor pressure: 48-103 kPa Reid vapor pressure (seasonally adjusted — higher in winter for cold starting, lower in summer to prevent vapor lock). Sulfur: <10 ppm (ultra-low sulfur). Energy content: 34.2 MJ/L. Density: 0.72-0.78 g/mL. Additives: detergents, corrosion inhibitors, anti-oxidants, anti-icing agents.

**Diesel fuel**: Cetane number: 40-55 (higher = better ignition quality, opposite of octane). Sulfur: <15 ppm (ULSD). Energy: 38.6 MJ/L (13% more than gasoline per liter). Density: 0.82-0.86 g/mL. Cloud point: temperature where wax crystals form (-seasonal specification: -6°C to +5°C depending on climate). Pour point: 3-6°C below cloud point. Flash point: >52°C (minimum, much higher than gasoline's -43°C — safer to handle).

**Jet fuel (Jet A-1)**: Kerosene fraction. Freeze point: -47°C maximum. Flash point: >38°C. Energy: 34.7 MJ/L. Thermal stability: must not deposit coke in fuel lines at 150-200°C. Conductivity: 50-450 pS/m (static dissipator additive prevents static buildup during fueling).

**Heavy fuel oil (HFO)**: Atmospheric or vacuum residue diluted with lighter cutter stock. Viscosity: 10-380 cSt at 100°C (must be preheated to 100-130°C for atomization in burners). Sulfur: 0.5-3.5% (0.5% maximum in ECA emission control areas). Energy: 40-42 MJ/kg. Used in large marine diesel engines, industrial boilers, and power generation.

## Safety in Refining

**Flammability**: All petroleum products are flammable. Gasoline vapor is heavier than air and accumulates at floor level. LEL (lower explosive limit) for gasoline vapor: 1.4% in air. UEL: 7.6%. Below LEL: too lean to ignite. Above UEL: too rich. The hazardous range is 1.4-7.6% — a narrow band that is easily reached during transfer operations.

**Hydrogen sulfide (H₂S)**: Present in many crude oils and natural gas ("sour" crude/gas). Lethal at 300 ppm (IDLH). Detectable odor (rotten eggs) at 1-5 ppm, but olfactory paralysis occurs at 100+ ppm — victims cannot smell the gas that is killing them. Fixed H₂S detectors at 10 ppm alarm. Personal monitors for all workers in H₂S areas. SCBA (self-contained breathing apparatus) for emergency entry.

**Refinery fire protection**: Firewater system: dedicated pumps (2500-10,000 L/min at 10-14 bar), ring main around process units, monitors (fixed water cannons), and foam injection for hydrocarbon fires. Foam: AFFF (aqueous film-forming foam, 3-6% concentration) blankets fuel surface, excluding oxygen. Application rate: 4-8 L/min/m² of fuel surface for hydrocarbon fires. Fixed foam systems on storage tanks (foam chambers mounted on tank roof, delivering foam gently onto fuel surface).

## Product Treating and Upgrading

**Hydrotreating**: Remove sulfur, nitrogen, and metals from petroleum fractions by reaction with hydrogen over a catalyst. Conditions: 300-400°C, 30-130 bar H₂, Co-Mo/Al₂O₃ or Ni-Mo/Al₂O₃ catalyst. Desulfurization: organic sulfur + H₂ → H₂S + hydrocarbons. H₂S removed by amine scrubbing (MEA or MDEA absorbent, regenerated by stripping). Hydrogen consumption: 20-200 scf/bbl depending on feed sulfur content. Produces ultra-low sulfur diesel (<10 ppm S) and gasoline.

**Catalytic reforming**: Convert low-octane naphtha (RON 40-60) to high-octane reformate (RON 95-105) by dehydrogenation of naphthenes to aromatics and dehydrocyclization of paraffins. Catalyst: Pt/Al₂O₃ (0.3-0.6% Pt) with Cl₂ promoter. Conditions: 490-530°C, 5-30 bar. Major reaction: cyclohexane → benzene + 3H₂ (ΔH = +205 kJ/mol, strongly endothermic). Yield: 75-85% reformate + 10-20% H₂ (valuable co-product for hydrotreating). Benzene, toluene, and xylene (BTX) extracted as petrochemical feedstocks.

**Alkylation**: Combine isobutane (C₄) with light olefins (propylene, butylene) to produce high-octane branched-chain alkanes (iso-octane, RON 94-98). Catalyst: concentrated H₂SO₄ (98%) or HF (anhydrous) at 2-10°C. Isobutane:olefin ratio: 5:1 to 15:1 (excess isobutane prevents polymerization). Product: alkylate, the highest-quality gasoline blending component (no aromatics, no olefins, high octane). Production: 500-5,000 barrels/day per unit.

**Isomerization**: Convert normal pentane (n-C₅, RON 62) and normal hexane (n-C₆, RON 25) to their branched isomers (isopentane: RON 93; isohexanes: RON 73-90) over Pt/zeolite catalyst at 250-400°C, 15-30 bar. Improves gasoline front-end octane without changing molecular weight.

## Refinery Energy Balance

A refinery consumes 5-10% of its crude oil throughput as fuel for process heaters and steam generation. Major energy users:
- Atmospheric distillation heater: 80-120 MW thermal (1000-1500°C flame heating crude to 350-380°C)
- Vacuum distillation heater: 30-50 MW
- FCC regenerator: internally balanced (coke combustion provides heat for cracking)
- Catalytic reformer heaters: 40-80 MW (endothermic reactions require continuous heat input)
- Hydrogen production (steam reforming of natural gas): 500-700°C, 15-30 bar, consumes 3.5-4.5 GJ per tonne H₂

Overall refinery energy efficiency: 85-92% (energy in products / energy in crude input). Cogeneration (combined heat and power, CHP): gas turbine burning refinery gas drives electrical generator (5-50 MW), exhaust heat (450-550°C) generates steam in heat recovery boiler (10-100 tonnes/hour). Overall CHP efficiency: 75-85%.

## Wood Gasification

For areas without petroleum access, wood gasification produces a combustible gas mixture (producer gas) from solid biomass:

**Updraft gasifier**: Biomass fed at top, air enters at bottom. Zones from bottom up: ash zone (600-800°C) → combustion zone (1000-1200°C, C + O₂ → CO₂) → reduction zone (800-1000°C, CO₂ + C → 2CO, H₂O + C → CO + H₂) → pyrolysis zone (300-600°C, volatile release) → drying zone (100-200°C). Gas composition: 18-22% CO, 8-12% H₂, 2-4% CH₄, 8-12% CO₂, 50-55% N₂. Heating value: 4-6 MJ/m³ (low, due to nitrogen dilution). Gas must be cooled (to 20-40°C) and cleaned (cyclone + fabric filter removes tars and particulates) before use in internal combustion engines. Engine derating: 30-50% vs. gasoline operation. Wood consumption: 1.0-1.5 kg/kWh.

**Downdraft gasifier** (cleaner gas): Air and biomass move in the same direction (top to bottom). Tars pass through the hot combustion zone (1000-1200°C) and crack, producing cleaner gas with tar content <50 mg/m³ (vs. 10,000-50,000 mg/m³ for updraft). Suitable for engine applications. Gas heating value: 4.5-6.5 MJ/m³. Throughput: 10-500 kg biomass/hour.

## Storage and Transport of Refined Products

**Tank farms**: Above-ground vertical cylindrical steel tanks for bulk storage. Fixed-roof tanks (for heavy fuel oil, diesel): 500-100,000 m³ capacity. Floating-roof tanks (for gasoline, naphtha): roof floats on liquid surface, eliminating vapor space and reducing evaporative losses by 95% vs. fixed roof. Tank height: 10-20 m. Foundation: compacted sand/gravel with impermeable membrane (HDPE liner, 2 mm thick) for secondary containment. Dike (bund wall) around each tank or group: sized to contain 110% of largest tank volume.

**Pipeline transport**: Crude oil pipelines: 200-1200 mm diameter, operating at 20-100 bar, flow rate 500-30,000 m³/hour. Pump stations every 50-150 km. Product pipelines (multi-product): batch different products sequentially with interface mixing <0.5% of batch volume. Pipeline steel: API 5L Grade X42-X70, wall thickness 5-15 mm. External corrosion protection: fusion-bonded epoxy (FBE) coating + cathodic protection (impressed current or sacrificial anodes).

**Rail and road tanker**: Rail tank car: 60-130 m³ capacity, pressure-rated or atmospheric. Bottom loading (preferred — reduces static electricity generation and vapor release). Grounding and bonding during loading/unloading. Road tanker: 15-35 m³, aluminum or stainless steel. Maximum gross vehicle weight: 36-44 tonnes depending on jurisdiction. Delivery rate: 500-1500 L/min through hose with dry-break couplings.

**Marine transport**: Crude oil tanker: 50,000-320,000 deadweight tonnes (DWT). Product tanker: 10,000-80,000 DWT. Loading rate: 2,000-10,000 m³/hour. Ballast water management: segregated ballast tanks (SBT) prevent oil-contaminated ballast discharge. Inert gas system: flue gas (O₂ <8%) or nitrogen blanket prevents explosive atmosphere in cargo tanks.

## Refinery Wastewater Treatment

Process wastewater contains oil (100-500 ppm free oil), sulfides (10-100 ppm), phenols (5-50 ppm), ammonia (10-100 ppm), and suspended solids. Treatment train:

1. API separator: gravity separation removes free oil >150 μm droplet size. Oil rises (density 0.85 vs. water 1.0), skimmed from surface. Removal: 60-80% free oil.
2. Dissolved air flotation (DAF): microscopic air bubbles (30-100 μm) attach to oil droplets and suspended solids, float to surface, skimmed. Removal: 90-95% remaining oil, 80-90% suspended solids. Chemical aids: polyaluminum chloride (5-20 ppm) and polymer (0.5-2 ppm).
3. Biological treatment: activated sludge (aeration 6-12 hours, MLSS 2,000-4,000 mg/L) degrades dissolved organics (BOD removal >90%). Phenol-degrading bacteria acclimatized over 2-4 weeks.
4. Tertiary treatment: sand filtration, activated carbon (for trace organics), or chemical oxidation (ozone or H₂O₂) for final polishing before discharge.

Discharge limits (typical): oil <10 ppm, sulfides <1 ppm, phenols <0.5 ppm, BOD <30 ppm, COD <100 ppm, ammonia <5 ppm.

## Catalytic Reforming Detail

Catalytic reforming is the second most important conversion process after FCC, converting low-octane straight-run naphtha (RON 40-60) into high-octane reformate (RON 95-105) while co-producing hydrogen for hydrotreating.

**Reactions** (all occur simultaneously on Pt/Al₂O₃ catalyst at 490-530°C, 5-30 bar):
- Dehydrogenation of naphthenes: cyclohexane (C₆H₁₂) → benzene (C₆H₆) + 3H₂. Endothermic (ΔH = +205 kJ/mol). Produces 3 moles H₂ per mole naphthene — the primary source of refinery hydrogen.
- Dehydrocyclization of paraffins: n-hexane → benzene + 4H₂. Endothermic. Most difficult reaction — requires high temperature and low pressure.
- Isomerization: n-pentane → isopentane. Mildly exothermic. Improves octane without producing aromatics.
- Hydrocracking (undesired side reaction): C₇+ → C₃ + C₄ at high severity. Consumes H₂, reduces liquid yield.

**Semi-regenerative reformer** (most common design): 3-4 fixed-bed reactors in series with inter-stage firing (heaters between reactors reheat the process stream, which cools due to endothermic reactions). First reactor: fastest reactions (dehydrogenation), smallest bed. Last reactor: slowest reactions (dehydrocyclization), largest bed. Catalyst life: 6-24 months before regeneration (burn off coke at 400-500°C in air). Regeneration takes 5-10 days.

**Continuous regenerative (CCR) reformer**: Catalyst moves continuously through the reactors (by gravity flow) to a regenerator and back. Allows operation at lower pressure (3-5 bar vs. 15-30 bar for semi-regen), which favors dehydrocyclization and produces more aromatics and hydrogen. H₂ yield: 2.5-3.5 wt% of feed (vs. 1.5-2.5 wt% for semi-regen). Catalyst: Pt-Sn/Al₂O₃ or Pt-Re/Al₂O₃. Platinum content: 0.25-0.6% by weight. Total catalyst inventory: 30-100 tonnes.

## Blending and Additives

**Gasoline blending**: Mix components to meet octane, volatility, and specifications:
- Reformate (50-60% of blend): RON 95-105 from catalytic reformer
- FCC gasoline (20-30%): RON 88-93, contains olefins
- Alkylate (5-15%): RON 94-98, no aromatics or olefins
- Isomerate (5-10%): RON 82-89 from isomerization unit
- Butane (2-5%): RON 93-97, adjusts vapor pressure seasonally
- Ethanol (0-10%): RON 109, oxygenate mandated in some jurisdictions
- Additives: detergent (polyetheramine at 50-200 ppm keeps fuel injectors clean), antioxidant (butylated hydroxytoluene at 10-50 ppm prevents gum formation), corrosion inhibitor, anti-icing (isopropanol at 0.5-1.0%)

**Diesel blending**: Similar approach with different components (LCO from FCC, straight-run diesel, hydrocracked diesel). Cold flow improvers (polymer additives at 50-200 ppm lower pour point by 5-15°C by modifying wax crystal growth). Lubricity additives (fatty acid esters at 50-200 ppm protect fuel injection pumps — ultra-low sulfur diesel has poor natural lubricity). Cetane improvers (2-ethylhexyl nitrate at 0.1-0.5% raises cetane number by 3-8 points).

## Natural Gas Processing

Raw natural gas from wells contains methane (70-90%), ethane (1-10%), propane/butane (trace-5%), CO₂ (0-50%), H₂S (0-5%), water vapor, and heavier hydrocarbons. Processing removes impurities and separates NGL (natural gas liquids):

**Acid gas removal**: Amine treating — counter-current absorption in 15-30% MEA (monoethanolamine) or MDEA at 40-50°C. Rich amine regenerated by stripping at 110-120°C. Removes CO₂ to <50 ppm and H₂S to <4 ppm. For high-CO₂ gas, physical solvents (Selexol, Rectisol) are more economical.

**Dehydration**: Triethylene glycol (TEG) absorption at 30-50°C. Dew point depression: 30-50°C. Alternatively, molecular sieve (zeolite 4A or 3A) desiccant beds — two-tower system, one adsorbing while other regenerates at 250-300°C. Pipeline specification: <7 lb H₂O/MMscf (112 mg/m³) to prevent hydrate formation.

**NGL recovery**: Cryogenic turbo-expander process cools gas to -30 to -40°C. Ethane/propane/butane condense and are separated by fractionation. Demethanizer column at -90°C removes methane (product gas). De-ethanizer at -10°C produces ethane (petrochemical feedstock). De-propanizer at 40°C produces propane (LPG). De-butanizer at 70°C produces butane (gasoline blending). NGL recovery: 70-95% of ethane, 95-99% of propane and heavier.

**LNG (liquefied natural gas)**: Cool purified natural gas to -162°C at atmospheric pressure. Volume reduction: 600× (density 0.45 g/mL as liquid vs. gas at STP). Stored in double-wall insulated tanks (inner: 9% Ni steel, outer: carbon steel, perlite insulation). Boil-off rate: 0.05-0.15% per day. Regasification: seawater or submerged combustion vaporizers at 5-15 kg/s flow rate per LNG terminal. Liquefaction energy: ~850 kWh/tonne (12-15% of gas energy content).

### Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Column flooding (pressure spike) | Vapor velocity too high or liquid level too high | Reduce boil-up rate; check reflux ratio; verify tray/packing condition |
| Poor fraction separation (overlapping cuts) | Insufficient reflux or tray damage | Increase reflux ratio; inspect trays/packing; check for channeling |
| Catalyst deactivation (cracking unit) | Coke buildup or metal contamination (Ni, V) from feed | Regenerate catalyst by burning coke with air; switch to lower-metal feed; add metal traps |
| Heat exchanger fouling | Wax deposition or salt buildup from crude | Switch to desalted feed; increase exchanger cleaning frequency; add anti-foulant chemical |
| Gas hydrate formation (gas processing) | Water + high pressure + low temperature | Ensure dehydration upstream (TEG or molecular sieve); inject methanol as emergency antifreeze |
| High sulfur in product (diesel/gasoline) | Desulfurization unit not operating properly | Check H₂ supply pressure; verify catalyst activity; increase reactor temperature |

## See Also

- [Steam Power](steam-power.md) — boilers burning refined fuel oil for steam generation
- [Internal Combustion Engines](engine.md) — gasoline and diesel fueling engines
- [Petrochemicals](../petroleum/petrochemicals.md) — naphtha and gas oil as chemical feedstocks
- [Aluminum Production](../metals/aluminum.md) — petroleum coke for carbon anodes
- [Polymer Production](../polymers/thermoplastics.md) — ethylene and propylene from catalytic cracking
- [Roads](../transport/roads.md) — asphalt from atmospheric residue

[← Back to Energy](index.md)
