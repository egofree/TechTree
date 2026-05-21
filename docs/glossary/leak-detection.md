# Leak Detection

> **Type**: equipment | **Tier**: critical | **Domains**: chemistry, gas-handling, photolithography

Methods and equipment for identifying and locating unintended fluid (gas or liquid) passages in sealed systems. In semiconductor and chemical processing, leak detection ranges from simple soap-bubble testing of plumbing joints to helium mass spectrometry detecting leaks as small as 10⁻¹² atm·cc/second. Container-closure integrity testing (CCIT) verifies that packaged products are hermetically sealed against contamination.

## Context in the Tech Tree

Leak detection becomes critical in the gas-handling and semiconductor processing domains. Hydrogen and silane gas systems require rigorous leak detection because both gases are pyrophoric — silane auto-ignites on contact with air. Semiconductor dopant gases (arsine, phosphine) are lethal at ppm concentrations, making zero-leak-tolerance mandatory. Vacuum systems for crystal growth and thin-film deposition require leak rates below 10⁻⁹ atm·cc/second to maintain process vacuum integrity.

The progression of leak detection capability tracks industrial maturity: soap-bubble testing for visible leaks, pressure decay testing for enclosed volumes, helium leak detection with mass spectrometers for semiconductor-grade systems, and residual gas analysis (RGA) for identifying the species of leaking gases.

## Technical Details

Helium leak detection is the gold standard for high-vacuum systems. Helium is used as a tracer gas because it is inert, non-toxic, has small atomic size (penetrates the smallest leaks), and is present at only ~5 ppm in air (low background). A mass spectrometer tuned to helium mass (4 amu) detects tracer gas spraying the exterior of a vacuum system, pinpointing leak locations. Sensitivity reaches 10⁻¹² atm·cc/second — equivalent to a hole that would take 30 years to leak one cubic centimeter of gas.

For chemical process safety, explosive-gas detectors (catalytic bead or infrared sensors) continuously monitor for flammable gas leaks. Toxic gas cabinets include continuous monitoring with automatic valve shutoff on detection. Regular leak-checking with soap solution or commercial leak detectors is standard practice for all threaded and flanged connections.

## Related Terms

- [Operation](./operation.md) — leak detection is part of operational safety procedures
- [Materials](./materials.md) — material selection affects seal integrity

## Appears In

- [Hydrogen & Silane](../chemistry/hydrogen-silane.md)
- [Packaging & Testing](../chemistry/packaging-testing.md)
- [Vacuum](../gas-handling/vacuum.md)
