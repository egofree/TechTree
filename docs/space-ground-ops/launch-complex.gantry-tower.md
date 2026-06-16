# Gantry & Service Tower

> **Node ID**: space-ground-ops.launch-complex.gantry-tower
> **Domain**: [Space Ground Operations](./index.md)
> **Dependencies**: [`space-ground-ops.launch-complex`](./launch-complex.md)
> **Enables**: None
> **Timeline**: Years 50+
> **Outputs**: launch_pads
> **Critical**: No

The gantry and service tower provide physical access to the launch vehicle for fuelling connections, crew ingress, ordnance arming, and payload servicing. The LC-39A Fixed Service Structure (FSS) is a 106m-tall open-truss steel tower carrying eight umbilical arms — each weighing 9-22 tonnes and retracting in 2-8 seconds at T-0 via redundant hydraulic cylinders. The Shuttle-era Rotating Service Structure (RSS) pivoted 120° to envelope the orbiter payload bay with a Class 100K cleanroom (payload changeout room), enabling late stowage of satellites. Modern pads (Falcon 9, Starship) integrate the umbilical function into the TEL strongback, eliminating the RSS but retaining the FSS-level crew access arm for crewed missions.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| FSS height (LC-39A) | 106 m |
| FSS mass | 4,700 t structural steel |
| Umbilical arms | 8 (Shuttle config); 6 (SLS); ~12 (Starship) |
| Arm retraction time at T-0 | 2-8 seconds |
| Maximum vehicle sway tolerance | 0.6 m |
| RSS mass (Shuttle-era) | 4,190 t (demolished at LC-39A in 2018) |
| Payload changeout room class | Class 100K (ISO 9) |
| Crew access arm retraction | T-5 min (Shuttle); T-7 min (Dragon) |

## Process Overview

1. **Foundation**: Anchor FSS base to pad deck via 1.2m-diameter pier caps on piles
2. **Tower erection**: Stack 106m open-truss steel frame; align to ±25 mm plumb
3. **Arm installation**: Mount swing arms on rotational bearings; install hydraulic cylinders
4. **Umbilical integration**: Route propellant, pneumatic, power, and data lines through each arm
5. **Checkout**: Cycle each arm 100+ times under load; verify clearance at maximum sway

## Prerequisites

- Launch Complex capability (parent)
- Structural steel construction and crane operation expertise
- Hydraulic actuation systems for swing-arm retract

## See Also

- [Launch Complex](./launch-complex.md) — parent capability
- [Pad Structure & Flame Trench](./launch-complex.pad-structure.md) — pad foundation
- [Propellant Storage Facilities](./launch-complex.propellant-facilities.md) — umbilical fluid source

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Ground Operations](./index.md)*
