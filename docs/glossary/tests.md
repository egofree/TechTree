# Tests

> **Type**: noun | **Tier**: critical | **Domains**: ceramics, chemistry, machine-tools

DC parametric tests on test structures — process control monitors (PCMs) placed in scribe streets — measure threshold voltage (Vt), saturation current (Idsat), leakage current (Ileakage), and breakdown voltage to validate fabrication processes.

## Context in the Tech Tree

Tests are structured evaluation procedures that verify a component, material, or process meets its specifications. In [Packaging & Testing](../chemistry/packaging-testing.md), wafer probing performs DC parametric tests on PCM structures, functional tests on complete circuits, and speed/bin sorting that grades devices by maximum operating frequency. In [Pottery](../ceramics/pottery.md) and [Casting](../machine-tools/casting.md), tests verify structural integrity and dimensional accuracy of manufactured goods.

## Technical Details

Semiconductor testing follows a multi-stage protocol. Wafer-level testing uses probe cards with 50-500+ tungsten-rhenium needles (tip diameter 12-25 μm) that contact aluminum bond pads. Process control monitors — simple test structures placed in the scribe streets between die — provide parametric data: MOS threshold voltage, saturation current, leakage, and oxide breakdown voltage. These PCMs reveal process variations (implant dose, gate oxide thickness, lithography critical dimensions) before functional testing of complete circuits.

Speed/bin sorting tests devices at multiple clock frequencies, assigning each to a speed bin based on maximum verified operating speed. This allows manufacturers to sell the same die at multiple price points and ensures customers receive devices that meet their performance requirements.

Yield maps plot pass/fail results across the wafer surface, revealing spatial patterns in defects that guide process engineering improvements. Early fab yields of 10-50% mature to 80-95% through systematic defect reduction.

## Related Terms

- [Fuel](./fuel.md) — energy source for thermal testing
- [Sand](./sand.md) — raw material tested for purity
- [Construction](./construction.md) — test structures built into manufacturing
- [Advantages](./advantages.md) — benefits of statistical testing approaches
- [Pouring](./pouring.md) — casting operation validated by testing

## Appears In

- [Packaging & Testing](../chemistry/packaging-testing.md)
