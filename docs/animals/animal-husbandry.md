# Animal Husbandry

> **Node ID**: animals.animal-husbandry
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`animals.domestication`](domestication.md)
> **Enables**: [`animals.draft-power`](draft-power.md), [`animals.animal-materials`](animal-materials.md), [`foundations.food-agriculture`](../foundations/food-agriculture.md)
> **Timeline**: Years 0-10
> **Outputs**: draft_animals, wool, hides, milk, meat, dung
> **Critical**: Yes — core knowledge for managing all livestock species productively

## Problem

A bootstrapping civilization needs reliable sources of labor, food, fiber, and fertilizer. Wild animal populations cannot sustainably provide these at scale — hunting depletes stocks faster than they recover, and wild animals cannot be directed toward productive work. Animal husbandry transforms captive livestock into a managed resource: draft power for plowing and transport (1-2 hp sustained per ox), milk and meat as concentrated protein sources, wool and hides for textiles, and manure to sustain crop yields. Without systematic breeding, feeding, health management, and seasonal planning, livestock herds stagnate, succumb to disease, and fail to meet settlement needs.

## Prerequisites

- [Livestock domestication](domestication.md) — captive breeding populations of cattle, sheep, goats, pigs, or poultry
- [Food and agriculture](../foundations/food-agriculture.md) — fodder production (pasture, hay, grain) to feed stock through winter
- [Basic construction](../foundations/index.md) — barns, fences, and shelters for housing and containment
- [Water access](../agriculture/irrigation.md) — reliable clean water supply (40-100 L/day per cattle head)
- [Medicine](../health/medicine.md) — basic disease diagnosis and treatment capability
- [Iron working](../metals/iron-steel.md) — for horseshoes, harness hardware, fencing staples, and tools


Animal husbandry — the domestication, breeding, and management of livestock — provides labor power (oxen, horses, mules), raw materials (wool, leather, tallow, bone), and food (milk, meat, eggs). It is a prerequisite for pre-industrial transport, textile production, and sustainable agriculture.

## Breeding Programs & Genetic Improvement

Systematic breeding transforms a captive wild population into a productive domesticated one over 5-15 generations. Each generation of selection shifts the population mean by h² × S, where h² is the heritability (typically 0.2-0.5 for production traits) and S is the selection differential (the difference between selected parents and the population mean).

For milk yield in cattle with h² ≈ 0.3, selecting the top 20% of cows (selection differential ~400 L above the 4,000 L herd mean) yields an improvement of ~120 L per generation. At one generation per 3 years (cattle), that is ~40 L/year — compounding to a doubling of milk yield in ~30 years of consistent selection.

**Selection methods**: Mass selection (pick the best individuals based on their own performance) works well for highly heritable traits (growth rate 0.3-0.5 heritability, fleece weight 0.4-0.6). Family selection (pick based on siblings' or progeny's performance) works better for low-heritability traits (fertility 0.05-0.15, disease resistance 0.1-0.2). A practical breeding program tracks 4-6 key traits per species and applies a selection index weighting each trait by its economic value and heritability.

**Inbreeding management**: Maintain a minimum effective population size (Ne) of 50 breeding animals per species to keep inbreeding below 1% per generation. For cattle with 20 breeding cows and 2 bulls, Ne = 4 × (20 × 2) / (20 + 2) = 7.3 — dangerously low. Expand to 50 cows and 5 bulls for Ne = 18.2, still marginal. Exchange breeding males with neighboring settlements every 3-4 generations to introduce fresh genetics.

**Crossbreeding systems**: Two-breed rotation (breed cows of breed A to bulls of breed B, then resulting heifers back to breed A bulls) captures 67% of hybrid vigor (heterosis). Crossbred animals typically outperform purebreds by 5-15% for growth rate, 10-20% for reproduction, and 10-15% for milk yield. Three-breed rotation maintains 86% of maximum heterosis.

**Reproductive rates by species**:

| Species | Gestation (days) | Offspring/birth | Generations/year | Annual offspring/female |
|---------|-----------------|-----------------|------------------|------------------------|
| Cattle | 283 | 1 | 0.8 | 0.8 calves |
| Sheep | 147 | 1-3 | 1.0 | 1.5-3.0 lambs |
| Goats | 150 | 1-3 | 1.0 | 1.5-3.0 kids |
| Pigs | 114 | 8-12 | 2.0 | 20-25 piglets |
| Rabbits | 31 | 6-10 | 7-8 | 40-50 kits |
| Chickens | 21 (inc.) | 8-12 eggs/clutch | 4-6 | 200-300 eggs |

**Artificial insemination**: Collecting semen from a superior male allows wider distribution of desirable genetics without moving live animals. Fresh semen remains viable for 2-4 days at 4-5°C. A single bull ejaculate (5-10 mL, 1-2 billion sperm/mL) can inseminate 50-200 cows when extended with diluent (egg yolk-citrate or skim milk-glycerol). Detect estrus by observing mounting behavior (cattle cycle every 21 days, standing heat lasts 12-18 hours). Inseminate 6-12 hours after first observed standing heat for ~60-70% conception rate.

## Draft Power & Work Capacity

Oxen (castrated cattle trained to pull) are the primary draft animals for a bootstrapping civilization. A trained ox pulls 10-15% of its body weight at 3-4 km/h for 6-8 hours/day. A 600 kg ox generates 0.5-0.8 horsepower (370-600 W) sustained output, peaking at 1.5-2.0 hp for short bursts.

A pair of oxen plows 0.3-0.5 hectares per day with a single-furrow moldboard plow, turning soil to 15-20 cm depth. A horse-drawn mower cuts 2-3 hectares of hay per day. A horse pulling a cart on a good road transports 500-800 kg payload at 6-8 km/h for 30-40 km/day.

**Harness types**: The ox yoke (wooden beam across the withers, 8-12 cm diameter, padded with sheepskin) limits pulling efficiency to ~60% of capacity. The horse collar (padded oval resting on the shoulders) allows 95% efficiency — a horse in a collar pulls 30-50% more than in a yoke. The horse collar requires leather working, stuffed padding, and iron hardware: achievable by Year 3-5 with [basic iron working](../metals/iron-steel.md).

**Draft power comparison**:

| Animal | Weight (kg) | Pull force (N) | Speed (km/h) | Work hours/day | Power (W) |
|--------|-------------|----------------|--------------|----------------|-----------|
| Ox | 500-700 | 500-1000 | 3-4 | 6-8 | 400-750 |
| Horse | 400-600 | 400-900 | 6-8 | 8-10 | 650-1300 |
| Donkey | 150-350 | 150-350 | 4-5 | 6-8 | 150-350 |
| Mule | 350-500 | 350-750 | 5-7 | 8-10 | 400-900 |

**Work scheduling**: Draft animals need 2-3 hours of rest midday in hot weather. Water every 2 hours during work (40-60 L/day total for cattle). Grain supplementation of 2-4 kg oats or barley per working day sustains body condition through plowing season (60-90 days of heavy work). Rotate: 2 days on, 1 day off prevents exhaustion.

**Mule advantages**: Mules (horse mare × donkey jack) inherit the donkey's digestive efficiency (5-8 kg DM/day vs. 10-15 kg for horses), heat tolerance (effective to 35°C), and disease resistance. They live 30-40 years (vs. 20-25 for horses). Weight 350-500 kg, pulls 15-20% of body weight. Sterile — must be produced by keeping a jack donkey with horse mares.

**Shoeing**: Working horses on hard ground need iron shoes replaced every 6-8 weeks. A horseshoe weighs 400-800 g. Hot shoeing (heat shoe in forge, shape on anvil, burn-fit) provides best fit. Nail into the insensitive hoof wall with 6-8 nails per shoe. Shoeing requires: forge, anvil, tongs, horseshoe nails (5-6 mm square iron), hoof nippers, rasp, and knife. Ox shoes are split (two halves per cloven hoof, 8 shoes per ox). See [Draft Power & Harnessing](draft-power.md) for complete details.

## Dairy Production

A dairy cow produces 10-20 L milk/day during a 305-day lactation, yielding 3,000-6,000 L per cycle. Milk composition: 3.5-4.0% fat, 3.0-3.5% protein, 4.5-5.0% lactose, 0.7% minerals. At 650 kcal/L, 4,000 L represents 2.6 million kcal/year — enough dietary energy for 3-4 adults.

**Butter**: Separate cream by gravity (stand 12-24 hours at 10-15°C, skim top) or mechanical separator. Churn at 10-15°C for 20-40 minutes until granules form (0.5-3.0 mm). Wash with cold water (2-3 rinses at 5-8°C). Salt at 1-2% as preservative. Yield: 40-50 kg butter per 1,000 L whole milk. Working with wooden paddles removes air pockets and extends shelf life to 2-4 weeks at 10-15°C.

**Cheese (hard, cheddar-type)**: Yield 100 kg per 1,000 L milk. Warm to 30-32°C, add starter culture (1-2% lactic bacteria from previous batch), ripen 30-45 min to pH 6.5. Add rennet (1 mL calf rennet per 10 L, or vegetable rennet from cardoon thistle). Coagulate 30-45 min. Cut curd to 6-10 mm cubes. Cook to 38-40°C over 30 min. Drain whey. Press at 1-2 kg/cm² for 12-24 hours. Brine in 20% NaCl for 24-48 hours at 10-12°C. Age at 8-12°C, 80-85% humidity for 3-18 months. Moisture: 35-40%. pH 5.0-5.5.

**Goat dairy**: A dairy goat produces 2-5 L/day over 250 days. Goat milk fat globules are 1-2 μm (vs. 3-4 μm cow), naturally homogenized, and yield 10-15% more cheese per liter. Three goats produce the same volume as one cow on 1/4 the feed (6-9 kg DM/day for 3 goats vs. 20-30 kg for a cow).

**Milk preservation without refrigeration**: Milk spoils in 4-6 hours at 25°C. Methods: (1) Yogurt — inoculate at 42-45°C for 4-6 hours, pH 4.0-4.6, keeps 7-14 days at 4-10°C. (2) Cheese — removes 80-90% water, shelf life months to years. (3) Butter — fat fraction keeps 2-4 weeks at 10-15°C. (4) Pasteurization at 63°C/30 min or 72°C/15 sec kills tuberculosis and brucellosis — critical for [public health](../health/medicine.md). (5) Boiling extends shelf life to 12-24 hours.

**Milking hygiene**: Clean udders with warm water (40-45°C) before milking. Strip first 3-4 streams into strip cup (reveals clots indicating mastitis). Milk into sanitized vessels (scalded with boiling water). Strain through clean cloth. Cool to below 10°C within 1 hour. Mastitis detection: California Mastitis Test — gel formation indicates somatic cells above 500,000/mL, reducing yield 10-25%.

## Poultry Management

Chickens are the highest-priority poultry species: fast-growing (broilers reach 2.0-2.5 kg in 6-8 weeks), prolific egg layers (200-300 eggs/hen/year at 60-65 g each), and efficient feed converters (1.6-2.0 kg feed per kg gain). A flock of 25 hens produces 5,000-7,500 eggs/year (300-450 kg total egg weight) on 2-3 kg feed/day total.

**Housing**: Allow 0.1-0.2 m² per bird in the coop (2.5 m² for 25 hens) plus 0.5-1.0 m² per bird in an outdoor run. Perch space: 15-20 cm per bird. Nest boxes: 1 per 4-5 hens, 30 × 30 × 30 cm, dark and elevated. Ventilation: 4-6 air changes/hour; ammonia must stay below 25 ppm. Deep litter (10-15 cm wood shavings or straw, turned weekly) provides insulation and consumes manure through microbial action.

**Egg collection and storage**: Collect eggs 2-3 times daily. Store at 10-15°C, 70-80% humidity. Unwashed eggs (bloom intact) keep 2-3 weeks at room temperature, 4-6 weeks refrigerated. Washing removes the protective cuticle — washed eggs must be refrigerated and used within 2 weeks. Candle eggs (hold before bright light) to detect cracks and blood spots.

**Incubation**: Natural (broody hen sits on clutch of 10-12 eggs for 21 days) or artificial incubator (electrically heated cabinet at 37.5°C, 55-60% humidity days 1-18, 65-70% days 19-21, turn eggs 3-5×/day for first 18 days). Hatch rate: 85-95% fertile eggs with good management. Brooder temperature: 35°C first week, reduce 2-3°C per week until ambient.

## Fiber Production

**Wool**: A sheep produces 2-5 kg raw fleece per year. After cleaning (removing 30-50% as lanolin, dirt, and vegetable matter), yield is 1.0-3.5 kg clean wool. Shear annually in spring. Staple length 5-15 cm; fiber diameter 18-40 μm (under 19 μm = fine wool).

Processing chain: shear → skirt (remove stained edges) → wash (50-55°C water + mild alkali, 2-3 rinses) → card (hand carders 0.5-1.0 kg/hr, drum carder 2-5 kg/hr) → spin (drop spindle 50-100 m/hr; spinning wheel 200-400 m/hr) → ply (twist 2+ singles for strength) → weave (floor loom 1-3 m²/day) or knit.

**Wool grading**: Fine wool (Merino-type, <19 μm) for garments. Medium (19-25 μm) for outerwear and blankets. Coarse (>25 μm) for carpets and rugs. The Bradford count indicates hanks of 560 yards per pound of top: 60s ≈ 25 μm, 80s ≈ 19 μm. Finer wool commands 2-5× the price.

**Felt**: Layer clean carded wool 4-6 layers thick in cross-hatch on a mat. Saturate with hot soapy water (60-70°C, 2-3% soap). Agitate 30-60 min by rolling and pressing. Fibers interlock via scale structure, producing dense fabric (0.3-0.8 kg/m²). Shrinkage 30-40%. No spinning or weaving needed. Uses: hats, boots, saddle blankets, yurt covers, armor padding.

**Other fibers**: Cashmere (goat down, 14-19 μm, 100-200 g/goat/year, spring combing). Mohair (Angora goat, 23-38 μm, 2-6 kg/year, sheared 2×/year). Alpaca (20-30 μm, 2-5 kg/year, 22 natural colors). Rabbit angora (12-16 μm, 400-1200 g/year, 7× warmer than sheep wool by weight). Horsehair (tail, 50-150 μm, for upholstery and fishing lines).

## Meat Production & Preservation

**Slaughter yields by species**:

| Species | Live weight (kg) | Carcass yield (%) | Carcass weight (kg) | Edible meat (%) |
|---------|-----------------|-------------------|--------------------:|-----------------|
| Cattle | 450-600 | 50-60 | 225-360 | 55-70 |
| Sheep | 35-50 | 45-55 | 16-28 | 55-65 |
| Pigs | 100-130 | 70-80 | 70-104 | 65-75 |
| Chickens | 1.5-3.0 | 70-75 | 1.1-2.3 | 65-70 |
| Rabbits | 2.0-2.5 | 55-60 | 1.1-1.5 | 60-65 |

**Carcass utilization**: Blood (3-4% live weight, 15-20 L from a steer) — blood sausage or blood meal fertilizer (13% N). Organs: liver 1.5-2.0 kg, heart 1.5-2.0 kg — consume within 24 hours or cook and pot. Bones (15-20% of carcass) — bone broth (boil 12-24 hours with vinegar), bone meal fertilizer (calcine at 800°C, grind, 3% N, 12% P₂O₅), tools, buttons, glue. Fat (15-25 kg kidney/pelvic fat from steer) — render at 90-100°C into tallow for candles, [soap](../chemistry/alkalis.md), and lubricant. Hide — see [Leather Production](../animals/leather.md).

**Preservation without refrigeration**: (1) Salting — pack in coarse salt 10-15% by weight for 7-14 days at 2-5°C. Water activity below 0.85 inhibits bacteria. Keeps 6-12 months at 10-15°C. (2) Smoking — hang salted meat over hardwood fire at 50-70°C for 12-48 hours. Antimicrobial phenols in smoke. Combined: 12-18 months shelf life. (3) Jerky — cut lean meat 5-10 mm thick, dry at 50-60°C to <15% moisture. Weight loss 70-75%. Keeps 6-12 months. (4) Potting — cook meat, pack in crocks, cover with 1 cm rendered fat (excludes air). Keeps 3-6 months at 5-10°C.

**Sausage**: Grind meat (3-8 mm plate), mix with 2.5-3.0% salt, 0.25% sodium nitrite (from [nitrates](../chemistry/acids-bases.md), prevents botulism), 15-30% fat, spices. Stuff into natural casings (sheep intestine 20-22 mm, pig intestine 28-35 mm). Fresh: cook within 3 days. Fermented: add lactic culture, ferment at 20-25°C for 24-72 hours (pH 4.6-5.0), dry at 12-15°C, 70-80% humidity for 3-8 weeks until 30-40% weight loss. Shelf stable.

## Dung & Manure Management

A 500 kg cow produces 30-40 kg fresh manure/day containing 0.3-0.4 kg N, 0.1-0.2 kg P, 0.2-0.3 kg K. Over 180-day housing: 5,400-7,200 kg manure with 54-72 kg N — enough for 0.5-1.0 ha of cereals at 60-80 kg N/ha. Poultry manure is 3-4× more nutrient-dense: 1.5% N, 1.0% P₂O₅ dry basis. Apply poultry at 2-3 t/ha; cattle at 15-25 t/ha.

**Manure nutrient content by species**:

| Species | kg/day fresh | %N (dry) | %P₂O₅ (dry) | %K₂O (dry) | Application rate (t/ha) |
|---------|-------------|----------|-------------|------------|------------------------|
| Cattle | 30-40 | 2.0-2.5 | 1.0-1.5 | 1.5-2.0 | 15-25 |
| Sheep | 2-4 | 2.5-3.0 | 1.5-2.0 | 2.0-2.5 | 10-15 |
| Pigs | 5-8 | 2.5-3.0 | 2.0-2.5 | 1.5-2.0 | 10-20 |
| Poultry | 0.1-0.2 | 4.0-5.0 | 3.0-4.0 | 1.5-2.0 | 2-3 |
| Horses | 20-30 | 1.5-2.0 | 0.8-1.2 | 1.5-2.0 | 15-20 |

**Composting**: Mix manure with bedding (target C:N 25-30:1; manure is 10-15:1, straw is 80-100:1; mix 2-3 parts manure to 1 part bedding by volume). Windrows 1.5-2.0 m wide × 1.0-1.5 m tall. Turn every 3-5 days for 2 weeks, then weekly. Temperature reaches 55-65°C in 2-3 days — kills pathogens and weed seeds in 3 days at 55°C. Complete in 6-12 weeks. Volume reduces 40-50%. Final C:N 15-20:1.

**Biogas**: Anaerobic digestion in sealed tank (3-5 m diameter, 2-3 m deep, gas-tight cover) at 35-38°C. Yield: 0.2-0.3 m³ biogas per kg volatile solids. One cow produces 0.6-0.9 m³/day (60-70% CH₄, 21-24 MJ/m³). One m³ biogas replaces 0.5-0.6 L gasoline. A 20-cow digester produces enough cooking fuel for 4-6 hours/day for 6 people. Hydraulic retention time: 20-40 days. Effluent retains 90-95% of original N and P as fertilizer.

## Animal Health & Disease Prevention

**Vaccination schedule**: Core vaccines (where production exists): clostridial 7-way at 6-8 weeks + booster 4-6 weeks later; brucellosis (strain 19 or RB51 for heifers at 4-8 months); tetanus (0.5 mL toxoid IM, annual for horses); rabies (1 mL IM, annual where endemic). Cold chain: 2-8°C in insulated boxes, ice packs replaced every 24-48 hours. Discard if frozen or above 25°C.

**Parasite control**: Anthelmintic at spring turnout and autumn housing. Rotate drug classes annually (ivermectin → fenbendazole → levamisole → moxidectin). Fecal egg counts via McMaster technique (2 g feces in 28 mL saturated NaCl, count in 0.15 mL chamber; EPG = count × 50). Treat cattle at EPG >200-300, sheep at EPG >500-1,000.

**Quarantine**: Isolate incoming animals 30 days, 15+ m from herd. Test for tuberculosis (caudal fold: 0.1 mL tuberculin intradermally, read at 72 hours; >4 mm swelling = positive), brucellosis (serum agglutination), Johne's (fecal PCR). Temperature twice daily: >39.5°C cattle, >40.0°C sheep/goats, >40.5°C pigs warrants investigation.

**Emergency conditions**: Bloat — stomach tube or trocar through left flank. Milk fever — 500 mL 23% calcium gluconate IV over 10-15 min. Foot rot — trim hoof, 5-10% CuSO₄ foot bath. Flystrike — shear affected area, remove maggots, antiseptic. Dystocia — reposition fetus within 30 min; unresolved → Cesarean by trained practitioner. See [Medicine](../health/medicine.md) for treatment protocols.

## Seasonal Management Calendar

**Spring** (calving, lambing, planting): Move pregnant animals to clean paddocks 2 weeks before due dates. Check first-time mothers every 4 hours during labor. Ensure colostrum supply — newborns must receive colostrum within 6 hours (gut closes to antibody absorption after 24 hours; failure causes 50-80% mortality in first month). Castrate and tail-dock lambs within first week. Begin pasture turnout when grass reaches 10-15 cm. Shear sheep before lambing or 4-6 weeks after.

**Summer** (hay, heat, health): Cut hay at early heading stage for maximum protein (10-14% crude protein vs. 6-8% for mature cut). Field-dry to 18-20% moisture (2-4 days depending on weather), then bale or stack. Cattle drink 50-80 L/day in hot weather; provide shade above 25°C (heat stress reduces feed intake and milk production by 10-20%). Monitor for bloat on lush legume pasture. Wean spring-born young stock. Apply fly control.

**Autumn** (breeding, culling, feed stockpile): Sheep and goats cycle during shortening daylight — flush ewes (increase nutrition 2-3 weeks before breeding) to boost twinning by 15-20%. Pregnancy-check cattle 40-60 days post-breeding. Cull open females and low producers. Calculate winter feed budget: daily need × winter days × all animals + 15% buffer. Treat all livestock for parasites before housing. Store root crops for winter feed (fodder beet yields 40-80 tonnes/ha).

**Winter** (feeding, shelter, monitoring): Cattle require 10-15 kg hay/day; sheep 1.5-2.5 kg/day; horses 8-15 kg/day. Provide windbreaks (wind chill increases effective cold by ~1°C per km/h above 8 km/h). Increase grain for pregnant females in last trimester. Break ice on water troughs twice daily. Monitor body condition: target 2.5-3.0 on a 5-point scale for cattle. Poultry egg production declines below 12 hours daylight without supplemental light.

## Infrastructure Requirements

**Barn dimensions**: Tie-stall for 20 cows: 20 stalls at 1.2 m × 1.8 m, 1.5 m feed aisle, 1.0 m gutter. Footprint: 6.0 m × 24 m = 144 m². Hay loft above (5-8 tonnes). Concrete floor, 2-3% slope to drain. Ridge vent: 0.1 m² per 10 m² floor. Bedded pack: 5-7 m²/adult cattle, straw 3-5 kg/day/animal.

**Fencing**: Post-and-rail: posts 10-15 cm diameter, 60-80 cm deep, 2.5-3.0 m spacing, 2-3 rails, height 1.2-1.5 m. Hedgerow: hawthorn double row, 20-30 cm spacing, 5-8 years to barrier. Stone wall: 1.0-1.2 m high, 0.5 m base, 3-5 m/day/waller. Woven wire (when available): 8-10 cm mesh, 1.0-1.2 m height, posts every 5 m.

**Water system**: Daily demand: cattle 40-100 L, horses 30-50 L, sheep 4-10 L, pigs 8-15 L, chickens 0.25-0.50 L. A 50-head mixed operation: 2,500-3,500 L/day. Well at 5 L/min (7,200 L/day) provides margin. Troughs: 20-40 L per position, refill 2-3× daily. Freeze protection: insulated boxes with heated stones.

**Feed storage**: One cow eats 10-15 kg hay/day × 120 days = 1,200-1,800 kg. Twenty cows: 24-36 tonnes + 15% buffer = 28-41 tonnes. Stack density 200-250 kg/m³ → 112-205 m³. A hay barn 6 m × 12 m × 3 m (216 m³) stores ~48 tonnes. Stack on pallets, protect from rain. Hay above 25% moisture risks spontaneous combustion in 3-7 days.

## Economic Considerations

**Feed conversion ratios**: Cattle 6-8 kg DM/kg gain. Pigs 2.5-3.5:1. Chickens 1.6-2.0:1. Rabbits 2.5-3.0:1. Fish (aquaculture) 1.0-1.5:1. Poultry and rabbits are most protein-efficient; cattle are justified by multi-output capability.

**Land budget for family of 6** (150-200 kg meat/year): Cattle-only: 4-5 ha pasture + 2-3 ha hay. Chicken-only: 0.5-1.0 ha grain. Mixed system (1 cow + 5 sheep + 10 chickens + 2 pigs) on 3-4 ha provides meat, eggs, milk, wool, and draft power.

**Daily labor**: Dairy cows 30-45 min/cow. Sheep 5-10 min/head. Pigs 10-15 min/sow. Poultry 15-20 min/50 birds. Total for 2 cows + 10 sheep + 2 pigs + 30 chickens: 3-4 hours/day.

## Predator Protection & Guarding

Wolves, coyotes, foxes, big cats, and birds of prey all threaten livestock. Losses of 2-5% per year are typical without protection in predator-rich environments. Guard dogs raised with the flock from puppyhood (2-3 dogs per 100 sheep) are the most effective deterrent — a 40-60 kg guard dog (Anatolian Shepherd, Great Pyrenees, or similar breed) confronts predators and alerts humans by barking. Training: isolate pup with lambs at 8-12 weeks, minimize human contact to prevent bonding to people over sheep. Guard dogs reduce predation losses by 70-90%.

**Fencing for predator exclusion**: Electric fencing (one wire at 25 cm and one at 60 cm, 3,000-5,000 V pulse from energizer) deters most predators but requires [wire production](../metals/iron-steel.md) and a power source (solar energizer: 0.5-1.0 W output). Woven wire with a barbed wire overhang angled outward at 45° prevents climbing predators. Night housing in predator-proof enclosures (tight mesh or solid walls, covered where hawks are a threat) is essential for poultry and young stock.

**Donkey and llama guards**: A single donkey (180-450 kg) bonded to a sheep or goat flock attacks canid predators by charging, biting, and trampling. Introduce donkey to flock at least 30 days before predator season. Llamas (130-200 kg) serve the same function and are effective against coyotes and foxes. One guard animal per 50-100 head of small ruminants. Both species require the same feed as the flock they guard.

## Young Stock Management

**Colostrum and neonatal care**: All mammalian newborns must receive colostrum within 6 hours of birth. The gut closes to antibody absorption after 24 hours; failure to receive colostrum results in 50-80% mortality in the first month. For orphaned neonates, bottle-feed warmed colostrum (38-39°C) at 10% of body weight in the first 24 hours, divided into 3-4 feedings. A calf needs 2-4 L of colostrum in the first 12 hours.

**Creep feeding**: Provide supplemental feed to nursing young in an area accessible only to them (creep feeder: opening 30-40 cm wide for lambs, 60-70 cm for calves). Offer palatable grain (cracked corn, rolled oats) at 16-18% protein. Intake ramps from 0.1 kg/day initially to 1.0-1.5 kg/day by weaning. Creep feeding increases weaning weight by 15-25% and reduces lactation demand on the dam.

**Weaning**: Gradual weaning (fence-line contact for 7 days where young and dam can see and smell but not nurse) reduces cortisol and weight loss. Post-weaning, monitor daily for 2 weeks; weight loss exceeding 10% triggers investigation. Weaning ages: calves 6-8 months, lambs/kids 3-4 months, piglets 3-6 weeks, foals 4-6 months, chicks independent from day 1.

**Castration methods**: Elastrator banding (rubber ring at 1-7 days) — testicles atrophy in 2-4 weeks. Burdizzo clamp (crush spermatic cord at 2-8 weeks) — no incision, lowest infection risk. Surgical removal (scalpel at 2-12 weeks) — most reliable, requires clean instruments and antiseptic. All methods require monitoring for infection for 7 days post-procedure.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Low milk yield | Poor nutrition, mastitis, or genetics | Increase energy intake by 20%; California Mastitis Test; cull persistent low producers |
| Weight loss in herd | Parasites, inadequate feed, or disease | Fecal egg count (McMaster); body condition scoring; increase ration; anthelmintic treatment |
| Poor conception rates | Mineral deficiency, heat stress, low body condition | Supplement phosphorus and selenium; provide shade; target BCS 2.5-3.0 pre-breeding |
| Calf/lamb mortality >10% | Failure of passive transfer (colostrum), cold exposure, predators | Ensure colostrum within 6 hours; provide dry shelter; guard animals |
| Bloat in cattle | Lush legume pasture, grain overload | Remove from clover/alfalfa; pass stomach tube; prevent with gradual pasture introduction |
| Poultry egg drop | Short daylight, poor nutrition, disease, or molt | Provide 14-16 hours light; 16-18% protein layer ration; check for mites/lice |
| Hay mold/spoilage | Baled above 20% moisture, poor storage | Check moisture before baling; stack on pallets; ventilate storage; discard black/dusty bales |
| Lameness in herd | Foot rot, laminitis, or injury | 5-10% CuSO₄ foot bath; trim hooves; check for stones/abscesses |
| Diarrhea in young stock | Scours (E. coli, crypto, coccidia) | Electrolyte therapy; isolate affected; ensure colostrum; clean bedding |
| Aggressive bull/stallion | Sexual behavior, inadequate handling | Use experienced handler; breeding harness; cull dangerous animals |

## See Also

- [Livestock Domestication](domestication.md) — species-specific husbandry for all fifteen farmed species
- [Draft Power & Harnessing](draft-power.md) — working oxen, horses, and donkeys for plowing, transport, and milling
- [Animal-Derived Materials](animal-materials.md) — leather, tallow, wool, horn, bone, sinew, and hide glue
- [Leather Production](leather.md) — hide processing and tanning
- [Food & Agriculture](../foundations/food-agriculture.md) — manure sustains crop yields; meat, milk, eggs are primary protein sources
- [Medicine](../health/medicine.md) — disease diagnosis, treatment, and zoonotic disease prevention
- [Insect Farming](insect-farming.md) — black soldier fly larvae for waste conversion and animal feed protein
- [Crop Rotation](../agriculture/crop-rotation.md) — integrating livestock with arable farming
- [Soil Management](../agriculture/soil-management.md) — manure as soil amendment
- [Textiles](../textiles/spinning.md) — wool fiber processing chain

[← Back to Animals](index.md)
