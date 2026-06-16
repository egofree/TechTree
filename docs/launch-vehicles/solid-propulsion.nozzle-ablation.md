# Nozzle Ablation

> **Node ID**: launch-vehicles.solid-propulsion.nozzle-ablation
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.solid-propulsion`](./solid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: nozzle_assemblies
> **Critical**: No

Nozzle ablation is the design and fabrication of sacrificial, erosion-resistant nozzles for solid rocket motors. The nozzle throat sees the highest heat flux (10-50 MW/m²) and must survive the full burn duration without eroding open. This process is part of the [Solid Propulsion](./solid-propulsion.md) capability.

## Ablative Architecture

Solid motor nozzles are designed to char and shed material sacrificially, carrying heat away through pyrolysis-gas outgassing and material recession. A multi-layer stack handles the temperature gradient from the throat (2,500-3,500°C) to the housing (room temperature):

- **Carbon-carbon throat insert**: carbon fiber in a carbon matrix, densified by chemical vapor infiltration (CVI). Withstands 2,500-3,500°C continuously. Used in the Shuttle SRB throat. Manufacturing takes weeks of CVI per part; expensive but the standard for large motors.
- **Graphite sections**: cheaper than carbon-carbon, used in entrance and exit sections and in smaller motor throats. Nuclear-grade graphite (G-90, AXF-5Q) machines well at 2,500°C but erodes faster than carbon-carbon.
- **Ablative liners**: phenolic resin tape wound on a mandrel and cured, or silica-phenolic and carbon-phenolic composites. The phenolic pyrolyzes at 500-800°C, releasing fuel-rich pyrolysis gases that film-cool the surface, while the char layer recedes slowly. A carbon-phenolic throat liner survives 100+ seconds of solid-motor exhaust.

## Thrust Vector Control

Moveable nozzles provide thrust vector control (TVC):
- **Flex bearing**: a rubber-metal composite bearing between the fixed housing and the moveable nozzle, allowing ±8° gimbal. Used on the Shuttle SRB and SLS SRB.
- **Hydraulic actuation**: two or four hydraulic actuators gimbal the nozzle in response to guidance commands.

## Heritage Example

The Shuttle SRB nozzle: carbon-carbon throat insert, carbon-phenolic entrance and exit liners, steel housing, 1.2 m exit diameter, gimbaled ±8° by hydraulic actuators. Burn duration 123 seconds with acceptable throat erosion (throat diameter growth <5%, within thrust-tolerance margin).

See [Solid Propulsion](./solid-propulsion.md) for how the nozzle integrates with the full motor, and [Hybrid Propulsion](./hybrid-propulsion.md) for the shared nozzle technology.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
