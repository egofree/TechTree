# Electrostatic Discharge (ESD)

Electrostatic discharge (ESD) is the sudden flow of electricity between two electrically charged objects, typically caused by contact, an electrical short, or dielectric breakdown. In semiconductor manufacturing, ESD is a critical hazard: a static discharge as low as 50–100V can puncture the thin gate oxide of a MOSFET, creating a short circuit from gate to channel. Even non-catastrophic ESD events degrade oxide integrity, leading to premature device failure weeks or months after the initial damage.

Prevention requires a comprehensive ESD control program: grounded wrist straps for personnel, conductive flooring, ionizers to neutralize surface charges on insulators, and ESD-safe packaging (conductive foam or bags) for storage and transport of sensitive components. All workstations handling bare dies or unpackaged ICs must maintain a grounded, static-dissipative environment.

ESD damage is particularly insidious because it often produces latent defects—devices that pass initial testing but fail in the field. This makes ESD control essential at every stage from wafer fabrication through packaging, testing, and system assembly. In a bootstrap semiconductor industry, where each device represents significant manual effort, even a single ESD event can destroy irreplaceable components.

## See Also

- [Die Attach](./die-attach.md)
- [Temperature Cycling](./temperature-cycling.md)
- [Burn-In](./burn-in.md)
- [Wire Bonding](./wire-bonding.md)

## Appears In

- [Packaging and Testing](../chemistry/packaging-testing.md)
- [Digital Logic](../computing/digital-logic.md)
- [Basic Semiconductor Devices](../silicon/basic-devices.md)
