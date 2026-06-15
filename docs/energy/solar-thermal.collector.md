# Solar Thermal Collector

> **Node ID**: `energy.solar-thermal.collector`
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.solar-thermal`](./solar-thermal.md),
> [`glass.basic`](../glass/basic.md),
> [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None
> **Outputs**: thermal_energy, hot_water
> **Timeline**: Years 5-30
> **Critical**: No

## Overview

Solar thermal collectors absorb solar radiation and convert it to useful heat in a working fluid — typically water, glycol solution, thermal oil, or air. Unlike [photovoltaic panels](./photovoltaics.md), which convert only the visible and near-infrared portion of sunlight to electricity, thermal collectors can use the entire solar spectrum. They are the simplest and most efficient way to harvest solar energy for heat applications, which dominate residential and industrial energy demand.

Three collector families span a temperature range from 30°C to over 1000°C:

**Flat-plate collectors** are the workhorse of domestic and low-temperature industrial solar heat. A dark absorber plate (selectively coated copper or aluminium) under a transparent cover (single or double glazing) absorbs 90-95% of incident sunlight. Fluid tubes bonded to the absorber carry away heat. Maximum operating temperature: 60-90°C. Efficiency: 40-70% depending on temperature lift and solar irradiance. They produce [hot water](./solar-thermal.md) for domestic use, space heating, swimming pools, and low-temperature process heat (washing, food processing).

**Evacuated tube collectors** use a vacuum jacket to eliminate convective and conductive heat loss, allowing operation at 100-200°C with reasonable efficiency. Each tube contains an absorber fin with a heat pipe or direct-flow fluid tube inside a borosilicate glass envelope evacuated to <10⁻³ Pa. The vacuum makes them effective in cold climates and on overcast days. Per-unit-area cost is higher than flat-plate, but energy yield per m² is 20-40% greater, especially at higher temperatures.

**Concentrating collectors** use mirrors or lenses to focus sunlight onto a smaller receiver, achieving high flux concentration and high temperature. **Parabolic trough** collectors focus sunlight onto a linear receiver tube, heating thermal oil or molten salt to 300-400°C. **Parabolic dish** collectors achieve 500-1500°C at the focal point. **Solar power towers** use a field of mirrors (heliostats) to focus on a single receiver atop a tower, reaching 500-600°C for [steam turbine](./steam-turbines.md) power generation. Concentrating collectors require clear-sky direct (beam) radiation — they cannot use diffuse (cloudy-day) sunlight.

Solar thermal collectors are complementary to [photovoltaics](./photovoltaics.md): PV is optimal for electricity generation, while thermal collectors are 2-3× more efficient for direct heat applications. For a bootstrapping civilization, flat-plate collectors are achievable with basic materials ([copper](../metals/copper-refining.md), [glass](../glass/basic.md), selective coating), while concentrating systems require precision mirror manufacturing and sun-tracking mechanisms.

## Prerequisites

### Materials

- [Copper](../metals/copper-refining.md) — absorber plate and riser tubes for flat-plate collectors (high thermal conductivity: 400 W/m·K)
- [Aluminium](../metals/aluminum.md) — absorber fin stock, frame, reflector substrate (for concentrators). Thermal conductivity: 237 W/m·K.
- [Low-iron glass](../glass/basic.md) — transparent cover, 3-5 mm thick. Low-iron (extra-clear) glass transmits 91-92% of solar radiation vs 84-86% for standard glass.
- Selective coating — black chrome (Cr₂O₃ + Cr), nickel-pigmented alumina, or TiNOX (multilayer PVD sputtered). Absorptivity α = 0.90-0.96, emissivity ε = 0.05-0.15. This high α/ε ratio is critical: a black paint absorbs well (α=0.95) but also radiates well (ε=0.90), losing heat. A selective coating absorbs almost as well but radiates 6-18× less.
- [Insulation](../polymers/index.md) — mineral wool, polyurethane foam, or fibreglass. 30-80 mm thick on back and sides. Thermal conductivity: 0.02-0.04 W/m·K.
- Working fluid — water (domestic hot water), propylene glycol 30-50% (freeze protection), synthetic thermal oil (Dowtherm, Santowhite, max 350-400°C), molten salt (60% NaNO₃ + 40% KNO₃, "solar salt", 220-560°C)
- Reflector material (concentrating) — silvered glass mirror (reflectivity 0.92-0.96), polished aluminium (0.75-0.85), or aluminised polymer film (0.85-0.90)

### Tools and Equipment

- [Glass manufacturing](../glass/basic.md) — low-iron tempered glass cover production
- [Copper working](../metals/copper-refining.md) — tube bending, plate bonding (solder, braze, or laser weld)
- Selective coating deposition — electroplating (black chrome), PVD sputtering (TiNOX), or sol-gel (nickel-pigmented alumina)
- [Steel fabrication](../metals/iron-steel.md) — frame, support structure, tracking mechanism (for concentrators)
- Vacuum equipment — for evacuated tube production (diffusion pump or turbo-molecular pump, <10⁻³ Pa)
- Flow and temperature test rig — pump, flow meter, thermocouple array, pyranometer

### Knowledge

- Solar irradiance: peak direct normal irradiance (DNI) at sea level on a clear day: 800-1000 W/m². Global horizontal irradiance (GHI) includes diffuse component: typically 700-900 W/m² at midday. Annual totals: 1,000-2,500 kWh/m²/year depending on location.
- Collector efficiency: η = Q_useful / (A × G). Where Q_useful = m × c_p × ΔT (fluid heat gain), A is aperture area, G is solar irradiance. Efficiency decreases as the temperature difference between collector and ambient increases — the "collector efficiency curve" η = η₀ - a₁(ΔT/G) - a₂(ΔT²/G).
- Selective coating physics: a surface that has high absorptivity in the solar spectrum (0.3-2.5 μm) but low emissivity in the thermal infrared (3-30 μm) where the absorber radiates. This is achieved by interference coatings or metal-dielectric composites whose optical properties vary with wavelength.
- Concentration ratio (CR): the ratio of mirror aperture area to receiver area. CR = 1 for flat-plate, 1-5 for evacuated tube (CPC integrated), 15-80 for parabolic trough, 100-5000 for dish and tower. Higher CR → higher temperature but requires tracking accuracy of 0.1-1°.

### Infrastructure

- **Roof or ground mounting** — south-facing (in Northern hemisphere) at tilt angle approximately equal to latitude ±15° depending on seasonal optimisation target
- **Fluid circulation system** — pump (0.05-0.5 kW for domestic), expansion tank, pressure relief valve, air vent, check valve
- **Storage tank** — 50-300 L for domestic hot water; 5-50 m³ for industrial process heat; thousands of m³ (molten salt) for concentrating power plants
- **Backup heat source** — electric element, gas burner, or [boiler](./boiler.md) for periods of low solar irradiance
- **Tracking system** (concentrating only) — single-axis (trough) or dual-axis (dish, tower) tracking drive with 0.1-1° pointing accuracy

## Bill of Materials

### Flat-Plate Collector (2 m² aperture, water/glycol, domestic hot water)

| Material | Quantity per collector | Source | Alternatives |
|----------|------------------------|--------|--------------|
| Copper absorber plate (0.2-0.3 mm sheet) | 2.0 m², 3.5-5.5 kg | [Copper refining](../metals/copper-refining.md) | Aluminium plate (1.0 mm, lower conductivity, cheaper) |
| Copper riser tubes (10-15 mm dia, 0.6 mm wall) | 8-12 m, 1.5-2.5 kg | [Copper refining](../metals/copper-refining.md) | PEX polymer tubes (lower thermal conductivity, no freeze damage) |
| Selective coating (black chrome or TiNOX) | 2.0 m² deposited on absorber | Electroplating or PVD | High-temperature black paint (α=0.95, ε=0.90 — 20% lower efficiency at 60°C) |
| Low-iron tempered glass cover (4 mm) | 2.0 m², 20 kg | [Glass](../glass/basic.md) | Standard window glass (86% transmission vs 91%) |
| Aluminium frame (extruded, 30 mm × 100 mm) | 8 m linear, 3-5 kg | [Aluminium](../metals/aluminum.md) | Galvanised steel frame (heavier, corrosion risk) |
| Mineral wool insulation (50 mm) | 2.5 m², 3-4 kg | [Insulation](../polymers/index.md) | Polyurethane foam (better k, max 120°C) |
| Propylene glycol (30-50% in water) | 5-8 L | [Chemistry](../chemistry/index.md) | Ethylene glycol (toxic, food-industry prohibited) |
| Gaskets, sealants, hardware | 1 set | [Polymers](../polymers/index.md), [steel](../metals/iron-steel.md) | — |

### Evacuated Tube Collector (2 m² aperture, heat pipe)

| Material | Quantity per collector | Source | Alternatives |
|----------|------------------------|--------|--------------|
| Borosilicate glass tubes (47-58 mm OD × 1.8 m) | 20-30 tubes, 20-30 kg | [Glass](../glass/basic.md) — borosilicate (Pyrex-type) | Soda-lime glass (higher thermal expansion, poorer thermal shock resistance) |
| Selective coating (Al-N/Al, sputtered) | coated on inner tube | PVD sputtering | Black nickel (electrodeposited) |
| Copper heat pipe (condenser + evaporator) | 20-30 heat pipes, 5-8 kg total | [Copper refining](../metals/copper-refining.md) | U-tube direct flow (no heat pipe, simpler but less efficient) |
| Heat transfer fluid in heat pipe | purified water at ~0.01 bar (boils at ~7°C) | [Water treatment](../water/index.md) | Methanol (lower boiling point, for cold climates) |
| Manifold (copper header + insulation) | 1 unit, 5-8 kg | [Copper](../metals/copper-refining.md), [insulation](../polymers/index.md) | — |
| Frame (aluminium or stainless steel) | 1 unit, 5-10 kg | [Aluminium](../metals/aluminum.md) or [steel](../metals/iron-steel.md) | — |

### Parabolic Trough Collector (2.5 m aperture × 6 m length, ~15 m²)

| Material | Quantity per module | Source | Alternatives |
|----------|---------------------|--------|--------------|
| Silvered glass mirror facets (4 mm) | 15 m², 150 kg | [Glass](../glass/basic.md) — silvered back surface | Polished aluminium reflector (0.85 vs 0.94 reflectivity) |
| Steel support structure (galvanised) | 80-120 kg | [Iron and steel](../metals/iron-steel.md) | Aluminium (lighter, more expensive) |
| Receiver tube (Dewar-type, glass-to-metal seal) | 1 unit, 4 m × 70 mm | [Glass](../glass/basic.md) + [copper](../metals/copper-refining.md) | Bare tube (5-10% efficiency loss from convection) |
| Selective coating on receiver (Mo-Al₂O₃ or Ni-Cr) | 4 m × 70 mm coated | PVD sputtering | Black paint (unacceptable at 300-400°C) |
| Thermal oil (Dowtherm A or equivalent) | 20-30 L per module loop | [Chemistry](../chemistry/petroleum-alternatives.md) | Molten salt (max 560°C but freeze risk at 220°C) |
| Tracking drive (hydraulic or electric) | 1 unit per 50-100 m² | [Precision machining](../machine-tools/index.md) | Manual seasonal tilt adjustment (no daily tracking) |

## Process Description

### Flat-Plate Collector Fabrication

1. **Prepare absorber plate**: Bond copper riser tubes to absorber plate by soldering, brazing, or laser welding. Tube spacing: 100-150 mm. Bonding thermal resistance must be <0.01 K/W to ensure good heat transfer from plate to fluid. Laser welding produces the strongest bond with least thermal damage to the selective coating.
2. **Apply selective coating**: Deposit selective coating on the absorber plate surface. Black chrome: electroplate Cr₂O₃ with embedded Cr metal particles from a chromic acid bath. TiNOX: PVD sputter multi-layer coating (Al₂O₃ / AlN / Al gradient) in a vacuum chamber. Verify: absorptivity α >0.92, emissivity ε <0.12.
3. **Assemble collector box**: Construct frame from extruded aluminium sections. Install mineral wool insulation on the back (50-80 mm) and sides (20-30 mm). Fit absorber plate-tube assembly into insulated box. Connect inlet and outlet manifolds.
4. **Install glazing**: Place low-iron tempered glass cover on top of frame with EPDM gasket. Secure with aluminium retaining strip. Seal all edges with weatherproof silicone sealant.
5. **Pressure test**: Fill the tube circuit with water at 2-3 bar for 15 minutes. No leaks acceptable.
6. **Efficiency test**: Install outdoors facing south at latitude tilt. Connect to a pumped flow loop with temperature sensors and flow meter. Measure inlet and outlet temperature at solar irradiance 800-1000 W/m². Verify: efficiency η >55% at (T_collector - T_ambient)/G <0.05 K·m²/W.

### Evacuated Tube Collector Fabrication

1. **Form glass tubes**: Borosilicate glass tubes are drawn to 47-70 mm diameter, 1.5-2.0 m length. The outer tube and inner tube are fused at the top, open at the bottom for vacuum evacuation.
2. **Apply selective coating**: Deposit selective coating on the outer surface of the inner tube by PVD sputtering (Al-N-Al multilayer is standard).
3. **Insert heat pipe**: Insert a copper heat pipe with a small charge of purified water (5-10 mL) into the inner tube. The evaporator end is at the bottom (in sunlight); the condenser end extends into the manifold at the top.
4. **Evacuate**: Connect the tube to a vacuum pump. Pump down to <10⁻³ Pa. Seal the exhaust tube tip by melting it shut with a torch (glass-to-glass seal). Verify: pressure rise <10⁻² Pa over 24 hours (indicates a good seal).
5. **Assemble manifold**: Mount the condenser ends of all tubes into a copper header manifold with dry-fit sockets (heat pipe condensers slide into sleeves that thermally connect to the manifold fluid). Insulate manifold with 50-80 mm polyurethane foam.

### Parabolic Trough Collector Fabrication

1. **Fabricate parabolic reflector**: Mount curved silvered glass mirror facets onto a steel parabolic support structure. Parabolic accuracy: ±0.5° slope error to maintain focus on the receiver tube. Mirror reflectivity >0.93.
2. **Install receiver tube**: A steel absorber tube (70 mm dia) inside a glass envelope (115 mm dia) with vacuum annulus. Glass-to-metal seal at each end. Selective coating on the steel tube. Bellows accommodate differential thermal expansion.
3. **Mount and align**: Install the collector on a single-axis tracking drive that rotates the trough east-to-west to follow the sun daily. Tracking accuracy: ±0.1-0.5°. Position receiver tube precisely at the focal line.
4. **Connect thermal loop**: Route thermal oil through series-connected receiver tubes. Include expansion tank (oil expands 10-15% from cold to operating temperature), circulation pump, and heat exchanger to [steam generator](./boiler.md).

## Quantitative Parameters

| Parameter | Flat-Plate | Evacuated Tube | Parabolic Trough | Parabolic Dish |
|-----------|------------|----------------|-------------------|----------------|
| Max operating temp | 60-90°C | 120-200°C | 300-400°C | 500-1500°C |
| Optical efficiency (η₀) | 0.75-0.85 | 0.70-0.80 | 0.70-0.80 | 0.80-0.90 |
| Heat loss coefficient (a₁) | 3-6 W/m²·K | 1.0-2.0 W/m²·K | 0.1-0.3 W/m²·K | — |
| Efficiency at 0.05 K·m²/W | 50-65% | 55-70% | 65-75% | — |
| Efficiency at 0.1 K·m²/W | 20-40% | 45-60% | 60-70% | — |
| Concentration ratio | 1 | 1-5 (CPC) | 15-80 | 100-5000 |
| Tracking required | No | No | Single-axis | Dual-axis |
| Uses diffuse light | Yes | Yes | No | No |
| Aperture cost | $50-150/m² | $150-300/m² | $200-400/m² | $500-1500/m² |
| Annual energy yield | 300-800 kWh/m² | 400-1000 kWh/m² | 800-1400 kWh/m² | 1000-1800 kWh/m² |
| Lifetime | 15-25 years | 15-25 years | 20-30 years | 15-20 years |

### Collector Efficiency by Temperature Lift (G = 800 W/m²)

| (T_in - T_amb) | Flat-Plate | Evacuated Tube | Parabolic Trough |
|----------------|------------|----------------|-------------------|
| 10°C | 68-75% | 65-72% | — (not used at low ΔT) |
| 30°C | 55-65% | 60-68% | — |
| 50°C | 40-55% | 55-62% | 70-78% |
| 80°C | 15-30% | 45-55% | 65-72% |
| 120°C | <5% | 25-40% | 58-65% |
| 200°C | Not feasible | <10% | 45-55% |
| 350°C | Not feasible | Not feasible | 30-40% |

## Scaling Notes

- **Domestic scale** (2-8 m²): Single flat-plate collector or 15-30 evacuated tubes on a residential roof. Heats a 150-300 L storage tank. Provides 50-80% of annual domestic hot water demand in temperate climates. Total installed cost: $1,500-5,000.
- **Commercial scale** (20-200 m²): Array of collectors on a building roof or ground frame. Heats a 2,000-10,000 L storage tank for space heating, domestic hot water, or low-temperature process heat (food processing, car washes, swimming pools).
- **Industrial process heat** (500-10,000 m²): Large ground-mounted array of parabolic trough or flat-plate collectors. Produces 80-200°C heat for food processing, textile dyeing, chemical drying, or [desalination](../chemistry/water-electrolysis.md). Requires thermal storage (insulated tank, 5-50 m³) to buffer intermittent input.
- **Power generation** (50,000-500,000 m²): Utility-scale parabolic trough or solar tower field with molten salt storage. Generates 50-500 MW of [steam turbine](./steam-turbines.md) power. Molten salt storage (2-15 hours) enables dispatchable output after sunset.

Key scaling challenges: **intermittency** — solar input varies diurnally and seasonally; thermal storage or backup heat is essential for continuous heat supply. **Thermal losses** increase with temperature and collector area — large arrays need insulated piping runs. **Tracking system reliability** for concentrating collectors — drive motors, bearings, and controls must survive 20+ years outdoors. **Mirror degradation** — silvered glass mirrors lose reflectivity at 0.5-1.5% per year from soiling and corrosion; regular washing is required.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low collector output (efficiency <40% at rated conditions) | Dust or dirt on glazing reducing transmission by 10-30%; selective coating degraded (faded or peeling); air in fluid circuit blocking flow | Wash glass cover every 1-3 months; inspect selective coating visually (should be uniform dark blue/black, not mottled); bleed air from circuit at high points |
| Nighttime heat loss (storage tank cools 10-15°C overnight) | Reverse thermosiphoning — cold collector draws heat from tank at night; missing or failed check valve | Install swing-check valve in the supply line (opens only when pump runs); verify valve orientation (arrow pointing toward collector) |
| Freeze damage (burst tubes in winter) | Insufficient glycol concentration, or drainback system failed to drain | Test glycol concentration annually (target -30°C freeze point for 40% propylene glycol); verify drainback tank and piping slope (min 1:50) |
| Boiling in collector (steam hammer, pressure spikes) | Pump failure during high irradiance, undersized expansion tank, blocked flow | Install high-temperature cut-off sensor (shuts pump and diverts flow at 95°C); verify expansion tank sizing (10-15% of system volume); install pressure relief valve rated at 3-6 bar |
| Evacuated tube vacuum loss (tube feels hot on outside, efficiency drops 30-50%) | Glass-to-glass seal failure, mechanical impact crack | Check tube tip seal for cracks (silver coating on barium getter indicates vacuum integrity — white = vacuum lost); replace affected tube |
| Parabolic trough tracking error (receiver not at focal line) | Drive motor encoder drift, structural deflection from wind load, foundation settling | Recalibrate tracking controller seasonally; check for mechanical play in drive (backlash <0.1°); survey foundation for settling; verify sun sensor alignment |
| Selective coating oxidation (at high temperature, in flat-plate) | Air ingress at high operating temperature, coating not rated for >180°C, degradation from repeated thermal cycling | Keep collector sealed; verify gasket integrity; use high-temperature-rated coating (TiNOX-rated to 220°C, black chrome to 300°C); reduce stagnation temperature by shading or draining during idle periods |
| Stagnation damage (collector reaches 180-220°C with no fluid flow, degrading glycol and plastics) | Power outage during high irradiance; pump failure; controller fault | Install drainback or drain-pan system that empties collector on shutdown; use high-temperature glycol (propylene glycol degrades >115°C, specialised solar glycol to 180°C); shade collectors during extended shutdowns |

## Safety

- **Thermal burns**: Collector surfaces can reach 80-120°C (flat-plate) or 150-200°C (evacuated tube) during operation. Receiver tubes in parabolic troughs reach 300-400°C. Allow 30+ minutes cooling after sundown before servicing. Use thermal gloves for any hot-zone work.
- **Steam explosion**: If fluid boils in a sealed collector loop, pressure can exceed pipe and tank ratings. Install pressure relief valve (3-6 bar) at the highest point. Size expansion tank for 10-15% of system volume. Never block a pressure relief valve.
- **Concentrated sunlight (parabolic trough, dish)**: The focused beam at the receiver is intensely bright and hot. Do not look directly at the receiver — focused IR causes retinal damage. Install warning signs. Do not place hands or tools at the focal line during operation.
- **Glycol toxicity (ethylene glycol)**: If ethylene glycol is used instead of propylene glycol, it is toxic (oral LD₅₀ 1.4 mL/kg human). Propylene glycol is non-toxic (GRAS — generally recognised as safe) and preferred for domestic systems. Label all system fluid.
- **Thermal oil fire (parabolic trough)**: Synthetic thermal oils (Dowtherm A) have flash point 113°C and autoignition temperature 535°C. Leaks from overheated or degraded oil can ignite. Monitor oil degradation quarterly (total acid number, insolubles). Keep oil below 400°C operating temperature.
- **Glass breakage**: Tempered glass cover shatters into small granules if broken — less injurious than sharp shards. Evacuated tube implosion on breakage can scatter glass fragments. Wear safety glasses when handling tubes.

## Quality Control

### Acceptance Criteria

- **Instantaneous efficiency**: Tested per ISO 9806. Measured at four temperature points (ΔT/G = 0, 0.02, 0.05, 0.08 K·m²/W). Accept: η₀ >0.75 (flat-plate), >0.70 (evacuated tube). Plot efficiency curve; slope and intercept must meet manufacturer's published values within ±5%.
- **Pressure drop**: Fluid-side pressure drop at design flow rate (0.5-1.5 L/min per m²) must be <10 kPa (flat-plate) or <20 kPa (evacuated tube header). Excessive drop indicates blocked tubes or undersized manifolds.
- **Stagnation temperature**: With no fluid flow at 1000 W/m² irradiance, collector reaches equilibrium. Flat-plate: 160-200°C. Evacuated tube: 180-250°C. Verify all materials survive stagnation (gaskets, insulation, selective coating) without permanent degradation.
- **Optical efficiency (concentrating)**: Measured by calorimetric method at near-ambient temperature. Parabolic trough: η₀ >0.70. Check intercept factor ( >95% of receiver absorbs reflected energy).
- **Thermal loss (concentrating receiver)**: Heat loss per unit length at operating temperature. Parabolic trough receiver: <150 W/m at 350°C, <250 W/m at 400°C. Measured by electrically heated "cold-receiver" test.

### Testing Methods

- **Calorimetric efficiency test (ISO 9806)**: Circulate fluid at controlled inlet temperature through collector under measured solar irradiance. Measure flow rate and temperature rise. Calculate efficiency: η = (ṁ × c_p × ΔT) / (A × G).
- **Steady-state efficiency curve**: Repeat efficiency test at 4-6 inlet temperatures spanning the operating range. Fit to η = η₀ - a₁(ΔT/G) - a₂(ΔT²/G). Report η₀, a₁, a₂.
- **Thermal shock test**: Expose to simulated rain (20°C water spray) while collector surface is at 200°C. No glass fracture or seal failure. Repeat 5 cycles.
- **Exposure test (ISO 9806)**: Mount collector outdoors for 30 days of cumulative irradiance >7 MJ/m²/day without fluid. Inspect for coating, glazing, gasket degradation. Acceptable: no visible change.

### Sampling Protocol

- 100% of collectors: visual inspection, pressure test
- 5% of production or 1 per batch: full ISO 9806 efficiency curve test
- Prototype and design changes: full test suite including thermal shock, exposure, stagnation

## Variations and Alternatives

### Collector Type Selection Guide

| Application | Required temperature | Recommended collector | Reason |
|-------------|----------------------|-----------------------|--------|
| Domestic hot water (40-60°C) | Low | Flat-plate | Lowest cost, reliable, no tracking |
| Space heating (30-50°C) | Low | Flat-plate | Large area, low temperature lift |
| Swimming pool (25-35°C) | Very low | Unglazed (bare rubber/plastic) | Lowest cost, no glazing needed |
| Absorption cooling (70-95°C) | Medium | Evacuated tube | Higher efficiency at elevated temperature |
| Industrial process heat (80-150°C) | Medium | Evacuated tube or CPC | Good efficiency above flat-plate limit |
| Steam generation (150-250°C) | High | Parabolic trough | Concentrating needed for high ΔT |
| Power generation (300-550°C) | High | Parabolic trough or solar tower | See [steam turbines](./steam-turbines.md) |
| High-temperature process (600-1000°C) | Very high | Solar dish or tower | Only viable with high concentration |

### Material and Design Variations

- **Unglazed flat-plate**: Absorber plate without glass cover. Used for swimming pool heating where low temperature lift (ΔT <10°C) makes heat loss acceptable. Lowest cost ($30-80/m²).
- **Integrated Collector Storage (ICS)**: A tank inside the collector acts as both absorber and storage. No separate tank needed. Simpler system but limited to 50-100 L and overnight heat loss is high. Good for frost-free climates.
- **Compound Parabolic Concentrator (CPC)**: Involute/parabolic reflector shape that accepts sunlight over a range of angles and concentrates it onto a flat or tubular absorber. CR = 1.5-5. Can operate without tracking (accepts ±30° incidence angle).
- **Thermosiphon system**: Natural circulation driven by density difference (hot water rises) — no pump or controller needed. Tank must be above collector. Simple, reliable, common in developing countries.
- **Active pumped system**: Circulation pump controlled by differential thermostat (turns on when collector is 5-10°C hotter than tank). More flexible placement, higher efficiency, but requires electricity for pump and controller.

## References

- [Solar thermal energy](./solar-thermal.md) — parent capability covering all solar thermal technologies including power generation
- [Glass — basic](../glass/basic.md) — low-iron and borosilicate glass production for covers and evacuated tubes
- [Copper refining](../metals/copper-refining.md) — absorber plate and tube materials
- [Photovoltaics](./photovoltaics.md) — complementary solar technology for electricity generation
- [Steam turbines](./steam-turbines.md) — driven by high-temperature solar thermal collectors
- [Boiler](./boiler.md) — conventional heat source and steam generation for comparison
- [Iron and steel](../metals/iron-steel.md) — support structures and tracking mechanism
- [Polymers](../polymers/index.md) — insulation, gaskets, and glazing materials

---
*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
