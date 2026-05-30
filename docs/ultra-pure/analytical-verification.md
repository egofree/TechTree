# Analytical Verification: PPT-Level Contamination Detection

> **Node ID**: ultra-pure.analytical-verification
> **Domain**: [Ultra-Pure Materials](./index.md)
> **Dependencies**: [Measurement](../measurement/index.md), [Ultra-Pure Water](upw.md), [High-Purity Chemicals](high-purity-chemicals.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 40-80
> **Outputs**: contamination_data, purity_certification
> **Tags**: materials=[chemicals], capability=[measurement], era=semiconductor


You cannot produce what you cannot measure. Ultra-pure materials — 9N chemicals and 18.2 MΩ·cm water — require analytical instrumentation capable of detecting contaminants at parts-per-trillion (ppt) concentrations. One ppt corresponds to one gram of impurity in one million metric tons of material — roughly one grain of salt dissolved in an Olympic swimming pool.

The analytical verification capability is the enabling technology for the entire ultra-pure materials domain. Without ICP-MS (inductively coupled plasma mass spectrometry), TOC analyzers, and laser particle counters, there is no way to confirm that purification processes are working, that distribution systems are clean, or that chemicals meet semiconductor specifications.

## Detection Limits by Technique

| Technique | Detection Limit | Target Contaminants | Primary Use |
|-----------|----------------|--------------------|-------------|
| **ICP-MS** | 0.1-10 ppt | Metallic ions (Fe, Cu, Ni, Cr, Na, K, Ca, etc.) | Metal impurity quantification |
| **TOC analyzer** | 0.5-5 ppb (μg/L) | Dissolved organic carbon | Organic contamination |
| **Ion chromatography** | 0.01-0.1 ppb | Anions (Cl⁻, SO₄²⁻, NO₃⁻) and cations (Na⁺, K⁺, NH₄⁺) | Ionic impurity profiling |
| **Laser particle counter** | 0.05-0.2 μm | Suspended particles | Particle contamination |
| **Conductivity/resistivity** | 0.01 MΩ·cm resolution | Total ionic content | UPW quality monitoring |
| **DO meter** | 0.1-1 ppb | Dissolved oxygen | UPW DO monitoring |
| **UV-Vis spectrophotometry** | 1-10 ppb | Specific absorbing species | Silica, residual chemicals |
| **FTIR spectroscopy** | 10-100 ppb | Organic functional groups | Organic contamination ID |
| **Atomic absorption (AA)** | 0.1-10 ppb | Specific metals | Targeted metal analysis |
| **Gas chromatography (GC)** | 1-100 ppb | Volatile organic compounds | Solvent purity |

## ICP-MS (Inductively Coupled Plasma Mass Spectrometry)

ICP-MS is the workhorse instrument for trace metal analysis in ultra-pure materials. It can simultaneously quantify 60+ metallic elements at sub-ppt concentrations.

**Strengths**:
- Multi-element capability: 60+ metallic elements simultaneously in a single analysis
- Ultra-low detection limits: 0.01-10 ppt depending on element
- Wide dynamic range: 9 orders of magnitude (ppt to ppm) in a single run

**Weaknesses**:
- High instrument cost: $150,000-$500,000 per unit
- Sample contamination risk at ppt detection levels requires ISO Class 4 cleanroom preparation
- Spectral interferences from polyatomic ions require collision/reaction cell technology or mathematical correction

## ICP-MS Principle

1. **Sample introduction**: Liquid sample is nebulized into an aerosol by a pneumatic nebulizer in a spray chamber. Fine droplets (1-3 μm) enter the plasma torch.
2. **Ionization**: The aerosol enters an argon plasma at 6,000-10,000 K. At this temperature, all elements are atomized and ionized to +1 charge state. The plasma is sustained by RF induction coil at 27 or 40 MHz.
3. **Mass separation**: Ions are extracted from the plasma through a series of cones (sampler cone and skimmer cone) into a high-vacuum mass spectrometer. A quadrupole mass filter separates ions by mass-to-charge ratio (m/z). Each element has a unique m/z (or set of m/z values for isotopes).
4. **Detection**: Ions strike an electron multiplier detector. Counting rates are proportional to concentration. Detection limits: 0.01-10 ppt depending on element and matrix.

## Equipment

**RF generator**: 27.12 MHz or 40.68 MHz, 1.0-1.6 kW output. Solid-state RF generators are preferred over older tube-based designs for stability.

**Plasma torch**: Three concentric quartz tubes — outer (coolant argon, 12-15 L/min), intermediate (auxiliary argon, 0.5-1.5 L/min), and inner (sample aerosol carrier, 0.5-1.5 L/min). Torch alignment is critical for sensitivity and stability.

**Interface cones**: Nickel or platinum sampler cone (1.0 mm orifice) and skimmer cone (0.4-0.8 mm orifice). Platinum cones are required for HF-containing samples (nickel dissolves in HF). Cone condition directly affects sensitivity — replace when signal drops >30%.

**Mass spectrometer**: Quadrupole mass filter (most common) or magnetic sector (higher resolution for complex matrices). Scanning range: m/z 2-260 amu. Resolution: 0.3-1.0 amu (quadrupole), 0.01 amu (sector field).

**Detector**: Discrete dynode electron multiplier or Faraday cup. Electron multiplier for trace analysis (ppt), Faraday cup for higher concentrations (ppb-ppm).

**Vacuum system**: Two-stage: rotary vane pump (rough vacuum, ~1 Torr) + turbomolecular pump (high vacuum, 10⁻⁶ Torr). Interface region: ~2 Torr. Analyzer region: ~10⁻⁶ Torr.

## Sample Preparation

**Cleanroom environment**: All sample preparation must be performed in an ISO Class 4 (Class 10) cleanroom or better. Sample vials, pipettes, and reagents must be electronic-grade.

**Sample vials**: Pre-cleaned PFA vials. Leached with electronic-grade HNO₃ (1+1) for 24 hours, rinsed three times with UPW, dried in a Class 10 laminar flow hood.

**Acid digestion** (for solid samples): Dissolve in electronic-grade HNO₃ + HF in a PTFE microwave digestion vessel. Heat to 180°C under pressure. Cool, evaporate to near dryness, re-dissolve in 2% HNO₃ for analysis.

**Dilution**: Use electronic-grade 2% HNO₃ (sub-boiled) as diluent. Serial dilution to bring analyte concentrations into the calibration range.

**Blanks**: Method blanks (reagents only, no sample) run with every batch of 10 samples. Blank subtraction corrects for background contamination from reagents and vials.

## Calibration

**External calibration**: Prepare multi-element standard solutions from certified stock solutions (1,000 ppm single-element standards in 2-5% HNO₃). Serial dilution in electronic-grade 2% HNO₃ to create calibration curve points: 0 (blank), 0.1, 1, 10, 100 ppt (or appropriate range for elements of interest).

**Internal standardization**: Add internal standards (elements not present in samples, typically Sc, Ge, Rh, In, Lu, Bi) at 10-100 ppb to all samples, blanks, and standards. Corrects for:
- Instrument drift over time
- Matrix effects (sample viscosity, dissolved solids)
- Nebulizer efficiency variations
- Plasma instability

**Quality control samples**: Certified reference materials (CRMs) with known trace metal concentrations run at beginning, middle, and end of each batch. Recovery must be 85-115% for acceptance.

## SEMI Standard Method

SEMI C35 (Specifications and Guidelines for Hydrogen Fluoride) defines the required analytical methods and detection limits for electronic-grade HF. Similar SEMI standards exist for HCl (C36), HNO₃ (C37), H₂SO₄ (C38), H₂O₂ (C30), and NH₄OH (C39).

## TOC Analysis (Total Organic Carbon)

TOC analysis quantifies the total amount of dissolved organic carbon in UPW and electronic-grade chemicals. Organic contaminants leave carbonaceous residues on wafer surfaces, interfere with photoresist adhesion, and create nucleation sites for crystal defects.

**Strengths**:
- Direct measurement of total organic load regardless of individual species
- UV-persulfate method achieves 0.5-1 ppb TOC detection limit
- Continuous inline monitoring possible for UPW distribution systems

**Weaknesses**:
- Cannot identify specific organic compounds — only total carbon content
- UV lamp output degrades over 6-12 months affecting oxidation efficiency
- Combustion method at 680-800°C requires catalyst and higher sample volume

## UV-Persulfate Method (Standard for UPW)

1. **Acidification**: Add phosphoric acid to sample, lower pH to 2-3.
2. **Sparging**: Purge inorganic carbon (CO₂, HCO₃⁻, CO₃²⁻) with carrier gas (O₂ or N₂).
3. **UV oxidation**: Expose to 185 nm UV radiation in the presence of sodium persulfate (Na₂S₂O₈). Persulfate decomposes to sulfate radical (SO₄⁻·), a powerful oxidant. Organic carbon is oxidized to CO₂.
4. **Detection**: CO₂ is carried by gas stream to a non-dispersive infrared (NDIR) detector. CO₂ concentration is proportional to TOC.
5. **Calibration**: Potassium hydrogen phthalate (KHP) standard solutions at 0, 5, 10, 50, 100 ppb TOC.

## Combustion Method (for Chemicals)

For chemicals with higher organic content or complex matrices:
1. Inject sample into a combustion tube at 680-800°C with platinum catalyst.
2. Organic carbon oxidizes to CO₂.
3. NDIR detection of CO₂.

**Detection limit**: 1-5 ppb TOC (combustion), 0.5-1 ppb TOC (UV-persulfate).

## Ion Chromatography (IC)

Ion chromatography separates and quantifies dissolved ionic species — anions and cations — at sub-ppb concentrations. Essential for monitoring UPW quality and detecting trace ionic contamination in electronic-grade chemicals.

## Ion Chromatography Principle

1. **Eluent**: A dilute alkaline solution (Na₂CO₃/NaHCO₃ for anions, methanesulfonic acid for cations) flows through the system at 0.5-2.0 mL/min.
2. **Injection**: Sample loop (10-500 μL) injects sample into eluent stream.
3. **Separation**: Guard column + analytical column packed with ion-exchange resin. Ions separate based on their affinity for the resin — more strongly retained ions elute later.
4. **Suppression**: A suppressor membrane converts eluent ions to low-conductivity forms (e.g., Na⁺ → H⁺) while passing analyte ions. This dramatically improves signal-to-noise ratio.
5. **Detection**: Conductivity detector measures the conductivity of the eluent stream. Each ion produces a peak at a characteristic retention time. Peak area is proportional to concentration.

## Typical UPW IC Results

| Analyte | Detection Limit | SEMI F63 Limit | Typical UPW Value |
|---------|----------------|----------------|-------------------|
| Fluoride (F⁻) | 0.05 ppb | <0.5 ppb | <0.05 ppb |
| Chloride (Cl⁻) | 0.05 ppb | <0.1 ppb | <0.05 ppb |
| Nitrite (NO₂⁻) | 0.05 ppb | <0.1 ppb | <0.05 ppb |
| Bromide (Br⁻) | 0.05 ppb | <0.1 ppb | <0.05 ppb |
| Nitrate (NO₃⁻) | 0.05 ppb | <0.1 ppb | <0.05 ppb |
| Phosphate (PO₄³⁻) | 0.05 ppb | <0.1 ppb | <0.05 ppb |
| Sulfate (SO₄²⁻) | 0.05 ppb | <0.1 ppb | <0.05 ppb |
| Lithium (Li⁺) | 0.01 ppb | <0.05 ppb | <0.01 ppb |
| Sodium (Na⁺) | 0.01 ppb | <0.1 ppb | <0.01 ppb |
| Ammonium (NH₄⁺) | 0.01 ppb | <0.1 ppb | <0.01 ppb |
| Potassium (K⁺) | 0.01 ppb | <0.1 ppb | <0.01 ppb |
| Magnesium (Mg²⁺) | 0.01 ppb | <0.1 ppb | <0.01 ppb |
| Calcium (Ca²⁺) | 0.01 ppb | <0.1 ppb | <0.01 ppb |

## Laser Particle Counting

Particles are the leading cause of yield loss in semiconductor manufacturing. Laser particle counters detect and size individual particles suspended in liquids.

## Laser Particle Counting Principle

**Light scattering**: A laser diode (typically 650-780 nm) is focused into the sample stream through a sapphire window. When a particle passes through the beam, it scatters light in all directions. A photodetector collects scattered light at a fixed angle (typically 90°). The pulse amplitude is proportional to particle size.

**Light extinction** (for larger particles): The particle blocks a portion of the laser beam. The decrease in transmitted light is proportional to the particle cross-sectional area. Used for particles >1 μm.

## Configuration for UPW

- **Sample flow**: 10-100 mL/min through a precision flow cell
- **Sensitivity**: 0.05 μm (50 nm) for state-of-the-art instruments
- **Size channels**: 0.05, 0.1, 0.2, 0.5, 1.0, 2.0 μm (configurable)
- **Sampling rate**: Continuous or periodic (e.g., 1 minute every 15 minutes)

## Particle Sources and Control

| Source | Typical Particle Size | Control Method |
|--------|----------------------|----------------|
| Pump seal wear | 0.1-10 μm | Magnetic-drive pumps (no seals) |
| Filter fiber shedding | 0.05-1 μm | Integrity-test filters; use PES not fiberglass |
| Pipe corrosion | 0.1-50 μm | PFA piping; no metal contact |
| Bacterial growth | 0.2-5 μm | UV sterilization; hot water sanitization |
| Resin fines | 0.05-0.5 μm | Sub-micron filtration after ion exchange |
| Environmental dust | 0.5-100 μm | HEPA-filtered cleanroom environment |

## Dissolved Oxygen Measurement

Dissolved oxygen (DO) in UPW causes uncontrolled native oxide growth on silicon surfaces, which degrades gate oxide quality and uniformity.

## Measurement Methods

**Electrochemical (Clark-type)**: A gas-permeable membrane covers a gold cathode and silver anode in an electrolyte solution. Oxygen diffuses through the membrane and is reduced at the cathode. Current is proportional to oxygen concentration. Detection limit: ~1 ppb. Requires frequent membrane replacement and electrolyte replenishment.

**Optical (fluorescence quenching)**: A fluorescent dye embedded in a polymer film is excited by blue light. The presence of oxygen quenches the fluorescence — higher oxygen concentration means lower fluorescence intensity. Detection limit: ~0.1 ppb. No membrane, no electrolyte, longer sensor life. Preferred method for modern UPW systems.

## Resistivity Monitoring

Inline resistivity measurement is the primary continuous indicator of UPW ionic purity. Resistivity at 18.2 MΩ·cm at 25°C indicates total dissolved ionic solids below ~0.5 ppb.

## Instrument

**Toroidal (electrodeless) conductivity cell**: An oscillating magnetic field induces a current in the water flowing through the toroid. The induced current is proportional to water conductivity (inverse of resistivity). No electrodes contact the water — no polarization, no fouling, no drift from electrode contamination.

**Temperature compensation**: Resistivity is strongly temperature-dependent (18.2 MΩ·cm at 25°C but only ~12 MΩ·cm at 50°C). Inline temperature measurement with automatic compensation to 25°C reference is essential.


## Incoming Chemical Inspection

Every batch of electronic-grade chemical must be tested before release to the fab:

1. **ICP-MS**: 30+ metallic elements at ppt detection limits. All elements must be below SEMI specification limits.
2. **TOC**: <1 ppb for UPW-grade chemicals, <5 ppb for process chemicals.
3. **Particles**: <100/mL at ≥0.2 μm.
4. **Concentration**: Titration or density measurement to verify stated concentration ±0.5%.
5. **Certificate of Analysis (CoA)**: Manufacturer provides test results. Verify against SEMI specification.

## Continuous UPW Monitoring

| Parameter | Frequency | Method | Alert Threshold |
|-----------|-----------|--------|-----------------|
| Resistivity | Continuous (1 sec) | Toroidal cell | <18.0 MΩ·cm |
| TOC | Continuous (5 min) | UV-persulfate | >1 ppb |
| Particles | Continuous (1 min) | Laser counter | >100/mL (0.05 μm) |
| DO | Continuous (1 sec) | Optical sensor | >5 ppb |
| Flow | Continuous (1 sec) | Magnetic flow meter | ±10% |
| Temperature | Continuous (1 sec) | RTD | Outside 22-25°C |
| Bacteria | Daily | Membrane filtration | >1 CFU/100 mL |
| Silica | Weekly | Colorimetric | >0.5 ppb |
| Full IC panel | Monthly | Ion chromatography | Any anion/cation >0.1 ppb |
| Full ICP-MS panel | Monthly | ICP-MS | Any metal >1 ppt |

## Failure Response

**Resistivity excursion**: Isolate affected distribution loop. Switch to backup train. Investigate mixed-bed exhaustion or RO degradation. Do not resume UPW delivery until resistivity recovers to 18.2 MΩ·cm.

**TOC excursion**: Replace UV lamps. Flush distribution loop. Check for bacterial contamination. Sanitize with hot water (80°C for 2 hours) or hydrogen peroxide.

**Particle excursion**: Integrity-test all UF membranes. Check for distribution system breach. Flush and resample. Do not resume delivery until particle counts return to specification.

**Metallic contamination** (ICP-MS): Trace contamination to source — incoming chemical, resin leaching, pipe corrosion, or new component contamination. Quarantine affected lots. Replace or regenerate purification media.

## Safety & Hazards

- **ICP-MS plasma**: The inductively coupled plasma operates at 6000-10000 K. The torch assembly becomes extremely hot during operation. Allow 15-30 minutes cool-down after plasma shutdown before servicing. RF generator operates at 27-40 MHz — keep metallic objects clear of the RF coil. Argon gas supply requires proper ventilation — argon is an asphyxiant in confined spaces.
- **Strong acids**: Sample preparation involves concentrated HF, HNO₃, HCl, and H₂SO₄. Hydrofluoric acid (HF) is particularly dangerous — penetrates skin, binds calcium, causes deep tissue necrosis and potentially fatal hypocalcemia. Calcium gluconate gel must be available at every HF work station. Apply immediately to any HF skin contact, then seek medical attention. All acid handling under fume hood with face shield, acid-resistant gloves (neoprene for HF, nitrile for others), and apron.
- **UV radiation**: TOC analyzers use UV lamps (185 nm, 254 nm) for persulfate oxidation. Enclose UV sources. Interlock access panels. Replace lamps per schedule.
- **High-pressure components**: IC and TOC analyzers may operate at 5-15 MPa (50-150 bar) in sample introduction systems. Ensure all fittings are rated for operating pressure. Replace worn ferrules and fittings on schedule — a failed high-pressure fitting releases chemical spray.
- **Nanoparticle exposure**: Laser particle counters handle ultra-pure water samples that may contain nanoparticles. While sample volumes are small (<100 mL), avoid aerosol generation. Work in ventilated area.

## Cross-Domain Dependencies

- **[Measurement](../measurement/index.md)**: Precision metrology and calibration infrastructure. Temperature and pressure sensors.
- **[Ultra-Pure Water](upw.md)**: UPW is used for sample preparation, dilution, and instrument cooling. ICP-MS requires UPW for rinse cycles.
- **[High-Purity Chemicals](high-purity-chemicals.md)**: Electronic-grade acids (HNO₃, HCl) for sample preparation. Calibration standards.
- **[Chemistry](../chemistry/index.md)**: Bulk chemicals for reagent preparation. Ion exchange resins for IC columns.
- **[Optics](../optics/index.md)**: Lenses and optical components for particle counters and spectrophotometers.
- **[Gas Handling / Vacuum](../gas-handling/index.md)**: High-purity argon for ICP-MS plasma. Vacuum pumps for mass spectrometer.

## Limitations

- **Instrument cost**: ICP-MS: $150,000-$500,000 per instrument. TOC analyzer: $30,000-$100,000. Laser particle counter: $20,000-$60,000. A complete analytical laboratory requires $500,000-$2,000,000 of instrumentation.
- **Operator expertise**: ICP-MS operation requires extensive training. Spectral interferences, matrix effects, and contamination control are non-trivial. A skilled analytical chemist is essential.
- **Sample contamination risk**: At ppt detection limits, any contact with metal surfaces contaminates the sample. Sample preparation is the largest source of analytical error. All preparation must occur in cleanroom environments using electronic-grade reagents and PFA labware.
- **Throughput**: ICP-MS analysis of 30+ elements takes 2-5 minutes per sample. A full batch (10 samples + blanks + QC) takes 1-2 hours. Chemical production lines may need rapid turnaround that exceeds analytical capacity.
- **Instrument maintenance**: ICP-MS cones degrade with use (sampler cone lifetime: 50-200 hours of analysis depending on matrix). Torch replacement every 200-500 hours. Daily performance verification required.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| ICP-MS sensitivity drops >30% during analytical run | Sampler cone (1.0 mm orifice) clogged with matrix deposits — nickel cones degrade after 50–200 hours; platinum cones required for HF-containing samples | Replace sampler cone; clean with dilute HNO₃ if deposit is soluble; schedule cone replacement based on hours of analysis; monitor sensitivity drift with internal standard (Sc, Ge, Rh, In, Lu, Bi at 10–100 ppb) |
| ICP-MS blank readings show 50+ ppt iron contamination | Sample vials not adequately leached; or preparation occurred outside ISO Class 4 cleanroom — environmental dust introduces metals at ppt detection levels | Leach PFA vials with electronic-grade HNO₃ (1+1) for 24 hours, rinse 3× with UPW, dry in Class 10 laminar flow hood; move all preparation into ISO Class 4 cleanroom; verify operator is wearing cleanroom-appropriate gloves |
| TOC analyzer reads 5 ppb on UPW sample that should be <1 ppb | UV lamp (185 nm) output degraded after 6–12 months — oxidation efficiency drops, underreporting organic carbon initially, then reading spikes as incomplete oxidation creates artifacts | Replace UV lamp per manufacturer schedule; verify persulfate reagent (Na₂S₂O₈) is not expired; run calibration check with KHP standards at 0, 5, 10, 50, 100 ppb TOC |
| Ion chromatography baseline drift makes quantitation impossible | Suppressor membrane exhausted — ion-exchange capacity depleted; or eluent (Na₂CO₃/NaHCO₃) concentration drifted from preparation error | Regenerate or replace suppressor cartridge; prepare fresh eluent from electronic-grade reagents; verify eluent concentration by conductivity measurement before use; check pump for pulsation that causes baseline noise |
| Resistivity reads 17.0 MΩ·cm instead of 18.2 MΩ·cm on UPW system | Mixed-bed ion exchange resin exhausted — total dissolved ionic solids above ~0.5 ppb; or temperature compensation not correcting to 25°C reference (resistivity drops from 18.2 to ~12 MΩ·cm at 50°C) | Regenerate or replace mixed-bed ion exchange resin; verify inline temperature sensor and automatic compensation to 25°C reference; check for microbial contamination that produces ionic metabolic byproducts |
| Laser particle counter reports >100/mL particles at ≥0.05 μm on UPW that tested clean yesterday | UF membrane integrity failure — membrane tear allows sub-micron particles to pass; or distribution system has a breach introducing environmental contamination | Perform membrane integrity test (bubble point or diffusion test); flush distribution loop and resample; check for recent construction or maintenance activity near UPD distribution piping; inspect all O-ring seals in the sample path |
| CRM (Certified Reference Material) recovery only 75% — below 85–115% acceptance | Internal standard added at wrong concentration; or matrix effect from sample dissolved solids suppressing ionization in ICP-MS plasma | Verify internal standard (Sc, Ge, Rh, In, Lu, Bi) addition at correct 10–100 ppb concentration; dilute sample further to reduce matrix effects; check nebulizer efficiency — clogged nebulizer reduces transport to plasma |
| Dissolved oxygen reads 50 ppb in UPW (specification: <5 ppb) | Optical sensor (fluorescence quenching) membrane fouled or damaged; or UPW system membrane contactor degraded, allowing atmospheric O₂ ingress | Clean or replace DO sensor membrane; verify membrane contactor nitrogen purge is functioning; check for leaks on the UPW distribution loop — even a small fitting leak at low pressure allows O₂ diffusion into the high-purity water |
| High-pressure fitting in IC system leaks chemical spray at 10 MPa | Worn ferrule on compression fitting — ferrules rated for finite number of make/break cycles; fitting not re-tightened after thermal cycling | Replace worn ferrule with correct size and material; torque fitting to manufacturer specification; replace all high-pressure fittings on schedule — never exceed rated pressure of 50–150 bar (5–15 MPa) |
| ICP-MS quadrupole mass calibration drifts >0.5 amu from target | Mass calibration not updated after vacuum system maintenance; or RF generator (27/40 MHz) frequency instability from aging components | Perform mass calibration with tuning solution covering full m/z 2–260 range; verify turbomolecular pump maintains ~10⁻⁶ Torr in analyzer region; check RF generator stability — solid-state generators preferred over tube-based for drift performance |

## See Also

- [Ultra-Pure Water](upw.md) — 18.2 MΩ·cm water production
- [High-Purity Chemicals](high-purity-chemicals.md) — 9N+ chemical purification
- [Measurement](../measurement/index.md) — Precision metrology and standards
- [Chemistry / Acids](../chemistry/acids.md) — Bulk acid production
- [Optics](../optics/index.md) — Optical components for analytical instruments



[← Back to Ultra-Pure Materials](index.md)
