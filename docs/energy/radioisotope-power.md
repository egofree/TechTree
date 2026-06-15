# Radioisotope Power

> **Node ID**: energy.radioisotope-power
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.nuclear-fission.isotope-production`](./isotope-production.md),
> [`ehs.radiation-safety`](../ehs/radiation-safety.md),
> [`energy.electricity`](./electricity.md),
> `energy`
> **Enables**: None
> **Timeline**: Years 30-100+
> **Outputs**: radioisotope_electricity, radioisotope_heat, radioisotope_power
> **Critical**: No — not on the minimum-viable path. Every radioisotope power system presupposes a operating reactor producing heat-source isotopes, hot-cell fuel fabrication, thermoelectric or dynamic-conversion hardware, and a launch-qualified safety case. These arrive late in the industrial buildup, after [nuclear fission](./nuclear-fission.md) is already delivering baseload power.

## Overview

Radioisotope power systems (RPS) convert the heat and particle energy of decaying radioactive isotopes into electricity. Unlike fission reactors, there is no chain reaction — the fuel simply decays at a fixed rate determined by its half-life, releasing energy steadily for decades with no moving parts, no refueling, and no operator intervention. A plutonium-238 RTG launched in 1977 still powers Voyager 1 today, 47 years later.

This capability matters for three reasons. First, it is the only practical power source for deep-space missions beyond Jupiter, where solar flux falls below usable levels. Second, it delivers 100-year unattended operation for terrestrial and marine sensors, polar stations, and navigation aids where maintenance is impossible. Third, thermoelectric conversion is entirely solid-state — no turbines, no bearings, no lubricant — so failure rates are set by radioactive decay physics, not mechanical wear.

In the tech tree, radioisotope power sits downstream of four prerequisites. [Nuclear fission](./nuclear-fission.md) provides the neutron flux to irradiate target nuclides. [Isotope production](./isotope-production.md) handles the chemical separation of Pu-238, Sr-90, Am-241, and Co-60 in shielded hot cells. [Radiation safety](../ehs/radiation-safety.md) infrastructure governs hot-cell work, dosimetry, and the launch-accident safety case. [Electricity](./electricity.md) capability provides the power conditioning — shunt regulators, DC-DC converters, and charge controllers — that interfaces the generator to its load bus.

## Materials

- **Plutonium-238 dioxide (²³⁸PuO₂)** — Primary fuel for space RTGs. 0.57 W/g specific power, 87.7-year half-life, pure alpha emission. See [Isotope Production](./isotope-production.md).
- **Strontium-90 titanate (SrTiO₃)** — Fuel for terrestrial RTGs (Beta-M, SNAP-7). 0.46 W/g, 28.8-year half-life, beta emission requiring heavy shielding.
- **Iridium-0.3% clad** — 0.6 mm capsule wall encapsulating each Pu-238 fuel pellet. Survives 1400°C re-entry temperatures. See [Metals](../metals/index.md).
- **Fine Weave Pierced Fabric (FWPF) graphite** — Aeroshell material that ablates during atmospheric re-entry, protecting the iridium clad.
- **Lead telluride (PbTe) / Tellurium-antimony-germanium-silver (TAGS)** — Thermoelectric couple materials for the SNAP-19 and GPHS-RTG converters.
- **SK-3 silicon-germanium (SiGe)** — Thermoelectric material for high-temperature RTG couples (Voyager MHW-RTG, GPHS-RTG).
- **Aerogel insulation** — Multi-layer insulation packages that prevent heat loss from the hot junction to the radiator. See [Ceramics](../ceramics/index.md).

## Conversion Methods

Seven physical principles have been explored for converting decay energy to electricity. Each conversion method will receive a dedicated sub-article; this overview compares them and identifies the bootstrap-relevant subset.

### Thermoelectric (Seebeck Effect)

A temperature gradient across a thermocouple (doped bismuth telluride, lead telluride, or silicon-germanium) drives electrons from hot junction to cold junction via the Seebeck effect. No moving parts, no fluids, no optics. Thermoelectric conversion has powered every RTG ever flown — from SNAP-3 in 1961 to the MMRTG on Perseverance. The penalty is low efficiency: 5-8% of decay heat becomes electricity, the rest radiates to space.

Thermoelectric materials are characterised by the figure of merit ZT = S²σT/κ, where S is the Seebeck coefficient, σ is electrical conductivity, and κ is thermal conductivity. Higher ZT means more electricity extracted per unit of heat flow. PbTe (ZT ≈ 0.8 at 800 K) and SiGe (ZT ≈ 0.6 at 1300 K) have been the workhorse materials since the 1960s. Modern segmented couples that layer different materials across the temperature gradient push effective ZT above 1.0, which is the focus of the Next-Gen RTG programme.

The `thermoelectric-rtg` sub-article covers couple geometry, degradation mechanisms (sublimation of Te, dopant diffusion), and the 87-year degradation curves extracted from Voyager telemetry.

### Stirling (Dynamic Conversion)

Free-piston Stirling engines convert heat to mechanical motion via oscillating helium pistons driving linear alternators. The Advanced Stirling Radioisotope Generator (ASRG) achieved 28.6% efficiency — four times thermoelectric — at 7.0 W/kg specific power. A 143 W unit needed only one-eighth the plutonium of an equivalent MMRTG.

Stirling conversion moves the complexity bottleneck from fuel scarcity (plutonium) to mechanical reliability (bearings, seals, helium retention). The ASRG used flexure bearings that never touch their housing — the piston floats on gas bearings — but helium leaks through any seal at a rate that limits lifetime to 14-17 years. Vibration from the oscillating piston couples into sensitive science instruments and must be actively cancelled.

The ASRG was cancelled in 2013 in favour of continued MMRTG production, but Stirling technology continues under the [Stirling Engine](./engine.md) capability. The `stirling-isotope-generator` sub-article will cover the ASRG architecture, helium retention, and vibration cancellation.

### Thermophotovoltaic (TPV)

Heat from the isotope source emits infrared photons that a low-bandgap photovoltaic cell (GaSb, InGaAs) converts to electricity. No moving parts, but the cell must absorb infrared rather than visible light. In 2024, a National Science Foundation study demonstrated 32.5% efficiency at a 1309 K emitter temperature — exceeding Stirling without mechanical complexity.

TPV systems pair an emitter (tungsten or silicon carbide heated to 1300-1500 K by the isotope) with a low-bandgap photovoltaic cell (GaSb at 0.67 eV, InGaAs at 0.6-0.74 eV tuned to the emitter's infrared spectrum). A selective filter reflects sub-bandgap photons back to the emitter, boosting efficiency. The 2024 result at 32.5% used a tandem cell architecture.

TPV is maturing under the advanced-isotope-conversion track. Current TRL is 4 (laboratory demonstrations); flight qualification is a decade away.

### Betavoltaic

Beta particles (electrons) from a low-energy source such as nickel-63 or tritium are captured directly by a semiconductor junction, generating current without thermal conversion. Power is in the microwatt range — 100 µW from the Betavolt BV100 (Ni-63 on diamond, mass production announced 2025). Betavoltaics power cardiac pacemakers, industrial sensors, and memory backup for decades with no decay of output.

The BV100 uses a nickel-63 source (67 keV max beta energy, 100-year half-life) sandwiched between 4-micron diamond semiconductor layers. The diamond survives the beta bombardment because Ni-63 betas are low-energy — they damage the lattice slowly enough that the 100-year half-life dominates lifetime. Higher-energy beta sources (Sr-90 at 2.28 MeV) would destroy a semiconductor junction in hours.

Betavoltaics cannot scale to space missions, but they fill a niche for zero-maintenance micro-power that no other source addresses. The `advanced-isotope-conversion` sub-article will cover betavoltaic cell design and the diamond semiconductor frontier.

### Alpha-Voltaic

Alpha particles from Pu-238 or Am-241 strike a wide-bandgap semiconductor (GaN, SiC, diamond), generating electron-hole pairs. A 2023 paper in Nature Communications Materials reported 4.51% efficiency from a GaN PIN diode irradiated by a Pu-238 source. Theoretical limits are higher (each 5 MeV alpha particle generates 10⁶ electron-hole pairs), but lattice damage from alpha bombardment degrades the cell within days to weeks.

Current work focuses on defect-tolerant diamond and structured junctions that channel alphas along controlled paths, spreading damage over a larger volume. Alpha-voltaic conversion is at TRL 3-4, laboratory only. The `advanced-isotope-conversion` sub-article will cover lattice damage modelling and wide-bandgap materials.

### Thermionic

Heat boils electrons off a hot cathode (T > 1500 K) that cross a vacuum gap to a cold anode. Thermionic conversion was investigated heavily in the 1960s for space reactors and radioisotope systems. The requirement for cathode temperatures above 1500 K proved incompatible with the 1270 K surface temperature of a Pu-238 source, and emitter degradation from vaporised materials limited lifetime.

Thermionic conversion has been largely abandoned for RPS in favour of thermoelectric and Stirling. Research continues for solar and fission-heated converters where higher temperatures are available.

### Piezoelectric

Decay heat drives a bimorph or mechanical oscillator that flexes a piezoelectric ceramic (PZT), converting strain to charge. Research-stage demonstrations produce milliwatts. No flight heritage. Piezoelectric conversion for RPS remains a laboratory curiosity without a clear performance advantage over thermoelectric or betavoltaic alternatives.

## Conversion Method Comparison

| Method | Efficiency | Specific Power | Moving Parts | TRL | Example |
|--------|------------|----------------|--------------|-----|---------|
| Thermoelectric | 6% | 2.8-5.3 W/kg | No | 9 | MMRTG (Curiosity, Perseverance) |
| Stirling | 28.6% | 7.0 W/kg | Yes | 6 | ASRG (cancelled 2013) |
| TPV | 19-32.5% | ~21 W/kg (theoretical) | No | 4 | Lab demos (2024, 32.5%) |
| Betavoltaic | 10-18% | µW range | No | 8 | BV100 (Betavolt, 2025) |
| Alpha-voltaic | 2-4.5% | lab only | No | 3 | GaN PIN diode (2023) |
| Thermionic | 10-15% | 1-5 W/kg | No | 5 | SNAP-10A (abandoned for RPS) |
| Piezoelectric | <1% | mW range | Yes | 2 | Research prototypes |

Thermoelectric dominates flown missions. Stirling holds the efficiency record but carries mechanical risk. TPV is the leading candidate for next-generation solid-state systems. Betavoltaic occupies a separate micro-power niche that does not compete with the others.

## Fuel Isotope Comparison

The choice of radioisotope determines half-life, power density, shielding mass, and the irradiation route. Detailed production chemistry is covered in [Isotope Production](./isotope-production.md); fuel encapsulation and safety qualification in the `isotope-fuel-fabrication` sub-article.

| Isotope | Half-Life | Specific Power | Decay Mode | Shielding | Primary Use |
|---------|-----------|----------------|------------|-----------|-------------|
| Pu-238 | 87.7 yr | 0.57 W/g | Alpha | Minimal (light) | Space RTGs, RHUs |
| Sr-90 | 28.8 yr | 0.46 W/g (as SrTiO₃) | Beta | Heavy (bremsstrahlung) | Terrestrial RTGs (Beta-M) |
| Am-241 | 432 yr | 0.11 W/g | Alpha | Minimal (light) | Long-life terrestrial, deep-space |
| Co-60 | 5.3 yr | 1.7 W/g | Beta + gamma | Very heavy (lead) | Industrial heat, short missions |
| Cs-137 | 30.0 yr | 0.28 W/g (as CsCl) | Beta + gamma | Heavy (lead) | Sterilization, terrestrial heat |

Pu-238 dominates space missions because its pure alpha emission requires no heavy shielding, its 88-year half-life matches mission durations, and its 0.57 W/g specific power is high enough to build practical generators. Sr-90, recovered from spent fuel, is the workhorse for terrestrial applications where shield mass is tolerable. Co-60 delivers the highest specific power but its 5.3-year half-life and intense gamma emission limit it to short industrial runs. Cs-137 is abundant as a fission product but gamma emission forces heavy containment.

## Historical Timeline

Radioisotope power flight heritage spans six decades and four generations of generators. The United States has launched 27 RPS missions; the Soviet Union and Russia launched over 40, mostly Sr-90 terrestrial and marine units.

### SNAP-3 (1961, Transit 4A)

The first radioisotope generator in space. 2.7 W_e from 2.1 kg of Pu-238 metal, paired with a thermoelectric converter. Proved that nuclear power could operate in orbit. The SNAP programme (Systems for Nuclear Auxiliary Power) ran from 1955 to 1973 and developed 10 generations of generators spanning thermoelectric, dynamic, and reactor architectures.

### SNAP-19 (1968-1976)

Improved thermoelectric design using PbTe/TAGS couples. Powered Nimbus-B (1968, launch failure — RHUs survived intact, recovered from the ocean floor), Pioneer 10/11 (launched 1972/1973, last signal from Pioneer 10 in 2003), and the Viking Mars landers (1976). Pioneer 10 was the first spacecraft to leave the solar system, powered by four SNAP-19Bs delivering a combined 160 W at launch. Each SNAP-19 carried approximately 0.5 kg of Pu-238.

### MHW-RTG (1976-1977)

The Multi-Hundred Watt RTG used silicon-germanium thermocouples and a modified heat source. Powered Voyager 1 and Voyager 2 (launched 1977), LES-8/9 (1976), and Lincoln Experimental Satellites. Each MHW-RTG delivered 158 W_e at launch from 4.5 kg of Pu-238 dioxide. Voyager 1 and 2 continue transmitting from interstellar space — 47 years of continuous operation, with power now at 249 W from an initial 470 W.

### GPHS-RTG (1989-2006)

The General Purpose Heat Source RTG was the standard for two decades. Each unit delivered 285 W_e at 5.1 W/kg specific power, using 4.4 kg of Pu-238 dioxide in 18 General Purpose Heat Source modules. Powered Galileo (Jupiter, launched 1989), Ulysses (solar polar orbit, 1990), Cassini (Saturn, 1997), and New Horizons (Pluto, 2006 — still operating beyond the solar system). Cassini carried three GPHS-RTGs delivering 885 W at launch, sufficient to power the orbiter's instruments through a 13-year Saturn tour.

### MMRTG (2011-present)

The Multi-Mission RTG replaced the space-specific GPHS-RTG with a design qualified for both vacuum and planetary atmospheres (Mars surface pressure is 600 Pa, enough to affect thermal performance). Delivers 110 W_e at launch at 2.8 W/kg specific power, using 4.8 kg of Pu-238 dioxide and PbTe/TAGS thermocouples. Powers Curiosity (MSL, landed 2012), Perseverance (Mars 2020, landed 2021), and the Dragonfly rotorcraft mission to Titan (launch 2028). The lower specific power versus GPHS-RTG reflects the heavier, atmosphere-rated converter design and conservative thermal margins.

### Next-Gen RTG (in development)

NASA and the Department of Energy are developing a modernised thermoelectric RTG using segmented couples (higher ZT material combinations — CoSb₃ skutterudite on the hot side, Bi₂Te₃ on the cold side) and enhanced GPHS modules. Target: 130+ W_e at 3.5 W/kg with a 20% reduction in plutonium loading. First flight anticipated late 2020s. The Next-Gen design preserves the solid-state reliability of thermoelectric conversion while closing the specific-power gap with Stirling.

### Flight Mission Summary

| Mission | Generator | Power (W_e) | Pu-238 (kg) | Year | Status |
|---------|-----------|-------------|-------------|------|--------|
| Transit 4A | SNAP-3 | 2.7 | 2.1 | 1961 | Decommissioned |
| Pioneer 10 | SNAP-19B | 40 (each) | 0.5 (each) | 1972 | Last contact 2003 |
| Viking 1/2 | SNAP-19 | 42 (each) | 0.5 (each) | 1976 | Decommissioned |
| Voyager 1/2 | MHW-RTG | 158 (each) | 4.5 (each) | 1977 | Operating (249 W, 2024) |
| Galileo | GPHS-RTG | 285 (each) | 4.4 (each) | 1989 | Decommissioned 2003 |
| Cassini | GPHS-RTG | 295 (each) | 4.4 (each) | 1997 | Decommissioned 2017 |
| New Horizons | GPHS-RTG | 245 | 4.4 | 2006 | Operating |
| Curiosity | MMRTG | 110 | 4.8 | 2011 | Operating on Mars |
| Perseverance | MMRTG | 110 | 4.8 | 2021 | Operating on Mars |

## Radioisotope Heater Units (RHUs)

Not every radioisotope power system generates electricity. Radioisotope Heater Units provide pure heat — 1.1 W_th each from 2.7 g of Pu-238 dioxide, packaged in a 40-gram capsule. The Light Weight Radioisotope Heater Unit (LWRHU) uses a Pt-30% Rh clad (0.6 mm wall), a FWPF graphite aeroshell, and a carbon-carbon impact shell to survive launch accidents and atmospheric re-entry.

Each Mars rover carries 8-12 RHUs to keep electronics above minimum operating temperature during Martian nights (−90°C) and winter. The Apollo ALSEP surface science packages used RHUs to survive lunar nights (−180°C). Cassini carried 82 RHUs for thermal control during its Saturn tour. Galileo carried 120 RHUs.

A single RHU's 1.1 W output is trivial, but it arrives with 100% reliability for decades — no electrical failure mode, no moving parts, no telemetry to monitor. The heat simply arrives, day and night, for the 87-year half-life of the fuel.

### RHU Construction

The LWRHU (Light Weight Radioisotope Heater Unit) is the smallest flown radioisotope device. Each unit measures 3.2 cm long and 2.6 cm in diameter, weighing 40 g total. The fuel is a 2.7 g pellet of ²³⁸PuO₂ pressed to high density. The clad is Pt-30% Rh (platinum-rhodium), chosen for its ductility, oxidation resistance at re-entry temperatures, and compatibility with the fuel chemistry. The aeroshell is FWPF graphite — a three-directional carbon-carbon composite woven for isotropic strength. A carbon-bonded carbon-carbon (CBC-C) insulator sits between the aeroshell and the clad. The complete assembly survives 1400°C re-entry, 50 m/s ground impact, and explosive overpressure equivalent to a launch vehicle detonation.

## Bootstrap Path

Radioisotope power arrives late in the bootstrap sequence because it requires a operating reactor first. The path has two tiers.

### Minimum Tier

A research or isotope-production reactor producing modest neutron flux can irradiate Co-59 targets to produce Co-60, or separate Sr-90 and Cs-137 from spent fuel using standard PUREX chemistry. A Sr-90-fuelled thermoelectric generator like the Soviet Beta-M (10 W_e, ~560 kg, deployed from the 1970s for unattended lighthouse and navigational beacon power along the Arctic coast) is achievable once hot-cell chemistry and lead shielding are available.

Beta-M units operated for 10+ years with no maintenance in Arctic conditions. This tier sacrifices specific power (W/kg) for accessibility — the isotopes are fission products, not requiring specialised target irradiation. Sr-90 titanate is chemically stable, insoluble in water, and has a melting point of 1910°C, making it a forgiving fuel form for imperfect fabrication conditions.

### Full Tier

Pu-238 production requires dedicated Np-237 target irradiation. Np-237 is a minor actinide recovered from spent reactor fuel during reprocessing. Targets are fabricated as NpO₂-Al cermet, loaded into reactor positions with high thermal neutron flux, and irradiated for 2-4 years. The resulting Np-238 beta-decays to Pu-238 with a 2.1-day half-life. The irradiated target is then dissolved and the Pu-238 separated in hot cells using anion exchange or solvent extraction.

The United States produced Pu-238 at Savannah River until 1988 and resumed production at Oak Ridge National Laboratory in 2015 at a target rate of 1.5 kg/year. Full Pu-238 capability, combined with segmented thermoelectric couples and GPHS-qualified safety containment, enables space missions with specific power above 2.8 W/kg and 14-year design lifetimes. See [Isotope Production](./isotope-production.md) for the irradiation chemistry and target fabrication details.

### Bootstrap Tiers Compared

| Tier | Isotope | Source | Output | Specific Power | Example |
|------|---------|--------|--------|----------------|---------|
| Minimum | Sr-90 | Spent fuel (PUREX) | 10 W_e | 0.018 W/kg | Soviet Beta-M |
| Minimum | Co-60 | Reactor irradiation (Co-59) | 1-100 W_th | 0.1-1.0 W/kg | Industrial heat |
| Full | Pu-238 | Np-237 target irradiation | 110-285 W_e | 2.8-5.1 W/kg | MMRTG, GPHS-RTG |

## Power Conditioning

A radioisotope generator produces DC at a voltage that drifts with temperature and load. The output must be conditioned — regulated, converted, and protected — before it reaches the spacecraft or station bus. See [Electricity Generation & Distribution](./electricity.md) for the broader power-conditioning discussion.

Key elements specific to RPS:

- **Shunt regulators** — The isotope produces constant heat regardless of electrical load. Excess power that the spacecraft cannot use must be dissipated as heat, typically through a shunt resistor that the thermal management system accommodates.
- **DC-DC converters** — RTG output voltage varies from 16-34 V depending on load and temperature. A boost converter steps this up to a standard 28 V or 100 V spacecraft bus with regulated output.
- **Charge controllers** — A rechargeable battery (nickel-hydrogen or lithium-ion) buffers load transients. The charge controller prevents overcharge during periods of low power demand and prevents deep discharge during launch or landing transients.
- **Diode isolation** — Blocking diodes prevent backfeed from the battery into a failed RTG string. RTGs are series-connected in strings of 2-3 to achieve the required bus voltage; if one string shorts, the diode isolates it.

## Safety

Every RPS carries radioactive material through launch, ascent, and potential launch-accident environments. The safety philosophy is defence in depth: multiple barriers contain the isotope through nominal flight, explosion overpressure, shrapnel impact, atmospheric re-entry, and ground impact. See [Radiation Safety](../ehs/radiation-safety.md) for the underlying dose limits and the `isotope-fuel-fabrication` sub-article for the containment hardware.

### Containment Barriers (GPHS Module)

1. **Fuel pellet** — Pu-238 dioxide pressed and sintered to 95% theoretical density. Ceramic form is chemically inert and fractures rather than disperses on impact.
2. **Iridium clad** — 0.6 mm iridium capsule welded shut around each pellet. Survives 1400°C re-entry heating. Iridium was chosen for its ductility at high temperature and resistance to oxidation.
3. **Graphite aeroshell** — FWPF (Fine Weave Pierced Fabric) graphite, 2.5 mm thick. Ablates during atmospheric re-entry, carrying heat away from the iridium clad.
4. **Carbon-carbon impact shell** — Survives ground impact at up to 50 m/s without breaching the aeroshell.

### Launch Approval Process

Each RPS mission requires a Final Safety Analysis Report (FSAR) reviewed by an interagency nuclear safety review board. The analysis demonstrates that the probability of any radioactive release is below 1 in 10,000 per mission, and that the expected dose to any member of the public is below the 0.1 mSv screening threshold — comparable to the dose received during a cross-country airline flight. The FSAR considers launch vehicle failure modes, atmospheric re-entry trajectories, and ground impact on land and water.

## Degradation and Lifetime

RTG output declines predictably over mission lifetime. Three mechanisms drive power loss:

- **Fuel decay** — Pu-238 has an 87.7-year half-life, so thermal output drops 0.79% per year. After 14 years (Curiosity design life), thermal output has declined 10.5%.
- **Thermoelectric degradation** — Thermocouple materials lose efficiency through sublimation of tellurium at the hot junction, dopant diffusion across the couple, and increased contact resistance. PbTe couples degrade approximately 1.5% per year; SiGe couples degrade approximately 0.8% per year.
- **Radiator fouling** — The radiator fins that reject waste heat to space degrade slowly through micrometeoroid impacts and ultraviolet darkening, reducing emissivity.

Combined, these effects reduce MMRTG electrical output by approximately 3-4% per year. Curiosity's MMRTG delivered 110 W at launch (2012) and was producing approximately 80 W by 2024 — a 27% decline over 12 years, consistent with the pre-flight degradation model. Voyager 1's MHW-RTGs delivered 470 W at launch in 1977 and produced approximately 249 W in 2024, a 47% decline over 47 years — remarkably close to the Pu-238 half-life alone, confirming that thermoelectric degradation in SiGe is slower than in PbTe.

Predictable degradation is a feature, not a bug: mission planners know the power available at any future date and can sequence science operations accordingly. No other power source offers this level of lifetime predictability.

## Ground Testing and Qualification

Every RTG design undergoes years of ground testing before flight. The qualification programme includes:

- **Thermal vacuum testing** — The complete generator operates in a vacuum chamber at flight-expected temperatures (−20°C radiator to +1270°C hot junction) for months, simulating mission lifetime thermal cycling.
- **Vibration testing** — Shaker tables reproduce launch vehicle acoustic and structural vibration environments. The GPHS modules must survive pyrotechnic shock, steady-state acceleration, and random vibration without fuel release.
- **Impact testing** — Full-scale GPHS modules are fired at sand, water, and granite targets at 50 m/s to verify containment during launch accidents. The iridium clad and graphite aeroshell must not breach.
- **Re-entry testing** — Arc-jet facilities subject GPHS modules to simulated atmospheric re-entry heating (1400°C for 90 seconds). The aeroshell ablation profile must protect the iridium clad throughout the trajectory.

Ground qualification data feeds into the FSAR launch approval process. No RPS has ever flown without completing this testing matrix.

## Design Trade-offs

| Decision | Options | Trade-off |
|----------|---------|-----------|
| Fuel | Pu-238 vs Sr-90 | Pu-238: higher specific power, lighter shielding. Sr-90: no target irradiation needed, recovered from spent fuel |
| Conversion | Thermoelectric vs Stirling | Thermoelectric: lower efficiency (6%), zero moving parts, 50+ year heritage. Stirling: 28.6% efficiency, moving parts, helium retention limits |
| Shielding | Minimal vs heavy | Alpha-only (Pu-238, Am-241): minimal shielding, lighter unit. Beta/gamma (Sr-90, Co-60): heavy lead or depleted uranium shielding |
| Scale | RHU (1 W) vs RTG (100 W) vs terrestrial (10 W) | RHU: pure heat, 40 g. RTG: electricity, 40-60 kg. Terrestrial: electricity, 500-1000 kg including shielding |

## Comparison with Nuclear Fission

Radioisotope power and [nuclear fission](./nuclear-fission.md) both derive energy from atomic nuclei, but they occupy different niches. Fission sustains a chain reaction to produce megawatts of heat for baseload electricity; radioisotope systems harvest natural decay to produce watts for unattended niche loads.

| Parameter | Nuclear Fission | Radioisotope Power |
|-----------|----------------|-------------------|
| Power output | 1-1500 MW_th | 0.001-300 W_e |
| Fuel | U-235 (3-5% enriched) | Pu-238, Sr-90, Am-241 |
| Refueling | Every 12-24 months | Never (sealed source) |
| Moving parts | Turbine, pumps, control rods | None (thermoelectric) |
| Lifetime | 40-80 years (plant) | 10-100 years (half-life limited) |
| Control | Active (control rods, feedback) | Passive (fixed decay rate) |

A civilization building its first reactor will use the reactor for grid power and reserve its first kilograms of separated Sr-90 or Pu-238 for the missions — polar stations, ocean-floor sensors, deep-space probes — where a reactor is impractical and solar is insufficient.

## Scale and Applications

Radioisotope power systems span six orders of magnitude in output power, each serving a distinct niche:

- **Betavoltaic cells (µW)** — Cardiac pacemakers, industrial sensor memory backup, cryptographic key retention. The BV100 delivers 100 µW for 50+ years. No competing technology matches this combination of lifetime and zero-maintenance.
- **RHUs (1 W_th)** — Spacecraft thermal control. Each Mars rover carries 8-12 RHUs; Cassini carried 82. Pure heat, no electricity, no conversion hardware. The simplest and most reliable radioisotope device.
- **Terrestrial RTGs (10 W_e)** — Unattended lighthouses, navigational beacons, seismic stations, polar weather stations. Soviet Beta-M (Sr-90, 10 W_e) and US SNAP-7 series (Sr-90, 10-60 W_e) served this role from the 1960s through 1990s. Shielding mass dominates system weight (500-1000 kg for 10 W_e).
- **Space RTGs (100-300 W_e)** — Deep-space probes and planetary landers. MMRTG (110 W) for Mars rovers; GPHS-RTG (285 W) for outer-planet missions. Each unit weighs 40-57 kg and carries 4-5 kg of Pu-238.
- **Multi-unit stacks (500-1000 W_e)** — Cassini (3 × GPHS-RTG = 885 W), Voyager (3 × MHW-RTG = 474 W). Scaling is linear: double the plutonium, double the power, double the mass.

No single RPS design serves all niches. The fuel choice (Pu-238 vs Sr-90), conversion method (thermoelectric vs Stirling vs betavoltaic), and shielding strategy are selected per mission based on required power, lifetime, mass budget, and available isotopes.

## Products

| Output | Description | Use Case |
|--------|-------------|----------|
| `radioisotope_electricity` | DC electrical power from decay heat conversion | Spacecraft bus, remote sensors |
| `radioisotope_heat` | Thermal output from encapsulated isotope | Spacecraft thermal control (RHU), industrial heat |
| `radioisotope_power` | Integrated generator system (fuel + converter + containment) | Flight RPS, terrestrial RTG |

## See Also

- [Thermoelectric RTG](./thermoelectric-rtg.md) — Seebeck conversion, thermocouple materials, flight degradation data *(sub-article, Wave 4)*
- [Stirling Isotope Generator](./stirling-isotope-generator.md) — Dynamic conversion, ASRG, free-piston engines *(sub-article, Wave 4)*
- [Isotope Fuel Fabrication](./isotope-fuel-fabrication.md) — Hot-cell encapsulation, GPHS, iridium clad *(sub-article, Wave 4)*
- [Advanced Isotope Conversion](./advanced-isotope-conversion.md) — TPV, alpha-voltaic, betavoltaic frontiers *(sub-article, Wave 4)*
- [Isotope Production](./isotope-production.md) — Reactor irradiation, PUREX, Np-237 to Pu-238
- [Nuclear Fission Power](./nuclear-fission.md) — Reactor design, fuel cycle, parent capability
- [Radiation Safety](../ehs/radiation-safety.md) — Shielding, dosimetry, launch approval
- [Electricity Generation & Distribution](./electricity.md) — Power conditioning, DC-DC conversion
- [Heat Engines](./engine.md) — Stirling engine fundamentals

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
