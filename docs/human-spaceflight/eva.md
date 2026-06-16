# Extravehicular Activity (EVA)

> **Node ID**: human-spaceflight.eva
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.space-suits`, `human-spaceflight.eclss`, `automation`, `human-spaceflight.space-stations`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: eva_capability, eva_procedures, eva_tools, body_restraint_systems
> **Critical**: Yes

Extravehicular activity (EVA) — commonly called a spacewalk — is the set of procedures, tools, and physical techniques that allow an astronaut to leave the pressurised spacecraft and work in the vacuum, thermal, and radiation environment of open space. An EVA combines the [spacesuit](./space-suits.md) (pressure garment and portable life support), the [ECLSS](./eclss.md) airlock and prebreath infrastructure, [automation](../automation/index.md) for SAFER jetpack control, and the [space station](./space-stations.md) exterior interfaces (handrails, foot restraint sockets, tool stowage) into a single integrated operation that no other domain in the tech tree replicates.

This article covers the integrated discipline of EVA across two process areas: [EVA procedures and protocols](./eva.eva-procedures.md) (prebreath, campout, timeline construction, airlock ops) and [EVA tools and restraints](./eva.eva-tools.md) (pistol-grip tools, body restraint tethers, foot restraint platforms, SAFER jetpack). Together they define what it takes to perform useful work outside the spacecraft — the most physically and procedurally demanding task in human spaceflight.

## Overview

A nominal EVA lasts 6-8 hours, bounded by the consumables in the suit's Primary Life Support System (PLSS): oxygen supply, CO₂ scrubbing capacity, and battery power. The astronaut exits the airlock, traverses to the work site using handrails or a robotic arm ride, performs the planned task — maintenance, assembly, science deployment, or inspection — and returns before consumables are exhausted. Every minute of that timeline is pre-planned, rehearsed in the Neutral Buoyancy Laboratory (NBL) pool, and executed against a written checklist worn on the astronaut's cuff.

The [space suit](./space-suits.md) is the fundamental prerequisite: it provides 29.6 kPa (4.3 psi) of pure oxygen pressure, thermal regulation via the liquid cooling and ventilation garment, micrometeoroid protection, and a 6.5-8.5 hour supply of oxygen, water, and battery power. The [ECLSS](./eclss.md) airlock provides the depressurisation and prebreath protocol that prevents decompression sickness (the bends) when the astronaut transitions from the 101 kPa cabin to the 29.6 kPa suit. [Automation](../automation/index.md) provides the cold-gas thruster controllers for the SAFER (Simplified Aid for EVA Rescue) emergency jetpack. The [space station](./space-stations.md) exterior provides the handrails, foot restraint sockets, and tool stowage that make controlled work possible in weightlessness.

## Decompression Sickness and Prebreath

The fundamental physiological challenge of EVA is decompression sickness (DCS). The station cabin is maintained at 101 kPa with 21% oxygen (an oxygen partial pressure of 21.2 kPa). The suit is pressurised to only 29.6 kPa with 100% oxygen (an oxygen partial pressure of 29.6 kPa). This pressure difference means nitrogen dissolved in the astronaut's tissues at cabin pressure would come out of solution as bubbles in the suit — causing joint pain, neurological symptoms, or potentially fatal embolisms.

To prevent DCS, the astronaut must reduce dissolved tissue nitrogen before the EVA by breathing pure oxygen, which washes nitrogen out of the blood and tissues. Two protocols are in use:

### Campout Protocol

The campout protocol reduces nitrogen over a longer, gentler period by having the astronaut sleep overnight at reduced pressure in the airlock:

| Phase | Duration | Environment | ppO₂ |
|-------|----------|-------------|------|
| Pre-campout (T-18 hr) | 1 hr | Don mask; breathe 100% O₂ | — |
| Campout (T-15 hr) | ~8 hr (overnight) | Airlock at 70.3 kPa, 26.5% O₂ | 18.6 kPa |
| Morning mask (T-7 hr) | 50 min | Mask; 100% O₂ + exercise | — |
| Suit purge (T-1 hr) | 40 min | Suit purge to 100% O₂ | 29.6 kPa |
| In-suit prebreath (T-0.5 hr) | 30 min | 100% O₂ in suit, resting | 29.6 kPa |
| Airlock depress | 15 min | Reduce to vacuum | — |
| **EVA begins** | 6-8 hr | Suit at 29.6 kPa | 29.6 kPa |

### Exercise Prebreath Protocol

The exercise prebreath protocol is a faster alternative that accelerates nitrogen washout by combining exercise with pure oxygen breathing. Exercise increases blood flow and respiration rate, speeding nitrogen elimination:

| Phase | Duration | Activity |
|-------|----------|----------|
| Mask donning (T-2.5 hr) | 5 min | Don mask; verify O₂ flow |
| Resting prebreath | 50 min | Rest; breathe 100% O₂ |
| Exercise phase | 10 min | Cycle ergometer at 75% VO₂max |
| Resting prebreath | 50 min | Rest; breathe 100% O₂ |
| Suit don | 30 min | Don suit; purge to 100% O₂ |
| In-suit prebreath | 50 min | Rest in suit on 100% O₂ |
| Airlock depress | 15 min | Reduce to vacuum |
| **EVA begins** | 6-8 hr | Suit at 29.6 kPa |

The exercise protocol's 30-minute exercise window (actually 10 minutes active within a 50-minute cycle) roughly halves the total prebreath time compared to earlier protocols while maintaining a DCS incidence rate of zero across hundreds of EVAs.

## EVA Timeline

A nominal EVA follows a tightly choreographed timeline broken into 30-minute increments. The table below shows a representative 6.5-hour assembly EVA:

| Time (GET) | Phase | Duration | Key actions |
|-----------|-------|----------|-------------|
| 0:00 | Airlock egress | 0:30 | Suit checks; depress; hatch open; translation to worksite |
| 0:30 | Setup | 0:30 | Install foot restraint; deploy tool board; verify tethering |
| 1:00 | Task block 1 | 1:30 | Remove thermal blanket; disconnect fluid lines; unbolt ORU |
| 2:30 | ORU swap | 1:00 | Remove old ORU; install new ORU; torque bolts to spec |
| 3:30 | Task block 2 | 1:30 | Reconnect fluid lines; verify seal; reinstall thermal blanket |
| 5:00 | Cleanup | 0:30 | Stow tools; retrieve foot restraint; route tethers |
| 5:30 | Translation | 0:20 | Traverse to airlock; pause for tool inventory |
| 5:50 | Airlock ingress | 0:20 | Enter airlock; hatch close; repress |
| 6:10 | Post-EVA | 0:20 | Suit doff; medical check; debrief |
| **6:30** | **Complete** | | |

Each task block includes a 5-minute buffer for contingencies. If a task runs over budget, lower-priority "get-ahead" tasks at the end of the timeline are deferred to a future EVA.

## Pistol Grip Tool (PGT)

The Pistol Grip Tool is the workhorse power tool of EVA. Designed for gloved hand operation in vacuum, it drives bolts, removes fasteners, and reconfigures mechanisms that would be impossible to operate by hand in a pressurised suit.

### PGT Specifications

| Parameter | Value |
|-----------|-------|
| Torque range | 0.7-81 Nm (5-720 in-lb) |
| Speed range | 5-30 rpm |
| Torque accuracy | ±5% of setpoint |
| Power source | 28 V DC rechargeable Li-ion battery |
| Battery capacity | 4.0 Ah (8-10 hr operation) |
| Mass | 4.1 kg |
| Drive socket | 7/16" hex (standard EVA fastener) |
| Display | LCD with backlight (visible through helmet visor) |
| Controls | Trigger, torque dial, direction switch, speed dial |
| Data logging | Torque, angle, count, timestamp per fastener |

The PGT's 7/16" hex drive socket is the universal interface for EVA fasteners — virtually every external bolt and screw on the ISS uses a 7/16" hex head specifically so the PGT can drive it. The tool's torque accuracy of ±5% is critical for structural joints where over-torqueing could strip threads or shear a fastener, and under-torqueing could leave a joint loose under launch or thermal loads.

### PGT Operating Procedure

1. Verify battery charge and socket installation
2. Set torque dial to specified value (per procedure)
3. Set speed (low for high-torque joints, high for quick removal)
4. Engage socket on fastener head; verify full seating
5. Pull trigger; tool auto-stops at preset torque
6. Read torque and angle from display; log to cuff checklist
7. Reverse direction to remove fastener (set direction switch to "REV")

## Body Restraint Systems

Working in weightlessness is fundamentally different from working on Earth: there is no gravity to hold the astronaut in place, and every force applied to a tool produces an equal and opposite reaction on the astronaut. Without restraint, driving a bolt would simply spin the astronaut around the fastener. Body restraint systems anchor the astronaut to the structure, transferring tool reaction forces through the body to the station.

### Foot Restraint Platforms

A foot restraint is a platform that clips into a socket on the station exterior (or onto the end of the robotic arm), holding the astronaut's boots in spring-loaded clips. Once locked in, the astronaut has both hands free and a stable base against which to apply force.

| Parameter | Value |
|-----------|-------|
| Socket interface | PFR (Portable Foot Restraint) standard socket |
| Boot retention | Spring-loaded toe clips; 200 N hold-off |
| Pitch/yaw adjustment | ±15° detent positions |
| Robotic arm interface | Yes (rides on LEE or PDGF adapter) |
| Mass | 11 kg |

When the foot restraint is mounted on the end of [Canadarm2](./space-stations.md), the arm operator inside the station can reposition the astronaut across the work site without any EVA time spent translating — dramatically increasing productive work time.

### Body Restraint Tethers

For shorter tasks, a body restraint tether (BRT) provides a quick-connect anchor point. The BRT is a telescoping rod with a hook at each end: one hooks to a station handrail, the other to a D-ring on the astronaut's suit. The rod can be adjusted from 0.6 m to 1.5 m and locked at any length, providing a rigid anchor that prevents drift.

## Tether Protocols

Every tool and every astronaut is tethered to the station at all times during EVA. A lost tool becomes orbital debris; a drifting astronaut without SAFER becomes a rescue situation. The tethering system uses a hierarchy of connections:

### Tether Hierarchy

| Level | Type | Function |
|-------|------|----------|
| 1 | Safety tether (23.8 m steel cable) | Primary — astronaut to station |
| 2 | Wrist tether (1.2 m webbing) | Per-tool — tool to suit |
| 3 | Body restraint tether | Worksite — suit to structure |
| 4 | Translation tether (guide wire) | Route — handrail-to-handrail path |

The primary safety tether is a 23.8 m stainless steel cable on a spring-loaded reel attached to the astronaut's waist D-ring. As the astronaut translates along handrails, the tether slides along a guide wire that parallels the translation path — always maintaining a connection between astronaut and station.

### Golden Rule

**No tool is ever let go.** Every tool has a wrist tether. When a tool is set down, it is tethered to a tool board or stowed in a bag before the tether is released. The [spacewalk](https://www.nasa.gov/eva) training programme drills this rule until it is reflexive — the muscle memory of tethering comes before the action of releasing.

## SAFER (Simplified Aid for EVA Rescue)

SAFER is a self-rescue jetpack worn on the back of the suit, designed for the scenario where an astronaut becomes untethered and drifts away from the station. Without SAFER, a drifting astronaut has no way to return — the suit has no propulsion of its own.

### SAFER Specifications

| Parameter | Value |
|-----------|-------|
| Thrusters | 24 nitrogen gas (×2 sets = 48, 33 unique valve positions) |
| Propellant | Gaseous nitrogen (GN₂) |
| Delta-v | 3.3 m/s (10.8 ft/s) |
| Propellant tank pressure | 20.7 MPa (3,000 psi) |
| Propellant mass | 1.4 kg GN₂ |
| Mass (with propellant) | 37 kg |
| Control | Hand controller (4-axis: pitch, yaw, roll, translation) |
| Power | Suit battery (shared) |
| Operation mode | Automatic ( ATTITUDE HOLD) or manual |

SAFER uses 33 nitrogen thruster valve positions arranged for 6-degree-of-freedom control. The astronaut steers with a hand controller mounted on the suit chest, selecting attitude hold mode to stop rotation, then translating back toward the station. The 3.3 m/s of delta-v is sufficient to rescue an astronaut drifting at up to 3 m/s relative velocity — well beyond the typical separation rate from a missed handhold (0.1-0.5 m/s).

### SAFER Flight Profile

SAFER has never been needed in an actual emergency. It is tested once per astronaut during a dedicated check-out EVA early in their station increment:

1. Astronaut positions at a fixed point on the station, still tethered
2. Tether is briefly released (safety tether remains attached)
3. Astronaut commands a 0.2 m/s translation away from station using hand controller
4. Engages ATTITUDE HOLD; verifies attitude stabilisation
5. Commands return translation to station; re-attaches tether
6. Full system check takes approximately 15 minutes

## Worksite Setup

Before any task begins, the worksite must be prepared: foot restraint installed, tool board deployed, lighting verified, and contingency items staged. A typical worksite setup takes 20-30 minutes and follows a standard sequence:

1. **Inspect**: Survey the worksite; verify no damage, no FOD (foreign object debris)
2. **Anchor**: Install foot restraint in nearest PFR socket; lock in position
3. **Stage**: Deploy tool board with PGT, torque multiplier, sockets, and consumables
4. **Light**: If in orbital night, deploy portable floodlight; verify battery
5. **Tether**: Attach body restraint tether from suit to nearest hardpoint
6. **Verify**: Double-check all tether connections before releasing any fastener

## Neutral Buoyancy Training

Every EVA is rehearsed for 6-10 hours in the Neutral Buoyancy Laboratory (NBL) — a 23.7 million litre pool at Johnson Space Center containing a 1:1 scale mockup of the ISS. Astronauts in pressurised suits practice the exact task sequence underwater, where buoyancy cancels gravity and the suit's internal pressure creates the same limited mobility as in orbit.

The NBL cannot perfectly simulate weightlessness — water drag damps motion that would be free in vacuum, and the suits are neutrally buoyant but still have full inertia. But it is the highest-fidelity EVA training environment available and produces the muscle memory and task familiarity that make the real EVA execute on timeline.

### NBL Specifications

| Parameter | Value |
|-----------|-------|
| Pool volume | 23.7 million litres |
| Pool dimensions | 62 m × 31 m × 12 m |
| Mockups | ISS USOS, Orion, commercial vehicles |
| Suit type | Modified EMU (neutrally ballasted) |
| Divers per suit | 4 (safety, camera, comms, utility) |
| Training ratio | 6-10 hr in pool per 1 hr of EVA |

## Suit Pressure and Mobility

The Extravehicular Mobility Unit (EMU) — the US EVA suit — operates at 29.6 kPa (4.3 psi) of pure oxygen. This low pressure is a compromise: a higher suit pressure would reduce prebreath time but make the suit joints harder to bend, because the internal pressure acts as a pneumatic spring resisting any flexion. At 29.6 kPa, the suit joints use a system of pressure bearings and convoluted bellows to permit movement, but every motion still requires continuous muscular effort.

| Joint | Flexion range (suited) | Effort vs. unsuited |
|-------|----------------------|---------------------|
| Shoulder | 0-150° (elevation) | 2-3× |
| Elbow | 20-130° | 1.5-2× |
| Wrist | ±90° (pitch), ±70° (yaw) | 1.5× |
| Hip | 0-90° (flexion) | 2× |
| Knee | 0-120° | 1.5-2× |
| Glove fingers | Full grip (with effort) | 3-4× |

The glove is the limiting element of EVA productivity. Gripping a tool for hours against suit pressure causes hand fatigue, fingertip bruising, and occasionally onycholysis (nail detachment). Glove design is the single most active area of EVA hardware improvement.

## Airlock Operations

The airlock is the gateway between the pressurised cabin and the vacuum of space. On the ISS, the Quest Joint Airlock provides the EVA preparation and egress capability for the USOS:

### Quest Airlock Specifications

| Parameter | Value |
|-----------|-------|
| Volume | 34 m³ (crew lock) + 3.6 m³ (equipment lock) |
| Hatch diameter | 1.27 m (CBM compatible) |
| Maximum depress rate | 0.69 kPa/s |
| Re-pressurisation time | 5 min (emergency), 15 min (normal) |
| Suit prebreath station | 2 (campout configuration) |
| Umbilical connections | 4 (O₂, power, comms, cooling) |

The airlock equipment lock serves as the suit donning, doffing, and maintenance area. Suit don takes approximately 45 minutes with a helper (suit technician). The crew lock is the depressurisation chamber; it can be pumped down to vacuum in approximately 15 minutes once the hatch to the cabin is closed.

## Troubleshooting

| Symptom | Likely cause | Diagnostic | Fix |
|---------|-------------|-----------|-----|
| Suit pressure drop | Glove or seal leak | Isolate via suit shutoff valves; listen for hiss | Tighten glove wrist ring; bypass via secondary O₂ |
| CO₂ partial pressure rising | Contaminant cartridge saturated | Check PLSS CO₂ gauge; trend rate | Terminate EVA; return to airlock early |
| PGT stops driving | Battery depleted or socket jam | Check battery indicator; inspect socket | Swap battery from tool board; clear socket |
| Astronaut stuck (foot jam) | Boot clip binding in cold | Check clip engagement; wiggle boot | Buddy assist; use PGT to pry clip |
| Visibility fogging | Humidity control failure | Check visor; check LCVG flow | Reduce exertion; crack purge valve |

## Glossary

- **EVA**: Extravehicular Activity — any work performed by an astronaut outside a pressurised spacecraft
- **PLSS**: Portable Life Support System — the backpack that supplies oxygen, scrubs CO₂, and manages thermal control for the suit
- **PGT**: Pistol Grip Tool — the battery-powered torque wrench used for all EVA fastener operations
- **SAFER**: Simplified Aid for EVA Rescue — the nitrogen-jet self-rescue backpack
- **PFR**: Portable Foot Restraint — the socket-and-clip platform that anchors the astronaut's boots
- **BRT**: Body Restraint Tether — a telescoping rigid rod that anchors the suit to station structure
- **ORU**: Orbital Replacement Unit — a modular component designed for swap-out during EVA
- **NBL**: Neutral Buoyancy Laboratory — the underwater training pool at JSC
- **DCS**: Decompression Sickness — the condition caused by nitrogen bubble formation in tissues during depressurisation
- **ATTITUDE HOLD**: SAFER's automatic stabilisation mode that stops unwanted rotation
- **LCVG**: Liquid Cooling and Ventilation Garment — the undergarment that circulates water for thermal regulation
- **FOD**: Foreign Object Debris — any loose item that could damage station systems
