# Float Glass Process

> **Node ID**: glass.basic.float-glass
> **Domain**: [Glass](./index.md)
> **Dependencies**: [`metals.non-ferrous`](../metals/non-ferrous.md), [`gas-handling`](../gas-handling/index.md), [`energy.electric-furnaces`](../energy/electric-furnaces.md)
> **Enables**: Architectural glazing, automotive glass, mirrors, solar panel cover glass, display substrates
> **Timeline**: Years 30-50
> **Outputs**: float_glass, flat_glass_ribbon
> **Critical**: No — enables high-volume flat glass but not a bootstrap bottleneck; rolled and polished flat glass suffices at smaller scale


The float glass process, invented by Sir Alastair Pilkington in 1952 and commercially deployed in 1959, produces perfectly flat glass with parallel surfaces by floating molten glass on a bath of molten tin. It eliminated the expensive grinding and polishing steps previously required for quality flat glass and now accounts for over 90% of worldwide flat glass production — roughly 80 million tonnes per year. The process combines high-temperature materials science, precise atmosphere control, and continuous-process engineering into a single production line 50-70 meters long.

Without float glass, flat glass production relies on the rolled glass method (pour molten glass onto a flat table, roll to thickness, then grind and polish both surfaces). Rolling wastes 15-20% of the glass as grinding swarf, requires expensive abrasive materials, and produces glass with residual wave distortion. Float glass produces optically smooth surfaces directly from the tin bath — no grinding, no polishing, no material waste. The economic advantage is decisive at any scale above artisan production.

## Prerequisites

**Materials:**
- [Soda-lime glass batch](basic.md) (SiO₂ 73%, Na₂O 14%, CaO 10%, Al₂O₃ 2%) — the same composition used for container glass, melted in a [tank furnace](basic.md)
- [Tin](../metals/non-ferrous.md) (≥99.9% purity) — 100-200 tonnes for a standard float bath, replaced every 3-5 years as impurities accumulate
- [Nitrogen gas](../gas-handling/index.md) (≥99.99% purity) — 1000-3000 m³/hour continuous supply for atmosphere control
- [Hydrogen gas](../gas-handling/index.md) (≥99.9% purity) — 30-100 m³/hour, mixed with nitrogen to form reducing atmosphere (typically 95% N₂ / 5% H₂)
- [Cullet](basic.md) (crushed scrap glass) — 20-25% of batch for fuel efficiency

**Tools:**
- [Tank furnace](basic.md) capable of 1500-1600°C continuous melting (1-500 tonnes/day throughput)
- Tin bath structure: refractory-lined steel casing, 4-8 m wide × 50-70 m long × 0.6-1 m deep
- [Electric resistance heating elements](../energy/electric-furnaces.md) — tin bath temperature control (top heaters, 50-100 kW per zone)
- Annealing lehr — 80-120 m long tunnel furnace with controlled cooling gradient
- Atmosphere control system — gas mixing panel, flow controllers, oxygen sensors
- Ribbon edge rollers and thickness control devices (top rollers, knurled wheels)
- Cutting and snapping table for glass ribbon

**Knowledge:**
- Viscosity-temperature relationship for soda-lime glass at 600-1100°C
- Tin-glass interfacial tension and equilibrium thickness (~6.76 mm for soda-lime on tin at 1000°C)
- Atmosphere dew point control (< -40°C to prevent tin oxidation)
- Continuous process control for a 24/7 production line

**Infrastructure:**
- [Gas handling and purification](../gas-handling/index.md) — nitrogen generation (pressure swing adsorption or cryogenic distillation), hydrogen supply (steam methane reforming or electrolysis)
- [Electric furnaces and power supply](../energy/electric-furnaces.md) — reliable 1-5 MW electrical supply for tin bath heaters
- Industrial water cooling for lehr and cutting systems
- Material handling: batch charging system, glass ribbon conveyor, automated cutting

## The Pilkington Process

### Stage 1: Glass Melting

Soda-lime glass batch is melted in a [continuous tank furnace](basic.md) at 1500-1600°C. The furnace operates 24/7 — a float line runs continuously for 10-15 years between major rebuilds. Raw materials (silica sand, soda ash, limestone, feldspar, cullet) are automatically weighed, mixed, and charged at the batch charging end. The melt flows through distinct zones:

- **Melting zone** (1500-1600°C): Raw materials dissolve into the glass melt. Carbonates decompose, releasing CO₂. Electric boost heating supplements fossil-fuel firing to achieve target temperature.
- **Refining zone** (1500-1550°C): Fining agents (sodium sulfate Na₂SO₄, 0.5-1%) release SO₂ and O₂ bubbles that sweep up smaller bubbles. Temperature is raised to reduce viscosity and allow bubble rise. Glass must be seed-free before entering the float bath.
- **Conditioning zone** (1100-1200°C): Glass cools to working temperature. Homogenized by stirring and thermal convection. Temperature must be uniform within ±5°C across the full width before delivery to the tin bath.

The conditioned glass exits the furnace through a canal called the **lip tile** — a narrow channel (0.6-1.0 m wide) that controls the flow rate onto the tin bath. A refractory tweel (adjustable gate) regulates the glass depth and flow velocity.

### Stage 2: Tin Bath (Float Chamber)

The heart of the process. Molten glass at ~1050°C flows from the lip tile onto a bath of molten tin held at 600-1000°C (temperature varies along the bath length). The tin bath is the single most critical and expensive component of the float line.

**Physical principle**: Molten soda-lime glass (density ~2.4 g/cm³) floats on molten tin (density 7.3 g/cm³ at 1000°C) because glass is less dense. Surface tension and gravity establish an equilibrium thickness of approximately 6.76 mm for soda-lime glass at 1000°C, determined by the ratio of glass-tin and glass-atmosphere interfacial tensions. This equilibrium is known as the **Pilkington equilibrium thickness**.

**Tin bath construction**:
- Dimensions: 4-8 m wide × 50-70 m long × 60-100 mm tin depth
- Tin inventory: 100-200 tonnes per bath (at ~$25,000/tonne, the tin alone costs $2.5-5 million)
- Refractory lining: high-alumina or chromia refractories resistant to tin erosion
- Steel casing: water-cooled outer shell to protect structural steel from heat
- Top heaters: electric resistance elements (molybdenum disilicide MoSi₂ or silicon carbide SiC) suspended above the bath for temperature control
- Bath divided into 8-12 temperature zones, each independently controlled

**Tin bath atmosphere control**:
The tin bath operates under a carefully controlled atmosphere of nitrogen and hydrogen (typically 92-97% N₂, 3-8% H₂). This is essential because tin oxidizes readily at elevated temperatures:

- **Without atmosphere control**: Tin reacts with oxygen to form SnO and SnO₂ on the surface. These tin oxides contaminate the glass bottom surface, causing hazing, adhesion defects, and optical distortion. Even 10 ppm O₂ causes visible defects over hours of production.
- **Reducing atmosphere**: The H₂ component (minimum 2-3%) scavenges any oxygen that enters the bath enclosure, reacting to form H₂O vapor that is swept out by the nitrogen gas flow. Oxygen levels are maintained below 1 ppm.
- **Dew point control**: Atmosphere dew point must be kept below -40°C (preferably below -60°C) to prevent water from reacting with tin. Moisture in the atmosphere produces stannic hydroxide and causes tin pickup on the glass surface.
- **Gas flow**: 1000-3000 m³/hour of nitrogen + 30-100 m³/hour of hydrogen, supplied from [gas handling systems](../gas-handling/index.md). Gas enters at the exit end and flows countercurrent to the glass ribbon, exiting near the entry seal.

**Tin contamination management**: Over time, impurities accumulate in the tin bath — iron, lead, and zinc dissolve from the glass; atmospheric oxygen and moisture cause surface oxidation. Tin is replaced every 3-5 years during major line rebuilds. Contaminated tin is refined and recycled.

### Stage 3: Ribbon Formation and Thickness Control

As the glass flows onto the tin bath, it spreads laterally and thins toward the equilibrium thickness (~6.76 mm). The glass ribbon travels the full length of the tin bath (50-70 m) in 5-10 minutes, cooling from ~1050°C at entry to ~600°C at exit.

**Thickness control mechanisms**:

- **Natural (equilibrium) thickness**: ~6.76 mm for soda-lime glass — no mechanical intervention needed. The ribbon self-levels through surface tension and gravity.
- **Thinner glass (< 6 mm)**: Edge rollers called **top rollers** or **knurled wheels** grip the edges of the ribbon and stretch it longitudinally, pulling the glass thinner. By adjusting roller speed and pull rate, thickness is controlled down to 0.5 mm (for specialty applications). Standard thin products: 2 mm, 3 mm, 4 mm, 5 mm.
- **Thicker glass (> 7 mm)**: The ribbon is constrained from spreading laterally using **fenders** (water-cooled graphite or refractory barriers) that dam the glass edges. Preventing lateral spread forces the glass to maintain greater thickness. Alternatively, a second stream of glass can be overlaid on the first. Standard thick products: 8 mm, 10 mm, 12 mm, 15 mm, 19 mm, 25 mm.

**Typical production speeds**: 2-25 m/min depending on glass thickness. Thinner glass moves faster; thick glass moves slower. A single float line produces 400-1000 tonnes per day.

### Stage 4: Annealing Lehr

The glass ribbon exits the tin bath at ~600°C onto a roller conveyor that carries it into the **annealing lehr** — a long tunnel furnace (80-120 m) with a precisely controlled cooling gradient.

- **Entry temperature**: ~600°C (above the annealing point of 510-550°C)
- **Cooling rate**: 1-5°C/min through the critical strain point range (450-510°C). Faster cooling would lock in thermal stresses that weaken the glass and cause distortion during cutting.
- **Exit temperature**: ~50-80°C (cool enough for inspection and cutting)
- **Residence time**: 30-60 minutes depending on glass thickness
- The lehr uses electric heaters and forced-air cooling zones to maintain the precise temperature profile. Temperature uniformity across the ribbon width must be within ±3°C to prevent bowing or warping.

**Stress measurement**: Annealed float glass typically has less than 15 nm/cm of residual stress (measured by birefringence with a polarimeter). This is well below the 40 nm/cm threshold for architectural glass standards.

### Stage 5: Cutting and Packaging

The continuous glass ribbon is cut to size at the end of the line:

- **Cross-cutting**: A scoring wheel (tungsten carbide) scores the top surface, then the glass snaps cleanly along the score line. Automated scoring machines cut at 60-120 cuts per minute for standard sizes.
- **Edge trimming**: The ribbon edges (which touched the top rollers and contain thickness irregularities) are scored and removed first. Edge waste: 100-200 mm per side, recycled as cullet.
- **Quality inspection**: Automated optical scanners detect bubbles, tin pickup, scratches, and inclusions. Laser scanners measure thickness to ±0.01 mm across the full sheet. Defective regions are marked and culled.
- **Standard sheet sizes**: 3.21 m × 6.0 m (jumbo sheets) down to custom sizes. Sheets are stacked on racks for shipping or further processing (tempering, laminating, coating).

## Glass Composition for Float Glass

Float glass uses a standard soda-lime composition optimized for the float process:

| Oxide | Weight % | Function | Source |
|-------|----------|----------|--------|
| SiO₂ | 72-74% | Glass network former | Silica sand |
| Na₂O | 13-15% | Flux — lowers melting point | Soda ash (Na₂CO₃) |
| CaO | 8-10% | Stabilizer — prevents water solubility | Limestone (CaCO₃) |
| MgO | 3-4% | Prevents devitrification | Dolomite |
| Al₂O₃ | 0.5-2% | Improves chemical durability | Feldspar |
| Fe₂O₃ | 0.05-0.15% | Natural impurity (green tint) | Sand impurity |

**Iron content**: Even 0.05% Fe₂O₃ produces a faint green tint visible in thick sections. Ultra-clear float glass (for solar panels and display glass) uses iron-free sand (<0.01% Fe₂O₃), producing glass with >91% visible light transmission versus ~85% for standard float glass.

**Tin-side vs. air-side**: The bottom surface of float glass (tin side) absorbs a microscopic layer of tin (10-50 μg/cm² of tin) during the float process. This tin layer is detectable by UV fluorescence (the tin side glows under 254 nm UV light). The tin side affects downstream processes:
- Coatings adhere differently to tin side vs. air side
- The tin side is slightly harder (tin diffusion into the glass surface)
- Tempering may cause tin-side blooming (microscopic surface haze) if tin concentration is high

## Product Applications

**Architectural glazing** (60-65% of float glass production):
- Windows, curtain walls, skylights — single pane or insulated glass units (double/triple glazing)
- Tempered float glass (heat-soaked at 620-650°C, then rapidly cooled) — 4-5× stronger than annealed, breaks into small dice rather than sharp shards. Required for safety glazing (doors, shower enclosures, automotive side windows).
- Laminated glass (PVB interlayer between two sheets) — holds together when shattered. Used for automotive windshields, skylights, security glazing.

**Automotive glass** (10-15%):
- Side windows: tempered float glass, 3-5 mm
- Windshields: laminated float glass (2 × 2.1 mm + 0.76 mm PVB)
- Backlites: tempered, often with ceramic frit band for UV protection

**Mirrors** (5-8%):
- Float glass coated with silver (0.5-1 g/m²) + copper protective layer + paint backing
- Silver reflects 92-95% of visible light. Alternative: aluminum coating (85-90% reflectance)

**Solar panel cover glass** (3-5 mm, low-iron):
- Ultra-clear float glass (<0.01% Fe₂O₃) maximizes light transmission to photovoltaic cells
- Textured surface (patterned rollers) reduces reflection losses from 4% to <2%
- Must survive 25+ years of outdoor exposure without degradation

**Display glass** (0.5-1.1 mm):
- Ultra-thin float glass for LCD, OLED, and touchscreen substrates
- Requires <0.01% Fe₂O₃, <1 defect per m² for bubbles >0.1 mm
- Produced on specialty float lines with extreme thickness control

**Further processed products**:
- [Photomask substrates](photomask-substrates.md) — high-purity fused silica, not float glass, but float glass production infrastructure supports the broader glass industry
- Coated glass (low-E coatings, solar control coatings) — applied by magnetron sputtering or chemical vapor deposition
- Fire-rated glass (ceramic or wire-inserted float glass)

## Engineering Parameters

**Float line specifications (typical 600 tonnes/day line)**:

| Parameter | Value |
|-----------|-------|
| Tin bath dimensions | 6 m wide × 60 m long |
| Tin inventory | 150-200 tonnes |
| Glass ribbon width | 3.2-4.0 m (after edge trimming) |
| Production speed | 2-15 m/min (thickness dependent) |
| Daily output | 400-800 tonnes (500-1000 m²/hour) |
| Power consumption | 3-8 MW (tin bath heaters, lehr, auxiliaries) |
| Gas consumption (N₂) | 1500-2500 m³/hour continuous |
| Gas consumption (H₂) | 50-80 m³/hour continuous |
| Natural gas (melting furnace) | 1500-3000 m³/hour |
| Tin replacement interval | 3-5 years (during major rebuild) |
| Campaign length | 10-15 years continuous operation |

**Key temperatures**:

| Location | Temperature |
|----------|-------------|
| Glass delivery to tin bath | 1050-1100°C |
| Tin bath entry zone | 1000-1050°C |
| Tin bath exit zone | 600-650°C |
| Annealing lehr entry | ~600°C |
| Annealing lehr exit | 50-80°C |
| Tin melting point | 232°C |
| Tin boiling point | 2602°C |
| Glass annealing point | 510-550°C |
| Glass strain point | 470-510°C |

## Safety & Hazards

- **Molten tin exposure**: The tin bath operates at 600-1050°C. Tin splashes cause severe burns similar to molten glass. The atmosphere inside the bath enclosure is nitrogen/hydrogen — oxygen-deficient and explosive if mixed with air. Personnel must never enter the bath enclosure during operation. Maintenance access requires complete purging with air and atmospheric verification before entry.
- **Hydrogen atmosphere**: The nitrogen/hydrogen atmosphere (3-8% H₂) is within the explosive range for hydrogen-air mixtures (4-75% H₂ in air). Strict sealing of the tin bath enclosure and continuous positive-pressure gas flow prevent air ingress. Hydrogen detectors alarm at 1% H₂ in the workplace atmosphere. Nitrogen asphyxiation hazard exists in enclosed spaces near the gas supply system — nitrogen displaces oxygen without warning signs.
- **Continuous operation hazard**: A float line operates 24/7 for 10-15 years. Stopping and restarting costs millions of dollars in lost production and tin bath damage. Maintenance is performed on running equipment with extensive safety protocols. Molten glass and tin are always present — there is no "cold" state during a campaign.
- **Tin toxicity**: Metallic tin has low toxicity, but organotin compounds and tin oxide fume can cause health effects. Tin oxide (SnO₂) exposure limits: 2 mg/m³ TWA. Local exhaust ventilation is required at tin bath access points during maintenance.

## Comparison with Alternative Flat Glass Methods

| Method | Surface Quality | Max Width | Production Rate | Waste | Capital Cost |
|--------|----------------|-----------|-----------------|-------|-------------|
| **Float process** | Excellent (no grinding needed) | 4-6 m | 400-1000 t/day | <5% (edge trim only) | $100-300M |
| Rolled/polished | Good (after grinding) | 3 m | 50-200 t/day | 15-20% (grinding swarf) | $20-50M |
| Crown glass (spun) | Fair (bullseye distortion) | 1.2 m diameter | 5-20 t/day | 30-40% | < $1M |
| Cylinder blown | Fair (flattened cylinder) | 1.2 m wide | 5-15 t/day | 20-30% | < $1M |
| Fourcault (drawn) | Good | 2.5 m | 20-80 t/day | 10-15% | $10-30M |

The float process dominates because it achieves the best surface quality at the highest throughput with the lowest waste. The barrier to entry is the enormous capital cost and the requirement for [high-purity tin](../metals/non-ferrous.md), [controlled atmosphere systems](../gas-handling/index.md), and [continuous electric heating](../energy/electric-furnaces.md).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Tin pickup (hazy bottom surface) | Oxygen ingress to tin bath atmosphere (>1 ppm O₂); high dew point | Seal bath enclosure; increase N₂/H₂ flow rate; check atmosphere dew point (<-40°C); repair gas supply leaks |
| Bloom (white haze on tin side after tempering) | Excessive tin absorption during float process | Reduce tin bath residence time; lower tin bath temperature; reduce iron content in glass (Fe₂O₃ promotes tin absorption) |
| Distortion (wave in glass ribbon) | Uneven temperature across tin bath; non-uniform glass flow from furnace | Adjust top heater zones for ±2°C uniformity; check lip tile wear; clean tweel adjustment |
| Bottom surface scratches | Roller contamination or misalignment in lehr | Inspect and clean lehr rollers; check roller alignment; ensure adequate glass temperature at lehr entry (>580°C) |
| Seeds (tiny bubbles) | Insufficient refining in melting furnace | Extend refining zone residence time; increase fining temperature to 1550-1600°C; check fining agent (Na₂SO₄) dosage |
| Thickness variation across width | Uneven top roller pressure; temperature gradient across tin bath width | Calibrate top roller gap; adjust side heaters; verify glass temperature uniformity at lip tile |
| Edge cracking | Excessive cooling rate at tin bath exit; uneven lehr cooling | Reduce cooling rate at bath exit zone; verify lehr temperature profile; check for cold air leaks into lehr |

## See Also

- [Basic Glass Production](basic.md) — glass melting, batch composition, and annealing fundamentals
- [Advanced Glass Production](advanced.md) — borosilicate and fused silica compositions
- [Glass Fibers](fibers.md) — fiberglass insulation and textile production
- [Glass Recycling](glass-recycling.md) — cullet recovery and reuse in float glass production
- [Non-Ferrous Metals](../metals/non-ferrous.md) — tin production and refining
- [Gas Handling](../gas-handling/index.md) — nitrogen and hydrogen supply systems
- [Electric Furnaces](../energy/electric-furnaces.md) — resistance heating for tin bath temperature control
- [Energy: Fuels](../energy/fuels.md) — natural gas for tank furnace firing

[← Back to Glass](index.md)
