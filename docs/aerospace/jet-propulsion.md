# Jet Propulsion

> **Node ID**: aerospace.jet-propulsion
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`metals.aluminum`](../metals/aluminum.md),
> [`energy.gas-turbine`](../energy/gas-turbine.md),
> [`chemistry.petroleum-alternatives`](../chemistry/petroleum-alternatives.md)
> **Enables**: None
> **Timeline**: Years 30-60+
> **Outputs**: jet_engines, turbofan_engines, afterburners, ramjet_engines
> **Critical**: No

Jet propulsion transformed aviation from propeller-driven speeds of 300-600 km/h to transonic and supersonic regimes. The gas turbine — a continuous-flow engine with no reciprocating parts — solved the fundamental limitation of piston engines: their power-to-weight ratio degrades catastrophically at large scales because reciprocating mass rises faster than cylinder displacement. Jet engines scale gracefully: doubling the compressor diameter roughly quadruples mass flow (and thus thrust) while weight increases by only a factor of two.

The capability builds directly on [gas turbine](../energy/gas-turbine.md) turbomachinery — compressors, combustors, and turbines are shared technology. The distinction is that a jet engine uses its exhaust as propulsive thrust rather than expanding all the gas through additional turbine stages to drive a shaft. This article covers the four jet engine architectures in the capability: [turbojets](jet-propulsion.turbojet.md), [turbofans](jet-propulsion.turbofan.md), [afterburners](jet-propulsion.afterburner.md), and [ramjet/scramjets](jet-propulsion.ramjet-scramjet.md).

## The Brayton Cycle

All turbine-based jet engines operate on the **Brayton (Joule) cycle** — a continuous-flow constant-pressure heat engine. Unlike the Otto cycle of piston engines (which is intermittent), the Brayton cycle processes air in a steady stream, enabling smooth high-frequency combustion and eliminating vibration.

### T-s Diagram Description

On a temperature-entropy (T-s) diagram, the ideal Brayton cycle traces four processes:

1. **Isentropic compression** (1→2): Air enters the compressor at ambient temperature T₁ (e.g., 15°C / 288 K at sea level). The compressor raises both pressure and temperature along a vertical line of constant entropy (S₁ = S₂). For a compressor pressure ratio (CPR) of 40:1, the exit temperature T₂ reaches approximately 550-600°C (820-870 K). The area to the left of this line represents compressor work input.

2. **Constant-pressure heat addition** (2→3): Fuel is injected and burned in the combustor at essentially constant pressure. Temperature rises from T₂ to the turbine inlet temperature T₃ (1,400-1,700°C / 1,670-1,970 K in modern engines). On the T-s diagram, this is a horizontal line extending rightward (entropy increases because heat is added). The length of this line is proportional to fuel energy input.

3. **Isentropic expansion** (3→4): Hot gas expands through the turbine (and nozzle), doing work and dropping in temperature along a constant-entropy line. The turbine extracts enough work to drive the compressor (and fan, if present); the remaining enthalpy becomes kinetic energy in the exhaust jet. For a turbojet, T₄ is typically 700-900°C at the nozzle exit.

4. **Constant-pressure heat rejection** (4→1): In an open-cycle engine, the exhaust gas dumps its remaining heat to the atmosphere. On the T-s diagram, this closes the loop horizontally. The enclosed area represents the net work output (which, for a jet engine, is manifested as thrust rather than shaft work).

The **thermal efficiency** of the ideal Brayton cycle depends only on the pressure ratio: η = 1 − (1/CPR)^((γ−1)/γ), where γ ≈ 1.4 for air. At CPR = 40:1, ideal efficiency reaches 65%. Real engines achieve 35-45% due to component inefficiencies (compressor and turbine isentropic efficiencies of 85-92%), pressure losses in the combustor, and bypass air that does not pass through the core.

## Engine Cycle Comparison

| Parameter | Turbojet | Turbofan (high-bypass) | Turbofan (low-bypass) | Turboprop |
|-----------|----------|------------------------|-----------------------|-----------|
| **Bypass ratio** | 0 (all core) | 5:1 – 12:1 | 0.3:1 – 1:1 | effectively 50:1 – 100:1 |
| **Specific thrust** | High (500-800 N·s/kg) | Low (100-300 N·s/kg) | Medium-High | Very low |
| **Specific fuel consumption (SFC)** | 0.90-1.10 kg/daN·h | 0.35-0.55 kg/daN·h | 0.70-0.90 kg/daN·h | 0.25-0.35 kg/daN·h |
| **Propulsive efficiency** | Low at subsonic (55-65%) | High at subsonic (75-85%) | Medium | Very high (85-90%) |
| **Noise** | Very high | Low (bypass air shields exhaust) | High | Low |
| **Speed range** | Subsonic to Mach 2+ | Subsonic to Mach 0.9 | Subsonic to Mach 2+ | Subsonic to Mach 0.6 |
| **Typical application** | Early military, SR-71 core | Commercial airliners, transports | Fighter aircraft, afterburner-equipped | Regional turboprops, C-130 |
| **Thrust lapse with speed** | Relatively flat | Decreases with speed | Decreases, offset by afterburner | Drops sharply with speed |

The key insight: **propulsive efficiency** η_p = 2v / (v + v_e), where v is flight speed and v_e is exhaust velocity. To maximize efficiency, the exhaust velocity should be close to the flight speed. A turbojet's high exhaust velocity (600-800 m/s) is wasteful at subsonic cruise (250 m/s) — most kinetic energy is left in the exhaust plume. A high-bypass turbofan moves a large mass of air slowly (bypass exhaust at 300-350 m/s), closer to the flight speed, transferring more energy to useful thrust.

## Compressor Design

### Centrifugal vs Axial

**Centrifugal compressors** (Whittle-style, used in early British engines): Air enters the eye of a rotating impeller and is flung outward by centrifugal force, gaining both pressure and velocity. A diffuser converts the velocity to static pressure. A single centrifugal stage achieves a pressure ratio of 4:1 to 8:1. Advantages: simple, rugged, short, easy to manufacture, tolerant of foreign object damage. Disadvantages: large frontal area (high drag), limited to 2-3 stages before the air path becomes tortuous. Still used in small turboshaft/APU engines and early helicopter engines.

**Axial compressors** (von Ohain-style, refined by Griffith): Air flows parallel to the shaft axis through alternating rows of rotating (rotor) and stationary (stator) blades. Each rotor row accelerates the air; each stator row diffuses it, converting velocity to pressure. A single axial stage achieves only 1.1:1 to 1.6:1 pressure ratio, but 10-15 stages can be stacked in series. Advantages: small frontal area (low drag at high speed), scalable to very high mass flows. Disadvantages: complex blade aerodynamics, narrow stall margin at off-design conditions, many precision-machined parts.

### Compressor Pressure Ratios (CPR)

Modern engines operate at CPR values that were unimaginable in the 1940s:

| Era | Typical CPR | Example |
|-----|-------------|---------|
| 1940s (Jumo 004) | 3-4:1 | Me 262 fighter |
| 1950s (J57) | 10-12:1 | B-52, early 707 |
| 1970s (JT9D) | 20-25:1 | Boeing 747 |
| 1990s (GE90) | 40-42:1 | Boeing 777 |
| 2010s (GE9X) | 50-60:1 | Boeing 777X |

Higher CPR improves thermal efficiency but demands tighter tip clearances, more compressor stages, and variable inlet guide vanes (VIGVs) to prevent stall at low speeds. The GE9X compressor achieves 27:1 in the high-pressure compressor alone (10 stages) plus a 4:1 boost from the low-pressure / fan booster section, for a combined OPR of approximately 60:1 at takeoff.

**Stall and surge**: If the compressor is pushed beyond its stall line (too much pressure demand for the airflow), blades stall — airflow separates from the blade suction surface, pressure ratio drops abruptly, and combustion gases can reverse-flow forward through the compressor (surge). Surge produces a loud bang, flame from the intake, and can destroy the engine in seconds. Variable stator vanes (adjusting blade inlet angle with speed) and bleed valves (dumping air from intermediate stages) prevent stall by maintaining a stable operating line within the compressor map.

## Combustor Design

The combustor burns fuel at nearly constant pressure — a constraint imposed by the open-cycle Brayton architecture. Air from the compressor (at 40-60 bar, 500-600°C) enters the combustor, but combustion cannot occur at this temperature or with this much excess air (the fuel-air ratio is only 1:50 to 1:100, far below stoichiometric 1:15).

**Combustion zone design**: Only 25-30% of compressor air enters the primary combustion zone through a swirler (creating a recirculating vortex that stabilizes the flame). The remaining air enters as secondary and dilution air through holes in the combustor liner, cooling the liner walls (via slots and films) and diluting the combustion products from the stoichiometric flame temperature (2,000-2,200°C) down to the turbine inlet temperature (1,400-1,700°C) that the turbine blades can survive.

**Combustor types**: Can (individual combustors, easiest to develop), annular (single ring-shaped chamber, most efficient and compact, standard since 1960s), and can-annular (hybrid, multiple cans feeding an annular duct). Modern annular combustors are 15-20 cm tall, 40-80 cm in axial length, and must burn fuel uniformly across a 360° ring with no hot spots that would distort the turbine stators.

**Fuel injection**: Atomizing nozzles break liquid fuel (Jet A-1, kerosene) into droplets smaller than 50 μm for rapid vaporization and mixing. Modern designs use air-blast atomizers (high-velocity air shears the fuel film into fine droplets) rather than pure pressure atomizers, producing better mixing and lower soot/NOx emissions. [Fuel production](../chemistry/petroleum-alternatives.md) provides the kerosene fraction (150-300°C boiling range).

## Turbine Design

The turbine extracts work from the hot gas to drive the compressor (and fan, in a turbofan). This is the most technologically demanding component — it operates in a gas stream hotter than the melting point of its own material, under centrifugal loads that would burst a less carefully designed disc.

### Turbine Inlet Temperature (TIT)

| Era | TIT (°C) | TIT (K) | Technology |
|-----|---------|---------|------------|
| 1940s | 700-800 | 970-1,070 | Uncooled forged blades |
| 1960s | 900-1,000 | 1,170-1,270 | Air-cooled hollow blades |
| 1980s | 1,200-1,350 | 1,470-1,620 | Single-crystal blades, film cooling |
| 2000s | 1,500-1,600 | 1,770-1,870 | TBC + single-crystal + advanced cooling |
| 2010s | 1,600-1,700 | 1,870-1,970 | 3rd-gen single-crystal, TBC, full-coverage film cooling |

The gas temperature exceeds the melting point of the superalloy (typically 1,280-1,350°C) by 200-400°C. The blades survive only because of aggressive internal cooling and external thermal barrier coatings.

### Blade Cooling Techniques

**Internal convection cooling**: Hollow blade castings have serpentine internal passages. Compressor bleed air (diverted from an intermediate stage) flows through these passages, convectively cooling the blade metal from inside before exiting through trailing-edge slots. This alone can reduce metal temperature by 200-300°C below gas temperature.

**Film cooling**: Air exits through rows of tiny holes (0.3-0.8 mm diameter, laser-drilled) on the blade surface, creating a thin insulating film of cool air between the hot gas and the metal. Well-designed film cooling reduces metal temperature by an additional 100-200°C. A typical modern HPT blade has 300-500 film cooling holes.

**Thermal Barrier Coatings (TBC)**: A ceramic layer (yttria-stabilized zirconia, YSZ, 100-300 μm thick) is deposited on the blade surface by electron-beam physical vapor deposition (EB-PVD) or plasma spraying. The ceramic has very low thermal conductivity (≈2 W/m·K vs. 90 W/m·K for the superalloy), creating a temperature drop of 100-150°C across the coating. A bond coat (MCrAlY or platinum-aluminide) between the TBC and the superalloy prevents oxidation of the substrate.

### Single-Crystal Turbine Blades

Conventionally cast turbine blades are polycrystalline — many grains with grain boundaries between them. Grain boundaries are weak points: they creep (slowly elongate under stress) at high temperature, and they are pathways for oxidation and sulfidation that attack the interior of the blade.

**Single-crystal (SX) blades** are grown as a single crystal with no internal grain boundaries. A spiral "selector" in the casting mold allows only one crystal to emerge into the blade cavity; the entire blade solidifies as a single crystal of the nickel-base superalloy. The result: creep resistance improves by 5-10×, oxidation resistance improves dramatically, and the blade can operate 50-80°C hotter than a polycrystalline blade of the same alloy.

**Directionally solidified (DS) blades** are an intermediate technology: grains run parallel to the blade axis (all grain boundaries are longitudinal, so no transverse boundaries where creep is worst). DS blades are 2-3× better than conventional castings but 2× worse than single-crystal. Used in older and lower-temperature turbines.

## Superalloys

Turbine blades, discs, and combustor liners are made from **nickel-base superalloys** — the highest-temperature structural metals available. These are fundamentally different from steels: the nickel matrix is strengthened not by carbon (as in steel) but by a coherent precipitate of gamma-prime (Ni₃Al) that forms 40-70% of the alloy volume and blocks dislocation motion up to 80% of the melting temperature.

| Alloy | Composition (key elements) | Application | Tensile strength at 1,000°C |
|-------|---------------------------|-------------|------------------------------|
| **Inconel 718** | Ni + 19Cr + 18Fe + 5Nb + 3Mo + Ti,Al | Compressor discs, cases, afterburner liners | 400 MPa |
| **Rene N5** | Ni + 7Cr + 7Co + 6.5Ta + 5W + 3Re + Mo,Al | Single-crystal HPT blades (GE) | 500-600 MPa |
| **CMSX-4** | Ni + 6.5Cr + 9Co + 6.5Ta + 6W + 3Re + Mo,Al | Single-crystal HPT blades (Rolls-Royce, P&W) | 500-600 MPa |
| **Hastelloy X** | Ni + 22Cr + 18Fe + 9Mo | Combustor liners, flame holders | 250-300 MPa |

**Inconel 718** is the workhorse for rotating discs and structural cases — it retains 70% of room-temperature strength at 650°C, is weldable (rare among superalloys), and is precipitation-hardened by gamma-double-prime (Ni₃Nb) rather than gamma-prime, giving it excellent slow-cooling weldability. Every modern engine contains hundreds of kilograms of Inconel 718 in compressor and turbine discs, shafts, and casings.

**Rhenium** (3% in CMSX-4 and Rene N5) is the single most effective creep-resistance enhancer in single-crystal superalloys. It slows diffusion at high temperature, resisting the coarsening of the gamma-prime precipitate that weakens the alloy over thousands of hours of service. Rhenium is one of the rarest elements in Earth's crust (1 ppb) and accounts for a significant fraction of single-crystal blade cost. Third-generation SX alloys push rhenium to 6%, trading cost for even higher temperature capability.

## Real Engine Specifications

### CF6-80C2 (Commercial High-Bypass Turbofan)

The CF6 family powers the Boeing 747, 767, and Airbus A300/A310. The -80C2 is a 1980s-generation engine representative of wide-body commercial turbofan technology.

| Parameter | Value |
|-----------|-------|
| **Takeoff thrust** | 52,500-63,500 lbf (234-282 kN) |
| **Maximum thrust (uprated)** | 84,000 lbf (374 kN) in CF6-80E1 variant |
| **Bypass ratio** | 5.05:1 (fan diameter 2.36 m) |
| **Overall pressure ratio** | 30.4:1 |
| **Turbine inlet temperature** | ~1,360°C |
| **Fan stages** | 1 (36 titanium blades) |
| **HPC stages** | 14 (axial) |
| **HPT stages** | 2 (air-cooled) |
| **LPT stages** | 5 |
| **SFC (cruise)** | ~0.56 kg/daN·h |
| **Weight (dry)** | 4,340 kg |

### F119-PW-100 (Military Low-Bypass Turbofan with Afterburner)

The F119 powers the F-22 Raptor air superiority fighter. It represents the state of the art in military engine technology: high thrust-to-weight, low observability, and supercruise (sustained supersonic flight without afterburner).

| Parameter | Value |
|-----------|-------|
| **Thrust (dry / max)** | ~35,000 lbf (156 kN) / ~43,000 lbf (191 kN) with afterburner |
| **Bypass ratio** | ~0.3:1 (very low — maximizes specific thrust) |
| **Overall pressure ratio** | ~35:1 |
| **Turbine inlet temperature** | ~1,600°C (estimated) |
| **Thrust-to-weight ratio** | ~9:1 |
| **Fan stages** | 3 |
| **HPC stages** | 6 |
| **Notable features** | 2D thrust-vectoring nozzle, stealth-shaped afterburner, supercruise at Mach 1.5+ dry |

### J58 (Pratt & Whitney, SR-71 Blackbird)

The J58 is a unique turbo-ramjet hybrid that operated as a turbojet at low speed and transitioned to partial ramjet mode at Mach 3+. It represents the extreme of turbine-based high-speed propulsion.

| Parameter | Value |
|-----------|-------|
| **Thrust (dry / max afterburner)** | 25,000 lbf / 32,500 lbf (145 kN) |
| **Maximum Mach** | 3.2+ (cruise Mach 3.0-3.2) |
| **Bypass ratio** | Variable (turbojet at low speed; ramjet bypass at Mach 3+) |
| **Inlet cones** | Translating spike (moves fore/aft to position shock wave) |
| **Unique feature** | At Mach 3+, 80% of thrust comes from ramjet bypass air around the turbojet core; compressor bleed air is ducted directly to the afterburner |
| **Fuel** | JP-7 (special high-flashpoint kerosene, 60°C flash point) |

## Exhaust Nozzle Design

The nozzle converts the remaining thermal and pressure energy of the exhaust gas into kinetic energy (thrust). A poorly designed nozzle can waste 10-15% of the engine's available thrust.

**Convergent nozzle**: The simplest nozzle — a contracting duct that accelerates subsonic or transonic exhaust to Mach 1 at the throat. Used on early turbojets and low-speed turboprops. Maximum exhaust velocity is Mach 1 regardless of upstream pressure; any remaining pressure energy is lost to the atmosphere as an expanding plume.

**Convergent-divergent (de Laval) nozzle**: A contracting section accelerates flow to Mach 1 at the throat, then a diverging section further accelerates the now-supersonic flow. The area ratio (exit area / throat area) determines the exit Mach number: for a pressure ratio of 10:1, the area ratio is approximately 3.5:1 and exit Mach is 2.2. All modern turbojet and low-bypass turbofan engines use C-D nozzles for supersonic exhaust.

**Variable-area nozzle**: Military engines with afterburners require a nozzle that can change its throat area by 50-100% to accommodate the increased mass flow and temperature of afterburner operation without choking the upstream turbine. Iris (or "turkey feather") nozzles use overlapping petals that slide radially to adjust the throat diameter. The F119's 2D nozzle uses rectangular flaps that also vector thrust ±20° for pitch control.

**Noise**: Jet exhaust noise is proportional to the eighth power of exhaust velocity (v⁸). High-bypass turbofans reduce noise dramatically by producing the same thrust at a lower velocity over a larger area. Modern nacelle designs include chevron nozzles (serrated trailing edges on the bypass exhaust duct) that reduce low-frequency jet noise by 2-4 dB through enhanced mixing of the exhaust with ambient air.

## Fuel Systems

Jet engines consume kerosene-range fuels distilled from [petroleum](../chemistry/petroleum-alternatives.md) or synthesized via the Fischer-Tropsch process from coal, natural gas, or biomass. The fuel serves two roles: energy source for combustion, and heat sink for cooling engine oil and aircraft avionics.

**Jet A / Jet A-1**: The global standard commercial turbine fuel. Freezing point -40°C (Jet A) or -47°C (Jet A-1). Energy density 43.15 MJ/kg. Specific gravity 0.775-0.840. Flash point 38°C minimum. Distillation range 150-300°C boiling fraction from petroleum crude.

**JP-8 (military)**: Equivalent to Jet A-1 with military additives (fuel system icing inhibitor, corrosion inhibitor, static dissipater). Used by NATO military aircraft as a single battlefield fuel (replacing multiple gasoline/diesel/kerosene grades).

**JP-7 (SR-71)**: A specialty high-flashpoint fuel (60°C flash point) designed for the thermal stability required by the J58's Mach 3+ operation where the fuel reaches 150-200°C before injection. JP-7 is so thermally stable and low-volatility that it will not sustain combustion at sea-level ambient conditions — the J58 requires triethylborane (TEB) chemical igniter to light the afterburner.

**Thermal stability**: As fuel heats up while cooling engine oil, dissolved oxygen reacts with trace reactive hydrocarbons, forming deposits ("coke") on heat exchanger surfaces and fuel nozzle tips. Approved fuels must pass the JFTOT (Jet Fuel Thermal Oxidation Tester) at 260-350°C with less than 3 mg of deposit — a requirement that limits the aromatic and olefin content of the fuel.

## Materials and Manufacturing

### Titanium Alloys

The compressor front stages (fan blades and low-pressure compressor) operate at 300-500°C where titanium alloys offer the best strength-to-weight ratio. **Ti-6Al-4V** (6% aluminum, 4% vanadium) is the most widely used titanium alloy in aerospace, with a density of 4.43 g/cm³ (57% of steel), tensile strength of 1,000 MPa, and usable strength up to 400°C. Fan blades in the GE90 are solid Ti-6Al-4V forgings with hollow internal stiffening structures; newer designs use carbon-fiber composite fan blades with titanium leading edges (GE9X).

Titanium is produced by the [Kroll process](../metals/aluminum.md) (reduction of TiCl₄ with magnesium) and is one of the most energy-intensive structural metals to refine. Its use in jet engines must be justified by the weight savings (every kilogram saved in an engine saves 3-5 kg of airframe structure needed to carry it).

### Thermal Barrier Coatings

The YSZ ceramic coating (7-8 wt% yttria-stabilized zirconia) is the standard TBC for turbine blades. Applied by EB-PVD in a vacuum chamber at 900-1,000°C, the coating grows in a columnar microstructure with vertical microcracks that accommodate thermal expansion mismatch with the substrate. The coating is strain-tolerant (columns can slide relative to each other) and adheres well through the thermally grown oxide (TGO) on the bond coat surface. TBC life is limited by spallation — the coating flakes off after hundreds to thousands of thermal cycles due to TGO growth stresses.

## Engine Testing and Qualification

A new jet engine design undergoes 5,000-15,000 hours of ground testing before first flight, followed by another 5,000-20,000 hours of flight testing before certification. Key test types:

- **Bird strike**: Dead birds (1-4 kg) fired from an air cannon into the running engine at takeoff thrust. The engine must continue producing at least 50% thrust for 5 minutes after ingesting a 1.8 kg bird (FAR Part 33). Fan blade release (fan blade out test, FBO) requires the engine to contain a released fan blade without fragments exiting the casing — the most violent and expensive single test.
- **Endurance / cyclic**: 150 hours of alternating maximum and idle thrust, simulating decades of flight cycles. Blade creep and disc low-cycle fatigue (LCF) are the dominant failure modes — turbine disc burst at 40,000 RPM is catastrophic and non-containable.
- **Altitude / icing**: Engine operated in an altitude chamber at simulated cruise conditions (Mach 0.8, 10 km altitude, -55°C). Ice ingestion test: the engine must continue running while ingesting 2-3% mass fraction of ice crystals for 5 minutes, simulating thunderstorm penetration.
- **Crosswind / ground vortex**: Engine tested at up to 30 knots (15 m/s) crosswind to verify that inlet distortion does not cause compressor stall during takeoff and landing.

## Integration Points

| Stage | Contribution |
|-------|-------------|
| [Gas Turbines](../energy/gas-turbine.md) | Turbomachinery foundation — compressors, combustors, turbine stages |
| [Aluminum & Light Metals](../metals/aluminum.md) | Light-alloy casings, compressor blades, airframe structures |
| [Petroleum & Fuels](../chemistry/petroleum-alternatives.md) | Kerosene-based jet fuel (Jet A-1, JP-8), synthetic fuels |
| [Machine Tools](../machine-tools/index.md) | Precision machining of compressor/turbine blading, disc bores |
| [Aviation](aviation.md) | Airframe integration, flight testing, fuel infrastructure |

## Limitations

- **Superalloy supply chain**: Nickel, cobalt, rhenium, and yttrium are rare or strategically concentrated metals. Single-crystal blade foundries require years to build and qualify.
- **Precision manufacturing**: Compressor blade tip clearances of 0.2-0.5 mm over a 3-meter-diameter fan demand extraordinary manufacturing precision and thermal-expansion-matched casing designs.
- **Fuel sensitivity**: Jet engines require carefully specified kerosene fuels with tight limits on freeze point (-47°C for Jet A-1), flash point, sulfur content, and thermal stability (the fuel cools the engine oil and must not coke at 200°C).
- **Scale threshold**: A useful turbojet requires at least 5-10 kN of thrust; below this, piston engines are lighter and more efficient. The minimum viable jet engine weighs 80-150 kg and requires precision turbomachinery foundry capability.
- **Afterburner fuel burn**: Afterburner operation increases fuel consumption by 300-600%, limiting afterburner use to minutes per mission.
- **Ramjet/scramjet ignition**: Ramjets cannot produce static thrust — they require a rocket or turbine booster to reach Mach 3 before combustion can sustain. Scramjets require Mach 4-5 ignition speed.

## See Also

- [Turbojet Engines](jet-propulsion.turbojet.md) — centrifugal/axial compressor, combustor, turbine stages
- [Turbofan Engines](jet-propulsion.turbofan.md) — bypass ratio, high-bypass commercial, low-bypass military
- [Afterburners](jet-propulsion.afterburner.md) — afterburner design, variable nozzle, fuel injection
- [Ramjet and Scramjet Engines](jet-propulsion.ramjet-scramjet.md) — supersonic combustion ramjet, Mach 3-12+
- [Gas Turbines](../energy/gas-turbine.md) — turbomachinery foundation
- [Aviation](aviation.md) — propeller-driven aircraft development
- [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md) — jet fuel production

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
