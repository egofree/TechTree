# Power Processing Unit

> **Node ID**: space-propulsion.electric-ion.power-processing-unit
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-ion`](./electric-ion.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: ion_thrusters
> **Critical**: No

The Power Processing Unit (PPU) converts the spacecraft bus (28–100 V DC) into the multiple isolated, regulated high-voltage outputs the ion thruster requires. It is typically the heaviest single component of an ion propulsion system, accounting for 30–50% of dry mass. PPU efficiency must exceed 90% to avoid dissipating hundreds of watts of waste heat in vacuum. See [Electric Propulsion — Ion](./electric-ion.md) for the integrated context.

## Process Description

1. **Input conditioning**: EMI filtering and inrush current limiting protect the spacecraft bus from PPU switching transients.
2. **Beam supply conversion**: a high-frequency DC-DC converter (50–200 kHz) steps up the bus voltage to 300–2000 V DC at 1–7 A — the dominant output (70–80% of input power).
3. **Discharge supply**: a buck or flyback converter provides 25–40 V at 5–20 A for the discharge cathode.
4. **Accelerator supply**: a negative-output converter provides −100 to −500 V at 1–10 mA for the accel grid bias.
5. **Cathode heater supply**: a low-voltage isolated output (4–10 V, 3–8 A) preheats the cathode emitter for ignition.
6. **Neutralizer keeper**: a 10–25 V, 1–3 A regulated output sustains the neutralizer hollow cathode.
7. **Telemetry and control**: digital controller monitors all outputs, reports telemetry via spacecraft MIL-STD-1553 or SpaceWire bus.

## Key Parameters

- **Input voltage**: 22–100 V DC (spacecraft bus)
- **Beam output**: 300–2000 V DC, 1–7 A (70–80% of total power)
- **Total efficiency**: 90–95% (DC-DC conversion)
- **Power density**: 0.5–1.0 kW/kg (improving with SiC wide-bandgap devices)
- **Isolation**: 3000 V DC between primary and beam secondary
- **Switching frequency**: 50–200 kHz
- **Radiation tolerance**: 25–100 krad TID (total ionizing dose)

## Prerequisites

- High-voltage DC-DC converter design (power electronics heritage)
- Radiation-hardened MOSFETs and control ICs
- Vacuum-impregnated high-voltage transformer potting

## See Also

- [Electric Propulsion — Ion](./electric-ion.md) — parent capability
- [Power Electronics](../electronics/power-electronics.md) — PPU heritage domain
- [Neutralizer Design](./electric-ion.neutralizer-design.md) — powered by PPU keeper output

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
