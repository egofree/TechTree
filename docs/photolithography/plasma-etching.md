# Plasma Etching (RIE & DRIE)

> **Node ID**: photolithography.fab-processes.plasma-etching
> **Domain**: [Photolithography](./index.md)
> **Dependencies**: [`Silicon`](../silicon/index.md)
> **Enables**: [`Basic Gas Handling`](../glass/basic.md), [`Vacuum Chambers & Sealing`](../vacuum/chambers.md)
> **Timeline**: Years 45-70
> **Outputs**: etched_features, anisotropic_profiles, deep_trenches, via_holes
> **Critical**: No

## Overview

Reactive ion etching (RIE) and deep reactive ion etching (DRIE) using fluorocarbon, sulfur hexafluoride, and chlorine-based plasmas. Covers RIE reactor design (parallel plate, ICP), plasma generation (RF 13.56 MHz, ICP), etch chemistries (CF₄, SF₆, Cl₂, BCl₃), selectivity and aspect ratio control, DRIE Bosch process for high-aspect-ratio features, and etch rate monitoring (OES endpoint detection).

Plasma etching is the complementary process to lithography: where lithography paints the pattern in photoresist, plasma etching carves that pattern into the underlying film. An RF generator (typically 13.56 MHz) ionizes process gases in a vacuum chamber, creating a soup of reactive radicals, ions, and electrons. The radicals provide chemical etching (isotropic, material-selective) while the ions provide physical sputtering (directional, non-selective). Combining both yields anisotropic etching: vertical sidewalls without lateral undercut, something wet etching cannot achieve for crystalline silicon.

Reactive Ion Etching (RIE) places the wafer on the powered electrode, which develops a negative DC self-bias that accelerates positive ions downward into the wafer surface. Deep Reactive Ion Etching (DRIE) adds high-density plasma sources (ICP coils) to achieve etch rates of several micrometers per minute for MEMS structures and through-silicon vias.

Etch selectivity, the ratio of target material etch rate to mask (or underlying layer) etch rate, determines whether the pattern transfers cleanly. A selectivity of 10:1 means the mask erodes ten times slower than the film being etched. Fluorocarbon-rich chemistries achieve high selectivity for oxide over silicon because the polymer deposits on silicon surfaces (protecting them) but is continuously consumed on oxide by the etching reaction. Selectivity below 3:1 limits the achievable etch depth and requires thick masks.

## Prerequisites

### Materials

- Process gases: SF₆, CF₄, CHF₃, C₄F₈ (silicon and oxide etch); Cl₂, BCl₃ (metal etch); O₂ (resist strip and polymer control)
- Patterned wafers with photoresist or hard mask already defined by lithography

### Equipment

- [Silicon](../silicon/index.md) — material dependency
- Etch chamber with RF generator (13.56 MHz), impedance matching network, and powered electrode
- Gas delivery system with mass flow controllers for 4-8 gas lines
- Vacuum system: roughing pump + turbo-molecular pump, base pressure below 10⁻⁶ Torr
- Optical emission spectrometer (OES) for endpoint detection
- Exhaust gas abatement: burn box or wet scrubber for PFC and toxic gas destruction
- Electrostatic chuck with helium backside cooling for wafer temperature control during etch

### Knowledge

- Plasma physics: RF sheath formation, self-bias voltage, ion energy distribution
- Etch chemistry: radical generation, volatile byproduct formation, sidewall passivation mechanisms
- Vacuum technology: pump-down curves, leak detection, chamber conditioning
- Process integration: how etch selectivity and profile affect subsequent deposition and lithography steps
- RF matching network tuning: load impedance changes with plasma conditions, affecting power delivery

### Infrastructure

- Cleanroom environment for wafer loading and unload operations
- Toxic gas monitoring and alarm system for Cl₂, HCl, and HF byproducts
- RF-shielded enclosure around the etch tool (13.56 MHz radiation hazard)
- Waste gas abatement: thermal destruction or wet scrubbing for PFC greenhouse gases

## Process Description

The etch chamber is the heart of the system. Two parallel electrodes sit inside a vacuum vessel: the upper electrode is grounded and often serves as the gas showerhead, while the lower electrode holds the wafer and is connected to the RF generator through an impedance matching network. When RF power is applied at 13.56 MHz, electrons (light and fast) oscillate with the field and gain energy, while ions (heavy and slow) respond to the time-averaged field. Energetic electrons collide with gas molecules, dissociating them into reactive radicals and ionizing them. The powered electrode develops a negative DC self-bias (typically 100-800 V) that accelerates positive ions perpendicular to the wafer surface.

Silicon etching uses fluorine-based chemistries (SF₆, CF₄) where fluorine radicals react with silicon to form volatile SiF₄. Oxide etching uses fluorocarbon gases (CHF₃, C₄F₈) where the carbon species deposit a protective polymer on sidewalls and on silicon (providing selectivity over silicon), while fluorine radicals attack the oxide. Metal etching (aluminum) relies on chlorine chemistries (Cl₂, BCl₃) forming volatile AlCl₃. The Bosch process for DRIE alternates between etch (SF₆) and passivation (C₄F₈) cycles every few seconds, producing scalloped but nearly vertical sidewalls with aspect ratios exceeding 20:1.

Endpoint detection monitors the optical emission from the plasma during etching. Different materials produce characteristic emission lines as they are volatilized: carbon monoxide emission indicates organic (resist) etching, while changes in fluorine emission signal silicon clearance. Real-time OES tracking tells the operator when the target layer has been completely etched through, preventing over-etch that would damage the underlying film. For processes without a clear optical endpoint, timed etch with pre-calibrated etch rate is used, with a safety margin of 10-20% over-etch to ensure complete clearance.

### Step-by-Step Procedure

1. Load patterned wafers onto the electrostatic chuck in the etch chamber. Verify photoresist integrity and that the correct mask layer is exposed.
2. Pump down to base pressure (below 10⁻⁶ Torr). Stabilize gas flows and pressure at the recipe setpoint (typically 5-100 mTorr).
3. Strike the plasma by applying RF power. Allow the chamber to condition for 10-30 seconds (stabilize self-bias, gas dissociation, and chamber wall state).
4. Run the etch recipe: monitor OES endpoint signal for the characteristic emission line that indicates the target layer has cleared. Etch time is the primary control variable for depth.
5. Upon endpoint detection (or timer completion), extinguish the plasma and purge the chamber with inert gas.
6. Unload wafers and inspect. Remove photoresist and etch residues in an oxygen plasma asher followed by wet clean.

The Bosch process for DRIE deserves closer examination because it is the workhorse technique for MEMS fabrication and through-silicon vias. In each cycle, the chamber first flows C₄F₈ to deposit a thin fluorocarbon polymer on all surfaces (sidewalls and trench bottom). Then the gas switches to SF₆, which generates fluorine radicals that etch silicon. The ions accelerated by the RF bias sputter through the polymer on the horizontal trench bottom (where ions strike perpendicularly) but not on the vertical sidewalls (where the polymer protects the silicon). The result is an anisotropic etch cycle. Repeating the cycle hundreds of times produces deep trenches with nearly vertical sidewalls, at the cost of small scallops (50-200 nm periodic undulations) on the sidewall surface from the alternating etch and passivation steps. The scallop size can be reduced by shortening the cycle time, at the expense of overall etch rate.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| RF Power | 50 - 3000 W | Higher power = higher ion flux and etch rate; also more damage |
| Pressure | 5 - 200 mTorr | Lower pressure = more anisotropic (longer mean free path); higher = more chemical |
| Gas Flow | 10 - 500 sccm | Controls radical density and etch rate |
| Self-bias Voltage | 50 - 800 V | Determines ion energy; higher = more physical sputtering component |
| Temperature | -150°C to +200°C | Cryo etching for smoother sidewalls; substrate cooling via He backside |
| Etch Rate | 0.01 - 10 μm/min | Depends on material, chemistry, and plasma density |
| Gas Chemistry | Material-specific | Si: SF₆/CF₄; SiO₂: CHF₃/C₄F₈; Al: Cl₂/BCl₃ |

### Etch Rates by Material and Chemistry

The etch rate depends on the target material, gas chemistry, RF power, pressure, and plasma source (RIE vs ICP). The table below gives representative etch rates for common IC materials under production-typical conditions.

| Material | Gas Chemistry | RF Power (W) | Pressure (mTorr) | Etch Rate (nm/min) | Selectivity to Photoresist | Selectivity to SiO₂ |
|----------|--------------|-------------|-------------------|--------------------|-----------------------------|---------------------|
| Silicon (single crystal) | SF₆ / O₂ (90/10 sccm) | 300 | 30 | 200-500 | 3-5:1 | 1-2:1 |
| Silicon (single crystal) | SF₆ / C₄F₈ (Bosch etch step) | 800 ICP + 20 bias | 30 | 1000-3000 (per cycle avg) | 5-10:1 | 2-5:1 |
| Silicon (single crystal) | Cl₂ / HBr (gate etch) | 400 | 10 | 50-150 | 5-10:1 | 10-20:1 |
| Polysilicon | HBr / Cl₂ / O₂ (70/20/5 sccm) | 300 | 15 | 80-200 | 5-10:1 | 10-30:1 |
| Polysilicon | SF₆ / CHF₃ (30/20 sccm) | 250 | 40 | 150-400 | 3-5:1 | 1-3:1 |
| SiO₂ (thermal) | CHF₃ / CF₄ (30/20 sccm) | 300 + 800 ICP | 30 | 100-300 | 3-5:1 | — |
| SiO₂ (PECVD) | CHF₃ / Ar (40/50 sccm) | 350 + 800 ICP | 25 | 150-350 | 3-5:1 | — |
| SiO₂ (thermal, high selectivity) | C₄F₈ / Ar / O₂ (25/50/5 sccm) | 400 + 1000 ICP | 20 | 80-200 | 5-10:1 | — |
| Si₃N₄ (silicon nitride) | CHF₃ / O₂ (40/5 sccm) | 300 | 40 | 80-200 | 3-5:1 | 0.5-1:1 (etches slower than oxide) |
| Si₃N₄ (spacer etch) | CHF₄ / O₂ / Ar (25/5/50 sccm) | 250 | 30 | 50-150 | 5-8:1 | 1-2:1 |
| Aluminum (Al or Al-Cu 0.5%) | Cl₂ / BCl₃ / N₂ (40/30/10 sccm) | 200 + 600 ICP | 15 | 300-600 | 2-4:1 | 5-15:1 |
| Aluminum (Al-Si 1%) | Cl₂ / BCl₃ (50/25 sccm) | 250 | 20 | 200-500 | 2-3:1 | 5-10:1 |
| Tungsten (W) | SF₆ / Ar (40/30 sccm) | 300 | 30 | 200-400 | 3-5:1 | 1-3:1 |
| Titanium (Ti) | Cl₂ / BCl₃ (30/20 sccm) | 200 | 15 | 100-300 | 2-4:1 | 3-8:1 |
| TiN (barrier) | Cl₂ / BCl₃ / Ar (30/15/30 sccm) | 250 | 20 | 80-200 | 2-4:1 | 3-6:1 |
| Photoresist (Novolac/DNQ) | O₂ (100 sccm, ash) | 300 | 500 | 500-2000 | — | 5-20:1 (resist etches faster) |
| Photoresist (CAR, DUV) | O₂ (100 sccm, ash) | 200 | 500 | 300-1000 | — | 3-10:1 |
| SiGe (selective to Si) | CF₄ / O₂ (20/5 sccm) | 200 + 600 ICP | 15 | 100-300 (SiGe) / <5 (Si) | 10-20:1 | 5-10:1 |
| Cu seed (for cleaning) | Cl₂ / Ar (20/40 sccm) | 300 | 20 | 50-150 | 1-2:1 | 3-5:1 |

**Reading the table**: Selectivity to photoresist of 5:1 means the target material etches 5 times faster than the photoresist mask. For a 1 μm deep silicon etch with 5:1 selectivity, the photoresist loses 200 nm of thickness. Selectivity to SiO₂ matters when SiO₂ serves as an etch stop or mask: a 10:1 Si:SiO₂ selectivity means that for every 100 nm of silicon removed, only 10 nm of SiO₂ is consumed.

**Loading effect**: The etch rates above are for typical pattern densities (20-50% open area). Densely patterned wafers (high loading) etch 10-30% slower than sparsely patterned wafers because more reactive species are consumed by the larger etching surface. Always calibrate etch rate on a test wafer with the actual pattern density of the production design.

## Safety Considerations

Plasma etching gases present a spectrum of hazards. Chlorine and boron trichloride are corrosive and toxic, producing HCl upon contact with moisture. Sulfur hexafluoride and perfluorocarbons (CF₄, C₄F₈) are potent greenhouse gases with global warming potentials thousands of times higher than CO₂. Fluorine radicals etching silicon dioxide produce SiF₄ and can generate HF as a byproduct. All exhaust gases must pass through burn boxes (thermal decomposition at 1000°C) or wet scrubbers before release.

The 13.56 MHz RF power supply can cause deep tissue burns if the operator contacts the matching network or electrode during operation. RF interlocks must prevent access to the chamber and RF components when power is on. The vacuum chamber presents implosion risk if the viewing window or chamber wall is compromised. The plasma itself emits intense UV radiation; never view the plasma directly through the viewport without proper filtering.

- **Chemical**: Toxic and corrosive gases (Cl₂, BCl₃, HF byproduct) require gas cabinets with monitoring
- **RF radiation**: 13.56 MHz exposure hazard; interlocked enclosure mandatory
- **Mechanical**: Vacuum implosion; regular inspection of chamber walls and viewports
- **Environmental**: PFC greenhouse gas abatement required by regulation in most jurisdictions

### Personal Protective Equipment

- Chemical splash goggles and face shield when connecting gas lines or handling wet-clean chemicals
- Nitrile gloves for wafer handling; heavy rubber gloves for gas cylinder changes
- UV-filtering safety glasses if observing plasma through a viewport
- Cryogenic gloves when handling liquid nitrogen for cold traps

### Emergency Procedures

- Chlorine gas alarm triggers automatic gas shutoff, chamber pump-and-purge, and area ventilation to exhaust
- RF interlock breach immediately kills RF power and grounds the matching network
- Vacuum breach (implosion or leak): evacuate area, shut roughing pump to prevent oil backstreaming
- Know the location of calcium gluconate gel (HF burn treatment) even if HF is only a potential byproduct

## Quality Control

### Acceptance Criteria

- **Etched Features**: Critical dimension (CD) within ±5% of target; sidewall angle between 85° and 90°
- **Anisotropic Profiles**: Lateral undercut less than 10% of etch depth; sidewall roughness below 5 nm RMS
- **Deep Trenches**: Depth within ±3% across the wafer; aspect ratio capability verified by test structures
- **Via Holes**: Via diameter uniformity within ±5% across the wafer; complete etch-through verified electrically

### Testing Methods

- CD-SEM (Critical Dimension Scanning Electron Microscope): top-down measurement of feature widths
- Cross-section SEM: direct imaging of sidewall profile, undercut, and scalloping (for DRIE)
- Spectroscopic ellipsometry or reflectometry: thin film thickness measurement for etch rate calculation
- OES endpoint detection: real-time monitoring of etch progress by tracking emission lines characteristic of each material
- Electrical test structures: chain resistance or via resistance measurements to confirm complete etch-through

### Sampling Protocol

- Measure CD on five sites per wafer (center, top, bottom, left, right) using CD-SEM
- Run cross-section SEM on one sacrificial wafer per lot to verify sidewall profile
- Track OES endpoint time trend across lots: drift indicates chamber condition change
- Run etch rate test wafers after every chamber cleaning or gas cylinder change

Etch rate is measured by etching a blanket (unpatterned) test wafer for a fixed time and measuring the film thickness before and after using ellipsometry or reflectometry. The etch rate in nm/min is the thickness removed divided by the etch time. However, the blanket etch rate differs from the patterned etch rate because of loading effects and microloading. Production etch recipes are characterized on patterned test structures with the actual feature sizes used in production, and the etch time is calibrated to achieve the target etch depth on those specific structures.

- Etch chambers must be periodically cleaned to remove accumulated deposits that generate particles and change the etch characteristics
- Track etch rate on monitor wafers before and after chamber cleans to quantify the "first wafer effect"

## Scaling Notes

Modern plasma etchers process one wafer at a time (single-wafer tools) for uniformity control. Scaling from a bench-top research RIE to a production etch module involves:

- **Research RIE**: Manual wafer loading, single gas line, 50-100 W RF power, 1-10 nm/min etch rate. One wafer at a time, manual unload.
- **Pilot production**: Cassette-to-cassette automation, 4-6 gas lines, 300-1000 W RF, 0.1-1 μm/min etch rate. Recipe-driven process control with OES endpoint.
- **Volume production**: Cluster tool (multiple process chambers on a central vacuum transport), ICP source for high-density plasma, 2000+ W total power, etch rates up to 10 μm/min. Throughput of 40-60 wafers per hour per chamber.

Single-wafer processing displaced batch etching in the late 1980s when feature sizes shrank below one micrometer. One wafer per chamber allows independent control of each wafer's process conditions, improving yield at the cost of needing more chambers for the same throughput. Cluster tools with 2-4 chambers per platform are the standard production configuration, wafers moving between process modules through a central vacuum transport without breaking vacuum.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Grass-like residue on etched surface | Micromasking from particles or non-volatile etch byproducts | Clean chamber, increase ion energy to sputter through contamination, check gas purity |
| Notching at oxide-silicon interface | Charging of the oxide surface deflecting ions at the trench bottom | Adjust gas chemistry for more polymer passivation; use pulsed RF to reduce charging |
| Small features etch slower than large ones (ARDE) | Reduced radical and ion transport into high-aspect-ratio features | Lower pressure (longer mean free path), higher ion energy, or time-multiplexed etch (Bosch) |
| Sidewall bowing (undercut mid-profile) | Excess lateral chemical etching component | Increase sidewall passivation (add C₄F₈), reduce pressure, increase self-bias |
| Selectivity loss (mask erodes too fast) | Insufficient polymer deposition on mask surface | Add fluorocarbon gas to build protective polymer, lower ion energy, reduce O₂ flow |
| Etch rate drift over time | Chamber wall condition change from polymer accumulation | Run chamber clean recipe (O₂ plasma) between lots; track first-wafer effect |
| Residue after aluminum etch | Incomplete removal of aluminum chloride byproducts or sidewall polymer | Post-etch wet clean in DI water (AlCl₃ is water-soluble); add resist strip step |
| Notching at insulator interface | Charging of the oxide surface deflecting ions at the trench bottom | Adjust gas chemistry for more polymer passivation; use pulsed RF to reduce charging |

## Variations and Alternatives

- **Parallel plate RIE**: Simplest configuration. RF power on the wafer electrode. Ion density and ion energy are coupled, limiting independent control.
- **ICP (Inductively Coupled Plasma)**: Separate RF coil generates high-density plasma (10¹¹-10¹² ions/cm³) while wafer electrode bias independently controls ion energy. Higher etch rates with lower ion damage.
- **DRIE Bosch process**: Alternates SF₆ etch and C₄F₈ passivation cycles every 1-10 seconds. Achieves vertical sidewalls at etch rates of 5-50 μm/min. Scalloped sidewalls (50-200 nm ripple) are the characteristic artifact.
- **Cryogenic etching**: Substrate cooled to -100°C or below. Sidewall passivation forms naturally from etch byproducts. Smoother sidewalls than Bosch, but limited to specialized equipment.
- **Wet etching**: Simpler, cheaper, but inherently isotropic for most materials. Cannot produce vertical sidewalls in silicon without crystal orientation effects. Still used for non-critical steps and blanket film removal.
- **Atomic layer etching (ALE)**: Cycles of self-limiting surface modification (e.g., chlorine adsorption) followed by low-energy ion removal. Removes one atomic layer per cycle with atomic-scale precision. Emerging technique for sub-10 nm features where conventional RIE lacks the selectivity and damage control needed.

Inductively coupled plasma (ICP) etching uses a separate RF coil wrapped around the etch chamber to generate a high-density plasma (10¹¹ to 10¹² ions/cm³), independent of the RF bias applied to the wafer electrode. This decoupling allows the process engineer to set ion flux (through ICP power) and ion energy (through bias power) independently. The result is high etch rates at low ion energies, reducing substrate damage while maintaining throughput. ICP sources are standard on production etchers for feature sizes below 130 nm.

Microloading, also called aspect-ratio-dependent etching (ARDE), causes features of different sizes to etch at different rates on the same wafer. Small features with high aspect ratios etch slower than large features because the reactive species and volatile etch products must diffuse through narrower openings. This effect worsens as feature sizes shrink below 100 nm. Process engineers compensate by adjusting gas pressure (lower pressure extends the mean free path), ion energy (higher energy drives species deeper into narrow features), and sidewall passivation chemistry to narrow the etch rate gap between large and small features.

Loading effects are a related but distinct phenomenon: the etch rate depends on the total exposed silicon area on the wafer. A wafer with mostly open silicon etches faster than a densely patterned wafer because more reactive species are consumed by the larger etching surface. This makes uniform etch depth difficult across wafers with different pattern densities, and is the reason modern etch chambers process one wafer at a time with tightly controlled conditions rather than in batches.

Post-etch residue removal is a mandatory follow-on step. Etching byproducts, including fluorocarbon polymers, metal chlorides, and sputtered photoresist fragments, must be completely stripped before the next process step. Oxygen plasma ashing removes organic residues, while wet chemical cleans (often involving dilute HF or specialized proprietary mixtures) dissolve inorganic residues and sidewall polymers. Incomplete residue removal causes defects in subsequent deposition and lithography steps that are difficult to trace back to the etch step.

Etch chamber conditioning is a recurring operational concern. Polymer deposits on the chamber walls change the radical density in the plasma by absorbing and re-emitting reactive species. After a chamber clean (O₂ plasma to strip polymer), the first few wafers etch differently than subsequent wafers because the walls re-accumulate the conditioning layer. This "first wafer effect" is managed by running dummy wafers (non-production wafers etched with the production recipe) to re-condition the chamber after each clean, before committing production material.

The electrostatic chuck (ESC) that holds the wafer during etching serves two functions: mechanical clamping and thermal contact. Helium gas flows between the backside of the wafer and the chuck surface at a few Torr pressure, providing thermal conduction that removes heat from the wafer. Without helium backside cooling, the wafer temperature would rise uncontrollably during high-power etching, causing photoresist reticulation and changing etch rates. The chuck must also clamp the wafer securely without mechanical edges that could generate particles, and the clamping voltage must be compatible with the wafer's electrical characteristics (conductive silicon versus insulating SOI wafers require different chuck designs).

Damage from plasma etching is a concern for devices with thin gate oxides. Ion bombardment can create interface traps and fixed oxide charge in the gate dielectric, degrading transistor performance. Low-damage etch processes minimize ion energy (below 50 eV) while maintaining etch rate through high plasma density. Pulsed plasma etching, where the RF power is switched on and off at kHz rates, reduces the time-averaged ion energy while maintaining radical generation, providing a lower-damage alternative to continuous-wave RF.

## References

- [Core Fab Processes](fab-processes.md) — parent capability
- [Photolithography Domain](./index.md) — domain overview and related capabilities
- [Silicon](../silicon/index.md) — upstream dependency (material)
- [Basic Gas Handling](../glass/basic.md) — downstream capability
- [Vacuum Chambers & Sealing](../vacuum/chambers.md) — downstream capability

---

Etch selectivity is controlled by the gas chemistry: fluorocarbon-rich mixtures (high C₄F₈ or CHF₃ flow relative to CF₄ or SF₆) deposit more protective polymer, increasing selectivity to oxide over silicon and photoresist. However, excessive polymer deposition causes residue problems and can close off narrow features (polymer plugging). The selectivity versus residue tradeoff is managed by tuning the fluorine-to-carbon ratio in the gas mixture, a balance that shifts with every new technology node as feature sizes shrink.

The transition from batch etching to single-wafer etching in the late 1980s was driven by the need for better uniformity control as feature sizes shrank below one micrometer. Single-wafer tools allow independent control of each wafer's process conditions, improving yield at the cost of lower throughput. Modern etch chambers process one wafer at a time with cycle times of tens of seconds to several minutes depending on the etch depth and selectivity requirements.

*Part of the [Bootciv Tech Tree](../../index.md) · [Photolithography](./index.md) · [All Domains](../../index.md)*
