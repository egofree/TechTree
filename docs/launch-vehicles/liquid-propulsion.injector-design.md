# Injector Design

> **Node ID**: launch-vehicles.liquid-propulsion.injector-design
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.liquid-propulsion`](./liquid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: injectors
> **Critical**: No

The injector meters, mixes, and atomizes the propellants as they enter the chamber. It is the single most critical component for combustion stability — injector design determines whether the engine runs smoothly or destroys itself in 100 milliseconds. See [Liquid Propulsion](./liquid-propulsion.md) for the integrated engine context.

## Injector Types

- **Impinging jet**: Streams of fuel and oxidizer impinge at a point, shattering each other into droplets. Unlike-impinging (fuel-on-oxidizer) and doublet (paired) patterns are standard for LOX/RP-1. The F-1 used a 5700-orifice doublet pattern.
- **Shear-coaxial**: An annular oxidizer stream surrounds a central fuel jet; shear at the interface atomizes the propellants. Standard for LOX/LH2 (RS-25, Vulcain, LE-7).
- **Pintle**: A central pintle sprays propellant radially through slots while the other flows through an annular gap. Used by Merlin and Apollo LMDE. Simple, throttleable, but sensitive to mixture ratio distribution.

## Key Parameters

- **Orifice diameter**: 0.5-3 mm (tolerance ±2 μm)
- **Injection pressure drop**: 15-25% of chamber pressure (stability margin)
- **Pattern density**: 100-5000 orifices depending on engine size
- **Mixture ratio uniformity**: ±3% across the face (prevents local hot spots)
- **Atomization droplet size (SMD)**: 10-100 μm at injection

## Acoustic Stability

- **Baffles**: 3-8 radial vanes projecting 20-50 mm from the injector face, disrupting tangential acoustic modes
- **Acoustic cavities**: Quarter-wave Helmholtz resonators in the chamber wall, tuned to dominant instability frequency
- **Injector pattern**: Even orifice distribution prevents local mixture-ratio hot spots that seed pressure perturbations

## See Also

- [Liquid Propulsion](./liquid-propulsion.md) — parent capability
- [Combustion Chamber](./liquid-propulsion.combustion-chamber.md) — downstream of injector

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md)*
