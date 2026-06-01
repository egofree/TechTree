# Plasma Etching (RIE & DRIE)

> **Node ID**: photolithography.plasma-etching
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Parent**: [Core Fab Processes](fab-processes.md)
> **Dependencies**: [`vacuum`](../vacuum/index.md), [`gas-handling`](../gas-handling/index.md), [`energy.electricity`](../energy/electricity.md)
> **Timeline**: Years 45-70
> **Outputs**: etched_features, anisotropic_profiles, deep_trenches, via_holes

## Overview

Plasma etching is the primary pattern transfer method in semiconductor manufacturing, using ionized gas plasmas to selectively remove material through a combination of chemical reactions and physical ion bombardment. Unlike wet etching, plasma etching produces anisotropic (vertical) sidewall profiles essential for sub-micron feature definition. The two dominant variants are reactive ion etching (RIE) for conventional feature sizes and deep reactive ion etching (DRIE) for high-aspect-ratio structures.

## RIE Reactor Design

### Parallel-Plate (Capacitively Coupled) Reactor

The standard RIE tool is a parallel-plate reactor operating at 13.56 MHz (ISM band, chosen to avoid RF interference with communications):

- **Chamber**: Aluminum or anodized aluminum body, 200-300 mm diameter for wafer compatibility. Water-cooled walls (15-25°C) to control polymer deposition and particle generation.
- **Electrodes**: Bottom electrode (cathode, powered) holds the wafer on an electrostatic or mechanical chuck. Top electrode (grounded) serves as the counter-electrode and gas showerhead. Typical gap: 30-80 mm.
- **Gas delivery**: Showerhead (perforated plate with 100-500 holes, 0.5-1 mm diameter) ensures uniform gas distribution across the wafer. Mass flow controllers (MFCs) regulate each gas to ±1% of setpoint at 10-200 sccm.
- **Vacuum system**: Turbo-molecular pump backed by a dry roughing pump maintains process pressure at 10-200 mTorr. Throttle valve controls pressure independently of gas flow. Base pressure: <1 × 10⁻⁶ Torr to minimize contamination.
- **RF system**: 13.56 MHz RF generator (50-1500 W) with automatic impedance matching network (L-type or Pi-type). The matching network minimizes reflected power (<5% of forward power). DC self-bias develops on the powered electrode: V_dc = 100-800 V depending on power, pressure, and gas chemistry.
- **Wafer cooling**: Helium backside cooling at 5-20 Torr maintains wafer temperature at setpoint (20-80°C). Without cooling, ion bombardment heats the wafer uncontrollably, degrading photoresist and changing etch rates.

### Inductively Coupled Plasma (ICP) Reactor

ICP reactors decouple plasma density from ion energy, enabling independent control of etch rate and selectivity:

- **Plasma source**: RF coil (2-5 turns of water-cooled copper tubing) wrapped around a dielectric window (quartz or alumina) at the top of the chamber. Powered at 13.56 MHz, 500-3000 W. The oscillating magnetic field induces a high-density plasma (10¹⁰-10¹² ions/cm³, 10-100× denser than capacitive coupling).
- **Substrate bias**: Separate RF generator (13.56 MHz, 50-500 W) on the bottom electrode controls ion energy independently. Low bias power = gentle ion bombardment = high selectivity. High bias power = aggressive ion bombardment = fast etch but poor selectivity.
- **Advantage**: High etch rates (up to 10× capacitive RIE) with excellent selectivity, because the dense plasma provides abundant reactive species while the independently controlled bias keeps ion energy low enough to avoid physical damage to the mask and underlying layers.

### Etch Chamber Materials

| Component | Material | Reason |
|-----------|----------|--------|
| Chamber walls | Anodized Al or Al₂O₃-coated | Resists fluorine/chlorine plasmas, low particle generation |
| Electrode | Al, graphite, or SiO₂-coated | Depends on process chemistry; SiO₂ for silicon etch to minimize contamination |
| Showerhead | Al or SiC | Chemical resistance, uniform gas distribution |
| Viewport | Quartz (fused silica) | OES endpoint detection requires optical access |
| Seals | Viton or Kalrez O-rings | Chemical resistance; Kalrez for chlorine processes (Viton degrades) |

## Plasma Generation

### RF Plasma Physics

At 13.56 MHz, electrons respond to the oscillating electric field (light, mobile) while ions cannot follow (heavy, slow). This creates a state where:

1. **Electron-impact dissociation**: Electrons (2-10 eV average energy, Maxwellian distribution) collide with feed gas molecules, breaking them into reactive fragments: CF₄ + e⁻ → CF₃· + F· + e⁻. The free fluorine atoms are the primary etching species for silicon.
2. **Electron-impact ionization**: Higher-energy collisions create positive ions: CF₄ + e⁻ → CF₃⁺ + 2e⁻. These ions are accelerated toward the wafer by the DC self-bias.
3. **DC self-bias formation**: In an asymmetric reactor (small powered electrode, large grounded wall), more electrons than ions escape to the walls each RF cycle. The powered electrode charges negatively, creating a DC offset (self-bias) of 100-800 V. This bias accelerates ions perpendicular to the wafer surface, producing anisotropic etching.

### Key Plasma Parameters

| Parameter | Range | Effect |
|-----------|-------|--------|
| Pressure | 5-200 mTorr | Lower → more anisotropic (longer mean free path), higher → more isotropic (more collisions randomize ion direction) |
| RF power | 50-1500 W | Higher → faster etch, more dissociation, but lower selectivity and more resist damage |
| Gas flow | 10-200 sccm total | Controls residence time; higher flow = shorter residence time = less polymer deposition |
| Wafer temperature | 20-80°C | Lower → more polymer deposition on sidewalls (better anisotropy); higher → more volatile etch products (faster etch) |
| DC self-bias | 100-800 V | Higher → more physical sputtering component, faster oxide etch, poorer selectivity to resist |

## Etch Gases & Chemistries

### Fluorocarbon Gases (SiO₂, Si₃N₄ etch)

Fluorocarbon plasmas are the workhorse for dielectric etching. The carbon-to-fluorine ratio controls the balance between etching and polymer deposition:

| Gas | Formula | C:F Ratio | Primary Use | Etch Rate (SiO₂) |
|-----|---------|-----------|-------------|-------------------|
| CF₄ | Tetrafluoromethane | 1:4 | Fast silicon/oxide etch, low polymer | 50-200 nm/min |
| CHF₃ | Trifluoromethane | 1:3 | Oxide etch with sidewall passivation | 30-100 nm/min |
| C₄F₈ | Octafluorocyclobutane | 1:2 | DRIE passivation step, high polymer | Deposits polymer (passivation) |
| C₂F₆ | Hexafluoroethane | 1:3 | Oxide etch, moderate polymer | 40-120 nm/min |
| CH₂F₂ | Difluoromethane | 1:2 | High-selectivity oxide etch | 20-60 nm/min |

**Mechanism**: CFₓ radicals adsorb on the SiO₂ surface. Ion bombardment provides activation energy for the reaction: SiO₂ + 4F· → SiF₄↑ + O₂↑. The volatile SiF₄ is pumped away. Excess CFₓ forms a polymer film (CF₂)ₙ that passivates sidewalls, preventing lateral etching.

**Selectivity control**: Adding O₂ to CF₄ consumes free fluorine (O₂ + 2F· → OF₂ or CO + F₂ → COF₂), reducing the etch rate of silicon relative to SiO₂. Adding H₂ consumes fluorine and increases polymer deposition (H₂ + F· → HF), improving selectivity to silicon but potentially causing grassing (micromasking by polymer residues).

### Sulfur Hexafluoride (Si etch)

SF₆ is the primary etch gas for silicon, offering high etch rates and isotropic character:

- **Dissociation**: SF₆ + e⁻ → SFₓ· + (6-x)F· + e⁻. Free fluorine atoms etch silicon: Si + 4F· → SiF₄↑.
- **Etch rate**: 100-500 nm/min in standard RIE; up to 5-10 μm/min in high-density ICP plasmas.
- **Character**: Inherently isotropic (neutral F atoms etch in all directions). Anisotropy requires ion bombardment to clear the horizontal surface plus sidewall passivation (from adding O₂ for SiOₓFᵧ or using the Bosch process).
- **Typical process**: SF₆ at 20-100 sccm, 10-50 mTorr, 100-300 W RF. Selectivity to photoresist: 2-5:1. Selectivity to SiO₂: 5-20:1 (Si:SiO₂).

### Chlorine-Based Gases (Metal, Compound Semiconductor etch)

Chlorine plasmas etch metals (Al, Ti, W) and compound semiconductors (GaAs, InP) with high selectivity:

| Gas | Formula | Target Material | Etch Rate | Selectivity vs. Resist |
|-----|---------|----------------|-----------|----------------------|
| Cl₂ | Chlorine | Al, GaAs, InP | 50-300 nm/min (Al), 200-1000 nm/min (GaAs) | 3-8:1 |
| BCl₃ | Boron trichloride | Al (with native oxide breakthrough) | 30-200 nm/min | 4-10:1 |
| SiCl₄ | Silicon tetrachloride | GaAs, InP | 50-200 nm/min | 5-10:1 |

**Aluminum etch with Cl₂/BCl₃**:
- BCl₃ serves two critical functions: (1) it reduces native Al₂O₃ (BCl₃ + Al₂O₃ → AlCl₃ + B₂O₃), breaking through the 2-5 nm oxide barrier that would block etching, and (2) it scavenges residual water vapor and oxygen (BCl₃ + H₂O → B₂O₃ + HCl), keeping the chamber chemistry stable.
- Typical recipe: Cl₂/BCl₃ at 2:1 to 4:1 ratio, 30-100 sccm total flow, 10-50 mTorr, 200-500 W RF. Etch rate: 100-500 nm/min. Selectivity to photoresist: 3-5:1.
- **Product volatility**: AlCl₃ sublimes at 180°C, so the wafer must be kept above ~60°C for efficient product removal, but below photoresist flow temperature (~120°C).

### Etch Gas Safety

All plasma etch gases are hazardous and many are potent greenhouse gases:

- **CF₄**: GWP 6,630× CO₂. Chemically inert in the atmosphere (50,000+ year lifetime). Requires point-of-use abatement (plasma destruct or thermal burn box, >99% destruction efficiency).
- **SF₆**: GWP 23,900× CO₂. The most potent greenhouse gas in common industrial use. Mandatory abatement on all exhaust lines.
- **Cl₂**: Toxic (IDLH 10 ppm), corrosive. Gas cabinet with toxic gas monitoring (electrochemical sensor). Exhaust scrubbing with NaOH wet scrubber.
- **BCl₃**: Reacts violently with moisture to produce HCl and boric acid. Gas cabinet with toxic gas monitoring. Same scrubber requirements as Cl₂.

## Selectivity and Aspect Ratio

### Selectivity

Selectivity is the ratio of etch rates between the target material and the masking or underlying layer. It determines how much mask erosion occurs and whether underlying layers are damaged at the endpoint:

| Material Pair | Chemistry | Selectivity | Notes |
|---------------|-----------|-------------|-------|
| SiO₂:photoresist | CHF₃/CF₄ | 5-10:1 | Resist erodes significantly; thick resist needed for deep oxide etch |
| Si:photoresist | SF₆/O₂ | 2-5:1 | Poor selectivity limits etch depth; hard mask (SiO₂ or metal) preferred |
| Si:SiO₂ | SF₆ or CF₄ | 5-20:1 | Fluorocarbon polymer on SiO₂ surface acts as etch stop |
| SiO₂:Si | CHF₃/CF₄ | 10-20:1 | Carbon-rich chemistry deposits polymer on Si, protecting it |
| Al:photoresist | Cl₂/BCl₃ | 3-5:1 | Moderate; requires careful endpoint to avoid resist failure |
| Poly-Si:SiO₂ (gate) | HBr/Cl₂/O₂ | 20-50:1 | HBr provides excellent selectivity to thin gate oxide |
| Si₃N₄:SiO₂ | CH₂F₂/CHF₃ | 4-8:1 | Used for nitride mask etch with oxide etch stop |

**Improving selectivity**:
- Reduce ion energy (lower bias power) — chemical etching is more selective than physical sputtering.
- Add passivation gases (H₂, CH₂F₂) that deposit protective polymer on the non-target material.
- Lower wafer temperature (cryogenic etching at -100°C dramatically improves selectivity by condensing etch products as passivation on sidewalls).
- Choose chemistry with natural selectivity (e.g., fluorine etches Si but not SiO₂ when passivated with fluorocarbon polymer).

### Aspect Ratio-Dependent Etching (ARDE)

As features get deeper and narrower, etch rate decreases due to transport limitations:

- **Problem**: Reactive species must diffuse into the trench, and volatile products must diffuse out. For a trench with aspect ratio (depth:width) of 10:1, the neutral flux at the bottom is reduced by a factor of 2-5 compared to the opening.
- **Microloading**: Small features etch slower than large features on the same wafer. A 0.5 μm trench etches 30-50% slower than a 5 μm trench at the same process conditions.
- **Reactant depletion**: At high aspect ratios, the etchant gas is consumed before reaching the trench bottom. Increasing flow rate helps but cannot fully compensate.
- **Ion shadowing**: At aspect ratios >5:1, the angular spread of ions (typically ±5-10° from vertical) causes some ions to strike the sidewall instead of the bottom, reducing the vertical etch rate and depositing material on sidewalls.
- **Bosch process mitigation**: The alternating etch-passivation cycles of DRIE partially mitigate ARDE by maintaining a fresh passivation layer and clearing reaction products between etch steps.

## Deep Reactive Ion Etching (DRIE) — Bosch Process

The Bosch process is the industry standard for creating deep, high-aspect-ratio silicon features. It alternates between isotropic etching and conformal polymer passivation in rapid cycles (typically 1-10 seconds per step):

### Process Cycle

**Step 1 — Etch (SF₆ plasma, 1-5 seconds)**:
- SF₆ plasma (100-400 sccm, 20-80 mTorr, 500-2000 W ICP power, 10-50 W bias power) generates fluorine radicals.
- Fluorine etches silicon isotropically: Si + 4F· → SiF₄↑. Etch depth per cycle: 0.5-5 μm depending on SF₆ flow, ICP power, and cycle time.
- Ion bombardment (from bias power) primarily clears the passivation polymer from horizontal surfaces, allowing etching to proceed vertically.

**Step 2 — Passivation (C₄F₈ plasma, 1-5 seconds)**:
- C₄F₈ plasma (50-200 sccm, 20-80 mTorr, 500-2000 W ICP power, 0-10 W bias power) deposits a thin fluorocarbon polymer ((CF₂)ₙ) on all surfaces — horizontal and vertical.
- The polymer thickness per cycle: 10-50 nm. This layer protects sidewalls from fluorine attack during the next etch step.
- Low or zero bias power ensures conformal deposition (no directional ion clearing).

**Step 3 — Repeat** (100-10,000 cycles for typical structures).

### Bosch Process Parameters & Results

| Parameter | Typical Range | Effect |
|-----------|---------------|--------|
| Etch gas flow (SF₆) | 100-400 sccm | Higher → faster etch per cycle, but wider scallops |
| Passivation gas flow (C₄F₈) | 50-200 sccm | Higher → thicker polymer, narrower scallops, slower overall rate |
| ICP power | 500-3000 W | Higher → denser plasma → faster etch and deposition |
| Bias power | 10-50 W (etch), 0-10 W (passivation) | Higher etch bias → faster horizontal clearing, more anisotropic |
| Cycle time (etch) | 1-5 seconds | Shorter → smaller scallops, slower overall rate |
| Cycle time (passivation) | 1-5 seconds | Shorter → thinner passivation, wider scallops |
| Number of cycles | 100-10,000 | Determines total etch depth |

### Performance Characteristics

- **Etch rate**: 2-5 μm/min for silicon (throughput depends on wafer size and feature density).
- **Aspect ratio**: >20:1 achievable (e.g., 100 μm deep trench, 5 μm wide). State-of-the-art tools reach >50:1.
- **Sidewall scalloping**: Each etch-passivation cycle produces a small notch (scallops) on the sidewall. Scalloping amplitude: 50-200 nm, determined by the isotropic component of the etch step. Reducing etch cycle time decreases scallop size at the cost of throughput.
- **Verticality**: 90° ± 0.5° with optimized process. Slight positive or negative taper can be controlled by adjusting the etch:passivation ratio.
- **Selectivity to photoresist**: 20-75:1 (much better than RIE because the low bias power during etch steps reduces physical sputtering of the mask).
- **Selectivity to SiO₂**: >100:1 (fluorocarbon polymer naturally protects oxide surfaces).

### Variants

- **Cryogenic DRIE**: Wafer cooled to -100°C to -140°C. SF₆/O₂ chemistry (no passivation step needed). The cold sidewalls condense SiOₓFᵧ etch products as a passivation layer. Advantages: smooth sidewalls (no scalloping), faster overall etch rate. Disadvantages: requires cryogenic cooling system, selectivity to masking layers varies with temperature.
- **ASE (Advanced Silicon Etch)**: Trade name for Bosch-process DRIE from STS/Surface Technology Systems. The original commercial implementation.
- **Pseudo-Bosch**: Continuous flow of SF₆ + C₄F₈ simultaneously (no switching). Produces smoother sidewalls than standard Bosch but with lower etch rates (~1-2 μm/min). Used for MEMS where scalloping is unacceptable.

## Etch Rate Monitoring & Endpoint Detection

### Optical Emission Spectroscopy (OES)

The primary in-situ endpoint detection method for production plasma etching:

- **Principle**: The plasma emits characteristic optical wavelengths from excited-state species. As the etch reaches the interface between layers, the concentration of etch products changes, altering the emission spectrum.
- **Implementation**: Fiber optic cable views the plasma through a quartz viewport. Diffraction grating spectrometer (200-800 nm) measures intensity at selected wavelengths. Photomultiplier tube or CCD detector provides real-time monitoring.
- **Common endpoint wavelengths**:
  - Si etch: SiF at 440 nm, F at 703.7 nm (decreases as Si is consumed)
  - SiO₂ etch: CO at 483 nm, SiO at 425 nm
  - Al etch: AlCl at 261 nm, Al at 396 nm
  - Photoresist: CN at 388 nm, CH at 431 nm (increases when resist is being etched)
- **Endpoint algorithm**: Monitor the ratio of etch-product wavelength to a reference wavelength (e.g., Ar at 750 nm from a trace argon addition). When the ratio changes by a set amount (typically 10-30% shift), the endpoint is triggered. This compensates for plasma drift during the etch.
- **Accuracy**: ±1-5% of total etch time for open-area etches. For small features (<5% open area), the signal change is too small for reliable endpoint — timed etch or interferometry is used instead.

### Laser Interferometry

- **Principle**: A HeNe laser (632.8 nm) reflects from the wafer surface. As the film thickness changes during etching, the optical path length changes, producing constructive and destructive interference fringes (intensity oscillations). Each full fringe cycle corresponds to λ/(2n) of film removal, where n is the refractive index of the film.
- **For SiO₂ etch** (n = 1.46): each fringe = 632.8/(2 × 1.46) = 217 nm. Count fringes to track etch depth in real time.
- **For silicon etch**: works when the surface is smooth enough for specular reflection. Rough surfaces scatter light and destroy the interference signal.
- **Accuracy**: ±5-10 nm per fringe. Best for transparent films (SiO₂, Si₃N₄, photoresist) where interference is strong.

### Mass Spectrometry (RGA)

- **Principle**: Residual gas analyzer samples the exhaust gas from the etch chamber. Detects etch products (SiF₄ at mass 104, AlCl₃ at mass 133, WF₆ at mass 298).
- **Use case**: Complementary to OES, especially when the optical signal is weak (small feature sizes, deep trenches). Also used for chamber cleanliness verification between runs.

## Process Recipes

### Standard SiO₂ Contact/Via Etch (RIE)

| Parameter | Value |
|-----------|-------|
| Gas chemistry | CHF₃ (40 sccm) / CF₄ (20 sccm) / O₂ (2 sccm) |
| Pressure | 40 mTorr |
| RF power | 300 W (13.56 MHz) |
| DC self-bias | ~450 V |
| Wafer temperature | 20°C (He backside cooling) |
| Etch rate | 80-120 nm/min (SiO₂) |
| Selectivity | 6:1 vs. photoresist, 15:1 vs. Si |
| Endpoint | OES (CO at 483 nm) + 10% overetch |

### Polysilicon Gate Etch (RIE)

| Parameter | Value |
|-----------|-------|
| Gas chemistry | HBr (60 sccm) / Cl₂ (20 sccm) / O₂ (5 sccm) |
| Pressure | 20 mTorr |
| RF power | 250 W |
| DC self-bias | ~350 V |
| Etch rate | 50-100 nm/min (poly-Si) |
| Selectivity | 30:1 vs. SiO₂ (gate oxide etch stop), 4:1 vs. photoresist |
| Critical parameter | Endpoint must stop within 5 nm of gate oxide surface — gate oxide perforation destroys the transistor |

### Aluminum Interconnect Etch (RIE)

| Parameter | Value |
|-----------|-------|
| Gas chemistry | Cl₂ (40 sccm) / BCl₃ (80 sccm) / N₂ (10 sccm) |
| Pressure | 30 mTorr |
| RF power | 400 W |
| DC self-bias | ~500 V |
| Etch rate | 200-400 nm/min (Al) |
| Selectivity | 4:1 vs. photoresist |
| Endpoint | OES (AlCl at 261 nm) |
| Post-etch | DI water rinse to remove chlorine residues (AlCl₃ + H₂O → Al(OH)₃ + HCl — corrosion risk if residues remain) |

### Silicon DRIE (Bosch Process)

| Parameter | Etch Step | Passivation Step |
|-----------|-----------|------------------|
| Gas | SF₆ (200 sccm) | C₄F₈ (100 sccm) |
| ICP power | 2000 W | 1800 W |
| Bias power | 20 W | 0 W |
| Pressure | 40 mTorr | 35 mTorr |
| Duration | 3 seconds | 2 seconds |
| Result per cycle | ~2 μm etch | ~30 nm polymer deposition |
| **Overall etch rate** | **~24 μm/min** (effective) | |
| Selectivity vs. resist | 50:1 | |
| Aspect ratio capability | >20:1 | |

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Grassing (micromasking — conical silicon residues after etch) | Polymer residues from fluorocarbon chemistry act as local etch masks; insufficient ion energy to clear polymer from horizontal surfaces | Increase bias power by 10-20%; reduce CHF₃ or C₄F₈ flow; add 5-10% O₂ to oxidize polymer residues; ensure chamber is clean (run O₂ plasma clean between wafers) |
| Notching at trench bottom (footing) | Charging of SiO₂ at the trench bottom deflects ions laterally, causing localized lateral etching at the oxide-silicon interface | Reduce bias power; increase pressure to reduce ion directionality spread; use notching-suppression chemistry (add H₂ to form passivating SiHₓ); switch to ICP for better ion energy control |
| Sidewall bowing (concave profile) | Excessive isotropic etch component relative to passivation; sidewall polymer too thin or etch step too long | Reduce SF₆ flow or etch cycle time; increase C₄F₈ flow or passivation cycle time; lower pressure to increase ion directionality |
| Photoresist burning (reticulation) | RF power too high for the resist thermal budget; wafer overheating from inadequate He cooling | Reduce RF power; verify He backside cooling pressure (5-20 Torr); use hard mask (SiO₂ or metal) instead of thick resist for deep etches; reduce process time per step |
| Non-uniform etch across wafer (>±5%) | Gas flow maldistribution from showerhead; edge-to-center temperature gradient; RF coupling non-uniformity | Check showerhead for clogging; verify He cooling uniformity; adjust gas flow ratios (add center-edge flow biasing if tool supports it); inspect chamber for coating buildup affecting RF coupling |
| Endpoint detection failure (OES) | Open area too small (<5%); etch product signal below noise floor; viewport coating reduces optical transmission | Use timed etch with pre-calibrated etch rate for small features; clean viewport quartz window; add trace Ar (2-5 sccm) as reference signal; switch to laser interferometry if applicable |

## See Also

- [Core Fab Processes](fab-processes.md) — parent capability: oxidation, deposition, doping, metallization
- [Dopant & Etch Gases](../chemistry/dopant-etch-gases.md) — process gas chemistry supply
- [Gas Handling Vacuum](../gas-handling/vacuum.md) — vacuum systems for etch tools
- [Vacuum Pumps](../vacuum/pumps.md) — pump technology for semiconductor tools
- [Resists & Masks](resists-masks.md) — photoresist and mask technology
- [Cleanrooms](cleanrooms.md) — contamination-controlled environments
- [Advanced Processes](../vlsi-scaling/advanced-processes.md) — advanced node etch challenges

[← Back to Photolithography](index.md)
