# Efficiency

> **Type**: noun | **Tier**: critical | **Domains**: chemistry, energy, manufacturing, transport

The ratio of useful output to total input for any process or system. Efficiency is the universal constraint on industrial capability — it determines how much raw material, energy, and labor is required to produce a given output, and therefore what scale of infrastructure is needed to sustain production.

## Context in the Tech Tree

Efficiency appears at every level of the tech tree. In [Fuel Production](../energy/fuels.md), combustion efficiency determines how much heat is extracted from each unit of fuel. In [Electric Furnaces](../energy/electric-furnaces.md), thermal efficiency governs energy cost per tonne of steel. In [Distillation](../chemistry/distillation.md), separation efficiency determines product purity and energy consumption. In [Steam Power](../energy/steam-power.md), thermal efficiency (typically 5-40% depending on configuration) sets the fuel requirement for mechanical work.

Low efficiency in early-stage processes is not a failure — it is the expected starting point. Charcoal production loses 60-80% of wood's energy content as volatile gases. Simple bloomery furnaces capture only 10-20% of charcoal's heating value in the iron product. Each technological improvement (better furnace design, waste heat recovery, regenerative systems) incrementally raises efficiency, reducing the resource base needed to sustain industrial output.

## Technical Details

Efficiency is expressed differently depending on the domain, but the principle is always the same:

- **Thermal efficiency**: η = useful heat output / total heat input. Steam boilers: 60-85%. Internal combustion engines: 20-40%. Combined cycle gas turbines: 55-60%.
- **Electrical efficiency**: η = electrical output / energy input. Generators: 90-98%. Transformers: 95-99%. Transmission lines: 90-95% over moderate distances.
- **Material efficiency**: η = mass of desired product / total mass of input materials. Steelmaking yield: 85-95%. Chemical synthesis: varies widely (30-95%).
- **Mechanical efficiency**: η = useful work output / work input. Gear trains: 95-99% per stage. Belt drives: 93-98%. Bearings: 95-99.5%.

The second law of thermodynamics sets absolute upper limits on thermal efficiency (Carnot efficiency: η_max = 1 - T_cold/T_hot). Real systems always fall short of Carnot due to friction, heat loss, incomplete combustion, and other irreversibilities. The gap between actual and theoretical efficiency is the engineering challenge — each improvement reduces waste and expands what can be accomplished with limited resources.

In bootstrapping, efficiency gains compound. A 10% improvement in furnace efficiency means 10% less fuel to cut, transport, and process — which frees labor and resources for other tasks. This compounding effect is why incremental process improvements matter disproportionately in early industrial development.

## Related Terms

- [Capacity](./capacity.md) — maximum output rate, often limited by efficiency of energy/material conversion
- [Distribution](./distribution.md) — distribution losses reduce overall system efficiency
- [Scaling](./scaling.md) — scaling often changes efficiency characteristics of processes
- [Yield](./yield.md) — material yield is a form of efficiency for production processes

## Appears In

- [Fuel Production](../energy/fuels.md)
- [Electric Furnaces](../energy/electric-furnaces.md)
- [Distillation](../chemistry/distillation.md)
- [Steam Power](../energy/steam-power.md)
- [Electricity](../energy/electricity.md)
