# Nutrition & Dietary Planning

> **Node ID**: health.nutrition
> **Domain**: [Health](./index.md)
> **Dependencies**: [`food-processing.preservation`](../food-processing/preservation.md), [`health.diagnostics`](diagnostics.md)
> **Enables**: [`health.pharmacology`](pharmacology.md), [`health.occupational-health`](occupational-health.md)
> **Timeline**: Years 5-100+
> **Outputs**: nutritional_guidelines, deficiency_prevention_protocols
> **Critical**: No — but deficiency diseases are among the fastest-acting civilization-killers; scurvy incapacitates in 4-8 weeks of vitamin C deprivation

Nutrition science in a bootstrap civilization focuses on the biochemistry of human metabolism: which nutrients are required in what quantities, how to obtain them from available food sources, and how to recognize and treat deficiency diseases before they cripple the workforce. The discipline bridges [food processing](../food-processing/index.md) (which transforms raw materials into edible products) and [diagnostics](diagnostics.md) (which detects deficiency states through physical signs and laboratory tests).

The gap between "eating food" and "eating nutritionally complete food" is deceptively large. A population subsisting on milled white rice, salted meat, and no fresh produce can survive for months while progressively losing the capacity for physical labor to beriberi, scurvy, and anemia. Historical navies lost more sailors to scurvy than to combat; the British Royal Navy's adoption of citrus rations in 1795 was arguably the single most consequential nutritional decision in military history.

## Macronutrients

### Protein

| Parameter | Value | Notes |
|-----------|-------|-------|
| RDA (sedentary adult) | 0.8 g/kg body weight/day | 56 g/day for 70 kg adult |
| RDA (heavy labor) | 1.2-1.6 g/kg/day | 84-112 g/day for 70 kg worker |
| Caloric density | 4 kcal/g | Same as carbohydrate |
| Essential amino acids | 9: histidine, isoleucine, leucine, lysine, methionine, phenylalanine, threonine, tryptophan, valine | Must be obtained from food |

**Sources by completeness**:
- **Complete proteins** (all 9 essential amino acids in adequate ratios): meat, fish, eggs, dairy. Soybeans are the only common plant source with a complete amino acid profile.
- **Complementary plant proteins**: grains + legumes (e.g., rice + beans, wheat + lentils) provide all essential amino acids when combined. The combination need not occur in the same meal — eating both within the same day is sufficient.
- **Protein deficiency (kwashiorkor)**: Edema (fluid retention, particularly distended abdomen), muscle wasting, hair depigmentation, impaired wound healing, immunosuppression. Onset within weeks of severe protein deprivation. Mortality rate untreated: 25-50%. Treatment: reintroduce protein gradually — rapid refeeding causes metabolic crisis.

**Workforce implications**: Manual labor — construction, farming, mining, metalworking — increases protein requirements by 50-100% above sedentary levels. A blacksmith or miner consuming only 0.8 g/kg/day will progressively lose muscle mass and strength over weeks to months.

### Carbohydrates

| Parameter | Value | Notes |
|-----------|-------|-------|
| Recommended minimum | 130 g/day | Brain glucose requirement |
| Typical requirement (heavy labor) | 300-500 g/day | 1,200-2,000 kcal from carbohydrate |
| Caloric density | 4 kcal/g | Primary energy source |
| Glycogen storage | ~400 g total (liver + muscle) | 1,600 kcal reserve — ~1 day of moderate activity |

Carbohydrates provide the primary fuel for physical labor. The body stores limited glycogen; once depleted (after 1-2 days of heavy exertion without adequate intake), fatigue accelerates dramatically. Complex carbohydrates (whole grains, tubers) provide sustained energy release; refined sugars provide rapid but short-lived energy spikes.

**Critical food sources**: Potatoes, rice, wheat, corn, cassava, sweet potatoes. Potatoes are exceptionally efficient — 1 hectare of potatoes yields more usable calories than any other staple crop (~36 million kcal/ha vs. ~14 million for wheat).

### Fats

| Parameter | Value | Notes |
|-----------|-------|-------|
| Recommended intake | 20-35% of total calories | 44-122 g/day for 2,000 kcal diet |
| Caloric density | 9 kcal/g | Most energy-dense macronutrient |
| Essential fatty acids | Linoleic acid (omega-6), alpha-linolenic acid (omega-3) | Must be obtained from food |
| Fat-soluble vitamins | A, D, E, K | Require dietary fat for absorption |

**Sources**: Animal fats (lard, tallow, butter), plant oils (olive, sunflower, flaxseed), nuts and seeds. Fat deficiency is rare when caloric intake is adequate, but essential fatty acid deficiency causes dermatitis, impaired wound healing, and hair loss after several weeks.

**Caloric requirements for physical labor**:

| Activity Level | kcal/day (70 kg adult) | Example |
|----------------|------------------------|---------|
| Sedentary | 1,800-2,200 | Desk work, light tasks |
| Moderate labor | 2,500-3,000 | Farming (mechanized), carpentry |
| Heavy labor | 3,000-3,800 | Mining, blacksmithing, construction, logging |
| Extreme exertion | 3,800-5,000 | Military campaigning, expeditionary work |

A workforce chronically underfed by even 200-300 kcal/day will lose weight, lose strength, and eventually lose the capacity to perform the labor the civilization depends on. This is not theoretical — Napoleon's retreat from Moscow was destroyed more by starvation than by the Russian army.

## Micronutrients

### Vitamin C (Ascorbic Acid)

| Parameter | Value |
|-----------|-------|
| RDA | 90 mg/day (men), 75 mg/day (women) |
| Minimum to prevent scurvy | ~10 mg/day |
| Body pool at saturation | ~2,000 mg |
| Onset of scurvy (zero intake) | 4-8 weeks (depletion of body pool) |

**Scurvy** is the most operationally dangerous deficiency disease in a bootstrap civilization because it develops rapidly, disables victims completely, and requires only trace amounts of vitamin C to prevent. Symptoms in order of progression: fatigue, gum inflammation and bleeding, petechiae (pinpoint hemorrhages), joint pain, poor wound healing, reopening of old wounds, tooth loss, internal hemorrhage, death.

**Sources**: Citrus fruits (oranges: ~53 mg/100 g, lemons: ~53 mg/100 g), fresh bell peppers (~128 mg/100 g), kale (~120 mg/100 g), broccoli (~89 mg/100 g), potatoes with skin (~20 mg/100 g — important because potatoes are a staple), sprouted grains and beans. Vitamin C is destroyed by prolonged heating — raw or lightly cooked sources are essential.

**Prevention protocol**: One lemon or lime per person per day (provides ~30-40 mg vitamin C, well above the 10 mg/day minimum). Alternatively, 100 g of fresh cabbage or kale every other day. Sprouting beans and grains increases vitamin C content dramatically — mung bean sprouts contain ~14 mg/100 g (unsprouted beans contain essentially none).

### Vitamin D

| Parameter | Value |
|-----------|-------|
| RDA | 600-800 IU/day (15-20 µg) |
| Synthesis from sunlight | 10,000-25,000 IU from 15-30 min full-body UV exposure | Skin type dependent |
| Body storage | 2-3 months in fat tissue | |

**Rickets** (children) and **osteomalacia** (adults): Softening of bones due to impaired calcium metabolism. Symptoms: bone pain, muscle weakness, skeletal deformities (bowed legs in children), increased fracture risk. Prevalence in populations with limited sun exposure (northern latitudes >50°, indoor workers, heavily clothed populations) or dark-skinned populations at high latitudes.

**Sources**: Sunlight (UV-B on skin synthesizes vitamin D — primary source for most humans), fatty fish (salmon: ~500-1,000 IU/100 g, cod liver oil: ~1,360 IU/tablespoon), egg yolks (~40 IU/yolk), mushrooms exposed to UV light. Dietary sources alone are usually insufficient without sun exposure or supplementation.

**Bootstrap prevention**: Ensure outdoor work schedules provide at least 15-30 minutes of skin exposure to direct sunlight 2-3 times per week. At latitudes above 50°, dietary sources become critical during winter months — cod liver oil or fatty fish preservation are necessary.

### B-Complex Vitamins

**Thiamine (B1) — Beriberi**:

| Parameter | Value |
|-----------|-------|
| RDA | 1.1-1.2 mg/day |
| Minimum to prevent beriberi | ~0.3 mg/day |
| Onset of deficiency (zero intake) | 2-3 weeks |

Beriberi takes two forms. **Dry beriberi**: peripheral neuropathy (numbness, tingling, weakness in extremities), difficulty walking, muscle wasting. **Wet beriberi**: cardiovascular failure — edema, enlarged heart, tachycardia, ultimately heart failure and death. Wernicke-Korsakoff syndrome (confusion, ataxia, vision changes, irreversible memory loss) occurs with severe thiamine deficiency, particularly associated with high carbohydrate intake without adequate thiamine.

**Critical risk scenario**: Populations dependent on polished (white) rice as a staple are at extreme risk. The thiamine in rice is concentrated in the bran and germ, which are removed during milling. Historical beriberi epidemics in rice-dependent populations (East Asia, 19th century) killed hundreds of thousands. Brown rice (unmilled) contains adequate thiamine; parboiled rice retains some because the process drives thiamine into the endosperm.

**Sources**: Whole grains (wheat germ: ~1.9 mg/100 g, brown rice: ~0.4 mg/100 g vs. white rice: ~0.07 mg/100 g), pork (~0.9 mg/100 g), legumes, yeast. Sprouting increases thiamine content.

**Niacin (B3) — Pellagra**:

| Parameter | Value |
|-----------|-------|
| RDA | 14-16 mg/day |
| Onset of deficiency | 4-6 weeks |

Pellagra: the "4 Ds" — **Dermatitis** (pigmented, scaling rash on sun-exposed skin), **Diarrhea**, **Dementia** (confusion, aggression, insomnia), **Death** if untreated. Corn-dependent populations are at risk unless corn is treated with alkali (nixtamalization), which releases bound niacin. This is why Mesoamerican cultures that soaked corn in lime water (calcium hydroxide) never developed pellagra despite corn-heavy diets.

**Sources**: Meat (chicken: ~8-12 mg/100 g, beef: ~5 mg/100 g), fish, peanuts (~12 mg/100 g), whole grains. Tryptophan converts to niacin in the body at a ratio of ~60:1 (60 mg tryptophan → 1 mg niacin).

**Other B vitamins**:

| Vitamin | RDA | Key Function | Deficiency |
|---------|-----|-------------|------------|
| Riboflavin (B2) | 1.1-1.3 mg/day | Energy metabolism | Ariboflavinosis: mouth sores, angular stomatitis, skin disorders |
| Pyridoxine (B6) | 1.3-1.7 mg/day | Amino acid metabolism | Peripheral neuropathy, anemia, confusion |
| Cobalamin (B12) | 2.4 µg/day | DNA synthesis, nerve function | Megaloblastic anemia, neurological damage — **only in animal foods** |
| Folate (B9) | 400 µg/day | DNA synthesis | Megaloblastic anemia, neural tube defects in pregnancy |

**Vitamin B12 is exclusively found in animal products** (meat, fish, eggs, dairy). Strictly vegetarian populations will develop B12 deficiency after 3-5 years of stored vitamin depletion, leading to irreversible neurological damage. In a bootstrap civilization, some animal-sourced food is metabolically necessary.

### Iron

| Parameter | Value |
|-----------|-------|
| RDA (men) | 8 mg/day |
| RDA (women, reproductive age) | 18 mg/day |
| Total body iron | 3-4 g |
| Absorption rate (heme iron) | 15-35% |
| Absorption rate (non-heme iron) | 2-20% |

**Iron-deficiency anemia** is the most common nutritional deficiency worldwide. Symptoms: fatigue, weakness, pallor, shortness of breath on exertion, reduced physical work capacity, impaired cognitive function, pica (craving non-food substances). Hemoglobin levels below 12 g/dL (women) or 13 g/dL (men) indicate anemia. Below 7 g/dL is life-threatening.

**Sources**: Red meat (beef: ~2.6 mg/100 g, with high absorption), liver (~5 mg/100 g, highest bioavailability), legumes (lentils: ~3.3 mg/100 g, but low absorption), spinach (~2.7 mg/100 g, low absorption due to oxalates). Cooking in cast iron pots adds dietary iron — acidic foods (tomato sauce) cooked in cast iron can increase iron content 6- to 20-fold.

**Enhancing absorption**: Vitamin C consumed with non-heme iron sources increases absorption 2- to 6-fold. This is operationally important — pairing iron-rich plant foods with vitamin C sources is a practical deficiency prevention strategy. Conversely, tannins (tea, coffee), calcium, and phytates (whole grains, legumes) inhibit iron absorption.

### Calcium

| Parameter | Value |
|-----------|-------|
| RDA | 1,000-1,200 mg/day |
| Absorption rate | 25-35% (varies with vitamin D status) |
| Body content | ~1,000-1,200 g (99% in bone) |

**Calcium deficiency** leads to osteoporosis (reduced bone density, increased fracture risk) and, in severe acute cases, tetany (muscle spasms, tingling, seizures). Calcium requirements are highest in adolescence (bone growth), pregnancy, and lactation.

**Sources**: Dairy products (milk: ~120 mg/100 mL, cheese: ~700 mg/100 g), leafy greens (kale: ~150 mg/100 g, though absorption varies), bones (bone broth, small fish eaten whole with bones), limestone (calcium carbonate — can be added to food as a supplement in minute quantities; nixtamalization of corn uses calcium hydroxide).

### Other Critical Micronutrients

| Nutrient | RDA | Deficiency | Sources |
|----------|-----|------------|---------|
| Iodine | 150 µg/day | Goiter (thyroid enlargement), cretinism (severe: intellectual disability) | Iodized salt, seafood, seaweed. **Preventable with iodized salt — add KI to salt at 20-40 mg/kg** |
| Zinc | 8-11 mg/day | Impaired wound healing, immune dysfunction, hair loss, taste/smell loss | Meat, shellfish (oysters: ~78 mg/100 g), legumes, nuts |
| Vitamin A | 900 µg RAE/day | Night blindness → xerophthalmia → corneal ulceration → irreversible blindness | Liver (~6,500 µg/100 g), sweet potatoes (~960 µg/100 g), carrots (~835 µg/100 g), dark leafy greens |
| Vitamin K | 90-120 µg/day | Impaired blood clotting (hemorrhage) | Leafy greens (kale: ~817 µg/100 g), fermented foods. Gut bacteria also synthesize vitamin K2 |

## Food Composition Analysis

### Proximate Analysis Method

To determine the nutritional content of an unknown foodstuff, perform proximate analysis:

1. **Moisture**: Dry a weighed sample at 105°C to constant weight. Weight loss = moisture content.
2. **Ash (minerals)**: Incinerate dried sample in a crucible at 550°C for 6 hours. Residue = total mineral content.
3. **Crude protein**: Determine nitrogen content via Kjeldahl digestion (digest sample in concentrated H₂SO₄ with catalyst → distill ammonia into boric acid → titrate). Protein = nitrogen × 6.25 (standard conversion factor; varies by food type).
4. **Crude fat**: Extract dried sample with petroleum ether or diethyl ether in a Soxhlet apparatus for 4-6 hours. Evaporate solvent, weigh residue = fat content.
5. **Crude fiber**: Boil defatted sample in 1.25% H₂SO₄ for 30 minutes, then in 1.25% NaOH for 30 minutes. Filter, dry, ash, and weigh. Fiber = weight loss on ashing.
6. **Carbohydrate (by difference)**: 100% - (moisture + protein + fat + ash + fiber) = nitrogen-free extract (digestible carbohydrates).

**Equipment needed**: Drying oven (105°C), muffle furnace (550°C), Kjeldahl digestion apparatus, Soxhlet extractor, analytical balance (0.001 g precision), glassware, reagents.

### Quick Field Assessment

When proximate analysis equipment is unavailable, estimate nutritional quality using:

- **Protein content indicator**: Foods that are dense, chewy, and not sweet tend to be higher in protein. Meat, legumes, and nuts are reliably protein-rich.
- **Vitamin C indicator**: Fresh, raw, tart/acidic plant foods contain the most vitamin C. Cooking destroys 30-60% of vitamin C; prolonged boiling destroys >90%.
- **Iron indicator**: Red/dark meats and dark green leaves contain the most bioavailable iron.
- **Energy density indicator**: Fatty foods (>5 kcal/g) provide the most calories per unit weight — important for limited food transport capacity.

## Dietary Planning for Workforces

### Minimum Viable Diet

A nutritionally adequate minimum diet for a manual laborer requires:

| Component | Daily Amount | Provides |
|-----------|-------------|----------|
| Whole grain (wheat, brown rice, or oats) | 400-500 g | Calories (1,400-1,800 kcal), B vitamins, iron, fiber |
| Legumes (beans, lentils, or chickpeas) | 100-150 g | Protein (25-40 g), iron, folate |
| Fresh vegetables (leafy greens, peppers, cabbage) | 200-300 g | Vitamin C, vitamin A, folate, calcium |
| Fat source (oil, butter, lard) | 30-50 g | Essential fatty acids, calories (270-450 kcal), fat-soluble vitamins |
| Animal protein (meat, fish, or eggs) | 50-100 g | Complete protein, B12, iron, zinc |
| Salt (iodized) | 5-10 g | Sodium, iodine, chloride |
| Clean water | 3-5 L (more in heat/heavy labor) | Hydration |

**Total: ~2,800-3,200 kcal, 65-100 g protein** — sufficient for moderate to heavy labor.

### Meal Planning Principles

1. **Combine protein sources**: Grain + legume at every meal ensures complete amino acid intake. Rice and beans, bread and lentil soup, tortillas and black beans — these pairings are not cultural accidents, they are nutritional engineering.
2. **Include raw or lightly cooked vegetables daily**: Vitamin C is the most labile nutrient. At least one meal per day should include raw or briefly steamed vegetables.
3. **Vary food sources across the week**: No single food provides all micronutrients. Weekly rotation through diverse vegetables, protein sources, and grains prevents marginal deficiencies.
4. **Prioritize calorie adequacy**: Underfeeding is more immediately dangerous than any specific micronutrient deficiency. If food is scarce, caloric adequacy takes priority over nutritional balance — but only as a short-term measure.
5. **Preserve nutrient content during storage and cooking**: Soaking legumes before cooking reduces phytate (improves iron absorption) and cooking time. Steaming retains more water-soluble vitamins than boiling. Fermentation (sauerkraut, kimchi, sourdough) increases bioavailability of several nutrients and produces vitamin C in some cases.

### Deficiency Surveillance Protocol

Monitor workforce for early deficiency signs:

| Deficiency | Early Sign | Detection Method | Threshold for Action |
|-----------|-----------|-----------------|---------------------|
| Vitamin C (scurvy) | Fatigue, bleeding gums | Oral examination | Any cases → increase fresh produce immediately |
| Thiamine (beriberi) | Leg swelling, numbness | Physical examination | Any cases → switch to whole grains |
| Iron (anemia) | Pallor, exertional dyspnea | Conjunctival examination, hemoglobin test | >10% workforce affected → fortify diet with iron sources + vitamin C |
| Vitamin D (rickets/osteomalacia) | Bone pain, weakness | Physical examination, dietary history | Any cases → ensure sun exposure + fatty fish/liver |
| Vitamin A | Night blindness | History (difficulty seeing at dusk) | Any cases → add liver, sweet potatoes, or carrots to diet |
| Iodine (goiter) | Thyroid enlargement | Neck palpation | Any cases → iodize salt (KI at 20-40 mg/kg) |

## Food Safety in Processing

Food safety failures can incapacitate a workforce faster than any nutritional deficiency. Contaminated food causes acute illness (hours to days), while deficiencies develop over weeks to months. A single batch of improperly preserved meat or contaminated grain can sicken an entire work crew.

### Biological Contamination

- **Bacterial pathogens**: The primary food safety threat. *Salmonella* (raw meat, eggs), *E. coli* (contaminated water, unwashed produce), *Clostridium botulinum* (improperly canned low-acid foods), *Staphylococcus aureus* (food handled by infected workers), and *Bacillus cereus* (improperly stored cooked rice). Prevention: cook food thoroughly, keep hot food hot and cold food cold, prevent cross-contamination between raw and cooked food.
- **Botulism**: The most lethal foodborne hazard. *C. botulinum* toxin causes progressive paralysis, starting with vision changes and difficulty swallowing, progressing to respiratory failure. Mortality: 5-10% with treatment, much higher without. Occurs in improperly canned or preserved low-acid foods (vegetables, meat) where the anaerobic environment allows the organism to grow and produce toxin. Prevention: acidify low-acid foods before canning (vinegar, fermentation), or heat-process at pressure-cooker temperatures that destroy the spores.
- **Mycotoxins**: Fungal toxins produced by *Aspergillus* (aflatoxin), *Fusarium*, and *Penicillium* species growing on stored grain, nuts, and dried food. Aflatoxin is a potent liver carcinogen. Occurs in grain stored at moisture content above 14-15% in warm conditions. Prevention: dry grain thoroughly before storage, keep storage dry and ventilated, discard any visibly moldy grain.

### Chemical Contamination

- **Heavy metals**: Lead (from lead-glazed pottery or lead water pipes) accumulates in the body, causing neurological damage, kidney damage, and anemia. Cadmium (from contaminated soil or water) accumulates in kidneys. Mercury (in fish from contaminated water) causes neurological damage. Prevention: use lead-free glazes on food pottery; avoid storing acidic foods in lead-soldered containers.
- **Plant toxins**: Many wild plants contain natural toxins. Cassava contains cyanogenic glycosides (must be peeled, grated, and soaked to remove cyanide). Kidney beans contain phytohaemagglutinin (must be boiled — slow cooking at moderate temperatures actually increases toxin levels). Potatoes exposed to light produce solanine (green potatoes — peel deeply or discard). Proper food preparation knowledge is a safety requirement.

### Food Handling Hygiene

- **Hand washing**: The single most effective food safety measure. Wash hands with soap and water after using latrines, before handling food, and after handling raw meat. A community without hand-washing discipline will experience chronic gastrointestinal illness.
- **Water safety**: Drinking water must be from a protected source (covered well, spring, boiled or filtered water). Waterborne pathogens (cholera, typhoid, dysentery) devastate communities that drink from unprotected surface water. Boiling water for one minute kills most bacterial and viral pathogens.
- **Cross-contamination prevention**: Separate raw meat from ready-to-eat food. Use different cutting surfaces and utensils for raw and cooked food. Clean food preparation surfaces between uses.
- **Temperature control**: Bacterial growth accelerates between 5°C and 60°C (the "danger zone"). Keep perishable food below 5°C or above 60°C. Food left at room temperature for more than 4 hours should be considered potentially hazardous. In practice, this means eating food promptly after cooking or cooling it rapidly for storage.

## Nutritional Assessment Methods

Assessing the nutritional status of a population enables early detection of deficiency trends before they become incapacitating. Three complementary approaches: dietary assessment, clinical examination, and anthropometric measurement.

### Dietary Assessment

- **Food frequency questionnaire**: Ask workers what they ate in the past week — which foods, how often, approximate quantities. Compare against the minimum viable diet requirements. A diet missing entire food groups (no fresh vegetables, no animal products, no legumes) is an immediate red flag.
- **Food inventory tracking**: Monitor community food stores — what comes in, what goes out, and what's available. If the food inventory shows no vitamin C sources for more than 2-3 weeks, scurvy risk is elevated.
- **Meal observation**: Visit meal preparation areas periodically. Observe whether the planned diet is actually being prepared and consumed. A diet plan that exists on paper but is not followed in practice provides no nutritional protection.

### Clinical Examination

Physical signs of specific nutritional deficiencies that can be detected by a trained examiner:

| Sign | Deficiency | Examination Method |
|------|-----------|-------------------|
| Bleeding gums, petechiae | Vitamin C (scurvy) | Oral examination — inspect gums |
| Pale conjunctiva | Iron (anemia) | Pull down lower eyelid, observe color |
| Night blindness | Vitamin A | History — difficulty seeing at dusk |
| Thyroid enlargement | Iodine (goiter) | Neck palpation |
| Edema (ankle swelling) | Protein (kwashiorkor) | Press thumb on ankle, observe indentation |
| Angular stomatitis (mouth corner cracks) | Riboflavin (B2) | Oral examination |
| Rickets (bowed legs in children) | Vitamin D | Physical examination of children |

Clinical signs appear after deficiency is moderately advanced. They provide late warning — by the time signs are visible, the workforce is already impaired. Dietary assessment provides earlier warning.

### Anthropometric Measurement

Body measurements that indicate nutritional status:

- **Body weight**: Weigh workers monthly. Weight loss of more than 5% over one month indicates inadequate caloric intake or illness. Weight loss of 10% or more is clinically significant and requires intervention.
- **Body Mass Index (BMI)**: Weight (kg) / height (m)². BMI below 18.5 indicates underweight; below 16.0 indicates severe malnutrition requiring urgent intervention. BMI above 30 indicates obesity (less common in a bootstrap civilization but possible if food supply is adequate and labor is sedentary).
- **Mid-upper arm circumference (MUAC)**: A simpler field measurement than BMI. Measure arm circumference at the midpoint of the upper arm with a tape measure. Adult MUAC below 23 cm suggests undernutrition; below 18.5 cm indicates severe malnutrition. Useful for rapid screening of large groups.
- **Child growth monitoring**: For communities with children, monthly weight and height measurements plotted on growth charts. Growth faltering (crossing downward through percentile lines) is the most sensitive indicator of chronic nutritional inadequacy in a population.

### Surveillance Schedule

- **Weekly**: Review food inventory for gaps in essential food groups. Check that meal plans are being followed.
- **Monthly**: Weigh all workers. Perform clinical screening for visible deficiency signs. Record findings.
- **Quarterly**: Perform a detailed dietary assessment on a sample of the workforce. Calculate average caloric and protein intake. Compare against requirements for the work being performed.
- **Annually**: Full nutritional survey including anthropometric measurements of the entire community. Adjust food production and distribution plans based on findings.

## Safety & Hazards

- **Refeeding syndrome**: Chronically malnourished individuals given large meals rapidly develop dangerous electrolyte shifts (hypophosphatemia, hypokalemia, hypomagnesemia) that can cause cardiac arrest. Refeed gradually: start at 1,000 kcal/day, increase by 300-500 kcal/day over 5-7 days. Monitor serum phosphate, potassium, and magnesium daily during refeeding. Supplement thiamine 100 mg IV before the first meal to prevent Wernicke's encephalopathy (acute confusion, ataxia, eye movement paralysis) from sudden carbohydrate-driven thiamine depletion. The mechanism: carbohydrate intake triggers insulin release, which drives phosphate and potassium into cells, causing serum levels to crash.
- **Vitamin A toxicity**: Liver consumption in excess (polar bear liver, large amounts of beef liver >100 g/day) causes hypervitaminosis A — headache, nausea, blurred vision, ultimately liver damage and death. Vitamin A has a narrow therapeutic window — deficiency causes blindness, excess causes toxicity. Chronic intake above 10,000 IU/day (3,000 μg RAE) in adults causes liver damage over months to years. Acute single dose above 500,000 IU (150,000 μg RAE) causes nausea, vomiting, and headache within hours.
- **Iron overload**: Chronic excessive iron intake (from repeated blood transfusions, or iron supplement overuse) causes hemochromatosis — liver cirrhosis, heart failure, diabetes. Iron supplements should be given only when deficiency is confirmed. Therapeutic iron dose for deficiency: ferrous sulfate 325 mg (65 mg elemental iron) orally 3 times daily. Treat for 3-6 months to replenish stores. Monitor hemoglobin: should rise 1-2 g/dL per month with adequate iron supplementation. If no response after 1 month, consider malabsorption or ongoing blood loss.
- **Goitrogenic foods**: Raw cruciferous vegetables (cabbage, broccoli, Brussels sprouts) contain goitrogens that interfere with thyroid iodine uptake. Cooking inactivates most goitrogens. Not clinically significant unless iodine intake is marginal and cruciferous consumption is very high.
- **Food adulteration**: In scarcity conditions, food may be adulterated with non-nutritive fillers (sawdust in flour, chalk in bread). This reduces caloric and nutritional density below expected values, causing deficiency even when food quantity appears adequate.
- **Iron supplement poisoning in children**: A single dose of 20-60 mg elemental iron per kg body weight can cause serious poisoning in children. A bottle of ferrous sulfate tablets (325 mg, 65 mg elemental iron each) contains enough iron to kill a 10 kg child who consumes 15-20 tablets. Store iron supplements in childproof containers away from children. Symptoms of acute iron poisoning: vomiting (often bloody), abdominal pain, diarrhea, lethargy, progressing to shock and liver failure. Treatment: induce vomiting if within 1 hour of ingestion, then administer oral deferoxamine or seek emergency medical care.
- **Cassava cyanide toxicity**: Improperly processed cassava contains cyanogenic glycosides that release hydrogen cyanide. Bitter cassava varieties contain 15-400 mg HCN/kg. Lethal dose: 0.5-3.5 mg HCN/kg body weight. For a 60 kg adult, as little as 30 mg HCN can be lethal. Traditional processing (peel, grate, ferment 3-5 days, then press and cook) reduces cyanide to safe levels (<10 mg/kg). Shortcut processing (peel and boil only) may leave dangerous residual cyanide. Symptoms: headache, dizziness, nausea, vomiting, rapid breathing, convulsions, death. Chronic low-level exposure causes konzo (spastic paraparesis — irreversible leg paralysis) and tropical ataxic neuropathy.

## Deficiency Disease Treatment Protocols

When deficiency diseases are identified, the following treatment dosages and schedules restore body stores. These assume oral administration, which is adequate for most deficiencies. IV supplementation is reserved for severe symptomatic cases and requires medical supervision.

| Deficiency | Treatment Dose | Duration | Monitoring | Expected Response |
|-----------|---------------|----------|------------|-------------------|
| Scurvy (vitamin C) | 100-200 mg orally 3 times daily | 7 days, then 100 mg/day maintenance | Gum bleeding stops in 24-48 hours; petechiae fade in 3-5 days | Energy returns in 1-2 days; wound healing resumes in 5-7 days |
| Beriberi (thiamine) | 100 mg orally 3 times daily (or 300 mg IV daily for wet beriberi) | 5-7 days, then 10 mg/day maintenance | Heart rate decreases within hours (wet beriberi); neuropathy improves over weeks | Cardiac symptoms resolve in 1-3 days; nerve recovery takes weeks to months |
| Pellagra (niacin) | 100 mg niacinamide orally 3 times daily | 10-14 days, then 20 mg/day maintenance | Skin rash begins fading in 3-4 days; diarrhea resolves in 2-3 days | Mental confusion clears in 3-7 days |
| Iron-deficiency anemia | Ferrous sulfate 325 mg (65 mg elemental iron) 3 times daily between meals | 3-6 months (continue 2-3 months after hemoglobin normalizes to replenish stores) | Hemoglobin rises 1-2 g/dL per month; reticulocyte count increases within 72 hours | Fatigue improves in 2-4 weeks; pallor resolves in 1-2 months |
| Vitamin D deficiency | 50,000 IU (1,250 μg) orally once weekly for 8 weeks, then 800-1,000 IU/day maintenance | 8 weeks loading, then lifelong maintenance | Serum 25-OH vitamin D reaches >30 ng/mL in 4-8 weeks; bone pain resolves in 2-4 weeks | Muscle strength improves in 2-4 weeks; rickets deformity stabilizes but may not fully correct |
| Vitamin A deficiency | 200,000 IU (60,000 μg RAE) orally as a single dose; repeat in 1-4 weeks if symptoms persist | 1-2 doses, then dietary maintenance | Night blindness resolves in 24-48 hours; xerophthalmia improves in 3-5 days | Corneal ulceration, if present, requires urgent treatment to prevent permanent blindness |
| Iodine deficiency | Potassium iodide 130 mg as a single dose (provides 100 mg iodine), then iodized salt (20-40 mg KI per kg salt) for maintenance | Single dose for acute goiter; lifelong iodized salt for prevention | Goiter shrinks over weeks to months; neonatal cretinism is prevented by maternal iodization before and during pregnancy | Goiter reduction takes 3-12 months; neurological damage from cretinism is irreversible if it occurs in utero |
| Folate deficiency | 1 mg folic acid orally daily | 1-4 months, then 400 μg/day maintenance | Reticulocyte count rises within 5-7 days; hemoglobin normalizes in 1-2 months | Must rule out B12 deficiency first (folate corrects anemia but allows neurological damage from B12 deficiency to progress) |

**Critical interaction**: Before treating megaloblastic anemia with folate, always confirm B12 status. Folate supplementation corrects the anemia of B12 deficiency (masking the deficiency) while allowing irreversible neurological damage (posterior column degeneration, peripheral neuropathy, cognitive decline) to progress. If B12 testing is unavailable and the patient has neurological symptoms (numbness, tingling, balance problems, confusion), treat with both B12 (1,000 μg cyanocobalamin IM daily for 7 days, then monthly) and folate (1 mg orally daily).

## Food Processing for Nutrient Preservation

The way food is processed, stored, and cooked determines how much of its original nutrient content reaches the consumer. Industrial food processing can strip nutrients (white flour loses 70-80% of the B vitamins, 60% of the calcium, and 75% of the iron found in whole wheat); careful processing can enhance bioavailability.

### Nutrient Loss During Common Processing Methods

| Method | Nutrients Most Affected | Typical Loss | Mitigation |
|--------|------------------------|-------------|------------|
| Boiling (water immersion) | Vitamin C, B vitamins (thiamine, folate, riboflavin) | 30-60% (water-soluble vitamins leach into cooking water) | Use minimal water; consume cooking liquid (soups, stews); steam instead of boil |
| Steaming | Vitamin C | 10-25% | Preferred method for vegetables; retains water-soluble vitamins |
| Roasting/baking | Vitamin C, thiamine | 15-30% | Lower temperatures (160-180°C) reduce loss vs. high heat (>200°C) |
| Milling (grain) | B vitamins, iron, fiber | 50-80% (removed with bran and germ) | Use whole grain flour; fortify refined flour with thiamine (2.5 mg/kg), niacin (35 mg/kg), riboflavin (2.5 mg/kg), iron (35 mg/kg) |
| Canning (heat sterilization) | Vitamin C, thiamine, folate | 40-70% (initial heat), additional 10-20%/year storage | Consume within 2 years; canned foods still provide adequate calories and minerals |
| Drying (sun or air) | Vitamin C, vitamin A (carotenoids) | 30-50% (vitamin C), 10-30% (vitamin A) | Dry quickly at moderate temperature (50-60°C); store in opaque, airtight containers |
| Fermentation | Variable; creates B vitamins and vitamin K2 | Minimal loss of most nutrients; increases bioavailability of iron and zinc | Lactic acid fermentation (sauerkraut, sourdough, yogurt) improves mineral absorption by reducing phytate |

### Sprouting for Emergency Vitamin C Production

When fresh produce is unavailable (winter, long sea voyages, siege conditions), sprouting seeds provides a reliable source of vitamin C. Most dry seeds contain no vitamin C; the vitamin is synthesized during germination.

1. **Select seeds**: Mung beans, lentils, chickpeas, wheat berries, alfalfa, or radish seeds. Mung beans are the most common and produce sprouts in 3-4 days.
2. **Soak**: Cover seeds with 3× their volume of water. Soak 8-12 hours at room temperature (20-25°C). The seeds absorb water and swell.
3. **Drain and rinse**: Pour off soak water. Rinse seeds with clean water twice daily. Drain thoroughly (excess water causes rot). Keep in a jar covered with cloth (allows air exchange, prevents contamination).
4. **Grow**: Sprouts reach edible size (2-5 cm stem length) in 3-5 days at room temperature. Keep out of direct sunlight (causes bitterness). White sprouts are fine; exposure to indirect light on the last day produces green, more nutritious sprouts.
5. **Yield**: 100 g of mung bean seeds produces roughly 500-700 g of sprouts. Sprouted mung beans contain approximately 14 mg vitamin C per 100 g fresh weight (dry mung beans contain essentially none). Wheat sprouts contain approximately 6 mg/100 g. Alfalfa sprouts contain approximately 8 mg/100 g.

### Nixtamalization for Niacin Release

Corn-dependent populations that do not treat corn with alkali develop pellagra because niacin in corn is chemically bound (niacytin) and biologically unavailable. Alkaline treatment hydrolyzes the bond, releasing free niacin. This is why Mesoamerican cultures that soaked corn in lime water never developed pellagra despite diets consisting of up to 80% corn.

1. **Prepare lime water**: Dissolve 1-2% calcium hydroxide (slaked lime, Ca(OH)₂) in water. Slaked lime is produced by heating limestone (CaCO₃) to 900°C to produce quicklime (CaO), then adding water to produce Ca(OH)₂. Use 1 g lime per 100 g dry corn kernels.
2. **Cook**: Add corn kernels to the lime solution. Bring to a boil and simmer for 15-30 minutes. The kernels soften and the pericarp (outer skin) loosens.
3. **Steep**: Remove from heat and let stand 8-12 hours (overnight). During steeping, the alkaline environment hydrolyzes niacytin to release free niacin, and calcium from the lime is absorbed into the kernel (increasing dietary calcium intake by 30-50%).
4. **Wash**: Drain and rinse the corn 2-3 times to remove the loose pericarp and excess lime. The corn is now "nixtamal" and can be ground into masa (dough) for tortillas, tamales, or similar foods.
5. **Nutritional improvement**: Untreated corn contains approximately 1.5 mg/g total niacin but only 0.3 mg/g bioavailable. Nixtamalized corn has approximately 1.2 mg/g bioavailable niacin, a 4× improvement. The process also increases calcium content from ~7 mg/100 g to ~150 mg/100 g and improves the protein quality score.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Workforce productivity declining over weeks despite adequate food quantity | Marginal micronutrient deficiency (likely iron or B vitamins) | Perform dietary analysis; add organ meats, leafy greens, and whole grains to rations |
| Multiple workers develop bleeding gums and fatigue in winter | Scurvy — vitamin C deficiency from lack of fresh produce | Immediate: sprout beans/grains for emergency vitamin C. Short-term: procure citrus, cabbage, or potatoes. Long-term: plan year-round fresh produce supply |
| Rice-dependent population develops leg swelling and heart failure | Beriberi — thiamine deficiency from polished white rice | Switch to brown rice or parboiled rice immediately. Add pork, legumes, or wheat germ to diet |
| Workers in underground operations develop bone pain and weakness | Vitamin D deficiency — insufficient sun exposure | Schedule outdoor rotation 15-30 minutes 2-3 times per week. Add fatty fish or cod liver oil to rations |
| Women of reproductive age show pallor and exertional fatigue at higher rates than men | Iron-deficiency anemia — menstrual iron losses + inadequate dietary iron | Increase heme iron sources (meat, fish). Pair plant iron sources with vitamin C. Consider cooking in cast iron pots |
| Population eating primarily corn develops skin rash, diarrhea, and confusion | Pellagra — niacin deficiency from untreated corn diet | Implement nixtamalization (soak corn in lime water — calcium hydroxide from limestone). Add peanuts, meat, or fish to diet |
| High-altitude or northern latitude workers develop thyroid enlargement | Iodine deficiency — low environmental iodine | Add potassium iodide to salt at 20-40 mg KI per kg salt. This is cheap and prevents both goiter and cretinism |
| Proximate analysis shows lower protein content than expected for grain | Grain variety, growing conditions, or storage degradation | Re-test with fresh sample. Adjust dietary calculations based on actual measured values, not book values |

## See Also

- [Food Processing](../food-processing/index.md) — preservation, milling, and food preparation techniques
- [Food Preservation](../food-processing/preservation.md) — methods to retain nutrients during storage
- [Diagnostics](diagnostics.md) — physical examination and laboratory testing for deficiency diseases
- [Pharmacology](pharmacology.md) — vitamin and mineral supplementation as pharmaceutical preparations
- [Occupational Health](occupational-health.md) — workforce health monitoring and hazard exposure
- [Agriculture](../agriculture/index.md) — crop production for food supply
- [Chemistry](../chemistry/index.md) — analytical chemistry for food composition testing

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Public Health, Sanitation & Medicine](./index.md) • [All Domains](../../index.md)*

