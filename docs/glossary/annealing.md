# Annealing

> **Type**: process | **Tier**: critical | **Domains**: glass, metals, vlsi-scaling

(Damage recovery + dopant activation): Implantation amorphizes the crystal lattice. Anneal restores crystallinity and moves dopants to substitutional sites. Furnace anneal: 900-1050°C, 30-60 min in N₂. Rapid thermal anneal (RTA): Ramp to 1000-1100°C in seconds, hold 10-30 sec, cool. Minimizes dopant redistribution.

## Context in the Tech Tree

Annealing — heating a material to a specific temperature and cooling it under controlled conditions — appears at three distinct scales in the tech tree. In [Basic Glass Production](../glass/basic.md), annealing removes internal thermal stress from glassware. In [Copper & Bronze](../metals/copper-bronze.md) and [Iron & Steel](../metals/iron-steel.md), it restores ductility to work-hardened metals and prepares steel for further processing. In [Advanced Processes](../vlsi-scaling/advanced-processes.md), annealing repairs crystal lattice damage after ion implantation and activates dopants in semiconductor wafers.

## Technical Details

In metallurgy, annealing restores ductility to metals that have been work-hardened by hammering, drawing, or rolling. Copper is heated to 400-650°C (dull to cherry red), held 30-60 minutes, then cooled in air. Steel is heated to 700-900°C and cooled slowly (buried in ashes or lime). The process relieves internal stresses, recrystallizes the grain structure, and softens the metal for further shaping. Without annealing, work-hardened copper becomes brittle and cracks; work-hardened steel becomes unpredictable.

In glass production, annealing is equally critical. Unannealed glass retains internal thermal stress from uneven cooling and can shatter spontaneously. The Lehr furnace holds glass at 500-550°C (the annealing point for soda-lime glass), then cools at 1-5°C/min through the strain point (~450°C). Stress is verified by viewing the glass between crossed polarizers — colored fringes indicate residual stress; a uniform dark field indicates success.

In semiconductor manufacturing, annealing serves a dual purpose: repairing lattice damage from ion implantation and electrically activating dopants by moving them to substitutional crystal sites. Furnace annealing (900-1050°C, 30-60 min) is simple but causes excessive dopant diffusion. Rapid thermal annealing (1000-1100°C in seconds, hold 10-30 sec) minimizes redistribution of carefully controlled dopant profiles.

## Related Terms

- [Process](./process.md) — annealing as a fundamental thermal process across domains
- [Applications](./applications.md) — specific uses of annealed materials
- [Purity Verification](./purity-verification.md) — checking results of annealing in semiconductor contexts

## Appears In

- [Basic Glass Production](../glass/basic.md)
- [Advanced Glass](../glass/advanced.md)
- [Copper & Bronze](../metals/copper-bronze.md)
- [Iron & Steel](../metals/iron-steel.md)
- [Advanced Processes](../vlsi-scaling/advanced-processes.md)
