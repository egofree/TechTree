# Food Preservation

> **Node ID**: food-processing.preservation
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: [`ceramics`](../ceramics/index.md), [`chemistry.petroleum-alternatives.fermentation`](../chemistry/fermentation.md), [`health.sanitation`](../health/sanitation.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 0-30+
> **Outputs**: preserved_food, canned_food, pasteurized_food, refrigerated_food, dried_food, salted_food, smoked_food, fermented_food


Food preservation is the technology that eliminates seasonal starvation. Without it, food rots within days to weeks and populations face annual hunger gaps between harvests. With it, food becomes a stable, bankable commodity — enabling urban concentration, specialist labor, and long-distance trade. Every preservation method either removes water (drying, salting), creates hostile chemistry (fermentation, pickling), kills microorganisms with heat (canning, pasteurization), or slows microbial growth (refrigeration, freezing).

Preservation depends on [ceramics](../ceramics/index.md) for storage vessels, [health.sanitation](../health/index.md) for germ theory and hygiene, [chemistry.petroleum-alternatives.fermentation](../chemistry/fermentation.md) for fermentation chemistry, and [energy](../energy/index.md) for steam and electricity.


## Drying Materials

| Material | Quantity per 100 kg fresh food | Source | Alternatives |
|----------|:------------------------------:|--------|-------------|
| Fresh produce or meat | 100 kg | [Agriculture](../foundations/food-agriculture.md) | Wild foraged foods |
| Drying racks (wood/bamboo) | 2-4 m² surface area per 10 kg | [Forestry](../plants/index.md) | Clean flat stones, concrete surface |
| Fuel (for kiln drying) | 5-15 kg wood per 10 kg food | [Energy](../energy/index.md) | Solar drying (climate dependent) |
| Storage containers (sealed) | As needed | [Ceramics](../ceramics/index.md) | Glass jars, metal tins |

## Salting and Curing Materials

| Material | Quantity per 100 kg meat/fish | Source | Alternatives |
|----------|:----------------------------:|--------|-------------|
| Salt (NaCl) | 20-30 kg (heavy cure) or 10-15 kg (light) | [Mining](../mining/index.md) | Sea salt (solar evaporated) |
| Potassium nitrate (KNO₃) | 100-200 g (0.1-0.2%) | [Mining](../mining/index.md) or [Chemistry](../chemistry/index.md) | Sodium nitrite (120-150 ppm, more effective) |
| Barrels or crocks | 5-10 per 100 kg | [Ceramics](../ceramics/index.md) or [Forestry](../plants/index.md) | Food-grade plastic buckets |

## Canning Materials

| Material | Quantity per 1000 jars/cans | Source | Alternatives |
|----------|:--------------------------:|--------|-------------|
| Glass jars (Mason) or tinplate cans | 1000 units | [Glass](../glass/index.md) or [Metals](../metals/index.md) | Ceramic jars (lower reliability) |
| Lids and sealing compound | 1000 units | [Polymers](../polymers/index.md) | Rubber gaskets |
| Steam (for retort) | 150-300 kg | [Energy](../energy/index.md) — boiler | Direct-fired retort (less uniform) |
| Cooling water | 500-1000 L | [Water](../water/index.md) | Recirculated with cooling tower |


## Preservation Method Progression

**Drying** (Years 0+, stone-age)

The oldest and simplest preservation method. Reduces water activity (aw) below 0.60, inhibiting virtually all microbial growth.

- **Sun drying**: Spread thin slices (<5 mm) on clean surfaces in direct sun. 2-5 days depending on temperature and humidity. Works best below 60% relative humidity.
- **Air drying**: Hang whole items (herbs, sausages, whole fish) in warm, dry, well-ventilated area. 1-4 weeks. Temperature 20-35°C, humidity <50%.
- **Key parameters**: Final moisture content must reach 10-20% for vegetables/fruits, 5-10% for meat (jerky). Water activity aw < 0.60.
- **Reconstitution**: Soak dried foods in water for 2-12 hours before cooking. 10-30% vitamin loss from drying process.
- **Shelf life**: 6-12 months at room temperature when stored in dry, dark conditions. Insect-resistant packaging essential.
- **Limitations**: Climate dependent (fails in humid regions). Nutrient loss (vitamin C degrades). Texture changes. Labor intensive for large volumes.

**Strengths**:
- Sun drying requires no energy input — free solar energy reduces moisture below 0.60 water activity, inhibiting virtually all microbial growth
- Weight reduction of 70-90% (water removal) dramatically reduces transport and storage costs
- Achievable with zero technology: clean flat surfaces and sunlight are sufficient

**Weaknesses**:
- Fails in humid climates (>60% RH) where evaporation cannot reduce moisture to the safe threshold of 10-20%
- Vitamin C loss of 10-30% during drying reduces nutritional value vs. fresh produce
- Sun-dried food is vulnerable to insect infestation and dust contamination during the 2-5 day drying period

**Salting & Curing** (Years 0+, stone-age)

Salt (NaCl) creates osmotic pressure that kills or inhibits bacteria and molds. Dry salting or brining.

- **Dry salting**: Layer food with 20-30% salt by weight (for meat/fish). Salt draws water out via osmosis. Stack in barrels or on racks. Duration: 2-8 weeks for whole fish, 1-4 weeks for meat cuts.
- **Brining**: Submerge food in saturated salt solution (26.4% NaCl at 20°C — saturation point). Faster penetration than dry salting. Duration: 1-7 days depending on thickness.
- **Salt quantities**: Heavy cure (30% salt by weight) for long storage. Light cure (10-15%) for flavor + moderate preservation.
- **Nitrates**: Potassium nitrate (saltpeter, KNO₃) added at 0.1-0.2% prevents botulism in cured meats and maintains red color. Sodium nitrite (NaNO₂) is more effective at 120-150 ppm. Both are essential safety additives for low-temperature curing.
- **Shelf life**: Salted meat/fish: 6-18 months. Heavily salted cod (bacalao) stores for years.
- **Limitation**: Salt was historically expensive and strategically critical — same salt used for food was needed for leather tanning, chemical production, and metal processing. Salt supply chains are a civilization-level dependency.

**Strengths**:
- Heavy salt curing (20-30% by weight) preserves meat and fish for 6-18 months without refrigeration or any energy input
- Salt is reusable: brine can be boiled down and the salt recovered for subsequent batches
- Nitrates (KNO₃ at 0.1-0.2%) prevent botulism in cured meats and maintain appealing red color

**Weaknesses**:
- Salt was historically a strategic resource — preserving 1 tonne of meat requires 200-300 kg salt, competing with leather tanning and chemical production
- Heavy salt consumption (>5 g/day) increases blood pressure and cardiovascular risk in the workforce
- Nitrate-cured meats form nitrosamines (carcinogenic) when cooked at high temperatures — fry bacon at moderate temperature only

**Smoking** (Years 0+, stone-age)

Smoke contains antimicrobial compounds (phenols, formaldehyde, acetic acid) and deposits a preservative layer. Combined with partial drying.

- **Cold smoking**: 20-30°C for 12-48 hours. Preserves without cooking. Requires prior salting. Risk: botulism if temperature exceeds 30°C in anaerobic conditions.
- **Hot smoking**: 60-80°C for 4-12 hours. Cooks and preserves simultaneously. Safer (cooking temperature kills most pathogens).
- **Smoke composition**: Hardwoods (hickory, oak, apple, cherry) preferred. Softwoods (pine) produce bitter, resinous smoke. Key antimicrobial compounds: guaiacol, syringol, catechol.
- **Water activity after smoking**: Reduced to 0.75-0.85. Shelf life: 1-4 weeks without refrigeration, 2-6 months with refrigeration.
- **Safety**: Must be combined with salting for reliable preservation. Smoking alone is insufficient.

**Strengths**:
- Smoke deposits antimicrobial phenols (guaiacol, syringol) and formaldehyde on food surface, extending shelf life 2-6× over salting alone
- Hot smoking (60-80°C) simultaneously cooks and preserves — reduces fuel needed for separate cooking
- Hardwood smoke adds flavor compounds that improve palatability of preserved meats, increasing willingness to eat preserved food

**Weaknesses**:
- Smoking alone is insufficient for preservation — must be combined with prior salting or brining
- Cold smoking (20-30°C) creates botulism risk if temperature exceeds 30°C in anaerobic conditions
- Wood smoke contains polycyclic aromatic hydrocarbons (PAHs), some carcinogenic — prolonged exposure during smoking operations is a health hazard

**Fermentation** (Years 0+, stone-age → industrial)

Controlled microbial growth that produces acids (lactic, acetic) lowering pH below 4.6, the critical threshold where Clostridium botulinum cannot grow or produce toxin.

- **Sauerkraut/kimchi**: Lactic acid bacteria (Lactobacillus) ferment cabbage. Salt at 2-3% suppresses undesirable organisms while allowing LAB. pH drops from 6.5 to 3.5 over 1-4 weeks at 18-22°C. Shelf life: 6+ months when kept anaerobic and cool.
- **Vinegar pickling**: Submerge vegetables in 5% acetic acid (vinegar). pH < 4.0. Heat-process sealed jars. Shelf life: 12+ months.
- **Yogurt**: Lactobacillus bulgaricus + Streptococcus thermophilus ferment milk at 42-45°C for 4-6 hours. pH drops to 4.0-4.6. Shelf life: 2-3 weeks refrigerated.
- **Safety critical**: Fermentation pH must reach <4.6 within 48 hours to prevent botulism. If pH stalls above 4.6 after 48 hours, discard the batch.

See also: [Brewing & Distilling](brewing.md) for alcoholic fermentation, and [Chemistry: Fermentation](../chemistry/fermentation.md) for industrial fermentation chemistry.

**Strengths**:
- Lactic acid fermentation lowers pH below 4.6 (botulism-safe threshold) using only salt and the naturally present LAB on vegetable surfaces — no starter culture needed
- Fermented foods contain B vitamins and bioavailable minerals produced by microbial metabolism — nutritional value increases vs. raw ingredients
- Minimal energy input: vegetable fermentation proceeds at ambient temperature (18-22°C) for 1-4 weeks with no heat required

**Weaknesses**:
- pH must reach <4.6 within 48 hours to prevent botulism — requires adequate salt concentration and viable LAB population
- Temperature sensitivity: below 15°C fermentation stalls; above 25°C texture degrades and off-flavors develop
- Fermented products are high in sodium (sauerkraut: 600-1,500 mg Na per 100 g; soy sauce: 5,000-7,000 mg Na per 100 mL)

**Canning** (Years 15-25, industrial)

Nicholas Appert's method (1809): heat food in sealed containers to destroy all microorganisms. The container prevents recontamination. Canning is the most reliable long-term preservation method but requires precise temperature/pressure control.

- **Acid foods** (pH < 4.6): Water bath canning at 100°C for 10-30 minutes. Tomatoes, fruits, pickles. Botulism spores cannot germinate at this pH.
- **Low-acid foods** (pH > 4.6): **Pressure canning required** at 116-121°C (10-15 psi pressure) for 20-90 minutes. Vegetables, meats, soups. These temperatures destroy Clostridium botulinum spores.
- **Botulism risk**: C. botulinum spores survive 100°C boiling. They germinate in anaerobic, low-acid canned foods and produce the most potent biological toxin known (LD₅₀ ~1 ng/kg). One gram of botulinum toxin could theoretically kill over 1 million people. Proper pressure canning at 121°C for the full specified time is non-negotiable.
- **Can construction**: Tin-plated steel cans with double-seam construction. Tin coating: 0.5-1.5 μm. Seam integrity tested by submerging in hot water and checking for bubbles (indicating seal failure).
- **Glass jars**: Reusable, visual inspection possible. But fragile and heavier. Mason jars with two-piece lids (flat seal + threaded band).
- **Processing times** (pressure canning at 121°C / 15 psi):
  - Green beans (quart jar): 25 minutes
  - Carrots (quart jar): 30 minutes
  - Meat (quart jar): 75 minutes for chunks, 90 minutes for ground
  - Fish (pint jar): 100 minutes
  - Soup (quart jar): 60-90 minutes depending on ingredients

**Strengths**:
- Pressure canning achieves 12D reduction of C. botulinum at 121°C — the only preservation method that guarantees sterilization of all microorganisms including heat-resistant spores
- Shelf-stable for 2-5 years at ambient temperature with zero energy input after processing — no refrigeration, no ongoing cost
- Works for complete meals (soups, stews, meat + vegetables together), not just single ingredients

**Weaknesses**:
- Requires precision pressure vessel rated for 15-30 psi and can seamer with ±0.05 mm tolerance — industrial-era technology
- Botulism risk from under-processing is lethal (LD₅₀ ~1 ng/kg): there is no safe shortcut, and errors are catastrophic
- Nutrient loss from thermal processing: vitamin C degrades 30-50%, texture softens, color changes in canned vegetables

**Pasteurization** (Years 15-25, industrial)

Heat treatment that destroys pathogenic microorganisms without sterilizing the food. Named after Louis Pasteur (1864). Critical for milk, juice, beer, and other liquid foods.

- **Low-Temperature Long-Time (LTLT)**: 63°C for 30 minutes. Traditional batch method. Gentle on flavor but requires careful time-temperature control.
- **High-Temperature Short-Time (HTST)**: 72°C for 15 seconds. Continuous flow method. Industry standard for milk. Requires plate heat exchanger.
- **Ultra-High Temperature (UHT)**: 135-150°C for 2-8 seconds. Produces shelf-stable milk (6+ months without refrigeration). Requires aseptic packaging. Common outside North America.
- **Verification**: Phosphatase test confirms adequate milk pasteurization. Alkaline phosphatase is destroyed at the same temperature as Mycobacterium tuberculosis (the target pathogen). Negative test = properly pasteurized.
- **Temperature monitoring**: Mercury or digital thermometers calibrated to ±0.5°C. Recording thermometers provide continuous documentation. Divert valve activates if temperature drops below setpoint.

**Strengths**:
- HTST pasteurization (72°C for 15 seconds) achieves 5-log pathogen reduction while preserving flavor, color, and nutritional quality
- Regenerative heat recovery in plate heat exchangers recovers 80-90% of thermal energy — fuel cost of only 0.1-0.3 MJ/L
- Phosphatase test provides simple verification: negative result confirms adequate heat treatment

**Weaknesses**:
- Pasteurized milk still requires refrigeration (0-4°C) with shelf life of only 5-7 days — does not eliminate cold chain dependency
- Plate heat exchanger requires stainless steel construction and food-grade gaskets — not available in early bootstrap
- Post-pasteurization contamination is the leading cause of spoilage: any breach in sanitary handling re-introduces pathogens

**Refrigeration** (Years 20-30, industrial)

Mechanical cooling slows microbial growth, chemical degradation, and enzymatic activity. Extends fresh food shelf life by 5-20×.

- **Temperature zones**: Refrigerator: 0-4°C (fresh food). Freezer: -18°C or below (long-term storage). Blast freezer: -30°C to -40°C (rapid freezing for quality preservation).
- **Microbial growth rates**: At 4°C, most bacteria double every 12-24 hours (vs. 20 minutes at 37°C). At -18°C, growth is essentially halted.
- **Ice production**: Pre-mechanical: ice harvested from frozen lakes, stored in insulated ice houses (sawdust insulation, underground). 50-70% of stored ice survives summer. Mechanical ice production: ammonia absorption or vapor-compression cycle.
- **Cold chain**: Continuous refrigeration from production to consumption. A single break in the cold chain can allow dangerous bacterial growth. Temperature monitoring with recording devices is essential.

**Strengths**:
- At 4°C, bacterial doubling time extends from 20 minutes (37°C) to 12-24 hours — extends fresh food shelf life by 5-20×
- Freezing at -18°C halts microbial growth entirely, preserving food for 6-12 months with minimal quality loss
- Ice harvesting from frozen lakes provides 50-200 tonnes of natural ice per winter, enabling cold storage without mechanical refrigeration

**Weaknesses**:
- Mechanical refrigeration requires 0.5-2.0 kW per m³ of cold storage and 200-500 kWh/day for a 100 m³ freezer — massive energy demand
- Cold chain is fragile: a single power failure or equipment breakdown can destroy an entire inventory of frozen food
- Blast freezing (-30°C to -40°C) is needed for quality preservation; slow freezing creates large ice crystals that rupture cell walls and produce mushy texture on thawing

## Food Spoilage Mechanisms

Understanding *why* food spoils is essential for choosing the right preservation method:

| Mechanism | Cause | Time to Spoilage | Prevention |
|-----------|-------|:----------------:|-----------|
| Microbial growth | Bacteria, yeasts, molds | 4-48 hours | Heat kill, pH control, water removal, cold |
| Enzymatic browning | Polyphenol oxidase | 1-4 hours (cut fruit) | Acid (lemon juice), blanching, cold |
| Lipid oxidation | Oxygen + unsaturated fats | Days to weeks | Antioxidants, vacuum packaging, cold |
| Moisture migration | Water activity differential | Days | Proper packaging, moisture barriers |
| Insect/rodent damage | Physical access | Days to weeks | Sealed containers, elevated storage |

## Industrial Canning Line

An industrial canning operation for the industrial era:

1. **Raw material preparation**: Washing, sorting, peeling (mechanical or lye), cutting. Lye peeling: 10-20% NaOH at 90-100°C for 30-90 seconds, then water rinse removes loosened skins.
2. **Blanching**: Hot water or steam at 85-100°C for 1-5 minutes. Inactivates enzymes, removes air from tissue, softens for packing. Weight loss: 5-15%.
3. **Filling**: Mechanical or hand filling into cans. Fill weight controlled to ±2%. Headspace: 6-10 mm for thermal expansion.
4. **Exhausting**: Heat to 75-85°C or vacuum seaming to remove air (oxygen causes quality loss and can deformation during processing).
5. **Seaming**: Double-seam operation. First operation roll: curls cover hook around body hook. Second operation roll: compresses and tightens the seam. Seam thickness: 1.2-1.5 mm. Overlap: ≥1.0 mm. Gap: ≤0.15 mm.
6. **Thermal processing**: Retort (pressure vessel) at 121°C for prescribed time. Critical controls: initial temperature, come-up time, holding time, cooling time. Process deviation = product must be re-processed or destroyed.
7. **Cooling**: Rapid cooling to 38°C to prevent thermophilic spoilage. Pressure maintained during cooling to prevent can buckling (paneling). Chlorinated cooling water (2-5 ppm free chlorine) prevents post-process contamination through seam micro-leaks.
8. **Storage and inspection**: Hold canned goods for 10-14 days at 35-40°C (incubation test) to detect under-processing. Swollen cans = microbial growth = discard. Also called "swell test."


## Preservation Method Comparison

| Method | Water Activity (aw) | Temperature | Processing Time | Shelf Life | Energy Required |
|--------|:-------------------:|:-----------:|:---------------:|:----------:|:---------------:|
| Sun drying | <0.60 | Ambient (25-40°C) | 2-5 days | 6-12 months | None (solar) |
| Kiln drying | <0.60 | 50-70°C | 6-24 hours | 6-12 months | 2-5 MJ/kg |
| Salting (heavy) | 0.65-0.75 | Ambient | 2-8 weeks | 6-18 months | Minimal |
| Smoking (cold) | 0.75-0.85 | 20-30°C | 12-48 hours | 1-4 weeks | 1-3 MJ/kg (wood) |
| Smoking (hot) | 0.70-0.80 | 60-80°C | 4-12 hours | 2-6 months (refrigerated) | 2-5 MJ/kg |
| Fermentation | 0.95-0.99 (moist) | 18-42°C | 2 days-18 months | 1-12 months | Minimal |
| Water bath canning | 0.99+ (sealed) | 100°C | 10-45 minutes | 12-24 months | 0.5-1.5 MJ/jar |
| Pressure canning | 0.99+ (sealed) | 116-121°C | 20-100 minutes | 12-60 months | 1-3 MJ/jar |
| Pasteurization (HTST) | 0.99+ | 72°C | 15 seconds | 5-7 days (refrigerated) | 0.1-0.3 MJ/L |
| UHT sterilization | 0.99+ | 135-150°C | 2-8 seconds | 6+ months (ambient) | 0.3-0.5 MJ/L |
| Freezing | 0.99+ | -18°C | Ongoing | 6-12 months | 0.5-1.0 MJ/kg (initial) + 0.05 MJ/kg/day |

## Thermal Death Parameters for C. botulinum

| Temperature | D-value (min) | F-value for 12D (min) | Z-value |
|:-----------:|:--------------:|:----------------------:|:-------:|
| 100°C | ~800 | ~9,600 | — |
| 110°C | ~20 | ~240 | — |
| 115°C | ~1.5 | ~18 | — |
| 121°C | 0.21 | 2.52 | 10°C |
| 130°C | 0.02 | 0.24 | — |

D-value = time to reduce population by 90% (1 log). 12D reduction (F₀ = D × 12) is the industry standard for commercial sterility. At 121°C, F₀ = 2.52 minutes minimum. Most canning processes target F₀ = 3.0-6.0 minutes for safety margin.

## Steam Pressure-Temperature Relationship

| Gauge Pressure (psi) | Temperature (°C) | Temperature (°F) |
|:--------------------:|:-----------------:|:-----------------:|
| 0 (atmospheric) | 100 | 212 |
| 5 | 108 | 227 |
| 10 | 115 | 240 |
| 15 | 121 | 250 |
| 20 | 126 | 259 |
| 25 | 130 | 267 |
| 30 | 134 | 273 |

Values assume sea level and pure steam (no air). Air in the retort lowers actual temperature — 5% air at 15 psi reduces temperature from 121°C to ~118°C.

## Water Activity Thresholds for Microbial Growth

| Organism Type | Minimum aw for Growth | Examples | Key Products Affected |
|:-------------:|:---------------------:|:--------:|:--------------------:|
| Most bacteria | 0.90 | E. coli, Salmonella, C. botulinum | Fresh meat, milk, vegetables |
| Most yeasts | 0.88 | Saccharomyces, Candida | Fruit, syrups |
| Most molds | 0.70 | Aspergillus, Penicillium | Bread, cheese, dried fruit |
| Halophilic bacteria | 0.75 | Halobacterium | Salted fish |
| Xerophilic molds | 0.61 | Aspergillus restrictus | Dried grains, spices |
| No microbial growth | <0.60 | — | Fully dried foods (stable) |

## Food Spoilage Rates by Temperature

| Food | Room Temp (25°C) | Refrigerated (4°C) | Frozen (-18°C) |
|------|:----------------:|:------------------:|:--------------:|
| Raw meat | 4-8 hours | 3-5 days | 6-12 months |
| Raw fish | 4-6 hours | 1-2 days | 3-6 months |
| Fresh milk | 4-6 hours | 5-7 days | 3 months |
| Cooked rice | 6-8 hours | 4-6 days | 6 months |
| Cut fruit | 2-4 hours | 3-5 days | 6-12 months |
| Fresh vegetables | 1-2 days | 5-7 days | 8-12 months |
| Bread | 3-5 days (mold) | 7-10 days | 3-6 months |

## Scaling Notes

- **Household preservation** (family of 4-8): Sun drying on racks, small-batch salting in crocks, water bath canning on kitchen stove. Throughput: 5-20 kg per batch. Labor: 4-8 hours per batch. Equipment: minimal (pots, jars, racks).
- **Community preservation** (50-200 people): Dedicated drying shed, barrel salting operation, community cannery with small retort (100-200 L). Throughput: 100-500 kg per batch. 2-3 workers per session. Requires dedicated building with ventilation and water supply.
- **Industrial preservation** (10,000+ people): Continuous drying tunnels, automated salting lines, industrial retorts (continuous rotary or hydrostatic), cold storage warehouses. Throughput: 1-50 tonnes/day. 20-100 workers. Requires steam supply, electrical power, and transportation infrastructure.
- **Cold chain scaling**: Ice harvesting from frozen lakes provides 50-200 tonnes of ice per winter per lake — sufficient for small community cold storage. Mechanical refrigeration requires 0.5-2.0 kW per m³ of cold storage. A 100 m³ cold room at -18°C requires 50-100 kW cooling capacity and 200-500 kWh/day electrical energy.
- **Salt consumption**: Preserving 1 tonne of meat by heavy salting requires 200-300 kg salt. A community of 500 people preserving meat for winter needs 5-10 tonnes of salt per year — a significant logistics burden. Salt production must be planned alongside food preservation infrastructure.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Mold on dried food | Insufficient drying, storage humidity too high, poor packaging | Dry to <10% moisture. Store in sealed containers with desiccant. Keep below 60% RH |
| Rancid salted meat | Fat oxidation, temperature too high during storage, insufficient salt | Store below 15°C. Increase salt concentration. Trim visible fat before salting (fat oxidizes faster) |
| Swollen cans (botulism risk) | C. botulinum growth from under-processing or seal failure | **Discard immediately** — do not taste. Review retort temperature logs. Verify seam integrity. Increase processing time |
| Fermentation stalls (pH >4.6) | Low temperature, insufficient salt for selective pressure, contaminant organisms | Raise temperature to 18-22°C. Verify salt concentration (2-3% for vegetables). Discard if pH >4.6 after 48 hours |
| Freezer burn | Poor packaging, temperature fluctuation, extended storage | Wrap tightly in moisture-proof material. Maintain -18°C continuously. Use within recommended time |
| Pickles soft/mushy | Enzymes not destroyed, insufficient acidity, wrong cucumber variety | Blanch before pickling. Ensure vinegar is 5% acetic acid. Use pickling varieties (not slicing cucumbers) |
| Smoked food spoils quickly | Insufficient salting before smoking, temperature too low during hot smoking | Salt or brine before smoking. Hot smoke at 60-80°C. Ensure internal temperature reaches 63°C |
| Pasteurized milk spoils early | Post-pasteurization contamination, temperature abuse during storage | Clean and sanitize all equipment after pasteurization. Cool rapidly to 4°C. Maintain cold chain |
| Dried food won't rehydrate | Over-dried (<3% moisture), case hardening from too-hot drying | Dry to 10-20% moisture, not lower. Use lower temperature (50-60°C) for initial drying, increase gradually |


## Food Safety Reference

| Hazard | Source | Prevention | Lethal Dose |
|--------|--------|-----------|-------------|
| Botulism | C. botulinum toxin | Acidify pH<4.6 OR pressure can 121°C | ~1 ng/kg (ingested) |
| Salmonella | Raw eggs, poultry | Cook to 74°C | Varies (infectious dose ~10-100 organisms) |
| E. coli O157:H7 | Contaminated produce | Cook to 71°C, wash produce | ~10 organisms |
| Listeria | Soft cheese, deli meats | Pasteurize, cook to 74°C | Varies (high risk for immunocompromised) |
| Aflatoxin | Moldy grain/nuts | Dry storage <13% moisture | Chronic exposure: liver cancer |

- **Botulism is the primary hazard** in all food preservation. C. botulinum spores survive 100°C boiling indefinitely. They germinate in anaerobic, low-acid (pH >4.6), moist conditions and produce the most potent biological toxin known. **Prevention is non-negotiable**: pressure can all low-acid foods at 121°C for the full specified time, or ensure pH <4.6 through acidification or fermentation.
- **Salt and nitrate safety**: Heavy salt consumption (above 5 g/day) increases blood pressure and cardiovascular risk. Nitrate-cured meats should be consumed in moderation — nitrates convert to nitrosamines (carcinogenic) at high cooking temperatures. Fry bacon at moderate temperature.
- **Pressure vessel safety**: Retorts at 15 psi contain steam at 2.7× atmospheric pressure. Structural failure causes explosive release of scalding steam. Mandatory: pressure relief valve set 10% above operating pressure, calibrated pressure gauge, operator training.
- **Smoke inhalation**: Wood smoke contains polycyclic aromatic hydrocarbons (PAHs), some carcinogenic. Smokehouses require ventilation. Do not stand in smoke for extended periods.
- **Phosphine fumigation**: Aluminum phosphide tablets release phosphine gas (PH₃) — lethal at 0.01% in air. Apply only to sealed storage. Aerate for 48+ hours before re-entry. Phosphine is heavier than air — evacuate from bottom up.

## See Also

- [Canning & Thermal Sterilization](canning.md) — detailed thermal processing methodology
- [Food Fermentation](fermentation.md) — biological preservation, acidification
- [Dairy Processing](dairy.md) — pasteurization of milk and dairy products
- [Brewing & Distilling](brewing.md) — pasteurization of beer and wine
- [Ceramics](../ceramics/index.md) — storage vessels, jars, pots for fermentation and canning
- [Health & Sanitation](../health/sanitation.md) — germ theory, hygiene protocols
- [Chemistry: Fermentation](../chemistry/fermentation.md) — fermentation chemistry and microbiology
- [Energy](../energy/index.md) — steam for canning retorts, electricity for refrigeration
- [Mining](../mining/index.md) — salt production for curing and preservation
- [Oil & Fat Processing](oil-processing.md) — oil as a preservation medium (confit, oil-packed foods)



[← Back to Food Processing](index.md)
