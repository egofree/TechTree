# Requires

> **Type**: verb | **Tier**: foundational | **Domains**: all

A dependency relationship in the tech tree: capability A requires capability B as a material input (consumed) or tool (reusable). For example, edible plants require botanical knowledge and species identification, enable agriculture and health, and use fire for cooking and processing.

## Context in the Tech Tree

"Requires" is the fundamental dependency verb in the tech tree's knowledge structure. Every capability node has dependencies — materials and tools that must exist before the capability can be implemented. These dependencies are captured in [edges.json](../../data/edges.json) and visualized in the Mermaid dependency diagrams. Understanding what each capability requires is essential for planning the bootstrap sequence: you cannot purify silicon without first producing metallurgical-grade silicon, which requires carbon reductants and quartz, which require mining and charcoal production.

## Technical Details

The tech tree distinguishes two types of requirements: **material** dependencies (consumed inputs — ore is consumed in smelting, fuel is consumed in firing) and **tool** dependencies (reusable infrastructure — a furnace is not consumed, a hammer is not consumed). This distinction matters for resource planning: materials must be continuously supplied, while tools need only be built once and maintained.

Dependency chains can be deep: [Semiconductor Lithography](../vlsi-scaling/lithography.md) requires [Polysilicon](../silicon/purification.md), which requires [MG-Si](../silicon/mg-si-production.md), which requires [Carbon Electrodes](../energy/electrode-manufacturing.md), which requires [Petroleum Coke](../energy/refining.md), which requires [Oil Drilling](../mining/drilling.md), which requires [Steel Tools](../metals/iron-steel.md), which requires [Iron Smelting](../metals/iron-steel.md), which requires [Charcoal](../energy/charcoal.md) and [Bellows](../metals/copper-bronze.md). The chain extends 8+ levels deep — this is why bootstrapping industrial civilization takes decades even with full technical knowledge.

Each "requires" relationship also implies a knowledge requirement: not just the physical material or tool, but the know-how to produce and use it. A blast furnace requires not just firebrick and ore, but the accumulated experience of controlling air flow, managing the burden, and interpreting tapping conditions.

## Related Terms

- [Raw Materials](./raw-materials.md) — the material inputs that capabilities require
- [Requirements](./requirements.md) — formal specifications for inputs and outputs
- [Procedure](./procedure.md) — the know-how that accompanies physical requirements

## Appears In

- [Edible Plants](../plants/edible-plants.md)
- [All domain capability articles](../index.md)
