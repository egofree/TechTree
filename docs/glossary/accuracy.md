# Accuracy

> **Type**: noun | **Tier**: critical | **Domains**: computing, measurement, optics, silicon

±2% for uniform samples. Doping concentration calculated from resistivity: N ≈ 1/(q·μ·ρ), where μ is carrier mobility. Maps wafer uniformity (49 or 121 point contour maps reveal doping variations across the ingot cross-section).

## Context in the Tech Tree

Accuracy is the degree to which a measurement conforms to the true value — a foundational requirement that threads through every stage of industrial bootstrapping. In [Precision Metrology](../measurement/precision-metrology.md), accuracy defines the quality of length standards, gauge blocks, and micrometers that make interchangeable parts possible. In [Silicon Purification](../silicon/purification.md), accuracy of resistivity mapping determines whether wafers meet semiconductor-grade specifications. In [Electromechanical Computing](../computing/electromechanical.md) and [Optical Inspection](../optics/inspection.md), accuracy governs the reliability of computed results and defect detection.

## Technical Details

Accuracy differs from precision: a measurement can be precise (repeatable) without being accurate (close to the true value), and vice versa. The calibration chain — from national standards to working gauges — exists to ensure accuracy propagates from reference artifacts to every instrument on the shop floor.

In semiconductor manufacturing, accuracy requirements are extreme. Wafer doping uniformity must be mapped to ±2% using four-point probe arrays, with contour maps revealing radial and axial variations across ingot cross-sections. The relationship between resistivity and dopant concentration (N ≈ 1/(q·μ·ρ)) provides the bridge between an electrical measurement and the physical property that matters for device behavior.

For mechanical metrology, gauge blocks (Jo-blocks) calibrated to ±0.05 μm serve as the primary length reference. Micrometers achieve ±0.002-0.005 mm accuracy when properly calibrated against these blocks. The iterative bootstrap of measurement accuracy — using the best available standards to make better instruments, which in turn make better standards — is a recurring pattern throughout the tech tree.

## Related Terms

- [Calibration](./calibration.md) — process of verifying and correcting instrument accuracy against known standards
- [Capacity](./capacity.md) — rated output often depends on measurement accuracy at specification boundaries
- [Principle](./principle.md) — underlying physical or mathematical basis for accurate measurement methods

## Appears In

- [Precision Metrology](../measurement/precision-metrology.md)
- [Silicon Purification](../silicon/purification.md)
- [Electromechanical Computing](../computing/electromechanical.md)
- [Optical Inspection](../optics/inspection.md)
- [Mechanical Calculation](../computing/mechanical.md)
