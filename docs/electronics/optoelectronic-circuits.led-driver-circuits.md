# LED Driver Circuits

> **Node ID**: `electronics.optoelectronic-circuits.led-driver-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md),
> [`electronics.passive-components`](passive-components.md)
> **Enables**: None
> **Outputs**: led-driver-designs
> **Timeline**: Years 25-50
> **Critical**: No — LED drivers extend electronics into light emission for signaling, indication, and illumination, but they are not on the minimum-viable bootstrap critical path

This is the Forrest Mims III *Optoelectronics Projects* entry point for **light emission**. An [LED](semiconductor-devices.md) is a pn junction that emits photons when forward-biased — the semiconductor physics and device manufacturing are covered under [Semiconductor Devices](semiconductor-devices.md). This article teaches the **circuit design**: how to deliver a controlled forward current so the diode lights up brightly, predictably, and without burning out.

The governing rule of LED drive is simple and absolute: **LEDs are current-driven devices, not voltage-driven.** A silicon diode's forward voltage V_F is roughly fixed by its material and color (1.8 V for red, 3.2 V for blue). The supply voltage is whatever the rail provides. The LED will happily draw destructive current the moment V_supply exceeds V_F — so every LED driver is, at its core, a **current limiter**. The four topologies below escalate in sophistication, each solving a limitation of the previous.

---

## 1. Resistor Current Limiting (the simplest driver)

The entry-level circuit: a single [resistor](passive-components.md) in series with the LED. The resistor drops the voltage difference between the supply and the LED's forward voltage, and Ohm's law sets the current.

### The design equation

```
              V_supply
                 │
                 ├─── R_limit ───┐
                 │               │
                                 ▼
                               ┌─┴─┐
                               │   │  LED  (V_F, I_F)
                               │   │
                               └─┬─┘
                                 │
                                GND

    R_limit = (V_supply − V_F) / I_F
```

### Worked example: red LED at 20 mA from a 5 V rail

A standard red indicator LED specifies V_F = 1.8 V at I_F = 20 mA. Driven from a 5 V supply:

```
    R_limit = (5.0 V − 1.8 V) / 0.020 A
            = 3.2 V / 0.020 A
            = 160 Ω
```

The nearest standard value above 160 Ω (always round *up* to reduce current, never down) is **180 Ω**. Recompute the actual current:

```
    I_actual = (5.0 − 1.8) / 180 = 17.8 mA
```

That is 89% of the nominal 20 mA — visibly indistinguishable from full brightness, and well inside the LED's 30 mA absolute-maximum rating. Resistor power dissipation: P = I²·R = (0.0178)²·180 ≈ 57 mW, so a standard 1/4 W resistor is ample.

**When to use this topology:** indicator LEDs, low-power displays, hobby circuits, and any fixed-voltage rail where V_supply exceeds V_F by at least ~1 V. The rule of thumb is that the resistor needs at least 1 V of headroom to swamp out V_F manufacturing variation (±0.3 V typ.) — if V_supply − V_F < 1 V, current becomes wildly sensitive to V_F spread and this topology is the wrong choice.

**Limitation:** current varies with supply voltage and V_F. If V_supply sags (battery discharge) or V_F rises with temperature, brightness drifts. For strings of LEDs, each LED needs its own resistor — paralleling LEDs directly shares current unequally because of V_F mismatch.

---

## 2. Transistor-Driven LED (digital control, higher current)

When the LED must be switched on and off by a logic signal, or when the required current exceeds what the driving source can provide directly, a [bipolar transistor](semiconductor-devices.md) is inserted as a low-side switch. The signal drives the base through a current-limiting resistor; the transistor sinks the LED current through the collector.

```
              V_supply (+5 to +12 V)
                 │
                 ├─── R_limit ───┐
                 │               │
                                 ▼  Collector
                              ┌─────┐
               Logic in ───Rb──┤ B   │
                              │  NPN│ (e.g. 2N3904, TIP31C)
                              ┤     │
                              └──┬──┘
                                 │  Emitter
                                GND
```

The transistor saturates when on (V_CE(sat) ≈ 0.2 V), so almost all of V_supply appears across R_limit. The design has two steps:

1. **Choose R_limit** for the desired LED current, using V_CE(sat) in the drop:
   `R_limit = (V_supply − V_F − V_CE(sat)) / I_F`
2. **Choose R_B** to provide enough base current to saturate. For saturation the base current must exceed I_F / β. In practice use I_B = I_F / 10 (forced β = 10) to guarantee hard saturation regardless of β spread:
   `R_B = (V_logic − V_BE) / (I_F / 10)` where V_BE ≈ 0.7 V.

**Worked example:** drive a 100 mA high-brightness LED from a 12 V rail, controlled by a 5 V logic pin. Use a TIP31C power NPN (β ≈ 25 at 100 mA, but force β = 10).

```
    R_limit = (12 − 2.0 − 0.2) / 0.100 = 98 Ω  → use 100 Ω
    I_B_needed = 100 mA / 10 = 10 mA
    R_B = (5 − 0.7) / 0.010 = 430 Ω  → use 430 Ω
```

The transistor dissipates P = I·V_CE(sat) = 0.1 × 0.2 = 20 mW — negligible. The [transistor-switch circuit](analog-circuits.md) pattern itself is taught in depth under Analog Circuits; this article covers only its LED-specific application.

---

## 3. Constant-Current Driver (consistent brightness, LED strings)

When supply voltage varies (vehicle 12 V systems swinging 10–14.5 V), or when driving **strings** of series LEDs (where total V_F may approach or exceed the rail), a resistor limiter is inadequate. A constant-current source delivers the same current regardless of voltage headroom, keeping brightness stable and protecting the LEDs.

### 3a. LM317 as a 1.25 V constant-current regulator

The LM317 linear regulator holds 1.25 V between its OUT and ADJ pins. Putting a resistor between them forces a fixed current through that resistor; the same current flows through whatever load is in series with the ADJ pin.

```
              V_supply
                 │
                 ├──────┬─────── IN
                 │      │      ┌─────────┐
                 │      │      │  LM317  │
                 │      │      │ Regulator│
                 │      │      └──┬───┬───┘
                 │      │         │   │
                 │      │       OUT   ADJ
                 │      │         │   │
                 │      │         │   ├── R_set
                 │      │         │   │
                 │      │         ▼   ▼
                 │      │       ┌─────┐
                 │      │       │ LED │ (or string of LEDs)
                 │      │       │string│
                 │      │       └──┬──┘
                 │      │          │
                 │      │         GND (returns via load)
                 │      │
                 │      └── I_out = 1.25 V / R_set
                 │
```

The set resistor is breathtakingly simple:

```
    R_set = 1.25 V / I_LED
```

For a 20 mA LED string: R_set = 1.25 / 0.020 = 62.5 Ω → use 62 Ω. The current is locked at 1.25 / 62 = 20.2 mA whether the supply is 9 V or 30 V, as long as there is enough headroom (V_supply ≥ V_string + 3 V for the LM317's dropout). The 1.25 V bandgap reference inside the LM317 is itself a [semiconductor device](semiconductor-devices.md) product.

**Dropout limitation:** the LM317 needs ~3 V of overhead (V_IN − V_OUT ≥ 3 V). For a 4-LED white string (4 × 3.2 = 12.8 V) at 20 mA, the minimum supply is 12.8 + 3 = 15.8 V. Below that, current regulation collapses.

### 3b. Discrete two-transistor current source

When an integrated regulator is unavailable, a constant-current source can be built from two BJTs and two resistors. Q2's emitter resistor senses the current; when the voltage across it reaches V_BE (≈0.65 V), Q2 turns on and steals base drive from Q1, closing the negative-feedback loop.

```
              V_supply
                 │
                 ├─── Load (LED) ───┬── Collector (Q1, NPN)
                 │                  │
                 │                  ├── Base (Q1) ───┐
                 │                  │               │
                 │                  ├── Collector (Q2, NPN, senses)
                 │                  │               │
                 │                  │            ┌──┴── Base (Q2)
                 │                  │            │
                 │                  └── R_sense ─┴── Emitter (Q2) / Emitter (Q1)
                 │                                   │
                 │                                  GND

    I_LED ≈ V_BE / R_sense = 0.65 V / R_sense
```

For 20 mA: R_sense = 0.65 / 0.020 = 33 Ω. The thermal V_BE drift (−2.2 mV/°C) makes this less precise than the LM317 bandgap reference, but it requires no IC.

---

## 4. Multiplexing (driving many LEDs from few pins)

A 7-segment display has 8 LEDs per digit (including decimal point); a 4-digit display is 32 LEDs — far too many to wire individually. **Multiplexing** drives one digit at a time at high current, cycling through digits faster than the eye can perceive (typically >100 Hz refresh). At any instant only one digit's LEDs are lit, but persistence of vision makes all four appear continuously illuminated.

A 4-digit display needs only 8 segment lines + 4 digit-select lines = **12 pins** instead of 32. The arrangement is a matrix of rows (digits) and columns (segments):

```
            Seg A   Seg B   Seg C   ...   Seg DP
              │       │       │              │
   Digit 1 ───┼───────┼───────┼──── ... ─────┤
              │       │       │              │
   Digit 2 ───┼───────┼───────┼──── ... ─────┤
              │       │       │              │
   Digit 3 ───┼───────┼───────┼──── ... ─────┤
              │       │       │              │
   Digit 4 ───┼───────┼───────┼──── ... ─────┤

   At any instant: drive ONE digit-select line low (sink),
   and the segment lines high (source) for LEDs to light on that digit.
   Cycle digit1 → digit2 → digit3 → digit4 → repeat, >100 Hz.
```

**Peak vs. average current:** each digit is on for 1/N of the time (duty cycle = 1/4 for 4 digits). The perceived brightness equals the *average* current. To match the brightness of a continuously-driven LED at 5 mA, each multiplexed LED must pulse at 4 × 5 = 20 mA peak (within the LED's peak-current rating, typically 5–10× the DC rating). The [passive components](passive-components.md) (current-limit resistors) are sized for the peak current, one resistor per segment line (shared across all digits of that segment).

### Charlieplexing

For maximum LED count per pin, **charlieplexing** exploits the tri-state capability of microcontroller pins (high / low / high-impedance). N pins can drive N × (N − 1) LEDs — so 3 pins = 6 LEDs, 5 pins = 20 LEDs, 10 pins = 90 LEDs. Each LED connects between a unique pair of pins; only one LED lights at a time, with all other pins set to high-Z.

```
   3-pin charlieplex, 6 LEDs:

        Pin 1 ───┬── LED1 ► ──┬── LED2 ◄ ──┐
                 │            │            │
        Pin 2 ───┼── LED3 ◄ ──┼────────────┤
                 │            │            │
                 └── LED4 ► ──┴── LED5 ► ──┤
                                              │
        Pin 3 ────── LED6 ◄ ──────────────────┘

   To light LED1: Pin1 = HIGH, Pin2 = LOW, Pin3 = high-Z.
   Current-limiting resistor goes in series with each pin.
```

The trade-off is refresh complexity and lower per-LED duty cycle (each LED is on for 1/(N×(N−1)) of the time), which limits the practical size before brightness suffers.

---

## 5. PWM Dimming (perceived brightness control)

Pulse-width modulation drives the LED at full rated current, but rapidly switches it on and off. The **duty cycle** (fraction of the period the LED is on) controls perceived brightness — the human eye integrates the rapid flicker (>200 Hz) into a steady glow proportional to the average light output.

```
    100% duty (full brightness)      50% duty (half brightness)      25% duty (quarter)
    ┌──────┐ ┌──────┐ ┌──────┐       ┌──┐   ┌──┐   ┌──┐            ┌─┐    ┌─┐    ┌─┐
    │      │ │      │ │      │       │  │   │  │   │  │            │ │    │ │    │ │
    └──────┘ └──────┘ └──────┘       └──┘   └──┘   └──┘            └─┘    └─┘    └─┘
    ←─T─→                         ←─T─→                        ←─T─→
    T = period (e.g. 4 ms → 250 Hz)

    brightness ∝ duty cycle = t_on / T
```

**Why PWM beats analog dimming:** dimming by reducing the DC current shifts the LED's chromaticity (color shifts toward the blue/green at low current in white LEDs) and reduces efficiency. PWM keeps the LED at its optimal current (correct color, rated efficacy) on every pulse — only the *average* light changes. It also permits resolution down to 8-bit (256 levels) or 12-bit (4096 levels) using a digital timer, with zero temperature drift.

PWM dimming stacks cleanly on top of any of the four topologies above — the limiter sets the peak current; a transistor switch (topology 2) modulates that current on and off. This combination is the basis of every LED backlight, photographic light, and dimmable LED bulb.

---

## LED Parameter Reference

Typical V_F, maximum forward current, peak wavelength, and luminous intensity by color. Values are indicative for 5 mm indicator-grade LEDs; high-power illumination LEDs differ markedly.

| Color | V_F (typ., 20 mA) | Max I_F (DC) | Wavelength (nm) | Luminous intensity (mcd, typ.) | Material |
|----------|-------------------|--------------|-----------------|--------------------------------|----------|
| Red | 1.8 V | 30 mA | 620–630 | 2000–5000 | AlInGaP |
| Orange | 2.0 V | 30 mA | 605–620 | 2500–6000 | AlInGaP |
| Yellow | 2.1 V | 30 mA | 585–595 | 3000–8000 | AlInGaP |
| Green (standard) | 2.1 V | 30 mA | 565–570 | 2000–6000 | GaP |
| Green (bright) | 3.2 V | 30 mA | 520–535 | 8000–15000 | InGaN |
| Blue | 3.2 V | 30 mA | 465–470 | 3000–8000 | InGaN |
| White (cool) | 3.2 V | 30 mA | broadband (6500 K) | 8000–20000 | InGaN + phosphor |
| IR (940 nm) | 1.2 V | 50 mA | 940 | — (invisible) | GaAs |

**Peak forward current** (for multiplexing / PWM, ≤ 1 ms pulse, 10% duty): typically 5–10× the DC max — consult the datasheet. **Reverse voltage** is uniformly low: most LEDs are destroyed by V_R > 5 V — never reverse-bias an LED.

---

## Design Heuristics

| Design goal | Recommended topology | Why |
|-------------|---------------------|-----|
| Single indicator LED on fixed rail | Resistor (§1) | One component, lowest cost |
| LED switched by logic | Transistor switch (§2) | Isolates logic from LED current |
| LED on variable supply (battery) | Constant-current (§3a/b) | Brightness stable across discharge |
| Series string (backlight, illumination) | LM317 CC or switching driver | Headroom + matching |
| 4-digit 7-segment display | Multiplexing (§4) | Pin count, average-current trick |
| Many LEDs, few pins | Charlieplexing (§4) | N×(N−1) LEDs from N pins |
| Smooth brightness control | PWM (§5) | Stable color, digital resolution |
| High-power LED (> 350 mA) | Switching constant-current | Thermal + efficiency — see [Power Electronics](power-electronics.md) |

---

## Prerequisites

- [Semiconductor Devices](semiconductor-devices.md) — the LED itself is a forward-biased pn junction; its construction and V_F behavior live there.
- [Passive Components](passive-components.md) — the current-limiting resistors used in every topology here.
- [Analog Circuits](analog-circuits.md) — transistor biasing and the transistor-switch pattern, taught in depth under that capability.
- DC circuit analysis (Ohm's law, series resistance) — covered under the circuit-fundamentals track.

## Scope Boundary

This article covers LED **drive** circuits only. It does **not** cover:

- LED semiconductor physics or manufacturing — see [Semiconductor Devices](semiconductor-devices.md).
- Optocoupler circuits (LED + photodetector in one package) — a separate [Optoelectronic Circuits](optoelectronic-circuits.md) article.
- IR and fiber-optic signaling circuits — a separate article.
- High-power LED illumination power supplies — see [Power Electronics](power-electronics.md).

The inverse process — detecting light with semiconductor devices — is covered in the sibling article [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md).

---


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
