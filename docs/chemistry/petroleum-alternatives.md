# Petroleum & Alternative Chemistry

> **Node ID**: `petrochemicals`
> **Domain**: [Petroleum & Alternative Chemistry](./)
> **Dependencies**: `foundations`
> **Enables**: `aircraft`, `energy.ice`, `lubricants`, `polymers.synthetic-rubbers`, `polymers.thermoplastics`, `polymers.thermosets`
> **Timeline**: Years 5-50+
> **Outputs**: gasoline, kerosene, diesel, lubricating_oil, benzene, phenol, ethanol, acetone, methanol, producer_gas, ...

## Problem

Organic chemistry feedstocks fuel the entire materials chain: solvents for semiconductor processing, polymers for packaging and cleanrooms, fuels for transport and furnaces. Without them, the chemical industry stalls at inorganic bulk chemicals. The good news is that there are two independent paths to these molecules. Petroleum is the fast lane; coal tar and fermentation are the reliable fallback.

## Technologies &amp; Systems

### Petroleum Extraction

**Surface seeps** (Foundations-Metallurgy stages):
- Oil seeps to surface naturally in many geological settings. Collect by hand with buckets or by digging shallow pits (1-3 m deep) where oil accumulates. Filter through cloth to remove sand and water. Yield: 5-50 liters/day per seep.
- **Oil springs**: Where oil flows with water, dig collecting pool. Oil floats on water — skim with ladles. This is how the first oil wells began (Titusville, Pennsylvania, 1859).

**Cable-tool drilling** (the Metallurgy-Machine Tools stage transition):
- **Principle**: Heavy steel bit (chisel shape, 50-200 kg) lifted and dropped by cable onto rock floor. Crushes rock. Bail out debris with sand pump (valved tube on separate cable). Repeat.
- **Rig construction**: Wooden derrick 10-20 m tall. Walking beam (rocking beam powered by steam engine or horse). Drill cable on one end, counterweight on other. Cable wraps around drum with ratchet for controlled feed.
- **Casing**: Iron pipes (10-15 cm diameter) driven into hole as drilling progresses. Prevents hole collapse and groundwater contamination. Joints screwed and sealed with lead or hemp packing.
- **Depth**: 50-500 m practical. Penetration rate: 3-10 m/day in soft rock, 0.5-2 m/day in hard rock.
- **Oil recovery**: Once oil-bearing formation is reached, oil flows into well (if under pressure) or must be bailed. Place screen (perforated pipe section) at production depth. Oil flows through perforations, is pumped to surface.

**Rotary drilling** (Energy+):
- **Principle**: Rotating drill bit (tri-cone or diamond-studded) grinds rock. Continuous circulation of drilling mud (water + bentonite clay + barite weighting agent) carries cuttings to surface, cools bit, and holds back formation pressure.
- **Advantages over cable-tool**: Faster (10-50 m/day), reaches deeper (1000-5000+ m), handles soft formations better, continuous mud prevents blowouts.
- **Equipment**: Rotary table (turns drill string), mud pumps (triplex piston pumps, 5-20 MPa pressure), blowout preventer (hydraulic ram seals wellhead in emergency), drill pipe (seamless steel tube, 5-10 m joints screwed together).
- **Mud engineering**: Bentonite clay (4-8% by weight in water) provides viscosity. Barite (BaSO₄) added for density control (mud must exceed formation fluid pressure). pH controlled with NaOH (9.5-10.5). Mud weight typically 1.0-2.0 g/cm³.

### Petroleum Refining

**Simple distillation** (batch still, the Metallurgy-Machine Tools stage transition):
- **Equipment**: Iron or copper pot (200-1000 liters) with removable top. Top connects to condenser (copper coil in water bath, 10-20 m coiled length). Heat from wood fire or coal beneath pot.
- **Process**: Fill pot with crude oil. Heat gradually. Monitor temperature at still head. Collect fractions by temperature range:
  - **Light naphtha** (30-90°C): Solvents, cleaning, later gasoline blending (~5-15% of crude)
  - **Heavy naphtha** (90-150°C): Further processing into gasoline (~10-20%)
  - **Kerosene** (150-250°C): Lamp fuel, heating, jet fuel precursor (~15-25%)
  - **Diesel/gas oil** (250-350°C): Engine fuel, heating oil (~15-25%)
  - **Lubricating oil** (350-500°C): Bearing oil, machine oil, later hydraulic fluid (~10-20%)
  - **Residual fuel oil / asphalt** (>500°C): Boiler fuel, road paving, waterproofing (~15-30%)
- **Yield**: ~40-60% usable products from simple distillation. Residue can be cracked thermally (heat to 450-500°C in closed vessel → breaks large molecules into smaller ones, yields more gasoline/kerosene).
- **Safety**: NEVER distill in sealed vessel — pressure explosion risk. Use open system with vent. Fire risk extreme — have sand and fire blankets ready. No open flames near crude oil. Work outdoors or in well-ventilated shed.

**Fractional distillation column** (continuous, Chemistry+):
- **Construction**: Vertical column 5-20 m tall, 0.3-1.5 m diameter. Iron or steel construction. Internal trays (bubble-cap or sieve trays) every 0.3-0.6 m — each tray is a theoretical separation stage. 15-40 trays typical. Reboiler at bottom (steam-heated or oil-fired). Condenser at top (water-cooled).
- **Operation**: Preheated crude oil fed into column at midpoint (~tray 10-15 of 30). Hot vapors rise through trays. Each tray holds a liquid layer. Rising vapors bubble through liquid — heavier components condense, lighter components strip out. Temperature gradient from bottom (~350°C) to top (~30°C). Draw products at appropriate side ports. Continuous operation — feed in, multiple products out.
- **Control**: Monitor temperature at each draw point. Adjust reboiler heat rate and reflux ratio (fraction of condensed top product returned to column — higher reflux = better separation, lower throughput). Typical reflux ratio 2:1 to 5:1.
- **Product purities**: Much cleaner cuts than batch still. Kerosene fraction: 95%+ pure in boiling range. Critical for consistent fuel quality.

**Thermal cracking** (Chemistry):
- Heat heavy oil fractions to 450-500°C at 0.7-3.5 MPa pressure in tubular furnace. Residence time 10-60 seconds. Large hydrocarbon molecules break into smaller ones. Converts heavy fuel oil into additional gasoline and middle distillates. Yield: ~40-50% gasoline from heavy feed.

### Coal Tar Chemistry (the petroleum-free path)

**Coke oven operation**:
- **Byproduct coke oven**: Horizontal chamber (12-15 m long × 4-6 m tall × 0.4-0.5 m wide) made of refractory brick (silica or alumina). Load with crushed coal (3-5 cm pieces). Seal chamber. Heat externally by burning coke oven gas (from previous batch) in flues between chambers. Temperature reaches 1000-1100°C. Time: 14-24 hours per batch.
- **Products per tonne coal**: ~700 kg coke, ~30-40 kg coal tar, ~10-15 kg light oil (benzene/toluene), ~350-400 m³ coke oven gas (55% H₂, 25% CH₄, heating value ~18 MJ/m³), ~3-5 kg ammonia (as (NH₄)₂SO₄).
- **Coal tar collection**: Tar condenses in gas main and collecting main. Separate from water (ammoniacal liquor) by gravity — tar is denser. Store in tanks.

**Coal tar distillation**:
- Distill coal tar in pot still or fractionating column (cast iron or steel). Gradual heating:
  - **Light oil** (up to 170°C): ~5% of tar. Contains benzene (C₆H₆), toluene (C₇H₈), xylene (C₈H₁₀) — KEY organic chemistry feedstocks. Further fractionated by re-distillation. Benzene boils at 80°C, toluene at 111°C, xylene at 139°C.
  - **Carbolic/creosote oil** (170-230°C): ~10% of tar. Contains phenol (C₆H₅OH), cresols (methylphenols). Phenol extracted with NaOH solution → sodium phenolate → re-precipitate with CO₂ or H₂SO₄. Phenol critical for Bakelite resin, pharmaceuticals, disinfectants.
  - **Naphthalene oil** (230-270°C): ~10% of tar. Naphthalene (C₁₀H₈) crystallizes on cooling (mp 80°C). Purify by sublimation or re-crystallization. Feedstock for phthalic anhydride (plasticizers, dyes).
  - **Anthracene oil** (270-350°C): ~15% of tar. Contains anthracene — dye precursor.
  - **Pitch** (>350°C residue): ~50-60% of tar. Used for roofing, waterproofing, electrode binder (for aluminum smelting and arc furnace electrodes), road binding.

### Fermentation Chemistry

**Ethanol production** (C₂H₅OH):
- **Feedstocks**: Grain (barley, wheat, corn — starch → sugar via malt enzymes), sugar cane/beets (direct sugar), fruit (sugars), potatoes (starch). Starch must be converted to sugar first (malting/sprouting grain produces amylase enzymes that break starch into maltose).
- **Malting**: Soak grain in water 2-3 days. Spread on floor 5-7 days, keep moist and 15-20°C. Grain sprouts, producing amylase. Dry at 50-60°C to stop germination (kilning). Crush malt to coarse grist.
- **Mashing**: Mix grist with hot water (65-68°C) in insulated vessel. Hold 1-2 hours. Amylase converts starch to maltose (C₁₂H₂₂O₁₁) and glucose (C₆H₁₂O₆). Test with iodine — blue = starch still present, no blue = conversion complete. Strain liquid (wort) from grain.
- **Fermentation**: Cool wort to 20-30°C. Add yeast (Saccharomyces cerevisiae — from previous batch or wild-captured). Ferment 3-7 days in closed vessel with airlock (CO₂ escapes, air cannot enter). Yeast converts sugar → ethanol + CO₂. Maximum ~12-15% ABV (alcohol kills yeast above ~15%).
  - C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂ (glucose → ethanol + carbon dioxide)
- **Distillation**: Distill fermented wash in pot still or column. Ethanol boils at 78.3°C. First distillation: ~40-50% ABV. Second distillation: ~70-80% ABV. Third distillation or fractionating column: ~95% ABV (azeotrope — cannot exceed 95.6% by simple distillation). For anhydrous (>99%), add quicklime (CaO) to absorb water, re-distill, or use molecular sieves.
- **Applications**: Solvent (dissolves resins, oils, organic compounds), fuel (ethanol burns cleanly), feedstock for acetic acid, ethyl acetate, ether, and many other chemicals. Denature with methanol or bitterants to prevent consumption if desired for industrial use.

**Acetone-butanol fermentation** (Weizmann process):
- **Organism**: Clostridium acetobutylicum (anaerobic bacterium). Can be isolated from soil or preserved culture.
- **Process**: Ferment starch (corn, potato, or grain mash) at 35-37°C for 48-72 hours. Products: acetone (~30%), n-butanol (~60%), ethanol (~10%) by volume, plus CO₂ and H₂ gases.
- **Distillation**: Separate by fractional distillation. Acetone bp 56°C, ethanol bp 78°C, n-butanol bp 118°C.
- **Applications**: Acetone — solvent for resins, fats, plastics; key ingredient in nitrocellulose dope (Aircraft aircraft). n-Butanol — solvent, feedstock for butyl rubber and esters.

**Acetic acid production** (CH₃COOH):
- **Vinegar method**: Expose ethanol solution to air with Acetobacter bacteria (present on fruit surfaces). Aerobic fermentation at 25-30°C for days-weeks. Produces 5-12% acetic acid. Slow but simple.
- **Chemical oxidation**: Pass ethanol vapor over heated copper catalyst (copper gauze at 300-400°C) with air. Ethanol oxidizes to acetaldehyde (CH₃CHO), then to acetic acid. Faster, higher concentration.
- **Applications**: Vinegar (food preservation), cellulose acetate (photographic film, synthetic fibers), acetic anhydride (aspirin synthesis), metal etching, solvent.

**Methanol production** (CH₃OH, wood alcohol):
- **Wood pyrolysis**: Heat hardwood in closed iron retort to 400-500°C. Destructive distillation produces: charcoal (solid), wood tar (liquid), pyroligneous acid (aqueous condensate containing methanol, acetic acid, acetone). Distill pyroligneous acid — methanol boils at 64.7°C. Yield: ~1-2% methanol by weight of wood. Low yield but works with the Metallurgy stage technology.
- **Synthetic methanol** (Chemistry+): React CO + 2H₂ over ZnO/Cr₂O₃ catalyst at 300-400°C, 20-30 MPa. Requires purified synthesis gas (from coal gasification or natural gas reforming). Much higher yield and purity.

### Wood Gasification &amp; Pyrolysis

**Producer gas** (CO + H₂ + N₂):
- **Gas producer**: Cylindrical shaft 1-3 m diameter × 2-5 m tall, lined with refractory brick. Fill with lump charcoal or coke. Ignite bottom. Blow limited air upward through bed. Incomplete combustion produces CO (carbon monoxide) instead of CO₂.
  - C + ½O₂ → CO (exothermic, provides heat)
  - C + H₂O → CO + H₂ (endothermic water-gas reaction — add steam to enrich gas)
- **Gas composition**: ~25% CO, ~10% H₂, ~60% N₂, ~5% CO₂. Heating value ~5-6 MJ/m³ (low, but usable).
- **Applications**: Run internal combustion engines (modified — need lower compression ratio), furnace heating, substitute for natural gas. The "wood gasifier" powered vehicles during WWII petroleum shortages.
- **Cleaning**: Pass gas through water scrubber (removes tars and particulates), sawdust filter, then cyclone separator. Critical for engine use — tars will destroy engine quickly.

**Charcoal retort** (for charcoal + gas + tar):
- **Batch retort**: Iron or steel cylinder (1-2 m diameter × 2-4 m long), loaded with hardwood billets. Seal. Heat externally (burn wood waste or previous batch gas). Internal wood pyrolyzes: releases volatile gases (which can be burned to heat the retort — self-sustaining after initial heating), leaves charcoal. Temperature 400-600°C. Time: 12-24 hours. Cool before opening (charcoal ignites spontaneously when hot and exposed to air). Yield: 25-35% charcoal by weight.

### Synthetic Polymers
Petrochemicals produces the chemical feedstocks (phenol, formaldehyde, ethanol, acetone, cellulose, lignin) that serve as monomer and resin precursors. Polymerization processes, material properties, and end-use applications are covered in [**Polymers & Composites**](../polymers/index.md).
- Aircraft fuels and dopes: gasoline distillation fraction for piston engines; acetone for nitrocellulose dope production — see [Aircraft](../transport/aviation.md)

### The Dual Path Principle
- **Petroleum available**: everything accelerates. Cheap solvents, fuels, monomers, polymers. Decades saved.
- **No petroleum**: coal tar + fermentation + wood chemistry produces the same core molecules (benzene, phenol, ethanol, acetone, methanol, acetic acid). Slower, smaller scale, more labor, but entirely viable.
- Plan for both. Do not assume petroleum.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Metallurgy | Coke ovens → coal tar; surface petroleum; wood pyrolysis |
| Energy | Petroleum drilling (steam-powered); producer gas for engines |
| Chemistry | Fractional distillation columns; bulk organic solvents and acids |
| Advanced Materials | Feedstocks for advanced polymers, high-temp resins, composites |
| Specialty Gases | Solvents, photoresist precursors, packaging polymers |
| Aircraft | Gasoline fuel, acetone for dope, solvents for aircraft finishes |
| Polymers | Polymerization of feedstocks into engineering materials |
| the Silicon-Photolithography stage transition | Ultra-pure solvents for wafer cleaning and processing |

## Key Deliverables

- Coke oven operation with coal tar collection
- Fractional distillation capability (crude oil or coal tar)
- Fermentation-derived solvents (ethanol, acetone, acetic acid)
- Producer gas / wood gas for engines and heating
- Early synthetic polymers (Bakelite, celluloid, cellulose derivatives)
- Dual-path feedstock strategy documented

## Safety Concerns

- **Petroleum vapors**: Flammable, heavier than air, accumulate in low spots. No open flames. Adequate ventilation.
- **Benzene**: Carcinogen. Minimize inhalation and skin contact. Use in well-ventilated areas.
- **CO (producer gas)**: Odorless, lethal. Never operate gasifier indoors. Vent all exhaust. CO detectors essential.
- **Methanol**: Toxic if ingested — causes blindness and death. Can be absorbed through skin. Label clearly, never store near food/drink.
- **Distillation fires**: Have sand, fire blankets, and water spray. Never distill in sealed vessels. Pressure relief valves on all heated vessels.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
