# Cargo Aircraft

> **Node ID**: aerospace.cargo-aircraft
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.aviation`](aviation.md), [`aerospace.jet-propulsion`](jet-propulsion.md), [`metals.aluminum`](../metals/aluminum.md)
> **Timeline**: Years 30-50+
> **Outputs**: cargo_aircraft, cargo_loading_systems
> **Critical**: No

Once civilization has mastered passenger and general aviation, the next leap is dedicated heavy-lift flight. Cargo aircraft move outsized industrial equipment, disaster relief supplies, and high-value time-critical freight over intercontinental distances that ground transport cannot match. Unlike a passenger jet converted with a cargo door, a true freighter is engineered from the keel up around payload volume, floor strength, and loading cycle efficiency. This capability covers the airframe, propulsion integration, door geometry, and weight-and-balance discipline that distinguish a freighter from a people-carryer.

The cargo aircraft capability builds directly on [Aviation](aviation.md) (airframe, flight controls, piston and turboprop foundations) and [Jet Propulsion](jet-propulsion.md) (turbofan and turbojet engines for heavy long-range aircraft). The dominant structural material remains [aluminum](../metals/aluminum.md) — specifically 2024-T3 and 7075-T6 alloys — supplemented by titanium at high-load attachment points and emerging composites for secondary structure.

## Freighter Design Philosophy

A dedicated freighter differs from a passenger aircraft in four fundamental ways:

1. **Payload density drives everything.** Passenger cabins carry 90-100 kg/m² (people + seats + bags). Cargo decks carry 500-1,500 kg/m² (machinery, dense pallets, vehicles). The floor must survive this. A passenger-to-freighter conversion that ignores floor reinforcement will buckle the cabin floor on the first heavy pallet.
2. **Loading time is money.** A freighter earns revenue only when airborne. Turnaround targets are 60-90 minutes for a 100-tonne payload, compared to 25-35 minutes for passenger boarding. Every design choice — door position, roller system, drive hardware, clearance height — serves this goal.
3. **Weight and balance shift in flight.** Passengers sit in assigned seats. Cargo is lashed but the aircraft is loaded to exploit every cubic metre. A poorly loaded freighter can exceed aft center-of-gravity limits as fuel burns off, causing catastrophic pitch instability.
4. **Outsized cargo demands oversized doors.** A mining truck, a transformer, or a satellite bus will not fit through a side cargo door. Nose-loading or tail-loading freighters swing the entire forward or rear fuselage open, permitting drive-through loading of vehicles and oversize machinery.

## High-Wing vs Low-Wing Configurations

| Parameter | High-Wing Freighter | Low-Wing Freighter |
|-----------|--------------------|--------------------|
| Typical aircraft | Lockheed C-5 Galaxy, C-130 Hercules, Airbus A400M, ATR 72F | Boeing 747F, 777F, 757-200F, MD-11F |
| Cargo floor height | 3-5 m (truck-level direct drive-on) | 4-5.5 m (requires high-loader or built-in cargo handling) |
| Ground clearance | Excellent (propeller and engine clearance) | Lower (risk of pod-strike on poorly maintained runways) |
| Landing gear | Long, fuselage-mounted (retracts into side fairings) | Shorter, wing-mounted (retracts into wing root) |
| Structural penalty | Heavier wing-to-fuselage attachment, complex gear | Lighter, conventional |
| Loading method | Drive-on / drive-off via ramp (military and rough-field) | Side door or nose door with conveyor/pallet system |

**High-wing freighters** (Lockheed C-5 Galaxy, C-130, ATR 72F regional turboprop freighters) place the cargo floor high enough that trucks and forklifts can drive directly to the door without elevated loaders. This is why military tactical transports almost universally adopt high wings — they must operate from austere fields with minimal ground equipment. The trade-off is a longer, heavier landing gear that retracts into fuselage blisters, adding drag and structural weight.

**Low-wing freighters** (Boeing 747F, 777F, 757-200F) descend from passenger aircraft families where the low wing gives a crashworthy structure under the cabin and shorter, lighter gear. Cargo loading uses elevated belt loaders, forklifts, or the aircraft's own internal power drive units (PDUs). The 747F solves the outsized-cargo problem with a nose door that swings upward, allowing 2.4 m tall pallets and vehicles to drive straight in — a feature impossible on a high-wing design derived from a passenger tube.

## Reinforced Cargo Floors

The cargo floor is the single most engineered component of a freighter. It must support concentrated point loads from pallet feet and vehicle wheels while distributing that load into the fuselage frames without permanent deformation.

**Floor beam construction:**
- Floor beams run laterally across the fuselage at 0.5-1.0 m spacing, connecting to the main fuselage frames. On a 747F, these are extruded 7075-T6 aluminum I-sections, 100-150 mm deep, machined to remove every gram of non-load-bearing metal.
- The beam flanges carry bending loads; the web carries shear. Beam depth is set by the maximum bending moment at the fuselage centre, then tapered toward the sides where loads diminish.
- Floor panels bolt or rivet to the beam top flanges. Panels are 5-12 mm aluminum alloy sheet or aluminum honeycomb sandwich (two thin aluminum skins bonded to a Nomex or aluminum hexagonal core — high stiffness at low weight).

**Floor load ratings:**
- Passenger cabin floors: rated for 365 kg/m² (7.5 lb/ft²) per FAR Part 25.
- Cargo deck floors: 732 kg/m² (cargo area, lower deck) to 1,953 kg/m² (main deck freighter, dense loads).
- Tanker / vehicle deck floors: 4,880 kg/m² or higher (reinforced for tracked and wheeled vehicles, as on the C-5 Galaxy and A400M).

**Tie-down fittings:**
- The floor is drilled with a regular grid of attachment points — typically 254 mm (10 inch) or 305 mm (12 inch) spacing — accepting cargo lashing rings rated at 10,000-22,000 lb (4,500-10,000 kg) ultimate load each.
- Fittings are forged steel or titanium inserts set into the floor beams. A pallet may be secured by 8-20 fittings, depending on weight and flight load factor assumptions.
- Mil-spec freighters (C-5, C-130, C-17) use a dual-row fitting system with 10,000 lb rings; civil freighters typically use IATA-compliant 5,000-8,000 lb rings at 508 mm spacing.

## Cargo Door Sizing and Geometry

| Aircraft | Door Type | Width × Height (m) | Notable Capability |
|----------|-----------|--------------------|--------------------|
| Boeing 747-8F | Nose door (swing-up) | 2.44 × 2.44 | Drive-in loading; tallest pallets in civil fleet |
| Boeing 777F | Side main-deck door | 3.52 × 2.71 | Wide-body side loader; largest side door |
| Boeing 757-200F | Side main-deck door | 2.21 × 1.88 | Narrow-body feeder freighter |
| Lockheed C-5 Galaxy | Nose + tail (visors) | 4.11 × 4.11 | Tanks, helicopters; full drive-through |
| Antonov An-124 | Nose + tail (swing) | 4.40 × 4.40 | Outsized cargo: turbines, rail cars, spacecraft |
| ATR 72F | Side forward door | 1.27 × 1.27 | LD3 container loading on turboprop freighter |

**Nose doors** (747F, C-5, An-124) require the flight deck to be hinged upward or relocated, creating a structural challenge at the pressure bulkhead. The 747F's hinged nose maintains the pressure shell by using a separate inner door; the outer nose swings only for cargo access. The C-5 and An-124 are unpressurised in the cargo compartment (or only partially pressurised), simplifying the nose-door seal problem.

**Side doors** are simpler structurally but limit pallet height to the door opening. The 777F's 3.52 m wide side door is the largest in civil service, accepting 2.44 m tall pallets at an angle. Side-door freighters use internal power drive units (rollers, conveyors, winches) to move pallets from the door to their locked position along the full length of the deck.

## Pallet and Container Standards

Air cargo is unitised into standard shapes so that the same pallet can move from truck to aircraft to truck without breaking down the load. Three families dominate:

**88 × 125 inch PMC pallet:**
- The universal air-cargo pallet. Dimensions: 2,242 × 3,175 mm (88 × 125 in). Built from an aluminum sheet (typically 1.5-2.0 mm 2024-T3) over a rigid aluminum frame. Net attachment points around the edge.
- Cargo is stacked on the pallet and secured with a cargo net (woven polyester or nylon webbing, 25-50 mm mesh) lashed to the pallet edge. A loaded PMC pallet weighs 300-500 kg empty + up to 4,600-5,000 kg cargo = 5,000 kg typical.
- Fits all wide-body freighters and most narrow-body freighters. The 747F main deck carries 30 PMC pallets; the 777F carries 27.

**LD3 container (AKE type):**
- The lower-deck standard for wide-body aircraft. Dimensions: 1,534 × 1,562 × 1,626 mm. Shaped to fit the curved lower-deck cross-section of a wide-body fuselage.
- Capacity: 1,500 kg typical. Loaded through the lower-deck side doors via belt conveyor. A 747F carries 14 LD3s in the lower hold; a 777F carries 10.
- LD3s are aluminium-sheet containers with hinged or canvas doors. They protect cargo from weather and simplify handling but add 70-100 kg tare weight per position.

**LD7 container (88 × 125 inch lower-deck):**
- A flat pallet container for the lower deck of wide-body aircraft. Dimensions: 2,242 × 3,175 mm — same footprint as the PMC pallet but lower height (1,626 mm) to fit the lower lobe.
- Used for bulk cargo, baggage, or small parcels. A 777F lower deck accepts 10 LD7 positions.

## Weight and Balance

A freighter's center of gravity (CG) must remain within the certified envelope throughout the entire flight — from maximum fuel and full payload at takeoff, through fuel burn-down, to landing. Cargo loading is the primary lever for controlling CG.

**CG envelope:**
- Typical wide-body freighter CG range: 16-32% mean aerodynamic chord (MAC). The forward limit is set by elevator authority (ability to raise the nose at rotation). The aft limit is set by static stability margin (too far aft and the aircraft becomes uncontrollable in pitch).
- As fuel burns from wing tanks, CG typically shifts forward by 1-3% MAC over a long flight. Loaders must place heavy pallets to compensate — a nose-heavy aircraft at landing will float and risk overrunning the runway; a tail-heavy aircraft will rotate uncontrollably on takeoff.

**Load planning:**
- Each pallet position has a defined weight limit and a known moment arm (distance from the aircraft's reference datum). The loadmaster computes the total weight and total moment, then verifies the resulting CG falls within the envelope.
- Heavy items (1,500-5,000 kg) go toward the wing root area (the strongest part of the fuselage, closest to the centre of lift). Light items go forward and aft.
- If the computed CG is out of limits, the loadmaster rearranges pallets or adds ballast (concrete blocks or sandbags in the nose or tail) — an embarrassing but sometimes necessary practice.

## Reference Freighters

| Aircraft | MTOW (t) | Payload (t) | Range (km) | Deck | Typical Use |
|----------|----------|-------------|------------|------|-------------|
| Boeing 747-8F | 448 | 137 | 8,130 | Main + lower | Intercontinental heavy freight |
| Boeing 777F | 348 | 103 | 9,070 | Main + lower | Long-range express freight |
| Boeing 757-200F | 116 | 39 | 5,800 | Main (narrow-body) | Regional / overnight freight |
| ATR 72F | 23 | 8 | 1,665 | Main (turboprop) | Short-haul feeder / LD3 |
| Lockheed C-5 Galaxy | 381 | 128 | 5,524 | Main (outsized) | Military outsized cargo |
| Antonov An-124 | 402 | 150 | 5,400 | Main (outsized) | Outsized civil / charter cargo |

The **747F** remains the benchmark for civil air cargo. Its nose door, high main-deck floor, and 137-tonne payload made it the workhorse of global air freight for 50 years. The **777F** succeeds it with twin-engine fuel economy and no nose door, trading outsized-cargo capability for lower operating cost. The **ATR 72F** illustrates the feeder freighter: a high-wing turboprop carrying LD3s on short sectors where jet speed is irrelevant. The **C-5 Galaxy** and **An-124** serve the outsized-cargo niche — transporting satellites, transformers, and military vehicles that no other aircraft can accept.

## Propulsion Integration

Freighter propulsion follows payload and range requirements:

- **Turboprop feeders** (ATR 72F, C-130): 1,800-4,600 kW per engine. High propulsive efficiency at 500-600 km/h cruise. Ideal for short sectors, austere fields, and fuel-constrained scenarios. The [jet propulsion](jet-propulsion.md) turbofan is not required.
- **High-bypass turbofan freighters** (747F, 777F, 757-200F): 250-500 kN thrust per engine. Cruise at 850-900 km/h, altitude 10-12 km. The engines are identical to their passenger-aircraft siblings — freighter and passenger variants share the same engine pool, reducing development cost.
- **Engine mount considerations:** A freighter's higher gross weight may require uprated engine variants or higher thrust settings at takeoff. The 747-8F uses GEnx-2B engines derated slightly from the passenger 747-8I to extend life under the harder duty cycle of cargo operations (more cycles, more full-thrust takeoffs).

## Manufacturing Implications

Building a freighter requires capabilities already established by passenger aviation, with additions:

- **Thicker floor extrusions** — larger 7075-T6 billets, heavier extrusion presses (5,000-10,000 tonne press force for sections up to 150 mm deep).
- **Cargo door actuation** — hydraulic or electromechanical actuators rated for 10,000-50,000 cycles. The 747F nose door uses four hydraulic cylinders; the C-5 uses an electric screw-jack system.
- **Roller and guide hardware** — thousands of precision-machined rollers, ball-transfer units, and guide rails per aircraft. These are aluminium and steel components produced on automated turning centres.
- **Interior systems wiring** — PDU power buses (28V DC or 270V DC), control panels at each door station, and intercom wiring for the loadmaster. Adds 500-1,000 kg of wiring versus a passenger aircraft.

## Integration Points

| Stage | Contribution |
|-------|-------------|
| [Aviation](aviation.md) | Airframe, flight controls, pressurisation, piston/turboprop foundation |
| [Jet Propulsion](jet-propulsion.md) | Turbofan engines for heavy long-range freighters |
| [Aluminum](../metals/aluminum.md) | 2024-T3 skin/stringers, 7075-T6 floor beams and fittings |
| [Machine Tools](../machine-tools/index.md) | Floor extrusion presses, precision rollers, door actuator machining |
| [Hydraulics](../energy/gas-turbine.md) | Cargo door, ramp, and PDU hydraulic power |
| [Electronics](../electronics/index.md) | Weight-and-balance computer, PDU control, loadmaster intercom |

## Key Deliverables

- Dedicated freighter airframe (high-wing or low-wing) with reinforced cargo floor
- Cargo door: side, nose, or tail, sized for target pallet/container height
- Internal cargo handling system: roller conveyors, power drive units, lashing fittings
- Load planning tools: weight-and-balance software, pallet position diagrams
- Ground support: high-loader forklifts, belt conveyors, pallet dollies
- Fuel supply chain: Jet A-1 kerosene for turbofan freighters (see [Aviation](aviation.md) fuel section)

## Bootstrapping Path

In a bootstrapping scenario, cargo aircraft arrive late — after passenger aviation, after jet propulsion, after the machine tool base can produce the heavy floor extrusions. The path is:

1. Establish [piston/turboprop aviation](aviation.md) with light aircraft (Years 10-30).
2. Develop [turbojet and turbofan](jet-propulsion.md) engines for heavy aircraft (Years 30-40).
3. Convert existing large airframes to freighters: add side cargo door, reinforce floor, install roller system (Years 30-40).
4. Design dedicated freighter from clean sheet: optimised for payload volume, not passenger comfort (Years 40-50+).

The first freighters in a bootstrapping economy will likely be converted passenger aircraft — a 707 or DC-8 equivalent with a side door cut into the fuselage and a reinforced floor. Only after air freight demand justifies the investment does a clean-sheet freighter (a 747F equivalent) become worthwhile.

## Cargo Door Actuation

A freighter cargo door is the largest single moving structure on the aircraft. The 747F nose door weighs over 2 tonnes; the C-5 Galaxy nose visor weighs 4 tonnes. Actuating these doors reliably under wind loads, icing, and thermal expansion requires engineered power systems.

**Hydraulic actuation** (standard on civil freighters):
- The door is driven by 1-4 hydraulic cylinders supplied by the aircraft's central hydraulic system (3,000-5,000 psi / 207-345 bar). A 747F side door uses two cylinders; the nose door uses four. Hydraulic pressure is available from engine-driven pumps when engines are running, or from an auxiliary power unit (APU) or ground cart when the engines are off.
- Latching is mechanical — hydraulic pressure moves the door to the closed position, then mechanical latch hooks engage over latch pins on the doorframe. The latches are locked by over-centre linkages that cannot back-drive from cabin pressure. A separate latch-locked sensor confirms engagement before pressurisation is permitted.

**Electromechanical actuation** (military freighters):
- The C-5 Galaxy uses electric motor-driven ball screw actuators for its nose and tail visors. Each actuator is rated at 50-100 kN thrust. Ball screws offer precise position control and hold position without hydraulic bleed-down, but are heavier than hydraulic cylinders for the same force.
- The Antonov An-124 uses a combination of hydraulic cylinders for the nose door swing and mechanical latches for the tail ramp.

**Sealing:**
- Pressurised freighter doors use inflatable silicone rubber seals (pressurised to 15-25 psi from the cabin air system) that expand to fill the gap between door and frame. Unpressurised freighters (C-5, An-124 cargo compartments) use simple compression seals — rubber gaskets crushed between door and frame by latch force.
- A failed seal on a pressurised freighter causes a pressurisation leak — cabin altitude climbs, oxygen masks may deploy, and the aircraft must descend to a safe altitude (typically 3,000 m or below).

## Structural Fatigue and Cycle Life

Freighter airframes accumulate fatigue differently from passenger aircraft. A passenger jet flies 2-6 hours per sector; a freighter may fly 1-14 hours. Cargo loading and unloading impose repeated floor deformations that passenger cabins never experience. A dedicated freighter is certificated for 30,000-45,000 equivalent flight cycles, compared to 75,000-100,000 for a short-haul passenger aircraft — because each freighter cycle is more damaging.

**Floor beam fatigue:**
- Each loading cycle deflects the floor beams under pallet weight. A 5-tonne pallet placed on a 1 m floor section deflects the beam 2-5 mm at midspan. Over 10,000 loading cycles, this repeated deflection accumulates fatigue at the beam-to-frame attachment (usually riveted or bolted joints). Fatigue cracks initiate at stress concentration features: rivet holes, bolt holes, and section changes.
- Inspection: floor beams are inspected by visual and eddy-current methods at every C-check (every 4,000-6,000 flight hours). Cracks under 5 mm are monitored; cracks over 12 mm require beam replacement.

**Fuselage pressure cycling:**
- Each flight pressurises the fuselage to 6-8 psi differential (cabin altitude 2,400 m at flight level 350). The fuselage skin expands and contracts by 1-2 mm in diameter each cycle. Hoop stress in the skin from pressurisation is 50-70 MPa in 2024-T3 aluminum (ultimate strength 450 MPa, fatigue limit ~140 MPa for unnotched material, but 60-80 MPa at rivet holes due to stress concentration).
- This is why freighter conversions (passenger aircraft modified for cargo) have a reduced cycle life — the airframe has already consumed 10,000-40,000 cycles in passenger service before conversion. The 737-800BCF (Boeing Converted Freighter) is certificated for 60,000 cycles total, but a 20-year-old passenger airframe may have already used 40,000 of them.

## Fire Suppression

Cargo fires are the most feared emergency in air freight. Unlike a passenger cabin where a fire is seen and fought immediately, a fire in a lower-deck cargo hold may burn undetected for minutes.

**Detection:**
- Smoke detectors (photoelectric or ionisation type) are mounted in the ceiling of each cargo compartment. The 747F lower deck has 8-12 smoke detectors; the main deck has 6-10. Detectors feed a fire warning panel on the flight deck that identifies the affected zone.
- Rate-of-temperature-rise detectors are used as backup in some installations. A rapid temperature increase (>5°C/minute) triggers an alarm independent of smoke.

**Suppression:**
- Halon 1301 (bromotrifluoromethane, CBrF₃) was the universal cargo fire suppressant. One or two discharge bottles per compartment release 2-5% Halon concentration by volume, extinguishing flame by interrupting the chemical chain reaction. Halon is a potent ozone-depleting substance — production was banned under the Montreal Protocol in 1994, but existing stocks are still used in aviation because no drop-in replacement matches its performance.
- Modern alternatives: Halon 1301 reserves are being depleted. Candidate replacements include Halon 1211 (also being phased out), FM-200 (heptafluoropropane, requires 50% more concentration), and water-mist systems (effective on Class A fires — cardboard, fabric — but not on flammable liquid cargo).
- In a bootstrapping scenario without halon chemistry, the only suppression option is water spray (manual or automatic) combined with cabin descent to a lower altitude where the fire is starved of oxygen. This is a desperate measure — a cargo fire at cruise altitude over ocean is one of the most dangerous scenarios in aviation.

## Loading Cycle and Turnaround

The economic case for air freight depends on keeping the aircraft airborne. A 777F that costs $12,000/hour to operate earns nothing while sitting on the ground. Turnaround procedure is engineered as a parallel sequence:

**Standard freighter turnaround (target: 60-90 minutes):**

| Step | Time (min) | Parallel? |
|------|-----------|-----------|
| Park, chock, connect ground power | 3 | — |
| Open main-deck cargo door | 2 | — |
| Position ground handling equipment (conveyor, forklift) | 5 | Parallel with door |
| Offload main-deck pallets (27 PMC for 777F) | 20 | Sequential |
| Offload lower-deck containers (10 LD3 for 777F) | 10 | Parallel with main deck |
| Refuel (60,000-100,000 L Jet A-1) | 25 | Parallel with loading |
| Load lower-deck containers | 10 | Parallel with main deck |
| Load main-deck pallets | 20 | Sequential |
| Close cargo door | 2 | — |
| Load planning verification, paperwork | 5 | Parallel with loading |
| Push back / start engines | 5 | — |
| **Total** | **~65** | — |

The critical path is main-deck pallet loading (20 minutes offload + 20 minutes load = 40 minutes of conveyor operation). Refuelling runs in parallel but is itself a 25-minute task. Any delay in one step cascades into missed departure slots.

## Weight and Balance Envelope

The certified CG envelope is the most important diagram in a freighter's operating manual. It defines the safe combinations of gross weight and centre-of-gravity position.

**Envelope geometry:**
- The envelope is a polygon on a graph of weight (vertical axis) vs. CG position in % MAC (horizontal axis). At low gross weight, the CG range is wide (20-35% MAC). At maximum takeoff weight, the range narrows (22-30% MAC) because structural limits and control authority are tighter.
- The forward limit slopes aft at high weight — at MTOW, the aircraft needs the CG further aft to reduce tail-down force (which adds to effective weight). The aft limit slopes forward at high weight — too far aft and the aircraft lacks the pitch authority to recover from a stall.

**Loadmaster's calculation:**
- The loadmaster uses a loading manifest listing each pallet position, its weight, and its distance from the datum (a reference point, usually the nose or the wing leading edge). The total weight is divided by the total moment (weight × arm) to give the CG position.
- If the computed CG falls outside the envelope, pallets must be rearranged. This is an iterative process — move a 4-tonne pallet from position L7 (arm +5.0 m) to position L3 (arm +1.0 m), recompute, check the envelope. A skilled loadmaster can place 27 pallets correctly in 2-3 iterations.

## Freighter Conversion vs Clean Sheet

Most air freight in the early decades of a bootstrapping economy will be carried by converted passenger aircraft, not purpose-built freighters. The decision hinges on volume:

**Passenger-to-freighter (PTF) conversion:**
- Cut a 3.5 × 2.7 m cargo door into the left side of the fuselage (between frames 3A and 5 on a 737). This requires re-engineering the fuselage skin load path — a door that large concentrates stress at its corners, requiring doubler plates and forged doorframes.
- Strip the passenger interior: seats, overhead bins, sidewall panels, galleys, lavatories. Remove floor tracks for seats; install floor tracks for cargo rollers and fittings.
- Reinforce the floor: add 5-10 mm to the floor beam flanges, replace floor panels with higher-rated cargo panels (732-1,953 kg/m²).
- Install a cargo handling system: roller tracks, PDUs, lashing points, smoke detectors, fire suppression bottles.
- Cost: $4-13 million per aircraft (737-800BCF: $4M; 777-3000ERSF: $13M). Takes 90-120 days in a conversion facility.
- Result: a freighter with 80-90% of the payload of a clean-sheet design, at 30-50% of the acquisition cost. The economics favour conversion until annual cargo volume exceeds the capacity of the existing passenger fleet's retirements.

**Clean-sheet freighter:**
- Designed from the start for cargo: optimised floor height for ground equipment, nose door option, maximum payload volume. The 747F and 777F are clean-sheet freighters (though the 777F shares its fuselage with the 777-200LR passenger aircraft, it was designed with cargo as the primary mission from the outset).
- Justified when: annual air cargo volume exceeds 500,000 tonnes per route pair, or when outsized cargo demand (satellites, military vehicles) requires a nose door that no conversion can provide.

## See Also

- [Aviation](aviation.md) — airframe and engine fundamentals
- [Jet Propulsion](jet-propulsion.md) — turbofan engines for heavy freighters
- [Turbofan Engines](jet-propulsion.turbofan.md) — high-bypass engines used in civil freighters
- [Cargo Handling Systems](cargo-aircraft.cargo-handling-systems.md) — interior loading systems process
- [Aluminum](../metals/aluminum.md) — primary structural material
- [Transport](../transport/index.md) — ground and marine transport alternatives

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
