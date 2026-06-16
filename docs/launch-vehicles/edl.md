# Entry, Descent & Landing

> **Node ID**: launch-vehicles.edl
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`metals`](../metals/index.md),
> [`ceramics`](../ceramics/index.md), [`polymers`](../polymers/index.md),
> `launch-vehicles.liquid-propulsion`
> **Enables**: Stage recovery, planetary sample return, crewed landings
> **Timeline**: Years 30-200+
> **Outputs**: heat_shields, edl_systems, parachutes
> **Critical**: No — advanced capability requiring mature materials, propulsion, and precision
> navigation. EDL is the inverse of launch: converting orbital or hyperbolic velocity to zero
> relative velocity at a surface, surviving the aerothermal environment of atmospheric entry.

Entry, Descent, and Landing (EDL) is the sequence of events that brings a vehicle or payload
from orbital or interplanetary velocity to a soft landing on a surface. For Earth entry from
LEO, that means shedding 7.8 km/s of velocity. For Mars entry from a hyperbolic approach, it
means shedding 5.5-6.0 km/s in an atmosphere only 1% as dense as Earth's. The challenge is
fundamentally one of **energy management**: every kilogram entering at 7.8 km/s carries 30 MJ
of kinetic energy, and that energy must be dissipated as heat into the atmosphere, into the
thermal protection system, or through propulsive braking.

## Entry Trajectory Physics

The entry vehicle's behaviour is governed by the **ballistic coefficient**:

**β = m / (Cd × A)**

Where m is vehicle mass (kg), Cd is the drag coefficient (typically 1.2-1.5 for a blunt-body
entry capsule at hypersonic speeds), and A is the reference (base) area (m²). A **low β**
(light vehicle, large area) decelerates higher in the atmosphere: peak deceleration occurs at
higher altitude with lower peak heating, but longer descent time. A **high β** (heavy vehicle,
small area) punches deeper before decelerating: peak heating is more intense and occurs lower.

For Mars, the thin atmosphere means even a low-β vehicle decelerates late and low. The Mars
Science Laboratory (Curiosity) had β ≈ 140 kg/m² — high by Earth standards — and still required
a supersonic parachute plus a skycrane for landing because the atmosphere could not decelerate
the 900 kg rover to touchdown velocity on parachutes alone.

**Peak heating** during entry scales with the cube of entry velocity and inversely with the
square root of the nose radius (Sutton-Graves correlation):

**q̇ = k × √(ρ/Rn) × V³**

Where q̇ is stagnation-point heat flux (W/cm²), k is a planet-dependent constant (1.9027×10⁻⁴
for Earth, SI units), ρ is atmospheric density at the deceleration altitude, Rn is the nose
radius (m), and V is velocity (m/s). A larger, blunter heat shield spreads the heating over a
larger area, reducing peak flux — which is why entry capsules are blunt bodies, not sharp
nosecones.

## Heat Shield Design

The [heat shield design](./edl.heat-shield-design.md) process selects a thermal protection
system (TPS) material matched to the entry environment. Three families dominate:

### Ablative TPS: PICA

**PICA (Phenolic Impregnated Carbon Ablator)** is the workhorse ablative for high-energy entry.
Developed by NASA Ames Research Center in the 1990s, it is a low-density carbon-fibre substrate
impregnated with phenolic resin. PICA was the heat shield material for the Stardust comet-sample
return capsule (entry velocity 12.9 km/s — the fastest Earth entry ever) and for the Mars Science
Laboratory heat shield.

| Parameter | PICA | PICA-X (SpaceX) |
|-----------|------|-----------------|
| Density | 0.27 g/cm³ | 0.27 g/cm³ |
| Max service temperature | 2,900°C (2,900°C) | 2,900°C |
| Reuse target | Single-use | 10+ flights |
| Ablation onset | ~1,650°C | ~1,650°C |
| Thermal conductivity | 0.05-0.10 W/m·K | 0.05-0.10 W/m·K |

SpaceX developed **PICA-X** as a higher-performance, lower-cost variant manufactured in-house.
PICA-X retains PICA's 0.27 g/cm³ density and 2,900°C capability but is engineered for reuse —
the Dragon capsule heat shield was designed to survive multiple orbital reentries without
replacement. The reuse target of 10+ flights dramatically reduces per-mission TPS cost.

### Heritage Ablative: Apollo CM

The Apollo Command Module heat shield used a custom **ablative resin** (AVcoat 5026-39HC/G,
an epoxy-novaloc resin in a fibreglass honeycomb matrix) bonded to the stainless-steel
structure. The honeycomb cells (approximately 6.4 mm cells × 50 mm deep) were individually
filled with the ablator by a manual gunning process — one of the most labour-intensive
manufacturing steps in the Apollo programme.

| Parameter | Apollo CM |
|-----------|-----------|
| TPS density | 0.50 g/cm³ (AVcoat) |
| Peak heating | ~3,000 W/cm² |
| Peak deceleration | 6-7 g |
| Entry velocity | 11.0 km/s (lunar return) |
| Total heat load | ~44,000 kJ/m² |
| Ablation depth | ~30-70 mm (varies by location) |

Apollo's lunar-return entry velocity (11.0 km/s) produced peak heating roughly **2.5 times
more severe** than LEO return (7.8 km/s), following the V³ scaling of the Sutton-Graves
correlation. The 6-7 g peak deceleration was at the upper limit of crew tolerance — Apollo
entries were timed and angled precisely to stay within this limit.

### Reusable TPS: Shuttle Tiles

The Space Shuttle pioneered **reusable ceramic tiles** as an alternative to ablators. The LI-900
silica tile is 90% porous amorphous silica with a density of only 0.14 g/cm³ — lighter than
PICA. The tile surface is coated with a high-emissivity borosilicate glass (reaction-cured
glass, RCG) that radiates 85-90% of incident heat back to the atmosphere. The tile's low
thermal conductivity means the surface can glow at 1,260°C while the underlying aluminium
airframe stays below 175°C.

| Parameter | LI-900 (Shuttle tile) |
|-----------|----------------------|
| Density | 0.14 g/cm³ |
| Max surface temperature | 1,260°C |
| Thermal conductivity | 0.047 W/m·K (at 20°C) |
| Compressive strength | 0.6 MPa (very fragile) |

Shuttle tiles were fragile — a 5 g impact could crack them — and 100-150 tiles required
replacement after every flight due to impact and water damage. This fragility and maintenance
burden drove the shift back to ablators (PICA) for Dragon and to hexagonal reusable tiles
bonded to a transpiration-cooled backing for Starship.

## Parachute Systems

The [parachute systems](./edl.parachute-systems.md) process provides the terminal deceleration
for payloads too heavy or too sensitive for propulsive landing alone. Parachutes are
remarkably mass-efficient: a 50 kg canopy and riser can decelerate a 5-tonne payload from
200 m/s to 8 m/s. But they are fundamentally limited by **opening shock** at supersonic speeds
and by the **stability** of inflated canopies in turbulent flow.

### Parachute Types

| Type | Application | Diameter | Deploy speed | Material |
|------|-------------|----------|--------------|----------|
| Disk-Gap-Band (DGB) | Apollo CM main | 25.5 m | Subsonic | Nylon |
| Ringsail | Orion MPS main | 33.5 m | Subsonic | Kevlar/Nylon |
| Supersonic DGB | Mars Science Laboratory | 21.5 m | Mach 2.0 | Nylon/PET |

**Disk-Gap-Band (DGB)**: The DGB canopy has a flat circular disk, a gap (annular opening), and
a cylindrical band at the periphery. The gap vents high-pressure air from under the canopy,
improving stability and reducing oscillation. The DGB is the most-tested parachute design for
high-load applications — Apollo, Viking, Mars Pathfinder, and MSL all used DGB mains. The
Apollo CM three-canopy system (two drogues + three mains, each 25.5 m) slowed the 5,300 kg
capsule from 180 m/s to 8 m/s for splashdown.

**Ringsail**: The ringsail canopy is built from concentric rings of fabric with sails
protruding between rings, creating a vented, cambered profile. Ringsails achieve higher drag
coefficients (Cd ≈ 0.55 vs 0.45 for DGB) and pack smaller, making them suitable for large
payloads. The Orion Multi-Purpose Crew Vehicle uses three ringsail mains, each 33.5 m in
diameter, to decelerate the 9,000 kg capsule for ocean splashdown.

**Supersonic parachutes**: Deploying a parachute at supersonic speeds (Mach 1.5-2.5) is
extremely demanding. The canopy inflates violently — the opening shock can briefly generate
100,000 N on a canopy designed for 20,000 N steady load. The Mars Science Laboratory
parachute (21.5 m DGB) deployed at **Mach 2.0** at 10 km altitude, generating 65,000 N peak
drag to decelerate the 900 kg rover. Supersonic parachute deployment uses a mortar — a
pyrotechnic-powered cannon that fires the packed canopy into the slipstream at 30-50 m/s
relative velocity, ensuring clean inflation before the slipstream can tangle the riser.

**Reefing**: To limit opening shock, large parachutes are **reefed** — a circumferential reefing
line (a temporary loop around the canopy skirt) restricts the initial inflation to a fraction of
full diameter. After the initial shock dissipates, a pyrotechnic cutter severs the reefing line
and the canopy inflates fully. A three-reef-stage sequence (25% → 50% → 100% area) is typical
for crewed mains. Each stage lasts 6-10 seconds, smoothing the deceleration profile.

### Fabric Materials

- **Nylon** (polyamide): the workhorse parachute fabric. Tensile strength 500-800 MPa, density
  1.14 g/cm³, low cost. Used for Apollo mains, most drogues. Limiting temperature ~120°C —
  unsuitable for high-heating environments.
- **Kevlar** (para-aramid): 5× stronger than nylon by weight, heat-resistant to 400°C. Used for
  riser lines and high-load canopies. Apollo's drogue chutes used Kevlar.
- **Zylon** (PBO): 1.5× stronger than Kevlar, used for the MSL parachute suspension lines where
  minimum mass was critical.

## Retropropulsion

The [retropropulsion](./edl.retropropulsion.md) process uses rocket engines firing opposite to
the velocity vector to decelerate the vehicle. Retropropulsion is the only EDL technique that
works in vacuum (no atmosphere to parachute into) and is essential for high-mass landings where
parachutes would be impractically large.

### Falcon 9 Booster Recovery

The Falcon 9 first-stage recovery is the first commercially operational retropropulsive
landing system. The sequence:

1. **Boost-back burn**: After stage separation (~70 km altitude, ~2,400 m/s velocity), three
   Merlin engines reignite to cancel the downrange velocity and push the stage back toward the
   landing zone. The stage performs a flip manoeuvre using cold-gas nitrogen thrusters to
   orient engines-first.
2. **Entry burn**: At ~40 km altitude, descending at ~1,500 m/s, three engines reignite for
   ~20 seconds. This "entry burn" dissipates most of the kinetic energy and creates a
   supersonic exhaust plume that acts as a heat shield — the engine exhaust deflects the
   bow shock and dramatically reduces heating on the stage's aft end.
3. **Landing burn**: At ~4 km altitude, descending at ~300 m/s, a single central engine
   (the "Octaweb" centre engine) reignites for the final deceleration. The guidance system
   commands a variable-thrust "hoverslam" — throttling the engine to reach exactly zero
   velocity at zero altitude. Grid fins (titanium lattice control surfaces deployed at the
   top of the stage) provide aerodynamic steering during descent to refine the trajectory to
   the landing pad or droneship.

The landing burn achieves sub-metre accuracy via closed-loop GPS-aided inertial guidance.
The stage touches down on four deployable carbon-fibre legs at 1-2 m/s vertical velocity.

### Supersonic Retropropulsion: Starship

SpaceX's Starship extends retropropulsion to the full vehicle — both the Super Heavy booster
and the Starship upper stage are recovered propulsively. Starship's EDL profile is unique: the
vehicle enters **belly-first** (horizontal attitude) to maximise aerodynamic drag, using four
actuated body flaps to control pitch and roll during the hypersonic and supersonic regime. At
approximately 1-2 km altitude, the vehicle performs a **belly-flip manoeuvre** — rotating from
horizontal to vertical in ~20 seconds using differential engine ignition and RCS thrusters.
The Raptor engines then ignite for the landing burn, touching down vertically.

Supersonic retropropulsion (firing engines into a supersonic freestream) was previously
considered infeasible due to plume-shock interactions that could destabilise the vehicle.
SpaceX's systematic test campaign (starting with the "Grasshopper" test vehicle in 2012 and
progressing through Falcon 9 booster recoveries) demonstrated that the plume creates a stable
aerodynamic wake rather than destabilising the vehicle, opening a new regime of EDL for heavy
vehicles on Earth and Mars.

## Precision Landing

The [precision landing](./edl.precision-landing.md) process provides the navigation accuracy
required to hit a small landing zone — a recovery pad, a droneship, or a pre-surveyed safe site
on another planet. Three navigation modes are combined:

**GPS-aided inertial**: For terrestrial landings, a GPS receiver on the descending stage
provides position updates to the IMU at 10-20 Hz. Falcon 9 uses this to achieve sub-metre
landing accuracy on the droneship. GPS is unavailable during the hypersonic plasma-blackout
phase (ionised gas around the vehicle blocks radio signals) but recovers below ~40 km altitude.

**Terrain-Relative Navigation (TRN)**: For landings on Mars or the Moon (no GPS), TRN matches
descent-camera imagery to a pre-loaded orbital map to determine position. The Mars 2020 Perseverance
rover used TRN to achieve 5-10 m landing accuracy (versus 10+ km for Viking and 3-4 km for MSL).
TRN runs the camera at 5-10 Hz during the final 1-2 km of descent, correlating features against
a map generated from the HiRISE camera on the Mars Reconnaissance Orbiter.

**Hazard avoidance**: Even with accurate navigation, the landing site may contain boulders,
craters, or slopes. Hazard-detection algorithms analyse descent imagery in real-time to identify
safe landing spots within a target zone, commanding divert manoeuvres to the safest location.
Perseverance's TRN + LVS (Lander Vision System) could detect hazards down to 50 cm and divert
to avoid them during the powered descent.

**Doppler radar altimeter**: For terminal altitude and velocity, a Ka-band or X-band radar
altimeter provides direct altitude measurement independent of inertial drift. Used on all
crewed lunar landers, Falcon 9, and Mars landers.

## Integration Points

| Stage | Contribution |
|-------|-------------|
| [Metals](../metals/index.md) | Heat shield backup structure, titanium grid fins, steel landing legs |
| [Ceramics](../ceramics/index.md) | PICA substrate, silica tiles, phenolic ablator fillers |
| [Polymers](../polymers/index.md) | Nylon/Kevlar/Zylon parachute fabric, phenolic resin binders |
| [Liquid Propulsion](../launch-vehicles/index.md) | Raptor/Merlin engines for retropropulsive landing burns |

## See Also

- [Vehicle Architecture](./vehicle-architecture.md) — launch vehicle design and staging
- [Heat Shield Design](./edl.heat-shield-design.md) — PICA, PICA-X, Shuttle tiles
- [Parachute Systems](./edl.parachute-systems.md) — DGB, ringsail, supersonic canopies
- [Retropropulsion](./edl.retropropulsion.md) — Falcon 9 and Starship landing burns
- [Precision Landing](./edl.precision-landing.md) — GPS, TRN, hazard avoidance
- [Composites](../polymers/composites.md) — parachute risers, heat shield substrates
- [Ceramics](../ceramics/index.md) — ablative and reusable TPS materials

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
