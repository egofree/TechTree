# Dairy Processing

> **Node ID**: food-processing.dairy
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: `ceramics`, [`health.sanitation`](../health/sanitation.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 0-20
> **Outputs**: butter, cheese, cream, yogurt, whey, ghee

## Overview

Dairy processing converts raw milk — one of the most perishable foods (spoils in 4-6 hours at room temperature) — into stable, protein-rich products with shelf lives measured in weeks to months. A single dairy cow produces 15-25 liters of milk per day. Without processing, this bounty rots within hours. With processing, it becomes butter (weeks), cheese (months), or ghee (years). Cheese is perhaps the most calorie-efficient preservation method: 10 liters of milk (34 MJ) yields ~1 kg cheese (17 MJ) with months of shelf life and no refrigeration required.

Dairy depends on [ceramics](../ceramics/index.md) for storage vessels and cheese molds, [health.sanitation](../health/index.md) for hygiene protocols, and [foundations.food-agriculture](../foundations/food-agriculture.md) for animal domestication and management.

## Bill of Materials

### Cheese Making Materials

| Material | Quantity per 10 kg cheese | Source | Alternatives |
|----------|:------------------------:|--------|-------------|
| Whole milk | 100-120 L (cow) | [Agriculture](../foundations/food-agriculture.md) | Goat milk (8-10 L/kg), sheep milk (6-8 L/kg) |
| Starter culture (Lactococcus) | 1-2 L or 50-100 g freeze-dried | Propagated from previous batch | Buttermilk (1-2% addition) |
| Rennet (animal) | 5-10 mL liquid or 1 tablet | Calf stomach extract | Vegetable rennet (cardoon thistle, fig sap) |
| Salt (NaCl) | 150-250 g (1.5-2.5% of cheese) | [Mining](../mining/index.md) | Sea salt; non-iodized preferred |
| Calcium chloride (CaCl₂) | 10-20 g per 100 L milk | [Chemistry](../chemistry/index.md) | Restores calcium in pasteurized milk |

### Butter Production Materials

| Material | Quantity per 10 kg butter | Source | Alternatives |
|----------|:------------------------:|--------|-------------|
| Whole milk | 200-220 L (4% fat) | [Agriculture](../foundations/food-agriculture.md) | Cream separated first: 25-30 L cream per 10 kg butter |
| Salt (optional) | 100-200 g (1-2%) | [Mining](../mining/index.md) | Unsalted butter (shorter shelf life) |
| Cold water (washing) | 30-50 L | [Water](../water/index.md) | Must be potable, 5-10°C |

## Process Description

### Milk Composition

Understanding milk composition is essential for all dairy processing:

| Component | Content (cow's milk) | Role |
|-----------|:--------------------:|------|
| Water | 87-88% | Carrier medium |
| Fat | 3.5-4.5% | Cream, butter source |
| Protein (casein) | 2.5-3.0% | Cheese curd former |
| Protein (whey) | 0.5-0.7% | Byproduct, nutritious |
| Lactose | 4.5-5.0% | Sugar, fermentation substrate |
| Minerals | 0.7-0.8% | Calcium, phosphorus |
| Total solids | 12-13% | Everything except water |

### Cream Separation

The first step in most dairy processing. Fat globules (1-10 μm diameter) are lighter than the milk serum and rise naturally, but slowly.

**Gravity separation**: Let milk stand undisturbed 12-24 hours at 5-10°C. Fat globules rise to form a cream layer. Skim cream off the top. Cream yield: 10-15% of milk volume. Fat content: 20-35%.

**Mechanical separation** (cream separator, Years 10-20): Centrifugal separator spinning at 5,000-10,000 RPM. Milk enters near the center, cream (lighter) flows inward and up, skim milk (heavier) flows outward and down. Separation in seconds rather than hours. Gustaf de Laval's 1878 separator design:

- **Bowl diameter**: 100-200 mm
- **Speed**: 6,000-8,000 RPM
- **Throughput**: 100-500 liters/hour (hand-cranked) to 5,000+ L/h (motorized)
- **Cream fat content**: Adjustable by regulating cream outlet: 20-50% fat
- **Skim milk fat content**: <0.1% (vs. 0.5-1.0% from gravity separation)
- **Materials**: Bowl is stainless steel or tinned copper. Precision machining required for balance at high RPM.

### Butter Production

Butter is 80-82% milk fat, 15-16% water, 1-2% milk solids, and 1-2% salt (if salted).

**Churning process**:
1. **Cream ripening**: Hold cream at 16-18°C for 6-12 hours to develop flavor (lactic bacteria produce diacetyl). For sweet butter, skip this step and keep cream at 5°C.
2. **Churning temperature**: 8-12°C in summer, 12-15°C in winter. Temperature critical — too warm produces soft butter, too cold prevents fat aggregation.
3. **Churning**: Agitate cream until fat globules rupture and aggregate into butter grains. Takes 20-45 minutes in a dash churn (plunger type) or 10-20 minutes in a barrel churn (rotating). Volume of cream: 30-40% of churn capacity for proper agitation.
4. **Butter grains form**: Visible when butter granules reach pea-to-walnut size. Buttermilk separates and can be drained off (drinkable or for baking).
5. **Washing**: Rinse butter grains with cold water (2-3× the volume of butter) to remove residual buttermilk. Reduces spoilage.
6. **Working (kneading)**: Press and fold butter to consolidate mass and distribute moisture evenly. Moisture content must not exceed 16% (legal standard in most jurisdictions). Add salt at this stage if making salted butter: 1-2% by weight (10-20 g/kg).
7. **Yield**: 22-25 kg butter from 500 kg whole milk (4% fat). Or equivalently, ~5 kg butter per 100 kg milk.

**Clarified butter (ghee)**: Heat butter to 110-120°C until all water evaporates (foaming stops) and milk solids brown and precipitate. Filter through cloth. Shelf life: 6-12 months at room temperature without refrigeration. Ghee is 99.5% fat, no water = no microbial growth. Essential in hot climates where refrigeration is unavailable.

### Cheese Making

Cheese making is controlled coagulation of milk protein (casein) to separate curds (solid) from whey (liquid). The curds are then processed and aged.

**Coagulation methods**:

1. **Acid coagulation**: Add acid (lemon juice, vinegar, lactic acid bacteria) until pH drops to 4.6 (casein isoelectric point). Curds form immediately. Examples: paneer, ricotta, cottage cheese, queso fresco. Simplest method, no special equipment.

2. **Rennet coagulation**: Add rennet enzyme (chymosin) to milk at 30-32°C. Enzyme cleaves κ-casein, causing casein micelles to aggregate. Curds form in 30-60 minutes. Most cheese varieties use rennet.
   - **Animal rennet**: Extracted from calf stomach lining (abomasum). 1 mL rennet coagulates 10-20 L milk. Active at pH 6.0-6.8.
   - **Vegetable rennet**: From cardoon thistle (Cynara cardunculus), fig sap. Less consistent than animal rennet but available without slaughter byproducts.
   - **Microbial rennet**: From Rhizomucor miehei or Cryphonectria parasitica. Modern industrial standard but requires biotechnology.

**Basic cheese process (hard cheese like cheddar)**:

1. **Milk preparation**: Heat milk to 30-32°C. Add starter culture (Lactococcus lactis, 1-2% by volume). Ripen 30-60 minutes until pH drops to 6.4-6.5.
2. **Rennet addition**: Add rennet (1 mL per 10 L milk). Stir gently for 1-2 minutes, then stop. Let stand 30-45 minutes until firm curd forms ("clean break" test: knife inserted and lifted should leave a clean cut).
3. **Cutting**: Cut curd into uniform cubes (6-12 mm for hard cheese, 12-25 mm for soft cheese) using wire curd knives. Smaller curds = more whey expelled = harder, drier cheese.
4. **Cooking**: Gradually heat curds and whey to 38-42°C over 30-45 minutes, stirring gently. Heat causes curds to contract (syneresis), expelling whey. Higher temperature = harder cheese.
5. **Draining**: Drain whey through cloth or perforated mold. Whey can be fed to livestock or processed for whey cheese (ricotta).
6. **Pressing**: Weight the curds (1-5 kg weight per kg cheese, depending on variety) for 6-24 hours. Removes remaining whey, consolidates curd mass.
7. **Salting**: Brine bath (18-22% NaCl) for 12-48 hours, or dry salt rubbed on surface. Salt at 1.5-2.5% of cheese weight. Controls microbial growth, enhances flavor, aids rind formation.
8. **Aging (ripening)**: Store at specific temperature and humidity for defined period:

| Cheese Type | Temperature | Humidity | Duration | pH |
|------------|:-----------:|:--------:|:--------:|:--:|
| Fresh (ricotta, cottage) | 4°C | N/A | 0-7 days | 4.5-5.0 |
| Soft (Camembert, Brie) | 10-13°C | 85-90% | 2-6 weeks | 4.6-5.2 |
| Semi-hard (Gouda, Edam) | 12-15°C | 80-85% | 2-6 months | 5.0-5.4 |
| Hard (Cheddar, Swiss) | 8-12°C | 85-90% | 3-18 months | 5.0-5.5 |
| Very hard (Parmesan) | 10-14°C | 80-85% | 12-36 months | 5.2-5.5 |

**Yield**: 10 kg cheese from 100 kg milk (10:1 ratio for hard cheese). 6-8 kg from 100 kg for soft cheese (higher moisture).

### Yogurt and Fermented Dairy

**Yogurt**: Heat milk to 85°C for 30 minutes (denatures whey proteins for thicker texture). Cool to 42-45°C. Inoculate with 2-3% starter culture (Lactobacillus delbrueckii subsp. bulgaricus + Streptococcus thermophilus). Incubate at 42°C for 4-6 hours until pH reaches 4.4-4.6. Cool immediately to 4°C. Shelf life: 2-3 weeks refrigerated.

**Kefir**: Add kefir grains (symbiotic culture of LAB + yeast) to milk at 22°C. Ferment 18-24 hours. Produces slightly carbonated, tangy drink. Shelf life: 1-2 weeks refrigerated.

## Quantitative Parameters

### Dairy Product Yields per 100 L Milk

| Product | Yield (kg or L) | Milk Required (L/kg) | Shelf Life | Key Parameter |
|---------|:---------------:|:--------------------:|:----------:|:-------------:|
| Butter | 4.5-5.5 kg | 18-22 L/kg | 2-4 weeks (refrigerated) | Fat content ≥80% |
| Ghee | 3.5-4.5 kg | 22-28 L/kg | 6-12 months (room temp) | Fat content ≥99.5% |
| Hard cheese (cheddar) | 8-10 kg | 10-12 L/kg | 3-18 months | Moisture 35-39% |
| Soft cheese (Brie) | 10-14 kg | 7-10 L/kg | 2-6 weeks | Moisture 50-60% |
| Fresh cheese (ricotta) | 12-16 kg | 6-8 L/kg | 0-7 days | Moisture 70-80% |
| Yogurt | 90-95 L | 1.05-1.1 L/L | 2-3 weeks (refrigerated) | pH 4.4-4.6 |
| Cream (35% fat) | 10-15 L | — | 5-7 days (refrigerated) | Fat 35-40% |

### Dairy Animal Productivity

| Animal | Milk (L/day) | Butterfat % | Season | Key Traits |
|--------|:-----------:|:----------:|:------:|-----------|
| Dairy cow | 20-30 | 3.5-4.5 | Year-round | Highest volume, industrial standard |
| Goat | 2-4 | 3.5-4.5 | Seasonal (8-10 mo) | Hardy, browse-fed, small scale |
| Sheep | 1-3 | 6-8 | Seasonal (6-8 mo) | High fat, excellent for cheese |
| Water buffalo | 8-15 | 7-9 | Year-round | Premium mozzarella, tropical climates |
| Yak | 1-3 | 5-7 | Seasonal | High altitude, cold climates |
| Camel | 5-10 | 2.5-5.5 | Year-round | Arid regions, drought-resistant |

### Milk Spoilage Rates by Temperature

| Temperature | Time to Souring | Dominant Spoilage | Preventive Action |
|:-----------:|:--------------:|:-----------------:|:-----------------:|
| 37°C (body temp) | 4-6 hours | Lactic acid bacteria | Immediate processing or cooling |
| 25°C (room temp) | 8-12 hours | Mesophilic bacteria | Process within 2 hours |
| 15°C | 18-24 hours | Psychrotrophic bacteria | Cool to 4°C within 4 hours |
| 4°C (refrigerated) | 5-7 days | Pseudomonas, Listeria | Pasteurize for longer storage |
| -18°C (frozen) | 6-12 months | Enzymatic (lipolysis) | Limit to 6 months for quality |

### Nutritional Comparison of Dairy Products

| Product | Energy (kcal/100 g) | Protein (g/100 g) | Fat (g/100 g) | Calcium (mg/100 g) |
|---------|:-------------------:|:------------------:|:-------------:|:------------------:|
| Whole milk | 60-65 | 3.2-3.5 | 3.5-4.0 | 110-120 |
| Butter | 716-720 | 0.5-1.0 | 80-82 | 15-20 |
| Ghee | 890-900 | 0.0-0.5 | 99.5 | 0 |
| Cheddar cheese | 400-420 | 24-26 | 32-35 | 720-760 |
| Parmesan | 420-440 | 35-38 | 25-29 | 1100-1200 |
| Yogurt (plain) | 60-65 | 3.5-4.5 | 1.5-3.5 | 110-130 |
| Whey | 25-30 | 0.8-1.0 | 0.2-0.5 | 40-50 |

## Scaling Notes

- **Household dairy** (1-5 L milk/day): Hand milking, gravity cream separation, small churn or jar shaking for butter, simple acid coagulation for fresh cheese. No specialized equipment. Labor: 1-2 hours daily.
- **Village dairy** (50-200 L milk/day): Hand or simple mechanical milking, small cream separator (hand-cranked, 100-200 L/h), barrel churn (20-50 L), cheese press, aging cave or cellar. 1-2 workers. Throughput: 5-20 kg cheese/day, 2-5 kg butter/day.
- **Industrial dairy** (5,000-50,000+ L milk/day): Mechanical milking pipeline, industrial centrifugal separator, continuous butter maker (500-5000 kg/h), automated cheese vats (10,000-50,000 L), mechanical press, climate-controlled aging rooms. 10-50 workers. Throughput: 500-5000 kg cheese/day.
- **Cold chain requirement**: Milk must be cooled from 37°C (body temperature) to 4°C within 2 hours of milking. Each hour of delay at ambient temperature reduces cheese yield by 0.5-1.0% due to bacterial growth consuming lactose. Industrial dairies use plate heat exchangers for rapid cooling; village dairies use water baths or cool cellars.
- **Whey utilization**: Cheese making produces 80-90 L whey per 10 kg cheese. Whey contains 0.8% protein and 5% lactose — nutritious but perishable (spoils in 12-24 hours at room temperature). Feed to livestock immediately, or process into ricotta (heat to 80°C, pH to 5.5, collect precipitated proteins). Industrial dairies produce whey protein concentrate (35-80% protein) by ultrafiltration.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Cheese curd won't set | Rennet inactive, milk too hot/cold, calcium deficiency | Check milk temperature (30-32°C). Use fresh rennet. Add CaCl₂ (10-20 g/100 L) if milk is pasteurized |
| Cheese tastes bitter | Excess rennet, proteolysis from contaminant bacteria, over-aging | Reduce rennet to 1 mL/10 L. Improve sanitation. Age at correct temperature |
| Butter won't form (cream won't break) | Cream too cold or too warm, wrong fat content, over-agitation | Adjust to 8-12°C. Cream should be 30-35% fat. Stop when grains are pea-sized |
| Butter too soft/wet | Insufficient washing, excess moisture, temperature too high during working | Wash 2-3× with cold water. Work until moisture <16%. Keep below 15°C during working |
| Yogurt too thin | Insufficient incubation time, wrong temperature, low solids milk | Incubate at 42°C until pH 4.4-4.6 (4-6 hours). Add milk powder (2-3%) to increase solids |
| Yogurt too sour | Over-fermentation (pH below 4.0), incubation too long | Cool to 4°C immediately at pH 4.4-4.6. Reduce incubation time |
| Ghee smokes excessively | Temperature too high, residual buttermilk solids | Keep below 120°C. Ensure butter is well-washed before clarifying. Filter through fine cloth |
| Milk off-flavors | Feed taints (onion, weed), lipase action (raw milk), oxidation | Control cattle feed. Pasteurize within 2 hours. Store in opaque containers |
| Cheese swelling (gas holes) | Coliform or yeast contamination producing CO₂ | Improve sanitation. Use pasteurized milk. Ensure proper starter culture activity |
| Mold on cheese surface (unintended) | High humidity, poor air circulation, contaminated aging environment | Maintain correct humidity per cheese type. Increase air flow. Wipe with brine-soaked cloth |

## Safety

- **Pasteurization**: Raw milk carries Brucella, Listeria, E. coli O157:H7, Salmonella, and Campylobacter. All milk for cheese/dairy should be pasteurized (72°C/15 sec) unless making raw milk cheese with strict controls (aged 60+ days at >4°C allows acid/enzymes to destroy most pathogens).
- **Listeria risk**: Soft cheeses (Camembert, Brie) have neutral pH on surface during ripening, allowing Listeria monocytogenes growth. Strict sanitation of aging caves and equipment required. Listeria grows at refrigerator temperatures (1-4°C) — it is psychrotrophic.
- **Brucellosis**: Raw milk from infected cattle transmits Brucella. Causes chronic undulant fever in humans. Pasteurization destroys Brucella. In regions without brucellosis eradication programs, raw milk dairy products are dangerous.
- **Aflatoxin M1**: Carcinogenic metabolite of Aspergillus flavus, secreted in milk when cattle eat moldy feed. Cannot be destroyed by pasteurization. Prevent by controlling cattle feed quality. Regulatory limit: 0.5 μg/L in most jurisdictions.
- **Cream separator safety**: Centrifugal separators at 6,000-8,000 RPM contain significant rotational energy. Imbalance causes destructive vibration. Never open a spinning separator bowl. Ensure locking mechanism is engaged before starting.

## Quality Control

### Dairy Equipment Construction

The key pieces of dairy processing equipment and their construction:

**Cream separator** (industrial era):
- **Bowl**: Stainless steel or tinned copper. Spinning at 6,000-8,000 RPM requires dynamic balancing to within 0.01 mm. Imbalance causes destructive vibration. Bowl design: stack of conical discs (0.5-1.0 mm gap) creates large surface area for efficient separation.
- **Drive**: Hand-cranked (via step-up gear) or electric motor with belt drive. Power: 100-500 W for small units, 1-5 kW for industrial. Bearings must handle high radial loads from centrifugal forces.
- **Sanitation**: All milk-contact surfaces must be smooth (Ra <0.8 μm), non-porous, and cleanable. CIP (Clean-In-Place) system: circulate hot caustic (1-2% NaOH at 70°C for 15 min), rinse, circulate acid (0.5-1% phosphoric or nitric at 60°C for 10 min), rinse, sanitize (200 ppm chlorine or 25 ppm peracetic acid).

**Cheese press**:
- **Design**: Wooden or steel frame with threaded rod and follower plate. Pressure applied via lever weight or screw mechanism. Pressure range: 0.5-5 kg per kg cheese.
- **Cheese molds (hoops)**: Traditionally ceramic or woven reed baskets. Industrial: perforated stainless steel or food-grade plastic. Perforations allow whey drainage while containing curds.

**Butter churn**:
- **Barrel churn**: Wooden (oak, ash) or stainless steel barrel with internal paddles or mounted on pivots for tumbling action. Capacity: 20-500 L. Wood preferred for small-scale — naturally insulating and slightly porous (maintains temperature stability).
- **Dash churn**: Plunger type — wooden dasher with cross-holes agitates cream in tall narrow vessel. Oldest design, labor-intensive but effective.
- **Continuous butter maker** (industrial): Forced cream through high-shear zone at controlled temperature. Produces butter continuously at 500-5000 kg/hour. Requires precise temperature control and cream quality.

### Cheese Ripening Science

The transformation of fresh curd into aged cheese involves complex biochemical changes:

- **Proteolysis**: Casein proteins are broken down by residual rennet, plasmin (native milk enzyme), and bacterial enzymes. Large proteins → peptides → free amino acids. Amino acids contribute savory (umami) flavors. Extent measured by pH 4.6 soluble nitrogen as percentage of total nitrogen: fresh cheese <5%, aged cheddar 20-35%, parmesan 35-50%.
- **Lipolysis**: Milk fat (triglycerides) hydrolyzed by lipase enzymes to free fatty acids. Short-chain fatty acids (butyric C4, caproic C6, caprylic C8) give sharp, pungent flavors characteristic of aged cheese. Controlled lipolysis essential — too much = rancid.
- **Texture development**: Calcium phosphate dissolution during aging softens the protein matrix. Moisture loss (1-2% per month) firms the paste. Proteolysis breaks the casein network, changing from elastic (young cheese) to crumbly (aged cheddar) to crystalline (parmesan). Tyrosine crystals in parmesan are visible amino acid crystals — a sign of extensive proteolysis, not a defect.
- **Rind formation**: Surface drying creates a protective rind. Natural rind: simply air-dried. Washed rind: brine-washed periodically (promotes Brevibacterium linens growth — orange, pungent). White mold rind: Penicillium camemberti (Camembert/Brie) — the mold creates a soft, gooey interior by breaking down proteins from outside in.

## References

- [Ceramics](../ceramics/index.md) — storage vessels, cheese molds, butter churns
- [Health & Sanitation](../health/index.md) — hygiene protocols, germ theory for safe milk handling
- [Foundations: Food & Agriculture](../foundations/food-agriculture.md) — animal domestication and dairy animal management
- [Food Preservation](preservation.md) — fermented dairy as preservation method
- [Food Fermentation](fermentation.md) — lactic acid fermentation biology
- [Energy](../energy/index.md) — mechanical power for cream separators, cooling for storage
- [Metals](../metals/index.md) — stainless steel for dairy equipment, tin for separator bowls

---

*Part of the [Bootciv Tech Tree](../index.md) • [Food Processing](./index.md) • [All Domains](../index.md)*
