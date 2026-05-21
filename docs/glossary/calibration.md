# Calibration

> **Type**: noun | **Tier**: critical | **Domains**: computing, measurement

Illuminate the slit with a mercury lamp. Identify the prominent lines (404.7 nm violet, 435.8 nm blue, 546.1 nm green, 577/579 nm yellow doublet). Record the angular position of each line. Fit a calibration curve (wavelength vs. angle). Thereafter, any unknown line's wavelength follows from its angular position.

## Context in the Tech Tree

Calibration is the process of comparing an instrument's readings against known reference standards and adjusting for any deviation. In [Optical Instruments](../measurement/optical-instruments.md), spectroscopes are calibrated using mercury emission lines of known wavelength. In [Precision Metrology](../measurement/precision-metrology.md), micrometers and gauge blocks are calibrated against master standards. In [Electromechanical Computing](../computing/electromechanical.md) and [Temperature & Pressure](../measurement/temperature-pressure.md), instrument calibration ensures measurement reliability. Without calibration, systematic errors propagate through every downstream measurement and process.

## Technical Details

Spectroscope calibration illustrates the principle: a mercury vapor lamp emits light at precisely known wavelengths (404.7 nm, 435.8 nm, 546.1 nm, 577/579 nm). By illuminating the spectroscope slit with this lamp and recording the angular position of each emission line, a wavelength-vs-angle calibration curve is established. Once calibrated, any unknown spectral line's wavelength is determined from its angular position on the same curve.

For mechanical instruments, calibration follows a hierarchy. Master gauge blocks (calibrated against national standards or the best available length reference) set the baseline. Inspection-grade blocks calibrate working micrometers. Working micrometers verify production parts. Each step down the hierarchy trades some accuracy for accessibility and throughput. The chain must be verified periodically — thermal drift, wear, and contamination shift calibrations over time.

In semiconductor manufacturing, calibration extends to temperature sensors (thermocouples referenced against ice-point and steam-point junctions), mass flow controllers (calibrated against bubble flowmeters or primary standards), and electrical instruments (calibrated against Weston standard cells and standard resistors). The principle is universal: every measurement is only as good as its calibration chain.

## Related Terms

- [Accuracy](./accuracy.md) — the property that calibration verifies and maintains
- [Construction](./construction.md) — building calibration standards and reference artifacts
- [Materials](./materials.md) — reference materials used in calibration procedures
- [Principle](./principle.md) — the theoretical basis for calibration methods

## Appears In

- [Optical Instruments](../measurement/optical-instruments.md)
- [Precision Metrology](../measurement/precision-metrology.md)
- [Temperature & Pressure](../measurement/temperature-pressure.md)
- [Electromechanical Computing](../computing/electromechanical.md)
