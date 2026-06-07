# Epitaxial Layer Growth

> **Node ID**: silicon.wafering.epitaxy
> **Domain**: [Silicon](./index.md)
> **Dependencies**: See prerequisites
> **Enables**: [`Dopant & Etch Gases`](../chemistry/dopant-etch-gases.md), [`Wafer Slicing & Polishing`](wafering.md)
> **Timeline**: Years 60-150+
> **Outputs**: epitaxial_wafers, epitaxial_layers
> **Critical**: No

## Overview

CVD epitaxial growth of single-crystal silicon layers on polished wafer substrates using trichlorosilane or silane at 900-1200°C. Enables independently doped device layers (p/p+ or n/n+ configurations) with autodoping control via reduced pressure and buffer layers.

Epitaxy, from the Greek epi (upon) and taxis (arrangement), deposits a crystalline silicon layer that inherits the atomic ordering of the substrate beneath it. Unlike polycrystalline or amorphous silicon deposits, an epitaxial layer is a single crystal with the same lattice orientation as the wafer. This matters because transistors built on a single-crystal epilayer have far fewer defects and higher carrier mobility than those built on polycrystalline silicon.

The primary industrial method is chemical vapor deposition (CVD) epitaxy. A silicon source gas, either silane (SiH₄), dichlorosilane (SiH₂Cl₂), or trichlorosilane (SiHCl₃), decomposes on a heated wafer surface in a hydrogen atmosphere. The released silicon atoms migrate across the surface and incorporate into the crystal lattice at energetically favorable sites, extending the substrate crystal structure upward. Dopant gases added to the flow (PH₃ or AsH₃ for n-type, B₂H₆ for p-type) allow independent control of the epilayer doping, separate from the substrate.

Epitaxial layers serve several distinct purposes in semiconductor manufacturing. They provide a high-purity active layer on a heavily-doped substrate, reducing latch-up susceptibility in CMOS circuits. They enable doping profiles that cannot be achieved by diffusion or ion implantation alone, such as a lightly-doped layer on a heavily-doped substrate, or a stack of layers with alternating doping types (n on p). They also allow growth of silicon-germanium (SiGe) or silicon-carbon (SiC) alloy layers where strain from lattice mismatch modifies carrier mobility for higher-performance transistors.

The growth rate in CVD epitaxy is governed by whichever of two processes is slower: mass transport (delivery of precursor gas to the wafer surface) or surface reaction (decomposition and incorporation of silicon atoms into the crystal lattice). At high temperatures (above 1100°C for chlorinated sources), mass transport limits growth because the surface reaction is fast. Operating in this mass-transport-limited regime provides better thickness uniformity because the growth rate becomes less sensitive to local temperature variations across the wafer. At lower temperatures, the surface reaction rate drops exponentially and becomes the bottleneck, making growth rate highly temperature-sensitive.

## Prerequisites

### Materials

- Polished silicon substrates (prime grade, damage-free surface)
- Silicon source gases: silane (SiH₄), dichlorosilane (SiH₂Cl₂), or trichlorosilane (SiHCl₃)
- Hydrogen carrier gas (ultra-high purity, 99.999%)
- Dopant gases: phosphine (PH₃), arsine (AsH₃), or diborane (B₂H₆), typically diluted to 10-1000 ppm in H₂
- HCl gas for in-situ substrate cleaning and selective epitaxy
- Nitrogen for reactor purging between hydrogen and air atmospheres

### Equipment

- [Silicon](index.md) — material dependency
- Epitaxial reactor: horizontal or vertical quartz chamber with resistance-heated or RF-induction-heated susceptor
- Gas delivery system with mass flow controllers for Si source, H₂, dopant, and HCl lines
- Exhaust gas abatement: burn box or wet scrubber for silane and chlorinated compounds
- Thickness measurement tool: spectroscopic ellipsometer or FTIR
- Particle counter for incoming substrate inspection

### Knowledge

- Crystal growth kinetics: surface reaction limited versus mass-transport limited regimes
- Gas-phase nucleation: why silane decomposition must occur on the wafer surface, not in the gas phase
- Autodoping mechanisms: dopant evaporation from the substrate contaminating the growing layer
- Defect nucleation: how substrate contamination, scratches, and oxygen precipitates spawn stacking faults
- Gas flow dynamics in horizontal versus vertical reactor geometries

### Infrastructure

- Cleanroom for wafer handling and post-growth inspection (Class 10 or better at the reactor load lock)
- Gas cabinets with continuous toxic gas monitoring for silane, PH₃, AsH₃, B₂H₆
- Hydrogen supply with flashback arrestors and ventilation: silane is pyrophoric and hydrogen is explosive
- Cooling water for the reactor jacket and exhaust gas quench system
- Exhaust gas monitoring: chlorinated silicon byproducts (SiCl₄, HCl) must be scrubbed before release

## Process Description

A production epitaxial reactor heats silicon wafers on a graphite susceptor (coated with SiC to prevent carbon contamination) to 1000-1200°C in a hydrogen atmosphere. The high temperature serves two purposes: it drives the decomposition of the silicon source gas on the wafer surface, and it allows surface migration of deposited silicon atoms to find their correct lattice sites. The growth rate, typically 0.5-5 μm/min, depends on temperature, reactor pressure, and gas composition.

Before growth begins, the wafer surface is cleaned in-situ by flowing HCl gas at high temperature. This etches away a thin layer of silicon, removing native oxide, surface contamination, and any mechanical damage from polishing. A clean, atomically ordered surface is essential for defect-free epitaxy; even a single particle can nucleate a stacking fault that propagates through the entire epilayer.

The silicon source gas choice involves tradeoffs. Silane (SiH₄) decomposes at lower temperatures (600-900°C) but is pyrophoric and prone to gas-phase nucleation (silicon particles forming in the gas rather than on the wafer). Trichlorosilane (SiHCl₃) requires higher temperatures (1000-1200°C) but suppresses gas-phase nucleation and provides some in-situ etching of oxide contaminants. Dichlorosilane (SiH₂Cl₂) splits the difference. Production processes for silicon ICs typically use trichlorosilane at atmospheric or slightly reduced pressure.

### Step-by-Step Procedure

1. Load polished silicon wafers onto the susceptor. Inspect substrate surfaces under collimated light for particles and scratches before loading.
2. Purge the reactor with nitrogen, then hydrogen. Ramp the susceptor temperature to the cleaning setpoint (1150-1200°C).
3. Flow HCl gas for 1-5 minutes to etch-clean the wafer surface. Etch depth is typically 0.1-0.5 μm to remove all damage and contamination.
4. Switch off HCl. Stabilize temperature at the growth setpoint. Introduce the silicon source gas and dopant gas at the recipe flow rates.
5. Grow the epitaxial layer for the calculated time based on the target thickness and growth rate. Monitor temperature uniformity across the susceptor.
6. Shut off silicon source and dopant gases. Cool in hydrogen ambient. Unload wafers when temperature drops below 600°C to prevent thermal shock.

The silicon source gas choice involves tradeoffs that affect reactor design and process capability. Silane (SiH₄) decomposes at lower temperatures (600-900°C), enabling epitaxial growth with less thermal budget and less autodoping, but it is pyrophoric and prone to gas-phase nucleation where silicon particles form in the gas stream rather than depositing on the wafer surface. Trichlorosilane (SiHCl₃) requires higher temperatures (1100-1200°C) but the chlorine byproduct provides a natural etching action that suppresses gas-phase nucleation and helps clean oxide contaminants from the wafer surface during growth. Dichlorosilane (SiH₂Cl₂) splits the difference and is the most commonly used source in production reactors. The chlorinated sources also produce HCl as a byproduct, which must be scrubbed from the exhaust.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Growth Temperature | 900 - 1200°C | SiHCl₃: 1100-1200°C; SiH₄: 600-900°C |
| Growth Rate | 0.1 - 5 μm/min | Lower for thin layers (precision), higher for thick layers (throughput) |
| Reactor Pressure | 50 - 760 Torr | Reduced pressure suppresses autodoping and improves uniformity |
| Dopant Flow | 10 ppm - 1000 ppm | Diluted in H₂; concentration sets epilayer resistivity |
| H₂ Carrier Flow | 20 - 200 slm | Sets residence time and gas-phase uniformity across susceptor |
| HCl Etch Rate | 0.1 - 0.5 μm/min | Pre-growth substrate clean; must remove all surface damage |

### Source Gas Comparison

The silicon source gas determines the operating temperature range, growth rate ceiling, and defect mechanisms. Production processes select the source gas based on the required epilayer thickness, autodoping tolerance, and available reactor design.

| Source Gas | Formula | Growth Temp | Typical Rate | Max Practical Rate | Boiling Point | Key Tradeoff |
|-----------|---------|-------------|-------------|-------------------|---------------|-------------|
| Silane | SiH₄ | 600-900°C | 0.1-0.5 μm/min | 2.0 μm/min | -112°C | Lowest thermal budget and autodoping, but prone to gas-phase nucleation above 2 μm/min |
| Dichlorosilane | SiH₂Cl₂ | 900-1100°C | 0.5-2.0 μm/min | 3.0 μm/min | 8.2°C | Most common production source; good balance of rate, quality, and stability |
| Trichlorosilane | SiHCl₃ | 1100-1200°C | 1.0-3.0 μm/min | 5.0 μm/min | 31.8°C | Highest throughput; chlorine suppresses gas-phase nucleation |
| Silicon tetrachloride | SiCl₄ | 1150-1250°C | 0.5-1.5 μm/min | 3.0 μm/min | 57.6°C | Historically common; slower but excellent uniformity |

Chlorinated sources (SiHCl₃, SiH₂Cl₂, SiCl₄) generate HCl as a byproduct of surface decomposition. This HCl provides in-situ etching of oxide contaminants and suppresses gas-phase nucleation by etching silicon nuclei before they grow into particles. The tradeoff is higher growth temperature, which increases autodoping from the substrate.

Silane decomposes at lower temperatures but without the protective chlorine etching effect. Silane partial pressure above 0.1% in H₂ at temperatures below 900°C produces gas-phase nucleation: silicon atoms nucleate in the gas stream rather than on the wafer, creating a snowstorm of polysilicon particles that rain onto the growing epilayer. This appears as surface haze. Reduce silane partial pressure, raise temperature, or switch to a chlorinated source.

### Epitaxial Layer Specifications by Application

Different device types demand different epilayer thicknesses, resistivities, and defect tolerances. A CMOS logic wafer needs a thin, lightly-doped epi on a heavily-doped substrate. A power device needs a thick drift region with controlled resistivity.

| Application | Epi Thickness | Resistivity | Doping Config | Max Defect Density | Surface Roughness | Epi/Substrate Example |
|------------|--------------|-------------|---------------|-------------------|-------------------|----------------------|
| CMOS logic (advanced, <100nm) | 1-5 μm | 5-30 Ω·cm | p/p+ or n/n+ | <0.1 cm⁻² | <0.5 nm RMS | 10 Ω·cm p-type on 0.01 Ω·cm p+ substrate |
| CMOS logic (legacy, >250nm) | 5-20 μm | 1-20 Ω·cm | p/p+ | <0.5 cm⁻² | <1 nm RMS | 5 Ω·cm p-type on 0.015 Ω·cm p+ substrate |
| Power MOSFET (low voltage) | 5-15 μm | 0.5-5 Ω·cm | n/n+ | <1 cm⁻² | <1 nm RMS | 1 Ω·cm n-type on 0.008 Ω·cm n+ substrate |
| Power device (high voltage, >500V) | 30-100 μm | 10-80 Ω·cm | n/n+ | <0.5 cm⁻² | <1 nm RMS | 30 Ω·cm n-type on 0.01 Ω·cm n+ substrate |
| Bipolar / BiCMOS | 1-10 μm | 0.1-10 Ω·cm | Various stacks | <0.5 cm⁻² | <0.5 nm RMS | Multi-layer: n-epi on n+ buried layer on p substrate |
| SiGe HBT (heterojunction) | 0.05-0.5 μm SiGe | — | Graded Ge 0-30% | <0.1 cm⁻² | <0.3 nm RMS | SiGe base layer between Si emitter and collector |
| Advanced solar (PERC, TOPCon) | 10-30 μm | 0.5-5 Ω·cm | n-type | <5 cm⁻² | <2 nm RMS | Lightly doped n-epi on high-purity n-type substrate |

### Contamination Limits for Epitaxial Layers

Epitaxial layers must meet purity requirements that are stringent even by semiconductor standards, because metallic impurities in the active device region directly degrade transistor performance. The limits below apply to the finished epilayer after growth, measured by spreading resistance profiling (SRP), secondary ion mass spectrometry (SIMS), or surface analysis techniques.

| Impurity | Maximum Concentration | Measurement Method | Effect if Exceeded |
|----------|----------------------|-------------------|-------------------|
| Fe (iron) | <5×10¹³ atoms/cm³ (~0.5 ppb) | SIMS, DLTS | Deep-level trap (Ev +0.39 eV); reduces minority carrier lifetime by 10× per decade above limit; increases junction leakage |
| Cu (copper) | <5×10¹³ atoms/cm³ (~0.5 ppb) | SIMS, TXRF | Diffuses rapidly through Si at process temperatures (>500°C); decorates dislocations and stacking faults; causes junction shorts |
| Ni (nickel) | <5×10¹³ atoms/cm³ (~0.5 ppb) | SIMS | Silicide formation at defect sites; increases p-n junction leakage current by >10× |
| Na (sodium) | <1×10¹³ atoms/cm³ (~0.1 ppb) | SIMS, AAS | Mobile ion contamination in gate oxides; shifts MOS threshold voltage by >0.1 V per 10¹² cm⁻² |
| K (potassium) | <1×10¹³ atoms/cm³ (~0.1 ppb) | SIMS, AAS | Mobile ion contamination; similar effect to sodium in gate dielectrics |
| Cr (chromium) | <5×10¹³ atoms/cm³ (~0.5 ppb) | SIMS, DLTS | Deep-level trap; reduces carrier lifetime; can form Cr-B pairs in p-type Si that compensate doping |
| Au (gold) | <1×10¹² atoms/cm³ (~0.01 ppb) | DLTS | Extremely effective recombination center (capture cross-section 10⁻¹⁵ cm²); fatal for bipolar devices even at 10¹² cm⁻³ |
| O (oxygen) | <5×10¹⁶ atoms/cm³ (~0.25 ppma) | FTIR (1107 cm⁻¹) | Thermal donor formation shifts resistivity; SiO₂ precipitates in epi create defects |
| C (carbon) | <1×10¹⁶ atoms/cm³ (~0.05 ppma) | FTIR (605 cm⁻¹) | SiC precipitates at >10¹⁷ cm⁻³; nucleates oxidation-induced stacking faults (OSF) |
| Bulk metals (total) | <1×10¹⁴ atoms/cm³ (~1 ppb) | ICP-MS, GDMS | Sum of all transition metals must not exceed this level for reliable device operation |

These limits assume the epitaxial layer will be used for active device fabrication (transistors, diodes). For solar cell epitaxial layers, metallic impurity tolerances are 10-100× higher (up to 10¹⁵-10¹⁶ atoms/cm³ for individual metals) because solar cells are less sensitive to individual defect sites than nanometer-scale transistors.

### Autodoping Transition Width

The autodoping transition region, where the dopant concentration shifts from substrate level to epi level, is one of the most critical quality metrics for epitaxial wafers. A sharp transition (narrow width) is essential for CMOS latchup prevention and precise junction control.

| Growth Condition | Transition Width | Autodoping Level | Use Case |
|-----------------|-----------------|-----------------|----------|
| APCVD, SiHCl₃, 1150°C, 760 Torr | 2-5 μm | High | Thick epi layers (>20 μm), legacy processes |
| RPCVD, SiHCl₃, 1100°C, 80 Torr | 0.5-1.5 μm | Moderate | Standard CMOS (5-20 μm epi) |
| RPCVD, SiH₂Cl₂, 1000°C, 50 Torr | 0.3-0.8 μm | Low | Advanced CMOS (<5 μm epi) |
| RPCVD + undoped buffer, SiH₂Cl₂, 950°C, 40 Torr | <0.3 μm | Very Low | Sub-micron CMOS, latchup-sensitive designs |
| LPCVD, SiH₄, 850°C, 10 Torr | <0.2 μm | Minimal | Thin epi (<2 μm) for advanced nodes |

The transition width is measured by spreading resistance profiling (SRP) with 20-50 nm depth resolution. The metric reported is the distance over which the dopant concentration changes from 90% of substrate concentration to 110% of target epi concentration.

## Safety Considerations

Silane (SiH₄) ignites spontaneously in air at concentrations above 2-3%. It burns with an invisible flame and can detonate under confinement. Silane gas lines must be welded stainless steel with no threaded fittings, and the exhaust must pass through a burn box (a heated chamber where silane is deliberately ignited and oxidized under controlled conditions). Hydrogen carrier gas presents explosion risk; flashback arrestors on all hydrogen lines are mandatory.

The dopant gases are extraordinarily toxic. Arsine (AsH₃) and phosphine (PH₃) have IDLH (Immediately Dangerous to Life and Health) values of 3 ppm and 50 ppm respectively. Diborane (B₂H₆) is both pyrophoric and toxic. Gas cabinets with continuous monitoring, automatic shut-off valves, emergency exhaust, and audible alarms are required for all dopant gases. Exhaust gases from the reactor must pass through scrubbers or burn boxes before release.

- **Pyrophoric**: Silane and diborane ignite on contact with air. Welded gas lines, burn boxes, and inert purges are non-negotiable.
- **Toxic**: Arsine causes hemolytic anemia at ppm concentrations. Phosphine attacks the central nervous system. Continuous gas monitoring with alarms at 10% of the TLV.
- **Thermal**: Susceptor temperatures exceed 1000°C. Radiation shields and interlocked access panels prevent burn injuries.
- **Explosion**: Hydrogen atmosphere inside the reactor. Nitrogen purge before hydrogen introduction; hydrogen purge before air introduction.

### Personal Protective Equipment

- Chemical splash goggles and face shield when handling gas cylinders or connecting gas lines
- Heat-resistant gloves (Kevlar or similar) for reactor component handling after cooldown
- Self-contained breathing apparatus (SCBA) available in the gas cabinet area for arsine/phosphine emergency
- Anti-static garments when working near silane gas lines (static sparks ignite silane leaks)
- Heat-resistant face shield when opening the reactor after a high-temperature run

### Emergency Procedures

- Silane leak: evacuate immediately, do not attempt to extinguish a silane fire (shut off gas supply remotely)
- Toxic gas alarm (arsine/phosphine): triggers automatic gas shutoff, building exhaust to full emergency mode, and area evacuation
- Hydrogen fire: shut off hydrogen supply remotely, do not extinguish the flame until gas is isolated (burning hydrogen prevents explosion)
- Reactor overtemperature: automatic power cutoff and hydrogen purge to nitrogen
- Gas cabinet alarm (silane, arsine, phosphine): evacuate area, trigger emergency exhaust, remote gas shutoff

## Quality Control

### Acceptance Criteria

- **Epitaxial Wafers**: Layer thickness within ±5% of target across the wafer; surface defect density below 0.5 cm⁻²
- **Epitaxial Layers**: Resistivity within ±10% of target; transition width (autodoping tail) less than 0.5 μm

### Testing Methods

- Spectroscopic ellipsometry: non-destructive thickness measurement with sub-nm precision
- FTIR (Fourier Transform Infrared): measures epilayer thickness by interference fringes from the epi-substrate interface
- Spreading resistance profiling (SRP): measures dopant concentration versus depth with high resolution
- Surface inspection under collimated light: visual detection of haze, hillocks, stacking faults, and orange peel texture
- Mercury probe CV: non-destructive measurement of epilayer doping concentration
- X-ray diffraction (XRD): measures crystal quality and strain in heteroepitaxial layers (SiGe on Si)
- Defect density inspection: automated surface scanning under collimated UV light

### Sampling Protocol

- Measure thickness at 49 points across every wafer (center + radial map)
- Run SRP on one wafer per lot to verify the doping profile and autodoping transition width
- Inspect surface quality on every wafer under collimated light before committing to device fabrication
- Track defect density trends across lots to detect reactor contamination or susceptor degradation

## Scaling Notes

Production epitaxial reactors process 20-50 wafers simultaneously on a large susceptor. Scaling considerations:

- **Research scale**: Single-wafer horizontal reactor, manual loading, silane source at 650°C. Growth rates of 0.1-0.5 μm/min. A few wafers per day.
- **Pilot production**: Batch horizontal or vertical reactor, 5-10 wafers, trichlorosilane at 1100°C. Growth rates of 1-3 μm/min. 10-20 wafers per run.
- **Volume production**: Large-diameter vertical reactor with 50+ wafer capacity, automated load/unload, reduced pressure operation for uniformity. Growth rates of 2-5 μm/min. Multiple runs per day.

Temperature uniformity across the susceptor is the primary scaling challenge. A ±1°C variation at 1100°C translates to measurable growth rate variation across the batch. Production reactors use careful susceptor design (rotation, tapered heating zones) and reduced pressure operation to achieve ±3% thickness uniformity across a 50-wafer batch.

Epitaxial wafers require cleanroom handling identical to prime silicon wafers, with one additional concern: the epitaxial surface is more susceptible to contamination than bulk silicon because the deposited layer may have different surface chemistry. Store epitaxial wafers in nitrogen-purged containers to prevent native oxide growth on the epi surface. Even a thin native oxide (1-2 nm) changes the effective silicon thickness available for gate oxidation in subsequent processing. Inspect incoming epilayers under collimated light for haze, hillocks, and stacking faults before committing them to device fabrication runs.

Selective epitaxy is a specialized variant where the epitaxial layer grows only on exposed silicon areas and not on oxide or nitride masking layers. The gas chemistry must suppress nucleation on dielectric surfaces, typically by adding HCl which etches away any silicon nuclei that form on the oxide or nitride. Selective epitaxy is used for raised source/drain structures (growing extra silicon on the source/drain areas of a transistor to reduce series resistance) and for finFET channel formation where the silicon fin is grown epitaxially within an oxide trench. The growth selectivity ratio of silicon growth rate on Si versus SiO₂ must exceed 100:1 for production use.

Reactor design affects both throughput and film quality. Horizontal reactors (gas flows parallel to the wafer surface) are simple but suffer from gas depletion along the flow direction, causing the downstream wafers to grow slower than upstream wafers. Vertical reactors (gas flows perpendicular to the susceptor) provide more uniform gas access across all wafers. Rotating the susceptor during growth averages out radial temperature and flow non-uniformities. Barrel reactors (wafers mounted on the faces of a rotating polyhedron inside a cylindrical chamber) provide good uniformity and high throughput but are mechanically complex. Most modern production reactors use a vertical geometry with susceptor rotation.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Stacking faults in epilayer | Substrate surface contamination (particles, scratches, metal residues) | Improve pre-epi clean; verify HCl etch is removing all damage; inspect substrates before loading |
| Haze on epilayer surface | Gas-phase nucleation depositing polysilicon particles | Lower silane partial pressure, increase temperature, or switch to chlorinated source |
| Autodoping (substrate dopant contaminating epilayer) | Dopant evaporation from heavily-doped substrate at growth temperature | Reduce growth pressure (LPCVD), grow undoped buffer layer first, use chlorinated source |
| Orange peel (surface roughness) | Inadequate substrate polishing or incomplete HCl pre-etch | Verify substrate CMP quality, increase HCl etch time or temperature |
| Thickness non-uniformity across batch | Temperature gradients across susceptor | Rotate susceptor during growth, adjust heating zone power ratios |
| Slip lines (crystal dislocations from thermal stress) | Rapid temperature ramps causing thermal gradients in wafer | Slow down temperature ramp rates, use ring-shaped susceptor support to minimize contact stress |
| Gas-phase nucleation (polysilicon particles on surface) | Silane concentration too high or temperature too low for surface-reaction-limited growth | Reduce silane partial pressure, increase temperature, or switch to chlorinated source (SiHCl₃) |
| Resistivity out of specification | Dopant gas flow incorrect or gas line contamination | Verify MFC calibration for dopant line; check for leaks in gas delivery; verify carrier gas purity |
| Poor thickness uniformity | Temperature gradient across susceptor or gas flow asymmetry | Rotate susceptor during growth, adjust gas injection geometry, check susceptor flatness |
| Pattern-dependent loading (growth rate varies with pattern density) | Localized gas depletion over dense exposed Si areas in selective epitaxy | Adjust DCS/HCl ratio (increase HCl to suppress growth rate on dense features); reduce pressure to 40-80 Torr for more uniform gas transport; design layout with balanced pattern density |
| SiGe layer relaxation (dislocation network visible in XRD) | Ge concentration exceeds critical thickness (Matthews-Blakeslee limit): >30% Ge in layers >50 nm thick on (100) Si | Grade Ge concentration gradually (ramp from 0% to target over 20-50 nm); keep SiGe layer below critical thickness for target Ge%; reduce growth temperature to 600-750°C to lower strain energy |
| Carbon contamination in epilayer (>10¹⁶ atoms/cm³) | CO contamination from graphite susceptor degradation, or organic residues on substrate | Replace graphite susceptor if SiC coating is compromised; verify argon purge gas has O₂+H₂O <0.5 ppm; extend N₂ purge cycle to 5+ volume exchanges before growth |
| Oxygen incorporation in epilayer (>5×10¹⁶ cm⁻³) | Air leak into reactor or moist gas lines; quartz chamber components at high temperature | Helium leak-check all seals (target <10⁻⁶ mbar·L/s); verify H₂ carrier gas purity >99.999%; install moisture trap on gas inlet; check that reactor door seal is clean and undamaged |
| Epilayer cracking (thick layers, >30 μm) | Thermal mismatch stress during cooling from growth temperature, especially on heavily-doped substrates | Reduce cooling rate to <5°C/min through 800-1000°C range; reduce growth temperature where possible (SiH₂Cl₂ at 950°C instead of SiHCl₃ at 1150°C); use thicker substrate wafers (>775 μm for 300 mm) |
| Spotty or incomplete growth on some wafers in batch | Gas flow shadowing from upstream wafers, or susceptor temperature not uniform to within ±1°C | Rotate susceptor continuously during growth; check susceptor flatness (<0.1 mm warpage); adjust gas injection angle; for barrel reactors, verify all faces receive equal gas flow |
| High particle count on finished epi wafers (>50 particles ≥0.3 μm) | Reactor wall deposits flaking during loading/unloading, or dirty wafer carriers | Clean reactor chamber walls with HCl burn-off cycle at 1200°C before production run; replace or clean wafer carriers (ultrasonic clean in DI water + IPA); load wafers in Class 10 environment at load lock |
| Doping profile spike at epi-substrate interface | Buried layer out-diffusion or autodoping from patterned substrate regions | Reduce growth temperature to minimize diffusion; use lower pressure (40-60 Torr); grow 0.5 μm undoped buffer layer before doped layer; verify substrate has no exposed heavily-doped regions outside device areas |
| Interfacial oxide detected by ellipsometry | Incomplete HCl pre-etch, or moisture in reactor during temperature transitions | Increase HCl pre-etch to remove >0.3 μm; verify N₂ purge is complete before introducing H₂; check that reactor is leak-tight (O₂ <0.1 ppm at growth temperature); ensure wafers are loaded within 2 hours of last RCA clean |

## Variations and Alternatives

- **Atmospheric pressure CVD (APCVD)**: Simplest reactor design. Fast growth rates but limited uniformity control. Common for thick (10+ μm) epitaxial layers.
- **Reduced pressure CVD (RPCVD)**: Operates at 50-200 Torr. Better thickness uniformity and lower autodoping. Standard for thin epilayers in advanced CMOS.
- **Molecular beam epitaxy (MBE)**: Ultra-high vacuum, elemental sources in effusion cells, atomic-layer precision. Growth rates are 0.01-0.1 μm/min. Used for compound semiconductors (GaAs, InP) and heterostructures, not for volume silicon production.
- **Selective epitaxy**: Epitaxial growth only on exposed silicon areas, not on oxide or nitride. Requires HCl in the gas mixture to suppress nucleation on dielectric surfaces. Used for raised source/drain and finFET structures.
- **Epitaxial lateral overgrowth (ELO)**: The epitaxial layer grows vertically from a seed window through a masking layer and then extends laterally over the mask. This technique creates silicon-on-insulator structures without wafer bonding, and is used for integrating photonic devices with CMOS electronics. The lateral growth rate depends on crystal orientation, with growth along <100> directions being fastest.
- **Liquid phase epitaxy (LPE)**: Grows crystalline layers from a supersaturated metal solution. Historically used for GaAs and other compound semiconductors. Rarely used for silicon because CVD provides better control and purity. Still finds niche applications in specialized compound semiconductor devices.

Autodoping is a persistent challenge where dopant atoms from the heavily-doped substrate evaporate during high-temperature growth and incorporate into the growing epitaxial layer, distorting the intended doping profile. This is worst when growing a lightly-doped epilayer on a heavily-doped substrate (a common CMOS configuration). The transition region where the dopant concentration shifts from substrate level to epilayer level can extend several micrometers if not controlled. Reduced pressure operation (50-200 Torr instead of atmospheric) suppresses autodoping by reducing the residence time of evaporated dopant atoms in the gas phase. A thin undoped buffer layer grown before the doped epilayer also helps by trapping the autodoping tail. Chlorinated silicon sources (SiHCl₃) provide additional etching of the substrate surface that removes dopant atoms before they can evaporate.

Defect control is critical because crystal defects propagate directly into the devices built on the epitaxial layer. Stacking faults, caused by contamination or scratches on the substrate surface, extend through the entire epilayer thickness. Hillocks from localized fast growth create surface bumps that interfere with subsequent lithography. Orange peel surface roughness from improper substrate preparation degrades gate oxide quality. The substrate must be particle-free and atomically clean before growth begins; a single particle on the starting surface can nucleate a defect that ruins the entire wafer.

## References

- [Wafer Slicing & Polishing](wafering.md) — parent capability for wafer substrate preparation
- [Silicon Purification](purification.md) — polysilicon feedstock and chlorosilane chemistry
- [Crystal Growth & Wafering](crystal-growth.md) — CZ and FZ crystal growth, wafer specifications
- [CZ Pulling](cz-pulling.md) — CZ puller equipment, dopant addition, crystal properties
- [Basic Semiconductor Devices](basic-devices.md) — device fabrication from epi wafers
- [Silicon Domain](./index.md) — domain overview and related capabilities
- [Dopant & Etch Gases](../chemistry/dopant-etch-gases.md) — PH₃, AsH₃, B₂H₆ gas handling
- [Hydrogen & Silane](../chemistry/hydrogen-silane.md) — silane production and H₂ supply
- [Silicon-on-Insulator](soi.md) — SOI wafer production using epitaxial techniques
- [CMP](../photolithography/cmp.md) — post-epi polishing for SOI wafer finishing

---

The transition from atmospheric-pressure epitaxy to reduced-pressure (RP) epitaxy in the 1990s enabled production of thin, lightly-doped epilayers on heavily-doped substrates. Atmospheric-pressure growth at 1100°C produces a heavily autodoped transition region several micrometers thick, unacceptable for advanced CMOS. Growing at 50-100 Torr narrows the transition region to below 0.5 μm by sweeping evaporated dopant atoms out of the reactor before they can incorporate into the growing layer. RP-CVD also improves thickness uniformity by making the growth rate less sensitive to local temperature variations.

Epitaxial silicon-germanium (SiGe) layers are used in heterojunction bipolar transistors (HBTs) and strained-channel MOSFETs. The germanium concentration is graded from 0% at the substrate interface to 10-30% at the surface, creating a gradual lattice parameter change that prevents dislocation formation. The strain from the larger Ge atoms modifies the silicon band structure, increasing hole mobility for p-channel devices. SiGe epitaxy requires ultra-high vacuum CVD (UHVCVD) or reduced-pressure CVD with careful gas switching to achieve the abrupt interfaces needed for heterostructure devices.

The HCl pre-etch step before epitaxial growth deserves attention because it sets the baseline for defect density in the resulting epilayer. The HCl gas etches silicon at a rate that depends on temperature, HCl concentration, and crystal orientation, etching faster along defect sites (scratches, grain boundaries) than on the pristine crystal surface. A proper HCl pre-etch removes 0.1-0.5 μm of silicon, eliminating polishing damage, native oxide patches, and surface contaminants. Under-etching leaves residual damage that nucleates stacking faults in the epilayer. Over-etching roughens the surface and wastes time. The HCl etch rate must be characterized for each reactor and susceptor configuration.

---
*Part of the [Bootciv Tech Tree](../index.md) · [Silicon](./index.md) · [All Domains](../index.md)*
