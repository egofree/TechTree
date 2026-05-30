# Food Fermentation

> **Node ID**: food-processing.fermentation
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: [`ceramics`](../ceramics/index.md), [`health.sanitation`](../health/sanitation.md), [`food-processing.milling`](milling.md)
> **Enables**: [`food-processing.brewing`](brewing.md), [`food-processing.preservation`](preservation.md)
> **Timeline**: Years 0-15
> **Outputs**: sourdough_bread, sauerkraut, kimchi, soy_sauce, miso, tempeh, pickles, vinegar
> **Critical**: No — fermentation enhances nutrition and preservation but other methods can substitute


Food fermentation is the controlled cultivation of microorganisms — lactic acid bacteria, yeasts, molds, and acetic acid bacteria — to transform raw foods into more stable, nutritious, and digestible products. Unlike the alcoholic fermentation covered in [Brewing & Distilling](brewing.md), food fermentation focuses on non-alcoholic transformations: vegetables into sauerkraut and kimchi, soybeans into soy sauce and tempeh, milk into yogurt and cheese (see [Dairy Processing](dairy.md)), and flour into sourdough bread.

Fermentation is the earliest biotechnology. Every human civilization independently developed fermented foods. The process preserves food by producing acids that lower pH below 4.6 (the threshold where *Clostridium botulinum* cannot grow), produces B vitamins and bioavailable minerals, breaks down anti-nutritional factors (phytic acid, trypsin inhibitors), and creates novel flavors that improve palatability of monotonous diets.

For industrial ethanol and solvent fermentation, see [Chemistry: Fermentation](../chemistry/fermentation.md). For beer and wine, see [Brewing & Distilling](brewing.md).


## Materials

- **Salt (NaCl)**: 2-3% concentration for vegetable fermentation; 12-18% for soy sauce brine. Non-iodized salt preferred — iodine inhibits lactic acid bacteria. Source: [Mining](../mining/processing.md) or solar evaporation of seawater.
- **Water**: Clean, chlorine-free. Chlorine in municipal water kills lactic acid bacteria. Remove by boiling and cooling, or by leaving uncovered for 24 hours. Source: [Water Supply](../water/basic-treatment.md).
- **Starter cultures**: Wild (from environment), backslopped (from previous batch), or commercial freeze-dried. Sourdough starter takes 5-7 days to establish from flour and water.
- **Grain**: Wheat, rye, or other flour for sourdough. Source: [Grain Milling](milling.md).
- **Vegetables**: Cabbage, radish, cucumber, carrot, and other produce. Source: [Agriculture](../foundations/food-agriculture.md).
- **Soybeans**: For soy sauce, miso, tempeh, natto. Source: [Agriculture](../foundations/food-agriculture.md).

## Tools and Equipment

- **Fermentation vessels**: Ceramic crocks (glazed or unglazed), glass jars, wooden barrels. Must be non-reactive — no bare iron, copper, or aluminum (metals leach into acidic ferment). Source: [Ceramics](../ceramics/index.md).
- **Weights**: To submerge vegetables under brine. Glass disks, boiled stones, or food-grade plastic bags filled with brine.
- **Airlocks**: One-way valves that allow CO₂ to escape while preventing oxygen entry. Essential for anaerobic vegetable fermentation. Simple water airlock: inverted jar in water trough.
- **Thermometer**: Range -10°C to 100°C, accuracy ±1°C. Fermentation temperature control is critical for consistent results.
- **pH meter or strips**: Range 2.0-7.0, accuracy ±0.2. Target pH <4.6 for safety confirmation.

## Knowledge

- Understanding of anaerobic vs. aerobic conditions and their effect on microbial selection
- Ability to identify contamination by sight (mold colors, texture changes) and smell (putrid, acetone, solvent odors)
- Basic grasp of pH measurement and interpretation

## Bill of Materials

| Material | Quantity per kg output | Source | Alternatives |
|----------|:----------------------:|--------|-------------|
| Cabbage | 1.1-1.3 kg | [Agriculture](../foundations/food-agriculture.md) — fresh, compact heads | Other cruciferous vegetables (radish, turnip) |
| Salt (NaCl) | 20-30 g per kg cabbage | [Mining](../mining/processing.md) — non-iodized | Sea salt; avoid iodized (inhibits LAB) |
| Water (chlorine-free) | As needed for brine | [Water](../water/index.md) | Boiled and cooled tap water |
| Soybeans (dry) | 0.8-1.0 kg per kg miso | [Agriculture](../foundations/food-agriculture.md) | Chickpeas for alternative miso |
| Koji mold (*Aspergillus oryzae*) | 1-5 g per kg substrate | Commercial starter or propagated from rice | Cannot substitute — defines the product |
| Wheat flour | 1.0-1.2 kg per kg sourdough starter | [Grain Milling](milling.md) | Rye flour (more active fermentation) |
| Sea salt (coarse) | 150-250 g per L soy sauce | [Mining](../mining/processing.md) | Rock salt, solar salt |
| Ceramic crocks (5-20 L) | 1 per batch | [Ceramics](../ceramics/index.md) | Glass jars, wooden barrels |


## Sourdough Bread

Sourdough uses wild yeast (*Saccharomyces exiguus*, *Candida milleri*) and lactic acid bacteria (*Lactobacillus sanfranciscensis*, *L. brevis*) maintained in a flour-water culture called a starter or levain.

**Starter establishment** (5-7 days):

1. Mix 50 g whole-grain flour (rye or whole wheat) with 50 g warm water (30°C) in a clean jar. Cover loosely with cloth.
2. Stir vigorously twice daily to incorporate wild yeast from the flour and air.
3. **Day 2**: Discard 80 g of the mixture. Add 50 g flour + 50 g water. This "feeding" provides fresh food for growing microorganisms.
4. **Days 3-7**: Repeat discard-and-feed daily. By day 3-4, mixture will bubble and rise within 4-6 hours of feeding — the culture is active. By day 5-7, it should double in volume within 4-6 hours.
5. **Viability test**: Drop a spoonful of starter into a glass of water. If it floats, it has sufficient gas production for leavening.

**Sourdough bread production**:

1. **Levain build**: Mix 20 g starter with 100 g flour + 100 g water. Ferment 8-12 hours at 22-25°C until doubled.
2. **Dough mixing**: Combine 300 g levain, 700 g flour, 450 g water (72% hydration), and 18 g salt. Mix until no dry flour remains. Rest 30 minutes (autolyse).
3. **Stretch and fold**: Every 30 minutes for 2 hours (4 sets), stretch one side of the dough up and fold over. This develops gluten without mechanical mixing.
4. **Bulk fermentation**: 4-8 hours at 24-26°C until dough has risen 50-75% and shows visible bubbles. Temperature controls speed: 24°C = 6-8 hours, 28°C = 3-4 hours.
5. **Shaping**: Gently shape dough into boule (round) or batard (oval). Place seam-side up in floured proofing basket (banneton).
6. **Cold retard**: Refrigerate 8-16 hours at 4°C. Slows fermentation, develops complex flavors (acetic acid production increases at low temperature).
7. **Baking**: Preheat oven with dutch oven or baking stone to 250°C. Score dough surface (5-10 mm deep cuts allow controlled expansion). Bake covered 20 minutes (steam trapped creates crust), then uncovered 20-25 minutes at 230°C. Internal temperature target: 95-98°C.
8. **Cooling**: Rest on wire rack minimum 1 hour before cutting. Cutting hot bread compresses crumb and makes it gummy.

**Strengths**:
- Sourdough starter is self-perpetuating: once established from flour and water, it can be maintained indefinitely with daily feeding
- Wild yeast + LAB combination lowers pH to 3.8-4.5, providing natural preservation extending bread shelf life to 4-7 days vs. 1-2 days for commercial yeast bread
- Long cold fermentation (8-16 hours at 4°C) develops complex flavor compounds (acetic acid, lactic acid) without any added ingredients

**Weaknesses**:
- Starter establishment takes 5-7 days of daily feeding, consuming 100 g flour per day before any bread is produced
- Sourdough timing is temperature-sensitive: ±3°C changes fermentation speed by 50%, making consistent results difficult without temperature control
- High-humidity doughs (72%+ hydration) are sticky and difficult to handle — require practiced technique and well-floured surfaces

## Vegetable Fermentation (Sauerkraut)

1. **Selection**: Fresh, compact cabbage heads. Outer leaves removed. Core retained — highest lactobacillus population.
2. **Shredding**: Slice cabbage 1-3 mm thick using knife or mandoline. Thinner = faster fermentation, softer texture. Thicker = crunchier.
3. **Salting**: Add 20-25 g salt per kg shredded cabbage (2.0-2.5%). Massage salt into cabbage with hands for 5-10 minutes until liquid releases and cabbage volume reduces by ~30%. The salt draws water from cabbage cells via osmosis, creating the brine.
4. **Packing**: Pack salted cabbage tightly into fermentation vessel. Press down firmly to eliminate air pockets. Leave 5-8 cm headspace.
5. **Submersion**: Place weight (ceramic disk, boiled stone) on top of cabbage to keep it below brine level. All cabbage must be submerged — exposed cabbage molds rapidly.
6. **Sealing**: Cover with lid and airlock, or cloth tied tightly. If using cloth, check daily for Kahm yeast (white film, harmless but remove it) and mold (colored, fuzzy, discard affected area).
7. **Fermentation temperature**: 18-22°C is optimal. Below 15°C: fermentation stalls. Above 25°C: rapid but mushy texture and off-flavors.
8. **Timeline by temperature**:
   - 18-20°C: 3-4 weeks for full flavor development
   - 20-22°C: 2-3 weeks
   - 22-25°C: 1-2 weeks (less complex flavor)
9. **pH target**: Below 4.0 for full preservation. Check with pH strips after 5-7 days.
10. **Storage**: Once desired flavor reached, move to cool storage (4-10°C). Fermentation slows dramatically but continues. Shelf life: 6-12 months in cool conditions.

**Strengths**:
- Sauerkraut preserves cabbage for 6-12 months with only salt (2-2.5%) and an anaerobic vessel — no heat, no energy, no specialized equipment
- Fermentation produces B vitamins (B12, folate) and breaks down phytic acid, increasing mineral bioavailability vs. raw cabbage
- LAB succession (Leuconostoc → Lactobacillus → Pediococcus) is self-organizing: no starter culture needed, just salt and anaerobic conditions

**Weaknesses**:
- Exposed cabbage (not submerged in brine) molds within 24-48 hours — submersion must be verified daily during the first week
- Temperature above 25°C produces mushy texture and off-flavors from rapid fermentation; below 15°C fermentation stalls
- High sodium content (600-1,500 mg per 100 g) is a health concern for workers with hypertension

## Kimchi

Korean-style fermented vegetables, typically napa cabbage and Korean radish with chili, garlic, ginger, and fermented seafood:

1. **Brining**: Quarter napa cabbage, salt between leaves with coarse salt (5-6% by weight). Rest 2-4 hours, turning every 30 minutes, until leaves are flexible and wilted. Rinse 3 times to remove excess salt.
2. **Seasoning paste**: Mix gochugaru (Korean chili flakes, 30-50 g per cabbage), garlic (20-30 g), ginger (10-15 g), sugar (10-15 g), and fermented shrimp or fish sauce (15-30 mL). Add rice porridge (cooked rice blended with water) as binder.
3. **Stuffing**: Rub seasoning paste between each cabbage leaf, coating evenly.
4. **Packing**: Pack into fermentation vessel, pressing tightly. Seal.
5. **Fermentation**: 18-22°C for 1-3 days (quick ferment), or 4-10°C for 2-4 weeks (slow, more complex). Kimchi is traditionally fermented in onggi (unglazed clay vessels) which allow slight gas exchange.
6. **Storage**: Refrigerate at 0-4°C after initial fermentation. Continues to slowly age and sour over months.

**Strengths**:
- Kimchi fermentation produces a complex flavor profile (spicy, sour, umami) from simple ingredients — cabbage, salt, chili, garlic, and fish sauce
- The Korean onggi (unglazed clay vessel) allows slight gas exchange, preventing pressure buildup while maintaining anaerobic conditions
- Fast fermentation (1-3 days at 18-22°C) enables rapid turnaround from raw ingredients to preserved food

**Weaknesses**:
- Requires multiple specialty ingredients (gochugaru chili, fermented shrimp) that may not be available outside Korean agricultural traditions
- Seasoning paste must coat every leaf individually — labor-intensive process requiring 20-40 minutes per cabbage head
- Carbon dioxide from fermentation builds pressure in sealed containers; glass jars can crack if not vented

## Soy Sauce (Shoyu)

Soy sauce production is a two-stage fermentation spanning 6-18 months:

**Stage 1: Koji production** (2-3 days):

1. **Substrate preparation**: Soak soybeans 12-18 hours until doubled in size. Steam at 120°C for 30-45 minutes or boil 3-4 hours until soft. Roast wheat, crush coarsely. Mix soybeans and wheat at 1:1 ratio by weight.
2. **Inoculation**: Cool substrate to 30-35°C. Sprinkle *Aspergillus oryzae* spores (koji-kin) at 0.1-0.5% by weight. Mix thoroughly.
3. **Incubation**: Spread on trays 3-5 cm deep. Maintain 30°C, 90-95% humidity for 40-48 hours. Stir at 12 and 24 hours to distribute heat and mycelium. Koji is ready when substrate is covered in white mycelium and smells sweet-fruity. Internal temperature must not exceed 40°C or mold dies — monitor closely.

**Stage 2: Moromi fermentation** (6-18 months):

4. **Brine mixing**: Mix finished koji with 18-22% salt brine (by weight of water). Ratio: 1.2-1.4 kg koji per L brine. The resulting mash is called moromi.
5. **Fermentation**: Transfer moromi to large fermentation tanks. Stir (mix) the moromi 2-3 times per week for the first month, then 1-2 times per week thereafter. Stirring incorporates air needed by the yeast and acetic acid bacteria.
6. **Microbial succession**: Lactic acid bacteria dominate first 1-3 months (lower pH to 4.7-5.0). Yeast (*Zygosaccharomyces rouxii*) produces ethanol over months 2-6. Further aging develops 300+ flavor compounds.
7. **Duration**: Minimum 6 months for basic soy sauce. Premium soy sauce ferments 12-18 months. Some artisanal soy sauces ferment 2-3 years.
8. **Pressing**: Press moromi through cloth bags in a screw press or hydraulic press at 50-100 kg/cm². Raw soy sauce (nama-shoyu) is collected. Yield: 50-60% of moromi weight as raw soy sauce.
9. **Pasteurization**: Heat to 70-80°C for 15-30 minutes. Kills residual microorganisms, stabilizes color and flavor, denatures enzymes.
10. **Settling and bottling**: Sediment settles 1-2 weeks. Decant clear soy sauce. Bottle in sterilized containers.

**Strengths**:
- Soy sauce production converts inexpensive soybeans and wheat into a high-value condiment with 300+ flavor compounds developed through months of fermentation
- Koji mold (Aspergillus oryzae) produces enzymes that break down proteins into amino acids (umami) and starches into sugars — no external enzymes needed
- Moromi fermentation preserves food through 16-18% salt brine — shelf-stable without refrigeration

**Weaknesses**:
- Minimum 6-month fermentation time ties up vessels and storage space — 12-18 months for premium quality
- Koji incubation temperature must stay below 40°C or the mold dies — requires daily monitoring and active cooling in hot climates
- Pressing moromi at 50-100 kg/cm² requires a heavy-duty screw press or hydraulic press — not achievable with simple wooden presses

## Tempeh

Tempeh is fermented soybean cake from Indonesia, produced by *Rhizopus oligosporus* mold:

1. **Soybean preparation**: Soak soybeans 12-18 hours. Dehull by rubbing between hands or passing through coarse screen (hulls float off). Boil dehulled beans 30-45 minutes until tender but not mushy. Drain and cool to 35-40°C. Surface moisture must be removed — spread on clean cloth and pat dry.
2. **Acidification**: Add vinegar (1-2 tablespoons per kg beans) to lower pH to 4.5-5.0. Acidification prevents bacterial contamination during the long, warm fermentation.
3. **Inoculation**: Sprinkle *Rhizopus oligosporus* spores at 1-3 g per kg cooked beans. Mix thoroughly.
4. **Packing**: Pack inoculated beans into banana leaves, plastic bags with perforations, or shallow trays. Thickness: 2-3 cm. Perforations allow gas exchange — *Rhizopus* requires oxygen.
5. **Incubation**: 30-32°C for 24-48 hours. Maintain humidity 80-90%. Mycelium knits beans into a solid cake. Temperature must stay below 38°C — the mold dies above this threshold.
6. **Harvest**: Tempeh is ready when the cake is firm, white throughout, and beans are bound into a coherent mass. Fresh tempeh keeps 3-5 days refrigerated, 6+ months frozen.

**Strengths**:
- Tempeh fermentation (24-48 hours) is one of the fastest high-protein food processes — converts raw soybeans into a sliceable cake with 19 g protein per 100 g
- Rhizopus mycelium binds individual beans into a solid cake, creating a meat-like texture from plant protein without any binding agent
- The process requires only soybeans, vinegar, and Rhizopus spores — no salt, no specialized vessels, no long aging

**Weaknesses**:
- Temperature must stay below 38°C throughout the 24-48 hour fermentation — Rhizopus dies above this threshold, and spoilage bacteria take over
- Dehulling soybeans is labor-intensive by hand (rub between palms or pass through coarse screen) — commercial dehullers save hours per batch
- Fresh tempeh has only 3-5 days refrigerated shelf life — must be consumed or frozen soon after production


## Fermentation Parameters by Product

| Parameter | Sourdough | Sauerkraut | Soy Sauce | Tempeh | Miso |
|-----------|:---------:|:----------:|:---------:|:------:|:----:|
| Temperature range | 24-28°C | 18-22°C | 15-30°C | 30-32°C | 25-35°C |
| Duration | 4-16 hours | 2-4 weeks | 6-18 months | 24-48 hours | 3-36 months |
| Target pH | 3.8-4.5 | 3.4-3.8 | 4.6-5.0 | 4.5-5.0 | 4.8-5.2 |
| Salt concentration | 1.8-2.2% | 2.0-2.5% | 16-18% (brine) | None | 10-13% |
| Primary organism | *L. sanfranciscensis* | *L. plantarum* | *A. oryzae* + LAB | *R. oligosporus* | *A. oryzae* + LAB |

## Lactic Acid Fermentation Progression (Sauerkraut)

| Day | pH | LAB Population (CFU/g) | Dominant Species | Sensory |
|:---:|:--:|:----------------------:|------------------|---------|
| 0 | 6.2-6.5 | 10³-10⁴ | *Leuconostoc mesenteroides* | Fresh cabbage |
| 2 | 5.0-5.5 | 10⁶-10⁷ | *L. mesenteroides* | Bubbly, slight tang |
| 5 | 4.2-4.6 | 10⁸-10⁹ | *Lactobacillus plantarum* | Tangy, cabbage aroma |
| 10 | 3.8-4.2 | 10⁸-10⁹ | *L. plantarum* | Sour, complex |
| 21 | 3.4-3.8 | 10⁷-10⁸ | *L. plantarum*, *L. brevis* | Fully sour |
| 30+ | 3.2-3.6 | 10⁶-10⁷ | *Pediococcus* species | Very sour, soft |

## Sourdough Hydration and Flour Ratios

| Hydration % | Dough Character | Crumb Structure | Handling Difficulty | Typical Use |
|:-----------:|:---------------:|:---------------:|:-------------------:|:-----------:|
| 60-65% | Stiff, easy to shape | Tight, even | Easy | Sandwich bread |
| 68-72% | Moderate, slightly sticky | Open, irregular | Moderate | Artisan boule |
| 75-82% | Very soft, sticky | Very open, holes | Difficult | Ciabatta, focaccia |
| 85%+ | Batter-like | Extremely open | Very difficult | batter dough, ciabatta, pizza |

## Scaling Notes

- **Household scale** (1-5 kg batches): Hand-processing, ceramic crocks, cloth covers. Sufficient for family food preservation. Labor: 2-4 hours per batch setup, then passive fermentation time.
- **Community scale** (50-200 kg batches): Larger wooden barrels or concrete vats with removable lids. Mechanical cabbage shredder (hand-cranked). Multiple fermentation vessels staged at different stages. Labor: 1-2 people for 4-6 hours per batch.
- **Industrial scale** (1-10 tonnes/day): Stainless steel fermentation tanks with temperature control, pH monitoring, and automated stirring. Mechanized vegetable processing (shredding, salting, packing). Controlled atmosphere rooms. Key scaling challenge: maintaining anaerobic conditions at large volume — air pockets in large batches cause localized spoilage.
- **Soy sauce scaling**: Traditional methods scale linearly — larger tanks, longer aging. Industrial methods use temperature-controlled rooms at 30-35°C to accelerate fermentation to 3-6 months (vs. 12-18 months traditional). Trade-off: faster fermentation produces simpler flavor profile.
- **Temperature control at scale**: Active fermentation of sauerkraut generates ~0.5 kW of heat per tonne of fermenting cabbage from microbial metabolism. In insulated tanks, this heat can raise temperature 5-10°C above ambient, potentially exceeding the safe range. Cooling coils or external heat exchangers are needed for batches over 500 kg in warm climates.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Kahm yeast (white film on surface) | Oxygen exposure, temperature too warm | Remove film with spoon; ferment at lower temperature. Kahm yeast is not harmful but affects flavor |
| Colored mold (green, black, pink) | Oxygen exposure, contaminated equipment | Discard top 2-3 cm of ferment. If mold penetrates deep, discard entire batch. Sanitize vessel before reuse |
| Soft, mushy sauerkraut | Temperature >25°C, insufficient salt, or uneven salt distribution | Ferment below 22°C. Weigh salt precisely. Massage salt thoroughly into cabbage |
| Pink discoloration | Wild yeast (*Rhodotorula*) from too much salt or uneven distribution | Reduce salt to 2-2.5%. Ensure even distribution. Pink color is not toxic but indicates suboptimal conditions |
| Sourdough won't rise | Starter inactive (underfed), temperature too low, or insufficient gluten development | Feed starter 2-3× daily at 25°C for 2 days before baking. Ferment dough at 25-26°C. Use bread flour (>12% protein) |
| Sourdough too sour | Over-fermented bulk fermentation, or too much starter | Reduce bulk fermentation time. Use 15-20% starter (by flour weight) instead of 30%+ |
| Tempeh black spots | *Rhizopus* sporulation from temperature >38°C or too much oxygen | Incubate at 30-32°C. Ensure packaging is not over-perforated. Black spots are not toxic but indicate quality loss |
| Soy sauce not darkening | Insufficient aging time or low temperature | Extend aging. Maintain moromi above 20°C during fermentation |
| Fermentation stalls (pH plateaus) | Low temperature, insufficient salt (for vegetables), or competing organisms | Raise temperature to optimal range. Check salt concentration. Start over if contamination suspected |

## Safety

- **Botulism**: The primary hazard in all anaerobic food preservation. *Clostridium botulinum* produces the most potent biological toxin known (LD₅₀ ~1 ng/kg). It grows in anaerobic, low-acid, moist conditions above 4°C. **Prevention**: Ensure pH drops below 4.6 within 48 hours of starting fermentation. If pH stalls above 4.6 after 48 hours, discard the batch. Use adequate salt (2%+ for vegetables) to suppress undesirable organisms while allowing LAB growth.
- **Mycotoxin risk (soy fermentation)**: *Aspergillus oryzae* (koji mold) is domesticated and safe, but wild *Aspergillus flavus* or *A. parasiticus* can contaminate and produce aflatoxin, a potent liver carcinogen. **Prevention**: Use pure koji starter cultures. Discard any koji with green or black sporulation (signs of wild *Aspergillus*). Maintain cleanliness of koji incubation area.
- **High blood pressure from salt**: Fermented foods are high in sodium (sauerkraut: 600-1500 mg Na per 100 g; soy sauce: 5000-7000 mg Na per 100 mL). Workers with hypertension should moderate intake.
- **Histamine intolerance**: Fermented foods contain high levels of biogenic amines (histamine, tyramine). Symptoms: headache, flushing, gastrointestinal distress. Individuals with diamine oxidase deficiency cannot metabolize histamine efficiently.
- **Hygiene**: All fermentation equipment must be cleaned and sanitized before use. Residue from previous batches can harbor undesirable organisms. Wash vessels with hot soapy water, rinse thoroughly, and sanitize with boiling water or 1% vinegar solution.

## Quality Control

- **pH measurement**: The primary quality metric. Use pH strips (range 2.0-7.0, ±0.2 accuracy) or digital pH meter (±0.01 accuracy). Target pH <4.6 for all fermented foods. Measure at multiple points in the batch — pH may vary between surface and center of large batches.
- **Sensory evaluation**: Normal fermentation smells tangy, acidic, slightly yeasty. Abnormal odors: putrid (rotten egg), solvent-like (acetone), or fecal — these indicate contamination and the batch should be discarded.
- **Texture assessment**: Sauerkraut should remain crisp. Mushy texture indicates over-fermentation or excessive temperature. Tempeh should be firm and sliceable. Soft, crumbly tempeh indicates contamination or insufficient mycelial growth.
- **Microbiological testing** (at scale): Plate counts for total lactic acid bacteria (target: 10⁷-10⁹ CFU/g). Absence of coliforms (<100 CFU/g). Absence of *E. coli* and *Salmonella* in 25 g sample.
- **Salt concentration**: Measure with salometer (brine hydrometer) or by weighing salt. Sauerkraut: 2.0-2.5%. Soy sauce moromi: 16-18% brine. Miso: 10-13%. Variations of ±0.5% are acceptable.

## Variations and Alternatives

| Method | Temperature | Duration | Products | Advantages |
|--------|:-----------:|:--------:|----------|-----------|
| Wild fermentation | Ambient | 1-4 weeks | Sauerkraut, kimchi, pickles | No starter needed, simple |
| Backslopping | Ambient | 3-10 days | Yogurt, sourdough | Fast, consistent, perpetuates culture |
| Koji inoculation | 30°C controlled | 2-3 days + months | Soy sauce, miso, amazake | Complex flavors, unique products |
| Controlled lactic fermentation | 18-22°C | 1-3 weeks | Consistent sauerkraut | Reliable, reproducible |
| Tempeh fermentation | 30-32°C | 24-48 hours | Tempeh | Fast, high-protein product |

**Regional variations**:
- **Germany**: Sauerkraut — cabbage + salt, slow fermented. White wine flavor profile.
- **Korea**: Kimchi — napa cabbage + chili + garlic + fermented seafood. Complex, spicy.
- **Japan**: Miso (soybean + koji + salt, aged 3-36 months), natto (soybeans + *Bacillus subtilis*, sticky, strong flavor).
- **Indonesia**: Tempeh — soybeans + *Rhizopus oligosporus*. Firm cake, nutty flavor.
- **Ethiopia**: Injera — teff flour sourdough fermented 2-3 days. Spongy flatbread.
- **India**: Idli/dosa — rice + black lentil batter, fermented 8-12 hours. Steamed cakes or crepes.

**Low-salt alternatives**: For situations where salt is scarce, reduce salt to 1.5% and rely on starter culture (*Lactobacillus plantarum* at 10⁶ CFU/g) to outcompete undesirable organisms. Risk increases — monitor pH closely.

## See Also

- [Brewing & Distilling](brewing.md) — alcoholic fermentation, distillation chemistry, and yeast biology
- [Food Preservation](preservation.md) — broader preservation methods including fermentation overview
- [Dairy Processing](dairy.md) — yogurt, kefir, and cheese fermentation
- [Grain Milling](milling.md) — flour production, the primary input for sourdough bread
- [Ceramics](../ceramics/index.md) — fermentation vessel construction
- [Chemistry: Fermentation](../chemistry/fermentation.md) — industrial fermentation chemistry, ethanol production
- [Health & Sanitation](../health/sanitation.md) — food safety and hygiene protocols



[← Back to Food Processing](index.md)
