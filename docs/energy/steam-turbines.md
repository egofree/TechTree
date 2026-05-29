# Steam Turbines

> **Node ID**: energy.steam-power.steam-turbines
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.steam-power`](steam-power.md), [`machine-tools.machining`](../machine-tools/machining.md), [`metals.alloys`](../metals/alloys.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-35
> **Outputs**: turbine_power, electrical_generation, rotary_power
> **Critical**: Yes — steam turbines are the dominant prime mover for large-scale electricity generation; no practical alternative exists for utility-scale power above 50 MW

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

**Strengths**:
- Simple rotor design — no pressure differential across blades, reducing thrust bearing loads
- Nozzle-based design allows partial admission (only some nozzles active) for efficient operation at reduced load
- Multi-stage designs (Curtis, Rateau) extract far more energy per unit than single-stage impulse

**Weaknesses**:
- Single-stage requires 10,000-30,000 RPM — reduction gearing is mandatory for generator coupling
- Multi-stage designs require precision-machined blade profiles and nozzle clearances (tolerances ±0.1 mm)
- No casing pressure seal needed for pure impulse, but multi-stage designs lose this advantage

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

**Strengths**:
- Direct-drive to 50/60 Hz generators at 1,500-3,600 RPM — no reduction gearing needed
- Highest peak efficiency of any steam turbine type (80-94% stage efficiency)
- 20-50 stages extract nearly all available energy from the steam expansion

**Weaknesses**:
- Requires pressure-tight casing — casing must withstand full steam pressure at HP inlet (10-100+ bar)
- Thrust bearings must handle significant axial force from pressure differential across rotor discs
- LP last-row blades (300-1200 mm) are among the longest precision-machined components in manufacturing

### Impulse-Reaction Combination

Modern utility turbines use impulse stages at the HP end and reaction stages in the LP end:
- **HP impulse stages**: High steam density means partial admission (only some nozzle arcs are open) is efficient — impulse handles this well. Impulse stages are shorter and more robust against erosion from water droplets in the steam.
- **LP reaction stages**: Steam volume is enormous — full admission across the entire annulus. Reaction blading provides better efficiency at large volume flows and lower pressures.
- **Transition**: The crossover from impulse to reaction is gradual — intermediate stages often have a mix of characteristics.

### Condenser Systems

**[Surface condenser](../glossary/surface-condenser.md)** (standard for power generation):
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

### Blade Manufacturing Process

**From forging to finished blade**: Turbine blades are among the most precisely manufactured metal components in any industry. The process starts with a forged steel blank (or an investment-cast wax pattern for complex airfoil shapes). The blank is rough-machined to within 0.5 mm of final dimensions, then finish-machined on multi-axis CNC equipment or, in earlier practice, on tracer-controlled milling machines following a master template.

**Root attachment design**: The blade root (the base that locks into the rotor disc) carries the full centrifugal load of the blade. The fir-tree (or dovetail) design is standard: a series of interlocking serrated teeth on the blade root engage matching grooves in the disc rim. The load is distributed across multiple contact surfaces, each machined to ±0.01 mm tolerance. A typical fir-tree root has 3-6 pairs of contact faces. The blade slides axially into the disc groove and is locked in place by a small pin or peened tab.

**Blade profile grinding**: The airfoil section of each blade must match the designed aerodynamic profile within ±0.01 mm over its entire length. Deviations cause flow separation, reduced efficiency, and local stress concentrations. Profile grinding uses formed grinding wheels or continuous-path CNC grinding. Surface finish requirement: Ra 0.4-1.6 μm. After grinding, each blade is measured on a coordinate measuring machine (CMM) or optical comparator against the master profile.

**Surface finishing for erosion resistance**: LP blades in particular need protection from water-droplet erosion. Leading edges may be coated with stellite (cobalt-chromium-tungsten alloy) by welding or laser cladding. Alternatively, the blade surface is hardened by shot peening (bombarding with steel or glass shot to create a compressive residual stress layer that resists crack initiation). Titanium blades for the last LP row have natural erosion resistance superior to steel.

### Turbine Stage Design: Impulse vs. Reaction

**Impulse staging**: In a pure impulse stage, all the pressure drop occurs in the stationary nozzles. Steam exits the nozzle at high velocity (500-1200 m/s depending on stage conditions) and impinges on the moving blades. The moving blades experience no pressure drop, only a change in velocity direction. The Curtis (velocity-compounded) stage is used for the first stage in many turbines: one nozzle feeds two rows of moving blades separated by a row of fixed guide blades. This arrangement extracts more energy from a single pressure drop than a single-row impulse stage, allowing a compact first stage that handles the highest energy density steam.

**Reaction staging (Parsons type)**: In a 50% reaction stage (the most common Parsons design), half the pressure drop occurs in the fixed blades (stator) and half in the moving blades (rotor). The rotor blades are shaped as nozzles themselves, accelerating the steam and creating a reaction force (like a rocket nozzle). This means the rotor experiences a net pressure force in addition to the impulse from velocity change. Reaction blading produces a net axial thrust on the rotor that must be balanced by a thrust bearing or dummy piston. Reaction stages achieve higher peak efficiency than impulse stages but are more sensitive to off-design conditions.

**Stage count progression**: A large condensing turbine may have 20-40 stages. The HP end has many short stages with small blade heights (the steam is dense and the volume flow is low). Each successive stage has longer blades and larger flow area as the steam expands. The LP end may have only 2-4 stages but with enormous blade heights (600-1200 mm for the last row). The transition from HP to IP to LP sections is a continuous expansion process, not discrete jumps.

### Condenser System Design

**Surface condenser construction**: The condenser is a large shell-and-tube heat exchanger positioned directly below the turbine exhaust. The shell is a cylindrical or box-shaped steel vessel rated for full vacuum (external pressure of ~1 bar). Inside, thousands of tubes (20-30 mm OD, 0.5-1.0 mm wall thickness, brass, cupro-nickel, or titanium) carry cooling water. Steam condenses on the outside of the tubes, and the condensate drips to the hotwell at the bottom.

**Cooling water temperature**: Cooling water inlet temperature must be 10-20°C below the steam saturation temperature at the desired condenser vacuum. For a condenser operating at 5 kPa absolute (saturation temperature 33°C), cooling water inlet should be at 15-20°C. The cooling water temperature rise across the condenser is typically 8-12°C. Higher temperature rise means less water flow needed but poorer vacuum.

**Vacuum operation**: The condenser maintains 5-10 kPa absolute pressure (90-95% vacuum). This low exhaust pressure is what makes condensing turbines so much more efficient than non-condensing types. The pressure ratio across the turbine increases from perhaps 10:1 (exhaust to atmosphere) to 100:1 or more (exhaust to vacuum). Each 1 kPa reduction in exhaust pressure improves turbine output by roughly 0.5-1% of rated power.

**Condensate return**: The condensed steam collects in the hotwell as pure, deaerated water at near-boiling temperature. Condensate extraction pumps (typically two in parallel, one standby) pump this water forward through the feedwater heating chain back to the boiler. Returning hot condensate saves 10-15% on boiler fuel compared to cold makeup water. Condensate purity is monitored continuously: a conductivity increase indicates a cooling water tube leak (cooling water contamination would cause boiler scale and corrosion).

**Air ejector system**: Non-condensable gases (air leaking through shaft seals, gases dissolved in feedwater) accumulate in the condenser and degrade vacuum. A two-stage steam jet air ejector is the standard removal method. The first stage pulls the air-steam mixture from the condenser, compresses it, and condenses the steam in an inter-aftercondenser. The second stage compresses the remaining non-condensables to atmospheric pressure for venting. Mechanical vacuum pumps (liquid ring type) are an alternative where motive steam is scarce.

### Governing Systems

**Centrifugal governor to valve actuation chain**: Speed sensing begins with centrifugal flyweights mounted on a governor shaft driven from the main turbine rotor (typically via a worm gear at 1/10 to 1/20 of turbine speed). As turbine speed increases, the flyweights swing outward, lifting a sleeve connected to a pilot valve. The pilot valve modulates hydraulic oil pressure to the main steam admission valve servomotor. This is a proportional control system: speed error produces a proportional valve correction.

**Speed regulation accuracy**: For electrical generation, the turbine must maintain speed within ±0.1% to produce AC power at the correct frequency (50.00 ± 0.05 Hz or 60.00 ± 0.06 Hz). This requires a governor with high gain and fast response. Electro-hydraulic governors achieve this with electronic PID (proportional-integral-derivative) controllers driving hydraulic servo valves. The integral term eliminates steady-state speed error; the derivative term dampens oscillations.

**Droop setting**: Governor droop is the percentage speed change from no-load to full-load. A 4% droop means the turbine runs 4% faster unloaded than at rated load. Droop is essential for load sharing between parallel turbines: each turbine picks up load in proportion to its droop setting. Lower droop gives faster response but risks hunting (oscillation). Isochronous (0% droop) mode is possible with electronic governors for single-turbine installations.

### Turbine Materials by Section

**HP blades (inlet temperatures 400-565°C)**: 12% chromium martensitic stainless steel (AISI 422 or similar). The chromium provides oxidation resistance and hardenability. These blades face the highest temperatures and pressures in the turbine. Creep resistance is the critical property: the blade must not slowly elongate under centrifugal stress at operating temperature. For temperatures above 565°C, austenitic stainless steels or nickel-based alloys are required.

**IP blades (200-400°C)**: Chromium-molybdenum steels (1-2.25% Cr, 0.5-1% Mo) provide adequate strength and oxidation resistance at intermediate temperatures. The molybdenum contributes to creep strength. These blades are generally less stressed than HP blades because the steam density is lower, but they are longer and thus experience higher centrifugal loading.

**LP blades (near-ambient temperature but highest stress)**: The last few rows of LP blades are the longest in the turbine (up to 1200 mm in large units) and spin at full rated speed. Centrifugal stress at the blade root scales with the product of blade mass and the square of rotational speed. Titanium alloy (Ti-6Al-4V) is preferred for blades longer than 900 mm because its density (4430 kg/m³) is roughly half that of steel (7850 kg/m³), halving the centrifugal load for the same blade geometry. Titanium also has excellent resistance to water-droplet erosion, which is severe in the wet-steam environment of the LP exhaust.

### Blade Manufacturing Process

**From forging to finished blade**: Turbine blades are among the most precisely manufactured metal components. The process starts with a forged steel blank (or investment-cast wax pattern for complex shapes). The blank is rough-machined to within 0.5 mm of final dimensions, then finish-machined on multi-axis CNC equipment or tracer-controlled milling machines following a master template.

**Root attachment (fir-tree design)**: The blade root locks into the rotor disc and carries the full centrifugal load. The fir-tree (dovetail) design uses interlocking serrated teeth, typically 3-6 pairs of contact faces, each machined to ±0.01 mm tolerance. The blade slides axially into the disc groove and is locked by a small pin or peened tab.

**Blade profile grinding**: The airfoil section must match the designed profile within ±0.01 mm over its entire length. Deviations cause flow separation, reduced efficiency, and stress concentrations. Surface finish: Ra 0.4-1.6 μm. Each blade is measured against the master profile on a coordinate measuring machine.

**Erosion protection**: LP blade leading edges are coated with stellite (cobalt-chromium-tungsten alloy) by welding or laser cladding. Alternatively, surfaces are shot-peened to create compressive residual stress that resists crack initiation.

### Turbine Stage Design: Impulse vs. Reaction

**Impulse staging**: All pressure drop occurs in stationary nozzles. The Curtis (velocity-compounded) stage uses one nozzle feeding two rows of moving blades separated by fixed guide blades, extracting more energy per disc. Used at the HP end where steam density and energy density are highest.

**Reaction staging (Parsons, 50% reaction)**: Half the pressure drop in fixed blades (stator), half in moving blades (rotor). The rotor blades act as nozzles, creating a reaction force. This produces net axial thrust requiring a thrust bearing. Reaction stages achieve higher peak efficiency but are more sensitive to off-design conditions.

**Stage count**: A large condensing turbine has 20-40 stages. The HP end has many short stages (dense steam, low volume flow). Each successive stage has longer blades as the steam expands. The LP end has 2-4 stages with blade heights of 600-1200 mm.

### Condenser System Design

**Surface condenser**: Large shell-and-tube heat exchanger below the turbine exhaust. Thousands of tubes (20-30 mm OD, brass or titanium) carry cooling water. Steam condenses on tube outer surfaces. Cooling water inlet must be 10-20°C below steam saturation temperature at the desired vacuum.

**Vacuum operation**: Condenser maintains 5-10 kPa absolute pressure (90-95% vacuum). Each 1 kPa reduction in exhaust pressure improves turbine output by roughly 0.5-1% of rated power. The low exhaust pressure increases the pressure ratio across the turbine from roughly 10:1 (atmospheric exhaust) to 100:1 or more.

**Condensate return**: Hot, deaerated water from the hotwell is pumped back to the boiler. Returning hot condensate saves 10-15% on boiler fuel compared to cold makeup water. Conductivity monitoring detects cooling water tube leaks.

**Air ejector system**: Non-condensable gases degrade vacuum. A two-stage steam jet air ejector pulls the air-steam mixture, condenses the steam, and vents non-condensables to atmosphere. Mechanical vacuum pumps (liquid ring type) are an alternative.

### Governing Systems

**Centrifugal governor to hydraulic servo**: Flyweights sense speed, modulating a pilot valve that controls hydraulic oil pressure to the main steam admission valve servomotor. For electrical generation, speed must stay within ±0.1% for correct frequency (50.00 ± 0.05 Hz). Electro-hydraulic governors with electronic PID controllers achieve this precision.

**Droop setting**: Governor droop is the percentage speed change from no-load to full-load. A 4% droop means the turbine runs 4% faster unloaded. Droop is essential for load sharing between parallel turbines. Lower droop gives faster response but risks hunting (oscillation).

**Overspeed trip**: An independent mechanical bolt mounted on the rotor shaft. At 110-115% of rated speed, centrifugal force flings the bolt outward, tripping a latch that dumps hydraulic oil from the steam valve actuators. Valves slam shut under spring force. This is the last line of defense against runaway. Test the overspeed trip regularly.

**Condenser vacuum failure protection**: If cooling water flow is lost, vacuum collapses, exhaust pressure rises, and LP stages operate in choked, overheated flow. Automatic trip on low vacuum protects the turbine. Never override vacuum trip.

**Lubrication system**: Turbine bearings require forced-feed lubrication at 1-3 bar oil pressure. A main shaft-driven oil pump circulates oil through coolers and filters to the bearings. An auxiliary AC or DC motor-driven pump provides oil pressure during startup and coast-down when the shaft pump is ineffective. Oil temperature maintained at 40-50°C. Bearing metal temperature monitored with thermocouples: alarm at 85°C, trip at 95°C.

**Steam seal system**: Where the rotor shaft exits the casing, labyrinth seals (interlocking fins on the rotor and grooves in the casing) minimize steam leakage. A small amount of sealing steam is supplied at slightly above atmospheric pressure to prevent air ingress into the vacuum section. Gland steam condenser recovers the sealing steam.

**Thermal efficiency summary**: Non-condensing turbine (exhaust to atmosphere): 15-20%. Condensing turbine with vacuum: 30-40%.

### Limitations

- **Water quality requirements**: Boiler feedwater must be highly purified (conductivity <0.2 µS/cm). Dissolved oxygen, silica, and dissolved solids cause corrosion and scale. Extensive water treatment plant required.
- **Start-up time**: Large steam turbines require 4-8 hours from cold start to full load due to thermal expansion constraints. Rapid start-up causes differential expansion and blade rubbing.
- **Blade erosion**: Moisture in low-pressure stages causes erosion of last-stage blades. Water droplets impact blade leading edges at high velocity. Requires stainless steel or Stellite-shielded blade tips.
- **Condenser fouling**: Cooling water fouling (biofilm, scaling, sediment) degrades vacuum and reduces efficiency by 2-5%. Regular tube cleaning required.
- **High capital cost**: Steam turbine plants require boiler, turbine, condenser, feedwater system, and cooling system — complex integrated plant with high upfront investment.
- **Minimum efficient size**: Steam turbines become cost-effective above ~5 MW. Below this, reciprocating steam engines or internal combustion engines are more economical.

### See Also

- [Steam Power](steam-power.md) — Boiler design and steam generation
- [Coal](coal.md) — Primary fuel for steam turbine plants
- [Water Turbines](water-turbines.md) — Hydraulic turbine comparison
- [Electricity Generation](electricity.md) — Generators and power distribution
- [Cooling Systems](cooling.md) — Condenser cooling systems
- [Iron & Steel](../metals/iron-steel.md) — Materials for turbine construction

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
