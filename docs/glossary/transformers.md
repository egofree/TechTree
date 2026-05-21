# Transformers

> **Type**: noun | **Tier**: critical | **Domains**: computing, energy

Two coils on shared iron core — alternating current in primary creates changing magnetic flux, inducing voltage in secondary. Turns ratio determines voltage ratio: V₂/V₁ = N₂/N₁. Laminated iron core (thin sheets, 0.3-0.5 mm, insulated with shellac or paper) prevents eddy current losses.

## Context in the Tech Tree

Transformers are essential for electrical power distribution, enabling voltage step-up for efficient long-distance transmission and step-down for safe end use. In [Electricity](../energy/electricity.md), transformers are the key enabling technology that made AC power distribution superior to DC — stepping voltage up to thousands of volts for transmission (reducing I²R losses) and back down to usable levels at the destination. In [Electric Furnaces](../energy/electric-furnaces.md), transformers provide the low-voltage, high-current power needed for arc furnaces and resistance heating. In [Electronic Computing](../computing/electronic.md), transformers provide power supply voltages and signal isolation.

## Technical Details

The transformer operates on Faraday's law of induction: a changing magnetic flux through a coil induces a voltage proportional to the rate of change and the number of turns. The turns ratio N₂/N₁ sets the voltage ratio, while the current ratio inverts (I₂/I₁ = N₁/N₂) to conserve power (minus losses).

Core construction uses laminated iron sheets (0.3-0.5 mm thick) insulated from each other by shellac or paper. This prevents eddy currents — circulating currents in the core that would otherwise convert magnetic energy into waste heat. Thin laminations restrict eddy current paths, reducing losses. At higher frequencies, ferrite cores replace laminated iron.

Winding insulation is critical: enamel-coated copper wire, with additional insulation layers between primary and secondary windings for safety isolation. Shellac, varnished cloth, or paper serve as inter-layer insulation.

Efficiency ranges from 95-99% for well-designed power transformers. Losses include core losses (hysteresis and eddy currents) and copper losses (I²R in windings).

## Related Terms

- [Principle](./principle.md) — electromagnetic induction underlying transformer operation
- [Capacity](./capacity.md) — power rating of transformers
- [Power Requirement](./power-requirement.md) — electrical loads that transformers serve
- [Applications](./applications.md) — voltage conversion uses
- [Construction](./construction.md) — winding and core assembly methods

## Appears In

- [Electricity](../energy/electricity.md)
