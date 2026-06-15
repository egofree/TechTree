# DAC Circuits

> **Node ID**: `electronics.interface-circuits.dac-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md),
> [`electronics.passive-components`](passive-components.md)
> **Enables**: None
> **Outputs**: dac-designs
> **Timeline**: Years 30-50
> **Critical**: No — mixed-signal interface pedagogy; the underlying semiconductor and passive-component manufacturing capabilities are the critical prerequisites

This article is the inverse of the companion [ADC Circuits](interface-circuits.adc-circuits.md) article: where that one captures an analog voltage as a digital word, this one **reconstructs** an analog voltage from a digital word. Every DAC maps an N-bit input onto one of `2^N` discrete output voltages spanning `[0, V_ref]`:

```
    V_out = (D / 2^N) × V_ref         where D is the N-bit digital input code (0 .. 2^N − 1)
```

The architectures below — R-2R ladder, weighted-resistor (string), and PWM-filtered — are different ways to realize that mapping. The active building blocks (analog switches, references, output buffers) come from [Semiconductor Devices](semiconductor-devices.md); the precision matched [resistors](passive-components.md) that set the conversion accuracy come from [Passive Components](passive-components.md). This article does **not** re-derive op-amp internals (see [Analog Circuits](analog-circuits.md)) and does **not** cover sensor-specific signal conditioning (a separate article owns that).

---

## 1. The R-2R Ladder

The R-2R ladder is the dominant DAC architecture: it appears inside virtually every monolithic DAC and inside the internal DAC of every SAR ADC. Its genius is that it achieves binary weighting using **only two resistor values** — R and 2R — regardless of resolution. This sidesteps the fabrication nightmare of the weighted-resistor DAC (Section 2), where the MSB and LSB resistors differ by a factor of `2^(N−1)`.

### How it works

The ladder is a chain of identical cells, one per bit. Each cell has a switchable 2R leg connected to either `V_ref` (bit = 1) or ground (bit = 0), plus an R link to the next cell. The "far end" of the ladder is terminated by a final 2R resistor to ground. The topology guarantees that every node sees a Thévenin resistance of exactly R looking either way, so each bit injects a current that is **exactly half** of the bit above it — a binary-weighted current divider.

```
   4-bit R-2R ladder DAC (bits D3..D0, MSB on the left):

     D3=1   D2=1   D1=1   D0=1          switch each bit's 2R leg
       │      │      │      │             to V_ref (1) or GND (0)
       S3     S2     S1     S0
       │      │      │      │
   ┌───┴──┬──┴──┬───┴──┬───┴──┬─── 2R ──┐
   │      │     │      │      │         │
   2R     2R    2R     2R     │         │  ← all resistors are
   │      │     │      │      │         │    only TWO values: R, 2R
   ├──R───┼──R──┼──R───┤      │         │
   │      │     │      │     V_ref bus  │
   │      │     │      │      │         │
                              ▼         ▼
                          summing node  GND
                          (output)

   V_out = (D / 2^N) × V_ref
```

**Why two values suffice:** in a weighted-resistor DAC the MSB current must be `2^(N−1)` times the LSB current, demanding resistors spanning `2^(N−1)` in value — impossible to fabricate with matched precision beyond ~8 bits. The R-2R ladder instead relies on a single **ratio** (2R/R = 2) repeated N times. Trimming one ratio achieves all N binary weights at once, which is why R-2R scales cleanly to 16+ bits while weighted-resistor does not.

### Worked Example: 4-bit R-2R DAC, V_ref = 5 V, digital input `1011` (= 11)

Apply the governing equation directly:

```
    V_out = (D / 2^N) × V_ref
          = (11 / 2^4) × 5.000 V
          = (11 / 16) × 5.000 V
          = 0.6875 × 5.000 V
          = 3.4375 V
```

Bit-by-bit breakdown (each bit contributes a binary-weighted fraction of V_ref to the output):

| Bit | Value | Weight (1/2^position) | Contribution to V_out |
|-----|-------|-----------------------|-----------------------|
| D3 (MSB) | 1 | 1/2 | 5.000 × 0.5 = 2.5000 V |
| D2 | 0 | 1/4 | 0 |
| D1 | 1 | 1/8 | 5.000 × 0.125 = 0.6250 V |
| D0 (LSB) | 1 | 1/16 | 5.000 × 0.0625 = 0.3125 V |
| **Total** | `1011` = 11 | | **3.4375 V** |

The LSB step size is `V_ref / 2^N = 5.000 / 16 = 0.3125 V` — exactly D0's contribution. Stepping the code from 11 (`1011`) to 12 (`1100`) raises the output by 1 LSB from 3.4375 V to 3.7500 V. A practical DAC adds an [op-amp](analog-circuits.md) buffer at the output so the ladder's high impedance does not interact with the load; the buffer is a non-inverting voltage follower with high input impedance and low output impedance.

---

## 2. Weighted-Resistor (String) DAC

The weighted-resistor DAC is the conceptually simplest topology: each bit switches a current of binary weight into a summing node. It is rarely used as a standalone DAC above ~6 bits because of the resistor-spread problem, but it appears in teaching and in some high-speed low-resolution designs.

### Weighted-resistor (binary-weighted current sources)

```
                 V_ref
                   │
          ┌────────┼────────┬────────┬─────
          │        │        │        │
         2R        4R      8R      2^(N)R     ← each bit's resistor
          │        │        │        │           is 2× the previous
          S3       S2       S1       S0         (MSB smallest current)
          │        │        │        │
          └────────┴────────┴────────┴─── summing node ──► [op-amp I/V] ──► V_out
```

**The fatal flaw:** the MSB resistor is R and the LSB resistor is `2^(N−1)·R`. For 8 bits that is a 128:1 spread; for 12 bits, 2048:1. Fabricating resistors that span two to three decades **and** match each other to the required N-bit precision is beyond practical thin-film trimming. If the MSB resistor is off by even 0.5%, the DAC becomes non-monotonic at the major carry (code `0111…` → `1000…`), producing a glitch larger than several LSBs. The R-2R ladder exists precisely to escape this problem.

### String (Kelvin-divider) DAC

A second "string" architecture uses `2^N` equal resistors in series between `V_ref` and ground, with `2^N` analog switches selecting the tap corresponding to the input code. This is inherently **monotonic** (a larger code can only select a higher tap) and needs only one resistor value, but it requires `2^N` resistors and switches — practical only for low resolution (8–10 bits). It is favored as the internal DAC inside some precision SAR ADCs precisely because of its guaranteed monotonicity.

---

## 3. PWM as a DAC

When a dedicated DAC IC is unavailable — on a minimalist microcontroller, or when only one analog output is needed and the bill-of-materials must stay tiny — a **PWM (pulse-width modulation) signal filtered by a low-pass RC network** produces a usable analog voltage. This is the cheapest DAC of all: one digital output pin, one resistor, one capacitor.

### Principle

A PWM signal is a square wave of fixed frequency `f_PWM` whose duty cycle `δ` (fraction of the period that the signal is HIGH) is set by software. Averaging the waveform over many periods recovers a DC level:

```
    V_out = δ × V_CC          (δ = duty cycle, 0 to 1)
```

A simple first-order RC low-pass filter removes the switching ripple:

```
   digital                               ┌─── V_out (analog)
   PWM  ─────────[ R ]───────────────────┤
   pin                                      └─── C ─── GND

   f_c = 1 / (2π·R·C)   should be << f_PWM  (typically f_c ≈ f_PWM / 100)
```

For example, an 8-bit PWM (`δ` adjustable in 1/256 steps) from a 5 V microcontroller pin yields:

| Duty cycle δ | Digital code (8-bit) | V_out = δ × 5 V |
|--------------|----------------------|------------------|
| 0% | 0 | 0.000 V |
| 25% | 64 | 1.250 V |
| 50% | 128 | 2.500 V |
| 75% | 192 | 3.750 V |
| 100% | 255 | 5.000 V |

**Trade-offs:** the RC filter sets a hard **speed/resolution/ripple** triangle. A low cutoff rejects ripple but makes the output slow to settle (time constant τ = RC); a high cutoff tracks fast changes but passes switching ripple. A 2-pole (RC-RC) or 3-pole (active Sallen-Key) filter dramatically improves the ripple/settling trade-off — these are pure [op-amp](analog-circuits.md) techniques. PWM-DAC accuracy is also bounded by the pin's logic-high voltage (`V_oh` varies with supply tolerance and load) and by the digital PWM resolution (`δ` step size). For lab-grade precision, a real DAC wins decisively; for a single setpoint or slow control voltage, PWM is hard to beat on cost.

---

## 4. Static and Dynamic Specifications

A DAC's data sheet specifies both **static** (DC) and **dynamic** (AC) performance. The static specs govern DC accuracy; the dynamic specs govern how quickly and cleanly the output moves between levels.

### Static specifications

| Parameter | Definition | Why it matters |
|-----------|------------|----------------|
| **Resolution** | N bits → `2^N` output levels | Smallest step size = `V_ref / 2^N` |
| **Offset error** | Output at code 0 (ideally 0 V) | Systematic DC shift; trimmable |
| **Gain error** | Slope of V_out vs. code differs from ideal | Full-scale span error; trimmable |
| **INL** (integral nonlinearity) | Max deviation of V_out from the ideal straight line | Uncorrectable linearity floor; limits AC spectral purity |
| **DNL** (differential nonlinearity) | Max deviation of any single step from 1 LSB | If DNL ≥ −1 LSB → **non-monotonic** (a code increase can decrease V_out) |
| **Monotonicity** | V_out never decreases as code increases | Mandatory for closed-loop control — a non-monotonic DAC causes servo lockup |

**Monotonicity** is the single most important static spec for a DAC in a feedback loop. A non-monotonic DAC (typically caused by a overweighted MSB in a weighted-resistor network) inverts the loop sign at the major carry, causing the controller to hunt or oscillate. The R-2R ladder and the Kelvin string are monotonic by construction when trimmed to ≤½ LSB DNL; the weighted-resistor DAC is not.

### Dynamic specifications

| Parameter | Definition | Why it matters |
|-----------|------------|----------------|
| **Settling time** | Time from a code step to V_out staying within ±½ LSB of final | Limits maximum update rate; critical for waveform generation |
| **Glitch energy** | Area (V·s) of the transient spike at a code transition | Caused by switch timing skew; corrupts fast waveform reconstruction |
| **Glitch impulse** | Peak amplitude of the transition transient | Worst at the major carry (`0111…` ↔ `1000…`) where many bits switch |
| **Update rate** | Maximum code-to-code frequency | Bounded by settling time; sets max output frequency (≈ update rate / 4 for a sine) |

**Settling time** is dominated by the output amplifier's slew rate and the RC of the ladder plus any load capacitance. A high-speed DAC may settle to 16 bits in under 100 ns; a precision DAC may take 10 µs to settle to the same accuracy.

**Glitch energy** is the dynamic signature of a DAC. When several bits switch at once (worst at the major carry), tiny timing skews between the internal analog switches produce a brief but large output spike — often many LSBs tall — before the output settles. The glitch's area, not its peak, is what matters because it injects spurious spectral energy into the reconstructed waveform. The standard remedies are **deglitcher** sample-and-hold circuits (which disconnect the output during the switch transition and re-sample after settling) and **segmented architectures** (which decode the upper bits thermometrically so the major carry never switches many current sources at once).

---

## DAC Parameter Reference

| DAC type | Resolution | Settling time | Power (typ.) | Monotonic? | Typical application |
|----------|-----------|---------------|--------------|------------|---------------------|
| **R-2R ladder** | 8–18 bit | 0.1–10 µs | µW – tens of mW | Yes (trimmed) | General-purpose, audio, industrial control, internal DAC in SAR ADCs |
| **Weighted-resistor** | 4–8 bit | 10–100 ns | mW | Poor (non-monotonic at major carry) | Teaching, ultra-fast low-resolution |
| **String (Kelvin divider)** | 8–10 bit | 0.1–1 µs | mW – tens of mW | **Guaranteed** | Precision SAR ADC internals, high-reliability |
| **Segmented** (thermometric + binary) | 12–16 bit | 10–100 ns | tens – hundreds of mW | Yes | High-speed video, arbitrary waveform generators, communications |
| **Current-steering** (binary-weighted current sources) | 10–16 bit | 1–20 ns | tens of mW – W | With segmentation | RF/IF signal synthesis, high-speed instrumentation |
| **PWM-filtered** (microcontroller) | 8–12 bit (effective) | ms (filter-limited) | ~0 (µW) | Yes (inherently) | Cheap setpoints, slow control voltages, single-channel outputs |

The selection rule of thumb: **general-purpose → R-2R; need guaranteed monotonicity at low resolution → Kelvin string; need speed → current-steering or segmented; need one cheap slow output → PWM.** R-2R covers the broad middle for the same reason SAR dominates the ADC world: its resolution/speed/power compromise fits most applications, and its two-value resistor topology keeps the silicon cheap.

### Design Heuristics

| Design goal | Recommended architecture | Why |
|-------------|--------------------------|-----|
| Audio output (20 kHz, 16–24 bit) | R-2R or segmented current-steering | R-2R for audio DACs; segmented for low glitch energy |
| Programmable setpoint (DC, slow) | R-2R or PWM-filtered | PWM if no DAC pin available; R-2R for precision |
| Arbitrary waveform generator (1 MHz) | Current-steering (segmented) | Fast settling + low glitch for clean reconstruction |
| Closed-loop control (must be monotonic) | R-2R or Kelvin string | Guaranteed monotonicity prevents servo lockup |
| One analog output on a minimal MCU | PWM + RC filter | Zero extra parts; accuracy bounded by V_CC and filter |

---

## Prerequisites

- [Semiconductor Devices](semiconductor-devices.md) — the analog switches (CMOS transmission gates) that steer each bit's leg of the ladder to V_ref or ground, the precision bandgap references that set V_ref, and the output-buffer op-amps.
- [Passive Components](passive-components.md) — the thin-film matched resistor networks (R and 2R) that set the conversion accuracy; R-2R ladders demand ≤0.1% matching for 10-bit linearity, ~0.01% for 14 bits.
- [Analog Circuits](analog-circuits.md) — op-amp output buffers, active reconstruction (smoothing) filters, and deglitcher sample-and-hold circuits (no op-amp internals re-derived here).
- [Interface Circuits](interface-circuits.md) — parent capability; the conversion-fundamentals progression and the system-level signal chain.

## Scope Boundary

This article covers the **conversion architectures** — R-2R ladder, weighted-resistor/string, PWM-as-DAC, and the static/dynamic specs that govern them. It does **not** cover:

- **ADC design** (the inverse conversion) — see the companion [ADC Circuits](interface-circuits.adc-circuits.md) article. Note that every SAR and sigma-delta ADC *contains* an internal DAC, almost always an R-2R ladder or Kelvin string taught here.
- **Reconstruction (smoothing) filter design in depth** — the analog low-pass that follows a DAC to remove the sample-and-hold image is an [Analog Circuits](analog-circuits.md) topic; this article states the requirements but does not re-derive active filter synthesis.
- **Sensor-specific signal conditioning** — owned by the sibling sensor-circuits article.
- **Processor-side waveform generation** — direct digital synthesis (DDS) phase accumulators, DMA streaming to the DAC register — covered under [Computing: embedded systems](../computing/embedded-systems.md).

---


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
