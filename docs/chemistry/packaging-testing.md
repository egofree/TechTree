# Semiconductor Packaging & Testing

> **Node ID**: chemistry.packaging-testing
> **Domain**: Chemistry
> **Timeline**: Years 40-70
> **Outputs**: packaged_ics, tested_ics, yield_data

### Cleanroom Consumables

**HEPA/ULPA filter media**:
- **HEPA (High Efficiency Particulate Air)**: Remove 99.97% of particles ≥0.3 μm. Construction: fine fiberglass mat (fiber diameter 0.5-2 μm), folded into accordion pleats (increases surface area 20-50x). Separator: corrugated aluminum or hot-melt bead between pleats. Frame: wood, metal, or plastic. Air velocity through filter: 0.025 m/s. Pressure drop: 250 Pa at rated flow.
- **ULPA (Ultra-Low Penetration Air)**: Remove 99.999% of particles ≥0.12 μm. Even finer glass fibers. Higher pressure drop. Used in most critical zones (lithography bays).
- **Filter production**: Glass fiber production (melt borosilicate glass, attenuate into fine fibers by flame attenuation or rotary spinning). Form mat on moving belt with vacuum forming. Bond with acrylic resin binder (5-10% by weight). Cut, pleat, frame, test (challenge with DOP or PAO aerosol particles, measure penetration with photometer).

**Cleanroom garments**:
- Woven polyester or polyester-blend fabric (lint-free, low particle shedding). Coverall design: full body coverage, elastic cuffs, zip front with flap covering zipper. Hood covering head and neck, integrated face mask or separate. Booties over street shoes, low-particulate soles. Boot cover or change into cleanroom-dedicated shoes.
- **Laundering**: Wash in ultra-pure water (18 MΩ·cm) with non-ionic detergent. Dry in HEPA-filtered dryer. Package in cleanroom-compatible bags. Typical garment life: 40-50 washes before particle shedding exceeds spec.

**Wipers**: Polyester knit (cleanest) or non-woven polypropylene. Sealed edges (laser-cut or ultrasonically sealed) to prevent fiber shedding. Used dry or wetted with IPA for surface cleaning. Tested for particle generation, absorbency, and extractable ions.

**Gloves**: Nitrile rubber (synthetic rubber — acrylonitrile + butadiene copolymer, from Polymers). 0.2-0.3 mm thickness for dexterity. Powder-free (powder contaminates cleanroom). Chlorinated inner surface for easy donning. Tested for pinholes (water-fill test), particle count, extractable ions. Change every 2 hours or when contaminated.

### Semiconductor Packaging

**Die preparation**:
- **Wafer backgrinding**: Grind back of completed wafer from ~725 μm to 200-350 μm (thinner die fit in thinner packages, better heat dissipation). Diamond-grit grinding wheel, water coolant. Multi-step: coarse grind (30 μm grit, ~600 μm/min removal) → fine grind (5 μm grit, ~100 μm/min) → polish (1 μm grit). Stress relief etch (brief HF dip to remove grinding damage).
- **Wafer mounting**: Adhere wafer to adhesive film (PVC or polyolefin with UV-release adhesive) on metal ring frame. Film holds wafer during dicing.
- **Die singulation (dicing)**: Diamond-impregnated blade (25-50 μm kerf) on high-speed spindle (20,000-40,000 RPM). Cut along scribe streets (pre-defined blank areas between die). Water coolant with surfactant. Feed rate 5-20 mm/second. Produce individual die ~5-20 mm on a side.

**Die attach**:
- **Eutectic bonding**: Au-Si eutectic (97.1% Au, 2.9% Si, mp 363°C). Place die on gold-plated package substrate. Heat to 400-425°C. Gold reacts with silicon die backside → liquid eutectic → bonds on cooling. Very reliable, high thermal conductivity.
- **Epoxy attachment** (more common, lower temperature): Silver-filled epoxy (80% Ag flakes by weight in epoxy resin — provides electrical and thermal conductivity). Dispense epoxy on substrate. Place die (pick-and-place tool — vacuum pickup needle, automated XY positioning). Cure at 150-175°C for 1-2 hours. Epoxy: bisphenol-A + hardener (amine or anhydride), loaded with silver flake 5-20 μm particle size.

**Wire bonding**:
- **Gold ball bonding**: 25 μm (1 mil) diameter gold wire. Form ball on wire tip by electric spark (flame-off). Bond ball to die pad by thermosonic bonding — apply heat (200-250°C), ultrasonic energy (60-120 kHz, 0.5-2 W), and force (0.3-0.8 N) simultaneously. Gold deforms and bonds to aluminum pad. Loop wire to lead frame pad. Bond second end by crescent (wedge) bond. Break wire, repeat. 10-20 bonds/second. Wire length 2-5 mm, loop height 0.2-0.5 mm.
- **Aluminum wedge bonding**: 25-50 μm Al wire. Ultrasonic energy only (room temperature). Wedge tool presses wire against pad. Lower cost but slower. Used for power devices (thicker wire carries more current).
- **Wire drawing for bonding wire**: Draw gold wire through successively smaller diamond dies. Start with 2 mm rod → draw through 20+ dies to 25 μm. Anneal between passes (heat to 500-600°C to restore ductility). Final tensile strength ~200-300 MPa, elongation 2-5%.

**Encapsulation**:
- **Transfer molding** (most common for plastic packages): Place die + wire-bonded lead frame in mold cavity. Inject molding compound (epoxy resin + silica filler 70-80% by weight + catalyst + mold release agent) at 175°C, 6-10 MPa pressure. Cure 2-5 minutes. Mold compound protects die from moisture, mechanical damage, contamination. Silica filler reduces thermal expansion coefficient (match silicon → less stress).
- **Ceramic hermetic packages** (high-reliability): Multi-layer ceramic (alumina) with tungsten metallization traces. Co-fired at 1500-1600°C. Seal lid to package with gold-tin eutectic solder (Au-20Sn, mp 280°C) in dry nitrogen atmosphere. Hermetic (gas-tight) — moisture cannot penetrate. For military, aerospace, high-temperature applications.

**Lead forming and finishing**:
- Trim and form lead frame leads (cut free from frame, bend to required shape — DIP, SOP, QFP lead shapes). Apply solder finish (dip in Sn-Pb or Sn-Ag-Cu solder bath at 230-260°C) for solderability. Mark package top with laser (part number, date code, lot code).

### Testing Infrastructure

**Wafer probing** (test before packaging):
- **Probe card**: Printed circuit board or ceramic substrate with precisely positioned probe needles (tungsten-rhenium or beryllium-copper, tip diameter 12-25 μm). Needles aligned to bond pad pattern. 50-500+ needles per card for complex ICs.
- **Probing station**: Precision XY stage positions wafer under probe card. Camera system for alignment. Z-axis actuator brings probe card into contact — needles scratch through oxide on aluminum pads. Contact resistance <1 Ω.
- **Tests**: DC parametric (Vt, Idsat, Ileakage, breakdown voltage) on test structures (PCMs — process control monitors, placed in scribe streets). Functional test on complete circuits. Speed/bin sort (test at multiple frequencies, bin by maximum operating speed).
- **Yield**: Map pass/fail across wafer → yield map. Typical early fab yields: 10-50%. Mature fab: 80-95%. Track yield by defect type, location, pattern → feedback to process engineering.

**Packaged part testing**:
- **Automated test equipment (ATE)**: Test head with socket for device under test (DUT). Pattern generator applies digital stimuli. Comparator checks outputs. Tests at speed (apply clock, verify timing margins). Temperature testing (hot/cold chuck, -55°C to +125°C for automotive/military grade).
- **Burn-in**: Subject devices to elevated temperature (125-150°C) and voltage (1.2-1.5× rated) for 24-168 hours. Accelerates early-life failures (infant mortality). Devices that survive burn-in have much lower field failure rate.
- **Final test**: Verify all specifications (speed, power, functionality at temperature extremes, I/O levels). Mark passing devices. Package, label, ship.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Chemistry | Bulk gas production (Cl₂, H₂, O₂, N₂), purification infrastructure |
| Vacuum & Optics | Vacuum technology for gas handling and distillation |
| Silicon | Gas supply for CZ growth (argon), CVD precursors (SiH₄, SiHCl₃) |
| Photolithography | Complete gas/consumable supply chain for fab, packaging, testing |
| Polymers | Epoxy encapsulation, fiberglass filters, nitrile gloves, cleanroom garment materials |

## Key Deliverables

- High-purity argon (99.999%+), nitrogen, hydrogen production via air separation and electrolysis
- Silane production with full pyrophoric safety infrastructure
- Dopant gas supply (PH₃, AsH₃, B₂H₆) with exhaust abatement and monitoring
- Etch gas production (CF₄, SF₆, Cl₂, F₂)
- Gas distribution system (electropolished SS tubing, MFCs, valves)
- HEPA/ULPA filter production
- Cleanroom consumable supply chain (garments, wipers, gloves)
- Die packaging line (dice, attach, wire bond, encapsulate, form leads)
- Wafer probing and parametric test capability
- Burn-in and final test infrastructure

### Cleanroom Consumables — Detailed Specifications

**Wipers**: Ultra-low lint wipers made from polyester (knitted, sealed-edge) for ISO Class 1-4 environments, or nonwoven polyester-cellulose blend for ISO Class 5-7. Critical parameters: particles released (ASTM E2090, <50 particles ≥0.5 µm per cm² for Class 10 wipers), non-volatile residue (NVR <1 mg per m²), ionic extractables (<1 ppm Na⁺, K⁺, Cl⁻). Pre-wetted wipers (with IPA/DI water blend) reduce particle generation during wiping. Cost: $0.50-3.00 per wiper.

**Gloves**: Natural rubber latex causes allergic reactions (protein sensitization) — largely replaced by nitrile (acrylonitrile-butadiene copolymer) in cleanrooms. Nitrile gloves: powder-free, chlorinated inner surface for donning. Thickness: 0.08-0.15 mm (thinner = better dexterity, thicker = better chemical resistance). Critical: ionic extractables, particle shedding, ESD properties (surface resistivity 10⁸-10¹¹ Ω/square for ESD-safe gloves). Change frequency: every 30 minutes to 2 hours depending on protocol. Typical cleanroom uses 20-40 pairs of gloves per operator per shift.

**Chemicals and solvents**: Ultra-pure grades for semiconductor use — "semiconductor grade" or "electronic grade" with specifications tighter than ACS reagent grade. Isopropanol (IPA): <1 ppb each metallic impurity (Fe, Cu, Na, K). Particle specification: <100 particles/mL ≥0.5 µm. Hydrogen peroxide (H₂O₂, 30%): <10 ppb total metallic impurities. Ammonium hydroxide (NH₄OH, 29%): similar metallic specs. These three plus DI water form the "RCA clean" solutions: SC-1 (NH₄OH:H₂O₂:H₂O = 1:1:5) for organic/particle removal; SC-2 (HCl:H₂O₂:H₂O = 1:1:6) for metallic contamination removal.

### Wafer Probing and Test

**Probe cards**: Interface between automated test equipment (ATE) and the wafer — an array of fine needles (tungsten-rhenium or cantilever-style) that make electrical contact to bond pads (50-100 µm aluminum pads) on each die. Modern probe cards use MEMS technology for fine-pitch probing (<50 µm pad pitch). Contact resistance must be <1 Ω per probe. Probe marks on pads must be small enough not to interfere with subsequent wire bonding — typically <25 µm diameter mark. Probe cards are the most expensive consumable in wafer test ($5,000-50,000 each, lifetime 100,000-1,000,000 touchdowns).

**Test flow**: (1) **Wafer sort** (probe test): Test every die on the wafer while still on the full wafer. Marks failed dies with ink dot (or electronic map). Determines yield — critical metric for fab economics. Typical test time: 1-10 seconds per die. Tests: DC parametrics (leakage, threshold voltage, breakdown voltage), basic functional test, sometimes at-speed test for critical paths. (2) **Packaged part test**: After packaging, full functional test at speed, AC timing, thermal testing (hot/cold). (3) **Burn-in**: Stress testing at elevated temperature (125-150°C) and voltage (1.2-1.5× nominal) for 24-168 hours to weed out infant mortality failures. Devices that pass burn-in have much lower field failure rate.

**Automated test equipment (ATE)**: Tester applies test patterns (input stimuli) and measures output responses. Timing accuracy: ±50-100 ps for high-speed digital. Parametric measurement units (PMUs) force voltage/measure current (or force current/measure voltage) with picoamp resolution. Test programs generated from design simulation vectors — "design for test" (DFT) structures like scan chains and built-in self-test (BIST) embedded in the chip during design enable comprehensive testing with reasonable test time.

### Reliability Testing

**Accelerated life testing**: Devices stressed beyond normal operating conditions to predict lifetime. Arrhenius model: failure rate doubles for every 10°C temperature increase. Typical acceleration: operating at 125°C for 1000 hours ≈ equivalent to 10+ years at 55°C use temperature.

**Key reliability tests**: (1) **Temperature cycling**: -65°C to +150°C, 500-1000 cycles. Detects: die attach voids, wire bond degradation, solder joint fatigue, package cracking. (2) **High temperature operating life (HTOL)**: 125°C at nominal voltage, 1000 hours. Detects: gate oxide breakdown, electromigration, hot carrier degradation. (3) **Temperature-humidity-bias (THB)**: 85°C/85%RH with applied bias, 1000 hours (the "85/85" test). Detects: corrosion, ionic contamination, moisture ingress. (4) **Electrostatic discharge (ESD)**: Human body model (HBM, 2000V), charged device model (CDM, 500V). (5) **Pressure cooker (PCT)**: 121°C, 100%RH, 2 atm, 96-168 hours — accelerated version of THB. (6) **Mechanical**: vibration (5-2000 Hz), shock (1500g, 0.5 ms), constant acceleration (30,000g).

**Failure analysis techniques**: (1) **Optical microscopy** and **SEM** for visual inspection. (2) **Acoustic microscopy** (C-SAM) for delamination and void detection — non-destructive. (3) **Decapsulation**: acid (fuming HNO₃ or H₂SO₄) or laser to remove package molding compound and expose die for analysis. (4) **FIB (focused ion beam)**: cross-section specific features for SEM inspection, or cut circuit traces for circuit edit. (5) **EMMI (emission microscopy)**: detects photon emission from defective transistors (hot carrier luminescence, avalanche breakdown). (6) **OBIRCH (optical beam induced resistance change)**: laser scanning detects thermal response changes — localizes shorts and leakage paths.

### Reliability Standards

**JEDEC** standards define test methods and acceptance criteria: JESD22 (test methods), JESD47 (stress-test-driven qualification), JESD74 (early life failure rate). **AEC-Q100** for automotive electronics: more stringent than JEDEC — temperature range -40 to +150°C (Grade 0), zero defects philosophy, additional tests (electromigration, soft error rate). **MIL-STD-883** for military/space: even more stringent — radiation testing (total ionizing dose, single event effects), outgassing testing (ASTM E595, <1% total mass loss, <0.1% collected volatile condensable materials for spacecraft materials).

## Safety Concerns

- **Dopant gases (PH₃, AsH₃, B₂H₆)**: Among the most toxic substances used industrially. Lethal at ppm concentrations. Continuous gas monitoring, automated shutdown, emergency evacuation procedures. Always use diluted cylinders. Never store large quantities. Exhaust gas abatement mandatory.
- **Silane**: Pyrophoric. Can auto-detonate without ignition source. Leak detection, inert gas purge protocols, no confined spaces.
- **Fluorine gas**: Reacts with almost everything. Severe chemical burns. Handle only in nickel/Monel equipment. Full PPE including face shield and HF-rated gloves (F₂ penetration produces HF on contact with moisture).
- **Gas cylinder safety**: Secure all cylinders upright (chain or strap to wall). Valve caps on when not in use. Never drag cylinders. Proper labeling (color-coded + text). Separate incompatible gases (flammables from oxidizers). Ventilated cylinder storage.

 ---

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*

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

## IC Package Types

**Plastic packages**: Over 95% of ICs use plastic (epoxy molding compound) packages. DIP (dual in-line package): 8-40 leads, 2.54 mm lead pitch, through-hole mounting. SOP (small outline package): 8-28 leads, 1.27 mm pitch, surface mount. QFP (quad flat package): 44-240 leads on all four sides, 0.5-0.8 mm pitch. QFN (quad flat no-lead): compact, leads on all four sides but flush with package body, 0.4-0.65 mm pitch. BGA (ball grid array): solder balls on the package bottom, 0.5-1.27 mm pitch, 100-2000+ connections. Higher pin count devices require finer pitch and area array configurations.

**Hermetic packages**: Ceramic or metal packages that are sealed against gas and moisture ingress. Used for high-reliability applications: military (MIL-STD-883), aerospace, medical implants, and high-temperature environments. CERDIP (ceramic dual in-line): ceramic body with glass-sealed ceramic lid. CQFP (ceramic quad flat pack): ceramic body with Kovar leads brazed to the side walls. Metal can packages (TO-5, TO-8): metal body with glass-sealed leads, welded or soldered lid. Hermeticity verified by fine leak test (helium mass spectrometry, leak rate <1×10⁻⁸ atm·cc/sec) and gross leak test (fluorocarbon bubble test).

**Die attach materials**: For plastic packages, silver-filled epoxy (80% Ag by weight, cured at 175°C for 1 hour) provides thermal conductivity 1.5-5.0 W/m·K and electrical conductivity to the lead frame. For high-power devices, eutectic Au-Si attach (mp 363°C) provides superior thermal conductivity (50+ W/m·K through the gold layer). For ceramic hermetic packages, gold-gold thermocompression bonding or silver-glass paste (fired at 350-400°C) provides reliable die attach with excellent thermal performance.

## Semiconductor Test Economics

**Test cost per die**: Wafer sort (probe test): $0.01-0.10 per die depending on complexity. Package test: $0.05-0.50 per die. Burn-in: $0.10-1.00 per die (depends on duration, 24-168 hours). For a complex SoC (system-on-chip), total test cost can be 5-10% of the die cost. Test cost increases with pin count, test speed, and test time. Design-for-test (DFT) structures embedded in the chip reduce test cost by enabling fast structural testing (scan chains test all flip-flops in a serial shift pattern) rather than slow functional testing.

**Yield learning curve**: New semiconductor products start at 10-30% yield and improve to 80-95% over 12-24 months through systematic defect reduction. Each 1% yield improvement on a 300 mm wafer producing 500 die at $50/die represents $250,000 annual revenue increase. This economic incentive drives aggressive yield improvement programs: failure analysis of every failed die, root cause identification, and process or design modification. The Pareto principle applies: 80% of yield loss comes from 20% of defect types, allowing focused improvement efforts.

## Semiconductor Grade Chemical Specifications

**Ultra-pure water (UPW)**: Used for all wafer rinsing steps. Resistivity: 18.2 MΩ·cm at 25°C (theoretical maximum for pure water). TOC (total organic carbon): <1 ppb. Particles: <1000 particles/L ≥0.05 μm. Dissolved oxygen: <10 ppb (oxygen in rinse water causes native oxide growth on silicon). Bacteria: <1 CFU/100 mL. Metals: <0.1 ppb each for Fe, Cu, Ni, Zn. UPW production: municipal water → multimedia filter → softener → activated carbon → RO (reverse osmosis) → EDI (electrodeionization) → UV sterilization → mixed bed ion exchange → 0.05 μm ultrafiltration → distribution loop (continuous recirculation at 1-3 m/s to prevent bacterial growth).
