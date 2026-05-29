# Sheep (*Ovis aries*)

> **Node ID**: animals.sheep
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`animals.domestication`](domestication.md)
> **Enables**: [`animals.animal-materials`](animal-materials.md), [`textiles.fibers`](../textiles/fibers.md), [`foundations.food-agriculture`](../foundations/food-agriculture.md)
> **Timeline**: Years 1-25+
> **Outputs**: wool, mutton, milk, lanolin, sheepskins, manure
> **Critical**: Yes — premier fiber and meat species with lowest infrastructure requirements

## Overview

Sheep are the most versatile small ruminant for a bootstrapping civilization — producing wool (the premier natural fiber for textiles), meat (lamb and mutton), milk (for cheese and fermented products), and pelts. Their modest size (mature weight 60-120 kg depending on breed) makes them easier to handle than cattle, and their gregarious flocking instinct simplifies herding. Gestation is 147 days (range 144-152), with typical litters of singles for hill breeds, twins for lowland breeds, and occasional triplets. A well-managed flock of 50-100 ewes on 10-15 hectares of improved pasture can sustain a small community with food, fiber, and fertilizer.

Sheep are particularly valuable in early-stage agriculture because they graze closer to the ground than cattle, utilize vegetation that cattle refuse, and produce nitrogen-rich manure (0.7% N fresh weight, 2-3 kg/day per animal) that builds soil fertility. Their relatively low infrastructure requirements — simple shelters for winter and lambing, basic fencing — make them accessible at an early stage of development.

| Parameter | Value | Notes |
|-----------|-------|-------|
| Mature weight | 60-120 kg | Breed dependent |
| Gestation | 147 days (range 144-152) | Singles, twins, or triplets |
| Lambing interval | 8 months (accelerated) to 12 months | Annual lambing most common |
| Daily dry matter intake | 1.5-3.0 kg | 2.5-3.0% of body weight |
| Daily water intake | 4-10 L | More in hot conditions |
| Manure production | 2-3 kg/day | 0.7% N, 0.3% P, 0.6% K |
| Wool yield | 2-8 kg greasy fleece/year | Depends on breed |
| Productive lifespan | 5-7 lambing seasons | Lowland breeds |

## Prerequisites

| Requirement | Source | Notes |
|-------------|--------|-------|
| Fencing (woven wire 1.0-1.2 m or electric) | [`foundations.tools-basic`](../foundations/tools-basic.md) | Sheep respect fencing better than goats |
| Basic shelter for lambing and winter | [`construction`](../construction/index.md) | Three-sided shed sufficient in most climates |
| Stored winter feed | [`agriculture`](../agriculture/index.md) | 150-250 kg hay per ewe per winter |
| Clean water supply | [`water`](../water/index.md) | 4-10 L per ewe per day |
| Shearing equipment | [`foundations.tools-basic`](../foundations/tools-basic.md) | Hand shears or mechanical clippers |
| Basic veterinary supplies | [`health.medicine`](../health/medicine.md) | Iodine, dewormer, antibiotics |
| Guardian animal or fencing for predators | [`animals.pest-management`](pest-management.md) | LGD, donkey, or llama |

## Bill of Materials

Materials listed per 50-ewe flock per year.

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Hay (winter feed) | 7.5-12.5 tonnes | [`agriculture`](../agriculture/index.md) | Silage, crop residues |
| Grain supplement (late pregnancy) | 1.5-3.0 tonnes | [`agriculture`](../agriculture/index.md) | Screened grain byproducts |
| Salt/mineral mix | 100-200 kg | [`mining`](../mining/index.md) | Loose rock salt |
| Straw bedding | 2-4 tonnes | [`plants`](../plants/index.md) | Wood shavings |
| Shearing equipment | Hand shears or clippers | [`foundations.tools-basic`](../foundations/tools-basic.md) | Mechanical clippers if power available |
| Dewormer (anthelmintic) | 1-3 L | [`health.medicine`](../health/medicine.md) | Pasture rotation as primary control |
| Iodine solution (7%) | 0.5-1 L | [`health.medicine`](../health/medicine.md) | Other antiseptics |
| Lambing pens (1.5-2.0 m² each) | 5-8 pens | [`foundations.tools-basic`](../foundations/tools-basic.md) | Portable panels or straw bales |

## Process Description

## 4.1 Wool Production

**Principle**: Sheep produce a fleece of keratin fiber that grows continuously and is harvested annually by shearing. Wool fibers have natural crimp (wave pattern) and scales that interlock during spinning and felting, creating strong yarn and fabric. The fleece also contains lanolin (wool wax) that protects the fiber and has industrial applications.

**Prerequisites**: Shearing equipment (hand shears or mechanical clippers), clean shearing floor, burlap or paper for fleece storage, basic knowledge of shearing technique.

**Materials**: Hand shears (blade shears) or mechanical clippers, sharpening stone, fleece skirts (table or frame), burlap bags for fleece storage.

**Procedure**:
1. Shear once per year in spring before lambing or shortly after.
2. Lay the sheep on its hip in a sitting position (sheep become calm and immobile in this posture).
3. Work in a systematic pattern: belly first (separate, lower grade), then long blows from the hindquarters forward along the back and sides.
4. Keep the skin stretched flat with the free hand to prevent cuts.
5. Remove the complete fleece in one piece ("the blanket").
6. Skirt the fleece (remove belly wool, stained wool, and vegetable matter).
7. Roll and store in breathable bags.
8. A professional shearer processes 100-200 sheep/day with mechanical shears; hand shears manage 20-40/day.

**Expected yield**: 2-5 kg greasy (unwashed) fleece per shearing, yielding 60-70% clean fiber after scouring. Merino: 4-6 kg greasy at 65-70% clean yield. Longwool breeds: 5-8 kg greasy at 75-80% clean yield. Lanolin recovery: 10-15% of greasy fleece weight (500-750 g per 5 kg fleece).

**Strengths**:
- Wool stores indefinitely without degradation — no rush to process
- Shearing requires no special facilities — flat clean floor suffices
- Lanolin recovered from scouring provides water-repellent and lubricant
- Multiple grades obtainable: fine (under 19 microns) for garments, coarse (25+ microns) for carpets

**Weaknesses**:
- Requires annual shearing — neglected fleece causes heat stress and flystrike
- Hand shearing is physically demanding (back, wrist, shoulder strain)
- Greasy fleece contains 25-40% impurities requiring scouring before use
- Wool prices fluctuate widely ($3-30/kg depending on micron and quality)

## 4.2 Lambing Management

**Principle**: Sheep give birth after 147 days of gestation. Lambs are precocial — standing and nursing within 30 minutes. Colostrum (first milk) provides passive immunity. Lambing percentage (lambs born per ewe) ranges from 100% (hill breeds, singles) to 300% (prolific breeds, twins and triplets).

**Prerequisites**: Lambing pens (1.5-2.0 m² each), iodine solution (7%), clean straw bedding, heat lamp for cold weather, colostrum substitute or frozen supply.

**Materials**: Iodine solution (7%), clean towels for drying lambs, feeding tube for weak lambs, ear tags or marking supplies, record book.

**Procedure**:
1. Bring ewes into lambing pens 1-2 days before expected lambing.
2. Monitor closely during lambing season — check every 2-3 hours.
3. If a ewe strains for 30-60 minutes without progress, check presentation. Normal: front feet first, nose on knees.
4. Clear fetal membranes from lamb's nose immediately after birth.
5. Dry lamb vigorously with clean towel in cold weather.
6. Dip navel in 7% iodine solution within 15 minutes.
7. Ensure lamb nurses colostrum within 2 hours — palpate lamb's abdomen to confirm full stomach.
8. If lamb won't nurse, tube-feed colostrum (30-50 mL per kg body weight in first feeding).
9. Keep ewe and lamb in pen for 24-48 hours to bond before turning out.

**Expected yield**: Lambing percentage 100-300% depending on breed. Lamb birth weight: 2.5-5.0 kg. Lamb mortality target: under 10% (intensive) to 15-25% (extensive/pasture lambing).

**Strengths**:
- Strong maternal instincts — most ewes lamb without assistance
- Short gestation (147 days) allows flexible breeding schedules
- Lambs grow rapidly: 250-350 g/day on good pasture
- Multiple births (twins common) increase output per ewe

**Weaknesses**:
- Predation risk high during lambing — foxes, coyotes, eagles target newborns
- Hypothermia kills lambs in cold, wet weather within hours
- Mastitis and pregnancy toxemia threaten ewe health in late gestation
- mismothering (ewe rejecting a lamb) requires intervention or fostering

## 4.3 Meat Production

**Principle**: Lambs convert pasture to meat with dressing percentages of 45-55%. Growth from birth to slaughter takes 4-12 months depending on system and target weight. Sheep produce three categories: lamb (under 12 months), hogget (12-24 months), and mutton (over 24 months).

**Prerequisites**: Adequate pasture for lamb growth, finishing ration if targeting grain-finished lamb, basic handling and sorting facilities.

**Materials**: Pasture or finishing ration, mineral supplement, handling and loading facilities.

**Procedure**:
1. Lambs nurse for 6-8 weeks, then wean onto pasture.
2. Target daily gain: 250-350 g/day for singles, 200-280 g/day for twins.
3. Slaughter at 35-50 kg live weight for lamb (4-6 months on good pasture).
4. Process: bleed, skin, eviscerate, chill to 4°C within 1 hour.
5. Dressing percentage: 45-55% (17-25 kg carcass from 35-50 kg live lamb).

**Expected yield**: 17-25 kg dressed carcass per lamb. A flock of 50 ewes at 170% lambing produces 1,530-2,125 kg carcass per year.

**Strengths**:
- Fast growth — market weight in 4-6 months on pasture alone
- Multiple market classes (lamb, hogget, mutton) provide flexibility
- Sheep utilize vegetation that cattle refuse — no competition for the same forage
- Carcass byproducts (pelt, tallow, bone meal) have additional value

**Weaknesses**:
- Lower dressing percentage than cattle or pigs (45-55% vs 55-80%)
- Fat cover varies with season and forage quality
- Stronger flavor in older animals limits mutton market
- Predation and parasite losses reduce effective yield

## 4.4 Flock Health and Parasite Management

**Principle**: Sheep are susceptible to internal parasites (especially *Haemonchus contortus*), foot rot, and flystrike. Integrated management combining pasture rotation, targeted treatment, and monitoring maintains flock health without relying solely on chemical dewormers.

**Prerequisites**: Fencing for rotational grazing (6-8 paddocks), foot bath (copper sulfate or zinc sulfate), FAMACHA scoring card, basic knowledge of parasite life cycles.

**Materials**: Dewormer (ivermectin, fenbendazole, or levamisole), copper sulfate (5-10% solution for foot bath), FAMACHA card, sharps for injections.

**Procedure**:
1. Rotate pastures every 3-5 days. Rest paddocks 60-90 days (parasite larvae die without host).
2. FAMACHA scoring every 2-4 weeks during parasite season: check inner lower eyelid color. Treat only scores 3-5.
3. Foot bath monthly in wet seasons: run sheep through 10-15 cm deep copper sulfate solution, stand 5-10 minutes.
4. Trim hooves every 3-4 months. Pare away diseased horn. Apply copper sulfate paste to infected feet.
5. Crutch (shear breech area) 2-4 weeks before lambing to prevent flystrike.
6. Monitor for flystrike daily in warm weather — blowflies lay eggs in soiled wool.

**Expected results**: Target parasite egg count below 500 EPG (eggs per gram feces). Foot rot incidence below 5% of flock. Lamb mortality under 10%.

**Strengths**:
- FAMACHA scoring requires no laboratory equipment — visual assessment only
- Pasture rotation controls parasites without chemicals
- Mixed grazing with cattle "vacuums" sheep parasite larvae from pasture
- Targeted treatment (only affected animals) slows dewormer resistance

**Weaknesses**:
- Barber pole worm (*Haemonchus*) develops dewormer resistance rapidly
- Foot rot spreads quickly in wet conditions — entire flock can be affected in weeks
- Flystrike kills sheep within 48-72 hours if undetected
- Labor-intensive monitoring during parasite season (2-4 week intervals)

## Quantitative Parameters

## Production Benchmarks by Breed Type

| Parameter | Merino (Wool) | Suffolk (Meat) | East Friesian (Dairy) | Corriedale (Dual) |
|-----------|--------------|----------------|----------------------|-------------------|
| Mature weight (kg) | 50-80 | 80-120 | 70-90 | 60-90 |
| Fleece weight greasy (kg) | 4-6 | 2-3 | 3-5 | 4-6 |
| Fiber diameter (microns) | 17-24 | 28-33 | 25-32 | 25-32 |
| Lambing percentage (%) | 100-130 | 150-180 | 200-300 | 150-180 |
| Milk yield (L/lactation) | — | — | 400-600 | — |
| Daily gain lambs (g/day) | 150-200 | 300-400 | 250-350 | 250-350 |
| Feed DM per day (kg) | 1.5-2.5 | 2.0-3.0 | 2.5-3.5 | 2.0-3.0 |

## Scale Estimates per 50-Ewe Flock

| Output | Annual Quantity | Notes |
|--------|----------------|-------|
| Lamb carcass | 1,530-2,125 kg | 85 lambs at 18-25 kg each |
| Wool (greasy) | 200-400 kg | 4-8 kg per ewe |
| Manure | 36-55 tonnes | Fertilizes 2-5 hectares |
| Sheep milk (dairy flock) | 20,000-30,000 L | East Friesian breed only |

## Scaling Notes

A founding flock of 10-20 ewes and 1-2 rams expands to 50-100 head within 4-5 years at 150% lambing with 85% weaning rate. Expansion is limited by pasture area and winter feed — each ewe needs 0.1-0.3 hectares of improved pasture during grazing season and 150-250 kg of hay for winter.

**Minimum economic scale**: 5-10 ewes provide 8-20 lambs and 20-60 kg wool per year — sufficient for household meat and fiber. 25 ewes on 2-3 hectares is a viable smallholder operation.

**Scale bottlenecks**: Predator protection scales poorly — one guardian dog per 50-200 sheep. Shearing is a peak labor demand (1-2 days per 50 ewes). Winter feeding requires 7.5-12.5 tonnes hay storage per 50 ewes.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low lambing percentage | Ewes too thin at breeding, ram infertility | Body condition score 3.0-3.5 at breeding; fertility test rams |
| Lamb deaths in first week | Hypothermia, inadequate colostrum, predation | Provide shelter at lambing; ensure colostrum within 2 hours; guardian animals |
| Weight loss in ewes | Internal parasites, inadequate nutrition | Fecal egg count; deworm; increase grain to 0.3-1.0 kg/day in late pregnancy |
| Flystrike | Soiled wool attracting blowflies | Crutch breech area; apply preventative; check daily in warm weather |
| Wool break (tender fleece) | Illness or nutritional stress during growth | Maintain consistent nutrition; avoid sudden feed changes during fiber growth |
| Foot rot | Wet conditions, infected animals | Foot bath in 5-10% copper sulfate weekly; cull chronically infected ewes |

## Safety

**Ram handling**: Rams can be aggressive during breeding season (autumn). A charging ram knocks adults down and causes serious injury. Signs of aggression: lowering head, pawing, charging. Never turn your back on a ram. Use a handling shield or staff. A spray bottle of water to the face interrupts a charge.

**Shearing injuries**: Hand shears or clippers cut skin on both sheep and shearer. Keep blades sharp — dull blades require more pressure and cause tears. Treat cuts on sheep immediately with iodine antiseptic. Shearers risk back injury from repetitive lifting — use legs, not back, when positioning sheep.

**Zoonotic diseases**: Orf (contagious ecthyma — parapoxvirus causing painful sores on hands), Q fever (*Coxiella burnetii* — flu-like illness from birthing fluids), listeriosis (from contaminated silage). Wear gloves when handling sheep with sores, during lambing, and when processing fleece. Wash hands thoroughly.

**Quarantine**: New animals quarantined 30 days and tested for foot rot, caseous lymphadenitis, ovine progressive pneumonia, and scrapie before flock introduction. A single infected introduction can devastate a naive flock.

## Quality Control

**Wool grading**: Classify fleece by fiber diameter (microns), staple length, crimp, color, vegetable matter contamination, and strength. Test for tender break (fibers break along a line, caused by illness or stress during growth). Target: under 19 microns for fine wool ($12-25/kg), 25-32 microns for medium wool ($4-8/kg).

**Meat grading**: Carcass classified by conformation (EUROP scale) and fat cover (1-5). Premium carcasses (E/R conformation, fat class 2-3L) yield 70-80% saleable meat. Over-fat carcasses (4-5) yield only 55-65%.

**Lamb growth monitoring**: Weigh at birth, 4 weeks, 8 weeks, weaning (12-16 weeks), and target slaughter. Lambs failing 200 g/day gain should be checked for parasites, insufficient milk, or poor pasture.

**Flock records**: Track lambing date, litter size, birth weights, weaning weights per ewe. Calculate kg of lamb weaned per ewe per year. Target: 60-80 kg. Cull ewes producing below flock average for two consecutive years.

## Variations and Alternatives

**Hill and mountain systems**: Hill breeds (Scottish Blackface, Welsh Mountain, Swaledale) thrive on nutrient-poor grazing at 300-900 m elevation. Ewes weigh 45-60 kg, produce 1.5-2.5 kg fleeces, but survive on pasture that would starve any other livestock. Transhumance — seasonal movement between lowland winter and mountain summer pasture — requires no winter housing.

**Arid rangeland**: Dorper, Rambouillet, and Navajo Churro tolerate annual rainfall below 400 mm and temperatures from -10 to 45°C. Stocking rates: 1-3 sheep per hectare on arid rangeland (vs 10-15 on improved temperate pasture). Awassi and Blackhead Persian breeds drink saline water (up to 10,000 ppm TDS) and require watering only every 2-3 days.

**Temperate improved pasture**: Most productive systems on improved pasture — 10-15 ewes per hectare with rotational grazing produce 150-250 kg lamb carcass per hectare annually. New Zealand all-grass system produces lamb at $2.50-3.50/kg carcass with no grain feeding.

**Goat alternative**: Goats browse rather than graze, preferring woody vegetation. Mixed sheep-goat grazing utilizes both pasture types. See [`animals.goats`](goats.md).

## Cross-Domain Links

- [`animals.domestication`](domestication.md) — livestock principles: housing, nutrition, breeding, health fundamentals
- [`animals.animal-materials`](animal-materials.md) — wool processing, leather tanning, lanolin extraction
- [`textiles.fibers`](../textiles/fibers.md) — scouring, carding, spinning, weaving, and felting wool into textiles
- [`food-processing`](../food-processing/index.md) — sheep milk cheese (pecorino, feta, Roquefort), yogurt
- [`agriculture`](../agriculture/index.md) — pasture management, crop residues as winter feed, manure as fertilizer
- [`animals.pest-management`](pest-management.md) — guardian dogs, predator control strategies


[← Back to Animals](index.md)
