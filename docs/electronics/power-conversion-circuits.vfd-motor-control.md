# VFD Motor Control

> **Node ID**: electronics.power-conversion-circuits.vfd-motor-control
> **Domain**: [Electronics](index.md)
> **Dependencies**: None (see body text for prerequisite circuit articles)
> **Enables**: None
> **Timeline**: Years 30-50
> **Outputs**: variable_frequency_drives, motor_speed_controllers
> **Critical**: No

A **variable-frequency drive** (VFD) is a power-electronic circuit that adjusts the speed and torque of an AC induction motor by synthesizing a three-phase AC waveform whose **frequency** and **voltage** are both controllable from zero up to the motor's nameplate rating. Fixed-speed motors — the default since Tesla and Dolivo-Dobrovolsky established the three-phase induction motor in the 1890s — run at whatever speed the 50/60 Hz line dictates, and any flow or pressure adjustment is done mechanically (throttles, dampers, valves, gears). A VFD eliminates that waste: it lets the motor turn only as fast as the load actually requires, recovering 20–60% of the energy in pumps, fans, and compressors.

This article covers the **circuit-level design pedagogy** of VFDs: the rectifier → DC bus → inverter signal chain, V/f scalar control (the constant volts-per-hertz law that keeps motor flux constant), vector/field-oriented control concepts, PWM carrier-frequency tradeoffs, and bearing-current mitigation. The boundary with the sibling [inverter-circuits](power-conversion-circuits.inverter-circuits.md) article is explicit: that article teaches the H-bridge switching circuit and SPWM modulation *in general*; this article teaches the **specific application** of that circuit to AC motor control — the V/f law, the 3φ topology, the control strategies, and the motor-side problems (bearing currents, insulation stress, cable reflections) that arise only when the load is a motor rather than a passive grid or appliance. The [power-electronics](power-electronics.md) capability owns system-level packaging, harmonic compliance, and industrial installation; the [electrical-systems](electrical-systems.md) capability owns the motor physics (rotating magnetic field, slip, torque production).

## Why Variable Speed Matters — the Affinity Laws

The economic case for VFDs rests on the **affinity laws** (also called the fan/pump laws), which describe how the power demand of a centrifugal load scales with motor speed:

```
   Flow  (Q)  ∝  speed (n)
   Head  (H)  ∝  speed² (n²)
   Power (P)  ∝  speed³ (n³)
```

The cubic law is the whole story. If a pump only needs to deliver 80% of its rated flow, the motor can turn at 80% speed — and the power it draws drops to (0.8)³ = **51%** of full speed. At 50% speed the draw is (0.5)³ = **12.5%**. Compare that to the throttle alternative: a fixed-speed motor running at 100% with a downstream valve pinched back to deliver 50% flow still draws ~85–95% of full power (the valve wastes the rest as turbulence and heat). The savings are enormous:

```
   Power
     ▲
 100 │ ─ ─ ─ ─●─ ─ ─ ─ ─ ─ ─     ← throttle (valve/damper) curve
     │          ╲
     │           ╲                  nearly flat: motor works
     │            ╲                 just as hard, valve eats
     │             ╲                the difference
     │              ╲
  50 │ ─ ─ ─ ─ ─ ─ ─●─ ─ ─ ─     ← VFD (affinity-law) curve
     │              ╱
     │            ╱                P ∝ n³: half speed = 12.5% power
     │          ╱
     │        ╱
     │      ╱
   0 └──────────────────────────▶ Motor speed (%)
     0%    25%   50%   75%   100%
```

At 70% speed the throttle system draws ~90% power; the VFD draws (0.7)³ = 34% — a **56-point** gap. Over a 6000-hour operating year at $0.12/kWh for a 50 kW pump, that gap is worth:

```
   (0.90 − 0.34) × 50 kW × 6000 h × $0.12/kWh = $20,160 / year
```

The VFD hardware typically pays for itself in 6–18 months. This single economic fact is why VFDs are now universal in HVAC, water/wastewater, and process industries. Variable-torque loads (centrifugal pumps, fans, blowers) get the cubic benefit; constant-torque loads (conveyors, hoists, positive-displacement pumps) see only linear savings (P ∝ n), but even there the soft-start and speed-matching benefits justify the drive.

A secondary benefit is **soft starting**. Across-the-line starting slams the motor with 5–8× rated current and 2–3× rated torque for the 1–10 seconds it takes to reach full speed — stressing windings, bearings, couplings, and the supply grid. A VFD ramps the frequency from zero, holding starting current to 1.5–2× rated and starting torque at the motor's rated value, extending mechanical and electrical equipment life by 2–3×.

## VFD Architecture — the Three-Stage Signal Chain

Every VFD follows the same three-stage signal chain: **rectifier** (AC line → DC), **DC bus** (energy storage / smoothing), and **inverter** (DC → variable AC to the motor). This is a **voltage-source inverter (VSI)** topology — the industry standard for motor drives up to ~1 MW.

```
   3-phase AC line        Rectifier              DC bus              Inverter              3-phase motor
   (480V, 60 Hz)          (diode bridge)         (capacitor bank)    (6× IGBT, PWM)        (induction)
        ┌─┐ ┌─┐ ┌─┐      ┌──────────┐           ┌────────────┐      ┌────────────┐        ┌─────┐
   L1 ──┤ ├─┤ ├─┤ ├─ ──▶ │ 6 diodes │ ── ▒▒▓▓ ─▶│  C_bus     │ ──▶ │ 6 IGBTs    │ ──PWM─▶│  M  │
   L2 ──┤ ├─┤ ├─┤ ├─ ──▶ │ (3φ full │   DC      │ 1000–10000 │  DC │ 3 half-    │  3φ    │  o  │
   L3 ──┤ ├─┤ ├─┤ ├─ ──▶ │  bridge) │   link    │ µF         │  link│ bridge legs│ 0–400  │  t  │
        └─┘ └─┘ └─┘      └──────────┘           └────────────┘      └────────────┘  Hz   └─────┘
                          fixed V_dc              smooths ripple     synthesizes       variable
                          (~650 V for             stores energy      variable-freq     speed +
                          480 V AC)               for regeneration   3-phase AC        torque
```

### Stage 1 — Rectifier (AC → DC)

The front end is a **three-phase diode bridge** — six diodes arranged so that at any instant the two diodes connecting the most-positive and most-negative line phases to the DC bus conduct. This is identical to the controlled and uncontrolled rectifiers taught in [power-electronics](power-electronics.md) §Rectifiers, but in VFDs the uncontrolled (diode) version dominates because the VFD does all its voltage/frequency control on the inverter side — the rectifier's only job is to produce a roughly constant DC voltage.

For a 480 V AC line-to-line input, the peak DC bus voltage is:

```
   V_dc(peak) = √2 × V_LL = √2 × 480 = 679 V
```

The average DC bus (after the capacitor bank smooths the 360 Hz ripple of a 6-pulse rectifier on 60 Hz) sits at:

```
   V_dc(avg) = 1.35 × V_LL = 1.35 × 480 = 648 V
```

The diodes see a peak inverse voltage (PIV) equal to the line-to-line peak = 679 V, so 1200 V-rated diodes (giving 1.8× margin) are standard for 480 V drives. Above ~500 kW, 12-pulse or 18-pulse rectifiers (multiple diode bridges fed by phase-shifting transformers) replace the 6-pulse bridge to reduce line-current harmonics — the subject of IEEE 519 compliance in [power-electronics](power-electronics.md).

Some VFDs use a **controlled rectifier** (thyristor bridge) to regulate the DC bus voltage directly, allowing a smaller DC bus capacitor and regeneration back to the line. But the added cost and the thyristor's reactive-power draw make this rare below ~100 kW; the diode-bridge + IGBT-inverter combination is the default.

### Stage 2 — DC Bus (Energy Storage)

The DC bus is a **large electrolytic capacitor bank** — typically 1000–10,000 µF sized at roughly 80–100 µF per ampere of rated output current. Its three jobs:

1. **Smooth the rectifier ripple.** A 6-pulse rectifier on 60 Hz produces 360 Hz ripple (6 pulses per cycle). The capacitor absorbs the peaks and fills the valleys. Ripple voltage: ΔV = I_load / (6 × f_line × C). Example: 100 A load, 4700 µF capacitor: ΔV = 100 / (6 × 60 × 0.0047) = 59 V peak-to-peak on a 648 V bus — about 9% ripple, typical.
2. **Source the inverter's high-frequency pulsed current.** The inverter draws current in sharp pulses at the PWM frequency (2–16 kHz). The line and rectifier cannot supply this fast-changing current (line inductance chokes it), so the capacitor must be local and low-inductance. Film capacitors (lower ESR, longer life) are sometimes paralleled with the electrolytics to handle the high-frequency ripple.
3. **Store regenerative energy.** When the motor decelerates a high-inertia load (a fan, a conveyor belt, an elevator), it acts as a generator, pumping energy back into the DC bus. The bus voltage rises. A **brake chopper** (a transistor + resistor) detects the overvoltage and dumps the energy as heat; large drives use a regenerative rectifier to feed it back to the line.

The bus voltage sets the maximum AC output the inverter can synthesize. With 648 V DC, a space-vector-modulated inverter can produce up to ~460 V AC line-to-line — exactly the motor's nameplate rating.

### Stage 3 — Inverter (DC → Variable AC)

The inverter is the heart of the VFD — and it is the circuit taught in detail in [inverter-circuits](power-conversion-circuits.inverter-circuits.md): three half-bridge legs (six switches total), each leg producing one phase of the motor's three-phase supply. The difference from a single-phase inverter is that the three legs' PWM references are **120° phase-shifted** sinusoids, and there is **no output LC filter** — the motor's own inductance does the filtering.

```
                          +V_dc (DC bus +, ~650 V)
                           │
            ┌──────────────┼──────────────┐
            │              │              │
          ┌─┴─┐          ┌─┴─┐          ┌─┴─┐
          │Q1 │          │Q3 │          │Q5 │    Upper IGBTs
          │   │          │   │          │   │    (1200 V, with
          └─┬─┘          └─┬─┘          └─┬─┘     anti-parallel
   phase A │       phase B │       phase C │     diodes)
            │              │              │
            ├──▶ Motor A   ├──▶ Motor B   ├──▶ Motor C
            │  terminal    │  terminal    │  terminal
            │              │              │
          ┌─┴─┐          ┌─┴─┐          ┌─┴─┐
          │Q4 │          │Q6 │          │Q2 │    Lower IGBTs
          │   │          │   │          │   │
          └─┬─┘          └─┬─┘          └─┬─┘
            │              │              │
            └──────────────┼──────────────┘
                           │
                          ───  (DC bus − / ground)

   PWM reference per phase (120° apart):
   A:  sin(ωt)
   B:  sin(ωt − 120°)
   C:  sin(ωt − 240°)
```

The six **IGBTs** (insulated-gate bipolar transistors) are the standard switch for 480 V motor drives: their 1200 V rating gives margin on the 650 V bus, and their ~2 V saturation drop (V_CE(sat)) gives acceptable conduction loss at the high currents motor drives handle. At lower voltages (240 V drives, servo drives) power MOSFETs dominate; at very high power (>500 kW) IGBT modules with multiple dies in parallel are used. Device selection is covered in [inverter-circuits](power-conversion-circuits.inverter-circuits.md) and [semiconductor-devices](semiconductor-devices.md).

The PWM carrier frequency (2–16 kHz) is compared against the three 120°-shifted sinusoidal references to generate the gate-drive signals, exactly as the single-phase SPWM technique in [inverter-circuits](power-conversion-circuits.inverter-circuits.md). The motor's winding inductance (typically 1–10 mH per phase) integrates the PWM pulses into a near-sinusoidal current — the motor "sees" a smooth sine wave even though the inverter output is a stream of ±V_dc pulses.

## V/f Scalar Control — the Constant Volts-Per-Hertz Law

The simplest and most common VFD control strategy is **V/f control** (volts per hertz, also called scalar control). The goal is to keep the motor's **magnetic flux** (Φ) constant as the frequency changes. Why does flux matter? An induction motor produces torque proportional to flux × rotor current, and the flux is set by the applied voltage and frequency:

```
   V_applied = 4.44 × N × f × Φ × k_w      (Faraday's law for the stator winding)
```

where N is turns per phase, f is frequency, Φ is air-gap flux, and k_w is the winding factor. Solving for flux:

```
   Φ  =  V_applied / (4.44 × N × f × k_w)  =  V / f  (up to the constant 4.44·N·k_w)
```

So **to hold flux constant, the voltage must rise and fall in proportion to the frequency**. The ratio V/f is kept at its nameplate value across the whole speed range:

```
   V/f  =  V_rated / f_rated  =  constant
```

### Worked V/f Example — 460 V / 60 Hz Motor at Various Speeds

A 460 V, 60 Hz, 4-pole induction motor (synchronous speed 1800 RPM at 60 Hz) has a nameplate V/f ratio:

```
   V/f  =  460 V / 60 Hz  =  7.67 V/Hz
```

To run this motor at different speeds, hold the 7.67 V/Hz ratio constant:

| Output frequency | Motor speed (sync) | Required voltage | V/f ratio | Result |
|------------------|--------------------|------------------|-----------|--------|
| 60 Hz | 1800 RPM | 460 V | 460/60 = 7.67 | Full speed, full torque |
| 45 Hz | 1350 RPM | 345 V | 345/45 = 7.67 | 75% speed, full torque |
| **30 Hz** | **900 RPM** | **230 V** | **230/30 = 7.67** | **50% speed, full torque** |
| 15 Hz | 450 RPM | 115 V | 115/15 = 7.67 | 25% speed, full torque |
| 5 Hz | 150 RPM | 38 V | 38/5 = 7.67 | Low speed, full torque (ideally) |

At 30 Hz the controller commands 230 V — exactly half the rated voltage, matching the half-frequency, keeping flux at its design value and torque at rated. The motor turns at 900 RPM and delivers its full rated torque. This is the whole point of a VFD: **full torque at any speed**, with power scaling linearly with speed (P = T × ω, torque constant, speed halved → power halved).

### Voltage Boost (Torque Compensation)

The V/f law breaks down at very low frequencies. At 5 Hz the formula demands 38 V, but the motor's **stator winding resistance** (R_s) drops a fixed voltage (I × R_s) that doesn't scale with frequency. At full load the resistive drop might be 15 V — nearly half of the commanded 38 V — so the air-gap voltage is only 38 − 15 = 23 V, and the flux collapses to 23/(4.44·N·5·k_w). The motor loses torque at low speed.

The fix is **voltage boost** (also called torque compensation or IR compensation): the controller adds a small voltage offset at low frequencies to compensate for the resistive drop:

```
   V_command = (V/f × f)  +  V_boost

   V_boost ≈ I_rated × R_s         (set during commissioning, typically 2–10 V)
```

```
   Voltage
     ▲
 460 │                            ●
     │                        ╱
     │                    ╱
     │                ╱                    ← ideal V/f (pure linear)
     │            ╱
 230 │        ●
     │     ╱
     │   ╱     ╲                     ← actual V/f with boost
     │ ●         ╲                     (boost dominates at low f)
     │   ╲         ╲
   0 └─────┬──────┬──────┬──────┬────▶ frequency
          0     15     30     45    60 Hz
```

The boost fades out as frequency rises (the resistive drop becomes a smaller fraction of the total voltage). Some VFDs use **sensorless vector control** at low speeds instead of a fixed boost — but that is the subject of the next section.

### Weakness of V/f Control

V/f control is **open-loop** (in its basic form): it commands a voltage and frequency and assumes the motor follows. It does not measure motor speed or correct for slip. This means:

- **Speed regulation is ±0.5–3%** of synchronous speed, depending on load. A pump might run at 5% slip at light load and 3% slip at full load — the V/f controller doesn't know the difference.
- **Low-speed torque is poor** without boost, and even with boost the slip-dependent flux variation limits low-speed performance.
- **No dynamic torque control** — the motor responds to load changes on its own mechanical time constant (hundreds of milliseconds), not actively.

For fans and pumps (variable-torque loads, no precision required), V/f is ideal — cheap, robust, and efficient. For applications needing precise speed or torque (paper mills, winders, CNC spindles, elevators, EV traction), vector control takes over.

## Vector / Field-Oriented Control (FOC)

**Field-oriented control** (FOC, also called vector control) was developed in the 1970s (Blaschke, Hasse) to give AC induction motors the same fast, independent torque and flux control that DC motors enjoy. The idea is mathematically elegant and the implementation is where most modern VFD complexity lives — so this section is a conceptual overview, not a full derivation.

### The d-q Frame Transformation

In a DC motor, torque and flux are **physically decoupled**: the field winding sets the flux (via field current), the armature winding sets the torque (via armature current), and the commutator keeps them orthogonal. The operator can control each independently. In an AC induction motor, the three stator currents together produce **both** flux and torque — they are mixed together in a single set of three sinusoids, and changing one changes both.

FOC solves this with a mathematical trick: it transforms the three measured phase currents (i_a, i_b, i_c — 120°-shifted sinusoids) into a **rotating reference frame** locked to the motor's rotor flux. The result is two **DC quantities**:

```
   3φ stator currents               Clarke transform              Park transform
   (ia, ib, ic)                     (3φ → 2φ stationary)          (2φ → rotating)
        │                                  │                              │
        ▼                                  ▼                              ▼
   ia = Im cos(ωt)               iα = ia                    id = flux current (DC)
   ib = Im cos(ωt − 120°)        iβ = (ia + 2ib)/√3          iq = torque current (DC)
   ic = Im cos(ωt − 240°)
                                                                   │
                                                                   ▼
                                            id controls flux   ◄── like DC motor field
                                            iq controls torque ◄── like DC motor armature
```

- **i_d (direct axis)**: aligned with the rotor flux. Controls the **flux** — analogous to the DC motor's field current.
- **i_q (quadrature axis)**: 90° ahead of the flux. Controls the **torque** — analogous to the DC motor's armature current.

Once the currents are in the d-q frame, each is regulated by its own PI controller. The torque command becomes a commanded i_q; the flux command becomes a commanded i_d. The controllers compute the needed voltage commands in the d-q frame, which are then inverse-transformed back to the three PWM references for the inverter.

### Why It Matters

```
   Torque
   response
      ▲
      │      │ ◄── FOC: torque settles in 1–5 ms
      │      │     (electrical time constant)
      │      │╱
      │     ╱
      │    ╱
      │   ╱
      │  ╱     ╲╲╲╲  ◄── V/f: torque settles in 200–500 ms
      │ ╱        ╲╲╲╲      (mechanical time constant)
      │╱            ╲╲╲╲
      └──────────────────────▶ time (ms)
      0     100    200   500
```

Because i_d and i_q are DC quantities (in the rotating frame), the PI controllers act on the **instantaneous** current error — torque responds in milliseconds (the electrical time constant), not the hundreds of milliseconds of a V/f drive's mechanical response. The benefits:

- **Speed regulation**: ±0.01% with an encoder (1000× better than V/f's ±0.5%).
- **Full torque at zero speed**: because the controller actively maintains flux (i_d) and torque (i_q) independently, the motor can hold a load stationary (e.g., an elevator hoist, a crane) — impossible with V/f.
- **Fast dynamic response**: essential for servo-grade applications (robotics, CNC, web tension control).

The cost is complexity: the Clarke and Park transforms require knowing the **rotor flux angle** at all times. With a shaft encoder this is direct; without one (sensorless FOC), the angle is **estimated** from the measured stator currents and voltage model — a task that fails at zero speed (no back-EMF to measure) and degrades at very low frequencies. Sensorless FOC works above ~1 Hz; below that, the drive needs an encoder or falls back to V/f mode.

The [electrical-systems](electrical-systems.md) capability covers the motor physics (slip, torque-speed curve, rotating field) that FOC manipulates; this article treats FOC as a control strategy applied to the inverter circuit.

## PWM Carrier Frequency — the Switching-Frequency Tradeoff

The **carrier frequency** (f_s, also called switching frequency) is the rate at which the inverter's IGBTs switch on and off to synthesize the PWM waveform. Typical range: **2–16 kHz**. This single parameter controls a web of tradeoffs — there is no "right" answer, only the best fit for the application.

### What Carrier Frequency Affects

```
   Higher carrier frequency ──▶
        ┌──────────────────────────────────────────────────────┐
        │ ✓ Smoother motor current (less ripple)              │ better
        │ ✓ Lower acoustic motor noise (above human hearing)  │ better
        │ ✓ Less motor heating (lower ripple loss)            │ better
        │ ─────────────────────────────────────────────────── │
        │ ✗ Higher switching loss (1–2% per kHz above 4 kHz)  │ worse
        │ ✗ More EMI (higher dV/dt at higher f)              │ worse
        │ ✗ More bearing currents (common-mode voltage)       │ worse
        │ ✗ Shorter drive life (IGBT thermal cycling)         │ worse
        │ ✗ Must derate drive output current                  │ worse
        └──────────────────────────────────────────────────────┘
```

**Switching loss** dominates the high-frequency penalty. Each switching event dissipates energy in the IGBT (E_on + E_off ≈ 1–5 mJ per event for a 1200 V IGBT at rated current). At 4 kHz with 6 IGBTs, that's 4 × 2 × 6 = 48,000 events/second — at 2 mJ each, 96 W of pure switching loss. At 16 kHz it's 384 W. The drive's efficiency drops from ~97% at 4 kHz to ~90–93% at 16 kHz, and the lost energy becomes heat that the IGBT heatsink must remove. Manufacturers specify a **current derating curve**: typically derate 1–2% of rated output current per kHz above 4 kHz — a 100 A drive at 16 kHz might be limited to 75–80 A.

**Acoustic noise** is the main reason to raise the carrier. At 2–4 kHz the PWM frequency is in the middle of the human hearing range, and the motor's magnetostriction (the iron core physically vibrates with the flux) produces a loud, irritating whine. Above ~8–10 kHz the whine moves to the top of the audible range and becomes much less noticeable; above 16–20 kHz it is ultrasonic and inaudible to humans (though pets and some animals can still hear it). HVAC and building installations favor 8–16 kHz for quietness; industrial machinery that is already loud tolerates 2–4 kHz for efficiency.

### Carrier-Frequency Tradeoff Table

| Carrier freq | Switching loss | Drive efficiency | Acoustic noise | EMI level | Bearing current | Motor heating | Typical application |
|-------------|---------------|-----------------|----------------|-----------|-----------------|--------------|---------------------|
| 2 kHz | Lowest | 97–98% | Loud whine (audible) | Low | Low | Slightly higher (ripple) | Heavy industry, loud environments |
| 4 kHz | Low (baseline) | 96–97% | Audible whine | Low–Medium | Low–Medium | Baseline | Industrial machinery (default) |
| 8 kHz | Medium | 94–96% | Faint, top of hearing | Medium | Medium | Low | HVAC fans, general purpose |
| 12 kHz | High | 92–94% | Near-inaudible | Medium–High | High | Low | Buildings, offices, quiet areas |
| 16 kHz | Very high | 90–92% | Ultrasonic (inaudible) | High | High | Lowest | Critical acoustic environments, hospitals |
| 16+ kHz | Extreme (derate required) | <90% (derated) | Inaudible | Very high | Very high | Lowest | Rare — only where silence is mandatory |

**Selecting the carrier**: start at 4 kHz (the efficiency sweet spot). Raise it only if acoustic noise complaints or motor ripple heating demand it. For long motor cables (>30 m), lower it — high carrier frequency worsens the cable-reflection voltage doubling that stresses motor insulation (see below). Modern drives let the carrier be changed in software during commissioning — no hardware change.

## Bearing Currents — the Hidden VFD Failure Mode

VFDs introduce a failure mode that fixed-speed motors never see: **bearing current damage**. It is the single most common cause of premature bearing failure in VFD-driven motors, often shortening bearing life from a theoretical 100,000+ hours to 10,000–20,000 hours.

### The Mechanism — Common-Mode Voltage

The inverter's PWM output is not a clean sine wave — it is a series of ±V_dc pulses. The three phases' pulses are not symmetric around zero; their **common-mode voltage** (the average of the three phase voltages) is a high-frequency square wave that jumps between 0 and ±V_dc/2 at every switching event:

```
   Phase voltages    V_A     V_B     V_C      Common-mode V_cm = (V_A + V_B + V_C)/3
   (relative to
   DC bus midpoint)
        ▲                          ▲
   +V/2 │ ┐ ┐ ┐ ┐ ┐              V_cm│     ┌──┐     ┌──┐     ┌──┐
        │ │ │ │ │ │                  │     │  │     │  │     │  │   (jumps between
        │ │ │ │ │ │                  │  ┌──┘  └────┘  └────┘  └─    +V/6, −V/6, ±V/2
        │ │ │ │ │ │                  │  │                          at every switching)
   ─────┼─┴─┴─┴─┴─┴────────────────  │──┴────────────────────────
        │ │ │ │ │ │                  │
   −V/2 │ ┘ ┘ ┘ ┘ ┘                  │
        └────────────────▶ time      └────────────────────────▶ time
```

This high-dV/dt common-mode voltage capacitively couples from the stator windings, through the motor's air gap, onto the **rotor** — charging the rotor to a voltage that the shaft and bearings must conduct to ground. If the bearings are the lowest-impedance path, the common-mode current flows through them.

### EDM (Electrical Discharge Machining) Damage

The bearing's rolling elements (balls or rollers) are separated from the races by a thin oil film (~0.1–1 µm). At low speed or with grease aging, this film can be insulating — the shaft voltage builds up until it exceeds the film's dielectric breakdown (~20–50 V), then **discharges** as a tiny arc (2–5 A for nanoseconds). Each discharge blasts a microscopic pit (~10–100 µm diameter) in the bearing race — the same process as EDM (electrical discharge machining), but unintentional.

```
   Shaft voltage builds up ──▶ oil film breaks down ──▶ arc discharge ──▶ pit in race
         (capacitive coupling)        (V_shaft > 20 V)      (EDM event)      (fluting)
                                                                               │
                                                                               ▼
                                                     thousands of pits merge into "fluting" —
                                                     washboard-pattern grooves in the race
                                                     that vibrate and destroy the bearing
```

The visible symptom is **fluting** — a washboard pattern of parallel grooves in the bearing races, audible as a growling noise and eventually causing mechanical bearing failure.

### Mitigation Techniques

| Technique | How it works | Effectiveness | Cost | When to use |
|-----------|-------------|--------------|------|-------------|
| **Insulated bearings** (ceramic-coated outer race, ceramic balls) | Breaks the conductive path through the bearing | High (blocks 95–99% of circulating current) | Medium ($50–200 per bearing) | Standard on all NEMA Premium VFD-rated motors |
| **Shaft grounding ring** (conductive microfiber brush riding on shaft) | Provides a low-impedance path to ground, bypassing the bearing | High (conducts current to frame before bearing sees it) | Low–Medium ($30–100) | Retrofit on existing motors; common OEM fitment |
| **Common-mode choke** (toroidal core around 3 output phases) | Adds impedance to the common-mode path, reducing common-mode current | Medium (50–70% reduction) | Medium ($50–150) | Long motor cables (>30 m); high-carrier-frequency drives |
| **Output dV/dt filter** (LC filter on inverter output) | Slows the voltage edges, reducing common-mode dV/dt | Medium–High (also protects motor insulation) | High ($100–500) | Long cables, old motors not rated for VFD |
| **Symmetric motor cable** (3 phases + ground in symmetric geometry) | Reduces common-mode coupling by canceling magnetic fields | Low–Medium | Low (cable selection) | All new installations — use 3-conductor + ground, not random |
| **Grounding the motor frame to the drive frame** | Lowers the ground-path impedance so common-mode current flows safely | Medium | Low (wire) | All installations — mandatory best practice |

The most cost-effective strategy for new VFD installations is **insulated bearings + shaft grounding ring + symmetric cable** — together they reduce bearing currents by 99%+ and eliminate EDM damage for the motor's mechanical lifetime. For retrofits on older motors, a shaft grounding ring kit can be field-installed without removing the motor.

### Insulation Stress and Cable Reflections

A related VFD-induced failure is **motor winding insulation breakdown** from the high-dV/dt PWM pulses, worsened by **transmission line effects** on long motor cables. When the PWM pulse (with rise time ~100–500 ns) travels down a cable longer than ~15–30 m, the cable behaves as a transmission line, and the pulse **reflects** off the motor's high-impedance end. The reflected wave adds to the incoming pulse, doubling the voltage at the motor terminals:

```
   Drive output                 Cable (L > 30 m)              Motor terminals
        │                                                     │
        │ ──▶ pulse 650 V ────────────────────────────────▶  │ pulse reaches motor
        │                                                     │ reflected back
        │                                                     │ incoming + reflected
        │                                                     │ = 2 × 650 = 1300 V !
        │                                                     │ (standard motor insulation
        │                                                     │  is only 1000 V peak)
```

A 650 V DC bus can produce **1300 V peak** at the motor terminals on a long cable — exceeding the 1000 V insulation rating of a standard motor. **NEMA MG1 Part 31** specifies that motors operated on VFDs must withstand 1600 V peaks; older motors (pre-1990s, or inverter-rated only above NEMA frame 449) often cannot. The fix is a **dV/dt filter** or **sine-wave filter** on the inverter output, or keeping cables short (<30 m), or using a motor with reinforced insulation (VFD-rated / inverter-duty).

## Parameter Table — VFD Design Space

| Parameter | Typical range | Typical value (480 V industrial) | Notes |
|-----------|--------------|----------------------------------|-------|
| Input voltage | 200–690 V AC, 3φ | 480 V AC, 3φ, 60 Hz | Matches standard industrial supply; 240 V for small drives |
| DC bus voltage | 300–1150 V DC | 650 V DC | √2 × V_LL(peak); sets max AC output |
| Output frequency | 0–400 Hz | 0–60 Hz (standard motor) | Above 60 Hz the motor enters constant-power region (torque drops) |
| Carrier (switching) frequency | 2–16 kHz | 4 kHz | Raise for quietness, lower for efficiency (see §Carrier Frequency) |
| Switching device | IGBT (600–1700 V) | 1200 V IGBT (6 devices) | MOSFET for <100 V drives; SiC IGBT/MOSFET for high-efficiency |
| Control method | V/f, sensorless vector, FOC with encoder | V/f for fans/pumps; sensorless vector for general | FOC with encoder for precision (±0.01% speed regulation) |
| Efficiency (drive only) | 95–98% | 97% at 4 kHz carrier | Drops 1–2% per kHz above 4 kHz (switching loss) |
| Efficiency (system, drive + motor) | 88–94% | 92% | Motor adds its own 2–6% loss |
| Input current harmonics (THD_I) | 30–90% (6-pulse) without filter | 35–45% THD_I | IEEE 519 requires <5% at point of common coupling → needs 12-pulse or active front end |
| Output voltage THD | <3% (at motor terminals) | <3% | Motor inductance does the filtering — no output LC filter needed |
| Power range | 0.37 kW – 10 MW | 0.37–500 kW (common) | Below 0.37 kW = single-phase; above 500 kW = medium-voltage (2300–4160 V) |
| Overload capacity | 110–150% for 60 s | 150% for 60 s | Sized to start the load without tripping |
| Speed regulation | ±0.5% (V/f) to ±0.01% (FOC + encoder) | ±0.5% (V/f) | Depends on control method |
| Braking | Resistor (standard) or regenerative (option) | Brake chopper + resistor | Regenerative for elevators, cranes, high-inertia loads |
| Motor cable length (max) | 30–300 m (unfiltered) | 100 m | Longer cables need dV/dt or sine-wave filter (see §Bearing Currents) |
| Voltage boost (IR comp) | 0–15 V | 3–8 V (commissioned) | Compensates stator resistance at low speed |
| V/f ratio | V_rated / f_rated | 460/60 = 7.67 V/Hz | Held constant for constant flux (see §V/f Control) |

## Boundary with Sibling Articles

This article owns the **VFD circuit design and application**: the three-stage signal chain, the V/f law, vector control concepts, carrier-frequency tradeoffs, and motor-side problems (bearing currents, insulation stress). The boundaries:

| This article (VFD application) | inverter-circuits.md (circuit design) |
|-------------------------------|--------------------------------------|
| 3φ inverter topology for motor drives | H-bridge topology, diagonal switching, single-phase SPWM |
| V/f scalar control, the constant-V/Hz law | Modulation index mₐ, V₁,rms = (mₐ × V_dc)/√2 |
| Vector/FOC control strategies | Dead-time calculation, MOSFET vs IGBT selection |
| Bearing currents, insulation stress, cable reflection | LC output filter design (f_c = √(f_o × f_s)) |
| VFD parameter table, commissioning | Square-wave inverter, Fourier, THD analysis |

| This article (VFD application) | power-electronics.md (system level) |
|-------------------------------|-------------------------------------|
| V/f law, vector control, carrier tradeoffs | VFD architecture summary + cross-link |
| Bearing current mitigation (design-level) | Industrial drive packaging, panel mounting |
| Motor-side failure modes (design-level) | Harmonic compliance, IEEE 519, 12-pulse rectifiers |
| Inverter-stage design | Rectifier + DC bus + inverter as system blocks |

| This article (VFD application) | electrical-systems.md (motor physics) |
|-------------------------------|--------------------------------------|
| How the inverter drives the motor | Induction motor construction, rotating field, slip |
| FOC transforms 3φ → d-q frame | Torque production, torque-speed curve, starting |
| Motor terminal voltage, insulation stress | Motor winding construction, insulation classes |

The boundary is: read this article to **design the VFD circuit and choose the control strategy**; read [inverter-circuits](power-conversion-circuits.inverter-circuits.md) for the underlying switching circuit theory; read [power-electronics](power-electronics.md) for system-level packaging and compliance; read [electrical-systems](electrical-systems.md) for the motor physics.

## Prerequisites

- **[Inverter Circuits](power-conversion-circuits.inverter-circuits.md)** — the H-bridge switching topology, SPWM modulation, dead-time, MOSFET vs IGBT selection, LC output filtering. A VFD's inverter stage is this circuit triplicated for three phases.
- **[Power Conversion Circuits](power-conversion-circuits.md)** — parent capability: DC→AC inversion, variable-frequency drive architecture, switching-device selection at the circuit level.
- **[Electrical Systems](electrical-systems.md)** — induction motor physics (rotating magnetic field, slip, torque-speed curve), three-phase power fundamentals, the load the VFD drives.
- **[Semiconductor Devices](semiconductor-devices.md)** — IGBT construction, V_CE(sat), gate charge, switching characteristics, anti-parallel diodes. The VFD's six switches are IGBTs.
- **[Passive Components](passive-components.md)** — DC bus capacitor selection (electrolytic for bulk, film for ripple), inductor cores for output filters and common-mode chokes.


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

## See Also

- **[Inverter Circuits](power-conversion-circuits.inverter-circuits.md)** — the circuit-level switching topology that the VFD's inverter stage is built from.
- **[Power Electronics](power-electronics.md)** — system-level power conversion: rectifiers, converters, UPS, switching device comparison, topology selection.
- **[Electrical Systems](electrical-systems.md)** — motor construction, three-phase power, the mechanical load the VFD controls.
- **[Semiconductor Devices](semiconductor-devices.md)** — IGBT and MOSFET physics, device parameters, wide-bandgap (SiC, GaN) devices for next-generation drives.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
