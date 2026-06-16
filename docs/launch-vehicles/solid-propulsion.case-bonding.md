# Case Bonding

> **Node ID**: launch-vehicles.solid-propulsion.case-bonding
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.solid-propulsion`](./solid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: motor_cases
> **Critical**: No

Case bonding is the fabrication of the solid motor pressure vessel and its integration with the cast propellant grain. In a case-bonded motor, the propellant is cast directly against an insulated case wall, forming a single bonded structure with no free volume. This process is part of the [Solid Propulsion](./solid-propulsion.md) capability.

## Case Materials

Two material families dominate:

- **Steel cases**: Maraging steel (18Ni, grade 250/300, yield 1,700-2,400 MPa) for large segmented motors (Shuttle SRB, SLS SRB). 6Al-4V titanium (yield 880-1,100 MPa, 45% lighter than steel) for smaller high-performance motors. Steel cases are machined, forged, and welded; segments are bolted together at field joints.
- **Composite cases**: filament-wound carbon fiber/epoxy (T700/T800 fiber, 3,500-5,000 MPa tensile) wound over a mandrel in helical and hoop patterns, oven-cured at 120-150°C. Specific strength 3-5× better than steel; 30-50% lighter. Used in modern commercial motors (Atlas V GEM, Vega P80). Aramid/epoxy (Kevlar) is used where impact resistance matters.

## Liner and Insulation

Before casting, the case inner wall is coated with:
- **Insulation**: EPDM or NBR rubber loaded with silica filler (1-10 mm thick), applied by tape-wrapping or spraying, cured at 60-80°C. Survives direct flame impingement for seconds to minutes at the head end and slot exits late in the burn.
- **Liner**: thin (0.2-0.5 mm) HTPB or CTPB layer with bonding agent (HX-752) applied over the insulation. Chemically bonds the cast propellant to the insulation during cure.

## Case-Bonded Architecture

The case serves directly as the propellant mold. After insulation and liner application, the mandrel is inserted, propellant is cast and cured, and the mandrel is removed. The result: propellant-liner-insulation-case as a single bonded monolith. Propellant mass fraction reaches 0.85-0.92. The case carries combustion pressure directly into its wall — no cartridge gap, no free volume.

Debonding (propellant separating from the liner) is the most feared failure mode; it caused the 1993 Titan IV SRM loss. Post-cast ultrasonic inspection detects any debond larger than a few centimeters.

See [Propellant Casting](./solid-propulsion.propellant-casting.md) for the grain step and [Solid Propulsion](./solid-propulsion.md) for the full capability.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
