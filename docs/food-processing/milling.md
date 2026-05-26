# Grain Milling

> **Node ID**: food-processing.milling
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: `energy`
> **Enables**: None (leaf capability)
> **Timeline**: Years 0-20
> **Outputs**: flour, bran, grits, meal

## Overview

Grain milling converts harvested grain into flour — the single most important food processing operation in civilization. A workforce that eats bread is 2-3x more calorie-efficient than one eating whole-grain porridge. Milling also produces bran (animal feed), grits (coarse meal), and germ (oil source). The progression from hand-powered stone grinding to water-powered millstones to roller milling mirrors the broader energy revolution: each step multiplies throughput by 5-10x while reducing human labor.

This capability begins with stone-age saddle querns (covered in [Agriculture & Food Production](../foundations/food-agriculture.md)) and extends through industrial roller milling. The focus here is on the technological progression beyond hand querns.

## Bill of Materials

### Stone Milling Materials

| Material | Quantity per tonne flour | Source | Alternatives |
|----------|:-----------------------:|--------|-------------|
| Wheat grain (clean, dry) | 1.25-1.43 tonnes (70-80% extraction) | [Agriculture](../foundations/food-agriculture.md) | Rye, barley, oats, corn (different flour properties) |
| Millstones (pair) | 1 pair per mill (1.0-1.5 m diameter) | [Mining](../mining/index.md) — granite, basalt, burrstone | French burrstone (premium), sandstone (soft, wears fast) |
| Water (tempering) | 100-150 L per tonne grain | [Water](../water/index.md) | Must be clean; 15-16% target moisture |
| Wire mesh screens | 2-4 sets per mill | [Metals](../metals/index.md) — steel wire | Silk cloth (finer, less durable) |

### Roller Milling Materials (Industrial)

| Material | Quantity per tonne white flour | Source | Alternatives |
|----------|:-----------------------------:|--------|-------------|
| Wheat grain | 1.32-1.40 tonnes (72-76% extraction) | [Agriculture](../foundations/food-agriculture.md) | Different grain varieties affect extraction |
| Roller mill chill iron | 4-8 pairs rollers per mill line | [Metals](../metals/index.md) — cast iron, steel | Stone milling (lower throughput, coarser) |
| Screens (plansifter) | 20-40 screens per sifter | [Metals](../metals/index.md) — steel wire, nylon | Silk (traditional, less durable) |
| Electrical energy | 30-50 kWh per tonne wheat | [Energy](../energy/index.md) | Steam engine (via belt drive), water wheel |
| Water (tempering) | 100-150 L per tonne grain | [Water](../water/index.md) | Moisture must reach 15-16% before milling |

## Process Description

### Milling Technology Progression

**Stage 1: Rotary Quern** (Years 0-5)

Two circular stones 30-50 cm diameter. Upper stone rotates on stationary lower stone via a central pivot. Grain fed through central hole, grooves channel flour outward.

- **Materials**: Hard, coarse stone (granite, basalt, sandstone). Stone selection critical — porous stones contaminate flour with grit. Peak hardness stones (granite) last longest but are hardest to shape.
- **Output**: 1-5 kg flour/hour (5× improvement over saddle quern)
- **Screen sizes**: Not screened. Whole-grain flour with bran particles. Coarser than modern whole wheat.
- **Labor**: One person can operate a rotary quern. Requires sustained upper-body effort.
- **Limitation**: Hand-powered only. Throughput capped by human power output (~100W sustained).

**Stage 2: Animal-Powered Mill** (Years 5-10)

Same stone geometry as rotary quern, but power source changed to draft animal (ox, donkey, horse) walking in a circle, turning the upper stone via a wooden gear mechanism.

- **Power**: 0.5-1 HP (horse), providing 5-10× more sustained power than a human
- **Output**: 10-50 kg flour/hour
- **Mechanism**: Vertical shaft connected to horizontal lever arm. Animal walks in 3-5 m diameter circle. Bevel gear or direct drive connects shaft to upper millstone.
- **Advantage**: Frees human labor for other tasks. Continuous operation possible for hours.
- **Feed control**: Hopper above millstones regulates grain feed rate. Too fast = coarse meal, too slow = flour burns from friction heat.

**Stage 3: Water-Powered Mill** (Years 5-15)

Water wheel (undershot or overshot) drives millstones through gear train. The first industrial application of water power.

- **Power**: 1-5 HP depending on water flow and wheel diameter
- **Output**: 50-200 kg flour/hour
- **Overshot wheel**: Water flows over the top of the wheel. Efficiency 60-70%. Requires a headrace (elevated water channel). 2-4 m diameter wheel.
- **Undershot wheel**: Water flows under the wheel. Efficiency 20-30%. Simpler construction. Works with any flowing water.
- **Gear train**: Wooden cog wheels (later iron) convert horizontal wheel rotation to vertical millstone rotation. Gear ratio typically 3:1 to 5:1.
- **Millstone pairs**: "Bedstone" (fixed lower stone, 1.0-1.5 m diameter) and "runner" (rotating upper stone). Grooves (called "lands" and "furrows") cut into faces channel grain from center to edge, progressively grinding finer.
- **Dressing**: Millstones must be re-grooved ("dressed") every 2-4 weeks depending on stone hardness. A skilled stone dresser can dress a pair in 4-8 hours.
- **Screening**: Wire mesh or silk screens sort output into flour (<180 μm), middlings (180-500 μm), and bran (>500 μm). Multiple passes through progressively finer screens improve extraction rate.
- **Extraction rate**: Stone milling typically extracts 70-80% of the grain as flour (the rest is bran and shorts). Higher extraction = more flour but darker, coarser product.

**Stage 4: Wind-Powered Mill** (Years 5-15)

Post mill or tower mill with sail-type rotor driving millstones. Independent of water availability.

- **Power**: 2-10 HP depending on sail area and wind speed
- **Output**: 100-500 kg flour/hour (when wind blows)
- **Post mill**: Entire wooden structure rotates on a central post to face the wind. Simpler but smaller.
- **Tower mill**: Only the cap (top) with the sails rotates. Stone/brick tower is permanent. Larger, more powerful.
- **Sail design**: Four sails, 5-12 m length each. Sail area adjustable via shutters or canvas reefing. Optimal performance at 15-25 km/h wind speed. Automatic shutdown via spring-loaded mechanism at dangerous speeds.
- **Limitation**: Intermittent power. Requires grain storage and operational flexibility. Best combined with water mill in same community.

**Stage 5: Roller Mill** (Years 15-25)

Cast iron or steel rollers replace millstones. Each pair of rollers has progressively smaller gap settings. This is the modern industrial milling system.

- **Roller design**: Chilled cast iron or steel rollers, 250-300 mm diameter, 1000-1500 mm length. Corrugated surface for break rollers, smooth surface for reduction rollers.
- **Break system**: 4-5 pairs of rollers with progressively finer corrugations and smaller gaps. First break: gap ~0.5 mm (cracks grain open). Last break: gap ~0.1 mm. Each break releases endosperm from bran.
- **Sifting system**: Plansifters (multi-deck vibrating screens) sort output after each break pass. Screens: 1320 μm (coarse bran), 860 μm (fine bran), 560 μm (coarse semolina), 320 μm (fine semolina), <150 μm (patent flour).
- **Reduction system**: 8-12 pairs of smooth rollers progressively reduce semolina particle size to flour. Gap settings from 0.08 mm down to 0.02 mm.
- **Purifiers**: Air classification removes bran particles from semolina using controlled airflow. Lighter bran particles are carried away while heavier endosperm particles fall through.
- **Extraction rate**: 72-76% white flour (patent flour), up to 85% with clear flour grades.
- **Output**: 5-50 tonnes flour/day per roller mill line. A modern mill has 3-5 lines.
- **Power requirement**: 30-50 kW per tonne/hour of wheat milled (steam or electric motor drive).

### Flour Grades

| Grade | Extraction % | Particle Size | Color | Use |
|-------|:-----------:|:--------------|:------|:----|
| Patent flour | 40-60% | <150 μm | White | Bread, pastry |
| Clear flour | 60-75% | <180 μm | Off-white | General baking |
| Whole wheat | 95-100% | <500 μm | Brown | Whole grain bread |
| Semolina | N/A | 150-500 μm | Yellow | Pasta, couscous |
| Bran | N/A | >500 μm | Brown | Animal feed, fiber |

### Baking (Flour's Primary Use)

Bread is the primary use of flour and the staple calorie source for industrial workforces:

- **Leavened bread**: Wheat flour + water + yeast (Saccharomyces cerevisiae) + salt. Knead 10-15 minutes to develop gluten network. Ferment (proof) 1-2 hours at 25-30°C until doubled in volume. Shape, proof again 30-60 minutes. Bake at 200-230°C for 25-45 minutes depending on loaf size.
- **Sourdough**: Wild yeast + Lactobacillus culture maintained from previous batch. More complex flavor, lower pH (4.0-4.5) provides natural preservation. Culture fed daily with equal weight flour and water.
- **Flatbread (unleavened)**: Flour + water + salt, rolled thin, cooked on hot surface (griddle, stone, or pan) 1-3 minutes per side. Simplest, fastest bread. Examples: tortilla, chapati, pita. No yeast required.
- **Oven design**: Beehive oven (brick dome, 60-100 cm diameter). Heat with wood fire for 2-3 hours until dome is white-hot. Remove coals, mop floor. Bake bread using stored heat (temperature declining from 300°C to 180°C over 1-2 hours). A single firing can bake 20-50 loaves in sequence.
- **Flour requirement**: A workforce of 100 people needs ~30-40 kg flour/day (assuming 300-400 g bread per person). This requires milling 40-55 kg wheat/day, achievable with a single water-powered mill running 2-3 hours/day.

### Grain Storage Before Milling

Proper grain storage is critical to prevent losses between harvest and milling:

- **Moisture content**: Must be below 14% for safe storage. Above 15%, mold (Aspergillus) grows and produces aflatoxin. Above 18%, spontaneous heating occurs from microbial respiration.
- **Drying methods**: Sun drying on hard surfaces (concrete, stone) for 2-3 days. Grain depth <10 cm, turned 2-3 times daily. Mechanical drying: forced air at 40-60°C through grain bed. Temperature must stay below 60°C or grain cracks (reduced milling quality).
- **Storage structures**: Elevated granaries (rodent protection), sealed containers (insect protection), or bulk bins with controlled atmosphere. Fumigation with carbon dioxide (60% CO₂ for 4+ days) kills all insect life stages without chemical residues.
- **Storage losses**: Typical 5-15% losses in developing-world storage due to insects (weevils, borers), rodents, and mold. Proper storage reduces this to <2%.
- **Quality testing before milling**: Visual inspection (mold, insect damage, foreign material). Moisture meter reading. Test weight (heavier grain = plumper kernels = more flour). Falling number test (measures α-amylase activity — too high indicates sprouting damage).

## Quantitative Parameters

### Milling Throughput by Technology Stage

| Stage | Power Source | Output (kg flour/hour) | Extraction Rate | Labor (persons) | Energy Input |
|:-----:|:-----------:|:---------------------:|:---------------:|:---------------:|:------------:|
| Rotary quern | Human (~100 W) | 1-5 | 95-100% (whole grain) | 1 | 0.1 kW (sustained) |
| Animal mill | Horse/ox (0.5-1 HP) | 10-50 | 85-95% | 1 | 0.5-1 kW |
| Water mill | Water wheel (1-5 HP) | 50-200 | 70-80% | 1-2 | 1-5 kW |
| Wind mill | Wind sails (2-10 HP) | 100-500 | 70-80% | 1-2 | 2-10 kW (intermittent) |
| Roller mill | Steam/electric (30-50 HP) | 200-2000 | 72-76% (white) | 3-5 | 25-40 kW |

### Flour Particle Size and Screen Specifications

| Fraction | Particle Size (μm) | Screen Mesh | Typical Yield (%) | Primary Use |
|----------|:------------------:|:-----------:|:-----------------:|:-----------:|
| Patent flour | <150 | 100 mesh | 40-60 | Bread, pastry |
| Clear flour | 150-180 | 80 mesh | 15-25 | General baking |
| Fine semolina | 180-320 | 50 mesh | 5-10 | Pasta |
| Coarse semolina | 320-560 | 30 mesh | 3-5 | Couscous |
| Middlings | 500-860 | 20 mesh | 2-5 | Re-mill or animal feed |
| Fine bran | 860-1320 | 14 mesh | 3-5 | Animal feed |
| Coarse bran | >1320 | — | 10-15 | Animal feed, fiber |

### Millstone Dressing Parameters

| Parameter | Specification | Notes |
|-----------|:------------:|:-----:|
| Furrow depth (center) | 3-8 mm | Tapers to 1-2 mm at edge |
| Furrow angle to tangent | 15-25° | Quarter dress pattern |
| Stone diameter | 1.0-1.5 m | Larger = higher throughput |
| Runner RPM | 80-120 | Faster = finer but hotter |
| Dressing frequency (sandstone) | 2-4 weeks | Soft stone wears fast |
| Dressing frequency (granite) | 2-3 months | Hard stone wears slowly |
| Dressing time per pair | 4-8 hours | Skilled stone dresser required |

### Grain Storage Parameters

| Parameter | Safe Range | Failure Mode if Exceeded |
|-----------|:----------:|:------------------------:|
| Moisture content | <14% | Mold growth, aflatoxin production above 15% |
| Storage temperature | <20°C | Accelerated insect reproduction above 25°C |
| Storage duration | <12 months | Nutrient degradation, flavor loss after 12 months |
| Grain depth (drying) | <10 cm | Uneven drying, mold in center |
| Mechanical drying temp | 40-60°C | Grain cracking above 60°C |

## Scaling Notes

- **Household mill** (5-20 kg/day): Rotary quern operated by one person. Sufficient for a family's daily bread. Labor: 2-4 hours daily grinding. No external power required. Output: 1-5 kg/hour.
- **Village mill** (50-200 kg/day): Water or animal-powered stone mill. Serves 50-200 people. One miller operates the mill; community members bring grain. Requires water source (stream with 1+ m head) or draft animal. Millstones need dressing every 2-8 weeks.
- **Regional mill** (1-5 tonnes/day): Multiple water or wind mills, or a single small roller mill (steam-powered). Serves a town of 1,000-5,000 people. Requires permanent water infrastructure or reliable wind. Roller mill requires 25-40 kW steam or electric power.
- **Industrial mill** (50-500 tonnes/day): Multiple roller mill lines with automated grain handling, tempering, and sifting. 3-5 roller lines, each producing 10-100 tonnes/day. Requires 500-2500 kW electrical power and rail or truck grain delivery infrastructure. 20-100 workers per shift.
- **Key scaling constraint**: The stone dresser is the critical skilled worker for stone mills. Without regular dressing, millstone grinding efficiency drops 30-50% in weeks. For roller mills, the plansifter (vibrating screen) is the bottleneck — screen capacity determines maximum throughput per milling line.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Flour too coarse | Worn millstone grooves, roller gap too wide, grain feed too fast | Dress millstones. Tighten roller gap. Reduce grain feed rate via hopper adjustment |
| Flour too hot (>55°C) | Excessive friction from worn stones, roller speed too high, insufficient cooling | Dress stones. Reduce RPM. Add water cooling to roller mill. Check bearing lubrication |
| Low extraction rate | Screens clogged, grain moisture too low (shatters), bran not fully separated | Clean screens. Temper grain to 15-16% moisture. Increase number of break passes |
| Grain shatters to powder | Grain moisture <12%, roller gap too small on first break | Temper grain to 15-16% (8-24 hours). Widen first break gap to ~0.5 mm |
| Flour contains grit | Porous millstone shedding, foreign material in grain | Switch to harder, less porous stone. Clean grain before milling (winnowing, sieving) |
| Insect infestation in stored flour | Mediterranean flour moth, weevils — poor storage conditions | Store in sealed containers. Fumigate with CO₂ (60% for 4+ days). Keep below 15°C |
| Bran specks in white flour | Incomplete sifting, torn screens, purifier airflow too low | Replace torn screens. Increase purifier air velocity. Add extra sifting pass |
| Mill vibration (stone mill) | Unbalanced runner stone, worn bearings, uneven stone wear | Check stone balance (rotate empty, observe wobble). Replace bearings. Re-dress stones |
| Flour rancidity | Wheat germ oil oxidizing — high extraction flour stored too long | Separate germ during milling (store separately under refrigeration). Use whole wheat flour within 2-3 months |

## Safety

- **Milling temperature**: Stone mills generate friction heat. Flour temperature must stay below 55°C or gluten proteins denature. Water cooling on roller mills maintains 25-35°C.
- **Moisture control**: Grain must be tempered to 15-16% moisture before milling. Too dry = shatters into fine powder (no separation). Too wet = clogs screens. Tempering time: 8-24 hours.
- **Insect contamination**: Mediterranean flour moth (Ephestia kuehniella) is the primary pest. Flour must be sifted and stored in sealed containers. Phosphine fumigation for infestations (requires careful ventilation — phosphine is lethal).
- **Aflatoxin risk**: Mold-contaminated grain (Aspergillus flavus) produces aflatoxin, a potent carcinogen. Grain must be visually inspected and moisture kept below 13% for storage. UV fluorescence screening detects contaminated lots.
- **Flour dust explosion**: Flour dust is explosive at concentrations of 40-60 g/m³ in air. All electrical equipment in mills must be explosion-proof. Dust collection systems (cyclone separators + bag filters) are mandatory. Ignition sources (sparks, static, open flames) must be eliminated. Historical flour mill explosions were a major industrial hazard.
- **Rotating machinery**: Roller mills and millstones have powerful rotating components. Guard all belt drives and gear trains. Emergency stop mechanism accessible from operator position. Never reach into a running roller mill.

## Quality Control

### Millstone Dressing and Maintenance

Millstones require regular maintenance to maintain grinding efficiency. The grooves (lands and furrows) wear flat over time, reducing cutting action and increasing friction heat.

- **Dressing frequency**: Every 2-4 weeks for soft stone (sandstone), every 2-3 months for hard stone (granite, burrstone). Industrial mills keep spare stone pairs.
- **Dressing tools**: Carbide-tipped chisels, stone pick (hardened steel point). Wooden measuring template to verify furrow depth and angle.
- **Furrow pattern**: "Quarter dress" (furrows radiate from center in four quarters) is most common for grain. Furrow depth: 3-8 mm at center, tapering to 1-2 mm at edge. Furrow angle: 15-25° to the tangent.
- **Stone balance**: Runner stone must be dynamically balanced to prevent vibration. Unbalanced stones cause bearing wear, uneven grinding, and structural damage. Balance checked by rotating empty stone and observing for wobble.
- **Stone selection**: French burrstone (siliceous limestone from La Ferté-sous-Jouarre) was historically the premium millstone material — porous, hard, self-sharpening. Equivalent: any fine-grained siliceous stone with natural porosity.

### Power Transmission for Mills

Converting water wheel or wind shaft rotation to millstone rotation requires a power transmission system:

- **Gear ratios**: Water wheels typically rotate at 5-15 RPM. Millstones need 80-120 RPM. Gear ratio 6:1 to 15:1 required.
- **Wooden gears**: Lignum vitae or oak cog wheels on elm or ash shafts. Wooden gears are self-lubricating (lignum vitae contains natural oils) but wear out every 3-5 years. Replacement requires a wheelwright.
- **Iron gears**: Cast iron gear wheels on wrought iron shafts. Last 20+ years. Require lubrication (tallow or oil).
- **Belt drives**: Leather or canvas belts on wooden or iron pulleys. Allow flexible power routing. Belt slip at high loads acts as a natural safety mechanism (prevents jamming).
- **Bearings**: Wooden bearing blocks lubricated with tallow (simple, needs frequent replacement). Babbitt metal bearings (tin-antimony-copper alloy) for iron shafts — much longer lasting, still require oil lubrication.
- **Power losses**: Typical 15-25% power loss through gear friction and belt slip in a well-maintained mill. Poorly maintained mills lose 40-60%.

### Byproducts and Waste Utilization

Milling produces valuable byproducts beyond flour:

- **Bran (pericarp + aleurone layer)**: 12-15% of grain weight. High in fiber (40-50%), protein (14-16%), fat (4-5%), and minerals. Used for animal feed (cattle, poultry), dietary fiber supplement, and bran oil extraction. Bran oil (from rice bran) contains oryzanol — a valuable antioxidant.
- **Wheat germ**: 2-3% of grain weight. Rich in vitamin E, B vitamins, and protein (25-28%). Used as nutritional supplement. Contains lipase enzyme that causes rancidity — must be stabilized by toasting or refrigeration.
- **Middlings**: Intermediate particles between flour and bran. Used for animal feed or re-milled. Sometimes marketed as "farina" or "cream of wheat" for porridge.
- **Mill screen waste**: Oversize particles caught on final screen. Can be re-milled or fed to livestock.
- **Dust**: Flour dust is explosive. Minimum explosive concentration: 40-60 g/m³. All electrical equipment in mills must be explosion-proof. Dust collection systems (cyclone separators + bag filters) are mandatory. Historical flour mill explosions were a major industrial hazard.

## References

- [Foundations: Food & Agriculture](../foundations/food-agriculture.md) — grain cultivation provides the raw material
- [Energy](../energy/index.md) — water/wind/steam power drives the millstones or rollers
- [Metals](../metals/index.md) — iron/steel for roller mills, gear trains, and wire screens
- [Brewing & Distilling](brewing.md) — malted grain requires milling to expose starches for mashing
- [Food Fermentation](fermentation.md) — sourdough bread uses fermented flour
- [Ceramics](../ceramics/index.md) — grain storage vessels
- [Machine Tools](../machine-tools/index.md) — precision machining for roller mill components

---

*Part of the [Bootciv Tech Tree](../index.md) • [Food Processing](./index.md) • [All Domains](../index.md)*
