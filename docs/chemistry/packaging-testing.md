# Analytical Testing & Pharmaceutical Packaging

> **Node ID**: chemistry.packaging-testing
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: `machine-tools`,
> [`machine-tools.joining.ultrasonic-bonding`](../machine-tools/joining.ultrasonic-bonding.md),
> [`photolithography.fab-processes`](../photolithography/fab-processes.md),
> [`polymers.thermosets`](../polymers/thermosets.md)
> **Timeline**: Years 10-30
> **Outputs**: tested_products, quality_data, stability_data
> **Critical**: Yes — analytical testing and pharmaceutical packaging ensure drug product safety, efficacy, and shelf life. Without validated test methods and robust packaging, medicines cannot be reliably delivered to patients.

Analytical testing and pharmaceutical packaging encompass the methods and infrastructure for verifying the identity, purity, potency, and stability of chemical and pharmaceutical products. This capability spans classical analytical chemistry (titration, gravimetry, spectrophotometry), modern instrumental methods (HPLC, AAS), statistical quality control, and the full suite of pharmaceutical packaging requirements from container selection through finished product release testing. Together, these ensure that manufactured products meet established specifications and remain safe and effective throughout their shelf life.

## Analytical Testing Methods

**Titration**: The workhorse quantitative method for acid-base, redox, and complexometric analysis. Acid-base titration uses a burette to deliver standard solution (e.g., 0.1 M NaOH) to an unknown sample with indicator (phenolphthalein, pH 8.2-10.0 endpoint) or pH meter detection. Precision ±0.1 mL on a 25 mL burette gives ±0.4% relative error. Redox titration: KMnO₄ or I₂ as titrant for reducing agents. Complexometric: EDTA (ethylenediaminetetraacetic acid) titration for Ca²⁺ and Mg²⁺ with Eriochrome Black T indicator. Karl Fischer titration for water content in chemicals: coulometric (for trace water, 10 μg to 10 mg) or volumetric (0.1-500 mg H₂O range).

**Gravimetric analysis**: Precipitate the analyte as an insoluble compound, filter, dry, and weigh on an analytical balance (±0.1 mg). Example: sulfate determination by BaCl₂ addition → BaSO₄ precipitate, filtered on ashless filter paper, ignited at 800°C, weighed. Precision ±0.1% for major components. Slow but accurate. Also used for moisture determination (dry sample at 105°C to constant weight) and ash content (ignite at 550°C to destroy organics).

**Colorimetric and spectrophotometric methods**: Based on Beer-Lambert law: A = εbc, where A = absorbance, ε = molar absorptivity (L/mol·cm), b = path length (cm), c = concentration (mol/L). Measure absorbance at specific wavelength using UV-visible spectrophotometer. Detection limits: 0.1-10 ppm for most analytes. Common applications: phosphate (molybdenum blue method, 880 nm), iron (phenanthroline method, 510 nm), silica (molybdosilicate method, 410 nm). Atomic absorption spectroscopy (AAS) for trace metals: detection limits 0.01-1 ppm.

## Quality Control and Statistical Methods

**Statistical process control (SPC)**: X̄-R (mean and range) charts track process parameters over time. Sample 3-5 units per batch, measure critical quality attribute, plot average (X̄) and range (R). Upper and lower control limits set at ±3σ from the process mean. A point outside control limits signals a special cause of variation requiring investigation. Western Electric rules detect trends: 7 consecutive points on one side of the center line, or 7 consecutive trending points, also signal loss of statistical control.

**Process capability index (Cp)**: Ratio of specification tolerance to process spread. Cp = (USL - LSL) / 6σ, where USL = upper spec limit, LSL = lower spec limit, σ = process standard deviation. Cp > 1.33 (process fits within specs with margin) is the minimum for capable processes. Cp = 1.0 means the process just fits specs (0.27% out-of-spec expected). Cp < 1.0 means the process is wider than specs, producing unacceptable defect rates.

**Sampling plans**: Acceptable Quality Level (AQL) 0.65-2.5% defines the maximum defect rate considered acceptable for incoming material inspection. Inspection level II (normal) per MIL-STD-105E (ISO 2859-1): for a lot of 1000 units, sample 80 units. Accept the lot if ≤5 defects found, reject if ≥6. Tightened inspection (Level III) increases sample size for suppliers with poor quality history. Reduced inspection (Level I) rewards consistent suppliers with smaller samples.

## Packaging Materials

**Glass containers**: Type I borosilicate glass (neutral glass, low alkaline release) for injection and biological products — withstands autoclaving at 121°C. Type III soda-lime glass for oral and topical products — less expensive, adequate chemical resistance for most drugs. Glass quality testing: hydrolytic resistance (powdered glass test, USP <660>), arsenic release (from glass decolorizers), internal surface delamination. Glass defects: stones (inclusions), seeds (gas bubbles), cords (refractive index variations) inspected by automated optical systems.

**Plastic packaging**: HDPE (high-density polyethylene): excellent moisture barrier, poor O₂ barrier, used for bottles and closures. PP (polypropylene): higher temperature resistance than HDPE (melting point 160°C vs 130°C), autoclavable, used for containers and syringes. PET (polyethylene terephthalate): excellent clarity, good O₂ and CO₂ barrier, used for beverage bottles and blister packs. O₂ permeability ranges: HDPE 40-150 cc·mm/m²·day·atm, PP 50-100, PET 5-10, EVOH (ethylene vinyl alcohol, high-barrier layer) 0.01-0.1. WVTR (water vapor transmission rate) at 38°C/90%RH: HDPE 0.3-0.5 g·mm/m²·day, PET 1-2.

**Aluminum foil**: 0.02-0.05 mm thickness for blister packs (push-through packaging for tablets and capsules). Aluminum provides essentially zero permeability to moisture, oxygen, and light when pinhole-free. Foil below 0.025 mm may have pinholes. Cold-formed blister packs use 0.045-0.060 mm aluminum foil formed into cavities by a die — provides superior barrier compared to thermoformed PVC blisters. Aluminum-aluminum laminates (foil + adhesive + PET film) provide tamper evidence and moisture protection.

## Stability Testing

ICH (International Council for Harmonisation) guidelines define standard conditions for drug substance and product stability testing:

**Long-term storage**: 25°C ± 2°C / 60% RH ± 5% RH. Test intervals: 0, 3, 6, 9, 12, 18, 24, 36 months. Establishes shelf life (expiry dating). The statistical analysis of degradation data determines the period during which the product remains within specification at the 95% confidence level.

**Accelerated storage**: 40°C ± 2°C / 75% RH ± 5% RH for 6 months. Predicts degradation pathways and provides early data for shelf-life estimation using the Arrhenius relationship. If the product passes accelerated testing (remains within specs), it is likely stable under long-term conditions. Failure at accelerated conditions does not necessarily mean failure at long-term, but triggers additional investigation.

**Intermediate conditions**: 30°C ± 2°C / 65% RH ± 5% RH, required if significant change occurs during the first 6 months at accelerated conditions. Tests at 0, 6, 9, 12 months.

**Photostability**: Expose to 1.2 million lux hours of visible light and 200 W·h/m² of UV (ICH Q1B). Determines if the product is photosensitive and requires light-protective packaging. The light source is a cool white fluorescent lamp (visible) plus a near-UV fluorescent lamp (320-400 nm). Samples compared to dark controls for color, assay, degradation products, and dissolution.

## Test Equipment and Calibration

**Analytical balances**: Readability 0.01 mg (0.1 mg for routine work). Calibration with certified reference weights (ASTM E617 Class 1 or 2) before each use. Draft shield to prevent air current interference. Located on vibration-isolated bench, away from HVAC vents. Daily verification with 2-3 reference weights spanning the working range. Environmental control: temperature ±1°C, relative humidity <70%.

**pH meter**: Glass electrode with Ag/AgCl reference. Calibration with two buffer solutions (pH 4.00 and 7.00 at 25°C, or pH 7.00 and 10.00 for alkaline measurements) before each use. Slope must be 95-105%. Electrode stored in 3M KCl solution when not in use. Electrode life: 6-24 months depending on usage and sample matrix (strongly acidic or alkaline samples shorten electrode life).

**Temperature and humidity chambers**: Stability chambers maintained at ICH conditions (25°C/60%RH, 30°C/65%RH, 40°C/75%RH) with continuous data logging. Temperature uniformity ±2°C throughout the chamber volume. Humidity ±5% RH. Calibrated with NIST-traceable temperature and humidity sensors. Backup power (generator or UPS) to prevent chamber excursions during power outages (a 2-hour excursion at 40°C can invalidate months of accelerated stability data).

**Dissolution testing**: USP Apparatus 2 (paddle method): 900 mL dissolution medium (simulated gastric fluid pH 1.2 or simulated intestinal fluid pH 6.8, maintained at 37.0±0.5°C), paddle rotation 50-100 RPM. Sample withdrawal at 15, 30, 45, 60 minutes through a filter (prevents undissolved particles from being assayed). Analyze by UV spectrophotometry or HPLC. Immediate-release tablets: ≥80% dissolved within 30 minutes (Q=80% at 30 min). Extended-release: specified dissolution profile over 8-24 hours.

## Packaging Line Testing

**Leak detection**: Container-closure integrity testing (CCIT) verifies that packaged products are hermetically sealed. Methods: (1) Dye ingress test: immerse packages in methylene blue dye solution under vacuum (250 mbar, 15 minutes). Inspect for dye penetration into the container. Sensitivity: detects 5-20 μm defects. (2) Vacuum decay: place package in a test chamber, apply vacuum, monitor pressure rise over 30-60 seconds. Pressure increase indicates a leak. Sensitivity: detects 5 μm defects. (3) High-voltage leak detection (for liquid-filled glass ampoules): apply 5-25 kV across the ampoule. Current passes through any crack or defect containing liquid. Detects 1-5 μm defects.

**Content uniformity**: Per USP <905>, test 10 dosage units individually for drug content. Acceptance: each unit contains 85-115% of label claim, and the relative standard deviation (RSD) is ≤6%. If one unit falls outside 85-115% but within 75-125%, test 20 more units. All 30 units must be 75-125%, and RSD of the 30 must be ≤7.8%. Content uniformity depends on adequate mixing during granulation and compression (for tablets) or filling (for capsules). Weight variation is a surrogate test for content uniformity when the drug substance is ≥25% of the tablet weight.

**Visual inspection**: Every manufactured unit inspected for defects. Automated visual inspection (machine vision systems with cameras and image analysis) at 100-300 units/minute. Defect categories: critical (cracked container, wrong cap color, foreign particle in solution — reject lot), major (missing or illegible label, scratched container — investigate and reject affected units), minor (minor cosmetic defect — trend and monitor). Manual visual inspection under polarized light at 2000-3000 lux for particulate matter in injectable solutions (USP <788> limits: ≤25 particles/mL ≥10 μm, ≤3 particles/mL ≥25 μm for small-volume parenterals).

## Finished Product Release Testing

**Identity testing**: Confirm the product contains the correct active ingredient. Methods: FTIR spectroscopy (Fourier transform infrared, compares sample spectrum to reference standard), Raman spectroscopy (non-destructive, can test through glass or plastic packaging), HPLC retention time matching, or colorimetric reaction (specific to the drug molecule). Every batch must pass identity testing before release.

**Assay (potency)**: Quantify the amount of active ingredient per dosage unit. HPLC (high-performance liquid chromatography) with UV detection is the most common method. Column: C18 reversed-phase, 150-250 mm × 4.6 mm ID, 5 μm particle size. Mobile phase: buffer + organic modifier (acetonitrile or methanol). Flow rate 1.0-2.0 mL/min. Detection: UV at λ_max of the drug compound. Results expressed as % of label claim. Acceptance: 90-110% for most drug products (tighter for narrow-therapeutic-index drugs).

**Impurity profiling**: Related substances (degradation products and process impurities) quantified by HPLC with gradient elution. Each known impurity has an individual specification (typically 0.1-0.5% of the active peak area). Total impurities: typically <2.0%. Unknown impurities: each <0.10%. ICH Q3B(R2) sets qualification thresholds for impurities above which toxicological assessment is required. Forced degradation studies (stress the drug with heat, humidity, acid, base, oxidation, and light) identify likely degradation products and validate that the analytical method can separate them from the main peak.

**Microbiological testing**: Total aerobic microbial count (TAMC): <100 CFU/g for oral solid dosage forms, <10³ CFU/g for oral liquids. Total yeast and mold count (TYMC): <10 CFU/g solids, <10² CFU/g liquids. Absence of specified organisms: E. coli, Salmonella, S. aureus, P. aeruginosa (USP <62>). Sterile products (injectables, ophthalmics): must pass sterility test (USP <71>, membrane filtration, incubate 14 days in thioglycollate and soybean-casein digest media). Bacterial endotoxin test (BET, USP <85>, Limulus amebocyte lysate method): limit for injectables is 5 EU/kg body weight per hour.

## See Also

- [Solvents](solvents.md) — solvents and reagents for analytical sample preparation
- [Semiconductor Packaging & Testing](../electronics/packaging-testing.md) — semiconductor die packaging, wire bonding, wafer probing, burn-in
- [Quality Control](../quality-control/metrology.md) — metrology and measurement standards
- [Thermoplastics](../polymers/thermoplastics.md) — polymer materials for pharmaceutical packaging
- [Glass Manufacturing](../glass/container-making.md) — glass container production for pharmaceutical use

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Chemistry](./index.md) • [All Domains](../../index.md)*
