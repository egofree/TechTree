# EVA Tools + Restraints

> **Node ID**: human-spaceflight.eva.eva-tools
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.eva`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: eva_tools, body_restraint_systems, eva_capability
> **Critical**: Yes

EVA tool design encompasses the hand tools, body restraint systems, and SAFER self-rescue jetpack that enable useful work in vacuum. The dominant tool is the Pistol Grip Tool (PGT) — a battery-powered torque wrench driving the universal 7/16" hex fastener used on all ISS external hardware. Without body restraint systems (foot restraints, tethers), tool reaction forces would spin the astronaut uselessly in weightlessness.

SAFER (Simplified Aid for EVA Rescue) provides 3.3 m/s of delta-v via 33 nitrogen gas thruster positions, enabling self-rescue if an astronaut becomes untethered. It has never been needed in an actual emergency but is tested once per astronaut.

## Key Parameters

| Parameter | PGT | SAFER |
|-----------|-----|-------|
| Torque range | 0.7-81 Nm | — |
| Speed | 5-30 rpm | — |
| Battery | 28 V Li-ion, 4.0 Ah | Suit-shared |
| Thrusters | — | 33 GN₂ positions |
| Delta-v | — | 3.3 m/s |
| Mass | 4.1 kg | 37 kg |
| Accuracy | ±5% torque | ATTITUDE HOLD |

## Tool Restraint Hierarchy

| Level | Type | Function |
|-------|------|----------|
| 1 | Safety tether (23.8 m steel cable) | Astronaut to station |
| 2 | Wrist tether (1.2 m webbing) | Tool to suit |
| 3 | Body restraint tether | Suit to worksite |
| 4 | Foot restraint platform | Boots locked in PFR socket |

**Golden rule**: No tool is ever let go. Every tool has a wrist tether attached before release.

## Prerequisites

- [EVA](./eva.md) — parent capability
- [Automation](../automation/index.md) — SAFER thruster control
- [Metals](../metals/index.md) — tool bodies and tether hardware
- [Space Stations](./space-stations.md) — PFR sockets and handrail interfaces

## See Also

- [Extravehicular Activity](./eva.md) — parent capability
- [EVA Procedures + Protocols](./eva.eva-procedures.md) — sibling process
- [Space Stations](./space-stations.md) — exterior restraint interfaces
