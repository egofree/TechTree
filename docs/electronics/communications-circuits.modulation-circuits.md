# Modulation and Demodulation Circuits

> **Node ID**: `electronics.communications-circuits.modulation-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.analog-circuits`](analog-circuits.md), [`electronics.passive-components`](passive-components.md)
> **Timeline**: Years 20-40
> **Outputs**: modulation-circuit-designs
> **Critical**: No — modulation pedagogy extends analog design into RF communications, but it is not on the minimum-viable bootstrap critical path

This is the **TESLA/RF thread** — how information rides on a carrier. You already understand the sinusoid: `v(t) = A·sin(ωt + φ)`, where amplitude `A`, angular frequency `ω = 2πf`, and phase `φ` are the three knobs you can turn. Modulation is the act of turning one of those knobs in step with a message (voice, data, a Morse key) so the message can travel through a channel that the raw message could not use. Demodulation is recovering the message at the other end.

This article stays at the **Forrest Mims III level** — enough to build a working AM transmitter/receiver, an FM demodulator, and understand a mixer. It deliberately does **not** cover Smith charts, impedance-matching network synthesis, phased arrays, or antenna theory beyond a one-paragraph mention. Those belong to a specialized RF track well beyond the bootstrap horizon.

## 1. Why Modulation — The Antenna Problem

Voice and music live at low frequencies: roughly **20 Hz to 20 kHz** for human hearing. Suppose you tried to transmit a 1 kHz tone directly as a radio wave. The wavelength is:

```
   λ = c / f = (3×10⁸ m/s) / (10³ Hz) = 300 000 m = 300 km
```

A practical antenna needs to be roughly **λ/4 to λ/2** long to radiate efficiently — that means a 75–150 km wire for a 1 kHz signal. This is physically absurd. Worse, every transmitter would share the same 20 kHz-wide slice of spectrum; there would be room for exactly one audio channel in the whole world.

Modulation solves both problems at once:

- **Practical antennas.** Shift the message up to a *carrier* frequency `f_c` of, say, 1 MHz (AM broadcast band). Now `λ = 300 m`, and a `λ/4` antenna is a 75 m mast — large but buildable. At 100 MHz (FM band), `λ = 3 m` and a quarter-wave whip fits on a car.
- **Channel multiplexing.** Each station gets its own carrier frequency. A receiver tuned to `f_c = 1 MHz` hears station A; one tuned to `f_c = 1.2 MHz` hears station B. The *selectivity* of a tuned [LC tank](passive-components.md) is what separates them.

> **Note on antennas.** We mention antennas only to motivate modulation. The physical art of making a conductor radiate efficiently — ground planes, dipoles, gain, polarization — is out of scope here. For the bootstrap-level builder, a random wire of reasonable length plus a good earth ground will receive strong local stations, and that is enough to learn with.

## 2. Amplitude Modulation (AM)

In AM, the message `m(t)` varies the *amplitude* of a fixed-frequency carrier. For a single-tone message `m(t) = A_m·sin(ω_m t)` riding on a carrier `c(t) = A_c·sin(ω_c t)`, the AM signal is:

```
   s(t) = A_c · [1 + m·sin(ω_m·t)] · sin(ω_c·t)

   where  m = modulation index = A_m / A_c        (dimensionless)
          ω_c = 2π·f_c  (carrier angular frequency)
          ω_m = 2π·f_m  (message angular frequency)
```

The bracketed term is the carrier envelope, and it swings between `(1−m)` and `(1+m)`. The modulation index `m` is the star of AM:

- **m = 0** — no modulation, pure carrier (silence on the line).
- **0 < m < 1** — the envelope faithfully follows the message. This is the good zone.
- **m = 1** — 100% modulation, the deepest that stays linear. Envelope touches zero.
- **m > 1** — **overmodulation**. The envelope crosses zero and "folds back," distorting the recovered audio (envelope-detector distortion / splatter into adjacent channels). Never do this.

### 2.1 Worked Example — Sideband Power for m = 0.5

Expand the AM equation with the product-to-sum identity `sin A · sin B = ½[cos(A−B) − cos(A+B)]`:

```
   s(t) = A_c·sin(ω_c·t)                                    ← carrier
        + (m·A_c / 2)·cos[(ω_c − ω_m)·t]                    ← lower sideband (LSB)
        + (m·A_c / 2)·cos[(ω_c + ω_m)·t]                    ← upper sideband (USB)
```

The signal is *three* frequencies: the carrier `f_c` and two sidebands at `f_c ± f_m`, each at amplitude `m·A_c/2`. Power goes as voltage squared, so:

```
   Let  P_c = carrier power = A_c²/2  (normalized to 1 Ω)

   P_LSB = P_USB = (m²/4)·P_c

   For m = 0.5:
       P_c      = 1.000 · P_c       ← the carrier hogs almost everything
       P_LSB    = (0.25/4)·P_c = 0.0625·P_c
       P_USB    = 0.0625·P_c
       ─────────────────────────────────────────
       P_total  = 1.125·P_c
       P_sidebands = 0.125·P_c   (only 11% of total power carries the message!)
```

This is AM's dirty secret: **two-thirds of the carrier power carries no information at all** — it is a constant-amplitude sine that the receiver throws away at the detector. At `m = 0.5`, only 11% of the transmitted energy is in the sidebands. This waste motivates *single-sideband* (SSB) and suppressed-carrier schemes, but those are beyond the Mims level. Ordinary AM broadcast persists because the receiver can be spectacularly simple (next section).

### 2.2 AM Bandwidth

Each sideband sits `f_m` from the carrier, so the full signal spans **2·f_m** of spectrum. A 5 kHz audio message needs 10 kHz of RF bandwidth. The AM broadcast channel spacing (10 kHz Americas, 9 kHz Europe) is chosen to fit exactly that.

## 3. AM Demodulation — The Envelope Detector

The genius of AM is how cheaply it is received. The envelope — the outline `(1 + m·sin ω_m t)` — *is* the message, offset by a DC term. Strip the carrier, remove the DC, and you have audio. A **diode + RC** does it in two components:

```
   ┌───────── AM signal in (f_c carrier + sidebands)
   │
   ▼
  ┌──┐ diode (half-wave rectifier — strips the negative half of the carrier)
  │  │   leaves only the positive envelope riding on f_c ripple
  └──┘
   │
   ▼
  ──┬─── C ───┐
    │         │   RC low-pass: τ = RC chosen so 1/f_c ≪ τ ≪ 1/f_m
    └─/\/\─R──┘   → averages out the f_c ripple, follows the f_m envelope
   │
   ▼
  ┌────────┐ coupling capacitor (blocks DC, passes audio)
  │ = audio│
  └────────┘
```

Design rule for the RC time constant: it must discharge *slowly* between carrier peaks (so the carrier ripple is smoothed) but *fast* enough to follow the highest audio frequency (so the message is not slurred). With `f_c = 1 MHz` and top audio `f_m = 5 kHz`:

```
   τ = R·C  must satisfy:   1/f_c ≪ τ ≪ 1/f_m
   ⇒ 1 µs ≪ τ ≪ 200 µs     → a common choice is τ ≈ 50–100 µs
```

That is the entire AM receiver front end after the tuned RF stage. It is why AM won the early broadcast century: a crystal radio — a tuned LC circuit, one diode (originally a galena crystal "cat's whisker"), and high-impedance headphones — needs **no power supply at all**. The received RF energy itself drives the headphones.

## 4. Frequency Modulation (FM)

In FM, the message varies the carrier's *frequency*, not its amplitude. The amplitude stays constant, which is the source of FM's famous **noise immunity**: most natural and man-made noise is *amplitude* noise (lightning, ignition, motors), and an FM receiver simply clips it off with a hard limiter before demodulating.

For a message `m(t)`, the FM carrier's instantaneous frequency is:

```
   f_inst(t) = f_c + k_f · m(t)

   where k_f = frequency sensitivity (Hz per volt, set by the modulator)

   The peak frequency deviation is  Δf = k_f · max|m(t)|
```

The instantaneous phase is the integral of frequency, so the FM waveform is `s(t) = A_c·cos(ω_c·t + 2π·k_f·∫m(t)dt)`. Unlike AM there is no simple closed-form spectrum, but the **bandwidth** is well approximated by **Carson's rule**:

```
   B_FM ≈ 2·(Δf + f_m)

   where Δf = peak deviation, f_m = highest message frequency
```

For FM broadcast, `Δf = 75 kHz` and `f_m = 15 kHz`, giving `B ≈ 2·(75+15) = 180 kHz` — hence the 200 kHz channel spacing. FM trades *much more bandwidth* for *much more noise immunity*. This bandwidth-for-noise trade is a central idea of all communications engineering.

### 4.1 Generating FM — The Varactor Modulator

The simplest FM modulator exploits a [varactor](passive-components.md) — a reverse-biased diode whose junction capacitance `C_j` varies with the applied reverse voltage. Put the varactor across the capacitor of an LC tank oscillator, and the message voltage (applied as reverse bias) pulls the resonant frequency:

```
   message voltage m(t)  ──►  varactor reverse bias  ──►  C_j varies
                                                       ──►  f = 1/(2π√(LC_j)) varies

   ⇒ the oscillator frequency tracks m(t). That is FM.
```

A larger message voltage → smaller `C_j` (reverse bias widens the depletion region) → higher frequency. The deviation `k_f` is set by the varactor's capacitance-voltage characteristic and how strongly it is coupled into the tank.

## 5. FM Demodulation — Slope Detector and PLL

### 5.1 Slope Detector

If FM is "frequency carries the message," then converting frequency changes back to voltage changes is the receiver's job. The simplest trick: pass the FM signal through a circuit whose gain *slopes* with frequency — a deliberately detuned LC tank sitting on the skirt of its resonance curve.

```
      gain
       │   ╱╲    resonance peak of LC tank (centered at f_r, slightly off f_c)
       │  ╱  ╲
       │ ╱    ╲
   f_c │●      ╲      ← park the carrier on the linear slope of the curve
       │        ╲         ↑ a frequency swing Δf → an amplitude swing Δv
       └──────────► f
                 f_r

   As f_inst swings up/down around f_c, output amplitude rides the slope
   ⇒ converts FM → AM, then a normal envelope detector recovers the message.
```

It is inelegant (the slope is not perfectly linear, causing distortion), but it works and is a classic Mims-level circuit. Better linearity comes from the **Foster-Seeley discriminator** and the **ratio detector** — refinements using two coupled tuned circuits, mentioned here only by name.

### 5.2 The Phase-Locked Loop (PLL) — Intro

The modern way to demodulate FM is the **PLL**: a closed feedback loop that locks a local voltage-controlled oscillator (VCO) onto the incoming carrier's frequency and phase. When the input frequency deviates by `Δf`, the loop's error correction — the voltage driving the VCO — *is* the demodulated message.

```
                       ┌──────────────┐
    FM in ──►(+)──────►│ phase detector│──┬/\/\──► VCO control = message out!
            ▲ −        └──────────────┘   │
            │                            ▼
            │              ┌──────────────┐
            └──────────────│     VCO      │  (local oscillator tracks input)
                           └──────────────┘
```

The PLL is one of the most versatile building blocks in electronics — beyond FM demodulation it does frequency synthesis, clock recovery, and tone decoding (e.g., the NE567 tone-decoder IC). At this level, just grasp the loop concept: *detect phase error → filter → drive VCO → feed VCO back to compare again*. The VCO control voltage is your recovered audio.

## 6. Mixers and Heterodyning

A **mixer** multiplies two signals together. Multiplication in time is convolution in frequency: two sine waves at `f_1` and `f_2` produce outputs at the **sum** (`f_1 + f_2`) and **difference** (`|f_1 − f_2|`) frequencies. This is **heterodyning**, the trick that lets you shift a signal from one frequency to another.

```
   Inputs:  cos(2π·f₁·t)  and  cos(2π·f₂·t)

   Product = ½·cos[2π(f₁+f₂)t]  +  ½·cos[2π(f₁−f₂)t]
              └─ sum frequency ─┘    └─ difference ─┘
```

Mixers are realized as:

- **Switching mixers** — a transistor or diode bridge toggled by the local oscillator (LO), effectively multiplying the RF signal by a square wave. The classic is the **diode-ring double-balanced mixer**.
- **Transconductance mixers** — a BJT/MOSFET whose gain is modulated by the LO applied to one port while the RF rides another.

The killer application is the **superheterodyne receiver**: instead of trying to build a tunable filter sharp enough to select one station at an arbitrary RF frequency, you mix the incoming RF with a tunable **local oscillator** to produce a fixed **intermediate frequency (IF)** (e.g., 455 kHz for AM, 10.7 MHz for FM). All your selectivity and gain is then built once, at the fixed IF, where filters are easy to make sharp and stable. Every commercial radio you have ever owned is a superhet. (A deeper superhet treatment belongs to the sibling *receiver-circuits* article.)

## 7. A Simple AM Transmitter

Putting it together — the block diagram of the simplest possible voice transmitter:

```
   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
   │  audio   │    │          │    │          │    │          │
   │  source  ├──►│ AM       ├──►│ RF       ├──►│ antenna  │
   │ (mic /   │    │ modulator│    │ power    │    │ (wire +  │
   │  tone)   │    │          │    │ amplifier│    │  ground) │
   └──────────┘    └────┬─────┘    └──────────┘    └──────────┘
                         ▲
                         │
                   ┌─────┴─────┐
                   │ RF         │   carrier oscillator (LC or crystal)
                   │ oscillator │   sets f_c — e.g. ~1 MHz AM band
                   └────────────┘

   Signal flow:
     • oscillator generates a clean sine at f_c
     • modulator multiplies/amplifies it by (1 + m·audio)   ← AM
     • power amplifier boosts it to drive the antenna
     • antenna radiates the modulated wave into space
```

The modulator is often just the audio signal varying the bias (hence the gain) of the RF amplifier stage — a single transistor doing double duty. The [amplifier fundamentals](analog-circuits.md) (biasing, coupling, classes A/B/C) are covered under the analog-circuits family; here we only apply them at RF. The oscillator is an LC or crystal oscillator — again, a circuit owned by the analog/oscillator family, selected here for the specific property of *frequency stability*.

A matching **receiver** is a tuned LC input stage → diode envelope detector → audio amplifier → speaker. Together the two form a complete one-way voice link at the Mims *Communications Projects* level — achievable as soon as you can build oscillators, amplifiers, and [passive LC tanks](passive-components.md).

## Frequency Bands Quick Reference

A practical map of the spectrum the bootstrap engineer will encounter. Wavelength `λ = c/f`; propagation behavior dictates which band serves which purpose.

| Band | Frequency range | Wavelength (approx.) | Typical use | Propagation characteristic |
|------|-----------------|----------------------|-------------|----------------------------|
| VLF | 3–30 kHz | 100–10 km | Submarine, navigation | Ground wave; penetrates seawater |
| LF | 30–300 kHz | 10–1 km | Navigation, time signals | Ground wave; stable day/night |
| MF | 300 kHz–3 MHz | 1 km–100 m | **AM broadcast** (530–1710 kHz) | Ground wave + night sky-wave |
| HF | 3–30 MHz | 100–10 m | Shortwave, long-distance | Sky-wave (ionospheric) → global hops |
| VHF | 30–300 MHz | 10–1 m | **FM broadcast** (88–108 MHz), TV, aviation | Mostly line-of-sight |
| UHF | 300 MHz–3 GHz | 1 m–10 cm | TV, mobile, GPS, early Wi-Fi | Line-of-sight; penetrating |

The two bands that matter most at the Mims level are **MF** (build an AM transmitter/receiver around 1 MHz) and **VHF** (build an FM receiver around 100 MHz). HF shortwave is rewarding for long-distance reception but its sky-wave behavior is a topic for later study.

## Scope Boundary

This article stays at the **Mims / introductory level**. Deliberately **not** covered here:

- **Smith charts** and impedance-matching network synthesis — a specialized RF-technique track.
- **Phased arrays / beamforming** — advanced antenna systems beyond bootstrap scope.
- **Digital modulation** (QAM, PSK constellations) — beyond a passing mention; needs a digital-communications track.
- **Software-defined radio (SDR)** — a computing-hardware topic, not a circuit topic.
- **Antenna theory depth** — antennas are mentioned only to motivate modulation and the carrier-frequency requirement.

Those advanced topics belong to a specialized RF engineering track well beyond the bootstrap horizon.

## Prerequisites

- [Analog circuits](analog-circuits.md) — amplifier fundamentals (biasing, gain, classes A/B/C) and oscillator circuits (LC, crystal) are applied here at RF frequencies.
- [Passive components](passive-components.md) — inductors and capacitors form the tuned LC tanks that set the carrier frequency and provide receiver selectivity; the varactor is a passive modulator element.
- AC circuit analysis (phasors, reactance, resonance) — the shared bedrock; the tuned LC tank is a Tesla-era invention that makes selectivity possible.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
