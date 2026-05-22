# Cycle Time

> **Type**: noun | **Tier**: critical | **Domains**: energy, polymers, vlsi-scaling

10-60 seconds depending on part size and wall thickness. Cooling time dominates (typically 50-70% of cycle). Thicker walls require disproportionately longer cooling — a 4 mm wall takes ~4× longer to cool than a 2 mm wall (cooling time scales roughly with wall thickness squared, following Fourier's law of heat conduction).

## Context in the Tech Tree

Cycle time is the total time to complete one production cycle of a manufacturing process, and it directly determines throughput and unit cost. In injection molding, cycle time governs how many parts per hour a single mold can produce. In charcoal production and electric furnace operation, cycle time determines batch scheduling and energy efficiency. In semiconductor fabrication, cycle time for each lithography layer compounds across dozens of layers to set overall wafer throughput.

## Technical Details

In thermoplastic injection molding, the cycle breaks into four phases: injection (1-5 seconds), packing/holding (2-10 seconds), cooling (10-90 seconds, typically 50-70% of total), and mold open/ejection (2-5 seconds). Total cycle ranges from 15-120 seconds. The critical insight is that cooling time scales with the square of wall thickness (Fourier's law): doubling the wall thickness quadruples the cooling time. A 20-second cycle produces 180 parts/hour per cavity; a 60-second cycle produces only 60.

This quadratic relationship means that part design for manufacturability starts with minimizing wall thickness. Uniform wall thickness prevents sink marks and internal stresses. Designers must balance structural requirements against the exponential cycle time penalty of thicker sections.

In charcoal production, the carbonization cycle runs 3-7 days depending on kiln size and wood species. The cycle includes heating (drying and pyrolysis), active carbonization (maintaining reduction temperature), and cooling (sealing the kiln and waiting for the charge to drop below ignition temperature before unloading).

## Related Terms

- [Efficiency](./efficiency.md) — shorter cycle times improve throughput efficiency
- [Duration](./duration.md) — related time concept for process length

## Appears In

- [Electric Furnaces](../energy/electric-furnaces.md)
- [Charcoal Production](../energy/charcoal.md)
- [Thermoplastics](../polymers/thermoplastics.md)
- [Advanced Processes](../vlsi-scaling/advanced-processes.md)
