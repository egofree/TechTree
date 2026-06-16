# Ionization Chamber

> **Node ID**: space-propulsion.electric-ion.ionization-chamber
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-ion`](./electric-ion.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: ion_thrusters
> **Critical**: No

The ionization chamber is the plasma generation stage of a gridded ion thruster. Xenon propellant enters at 2–20 mg/s and is ionized to a plasma density of 10¹⁷–10¹⁸ m⁻³ by one of three methods: DC electron bombardment (NSTAR, NEXT), RF inductive coupling (RIT series), or microwave electron cyclotron resonance (µ10). See [Electric Propulsion — Ion](./electric-ion.md) for the integrated thruster context.

## Process Description

1. **Propellant injection**: xenon gas enters through a porous metal distributor plate or an array of injection orifices, ensuring azimuthally uniform flow into the discharge volume.
2. **Primary electron injection**: a BaO hollow cathode at the chamber center or rear injects 25–40 V electrons at 5–20 A.
3. **Magnetic confinement**: a multi-cusp SmCo magnet array creates 100–500 G fields at the chamber wall, reflecting electrons back inward and increasing their path length.
4. **Ionizing collisions**: primary electrons collide with neutral xenon atoms (ionization potential 12.1 eV), creating Xe⁺ ions and secondary electrons.
5. **Plasma diffusion**: ions diffuse to the screen grid at the exit plane, where they are extracted into the acceleration stage.
6. **Doubly-charged formation**: 5–15% of ions become Xe²⁺ (requires 22 eV), which erodes grids faster per ion due to 2× charge.

## Key Parameters

- **Discharge voltage**: 25–40 V DC (optimized for xenon cross-section)
- **Discharge current**: 5–20 A (scales with thruster power)
- **Discharge loss**: 100–300 W per amp of beam current
- **Propellant utilization**: 85–90% (fraction of Xe atoms ionized)
- **Plasma density**: 10¹⁷–10¹⁸ m⁻³ at the screen grid plane
- **Double-ion fraction**: 5–15% (Xe²⁺/Xe⁺ ratio)

## Prerequisites

- Hollow cathode technology (BaO emitter, tungsten orifice)
- Samarium-cobalt permanent magnets for multi-cusp confinement
- Precision-machined discharge chamber (stainless steel or titanium)

## See Also

- [Electric Propulsion — Ion](./electric-ion.md) — parent capability
- [Acceleration Grids](./electric-ion.acceleration-grids.md) — downstream consumer
- [Neutralizer Design](./electric-ion.neutralizer-design.md) — electron emission

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
