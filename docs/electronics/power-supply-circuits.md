# Power Supply Circuits

> **Node ID**: electronics.power-supply-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](./semiconductor-devices.md), [`electronics.electrical-systems`](./electrical-systems.md)
> **Enables**:
> **Timeline**: Years 20-40
> **Outputs**: regulated-dc-power
> **Critical**: No — this is a design-pedagogy capability (circuit-analysis layer); the underlying device manufacturing and system-level converter building are covered by the critical capabilities it depends on.

This capability is the **design-pedagogy layer** for the circuits that convert raw AC mains or a coarse DC source into clean, regulated DC power. It teaches the canonical three-stage power-supply chain that every bench supply, battery charger, and embedded-system brick follows:

```
 AC or raw DC ──▶ [ Rectifier ] ──▶ [ Filter ] ──▶ [ Regulator ] ──▶ Clean DC
 (uncontrolled)   AC → DC         reduce ripple   hold V_out fixed   (regulated)
```

## The Three-Stage Progression

1. **Rectifier** — converts AC to pulsating DC using diode topologies (half-wave, full-wave, bridge, polyphase). This is where [semiconductor-devices](semiconductor-devices.md) diode physics meets circuit topology. *Article: [rectifier-circuits](power-supply-circuits.rectifier-circuits.md).*

2. **Filter** — smooths the rectifier's pulsating waveform into a near-DC level with residual ripple, using passive LC networks (capacitor-input, π-section, choke-input). The design leverages [passive components](passive-components.md) and the reactance/impedance theory from AC analysis. *Article: [filter-circuits](power-supply-circuits.filter-circuits.md).*

3. **Regulator** — holds the output voltage (or current) constant against line and load variation. Two families:
   - **Linear regulators** — series/shunt pass elements, zener references, LDOs. Simple, low-noise, dissipative.
   - **Switching regulators** — buck, boost, buck-boost, flyback. High efficiency via PWM-controlled inductor energy transfer.

   *Articles: [linear-regulators](power-supply-circuits.linear-regulators.md), [switching-regulators](power-supply-circuits.switching-regulators.md).*

## Boundary with Power Electronics

This capability is **distinct from** [power-electronics](power-electronics.md):

| Aspect | power-supply-circuits (this) | power-electronics |
|--------|------------------------------|-------------------|
| Focus | **Circuit design & analysis** of supply topologies | **System-level** converter manufacturing & integration |
| Scope | Rectifier→filter→regulator design pedagogy | Rectifiers, inverters, DC-DC, motor drives, UPS as deployed systems |
| Output | Design knowledge (regulated-dc-power token) | Manufactured converters, drives, UPS hardware |

When a design choice here becomes a system-integration concern (thermal management of a 1 kW supply, grid-tie compliance, motor-drive packaging), it crosses into power-electronics territory. The two capabilities cross-link rather than overlap.

## Prerequisites

- [Semiconductor devices](semiconductor-devices.md) — diodes (rectifiers), transistors/MOSFETs (regulators), zener/bandgap references.
- [Electrical systems](electrical-systems.md) — transformers, mains wiring, safety grounding, fusing.
- [Passive components](passive-components.md) — capacitors (reservoir/filter), inductors (chokes, switching energy storage), resistors (bleeder, divider).

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
