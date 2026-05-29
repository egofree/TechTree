# Pigs (*Sus scrofa domesticus*)

> **Node ID**: animals.pigs
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`animals.domestication`](domestication.md)
> **Enables**: [`foundations.food-agriculture`](../foundations/food-agriculture.md), [`animals.animal-materials`](animal-materials.md)
> **Timeline**: Years 1-20+
> **Outputs**: pork, lard, bacon, bristles, leather, manure, waste_disposal
> **Critical**: Yes — fastest feed-to-meat conversion, waste recycling

## Overview

Pigs are the most efficient converter of feed to meat among domesticated livestock. They produce 70-80% of their live weight as usable carcass (compared to 55-60% for cattle), and they consume virtually anything organic — crop residues, kitchen scraps, whey from cheese making, culled fruits and vegetables, and forest mast (acorns, beechnuts). Mature weight ranges from 150-300 kg for modern breeds, 100-180 kg for traditional landraces. Gestation is 114 days ("three months, three weeks, three days"), with litter sizes of 8-12 piglets for improved breeds and 6-8 for traditional types.

Pigs reach market weight (90-110 kg) in just 5-7 months — the fastest turnaround of any major livestock species. This rapid growth, combined with high feed conversion efficiency (2.5-3.5 kg feed per kg of gain), makes pigs the premier meat-producing animal for a bootstrapping settlement. A single sow producing two litters per year (16-24 piglets) yields 1,500-2,500 kg of pork annually.

Beyond meat, pigs produce lard (15-30 kg per animal for fat-type breeds) — a versatile cooking fat, lubricant, and industrial material. Bristles are used for brushes. Pigskin makes durable leather. Pig manure (5-10 kg/day, high in nitrogen and phosphorus) is an excellent fertilizer. The pig's role as a waste recycler is perhaps its most underappreciated function: a pig converts food waste and agricultural byproducts into edible protein.

| Parameter | Value | Notes |
|-----------|-------|-------|
| Mature weight | 100-300 kg | Breed dependent |
| Gestation | 114 days | "3 months, 3 weeks, 3 days" |
| Litter size | 6-12 piglets | 8-10 average for heritage breeds |
| Market weight | 90-110 kg | Reached at 5-7 months |
| Feed conversion ratio | 2.5-3.5:1 | kg feed per kg gain |
| Carcass yield | 70-80% | Highest of any livestock |
| Daily gain | 0.35-0.8 kg/day | Breed and system dependent |
| Lard yield | 15-30 kg per animal | Fat-type breeds |

## Prerequisites

| Requirement | Source | Notes |
|-------------|--------|-------|
| Secure housing and fencing | [`foundations.tools-basic`](../foundations/tools-basic.md) | Pigs root under and through weak barriers |
| Feed supply (grain, scraps, forage) | [`agriculture`](../agriculture/index.md) | 2.5-3.5 kg feed per kg of gain |
| Clean water supply | [`water`](../water/index.md) | 8-15 L/day (15-30 L in heat) |
| Farrowing pen with guard rails | [`foundations.tools-basic`](../foundations/tools-basic.md) | Prevents piglet crushing |
| Waste handling system | [`construction`](../construction/index.md) | Composting area for manure |
| Basic veterinary supplies | [`health.medicine`](../health/medicine.md) | Iodine, iron supplement for piglets |

## Bill of Materials

Materials listed per 5-sow operation per year.

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Grain/complete feed | 4,000-6,000 kg | [`agriculture`](../agriculture/index.md) | Food waste, whey, forage |
| Whey or protein supplement | 2,000-4,000 L | [`food-processing`](../food-processing/index.md) | Fish meal, insects |
| Straw bedding | 1-2 tonnes | [`plants`](../plants/index.md) | Wood shavings, sawdust |
| Iron supplement (piglet) | Injectable or oral paste | [`health.medicine`](../health/medicine.md) | Soil access for iron |
| Iodine solution (7%) | 0.5-1 L | [`health.medicine`](../health/medicine.md) | Other antiseptic |
| Farrowing pen materials | 3-5 pens (3-4 m² each) | [`foundations.tools-basic`](../foundations/tools-basic.md) | Portable panels |
| Electric fencing | 2-3 strands, 3,000-5,000 V | [`energy`](../energy/index.md) | Woven wire, hog panels |

## Process Description

## 4.1 Farrowing Management

**Principle**: Farrowing (birthing) is the most critical management period. Piglets are born with minimal body fat and are vulnerable to chilling, crushing, and starvation. Mortality in the first 3 days accounts for 60-80% of all pre-weaning losses.

**Prerequisites**: Farrowing pen (3-4 m²) with guard rails (20-25 cm off ground, 15-20 cm out from wall), heated creep area (30-34°C for newborns), iodine solution (7%), clean cloth for drying piglets.

**Materials**: Guard rail pipes or wooden rails, heat lamp or heating pad for creep area, iodine solution (7%), side-cutting pliers for needle teeth, clean towels.

**Procedure**:
1. Move sow to farrowing pen 5-7 days before expected date (day 107-109 of gestation).
2. Provide clean, dry bedding. Monitor for nesting behavior, restlessness, milk letdown.
3. Piglets arrive at 10-20 minute intervals. Total duration: 2-6 hours.
4. Clear fetal membrane from each piglet's nose immediately. Dry vigorously.
5. Dip navel in 7% iodine solution.
6. Ensure each piglet nurses colostrum within 2 hours.
7. Clip needle teeth with side-cutting pliers to prevent injury to sow's udder.
8. Maintain creep area at 30-34°C for day 1, decreasing to 25-28°C by day 7.

**Expected yield**: 8-12 piglets per litter (heritage breeds 6-8). Piglet birth weight: 1.0-1.5 kg. Mortality target: under 15% with guard rails and creep heating.

**Strengths**:
- Guard rails reduce crushing deaths by 50-70%
- Heated creep area attracts piglets away from sow, further reducing crushing
- Short farrowing interval (2-6 hours) limits supervision time
- Piglets grow rapidly on sow's milk (150-250 g/day in first 3 weeks)

**Weaknesses**:
- Crushing accounts for 50%+ of piglet deaths without guard rails
- Piglets are born with no brown fat — hypothermia kills within hours without heat
- Sow may cannibalize piglets if stressed or underfed
- Large litters may exceed functional teats — fostering required

## 4.2 Pasture-Based and Forest Systems

**Principle**: Pigs on pasture require less purchased feed, produce healthier meat with higher omega-3 fatty acids, and distribute manure directly onto the land. Forest pannage (autumn woodland grazing on acorns and beechnuts) produces premium pork with minimal feed input.

**Prerequisites**: Portable electric fencing (2-3 strands at 30-50 cm, 3,000-5,000 V), portable shelters, access to shade and wallows for heat relief above 25°C.

**Materials**: Electric fence energizer and wire or netting, portable A-frame shelters, water troughs, supplemental grain (1-2 kg/day per growing pig on pasture).

**Procedure**:
1. Create paddocks with portable electric fencing. Rotate every 1-2 weeks.
2. Stock at 10-15 growing pigs per hectare on good pasture.
3. Provide wallows (mud baths) above 25°C — pigs cannot sweat.
4. Supplement with 1-2 kg grain per pig per day (pigs cannot thrive on grass alone).
5. For forest pannage: release into oak/beech woodland in autumn. Stock at 3-5 pigs per hectare. Acorns are toxic to cattle and horses but ideal pig feed.
6. Monitor body condition — adjust supplement based on forage quality.

**Expected yield**: Heritage breeds on pasture reach 70-80 kg at 8-10 months (0.35-0.55 kg/day gain). Forest-finished pork commands 30-50% price premium.

**Strengths**:
- Pigs convert mast (acorns, beechnuts) into premium pork — acorns toxic to other livestock
- Rooting behavior aerates soil and clears underbrush
- Manure deposited directly on pasture eliminates hauling
- 40-60% of diet from forage reduces purchased feed costs

**Weaknesses**:
- Pigs destroy established pasture if left too long in one area
- Cannot sweat — wallows mandatory above 25°C, water consumption doubles
- Electric fencing required — pigs challenge barriers relentlessly
- Feed supplement always needed (pigs need concentrated energy and protein)

## 4.3 Waste Feeding and Nutrient Cycling

**Principle**: Pigs consume food waste and agricultural byproducts, converting them into edible protein. Dairy-pig integration (whey feeding) is one of the oldest and most efficient farming combinations.

**Prerequisites**: Reliable waste stream (kitchen scraps, whey, crop residues), basic feed formulation knowledge, clean storage for feed materials.

**Materials**: Collection containers for waste, feed storage bins (rodent-proof), mixing area or trough.

**Procedure**:
1. Collect kitchen scraps, whey, cull produce, spent brewery grain daily.
2. Avoid meat scraps from other pigs (disease risk — African swine fever, classical swine fever) and excessive salt.
3. Mix waste with grain supplement to meet nutritional targets: 14-18% crude protein, 13-14 MJ metabolizable energy per kg feed for growing pigs.
4. Feed gestating sows 1.8-2.5 kg/day (restricted). Lactating sows: ad libitum (4-6 kg/day).
5. Ensure clean water available at all times — whey-fed pigs need additional fresh water.

**Expected yield**: Whey feeding reduces grain requirement by 30-40%. A pig consuming 4-6 L whey/day plus 1-2 kg grain achieves 0.4-0.6 kg/day gain.

**Strengths**:
- Closes nutrient loop — waste that would rot becomes edible protein
- Whey from cheese making is free feed — dairy-pig integration reduces costs by 25-35%
- Pigs consume virtually any organic material, reducing settlement waste
- Manure from waste-fed pigs is indistinguishable from grain-fed for composting

**Weaknesses**:
- Uncooked meat scraps transmit diseases (ASF, trichinellosis)
- Variable waste composition makes consistent nutrition challenging
- Excessive salt or spoiled feed causes health problems
- Waste feeding requires daily collection and processing labor

## 4.4 Growth and Processing

**Principle**: Pigs reach market weight at 90-110 kg in 5-7 months (modern breeds) or 70-80 kg in 8-10 months (heritage breeds). Carcass yield of 70-80% is the highest of any livestock species.

**Prerequisites**: Target weight achieved, processing area with clean water, sharp knives, scalding water (55-60°C).

**Materials**: Sharp boning knife, scalding vat or barrel, scraping tools, meat saw, curing salt (if preserving), rendering pot for lard.

**Procedure**:
1. Dispatch by captive bolt or electrical stunning followed by bleeding.
2. Scald at 55-60°C for 30-60 seconds to loosen hair. Scrape clean.
3. Eviscerate. Save liver, heart, kidneys, intestines (sausage casings).
4. Split carcass. Chill to 4°C within 1 hour.
5. Cut into primal cuts: shoulder, loin, belly (bacon), ham.
6. Render fat at 100-120°C for 4-6 hours. Strain through cloth. Lard yield: 70-85% of fat weight.
7. Cure hams and bacon with salt (3-4% body weight) or smoke for preservation.

**Expected yield**: 75-80 kg dressed carcass from 100 kg live pig. 55-60 kg retail cuts. 12-15 kg renderable fat. 15-20 m sausage casing from intestines.

**Strengths**:
- Highest carcass utilization of any livestock (80-85% of live weight used)
- Lard provides cooking fat with 190°C smoke point — highest of any animal fat
- Every part usable: meat, fat, skin, organs, blood, bristles, bones
- Curing and smoking extend shelf life from days to months

**Weaknesses**:
- Processing requires scalding water at precise temperature — too hot cooks the skin
- Lard rendering generates strong odors and acrolein fumes — do outdoors
- Fresh pork is highly perishable — must chill to 4°C within 1 hour
- Cook pork to 71°C internal temperature — Trichinella risk from undercooked meat

## Quantitative Parameters

## Growth Performance by System

| Parameter | Modern (Confinement) | Heritage (Pasture) | Heavy (Cured Products) |
|-----------|---------------------|--------------------|-----------------------|
| Market weight (kg) | 90-110 | 70-80 | 140-170 |
| Days to market | 140-160 | 200-280 | 365-540 |
| Daily gain (kg/day) | 0.6-0.8 | 0.35-0.55 | 0.4-0.5 |
| Feed conversion ratio | 2.5-2.8 | 3.5-4.5 | 4.0-5.0 |
| Carcass yield (%) | 75-80 | 70-75 | 70-75 |
| Lard yield (kg) | 10-15 | 15-25 | 25-40 |

## Scale Estimates per 5-Sow Operation

| Output | Annual Quantity | Notes |
|--------|----------------|-------|
| Market pigs | 80-100 head | 2.0-2.2 litters/sow/year |
| Live weight | 7,200-10,000 kg | At 90-100 kg each |
| Carcass weight | 5,400-8,000 kg | 75-80% dressing |
| Lard | 400-750 kg | From fat rendering |
| Manure | 10-20 tonnes | 5-10 kg/pig/day |

## Scaling Notes

A founding pair (1 sow + 1 boar) produces 16-24 piglets in the first year — sufficient to establish a self-sustaining herd of 8-12 breeding sows within 18-24 months.

**Minimum economic scale**: 2-3 sows provide 32-72 piglets per year — 2,400-5,400 kg live weight, enough protein for 30-50 people.

**Scale bottlenecks**: Feed is the primary cost (60-70% of production). 5 sows and their offspring consume 4,000-6,000 kg of grain per year. Farrowing supervision is labor-intensive during piglet seasons.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Piglet crushing | No guard rails, no creep heat | Install guard rails 20-25 cm off ground; provide heated creep area at 30-34°C |
| Slow growth | Insufficient protein, parasites | Increase protein to 16-18%; deworm with ivermectin or fenbendazole |
| Cannibalism (tail biting) | Overcrowding, boredom, insufficient protein | Reduce stocking density; provide straw or toys; increase protein to 16%+ |
| Scours (diarrhea) in piglets | *E. coli*, cold stress, dirty farrowing pen | Clean pen before farrowing; ensure colostrum; electrolytes for affected piglets |
| Sow not milking | Mastitis, poor body condition | Check udder for heat/swelling; increase feed to ad libitum during lactation |
| Escape | Inadequate fencing | Electric fence at 3,000-5,000 V; check for gaps under gates; bury wire 15 cm |

## Safety

**Boar handling**: Boars weigh 200-350 kg with tusks that inflict severe lacerations. Never turn your back on a boar. Use a boar board (1 m × 1.2 m solid barrier) during handling. Boars signal aggression by chomping (jaw clicking), frothing, and sidling up broadside. If charged, get behind a solid barrier — do not wrestle a charging boar.

**Zoonotic diseases**: Erysipeloid (skin infection from handling infected animals or carcasses). Trichinellosis (*Trichinella spiralis* larvae encyst in muscle — cook pork to 71°C internal temperature or freeze at -15°C for 20+ days). Salmonella. Influenza (pigs are mixing vessels for avian, swine, and human influenza — they can generate novel pandemic strains). Always cook pork thoroughly. Wear gloves when handling manure.

**Crushing during farrowing**: Sows are large and clumsy with piglets. Guard rails and heated creep areas are essential — without them, 20-30% of piglets may be crushed in the first 3 days. Monitor closely during first 48 hours post-farrowing.

**Lard rendering fumes**: Heating fat produces acrolein — a potent respiratory irritant. Render outdoors or in well-ventilated spaces. Temperature above 120°C generates more fumes. Maintain rendering at 100-120°C.

## Quality Control

**Carcass grading**: Target 75-80% dressing percentage. Backfat thickness: 2.0-3.0 cm ideal. Lean meat percentage above 55% (heritage breeds), above 60% (modern breeds). Meat pH below 5.8 at 24 hours indicates proper handling.

**Feed quality**: Test grain for mycotoxins (aflatoxin lethal at low concentrations). Protein content 14-18% for growing pigs, 16-18% for lactating sows. Moisture below 15% to prevent mold.

**Health monitoring**: Weekly observation for lethargy, coughing, diarrhea, skin lesions. Body condition scoring (1-5 scale) monthly. Target BCS 3.0 for gestating sows, 2.5-3.0 at weaning.

## Variations and Alternatives

**Tropical systems**: Pigs managed as free-range scavengers in Southeast Asia and Pacific Islands consume 40-60% of diet from forage, fallen fruit, and root crops. Pacific Island pigs grow slowly (100-150 g/day) but survive on minimal inputs.

**Cold climate**: Mangalitsa pigs produce 40-50% body fat, survive outdoors to -15°C with curly woolly coat. Require 20-30% more feed than lean breeds. Housed indoors 5-7 months in Scandinavian/Russian systems with deep straw generating composting heat.

**Arid climate**: Pigs require shade and wallows above 25°C; water consumption doubles from 8-15 L/day to 15-30 L/day above 30°C. Not suited to arid regions without water infrastructure.

**Integrated dairy-pig**: Most efficient small-scale system. Whey from cheese making feeds pigs at 4-6 L/day per grower, converting waste into 150-200 g daily weight gain. See [`food-processing`](../food-processing/index.md).

## Cross-Domain Links

- [`animals.domestication`](domestication.md) — livestock principles: housing, nutrition, breeding, health
- [`animals.animal-materials`](animal-materials.md) — lard rendering, leather tanning, bristle harvesting
- [`food-processing`](../food-processing/index.md) — bacon curing, ham smoking, sausage making, lard storage
- [`agriculture`](../agriculture/index.md) — crop residues as feed, pig manure as fertilizer, pasture rotation
- [`health.medicine`](../health/medicine.md) — disease treatment, zoonotic disease prevention


[← Back to Animals](index.md)
