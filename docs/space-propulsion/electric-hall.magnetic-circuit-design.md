# Magnetic Circuit Design

> **Node ID**: space-propulsion.electric-hall.magnetic-circuit-design
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-hall`](./electric-hall.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: hall_thrusters
> **Critical**: No

The magnetic circuit shapes the radial magnetic field that traps electrons in the Hall current drift and defines the plasma acceleration zone. It is the most critical design element of a Hall thruster — the field topology directly determines ionization efficiency, beam divergence, wall erosion rate, and discharge stability. Modern designs use **magnetic shielding** — field lines parallel to the wall surface — to reduce wall ion flux by 10–100× and extend lifetime 5–10×. See [Electric Propulsion — Hall](./electric-hall.md) for the integrated context.

## Process Description

1. **Pole piece design**: low-carbon steel inner and outer pole pieces are machined to concentrate magnetic flux at the channel exit plane, creating a radial B-field across the annular gap.
2. **Magnet selection**: samarium-cobalt (SmCo) or neodymium (NdFeB) permanent magnets provide the bias field; electromagnet coils (0.5–5 A) provide adjustable control.
3. **Coil winding**: inner and outer solenoid coils are wound with magnet wire on bobbins, potted for thermal conductivity and electrical isolation.
4. **Assembly and alignment**: pole pieces, magnets, and coils are assembled with the discharge channel, ensuring ±5% azimuthal field uniformity.
5. **Field mapping**: a 3-axis Hall probe scans the channel volume on a precision stage, mapping B-field magnitude and direction.
6. **Magnetic shielding optimization**: advanced designs reshape the pole pieces so field lines run parallel to the ceramic walls in the acceleration zone, redirecting ion flux away from the walls.

## Key Parameters

- **Radial B-field**: 100–250 Gauss at channel centerline (peak near exit)
- **Field topology**: lens-shaped (converging upstream, peaking near exit, diverging downstream)
- **Azimuthal uniformity**: ±5% (prevents plasma asymmetries and discharge oscillations)
- **Magnet type**: SmCo (radiation-hard) or NdFeB (higher energy product)
- **Coil power**: 5–30 W total for inner + outer electromagnets
- **Shielding topology**: field lines parallel to wall surface in acceleration zone

## Prerequisites

- Soft magnetic material (low-carbon steel) machining
- Permanent magnet manufacturing (SmCo, NdFeB)
- Precision Hall probe field-mapping instrumentation

## See Also

- [Electric Propulsion — Hall](./electric-hall.md) — parent capability
- [Hall Thruster Design](./electric-hall.hall-thruster-design.md) — channel integration
- [Cathode Design](./electric-hall.cathode-design.md) — coupling to beam plasma

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
