# Circuit Fundamentals

> **Node ID**: electronics.circuit-fundamentals
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.passive-components`](passive-components.md), [`electronics.electrical-systems`](electrical-systems.md)
> **Enables**: None
> **Timeline**: Years 15-30
> **Outputs**: circuit-analysis
> **Critical**: No — circuit theory is analytical knowledge, not a physical bottleneck; a practiced practitioner can derive results from memory once components exist

## Overview

Circuit fundamentals is the body of theory that lets you predict what a network of components will do *before* you build it. It does not manufacture anything itself — it is the analytical lens applied to the outputs of [Passive Components](passive-components.md) and [Electrical Systems](electrical-systems.md). Without it, every circuit is built by trial and error; with it, a designer can specify resistor, capacitor, and inductor values on paper and expect a working prototype on the first build.

DC and AC circuit theory was complete by the late 19th century — Ohm (1827), Kirchhoff (1845), Thévenin (1883), Steinmetz's phasor method (1893). It belongs to the same era as dynamos, telegraphs, and incandescent lighting. The `electronic` era (tubes, transistors, integrated circuits) builds *on top of* this foundation but does not redefine it. A civilization with copper wire, batteries, and galvanometers can derive and verify all of this material.

This capability is the family hub for the DC and AC theory articles. Every later electronics capability — [analog circuits](analog-circuits.md), [power supply circuits](power-supply-circuits.md), [communications circuits](communications-circuits.md) — is designed using these analytical tools. The deep worked examples live in the process articles [dc-analysis](circuit-fundamentals.dc-analysis.md) and [ac-analysis](circuit-fundamentals.ac-analysis.md).

## Prerequisites

### Materials

- **Resistors** — E12 and E24 series carbon-film or metal-film parts, ¼ W and ½ W, from [Passive Components](passive-components.md). Values spanning 10 Ω to 1 MΩ cover the teaching range.
- **Capacitors** — ceramic 10 pF–1 μF and electrolytic 1–1000 μF from [Passive Components](passive-components.md), for RC timing and coupling demonstrations.
- **Inductors** — 1 μH–10 mH air-core and iron-core, for RL and RLC resonance work.
- **Hookup wire** — 22 AWG solid or stranded, for breadboard interconnect.

### Tools and Equipment

- [Electrical Systems](electrical-systems.md) — variable DC bench supply (0–30 V, 0–2 A), AC signal generator (sine, 10 Hz–1 MHz), and analog or digital multimeter (DMM) with voltage, current, and resistance ranges.
- Breadboard (solderless) for rapid prototyping, or perforated PCB for soldered builds.
- Oscilloscope (dual-channel, ≥20 MHz bandwidth) for observing time-varying waveforms — essential for AC and transient analysis.

### Knowledge

- Arithmetic of fractions, powers of ten, and scientific notation — the load-bearing math for Ohm's law and series/parallel combinations.
- Basic algebra for solving 2–N linear equations (mesh and node analysis).
- Complex numbers for the phasor transform in AC analysis.

### Infrastructure

- A dry, lit workbench with AC mains access for the bench supply and signal generator.
- Ground-fault circuit interrupter (GFCI) on bench mains if circuits will be powered above 30 V.

## Bill of Materials

| Component | Quantity (per lab station) | Source | Alternatives |
|-----------|---------------------------|--------|--------------|
| Resistor assortment (E12: 10 Ω–1 MΩ, ¼ W, 5%) | 5 each value (≈60 values, 300 parts) | [Passive Components](passive-components.md) — carbon film | Metal-film 1% for precision work |
| Capacitor assortment (ceramic 10 pF–1 μF + electrolytic 1–1000 μF, 25 V) | 3 each value | [Passive Components](passive-components.md) | Tantalum for low-leakage timing |
| Inductor assortment (1 μH–10 mH) | 2 each value | [Passive Components](passive-components.md) | Hand-wound on ferrite cores |
| Solderless breadboard (830 tie-points) | 1 | [Electrical Systems](electrical-systems.md) | Perfboard + solder for permanent builds |
| DC bench supply (0–30 V, 0–2 A, dual) | 1 | [Electrical Systems](electrical-systems.md) | Battery packs (6 V, 9 V) for fixed rails |
| Digital multimeter (3½ digit, AC/DC V, A, Ω) | 1 | [Electrical Systems](electrical-systems.md) | Analog VOM (less precise, needs no battery) |
| Oscilloscope (dual-channel, ≥20 MHz) | 1 shared / 2–4 stations | [Electrical Systems](electrical-systems.md) | PC sound-card scope (limited to ~20 kHz) |
| hookup wire (22 AWG solid, assorted colors) | 1 spool (25 m) | [Passive Components](passive-components.md) | Recycled Cat5 twisted-pair |

## Process Description

### Step 1: DC Analysis — Ohm's Law and Power

Apply Ohm's law (V = I·R) and the power law (P = V·I = I²R = V²/R) to single-resistor circuits. Measure voltage across and current through a known resistor (e.g., 1 kΩ at 5 V → expect I = 5 mA, P = 25 mW). Verify with the DMM that measured values fall within resistor tolerance (±5% for carbon film). Any deviation larger than tolerance indicates a meter burden (ammeter insertion resistance) or a supply sag under load.

### Step 2: Series and Parallel Combination

Combine resistors in series (R_total = R₁ + R₂ + …) and parallel (1/R_total = 1/R₁ + 1/R₂ + …). For two parallel resistors the shortcut R_total = R₁·R₂/(R₁+R₂) is used constantly. Build a voltage divider (e.g., two 10 kΩ resistors across 12 V → 6 V at the midpoint), then measure with a DMM. Note the loading effect: a 10 kΩ voltmeter across one divider half shifts the reading by ~1 V.

### Step 3: Kirchhoff's Voltage and Current Laws

Build a two-loop network (e.g., a T or π of three resistors fed from two supplies). Write KVL (sum of voltages around any closed loop = 0) and KCL (sum of currents at any node = 0). Solve the resulting 2–3 equation linear system by hand. Measure every branch voltage and current; they must match to within meter tolerance.

### Step 4: Thévenin and Norton Equivalents

Take a resistive network with a source and collapse it to its Thévenin equivalent (V_th in series with R_th). Determine V_th by open-circuit voltage measurement, and R_th by (V_oc − V_loaded) / I_loaded. Verify Norton equivalent (I_norton in parallel with same R_th) by computing I_norton = V_th / R_th and confirming the short-circuit current.

### Step 5: RC and RL Transient Analysis

Charge a capacitor through a resistor and observe the exponential: V(t) = V_final · (1 − e^(−t/τ)), where τ = R·C. With R = 10 kΩ and C = 100 μF, τ = 1 s — slow enough to time with a stopwatch. For an RL circuit, τ = L/R; with L = 10 mH and R = 1 kΩ, τ = 10 μs, requiring the oscilloscope. Measure τ from the scope trace and compare to the calculated value.

### Step 6: AC Analysis — Reactance and Impedance

Drive RC, RL, and RLC circuits with a sine-wave generator. Compute capacitive reactance X_C = 1/(2πfC) and inductive reactance X_L = 2πfL at the generator frequency. Measure the amplitude and phase shift across each element with the oscilloscope. For a series RLC circuit, observe resonance at f₀ = 1/(2π√(LC)) — at resonance X_L = X_C, impedance is purely resistive, and current peaks.

## Quantitative Parameters

| Parameter | Symbol | Formula | Typical Lab Range | Notes |
|-----------|--------|---------|-------------------|-------|
| Ohm's law | — | V = I·R | 0–30 V, 0–2 A, 10 Ω–1 MΩ | Foundation of all DC analysis |
| Power (DC) | P | P = V·I = I²R = V²/R | mW to a few W | ¼ W resistor limit; P > rating → smoke |
| Series resistance | R_s | R₁ + R₂ + … | — | Linear in count |
| Parallel resistance (2) | R_p | R₁·R₂ / (R₁+R₂) | — | Always less than smallest R |
| Voltage divider | V_out | V_in · R₂ / (R₁+R₂) | — | Loaded by voltmeter; R ≪ R_meter needed |
| RC time constant | τ_RC | R · C | µs (kΩ·nF) to hours (MΩ·F) | 63.2% of final value after 1τ |
| RL time constant | τ_RL | L / R | µs to ms | Limited by inductor parasitics |
| Capacitive reactance | X_C | 1 / (2πfC) | Ω | Decreases with frequency |
| Inductive reactance | X_L | 2πfL | Ω | Increases with frequency |
| Resonant frequency (LC) | f₀ | 1 / (2π√(LC)) | Hz to MHz | At f₀, X_L = X_C in series RLC |
| Quality factor (series RLC) | Q | (1/R)·√(L/C) = 2πf₀L/R | 0.1–100 | High Q → sharp resonance |
| Thévenin equivalent resistance | R_th | V_oc / I_sc | — | Collapse any linear 2-terminal network |
| RMS of sine | V_rms | V_peak / √2 | — | V_avg of full-wave rectified sine = 0.637·V_peak |
| Average power | P_avg | V_rms · I_rms · cos(φ) | W | cos(φ) = power factor; 1 for resistive |
| Reactive power | Q | V_rms · I_rms · sin(φ) | VAR | No net energy transfer; stored and returned |
| Apparent power | S | V_rms · I_rms | VA | What transformers and wires must carry |

### RC and RL Transient Values

The exponential approach to steady state is governed by the time constant τ. After each multiple of τ, the remaining gap closes by 63.2%:

| Elapsed time | % of final value (charging) | % of initial value (discharging) |
|-------------|----------------------------|--------------------------------|
| 1τ | 63.2% | 36.8% |
| 2τ | 86.5% | 13.5% |
| 3τ | 95.0% | 5.0% |
| 4τ | 98.2% | 1.8% |
| 5τ | 99.3% | 0.7% |

Engineering convention: a capacitor is "fully charged" after 5τ (within 1%). For τ = 1 s, that is 5 seconds. For τ = 10 µs, that is 50 µs — the oscilloscope timebase needed to observe the complete transient.

### Standard Resistor Value Examples (E12 series)

| Multiplier | Values | Power rating |
|-----------|--------|--------------|
| ×1 | 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82 | ¼ W (0.25 W) |
| ×100 | 1 k, 1.2 k, 1.5 k, 1.8 k, 2.2 k, 2.7 k, 3.3 k, 3.9 k, 4.7 k, 5.6 k, 6.8 k, 8.2 k | ¼ W |
| ×10 000 | 100 k, 120 k, …, 820 k | ¼ W |

E24 inserts intermediate values (e.g., 11, 13, 16, 20, 24, 30, 36, 43, 51, 62, 75, 91) for 5% tolerance work. 1% metal-film uses E96 (96 values per decade).

## Scaling Notes

Circuit theory scales from a single ¼ W resistor on a breadboard to megawatt transmission lines with no change in the governing equations — Ohm's law holds from microamps to kiloamps. What changes are the parasitics: at DC, wire resistance is often negligible; at 1 MHz, trace inductance (~1 nH/mm) dominates. A breadboard's parasitic capacitance (~2 pF between adjacent rows) corrupts measurements above ~1 MHz, requiring a ground-plane PCB.

- **Bench scale**: single components on breadboard, DMM and oscilloscope, 0–30 V, 0–2 A. Maximum frequency limited by breadboard parasitics (~1 MHz).
- **Instrument scale**: shielded coaxial probes, ground-plane PCB, precision references (0.01% voltage references). Enables 5½-digit DMM resolution and sub-µV measurements.
- **Power scale**: same KVL/KCL, but now thermal management (I²R losses in connectors), skin effect at high frequency, and safety become dominant constraints.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Measured voltage disagrees with calculated by >5% | Meter burden loading (DMM 10 MΩ input on high-impedance node) or resistor out of tolerance | Measure resistor out of circuit; use high-impedance (10 MΩ+) voltmeter; account for divider loading |
| RC charging curve much slower than τ = RC predicts | Electrolytic capacitor tolerance −20%/+80%, or leakage current | Use film or ceramic capacitor for timing; characterize actual C with a capacitance meter |
| Oscilloscope shows 50/60 Hz hum on all traces | Ground loops or unshielded leads picking up mains | Use shielded coaxial probes; tie all instruments to one ground point; route signal leads away from power cables |
| Series RLC resonance peak not sharp | Inductor series resistance too high (low-Q), or generator output impedance loading the tank | Use higher-Q inductor (air-core or low-DCR ferrite); drive through a series resistor >> R of the tank |
| Ammeter reading shifts when multimeter range changed | Ammeter burden resistance changes per range (0.1 Ω on 10 A range, 10 Ω on mA ranges) | Use the highest range that still resolves; or compute current from measured V across a known shunt |
| Voltage divider output drifts over minutes | Resistor self-heating (I²R) changing resistance, or supply sag | Compute power dissipation: P = V²/R; use higher-wattage resistor if P > rating/2 |

## Safety

- **Resistor overheating**: Applying V²/R > power rating ignites the component. A ¼ W resistor dissipating 1 W reaches >200°C in seconds, producing smoke and burning the breadboard. Compute P before energizing.
- **Electrolytic capacitor polarity**: Reversed-polarity electrolytics (or voltage > rating) can rupture explosively, ejecting hot electrolyte. Observe the stripe (cathode) and derate to 60–70% of rated voltage.
- **High-current bench supplies**: A 2 A supply shorted through thin wire (or a low-ohm resistor) can melt insulation and start fires. Set current limits on the supply before connecting; use appropriate-gauge wire (≥22 AWG for 2 A).
- **Mains-powered instruments**: All bench equipment chassis must be earth-grounded. Use GFCI outlets for any mains-connected setup above 30 V.

## Quality Control

### Acceptance Criteria

- Calculated vs measured values agree within component tolerance: ±5% for carbon-film resistors, ±10% for ceramic capacitors, −20%/+80% for electrolytics.
- KVL loops close to within DMM accuracy (±0.5% of reading + 1 digit on a 3½-digit meter).
- Time-constant measurements match R·C or L/R within 10% (limited by capacitor tolerance).

### Testing Methods

- Four-wire (Kelvin) resistance measurement for values below 10 Ω, where lead resistance introduces >1% error.
- Capacitance meter for verifying electrolytic value; these have wide tolerance and drift with age.
- Oscilloscope cursor measurement for time constants and phase shifts — set the timebase so 3–5 τ fit across the screen.

### Sampling Procedure

- Verify resistor assortment against markings on receipt: sample 5% per value with the DMM. Reject the lot if any sampled part is out of tolerance.
- Periodically calibrate the DMM against a known voltage reference (e.g., 1.000 V bandgap reference).

## Variations and Alternatives

- **Nodal analysis vs mesh analysis**: Both solve the same linear network. Nodal (KCL at each node) is easier for circuits with many parallel branches; mesh (KVL around each independent loop) is easier for circuits with many series elements. Nodal is the method computers use (SPICE).
- **Thévenin vs Norton equivalent**: Interchangeable — V_th = I_norton · R_th. Thévenin (voltage source in series with R) is more intuitive for voltage-divider-loaded circuits; Norton (current source in parallel with R) is more intuitive for transistor modeling.
- **Phasor vs time-domain AC analysis**: Phasor (complex-number) method reduces sinusoidal AC to algebra; time-domain keeps the full waveform but requires differential equations. Phasor is the standard for single-frequency analysis; time-domain (via Fourier or Laplace) is needed for non-sinusoidal or multi-frequency signals.
- **Maximum power transfer vs efficiency**: Matching R_load = R_th delivers maximum *power* to the load but wastes 50% in R_th. Power transmission prioritizes *efficiency* (R_load ≫ R_source). This trade-off governs audio amplifier output (matched) vs grid power distribution (mismatched for efficiency).

### Comparison: Analysis Methods

| Method | Best for | Complexity | Computer-solvable |
|--------|----------|-----------|-------------------|
| Ohm's law + series/parallel | Single-source, reducible networks | Low (mental arithmetic) | N/A |
| Node-voltage (KCL) | Multi-source, many nodes | Medium (linear system) | Yes (SPICE default) |
| Mesh-current (KVL) | Multi-loop, planar circuits | Medium (linear system) | Yes |
| Thévenin/Norton | Simplifying a network feeding a varying load | Low (once V_oc, I_sc found) | N/A |
| Superposition | Linear circuits with multiple sources | Medium (one source at a time) | Yes |

### Maximum Power Transfer — Worked Example

A 12 V battery with internal resistance R_s = 0.5 Ω drives a variable load R_load. Maximum power transfer occurs at R_load = R_s = 0.5 Ω. The load current is I = 12/(0.5+0.5) = 12 A. Load power P_load = I²·R_load = 144·0.5 = 72 W. Battery internal dissipation P_s = I²·R_s = 72 W. Efficiency = P_load / (P_load + P_s) = 50%. The matched condition wastes half the available energy in the source resistance — which is why power transmission lines operate at R_load ≫ R_s (efficiency >95%), while audio amplifiers operate near R_load = R_s for maximum *power* delivery to the speaker.

### Y-Delta (Star-Mesh) Transformation

When a network contains a delta (Δ) or wye (Y) of three resistors that cannot be reduced by series/parallel alone, the Y-Δ transformation converts one to the other:

- **Y to Δ**: R_ab = (R_a·R_b + R_b·R_c + R_c·R_a) / R_c
- **Δ to Y**: R_a = (R_ab·R_ca) / (R_ab + R_bc + R_ca)

This unlocks bridge circuits (Wheatstone bridge) and three-phase power networks (Y-connected vs Δ-connected motors and transformers).

## References

- [Passive Components](passive-components.md) — the physical R, L, C parts this theory analyzes.
- [Electrical Systems](electrical-systems.md) — sources, wiring, meters, and bench instruments.
- [Analog Circuits](analog-circuits.md) — bias networks, amplifiers, and filters designed with these fundamentals.
- [Power Supply Circuits](power-supply-circuits.md) — rectifier→filter→regulator chain built on RC time constants and impedance.
- Process articles: [dc-analysis](circuit-fundamentals.dc-analysis.md), [ac-analysis](circuit-fundamentals.ac-analysis.md) — worked examples and parameter tables.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md)*
