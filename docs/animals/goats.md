# Goats (*Capra aegagrus hircus*)

> **Node ID**: animals.goats
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`animals.domestication`](domestication.md)
> **Enables**: [`textiles.fibers`](../textiles/fibers.md), [`foundations.food-agriculture`](../foundations/food-agriculture.md)
> **Timeline**: Years 1-20+
> **Outputs**: goat_milk, chevon, cashmere, mohair, goatskins, manure, brush_clearing
> **Critical**: No — versatile but replaceable by sheep/cattle combination


Goats are the most adaptable and resilient domesticated livestock species. They thrive in arid, mountainous, and marginal environments where cattle and sheep struggle, browsing on woody vegetation that other ruminants refuse. Mature weight ranges from 30-80 kg (does 30-55 kg, bucks 50-80 kg), making them manageable without specialized handling equipment. Gestation is 150 days (range 145-155), producing litters of 1-3 kids with twins as the most common outcome. A doe's productive lifespan is 8-12 years.

Goats produce milk that is more digestible than cow milk (smaller fat globules, different protein structure), meat (chevon) with a dressed yield of 45-50%, and specialty fibers (cashmere, mohair) that are among the most valuable natural textile fibers. Their browsing behavior makes them excellent brush clearers — 8-12 goats per hectare on browse can suppress invasive woody plants and reclaim overgrown land for cultivation.

| Parameter | Value | Notes |
|-----------|-------|-------|
| Mature weight (does) | 30-55 kg | Breed dependent |
| Mature weight (bucks) | 50-130 kg | Boer bucks heaviest |
| Gestation | 150 days (range 145-155) | Twins most common |
| Daily dry matter intake | 1.5-3.0 kg | 3-4% of body weight |
| Daily water intake | 4-8 L | 10-15 L during lactation |
| Manure production | 1.5-2.5 kg/day | 0.6-0.7% N fresh weight |
| Milk yield (Saanen) | 3-5 L/day peak | 600-1,200 L per lactation |
| Productive lifespan | 8-12 years | Doe |

## Prerequisites

| Requirement | Source | Notes |
|-------------|--------|-------|
| Secure fencing (1.2-1.5 m, mesh under 15 cm) | [`foundations.tools-basic`](../foundations/tools-basic.md) | Goats climb, push, dig |
| Basic shelter (three-sided) | [`construction`](../construction/index.md) | Draft-free, dry |
| Browse or pasture access | [`agriculture`](../agriculture/index.md) | Goats prefer woody browse |
| Stored winter feed | [`agriculture`](../agriculture/index.md) | Hay, 150-250 kg per doe per winter |
| Clean water supply | [`water`](../water/index.md) | 4-8 L/day, 10-15 L during lactation |
| Milking stand (dairy) | [`foundations.tools-basic`](../foundations/tools-basic.md) | Elevated platform with head catch |

## Bill of Materials

Materials listed per 20-doe operation per year.

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Hay (winter feed) | 3-5 tonnes | [`agriculture`](../agriculture/index.md) | Browse, silage |
| Grain supplement (milking does) | 1-2 tonnes | [`agriculture`](../agriculture/index.md) | Screened grain byproducts |
| Salt/mineral mix | 50-100 kg | [`mining`](../mining/index.md) | Loose rock salt |
| Fencing materials | 1,200-1,500 m perimeter | [`metals`](../metals/index.md) | Electric netting for paddocks |
| Iodine solution (7%) | 0.5 L | [`health.medicine`](../health/medicine.md) | Other antiseptic |
| Disbudding iron (dairy kids) | 1 tool | [`metals`](../metals/index.md) | Required for hornless dairy goats |


## Dairy Management

**Principle**: Dairy goats convert browse and forage into milk with 3.2-5.0% butterfat, depending on breed. Goat milk has smaller fat globules (2-3 microns vs 3-4 for cow milk) and different casein structure, making it naturally homogenized and more digestible for many people.

**Prerequisites**: Milking stand with head catch, stainless steel or food-grade buckets, straining cloth, cooling vessel, 12-hour milking interval schedule.

**Materials**: Milking stand, straining cloth or filter, clean buckets, iodine-based teat dip, cooling container, thermometer.

**Procedure**:
1. Milk at 12-hour intervals for maximum yield.
2. Clean udder with warm water before milking. Strip first streams to check for mastitis.
3. Hand-milk using squeeze-and-press technique (same as cow milking but faster per animal).
4. Strain milk through fine mesh or cloth to remove hair and debris.
5. Cool to 4°C within 30-60 minutes.
6. Dip teats in iodine-based antiseptic post-milking.
7. Keep bucks separate from milking does — buck odor taints milk flavor.

**Expected yield**: Saanen: 3-5 L/day at peak, 600-1,200 L per 250-305 day lactation. Nubian: 2-3 L/day at 4.5-5.0% butterfat. Alpine: 2.5-4.0 L/day at 3.3-3.6% butterfat.

**Strengths**:
- Goat milk is naturally homogenized — cream does not separate as readily
- Higher cheese yield than cow milk: 9-12 kg cheese per 100 L (vs 8-10 kg for cow)
- Smaller animals require less feed and infrastructure than cattle
- Multiple breeds cover volume (Saanen) and high-component (Nubian) production

**Weaknesses**:
- Lower total volume per animal than cattle — need more animals for same output
- Buck odor contaminates milk if bucks are housed near milking does
- "Goaty" flavor results from poor hygiene, improper cooling, or buck proximity
- CAE (caprine arthritis encephalitis) reduces production in unmanaged herds

## Meat Production (Chevon)

**Principle**: Goat meat (chevon) is lean (2-3% fat vs 10-15% for beef), high in protein, and produced from kids reaching slaughter weight at 3-4 months on browse and pasture.

**Prerequisites**: Breeding does (Boer or Kiko for meat focus), buck at 1:25-30 ratio, pasture or browse access, basic handling facilities.

**Materials**: Pasture/browse access, supplemental grain (0.25-0.5 kg/day for growing kids), fencing.

**Procedure**:
1. Breed does to kid in spring (pasture kidding) or year-round in managed systems.
2. Kids nurse for 6-8 weeks while grazing with dam.
3. Wean at 8-10 weeks for accelerated breeding, or 12-14 weeks for natural systems.
4. Grow kids on pasture/browse to 30-40 kg live weight (3-4 months for Boer cross).
5. Slaughter: dispatch, bleed, skin, eviscerate, chill to 4°C within 1 hour.

**Expected yield**: 16-19 kg dressed carcass from 35 kg live kid (46-55% dressing percentage). Chevon is 75-80% lean by weight.

**Strengths**:
- Boer kids reach slaughter weight in 3-4 months — fastest land-mammal meat production after rabbits
- Goats thrive on browse where cattle and sheep cannot survive
- Very lean meat appeals to health-conscious consumers
- Low feed costs — browse is free, supplement only 0.25-0.5 kg/day

**Weaknesses**:
- Lower dressing percentage than cattle or pigs (46-55% vs 55-80%)
- Chevon benefits from moist-heat cooking (braising, stewing) — less versatile than beef
- Stronger flavor than lamb limits market in some cultures
- Predation risk higher than cattle due to smaller size

## Fiber Production (Mohair and Cashmere)

**Principle**: Angora goats produce mohair (long, lustrous, curly fiber). Cashmere-producing goats produce fine undercoat (down) shed in spring. Both are high-value specialty fibers.

**Prerequisites**: Angora goats (for mohair) or cashmere-type goats, shearing equipment (mohair) or combing tools (cashmere), fiber storage bags.

**Materials**: Shearing clippers or hand shears (mohair), fine-toothed comb (cashmere), burlap bags for fiber storage.

**Procedure — Mohair**:
1. Shear Angora goats twice per year (spring and autumn).
2. Shear to the skin in one piece ("the blanket").
3. Skirt fleece: remove stained, matted, and short fibers.
4. Store in breathable bags.
5. Yield: 4-6 kg per shearing for mature animals (8-12 kg/year).

**Procedure — Cashmere**:
1. Comb or shear cashmere goats in spring when down begins to shed.
2. Collect raw fleece containing fine down (under 18.5 microns) and coarse guard hairs (50-100 microns).
3. Dehair by mechanical separation — only 20-40% of raw weight is usable cashmere.
4. Yield: 100-300 g dehaired cashmere per goat per year.

**Expected yield**: Mohair: 8-12 kg/year per adult goat at 23-38 microns. Cashmere: 100-300 g dehaired fiber per goat per year at 14-16 microns.

**Strengths**:
- Mohair takes dye well, has silk-like sheen — commands premium for knitting yarns
- Cashmere is one of the finest natural fibers (14-16 microns) — highest value per gram
- Fiber stores indefinitely without processing
- Goats produce fiber while clearing brush — dual output from one animal

**Weaknesses**:
- Cashmere yield is very low (100-300 g/year) — requires large flocks for commercial production
- Dehairing cashmere is labor-intensive without mechanical equipment
- Angora goats are more delicate than other breeds — require better nutrition and shelter
- Mohair fiber diameter increases with age, reducing value of older animals

## Brush Clearing and Land Reclamation

**Principle**: Goats browse on woody vegetation (shrubs, saplings, brambles, invasive species) that other livestock refuse. Stocked at 8-12 goats per hectare on dense browse, they strip bark, defoliate shrubs, and suppress regrowth.

**Prerequisites**: Portable electric fencing or netting for paddock creation, guardian animal (dog, donkey, or llama) for predator protection, browse-targeted stocking rate.

**Materials**: Electric netting (1.0-1.2 m, 4,000-5,000 V), portable water trough, guardian animal.

**Procedure**:
1. Fence browse area into paddocks. Stock at 8-12 goats per hectare on dense brush.
2. Rotate every 2-4 weeks depending on browse density.
3. Goats strip bark from saplings, defoliate shrubs, consume multiflora rose, kudzu, blackberry.
4. Supplement with mineral and water. Goats obtain most nutrition from browse.
5. Monitor for toxic plants (rhododendron, azalea, yew — all lethal to goats).
6. A 30-goat flock on 3-4 hectares reduces canopy cover by 60-80% in one grazing season.

**Expected results**: 60-80% reduction in invasive brush canopy within one 90-120 day grazing season. 5-8 tonnes manure per hectare applied during clearing.

**Strengths**:
- Reclaims overgrown land for cultivation at $200-400/hectare (vs $500-1,500 mechanical clearing)
- Goats consume invasive species (kudzu, multiflora rose) that resist other control methods
- Simultaneously clears land and fertilizes it
- No equipment or fuel required — goats do the work

**Weaknesses**:
- Goats strip bark from valuable trees — protect orchard and timber trees with guards
- Browse must be sufficient — overstocked goats starve on cleared land
- Predator losses higher on brush than open pasture (cover for coyotes)
- Toxic plant risk — goats sample everything, including poisonous species


## Production Benchmarks by Breed Type

| Parameter | Saanen (Dairy) | Boer (Meat) | Angora (Mohair) | Cashmere |
|-----------|----------------|-------------|-----------------|----------|
| Mature weight (kg) | 60-70 | 80-100 | 35-55 | 40-60 |
| Milk yield (L/lactation) | 600-1,200 | — | — | — |
| Butterfat (%) | 3.2-3.5 | — | — | — |
| Kid growth rate (g/day) | 150-200 | 200-350 | 100-150 | 100-150 |
| Fiber yield/year | — | — | 8-12 kg mohair | 0.1-0.3 kg cashmere |
| Fiber diameter (microns) | — | — | 23-38 | 14-16 |
| Dressing percentage (%) | — | 50-55 | — | — |

## Scale Estimates per 25-Doe Operation

| Output | Annual Quantity | Notes |
|--------|----------------|-------|
| Milk (dairy herd) | 7,000-10,000 L | From 20 dairy does |
| Chevon (meat) | 400-600 kg | 3.2-4.0 kids per doe × 20 does |
| Fiber | 20-40 kg | Mohair or cashmere |
| Manure | 14-23 tonnes | Fertilizes 2-4 hectares |

## Scaling Notes

A founding herd of 10-15 goats (8-10 does, 1-2 bucks) reaches 40-60 head within 3-4 years. Does kid at 12-18 months and produce 3.2-4.0 kids per year.

**Minimum economic scale**: 2-3 dairy does provide 6-15 L milk/day at peak lactation — sufficient for household dairy. 5-8 does for brush clearing on 2-3 hectares.

**Scale bottlenecks**: Fencing is the primary cost and challenge — goats escape from barriers that hold all other livestock. Guardian animal required in predator country.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low milk yield | Insufficient nutrition, CAE infection | Increase grain to 0.5-1.0 kg/day; test for CAE |
| Escapes | Inadequate fencing height or gaps | Increase to 1.5 m height; eliminate gaps under 15 cm; add electric offset wire |
| Barber pole worm | Warm humid conditions, overstocking | FAMACHA scoring every 2 weeks; deworm scores 3-5; rotate pasture |
| Foot rot | Wet conditions, no foot trimming | Trim hooves every 8-12 weeks; foot bath in copper sulfate |
| CAE in kids | Transmitted through colostrum/milk | Heat-treat colostrum to 56°C for 60 min; pasteurize milk; separate at birth |
| Disbudding failure | Done too late or incomplete | Disbud at 3-7 days; burn copper-colored ring through skin to bone |

## Safety

**Buck handling**: Bucks produce powerful musky odor and can be aggressive during breeding season. Handle with lead and halter. Never corner one. Castrated males (wethers) are docile and make excellent pack animals or companions.

**Butting**: Goats butt as play and dominance behavior. A 60 kg goat butting a human causes bruising or knocks a person down. Discourage butting in bottle-raised kids — cute play from a 5 kg kid is dangerous from a 60 kg adult.

**Zoonotic diseases**: Q fever (*Coxiella burnetii* from birthing fluids — flu-like illness), leptospirosis (from urine), orf (contagious ecthyma — painful hand sores), caseous lymphadenitis (abscesses transmit through open wounds). Wear gloves when handling abscesses or birthing materials.

**Escape prevention**: Goats destroy gardens, orchards, and ornamental plantings in hours. Invest in fencing before acquiring goats. A bored goat is a destructive goat — provide companionship (goats are social and should never be kept singly).

## Quality Control

**Milk quality**: Strain through fine filter to remove hair. Cool to 4°C within 30-60 minutes. Test for mastitis by strip cup examination. SCC target below 1,000,000/mL. Goat milk keeps 5-7 days at 4°C.

**Fiber quality**: Mohair: measure fiber diameter with micrometer. Kid mohair (first shear, 23-27 microns) commands highest price. Adult mohair grades: 23-30 microns (premium), 30-38 microns (standard). Cashmere: must be under 18.5 microns to qualify. Dehairing recovery rate 20-40%.

**Meat quality**: Carcass should be lean with 2-3% fat cover. pH below 5.8 at 24 hours post-slaughter. No off-flavors from buck taint (castrate males intended for meat).

## Variations and Alternatives

**Tropical**: West African Dwarf goats (20-30 kg) resist trypanosomiasis (sleeping sickness) that kills cattle. Thrive in humid tropical conditions on browse alone.

**Arid/semi-arid**: Goats survive on 1.5-2.5% body weight in dry matter from browse (Acacia, Prosopis) on 50-100 mm annual rainfall. Bedouin pastoralists maintain herds where cattle perish.

**Mountain**: Alpine goats (55-65 kg) navigate slopes to 35-45° and graze at 2,000-3,000 m elevation.

**Cold climate**: Goats tolerate to -15°C without shelter if wind protection available. Below -15°C, feed intake increases 15-25% for thermoregulation.

**Pack goats**: A mature wether (50-70 kg) carries 15-25 kg over mountainous trails at 3-4 km/h for 6-8 hours. Browses along the trail, reducing feed carried.

## Cross-Domain Links

- [`animals.domestication`](domestication.md) — livestock principles: housing, nutrition, breeding, health
- [`animals.sheep`](sheep.md) — complementary species for mixed grazing; compare management
- [`animals.animal-materials`](animal-materials.md) — goatskins, tallow, fiber processing
- [`textiles.fibers`](../textiles/fibers.md) — cashmere dehairing, mohair spinning, textile production
- [`food-processing`](../food-processing/index.md) — goat cheese (chèvre, feta), yogurt, fermented products
- [`agriculture`](../agriculture/index.md) — brush clearing as land reclamation, manure as fertilizer


[← Back to Animals](index.md)
