# Fermentation Chemistry

> **Node ID**: chemistry.fermentation
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`foundations.food-agriculture`](../foundations/food-agriculture.md)
> **Enables**: [`chemistry.solvents`](solvents.md), [`food-processing.brewing`](../food-processing/brewing.md), [`food-processing.preservation`](../food-processing/preservation.md)
> **Timeline**: Years 5-20
> **Outputs**: ethanol, acetone, butanol, acetic_acid, methanol
> **Critical**: No — fermentation provides solvents and fuels at early development stages but is superseded by petrochemical routes

## Problem

Fermentation converts sugars and starches into alcohols, solvents, and organic acids using microorganisms. Before petrochemical infrastructure exists, fermentation is the primary route to ethanol (fuel and solvent), acetone, butanol, acetic acid, and methanol. The process requires controlling temperature, pH, nutrient supply, and contamination to maintain microbial cultures that perform specific chemical transformations. Industrial-scale fermentation demands vessels of 10,000-100,000 liters with temperature control, agitation, and sterile operation.

## Prerequisites

- [Food & Agriculture](../foundations/food-agriculture.md) — grain and sugar feedstocks
- [Distillation](distillation.md) — product recovery from fermentation broth
- [Solvents](solvents.md) — downstream solvent purification

## Ethanol Production

**Feedstocks**: Grain (barley, wheat, corn — starch → sugar via malt enzymes), sugar cane/beets (direct sugar), fruit (sugars), potatoes (starch). Starch must be converted to sugar first (malting/sprouting grain produces amylase enzymes that break starch into maltose).

**Malting**:
1. Soak grain in water 2-3 days. Drain and spread on malting floor.
2. Sprout 5-7 days, keep moist and at 15-20°C. Turn regularly to prevent matting and ensure even sprouting.
3. Grain produces amylase enzymes during germination — this is the key step. Amylase converts starch (long glucose polymer) into maltose and glucose (fermentable sugars).
4. Dry at 50-60°C to stop germination (kilning). Higher kilning temperatures produce darker, more roasted malt (affects flavor — irrelevant for industrial ethanol, relevant for distilled spirits).
5. Crush dried malt to coarse grist with roller mill.

**Mashing**:
- Mix grist with hot water (65-68°C) in insulated vessel (mash tun). Water-to-grist ratio ~3:1 by weight.
- Hold at 65-68°C for 1-2 hours. Amylase enzymes (alpha-amylase and beta-amylase) convert starch to maltose (C₁₂H₂₂O₁₁) and glucose (C₆H₁₂O₆).
- Test with iodine — blue = starch still present, no blue = conversion complete. Adjust temperature: 62-65°C favors beta-amylase (more maltose, more fermentable sugar). 68-72°C favors alpha-amylase (more dextrins, less fermentable sugar, fuller body).
- Strain liquid (wort) from spent grain. Spent grain is valuable livestock feed.

**Fermentation**:
- Cool wort to 20-30°C (yeast dies above ~40°C). Transfer to fermentation vessel.
- Add yeast (*Saccharomyces cerevisiae* — from previous batch or wild-captured). Pitching rate: ~1 g dry yeast per liter of wort.
- Ferment 3-7 days in closed vessel with airlock (CO₂ escapes, air cannot enter — wild microorganisms contaminate open vessels).
- C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂ (glucose → ethanol + carbon dioxide)
- Maximum ~12-15% ABV (alcohol kills yeast above ~15%). Fermentation is exothermic — temperature control critical. Active fermentation generates heat: monitor temperature, cool with water jacket or cold water bath if exceeding 30°C.

**Distillation**:
- Ethanol boils at 78.3°C (water at 100°C). Distill fermented wash in pot still or fractionating column.
- First distillation: ~40-50% ABV. Second distillation: ~70-80% ABV. Third distillation or fractionating column: ~95% ABV (azeotrope — cannot exceed 95.6% by simple distillation).
- For anhydrous ethanol (>99%): add quicklime (CaO) to absorb water, re-distill. Or use molecular sieves (zeolites — selectively adsorb water).
- Discard foreshots (first 50-100 mL — contains methanol and other low-boiling congeners, toxic). Discard fusel oils (last fraction — higher alcohols with unpleasant odor).

**Strengths**: Well-understood process with 5000+ years of practice; multiple feedstock options (grain, sugar, fruit, potatoes); 90-95% theoretical yield achievable; byproducts have value (spent grain as livestock feed, CO₂ for carbonation or dry ice).

**Weaknesses**: Azeotrope limits distillation to 95.6% ABV (anhydrous requires extra steps); 12-15% ABV ceiling from batch fermentation (dilute feedstock means large volumes to distill); energy-intensive distillation (2.5-4.0 kg steam per liter of 95% ethanol); competes with food supply for grain feedstock.

## Weizmann Acetone-Butanol Process

**Organism**: *Clostridium acetobutylicum* (anaerobic bacterium, Gram-positive, spore-forming). Can be isolated from soil or maintained as preserved culture on agar slants.

**Process**:
- Prepare starch substrate (corn, potato, or grain mash — same mashing process as ethanol).
- Sterilize mash by boiling (critical — competing bacteria will outcompete *Clostridium* if present).
- Cool to 35-37°C. Inoculate with *C. acetobutylicum* culture. Maintain strict anaerobic conditions (no oxygen — sparge with nitrogen or CO₂).
- Fermentation has two phases:
  - **[Acidogenic phase](../glossary/acidogenic-phase.md)** (first 18-24 hours): Bacteria produce acetic acid and butyric acid, pH drops to ~4.5.
  - **[Solventogenic phase](../glossary/solventogenic-phase.md)** (next 24-48 hours): Bacteria convert acids to solvents, pH stabilizes ~4.3.
- Products: acetone (~30%), n-butanol (~60%), ethanol (~10%) by volume, plus CO₂ and H₂ gases.
- **Distillation**: Separate by fractional distillation. Acetone bp 56°C, ethanol bp 78°C, n-butanol bp 118°C.

**Applications**: Acetone — solvent for resins, fats, plastics; key ingredient in nitrocellulose dope. n-Butanol — solvent, feedstock for butyl rubber and esters. This process was THE primary source of acetone for British cordite production during World War I.

**Strengths**: Produces three valuable solvents from starch in a single fermentation; butanol is a superior fuel to ethanol (29.2 MJ/L vs 21.2 MJ/L, miscible with gasoline); historically proven at industrial scale (WWI cordite production); anaerobic process — no aeration equipment needed.

**Weaknesses**: Butanol toxicity limits product concentration to 12-15 g/L (dilute broth = high distillation cost); strict anaerobic requirements increase contamination risk; product ratio (3:6:1 acetone:butanol:ethanol) is fixed by organism — not tunable; bacterium forms spores that complicate continuous fermentation.

## Acetic Acid Production

**[Vinegar method](../glossary/vinegar-method.md)** (biological):
- Expose ethanol solution to air with *Acetobacter* bacteria (present on fruit surfaces, in unpasteurized vinegar).
- Aerobic fermentation at 25-30°C for days to weeks. Provides continuous aeration (oxygen is required — unlike ethanol fermentation which is anaerobic).
- Produces 5-12% acetic acid. Slow but simple. No special equipment beyond vessels and air exposure.
- CH₃CH₂OH + O₂ → CH₃COOH + H₂O

**[Chemical oxidation](../glossary/chemical-oxidation.md)** (faster, higher yield):
- Pass ethanol vapor over heated copper catalyst (copper gauze at 300-400°C) with air.
- Ethanol oxidizes to acetaldehyde (CH₃CHO), then to acetic acid. Faster, higher concentration achievable.
- Applications: food preservation (vinegar), cellulose acetate (photographic film, synthetic fibers), acetic anhydride (aspirin synthesis, cellulose acetate production), metal etching, solvent.

**Strengths**: Biological route (vinegar method) requires no special equipment — just ethanol, air, and Acetobacter bacteria; chemical oxidation achieves higher concentrations (>12% vs biological limit); acetic acid is a versatile chemical intermediate (cellulose acetate, aspirin, vinyl acetate); multiple production routes offer flexibility.

**Weaknesses**: Biological route is slow (days to weeks) and limited to 12-14% acid concentration; chemical oxidation requires 300-400°C copper catalyst and careful temperature control; vinegar method needs continuous aeration (energy for air pumping); both routes consume ethanol feedstock that could be used for fuel.

## Methanol from Wood Pyrolysis

**Process**: Heat hardwood in closed iron retort to 400-500°C. Destructive distillation produces: charcoal (solid), wood tar (liquid), pyroligneous acid (aqueous condensate containing methanol, acetic acid, acetone).

- Distill pyroligneous acid — methanol boils at 64.7°C (lowest-boiling fraction, collected first).
- Yield: ~1-2% methanol by weight of wood. Low yield but works with basic metallurgy-stage technology.
- **Synthetic methanol**: React CO + 2H₂ over ZnO/Cr₂O₃ catalyst at 300-400°C, 20-30 MPa. Requires purified synthesis gas from coal gasification. Much higher yield and purity.

**Strengths**: Wood pyrolysis requires only basic iron retort technology — achievable at early metallurgical stages; methanol is a versatile solvent and fuel; pyrolysis co-produces charcoal (fuel) and wood tar (preservative); synthetic route from syngas gives much higher yields at industrial scale.

**Weaknesses**: Wood pyrolysis yield is extremely low (~1-2% by weight of wood); methanol is highly toxic (10 mL causes blindness, 30 mL death); requires careful fractionation to separate from acetic acid and acetone in pyroligneous acid; synthetic route needs coal gasification infrastructure (high pressure, catalyst).

## Temperature Control

Fermentation is exothermic — uncontrolled temperature kills yeast or produces off-flavors:

- **Active fermentation peak**: 30-35°C generates maximum heat. Cool if exceeding 30°C for ale yeast, 15-20°C for lager yeast.
- **Methods**: Submerge fermentation vessel in cold water bath. Wrap with wet cloth (evaporative cooling). For large-scale: water jacket or cooling coil with circulating cold water. Monitor with thermometer twice daily minimum.
- **Kill temperature**: >45°C kills *Saccharomyces* within minutes. >35°C promotes production of fusel alcohols and esters (irrelevant for industrial ethanol, but wastes sugar carbon).

## Butanol and Biobutanol (ABE Fermentation)

The **[Weizmann process](../glossary/weizmann-process.md)** (Clostridium acetobutylicum) produces acetone, butanol, and ethanol in a 3:6:1 ratio. Butanol (C₄H₉OH) is a superior fuel to ethanol: higher energy density (29.2 MJ/L vs 21.2 MJ/L), miscible with gasoline at any ratio, lower hygroscopicity (doesn't absorb water), usable in unmodified engines. Feedstocks: corn starch, molasses, cellulose hydrolysate. Conditions: 30-37°C, anaerobic, pH controlled (switches from acidogenesis to solventogenesis at pH ~5). Yield: 10-20 g/L total solvents (low — product toxicity limits concentration). Modern strain improvement targets: higher tolerance (butanol inhibits growth above 12-15 g/L), continuous product removal by gas stripping or pervaporation membranes.

## Lactic Acid Fermentation

Lactic acid bacteria (Lactobacillus, Streptococcus, Pediococcus) convert sugars to lactic acid (C₃H₆O₃) via homofermentative pathway (2 mol lactic acid per mol glucose, yield >90%) or heterofermentative pathway (lactic acid + ethanol + CO₂). Industrial production: 30-45°C, pH 5-7 (neutralized with CaCO₃ or NaOH to prevent acid inhibition). Feedstock: glucose from corn starch or cane sugar. Downstream: calcium lactate filtered, acidified with H₂SO₄ to free lactic acid, purified. **Polylactic acid (PLA)**: Lactic acid oligomerized to lactide (cyclic dimer), then ring-opening polymerized to PLA — biodegradable thermoplastic for packaging, textiles, 3D printing filament. NatureWorks (USA) produces 150,000 tonnes/year PLA.

**Strengths**: Homofermentative strains achieve >90% theoretical yield from glucose; PLA bioplastic is compostable and petroleum-independent; lactic acid is a versatile platform chemical (food preservative, pharmaceutical, leather tanning); fermentation operates at moderate conditions (37-45°C, ambient pressure).

**Weaknesses**: Product inhibition requires pH control via base addition (CaCO₃ or NaOH); downstream purification adds cost (calcium lactate → H₂SO₄ acidification → crystallization); PLA has low Tg (55-65°C) limiting heat resistance; composting requires industrial composting conditions (>58°C, not home compost).

**Strengths**: Highest-volume industrial fermentation product (~2 million tonnes/year); low pH (2-3) prevents bacterial contamination naturally; 80-95% theoretical yield from glucose; A. niger is robust and non-pathogenic; multiple applications (food acidulant, detergent builder, pharmaceuticals).

**Weaknesses**: Requires strict trace metal limitation (especially iron and manganese) to trigger citric acid overflow; 5-7 day fermentation cycle; downstream purification is multi-step (filtration, calcium citrate precipitation, acid liberation, crystallization); nitrogen limitation strategy reduces cell growth rate (longer batch time).

**Strengths** (biogas): Converts organic waste (manure, food waste, sewage) into useful fuel; mesophilic operation at 35-40°C is stable and low-energy; biogas can replace natural gas after upgrading to biomethane; digestate is nutrient-rich fertilizer; continuous operation (CSTR) with 15-30 day HRT.

**Weaknesses** (biogas): Biogas only 55-70% CH₄ (requires upgrading for pipeline quality); HRT of 15-30 days requires large reactor volume; ammonia inhibition above 1500 mg/L NH₃-N with protein-rich feedstocks; thermophilic operation (higher yield) is less stable and more energy-intensive to maintain.

## Fermentation Equipment Design

**Bioreactor types**: (1) **[Stirred tank](../glossary/stirred-tank.md)** — impeller (Rushton turbine or marine blade) provides mixing and O₂ transfer, baffles prevent vortexing. Standard for aerobic fermentations (citric acid, antibiotics). (2) **[Air-lift](../glossary/air-lift.md)** — rising bubbles in the riser section create circulation through the downcomer — no mechanical seals, lower shear. Used for shear-sensitive cells and large-scale single-cell protein. (3) **[Bubble column](../glossary/bubble-column.md)** — simplest: sparge air at the bottom, bubbles rise through liquid. Low cost, good for viscous broths. (4) **[Packed bed / fluidized bed](../glossary/packed-bed-fluidized-bed.md)** — immobilized cells on solid support (ceramic, alginate beads). Continuous operation. (5) **[Anaerobic digester](../glossary/anaerobic-digester.md)** — CSTR with gas-tight cover, heating jacket or heat exchanger (maintain 35°C), gas collection system.

**Sterilization**: Critical for pure-culture fermentations (contaminants compete for substrate and may produce toxins). Methods: (1) **[Heat](../glossary/heat.md)** — steam at 121°C for 15-30 minutes (batch sterilization of medium in the vessel). (2) **[Continuous HTST](../glossary/continuous-htst.md)** — 140°C for 5-10 seconds in a heat exchanger, then flash-cooled. More energy-efficient for large volumes. (3) **[Filter sterilization](../glossary/filter-sterilization.md)** — 0.2 µm membrane filters for heat-sensitive components (vitamins, some growth factors). Equipment sterilization: steam all pipes, valves, and seals before filling — any dead leg or unsterilized pocket becomes a contamination source.

## Safety & Hazards

- **Ethanol fire**: Ethanol burns with nearly invisible blue flame. Cannot be seen in daylight. Keep away from open flames and sparks. Store in sealed metal containers. Fire extinguisher (CO₂ or dry chemical) required near distillation equipment.
- **Methanol toxicity**: Methanol is metabolized to formaldehyde and formic acid — causes blindness and death. As little as 10 mL can cause permanent blindness. Absorbed through skin. Label all containers clearly. NEVER store near food or drink. Use different-shaped containers than food/water vessels.
- **Distillation explosion**: NEVER distill in sealed vessels — pressure buildup causes explosion. Use open system with condenser vented to atmosphere. Never heat above boiling point of highest-boiling component. Pressure relief on all heated vessels.
- **CO₂ asphyxiation**: Fermentation produces large volumes of CO₂ (heavier than air, displaces oxygen). Never enter fermentation room without ventilation. CO₂ buildup in enclosed spaces causes rapid unconsciousness and death. Ensure adequate ventilation in all fermentation areas.

 *Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*

## Ethanol Production: Detailed Process Parameters

**Sugar sources**: Sugarcane juice (12-18% fermentable sugar, predominantly sucrose) provides the simplest route, requiring only pressing and clarification before fermentation. Grain starch requires enzymatic hydrolysis: barley amylase (α-amylase and β-amylase produced during malting) converts starch to maltose and glucose at 60-65°C. One tonne of corn yields 370-400 L of anhydrous ethanol (vs 70-80 L per tonne from sugarcane juice). Cellulosic ethanol (crop residues, wood chips) requires pretreatment (steam explosion or dilute acid hydrolysis) followed by cellulase enzymes, but can reach theoretical yields of 400-450 L per dry tonne.

**Fermentation parameters**: Saccharomyces cerevisiae ferments glucose at 25-35°C (optimum 30-32°C), pH 4.0-5.0 (maintained with CaCO₃ or Ca(OH)₂ addition). Sugar concentration 15-25% w/v in the mash. Yeast pitching rate 10-30 million cells/mL. Fermentation duration 48-72 hours to reach terminal gravity (8-12% ABV in batch, up to 15-18% in very high gravity fermentations with adapted yeast strains). Ethanol yield: 90-95% of theoretical (0.511 g ethanol per g glucose, from Gay-Lussac equation). The remaining 5-10% of sugar carbon becomes yeast biomass, glycerol, and minor byproducts.

**Distillation to azeotrope**: Beer column strips ethanol from fermented mash at atmospheric pressure. Overhead vapor: 40-50% ethanol (enriched from 8-12% in beer). Rectifying column further concentrates to 95.6% ethanol (the azeotropic composition with water at 78.2°C). Energy consumption: 2.5-4.0 kg steam per liter of 95% ethanol. Dehydration to anhydrous ethanol (>99.5%) requires molecular sieve pressure swing adsorption (3Å zeolite selectively adsorbs water at 10-20 bar, regenerates at atmospheric with purge gas) or extractive distillation.

## Acetic Acid and Vinegar Production

**Acetobacter oxidation**: Acetic acid bacteria (Acetobacter aceti, Gluconobacter oxydans) oxidize ethanol to acetic acid aerobically: CH₃CH₂OH + O₂ → CH₃COOH + H₂O. Surface culture (Orleans method): wine or cider in barrels with perforated covers, bacteria form a pellicle at the air-liquid interface. Slow (weeks to months), produces 3-6% acetic acid. Submerged culture (Fringes generator): ethanol solution pumped through a column packed with beechwood shavings colonized by bacteria, air forced upward. Faster (24-48 hours), produces 10-12% acetic acid. Temperature 25-30°C. Acetic acid concentration above 12-14% becomes toxic to the bacteria, limiting vinegar strength.

## Lactic Acid Fermentation for PLA Bioplastic

Lactobacillus species (L. delbrueckii, L. bulgaricus, L. rhamnosus) produce L-lactic acid from glucose at 37-45°C, pH 5.5-6.0 (maintained by adding CaCO₃ or NaOH to neutralize the acid as it forms). Homofermentative strains achieve >90% theoretical yield (1 g lactic acid per g glucose). The resulting calcium lactate is acidified with H₂SO₄ to precipitate CaSO₄ and liberate free lactic acid, which is purified by evaporation and crystallization. Polylactic acid (PLA) synthesis: lactic acid oligomerized to low molecular weight prepolymer, then thermally depolymerized to lactide (cyclic dimer, mp 95-98°C). Lactide purified by distillation and undergoes ring-opening polymerization with tin(II) octoate catalyst at 180-200°C to form high molecular weight PLA (100,000-300,000 Da). PLA mechanical properties: tensile strength 50-70 MPa, elongation 2-10%, Tg 55-65°C.

## Anaerobic Digestion Parameters

Biogas composition depends on feedstock and operating conditions. Typical: 55-70% CH₄, 30-45% CO₂, trace H₂S (100-4000 ppm from protein-rich feedstocks), moisture saturated. Calorific value: 20-25 MJ/m³ (pure methane is 35.8 MJ/m³).

**Operating regimes**: Mesophilic (35-38°C) is most common, stable, and tolerant of feedstock variations. Thermophilic (50-55°C) is faster (HRT 10-15 days vs 15-30 days mesophilic), gives 20-30% higher gas yield, but is more sensitive to temperature fluctuations and ammonia inhibition. Feedstock C:N ratio 20-30:1 is optimal. Below 15:1, excess nitrogen produces ammonia that inhibits methanogens at >1500 mg/L NH₃-N. Above 35:1, nitrogen limitation slows bacterial growth.

**Biogas yield**: 0.3-0.5 m³ biogas per kg volatile solids (VS) added, depending on feedstock degradability. Cattle manure: 0.20-0.30 m³/kg VS. Food waste: 0.40-0.60 m³/kg VS. Energy crops (maize silage): 0.50-0.65 m³/kg VS. Hydraulic retention time (HRT): 15-30 days mesophilic, 10-15 days thermophilic. Organic loading rate (OLR): 1-4 kg VS/m³/day. Loading above 4 kg VS/m³/day risks acidification (volatile fatty acid accumulation exceeds methanogenic consumption rate).

## Citric Acid Fermentation

Aspergillus niger produces citric acid as a metabolic overflow product when grown on sugar under specific stress conditions: limited nitrogen (C:N >40:1), trace metal limitation (especially iron and manganese), pH 2.0-3.0 (suppresses oxalic acid formation), and 28-30°C. The low pH prevents bacterial contamination. Submerged fermentation in 100-500 m³ stirred tanks with aeration (0.5-1.5 vvm) for 5-7 days. Yield: 80-95% of theoretical (0.71 g citric acid per g glucose, from the truncated TCA cycle). Downstream: filter mycelium (recovered as protein-rich animal feed), precipitate calcium citrate with Ca(OH)₂ at pH 7-8, acidify with H₂SO₄ to liberate citric acid, crystallize as monohydrate or anhydrate. Global production ~2 million tonnes/year, 60% used as food acidulant.

## Fermentation Scale-Up Considerations

**Oxygen transfer**: Aerobic fermentations (citric acid, antibiotics, single-cell protein) require continuous oxygen supply. The critical dissolved oxygen concentration is typically 10-30% of air saturation; below this, oxygen becomes rate-limiting. Oxygen transfer rate (OTR) = k_La × (C* - C_L), where k_La is the volumetric mass transfer coefficient (h⁻¹), C* is the saturated dissolved oxygen concentration, and C_L is the actual concentration. k_La increases with agitation speed (Rushton turbine impeller at 100-500 RPM) and aeration rate (0.5-2.0 vvm). Typical k_La in production-scale fermenters: 50-300 h⁻¹. Scale-up criterion: maintain constant k_La or constant oxygen transfer rate per unit volume when moving from lab (5-50 L) to pilot (500-5000 L) to production (50-500 m³).

**Heat removal**: Fermentation generates heat from microbial metabolism (~3-5 kW/m³ for fast-growing cultures). Temperature must be controlled within ±1°C. Heat removal via: cooling jackets (surface area limited, adequate for <10 m³ vessels), internal coils (provide additional surface area, but interfere with mixing and cleaning), or external heat exchangers (pump broth through shell-and-tube exchanger and return to fermenter). At production scale (>100 m³), heat removal can become the limiting factor for cell density.

**Inoculum development**: Industrial fermentations require a pure, vigorous inoculum at 5-10% of production volume. Development sequence: agar slant (single colony) → shake flask (50-500 mL, 24-48 hours) → seed fermenter (5-50 L, 24-48 hours) → production seed tank (500-5000 L, 24-48 hours) → production fermenter. Each step transfers active, log-phase culture. Contamination at any stage ruins the batch — strict aseptic technique throughout.

**Downstream processing**: The fermentation broth is a complex mixture: cells (or mycelium), product, unreacted substrate, and byproducts. Primary recovery: centrifugation (disc-stack centrifuge, 5000-15,000 × g, continuous) or rotary vacuum filtration (with filter aid: diatomaceous earth precoat). Product purification: solvent extraction (penicillin: extract into amyl acetate at pH 2.0-2.5, back-extract into aqueous buffer at pH 7), ion exchange, crystallization, or chromatography. Overall recovery yield from fermentation broth to purified product: 60-90% depending on the product and process.

## Fermentation Economics

**Capital costs**: A stainless steel production fermenter (100 m³ working volume, with agitator, sterile air system, temperature control, and instrumentation) costs $1-5 million depending on specification (316L stainless, ASME pressure vessel rating, CIP/SIP capability). Supporting infrastructure (media preparation, sterilization, inoculum rooms, downstream processing, utilities) adds 3-5× the fermenter cost. Total plant capital for a 500 m³/year citric acid plant: $20-50 million.

**Operating costs**: Raw materials 30-50%, energy (steam, electricity, compressed air) 15-25%, labor 10-20%, maintenance and depreciation 15-25%. For ethanol from corn: feedstock (corn) accounts for 50-65% of production cost. For citric acid: sugar (glucose or molasses) is 25-35% of cost. Energy for sterilization (steam at 121°C) and aeration (compressed air at 0.5-1.5 vvm for aerobic processes) are major utility costs. Water consumption: 5-15 m³ per m³ of fermentation broth (for cooling, cleaning, and steam generation).

**Batch vs continuous**: Batch fermentation (fill, sterilize, inoculate, ferment, harvest, clean, repeat) is the most common mode. Cycle time: 24-120 hours per batch. Equipment utilization: 60-80% (remaining time for cleaning, sterilization, and turnaround). Continuous fermentation (chemostat: fresh medium continuously fed, product continuously withdrawn at the same rate) achieves higher volumetric productivity but risks contamination over extended operation (a contaminated continuous fermenter must be shut down, sterilized, and restarted). Fed-batch (substrate added gradually during fermentation to avoid substrate inhibition) is the most practical compromise, widely used for antibiotics, amino acids, and yeast production.

## Fermentation Nutrient Requirements

**Carbon source**: Provides energy and building blocks for cell growth and product formation. Glucose (from starch hydrolysis or cane sugar) is the most common. Sucrose (from cane or beet) is directly fermentable by most organisms. Lactose (from whey) is used by specific strains. Cellulose (from agricultural residues) requires enzymatic hydrolysis to glucose first. Carbon cost: 40-60% of raw material cost for most fermentations. Carbon conversion efficiency to product: 40-90% depending on the organism and product.

**Nitrogen source**: Required for protein and nucleic acid synthesis. Sources: ammonium sulfate ((NH₄)₂SO₄, cheapest), ammonium hydroxide (NH₄OH, also provides pH control), urea (cheaper per unit nitrogen but slower release), corn steep liquor (byproduct of corn wet milling, provides nitrogen plus vitamins and minerals), yeast extract (rich in B vitamins and amino acids, expensive but used for fastidious organisms), soybean meal (complex nitrogen source for antibiotic fermentations). C:N ratio in the medium: 10-25:1 for balanced growth, >40:1 for citric acid production (nitrogen limitation triggers product accumulation).

**Trace elements**: Iron (FeSO₄, 1-50 mg/L), magnesium (MgSO₄, 0.1-1.0 g/L), zinc (ZnSO₄, 0.1-5 mg/L), manganese (MnSO₄, 0.01-1 mg/L), copper (CuSO₄, 0.01-0.5 mg/L). These are enzyme cofactors essential for metabolic activity. For citric acid production, iron limitation is deliberately imposed (iron is a cofactor for aconitase, the enzyme that would otherwise consume citric acid in the TCA cycle). Phosphorus (KH₂PO₄, 0.5-5 g/L) is needed for ATP, nucleic acids, and phospholipids. Calcium (CaCl₂, 0.01-0.1 g/L) stabilizes cell walls and enzymes.

**Vitamins and growth factors**: Biotin (0.01-0.1 mg/L) is essential for S. cerevisiae growth (biotin-deficient molasses must be supplemented). Thiamine (vitamin B₁), riboflavin (B₂), and pantothenic acid (B₅) are required by many bacterial species. Corn steep liquor and yeast extract provide these as natural complexes, avoiding the need for pure vitamin supplements.

## Fermentation Process Control

**pH control**: Most fermentations are sensitive to pH. S. cerevisiae: pH 4.0-5.0 (acidic conditions suppress bacterial contamination). Lactobacillus: pH 5.5-6.0 (acid inhibition below pH 5). Aspergillus niger (citric acid): pH 2.0-3.0 (maintained naturally by acid production). pH is controlled by automatic addition of acid (H₂SO₄, HCl) or base (NaOH, NH₄OH, CaCO₃ slurry) via peristaltic pumps triggered by a pH controller with setpoint ±0.1 pH unit. In large fermenters, pH probes must be sterilizable (steam-sterilizable glass electrode with Ag/AgCl reference, rated to 130°C).

**Foam control**: Fermentation generates foam from proteins and surfactants in the broth. Uncontrolled foam can overflow the fermenter, contaminating the air filter and losing product. Antifoam agents (silicone-based: polydimethylsiloxane at 0.01-0.1% v/v, or vegetable oil-based) are added automatically when a foam probe (conductivity or capacitance sensor) detects foam approaching the vessel top. Mechanical foam breakers (high-speed disc or impeller mounted on the agitator shaft above the liquid level) provide continuous foam control without adding foreign material to the broth.

**Sterilization validation**: Each batch of medium must be sterile before inoculation. Validation: biological indicators (spores of Geobacillus stearothermophilus, D₁₂₁ value = 1.5-3.0 minutes) placed in the medium before sterilization, recovered and cultured after. If no growth, sterilization is confirmed. Thermal death time for typical contaminants: E. coli killed at 72°C for 15 seconds (pasteurization), bacterial spores require 121°C for 15 minutes. Fermentation vessels must maintain sterility for the entire batch (3-14 days), requiring aseptic seals on agitator shafts, sterile air filters (0.2 μm membrane), and positive pressure of sterile air to prevent ingress.

## Industrial Fermentation Products Summary

**[Commodity products](../glossary/commodity-products.md)** (production >1 million tonnes/year): ethanol (fuel and beverage, ~100 million tonnes/year), lactic acid (~2 million tonnes/year, PLA precursor), citric acid (~2 million tonnes/year, food and detergent use), monosodium glutamate (~3 million tonnes/year, flavor enhancer), lysine (~2 million tonnes/year, animal feed additive). These are high-volume, low-margin products where raw material cost and fermentation yield are the primary competitive factors.

**[Fine chemicals and pharmaceuticals](../glossary/fine-chemicals-and-pharmaceuticals.md)** (production 10-10,000 tonnes/year): antibiotics (penicillin, cephalosporins, tetracyclines), amino acids (phenylalanine, tryptophan), vitamins (B₁₂, B₂, C via Reichstein-Grüssner process with fermentation step), steroids (hydrocortisone, prednisone from diosgenin via microbial transformation). These are high-value products where strain productivity, product purity, and intellectual property are the competitive factors. Fermentation titers: penicillin 30-50 g/L (improved from 0.001 g/L in 1940s by strain improvement and fed-batch fermentation), citric acid 100-150 g/L.

**Emerging products**: Single-cell protein (SCP from methanol or methane fermentation, 60-80% protein content, for animal feed), polyhydroxyalkanoates (PHAs, biodegradable plastics from bacterial fermentation), 1,3-propanediol (PDO, from corn sugar via DuPont/Tate & Lyle bio-PDO process, used for Sorona fiber), succinic acid (bio-based platform chemical, precursor for PBS bioplastic and 1,4-butanediol), and isobutanol (biofuel and chemical feedstock via engineered yeast). The bioeconomy continues to expand as petroleum alternatives gain economic viability.

## Fermentation Process Monitoring

**Online measurements**: Modern fermenters are equipped with probes for continuous monitoring of: dissolved oxygen (DO, polarographic or optical sensor, 0-100% saturation), pH (steam-sterilizable glass electrode), temperature (Pt100 RTD in a thermowell), off-gas composition (CO₂ and O₂ by infrared and paramagnetic analyzers), foam level (capacitance probe), and redox potential (for anaerobic fermentations). These measurements enable real-time process control and early detection of contamination (contaminated fermentations often show unusual DO, pH, or off-gas patterns).

**Off-line measurements**: Samples withdrawn aseptically every 2-8 hours for: optical density (OD₆₀₀, measures cell concentration, linear range 0.1-0.8, requires dilution for dense cultures), glucose concentration (YSI enzymatic analyzer or HPLC), product titer (HPLC or enzymatic assay), and microscope examination (contamination check, cell morphology). Biomass concentration calculated from OD₆₀₀: dry cell weight (g/L) ≈ 0.4 × OD₆₀₀ for bacteria, 0.5 × OD₆₀₀ for yeast (calibrated for each organism).

## Solid-State Fermentation

**Definition and applications**: Fermentation performed on solid substrates without free water. Traditional examples: tempeh (Rhizopus oligosporus on soybeans), soy sauce (Aspergillus oryzae on soy/wheat mixture), cheese (Penicillium roqueforti), and composting (mixed microbial communities on organic waste). Industrial solid-state fermentation produces: enzymes (amylase, cellulase, protease from fungi grown on wheat bran), citric acid (A. niger on solid substrates), and biopesticides (Beauveria bassiana spores on rice grains).

**Process parameters**: Moisture content 40-70% (vs >95% for submerged fermentation). Temperature 25-35°C, controlled by forced aeration through the substrate bed. Oxygen supply: critical, as fungal mycelium grows on the particle surface and requires O₂. Aeration rate: 0.5-2.0 vvm (volumes of air per volume of substrate per minute). Heat removal is the primary engineering challenge: the solid matrix has poor thermal conductivity, and metabolic heat can raise local temperature 10-20°C above ambient in poorly ventilated beds. Tray fermenters (shallow trays, 5-10 cm bed depth) provide adequate aeration but have low volumetric productivity. Packed bed bioreactors (air forced upward through a 0.5-1.0 m deep bed) provide better temperature control at larger scale.

## Fermentation Water Quality

**Process water requirements**: Fermentation water must be free of heavy metals (Fe <0.1 mg/L, Cu <0.01 mg/L, Zn <0.1 mg/L) that inhibit microbial growth, and free of chlorine (residual Cl₂ <0.1 mg/L, which kills microorganisms on contact). For large-scale operations, municipal water is typically treated by: (1) activated carbon filtration (removes chlorine and organics), (2) softening (removes Ca²⁺ and Mg²⁺ that can precipitate with media components), (3) deionization or reverse osmosis if needed for pharmaceutical-grade fermentations. Water quality is tested weekly for microbial count (<100 CFU/mL) and quarterly for heavy metals.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Fermentation stalled (no CO₂ production) | Temperature too low or yeast nutrient exhausted | Raise temperature to 25-30°C; add yeast nutrient (diammonium phosphate); check sugar concentration |
| Contamination (off-flavors, slime) | Wild bacteria or mold outcompeting culture | Sterilize vessel and medium; pitch active yeast at higher rate; lower pH to 4.0-4.5 (bacteria-sensitive range) |
| Low ethanol yield | Incomplete sugar conversion or excessive temperature | Monitor specific gravity to confirm fermentation complete; keep below 35°C (yeast stress threshold); ensure adequate yeast pitching rate |
| Stuck fermentation (stops early) | High sugar osmotic pressure or ethanol toxicity | Dilute initial sugar concentration; use alcohol-tolerant yeast strain; step-feed sugar incrementally |
| Vinegar production instead of ethanol | Acetobacter contamination introducing oxygen | Eliminate air exposure during fermentation; use airlock; maintain anaerobic conditions |
| Slow solid-state fermentation | Poor aeration or temperature gradient in substrate bed | Increase aeration rate; reduce bed depth; install temperature probes at multiple depths |

## See Also

- [Solvents](solvents.md) — ethanol, methanol, and butanol production via fermentation
- [Petroleum Alternatives](petroleum-alternatives.md) — biochemical routes to organic chemicals
- [Soap](soap.md) — glycerol byproduct from saponification, also produced by fermentation
- [SEM Tech](sem-tech.md) — membrane-based separation for fermentation product recovery
- [Distillation](distillation.md) — ethanol recovery from fermentation broth
- [Brewing](../food-processing/brewing.md) — beverage-scale fermentation
- [Food Preservation](../food-processing/preservation.md) — fermentation as preservation method

[← Back to Chemistry](index.md)
