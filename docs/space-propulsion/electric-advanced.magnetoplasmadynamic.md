# Magnetoplasmadynamic

> **Node ID**: space-propulsion.electric-advanced.magnetoplasmadynamic
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-advanced`](./electric-advanced.md)
> **Enables**: None
> **Timeline**: Years 50-200+
> **Outputs**: advanced_thrusters
> **Critical**: No

Magnetoplasmadynamic (MPD) thrusters use the Lorentz force (J × B) to accelerate plasma directly, without grids or nozzles. A high-current DC arc (1–25 kA) flows radially between a central cathode and a surrounding ring anode; the current generates a self-induced azimuthal magnetic field (Bθ); the interaction produces an axial Lorentz force that accelerates the plasma. At megawatt power levels, MPD thrusters can deliver 10–50 N of thrust at 2000–5000 s Isp — performance unattainable by any other electric propulsion technology. See [Electric Propulsion — Advanced](./electric-advanced.md) for the integrated context.

## Process Description

1. **Cathode fabrication**: a thoriated tungsten rod (3–10 mm diameter) is machined to a tapered tip; multi-channel hollow cathode designs improve current distribution at high currents.
2. **Anode ring manufacturing**: a copper or tungsten ring anode (20–50 mm inner diameter) is machined with internal cooling channels for thermal management.
3. **Insulator assembly**: boron nitride or alumina insulators separate the cathode and anode, withstanding the multi-kV potential during pulsed operation.
4. **Propellant injection**: lithium (vaporized from a reservoir), argon, or hydrogen is injected radially through the anode or axially through a hollow cathode.
5. **Arc initiation**: a high-voltage pulse breaks down the gas; the discharge transitions to a high-current DC or pulsed arc (1–25 kA).
6. **Self-field acceleration**: the arc current induces Bθ; the radial current density (Jr) interacting with Bθ produces axial thrust (Jr × Bθ) on the plasma.

## Key Parameters

- **Propellant**: lithium (Li), argon (Ar), hydrogen (H₂), ammonia (NH₃)
- **Arc current**: 1–25 kA (self-field); 0.1–1 kA (applied-field with external coils)
- **Arc voltage**: 50–150 V (self-field at high current)
- **Power**: 100 kW–6 MW (self-field); 1–100 kW (applied-field)
- **Thrust**: 1–50 N (self-field at MW power)
- **Isp**: 2000–5000 s (lithium), 1000–2500 s (argon)
- **Efficiency**: 20–35% (self-field at 1 MW), 35–50% projected at 10 MW
- **Electrode erosion**: 1–10 μg/Coulomb (cathode spot mode — primary lifetime limiter)

## Prerequisites

- High-current DC power supply (kA class) or pulsed capacitor bank
- Thoriated tungsten cathode manufacturing (shared with arcjet)
- MW-class space nuclear power (enabling requirement)

## See Also

- [Electric Propulsion — Advanced](./electric-advanced.md) — parent capability
- [VASIMR Design](./electric-advanced.vasimr-design.md) — electrodeless alternative (no erosion limit)
- [Arcjet Design](./electric-advanced.arcjet-design.md) — lower-power electrothermal alternative

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
