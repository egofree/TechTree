# Grain Design

> **Node ID**: launch-vehicles.solid-propulsion.grain-design
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.solid-propulsion`](./solid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: grain_geometries
> **Critical**: No

Grain design is the engineering of the solid propellant's internal geometry — the shape of the cavity exposed to combustion — to tailor the thrust-time profile of a solid rocket motor. As the burning surface recedes normal to itself at the burn rate, the exposed area evolves, and thrust follows the surface-area evolution. This process is part of the [Solid Propulsion](./solid-propulsion.md) capability.

## Grain Geometries

Three primary cross-sections set the thrust profile:

- **Cylindrical (core-burning)**: a simple cylindrical port. As the port radius grows, wall area (2πrL) increases — producing **progressive** thrust (rising toward burnout).
- **Star (pointed)**: a star-shaped cross-section with many pointed fins. Fins burn back first (high initial surface area), then round off — producing **regressive** thrust (falling after an initial peak).
- **Finocyl (finned cylinder)**: a central cylinder with radial fin slots. The cylinder area increases progressively while fin areas decrease regressively; the two effects cancel for near-**neutral** thrust. The Shuttle SRB used a finocyl grain.

## Burn Rate Law

Burn rate follows **Saint Robert's law**:

**r = a · P^n**

where `r` is burn rate (mm/s), `P` is chamber pressure (MPa), `a` is a pre-exponential coefficient set by propellant formulation, and `n` is the **pressure exponent** — typically **0.2-0.5** for stable propellants. Values approaching 0.5 are acceptable only with precise pressure-relief design; n > 1 is unstable (catastrophic runaway).

Burn-rate modifiers tune `a`: iron oxide (Fe₂O₃) accelerates; lithium fluoride (LiF) retards. AP particle size (bimodal 6 μm + 200 μm blend) sets the baseline rate. A typical AP/Al/HTPB propellant at 7 MPa burns at 7-10 mm/s.

## Design Workflow

1. Define the mission thrust-time requirement (e.g., constant 12 MN for 120 s).
2. Select the propellant formulation (sets `a`, `n`, density, flame temperature).
3. Iterate the mandrel cross-section (star/finocyl/cylinder) in a burnback simulation until the predicted P_c(t) matches the requirement.
4. Verify peak pressure stays within 1.25-1.5× MEOP (case burst margin).
5. Machine the casting mandrel to the final geometry.

See [Propellant Casting](./solid-propulsion.propellant-casting.md) for the mandrel-to-grain step and [Solid Propulsion](./solid-propulsion.md) for the full capability.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
