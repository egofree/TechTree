# Ion Implanter

> **Node ID**: photolithography.ion-implanter
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`vacuum`](../vacuum/index.md), [`gas-handling`](../gas-handling/index.md), [`energy.electricity`](../energy/electricity.md), [`measurement`](../measurement/index.md)
> **Enables**: [`photolithography.fab-processes`](fab-processes.md), [`vlsi-scaling.advanced-processes`](../vlsi-scaling/advanced-processes.md)
> **Timeline**: Years 50-80
> **Outputs**: doped_wafers, junction_profiles, threshold_adjusted_devices
> **Critical**: No — thermal diffusion provides a functional baseline for doping; ion implantation enables independent control of dose and junction depth required for sub-micron devices

This article covers the construction of a medium-current ion implanter (10-500 keV, 0.1-5 mA). For implantation physics, dose/energy parameters, annealing, and process integration, see [Ion Implantation](ion-implantation.md). For high-current (>5 mA) and high-energy (>500 keV) implanters, the construction principles are similar but scaled — higher beam currents require more powerful ion sources and beam optics; higher energies require larger acceleration columns and more extensive radiation shielding.

**Note on complexity**: The ion implanter is one of the most complex pieces of semiconductor equipment, combining a particle accelerator, mass spectrometer, high-voltage system, and precision wafer handling into one tool. Construction requires precision machining, high-voltage engineering, magnetic field design, and vacuum technology at a level that presupposes substantial industrial infrastructure. This article describes the subsystems and construction approach; practical construction at a bootstrap-civilization level represents a significant engineering challenge.

## Overview

![Ion implantation machine at LAAS 0521](../images/photolithography/photolithography_ion-implanter.jpg)

> *Ion implantation machine front end at LAAS-CNRS technological facility in Toulouse, France.*

> *Image: Guillaume Paumier (user:guillom), CC BY-SA 3.0*

Ion implantation is the primary method for introducing dopant atoms (boron, phosphorus, arsenic) into silicon wafers at controlled concentrations and depths. Unlike thermal diffusion — where dopant concentration and junction depth are coupled — ion implantation independently controls dose (atoms/cm²) via beam current and time, and junction depth (projected range) via acceleration energy. This independent control is essential for modern device fabrication: source/drain junctions, threshold voltage adjustment, channel stops, and well formation all require precise dopant profiles that thermal diffusion cannot provide.

A medium-current implanter (10-500 keV, 0.1-5 mA) handles approximately 80% of all implant steps in a typical IC process flow. The machine accelerates ions to energies of 10-500 keV, selects the desired species by mass analysis, scans the beam uniformly across the wafer, and measures the delivered dose in real time. Typical throughput: 10-30 wafers/hour. The machine requires high vacuum (10⁻⁶-10⁻⁷ Torr) throughout the beamline to prevent ion scattering, and handles some of the most toxic gases in industrial use (arsine, IDLH 3 ppm; phosphine, IDLH 50 ppm).

The ion implanter represents a convergence of particle accelerator physics, mass spectrometry, high-voltage engineering, and precision vacuum mechanics. It is one of the last pieces of semiconductor equipment that a bootstrap civilization would develop — thermal diffusion provides a functional baseline for doping at feature sizes above ~2 μm, while ion implantation becomes necessary for sub-micron devices.

## Principle

An ion implanter ionizes dopant atoms (B⁺, P⁺, As⁺, BF₂⁺) from a gas or solid source, selects a single ion species by mass using a magnetic sector analyzer, accelerates the ions to a controlled energy (10-500 keV) in an electrostatic column, and scans the ion beam uniformly across the wafer surface. The ion energy determines the implant depth (projected range); the ion current integrated over time determines the dose (atoms/cm²). This provides independent control of junction depth and dopant concentration — unlike thermal diffusion where these parameters are coupled.

The ion beam path: ion source → extraction electrode → mass analyzer magnet → resolving slit → acceleration column → beam scanning → wafer (end station). Each component operates at high vacuum (10⁻⁶–10⁻⁷ Torr) to prevent beam scattering by residual gas molecules.

## Prerequisites

- [High vacuum technology](../vacuum/index.md) — turbomolecular or cryopumps for beamline vacuum
- [High-voltage power supplies](../energy/electricity.md) — 10-500 kV DC, stable to ±0.1%
- [Electromagnet construction](../energy/electricity.md) — for the mass analyzer (B = 0.1-1 T)
- [Precision machining](../machine-tools/machining.md) — beamline components, electrode alignment
- [Gas handling](../gas-handling/index.md) — dopant gas delivery (BF₃, AsH₃, PH₃)
- [Water cooling](../water/index.md) — for beamline components and electromagnet

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Stainless steel beamline tube | 10-30 m total | 100-200 mm ID, CF-flanged sections | [Vacuum Chamber](../vacuum/vacuum-chamber.md) | — |
| Turbomolecular pumps | 3-5 | 300-1000 L/s each, for beamline sections | [Vacuum Pumps](../vacuum/pumps.md) | Cryopumps |
| Ion source assembly | 1 | Arc chamber, filament, extraction electrodes | Custom fabrication | — |
| Tungsten filament (ion source) | Spares | 0.5-1.0 mm wire, for electron emission | [Metals](../metals/index.md) | — |
| Electromagnet (mass analyzer) | 1 | 90° bend, B = 0.1-1 T, pole gap 50-100 mm | Custom fabrication | — |
| Copper magnet wire | 50-200 kg | Rectangular cross-section, insulated | [Metals](../metals/index.md) | — |
| High-voltage power supply | 1 | 10-500 kV DC, 0.1-5 mA, ±0.1% stability | [Energy](../energy/electricity.md) | — |
| Extraction power supply | 1 | 20-50 kV DC, 10-50 mA | [Energy](../energy/electricity.md) | — |
| Electrostatic deflection plates | 2 pairs | For X-Y beam scanning, 100-1000 Hz | Custom fabrication | — |
| Faraday cup | 1 | Beam current measurement, water-cooled | Custom fabrication | — |
| Wafer handling robot | 1 | End station, cooled platen, cassette-to-cassette | [Automation](../automation/index.md) | Manual load (reduced throughput) |
| Dopant gas handling | 1 set | BF₃, AsH₃, PH₃ gas cabinets, MFCs | [Gas Handling](../gas-handling/index.md) | Solid source with heated oven |

## Process Description

### Ion Source

1. **Build the arc chamber**: Machine a stainless steel or aluminum chamber (50-100 mm diameter, 50-80 mm long) with gas inlet, filament feedthroughs, and an extraction aperture (5-15 mm slit or circular opening). The chamber holds the dopant gas at 10⁻³–10⁻² Torr during operation.

2. **Install the filament**: Mount a tungsten filament (0.5-1.0 mm wire, hairpin shape) inside the arc chamber on electrical feedthroughs. The filament is heated to ~2500°C by passing 20-50 A through it, emitting electrons (thermionic emission) that ionize the dopant gas. Filament lifetime: 20-100 hours depending on gas chemistry.

3. **Install the extraction electrode**: Mount a stainless steel extraction electrode (plate with matching aperture) 5-15 mm outside the arc chamber aperture. Apply +20-50 kV to the extraction electrode to pull positive ions out of the arc chamber and form them into a beam. The extraction gap and voltage determine the beam emittance (quality).

### Mass Analyzer

4. **Build the analyzing magnet**: Construct a 90° bending electromagnet. The magnet consists of an iron or low-carbon steel yoke with pole pieces that create a uniform magnetic field across the beam path. Pole gap: 50-100 mm (must accommodate the beam diameter plus clearance). Field strength: 0.1-1 T, adjustable by varying the coil current. Wind the magnet coils from rectangular copper wire (enough for 50-200 A at 10-50 V). The magnet bends the ion trajectory with radius r = mv/(qB). At fixed B, only ions with the desired mass-to-charge ratio pass through the exit slit.

5. **Install the resolving slit**: Place a stainless steel plate with an adjustable slit (0.5-3 mm width) at the exit of the analyzing magnet. The slit width determines mass resolution (m/Δm) and beam current — narrower slit gives better species purity but lower current. Adjust to achieve m/Δm > 100 (sufficient to separate ¹¹B⁺ from ¹²C⁺).

### Acceleration Column

6. **Build the acceleration tube**: Assemble a series of ceramic (alumina) insulator rings with stainless steel electrodes, stacked to form a column 0.5-2 m long. Each electrode ring is biased at a progressively higher voltage, creating a uniform electric field that accelerates ions from the extraction energy to the final implant energy. The column must hold off the full voltage (10-500 kV) without arcing. Voltage grading resistors (100 MΩ each) between electrodes ensure uniform voltage distribution. Mount the column inside a grounded steel enclosure filled with SF₆ gas (insulating) or oil for voltages above 100 kV.

7. **Install the high-voltage power supply**: Connect a high-stability DC power supply (10-500 kV, 0.1-5 mA, ±0.1% regulation) to the acceleration column. The supply must maintain stable voltage during beam current variations — voltage ripple translates directly into implant energy spread (±0.1% = ±100 eV at 100 keV). Enclose the HV supply and column in an interlocked cabinet with grounding sticks for safe maintenance.

### Beam Scanning and End Station

8. **Install electrostatic scan plates**: Mount two pairs of deflection plates (X and Y) in the beamline after the acceleration column. Apply ramp voltages (100-1000 Hz triangular waveform) to raster the beam across the wafer. The scan amplitude is set so the beam overshoots the wafer edges by 10-20% to ensure uniform dose at the wafer periphery (overscan).

9. **Build the Faraday cup**: Machine a water-cooled stainless steel cup (beam dump) that measures the ion beam current. The Faraday cup is the primary dose measurement instrument: Dose = ∫I dt / (q × A), where I = beam current, q = electronic charge, A = scan area. The cup must suppress secondary electron emission (biased to -300 V) for accurate measurement. Accuracy: ±0.5%.

10. **Build the end station**: Construct a wafer handling chamber with a cooled platen (-20°C to +100°C), wafer load lock, and cassette-to-cassette wafer handling. The platen holds the wafer at a controlled tilt angle (typically 7° from beam axis to prevent ion channeling). Helium backside cooling (5-20 Torr) maintains wafer temperature below 100°C during high-current implants. Install a wafer rotation mechanism for uniform implantation.

### Vacuum System

11. **Assemble the beamline vacuum**: Connect all beamline sections with CF flanges. Install turbomolecular pumps at 3-5 points along the beamline (ion source region, mass analyzer region, acceleration column, end station). Base pressure target: <10⁻⁶ Torr throughout the beamline. Higher pressure causes beam neutralization (ions capture electrons from residual gas) and loss of dose accuracy.

### Safety Systems

12. **Install radiation shielding**: For implanters operating above 30 keV, Bremsstrahlung X-rays are produced when ions strike beamline components. Shield the acceleration column and beamline with lead or steel sheeting (thickness depends on maximum energy — 2-5 mm Pb for 100-500 keV). Install radiation area monitors and warning signs. For MeV-class implanters, substantial concrete shielding is required.

13. **Install toxic gas safety**: Dopant gases (AsH₃, PH₃) are among the most toxic industrial gases (IDLH: AsH₃ = 3 ppm, PH₃ = 50 ppm). Install gas cabinets with continuous monitoring, automatic shut-off valves, and exhaust gas scrubbing (caustic wet scrubber or thermal destruct). Emergency protocol: evacuate immediately, SCBA required for re-entry.

## Quantitative Parameters

| Parameter | Value |
|-----------|-------|
| Energy range | 10-500 keV (medium-current) |
| Beam current | 0.1-5 mA |
| Dose range | 10¹¹–10¹⁶ cm⁻² |
| Dose uniformity | ±1% across 200 mm wafer |
| Mass resolution (m/Δm) | >100 |
| Throughput | 10-30 wafers/hour |
| Base pressure (beamline) | <10⁻⁶ Torr |
| Energy stability | ±0.1% |
| Wafer temperature during implant | <100°C (with He backside cooling) |
| Implanted species | B⁺, BF₂⁺, P⁺, As⁺ |

## Strengths

- Independent control of dose (beam current × time) and junction depth (acceleration energy) — impossible with thermal diffusion
- Excellent dose uniformity (±1%) across large wafers
- Multiple dopant species selectable by adjusting the mass analyzer magnetic field
- Self-aligned implantation — the gate electrode acts as a mask for source/drain implant, ensuring perfect registration
- Shallow junctions achievable with low energies (5-30 keV) — not possible with thermal diffusion

## Weaknesses

- Extremely complex machine — combines particle accelerator, mass spectrometer, and precision wafer handling
- Requires toxic dopant gases (AsH₃, PH₃) with full safety infrastructure
- High-voltage systems (10-500 kV) require extensive safety interlocks and radiation shielding
- Ion bombardment damages the silicon crystal lattice — annealing (900-1100°C) is required after every implant step
- Throughput limited for high-dose implants — source/drain implants at 10¹⁵-10¹⁶ cm⁻² can take 30-120 seconds per wafer
- Ion bombardment damages the silicon crystal lattice — annealing (900-1100°C) is required after every implant step

## Safety

- **Toxic dopant gases**: AsH₃ (IDLH 3 ppm) and PH₃ (IDLH 50 ppm) are immediately dangerous to life. Gas cabinets with continuous electrochemical monitoring, automatic shut-off, and exhaust scrubbing are mandatory. Emergency protocol: evacuate, SCBA. BF₃ is corrosive and reacts with moisture to form HF and boric acid — treat any BF₃ leak as an HF exposure hazard.
- **High voltage**: 10-500 kV DC is lethal. Interlocked enclosures, grounding sticks, and lock-out/tag-out. Never approach the acceleration column without verifying zero voltage with a grounded probe. Capacitors in the HV power supply can hold lethal charge for minutes after power-off — always discharge through a grounding stick.
- **X-ray radiation**: Bremsstrahlung X-rays produced at energies >30 keV. Shield with lead or steel. Radiation monitoring badges for operators. Post radiation area warnings for MeV-class implanters. Annual dosimetry report required for all personnel working within 3 meters of the beamline.
- **Ionizing radiation dose limits**: Monitor and limit operator exposure per local radiation safety regulations. Dosimetry badges (TLD or film) worn by all personnel working near the implanter. Quarterly dose reports. Annual dose limit: 50 mSv (5 rem) whole body per 10 CFR 20.
- **Ozone generation**: High-voltage components can produce ozone from corona discharge. Verify ventilation in the high-voltage cabinet. Ozone TLV: 0.1 ppm. Prolonged exposure causes respiratory irritation and lung damage.
- **Vacuum implosion risk**: Beamline tubes and viewports are under vacuum (10⁻⁶-10⁻⁷ Torr). Scratched or chipped viewports can implode, launching glass fragments at high velocity. Replace any viewport with visible damage. Stand clear of viewports during pump-down (maximum implosion risk at 1-100 Torr).
- **Wafer breakage during implant**: Thin wafers (<200 μm) under mechanical clamp force can fracture during high-current implants. Use electrostatic clamping instead of mechanical clamps for wafers below 250 μm thickness. Broken wafer fragments contaminate the end station and require a 30-60 minute clean-up procedure before resuming production.
- **Noise exposure**: High-current ion sources, turbomolecular pumps, and cooling water systems generate sustained noise levels of 70-85 dB in the implanter enclosure. Hearing protection required for personnel spending more than 30 minutes inside the enclosure during operation.

## Beam Characterization

After construction, the beam must be characterized to verify that dose, energy, and uniformity meet specification:

**Beam current measurement**: Measure the beam current at the Faraday cup with the electrometer. Verify linearity of beam current vs. arc current in the ion source (should be linear at low arc currents, saturating at high arc currents when the source gas is fully ionized). Record the maximum beam current achievable for each species.

**Beam profile measurement**: Place a segmented Faraday cup (array of small collectors across the beam cross-section) at the wafer plane. Measure the beam current density profile. A Gaussian profile is expected — the full-width at half-maximum (FWHM) should be 30-80 mm depending on the extraction and focusing optics. Non-Gaussian profiles indicate misaligned electrodes or magnetic field errors.

**Mass resolution verification**: Set the analyzing magnet to transmit B⁺ (mass 11). Scan the magnetic field slowly while monitoring beam current. Plot beam current vs. mass number. The mass peaks should be well-separated — m/Δm >100 means the ¹¹B⁺ peak is fully resolved from ¹²C⁺. If peaks overlap, narrow the resolving slit or improve the magnetic field uniformity.

**Energy verification**: Implant a test wafer at a known energy (e.g., 100 keV B⁺). Measure the implant profile by SIMS (secondary ion mass spectrometry). The projected range (Rp) should match SRIM/TRIM simulation within ±5%. Energy error indicates voltage calibration problems in the acceleration column.

## Quality Control

**Dose verification**: Implant test wafers at 3 dose levels (low, medium, high) for each species. Anneal and measure sheet resistance at 49 points. Verify dose uniformity <±1% across the wafer and <±2% wafer-to-wafer repeatability. Run dose verification weekly or after any beamline maintenance.

**Beam purity check**: With the analyzing magnet set for B⁺, scan a small fraction of the beam into a secondary Faraday cup or beam profile monitor. Verify that the beam contains >99% B⁺ (no significant C⁺, N⁺, or O⁺ contamination from residual gas ionization in the source). Poor beam purity produces uncontrolled doping.

**Particle monitoring**: Measure particles on test wafers before and after implant. Added particles must be <20 particles ≥0.16 μm (200 mm wafer). High particle counts indicate wafer handling contamination (mechanical clamp wear, robotic arm debris) or beamline debris (sputtered metal from apertures).

**Energy calibration**: Verify acceleration energy quarterly by implanting a known species at a known energy and measuring Rp by SIMS. Energy error must be <±1%. Recalibrate the high-voltage power supply if energy drifts beyond this tolerance.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Beam current unstable — fluctuating ±20% | Filament in ion source aging or arcing; gas flow instability in source chamber | Replace tungsten filament; stabilize gas flow with a precision leak valve; check source chamber pressure with capacitance manometer |
| Wrong species detected at wafer — B⁺ contains C⁺ contamination | Mass analyzer resolving slit too wide; magnetic field drift with temperature | Narrow the resolving slit (reduces beam current but improves purity); install temperature-stabilized magnet yoke; recalibrate B-field vs. current curve |
| Dose non-uniformity ±5% across wafer | Electrostatic scan plates unbalanced; scan waveform not linear; wafer not flat on platen | Verify scan waveform linearity with oscilloscope; adjust X and Y scan amplitudes independently; check wafer mounting (vacuum chuck hold-down, no wafer bow) |
| Beam spot at wrong position on wafer | Beam steering from stray magnetic fields; misaligned beamline components | Install magnetic shielding (μ-metal) around beamline; realign beamline components with laser alignment tool; check earth field compensation coils |
| Excessive wafer heating during implant — resist reticulation | Beam power density too high; inadequate He backside cooling; platen not in thermal contact | Reduce beam current or increase scan speed; verify He backside pressure at 5-20 Torr; check platen surface flatness and wafer-to-platen contact |
| X-ray alarm triggered during high-energy operation | Inadequate Bremsstrahlung shielding around acceleration column; beam striking beamline wall instead of Faraday cup | Add lead shielding (2-5 mm for 100-500 keV); realign beam to center on Faraday cup; verify all beamline apertures are aligned |

## Maintenance Schedule

| Component | Interval | Action |
|-----------|----------|--------|
| Ion source filament | 20-100 hours | Replace when beam current drops 20% below initial value at standard conditions |
| Extraction electrode | 200-500 hours | Inspect for sputter erosion; replace when aperture diameter increases >10% from nominal |
| Analyzing magnet pole pieces | 1000+ hours | Inspect for deposited material from beam; clean with fine abrasive if needed |
| Faraday cup | 500-1000 hours | Inspect for sputter erosion; verify secondary electron suppression bias (-300 V) is functional |
| Vacuum pump oil (if rotary vane) | 500-1000 hours | Change oil; switch to dry pumps to eliminate hydrocarbon contamination |
| O-ring seals on beamline | 1000+ hours | Inspect for compression set; replace if leak rate exceeds 10⁻⁸ atm·cc/s |
| High-voltage power supply | 5000+ hours | Verify voltage calibration with high-voltage divider; check ripple <0.1% |
| Beamline alignment | 1000+ hours or after any service | Verify beam spot position at end station using beam profile monitor; realign if offset >5 mm from center |

## Scaling Notes

- **Medium-current to high-current**: High-current implanters (5-25 mA beam current) use larger ion sources (Bernas or Freeman sources), dual-magnet mass analysis, and mechanical wafer scanning (spinning disk) instead of electrostatic scanning. The spinning disk handles higher beam power without beam steering limitations.

- **Medium-current to high-energy**: High-energy implanters (500 keV to several MeV) use tandem accelerators (negative ion source → strip to positive → accelerate twice) or RF linear accelerators. The construction principles are the same but the acceleration column is 2-5× longer, radiation shielding requirements increase, and the high-voltage power supply must be rated for MeV operation.

- **From single-wafer to batch**: Early implanters processed one wafer at a time (throughput: 5-15 wafers/hour). Production implanters use spinning disks holding 10-20 wafers, increasing throughput to 30-100 wafers/hour. The disk spins at 1000-2000 rpm while translating linearly through the stationary beam.

## Variations and Alternatives

| Implanter Type | Energy Range | Beam Current | Throughput | Primary Use |
|---------------|-------------|-------------|------------|-------------|
| Medium-current | 10-500 keV | 0.1-5 mA | 10-30 wafers/hr | Threshold adjust, well implants, most production steps |
| High-current | 10-200 keV | 5-25 mA | 30-80 wafers/hr | Source/drain, high-dose implants (10¹⁵-10¹⁶ cm⁻²) |
| High-energy | 200 keV - 5 MeV | 0.01-1 mA | 5-20 wafers/hr | Buried layers, retrograde wells, SIMOX |
| Ion shower (no mass analysis) | 1-50 keV | 10-100 mA | 50-100 wafers/hr | Solar cell doping, display panel doping |

The medium-current implanter described in this article is the most versatile — it handles ~80% of all implant steps in a typical IC process flow. High-current and high-energy tools are specialized additions that become necessary only for specific process nodes. For bootstrapping, a medium-current implanter covers all essential implant steps.

## References

- [Ion Implantation](ion-implantation.md) — implant physics, dose/energy tables, annealing methods, process integration
- [Vacuum Technology](../vacuum/index.md) — vacuum systems for the beamline
- [Gas Handling](../gas-handling/index.md) — toxic gas handling and safety
- [Core Fab Processes](fab-processes.md) — how ion implantation fits into the IC fabrication flow
- [Advanced Processes](../vlsi-scaling/advanced-processes.md) — ion implantation for sub-250 nm nodes

---
*Part of the [Bootciv Tech Tree](../index.md) • [Photolithography & IC Fabrication](./index.md) • [All Domains](../index.md)*
