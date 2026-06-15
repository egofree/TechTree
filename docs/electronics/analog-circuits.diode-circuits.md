# Diode Circuits

> **Node ID**: `electronics.analog-circuits.diode-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md)
> **Enables**: None
> **Outputs**: diode-circuit-designs
> **Timeline**: Years 20-30
> **Critical**: No — design pedagogy layer; the underlying diode manufacturing (semiconductor-devices) is the critical prerequisite

This is the first active circuit a practitioner builds. A diode on its own is a two-terminal lump of doped silicon (see [Semiconductor Devices](semiconductor-devices.md) for how it is made); wired into a network with resistors, capacitors, and inductors from [Passive Components](passive-components.md) it becomes a clipper, a clamper, a detector, a protective snubber, or the heart of a voltage multiplier. This article teaches how to *design* all of those circuits from one piecewise-linear model, without re-deriving the underlying pn-junction physics.

## The One Model You Need

Every circuit below is analyzed with the **piecewise-linear diode model**:

- **Forward biased** (anode > cathode by V_F): the diode is a ~0.7 V battery (Si). It conducts any current.
- **Reverse biased** (anode < cathode): the diode is an open circuit. Zero current.
- **Breakdown** (reverse voltage exceeds V_R): used deliberately only in Zener regulation circuits (out of scope here — see power-supply-circuits).

That is the whole trick. V_F depends on diode chemistry: ~0.7 V for silicon, ~0.3 V for germanium, ~0.2-0.4 V for Schottky, ~1.8-3.3 V for an LED (see parameter table below).

## Clipper Circuits

A clipper *limits* (clamps) a signal so it never exceeds a threshold — protecting a sensitive input, shaping a waveform, or extracting a sync tip.

### Series clipper (positive peak removed)

The diode is in series with the signal; it blocks the half-cycle that would forward-bias it, passing only the negative half.

```
           D1 (anode->cathode, pointing right)
 Vin --|>|--*-- Vout          D1 conducts on NEGATIVE half-cycles
              |               (reverse of arrow), blocking positive.
             Rload
              |
             GND
```

Wait — orient it so the cathode faces the source and the diode conducts only when Vin < 0:

```
          D1  (cathode toward source)
 Vin --|<|--*-- Vout          Conducts only when Vin < -V_F.
             |               Positive half-cycle: diode reverse-biased,
            Rload            Vout clamped to ~0 V.
             |
            GND
```

### Shunt (parallel) clipper — the canonical ±0.7 V limiter

Far more common: the diode sits *across* the load. Two anti-parallel diodes clip *both* peaks to ±V_F. This is the standard input-protection circuit on every multimeter and logic input.

```
                Rseries
 Vin ---/\/\/\---*--------*-- Vout
                 |        |
                D1|<|   D2|>|
                 |        |
                GND------GND

  D1 clips the NEGATIVE peak at -0.7 V (anode at GND).
  D2 clips the POSITIVE peak at +0.7 V (cathode at GND).
  Rseries limits current during clipping: I = (Vin - 0.7) / Rseries.
```

### Biased clipper (clip at an arbitrary level)

Add a DC reference (battery or Zener) in series with the diode to set the clip threshold wherever you want. Clip at +3.3 V to protect a 3.3 V logic input:

```
                Rseries
 Vin ---/\/\/\---*-----------*-- Vout
                 |           |
                 |          D2|>|  <-- clips at Vref + V_F
                 |     +3.3V  |       = 3.3 + 0.7 = 4.0 V
                 |      |    GND
                 |     Vref
                 |      |
                 |     D1|<|  <-- clips negative at -0.7 V
                 |      |
                GND----GND
```

### Worked example — design a clipper that limits a signal to ±0.7 V

Given: a 10 V peak-to-peak (±5 V) audio signal from a low-impedance source must be reduced to ±0.7 V before entering a 1 kΩ logic input.

1. **Topology**: shunt clipper with two anti-parallel silicon diodes (1N4148) across the load.
2. **Series resistor**: sized so peak clipping current stays well within the diode's 300 mA rating. The source is 5 V peak; the diode holds Vout at 0.7 V, so the resistor drops 4.3 V at the peak. Choose I_clip = 4.3 mA (conservative, 100× below rating):

   `Rseries = (Vpeak - V_F) / I_clip = (5.0 - 0.7) / 4.3 mA = 1.0 kΩ`

3. **Load interaction**: the 1 kΩ load in parallel with the diode during clipping is fine — at Vout = 0.7 V the load draws only 0.7 mA, leaving 3.6 mA through the diode. Verify diode power: P = V_F × I = 0.7 × 3.6 mA = 2.5 mW (far below the 500 mW limit).
4. **Result**: Vout never exceeds ±0.7 V. Rseries = 1 kΩ.

## Clamper Circuits (DC Restorer)

A clamper *shifts* the DC level of a signal without changing its shape — it "restores" a lost DC component. The classic negative clamper shifts the waveform so its positive peak sits at 0 V:

```
          C1          D1 (cathode to GND)
 Vin --||--*--|<|--*-- Vout
              |    |
              |   Rload   C1 charges to Vpeak on first negative half-cycle
              |    |      through D1; thereafter Vout = Vin + Vpeak.
             GND  GND     (shifts the whole wave UP so the negative peak = ~0)
```

On the first negative half-cycle, D1 conducts and charges C1 to the peak voltage with the polarity shown. Once charged, C1 acts as a battery in series with Vin, shifting the entire waveform up. The positive peak, formerly at +Vpeak, now sits at 0 V; the negative peak, formerly at -Vpeak, now sits at +Vpeak... actually with the diode clamping the most negative point to -V_F, the waveform is shifted so its top is near ground. Adding a bias battery in series with the diode clamps at an arbitrary DC level.

A clamper followed by a clipper is the basis of a **DC restorer** in video and sync circuits: it re-establishes a known DC reference on an AC-coupled signal.

## Protection: Freewheeling (Flyback) Diode for Inductive Loads

When current through an inductor (relay coil, solenoid, motor winding) is interrupted, the inductor opposes the change (`V = -L·di/dt`) and can generate hundreds of volts of reverse spike — destroying the driving transistor and arcing switch contacts. A freewheeling diode gives that stored energy a safe circulation path.

```
                  +V (+12 V)
                   |
                   )||  Relay coil
                   )||  (inductor, L = 150 mH, R = 240 Ω)
                   |
          D1  (|<|)--*   freewheeling diode, cathode toward +V
                   |
                   *------*-- to transistor collector / switch
                   |      |
                  ( )    switch (was ON, now opening)
                          |
                         GND

  While switch is ON:  current flows +V -> coil -> switch -> GND.
                       D1 is reverse-biased (cathode at +12, anode at ~0).
  At turn-OFF:         coil voltage flips to keep current flowing.
                       Without D1: anode spike flies to +V + L·di/dt (hundreds
                         of volts, destroying the switch).
                       With D1:    diode forward-biases, current circulates
                         through coil -> D1 -> coil, decaying as I·R/L.
```

### Worked example — freewheeling diode for a relay coil

Given: a 12 V relay with a 240 Ω coil (50 mA holding current, L = 150 mH), switched by a transistor at 25 °C.

1. **Steady current** (the current the diode must handle at the moment of turn-off): I = V/R = 12/240 = 50 mA.
2. **Diode voltage rating**: must block the supply when OFF. The 1N4148 (75 V PIV) suffices; the 1N4001 (50 V) is the conventional choice and more robust. Choose 1N4001.
3. **Diode current rating**: the initial circulating current equals the steady-state coil current (50 mA). A 1 A rectifier has 20× margin.
4. **Decay time constant**: τ = L/R = 0.150/240 = 0.625 ms. The coil energy (½·L·I² = ½·0.150·0.05² = 188 µJ) dissipates mostly in the coil resistance over ~3τ ≈ 1.9 ms. The relay releases after the current falls below its dropout threshold.
5. **Orientation**: cathode to +V, anode to the collector. Verify with a meter before powering — a reversed diode shorts the supply through the coil on turn-on.
6. **Trade-off**: the diode slows relay release (current decays exponentially). For fast release, add a Zener (e.g. 18 V) in series opposing — it lets the collector fly to 12 + 18 = 30 V, decaying ~4× faster while still clamping below the transistor's V_CEO.

## Detector / Envelope Circuit

A diode + RC low-pass extracts the amplitude envelope of an AM (amplitude-modulated) RF carrier — the simplest radio receiver front end ("crystal radio" principle).

```
   RF in (antenna)                   AF out (to headphones)
        |                                  |
       C1 (tuning, LC tank selects freq)   |
        |                                  |
        *---|>|---*----/\/\/\----*-- Vout
        |   D1    |      Rload    |
        |  (germanium or Schottky C2      (Rload*C2 time constant
        |   for low V_F)        |        >> carrier period 1/f_c
        |                        |        << envelope period 1/f_m)
       GND                      GND
```

D1 rectifies the RF carrier (Germanium 1N34A or Schottky 1N5819 preferred — their low V_F of ~0.3 V detects small signals that a Si diode's 0.7 V would swallow). C2 charges to the carrier peaks and discharges through Rload slowly enough to track the audio envelope but fast enough to follow the modulation. The design constraint is `1/f_carrier << Rload·C2 << 1/f_modulation`. For a 1 MHz carrier with 5 kHz audio: choose Rload·C2 ≈ 100 µs (e.g. Rload = 47 kΩ, C2 = 2.2 nF).

## Voltage Multiplier

Diodes and capacitors can stack peak voltages to produce a DC output several times the AC input peak — useful for high-voltage, low-current loads (CRT anodes, photomultiplier supplies, bug zappers) without a transformer.

### Voltage doubler (half-wave, Villard cascade)

```
                                              +2·Vpeak DC
   AC in ~AC                      D2  |<|       |
        |                          /----------* |
        *---||---*----*     D1 |<|            | |
        |   C1   |    |      /---*            | |
        |        |    *------*   |            C2
       GND      GND              |            | |
                              ~Vpeak        GND |
                                             (Vout = 2·Vpeak)
```

On the negative half-cycle, D1 charges C1 to V_peak (clamping the input). On the positive half-cycle, the input adds to C1's charge and D2 charges C2 to 2·V_peak. Each stage added stacks another V_peak. A tripler adds one more diode-capacitor stage; a quadrupler, two more. Regulation is poor — output droops with load current — because the capacitors are charged in series only on specific half-cycles.

## Parameter Table — Diode Selection

| Diode type | Typical V_F | Max current (continuous) | Switching speed | Best application |
|------------|-------------|--------------------------|-----------------|------------------|
| Silicon signal (1N4148) | 0.6-0.7 V | 300 mA | 4 ns (fast) | Clippers, detectors, logic, small-signal clamping |
| Silicon rectifier (1N400x) | 0.7-1.0 V | 1 A | 30 µs (slow) | Freewheeling for relays, low-freq rectification |
| Germanium (1N34A, 1N60) | 0.2-0.3 V | 5-50 mA | fast | Envelope detector / crystal radio (low V_F catches weak signals) |
| Schottky (1N5817-5819) | 0.2-0.4 V | 1-3 A | <50 ns (fast) | Low-loss clipper, flyback protection, fast detectors |
| LED (red/green/blue/white) | 1.8 / 2.1 / 3.2 / 3.3 V | 20-30 mA | slow (µs) | Indicator (use a series resistor — the LED is the load, not a clipper) |
| Zener (reverse breakdown) | (uses V_Z, not V_F) | 20 mA - 1 A | — | Voltage reference / clamp at a set level (see power-supply-circuits) |

## Design Checklist

- [ ] Identified whether the diode should be series or shunt for the function required.
- [ ] Computed peak diode current during clipping/freewheeling and confirmed it is < 1/5 of the datasheet rating.
- [ ] Sized the series resistor to limit clipping current without loading the source excessively.
- [ ] For inductive loads: confirmed diode polarity (cathode to +V) and PIV ≥ supply voltage with margin.
- [ ] For detectors: verified R·C time constant sits between the carrier and modulation periods.
- [ ] For multipliers: confirmed load current is low enough that droop is acceptable.


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

## See Also

- [Semiconductor Devices](semiconductor-devices.md) — how diodes are manufactured (pn junction, doping, V_F origins); this article links, not re-derives.
- [Passive Components](passive-components.md) — the resistors, capacitors, and inductors every circuit above relies on.
- [Transistor Switch Circuits](analog-circuits.transistor-switch-circuits.md) — the sibling entry point: the freewheeling diode protects the transistor discussed there.
- [Analog Circuits](analog-circuits.md) — the parent capability hub.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
