# Power Electronics

> **Node ID**: electronics.power-electronics
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md), [`electronics.electrical-systems`](electrical-systems.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`energy.photovoltaics`](../energy/index.md), [`automation`](../automation/index.md), [`machine-tools.cnc`](../machine-tools/edm-cnc.md)
> **Timeline**: Years 35-60
> **Outputs**: rectifiers, inverters, converters, motor_drives, ups_systems
> **Critical**: Yes — power electronics enables efficient energy conversion, motor control, and solar/grid integration without which industrial electrification is impossible


Power electronics is the technology of converting and controlling electrical power using semiconductor switching devices. It encompasses rectifiers (AC→DC), inverters (DC→AC), DC-DC converters, and AC-AC converters. Every modern power system — from [solar inverters](../energy/index.md) to variable-frequency motor drives to welding machines to [computer power supplies](../computing/electronic.md) — relies on power electronics.

The core principle is high-frequency switching (1 kHz to 1 MHz) of semiconductor devices (diodes, MOSFETs, IGBTs, thyristors) to process power with 90-98% efficiency. By switching at frequencies far above the 50/60 Hz power line, the magnetic components (inductors, transformers) shrink dramatically — a 100 kHz transformer is 1/1000th the size of a 50 Hz transformer handling the same power.

Power electronics depends on [semiconductor devices](semiconductor-devices.md) (switches and diodes), [passive components](passive-components.md) (inductors, capacitors for energy storage and filtering), [PCB fabrication](pcb-fabrication.md) (high-current, thermally-managed circuit boards), and [electrical systems](electrical-systems.md) (power distribution). It enables efficient industrial automation, renewable energy integration, and virtually all modern power management.

## Prerequisites

## Materials
- **Power semiconductors**: Diodes, MOSFETs, IGBTs, thyristors (from [Semiconductor Devices](semiconductor-devices.md))
- **Magnetic cores**: Ferrite (MnZn, NiZn) for high-frequency transformers and inductors, iron powder or amorphous metal for high-power inductors
- **Magnet wire**: Copper wire (0.1-3.0 mm dia) with enamel insulation (polyurethane, polyester, or polyimide), rated 155-220°C
- **Capacitors**: Electrolytic (bulk energy storage, 100-10,000 μF), ceramic (decoupling, 0.01-10 μF), film (snubbers and filters, 0.01-100 μF)
- **PCB substrate**: FR-4 (standard) or aluminum-backed (high power), 2-4 oz copper (70-140 μm) for high-current traces
- **Thermal interface materials**: Thermal grease (1-5 W/m·K), mica or silicone pads, aluminum or copper heatsinks
- **Gate driver ICs**: Or discrete gate drive circuits using small-signal transistors and optocouplers

## Tools
- [Oscilloscope](../measurement/electrical-instruments.md) (100+ MHz, 2+ channels) for switching waveform analysis
- [Power analyzer](../measurement/electrical-instruments.md) for efficiency measurement (±0.1-0.5% accuracy)
- [LCR meter](../measurement/electrical-instruments.md) for inductor/capacitor characterization
- Thermal imaging camera or thermocouples for thermal validation
- [Electronics assembly](assembly.md) equipment (soldering, PCB fabrication)

## Knowledge
- PWM (pulse-width modulation) theory: duty cycle D = ton/(ton + toff), average output = D × input
- Switching loss analysis: Psw = ½ × V × I × (tr + tf) × fsw
- Magnetic design: volt-second balance, core selection (Ae, le, Bmax), copper loss (proximity effect, skin effect)
- Control theory: voltage-mode control, current-mode control, feedback loop stability (Bode plot, phase margin)
- Thermal design: junction-to-heatsink thermal resistance chain, forced vs. natural convection

## Bill of Materials

| Material | Quantity (per 1 kW DC-DC converter, 48V→12V) | Source | Alternatives |
|----------|---------------------------------------------|--------|-------------|
| Power MOSFETs (100V, 10 mΩ, TO-220) | 4 devices (full bridge) | [Semiconductor Devices](semiconductor-devices.md) | IGBT (higher voltage, slower switching) |
| Gate driver ICs (half-bridge) | 2 ICs | [Semiconductor Devices](semiconductor-devices.md) | Discrete gate drive (transistor + pulse transformer) |
| Ferrite core (ETD39, MnZn) | 1 core | [Passive Components](passive-components.md) | Iron powder core (higher loss, larger) |
| Magnet wire (0.5 mm, polyurethane) | 50-100 m | [Electrolysis](../chemistry/electrolysis.md) | — |
| Electrolytic capacitors (470 μF, 63V) | 4-6 pcs | [Passive Components](passive-components.md) | Film capacitors (longer life, larger) |
| Ceramic capacitors (1 μF, 100V, X7R) | 8-12 pcs | [Passive Components](passive-components.md) | — |
| PCB (4-layer, 2 oz Cu, 100×80 mm) | 1 board | [PCB Fabrication](pcb-fabrication.md) | Point-to-point wiring (prototyping only) |
| Aluminum heatsink (50×50×25 mm) | 1 piece | [Metals](../metals/index.md) | Copper (better thermal, heavier) |
| Thermal grease | 2-5 g | [Polymers](../polymers/index.md) | Thermal pad (higher Rth but cleaner) |
| Inductor core (iron powder, 33 μH) | 1 core | [Passive Components](passive-components.md) | Ferrite + gap (lower loss, tighter tolerance) |

## Process Description

## 4.1 Rectifiers (AC → DC)

#### Uncontrolled Rectifier (Diode Bridge)

1. **Single-phase full bridge**: 4 diodes in H-bridge configuration. AC input across left-right terminals. DC output across top-bottom terminals. Diodes conduct in pairs: D1+D3 for positive half-cycle, D2+D4 for negative half-cycle. Output: full-wave pulsating DC with 120 Hz ripple (from 60 Hz input).
2. **Filter**: Add capacitor (1000-10,000 μF per amp of load current) across DC output. Ripple voltage: ΔV = I_load / (2f × C). Example: 5A load, 4700 μF capacitor, 60 Hz: ΔV = 5/(2×60×0.0047) = 8.9V peak-to-peak on a 170V peak DC bus. Larger capacitor = lower ripple but higher peak diode current (capacitor charging spikes).
3. **Three-phase full bridge**: 6 diodes. Output ripple at 360 Hz (6× line frequency). Much lower ripple without filtering: 4.2% ripple factor vs. 48% for single-phase. Standard for industrial power above ~5 kW. Ripple: ΔV/Vdc ≈ 0.055/(f×C×Rload).

#### Controlled Rectifier (Thyristor Bridge)

Replace diodes with thyristors (SCRs). Control firing angle α (0-180°) to vary output voltage: Vdc = 1.35 × VLL × cos(α) for three-phase bridge. At α = 0°: full output (same as diode bridge). At α = 90°: zero average output. Above 90°: inverter mode (power flows from DC to AC — used in HVDC transmission). Disadvantages: draws reactive power from AC line (power factor = cos(α)), generates line harmonics (5th, 7th, 11th, 13th...). For industrial DC motor drives and electroplating power supplies.

**Strengths**:
- Diode bridge rectification provides the highest reliability of any power conversion topology — no active switches, no control circuitry, and MTBF >1,000,000 hours for a properly derated design
- Three-phase bridge achieves 95% efficiency with only 6 passive components (diodes) — lowest component count per watt of any power converter
- Thyristor-controlled rectifiers enable continuous output voltage adjustment from 0-100% without any switching losses (line-frequency commutation), making them ideal for high-power DC motor drives and electroplating

**Weaknesses**:
- Uncontrolled rectifiers cannot regulate output voltage — the DC bus voltage varies with AC line voltage (±10% typical utility tolerance), requiring downstream regulation for sensitive loads
- Rectifiers draw non-sinusoidal input current (flat-topped waveform with current peaks near voltage peaks), generating harmonics (5th, 7th, 11th) that distort the AC supply — IEEE 519 limits total harmonic distortion to 5% at the point of common coupling, often requiring input harmonic filters
- Thyristor rectifiers draw reactive power proportional to firing angle (power factor = cos(α)) — at half output voltage, power factor is only 0.5, requiring capacitor banks for correction

## 4.2 DC-DC Converters

#### Buck Converter (Step-Down)

Vout = D × Vin, where D = ton / Tswitch is the duty cycle (0-100%). Maximum Vout = Vin.

1. **Switch** (MOSFET) connects input to output through **inductor** during ton. Inductor current ramps up: ΔIL = (Vin - Vout) × ton / L.
2. **Diode** (freewheeling) provides current path for inductor during toff. Inductor current ramps down: ΔIL = Vout × toff / L.
3. **Capacitor** smooths output voltage. Ripple: ΔVout = ΔIL / (8 × fsw × C).
4. **Control loop**: Measure Vout with voltage divider. Compare to reference. Error amplifier drives PWM controller. Adjust D to regulate Vout.

**Design example** (12V input → 5V output at 5A, 100 kHz):
- D = 5/12 = 0.42 (42% duty cycle)
- Inductor: L = (Vin - Vout) × D / (ΔIL × fsw). Target ΔIL = 20-40% of Iout = 1.0-2.0A. L = (12-5) × 0.42 / (1.5 × 100,000) = 19.6 μH → use 22 μH.
- Capacitor: C = ΔIL / (8 × fsw × ΔVout). Target ΔVout < 50 mV. C = 1.5 / (8 × 100,000 × 0.05) = 37.5 μF → use 47 μF ceramic + 470 μF electrolytic.
- MOSFET: Id = 5A, Vds > 20V (2× Vin margin). Select 30V, 10 mΩ MOSFET. Conduction loss: 5² × 0.01 = 0.25W.
- Diode: Schottky (Vf = 0.3V, low loss) or use synchronous rectification (replace diode with MOSFET for <0.05V drop).

#### Boost Converter (Step-Up)

Vout = Vin / (1 - D). Output is always higher than input.

1. **Switch** (MOSFET) connects inductor to ground during ton. Inductor current ramps up.
2. **Switch opens**: inductor voltage reverses, adds to Vin, forces current through diode to output.
3. Output capacitor absorbs pulsating current.

**Design example** (12V input → 48V output at 2A, 100 kHz):
- D = 1 - Vin/Vout = 1 - 12/48 = 0.75
- MOSFET: Vds > 60V (1.25× Vout). Select 100V, 20 mΩ. Id_peak = Iout/(1-D) + ΔIL/2 = 2/0.25 + 0.5 = 8.5A.

#### Buck-Boost and SEPIC

Buck-boost: inverting output (negative voltage). Vout = -D × Vin / (1 - D). Used for negative supplies. SEPIC (Single-Ended Primary-Inductor Converter): non-inverting buck-boost. Vout = D × Vin / (1 - D). Can step up or down. Requires two inductors and a coupling capacitor.

#### Forward and Flyback (Isolated Converters)

- **Flyback**: Single switch + coupled inductor (transformer). Output isolated from input. Power: 1-200W. Used in chargers, small power supplies. Flyback transformer stores energy in air gap (not a true transformer — operates as a coupled inductor). Peak flux density: Bmax = Vin × ton / (Np × Ae). Design to avoid core saturation.
- **Forward**: Single switch + true transformer + output inductor + reset winding. Power: 50-500W. Lower output ripple than flyback. Reset mechanism (tertiary winding or RCD clamp) resets transformer core each cycle.
- **Half-bridge, full-bridge, push-pull**: Higher power (200W to 10 kW+). Full bridge: 4 switches, highest utilization of transformer core. Used in server power supplies, EV chargers, welding machines.

**Strengths**:
- Buck and boost converters achieve 90-97% efficiency with only 1 active switch, 1 diode, 1 inductor, and 1 capacitor — the simplest possible power conversion topology
- High-frequency operation (50-500 kHz) shrinks inductors and capacitors by 100-1000× compared to 50/60 Hz designs — a 100 kHz, 100W buck converter inductor is <5 cm³ vs. >500 cm³ at 60 Hz
- Wide input-to-output ratio capability: boost converters can step up 12V to 400V (33:1) and buck-boost/SEPIC can handle input voltages both above and below the output

**Weaknesses**:
- Non-isolated topologies (buck, boost, SEPIC) provide no galvanic isolation between input and output — a single component failure can connect mains voltage directly to the load
- Flyback converters (the simplest isolated topology) store all energy in the transformer air gap during each cycle, limiting practical power to ~200W — above this, forward or bridge topologies are required with increased component count
- All DC-DC converters generate conducted and radiated EMI from high di/dt and dv/dt switching — compliance with FCC Part 15 or CISPR 32 requires input EMI filters that add 10-20% to converter cost and volume

## 4.3 Inverters (DC → AC)

#### Single-Phase H-Bridge Inverter

1. **Topology**: 4 switches (MOSFETs or IGBTs) in H-bridge. DC bus across top-bottom. AC output across left-right. Diagonally opposite switches turn on in pairs: S1+S4 for positive output, S2+S3 for negative output.
2. **PWM generation**: Compare sinusoidal reference (50/60 Hz) with triangular carrier (5-20 kHz). When reference > carrier: S1+S4 on. When reference < carrier: S2+S3 on. Duty cycle varies sinusoidally.
3. **Output filter**: LC low-pass filter removes switching harmonics. Cutoff frequency: fc = 1/(2π√(LC)), set between 1-5 kHz (well below switching frequency, well above output frequency). Typical: L = 1-10 mH, C = 1-20 μF.
4. **Dead time**: Insert 0.5-2.0 μs delay between turning off one switch and turning on its complement. Prevents shoot-through (both switches in one leg on simultaneously = DC bus short circuit through switches).

**Design example** (48V DC → 120V AC, 60 Hz, 2 kW, 20 kHz switching):
- Transformer: step up 48V to 170V peak (120V RMS). Ferrite core (ETD49 or larger). Primary: 10-20 turns. Secondary: 35-70 turns. Operating flux density: 0.15-0.25 T at 20 kHz (ferrite saturates at 0.3-0.5 T; stay below 0.25 T to limit core loss).
- MOSFETs: 100V, 5-10 mΩ (for 48V bus). Peak current: 2000W / 48V / 0.8 (efficiency) ≈ 52A. Use 2-3 MOSFETs in parallel per switch position.
- Output filter: L = 2 mH (20 turns on ferrite toroid), C = 10 μF (film). fc = 1/(2π√(0.002 × 0.000010)) = 1.1 kHz.

#### Three-Phase Inverter

6 switches (3 half-bridge legs). Three PWM outputs, 120° phase-shifted sinusoidal references. Standard for motor drives above ~1 kW. Output: three-phase AC, 0-400 Hz (for motor speed control) or 50/60 Hz (for grid-tie). Space vector modulation (SVM) provides 15% better DC bus utilization than sinusoidal PWM.

**Strengths**:
- PWM synthesis produces clean sinusoidal AC output (THD <3%) with an LC filter orders of magnitude smaller than a 50/60 Hz transformer — the entire inverter stage for a 5 kW system fits in <2 L volume
- Three-phase inverter with space vector modulation achieves 15% higher output voltage from the same DC bus compared to sinusoidal PWM — reduces DC bus capacitor requirements proportionally
- Bidirectional power flow capability: the same inverter hardware can operate as a rectifier (AC→DC) by reversing the PWM control — essential for regenerative braking in motor drives

**Weaknesses**:
- Dead time between complementary switches (0.5-2.0 μs) causes output voltage distortion proportional to switching frequency — at 20 kHz with 1 μs dead time, distortion is 2% of the output period, introducing low-order harmonics (5th, 7th) that are difficult to filter
- Shoot-through fault (both switches in one leg conducting simultaneously) creates a DC bus short circuit that destroys both switches in microseconds — requires careful gate drive timing and fast overcurrent protection (desaturation detection for IGBTs, current-sense comparator for MOSFETs)
- Output LC filter resonant frequency must be carefully placed between the output frequency (50/60 Hz) and switching frequency (5-20 kHz) — too low degrades transient response, too high allows switching harmonics into the load

## 4.4 Motor Drives (VFD — Variable Frequency Drive)

1. **Rectifier stage**: Three-phase diode bridge converts AC line to DC. 575V DC bus for 480V AC input.
2. **DC bus**: Capacitor bank (1000-10,000 μF) smooths DC ripple. Bus voltage: 300V (240V input), 575V (480V input), 1150V (960V input).
3. **Inverter stage**: Six IGBTs (for 480V systems: 1200V rated) generate three-phase PWM output at 0-400 Hz. Carrier frequency: 2-16 kHz. Higher carrier = smoother motor current but higher switching losses (derate drive by 1-2% per kHz above 4 kHz).
4. **Control**: V/f (volts-per-hertz) for simple applications. Vector control (field-oriented control) for precision: measures motor current, transforms to rotating reference frame, independently controls torque and flux. Speed regulation: ±0.5% (V/f), ±0.01% (vector with encoder).

**Strengths**:
- Reduces motor energy consumption by 20-60% in variable-torque applications (pumps, fans) by matching motor speed to actual load demand instead of running at full speed with throttle or damper
- Soft-start capability limits motor inrush current to 1.5-2× rated (vs. 5-8× across-the-line starting) — reduces mechanical stress on couplings, bearings, and gearboxes, extending equipment life by 2-3×
- Vector control achieves ±0.01% speed regulation with encoder feedback — enables precision speed applications (paper mills, textile machines, CNC spindle drives) that are impossible with mechanical speed control

**Weaknesses**:
- VFD output PWM waveform (5-16 kHz carrier with 0-400 Hz modulation) causes motor winding insulation stress — standard motors rated for sinusoidal power experience 2-3× higher peak voltage at motor terminals from reflected wave phenomena on long cables (>30 m), requiring VFD-rated motors with reinforced insulation (NEMA MG1 Part 31)
- High carrier frequency increases switching losses by 1-2% per kHz above 4 kHz — a 16 kHz carrier reduces drive efficiency from 97% to ~85% and requires derating the drive output current by 15-20%
- VFDs generate common-mode voltage on the motor shaft, causing bearing current flow that produces electrical discharge machining (EDM) pits in bearing races — shaft grounding rings or insulated bearings are required for reliable long-term operation

## 4.5 UPS (Uninterruptible Power Supply)

Online (double-conversion) UPS topology:
1. Rectifier: AC input → DC bus (maintains battery charge)
2. Battery bank: VRLA lead-acid or lithium-ion (see [Energy Storage](../energy/storage.md))
3. Inverter: DC bus → AC output (continuous, zero transfer time)
4. Static bypass: If inverter fails, thyristor switch transfers load to utility AC in <4 ms

Efficiency: 90-95% (double conversion always active). Battery runtime: 5-30 minutes at full load (sized for orderly shutdown or generator start). Typical sizing: 1-500 kVA.

**Strengths**:
- Zero transfer time (0 ms) — the inverter is always supplying the load, so utility failure produces no output interruption, making double-conversion UPS suitable for life-safety systems and critical computing
- Continuous power conditioning: the rectifier-inverter chain isolates the load from all utility power quality issues (sags, surges, harmonics, frequency variations) — output is regenerated to ±1% voltage and ±0.5% frequency
- Static bypass provides redundant power path — if the inverter fails, a thyristor switch transfers the load to utility power in <4 ms, maintaining continuity while the inverter is repaired

**Weaknesses**:
- Double conversion topology processes power twice (AC→DC→AC), resulting in 5-10% continuous energy loss as heat — for a 500 kVA data center UPS, this wastes 25-50 kW continuously, requiring substantial cooling infrastructure
- Battery bank replacement every 3-5 years for VRLA lead-acid types is the largest lifecycle cost — battery replacement typically exceeds the original UPS purchase price over a 15-year system life
- Battery runtime is inherently limited (5-30 minutes at full load) — a UPS alone cannot sustain operation through extended outages and must be paired with a standby generator for continuous availability

## Quantitative Parameters

## Converter Topology Comparison

| Topology | Power Range | Efficiency | Isolation | Complexity | Typical Application |
|----------|------------|-----------|-----------|-----------|-------------------|
| Buck | 1W-10kW | 90-97% | No | Low | Point-of-load DC regulation |
| Boost | 1W-5kW | 90-96% | No | Low | LED drivers, power factor correction |
| Buck-boost | 1W-1kW | 85-95% | No | Low | Battery chargers (wide input range) |
| SEPIC | 1W-500W | 85-93% | No | Medium | Battery-powered systems |
| Flyback | 1-200W | 75-90% | Yes | Medium | Phone chargers, small adapters |
| Forward | 50-500W | 80-92% | Yes | Medium | Industrial power supplies |
| Half-bridge | 200W-2kW | 85-94% | Yes | High | ATX power supplies |
| Full-bridge | 500W-100kW | 90-97% | Yes | High | Server PSUs, EV chargers |
| Push-pull | 100W-5kW | 85-93% | Yes | Medium | DC-DC converters, telecom |
| Three-phase inverter | 1kW-10MW | 90-98% | Yes (if transformer) | High | Motor drives, grid-tie |

## Switching Device Selection

| Device | Voltage Range | Frequency Range | Switching Loss | Conduction Loss | Best For |
|--------|--------------|----------------|---------------|----------------|----------|
| MOSFET (Si) | 20-900V | 20-500 kHz | Low (fast) | Rds(on) × Id² | Low-voltage, high-frequency |
| IGBT | 600-6500V | 5-40 kHz | Medium (tail current) | Vce(sat) × Ic | Medium-high voltage, motor drives |
| Thyristor (SCR) | 200-10,000V | Line frequency | Negligible (self-commutating) | Vt × It | AC power control, HVDC |
| SiC MOSFET | 650-3300V | 50-250 kHz | Very low | Low (wide bandgap) | High-efficiency, high-voltage |
| GaN HEMT | 40-650V | 100-1000 kHz | Ultra-low | Very low | High-frequency, compact |

## Magnetic Component Design Parameters

| Core Material | Frequency Range | Bmax (at frequency) | Core Loss (mW/cm³) | Relative Cost |
|--------------|----------------|---------------------|-------------------|---------------|
| MnZn ferrite | 10-500 kHz | 0.2-0.35 T | 50-500 | 1× |
| NiZn ferrite | 500 kHz-100 MHz | 0.1-0.2 T | 100-1000 | 1.5× |
| Iron powder | 1-200 kHz | 1.0-1.5 T | 200-1000 | 0.5× |
| Amorphous metal | 10-200 kHz | 0.5-0.6 T | 30-200 | 3-5× |
| Nanocrystalline | 10-200 kHz | 0.8-1.0 T | 10-100 | 5-10× |
| Sendust (Fe-Si-Al) | 1-500 kHz | 0.5-0.8 T | 100-500 | 1-2× |

## Power Converter Efficiency by Power Level

| Power Level | Typical Efficiency | Key Losses | Dominant Loss Mechanism |
|-------------|-------------------|-----------|------------------------|
| 1-10W | 75-90% | Switching, control overhead | Fixed losses dominate |
| 10-100W | 85-93% | Core loss, diode Vf | Diode conduction |
| 100W-1kW | 90-96% | MOSFET Rds(on), core | Conduction loss |
| 1-10kW | 93-97% | Switching loss, magnetic | Switching + copper |
| 10-100kW | 95-98% | IGBT Vce(sat), transformer | Conduction + core |
| 100kW-10MW | 96-99% | Transformer, filter | Magnetic losses |

## Scaling Notes

## Power Level Scaling

- **1-100W**: Single MOSFET, PCB-mount inductors, electrolytic capacitors. Air cooling. Design time: hours. Cost: $2-20.
- **100W-10kW**: Multiple MOSFETs or IGBTs in parallel, custom-wound transformers on ferrite cores, forced-air cooled heatsinks. Design time: days to weeks. Cost: $20-500.
- **10-100kW**: IGBT modules (multi-chip), liquid-cooled heatsinks, laminated bus bars, LCL filters. Design time: weeks to months. Cost: $500-10,000.
- **100kW-10MW**: Series/parallel IGBT stacks or thyristor valves, oil-immersed transformers, water cooling, custom control systems. Design time: months to years. Cost: $10,000-1,000,000.

## Frequency Scaling

Higher switching frequency shrinks magnetic components but increases switching losses. Practical limits:
- Silicon MOSFETs: 20-500 kHz (above 500 kHz, switching losses dominate)
- IGBTs: 5-40 kHz (tail current limits switching speed)
- SiC MOSFETs: 50-250 kHz (10-50× lower switching loss than Si)
- GaN HEMTs: 100-1000 kHz (enables MHz-class converters for very compact designs)

## Integration Level

- **Discrete design**: Individual switches, gate drivers, magnetics on PCB. Maximum flexibility. Standard approach for 1W-100kW.
- **Power module**: Pre-packaged IGBT or MOSFET dies in single package with internal isolation. Reduced parasitic inductance. Easier thermal management. Common above 5 kW.
- **Power IC**: Controller + switches on one chip. Limited power (<50W). Highest integration. Used in POL (point-of-load) converters.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Output voltage out of regulation | Feedback loop unstable, reference drift | Check compensation network; verify voltage reference; measure loop gain/phase with network analyzer |
| Excessive MOSFET/IGBT heating | High switching loss, inadequate heatsinking, high Rds(on) | Reduce switching frequency; improve thermal interface; parallel devices; verify gate drive voltage is adequate |
| Audible noise (whining) from converter | Magnetics vibrating at switching frequency (magnetostriction) | Varnish-dip inductors/transformers; increase switching frequency above audible range (>20 kHz); secure core clamping |
| EMI fails conducted emissions test | High di/dt loops, inadequate input filtering | Add input EMI filter (common-mode choke + X/Y capacitors); minimize loop area of high-current paths; use snubbers across switches |
| MOSFET failure at turn-on | Shoot-through (both switches in half-bridge on simultaneously) | Increase dead time; verify gate drive timing; check for excessive miller capacitance coupling (add gate-source resistor) |
| Transformer saturation | Excessive volt-seconds, DC bias, inadequate core gap | Reduce maximum duty cycle; add current-mode control to limit peak current; increase core gap; verify reset mechanism works |
| Output ripple too high | Insufficient output capacitance, ESR too high | Add more capacitance; switch to low-ESR types (polymer electrolytic, ceramic); increase switching frequency |
| Inverter output has high THD | Dead time distortion, inadequate filter design | Compensate dead time in control algorithm; increase output filter LC values; use space vector modulation |
| Intermittent resets under load | Input voltage sagging below UVLO, ground bounce | Add input capacitance; verify PCB ground plane integrity; check input cable resistance; use remote voltage sensing |
| Capacitor lifetime short | High ripple current, excessive ambient temperature | Derate ripple current to <70% of rated; use higher-temperature rated capacitors (105°C vs. 85°C); improve airflow |

## Safety

- **High energy storage**: Power converters store energy in capacitors (½CV²) and inductors (½LI²). A 4700 μF capacitor charged to 400V stores 376 J — enough to cause severe burns, cardiac arrest, or arc flash. **Always discharge capacitors** through a bleeder resistor (100-1000 Ω, rated for peak power) before servicing. Wait 5× the RC time constant for full discharge. Never short charged capacitors with a screwdriver — the arc causes copper vapor and shrapnel.
- **High voltage**: Off-line converters (rectified mains: 170V DC for 120V AC, 340V DC for 240V AC) present lethal shock hazard. Creepage and clearance requirements: 3-6 mm for 240V mains. All high-voltage sections must be insulated and marked. Service personnel must use isolated tools and insulating mats. GFCI protection on test bench circuits.
- **High current**: Low-voltage, high-current converters (e.g., 12V at 100A = 1.2 kW) can cause severe burns from heated conductors and arc flash from short circuits. A short across a 12V, 100A supply can sustain an arc at >1000A peak. Use appropriately rated fuses or circuit breakers on every output. Wire gauge must match current: minimum 6 AWG for 100A.
- **Thermal hazards**: Power semiconductor heatsinks may reach 60-100°C during normal operation. MOSFET/IGBT junction temperatures operate at 100-150°C. Burns from contact with heatsinks or power resistors. Use warning labels. Enclose hot surfaces in vented covers.
- **Arc flash**: In high-voltage inverters (>480V), arc flash from short circuits can reach 20,000°C. Incident energy calculations per IEEE 1584 determine required PPE (arc-rated clothing, face shield, hearing protection). Arc flash boundary: distance where incident energy = 1.2 cal/cm².
- **Gate driver hazards**: High-side gate drivers float at the switch node voltage (0 to Vbus). Isolated gate drive circuits use optocouplers or pulse transformers to level-shift. Never probe high-side gate drive circuits with a grounded oscilloscope — use differential probes or isolated oscilloscope channels.
- **Inductor/transformer safety**: Magnetic components can generate high voltage spikes (V = L × dI/dt) during switching transients. A 1 mH inductor with 10A interrupted in 100 ns produces a 100 kV spike. Clamp inductive kicks with snubber circuits (RCD clamp: fast diode + resistor + capacitor) or TVS (transient voltage suppression) diodes.

## Quality Control

## Component-Level Tests
- **MOSFET/IGBT verification**: Measure Rds(on) or Vce(sat) at rated current. Verify breakdown voltage (ramp to Vds(max) or Vces(max), confirm leakage < datasheet limit). Gate threshold check: Vgs(th) within specified range.
- **Capacitor ESR**: Measure at switching frequency (100 kHz) with ESR meter. Compare to specification. ESR >2× initial value indicates degradation.
- **Inductor/transformer**: Measure inductance at operating frequency (LCR meter). Verify saturation current (increase DC bias until inductance drops 10%). Hipot test: 1500-3000V between primary and secondary (isolated converters) for 60 seconds.

## Board-Level Tests
- **Functional test**: Apply input power, verify output voltage, regulation, and ripple under no-load, half-load, and full-load conditions. Measure efficiency at each load point.
- **Dynamic response**: Step load from 10% to 90% and back. Measure voltage deviation and recovery time. Target: deviation <5% of Vout, recovery <500 μs.
- **Thermal validation**: Run at full load in worst-case ambient temperature (40-50°C). Measure semiconductor junction temperatures (thermocouple on case, calculate Tj = Tc + Pd × Rth(jc)). All Tj < rated maximum with 15-25°C margin.

## EMC (Electromagnetic Compatibility)
- **Conducted emissions**: Measure on AC input and DC output with LISN and spectrum analyzer (150 kHz to 30 MHz). Must meet IEC 61000-4-6 or FCC Part 15.
- **Radiated emissions**: Measure with antenna at 3-10 m distance (30 MHz to 1 GHz). Must meet CISPR 32 or FCC Part 15 Class A/B.
- **Immunity**: Surge (IEC 61000-4-5: 1-6 kV), EFT/burst (IEC 61000-4-4: 0.5-4 kV), ESD (IEC 61000-4-2: 4-8 kV contact, 8-15 kV air). Converter must operate correctly during and after these disturbances.

## Reliability Qualification
- **Thermal cycling**: -40°C to +125°C, 500-2000 cycles. Check for solder joint cracks, PCB delamination, wire bond failures.
- **HTOL (High Temperature Operating Life)**: 1000 hours at maximum rated Tj under full electrical stress.
- **HALT (Highly Accelerated Life Test)**: Temperature + vibration + electrical stress combined. Identify weak points.

## Variations and Alternatives

## Converter Topology Selection Guide

| Requirement | Recommended Topology | Key Advantage |
|-------------|---------------------|---------------|
| DC step-down, non-isolated | Buck | Simplest, highest efficiency for step-down |
| DC step-up, non-isolated | Boost | Simplest step-up |
| DC up or down, non-isolated | SEPIC or Cuk | Single switch, continuous input/output current |
| Low power, isolated | Flyback | Fewest components, lowest cost isolated converter |
| Medium power, isolated | Forward or push-pull | Lower output ripple than flyback |
| High power, isolated | Full-bridge | Highest power capability, best transformer utilization |
| Three-phase motor drive | Voltage-source inverter (VSI) | Industry standard for AC motor control |
| High-power grid-tie | Current-source inverter (CSI) or MMC | Natural short-circuit protection, scalable |
| Battery backup | Online UPS | Zero transfer time, continuous conditioning |
| Renewable grid-tie | Grid-tied inverter with MPPT | Maximum power point tracking, anti-islanding |

## Soft Switching Techniques

- **ZVS (Zero Voltage Switching)**: Switch turns on when Vds = 0V. Eliminates capacitive turn-on loss. Achieved with resonant or quasi-resonant topologies (LLC resonant converter, phase-shifted full bridge). Reduces switching loss by 50-90%. Enables higher frequency operation.
- **ZCS (Zero Current Switching)**: Switch turns off when Id = 0A. Eliminates inductive turn-off loss. Used with IGBTs (eliminates tail current loss). Less common with MOSFETs.
- **Trade-off**: Soft switching adds circuit complexity (resonant components, auxiliary switches) but dramatically reduces EMI and allows higher switching frequency → smaller magnetics. LLC resonant converters achieve 95-97% efficiency at 500W-5 kW with switching frequencies of 100-500 kHz.

## Control Methods

| Method | Implementation | Performance | Cost |
|--------|---------------|-------------|------|
| Voltage-mode PWM | Comparator + ramp generator | Moderate regulation, simple | Lowest |
| Current-mode PWM | Inner current loop + outer voltage loop | Better transient response, inherent current limiting | Low |
| Digital control (DSP/MCU) | ADC samples + firmware control loop | Most flexible, adaptive algorithms | Medium |
| Hysteresis (bang-bang) | Comparator with hysteresis band | Fastest response, variable frequency | Very low |
| Sliding mode | State-space control with discontinuous surface | Very robust, handles large perturbations | Medium |

## See Also

- **[Semiconductor Devices](semiconductor-devices.md)**: diodes, MOSFETs, IGBTs, and thyristors used as switching elements
- **[Passive Components](passive-components.md)**: inductors, capacitors, and transformers used in power converters
- **[Electrical Systems](electrical-systems.md)**: power distribution and motor fundamentals
- **[PCB Fabrication](pcb-fabrication.md)**: circuit boards for power electronics assemblies
- **[Electronics Assembly](assembly.md)**: soldering and packaging of power electronic assemblies
- **[Electricity Generation](../energy/electricity.md)**: generators that power converters interface with
- **[Photovoltaics](../energy/index.md)**: solar inverters that convert DC to grid-compatible AC
- **[Energy Storage](../energy/storage.md)**: battery systems that power electronics charge and discharge



[← Back to Electronics](index.md)
