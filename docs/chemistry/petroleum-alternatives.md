# Petroleum & Alternative Chemistry

> **Node ID**: chemistry.petroleum-alternatives
> **Domain**: [Petroleum & Alternative Chemistry](./index.md)
> **Dependencies**: [`foundations`](../foundations/index.md)
> **Enables**: [`transport.aviation`](../transport/aviation.md), [`energy.cooling`](../energy/cooling.md), [`chemistry.lubricants`](lubricants.md), [`polymers.rubber.synthetic`](../polymers/synthetic.md), [`polymers.thermoplastics`](../polymers/thermoplastics.md), [`polymers.thermosets`](../polymers/thermosets.md)
> **Timeline**: Years 5-50+
> **Outputs**: gasoline, kerosene, diesel, lubricating_oil, benzene, phenol, ethanol, acetone, methanol, producer_gas, ...

## Problem

Organic chemistry feedstocks fuel the entire materials chain: solvents for semiconductor processing, polymers for packaging and cleanrooms, fuels for transport and furnaces. Without them, the chemical industry stalls at inorganic bulk chemicals. The good news is that there are two independent paths to these molecules. Petroleum is the fast lane; coal tar and fermentation are the reliable fallback.

## Technologies & Systems

### Petroleum Extraction

**[Surface seeps](../glossary/surface-seeps.md)** (Foundations-Metallurgy stages):
- Oil seeps to surface naturally in many geological settings. Collect by hand with buckets or by digging shallow pits (1-3 m deep) where oil accumulates. Filter through cloth to remove sand and water. Yield: 5-50 liters/day per seep.
- **Oil springs**: Where oil flows with water, dig collecting pool. Oil floats on water — skim with ladles. This is how the first oil wells began (Titusville, Pennsylvania, 1859).

**[Cable-tool drilling](../glossary/cable-tool-drilling.md)** (the Metallurgy-Machine Tools stage transition):
- **Principle**: Heavy steel bit (chisel shape, 50-200 kg) lifted and dropped by cable onto rock floor. Crushes rock. Bail out debris with sand pump (valved tube on separate cable). Repeat.
- **Rig construction**: Wooden derrick 10-20 m tall. Walking beam (rocking beam powered by steam engine or horse). Drill cable on one end, counterweight on other. Cable wraps around drum with ratchet for controlled feed.
- **Casing**: Iron pipes (10-15 cm diameter) driven into hole as drilling progresses. Prevents hole collapse and groundwater contamination. Joints screwed and sealed with lead or hemp packing.
- **Depth**: 50-500 m practical. Penetration rate: 3-10 m/day in soft rock, 0.5-2 m/day in hard rock.
- **Oil recovery**: Once oil-bearing formation is reached, oil flows into well (if under pressure) or must be bailed. Place screen (perforated pipe section) at production depth. Oil flows through perforations, is pumped to surface.

**Rotary drilling**:
- **Principle**: Rotating drill bit (tri-cone or diamond-studded) grinds rock. Continuous circulation of drilling mud (water + bentonite clay + barite weighting agent) carries cuttings to surface, cools bit, and holds back formation pressure.
- **Advantages over cable-tool**: Faster (10-50 m/day), reaches deeper (1000-5000+ m), handles soft formations better, continuous mud prevents blowouts.
- **Equipment**: Rotary table (turns drill string), mud pumps (triplex piston pumps, 5-20 MPa pressure), blowout preventer (hydraulic ram seals wellhead in emergency), drill pipe (seamless steel tube, 5-10 m joints screwed together).
- **Mud engineering**: Bentonite clay (4-8% by weight in water) provides viscosity. Barite (BaSO₄) added for density control (mud must exceed formation fluid pressure). pH controlled with NaOH (9.5-10.5). Mud weight typically 1.0-2.0 g/cm³.

### Petroleum Refining

**[Simple distillation](../glossary/simple-distillation.md)** (batch still, the Metallurgy-Machine Tools stage transition):
- **Equipment**: Iron or copper pot (200-1000 liters) with removable top. Top connects to condenser (copper coil in water bath, 10-20 m coiled length). Heat from wood fire or coal beneath pot.
- **Process**: Fill pot with crude oil. Heat gradually. Monitor temperature at still head. Collect fractions by temperature range:
  - **[Light naphtha](../glossary/light-naphtha.md)** (30-90°C): Solvents, cleaning, later gasoline blending (~5-15% of crude)
  - **[Heavy naphtha](../glossary/heavy-naphtha.md)** (90-150°C): Further processing into gasoline (~10-20%)
  - **[Kerosene](../glossary/kerosene.md)** (150-250°C): Lamp fuel, heating, jet fuel precursor (~15-25%)
  - **[Diesel/gas oil](../glossary/dieselgas-oil.md)** (250-350°C): Engine fuel, heating oil (~15-25%)
  - **[Lubricating oil](../glossary/lubricating-oil.md)** (350-500°C): Bearing oil, machine oil, later hydraulic fluid (~10-20%)
  - **[Residual fuel oil / asphalt](../glossary/residual-fuel-oil-asphalt.md)** (>500°C): Boiler fuel, road paving, waterproofing (~15-30%)
- **Yield**: ~40-60% usable products from simple distillation. Residue can be cracked thermally (heat to 450-500°C in closed vessel → breaks large molecules into smaller ones, yields more gasoline/kerosene).
- **Safety**: NEVER distill in sealed vessel — pressure explosion risk. Use open system with vent. Fire risk extreme — have sand and fire blankets ready. No open flames near crude oil. Work outdoors or in well-ventilated shed.

**[Fractional distillation column](../glossary/fractional-distillation-column.md)** (continuous):
- **Construction**: Vertical column 5-20 m tall, 0.3-1.5 m diameter. Iron or steel construction. Internal trays (bubble-cap or sieve trays) every 0.3-0.6 m — each tray is a theoretical separation stage. 15-40 trays typical. Reboiler at bottom (steam-heated or oil-fired). Condenser at top (water-cooled).
- **Operation**: Preheated crude oil fed into column at midpoint (~tray 10-15 of 30). Hot vapors rise through trays. Each tray holds a liquid layer. Rising vapors bubble through liquid — heavier components condense, lighter components strip out. Temperature gradient from bottom (~350°C) to top (~30°C). Draw products at appropriate side ports. Continuous operation — feed in, multiple products out.
- **Control**: Monitor temperature at each draw point. Adjust reboiler heat rate and reflux ratio (fraction of condensed top product returned to column — higher reflux = better separation, lower throughput). Typical reflux ratio 2:1 to 5:1.
- **Product purities**: Much cleaner cuts than batch still. Kerosene fraction: 95%+ pure in boiling range. Critical for consistent fuel quality.

**[Thermal cracking](../glossary/thermal-cracking.md)** (Chemistry):
- Heat heavy oil fractions to 450-500°C at 0.7-3.5 MPa pressure in tubular furnace. Residence time 10-60 seconds. Large hydrocarbon molecules break into smaller ones. Converts heavy fuel oil into additional gasoline and middle distillates. Yield: ~40-50% gasoline from heavy feed.

### Coal Tar Chemistry (the petroleum-free path)

**Coke oven operation**:
- **Byproduct coke oven**: Horizontal chamber (12-15 m long × 4-6 m tall × 0.4-0.5 m wide) made of refractory brick (silica or alumina). Load with crushed coal (3-5 cm pieces). Seal chamber. Heat externally by burning coke oven gas (from previous batch) in flues between chambers. Temperature reaches 1000-1100°C. Time: 14-24 hours per batch.
- **Products per tonne coal**: ~700 kg coke, ~30-40 kg coal tar, ~10-15 kg light oil (benzene/toluene), ~350-400 m³ coke oven gas (55% H₂, 25% CH₄, heating value ~18 MJ/m³), ~3-5 kg ammonia (as (NH₄)₂SO₄).
- **Coal tar collection**: Tar condenses in gas main and collecting main. Separate from water (ammoniacal liquor) by gravity — tar is denser. Store in tanks.

**Coal tar distillation**:
- Distill coal tar in pot still or fractionating column (cast iron or steel). Gradual heating:
  - **[Light oil](../glossary/light-oil.md)** (up to 170°C): ~5% of tar. Contains benzene (C₆H₆), toluene (C₇H₈), xylene (C₈H₁₀) — KEY organic chemistry feedstocks. Further fractionated by re-distillation. Benzene boils at 80°C, toluene at 111°C, xylene at 139°C.
  - **[Carbolic/creosote oil](../glossary/carboliccreosote-oil.md)** (170-230°C): ~10% of tar. Contains phenol (C₆H₅OH), cresols (methylphenols). Phenol extracted with NaOH solution → sodium phenolate → re-precipitate with CO₂ or H₂SO₄. Phenol critical for Bakelite resin, pharmaceuticals, disinfectants.
  - **[Naphthalene oil](../glossary/naphthalene-oil.md)** (230-270°C): ~10% of tar. Naphthalene (C₁₀H₈) crystallizes on cooling (mp 80°C). Purify by sublimation or re-crystallization. Feedstock for phthalic anhydride (plasticizers, dyes).
  - **[Anthracene oil](../glossary/anthracene-oil.md)** (270-350°C): ~15% of tar. Contains anthracene — dye precursor.
  - **[Pitch](../glossary/pitch.md)** (>350°C residue): ~50-60% of tar. Used for roofing, waterproofing, electrode binder (for aluminum smelting and arc furnace electrodes), road binding.

### Fermentation Chemistry

**[Ethanol production](../glossary/ethanol-production.md)** (C₂H₅OH):
- **Feedstocks**: Grain (barley, wheat, corn — starch → sugar via malt enzymes), sugar cane/beets (direct sugar), fruit (sugars), potatoes (starch). Starch must be converted to sugar first (malting/sprouting grain produces amylase enzymes that break starch into maltose).
- **Malting**: Soak grain in water 2-3 days. Spread on floor 5-7 days, keep moist and 15-20°C. Grain sprouts, producing amylase. Dry at 50-60°C to stop germination (kilning). Crush malt to coarse grist.
- **Mashing**: Mix grist with hot water (65-68°C) in insulated vessel. Hold 1-2 hours. Amylase converts starch to maltose (C₁₂H₂₂O₁₁) and glucose (C₆H₁₂O₆). Test with iodine — blue = starch still present, no blue = conversion complete. Strain liquid (wort) from grain.
- **Fermentation**: Cool wort to 20-30°C. Add yeast (Saccharomyces cerevisiae — from previous batch or wild-captured). Ferment 3-7 days in closed vessel with airlock (CO₂ escapes, air cannot enter). Yeast converts sugar → ethanol + CO₂. Maximum ~12-15% ABV (alcohol kills yeast above ~15%).
  - C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂ (glucose → ethanol + carbon dioxide)
- **Distillation**: Distill fermented wash in pot still or column. Ethanol boils at 78.3°C. First distillation: ~40-50% ABV. Second distillation: ~70-80% ABV. Third distillation or fractionating column: ~95% ABV (azeotrope — cannot exceed 95.6% by simple distillation). For anhydrous (>99%), add quicklime (CaO) to absorb water, re-distill, or use molecular sieves.
- **Applications**: Solvent (dissolves resins, oils, organic compounds), fuel (ethanol burns cleanly), feedstock for acetic acid, ethyl acetate, ether, and many other chemicals. Denature with methanol or bitterants to prevent consumption if desired for industrial use.

**[Acetone-butanol fermentation](../glossary/acetone-butanol-fermentation.md)** (Weizmann process):
- **Organism**: Clostridium acetobutylicum (anaerobic bacterium). Can be isolated from soil or preserved culture.
- **Process**: Ferment starch (corn, potato, or grain mash) at 35-37°C for 48-72 hours. Products: acetone (~30%), n-butanol (~60%), ethanol (~10%) by volume, plus CO₂ and H₂ gases.
- **Distillation**: Separate by fractional distillation. Acetone bp 56°C, ethanol bp 78°C, n-butanol bp 118°C.
- **Applications**: Acetone — solvent for resins, fats, plastics; key ingredient in nitrocellulose dope (aircraft fabric). n-Butanol — solvent, feedstock for butyl rubber and esters.

**[Acetic acid production](../glossary/acetic-acid-production.md)** (CH₃COOH):
- **Vinegar method**: Expose ethanol solution to air with Acetobacter bacteria (present on fruit surfaces). Aerobic fermentation at 25-30°C for days-weeks. Produces 5-12% acetic acid. Slow but simple.
- **Chemical oxidation**: Pass ethanol vapor over heated copper catalyst (copper gauze at 300-400°C) with air. Ethanol oxidizes to acetaldehyde (CH₃CHO), then to acetic acid. Faster, higher concentration.
- **Applications**: Vinegar (food preservation), cellulose acetate (photographic film, synthetic fibers), acetic anhydride (aspirin synthesis), metal etching, solvent.

**[Methanol production](../glossary/methanol-production.md)** (CH₃OH, wood alcohol):
- **Wood pyrolysis**: Heat hardwood in closed iron retort to 400-500°C. Destructive distillation produces: charcoal (solid), wood tar (liquid), pyroligneous acid (aqueous condensate containing methanol, acetic acid, acetone). Distill pyroligneous acid — methanol boils at 64.7°C. Yield: ~1-2% methanol by weight of wood. Low yield but works with the Metallurgy stage technology.
- **Synthetic methanol**: React CO + 2H₂ over ZnO/Cr₂O₃ catalyst at 300-400°C, 20-30 MPa. Requires purified synthesis gas (from coal gasification or natural gas reforming). Much higher yield and purity.

### Wood Gasification & Pyrolysis

**[Producer gas](../glossary/producer-gas.md)** (CO + H₂ + N₂):
- **Gas producer**: Cylindrical shaft 1-3 m diameter × 2-5 m tall, lined with refractory brick. Fill with lump charcoal or coke. Ignite bottom. Blow limited air upward through bed. Incomplete combustion produces CO (carbon monoxide) instead of CO₂.
  - C + ½O₂ → CO (exothermic, provides heat)
  - C + H₂O → CO + H₂ (endothermic water-gas reaction — add steam to enrich gas)
- **Gas composition**: ~25% CO, ~10% H₂, ~60% N₂, ~5% CO₂. Heating value ~5-6 MJ/m³ (low, but usable).
- **Applications**: Run internal combustion engines (modified — need lower compression ratio), furnace heating, substitute for natural gas. The "wood gasifier" powered vehicles during WWII petroleum shortages.
- **Cleaning**: Pass gas through water scrubber (removes tars and particulates), sawdust filter, then cyclone separator. Critical for engine use — tars will destroy engine quickly.

**[Charcoal retort](../glossary/charcoal-retort.md)** (for charcoal + gas + tar):
- **Batch retort**: Iron or steel cylinder (1-2 m diameter × 2-4 m long), loaded with hardwood billets. Seal. Heat externally (burn wood waste or previous batch gas). Internal wood pyrolyzes: releases volatile gases (which can be burned to heat the retort — self-sustaining after initial heating), leaves charcoal. Temperature 400-600°C. Time: 12-24 hours. Cool before opening (charcoal ignites spontaneously when hot and exposed to air). Yield: 25-35% charcoal by weight.

### Synthetic Polymers
Petrochemicals produces the chemical feedstocks (phenol, formaldehyde, ethanol, acetone, cellulose, lignin) that serve as monomer and resin precursors. Polymerization processes, material properties, and end-use applications are covered in [**[Polymers & Composites](../polymers/index.md)**](../polymers/index.md).
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

### Catalytic Cracking (FCC)

**[Fluid catalytic cracking](../glossary/fluid-catalytic-cracking.md)** converts heavy gas oil (bp 340-550°C) into gasoline, diesel, and light gases using a zeolite catalyst at 500-550°C. The most important conversion process in a modern refinery — produces ~40% of US gasoline.

**Process**: Preheated gas oil feed (350°C) contacts hot regenerated catalyst (700°C) in a riser reactor. The catalyst is a fine powder (60 µm) that behaves like a fluid when aerated. Reaction time in the riser: 2-5 seconds. Cracking reactions break C-C bonds in large molecules, producing smaller products. Catalyst deactivated by coke — separated in cyclones, regenerated by burning coke in air at 650-700°C (provides heat for cracking — thermally balanced). Product: gasoline (50-60%), light cycle oil/diesel (15-25%), LPG (10-20%), dry gas + coke (5-10%).

**Catalyst**: Zeolite Y (sodium aluminosilicate, pore size ~0.74 nm) in clay matrix. Acid sites promote carbonium ion cracking. Inventory: 100-300 tonnes per unit, circulated at 20-50 tonnes/minute between reactor and regenerator.

### Steam Cracking (Ethylene Production)

The most important petrochemical process — produces ethylene (C₂H₄) and propylene (C₃H₆), building blocks for most plastics. Hydrocarbon feed (ethane, propane, naphtha, or gas oil) mixed with steam (diluent, reduces coking) and heated to 800-900°C in a tubular furnace (residence time 0.1-0.5 seconds). Short residence time maximizes ethylene yield. Furnace tubes: centrifugally cast HK-40 alloy (25Cr-20Ni-Fe), 50-150 mm ID. Product gases quenched in transfer line exchanger (generates high-pressure steam), then separated by cryogenic distillation: H₂ + CH₄ (fuel gas), ethylene (99.9%), ethane (recycled), propylene, C₄ fraction (butadiene, butenes), pyrolysis gasoline (BTX). Yields: ethane feed → 80% ethylene; naphtha feed → 35% ethylene, 15% propylene, 10% BTX.

### Ethanol-to-Ethylene (Non-Petroleum Route)

Critical bootstrap route: ethanol (from fermentation) dehydrated over alumina (Al₂O₃) catalyst at 170°C to produce ethylene. C₂H₅OH → C₂H₄ + H₂O. Yield: 95-99%. Enables polyethylene production without petroleum. From ethylene: polyethylene (50%), ethylene oxide → ethylene glycol (antifreeze), PVC (via vinyl chloride), polystyrene (via styrene).

### Catalytic Reforming (Aromatics)

Converts low-octane naphtha (C₆-C₁₀ paraffins) into high-octane reformate rich in aromatics (benzene, toluene, xylene — BTX) and hydrogen. Pt-Re catalyst on chlorided alumina at 490-530°C, 1-3 MPa. Reactions: dehydrogenation of naphthenes → aromatics (produces H₂), dehydrocyclization of paraffins → aromatics. Product: reformate (RON 95-105) for gasoline blending. BTX for chemicals: benzene → styrene → polystyrene; toluene → TNT, polyurethane; xylene → PET polyester. H₂ byproduct: 100-200 Nm³/tonne — valuable for ammonia synthesis and hydroprocessing.

### Natural Gas Processing

Raw natural gas contains methane (70-90%), ethane, propane, butane, CO₂, H₂S, N₂, and water. Processing steps: (1) **Sweetening**: Amine treating — absorb H₂S and CO₂ in aqueous amine solution (MEA or MDEA), regenerate by heating to strip acid gases. (2) **Dehydration**: Glycol absorption (triethylene glycol) or molecular sieve desiccant. (3) **NGL recovery**: Turboexpander or refrigeration to -30 to -40°C to condense ethane, propane, butane. Separated by fractionation. (4) **LNG**: Liquefy methane at -162°C for transport by ship (1/600 volume reduction).

## Safety Concerns

- **Petroleum vapors**: Flammable, heavier than air, accumulate in low spots. No open flames. Adequate ventilation.
- **Benzene**: Carcinogen. Minimize inhalation and skin contact. Use in well-ventilated areas.
- **CO (producer gas)**: Odorless, lethal. Never operate gasifier indoors. Vent all exhaust. CO detectors essential.
- **Methanol**: Toxic if ingested — causes blindness and death. Can be absorbed through skin. Label clearly, never store near food/drink.
- **Distillation fires**: Have sand, fire blankets, and water spray. Never distill in sealed vessels. Pressure relief valves on all heated vessels.
### Fischer-Tropsch Synthesis

**Process**: Converts syngas (CO + H₂) into linear hydrocarbons over iron (Fe) or cobalt (Co) catalyst at 200-350°C and 10-40 bar pressure. The chain-growth reaction: nCO + (2n+1)H₂ → CnH₂n+2 + nH₂O. Product distribution follows Anderson-Schulz-Flory statistics, yielding a broad mix: C₁-C₄ gases (methane through butane), C₅-C₁₂ gasoline-range hydrocarbons, C₁₂-C₂₀ diesel-range hydrocarbons, and C₂₀+ waxes. Selectivity is controlled by temperature and catalyst choice. Higher temperature shifts selectivity toward lighter products (more gas, less wax). Cobalt catalysts favor heavier, straight-chain paraffins with high selectivity to diesel and wax. Iron catalysts produce more olefins and oxygenates (alcohols, aldehydes) alongside paraffins, and also catalyze the water-gas shift reaction (CO + H₂O → CO₂ + H₂), allowing use of syngas with lower H₂:CO ratios typical of coal gasification.

**Coal-to-liquids economics**: One tonne of coal yields 2-3 barrels of synthetic crude via Fischer-Tropsch after gasification to syngas. The SASOL plant in South Africa has produced approximately 150,000 barrels per day of synthetic fuels from coal since 1955, demonstrating decades of commercial-scale operation without petroleum. Capital intensity is high ($100,000-200,000 per daily barrel of capacity), but viable when crude oil prices exceed $60-80/barrel or when energy independence is prioritized over cost.

### Bio-Based Alternatives

**[Vegetable oil transesterification](../glossary/vegetable-oil-transesterification.md)** (biodiesel): React 100 kg vegetable oil (soybean, rapeseed, palm, or sunflower) with 11 kg methanol and 0.5 kg sodium hydroxide catalyst at 60-65°C for 1-2 hours with stirring. Products: ~97 kg fatty acid methyl ester (biodiesel) + ~11 kg glycerol by-product. Biodiesel properties: cetane number 48-65, energy density 37 MJ/kg (9% less than petroleum diesel), pour point -3 to +15°C depending on feedstock. Compatible with existing diesel engines at blend ratios up to B20 (20% biodiesel) without modification; higher blends require fuel system seal changes.

**Cellulosic ethanol**: Acid hydrolysis (dilute H₂SO₄ at 0.5-2% concentration, 120-200°C, 10-60 minutes) or enzymatic hydrolysis (cellulase enzymes at 45-50°C, pH 4.8-5.2, 48-120 hours) breaks cellulose into fermentable sugars. Yields: 280-340 liters ethanol per tonne of dry biomass (corn stover, wheat straw, wood chips). Enzymatic route gives higher yield but requires enzyme production capability. Acid route is simpler but produces fermentation inhibitors (furfural, HMF) that must be removed or neutralized before yeast fermentation.

**Fischer-Tropsch catalyst preparation**: Cobalt-based FT catalyst is prepared by impregnating γ-alumina or silica support with cobalt nitrate solution, drying at 110°C, and calcining at 300-400°C to convert cobalt nitrate to Co₃O₄. Typical cobalt loading: 15-25% by weight. A promoter (ruthenium at 0.1-1% or platinum at 0.05-0.5%) enhances reduction of Co₃O₄ to active metallic Co during hydrogen activation at 350-400°C. Iron-based catalyst for high-temperature FT: precipitated Fe₂O₃ with Cu (1-5%) as reduction promoter and K₂O (1-3%) as activity promoter, calcined at 400°C. Catalyst lifetime: 1-5 years depending on operating conditions and feedstock purity.

**FT reactor types**: Multi-tubular fixed-bed reactor (Shell Middle Distillate Synthesis process): thousands of narrow tubes (25-50 mm diameter) packed with cobalt catalyst, surrounded by boiling water for temperature control. Slurry bubble column reactor (SASOL): catalyst particles suspended in liquid wax, syngas bubbled upward through the slurry. The slurry reactor offers better temperature control and higher per-pass conversion but requires catalyst-wax separation (filtration or hydrocyclone) that adds mechanical complexity.

**Methanol-to-Gasoline (MTG)**: Alternative to FT for producing gasoline-range hydrocarbons. Methanol (from syngas over Cu/ZnO/Al2O3 at 250-300C, 50-100 bar) is dehydrated over ZSM-5 zeolite catalyst at 350-400C to produce a mixture of aromatics and branched alkanes in the gasoline boiling range (C5-C10). MTG gasoline has research octane number 92-95, suitable for spark-ignition engines. Mobil developed this process commercially in New Zealand in 1985 (1500 tonnes/day from natural gas). Zeolite catalyst deactivation by coking requires regeneration every 2-4 weeks by controlled air burn at 500C.

**Thermal Cracking of Biomass (Pyrolysis)**: Fast pyrolysis of biomass at 450-550C with <2 second residence time produces bio-oil (60-75% yield), biochar (15-25%), and syngas (10-20%). Bio-oil is a viscous, acidic (pH 2-3), oxygen-rich liquid with half the energy density of petroleum oil (16-19 MJ/kg vs 42 MJ/kg), requiring upgrading (hydrotreating with H2 at 300-400C over CoMo catalyst) for use as transport fuel. Biochar is valuable as soil amendment (carbon sequestration, water retention) or as solid fuel (calorific value 25-30 MJ/kg).

**Syngas production routes for FT and chemicals**: Coal gasification (Lurgi fixed-bed or Texaco entrained-flow gasifier): C + H₂O → CO + H₂ at 1200-1500°C, 20-40 bar. Raw syngas cleaned of sulfur (H₂S removed by Rectisol process using chilled methanol at -40°C, reducing sulfur to <0.1 ppm) because sulfur poisons FT catalysts and downstream refining catalysts within hours. H₂:CO ratio adjusted to 2.0-2.1 for cobalt FT catalyst or 1.5-1.8 for iron catalyst. Biomass gasification follows the same chemistry but at lower temperature (800-1000°C), producing syngas with higher CO₂ and tar content that requires additional scrubbing before FT synthesis.

**Biomass gasification tar management**: Raw producer gas from biomass contains 1-20 g/m³ of tar (condensable organic vapors: phenol, naphthalene, benzene derivatives). Tars condense in downstream piping and catalyst beds, causing blockages and deactivation. Hot gas cleaning: catalytic tar cracking over dolomite (CaMg(CO₃)₂) or nickel-based catalyst at 800-900°C decomposes tars to CO + H₂. Cold gas cleaning: scrub with water or oil to physically remove tars, then treat the contaminated scrubbing liquid. For bootstrap FT operations, hot gas cleaning is preferred because it preserves the chemical energy content of the tars as additional syngas.

**Turpentine and Rosin from Pine**: Steam distillation of pine resin (exuded from wounded Pinus species) yields turpentine (15-25% by weight, a mixture of pinene isomers, bp 156-170C, used as solvent and chemical feedstock) and rosin (75-85%, also called colophony, mp 70-80C, used for soldering flux, varnishes, and paper sizing). Turpentine can substitute for petroleum-derived solvents in paint and coatings formulations. Global production ~300,000 tonnes/year turpentine, predominantly from China, Brazil, and Indonesia.

**Destructive Distillation of Wood**: Heating hardwood (oak, beech) in a retort at 400-500C without air produces charcoal (25-35% yield), wood tar (15-20%, contains creosote, acetic acid, methanol), pyroligneous acid (wood vinegar: 5-10% acetic acid, 2-3% methanol, 0.5-1% acetone), and wood gas (CO, H2, CH4, CO2 — calorific value 5-10 MJ/m3). Acetic acid from wood vinegar was the primary source before synthetic routes via methanol carbonylation. Methanol ("wood alcohol") was produced this way until the 1920s when catalytic synthesis from syngas became dominant. The charcoal is suitable for metallurgy; the creosote from tar is used as wood preservative (railroad ties, utility poles, 20-30 year service life).

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
