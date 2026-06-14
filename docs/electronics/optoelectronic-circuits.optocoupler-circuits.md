# Optocoupler Circuits

> **Node ID**: `electronics.optoelectronic-circuits.optocoupler-circuits`
> **Domain**: [Electronics](index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md),
> [`electronics.passive-components`](passive-components.md),
> [`electronics.optoelectronic-circuits.led-driver-circuits`](optoelectronic-circuits.led-driver-circuits.md),
> [`electronics.optoelectronic-circuits.photodetector-circuits`](optoelectronic-circuits.photodetector-circuits.md)
> **Outputs**: optocoupler-circuit-designs
> **Timeline**: Years 25-50
> **Critical**: No — optocouplers provide galvanic isolation for safety and signal integrity, but they are not on the minimum-viable bootstrap critical path

An **optocoupler** (also called an **optoisolator** or **photocoupler**) is a single package containing an LED on the input side optically coupled to a light-sensitive device on the output side, with no electrical connection between the two. The signal crosses the gap as **photons**, not electrons. This article teaches the circuit design: how to choose drive current, size pull-up resistors, predict speed, and apply optocouplers to the five canonical jobs — digital isolation, AC load switching (solid-state relays), analog isolation, infrared links, and fiber-optic data links.

The LED half of an optocoupler is driven exactly like any other indicator LED — see [LED Driver Circuits](optoelectronic-circuits.led-driver-circuits.md) for current limiting, transistor drive, and constant-current topologies. The detector half is a photodiode or phototransistor whose readout follows the same circuit patterns taught in [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md). What is **new** here is the coupling: two independent circuits joined only by light, and the key parameter — **Current Transfer Ratio (CTR)** — that links them.

---

## 1. Why Galvanic Isolation Matters

"Galvanic" means a direct metallic (wire) connection. **Galvanic isolation** removes that connection. Two circuits that share no common ground or power rail cannot exchange fault current, cannot form ground loops, and cannot impose their voltage on each other. Four problems drive the need:

1. **High-voltage safety isolation** — A microcontroller running at 5 V must often switch or monitor 120/240 VAC mains, 600 V DC solar strings, or multi-kV motor drives. A single failed transistor would put lethal voltage on the logic. An optocoupler rated for 5 kV isolation (the typical minimum for through-hole DIP packages; SMT parts are often rated 3.75 kV or higher) guarantees that a fault on the high-voltage side cannot reach the low-voltage side within its dielectric rating.
2. **Ground-loop elimination** — When two circuits share a ground conductor carrying current, the IR drop along that conductor appears as a voltage difference between the two "grounds." In sensor and audio systems this manifests as 50/60 Hz hum or DC offset errors. Isolating the signal breaks the shared-current path without breaking the signal.
3. **Noise immunity** — Industrial environments couple switching noise (VFDs, contactors, arc welders) into signal wiring via capacitance and inductance. An optocoupler's input LED draws milliamps; noise sources that could corrupt a volt-level analog signal cannot forward-bias the LED, so noise is rejected by the LED's forward-voltage threshold.
4. **Level shifting** — Translating between logic families at different supply voltages (e.g. a 3.3 V MCU driving 15 V IGBT gate-driver circuitry) is trivially done with an optocoupler: the LED is driven by the 3.3 V logic; the phototransistor pull-up sits at whatever voltage the downstream circuit uses.

---

## 2. Optocoupler Internals

The optocoupler package contains an infrared LED (usually GaAs, λ ≈ 940 nm) facing a detector across a thin optical coupling medium (transparent silicone or air gap), both molded in light-blocking epoxy so only the internal LED's light reaches the detector. The isolation barrier is the physical dielectric between the two dies.

```
                ┌──────── optocoupler package (e.g. 6-pin DIP) ────────┐
                │                                                       │
   Anode ───────┤  LED    │◄ optical │    phototransistor               │
                │  (IR)   │  gap     │    ┌─── C (collector) ──────────┤──── Output
   Cathode ─────┤         │          │    │                            │
                │   GaAs  │ silicone │  B │(base, floating or pinned)  │
                │  die    │  or air  │    │                            │
                │         │ barrier  │    └─── E (emitter) ────────────┤──── Return
                │                                                       │
                └───────────────────────────────────────────────────────┘

     Input side (LED)              Output side (phototransistor)
     ──────────────────             ─────────────────────────────
     Galvanically isolated          No electrical connection
     from output side               to input side
```

The **detector type** determines the part's function and speed:

| Detector type | Part families | Output | Speed | Typical use |
|---------------|---------------|--------|-------|-------------|
| Phototransistor | 4N25, 4N35, PC817 | Open-collector, CTR 20–600% | Slow (2–20 µs) | Digital isolation, logic-level shift |
| Photodarlington | 4N29, 4N33 | Open-collector, CTR 200–1000%+ | Very slow (50–200 µs) | Direct relay/SSR drive, low LED current |
| Photodiode + amplifier | 6N137, HCPL-2601 | Logic output (TTL) | Fast (75 ns–1 µs) | High-speed digital isolation |
| Phototriac (optotriac) | MOC3041, MOC3020, MOC3063 | AC triac trigger | Zero-cross or random | Solid-state relay, AC load control |
| Linear photodiode pair | HCNR201, IL300 | Analog current mirror | DC–1 MHz | Analog isolation amplifier |

**Isolation voltage** (rated 3.75–7.5 kV depending on package) is the dielectric withstand between input and output. This is verified by a HIPOT (dielectric withstand) test during manufacturing and is a *safety* rating, not an operating voltage.

---

## 3. Current Transfer Ratio (CTR)

CTR is the single most important parameter for phototransistor-output optocouplers. It is the DC current gain of the optical link:

```
                    I_C (collector current of phototransistor)
    CTR  =  ─────────────────────────────────────────────────── × 100%
                     I_F (forward current through the LED)
```

A CTR of 100% means 1 mA of LED drive produces 1 mA of available collector current — a 1:1 optical current mirror. CTR varies wildly with operating conditions:

- **Device-to-device spread**: datasheets specify a range, often 50% to 600% for the same part number at the same test condition. The 4N35 datasheet quotes CTR min 50% / typ 200% at I_F = 10 mA, V_CE = 10 V — your design must work at the **minimum**, not the typical.
- **Temperature**: CTR drops roughly 50% from 25 °C to 75 °C (LED output falls with temperature faster than phototransistor gain rises).
- **Age / LED degradation**: IR LEDs lose 10–30% of their light output over 10,000–50,000 hours of operation. Designs run at the nominal CTR will fail late in life.
- **LED drive current**: CTR peaks around I_F = 5–20 mA and falls off at both extremes (low current: poor LED efficiency; high current: saturation).

The safe design practice is to derate: divide the datasheet minimum CTR by **3–5×** to account for temperature + age + current swing, then design around that worst case.

### Worked CTR example: logic-level isolated output

**Goal:** Isolate a 5 V logic signal. The microcontroller can drive the optocoupler LED at 5 mA. We want a clean logic-level output on the isolated side.

**Step 1 — Available collector current (worst case):**

The 4N35 datasheet quotes CTR_min = 50% at I_F = 10 mA. We are driving at only 5 mA, where CTR is slightly lower (the CTR-vs-I_F curve rolls off below 5 mA). Derate by 4× total for temperature + age + current:

```
    CTR_design = CTR_min / 4 = 50% / 4 = 12.5%

    I_C(available) = CTR_design × I_F = 0.125 × 5 mA = 0.625 mA
```

**Step 2 — Pull-up resistor:**

The phototransistor acts as an open-collector output. To pull the output LOW (transistor ON), the phototransistor must sink the pull-up current. To produce a valid logic LOW (≤ 0.4 V for standard 5 V TTL/CMOS), we need the pull-up current to be comfortably less than the available collector current:

```
    Design target:  I_pullup = I_C(available) / 2  (50% margin)
                   = 0.625 mA / 2
                   = 0.3125 mA  →  round to 0.25 mA for a standard resistor

    R_pullup = V_CC / I_pullup = 5 V / 0.25 mA = 20 kΩ  →  use 10 kΩ
```

With a 10 kΩ pull-up the load current is 5 V / 10 kΩ = 0.5 mA. Our worst-case available current is 0.625 mA — the phototransistor can sink it with margin, holding the output well below 0.4 V (V_CE(sat) ≈ 0.2 V at this current). When the LED is OFF, no light reaches the phototransistor, the transistor is OFF, and the 10 kΩ pull-up brings the output cleanly to V_CC = 5 V (logic HIGH) within a microsecond.

```
                   +5 V (isolated side)
                    │
                    │
                    ├─── R_pullup (10 kΩ) ───┐
                    │                        │
                    │                        ├──► V_out (logic)
                    │                        │
                ┌───┴───┐                    │
                │  4N35 │  Collector ────────┘
   Input ──R_LED─┤ LED   │
   (5 mA)        │  +    │  Emitter
   (MCU pin)     │phototr│
                └───┬───┘    │
                    │       GND (isolated)
                   GND (driving side)
```

This is the canonical isolated digital interface: one resistor on each side, one optocoupler. The 10 kΩ value is a standard rule-of-thumb for 4N35-class parts driven at 5–10 mA.

---

## 4. Digital Isolation

The circuit above is the basic **digital isolator**: a logic signal on the driving side switches the LED; the phototransistor reproduces a logic signal on the isolated side. Two design points dominate:

### 4a. LED drive resistor

The LED needs a series resistor exactly as in [LED Driver Circuits](optoelectronic-circuits.led-driver-circuits.md) §1:

```
    R_LED = (V_logic − V_F) / I_F
```

For a 5 V MCU driving at 5 mA through a 4N35 (V_F ≈ 1.2 V):

```
    R_LED = (5 − 1.2) / 0.005 = 760 Ω  →  use 750 Ω  →  I_F = 5.07 mA
```

If the driving pin cannot source enough current (some 3.3 V MCUs max out at 4 mA), use a transistor-driven LED (LED Driver Circuits §2) or select a high-CTR photodarlington (4N33, CTR ≥ 500%) that works at I_F = 0.5 mA.

### 4b. Speed limitations

Phototransistor optocouplers are **slow** — typically 2–20 µs rise/fall time — for three reasons:

1. **Saturation storage time** — The phototransistor, driven into saturation by the photogenerated base current, stores charge in its base region. When the LED turns OFF, the transistor cannot turn OFF until this stored charge recombines. This adds several microseconds of turn-off delay (the turn-OFF is always slower than the turn-ON in a saturated phototransistor).
2. **Miller capacitance** — The collector-base capacitance, multiplied by the voltage gain, slows the transition.
3. **Base-emitter leakage path** — The floating base has no active pull-down; charge leaves only by recombination.

Practical consequence: a 4N35 is usable to perhaps **10–50 kHz** as a digital isolator. This is fine for UART at 9600 baud, relay control, button sensing, and slow serial links — but it **cannot** pass SPI, I²C, or video.

**Speed remedies:**

- **Baker clamp / anti-saturation** — A Schottky diode from base to collector prevents deep saturation, cutting storage time. Implemented internally in some "high-speed" optocouplers.
- **Photodiode + amplifier** (e.g. 6N137, HCPL-2601) — The photodiode is fast (ns); an internal transimpedance amplifier converts photocurrent to a logic output. These parts achieve 75 ns–1 µs, supporting data rates of 1–10 MBd. They cost more and need a V_CC pin on the output side.
- **Blasphemous base pin** — 6-pin optocouplers (4N25, 4N35) expose the base on pin 6. Tying a resistor (e.g. 100 kΩ–1 MΩ) from base to emitter bleeds off stored charge faster, cutting storage time by 2–5× at the cost of some CTR. This is a known "speed-up" trick for free, using only the base pin.
- **Capacitive-coupled LED drive** — Driving the LED through a small capacitor (AC coupling) injects a pulse of extra current at the edge, "kicking" the phototransistor out of saturation faster.

### 4c. Modern digital isolators (context)

For new high-speed designs, **capacitive** and **magnetic** isolators (e.g. Silicon Labs Si86xx, TI ISO164x, ADuM iCouplers) have largely replaced optocouplers above 1 MBd. They use on-chip transformers or capacitors as the barrier and achieve 100 Mbps+ with lower power and no LED aging. However, they require a dielectrically-isolated supply rail on the isolated side (the barrier must still carry power somehow). For mains-referenced safety isolation where **proven long-term reliability of the barrier** is paramount, optocouplers remain the conservative choice — the LED degradation mechanism is well-characterized and the barrier is a simple dielectric.

---

## 5. Solid-State Relays (SSR) — Optotriac Driving a Triac

A **solid-state relay** switches AC load current with no moving parts. The heart of an SSR is an **optotriac** (a phototriac-output optocoupler like the MOC3041, MOC3063, or MOC3020): an LED on the input side optically triggers a triac on the output side. The optotriac itself handles only tens of milliamps — it is a **driver**. To switch an ampere or more of load current, the optotriac triggers a larger **power triac** in a cascade.

```
    ── AC load (lamp, motor, heater) ──
    │                                 │
    │                                 │
   MT2 ───────── load ──── MT2       │
                          ┌───┴───┐    │
                          │ power │    │
                          │ triac │    │   (e.g. BTA16-600B: 16 A, 600 V)
                          │ BT13x │    │
                          └───┬───┘    │
                          MT1 ─┼────────┤
                               │        │
                              gate      │
                               │        │
                          ┌────┴────┐   │
                          │ MOC3041 │   │
                          │optotriac│   │
                          │  MT1 ───┼───┤
                          │  MT2 ───┼───┘
                          │  gate ──┘  (internal optotriac
                          │            triggers via gate
                          └────┬────┘   terminal of power triac)
                               │
                        +------+
                        │
    Logic in ──R_LED────┤ LED (pin 1)
                        │
                        +─── pin 2 (LED cathode)

    The MOC3041 includes a ZERO-CROSSING detector:
    it only triggers the output triac when mains voltage
    is near a zero crossing — reducing EMI and inrush surge.
```

### Zero-crossing vs. random-fire

- **Zero-cross optotriacs** (MOC3041, MOC3063, MOC3083) include circuitry that inhibits the output triac from turning on until the AC waveform crosses zero. This is mandatory for resistive loads (lamps, heaters) because it eliminates the high-frequency EMI burst that a mid-cycle turn-on would generate. Zero-crossing also minimizes the surge into cold lamp filaments (lower inrush → longer lamp life).
- **Random-fire (phase-control) optotriacs** (MOC3020, MOC3021, MOC3052) turn on the instant the LED is driven, regardless of AC phase. These are used for **light dimmers** and motor speed control, where the user *wants* to vary the turn-on point within each half-cycle (phase angle control) to control the delivered power. A dimmer triggers the optotriac at a user-set phase angle each half-cycle; the triac then latches on until the next zero crossing.

### Worked example: 12 VDC-controlled SSR for a 240 VAC / 8 A heater

**Components:**
- **MOC3041** optotriac (zero-cross, 600 V blocking, I_FT = 15 mA trigger, 250 V/µs dv/dt)
- **BTA16-600B** power triac (16 A_RMS, 600 V, I_GT = 50 mA gate trigger)
- **Snubber**: R_s = 39 Ω in series with C_s = 0.01 µF across MT1–MT2 of the optotriac to prevent false triggering from high dv/dt (the optotriac is more sensitive than the power triac and can be fooled by fast voltage edges from inductive loads).

**LED drive:** I_FT(trigger) = 15 mA max for the MOC3041. From a 5 V logic pin:

```
    R_LED = (5 − 1.2) / 0.015 = 253 Ω  →  use 220 Ω  →  I_F = 17.3 mA
```

The power triac's gate is driven through the MOC3041's internal optotriac; no gate resistor is needed because the optotriac limits the gate current. The triac latches on until the load current drops below its holding current at the next zero crossing.

**Comparison to a mechanical relay:** See [Relay Logic](control-circuits.relay-logic.md) for contactor sizing and the trade-offs. The SSR has **no moving parts** (no contact wear, no arc, no audible click, no bounce), switches at the zero crossing (no EMI), and can cycle millions of times (a mechanical contactor's life is 10⁵–10⁶ cycles under load). The downsides: the SSR has a finite on-state voltage drop (~1.5 V across the triac) so it dissipates heat (8 A × 1.5 V = 12 W → needs a heatsink), it leaks a small current when off (~0.1 mA through the snubber — enough to faintly glow a neon lamp), and a failed-short SSR leaves the load permanently energized (a dangerous failure mode that mechanical relays rarely suffer).

---

## 6. Linear / Analog Isolation

A phototransistor optocoupler is wildly nonlinear and temperature-dependent — useless for passing an analog voltage intact. Two approaches recover analog fidelity:

### 6a. Two-photodiode servo (the IL300 / HCNR201 approach)

A **linear optocoupler** contains one LED and **two** matched photodiodes. Photodiode 1 (PD1) receives a known fraction of the LED's light and feeds back to the input-side op-amp; photodiode 2 (PD2) receives an identical-fraction light and drives the output-side op-amp. The input op-amp servos the LED current to keep PD1's photocurrent equal to the input signal; because PD2 is matched to PD1 on the same die, it reproduces the same current on the isolated side.

```
                    ┌──── linear optocoupler (HCNR201) ──────┐
   V_in ──R_in──┐   │                                         │
                │   │   LED ◄────┬─────► PD1 ────► op-amp in  │  (input side, servo)
                ▼  │             │                            │
              op-amp│ (input)    │                            │
                │   │             │     ► PD2 ────► op-amp out │──► V_out (isolated)
                └───┤             │                            │     (output side)
                    │             │                            │
                    └──────────────────────────────────────────┘
                              galvanic barrier (5 kV)

    Input op-amp forces:  I_PD1 = V_in / R_in
    Matched photodiodes:  I_PD2 = I_PD1 × (K3/K2)    (transfer gain ~1.0 ± 1%)
    Output op-amp:        V_out = I_PD2 × R_out

    Linearity: 0.01% (100× better than a bare phototransistor optocoupler)
    Bandwidth: DC to ~1 MHz
```

This is the building block of an **isolation amplifier** — a device that faithfully reproduces an analog voltage across an isolation barrier. Isolation amplifiers are used in medical instrumentation (ECG patient isolation), motor current sensing (measuring current on the high side of a 600 V inverter), and industrial process control.

### 6b. PWM-encoded isolation (the pragmatic approach)

When a linear optocoupler is unavailable, encode the analog value as a **pulse-width** or **frequency** that a standard digital optocoupler can pass cleanly. A voltage-to-PWM converter on the input side drives the LED; an RC low-pass filter on the output side recovers the average voltage. This trades bandwidth (limited by the carrier frequency and filter) for accuracy (set by the PWM duty-cycle resolution, not the optocoupler CTR). A 555 [timer circuit](analog-circuits.timer-circuits.md) in astable/PWM mode is the classic modulator.

---

## 7. Infrared (IR) TX/RX Links

An IR link is a **free-space** optocoupler: the LED and detector are in **separate packages** separated by air (centimeters to meters) instead of a millimeter of silicone inside one package. The same physics — LED emits, phototransistor detects — applies, but CTR is far lower because most of the LED's light misses the detector entirely.

### 7a. IR break-beam / proximity sensor

An IR LED (940 nm) and an IR phototransistor face each other across a gap. When the beam is unbroken, the phototransistor conducts; when an object blocks the beam, the phototransistor turns off. This is the basis of industrial parts counters, garage-door safety edges, and old-school computer "light pens."

```
    IR transmitter (TX)                    IR receiver (RX)

     +5 V                                    +5 V
      │                                       │
      ├── R_LIMIT ──┐                         ├── R_PULLUP (10 kΩ) ──┐
      │             │                         │                      │
      │            ┌─┴─┐    IR beam        ┌──┴──┐                    ├──► V_out
      │            │IR │ ──────────────►   │ IR  │ phototransistor    │     (HIGH = beam
      │            │LED│   (940 nm)        │ PHT │                    │      broken)
      │            └─┬─┘                   └──┬──┘                    │
      │              │                        │                       │
      │             GND                       │                       │
      │                                       │                       │
     Input (DC or                              └───────────────────────┘
     38 kHz modulated)                        GND

     R_LIMIT = (5 − 1.2) / I_F    V_out = LOW when beam hits detector (transistor ON)
                                   V_out = HIGH when beam is blocked (transistor OFF)
```

The readout circuit is identical to the [phototransistor switch](optoelectronic-circuits.photodetector-circuits.md) — the only difference is the *source* of light. Ambient light (sunlight, room lamps) also contains IR, so a DC-coupled break-beam is easily fooled by a desk lamp. The cure is **modulation**.

### 7b. 38 kHz modulation for IR remote control

IR remote controls (TV, stereo, appliance) modulate the IR LED at **38 kHz** (some use 36, 40, or 56 kHz; 38 kHz is the de facto standard) and send the actual data as **gaps** in the 38 kHz carrier. The receiver is an IR photodiode followed by a **bandpass filter tuned to 38 kHz** and an integrator/demodulator, all in a 3-pin package (e.g. TSOP38238, VS1838B). Because the receiver only responds to 38 kHz pulsing light, it completely rejects steady ambient IR (sunlight, lamps) — only a deliberately modulated signal gets through.

The 38 kHz carrier is typically generated by a **555 timer** in astable mode (see [Timer Circuits](analog-circuits.timer-circuits.md) for the astable formula f = 1.44 / ((R_A + 2·R_B)·C)). A worked example: for 38 kHz with C = 1 nF and R_A = R_B:

```
    f = 1.44 / ((R_A + 2·R_B) · C)
    38000 = 1.44 / (3·R · 1e-9)
    R = 1.44 / (3 × 1e-9 × 38000) = 12.6 kΩ  →  use 12 kΩ + 1 kΩ trimmer
```

The data protocol (NEC, RC-5, Sony SIRC) then gates this 38 kHz carrier on and off: the carrier is present for a "mark" (e.g. 562 µs) and absent for a "space" (562 µs for a 0-bit, 1.688 ms for a 1-bit in the NEC protocol). The receiver demodulates the 38 kHz presence/absence back to a logic-level baseband signal that a microcontroller decodes.

---

## 8. Fiber-Optic Data Link

A fiber-optic link replaces the free-space or silicone optical gap with a **glass or plastic fiber** — a waveguide that traps light by total internal reflection. The fiber itself is the isolation barrier: there is no metallic path of any length between transmitter and receiver, and the fiber is immune to electromagnetic interference (light is not affected by electric or magnetic fields). This makes fiber the standard for:

- **High-voltage substation telemetry** — data and protection signals between a 500 kV switchyard and the control room, with kilovolts of potential difference bridged by a few meters of non-conductive fiber.
- **Medical isolation** — fiber-optic ECG and sensor links provide patient isolation superior to any transformer or optocoupler.
- **Long-haul communication** — single-mode fiber at 1310/1550 nm carries data tens of kilometers before amplification, with effectively unlimited bandwidth-distance product.

**Transmitter (TX):** An LED (for short-distance plastic-fiber links, 650 nm visible red is common) or a **laser diode** (for glass fiber, 850/1310/1550 nm) driven by the data signal through a current-limiting resistor or a dedicated laser-driver IC. The drive circuit is an LED driver (see [LED Driver Circuits](optoelectronic-circuits.led-driver-circuits.md)); laser diodes additionally need a monitor photodiode and APC (automatic power control) loop to prevent over-current destruction — the same constant-current principle, with tighter control.

**Receiver (RX):** A **PIN photodiode** or **avalanche photodiode (APD)** converts the received light back to photocurrent, followed by a **transimpedance amplifier** (TIA) to convert photocurrent to voltage (see [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md) for TIA design). The TIA output is then sliced by a comparator to recover the digital signal.

```
    ── fiber-optic data link (conceptual) ──

    TX side                              RX side
    ───────                              ───────

    Data ──► LED driver    ╔═══════╗   PIN photodiode ──► TIA ──► Comparator ──► Data out
             or laser      ║ glass ║     or APD
             diode TX      ║ fiber ║
                           ╚═══════╝
            ─────────────────────────────────────────────────────
                          galvanic isolation barrier
                          (the fiber; km of dielectric glass)
```

This article covers only the **circuit-level** concept of fiber links. The physics of fiber (numerical aperture, single-mode vs. multi-mode, dispersion, attenuation windows, optical amplifiers, WDM multiplexing) is a full discipline of its own and is out of scope for the electronics-articles track.

---

## Optocoupler Parameter Reference

Representative devices spanning the five detector types. Values are indicative; consult the manufacturer datasheet for exact ratings.

| Device | Detector | Isolation (kV) | CTR (min) | Speed (t_on/t_off) | Application |
|--------|----------|:--------------:|:---------:|:------------------:|-------------|
| PC817 / PC817C | Phototransistor | 5.0 | 50–600% | 4 µs / 3 µs (typ) | General digital isolation, logic level shift, PSU feedback |
| 4N35 | Phototransistor (base exposed) | 5.0 | 50% @ 10 mA | 2 µs / 20 µs (sat) | Digital isolation, UART, relay drive |
| 4N33 | Photodarlington | 5.0 | 500% @ 10 mA | 50 µs / 50 µs | Low-current LED drive, SSR input |
| 6N137 | Photodiode + amp | 5.0 | (logic out) | 75 ns / 75 ns | High-speed digital (1–10 MBd), SPI isolation |
| MOC3041 | Phototriac (zero-cross) | 7.5 | (triac out, 100 mA) | (zero-cross latched) | SSR driver for resistive AC loads |
| MOC3020 | Phototriac (random-fire) | 7.5 | (triac out, 100 mA) | (instant trigger) | Light dimmer, phase-control, motor speed |
| HCNR201 / IL300 | Dual linear photodiode | 5.0 | (matched pair) | DC–1 MHz | Analog isolation amplifier, isolated sensor |
| TLP2745 / ADuM1xxx | Capacitive / magnetic | 5.0 | (logic out) | 20–50 ns | Modern high-speed digital isolator (non-optical) |

---

## Design Heuristics

| Design goal | Recommended device | Circuit pattern |
|-------------|--------------------|-----------------|
| Isolate a slow digital signal (UART, relay, button) | PC817 / 4N35 (phototransistor) | LED + R_LED in; phototransistor + R_pullup out (§4) |
| Isolate a fast signal (SPI, encoder, 1 Mbps+) | 6N137 / HCPL-2601 (photodiode + amp) | Same topology, needs V_CC on output side |
| Switch an AC load from logic | MOC3041 + power triac (§5) | Zero-cross for resistive; random-fire for dimming |
| Measure an analog voltage across a barrier | HCNR201 / IL300 (§6a) | Dual-photodiode servo, two op-amps |
| Isolate an analog signal cheaply | 4N35 + PWM encode/decode (§6b) | 555 or MCU PWM → opto → RC LPF |
| Short-range object detection | IR LED + IR phototransistor (§7a) | Break-beam or reflective pair |
| IR remote control | IR LED + TSOP38238 (§7b) | 38 kHz carrier, protocol-gated |
| Long-distance / high-EMI data | Fiber-optic TX/RX pair (§8) | LED/laser + fiber + PIN photodiode + TIA |

---

## Prerequisites

- [Semiconductor Devices](semiconductor-devices.md) — the LED and phototransistor/photodiode are semiconductor devices; their construction and physics live there.
- [Passive Components](passive-components.md) — the current-limiting and pull-up resistors used in every circuit here.
- [LED Driver Circuits](optoelectronic-circuits.led-driver-circuits.md) — driving the optocoupler's input LED is identical to driving any indicator LED; this article references the resistor, transistor, and constant-current topologies taught there.
- [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md) — reading the optocoupler's output phototransistor uses the same open-collector switch and TIA patterns taught there.
- [Relay Logic](control-circuits.relay-logic.md) — mechanical relay and contactor fundamentals; the solid-state relay (§5) is the optocoupler-based alternative to a mechanical contactor.
- [Timer Circuits](analog-circuits.timer-circuits.md) — the 555 timer in astable mode generates the 38 kHz IR remote carrier (§7b) and the PWM carrier for analog isolation (§6b).

## Scope Boundary

This article covers **optocoupler and optoisolator circuit design** only. It does **not** cover:

- LED or photodiode semiconductor physics — see [Semiconductor Devices](semiconductor-devices.md).
- LED driving techniques (resistor, transistor, constant-current, PWM dimming) — see [LED Driver Circuits](optoelectronic-circuits.led-driver-circuits.md).
- Photodiode/phototransistor readout circuit patterns (TIA, transimpedance, light/dark switches) — see [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md).
- Fiber-optic physics (dispersion, attenuation, single vs. multi-mode, WDM) — a full discipline, out of scope.
- Mechanical relay and contactor construction — see [Relay Logic](control-circuits.relay-logic.md).

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
