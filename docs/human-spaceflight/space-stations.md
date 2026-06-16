# Space Stations

> **Node ID**: human-spaceflight.space-stations
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `spacecraft-systems.bus-structure`, `automation`, `construction`, `metals`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: space_stations, habitat_modules, docking_systems, robotic_manipulator_arms
> **Critical**: Yes

A space station is a pressurised outpost assembled in orbit from individually launched modules, then continuously crewed for months or decades. It combines every subsystem in the tech tree — [life support](./eclss.md), [spacesuits](./space-suits.md), [spacecraft power](../spacecraft-systems/spacecraft-power.md), [thermal control](../spacecraft-systems/thermal-control.md), and [telecom](../telecom/index.md) — into a single integrated platform. The station itself adds four disciplines that no uncrewed satellite needs: habitable volume, structural docking interfaces, robotic manipulator arms for assembly and capture, and a logistics resupply chain to sustain the crew indefinitely.

This article covers the integrated design of space stations across four process areas: [habitat module fabrication](./space-stations.habitat-modules.md) (pressure vessels, meteoroid shielding, rack integration), [structural docking and berthing](./space-stations.structural-docking.md) (common berthing mechanisms, probe-and-drogue adapters), [robotic manipulator arms](./space-stations.robotic-arms.md) (Canadarm2, Dextre, ERA), and [logistics resupply](./space-stations.logistics-resupply.md) (Cargo Dragon, Cygnus, HTV, Progress rendezvous and cargo transfer). Together they define what it takes to keep humans alive and productive in orbit for years.

## Overview

The International Space Station (ISS) is the reference architecture. Assembled from 1998 to 2011 across more than 40 assembly flights, the ISS comprises 16 pressurised modules with a total pressurised volume of 916 m³ and a total mass of approximately 420,000 kg. The truss structure spans 109 m from end to end; the solar array wings cover 2,500 m² and generate up to 100 kW of electrical power. A crew of six — expandable to seven — conducts roughly 250 ongoing experiments across science disciplines during continuous occupation now exceeding two decades.

The [spacecraft bus structure](../spacecraft-systems/bus-structure.md) heritage provides the module hulls: each pressurised module is fundamentally a spacecraft bus scaled up to human-rated diameter. The [automation](../automation/index.md) domain supplies the joint controllers, motor drives, and teleoperation interfaces for robotic arms. [Construction](../construction/index.md) techniques — precision alignment, bolted joint preload, structural shimming — translate from ground assembly to on-orbit integration. [Metals](../metals/index.md) provide the aluminium-lithium, stainless steel, and titanium alloys for pressure vessels, docking rings, and fastener systems.

## Operational Stations

### International Space Station (ISS)

The ISS is the largest human-built structure in orbit. Its assembly required the convergence of five space agencies (NASA, Roscosmos, ESA, JAXA, CSA) and the development of the [space shuttle](https://www.nasa.gov), Russian Proton, and Soyuz launch systems to deliver modules one at a time.

| Parameter | Value |
|-----------|-------|
| Mass | 420,000 kg |
| Length (truss) | 109 m |
| Pressurised volume | 916 m³ |
| Pressurised modules | 16 (15 active) |
| Solar array area | 2,500 m² |
| Power generation | 75-100 kW |
| Crew | 6 (nominal), 7 (surge) |
| Orbital altitude | 408 km |
| Orbital inclination | 51.6° |
| Orbital velocity | 27,600 km/h |
| Atmospheric drag makeup | 7,000 kg/yr propellant |

The US Orbital Segment (USOS) modules berth to Node modules via the Common Berthing Mechanism (CBM), while Russian segment modules dock via the Probe-and-Drogue and Hybrid systems. The CBM is a 1.27 m square hatch passage — large enough to pass full-size International Standard Payload Racks (ISPRs) — that mates two modules with a capture-and-berth sequence executed by the robotic arm.

### Tiangong CSS

China's Tiangong space station (Tiangong gongjian kongtian, "Heavenly Palace") achieved its three-module configuration in 2022. It represents a leaner architecture than the ISS — fewer modules, smaller crew, but with modern subsystems designed from the outset for long-duration operation.

| Parameter | Value |
|-----------|-------|
| Mass | ~100,000 kg |
| Modules | 3 (Tianhe core, Wentian, Mengtian) |
| Pressurised volume | ~340 m³ |
| Power generation | ~27 kW |
| Crew | 3 (nominal), 6 (during handover) |
| Orbital altitude | 340-450 km |
| Orbital inclination | 41.5° |

Tianhe provides life support, living quarters, and propulsion. Wentian and Mengtian are experiment modules, each carrying airlock cabins for [EVA](./eva.md) and payload exposure. The station uses a derivative of the APAS (Androgynous Peripheral Attach System) docking mechanism.

### Commercial Stations (Planned)

The ISS is expected to retire by 2030-2031. NASA's Commercial Low Earth Orbit Development (CLD) programme is funding the next generation of commercially owned and operated stations:

- **Orbital Reef** (Blue Origin, Sierra Space): A mixed-use "business park" design targeting 10-person capacity by the late 2020s, with inflatable expandable modules (LIFE — Large Integrated Flexible Environment) providing high volume per launch.
- **Starlab** (Nanoracks, Lockheed Martin, Thales Alenia): A single-launch station with a 340 m³ inflatable habitat and a docking node, designed to support four crew continuously. Targeted operational date 2027.
- **Axiom Station** (Axiom Space): Modules attach to the ISS forward Node 2 initially, then separate as a free-flying station when ISS retires. First module (Hx1) targeted 2026.

## Module Comparison

The pressurised modules that form a station's habitable volume vary widely in size, construction, and function. The table below compares representative modules across operational stations:

| Module | Station | Mass (kg) | Length (m) | Diameter (m) | Volume (m³) | Launch |
|--------|---------|-----------|-----------|-------------|------------|--------|
| Destiny (US Lab) | ISS | 14,515 | 8.5 | 4.3 | 106 | 2001 (STS-98) |
| Harmony (Node 2) | ISS | 14,288 | 7.2 | 4.4 | 70 | 2007 (STS-120) |
| Tranquility (Node 3) | ISS | 18,588 | 6.7 | 4.5 | 74 | 2010 (STS-130) |
| Kibo (JEM PM) | ISS | 14,800 | 11.2 | 4.4 | 123 | 2008 (STS-124) |
| Columbus (ESA Lab) | ISS | 12,800 | 6.9 | 4.5 | 75 | 2008 (STS-122) |
| Zarya (FGB) | ISS | 19,323 | 12.6 | 4.1 | 78 | 1998 (Proton) |
| Zvezda (Service) | ISS | 19,051 | 13.1 | 4.2 | 89 | 2000 (Proton) |
| Tianhe (Core) | Tiangong | 22,600 | 16.6 | 4.2 | ~50 | 2021 (LM-5B) |
| Wentian | Tiangong | 23,000 | 17.9 | 4.2 | ~55 | 2022 (LM-5B) |

## Common Berthing Mechanism (CBM)

The CBM is the primary structural interface between USOS pressurised modules on the ISS. It is an androgynous, non-androgynous-active/passive system: one side (active) has capture latch assemblies and powered bolts; the other (passive) has capture fittings and nut plates. The CBM provides a 1.27 m × 1.27 m square passage — the largest clear hatch opening of any docking system — enabling the transfer of full International Standard Payload Racks (ISPRs).

### CBM Berthing Sequence

The CBM is a berthing system, not a docking system: the approaching module is positioned by the robotic arm, not by its own propulsion. The sequence is:

1. **T+0 min**: Robotic arm grapples the visiting vehicle's Flight Releasable Grapple Fixture (FRGF)
2. **T+15 min**: Arm slowly translates the module to within 10 cm of the CBM interface, aligned to ±25 mm and ±1.5°
3. **T+45 min**: Ready-to-latch indicators confirm 4 capture latch keepers are in position
4. **T+46 min**: Capture latch assembly actuates; 4 capture latches engage the passive fittings, pulling the modules into soft capture
5. **T+48 min**: 16 powered bolts drive (4.8 mm stroke), compressing the main seal and achieving hard capture at 16,330 N per bolt
6. **T+50 min**: Leak checks confirm seal integrity; hatch can be opened

### CBM Specifications

| Parameter | Value |
|-----------|-------|
| Hatch opening | 1,270 mm × 1,270 mm (square) |
| Structural attachment | 16 × M16 powered bolts |
| Bolt preload | 16,330 N per bolt |
| Main seal | Dual silicone elastomer O-rings |
| Mass (active half) | 202 kg |
| Mass (passive half) | 166 kg |
| Alignment tolerance | ±25 mm linear, ±1.5° angular |

## Robotic Arms

Space station robotic arms perform module berthing, [EVA](./eva.md) crew restraint, payload handling, and external inspection. Three major arm systems are currently in service on the ISS.

### Canadarm2 (SSRMS)

The Space Station Remote Manipulator System (SSRMS), known as Canadarm2, is the primary robotic arm of the ISS. Built by MDA (Canada) under the Canadian Space Agency's contribution to the ISS programme, it was delivered on STS-100 in 2001.

| Parameter | Value |
|-----------|-------|
| Length | 17.6 m |
| Mass | 1,800 kg |
| Degrees of freedom | 7 |
| Lifting capacity (station mass) | 116,000 kg |
| Lifting capacity (fine positioning) | 0-1,200 kg |
| Tip positioning accuracy | ±45 mm |
| Joint actuators | Brushless DC motors with harmonic drives |
| End effectors | Latching End Effector (LEE) × 2 |
| Grapple fixtures | PDGF (Power Data Grapple Fixture) |

Canadarm2 is symmetric — both ends can grapple a PDGF, allowing the arm to "walk" end-over-end across the station's surface by relocating its base from one PDGF to another. Each LEE contains three snare cables that close around the grapple fixture pin, providing a capture load of 12,000 N.

### Dextre (SPDM)

The Special Purpose Dexterous Manipulator (SPDM), called Dextre, is a two-armed robot that rides on the end of Canadarm2 for fine manipulation tasks. Delivered on STS-123 in 2008, Dextre can replace orbital replacement units (ORUs), manipulate tools, and perform tasks that would otherwise require an EVA.

### ERA (European Robotic Arm)

The European Robotic Arm, launched in 2021 on the Russian Nauka module, operates on the Russian segment of the ISS. It is 11.3 m long and can walk end-over-end like Canadarm2, but uses different grapple fixtures incompatible with the USOS arm.

## Logistics Resupply

A continuously crewed station requires a steady flow of consumables: propellant for reboost, oxygen, water, food, spare parts, and experiment hardware. Four cargo vehicles service the ISS, each with different capabilities and berthing interfaces.

### Resupply Vehicle Comparison

| Vehicle | Agency | Payload up (kg) | Payload down (kg) | Pressurised | Interface |
|---------|--------|-----------------|--------------------|-------------|-----------|
| Cargo Dragon 2 | NASA (SpaceX) | 3,300 | 2,500 | Yes | IDA docking |
| Cygnus | NASA (Northrop) | 3,500 | 0 (destructive reentry) | Yes | CBM berthing |
| HTV (Kounotori) | JAXA | 5,200 | 0 (destructive reentry) | Yes | CBM berthing |
| Progress MS | Roscosmos | 2,500 | 0 (destructive reentry) | Yes | Probe-drogue |

Cargo Dragon 2 is unique among resupply vehicles in its ability to return significant payload to Earth — critical for returning failed ORUs for repair, completed experiment samples, and biological specimens requiring analysis in ground laboratories. The other vehicles dispose of trash and waste by burning up during controlled atmospheric reentry.

### Resupply Cadence

The ISS typically receives 6-8 resupply flights per year, sustaining a crew of 6-7 for 365 days. A single crew member consumes approximately:

- Oxygen: 0.84 kg/day
- Water (potable + food): 3.0 kg/day
- Food (dry mass): 1.5 kg/day
- LiOH CO₂ scrubber cartridges: 1.0 kg/day (if not recycled)
- Total: ~6.3 kg/person/day minimum

For a crew of six over one year, this totals approximately 13,800 kg of consumables — well within the combined annual upmass of 30,000+ kg available from the four cargo vehicles.

## Pressure Vessel Design

Every habitat module is a pressure vessel: a cylindrical or spherical shell that maintains 101.3 kPa (1 atm) internal pressure against the vacuum of space while withstanding launch loads, micrometeoroid impacts, and thermal cycling.

The dominant material for ISS pressurised modules is 2219-T87 aluminium alloy, selected for its weldability, fracture toughness, and cryogenic properties. 2219 was originally developed for the Saturn V fuel tanks and remains the reference alloy for welded pressure vessels. Wall thicknesses range from 3.0 mm (thin-shell modules) to 4.8 mm (thicker modules like the US Lab Destiny).

Aluminium-lithium 2195, developed for the Shuttle Super Lightweight Tank, offers approximately 5% lower density and 30% higher specific stiffness than 2219. It is used on some newer module designs and is the baseline for several commercial station concepts.

## Meteoroid and Debris Shielding

The orbital environment contains micrometeoroids (natural particles travelling at 10-70 km/s) and orbital debris (human-made fragments travelling at 7-10 km/s relative to the station). A 1 cm aluminium sphere impacting at 10 km/s carries kinetic energy equivalent to a hand grenade.

### Whipple Shield

The standard protection is the Whipple shield, invented by Fred Whipple in 1947. It consists of a thin sacrificial "bumper" sheet spaced a stand-off distance from the pressure wall:

1. **Bumper** (1.0-2.5 mm Al 6061-T6): Shatters the impacting projectile into a debris cloud
2. **Stand-off gap** (50-300 mm): Allows the debris cloud to expand, reducing energy density
3. **Rear wall** (2.5-4.8 mm Al 2219): Stops the dispersed debris cloud without penetration

The ISS uses a modified Nextel-Kevlar stuffed Whipple shield on the USOS modules: a Nextel ceramic fabric intermediate layer catches molten projectile material, backed by Kevlar fabric for structural reinforcement. This provides protection against particles up to approximately 1.5 cm diameter.

## On-Orbit Assembly

The ISS was assembled over 13 years through more than 40 launches and 160+ EVAs. The assembly sequence required precise coordination of launch scheduling, module delivery, robotic arm operations, and EVA tasks — each dependent on the previous step.

Key assembly principles include:

- **Node-centric architecture**: Node modules (Unity, Harmony, Tranquility) provide 6 ports for berthing other modules, acting as intersection hubs
- **Truss backbone**: The integrated truss structure carries solar arrays, radiators, and ammonia cooling loops, assembled segment by segment
- **Robotic-assisted berthing**: Every CBM berthing requires the robotic arm to position the module — no visiting module docks directly to a CBM
- **EVA-assisted connection**: Fluid line hookups (ammonia, water, data, power) between modules are mated manually during post-berthing EVAs

### Assembly Milestones

| Date | Event | Module / Element |
|------|-------|-----------------|
| 1998 Nov | First element launch | Zarya (FGB) |
| 1998 Dec | First US element | Unity (Node 1) |
| 2000 Jul | Service module | Zvezda |
| 2000 Nov | First crew (Expedition 1) | 3-person crew |
| 2001 Feb | US Laboratory | Destiny |
| 2001 Apr | Robotic arm | Canadarm2 (SSRMS) |
| 2008 Feb | European laboratory | Columbus |
| 2008 Mar | Dextre (SPDM) | Fine manipulation robot |
| 2008 Jun | Japanese laboratory PM | Kibo (JEM PM) |
| 2011 May | Final assembly flight | STS-134 (Alpha Magnetic Spectrometer) |

## Interior Configuration

Inside each pressurised module, racks line the cylindrical walls in standardized arrays. The International Standard Payload Rack (ISPR) defines the common envelope: a sealed box 1.05 m wide, 1.90 m tall, and 0.86 m deep, with a mass allowance of 700 kg. Every USOS module is designed around the ISPR envelope, and the CBM square hatch was sized specifically to pass an ISPR without disassembly.

### Rack Categories

| Rack type | Function | Typical location |
|-----------|----------|------------------|
| ISPR (science) | Experiment payload | Destiny, Columbus, Kibo |
| System rack | ECLSS, power distribution | Node modules, Destiny |
| Storage rack | Cargo stowage, food | All modules |
| Human-rated facility | Crew sleep quarters, galley, waste | Node 3, Harmony |

Each rack connects to the module's utility panels through a standardised utility interface: power (120 V DC), data (MIL-STD-1553, Ethernet), cooling water, vacuum exhaust, and gas supply. Rack installation is performed by the crew inside the module, sliding the rack on guide rails and engaging quick-disconnect fluid and electrical connectors.

## Power Subsystem

The ISS generates electrical power from eight Solar Array Wings (SAWs), each 34 m × 12 m, mounted on the integrated truss structure. The arrays use silicon photovoltaic cells with an initial conversion efficiency of 14.2% (degrading to approximately 11% after 15 years due to radiation and thermal cycling).

| Parameter | Value |
|-----------|-------|
| Array count | 8 wings (4 pairs) |
| Total array area | 2,500 m² |
| Cell type | Silicon (8 cm × 8 cm) |
| Initial power | 100 kW |
| Power (after 15 yr) | ~75 kW |
| Energy storage | 24 × NiH₂ batteries (now Li-ion) |
| Distribution | 120 V DC primary bus |

In 2017-2021, the original nickel-hydrogen batteries were replaced with lithium-ion units, cutting battery mass by half and extending cycle life from 6.5 years to 10+ years. The [solar cell](../spacecraft-systems/spacecraft-power.md) and [battery](../spacecraft-systems/spacecraft-power.md) heritage traces directly to the spacecraft power system domain.

## Thermal Management

The station rejects approximately 75-100 kW of waste heat through an active thermal control system using two ammonia loops on the truss and water loops inside the pressurised modules.

### Thermal Loop Architecture

1. **Internal loop (water)**: Circulates water at 4-30°C through cabin heat exchangers, avionics cold plates, and rack interfaces — collecting heat inside the pressurised volume
2. **Interface heat exchanger**: Transfers heat from the water loop to the external ammonia loop across a plate-fin heat exchanger, keeping ammonia outside the habitable volume (ammonia is toxic)
3. **External loop (ammonia)**: Pumps ammonia at -1 to +3°C through 12 radiators mounted on the truss, each 13.6 m × 4.6 m, rejecting heat to deep space via infrared radiation
4. **Radiators**: 14 panels (2 per truss segment) with a combined area of 1,680 m², capable of rejecting up to 200 kW

## Troubleshooting

| Symptom | Likely cause | Diagnostic | Fix |
|---------|-------------|-----------|-----|
| CBM bolt fails to drive | Bolt jam in nut plate | Telemetry bolt current; visual arm survey | Warm-restart bolt motor; EVA manual override |
| Arm LEE snare fails to capture | PDGF pin misalignment | Check grapple camera imagery | Reposition arm; retry capture |
| Module pressure decay | Seal degradation or micrometeoroid leak | Isolate module; monitor delta-P | Patch leak from inside; contingency EVA for external repair |
| Resupply vehicle berthing miss | Arm positioning error | Review arm joint telemetry | Recycle to standoff; re-attempt with updated alignment |

## Glossary

- **CBM**: Common Berthing Mechanism — the square-hatch berthing interface for USOS ISS modules
- **SSRMS**: Space Station Remote Manipulator System — Canadarm2, the 17.6 m primary robotic arm
- **SPDM**: Special Purpose Dexterous Manipulator — Dextre, the two-armed fine manipulation robot
- **PDGF**: Power Data Grapple Fixture — the target pin that the arm's LEE grasps
- **LEE**: Latching End Effector — the snare-cable grasping mechanism at each arm tip
- **ISPR**: International Standard Payload Rack — the standardised rack size that passes through the CBM
- **ORU**: Orbital Replacement Unit — a component designed for swap-out in orbit
- **FRGF**: Flight Releasable Grapple Fixture — the grapple interface on a visiting vehicle
- **FGB**: Functional Cargo Block — the Russian term for the Zarya initial module
- **Whipple shield**: A multi-layer meteoroid shield with a sacrificial bumper and rear wall
