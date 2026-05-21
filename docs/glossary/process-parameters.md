# Process Parameters

> **Type**: noun | **Tier**: critical | **Domains**: chemistry, ceramics, energy, silicon

Moisture content 40-70% (vs >95% for submerged fermentation). Temperature 25-35°C, controlled by forced aeration through the substrate bed. Oxygen supply is critical, as fungal mycelium grows on the particle surface and requires O₂. Aeration rate: 0.5-2.0 vvm. Heat removal is the primary engineering challenge: the solid matrix has poor thermal conductivity, and metabolic heat can raise local temperature 10-20°C above ambient in poorly ventilated beds.

## Context in the Tech Tree

Process parameters are the controllable variables that determine whether an industrial process produces acceptable output. In solid-state fermentation ([Chemistry](../chemistry/fermentation.md)), parameters include moisture content, temperature, aeration rate, and pH. In [Lime Production](../ceramics/lime.md), parameters are kiln temperature, residence time, and fuel-to-stone ratio. In [Silicon Purification](../silicon/purification.md), CVD parameters (temperature, gas flow rate, pressure, deposition time) directly control polysilicon purity and deposition rate. In [Iron & Steel](../metals/iron-steel.md), heat treatment parameters (austenitizing temperature, soak time, cooling rate) determine the final microstructure and mechanical properties.

## Technical Details

Process parameters fall into several categories: temperature (the most universally critical parameter), pressure (critical for vacuum processes, CVD, and distillation), time (residence time, soak time, reaction time), composition (feed ratios, gas concentrations, alloy additions), and flow rates (gas flow, liquid flow, aeration). Each parameter typically has an acceptable window — deviations in either direction degrade product quality or yield.

In semiconductor CVD, for example, temperature controls deposition rate (Arrhenius relationship — rate approximately doubles for every 10°C increase) and film quality (too low = amorphous, too high = rough polycrystalline). Gas flow rate affects uniformity across the wafer. Pressure influences mean free path and therefore film conformity in high-aspect-ratio features.

The interrelationship between parameters is critical: changing one often requires adjusting others. Increasing fermentation temperature speeds reaction but also increases metabolic heat generation, requiring more aeration for cooling — which in turn dries the substrate bed, changing moisture content. Process optimization involves finding the stable operating point where all parameters remain within their acceptable windows simultaneously.

## Related Terms

- [Principle](./principle.md) — the physical or chemical mechanism that the parameters control
- [Procedure](./procedure.md) — the step sequence that sets process parameters
- [Requirements](./requirements.md) — the specifications that process parameters must satisfy

## Appears In

- [Lime Production](../ceramics/lime.md)
- [Silicon Purification](../silicon/purification.md)
- [Iron & Steel Production](../metals/iron-steel.md)
