# Centrifugal Pump

> **Node ID**: water.centrifugal-pump
> **Domain**: [Water](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`water.distribution`](distribution.md), [`water.desalination`](desalination.md), [`water.sewage`](sewage.md)
> **Timeline**: Years 15-25
> **Outputs**: pressurized_water
> **Critical**: Yes — centrifugal pumps are the primary mover for water distribution, treatment, and industrial recirculation beyond gravity-fed systems

## Principle

A centrifugal pump converts rotational kinetic energy from an impeller into hydrodynamic pressure. Fluid enters the impeller eye (center) axially and is accelerated radially outward by rotating vanes. The volute casing (spiral-shaped housing) collects the high-velocity discharge and converts velocity head to pressure head via the Bernoulli principle. The relationship between flow rate Q, head H, and power P follows the affinity laws: flow is proportional to speed (Q ∝ N), head proportional to speed squared (H ∝ N²), and power proportional to speed cubed (P ∝ N³).

The pump curve (head vs. flow) defines the operating characteristic for a given impeller diameter and speed. The system curve (static head + friction losses vs. flow) defines the resistance of the piping network. The intersection of pump curve and system curve is the operating point. A centrifugal pump cannot develop pressure beyond its shutoff head (flow = 0) and cannot deliver flow beyond its runout condition (head = 0).

Key limitation: a centrifugal pump cannot lift water on its suction side by more than approximately 7 m at sea level (theoretical atmospheric limit ~10.3 m, reduced by vapor pressure and friction losses). For deeper lifts, a positive-displacement pump or a submersible centrifugal pump is required.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Cast iron (casing) | 20-80 kg | Class 30 gray iron or ductile iron, for volute housing | [Iron & Steel](../metals/iron-steel.md) | Bronze (corrosive water), stainless steel (food/pharma) |
| Bronze or cast iron (impeller) | 5-15 kg | 85-5-5-5 bronze (water service) or cast iron (non-corrosive) | [Metals](../metals/index.md) | Stainless steel (304/316) for corrosive service |
| Steel shaft | 2-5 kg | 1045 or 416 stainless, 25-40 mm diameter, ground to 0.8 μm Ra | [Iron & Steel](../metals/iron-steel.md) | 316 stainless (corrosive service) |
| Mechanical seal or packing | 1 set | Carbon-ceramic mechanical seal or PTFE/graphite packing | [Polymers](../polymers/index.md) | Gland packing (leaks slightly, acceptable for non-critical service) |
| Bearings | 2-4 | Deep-groove ball bearings (6205-6209 series) rated for pump speed + radial load | [Bearings](../machine-tools/bearings-abrasives.md) | Sleeve bearings (oil-lubricated, for vertical pumps) |
| Electric motor | 1 | 0.75-15 kW, 1450 or 2900 RPM (4-pole or 2-pole at 50 Hz) | [Electricity](../energy/electricity.md) | Diesel engine, steam turbine, or belt-driven from line shaft |
| Bolts and gaskets | 1 set | Foundation bolts (M12-M16), flange gaskets (rubber or fiber) | [Fasteners](../metals/fasteners.md) | — |

## Construction Steps

### Impeller

1. **Cast the impeller**: Use a split sand mold with a pattern matching the impeller geometry. Typical closed-impeller design: 5-7 backward-curved vanes, 150-250 mm outer diameter for a medium-capacity pump, vane thickness 4-8 mm at the periphery. Pour molten bronze (for water service) or cast iron at the appropriate pouring temperature (bronze: 1050-1150°C; cast iron: 1350-1450°C).
2. **Machine the impeller bore**: Chuck the impeller in a lathe on a mandrel that registers off the vane tips. Bore the center hole to fit the shaft diameter (25-40 mm typical) with an H7 tolerance (+0.000/-0.025 mm). Cut a keyway 6-10 mm wide × 3-6 mm deep for shaft locking.
3. **Balance the impeller**: Mount the impeller on a balance mandrel supported by knife-edge ways. Heavy spots roll to the bottom. Remove material by grinding or drilling from the heavy side. Target balance grade G6.3 (maximum residual unbalance in g·mm = 6.3 × rotor mass in kg × radius in mm / 1000). Unbalanced impellers cause vibration, bearing wear, and seal failure.
4. **Trim the impeller diameter**: If the pump produces too much head at the design speed, reduce impeller diameter by turning on a lathe. Head reduction follows: H_new = H_original × (D_new / D_original)². Do not reduce by more than 20% or vane geometry is compromised.

### Volute Casing

5. **Cast the volute casing**: Use a sand mold with a core forming the internal spiral passage. The volute cross-section increases from the tongue (cutwater) to the discharge flange, collecting flow from the impeller periphery. Minimum wall thickness: 6-8 mm for cast iron at pressures up to 10 bar. Cast the suction and discharge flanges integral with the casing (bolt holes drilled after casting).
6. **Machine mating surfaces**: Face the suction flange (inlet) and discharge flange (outlet) flat for gasket sealing. Bore the stuffing box (seal housing) to 0.05 mm clearance over the shaft diameter. Drill and tap bearing housing bores concentric with the volute center to within 0.05 mm.

### Assembly

7. **Install shaft and bearings**: Press bearings onto the shaft using an arbor press (never hammer bearings — brinelling damage). Install the shaft/bearing assembly into the bearing housing. Shaft runout (total indicated reading at the impeller end) must not exceed 0.05 mm.
8. **Install the mechanical seal**: Mount the stationary seal face in the stuffing box bore. Mount the rotating seal face on the shaft. The two faces are lapped flat to within 0.5 μm (helium light-band contact). Seal faces are spring-loaded to maintain contact. Apply a thin film of clean oil to the seal faces before assembly — never run a dry mechanical seal.
9. **Mount impeller on shaft**: Slide the impeller onto the shaft keyway. Secure with a locknut or lockwasher. Verify impeller-to-volute clearance: the gap between impeller outer edge and volute tongue should be 0.5-1.0 mm. Too tight → rubbing and wear. Too loose → internal recirculation and reduced efficiency.
10. **Close the casing**: Bolt the casing halves together (split-case design) or install the cover plate (end-suction design). Torque casing bolts in a cross-pattern to the specified value (typically 40-80 N·m for M12-M16 bolts). Install flange gaskets on suction and discharge ports.
11. **Couple to motor**: Align the pump shaft to the motor shaft within 0.05 mm angular misalignment and 0.1 mm parallel offset, measured with a dial indicator at the coupling faces. Misalignment causes vibration, coupling wear, and bearing failure. Secure the coupling with a flexible spider or grid element to absorb residual misalignment.
12. **Mount on baseplate**: Bolt the pump and motor to a common baseplate (steel channel or cast iron). Grout the baseplate to the concrete foundation with non-shrink grout. Check alignment after grouting — grout shrinkage can shift the baseplate.

## Calibration and Verification

1. **Rotation check**: Jog the motor (briefly energize) and confirm impeller rotation matches the arrow on the casing. Reverse rotation pumps water backward and produces zero net head. Swap any two motor leads to reverse a three-phase motor.
2. **Prime the pump**: Fill the suction piping and pump casing completely with water before starting. A centrifugal pump cannot prime itself — it merely spins air with no fluid transfer. Air-bound pumps overheat and destroy the seal.
3. **Measure shutoff head**: Close the discharge valve completely. Start the pump. Read the discharge pressure gauge. Shutoff head (m) = gauge pressure (bar) × 10.2. Compare to the manufacturer's pump curve at the installed impeller diameter. Deviation >10% indicates impeller damage, wrong rotation, or air in the system.
4. **Measure flow at operating point**: Open the discharge valve to the normal operating position. Measure flow rate with a flow meter or timed fill. Verify the operating point (flow, head) lies on the pump curve. If flow is significantly below design, check for suction-side air leaks, clogged strainers, or undersized piping.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Flow range (medium pump, 150 mm impeller) | 10-100 m³/hour |
| Head range | 10-80 m (1-8 bar) |
| Efficiency (at best efficiency point) | 55-75% |
| Suction lift (maximum) | 5-7 m at sea level |
| Net positive suction head required (NPSHr) | 2-6 m depending on design |
| Speed | 1450 or 2900 RPM (50 Hz); 1750 or 3500 RPM (60 Hz) |
| Power consumption | 0.75-15 kW typical for medium-capacity water pumps |
| Seal life (mechanical seal) | 1-3 years in clean water service |
| Bearing life (L10) | 20,000-40,000 hours |
| Service life (casing) | 15-30 years in non-corrosive water |

## Strengths

- Simple, robust construction with few wearing parts (seal, bearings) — low maintenance
- Handles clean and slightly contaminated water without damage
- Flow is continuous and pulse-free — no vibration in piping from pressure pulsations
- Can operate against a closed discharge valve for short periods without damage (unlike positive-displacement pumps)
- Available in an enormous range of sizes — from fractional-horsepower circulators to 10 MW municipal supply pumps

## Weaknesses

- Cannot self-prime — requires flooded suction or external priming
- Efficiency drops sharply at flow rates far from the best efficiency point (BEP) — oversized pumps waste energy
- Viscous fluids rapidly degrade performance — centrifugal pumps move thin fluids (water, light oils) only
- Cavitation damage occurs when suction pressure drops below the fluid vapor pressure — erodes impeller vanes and destroys the pump over weeks to months
- Not suitable for metering or dosing — flow varies with system resistance

## Safety

- **Rotating parts**: The coupling between motor and pump is an entanglement hazard. Install a coupling guard (sheet metal or wire mesh) that completely encloses the rotating assembly. Never reach into the coupling area while the pump is running.
- **Pressure hazard**: Pump casings are rated for a maximum working pressure (typically 10-25 bar). Never operate above rated pressure. Install a pressure relief valve on the discharge side if system overpressure is possible.
- **Electrical hazard**: Pump motors operate at 200-480 V (three-phase). Lockout/tagout before any maintenance. Ground the motor frame to prevent shock if insulation fails.
- **Cavitation**: Indicated by a gravelly rattling noise from the pump. Not immediately dangerous but destroys the impeller over time. Fix the cause (increase suction pressure, reduce flow, lower pump speed) rather than tolerating the noise.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Pump runs but no flow | Not primed; air leak on suction side; impeller loose on shaft; wrong rotation | Fill casing and suction pipe with water. Check suction fittings for air leaks with soap solution. Verify impeller key is installed. Check rotation direction. |
| Low flow and low head | Worn impeller (vane tips eroded); impeller diameter too small for system; air entrainment | Inspect impeller vanes. Measure impeller diameter against spec. Check suction for vortexing or air leaks. |
| Pump draws high current | Impeller rubbing on volute; bearing failure; pump operating far right of BEP (high flow, low head) | Check impeller clearance. Listen for bearing noise (rough, grinding). Throttle discharge valve to move operating point toward BEP. |
| Cavitation noise (gravelly rattle) | Insufficient NPSHa — suction lift too high, suction pipe too small, or fluid too hot | Reduce suction lift. Increase suction pipe diameter. Lower fluid temperature. Install a booster pump on the suction side. |
| Seal leaking | Mechanical seal faces worn, contaminated, or run dry | Replace mechanical seal. Ensure pump is never run dry — seal faces require fluid for lubrication and cooling. |
| Excessive vibration | Impeller unbalance; shaft misalignment; worn bearings; resonance with structure | Rebalance impeller. Realign pump-to-motor coupling. Replace bearings. Stiffen or dampen the baseplate. |

## See Also

- [Positive Displacement Pump](positive-displacement-pump.md) — for high-pressure, low-flow, and viscous fluid applications
- [Water Distribution](distribution.md) — centrifugal pumps pressurize distribution networks
- [Desalination](desalination.md) — high-pressure multistage centrifugal pumps for reverse osmosis
- [Water Valves](water-valves.md) — isolation and control valves for pump stations
- [Iron & Steel](../metals/iron-steel.md) — materials for pump casings and impellers
- [Electricity](../energy/electricity.md) — motor power supply and control

[← Back to Water](index.md)
