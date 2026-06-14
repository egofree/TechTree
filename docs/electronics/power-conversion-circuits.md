# Power Conversion Circuits

> **Node ID**: electronics.power-conversion-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](./semiconductor-devices.md)
> **Enables**:
> **Timeline**: Years 30-50
> **Outputs**: inverter-circuit-design
> **Critical**: No — this is a design-pedagogy capability (circuit-analysis layer); the underlying device manufacturing and system-level drive/converter building are covered by the critical capabilities it depends on.

This capability is the **design-pedagogy layer** for circuits that convert DC back into controlled AC and use that AC to drive motors and loads. It teaches the DC→AC inversion and variable-frequency drive chain that underpins modern motor control, renewable-energy grid injection, and uninterruptible power:

```
  Fixed DC ──▶ [ Inverter (H-bridge + SPWM) ] ──▶ [ Output Filter ] ──▶ Controlled AC ──▶ [ Motor / Load ]
              synthesizes AC waveform             reduces switching harmonics   V/f or vector controlled
```

## The Inverter→VFD Progression

1. **Inverter circuits** — the DC→AC building block. An H-bridge of four switching devices (MOSFETs or IGBTs) chops the DC bus into a synthesized AC waveform via pulse-width modulation. Sinewave PWM (SPWM) compares a sinusoidal reference against a triangular carrier to produce a duty-cycle sequence whose average is a clean sine wave. Design concerns: switch selection, dead-time generation, gate-drive isolation, dv/dt management. *Article: inverter-circuits (forthcoming).*

2. **Variable-frequency drive (VFD)** — an inverter wrapped in the control architecture needed to spin an AC induction or PM motor at adjustable speed/frequency. A VFD chains a rectifier (AC mains → DC bus), a DC-bus capacitor bank, and a controlled inverter, governed by a V/f or field-oriented-control (FOC) loop. Design concerns: V/f ratio holding, carrier-frequency vs. efficiency tradeoff, bearing-current mitigation. *Article: vfd-motor-control (forthcoming).*

## Boundary with Power Electronics

This capability is **distinct from** [power-electronics](power-electronics.md):

| Aspect | power-conversion-circuits (this) | power-electronics |
|--------|----------------------------------|-------------------|
| Focus | **Circuit design & analysis** of inverter/drive topologies | **System-level** converter/drive manufacturing & deployment |
| Scope | H-bridge, SPWM, gate-drive, V/f & FOC design pedagogy | Rectifiers, inverters, DC-DC, motor drives, UPS as built systems |
| Output | Design knowledge (inverter-circuit-design token) | Manufactured inverters, drives, UPS hardware |

The VFD section currently consolidated under [power-electronics](power-electronics.md) will be migrated (expanded as design pedagogy) into this capability's forthcoming vfd-motor-control article, leaving a cross-link behind. Until then, treat power-electronics as the authoritative VFD reference and this capability as the analytical companion.

## Prerequisites

- [Semiconductor devices](semiconductor-devices.md) — MOSFETs and IGBTs (the H-bridge switches), freewheel diodes, gate-drive transistors.
- [Electrical systems](electrical-systems.md) — motor theory, transformers, mains interface (linked from drive articles).
- [Passive components](passive-components.md) — DC-bus electrolytics, snubber RC networks, output-filter inductors.

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
