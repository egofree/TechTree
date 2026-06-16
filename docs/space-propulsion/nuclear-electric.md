# Nuclear Electric Propulsion

> **Node ID**: space-propulsion.nuclear-electric
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`energy.nuclear-fission`](../energy/nuclear-fission.md),
> [`silicon`](../silicon/index.md),
> [`metals`](../metals/index.md)
> **Enables**: High-delta-v outer-planet missions (Jupiter, Saturn, Kuiper Belt); cargo pre-positioning to Mars; Neptune/Uranus orbiters; deep-space power-rich science
> **Timeline**: Years 40-200+
> **Outputs**: nep_systems
> **Critical**: No — NEP requires an advanced nuclear-industrial base (space-qualified reactor, multi-megawatt heat rejection, high-voltage power electronics, long-life ion or Hall thruster arrays) and a regulatory environment for nuclear space launch, all of which arrive late in the bootstrap sequence

A Nuclear Electric Propulsion (NEP) system is a fission reactor, a heat-to-electric converter, a radiator to reject waste heat, and a cluster of electric thrusters — all assembled into one vehicle that accelerates continuously for weeks to years. Unlike [Nuclear Thermal Propulsion](./nuclear-thermal.md), which uses the reactor as a propellant heater and achieves high thrust at 850-1000 s Isp, NEP trades away thrust entirely: the reactor generates electricity, the electricity accelerates a small mass of xenon or krypton to enormous velocity, and the resulting thrust is in millinewtons to a few newtons. The payoff is specific impulse of **3000-7000 seconds**, ten times chemical and three to seven times NTP.

NEP exists for one reason: it reaches places chemical and NTP cannot. A Neptune orbiter with chemical propulsion would need a Saturn flyby, a Jupiter flyby, and a 15-year cruise to arrive with barely enough propellant to enter orbit. The same mission with NEP spirals out of Earth gravity over six months, accelerates continuously for four years, brakes into Neptune orbit over six months, and arrives with reactor power for a multi-year orbital tour — all on a single launch. The trade is time: NEP missions take longer than impulsive-burn missions of comparable payload, but they deliver far more payload at the destination.

This article covers the propulsion-specific engineering of NEP: the reactor-to-electric power conversion, the heat radiator that dominates vehicle mass, and the integration of the electric bus with ion or Hall thrusters. It deliberately does **not** duplicate reactor design, which is documented under [Nuclear Fission Power](../energy/nuclear-fission.md) — NEP inherits reactor physics unchanged. Here we focus on what makes NEP different from a stationary reactor or an NTP engine: the reactor is a power supply, not a heater; the propellant is xenon accelerated by electric fields, not hydrogen heated by fission.

## Operating Principle

An NEP vehicle is a power system bolted to an electric propulsion system. The reactor produces heat; the converter (Brayton, Stirling, or thermoelectric) turns part of that heat into electricity; the radiator rejects the rest; the power-conditioning unit distributes electricity at the voltage and current the thrusters need; and the thrusters ionise xenon and accelerate the ions through electrostatic grids (ion thrusters) or in a crossed-field Hall current (Hall thrusters).

The reactor thermal-to-electric conversion efficiency is **15-30%** for Brayton or Stirling cycles at the 100-1000 kWe scale. The remaining 70-85% of the reactor heat becomes waste heat that must be radiated to space. A 1 MWe reactor (3 MW thermal at 33% efficiency) must radiate 2 MW of waste heat — which at a radiator temperature of 350 K (a typical sink for pumped water or NaK loops) requires roughly:

**P = ε × σ × A × T⁴**

where P is radiated power, ε is emissivity (~0.85 for white paint), σ is the Stefan-Boltzmann constant (5.67×10⁻⁸ W/m²/K⁴), A is radiator area, T is absolute temperature. For P = 2 MW, T = 350 K:

- A = 2×10⁶ / (0.85 × 5.67×10⁻⁸ × 350⁴)
- A = 2×10⁶ / 728 ≈ **2750 m²**

That is a square 52 metres on a side, or a series of radiator panels strung along a 100-metre truss. At a panel mass of 3-5 kg/m² (aluminum fins, NaK coolant, polymer backing) the radiator alone masses 8-14 tonnes — more than the reactor itself. This is the central scaling challenge of NEP: **the radiator sets the mass, not the reactor.**

### Why Radiator Temperature Sets Everything

The Stefan-Boltzmann law (P = ε × σ × A × T⁴) makes radiator temperature a brutal fourth-power lever. Raising the cold-side temperature from 350 K to 500 K drops the required radiator area for a given power by a factor of (500/350)⁴ ≈ 4.2 — but the Brayton cycle efficiency falls as the temperature ratio narrows, so the reactor thermal power that must be rejected rises by roughly 30%. Net area reduction is still about 3×.

| Cold-side Temp (K) | Brayton Efficiency | Radiator Area / MW waste | Mass per MW |
|--------------------|-------------------|---------------------------|-------------|
| 300 | 35% | 4900 m² | 15-25 t |
| 350 | 30% | 2750 m² | 8-14 t |
| 500 | 22% | 660 m² | 2-3 t |
| 700 | 15% | 170 m² | 0.5-1 t |

The trade forces NEP designers toward higher cold-side temperatures even at the cost of efficiency, because area and mass scale so steeply with temperature. Liquid-metal-cooled radiators (lithium, NaK) operating at 500-700 K are the design target for megawatt-class systems; water-loop radiators at 350 K are limited to 100-200 kWe.

## Reactor Power Conversion

The reactor-to-electric converter is what turns fission heat into useful power. Three converter technologies are in active development for space reactors:

- **Closed-loop Brayton cycle** — the baseline for megawatt-class NEP. Helium-xenon working fluid is heated in the reactor heat exchanger (550-1100 K hot side), expands through a turbine, is cooled in the radiator heat exchanger (350-400 K cold side), and is recompressed by a shaft-coupled compressor. Cycle efficiency 25-30%. Heritage: International Space Station solar-Brayton experiments, the SP-100 Brayton design (100 kWe), and the JIMO concept (100 kWe).
- **Free-piston Stirling cycle** — preferred for kilowatt to tens-of-kilowatts applications. Helium in a sealed cylinder is alternately heated and cooled by displacer pistons driving a linear alternator. Cycle efficiency 25-35%. Heritage: Kilopower (1-10 kWe, 2018 ground test of KRUSTY 1 kWe), ASC (Advanced Stirling Convertor).
- **Thermoelectric** — solid-state Seebeck-effect converters with no moving parts. Cycle efficiency 5-8%. Heritage: RTGs (radioisotope thermoelectric generators), SNAP-10A (the only space reactor ever flown, 500 We, 1965). Reliable but heavy per watt; not used for >10 kWe systems.

| Converter | Efficiency | Power Range | Hot Side (K) | Cold Side (K) | TRL |
|-----------|-----------|-------------|--------------|---------------|-----|
| Brayton (closed) | 25-30% | 10-1000 kWe | 1100 | 350 | 5 (JIMO design) |
| Stirling (free-piston) | 25-35% | 1-100 kWe | 850 | 300 | 6 (Kilopower test) |
| Thermoelectric (PbTe/TAGS) | 5-8% | 0.1-1 kWe | 800 | 400 | 9 (RTG flight) |
| Thermionic | 5-10% | 1-100 kWe | 1600 | 800 | 3 (concept) |

The SP-100 programme (1983-1994) was the most thorough American design effort for a space reactor at the 100 kWe scale. SP-100 used uranium nitride (UN) fuel, lithium coolant at 1370 K, and a SiGe thermoelectric converter — producing 100 kWe at 550°C with a 10-year design life. It was never launched; the programme ended when the Strategic Defense Initiative's mission priorities shifted. SP-100 established the engineering baseline for fast-spectrum, liquid-metal-cooled space reactors that every modern design (JIMO, Kilopower's 10 kWe variant, Prometheus) builds on.

The JIMO concept (Jupiter Icy Moons Orbiter, 2003-2005, cancelled under Prometheus) would have used a Brayton-cycle reactor producing 100 kWe, powering a cluster of ion thrusters to orbit Callisto, Ganymede, and Europa sequentially over a 10-year mission. The reactor design heritage was SP-100; the Brayton converter was derived from the International Space Station Brayton experiments.

### Brayton Cycle Thermodynamics

The closed-loop Brayton cycle is the workhorse converter for megawatt NEP. Helium-xenon mixture (typically 40 g/mol average molecular weight, a compromise between low M for high turbine work and high M for low heat-exchanger area) circulates through four components:

- **Compressor** — low-pressure He-Xe at 300 K is compressed to 0.5-2 MPa; absorbs shaft work
- **Reactor heat exchanger** — high-pressure He-Xe is heated to 1100 K at constant pressure
- **Turbine** — hot gas expands to low pressure, driving the compressor-alternator shaft; produces work
- **Recuperator + radiator heat exchanger** — exhaust heat is partially recovered to pre-heat the compressor discharge, then fully rejected to the radiator cold side

The ideal Brayton efficiency is **1 - (T_cold/T_hot)**, giving a theoretical maximum of **1 - (300/1100) = 73%** at those temperatures. Real cycles with recuperation achieve **25-30%** at 100 kWe and **35-40%** at megawatt scale. The gap between ideal and real is recuperator effectiveness (<95%), turbomachinery isentropic efficiency (<85%), and pressure drops in piping. Modern superalloy turbines with carbon composite recuperators are targeting 40% at 100 kWe in the next design generation.

This is the power-conversion process — see [Reactor Power Conversion](./nuclear-electric.reactor-power-conversion.md) for the dedicated process. The reactor neutronics, fuel fabrication, and criticality control are documented under [Nuclear Fission Power](../energy/nuclear-fission.md) — NEP uses the same reactor physics.

## Heat Radiator Design

Heat rejection is the dominant mass term in any NEP architecture, and the one that sets the practical upper limit on reactor power. A 100 kWe reactor with 30% Brayton efficiency produces 333 kW thermal, of which 233 kW must be radiated. A 1 MWe reactor radiates 2.3 MW. There is no convection in space; the only way to remove heat is thermal radiation, which scales as T⁴ and is brutally inefficient at the temperatures a spacecraft can tolerate.

| Reactor Power | Waste Heat | Radiator Area (T=350 K) | Radiator Mass |
|---------------|------------|--------------------------|---------------|
| 1 kWe (Stirling) | 3 kW | 4 m² | 15 kg |
| 10 kWe (Stirling) | 30 kW | 40 m² | 150 kg |
| 100 kWe (Brayton) | 233 kW | 320 m² | 1-1.5 t |
| 1 MWe (Brayton) | 2.3 MW | 2750 m² | 8-14 t |
| 10 MWe (Brayton) | 23 MW | 27500 m² | 80-140 t |

The radiator mass scales roughly linearly with reactor power, but the area that has to be deployed scales linearly as well — and that deployment is what kills large NEP concepts. A 1 MWe vehicle needs a radiator the size of a football field, deployed in vacuum, structurally stiff enough to survive the g-loads of impulsive manoeuvres. A 10 MWe vehicle needs a radiator that no current launch vehicle fairing can house.

### Radiator Architectures

Three radiator concepts have been studied for NEP, each trading off mass, complexity, and technology readiness:

- **Pumped-loop radiator** — the baseline. Liquid NaK (sodium-potassium eutectic, mp = -12°C) or water is pumped through aluminum or titanium-polymer finned panels; the fins radiate to space.TRL 9 (flown on the ISS main radiator, which rejects 70 kW from 1500 m²). Mass: 3-5 kg/m² for the panel plus 1-2 kg/m² for the coolant, plumbing, and pumps.
- **Heat-pipe radiator** — sealed tubes filled with working fluid (ammonia, water, or sodium) that transfers heat by two-phase evaporation-condensation. No moving parts; individual heat-pipe failures do not disable the radiator. TRL 6 (flown on small satellites). Mass: 4-7 kg/m².
- **Liquid-droplet radiator** — a sheet of molten metal (lithium, NaK, or tin) sprayed into space from a generator arm, travels several metres through vacuum while radiating, and is recaptured by a collector arm. Achieves 4-10× the heat flux per unit mass of solid radiators because the droplets have enormous surface-area-to-volume ratio. TRL 3 (ground-tested in vacuum chambers, never flown). Mass: 0.5-1.5 kg/m².

Liquid-droplet radiators are the technology that would unlock 10+ MWe NEP. A 10 MWe system with droplet radiators masses 80-140 tonnes; with pumped-loop radiators it masses 200-400 tonnes. No mission that requires 10 MWe has been funded, so the droplet radiator remains in the laboratory.

This is the radiator-design process — see [Heat Radiator Design](./nuclear-electric.heat-radiator-design.md).

## Electric Propulsion Integration

The electric thruster is what turns reactor electricity into thrust. NEP systems use two thruster families, both electrostatic:

- **Ion thrusters** — xenon gas is ionised in a discharge chamber and accelerated through a pair of electrostatic grids at 20-40 kV. Specific impulse **3000-7000 s**, thrust per thruster 0.05-0.5 N, efficiency 60-80%. Heritage: NSTAR (Deep Space 1, 1998), NEXT (Dawn, 2007), and the 30-cm NASA Evolutionary Xenon Thruster used operationally on Dawn (asteroid Vesta and Ceres).
- **Hall thrusters** — xenon is ionised in a radial magnetic field that traps electrons; ions accelerate through the Hall current at 150-400 V. Specific impulse **1500-3000 s**, thrust per thruster 0.1-1 N, efficiency 45-60%. Heritage: SPT-100 (Russian, flown on dozens of comsats), AEPS (Advanced Electric Propulsion System, 13 kW, baselined for the Lunar Gateway PPE).

| Thruster | Type | Power (kW) | Isp (s) | Thrust (mN) | Efficiency |
|----------|------|-----------|---------|-------------|------------|
| NSTAR (DS1) | Ion | 2.3 | 3100 | 92 | 62% |
| NEXT (Dawn) | Ion | 6.9 | 4190 | 236 | 71% |
| HERMeS/AEPS | Hall | 12.5 | 2200 | 600 | 50% |
| NEXIS (concept) | Ion | 20-25 | 7000 | 200 | 78% |
| VASIMR (concept) | Plasma | 200 | 3000-5000 | 5000 | 60% |

A 100 kWe NEP vehicle needs 8-15 NEXT-class ion thrusters or 5-8 AEPS-class Hall thrusters, each with its own power-processing unit (PPU), thruster-gimbal mechanism, and xenon flow controller. The thruster array mass (thrusters + PPUs + gimbals + cabling) is typically 8-12 kg/kWe — so a 100 kWe NEP array masses 800-1200 kg. This is small compared to the reactor and radiator, but it is the one subsystem where efficiency directly limits mission performance.

### Thruster Array Scaling

A 100 kWe NEP vehicle is not built around one giant thruster — it is built around dozens of moderate thrusters ganged in parallel. The reasons are fault tolerance, beam-current limits, and the simple fact that no single 100 kWe ion thruster has ever been qualified. The Dawn spacecraft used three 2.3 kW NSTAR thrusters (one active at a time); the Lunar Gateway PPE uses four 12.5 kW AEPS Hall thrusters (two active, two redundant). Megawatt-class NEP concepts extrapolate to 20-80 thrusters in a 4×5 to 8×10 array.

| NEP Power | # Ion Thrusters (NEXT-class, 7 kW each) | # Hall Thrusters (AEPS-class, 12.5 kW each) | Array Mass (kg) |
|-----------|------------------------------------------|----------------------------------------------|------------------|
| 10 kWe | 2 (1 active) | 1 | 80-120 |
| 100 kWe | 15 (12 active, 3 spare) | 8 (6 active, 2 spare) | 800-1200 |
| 500 kWe | 75 (60 active, 15 spare) | 40 (32 active, 8 spare) | 4000-6000 |
| 1 MWe | 150 (120 active, 30 spare) | 80 (64 active, 16 spare) | 8000-12000 |

The PPU — the box that converts 100-1000 V DC reactor bus power into the precisely regulated RF or DC discharge that the thruster needs — is the heaviest single component of each thruster station, at 3-5 kg/kWe. PPU efficiency (90-95%) and specific mass (kg/kWe) have improved slowly over 30 years; they are the bottleneck for scaling NEP above 100 kWe.

Total system Isp for an NEP vehicle is set by the thruster, not the reactor. The reactor sets the power available; the thruster sets how efficiently that power becomes thrust. For a 100 kWe reactor driving ion thrusters at 4000 s Isp, the total system Isp is 4000 s. There is no reactor-to-Isp penalty as there is in NTP (where the 2700 K fuel temperature cap fixes Isp at 850-1000 s); an NEP system can reach 7000 s Isp with sufficiently high-voltage ion optics and low-mass propellant (krypton, argon, or iodine have all been proposed).

This is the integration process — see [Electric Propulsion Integration](./nuclear-electric.electric-propulsion-integration.md). Electric propulsion thrusters themselves are documented under the [Electric Ion](./index.md) capability where that domain exists.

### Power Conditioning and Distribution

The power-conditioning and distribution unit (PCDU) is the bridge between the reactor DC bus and the thruster discharge circuits. It must:

- **Convert** the 100-1000 V DC reactor bus to the 300-5000 V AC or DC discharge that each thruster needs
- **Regulate** discharge current to ±1% over the bus voltage ripple (typically ±5%)
- **Isolate** thruster faults (arc-over, grid short) so a single failed thruster does not collapse the bus
- **Sequence** thruster ignition, with current-limited soft-start on each unit

The PCDU is the second-heaviest single subsystem after the radiator, at 3-5 kg/kWe distributed across the array. Modern designs target 1-2 kg/kWe using silicon-carbide power semiconductors (see [Silicon](../silicon/index.md) for the device-fabrication heritage), which would halve PCDU mass and unlock >500 kWe class vehicles within current launch-fairing mass limits.

## Comparison — NEP vs NTP vs Solar Electric

| Parameter | Solar Electric | NTP (LH2) | NEP |
|-----------|---------------|-----------|-----|
| Reactor power | 0 (solar arrays) | 1-4 GW thermal | 0.1-10 MWe |
| Isp (s) | 3000-4500 | 850-1000 | 3000-7000 |
| Thrust (N) | 0.05-0.5 | 110000-330000 | 0.5-50 |
| Mission mode | continuous low-thrust | impulsive burns | continuous low-thrust |
| Outer planet feasible | no (sun too dim) | slow | yes (power independent of sun) |
| Mass at destination | low (high Isp) | medium (lower Isp, higher thrust) | highest (longest acceleration time) |
| Crewed Mars transit | not used | 90-120 days | 18-24 months (crewed NEP not viable) |
| Test status | operational (Dawn, Psyche) | ground-tested (NERVA) | conceptual (JIMO cancelled) |

The table captures the niche NEP occupies. Solar electric wins anywhere the sun is bright (inner solar system, near-Earth asteroids, lunar orbit). NTP wins for crewed Mars (the only option that combines high enough thrust to get humans there fast with high enough Isp to halve the propellant mass). NEP wins for uncrewed outer-planet orbiters and for cargo pre-positioning missions where transit time does not matter but delivered mass does.

## Mission Applications

- **Outer-planet orbiters** — the canonical NEP mission class. A 100 kWe NEP vehicle can deliver 2-4 tonnes of science payload to Jupiter, Saturn, Uranus, or Neptune orbit and still have reactor power for a 5-10 year orbital tour. Chemical propulsion cannot reach Uranus or Neptune with an orbit insertion; NEP can.
- **Mars cargo pre-positioning** — sending crew habitats, ascent vehicles, and return propellant to Mars months or years ahead of the crew. A 500 kWe NEP cargo vehicle can deliver 40 tonnes of payload to Mars surface or orbit per launch, compared to 15 tonnes for a chemical mission of the same launch mass.
- **Kuiper Belt and interstellar precursor** — a 1 MWe NEP vehicle with 10-year xenon supply can reach 500-1000 AU, enabling missions to the heliopause and the inner Oort cloud.
- **Asteroid redirect** — NEP can rendezvous with, capture, and return a 5-10 metre near-Earth asteroid to lunar orbit over 5-10 years. The ARM (Asteroid Redirect Mission) concept studied this architecture before cancellation.

### Mass Budget — Reference 100 kWe NEP Vehicle

A representative 100 kWe NEP vehicle sized for a 10-year outer-planet mission has the following mass breakdown:

| Subsystem | Mass (kg) | Notes |
|-----------|-----------|-------|
| Reactor (100 kWe fast-spectrum, UN fuel, Li coolant) | 1500 | SP-100 heritage |
| Shielding (LiH + W shadow cone) | 800 | Sized for 10 m separation |
| Power conversion (Brayton, 100 kWe output) | 600 | Alternator + compressor + turbine + recuperator |
| Heat radiator (pumped-loop, NaK, 320 m²) | 1100 | At 350 K cold side, 3.5 kg/m² |
| Power conditioning (PPU + cabling) | 800 | 100 kWe at 95% efficiency |
| Thruster array (8 NEXT-class ion, 6 active) | 300 | Thrusters + gimbals |
| Xenon propellant (10 tonnes) | 10000 | 4000 s Isp gives 392 km/s delta-v |
| Propellant tankage (tanks + feed) | 600 | 6% of propellant |
| Structure + thermal + harness | 1500 | Truss, ties, MLI |
| **Total wet mass** | **17200** | launched to LEO on a single heavy-lift vehicle |
| **Dry mass** | **7200** | everything except xenon |

With this mass and 100 kWe driving ion thrusters at 4000 s Isp, the vehicle delta-v is roughly:

- **delta-v = Isp × g × ln(m_wet/m_dry) = 4000 × 9.81 × ln(17200/7200) ≈ 33.9 km/s**

This is enough for a Jupiter orbiter mission (C3 ≈ 85 km²/s² from LEO, plus capture and tour delta-v) and is the standard reference architecture for NEP outer-planet missions. Scaling the reactor to 1 MWe and the radiator proportionally yields a 50-100 km/s delta-v vehicle, but the dry mass rises to 40-60 tonnes and requires multiple heavy-lift launches to assemble in LEO.

## What This Article Does Not Cover

Per the task brief, this article focuses on propulsion-specific aspects and does not duplicate reactor design. The following are documented under [Nuclear Fission Power](../energy/nuclear-fission.md):

- Reactor neutronics, criticality, control, and shutdown margins
- Fuel fabrication (enrichment, UN pelletising, cladding)
- Decay heat removal after shutdown
- Launch-abort nuclear safety and criticality accidents
- Terrestrial test reactor design and qualification

NEP inherits all of these. What NEP adds — Brayton/Stirling power conversion, megawatt-class heat rejection, high-voltage power distribution to electric thruster arrays — is what makes it a propulsion system and not just a reactor with a thruster bolted on.

## Recent Programmes

- **SNAP-10A** (1965) — the only fission reactor ever flown in space. 500 We thermoelectric, launched into polar orbit, operated 43 days before a voltage regulator failed. Demonstrated that a space reactor could be deployed and operated; established no design heritage for modern NEP.
- **SP-100** (1983-1994) — the most thorough American space-reactor design effort. 100 kWe, UN fuel, liquid lithium coolant, SiGe thermoelectric conversion. Never flown but established the design baseline for fast-spectrum space reactors.
- **Topaz** (Soviet, 1970-1988) — flew two reactors in space (Cosmos 1818 and 1867, 1987). 5-10 kWe thermionic conversion. Demonstrated long-duration operation in orbit.
- **Prometheus** (NASA, 2003-2005) — would have built JIMO: a 100 kWe Brayton reactor powering ion thrusters for a Jupiter Icy Moons Orbiter mission. Cancelled in the FY2006 NASA budget.
- **Kilopower / KRUSTY** (NASA-NNSA, 2015-2018) — 1 kWe Kilopower Reactor Using Stirling Technology, ground-tested in 2018. Scaled-up 10 kWe concepts target lunar surface power. Heritage for the converter technology that any future megawatt-class NEP would scale.

## Manufacturing Challenges

The reasons NEP has not flown since SNAP-10A in 1965 are industrial, not scientific:

- **Space-qualified reactor** — fast-spectrum reactors using UN fuel and liquid-metal coolant have only been ground-tested. The qualification campaign for SP-100 ran 11 years and never reached a flight unit; JIMO was cancelled before the reactor design was finalised. A flight-qualified 100 kWe reactor is a billion-dollar, decade-long development.
- **Megawatt-class radiator deployment** — a 320 m² radiator for 100 kWe, or a 2750 m² radiator for 1 MWe, must be folded into a 4-5 m launch fairing, deployed in vacuum, and survive 5-10 years of micrometeoroid impacts. State of the art (ISS radiators) is 1500 m² deployed robotically; scaling to NEP-class areas is unflown.
- **Brayton alternator lifetime** — the closed-loop Brayton unit's turbine-alternator-compressor shaft spins at 30,000-60,000 RPM on gas bearings. Ground units have demonstrated 50,000+ hour lifetimes; qualifying for 10-year uncrewed mission operation requires accelerated-life testing that has not been done at >10 kWe scale.
- **High-voltage power distribution in vacuum** — a 100 kWe thruster array operates at 300-1000 V DC, distributed across 8-15 thruster stations through wiring that must not arc in vacuum or under radiation. The state of the art for space HV distribution is the ISS 160 V main bus; NEP needs 5-10× that voltage.
- **Launch licensing** — same nuclear-safety launch approval regime as NTP. SNAP-10A was launched under a 1960s-era safety framework that no longer exists; modern NEP launches face a multi-year review.

## Regulatory and Safety Environment

NEP, like NTP, falls under multiple regulatory regimes:

- **Launch safety** — a cold reactor must remain subcritical through all launch-accident scenarios: fire, explosion, hard impact, immersion in seawater or wet sand, burial in soil. The United States requires Presidential nuclear safety launch approval (NSLA) signed off by the Office of Science and Technology Policy.
- **Atmospheric re-entry** — the reactor must be designed to disintegrate on accidental re-entry into the upper atmosphere, dispersing fuel into small particles that dilute below radiological concern. SP-100 was designed this way; modern designs follow the same principle.
- **End-of-life disposal** — after mission completion, the reactor must be moved to a disposal orbit with a >300-year (NEP) or >1000-year (some concepts) decay time, to allow fission products to decay before any re-entry risk.
- **International safeguards** — NEP reactors use 20-97% enriched U-235; under the IAEA, HEU (>20%) reactors are subject to international inspection and accounting. The trend toward LEU (<20%) reactors (DRACO, Kilopower) avoids proliferation concerns at the cost of lower power density.

These regimes are not barriers to NEP in principle — they are gates that any flight NEP must pass, and they take 5-10 years to clear for a first mission. They are why no space reactor has flown since 1988.

## Glossary

- **Brayton cycle** — closed-loop gas-turbine cycle using helium-xenon; preferred converter for megawatt NEP.
- **Stirling cycle** — closed-loop piston engine using helium; preferred converter for kilowatt-to-tens-of-kilowatt NEP.
- **NaK** — sodium-potassium eutectic alloy; liquid at room temperature, used as a pumped-loop radiator coolant.
- **Hall thruster** — electrostatic thruster using a radial magnetic field to trap electrons; moderate Isp (1500-3000 s), high thrust.
- **Ion thruster** — electrostatic thruster using grid-accelerated ions; high Isp (3000-7000 s), lower thrust.
- **SP-100** — 100 kWe space reactor design programme (1983-1994); design baseline for modern fast-spectrum space reactors.
- **JIMO** — Jupiter Icy Moons Orbiter; cancelled 2005 NEP mission concept (100 kWe Brayton + ion).
- **TRL** — Technology Readiness Level, 1 (concept) to 9 (flight-proven).

## See Also

- [Nuclear Thermal Propulsion](./nuclear-thermal.md) — the competing nuclear-space-propulsion architecture
- [Nuclear Fission Power](../energy/nuclear-fission.md) — the reactor heritage that NEP depends on
- [Reactor Power Conversion](./nuclear-electric.reactor-power-conversion.md) — Brayton/Stirling cycle process
- [Heat Radiator Design](./nuclear-electric.heat-radiator-design.md) — megawatt heat rejection
- [Electric Propulsion Integration](./nuclear-electric.electric-propulsion-integration.md) — thruster array integration

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md) • [All Domains](../index.md)*
