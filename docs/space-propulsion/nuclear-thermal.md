# Nuclear Thermal Propulsion

> **Node ID**: space-propulsion.nuclear-thermal
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`energy.nuclear-fission`](../energy/nuclear-fission.md),
> [`energy.nuclear-fission.reactor-design`](../energy/nuclear-fission.md),
> [`cryogenics.liquefaction-storage`](../cryogenics/liquefaction-storage.md),
> [`metals`](../metals/index.md)
> **Enables**: Fast crewed transits to Mars (90-120 days vs 180 for chemical); high-thrust cislunar tugs; heavy cargo orbit-raising
> **Timeline**: Years 40-200+
> **Outputs**: ntp_engines
> **Critical**: No — NTP requires an advanced nuclear-industrial base (enriched uranium, refractory-metal fuel fabrication, qualified reactor test stands, cryogenic LH2 handling) and a regulatory environment for nuclear space launch, all of which arrive late in the bootstrap sequence

A nuclear thermal rocket (NTR) is the simplest high-performance propulsion that has ever been ground-tested: a compact fission reactor heats hydrogen propellant directly to roughly 2700 K, the hot gas expands through a nozzle, and the vehicle moves. There is no combustion, no oxidizer, no chemical energy release at all — every joule of thrust comes from the controlled splitting of uranium-235 nuclei. Because the propellant is pure hydrogen (molecular weight 2 vs 18 for water combustion products or 9 for the LOX/LH2 exhaust of a chemical engine), the exhaust velocity is two to three times higher than any chemical rocket can reach, even though the temperature is comparable.

That performance advantage is why the United States poured almost two decades of work into NERVA (Nuclear Engine for Rocket Vehicle Application) between 1955 and 1973, running dozens of reactor-in-a-nozzle tests at Jackass Flats in Nevada. NRX-A1 ran for 116 minutes at 1.1 GW thermal and delivered 850 s Isp; Pewee reached 2500 MW and 245 kN thrust; Phoebus-2A, the most powerful nuclear reactor ever built for spaceflight, ran at 4 GW thermal. The engines worked. They were cancelled not because of technical failure but because the post-Apollo Mars programme they were built for was cancelled, and no other mission required their unique combination of high thrust and high Isp.

This article covers the propulsion-specific engineering of an NTR: the reactor core as a propellant heater, the LH2 feed and expander cycle, the hot-hydrogen nozzle, and the shadow shield that protects the crew. It deliberately does **not** duplicate the reactor physics, neutronics, or fuel-cycle chemistry already documented under [Nuclear Fission Power](../energy/nuclear-fission.md) — that material is treated there. Here we focus on what makes an NTR different from a stationary power reactor: the propellant is the coolant, the coolant is hydrogen at 2700 K, and the whole assembly must fit inside a launch vehicle and survive launch loads.

## Operating Principle

An NTR works by running cold hydrogen through a fission reactor core and exhausting the hot hydrogen through a convergent-divergent nozzle. The reactor fuel — uranium carbide (UC), uranium nitride (UN), or TRISO-style coated particle fuel embedded in a graphite or refractory-metal matrix — is formed into elements with internal channels. Cold LH2 (20 K) enters the top of the core, flows down through these channels picking up heat from the fuel matrix, and exits the bottom at 2500-3000 K. From there the hot hydrogen enters the nozzle, expands to supersonic velocity, and produces thrust at a specific impulse of **850-1000 seconds**.

The physics of the Isp advantage is straightforward. Rocket exhaust velocity scales as √(T/M) where T is the chamber temperature and M is the average molecular weight of the exhaust gases. A LOX/LH2 chemical engine burns hydrogen with oxygen, producing steam (H₂O, M = 18) at 3500 K; an NTR heats pure hydrogen (H₂, M = 2) to only 2700-3000 K. Even though the NTR chamber is cooler, the factor-of-nine lower molecular weight wins: the exhaust moves 2-3× faster. No chemical combination can match this without carrying an oxidizer, which always raises M.

| Engine Type | Propellant | T_chamber (K) | M_exhaust | Isp (s) | Thrust (kN) |
|-------------|------------|---------------|-----------|---------|-------------|
| Chemical LOX/RP-1 | LOX + kerosene | 3500 | 21.9 | 300-330 | 7,600 (Merlin 1D) |
| Chemical LOX/LH2 | LOX + LH2 | 3600 | 8.9 | 440-465 | 2,280 (RS-25) |
| NTP (NERVA-class) | LH2 only | 2700-3000 | 2.0 | 850-1000 | 245 (Pewee) |
| Nuclear Electric | Xe/Kr (ion) | — | — | 3000-7000 | 0.001-0.5 |

The combination of high thrust (hundreds of kN) and high Isp (850-1000 s) is unique to NTP. Chemical engines match the thrust but at one-third the Isp; electric propulsion (ion, Hall) match the Isp but at one-thousandth the thrust. NTP is the only propulsive option that shortens a manned Mars transit enough to matter.

## NERVA Heritage

The Nuclear Engine for Rocket Vehicle Application programme is the engineering baseline against which every modern NTR proposal is measured. Tested between 1959 and 1972 at the Nevada Test Site, NERVA demonstrated that a fission reactor could run as a rocket engine — repeatedly, for tens of minutes per burn, across multiple restarts.

| NERVA Engine | Thermal Power | Thrust (kN) | Isp (s) | Power Density | Fuel |
|--------------|---------------|-------------|---------|---------------|------|
| NRX-A1 (1962) | 1.1 GW | ~245 | 850 | 0.25 GW/m³ | UC-graphite |
| NRX-XE (1969) | 1.1 GW | 245 | 710 | 0.25 GW/m³ | UC-graphite |
| Pewee (1968) | 0.5 GW | 110 | 925 | — | UC-graphite |
| Phoebus-2A (1968) | 4.0 GW | 245 | 825 | — | UC-graphite |
| Pewee 2 (1968) | 0.5 GW | 110 | 850 | — | UN-coated particle |

The NRX series ran for 28 start-stop cycles totalling nearly two hours of operation; Pewee ran at design temperature for 40 minutes; Phoebus-2A, at 4 GW the most powerful reactor ever tested for spaceflight, ran for 12 minutes at 1500 MW before being deliberately pushed past design limits. None of the engines failed structurally. The cancellation in January 1973 was a programme decision, not a technical one: NASA had no funded Mars mission to fly the engines on.

### What NERVA Actually Proved

The NERVA programme, taken as a whole, demonstrated eight engineering facts that any modern NTR can rely on:

- **Repeatable cold-start to full-power transients** — NRX-A1 ramped from cold to 1100 MW in 60 seconds, with no fuel-element damage. Reactor dynamics allowed load-following the turbopump in real time.
- **Multi-burn mission profile** — Pewee demonstrated 6 start-stop cycles totalling 40 minutes at design temperature, sufficient for a LEO-departure burn, mid-course correction, and Mars-capture burn.
- **Hydrogen expander turbopump** — the cycle where cold LH2 cools the nozzle and reactor structure, vaporises, drives the turbine, and is then superheated in the core, was demonstrated at 27 kg/s flow and 5.5 MPa discharge.
- **Power density** — the 0.25 GW/m³ figure is not theoretical; it was measured at the core of NRX-A1. This is roughly 10× the power density of a pressurised-water reactor.
- **Coated fuel survival** — ZrC and NbC coatings on UC-graphite fuel elements survived dozens of thermal cycles, with erosion rates low enough to project multi-burn reliability at 0.999.
- **Shadow-shield mass budget** — NRX-XE demonstrated a tungsten/LiH shadow shield sized for a 10-m separation, with a measured mass under 1500 kg.
- **Nozzle operation in simulated vacuum** — the exhaust nozzle delivered its design Isp when tested in a steam-ejector vacuum chamber that simulated LEO back-pressure.
- **Radiation signature** — measured crew-dose rates at 10 m behind the shield during full-power runs allowed extrapolation to a Mars mission profile of <30 rem for the entire transit.

### What NERVA Did Not Solve

- **Long-duration LH2 storage** — NERVA was a ground test article; it did not have to store LH2 for a 30-day LEO coast before ignition. Zero-boiloff tankage, multi-layer insulation, and active cryocoolers remain untested at NTP scale.
- **Multi-year reliability** — NERVA fuel elements were qualified for ~2 hours of operation. A crewed Mars mission with three burns needs ~30 minutes per burn, so the test envelope covers it — but with margins thinner than the chemical-engine industry considers acceptable.
- **Launch-abort nuclear safety** — if a launch vehicle carrying an NTR (with cold, unstarted reactor) fails, the reactor disperses as low-enriched-uranium debris. Modern programmes (DRACO, later NASA Mars studies) require the reactor to remain subcritical even when fully immersed in water or sand.
- **Atmospheric radiation release** — the United States stopped above-ground reactor testing in the 1970s. Any future flight test must ignite only after the reactor is on a suborbital or escape trajectory that does not re-enter Earth's atmosphere.

Key NERVA lessons that constrain every modern NTR design:

- **Hydrogen corrosion of fuel**: hot hydrogen attacks graphite (forms methane) and carbide fuels. NERVA used ZrC or NbC coatings on the fuel elements to slow erosion; modern designs lean toward TRISO-style coated particles or all-ceramic CERMET (ceramic-metal composite) matrices.
- **Power density**: NRX achieved 0.25 GW/m³ at the core, roughly 10× the power density of a terrestrial power reactor. This is achievable because the hydrogen coolant removes heat faster than water, and because the engine only runs for minutes rather than years.
- **Reactor dynamics**: the temperature feedback coefficient (hydrogen heats up, density drops, reactivity falls) was used as passive load-following. Pumping more hydrogen through the core cooled it, raised its density, and increased reactivity — so thrust and power tracked the propellant flow rate naturally.

## Fuel and Core Design

The reactor core of an NTR is the heart of the engine, and the choice of fuel sets every other design parameter. Three fuel classes have been ground-tested:

- **Graphite-matrix UC (uranium carbide)** — the NERVA baseline. Uranium carbide particles dispersed in a graphite matrix, with the whole element coated in zirconium carbide or niobium carbide to resist hydrogen corrosion. Operational to ~2700 K; tested to 5000+ MW thermal. The coating is the limiting technology: pinhole defects allow hydrogen to reach the graphite, which methanizes and erodes.
- **CERMET (W-UO₂ or Mo-UO₂)** — ceramic UO₂ fuel particles in a tungsten or molybdenum metal matrix. Higher temperature capability (3000 K), excellent hydrogen compatibility, and high thermal conductivity that evens out fuel temperature gradients. The tradeoff is neutron poisoning: tungsten and molybdenum are not as transparent to neutrons as graphite, requiring higher enrichment (93% U-235 typical) and larger cores.
- **Coated particle (TRISO-style)** — uranium nitride or uranium carbide kernels in pyrocarbon/SiC multilayer shells, packed into a graphite or refractory matrix. Each particle is a self-contained pressure vessel that retains fission products even at 3000 K. The dominant modern approach for both NTP and high-temperature gas reactors.

Fuel temperatures are set by the Isp target. A core averaging 2700 K delivers ~850-900 s Isp; pushing the fuel to 3000 K (the practical limit of refractory metals and carbides in hydrogen) reaches 950-1000 s. Above 3000 K, no known material survives — this is the structural ceiling on NTP performance that no amount of engineering can lift.

A worked example illustrates the fuel-temperature-to-Isp relationship. Specific impulse in vacuum is approximately:

**Isp = (1/g) × √(2 × (k/(k-1)) × R × T_c × (1 - (P_e/P_c)^((k-1)/k)))**

where k = 1.4 (diatomic hydrogen), R = 4124 J/(kg·K) (hydrogen gas constant), T_c is chamber temperature in kelvin, P_e/P_c is the expansion pressure ratio. For T_c = 2700 K and an expansion ratio giving P_e/P_c = 0.001:

- Isp = (1/9.81) × √(2 × 3.5 × 4124 × 2700 × (1 - 0.001^0.286))
- Isp ≈ 880 s

For T_c = 3000 K the same expansion gives Isp ≈ 930 s; pushing T_c to 3200 K (which no fuel has survived) would yield ~960 s. The 850-1000 s Isp range quoted for NTP is set directly by the 2500-3000 K fuel temperature window — not by neutronics, thrust chamber pressure, or any other design variable. This is why every NTP paper debates fuel temperature: it is the single number that sets performance.

This is the core-design process — see [Reactor Core Design](./nuclear-thermal.reactor-core-design.md) for the dedicated process. The reactor neutronics, criticality safety, and fuel-cycle chemistry are documented under [Nuclear Fission Power](../energy/nuclear-fission.md) and [Reactor Design](../energy/nuclear-fission.md) — NTP inherits those disciplines without modification.

## Propellant Feed — LH2 Expander Cycle

NTP propellant is liquid hydrogen stored at 20 K in cryogenic tanks and fed to the reactor core by a turbopump. The dominant cycle is the **expander cycle**: cold LH2 is pumped through the nozzle cooling jacket and the reactor support structure, where it absorbs heat and becomes high-pressure hydrogen gas; this gas drives the turbopump turbine; the turbine exhaust is routed into the top of the reactor core, where it is superheated to 2700 K and exhausted through the nozzle. The cycle is self-driving — the reactor's own waste heat powers the turbopump — and requires no preburner or gas generator.

| Parameter | NERVA NRX-A1 | Modern Target |
|-----------|--------------|---------------|
| LH2 tank temperature | 20 K | 20 K |
| Pump inlet pressure | 0.3 MPa | 0.3 MPa |
| Pump outlet pressure | 5.5 MPa | 5-7 MPa |
| Reactor inlet temperature | 280 K (post-cooling jacket) | 300 K |
| Reactor outlet temperature | 2500-2700 K | 2900-3000 K |
| Mass flow rate | 27 kg/s | 10-40 kg/s |
| Burn duration | 60-120 min | 30-60 min/burn |

The unique NTP challenge is **hydrogen embrittlement**. Atomic hydrogen diffuses into the crystal lattice of refractory metals (tungsten, molybdenum, niobium alloys) and causes intergranular cracking. NERVA fuel elements that ran too hot or too long showed lattice damage after only a few hours of operation. Modern designs either use CERMET matrices (which isolate the hydrogen from the refractory metal) or replace refractory claddings with silicon carbide composites that are immune to embrittlement.

LH2 storage for multi-month missions is the second challenge. NTP vehicles stage from LEO, where solar heating boils off 0.1-3% of the LH2 per day depending on tank insulation. A Mars transit that stages in LEO and burns after 30 days of coast needs active cryocoolers or zero-boiloff systems — the same technology used for [Cryogenic Liquefaction & Storage](../cryogenics/liquefaction-storage.md), scaled to tonnes of LH2.

## Nozzle Integration

The NTR nozzle is a convergent-divergent nozzle operating in vacuum, fed with hot hydrogen at 2500-3000 K. Because hydrogen is the lowest-molecular-weight propellant in use, and because the engine operates in vacuum with no atmospheric back-pressure, NTR nozzles use very high expansion ratios — typically **80:1 to 300:1** — to maximise exhaust velocity. The Space Shuttle Main Engine (RS-25), for comparison, runs at 77.5:1 because it stages in atmosphere; an NTR that ignites in LEO can expand to 200:1 without flow separation.

Two nozzle architectures have flown in ground test:

- **Refractory nozzle** (NERVA): a graphite or carbon-carbon nozzle with refractory metal liners (Nb, Ta, W), radiatively cooled to space. Heavy but simple. Survives 2700 K hydrogen for tens of minutes.
- **Regeneratively-cooled nozzle** (modern designs): the LH2 propellant is pumped through channels in the nozzle wall before entering the reactor. This cools the nozzle to 300 K on the metal side while preheating the propellant, recovering waste heat as thrust. The technology is identical to chemical-engine regen nozzles — see [Nozzle Integration](./nuclear-thermal.nozzle-integration.md).

A nozzle-integration subtlety: the exhaust plume of an NTR contains trace fission products (from fuel-element corrosion) and is mildly radioactive. Engines must be started only after the vehicle is on a trajectory that does not point the plume back at Earth or at other spacecraft.

### Nozzle Materials Trade-off

The nozzle material selection is a thermal-vs-mass trade-off:

| Material | Max Service Temp (K) | Density (g/cm³) | Hydrogen Compatibility | Use Case |
|----------|---------------------|-----------------|------------------------|----------|
| Carbon-carbon composite | 3300 (radiative) | 1.8 | good (coated) | NERVA-class refractory nozzles |
| Niobium C-103 alloy | 1500 (regen-cooled) | 8.57 | good | regen-cooled nozzle walls |
| Copper alloy (GlidCop/Narloy-Z) | 800 (channel wall) | 8.9 | excellent | RS-25-derived regen channels |
| Silicon carbide composite | 2700 (radiative) | 2.5 | excellent | modern lightweight nozzles |
| Tungsten (W-Re) | 3000 (radiative) | 19.3 | fair (embrittlement) | radiation-shield backing |

Carbon-carbon is the mass-efficient choice for radiatively-cooled nozzles; copper alloy is the temperature-efficient choice for regen channels; silicon carbide composites are the modern compromise being qualified for the DRACO programme.

## Shadow Shield

An NTR reactor produces intense fast-neutron and gamma flux — enough to deliver a lethal dose in seconds at 100 m. Crewed vehicles place a **shadow shield** between the reactor and the crew compartment: a cone of shielding that absorbs radiation only in the direction of the spacecraft, letting the rest radiate freely into space. This minimises shield mass, which is critical because every kilogram of shield mass is a kilogram taken from payload.

A typical shadow shield is a sandwich of:

- **Lithium hydride (LiH)** — 0.5-1.5 m thick; moderates fast neutrons to thermal energies (where they are captured by Li-6) and is the lowest-mass neutron shield per unit attenuation.
- **Tungsten or depleted uranium** — 5-10 cm thick; attenuates gamma rays by photoelectric absorption and pair production. Tungsten is preferred over lead for its higher temperature capability and lower sputtering.
- **Optional hydrogenous layer** — polyethylene or water, sometimes added for additional neutron moderation at lower temperatures than LiH.

A 2-tonne shadow shield at 10-15 m from a 1 GW reactor reduces the crew dose to roughly 5 rem/year, comparable to the background dose at the International Space Station. The reactor itself has no pressure vessel and no biological shield — that mass would be wasted in space, where radiation only needs to be steered *away* from what matters.

### Crew Dose Calculation

The dose behind a shadow shield follows an inverse-square plus exponential attenuation model. For a 1 GW reactor producing 10^14 neutrons/cm²/s at 1 m and 10^7 rad/h gamma at 1 m, with a 1-tonne LiH+W shield (2 half-value layers for gammas, 10 decades for thermal neutrons):

| Distance (m) | Unshielded dose | Dose behind 2-tonne shield |
|--------------|-----------------|-----------------------------|
| 10 | 10^4 rem/h (lethal in minutes) | 0.5 mrem/h (~4 rem/year) |
| 25 | 1.6×10^3 rem/h | 0.08 mrem/h (~0.7 rem/year) |
| 50 | 400 rem/h | 0.02 mrem/h (~0.2 rem/year) |

The shield is sized so that crew dose over a Mars transit (90 days burn-coast-burn, plus 500 days on the surface with the reactor shutdown) stays under the 50-rem NASA career limit for a single mission. Increasing the separation from 10 m to 25 m lets the shield mass drop from 2 tonnes to 1 tonne — which is why crewed NTP vehicles are long and thin, with the reactor at the tip and the crew cabin at the far end of a truss.

See [Radiation Shielding](./nuclear-thermal.radiation-shielding-engine.md) for the dedicated process. This is distinct from the reactor vessel shielding documented under [Nuclear Fission Power](../energy/nuclear-fission.md), which is a full-surround ground-reactor design with no mass constraint.

## Comparison — NTP vs Chemical vs Nuclear Electric

| Parameter | Chemical (LOX/LH2) | NTP (LH2) | Nuclear Electric |
|-----------|-------------------|-----------|------------------|
| Isp (s) | 440-465 | 850-1000 | 3000-7000 |
| Thrust (kN) | 200-7600 | 110-330 | 0.001-0.5 |
| Thrust-to-weight | 30-80 | 3-8 | 0.0001-0.001 |
| Burn duration | minutes | minutes | weeks to months |
| Mission mode | impulsive burns | impulsive burns | continuous low-thrust |
| Mars transit (crewed) | 180 days | 90-120 days | not crewed |
| Reactor required | no | yes (1-4 GW) | yes (0.1-1 MWe) |
| Test status | operational | ground-tested (NERVA) | conceptual (JIMO) |

The table captures why NTP exists at all: it is the only option that combines enough thrust for impulsive burns (avoiding weeks of Van Allen transit) with enough Isp to halve the Mars transit time. Chemical cannot do the Isp; nuclear electric cannot do the thrust. NTP is the middle ground for crewed Mars.

## Mission Applications

- **Crewed Mars transit** — the canonical NTP mission. A 25-tonne NTR stage with 50 tonnes of LH2 can deliver a crewed capsule to Mars in 90-120 days (vs 180 for chemical), halving crew radiation exposure and zero-g deconditioning. NASA's DRMA reference mission uses three NTR stages sized at 25 klb (111 kN) each.
- **Lunar cargo tug** — a reusable NTR that ferries cargo between LEO and lunar orbit, returning to LEO for refuelling. The high Isp allows 2-3× the payload of chemical tugs per kg of propellant launched from Earth.
- **Cislunar exploration** — NTP enables fast-spiralling crewed missions to near-Earth asteroids (90-day round trips) and to the Mars moons (150-day).
- **Outer planet probes** — for uncrewed flagship missions to Jupiter, Saturn, and beyond, NTP halves the transit time of chemical trajectories. The trade versus nuclear electric is shorter mission duration (NTP) versus higher delivered mass at destination (NEP).

### Mars Transit Delta-v Budget

A crewed Mars mission using NTP follows a roughly 90-120 day transit each way. The delta-v budget for a conjunction-class mission (long surface stay, ~500 days):

| Burn | Delta-v (m/s) | Burn duration | Propellant (t, per 100 t IMLEO) |
|------|--------------|---------------|--------------------------------|
| LEO departure (TMI) | 4200 | 25 min | 32 |
| Mars capture (MOI) | 2700 | 15 min | 14 |
| Mars departure (TEI) | 2100 | 12 min | 8 |
| Earth re-entry | 0 (aerocapture) | — | — |
| Reserves + course corrections | 500 | multiple | 3 |
| **Total** | **9500** | **~55 min** | **57** |

For a chemical LOX/LH2 mission the same transit requires ~12000 m/s delta-v (less efficient trajectory) at 450 s Isp, requiring 89 tonnes of propellant per 100 t of initial mass — 56% more propellant, all of which must be launched from Earth. The NTP advantage is not the Isp number alone; it is the Isp multiplied by the trajectory efficiency, which compounds.

## Manufacturing Challenges

The reasons NTP has not flown since NERVA are industrial, not scientific:

- **Enriched uranium supply** — NTR cores use 20-93% enriched U-235, requiring the same enrichment infrastructure as nuclear weapons. Civilian NTP programmes must source fuel from existing stockpiles or commercial enrichment cascades qualified for HEU.
- **Refractory-metal fabrication** — tungsten, molybdenum, niobium, and tantalum fuel-element claddings require vacuum-arc remelting, electron-beam welding, and hot isostatic pressing at 2000+ K. Only a handful of facilities worldwide produce refractory-matrix CERMET fuel.
- **Hydrogen-compatible coatings** — chemical-vapour-deposited ZrC and NbC coatings, a few micrometres thick, must be defect-free over millions of fuel-element channels. NERVA-era coatings had pinhole densities of ~1/cm²; modern programmes target <0.001/cm².
- **Ground test stands** — NERVA was tested at Jackass Flats in open air, exhausting radioactive hydrogen to atmosphere. Environmental regulations now require closed-loop capture of fission products or testing in a sealed underground vacuum chamber, which no facility currently provides at NTR scale.
- **Launch licensing** — launching a reactor (even cold, subcritical, with fuel loaded) requires a Presidential nuclear safety launch approval in the United States, a multi-year review process with no precedent for an NTR.

## Recent Programmes

After NERVA's 1973 cancellation, NTP work continued at low levels in the Soviet Union (RD-0410, ground-tested 1978-1989, 70 kN thrust, 30 MW, 800 s Isp, ~1 hour cumulative operation), then revived in the United States with the Space Exploration Initiative (1989), the Prometheus programme (2003, focused on nuclear electric), and most recently the DRACO programme (Demonstration Rocket for Agile Cislunar Operations, 2023-present). DRACO, a joint NASA-DARPA-NNSA effort, targets a 2027 in-space flight demonstration of a low-enriched-uranium (<20% U-235) NTR producing ~7 kN thrust at 700+ s Isp — the first NTP flight test if it flies. The low-enriched-uranium fuel avoids the weapons-proliferation concerns that have historically blocked civilian NTP, at the cost of lower power density (~0.1 GW/m³ vs NERVA's 0.25) and lower Isp (~700 s vs 900 s).

## Glossary

- **Isp** — specific impulse (seconds); exhaust velocity divided by g (9.81 m/s²). Higher is better.
- **Expander cycle** — turbopump cycle where propellant vaporises in the nozzle cooling jacket and drives the turbine before entering the combustion chamber (or reactor core, for NTP).
- **Shadow shield** — a directional radiation shield that protects only a cone behind it; used to minimise shield mass on spacecraft.
- **LiH** — lithium hydride; a low-mass neutron shield used in NTP shadow shields.
- **CERMET** — ceramic-metal composite fuel; typically UO₂ particles in a tungsten or molybdenum matrix.
- **TRISO** — tristructural-isotropic fuel; uranium-bearing kernels coated in successive layers of pyrocarbon and silicon carbide.
- **TMI** — trans-Mars injection; the burn that puts a vehicle on a trajectory to Mars.
- **MOI** — Mars orbit insertion; the capture burn at Mars arrival.
- **TEI** — trans-Earth injection; the burn that departs Mars for the return transit.

## What This Article Does Not Cover

Per the task brief, this article focuses on propulsion-specific aspects and does not duplicate reactor physics. The following are documented under [Nuclear Fission Power](../energy/nuclear-fission.md):

- Reactor neutronics, criticality, control drums, and burnup
- Fuel fabrication (enrichment, pelletising, cladding) for stationary reactors
- Fuel-cycle chemistry (uranium mining, conversion, enrichment to 20-93% U-235)
- Reactor safety (decay heat, scram systems, defence-in-depth)
- Terrestrial reactor vessel and containment building design

NTP inherits all of these. What NTP adds — propellant-as-coolant, expander cycle turbopump, hot-hydrogen nozzle, shadow shield geometry — is what makes it a rocket engine and not just a reactor with a hole in one end.

## See Also

- [Nuclear Electric Propulsion](./nuclear-electric.md) — the competing nuclear-space-propulsion architecture
- [Nuclear Fission Power](../energy/nuclear-fission.md) — the reactor heritage that NTP depends on
- [Cryogenic Liquefaction & Storage](../cryogenics/liquefaction-storage.md) — LH2 storage and transfer
- [Reactor Core Design](./nuclear-thermal.reactor-core-design.md) — NTP core design process
- [Propellant Feed System](./nuclear-thermal.propellant-feed.md) — LH2 expander cycle
- [Nozzle Integration](./nuclear-thermal.nozzle-integration.md) — hot-hydrogen nozzle
- [Radiation Shielding](./nuclear-thermal.radiation-shielding-engine.md) — shadow shield design

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md) • [All Domains](../index.md)*
