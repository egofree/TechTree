# High-Speed Rail

> **Node ID**: transport.high-speed-rail
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.railways`](./railways.md), [`transport.electric-railways`](./electric-railways.md), [`energy.electricity`](../energy/electricity.md), [`energy.electricity.motor`](../energy/electricity.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 40-60+
> **Outputs**: high_speed_trains, aerodynamic_train_sets
> **Critical**: No

## Overview

High-speed rail (HSR) is the engineering discipline of moving passengers on steel wheels or magnetic cushions at 200–350+ km/h over dedicated infrastructure. It is not simply a faster train — it is an integrated system in which vehicle, track, power supply, and signaling must be co-designed to within millimeter and millisecond tolerances. A 1 mm track misalignment invisible at 80 km/h becomes a violent harmonic at 300 km/h. A pantograph that arcs at 100 km/h can weld itself to the catenary at 300 km/h.

The capability builds directly on conventional [Railways](./railways.md) (track, gauge, rolling stock principles) and on [Electric Railways](./electric-railways.md) (overhead catenary, traction motors, regenerative braking). It is treated as a separate capability because the speed regime introduces qualitatively new problems — aerodynamic drag scaling with velocity squared, tunnel pressure waves, wheel-rail contact fatigue at high contact stress, and signaling that must resolve train positions faster than the human eye can react.

High-speed rail is a bootstrap-capability milestone: it requires precision metallurgy (rail steel), high-power electronics (IGBT/SiC traction converters), advanced aerodynamics (wind-tunnel-validated trainset design), precision surveying (millimeter alignment over kilometers), and sophisticated control systems (continuous cab signaling with automatic train protection). It is not a single technology but the integration of mature capabilities across multiple domains.

### Speed Categories

| Category | Speed Range (km/h) | Representative Systems | Key Challenge |
|----------|-------------------|----------------------|---------------|
| Conventional upgraded | 160–200 | Amtrak Northeast Corridor, older TGV lines | Mixed traffic conflicts |
| Entry high-speed | 200–250 | Early Shinkansen 0 Series (1964, 210 km/h) | Aerodynamic drag onset |
| High-speed | 250–300 | TGV (Paris–Lyon, 1981, 260 km/h), ICE 1, Shinkansen 300/500 | Wheel-rail dynamics |
| Very high-speed | 300–350 | Shinkansen N700, TGV POS, CRH380, ICE 3 Velaro | Current collection at speed |
| Ultra high-speed (maglev) | 500–600+ | JR-Maglev L0 (603 km/h record), Transrapid (Shanghai, 430 km/h) | Guideway tolerance, cost |

## Why High Speed Is Hard

### The Power–Drag Problem

Aerodynamic drag scales with the cube of speed. Doubling speed requires roughly eight times the power. The total resistance of a high-speed train is the sum of rolling resistance (nearly constant, ~5–8 N/tonne at speed) and aerodynamic resistance (proportional to v²). The crossover where aerodynamic drag exceeds rolling resistance occurs near 70–80 km/h for a typical trainset; at 300 km/h, aerodynamic drag is 90–95% of total resistance.

A 200 m long trainset at 300 km/h faces aerodynamic resistance comparable to a small aircraft at the same dynamic pressure. The Shinkansen N700 develops approximately 13 MW (17,500 HP) at the rail — distributed across 16 powered axles — to sustain 300 km/h on level track. The original 0 Series managed 210 km/h with only 4 MW, because drag at that lower speed was one-third as severe. Energy consumption at 300 km/h is approximately 50–70 Wh per seat-km — competitive with short-haul air (60–90 Wh/seat-km including climb) but far higher than a 160 km/h train (20–30 Wh/seat-km).

The power-to-weight ratio for high-speed stock is 10–20 kW/tonne, compared to 3–5 kW/tonne for conventional electric multiple units. This is not achieved by a single massive locomotive — the power is distributed along the train in powered bogies (EMU configuration: Electric Multiple Unit) so that adhesive weight carries the motors and no single axle is overloaded. The alternative — a single power car at each end (TGV-style articulated trainset) — concentrates traction but limits the number of driven axles to 4–8 per power car, demanding higher per-axle power and raising the adhesion limit risk on wet rails or autumn leaf contamination.

### Current Collection at Speed

The [electric motor](../energy/electricity.md) is fed through a pantograph sliding against a contact wire suspended in a zigzag "stitch" catenary 4–5 m above the track. At 300 km/h the pantograph traverses approximately 83 m of wire per second. The contact wire oscillates laterally 20–30 cm per stitch, so the pantograph head must follow this geometry while maintaining steady downward force (70–120 N). Loss of contact for even 10 ms causes an arc — a miniature lightning bolt — that erodes the contact strip and can weld the pantograph to the wire. At 300 km/h, a stuck pantograph tears down kilometers of catenary before the train stops.

High-speed pantographs use a low-mass carbon contact strip on a spring-loaded frame with aerodynamic lift compensation: the faster the train moves, the more aerodynamic lift pulls the head up, so the suspension is pre-loaded to counteract this. The catenary tension is increased (20–30 kN per wire vs. 10 kN for conventional) so the wire sag between supports is minimized and the natural frequency stays well above the excitation frequency of the passing pantograph.

### Wheel–Rail Forces

At speed, the steel wheel–steel rail contact patch is an ellipse roughly 1 cm² carrying 10–15 tonnes of axle load. The conical wheel tread (1:40 cone angle) provides self-centering through the kinematic oscillation known as hunting — a sinusoidal lateral motion whose wavelength depends on speed. Below 120 km/h, hunting is damped by the rail and wheel flange geometry. Above roughly 200 km/h, the hunting wavelength stretches and its amplitude grows, demanding precision wheel re-profiling and tight track gauge control. A wheel with a worn profile or a rail with gauge widening of more than a few millimeters will develop violent hunting that derails the train.

The contact patch transmits tractive effort, braking, and lateral guidance simultaneously. At 300 km/h with 250 kN per axle of tractive effort, the rail steel (900–1100 MPa tensile, 300+ HB surface) must resist rolling contact fatigue — a network of subsurface cracks that propagates under cyclic loading. Rails on high-speed lines are ground regularly (every 30–100 million gross tonnes of traffic) to remove the thin work-hardened layer where cracks initiate, before they reach 3 mm depth.

Wheel-rail adhesion also limits how rapidly the train can accelerate or brake. The coefficient of friction between clean dry steel wheel and steel rail is 0.25–0.35; under full adhesion, a train can brake at 1.0–1.5 m/s² deceleration. Under wet conditions adhesion drops to 0.10–0.15 and emergency braking distances stretch from 3,000 m (dry, 300 km/h) to 4,500–5,000 m (wet). Leaf contamination in autumn can drop adhesion below 0.05, requiring sandite (sand/gel mixture) application to the rails or reduced service speed. Regenerative braking (feeding power back to the catenary) is preferred for normal braking because it avoids friction-wear on brake discs and recovers energy; friction brakes are reserved for low-speed and emergency stops.

### Tunnel Boom

When a train enters a tunnel at 300 km/h, it compresses the air ahead of it into a pressure wave that travels at the speed of sound. When this wave reaches the tunnel exit, part of it reflects back as a rarefaction wave and part radiates outward as a sonic boom — a sharp "bang" audible up to a kilometer away, sufficient to damage nearby structures and trigger noise complaints. The Shinkansen Nakayama tunnel (1975) saw booms measured at 150+ dB at the exit portal.

Mitigation requires aerodynamically shaped tunnel entrance hoods (flared portals extending 20–50 m, with ventilation slots that release pressure gradually) and train noses long enough (Shinkansen N700: 7 m, L0 maglev: 15 m) to reduce the pressure gradient at entry. Cross-sectional area ratio of train to tunnel (the "blockage ratio") is kept below 0.15 for high-speed lines, compared to 0.20–0.25 for conventional tunnels.

## Aerodynamic Trainset Design

The trainset must be shaped as one continuous aerodynamic body, not a collection of cars. The [aerodynamic design process](high-speed-rail.aerodynamic-design.md) addresses:

- **Nose geometry**: A long tapered nose (5–15 m) reduces the pressure gradient at tunnel entry and lowers the drag coefficient. The Shinkansen 500 Series introduced an aircraft-like nose based on the boundary layer intake theory; the L0 maglev uses a 15 m nose for double duty — tunnel pressure relief and drag minimization.
- **Cross-section**: Smaller frontal area reduces drag (which scales with area). Shinkansen 3.4 m² cross-section vs. 4.0 m² for older series. But internal passenger space must be preserved, so the car body cross-section is curved to shave corners without sacrificing headroom.
- **Inter-car gaps**: The turbulent wake behind each car junction creates 20–30% of total train drag. Sealing the gaps with articulated fairings (TGV articulated trainset rigidly couples adjacent cars at the bogie, eliminating the gap entirely) or bellows-type diaphragms reduces this loss.
- **Bogie skirts**: Fairings over the underframe bogies cut underbody drag (15% of total) and reduce ballast pickup — a serious hazard at 300 km/h where ballast stones are sucked up by the wake and strike the underside of following cars.
- **Pantograph aerodynamics**: The pantograph itself is a drag source. High-speed designs use a low-profile single-arm design with active suspension and aerodynamic shrouding.

Drag coefficient (Cd) for a full trainset: 0.8–1.2 measured against frontal area. The Shinkansen N700 achieves approximately 0.8; older 0 Series measured 1.4. Each 0.1 reduction saves roughly 1 MW at 300 km/h.

## High-Speed Track Geometry

The track for 300+ km/h is not merely conventional railway built more carefully — it requires dedicated alignment. The [track geometry process](high-speed-rail.track-geometry.md) defines:

- **Curve radius**: Minimum 5,000 m for 300 km/h (sufficient to keep lateral acceleration under 1.0 m/s² without tilting). For 350 km/h, minimum 7,000–10,000 m. Curves of 15,000 m radius are used where terrain allows. Superelevation (cant) is limited to 150–180 mm (conventional) or 200 mm (special), with cant deficiency (the under-banking felt as lateral force by passengers) capped at 90–130 mm.
- **Gradient**: Maximum 2.0–2.5% (less than the 3–4% allowed for conventional electric). Steeper grades cost energy climbing and demand more braking power descending; the TGV Paris–Lyon line keeps gradients under 1.5%.
- **Slab track (ballastless)**: Conventional ballasted track drifts under high-speed dynamic loading — ballast particles migrate, sleepers settle unevenly, and gauge opens up over weeks. Slab track — a continuously reinforced concrete slab supporting the rails on elastic pads or directly fastened — holds geometric tolerance to ±1–2 mm over 10 m measurement chords. Two designs dominate: the Shinkansen slab (precast concrete slabs 5 m long on a cement-asphalt mortar bed) and the Rheda system (cast in-situ concrete track on a bitumen base). Slab track costs 2–3× ballasted track initially but halves maintenance cost and lasts 60 years vs. 30 for ballast. The Shinkansen pioneered slab track; Chinese, German, and Spanish lines have adopted it. Ballast is still used on some lower-speed high-speed segments (200–250 km/h) for cost reasons, but it requires ballast bonding (glue or polyurethane) to prevent particle flight.
- **Continuous welded rail (CWR)**: Rails welded into strings of 1–2 km or longer (thermite or flash-butt welding). No bolted joints. CWR must be anchored against thermal expansion: rails are tensioned to a neutral temperature (20–25°C) so they neither buckle in summer nor fracture in winter. The longitudinal restraint of each fastener clip must be 8–12 kN; with 600+ clips per km, the total rail anchorage is enormous. Rail temperature is monitored continuously in hot weather; when it exceeds 55–60°C (measured in rail, not air), speed restrictions are imposed to avoid buckling risk.
- **Transition curves**: Clothoid spirals (linear curvature ramp) connect tangent (straight) track to circular curves, so lateral acceleration builds up gradually rather than as a step. Spiral length: 200–400 m for 300 km/h, proportional to speed cubed.
- **Rail fastening**: Modern elastic fastening systems (e.g., Pandrol Vipa, VOSSLOH Skl) use a tensioned clip providing 8–12 kN toe load with 20–30 kN/m longitudinal resistance. The rail pad between rail and baseplate is a 5–10 mm thick elastomer (EPDM or natural rubber) tuned to provide 20–50 kN/mm vertical stiffness — stiff enough to prevent rail rotation under load, soft enough to damp high-frequency wheel impact. Pad life is 15–25 years; degraded pads (hardened, cracked) must be replaced to avoid uncontrolled track geometry degradation.

## Electric Traction Systems

High-speed trains consume enormous power. A 16-car Shinkansen at 300 km/h draws 13 MW — comparable to a small town. The overhead supply is 25 kV AC at 50/60 Hz (standard) or 15 kV AC at 16⅔ Hz (German/Austrian/Swiss). The high voltage minimizes line losses: at 25 kV, 13 MW is 520 A; at lower voltage the same power would require proportionally more current and correspondingly heavier copper catenary. The 16⅔ Hz systems are legacy from the early 20th century when rotary converters could not easily change frequency; they remain because the lower frequency reduces reactive line impedance over long distances, but they require dedicated power plants or frequency converters separate from the national grid.

Each powered axle has its own AC induction or synchronous motor (typically 200–300 kW per axle), driven by a power converter (GTO thyristor or IGBT inverter) that synthesizes variable-frequency three-phase AC from the fixed-frequency overhead supply. The converter regenerates during braking — feeding power back into the catenary for use by other trains or returning it to the grid. Modern Shinkansen recover 20–30% of traction energy this way. The power-electronics revolution of the 1990s (replacement of GTO thyristors by IGBTs, and later SiC MOSFETs) reduced converter weight by 40% and losses by half, enabling the distributed-traction architecture that dominates modern high-speed stock.

The traction motor itself is a three-phase AC induction motor (squirrel-cage rotor, no brushes, maintenance-free) or a permanent-magnet synchronous motor (PMSM, higher efficiency, smaller, but requires rare-earth magnets). The motor is frameless and integrated into the bogie gearbox, driving the axle through a hollow shaft with flexible coupling. Total mass per axle drive: 1.5–2.5 tonnes including gearbox and converter. Cooling is forced-air (ducted from roof intake) or water-jacketed (closed-loop glycol, radiator on car roof).

Current collection is the critical interface. See the power–drag discussion above for the physics; operationally, a second pantograph on the last powered car is standard (backup) and the front pantograph alone is used in normal running to minimize catenary wear. The contact wire is grooved copper (107–150 mm² cross-section), tensioned to 20–30 kN, supported on bracket tubes every 50 m, and stitched to maintain geometric uniformity. The wire is replaced every 3–5 million pantograph passes on high-speed lines.

## Magnetic Levitation Systems

Maglev eliminates the wheel-rail contact entirely, removing the kinematic constraints of hunting and the tractive-effort cap of adhesion. The [maglev process](high-speed-rail.maglev-systems.md) covers two technologies:

### Electromagnetic Suspension (EMS) — Transrapid

The train wraps around the guideway from below. Electromagnets on the train underside pull upward against the steel guideway rail, levitating the train 8–10 mm below the guideway. The gap is tiny and unstable: any disturbance must be corrected by the control system within milliseconds, or the train touches down. Active gap sensors sample at 100 kHz; the current to the support magnets is adjusted to hold the gap at 10 mm ± 1 mm. The Transrapid system (developed in Germany, deployed in Shanghai 2004) reaches 430–500 km/h in commercial service.

Propulsion is by a linear synchronous motor built into the guideway: the track is the stator (wound with three-phase cable), and the train's support magnets are the rotor. The guideway is energized in sections ahead of the train, so only the segment the train currently occupies draws power. This is expensive in guideway cost (3–5× conventional HSR per km) but eliminates onboard propulsion power and allows higher acceleration.

### Electrodynamic Suspension (EDS) — JR-Maglev

Superconducting electromagnets on the train (cooled with liquid helium to 4 K, persistent-mode NbTi coils carrying 700 kA-turns) induce repulsive currents in aluminum coils embedded in the guideway walls as the train moves faster than 100 km/h. Below 100 km/h there is insufficient induced current to levitate, so the train runs on retractable wheels until takeoff speed. The gap is much larger than EMS — typically 100 mm — making the system inherently stable and far more tolerant of guideway irregularity.

The JR-Maglev L0 series set the world rail speed record of 603 km/h (2015) on the Yamanashi test track. Commercial service between Tokyo and Nagoya is targeted at 500 km/h, reducing the 1.5 h Shinkansen trip to 40 min. The cost is dominated by the guideway (precision-bored tunnels and elevated viaducts for a route that is 86% in tunnel through the Japanese Alps) and the cryogenic systems on each train.

### Guideway Tolerance

Both maglev technologies demand guideway geometric precision that exceeds even high-speed slab track:
- **EMS (Transrapid)**: ±0.6 mm over 3 m measurement chord. Achievable only with precision surveying, laser alignment during construction, and periodic re-measurement. Thermal expansion of the steel guideway is controlled by painting it white (low solar absorption) and by expansion joints.
- **EDS (JR-Maglev)**: ±2 mm over 10 m chord. More relaxed than EMS because of the larger gap, but still an order of magnitude tighter than conventional railway.

## Notable Systems (Historical Reference)

- **Shinkansen 0 Series** (1964, Japan): The original HSR. 210 km/h Tokyo–Osaka. 12-car EMU, 11.8 MW. Proved that dedicated high-speed infrastructure was viable at scale. Retired 2008. Named for its distinctive blue-and-white livery; nicknamed "yume no chotokkyu" (the dream superexpress).
- **Shinkansen N700** (2007, Japan): 300 km/h. 16-car EMU, 13 MW. Introduced active suspension (tilting on curves by 1° without passenger discomfort) and full EMU configuration (all axles powered for maximum tractive effort on gradients up to 2.5%).
- **Shinkansen L0 (maglev)** (2014 test, 2015 record): 603 km/h. World rail speed record. 24 superconducting magnets per car. Target commercial service Tokyo–Nagoya at 500 km/h.
- **TGV Paris–Lyon** (1981, France): 260 km/h. Proved HSR could be built on existing right-of-way with carefully aligned new construction only where necessary (the lignes nouvelles). Articulated trainset with power cars at both ends sharing a Jacobs bogie between adjacent passenger cars.
- **TGV V150** (2007 test): 574.8 km/h world speed record for conventional wheel-rail. Modified 3-car trainset with oversized wheels, doubled power, and specially prepared catenary. Demonstrated the theoretical ceiling of wheel-rail technology; not a commercial configuration.
- **ICE 1** (1991, Germany): 250–280 km/h. First major system to use distributed traction on some variants. Later ICE 3 Velaro (2000) adopted full EMU configuration and exported to Spain (AVE S-103), China (CRH3), and the UK (Class 395).
- **Acela** (2000, USA): 240 km/h peak, limited by shared-corridor curves. Tilting trainset for existing curves — the train leans into curves by up to 4.2° to compensate for cant deficiency, allowing 30% higher speed on curves without passenger discomfort.
- **CRH (China Railway High-speed)** (2007–present): Largest network (40,000+ km of HSR track, more than the rest of the world combined). CRH380 series reaches 350 km/h in service. Multiple platforms from technology transfer (CRH2 from Kawasaki Shinkansen, CRH3 from Siemens Velaro) plus indigenous designs (CR400AF/BF "Fuxing," 350 km/h, 2020s).

## Signaling and Control

High-speed trains cannot rely on the driver sighting wayside signals — at 300 km/h the train covers 83 m per second, and driver reaction time plus braking distance means a signal visible at 1,000 m is only 12 seconds away. All high-speed lines use continuous in-cab signaling (ATC: Automatic Train Control), where permitted speed is displayed in the cab and enforced by automatic braking if exceeded. The European Rail Traffic Management System (ERTMS/ETCS Level 2) is the emerging standard: trackside signals are eliminated entirely; movement authorities are transmitted by GSM-R or LTE radio to the train, and train position is determined by axle counters and balises (transponders between the rails). This permits very short headways (2–3 minutes) at full speed and is the basis for the capacity claims of modern HSR lines.

Train detection relies on track circuits (electrical continuity of the rails is broken by a train's axles) or axle counters (counting axles entering and leaving each block). Both methods must be immune to the traction return current (1,000+ A in the rails on AC-electrified lines) and to lightning surges. The signaling system is fail-safe: loss of signal is interpreted as "stop," and any discontinuity in the track circuit drops all signals to danger. See [Railways](./railways.md) § Signaling for the semaphore and block-system foundations; high-speed lines extend these with continuous cab signaling and automatic train protection.

## Safety Systems

High-speed rail has an exceptionally strong safety record. The Shinkansen has carried over 10 billion passengers since 1964 with zero passenger fatalities from derailment or collision. This safety level is achieved through multiple redundant systems:

**Derailment prevention**: The most dangerous HSR scenario is a high-speed derailment — the kinetic energy at 300 km/h is 100× that at 30 km/h and the train can disintegrate or overturn. Guard rails (deflectors mounted inside the running rails on viaducts and bridges) catch a derailed wheel and guide it along the track rather than letting the train fall. Bogie-mounted sensors detect abnormal vertical or lateral acceleration and trigger emergency braking before a hunting oscillation can build to derailment. The Shinkansen's earthquake early-warning system (UREDAS) detects P-waves from offshore seismic events and brings trains to a halt before the damaging S-waves arrive — at 300 km/h, even 10 seconds of warning is 800 m of braking distance saved.

**Collision prevention**: Automatic Train Control (ATC) enforces speed limits at all times; the driver cannot exceed the permitted speed without the system intervening. If the driver becomes incapacitated (dead-man's handle / vigilance device), the train stops automatically. Point (switch) machines are interlocked with signaling so that no train can be routed into an occupied block or a wrongly set route. Track circuits detect broken rails: a rail break interrupts the electrical circuit and drops all signals in the area to stop.

**Fire safety**: All materials in the passenger compartment must meet stringent flame-spread and smoke-toxicity standards (e.g., DIN 5510, NF F 16-101). Escape paths are designed so that passengers can evacuate a burning train through the ends of each car into adjacent cars, and side doors can be opened manually from inside or outside in emergency. Emergency lighting on battery backup illuminates the escape path for at least 90 minutes.

## System Integration

High-speed rail succeeds or fails as an integrated system. A train that can do 350 km/h is useless on a track that is geometrically limited to 250 km/h; a precision slab track is wasted on a train with poor aerodynamics that wastes energy. The design discipline requires:

- **Route alignment first**: The single most expensive and irreversible decision is the route geometry. Tunnel and viaduct proportions of 20–80% of route length are common in mountainous terrain (Japan, Taiwan, Italy); these dominate capital cost and cannot be modified later.
- **Fleet matched to line**: Trainset power, adhesion, and braking are specified for the steepest grade, tightest curve, and maximum speed of the route. An under-powered trainset will fail to maintain schedule on gradients; an over-powered one wastes capital on traction equipment.
- **Power supply matched to traffic**: The traction substation spacing (typically 20–50 km apart for 25 kV AC lines) must supply the simultaneous draw of multiple trains. Two 16-car trainsets accelerating at the same time on the same electrical section can draw 30+ MW; the substation transformer and feeder cable must be sized for this peak, not for average demand.
- **Maintenance regime built into operations**: Night-time maintenance windows (typically 4–6 hours) are mandatory on high-speed lines. Track geometry is re-measured weekly to monthly; rails are ground every 1–3 years; catenary is inspected by pantograph measuring car every 2–4 weeks. The line cannot operate 24/7 — the engineering demands dedicated maintenance time.

## Energy and Sustainability

Per seat-kilometer, HSR is among the most energy-efficient modes of motorized transport:
- 18–30 Wh/seat-km at 300 km/h (typical 75% load factor)
- Compared to: short-haul air 50–80 Wh/seat-km, private automobile 35–60 Wh/seat-km (single occupancy), conventional electric train 15–25 Wh/seat-km at 160 km/h

The energy signature is dominated by speed: energy consumption per seat-km roughly doubles between 200 km/h and 300 km/h. Operating at 300 km/h instead of 350 km/h saves approximately 25% of traction energy at the cost of longer trip time. Several operators (SNCF, DB) have reduced maximum speeds by 10–20 km/h to cut energy cost without materially affecting schedule.

Regenerative braking recovers energy during deceleration. A TGV or Shinkansen arriving at a station feeds 20–30% of its kinetic energy back into the catenary, where it is consumed by nearby accelerating trains (line receptivity) or returned to the utility grid. Where the local grid cannot absorb this reverse flow (some older substations), the regenerated energy is dumped into on-board braking resistors as heat — a less efficient but simpler arrangement.

## Environmental and Acoustic Impact

Noise is the dominant environmental constraint on high-speed rail. Unlike conventional railways where engine and wheel noise dominate, at speeds above 300 km/h the aerodynamic noise of the train body and pantograph exceeds mechanical sources. A train at 300 km/h generates 90–95 dB(A) at 25 m from the track; at 350 km/h it rises to 95–100 dB(A). For context, 85 dB(A) is the threshold for hearing damage over 8-hour exposure.

Mitigation measures:
- **Wayside noise barriers**: Concrete or transparent acrylic walls 2–4 m high on each side of the track, reducing noise by 10–15 dB at the receiver. On slab track, barriers are integrated with the track slab for structural efficiency. Transparent barriers are preferred in scenic areas but suffer from graffiti and bird strikes.
- **Trackside berms**: Earth mounds 3–6 m high, cheaper and more visually acceptable than walls, but require 4–6 m of additional right-of-way width per side.
- **Aerodynamic shaping of trains**: The dominant noise source above 300 km/h is the pantograph and bogie wake; shaping the pantograph with low-drag fairings and sealing bogie cavities reduces noise at the source. The Shinkansen N700S reduced pantograph noise by 4–5 dB through redesigned collector heads.
- **Speed limits in urban areas**: Many HSR lines impose 200–250 km/h speed restrictions through densely populated zones to keep noise below regulatory thresholds, trading trip time for community acceptance.

Vibration is a secondary concern: the dynamic loading of a passing high-speed train propagates through the ground as Rayleigh waves, felt as a low-frequency rumble in nearby buildings 20–50 m from the track. Mitigation requires resilient track mounting (rubber mat under slab, floating-slab track on springs) or, in extreme cases, trench barriers filled with stiff foam to intercept the wave path.

## Strengths

- Effective capacity: a double-track HSR line moves 15,000–20,000 passengers per hour per direction at 3-minute headways — far above air or road for the 200–1000 km city-pair range where HSR dominates
- Energy efficiency per passenger-km: 3–5× lower than short-haul air, 2× lower than private car, because steel-wheel-on-steel-rail rolling resistance is the lowest of any ground transport mode
- Speed reliability: dedicated track (no freight or grade crossings) means no interference, so 300+ km/h cruise is sustained hour after hour
- City-center to city-center routing: avoids airport peripheral location and check-in overhead
- All-weather operation: unlike air travel, HSR operates in fog, light snow, and moderate wind without significant delay. Heavy snow requires de-icing of catenary and reduced speed, but the system does not shut down
- Safety record: Shinkansen has carried over 10 billion passengers since 1964 without a single passenger fatality from derailment or collision — the best safety record of any transport mode
- Modal shift: well-implemented HSR captures 60–80% of the air/rail combined market in its sweet-spot distance range, reducing road congestion and aviation emissions

## Weaknesses

- Capital intensity: 15–40 M USD/km depending on terrain and proportion of tunnel/viaduct; comparable to a divided highway but with no freight revenue to defray cost
- Dedicated infrastructure: HSR track cannot carry conventional freight without speed penalties; the line is a single-purpose asset
- Noise footprint: aerodynamic noise (not engine noise) dominates above 300 km/h; a train at 300 km/h generates 90–95 dB at 25 m, requiring extensive noise barriers in populated areas
- Brittle to disruption: a single track incident stops an entire corridor; resilience comes only from double-tracking and redundant fleet
- Long payback period: typical financial payback exceeds 30 years; most HSR systems require public subsidy for construction and some for ongoing operation. The economic case rests on wider benefits (time savings, agglomeration, regional development) that are hard to monetize on a balance sheet
- Land take: the alignment requires straight corridors through sometimes densely populated or environmentally sensitive land, leading to lengthy planning disputes and compulsory acquisition

## Materials

| Component | Material | Specification |
|-----------|----------|---------------|
| Rails | Heat-treated steel | 60 kg/m, 900–1100 MPa tensile, 300+ HB surface, 100 m rolling length welded |
| Slab track | Reinforced concrete | C40/50 grade, 5–6 m wide slab on bitumen pad or asphalt concrete, 60-year design life |
| Slab track pad | EPDM rubber or cork-rubber | 5–10 mm thick, 20–50 kN/mm vertical stiffness, 15–25 year life |
| Continuous welded rail strings | Flash-butt welded steel | 1–2 km long, thermite welds at site joints, neutral temperature 20–25°C |
| Contact wire | Copper alloy (Cu-Ag, Cu-Mg) | 107–150 mm², 20–30 kN tension, grooved section |
| Train body | Aluminum extrusion or double-skin steel | Welded monocoque, 8–12 tonne per car, 3.0 m width |
| Bogie frame | Cast steel | Box section, 5–8 tonne per bogie, fatigue-rated to 10⁹ cycles |
| Wheel | R8 or ER7 steel | 860–920 mm diameter, 1:40 conical tread, re-profiled every 1.2 M km |
| Motor | AC induction or PMSM | 200–300 kW per axle, water-cooled, IGBT inverter drive |
| Maglev coil (EDS) | NbTi superconductor in Cu matrix | Persistent mode, 700 kA-turns, 4 K liquid helium |

## Equipment

- **Track maintenance**: High-speed track recording car (measures gauge, cross-level, alignment, and twist at 200+ km/h, sampling every 0.25 m), rail grinding train (48–96 grinding stones remove the work-hardened layer in a single pass at 5–12 km/h), tamping machine (for ballasted sections), slab inspection trolley (laser-measures slab position to ±0.5 mm)
- **Catenary maintenance**: Pantograph inspection vehicle (measures contact force dynamically at speed), wire wear measuring car (optical/laser measurement of remaining cross-section every 50 m), tensioning system calibration rig, contact wire de-icing pantograph (winter operation)
- **Train inspection**: Underfloor lifting jacks (synchronize-lift 4–16 cars), wheel lathe (re-profiles wheels in-place under the train without bogie removal, 0.1 mm precision), bogie swap rig (exchange a full bogie in 2–4 hours), motor test bench, pantograph drop test rig (verifies downward force and contact strip condition)
- **Depot infrastructure**: Wheel lathe pit, underfloor inspection pit (lighted, with dropped-wrench detection), overhead catenary isolation switches (ground the overhead line for safe depot work), train wash plant (automatic roof-and-side wash cycle, 8–12 min per train), waste and toilet-system servicing bay

## Limitations

- **Speed ceiling (wheel-rail)**: Approximately 350–400 km/h before wheel-rail dynamics, current collection, and aerodynamic heating make further gains uneconomic. The French V150 test reached 574.8 km/h (2007) but only with a modified 3-car trainset on a specially prepared track — not a commercial configuration
- **Maglev cost**: 3–5× conventional HSR guideway cost per km; only justified where population density and trip volume are extreme (Tokyo–Osaka corridor)
- **Noise**: Aerodynamic noise above 300 km/h cannot be reduced by engine modifications — only by overall train shaping and wayside barriers. The cost per dB of noise reduction rises steeply above 90 dB
- **Network effects**: HSR works only as a point-to-point corridor with large cities at both ends; branch lines dilute the speed advantage. The 200–1000 km city-pair is the sweet spot — below 200 km/h, conventional rail or road is competitive; above 1000 km, air travel dominates on time
- **Mixed traffic constraint**: A high-speed line that also carries slower freight or conventional passenger trains has its capacity and speed degraded — the slowest train sets the average speed. Dedicated passenger-only infrastructure is the norm
- **Power infrastructure**: The traction substations, catenary reinforcement, and feeder cable are a substantial fraction of capital cost (10–20%) and require grid capacity that may not exist in less-developed regions
- **Earthquake exposure**: In seismic zones (Japan, Taiwan, Turkey), HSR track and structures are vulnerable to ground displacement that can throw a train off its rails. Earthquake early-warning systems and automatic power-off mitigations are required, but a major event under a moving train remains catastrophic risk

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Violent car-body lateral oscillation above 250 km/h | Wheel tread worn out of conical profile or track gauge widened beyond ±2 mm | Re-profile wheels to 1:40 cone (wheel lathe, every 1.2 M km); inspect and tamp track to restore gauge; check rail fastener clip torque |
| Pantograph arcing visible as continuous sparking at 300 km/h | Contact wire wear below minimum cross-section or pantograph contact strip worn | Measure contact wire wear (ultrasonic or micrometer); replace below 80 mm² remaining section; inspect pantograph contact strip — replace below 5 mm thickness |
| Tunnel boom at portal exceeds 140 dB | Tunnel entrance lacks pressure-relief hood or nose geometry is suboptimal | Install flared tunnel entrance hood (20–50 m) with ventilation slots; verify train nose is within design profile |
| Slab track shows longitudinal cracking after 5 years | Differential subgrade settlement exceeding 5 mm per 10 m chord, or thermal stress in continuous slab | Underpin settled area with grout injection; install expansion joints at 20–30 m intervals in new construction; monitor subgrade with quarterly survey |
| Train speed restricted below design speed on a new line | Track geometry measurements out of tolerance on commissioning | Re-run track geometry car; correct alignment by grinding rail or adjusting slab fasteners; verify transition (clothoid) spiral entry geometry |
| Excessive ballast flight damage to underframe on ballasted section at 250+ km/h | Loose ballast particles lifted by train wake | Bond ballast with polyurethane coating (50 mm depth) or convert to slab track; install bogie skirts to reduce underbody wake |
| Maglev EMS control system trips gap-fault above 200 km/h | Guideway geometric deviation exceeding 0.6 mm in a 3 m chord or thermal distortion of guideway | Re-survey guideway with laser alignment; repaint guideway white to reduce solar thermal expansion; check expansion joint function |
| Catenary contact wire tension drops below 20 kN | Tensioning weight stack frozen (winter) or compensator pulley seized | Inspect tensioning assembly seasonally; de-ice contact wire with de-icing pantograph or electrical heating current injection |
| Train energy consumption 15% above specification | Pantograph arcing losses or dirty aerodynamic surfaces | Measure pantograph contact force (measuring car); wash train nose and roof with high-pressure water at depot to remove insect and dust buildup |
| Passenger ear discomfort on transition from tunnel to open air | Pressure transient at tunnel exit exceeding 2 kPa in the cabin | Verify tunnel entrance hood ventilation slots are unobstructed; check cabin pressure-seal integrity at door gaskets and inter-car gangways |

## See Also

- [Railways](./railways.md) — Conventional track construction, gauge, rolling stock fundamentals
- [Electric Railways](./electric-railways.md) — Catenary, traction motor, and regenerative braking principles
- [Electricity](../energy/electricity.md) — Power generation and distribution
- [Iron & Steel](../metals/iron-steel.md) — Rail steel and structural steel
- [Aerodynamic Trainset Design](high-speed-rail.aerodynamic-design.md) — Vehicle shaping process
- [High-Speed Track Geometry](high-speed-rail.track-geometry.md) — Track alignment process
- [Magnetic Levitation Systems](high-speed-rail.maglev-systems.md) — Maglev process
- [Machine Tools](../machine-tools/index.md) — Precision machining for bogie and motor components

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
