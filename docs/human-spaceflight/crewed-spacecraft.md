# Crewed Spacecraft

> **Node ID**: `human-spaceflight.crewed-spacecraft`
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: [`launch-vehicles.edl`](../launch-vehicles/edl.md),
> [`metals`](../metals/index.md), [`aerospace.aviation`](../aerospace/aviation.md),
> [`computing`](../computing/index.md)
> **Enables**: Crewed orbital flight, lunar missions, space station rotation, planetary return
> **Timeline**: Years 50-200+
> **Outputs**: crewed_capsules, launch_abort_systems, docking_systems, reentry_systems
> **Critical**: No — advanced integration capability requiring mature launch vehicles, EDL,
> computing, and aerospace heritage. A crewed spacecraft is a launch vehicle payload that must
> keep its occupants alive through launch, orbital flight, rendezvous, and the most violent
> environment in the tree: atmospheric reentry from orbital or lunar return velocity.

A crewed spacecraft is the most demanding integration task in the technology tree. Unlike an
uncrewed satellite, it must protect fragile biological cargo through four regimes that each
push hardware to its limit: the 3-4 g vibration and acoustic shock of launch, the thermal
and vacuum environment of orbit, the millimetre-precision of docking, and the plasma-sheathed
8-11 km/s inferno of reentry. Every subsystem — pressure shell, life support, thermal
protection, guidance, landing — must fail-safe at every step, because the crew cannot be
replaced.

## Crewed Capsule Comparison

| Capsule | Crew | Launch mass | Reentry | Heat shield | Reentry g-load | First crewed |
|---------|------|-------------|---------|-------------|----------------|--------------|
| Soyuz (Russia) | 3 | 7,080 kg | Ballistic or lifting | Soyuz ablator (phenolic) | 3.5-4.0 g (lifting) / 8-9 g (ballistic) | 1967 |
| Apollo CM (NASA) | 3 | 5,560 kg | Lifting, -1.7 L/D | Avcoat (honeycomb ablator) | 4-7 g (lunar return) | 1968 |
| Shenzhou (China) | 3 | 7,840 kg | Lifting | Silica-phenolic ablator | 3-4 g | 2003 |
| Crew Dragon (SpaceX) | 7 | 12,519 kg | Lifting, propulsive option | PICA-X (phenolic impregnated carbon ablator) | 3-4 g | 2020 |
| Orion (NASA/ESA) | 4-6 | 10,400 kg | Lifting, -1.5 L/D | Avcoat (block) | 4-5 g (lunar return at 40,000 km/h) | Not yet characterized (Artemis program) |
| Starship crew (SpaceX) | 100+ | ~1,200,000 kg | Lifting, propulsive | Hexagonal ceramic tiles | In development | In development |

## Crew Dragon (Spacex)

Crew Dragon is the first commercially developed crewed spacecraft, flying NASA astronauts to
the ISS since 2020. It is a fully autonomous capsule with manual-override touchscreen
controls — there is no physical stick or throttle.

| Parameter | Crew Dragon value |
|-----------|-------------------|
| Crew capacity | 7 seats (4 for NASA ISS missions) |
| Launch mass | 12,519 kg |
| Diameter | 4.0 m |
| Pressurised volume | 9.3 m3 |
| Heat shield | PICA-X (phenolic impregnated carbon ablator) |
| Thermal limit | rated for lunar-return velocities (~11 km/s) |
| Parachutes | 4 main (Mark 3), 2 drogue |
| Propulsive landing | designed but not used for crew; SuperDracos for abort |
| Autonomous docking | via IDA / APAS-95 interface to ISS |
| On-orbit endurance | 210 days docked |

The PICA-X heat shield is the headline technology: a phenolic-impregnated carbon ablator
developed from NASA's Stardust mission, refined by SpaceX to roughly 10% of the original
unit cost while surviving lunar-return heat flux (~2,500 W/cm2). The capsule returns under
four main parachutes (a Mark 3 nylon ringsail cluster, sized to two-out redundancy),
splashing down in the Atlantic at 7-8 m/s. The SuperDraco engines (8 x 73 kN) provide
launch-abort capability integrated into the capsule — the first system to use the same
engines for abort and (originally) propulsive landing.

## Soyuz

Soyuz is the longest-flying crewed spacecraft in history (1967-present). A three-seat
capsule massing just over 7 tonnes, it is small, rugged, and extraordinarily reliable.

| Parameter | Soyuz value |
|-----------|--------------|
| Crew capacity | 3 (custom-moulded couches) |
| Launch mass | 7,080 kg |
| Diameter (descent module) | 2.2 m |
| Pressurised volume (descent) | 2.5 m3 |
| Heat shield | phenolic-impregnated asbestos ablator |
| Reentry mode | lifting (guidable) or ballistic fallback |
| Peak g-load | 3.5-4.0 g lifting / 8-9 g ballistic |
| Parachutes | 1 drogue + 1 main (with solid retrorocket soft-landing) |
| On-orbit endurance | ~200 days |

Soyuz descends under a single main parachute, with retrorockets firing 0.8 m above the
ground to cushion touchdown to 1-2 m/s. The descent module is a bell-shaped capsule with a
-0.3 lift-to-drag ratio: it can generate lift by offsetting its centre of mass, allowing
guided reentry at 3.5-4 g. If guidance fails, it falls into ballistic reentry, spiking to
8-9 g — uncomfortable but survivable.

## Orion

Orion is NASA's deep-space crewed capsule, designed for lunar and eventually Mars missions
under the Artemis programme. It is the only Western capsule rated for the 40,000 km/h
(11 km/s) lunar-return environment since Apollo.

| Parameter | Orion value |
|-----------|--------------|
| Crew capacity | 4-6 seats |
| Launch mass | 10,400 kg (capsule + service module) |
| Diameter | 5.0 m |
| Pressurised volume | 8.95 m3 |
| Heat shield | Avcoat (epoxy-phenolic in fibreglass honeycomb, block-replaceable) |
| Service module | European Service Module (ESM) — Airbus, based on ATV |
| ESM propellant | 8,600 kg (MMH / MON-3 bipropellant) |
| Main engine | 1 x Orbital Maneuvering System (27.7 kN) |
| Delta-v | 1,580 m/s |
| Solar arrays | 4 x 7 m2 arrays, 11.1 kW |
| Lunar return velocity | ~40,000 km/h (11 km/s), ~4-5 g peak |

The European Service Module provides propulsion, power, water, and atmosphere storage,
derived from the Automated Transfer Vehicle that resupplied the ISS. The Avcoat heat shield
was originally fabricated as 330,000 honeycomb cells hand-filled with ablator (Apollo-era
process); later production moved to blocks for reusability. Orion reenters from lunar
return at 40,000 km/h — generating a 2,800°C plasma sheath and roughly 4-5 g for the crew.

## Starship (Crewed Variant)

Starship, in development by SpaceX, aims to be the first fully reusable crewed spacecraft
with deep-space capability and a nominal capacity of 100+ passengers. Unlike capsules above,
Starship reenters belly-first (high surface area, lower peak heat flux) using hexagonal
ceramic thermal tiles, and lands propulsively — no parachutes, no ocean splashdown. As of
the time of writing, the crewed configuration has not flown; the engineering challenges
(on-orbit refilling, life support for 100, tile reliability) remain open.

## Crew Cabin Atmosphere and Life Support

The crew cabin must reproduce a breathable, temperature-controlled atmosphere for the full
mission duration. The baseline is sea-level-equivalent: 101 kPa (14.7 psi), 78% nitrogen /
21% oxygen, 20-22°C, 30-70% relative humidity. This requires five interlocking subsystems:

| Subsystem | Function | Capacity / Spec |
|-----------|----------|-----------------|
| O2 storage | Breathing gas make-up | Crew Dragon: high-pressure O2 tanks; Soyuz: compressed O2 + solid KO2 candles (also scrub CO2) |
| N2 storage | Cabin pressurisation, make-up for leakage | High-pressure N2 tanks |
| CO2 removal | Scrub exhaled CO2 | LiOH cartridges (Apollo, Dragon) or regenerable amine beds (Orion) |
| Humidity control | Condense and remove exhaled/evaporated water | Condensing heat exchanger + water separator |
| Trace contaminant control | Remove CO, VOCs, metabolic byproducts | Activated charcoal + catalytic oxidiser |

A four-person crew metabolises roughly 2.5 kg O2 per day, exhales 3.0 kg CO2, and produces
1.5 kg of water vapour. For a 6-month ISS expedition, that totals roughly 450 kg of O2 and
540 kg of CO2 to manage — which is why long-duration missions (ISS, planned Mars) shift to
regenerable systems (amine beds, electrolysis water recycling) rather than open-loop
cartridges.

Cabin pressure is actively regulated: a pressure sensor drives a solenoid valve that admits
O2 or N2 from storage to hold 101 kPa. If pressure drops below 95 kPa (a slow leak), the
emergency O2 system kicks in; if it drops below 70 kPa, the crew dons IVA suits (see
[Space Suits](./space-suits.md)).

## Pressure Vessel and Structural Design

The crew cabin is a pressure vessel: it holds 101 kPa against the vacuum of space. The
classic design is a **double-walled aluminium-lithium shell**: an inner pressure vessel
(2-4 mm Al-Li, welded) carries the pressure load, and an outer meteoroid/debris shield
(Whipple shield: thin bumper spaced off the inner wall by 5-15 cm) absorbs micrometeoroid
impacts. Crew Dragon uses a structural aluminium tankage shell; Orion uses aluminum-lithium
2195 alloy for both the capsule and ESM structure.

Windows are the structural weak point: a fused-silica glass pane in a pressure shell must
withstand the full pressure delta without cracking, while surviving thermal shock, acoustic
vibration, and micrometeoroid pitting. Crew Dragon has no side windows (cargo-derived
design); Orion's four 58 cm side windows use triple-paned fused silica with a redundant
inner pressure pane.

## Rendezvous and Proximity Operations

Docking is the final metre of a rendezvous that begins hours earlier. The sequence:

1. **Phasing burns**: the chaser spacecraft adjusts its orbit to arrive near the target's
   orbital plane, then circularises at the target's altitude.
2. **Relative navigation**: at 30-50 km separation, the chaser switches to relative
   navigation sensors (GPS differential, star trackers, LIDAR) to close the range.
3. **Approach corridor**: from 1 km to 100 m, the chaser approaches along a safety corridor
   (keep-out zone around the target) using proportional thrusters.
4. **Final approach**: from 100 m to contact, at 1-10 cm/s closing velocity, with active
   hold-and-retreat capability if anything deviates.
5. **Contact and capture**: at 1-5 cm/s, the docking ring engages, soft-capture latches
   fire, then hard-capture hooks lock the two vehicles together.

Crew Dragon performs the entire sequence autonomously; the crew monitors and can take manual
control via touchscreen. Soyuz historically required manual docking on the final 200 m
(Kurs system automated to that point).

## Launch Abort Systems (LAS)

A launch abort system pulls the crew capsule clear of a failing rocket. It must detect a
failure, ignite, and extract the capsule within 1-2 seconds — before the rocket explodes —
while imposing 6-15 g on the crew for 2-6 seconds.

| LAS | Type | Thrust | Burn | Peak g | Escape |
|-----|------|--------|------|--------|--------|
| Apollo LES | solid escape tower | 680 kN | 3.2 s | ~7 g | pad to 91 km |
| Soyuz SAS | solid escape tower | 730 kN | 4-6 s | 10-14 g (ballistic) | pad to T+2.5 min |
| Shenzhou | solid escape tower | ~730 kN | 3-5 s | 10-14 g | pad to T+2 min |
| Crew Dragon | integrated SuperDraco (pusher) | 8 x 73 kN = 584 kN | 5-7 s | 4-6 g | pad to orbit |
| Orion LAS | solid escape tower | 1,800 kN | 3-6 s | ~7-10 g | pad to T+3 min |

Two architectures dominate. **Escape-tower LAS** (Apollo, Soyuz, Shenzhou, Orion): a solid
motor sits on a tower above the capsule, pulls it up and away when fired, then is jettisoned
once no longer needed (after Max-Q). **Pusher LAS** (Crew Dragon): eight SuperDraco engines
integrated into the capsule sidewall push it off the booster, with no tower to jettison and
the engines reusable for propulsive landing. Pusher abort enables abort-to-orbit (the capsule
can continue to orbit rather than always returning to landing), and works all the way to orbit
insertion.

The Soyuz T-10-4 abort in 1983 demonstrated tower LAS: the rocket caught fire on the pad, the
SAS fired, and the capsule was thrown 2 km clear, landing safely — while the pad was
destroyed. The Crew Dragon in-flight abort test (2020) demonstrated pusher LAS, destroying a
Falcon 9 deliberately and recovering the capsule intact.

## Docking Systems

Docking joins two spacecraft in orbit. It requires soft capture (initial contact, damping
relative velocity), structural hard capture (locking the rings together), and a pressure-tight
seal to allow hatch opening and crew transfer.

| System | Type | Used by | Notes |
|--------|------|---------|-------|
| Probe-and-drogue | active probe / passive cone | Soyuz, Progress, Apollo CSM-LEM | One side has a probe, the other a receiving cone; non-androgynous (male/female halves) |
| APAS-95 | androgynous peripheral | Shuttle-ISS, Crew Dragon | Both sides identical; any vehicle can dock any other |
| IDA / NDS | androgynous peripheral, international | Crew Dragon, Starliner, Orion (ISS IDA ports) | The modern standard, based on APAS / LIDS |
| CBM | common berthing mechanism | ISS modules, Cargo Dragon | Non-androgynous berthing (robot arm positions, then bolts); not for crewed docking |

**APAS (Androgynous Peripheral Attach System)** and its successor **IDA (International
Docking Adapter) / NDS (NASA Docking System)** are androgynous: either vehicle can be the
active partner. The interface is a ring of capture latches surrounded by 12 structural hooks;
soft capture occurs on contact via spring-loaded petals, then motorised hooks pull the two
vehicles together for hard capture. Crew Dragon and Starliner both dock autonomously to IDA
ports on the ISS — no astronaut hand-flying required.

The **Soyuz probe-and-drogue** is the older, non-androgynous design: the Soyuz carries a
spring-loaded probe that seats into a cone on the station, damps the approach velocity, then
a drive pulls the two together for hard-latch. The probe retracts after docking.

## Reentry G-Load Profiles

The reentry trajectory determines the peak g-load on the crew. A **ballistic** reentry (no
lift) is steep and violent. A **lifting** reentry (capsule generates lift by offset centre of
mass) is shallower, longer, and gentler.

| Mission profile | Entry velocity | Peak g | Duration |
|-----------------|----------------|--------|----------|
| LEO ballistic | 7.8 km/s | 8-9 g | 5-8 min |
| LEO lifting | 7.8 km/s | 3-4 g | 10-15 min |
| Lunar return lifting | 11.0 km/s | 4-7 g | 8-12 min |
| Mars return lifting | 12-14 km/s | 5-10 g | 10-15 min |
| Soyuz ballistic (failure mode) | 7.8 km/s | 8-9 g | 4-6 min |

Crew couches are custom-moulded to distribute g-load along the spine (eyeballs-in is the
tolerable direction; eyeballs-out causes retinal damage above ~10 g). The Soyuz uses
individual custom-fibreglass couches cast to each crew member's body. Apollo and Orion
recumbent-position the crew to take g through the back and seat.

## Prerequisites

- [Launch Vehicles EDL](../launch-vehicles/edl.md) — reentry, heat shield, parachute heritage
- [Metals](../metals/index.md) — aluminum-lithium pressure shells, titanium fittings
- [Aviation](../aerospace/aviation.md) — cabin pressurisation and structural heritage
- [Computing](../computing/index.md) — flight software, avionics, GNC

## Sub-Processes

- [Crew Cabin Design](./crewed-spacecraft.crew-cabin.md) — pressure vessel, atmosphere, layout
- [Launch Abort Systems](./crewed-spacecraft.launch-abort-systems.md) — escape tower and abort motors
- [Docking Systems](./crewed-spacecraft.docking-systems.md) — APAS, probe-cone, capture latches
- [Reentry Systems](./crewed-spacecraft.reentry-systems.md) — heat shield, trajectory, recovery

## See Also

- [Space Suits](./space-suits.md) — crew pressure garment backup to cabin
- [Launch Vehicles](../launch-vehicles/index.md) — booster and EDL heritage
- [Aerospace](../aerospace/index.md) — aviation cabin and life-support heritage
- [Computing](../computing/index.md) — flight software and avionics

---

*Part of the [Bootciv Tech Tree](../index.md) • [Human Spaceflight](./index.md) • [All Domains](../index.md)*
