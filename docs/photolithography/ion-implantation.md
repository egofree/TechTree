# Ion Implantation

> **Node ID**: photolithography.fab-processes.ion-implantation
> **Domain**: [Photolithography](./index.md)
> **Dependencies**: [`Silicon`](silicon.md)
> **Enables**: [`Vacuum Chambers & Sealing`](chambers.md), [`Electricity Generation & Distribution`](electricity.md)
> **Timeline**: Years 50-80
> **Outputs**: ion_implantation, doped_regions, doping_profiles
> **Critical**: No

## Overview

Precision doping by accelerating ionized dopant species (B⁺, BF₂⁺, P⁺, As⁺) into silicon wafers using a particle accelerator chain: ion source, mass analyzer, acceleration column, and beam scanning system. Replaces thermal diffusion with independent control of dose (10¹¹ to 10¹⁶ ions/cm²) and junction depth (10 to 1000 nm via energy selection from 10 keV to several MeV). Requires high-voltage power, toxic dopant gas handling, and high-vacuum beam lines.

The four parameters that define every implant recipe are species, energy, dose, and beam current. Species selects the dopant type: boron for p-type, phosphorus or arsenic for n-type. Energy sets the penetration depth, ranging from a few keV for shallow source/drain extensions to several MeV for deep retrograde wells. Dose sets the dopant concentration, from 10¹¹ ions/cm² for threshold voltage tweaks to 10¹⁶ ions/cm² for low-resistance contact regions. Beam current sets throughput, measured in milliamps for high-current machines or microamps for precision medium-current tools.

After implantation the wafer must be annealed. The ion impacts displace silicon atoms from their lattice sites, leaving a damaged amorphous layer. Thermal annealing at 900-1100°C accomplishes two things: it repairs the crystal damage by allowing silicon atoms to return to lattice sites, and it electrically activates the dopant by moving implanted atoms from interstitial positions onto substitutional lattice sites where they can donate carriers. These two processes, damage repair and dopant activation, compete with an undesirable third: dopant diffusion. The anneal strategy must maximize activation while minimizing the time at temperature, which drives the adoption of rapid thermal annealing (RTA) that heats the wafer to 1050°C for 10-30 seconds rather than the hours-long furnace soak that would broaden the junction beyond its intended depth.

Modern high-current implanters use a ribbon beam architecture, a wide thin beam that scans the full wafer width in a single pass. This parallel scan replaces the older serial spot-scan approach where a focused beam had to raster across the entire wafer surface. The throughput improvement is dramatic for high-dose implants (source/drain, polysilicon gate doping) that are the bottleneck step in many production flows.

## Prerequisites

### Materials

- Dopant source gases: BF₃ (boron), PH₃ (phosphorus), AsH₃ (arsenic)
- Silicon wafers with photoresist or hard mask patterns already defined
- Photoresist thick enough to stop the implanted ions completely

### Equipment

- [Silicon](silicon.md) — material dependency
- Ion implanter: ion source, mass-analyzing magnet, acceleration column, beam scanner, end station
- High-voltage power supply (10 kV to several MV)
- High-vacuum pumping system (turbo-molecular or cryogenic pumps)
- Rapid thermal annealer (RTA) or batch diffusion furnace

### Knowledge

- Beam physics: mass-to-charge ratio selection, energy-to-depth relationships, Gaussian implant profiles
- Doping physics: carrier concentration versus dose and activation, junction formation
- Vacuum system operation and maintenance
- Radiation safety and toxic gas handling procedures
- Statistical process control: tracking dose uniformity, sheet resistance, and particle counts across lots
- Understanding of projected range (Rp) and straggle (ΔRp) for each species-energy combination

### Infrastructure

- Cleanroom (Class 100 or better) for wafer loading and unloading
- Toxic gas cabinets with continuous monitoring for PH₃ and AsH₃ (exposure limits in low ppb)
- X-ray shielding around the acceleration column and beam line
- Exhaust gas abatement (burn boxes or scrubbers) for dopant source gases
- Backup power for toxic gas monitoring and emergency ventilation (must remain active during power outages)

## Process Description

An ion implanter is a specialized particle accelerator. The ion source ionizes a dopant gas by arc discharge or RF plasma, extracting positive ions. A mass-analyzing magnet bends the extracted beam through a curved flight tube: only ions with the correct mass-to-charge ratio follow the right radius and pass through the resolving aperture. Doubly-charged ions (which would implant at twice the intended depth for a given voltage) are filtered out at this stage. The acceleration column then gives the selected ions their final energy, and a scanning system (electrostatic plates or mechanical scanning) sweeps the beam uniformly across the wafer.

The entire beam path from source to wafer runs under high vacuum (10⁻⁶ Torr or below). Residual gas molecules would scatter the ion beam, degrading uniformity and causing energy contamination. Cryogenic pumps on the end station also serve a second purpose: they capture the gases released when the ion beam strikes photoresist, which outgasses hydrogen, CO, CO₂, and hydrocarbons during high-dose implants.

Photoresist outgassing is a significant process concern beyond its effect on vacuum pressure. The outgassed species can polymerize on high-voltage insulators inside the implanter, creating conductive paths that cause electrical breakdown and beam instability. Regular cryo-pump regeneration and periodic chamber cleaning are necessary to maintain process integrity. The photoresist itself must be thick enough to stop the ions completely; under-thinned resist lets ions penetrate to unintended areas, creating unwanted doping that no amount of annealing can fix.

### Step-by-Step Procedure

1. Load patterned wafers onto the implanter end station. Verify photoresist thickness against the implant energy using the resist stopping range tables.
2. Select the dopant gas and set the ion source parameters. Ignite the source plasma and tune for stable beam extraction.
3. Set the mass-analyzing magnet to select the desired ion species (B⁺, BF₂⁺, P⁺, As⁺). Verify species purity by scanning the mass spectrum at the resolving aperture.
4. Set the acceleration voltage for the target implant depth. Calibrate dose by measuring beam current with a Faraday cup before exposing wafers.
5. Implant wafers at the programmed tilt angle (typically 7° from normal) and twist rotation to suppress channeling. Monitor dose uniformity via four corner Faraday cups.
6. Unload wafers and transfer to rapid thermal annealer. Anneal at 950-1100°C for 10-30 seconds to activate dopants and repair crystal damage with minimal diffusion.

7. Strip photoresist in an oxygen plasma asher, followed by a wet clean (sulfuric/peroxide or solvent) to remove any residual carbonized resist left by the ion bombardment. Inspect for particles and resist residue before the next lithography step.

For implant-through-mask processes, the photoresist must be thick enough to stop the highest-energy ions in the recipe. The stopping range depends on the ion species, energy, and resist density, and is calculated from tabulated stopping power data (e.g., SRIM/TRIM simulations). A common rule of thumb is to use resist thickness equal to 1.5× the projected range, with an additional safety margin for straggle (the statistical spread in implant depth). For high-energy implants (above 500 keV), photoresist may be impractical as a mask, and a hard mask of deposited oxide or nitride is used instead.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Implant Energy | 10 keV - 5 MeV | Determines junction depth; higher energy = deeper implant |
| Dose | 10¹¹ - 10¹⁶ ions/cm² | Sets dopant concentration; low dose for Vt adjust, high dose for S/D |
| Beam Current | 1 μA - 30 mA | Sets throughput; high current for high-dose implants |
| Tilt Angle | 0° - 15° from normal | 7° typical to suppress channeling |
| Anneal Temperature | 900 - 1100°C | RTA: 10-30 sec; furnace: 30-60 min |
| Twist Rotation | 0° - 360° | Rotated 30-90° from major flat to avoid crystal planes |

## Safety Considerations

Ion implanters present multiple severe hazards. The acceleration column operates at tens to hundreds of kilovolts, storing lethal electrical energy. All maintenance requires lockout/tagout, residual voltage discharge, and verified zero-energy state. The ion beam striking metal surfaces generates X-rays proportional to the beam energy, requiring lead shielding and safety interlocks that prevent access during operation.

The dopant gases are the most acute hazard. Arsine (AsH₃) and phosphine (PH₃) have occupational exposure limits below 50 parts per billion. Both are blood and nerve toxins with no warning properties at dangerous concentrations. Gas cabinets must have welded stainless steel tubing, continuous toxic gas monitors with audible alarms, automatic shutdown on detection, and emergency exhaust ventilation. BF₃ is corrosive and reacts with moisture to form hydrofluoric acid. Arsine exposure causes hemolytic anemia (destruction of red blood cells) with symptoms that may be delayed by hours, making continuous monitoring more reliable than human perception for detecting leaks.

- **Electrical**: High-voltage lockout/tagout procedures mandatory for all maintenance
- **Radiation**: X-ray shielding and interlocks on beam line; dosimetry badges for operators
- **Toxic gas**: PH₃ and AsH₃ gas cabinets with ppm-level monitoring, auto-shutdown, emergency ventilation
- **Mechanical**: Vacuum chamber implosion risk; never exceed pressure ratings

### Personal Protective Equipment

- Chemical splash goggles and face shield when connecting or disconnecting gas lines
- Heavy rubber gloves and chemical apron for gas cylinder handling
- Dosimetry badge (X-ray) for personnel working near the implanter during operation
- Cryogenic gloves when handling liquid nitrogen dewars for cryo-pumps
- Anti-static wrist strap when handling wafers near beam line components to prevent electrostatic discharge damage

### Emergency Procedures

- Toxic gas alarm triggers automatic gas shutoff, building ventilation exhaust, and area evacuation
- Know the location of the nearest emergency gas shutoff valve and the scrubber bypass
- Hydrogen cyanide antidote kits (for arsine exposure) must be stocked within the facility
- X-ray interlock breach stops the beam and discharges high voltage within seconds

## Quality Control

### Acceptance Criteria

- **Doped Regions**: Sheet resistance within ±5% of target across the wafer (measured by 4-point probe mapping)
- **Doping Profiles**: Junction depth within ±10% of target, peak concentration within specification
- **Uniformity**: Dose uniformity across 300mm wafer better than ±1% (1σ) for medium-current implants

### Testing Methods

- Four-point probe sheet resistance mapping: 49-point or 121-point maps across the wafer surface
- Secondary Ion Mass Spectrometry (SIMS): depth profile of dopant concentration with nm resolution
- Therma-Wave or carrier illumination: non-destructive measurement of implant dose for inline monitoring
- Cross-section SEM or TEM: direct imaging of junction depth and crystal damage recovery
- Spreading resistance profiling (SRP): measures carrier concentration versus depth by probing a beveled wafer surface

### Sampling Protocol

- Measure sheet resistance on every wafer at 49+ sites; map uniformity across lot
- Run SIMS depth profiles on one wafer per lot to verify junction depth and profile shape
- Calibrate beam current against Faraday cup standards before each implant campaign
- Track uniformity trends across lots to detect scanner drift or source degradation early

The sheet resistance map is the primary inline quality metric for ion implantation. A four-point probe measures resistance at 49 or more sites across the wafer, producing a contour map that reveals radial uniformity patterns. Center-to-edge non-uniformity indicates beam scanning issues. Localized hot spots suggest beam astigmatism or Faraday cup calibration errors. The sheet resistance is related to dose by the Irvin curve, which maps dose and species to expected sheet resistance for a given junction depth. Discrepancies between measured and predicted sheet resistance point to activation problems, contamination, or energy contamination from unwanted ion species.

## Scaling Notes

Production ion implanters process 20-25 wafers per hour at high dose, limited by beam current capacity. Scaling from a single-wafer research implanter to a production tool involves:

- **Research scale**: Single wafer, manual loading, 10 μA beam, one species at a time. A few wafers per day.
- **Pilot production**: Batch end station (25 wafers), automated cassette-to-cassette loading, 1-5 mA beam. Tens of wafers per hour.
- **Volume production**: Ribbon beam (scans full wafer width in one pass), 10-30 mA beam current, dual species capability, in-situ charge neutralization. 20+ wafer equivalents per hour even at high dose.

The throughput bottleneck at scale is high-dose implants (source/drain, polysilicon gate doping), which can consume 30-60 seconds per wafer at 10¹⁵ ions/cm². High-current implanters use ribbon beam architecture to scan the full wafer width simultaneously, eliminating the serial spot-scan bottleneck.

Wafer charging is a concern during high-current implantation. The ion beam deposits positive charge on the wafer surface, and if the photoresist is insulating (as it typically is), charge accumulates until dielectric breakdown occurs, damaging thin gate oxides on the wafer. Modern implanters use electron flood guns or plasma electron showers to neutralize the beam charge, flooding the wafer surface with low-energy electrons that compensate for the positive ion current. Charge neutrality must be maintained within a few volts to avoid damaging sub-5 nm gate oxides.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Energy contamination (double peaks in SIMS profile) | Doubly-charged ions passing the mass analyzer | Adjust mass resolution; add electrostatic filter after magnet |
| Channeling (ions penetrate deeper than projected range) | Beam aligned with crystal channel direction | Set tilt to 7°, add twist rotation, or pre-amorphize with Ge implant |
| Particle contamination on wafer surface | Beam line deposits or end station debris | Clean beam line, replace worn wafer clamps, add electrostatic shields |
| Dose non-uniformity at wafer edge | Beam scan overshoot or undershoot at edge | Adjust scan waveform compensation; verify corner Faraday cup readings |
| Photoresist outgassing causing pressure spike | High-dose beam decomposing resist too fast | Reduce beam current, add cryo-pumping capacity, or pre-bake resist |
| Sheet resistance higher than target | Incomplete dopant activation during anneal | Increase anneal temperature or time; check for residual crystal damage by TEM |
| Boron penetration through gate oxide | Boron diffusing through thin gate oxide during anneal | Add nitrogen to gate oxide (NO anneal) to block boron diffusion; reduce anneal temperature |
| Implant angle error from wafer misalignment | Incorrect notch or flat orientation on end station | Verify wafer orientation before implant; recalibrate notch alignment sensor |

## Variations and Alternatives

- **High-current implanters**: Large beam currents (5-30 mA) for source/drain and polysilicon doping. Limited energy range, optimized for throughput at high dose.
- **Medium-current implanters**: Wide energy range (10 keV to 1 MeV) for well implants and threshold voltage adjustment. Lower beam current but higher precision.
- **High-energy implanters**: Tandem acceleration achieves 1-5 MeV for deep retrograde wells and buried layers, eliminating the need for some epitaxial layers.
- **Cluster ion implantation**: Molecular ions like B₁₀H₁₄ or B₁₈H₂₂ deliver many dopant atoms per incident ion, boosting throughput and suppressing channeling.
- **Thermal diffusion**: Older, simpler alternative that requires fewer capital resources. Cannot independently control dose and depth. Still used for deep wells where precision is less critical.

- **BF₂⁺ molecular implant**: Using BF₂⁺ instead of B⁺ for shallow p-type implants. The heavier molecule implants at roughly half the depth of B⁺ at the same energy, making it easier to achieve ultra-shallow junctions without going to impractically low energies. The fluorine byproduct can passivate defects in the implanted region.

Channeling is a phenomenon specific to crystalline substrates where implanted ions travel abnormally deep into the crystal by passing through the open channels between rows of silicon atoms rather than stopping at the statistical projected range. Silicon has a diamond cubic lattice with channels along the <110> directions that are wide enough for small dopant ions like boron to penetrate deeply. Channeling is suppressed by tilting the wafer (typically 7° from the beam normal) and applying a twist rotation to avoid major crystal axes. For critical implants where even residual channeling is unacceptable, a pre-amorphization implant of a heavy species (germanium at 10-50 keV) destroys the crystal order before the dopant implant, eliminating the channeling paths entirely.

Dopant activation during annealing involves two competing processes. The thermal energy moves implanted dopant atoms from interstitial positions (electrically inactive) to substitutional lattice sites (electrically active). Simultaneously, the same thermal energy causes dopant atoms to diffuse, broadening the as-implanted concentration profile. The ratio of activated fraction to diffusion broadening improves with spike anneals (very rapid heating to peak temperature followed by immediate cooling), which are enabled by RTA systems with ramp rates exceeding 100°C per second. These spike anneals achieve near-complete activation at 1050°C with total process times under 30 seconds, limiting diffusion to a few nanometers.

A typical CMOS transistor requires 5-10 separate implant steps at different energies, doses, and species: well implants (MeV phosphorus for n-well, MeV boron for p-well), channel stop implants, threshold voltage adjust implants (low-dose boron), source/drain extension implants (low-energy arsenic or BF₂⁺), halo implants (tilted implant for short-channel effect control), and source/drain contact implants (high-dose phosphorus or boron). Each implant requires a separate photoresist mask level and anneal cycle. The cumulative thermal budget from all anneals must be managed to prevent excessive diffusion of earlier implants.

The ion source requires periodic maintenance because the arc discharge or RF plasma erodes the source components over time. Tungsten filaments in arc discharge sources burn out after 50-100 hours of operation. The source chamber walls accumulate conductive deposits from the dopant gas decomposition, eventually shorting the extraction electrodes. Source rebuilds are scheduled maintenance events, typically every 100-200 hours, and each rebuild requires beam re-tuning and dose re-calibration before production resumes.

The mass-analyzing magnet is the critical species-selection element. The magnetic field bends the ion beam through a curved trajectory, with the radius of curvature determined by the ion mass-to-charge ratio. By setting the magnetic field strength, only the desired ion species (e.g., B⁺ at mass 11) follows the correct path through the resolving slit into the acceleration column. Heavier or lighter species are deflected too little or too much and strike the chamber walls. The resolving power of the magnet must be sufficient to separate species with close mass-to-charge ratios, such as ¹¹B⁺ (mass 11) from ²²Ne²⁺ (also mass 11), which would otherwise cause energy contamination.

Implanted wafers must be annealed promptly after implantation. If wafers sit for extended periods after a high-dose implant, the amorphous damage layer can recrystallize imperfectly (solid-phase epitaxial regrowth), creating extended defects that are harder to anneal out than the initial point defects. Rapid thermal annealing (RTA) is preferred for shallow junctions because the short time at temperature (10-30 seconds) limits dopant diffusion to a few nanometers while still achieving 95%+ electrical activation. Furnace annealing is used for deeper implants where diffusion is less concerning and batch throughput is needed. The anneal ambient is typically nitrogen or forming gas (N₂/H₂) to prevent unwanted oxidation during the thermal cycle.

## References

- [Core Fab Processes](fab-processes.md) — parent capability
- [Photolithography Domain](./index.md) — domain overview and related capabilities
- [Silicon](silicon.md) — upstream dependency (material)
- [Vacuum Chambers & Sealing](chambers.md) — downstream capability
- [Electricity Generation & Distribution](electricity.md) — downstream capability

---

Ion implantation has largely replaced thermal diffusion as the primary doping method in semiconductor manufacturing because it provides independent control of two variables that diffusion couples together: dopant concentration and junction depth. In thermal diffusion, the surface concentration and junction depth are both determined by the temperature and time of the diffusion step, making it impossible to independently adjust one without affecting the other. Ion implantation decouples these parameters: the dose sets the concentration and the energy sets the depth, giving the process engineer full control over the doping profile.

The projected range (Rp) of an implanted ion is the average depth the ion penetrates before coming to rest, and it depends on the ion energy, ion mass, and target material. Lighter ions (boron, mass 11) penetrate deeper than heavier ions (arsenic, mass 75) at the same energy. The straggle (ΔRp) is the standard deviation of the implant depth distribution, representing how spread out the dopant atoms are around the peak concentration. A typical boron implant at 100 keV has a projected range of about 300 nm with a straggle of 80 nm, producing a roughly Gaussian doping profile. Higher energies push the peak deeper but also increase straggle, broadening the profile.

For shallow junctions required in sub-100 nm transistors, the implant energy is reduced to a few keV. At these low energies, the beam becomes difficult to transport (space charge repulsion within the beam causes it to expand), and deceleration mode is used: the beam is extracted at higher energy (where transport is efficient) and then decelerated just before the wafer. Beam neutralization (electrons trapped in the beam potential well) must be carefully managed in deceleration mode to prevent energy contamination from neutral atoms that cannot be decelerated.

*Part of the [Bootciv Tech Tree](../index.md) · [Photolithography](./index.md) · [All Domains](../index.md)*
*Part of the [Bootciv Tech Tree](../index.md) · [Photolithography](./index.md) · [All Domains](../index.md)*
