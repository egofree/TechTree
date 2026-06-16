# Acceleration Grids

> **Node ID**: space-propulsion.electric-ion.acceleration-grids
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-ion`](./electric-ion.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: ion_thrusters
> **Critical**: No

The acceleration grid assembly — also called the ion optics — is the defining component of a gridded ion thruster. Two or three precisely aligned perforated plates extract ions from the discharge chamber and electrostatically accelerate them to exhaust velocities of 30,000–50,000 m/s. The grid gap (0.5–1.0 mm), aperture diameter (1–3 mm), and material selection directly set the thruster's thrust, Isp, and lifetime. See [Electric Propulsion — Ion](./electric-ion.md) for the integrated context.

## Process Description

1. **Grid material selection**: molybdenum sheet (0.3–1.0 mm thick) is the flight standard; carbon-carbon composite is used experimentally for lower sputter yield.
2. **Aperture drilling**: photochemical etching or laser drilling creates 1000–10,000 holes per grid (NSTAR has 15,000 apertures over 30 cm diameter).
3. **Grid forming**: the flat sheet is dished (spherical curvature) to maintain uniform gap under thermal expansion — dished grids are self-aligning.
4. **Standoff assembly**: insulating ceramic (alumina) standoffs set the grid gap to ±5 μm tolerance across the full diameter.
5. **Voltage biasing**: screen grid at +1000 to +2000 V, accelerator grid at −100 to −500 V, optional decelerator at ground.
6. **Perveance matching**: the beam current density is matched to the Child-Langmuir limit `j = (4/9)ε₀√(2q/m)V^(3/2)/d²` to prevent direct ion impingement.

## Key Parameters

- **Grid gap**: 0.5–1.0 mm (screen to accelerator)
- **Screen aperture**: 1–3 mm diameter (sets beam current density)
- **Accel aperture**: 0.5–2.0 mm (smaller than screen to block backstreaming electrons)
- **Beam voltage**: 300–2000 V (sets Isp)
- **Accelerator voltage**: −100 to −500 V (prevents electron backstreaming)
- **Grid material**: molybdenum (sputter yield 0.3 atoms/Xe-ion at 300 eV)
- **Lifetime**: 30,000–50,000 hr (erosion-limited)

## Prerequisites

- Refractory metal sheet manufacturing (molybdenum, carbon-carbon)
- Photochemical etching or laser drilling for aperture arrays
- Precision ceramic standoff machining (±5 μm tolerance)

## See Also

- [Electric Propulsion — Ion](./electric-ion.md) — parent capability
- [Ionization Chamber](./electric-ion.ionization-chamber.md) — upstream plasma source
- [Refractory Specialty Metals](../metals/refractory-specialty.md) — grid material source

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
