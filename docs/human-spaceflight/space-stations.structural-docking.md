# Structural Docking + Berthing

> **Node ID**: human-spaceflight.space-stations.structural-docking
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.space-stations`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: docking_systems, space_stations
> **Critical**: Yes

Structural docking and berthing mechanisms provide the mechanical, fluid, and electrical interfaces between independently launched modules and visiting vehicles. The two dominant systems on the ISS are the Common Berthing Mechanism (CBM) — a robotic-arm-positioned interface with a 1.27 m square hatch — and the Probe-and-Drogue / Hybrid system used for Russian segment self-docking vehicles.

Berthing differs from docking: a berthing interface is passive during approach, with the approaching module positioned by the [robotic arm](./space-stations.robotic-arms.md). Docking interfaces are active — the visiting vehicle uses its own propulsion to drive into the interface and capture.

## Key Parameters

| Parameter | CBM | Probe-Drogue | IDA (NDS) |
|-----------|-----|-------------|-----------|
| Hatch shape | Square (1.27 m) | Circular (0.8 m) | Circular (0.8 m) |
| Capture method | Robotic arm positioned | Vehicle propulsion | Vehicle propulsion |
| Bolts | 16 × M16 powered | Latches (mechanical) | Hooks + bolts |
| Seal | Dual O-ring | Single O-ring | Dual O-ring |
| Active/passive | Yes/No halves | Probe (active)/Drogue | Androgynous |

## CBM Berthing Sequence

1. Robotic arm grapples visiting vehicle FRGF
2. Arm translates module to ±25 mm alignment at CBM interface
3. Capture latches actuate — soft capture achieved
4. 16 powered bolts drive — hard capture at 16,330 N each
5. Dual O-ring seal verified; hatch cleared for opening

## Prerequisites

- [Space Stations](./space-stations.md) — parent capability
- [Metals](../metals/index.md) — titanium and steel for latch mechanisms
- [Machine tools](../machine-tools/index.md) — interface ring precision machining
- [Construction](../construction/index.md) — alignment and shimming

## See Also

- [Space Stations](./space-stations.md) — parent capability
- [Habitat Module Fabrication](./space-stations.habitat-modules.md) — sibling process
- [Logistics Resupply](./space-stations.logistics-resupply.md) — uses docking interfaces
