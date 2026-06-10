# Resistance Welding (Spot & Seam)

> **Node ID**: machine-tools.joining.resistance-welding
> **Domain**: [Machine-Tools](./index.md)
> **Dependencies**: See prerequisites
> **Enables**: [`Metal Joining`](joining.md), [`Electricity Generation & Distribution`](../energy/electricity.md)
> **Timeline**: Years 20-50
> **Outputs**: resistance_welds, spot_welds, seam_welds
> **Critical**: No

## Overview

Spot welding (copper electrodes, 5000-20000A, 1-10 cycles at 50Hz) and seam welding (roller electrodes, overlapping spots for continuous gas-tight seams). No filler, no gas, no flux. Uses resistance heating at the workpiece interface: H = I²Rt. Projection welding for nuts and brackets. Critical for automotive body assembly and battery tab welding.

Resistance welding generates heat at the joint interface through electrical resistance. The workpiece material, the contact resistance between the two sheets, and the bulk resistance of the material itself all contribute. Heat is concentrated at the interface between the workpieces because the contact resistance there is highest. Electrode force and current are applied for a precise number of cycles, forming a nugget of fused metal at the interface that solidifies under continued electrode pressure.

The process is inherently fast: a single spot weld completes in a fraction of a second, and requires no consumable filler material, shielding gas, or flux. This makes it economical for high-volume production. The primary limitation is that it works best on sheet metal of similar thickness and composition, and the electrodes must be periodically dressed or replaced as they wear from repeated heating and mechanical contact.

Projection welding uses pre-formed projections (bumps) on one workpiece to localize current and heat at specific points, allowing simultaneous welding of multiple locations in a single press cycle. This is the standard method for welding threaded nuts and studs to sheet metal panels in automotive and appliance manufacturing.

Primary outputs: `resistance_welds`, `spot_welds`, `seam_welds`.

Resistance welding was among the earliest forms of electric welding, with the first spot welding patents issued in the late 19th century. The process found rapid application in automotive manufacturing, where the need to join thin steel sheets at high speed made resistance welding the natural choice for body assembly. A modern automotive body contains thousands of spot welds, each completed in a fraction of a second by robotic welding guns.

The heat generation equation H = I²Rt defines the process. Current (I) is the dominant variable because heat is proportional to the square of current. Doubling the current produces four times the heat. The resistance (R) is determined by the material properties and the contact conditions at the interface.

Resistance welding is uniquely suited to high-volume production because the process requires no consumables (no filler wire, no shielding gas, no flux), completes each weld in a fraction of a second, and can be fully automated. The economics of resistance welding improve with production volume: the capital cost of robotic welding guns and MFDC power supplies is amortized over millions of welds in automotive production.

## Prerequisites

### Materials

- Sheet metal workpieces (steel, stainless steel, aluminum, or dissimilar combinations)
- Copper-chromium-zirconium alloy electrode caps and shanks
- Cooling water for electrodes (recirculated or once-through)

### Equipment

- Resistance welding power supply: AC (transformer-based), MFDC (medium-frequency direct current, inverter-based), or CD (capacitor discharge)
- Spot welding gun (pneumatic, hydraulic, or servo-driven) or seam welding machine with roller electrodes
- Electrode tip dresser (lathe-type or mill-type) for maintaining electrode face geometry

### Knowledge

- Resistance heating principles: how current, resistance, and time interact to form the weld nugget (H = I²Rt)
- Electrode materials, tip geometry, and dressing schedules for consistent nugget formation
- Dynamic resistance monitoring: interpreting the resistance curve during each weld to detect problems in real time
- Weld schedule development: selecting current, time, and force for material type and thickness combinations
- Shunting currents and how they cause missed welds in multi-spot assemblies

### Infrastructure

- Resistance welding machine with programmable current, time, and force (MFDC preferred for consistent results)
- Cooling water circulation system for electrodes and transformer (5-10 L/min per electrode)
- Compressed air supply for pneumatic weld guns (6-8 bar)
- Electrode tip dresser and replacement electrode caps inventory
- Quality testing area with peel test fixture and cross-section sample preparation

## Process Description

In spot welding, two copper alloy electrodes clamp the workpieces together under controlled force. A high-amplitude, low-voltage current passes through the electrodes and workpieces for a precise number of power line cycles (typically 1-30 cycles at 50/60 Hz, or 20-600 ms). The bulk of the heat is generated at the interface between the two sheets, where contact resistance is highest. The molten nugget grows radially outward from the interface, reaching a specified diameter (typically 4 times the square root of the thinner sheet thickness, in mm). Current stops, and the electrode force forges the nugget solid before the electrodes retract.

### Step-by-Step Procedure

1. Clean workpiece surfaces to remove oil, scale, paint, and coatings. Surface contamination increases contact resistance unpredictably, causing inconsistent nugget size or expulsion. Mechanical cleaning (abrasive) or chemical cleaning (solvent degreasing) depending on the contaminant.
2. Position the workpieces between the electrodes. Verify that the electrodes contact the correct locations on the assembly. For multiple spot welds on one assembly, ensure minimum edge distance (typically 1.5 times the nugget diameter) to prevent edge tearing.
3. Set the weld schedule: squeeze time (electrodes reach full force before current starts), weld current (5-20 kA depending on material and thickness), weld time (cycles), and hold time (current off, electrodes maintain force during nugget solidification).
4. Initiate the weld cycle. The electrodes close under force, current flows for the programmed time, then stops. The electrodes maintain force during hold time to forge the nugget.
5. Open the electrodes. Inspect the spot weld visually for surface indentation depth and any signs of expulsion (metal splash around the weld). Excessive indentation indicates too much heat or insufficient electrode force.
6. Periodically perform destructive peel testing on sample welds to verify nugget diameter meets the minimum specification. Section and measure nugget diameter under magnification.
7. Dress or replace electrode tips per the maintenance schedule. As electrode tips mushroom and degrade, current density drops and nugget size decreases below the minimum specification.

The weld schedule is the combination of squeeze time, weld current, weld time, and hold time that defines the welding cycle. Squeeze time allows the electrodes to reach full clamping force before current flows, preventing expulsion caused by current passing through poorly contacting surfaces. Hold time maintains electrode force after current stops, allowing the nugget to solidify under pressure and preventing the formation of shrinkage voids. A properly developed weld schedule produces consistent nugget size across the full range of production variability.

Developing a weld schedule for a new material or thickness combination begins with published starting parameters, then refines through systematic testing. Current is increased until expulsion occurs, then reduced by 10-15%. Weld time is adjusted to achieve the target nugget diameter as measured by destructive peel testing. Force is set high enough to contain the molten nugget but not so high as to cause excessive indentation. The final schedule is validated by producing a minimum of 30 consecutive welds and verifying that all meet the minimum nugget diameter specification with a standard deviation below 10% of the mean.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Weld Current | 5-20 kA | Higher current for thicker material; MFDC preferred for consistency |
| Weld Time | 1-30 cycles (50Hz) | 20-600 ms; shorter time with higher current reduces heat-affected zone |
| Electrode Force | 1-8 kN | Sufficient to maintain contact and contain the molten nugget |
| Electrode Tip Diameter | 4-8 mm (for 0.5-2 mm sheet) | Matches sheet thickness; 5 times square root of thinner sheet |
| Coolant Flow | 5-10 L/min per electrode | Prevents electrode overheating; loss of cooling causes rapid electrode wear |

### Recommended Weld Schedules by Material and Thickness

| Material | Sheet Thickness (mm) | Current (kA) | Weld Time (cycles at 50Hz) | Electrode Force (kN) | Tip Diameter (mm) | Min. Nugget Dia. (mm) |
|----------|---------------------|-------------|---------------------------|---------------------|-------------------|----------------------|
| Low carbon steel | 0.5 | 5-7 | 5-8 | 1.5-2.5 | 4-5 | 2.8 |
| Low carbon steel | 0.8 | 6-8 | 8-12 | 2.0-3.0 | 5-6 | 3.6 |
| Low carbon steel | 1.0 | 7-9 | 10-15 | 2.5-3.5 | 5-6 | 4.0 |
| Low carbon steel | 1.5 | 8-11 | 12-20 | 3.0-4.5 | 6-7 | 4.9 |
| Low carbon steel | 2.0 | 9-13 | 15-25 | 4.0-6.0 | 7-8 | 5.7 |
| Stainless 304 | 0.5 | 4-5 | 4-6 | 2.0-3.0 | 4-5 | 2.8 |
| Stainless 304 | 1.0 | 5-7 | 8-12 | 3.0-4.5 | 5-6 | 4.0 |
| Stainless 304 | 1.5 | 6-9 | 10-18 | 4.0-6.0 | 6-7 | 4.9 |
| Aluminum 6061 | 0.5 | 8-12 | 3-5 | 1.5-2.5 | 5-6 | 2.8 |
| Aluminum 6061 | 1.0 | 12-18 | 5-10 | 2.5-4.0 | 6-8 | 4.0 |
| Aluminum 6061 | 1.5 | 15-22 | 8-15 | 3.5-5.5 | 8-10 | 4.9 |
| Galvanized steel | 0.8 | 8-11 | 12-18 | 2.5-4.0 | 5-6 | 3.6 |
| Galvanized steel | 1.0 | 9-13 | 15-22 | 3.0-4.5 | 6-7 | 4.0 |

Aluminum requires higher current and shorter weld times than steel because its higher thermal conductivity conducts heat away from the nugget zone faster. Galvanized steel needs higher current and longer times because the zinc coating melts first, increasing contact resistance unpredictably.

The nugget diameter in spot welding must meet minimum specifications based on the sheet thickness being joined. Adequate nugget size ensures that the weld can transfer the required shear load across the joint. Weld strength increases with nugget diameter up to the point where the weld begins to interfere with adjacent welds or approaches the sheet edge, reducing the tear-out strength of the surrounding material.

The minimum spacing between adjacent spot welds must prevent shunting, where current from a new weld finds an easier path through an existing weld rather than through the interface of the new joint. This shunting current reduces the effective heat at the new weld location, producing an undersized nugget or a complete miss. Minimum weld spacing is typically 3-4 times the nugget diameter to ensure adequate resistance in the shunting path.

## Safety Considerations

Resistance welding electrodes close with substantial force, and the high secondary currents present electrical hazards. The combination of mechanical force and electrical energy requires specific controls.

- **Pinch/crush**: Resistance welding electrodes close with 1-8 kN force. Finger or hand amputations occur when operators reach between the tips during manual spot welding. Two-hand anti-tie-down controls are mandatory on manual spot welders.
- **Expulsion (metal splash)**: Violent ejection of molten metal droplets from the weld interface occurs unpredictably when current is too high, force is too low, or surface contamination causes uneven heating. Expulsion droplets cause eye injuries and burns at several meters distance. Face protection is mandatory during manual spot welding.
- **Electrical shock**: Secondary currents reach 5-20 kA at low voltage (2-10V). While the voltage is generally safe, insulation failure on the secondary circuit can expose operators to hazardous voltage from the primary side. Regular insulation testing is required.
- **Stored energy**: Pneumatic and hydraulic resistance welders store energy in the actuator system that can cause sudden tip closure. Capacitor discharge (CD) welders store lethal electrical energy in the capacitor bank. Discharge procedures are required before maintenance.

### Personal Protective Equipment

- Safety glasses with side shields at all times (expulsion droplets travel several meters)
- Face shield when performing manual spot welding operations
- Leather gloves for handling sheet metal (sharp edges) and for protection from expulsion
- Flame-resistant sleeves or jacket for manual spot welding (expulsion burns forearms)
- Steel-toe boots for handling heavy fixtures and workpieces

### Emergency Procedures

- Verify two-hand control anti-tie-down function before each shift (both hands must be on the controls to close the electrodes; releasing either hand must immediately open the electrodes)
- Maintain cooling water flow alarm on electrode and transformer circuits (overheated transformer fails catastrophically)
- Post pinch point hazard warnings on all manual spot welders
- Train operators on expulsion response: do not look directly at the weld zone during the weld cycle
- Keep burn kit at the welding station for expulsion burns

## Quality Control

### Acceptance Criteria

- **Spot Welds**: Nugget diameter meets minimum specification (typically 4 times square root of thinner sheet thickness, in mm). No expulsion marks. Surface indentation does not exceed 25% of sheet thickness. Peel test shows button pull (weld nugget pulls out of one sheet) rather than interfacial failure.
- **Seam Welds**: Continuous gas-tight seam with no skipped spots. Overlap between successive nuggets is 30-50% of nugget diameter. Leak test passes at specified pressure.

### Testing Methods

- Peel testing of sample spot welds to verify nugget diameter: clamp one sheet in a vise, peel the other back with pliers. Measure the button diameter or torn-out nugget.
- Ultrasonic spot weld inspection for production monitoring (detects undersized or missing nuggets without destructive testing)
- Cross-section metallography of seam weld samples for penetration depth and nugget overlap verification
- Leak testing of seam welds (pressurize the enclosed volume and monitor for pressure decay)
- Dynamic resistance monitoring: the electrical resistance curve during each weld follows a characteristic shape that indicates proper nugget formation

### Sampling Protocol

- Perform daily electrode tip dressing and measurement verification; dressed tips must meet the specified face diameter within tolerance
- Peel test sample spot welds at the start of each shift and after every electrode tip change
- Log dynamic resistance curves for reference against baseline signatures; deviations signal electrode wear, surface contamination, or insufficient electrode force
- Cross-section seam weld samples from each new parameter setup
- Record weld count per electrode tip pair; replace or dress per the preventive maintenance schedule

## Scaling Notes

- **Bench scale**: Portable spot welder with hand-operated pincer arms. Laboratory and workshop sheet metal work. 1-3 kA output. Manual timing. Suitable for prototype fabrication and small assemblies.
- **Pilot scale**: Pedestal spot welder with pneumatic operation and MFDC power supply. Programmable weld schedules. Production of moderate-volume sheet metal assemblies. Electrode tip dresser on site.
- **Production scale**: Robotic spot welding guns on multi-axis arms traversing the workpiece. MFDC transformers mounted on the robot arm. Thousands of spot welds per shift on automotive body-in-white. Automated electrode tip changing and dressing stations.

Scaling from pedestal to robotic spot welding requires investment in gun design, transformer technology, and control systems. The transformer must be lightweight enough to mount on the robot arm, which drives the use of MFDC inverters (smaller and lighter than AC transformers at equivalent power). Servo-driven guns provide more precise force control than pneumatic guns, enabling consistent weld quality across varying material conditions. The integration of vision systems for seam tracking and inspection further increases the complexity and capability of production resistance welding systems.

Electrode life depends on the material being welded, the cooling effectiveness, and the mechanical wear from repeated impact. Copper-chromium-zirconium alloy electrodes provide a balance of electrical conductivity and mechanical strength at elevated temperature. Electrode tip dressing with a lathe or mill restores the face geometry and removes surface contamination, extending electrode life. Water cooling channels within the electrodes remove heat between welds.

Medium-frequency direct current (MFDC) resistance welders have largely replaced traditional AC welders in automotive and electronics manufacturing. MFDC provides more consistent heat input because the current does not pass through zero each half-cycle, and it is more efficient electrically. The smaller transformer size of MFDC systems allows mounting directly on robotic arms.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Expulsion (metal splash) | Excessive current or insufficient electrode force | Increase electrode force; reduce current; verify electrode tip alignment |
| Small nugget size | Low current, short weld time, or worn electrode tips | Increase current; extend weld time; dress or replace electrode tips |
| Sticking to electrodes | Electrode tip contamination or insufficient cooling | Dress electrodes; verify cooling water flow; check electrode material grade |
| Missed welds (shunting) | Current bypassing through adjacent welds or conductive path | Increase spacing between welds; change welding sequence to prevent current path through existing welds |
| Excessive indentation | Too much heat or too little electrode force | Reduce current or weld time; increase electrode force; use larger electrode tip diameter |
| Cracking in nugget | Welding galvanized or high-carbon steel without proper schedule | Extend hold time to allow nugget solidification under pressure; add temper pulse after weld pulse |

## Variations and Alternatives

- **Seam welding**: Roller electrodes rotate along the joint line, producing overlapping spot welds at high speed. Creates continuous gas-tight or liquid-tight seams in sheet metal containers, fuel tanks, and radiator assemblies. Wheel electrodes require continuous water cooling.
- **Projection welding**: Pre-formed projections (stamped dimples) on one workpiece concentrate current at specific points. Allows simultaneous welding of multiple points in a single press cycle. Standard method for attaching nuts, studs, and brackets to sheet metal.
- **Capacitor discharge (CD) welding**: Stores energy in a capacitor bank and discharges it in a single pulse (1-10 ms). Very short weld time limits the heat-affected zone. Used for welding near heat-sensitive components and battery cell tabs.

Resistance welding is uniquely suited to joining dissimilar metals because the heat is generated at the interface between the workpieces rather than in the bulk material. This allows joining of steel to aluminum, copper to steel, and other combinations that are difficult or impossible with fusion welding. The solid-state bond formed at the interface avoids the intermetallic compounds that weaken fusion welds in dissimilar metal pairs.

Projection welding is particularly effective for attaching threaded fasteners to sheet metal because the projections concentrate heat at the desired joint locations while the surrounding sheet remains relatively cool, preventing distortion of the panel surface. Cross-wire welding of mesh and grid products uses resistance welding to join intersecting wires at their contact points, producing reinforcement mesh for concrete construction and screening products for industrial applications.

The speed and automation compatibility of resistance welding make it the dominant joining method for high-volume sheet metal assembly. Resistance welds are inherently fast (a single spot weld completes in a fraction of a second), require no consumable filler material, and can be performed by robotic guns that follow programmed paths around the assembly. These characteristics make resistance welding the standard for automotive body construction, appliance assembly, and battery pack fabrication where thousands of joints per assembly must be made economically.

## References

- [Metal Joining](joining.md) — parent capability
- [Machine-Tools Domain](./index.md) — domain overview and related capabilities
- [Metal Joining](joining.md) — downstream capability
- [Electricity Generation & Distribution](../energy/electricity.md) — downstream capability

### Material Handling

- Clean workpiece surfaces of oil, scale, and coatings before loading; surface contamination causes expulsion and inconsistent nugget size
- Dress electrode tips to specified face diameter and alignment after the scheduled number of welds; progressive tip wear reduces current density
- Maintain cooling water flow to electrodes and transformer at all times during operation; even brief interruption causes rapid electrode degradation
- Sort welded assemblies by inspection status; segregate uninspected parts from accepted and rejected lots
- Store electrode caps in dry conditions; oxidized electrode faces produce inconsistent contact resistance
- Track electrode tip wear by logging weld count per tip pair; replace before nugget size falls below minimum specification
- Maintain weld schedule documentation for each material and thickness combination; record any schedule changes with engineering approval
- Separate different material types (galvanized, bare, stainless) in the work area to prevent welding the wrong schedule to the wrong material
- Verify electrode alignment (tip-to-tip) after every tip change; misaligned electrodes produce off-center nuggets with reduced strength
- Check cooling water temperature at the electrode return line; rising temperature indicates blockage or insufficient flow
- Maintain spare electrode caps and transformer secondary cables; production downtime from electrode failure is costly in high-volume operations
- Verify coolant flow switch alarm function before each shift; loss of cooling water during welding damages electrodes and transformer
- Check electrode alignment with a gauge after every tip dress; misaligned tips produce off-center nuggets
- Verify weld schedule is correctly programmed before starting each new part number
- Maintain a reference set of peel-tested samples for each schedule to compare with production results

---
*Part of the [Bootciv Tech Tree](../../index.md) · [Machine-Tools](./index.md) · [All Domains](../../index.md)*
