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

## Materials

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

## Construction Steps

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

## Expected Performance

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

## Weaknesses

- Extremely complex machine — combines particle accelerator, mass spectrometer, and precision wafer handling
- Requires toxic dopant gases (AsH₃, PH₃) with full safety infrastructure
- High-voltage systems (10-500 kV) require extensive safety interlocks and radiation shielding
- Ion bombardment damages the silicon crystal lattice — annealing (900-1100°C) is required after every implant step

## Safety

- **Toxic dopant gases**: AsH₃ (IDLH 3 ppm) and PH₃ (IDLH 50 ppm) are immediately dangerous to life. Gas cabinets with continuous electrochemical monitoring, automatic shut-off, and exhaust scrubbing are mandatory. Emergency protocol: evacuate, SCBA.
- **High voltage**: 10-500 kV DC is lethal. Interlocked enclosures, grounding sticks, and lock-out/tag-out. Never approach the acceleration column without verifying zero voltage with a grounded probe.
- **X-ray radiation**: Bremsstrahlung X-rays produced at energies >30 keV. Shield with lead or steel. Radiation monitoring badges for operators. Post radiation area warnings for MeV-class implanters.
- **Ionizing radiation dose limits**: Monitor and limit operator exposure per local radiation safety regulations.

## See Also

- [Ion Implantation](ion-implantation.md) — implant physics, dose/energy tables, annealing methods, process integration
- [Vacuum Technology](../vacuum/index.md) — vacuum systems for the beamline
- [Gas Handling](../gas-handling/index.md) — toxic gas handling and safety
- [Core Fab Processes](fab-processes.md) — how ion implantation fits into the IC fabrication flow
- [Advanced Processes](../vlsi-scaling/advanced-processes.md) — ion implantation for sub-250 nm nodes

[← Back to Photolithography](index.md)
