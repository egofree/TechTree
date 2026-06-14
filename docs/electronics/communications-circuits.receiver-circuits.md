# Receiver Circuits

> **Node ID**: `electronics.communications-circuits.receiver-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md), [`electronics.communications-circuits.modulation-circuits`](communications-circuits.modulation-circuits.md)
> **Timeline**: Years 20-40
> **Outputs**: receiver-circuit-designs
> **Critical**: No — receiver pedagogy extends communications design into signal recovery; not on the minimum-viable bootstrap critical path

A receiver does the opposite of a transmitter: it captures a tiny modulated RF signal from an antenna, amplifies it, selects the desired station from dozens sharing the band, strips the modulation off the carrier, and amplifies the resulting audio to drive a speaker. The transmitter asks "how do I put information on a wave?"; the receiver asks "how do I get it back, when the wave arriving at my antenna is one millionth of a volt and buried in a dozen other signals a hundred times stronger?"

This article is the **Forrest Mims III / Communications Projects** level. It covers the two receiver architectures that matter — the simple **tuned-radio-frequency (TRF)** receiver and the brilliant **superheterodyne** that every commercial radio has used since the 1930s — plus the supporting circuits (image rejection, FM demodulation, AGC). The modulation and demodulation *theory* — envelope detection, slope detection, the PLL — is fully covered in [Modulation Circuits](communications-circuits.modulation-circuits.md); **we link rather than re-teach it.** The RF oscillator that drives the superhet's local oscillator is covered in [RF Oscillator Circuits](communications-circuits.rf-oscillator-circuits.md).

This article does **not** cover advanced RF engineering techniques. Those belong to a specialized track well beyond the bootstrap horizon.

---

## 1. The TRF (Tuned Radio Frequency) Receiver

The simplest receiver is a chain of identical-tuned amplifiers followed by a detector and an audio amplifier. This is the **TRF** — the architecture of the earliest tube radios (1910s–1920s), and of the crystal set that precedes even the amplifier stage.

```
   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
   │ antenna  │───►│  tuned   │───►│  tuned   │───►│ detector │───►│  audio   │
   │  (wire + │    │ RF amp   │    │ RF amp   │    │ (diode + │    │  amp →   │
   │  ground) │    │ (LC #1)  │    │ (LC #2)  │    │   RC)    │    │ speaker  │
   └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘

   Each LC stage is tuned to f_c (the desired station).
   Multiple tuned stages sharpen selectivity.
   Detector: envelope diode — see Modulation Circuits §3.
```

### How It Works

1. **Antenna** captures RF energy across the whole band. A long wire (≥ λ/4) or a loopstick picks up the electric/magnetic field of every transmitter in range.
2. **Tuned RF amplifier** (one or more stages, each with an LC tank) selects and amplifies only the desired station frequency `f_c`. Each stage contributes gain (more sensitivity) and another LC resonance (sharper selectivity). The tanks are "ganged" — they share a common tuning shaft so they all track the same frequency.
3. **Detector** recovers the audio envelope from the amplified RF. For AM this is a simple diode + RC envelope detector (fully derived in [Modulation Circuits §3](communications-circuits.modulation-circuits.md)). For FM it would be a slope detector or discriminator ([Modulation Circuits §5](communications-circuits.modulation-circuits.md)).
4. **Audio amplifier** boosts the detector output to speaker level. A single-transistor class-A stage or an LM386 audio IC suffices for headphones or a small speaker.

### Why the TRF Was Replaced

The TRF has two fatal flaws that drove its replacement by the superheterodyne within a decade of its commercialization:

**Sensitivity is poor.** Each RF amplifier stage must operate at the carrier frequency `f_c` — which, in the AM band, is anywhere from 530 to 1710 kHz. Building a stable, high-gain amplifier that tracks across a 3:1 frequency range is hard: the transistor's gain drops at higher frequencies, the LC tanks must all be retuned in sync, and the whole chain is prone to oscillation (unwanted feedback between stages via stray capacitance).

**Selectivity varies across the band.** The bandwidth of an LC tank is `BW = f₀/Q` (see [RF Oscillator Circuits §2](communications-circuits.rf-oscillator-circuits.md)). At the low end of the AM band (530 kHz, Q = 100), `BW = 5.3 kHz` — excellent, a single station. At the high end (1710 kHz, same Q), `BW = 17.1 kHz` — two adjacent stations overlap. The TRF's selectivity is 3× better at the bottom of the band than at the top. This asymmetry is inherent and cannot be fixed by better design — it is a property of fixed-Q tuned circuits.

The superheterodyne, invented by Edwin Armstrong in 1918, solves both problems at once by **moving the signal to a fixed frequency** where gain and selectivity are optimized once and for all.

### The Crystal Radio — The Ultimate TRF

The simplest possible receiver strips out all the amplifiers: just antenna → tuned LC → diode detector → headphones. This is the **crystal radio** — it needs *no power supply at all*. The RF energy captured by the antenna drives the high-impedance headphones directly. With a good antenna (15 m of wire, high up) and a solid earth ground, a crystal set will receive strong local AM stations clearly. It was the first radio most rural households owned, and it is the ideal Mims-level first build.

---

## 2. The Superheterodyne Receiver

The **superheterodyne** ("superhet") is the architecture of every commercial radio, television, radar, and cell-phone receiver built since the 1930s. Armstrong's insight was to **mix** the incoming RF signal with a tunable **local oscillator (LO)** to produce a fixed **intermediate frequency (IF)** — and do all the heavy lifting (gain, selectivity) at that fixed IF.

```
   ┌────────┐   ┌────────┐         ┌───────┐   ┌────────┐   ┌────────┐   ┌────────┐
   │antenna │──►│  RF    │──►(●)──►│ mixer │──►│   IF   │──►│detector│──►│  AF    │
   │        │   │  amp + │   ↑     │       │   │  amp   │   │ (AM/FM)│   │  amp → │
   └────────┘   │pre-    │   │ RF  └───┬───┘   │ (fixed │   └────────┘   │speaker │
                │selector│   │         │       │  freq) │                └────────┘
                └────────┘   │         │       │ 455 kHz│
                             │    ┌────┴────┐  │or 10.7M│
                             │    │  local  │  │   Hz   │
                             └───►│oscillator│ └────────┘
                                  │ (VFO)   │
                                  │tunable  │
                                  └─────────┘

   f_LO − f_RF = f_IF   (fixed)
   Tuning the LO shifts ANY station to the SAME IF frequency.
```

### How It Works — Step by Step

1. **Antenna → RF amplifier + preselector.** A single tuned RF stage amplifies the whole band weakly, and a tunable LC **preselector** rejects stations far from the desired one (important for image rejection — §3 below). This stage is NOT the main source of selectivity — it just gets the signal to a usable level and rejects gross interference.

2. **Mixer.** The incoming RF signal at `f_RF` is multiplied by the local oscillator signal at `f_LO`. Multiplication in time produces sum and difference frequencies (the heterodyne — derived in [Modulation Circuits §6](communications-circuits.modulation-circuits.md)). The mixer output contains signals at `|f_LO ± f_RF|`.

3. **IF amplifier.** A fixed-tuned amplifier (or several cascaded stages) selects only the **difference** frequency `f_LO − f_RF = f_IF` and amplifies it enormously. Because the IF is *fixed* (455 kHz for AM, 10.7 MHz for FM), the IF filter can be optimized once — sharp, stable, high-gain. This is the genius of the superhet: **all the selectivity and most of the gain live at a single fixed frequency**, regardless of what station you are tuned to.

4. **Detector.** Demodulates the IF signal — recovers AM envelope or FM frequency deviation. Detection theory is in [Modulation Circuits](communications-circuits.modulation-circuits.md); here we just note *where* it happens: after the IF chain, on the fixed-frequency signal. This means the detector is also optimized for one frequency and never needs to tune.

5. **Audio (AF) amplifier.** Boosts the detector output to speaker level.

### Worked Example — Receiving a 1000 kHz AM Station

You want to listen to a station broadcasting at 1000 kHz (top of the AM band in most regions). The standard AM intermediate frequency is **455 kHz**.

**Step 1: Set the local oscillator.** The LO runs *above* the signal frequency by exactly the IF:

```
   f_LO = f_RF + f_IF
        = 1000 kHz + 455 kHz
        = 1455 kHz
```

**Step 2: The mixer produces the IF.** The mixer multiplies the 1000 kHz signal by the 1455 kHz LO. The difference frequency is:

```
   f_IF = f_LO − f_RF = 1455 − 1000 = 455 kHz      ✓
```

The 455 kHz IF signal carries the *same audio modulation* that was on the original 1000 kHz carrier — the mixer shifts it down in frequency without changing the modulation content.

**Step 3: IF amplification and detection.** The 455 kHz IF signal passes through 2–3 stages of IF amplification (transformer-coupled, fixed-tuned to 455 kHz), accumulating 60–80 dB of gain with sharp selectivity. The envelope detector ([Modulation Circuits §3](communications-circuits.modulation-circuits.md)) then strips the 455 kHz carrier, leaving the audio.

**Step 4: Tuning to a different station.** To listen to 1200 kHz instead, you retune the LO to `1200 + 455 = 1655 kHz` and simultaneously retune the RF preselector to 1200 kHz. The IF stays at 455 kHz — the IF amplifier and detector do not change. This is why a superhet tracks beautifully across the whole band: the hard parts (selectivity, gain, detection) are fixed, and only the LO and preselector tune.

### Why the IF Is Brilliant

The superhet's elegance is that it decouples **selectivity** from **tuning frequency**:

| Property | TRF (tuned at f_RF) | Superhet (fixed at f_IF) |
|----------|---------------------|--------------------------|
| Selectivity | Varies across band (BW = f₀/Q) | Constant — IF filter fixed at 455 kHz |
| Bandwidth at low end (530 kHz) | 5.3 kHz (Q=100) | 10 kHz (set by IF filter) |
| Bandwidth at high end (1710 kHz) | 17.1 kHz (Q=100) | 10 kHz (same IF filter) |
| IF filter technology | N/A | Ceramic resonator or mechanical filter: sharp, stable |
| Gain accumulation | Hard (each stage at f_RF, oscillation risk) | Easy (IF stages are transformer-coupled, stable, identical) |

The IF amplifier uses **transformer-coupled** stages: each transistor drives a tuned transformer primary, and the secondary feeds the next stage. The transformers provide impedance matching, DC isolation, and (because they are tuned to 455 kHz) selectivity. The canonical AM-radio IF can is a metal-shielded transformer with a ferrite slug for fine-tuning to exactly 455 kHz during alignment. Three IF stages (three cans in a row, visible in any 1960s transistor radio) give 60–80 dB of gain at a single frequency with rock-stable selectivity — impossible with tunable TRF stages.

The **455 kHz** value for AM was chosen by international convention: it is high enough above the audio band that the IF signal is easy to filter, low enough that the IF stages are stable and the transformers are compact, and far enough from the image frequency (see next section) that the preselector can reject the image. For FM broadcast, the standard IF is **10.7 MHz** — chosen similarly for the 88–108 MHz FM band.

---

## 3. Image Frequency Rejection

The superhet has one design challenge the TRF does not: the **image frequency**. The mixer produces the IF from *any* signal that is 455 kHz away from the LO — and there are two such frequencies, one above and one below the LO.

```
   Desired:   f_LO − f_desired = f_IF     →   f_desired = f_LO − f_IF
   Image:     f_image − f_LO = f_IF       →   f_image  = f_LO + f_IF

   Since f_LO = f_desired + f_IF:
   f_image = f_desired + 2·f_IF
```

### Worked Example — Image at 1910 kHz

Tuning to a 1000 kHz station (LO = 1455 kHz, IF = 455 kHz). The image frequency is:

```
   f_image = f_desired + 2·f_IF
           = 1000 kHz + 2 × 455 kHz
           = 1000 + 910
           = 1910 kHz
```

Any station broadcasting at 1910 kHz will *also* mix with the 1455 kHz LO to produce a 455 kHz IF signal — and the IF amplifier cannot tell the two apart. You would hear both stations superimposed: a howling heterodyne whistle as their carriers beat against each other.

**Solution: the RF preselector.** The single tuned RF stage before the mixer (the "preselector") is there primarily to reject the image. It is tuned to `f_desired` (1000 kHz), so a 1910 kHz image signal sees the preselector's LC tank far off-resonance and is attenuated:

```
   Image attenuation depends on the preselector's Q and the image offset:

   Image offset = 2 × f_IF = 2 × 455 = 910 kHz

   For Q = 50 at f₀ = 1000 kHz:  BW = 20 kHz
   The image at 1910 kHz is 910 kHz off-tune = 45.5 bandwidths away.
   → Preselector attenuation at 910 kHz offset ≈ 40+ dB (essentially gone).

   This is why the IF is chosen to be a SIGNIFICANT fraction of f_RF —
   so the image lands far enough from f_desired for the preselector to kill it.
```

The image-rejection requirement is why **the IF frequency matters**: too low an IF (e.g., 100 kHz) and the image is only 200 kHz away from the desired signal — the preselector (Q = 50) barely attenuates it. Too high an IF (e.g., 2 MHz) and the IF stages become harder to stabilize and the IF transformers get bulky. 455 kHz is the sweet spot for the AM broadcast band; 10.7 MHz is the sweet spot for FM (image at `f_desired + 21.4 MHz` is easy for a 100 MHz preselector to reject).

For receivers covering multiple bands (a shortwave receiver, for example), the preselector must be **trackable** — it tunes along with the LO, staying on `f_desired` while the LO stays 455 kHz above. This tracking is done mechanically (ganged capacitors on a common shaft) or electronically (varactor diodes driven by the same tuning voltage as the LO). Good image rejection (≥ 60 dB) is a hallmark of a well-designed communications receiver.

---

## 4. Detection in the Superhet Chain

The theory of AM envelope detection, FM slope detection, and PLL demodulation is fully developed in [Modulation Circuits](communications-circuits.modulation-circuits.md) §§3–5. We do not re-teach it here. What matters for the receiver architect is **where detection happens** and what feeds it:

```
   AM superhet:  IF amp (455 kHz) → diode envelope detector → AF amp
                 The 455 kHz IF signal's envelope IS the audio.
                 A simple 1N34A (germanium) or 1N4148 (silicon) diode + RC does it.

   FM superhet:  IF amp (10.7 MHz) → limiter → discriminator → AF amp
                 The limiter clips amplitude variations (noise).
                 The discriminator converts frequency deviations to voltage.
```

The key point: **detection happens after the IF chain, on the fixed-frequency IF signal.** This means the detector circuit is optimized for one frequency (455 kHz or 10.7 MHz) and never needs to tune. The detector can be a single diode (AM), a ratio detector (FM), or a PLL (FM, modern). See [Modulation Circuits](communications-circuits.modulation-circuits.md) for the full treatment of each.

---

## 5. FM Receiver Specifics

FM receivers use the same superhet architecture as AM receivers, but with three FM-specific additions. The FM IF is **10.7 MHz** (vs 455 kHz for AM), and the detection principle differs because FM encodes information in *frequency*, not *amplitude*.

### 5.1 The Limiter

FM's claim to fame is noise immunity: most noise is *amplitude* noise (lightning, ignition, motors), and FM receivers simply clip it off before demodulating. The **limiter** is a saturated IF amplifier stage that strips all amplitude variations — outputting a constant-amplitude square-ish wave whose *frequency* still carries the modulation. Any amplitude noise riding on the IF signal is flattened by the limiter. This is why FM is quiet between stations: there is no amplitude information to carry noise.

```
   IF in (10.7 MHz, amplitude-modulated by noise):
      ~~~^^~~~~~^^^^^^~~~~~   ← amplitude varies (noise + signal)

   Limiter (saturated IF stage — clips to fixed amplitude):
      ┌┐ ┌┐ ┌┐ ┌┐ ┌┐ ┌┐ ┌┐   ← constant amplitude, frequency preserved
      └┘ └┘ └┘ └┘ └┘ └┘ └┘      → noise is gone, modulation remains
```

### 5.2 The Discriminator

After the limiter, the FM receiver must convert *frequency* variations back to *voltage* variations — this is the discriminator (or FM demodulator). Three classic types, all derived in [Modulation Circuits §5](communications-circuits.modulation-circuits.md):

| Discriminator type | Principle | Complexity | Linearity |
|--------------------|-----------|------------|-----------|
| Slope detector | Detune an LC tank to the skirt of resonance; FM→AM, then envelope detect | Simplest | Poor (slope is curved) |
| Foster-Seeley | Two coupled tuned circuits; phase shifts convert FM to AM | Moderate | Good |
| Ratio detector | Like Foster-Seeley but with a limiting diode; immune to amplitude variations | Moderate | Good + self-limiting |

The **ratio detector** was the standard FM discriminator in tube and early transistor radios because it provides its own amplitude limiting — no separate limiter stage needed. Modern FM receivers use a **PLL** ([Modulation Circuits §5.2](communications-circuits.modulation-circuits.md)) as the demodulator: the PLL's VCO control voltage *is* the demodulated audio. PLL demodulation is more linear and requires no tuned circuits — a major simplification, and the approach used in virtually every FM-receiver IC since the 1980s.

### 5.3 The Complete FM Superhet Chain

```
   ┌────────┐  ┌────────┐  ┌───────┐  ┌──────┐  ┌────────┐  ┌────────┐  ┌──────┐  ┌──────┐
   │antenna │─►│ RF amp │─►│       │  │  IF  │  │ limiter│  │ discrim│  │ de-  │  │ AF   │
   │88-108M │  │+ pre-  │  │ mixer │─►│ amp  │─►│ (clip) │─►│ (PLL or│─►│empha-│─►│ amp  │
   └────────┘  │selector│  │       │  │10.7 M│  │        │  │ ratio) │  │ sis  │  │→spkr │
               └────────┘  └───┬───┘  │ Hz   │  └────────┘  └────────┘  └──────┘  └──────┘
                              │ LO   └──────┘
                         ┌────┴────┐
                         │  VFO    │  tunes 98.7–118.7 MHz (= f_signal + 10.7)
                         │ (f_LO)  │
                         └─────────┘

   LO range for FM band (88–108 MHz):
      f_LO = f_signal + 10.7 MHz
      98.7 MHz ≤ f_LO ≤ 118.7 MHz
```

The **de-emphasis** block at the end is an FM-specific detail: FM broadcasts boost high audio frequencies at the transmitter (pre-emphasis, 75 µs in the US, 50 µs in Europe) to overcome high-frequency noise. The receiver mirrors this with a matching de-emphasis (simple RC low-pass) to restore flat frequency response. This is covered in [Modulation Circuits](communications-circuits.modulation-circuits.md) §4.

---

## 6. Automatic Gain Control (AGC)

Signals arriving at a receiver vary enormously in strength: a local 50 kW AM station might deliver 10 mV at the antenna, while a distant 1 kW station at the same frequency delivers 10 µV — a **1000:1 range** (60 dB). Without compensation, the strong station would overload the IF stages (clipping, distortion) and the weak station would be inaudible (buried in noise). **AGC** solves this by sampling the detector output, converting it to a DC control voltage, and feeding it back to reduce the gain of the RF and IF stages when a strong signal is present.

```
                        ┌──────────────────────────────────────┐
                        │                                      │
                        ▼                                      │
   ┌────────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌─────┴────┐  ┌──────┐
   │antenna │─►│ RF   │─►│mixer │─►│ IF   │─►│detec-│─►│  AGC     │  │ AF   │
   │        │  │ amp  │  │      │  │ amp  │  │ tor  │  │ rectifier│  │ amp  │
   └────────┘  └──┬───┘  └──────┘  └──┬───┘  └──────┘  │ + filter │  └──────┘
                  │                    │                  │ → DC V   │
                  │                    │                  └────┬─────┘
                  │                    │                       │
                  └────────────────────┴───────────────────────┘
                     AGC control voltage (negative feedback)
                     → strong signal raises AGC voltage → lowers RF/IF gain
                     → weak signal drops AGC voltage → raises RF/IF gain
```

### How AGC Works

1. **Sample the detector output.** The detector output (audio + DC) is fed to an AGC rectifier — a diode and an RC filter with a long time constant (≈ 0.1 s). The RC filter extracts the *average* DC level, which is proportional to the carrier strength (not the instantaneous audio).

2. **Generate the control voltage.** The filtered DC voltage (0 to a few volts) is the AGC control line. Strong signal → high AGC voltage; weak signal → low (near zero) AGC voltage.

3. **Apply to gain-controlled stages.** The AGC voltage is applied to the *bias* of the RF amplifier and one or more IF amplifier transistors. A high AGC voltage reduces the transistor's quiescent current (`I_C`), which reduces its transconductance (`g_m`) and hence its gain. A low AGC voltage lets the transistor run at full bias and full gain.

The net effect is **negative feedback on signal strength**: a strong signal automatically turns down the receiver's gain so the detector sees a constant output level. A typical AGC can hold the audio output within 5 dB for an input range of 60 dB (1000:1) — the listener hears a steady volume as the car drives toward and away from the transmitter.

AGC is the reason a radio does not blast deafeningly when tuned to a local station and does not go silent between stations (the AGC runs the gain to maximum when no carrier is present, amplifying background hiss to a gentle static). A **squelch** circuit (used in ham and CB radios) gates the audio off entirely when the AGC voltage indicates no real signal — eliminating the inter-station noise.

---

## Parameter Table — Receiver Architecture Selection

| Receiver type | Sensitivity | Selectivity | Complexity | Typical application |
|---------------|------------|------------|------------|---------------------|
| Crystal set (no amp) | Poor (mV at antenna) | One LC tank | Minimal (4 parts) | First build, strong-local-station reception |
| TRF (tuned RF amp) | Moderate (µV) | Varies across band (f₀/Q) | Moderate (2–3 tuned stages, ganged) | Early 1920s radios, simple kit receivers |
| Superhet (AM, 455 kHz IF) | Excellent (µV to tens of µV) | Excellent (fixed IF filter) | Higher (mixer + LO + 2–3 IF stages) | **Every commercial AM radio** |
| Superhet (FM, 10.7 MHz IF) | Excellent | Excellent | Higher (limiter + discriminator added) | **Every commercial FM radio** |
| Superhet + PLL synthesizer | Excellent | Excellent | Highest (PLL LO, digital tuning) | Modern multiband receiver, scanner, SDR front end |

At the Mims level: build a **crystal radio** first (no power, validates antenna + tuned circuit + detector), then a **TRF** (adds RF amplification — a single transistor stage makes the difference between headphones-only and a small speaker), then a **superhet** from a kit or published schematic (the LM386 audio amp + a handful of IF cans + a transistor mixer is a classic weekend project). The superhet is where the magic happens: once you hear the sharp selectivity and the steady volume (AGC), you understand why every radio since 1930 uses Armstrong's architecture.

---

## Design Checklist

- [ ] Chosen the architecture: crystal set for learning, TRF for simple single-band, superhet for any real receiver.
- [ ] For superhet: selected the IF (455 kHz AM, 10.7 MHz FM) and verified `f_LO = f_signal + f_IF` covers the tuning range.
- [ ] Computed image frequency (`f_image = f_signal + 2·f_IF`) and verified the RF preselector attenuates it by ≥ 40 dB.
- [ ] Designed the RF preselector (one tuned stage before the mixer) for image rejection, not for gain.
- [ ] Used transformer-coupled or ceramic-resonator IF filters for selectivity (not just LC tanks — the ceramic resonator is far sharper and needs no alignment).
- [ ] For FM: included a limiter stage before the discriminator (or used a self-limiting ratio detector / PLL demodulator).
- [ ] Added AGC: rectified detector output → filtered DC → bias control on RF amp and first IF stage.
- [ ] Decoupled each amplifier stage (RF, IF, AF) from the power supply with its own RC filter to prevent feedback oscillation.
- [ ] Shielded the LO and IF stages (metal cans or a shielded enclosure) to prevent radiation and pickup.
- [ ] Verified tracking: the RF preselector and the LO tune together across the band (ganged capacitor or common tuning voltage).

## See Also

- [Modulation Circuits](communications-circuits.modulation-circuits.md) — the sibling article: AM/FM modulation and demodulation theory (envelope detection, slope detection, PLL, mixers and heterodyning). This article links rather than re-teaches all of that.
- [RF Oscillator Circuits](communications-circuits.rf-oscillator-circuits.md) — the sibling article: the LC and crystal oscillators that serve as the superhet's local oscillator and the VFO that tunes across the band.
- [Semiconductor Devices](semiconductor-devices.md) — the transistors, diodes (detectors), and ICs (LM386 audio amp, NE602 mixer) used throughout the receiver chain.
- [Passive Components](passive-components.md) — the inductors, capacitors, transformers (IF cans), and ceramic resonators that provide the superhet's selectivity and the preselector's image rejection.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
