# RF Oscillator Circuits

> **Node ID**: `electronics.communications-circuits.rf-oscillator-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md), [`electronics.analog-circuits.oscillator-circuits`](analog-circuits.oscillator-circuits.md)
> **Timeline**: Years 20-40
> **Outputs**: rf-oscillator-designs
> **Critical**: No — RF oscillator pedagogy extends general oscillator design into the communications band; not on the minimum-viable bootstrap critical path

This article is the **RF thread** of oscillator design. The general theory of oscillation — the Barkhausen criterion (loop gain ≥ 1, total phase shift = 360°), feedback amplifier topology, amplitude stabilization, and the catalog of RC, LC, and crystal circuits — is fully derived in [Oscillator Circuits](analog-circuits.oscillator-circuits.md). **Read that article first.** This one assumes you understand `f₀ = 1/(2π√(LC))`, the series-capacitor equivalent `C_eq = C₁·C₂/(C₁+C₂)`, and why a quartz crystal achieves Q values of 10 000+. We will not re-derive any of that here.

What this article *does* cover is the engineering that turns a generic LC oscillator into a **radio-frequency source**: the resonant-circuit quality factor and bandwidth that set oscillator purity, the three RF-grade topologies (Colpitts, Hartley, crystal Pierce) and how to choose between them, the variable-frequency oscillator (VFO) that lets you tune across a band, and a brief mention of the antenna that radiates the result.

This is the **Forrest Mims III / Communications Projects** level. We deliberately do **not** cover advanced RF engineering techniques — those belong to a specialized track well beyond the bootstrap horizon.

---

## 1. What Makes an Oscillator "RF"

Every LC oscillator you met in [Oscillator Circuits](analog-circuits.oscillator-circuits.md) *could* run at RF — the Colpitts example there was designed for ~1 MHz, right in the AM broadcast band. So what changes as you push toward higher RF frequencies (10 MHz, 100 MHz, 1 GHz)?

**1. Parasitics dominate.** At audio frequencies a transistor's internal capacitances (a few pF) and the wiring capacitance of a breadboard (another few pF) are negligible compared to the 100 nF tank capacitor. At 100 MHz the tank capacitor might be 10 pF — now the parasitics are a significant fraction of the design value, and they drift with temperature. RF oscillator design means *controlling* parasitics: short leads, grounded shields, and tank capacitors large enough to swamp the unknowns.

**2. The inductor is no longer ideal.** A hand-wound air-core coil has series resistance (copper loss), inter-turn capacitance (self-resonance), and radiates energy directly. Below 1 MHz these are minor; above 10 MHz they set the quality factor and the achievable frequency stability. Toroid cores (powdered iron or ferrite) concentrate the magnetic field, raise Q, and reduce radiation — the FT-37 and FT-50 cores are the workhorses of the hobbyist RF bench.

**3. Frequency stability becomes the whole game.** A 1% drift at 1 kHz audio is inaudible. A 1% drift at 100 MHz is a full megahertz — you slide right off the FM dial. RF oscillator engineering is dominated by the question "how do I keep this frequency from moving?" — and the answer ranges from good mechanical construction (rigid coil forms, NPO ceramic capacitors) to temperature compensation to, ultimately, replacing the LC tank with a quartz crystal.

### The RF Spectrum — Where Oscillators Live

| Band | Frequency | Wavelength λ | Oscillator technology | Typical use |
|------|-----------|--------------|----------------------|-------------|
| LF | 30–300 kHz | 10–1 km | LC (large L, iron core) | Navigation, time signals |
| MF | 300 kHz–3 MHz | 1 km–100 m | LC Colpitts/Hartley | **AM broadcast** (530–1710 kHz) |
| HF | 3–30 MHz | 100–10 m | LC VFO or crystal | Shortwave, ham radio |
| VHF | 30–300 MHz | 10–1 m | Crystal + multiplier, LC | **FM broadcast** (88–108 MHz) |
| UHF | 300 MHz–3 GHz | 1 m–10 cm | Crystal + PLL synthesizer | TV, GPS, mobile phones |

At the Mims level, the action is in **MF** (build a 1 MHz AM-band Colpitts) and **HF** (build a 7 MHz ham-band VFO). VHF and above require crystal references and frequency multiplication — still buildable, but the circuit construction (ground planes, shielded coils) gets demanding.

---

## 2. Resonant Circuit Fundamentals — Q and Bandwidth

The LC tank is the heart of every RF oscillator. The [Oscillator Circuits](analog-circuits.oscillator-circuits.md) article showed that the tank selects the oscillation frequency via `f₀ = 1/(2π√(LC))`. For RF work, two additional properties of the tank matter enormously: the **quality factor Q** and the **bandwidth BW**.

### The Quality Factor Q

A real LC tank is not lossless. The inductor has winding resistance `R_s`; the capacitor has a smaller equivalent series resistance; the coupling to the amplifier and load extracts energy too. The quality factor measures how many cycles the tank "rings" before its stored energy dissipates:

```
   Q = 2π · (energy stored per cycle) / (energy lost per cycle)

   For a series-resonant tank:   Q = ω₀·L / R_s = 1 / (ω₀·C·R_s)
   For a parallel-resonant tank: Q = R_p / (ω₀·L) = ω₀·C·R_p

   where ω₀ = 2π·f₀ = 1/√(LC)
```

A tank with `Q = 50` loses about 12.6% of its energy per cycle (2π/50); `Q = 200` loses about 3.1% (2π/200). The higher the Q, the sharper the resonance peak, the purer the oscillation frequency, and (critically for oscillators) the better the **phase noise** — random frequency jitter caused by thermal and shot noise perturbing the tank.

Practical Q values for RF tanks:

| Inductor type | Typical Q (at 1 MHz) | Notes |
|---------------|---------------------|-------|
| Air-core solenoid, thick wire | 50–150 | Best Q per part; radiates, picks up hum |
| Iron-powder toroid (mix 2, 7) | 100–250 | Concentrated field, self-shielding, stable |
| Ferrite toroid (mix 43, 61) | 50–150 | Higher µ for compact L at lower freq |
| Slug-tuned coil (adjustable core) | 30–100 | Allows tuning via core position |
| PCB trace inductor | 10–40 | Low Q, for UHF/μWave only |

### Bandwidth BW

The resonance curve of an LC tank is not infinitely sharp. A signal at `f₀` sees the maximum impedance; a signal offset from `f₀` sees less. The **bandwidth** is the frequency span where the tank response is within 3 dB (half power) of the peak:

```
   BW = f₀ / Q        (3 dB bandwidth of the resonant tank)

   Example: f₀ = 1 MHz, Q = 100  →  BW = 10 kHz

   → a 1 MHz tank with Q=100 passes 995 kHz to 1005 kHz at half power.
   This is what lets a receiver SEPARATE two stations 20 kHz apart.
```

This single relationship — `BW = f₀/Q` — is the origin of receiver selectivity (see [Receiver Circuits](communications-circuits.receiver-circuits.md)). A higher-Q tank passes a narrower slice of spectrum, rejecting adjacent-channel interference. But Q cannot be made arbitrarily high: losses in real inductors cap it, and too-narrow bandwidth distorts the sidebands that carry the modulation information. The art is choosing Q to pass the signal but reject the neighbor.

---

## 3. The Colpitts RF Oscillator

The Colpitts — introduced in [Oscillator Circuits](analog-circuits.oscillator-circuits.md) §3 — is the workhorse RF oscillator. Its capacitive divider feedback (C₁, C₂ across L) is stable, cheap, and easy to reproduce with close-tolerance capacitors. Here we treat it as a radio-frequency circuit: the tank component values, the construction, and the frequency calculation that places it in a target band.

```
                        Vcc (RFC = RF choke, blocks RF from supply)
                         │
                     ┌───┴───┐
                     │  RFC  │   (≈ 1 mH: high Z at f₀, DC short for bias)
                     └───┬───┘
                         │
              ┌──────────┼──────────┐
              │          │          │
              │         L ●         │  collector output (C-coupled)
              │    ┌[UUUUUUU]┐      │     → xout
              │    │         │      │
              ●────┤         ├──────●
              │    └─────────┘      │
              │          │          │
            C1 ●        C2 ●        │
              │          │          │
              │          │     ┌────┴────┐
              │          │     │ bypass  │  (emitter bypass cap for AC gain)
              │          │     │  cap C_E│
              │          │     └────┬────┘
              ●──────────●──────────●
              │                     │
              │          ┌──────┐    │
              │          │  Q1  │ BJT│
              │          │2N3904│    │
              │          └──┬───┘    │
              │             │emitter │
              │             │        │
             GND           GND      GND

   Tank: C1 series C2, parallel L.
   C_eq = C1·C2 / (C1 + C2)   →   f₀ = 1 / (2π·√(L·C_eq))
   Feedback: C1/C2 divider feeds fraction of tank voltage to emitter.
```

The transistor operates **common-base** at RF: the base is bypassed to ground with a large capacitor (so the base is an AC ground), the input signal enters at the emitter, and the output is taken from the collector. The common-base configuration is preferred at RF because it has **no Miller multiplication** of the collector-base capacitance — the base is grounded, so `C_CB` is not amplified by voltage gain. This gives the common-base stage much higher usable bandwidth than common-emitter.

### Worked Example — Colpitts in the AM Broadcast Band

Design a Colpitts oscillator to run near the top of the AM broadcast band. Choose `L = 1 µH` (a small air-core or iron-powder toroid coil) and `C₁ = C₂ = 100 pF` (silver-mica or NPO ceramic for stability).

**Step 1: Series-equivalent capacitance.**

```
   C_eq = (C1 · C2) / (C1 + C2)
        = (100 pF × 100 pF) / (100 pF + 100 pF)
        = 10 000 pF² / 200 pF
        = 50 pF
```

**Step 2: Resonant frequency.**

```
   f₀ = 1 / (2π·√(L · C_eq))
      = 1 / (2π·√(1×10⁻⁶ × 50×10⁻¹²))
      = 1 / (2π·√(5×10⁻¹⁷))
      = 1 / (2π × 7.071×10⁻⁹)
      = 1 / (4.443×10⁻⁸)
      ≈ 22.5 MHz
```

That lands in the **15-meter ham band** region, not the AM broadcast band. The 1 µH inductor is too small for 1 MHz — let us redesign for the AM band (~1 MHz).

**Redesign for f₀ ≈ 1 MHz.** Solve for the LC product needed:

```
   LC = 1 / (2π·f₀)² = 1 / (2π × 10⁶)² = 1 / (3.948×10¹³) = 2.533×10⁻¹⁴
```

With `C_eq = 50 pF = 5×10⁻¹¹ F` (keeping the same C₁ = C₂ = 100 pF divider):

```
   L = LC / C_eq = 2.533×10⁻¹⁴ / 5×10⁻¹¹ = 5.07×10⁻⁴ H ≈ 507 µH
```

A ~500 µH inductor is a substantial coil — typically 60–80 turns on a ferrite or iron-powder core (an AM-radio loopstick antenna coil is exactly this range). This is why AM-band oscillators use large L and small C: the inductor is bulky but the frequency is low. Conversely, at VHF (100 MHz) the same calculation gives L ≈ 50 nH — a single turn of wire — and C ≈ 50 pF, which is why VHF oscillators use crystal references and multipliers instead of fundamental LC tanks.

**Verify loop gain.** With equal capacitors, the feedback fraction is `C₁/C₂ = 1.0` (half the tank voltage reaches the emitter). A 2N3904 at `I_C = 1 mA` has `g_m = 40 mS`. The reactance of C₂ at 1 MHz is `X_C2 = 1/(2π·1 MHz·100 pF) = 1590 Ω`. The loop gain product `g_m · X_C2 ≈ 0.04 × 1590 = 63.6` — far exceeds unity, so oscillation starts aggressively (and the transistor's nonlinearity will limit the amplitude). This is healthy: the Colpitts oscillates reliably once `g_m · X_C2 > 1`.

---

## 4. The Hartley RF Oscillator

The Hartley is the mirror image of the Colpitts: feedback is taken from a **tapped inductor** (L₁, L₂ on one core) instead of a tapped capacitor. A single capacitor C shunts the whole tank.

```
                         Vcc
                          │
                      ┌───┴───┐
                      │  RFC  │
                      └───┬───┘
                          │
              ┌───────────┼───────────┐
              │           │           │
              │     L1 ●  │  ● L2     │
              │   ┌[UUU]──┼──[UUU]┐   │  collector output → xout
              │   │       ●       │   │
              ●───┘      (tap)    └───●
              │           │           │
              │           │          C (single tank capacitor)
              │           │           │
              │      ┌────┴────┐      │
              │      │emitter  │      │
              │      │ bypass  │      │
              │      └────┬────┘      │
              ●───────────●───────────●
              │           │
             GND        GND

   Tank: L1 + L2 (series) parallel with C.
   L_eq = L1 + L2 (+ 2M if magnetically coupled)
   f₀ = 1 / (2π·√(L_eq·C))
   Feedback: inductive divider — fraction L2/(L1+L2) of tank voltage
             appears at the tap and feeds the emitter.
```

The Hartley was historically dominant in vacuum-tube radios because a variable inductor (slider or wiper on the coil) was the easiest tuning element to build. Today the Colpitts is preferred — capacitors are cheaper, more stable, and available in closer tolerances than tapped inductors. The Hartley survives in applications where a single adjustable inductor provides both tuning and feedback (the tap ratio is fixed by the winding geometry, and the core position tunes the inductance).

The frequency equation uses the **total** series inductance. If the two windings share a common core (the usual case — they are one tapped coil), mutual inductance M adds:

```
   L_eq = L1 + L2 + 2·M      (aiding fields)
```

For a close-wound tapped coil on a high-µ core, M can be 30–60% of √(L₁·L₂), so the effective inductance is noticeably larger than the sum of the isolated winding inductances. This must be measured, not estimated, if frequency accuracy matters.

---

## 5. The Crystal Oscillator for RF

The quartz crystal oscillator is covered in depth in [Oscillator Circuits](analog-circuits.oscillator-circuits.md) §4 — the Butterworth-Van Dyke equivalent circuit, the AT-cut temperature characteristic, and the Pierce gate oscillator topology. **We do not re-derive that here.** What matters for RF is *why and when* you trade the tunable LC tank for a fixed crystal.

### When to Use a Crystal

The LC oscillator's frequency drifts. The causes, in order of severity:

| Drift source | Typical magnitude (LC) | Typical magnitude (crystal) |
|--------------|----------------------|---------------------------|
| Temperature (0–50 °C) | ±500–2000 ppm | ±20–50 ppm (AT-cut) |
| Supply voltage change | ±100–500 ppm/V | ±1–5 ppm/V |
| Load variation | ±200–1000 ppm | ±5–20 ppm |
| Mechanical vibration | ±100–1000 ppm | ±1–10 ppm |
| Aging (per year) | ±1000+ ppm | ±1–5 ppm |

At 1 MHz, a 1000 ppm temperature drift is ±1 kHz — still inside the 10 kHz AM channel, audible as a faint whistle but usable. At 100 MHz, the same 1000 ppm is ±100 kHz — you have slid completely off the 200 kHz FM channel. **The crystal's 10–50× better stability is what makes VHF communication possible.**

### The Pierce Crystal Oscillator at RF

The Pierce circuit (a CMOS inverter biased linearly, with the crystal providing the 180° phase shift) is the universal RF frequency reference. Every modern transceiver — from a $5 keyfob to a cell-phone baseband — has at least one. The crystal frequency is fixed by the cut and thickness of the quartz plate (1–30 MHz fundamental, up to ~100 MHz on overtones). The Pierce circuit is identical to the one in [Oscillator Circuits](analog-circuits.oscillator-circuits.md) §4 — the only RF-specific consideration is layout: short traces, a ground plane under the crystal, and the two load capacitors placed physically adjacent to the crystal pins to minimize stray capacitance drift.

```
   RF Pierce crystal oscillator (topology identical to the digital one):

                 Rf (~1 MΩ)
              ┌────/\/\/\──────┐
              │                │
         C1   │  ┌──────────┐  │   C2
    XOUT ─┤├──┴──┤  CMOS   ├──┴──┤├── XIN
                   │ inverter │
                   └────┬─────┘
                        │
                   ┌────┴────┐
                   │  XTAL   │  e.g. 10 MHz, 14.318 MHz, 16 MHz
                   │ quartz  │  (HF reference for PLL or direct drive)
                   └────┬────┘
                       GND

   Load capacitance: C_L = (C1·C2)/(C1+C2) + C_stray
   Crystal specified for C_L (e.g. 18 pF, 20 pF).
   Choose C1 = C2 = 2·(C_L − C_stray), C_stray ≈ 5–7 pF.
```

### Getting to VHF from a Crystal

A fundamental-mode crystal above ~30 MHz is too thin to manufacture. To reach the FM band (88–108 MHz), RF engineers use one of two techniques — both buildable at the Mims level with care:

**Frequency multiplication.** Drive a nonlinear element (a class-C biased transistor or a diode) with the crystal signal. The nonlinearity generates harmonics (2f, 3f, 5f ...), and a tuned output tank selects the desired multiple. A 36 MHz crystal × 3 = 108 MHz; a 24 MHz crystal × 4 = 96 MHz. This is how crystal-controlled walkie-talkies and older FM transmitters reach VHF.

**The PLL synthesizer.** A phase-locked loop (introduced in [Modulation Circuits](communications-circuits.modulation-circuits.md) §5.2) multiplies a crystal reference by a programmable integer `N`: `f_out = N · f_ref`. This is the modern approach — one crystal + one PLL chip gives any channel frequency with crystal stability. The PLL itself is a system topic; the oscillator *inside* the PLL is a voltage-controlled LC or cavity resonator, and the crystal is the stability reference that disciplines it.

---

## 6. The Variable Frequency Oscillator (VFO)

A crystal is locked to one frequency. To *tune* a receiver across the broadcast band — or to sweep a transmitter across the ham bands — you need an oscillator whose frequency you can change. This is the **VFO**, and at the Mims level it is an LC oscillator (Colpitts or Hartley) with a variable capacitor or variable inductor in the tank.

### Variable Capacitor Tuning

The classic AM-radio variable capacitor is a set of interleaved metal plates: one fixed set (stator) and one rotating set (rotor) on a shaft. As the rotor meshes deeper into the stator, the plate-overlap area increases and so does the capacitance. A typical AM-radio dual-gang variable spans **10–365 pF** per section — a 36:1 range, which (because frequency goes as `1/√C`) gives a **6:1 frequency range** — exactly right for the AM broadcast band (530–1710 kHz = 3.2:1, with margin).

```
   Tuning range for a Colpitts VFO with variable capacitor C_var:

   f_max / f_min = √(C_max / C_min)

   AM radio: C_max/C_min = 365/10 = 36.5
             → f_max/f_min = √36.5 = 6.04
             Covers 530–1710 kHz (3.2:1) with tuning margin to spare.
```

The variable capacitor is the most mechanically complex component in a radio — precision-machined brass or aluminum plates, bearings, a shaft coupling to the tuning knob. In the bootstrap sequence, the variable capacitor is achievable once you have [precision machining](../machine-tools/index.md) capable of flat plates and accurate shafts.

### Variable Inductor Tuning

An alternative: a fixed capacitor and a variable inductor, tuned by sliding a ferrite slug (a threaded magnetic core) in and out of the coil. The slug raises the effective permeability and thus the inductance; threading it deeper lowers the frequency. Slug-tuned coils (the "tuned circuit in a can" — shielded, threaded, adjustable with a non-metallic screwdriver) are standard in communications receivers because they allow fine-tuning without the mechanical complexity of a multi-plate variable capacitor.

### VFO Stability — The Hard Problem

A VFO's frequency is only as stable as its tank, and the tank drifts. The four enemies:

**1. Temperature.** The inductor's copper winding expands with heat, changing its dimensions and inductance. The capacitor's dielectric constant shifts with temperature. Iron-powder toroid cores (mix 2, 7) have a positive temperature coefficient; NPO/C0G ceramic capacitors have near-zero coefficient; silver-mica is slightly positive. A well-designed VFO *compensates*: the positive drift of the coil is offset by a negative-coefficient capacitor (N750) in the tank, achieving net-zero drift over the operating range. This is an empirical art — you build it, measure drift with a frequency counter over a temperature sweep, and swap compensating caps until it holds.

**2. Mechanical vibration.** The coil's turns move, the variable capacitor's plates flex, and the frequency jumps. Solution: rigid construction (coil wound tight on a solid form, glued in place; variable capacitor shock-mounted), and a slow-motion dial (vernier drive) so hand capacitance on the knob does not pull the frequency.

**3. Load variation.** If the circuit the VFO drives changes impedance (e.g., an antenna whose coupling shifts), the tank's effective capacitance changes and the frequency shifts. Solution: a **buffer amplifier** — an emitter-follower or common-collector stage between the VFO and its load, providing high input impedance (light loading of the tank) and low output impedance (drive any load without frequency shift). Every stable VFO has a buffer.

**4. Supply voltage variation.** Transistor capacitances depend on bias voltage; a ripple or drift in Vcc shifts them. Solution: a regulated supply (a zener diode or 78Lxx regulator) dedicated to the VFO stage.

```
   Stable VFO block diagram:

   ┌──────────┐    ┌──────────┐    ┌──────────┐
   │  LC VFO  │───►│  buffer  │───►│  output  │  → to mixer / antenna
   │ (Colpitts│    │ (emitter │    │  amp     │
   │ + var C) │    │ follower)│    │          │
   └────┬─────┘    └──────────┘    └──────────┘
        │
   ┌────┴─────┐
   │ regulated│  dedicated zener or 78L05 — isolates VFO from supply drift
   │ supply   │
   └──────────┘
```

A well-compensated VFO can hold ±200 ppm over a 20 °C room-temperature change — enough for AM and casual ham reception, but inadequate for FM or precision work (where the crystal + PLL approach is mandatory). VFO drift is the primary reason the superheterodyne receiver (next section) was invented with its fixed intermediate frequency — the IF filter does not drift because it does not tune.

---

## 7. Antenna Fundamentals (Brief)

An oscillator is useless for communication until its signal reaches an antenna. This is *not* an antenna-theory article — we cover only the minimum needed to get a signal on the air at the Mims level.

### Wavelength and Antenna Size

Radio waves travel at the speed of light, `c = 3×10⁸ m/s`. The wavelength is:

```
   λ = c / f

   Worked example — FM broadcast at 100 MHz:
      λ = (3×10⁸ m/s) / (100×10⁶ Hz) = 3.0 m

   → A half-wave dipole for 100 MHz is λ/2 = 1.5 m long.
   → A quarter-wave monopole (whip antenna) is λ/4 = 0.75 m long.
```

A few reference points for the Mims-level builder:

| Frequency | Wavelength λ | λ/2 dipole | λ/4 monopole | Typical antenna |
|-----------|-------------|------------|--------------|-----------------|
| 1 MHz (AM band) | 300 m | 150 m | 75 m | Long wire + ground |
| 10 MHz (shortwave) | 30 m | 15 m | 7.5 m | Dipole or vertical |
| 100 MHz (FM band) | 3.0 m | 1.5 m | 0.75 m | Whip or dipole |

### The Dipole and the Monopole

The **half-wave dipole** is the reference antenna: a straight conductor λ/2 long, split at the center, fed at the gap by the transmitter (via coaxial cable). It radiates broadside to its length. The **quarter-wave monopole** is half a dipole, mounted vertically over a ground plane (a metal car body, or a set of radial wires laid on the ground). The ground plane "mirrors" the missing half — making the monopole behave like a full dipole. The classic car-radio whip (a 0.75 m rod on a metal roof) is a λ/4 monopole for the FM band.

For AM-band reception, a full λ/4 antenna (75 m) is impractical. Crystal radios and AM receivers instead use a **loopstick antenna** — a ferrite rod with many turns of wire, which is a compact magnetic-field sensor rather than an electric-field antenna. The loopstick is small, directional (rotate the radio to peak the station), and good enough for strong local signals. This is all the antenna the Mims-level AM receiver needs.

> **Scope note.** Real antenna engineering — radiation patterns, feedline impedance, gain in dBi, polarization, stacking, yagis — is a substantial field of its own and out of scope at this level. The above is enough to get on the air with a reasonable wire. For reception, almost any conductor of reasonable length plus a good earth ground will pick up strong local stations.

---

## Parameter Table — RF Oscillator Type Selection

| Oscillator type | Useful frequency range | Stability (over 0–50 °C) | Tunable? | Typical application |
|-----------------|----------------------|--------------------------|----------|---------------------|
| Colpitts (LC) | 30 kHz – 300 MHz | ±200–1000 ppm | Yes (var C or L) | AM/FM VFO, general RF source, ham transmitter |
| Hartley (LC) | 30 kHz – 100 MHz | ±200–1000 ppm | Yes (slug-tuned L) | Classic tube radios, simple tunable VFO |
| Clapp (LC) | 100 kHz – 100 MHz | ±100–500 ppm (best LC) | Yes | High-stability VFO where crystal cannot tune |
| Pierce (crystal) | 32 kHz – 30 MHz | ±20–50 ppm | No (fixed) | Channel frequency reference, PLL clock |
| Crystal + multiplier | 30–300 MHz | ±20–50 ppm | No (channelized) | Crystal-controlled VHF transmitter |
| PLL synthesizer (VCO + crystal ref) | 1 MHz – 3 GHz | ±10–50 ppm | Yes (digital) | Modern multichannel receiver/transmitter |

At the Mims level: **build a Colpitts VFO** for tunable MF/HF work, and a **Pierce crystal oscillator** for a fixed reference frequency. The PLL synthesizer is the modern upgrade path — conceptually simple (divide a crystal reference, compare phase to a VCO, feed back the error) but requires a handful of chips and is a system-level project rather than a single circuit.

---

## Design Checklist

- [ ] Chosen LC vs crystal based on required frequency stability (LC ≈ ±500 ppm, crystal ≈ ±30 ppm).
- [ ] For LC oscillators: verified tank capacitor values are large enough to swamp transistor stray capacitances (C₁, C₂ ≫ C_internal, typically ≥ 50 pF).
- [ ] Used common-base or common-gate configuration for RF (avoids Miller capacitance, higher usable frequency).
- [ ] Included an RFC (RF choke) or tuned collector load to develop output voltage without loading the tank.
- [ ] For VFOs: added a buffer amplifier (emitter follower) between the oscillator and its load to prevent frequency pulling.
- [ ] Powered the VFO stage from a regulated supply (zener or 78Lxx) to isolate it from Vcc ripple.
- [ ] Chosen inductor type for adequate Q (toroid ≥ 100, air-core ≥ 50); measured actual L (not calculated) before finalizing C.
- [ ] For crystal oscillators: computed load capacitance `C_L = (C1·C2)/(C1+C2) + C_stray` and matched the crystal's specified C_L (else frequency is off by 100+ ppm).
- [ ] For VHF: planned a frequency-multiplication or PLL strategy rather than fundamental LC oscillation above ~50 MHz.
- [ ] Built the oscillator in a shielded enclosure (metal box) to prevent it radiating directly or picking up stray fields.

## See Also

- [Oscillator Circuits](analog-circuits.oscillator-circuits.md) — the general theory: Barkhausen criterion, RC/LC/crystal families, amplitude stabilization. This article extends that foundation into the RF band without re-deriving it.
- [Modulation Circuits](communications-circuits.modulation-circuits.md) — the sibling article: how an RF oscillator's carrier is modulated (AM, FM) and demodulated, mixers and heterodyning, the PLL as FM demodulator.
- [Receiver Circuits](communications-circuits.receiver-circuits.md) — the sibling article: the TRF and superheterodyne receiver architectures that consume the RF oscillator's output as a local oscillator.
- [Semiconductor Devices](semiconductor-devices.md) — the BJTs, JFETs, and quartz crystal resonators used in every circuit above.
- [Passive Components](passive-components.md) — the inductors, capacitors (especially NPO ceramic and silver-mica for stability), and variable tuning capacitors that set the RF frequency.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
