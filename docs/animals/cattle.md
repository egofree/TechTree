# Cattle (*Bos taurus*)

> **Node ID**: animals.cattle
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`animals.domestication`](domestication.md)
> **Enables**: [`animals.animal-materials`](animal-materials.md), [`animals.draft-power`](draft-power.md), [`foundations.food-agriculture`](../foundations/food-agriculture.md)
> **Timeline**: Years 1-30+
> **Outputs**: beef, dairy, tallow, leather_hides, manure, draft_power
> **Critical**: Yes — most productive multi-purpose livestock species


Cattle are the single most productive domesticated species for a bootstrapping civilization. A mature cow converts pasture and roughage into high-value protein (meat and milk), provides draft power for plowing and transport, produces leather and tallow as industrial materials, and generates 30-40 kg of nitrogen-rich manure per day that sustains soil fertility. Mature weight ranges from 400-800 kg (cows at the lower end, bulls and oxen at the upper). Gestation is 283 days (range 279-290), producing a single calf per pregnancy (twins in roughly 1-2% of births).

No other livestock species matches cattle for combined output of food, fiber, power, and fertilizer. Their size makes them capital assets — each animal represents significant investment in feed, housing, and labor, but returns proportionally high value over a productive lifespan of 10-15 years.

| Parameter | Value | Notes |
|-----------|-------|-------|
| Mature weight (cows) | 400-700 kg | Breed dependent |
| Mature weight (bulls) | 700-1,200 kg | Breed dependent |
| Gestation | 283 days (range 279-290) | Single calf typical |
| Breeding age (heifers) | 14-18 months | Target 60-65% mature weight |
| Productive lifespan | 10-15 years | Declining after year 8 |
| Daily dry matter intake | 2.5-3.0% of body weight | 12-25 kg/day for mature cow |
| Daily water intake | 40-80 L | Doubles above 30°C |
| Manure production | 30-40 kg/day | 8-12 tonnes/year |

## Prerequisites

| Requirement | Source | Notes |
|-------------|--------|-------|
| Secure fencing and handling facilities | [`foundations.tools-basic`](../foundations/tools-basic.md) | Cattle crush, races, gates |
| Winter feed storage (hay/silage) | [`plants.fiber-plants`](../plants/index.md) | 1.2-1.8 tonnes hay per animal per winter |
| Reliable water source (40-80 L/day per animal) | [`water.purification`](../water/index.md) | Well, spring, or piped supply |
| Pasture (0.5-3.0 ha per animal) | [`agriculture`](../agriculture/index.md) | Stocking rate depends on land quality |
| Basic veterinary supplies | [`health.medicine`](../health/medicine.md) | Iodine, antibiotics, dewormers |
| Shelter for calving and extreme weather | [`construction`](../construction/index.md) | Three-sided barn or bedded-pack structure |
| Milking equipment (dairy operations) | [`ceramics.pottery`](../ceramics/pottery.md) | Buckets, straining cloth, cooling tank |

## Bill of Materials

Materials listed per 20-cow operation per year.

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Hay (winter feed) | 36-54 tonnes (plus 15% buffer) | [`agriculture`](../agriculture/index.md) — meadow hay | Silage (fermented forage) |
| Grain supplement | 2-4 tonnes | [`agriculture`](../agriculture/index.md) — oats, barley | Screened grain byproducts |
| Straw bedding | 40-60 tonnes/year | [`plants.fiber-plants`](../plants/index.md) | Sawdust, wood shavings |
| Salt/mineral mix | 200-400 kg | [`mining.extraction`](../mining/index.md) | Loose rock salt |
| Iodine solution (7%) | 2-4 L | [`health.medicine`](../health/medicine.md) | Betadine antiseptic |
| Fencing materials | Wire, posts, hardware | [`metals.iron-steel`](../metals/index.md) | Hedgerows, stone walls |
| Breeding bull or AI supplies | 1 bull per 25 cows | Natural service or [`health.medicine`](../health/medicine.md) | AI straws (requires liquid nitrogen) |


## Dairy Management

**Principle**: Cattle convert pasture and forage into milk — a complete protein food containing 3.2-5.5% butterfat, 3.0-4.0% protein, and 4.8% lactose. Milking stimulates continued lactation through a 305-day cycle, after which the cow is dried off for 60 days before calving again.

**Prerequisites**: Secure milking parlor or stanchion, clean water supply at 40-80 L/cow/day, feeding program delivering 14-18% crude protein, iodine-based teat dip (0.5-1% concentration).

**Materials**: Milking bucket (stainless steel or food-grade plastic), clean cloth for udder washing, strip cup for mastitis detection, teat dip solution, storage containers for milk.

**Procedure**:
1. Clean the udder with warm water and a clean cloth before milking.
2. Strip the first two streams from each teat into a strip cup — check for clots, discoloration, or watery appearance indicating mastitis.
3. Apply milking lubricant or dip teats in antiseptic solution (0.5-1% iodine).
4. Hand-milk using squeeze-and-press technique: grasp teat at base with thumb and forefinger (teat closure), squeeze progressively with remaining fingers to force milk downward. Release grip to allow refill. A skilled milker extracts 1-2 L/minute.
5. Strain milk through clean cloth into storage containers. Cool to 4°C within 30 minutes.
6. Dip teats in post-milking antiseptic to prevent mastitis.
7. Milk at 12-hour intervals for maximum yield.

**Pasteurization**: Raw milk carries *Brucella*, *Mycobacterium bovis*, *Listeria*, *E. coli* O157:H7, *Salmonella*, *Campylobacter*. Low-Temperature Long-Time (LTLT): 63°C for 30 minutes — suitable for batch processing. High-Temperature Short-Time (HTST): 72°C for 15 seconds — requires flow-through heat exchanger. Both achieve 5-log reduction in pathogens.

**Expected yield**: 6,000-10,000 L per 305-day lactation for Holsteins; 4,500-5,500 L for Jerseys. Peak production at 4-8 weeks post-calving: 25-35 L/day (Holstein) or 15-20 L/day (Jersey at 4.5-5.5% butterfat).

**Strengths**:
- Milk provides complete protein requiring no further processing for consumption
- Daily cash flow — milk income arrives every day unlike seasonal crop harvests
- Manure from dairy operation fertilizes 0.2-0.4 hectares per cow annually
- Whey byproduct from cheese making feeds pigs at 4-6 L/day per grower pig

**Weaknesses**:
- Requires twice-daily milking at fixed times — no flexibility in schedule
- Mastitis risk demands strict hygiene; infection reduces yield 10-30%
- High feed requirements: 0.4-0.6 kg dry matter per liter of milk produced
- Winter housing and stored feed necessary in cold climates (4-6 months/year)

## Beef Production

**Principle**: Cattle convert pasture and forage into meat through growth from calf to finished animal over 18-30 months. A 500 kg cow yields a dressed carcass of 55-60% (275-300 kg), breaking down into 45-50% retail cuts, 15-20% bone, and 10-15% fat trim.

**Prerequisites**: Adequate pasture (0.5-2.0 ha per animal), winter feed supply, basic handling facilities for sorting and loading, access to slaughter and processing equipment.

**Materials**: Pasture grasses and legumes, supplemental grain for finishing (2-4 kg/day during final 60-120 days), mineral supplement, fencing materials.

**Procedure**:
1. Cow-calf phase: calf nurses on cow for 6-8 months, gaining 0.8-1.2 kg/day. Begin grazing at 2-3 weeks.
2. Wean at 6-8 months by separating calf from dam. Expect 2-3 days of vocalization and stress.
3. Stocker/yearling phase: graze on pasture, gaining 0.5-0.8 kg/day on good forage.
4. Finishing phase (last 60-120 days): increase energy ration — grain supplement or high-quality pasture to add fat cover and marbling. Gain 1.0-1.5 kg/day.
5. Slaughter at 18-24 months for grain-finished, 24-30 months for grass-finished. Target 450-650 kg live weight.

**Expected yield**: 270-400 kg dressed carcass per animal. 175-280 kg saleable retail cuts. Average daily gain on pasture: 0.7-1.0 kg/day (steers), 0.5-0.8 kg/day (heifers).

**Strengths**:
- Cattle convert low-quality forage on marginal land into high-value protein
- Minimal daily labor compared to dairy — primarily pasture management and occasional handling
- Byproducts (hide, tallow, bones, horns) have significant industrial value
- Manure produced during grazing fertilizes pasture in place

**Weaknesses**:
- Long production cycle (18-30 months) ties up capital and feed resources
- High total feed consumption: 12,000-15,000 kg forage dry matter per animal over lifetime
- Requires significant land area (0.5-2.0 ha per animal)
- Vulnerable to predation, disease, and weather events during long growth period

## Breeding and Calving

**Principle**: Cattle reproduction follows a 283-day gestation with targeted 365-day calving interval. Calves are born precocial — standing within 30 minutes and nursing within 2-4 hours. Passive immunity transfers through colostrum (first milk containing immunoglobulins).

**Prerequisites**: Breeding-age heifers (14-18 months, 60-65% mature weight) or mature cows. Breeding bull at 1:25 bull-to-cow ratio, or AI supplies. Calving pens (1.5 × 2.0 m per pen). Iodine solution (7%) for navel dipping.

**Materials**: Iodine solution (7%), clean straw for bedding, calf bottles or tube feeder for assisted nursing, ear tags or marking supplies, breeding records ledger.

**Procedure**:
1. Introduce bull to cow herd or perform AI 60-80 days postpartum for 365-day calving interval.
2. Monitor for signs of approaching calving: udder filling (2-4 weeks prior), pelvic ligament relaxation (24-48 hours), mucus discharge, restlessness.
3. Move calving cow to individual pen with clean straw bedding.
4. Observe Stage 1 labor (dilation, 2-6 hours) and Stage 2 (delivery). Intervene if no progress after 1 hour of active straining.
5. Clear fetal membrane from calf's nose. Dry calf vigorously.
6. Dip navel in 7% iodine solution within 15 minutes of birth.
7. Ensure calf nurses colostrum within 2-4 hours — test that the calf has suckled by palpating the abdomen.
8. Monitor cow for retained placenta (should pass within 12 hours).

**Expected yield**: One calf per pregnancy (twins in 1-2% of births). Calf birth weight: 30-45 kg. Conception rate: 50-70% per AI service; 85-95% natural service per breeding season.

**Strengths**:
- Single calf per birth simplifies management compared to litters
- Strong maternal instincts — most cows calve without assistance
- Calves grow rapidly on cow's milk alone (0.8-1.2 kg/day gain)
- Natural breeding requires no specialized equipment

**Weaknesses**:
- Long gestation (283 days) limits reproductive rate to one calf per year
- Dystocia (difficult birth) risk in first-calf heifers — requires monitoring
- Calf mortality 5-10% in first week (hypothermia, scours, inadequate colostrum)
- Bull handling poses significant safety risk (800 kg animal, unpredictable)

## Ox Training for Draft Power

**Principle**: Castrated male cattle (oxen) trained to pull loads provide sustained traction at 0.5-0.75 HP per animal. Oxen are slower than horses but stronger pound-for-pound, thrive on roughage alone, and have calmer temperaments. Training begins at 1-2 years and takes 2-3 years to produce a fully trained team.

**Prerequisites**: Castrated male calves (6-12 months old), halter and lead rope, yoke materials (hardwood beam 10 × 12 cm, 1.2-1.5 m long), wooden bows (5 cm diameter). See [`animals.draft-power`](draft-power.md) for full harnessing details.

**Materials**: Leather or rope halter, hardwood yoke beam (oak, ash, or hickory), wooden bows, draft chain or rope, light drag (log or sled) for initial training.

**Procedure**:
1. **Year 1-2**: Halter break calves. Teach leading, standing tied, basic handling. Accustom to voice commands ("gee" right, "haw" left, "whoa" stop, "get up" forward). Handle feet and legs.
2. **Year 2**: Introduce yoke. Begin with empty drag on flat ground. Short sessions of 15-30 minutes. Pair with experienced ox — cattle learn by following.
3. **Year 3-4**: Gradually increase load and duration. A mature ox team pulls 1,500-2,500 kg on wheeled cart on flat ground, or plows 0.5-1.0 hectares/day with single-bottom plow.
4. Working speed: 3-4 km/hour, 6-8 hours/day with rest breaks. Supplement with 2-4 kg grain on working days.

**Expected yield**: A trained ox team (2 animals, 600-800 kg each) replaces 4-6 human laborers for plowing, hauling, and timber extraction. One ox pulls 10-15% of body weight sustained.

**Strengths**:
- Oxen thrive on roughage alone — no grain required for maintenance
- Calm temperament makes them safer than horses for repetitive work
- Durable working life of 8-12 years
- Yoke construction requires only wood and basic tools

**Weaknesses**:
- Training takes 2-3 years before productive work begins
- Slower working speed than horses (3-4 km/h vs 6-8 km/h)
- Cannot sweat efficiently — require rest and shade in heat above 30°C
- Single ox out of service sidelines the entire team

## Pasture and Feed Management

**Principle**: Cattle are ruminants that convert cellulose in grasses and legumes into energy through microbial fermentation in the rumen. Rotational grazing management optimizes forage utilization, prevents overgrazing, distributes manure evenly, and reduces parasite loads.

**Prerequisites**: Fenced pasture divided into 6-12 paddocks (temporary electric or permanent fencing), water access in each paddock, hay-making equipment or manual labor for winter feed harvest.

**Materials**: Electric fencing or permanent woven wire fence, fence posts, water troughs, hay-making tools (scythe, rake, or mechanical mower/baler), storage structure for hay.

**Procedure**:
1. Divide pasture into 6-12 paddocks. Rotate cattle every 3-7 days.
2. Allow grazed paddocks 21-35 days recovery before re-grazing.
3. Stock at 0.5-1.0 animal per hectare on good grassland (2-3 ha per animal on marginal land).
4. Cut hay at early heading stage (maximum protein). Sun-dry to 15-20% moisture (2-4 days).
5. Store hay under cover at below 18% moisture. Above 25% moisture, spontaneous combustion risk within 3-7 days.
6. Feed 1.2-1.8 tonnes hay per animal per winter (5-6 month temperate feeding period).
7. Supplement with grain (2-4 kg/day) for working oxen or lactating dairy cows.

**Expected yield**: Well-managed temperate pasture produces 6-12 tonnes dry matter per hectare per year, supporting 1.5-2.5 cattle per hectare during grazing season. Legume content of 25-35% fixes 80-150 kg N per hectare per year.

**Strengths**:
- Cattle convert cellulose (indigestible to humans) into high-value protein
- Manure deposited during grazing fertilizes pasture in place
- Rotational grazing suppresses parasites without chemical treatment
- Mixed grass-clover pasture sustains productivity without synthetic fertilizer

**Weaknesses**:
- Requires significant land area — cattle are the most land-intensive livestock
- Winter feed storage (36-54 tonnes for 20 cows) demands barns and labor
- Drought reduces pasture productivity by 40-60%, requiring supplemental feed
- Overgrazing degrades pasture rapidly — recovery takes 1-3 years


## Production Benchmarks by Breed Type

| Parameter | Holstein (Dairy) | Jersey (Dairy) | Hereford (Beef) | Dual-Purpose |
|-----------|------------------|----------------|-----------------|--------------|
| Mature weight (kg) | 550-700 | 350-450 | 550-800 | 450-650 |
| Daily milk yield (L) | 25-35 | 15-20 | — | 8-12 |
| Butterfat (%) | 3.2-3.6 | 4.5-5.5 | — | 3.8-4.5 |
| Daily gain on pasture (kg) | — | — | 0.7-1.0 | 0.5-0.8 |
| Dressing percentage (%) | — | — | 60-65 | 55-60 |
| Feed DM per day (kg) | 18-25 | 12-17 | 12-20 | 12-18 |
| Feed cost per L milk ($) | 0.15-0.25 | 0.12-0.20 | — | 0.20-0.35 |

## Scale Estimates per 20-Cow Operation

| Output | Annual Quantity | Notes |
|--------|----------------|-------|
| Milk (10 dairy cows) | 60,000-100,000 L | From Holstein or Jersey herd |
| Beef (surplus calves + culls) | 2,000-3,000 kg | 8-12 animals slaughtered |
| Manure | 150-250 tonnes | Fertilizes 5-15 hectares |
| Draft power (4 oxen) | 1,000-1,500 hours | Plowing, hauling, timber |
| Tallow | 100-200 kg | From rendered fat |
| Leather (hides) | 8-12 hides | 3-5 m² each after tanning |

## Scaling Notes

A founding herd of 10-15 cattle (8-10 cows, 2-3 heifers, 1-2 bulls) expands to 40-60 head within 8-10 years using natural service at a 1:25 bull-to-cow ratio. Expansion is limited by feed supply and winter housing capacity — each additional animal requires 0.5-2.0 hectares of pasture and 1.2-1.8 tonnes of stored hay.

**Minimum economic scale**: 2-3 dairy cows provide 15-30 L milk/day for a household. 5-6 beef cows on 5-10 hectares produce 2-3 slaughter animals per year. A trained ox team (2 animals) plows 0.5-1.0 hectares/day.

**Scale bottlenecks**: Winter feed storage limits herd size more than summer pasture. A 20-cow herd requires 41-62 tonnes of stored hay, requiring 80-120 m² of hayloft space. Water supply must deliver 800-1,600 L/day. Milking labor scales linearly — one person can hand-milk 10-15 cows in 1.5-2 hours per session.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low milk yield | Insufficient feed protein, mastitis, or heat stress | Increase grain supplement to 4-6 kg/day; test for mastitis with CMT; provide shade and water above 30°C |
| Calving difficulty | Oversized calf or heifer too small | Monitor heifer body condition at calving (BCS 3.0-3.5); assist delivery if no progress after 1 hour of straining |
| Scours (calf diarrhea) | *E. coli*, *Cryptosporidium*, or *Salmonella* | Ensure adequate colostrum (2-4 L within 4 hours); isolate affected calves; electrolyte therapy |
| Bloat (rumen distension) | Grazing legume-rich pasture (alfalfa, clover) | Provide dry hay before turning onto legume pasture; anti-foaming agent (poloxalene) in water |
| Poor weight gain | Internal parasites, insufficient pasture, low-quality hay | Fecal egg count; deworm with ivermectin; supplement with grain; test hay protein content |
| Retained placenta | Deficient selenium/vitamin E, difficult birth, infection | Do not force removal; monitor for fever (>39.5°C indicates metritis); antibiotics if infected |

## Safety

**Bull handling**: Never enter a pen with a bull alone. A 800 kg bull charging at 35 km/h delivers massive blunt force. Use a bull staff (rigid pole with snap latch attached to nose ring) for control. Signs of aggression: pawing ground, head rubbing, broadside display, vocalizing. Breeding bulls require dedicated escape-proof pens with heavy gates.

**Crush and restraint**: Cattle handling requires a crush (squeeze chute) — a strong frame with head catch and squeeze panels. A properly designed race (curved, solid-sided) uses cattle's natural circling behavior to move them forward calmly. Never use dogs on cattle — stress raises cortisol and reduces immune function.

**Zoonotic diseases**: Brucellosis transmits through raw milk and birthing fluids (causes undulant fever in humans). Leptospirosis transmits via urine. Q fever (*Coxiella burnetii*) transmits from birthing fluids — causes flu-like illness. Cryptosporidiosis causes diarrhea from contact with manure. Wear gloves when handling birthing materials or manure. Pasteurize all milk. Wash hands after handling cattle.

**Kicking and crushing**: Cows kick forward and to the side (unlike horses, which kick backward). Stand to the side when working near the rear. Never stand behind a cow in a confined space. A 500 kg animal stepping on a foot causes serious injury — wear reinforced boots with steel toe caps.

## Quality Control

**Milk quality**: Test for mastitis at every milking using strip cup (visual inspection for clots or discoloration) or California Mastitis Test (CMT reagent reacts with somatic cells). Somatic cell count (SCC) below 200,000/mL indicates healthy udder. Above 500,000/mL indicates infection. Bacterial count below 20,000 CFU/mL for Grade A milk. Cool milk to 4°C within 30 minutes of milking.

**Beef quality**: Dressing percentage 60-65% indicates proper slaughter technique. Fat cover (grade 2-3 on 5-point scale) indicates adequate finishing. Meat pH below 5.8 at 24 hours post-slaughter indicates proper handling (pH above 6.0 indicates stress before slaughter — dark-cutting beef). Age meat at 0-4°C for 10-14 days for optimal tenderness.

**Breeding records**: Track breeding date, expected calving date (+283 days), actual calving date, calf birth weight, calving ease score (1-5), and rebreeding date. Target calving interval under 370 days. Cull cows failing to conceive within 90 days postpartum or producing below 70% of herd average.

## Variations and Alternatives

**Tropical adaptation**: Zebu-type breeds (*Bos indicus*) — Brahman, Nelore, Gir — tolerate 25-35°C with sweat glands 3-4× denser than *Bos taurus*, loose skin for cooling, and resistance to ticks and tropical parasites. Brahman crossbreeds (Brangus: 3/8 Brahman × 5/8 Angus) combine tropical adaptation with meat quality.

**Cold climate**: Highland cattle grow a double coat (outer guard hair 20-30 cm, dense woolly undercoat) insulating to -40°C. They require 20-30% less feed energy for thermoregulation than shorthaired breeds. Galloway cattle similarly thrive in cold, wet conditions.

**Arid regions**: Afrikaner and Tuli breeds survive on browse and sparse grass, requiring water only every 2-3 days (vs daily for European breeds). Stocking rates: 5-15 hectares per animal.

**Mountain systems**: Brown Swiss and Tyrol Grey navigate slopes up to 30° and produce 4,000-6,000 L milk on alpine pasture at 1,000-2,000 m elevation. Transhumance (seasonal movement between lowland and mountain pasture) eliminates need for winter housing.

**Bison alternative**: American bison (*Bison bison*) produce leaner meat (2-3% fat vs 10-15% for beef) on grass alone with no grain finishing and minimal disease susceptibility. See [`animals.bison`](bison.md). Bison require stronger fencing and handling facilities due to wilder temperament.

## Cross-Domain Links

- [`animals.domestication`](domestication.md) — livestock principles: housing, nutrition, breeding, herd health
- [`animals.draft-power`](draft-power.md) — ox training, yoke construction, hitching systems, load calculations
- [`animals.animal-materials`](animal-materials.md) — tallow rendering, leather tanning, horn and bone working
- [`food-processing`](../food-processing/index.md) — butter, cheese, and fermented milk products from raw milk
- [`agriculture`](../agriculture/index.md) — pasture management, crop rotation, manure as fertilizer
- [`health.medicine`](../health/medicine.md) — disease treatment, vaccination, veterinary supplies


[← Back to Animals](index.md)
