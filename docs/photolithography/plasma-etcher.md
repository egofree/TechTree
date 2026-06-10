# Plasma Etcher

> **Node ID**: photolithography.plasma-etcher
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`vacuum.chambers`](../vacuum/chambers.md), [`vacuum.pumps`](../vacuum/pumps.md), [`gas-handling`](../gas-handling/index.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`photolithography.fab-processes`](fab-processes.md), [`vlsi-scaling.advanced-processes`](../vlsi-scaling/advanced-processes.md)
> **Timeline**: Years 40-55
> **Outputs**: etched_patterns, via_holes, trench_structures, patterned_films
> **Critical**: Yes — plasma etching is the primary method for pattern transfer from photoresist to underlying films in semiconductor fabrication; wet etching cannot achieve the anisotropic profiles required for sub-micron features

This article covers the construction of reactive ion etching (RIE) and inductively coupled plasma (ICP) etching systems. For etching chemistry, process parameters, and etch selectivity data, see [Core Fab Processes](fab-processes.md).

## Overview

Plasma etching is the primary pattern transfer method in semiconductor manufacturing. After photolithography defines a photoresist mask on the wafer surface, plasma etching transfers that mask pattern into the underlying film (SiO₂, silicon, aluminum, or other materials) by combining chemical reactions with directional ion bombardment. The result is anisotropic etching — vertical sidewalls with minimal lateral undercut — which is essential for sub-micron feature definition. Wet chemical etching, by contrast, etches isotropically (equal rates in all directions), making it unusable for features below ~2 μm.

Two plasma etching configurations are addressed in this article. Reactive Ion Etching (RIE) uses a single RF power source to generate plasma and accelerate ions toward the wafer, providing etch rates of 20-1000 nm/min. Inductively Coupled Plasma RIE (ICP-RIE) adds a separate RF-driven antenna coil that generates high-density plasma independently of the ion energy, enabling etch rates of 100-5000 nm/min with better control of anisotropy and less substrate damage.

Plasma etching consumes corrosive and toxic gases (Cl₂, BCl₃, CF₄, SF₆, CHF₃) and operates at vacuum pressures of 1-100 mTorr. The equipment requires corrosive-gas-rated vacuum chambers, specialized pumping systems, toxic gas handling infrastructure, and exhaust gas scrubbing. Chamber wall condition (polymer deposits from previous runs) is a dominant process variable — production tools dedicate separate chambers to separate materials to avoid cross-contamination.

## Principle

Plasma etching uses a glow discharge to generate reactive chemical species (ions, radicals, atoms) from process gases. These species react with the exposed film material to form volatile products that are pumped away. The key advantage over wet (chemical) etching is anisotropy — ions accelerated perpendicular to the wafer surface etch vertically while passivation polymers deposit on sidewalls, preventing lateral etching. This produces the vertical sidewall profiles required for sub-micron pattern transfer.

**Reactive Ion Etching (RIE)**: RF power (13.56 MHz) is applied to the substrate electrode (cathode) while the chamber walls serve as the anode. Ions are accelerated across the plasma sheath (dark space) toward the wafer at energies of 100-1000 eV, providing both chemical etching (reaction with radicals) and physical sputtering (ion bombardment). The combination of chemical and physical etching gives controllable anisotropy.

**Inductively Coupled Plasma (ICP)**: A separate RF coil (antenna) around the chamber generates a high-density plasma (10¹⁰-10¹² ions/cm³) independently of the bias voltage on the substrate electrode. This decouples ion density (which controls etch rate) from ion energy (which controls anisotropy and damage), enabling higher etch rates at lower ion energies. The ICP source is the standard for advanced semiconductor etching.

## Prerequisites

- [Vacuum chamber](../vacuum/vacuum-chamber.md) — stainless steel or aluminum, base pressure <10⁻⁶ Torr
- [Turbomolecular pump](../vacuum/pumps.md) — 300-2000 L/s, with dry backing pump
- [Gas handling](../gas-handling/index.md) — multiple MFCs for etch gases (Cl₂, BCl₃, CF₄, SF₆, CHF₃, O₂, Ar)
- [RF power supplies](../energy/electricity.md) — 13.56 MHz, 100-3000 W (bias) + 500-5000 W (ICP source)
- [Corrosion-resistant materials](../metals/iron-steel.md) — 316L stainless steel or aluminum for chamber exposed to halogen plasmas

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Stainless steel 316L chamber | 1 | 300-500 mm diameter, corrosive-gas-rated | [Vacuum Chamber](../vacuum/vacuum-chamber.md) | Aluminum 6061 (lighter, He permeation) |
| Turbomolecular pump (corrosive-rated) | 1 | 300-2000 L/s, Ni-coated rotors, FKM seals | [Vacuum Pumps](../vacuum/pumps.md) | Standard turbo (shorter life in halogen service) |
| Dry scroll backing pump | 1 | 10-30 L/s, oil-free | [Vacuum Pump](../vacuum/vacuum-pump.md) | — |
| RF generator (bias, 13.56 MHz) | 1 | 100-3000 W, with matching network | [Energy](../energy/electricity.md) | — |
| RF generator (ICP source, 13.56 MHz) | 1 | 500-5000 W, with matching network | [Energy](../energy/electricity.md) | — (for RIE-only, not needed) |
| ICP antenna coil | 1 | 3-5 turn copper or silver-plated copper, around quartz dome | [Metals](../metals/index.md) | — |
| Quartz dome (ICP source) | 1 | Fused silica, 150-250 mm diameter | [Glass](../glass/index.md) | — |
| Heated substrate electrode | 1 | Aluminum or SiC-coated, -20°C to 200°C, with He backside cooling | [Machine Tools](../machine-tools/machining.md) | — |
| Mass flow controllers | 4-8 | For Cl₂, BCl₃, CF₄, SF₆, CHF₃, O₂, Ar, N₂ | [Gas Handling](../gas-handling/index.md) | — |
| Capacitance manometer | 1 | 0-100 mTorr range | [Measurement](../measurement/index.md) | — |
| Optical emission spectrometer (OES) | 1 | For endpoint detection (optional but recommended) | [Optics](../optics/index.md) | — |
| Load lock chamber | 1 | 5-20 L with gate valve | [Vacuum Chamber](../vacuum/vacuum-chamber.md) | — |

## Process Description

### Chamber and Pumping

1. **Prepare the vacuum chamber**: Construct a vacuum chamber from 316L stainless steel (corrosive-gas service) or aluminum 6061-T6 per [Vacuum Chamber](../vacuum/vacuum-chamber.md). The chamber must withstand exposure to chlorine and fluorine plasmas. Electropolish the interior to minimize adsorption sites. Install CF flanges for: ICP source (top), turbo pump (bottom), substrate electrode entry, gas injection, pressure gauge, viewport, OES window, and load lock.

2. **Mount the turbomolecular pump**: Use a turbo rated for corrosive gas service (Ni-coated rotor and stator blades, FKM or PTFE seals). Mount on a CF200 flange with a gate valve. Connect to the dry scroll backing pump. Install a foreline trap or scrubber to neutralize halogen exhaust gases.

3. **Install throttle valve and pressure control**: Mount a throttle valve between chamber and turbo. Connect a capacitance manometer (0-100 mTorr range). The throttle valve maintains constant process pressure (1-100 mTorr) during etching by adjusting the conductance between chamber and pump.

### ICP Source (for ICP-RIE Configuration)

4. **Install the quartz dome**: Mount a fused silica dome (150-250 mm diameter) on the top CF flange of the chamber. The dome separates the ICP antenna coil (at atmospheric pressure) from the plasma (at process pressure). The dome must be clean, scratch-free, and rated for the temperature and RF environment.

5. **Wind the ICP antenna coil**: Wind 3-5 turns of copper tubing (6-10 mm OD) or silver-plated copper wire around the outside of the quartz dome. Connect the coil to the ICP RF generator through a matching network. The coil generates an oscillating magnetic field that induces an electric field inside the chamber, sustaining a high-density plasma without direct electrode contact. Water-cool the coil if power exceeds 1000 W.

### Substrate Electrode (Bias Electrode)

6. **Build the substrate electrode**: Machine a flat aluminum plate (200-300 mm diameter) with a recess for the wafer. Install helium backside cooling: a regulated He supply (5-20 Torr) flows between the wafer backside and the electrode surface through a grooved pattern, providing thermal contact for heat removal during etching (ion bombardment deposits 0.1-10 W/cm²). The electrode is temperature-controlled (-20°C to +200°C) by a recirculating chiller or heater.

7. **Mount and insulate the electrode**: Mount the substrate electrode on a ceramic (alumina) insulator ring that electrically isolates it from the chamber body. Connect the bias RF power through a vacuum feedthrough (coaxial, rated for 3 kW at 13.56 MHz). The electrode is the powered cathode; the chamber walls are the grounded anode. Install a matching network between the RF generator and the feedthrough.

### Gas Delivery

8. **Build the gas delivery manifold**: Install MFCs for each etch gas. Route gas lines to injection nozzles or a showerhead ring positioned near the top of the chamber for uniform distribution. Use electropolished 316L stainless steel tubing with VCR fittings throughout. Install pneumatic shut-off valves and check valves on each gas line. For chlorine-based etching (Cl₂, BCl₃), use Hastelloy or Monel components in the gas path — stainless steel corrodes in wet chlorine service.

9. **Install gas cabinet and exhaust abatement**: House toxic and corrosive gas cylinders (Cl₂, BCl₃, SF₆) in ventilated gas cabinets with continuous gas monitoring and automatic shut-off valves. Route exhaust from the backing pump through a wet scrubber (caustic solution, NaOH) or burn box to neutralize halogen gases before release.

### Load Lock and Wafer Handling

10. **Add the load lock**: Build a load lock chamber (5-20 L) with a gate valve to the main chamber and a vent/door to atmosphere. Pump with a dedicated roughing pump. Install a motorized wafer transfer arm. The load lock preserves the main chamber vacuum — critical because every vent cycle deposits water vapor requiring hours of pumping to recover.

### Endpoint Detection

11. **Install OES endpoint detection** (recommended): Mount an optical fiber through a viewport to collect plasma emission light. Route to a spectrometer monitoring a characteristic wavelength (e.g., 704 nm for AlCl₃ during aluminum etch, 337 nm for CN during oxide etch). When the etch reaches the underlying layer, the emission intensity changes — this is the endpoint signal. Endpoint detection prevents over-etching into underlying films.

## Calibration and Verification

1. **Leak rate verification**: After assembly, helium leak check all seals and feedthroughs. Target: <10⁻⁸ atm·cc/s. Halogen plasmas are extremely aggressive — even tiny leaks introduce O₂ and H₂O that disrupt etch chemistry.

2. **Etch rate calibration**: Etch a test wafer with a patterned photoresist mask at fixed RF power, pressure, and gas flow. Measure the etched depth with a profilometer at 5-9 points. Calculate etch rate (nm/min) and uniformity. Target: ±5% across the wafer.

3. **Selectivity measurement**: Etch through a known film thickness on a test wafer. Measure the photoresist loss and underlying film loss. Calculate selectivity (film etch rate / resist etch rate). Target: >3:1 for most processes.

4. **RF power calibration**: Verify forward and reflected power at the wafer electrode using an in-line RF power sensor. Reflected power must be <5% of forward power. Adjust matching network if reflected power exceeds this.

## Quantitative Parameters

| Parameter | RIE | ICP-RIE |
|-----------|-----|---------|
| Plasma density (ions/cm³) | 10⁸-10¹⁰ | 10¹⁰-10¹² |
| Operating pressure | 1-100 mTorr | 1-50 mTorr |
| Bias voltage | 100-1000 V (fixed by RF power) | 50-500 V (independently controllable) |
| RF bias power | 100-3000 W | 100-1000 W |
| ICP source power | N/A | 500-5000 W |
| Etch rate (SiO₂, CHF₃/CF₄) | 20-100 nm/min | 100-1000 nm/min |
| Etch rate (Al, Cl₂/BCl₃) | 50-300 nm/min | 200-2000 nm/min |
| Etch rate (Si, SF₆/C₄F₈) | 100-1000 nm/min | 500-5000 nm/min |
| Anisotropy (sidewall angle) | 85-89° | 87-90° |
| Uniformity | ±5-10% | ±3-5% |
| Base pressure | <10⁻⁶ Torr | <10⁻⁶ Torr |

## Strengths

- Anisotropic etching produces vertical sidewalls — essential for sub-micron pattern transfer where wet etching's isotropy is unacceptable
- ICP-RIE decouples ion density from ion energy — higher etch rates with less substrate damage
- Wide range of etch chemistries available for different materials (Cl-based for metals, F-based for oxides and silicon)

## Weaknesses

- Corrosive gases (Cl₂, BCl₃, SF₆) require special gas handling, scrubbing, and chamber materials — significant safety infrastructure
- Plasma-induced damage to sensitive devices (gate oxides) from ion bombardment and charging — limits bias voltage on front-end-of-line processes
- Chamber wall condition affects etch repeatability — polymer deposition from fluorocarbon plasmas changes chamber seasoning between runs

## Safety

- **Chlorine gas (Cl₂)**: Toxic (IDLH 10 ppm), corrosive, greenish-yellow. Gas cabinet with continuous monitoring, automatic shut-off, and exhaust scrubbing. Emergency protocol: evacuate, SCBA required. Reacts with moisture to form HCl and HOCl.
- **Boron trichloride (BCl₃)**: Corrosive, reacts with moisture to form HCl and boric acid. Same gas cabinet requirements as Cl₂.
- **Sulfur hexafluoride (SF₆)**: Non-toxic but decomposes in plasma to form SF₄, SO₂, and HF. Exhaust scrubbing required.
- **Fluorine compounds**: CF₄, CHF₃ decompose in plasma to produce HF and other fluorine species. Exhaust must pass through a caustic scrubber.
- **High voltage**: Bias electrode at 100-1000 V DC equivalent. RF power at 300-3000 W. Interlocked enclosure. Lock-out/tag-out before servicing.
- **RF radiation**: 13.56 MHz. Verify RF shielding integrity. Measure leakage with RF probe.

## Chamber Seasoning and Process Recipes

Chamber wall condition is a dominant variable in plasma etching. Fluorocarbon plasmas (CF₄, CHF₃, C₄F₈) deposit polymer films on the chamber walls during etching. These wall films affect subsequent etches — a "seasoned" chamber (coated with polymer from previous runs) produces different etch rates than a freshly cleaned chamber. This is why production etch tools use dedicated chambers for each material (one for oxide etch, one for metal etch, one for silicon etch) to avoid cross-contamination of wall films.

**Oxide etch recipe (SiO₂ with CHF₃/CF₄)**:
- Gases: CHF₃ at 30 sccm, CF₄ at 20 sccm, Ar at 50 sccm
- Pressure: 30 mTorr
- RF bias power: 300 W
- ICP source power: 800 W
- Electrode temperature: 20°C
- Etch rate: 200-400 nm/min
- Selectivity to photoresist: 3-5:1
- Selectivity to silicon: 10-20:1

**Aluminum etch recipe (Al with Cl₂/BCl₃)**:
- Gases: Cl₂ at 40 sccm, BCl₃ at 30 sccm, N₂ at 10 sccm
- Pressure: 15 mTorr
- RF bias power: 200 W
- ICP source power: 600 W
- Electrode temperature: 40°C
- Etch rate: 300-600 nm/min
- Selectivity to photoresist: 2-4:1
- BCl₃ scavenges native Al₂O₃ and residual water vapor that would otherwise passivate the aluminum surface

**Silicon etch recipe (Bosch DRIE with SF₆/C₄F₈)**:
- Deposition step: C₄F₈ at 80 sccm, 20 mTorr, 600 W ICP, 0 W bias, 2 seconds — deposits a thin fluorocarbon passivation layer on all surfaces
- Etch step: SF₆ at 100 sccm, 30 mTorr, 800 W ICP, 20 W bias, 3 seconds — etches silicon vertically, passivation protects sidewalls
- Cycle rate: 12-20 cycles/minute
- Etch rate: 2-10 μm/min (depending on feature size)
- Aspect ratio: up to 20:1 achievable
- Scallop size (sidewall roughness): 50-200 nm per cycle, reduced by shorter etch steps

**Chamber clean recipe** (between process runs):
- Gases: O₂ at 100 sccm, Ar at 50 sccm
- Pressure: 50 mTorr
- RF bias power: 200 W
- ICP source power: 1000 W
- Duration: 5-10 minutes
- Purpose: Remove fluorocarbon wall deposits as volatile CO₂, CO, and HF. Restores chamber to a known baseline condition.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Etch rate drops 30-50% between first and last wafer in lot | Chamber wall polymer buildup changes reactive species concentration; O₂ leak introduces passivating species | Run chamber clean recipe (O₂ plasma) between lots; check for vacuum leaks with helium leak detector; install load lock to prevent air exposure |
| Micrograss (residual silicon pillars on etched surface) | Passivation particles or resist residues mask small areas from etching; insufficient ion bombardment energy | Increase RF bias power to 300+ W; verify photoresist is fully developed (no scumming); add O₂ to etch gas to volatilize organic residues |
| Notching at bottom of deep trenches | Charging of insulating features deflects ions; electrical isolation of trench floor from substrate in SOI wafers | Reduce ion energy (lower bias); add pulsed bias (synchronously reverse bias during positive ion half-cycle); use notching-suppression etch chemistry |
| Photoresist erosion exceeds expected rate — selectivity <2:1 | Excessive ion bombardment (high bias power); insufficient polymer deposition in fluorocarbon etch; resist not hard-baked | Reduce bias power; increase CHF₄ or C₄F₈ flow to increase polymer formation; hard-bake resist at 140°C for 60 seconds before etch |
| Feature size varies ±10% across wafer | Gas flow non-uniformity; temperature gradient across electrode; RF power coupling varies with wafer position | Install showerhead gas distributor for uniform flow; verify electrode temperature ±3°C across wafer; check RF grounding straps |

## Maintenance and Consumables

**Chamber component replacement schedule**:
- **O-rings (door seal, viewport)**: Replace every 500-1000 vent cycles or when leak rate exceeds 10⁻⁸ atm·cc/s. Use Viton for general service, Kalrez for aggressive fluorine chemistry.
- **Electrode surface**: Inspect every 200-500 hours. Replace when surface roughness exceeds 1 μm Ra (measured by profilometer) or when pinhole corrosion is visible. Aluminum electrodes in chlorine service corrode faster than SiC-coated electrodes.
- **Turbomolecular pump**: Follow manufacturer maintenance schedule. Bearing replacement at 20,000-40,000 hours. Monitor vibration levels — increasing vibration indicates bearing wear.
- **Quartz dome (ICP)**: Inspect for cracking, deposit buildup, or discoloration every 500 hours. Replace when transmission at the monitoring wavelength drops below 90% of new.
- **Mass flow controllers**: Calibrate annually against a primary standard (bubble flowmeter or dry calibrator). MFC accuracy degrades with exposure to corrosive gases — chlorine service MFCs should be recalibrated every 6 months.

**Exhaust gas treatment**: All plasma etch exhaust must pass through a wet scrubber (caustic NaOH solution) or thermal abatement system before release. Halogen gases (Cl₂, F₂ from plasma decomposition) are toxic and corrosive. Scrubber efficiency monitored by pH of the drain water — replace or refresh scrubber solution when pH drops below 9.

## Quality Control

**Etch rate measurement**: Etch a patterned test wafer at fixed RF power, pressure, and gas flow for a known time. Measure etched depth with a profilometer (stylus instrument, ±5 nm accuracy) at 5-9 points across the wafer. Calculate etch rate (nm/min). Track etch rate on a run-to-run control chart — drift >±10% from qualified value signals chamber seasoning change, gas flow drift, or RF power calibration error.

**Selectivity verification**: Measure photoresist thickness before and after etch (ellipsometer or profilometer). Calculate selectivity = film etch rate / resist etch rate. Target: >3:1 for oxide etch, >2:1 for metal etch. Low selectivity requires thicker resist or lower ion energy.

**Uniformity mapping**: Measure etched depth at 49 points across the wafer after clearing the film. Within-wafer non-uniformity target: ±5% (1σ). Non-uniformity >±10% indicates gas flow maldistribution, temperature gradient, or RF coupling variation.

**Critical dimension (CD) after etch**: Measure feature widths by CD-SEM (critical dimension scanning electron microscope) at 5-9 sites. CD after etch should match CD after lithography (etch bias <10% of target CD). Etch bias (difference between lithographic CD and etched CD) is a systematic offset that can be compensated in the mask design.

**Endpoint detection verification**: For processes using optical emission spectroscopy (OES) endpoint, verify the endpoint signal is clear and reproducible by etching test wafers with known film stacks. The endpoint should trigger within ±5% of the expected etch time. Endpoint failure causes over-etch (damage to underlying film) or under-etch (residual material).

**Particle monitoring**: Measure particles on test wafers before and after etch. Added particles must be <20 particles ≥0.16 μm (200 mm wafer). High particle counts after etch indicate chamber wall flaking, electrode degradation, or wafer handling debris.

## Variations and Alternatives

| Method | Etch Rate | Anisotropy | Selectivity | When to Use |
|--------|-----------|------------|-------------|-------------|
| RIE (capacitively coupled) | 20-300 nm/min | 85-89° sidewalls | 2-10:1 | Features ≥1 μm; oxide, metal, silicon etching |
| ICP-RIE (inductively coupled) | 100-5000 nm/min | 87-90° sidewalls | 3-20:1 | Sub-micron features, DRIE, high-aspect-ratio structures |
| Bosch DRIE (alternating etch/passivation) | 2-10 μm/min | 89-90° (with scallops) | Variable | Through-silicon vias, MEMS, deep trenches (>10 μm depth) |
| Wet chemical etching | 10-2000 nm/min | Isotropic (45° sidewalls) | 10-100:1 | Large features (≥2 μm), non-critical layers, wafer thinning |
| Ion milling (Ar⁺ physical sputtering) | 10-50 nm/min | Highly anisotropic | ~1:1 (no selectivity) | Materials with no chemical etch (noble metals, magnetic films) |
| ALE (atomic layer etching) | 0.1-1 nm/cycle | Atomic-level control | >50:1 | Sub-10 nm features, monolayer precision, damage-sensitive materials |

RIE is the default for most production etching at features ≥1 μm. ICP-RIE extends capability to sub-micron features with higher etch rates and lower ion damage. The Bosch DRIE process (alternating SF₆ etch and C₄F₈ passivation) enables deep silicon etching for MEMS and through-silicon vias. Wet etching remains useful for non-critical layers and large features where its isotropy is acceptable. Ion milling is reserved for materials that lack volatile etch products (gold, platinum). ALE provides atomic-layer precision for the most advanced nodes.

## Scaling Notes

- **From RIE to ICP-RIE**: RIE provides adequate etch rates (20-300 nm/min) for features ≥1 μm. ICP-RIE is required for high-aspect-ratio etching (DRIE, through-silicon vias) where etch rates of 1-10 μm/min are needed. ICP adds the quartz dome and antenna coil — a moderate complexity increase.
- **Single-wafer to cluster tool**: Production etch tools use 2-4 process chambers on a central vacuum handler, enabling parallel processing. Throughput scales linearly with chamber count.
- **Wafer size scaling**: 200 mm to 300 mm wafers require larger chambers, higher gas flows, and more uniform RF coupling. Chamber volume roughly doubles; pump speed must increase proportionally.

## References

- [Core Fab Processes](fab-processes.md) — etching chemistry, process integration, wet vs. dry etching comparison
- [Vacuum Chamber](../vacuum/vacuum-chamber.md) — chamber construction
- [Gas Handling](../gas-handling/index.md) — toxic gas handling, gas cabinet safety
- [Sputtering System](sputtering-system.md) — complementary thin-film deposition
- [CVD Reactor](cvd-reactor.md) — alternative deposition technology

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Photolithography & IC Fabrication](./index.md) • [All Domains](../../index.md)*
