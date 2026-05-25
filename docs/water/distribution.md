# Water Distribution

> **Node**: `water.distribution`
> **Parent**: [Water](index.md)
> **Timeline**: Years 5-25
> **Outputs**: water_distribution, irrigation, pressurized_water

Transporting water from source to point of use. Once a reliable water
source exists (see [Water Procurement](procurement.md)), the next
challenge is moving water to where people need it — for drinking,
washing, irrigation, and industrial processes. Distribution systems
range from simple gravity channels to pressurized pipe networks.

## Gravity-Fed Systems

Gravity is the cheapest and most reliable motive force for water. Every
distribution system should exploit gravity wherever possible.

### Open Channels and Canals

The simplest distribution method: excavated earth or lined channels.

- **Gradient**: Minimum 0.1% slope for adequate flow. Steeper channels
  erode; flatter channels silt up.
- **Lining**: Unlined canals lose 30-60% of water to seepage. Clay,
  stone, or concrete lining reduces losses to 5-10%.
- **Flow rate**: Manning's equation estimates flow. A 0.5 m wide × 0.3 m
  deep channel at 0.2% slope moves roughly 50-100 L/s.
- **Erosion control**: Drop structures at elevation changes. Vegetation
  on banks stabilizes soil.
- **Typical applications**: Irrigation, conveying water to settlements,
  routing water to treatment facilities.

### Aqueducts

Covered or elevated channels for long-distance water transport. Roman
aqueducts maintained consistent gradients over distances of 50+ km.

- **Design gradient**: 0.1-0.3% (1-3 meters per kilometer). Requires
  careful surveying with leveling instruments.
- **Cross-section**: Typically 0.5-1.5 m². Flow velocity 0.5-1.5 m/s.
- **Construction**: Stone or brick with waterproof cement mortar lining.
  Arcaded bridges where terrain demands elevation.
- **Capacity**: Roman aqueducts delivered 1,000-190,000 m³/day. The
  Aqua Claudia supplied 185,000 m³/day to Rome.
- **Maintenance**: Regular inspection for leaks, vegetation intrusion,
  and silt accumulation. Annual cleaning recommended.

### Qanats (Infiltration Galleries)

Persian water tunnels that tap groundwater at the base of hills and
deliver it to valleys via gently sloping underground tunnels.

- **Construction**: Dig a mother well into the water table, then tunnel
  downhill with maintenance shafts every 20-30 meters.
- **Gradient**: 0.05-0.5%. Water flows by gravity from aquifer to
  surface.
- **Advantage**: No pumping required. Evaporation losses near zero.
  Natural filtration through soil.
- **Yield**: 0.5-50 L/s depending on aquifer and tunnel length.
- **Longevity**: Some qanats have operated continuously for over 2,000
  years.

## Pipe Systems

Sealed pipes deliver water with minimal contamination and evaporation
losses. Material selection determines pressure capability and longevity.

### Pipe Materials (Progression)

1. **Bamboo and wood**: Split bamboo or bored wooden logs. Low pressure
   (0.1-0.5 bar). Life span 3-10 years. Suitable for short runs and
   irrigation.
2. **Clay (terracotta)**: Fired clay pipes with socket joints sealed
   with clay or bitumen. Low to moderate pressure (0.5-2 bar). Life span
   50+ years. Used extensively in Indus Valley and Minoan civilizations.
3. **Lead**: Soft, easily worked, corrosion-resistant. Cast or rolled
   sheets. Moderate pressure (2-5 bar). **Health hazard: lead
   poisoning.** Should be avoided for potable water.
4. **Cast iron**: Sand-cast pipes with bell-and-spigot joints sealed
   with lead or cement. High pressure (5-20 bar). Life span 100+ years.
   Requires metallurgy capability.
5. **Steel**: Welded or riveted steel pipes. Very high pressure (20-100
   bar). Requires machine tools and welding capability.
6. **Concrete**: Reinforced concrete pressure pipes for large-diameter
   mains. Cast in situ or precast.

### Hydraulic Design Fundamentals

- **Pressure**: 1 bar ≈ 10 meters of water head. Typical distribution
  systems operate at 2-6 bar (20-60 meter head).
- **Pipe sizing**: Larger pipes have lower friction losses. Undersized
  pipes waste energy; oversized pipes waste material.
- **Friction loss**: Hazen-Williams equation estimates head loss per
  meter of pipe. Smooth pipes (iron, steel): C=130. Rough pipes (old
   clay): C=80.
- **Air locks**: High points in pipelines trap air, blocking flow.
   Install air release valves at all local high points.

## Reservoirs and Storage

Storage buffers supply against variable demand and source fluctuations.

- **Service reservoirs**: Located at high points near settlements.
  Capacity: typically 1-2 days of peak demand. Construction: stone,
   concrete, or ferrocement. Covered to prevent contamination.
- **Break-pressure tanks**: In mountainous terrain, reduce pressure
  before distribution. Prevents pipe bursts from excessive static head.
- **Elevated tanks**: Steel or concrete tanks on towers. Provide
  consistent pressure in flat terrain. Typical height: 15-30 meters for
  1.5-3 bar pressure.

## Pressurized Systems

When gravity alone cannot deliver adequate pressure, mechanical pumping
is required.

- **Hand pumps**: Simple reciprocating pumps for wells. Lift water up to
  7 meters by suction; beyond that requires pump at depth.
- **Wind pumps (windmills)**: Multi-blade windmills drive reciprocating
  pumps. Typical yield: 5-20 m³/day in moderate wind regions.
- **Steam pumps**: Newcomen and Watt engines driving force pumps. Enable
  large-scale water supply for cities.
- **Centrifugal pumps**: After electric motors become available. Highly
  efficient for continuous supply.

## Irrigation Distribution

Agricultural water demand typically exceeds domestic demand by 10-50×.

- **Flood irrigation**: Simplest method — flood fields from canals. Low
  efficiency (30-50%) but minimal infrastructure.
- **Furrow irrigation**: Channels between crop rows. Moderate efficiency
  (50-70%).
- **Sprinkler systems**: Pressurized pipes with spray nozzles. Requires
  pumps and metal piping. Efficiency 70-85%.

## Dependencies

- [Water Procurement](procurement.md) — must have water before
  distributing it
- [Foundations](../foundations/index.md) — basic tools and construction
  capability
- [Chemistry: Cement & Concrete](../chemistry/cement.md) — for
  reservoir and aqueduct construction
- [Metals: Iron & Steel](../metals/iron-steel.md) — for iron and steel
  pipe systems

## Enables

- [Sewage Collection & Treatment](sewage.md) — distribution
  infrastructure parallels sewage collection
- [Basic Water Treatment](basic-treatment.md) — treatment plants
  receive water via distribution

[↑ Back to Water Infrastructure](index.md)
