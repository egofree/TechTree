# Food Preservation

> **Node ID**: food-processing.preservation
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: `ceramics`,
> [`chemistry.petroleum-alternatives.fermentation`](../chemistry/fermentation.md),
> [`health.sanitation`](../health/sanitation.md)
> **Enables**: None
> **Critical**: No — food preservation extends storage life but canning (a separate capability) is the critical long-term storage method
> **Timeline**: Years 0-30+
> **Outputs**: preserved_food, canned_food, pasteurized_food, refrigerated_food, dried_food, salted_food, smoked_food, fermented_food

## Overview

Food preservation is the technology that eliminates seasonal starvation. Without it, food rots within days to weeks and populations face annual hunger gaps between harvests. With it, food becomes a stable, bankable commodity — enabling urban concentration, specialist labor, and long-distance trade. Every preservation method operates through one of four mechanisms: removes water (drying, salting), creates hostile chemistry (fermentation, pickling, smoking), kills microorganisms with heat (canning, pasteurization), or slows microbial growth (refrigeration, freezing).

This article is the overview hub for the food-preservation family. Each method has its own dedicated article with full workshop-manual depth: [Traditional Preservation](traditional-preservation.md) (drying, salting, smoking), [Canning & Thermal Sterilization](canning.md), [Pasteurization](pasteurization.md), [Refrigeration](refrigeration.md), and [Food Fermentation](fermentation.md). Here we cover the principles common to all methods — spoilage mechanisms, water activity thresholds, food safety reference data, and decision criteria for selecting the right method for a given food and scale.

The position of food preservation in the bootstrap chain: [agriculture](../foundations/food-agriculture.md) produces raw food; preservation makes it storable. Without preservation, a civilization cannot sustain urban populations through winter or drought, cannot maintain standing armies, and cannot conduct long-distance trade in food commodities. Salt production ([mining](../mining/index.md)), ceramic vessels ([ceramics](../ceramics/index.md)), and germ-theory hygiene ([health sanitation](../health/sanitation.md)) are the upstream dependencies. Downstream, stable food supplies enable population density, labor specialization, and the surplus that funds every other bootstrap activity.

## Prerequisites

### Materials

- Raw food inputs — produce, meat, fish, dairy, grain from [agriculture](../foundations/food-agriculture.md)
- [Salt](../mining/salt.md) (NaCl) — 10-30 kg per 100 kg food for curing; strategic resource shared with leather tanning and chemical production
- Fuel wood or charcoal — 2-15 kg per 10 kg food for smoking and kiln drying, from [energy](../energy/index.md)
- Preservative additives — potassium nitrate (saltpeter, KNO₃) at 0.1-0.2% for cured meats; vinegar, sugar, oil as method-appropriate

### Equipment

- [Ceramic vessels](../ceramics/index.md) — storage jars, crocks, fermentation pots
- Drying racks — wood/bamboo frames, 2-4 m² surface per 10 kg fresh food
- Sealed containers — glass jars, metal tins for canning and dry storage
- Heat exchangers and retorts — [metals](../metals/iron-steel.md) fabrication required for industrial methods

### Knowledge

- Water activity (aw) concept — the single most important parameter in food preservation; microbes cannot grow below defined aw thresholds
- pH and acidification — the pH 4.6 boundary separates low-acid foods (require pressure canning at 121°C) from high-acid foods (safe in boiling water bath)
- [Germ theory and sanitation](../health/sanitation.md) — required for all post-Pasteur methods; prevents re-contamination after preservation

### Infrastructure

- Dry, dark, cool storage space — 10-20°C, relative humidity below 60% for dried goods
- Clean water supply for washing produce and equipment
- Ventilation for smoking operations — smoke contains carcinogenic PAHs

## Bill of Materials

The BOM varies by method. The table below shows materials for a representative preservation operation covering the five major method families, scaled per 100 kg of fresh food input.

| Material | Drying | Salting/Curing | Canning | Fermentation | Refrigeration |
|----------|:------:|:--------------:|:-------:|:------------:|:-------------:|
| Fresh food | 100 kg | 100 kg | 100 kg | 100 kg | 100 kg |
| Salt (NaCl) | — | 20-30 kg | — | 2-3 kg (brine) | — |
| Fuel (wood/charcoal) | 5-15 kg (kiln) | — | 10-30 kg (retort) | — | — |
| Sugar | — | — | — | 0-50 kg | — |
| Curing salt (KNO₃) | — | 100-200 g | — | — | — |
| Jars/cans (1 L) | — | — | 80-120 units | 20-50 units | — |
| Ceramic crocks | — | 5-10 units | — | 5-10 units | — |
| Electricity | — | — | — | — | 200-500 kWh/day (100 m³) |
| Source | [Agriculture](../foundations/food-agriculture.md), [Forestry](../plants/index.md) | [Mining](../mining/salt.md) | [Metals](../metals/iron-steel.md), [Ceramics](../ceramics/index.md) | [Agriculture](../foundations/food-agriculture.md) | [Energy](../energy/index.md) |

## Process Description

Each preservation method follows a distinct procedure. The steps below cover the method-selection decision process and the common preparatory steps; detailed step-by-step procedures for each method are in the dedicated articles linked from [Variations and Alternatives](#variations-and-alternatives).

### Method Selection

1. Assess food type: high-acid (pH <4.6: most fruits, fermented foods) or low-acid (pH >4.6: meat, vegetables, dairy).
2. Assess required shelf life: days (refrigeration), weeks-6 months (drying, fermentation), 1-5 years (canning).
3. Assess available infrastructure: no energy (sun drying, salting, fermentation), fuel available (smoking, kiln drying, canning), electricity available (refrigeration, freezing, industrial canning).
4. Assess water activity target: reduce to <0.60 for full microbial stability (drying, heavy salting); or maintain high aw with other controls (refrigeration, fermentation at pH <4.6, canning via thermal kill).

### Common Preparatory Steps

1. Sort and grade raw food — remove bruised, moldy, or damaged items. One spoiled item contaminates the batch.
2. Wash thoroughly in clean potable water — remove soil, insect debris, and surface microbial load.
3. Peel, trim, and cut to uniform size — ensures even penetration of salt, heat, or smoke. Non-uniform pieces dry or heat at different rates.
4. Blanch vegetables (optional) — immerse in boiling water or steam for 1-5 minutes to deactivate enzymes that cause off-flavors and color loss during storage.
5. Apply the preservation method per its dedicated procedure.
6. Package in appropriate container — moisture-proof for dried goods, hermetic seal for canned goods, anaerobic for fermented goods.
7. Label with date and method. Store under conditions appropriate to the method (dry/cool/dark for shelf-stable; refrigerated for pasteurized).

### Food Spoilage Mechanisms

Understanding why food spoils is essential for choosing the right preservation method:

| Mechanism | Cause | Time to Spoilage | Prevention |
|-----------|-------|:-----------------:|------------|
| Microbial growth | Bacteria, yeasts, molds | 4-48 hours | Heat kill, pH control, water removal, cold |
| Enzymatic browning | Polyphenol oxidase | 1-4 hours (cut fruit) | Acid (lemon juice), blanching, cold |
| Lipid oxidation | Oxygen + unsaturated fats | Days to weeks | Antioxidants, vacuum packaging, cold |
| Moisture migration | Water activity differential | Days | Proper packaging, moisture barriers |
| Insect/rodent damage | Physical access | Days to weeks | Sealed containers, elevated storage |

## Quantitative Parameters

### Water Activity Thresholds for Microbial Growth

Water activity (aw) is the ratio of water vapor pressure in food to that of pure water at the same temperature. It is the single most predictive parameter for microbial growth.

| Organism Type | Minimum aw for Growth | Examples | Key Products Affected |
|:-------------:|:---------------------:|:--------:|:---------------------:|
| Most bacteria | 0.90 | E. coli, Salmonella, C. botulinum | Fresh meat, milk, vegetables |
| Most yeasts | 0.88 | Saccharomyces, Candida | Fruit, syrups |
| Most molds | 0.70 | Aspergillus, Penicillium | Bread, cheese, dried fruit |
| Halophilic bacteria | 0.75 | Halobacterium | Salted fish |
| Xerophilic molds | 0.61 | Aspergillus restrictus | Dried grains, spices |
| No microbial growth | <0.60 | — | Fully dried foods (stable) |

### Preservation Method Comparison

| Method | Target aw | Temperature | Processing Time | Shelf Life | Energy |
|--------|:---------:|:-----------:|:---------------:|:----------:|:------:|
| Sun drying | <0.60 | Ambient (25-40°C) | 2-5 days | 6-12 months | None (solar) |
| Kiln drying | <0.60 | 50-70°C | 6-24 hours | 6-12 months | 2-5 MJ/kg |
| Salting (heavy) | 0.65-0.75 | Ambient | 2-8 weeks | 6-18 months | Minimal |
| Fermentation | pH <4.6 | 15-30°C | 3-30 days | 1-12 months | Minimal |
| Smoking (hot) | 0.70-0.80 | 60-80°C | 4-12 hours | 2-6 months (refrigerated) | 2-5 MJ/kg |
| Pasteurization (HTST) | — | 72°C | 15 sec | 5-7 days (refrigerated) | 0.1-0.3 MJ/L |
| Canning (pressure) | — | 121°C | 15-90 min | 2-5 years | 0.5-3 MJ/jar |
| Refrigeration | — | 0-4°C | Ongoing | 3-7 days | 0.5-2.0 kW/m³ |
| Freezing | — | -18°C | Ongoing | 6-12 months | 0.5-2.0 kW/m³ |

## Scaling Notes

- **Household scale** (family of 4-8): Sun drying on racks, small-batch salting in crocks, water-bath canning of high-acid foods. Throughput: 5-20 kg per batch. Labor: 4-8 hours per batch. Equipment: minimal (pots, jars, racks).
- **Community scale** (50-2,000 people): Dedicated drying sheds, barrel salting operations, small HTST pasteurizer or batch pasteurizer, walk-in cold room (10-50 m³). Throughput: 100-500 kg per batch. Requires 5-20 kW for mechanical refrigeration.
- **Industrial scale** (10,000+ people): Continuous drying tunnels, automated canning lines (retort sterilization), large plate heat exchangers, 100-1,000+ m³ cold storage. Throughput: 1-50 tonnes/day. Requires steam supply, electrical power, and transportation infrastructure.
- **Salt logistics bottleneck**: Preserving 1 tonne of meat by heavy salting requires 200-300 kg salt. A community of 500 people preserving winter meat needs 5-10 tonnes of salt per year — a significant supply-chain burden. Salt production must be planned alongside food preservation infrastructure (see [Mining](../mining/salt.md)).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Mold on dried food | Insufficient drying (aw >0.70), storage humidity too high, poor packaging | Dry to <10% moisture (aw <0.60). Store in sealed containers with desiccant. Keep below 60% RH |
| Swollen cans (botulism risk) | C. botulinum growth in under-processed low-acid canned food | Discard immediately — do NOT taste. Review pressure canning time/temperature. Low-acid foods require 121°C at 15 psi for full duration |
| Fermentation fails to start | Insufficient salt (allows spoilage bacteria), temperature too low, no inoculum | Use 2-3% brine for vegetables. Maintain 18-25°C. Add starter culture (whey, brine from previous batch) |
| Rancid salted meat | Fat oxidation, storage temperature too high, insufficient salt | Store below 15°C. Increase salt concentration. Trim visible fat before salting (fat oxidizes faster than lean) |
| Refrigerated food spoils early | Cold chain break, temperature above 4°C, post-processing contamination | Maintain 0-4°C continuously. Install temperature alarms. Cool rapidly after processing |
| Fermented food too sour | Extended fermentation, temperature too high | Reduce fermentation time. Lower temperature to slow lactic acid bacteria activity |

## Safety

Botulism is the primary hazard across all food preservation. *Clostridium botulinum* spores survive 100°C boiling indefinitely. They germinate in anaerobic, low-acid (pH >4.6), moist conditions and produce the most potent biological toxin known — lethal dose approximately 1 ng/kg body weight (ingested). Prevention is non-negotiable: pressure-can all low-acid foods at 121°C for the full specified time, or ensure pH <4.6 through acidification or fermentation.

### Food Safety Reference Table

| Hazard | Source | Prevention | Lethal Dose |
|--------|--------|-----------|-------------|
| Botulism | C. botulinum toxin | Acidify pH <4.6 OR pressure can 121°C | ~1 ng/kg (ingested) |
| Salmonella | Raw eggs, poultry | Cook to 74°C | Infectious dose ~10⁵ organisms |
| E. coli O157:H7 | Contaminated produce | Cook to 71°C, wash produce | Infectious dose ~10 organisms |
| Listeria | Soft cheese, deli meats | Pasteurize, cook to 74°C | Varies (high risk for immunocompromised) |
| Aflatoxin | Moldy grain/nuts | Dry storage <13% moisture | Chronic exposure: liver cancer |

### Refrigerant Safety (Refrigeration Method)

Ammonia (R717) is toxic at 300 ppm and lethal at 5,000 ppm. Ammonia refrigeration systems require leak detection and forced ventilation. See [Refrigeration](refrigeration.md) for full refrigerant safety details.

### Personal Protective Equipment

- Heat-resistant gloves for canning retort and smoking operations
- Cutting boards and sharp knives (dull knives cause more accidents than sharp ones)
- Food-grade gloves when handling curing salts (KNO₃ and NaNO₂ are toxic in concentrated form)

## Quality Control

### Acceptance Criteria

- **Dried foods**: Final moisture content 10-20% for vegetables/fruits, 5-10% for meat (jerky). Water activity aw <0.60.
- **Canned foods**: Vacuum seal intact (lid concave, does not flex). No swelling, no leakage. pH <4.6 for water-bath canned goods.
- **Fermented foods**: pH dropped to ≤4.0 (lactic fermentation). Characteristic aroma, no off-odors.
- **Pasteurized liquids**: Phosphatase test negative (confirms adequate heat treatment for milk).

### Testing Methods

- pH measurement — litmus paper (low-tech, ±0.5 accuracy) or pH meter (±0.1 accuracy). Critical threshold: pH 4.6 separates safe water-bath canning from required pressure canning.
- Water activity meter — electronic hygrometer, accuracy ±0.02 aw. Field alternative: salt brine calibration (saturated NaCl = aw 0.75).
- Visual inspection — mold growth, color change, gas bubbles in canned goods (sign of microbial activity).
- Smell test — off-odors (sulfurous, rancid, alcoholic in non-fermented goods) indicate spoilage. Never taste-test suspect food.

### Sampling Procedure

- Inspect every canned jar before opening: check seal integrity, lid flex, swelling.
- Sample dried goods weekly during first month of storage for mold or insect activity.
- Monitor fermentation daily during active phase (days 1-7): check pH, gas production, aroma.

## Variations and Alternatives

### Method Selection by Food Type

| Food Type | Best Method | Why | Alternative |
|-----------|-------------|-----|-------------|
| Fresh meat | Freezing (-18°C) | Minimal quality change, 6-12 month storage | Canning (2-5 years but texture changes) |
| Fresh fish | Freezing or heavy salting | Rapid quality loss at room temp | Smoking (after brining) |
| Fresh milk | Pasteurization + refrigeration | Preserves flavor, short chain | UHT (6+ months ambient) or cheese (fermentation) |
| Vegetables (low-acid) | Pressure canning (121°C) | Required for botulum safety | Freezing, fermentation (pickling) |
| Fruits (high-acid) | Water-bath canning, drying | pH <4.6 allows boiling-water processing | Jam/syrup (sugar preservation) |
| Grain/flour | Dry storage (aw <0.60) | Already low moisture; keep dry | — |

### Regional Adaptations

- **Humid tropical climates**: Sun drying fails (RH >60%). Use fermentation, salting, or smoking. Root crops (cassava, yam) ferment well in tropics.
- **Cold temperate climates**: Freezing is natural in winter — ice houses provide 50-200 tonnes of natural ice per winter. Combine with salting for summer.
- **Arid climates**: Sun drying is optimal. Grapes → raisins, plums → prunes, apricots, tomatoes all sun-dry efficiently.

For complete step-by-step procedures for each method, see the dedicated articles: [Traditional Preservation](traditional-preservation.md), [Canning & Thermal Sterilization](canning.md), [Pasteurization](pasteurization.md), [Refrigeration](refrigeration.md), [Food Fermentation](fermentation.md).

## References

- [Traditional Preservation](traditional-preservation.md) — drying, salting, smoking workshop manual
- [Canning & Thermal Sterilization](canning.md) — pressure canning and water bath canning
- [Pasteurization](pasteurization.md) — LTLT, HTST, UHT heat treatment
- [Refrigeration](refrigeration.md) — mechanical cooling, cold chain, ice production
- [Food Fermentation](fermentation.md) — biological preservation via lactic acid bacteria and yeasts
- [Dairy Processing](dairy.md) — cheese and fermented dairy as preservation
- [Brewing & Distilling](brewing.md) — fermentation-based calorie concentration
- [Ceramics](../ceramics/index.md) — storage vessels, jars, pots for all preservation methods
- [Health & Sanitation](../health/sanitation.md) — germ theory, hygiene protocols
- [Mining: Salt](../mining/salt.md) — salt production for curing
- [Energy](../energy/index.md) — steam for canning retorts, electricity for refrigeration

---

*Part of the [Bootciv Tech Tree](../index.md) • [Food Processing](./index.md) • [All Domains](../index.md)*
