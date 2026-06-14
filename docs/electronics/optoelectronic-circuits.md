# Optoelectronic Circuits

> **Node ID**: electronics.optoelectronic-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md)
> **Timeline**: Years 25-50
> **Outputs**: optoelectronic-interface
> **Critical**: No — optoelectronic circuits extend electronics into light-based sensing, signaling, and isolation, but they are not on the minimum-viable bootstrap critical path

Optoelectronic circuits convert between electrical energy and photons. Where [semiconductor devices](semiconductor-devices.md) exploit the behavior of charge carriers in solids for amplification and switching, optoelectronic circuits exploit the **emission** of light (LEDs, IR diodes, laser diodes) and the **absorption** of light (photodiodes, phototransistors, light-dependent resistors) to bridge the electrical and optical domains. The third family — **optocouplers** — uses an LED and a photodetector in one package to transfer signals across an isolation barrier with no galvanic connection.

This capability is the design-pedagogy hub for the Forrest Mims III *Optoelectronics Projects* thread. It does **not** re-cover LED or photodiode manufacturing (that belongs to [semiconductor devices](semiconductor-devices.md)); instead it teaches how to **design and analyze** the driver, sensor, and isolation circuits that use those components.

## Learning Progression

The family follows a natural pedagogical arc — each stage adds one new idea on top of the previous:

```
 LED Driver        Photodetector        Optocoupler
 Circuits    →     Circuits       →     Circuits
 (emit light)      (sense light)        (isolate + transfer)
     │                  │                     │
     ▼                  ▼                     ▼
 constant-current   transimpedance        galvanic isolation
 PWM dimming         light-activated       noise immunity
 multiplexing        switch                high-voltage safety
```

1. **LED-driver circuits** — The simplest optoelectronic circuit: drive an LED with a controlled current. Teaches constant-current limiting (resistor → transistor → dedicated driver), PWM dimming, and multiplexing. This is also the entry point for [transistor-switch circuits](analog-circuits.md), since every LED driver is fundamentally a current-controlled switch.
2. **Photodetector circuits** — The inverse: convert light into an electrical signal. Covers photodiode transimpedance amplifiers (current → voltage), phototransistor switches (light-activated / dark-activated relays), and light-dependent-resistor bridges. The key new concept is **transimpedance** — amplifying a tiny photocurrent into a usable voltage.
3. **Optocoupler circuits** — Combine an LED and a photodetector in one sealed package to transfer digital or analog signals across an isolation barrier. Teaches current-transfer ratio (CTR), isolation voltage ratings, and the design patterns for digit isolating switch-mode feedback, triac-driving zero-cross solid-state relays, and medical/industrial isolation. The key new concept is **galvanic isolation** — breaking ground loops and protecting low-voltage logic from high-voltage power circuitry.

## Why It Matters

Optoelectronic circuits are the foundation for:

- **Isolated feedback in power supplies** — every [switching regulator](power-electronics.md) uses an optocoupler to close the feedback loop across the isolation barrier between primary and secondary.
- **Industrial sensing** — photodiode and phototransistor circuits detect presence, position, and count in [automation](../automation/index.md) and manufacturing.
- **Fiber and IR signaling** — the lowest-complexity wireless data links (IR remote, fiber-optic serial) are LED-driver + photodetector pairs operating at a carrier the human eye cannot see.
- **Safety interlocks** — light curtains and optical interrupters protect operators around machinery without physical contact.

## Prerequisites

- [Semiconductor Devices](semiconductor-devices.md) — LEDs, photodiodes, and phototransistors are the active components; you must be able to manufacture them first.
- DC circuit analysis (Ohm's law, series/parallel, transistor biasing) — covered under the circuit-fundamentals track.

## Scope Boundary

This is the **overview hub**. The deep design articles — worked current-limiting calculations, transimpedance amplifier examples, optocoupler CTR tradeoffs, ASCII schematics, and parameter tables — live in the process-level articles that follow this capability:

- [LED-driver circuits](optoelectronic-circuits.led-driver-circuits.md) (Mims *Optoelectronics* entry point)
- [Photodetector circuits](optoelectronic-circuits.photodetector-circuits.md)
- [Optocoupler circuits](optoelectronic-circuits.optocoupler-circuits.md) (isolation design)
- IR and fiber-optic signaling circuits (covered within the articles above)

For the broader RF/wireless communications thread (modulation, RF oscillators, receivers), see [Communications Circuits](communications-circuits.md).

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](./index.md)*
