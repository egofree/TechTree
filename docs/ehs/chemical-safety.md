# Chemical Safety & Toxicology

> **Node ID**: ehs.chemical-safety
> **Domain**: [Environmental Health & Safety](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)
> **Timeline**: Years 30-70
> **Outputs**: chemical_hazard_protocols, tlv_databases, nfpa_ratings, exposure_control_plans

## Problem

Semiconductor fabrication uses the most hazardous chemicals in industrial production: hydrofluoric acid (HF) for silicon etching, silane (SiH₄) for silicon deposition, arsine (AsH₃) for N-type doping, phosphine (PH₃) for N-type doping, and dozens of corrosive, pyrophoric, and carcinogenic compounds. These chemicals demand safety protocols far beyond general industrial hygiene. A single silane leak can auto-ignite at concentrations above 1.4% in air; arsine exposure at 0.05 ppm for extended periods causes hemolytic anemia and renal failure. This document establishes the chemical safety knowledge base specific to semiconductor manufacturing environments.

## Semiconductor Process Chemicals

### Hydrofluoric Acid (HF)

**Properties**: Clear, colorless liquid. Pungent odor at higher concentrations. Molecular weight 20.01 g/mol. Boiling point 19.5°C (anhydrous). Miscible with water. Weak acid (pKₐ = 3.17) but extremely hazardous due to fluoride ion toxicity.

**Usage in semiconductor manufacturing**:
- Silicon dioxide (SiO₂) etching: SiO₂ + 6HF → H₂SiF₆ + 2H₂O
- Wafer cleaning (buffered oxide etch — BOE: NH₄F + HF mixture)
- Native oxide removal before deposition
- Glass etching and surface preparation

**Exposure Limits**:
| Standard | Value | Notes |
|----------|-------|-------|
| TLV-TWA (ACGIH) | 0.5 ppm (as F) | 8-hour time-weighted average |
| TLV-STEL (ACGIH) | Not established | Ceiling control recommended |
| PEL (OSHA) | 3 ppm (as F) | 8-hour TWA |
| REL (NIOSH) | 3 ppm (as F) | 8-hour TWA |
| IDLH (NIOSH) | 30 ppm | Immediately dangerous to life or health |
| ERPG-2 | 20 ppm | Emergency Response Planning Guideline |

**Health effects**: HF penetrates skin rapidly and dissociates, releasing fluoride ions that bind tissue calcium and magnesium. Deep tissue necrosis progresses for days after exposure. Systemic hypocalcemia causes cardiac arrhythmia and death. A skin exposure of 2.5% body surface area (palm-sized) with concentrated HF (>50%) can deliver a lethal systemic dose. Even dilute HF (≤10%) causes delayed but severe burns that may not become painful for 12-24 hours.

**NFPA 704 Diamond**: Health 4 (deadly), Flammability 0 (will not burn), Instability 1 (normally stable), Special: COR (corrosive)

**First aid**: Immediate flushing with water for 15+ minutes. Apply calcium gluconate gel (2.5%) generously to affected area and massage in continuously. For eye exposure, flush 30+ minutes and apply calcium gluconate drops. Seek emergency medical care for any exposure larger than a small spot.

### Silane (SiH₄)

**Properties**: Colorless gas with repulsive odor (may not be detectable at low concentrations). Molecular weight 32.12 g/mol. Boiling point -112°C. Density 1.15× air (heavier than air, accumulates at floor level). Autoignition temperature varies: as low as 21°C for concentrated releases; typically 500°C for diluted mixtures. Flammable range: 1.4% to 96% in air.

**Usage in semiconductor manufacturing**:
- Polycrystalline silicon deposition (LPCVD): SiH₄ → Si + 2H₂ at 580-650°C
- Silicon nitride deposition (PECVD/LPCVD): 3SiH₄ + 4NH₃ → Si₃N₄ + 12H₂
- Amorphous silicon for thin-film transistors (TFT) and solar cells
- Silicon dioxide deposition: SiH₄ + O₂ → SiO₂ + 2H₂

**Exposure Limits**:
| Standard | Value | Notes |
|----------|-------|-------|
| TLV-TWA (ACGIH) | 5 ppm | 8-hour time-weighted average |
| PEL (OSHA) | 5 ppm | 8-hour TWA |
| REL (NIOSH) | 5 ppm | 8-hour TWA |
| IDLH (NIOSH) | Not established | Withdrawn due to pyrophoric nature |
| ERPG-2 | 5 ppm | Below detectable odor threshold |

**Health effects**: Respiratory irritant at low concentrations. At high concentrations, causes headache, nausea, and respiratory distress. Primary hazard is pyrophoric: silane can spontaneously ignite on release, producing silicon dioxide fume and intense heat. Burns in air: SiH₄ + 2O₂ → SiO₂ + 2H₂O. Explosion risk in confined spaces where gas can accumulate above the lower flammable limit (1.4%). Silane fires produce fine SiO₂ particulate (respiratory hazard).

**NFPA 704 Diamond**: Health 1 (slight), Flammability 4 (extremely flammable), Instability 3 (shock/heat sensitive), Special: PYRO (pyrophoric)

**Special precautions**: Gas cabinets with continuous exhaust ventilation (minimum 200 ft³/min, typically 250-400 CFM per cabinet). Exhaust monitoring with silane-specific sensors (infrared or thermal conductivity detectors). Automatic shutoff valves triggered by gas detection or seismic sensors. Purge panels with inert gas (N₂) for cylinder change procedures. Maximum cylinder size indoors: typically restricted to 45 kg for production use.

### Arsine (AsH₃)

**Properties**: Colorless gas with mild garlic-like odor (detectable at 0.5 ppm, but odor not reliable — olfactory fatigue occurs rapidly). Molecular weight 77.95 g/mol. Boiling point -62.5°C. Density 2.7× air (heavier than air). Decomposes on heating above 300°C, releasing arsenic.

**Usage in semiconductor manufacturing**:
- N-type ion implantation (arsenic dopant source)
- Gallium arsenide (GaAs) epitaxial growth: AsH₃ + Ga(CH₃)₃ → GaAs + 3CH₄
- Solar cell doping
- Epitaxial silicon doping

**Exposure Limits**:
| Standard | Value | Notes |
|----------|-------|-------|
| TLV-TWA (ACGIH) | 0.005 ppm (5 ppb) | Extremely low — among the most toxic industrial gases |
| PEL (OSHA) | 0.05 ppm (50 ppb) | 8-hour TWA |
| REL (NIOSH) | 0.002 ppm (2 ppb) | Ceiling (not to be exceeded) |
| IDLH (NIOSH) | 3 ppm | Immediately dangerous to life or health |
| ERPG-2 | 0.5 ppm | Emergency Response Planning Guideline |

**Health effects**: Potent hemolytic agent — destroys red blood cells. Symptoms delayed 2-24 hours post-exposure. Initial symptoms: headache, malaise, weakness, nausea, abdominal pain. Progressive hemolysis causes hemoglobinuria (dark/red urine), jaundice, and renal failure from hemoglobin precipitation in renal tubules. Severe exposures cause multi-organ failure. Fatal dose: 0.5 ppm for 30 minutes can be lethal. Chronic low-level exposure causes peripheral neuropathy, anemia, and skin pigmentation changes.

**NFPA 704 Diamond**: Health 4 (deadly), Flammability 4 (extremely flammable), Instability 2 (violent chemical change at elevated temperatures), Special: None

**Special precautions**: Use only in gas cabinets with dedicated exhaust (scrubbed — see [Ventilation](ventilation-exhaust.md)). Continuous gas monitoring with electrochemical or infrared sensors capable of detecting at 1 ppb resolution. Dual-sensor monitoring (redundancy) for life-safety applications. Minimum detection alarm at 50% of PEL (0.025 ppm). Cylinder valves must be fail-closed (normally closed solenoid valves). Stainless steel tubing (316L) with VCR or welded fittings throughout. No brass or copper fittings (forms toxic arsine-copper complexes).

### Phosphine (PH₃)

**Properties**: Colorless gas with decaying fish or garlic odor (detectable at 0.02-0.3 ppm, highly variable sensitivity). Molecular weight 34.00 g/mol. Boiling point -87.7°C. Density 1.2× air (slightly heavier than air). Flammable range: 1.6% to 98% in air. Autoignition temperature: 38°C for pure gas (may ignite spontaneously at room temperature if impurities present).

**Usage in semiconductor manufacturing**:
- N-type ion implantation (phosphorus dopant source)
- InGaAsP epitaxial growth for photonics
- Phosphosilicate glass (PSG) deposition: SiH₄ + PH₃ + O₂ → PSG
- Phosphorus-doped silicon epitaxy

**Exposure Limits**:
| Standard | Value | Notes |
|----------|-------|-------|
| TLV-TWA (ACGIH) | 0.3 ppm | 8-hour time-weighted average |
| TLV-STEL (ACGIH) | 1 ppm | Short-term exposure limit (15 min) |
| PEL (OSHA) | 0.3 ppm | 8-hour TWA |
| REL (NIOSH) | 0.3 ppm | 8-hour TWA |
| IDLH (NIOSH) | 50 ppm | Immediately dangerous to life or health |
| ERPG-2 | 0.5 ppm | Emergency Response Planning Guideline |

**Health effects**: Respiratory irritant and systemic toxin. Causes pulmonary edema at moderate concentrations. Targets central nervous system, liver, and kidneys. Early symptoms: nausea, vomiting, abdominal pain, headache, dizziness. Delayed onset (up to 72 hours): pulmonary edema, cardiac arrhythmia, liver necrosis, renal failure. Chronic exposure causes bone and tooth damage (phosphorus necrosis of the jaw — "phossy jaw"). Fatal concentration: 400-600 ppm for 30-60 minutes.

**NFPA 704 Diamond**: Health 4 (deadly), Flammability 4 (extremely flammable), Instability 2 (violent chemical change at elevated temperatures), Special: None

### Hydrogen Chloride (HCl)

**Properties**: Colorless to slightly yellow gas with pungent, irritating odor. Molecular weight 36.46 g/mol. Boiling point -85°C. Highly soluble in water forming hydrochloric acid. Density 1.3× air.

**Usage in semiconductor manufacturing**:
- Wafer cleaning and surface preparation
- Native oxide removal
- Chlorosilane production intermediate
- Etching processes (with Cl₂)

**Exposure Limits**:
| Standard | Value | Notes |
|----------|-------|-------|
| TLV-TWA (ACGIH) | Not established (withdrawn) | Ceiling limit recommended |
| TLV-Ceiling (ACGIH) | 2 ppm | Not to be exceeded |
| PEL (OSHA) | 5 ppm | Ceiling |
| REL (NIOSH) | 5 ppm | Ceiling |
| IDLH (NIOSH) | 50 ppm | Immediately dangerous to life or health |

**NFPA 704 Diamond**: Health 3 (serious), Flammability 0, Instability 1, Special: COR

### Ammonia (NH₃)

**Properties**: Colorless gas with sharp, suffocating odor. Molecular weight 17.03 g/mol. Boiling point -33.3°C. Density 0.6× air (lighter than air, rises). Highly soluble in water forming ammonium hydroxide (NH₄OH).

**Usage in semiconductor manufacturing**:
- Silicon nitride deposition: 3SiH₄ + 4NH₃ → Si₃N₄ + 12H₂
- Cleaning solutions (SC-1: NH₄OH + H₂O₂ + H₂O)
- Chemical mechanical polishing (CMP) slurry pH adjustment
- Selective epitaxial growth processes

**Exposure Limits**:
| Standard | Value | Notes |
|----------|-------|-------|
| TLV-TWA (ACGIH) | 25 ppm | 8-hour TWA |
| TLV-STEL (ACGIH) | 35 ppm | 15-minute STEL |
| PEL (OSHA) | 50 ppm | 8-hour TWA |
| REL (NIOSH) | 25 ppm | 8-hour TWA |
| IDLH (NIOSH) | 300 ppm | Immediately dangerous to life or health |

**NFPA 704 Diamond**: Health 3 (serious), Flammability 1 (slight), Instability 0, Special: None

## Additional Semiconductor Chemicals

### Sulfuric Acid (H₂SO₄) — Piranha Clean

Piranha solution (H₂SO₄ + H₂O₂, typically 3:1 ratio at 120-150°C) is used for organic residue removal. Extremely exothermic on mixing; must always add peroxide to acid (never reverse). Temperature can exceed 200°C. Carbonized organic material releases gas, causing foaming. Can detonate if mixed with significant organic quantities. Allow to cool before disposal. Store in compatible containers only (glass, Teflon, HDPE — never sealed tightly as it continuously evolves O₂).

**Exposure Limits**: TLV-TWA 0.2 mg/m³ (thoracic fraction as sulfuric acid mist). IDLH: 15 mg/m³.
**NFPA 704**: Health 3, Flammability 0, Instability 2 (strong oxidizer), Special: COR

### Hydrogen Peroxide (H₂O₂)

Used in SC-1 (NH₄OH:H₂O₂:H₂O = 1:1:5) and SC-2 (HCl:H₂O₂:H₂O = 1:1:6) RCA cleaning sequences. Concentrated grades (30-50%) are strong oxidizers that cause severe skin burns and ignite organic materials. Store in vented containers (decomposes to O₂ + H₂O, pressure builds in sealed vessels). Never return unused peroxide to the stock container (contamination causes rapid decomposition).

**Exposure Limits**: TLV-TWA 1 ppm. IDLH: 75 ppm.
**NFPA 704**: Health 3, Flammability 0, Instability 3 (strong oxidizer), Special: OXY

### Nitrogen Trifluoride (NF₃)

Plasma chamber cleaning gas. Decomposes in plasma to atomic fluorine (cleaning agent) and nitrogen. Gas phase is relatively low toxicity (TLV-TWA 10 ppm), but decomposition products include HF. Primary environmental concern: extremely potent greenhouse gas (GWP 17,200× CO₂ over 100 years). Abatement is mandatory — thermal or plasma destruction to achieve >99% destruction removal efficiency (DRE).

**Exposure Limits**: TLV-TWA 10 ppm.
**NFPA 704**: Health 3, Flammability 0, Instability 0 (stable gas)

### Perfluorocarbons (CF₄, C₂F₆, C₃F₈, C₄F₈)

Etching gases and chamber cleaning agents. Low acute toxicity but extremely potent greenhouse gases (CF₄ GWP: 7,390× CO₂; C₂F₆ GWP: 12,200× CO₂). Abatement required by environmental regulation. Thermal destruction at >1,200°C converts to HF (scrub) and CO₂. Point-of-use abatement systems achieve 90-99% DRE.

## NFPA 704 Diamond Rating System

The NFPA "fire diamond" provides at-a-glance hazard communication:

**Health (Blue, 0-4)**:
- 0: No hazard beyond that of ordinary combustible materials
- 1: Exposure would cause irritation with only minor residual injury
- 2: Intense or continued exposure could cause temporary incapacitation or residual injury
- 3: Short exposure could cause serious temporary or moderate residual injury
- 4: Very short exposure could cause death or major residual injury

**Flammability (Red, 0-4)**:
- 0: Will not burn
- 1: Must be preheated before ignition (flash point >93°C)
- 2: Must be moderately heated (flash point 38-93°C)
- 3: Can be ignited at ambient temperature (flash point <38°C)
- 4: Will rapidly vaporize at ambient conditions and burn readily (flash point <23°C) or pyrophoric

**Instability (Yellow, 0-4)**:
- 0: Normally stable even under fire conditions
- 1: Normally stable but may become unstable at elevated temperatures
- 2: Violent chemical change at elevated temperatures or pressures
- 3: Capable of detonation or explosive decomposition but requires a strong initiating source
- 4: Readily capable of detonation or explosive decomposition at normal temperatures

**Special Notices (White)**:
- OXY: Oxidizer
- COR: Corrosive
- PYRO: Pyrophoric
- W: Reacts with water (no water for fire suppression)
- RAD: Radioactive

## Chemical Compatibility Matrix

Semiconductor chemicals must be stored and handled with full awareness of incompatibilities:

| Chemical | Incompatible With | Hazard of Mixing |
|----------|-------------------|------------------|
| HF | Glass, concrete, cast iron, strong bases (exothermic) | Violent reaction with bases; attacks glass |
| Silane | Oxidizers, halogens, air (above LEL) | Spontaneous ignition; explosive combustion |
| Arsine | Oxidizers, acids, copper/brass alloys | Toxic decomposition; flammable mixtures |
| Phosphine | Oxidizers, halogens, strong acids | Spontaneous ignition; toxic phosphorus oxides |
| H₂O₂ | Organic materials, metals, reducing agents | Violent oxidation; fire/explosion |
| H₂SO₄ | Water (reverse addition), organics, bases | Violent exothermic; spattering; charring |
| Piranha | Organic solvents, photoresist (bulk) | Detonation risk; violent oxidation |
| NH₃ | Strong acids, halogens, oxidizers | Violent reaction; toxic fumes |

## Gas Classification by Hazard

Semiconductor process gases are classified into categories for handling and facility design:

**Pyrophoric gases** (ignite spontaneously in air at ≤54.4°C):
- Silane (SiH₄), dichlorosilane (SiH₂Cl₂), trichlorosilane (SiHCl₃), phosphine (PH₃)

**Toxic/Corrosive gases**:
- Arsine (AsH₃), phosphine (PH₃), hydrogen fluoride (HF), hydrogen chloride (HCl), chlorine (Cl₂), hydrogen bromide (HBr), boron trichloride (BCl₃)

**Corrosive gases**:
- Hydrogen fluoride (HF), hydrogen chloride (HCl), chlorine (Cl₂), boron trichloride (BCl₃), tungsten hexafluoride (WF₆)

**Flammable gases**:
- Hydrogen (H₂), silane (SiH₄), phosphine (PH₃), ammonia (NH₃) at high concentrations

**Inert gases** (simple asphyxiants in confined spaces):
- Nitrogen (N₂), argon (Ar), helium (He)

**Oxidizer gases**:
- Oxygen (O₂), nitrous oxide (N₂O), nitrogen trifluoride (NF₃)

## Safety Data Sheet (SDS) Requirements

Every chemical in the fab must have an accessible SDS (formerly MSDS) covering 16 sections per GHS (Globally Harmonized System):

1. Identification (product name, manufacturer, emergency phone)
2. Hazard identification (GHS pictograms, signal word, hazard statements)
3. Composition/information on ingredients
4. First-aid measures (inhalation, skin, eye, ingestion — specific procedures per route)
5. Fire-fighting measures (extinguishing media, specific hazards, protective equipment)
6. Accidental release measures (personal precautions, containment, cleanup)
7. Handling and storage (safe handling practices, storage conditions, incompatibilities)
8. Exposure controls/personal protection (PELs, TLVs, PPE requirements)
9. Physical and chemical properties (appearance, odor, boiling point, vapor pressure, solubility)
10. Stability and reactivity (conditions to avoid, incompatible materials, decomposition products)
11. Toxicological information (acute/chronic toxicity, target organs, carcinogenicity)
12. Ecological information (aquatic toxicity, bioaccumulation, persistence)
13. Disposal considerations (waste treatment methods, regulatory requirements)
14. Transport information (UN number, proper shipping name, hazard class)
15. Regulatory information (applicable regulations, reporting requirements)
16. Other information (revision date, abbreviations)

## Exposure Monitoring Protocols

### Continuous Gas Monitoring

Semiconductor fabs use fixed-point gas detection systems for hydride gases (AsH₃, PH₃) and other toxic gases:

**Sensor types**:
- Electrochemical cells: Detect specific gases (AsH₃, PH₃, Cl₂, HCl, H₂S) at ppb levels. Response time 30-90 seconds. Sensor life 1-3 years. Cross-sensitivity must be characterized.
- Infrared (IR) sensors: For silane, CO₂, hydrocarbons. Non-consuming measurement. Longer sensor life. More expensive.
- Thermal conductivity: For binary gas mixtures (H₂ in air). Broad range detection.
- Catalytic bead: For combustible gases. Measures %LEL.

**Alarm thresholds** (typical semiconductor fab standard):
- Low alarm: 50% of TLV-TWA or PEL (whichever is lower)
- High alarm: TLV-TWA or PEL (whichever is lower)
- Critical alarm (evacuation): 2× TLV or 50% of IDLH (whichever is lower)

**Monitoring points**: Gas cabinets, valve manifold boxes (VMB), bulk gas delivery areas, process tool exhaust, fab return air plenums, utility corridors. Sensors mounted at breathing height (1.5 m) for gases heavier than air, and at ceiling level for lighter-than-air gases (H₂, NH₃), and both for gases near air density (silane).

### Personal Exposure Assessment

Routine industrial hygiene surveys assess worker exposure to chemical, physical, and biological agents:

**Air sampling strategy**: Follow NIOSH Occupational Exposure Sampling Strategy Manual. Full-shift personal samples (minimum 6 hours of an 8-hour shift) for TWA compliance. Short-term (15-minute) samples for STEL assessment. Worst-case sampling (highest-exposure tasks) first; if results are <50% of PEL, no further sampling required for that job category. If 50-100% of PEL, repeat sampling to confirm. If >PEL, implement controls and resample.

**Sampling methods by chemical**:
- HF: Treated cellulose filter (impregnated with sodium carbonate) in cassette, flow rate 2 L/min. Analyze by ion chromatography.
- Arsine/phosphine: Impinger solution (hydrogen peroxide/silver nitrate for arsine, mercuric chloride for phosphine) or solid sorbent tubes. Analyze by ICP-MS or colorimetric methods.
- Silane: Thermal desorption tubes analyzed by GC-FID, or direct-reading infrared analyzer.
- Acids (H₂SO₄, HCl, HNO₃): Treated filters or impingers with subsequent ion chromatography analysis.
- Solvents: Charcoal sorbent tubes, 50-200 mL/min flow. Desorb with CS₂, analyze by GC-FID.

## See Also

- [Ventilation & Exhaust Systems](ventilation-exhaust.md) — Gas cabinets, scrubbers, and abatement systems
- [Personal Protective Equipment](ppe.md) — PPE selection for chemical handling
- [Emergency Response](emergency-response.md) — Chemical exposure first aid and spill response
- [Waste Management](waste-management.md) — Acid and solvent waste handling
- [Occupational Health](../health/occupational-health.md) — General industrial hygiene and exposure monitoring
- [Acids & Bases](../chemistry/acids-bases.md) — Acid and alkali production
- [Hydrogen & Silane](../chemistry/hydrogen-silane.md) — Silane production processes
- [Semiconductor Chemicals](../chemistry/semiconductor-chemicals.md) — Chemical supply chain for semiconductor manufacturing

---

*Part of the [Bootciv Tech Tree](../index.md) · [EHS](./index.md) · [All Domains](../index.md)*
