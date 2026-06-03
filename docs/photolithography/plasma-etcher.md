# Plasma Etcher

> **Node ID**: photolithography.plasma-etcher
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`vacuum.chambers`](../vacuum/chambers.md), [`vacuum.pumps`](../vacuum/pumps.md), [`gas-handling`](../gas-handling/index.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`photolithography.fab-processes`](fab-processes.md), [`vlsi-scaling.advanced-processes`](../vlsi-scaling/advanced-processes.md)
> **Timeline**: Years 40-55
> **Outputs**: etched_patterns, via_holes, trench_structures, patterned_films
> **Critical**: Yes — plasma etching is the primary method for pattern transfer from photoresist to underlying films in semiconductor fabrication; wet etching cannot achieve the anisotropic profiles required for sub-micron features

This article covers the construction of reactive ion etching (RIE) and inductively coupled plasma (ICP) etching systems. For etching chemistry, process parameters, and etch selectivity data, see [Core Fab Processes](fab-processes.md).

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

## Materials

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

## Construction Steps

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

## Expected Performance

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

## See Also

- [Core Fab Processes](fab-processes.md) — etching chemistry, process integration, wet vs. dry etching comparison
- [Vacuum Chamber](../vacuum/vacuum-chamber.md) — chamber construction
- [Gas Handling](../gas-handling/index.md) — toxic gas handling, gas cabinet safety
- [Sputtering System](sputtering-system.md) — complementary thin-film deposition
- [CVD Reactor](cvd-reactor.md) — alternative deposition technology

[← Back to Photolithography](index.md)
