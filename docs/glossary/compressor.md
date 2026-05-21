# Compressor

> **Type**: noun | **Tier**: critical | **Domains**: chemistry, energy

Raises refrigerant vapor from low pressure (evaporator) to high pressure (condenser). Four types, in order of complexity: Reciprocating (piston) 2-16 cylinders, 500-3000 RPM. Capacity 5-500 kW. Rotary (scroll/screw). Centrifugal (impeller). Pressure ratio typically 3:1 to 10:1.

## Context in the Tech Tree

Compressors raise gas pressure — a function required at multiple stages. In [Cooling Systems](../energy/cooling.md), the compressor is the heart of vapor-compression refrigeration, driving the refrigerant cycle. In [Air Separation](../chemistry/air-separation.md), multi-stage compressors raise atmospheric air to 5-10 atm before cryogenic distillation. In [Heat Engines](../energy/engine.md), turbochargers use exhaust-driven compressors to force more air into cylinders. In [Energy Storage](../energy/storage.md), compressed air energy storage (CAES) uses compressors to store energy in pressurized vessels.

## Technical Details

The reciprocating (piston) compressor is the most directly buildable type, as it shares architecture with internal combustion engines: crankshaft, pistons, connecting rods, and cylinder valves. It uses 2-16 cylinders at 500-3000 RPM, with capacity from 5-500 kW and volumetric efficiency of 65-85%. Reed or ring-plate valves admit gas on the intake stroke and discharge it on the compression stroke. Multi-stage reciprocating compressors with intercoolers approach isothermal compression, reducing the work required.

Rotary compressors (scroll and screw types) offer higher efficiency and fewer moving parts but require precision machining. Scroll compressors use two interleaving spiral scrolls, one orbiting, to progressively compress gas pockets. Screw compressors use two meshing helical rotors. Both achieve 10-2000 kW capacity.

Centrifugal compressors use a rotating impeller to accelerate gas outward, converting velocity to pressure in a diffuser. Capacity ranges from 300-10,000+ kW, suited for large industrial and district cooling applications. They require high-speed precision rotor balancing.

For air separation, 3-4 stage compressors with inter-stage cooling achieve 5-10 atm. For refrigeration, a single-stage compressor achieves the typical 3:1 to 10:1 pressure ratio needed to drive the vapor-compression cycle. Compressor power: at COP 3.0, a 100 kW cooling load requires ~33 kW electrical input to the compressor.

## Related Terms

- [Limitations](./limitations.md) — compressor efficiency limits and failure modes
- [Advantages](./advantages.md) — benefits of different compressor types
- [Principle](./principle.md) — the thermodynamic principles governing compression
- [Construction](./construction.md) — building compressor components

## Appears In

- [Cooling Systems](../energy/cooling.md)
- [Air Separation](../chemistry/air-separation.md)
- [Heat Engines](../energy/engine.md)
- [Energy Storage](../energy/storage.md)
