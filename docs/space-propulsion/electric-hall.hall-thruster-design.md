# Hall Thruster Design

> **Node ID**: space-propulsion.electric-hall.hall-thruster-design
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-hall`](./electric-hall.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: hall_thrusters
> **Critical**: No

The Hall thruster design integrates the annular discharge channel, magnetic circuit, hollow cathode, and propellant feed into a compact gridless plasma accelerator. Unlike ion thrusters, there are no acceleration grids — the plasma itself establishes the acceleration field through crossed E×B fields. The defining component is the ceramic discharge channel, whose material properties, geometry, and erosion behavior set the thruster's performance and lifetime. See [Electric Propulsion — Hall](./electric-hall.md) for the integrated context.

## Process Description

1. **Channel geometry**: an annular ceramic channel (50–200 mm outer diameter, 5–25 mm channel width) defines the plasma acceleration region. SPT designs use deeper channels (15–40 mm); TAL designs use shallower channels (5–15 mm).
2. **Ceramic wall fabrication**: boron nitride (BN) or BN-SiO₂ composite (borosil) is hot-pressed and machined to the annular channel shape. SiC-coated variants extend lifetime.
3. **Anode integration**: the anode ring at the back of the channel doubles as the propellant injector — xenon enters through radial holes in the anode body.
4. **Magnetic circuit installation**: inner and outer magnetic pole pieces with SmCo or NdFeB permanent magnets or electromagnet coils are assembled around the channel.
5. **Cathode mounting**: an external hollow cathode is positioned 1–3 channel radii downstream of the exit plane, offset from the channel axis.
6. **Magnetic field mapping**: the assembled thruster is field-mapped to verify ±5% azimuthal B-field uniformity and correct peak location near the exit plane.

## Key Parameters

- **Channel diameter**: 50–200 mm (scales with power class)
- **Channel width**: 5–25 mm (annular gap between inner and outer walls)
- **Channel depth**: 15–40 mm (SPT deeper than TAL)
- **Wall material**: boron nitride (BN), borosil composite (BN-SiO₂)
- **Wall erosion rate**: 0.1–1.0 μm/hr (unshielded), 0.01 μm/hr (magnetically shielded)
- **Channel lifetime**: 7,000–10,000 hr (unshielded), 30,000+ hr (shielded)

## Prerequisites

- Ceramic hot-pressing and precision machining (BN, borosil)
- Magnetic circuit design and field mapping capability
- Hollow cathode technology (shared with ion thruster neutralizers)

## See Also

- [Electric Propulsion — Hall](./electric-hall.md) — parent capability
- [Magnetic Circuit Design](./electric-hall.magnetic-circuit-design.md) — B-field topology
- [Cathode Design](./electric-hall.cathode-design.md) — electron emission source

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
