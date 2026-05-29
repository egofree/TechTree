# Water Distribution

> **Node ID**: water.distribution
> **Domain**: [Water](./index.md)
> **Dependencies**: [`water.procurement`](procurement.md), [`foundations`](../foundations/index.md)
> **Enables**: [`water.sewage`](sewage.md), [`water.basic-treatment`](basic-treatment.md), [`agriculture`](../agriculture/index.md)
> **Timeline**: Years 5-25
> **Outputs**: water_distribution, irrigation, pressurized_water
> **Critical**: Yes — without distribution, water procurement and treatment serve only those at the source

## 1. Overview

Transporting water from source to point of use. Once a reliable water source exists (see [Water Procurement](procurement.md)), the next challenge is moving water to where people need it — for drinking, washing, irrigation, and industrial processes. Distribution systems range from simple gravity channels (achievable from Year 0) to pressurized pipe networks (requiring [metallurgy](../metals/index.md) and [pumps](../energy/steam-power.md)).

Every distribution system exploits three principles: gravity (water flows downhill), pressure (water moves from high to low pressure), and containment (pipes and channels prevent loss and contamination). The engineering challenge is applying these principles at the scale needed, with the materials available.

A settlement of 1,000 people at 50 L/person/day requires 50 m³/day of distributed water. Agricultural irrigation adds 10-50× that volume. Industrial processes (brewing, tanning, metal cooling) add further demand. Distribution infrastructure scales from a single channel serving a hamlet to aqueduct networks serving cities of millions.

## 2. Prerequisites

### Materials
- [Water source](procurement.md) with reliable yield
- Stone, brick, or [concrete](../chemistry/cement.md) for channels and aqueducts
- [Clay pipes](../ceramics/kilns.md) or [metal pipes](../metals/iron-steel.md) for sealed conveyance
- Sand and gravel for pipe bedding

### Tools
- Surveying instruments (level, plumb bob, measuring cord) for gradient control
- Digging tools for trench excavation
- Lifting equipment (ropes, pulleys, levers) for pipe and stone placement

### Knowledge
- Basic surveying and gradient calculation
- Hydraulic principles (flow, pressure, friction)
- Joint sealing techniques for the pipe material chosen

### Infrastructure
- Labor force (10-100+ people depending on scale)
- Access route along the distribution corridor

## 3. Bill of Materials

| Material | Quantity per 100 m of channel/pipe | Source | Alternatives |
|----------|-----------------------------------|--------|-------------|
| Stone or concrete (open channel) | 10-50 m³ | [Quarry](../mining/extraction.md) or [Cement](../chemistry/cement.md) | Earth (unlined, high seepage) |
| Clay pipe (terracotta, 100 mm) | 100 sections × 0.3 m | [Ceramics](../ceramics/index.md) | Bamboo (3-10 year life) |
| Cast iron pipe (100 mm) | 100 m | [Metals](../metals/iron-steel.md) | Steel (welded), lead (avoid for potable) |
| Cement mortar for joints | 0.2-0.5 m³ | [Chemistry: Cement](../chemistry/cement.md) | Clay seal, rubber gaskets |
| Sand for pipe bedding | 1-3 m³ | River or quarry | No substitute — protects pipe from settling |

## 4. Process Description

### Gravity-Fed Open Channels

The simplest and most energy-efficient distribution method. Used from the earliest civilizations through modern irrigation.

**Prerequisites**: Surveying tools, [construction materials](../chemistry/cement.md), water source at higher elevation than the delivery point.

**Materials**: Earth, stone, brick, or concrete for channel construction. Clay or cement mortar for lining.

**Construction**:
1. Survey the route from source to delivery point. Measure the total elevation drop. Calculate the required gradient: minimum 0.1% slope for adequate flow. Steeper channels erode; flatter channels silt up.
2. Mark the channel centerline with stakes. For long routes, use a water level or sight level to maintain consistent gradient (1-3 m drop per km).
3. Excavate the channel to design cross-section: typically 0.3-1.0 m wide at the base, with sides sloped at 1:1 to 1:1.5 (horizontal:vertical) for stability.
4. Line the channel: unlined canals lose 30-60% of water to seepage. Clay lining reduces losses to 10-20%. Stone or concrete lining reduces losses to 5-10%.
5. Install drop structures at elevation changes greater than 0.5 m to prevent erosion. Construct from stone or concrete with a stilling basin at the base.
6. Install intake structures with coarse screens (bar screens, 20-50 mm spacing) to exclude debris.

**Calibration**: Measure flow rate at the delivery point using a weir (V-notch or rectangular). Compare to design flow. Manning's equation estimates flow: a 0.5 m wide × 0.3 m deep channel at 0.2% slope moves roughly 50-100 L/s.

**Expected performance**: Gravity channels have operated for millennia. The Dujiangyan irrigation system in China has delivered 260 m³/s since 256 BCE. Roman aqueducts delivered 1,000-190,000 m³/day across 50+ km distances. Losses in unlined channels: 30-60%. Lined channels: 5-10%.

**Strengths**:
- Zero energy input — gravity does the work
- Constructible with stone-age tools (earth channels)
- Very long service life (centuries for stone/concrete)
- Simple to maintain — visible, accessible

**Weaknesses**:
- Requires consistent gradient from source to delivery point
- Large land footprint compared to pipes
- Vulnerable to contamination (open to environment)
- Freezing in cold climates stops flow
- Seepage losses significant without lining

### Aqueducts

Covered or elevated channels for long-distance water transport across varying terrain.

**Prerequisites**: [Stone construction](../construction/index.md), [cement mortar](../chemistry/cement.md), surveying capability, organized labor force.

**Materials**: Stone or brick, waterproof cement mortar (hydraulic lime or Portland cement), arched bridges where terrain demands elevation.

**Construction**:
1. Survey the route maintaining 0.1-0.3% gradient (1-3 m per km). This requires careful leveling instruments.
2. Build the channel as a covered stone or brick trough with waterproof cement mortar lining. Cross-section: typically 0.5-1.5 m². Flow velocity: 0.5-1.5 m/s.
3. Where terrain drops away, construct arcaded bridges (arches) to maintain the gradient. Roman arches span 5-10 m with stone piers.
4. Where terrain rises, cut tunnels or build pressurized inverted siphons (requires sealed pipe capable of withstanding pressure).
5. Install settling tanks at intervals (every 5-10 km) to remove accumulated sediment.
6. Construct a castellum divisorium (distribution tank) at the delivery point to split flow to multiple destinations.

**Expected performance**: Roman aqueducts delivered 1,000-190,000 m³/day. The Aqua Claudia supplied 185,000 m³/day to Rome across 69 km. Design life: centuries. Annual maintenance: regular inspection for leaks, vegetation intrusion, and silt accumulation.

**Strengths**:
- Very high capacity (thousands of m³/day)
- Covered channels prevent contamination
- Centuries-long service life
- Continuous gravity flow — no energy input

**Weaknesses**:
- Extremely labor-intensive to construct
- Requires organized workforce (hundreds of workers for months)
- Arcaded bridges require advanced [stone construction](../construction/index.md)
- Fixed route — cannot be easily modified or extended

### Pipe Systems

Sealed pipes deliver water with minimal contamination and evaporation losses. Material selection determines pressure capability and longevity.

**Prerequisites**: Pipe material (clay, metal, or concrete), joint sealing materials, excavation tools.

**Materials per 100 m of pipe**:

| Pipe material | Diameter range | Pressure rating | Life span | Prerequisites |
|---------------|---------------|----------------|-----------|--------------|
| Bamboo/wood | 25-75 mm | 0.1-0.5 bar | 3-10 years | None |
| Clay (terracotta) | 75-300 mm | 0.5-2 bar | 50+ years | [Ceramics](../ceramics/index.md) |
| Cast iron | 75-600 mm | 5-20 bar | 100+ years | [Metallurgy](../metals/iron-steel.md) |
| Steel | 25-1200 mm | 20-100 bar | 50+ years | [Machine tools](../machine-tools/index.md) |
| Reinforced concrete | 300-3000 mm | 2-10 bar | 75+ years | [Cement](../chemistry/cement.md) |

**Construction**:
1. Excavate trench to design depth (below frost line in cold climates, typically 0.5-1.5 m). Trench width: pipe diameter + 0.3 m on each side.
2. Place sand bedding in the trench bottom (10-15 cm) to provide uniform support.
3. Lay pipe sections from downstream (outlet) to upstream (inlet). Each section should seat fully into the previous joint.
4. Seal joints: clay pipes — cement mortar or bitumen; cast iron — lead caulked or rubber gasket; steel — welded or bolted flanges.
5. Backfill in layers, compacting each layer. Place warning tape 30 cm above pipe for future excavation awareness.
6. Install air release valves at all local high points to prevent air locks.
7. Install isolation valves (gate valves) at branch connections and every 200-500 m for maintenance isolation.
8. Pressure test the completed section before backfilling: fill with water, pressurize to 1.5× operating pressure, hold for 2 hours. No visible leaks.

**Calibration**: After installation, pressure test at 1.5× design pressure. Measure flow at outlet and compare to design. Check for leaks by monitoring pressure drop over 24 hours (should be <0.1 bar).

**Expected performance**: Head loss per 100 m of pipe (Hazen-Williams formula):
- Cast iron (C=130): 0.5-2.0 m head loss at 10-50 L/s in 100 mm pipe
- Old clay (C=80): 1.5-6.0 m head loss at same flow
Typical distribution pressure: 2-6 bar (20-60 m head). Higher pressures require stronger pipe materials.

**Strengths**:
- Sealed system prevents contamination
- Can deliver water uphill with pumping
- Minimal land footprint (buried)
- Low evaporation and seepage losses

**Weaknesses**:
- Requires pipe manufacturing capability (clay firing, metal casting)
- Buried pipes are harder to inspect and repair
- Pressure surges (water hammer) can burst pipes if not controlled
- Freezing risk in cold climates (must bury below frost line or drain in winter)

### Reservoirs and Storage

Storage buffers supply against variable demand and source fluctuations.

**Prerequisites**: Construction materials ([stone](../construction/index.md), [concrete](../chemistry/cement.md), or [ferrocement](../chemistry/cement.md)), elevated site (for gravity-fed systems).

**Materials**: Concrete, stone, or ferrocement for tank construction. Cover material (timber, metal, or concrete slab) to prevent contamination.

**Construction**:
1. Select site at highest practical elevation near the settlement. For gravity systems, the reservoir must be above all delivery points.
2. Construct tank from concrete, ferrocement, or stone with waterproof lining. Capacity: 1-2 days of peak demand.
3. Install inlet pipe from source, outlet pipe to distribution, overflow pipe, and drain pipe for cleaning.
4. Cover the tank tightly to prevent contamination, mosquito breeding, and algae growth.
5. Install an access hatch with a lockable cover for inspection and cleaning.

**Expected performance**: Service reservoirs provide consistent pressure: 10 m elevation = 1 bar pressure. A reservoir 30 m above the settlement delivers 3 bar — sufficient for most domestic needs. Elevated steel tanks on towers provide pressure in flat terrain.

**Strengths**:
- Buffers supply against demand peaks and source interruptions
- Provides consistent pressure through gravity
- Enables fire-fighting reserves
- Simple to construct and maintain

**Weaknesses**:
- Large tanks are expensive to construct
- Stagnant water risks quality degradation
- Requires periodic cleaning (sediment removal)
- Elevated tanks are vulnerable to freezing in cold climates

## 5. Quantitative Parameters

| Parameter | Open channel | Aqueduct | Clay pipe | Cast iron pipe | Concrete pipe |
|-----------|-------------|---------|----------|---------------|--------------|
| Typical capacity | 10-500 L/s | 10-2,000 L/s | 1-50 L/s | 1-500 L/s | 50-5,000 L/s |
| Gradient/pressure | 0.1-1% | 0.1-0.3% | 0.5-2 bar | 5-20 bar | 2-10 bar |
| Seepage loss | 10-60% | 1-5% | <1% | <0.1% | <0.5% |
| Service life | 20-100+ years | 100-2,000+ years | 50+ years | 100+ years | 75+ years |
| Construction cost/m | $1-10 | $50-500 | $5-20 | $15-80 | $20-100 |

## 6. Scaling Notes

- **Hamlet** (50-200 people): Single gravity channel from spring or well. Earthen or stone-lined. No storage needed if source is reliable. Cost: minimal (labor only).
- **Village** (200-2,000 people): Lined channel or clay pipe network. Small service reservoir (5-20 m³). Hand pumps for wells. Cost: $500-5,000.
- **Town** (2,000-20,000 people): Cast iron or steel pipe network with service reservoirs. Fire hydrants. Requires [pumping stations](../energy/steam-power.md) for pressure. Cost: $50,000-500,000.
- **City** (20,000+ people): Steel or concrete trunk mains, distribution grid, elevated storage tanks, pump stations. Requires [electric pumps](../energy/electricity.md) and organized water utility. Cost: millions.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low pressure at delivery point | Pipe too small for flow; excessive friction loss; air lock at high point; leak in line | Check for leaks by isolating sections and pressure testing. Install air release valves at high points. Replace undersized pipe sections. |
| Pipe burst | Water hammer (sudden valve closure); freeze expansion; corrosion; excessive pressure | Install slow-closing valves. Bury pipes below frost line (0.5-1.5 m depth). Add pressure relief valves. Replace corroded sections with resistant material. |
| Channel siltation | Gradient too flat; inadequate velocity to transport sediment; upstream erosion | Increase gradient where possible. Construct desilting basins at intervals. Plant vegetation on upstream banks to reduce erosion. |
| Water contamination in distribution | Broken pipe allowing soil/wastewater ingress; backflow from contaminated connection; open channel receiving runoff | Repair leaks immediately. Install backflow preventers at cross-connections. Cover open channels. Flush and disinfect affected sections. |
| Air lock blocking flow | Air trapped at high point in pipeline, preventing water flow | Install air release valves (automatic float type or manual petcocks) at all local high points in the pipeline. |
| Reservoir water quality degrading | Long storage time; sediment accumulation; algae growth in uncovered tank; no residual chlorine | Cover tank. Add chlorine residual (0.2-0.5 mg/L). Clean sediment annually. Ensure turnover time <3 days. |

## 8. Safety

- **Trench collapse**: The primary hazard during pipe installation. Trenches deeper than 1.5 m in unstable soil must be shored (timber or hydraulic shoring) before workers enter. Fatal trench collapses occur in sand, silt, and wet soil. Slope trench walls to 1:1 (45°) or shallower in unstable ground.
- **Water pressure**: Cast iron and steel pipes at 5-20 bar contain significant stored energy. A failed fitting or joint can release high-velocity water capable of causing blunt trauma. Never pressurize a system without verifying all joints are properly sealed. Release pressure before disassembling any connection.
- **Lead pipes**: Lead was historically used for water pipes (easy to work, corrosion-resistant). Lead dissolves into standing water at concentrations above 15 µg/L, causing cumulative lead poisoning (neurological damage, especially in children). Never use lead for potable water systems. If existing lead pipes are encountered, replace with iron, clay, or plastic.
- **Drowning**: Open channels, reservoirs, and inspection chambers are drowning hazards. Cover reservoirs. Install guardrails on elevated aqueducts. Never enter a confined chamber without testing for toxic gases (use a candle test — if it extinguishes, do not enter).

## 9. Quality Control

- **Pressure testing**: After pipe installation, pressurize to 1.5× operating pressure. Hold for 2 hours. Acceptable pressure drop: <0.1 bar. Walk the line looking for visible leaks.
- **Flow measurement**: Install a V-notch weir or flow tube at the delivery point. Measure actual flow against design flow. Significant deviation indicates blockage, leak, or undersized pipe.
- **Leak detection**: For buried pipes, monitor flow at inlet and outlet. Difference indicates losses. Target: <5% loss in new installations. Monthly readings track degradation over time.
- **Water quality testing**: Test distributed water monthly for turbidity (<5 NTU), chlorine residual (0.2-0.5 mg/L if chlorinated), and fecal coliforms (0 per 100 mL).

## 10. Variations and Alternatives

- **Qanats**: Persian underground tunnels delivering groundwater by gravity across kilometers. No pumping required. Some have operated for 2,000+ years. Construction is labor-intensive but service life is exceptional. See [Water Procurement](procurement.md).
- **Pumped systems**: When gravity alone cannot deliver adequate pressure, mechanical pumping is required. Hand pumps for wells (lift 7 m by suction). Wind pumps: 5-20 m³/day. Steam pumps for city-scale supply. Centrifugal pumps after electric motors become available.
- **Irrigation-specific distribution**: Flood irrigation (30-50% efficiency), furrow irrigation (50-70%), sprinkler systems (70-85%). Agricultural demand exceeds domestic by 10-50×.
- **Simplified sewerage**: Small-diameter (100 mm) gravity sewer pipes using the same construction techniques. Dual-purpose infrastructure — water supply and sewage collection. See [Sewage Collection](sewage.md).

## 11. References

- [Water Procurement](procurement.md) — must have water before distributing it
- [Chemistry: Cement & Concrete](../chemistry/cement.md) — for reservoir and aqueduct construction
- [Metals: Iron & Steel](../metals/iron-steel.md) — for iron and steel pipe systems
- [Ceramics](../ceramics/index.md) — for clay pipe manufacture
- [Sewage Collection](sewage.md) — distribution infrastructure parallels sewage collection
- [Basic Water Treatment](basic-treatment.md) — treatment plants receive water via distribution

---
*Part of the [Bootciv Tech Tree](../index.md) • [Water](./index.md) • [All Domains](../index.md)*
