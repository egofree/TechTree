# Brewing & Distilling

> **Node ID**: food-processing.brewing
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: [`chemistry.petroleum-alternatives.fermentation`](../chemistry/fermentation.md), `energy`
> **Enables**: None (leaf capability)
> **Timeline**: Years 0-25+
> **Outputs**: beer, wine, spirits, industrial_ethanol, spent_grain, vinegar

## Overview

Brewing and distilling are the earliest industrial biotechnology. Beer and wine were historically safer to drink than water (the ethanol and low pH kill pathogens), making them workforce fuel rather than luxury goods. Distillation produces concentrated spirits (water purification: whiskey, brandy, rum) and industrial ethanol (solvent, fuel, chemical feedstock). The same fermentation knowledge that produces beer and wine also produces vinegar (acetic acid), a critical food preservative and cleaning agent.

For industrial fermentation chemistry (ethanol, acetone, butanol as chemical feedstocks), see [Chemistry: Fermentation](../chemistry/fermentation.md). This document covers the food and beverage side of fermentation.

## Bill of Materials

### Beer Brewing Materials

| Material | Quantity per 100 L beer (5% ABV) | Source | Alternatives |
|----------|:---------------------------------:|--------|-------------|
| Malted barley | 20-25 kg | [Agriculture](../foundations/food-agriculture.md) | Wheat malt, rye malt |
| Hops (dried) | 100-300 g | [Agriculture](../foundations/food-agriculture.md) | Herbal bittering (gruit: wormwood, yarrow, heather) |
| Water (brewing liquor) | 120-150 L | [Water](../water/index.md) | Must be potable and chlorine-free |
| Yeast (S. cerevisiae) | 5-15 g dry or 0.5-1.0 L starter | Propagated from previous batch | Wild yeast capture (variable results) |
| Calcium sulfate (gypsum) | 50-150 g | [Mining](../mining/index.md) | Calcium chloride (CaCl₂) — different ion profile |
| Cleaning sanitizer | 50-100 mL 5% solution | [Chemistry](../chemistry/index.md) | Boiling water or steam |

### Wine Making Materials

| Material | Quantity per 100 L wine (12% ABV) | Source | Alternatives |
|----------|:---------------------------------:|--------|-------------|
| Grapes (fresh) | 130-170 kg | [Agriculture](../foundations/food-agriculture.md) | Other fruit (apples, plums, berries) |
| Wine yeast (S. cerevisiae) | 10-25 g dry | Commercial or propagated | Wild yeast on grape skins (unpredictable) |
| Sulfur dioxide (Campden tablets) | 5-10 g | [Chemistry](../chemistry/index.md) | Pasteurization for stabilization |
| Oak barrels (optional) | 1-4 barrels (225 L each) | [Forestry](../plants/index.md) | Stainless steel tanks (no oak character) |

### Distilling Materials

| Material | Quantity per L spirit (40% ABV) | Source | Alternatives |
|----------|:-------------------------------:|--------|-------------|
| Fermented wash (8-10% ABV) | 5.0-6.0 L | Produced on-site from grain or fruit | Sugar wash (molasses, cane juice) |
| Copper (still construction) | 2-5 kg per 100 L still | [Metals](../metals/index.md) | Stainless steel (no sulfur removal) |
| Cooling water | 200-500 L per distillation run | [Water](../water/index.md) | Recirculated with cooling tower |
| Oak barrels (aging, whiskey) | 1 barrel per 200 L | [Forestry](../plants/index.md) | Stainless steel (unaged spirit) |

## Process Description

### Beer Brewing

Beer is fermented malted grain. The basic process: malt grain → mash → boil with hops → ferment → condition.

**Malting** (grain preparation):
1. **Steeping**: Submerge barley (or wheat) in water, 8-12 hours at 12-15°C. Alternate wet/dry cycles over 48 hours until grain moisture reaches 43-46%.
2. **Germination**: Spread wet grain on malting floor, 12-18°C, for 4-6 days. Grain sprouts, producing enzymes (α-amylase, β-amylase, proteases) that will later convert starch to sugar. Turn grain daily to prevent matting and ensure even germination.
3. **Kilning**: Dry malted grain in kiln at 60-80°C for 24-48 hours (light malt) or 100-110°C for darker malts. Kilning stops germination and develops flavor/color through Maillard reactions. Moisture reduced to <5%.
4. **Malt types**: Pale malt (kilned 60-80°C, light color, high enzyme activity), crystal malt (stewed then kilned 130-150°C, caramel flavors, no enzyme activity), chocolate malt (kilned 200-220°C, dark color, roasted flavors). Most beers use 80-100% pale malt.

**Mashing** (starch conversion):
- **Process**: Mix crushed malt (see [Milling](milling.md)) with hot water in mash tun. Temperature controlled to activate specific enzymes:
  - **Protein rest**: 45-55°C for 10-20 minutes. Proteases break down proteins to amino acids (yeast nutrients). Only needed for undermodified malt.
  - **β-amylase optimum**: 60-65°C. Produces maltose (fermentable sugar). Creates dry, attenuated beer.
  - **α-amylase optimum**: 68-72°C. Produces dextrins (partially fermentable). Creates fuller body.
  - **Mash-out**: 76-78°C for 5-10 minutes. Denatures all enzymes, fixing sugar profile.
- **Water-to-grain ratio**: 2.5-3.5 L water per kg malt. Thicker mash = more body, thinner mash = more fermentable.
- **Single infusion mash** (simplest): Add grain to water at 65-68°C, hold 60 minutes, mash out at 78°C. Sufficient for well-modified pale malt. Temperature accuracy ±1°C critical.
- **Sparging**: After mashing, rinse grain bed with 75-78°C water to extract remaining sugars. Collect sweet liquid (wort). Stop sparging when gravity drops below 1.008 (2° Plato) to avoid extracting harsh tannins.
- **Yield**: 1 kg malt yields ~3-4 liters of wort at 12° Plato (1.048 SG), producing ~3 liters of 5% beer.

**Boiling** (wort sterilization and hopping):
- **Duration**: 60-90 minutes rolling boil. Purpose: sterilize wort, isomerize hop acids (bitterness), coagulate proteins (hot break), concentrate sugars.
- **Hops**: Add at start of boil for bitterness (60+ minutes, α-acid isomerization ~30% efficient), middle for flavor (15-30 minutes), end for aroma (0-10 minutes, volatile oils preserved).
- **Hop bittering**: α-acids (humulone, cohumulone, adhumulone) isomerize during boil. Bitterness measured in International Bitterness Units (IBU). Typical range: 10-40 IBU for standard ales, 15-25 IBU for lagers, 40-100 IBU for IPAs.
- **Original gravity**: 1.040-1.080 SG (10-20° Plato). Higher gravity = more alcohol = more body.
- **Cooling**: Rapidly cool wort from 100°C to 18-20°C (ale) or 8-12°C (lager) using wort chiller (copper coil with cold water, or plate heat exchanger). Fast cooling prevents bacterial contamination and cold break formation.

**Fermentation**:
- **Yeast**: Saccharomyces cerevisiae (ale yeast, top-fermenting, 15-22°C) or S. pastorianus (lager yeast, bottom-fermenting, 8-14°C).
- **Pitching rate**: 0.75-1.5 million cells per mL per degree Plato. Underpitching causes off-flavors, overpitching causes thin beer.
- **Primary fermentation**: 3-7 days (ale) or 7-14 days (lager). Yeast consumes sugars: glucose → maltose → maltotriose. Temperature control critical ±1°C. Excess temperature produces fusel alcohols (headache-causing).
- **Gravity monitoring**: Hydrometer tracks fermentation progress. Final gravity 1.008-1.015 (2-4° Plato). Alcohol by volume = (OG - FG) × 131.25. Typical: 4-6% ABV for standard ales/lagers.
- **Conditioning (secondary)**: 1-4 weeks at 10-15°C (ale) or 0-4°C (lager). Yeast reabsorbs off-flavors (diacetyl, acetaldehyde). Lager conditioning (lagering) at 0-4°C for 4-8 weeks produces clean flavor.

**Packaging**:
- **Cask (real ale)**: Secondary fermentation in cask with priming sugar. Natural carbonation. Shelf life: 3-7 days once tapped.
- **Bottling**: Add priming sugar (4-5 g/L) before sealing. Bottle conditioning produces natural carbonation over 1-2 weeks at 18-20°C. Shelf life: 6-12 months.
- **Kegging**: Force carbonate with CO₂ at 10-15 psi at 4°C. Immediate carbonation. Shelf life: 2-4 weeks once tapped.

### Wine Making

**Grape wine**:
1. **Harvest**: Grapes at 20-25° Brix (sugar content), pH 3.2-3.5. Harvest by hand or machine.
2. **Crushing/Destemming**: Break grape skins, remove stems. Press to separate juice (white wine) or ferment with skins (red wine, 5-10 days skin contact for color/tannin extraction).
3. **Pressing**: Basket press or bladder press at 1.5-2.0 bar. Yield: 600-700 L juice per tonne grapes.
4. **Fermentation**: Saccharomyces cerevisiae at 15-20°C (white) or 25-30°C (red). Duration: 7-14 days. Malolactic fermentation (Oenococcus oeni) optional for red wines and some whites: converts sharp malic acid to softer lactic acid.
5. **Aging**: Stainless steel tanks (fresh fruit flavors) or oak barrels (6-24 months, adds vanilla/toast compounds from oak lignin). Barrel size: 225 L (Bordeaux) or 228 L (Burgundy).
6. **Alcohol content**: 11-15% ABV. Higher alcohol inhibits spoilage organisms.

**Fruit wines and mead**: Same basic process with different sugar sources. Honey mead requires 15-18% dilution and yeast nutrient additions (honey lacks nutrients for yeast).

### Distilling

Distillation separates ethanol (boiling point 78.3°C) from water (100°C) by selective evaporation and condensation. Produces spirits of 40-95% ABV.

**Pot still distillation** (batch):
- **Design**: Copper pot (50-2000 L) with swan neck, lyne arm, and condenser (worm coil in cold water bath). Copper catalytically removes sulfur compounds (dimethyl sulfide, hydrogen sulfide) that cause off-flavors.
- **First distillation (stripping run)**: Distill fermented wash at 85-95°C. Collect "low wines" at 20-30% ABV. Discard first 2-5% ("foreshots" — methanol, acetone, highly toxic). Stop collecting at 5-10% ABV ("tails" — fusel oils, congeners).
- **Second distillation (spirit run)**: Redistill low wines with finer cuts:
  - **Heads/foreshots** (first 2-5%): Methanol (boiling point 64.7°C), acetone (56°C), ethyl acetate. **Discard — methanol causes blindness and death.** Methanol content in heads: 0.5-2% of distillate.
  - **Hearts** (middle 60-70%): Clean ethanol at 65-80% ABV. The drinkable product.
  - **Tails** (last 20-30%): Fusel alcohols (propanol, butanol, amyl alcohol), fatty acids. May be redistilled or discarded.
- **Yield**: 1 kg fermentable sugar yields ~0.51 kg ethanol (theoretical maximum by mass). Practical yield: 0.40-0.45 kg ethanol per kg sugar. For grain: 1 kg malted barley yields ~0.35 L pure ethanol.

**Column still distillation** (continuous):
- **Design**: Vertical column (3-10 m) with perforated plates. Steam enters bottom, wash enters middle. Vapor rises through plates, enriching in ethanol. Reflux condenser at top returns some vapor for separation improvement.
- **Advantage**: Continuous operation, higher throughput, more consistent product. Can produce 95.6% ABV (azeotrope limit for ethanol-water).
- **Products**: Neutral spirits (vodka, gin base), grain whisky (partially refined), industrial ethanol.
- **Beyond 95.6%**: Azeotropic distillation with benzene or cyclohexane, or molecular sieves (3 Å zeolite), required for absolute (anhydrous) ethanol.

**Aging spirits**:
- **Whiskey**: Oak barrels (charred American oak or toasted European oak), 3-12+ years. Char layer filters and adds flavor compounds. 2% volume loss per year ("angel's share"). Climate-controlled warehouse: 15-20°C, 60-70% humidity.
- **Brandy**: Oak barrels, 2-10+ years. Similar principles to whiskey aging.
- **Rum**: Oak barrels (often used bourbon barrels), 1-7+ years.

### Industrial Ethanol

Ethanol for industrial use (solvent, fuel, chemical feedstock) follows the same fermentation and distillation principles:

- **Feedstock**: Grain, sugarcane, or cellulosic biomass. Sugarcane is most efficient: 7,000 L ethanol/hectare/year (Brazil).
- **Concentration**: 95.6% ABV by simple distillation. 99.5%+ by molecular sieve dehydration.
- **Denaturing**: Add bitterant (denatonium benzoate, 10 ppm) or toxicant (methanol, 5-10%) to prevent human consumption of industrial ethanol. Denatured spirits ("denatured alcohol") is tax-exempt in most jurisdictions.
- **Fuel ethanol**: Blended with gasoline at 10-85% (E10 to E85). Requires anhydrous ethanol (<0.5% water) to prevent phase separation.

### Vinegar Production

Vinegar (acetic acid 5-8% in water) is produced by aerobic oxidation of ethanol by Acetobacter bacteria:

- **Orleans method** (traditional): Fill barrels 2/3 with wine/cider. Inoculate with vinegar mother (Acetobacter culture). Leave 1-3 months with air access. Surface fermentation — bacteria form a pellicle on the liquid surface.
- **Generator method** (faster): Trickling generator — alcohol solution percolates through beechwood shavings inoculated with Acetobacter. Air flows upward. 5-10× faster than Orleans method.
- **Submerged culture** (industrial): Forced aeration in stainless steel tanks at 28-32°C. 20-40 hour cycle. Most efficient. Acetic acid concentration reaches 12-15%.
- **Distilled white vinegar**: 5% acetic acid from grain alcohol. Standard for pickling and cleaning.
- **Apple cider vinegar**: 5-6% acetic acid from hard cider. Popular for food use.
- **Cleaning application**: 5% acetic acid solution kills 80-90% of bacteria and 90%+ of mold on surfaces. Food-safe disinfectant for dairy and brewing equipment.

## Quantitative Parameters

### Fermentation Yields and Efficiency

| Product | Feedstock | Yield (L product per kg feedstock) | ABV | Primary Process Temperature |
|---------|-----------|:----------------------------------:|:---:|:---------------------------:|
| Ale beer | Malted barley | 3.0-3.5 L/kg | 4-6% | 15-22°C |
| Lager beer | Malted barley | 3.0-3.5 L/kg | 4-5% | 8-14°C |
| Wine (grape) | Grapes | 0.60-0.70 L/kg | 11-15% | 15-30°C |
| Whiskey (pot still) | Grain mash | 0.30-0.40 L/kg | 65-80% (distillate) | 85-95°C (distillation) |
| Neutral spirits (column) | Grain/sugar | 0.35-0.45 L/kg | 95.6% (max) | 78-100°C (distillation) |
| Vinegar (submerged) | Wine/cider | 0.90-0.95 L/L | 5-15% acetic acid | 28-32°C |

### Mashing Temperature Ranges and Effects

| Temperature Range | Enzyme Active | Effect on Wort |
|:-----------------:|:-------------:|:--------------|
| 45-55°C | Proteases | Protein breakdown → amino acids (yeast nutrients) |
| 60-65°C | β-amylase | Maltose production → dry, attenuated beer |
| 68-72°C | α-amylase | Dextrin production → full body, less fermentable |
| 76-78°C | None (mash-out) | Denatures all enzymes, fixes sugar profile |

### Distillation Cut Points

| Fraction | Temperature Range | ABV | Composition | Disposition |
|----------|:-----------------:|:---:|-------------|:-----------:|
| Foreshots/heads | 64-78°C | 80-95% | Methanol, acetone, ethyl acetate | Discard (toxic) |
| Hearts | 78-82°C | 65-80% | Clean ethanol | Product |
| Tails | 82-95°C | 5-40% | Fusel alcohols, fatty acids | Redistill or discard |

### Wort Gravity and Alcohol Calculations

| Parameter | Symbol | Typical Range | Formula |
|-----------|:------:|:-------------:|---------|
| Original gravity | OG | 1.040-1.080 | Measured by hydrometer before fermentation |
| Final gravity | FG | 1.008-1.015 | Measured by hydrometer after fermentation |
| Alcohol by volume | ABV | 4-6% (beer), 11-15% (wine) | (OG - FG) × 131.25 |
| Apparent attenuation | AA | 70-80% (ale), 75-85% (lager) | (OG - FG) / (OG - 1.000) × 100 |
| Degrees Plato | °P | 10-20°P | °P ≈ (SG - 1) × 1000 / 4 |

## Scaling Notes

- **Home brewing** (20-50 L batch): Single vessel for mashing and boiling (brew-in-a-bag or mash tun + kettle). Ferment in food-grade bucket or glass carboy. Manual siphoning. Labor: 4-6 hours per batch (brew day) + passive fermentation. Throughput: 20-50 L every 2-4 weeks.
- **Community brewery** (200-1000 L): Separate mash tun, boil kettle, and fermenters. Gravity-fed or pumped transfer. Multiple fermenters staged at different phases. Labor: 2-3 workers for 6-8 hours per brew session. Throughput: 200-500 L/week.
- **Industrial brewery** (10,000-100,000+ L/year): Automated mashing, whirlpool, heat exchangers, cylindroconical fermenters with glycol jacket temperature control. Continuous bottling or kegging line. Throughput: 5,000-50,000 L/week. Key scaling issue: fermentation temperature control — a 10,000 L fermenter produces 670 MJ of heat during active fermentation, requiring 15-30 kW cooling capacity.
- **Distillery scaling**: Pot stills scale linearly (larger pot = more product per run). Column stills are inherently continuous and scale by diameter. A 0.3 m diameter column produces ~50 L/hour; a 1.0 m column produces ~500 L/hour. Copper requirement scales proportionally — catalytic surface area must remain proportional to throughput.
- **Energy budget**: Mashing requires 2-3 MJ/L (heating water and grain to 65-78°C). Boiling requires 1-2 MJ/L (maintaining rolling boil for 60-90 minutes). Distillation requires 5-10 MJ/L ethanol (latent heat of vaporization + column losses). Total energy for a brewery-distillery: 8-15 MJ/L of finished product.
- **Water consumption**: Brewing uses 3-7 L water per L beer (including cleaning, cooling, and sparging). Distillation adds 2-5 L cooling water per L distillate. Water reclamation via cooling towers reduces consumption by 60-80%.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Stuck fermentation (gravity stalls) | Yeast underpitched, temperature too low, nutrient deficiency | Re-pitch with fresh yeast at 18-20°C. Add yeast nutrient (diammonium phosphate at 200 mg/L). Ensure temperature within yeast strain range |
| Off-flavor: buttery (diacetyl) | Insufficient diacetyl rest, premature cooling | Raise to 15-18°C for 2-3 days near end of fermentation (diacetyl rest). Extend conditioning |
| Off-flavor: sour/acidic | Bacterial contamination (Lactobacillus, Acetobacter) | Improve sanitation. Replace airlock fluid. Discard batch if pH <3.0. Sanitize equipment with boiling water |
| Cloudy beer (chill haze) | Protein-polyphenol complex at cold temperatures | Use Irish moss (carrageenan, 5 g at 15 min left in boil). Cold condition at 0-2°C for 2+ weeks |
| Low alcohol (high final gravity) | Incomplete fermentation, mash too hot (excess dextrins) | Ensure mash temperature accuracy ±1°C. Use highly attenuating yeast strain. Extend fermentation |
| Excess foaming (boilover) | Proteins and hops cause foam, heat too high | Use larger kettle (minimum 20% headspace). Reduce heat to gentle roll. Add hops gradually |
| Methanol in spirits | Foreshots not properly discarded | Always discard first 2-5% of distillate. Never shortcut this cut. Foreshots volume: 20-50 mL per 100 L wash |
| Low distillation yield | Insufficient fermentation, leaks in still, poor cuts | Verify wash ABV before distilling (target 8-10%). Check all joints and seals. Make tighter cuts |
| Vinegar not forming | Acetobacter not established, temperature too low | Inoculate with raw vinegar mother. Maintain 25-30°C. Ensure air access (Acetobacter is aerobic) |

## Safety

- **Methanol poisoning**: Methanol (wood alcohol) is metabolized to formaldehyde and formic acid, causing blindness and death. Dose: 10 mL pure methanol can cause blindness, 30-100 mL can be fatal. **Never consume the foreshots/heads fraction of any distillation.**
- **Botulism in home brewing**: Improperly sealed home-canned beer or wine can grow C. botulinum. Maintain proper acidity (pH <4.6) and sanitary conditions.
- **Acetone and fusel alcohols**: Higher alcohols (propanol, butanol, amyl alcohol) in tails cause severe headaches and nausea. Proper cuts during distillation are essential.
- **Pressure in stills**: Pot stills must have pressure relief valves. Column stills operate at slight positive pressure. Overpressure can cause explosion. Never block a still outlet.
- **Fire hazard**: Ethanol vapor is flammable at 3.3-19% concentration in air. Distillation areas must be well-ventilated. No open flames near stills.
- **CO₂ asphyxiation**: Fermentation produces CO₂ (2 mol per mol glucose). In enclosed spaces, CO₂ accumulates at floor level (density 1.98 kg/m³ vs. air 1.29 kg/m³). Ventilation: minimum 5 air changes per hour for commercial fermentation rooms. CO₂ monitors at floor level mandatory. Evacuate at >5,000 ppm (0.5%).

## Quality Control

### Quality Control in Brewing

- **pH monitoring**: Mash pH must be 5.2-5.6 for optimal enzyme activity. Adjust with calcium salts (gypsum CaSO₄ at 100-300 mg/L, or calcium chloride CaCl₂ at 100-200 mg/L). Beer pH after fermentation: 3.8-4.4. pH >4.6 indicates incomplete fermentation or contamination.
- **Microbiological testing**: Plate counts for wild yeast and bacteria. Lactic acid bacteria (Lactobacillus, Pediococcus) cause souring. Acetobacter produces vinegar. Wild yeast (Brettanomyces) produces barnyard flavors (desired in some Belgian styles, fault in most others).
- **Diacetyl test**: Diacetyl (2,3-butanedione) produces a buttery flavor. Formed during fermentation, reabsorbed by yeast during conditioning. Diacetyl rest: raise temperature to 15-18°C for 2-3 days near end of fermentation. Test: heat sample to 60°C for 10 min, cool, smell for butter. If present, extend diacetyl rest.
- **Carbonation**: Target 2.2-2.8 volumes CO₂ for most ales (1 volume = 1 L CO₂ per L beer at STP). Force carbonation at 10-15 psi at 4°C. Natural carbonation via priming sugar at 4-5 g/L.

### Fermentation Biochemistry

Understanding the chemistry of fermentation is essential for process control:

**Glycolysis (Embden-Meyerhof pathway)**:
C₆H₁₂O₆ → 2 CH₃CH₂OH + 2 CO₂ + 2 ATP
Glucose → 2 ethanol + 2 carbon dioxide + energy (for yeast)

- **Stoichiometry**: 180 g glucose produces 92 g ethanol + 88 g CO₂. By volume: 1 mol glucose (180 g) → 2 mol ethanol (115 mL) + 2 mol CO₂ (44.8 L at STP).
- **Heat release**: Fermentation is exothermic: ~100 kJ per mol glucose fermented. A 1000 L fermentation tank at 12° Plato (120 g/L fermentable sugar) produces ~67 MJ of heat over the course of fermentation. Temperature control requires cooling capacity of 2-5 kW per 1000 L for active fermentation.
- **Byproducts**: Besides ethanol and CO₂, yeast produces glycerol (1-3% of sugar carbon), higher alcohols (fusel oils: 50-300 mg/L), esters (ethyl acetate, isoamyl acetate: 10-100 mg/L), and organic acids (succinic, acetic: 0.1-1 g/L). These byproducts define beer and wine flavor character.
- **Yeast nutrition**: Yeast requires nitrogen (amino acids from malt protein degradation, or diammonium phosphate supplement at 200-400 mg N/L for wine), vitamins (biotin, thiamine, pantothenic acid), and minerals (magnesium, zinc at 0.1-0.5 mg/L). Nutrient deficiency causes stuck fermentation (sugar remains unfermented, sweet product, spoilage risk).

**Wort gravity and alcohol calculation**:
- **Specific gravity (SG)**: Density of wort relative to water. Water = 1.000. Typical wort: 1.040-1.080.
- **Plato (°P)**: Grams of sugar per 100 g solution. 12°P ≈ 1.048 SG. Conversion: °P ≈ (SG - 1) × 1000 / 4.
- **Alcohol by volume (ABV)**: ABV ≈ (OG - FG) × 131.25. Example: OG 1.050, FG 1.012 → ABV = (1.050 - 1.012) × 131.25 = 4.99%.
- **Attenuation**: Percentage of sugars consumed. (OG - FG)/(OG - 1) × 100. Typical ale: 70-80%. High attenuation = dry beer. Low attenuation = sweet, full-bodied.

## References

- [Food Fermentation](fermentation.md) — broader fermentation biology, lactic acid fermentation
- [Food Preservation](preservation.md) — vinegar as preservative, pasteurization
- [Grain Milling](milling.md) — malt crushing for mashing
- [Dairy Processing](dairy.md) — pasteurization of milk and dairy products
- [Chemistry: Fermentation](../chemistry/fermentation.md) — industrial ethanol, solvent fermentation
- [Ceramics](../ceramics/index.md) — fermentation vessels, storage amphorae
- [Energy](../energy/index.md) — heat for mashing, boiling, distillation
- [Health & Sanitation](../health/sanitation.md) — microbiology, food safety

---

*Part of the [Bootciv Tech Tree](../index.md) • [Food Processing](./index.md) • [All Domains](../index.md)*
