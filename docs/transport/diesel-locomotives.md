# Diesel-Electric Locomotives

> **Node ID**: transport.diesel-locomotives
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`energy.internal-combustion`](../energy/internal-combustion.md), [`transport.railways`](./railways.md), [`energy.electricity.motor`](../energy/electricity.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-50+
> **Outputs**: diesel_locomotives, diesel_electric_generators
> **Critical**: No — diesel traction replaces steam with higher efficiency and lower maintenance, but the railway network itself is the critical asset

## Principle

A diesel-electric locomotive carries a large [diesel engine](../energy/internal-combustion.md) — typically a V8, V12, or V16 two-stroke or four-stroke — coupled to a generator (DC, on early units) or alternator (AC, with rectifiers, on modern units). The electrical output feeds **traction motors** mounted on the axles, one per powered axle. There is no mechanical driveshaft or gearbox between the engine and the wheels. The electrical transmission is the gearbox.

**Why no mechanical gearbox?** A locomotive must deliver full tractive effort from a standstill (starting a 5,000-tonne freight train) and still reach 100-120 km/h in road service. The ratio between stall torque and top-speed torque exceeds 20:1. A mechanical transmission capable of handling 2,000-4,500 HP would need 8-12 gear ratios, each a multi-disc clutch the size of a truck wheel, with a synchronization system that could shift under full load without shattering. No such transmission has ever proven reliable at this power level. The diesel-electric transmission sidesteps the problem entirely: the diesel engine turns at its optimal speed (typically 900-1,050 RPM governed), and the generator/motor combination provides an infinitely variable torque ratio through electrical means alone.

The torque-speed characteristic of a series-wound DC traction motor (or its AC equivalent under inverter control) is naturally hyperbolic: maximum torque at zero speed, torque decreasing inversely as speed rises, power roughly constant across the working range. This matches the locomotive's requirement almost perfectly — high force to start the train, declining force as speed builds. No other prime-mover characteristic fits as well.

## Prerequisites

- [Internal Combustion Engines](../energy/internal-combustion.md) — the diesel prime mover: high-pressure fuel injection, turbocharging, jacket-water cooling. The locomotive diesel is a direct descendant of the stationary/marine diesel, scaled to 1,000-6,000 HP.
- [Railways](./railways.md) — track infrastructure, gauge, signaling, and rolling stock that the locomotive operates on. The diesel locomotive is a drop-in replacement for the steam locomotive on the same track.
- [Electric Motors](../energy/electricity.md) — traction motor design: high-torque, thermally robust machines that can sustain 200-400% of rated current for minutes during starting without insulation failure.
- [Iron and Steel](../metals/iron-steel.md) — frame, trucks (bogies), wheelsets, and the massive cast-steel truck frames that carry 25-35 tonnes of axle load each.

## Diesel-Electric Transmission

### The Load Regulator

The core of the diesel-electric transmission is the **load regulator** (or load control), a feedback mechanism that matches generator load to engine power at every throttle notch. Without it, advancing the throttle would apply a load the engine cannot sustain, causing the diesel to lug down, smoke heavily, and stall.

The mechanical load regulator (EMD, GE classic) is a variable resistor (rheostat) in the generator exciter field circuit. A cam on the engine governor rotates a contact arm across the resistor bank as the engine responds to a throttle change. When the engineer advances the throttle:
1. The governor opens the fuel rack — more fuel to the injectors.
2. The engine begins to accelerate, but the generator load holds it back.
3. The load regulator cam rotates, increasing exciter field current, increasing generator output, increasing traction motor torque — loading the engine.
4. The regulator seeks the balance point where the engine runs at governed speed under maximum fuel without overloading.

This happens in 3-10 seconds per throttle notch. The engineer advances the throttle one notch at a time, waiting for the engine to settle before advancing again. Modern locomotives (microprocessor-controlled, Dash 2 and later) perform this matching electronically — the governor, exciter, and traction motor contactors are coordinated by a control computer that reads engine RPM, exhaust temperature, and generator voltage hundreds of times per second.

### Generator and Alternator

Early diesel-electrics (1920s-1960s) used a **DC generator** directly coupled to the diesel engine. The generator output is controlled by varying the excitation (field current) of the generator — the engine governor and the generator exciter are linked so that at any engine speed, the generator absorbs exactly the horsepower the engine can deliver without lugging down or over-speeding. This load-matching is the heart of the diesel-electric transmission. A DC generator of 1,000-2,000 kW is a large machine: 1.5-2.0 m diameter, 3-4 tonnes, with a commutator and brushgear that require regular maintenance. The commutator — a cylinder of copper segments insulated by mica, rotating under carbon brushes carrying 2,000-6,000 A — must be turned (machined) periodically to remove grooving and uneven wear, a shop-level operation requiring a wheel lathe or a portable grinder.

Modern locomotives (1960s onward) use an **AC alternator** with a rotating rectifier (silicon diodes mounted on the rotor) producing DC for the traction motors. The alternator is simpler and more reliable than the DC generator — no commutator, no brushes carrying full armature current. The slip rings on the alternator carry only the field excitation current (10-50 A), not the full armature output. The alternator can also be built larger for the same physical envelope because the absence of a commutator frees the rotor end. On AC-traction locomotives (post-1990s), the DC from the rectifier is inverted back to variable-frequency AC for the AC traction motors — the extra conversion stages pay for themselves in motor robustness and wheel-slip performance.

### Traction Motor Characteristics

The traction motor is geared to the axle (gear ratio typically 60:15 to 85:19, single-reduction). At standstill, the motor draws maximum current (limited only by the resistance of the armature and the series field) and delivers maximum torque — the **starting tractive effort**. As the locomotive accelerates, the motor's back-EMF rises, current falls, and torque decreases. At some speed the motor reaches its voltage limit; beyond that, field weakening (shunting the series field with a diverter resistor, or reducing field excitation on a shunt-wound machine) extends the speed range at the cost of some torque.

A series-wound DC traction motor on a freight locomotive sustains:
- **Continuous rating**: 400-800 kW per motor, sustained indefinitely without overheating
- **Short-term rating**: 150-300% of continuous for 5-10 minutes (starting a heavy train)
- **Stall current**: 3-5× continuous — must be limited by wheel-slip detection or the motor and its cabling will burn out

**AC traction motors** (synchronous reluctance or induction, fed by variable-voltage variable-frequency inverters) have largely replaced DC on new locomotives since the 1990s. AC motors are more robust (no brushes, no commutator, simpler insulation), offer higher adhesion (the inverter can control each axle independently at sub-Hz resolution), and allow full rated torque down to zero speed indefinitely. The GE AC4400CW and the EMD SD70MAC/SD70ACe are the archetypal AC-traction freight locomotives.

## Adhesion and Tractive Effort

A locomotive can only pull as much as its wheels can transmit to the rail without slipping. The limiting force is **adhesion**: the product of the weight on driven wheels (adhesive weight) and the coefficient of friction between steel wheel and steel rail.

- **Adhesive weight**: The portion of the locomotive's total weight carried by driven axles. A road-switcher with all axles powered (Co-Co or Bo-Bo arrangement) has 100% adhesive weight. A 130-tonne, 6-axle unit places ~21.7 tonnes on each axle.
- **Coefficient of adhesion**: Dry rail, clean wheels: 0.25-0.30. Wet rail: 0.18-0.22. Greasy or frost-covered rail: 0.10-0.15. Sanded rail (sand dropped ahead of the driving wheels): up to 0.30-0.35 on dry rail, restoring adhesion on wet rail.

The **maximum tractive effort** at the rail is adhesive weight × coefficient. For a 130-tonne, 6-axle locomotive on dry rail: TE = 130 × 0.25 = 32.5 tonnes-force (~319 kN). This is what the locomotive can exert before the wheels break loose and spin. The **continuous tractive effort** is lower — the torque the motors can sustain without overheating, typically 250-350 kN on a 3,000-4,000 HP unit.

### Wheel Slip Control

Wheel slip occurs when the applied torque exceeds the adhesion limit. An uncontrolled slip is destructive: the wheel spins, flats (flat spots) grind into the tire, the rail is burnished or gouged, and the traction motor over-speeds and may throw windings. Every locomotive since the 1930s has a **wheel-slip detection** system.

Early systems detect slip by comparing axle speeds — a faster-rotating axle is slipping. The detector cuts power to that motor momentarily (drops the contactor), the wheel grabs, and power is reapplied. This is effective but crude: the tractive effort oscillates, and on poor rail the system cycles continuously.

Modern systems (post-1970s, electronic) measure the rate of change of axle acceleration, not just speed difference. A wheel that is *about* to slip shows a tiny angular acceleration before the speed diverges measurably. The inverter or generator exciter reduces torque to that axle within milliseconds, holding it just below the slip threshold. This **creep control** extracts 5-15% more tractive effort than the old bang-bang systems and produces far less wheel/rail wear. AC traction with per-axle inverters (GE AC4400CW, EMD SD70ACe) is the state of the art: each axle is controlled independently, and the locomotive can keep pulling when one or two axles are on a greasy patch.

## Multiple-Unit Operation

A single locomotive has a fixed power and tractive effort limit. To move heavier trains (or to distribute power through the train for grade-climbing efficiency), multiple locomotives are coupled and operated as one from the leading cab. This is **multiple-unit (MU) control**.

The MU system runs a **train line** — a multi-conductor cable (the 27-point standard plug, or the modern 9-wire standard) along the locomotives, carrying:

- **Throttle position** (notches 1-8): the lead locomotive's throttle commands all units to the same notch simultaneously
- **Forward/neutral/reverse**: direction control
- **Dynamic brake**: commands all units into dynamic braking together
- **Alarm and sanders**: emergency stop and sand application synchronized across all units

Each locomotive's governor, generator exciter, and traction motor contactors respond to the train-line signals independently. The lead engineer operates one set of controls; the trailing units respond as if their cabs were manned. With MU control, a 15,000-tonne coal train may have three or four 4,000-HP units at the head end (12,000-16,000 HP total), or distributed power with units at the head, mid-train, and rear — all controlled from the lead cab over a radio link (radio distributed power, RDP).

MU operation demands **load matching**: all units must share the train's resistance in proportion to their power. A mismatched consist (one weak unit among three strong ones) will have the strong units dragging the weak one, whose traction motors may be pushed above their voltage ratings. MU compatibility standards (AAR standard in North America, UIC in Europe) ensure that locomotives of different manufacturers can be combined.

## Power Range and Classes

Diesel-electric locomotive power spans 1,000-6,000 HP, sized to the service:

| Power class | HP range | Typical service | Example models |
|-------------|----------|-----------------|----------------|
| Switcher | 1,000-1,500 | Yard switching, low-speed hump work | EMD SW1500, NW2 |
| Light road-switcher | 1,500-2,000 | Branch line freight, local passenger | ALCO RS-3, EMD GP7/GP9 |
| Medium road freight | 2,500-3,000 | Mainline freight, secondary passenger | EMD GP38-2, GP40 |
| Heavy road freight (DC) | 3,000-4,000 | High-speed intermodal, unit trains | EMD SD40-2, GE Dash 9-40CW |
| Heavy road freight (AC) | 4,300-4,500 | Heavy unit trains (coal, grain) | GE AC4400CW, EMD SD70ACe |
| High-speed passenger | 4,000-4,500 | Intercity passenger (HSP-46, Charger) | Siemens Charger SC-44 |
| High-power special | 6,000+ | Heavy haul, extreme grades | EMD SD90MAC-H (6000 HP) |

### Notable Models

- **EMD GP7/GP9** (1949/1954): the archetype road-switcher. 1,500 HP, B-B truck arrangement (four powered axles), EMD 567 two-stroke diesel. Over 7,000 built — the locomotive that dieselized North American railroads. The GP9 at 1,750 HP was the workhorse of the 1950s-1960s.
- **ALCO RS-3** (1950-1956): 1,600 HP, competitor to the GP7. ALCO's 244-series four-stroke diesel. Beloved for its distinctive exhaust sound and its willingness to lug; less reliable than EMD but capable.
- **EMD SD40-2** (1972-1989): the most successful road freight locomotive ever built — nearly 4,000 units. 3,000 HP, C-C trucks (six powered axles), EMD 645E3 two-stroke V16. The -2 suffix denotes the modular electrical cabinet (Dash 2) that standardized control and simplified maintenance. Many remain in service 40+ years after construction.
- **GE Dash 9-40CW** (1994-2004): 4,000 HP, C-C, GE 7FDL four-stroke V16. Dash 9 series introduced microprocessor control and wide-nose safety cabs. Defined the modern North American freight locomotive.
- **GE AC4400CW** (1993-2007): 4,400 HP with AC traction motors. The AC version of the Dash 9. Higher adhesion (up to 0.40 coefficient with creep control vs. 0.25 for DC) makes it the locomotive of choice for heavy coal and grain trains in mountainous territory.
- **Siemens Charger SC-44** (2017-): 4,400 HP, modern passenger locomotive. Cummins QSK95 four-stroke V16, AC traction, 200 km/h top speed. Used on Amtrak state-corridor services and VIA Rail.

## Auxiliary Systems

Beyond the prime mover and traction equipment, a diesel-electric locomotive carries a set of auxiliary systems essential to operation:

- **Air compressor**: Two-stage reciprocating compressor ( Gardner-Denver or WABCO type), driven off the engine or an electric motor. Provides compressed air at 8-10 bar for the train brake system, locomotive brake, sanders, and pneumatic controls. Capacity 300-800 L/min free air. Main reservoir 500-1,000 liters. Without air pressure, the train brake cannot apply or release.
- **Radiator and cooling**: The diesel engine rejects 60-80% of its fuel energy as heat — jacket water and exhaust. A locomotive radiator (roof-mounted or side-mounted, 50-150 m² fin area) dissipates 1,500-3,000 kW of waste heat. Cooling fans (1-3 large axial fans, 1.0-1.5 m diameter, belt or electric driven) draw air through the radiator core. In hot climates, a locomotive may be derated 10-20% at ambient temperatures above 40°C due to cooling limits.
- **Cab heating and pressurization**: The cab is pressurized (slight positive pressure from the engine intake fan) to keep out dust and fumes. Cab heater uses engine jacket water or an electric element.
- **Battery and starting**: A bank of lead-acid cells (32 V or 64 V, 8-16 cells of 500-1,000 Ah each) provides starting current for the diesel engine. The starter motor draws 1,000-3,000 A for 10-30 seconds to crank the V16 engine. A low battery is the most common cause of locomotive failure to start.
- **Control air and electrical**: A 72 V DC control circuit (separate from the traction circuits) operates the contactors, relays, lights, and MU train line. Powered by an auxiliary generator (or the battery, charged by an auxiliary alternator).

## Engine Types: Two-Stroke vs Four-Stroke

Two distinct diesel engine families dominate locomotive history:

**EMD two-stroke** (General Motors Electro-Motive Division): The 567, 645, and 710 engine families. Two-stroke, uniflow scavenged (exhaust valves in the cylinder head, scavenge air ports in the liner), Roots-blown or turbocharged. The two-stroke cycle produces one power stroke per revolution per cylinder (vs. one per two revolutions for four-stroke), giving high power density for a given displacement. The EMD 645E3 V16 (3,000 HP) and 710G3 V16 (4,000 HP) are the archetypal freight locomotive engines. Two-strokes are noisier and less fuel-efficient than four-strokes but are mechanically simpler and more tolerant of poor maintenance.

**GE/ALCO four-stroke**: The GE 7FDL (V12 or V16, 3,000-4,500 HP), the ALCO 244/251 series (V12 or V16, 1,000-3,000 HP), and the modern Cummins QSK95 (V16, 4,400 HP). Four-strokes produce one power stroke per two revolutions per cylinder. Quieter, more fuel-efficient, and cleaner-burning than two-strokes. The modern trend is entirely toward four-strokes (Cummins, GE GEVO series) as emission standards tighten and fuel costs rise.

For a bootstrapping economy, the four-stroke is the easier engine to manufacture: lower peak cylinder pressures (no scavenging blow-down), standard valve gear (not the complex uniflow port/valve arrangement of the two-stroke), and wider tolerance bands on fuel injection timing. The two-stroke's advantage — more power per cylinder — matters less when the locomotive fleet is small and fuel efficiency is the priority.



The road-switcher layout — a single hood with engine and generator, a cab at one end, and a full-length walkway on the outside — was the breakthrough that made the diesel locomotive practical. See [Road-Switcher Design](./diesel-locomotives.road-switcher-design.md) for the layout rationale.

Key elements:
- **Hood**: covers the engine, generator/alternator, compressor, and auxiliary equipment. Walkway along the top for inspection. Access doors on both sides.
- **Cab**: at one end (A-unit, for single-cab operation) or both ends (for bi-directional operation without turning). Modern wide-nose cabs (North American safety cab) provide crush protection and better visibility.
- **Trucks (bogies)**: two-axle (B) or three-axle (C) trucks, each with traction motors on all axles. Cast-steel truck frames (one-piece casting, 5-10 tonnes) carry the locomotive weight and transmit tractive and braking forces to the frame.

## Dynamic Braking

On long downgrades, friction brakes alone would overheat and fade. Dynamic braking converts the train's kinetic energy into electrical energy via the traction motors (acting as generators), dissipating it as heat in a resistor grid on the locomotive roof. See [Dynamic Braking](./diesel-locomotives.dynamic-braking.md).

Dynamic braking extends brake shoe life by 5-10×, prevents thermal cracking of wheels from overheated shoes, and allows sustained descending speeds on 2-3% grades without stopping to let brakes cool. On a 1,500-tonne train descending a 2.5% grade for 20 km, dynamic braking can dissipate 4-6 MW continuously — far beyond the capacity of any friction brake.

## Operations and Fuel

### Fuel Consumption

A diesel-electric locomotive's fuel consumption is roughly proportional to power output. Typical figures:
- Switcher (1,500 HP): 100-150 liters/hour at full power
- Road freight (3,000 HP, SD40-2): 200-280 liters/hour at full power (notch 8)
- High-power AC (4,400 HP, AC4400CW): 300-400 liters/hour at full power
- At idle: 5-15 liters/hour (engine turning 200-300 RPM, no load)

A 3,000 HP unit on a 1,000 km mainline run at an average of 60% power burns approximately 2,000-2,800 liters of diesel. Fuel tank capacity: 4,000-12,000 liters (sufficient for 800-1,500 km range). Fuel is measured by the locomotive's fuel gauge (tank level sensor) and reconciled against dispatched fuel at each terminal.

### Fuel Quality

Locomotive diesel is typically No. 2 diesel (distillate fuel oil), with cetane number 40-55, viscosity 2-4 cSt at 40°C, and sulfur content below 15 ppm (ULSD) in modern practice. Higher sulfur fuels (up to 500 ppm or 5,000 ppm) were historically used and are acceptable in older engines, but they increase corrosive wear of piston rings and cylinder liners from sulfuric acid condensation in the exhaust. For a bootstrapping economy, any distillate fuel in the diesel-kerosene boiling range (150-380°C) with a cetane number above 35 will run a locomotive diesel — the engine tolerates wide fuel variation better than a high-speed automotive diesel.

### Maintenance Cycle

- **Daily (pre-departure inspection)**: Check oil and water levels, fuel gauge, brake pipe pressure, sanders, lights, horn, wheel-slip alarm. Walk around the locomotive — inspect for leaks, loose parts, hot bearings.
- **Monthly (inspection, 30 days)**: Change lubricating oil (600-1,000 liters, changed every 90-180 days depending on oil analysis). Inspect traction motor brushgear (DC) or inverter cooling (AC). Check commutator/brush wear (DC motors). Grease axle bearings, traction motor bearings, and gear cases. Inspect wheels for flats and shelling.
- **Annual (annual inspection)**: Full brake test (train line pressure drop, brake cylinder travel). Clean and inspect generator/alternator. Test wheel-slip and dynamic brake systems. Ultrasonic test of axles and wheels for cracks. Calibrate load regulator and governor.
- **Shop (3-6 years)**: Major overhaul. Engine rebuild (cylinder liners, pistons, bearings, fuel injectors). Traction motor refurbishment (rewind if necessary). Truck overhaul (reline brakes, re-turn or replace wheels). Paint and corrosion repair.

## Economic Comparison: Diesel vs Steam

| Parameter | Steam locomotive (2-6-2, 1,500 HP) | Diesel-electric (1,500 HP switcher) |
|-----------|:-----------------------------------:|:------------------------------------:|
| Fuel consumption | 2-5 kg coal/HP/hour + 5-10 kg water/HP/hour | 0.15-0.22 liters diesel/HP/hour |
| Fuel cost per 1,000 km | 7-15 tonnes coal + 30-75 m³ water | 2,000-2,800 liters diesel |
| Crew | Driver + fireman (+ helper engine crew if MU) | Driver only (conductor on train) |
| Availability | 50-70% (daily boiler maintenance) | 90-95% |
| Water stops | Every 50-80 km | None |
| Shop overhaul | 2-5 years (boiler work) | 3-6 years (engine/mechanical) |
| Thermal efficiency | 6-8% | 25-30% |

The diesel's 3-4× efficiency advantage, combined with the elimination of water stops, coaling stages, and fireman labor, repays the higher capital cost within 5-10 years of operation. For a bootstrapping economy, the question is whether the diesel engine manufacturing capability and the petroleum refining capability exist — if they do, dieselization is overwhelmingly favorable. If not, steam remains viable using local coal and water.

## Materials

| Component | Material | Specification | Notes |
|-----------|----------|---------------|-------|
| Locomotive frame | Cast or fabricated steel | One-piece cast or welded plate frame, 15-30 tonnes | Carries all equipment; must withstand buff/draft forces of 1,000-2,000 kN |
| Truck frames | Cast steel | One-piece bolster and side frame castings | 5-10 tonnes per truck; the most demanding steel casting in the locomotive |
| Wheelsets | Forged steel tires on cast steel centers | 914-1,016 mm (36-40 in) diameter, AAR Class C | Tire hardness 300-360 HB; re-turned at 3-5 mm wear |
| Traction motors | Steel laminations, copper windings | 400-800 kW continuous, class H insulation (180°C) | Series DC or 3-phase AC induction |
| Generator/alternator | Steel laminations, copper | 1,000-4,500 kW | DC generator (early) or brushless alternator (modern) |
| Carbody (hood) | Steel plate, 3-6 mm | Welded to frame | Houses engine room |
| Resistor grid (dynamic brake) | Stainless steel ribbon | 2-6 MW dissipation capacity | Roof-mounted, fan-cooled |
| Axle bearings | Roller bearings (tapered or cylindrical) | 150-250 mm bore journal | Grease-lubricated, sealed for life |

## Strengths

- **Thermal efficiency**: 25-30% (diesel-electric) vs. 6-8% (steam). A diesel locomotive burns 1/4 to 1/3 the fuel of a steam locomotive of equivalent power. No coal or water logistics — diesel fuel is pumped, not shoveled.
- **No water stops**: A diesel locomotive carries 4,000-12,000 liters of fuel (enough for 800-1,500 km) and no boiler water. Eliminates the water-column infrastructure every 50-80 km that steam railways required.
- **MU capability**: Multiple units operated from one cab — a 3-unit consist delivers 9,000-13,500 HP from a single engineer. Steam locomotives required a separate crew on each helper engine.
- **High availability**: A diesel locomotive is available 90-95% of the time (excluding scheduled maintenance). A steam locomotive was available 50-70% — the rest was in the shop for boiler washout, tube cleaning, and running-gear adjustment.
- **Dynamic braking**: Eliminates brake-shoe wear on downgrades and allows sustained speed on mountain grades. Steam locomotives had no equivalent.
- **Electric transmission**: Infinitely variable torque ratio with no gear shifting. The diesel engine runs at constant speed, maximizing efficiency and life.

## Weaknesses

- **Petroleum dependency**: Diesel fuel supply chain is the single largest operational dependency. A steam locomotive can burn wood or coal; a diesel cannot. Fuel cost is 20-35% of operating cost.
- **Complexity**: A diesel-electric locomotive has an engine, generator, traction motors, control system, compressor, and auxiliary equipment — far more complex than a steam locomotive. Requires skilled maintenance and a parts supply chain.
- **Electrical maintenance**: Commutators, brushgear (on DC), inverters (on AC) are specialized components. Insulation failure in a traction motor requires shop-level rewinding — not a field repair.
- **High initial cost**: A diesel-electric locomotive costs 2-3× the equivalent steam locomotive. The payoff comes in fuel savings, crew reduction, and higher utilization — but the capital barrier is real for a bootstrapping economy.
- **No regenerative braking** (without an overhead electric line): Dynamic braking dissipates the energy as heat. On electrified lines, regenerative braking can return 15-25% of energy to the grid.

## Safety

- **Engine room hazards**: Hot exhaust manifolds (200-400°C), turbocharger spinning at 15,000-25,000 RPM, pressurized fuel lines (150-300 bar). Fire suppression systems (CO₂ or dry chemical) required. Never enter the engine room with the engine running without hearing protection (105-115 dB).
- **High voltage**: Traction circuits carry 600-1,000 V DC (or up to 1,400 V AC on modern units). Contact is lethal. Lock-out/tag-out before any work on traction equipment.
- **Wheel slip at low speed**: If a wheel slips at standstill under high throttle, the wheel can spin up and the motor throw windings within seconds. Wheel-slip indicators in the cab must be observed.
- **Dynamic brake resistor grid**: 200-600°C during operation. Roof access prohibited during dynamic braking.
- **Battery hazards**: 32-74 V DC starting batteries (lead-acid, 1,000-2,000 Ah). Short-circuit current exceeds 10,000 A — can melt tools and cause severe burns.
- **Fuel spill fire**: Diesel fuel spills on hot engine surfaces can ignite. Fuel spills in the engine room must be cleaned immediately.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Loss of power, engine lugs (RPM drops when throttle advanced) | Generator overloading engine — exciter or load regulator out of adjustment | Check load regulator linkage; verify exciter field current; adjust governor to match engine power to generator load |
| Traction motor overheating (thermal alarm) | Continuous high-current operation beyond motor rating, or blocked cooling blower | Reduce throttle; check motor cooling air path; if alarm persists, isolate the affected motor (cut out the traction motor contactor) |
| Wheel slip alarm continuous, cannot start train | Rail wet or greasy, adhesion below 0.15, or sanders empty | Apply sanders manually; reduce throttle to notch 2-3 and allow train to start slowly; refill sand boxes at next opportunity |
| Dynamic brake ineffective | Resistor grid blower motor failed, or grid contactor not closing | Check grid blower operation; inspect contactor; do not rely on friction brakes alone on sustained downgrades — stop and inspect |
| Engine fails to start | Battery voltage low, or fuel prime lost | Check battery voltage (>24 V for 32 V system under load); prime fuel system; check emergency fuel shutoff is not tripped |
| Alternator excitation failure, no traction power | Voltage regulator failed, or exciter brushes worn | Check exciter brush wear; test voltage regulator; carry spare regulator in locomotive stores |

## Scaling Notes

The minimum viable diesel-electric locomotive is a 1,000-1,500 HP switcher (EMD SW-class equivalent) suitable for yard work and short transfer freight. This requires:
- A reliable diesel engine of 800-1,200 HP continuous (see [Internal Combustion](../energy/internal-combustion.md))
- A DC generator or alternator of 600-900 kW
- Four DC traction motors of 150-250 kW each
- [Steel castings](../metals/iron-steel.md) for the truck frames and wheelsets
- Electrical cable, switchgear, and resistors

Scaling to mainline road service (2,500-4,500 HP) requires proportionally larger components and the addition of dynamic braking, wheel-slip control, and MU capability. The jump from DC traction to AC traction (inverter-fed induction motors) is a separate technology step requiring solid-state power electronics — a capability that depends on the semiconductor supply chain and is therefore reserved for a later industrial stage.

## See Also

- [Internal Combustion Engines](../energy/internal-combustion.md) — the diesel prime mover fundamentals
- [Railways](./railways.md) — track infrastructure and operations (not duplicated here)
- [Electricity](../energy/electricity.md) — traction motor and generator principles
- [Iron and Steel](../metals/iron-steel.md) — steel for frames, trucks, wheelsets, and structural components
- [Diesel-Electric Powertrain](./diesel-locomotives.diesel-electric-powertrain.md) — transmission detail
- [Road-Switcher Design](./diesel-locomotives.road-switcher-design.md) — locomotive layout and configuration
- [Dynamic Braking](./diesel-locomotives.dynamic-braking.md) — energy dissipation on downgrades

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transport](./index.md) • [All Domains](../index.md)*
