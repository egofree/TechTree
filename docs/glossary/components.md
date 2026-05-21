# Components

> **Type**: noun | **Tier**: critical | **Domains**: ceramics, computing

Multiple mechanical integrators (ball-and-disk type) interconnected by shafts and gear trains. Each integrator solves one variable. Input shafts represent known quantities; output shafts represent computed quantities. Addition performed by differential gear (summing two shaft rotations). Multiplication by a constant via gear ratio.

## Context in the Tech Tree

Components are the individual parts that combine into functional systems. In [Mechanical Calculation](../computing/mechanical.md), components include stepped drums, digit wheels, carry mechanisms, and ball-and-disk integrators. In [Electronic Computing](../computing/electronic.md), components are transistors, resistors, capacitors, and logic gates. In [Kilns](../ceramics/kilns.md), components include fireboxes, flues, damper systems, and temperature measurement points. The term highlights the modular nature of industrial systems — every complex machine is assembled from simpler, independently manufactured parts.

## Technical Details

The mechanical integrator illustrates the component concept in analog computing. A ball-and-disk integrator consists of a steel ball sandwiched between a rotating disk and a cylindrical output roller. The ball's radial position on the disk (set by an input shaft) determines how fast the output roller rotates. Moving the ball outward increases the transmission ratio, effectively multiplying one variable (ball position) by another (disk rotation). Multiple integrators interconnected by shafts and gear trains solve differential equations.

Components are manufactured to specific tolerances that determine system performance. In mechanical calculators, gear accuracy of ±0.025 mm ensures correct carry propagation across 16-20 digit accumulators. In vacuum systems, flange flatness and surface finish determine seal integrity. In electronic systems, resistor and capacitor tolerances define circuit accuracy.

The component approach enables modular construction, repair, and upgrading. A failed bearing in a spinning wheel is replaced without rebuilding the entire wheel. A damaged gear in a calculator is re-machined without scrapping the mechanism. This modularity is essential for bootstrapped industry, where manufacturing capacity is limited and equipment must be maintained over long service lives.

## Related Terms

- [Scale](./scale.md) — how component design scales with system size
- [Operation](./operation.md) — how components interact during system operation
- [Capacity](./capacity.md) — how component specifications determine system capacity
- [Design](./design.md) — component-level design decisions

## Appears In

- [Mechanical Calculation](../computing/mechanical.md)
- [Electronic Computing](../computing/electronic.md)
- [Kilns](../ceramics/kilns.md)
