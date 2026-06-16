# ICE Powertrains

> **Node ID**: transport.ice-powertrains
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`energy.internal-combustion`](../energy/internal-combustion.md), [`machine-tools.gears`](../machine-tools/gears.md), [`metals.iron-steel`](../metals/iron-steel.md), [`energy.fuels`](../energy/fuels.md), [`transport.motor-vehicles`](./motor-vehicles.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-40+
> **Outputs**: transmissions, drivetrains, fuel_systems, exhaust_systems, differentials
> **Critical**: No

## ICE Powertrains

This capability covers everything **between the engine flywheel and the driven wheels**, plus the fuel supply and exhaust aftertreatment that feed and clean up the combustion process. It does **not** cover engine fundamentals (thermodynamic cycles, cylinder architecture, valve gear) — those live in [Internal Combustion Engines](../energy/internal-combustion.md). It does **not** cover gear tooth cutting, hobbing, or heat treatment — those live in [Gears & Gear Manufacturing](../machine-tools/gears.md). EV powertrains (motor + inverter + battery) are a separate, later capability.

The powertrain must solve three problems at once: (1) match the engine's narrow useful RPM band (1500-6500 RPM) to a wheel speed range of 0-1500+ RPM across vehicle speeds from crawl to highway; (2) distribute torque to the driven wheels while letting them turn at different speeds in corners; and (3) deliver combustible fuel metered to load and treat the resulting exhaust to meet emission limits.

## Powertrain Layout: Longitudinal vs Transverse

**Longitudinal (north-south) engine**: the crankshaft axis runs along the vehicle centerline. This is the natural layout for **rear-wheel-drive (RWD)** and **all-wheel-drive (AWD)**. The engine sends torque rearward through a driveshaft to a final-drive differential on the live axle. Longitudinal packaging suits inline-4, inline-6, and V8 engines. It permits a long, compliant driveshaft that isolates vibration, and it leaves room for a robust transmission case bolted to the back of the engine block. The trade-off is a passenger cabin intruded by the longitudinal transmission tunnel.

**Transverse (east-west) engine**: the crankshaft axis runs across the car. This is the natural layout for **front-wheel-drive (FWD)**, where the engine, transmission, and differential form one compact transaxle unit driving the front wheels. Transverse packaging minimizes hood length, eliminates the rear driveshaft and tunnel, and yields a flat cabin floor and more cabin volume per meter of vehicle length. It dominates compact and mid-size passenger cars. The constraint: engine length is limited by the space between the front wheels (track width), favoring inline-4 over inline-6.

**Comparison**:

| Property | Longitudinal (RWD/AWD) | Transverse (FWD) |
|----------|------------------------|------------------|
| Driven wheels | Rear (or all) | Front |
| Cabin floor tunnel | Yes (driveshaft) | No (flat) |
| Engine types | I4, I6, V8, V12 | I3, I4, V6 (short) |
| Weight distribution | ~50/50 achievable | Nose-heavy (60/40) |
| Driveshaft | Yes (long) | No (short half-shafts) |
| Torque steer | None | Present at high torque |
| Packaging length | Longer hood | Shorter hood |

## Drivetrain Configurations

**Front-Wheel Drive (FWD)**: engine and transaxle drive the front wheels. Compact, efficient (no driveshaft losses, 1-2% gain over RWD), and inherently stable under power (pulling, not pushing). The front tires must handle steering, braking, and acceleration simultaneously — they are the limiting axle for total grip. At high engine torque (>250 N·m) the unequal-length half-shafts cause **torque steer**: the steering wheel pulls to one side under hard acceleration. Equal-length half-shafts (with an intermediate shaft and bearing) suppress this. Dana and GKN produce the constant-velocity (CV) half-shafts that allow the driven wheels to steer and articulate.

**Rear-Wheel Drive (RWD)**: engine drives the rear wheels via a driveshaft and live-axle or independent rear differential. Front tires handle only steering and braking; rear tires handle only acceleration. This separation maximizes total available grip and is preferred for sports cars, trucks, and heavy vehicles. Under hard cornering, RWD can oversteer (rear steps out), which is recoverable by a skilled driver but less forgiving than FWD understeer. Dana Spicer axles and Eaton differentials are the reference suppliers for RWD trucks.

**All-Wheel Drive (AWD)**: torque sent to all four wheels through a center differential, viscous coupling, or electronically controlled clutch (Haldex, BorgWarner). AWD multiplies available traction for launch and on low-friction surfaces (snow, gravel). The open center differential must be coupled with a limited-slip or locking mechanism, otherwise a single spinning wheel on ice sinks total traction to zero. AWD adds 50-100 kg of mass and 3-8% fuel-consumption penalty from the extra gears, shafts, and bearings. Full-time AWD (Audi Quattro, Subaru Symmetrical) runs all wheels continuously; part-time AWD (Haldex) runs FWD until slip is detected, then engages the rear.

## Manual Transmissions

See [Manual Transmissions](./ice-powertrains.manual-transmissions.md) for the detailed process. The manual transmission uses a countershaft (layshaft) cluster of gears that are in constant mesh with the mainshaft gears. The driver selects a ratio by sliding a dog clutch (synchronizer) to lock the desired gear to the mainshaft. The **synchronizer** — a small cone clutch that friction-matches gear speed before the dog teeth engage — was the critical 1928 invention (Cadillac Synchro-Mesh) that made non-double-clutching shifts possible.

**Ratio spread**: a 5-speed manual might use ratios 3.5 : 1 (1st), 2.1 : 1 (2nd), 1.4 : 1 (3rd), 1.0 : 1 (4th, direct), 0.85 : 1 (5th, overdrive). The final-drive ratio (differential) then multiplies this: e.g., 3.7 : 1. Overall ratio = gear ratio × final drive.

**Efficiency**: manual gearboxes are the most efficient transmissions at **94-98%** mechanical efficiency in direct (1:1) gear, dropping to 90-95% in non-direct gears due to additional loaded mesh points. The losses are gear-mesh sliding friction, bearing drag, and oil churning.

## Automatic Transmissions

See [Automatic Transmissions](./ice-powertrains.automatic-transmissions.md) for the detailed process. The modern automatic transmission uses one or more **epicyclic (planetary) gearsets** whose ratios are selected by hydraulically applying clutches and brakes to hold or release different elements (sun, carrier, ring). All gears remain in mesh; no sliding or shifting of gears is required.

**Torque converter**: a fluid coupling between the engine and the gearbox. Three elements — impeller (pump), turbine, and stator — circulate transmission fluid. At stall (vehicle stopped, engine at idle), the converter multiplies engine torque **2.0-2.5×** as the stator redirects fluid flow. Above ~30-50 km/h a **lock-up clutch** mechanically bridges the converter, eliminating fluid slip and recovering ~3-5% fuel economy. The ZF 8HP (8-speed, used by BMW, Audi, Chrysler) and Aisin AW (8-speed, used by Toyota, Volvo) are the reference modern units, achieving 6-8% fuel-economy gains over 6-speed predecessors through wider ratio spread (7.0:1 vs 6.0:1) and more frequent lock-up operation.

**Efficiency**: automatics have historically been 5-12% less efficient than manuals due to torque-converter slip, hydraulic pump parasitic load, and added gear meshes. Modern 8-9 speed automatics with lock-up and electronic control have closed most of this gap, reaching 88-93% efficiency.

## Gear Ratio Math

The **gear ratio** of a mesh is the ratio of driven gear teeth to driving gear teeth:

> ratio = N_driven / N_driven

A pinion with 20 teeth driving a gear with 60 teeth gives ratio 60/20 = 3.0 : 1. The driven gear turns 3× slower but transmits 3× the torque (minus efficiency losses).

**Torque and speed**: for a gearset with ratio R and efficiency η:

> T_out = T_in × R × η
> ω_out = ω_in / R

**Power conservation**: power in = power out / η. For a 95%-efficient mesh, 5% of input power is lost as heat.

**Overall powertrain ratio** = transmission gear ratio × final-drive ratio. Example: 1st gear 3.5 : 1 × final drive 3.7 : 1 = 12.95 : 1 overall. An engine producing 200 N·m at 3000 RPM delivers (200 × 12.95 × 0.92) = 2383 N·m to each driven axle at (3000 / 12.95) = 232 RPM axle speed.

**Vehicle speed**: with tire rolling radius r (m) and overall ratio R:

> v (km/h) = ω_engine (RPM) × 60 × 2πr / (R × 1000)

Example: 3000 RPM engine, r = 0.31 m, R = 12.95 → v = 3000 × 60 × 2π × 0.31 / (12.95 × 1000) = 27.1 km/h in 1st gear at 3000 RPM.

**Ratio steps**: the gap between consecutive gears. Tighter steps (1.25-1.40×) keep the engine in its power band after each shift; wide steps (1.60-1.80× in older 4-speeds) drop the engine out of boost or below its torque peak. The 8-speed ZF 8HP achieves average steps of 1.34×, keeping engine RPM within a narrow useful window across all 8 gears.

## Differentials

See [Drivetrain Architecture](./ice-powertrains.drivetrain-architecture.md) for the full process. The **open differential** splits torque 50/50 between wheels while allowing them to rotate at different speeds in corners — essential, since the outside wheel travels a longer arc than the inside wheel. The penalty: if one wheel loses traction (ice, mud), the open differential sends all torque to the spinning wheel, and the vehicle stalls.

**Limited-slip differential (LSD)**: clutches, gears (Torsen), or viscous fluid resist the speed difference and bias torque to the wheel with more grip. Torque bias ratios of 1.5-4.0 : 1 are typical. Eaton produces clutch-type LSDs widely used in trucks and performance cars; the Torsen (Torque-Sensing) gear-type LSD uses worm-gear self-locking and needs no clutch wear parts.

**Locking differential**: a dog clutch rigidly locks both output shafts together, forcing equal speed. Used off-road and in heavy trucks. Unlock before turning on dry pavement or tire scrub and drivetrain stress result.

## Fuel Systems

See [Fuel & Exhaust Systems](./ice-powertrains.fuel-and-exhaust-systems.md) for the detailed process.

**Carburetor** (early technology): a venturi in the intake airstream creates low pressure that draws fuel through a metering jet. Simple, no electricity required, but imprecise — mixture varies with air temperature, altitude, and venturi wear. Superseded for emissions reasons by the 1980s.

**Port fuel injection (PFI)**: an electric pump (3-5 bar) delivers fuel through an injector nozzle into each intake port, metered by an electronic control unit (ECU) reading throttle position, manifold air pressure, oxygen (lambda) sensor, and engine speed. Precise mixture control (stoichiometric, λ = 1.00) is the foundation of modern three-way catalytic converter operation.

**Direct injection (GDI/DI)**: fuel injected directly into the cylinder at 100-250 bar. Cools the charge (allowing higher compression ratio, +1-2 points) and stratifies mixture for lean-burn at part load. The trade-off: fuel impinging on cylinder walls washes off lubricating oil, and GDI engines accumulate intake-valve carbon deposits (no fuel washing the back of the valve). Bosch and Denso are reference GDI system suppliers.

## Exhaust & Emissions Aftertreatment

The three regulated ICE exhaust pollutants are **carbon monoxide (CO)**, **unburned hydrocarbons (HC)**, and **oxides of nitrogen (NOx = NO + NO₂)**. Particulate matter (PM/soot) is a fourth, critical for diesels. Modern aftertreatment converts all of these.

**Three-way catalytic converter (TWC)**: the core gasoline-engine emissions device since the 1975 model year. A ceramic honeycomb monolith (400-900 cells per square inch) coated with a washcoat of aluminum oxide carrying precious-metal catalysts **platinum (Pt), palladium (Pd), and rhodium (Rh)** at ~1-3 g/ft³ loading. The "three ways":

1. **Oxidation of CO** → CO₂: 2CO + O₂ → 2CO₂ (Pt, Pd catalyst)
2. **Oxidation of HC** → CO₂ + H₂O: C_xH_y + (x + y/4)O₂ → xCO₂ + (y/2)H₂O (Pt, Pd)
3. **Reduction of NOx** → N₂ + O₂: 2NO → N₂ + O₂ (Rh catalyst)

The TWC only achieves >95% conversion when the air-fuel ratio is held at **stoichiometric (λ = 1.000 ± 0.005)** — this is the "closed-loop" window where the oxygen sensor feedback lets the ECU trim injection pulse width in real time. Outside this narrow window, the catalyst's oxidation and reduction functions conflict and efficiency collapses (the "catalyst window" is roughly λ = 0.99-1.01). Lead (Pb) in fuel permanently poisons the catalyst by coating the active metal sites — unleaded fuel is mandatory with a TWC.

**Diesel particulate filter (DPF)**: a wall-flow ceramic monolith (cordierite or silicon carbide) that traps soot from diesel exhaust. The channels are alternately plugged so exhaust gas is forced through the porous walls, trapping >95% of particulate mass. As soot accumulates, backpressure rises. Periodically the ECU triggers **regeneration**: injects extra fuel or uses a downstream injector to raise exhaust gas temperature to 550-650°C, oxidizing the trapped carbon (C + O₂ → CO₂). A "forced regeneration" (workshop) is needed if the filter becomes over-loaded from short-trip driving.

**Selective catalytic reduction (SCR)**: the primary diesel NOx aftertreatment. An aqueous urea solution (**AdBlue / DEF**, 32.5% urea in deionized water) is injected into the exhaust upstream of the SCR catalyst (vanadium-tungsten-titanium or zeolite/ Cu-Fe). At 200-450°C the urea hydrolyzes to ammonia:

> CO(NH₂)₂ + H₂O → 2NH₃ + CO₂

The ammonia then reduces NOx over the catalyst:

> 4NO + 4NH₃ + O₂ → 4N₂ + 6H₂O

SCR achieves 70-95% NOx reduction. The urea tank must be refilled (consumption ~3-5% of diesel volume). Without SCR, modern diesel NOx limits cannot be met.

**EVAP (evaporative emission control)**: fuel vapor (volatile HC) from the tank is vented into a canister of activated carbon that adsorbs the vapor. When the engine runs, a purge valve draws the stored vapor (plus make-up air) into the intake to be burned. Without EVAP, evaporating fuel is a major HC emission source — a hot parked car can vent tens of grams of HC per day.

## Torque, NVH, and Efficiency

**Torque multiplication**: the transmission's job is to multiply engine torque at low vehicle speed (for acceleration and grade climbing) and reduce engine RPM at high vehicle speed (for fuel economy and noise). First gear provides 10-13× overall torque multiplication (gear × final drive); top overdrive gear reduces engine RPM by 15-30% below direct drive.

**NVH (Noise, Vibration, Harshness)**: powertrain NVH originates from engine firing pulses (2nd-order in a 4-cylinder), gear-mesh frequency (N_teeth × RPM), driveline vibration (universal-joint secondary couple), and exhaust pulsation. Countermeasures: dual-mass flywheel (damps engine torsionals before the gearbox), flexible couplings in the driveshaft, helical gears (quieter than spur by 5-10 dB), and hydraulic engine mounts (isolate block vibration from chassis). Exhaust noise is attenuated by the muffler (expansion chamber and Helmholtz resonator tuning) and the catalytic converter itself (acts as a sound attenuator).

**Gear efficiency**: a single helical-gear mesh loses 1-2% to sliding friction; a typical 2-shaft transmission passes through 2-3 loaded meshes, giving 94-97% efficiency. Bearing drag (0.1-0.3% per bearing) and oil churning (0.5-2% depending on oil level and viscosity) add parasitic loss. Synthetic ATF (automatic transmission fluid) reduces churning loss vs mineral oil.

## Driveline Geometry & U-Joints

The driveshaft in a longitudinal powertrain must transmit torque through a changing angle as the live axle articulates over bumps. The **universal joint (U-joint, Cardan joint)** — a four-point cross with needle bearings on each trunnion — allows this articulation. But a single U-joint is **non-constant-velocity**: when the input and output shafts are at an angle, the output shaft speeds up and slows down twice per revolution even with constant input speed. The velocity variation follows:

> ω_out / ω_in = cos β / (1 - sin²β · cos²θ)

where β is the joint angle and θ the joint rotation angle. At 10° joint angle the speed variation is ±1.5%; at 20° it is ±6%; at 30° it is ±15%. The resulting vibration torques the differential and excites driveline resonance.

**Phasing**: the cure is to install a **second U-joint** at the other end of the driveshaft, oriented (phased) 90° out so its velocity variation cancels the first. For perfect cancellation, the input and output shafts must be parallel (equal joint angles). This is **U-joint phasing**: the yokes at each end of the driveshaft are aligned in the same plane. A mis-phased shaft (yokes 90° out) vibrates at the 2nd-order driveshaft frequency.

**Constant-velocity (CV) joints**: in FWD transaxles, the half-shafts must articulate through large angles (up to 45-50°) during steering lock while transmitting full torque. A U-joint at these angles is unusable. The **Rzeppa CV joint** (ball-and-cage, 6 balls running in matching inner and outer races) transmits torque at constant velocity through any angle within its range. The outer race splines into the wheel hub; the inner race splines onto the half-shaft. A rubber boot retains the grease. GKN is the dominant CV-joint supplier. The **tripod joint** (three rollers on needle bearings running in a tulip-shaped housing) is used on the inboard end where it accommodates plunge (axial length change) as the suspension travels.

**Driveshaft critical speed**: a long thin shaft has a bending resonance. Above this speed the shaft whips and self-destructs. Critical speed N_cr (RPM):

> N_cr ≈ 4.8 × 10⁶ × √(D² + d²) / L²

where D and d are outer and inner diameters (mm) and L is the bearing-center distance (mm). A 50 mm steel tube shaft, 1.5 m between bearings, has N_cr ≈ 5300 RPM — comfortably above passenger-car operating RPM. A truck shaft over 2 m may need a center bearing (two-piece shaft) to keep critical speed above max RPM. Aluminum and carbon-fiber shafts raise critical speed (lower density) and reduce rotating mass.

## Transmission Ratio Design

Selecting gear ratios is a trade-off between acceleration, fuel economy, and grade capability. The **overall ratio in top gear** sets highway engine RPM and thus cruising fuel consumption; the **overall ratio in first gear** sets maximum tractive effort (grade and launch capability). The product — the **ratio spread** (1st ÷ top) — quantifies how well the transmission spans these extremes.

- **4-speed automatic** (legacy): spread ~2.4-3.0 : 1, e.g., 2.5 / 0.85 ≈ 2.94. Wide ratio steps, engine drops out of power band on each shift.
- **5-speed manual**: spread ~3.8-4.5 : 1, e.g., 3.5 / 0.85 ≈ 4.12. Tighter steps, decent cruising.
- **6-speed automatic**: spread ~6.0 : 1, e.g., 4.15 / 0.67 ≈ 6.2. The first modern overdrive-equipped unit.
- **8-speed automatic (ZF 8HP)**: spread ~7.0 : 1, e.g., 4.70 / 0.667 ≈ 7.05. Ratio steps of 1.30-1.40 keep engine in its torque band; two overdrive gears (6th, 7th) plus an ultra-tall 8th drop highway RPM to 1500-1800.
- **9-speed automatic (ZF 9HP, transverse)**: spread ~9.8 : 1. Four overdrive gears; the engine lugs at <1500 RPM on the highway.

**Grade capability**: maximum grade (gradient) the vehicle can climb in 1st gear at full throttle:

> grade % = (T_engine × R_overall × η / r_rolling − F_aero − F_roll) / (m × g) × 100

A 1500 kg car, 200 N·m engine, overall 1st ratio 12.95, 92% efficiency, 0.31 m tire: tractive force = 200 × 12.95 × 0.92 / 0.31 = 7684 N. Minus rolling resistance (~150 N) and low-speed aero (~0): climbable grade = 7684 / (1500 × 9.81) × 100 = 52%. Real vehicles target 30-40% grade in 1st gear, reserving margin for clutch/torque-converter slip and payload.

## Hybrid Powertrain Bridge

While full battery-electric powertrains are out of scope here, the **hybrid** (engine + electric motor) shares much of the ICE powertrain hardware. The **mild hybrid** (48 V belt-alternator-starter, 10-15 kW) adds torque assist and regenerative braking without a separate transmission — it bolts onto the existing ICE accessory drive. The **full hybrid** (Toyota HSD / Prius, Ford eCVT) replaces the multispeed gearbox with a **power-split device** — an epicyclic gearset that sums engine and motor torque continuously via two electric motor-generators (MG1, MG2). There are no discrete gear ratios; the engine RPM is set by the gearset kinematics and the two motor speeds. This is a natural evolution of the automatic-transmission epicyclic gearset technology — same gearset, different actuation. The plug-in hybrid (PHEV) adds a larger battery and charge-depleting operation, but the powertrain architecture remains an ICE + planetary gearset + two motors.

## Materials

| Component | Material | Specification |
|-----------|----------|---------------|
| Transmission case | Aluminum alloy (A380) or cast iron | Sand/permanent-mold cast, 3-5 mm walls |
| Gear teeth | Alloy steel (8620, 9310 carburizing grades) | Case-hardened 58-62 HRC, core 30-38 HRC |
| Shafts | Forged steel (4140, 4340) | Quench & tempered, 28-34 HRC |
| Synchronizer cones | Brass or powder-metal friction lining | μ = 0.08-0.12 on steel cone |
| Torque converter | Stamped steel shells, aluminum stator | Welded assembly, turbine on needle bearings |
| Clutch friction plates | Organic/cellulose or sintered bronze on steel core | μ = 0.25-0.35 |
| Driveshaft | Steel tube (4140) or aluminum/composite | Balanced to G16 (ISO 1940) |
| CV joint cages | Bearing steel (52100) | 60-64 HRC, mirror-finish raceways |
| Differential carrier | Ductile cast iron (65-45-12) | Sand cast, machined bores |
| Ring & pinion | Forged alloy steel (8620) | Carburized, lapped as a matched set |
| Catalyst substrate | Cordierite ceramic honeycomb | 400-600 cpsi, 0.10-0.15 mm wall |
| Catalyst washcoat | γ-Al₂O₃ with Pt/Pd/Rh (1-3 g/ft³) | Washcoated, precious-metal loaded |

## Equipment

- **Gear cutting**: [hobbing machines](../machine-tools/gears.md), shapers, shavers, grinders for gear finishing.
- **Heat treatment**: carburizing furnaces (gas or vacuum), quench tanks, tempering ovens for case-hardened gears.
- **Transmission assembly**: clean assembly room, press for bearing installation, leak-test stand, run-in dynamometer.
- **Driveline balancing**: driveshaft balancing machine (weld-on correction weights).
- **Emissions test**: chassis dynamometer with constant-volume sampling (CVS) and exhaust-gas analyzer (NDIR for CO/CO₂, FID for HC, chemiluminescence for NOx).

## Bootstrapping Path

A bootstrap civilization reaches ICE powertrains only after [internal combustion engines](../energy/internal-combustion.md), [iron & steel](../metals/iron-steel.md), [precision gear cutting](../machine-tools/gears.md), and [refined petroleum fuels](../energy/fuels.md) are all in hand — roughly the late 19th-century technological baseline. The earliest practical powertrain is a **sliding-mesh 2- or 3-speed gearbox** with an open differential and chain drive to a live rear axle (essentially the 1890s Panhard layout): no synchronizers, no torque converter, no emissions control. The driver double-clutches every shift; reverse is a sliding idler.

The next step adds **synchromesh** (1920s), giving manageable shifting for untrained drivers, and **hydraulic brakes** for the higher speeds the better transmissions enable. The **automatic transmission** (1940 Oldsmobile Hydra-Matic) requires hydraulic pump technology, precision casting of the epicyclic gearsets, and friction material that survives in hot ATF — a substantial industrial investment beyond the manual gearbox. **Fuel injection** (1957 Bosch, mechanical; 1980s electronic) needs electronics, magnetic injectors, and an oxygen sensor (zirconia electrochemical cell). The **catalytic converter** (1975) requires platinum-group metals (Pt, Pd, Rh), ceramic monolith extrusion, and unleaded, low-sulfur fuel. Each emissions-control tier represents a measurable industrial-capability step; a bootstrap civilization builds them in this sequence, not all at once.

## Limitations

- **Engine dependence**: this capability assumes a working [internal combustion engine](../energy/internal-combustion.md); without it, there is nothing to connect to the wheels.
- **Precision machining**: gears and shafts need [machine tools](../machine-tools/gears.md) capable of 0.01 mm tolerance — pre-machine-tool civilizations cannot produce a useful multispeed gearbox.
- **Fuel quality**: catalytic converters and high-pressure fuel systems need [refined petroleum](../energy/fuels.md) (gasoline/diesel) of controlled octane/cetane and zero lead/sulfur — sulfur poisons catalysts.
- **Maintenance burden**: automatic transmissions need fluid service (40,000-100,000 km); DPF and SCR need active regeneration and urea refill; CV joints need boot integrity (torn boot = joint failure in hundreds of km).
- **Weight penalty**: a full ICE powertrain (engine + transmission + driveline + fuel + exhaust) adds 300-500 kg versus an equivalent EV powertrain, with the fuel mass adding further payload.

## Safety & Hazards

- **Transmission fluid flammability**: ATF auto-ignites at ~300°C; a fluid leak onto a hot exhaust manifold ignites. Route fluid lines clear of exhaust; shield the manifold.
- **Driveshaft failure**: a failed universal joint or fractured driveshaft at speed flails the shaft into the floor pan or road — catastrophic. Inspect U-joints for play; balance driveshafts after any modification.
- **Catalyst fire risk**: the catalyst monolith reaches 400-800°C in operation. Parking over dry grass ignites it. Maintain 200 mm ground clearance and a heat shield under the catalyst.
- **Urea handling (AdBlue)**: mild irritant; ammonia vapor release on spill. Store above -11°C (freezing point); the tank includes a heater for cold climates.
- **High-pressure fuel**: GDI systems run at 100-250 bar — a pinhole leak injects fuel through skin (fluid injection injury). Depressurize before opening any fitting.
- **Pinch points**: rotating driveshafts, fan blades, and belt drives amputate fingers and snag clothing. Guards required; never service a running engine.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Gear clash on manual downshift | Synchronizer cone worn below 0.05 mm friction thickness | Rebuild synchronizer assembly; replace brass cones; use correct GL-4 gear oil (not GL-5 which attacks yellow-metal cones) |
| Automatic transmission slips in reverse | Low ATF or worn reverse clutch pack | Check fluid hot on level ground (pink/red, not brown/burnt); if low, find leak (cooler line, pan gasket); if brown and slipping, clutch rebuild required |
| Torque converter shudder at 40-60 km/h on lock-up | Lock-up clutch friction material contaminated or TCC solenoid sticking | Flush ATF and replace filter; if persists, replace converter; verify ECU lock-up duty-cycle command |
| Differential whine on deceleration | Ring-and-pionion backlash out of spec (should be 0.15-0.25 mm) or worn bearings | Reset backlash with select shims; re-lap as matched set; replace carrier or pinion bearings if pitted |
| CV joint clicking on tight turns | Torn CV boot → grease loss → water/debris ingress → bearing pitting | Replace boot immediately on tear (before joint damage); if clicking present, replace joint; repack with moly grease |
| DPF blocked / vehicle in limp mode | Excess soot from short trips preventing regeneration | Force regeneration via diagnostic tool (30 min at 600°C); if ash-loaded (>200k km), replace or clean filter off-vehicle |
| MIL / CEL with P0420 catalyst efficiency code | Catalyst substrate melted or precious metal poisoned (lead/sulfur/phosphorus) | Replace catalyst; verify air-fuel ratio stays at λ = 1.00 (pre- and post-cat O₂ sensors should differ); fix any coolant or oil consumption poisoning source |
| SCR NOx efficiency low (P20EE) | DEF contamination, crystalized injector, or aged catalyst | Verify DEF is 32.5% urea (refractometer); clear crystallized injector with hot-water flush; replace SCR catalyst if conversion <70% |
| Fuel smell / EVAP leak code (P0442 small leak) | Loose or faulty gas cap, cracked vapor hose, failed purge valve | Tighten/replace gas cap (click once); smoke-test vapor system to locate leak; test purge valve solenoid for stuck-open |
| Hard starting after hot-soak (vapor lock) | Fuel boils in injection line near hot engine | Route fuel lines away from exhaust; ensure fuel-system return line or reroute; modern EFI systems rarely vapor-lock |
| Vibration at highway speed, increases with speed | Driveshaft out of balance or U-joint phasing wrong | Check U-joint yokes are in-plane (phased); balance shaft to G16 (ISO 1940); inspect center bearing on two-piece shafts; verify joint angles equal at both ends (parallelism) |

## See Also

- [Internal Combustion Engines](../energy/internal-combustion.md) — engine fundamentals, thermodynamic cycles, cylinder architecture
- [Gears & Gear Manufacturing](../machine-tools/gears.md) — gear cutting, hobbing, heat treatment
- [Iron & Steel](../metals/iron-steel.md) — transmission case and gear steel
- [Fuels](../energy/fuels.md) — gasoline, diesel, and refining
- [Railways](./railways.md) — rail-specific powertrains (steam/diesel-electric, no multispeed gearbox)
- [Roads & Bridges](./roads.md) — the surfaces these powertrains drive on
- [Machine Tools](../machine-tools/index.md) — precision machining capability for transmission and drivetrain components

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
