# Centrifugal Pump

> **Node ID**: water.centrifugal-pump
> **Domain**: [Water](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`water.distribution`](distribution.md), [`water.desalination`](desalination.md), [`water.sewage`](sewage.md)
> **Timeline**: Years 15-25
> **Outputs**: pressurized_water
> **Critical**: Yes — centrifugal pumps are the primary mover for water distribution, treatment, and industrial recirculation beyond gravity-fed systems

## Overview

A centrifugal pump converts rotational kinetic energy from a motor-driven impeller into hydrodynamic pressure, moving water through pipes at controlled flow rates and pressures. Approximately 70% of all pumps in industrial service are centrifugal. They serve [distribution networks](distribution.md), feed [desalination systems](desalination.md) at high pressure, lift [sewage](sewage.md) to treatment plants, and circulate cooling water in engines and industrial processes.

Once [electricity](../energy/electricity.md) and [machining](../machine-tools/machining.md) are available, centrifugal pumps become the default choice for moving water at scale. A settlement of 1,000 people at 100 L/person/day with 30 m distribution head needs approximately 4 m³/hour continuous delivery — a single 1.5 kW centrifugal pump handles this.

Centrifugal pumps are simpler than [positive-displacement pumps](positive-displacement-pump.md) in construction (fewer wearing parts) but cannot self-prime, cannot handle viscous fluids, and cannot produce constant flow against varying pressure. They excel in high-flow, moderate-head applications with clean or slightly contaminated water.

**Principle of operation**: Fluid enters the impeller eye (center) axially and is accelerated radially outward by rotating vanes. The volute casing (spiral-shaped housing) collects the high-velocity discharge and converts velocity head to pressure head via the Bernoulli principle. The affinity laws govern performance with changes in speed or impeller diameter:

- Flow ∝ speed: Q₂/Q₁ = N₂/N₁
- Head ∝ speed²: H₂/H₁ = (N₂/N₁)²
- Power ∝ speed³: P₂/P₁ = (N₂/N₁)³

Specific speed (Ns) classifies impeller design: Ns = N × √Q / H^(3/4), where N is RPM, Q is flow in m³/s at best efficiency point (BEP), and H is head per stage in meters. Low specific speed (Ns < 30): radial-flow impellers for high head, low flow. Medium (Ns 30-80): mixed-flow for moderate head and flow. High (Ns > 80): axial-flow (propeller) for very high flow, low head.

**Pump curves and system curves**: The pump curve (head vs. flow at constant speed and impeller diameter) defines the pump's hydraulic characteristic. The system curve (static head + friction losses vs. flow) defines the piping resistance. The operating point is where the two curves intersect. Shutoff head is the maximum pressure the pump develops at zero flow. Runout is the maximum flow at zero head. A centrifugal pump cannot develop pressure beyond shutoff head or deliver flow beyond runout.

**Net Positive Suction Head (NPSH)**: NPSH determines whether a pump can draw water without cavitation. NPSHa (available) = atmospheric pressure ± static suction head - friction losses - vapor pressure. NPSHr (required) is the pump manufacturer's stated minimum suction head at the impeller eye — typically 2-8 m depending on pump size and speed. Cavitation occurs when NPSHa < NPSHr. The pump sounds like gravel is passing through it, and sustained cavitation destroys the impeller within days. A centrifugal pump at sea level can lift water on its suction side by a maximum of approximately 7 m (theoretical atmospheric limit ~10.3 m, reduced by vapor pressure and friction losses). For deeper lifts, use a submersible pump or a [positive-displacement pump](positive-displacement-pump.md).

**Priming**: Centrifugal pumps cannot self-prime — they cannot evacuate air from the suction line. If the pump casing contains air instead of water, the impeller spins the air without generating significant pressure differential (air is 800× less dense than water). Operating a dry pump destroys the mechanical seal within minutes. Install the pump with a flooded suction (water source above the pump) whenever possible. For suction-lift installations, install a foot valve (check valve at the bottom of the suction pipe) and fill the casing and suction line with water before starting. For reliable priming in suction-lift applications, use a self-priming centrifugal pump (designed with a priming chamber that retains enough water to evacuate air on startup) or install an external priming system (venturi eductor or vacuum pump).

## Prerequisites

- [Iron and steel](../metals/iron-steel.md) for casting the volute casing and machining the shaft
- [Machine tools](../machine-tools/machining.md) — lathe for boring, turning, and facing operations
- [Electricity](../energy/electricity.md) — 200-480 V three-phase for pump motors
- [Bearings](../machine-tools/bearings-abrasives.md) — deep-groove ball bearings rated for pump speed and radial load
- [Polymers](../polymers/index.md) — seal and gasket materials (PTFE, rubber)

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Cast iron (casing) | 20-80 kg | Class 30 gray iron or ductile iron, for volute housing | [Iron & Steel](../metals/iron-steel.md) | Bronze (corrosive water), stainless steel (food/pharma) |
| Bronze or cast iron (impeller) | 5-15 kg | 85-5-5-5 bronze (water service) or cast iron (non-corrosive) | [Metals](../metals/index.md) | Stainless steel (304/316) for corrosive service |
| Steel shaft | 2-5 kg | 1045 or 416 stainless, 25-40 mm diameter, ground to 0.8 μm Ra | [Iron & Steel](../metals/iron-steel.md) | 316 stainless (corrosive service) |
| Mechanical seal or packing | 1 set | Carbon-ceramic mechanical seal or PTFE/graphite packing | [Polymers](../polymers/index.md) | Gland packing (leaks slightly, acceptable for non-critical service) |
| Bearings | 2-4 | Deep-groove ball bearings (6205-6209 series) rated for pump speed + radial load | [Bearings](../machine-tools/bearings-abrasives.md) | Sleeve bearings (oil-lubricated, for vertical pumps) |
| Electric motor | 1 | 0.75-15 kW, 1450 or 2900 RPM (4-pole or 2-pole at 50 Hz) | [Electricity](../energy/electricity.md) | Diesel engine, steam turbine, or belt-driven from line shaft |
| Bolts and gaskets | 1 set | Foundation bolts (M12-M16), flange gaskets (rubber or fiber) | [Iron & Steel](../metals/iron-steel.md) | — |

## Process Description

### End-Suction Centrifugal Pump (Single-Stage)

This is the most common centrifugal pump configuration. The suction inlet is on one end (axial), the discharge is tangential from the volute, and the impeller mounts on a shaft supported by bearings in the pump casing. Construction proceeds in three phases: impeller, volute casing, and assembly.

**Principle**: A single impeller accelerates fluid radially outward from the eye. The volute casing converts the velocity energy to pressure. Head is limited to the capability of one impeller stage (typically 10-80 m per stage at 1450 RPM, or 20-150 m at 2900 RPM).

**Prerequisites**: [Iron and steel](../metals/iron-steel.md), [machine tools](../machine-tools/machining.md), [electric motor](../energy/electricity.md), [bearings](../machine-tools/bearings-abrasives.md), [seal materials](../polymers/index.md).

**Materials**: Cast iron casing (20-80 kg), bronze impeller (5-15 kg), steel shaft (2-5 kg), mechanical seal, 2-4 bearings, electric motor (0.75-15 kW).

#### Impeller Construction

1. **Cast the impeller**: Use a split sand mold with a pattern matching the impeller geometry. Typical closed-impeller design: 5-7 backward-curved vanes, 150-250 mm outer diameter for a medium-capacity pump, vane thickness 4-8 mm at the periphery. Pour molten bronze (for water service) or cast iron at the appropriate pouring temperature (bronze: 1050-1150°C; cast iron: 1350-1450°C).
2. **Machine the impeller bore**: Chuck the impeller in a lathe on a mandrel that registers off the vane tips. Bore the center hole to fit the shaft diameter (25-40 mm typical) with an H7 tolerance (+0.000/-0.025 mm). Cut a keyway 6-10 mm wide × 3-6 mm deep for shaft locking.
3. **Balance the impeller**: Mount the impeller on a balance mandrel supported by knife-edge ways. Heavy spots roll to the bottom. Remove material by grinding or drilling from the heavy side. Target balance grade G6.3 (maximum residual unbalance in g·mm = 6.3 × rotor mass in kg × radius in mm / 1000). Unbalanced impellers cause vibration, bearing wear, and seal failure.
4. **Trim the impeller diameter**: If the pump produces too much head at the design speed, reduce impeller diameter by turning on a lathe. Head reduction follows: H_new = H_original × (D_new / D_original)². Do not reduce by more than 20% or vane geometry is compromised.

#### Volute Casing Construction

5. **Cast the volute casing**: Use a sand mold with a core forming the internal spiral passage. The volute cross-section increases from the tongue (cutwater) to the discharge flange, collecting flow from the impeller periphery. Minimum wall thickness: 6-8 mm for cast iron at pressures up to 10 bar. Cast the suction and discharge flanges integral with the casing (bolt holes drilled after casting).
6. **Machine mating surfaces**: Face the suction flange (inlet) and discharge flange (outlet) flat for gasket sealing. Bore the stuffing box (seal housing) to 0.05 mm clearance over the shaft diameter. Drill and tap bearing housing bores concentric with the volute center to within 0.05 mm.

#### Assembly

7. **Install shaft and bearings**: Press bearings onto the shaft using an arbor press (never hammer bearings — brinelling damage). Install the shaft/bearing assembly into the bearing housing. Shaft runout (total indicated reading at the impeller end) must not exceed 0.05 mm.
8. **Install the mechanical seal**: Mount the stationary seal face in the stuffing box bore. Mount the rotating seal face on the shaft. The two faces are lapped flat to within 0.5 μm (helium light-band contact). Seal faces are spring-loaded to maintain contact. Apply a thin film of clean oil to the seal faces before assembly — never run a dry mechanical seal.
9. **Mount impeller on shaft**: Slide the impeller onto the shaft keyway. Secure with a locknut or lockwasher. Verify impeller-to-volute clearance: the gap between impeller outer edge and volute tongue should be 0.5-1.0 mm. Too tight → rubbing and wear. Too loose → internal recirculation and reduced efficiency.
10. **Close the casing**: Bolt the casing halves together (split-case design) or install the cover plate (end-suction design). Torque casing bolts in a cross-pattern to the specified value (typically 40-80 N·m for M12-M16 bolts). Install flange gaskets on suction and discharge ports.
11. **Couple to motor**: Align the pump shaft to the motor shaft within 0.05 mm angular misalignment and 0.1 mm parallel offset, measured with a dial indicator at the coupling faces. Misalignment causes vibration, coupling wear, and bearing failure. Secure the coupling with a flexible spider or grid element to absorb residual misalignment.
12. **Mount on baseplate**: Bolt the pump and motor to a common baseplate (steel channel or cast iron). Grout the baseplate to the concrete foundation with non-shrink grout. Check alignment after grouting — grout shrinkage can shift the baseplate.

#### Calibration and Verification

13. **Rotation check**: Jog the motor (briefly energize) and confirm impeller rotation matches the arrow on the casing. Reverse rotation pumps water backward and produces zero net head. Swap any two motor leads to reverse a three-phase motor.
14. **Prime the pump**: Fill the suction piping and pump casing completely with water before starting. A centrifugal pump cannot prime itself — it merely spins air with no fluid transfer. Air-bound pumps overheat and destroy the seal. If the installation has a flooded suction (source above the pump), priming happens automatically by opening the suction valve. For suction-lift installations, use a foot valve and fill the casing through the priming plug.
15. **Measure shutoff head**: Close the discharge valve completely. Start the pump. Read the discharge pressure gauge. Shutoff head (m) = gauge pressure (bar) × 10.2. Compare to the manufacturer's pump curve at the installed impeller diameter. Deviation >10% indicates impeller damage, wrong rotation, or air in the system.
16. **Measure flow at operating point**: Open the discharge valve to the normal operating position. Measure flow rate with a flow meter or timed fill. Verify the operating point (flow, head) lies on the pump curve. If flow is significantly below design, check for suction-side air leaks, clogged strainers, or undersized piping.

#### Expected Performance

| Parameter | Small (50 mm) | Medium (150 mm) | Large (300 mm) |
|-----------|--------------|-----------------|----------------|
| Flow range | 5-50 m³/hour | 10-100 m³/hour | 50-500 m³/hour |
| Head range | 5-50 m | 10-80 m | 10-200 m |
| Efficiency at BEP | 50-65% | 55-75% | 70-85% |
| Speed (50 Hz) | 2900 RPM | 1450 RPM | 1450 RPM |
| Speed (60 Hz) | 3500 RPM | 1750 RPM | 1750 RPM |
| Motor power | 0.75-5.5 kW | 2.2-15 kW | 15-110 kW |
| Suction lift (max) | 5-7 m | 5-7 m | 5-7 m |
| NPSHr at BEP | 2-4 m | 2-6 m | 3-8 m |
| Seal life | 1-3 years | 1-3 years | 2-5 years |
| Bearing life (L10) | 20,000-40,000 hours | 30,000-50,000 hours | 40,000-60,000 hours |
| Service life (casing) | 10-20 years | 15-30 years | 20-40 years |

## Quantitative Parameters

### Pump Performance by Size

| Parameter | End-Suction 50 mm | End-Suction 150 mm | Multistage 100 mm | Submersible 100 mm |
|-----------|-------------------|--------------------|--------------------|---------------------|
| Flow at BEP | 15 m³/hour | 60 m³/hour | 30 m³/hour | 30 m³/hour |
| Head at BEP | 25 m | 40 m | 150 m (5-stage) | 80 m |
| Motor power | 2.2 kW | 11 kW | 22 kW | 15 kW |
| Efficiency at BEP | 58% | 72% | 68% | 65% |
| NPSHr at BEP | 2.5 m | 4.0 m | 3.5 m | N/A (submerged) |
| Suction lift capability | 5-7 m | 5-7 m | 5-7 m | N/A (submerged) |
| Impeller diameter | 150-180 mm | 250-300 mm | 180-220 mm/stage | 150-200 mm/stage |

### NPSH Calculation Reference

| Condition | NPSHa (m) | Notes |
|-----------|----------|-------|
| Flooded suction, source 2 m above pump | 12.3 | Atmospheric (10.3 m) + static (2 m) - minor losses |
| Flooded suction, source at pump level | 10.1 | Atmospheric (10.3 m) - vapor pressure (0.2 m) - friction |
| Suction lift 3 m, 50 mm pipe, 10 m length | 6.5 | Atmospheric (10.3 m) - static lift (3 m) - friction (0.6 m) - vapor pressure (0.2 m) |
| Suction lift 5 m, 50 mm pipe, 20 m length | 3.8 | Atmospheric - static lift - friction (1.3 m) - vapor pressure |
| Suction lift 7 m (practical limit) | 1.5 | Marginal — requires oversized suction pipe and minimal fittings |

NPSHa must always exceed NPSHr by at least 0.5-1.0 m margin. If NPSHa is marginal, increase suction pipe diameter, reduce suction pipe length, or lower the pump relative to the water source.

### Friction Loss Reference (Steel Pipe, Water at 20°C)

| Flow (m³/hour) | 50 mm pipe | 80 mm pipe | 100 mm pipe | 150 mm pipe |
|----------------|-----------|-----------|------------|------------|
| 5 | 7.2 m/100m | 1.4 m/100m | 0.5 m/100m | 0.1 m/100m |
| 10 | 26 m/100m | 5.0 m/100m | 1.7 m/100m | 0.4 m/100m |
| 20 | — | 18 m/100m | 6.2 m/100m | 1.3 m/100m |
| 50 | — | — | 34 m/100m | 7.2 m/100m |
| 100 | — | — | — | 26 m/100m |

Velocities above 2.5 m/s cause excessive erosion and water hammer risk. Velocities below 0.6 m/s allow sediment deposition. Size suction pipes one size larger than discharge pipes to minimize NPSH impact.

## Scaling Notes

- **Household supply** (5-20 m³/day): A single small end-suction pump (0.75-1.5 kW) at 1450 RPM delivers 5-15 m³/hour at 20-40 m head. Adequate for a household or small workshop. Surface-mounted with suction lift up to 5 m.
- **Village distribution** (50-500 m³/day): One or two medium pumps (2.2-7.5 kW) operating in parallel or duty/standby. Install in a pump house with a header manifold and [valves](water-valves.md) for isolation. Include a pressure tank (200-1000 L) to reduce pump cycling.
- **Municipal supply** (1,000-50,000 m³/day): Horizontal split-case pumps or vertical turbine pumps (15-110 kW each) in a pump station with multiple units. Raw water pumping from rivers or reservoirs may require 20-60 m total dynamic head. Distribute across 3-4 pumps for redundancy and staged capacity.
- **Industrial recirculation** (cooling water, process water): Vertical turbine or horizontal pumps sized for continuous duty (24/7 operation). Motor sizing: add 10-15% margin above the calculated brake horsepower at the rated operating point. A pump running at its BEP draws the least power per unit of water delivered.
- **Flow scaling by impeller diameter**: For a fixed speed, flow scales linearly with impeller diameter (Q ∝ D), head scales with diameter squared (H ∝ D²), and power scales with diameter cubed (P ∝ D³). Trimming the impeller is the primary method for tuning pump output to the system without changing the motor or speed.
- **Multistage scaling**: For heads above 80-100 m from a single impeller, stack multiple impellers on a common shaft in a multistage casing. Each stage adds its head contribution: total head = stages × head per stage. A 5-stage pump at 1450 RPM with 30 m head per stage delivers 150 m total head. Multistage pumps are standard for [desalination](desalination.md) (RO feed at 55-70 bar) and deep-well applications.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Pump runs but no flow | Not primed; air leak on suction side; impeller loose on shaft; wrong rotation | Fill casing and suction pipe with water. Check suction fittings for air leaks with soap solution. Verify impeller key is installed. Check rotation direction. |
| Low flow and low head | Worn impeller (vane tips eroded); impeller diameter too small for system; air entrainment | Inspect impeller vanes. Measure impeller diameter against spec. Check suction for vortexing or air leaks. |
| Pump draws high current | Impeller rubbing on volute; bearing failure; pump operating far right of BEP (high flow, low head) | Check impeller clearance. Listen for bearing noise (rough, grinding). Throttle discharge valve to move operating point toward BEP. |
| Cavitation noise (gravelly rattle) | Insufficient NPSHa — suction lift too high, suction pipe too small, or fluid too hot | Reduce suction lift. Increase suction pipe diameter. Lower fluid temperature. Install a booster pump on the suction side. |
| Seal leaking | Mechanical seal faces worn, contaminated, or run dry | Replace mechanical seal. Ensure pump is never run dry — seal faces require fluid for lubrication and cooling. |
| Excessive vibration | Impeller unbalance; shaft misalignment; worn bearings; resonance with structure | Rebalance impeller. Realign pump-to-motor coupling. Replace bearings. Stiffen or dampen the baseplate. |
| Motor overheats | Pump operating at runout (far right of curve, high flow, low head, high power); low supply voltage; blocked ventilation | Throttle discharge valve to move operating point left toward BEP. Check motor voltage (should be within ±5% of nameplate). Clean motor cooling fan and air passages. |
| Pump short-cycles (starts and stops frequently) | Pressure tank waterlogged (bladder ruptured or air charge lost); pressure switch set too narrow | Check pressure tank air charge (should be 2 bar below cut-in pressure for bladder tanks). Replace tank or recharge air. Widen pressure switch differential. |
| Water leaks from shaft | Packing gland too loose; mechanical seal failed; shaft sleeve worn | Tighten packing gland nuts evenly (allow 10-60 drops/minute for packing lubrication). Replace mechanical seal. Replace shaft sleeve if grooved. |

## Safety

- **Rotating parts**: The coupling between motor and pump is an entanglement hazard. Install a coupling guard (sheet metal or wire mesh) that completely encloses the rotating assembly. Never reach into the coupling area while the pump is running.
- **Pressure hazard**: Pump casings are rated for a maximum working pressure (typically 10-25 bar). Never operate above rated pressure. Install a pressure relief valve on the discharge side if system overpressure is possible.
- **Electrical hazard**: Pump motors operate at 200-480 V (three-phase). Lockout/tagout before any maintenance. Ground the motor frame to prevent shock if insulation fails.
- **Cavitation**: Indicated by a gravelly rattling noise from the pump. Not immediately dangerous but destroys the impeller over time. Fix the cause (increase suction pressure, reduce flow, lower pump speed) rather than tolerating the noise.
- **Water hammer**: Rapid closure of a [valve](water-valves.md) on the discharge side creates a pressure surge that can rupture the casing or pipework. Close valves slowly, especially on long pipelines with high flow velocities. Install surge protection (surge anticipator, air chamber, or water hammer arrestor) on systems with >2 m/s flow velocity. A sudden valve closure on a pipeline with 2 m/s flow velocity produces approximately 20 bar surge pressure — enough to rupture cast iron fittings.
- **Dry running**: Operating a centrifugal pump without liquid destroys the mechanical seal within 2-5 minutes. The seal faces require liquid for lubrication and heat removal. Install a dry-run protection relay (current monitor or flow switch) on unattended installations.

## Quality Control

- **Vibration baseline**: After installation and alignment, run the pump at BEP and record vibration amplitude at the bearing housings (horizontal, vertical, axial). Initial readings establish the baseline. Acceptable vibration velocity: <2.5 mm/s (RMS) for rigid-mounted pumps per ISO 10816. Recheck monthly — rising vibration indicates developing faults (bearing wear, impeller erosion, misalignment drift).
- **Performance verification**: Record flow, head, and power draw at the operating point. Compare to the pump curve. If power draw exceeds the motor nameplate rating, the pump is operating too far right of BEP. If head is above the curve, the system is more restrictive than designed.
- **Seal integrity**: Monitor seal leak rate. Mechanical seals should show zero visible leakage. Packing glands should drip 10-60 drops/minute (seal water lubrication). Zero drip on packing means the gland is too tight — the packing overheats and wears rapidly.
- **Bearing temperature**: Bearing housing temperature should stabilize within 10-20°C above ambient during normal operation. Temperatures above 80°C indicate inadequate lubrication, overloading, or impending failure. Check lubricant level and quality.
- **NPSH margin verification**: At commissioning, measure suction pressure at the pump inlet flange while operating at design flow. Calculate NPSHa = (suction gauge reading in m + velocity head) - vapor pressure. Confirm NPSHa exceeds NPSHr by at least 0.5 m. If not, investigate suction pipe sizing or consider raising the water source level.

## Variations and Alternatives

### Submersible Pump

A centrifugal pump and motor combined in a single waterproof unit, designed to operate submerged in the fluid. The motor is sealed from the fluid by a mechanical seal (often dual-seal with oil chamber between). Eliminates the suction lift problem — the pump sits at the bottom of the well or sump and pushes fluid upward.

**Prerequisites**: [Electricity](../energy/electricity.md), waterproof cable, [mechanical seals](../polymers/index.md).

**Construction**: Motor and pump share a common shaft. The motor is a water-cooled, sealed unit — often filled with oil or water for heat transfer. Dual mechanical seals with an oil-filled chamber between them provide redundant sealing. A moisture sensor in the oil chamber detects seal failure before water reaches the motor windings.

**Expected performance**: Flow: 5-500 m³/hour. Head: 10-200 m (multistage). Motor: 1-150 kW, submerged duty. Efficiency: 60-75%. The power cable must be rated for continuous submersion and protected from abrasion. See [Water Procurement](procurement.md) for well pump installations.

**Strengths**:
- No suction lift limitation — pump is at the water source
- Quiet operation (motor and pump submerged)
- Minimal above-ground footprint
- No priming required — starts underwater

**Weaknesses**:
- Motor must be pulled from the well for maintenance — requires hoist equipment
- Cable damage causes pump failure — protect from abrasion at every bend
- Higher unit cost than surface-mounted pumps
- Motor cooling depends on water flow past the motor housing — do not install in still water or above the water level

### Multistage Centrifugal Pump

Multiple impellers mounted on a single shaft within a common casing. Each stage adds head — total head = number of stages × head per stage. Used for high-head applications: boiler feed water (20-200 bar), reverse osmosis feed for [desalination](desalination.md) (55-70 bar), mine dewatering, and deep-well pumping.

**Prerequisites**: [Precision machining](../machine-tools/machining.md), [high-strength steel](../metals/iron-steel.md), multiple impeller castings.

**Construction**: Horizontal multistage (ring-section or barrel casing) for industrial applications. Vertical multistage turbine for deep wells. Inter-stage seals (wear rings) maintain clearance between impeller eye and casing — these are the primary wearing parts. Replace wear rings when clearance exceeds twice the design value.

**Expected performance**: Flow: 5-500 m³/hour. Head: 50-1000 m (5-100 bar). Efficiency: 65-82% depending on stages and specific speed. Stage count ranges from 2-12 for typical water applications; up to 30+ for boiler feed.

**Strengths**:
- Very high head capability in a single pump unit
- Modular — add or remove stages to adjust head without changing the motor
- Higher efficiency at high head than single-stage alternatives

**Weaknesses**:
- More complex than single-stage — more wearing parts (wear rings per stage)
- Axial thrust from stacked impellers requires balance drum or balancing disc
- Higher cost per unit of flow than single-stage
- Longer shaft is more susceptible to vibration and critical speed issues

### Vertical Turbine Pump

A vertical-shaft centrifugal pump with the impeller(s) submerged in a sump, well, or open water body. The motor sits above ground, connected to the impeller by a long line shaft through a column pipe. Column pipe serves as both the discharge conduit and the shaft housing.

**Prerequisites**: [Precision shaft alignment](../machine-tools/index.md), [steel column pipe](../metals/iron-steel.md), adequate overhead clearance for motor removal.

**Construction**: The bowl assembly (impeller + diffuser + casing) sits at the bottom, submerged. Column pipe sections (3 m each typical) bolt together from the bowl to the motor support at surface. The line shaft runs through the column, supported by bearings at each joint. Bearings are lubricated by the pumped water (or externally lubricated for abrasive fluids).

**Expected performance**: Flow: 50-5000 m³/hour. Head: 10-300 m. The largest municipal water pumps are vertical turbine units. Efficiency: 70-85% at BEP.

**Strengths**:
- Handles deep suction conditions without priming issues
- High capacity — municipal-scale flow rates
- Motor stays dry and accessible above flood level

**Weaknesses**:
- Requires overhead clearance for shaft removal (shaft length = pump setting depth)
- Line shaft bearings require lubrication (water-lubricated or grease-lubricated)
- Disassembly for impeller access is time-consuming

### Regenerative Turbine Pump

A specialized centrifugal variant where the impeller has short vanes on its periphery that regeneratively add energy to the fluid as it circulates in the casing annulus. Produces very high head per stage (up to 250 m at small flows). Very low specific speed (Ns < 10).

**Prerequisites**: [Precision machining](../machine-tools/machining.md) — tight clearances (0.05-0.10 mm) between impeller and casing are essential.

**Construction**: Similar to a standard centrifugal pump but with a flat impeller having peripheral vanes on one or both faces, running in a channel machined into the casing. The fluid makes multiple passes through the impeller vanes, gaining energy with each pass. The tight clearances mean that even small amounts of wear degrade performance.

**Expected performance**: Flow: 0.1-10 m³/hour. Head: 10-250 m. Efficiency: 30-50% (lower than standard centrifugal due to recirculation losses).

**Strengths**: Very high head per stage in a compact package. Can handle some entrained gas (unlike standard centrifugal).

**Weaknesses**: Limited to clean fluids — solids rapidly erode the tight clearances. Not suitable for abrasive or high-solids fluids. Low efficiency compared to standard centrifugal designs.

### Pump Type Selection Guide

| Application | Recommended Type | Flow | Head | Notes |
|-------------|-----------------|------|------|-------|
| Household water supply | End-suction, single-stage | 5-20 m³/hour | 20-50 m | Most common pump type |
| Village distribution | Split-case, single-stage | 20-100 m³/hour | 30-60 m | Duty/standby pair |
| Deep well (10-200 m) | Submersible multistage | 5-100 m³/hour | 30-200 m | Eliminates suction lift |
| River/lake intake | Vertical turbine | 50-5000 m³/hour | 10-60 m | Motor above flood level |
| RO desalination feed | Horizontal multistage | 50-500 m³/hour | 500-800 m | 55-70 bar discharge |
| Boiler feed | Barrel casing multistage | 10-200 m³/hour | 200-2000 m | High temperature service |
| Chemical injection | Regenerative turbine | 0.1-5 m³/hour | 50-250 m | Compact, precise |
| Cooling water circulation | End-suction or vertical | 100-2000 m³/hour | 15-30 m | Continuous duty, low head |

## References

- [Positive Displacement Pump](positive-displacement-pump.md) — for high-pressure, low-flow, and viscous fluid applications
- [Water Distribution](distribution.md) — centrifugal pumps pressurize distribution networks
- [Desalination](desalination.md) — high-pressure multistage centrifugal pumps for reverse osmosis
- [Water Valves](water-valves.md) — isolation and control valves for pump stations
- [Filtration Equipment](filtration-equipment.md) — strainers on pump suction lines for impeller protection
- [Iron & Steel](../metals/iron-steel.md) — materials for pump casings and impellers
- [Electricity](../energy/electricity.md) — motor power supply and control
- [Machine Tools](../machine-tools/machining.md) — precision machining for shafts, bores, and impellers

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Water](./index.md) • [All Domains](../../index.md)*
