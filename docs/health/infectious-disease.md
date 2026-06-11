# Infectious Disease Management

> **Node ID**: health.infectious-disease
> **Domain**: [Health](./index.md)
> **Dependencies**: [`health.medicine`](medicine.md), [`health.sanitation`](sanitation.md), [`health.pharmacology`](pharmacology.md)
> **Enables**: (supporting capability for epidemic response and endemic disease control)
> **Timeline**: Years 5-100+
> **Outputs**: infection_control, disease_treatment, antisepsis
> **Critical**: Yes — infectious disease is the leading cause of death in pre-industrial civilizations; basic antisepsis and disease management saves more lives than any advanced intervention

Infectious disease management covers wound infection prevention and treatment, antiseptic practice, and treatment of the major endemic and epidemic diseases encountered in a bootstrap civilization. Before antibiotics, the cornerstone of infection control is antisepsis (killing pathogens before they enter the body), sanitation (preventing transmission), and the body's own immune response. Plant-derived antimicrobials (quinine for malaria, iodine for wound antisepsis) provide the limited pharmacological arsenal available at the bootstrap stage.

Drug preparation, dosing, and quality control are covered in [Pharmacology](pharmacology.md). Wound suturing and surgical technique are covered in [Surgery Basics](surgery-basics.md). Emergency procedures for trauma are covered in [Emergency Care](emergency-care.md).

## Wound Antisepsis

**Ethanol**: 70% concentration (by weight) is optimal. Applied to intact skin before procedures. Denatures bacterial proteins and disrupts cell membranes. Not effective against spores or some viruses. Fast-acting (15-30 seconds contact). Flammable.

**Povidone-iodine (Betadine)**: 2.5% iodine in a polymer carrier (povidone). Broad-spectrum: bacteria (including MRSA), fungi, viruses, spores (with prolonged contact). Applied to intact skin and mucous membranes. Less irritating than tincture of iodine. Inactivated by blood and organic material — clean wound before applying. Do not use on large open wounds or burns (systemic iodine absorption causes thyroid dysfunction).

**Chlorhexidine 4%**: Persistent antimicrobial activity (remains effective on skin for hours after application). More effective than povidone-iodine for surgical hand scrubs. Not effective against spores. Rare allergic reactions. Less inactivated by blood than iodine. Used for surgical site preparation and hand hygiene.

**Phenol (carbolic acid)**: First surgical antiseptic (Lister, 1867). From coal tar distillation (see Petrochemicals). Dilute to 2-5% solution for wound irrigation and instrument sterilization. Pure phenol causes chemical burns — handle with care.

**Iodine tincture**: Extract iodine from seaweed ash (kelp) or caliche deposits (Chilean saltpeter). Dissolve in ethanol + KI solution (5% iodine, 10% KI in 70% ethanol). Apply to wounds as antiseptic. Stains brown — normal.

**Hydrogen peroxide (H₂O₂)**: Antiseptic, wound cleaning. Produce by electrolysis of cold dilute sulfuric acid → peroxydisulfuric acid → hydrolysis → H₂O₂ + H₂SO₄. Distill under vacuum (bp 150°C at 1 atm — decomposes; distill at reduced pressure ~10 kPa, bp ~70°C). 3% solution for wound care. Store in dark bottle (decomposes in light). Do NOT use for deep wound irrigation — it damages healthy tissue and has minimal antimicrobial benefit in wounds.

## Medical Instrument Sterilization

**Methods by capability level**:
- **Boiling**: Submerge instruments in boiling water for 20+ minutes. Kills most bacteria and viruses. Does NOT kill bacterial spores (Clostridium tetani, C. perfringens, B. anthracis). Acceptable for instruments used in low-risk procedures (wound care, injections) when no better method is available.
- **Pressure cooking (autoclaving)**: 121°C at 15 psi for 15 minutes. Kills all microorganisms including spores. Wrap instruments in cloth or place in sterilization pouches before autoclaving. The gold standard for sterilization. Verify effectiveness with indicator tape (changes color at sterilization temperature) or biological indicators (spore strips cultured after autoclaving — no growth = successful sterilization).
- **Chemical sterilization**: Soak clean instruments in 2% glutaraldehyde solution for 10 hours (kills all microorganisms including spores). Rinse thoroughly with sterile water before use. Glutaraldehyde is toxic and irritating to skin and respiratory tract — use in a fume hood with gloves. Alternative: 6-8% hydrogen peroxide solution for 6 hours.
- **Dry heat**: 160°C for 2 hours or 170°C for 1 hour in a dry oven. Suitable for oils, powders, and instruments that corrode in steam. No corrosion risk, but takes much longer than autoclaving. Must use glass or metal containers (paper and cloth char at these temperatures).

## Plant-Derived Anti-Infective Medicines

> **Note**: Drug preparation, dosing, and quality control details are in [Pharmacology](pharmacology.md). This section covers clinical use and sourcing.

**Cinchona bark (quinine)**: Anti-malarial. The single most important anti-infective available at bootstrap stage. Extract by boiling bark in water. Quinine also treats arrhythmias. 8-10 g bark daily as decoction for malaria treatment. Malaria is the leading infectious disease killer in tropical regions — cinchona cultivation is a strategic priority.

**Artemisinin** (from Artemisia annua, sweet wormwood): Potent antimalarial — Nobel Prize 2015. Extract with low-polarity solvent at <60°C (compound degrades with heat). See [Pharmacology](pharmacology.md) for preparation details.

**Willow bark (salicin → salicylic acid → aspirin)**: Pain and fever management. Fever is a primary symptom of most infections — antipyretic treatment improves patient comfort and reduces fluid losses from sweating. Harvest bark from willow (Salix species) in spring when sap flows. Dry bark. Extract by boiling 30 g bark in 500 mL water for 15 minutes. Strain. Dose: 1 cup of decoction for pain/fever. Contains salicin (prodrug of salicylic acid). Later (Chemistry), synthesize acetylsalicylic acid (aspirin) from salicylic acid + acetic anhydride.

**Ephedra (ephedrine)**: Bronchodilator (asthma treatment), decongestant, vasoconstrictor. Extract by water decoction. Later synthesized chemically.

## Infection Control Principles

**Wound infection signs**: Redness spreading from wound, increasing pain, swelling, warmth, red streaks (lymphangitis), fever. If infected → open wound, irrigate under pressure, apply antiseptic. Honey (natural antibacterial — medical-grade honey has low water activity and produces hydrogen peroxide) can be applied as wound dressing.

**Systemic infection (sepsis)**: Signs include high fever (>39°C), rapid heart rate (>100 bpm), rapid breathing (>20/minute), confusion, low blood pressure. Without antibiotics, treatment is supportive: fluids, fever control, rest. Sepsis carries >50% mortality without antibiotic therapy. Prevention through antisepsis and sanitation is far more effective than treatment.

**Transmission prevention**:
- **Contact transmission**: Wash hands with soap and water before and after patient contact. Wear gloves if available. Clean surfaces with 70% ethanol or 2% phenol.
- **Droplet transmission**: Cloth mask over nose and mouth when within 2 meters of coughing patients. Isolate respiratory infection patients in separate room or area.
- **Waterborne transmission**: See [Sanitation](sanitation.md) — clean water prevents cholera, typhoid, dysentery.
- **Vector-borne transmission**: Mosquito control (drain standing water, use netting) prevents malaria, dengue, yellow fever.

## Major Bootstrap-Stage Infectious Diseases

> **Note**: Drug dosages for all treatments below are in the [Pharmacology dosing reference table](pharmacology.md#dosing-reference-table).

**Malaria** (Plasmodium spp., mosquito-borne): Intermittent high fever with chills, headache, body aches, anemia. Most deadly infectious disease in tropical regions. Treatment: quinine from cinchona bark. Prevention: mosquito netting, draining standing water, quinine prophylaxis (lower dose). Chronic malaria causes anemia and splenomegaly — quinine treatment is curative if completed.

**Wound infection / tetanus** (Clostridium tetani, soil-borne): Spasms beginning in jaw (lockjaw/trismus), spreading to entire body. Fatal without treatment. Caused by spore contamination of wounds. Prevention: thorough wound irrigation, sterilization of instruments (autoclaving kills spores; boiling does not). At bootstrap stage, once tetanus symptoms appear, treatment is largely supportive — prevention is critical.

**Gas gangrene** (Clostridium perfringens, wound contamination): Rapidly spreading tissue death with gas production under skin (crepitus on palpation), foul-smelling wound, severe pain, fever. Emergency requiring immediate surgical debridement of all dead tissue or amputation. Without treatment, fatal within 12-24 hours.

**Cholera** (Vibrio cholerae, waterborne): Profuse watery diarrhea ("rice water stools"), rapid dehydration, shock. Can kill within hours. Treatment: oral rehydration solution (ORS: 1 L water + 6 level teaspoons sugar + ½ level teaspoon salt). Prevention: clean water supply and sewage disposal — see [Sanitation](sanitation.md).

**Typhoid fever** (Salmonella typhi, waterborne/foodborne): Sustained high fever, abdominal pain, rose-colored rash on trunk, diarrhea or constipation. Without antibiotics, treatment is supportive (fluids, fever control). Mortality 10-30% without treatment. Prevention: clean water, proper sewage disposal, hand washing.

**Pneumonia** (bacterial: Streptococcus pneumoniae; or viral): Cough, fever, rapid breathing, chest pain, crackles on auscultation. Without antibiotics, bacterial pneumonia carries 20-40% mortality in adults, higher in elderly and infants. Treatment: supportive care (fluids, rest, fever control), postural drainage (position patient to drain affected lung segments).

**Tuberculosis** (Mycobacterium tuberculosis, airborne): Chronic cough (>3 weeks), night sweats, weight loss, hemoptysis (coughing blood). Diagnosis: acid-fast bacilli on sputum smear (requires microscope with 1000× oil immersion and Ziehl-Neelsen stain). Without antibiotics, tuberculosis is treatable only with rest, nutrition, and isolation (sanatorium model). Mortality 40-60% over years. Prevention: isolate infectious patients, improve ventilation, avoid overcrowding.

## Basic Laboratory for Infection Diagnosis

**Microscope**: Brightfield compound microscope with 10×, 40×, and 100× (oil immersion) objectives. Eyepiece 10× gives total magnifications of 100×, 400×, and 1000×. Used for: blood smears (malaria parasites, blood cell morphology), urine sediment (cells, crystals, casts), sputum (acid-fast bacteria for TB), stool (parasites, ova).

**Centrifuge**: Hand-cranked or electric, 3,000-5,000 RPM. For separating blood cells from plasma (hematocrit tubes), concentrating urine sediment.

**Gram stain**: Crystal violet → iodine → ethanol decolorization → safranin counterstain. Gram-positive bacteria stain purple (retain crystal violet); Gram-negative stain pink/red (safranin). Guides empirical antibiotic choice if antibiotics become available. Reagents: crystal violet, Gram's iodine, 95% ethanol, safranin O.

**Ziehl-Neelsen stain (acid-fast)**: For TB diagnosis. Smear sputum on slide, heat-fix. Flood with carbol fuchsin, heat to steaming for 5 minutes. Rinse. Decolorize with acid-alcohol (3% HCl in 95% ethanol) until no more color runs. Counterstain with methylene blue. Acid-fast bacilli (TB) appear red against blue background.

## Limitations

- **No antibiotics**: Until advanced microbiology and industrial fermentation are established, bacterial infections cannot be treated systemically. Reliance on antisepsis, wound drainage, and the body's immune response limits treatable conditions. A wound infection that would be cured with a course of penicillin in modern medicine may become lethal.
- **No blood transfusion**: Without blood banking (anticoagulant preservation, typing, cross-matching, refrigerated storage), severe hemorrhage can only be managed with fluid replacement (saline, oral rehydration).
- **Narrow pharmaceutical range**: Plant-derived medicines provide analgesics (morphine, salicin), anti-malarials (quinine), and a few cardiac drugs (digitalis). Many diseases (diabetes, hypertension, most cancers, autoimmune disorders) have no effective treatment in the bootstrap period.
- **Infection control limits**: Aseptic technique reduces surgical infection rates dramatically, but sterility is never absolute. Without antibiotics, post-operative infection remains a leading cause of surgical mortality.

## See Also

- [Medicine & Surgery](medicine.md) — overview hub for all medical capabilities
- [Pharmacology](pharmacology.md) — drug extraction, preparation, dosing, and quality control
- [Surgery Basics](surgery-basics.md) — wound assessment, suturing, sterilization procedures
- [Emergency Care](emergency-care.md) — triage, hemorrhage control, burn and fracture management
- [Sanitation](sanitation.md) — clean water, sewage disposal, hygiene practices
- [Diagnostics](diagnostics.md) — physical examination, vital signs, laboratory testing

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Public Health, Sanitation & Medicine](./index.md) • [All Domains](../../index.md)*
