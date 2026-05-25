# Grain Milling

> **Node ID**: food-processing.milling
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: [`foundations.food-agriculture`](../foundations/food-agriculture.md), [`energy`](../energy/index.md)
> **Timeline**: Years 0-20
> **Outputs**: flour, bran, grits, meal

### Overview

Grain milling converts harvested grain into flour — the single most important food processing operation in civilization. A workforce that eats bread is 2-3x more calorie-efficient than one eating whole-grain porridge. Milling also produces bran (animal feed), grits (coarse meal), and germ (oil source). The progression from hand-powered stone grinding to water-powered millstones to roller milling mirrors the broader energy revolution: each step multiplies throughput by 5-10x while reducing human labor.

This capability begins with stone-age saddle querns (covered in [Agriculture & Food Production](../foundations/food-agriculture.md)) and extends through industrial roller milling. The focus here is on the technological progression beyond hand querns.

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
- **Overshot wheel**: Water flows over the top of the wheel. Efficiency 60-70%. Requires a headrace (eleviated water channel). 2-4 m diameter wheel.
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

### Safety and Quality

- **Milling temperature**: Stone mills generate friction heat. Flour temperature must stay below 55°C or gluten proteins denature. Water cooling on roller mills maintains 25-35°C.
- **Moisture control**: Grain must be tempered to 15-16% moisture before milling. Too dry = shatters into fine powder (no separation). Too wet = clogs screens. Tempering time: 8-24 hours.
- **Insect contamination**: Mediterranean flour moth (Ephestia kuehniella) is the primary pest. Flour must be sifted and stored in sealed containers. Phosphine fumigation for infestations (requires careful ventilation — phosphine is lethal).
- **Aflatoxin risk**: Mold-contaminated grain (Aspergillus flavus) produces aflatoxin, a potent carcinogen. Grain must be visually inspected and moisture-kept below 13% for storage. UV fluorescence screening detects contaminated lots.

### Dependency Chain

Milling depends on:
- **[foundations.food-agriculture](../foundations/food-agriculture.md)**: Grain cultivation provides the raw material
- **[energy](../energy/index.md)**: Water/wind/steam power drives the millstones or rollers
- **[metals](../metals/index.md)**: Iron/steel for roller mills, gear trains, and wire screens

Milling enables:
- **[Baking](#)** (implicit in food processing): Flour is the primary input for bread, the staple calorie source
- **[Brewing](brewing.md)**: Malted grain (sprotten then dried) requires milling to expose starches for mashing

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

### Byproducts and Waste Utilization

Milling produces valuable byproducts beyond flour:

- **Bran (pericarp + aleurone layer)**: 12-15% of grain weight. High in fiber (40-50%), protein (14-16%), fat (4-5%), and minerals. Used for animal feed (cattle, poultry), dietary fiber supplement, and bran oil extraction. Bran oil (from rice bran) contains oryzanol — a valuable antioxidant.
- **Wheat germ**: 2-3% of grain weight. Rich in vitamin E, B vitamins, and protein (25-28%). Used as nutritional supplement. Contains lipase enzyme that causes rancidity — must be stabilized by toasting or refrigeration.
- **Middlings**: Intermediate particles between flour and bran. Used for animal feed or re-milled. Sometimes marketed as "farina" or "cream of wheat" for porridge.
- **Mill screen waste**: Oversize particles caught on final screen. Can be re-milled or fed to livestock.
- **Dust**: Flour dust is explosive. Minimum explosive concentration: 40-60 g/m³. All electrical equipment in mills must be explosion-proof. Dust collection systems (cyclone separators + bag filters) are mandatory. Historical flour mill explosions were a major industrial hazard.
