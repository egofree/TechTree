# Medicine & Surgery

> **Node ID**: health.medicine
> **Domain**: [Health](./index.md)
> **Dependencies**: [`animals.beekeeping`](../animals/beekeeping.md),
> [`health.sanitation`](./sanitation.md),
> [`knowledge.writing`](../knowledge/writing.md)
> **Enables**: [`health.emergency-care`](./emergency-care.md),
> [`health.infectious-disease`](./infectious-disease.md),
> [`health.pharmacology`](./pharmacology.md),
> [`health.surgery-basics`](./surgery-basics.md)
> **Timeline**: Years 5-100+
> **Outputs**: surgical_capability, medical_treatment
> **Critical**: Yes — basic medical capability reduces preventable death more than any other single intervention

## Overview

Medicine and surgery in a bootstrap civilization encompasses pharmaceutical production from plant and synthetic sources, basic surgical capability (wound management, fracture reduction, amputation), diagnostic examination, emergency procedures, and infection control. The foundational tier relies on plant-derived medicines and manual techniques; later stages add synthetic pharmaceuticals, laboratory diagnostics, and increasingly sophisticated surgical interventions.

Access to even basic medical capability — wound irrigation, fracture immobilization, antiseptic practice, and a handful of essential drugs (ether for anesthesia, morphine for pain, quinine for malaria) — dramatically reduces preventable death. Lister's introduction of antisepsis in 1867 alone cut surgical mortality from ~50% to ~15%. The gap between "no medical capability" and "basic wound care + essential drugs" is larger than the gap between "basic care" and "modern hospital medicine" in terms of lives saved.

Position in the dependency chain: medicine sits upstream of [Infectious Disease Management](infectious-disease.md), [Surgery Basics](surgery-basics.md), [Emergency Care](emergency-care.md), and [Pharmacology](pharmacology.md). It depends on [Sanitation](sanitation.md) (clean water and waste disposal are the foundation of public health), [Beekeeping](../animals/beekeeping.md) (honey as wound dressing and the source of beeswax for wound sealing), and [Writing](../knowledge/writing.md) (medical records, dosing tables, and knowledge transmission across generations). Without writing, accumulated medical knowledge is lost with each generation of practitioners.

This article is the hub for medical capability. The clinical specializations — emergency trauma, infectious disease, surgery, pharmacology, diagnostics, instrument fabrication — are covered in their own sub-articles. The sections below cover the shared foundations: the pharmaceutical pharmacopeia, surgical materials, equipment, basic diagnostic method, the wound-care procedure that every practitioner must master, and the training and scaling of medical capability in a bootstrap civilization.

## Prerequisites

### Materials

- [Pharmacological source materials](#bill-of-materials) — willow bark, cinchona bark, opium poppy, foxglove, iodine sources (kelp, caliche)
- [Surgical materials](#bill-of-materials) — catgut sutures, silk thread, cotton gauze, plaster bandages
- [Clean water](../water/index.md) — for wound irrigation, instrument sterilization, oral rehydration
- [Soap](../chemistry/soap.md) — handwashing is the single most effective infection-control intervention
- [Iodine and ethanol](../chemistry/index.md) — antiseptics
- [Iron and steel](../metals/iron-steel.md) — surgical instrument fabrication
- [Glass](../glass/index.md) — syringes, thermometers, microscope lenses, apothecary containers

### Tools and Equipment

- [Basic metalworking](../metals/index.md) — forging and grinding of scalpels, forceps, needle holders, retractors
- [Glassblowing](../glass/glassblowing.md) — syringes, thermometers, apothecary ware
- [Lens grinding](../optics/index.md) — microscope objectives for laboratory diagnostics
- [Knowledge of writing and arithmetic](../knowledge/writing.md) — record-keeping, dose calculation
- [Autoclave / pressure cooker](#bill-of-materials) — instrument sterilization

### Knowledge

- Anatomy — bone, vessel, nerve, and organ locations. Without anatomical knowledge, surgery is blind mutilation.
- The vital signs: pulse (60-100 bpm resting adult), respiratory rate (12-20/min), temperature (36.5-37.5°C oral), blood pressure (target systolic 90-140 mmHg — measurable only with a sphygmomanometer, which requires pressure-gauge capability).
- The germ theory of disease (Pasteur, 1860s; Lister antisepsis, 1867) — the conceptual foundation of infection control. Without it, antiseptic practice is not understood and is abandoned under pressure.
- Pharmacology fundamentals — dose, route, onset, duration, half-life. The difference between a therapeutic dose and a toxic dose is often 2-5×; without dosing discipline, medicines become poisons.

### Infrastructure

- Clean, well-lit work space for examination and minor procedures
- [Clean water supply](sanitation.md) — for handwashing, instrument cleaning, wound irrigation
- Waste disposal for contaminated dressings and sharps
- Sterilization capability — boiling vessel minimum; pressure cooker (autoclave) preferred
- Secure storage for medicines (cool, dark, child-proof)

## Bill of Materials

### Pharmaceutical Materials

| Material | Source | Use | Active compound |
|----------|--------|-----|-----------------|
| Willow bark (Salix spp.) | Wild harvest | Salicin → salicylic acid (pain/fever) | Salicin 0.5-1.5% of dry bark |
| Opium poppy latex | Cultivation | Morphine, codeine (analgesic) | Morphine 4-21% of opium latex |
| Cinchona bark | Tropical cultivation | Quinine (anti-malarial) | Quinine 2-9% of bark |
| Ephedra stems | Arid region harvest | Ephedrine (bronchodilator) | Ephedrine 0.5-2.0% of dry stem |
| Digitalis (foxglove) leaves | Cultivation | Cardiac glycosides (heart failure) | Digitoxin 0.15-0.40% of dry leaf |
| Ethanol | Fermentation + distillation | Solvent, antiseptic, anesthetic adjunct | 70% w/w for antisepsis; 95% for extraction |
| Sulfuric acid | [Chemical manufacturing](../chemistry/index.md) | Pharmaceutical synthesis | 95-98% concentrated |
| Acetic anhydride | [Chemical manufacturing](../chemistry/index.md) | Aspirin synthesis (acetylation of salicylic acid) | Pure reagent |
| Iodine | Seaweed ash (kelp) or caliche deposits | Antiseptic tincture | 5% iodine, 10% KI in 70% ethanol |
| Gypsum (CaSO₄·2H₂O) | [Mineral deposit](../mining/index.md) | Plaster of Paris for casts | Hemihydrate (Plaster of Paris) sets in 5-10 min |

### Surgical Materials

| Material | Use | Notes |
|----------|-----|-------|
| Catgut (sheep intestine submucosa) | Absorbable sutures | 7-21 day absorption depending on gauge and treatment |
| Silk thread | Non-absorbable sutures | Remove after 7-14 days; boil to sterilize |
| Cotton gauze | Wound dressings | Sterilized by boiling or autoclaving; 4-12 ply |
| Plaster bandages | Fracture immobilization | Dip in water 20-25°C, apply 5-12 layers; full set in 24-48 h |
| Adhesive tape | Wound closure, dressings | Fabric or paper backing with rubber-resin adhesive |
| Guttapercha | Dental fillings | Softens at 70°C, sets rigid at body temperature |
| Honey (medical grade) | Wound dressing | Low water activity; produces H₂O₂; Manuka-type preferred |

### Equipment

| Equipment | Purpose | Bootstrap Level |
|-----------|---------|----------------|
| Scalpel (forged steel) | Incisions, debridement | [Basic metalworking](../metals/index.md) |
| Forceps (toothed, smooth) | Tissue handling | [Basic metalworking](../metals/index.md) |
| Needle holder | Suturing | [Basic metalworking](../metals/index.md) |
| Hemostatic forceps | Vessel clamping | [Basic metalworking](../metals/index.md) |
| Retractors | Wound exposure | [Basic metalworking](../metals/index.md) |
| Syringe (glass/metal) | Irrigation, injection | [Glass](../glass/glassblowing.md) + [metalworking](../metals/index.md) |
| Stethoscope (wooden/metal tube) | Auscultation | [Basic turning](../machine-tools/machining.md) |
| Mercury thermometer | Temperature measurement | 35-42°C range, 0.1°C graduations; [glassblowing](../glass/glassblowing.md) + mercury |
| [Centrifuge](../chemistry/centrifuge.md) (hand-cranked) | Blood separation | 3,000-5,000 RPM; [metalworking](../metals/index.md) |
| Compound microscope (100×, 400×, 1000×) | Diagnostics | [Lens grinding](../optics/index.md) |
| Autoclave / pressure cooker | Sterilization | 121°C at 15 psi; [metal vessel](../metals/index.md) + heat source |
| Bone saw | Amputation | Steel + woodworking tools |
| Tourniquet | Hemorrhage control | Cloth + stick windlass; systolic pressure >250 mmHg required |

## Process Description

### Step-by-Step: Wound Care Procedure (The Foundational Skill)

Wound care is the most common surgical procedure in any civilization and the skill that every practitioner must master first. The procedure below covers a contaminated soft-tissue wound (laceration or abrasion).

1. **Scene safety and body substance isolation.** Confirm the scene is safe (no continuing hazard). Don gloves if available; eyewear if splash risk. The practitioner's own health is the first priority — a sick or injured practitioner helps no one.

2. **Assess the wound and the patient.** Determine mechanism (sharp laceration vs. crush vs. abrasion vs. bite), time since injury, depth, and structures involved. Assess distal pulse, sensation, and movement beyond the wound — nerve, tendon, or vessel injury changes management.

3. **Control hemorrhage.** Direct pressure with sterile gauze for 5-15 minutes controls 95% of bleeding. Tourniquet only for uncontrolled extremity hemorrhage (life over limb); note the application time — tourniquet left >2 hours risks limb loss.

4. **Anesthetize if available.** Local infiltration with 1% lidocaine (max 3 mg/kg without epinephrine, 7 mg/kg with) along wound margins. Field block for larger areas. Ether or chloroform general anesthesia only for major procedures (anesthesia risk vs. benefit).

5. **Irrigate the wound copiously.** This is the single most important step for infection prevention. Irrigate with sterile saline (or clean boiled water, cooled) at 5-8 psi pressure (squeeze bottle with 18-gauge needle, or bulb syringe). Volume: 100-300 mL per cm of laceration. Remove all visible foreign material with forceps.

6. **Debride dead tissue.** Excise clearly non-viable tissue (gray, non-bleeding edges, crushed muscle) with scalpel or scissors. Dead tissue is a bacterial culture medium; leaving it guarantees infection.

7. **Close the wound (or leave open).** Close clean wounds <6 hours old with sutures (silk or catgut, 4-0 to 6-0 gauge for face; 3-0 to 4-0 for trunk/extremity). Leave contaminated or >12-hour-old wounds open to heal by secondary intention (granulation), or close after 3-5 days of delayed primary closure if no infection develops.

8. **Dress the wound.** Apply sterile gauze, secure with tape or bandage. Change dressing daily, or sooner if saturated. Inspect for infection at each change.

9. **Tetanus prophylaxis if available.** At bootstrap stage, tetanus immune globulin and toxoid are not available — rely on thorough irrigation and debridement. Once [pharmaceutical production](pharmaceutical-production.md) capability exists, tetanus toxoid immunization is the preventive mainstay.

10. **Document.** Record wound location, size, depth, structures involved, irrigation volume, closure method, suture material, and date. Follow up at 24-48 hours for infection check; at 7-14 days for suture removal.

### Fracture Immobilization Procedure

1. **Assess the fracture.** Deformity, crepitus, point tenderness, loss of function. Check distal pulse, sensation, movement — absent pulse is a surgical emergency.
2. **Reduce the fracture if displaced.** Longitudinal traction, restore alignment, check pulse returns. Analgesia (morphine 10 mg IM adult) before reduction.
3. **Immobilize with plaster.** Pad bony prominences with cotton. Dip plaster bandages in water 20-25°C, apply 5-12 layers. Mold to limb contour, maintain reduction until set (5-10 min). Full set 24-48 h.
4. **Elevate and recheck.** Elevate limb above heart for 24-48 h to reduce swelling. Recheck distal pulse and sensation at 1, 4, 24 hours — increasing swelling in a tight cast can cause compartment syndrome (limb-threatening).
5. **Follow up.** Radiograph if capability exists at 7-10 days to confirm alignment. Cast for 4-8 weeks (long bones) or 3-4 weeks (small bones).

## Quantitative Parameters

### Vital Signs Reference (Adult, Resting)

| Parameter | Normal range | Concerning | Critical |
|-----------|--------------|------------|----------|
| Pulse rate | 60-100 bpm | 100-120 (fever, blood loss, shock); <50 (hypothermia, certain poisonings) | >130 or <40; irregular with poor perfusion |
| Respiratory rate | 12-20 /min | 20-30 (fever, acidosis, hypoxia); <12 (opioid, brain injury) | >30 or <8 |
| Temperature (oral) | 36.5-37.5°C | 37.5-38.5 (low fever); 38.5-40 (fever) | >40 (hyperthermia); <35 (hypothermia) |
| Systolic blood pressure | 100-140 mmHg | 90-100 (relative hypotension); 140-180 (hypertension) | <90 (shock); >180 (hypertensive emergency) |
| Capillary refill | <2 seconds | 2-3 seconds (dehydration, shock) | >3 seconds |
| Urine output | >0.5 mL/kg/h | 0.25-0.5 (dehydration) | <0.25 (renal failure) |

### Antiseptic Concentrations and Contact Times

| Antiseptic | Concentration | Contact time | Spectrum | Notes |
|------------|---------------|--------------|----------|-------|
| Ethanol | 70% w/w (≈78% v/v) | 15-30 sec skin | Bacteria, fungi, enveloped viruses | Not sporicidal; flammable |
| Povidone-iodine | 2.5% iodine (10% Betadine) | 30-60 sec skin; 5 min surgical scrub | Bacteria (incl. MRSA), fungi, viruses, spores (prolonged) | Inactivated by blood/organic material |
| Chlorhexidine | 4% (surgical scrub), 2% (alcohol rinse) | 30 sec skin; 3 min scrub | Bacteria, viruses (not spores) | Persistent activity 4-6 h; less irritating than iodine |
| Phenol (carbolic acid) | 2-5% solution | 5-10 min instrument soak | Bacteria, fungi | Toxic to tissue; historical (Lister 1867) |
| Hydrogen peroxide | 3% solution | 5-10 min (uncovered wound) | Bacteria, viruses (not spores) | Damages healthy tissue; not for deep wounds |

### Pediatric Drug Dosing (Weight-Based)

| Drug | Adult dose | Pediatric dose | Maximum |
|------|-----------|----------------|---------|
| Morphine (IM/IV) | 10 mg q4h | 0.1-0.2 mg/kg q4h | Adult max |
| Quinine (oral, malaria treatment) | 600 mg q8h × 7 days | 10 mg/kg q8h × 7 days | 600 mg/dose |
| Salicylic acid (aspirin, oral) | 300-600 mg q4h prn | 10-15 mg/kg q4h prn (>12 yr only) | 4 g/day adult |
| Ephedrine (oral, bronchodilator) | 25-50 mg q6h | Not recommended <6 yr | 150 mg/day |
| Digoxin (oral, loading) | 0.5-1.0 mg divided | 0.02-0.04 mg/kg divided | — |

> **Note:** Pediatric aspirin is avoided in viral illness (<12 yr) due to Reye's syndrome risk. Full pharmacology reference: [Pharmacology](pharmacology.md).

## Scaling Notes

- **Single village (≤500 people):** One trained practitioner with first-aid kit, essential drugs (aspirin, morphine, quinine, antiseptics), and wound-care skills. Mortality reduction: 30-50% vs. no care. Requires 1 person trained for 6-12 months.
- **Small community (500-5,000 people):** Dedicated clinic building, full-time practitioner + 1-2 apprentices. Adds basic laboratory (microscope), sterilization (pressure cooker), fracture management. Surgical capability: wound care, abscess drainage, simple closure. Mortality reduction: 50-70%.
- **Town (5,000-50,000 people):** Hospital with surgical theater, dedicated pharmacist, laboratory technician, 5-20 staff. Adds anesthesia (ether/chloroform), laparotomy for acute abdomen, Cesarean section, fracture internal fixation. Mortality reduction: 70-85%. The threshold where modern medicine's marginal returns begin.
- **Minimum economic scale:** One practitioner per 500 population is the WHO benchmark for primary care. Below this density, geographic access limits care more than clinical capability.
- **Non-linear returns:** The first tier of medical capability (wound care, antiseptics, oral rehydration, essential drugs) prevents ~70% of preventable deaths. Each subsequent tier adds diminishing mortality reduction but large quality-of-life improvement. A bootstrap civilization should prioritize the first tier before pursuing hospitals.
- **Bottleneck:** Trained practitioners. Knowledge transmission requires [writing](../knowledge/writing.md), structured apprenticeship, and 5-10 years of clinical experience per practitioner. Medical knowledge accumulates over generations; losing continuity (war, plague, diaspora) resets capability by decades.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Surgical wound infection (erythema, pus, fever) | Inadequate antisepsis, dead tissue left, contaminated closure | Open wound, irrigate copiously, debride necrotic tissue, dress open; systemic antibiotic if available |
| Postoperative fever (day 1-3) | Normal inflammatory response, OR early wound infection, OR atelectasis, OR urinary retention | Examine wound; encourage cough/deep breathing; check urine output; fever >38.5°C beyond 48 h warrants investigation |
| Hematoma at wound site | Inadequate hemostasis at closure | Small: observe, warm compresses; large: open, evacuate, control bleeder, re-close |
| Dehiscence (wound opens) | Inadequate tissue tension, infection, poor nutrition, premature suture removal | Approximate edges with adhesive strips or re-suture if clean; address malnutrition; treat infection |
| Cast too tight (pain, swelling, dusky toes/fingers) | Post-injury swelling under rigid cast | Split cast immediately (full thickness, down to skin) to relieve pressure; check pulse returns |
| Compartment syndrome (severe pain, paresthesia, rigid compartment) | Bleeding or edema within fascial compartment; limb-threatening | Fasciotomy — surgical release of the fascia; time-critical (<6 h for full recovery) |
| Drug dose error | Arithmetic mistake, weight mis-estimation, pediatric/adult confusion | Always calculate mg/kg, confirm with second practitioner, use written dosing reference; have naloxone available for opioid overdose (0.4 mg IV/IM) |
| Anesthetic complication (ether: respiratory depression, salivation; chloroform: hepatotoxicity, cardiac arrest) | Overdose, inadequate airway, patient sensitivity | Reduce dose; establish airway; supportive resuscitation (bag-valve-mask); avoid chloroform in favor of ether if possible |
| Post-partum hemorrhage | Uterine atony, retained placenta, laceration | Uterine massage; oxytocin 10 IU IM if available; bimanual compression; remove retained placenta; repair lacerations |
| Sepsis (fever >39°C, HR >100, RR >20, hypotension, confusion) | Overwhelming bacterial infection | Without antibiotics: aggressive supportive care (IV fluids, fever control, oxygen); prevention via antisepsis is the main lever |

## Safety

- **Sharps injury:** Needle-stick and scalpel cuts are the leading occupational hazard. Recapping needles is prohibited; dispose of sharps in puncture-proof containers. A sharps injury from a hepatitis- or HIV-positive patient requires immediate post-exposure prophylaxis if available.
- **Blood-borne pathogen exposure:** Hepatitis B (10-30% transmission per needle-stick from e-antigen positive source), hepatitis C (1.8-3%), HIV (0.3%). Universal precautions: treat all blood as infectious. Wear gloves, eyewear, gown for any procedure with blood exposure risk.
- **Anesthetic agents:** Ether (diethyl ether, bp 34.6°C) is extremely flammable — explosive at 1.85-36% concentration in air. No open flames, electrocautery, or static sparks in the anesthetizing room. Chloroform is hepatotoxic and cardiotoxic — avoid in favor of ether if possible. Nitrous oxide requires gas-compression infrastructure (not bootstrap-tier).
- **Mercury thermometer breakage:** Mercury vapor is a cumulative neurotoxin (IDLH 10 mg/m³, NIOSH). Clean up spills with sulfur powder to bind mercury, ventilate area, dispose of as hazardous waste. Use alcohol or digital thermometers if available.
- **Phenol (carbolic acid):** Concentrated phenol causes chemical burns on skin and is absorbed systemically, causing cardiac arrhythmia. Handle with gloves; dilute to <5% before use.
- **Autoclave pressure vessel:** Operates at 15 psi (103 kPa) above atmospheric — a pressure vessel failure is an explosion risk. Inspect vessel and seals regularly; never open under pressure; follow [pressure vessel safety](../ehs/index.md).

### Personal Protective Equipment

- Gloves (latex or nitrile) for any patient contact with blood or body fluids
- Eye protection (goggles or face shield) for procedures with splash risk
- Gown or apron for surgical and trauma procedures
- Mask (cloth minimum; N95 for suspected tuberculosis or pandemic respiratory illness)
- Sharps-resistant gloves when cleaning instruments

### Emergency Procedures

- **Needle-stick from known infected source:** Wash wound with soap and water, irrigate mucous membranes, post-exposure prophylaxis within 2 hours if available, baseline and follow-up serology.
- **Anesthetic arrest (apnea, hypotension):** Stop anesthetic, establish airway (bag-valve-mask with oxygen if available), CPR if no pulse, IV fluids, vasopressor if available.
- **Local anesthetic toxicity (CNS excitation then seizures, cardiovascular collapse):** Stop injection, IV benzodiazepine for seizures, IV lipid emulsion 20% (1.5 mL/kg bolus) if available — specific therapy for local anesthetic systemic toxicity.
- **Malignant hyperthermia (with succinylcholine or volatile anesthetics):** Stop trigger, IV dantrolene 2.5 mg/kg, cooling, treat acidosis. High mortality without dantrolene.

## Quality Control

### Acceptance Criteria

- **Sterility of instruments:** Autoclave indicator tape or chemical integrator confirms ≥121°C for ≥15 min. Biological indicator (Geobacillus stearothermophilus spore strip) cultured after autoclaving shows no growth.
- **Drug potency:** Plant-derived medicines must meet minimum active compound concentration (e.g., cinchona bark ≥5% quinine for therapeutic use). Assayed by extraction and gravimetric or titrimetric method if laboratory available.
- **Surgical outcomes:** Track wound infection rate (<5% for clean wounds; <10% for clean-contaminated), mortality per procedure, and readmission rate.
- **Diagnostic accuracy:** Microscope smear results cross-checked against clinical outcome; vital sign calibration (thermometer against reference, sphygmomanometer against mercury column).

### Testing Methods

- **Autoclave sterility:** Biological indicator (spore strip) incubated 24-48 h at 55-60°C; no growth = sterile.
- **Drug assay (basic):** Weight-loss-on-drying for moisture; titration for alkaloid content (quinine: acid-base titration); thin-layer chromatography if silica and solvents available.
- **Water purity:** Boil-test (no residue), Total Dissolved Solids <500 ppm (electrical conductivity measurement if meter available); coliform test (incubate water on nutrient agar 24 h at 37°C).
- **Instrument sharpness:** Scalpel cleanly cuts moist paper without tearing; suture needle penetrates rubber dam without resistance.

### Sampling

- Audit 1 in 20 wound closures for infection outcome; investigate clusters.
- Assay each batch of plant-derived drug for active compound.
- Calibrate thermometer and sphygmomanometer monthly against reference standard.

## Variations and Alternatives

- **Plant-based pharmacopeia (bootstrap default):** Willow bark (salicin), opium (morphine), cinchona (quinine), foxglove (digitalis), ephedra (ephedrine). Limited but effective for pain, fever, malaria, heart failure, asthma. See [Pharmacology](pharmacology.md) for extraction details.
- **Synthetic pharmaceuticals (later stage):** Once [chemistry](../chemistry/index.md) reaches acetylsalicylic acid (aspirin, 1897) and sulfonamide antibiotics (1935), the pharmacopeia expands dramatically. Penicillin (1928, mass-produced 1943) requires industrial fermentation.
- **Surgical specialization:** [Emergency Care](emergency-care.md) (trauma, triage), [Surgery Basics](surgery-basics.md) (wound closure, abscess, amputation, appendectomy), [Infectious Disease Management](infectious-disease.md) (antisepsis, sterilization, disease treatment).
- **Diagnostic methods:** Clinical examination (vital signs, auscultation, percussion) is the foundation. Microscopy adds laboratory confirmation. X-ray requires [electricity](../energy/electricity.md) and vacuum tubes — post-bootstrap.
- **Acupuncture and traditional systems:** Effective for some chronic pain and nausea; not a substitute for antisepsis, antibiotics, or surgery. Respectful integration where evidence supports.
- **Honey and sugar dressings:** Hyperosmolar wound environment inhibits bacteria; useful when antiseptics unavailable. Medical-grade honey (Manuka-type) has additional antibacterial activity from methylglyoxal.
- **Maggot debridement:** Sterile fly larvae (Lucilia sericata) selectively consume necrotic tissue. Effective for chronic wounds; controlled cultivation required.

### Medical System Trade-off Comparison

| Capability tier | Prevents | Requires | Lives saved per 1,000 pop/yr |
|----------------|----------|----------|------------------------------|
| None | — | — | Baseline |
| Wound care + antiseptics | Wound sepsis, tetanus | Training, ethanol, iodine | 5-15 |
| + Essential drugs (aspirin, morphine, quinine, ORS) | Pain, fever, malaria, diarrheal death | Plant sources, distillation | 15-30 |
| + Sterile surgery (autoclave, anesthesia) | Appendicitis, obstructed labor, fractures | Metal, glass, ether, pressure vessel | 30-50 |
| + Antibiotics (penicillin, sulfonamides) | Pneumonia, sepsis, child infections | Industrial fermentation | 50-70 |

## References

- [Emergency Care](emergency-care.md) — triage, hemorrhage control, burn management, shock resuscitation, fracture reduction, dental emergencies, PPE fabrication, gas detection
- [Infectious Disease Management](infectious-disease.md) — wound antisepsis, sterilization, plant-derived anti-infectives, major endemic diseases (malaria, cholera, typhoid, pneumonia, TB, tetanus), infection diagnosis laboratory
- [Surgery Basics](surgery-basics.md) — wound assessment, suturing technique, sterilization procedures, anesthesia, specific surgical procedures (amputation, abscess drainage, appendectomy)
- [Pharmacology](pharmacology.md) — drug extraction, preparation, formulation, dosing, quality control, storage, drug interactions
- [Diagnostics](diagnostics.md) — physical examination, vital signs, laboratory testing, imaging fundamentals
- [Medical Instruments](medical-instruments.md) — diagnostic and surgical instrument fabrication
- [Sanitation](sanitation.md) — clean water, sewage disposal, hygiene practices
- [Water Treatment](water-treatment.md) — clean water for disease prevention
- [Pharmaceutical Production](pharmaceutical-production.md) — industrial-scale drug manufacturing

---

*Part of the [Bootciv Tech Tree](../index.md) • [Public Health, Sanitation & Medicine](./index.md) • [All Domains](../index.md)*
