# ADC Circuits

> **Node ID**: `electronics.interface-circuits.adc-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md),
> [`electronics.passive-components`](passive-components.md)
> **Enables**: None
> **Outputs**: adc-designs
> **Timeline**: Years 30-50
> **Critical**: No — mixed-signal interface pedagogy; the underlying semiconductor and passive-component manufacturing capabilities are the critical prerequisites

This article is one half of the analog/digital bridge covered in [Interface Circuits](interface-circuits.md): where the companion [DAC Circuits](interface-circuits.dac-circuits.md) article teaches how to reconstruct an analog voltage from a digital word, this article teaches the inverse — how to capture a continuous analog voltage as a finite digital number. Every ADC performs two coupled operations: **sampling** (freezing a time-varying signal into discrete time points) and **quantization** (rounding each sample's amplitude onto a finite ladder of levels). The art of ADC design is choosing an architecture whose sampling rate, resolution, and power budget match the application.

The active building blocks — [comparators](analog-circuits.md), analog switches, precision references — come from [Semiconductor Devices](semiconductor-devices.md); the precision matched [resistors](passive-components.md) that build the internal DAC ladders and integration networks come from [Passive Components](passive-components.md). This article does **not** re-derive op-amp internals (see [Analog Circuits](analog-circuits.md)) and does **not** cover sensor-specific signal conditioning (a separate article owns that).

---

## 1. Sampling and the Nyquist Limit

A continuous signal `x(t)` must be observed at discrete instants `t = n·T_s` before any ADC can quantize it. The sample rate is `f_s = 1/T_s`. The fundamental theorem that governs this step is the **Nyquist–Shannon sampling theorem**:

> If a signal contains no energy above frequency `f_max`, it is fully represented by samples taken at rate `f_s ≥ 2·f_max`. The minimum rate `2·f_max` is the **Nyquist rate**.

Sample slower than this and the spectral replicas above `f_s/2` fold back into the baseband — an irreversible corruption called **aliasing**. Once a signal is aliased, no amount of digital processing can recover the original. The defense is an **anti-alias filter** (an analog low-pass filter) placed *before* the sampler that attenuates everything above `f_s/2` to below the quantization noise floor.

```
                  anti-alias          S/H          quantizer      encoder
  x(t)  -----> [ LPF ] ------> [ sample/ ] ------> [ flash or ] ---> [ N-bit ]
  analog         f_c <          [ hold ]          [ SAR or   ]      [ word ]
                 f_s/2                            [ ... ]           digital
```

The trade-off is fundamental: faster sampling eases the anti-alias filter (a gentler roll-off suffices) but demands a faster ADC and more digital storage; slower sampling allows a cheap ADC but forces a steep, expensive analog filter. Oversampling converters (Section 5) exploit headroom in `f_s` to trade speed for resolution via noise shaping.

### Quantization

Sampling fixes the **time** axis; quantization fixes the **amplitude** axis. An N-bit ADC maps each sample onto one of `2^N` discrete levels spanning the input range `[0, V_ref]`. The size of one step — the **LSB (least significant bit)** voltage — is:

```
    V_LSB = V_ref / 2^N
```

Because the continuous input can fall anywhere within a step, every conversion incurs up to ±½ LSB of **quantization error** — an irreducible error floor that no amount of analog precision can remove. The quantization error behaves like white noise spread uniformly across `[−V_LSB/2, +V_LSB/2]`, giving a theoretical **signal-to-quantization-noise ratio** for a full-scale sine wave of:

```
    SQNR = 6.02·N + 1.76   dB
```

Each extra bit buys ~6 dB of dynamic range. The table below makes the resolution concrete:

| Bits N | Levels (2^N) | LSB at V_ref=5V | SQNR (full-scale sine) | Typical use |
|--------|--------------|-----------------|------------------------|-------------|
| 8 | 256 | 19.53 mV | 50 dB | Video, simple sensors |
| 10 | 1 024 | 4.88 mV | 62 dB | Microcontroller ADCs |
| 12 | 4 096 | 1.22 mV | 74 dB | Industrial measurement |
| 16 | 65 536 | 76.3 µV | 98 dB | Audio, precision DMMs |
| 24 | 16 777 216 | 0.30 µV | 146 dB | High-resolution sigma-delta |

Resolution beyond ~16 bits in the raw converter is meaningless unless the analog front-end noise is below V_LSB — at 24 bits the LSB is sub-microvolt, below the thermal noise of any practical resistor. The architectures below exist to navigate this resolution/speed/power triangle.

---

## 2. SAR (Successive Approximation Register)

The SAR ADC is the workhorse of the mid-range: 8–16 bits, 100 kSPS to a few MSPS, microwatts of power. It converts one bit per clock cycle by performing a **binary search** over the input range. The name comes from the Successive Approximation Register that controls the search — a digital logic block that converges on the answer in exactly N cycles regardless of the input value.

### Architecture

```
                      V_ref
                        │
                     ┌──┴──┐
                     │ N-bit│ ◄── code under test from SAR register
                     │ DAC  │
                     └──┬──┘
                        │  V_DAC (trial voltage)
                        │
   V_in ─────────────►┌─┴─┐
                      │ CMP│  comparator: V_in >= V_DAC ?
                      └─┬─┘
                        │  decision (1 bit)
                        │
                     ┌──┴──┐
                     │ SAR │  successive approximation register
                     │ logic│  N+1 clocks → final N-bit result
                     └─────┘
                        │
                        ▼
                     N-bit output word
```

Each conversion proceeds as follows, starting from the MSB:

1. SAR sets the MSB (D_{N-1}) to 1; the DAC outputs the midpoint voltage `V_ref/2`.
2. The comparator reports whether `V_in ≥ V_DAC`. If yes, the bit stays 1; if no, it is cleared to 0.
3. SAR moves to the next bit down, sets it to 1, and repeats — halving the search window each time.
4. After N decisions, the register holds the digital word whose DAC output is the largest level not exceeding `V_in`.

A sample-and-hold (S/H) circuit freezes `V_in` for the full N cycles so the input does not change mid-conversion. The internal DAC is almost always an R-2R ladder (see [DAC Circuits](interface-circuits.dac-circuits.md)); the comparator is a high-gain [op-amp](analog-circuits.md) differential stage; the analog switches that reconfigure the ladder are the [semiconductor devices](semiconductor-devices.md) this process depends on.

### Worked Example: 8-bit SAR conversion of 3.2 V with V_ref = 5 V

First compute the LSB size and the target code:

```
    V_LSB = V_ref / 2^N = 5.000 / 256 = 19.531 mV
    Expected code ≈ V_in / V_LSB = 3.200 / 0.019531 = 163.84 → code 163
```

Now step through the eight bit decisions. At each step the SAR sets the test bit to 1 (keeping previously decided bits), the DAC produces the trial voltage, and the comparator decides keep (1) or clear (0):

| Step | Test bit | Test code (binary) | Decimal | V_DAC = code × V_LSB (V) | V_in ≥ V_DAC? | Decision |
|------|----------|--------------------|---------|---------------------------|---------------|----------|
| 1 | D7 | `10000000` | 128 | 2.500 | YES (3.20 ≥ 2.50) | **D7 = 1** |
| 2 | D6 | `11000000` | 192 | 3.750 | NO (3.20 < 3.75) | D6 = 0 |
| 3 | D5 | `10100000` | 160 | 3.125 | YES (3.20 ≥ 3.125) | **D5 = 1** |
| 4 | D4 | `10110000` | 176 | 3.438 | NO (3.20 < 3.438) | D4 = 0 |
| 5 | D3 | `10101000` | 168 | 3.281 | NO (3.20 < 3.281) | D3 = 0 |
| 6 | D2 | `10100100` | 164 | 3.203 | NO (3.20 < 3.203) | D2 = 0 |
| 7 | D1 | `10100010` | 162 | 3.164 | YES (3.20 ≥ 3.164) | **D1 = 1** |
| 8 | D0 | `10100011` | 163 | 3.184 | YES (3.20 ≥ 3.184) | **D0 = 1** |

**Result: `10100011` = 163**, reconstructed as 163 × 19.531 mV = **3.184 V**. The quantization error is 3.200 − 3.184 = **16 mV**, comfortably within ±½ LSB (9.77 mV would be the half-LSB ideal; the residual reflects that 3.2 V sits near the top of code 163's bin). The conversion took exactly 8 clock cycles, independent of the input value — the defining efficiency of binary search.

---

## 3. Flash (Parallel) ADC

The flash ADC is the fastest architecture and the most profligate with hardware. It quantizes the input in a **single step** by holding `2^N − 1` comparators in parallel, each biased at a different threshold by a resistor string from `V_ref` to ground. A thermometer-to-binary encoder then converts the comparator outputs into an N-bit word.

### Architecture

```
                  V_ref
                    │
              R ────┬──── threshold_1 ──► CMP_1 ──┐
              R ────┼──── threshold_2 ──► CMP_2 ──┤
              R ────┼──── threshold_3 ──► CMP_3 ──┤   (2^N − 1 = 15
              R ────┤      ...          ...      │    comparators for
              R ────┤      ...          ...      │    an N = 4 bit ADC)
              R ────┴──── threshold_15 ─► CMP_15─┘
                                         │
   V_in ─────────────────────────────►(+) all comparators share V_in
                                         │
                                    [ thermometer ]
                                    [   to binary  ]
                                    [   encoder    ]
                                         │
                                         ▼
                                      N-bit word
```

The name "thermometer" comes from the output pattern: for an input of level k, comparators 1 through k read HIGH and the rest read LOW — a one-fill (like mercury rising in a thermometer). The encoder is pure combinational logic.

**The cost:** an N-bit flash ADC needs `2^N − 1` comparators plus `2^N` resistors. Resolution is brutally hardware-limited:

| Bits N | Comparators (2^N − 1) | Resistors (2^N) | Practical? |
|--------|-----------------------|-----------------|------------|
| 4 | 15 | 16 | Yes — common |
| 6 | 63 | 64 | Yes |
| 8 | 255 | 256 | Yes — large die |
| 10 | 1023 | 1024 | Rare — huge, hot |
| 12 | 4095 | 4096 | never |

Doubling resolution doubles the die area, the input capacitance (which loads the signal source), and the power. This is why flash ADCs are almost always 6–8 bits. For higher resolution at near-flash speed, designers chain two or three low-resolution flash stages in a **pipelined** or **sub-ranging** converter — each stage resolves a few bits, subtracts the resolved voltage via an internal DAC, amplifies the residue, and passes it to the next stage. That trades latency (several clock cycles of pipeline delay) for resolution.

---

## 4. Dual-Slope / Integrating ADC

The integrating ADC is the precision instrument's converter: slow (a few to a few hundred samples per second) but extraordinarily accurate and inherently noise-rejecting. It is the architecture inside every benchtop [digital multimeter](test-equipment.md).

### Operating principle

A dual-slope converter integrates the **unknown** input voltage for a fixed number of clock counts, then integrates a **known** reference voltage of opposite polarity until the integrator output returns to zero. The ratio of the two integration times is the digital result:

```
   Step 1 (fixed time T1):     integrate V_in  →  ramp UP to V_peak
   Step 2 (measured time T2):  integrate −V_ref →  ramp DOWN to zero

   V_in × T1 = V_ref × T2   →   V_in = V_ref × (T2 / T1)
```

```
    V_in ──[ switch ]──┐            ┌──[ switch ]── V_ref (opposite sign)
                       │            │
                       ▼            ▼
                    ┌──────────────────┐
                    │  integrator      │──── V_integ ────► comparator ──► zero-cross
                    │  (op-amp + C)    │                                  │
                    └──────────────────┘                                  │
                                                                         ▼
                              counter counts clock during T2 → N-bit word
```

Because the result is a **ratio of two time intervals measured with the same clock**, the long-term stability of the clock and the absolute value of the integration capacitor cancel out — only the reference voltage's accuracy survives. Furthermore, the fixed-count integration time `T1` can be chosen to reject mains interference exactly: setting `T1 = 20 ms` (50 Hz) or `16.67 ms` (60 Hz) places a notch at the line frequency, rejecting hum by 60 dB or more. This is why a 4½-digit DMM reads steadily even in a noisy lab.

**Trade-off:** each conversion takes `T1 + T2`, typically tens to hundreds of milliseconds. Dual-slope ADCs are limited to ~10–300 SPS — useless for audio or video, ideal for a DMM measuring a stable DC voltage.

---

## 5. Sigma-Delta (ΣΔ) ADC

The sigma-delta converter trades extreme oversampling and digital signal processing for high resolution at modest speed — it dominates audio (16–24 bit, 48–192 kHz) and precision industrial measurement (24-bit, low SPS). A 1-bit ADC (just a comparator) runs at a rate `f_oversample` far above the Nyquist rate; a feedback loop and digital **decimation filter** average the 1-bit stream down to a high-resolution N-bit word at the output rate.

### Architecture

```
                                      ┌──────────────┐
   V_in ─►(+)──►[ integrator ]──►(+)──┤  1-bit       │── bitstream ──┬──►[ decimation ]──► N-bit
            ▲ └─── dither/quantizer   │  quantizer   │               │    [  filter   ]    word
            │         (1-bit DAC)     │  (comparator)│               │
            │                          └──────────────┘               │
            │                                                         │
            └────────────── 1-bit feedback DAC ◄─────────────────────┘
```

Two mechanisms give the sigma-delta its resolution:

1. **Oversampling.** Sampling at `f_oversample = R · f_Nyquist` (oversampling ratio R, typically 64–1024) spreads the quantization noise over a much wider band, so the in-band noise falls by 3 dB per octave of oversampling (½ bit per doubling of R).
2. **Noise shaping.** The integrator in the feedback loop **pushes** quantization noise up to high frequencies, out of the band of interest. A first-order loop gives ~9 dB/octave (1.5 bits) of in-band improvement per doubling; second- and third-order loops give far more.

The decimation filter (a digital low-pass + downsampler) then discards everything above the signal band — taking the high-frequency noise with it — and outputs a high-resolution word at the final sample rate. The result is a converter that achieves 20–24 bits of resolution with a 1-bit quantizer, something no other architecture can match at audio bandwidths.

**Trade-off:** the decimation filter introduces latency (often many output sample periods), making sigma-delta poor for control loops that need deterministic, low-latency conversion. It is also computationally heavy — the decimation filter is a substantial digital block, economical only on an IC.

---

## ADC Parameter Reference

| ADC type | Resolution | Speed (SPS) | Power (typ.) | Latency | Typical application |
|----------|-----------|-------------|--------------|---------|---------------------|
| **Flash** (parallel) | 6–8 bit | 10 M – 1 G | 100 mW – several W | 1 cycle | Oscilloscopes, radar, high-speed video |
| **Pipeline** (sub-ranging) | 8–16 bit | 1 M – 500 M | 20–500 mW | A few cycles (pipeline delay) | Communications, medical imaging, HD video |
| **SAR** | 8–18 bit | 100 k – 10 M | µW – tens of mW | N cycles (deterministic) | General-purpose, MCU ADCs, DAQ, battery systems |
| **Sigma-delta** | 16–32 bit | 10 – few M | mW – tens of mW | Many samples (filter delay) | Audio, precision industrial, weight/pressure sensors |
| **Dual-slope / integrating** | 16–24 bit (DMM-grade) | 1 – 300 | mW | T1 + T2 (tens of ms) | Digital multimeters, panel meters, slow DC |

The selection rule of thumb: **need speed → flash or pipeline; need a balanced general-purpose converter → SAR; need audio/precision resolution → sigma-delta; need line-noise-rejecting DC accuracy → dual-slope.** SAR covers ~80% of all applications by volume because its resolution/speed/power compromise fits the broad middle.

### Design Heuristics

| Design goal | Recommended architecture | Why |
|-------------|--------------------------|-----|
| Digitize a sensor at 1–100 kSPS, 10–12 bit | SAR | Best power/perf at mid-range; deterministic latency suits control |
| Audio line-in (20 kHz, 16–24 bit) | Sigma-delta | Noise shaping delivers the bits at audio bandwidths |
| 50/60 Hz industrial measurement, 16+ bit | Dual-slope or sigma-delta | Fixed integration time rejects mains hum |
| Digitize a 100 MHz signal (oscilloscope) | Flash or pipeline | Only parallel architectures reach hundreds of MSPS |
| Battery data-logger, 8–12 bit | SAR | Sub-microwatt standby, single-cycle wakeup |

---

## Prerequisites

- [Semiconductor Devices](semiconductor-devices.md) — the comparators that drive SAR and flash logic, the analog switches that reconfigure internal DACs and integrators, and the precision bandgap references that set V_ref.
- [Passive Components](passive-components.md) — the precision matched resistors of the flash string and the internal R-2R DAC ladder, plus the low-leakage integration capacitor in dual-slope converters.
- [Analog Circuits](analog-circuits.md) — op-amp integrators, comparators, and the active anti-alias filters that precede every sampler (no op-amp internals re-derived here).
- [Interface Circuits](interface-circuits.md) — parent capability; the conversion-fundamentals progression and the system-level signal chain.

## Scope Boundary

This article covers the **conversion architectures** — sampling, quantization, and the SAR / flash / integrating / sigma-delta topologies. It does **not** cover:

- **Sensor-specific signal conditioning** — thermocouple cold-junction compensation, strain-gauge bridge excitation, photodiode transimpedance — owned by the sibling sensor-circuits article.
- **Op-amp and comparator internals** — biasing, frequency response, slew rate — see [Analog Circuits](analog-circuits.md).
- **DAC design** (the inverse conversion) — see the companion [DAC Circuits](interface-circuits.dac-circuits.md) article. Note that every SAR and sigma-delta ADC *contains* an internal DAC; the R-2R ladder it uses is taught there.
- **Processor-side data handling** — DMA, interrupt service routines, digital filtering of converted samples — covered under [Computing: embedded systems](../computing/embedded-systems.md).

---


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
