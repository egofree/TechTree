# Spacecraft Power Systems

> **Node ID**: spacecraft-systems.spacecraft-power
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`energy.photovoltaics`](../energy/photovoltaics.md),
> [`energy.radioisotope-power`](../energy/radioisotope-power.md), `silicon`,
> `electronics`
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: spacecraft_power, solar_arrays, space_batteries
> **Critical**: No — spacecraft power systems synthesize photovoltaic, electrochemical, and nuclear technologies into a single orbital bus, demanding radiation-hardened electronics, vacuum-qualified materials, and decades of qualified cycle testing

A spacecraft without power is inert debris. Every watt of electrical energy on a satellite or probe must be generated, stored, conditioned, and distributed through a system that operates unattended for 5-20 years in vacuum, through temperature swings of 200°C, under constant particle radiation. The spacecraft power system is the intersection of [photovoltaic](../energy/photovoltaics.md) energy conversion, [electrochemical](../energy/batteries.md) storage, [radioisotope](../energy/radioisotope-power.md) thermal generation, and [power electronics](../electronics/index.md) conditioning — each adapted for the space environment.

This article covers the four process areas that constitute spacecraft power: [solar arrays](./spacecraft-power.solar-arrays.md), [space batteries](./spacecraft-power.space-batteries.md), [power management and distribution](./spacecraft-power.power-management-distribution.md), and [RTG integration](./spacecraft-power.rtg-integration.md).

## Overview

The power system architecture follows a simple chain: a primary source generates electricity (solar panels or RTG), a storage buffer absorbs the peaks and valleys (battery), and a distribution network conditions and routes the power to loads (PCDU). Each link is sized for the mission's power profile — the curve of demand versus time over one orbit.

Every spacecraft power budget starts with the **eclipse problem**. In low Earth orbit (LEO), a satellite spends 35-40 minutes of each 90-minute orbit in Earth's shadow. During eclipse, the solar arrays produce nothing and the entire load falls on the battery. A typical LEO Earth-observation satellite draws 0.5-2 kW; over 36 minutes of eclipse, that drains 300-1200 Wh from the battery pack. In geostationary orbit (GEO), eclipses occur only near the equinoxes — 45 minutes per day for 45 days per year — but the mission lifetime is 15 years, demanding 1,500-3,000 deep discharge cycles. A GEO communications satellite typically draws 8-15 kW, requiring battery capacity of 6-12 kWh.

| Orbit | Altitude | Eclipse Duration | Eclipses/Year | Mission Life | Typical Power |
|-------|----------|-----------------|---------------|-------------|--------------|
| LEO (Sun-synchronous) | 500-800 km | 35 min | ~5,500/yr | 3-7 yr | 0.5-2 kW |
| LEO (ISS) | 400 km | 36 min | ~5,500/yr | 15+ yr | 75-90 kW |
| MEO (Navigation) | 20,000 km | 55 min | ~2,400/yr | 12-15 yr | 1.5-4 kW |
| GEO (Comms) | 35,786 km | 72 min (equinox) | ~90/yr | 15-20 yr | 8-15 kW |
| Deep space | — | None/variable | — | 5-50 yr | 0.1-1 kW (RTG) |

## Solar Arrays

Spacecraft solar arrays are NOT terrestrial panels. They use III-V compound semiconductor multi-junction cells grown on germanium substrates, not silicon, because the radiation environment and the mass constraint demand the highest possible efficiency per kilogram. See [Solar Arrays](./spacecraft-power.solar-arrays.md) for the dedicated process article.

### Cell Technology

The state-of-the-art space solar cell is the **triple-junction GaInP/GaAs/Ge** cell. Three photovoltaic junctions are stacked monolithically, each tuned to a different wavelength band of the solar spectrum. The top junction (GaInP, bandgap 1.85 eV) absorbs blue light; the middle junction (GaAs, 1.42 eV) absorbs green-red; the bottom junction (Ge, 0.67 eV) absorbs infrared. This spectral splitting extracts 29.5% of the AM0 (air-mass-zero, space) solar flux at beginning of life (BOL).

| Cell Type | BOL Efficiency | EOL Efficiency (15yr GEO) | Cell Thickness | Radiation Tolerance |
|-----------|---------------|---------------------------|---------------|-------------------|
| Si (legacy) | 14-16% | 10-12% | 200 μm | Poor |
| GaAs single-junction | 19-21% | 15-17% | 140 μm | Moderate |
| Dual-junction GaInP/GaAs | 22-24% | 18-20% | 140 μm | Good |
| Triple-junction GaInP/GaAs/Ge | 28-30% | 24-26% | 140 μm | Good |
| 4-junction (ALSAs) | 30-33% | 26-29% | 140 μm | Very good |

The current production benchmark is the **Azur Space 3G30C** at 29.5% BOL efficiency. After 15 years in GEO (equivalent to 1 MeV electron fluence of 1×10¹⁵ cm⁻²), the same cell degrades to approximately 26.6% EOL — a 10% relative degradation. Silicon cells of equivalent area lose 25-30% over the same period.

### Radiation Degradation

Particle radiation is the dominant lifetime limiter for solar arrays. Trapped protons in the Van Allen belts and solar flare protons displace atoms in the semiconductor lattice, creating recombination centers that reduce cell efficiency. The damage follows a non-linear fluence curve: efficiency is roughly stable below 10¹³ cm⁻², then drops by 15-25% between 10¹⁴ and 10¹⁵ cm⁻².

- **Coverglass**: 100-300 μm fused silica or ceria-doped glass protects the cell front surface. The coverglass absorbs most protons below 1 MeV but is transparent to higher-energy particles. Thickness is traded against mass: 300 μm coverglass stops protons up to 8 MeV; 100 μm stops protons up to 3 MeV.
- **Reverse-bias protection**: Shadowed cells become reverse-biased by illuminated neighbors, dissipating power as heat. Shunt diodes are integrated across every cell string to bypass shadowed sections.
- **Annealing**: Some radiation damage heals thermally — cells recover 2-5% efficiency after sustained operation at 60-80°C. This effect is incorporated into EOL predictions.

### Panel-Level Performance

| Parameter | Value |
|-----------|-------|
| Cell-level BOL efficiency (3G30C) | 29.5% |
| Cell-level EOL efficiency (15yr GEO) | 26.6% |
| Panel-level packing factor | 85-90% |
| Panel-level BOL specific power | 80-150 W/kg |
| Panel-level areal density | 2-5 kg/m² |
| Deployment mechanism mass fraction | 15-25% of panel mass |
| Stowed specific power (compact) | 30-60 kW/m³ |
| Bus voltage range | 28V (small sats) to 100V (large GEO) |

Panel-level specific power of 80-150 W/kg accounts for the cell mass, coverglass, interconnect wiring, substrate (carbon-fiber facesheet on aluminum honeycomb), and deployment hinges. The cells themselves contribute only 30-40% of the total panel mass; the rest is structure and mechanisms.

### Deployment Mechanisms

Solar arrays are stowed folded against the spacecraft body during launch and deployed once in orbit. The deployment system is critical — a jammed hinge means a dead satellite.

- **Spring-hinge deployment**: Folded panels connected by spring-loaded hinges. A pyrotechnic or thermal knife releases the stowed panels; springs drive the unfolding. Simple and reliable — used by most GEO commsats.
- **Flexible blanket deployment**: Cells mounted on a thin Kapton substrate, rolled or folded into a canister. A motorized boom (articulated or coilable) deploys the blanket. Higher packing density — used by the ISS (8 arrays, 4 panels each, 250 kW total).
- **Tracking drives**: Solar array drive assemblies (SADA) continuously rotate the panel to track the Sun, maximizing incidence. Stepper-motor-driven with slip rings for power transfer across the rotating joint.

## Space Batteries

The battery is the eclipse energy buffer. During sunlight, the solar array charges the battery while simultaneously powering the loads; during eclipse, the battery carries the full spacecraft load. See [Space Batteries](./spacecraft-power.space-batteries.md) for the dedicated process article.

### Battery Chemistry Comparison

| Chemistry | Cell Voltage | Energy Density | Cycle Life (50% DoD) | Temperature Range | Heritage |
|-----------|-------------|---------------|---------------------|-------------------|----------|
| NiCd | 1.2V | 40-60 Wh/kg | 10,000-20,000 | -5 to +25°C | Legacy (1970s-90s) |
| NiH₂ | 1.2V | 45-65 Wh/kg | 30,000-35,000 | -10 to +20°C | GEO standard (1980s-2010s) |
| Li-ion | 3.6-3.7V | 150-200 Wh/kg | 20,000-30,000 | 0 to +30°C | Modern (2000s-present) |
| LiFePO₄ | 3.2V | 120-160 Wh/kg | 15,000-25,000 | 0 to +35°C | Emerging (high safety) |

**Nickel-cadmium** (NiCd) was the workhorse of the 1970s-1990s. Each cell delivers 1.2V with robust tolerance to overcharge and deep discharge. The memory effect — a gradual capacity loss if repeatedly partially discharged — required periodic full discharge reconditioning. NiCd packs on the Hubble Space Telescope (launched 1990) were replaced in 2009 after 19 years of service.

**Nickel-hydrogen** (NiH₂) became the GEO standard from the 1980s through 2010s. The NiH₂ cell uses a hydrogen gas electrode in a pressure vessel — charge/discharge cycles change the internal hydrogen pressure from 0.3 to 5 MPa. The pressure vessel provides a built-in state-of-charge indicator (pressure transducer). NiH₂ achieves exceptional cycle life: 35,000 cycles at 40% depth of discharge (DoD) for LEO missions, and 1,500 cycles at 70% DoD over 15 years for GEO. The International Space Station uses NiH₂ batteries (replaced 2017-2021 with Li-ion).

**Lithium-ion** (Li-ion) is the modern standard. The high cell voltage (3.6V vs 1.2V for NiCd/NiH₂) reduces cell count by a factor of 3. Energy density of 150-200 Wh/kg is 2.5-3× better than NiH₂. A 10 kW GEO commsat needs only 100-150 Li-ion cells vs 300-400 NiH₂ cells for the same capacity. The trade is stricter thermal management: Li-ion degrades rapidly above 35°C and cannot safely charge below 0°C without special protocols.

### Cycle Life and Depth of Discharge

Battery cycle life is a strong function of depth of discharge. Deeper cycles mean fewer total cycles before capacity falls below 80% of nominal:

| Depth of Discharge | Li-ion Cycles | NiH₂ Cycles | NiCd Cycles |
|-------------------|--------------|------------|------------|
| 20% DoD | 50,000-80,000 | 60,000-100,000 | 30,000-50,000 |
| 35% DoD | 30,000-50,000 | 35,000-50,000 | 15,000-25,000 |
| 50% DoD | 20,000-30,000 | 20,000-35,000 | 10,000-20,000 |
| 70% DoD | 5,000-10,000 | 10,000-15,000 | 3,000-5,000 |
| 100% DoD | 1,000-3,000 | 3,000-5,000 | 500-1,500 |

A GEO commsat battery is sized for 70% DoD during the worst equinox eclipse, but typically operates at 20-30% DoD for most of the year. This sizing strategy ensures 15-year life with the occasional deep cycle.

### Thermal Management

Battery temperature directly impacts cycle life. Li-ion cells lose 2-3% capacity per year at 20°C; at 35°C they lose 6-8% per year. Spacecraft batteries are mounted on dedicated thermal rails connected to radiator panels via heat pipes or conductive doublers, maintaining the pack between 5°C and 25°C. Battery heaters (resistance elements, 10-50W) prevent freezing during eclipse when the spacecraft radiates to deep space at -150°C.

## Power Management and Distribution

The power management and distribution system is the spacecraft's nervous system for energy. It regulates the solar array output, manages battery charge and discharge, protects against faults, and distributes conditioned power to every subsystem. See [PMAD](./spacecraft-power.power-management-distribution.md) for the dedicated process article.

### Bus Architecture

| Bus Type | Voltage | Regulation | Typical Use | Mass Penalty |
|----------|---------|-----------|-------------|-------------|
| Unregulated | 28V ± 5V | Battery-following | Small sats (< 1 kW) | Low (simpler PCDU) |
| Semi-regulated | 28-50V | Clamped above battery | Medium sats (1-5 kW) | Moderate |
| Fully regulated | 50-100V | Fixed bus voltage | Large GEO (> 5 kW) | Higher (more conversion) |
| High-voltage | 100-160V | Fixed, from direct energy transfer | ISS, large platforms | Higher (insulation) |

The 28V unregulated bus is the simplest architecture — the bus voltage tracks the battery voltage directly (24-32V as the battery charges and discharges). Loads must tolerate this 8V swing. For spacecraft above 5 kW, the bus current at 28V exceeds 180A — distribution harness mass becomes prohibitive. At 100V, the same power flows at only 50A, reducing harness gauge and mass by 60-70%.

### Shunt Regulation

When the solar array produces more power than the spacecraft needs (sunlight, low load, battery full), the excess must be dissipated. The **shunt regulator** diverts current away from the bus into dissipative resistors. Two architectures are common:

- **Sequential shunt**: The solar array is divided into 8-20 sections. The shunt controller switches sections offline one at a time as the bus voltage rises. Each section either feeds the bus fully or is shunted fully. Simple, robust, but causes bus voltage ripple at section switching boundaries.
- **PWM shunt**: A pulse-width-modulated switch continuously varies the fraction of solar array current shunted to the dissipator. Smoother bus voltage regulation but higher switching losses and EMI.

### Battery Charge Management

The PCDU controls battery charge current based on the charge state:

- **Constant current (CC)** phase: Charges at maximum rate until cell voltage reaches the target (4.1V/cell for Li-ion, 1.55V for NiH₂).
- **Constant voltage (CV)** phase: Holds voltage constant as current tapers. Terminates when current drops below C/20.
- **Trickle/top-off**: Low current to offset self-discharge. Li-ion uses voltage-limited float; NiH₂ uses periodic full charges with taper-charge cycling.

Overcharge is catastrophic for Li-ion — cells swell, vent, and can ignite. The charge controller must limit voltage to ±25mV per cell. Battery management electronics monitor individual cell voltages and temperatures, disconnecting any cell that exceeds safe limits.

## RTG Integration

For missions beyond Mars orbit, solar arrays become impractically large — the solar flux at Jupiter is 1/25 of Earth's. The alternative is the [radioisotope thermal generator](../energy/radioisotope-power.md), which converts the heat of decaying plutonium-238 into electricity. See [RTG Integration](./spacecraft-power.rtg-integration.md) for the dedicated process article.

### RTG Characteristics

The RTG itself is produced by the `energy.radioisotope-power` capability — spacecraft power engineers integrate it into the bus, they do not manufacture the RTG. Two flight-qualified designs dominate:

| RTG Model | Electrical Output | Thermal Output | Pu-238 Mass | Specific Power | Flight Heritage |
|-----------|------------------|----------------|-------------|---------------|----------------|
| GPHS-RTG | 300W (BOL) | 4,400W | 7.8 kg | 5.2 W/kg (system) | Voyager, Cassini, Galileo, New Horizons |
| MMRTG | 125W (BOL) | 2,000W | ~4.8 kg (4.8 kg PuO₂) | 2.8 W/kg (system) | Curiosity, Perseverance rovers |
| eMMRTG | 110W (BOL, 16yr EOL) | 2,000W | ~4.8 kg | 2.5 W/kg (system) | Dragonfly (2028) |

The **GPHS-RTG** (General Purpose Heat Source RTG) uses 18 GPHS modules containing a total of ~7.8 kg of Pu-238 dioxide, producing 300W electrical at beginning of life via SiGe thermocouples. The half-life of Pu-238 is 87.7 years, so power degrades at ~0.8% per year from isotope decay alone, plus ~0.4%/yr from thermocouple degradation — the 300W BOL unit delivers ~200W after 30 years.

The **MMRTG** (Multi-Mission RTG) is the modern standard: 125W electrical at BOL, using 8 GPHS modules with PbTe/TAGS thermocouples operating at lower hot-side temperature (575°C vs 1000°C for GPHS-RTG). Lower efficiency (6.2% vs 6.8%) but longer thermocouple life and scalable output for smaller missions.

### Integration Architecture

RTG output voltage varies with load and temperature. The spacecraft PCDU includes a dedicated DC-DC converter for each RTG:

- **Maximum power point tracking (MPPT)**: The converter continuously adjusts the RTG load impedance to extract maximum electrical power as the hot-side temperature drifts with age and environment.
- **Parallel solar/RTG operation**: Some missions (e.g., Juno at Jupiter) use both solar arrays and no RTG; others (e.g., Curiosity rover) use RTG exclusively. Missions like the proposed Europa Lander would use a hybrid architecture with RTG for continuous baseload and batteries for peak loads.
- **Thermal integration**: The RTG radiates ~2 kW of waste heat. This heat is partially redirected via heat pipes to warm spacecraft electronics — the Curiosity rover's MMRTG provides all rover thermal control without electrical heaters.

### Launch Safety

The RTG integration process must demonstrate that the Pu-238 fuel remains contained through all launch accident scenarios. The GPHS module is designed to survive:

- **Launch vehicle explosion on pad**: Projectile impact from exploding propellant tanks. The iridium clad and graphite aeroshell survive 200 m/s fragment impact.
- **Reentry from failed launch**: The module undergoes atmospheric reentry at orbital velocity. The graphite aeroshell ablates, protecting the iridium-clad fuel capsule inside.
- **Impact on concrete or water**: Terminal velocity impact at 50-100 m/s. The capsule deforms but does not rupture, preventing fuel dispersal.

This safety analysis, required by Presidential directive for U.S. launches, is performed by the spacecraft integrator in coordination with the Department of Energy.

## Eclipse Power Management

Eclipse is the most stressful event for the power system. The transition from solar power to battery power must be seamless:

1. **Pre-eclipse preparation** (T-5 min): Battery verified at 100% charge. Non-essential loads (science instruments, electric heaters) powered down or reduced to extend battery margin. Bus voltage confirmed stable.
2. **Eclipse entry** (T-0): Solar array output drops to zero as the spacecraft enters shadow. The bus voltage briefly dips as the battery assumes the full load, then stabilizes at battery voltage (24-28V for unregulated bus).
3. **Eclipse operation** (T+0 to T+36 min): Battery delivers 0.5-15 kW continuously. Depth of discharge reaches 20-70% depending on mission profile. Bus voltage slowly declines as battery discharges.
4. **Eclipse exit** (T+36 min): Solar array output returns as the spacecraft exits shadow. The charge controller enters constant-current mode, delivering maximum charge rate (C/2 to C/10) to replenish the battery before the next eclipse.

For GEO commsats, the eclipse season lasts 45 days around each equinox. The battery is fully charged and discharged every day during this window. Between eclipse seasons, the battery is maintained at trickle charge — the full 15-year cycle life budget is consumed during only 90 days per year of active cycling.

## Power Budget Example

A typical GEO communications satellite power budget at end of life (15 years):

| Component | Power Draw | Duty Cycle | Average Power |
|-----------|-----------|-----------|--------------|
| Communications payload (transponders) | 6,000 W | 60% | 3,600 W |
| TTC&M (telemetry, tracking, command) | 200 W | 100% | 200 W |
| Attitude control (reaction wheels, sensors) | 300 W | 100% | 300 W |
| Thermal control (heaters) | 500 W | 30% | 150 W |
| Propulsion (station-keeping) | 1,000 W | 5% | 50 W |
| Battery charge (sunlight only) | 3,500 W | — | — |
| **Total spacecraft load** | | | **4,300 W** |
| Solar array BOL output | | | 15,000 W |
| Solar array EOL output (15yr) | | | 11,800 W |
| Margin (EOL) | | | **7,500 W (64%)** |

The 64% EOL margin is typical — the solar array is oversized to account for radiation degradation over mission life. At BOL, the margin exceeds 70%, requiring the shunt regulator to dissipate 10 kW of excess power as heat during the first years of operation.

## Comparison of Power System Architectures

| Architecture | Source | Storage | Best Mission | Mass Efficiency | Complexity |
|-------------|--------|---------|-------------|----------------|-----------|
| Solar + Li-ion | GaAs triple-junction | Li-ion pack | LEO/GEO (< Mars) | 80-150 W/kg (panel) | Moderate |
| Solar + NiH₂ | GaAs triple-junction | NiH₂ pressure vessels | GEO (long life) | 45-65 W/kg (battery) | Moderate |
| RTG-only | Pu-238 decay | Li-ion buffer | Deep space (> Mars) | 2.5-5.2 W/kg (RTG) | Low (few moving parts) |
| Solar + RTG hybrid | Both | Li-ion pack | Outer planet orbiters | Mixed | High (two sources) |
| Fuel cell | H₂/O₂ | — | Crewed (short duration) | 200-400 Wh/kg | High (cryogenics) |

## Quantitative Parameters

| Parameter | Value |
|-----------|-------|
| GaAs triple-junction BOL efficiency | 28-30% |
| GaAs triple-junction EOL efficiency (15yr GEO) | 24-26% |
| Panel-level specific power | 80-150 W/kg |
| Li-ion cell voltage | 3.6-3.7V |
| Li-ion energy density | 150-200 Wh/kg |
| Li-ion cycle life (50% DoD) | 20,000-30,000 |
| NiH₂ cycle life (LEO) | 30,000-35,000 |
| NiCd energy density | 40-60 Wh/kg |
| GEO commsat bus power | 8-15 kW |
| LEO earth-obs bus power | 0.5-2 kW |
| Standard bus voltages | 28V, 50V, 100V |
| MMRTG electrical output | 125W (BOL) |
| MMRTG Pu-238 mass | ~4.8 kg |
| GPHS-RTG electrical output | 300W (BOL) |
| GPHS-RTG Pu-238 mass | 7.8 kg |
| RTG degradation rate | ~1.2%/yr |
| Eclipse duration (LEO) | 35-40 min |
| Eclipse duration (GEO equinox) | 72 min |

## Strengths

- GaAs triple-junction cells deliver 30% efficiency, the highest of any space-qualified power source
- Li-ion batteries achieve 150-200 Wh/kg, 3× the energy density of heritage NiCd
- Modern PMAD architectures handle 15+ kW with regulated 100V buses
- RTGs provide continuous power for decades with no refueling or maintenance
- Hybrid solar/battery/RTG architectures optimize for any orbital regime

## Weaknesses

- Solar array area scales inversely with solar flux — Jupiter missions need 25× the panel area
- Li-ion cycle life is temperature-sensitive: 35°C halves the cycle life vs 20°C
- RTGs require Pu-238 production via reactor irradiation — a bottleneck with global supply constraints
- Radiation degradation is unavoidable: 10-25% solar array efficiency loss over 15-year GEO mission
- Bus voltage regulation adds mass: 100V bus demands insulation and arc-suppression design

## See Also

- [Solar Arrays](./spacecraft-power.solar-arrays.md) — GaAs triple-junction cells, deployment mechanisms
- [Space Batteries](./spacecraft-power.space-batteries.md) — Li-ion, NiH₂, NiCd for eclipse power
- [Power Management and Distribution](./spacecraft-power.power-management-distribution.md) — PCDU, shunt regulation, bus architecture
- [RTG Integration](./spacecraft-power.rtg-integration.md) — MMRTG, GPHS-RTG integration, launch safety
- [Photovoltaic Solar Power](../energy/photovoltaics.md) — terrestrial PV heritage and p-n junction fundamentals
- [Radioisotope Power](../energy/radioisotope-power.md) — RTG fuel production and thermoelectric conversion
- [Electronics](../electronics/index.md) — power conditioning, DC-DC conversion, switching electronics
- [Silicon](../silicon/index.md) — semiconductor substrates for solar cells and power devices

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md) • [All Domains](../index.md)*
