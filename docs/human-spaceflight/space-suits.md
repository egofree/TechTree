# Space Suits

> **Node ID**: `human-spaceflight.space-suits`
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: [`polymers`](../polymers/index.md),
> [`textiles`](../textiles/index.md), [`metals`](../metals/index.md),
> [`glass`](../glass/index.md)
> **Enables**: Extravehicular activity, lunar surface operations, pressurised rover crews
> **Timeline**: Years 50-200+
> **Outputs**: pressure_garments, portable_life_support_systems, thermal_control_garments, eva_suits
> **Critical**: No — advanced life-support garment requiring mature polymers, textiles, and
> precision life-support hardware. A space suit is a human-shaped, self-contained spacecraft:
> it holds pressure against vacuum, rejects metabolic heat, scrubs carbon dioxide, shields the
> wearer from micrometeoroids and radiation, and still has to bend at every joint.

A space suit is the smallest crewed spacecraft ever built. Where a capsule surrounds its crew
with a pressure shell fed by tanked atmosphere, a suit wraps a single human in a multilayer
pressure garment and a backpack life support system that must keep that human alive, mobile,
and productive for six to eight hours of hard manual labour in vacuum. Every suit is a
compromise between **pressure retention** (which wants a rigid, fully inflated balloon),
**mobility** (which wants a limp, unresisting fabric), **thermal control** (which must dump
100-300 W of metabolic heat into a vacuum that conducts no heat away), and **mass** (because
every gram on a planetary surface is a gram the wearer must carry).

## Operating Pressure and the Pure-O2 Trade

The single most consequential design choice is the suit's internal pressure, because it
determines both the load on the pressure bladder and the force the wearer must overcome to
bend every joint.

| Suit | Pressure | Atmosphere | Notes |
|------|----------|------------|-------|
| Apollo A7LB (lunar) | 3.8 psi (26 kPa) | 100% O2 | Low pressure → low joint torque, easy bending. Fire risk. |
| Shuttle / ISS EMU | 4.3 psi (29.6 kPa) | 100% O2 | Standard EVA pressure. Requires prebreath. |
| Orlan-M (Russian) | 5.8 psi (40 kPa) | 100% O2 | Higher pressure, shorter prebreath, stiffer joints. |
| xEMU (Artemis) | 8.2 psi / 4.3 psi | 100% O2 | Dual pressure: high for campout prebreath, low for EVA mobility. |
| SpaceX EVA suit | ~5.5 psi (38 kPa) | 100% O2 | Lighter IVA/EVA hybrid, limited autonomous PLSS. |

A pure-oxygen atmosphere at 4.3 psi carries the same partial pressure of oxygen as sea-level
air (3.08 psi O2), so the wearer's blood stays fully oxygenated — but everything inside the
suit, including human skin oils, becomes a fire hazard in pure O2. The fire risk is why suits
operate at the **lowest pressure** compatible with sustained consciousness: lower pressure
means softer fabric, lower joint torque, and less effort per movement. The price is the
**prebreath protocol** (see below): the wearer must purge dissolved nitrogen from the blood
before dropping to 4.3 psi pure O2, or risk decompression sickness.

## Suit Types: IVA, EVA, and Planetary

- **IVA suit** (intra-vehicular): a pressure garment worn inside a capsule as a backup to
  cabin pressurisation. Light, slim, minimum joint reinforcement. The SpaceX Crew Dragon
  suit and the Soyuz Sokol are IVA suits — they are not designed for spacewalks, only for
  surviving a cabin depressurisation or high-g reentry.
- **EVA suit** (extra-vehicular): the full autonomous pressure garment plus PLSS backpack
  worn for spacewalks. The EMU and Orlan are EVA suits. They are heavy (110-130 kg),
  stiff, and self-contained for 6-8 hours.
- **Planetary suit**: an EVA suit optimised for walking on a surface. Requires leg and hip
  mobility, dust-tolerant bearings, and a suitport or airlock for repeated donning/doffing.
  The Apollo A7LB and the Artemis xEMU are planetary suits.

## The EMU (Extravehicular Mobility Unit)

The NASA/ISS EMU is the canonical EVA suit. First flown in 1981, it has been the workhorse
of Shuttle and ISS spacewalks for over four decades.

| Parameter | EMU value |
|-----------|-----------|
| Mass (suit + PLSS) | 127 kg |
| Operating pressure | 4.3 psi (29.6 kPa) pure O2 |
| EVA duration | 8.4 hr nominal (O2 limited) |
| Metabolic heat removal | 100-300 W (peak 500 W short) |
| Primary O2 tank | 0.55 kg @ 20.7 MPa |
| CO2 scrubber | LiOH cartridges (replaceable mid-EVA) |
| Battery | 11.6 Ah silver-zinc, replaceable |
| Water sublimator heat rejection | up to 730 W peak |
| Hard upper torso (HUT) | fibreglass/steel shell with built-in PLSS |
| Joints | ball bearings at shoulder/wrist/ankle, fabric convolutes at elbow/knee |

The EMU is a **semi-rigid** suit: the Hard Upper Torso (HUT) is a fibreglass and stainless
steel shell that integrates the helmet, arms, PLSS backpack, and life-support plumbing into
one rigid core. The arms, gloves, and lower torso assembly (LTA, the legs) are soft fabric
and detach separately. Astronauts don the suit by climbing in through the waist — first the
LTA, then inserting arms and head into the HUT, then sealing the waist ring.

## The Apollo A7LB Moon Suit

The A7LB was built for lunar surface operations: walking, bending, kneeling to collect
samples, and riding the Lunar Rover. It is the only suit to have walked on another world.

| Parameter | A7LB value |
|-----------|------------|
| Mass (suit + PLSS) | 28.5 kg suit / 54 kg PLSS backpack |
| Operating pressure | 3.8 psi (26 kPa) pure O2 |
| EVA duration | 7-8 hr (with PLSS consumables) |
| Thermal range | -150°C lunar night to +120°C lunar day |
| Outer fabric | Teflon-coated Beta fibre glass cloth (original) |
| Joint type | molded rubber convolutes, cable restraint |

The A7LB ran at a lower pressure (3.8 psi) than the EMU (4.3 psi), accepting more
decompression-sickness risk in exchange for softer joints and easier walking under lunar 1/6
gravity. The outer layer was **Beta cloth** — woven silica glass fibre, chosen because it
does not burn in pure oxygen. Later missions added Kapton and Mylar layers for thermal
control. The PLSS backpack carried its own oxygen, LiOH scrubber, water-cooling loop, and
radio.

## The xEMU (Artemis Programme)

The Exploration EVA Suit (xEMU) is NASA's next-generation planetary suit for the Artemis
lunar return and eventual Mars missions. The principal advance is **rear-entry**: the
astronaut climbs in through a hatch in the back of the HUT, then closes the hatch against the
suitport on a rover or habitat. This means the suit stays outside, the dust stays outside,
and the astronaut steps straight from the rover into the suit.

The xEMU introduces a **dual-pressure** architecture: 8.2 psi for "campout" prebreath
(breathing pure O2 overnight at moderate pressure to denitrogenate), then dropping to 4.3 psi
for the EVA itself. Modular bearings at hip, knee, and ankle improve walking gait. The PLSS
is rebuilt around a regenerable amine CO2 bed (no more LiOH cartridge swaps) and a larger
water sublimator rated for 8+ hours of lunar labour.

## The SpaceX EVA Suit

The SpaceX EVA suit, debuted on the Polaris Dawn mission in 2024, is a lighter, more
agile garment designed for short-duration EVAs from the Crew Dragon. It uses a 3D-printed
helelmet, touchscreen-compatible gloves, and a single umbilical to the spacecraft that
supplies oxygen, power, and cooling — the suit itself does not yet carry a full autonomous
PLSS backpack. At roughly 20 kg of garment plus umbilical, it trades duration for mobility
and manufacturability. It is the first new Western EVA suit architecture in 40 years.

## Pressure Garment Layer Breakdown

A modern EVA suit is built up in layers, each with a specific function. From the skin outward:

| Layer | Name | Material | Function |
|-------|------|----------|----------|
| 1 | Liquid Cooling & Ventilation Garment (LCVG) | Spandex mesh + 300 m PVC tubing | Removes metabolic heat, draws humid gas to PLSS |
| 2 | Bladder | urethane-coated nylon | Gas-retaining pressure membrane |
| 3 | Restraint / Pressure garment | Dacron webbing, linknet | Constrains bladder to human shape under pressure |
| 4 | Thermal Micrometeoroid Garment (TMG) inner | aluminised Mylar (multi-layer insulation) | Reflects radiative heat, 10-14 layers |
| 5 | TMG spacer | Dacron / Beta cloth scrim | Separates MLI layers, prevents heat conduction |
| 6 | TMG outer (cover) | Ortho-Fabric (Nomex/Kevlar/Teflon) | Micrometeoroid impact, abrasion, UV resistance |

**Layer 1 — LCVG**: The Liquid Cooling and Ventilation Garment is a full-body spandex
undergarment laced with roughly 300 metres of 1.6 mm PVC capillary tubing. Chilled water
(ideally 10-18°C) circulates at 1.5-2.5 L/min, directly absorbing body heat at the skin.
The LCVG removes **100-300 W of metabolic heat** — the heat produced by a human doing
moderate to hard work. Without it, the suit's insulation would trap that heat and the wearer
would overheat within minutes regardless of how cold the outside was. Ventilation ducting
along the limbs draws exhaled, humid oxygen back toward the PLSS for CO2 scrubbing and
dehumidification.

**Layer 2 — Bladder**: The gas-retaining membrane. A 0.25-0.50 mm cast urethane film on a
nylon ripstop substrate holds the 4.3 psi pure oxygen atmosphere against the vacuum. Urethane
is chosen for low gas permeability, flexibility at temperature extremes, and crack resistance
over thousands of pressure cycles.

**Layer 3 — Restraint**: The bladder would happily inflate into a rigid, spherical balloon;
the restraint layer forces it back into a human shape. The restraint is a network of Dacron
and steel cables (linknet) that distribute the pressure load along the limbs and torso,
transferring it to the hard torso rings. At every joint, the restraint terminates in a
bearing or convolute that allows bending.

**Layer 4 — TMG (Thermal Micrometeoroid Garment)**: The outer armour. 10-14 layers of
aluminised Mylar separated by Dacron scrim form a multi-layer insulation blanket that
reflects away the +120°C sunlit lunar surface and traps the -150°C shade. The outermost
cover fabric (Ortho-Fabric: a blend of Nomex, Kevlar, and Teflon) absorbs the kinetic
energy of micrometeoroid impacts at 10-20 km/s, spreading the hypervelocity crater across
the fabric before it reaches the bladder.

## Portable Life Support System (PLSS)

The PLSS backpack is the suit's lifeboat. It carries every consumable needed to keep a human
alive for the full EVA: oxygen, CO2 scrubber, humidity and thermal control, power, and
communications.

| PLSS Component | Function | Capacity / Spec |
|----------------|----------|-----------------|
| Primary O2 tank | Breathing gas, suit pressurisation | 0.55-1.0 kg @ 20.7 MPa |
| Contingency O2 tank | Emergency backup (30 min) | 0.5 kg @ 41.4 MPa |
| LiOH canister | CO2 scrubber (reaction: 2LiOH + CO2 → Li2CO3 + H2O) | Keeps pCO2 < 0.5 kPa for 8 hr |
| Sublimator | Heat rejection (water ice sublimes to vacuum) | 730 W peak (EMU) |
| Condensing heat exchanger | Dehumidifies ventilation loop | Removes 0.2-0.5 kg H2O per EVA |
| Contaminant control cartridge | Activated charcoal + catalytic oxidiser | Removes odours, trace organics |
| Ventilation fan | Circulates O2 through suit and scrubber | 0.17 m3/min |
| Battery | Power for fan, pumps, radios, displays | 11.6 Ah silver-zinc (EMU) |
| Radio / telemetry | UHF voice, suit telemetry to vehicle/ground | Redundant S-band |
| Suit pressure control | Regulates O2 feed, vent valve | 4.3 psi ±0.1 |

The PLSS **oxygen loop is open-loop for O2**: pure oxygen is metered from the primary tank,
breathed once, scrubbed of CO2, dehumidified, and recirculated — but leakage and metabolic
consumption require continuous make-up from the tank. A single tank lasts roughly 8.4 hours
at nominal metabolic load. The **thermal loop is closed**: water circulates through the
LCVG, picks up body heat, runs through the sublimator (where a controlled flow of feedwater
freezes to ice and sublimes directly to vacuum, carrying the heat away), and returns chilled
to the garment.

## Prebreath Protocol (Decompression Sickness Prevention)

The ISS cabin is pressurised to 101 kPa (14.7 psi) with a 78/22 N2/O2 mix. Dropping directly
to the EMU's 4.3 psi pure O2 would release dissolved nitrogen from the blood as bubbles —
decompression sickness, "the bends." The protocol purges that nitrogen first:

1. **Campout** (overnight): the astronaut sleeps in the airlock at 70 kPa with elevated O2.
   Over 8-12 hours, dissolved N2 equilibrates to the lower pressure.
2. **Prebreath** (morning): 60-75 minutes of breathing 100% O2 via mask while exercising on
   a stationary bike (to accelerate N2 washout from muscle tissue).
3. **In-suit prebreath** (final): 45-50 minutes in the sealed suit on 100% O2 before
   depressurising the airlock.

Total protocol: 4-6 hours from campout to airlock vent. The xEMU's dual-pressure mode
(8.2 psi campout, 4.3 psi EVA) reduces this to under 2 hours.

## Mobility Joints and Bearing Architecture

A pressurised suit resists every bend. Bending a fabric convolute (a bellows-like cylindrical
section) compresses one side and expands the other, doing work against the internal pressure.
The joint torque scales with pressure, diameter, and the stiffness of the restraint. Three
joint technologies dominate:

- **Convolutes**: molded rubber or urethane bellows. Simple, lightweight, but high torque
  (1-3 Nm at the elbow). Used on Apollo A7LB arms and knees.
- **Bearings**: precision ball or roller bearings at shoulder, wrist, waist, and ankle. Allow
  rotation with negligible torque. The EMU uses 7 bearings per suit; each is a sealed,
  titanium-race, vacuum-lubricated unit rated for thousands of cycles.
- **Conical / gimbal joints**: two nested cones that slide past each other, allowing
  compound bending. Used at the hip in the xEMU for walking gait.

A modern EVA suit combines all three: bearings for rotation, convolutes for flexion/extension,
and cable-driven linknets to keep the joint centred under pressure.

## Suitport and Rear-Entry Architecture

The xEMU and next-generation planetary suits use a **suitport**: the suit mounts to the
outside of a rover or habitat, with a rear hatch that opens directly into the cabin. The
astronaut climbs into the suit from inside, seals the hatch, and detaches — the suit's dust
and the suit's interior never enter the cabin. This eliminates the airlock cycle (30-60 min
of pumping down a full cabin volume) and dramatically reduces lunar dust ingress, which on
Apollo caused lung irritation, bearing failures, and seal degradation. Rear-entry also moves
the PLSS backpack into a fixed mounting position on the suitport, simplifying donning.

## Gloves — the Hardest Component

Suit gloves are the most revised, most problematic, and most personal component. A glove must
retain pressure, survive thermal extremes, resist abrasion, protect against micrometeoroids
— and still let the astronaut manipulate tools, turn bolts, and feel what they touch. The
EMU glove is a custom-moulded pressure bladder inside a multi-finger restraint cage with
bearings at every knuckle, a wrist bearing (to rotate the hand without twisting the arm),
and fingertip heaters. Joint torque at the fingers is 2-5 Nm per digit: small individually,
but over a 6-hour EVA it produces crippling fatigue. Every astronaut is fitted with custom
gloves cast from hand moulds; an ill-fitting glove causes nail-bed injury (onycholysis)
within a single EVA.

## Prerequisites

- [Polymers](../polymers/index.md) — urethane bladders, O-ring seals, nylon ripstop
- [Textiles](../textiles/index.md) — restraint webbing, multi-layer insulation, Beta cloth
- [Metals](../metals/index.md) — aluminum PLSS tanks, titanium bearing housings
- [Glass](../glass/index.md) — polycarbonate helmet shell, gold-film sun visor

## Sub-Processes

- [Pressure Garment Design](./space-suits.pressure-garment.md) — bladder, restraint, mobility joints
- [Portable Life Support System](./space-suits.plss-design.md) — backpack oxygen, CO2, thermal loop
- [Thermal Control Suit](./space-suits.thermal-control-suit.md) — LCVG and multi-layer insulation

## See Also

- [Crewed Spacecraft](./crewed-spacecraft.md) — parent capsule and cabin
- [Launch Vehicles EDL](../launch-vehicles/edl.md) — reentry heritage shared with suit thermal
  protection design
- [Gas Handling](../gas-handling/index.md) — oxygen and clean-gas system heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Human Spaceflight](./index.md) • [All Domains](../index.md)*
