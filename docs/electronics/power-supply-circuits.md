# Power Supply Circuits

> **Node ID**: electronics.power-supply-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](./semiconductor-devices.md), [`electronics.electrical-systems`](./electrical-systems.md)
> **Enables**: None
> **Timeline**: Years 20-40
> **Outputs**: regulated-dc-power
> **Critical**: No — this is a design-pedagogy capability (circuit-analysis layer); the underlying device manufacturing and system-level converter building are covered by the critical capabilities it depends on.

## Overview

This capability is the **design-pedagogy layer** for the circuits that convert raw AC mains or a coarse DC source into clean, regulated DC power. It teaches the canonical three-stage power-supply chain that every bench supply, battery charger, and embedded-system brick follows: rectifier → filter → regulator. The rectifier converts AC to pulsating DC; the filter smooths the pulsation into near-DC with residual ripple; the regulator holds the output constant against line and load variation.

```
 AC or raw DC ──▶ [ Rectifier ] ──▶ [ Filter ] ──▶ [ Regulator ] ──▶ Clean DC
 (uncontrolled)   AC → DC         reduce ripple   hold V_out fixed   (regulated)
```

The regulator stage splits into two families with sharply different trade-offs. **Linear regulators** (LM7805, LM317, LDOs) are simple, low-noise, and cheap, but dissipate all excess voltage as heat — efficiency is 30–50% for a 5 V output from 12 V input. **Switching regulators** (buck, boost, flyback) chop the input at 100 kHz–1 MHz and transfer energy through an inductor, achieving 85–95% efficiency but introducing switching noise that requires careful filtering.

This capability is distinct from [power electronics](power-electronics.md), which owns system-level converter manufacturing and deployment. When a design choice here becomes a system-integration concern (thermal management of a 1 kW supply, grid-tie compliance, motor-drive packaging), it crosses into power-electronics territory. The two capabilities cross-link rather than overlap. For DC-to-AC inversion and variable-frequency motor drives, see [power conversion circuits](power-conversion-circuits.md).

## Prerequisites

### Materials

- **Rectifier diodes** — 1N4001–1N4007 (1 A, 50–1000 V PIV) or 1N5400 series (3 A) from [semiconductor devices](semiconductor-devices.md). Bridge rectifier packages (KBP, W04M) integrate 4 diodes.
- **Filter capacitors** — electrolytic 470–4700 μF (25–63 V) for the reservoir; ceramic 100 nF for high-frequency bypass. From [passive components](passive-components.md).
- **Regulators** — LM7805 (5 V fixed), LM7812 (12 V fixed), LM317 (1.25–37 V adjustable); LM2576 (3 A buck switching); from [semiconductor devices](semiconductor-devices.md).
- **Inductors** — 47–330 μH, 2–5 A saturation, for switching regulators. From [passive components](passive-components.md).
- **Transformer** — 120/240 VAC to 6–24 VAC secondary, 0.5–5 A. From [electrical systems](electrical-systems.md).

### Tools and Equipment

- DC bench supply (for testing the regulator stage independently of the rectifier).
- Oscilloscope (≥20 MHz) for ripple measurement and switching waveform observation.
- DMM for DC voltage and current verification.
- AC variac (variable transformer) for testing rectifier stage at reduced mains voltage.

### Knowledge

- [Circuit fundamentals](circuit-fundamentals.md) — reactance (X_C = 1/2πfC), time constants (τ = RC), AC power (RMS).
- [Analog circuits](analog-circuits.md) — diode forward voltage (0.7 V silicon), zener reference operation, transistor pass-element behavior.
- Thermal design basics — junction temperature T_j = T_amb + P·θ_jA; heat sink selection.

### Infrastructure

- 120/240 VAC mains access with GFCI protection.
- Fusing on the primary side of any mains-connected supply (fast-blow, rated at 1.5× nominal primary current).

## Bill of Materials

| Component | Quantity (per bench supply built) | Source | Alternatives |
|-----------|--------------------------------|--------|--------------|
| Transformer 120V:12V, 1 A | 1 | [Electrical systems](electrical-systems.md) | 240V primary for international mains |
| Bridge rectifier (1 A, 50 V+, KBP/W04M package) | 1 | [Semiconductor devices](semiconductor-devices.md) | 4× 1N4001 diodes |
| Filter capacitor 2200 μF, 25 V electrolytic | 1 | [Passive components](passive-components.md) | 4700 μF for lower ripple |
| Bypass capacitor 100 nF ceramic | 2 | [Passive components](passive-components.md) | 1 μF for lower ESR |
| LM7805 regulator (5 V fixed, TO-220) | 1 | [Semiconductor devices](semiconductor-devices.md) | LM317 (adjustable); 7805 from other vendors |
| Heat sink (TO-220, ~10 °C/W) | 1 | [Electrical systems](electrical-systems.md) | Thermal pad + forced air |
| Input fuse (primary side, fast-blow, 0.5 A) | 1 | [Electrical systems](electrical-systems.md) | Resettable polyfuse (0.5 A hold) |
| Power switch and chassis (optional) | 1 | [Electrical systems](electrical-systems.md) | PCB-mounted switch |
| Output binding posts (red/black) | 1 pair | [Electrical systems](electrical-systems.md) | Terminal block |

## Process Description

### Step 1: Rectifier Stage

Connect a bridge rectifier to the transformer secondary. The bridge converts both half-cycles of AC to forward-polarity current, producing pulsating DC at 2× line frequency (100 Hz from 50 Hz mains, 120 Hz from 60 Hz). The peak output voltage is V_peak = V_secondary_rms × √2 − 2·V_diode ≈ 12·1.414 − 1.4 ≈ 15.6 V for a 12 VAC secondary. *(Deep article: [rectifier-circuits](power-supply-circuits.rectifier-circuits.md))*

### Step 2: Filter Stage

Add a reservoir capacitor across the rectifier output. The capacitor charges to V_peak on each peak and discharges into the load between peaks. Ripple voltage: V_ripple ≈ I_load / (f_ripple × C), where f_ripple = 2 × line frequency. With I_load = 0.5 A, C = 2200 μF, and f_ripple = 120 Hz: V_ripple ≈ 0.5 / (120 × 0.0022) ≈ 1.9 V peak-to-peak. Add a 100 nF ceramic in parallel to suppress high-frequency switching noise. *(Deep article: [filter-circuits](power-supply-circuits.filter-circuits.md))*

### Step 3: Linear Regulator Stage

Wire an LM7805 with input at the filter capacitor (V_in ≈ 13–16 V, including ripple) and output at 5.0 V. The regulator requires V_in ≥ V_out + dropout = 5 + 2 = 7 V minimum. The 2200 μF reservoir dips to ~13.6 V at ripple trough — well above dropout. Add 0.33 μF input and 0.1 μF output bypass capacitors per the datasheet to prevent oscillation. The regulator dissipates P = (V_in − V_out)·I_out = (14 − 5)·0.5 = 4.5 W as heat — requiring a heatsink.

### Step 4: Switching Regulator Alternative (Buck)

For higher efficiency, replace the LM7805 with an LM2576 buck converter. The LM2576 switches at 52 kHz, requires a 100 μH inductor (5 A saturation) and an output capacitor, and achieves 80–88% efficiency at 0.5 A load. The output ripple is higher than linear (20–50 mV vs <5 mV), governed by the inductor value and switching frequency. *(Deep article: [switching-regulators](power-supply-circuits.switching-regulators.md))*

### Step 5: Testing and Verification

Load the output with a power resistor sized for the rated current (R = V/I = 5 V/0.5 A = 10 Ω, 2.5 W). Measure output DC voltage with the DMM — must be within the regulator tolerance (LM7805: ±4%, i.e., 4.8–5.2 V). Measure ripple with the oscilloscope (AC-coupled) — target <50 mV peak-to-peak for linear, <100 mV for switching. Verify thermal stability: run at full load for 10 minutes; heatsink temperature should stabilize below 70 °C.

## Quantitative Parameters

### Linear vs Switching Regulator Comparison

| Parameter | Linear (LM7805) | Switching (LM2576 buck) |
|-----------|----------------|------------------------|
| Output voltage | 5.0 V ±4% | 5.0 V ±3% |
| Input voltage range | 7–25 V (dropout 2 V) | 7–40 V |
| Max output current | 1 A (with heatsink) | 3 A |
| Efficiency (5 V out, 12 V in, 0.5 A) | 42% | 85% |
| Power dissipation (0.5 A) | 3.5 W (as heat) | 0.5 W |
| Output ripple | <5 mV p-p | 20–50 mV p-p |
| Output noise | Very low (µRMS) | Higher (switching artifacts) |
| Switching frequency | N/A (linear) | 52 kHz |
| Transient response | ~1 µs | 50–100 µs |
| Component count | 3 (IC + 2 caps) | 8+ (IC + inductor + diode + caps) |
| Cost | Low ($0.30) | Moderate ($2.00) |
| Best use | Low-noise analog, precision, low current | High current, battery, efficiency-critical |

### Ripple and Filtering Calculations

| Capacitor (μF) | Line freq (Hz) | I_load (A) | Ripple V (p-p) | Notes |
|----------------|---------------|-----------|----------------|-------|
| 470 | 60 (full-wave: 120) | 0.1 | 1.77 V | Minimal for 100 mA |
| 2200 | 60 (full-wave: 120) | 0.1 | 0.38 V | Adequate at light load |
| 2200 | 60 (full-wave: 120) | 0.5 | 1.89 V | Marginal at 0.5 A |
| 4700 | 60 (full-wave: 120) | 0.5 | 0.89 V | Good for 0.5 A |
| 10000 | 60 (full-wave: 120) | 1.0 | 0.83 V | Required for 1 A linear |

Formula: V_ripple = I_load / (f_ripple × C), where f_ripple = 2 × line frequency.

### LM317 Adjustable Regulator Design Points

| Parameter | Value | Formula/Source |
|-----------|-------|---------------|
| Output range | 1.25–37 V | Set by R1 (240 Ω) and R2 (potentiometer) |
| Output voltage | V_out = 1.25 × (1 + R2/R1) | Datasheet equation |
| Dropout voltage | 2–3 V (typical) | Not an LDO |
| Line regulation | 0.01%/V | At 25 °C |
| Load regulation | 0.1% | For I_out: 10 mA–1.5 A |
| R1 reference current | 50 µA (flows through R1) | Determines min load; R1 = 240 Ω ensures 5 mA min |
| Max input-output differential | 40 V | Abs max; derate for thermal |

## Scaling Notes

- **Bench scale**: LM7805 + bridge rectifier + 2200 μF filter on a breadboard. Delivers 0.5–1 A at 5 V from a wall transformer. The default teaching build.
- **Lab supply scale**: LM317 with pass-transistor boost (2N3055) delivers 1.5–3 A continuously adjustable 1.25–30 V. Multiple output rails (+5, ±12, +3.3 V) from separate regulators on a shared rectifier-filter front end.
- **Production scale**: switching regulators (buck, flyback) at 100 kHz–1 MHz. A 50 W flyback supply for embedded systems fits in 10 cm³ and achieves 85% efficiency — impossible with linear (would dissipate 30 W as heat).
- **High-power scale**: forward/full-bridge converters at 100+ kW. System-level concern: PFC (power factor correction) front end, EMI filtering, thermal management. Crosses into [power electronics](power-electronics.md) territory.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Output voltage too low (4.2 V instead of 5 V) | Ripple trough drops below regulator dropout (7 V); reservoir capacitor too small | Increase C (4700 → 10000 μF); reduce load current; use higher-voltage transformer secondary |
| LM7805 overheats and shuts down (thermal protection) | Power dissipation (V_in − V_out)·I_out exceeds heatsink capability | Compute P = (V_in − V_out)·I; add heatsink with θ < (T_jmax − T_amb)/P; for P > 5 W, use switching regulator |
| Excessive ripple on output (>100 mV) | Reservoir capacitor too small for load, or capacitor ESR degraded (old electrolytic) | Replace C with larger value and fresh (low-ESR) part; verify with LCR meter |
| Switching regulator emits audible whine | Inductor saturation (core vibrating) or switching frequency in audio band | Use higher-saturation-current inductor (≥1.5× peak load); some older bucks switch at 20–30 kHz (audible); choose 100+ kHz part |
| Regulator oscillates (high-frequency output ripple not at 60 Hz) | Missing input/output bypass capacitors; regulator unstable | Add 0.33 μF on input, 0.1 μF on output, directly at regulator pins; check per datasheet |
| Transformer buzzes and overheats | Primary winding shorted turn, or secondary overloaded | Disconnect secondary; if buzz persists, transformer is faulty; verify secondary current is within VA rating |
| Output briefly correct then drops to zero | Current limit or thermal shutdown activating under load | Measure input voltage under load; if V_in sags, the rectifier/filter can't sustain the current; reduce load or increase reservoir capacitor |

## Safety

- **Mains voltage (120/240 VAC)**: The transformer primary is lethal. Always fuse the primary. Use an isolation transformer when prototyping on the line side. Never touch the primary circuit while powered.
- **Reservoir capacitors**: A 4700 μF capacitor charged to 25 V stores 1.5 J — enough to melt wire and burn skin. Add a bleeder resistor (1 kΩ, 1 W across the cap) to discharge within 30 s.
- **Heatsink temperature**: An LM7805 dissipating 5 W reaches 75 °C above ambient on a 10 °C/W heatsink — 100 °C case temperature at 25 °C ambient. Burns skin on contact. Mark as hot surface.
- **Regulator thermal shutdown**: LM7805 has internal thermal limiting at ~150 °C junction. The output will drop intermittently as the regulator cycles. This is a protective feature, not a failure mode — fix the thermal design.
- **Reverse polarity on output**: Applying external voltage in reverse to the regulator output (e.g., connecting a battery backwards) destroys the regulator. Add a reverse-protection diode across input-output per the LM7805 datasheet for any battery-backed supply.

## Quality Control

### Acceptance Criteria

- Output DC voltage within regulator tolerance: LM7805 specified as 4.8–5.2 V (±4%) over the full line and load range.
- Ripple <50 mV peak-to-peak at full rated load (linear); <100 mV (switching).
- Line regulation: output changes <100 mV for input varying from V_min to V_max.
- Load regulation: output changes <50 mV for load varying from 10% to 100% of rated.
- No oscillation: output stable under transient load steps (observe on oscilloscope — no ringing >10% of output).

### Testing Methods

- Line regulation: vary AC input ±10% with a variac; measure output DC at full load.
- Load regulation: step load from 10% to 100% (switch in a parallel power resistor); observe output transient and final value.
- Ripple measurement: oscilloscope AC-coupled at the output, bandwidth 20 MHz, full load.
- Thermal: full load for 10 minutes; infrared thermometer on regulator case and heatsink. Target case <70 °C (ensures junction <125 °C).

## Variations and Alternatives

### Regulator Topology Selection

| Topology | V_out vs V_in | Efficiency | Complexity | Best for |
|----------|---------------|-----------|-----------|----------|
| Linear (LM7805) | V_out < V_in only | 30–50% | Lowest | Low-noise, low-current, precision |
| LDO (low dropout) | V_out < V_in (ΔV 0.1–0.5 V) | 40–60% | Low | Battery (V_in barely > V_out) |
| Buck (step-down) | V_out < V_in | 85–95% | Medium | High-efficiency step-down |
| Boost (step-up) | V_out > V_in | 80–90% | Medium | Battery boost (e.g., 3.7 V → 5 V) |
| Buck-boost | V_out above or below V_in | 75–90% | Medium-high | Battery whose voltage crosses V_out |
| Flyback (isolated) | V_out independent of V_in | 70–85% | High | Mains-isolated supply, multi-output |

### Mains Front-End Choices

- **Half-wave rectifier** (1 diode): Simplest, but uses only one half-cycle; ripple at line frequency (60 Hz), requiring 2× the filter capacitance. Acceptable only for currents below ~100 mA.
- **Full-wave bridge** (4 diodes): Uses both half-cycles; ripple at 2× line frequency (120 Hz). Standard for all mains supplies above 100 mA. Two diode drops (1.4 V) cost some efficiency.
- **Full-wave center-tap** (2 diodes + center-tapped transformer): Only one diode drop (0.7 V); common in high-current supplies where diode loss matters.
- **Voltage doubler** (2 diodes + 2 capacitors): Produces ~2.8 × V_rms from 120 VAC; used in 120/240 VAC auto-ranging supplies.

## References

- [Semiconductor devices](semiconductor-devices.md) — diodes (rectifiers), transistors/MOSFETs (regulator pass elements), zener/bandgap references.
- [Electrical systems](electrical-systems.md) — transformers, mains wiring, safety grounding, fusing.
- [Passive components](passive-components.md) — capacitors (reservoir/filter), inductors (chokes, switching energy storage).
- [Circuit fundamentals](circuit-fundamentals.md) — reactance, time constants, AC analysis of the filter stage.
- [Analog circuits](analog-circuits.md) — [diode circuits](analog-circuits.diode-circuits.md) and zener reference operation.
- [Power electronics](power-electronics.md) — system-level converter manufacturing.
- [Power conversion circuits](power-conversion-circuits.md) — DC-AC inversion and motor drives.
- Deep articles: [rectifier-circuits](power-supply-circuits.rectifier-circuits.md), [filter-circuits](power-supply-circuits.filter-circuits.md), [linear-regulators](power-supply-circuits.linear-regulators.md), [switching-regulators](power-supply-circuits.switching-regulators.md).

---
*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
