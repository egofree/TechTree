# Timer Circuits

> **Node ID**: `electronics.analog-circuits.timer-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md)
> **Enables**: None
> **Outputs**: timer-circuit-designs
> **Timeline**: Years 25-40
> **Critical**: No — design pedagogy layer; the 555 IC and timing components come from semiconductor-devices and passive-components

The 555 timer is, by volume, the most ubiquitous integrated circuit ever manufactured. Introduced by Signetics in 1972 (designed by Hans Camenzind), it has sold in the tens of billions and is still in production from a dozen vendors fifty years later. Its genius is not doing anything new — it is, as we will see, a packaged relaxation oscillator — but doing it with *one* 8-pin chip, *two* external resistors, and *one* capacitor, for any timing interval from microseconds to hours. Before the 555, the same functions required an op-amp, a comparator, a flip-flop, and a transistor; after the 555, they cost twenty cents.

The 555 is a precision relaxation oscillator (see [Oscillator Circuits](analog-circuits.oscillator-circuits.md) §5 for the underlying principle). This article covers its internal architecture, its two canonical modes (astable and monostable), PWM generation, and the canonical applications. The chip itself comes from [Semiconductor Devices](semiconductor-devices.md); the timing R and C come from [Passive Components](passive-components.md).

---

## 1. The 555 Internals

### Block Diagram

The 555 contains five functional blocks, all built on one silicon die:

```
                          Vcc (pin 8)        ─── R ──┬── R ──┬── R ──┐
                                                       │       │       │
                                          ┌────────────┘       │       │
                                          │   (internal 3-     │       │
                                          │    resistor        │       │
                                          │    divider,        │       │
                                          │    each ~5 kΩ)     │       │
                                          │                    │       │
                                  2/3 Vcc ●                    │       │
                                          │ threshold ref       │       │
                                          ▼                    │       │
                          threshold ──►(−)│ comparator 1        │       │
                              (pin 6)    │             ┌───────┘       │
                                          └──►│ R       │ S      R    │
                                                │ Q ──┐ └── Flip-     │
                                          ┌──►│ S     │     Flop      │
                          trigger ──►(+)│  │             │  Q ──┬──────┘
                            (pin 2)     │ comparator 2  │      │
                                          │             │      │  ┌───┐
                                  1/3 Vcc ●  (1/3 ref   │      └──┤ Q │discharge
                                          │   from top  │         │(NPN)●── pin 7
                                          │   divider)  │         └───┘
                                                       │
   GND (pin 1) ────────────────────────────────────────┴────────────── GND

   Output: Q-bar drives pin 3 (push-pull, sinks OR sources up to 200 mA)
   Reset (pin 4): active-low, forces output low regardless of comparators
   Control (pin 5): overrides the 2/3 Vcc reference (for PWM / FM modulation)
```

### The Five Blocks

| Block | Function | Notes |
|-------|----------|-------|
| **Voltage divider** | Three equal resistors (~5 kΩ each) from Vcc to GND, producing reference levels of **2/3 Vcc** and **1/3 Vcc** | This is where the chip gets its name: "555" from the three 5 kΩ resistors. The control pin (5) taps the 2/3 Vcc node. |
| **Comparator 1 (threshold)** | Compares the threshold pin (6) against 2/3 Vcc. When pin 6 rises above 2/3 Vcc, it *resets* the flip-flop (output goes low). | The "end of charge" detector in astable mode; the input that ends a monostable pulse. |
| **Comparator 2 (trigger)** | Compares the trigger pin (2) against 1/3 Vcc. When pin 2 falls below 1/3 Vcc, it *sets* the flip-flop (output goes high). | The "start" input — the trigger that begins a monostable pulse or the lower threshold in astable mode. |
| **RS flip-flop** | Latches the comparator outputs: SET by comp 2, RESET by comp 1. Output Q drives pin 3. | The memory element that makes the timer *monostable* — once set by a trigger, it holds the output high until the threshold comparator resets it. |
| **Discharge transistor** | An NPN transistor whose collector is tied to pin 7. When the output is low, pin 7 is pulled to ground (discharging the timing cap); when the output is high, pin 7 is open (letting the cap charge through the external resistor). | This is the switch that alternately charges and discharges the timing capacitor, creating the free-running astable oscillation. |

The two thresholds — 1/3 Vcc and 2/3 Vcc — are the heart of the design. They are ratiometric (a fixed fraction of the supply, not an absolute voltage), so the timing formulas depend only on R, C, and ratios — *not* on the supply voltage. A 555 timer runs on anything from 4.5 V to 16 V and gives the same timing at any voltage within that range. This supply-voltage independence is why the 555 is so robust.

### The 8 Pins

| Pin | Name | Function |
|-----|------|----------|
| 1 | GND | Ground reference (0 V) |
| 2 | TRIGGER | Input: falling below 1/3 Vcc sets the flip-flop (output HIGH) |
| 3 | OUTPUT | Push-pull output; sinks or sources up to 200 mA |
| 4 | RESET | Active-low reset; tie to Vcc if unused (forces output LOW when pulled low) |
| 5 | CONTROL | Access to the 2/3 Vcc reference; apply a voltage here to modulate the threshold (PWM/FM) |
| 6 | THRESHOLD | Input: rising above 2/3 Vcc resets the flip-flop (output LOW) |
| 7 | DISCHARGE | Open-collector NPN; discharges the timing cap when output is LOW |
| 8 | Vcc | Supply voltage (4.5 – 16 V for bipolar NE555; 2 – 18 V for CMOS TLC555) |

---

## 2. Astable Mode — Free-Running Oscillator

In astable mode the 555 has no stable state — it oscillates continuously, producing a square wave with no trigger needed. The timing capacitor C charges through R_A and R_B (both in the charge path) until it hits 2/3 Vcc, then discharges through R_B alone (pin 7 pulls low, bypassing R_A) until it hits 1/3 Vcc, then repeats.

```
                              R_A
              Vcc ────/\/\/\────────┐
                                    │
                                    ●─── pin 7 (discharge)
                                    │
                              R_B   │
                          ───/\/\/\─┤
                                    │
                                    ●─── pin 6 (threshold)
                                    │  AND pin 2 (trigger)  ← tie 6 and 2 together
                                    │
                                   ─┴─  C (timing capacitor)
                                    │
                                   GND

              pins: 4,8 → Vcc ; 1 → GND ; 5 → 0.01 µF to GND ; 3 → OUTPUT

   Charge path (output HIGH):  C charges through R_A + R_B
       V_C rises 1/3 Vcc → 2/3 Vcc   (time t_high)
   Discharge path (output LOW):  C discharges through R_B only
       V_C falls 2/3 Vcc → 1/3 Vcc   (time t_low)
```

### Deriving the Timing Formulas

The capacitor charges from 1/3 Vcc toward Vcc through R_A + R_B. The time to go from 1/3 Vcc to 2/3 Vcc is found from the standard RC charging equation `V_C = V_final·(1 − e^(−t/RC))`:

```
Charge phase — capacitor rises 1/3 Vcc → 2/3 Vcc through (R_A + R_B):

    t_high = (R_A + R_B)·C · ln(2)
           = 0.693·(R_A + R_B)·C

Discharge phase — capacitor falls 2/3 Vcc → 1/3 Vcc through R_B only:

    t_low  = R_B·C · ln(2)
           = 0.693·R_B·C
```

The total period and frequency:

```
T = t_high + t_low = 0.693·(R_A + 2·R_B)·C

f = 1/T = 1.44 / ((R_A + 2·R_B)·C)
```

### Duty Cycle

The duty cycle is the fraction of the period the output is HIGH:

```
D = t_high / T = (R_A + R_B) / (R_A + 2·R_B)
```

Note two limitations of the standard astable:

1. **Duty cycle is always > 50%.** Because the charge resistance (R_A + R_B) is always greater than the discharge resistance (R_B alone), t_high > t_low, so D > 50%. You cannot reach exactly 50% with the standard topology.
2. **To approach 50%, make R_B ≫ R_A.** Then D ≈ R_B/(2·R_B) = 50% asymptotically. For a true 50% duty cycle, add a diode across R_B so C charges through R_A alone and discharges through R_B alone — then set R_A = R_B.

### Waveform

```
   V_C
   2/3 Vcc ────┐         ┌───┐         ┌───
                │        │   │        │
                │   t_high   │   t_low │
   1/3 Vcc ────┘   ┌─────┘   └─────┐
                    │               │
   0 ───────────────┘               └────────
                ↑ output HIGH   ↑ output LOW
   Output(3):
        HIGH ────────┐           ┌───────────
                    │           │
        LOW  ───────┘           └───
                |←── T ──→|
```

---

## 3. Monostable Mode — One-Shot Pulse Generator

In monostable mode the 555 has *one* stable state (output LOW). A negative-going trigger pulse on pin 2 produces a single output pulse of precisely controlled duration, then the chip returns to its stable state. This is the canonical **time-delay** and **pulse-stretching** circuit.

```
                          Vcc
                           │
                      R (timing resistor)
              Vcc ───/\/\/\────┬─── pin 7 (discharge)
                                 │
                                 ●─── pin 6 (threshold)
                                 │
                                ─┴─  C (timing capacitor)
                                 │
                                GND

              Trigger: pin 2 pulled below 1/3 Vcc (e.g. via pushbutton to GND)
              pins: 4,8 → Vcc ; 1 → GND ; 5 → 0.01 µF to GND ; 3 → OUTPUT

   Idle state: output LOW, pin 7 grounded → C held at 0 V (discharged).
   Trigger (pin 2 < 1/3 Vcc): flip-flop SET → output HIGH, pin 7 open.
       C now charges through R: V_C = Vcc·(1 − e^(−t/RC))
   At V_C = 2/3 Vcc: threshold comp RESETS flip-flop → output LOW,
       pin 7 grounds C → C rapidly discharges. Idle again.
```

### The Timing Formula

The output pulse width is the time for C to charge from 0 V to 2/3 Vcc:

```
T = R·C · ln(1 / (1 − 2/3))
  = R·C · ln(3)
  = 1.10·R·C
```

This is the single most-cited 555 formula. It is independent of Vcc (the 2/3 Vcc threshold is ratiometric) and accurate to within 1–2% for the bipolar NE555 (limited by comparator offsets, resistor tolerance, and capacitor leakage).

### Retriggering and the Duty Cycle Limit

The monostable does *not* retrigger: a second trigger during the output pulse is ignored (the flip-flop is already set). To get a retriggerable one-shot, add an external transistor to discharge C on each trigger. Also, the output pulse width is limited to roughly 50–70% of the period between triggers — the circuit needs time to recover (C must fully discharge through pin 7 before the next pulse).

---

## 4. PWM Generation

The 555 is a natural pulse-width modulator. Two techniques:

### 4a. Vary R_B (manual or voltage-controlled)

Since `D = (R_A + R_B)/(R_A + 2·R_B)`, replacing R_B with a potentiometer (or a JFET acting as a voltage-controlled resistor) varies the duty cycle continuously while the frequency stays approximately constant (it shifts by the R_B swing). This is the classic **LED dimmer** and **motor speed controller**.

### 4b. Apply a Control Voltage to Pin 5

Pin 5 taps the 2/3 Vcc internal reference. Applying an external voltage V_ctrl to pin 5 *overrides* the upper threshold — the capacitor now charges until V_C = V_ctrl instead of 2/3 Vcc. A higher V_ctrl lengthens t_high (longer charge time); a lower V_ctrl shortens it. Feed an audio signal into pin 5 and you get pulse-width modulation proportional to the instantaneous audio amplitude — a crude but functional **class-D-ish** modulator.

```
   Astable (as in §2) + control-voltage modulation on pin 5:

                      R_A          R_B
       Vcc ───/\/\/\───────┬──/\/\/\─┐
                            │         │
                            ● pin 7   │
                            │         │
                            ● pin 6/2 │
                           ─┴─ C      │
                            │         │
                           GND        │
                                      │
   Audio or control ───/\/\/\─────────● pin 5 (CONTROL)
   signal (AC-coupled)                │    (overrides 2/3 Vcc threshold)
                                     0.01 µF
                                      │
                                     GND

   As V_ctrl rises above 2/3 Vcc: t_high grows, duty cycle increases.
   As V_ctrl falls below 2/3 Vcc: t_high shrinks, duty cycle decreases.
   Frequency changes slightly; duty cycle sweeps widely. → PWM output at pin 3.
```

### PWM Dimmer Schematic (LED brightness via R_B pot)

```
                        R_A (1 kΩ)
       Vcc ───/\/\/\───────────┐
                                │
                                ●──── pin 7
                                │
                     R_B = potentiometer (100 kΩ)
              Vcc ───/\/\/\/\───┤    (wiper + one end in series:
                                │     varies effective R_B)
                                ●──── pin 6 + pin 2 (tied)
                                │
                                ─┴─  C (10 nF)
                                │
                               GND

       pin 3 (output) ──[ 220 Ω ]──┬── LED anode
                                    │
                                    LED (cathode)
                                    │
                                   GND

   Varying R_B from 0 to 100 kΩ sweeps duty cycle and LED brightness.
   f = 1.44 / ((1 kΩ + 2·R_B)·10 nF) ≈ 700 Hz – 144 kHz
       (frequency shifts with R_B; acceptable for LED dimming)
```

---

## 5. Worked Examples

### Example 1 — Astable at 1 kHz, ~50% Duty Cycle

Design a 555 astable to run at approximately 1 kHz with a near-50% duty cycle. Given: R_A = 1 kΩ, R_B = 72 kΩ, C = 10 nF.

**Frequency:**

```
f = 1.44 / ((R_A + 2·R_B)·C)
  = 1.44 / ((1000 + 2·72000) · 10×10⁻⁹)
  = 1.44 / ((1000 + 144000) · 1×10⁻⁸)
  = 1.44 / (145000 · 1×10⁻⁸)
  = 1.44 / (1.45×10⁻³)
  = 993 Hz   ≈  1.00 kHz    ✓
```

**Duty cycle:**

```
D = (R_A + R_B) / (R_A + 2·R_B)
  = (1000 + 72000) / (1000 + 144000)
  = 73000 / 145000
  = 0.503   =  50.3%
```

**High and low times:**

```
t_high = 0.693·(R_A + R_B)·C = 0.693·73000·1×10⁻⁸ = 506 µs
t_low  = 0.693·R_B·C         = 0.693·72000·1×10⁻⁸ = 499 µs
T = 1005 µs  →  f = 995 Hz   ✓  (consistent)
```

This is about as close to 50% as the standard topology gets without a diode. For a true 50.0% duty cycle, add a signal diode (1N4148) in parallel with R_B (anode at pin 7, cathode at pin 6/2) so the capacitor charges through R_A *only*, and set R_A = R_B = 144 kΩ.

### Example 2 — Monostable 1-Second Time Delay

Design a monostable 555 to produce a 1.0-second output pulse when triggered. Choose C = 10 µF (electrolytic), then solve for R:

```
T = 1.10·R·C

1.0 s = 1.10 · R · 10×10⁻⁶
R = 1.0 / (1.10 · 1×10⁻⁵)
R = 90 909 Ω   ≈  91 kΩ   (use the E24 standard value)
```

**Verify:**

```
T = 1.10 · 91000 · 10×10⁻⁶ = 1.001 s    ✓
```

**Caveat:** electrolytic capacitors have tolerances of ±20% and leak with temperature, so the actual pulse will be 0.8–1.2 s. For precision timing, use a film or C0G ceramic capacitor (±1–5%), or move to a crystal-referenced counter. For a 10-second or longer delay, an electrolytic becomes unavoidable (the required R would exceed practical values with a small C), and accuracy degrades further — in that regime, a digital counter clocked by a crystal (see [Oscillator Circuits](analog-circuits.oscillator-circuits.md)) is the better solution.

---

## 6. Applications

### LED Flasher (the canonical 555 project)

The first project on every electronics bench: blink an LED at ~1 Hz. R_A = 470 kΩ, R_B = 470 kΩ, C = 1 µF → f ≈ 1 Hz, D = 67%. The LED + 330 Ω resistor goes from pin 3 to ground (or Vcc, depending on whether you want it on during t_high or t_low).

### Time-Delay Relay

Monostable mode driving a transistor + relay: trigger on pin 2 (pushbutton to ground), output on pin 3 drives an NPN transistor base, the transistor switches a relay coil with a freewheeling diode. The relay activates for T = 1.1·R·C after each trigger. Use this for "motor runs for 10 seconds after a button press" or "porch light stays on for 2 minutes."

### Tone Generator

Astable at audio frequencies (300 Hz – 3 kHz): R_A = 1 kΩ, R_B = 72 kΩ, C = 0.1 µF → f ≈ 100 Hz. Drive an 8 Ω speaker through a 100 µF coupling cap and a 220 Ω limiting resistor. Vary R_B (potentiometer) to sweep the pitch — a simple electronic siren. For a two-tone doorbell, use two 555s (or one 556 dual timer) with different timing RC values, gated by the pushbutton.

### Servo PWM

RC hobby servos expect a 50 Hz refresh rate (20 ms period) with a 1.0–2.0 ms high pulse controlling position (1.5 ms = center). This is a 5–10% duty cycle at 50 Hz — well within the 555's range. Drive pin 5 (control voltage) with a potentiometer wiper (0–5 V) to vary the pulse width and thus the servo angle.

---

## Parameter Table — Mode / Formula / Application

| Mode | Timing formula | Typical timing range | Duty cycle | Typical application |
|------|----------------|----------------------|------------|---------------------|
| Astable (free-run) | `f = 1.44 / ((R_A + 2·R_B)·C)` | 1 µs – hours | `D = (R_A+R_B)/(R_A+2·R_B)`, always > 50% | LED flasher, clock source, tone generator, servo PWM |
| Monostable (one-shot) | `T = 1.10·R·C` | 10 µs – ~15 min | single pulse (width = T) | Time-delay relay, pulse stretcher, debouncer, missing-pulse detector |
| Bistable (SR flip-flop) | (no timing — R/C absent) | — | (latched) | Switch debouncer, SRAM-like latching, push-on/push-off toggle |
| PWM via control pin (5) | t_high varies with V_ctrl | (set by astable RC) | 5–95% controllable | Motor speed control, LED dimming, class-D-ish modulation |
| PWM via R_B pot | D varies with R_B | (set by astable RC) | ~50%–95% | Lamp dimmer, fan speed, simple ESC |

## Design Checklist

- [ ] Chosen the mode (astable / monostable / bistable) for the required behavior (oscillate / single pulse / latch).
- [ ] Computed R and C from the timing formula; checked that R is in the practical range (1 kΩ – 10 MΩ) and C is not so small that pin leakage swamps it (< 100 pF) nor so large that electrolytic tolerance dominates (> 100 µF).
- [ ] Verified the duty-cycle requirement; if exactly 50% is needed, added the diode-across-R_B modification.
- [ ] Decoupled pin 5 with a 0.01 µF capacitor to GND (prevents supply-noise jitter on the threshold reference).
- [ ] Confirmed the output load on pin 3 does not exceed 200 mA (bipolar NE555) or 100 mA (CMOS TLC555); added a transistor buffer if driving a relay, motor, or speaker beyond that.
- [ ] For monostable: confirmed the trigger pulse on pin 2 is shorter than the desired output pulse, and that the circuit is not retriggered before C fully discharges.
- [ ] For long timing intervals (> 1 min): considered a CMOS 555 (TLC555, LMC555) for lower leakage, or switched to a crystal-counter scheme for accuracy.
- [ ] Added a freewheeling diode across any inductive load (relay, motor) driven by pin 3 to protect the chip from flyback voltage.


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

## See Also

- [Analog Circuits](analog-circuits.md) — the parent capability hub: scope, progression, and sibling articles.
- [Oscillator Circuits](analog-circuits.oscillator-circuits.md) — the sibling article: the 555 is a precision *relaxation oscillator* (§5 there); this article specializes it into the 8-pin package.
- [Semiconductor Devices](semiconductor-devices.md) — how the 555 IC and its transistors, comparators, and resistors are manufactured on one silicon die.
- [Passive Components](passive-components.md) — the timing resistor R and timing capacitor C that set every interval above (note the electrolytic/film/C0G trade-offs for long vs. precise intervals).
- [AC Analysis](circuit-fundamentals.ac-analysis.md) §2 — the RC charging equation `V_C = V_final·(1 − e^(−t/RC))` from which the 1.10·R·C and 0.693·R·C formulas are derived; this article links rather than re-derives.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
