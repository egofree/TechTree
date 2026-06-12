# Food Preservation

> **Node ID**: food-processing.preservation
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: `ceramics`,
> [`chemistry.petroleum-alternatives.fermentation`](../chemistry/petroleum-alternatives.fermentation.md),
> [`health.sanitation`](../health/sanitation.md)
> **Critical**: No — food preservation extends storage life but canning (a separate capability) is the critical long-term storage method
> **Timeline**: Years 0-30+
> **Outputs**: preserved_food, canned_food, pasteurized_food, refrigerated_food, dried_food, salted_food, smoked_food, fermented_food

Food preservation is the technology that eliminates seasonal starvation. Without it, food rots within days to weeks and populations face annual hunger gaps between harvests. With it, food becomes a stable, bankable commodity — enabling urban concentration, specialist labor, and long-distance trade. Every preservation method either removes water (drying, salting), creates hostile chemistry (fermentation, pickling), kills microorganisms with heat (canning, pasteurization), or slows microbial growth (refrigeration, freezing).

## Preservation Methods

| Method | Era | Shelf Life | Energy | Article |
|--------|:---:|:----------:|:------:|:-------:|
| Drying, salting, smoking | Stone-age | 1-18 months | Minimal to none | [Traditional Preservation](traditional-preservation.md) |
| Fermentation | Stone-age → industrial | 1-12 months | Minimal | [Food Fermentation](fermentation.md) |
| Canning (thermal sterilization) | Industrial | 2-5 years | 0.5-3 MJ/jar | [Canning & Thermal Sterilization](canning.md) |
| Pasteurization | Industrial | 5-7 days (refrigerated) to 6+ months (UHT) | 0.1-0.5 MJ/L | [Pasteurization](pasteurization.md) |
| Refrigeration & freezing | Industrial | Days to months (ongoing energy) | 0.5-2.0 kW/m³ | [Refrigeration](refrigeration.md) |

## Food Spoilage Mechanisms

Understanding *why* food spoils is essential for choosing the right preservation method:

| Mechanism | Cause | Time to Spoilage | Prevention |
|-----------|-------|:----------------:|-----------|
| Microbial growth | Bacteria, yeasts, molds | 4-48 hours | Heat kill, pH control, water removal, cold |
| Enzymatic browning | Polyphenol oxidase | 1-4 hours (cut fruit) | Acid (lemon juice), blanching, cold |
| Lipid oxidation | Oxygen + unsaturated fats | Days to weeks | Antioxidants, vacuum packaging, cold |
| Moisture migration | Water activity differential | Days | Proper packaging, moisture barriers |
| Insect/rodent damage | Physical access | Days to weeks | Sealed containers, elevated storage |

## Water Activity Thresholds for Microbial Growth

| Organism Type | Minimum aw for Growth | Examples | Key Products Affected |
|:-------------:|:---------------------:|:--------:|:--------------------:|
| Most bacteria | 0.90 | E. coli, Salmonella, C. botulinum | Fresh meat, milk, vegetables |
| Most yeasts | 0.88 | Saccharomyces, Candida | Fruit, syrups |
| Most molds | 0.70 | Aspergillus, Penicillium | Bread, cheese, dried fruit |
| Halophilic bacteria | 0.75 | Halobacterium | Salted fish |
| Xerophilic molds | 0.61 | Aspergillus restrictus | Dried grains, spices |
| No microbial growth | <0.60 | — | Fully dried foods (stable) |

## Food Safety Reference

| Hazard | Source | Prevention | Lethal Dose |
|--------|--------|-----------|-------------|
| Botulism | C. botulinum toxin | Acidify pH<4.6 OR pressure can 121°C | ~1 ng/kg (ingested) |
| Salmonella | Raw eggs, poultry | Cook to 74°C | Varies (infectious dose ~10-100 organisms) |
| E. coli O157:H7 | Contaminated produce | Cook to 71°C, wash produce | ~10 organisms |
| Listeria | Soft cheese, deli meats | Pasteurize, cook to 74°C | Varies (high risk for immunocompromised) |
| Aflatoxin | Moldy grain/nuts | Dry storage <13% moisture | Chronic exposure: liver cancer |

- **Botulism is the primary hazard** in all food preservation. C. botulinum spores survive 100°C boiling indefinitely. They germinate in anaerobic, low-acid (pH >4.6), moist conditions and produce the most potent biological toxin known. **Prevention is non-negotiable**: pressure can all low-acid foods at 121°C for the full specified time, or ensure pH <4.6 through acidification or fermentation.

## See Also

- [Traditional Preservation](traditional-preservation.md) — drying, salting, smoking
- [Canning & Thermal Sterilization](canning.md) — detailed thermal processing methodology
- [Food Fermentation](fermentation.md) — biological preservation, acidification
- [Pasteurization](pasteurization.md) — heat treatment for liquid foods
- [Refrigeration](refrigeration.md) — mechanical cooling and cold chain
- [Dairy Processing](dairy.md) — pasteurization of milk and dairy products
- [Brewing & Distilling](brewing.md) — pasteurization of beer and wine
- [Ceramics](../ceramics/index.md) — storage vessels, jars, pots for fermentation and canning
- [Health & Sanitation](../health/sanitation.md) — germ theory, hygiene protocols
- [Chemistry: Fermentation](../chemistry/fermentation.md) — fermentation chemistry and microbiology
- [Energy](../energy/index.md) — steam for canning retorts, electricity for refrigeration
- [Mining](../mining/index.md) — salt production for curing and preservation

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Food Processing](./index.md) • [All Domains](../../index.md)*
