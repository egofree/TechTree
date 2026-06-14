# Power Amplifiers

> **Node ID**: `electronics.analog-circuits.power-amplifiers`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md), [`electronics.analog-circuits.amplifier-fundamentals`](analog-circuits.amplifier-fundamentals.md)
> **Outputs**: power-amplifier-designs
> **Timeline**: Years 30-50
> **Critical**: No — design pedagogy layer; the underlying transistor manufacturing (semiconductor-devices) is the critical prerequisite

This article is about amplifiers that deliver **watts to a load** — a loudspeaker, a transmission-line antenna, a servo motor, a piezo actuator — rather than the millivolts of signal voltage handled by [Amplifier Fundamentals](analog-circuits.amplifier-fundamentals.md). When the output must carry real power, three new problems dominate: **efficiency** (every watt dissipated as heat in the transistor needs a heatsink and a power supply big enough to deliver it), **linearity at large swing** (the small-signal hybrid-pi model from the prerequisite article breaks down when v_pi is hundreds of mV, not a few mV), and **distortion that comes from the amplifier class itself** (crossover in class B, switching ripple in class D).

The four canonical classes — A, B, AB, D — are defined by the **conduction angle**: the fraction of the input cycle over which each output transistor conducts. That single parameter fixes the maximum theoretical efficiency and the dominant distortion mechanism, and from it everything else (heatsink size, power supply rails, output filter) follows.

**Boundary**: The small-signal biasing, Q-point stability, and hybrid-pi model are owned by [Amplifier Fundamentals](analog-circuits.amplifier-fundamentals.md) — this article assumes all of that and proceeds to the power stage. The fabrication and parameters of power transistors (TIP31C, TIP122, IRF540N, IGBTs) are owned by [Semiconductor Devices](semiconductor-devices.md); we only use the datasheet numbers. Operational-amplifier power stages and integrated audio amplifiers (LM386, TDA7294) are out of scope — the foundation here is discrete transistors, the way the classes are derived and understood.

## The Conduction Angle and Efficiency

Each class is defined by how much of the input sine wave each output transistor conducts over:

| Class | Conduction angle | Devices conducting | Max theoretical efficiency | Dominant distortion |
|-------|------------------|--------------------|---------------------------|---------------------|
| **A** | 360° (full cycle) | One device, always on | 25% (single-ended) / 50% (push-pull) | Crossover: none. Nonlinear large-signal gain |
| **B** | 180° (half cycle each) | Two devices, alternately | 78.5% (π/4) | Crossover (the dead zone around zero) |
| **AB** | slightly > 180° each | Two devices, briefly overlapping | 50-70% (depends on idle current) | Crossover: nearly eliminated by idle bias |
| **D** | Switching (PWM), not linear | Two (or four) switching devices | 90-98% | Switching ripple, EMI; linearity depends on the modulator |

Efficiency here means **output signal power ÷ DC input power drawn from the rails**. The rest is heat in the transistors. A 100 W class-A amplifier dissipates ≥ 300 W as heat at idle and needs a fan-cooled heatsink; a 100 W class-D amplifier dissipates ~10 W and fits on a chip.

## Class A — Always On, Linear, Inefficient

A single transistor biased to carry the full load current all the time. The Q-point sits in the middle of the load line (V_CEQ ≈ V_CC/2, I_CQ ≈ I_load(peak)). The signal swings the operating point up and down the load line; the transistor never cuts off.

```
                V_CC
                 |
                 R_C  (or transformer primary, or constant-current source)
                 |
   v_in --Q1(base)--> Collector ----+----> v_out --> Load (via C_out or transformer)
                 |
                Emitter -- R_E -- GND
                 |
                GND

   Transistor conducts for the FULL 360° cycle.
   Max efficiency (single-ended, resistive load):  25%
        → because P_DC = V_CC × I_CQ  (constant)
                   P_out(max) = (V_CC/2)²/(2 × R_load) = V_CC² × I_CQ / 8
                   η_max = P_out / P_DC = 25%
   Max efficiency (transformer-coupled or inductive load): 50%
   Idle dissipation = V_CEQ × I_CQ = maximum (worst case is silence!)
```

Class A is the most linear class — there is no handoff between devices, so there is no crossover. That is why ultra-high-end audio and some RF amplifiers still use it. The cost is heat: the transistor dissipates the *most* power at zero signal (silence), because then no power goes to the load and all of P_DC cooks the device.

**Why 25%?** For a single-ended resistive load, the DC input is P_DC = V_CC × I_CQ (constant, all the time). The maximum undistorted sine output power into a load that swings V_CEQ from 0 to V_CC symmetrically is P_out = (V_CC/2)² / (2 R_load) = V_CC × I_CQ / 8. So η_max = (V_CC × I_CQ / 8) / (V_CC × I_CQ) = 1/4 = 25%. The other 75% is dissipated in the transistor and R_C. An inductive (transformer) load lets the collector swing to 2 V_CC peak-to-peak, doubling the output power and reaching 50% — still half the rail power goes up as heat.

## Class B — Push-Pull, Efficient, but Crossover-Distorted

Two **complementary** transistors (one NPN, one PNP) share the load. Each conducts for exactly half the cycle: the NPN pushes current into the load on the positive half, the PNP pulls current out on the negative half. With no idle current, both are off around the zero crossing — and that gap is the **crossover distortion** that defines class B.

```
                +V_CC
                 |
                 E   Q1 NPN (pushes on positive half)
                 |
   v_in ----+----B1
            |    |
            |    C1--+---> v_out --> Speaker (8 Ω)
            |    C2--+      |
            |    |          |
            |    B2         |
            |    E   Q2 PNP (pulls on negative half)
            |    |          |
                GND        R_L (load)

   Each transistor conducts 180°. Both OFF around zero → dead zone.
   Max efficiency: 78.5% (π/4 ≈ 0.785)
        → P_DC = (2/π) × V_CC × I_peak   (average of full-wave rectified sine)
          P_out = (I_peak)² × R_L / 2 = V_CC² / (2 × R_L) at peak swing
          η_max = (π/4) = 78.5%
   Crossover distortion: high THD (1-10%) at small signals, audible "fizz"
```

**Why 78.5%?** The DC drawn from each rail is the average of a half-wave rectified sine: I_DC = I_peak / π per rail, so total P_DC = 2 × V_CC × I_peak / π. The output power at peak swing (I_peak = V_CC/R_L into R_L) is P_out = V_CC² / (2 R_L). So η_max = (V_CC²/2 R_L) / (2 V_CC × V_CC/(π R_L)) = π/4 ≈ 78.5%. The remaining 21.5% is dissipated in the two transistors, split evenly.

**Crossover distortion**: in the dead zone around v_in = 0 (specifically, |v_in| < V_BE ≈ 0.7 V), neither transistor is on. The output is flat zero until one of them turns on. For a small input signal (say 100 mV), the output is a heavily distorted square-ish wave that spends most of its time stuck at zero. This sounds terrible — a "fizzy" or "buzzy" quality on quiet passages — and makes pure class B almost unusable for audio. Class AB is the fix.

## Class AB — Bias the Crossover Away

Class AB adds a small **idle bias current** so that both transistors are just barely on at zero input. The handoff from one device to the other now happens smoothly — at the moment v_in crosses zero, both devices are conducting slightly, so there is no dead zone. The conduction angle becomes slightly more than 180° per device, hence "AB".

The idle bias is set by a **V_BE multiplier** (a BJT with two resistors that synthesises ~1.4 V, enough to forward-bias both NPN and PNP bases) or by two diodes / a diode string biased to drop ~1.4 V between the bases:

```
                +V_CC
                 |
                 E   Q1 NPN (power)
                 |
                 C1
   v_in --[driver]-B1
                 |     <-- "V_BE multiplier" or bias diodes set V_BB ≈ 1.4 V
                 B2        across B1-B2; idle current ~ 20-100 mA
                 C2
                 E   Q2 PNP (power)
                 |
                GND
                 |
                 +----> v_out --> Speaker

   Both transistors slightly ON at v_in = 0 → no dead zone → crossover gone.
   Efficiency: 50-70% (depends on idle current — more idle = less efficient).
   Dominant residual distortion: gain mismatch between NPN and PNP (negative
       feedback from a driver op-amp fixes this, see "real AB amplifiers").
```

The price of class AB is the idle dissipation: each transistor dissipates V_CC × I_idle at all times, even at silence. For ±20 V rails and 50 mA idle per device, that is 2 W of idle heat per channel — easily handled by a modest heatsink, a huge improvement over class A's 300 W. Real AB amplifiers therefore run a "hotter" idle for lower distortion or a "cooler" idle for higher efficiency; the typical compromise is 20-100 mA per device, giving distortion around 0.1% THD and efficiency around 60% at full output.

**Real AB amplifiers** wrap the output stage in a negative-feedback loop driven by an op-amp or a long-tailed-pair input stage. The feedback forces the output to match v_in / β_feedback regardless of the output transistors' gain mismatch, dropping THD to < 0.01%. This is the topology of virtually every discrete hi-fi and professional audio amplifier ever built.

## Class D — PWM Switching, 90%+ Efficient

Class D abandons linear operation entirely. The output transistors are driven as **switches** (fully ON or fully OFF, never in the linear region — see [Transistor Switch Circuits](analog-circuits.transistor-switch-circuits.md) for that mode). The audio signal is converted to a pulse-width-modulated (PWM) square wave whose duty cycle tracks the instantaneous signal voltage. The load sees only the *average* of the PWM waveform, recovered by a passive LC low-pass filter.

```
   Audio in --> [PWM Modulator] --> [Gate driver] --> [H-bridge or half-bridge]
                                                              |
                                            +-----------------+
                                            |                 |
                                            |   LC reconstruction LPF
                                            |   (cuts at ~30-60 kHz)
                                            |                 |
                                            +-----------------+
                                                  |
                                              Speaker (8 Ω)

   Duty cycle D(t) = (1 + v_audio(t)/V_tri) / 2     (V_tri = triangle peak)
   Average output  = (2D − 1) × V_CC  = v_audio(t)  (after LPF removes carrier)
   Devices are always saturated (low loss) or off (zero loss) → η = 90-98%
   Switching frequency: 250 kHz - 4 MHz (modern designs)
```

Because the transistors dissipate power only during the brief switching transition (and a tiny I²R during ON), class D reaches 90-98% efficiency — an order of magnitude better than class A or B. The trade-offs are:

- **Switching ripple and EMI** at the carrier frequency (300 kHz - 4 MHz) — the LC filter and PCB layout must contain it; this is the dominant design challenge.
- **Dead-time distortion**: in an H-bridge, both transistors in one leg must never be ON simultaneously (that would short the supply). A small "dead time" is inserted between turn-off of one and turn-on of the other, during which the output is uncontrolled — this adds distortion at the zero-crossing, much like class-B crossover. Modern controllers minimise it.
- **Feedback is essential**: the open-loop linearity of a PWM modulator is poor. Real class-D amplifiers use closed-loop feedback (often with the modulator inside the loop) to drive THD below 0.1%.

Class D dominates battery-powered audio (phones, laptops, Bluetooth speakers) and is now standard in car audio, sound-reinforcement, and most home theatre receivers. Above a few hundred watts it is essentially the only practical choice — a 1000 W class-AB amplifier wastes ~700 W as heat; a class-D equivalent wastes ~100 W.

## Worked Example — Efficiency of a Class-AB Amplifier Delivering 10 W to an 8 Ω Speaker from ±20 V Rails

**Spec**: complementary class-AB output stage, supply rails ±20 V, load 8 Ω, output sine 10 W RMS. Idle bias current 50 mA per transistor (a typical low-distortion AB setting). Find the efficiency.

### Step 1 — Output voltage and current

```
   P_out = V_out(rms)² / R_L
   V_out(rms) = √(P_out × R_L) = √(10 × 8) = √80 ≈ 8.94 V rms
   V_out(peak) = 8.94 × √2 ≈ 12.65 V peak  (well within the ±20 V rails)
   I_out(peak) = V_out(peak) / R_L = 12.65 / 8 ≈ 1.58 A peak
```

### Step 2 — DC power drawn from the rails (signal portion only)

Each rail supplies a half-wave rectified sine of peak I_out(peak). The average of a half-wave rectified sine is I_peak / π:

```
   I_DC(per rail, signal) = I_out(peak) / π = 1.58 / π ≈ 0.503 A
   P_DC(signal) = 2 rails × V_CC × I_DC = 2 × 20 × 0.503 ≈ 20.1 W
```

### Step 3 — Idle dissipation

Both transistors carry 50 mA continuously (the class-AB idle bias):

```
   P_idle = 2 × V_CC × I_idle = 2 × 20 × 0.050 = 2.0 W
```

### Step 4 — Total DC input and efficiency

```
   P_DC(total) = P_DC(signal) + P_idle = 20.1 + 2.0 = 22.1 W
   η = P_out / P_DC(total) = 10 / 22.1 ≈ 0.452  →  45.2%
```

So this class-AB amplifier delivers 10 W to the speaker at 45% efficiency, dissipating 12.1 W as heat. (The pure class-B limit at this output would be 78.5% — the idle bias and the fact that we are below peak swing both cost efficiency.) The heatsink must dissipate ~12 W continuously; for a typical TO-220 pair on a 5 °C/W heatsink that is a 60 °C rise, giving a case temperature around 85 °C — warm but acceptable.

### Step 5 — Compare with class A and class D at the same 10 W output

- **Class A**: η ≤ 25% → P_DC ≥ 40 W, dissipating ≥ 30 W even at full output (and 40 W at silence). Needs a fan-cooled heatsink sized for the *idle* dissipation, not the signal.
- **Class D** at 92%: P_DC = 10/0.92 ≈ 10.9 W, dissipating 0.9 W. Fits on a small PCB pad, no heatsink.

The reason class D has displaced the others in commercial audio is visible in one line: **12 W vs 30 W vs 0.9 W** of heat for the same 10 W of audio output.

## Thermal Design

Power-transistor dissipation determines the heatsink. The junction temperature must be kept below the datasheet limit (150-175 °C for silicon, 200 °C for the junction itself but degraded reliability):

```
   T_j = T_ambient + P_diss × (R_θ(j-c) + R_θ(c-s) + R_θ(s-a))

   R_θ(j-c)  : junction-to-case, from datasheet (e.g. 1.0-5.0 °C/W for TO-220)
   R_θ(c-s)  : case-to-sink, set by insulator + grease (~0.5-1.0 °C/W)
   R_θ(s-a)  : sink-to-ambient, the heatsink rating (chosen by the designer)

   Design rule: keep T_j < 125 °C for long life (derate from the 150 °C max).
```

For the worked example above (12 W total dissipation, two devices, 1 °C/W junction-to-case each): each device dissipates 6 W. For T_j ≤ 125 °C at T_ambient = 50 °C, R_θ(s-a) ≤ (125 − 50)/6 − 1.0 − 0.5 ≈ 11 °C/W per device — a modest extruded heatsink. Class A's 30 W would need 2.3 °C/W with forced air; class D's 0.9 W needs no heatsink at all. This is why class matters.

## Output-Stage Topologies Beyond the Complementary Pair

The complementary NPN/PNP pair is the cleanest pedagogical class-B/AB circuit, but it requires a PNP power transistor with matching specs to the NPN. Real high-power amplifiers use several variants:

- **Quasi-complementary**: historically, good high-power PNPs were hard to make. Designers used an NPN power transistor on top and a complementary Darlington (NPN + PNP driver) on the bottom to fake the PNP. Obsolete now that matched complementary pairs exist, but the topology survives in older gear.
- **Darlington / Sziklai pairs**: each output device is replaced by a Darlington (two NPNs, gain ~10000) or a Sziklai pair (NPN + PNP, gain ~1000) to reduce drive current. The cost is ~1.2 V (Darlington) or ~0.6 V (Sziklai) of saturation loss, lowering the maximum output swing.
- **H-bridge (bridge-tied load, BTL)**: two complementary output stages drive the two ends of the load out of phase, doubling the voltage across the load for the same rails. Used in car audio (12 V single supply) and battery-powered class D to extract more power per rail volt.
- **Parallel devices**: for high current, several transistors are paralleled with small (0.1-0.5 Ω) emitter resistors for current sharing. The positive temperature coefficient of MOSFET R_DS(on) makes MOSFETs easier to parallel than BJTs (which suffer thermal runaway without emitter ballast).

## Class Comparison Table

| Class | Max efficiency | Typical THD | Complexity | Idle dissipation | Heat at full output | Typical application |
|-------|---------------|-------------|------------|------------------|---------------------|---------------------|
| **A** | 25% (SE) / 50% (PP) | 0.1-1% (best linearity) | Low (1 device) | Worst (max at silence) | High | Ultra-high-end hi-fi, guitar instrument amps, RF linear PA |
| **B** | 78.5% | 1-10% (crossover) | Medium (2 devices) | Zero (true class B) | Medium | Almost never used pure — crossover distortion disqualifies it for audio |
| **AB** | 50-70% | 0.01-0.5% (with feedback) | Medium (2 devices + bias network) | Low (2-20 W typical) | Medium | Discrete hi-fi and pro audio, the workhorse of audio power amps |
| **D** | 90-98% | 0.05-1% (modern, with feedback) | High (modulator + gate driver + LC filter) | Very low | Very low | Battery audio, phones/laptops, Bluetooth speakers, car audio, sound reinforcement, >100 W |

**Selection rule of thumb**: if you need < 1 W and care about linearity more than battery life → class A (or AB at low current). If you need 1-100 W of clean audio → class AB. If you need > 100 W, or you are battery-powered, or the heatsink budget is tight → class D. For RF power amplifiers (where the load is a tuned circuit, not a speaker) classes C, E, and F appear — they use the tuned load to filter the switching harmonics, but those are beyond the scope of this article.

## Design Checklist

- [ ] Chose the class by efficiency vs linearity needs (see selection rule above).
- [ ] Confirmed rail voltage gives enough swing: V_out(peak) = √(2 × P_out × R_L), with ~3-5 V of margin below the rail for saturation and bias losses.
- [ ] Computed worst-case device dissipation (per-device, not total) and sized the heatsink for T_j < 125 °C at the highest ambient.
- [ ] Class AB: set the idle bias (20-100 mA typical) using a V_BE multiplier thermally coupled to the output transistors (so it tracks their V_BE drop with temperature — without this, idle current runs away).
- [ ] Class AB: wrapped the output stage in negative feedback (op-amp or LTP driver) to suppress the NPN/PNP gain mismatch; set the feedback ratio for closed-loop gain.
- [ ] Class B: did not ship it — replace with AB. (Pure class B appears only where crossover distortion is tolerable, e.g. some motor drives.)
- [ ] Class D: chose switching frequency ≥ 10× the highest audio frequency; sized the LC reconstruction filter to cut at ~1/10 of the switching frequency; added dead-time to prevent shoot-through.
- [ ] Class D: confirmed the gate driver can source/sink the peak gate current at the switching frequency (Q_g × f_sw amperes average, much higher peak).
- [ ] Confirmed the load impedance is within the amplifier's stable range; most amplifiers are unstable below 4 Ω (some below 8 Ω) without output compensation.
- [ ] Added output protection: current limiting, SOA protection, and a Zobel network (series R-C across the output) to keep the amplifier stable into capacitive loads.

## See Also

- [Amplifier Fundamentals](analog-circuits.amplifier-fundamentals.md) — the prerequisite: small-signal biasing, Q-point stability, hybrid-pi model, voltage gain, input/output impedance. This article builds on it without re-deriving.
- [Semiconductor Devices](semiconductor-devices.md) — the physics and parameters of power transistors (TIP31C, TIP122 Darlington, IRF540N, IGBTs); the origin of V_CE(sat), R_DS(on), SOA curves, thermal resistance. Linked, not re-derived.
- [Passive Components](passive-components.md) — the power resistors (emitter ballast, Zobel), electrolytic coupling caps, and inductors (class-D LC filter, speaker crossover) that every power stage is built from.
- [Transistor Switch Circuits](analog-circuits.transistor-switch-circuits.md) — the saturated switching mode that class D operates in. The gate-driver and dead-time design of class D is the switch-circuits article applied at high frequency.
- [Analog Circuits](analog-circuits.md) — the parent capability hub.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
