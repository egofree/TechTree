# Poultry Farming

> **Node ID**: animals.poultry
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`foundations.food-agriculture`](../foundations/food-agriculture.md), [`animals.domestication`](domestication.md)
> **Enables**: [`animals.poultry.chickens`](poultry-chickens.md), [`animals.poultry.coturnix`](poultry-coturnix.md), [`animals.poultry.ducks`](poultry-ducks.md), [`animals.poultry.geese`](poultry-geese.md), [`animals.poultry.guinea-fowl`](poultry-guinea-fowl.md), [`animals.poultry.pigeons`](poultry-pigeons.md), [`animals.poultry.turkeys`](poultry-turkeys.md)
> **Timeline**: Years 0-10+
> **Outputs**: meat, eggs, feathers, manure, pest_control
> **Critical**: Yes — fastest-converting livestock; first animals to establish after securing grain production


Poultry farming is the managed raising of domesticated birds for meat, eggs, feathers, and other products. Poultry are the fastest-converting livestock — turning grain and forage into high-quality protein within weeks rather than months. They require less space, less feed, and less infrastructure than any mammalian livestock, making them the first animals a settlement should establish after securing grain production. Seven primary species span a wide range of sizes, temperaments, and specializations, from the universal chicken to the pest-hunting guinea fowl to the self-foraging pigeon.

| Species | Adult Weight | Eggs/Year | Incubation (days) | Feed/Day (g) | Space/Bird (m²) |
|---------|-------------|-----------|-------------------|--------------|-----------------|
| [Chickens](poultry-chickens.md) | 1.5-4.5 kg | 200-300 | 21 | 100-150 | 0.05-0.5 |
| [Coturnix Quail](poultry-coturnix.md) | 100-200 g | 250-300 | 17 | 20-30 | 0.02-0.05 |
| [Ducks](poultry-ducks.md) | 2-5 kg | 150-250 | 28 | 120-200 | 0.5-1.0 |
| [Geese](poultry-geese.md) | 4-10 kg | 30-60 | 28-30 | 150-300 | 2-5 |
| [Turkeys](poultry-turkeys.md) | 4-15 kg | 60-120 | 28 | 150-400 | 20+ (range) |
| [Guinea Fowl](poultry-guinea-fowl.md) | 1.2-1.6 kg | 80-130 | 26-28 | 30-80 | Free range |
| [Pigeons](poultry-pigeons.md) | 350-800 g | 400+ potential | 17 | 30-50 | 0.2 (loft) |

## Prerequisites

| Requirement | Source | Notes |
|-------------|--------|-------|
| Grain (corn, wheat, oats) | [`agriculture`](../agriculture/index.md) | 100-400 g/bird/day depending on species |
| Protein supplement (soy, peas, fish meal) | [`agriculture`](../agriculture/index.md) | 14-30% of diet depending on age |
| Secure housing (wire mesh, solid walls) | [`construction`](../construction/index.md) | 0.1-0.2 m² per bird indoor |
| Calcium (oyster shell, limestone) | [`mining`](../mining/index.md) | Free-choice for layers (3.5-4.0% of diet) |
| Clean water system | [`water`](../water/index.md) | 250-400 mL/bird/day; doubles in heat |
| Fencing (wire mesh or electric) | [`foundations.tools-basic`](../foundations/tools-basic.md) | Perimeter + covered runs |

## Bill of Materials

Materials listed for a 50-bird mixed flock per year.

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Grain (corn, wheat, oats mix) | 1,800-2,700 kg | [`agriculture`](../agriculture/index.md) | Home-mixed from grown grain |
| Protein supplement (soy/peas) | 400-600 kg | [`agriculture`](../agriculture/index.md) | Fish meal, insects, meat scraps |
| Oyster shell or limestone grit | 50-100 kg | [`mining`](../mining/index.md) | Crushed eggshells (recycled) |
| Bedding (straw, shavings) | 500-1,000 kg | [`plants`](../plants/index.md) | Deep litter method |
| Wire mesh (1-2 cm openings) | 20-30 m² | [`metals`](../metals/index.md) | For vents and run enclosures |
| Feed storage (metal bins) | 3-4 units (35-50 L each) | [`metals`](../metals/index.md) | Rodent-proof containers |

## Process Description

## Egg Production

**Principle**: Laying hens convert grain and protein feed into eggs at 2.0-2.5 kg feed per kg of egg mass. Each egg contains approximately 6 g protein, 5 g fat, and 70 kcal. Peak production at 22-72 weeks of age at 80-90% lay rate.

**Prerequisites**: Layer breed hens (dual-purpose or specialized), layer ration (14-18% protein, 3.5-4.0% calcium), nesting boxes (1 per 4-5 hens), clean water.

**Materials**: Layer feed, oyster shell (free-choice), nesting boxes with clean bedding, egg collection baskets.

**Procedure**:
1. Raise pullets from chicks or source at 16-18 weeks (point of lay).
2. Provide layer ration: 14-18% protein, 3.5-4.0% calcium. Feed 100-130 g/day per hen.
3. Ensure 14-16 hours of light per day (supplement with artificial light in winter — 5-10 watt LED per 10 m²).
4. Collect eggs 1-2 times daily. Store at 4°C. Fresh eggs maintain grade A quality for 4-6 weeks.
5. Candle eggs against bright light to check quality: tight yolk, air cell under 3 mm depth.
6. Replace 20-25% of flock annually with young pullets to maintain peak production.

**Expected yield**: 50 hens produce 40-45 eggs/day at peak (80-90% lay rate), 12,500-15,000 eggs/year. Annual feed cost: $0.05-0.08 per egg in feed alone.

**Strengths**:
- Fastest return on investment of any livestock — hens begin laying at 18-22 weeks
- Eggs are self-contained, shelf-stable protein — store 4-6 weeks at 4°C without processing
- Dual-purpose breeds provide both eggs and meat from the same flock
- Manure is high-nitrogen (1.5-2.0% N) — 50 hens produce 1.8-2.7 tonnes of manure per year

**Weaknesses**:
- Egg production declines 10-15% per year after first laying season — must replace layers regularly
- Light supplementation required in winter to maintain production — energy cost in northern latitudes
- Predation from hawks, foxes, raccoons, and weasels requires secure housing and covered runs
- Cannibalism and feather-picking develop in overcrowded or bored flocks — space and enrichment needed

## Meat Production (Broilers)

**Principle**: Broiler chickens convert feed to meat at 1.5-1.8 kg feed per kg of live weight — the most efficient of any terrestrial livestock. Broilers reach 2.0-2.5 kg at 6-8 weeks. Heritage breeds grow slower (12-16 weeks) but reproduce naturally and forage on range.

**Prerequisites**: Broiler chicks (day-old), brooder with heat source (35°C initial, reduce 3°C/week), starter/grower feed (20-24% protein starter, 16-18% grower).

**Materials**: Brooder lamp or heat plate, feeders, waterers, bedding (pine shavings), processing equipment (killing cone, scalder, plucker or hand-plucking).

**Procedure**:
1. Brood chicks at 35°C, reduce by 3°C per week until ambient temperature reached. Draft-free enclosure with solid walls.
2. Feed starter ration (20-24% protein) for 0-3 weeks. Switch to grower (16-18% protein) at 3 weeks.
3. Provide clean water constantly — broilers drink 250-400 mL/day at finish weight.
4. Process at 6-8 weeks (2.0-2.5 kg live weight). Slaughter, scald at 60°C for 30-60 seconds, pluck, eviscerate.
5. Chill to 4°C within 1 hour. Dressed yield: 70-75% of live weight.

**Expected yield**: 50 broilers produce 70-95 kg dressed meat in 6-8 weeks. Feed consumption: 150-225 kg total feed per batch. Feed conversion ratio: 1.5-1.8.

**Strengths**:
- Shortest production cycle of any meat animal — 6-8 weeks from chick to table
- Best feed conversion of any terrestrial livestock — 1.5-1.8:1
- Multiple batches per year — 4-6 growout cycles possible in a single housing unit
- Heritage breeds forage 30-50% of diet on range — reduces purchased feed costs

**Weaknesses**:
- Fast-growing broilers have leg problems and heart failure if management is poor
- Processing 50 birds takes 4-6 hours by hand — labor-intensive at slaughter
- Brooder heating required for first 3 weeks — energy cost or fuel consumption
- Disease spreads rapidly in confined flocks — biosecurity is essential

## Multi-Species Integration

**Principle**: Running multiple poultry species on shared range utilizes different ecological niches. Chickens scratch at ground level, ducks forage in wet areas, guinea fowl hunt in tall grass, geese graze pasture, turkeys forage woodland edges. Each species fills a different role.

**Prerequisites**: Multiple poultry species, adequate range area, separate housing for incompatible species.

**Materials**: Species-appropriate housing, perimeter fencing, covered runs or netting.

**Procedure**:
1. House species separately — turkeys must be separated from chickens (blackhead disease), waterfowl need separate housing (wet litter).
2. Run chickens on range first (scratch and fertilize), follow with crops the next season.
3. Use geese as weeders in established crop rows — they graze weeds but avoid many mature crops.
4. Range turkeys on land not used by chickens.
5. Guinea fowl patrol for ticks across all range areas — reduce tick populations by 70-90% on 1-2 hectares per 20-30 birds.
6. Rotate range areas annually to break parasite cycles.

**Expected yield**: A mixed operation of 30 chickens, 10 ducks, and 6 geese on 0.5-1.0 hectares produces 6,000-8,000 eggs, 80-120 kg dressed meat, and 1.5-2.5 tonnes of high-nitrogen manure annually.

**Strengths**:
- Each species exploits a different food source — reduces competition and maximizes total output
- Species diversity provides resilience against species-specific diseases
- Guinea fowl provide pest control for the entire operation as a byproduct
- Geese convert grass to meat and fat — no grain required for maintenance on good pasture

**Weaknesses**:
- Separate housing required for each species — more infrastructure than single-species operation
- Turkeys cannot share range with chickens due to blackhead disease transmission
- Waterfowl wet litter rapidly — damage housing and create disease risk for land poultry
- Different feeding schedules and rations increase management complexity

## Incubation and Brooding

**Principle**: All poultry eggs require specific temperature (37.5°C), humidity (55-65%), and regular turning for successful incubation. Incubation periods range from 17 days (quail, pigeons) to 30 days (geese). Newly hatched chicks need supplemental heat starting at 35°C, reducing by 3°C per week.

**Prerequisites**: Fertile eggs, incubator or broody hen, brooder with heat source.

**Materials**: Incubator (temperature-controlled box with egg turner) or broody hen, thermometer, hygrometer, brooder lamp or heat plate, chick starter feed.

**Procedure**:
1. Collect fertile eggs. Store at 12-15°C for up to 7 days before setting in incubator.
2. Set eggs in incubator at 37.5°C, 55-65% humidity. Turn 3-5 times daily (automatic turner preferred).
3. Stop turning 3 days before expected hatch. Increase humidity to 65-70% for hatching.
4. Chicks hatch over 12-24 hours. Leave in incubator until dry and fluffy (4-6 hours).
5. Move to brooder at 35°C. Provide chick starter feed and water immediately.
6. Reduce brooder temperature by 3°C per week until ambient temperature reached (3-6 weeks depending on species).
7. Use paper towels for bedding in first few days for tiny species (quail, keets) — their legs slip on smooth surfaces.

**Expected yield**: Fertility rate 85-95% for healthy breeding stock. Hatch rate of fertile eggs: 80-90% in well-managed incubators. Broody hens: 90%+ hatch rate on fewer eggs.

**Strengths**:
- Artificial incubation enables large-scale production independent of broody behavior
- Broody hens incubate and raise chicks at zero energy cost — lowest-tech option
- Chicken hens can incubate eggs of other species (quail, guinea fowl) as surrogate mothers
- Rapid generation turnover — quail go from egg to laying in 6-7 weeks

**Weaknesses**:
- Power failure during incubation kills the entire batch — backup heat or generator required
- Temperature variation of even 1°C reduces hatch rate significantly
- Broody behavior is unreliable in many modern breeds — heritage breeds retain the instinct
- Chicks are fragile for the first 2 weeks — mortality 5-10% even with good management

## Quantitative Parameters

## Manure Composition by Species

| Species | Nitrogen (%) | Phosphorus (%) | Potassium (%) | Manure/Bird/Year (kg) |
|---------|-------------|----------------|---------------|------------------------|
| Chickens | 1.5-2.0 | 1.0-1.5 | 0.5-0.8 | 35-55 |
| Ducks | 1.0-1.5 | 0.8-1.2 | 0.4-0.6 | 45-70 |
| Geese | 0.8-1.2 | 0.6-0.9 | 0.4-0.6 | 55-110 |
| Turkeys | 1.3-1.5 | 1.0-1.2 | 0.5-0.7 | 55-150 |
| Guinea Fowl | 1.5-1.8 | 1.0-1.3 | 0.5-0.7 | 25-40 |
| Pigeons | 4.0-5.0 | 2.0-3.0 | 1.5-2.0 | 10-15 |

## Protein Requirements by Age

| Species | Starter (0-3 wk) | Grower (3-8 wk) | Layer/Adult |
|---------|-------------------|------------------|-------------|
| Chickens | 20-24% | 16-18% | 14-18% |
| Turkey poults | 28-30% | 20-24% | 14-16% |
| Ducklings | 18-22% | 15-18% | 14-16% |
| Goslings | 18-20% | 15-16% | 14-15% |
| Quail | 24-28% | 20-24% | 16-20% |

## Egg Production Benchmarks

| Species | Eggs/Hen/Year | Egg Weight | Feed per Dozen Eggs |
|---------|---------------|------------|---------------------|
| Chickens | 200-300 | 50-65 g | 1.8-2.2 kg |
| Ducks | 150-250 | 70-80 g | 2.5-3.5 kg |
| Quail | 250-300 | 10-12 g | 0.6-0.8 kg |
| Geese | 30-60 | 140-170 g | 6-10 kg |
| Turkeys | 60-120 | 70-90 g | 4-6 kg |

## Scaling Notes

**Minimum viable scale**: 10-20 chickens (2-3 hens per rooster for breeding, plus 10-15 hens for egg production) produce 2,000-4,000 eggs per year within the first 6 months.

**Mixed operation**: 30 chickens, 10 ducks, 6 geese on 0.5-1.0 hectares produce 6,000-8,000 eggs, 80-120 kg dressed meat, and 1.5-2.5 tonnes of manure annually.

**Feed requirements**: A 50-bird mixed flock consumes 5-7.5 kg feed daily (150-225 kg monthly). Store in rodent-proof metal bins. A single rat consumes 20-30 g feed daily and contaminates 10× that amount — rodent control saves 5-10% of feed costs.

**Housing**: 50 layers need 5-10 m² indoor floor space (0.1-0.2 m²/bird) plus 200-300 m² outdoor run (4-6 m²/bird).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Drop in egg production | Reduced light, stress, disease, molting | Ensure 14-16 hr light; check for disease; expect natural molt at 12-18 months |
| Cannibalism/feather picking | Overcrowding, boredom, bright light, protein deficiency | Reduce stocking density; provide range or enrichment; dim lights to 10 lux; increase protein to 18% |
| Thin eggshells | Calcium deficiency, heat stress, age | Provide free-choice oyster shell; check calcium at 3.5-4.0%; replace old hens |
| Coccidiosis (bloody droppings) | Wet litter, overcrowding, young birds | Keep litter dry; add fresh bedding; treat with amprolium in water; provide medicated starter |
| Respiratory disease | Ammonia buildup, poor ventilation, mycoplasma | Increase ventilation; clean litter; 0.1 m² opening per 10 birds at roofline |
| Predation (missing birds) | Foxes, hawks, raccoons, weasels | Secure housing at night; covered runs; electric fence at 10-15 cm and 30-40 cm; lock up at dusk |

## Safety

**Zoonotic diseases**: All poultry carry *Salmonella* and *Campylobacter*. Wash hands after handling birds, eggs, or litter. Cook poultry meat and eggs thoroughly. Pregnant women should avoid cleaning poultry litter (listeria risk from contaminated dust).

**Respiratory hazards**: Poultry dust (feather dander, dried droppings, bedding particles) causes respiratory irritation and allergic reactions. Wear a mask when cleaning enclosed poultry housing. Ensure good ventilation.

**Avian influenza**: Wild waterfowl are natural reservoirs. Prevent contact between domestic poultry and wild birds. Screen all openings with hardware cloth (under 2.5 cm mesh). Report unusual mortality events immediately. High-pathogenicity strains are dangerous to both birds and humans.

**Biosecurity**: Footwear disinfection (walk-through boot bath with 2% sodium hydroxide) at every poultry area entrance. Dedicated tools for each species area — never shared between turkey and chicken zones. Quarantine new birds for 30 days in a separate building at least 15 m from main flock.

**Processing safety**: Use sharp knives. Scalding water at 60°C causes burns — use tongs and protective gloves. Chill processed birds to 4°C within 1 hour to prevent bacterial growth.

## Quality Control

**Egg quality**: Candle eggs against bright light (100+ lumens). Fresh eggs: tight centered yolk, air cell under 3 mm. Stale eggs: large mobile yolk, air cell above 5 mm. Shell thickness above 0.33 mm; below 0.28 mm indicates calcium deficiency. Blood spots (1-2% of eggs) are safe — not a sign of fertilization.

**Meat quality**: Process broilers at 6-8 weeks for optimal tenderness. Dressed yield should be 70-75% of live weight. Chill to 4°C within 1 hour. Fresh poultry keeps 2-3 days at 4°C; frozen keeps 6-12 months at -18°C.

**Flock health monitoring**: Weekly observation for lethargy, ruffled feathers, abnormal droppings, reduced feed/water intake. Monthly: clean and disinfect waterers and feeders; check for external parasites (mite and lice at vent area). Quarterly: complete coop cleanout, fresh bedding, lime wash on walls.

**Vaccination schedule**: Marek's disease (day 1, subcutaneous), Newcastle/bronchitis (day 10-14, booster at 4-6 weeks), fowl pox (6-8 weeks, wing web stab). Deworm at beginning and end of grazing season (spring and autumn) with 7-14 day egg withdrawal period.

## Variations and Alternatives

**Egg preservation**: Waterglass (sodium silicate, 1:10 ratio with water) preserves eggs 6-12 months at 10-15°C by sealing shell pores. Mineral oil coating extends shelf life to 4-6 months. Salt curing produces preserved eggs with concentrated yolks. Pickling in spiced vinegar brine (5% acetic acid) preserves hard-boiled eggs 3-6 months refrigerated.

**Meat preservation**: Salting (3-4% body weight, 5-7 days refrigerated), smoking (hot smoke 60-80°C for 2-4 hours or cold smoke 20-30°C for 12-24 hours), or drying as jerky (2-3% salt, dried at 55-60°C to below 20% moisture). Rendered poultry fat (duck, goose) preserves confit for 6-12 months.

**Tropical climate**: Open-sided housing with wire mesh walls maximizes airflow. Provide electrolytes in water (1 g NaCl + 1 g KCl per liter) above 30°C. Evaporative cooling (wet burlap curtains) reduces indoor temperature by 5-8°C.

**Cold climate**: Insulated walls (R-10 to R-15), deep litter composting heat, supplemental lighting (14-16 hours via 5-10 watt LED per 10 m²). Ducks excel in tropical and monsoon climates; geese thrive in cold temperate zones.

## Cross-Domain Links

- [`animals.domestication`](domestication.md) — livestock husbandry foundations, fencing, shelter construction
- [`agriculture`](../agriculture/index.md) — feed grain production, pasture management, range rotation
- [`food-processing`](../food-processing/index.md) — meat and egg preservation techniques
- [`textiles`](../textiles/index.md) — feathers and down for insulation and bedding
- [`animals.pest-management`](pest-management.md) — integrated pest management with poultry
- [`knowledge`](../knowledge/index.md) — homing pigeons for long-distance messaging


[← Back to Animals](index.md)
