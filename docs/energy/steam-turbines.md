# Steam Turbines

> **Node ID**: energy.steam-power.steam-turbines
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.steam-power`](steam-power.md), [`machine-tools.machining`](../machine-tools/machining.md), [`metals.alloys`](../metals/alloys.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-35
> **Outputs**: turbine_power, electrical_generation, rotary_power
> **Critical**: Yes — steam turbines are the dominant prime mover for large-scale electricity generation; no practical alternative exists for utility-scale power above 50 MW

Steam turbines replace reciprocating engines for power generation by converting the thermal energy of expanding steam directly into continuous rotary motion. No pistons, no crankshaft, no valve gear — just rows of blades spinning in a steam flow. They operate at far higher speeds and efficiencies than any reciprocating steam engine, and they are the reason large-scale electrical generation became practical. A single turbine-generator unit can deliver 50-500+ MW at 30-40% thermal efficiency, dwarfing the 5-15% efficiency and 1000-5000 HP ceiling of triple-expansion engines.

## Impulse Turbines (De Laval)

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

## Reaction Turbines (Parsons)

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

## Impulse-Reaction Combination

Modern utility turbines use impulse stages at the HP end and reaction stages in the LP end:
- **HP impulse stages**: High steam density means partial admission (only some nozzle arcs are open) is efficient — impulse handles this well. Impulse stages are shorter and more robust against erosion from water droplets in the steam.
- **LP reaction stages**: Steam volume is enormous — full admission across the entire annulus. Reaction blading provides better efficiency at large volume flows and lower pressures.
- **Transition**: The crossover from impulse to reaction is gradual — intermediate stages often have a mix of characteristics.

## Condenser Systems

**[Surface condenser](../glossary/surface-condenser.md)** (standard for power generation):

Exhaust steam enters a shell-and-tube heat exchanger positioned directly below the turbine exhaust. The shell is a cylindrical or box-shaped steel vessel rated for full vacuum (external pressure of ~1 bar). Inside, thousands of tubes (20-30 mm OD, 0.5-1.0 mm wall thickness, brass, cupro-nickel, or titanium) carry cooling water. Steam condenses on the tube outer surfaces, dripping to a hotwell for recovery as feed water.

- **Vacuum**: The condenser operates at 0.03-0.1 bar absolute pressure (96-97% vacuum). This low exhaust pressure is what makes condensing turbines so much more efficient than non-condensing types — the pressure ratio across the turbine increases from perhaps 10:1 (exhaust to atmosphere) to 100:1 or more (exhaust to vacuum). Each 1 kPa reduction in exhaust pressure improves turbine output by roughly 0.5-1% of rated power. Improves efficiency by 8-12 percentage points.
- **Cooling water**: River water, sea water, or cooling tower circulation. Flow rate: ~50-100 m³ per MW of turbine output. Temperature rise across condenser: 8-12°C. Cooling water inlet temperature must be 10-20°C below the steam saturation temperature at the desired condenser vacuum. For a condenser operating at 5 kPa absolute (saturation temperature 33°C), cooling water inlet should be at 15-20°C.
- **Air ejector system**: Non-condensable gases (air leaking through shaft seals, gases dissolved in feedwater) accumulate in the condenser and degrade vacuum. A two-stage steam jet air ejector is the standard removal method. The first stage pulls the air-steam mixture from the condenser, compresses it, and condenses the steam in an inter-aftercondenser. The second stage compresses the remaining non-condensables to atmospheric pressure for venting. Mechanical vacuum pumps (liquid ring type) are an alternative where motive steam is scarce.
- **Condensate return**: Condensed steam collects in the hotwell as pure, deaerated water at near-boiling temperature. Condensate extraction pumps (typically two in parallel, one standby) pump this water forward through the feedwater heating chain back to the boiler. Returning hot condensate saves 10-15% on boiler fuel compared to cold makeup water. Condensate purity is monitored continuously: a conductivity increase indicates a cooling water tube leak (cooling water contamination would cause boiler scale and corrosion).

## Blade Materials

Blades operate under extreme conditions — centrifugal stress, steam erosion, corrosion, and thermal cycling:
- **HP blades (400-565°C)**: 12-25% chromium martensitic stainless steel (AISI 422 or similar). The chromium provides oxidation resistance and hardenability. Creep resistance is the critical property: the blade must not slowly elongate under centrifugal stress at operating temperature. Precipitation-hardening grades (17-4PH) for highest-stress locations. For temperatures above 565°C, austenitic stainless steels or nickel-based alloys are required.
- **IP blades (200-400°C)**: Chromium-molybdenum steel (1-2.25% Cr, 0.5-1% Mo). Good strength, fatigue resistance, and oxidation resistance. The molybdenum contributes to creep strength.
- **LP last-row blades**: Precipitation-hardened stainless steel or titanium alloy (Ti-6Al-4V). Titanium preferred for the longest blades (>900 mm) because its density (4430 kg/m³) is roughly half that of steel (7850 kg/m³), halving the centrifugal load for the same blade geometry. Titanium also has excellent resistance to water-droplet erosion, which is severe in the wet-steam environment of the LP exhaust.
- **Erosion protection**: LP blades suffer erosion from water droplets condensing in the expanding steam. Hard-facing (stellite, tungsten carbide) on leading edges extends blade life. Moisture-recovery stages (water extraction slots in the casing) reduce the problem upstream.

## Blade Manufacturing Process

**From forging to finished blade**: Turbine blades are among the most precisely manufactured metal components in any industry. The process starts with a forged steel blank (or an investment-cast wax pattern for complex airfoil shapes). The blank is rough-machined to within 0.5 mm of final dimensions, then finish-machined on multi-axis CNC equipment or, in earlier practice, on tracer-controlled milling machines following a master template.

**Root attachment design**: The blade root (the base that locks into the rotor disc) carries the full centrifugal load of the blade. The fir-tree (or dovetail) design is standard: a series of interlocking serrated teeth on the blade root engage matching grooves in the disc rim. The load is distributed across multiple contact surfaces, each machined to ±0.01 mm tolerance. A typical fir-tree root has 3-6 pairs of contact faces. The blade slides axially into the disc groove and is locked in place by a small pin or peened tab.

**Blade profile grinding**: The airfoil section of each blade must match the designed aerodynamic profile within ±0.01 mm over its entire length. Deviations cause flow separation, reduced efficiency, and local stress concentrations. Profile grinding uses formed grinding wheels or continuous-path CNC grinding. Surface finish requirement: Ra 0.4-1.6 μm. After grinding, each blade is measured on a coordinate measuring machine (CMM) or optical comparator against the master profile.

**Surface finishing for erosion resistance**: LP blades in particular need protection from water-droplet erosion. Leading edges may be coated with stellite (cobalt-chromium-tungsten alloy) by welding or laser cladding. Alternatively, the blade surface is hardened by shot peening (bombarding with steel or glass shot to create a compressive residual stress layer that resists crack initiation). Titanium blades for the last LP row have natural erosion resistance superior to steel.

## Governing Systems

- **Mechanical-hydraulic governor**: Speed sensing begins with centrifugal flyweights mounted on a governor shaft driven from the main turbine rotor (typically via a worm gear at 1/10 to 1/20 of turbine speed). As turbine speed increases, the flyweights swing outward, lifting a sleeve connected to a pilot valve. The pilot valve modulates hydraulic oil pressure to the main steam admission valve servomotor. Proportional control with adjustable droop (typically 4-5% speed drop from no-load to full-load). Self-contained, reliable, no external power required for basic operation.
- **Electro-hydraulic governor**: Electronic speed sensor (magnetic pickup on a gear tooth) provides speed signal to an electronic controller, which drives hydraulic servo valves. More precise than mechanical, supports complex control modes (load sharing between multiple turbines, frequency regulation, isochronous operation). Electro-hydraulic governors achieve this with electronic PID (proportional-integral-derivative) controllers driving hydraulic servo valves. The integral term eliminates steady-state speed error; the derivative term dampens oscillations.
- **Speed regulation accuracy**: For electrical generation, the turbine must maintain speed within ±0.1% to produce AC power at the correct frequency (50.00 ± 0.05 Hz or 60.00 ± 0.06 Hz). This requires a governor with high gain and fast response.
- **Droop setting**: Governor droop is the percentage speed change from no-load to full-load. A 4% droop means the turbine runs 4% faster unloaded than at rated load. Droop is essential for load sharing between parallel turbines: each turbine picks up load in proportion to its droop setting. Lower droop gives faster response but risks hunting (oscillation). Isochronous (0% droop) mode is possible with electronic governors for single-turbine installations.
- **Overspeed trip**: Independent mechanical bolt (emergency trip) mounted on the rotor shaft. At 110-115% of rated speed, centrifugal force flings the bolt outward, tripping a latch that dumps hydraulic oil from the steam valve actuators — valves slam shut under spring force. This is the last line of defense against runaway. Test the overspeed trip regularly by tripping it electrically.

## Auxiliary Systems

**Lubrication system**: Turbine bearings require forced-feed lubrication at 1-3 bar oil pressure. A main shaft-driven oil pump circulates oil through coolers and filters to the bearings. An auxiliary AC or DC motor-driven pump provides oil pressure during startup and coast-down when the shaft pump is ineffective. Oil temperature maintained at 40-50°C. Bearing metal temperature monitored with thermocouples: alarm at 85°C, trip at 95°C.

**Steam seal system**: Where the rotor shaft exits the casing, labyrinth seals (interlocking fins on the rotor and grooves in the casing) minimize steam leakage. A small amount of sealing steam is supplied at slightly above atmospheric pressure to prevent air ingress into the vacuum section. Gland steam condenser recovers the sealing steam.

## Power Output Ranges

| Size Class | Power Output | Steam Conditions | Application |
|-----------|-------------|-----------------|-------------|
| Small industrial | 0.5-10 MW | 10-40 bar, 300-400°C | Factory cogeneration, mechanical drives |
| Medium utility | 10-100 MW | 40-100 bar, 400-480°C | Regional power plants |
| Large utility | 100-500 MW | 100-165 bar, 480-540°C | Baseload generation |
| Ultra-supercritical | 500-1000+ MW | 250-350 bar, 580-620°C | Most efficient baseload |

## Thermal Efficiency

- **Simple non-condensing**: 15-20% (exhausts to atmosphere, no condenser). Simple but wasteful.
- **Condensing turbine**: 30-40% (with condenser vacuum). Standard for power generation.
- **Superheat**: Each 50°C of superheat above saturation improves efficiency by ~2 percentage points.
- **Reheat**: Extract steam after the HP section, route back through the boiler for additional superheating, then return to the IP section. Adds 4-5 percentage points of efficiency.
- **Regenerative feedwater heating**: Bleed steam from intermediate turbine stages to preheat boiler feed water through a series of shell-and-tube heaters. Recovers energy that would otherwise be lost to the condenser. Adds 5-8 percentage points of efficiency.
- **Combined cycle**: Turbine exhaust heat generates steam for a second (bottoming) turbine. Combined efficiencies reach 55-62%.

## Safety and Hazards

- **Overspeed failure**: If the turbine loses its load (generator disconnects) and the governor fails to close the steam valves, the rotor accelerates until centrifugal forces tear the blades from the disc. Blade fragments become lethal projectiles. Prevention: redundant governor systems, tested overspeed trip bolt, regular testing of all protection systems.
- **Steam leaks**: High-pressure steam (100+ bar, 500+°C) leaks from flanges, valve packing, or casing cracks are invisible and instantly fatal. Infrared thermography for leak detection. Regular inspection of all bolted joints. Never approach a pressurized steam turbine without verifying isolation and depressurization.
- **Lubricating oil fires**: Turbine bearings are lubricated with large volumes of oil (hundreds of liters). An oil leak onto hot steam piping ignites spontaneously. Oil-fire detection and suppression systems required. Fire-resistant hydraulic fluids available but expensive.
- **Condenser vacuum failure**: If cooling water flow is lost, vacuum collapses, exhaust pressure rises, and the last LP stages operate in choked, overheated flow. Automatic trip on low vacuum protects the turbine. Never override vacuum trip.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Turbine vibration increasing | Blade loss or erosion, bearing wear, misalignment, thermal bow | Check vibration amplitude and frequency; inspect blades for erosion or cracking; check bearing clearances; verify alignment; if cold, roll rotor slowly to straighten thermal bow |
| Reduced power output at same steam flow | Blade fouling (silica deposits), nozzle erosion, condenser vacuum loss | Inspect blade surfaces through casing openings; clean condenser tubes; check cooling water flow; verify air ejector operation |
| High bearing temperature (>85°C alarm) | Oil flow restriction, oil cooler fouling, bearing damage, excessive load | Check oil pressure and flow; clean oil cooler; inspect bearing babbitt for damage; verify alignment and bearing preload |
| Condenser vacuum degrading | Air leak into condenser, fouled tubes, cooling water flow loss, air ejector failure | Leak test with helium sniffer or vacuum decay; clean condenser tubes; verify cooling water pump operation; inspect air ejector steam supply |
| Overspeed trip activates unexpectedly | Governor malfunction, electrical load rejection, trip bolt fatigue | Test governor response; check electrical breaker coordination; inspect trip bolt for wear; verify hydraulic oil pressure to steam valves |
| Blade cracking in LP stages | Water-droplet erosion fatigue, resonance vibration, corrosion pitting | Inspect last-stage blades for erosion depth (>0.5 mm requires replacement); verify moisture extraction slots are clear; check blade vibration frequency against running speed |
| Steam leak at casing joints | Bolt relaxation from thermal cycling, gasket degradation, casing distortion | Re-torque casing bolts to specification after thermal cycle; replace gaskets; check casing flange flatness with straightedge |
| Turbine fails to reach rated speed | Steam valve not fully open, excessive starting torque, governor set too low | Verify steam admission valve fully open; check driven equipment (generator, pump) for mechanical drag; verify governor speed setting |
| Oil contamination (water or particles) | Steam seal leak into bearing housing, cooler tube leak, filter bypass | Inspect gland steam seals; oil cooler pressure test; replace filter elements; check oil purifier operation |
| Differential expansion trip on startup | Rapid heating rate, insufficient soak time at intermediate temperatures | Follow manufacturer start-up curve: limit temperature ramp to 2-3°C/min; hold at 150°C and 300°C for thermal soaking; verify differential expansion indicators |

## Limitations

- **Water quality requirements**: Boiler feedwater must be highly purified (conductivity <0.2 µS/cm). Dissolved oxygen, silica, and dissolved solids cause corrosion and scale. Extensive water treatment plant required.
- **Start-up time**: Large steam turbines require 4-8 hours from cold start to full load due to thermal expansion constraints. Rapid start-up causes differential expansion and blade rubbing.
- **Blade erosion**: Moisture in low-pressure stages causes erosion of last-stage blades. Water droplets impact blade leading edges at high velocity. Requires stainless steel or Stellite-shielded blade tips.
- **Condenser fouling**: Cooling water fouling (biofilm, scaling, sediment) degrades vacuum and reduces efficiency by 2-5%. Regular tube cleaning required.
- **High capital cost**: Steam turbine plants require boiler, turbine, condenser, feedwater system, and cooling system — complex integrated plant with high upfront investment.
- **Minimum efficient size**: Steam turbines become cost-effective above ~5 MW. Below this, reciprocating steam engines or internal combustion engines are more economical.

## See Also

- [Steam Power](steam-power.md) — boilers providing steam for turbines
- [Electricity Generation](electricity.md) — generators and power distribution
- [Coal](coal.md) — primary fuel for steam turbine plants
- [Water Turbines](water-turbines.md) — hydraulic turbine comparison
- [Cooling Systems](cooling.md) — condenser cooling systems
- [Iron & Steel](../metals/iron-steel.md) — materials for blades and casings
- [Electric Furnaces](electric-furnaces.md) — graphite for turbine seals and lubricants
- [Geothermal Energy](geothermal.md) — geothermal flash steam driving turbines

[← Back to Energy](index.md)
