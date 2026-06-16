# Magnetorquers

> **Node ID**: spacecraft-systems.adcs.magnetorquers
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.adcs`](./adcs.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: adcs_hardware
> **Critical**: No

Magnetorquers (magnetic torque rods) produce torque by interacting an on-board magnetic dipole with the Earth's geomagnetic field. They are propellant-free, continuously available, and highly reliable — but only effective in low Earth orbit and constrained to torque perpendicular to the local field vector. See [ADCS](./adcs.md) for the integrated control system context.

## Overview

A magnetorquer is an electromagnetic coil wound on a ferrite or air-core rod. Driving current through the coil produces a magnetic dipole moment **m** (measured in A·m²). The torque on the spacecraft is τ = **m** × **B**, where **B** is the local geomagnetic field. A typical LEO spacecraft carries three orthogonal rods to provide two-axis torque at any attitude.

Because the torque is always perpendicular to **B**, magnetorquers cannot produce torque about the field axis. This constraint means the control law must schedule rod currents based on the instantaneous field direction, measured by an on-board magnetometer. The achievable torque is periodic — over one orbit, every axis becomes accessible as the field rotates relative to the spacecraft.

Primary uses: momentum dumping (desaturating reaction wheels without propellant), detumble after separation (B-dot law), and B-dot stabilization during safe hold. Cubesat-class magnetorquers embedded in PCB coils produce 0.1–0.5 A·m²; dedicated rods on medium satellites produce 5–10 A·m².

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Dipole moment | 0.1–10 A·m² |
| Max torque (30 μT LEO field) | 0.003–0.3 mN·m |
| Operating altitude | <2,000 km (strong field) |
| Power consumption | 0.5–5 W per rod |
| Residual dipole (off-state) | <0.05 A·m² |

## Prerequisites

- Electromagnetic coil winding and ferrite core manufacturing
- Magnetometer for field vector measurement
- Field model (IGRF) for control law scheduling

## See Also

- [ADCS](./adcs.md) — parent capability and momentum management
- [Reaction Wheels](./adcs.reaction-wheels.md) — primary actuator being dumped
- [Sun & Earth Sensors](./adcs.sun-earth-sensors.md) — sensors for safe-hold mode

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
