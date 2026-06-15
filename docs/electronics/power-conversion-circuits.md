# Power Conversion Circuits

> **Node ID**: electronics.power-conversion-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](./semiconductor-devices.md)
> **Enables**: None
> **Timeline**: Years 30-50
> **Outputs**: inverter-circuit-design
> **Critical**: No — this is a design-pedagogy capability (circuit-analysis layer); the underlying device manufacturing and system-level drive/converter building are covered by the critical capabilities it depends on.

## Overview

This capability is the **design-pedagogy layer** for circuits that convert DC back into controlled AC and use that AC to drive motors and loads. It teaches the DC→AC inversion and variable-frequency drive chain that underpins modern motor control, renewable-energy grid injection, and uninterruptible power:

```
  Fixed DC ──▶ [ Inverter (H-bridge + SPWM) ] ──▶ [ Output Filter ] ──▶ Controlled AC ──▶ [ Motor / Load ]
              synthesizes AC waveform             reduces switching harmonics   V/f or vector controlled
```

The inverter is the core building block. An H-bridge of four switching devices (MOSFETs or IGBTs) chops the DC bus into a synthesized AC waveform via pulse-width modulation. Sinewave PWM (SPWM) compares a sinusoidal reference against a triangular carrier to produce a duty-cycle sequence whose average is a clean sine wave. Wrap an inverter in a rectifier front-end and a control loop, and you have a variable-frequency drive (VFD) — the device that made AC induction motors speed-controllable, replacing mechanical transmissions and DC motors across industry.

This capability is distinct from [power electronics](power-electronics.md), which owns system-level converter manufacturing. It is also distinct from [power supply circuits](power-supply-circuits.md), which owns AC→DC rectification and DC voltage regulation. Here we focus on DC→AC synthesis, DC→DC conversion at power levels (buck, boost, buck-boost beyond what a simple regulator IC provides), and the motor-drive chain.

## Prerequisites

### Materials

- **MOSFETs** — IRF510 (100 V, 5.6 A), IRF3205 (55 V, 75 A, 8 mΩ), or logic-level IRLZ44N (55 V, 47 A). From [semiconductor devices](semiconductor-devices.md).
- **IGBTs** — IRG4BC30KD (600 V, 15 A) for higher-voltage motor drives. Preferred over MOSFETs above 200 V due to lower conduction loss.
- **Freewheel diodes** — intrinsic body diode in MOSFETs, or external ultrafast recovery diodes (MUR820, 200 V, 8 A) for high-frequency inductive loads.
- **Gate drivers** — IR2110 (high-side + low-side driver, 500 V level shifting) for H-bridge operation above the ground rail.
- **DC-bus capacitors** — 470–2200 μF, 63–400 V electrolytics. From [passive components](passive-components.md).
- **Output-filter inductors** — 100–1000 μH at rated motor current, for dv/dt filtering.
- **Snubber RC** — 100 Ω + 10 nF across each switch to suppress voltage spikes.

### Tools and Equipment

- Dual-channel oscilloscope (≥100 MHz, high-voltage differential probe required for floating measurements on the H-bridge).
- Signal generator (for the PWM reference sine and triangle carrier).
- DC bench supply capable of the motor bus voltage (24–48 V for bench; 300–600 VDC for industrial).
- Isolation transformer for scope isolation when measuring off-ground points.

### Knowledge

- [Circuit fundamentals](circuit-fundamentals.md) — Lenz's law (V = −L·di/dt), the physics of inductive switching spikes.
- [Analog circuits](analog-circuits.md) — transistor switching, PWM generation, comparator circuits.
- [Power supply circuits](power-supply-circuits.md) — rectifier→filter→regulator chain that precedes the inverter in a VFD.

### Infrastructure

- High-current DC bus (24–48 V at 10–50 A for bench-scale motor testing).
- Motor dynamometer or brake (for VFD load testing).
- Fused, isolated AC mains access for full bridge-rectifier front ends.

## Bill of Materials

| Component | Quantity (per H-bridge inverter) | Source | Alternatives |
|-----------|--------------------------------|--------|--------------|
| IRF3205 N-channel MOSFET (55 V, 75 A, 8 mΩ) | 4 | [Semiconductor devices](semiconductor-devices.md) | IRLZ44N (logic level); IGBT for >200 V |
| IR2110 high/low-side gate driver (DIP-14) | 2 | [Semiconductor devices](semiconductor-devices.md) | IR2104 (single channel); bootstrap discrete |
| Freewheel diode (MUR820, 200 V, 8 A, ultrafast) | 4 | [Semiconductor devices](semiconductor-devices.md) | MOSFET body diode (slower recovery) |
| DC-bus capacitor 1000 μF, 63 V electrolytic | 1 | [Passive components](passive-components.md) | 2200 μF for higher ripple current |
| Bootstrap diode (UF4007, 1000 V, 1 A ultrafast) | 2 | [Semiconductor devices](semiconductor-devices.md) | MUR120 |
| Bootstrap capacitor 1 μF, 25 V ceramic | 2 | [Passive components](passive-components.md) | 2.2 μF for higher gate charge |
| Output-filter inductor 470 μH, 10 A saturation | 1 per phase | [Passive components](passive-components.md) | Custom-wound on powdered-iron toroid |
| Gate-drive resistor 10 Ω, ¼ W | 4 | [Passive components](passive-components.md) | 4.7 Ω for faster switching; 22 Ω for lower EMI |
| Snubber (100 Ω + 10 nF, 1 kV) | 4 (one per switch) | [Passive components](passive-components.md) | RC across drain-source |
| PWM controller (microcontroller with 3 PWM channels) | 1 | [Computing: embedded systems](../computing/embedded-systems.md) | Dedicated SPWM IC (SG3525) |

## Process Description

### Step 1: Build the H-Bridge

Wire four N-channel MOSFETs in an H configuration. The load (motor or filter+resistor) connects between the two half-bridges. The top-left (Q1) and bottom-right (Q4) switches close together for one polarity; the top-right (Q3) and bottom-left (Q2) close for the opposite polarity. The DC bus (+ and −) connects across the top rail.

**Critical**: Never turn on both switches in the same leg simultaneously (Q1+Q2 or Q3+Q4) — this shorts the DC bus through both MOSFETs ("shoot-through"), destroying them in microseconds. Insert **dead time** (typically 200–500 ns) between turning one switch off and the other on in the same leg.

### Step 2: Generate the PWM Signal

Use a microcontroller timer to generate two complementary PWM signals per leg (high-side and low-side), with dead time. The duty cycle is modulated by a sinusoidal reference compared against a triangular carrier: when sine > triangle, the high-side is on. Carrier frequency is 4–20 kHz for motor drives (audible hiss below 16 kHz), 50–200 kHz for small power converters.

### Step 3: High-Side Gate Drive

The high-side MOSFET gate must be driven ~10 V above its source, which floats up to V_bus when the switch is on. Use a bootstrap circuit: a diode (UF4007) charges a bootstrap capacitor (1 μF) from a 12–15 V supply when the low-side is on; when the high-side turns on, the bootstrap capacitor provides the gate voltage floating on the source. The IR2110 handles this level-shifting internally.

### Step 4: Output Filter

The raw SPWM waveform is a high-frequency pulse train whose average is the sine wave. An LC low-pass filter (L = 470 μH, C = 10 μF) at the output with cutoff f_c = 1/(2π√(LC)) ≈ 7 kHz passes the fundamental (50/60 Hz) while attenuating the 8–20 kHz switching components by >40 dB.

### Step 5: Closed-Loop Control (VFD)

For motor speed control, wrap the inverter in a V/f or field-oriented control (FOC) loop:
- **V/f control**: maintain the voltage-to-frequency ratio constant so motor flux stays nominal. At 60 Hz, apply full voltage; at 30 Hz, apply half voltage.
- **FOC (vector control)**: transform the three-phase currents into a rotating reference frame aligned with the rotor flux, then regulate torque and flux independently. Requires a position sensor (encoder or hall sensors) or sensorless estimation.

*(Deep article: [vfd-motor-control](power-conversion-circuits.vfd-motor-control.md))*

## Quantitative Parameters

### DC-DC Converter Topology Comparison

| Topology | V_out / V_in (ideal) | Duty cycle range | Efficiency (typical) | Best for |
|----------|---------------------|-----------------|---------------------|----------|
| Buck (step-down) | V_out = D · V_in | 0 < D < 1 | 85–95% | Reducing voltage; highest efficiency |
| Boost (step-up) | V_out = V_in / (1 − D) | 0 < D < 0.9 | 80–90% | Battery boost, PFC |
| Buck-boost | V_out = −D / (1 − D) · V_in | 0 < D < 0.9 | 75–88% | Output above or below input |
| Ćuk | V_out = −D / (1 − D) · V_in | 0 < D < 0.9 | 75–85% | Low-ripple inverted output |
| SEPIC | V_out = D / (1 − D) · V_in | 0 < D < 0.9 | 75–85% | Non-inverted buck-boost |
| Flyback (isolated) | V_out = (N_s/N_p) · D / (1 − D) | 0.1 < D < 0.5 | 70–85% | Isolated low-power (<100 W) |
| Forward (isolated) | V_out = (N_s/N_p) · D · V_in | 0 < D < 0.5 | 75–90% | Isolated, 100–500 W |

D = duty cycle (fraction of period the switch is on). Isolated converters use a transformer for galvanic isolation.

### Inverter and VFD Parameters

| Parameter | Low-voltage (24 V bus) | Industrial (560 V bus) | Notes |
|-----------|----------------------|----------------------|-------|
| Switching device | MOSFET (IRF3205, 55 V) | IGBT (IRG4PH50KD, 1200 V) | IGBT preferred >200 V; lower conduction loss |
| Switching frequency | 20–100 kHz | 2–16 kHz | Higher = smaller filter, more loss |
| Output power | 100 W – 2 kW | 5 – 500 kW | Bus capacitor scales with power |
| SPWM carrier frequency | 8–20 kHz (audible) | 2–8 kHz | Above 16 kHz is silent but increases switching loss |
| Dead time per switching event | 200–500 ns | 1–4 µs | Prevents shoot-through; too long causes distortion |
| Output efficiency (inverter alone) | 92–96% | 95–98% | Excludes motor; IGBTs more efficient at high voltage |
| VFD system efficiency (incl. motor) | 80–88% | 90–95% | Motor losses dominate at low speed |
| Output voltage THD (with filter) | 3–5% | 2–4% | IEEE 519 recommends <5% |
| DC-bus ripple | <5% of bus voltage | <3% of bus voltage | Set by bus capacitor sizing |

### Buck Converter Component Sizing

| Parameter | Formula | Example (12 V → 5 V, 2 A) |
|-----------|---------|--------------------------|
| Duty cycle | D = V_out / V_in | 5/12 = 0.417 |
| Inductor ripple current | ΔI_L = (V_in − V_out) · D / (f_sw · L) | (12−5)·0.417 / (100k · 100µH) = 0.29 A |
| Inductor value (target 30% ripple) | L = (V_in − V_out) · D / (0.3 · I_out · f_sw) | (7)(0.417)/(0.3·2·100k) = 49 µH → use 47 µH |
| Output capacitor | C ≥ ΔI_L / (8 · f_sw · ΔV_ripple) | 0.29 / (8 · 100k · 0.05) = 7.25 µF → use 22 µF low-ESR |
| Switch RMS current | ≈ I_out · √D | 2 · √0.417 = 1.29 A |
| Diode (sync: MOSFET) RMS current | ≈ I_out · √(1 − D) | 2 · √0.583 = 1.53 A |

## Scaling Notes

- **Bench scale**: 4× MOSFETs on a PCB or breadboard, 12–24 V bus, 1–5 A, driving a small DC motor or resistor load. Demonstrates H-bridge, PWM, and shoot-through risk safely.
- **Motor-drive scale (100 W – 5 kW)**: IGBT H-bridge on a heatsink, 300–600 VDC bus (from 3-phase rectifier), 2–8 kHz carrier. The VFD is the dominant industrial motor-drive architecture. A 2 kW VFD fits in a 15×10×5 cm enclosure.
- **Grid-tie scale (10 kW – 1 MW)**: three-phase inverter (6 switches) for solar/wind grid injection. Requires grid synchronization (PLL), anti-islanding protection, and compliance with IEEE 1547. System-level concern — crosses into [power electronics](power-electronics.md).
- **Bottleneck at scale**: switching losses (P_sw = ½ · V · I · f_sw · t_sw) rise with frequency and voltage. At 600 V and 10 kHz, each IGBT dissipates 10–30 W just from switching — requiring liquid cooling above ~50 kW.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| MOSFETs fail immediately (shorted drain-source) | Shoot-through (both switches in a leg on simultaneously) — dead time missing or too short | Increase dead time to 500 ns minimum; verify with oscilloscope (dual-channel across gate-source of both switches); check gate-drive timing |
| Output voltage lower than calculated | Switching device not fully enhanced (gate drive insufficient), or inductor saturating | Verify gate voltage ≥10 V above source for MOSFET; check inductor saturation current (must be > peak current with margin) |
| Excessive ringing/spikes on switch node (>1.5× V_bus) | Stray inductance in the DC bus + high di/dt during switching | Minimize bus loop area (use heavy bus bars or planes); add snubber (100 Ω + 10 nF) across each switch; use low-ESR bus capacitor close to the switches |
| Motor runs rough / noisy | Carrier frequency too low (<4 kHz, audible torque ripple), or V/f ratio incorrect | Increase carrier to 8–16 kHz; verify V/f profile (voltage scales linearly with frequency down to ~5 Hz) |
| Gate driver fails repeatedly | Bootstrap capacitor too small (high-side gate not driven fully), or negative voltage transient on COM pin | Increase bootstrap cap to 2.2 µF; add reverse-blocking diode; use driver with under-voltage lockout (UVLO) |
| Overheating of IGBTs under load | Conduction loss (V_CE(sat) · I) + switching loss exceeds heatsink capability | Compute total loss per IGBT; add forced air or liquid cooling; reduce switching frequency if conduction loss dominates |
| Inverter trips on ground fault | Insulation breakdown in motor cable or windings (common on VFD-fed motors due to dv/dt stress) | Add output dv/dt filter or sine-wave filter; use VFD-rated motor (enhanced insulation); check cable shield grounding |

## Safety

- **High-voltage DC bus**: A 560 VDC bus (from 3-phase rectified 400 VAC) is lethal. The bus capacitor stores 80 J at 560 V, 470 μF — fatal shock. Always discharge through a bleeder resistor (10 kΩ, 25 W) and verify with a DMM before touching.
- **Shoot-through destruction**: Turning on both MOSFETs in one leg simultaneously creates a dead short across the bus. At 100 A the failure is explosive (package ruptures, shrapnel). Verify dead time with a scope at low voltage before applying full bus.
- **dv/dt motor stress**: Fast-switching IGBTs (dv/dt > 5000 V/μs) stress motor winding insulation, causing premature failure. Use VFD-rated motors (enhanced turn insulation) or a dv/dt output filter.
- **Ground-fault currents**: In a grounded DC bus, a single ground fault in the motor cable causes high current. Use a ground-fault relay on VFDs above 30 kW.
- **Arc flash**: Industrial inverters at 480 VAC can sustain an arc flash with enough energy to cause severe burns at 1 m. Follow NFPA 70E PPE requirements (category 2 or higher) when working on energized equipment.

## Quality Control

### Acceptance Criteria

- Output waveform THD <5% (with filter) measured by power analyzer or FFT on oscilloscope.
- Efficiency within 2 percentage points of design target at rated load.
- No shoot-through events (monitor with scope across both gate-source signals in each leg — confirm dead time on every switching transition).
- DC-bus ripple <5% of bus voltage at rated output.
- Motor speed tracking error <1% of commanded speed (closed-loop VFD; verify with tachometer or encoder).

### Testing Methods

- No-load test: run inverter into a resistor at reduced bus voltage; verify waveform, dead time, and thermal.
- Locked-rotor test: lock the motor shaft; command rated current; verify current limit and thermal protection.
- Heat-run test: full rated load for 1 hour; monitor IGBT case temperature, bus capacitor temperature, and motor winding temperature.
- Dielectric test: 1500 VAC between input (AC mains) and frame for 1 minute (per IEC 61800-5-1).

## Variations and Alternatives

### Inverter Topology Comparison

| Topology | Switch count | Output | Application |
|----------|-------------|--------|-------------|
| Single-phase H-bridge | 4 | Bipolar DC or single-phase AC | Low-power drives, UPS, solar micro-inverters |
| Three-phase bridge | 6 | Three-phase AC | Industrial motor drives (>1 kW) |
| Multilevel (NPC, flying capacitor) | 8–24+ | Lower-harmonic AC | High-voltage (>1 kV), high-power (MW) drives |
| Matrix converter | 9 | Direct AC-AC (no DC bus) | Theoretical; eliminates DC-bus cap |

### Motor Control Strategy Comparison

| Strategy | Feedback needed | Complexity | Speed accuracy | Torque ripple |
|----------|----------------|-----------|---------------|--------------|
| V/f (scalar) | None | Low | ±2% | Moderate (at low speed) |
| V/f with feedback (closed-loop) | Tachometer/encoder | Medium | ±0.5% | Low |
| Field-oriented control (FOC) | Encoder or sensorless | High | ±0.1% | Very low |
| Direct torque control (DTC) | None (hysteresis) | Medium-high | ±0.5% | Low |

## References

- [Semiconductor devices](semiconductor-devices.md) — MOSFETs, IGBTs, freewheel diodes, gate-drive transistors.
- [Electrical systems](electrical-systems.md) — motor theory, transformers, mains interface (linked from drive articles).
- [Passive components](passive-components.md) — DC-bus electrolytics, snubber RC networks, output-filter inductors.
- [Power supply circuits](power-supply-circuits.md) — the rectifier→filter front-end of a VFD; DC voltage regulation.
- [Power electronics](power-electronics.md) — system-level converter and drive manufacturing.
- [Control circuits](control-circuits.md) — PID and closed-loop control theory used in V/f and FOC.
- Deep articles: [inverter-circuits](power-conversion-circuits.inverter-circuits.md), [vfd-motor-control](power-conversion-circuits.vfd-motor-control.md).

---
*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
