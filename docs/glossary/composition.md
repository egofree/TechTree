# Composition

> **Type**: noun | **Tier**: important | **Domains**: chemistry, metals, ceramics

The chemical and physical makeup of a material — what elements, compounds, and phases it contains and in what proportions. Composition determines every material property: melting point, strength, conductivity, reactivity, color, and durability. Controlling composition is the fundamental skill that separates primitive metalworking from industrial metallurgy, and folk pottery from engineered ceramics.

## Context in the Tech Tree

Composition control appears throughout the tech tree. In [Copper & Bronze Production](../metals/copper-bronze.md), alloy composition (tin content 5-15%) determines whether the casting is hard and brittle or soft and ductile. In [Iron & Steel Production](../metals/iron-steel.md), carbon content (0.05-2.0%) is the difference between wrought iron, mild steel, and cast iron — materials with vastly different properties from the same base element. In [Glass Production](../glass/basic.md), the ratio of silica to soda to lime controls melting temperature, workability, and chemical resistance.

In [Steelmaking](../metals/steelmaking.md), the composition of the sintering mix (ore fines, flux, coke breeze) determines the permeability, strength, and reducibility of the sinter product. In [Blast Furnace](../metals/blast-furnace.md) operations, the composition of furnace atmospheres (CO/CO₂ ratio) determines whether the atmosphere is reducing or oxidizing — critical for controlling metal quality.

## Technical Details

Composition is measured through several methods, each available at different stages of the bootstrap:

- **Visual and physical tests** (earliest): fracture surface color and grain reveal approximate carbon content in steel (bright crystalline = low carbon, grey = high carbon). Spark testing on a grinding wheel gives composition clues from spark color and pattern.
- **Chemical analysis** (intermediate): wet chemistry methods — dissolving samples and titrating or gravimetrically determining constituent elements. Accurate but slow (hours per sample).
- **Spectroscopic analysis** (advanced): optical emission spectroscopy (OES) vaporizes a small sample and analyzes the emission spectrum to determine elemental composition in seconds. Requires calibrated reference standards.

The critical insight for bootstrapping is that approximate composition control (within 1-2%) is achievable through careful process control even without analytical instruments — by controlling input materials, temperatures, and processing times consistently. Precise composition control (within 0.1% or better) requires analytical feedback, but most industrial applications tolerate 0.5-1% variation.

## Related Terms

- [Heat Treatment](./heat-treatment.md) — heat treatment changes microstructure without changing bulk composition
- [Carbon Monoxide](./carbon-monoxide.md) — CO as a component of producer gas and furnace atmospheres
- [Sintering](./sintering.md) — sintering mix composition determines product quality

## Appears In

- [Copper & Bronze Production](../metals/copper-bronze.md)
- [Iron & Steel Production](../metals/iron-steel.md)
- [Glass Production](../glass/basic.md)
- [Steelmaking](../metals/steelmaking.md)
