# Analog Circuits

> **Node ID**: electronics.analog-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](../silicon/basic-devices.md), [`electronics.passive-components`](passive-components.md)
> **Timeline**: Years 20-45
> **Outputs**: analog-signal-processing
> **Critical**: No — pedagogy layer; underlying active and passive device manufacturing capabilities are the critical prerequisites

This capability is the **design pedagogy hub** for every major analog circuit family that processes continuous signals. It does not re-explain how diodes, transistors, resistors, or capacitors are *made* — that is owned by [semiconductor devices](../silicon/basic-devices.md) and [passive components](passive-components.md). Instead it teaches how to *analyze and design* with those components: how to bias a transistor, close a feedback loop around an op-amp, satisfy the Barkhausen criterion in an oscillator, and predict the free-running frequency of a 555 timer.

## The Pedagogical Progression

Analog circuit design is learned as a ladder. Each rung unlocks the next:

```
  diode/transistor-switch          <-- entry: a single nonlinear device as a switch or clipper
        |
  amplifier fundamentals           <-- small-signal BJT/MOSFET: bias, gain, impedance
        |
  op-amp circuits                  <-- ideal op-amp model, feedback, active filters, Schmitt
        |
  multivibrators                   <-- astable/monostable/bistable: the bridge to timing
       / \
oscillators   timers               <-- frequency selection (LC/RC/crystal) & the 555
```

This thread maps directly onto the Forrest M. Mims III notebook sequence — *Basic Semiconductor Circuits* → *Op Amp IC Circuits* → *555 Timer Circuits* — which has trained three generations of working engineers from first principles.

## Prerequisites (manufacturing, linked not duplicated)

- **[Semiconductor devices](../silicon/basic-devices.md)** — supplies the diodes, BJTs, MOSFETs, and thyristors these circuits are built from. Design pedagogy assumes they exist as catalog parts with known datasheets (V_F, h_FE, g_m, V_th).
- **[Passive components](passive-components.md)** — supplies the resistors that set bias points, the capacitors that couple and bypass signals, and the inductors that select frequency in LC tanks.
- **DC and AC circuit analysis** — Ohm's and Kirchhoff's laws, impedance, reactance. These fundamentals are the shared bedrock under every article in this family.

## Articles in this family

| Article | Scope | Key circuits |
|---------|-------|--------------|
| [diode-circuits](analog-circuits.diode-circuits.md) | diode as nonlinear element | clipper, clamper, detector, protection |
| [transistor-switch-circuits](analog-circuits.transistor-switch-circuits.md) | BJT/MOSFET as a switch | LED driver, relay driver, light-activated switch |
| [amplifier-fundamentals](analog-circuits.amplifier-fundamentals.md) | small-signal amplification | common-emitter/source, biasing, coupling |
| [power-amplifiers](analog-circuits.power-amplifiers.md) | power-stage classes | class A/B/AB/D, efficiency, heat |
| [op-amp-circuits](analog-circuits.op-amp-circuits.md) | op-amp feedback topologies | inverting, non-inverting, integrator, Schmitt, active filters |
| [multivibrator-circuits](analog-circuits.multivibrator-circuits.md) | regenerative timing | astable, monostable, bistable |
| [oscillator-circuits](analog-circuits.oscillator-circuits.md) | frequency generation | RC phase-shift, Colpitts/Hartley, Wien-bridge, crystal (Pierce) |
| [timer-circuits](analog-circuits.timer-circuits.md) | the 555 and its kin | astable, monostable, PWM, delay/flasher/tone |

## Cross-references

- [Power supply circuits](power-supply-circuits.md) — rectifiers, filters, and regulators feed these analog stages.
- [Interface circuits](interface-circuits.md) — ADCs/DACs consume the op-amp comparator and active-filter techniques taught here.
- [Power electronics](power-electronics.md) — system-level converter manufacturing; this family owns the circuit-level *design pedagogy*.

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
