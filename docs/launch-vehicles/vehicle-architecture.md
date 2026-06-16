# Vehicle Architecture

> **Node ID**: launch-vehicles.vehicle-architecture
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`metals.aluminum`](../metals/aluminum.md),
> [`polymers.composites`](../polymers/composites.md), `electronics`,
> `computing`, `launch-vehicles.liquid-propulsion`, `launch-vehicles.solid-propulsion`
> **Enables**: Orbital payload delivery, interplanetary transfer vehicles
> **Timeline**: Years 30-200+
> **Outputs**: launch_vehicles, orbital_delivery, payload_fairings
> **Critical**: No — advanced capability requiring mature metallurgy, precision machining,
> chemical energetics, and electronics before orbital flight is achievable.

A launch vehicle is a structure that carries propellant, burns it through engines to generate
thrust, and discards empty mass (stages) so that the remaining vehicle achieves orbital velocity.
The entire discipline is governed by one equation: the **Tsiolkovsky rocket equation**, which
relates a vehicle's mass ratio to the velocity change (delta-v) it can produce.

## The Rocket Equation

The fundamental relationship is:

**Δv = Isp × g₀ × ln(m₀ / m_f)**

Where Δv is the achievable velocity change (m/s), Isp is the engine specific impulse (seconds),
g₀ is standard gravity (9.81 m/s²), ln is the natural logarithm, m₀ is the initial (gross) mass,
and m_f is the final (dry) mass after propellant is consumed. The ratio m₀/m_f is the **mass
ratio**. For orbital flight the required delta-v to Low Earth Orbit (LEO) is approximately
**9.4 km/s** — comprising the orbital velocity (~7.8 km/s) plus gravity losses (~1.3-1.8 km/s,
the cost of thrusting upward against gravity while accelerating) and drag losses (~0.1-0.3 km/s,
the cost of pushing through the atmosphere).

This 9.4 km/s budget must be delivered by the vehicle's propellant. The fraction of the vehicle
that is propellant — the **propellant mass fraction** — must be 0.85-0.92 for a single-stage
orbital vehicle. That means only 8-15% of the vehicle's liftoff mass is structure, engines,
avionics, and payload combined. Achieving such extreme mass fractions is why staging is
near-universal: each stage discards its empty tanks and engines, so later stages do not waste
energy accelerating dead hardware.

## Staging

**Serial staging** (the standard configuration) stacks stages vertically: the first (booster)
stage ignites at liftoff, burns to depletion, then separates and falls away; the second
(upper) stage ignites and continues to orbit. The [staging design](./vehicle-architecture.staging-design.md)
process determines how the delta-v budget is partitioned. A typical two-stage vehicle assigns
roughly 3.5-4.0 km/s to the first stage and 4.5-5.5 km/s to the upper stage, after accounting
for losses — though the optimum split depends on each stage's Isp and mass fraction.

**Parallel staging** (used by Falcon Heavy, SLS, Ariane 5, Space Shuttle) straps booster
cores alongside a central core that ignites simultaneously. The boosters provide high thrust
at liftoff and are jettisoned early; the central core continues burning with a full propellant
load, effectively acting as a serial second stage. This "crossfeed" architecture maximises
payload for heavy-lift vehicles.

**Stage separation systems** must cleanly disconnect the spent stage without damaging the
remaining vehicle. Three mechanisms are common:

- **Spring thrusters**: compression springs in the interstage push the stages apart with a
  calibrated impulse (typically 2-5 kN for several milliseconds). Simple, reliable, and
  flight-proven on Atlas, Delta, and Falcon 9.
- **Pneumatic pushers**: compressed-gas pistons provide higher separation impulse than springs
  and are used on larger vehicles. Cold-gas thrusters on the spent stage add a small retrograde
  impulse to ensure clean separation.
- **Solid separation motors**: small solid rocket motors mounted on the spent stage fire in the
  retrograde direction to pull the stage away. Used on Titan, Space Shuttle SRB separation, and
  Ariane 5 boosters.

The **interstage** is the cylindrical structure connecting stages. It must transmit the full
thrust load of the upper stage's engines through to the booster during first-stage burn, then
release cleanly at separation. Interstages are typically aluminium-lithium semi-monocoque
cylinders with separation joints that use explosive bolts or pneumatic release latches.

## Vehicle Comparison

The following table compares representative orbital launch vehicles across a range of payload
classes and architectures:

| Vehicle | Height | Mass | Payload (LEO) | Stages | Propellant |
|---------|--------|------|---------------|--------|------------|
| Falcon 9 (Block 5) | 70 m | 549 t | 22.8 t | 2 | LOX/RP-1 |
| Starship (Super Heavy + Ship) | 120 m | 5,000 t | 150 t+ | 2 | LOX/LCH4 |
| SLS Block 1 | 98 m | 2,698 t | 95 t | 2 + 2 SRB | LOX/LH2 |
| Electron | 18 m | 13 t | 0.3 t | 2 | LOX/RP-1 |

**Falcon 9** demonstrates the value of a reusable first stage. Its nine Merlin engines burn
kerosene (RP-1) and liquid oxygen. The first stage performs a boost-back burn, an entry burn,
and a landing burn to return to a droneship or landing pad. The 22.8-tonne payload to LEO drops
to roughly 9-10 tonnes in reusable mode due to the propellant reserved for recovery.

**Starship** is a fully reusable two-stage system using liquid oxygen and liquid methane
(LCH4). Methane was chosen for its clean-burning properties (minimal coking, enabling engine
reuse), high performance (Isp ~380 s in vacuum for the Raptor engine), and the feasibility of
in-situ production on Mars via the Sabatier reaction. The 150-tonne payload target in fully
reusable mode would make it the highest-capacity launch vehicle ever flown.

**SLS Block 1** uses legacy Space Shuttle hardware: four RS-25 hydrogen engines on the core
stage and two five-segment solid rocket boosters. The hydrogen-fuelled core stage (LOX/LH2)
offers high Isp (~452 s vacuum) but low density fuel means large tankage. The two solid rocket
boosters provide 71% of liftoff thrust.

**Electron** is a smallsat launcher demonstrating that even 13-tonne vehicles can reach orbit
with electric-pump-fed engines (the Rutherford engine uses battery-powered electric motors
instead of gas generators to drive turbopumps). Its 300 kg payload serves the dedicated
smallsat market.

## Structural Design

The primary structural challenge is the **propellant tank**. For pressure-fed and pump-fed
vehicles alike, the tank walls serve as both propellant container and the vehicle's primary
load-bearing airframe. This dual function is called a **balloon tank** or **pressure-stabilised**
structure (Atlas used this — it could not stand unsupported when unpressurised).

The dominant tank material is **Aluminium-Lithium alloy 2195** (Al-Li 2195), developed for the
Space Shuttle Super Lightweight Tank. Lithium addition (1.0-1.3% by weight) reduces density to
**2.70 g/cm³** — approximately 5% lighter than Al 2219 (2.84 g/cm³) — while increasing stiffness
and yield strength. Every kilogram saved in tank mass translates directly to additional payload.

Tank wall patterns are machined to remove every gram of unnecessary metal:

- **Isogrid**: triangular grid pattern milled into the tank wall. The triangular cell structure
  provides near-isotropic stiffness (equal in all directions) with minimal weight. Machined on
  large multi-axis CNC mills from thick plate, then rolled and welded into cylinders. Used on
  Delta IV, SLS, and many spacecraft.
- **Orthogrid**: rectangular grid pattern, slightly less mass-efficient than isogrid for uniform
  loads but easier to manufacture and better for directional load paths. Used on Falcon 9 tanks
  and the Space Shuttle External Tank.

The [structural design](./vehicle-architecture.structural-design.md) process covers tank
geometry, the interstage cylinders, and the thrust structure — the conical or cruciform frame
that distributes engine thrust uniformly into the tank's aft dome. Thrust structures see the
highest loads in the vehicle (Falcon 9's nine Merlin engines produce 7,607 kN at liftoff,
transmitted through a structure weighing under 2 tonnes).

Welding is the critical manufacturing process for tanks. **Friction stir welding (FSW)** is the
preferred method for longitudinal and circumferential tank seams: a rotating pin tool plastically
deforms and stirs the metal across the joint line, producing a solid-state bond with no melt,
no porosity, and minimal distortion. FSW joints on Al-Li 2195 achieve 85-90% of parent-metal
strength, versus 60-70% for conventional TIG welding.

## Payload Fairing

The **payload fairing (PLF)** is the nose shroud that protects the payload from atmospheric
heating, acoustic vibration, and aerodynamic loads during ascent. It is jettisoned once the
vehicle is above the sensible atmosphere — typically at **~110 km altitude**, where aerodynamic
heating and dynamic pressure have dropped to negligible levels. See
[payload fairing design](./vehicle-architecture.payload-fairing.md) for details.

Fairing design must balance four requirements:

1. **Acoustic protection**: The launch pad acoustic environment (from engine exhaust reflecting
   off the flame trench) reaches 140-145 dB. An acoustic blanket of porous foam (typically 25-50
   mm thick open-cell polyimide foam) lines the fairing interior, attenuating acoustic energy by
   10-15 dB at the payload plane. Without this blanket, sensitive optics and solar panels would
   be damaged by acoustic vibration during the first 10-15 seconds of flight.

2. **Thermal protection**: The fairing exterior sees aerodynamic heating up to 150-200°C during
   Max-Q (maximum dynamic pressure, typically 30-50 kPa at T+60-90 seconds). Cork-based
   ablative coatings (0.5-2.0 mm of cork particles in a silicone binder) or ablative paint
   protect the composite shell. The interior must stay below 40-60°C to protect payload
   thermal limits — the acoustic foam also serves as thermal insulation.

3. **Structural integrity**: The fairing must withstand aerodynamic compression, bending, and
   the lateral loads of vehicle manoeuvres. It is a composite shell (carbon-fibre-reinforced
   polymer or aluminium honeycomb sandwich) sized to the payload envelope. Standard PLF
   diameters: 4.6 m (Ariane 5), 5.2 m (Falcon 9, Atlas V), 8.4 m (SLS).

4. **Reliable jettison**: At the jettison altitude, the fairing splits longitudinally into two
   halves and pivots away on hinges. The separation is initiated by explosive bolts or
   pneumatic latches that release the joint; spring thrusters or gas pistons push the halves
   clear. A failed jettison (fairing remains attached) destroys the vehicle: the extra mass and
   drag prevent orbital insertion. Fairing jettison has thus been a critical event on every
   orbital flight since Sputnik.

**Fairing recovery and reuse**: SpaceX has demonstrated catching or recovering Falcon 9 fairing
halves from the ocean, refurbishing them, and reflying. The fairing costs approximately
$6 million per pair — roughly 10% of the vehicle's marginal cost — so recovery and reuse
materially reduces launch price. Refurbishment replaces the acoustic blanket and thermal
coating and inspects the composite shell for salt-water and impact damage.

## Guidance, Navigation, and Control

The [GNC integration](./vehicle-architecture.gvnc-integration.md) process provides the brains
of the vehicle. Without closed-loop guidance, a rocket is an unguided firework — the engines
must be steered precisely along the planned trajectory to reach the target orbit.

**Inertial Measurement Unit (IMU)**: The IMU is the heart of the navigation system. Modern
vehicles use strapdown IMUs with ring-laser gyroscopes (RLG) or fibre-optic gyroscopes (FOG)
that measure angular rate with drift rates below 0.001°/hour, plus quartz or silicon MEMS
accelerometers measuring linear acceleration to micro-g precision. The IMU integrates
acceleration to get velocity and position — a process called **dead reckoning**. Over a
10-minute ascent, position accuracy degrades to tens of metres without external correction.

**GPS/GNSS update**: A GPS receiver on the upper stage provides periodic position and velocity
updates that correct the IMU's accumulated drift. This dramatically improves orbital insertion
accuracy — from kilometres (IMU-only) to tens of metres (GPS-aided). GPS is not available above
the GPS constellation altitude (~20,200 km), so GEO and interplanetary missions rely on IMU and
star trackers.

**Star tracker**: An optical camera that identifies star patterns and computes the vehicle's
attitude to arcsecond precision (1 arcsecond ≈ 5 microradians). Star trackers provide an
absolute attitude reference independent of IMU drift. Most vehicles carry one or two star
trackers for terminal guidance and on-orbit operations.

**Flight software**: The guidance computer runs a real-time operating system executing the
guidance law — typically a **powered explicit guidance (PEG)** algorithm that continuously
computes the thrust direction needed to reach the target orbit, accounting for the vehicle's
current state, remaining propellant, and engine performance. The control loop commands
**thrust vector control (TVC)** — gimballed engine nozzles that deflect thrust by ±5-10° to
steer the vehicle — at update rates of 20-100 Hz. The entire flight software for a modern
launch vehicle runs to 100,000-500,000 lines of code, rigorously tested in hardware-in-the-loop
simulators before flight.

## Mass Budget

A representative mass budget for a two-stage orbital vehicle (Falcon 9-class) illustrates how
the mass fractions compound:

| Component | Mass (t) | Fraction of liftoff mass |
|-----------|----------|--------------------------|
| First-stage propellant (LOX + RP-1) | 411 | 74.9% |
| First-stage dry mass (tanks, engines, avionics) | 27 | 4.9% |
| Second-stage propellant | 92 | 16.8% |
| Second-stage dry mass | 4.5 | 0.8% |
| Payload fairing | 1.9 | 0.3% |
| **Payload to LEO** | **22.8** | **4.2%** |
| **Total liftoff mass** | **549** | **100%** |

The propellant mass fraction across both stages is (411 + 92) / 549 = **91.6%** — squarely in
the 0.85-0.92 range typical of orbital vehicles. The payload fraction of 4.2% means that of
every 100 tonnes on the pad, only 4.2 tonnes reach orbit. This brutal mass discipline is why
every gram of structural mass is fought over and why reuse (recovering and reflying the 27-tonne
first stage) is economically transformative.

## Integration Points

| Stage | Contribution |
|-------|-------------|
| [Aluminum](../metals/aluminum.md) | Al-Li 2195 tanks, isogrid panels, thrust structures |
| [Composites](../polymers/composites.md) | Carbon-fibre payload fairings, interstage cylinders |
| [Electronics](../electronics/index.md) | IMU, flight computers, TVC drivers, telemetry |
| [Computing](../computing/index.md) | Flight software, simulation, guidance algorithms |
| Liquid Propulsion | Merlin/Raptor/Vulcain engines, turbopumps, injectors |
| Solid Propulsion | Strap-on boosters, SRB cases, propellant grain |

## See Also

- [Entry, Descent & Landing](./edl.md) — recovery of stages and payloads
- [Staging Design](./vehicle-architecture.staging-design.md) — separation systems and interstages
- [Payload Fairing](./vehicle-architecture.payload-fairing.md) — acoustic and jettison systems
- [Structural Design](./vehicle-architecture.structural-design.md) — Al-Li tanks and isogrid
- [GNC Integration](./vehicle-architecture.gvnc-integration.md) — IMU, GPS, flight software
- [Aviation](../aerospace/aviation.md) — atmospheric flight prerequisite
- [Aluminum](../metals/aluminum.md) — primary structural alloy
- [Composites](../polymers/composites.md) — fairing and interstage material

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
