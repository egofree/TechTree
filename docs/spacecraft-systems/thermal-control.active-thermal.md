# Active Thermal Control

> **Node ID**: spacecraft-systems.thermal-control.active-thermal
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `spacecraft-systems.thermal-control`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 40-200+
> **Outputs**: thermal_hardware
> **Critical**: Yes

Active thermal control uses powered actuators — heaters, louvers, fluid loops, and loop heat pipes — to maintain spacecraft temperatures when passive elements alone cannot meet requirements. Active elements are introduced when equipment dissipation varies widely, when survival temperatures must be maintained during eclipse, or when heat must be transported over distances that exceed the capability of constant-conductance heat pipes.

Heater zones (20-100 per spacecraft) maintain minimum temperatures on batteries, propellant lines, and cold-soaked electronics. Louvers modulate radiator emissivity between 0.15 (closed) and 0.85 (open) with a passive bimetallic actuator. Loop heat pipes (LHPs) transport 100-1000 W over distances up to 15 m using capillary action — no pump required. Pumped fluid loops handle the highest heat loads (500-5000 W) on large communications satellites and crewed vehicles.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Heater zones | 20-100 | Per spacecraft |
| Battery heater setpoint | +5°C | ±3°C deadband |
| Louver modulation ratio | 5:1 to 6:1 | ε_eff 0.15 to 0.85 |
| LHP heat transport | 100-1000 W | Up to 15 m distance |
| Fluid loop capacity | 500-5000 W | Pumped ammonia loop |
| Pump power | 5-50 W | Centrifugal DC |

## Active System Sizing Steps

1. Identify components with temperature ranges that passive design cannot meet
2. Map minimum-temperature cases (eclipse, low-dissipation modes) for heater sizing
3. Select heater setpoints and deadbands; add hardwired survive-safe thermostats
4. Identify radiator surfaces where louvers can modulate rejection (variable dissipation)
5. For loads >100 W over >1 m: size loop heat pipe (ammonia, capillary-driven)
6. For loads >500 W or multiple remote heat sources: size pumped fluid loop
7. Integrate active elements into TMM; verify control stability (no hunting)
8. Qualify in thermal-vacuum cycle test (20-200 hot/cold cycles)

## Prerequisites

- [Aluminium](../metals/index.md) — LHP evaporators, cold plates, fluid lines
- [Polymers](../polymers/index.md) — heater insulation, wiring harness materials
- [Vacuum](../vacuum/index.md) — thermal-vacuum qualification chamber

## See Also

- [Thermal Control](./thermal-control.md) — parent capability
- [Passive Thermal Control](./thermal-control.passive-thermal.md) — sibling process
- [Radiator Design](./thermal-control.radiator-design.md) — sibling process
