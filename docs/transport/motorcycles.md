# Motorcycles & Scooters

> **Node ID**: transport.motorcycles
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`energy.internal-combustion`](../energy/internal-combustion.md), [`energy.electricity.motor`](../energy/electricity.md), [`machine-tools`](../machine-tools/index.md), [`transport.tire-manufacturing`](./tire-manufacturing.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-40+
> **Outputs**: motorcycles, scooter_frames, motorcycle_suspensions
> **Critical**: No

## Overview

Motorcycles are the most produced motorized vehicles in history. The Honda Super Cub alone has sold over 100 million units since 1958 — more than any car, truck, or aircraft model. The motorcycle's appeal is fundamental: two wheels in line, a frame tying them together, an engine driving the rear wheel, and a rider balancing through counter-steering. This simplicity yields extraordinary fuel economy (1.5-5 L/100 km), low material cost (80-300 kg of steel and aluminum versus 1200+ kg for an automobile), and access to terrain where wider vehicles cannot travel.

This capability covers the three core processes: [frame design](motorcycles.motorcycle-frames.md), [suspension systems](motorcycles.motorcycle-suspension.md), and [powertrain integration](motorcycles.motorcycle-powertrain.md). Engine fundamentals belong to [internal combustion](../energy/internal-combustion.md); tire manufacturing belongs to [tire production](../transport/index.md) (edge deferred to a later integration wave). The motorcycle capability is about combining existing engine and material technology into a lightweight two-wheeled package with unique handling physics.

## Motorcycle Categories

**Standard (naked)**: Upright riding position, flat seat, moderate engine (250-650 cc). General-purpose machine for commuting and light touring. The Universal Japanese Motorcycle (UJM) archetype of the 1970s — inline-four engine, tubular steel frame, dual shock rear — established the pattern. Example: Honda CB series.

**Cruiser**: Feet-forward riding position, low seat height (650-700 mm), raked-out front fork (32-40° rake), large-displacement V-twin engine (800-1900 cc). Designed for relaxed pace and visual presence rather than performance. Example: Harley-Davidson Sportster (1957-present), Indian Chief.

**Sport**: Aggressive forward lean (clip-on handlebars, rear-set footpegs), full aerodynamic fairing, high-revving engine (600-1000 cc inline-four or V-twin), stiff suspension, large-diameter disc brakes. Optimized for cornering speed and track use. Steering geometry is quick (23-25° rake, 90-100 mm trail). Example: Yamaha YZF-R1, Ducati Panigale, BMW S1000RR.

**Touring**: Large fairing and luggage (panniers and top box), upright or slightly reclined position, large fuel tank (20-30 L), six-speed gearbox, shaft drive on premium models. Engine 1000-1800 cc. Designed for long-distance comfort. Example: BMW R 1200/1250 RT (boxer engine, shaft drive), Honda Gold Wing (flat-six, shaft drive).

**Dual-sport / adventure**: Long-travel suspension (200-300 mm front and rear), spoked wheels (19-21 inch front, 17-18 inch rear), high ground clearance (250-350 mm), upright riding position. Tolerates paved and unpaved surfaces. Example: BMW GS series (boxer twin, shaft drive), KTM Adventure.

**Scooter**: Step-through frame (rider does not straddle the fuel tank), engine and drivetrain enclosed in the rear swingarm (typically a continuously variable transmission, CVT), small wheels (10-16 inch). Engine 50-300 cc (mopeds ≤50 cc). Example: Vespa (Piaggio, 1946-present — pressed-steel monocoque frame), Honda Super Cub (pressed-steel backbone frame, step-through, underbone design).

**Moped**: Pedal-equipped, engine ≤50 cc, top speed ~45-50 km/h. Historically the entry point to motorized transport in countries with graduated licensing (Europe, Asia). The term "moped" derives from "motor pedal." Often legally classed separately from motorcycles.

## Steering Geometry and Physics

Motorcycle steering is governed by the front-end geometry — rake angle, trail, and wheelbase — which together determine stability, maneuverability, and the counter-steering behavior that defines motorcycle dynamics.

**Rake (caster) angle**: The angle of the steering axis (the line through the steering head bearing to the ground) from vertical. Typical values: 23-25° for sport bikes (quick steering, less stable), 27-30° for standards, 32-40° for cruisers (very stable, slow steering). A steeper rake turns more readily but demands more rider attention; a shallower rake self-centers and tracks straight with minimal input.

**Trail**: The distance between the contact patch of the front tire and the point where the steering axis meets the ground. Trail is the self-centering mechanism: as the front wheel is displaced from straight ahead, the contact patch trails behind the steering axis, generating a restoring torque that returns the wheel to center — exactly like a shopping cart caster wheel. Typical trail: 90-110 mm (sport), 100-120 mm (standard), 120-170 mm (cruiser). Too little trail (<80 mm) causes high-speed weave and tank-slapper oscillation; too much (>140 mm) makes the bike feel heavy and reluctant to turn.

**Counter-steering**: To initiate a right turn, the rider pushes the right handlebar forward — steering the front wheel momentarily to the left. The bike falls to the right due to the lateral force at the contact patch, establishing the lean. Once leaned, the front wheel turns into the curve and the bike holds the line. Counter-steering is not optional; it is the only way to steer a motorcycle above walking speed (~5-10 km/h). Riders who do not understand counter-steering cannot corner predictably. The physics: pushing the right bar turns the wheel left, the tire contact patch moves left of the center of mass, the bike rolls right, gravity pulls it into a lean, and the camber thrust of the leaned tire sustains the curve.

**Lean angle**: A motorcycle corners by leaning. At a given speed and turn radius, the lean angle (from vertical) is fixed: tan(θ) = v² / (r · g), where v is speed, r is turn radius, and g is gravitational acceleration. At 100 km/h through a 100 m radius turn, θ = arctan(27.8² / (100 × 9.81)) ≈ 38°. Sport bikes achieve 50-60° of lean with racing tires and ground-clearance optimization; cruisers are limited to ~25-30° by floorboard and exhaust clearance. The tire contact patch shrinks and moves toward the tire sidewall as lean increases, reducing available grip and requiring softer compound tires with reinforced sidewalls.

**Wheelbase**: The distance between front and rear axle centers. Short wheelbase (1300-1410 mm for sport bikes) gives quick turn-in but less straight-line stability. Long wheelbase (1500-1700 mm for cruisers and touring bikes) gives relaxed cruising stability but requires more effort to initiate direction changes. The wheelbase, combined with rake and trail, defines the machine's entire handling character — there is no "best" geometry, only geometry matched to intended use.

**Center of gravity (CoG)**: A low CoG (typically 500-600 mm above the ground for most motorcycles) makes the bike easier to balance at a standstill and reduces the effort to initiate lean. However, too low a CoG can make the bike feel "tippy" — eager to fall into turns. Sport bikes with high-mounted exhausts and fuel tanks raise the CoG slightly, improving flickability between corners. The boxer-engine BMW has a notably low CoG due to the cylinders projecting sideways below the frame — this gives a distinct, easily managed feel at low speed but reduces cornering clearance (the cylinder heads touch down at moderate lean).

### Tire Contact Patch and Grip

The tire contact patch is the only connection between the motorcycle and the road — roughly the size of two credit cards supporting the entire vehicle and rider. At rest, a sport-bike front tire contact patch is approximately 50-70 mm long × 30-40 mm wide; the rear is 70-100 mm × 50-60 mm. As the motorcycle leans, the contact patch migrates toward the tire's sidewall, where the carcass is stiffer and the tread compound may differ (dual- and triple-compound tires are harder in the center for straight-line durability, softer on the shoulders for cornering grip).

The coefficient of friction (μ) between a street tire and dry asphalt is 0.8-1.2; for racing slicks on a prepared surface, 1.2-1.7. These values are not constant: they drop sharply with surface contamination (water, dust, oil), temperature (cold tires have less grip until warmed to 60-80°C), and slide. The grip budget is shared between cornering (lateral force), braking (longitudinal deceleration), and acceleration (longitudinal force). The traction circle or "grip pyramid" describes this: total vector grip is limited — if the rider is cornering at 80% of available grip, only 60% remains for braking or throttle (by the Pythagorean sum √(0.8² + 0.6²) ≈ 1.0). Exceeding the budget causes a slide.

**Tire construction**: Bias-ply (layers of cord fabric at alternating bias angles, 30-40°) is robust and inexpensive, used on cruisers and touring bikes. Radial (cord layers at 90° to the tread, with a belt layer at 0° for stability) runs cooler, grips better, and is standard on sport bikes. Tube-type (inner tube holds air, used with spoked wheels) versus tubeless (air sealed by the rim and tire bead, used with cast wheels — lighter, and a puncture deflates slowly rather than explosively).

Tire manufacturing is referenced in [transport infrastructure](./index.md); the edge is deferred to a later integration wave. The motorcycle capability assumes tires are available as a material input.

## Frame Types

See [Motorcycle Frame Design](motorcycles.motorcycle-frames.md) for process detail. Summary of the four dominant architectures:

**Cradle frame**: Tubular steel — a single or double loop of tubes runs from the steering head down and under the engine, cradling it. The engine hangs within the frame. Used on the majority of classic machines (Triumph Bonneville, Royal Enfield Bullet) and many budget motorcycles. Steel tube (25-35 mm diameter, 1.5-2.5 mm wall) is inexpensive, forgiving of imperfections, and easily repaired. The Honda Super Cub's pressed-steel backbone is a mass-production variant: the frame is stamped from sheet steel and welded, costing far less than tube fabrication.

**Backbone frame**: A single large-section spine (box-section steel or cast aluminum) running from the steering head to the swingarm pivot, with the engine suspended below. Lighter and stiffer than a cradle frame. Used on many mopeds and small-displacement motorcycles. The Vespa uses a structural pressed-steel monocoque — the bodywork is the frame.

**Perimeter (twin-spar) frame**: Two large aluminum beams run from the steering head, around the sides of the engine, to the swingarm pivot. The engine is a stressed member, contributing to frame stiffness. Dominant on sport bikes since the 1980s (Suzuki GSX-R, Yamaha YZF). Beams are cast or extruded aluminum — light, very stiff, and expensive to manufacture. The twin-spar design minimizes frame flex during hard cornering, giving precise handling feedback.

**Trellis frame**: A triangulated lattice of short steel tubes (typically 12-20 mm diameter), joined by precision TIG welding at brazed or machined nodes. The trellis is the lightest and most aesthetically distinctive frame type, famously associated with Ducati since the 1970s. The triangulated geometry gives high torsional stiffness per unit weight. The tradeoff: trellis frames require many weld joints (each a potential stress concentration and quality variable), making consistent mass production harder than a twin-spar casting.

**Frame stiffness**: A motorcycle frame must be rigid in torsion (resisting twist between steering head and swingarm pivot) and in bending (resisting up-down flex under load) but compliant enough to absorb road vibration and feed traction information back to the rider. Too stiff and the bike feels harsh and skittish on imperfect surfaces; too flexible and it weaves unpredictably under power and braking. Target torsional stiffness: 50-150 N·m/degree for sport bikes, 30-80 N·m/degree for cruisers. The engine, when used as a stressed member (bolted solidly between frame rails), contributes 20-40% of total chassis stiffness — removing it for service significantly reduces frame rigidity.

## Suspension

See [Motorcycle Suspension Systems](motorcycles.motorcycle-suspension.md) for process detail.

**Front suspension**: The telescopic fork — two tubes sliding within outer stanchions, carrying the front wheel and brake. Spring (coil or air-assisted) and damper (oil bath with shimmed orifices) within each leg. Conventional forks have the stanchion (thicker tube) on top, sliding into the lower leg; upside-down (inverted) forks reverse this, putting the larger-diameter stanchion at the bottom (clamped in the triple clamp) for reduced unsprung weight and greater bending stiffness — preferred on sport bikes.

**Rear suspension**: Twin-shock (two shock absorbers flanking the swingarm, classic style) versus mono-shock (single shock linkage, modern style). The mono-shock reduces unsprung weight, allows progressive linkage rate (the suspension gets stiffer as it compresses), and eliminates side-to-side binding from asymmetric loading. First popularized by Yamaha (Monocross, 1970s); now standard on sport, dual-sport, and most modern motorcycles.

**Steering damper**: A hydraulic cylinder connecting the frame to the fork, resisting rapid steering oscillation. Required on sport bikes with aggressive geometry (low trail) to prevent tank-slappers — violent handlebar oscillation at high speed that can throw the rider. The damper allows slow, deliberate steering input while damping fast, involuntary movements.

**Spring rate and damping**: Front fork spring rate: 7-15 N/mm (street), 9-18 N/mm (sport). Rear shock spring rate: 70-150 N/mm, mechanically advantaged through linkage ratios. Damping converts kinetic energy to heat via oil forced through calibrated orifices — compression damping controls dive under braking, rebound damping controls how fast the fork extends after compression. Too much compression damping makes the ride harsh; too little lets the front dive excessively. Too much rebound damping causes packing (the suspension does not fully extend between bumps, gradually compressing); too little causes oscillation (the bike bounces after a bump).

## Powertrain

See [Motorcycle Powertrain Integration](motorcycles.motorcycle-powertrain.md) for process detail. Engine fundamentals belong to [internal combustion](../energy/internal-combustion.md); this section covers motorcycle-specific integration.

**Engine configurations**: Single cylinder (250-650 cc, thumping power pulse, light, cheap, used on dual-sport and budget bikes). Parallel twin (300-800 cc, narrow, smooth enough, used on many modern middleweights). Inline-four (600-1000 cc, smooth, high-revving, the classic sport-bike engine since the Honda CB750 in 1969). V-twin (600-1900 cc, two cylinders in a V — 45-90° depending on manufacturer, strong low-end torque, characterful exhaust note, used on cruisers and some sport bikes; Ducati uses 90° "L-twin"). Boxer twin (BMW R series since 1923 — two horizontally opposed cylinders, low center of gravity, air-cooled, distinctive cylinder-head protrusion).

**Final drive**: Chain (lightest, cheapest, most efficient ~96%, requires regular lubrication and adjustment every 500-1000 km, standard on sport and budget bikes). Belt (cleaner, quieter, longer service life ~80,000 km, used on cruisers and some scooters — Harley-Davidson, Buell). Shaft drive (heaviest, most expensive, nearly maintenance-free, used on touring and premium motorcycles — BMW, Honda Gold Wing). The shaft drive encloses the drive gears in oil, eliminating chain fling and adjustment, but adds unsprung weight to the swingarm and introduces torque reaction under power (shaft jacking — the rear end rises under acceleration).

**Gearbox**: Sequential constant-mesh — the rider shifts one gear at a time through a single shift drum, up or down, with no skip-shifting. Wet multi-plate clutch (bathed in engine oil, compact, self-cooling). 4-6 speeds typical. The sequential pattern (1-down, 4-6-up) is intuitive for a handlebar lever and prevents missed shifts at high rpm.

### Engine Cooling

**Air cooling**: Fins cast onto the cylinder and head increase surface area for convective heat transfer. No radiator, water pump, or coolant — simplicity itself. Used on classic designs (BMW boxer, Harley-Davidson V-twin, many single-cylinder commuters). Limitation: cooling depends on airflow, so the engine overheats in prolonged idling or slow traffic. Cylinder head temperature must stay below 220-250°C to avoid detonation and oil breakdown. Air-cooled engines run richer at idle (extra fuel as coolant) and are lower-specific-output than liquid-cooled equivalents.

**Liquid cooling**: A water pump circulates coolant (ethylene glycol + water, 50/50) through passages in the cylinder and head to a radiator (front-mounted, finned tubes). A thermostat regulates flow — closed until the engine reaches operating temperature (80-90°C), then opens. A fan behind the radiator activates at 100-105°C to pull air through when stationary. Liquid cooling permits tighter packaging, higher compression ratios, and sustained full-power operation. Standard on all modern sport bikes, most middleweights, and increasingly on scooters. The added complexity (radiator, hoses, water pump, thermostat, fan, coolant reservoir) is offset by performance and reliability gains.

### Fuel Systems

**Carburetor** (legacy, pre-2000s): Venturi effect draws fuel into the airstream proportional to airflow. Simple, repairable with hand tools, tolerant of poor fuel quality. Multiple carburetors (one per cylinder, or two for a V-twin) require synchronized adjustment — a vacuum gauge synchronizes the throttle openings so all cylinders contribute equally. Carbureted engines are less fuel-efficient and emit more pollutants than fuel-injected equivalents.

**Electronic fuel injection (EFI)** (standard since ~2000s): An electronic control unit (ECU) reads throttle position, engine rpm, intake air temperature, and oxygen content (from a lambda sensor in the exhaust). The ECU calculates the optimal fuel quantity and triggers an electromagnetic injector to spray fuel into the intake port at 2-5 bar pressure. EFI improves cold starting, fuel economy (5-15%), and emissions compliance. The tradeoff is complexity — an ECU failure stops the engine, and diagnosis requires electronic test equipment beyond simple hand tools.

## Electric Motorcycles

Battery-electric motorcycles use a [traction motor](../energy/electricity.md) and a single-speed or two-speed reduction gearbox — no clutch, no multi-speed transmission, no engine noise. The electric motor's flat torque curve (maximum torque at zero rpm) gives strong acceleration from a stop.

- **Zero Motorcycles** (USA, 2006-present): Air-cooled permanent-magnet motor, Z-Force battery pack (lithium-ion), belt drive, 100-300 km range depending on model. The largest electric motorcycle manufacturer by volume.
- **Energica** (Italy): High-performance sport bikes, liquid-cooled AC induction motor, 0-100 km/h under 3 seconds, racing-derived electronics. The basis for the MotoE World Championship spec bike.
- **Harley-Davidson LiveWire** (2019): First major-OEM electric motorcycle, permanent-magnet motor, 0-100 km/h in 3 seconds, 235 km range (city). Positioned as a premium urban commuter.

Electric motorcycles trade the refueling speed and range of ICE for simplicity (one moving part in the drivetrain), silence, and instant torque. Limiting factors are battery energy density (100-160 Wh/kg versus ~9000 Wh/kg for gasoline) and charging infrastructure. At current technology, an electric motorcycle needs 3-6 kg of battery per kg of equivalent gasoline energy storage.

**Regenerative braking**: Electric motorcycles recover kinetic energy during deceleration by running the motor as a generator, feeding current back to the battery. This extends urban range by 5-15% but does not fully compensate for the energy cost of acceleration — the recovery efficiency is 60-80% at best, and regen cannot recover energy lost to aerodynamic drag or tire rolling resistance.

**Thermal management**: High-performance electric motorcycles (Energica, LiveWire) use liquid-cooled motors and batteries to sustain high power output. Without active cooling, the motor and battery heat up under sustained load, triggering thermal derating — the ECU reduces power to protect components, resulting in sudden performance loss. Battery thermal management also affects charging speed: a cold battery charges slowly, a hot battery degrades faster.

## Manufacturing Process

Motorcycle assembly is a subset of [automotive assembly](../transport/index.md) principles, scaled to lower volumes and lower individual vehicle weight. Key operations:

1. **Frame fabrication**: Steel tube cutting, bending (mandrel bender for cradle frames), jig welding (TIG for trellis, MIG for cradle and perimeter). Aluminum perimeter frames are gravity-die-cast in two halves and welded at the steering head and swingarm pivot. Carbon fiber frames (premium, niche) require autoclave curing — outside the scope of early bootstrap capability.

2. **Engine machining**: Cylinder bore honing, crankshaft grinding, camshaft profile grinding — all requiring [precision machine tools](../machine-tools/index.md). Tolerances: cylinder bore ±10 µm, valve seat concentricity ±20 µm, crankshaft journal roundness ±5 µm.

3. **Assembly line**: Stations for frame prep, engine install, suspension install, electrical harness, bodywork, and final test. A medium-volume line (50,000 units/year) has 10-20 stations with 2-5 minutes per station. The Honda Super Cub is produced at over 1,000 units per day across multiple plants.

4. **Testing**: Rolling-road dynamometer for engine power and emissions, suspension travel check, brake function, headlight alignment. Sample-based destructive testing of welds and frame stiffness on a percentage basis.

## Aerodynamics

Aerodynamic drag dominates fuel consumption and top speed at velocities above 80-100 km/h. The drag force is F = ½ · ρ · Cd · A · v², where ρ is air density (1.225 kg/m³ at sea level), Cd is the drag coefficient, A is frontal area, and v is velocity. A naked motorcycle has Cd ≈ 0.5-0.6 and frontal area A ≈ 0.5-0.6 m²; a fully-faired sport bike reduces Cd to 0.3-0.4 with similar frontal area. At 100 km/h, the drag power required is 3-5 kW; at 200 km/h, it rises to 25-45 kW — a cubic relationship. This is why top speed scales sub-linearly with engine power: doubling power from 75 to 150 kW may raise top speed from 220 to only 260 km/h.

The rider's body position is a major drag contributor. A sport rider tucked behind the fairing reduces frontal area by 15-25% versus a sitting-up cruiser rider. Aerodynamic turbulence behind the rider (the wake) also affects following riders in group riding and racing — the slipstream effect reduces drag for the following rider by 15-30% at race speeds.

**Wind protection**: A fairing deflects airflow around the rider, reducing wind pressure on the torso (which causes fatigue on long rides) and providing weather protection. A full touring fairing with windshield reduces wind noise, keeps rain off the rider's upper body, and can include integrated lighting and luggage. Sport fairings are optimized for the tucked position and may be uncomfortable at street speeds (the rider sits upright in turbulent air behind a short screen).

## Braking Systems

Motorcycle brakes convert kinetic energy to heat through friction. The front brake provides 70-90% of stopping power during hard braking — weight transfers forward under deceleration, loading the front tire and unloading the rear. A rider who does not use the front brake effectively doubles their stopping distance.

**Disc brakes** (standard since the 1970s, pioneered by Honda CB750 Four in 1969): A steel or cast-iron rotor (250-330 mm diameter, 4-5 mm thick) is clamped by hydraulic calipers with friction pads. Single disc (front, on small motorcycles), twin disc (dual front calipers, on sport and large motorcycles), single rear disc. Caliper types: floating (single piston side, sliding on pins — economical) versus opposed-piston (2-4 pistons on each side, rigid mount — stiffer, better feel, used on sport bikes). Brake fluid (DOT 4 or DOT 5.1 glycol-ether) hydraulically transmits lever pressure; the fluid absorbs water over time (hygroscopic), lowering boiling point, and must be replaced every 1-2 years.

**Drum brakes** (legacy, pre-1970s front, still common on rear of small motorcycles and scooters): Cast iron drum with internal expanding shoes. Cheaper, less effective, prone to fade (heat buildup reduces friction). Largely superseded by discs on the front wheel.

**ABS (Anti-lock Braking System)**: A wheel-speed sensor detects impending lockup; a modulator releases and re-applies brake pressure 5-15 times per second, maintaining rolling traction. ABS reduces stopping distance on low-friction surfaces (wet, gravel) and prevents the fall that follows a front-wheel lock. Mandatory on new motorcycles over 125 cc in Europe since 2016; increasingly standard worldwide.

## Maintenance and Service

Regular maintenance is essential — a neglected motorcycle becomes unsafe rapidly due to the severity of consequences when components fail at speed.

| Interval | Task |
|----------|------|
| Daily / pre-ride | Tire pressure (front 2.0-2.5 bar, rear 2.2-2.9 bar), chain slack (20-30 mm), oil level, brake lever feel, lights |
| Every 500-1000 km | Chain clean, lubricate, and check adjustment |
| Every 5000-10000 km | Engine oil and filter change, valve clearance check (four-stroke), spark plug inspection, air filter, brake pad thickness |
| Every 20000-40000 km | Fork oil change, steering head bearing inspection, swingarm pivot lubrication, coolant change (if liquid-cooled), drive belt replacement (if belt-driven) |
| Annually | Brake fluid replacement, tire replacement (regardless of tread — rubber hardens with age, reducing grip after 5-7 years) |

## Maintenance Economics

A 125-250 cc commuter motorcycle, the most common category in Asia and the entry point globally, costs 1000-3000 USD new. Fuel consumption: 1.5-3.0 L/100 km. At 20,000 km/year and current fuel prices, annual fuel cost is a small fraction of an automobile's. Tire replacement (front and rear) every 15,000-25,000 km costs 100-200 USD for a pair. Chain and sprocket set every 20,000-30,000 km: 100-200 USD. Engine oil change every 5,000-8,000 km: 15-30 USD. The low running cost is the motorcycle's economic argument — it puts motorized transport within reach of a much larger population than any four-wheeled vehicle.

## Iconic Designs and Designers

- **Honda Super Cub (1958)**: Soichiro Honda and Takeo Fujisawa. Pressed-steel backbone frame, step-through design, 50 cc four-stroke, centrifugal clutch (no clutch lever). Over 100 million produced — the most-made motor vehicle. Its durability and simplicity make it a reference point for bootstrap-capable motorcycle design.
- **Harley-Davidson (1903-present)**: V-twin engine, cradle frame, shaft-drive optional. The longest continuously operating motorcycle manufacturer. The 45° V-twin (first 1909) established the cruiser template.
- **BMW Boxer (1923-present)**: Max Friz designed the R32 (1923) with a 837 cc horizontally opposed twin, shaft drive, and tubular steel frame. The boxer engine's cylinders protrude into the airflow for air cooling, giving the BMW its distinctive silhouette. Still in production as the R 1250 GS.
- **Ducati trellis (1970s-present)**: Fabio Taglioni's trellis frame and desmodromic valve gear (valves positively opened and closed by cam — no valve springs, enabling high rpm). The trellis frame is a Ducati signature since the Pantah (1979).
- **Vespa (1946)**: Corradino D'Ascanio for Piaggio. Pressed-steel monocoque, engine integral with rear swingarm, CVT, step-through. Over 18 million produced. Designed as affordable postwar transport — a precedent for minimalist, accessible two-wheeled vehicles.

## Materials

| Component | Material | Specification |
|-----------|----------|---------------|
| Frame (cradle) | Steel tube | 25-35 mm dia, 1.5-2.5 mm wall, CrMo 4130 or mild steel |
| Frame (perimeter) | Cast aluminum | A356-T6, 4-8 kg per beam |
| Frame (trellis) | Steel tube | 12-20 mm dia, 1.0-1.5 mm wall, AISI 4130 |
| Frame (backbone) | Pressed steel sheet | 1.5-2.5 mm, welded box section |
| Swingarm | Aluminum extrusion or steel tube | 6061-T6 or 4130 |
| Fork tubes | Chrome-plated steel | Surface hardness 60+ HRC, surface finish Ra 0.2 µm |
| Wheels | Cast aluminum or spoked steel | 17-21 inch, 1.85-3.50 inch rim width |
| Engine block | Aluminum casting | A356 or ADC12, cast iron cylinder liner |
| Crankshaft | Forged steel | 4140 or 4340, induction-hardened journals |
| Exhaust | Stainless steel | 304 grade, 1.0-1.5 mm wall |
| Bodywork | ABS or polypropylene | Injection molded, 2.0-3.5 mm wall |

## Equipment

- **Frame welding**: TIG welder (trellis, perimeter), MIG welder (cradle), welding jigs and fixtures.
- **Engine machining**: Cylinder hone, crankshaft grinder, camshaft grinder, valve seat cutter — all [precision machine tools](../machine-tools/index.md).
- **Wheel building**: Spoke wrench (spoked wheels), wheel balancer, tire changer.
- **Final assembly**: Rolling-road dynamometer, brake tester, headlight aligner.

## Limitations

- **Two-wheeled stability**: A motorcycle must be balanced by the rider at all speeds. It cannot stand unattended, carry as much cargo as a four-wheeled vehicle, or protect occupants in a collision. Fatigue, weather, and rider skill dominate the safety envelope.
- **Lean angle limits**: Cornering clearance (floorboards, exhaust, pegs) limits lean before the tire's grip does. Cruiser and touring designs corner less aggressively than sport bikes by geometry and clearance.
- **Engine air cooling**: Air-cooled engines (classic boxer, many V-twins) risk overheating in slow traffic or hot climates. Water cooling adds complexity (radiator, water pump, thermostat) but permits tighter packaging and higher specific output.
- **Chain maintenance**: Chain-driven motorcycles require cleaning, lubrication, and slack adjustment every 500-1000 km. Neglect causes rapid wear and potential breakage. Belt and shaft drives reduce this burden at higher initial cost.
- **Electric range**: Current lithium-ion energy density (100-160 Wh/kg) limits electric motorcycle range to 100-300 km versus 300-500 km for ICE. Battery weight (40-100 kg) significantly affects handling.
- **Cold and wet performance**: Tire grip drops sharply below 10°C and on wet surfaces. Cold rubber (below 5°C) can be as slippery as ice on painted lines. Heated grips and wind protection extend the usable season but do not restore warm-tire grip. Ice and snow make motorcycles effectively unusable — a fundamental seasonal limitation.
- **Cargo capacity**: A motorcycle carries 10-30 kg on the bike (tank bag, tail pack, panniers) and a rider. Towing a trailer is possible but rare and destabilizing. For goods transport, the motorcycle is limited to light parcels — a fundamental disadvantage versus a pickup truck or cargo bicycle for last-mile delivery.

## Safety & Hazards

- **Head injury**: Motorcycle riders are 25-40 times more likely to die in a crash per kilometer traveled than car occupants, with head injury the leading cause. Helmets reduce fatality risk by 37-42%. Full-face helmets exceed open-face and half-helmets in impact protection. Mandatory helmet laws correlate with 20-30% reductions in rider fatalities.
- **Road hazard vulnerability**: Potholes, gravel, wet leaves, painted lines, and train tracks cause loss of traction that a four-wheeled vehicle would absorb. A 10 cm pothole can deflect a motorcycle wheel enough to cause a fall.
- **Visibility**: Motorcycles are narrow and easily overlooked by car drivers at intersections. "SMIDSY" (Sorry, Mate, I Didn't See You) is the most common multi-vehicle crash pattern. Daytime running lights, high-visibility clothing, and lane positioning mitigate but do not eliminate the risk.
- **Braking**: Hard braking transfers weight to the front wheel, reducing rear grip. Anti-lock braking systems (ABS) prevent wheel lock — mandatory on new motorcycles over 125 cc in Europe since 2016. Without ABS, a locked front wheel drops the bike almost instantly.
- **Protective gear**: Leather or textile jacket and trousers (abrasion resistance), gloves, and over-ankle boots. Body armor (CE-rated back, shoulder, elbow, hip, knee protectors) reduces fracture risk in a slide. The gear is uncomfortable in hot weather, which reduces compliance.
- **Exhaust burns**: The exhaust header pipe reaches 400-600°C during operation and stays hot for 10-20 minutes after shutdown. Burns to the rider's leg or passenger are common — heat shields on the muffler and pipe are essential. Long pants and boots provide a critical barrier.
- **Carbon monoxide in traffic**: Riding in heavy traffic exposes the rider to elevated CO from vehicle exhaust. CO binds to hemoglobin 200× more readily than oxygen, causing drowsiness and impaired judgment at blood levels above 10%. Face masks with activated carbon reduce exposure.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Front end wobbles at 50-70 km/h (hands-off weave) | Tire imbalance, worn steering head bearings, or insufficient trail | Balance front wheel; inspect and re-torque steering head bearing (typically 15-20 N·m); check tire pressure (front 2.0-2.5 bar); if geometry altered (lowered suspension), restore standard ride height |
| Tank-slapper (violent handlebar oscillation at high speed) | Low trail geometry, abrupt throttle closure over bumps, worn rear shock | Fit a steering damper; avoid chopping the throttle in corners — maintain steady or rolling-on throttle; rebuild or replace worn rear shock absorber |
| Engine overheats in traffic (air-cooled) | Insufficient airflow over cylinder fins, lean mixture, or retarded ignition | Avoid prolonged idling — air-cooled engines need 20+ km/h airflow; richen idle mixture 1/4 turn; verify timing (typically 10° BTDC at idle); fit an oil cooler if available |
| Chain "snatches" under power ( jerky power delivery) | Worn chain and sprockets, loose chain, or worn rear shock bushings | Measure chain slack (typically 20-30 mm at the tightest point mid-span); replace chain and sprockets as a set if teeth are hooked; inspect swingarm pivot and shock bushings for play |
| Motorcycle pulls to one side under braking | Warped front disc, mismatched tire pressures, or bent fork tube | Measure disc runout (max 0.10-0.30 mm); replace warped disc; equalize tire pressures; check fork tube straightness (rotate in steering head — runout max 0.20 mm) |
| Hard cold starting (four-stroke) | Weak battery, fouled spark plug, or valve clearance out of spec | Load-test battery (minimum 9.6 V cranking); clean or replace plug (gap 0.7-0.9 mm); check valve clearances (typically 0.10-0.20 mm inlet, 0.15-0.30 mm exhaust, cold) at scheduled service |
| Clutch slips under power (rpm rises, speed does not) | Worn friction plates, weak clutch springs, or incorrect oil | Measure friction plate thickness (replace below spec, typically 2.5-3.0 mm); check spring free length; use JASO MA-rated oil (not car oil — friction modifiers cause clutch slip) |
| Rear suspension bottoms over bumps | Weak or worn rear shock, incorrect preload for load | Adjust spring preload for rider and luggage weight; rebuild or replace shock if oil is leaking; verify swingarm pivot is not worn (side play causes poor shock alignment) |
| Vespa-style scooter loses power on hills | Worn CVT drive belt or glazed variator rollers | Replace CVT belt every 15,000-25,000 km; inspect variator roller weights for flat spots (replace as a set); clean belt dust from transmission case — buildup causes slippage and heat |
| Battery discharges when parked (parasitic draw) | Alarm system, aftermarket accessories, or faulty rectifier/regulator | Disconnect battery negative terminal and measure current draw (should be <0.05 A); isolate circuit by pulling fuses; test regulator/rectifier output (13.5-14.5 V at 3,000 rpm) — a failed regulator overcharges or undercharges the battery |

## See Also

- [Motorcycle Frame Design](motorcycles.motorcycle-frames.md) — chassis process detail
- [Motorcycle Suspension Systems](motorcycles.motorcycle-suspension.md) — suspension process detail
- [Motorcycle Powertrain Integration](motorcycles.motorcycle-powertrain.md) — engine and drivetrain process detail
- [Internal Combustion](../energy/internal-combustion.md) — engine fundamentals
- [Iron & Steel](../metals/iron-steel.md) — frame and engine materials
- [Machine Tools](../machine-tools/index.md) — precision machining for engine and chassis
- [Electricity](../energy/electricity.md) — electric motorcycle motors
- [Railways](railways.md) — complementary rail transport
- [Roads & Bridges](roads.md) — road infrastructure motorcycles depend on
- [Water Transport](shipping.md) — alternative bulk transport
- [Internal Combustion](../energy/internal-combustion.md) — Otto-cycle engine fundamentals (not duplicated here)
- [Machine Tools](../machine-tools/index.md) — precision machining capability for frames and engines

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
