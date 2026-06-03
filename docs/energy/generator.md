# Generator (Electrical)

> **Node ID**: energy.electricity.generator
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.electricity`](electricity.md), [`machine-tools.machining`](../machine-tools/machining.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`energy.electric-furnaces`](electric-furnaces.md), [`energy.power-distribution`](power-distribution.md), all electrical capabilities
> **Timeline**: Years 15-25
> **Outputs**: electrical_power_DC, electrical_power_AC
> **Critical**: Yes — generators are the only practical way to convert mechanical energy (steam, water, wind, diesel) into electricity at industrial scale

## Principle

A generator converts mechanical rotation into electrical energy through electromagnetic induction (Faraday's law). When a conductor moves through a magnetic field, an electromotive force (EMF) is induced proportional to the rate of change of magnetic flux: E = -N × dΦ/dt, where N is the number of turns and Φ is the magnetic flux. In practice, a coil of wire (armature) rotates in a magnetic field produced by either permanent magnets (magneto) or electromagnets (dynamo/alternator).

The output voltage depends on: field strength (magnetic flux density B), number of armature turns (N), rotational speed (ω), and the area of the armature coil (A). For a simple generator: E_peak = N × B × A × ω. Doubling any one of these parameters doubles the output voltage. Current is determined by the load resistance: I = V/R. Power output: P = V × I × efficiency.

DC generators use a commutator (split copper ring with carbon brushes) to reverse the current direction each half-turn, producing pulsating DC. AC generators (alternators) use slip rings, producing alternating current. Three-phase alternators use three independent windings offset by 120° to produce three-phase AC power.

## Prerequisites

- [Copper wire](electricity.md) — drawn and insulated (enamel or shellac), 0.5-3.0 mm diameter
- [Iron or steel laminations](../metals/iron-steel.md) — for magnetic cores
- [Permanent magnets or electromagnet capability](electricity.md) — for field poles
- [Lathe and milling machine](../machine-tools/machining.md) — for shaft, bearings, commutator
- [Insulating materials](../polymers/thermoplastics.md) — shellac, varnish, kraft paper, pressboard

## Materials

### DC Generator (10 kW, 220V, 1500 RPM)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Copper magnet wire (armature)](electricity.md) | 8-15 kg | 0.8-1.5 mm diameter, enamel insulated | [Wire Drawing](electricity.md) | Aluminum wire (larger gauge needed, 60% conductivity) |
| [Copper magnet wire (field)](electricity.md) | 3-8 kg | 0.5-1.0 mm diameter, enamel insulated | [Wire Drawing](electricity.md) | — |
| [Silicon steel laminations](../metals/iron-steel.md) | 30-60 kg | 0.35-0.50 mm thick, 3% Si | [Iron & Steel](../metals/iron-steel.md) | Low-carbon steel laminations (higher core loss) |
| [Steel shaft](../metals/iron-steel.md) | 1 piece | 40-60 mm diameter × 300-500 mm, 1045 steel, turned | [Machining](../machine-tools/machining.md) | — |
| [Cast iron frame/yoke](../machine-tools/casting.md) | 1 piece | 200-300 mm diameter ring, 10-20 kg | [Foundry](../machine-tools/casting.md) | Fabricated steel frame |
| [Copper commutator segments](../metals/copper-bronze.md) | 20-40 segments | Hard-drawn copper, trapezoidal cross-section | [Wire Drawing](electricity.md) | — |
| [Carbon brushes](../chemistry/index.md) | 4-8 pieces | Carbon-graphite composite, 15-25 mm × 8-15 mm | [Chemistry](../chemistry/index.md) | Copper gauze brushes (higher wear, sparking) |
| [Bearings](../machine-tools/bearings-abrasives.md) | 2 pcs | Ball bearings, sealed, shaft diameter matched | [Machine Tools](../machine-tools/index.md) | Babbitt sleeve bearings |
| [Insulation materials](../polymers/thermoplastics.md) | 2-5 kg | Shellac, kraft paper, pressboard, cotton tape | [Polymers](../polymers/index.md) | Silk, mica |
| [Terminal block and hardware](../metals/index.md) | 2-5 kg | Brass terminals, steel bolts, mounting feet | [Metals](../metals/index.md) | — |

### AC Alternator (50 kVA, 400V three-phase, 1500 RPM)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Copper magnet wire (stator)](electricity.md) | 25-50 kg | 0.8-2.0 mm, enamel insulated, three-phase windings | [Wire Drawing](electricity.md) | Aluminum wire |
| [Copper magnet wire (rotor)](electricity.md) | 5-15 kg | 0.5-1.5 mm, field winding | [Wire Drawing](electricity.md) | — |
| [Silicon steel laminations](../metals/iron-steel.md) | 80-150 kg | 0.35-0.50 mm thick, stator and rotor cores | [Iron & Steel](../metals/iron-steel.md) | Low-carbon steel (50% higher core loss) |
| [Steel shaft](../metals/iron-steel.md) | 1 piece | 50-80 mm diameter × 400-600 mm, turned | [Machining](../machine-tools/machining.md) | — |
| [Slip rings](../metals/copper-bronze.md) | 2-3 pcs | Brass or copper, 40-80 mm diameter | [Foundry](../metals/index.md) | — |
| [Carbon brushes](../chemistry/index.md) | 4-6 pcs | Carbon-graphite, for slip rings | [Chemistry](../chemistry/index.md) | Copper gauze |
| [Bearings](../machine-tools/bearings-abrasives.md) | 2 pcs | Ball bearings, sealed | [Machine Tools](../machine-tools/index.md) | Sleeve bearings |
| [Cast iron frame](../machine-tools/casting.md) | 1 piece | 300-500 mm diameter, 30-50 kg | [Foundry](../machine-tools/casting.md) | Fabricated steel |
| [Insulation](../polymers/thermoplastics.md) | 5-10 kg | Shellac, kraft paper, pressboard, cotton tape, mica | [Polymers](../polymers/index.md) | — |

## Construction Steps

### Core Fabrication

1. **Stamp or cut laminations** from silicon steel sheet (0.35-0.50 mm thick) into the core shape. For a DC generator, the armature core is a cylinder with slots for windings; for an AC alternator, the stator core is a ring with internal slots. Tolerance: ±0.2 mm on slot dimensions.

2. **Deburr all edges** and apply insulating varnish (thin coat, bake at 150°C for 30 minutes). The insulation between laminations prevents eddy currents that would waste energy as heat.

3. **Stack laminations** on the shaft (rotor) or in the frame (stator), keyed to prevent rotation. Clamp tightly with end plates and through-bolts. The stack must be uniform — any loose laminations vibrate and generate noise and heat.

### Winding (DC Generator Armature)

4. **Calculate turns per coil** based on desired voltage. For a 220V DC generator at 1500 RPM with 4 poles: E = (p × Φ × Z × N) / (60 × a), where p = poles, Φ = flux per pole, Z = total conductors, N = RPM, a = parallel paths. Solve for Z and distribute across armature slots.

5. **Wind coils into armature slots** using a winding machine or by hand. Each coil spans from one slot to another approximately one pole pitch apart. Place insulation (kraft paper, 0.1 mm) in each slot before inserting wire. Secure coils in slots with wooden or fiber wedges.

6. **Connect coil ends to commutator segments** in sequence around the armature. Each commutator segment connects to the start of one coil and the end of the previous coil. Solder all connections using rosin-core solder. Verify continuity of each coil with a multimeter.

### Winding (AC Alternator Stator)

7. **Calculate turns per phase** for the target voltage. For 400V line-to-line three-phase at 50 Hz with 4 poles: V_phase = 231V. Turns per phase: N = V / (4.44 × f × Φ × k_w), where k_w is the winding factor (~0.9-0.95 for distributed windings).

8. **Wind three-phase coils** into the stator slots. The three phases (A, B, C) are distributed around the stator with 120° electrical displacement. Each phase consists of multiple coils connected in series. Use layer insulation (kraft paper) between top and bottom coil sides in the same slot.

9. **Connect the three phases** in either star (wye) or delta configuration. Star provides a neutral point and is standard for distribution. Bring out four terminals: three phase leads and one neutral. Insulate all connections with varnished cambric or heat-shrink tubing.

### Commutator or Slip Rings

10. **Build the commutator** (DC) from hard-drawn copper segments clamped between two steel V-rings with mica insulation between segments. The mica between segments must be undercut 1-1.5 mm below the copper surface to prevent carbon dust bridging adjacent segments. Turn the outside diameter true and concentric to the shaft within 0.02 mm.

11. **Mount slip rings** (AC) on the rotor shaft. Each ring is a brass or copper band, insulated from the shaft by mica or pressboard. The field winding leads connect to the slip rings. Surface finish: smooth, Ra 0.8 μm.

### Assembly

12. **Install the rotor in the frame** with bearings at both ends. Verify air gap between rotor and stator is uniform around the entire circumference — maximum variation: ±0.15 mm. A non-uniform air gap causes unbalanced magnetic pull, vibration, and noise.

13. **Mount the brush holders** with carbon brushes riding on the commutator (DC) or slip rings (AC). Brush pressure: 15-25 kPa (adjustable by spring tension). Brushes must be aligned with the commutator segments for spark-free commutation.

14. **Install the field poles** (electromagnets) inside the frame. Each pole is a laminated iron core with a copper coil wound around it. The field coils are connected in series for a self-excited shunt generator, or separately excited from an external DC source.

15. **Connect all wiring** — armature/rotor leads, field leads, brush leads — to the terminal block. Label all terminals clearly: A1/A2 (armature), F1/F2 (field), L1/L2/L3/N (three-phase AC). Check all connections with a multimeter for continuity and isolation.

16. **Varnish-impregnate the windings** by dipping or vacuum impregnation. Bake at 110-130°C for 4-8 hours. This solidifies the windings, improves heat transfer, and protects against moisture.

## Calibration and Verification

1. **Insulation resistance test**: Apply 500V DC (megger) between windings and frame, between armature and field, and between phases (AC). Minimum: 10 MΩ at room temperature. Below 1 MΩ indicates moisture or damaged insulation — do not energize.

2. **No-load test**: Drive the generator at rated speed with no electrical load. Measure output voltage. For a self-excited DC generator, the voltage should build up from residual magnetism. If it does not, flash the field with a battery (connect 12V DC to field terminals for 5 seconds).

3. **Voltage regulation test**: Apply load in steps (25%, 50%, 75%, 100% of rated current). Record voltage at each step. For a shunt DC generator: voltage drop from no-load to full-load should be <10%. For an AC alternator: voltage regulation should be <5% (without automatic voltage regulator).

4. **Temperature rise test**: Run at full rated load for 2-4 hours. Monitor winding temperature by resistance method: R_hot = R_cold × (1 + 0.004 × ΔT). Maximum temperature rise: 75°C for Class B insulation (130°C hot-spot limit).

5. **Phase balance test** (three-phase AC): Measure voltage and current on all three phases at rated load. Maximum imbalance: 2% between any two phases.

## Expected Performance

### DC Generator

| Parameter | Value |
|-----------|-------|
| Rated voltage | 110-440V DC (design-dependent) |
| Rated power | 1-500 kW |
| Speed | 750-3000 RPM |
| Efficiency | 80-92% (larger units more efficient) |
| Voltage regulation | 5-10% (shunt-wound), <2% (with regulator) |
| Copper loss at full load | 3-6% of rated output |
| Core loss (constant) | 1-3% of rated output |
| Friction and windage | 0.5-1.5% of rated output |

### AC Alternator

| Parameter | Value |
|-----------|-------|
| Rated voltage | 400V (line-to-line, three-phase) |
| Rated power | 10-50,000 kVA |
| Speed | 1500 RPM (50 Hz, 4-pole) or 3600 RPM (60 Hz, 2-pole) |
| Frequency | 50 or 60 Hz, determined by RPM and poles: f = (p/2) × (N/60) |
| Efficiency | 88-97% (larger units more efficient) |
| Voltage regulation | 3-5% (without AVR), <1% (with AVR) |
| Power factor | 0.8 lagging rated (adjustable with excitation) |
| Short-circuit ratio | 0.5-1.2 (determines stability) |

## Strengths

- Converts any mechanical power source (steam, water, wind, diesel, gas turbine) into electricity
- DC generators are mechanically identical to DC motors — a dynamo can run as a motor and vice versa
- AC alternators produce three-phase power directly, the standard for industrial distribution
- Self-excited generators require no external power source — they bootstrap from residual magnetism

## Weaknesses

- Commutator (DC) requires regular maintenance — brush wear, segment wear, sparking at high loads
- Efficiency limited by core losses (eddy currents, hysteresis) and copper losses (I²R heating)
- Large generators require precision manufacturing — laminated cores, balanced rotors, accurate windings
- Voltage regulation on basic generators is poor without electronic control

## Safety

- **Electrical shock**: Generator output at 220V+ is lethal. Ground the generator frame. De-energize before working on connections. Use insulated tools.
- **Rotating machinery**: Rotors at 1500-3600 RPM have enormous kinetic energy. Guard all rotating parts. Loose clothing, hair, or tools can be caught with fatal results.
- **Carbon dust**: Commutator brush wear produces conductive carbon dust that accumulates inside the generator. Clean regularly to prevent short circuits and fire.
- **Overheating**: Overloaded generators overheat windings, degrading insulation. Monitor winding temperature and never exceed rated current.

## See Also

- [Electricity Generation](electricity.md) — electrical fundamentals, wire drawing, and power systems
- [Electric Motor](electric-motor.md) — reverse of generators, converting electricity to mechanical power
- [Transformer & Power Distribution](power-distribution.md) — voltage transformation and grid distribution
- [Steam Turbines](steam-turbines.md) — prime mover for large alternators
- [Steam Engine](steam-engine.md) — prime mover for smaller generators
- [Water Turbines](water-turbines.md) — hydroelectric generation
- [Wind Power](wind.md) — wind-driven generation
- [Machine Tools](../machine-tools/machining.md) — precision machining of shafts and commutators

---

*Part of the [Bootciv Tech Tree](../index.md) · [Energy](./index.md) · [All Domains](../index.md)*
