# Electric Motor

> **Node ID**: `energy.electricity.motor`
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.electricity`](./electricity.md),
> [`metals.iron-steel`](../metals/iron-steel.md),
> [`metals.magnetic-materials`](../metals/magnetic-materials.md),
> [`metals.wire-drawing`](../metals/wire-drawing.md)
> **Enables**: None
> **Outputs**: mechanical_power
> **Timeline**: Years 5-30
> **Critical**: No

## Overview

Electric motors convert electrical energy into rotational mechanical power through the interaction of magnetic fields. A current-carrying conductor in a magnetic field experiences a force (Lorentz force: F = BIL), and the motor geometry converts this linear force into torque. Motors are the inverse of generators — the same machine can serve as both, depending on whether electrical or mechanical energy is the input.

Three dominant motor families exist. **DC motors** (series, shunt, compound, permanent magnet) use a commutator to switch current direction mechanically. They offer simple speed control (varying voltage adjusts speed) and high starting torque, but the commutator and brushes wear and spark. **AC induction motors** (squirrel cage) use a rotating magnetic field from the stator to induce current in the rotor — no electrical connection to the rotor, so no brushes. Invented by Tesla in 1887, they are the workhorse of industrial drives: rugged, cheap, maintenance-free, 75-90% efficient. **Brushless DC (BLDC)** and permanent-magnet synchronous motors use electronic commutation instead of brushes, achieving 85-95% efficiency and precise speed control, but require power electronics ([VFDs](../electronics/electrical-systems.md)).

Motors power everything from fractional-horsepower fans to 50,000 kW industrial mill drives. They are the primary load on the [electrical grid](./electricity.md), consuming 40-50% of global electricity. For a bootstrapping civilization, DC motors are first (simple, controllable from a battery), followed by AC induction (once alternating current is available), then BLDC (requiring [semiconductor power electronics](../electronics/index.md)).

The motor's key dependencies are [copper wire](../metals/wire-drawing.md) for windings, [magnetic materials](../metals/magnetic-materials.md) for field poles or permanent magnets, and [iron/steel](../metals/iron-steel.md) for the laminated core that concentrates magnetic flux.

## Prerequisites

### Materials

- [Copper wire](../metals/wire-drawing.md) — enamelled magnet wire, 0.5-2.0 mm diameter (18-24 AWG) for most windings; up to 5 mm for large motors
- [Electrical steel](../metals/iron-steel.md) — silicon steel (2-4% Si) laminations, 0.35-0.65 mm thick, for stator and rotor cores. Silicon reduces eddy-current losses.
- [Permanent magnets](../metals/magnetic-materials.md) — for PMDC and BLDC rotors. Ferrite (Ba/Sr ferrite, 0.3-0.4 T), Alnico (0.7-1.0 T), or NdFeB (1.0-1.4 T) depending on technology tier.
- Insulation — enamel (polyvinyl formal or polyamide-imide) on magnet wire; slot liners (kraft paper, Mylar, mica); phase insulation (Nomex or varnished cloth)
- Bearing steel — through-hardened 52100 chrome steel balls and races, or SAE 1045 carbon steel for low-speed applications
- Aluminium or cast iron frame — housing and end bells
- Commutator (DC motors only) — copper segments moulded in moulding compound, insulated by mica segments

### Tools and Equipment

- [Wire drawing](../metals/wire-drawing.md) — to produce magnet wire of required gauge
- [Electricity supply](./electricity.md) — for testing and magnetisation
- Coil winding machine — manual or motorised, with turn counter and wire tensioner
- Hydraulic press (5-50 tonne) — for stacking laminations and pressing bearings onto shaft
- Varnish tank and oven — for vacuum impregnation and curing of wound stators
- Dynamometer — for load testing finished motors (0.5-500 kW range)
- [Magnetising equipment](../metals/magnetic-materials.md) — DC current pulse through a coil to magnetise permanent magnets or field poles

### Knowledge

- Magnetic circuit design: flux Φ = NI/R (ampere-turns divided by reluctance). Air gaps are the dominant reluctance — keep gap length to 0.2-1.0 mm for efficiency.
- Back-EMF: a spinning motor generates a voltage opposing the supply (E = kΦω, where k is a motor constant, Φ is flux, ω is angular speed). At steady state, supply voltage ≈ back-EMF + IR drop.
- Torque-speed characteristic: DC shunt motor has nearly flat torque-speed curve (speed varies <10% from no-load to full-load). Series motor has steeply falling curve (high starting torque, no-load overspeed risk).
- Lamination theory: eddy current losses scale with the square of lamination thickness. 0.35 mm laminations lose 4× less eddy power than 0.65 mm at the same flux and frequency.

### Infrastructure

- Machine shop with [lathe](../machine-tools/index.md) and [milling machine](../machine-tools/machining.md) for shaft machining, housing boring, and commutator turning
- Coil winding area with wire inventory and winding fixtures
- Varnish impregnation and curing facility — fume extraction required for solvent-based varnishes
- Electrical test bench with variable DC and AC supply, ammeter, voltmeter, and tachometer

## Bill of Materials

### DC Shunt Motor (1 kW, 180 V, 1750 RPM)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|--------------|
| Copper magnet wire (enamelled, 1.0 mm) | 3-5 kg (armature + field windings) | [Wire drawing](../metals/wire-drawing.md) | Aluminium wire (60% conductivity by area, lighter but larger) |
| Silicon steel laminations (3.5% Si, 0.5 mm) | 15-25 kg (stator yoke + armature core) | [Iron and steel](../metals/iron-steel.md) | Carbon steel laminations (higher losses, 10-15% efficiency penalty) |
| Steel shaft (1045, 25 mm dia × 200 mm) | 1 piece, 1.5 kg | [Iron and steel](../metals/iron-steel.md) | Stainless steel (expensive, unnecessary) |
| Commutator (copper bars + mica) | 1 unit, 12-24 segments | [Copper](../metals/copper-refining.md) + mica | — (essential for brushed DC) |
| Carbon brushes (8-12 mm × 15-20 mm) | 2-4 pieces | Carbon/graphite compaction | Copper-graphite (lower voltage drop, faster wear) |
| Bearings (6204-2RS, 20 mm ID) | 2 pieces | Bearing steel | Sleeve bearings (babbitt on steel, lower speed limit) |
| Cast iron or aluminium frame | 1 housing + 2 end bells, 5-10 kg | [Foundry](../metals/iron-steel.md) | Welded steel frame (fabrication vs casting) |
| Insulation (enamel, slot liner, phase) | 0.2-0.5 kg total | [Polymers](../polymers/index.md) | Mica + varnished cloth (class H, high-temperature) |

### AC Induction Motor (5.5 kW, 400 V 3-phase, 1450 RPM)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|--------------|
| Copper magnet wire (enamelled, 1.2-1.5 mm) | 8-12 kg (stator windings) | [Wire drawing](../metals/wire-drawing.md) | — |
| Silicon steel laminations (3.5% Si, 0.5 mm) | 35-50 kg (stator + rotor core) | [Iron and steel](../metals/iron-steel.md) | — |
| Aluminium (die-cast rotor bars) | 1-2 kg | [Aluminium](../metals/aluminum.md) | Copper die-cast rotor (higher efficiency, 1-2% gain, higher cost) |
| Steel shaft (1045, 35 mm dia × 300 mm) | 1 piece, 3 kg | [Iron and steel](../metals/iron-steel.md) | — |
| Bearings (6307-2RS, 35 mm ID) | 2 pieces | Bearing steel | — |
| Cast iron frame (IEC 132) | 1 housing + 2 end bells, 20-30 kg | [Foundry](../metals/iron-steel.md) | Aluminium frame (lighter, higher cost) |

## Process Description

### DC Motor Construction

1. **Build magnetic circuit**: Stack silicon steel laminations to form the stator yoke (field poles) and armature core. Insulate each lamination with varnish or oxide layer to break eddy current paths. Press the armature stack onto the steel shaft.
2. **Wind field coils**: Wrap enamelled copper wire around each field pole shoe. Turns determined by field current and flux requirement (typically 200-1000 turns of 0.8-1.5 mm wire). Secure with tape and vacuum-impregnate with insulating varnish. Cure at 120-150°C for 2-4 hours.
3. **Wind armature**: Lay enamelled copper wire into armature slots in a pattern determined by pole count and slot count (lap or wave winding). Each coil end connects to a commutator segment. Secure windings with banding wire or glass thread. Vacuum-impregnate and cure.
4. **Fit commutator and brushes**: Press commutator onto shaft, turn concentric to <0.02 mm runout. Mount brush holders in end bell, fit carbon brushes with spring pressure of 15-25 kPa. Ensure brushes move freely in their boxes.
5. **Assemble**: Install bearings on shaft (press fit, 1-3 tonne). Mount end bells to frame. Set air gap between armature and field poles to 0.3-0.8 mm. Check that armature rotates freely — no rubbing.
6. **Test**: Apply rated voltage. Measure no-load speed and current. Apply load via dynamometer or coupled generator. Measure full-load speed, current, torque, efficiency, and temperature rise. Adjust brush position for minimum sparking (neutral commutation plane).

### AC Induction Motor (Squirrel Cage) Construction

1. **Stack stator laminations**: Press 0.35-0.5 mm silicon steel laminations into the cast iron frame to form the stator core. Slots face inward to receive windings.
2. **Insert slot liners**: Place 0.2-0.3 mm insulation (Mylar + kraft paper or Nomex) in each slot to protect wire from lamination edges.
3. **Wind stator**: Insert enamelled copper wire into slots by hand or machine (insertion winding for random-wound, or formed coils for large motors). For a 3-phase motor, wind three sets of coils offset by 120 electrical degrees. Connect windings in star (Y) or delta (Δ) configuration per the nameplate.
4. **Make rotor**: Stack laminations on shaft. Die-cast aluminium into the slots to form conductor bars and end rings (short-circuiting rings). This "squirrel cage" is the secondary winding — no external connection.
5. **Assemble and test**: Install bearings, mount rotor in stator, bolt end bells. Check air gap (0.3-0.8 mm). Apply rated 3-phase voltage. Measure no-load speed (should be just below synchronous speed: 1500 RPM at 50 Hz, 4 poles). Load test to full rated torque.

### BLDC Motor Construction

1. Build stator as for AC induction motor (laminated core with 3-phase copper windings).
2. Build rotor with permanent magnets (surface-mount or interior) on a steel hub. Magnetise after assembly using a high-current pulse magnetiser.
3. Assemble with Hall-effect sensors on the stator to detect rotor position for electronic commutation.
4. Connect to a 3-phase inverter (electronic speed controller) that energises stator phases in sequence based on Hall sensor feedback.

## Quantitative Parameters

| Parameter | DC Shunt | DC Series | AC Induction (squirrel cage) | BLDC / PMSM |
|-----------|----------|-----------|------------------------------|-------------|
| Power range | 0.1-500 kW | 0.1-200 kW | 0.1-50,000 kW | 0.05-500 kW |
| Voltage | 6-600 V DC | 6-600 V DC | 230-6900 V AC | 12-800 V DC |
| Efficiency (full load) | 75-90% | 75-88% | 80-93% | 85-97% |
| Starting torque | 150-200% rated | 150-600% rated | 150-250% rated | 150-300% rated |
| Speed control | Easy (vary voltage) | Moderate | VFD required | Electronic controller |
| Starting current | 150-200% rated | 300-600% rated | 500-800% rated (DOL) | Controlled by controller |
| Power factor | 1.0 (DC) | 1.0 (DC) | 0.75-0.90 lagging | 0.90-0.98 |
| Speed regulation | 5-10% | 20-50% | 2-5% | <1% (closed loop) |
| Maintenance | Brush replacement (2,000-10,000 h) | Brush replacement | Bearing grease only | Bearing grease only |
| Typical applications | Machine tools, cranes, traction | Vehicle starter, traction, hoists | Pumps, fans, compressors, conveyors | Servo drives, EVs, drones, precision automation |

### Efficiency Classes (IEC 60034-30-1, AC induction)

| Class | Efficiency (4-pole, 5.5 kW, 50 Hz) | Loss reduction vs IE1 |
|-------|--------------------------------------|------------------------|
| IE1 (Standard) | 84-87% | Baseline |
| IE2 (High) | 87-90% | 10-15% loss reduction |
| IE3 (Premium) | 89-92% | 20% loss reduction |
| IE4 (Super Premium) | 92-94% | 30% loss reduction |
| IE5 (Ultra Premium) | 94-96% | 40% loss reduction (future) |

## Scaling Notes

- **Bench scale** (<100 W): Hand-wound coils on stamped laminations. Bearings are standard sizes ( skateboard bearings: 608Z, 8 mm ID). Useful for fans, small pumps, and prototypes.
- **Workshop scale** (0.5-5 kW): Manual or semi-automatic coil winding machine, hydraulic press for lamination stacking. One motor per day per worker. Targets: machine tools, small pumps, [workshop drives](../machine-tools/index.md).
- **Production scale** (5-500 kW): Automated winding insertion machines, robotic die-casting for squirrel-cage rotors, conveyorised varnish impregnation. 10-1000 motors/day. Capital cost dominates at this scale — winding machines cost $50k-$2M.

Key scaling bottlenecks: lamination stamping throughput (a 100-tonne press stamps 30-60 laminations/minute); die-casting of rotor bars (requires aluminium melting and die-casting machine); copper wire supply (a 100 kW motor needs 40-80 kg of magnet wire — one wire-drawing line supplies it); testing capacity (a dynamometer rated for the motor's full output power is required).

Efficiency improvements at scale are disproportionately valuable: a 1% efficiency gain on a 100 kW motor running 8,000 h/year saves 8,000 kWh/year. Moving from IE2 to IE3 class typically adds 20-30% to motor cost but pays back in 1-3 years at industrial electricity prices.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Motor will not start (no rotation, humming sound) | Single-phasing (one phase lost) on 3-phase motor; blown fuse; loose connection; stuck rotor | Check all three phases with voltmeter; inspect fuses and contactors; manually rotate shaft to check for mechanical binding |
| Excessive sparking at brushes (DC motor) | Brush wear (<10 mm length), weak brush spring, dirty commutator, incorrect brush grade, shorted armature coil | Replace brushes at <50% original length; clean commutator with commstone (180-240 grit); check spring pressure (15-25 kPa); turn commutator if grooved >0.1 mm |
| Motor overheating (>80°C frame temperature) | Overload (current >110% rated), insufficient ventilation, dirty cooling fins, bearing failure, high ambient temperature | Measure current vs nameplate; clean air passages; check bearing temperature (should be <70°C); reduce load or improve cooling |
| Low starting torque | Low voltage at terminals (undersized supply cable), worn bearings increasing friction, open or shorted winding | Measure terminal voltage under load; replace bearings; test winding resistance between phases (should be within ±5% of each other) |
| Vibration and noise (above 2.5 mm/s RMS) | Misalignment between motor and load, unbalanced rotor, worn bearings, loose mounting bolts, resonance | Laser-align coupling to <0.05 mm; dynamically balance rotor (ISO 1940 G6.3 or better); replace bearings; tighten bolts; check for structural resonance |
| AC motor runs backwards | Phase sequence reversed (two leads swapped) | Swap any two of the three phase leads at the motor terminal box or starter |
| BLDC motor jerks or stalls | Hall sensor misalignment or failure, loose phase wire, controller fault | Check Hall sensor signals with oscilloscope; reseat phase connectors; test controller with known-good motor |
| Ground fault (breaker trips on start) | Winding insulation failure to frame, moisture in terminal box, damaged cable | Megger test: apply 500-1000 V DC between winding and frame; reading <1 MΩ indicates insulation failure; dry out motor or rewind |

## Safety

- **Electrical shock**: Motor terminals carry 230-6900 V. Even a 230 V supply can be lethal. Lock-out/tag-out before opening terminal boxes. Verify dead with a voltage tester before touching. One-hand rule when probing live circuits.
- **Rotating machinery**: Shafts, couplings, and fans can entangle clothing, hair, or fingers. Install guards on all rotating parts. Never wear loose clothing or jewellery near running motors. Emergency stop within arm's reach.
- **Arc flash**: Opening a motor contactor under load can produce an arc reaching 20,000°C. Use arc-rated PPE (cat 2-4 depending on available fault current) when working on energised starters.
- **Thermal burns**: Motor frames can reach 80-100°C at full load. Allow 30 minutes cooling after shutdown before touching. Wear gloves for handling hot motors.
- **Stored energy**: Capacitors in [motor controllers](../electronics/electrical-systems.md) and BLDC drives retain charge after disconnection. Discharge capacitors before servicing.

## Quality Control

### Acceptance Criteria

- **Efficiency**: Measured at rated load via dynamometer. Must meet nameplate value ±0.5% (IE2/IE3 tolerance per IEC 60034-2-1).
- **Temperature rise**: By resistance method. Class B insulation (130°C): rise ≤80°C. Class F (155°C): rise ≤105°C. Class H (180°C): rise ≤125°C. Measured after thermal equilibrium at full load (typically 2-4 hours).
- **Vibration**: Per ISO 10816. Acceptable: <2.3 mm/s RMS for rigid-mount machines (grade A). Alarm: 2.3-4.5 mm/s. Reject: >4.5 mm/s.
- **Insulation resistance**: Megger test at 500 V DC (for <1000 V motors) or 1000 V DC (for >1000 V). Accept: >1 MΩ per kV of rated voltage + 1 MΩ minimum.
- **No-load current**: AC induction: 25-40% of rated full-load current. Significantly higher indicates air gap problem or core damage.

### Testing Methods

- **No-load test**: Apply rated voltage, measure current, speed, input power. Separates friction/windage and core losses.
- **Blocked rotor (locked rotor) test**: Apply reduced voltage to stalled motor. Measures starting torque and current. Equivalent to short-circuit test on a transformer.
- **Load test**: Couple to dynamometer (eddy current, powder brake, or DC generator). Measure torque, speed, input power, and efficiency at 25%, 50%, 75%, 100%, 125% of rated load.
- **Hipot (dielectric withstand) test**: Apply 1000 V + 2 × rated voltage for 1 minute between windings and frame. No breakdown allowed.

### Sampling Protocol

- 100% of production motors: no-load test, megger, hipot
- 5-10% of production: full load test on dynamometer
- 1% of production or one per batch: teardown inspection of windings, bearings, laminations

## Variations and Alternatives

### Motor Type Selection Guide

| Application | Recommended type | Reason |
|-------------|-----------------|--------|
| Pump, fan, compressor | AC induction (IE3) | Cheap, reliable, maintenance-free, grid-powered |
| Machine tool spindle | DC shunt or BLDC | Speed control required; DC simpler, BLDC more efficient |
| Crane, hoist, winch | DC series or wound-rotor induction | High starting torque, speed control under load |
| Electric vehicle traction | BLDC / PMSM | Highest efficiency, compact size, regenerative braking |
| Servo positioning (robotics) | BLDC with encoder | Precise position and torque control, high dynamic response |
| Vehicle starter (12 V) | DC series | Very high torque from battery, short duty cycle |
| Precision instruments (CNC) | Stepper motor (specialised BLDC variant) | Open-loop position control, holding torque |

### Regional and Historical Adaptations

- **Early bootstrap (no AC grid)**: DC motors run from batteries or DC generators. Simpler to control; commutator wear is acceptable when alternatives are limited.
- **Pre-electronic era**: AC induction motors run direct-on-line (DOL) at fixed speed. Speed control via mechanical means (belt drives, gears, variable-diameter pulleys).
- **Modern era**: VFD-controlled induction motors replace DC motors in most speed-control applications. BLDC replaces DC brushed motors where efficiency and maintenance-free operation justify the electronics cost.

## References

- [Electricity generation & distribution](./electricity.md) — parent capability; covers wire drawing, generators, and power distribution
- [Generator](./generator.md) — the inverse machine; same construction principles
- [Magnetic materials](../metals/magnetic-materials.md) — permanent magnets and soft magnetic steel for motor cores
- [Wire drawing](../metals/wire-drawing.md) — copper magnet wire production
- [Power distribution](./power-distribution.md) — motor starters, protection, and supply infrastructure
- [Electrical systems](../electronics/electrical-systems.md) — variable frequency drives and motor controllers
- [Machine tools](../machine-tools/index.md) — primary consumer of motors for industrial drives

---
*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
