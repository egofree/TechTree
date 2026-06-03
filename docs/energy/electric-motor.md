# Electric Motor

> **Node ID**: energy.electricity.motor
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.electricity`](electricity.md), [`machine-tools.machining`](../machine-tools/machining.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: all factory mechanization, pumps, fans, compressors, conveyors
> **Timeline**: Years 15-25
> **Outputs**: rotary_mechanical_power_electric
> **Critical**: Yes — electric motors are the universal prime mover for factory mechanization, replacing line shafts and enabling individual machine drive

## Principle

An electric motor converts electrical energy into mechanical rotation through the interaction of magnetic fields. Current-carrying conductors in a magnetic field experience a force (Lorentz force): F = I × L × B, where I is current, L is conductor length, and B is magnetic flux density. In a motor, the armature (rotor) windings carry current in a magnetic field produced by field poles (stator), creating torque that rotates the shaft.

**DC motors** use a commutator to reverse current direction each half-turn, maintaining continuous torque in one direction. Three winding configurations exist: series-wound (field and armature in series — high starting torque, variable speed), shunt-wound (field and armature in parallel — constant speed, moderate starting torque), and compound-wound (combination of both). A DC motor is mechanically identical to a DC generator — any dynamo can operate as a motor.

**AC induction motors** (the most common industrial motor) operate on a different principle: the stator's three-phase winding creates a rotating magnetic field that sweeps past the rotor conductors, inducing current in them (by transformer action). The induced current in the rotor interacts with the rotating field, producing torque. The rotor always spins slightly slower than the rotating field (slip), typically 2-5% below synchronous speed. No commutator, no brushes — the induction motor is simpler, more robust, and lower-maintenance than any DC motor.

Synchronous speed: n_s = 120 × f / p, where f = supply frequency (Hz) and p = number of poles. At 50 Hz with 4 poles: n_s = 1500 RPM. Actual rotor speed: 1425-1470 RPM (3-5% slip).

## Prerequisites

- [Copper wire](electricity.md) — drawn and insulated
- [Silicon steel laminations](../metals/iron-steel.md) — for stator and rotor cores
- [Lathe](../machine-tools/machining.md) — for shaft and housing machining
- [Die-casting or casting](../machine-tools/casting.md) — for aluminum rotor bars (induction motor)
- [Insulating materials](../polymers/thermoplastics.md) — enamel, kraft paper, varnish

## Materials

### DC Motor (5 kW, 220V, 1500 RPM)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Copper magnet wire (armature)](electricity.md) | 5-10 kg | 0.8-1.5 mm diameter, enamel insulated | [Wire Drawing](electricity.md) | Aluminum wire (60% conductivity) |
| [Copper magnet wire (field)](electricity.md) | 3-6 kg | 0.5-1.0 mm diameter, enamel insulated | [Wire Drawing](electricity.md) | — |
| [Silicon steel laminations](../metals/iron-steel.md) | 20-40 kg | 0.35-0.50 mm thick, 3% Si | [Iron & Steel](../metals/iron-steel.md) | Low-carbon steel (higher loss) |
| [Steel shaft](../metals/iron-steel.md) | 1 piece | 35-50 mm diameter × 250-400 mm | [Machining](../machine-tools/machining.md) | — |
| [Cast iron frame](../machine-tools/casting.md) | 1 piece | 150-250 mm diameter | [Foundry](../machine-tools/casting.md) | Fabricated steel |
| [Copper commutator](../metals/copper-bronze.md) | 1 assembly | 20-40 segments, hard-drawn copper | [Wire Drawing](electricity.md) | — |
| [Carbon brushes](../chemistry/index.md) | 4 pcs | Carbon-graphite, matched to commutator size | [Chemistry](../chemistry/index.md) | Copper gauze (high wear) |
| [Bearings](../machine-tools/bearings-abrasives.md) | 2 pcs | Ball bearings, shaft diameter matched | [Machine Tools](../machine-tools/index.md) | Sleeve bearings |
| [Insulation](../polymers/thermoplastics.md) | 1-3 kg | Shellac, kraft paper, cotton tape | [Polymers](../polymers/index.md) | Silk, mica |

### AC Induction Motor (7.5 kW, 400V three-phase, 4-pole)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Copper magnet wire (stator)](electricity.md) | 10-20 kg | 0.8-1.5 mm, enamel insulated, three-phase | [Wire Drawing](electricity.md) | Aluminum wire (larger gauge) |
| [Silicon steel laminations (stator)](../metals/iron-steel.md) | 40-70 kg | 0.35-0.50 mm, internal slots | [Iron & Steel](../metals/iron-steel.md) | Low-carbon steel |
| [Silicon steel laminations (rotor)](../metals/iron-steel.md) | 15-30 kg | 0.35-0.50 mm, external slots | [Iron & Steel](../metals/iron-steel.md) | Solid iron rotor (very inefficient) |
| [Aluminum rotor bars](../metals/aluminum.md) | 2-5 kg | Cast into rotor slots, end rings | [Casting](../machine-tools/casting.md) | Copper bars (more expensive, lower loss) |
| [Steel shaft](../metals/iron-steel.md) | 1 piece | 40-55 mm diameter × 300-450 mm | [Machining](../machine-tools/machining.md) | — |
| [Cast iron frame](../machine-tools/casting.md) | 1 piece | 200-300 mm diameter, with cooling fins | [Foundry](../machine-tools/casting.md) | Fabricated steel |
| [Bearings](../machine-tools/bearings-abrasives.md) | 2 pcs | Ball bearings, sealed | [Machine Tools](../machine-tools/index.md) | Sleeve bearings |
| [Insulation](../polymers/thermoplastics.md) | 2-4 kg | Enamel, kraft paper, pressboard, varnish | [Polymers](../polymers/index.md) | Mica, glass fiber |
| [Cooling fan](../metals/iron-steel.md) | 1 piece | Aluminum or steel, mounted on shaft | [Casting](../machine-tools/casting.md) | Fabricated |

## Construction Steps

### DC Motor

1. **Fabricate the armature core** by stacking silicon steel laminations on the shaft with keyway alignment. Clamp with end plates. Each lamination has slots for winding conductors.

2. **Wind the armature coils** into the slots. Calculate turns per coil based on the back-EMF equation: E = V - I_a × R_a - brush_drop. Each coil is wound into two slots approximately one pole pitch apart. Insulate slots with kraft paper before winding. Secure with fiber wedges.

3. **Connect coil leads to commutator segments** in sequence. Solder all joints. The commutator assembly must be concentric with the shaft within 0.02 mm to prevent brush bouncing at speed.

4. **Wind the field poles** on laminated pole pieces mounted inside the frame. For a shunt motor, the field winding has many turns of fine wire (high resistance, low current). For a series motor, fewer turns of thick wire (low resistance, high current). For compound: both windings on each pole.

5. **Assemble the motor**: Install the armature in the frame with bearings. Adjust the air gap between armature and field poles to 0.5-1.5 mm uniformly. Mount brush holders with carbon brushes positioned at the geometric neutral plane (where armature coils have zero EMF).

6. **Set brush position** for sparkless commutation. Shift the brush holder slightly in the direction of rotation until sparking is minimized under load. Lock the position.

### AC Induction Motor

7. **Fabricate the stator core** by stacking laminations with internal slots in a steel frame. The frame has cooling fins cast integrally for surface cooling. Clamp laminations with end rings and through-bolts.

8. **Wind the stator** with three-phase distributed windings. Each phase occupies approximately one-third of the total slots. Use double-layer winding (two coil sides per slot) with 120° electrical displacement between phases. Insulate between phases and between layers.

9. **Connect the windings** in star (wye) configuration for 400V operation, or delta for 230V. Bring six leads out (three phase starts, three phase ends) to a terminal box, allowing field conversion between star and delta. Star-delta starting uses delta for running and star for reduced-voltage starting.

10. **Fabricate the rotor core** from silicon steel laminations with external slots (semi-closed or closed). Stack on the shaft with keyway.

11. **Cast aluminum rotor bars** using die-casting or centrifugal casting: heat the stacked rotor laminatures to 400-500°C, inject molten aluminum (660°C) into the rotor slots under pressure. The aluminum fills the slots and forms end rings at both ends simultaneously, creating the squirrel-cage winding. This is a single short-circuited winding — no external connections needed.

12. **Turn the rotor OD** on a lathe to achieve the designed air gap: 0.3-0.8 mm between rotor surface and stator bore. Surface finish: Ra 1.6 μm. The air gap must be uniform around the entire circumference.

13. **Assemble the motor**: Install the rotor in the stator frame with bearings at both ends. Mount the cooling fan on the non-drive end of the shaft. Install end shields (bearing housings) and verify rotor spins freely.

14. **Varnish-impregnate the stator** by dipping the wound stator in insulating varnish, draining excess, and baking at 130-150°C for 4-6 hours. This locks windings in place and improves heat transfer and moisture resistance.

## Calibration and Verification

1. **Insulation resistance**: Megger between windings and frame at 500V DC. Minimum: 20 MΩ cold. Below 5 MΩ — do not energize (moisture or insulation damage).

2. **No-load test**: Apply rated voltage, run unloaded. Measure current (no-load current should be 25-40% of rated current for induction motors), speed (should be close to synchronous speed with minimal slip), and input power (core loss + friction and windage).

3. **Locked-rotor test** (induction motor): Lock the rotor, apply reduced voltage (25-40% of rated), measure current and torque. This determines starting torque and starting current. Starting current is typically 4-8× rated current for direct-on-line starting.

4. **Load test**: Run at rated load for 2 hours. Monitor winding temperature (by resistance or embedded thermocouple). Temperature rise must not exceed insulation class limit: Class B = 80°C rise, Class F = 105°C rise, Class H = 125°C rise.

5. **Vibration check**: Measure vibration at each bearing housing. Acceptable: <2.5 mm/s RMS for 1500 RPM motors. Excessive vibration indicates rotor imbalance, misalignment, or bearing defect.

## Expected Performance

### DC Motor

| Parameter | Value |
|-----------|-------|
| Power range | 0.1-500 kW |
| Speed range | 100-3000 RPM (adjustable by voltage or field control) |
| Efficiency | 80-92% (larger units higher) |
| Starting torque (series) | 3-5× rated torque |
| Starting torque (shunt) | 1.5-2.5× rated torque |
| Speed regulation (shunt) | 5-10% no-load to full-load |
| Speed control range | 10:1 by armature voltage, 4:1 by field weakening |
| Brush life | 2,000-10,000 hours |

### AC Induction Motor

| Parameter | Value |
|-----------|-------|
| Power range | 0.1-50,000+ kW |
| Speed (4-pole, 50 Hz) | 1440-1470 RPM (synchronous: 1500 RPM) |
| Slip at full load | 2-5% |
| Efficiency | 85-96% (larger units higher) |
| Starting current | 4-8× rated current (direct-on-line) |
| Starting torque | 1.5-2.5× rated torque |
| Power factor at full load | 0.80-0.90 |
| Service life (bearings) | 20,000-100,000 hours |

## Strengths

- **DC motors**: Excellent speed control over wide range, high starting torque (series type), simple speed regulation by varying armature voltage
- **AC induction motors**: No commutator or brushes (zero maintenance on rotor), robust and reliable, lowest cost per kW of any motor type, inherently explosion-proof (no sparking parts)

## Weaknesses

- **DC motors**: Commutator and brushes wear out (2,000-10,000 hour brush life), sparking limits use in hazardous atmospheres, maintenance-intensive compared to induction motors
- **AC induction motors**: Poor speed control without variable-frequency drive, low starting torque relative to starting current, draws reactive power (low power factor when lightly loaded), fixed speed determined by supply frequency and pole count

## Safety

- **Electrical**: Motor terminals carry lethal voltage. Ground the motor frame. De-energize and lock out before servicing.
- **Rotating parts**: Guard couplings, belts, and pulleys. Entanglement with rotating shafts causes severe injury.
- **Thermal**: Overloaded motors overheat, damaging insulation and potentially igniting nearby combustible materials. Install overload relays on all motor circuits.
- **Starting current**: Large induction motors draw 4-8× rated current on direct-on-line start. Use star-delta or auto-transformer starters for motors >15 kW to reduce starting current and mechanical shock.

## See Also

- [Electricity Generation](electricity.md) — power supply for motors, wire drawing, electrical fundamentals
- [Generator](generator.md) — reverse conversion (mechanical to electrical)
- [Transformer & Power Distribution](power-distribution.md) — power supply and motor protection
- [Machine Tools](../machine-tools/machining.md) — precision machining of shafts and housings
- [Bearings & Abrasives](../machine-tools/bearings-abrasives.md) — bearing selection and lubrication

---

*Part of the [Bootciv Tech Tree](../index.md) · [Energy](./index.md) · [All Domains](../index.md)*
