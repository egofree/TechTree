# Steam Turbines

> **Node ID**: energy.steam-power.steam-turbines
> **Domain**: [Energy](./)
> **Dependencies**: `energy.steam-power`, `metals.iron-steel`, `machine-tools`
> **Timeline**: Years 20-35
> **Outputs**: turbine_power, electrical_generation, rotary_power

### Overview

Steam turbines replace reciprocating engines for power generation by converting the thermal energy of expanding steam directly into continuous rotary motion. No pistons, no crankshaft, no valve gear — just rows of blades spinning in a steam flow. They operate at far higher speeds and efficiencies than any reciprocating steam engine, and they are the reason large-scale electrical generation became practical. A single turbine-generator unit can deliver 50-500+ MW at 30-40% thermal efficiency, dwarfing the 5-15% efficiency and 1000-5000 HP ceiling of triple-expansion engines.

### Impulse Turbines (De Laval)

**Principle**: Steam expands entirely through stationary nozzles, converting pressure energy into kinetic energy (high-velocity jet). The jet impinges on bucket-shaped blades on the rotor. All pressure drop occurs at the nozzle — the rotor blades experience only the impulse (momentum transfer) of the jet. No pressure drop across the moving blades; the rotor casing operates at essentially atmospheric pressure.

**Construction**:
- **Nozzle**: Converging-diverging (de Laval) nozzle shape for supersonic steam velocities. Machined from bronze or steel. Steam exits at 500-1200 m/s depending on inlet conditions.
- **Rotor**: Single disc with bucket-shaped blades around the perimeter. Blades have a splitter ridge that divides the jet, redirecting each half ~165° for maximum momentum transfer.
- **Speed**: Single-stage impulse turbines run at 10,000-30,000 RPM. This is far too fast for direct generator coupling — requires reduction gearing (helical or epicyclic gears, 10:1 to 50:1 ratio).
- **Applications**: Small units (0.5-10 MW) for industrial power, marine propulsion (turbo-electric drives), and mechanical drives (compressors, pumps).

**Multi-stage impulse (Curtis / Rateau)**:
- Single-stage impulse wastes energy — the exhaust jet still carries significant velocity. Multi-stage designs arrange multiple rows of nozzles and blades in series.
- **Curtis staging**: Velocity-compound — one nozzle feeds a row of moving blades, then a row of fixed guide blades redirect the steam into a second row of moving blades on the same disc. Extracts more energy per disc but adds complexity.
- **Rateau staging**: Pressure-compound — multiple nozzles in series, each expanding the steam through a pressure drop, each feeding its own row of moving blades. Each row runs at lower steam velocity than a single-stage design.
- **Combined**: Large turbines use Curtis stages at the high-pressure end (compact, handle high energy density) and Rateau stages for intermediate and low-pressure sections.

### Reaction Turbines (Parsons)

**Principle**: Steam expands through both stationary guide blades (nozzles) AND rotating blades. The rotating blades act as moving nozzles — pressure drops continuously across both fixed and moving rows. The rotor is pushed both by impulse (velocity change) and reaction (pressure difference across the blade).

**Construction**:
- **Blading**: Alternating rows of fixed stator blades (mounted in the casing) and moving rotor blades (mounted on the rotor disc or drum). Each blade row has an airfoil profile optimized for the local steam conditions.
- **Rotor**: Drum-type (long cylinder with blades mounted along its length) or disc-type (individual discs shrunk onto a shaft). Drum-type handles thermal expansion better for large units.
- **Casing**: Heavy cast or fabricated steel shell containing the stator blades. Must withstand full steam pressure at the HP inlet.
- **Speed**: 1,500-3,600 RPM (direct drive to 50/60 Hz generators is practical). Lower speed than impulse because each stage extracts only a fraction of the energy — many stages in series.

**Multi-stage design**:
- A typical large turbine has 20-50 stages. Steam conditions progress from high-pressure, high-temperature, low-volume at the inlet to low-pressure, low-temperature, high-volume at the exhaust.
- **HP section**: Small blade heights (50-150 mm), high pressure (10-100+ bar), high temperature (400-540°C). Materials: 12% chromium steel or austenitic stainless.
- **IP section**: Medium blade heights (200-400 mm), moderate conditions. Materials: chromium-molybdenum steel.
- **LP section**: Very long blades (300-1200 mm, last-row blades are the longest precision blades ever manufactured), near-vacuum exhaust (0.05-0.1 bar absolute). Materials: precipitation-hardened stainless steel or titanium for last-row blades.
- **Double-flow LP**: The low-pressure section is often split into two flows (steam enters the center and exits both ends) to keep blade lengths manageable and reduce thrust bearing loads.

### Impulse-Reaction Combination

Modern utility turbines use impulse stages at the HP end and reaction stages in the LP end:
- **HP impulse stages**: High steam density means partial admission (only some nozzle arcs are open) is efficient — impulse handles this well. Impulse stages are shorter and more robust against erosion from water droplets in the steam.
- **LP reaction stages**: Steam volume is enormous — full admission across the entire annulus. Reaction blading provides better efficiency at large volume flows and lower pressures.
- **Transition**: The crossover from impulse to reaction is gradual — intermediate stages often have a mix of characteristics.

### Condenser Systems

**Surface condenser** (standard for power generation):
- Exhaust steam enters a shell-and-tube heat exchanger. Cooling water flows through thousands of tubes (20-30 mm diameter, brass or titanium). Steam condenses on the tube outer surfaces, dripping to a hotwell for recovery as feed water.
- **Vacuum**: Condenser operates at 0.03-0.1 bar absolute pressure (96-97% vacuum). This dramatically increases the pressure differential across the turbine — the LP stages extract energy down to this vacuum rather than exhausting to atmosphere. Improves efficiency by 8-12 percentage points.
- **Cooling water**: River water, sea water, or cooling tower circulation. Flow rate: ~50-100 m³ per MW of turbine output. Temperature rise across condenser: 8-12°C.
- **Air ejector**: Small steam jet or mechanical vacuum pump removes non-condensable gases (air leaked in through seals). Even small air accumulations degrade vacuum and reduce efficiency.

**Feed water recovery**: Condensed steam is pumped back to the boiler as feed water. This is critical — returning hot, deaerated feed water saves 10-15% on fuel compared to feeding cold raw water.

### Blade Materials

Blades operate under extreme conditions — centrifugal stress, steam erosion, corrosion, and thermal cycling:
- **HP blades (400-540°C)**: 12-25% chromium martensitic stainless steel. Good creep resistance at temperature. Precipitation-hardening grades (17-4PH) for highest-stress locations.
- **IP blades (200-400°C)**: Chromium-molybdenum steel (1-2.25% Cr, 0.5-1% Mo). Good strength and fatigue resistance.
- **LP last-row blades**: Precipitation-hardened stainless steel or titanium alloy (Ti-6Al-4V). Titanium preferred for the longest blades (>900 mm) due to its high strength-to-weight ratio — reduces centrifugal stress on the rotor. Titanium also resists water-droplet erosion better than steel.
- **Erosion protection**: LP blades suffer erosion from water droplets condensing in the expanding steam. Hard-facing (stellite, tungsten carbide) on leading edges extends blade life. Moisture-recovery stages (water extraction slots in the casing) reduce the problem upstream.

### Governor Mechanisms

- **Mechanical-hydraulic governor**: Centrifugal flyballs or flyweights sense turbine speed. Displacement of the flyweights controls a pilot valve, which modulates hydraulic oil pressure to the main steam valve servomotor. Proportional control with adjustable droop (typically 4-5% speed drop from no-load to full-load). Self-contained, reliable, no external power required for basic operation.
- **Electro-hydraulic governor**: Electronic speed sensor (magnetic pickup on a gear tooth) provides speed signal to an electronic controller, which drives hydraulic servo valves. More precise than mechanical, supports complex control modes (load sharing between multiple turbines, frequency regulation, isochronous operation).
- **Overspeed trip**: Independent mechanical bolt (emergency trip) mounted on the rotor shaft. At 110-115% of rated speed, centrifugal force flings the bolt outward, tripping a latch that dumps hydraulic oil from the steam valve actuators — valves slam shut under spring force. This is the last line of defense against runaway. Test the overspeed trip regularly by tripping it electrically.

### Power Output Ranges

| Size Class | Power Output | Steam Conditions | Application |
|-----------|-------------|-----------------|-------------|
| Small industrial | 0.5-10 MW | 10-40 bar, 300-400°C | Factory cogeneration, mechanical drives |
| Medium utility | 10-100 MW | 40-100 bar, 400-480°C | Regional power plants |
| Large utility | 100-500 MW | 100-165 bar, 480-540°C | Baseload generation |
| Ultra-supercritical | 500-1000+ MW | 250-350 bar, 580-620°C | Most efficient baseload |

### Thermal Efficiency

- **Simple non-condensing**: 15-20% (exhausts to atmosphere, no condenser). Simple but wasteful.
- **Condensing turbine**: 30-40% (with condenser vacuum). Standard for power generation.
- **Superheat**: Each 50°C of superheat above saturation improves efficiency by ~2 percentage points.
- **Reheat**: Extract steam after the HP section, route back through the boiler for additional superheating, then return to the IP section. Adds 4-5 percentage points of efficiency.
- **Regenerative feedwater heating**: Bleed steam from intermediate turbine stages to preheat boiler feed water through a series of shell-and-tube heaters. Recovers energy that would otherwise be lost to the condenser. Adds 5-8 percentage points of efficiency.
- **Combined cycle**: Turbine exhaust heat generates steam for a second (bottoming) turbine. Combined efficiencies reach 55-62%.

### Safety and Hazards

- **Overspeed failure**: If the turbine loses its load (generator disconnects) and the governor fails to close the steam valves, the rotor accelerates until centrifugal forces tear the blades from the disc. Blade fragments become lethal projectiles. Prevention: redundant governor systems, tested overspeed trip bolt, regular testing of all protection systems.
- **Steam leaks**: High-pressure steam (100+ bar, 500+°C) leaks from flanges, valve packing, or casing cracks are invisible and instantly fatal. Infrared thermography for leak detection. Regular inspection of all bolted joints. Never approach a pressurized steam turbine without verifying isolation and depressurization.
- **Lubricating oil fires**: Turbine bearings are lubricated with large volumes of oil (hundreds of liters). An oil leak onto hot steam piping ignites spontaneously. Oil-fire detection and suppression systems required. Fire-resistant hydraulic fluids available but expensive.
- **Condenser vacuum failure**: If cooling water flow is lost, vacuum collapses, exhaust pressure rises, and the last LP stages operate in choked, overheated flow. Automatic trip on low vacuum protects the turbine. Never override vacuum trip.

### Cross-References

- **Boilers providing steam**: [steam-power.md](steam-power.md)
- **Electricity generation from turbines**: [electricity.md](electricity.md)
- **Graphite for turbine seals/lubricants**: [electric-furnaces.md](electric-furnaces.md)
- **Metals for blades and casings**: [iron-steel.md](../metals/iron-steel.md)

---

*Part of the [Bootciv Tech Tree](../) • [Energy](./) • [All Domains](../)*
