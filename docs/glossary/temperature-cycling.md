# Temperature Cycling

> **Type**: noun | **Tier**: critical | **Domains**: chemistry, optics, silicon

-65°C to +150°C, 500-1000 cycles — the standard temperature cycling test for semiconductor devices detects die attach voids, wire bond degradation, solder joint fatigue, and package cracking.

## Context in the Tech Tree

Temperature cycling is a reliability stress test that subjects components to repeated thermal extremes, accelerating failure mechanisms caused by differential thermal expansion. In [Packaging & Testing](../chemistry/packaging-testing.md), temperature cycling is one of several environmental stress screens (alongside HTOL, THB, and ESD testing) that identify latent defects before devices reach customers. In [Optical Inspection](../optics/inspection.md) and [Basic Devices](../silicon/basic-devices.md), thermal cycling validates that optical coatings, die attachments, and wire bonds survive the thermal stresses of real-world operation.

## Technical Details

The standard temperature cycling profile ramps between extreme temperatures (typically -65°C to +150°C for military/automotive grade) with dwell times of 10-15 minutes at each extreme to allow internal thermal equilibrium. Ramp rates of 10-15°C/minute simulate realistic thermal transients. Failure mechanisms include: CTE (coefficient of thermal expansion) mismatch between silicon die (2.6 ppm/°C) and lead frame (17 ppm/°C for copper) causes solder joint fatigue; gold-aluminum intermetallic growth at wire bonds accelerates at elevated temperatures; and epoxy encapsulant absorbs moisture that expands during heating, cracking the package.

Complementary tests include High Temperature Operating Life (HTOL: 125°C at nominal voltage, 1000 hours), Temperature-Humidity-Bias (THB: 85°C/85% RH with applied bias, 1000 hours), and Electrostatic Discharge (ESD) testing. Each test targets a different failure mode.

## Related Terms

- [Die Attach](./die-attach.md) — bond most susceptible to thermal cycling failure
- [Burn-in](./burn-in.md) — elevated temperature screening for infant mortality
- [Wire Bonding](./wire-bonding.md) — interconnect vulnerable to thermal fatigue
- [Electrostatic Discharge (ESD)](./electrostatic-discharge-esd.md) — companion reliability test
- [High Temperature Operating Life (HTOL)](./high-temperature-operating-life-htol.md) — thermal endurance test

## Appears In

- [Packaging & Testing](../chemistry/packaging-testing.md)
- [Optical Inspection](../optics/inspection.md)
- [Basic Devices](../silicon/basic-devices.md)
