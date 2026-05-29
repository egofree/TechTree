# Toxicology

> **Node ID**: ehs.toxicology
> **Domain**: [Environmental Health & Safety](./index.md)
> **Dependencies**: [`ehs.chemical-safety`](chemical-safety.md), [`health.pharmacology`](../health/pharmacology.md), [`chemistry`](../chemistry/index.md)
> **Enables**: [`health.occupational-health`](../health/occupational-health.md), [`ehs.emergency-response`](emergency-response.md)
> **Timeline**: Years 20-100+
> **Outputs**: toxic_substance_databases, exposure_limits, antidote_protocols, material_safety_data
> **Critical**: No — enhances safety but chemical handling can proceed at basic level without formal toxicology

## Overview

Toxicology covers the identification, quantification, and management of toxic substances encountered in industrial, pharmaceutical, and environmental contexts. This capability extends [chemical-safety](chemical-safety.md) — which focuses on semiconductor process chemicals — into general toxicology for the full range of industrial chemicals a bootstrap civilization will encounter: smelting fumes, acid mists, organic solvents, heavy metals, and plant/animal toxins.

The core principle of toxicology (Paracelsus, 1538): "The dose makes the poison." Every substance is toxic at sufficient dose; the task is to define safe exposure limits and manage risks accordingly. For industrial chemicals, this means establishing TLV-TWA (Threshold Limit Value — Time Weighted Average) concentrations that workers can breathe for 8 hours per day, 40 hours per week, over a working lifetime without adverse effect. For acute exposures, it means knowing IDLH (Immediately Dangerous to Life or Health) concentrations and having antidotes available.

## Decision Framework: Exposure Assessment Method

| Scenario | Recommended Method | Accuracy | Cost | Turnaround |
|----------|-------------------|----------|------|------------|
| Quick check during operation | Colorimetric detector tube | ±25% | $5-15 per tube | Immediate (2-5 min) |
| Compliance TWA measurement | Personal air sampling pump + sorbent tube | ±10% | $50-150 per sample | Days (lab analysis) |
| Real-time area monitoring | Direct-reading electronic monitor | ±5-10% | $500-5,000 instrument | Continuous |
| Chemical identification (unknown) | GC-MS or FTIR analysis | ±1-5% | $200-500 per sample | Hours to days |
| Biological exposure assessment | Blood/urine biomarker analysis | ±10-20% | $50-300 per test | Days (lab analysis) |

### Implementation Steps

1. **Inventory all chemical hazards**: Document every chemical in use with SDS on file. For each, identify exposure route, TLV, and IDLH.
2. **Establish baseline monitoring**: Conduct initial full-shift personal air sampling for all job categories with chemical exposure potential. Use results to prioritize control efforts.
3. **Deploy detector tubes for routine checks**: Station colorimetric tubes at each process area. Train operators to use them for quick spot-checks before and during chemical operations.
4. **Implement medical surveillance**: For workers above 50% of TLV, establish annual biological monitoring (blood lead, urinary mercury, cholinesterase activity per chemical).
5. **Build antidote stockpile**: Ensure calcium gluconate gel (HF), sodium thiosulfate (cyanide), and atropine (organophosphates) are available at every first aid station.
6. **Review quarterly**: Analyze exposure trends. Investigate any result above 50% of TLV. Update monitoring strategy when processes change.

### Toxic Response Trade-offs

| Response Strategy | Speed | Effectiveness | Risk | Best For |
|------------------|-------|--------------|------|---------|
| Immediate decontamination (flush/discard clothing) | Seconds | High for dermal exposure | Low | Acid/base skin contact, solvent splash |
| Specific antidote administration | Minutes | High for specific poisons | Medium (wrong antidote can harm) | Known poison with available antidote (HF → Ca gluconate, cyanide → thiosulfate) |
| Supportive care only (O₂, fluids, monitoring) | Minutes | Variable | Low | Unknown poison, no specific antidote available |
| Gastric lavage / activated charcoal | Minutes-Hours | Moderate (time-dependent) | Medium (aspiration risk) | Recent oral ingestion (<1 hour) |

## Prerequisites

### Materials

- Reference materials: chemical identification charts, SDS (Safety Data Sheet) library
- Detection equipment: gas detector tubes (colorimetric), pH paper, chlorine test strips
- Emergency supplies: calcium gluconate gel (HF antidote), activated charcoal (oral poison adsorbent), sodium thiosulfate (cyanide antidote), oxygen supply
- Sample collection: impinger bottles, sorbent tubes, filter cassettes for air sampling

### Tools and Equipment

- Analytical balance (0.01 g)
- Fume hood or well-ventilated workspace for testing
- Colorimetric test kits for common toxic substances
- Personal air sampling pumps (if available)
- Biological testing supplies: urine collection containers, blood collection tubes

### Knowledge

- Dose-response relationships: LD50, LC50, NOAEL, LOAEL concepts
- Exposure routes: inhalation, dermal absorption, ingestion, injection
- Target organ toxicology: which chemicals damage which organs
- Antidote mechanisms: specific vs. nonspecific, when each is appropriate

### Infrastructure

- Ventilated workspace for handling toxic materials
- Emergency eyewash and shower (see [emergency-response](emergency-response.md))
- Locked storage for toxic substances
- Waste disposal system for contaminated materials

## Bill of Materials

| Material | Quantity per Assessment | Source | Alternatives |
|----------|------------------------|--------|-------------|
| Gas detector tubes (assorted) | 1-5 per test | [Chemistry](../chemistry/index.md) — reagent production | Electronic gas detector (requires electronics) |
| Activated charcoal | 50-100 g per acute ingestion | Wood charcoal, steam-activated | Plain charcoal (less effective) |
| Calcium gluconate gel 2.5% | 1 tube (25 g) per HF exposure | [Pharmacology](../health/pharmacology.md) | Calcium carbonate slurry (less effective) |
| pH paper (0-14 range) | 1 strip per test | Indicator chemistry | Litmus paper (blue/red only, limited range) |
| Sodium thiosulfate | 5-10 g per cyanide emergency | [Chemistry](../chemistry/index.md) | Sodium nitrite + thiosulfate kit (Cyanide Antidote Kit) |
| Sample collection bottles | 1-5 per assessment | [Glass](../glass/index.md) | Any clean sealed container |

## Process Description

### Toxic Substance Identification

1. **Gather information**: Identify the chemical by name, formula, and CAS number. Consult SDS (Safety Data Sheet) — Section 2 (hazard identification), Section 8 (exposure controls), Section 10 (stability/reactivity), Section 11 (toxicological information). If SDS unavailable, use chemical name to search available references.
2. **Classify the hazard**: Determine acute toxicity (LD50/LC50), chronic toxicity (target organs, carcinogenicity), physical hazards (flammability, reactivity), and environmental hazards. Assign NFPA 704 diamond rating (see [chemical-safety](chemical-safety.md)).
3. **Determine exposure route**: Inhalation (gases, vapors, dusts, fumes), dermal (skin contact, absorption), ingestion (hand-to-mouth, contaminated food/water), or injection (puncture wounds, needles).
4. **Assess exposure level**: Compare measured or estimated exposure concentration to established limits (TLV-TWA, TLV-STEL, PEL, IDLH). Use detector tubes, electronic monitors, or air sampling to measure concentration.

### Air Monitoring Procedure

1. **Select monitoring method**: Colorimetric detector tubes for quick spot checks (±25% accuracy). Personal air sampling pumps with sorbent tubes for full-shift TWA measurements (±10% accuracy). Direct-reading instruments for real-time monitoring (requires electronics).
2. **Position detector tube**: Break both ends of the glass detector tube. Insert into pump. Pull handle for specified number of strokes (each stroke = 100 mL air volume). Read concentration directly from tube color change scale.
3. **Full-shift personal sampling**: Attach sampling pump to worker's collar (breathing zone). Set flow rate per method specification (typically 50-200 mL/min). Run for minimum 6 hours of 8-hour shift. Send sorbent tube to laboratory for analysis (if laboratory available).
4. **Interpret results**: Compare to TLV-TWA for 8-hour average, TLV-STEL for 15-minute peak. If measured >50% of TLV, implement controls (ventilation, PPE, process change). If measured >TLV, mandatory corrective action and resampling.

### Exposure Assessment Methods Compared

**Colorimetric detector tubes**:
- Quick spot-check method — break sealed glass tube, pull air through with hand pump, read concentration from stain length on tube scale
- Accuracy ±25%, range depends on tube formulation (0-500 ppm for most gases)
- Cost: $5-15 per tube, $200-400 for hand pump

**Strengths**:
- Fastest results of any method — 2-5 minutes from tube break to reading
- No power supply or calibration required — hand pump is purely mechanical
- Lowest cost per measurement ($5-15 per tube) — affordable for any facility
- Visual result — stain length directly readable on tube scale, no electronic interpretation needed
- Specific to target chemical — each tube formulation reacts only to one gas or gas class
- Portable — hand pump and tubes fit in a belt pouch for walk-around surveys

**Weaknesses**:
- Lowest accuracy (±25%) — insufficient for compliance-grade TWA measurements
- Single-use — each tube consumed in one measurement, no repeat reading possible
- Cross-sensitivity — some tube formulations react to interfering gases (check cross-sensitivity chart)
- No continuous monitoring — provides a snapshot concentration, not a time-weighted average
- Limited shelf life — tubes expire 1-3 years from manufacture, must be stored at 4-25°C
- Cannot measure below tube detection limit — low-concentration exposures may read as zero

**Personal air sampling pumps**:
- Worker-worn pump draws air through sorbent tube or filter cassette at controlled flow rate (50-200 mL/min) for full shift (6-8 hours)
- Sorbent tube sent to laboratory for analysis (GC, HPLC, or ICP depending on analyte)
- Accuracy ±10% with proper calibration and flow control

**Strengths**:
- Gold standard for compliance TWA measurement — ±10% accuracy meets regulatory requirements
- Measures actual worker exposure — pump worn in breathing zone captures what the worker inhales
- Full-shift time-weighted average — integrates variable concentrations over entire workday
- Laboratory analysis provides definitive chemical identification and quantification
- Covers the broadest range of chemicals — different sorbent media for organics, acids, metals, particulates

**Weaknesses**:
- Slowest turnaround — lab analysis takes days to weeks; no immediate result
- Higher per-sample cost ($50-150) plus laboratory fees ($100-500 per analysis)
- Requires calibrated pump — flow rate must be verified before and after each sample with a bubble burette
- Does not identify peak exposures — full-shift average masks short-term concentration spikes
- Pump must be maintained and charged — battery failure during shift invalidates the sample

**Direct-reading electronic monitors**:
- Electrochemical, infrared, or PID sensors provide continuous real-time concentration readings
- Accuracy ±5-10%, depending on sensor type and calibration
- Data logging records concentration vs. time for trend analysis

**Strengths**:
- Real-time continuous monitoring — detects concentration spikes and excursions instantly
- Data logging captures time-resolved exposure profile — identifies when and where peaks occur
- Can trigger alarms at preset thresholds — automated safety system integration
- Best accuracy for time-varying exposures — does not average away peaks like sorbent tubes
- Multiple sensor configurations available — multi-gas monitors detect 4-6 gases simultaneously

**Weaknesses**:
- Highest instrument cost ($500-5,000 per unit) — expensive to deploy across many workers
- Requires regular calibration — sensor drift means recalibration every 1-3 months with known standard gases
- Sensor-specific — electrochemical cells detect only one gas each; multi-gas monitors need multiple cells
- Limited sensor lifespan — electrochemical cells deplete in 1-3 years and must be replaced
- Cross-sensitivity and interference — some sensors respond to non-target gases, causing false readings

### Acute Poisoning Response

1. **Secure the scene**: Remove patient from exposure source. Do NOT become a victim yourself — wear appropriate PPE before entering contaminated area. For gas releases, approach from upwind.
2. **Assess ABCs**: Airway, Breathing, Circulation. If any compromised, provide basic life support. Administer oxygen if available and breathing is present.
3. **Decontaminate**: Remove contaminated clothing. Flush skin with water for 15+ minutes (30+ minutes for HF exposure — see [chemical-safety](chemical-safety.md)). For eye exposure, flush 15-30 minutes continuously.
4. **Identify the poison**: Determine substance, estimated dose, time since exposure, and route. This information guides all subsequent treatment.
5. **Administer specific antidote if available**: See antidote table in Quantitative Parameters section.
6. **Supportive care**: Maintain airway, breathing, circulation. Monitor vital signs. Transport to medical facility if available.

## Quantitative Parameters

### TLV-TWA Values for Common Industrial Chemicals

| Chemical | TLV-TWA (ppm) | TLV-STEL (ppm) | PEL (ppm) | IDLH (ppm) | Primary Target Organ |
|----------|--------------|----------------|-----------|-------------|---------------------|
| Carbon monoxide (CO) | 25 | — | 50 | 1,200 | Blood (carboxyhemoglobin), CNS |
| Hydrogen sulfide (H₂S) | 1 | 5 | 10 (ceiling) | 50 | Respiratory, CNS |
| Sulfur dioxide (SO₂) | 0.25 | — | 5 | 100 | Respiratory |
| Ammonia (NH₃) | 25 | 35 | 50 | 300 | Respiratory, eyes |
| Chlorine (Cl₂) | 0.5 | 1 | 0.5 | 10 | Respiratory |
| Hydrogen cyanide (HCN) | — (skin) | — | 10 | 50 | Cellular respiration (cytochrome oxidase) |
| Benzene | 0.5 | 2.5 | 1 | 500 | Bone marrow (leukemia) |
| Toluene | 20 | — | 200 | 1,000 | CNS, liver |
| Xylene | 100 | 150 | 100 | 900 | CNS, liver |
| Methanol | 200 | 250 | 200 | 6,000 | Eyes (blindness), CNS |
| Lead (inorganic, dust/mist) | 0.05 mg/m³ | — | 0.05 mg/m³ | 100 mg/m³ | CNS, kidneys, blood |
| Mercury (vapor) | 0.025 mg/m³ | — | 0.1 mg/m³ | 10 mg/m³ | CNS, kidneys |
| Arsenic (inorganic) | 0.01 mg/m³ | — | 0.01 mg/m³ | 5 mg/m³ | Skin, liver, nerves |
| Crystalline silica (quartz) | 0.025 mg/m³ | — | 0.05 mg/m³ | 50 mg/m³ | Lungs (silicosis) |
| Asbestos (all forms) | 0.1 f/cc | — | 0.1 f/cc | — | Lungs (mesothelioma, asbestosis) |

### Acute Toxicity Data (LD50) — Common Industrial Chemicals

| Substance | LD50 Oral (rat, mg/kg) | LD50 Dermal (rat, mg/kg) | LC50 Inhalation (rat, ppm/4hr) | GHS Acute Toxicity Category |
|-----------|----------------------|--------------------------|-------------------------------|---------------------------|
| Ethanol | 7,060 | — | — | 5 (lowest hazard) |
| Sodium hydroxide | 325 | 1,350 | — | 3 |
| Sulfuric acid | 2,140 | — | — | 3 |
| Phenol | 317 | 630 | — | 3 |
| Lead acetate | 450 | — | — | 3 |
| Mercuric chloride | 1 | — | — | 1 (highest hazard) |
| Potassium cyanide | 5 | — | — | 1 |
| Arsenic trioxide | 15 | — | — | 2 |
| Sodium fluoride | 52 | — | — | 2 |

### Antidote Reference Table

| Poison | Antidote | Mechanism | Dose (Adult) | Critical Note |
|--------|---------|-----------|-------------|--------------|
| Cyanide | Sodium thiosulfate | Converts cyanide to thiocyanate (less toxic, excreted by kidneys) | 12.5 g IV over 10 min | Also: sodium nitrite 300 mg IV (induces methemoglobinemia, binds cyanide) |
| Carbon monoxide | Oxygen (100%) | Displaces CO from hemoglobin (half-life: 320 min on room air → 60-90 min on 100% O₂) | 10-15 L/min via non-rebreather mask | Hyperbaric oxygen if available (half-life → 20-30 min) |
| Opioids (morphine, etc.) | Naloxone (if available) | Competitive opioid receptor antagonist | 0.4-2.0 mg IV, repeat q2-3 min | Short acting — monitor for re-sedation; may need continuous infusion |
| Organophosphates | Atropine + pralidoxime | Atropine blocks muscarinic effects; pralidoxime reactivates cholinesterase | Atropine 2 mg IV, repeat q5-15 min; pralidoxime 1-2 g IV | Atropine dose titrated to drying of secretions (may need 10-100+ mg) |
| Iron | Deferoxamine | Chelates iron | 15 mg/kg/hr IV (max 6 g/day) | Turns urine red-vin-rose color (indicates iron excretion) |
| Methanol / Ethylene glycol | Ethanol (IV or oral) or fomepizole | Competes for alcohol dehydrogenase, preventing toxic metabolite formation | Loading: 15 mL/kg 10% ethanol IV over 30 min; maintain BAC 100-150 mg/dL | Fomepizole preferred if available (no CNS depression); hemodialysis for severe cases |
| Lead | Calcium disodium EDTA | Chelates lead for urinary excretion | 30-50 mg/kg/day IV or IM in divided doses | Also used: dimercaprol (BAL), succimer (oral); risk of lead redistribution to brain |
| Hydrofluoric acid (HF) | Calcium gluconate (topical or injection) | Binds fluoride ions, preventing tissue destruction and hypocalcemia | Topical: 2.5% gel applied continuously; Intra-arterial: 10 mL 10% solution | For systemic toxicity: IV calcium gluconate 10 mL 10% solution; monitor ECG |

### Exposure Duration Limits

| Scenario | CO (ppm) | H₂S (ppm) | SO₂ (ppm) | NH₃ (ppm) |
|----------|----------|-----------|-----------|-----------|
| 8-hour TWA | 25 | 1 | 0.25 | 25 |
| 15-minute STEL | — | 5 | — | 35 |
| 30 minutes | 100 | 50 | 5 | 150 |
| 10 minutes (evacuation) | 400 | 100 | 10 | 300 |
| IDLH (immediate danger) | 1,200 | 50 | 100 | 300 |
| Lethal concentration (est.) | 6,400 (30 min) | 400-700 (30 min) | 1,000 (10 min) | 5,000-10,000 (30 min) |

## Scaling Notes

- **Awareness level**: Workers know the names and basic hazards of chemicals they handle. SDS sheets available. No quantitative monitoring. Appropriate for low-toxicity operations (woodworking, basic metalworking).
- **Monitoring capability**: Colorimetric detector tubes for spot checks. Periodic personal air sampling. Can verify compliance with TLV-TWA for common chemicals. Serves 10-100 workers across multiple operations.
- **Industrial hygiene program**: Full-time industrial hygienist. Regular personal monitoring, area monitoring, biological monitoring (blood/urine testing for absorbed chemicals). Exposure trend analysis. Medical surveillance program. Requires [occupational-health](../health/occupational-health.md) capability. Serves 100+ workers.
- **Comprehensive toxicology**: Advanced analytical capability (GC, HPLC, mass spectrometry for exposure assessment). In-house toxicology reference laboratory. Research capability on novel toxic exposures. Requires full electronics and computing infrastructure.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Detector tube gives no reading | Tube expired, wrong tube type, insufficient pump strokes | Check expiration date; verify tube matches target chemical; pull correct number of strokes |
| False positive on air sample | Cross-sensitivity with interfering chemical | Consult tube cross-sensitivity chart; use a different detection method for confirmation |
| Worker symptoms below TLV | Individual sensitivity, skin absorption (TLV may not account for dermal route), mixed exposures | Evaluate dermal exposure; consider additive effects of multiple chemicals; lower exposure limit for sensitive individuals |
| Unexplained illness cluster | Shared exposure source, common ventilation pathway, contaminated water/food | Conduct environmental survey: air, water, food; interview affected workers for common factors; expand sampling |
| Antidote unavailable | Supply not stocked, expired, or never produced | Focus on decontamination and supportive care; initiate production of critical antidotes (thiosulfate, calcium gluconate) |

## Safety

- **Self-protection first**: Before treating any poisoned patient or entering a contaminated area, ensure your own safety. Wear appropriate PPE (see [PPE](ppe.md)). A second victim doubles the emergency.
- **Hydrogen sulfide (H₂S)**: Insidious killer — deadens sense of smell at >100 ppm (so you cannot smell it at dangerous concentrations). At 500+ ppm, causes immediate respiratory arrest ("knockdown"). Always use H₂S detector in confined spaces, sewers, and petroleum operations. Never enter an H₂S area without SCBA.
- **Cyanide**: Prevents cells from using oxygen. Patient turns cherry-red (venous blood remains oxygenated — cells cannot extract O₂). Rapid onset. Sodium thiosulfate antidote must be administered IV within minutes for best outcome. Industrial sources: metal plating, gold extraction, fumigation.
- **Lead**: Cumulative poison — body does not excrete lead efficiently. Chronic exposure causes: anemia, wrist drop (radial nerve palsy), kidney damage, reproductive effects, developmental delays in children. Children absorb 5× more lead than adults from the same exposure. Lead exposure sources: smelting, battery production, lead-based paint, lead solder in water pipes.
- **Mercury**: Vapor is the most dangerous form — inhaled mercury vapor crosses the blood-brain barrier. Chronic exposure causes: tremor ("hatter's shakes"), gingivitis, emotional lability, kidney damage. Elemental mercury spills: do NOT vacuum (vaporizes mercury). Collect with a card or pipette into sealed container. Ventilate area.

## Quality Control

- **Detector tube verification**: Check expiration dates monthly. Store at 4-25°C. Verify pump flow rate quarterly using a calibrated bubble burette (100 mL ±5%).
- **Analytical accuracy**: Run known-concentration standards with each batch of samples. Results must be within ±15% of known value for field methods, ±10% for laboratory methods.
- **Medical surveillance**: For workers exposed to toxic substances above 50% of TLV, conduct periodic medical examinations: baseline + annual. Include biological monitoring specific to the exposure (blood lead level for lead workers, urinary mercury for mercury workers, cholinesterase activity for organophosphate workers).
- **Exposure records**: Maintain individual exposure records for each worker for 30+ years. Many occupational diseases (cancer, silicosis, asbestosis) have latency periods of 10-40 years. Exposure records are essential for establishing causation.
- **Biological Exposure Indices (BEIs)**: Reference values for biological monitoring.

| Chemical | BEI (Biological Marker) | Specimen | Sampling Time | Action Level |
|----------|------------------------|----------|---------------|-------------|
| Lead | Blood lead level | Blood | Not critical | >20 μg/dL: increased monitoring; >40 μg/dL: removal from exposure |
| Mercury | Urinary mercury | Urine (end of shift) | Pre-shift vs post-shift | >20 μg/L: increased monitoring; >50 μg/L: removal from exposure |
| Carbon monoxide | Carboxyhemoglobin (COHb) | Blood | End of shift | >3.5% (non-smoker), >10% (smoker): investigate exposure |
| Cadmium | Urinary cadmium | Urine | Not critical | >5 μg/g creatinine: kidney damage risk |
| Benzene | Urinary S-phenylmercapturic acid | Urine | End of shift | >25 μg/g creatinine: exposure above acceptable level |

## Variations and Alternatives

### Toxic Substances by Industrial Sector

| Sector | Key Toxic Exposures | Primary Control | Medical Surveillance |
|--------|---------------------|----------------|---------------------|
| Smelting (iron, copper) | Lead, SO₂, CO, metal fumes | Local exhaust ventilation, respiratory protection | Blood lead, spirometry, chest X-ray |
| Mining | Silica dust, diesel exhaust, radon (underground) | Wet drilling, ventilation, dust suppression | Spirometry, chest X-ray (silicosis screening) |
| Chemical manufacturing | Acids, solvents, specific process chemicals | Enclosed processes, LEV, PPE | Biological monitoring specific to chemicals handled |
| Petroleum refining | Benzene, H₂S, PAHs, hydrocarbon vapors | Closed systems, gas detection, SCBA for entry | Benzene metabolites, liver function tests |
| Pharmaceuticals | Drug APIs, solvents, dust | Containment, LEV, glove boxes | Drug-specific biological monitoring |
| Construction | Asbestos, silica, lead (paint), noise | Wet methods, respiratory protection, hearing protection | Spirometry, chest X-ray, audiometry |

### Historical Toxicology

- **Paracelsus (1493-1541)**: Established dose-response principle. "All things are poison and nothing is without poison; only the dose permits something not to be poisonous." Before Paracelsus, substances were classified as simply "poisonous" or "not poisonous."
- **Percival Pott (1775)**: Identified chimney sweeps' carcinoma (scrotal cancer from soot) — first recognized occupational cancer. Demonstrated that environmental exposures cause cancer decades after exposure.
- **Alice Hamilton (1869-1970)**: Pioneer of industrial toxicology in the United States. Documented lead poisoning in pottery workers, mercury poisoning in hatters, and carbon disulfide poisoning in rubber workers. Established the field of occupational medicine.

## References

- [Chemical Safety](chemical-safety.md) — semiconductor process chemical hazards, NFPA ratings
- [Emergency Response](emergency-response.md) — spill response, chemical exposure first aid
- [Ventilation](ventilation-exhaust.md) — local exhaust ventilation for toxic substance control
- [PPE](ppe.md) — respiratory and dermal protection selection
- [Pharmacology](../health/pharmacology.md) — antidote preparation and drug interactions
- [Occupational Health](../health/occupational-health.md) — workplace exposure monitoring and medical surveillance
- [Acids & Bases](../chemistry/acids-bases.md) — acid and alkali toxicity data

---

*Part of the [Bootciv Tech Tree](../index.md) · [EHS](./index.md) · [All Domains](../index.md)*
