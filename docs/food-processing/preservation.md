# Food Preservation

> **Node ID**: food-processing.preservation
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: `ceramics`, [`chemistry.petroleum-alternatives.fermentation`](../chemistry/fermentation.md), [`health.sanitation`](../health/sanitation.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 0-30+
> **Outputs**: preserved_food, canned_food, pasteurized_food, refrigerated_food, dried_food, salted_food, smoked_food, fermented_food

### Overview

Food preservation is the technology that eliminates seasonal starvation. Without it, food rots within days to weeks and populations face annual hunger gaps between harvests. With it, food becomes a stable, bankable commodity — enabling urban concentration, specialist labor, and long-distance trade. Every preservation method either removes water (drying, salting), creates hostile chemistry (fermentation, pickling), kills microorganisms with heat (canning, pasteurization), or slows microbial growth (refrigeration, freezing).

### Preservation Method Progression

**Drying** (Years 0+, stone-age)

The oldest and simplest preservation method. Reduces water activity (aw) below 0.60, inhibiting virtually all microbial growth.

- **Sun drying**: Spread thin slices (<5 mm) on clean surfaces in direct sun. 2-5 days depending on temperature and humidity. Works best below 60% relative humidity.
- **Air drying**: Hang whole items (herbs, sausages, whole fish) in warm, dry, well-ventilated area. 1-4 weeks. Temperature 20-35°C, humidity <50%.
- **Key parameters**: Final moisture content must reach 10-20% for vegetables/fruits, 5-10% for meat (jerky). Water activity aw < 0.60.
- **Reconstitution**: Soak dried foods in water for 2-12 hours before cooking. 10-30% vitamin loss from drying process.
- **Shelf life**: 6-12 months at room temperature when stored in dry, dark conditions. Insect-resistant packaging essential.
- **Limitations**: Climate dependent (fails in humid regions). Nutrient loss (vitamin C degrades). Texture changes. Labor intensive for large volumes.

**Salting & Curing** (Years 0+, stone-age)

Salt (NaCl) creates osmotic pressure that kills or inhibits bacteria and molds. Dry salting or brining.

- **Dry salting**: Layer food with 20-30% salt by weight (for meat/fish). Salt draws water out via osmosis. Stack in barrels or on racks. Duration: 2-8 weeks for whole fish, 1-4 weeks for meat cuts.
- **Brining**: Submerge food in saturated salt solution (26.4% NaCl at 20°C — saturation point). Faster penetration than dry salting. Duration: 1-7 days depending on thickness.
- **Salt quantities**: Heavy cure (30% salt by weight) for long storage. Light cure (10-15%) for flavor + moderate preservation.
- **Nitrates**: Potassium nitrate (saltpeter, KNO₃) added at 0.1-0.2% prevents botulism in cured meats and maintains red color. Sodium nitrite (NaNO₂) is more effective at 120-150 ppm. Both are essential safety additives for low-temperature curing.
- **Shelf life**: Salted meat/fish: 6-18 months. Heavily salted cod (bacalao) stores for years.
- **Limitation**: Salt was historically expensive and strategically critical — same salt used for food was needed for leather tanning, chemical production, and metal processing. Salt supply chains are a civilization-level dependency.

**Smoking** (Years 0+, stone-age)

Smoke contains antimicrobial compounds (phenols, formaldehyde, acetic acid) and deposits a preservative layer. Combined with partial drying.

- **Cold smoking**: 20-30°C for 12-48 hours. Preserves without cooking. Requires prior salting. Risk: botulism if temperature exceeds 30°C in anaerobic conditions.
- **Hot smoking**: 60-80°C for 4-12 hours. Cooks and preserves simultaneously. Safer (cooking temperature kills most pathogens).
- **Smoke composition**: Hardwoods (hickory, oak, apple, cherry) preferred. Softwoods (pine) produce bitter, resinous smoke. Key antimicrobial compounds: guaiacol, syringol, catechol.
- **Water activity after smoking**: Reduced to 0.75-0.85. Shelf life: 1-4 weeks without refrigeration, 2-6 months with refrigeration.
- **Safety**: Must be combined with salting for reliable preservation. Smoking alone is insufficient.

**Fermentation** (Years 0+, stone-age → industrial)

Controlled microbial growth that produces acids (lactic, acetic) lowering pH below 4.6, the critical threshold where Clostridium botulinum cannot grow or produce toxin.

- **Sauerkraut/kimchi**: Lactic acid bacteria (Lactobacillus) ferment cabbage. Salt at 2-3% suppresses undesirable organisms while allowing LAB. pH drops from 6.5 to 3.5 over 1-4 weeks at 18-22°C. Shelf life: 6+ months when kept anaerobic and cool.
- **Vinegar pickling**: Submerge vegetables in 5% acetic acid (vinegar). pH < 4.0. Heat-process sealed jars. Shelf life: 12+ months.
- **Yogurt**: Lactobacillus bulgaricus + Streptococcus thermophilus ferment milk at 42-45°C for 4-6 hours. pH drops to 4.0-4.6. Shelf life: 2-3 weeks refrigerated.
- **Safety critical**: Fermentation pH must reach <4.6 within 48 hours to prevent botulism. If pH stalls above 4.6 after 48 hours, discard the batch.

See also: [Brewing & Distilling](brewing.md) for alcoholic fermentation, and [Chemistry: Fermentation](../chemistry/fermentation.md) for industrial fermentation chemistry.

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

**Pasteurization** (Years 15-25, industrial)

Heat treatment that destroys pathogenic microorganisms without sterilizing the food. Named after Louis Pasteur (1864). Critical for milk, juice, beer, and other liquid foods.

- **Low-Temperature Long-Time (LTLT)**: 63°C for 30 minutes. Traditional batch method. Gentle on flavor but requires careful time-temperature control.
- **High-Temperature Short-Time (HTST)**: 72°C for 15 seconds. Continuous flow method. Industry standard for milk. Requires plate heat exchanger.
- **Ultra-High Temperature (UHT)**: 135-150°C for 2-8 seconds. Produces shelf-stable milk (6+ months without refrigeration). Requires aseptic packaging. Common outside North America.
- **Verification**: Phosphatase test confirms adequate milk pasteurization. Alkaline phosphatase is destroyed at the same temperature as Mycobacterium tuberculosis (the target pathogen). Negative test = properly pasteurized.
- **Temperature monitoring**: Mercury or digital thermometers calibrated to ±0.5°C. Recording thermometers provide continuous documentation. Divert valve activates if temperature drops below setpoint.

**Refrigeration** (Years 20-30, industrial)

Mechanical cooling slows microbial growth, chemical degradation, and enzymatic activity. Extends fresh food shelf life by 5-20×.

- **Temperature zones**: Refrigerator: 0-4°C (fresh food). Freezer: -18°C or below (long-term storage). Blast freezer: -30°C to -40°C (rapid freezing for quality preservation).
- **Microbial growth rates**: At 4°C, most bacteria double every 12-24 hours (vs. 20 minutes at 37°C). At -18°C, growth is essentially halted.
- **Ice production**: Pre-mechanical: ice harvested from frozen lakes, stored in insulated ice houses (sawdust insulation, underground). 50-70% of stored ice survives summer. Mechanical ice production: ammonia absorption or vapor-compression cycle.
- **Cold chain**: Continuous refrigeration from production to consumption. A single break in the cold chain can allow dangerous bacterial growth. Temperature monitoring with recording devices is essential.

### Food Safety Reference

| Hazard | Source | Prevention | Lethal Dose |
|--------|--------|-----------|-------------|
| Botulism | C. botulinum toxin | Acidify pH<4.6 OR pressure can 121°C | ~1 ng/kg (ingested) |
| Salmonella | Raw eggs, poultry | Cook to 74°C | Varies (infectious dose ~10-100 organisms) |
| E. coli O157:H7 | Contaminated produce | Cook to 71°C, wash produce | ~10 organisms |
| Listeria | Soft cheese, deli meats | Pasteurize, cook to 74°C | Varies (high risk for immunocompromised) |
| Aflatoxin | Moldy grain/nuts | Dry storage <13% moisture | Chronic exposure: liver cancer |

### Dependency Chain

Preservation depends on:
- **[ceramics](../ceramics/index.md)**: Storage vessels, jars, pots for fermentation and canning
- **[health.sanitation](../health/index.md)**: Understanding of germ theory, hygiene protocols
- **[chemistry.petroleum-alternatives.fermentation](../chemistry/fermentation.md)**: Fermentation chemistry and microbiology
- **[energy](../energy/index.md)**: Steam for canning retorts, electricity for refrigeration

Preservation enables:
- **Urbanization**: Food can be stored and transported, enabling cities
- **Specialist workforce**: Year-round food supply frees workers from agriculture
- **Military logistics**: Armies travel on preserved rations
- **Maritime exploration**: Canned and salted provisions enable long voyages

### Food Spoilage Mechanisms

Understanding *why* food spoils is essential for choosing the right preservation method:

| Mechanism | Cause | Time to Spoilage | Prevention |
|-----------|-------|:----------------:|-----------|
| Microbial growth | Bacteria, yeasts, molds | 4-48 hours | Heat kill, pH control, water removal, cold |
| Enzymatic browning | Polyphenol oxidase | 1-4 hours (cut fruit) | Acid (lemon juice), blanching, cold |
| Lipid oxidation | Oxygen + unsaturated fats | Days to weeks | Antioxidants, vacuum packaging, cold |
| Moisture migration | Water activity differential | Days | Proper packaging, moisture barriers |
| Insect/rodent damage | Physical access | Days to weeks | Sealed containers, elevated storage |

- **Water activity (aw)**: The single most important parameter. Pure water = 1.00. Fresh meat = 0.98-0.99. Most bacteria cannot grow below 0.90. Most yeasts and molds cannot grow below 0.70. Dried foods at 0.50-0.60 are stable indefinitely.
- **D-value (decimal reduction time)**: Time at a given temperature to reduce a microbial population by 90% (1 log). At 121°C: C. botulinum spores D = 0.21 minutes. This means 12D reduction (industry standard) requires 2.5 minutes at 121°C — the basis for canning time calculations.
- **F-value**: Total lethality of a thermal process, expressed in equivalent minutes at 121°C. F₀ = 3.0 minutes minimum for low-acid canned foods (12D reduction of C. botulinum).

### Industrial Canning Line

An industrial canning operation for the industrial era:

1. **Raw material preparation**: Washing, sorting, peeling (mechanical or lye), cutting. Lye peeling: 10-20% NaOH at 90-100°C for 30-90 seconds, then water rinse removes loosened skins.
2. **Blanching**: Hot water or steam at 85-100°C for 1-5 minutes. Inactivates enzymes, removes air from tissue, softens for packing. Weight loss: 5-15%.
3. **Filling**: Mechanical or hand filling into cans. Fill weight controlled to ±2%. Headspace: 6-10 mm for thermal expansion.
4. **Exhausting**: Heat to 75-85°C or vacuum seaming to remove air (oxygen causes quality loss and can deformation during processing).
5. **Seaming**: Double-seam operation. First operation roll: curls cover hook around body hook. Second operation roll: compresses and tightens the seam. Seam thickness: 1.2-1.5 mm. Overlap: ≥1.0 mm. Gap: ≤0.15 mm.
6. **Thermal processing**: Retort (pressure vessel) at 121°C for prescribed time. Critical controls: initial temperature, come-up time, holding time, cooling time. Process deviation = product must be re-processed or destroyed.
7. **Cooling**: Rapid cooling to 38°C to prevent thermophilic spoilage. Pressure maintained during cooling to prevent can buckling (paneling). Chlorinated cooling water (2-5 ppm free chlorine) prevents post-process contamination through seam micro-leaks.
8. **Storage and inspection**: Hold canned goods for 10-14 days at 35-40°C (incubation test) to detect under-processing. Swollen cans = microbial growth = discard. Also called "swell test."

### Preservation Method Selection Guide

| Food Type | Best Method | Shelf Life | Notes |
|-----------|------------|:----------:|-------|
| Meat (fresh) | Freezing (-18°C) | 6-12 months | Blast freeze at -30°C for quality |
| Meat (cured) | Salting + smoking | 2-6 months | Nitrate essential for botulism safety |
| Fish (fatty) | Smoking + salting | 1-3 months | High oil content limits storage |
| Vegetables | Pressure canning | 12-24 months | Acidify if possible for water bath |
| Fruits | Water bath canning | 12-24 months | Natural acidity allows simpler process |
| Grain | Dry storage (<14% moisture) | 12+ months | Protect from insects and rodents |
| Milk | Pasteurization + refrigeration | 5-7 days | UHT for shelf-stable (6+ months) |
| Juice | Pasteurization (HTST) | 3-6 months | Refrigerated; or UHT for shelf-stable |
