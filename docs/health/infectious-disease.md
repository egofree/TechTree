# Infectious Disease Management

> **Node ID**: health.infectious-disease
> **Domain**: [Health](./index.md)
> **Dependencies**: [`health.medicine`](medicine.md), [`health.sanitation`](sanitation.md), [`health.pharmacology`](pharmacology.md)
> **Enables**: (supporting capability for epidemic response and endemic disease control)
> **Timeline**: Years 5-100+
> **Outputs**: infection_control, disease_treatment, antisepsis
> **Critical**: Yes — infectious disease is the leading cause of death in pre-industrial civilizations; basic antisepsis and disease management saves more lives than any advanced intervention

## Overview

Infectious disease management covers wound infection prevention and treatment, antiseptic practice, sterilization, and treatment of the major endemic and epidemic diseases encountered in a bootstrap civilization. Before antibiotics, the cornerstone of infection control is antisepsis (killing pathogens before they enter the body), sanitation (preventing transmission), and the body's own immune response. Plant-derived antimicrobials (quinine for malaria, iodine for wound antisepsis) provide the limited pharmacological arsenal available at the bootstrap stage.

The death toll of infectious disease in a pre-industrial population is staggering. Pre-1900, roughly 40-50% of all deaths were infectious — respiratory infections (pneumonia, TB), diarrheal disease (cholera, dysentery, typhoid), vector-borne (malaria), and wound infection (tetanus, sepsis). Child mortality under age 5 was 30-40%, overwhelmingly from infection. Lister's introduction of surgical antisepsis in 1867 cut operative mortality from ~50% to ~15%; the introduction of clean water and sewage systems (London, 1858-1875) cut cholera and typhoid death rates by 80-95%; vaccination (Jenner's smallpox, 1796) eliminated the disease that had killed 300-500 million people in the 18th century. These three interventions alone — antisepsis, sanitation, vaccination — prevented more death than every subsequent medical advance combined.

Position in the chain: infectious disease management depends on [Medicine & Surgery](medicine.md) (the foundational medical capability), [Sanitation](sanitation.md) (clean water and waste disposal), and [Pharmacology](pharmacology.md) (drug extraction and dosing). It is the medical capability with the highest ratio of lives-saved to knowledge-required — the interventions are simple, cheap, and staggeringly effective when consistently applied.

Drug preparation, dosing, and quality control are covered in [Pharmacology](pharmacology.md). Wound suturing and surgical technique are covered in [Surgery Basics](surgery-basics.md). Emergency procedures for trauma are covered in [Emergency Care](emergency-care.md).

## Prerequisites

### Materials

- [Antiseptics](#bill-of-materials) — ethanol, iodine (from kelp or caliche), phenol (from coal tar), chlorhexidine if chemistry allows
- [Clean water](../water/index.md) — for handwashing, instrument sterilization, wound irrigation, oral rehydration solution
- [Soap](../chemistry/soap.md) — fat + alkali saponification; handwashing alone reduces respiratory and diarrheal disease transmission by 30-50%
- Sterilization capability — pressure cooker (autoclave) at 121°C / 15 psi
- [Plant-derived antimicrobials](#bill-of-materials) — cinchona bark (quinine), Artemisia annua (artemisinin), willow bark (salicin)

### Tools and Equipment

- [Compound microscope](../optics/index.md) (100×, 400×, 1000× oil immersion) — laboratory diagnosis (blood smears, sputum, stool)
- [Hand-cranked or electric centrifuge](../chemistry/centrifuge.md) (3,000-5,000 RPM) — blood separation, urine concentration
- [Glass slides and cover slips](../glass/glassblowing.md) — microscopy
- [Autoclave / pressure cooker](../metals/index.md) — 121°C / 15 psi; the gold standard for instrument sterilization
- Glass syringes and steel needles — vaccination and injection (if reusable, must be sterilized between patients)
- Refrigeration (if available) — cold chain for vaccines and some drugs

### Knowledge

- **Germ theory of disease** (Pasteur, Koch, 1860s-1880s) — the conceptual foundation. Pathogens (bacteria, viruses, fungi, protozoa) cause specific diseases and are transmitted by specific routes. Without this theory, antisepsis appears magical and is abandoned under pressure.
- **Aseptic vs. antiseptic technique** — asepsis prevents contamination (sterile field); antisepsis kills contaminants after exposure. Surgery requires asepsis; wound care relies on antisepsis.
- **Disease transmission routes** — contact (direct, indirect), droplet (large respiratory droplets, <2 m), airborne (small droplet nuclei, >2 m), vector-borne (mosquito, flea, tick), waterborne, foodborne. Each route requires a different prevention strategy.
- **Herd immunity threshold** — the proportion of immune individuals needed to prevent sustained transmission: ~95% for measles (R₀ 12-18), ~80% for smallpox (R₀ 3.5-6), ~70% for rubella (R₀ 5-7). Vaccination programs below this threshold protect individuals but not the community.

### Infrastructure

- [Clean water supply](sanitation.md) — the single most important infrastructure for infectious disease prevention
- [Sewage disposal system](sanitation.md) — prevents waterborne disease transmission
- Isolation room or area — separate infectious patients (TB, cholera, plague) from other patients and the community
- Ventilation — airborne disease transmission reduced by 10+ air changes per hour
- Vector control — drainage of standing water (mosquitoes), rodent control (fleas)

## Bill of Materials

### Antiseptics and Disinfectants

| Material | Concentration | Use | Source |
|----------|---------------|-----|--------|
| Ethanol | 70% w/w | Skin antisepsis, instrument soaking 15-30 min | [Fermentation](../agriculture/index.md) + [distillation](../chemistry/distillation.md) |
| Iodine tincture | 5% I₂, 10% KI in 70% ethanol | Wound antisepsis, skin prep | [Seaweed ash](../plants/index.md) (kelp) or caliche deposits |
| Povidone-iodine | 10% (= 1% available I₂) | Surgical scrub, mucous membrane antisepsis | Iodine + polyvinylpyrrolidone (advanced chemistry) |
| Phenol (carbolic acid) | 2-5% solution | Instrument soak, surface disinfection | [Coal tar](../petroleum/index.md) distillation |
| Chlorhexidine gluconate | 4% surgical scrub, 2% rinse | Surgical hand scrub, persistent skin activity | Synthetic (advanced chemistry) |
| Hydrogen peroxide | 3% solution | Wound cleaning (uncovered); instrument sterilization 6% | Electrolysis of cold dilute H₂SO₄ → peroxydisulfuric → hydrolysis → H₂O₂ |
| Bleach (sodium hypochlorite) | 0.1-0.5% available chlorine | Surface disinfection, water treatment | [Chlor-alkali process](../chemistry/chlor-alkali.md); absorb Cl₂ in NaOH |
| Glutaraldehyde | 2% solution | Cold sterilization of instruments (10 h soak) | Synthetic (advanced chemistry) |

### Plant-Derived Anti-Infective Medicines

| Plant | Active compound | Disease treated | Source | Cultivation requirement |
|-------|-----------------|-----------------|--------|-------------------------|
| Cinchona (Cinchona officinalis) | Quinine (2-9% of bark) | Malaria | Tropical Andes; cultivated in India, Java after 1850s | Tropical montane, 1,500-3,000 m elevation |
| Artemisia annua (sweet wormwood) | Artemisinin (0.01-1% of leaves) | Malaria (including chloroquine-resistant) | Temperate; Nobel Prize 2015 | Annual herb; temperate cultivation |
| Willow (Salix spp.) | Salicin → salicylic acid | Fever, pain (antipyretic/analgesic) | Temperate; wild-harvest or cultivation | Riparian; widely distributed |
| Eucalyptus | Eucalyptol (1,8-cineole) | Decongestant, antiseptic | Australia; widely cultivated | Subtropical; fast-growing tree |
| Garlic (Allium sativum) | Allicin | Mild antibacterial, antifungal | Cultivated worldwide | Temperate; bulb crop |
| Tea tree (Melaleuca alternifolia) | Terpinen-4-ol | Topical antifungal, antiseptic | Australia | Subtropical wetland |
| Senna (Cassia angustifolia) | Sennosides | Laxative (supportive care) | India, Sudan | Tropical/subtropical |

### Sterilization and Personal Protective Equipment

| Material | Use | Quantity per procedure |
|----------|-----|------------------------|
| Sterile gauze (cotton, 4-12 ply) | Wound dressing, drapes | 5-30 pads |
| Cloth or surgical drapes | Sterile field | 2-6 drapes |
| Gloves (latex or nitrile if available) | Body substance isolation | 1-3 pairs |
| Cloth mask | Droplet precaution | 1 per patient encounter |
| Sterilization pouches or cloth wraps | Instrument packaging | 1-3 per instrument set |
| Autoclave indicator tape | Sterilization confirmation | 5-15 cm per pack |

## Process Description

### Wound Antisepsis Methods

The choice of antiseptic depends on the situation — intact skin preparation, wound cleaning, or instrument sterilization.

**Ethanol (70% w/w):** Applied to intact skin before procedures. Denatures bacterial proteins and disrupts cell membranes. Not effective against spores or some viruses. Fast-acting (15-30 second contact). Allow to dry before incision — wet ethanol causes pain on cut tissue. Flammable — no cautery or open flame during use.

**Povidone-iodine (Betadine, 2.5% iodine):** Broad-spectrum: bacteria (including MRSA), fungi, viruses, spores (with prolonged contact). Applied to intact skin and mucous membranes for surgical site preparation (30-second scrub, allow to dry). Less irritating than tincture of iodine. Inactivated by blood and organic material — clean wound before applying. Do not use on large open wounds or burns (systemic iodine absorption causes thyroid dysfunction).

**Chlorhexidine 4%:** Persistent antimicrobial activity (4-6 hours on skin after application). More effective than povidone-iodine for surgical hand scrubs. Not effective against spores. Rare allergic reactions. Less inactivated by blood than iodine. Standard for surgical site preparation and hand hygiene.

**Phenol (carbolic acid, 2-5%):** First surgical antiseptic (Lister, 1867). From coal tar distillation. Dilute to 2-5% solution for wound irrigation and instrument sterilization. Pure phenol causes chemical burns — handle with gloves. Largely superseded by iodine and chlorhexidine but usable if those are unavailable.

**Iodine tincture:** Extract iodine from seaweed ash (kelp dried and burned to ash, leached with water, oxidized with MnO₂ + H₂SO₄ → I₂ vapor, condensed) or caliche deposits (Chilean saltpeter containing sodium iodate; reduce with bisulfite). Dissolve 5 g I₂ + 10 g KI in 70% ethanol to 100 mL. Apply to intact skin and small wounds as antiseptic. Stains brown — normal.

**Hydrogen peroxide (3%):** Antiseptic, wound cleaning. Produce by electrolysis of cold dilute sulfuric acid → peroxydisulfuric acid → hydrolysis → H₂O₂ + H₂SO₄. Distill under vacuum (bp 150°C at 1 atm — decomposes; distill at reduced pressure ~10 kPa, bp ~70°C). 3% solution for wound care. Store in dark bottle (decomposes in light). Do NOT use for deep wound irrigation — it damages healthy tissue and has minimal antimicrobial benefit in wounds.

### Medical Instrument Sterilization — Step-by-Step

1. **Clean instruments mechanically.** Disassemble if possible. Wash in warm water with soap to remove all blood, tissue, and organic material. Organic material inactivates most disinfectants and shields microbes from sterilization. Ultrasonic cleaner if available.
2. **Rinse and dry.** Residual water dilutes the sterilant and corrodes instruments.
3. **Package.** Wrap in cloth, or place in sterilization pouch with internal chemical indicator. Do not seal airtight — steam must penetrate.
4. **Autoclave (preferred method).** 121°C at 15 psi (103 kPa) for 15 min (wrapped) or 3 min (unwrapped small items). For larger loads or porous materials, extend to 30 min. Verify with autoclave indicator tape (changes color at 121°C) or biological indicator (spore strip).
5. **Chemical sterilization (if no autoclave).** Soak clean instruments in 2% glutaraldehyde for 10 hours (kills all microorganisms including spores). Rinse thoroughly with sterile water before use. Glutaraldehyde is toxic — use in a vented area with gloves.
6. **Dry heat (alternative).** 160°C for 2 hours or 170°C for 1 hour in a dry oven. Suitable for oils, powders, and instruments that corrode in steam. No corrosion risk, but takes much longer than autoclaving.
7. **Boiling (minimum acceptable).** Submerge in boiling water for 20+ minutes. Kills most bacteria and viruses. Does NOT kill bacterial spores (Clostridium tetani, C. perfringens, B. anthracis). Acceptable only for low-risk procedures when no better method is available.

### Vaccination Procedure (Smallpox, Jenner 1796)

1. **Source vaccine lymph.** From a healthy cow with natural cowpox, or from a previously vaccinated human pustule (arm-to-arm transfer — risks hepatitis and syphilis transmission; animal-source preferred).
2. **Prepare the site.** Clean skin of upper outer arm with ethanol, allow to dry.
3. **Apply vaccine and scarify.** Place a drop of vaccine lymph on the skin. Use a sterile bifurcated needle or lancet to make 2-3 punctures through the vaccine drop into the epidermis (not into the dermis — intradermal vaccination is less effective).
4. **Observe "take."** At 6-8 days, a papule → vesicle → pustule → scab develops at the site. This "major reaction" confirms successful vaccination. No reaction = failed vaccination; repeat with fresh vaccine.
5. **Document.** Record date, vaccine source, lot, and reaction. Immunity from successful vaccination lasts 3-5 years; revaccinate every 5-10 years in endemic areas.

### Oral Rehydration Solution (ORS) Preparation

The single most effective treatment for diarrheal disease dehydration (cholera, rotavirus). Reduces diarrheal mortality by ~90%.

1. **To 1 liter of clean (boiled then cooled) water** add:
   - 6 level teaspoons (≈30 g) of sugar (sucrose or glucose)
   - ½ level teaspoon (≈2.5 g) of table salt (NaCl)
2. **Stir until dissolved.** Solution should taste mildly salty, slightly sweet — not unpleasant.
3. **Administer:** Adults: 200-400 mL after each loose stool. Children: 10-15 mL/kg after each loose stool, given in small sips over 10-15 min. Continue feeding.
4. **Discard after 24 hours** (bacterial growth in stored solution).

## Quantitative Parameters

### Sterilization Parameters by Method

| Method | Temperature | Pressure | Exposure time | Kills spores | Notes |
|--------|-------------|----------|---------------|--------------|-------|
| Boiling | 100°C | 1 atm | 20+ min | No | Minimum acceptable; not for surgical instruments |
| Autoclave (gravity) | 121°C | 15 psi (103 kPa) | 15-30 min | Yes | Standard for wrapped instruments |
| Autoclave (prevacuum) | 134°C | 30 psi (206 kPa) | 3-4 min | Yes | Faster; requires vacuum pump |
| Dry heat | 160°C | atmospheric | 120 min | Yes | For oils, powders, glass |
| Dry heat | 170°C | atmospheric | 60 min | Yes | Faster; shorter life for some materials |
| Glutaraldehyde 2% | 20-25°C | atmospheric | 20 min (high-level disinfection); 10 h (sterilization) | Yes (10 h) | Cold sterilization; toxic |
| Hydrogen peroxide 6% | 20-25°C | atmospheric | 6 h | Yes | Cold sterilization; irritant |
| Ethanol 70% | 20-25°C | atmospheric | 15-30 min | No | Skin antisepsis; instrument soaking |
| Phenol 5% | 20-25°C | atmospheric | 10-30 min | No | Surface disinfection |

### Major Endemic Diseases — Epidemiology and Treatment

| Disease | Pathogen | Transmission | Incubation | Untreated case fatality | Treatment (bootstrap) |
|---------|----------|--------------|-----------|------------------------|----------------------|
| Malaria | Plasmodium falciparum, vivax | Anopheles mosquito | 7-30 days | 0.1-20% (falciparum) | Quinine 600 mg q8h × 7 d; ORS for dehydration |
| Cholera | Vibrio cholerae | Contaminated water/food | 2 h-5 days | 25-50% (severe) | ORS; IV Ringer's lactate if available |
| Typhoid fever | Salmonella typhi | Contaminated water/food | 6-30 days | 10-30% | Supportive; fluids; fever control |
| Pneumonia (bacterial) | Streptococcus pneumoniae | Respiratory droplet | 1-3 days | 20-40% (adults) | Supportive; postural drainage; prayer for antibiotics |
| Tuberculosis | Mycobacterium tuberculosis | Airborne | 2-10 yr (latent) | 40-60% (over years) | Rest, nutrition, isolation; sanatorium model |
| Tetanus | Clostridium tetani | Spore in wound | 3-21 days | 30-90% | Supportive; sedation; wound debridement; prevention critical |
| Anthrax | Bacillus anthracis | Spore contact/ingestion | 1-7 days | 20-80% (cutaneous vs. inhalational) | Penicillin if available; otherwise supportive |
| Plague (bubonic) | Yersinia pestis | Flea bite | 2-6 days | 40-70% | Streptomycin if available; otherwise supportive |
| Smallpox (eradicated 1980) | Variola virus | Respiratory/contact | 7-17 days | 30% (ordinary); 90% (hemorrhagic) | Vaccination prevents; supportive care only |
| Measles | Measles virus | Airborne | 10-12 days | 5-15% (developing world) | Vitamin A 200,000 IU; supportive; prevention by vaccine |
| Influenza | Influenza virus | Respiratory droplet | 1-4 days | 0.1% (seasonal); 2-3% (1918) | Supportive; rest; fluids |

### Herd Immunity Thresholds (Vaccine-Preventable Diseases)

| Disease | Basic reproduction number (R₀) | Herd immunity threshold | Vaccine efficacy | Vaccination strategy |
|---------|-------------------------------|------------------------|------------------|----------------------|
| Measles | 12-18 | 95% | 95% (2 doses) | 2-dose childhood schedule |
| Pertussis | 12-17 | 92-94% | 80-85% | Multi-dose childhood |
| Smallpox | 3.5-6 | 80-85% | 95% (1 dose) | Mass vaccination, ring vaccination in outbreaks |
| Polio | 5-7 | 80-86% | 95% (3 doses OPV) | Universal childhood; eradication campaign |
| Rubella | 5-7 | 80-85% | 95% (1 dose) | Childhood + adolescent girls |
| Diphtheria | 6-7 | 85% | 95% | Childhood multi-dose |
| Influenza | 1.5-2 | 33-50% | 40-60% (seasonal) | Annual, high-risk groups |

## Scaling Notes

- **Single village (≤500 people):** Clean water, handwashing discipline, one trained practitioner with antiseptics and ORS. Prevents 60-80% of infectious death at this scale. Cost: training + a few liters of ethanol and iodine per year.
- **Community (500-5,000):** Add a basic laboratory (microscope for malaria smear, TB sputum), isolation room, vaccination program (smallpox eradication model). Mortality reduction: 70-90%.
- **Town (5,000-50,000):** Full sanitation infrastructure (sewer, treated water), epidemic surveillance, vaccination cold chain, laboratory with staining and culture capability. Mortality reduction: 80-95%. This is the threshold where endemic cholera, typhoid, and plague are eliminated.
- **Minimum economic scale:** ORS and antiseptic wound care pay for themselves in lives saved even at single-village scale. Clean water infrastructure pays for itself in prevented disease burden above ~1,000 population.
- **Non-linear returns:** The first 80% of infectious disease reduction is achieved with antisepsis, clean water, and ORS — cheap and simple. The next 15% requires vaccination programs and basic antibiotics — moderate cost. The final 5% requires advanced antibiotics, ICU care, and molecular diagnostics — enormous cost per life saved. A bootstrap civilization should focus relentlessly on the first tier.
- **Bottleneck:** Behavioral change. Antisepsis, handwashing, and clean water are effective only if practiced consistently. Cultural resistance (miasma theory, traditional healers, religious interpretation of disease) can delay adoption by generations. Education and demonstrable outcomes are the levers.
- **Bottleneck (cold chain):** Vaccines requiring refrigeration (2-8°C) are difficult to deploy without reliable electricity. Smallpox vaccine (lyophilized, stable at room temperature for weeks) was the historical exception — this is why it was the first disease eradicated. Most modern vaccines require a continuous cold chain from manufacture to patient.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Surgical wound infection rate >5% for clean wounds | Inadequate sterilization; breaks in aseptic technique; theatre air contamination | Audit autoclave (spore strips); review surgical scrub protocol; improve theatre ventilation (10+ air changes/h); restrict theatre traffic |
| Autoclave failing to sterilize (spore strip grows) | Temperature not reached; air not exhausted (trapped air insulates load); overload; packaging too dense | Verify cycle temperature (independent probe); check air discharge; reduce load size; repackage loosely |
| Wound infection despite antiseptic | Antiseptic inactivated by blood/organic material; spore contamination (tetanus); deep wound not debrided | Clean wound thoroughly before antiseptic; debride all necrotic tissue; leave contaminated wound open |
| Tetanus case despite wound care | Spores not killed by boiling instruments; wound not adequately debrided; no prior vaccination | Autoclave instruments (kills spores); aggressive debridement; establish vaccination program |
| Malaria treatment failure with quinine | Chloroquine-resistant strain (quinine still effective); inadequate dose; vomiting of oral dose; non-falciparum malaria (relapse from liver stage) | Confirm diagnosis (blood smear); parenteral quinine if vomiting; add primaquine for P. vivax liver stage |
| Cholera outbreak despite "clean" water | Source contaminated after treatment; storage contamination; food-borne transmission | Test water at point-of-use (not just source); chlorinate stored water (0.5 mg/L free Cl₂ residual); inspect food handlers |
| Measles outbreak in vaccinated population | Cold chain failure (vaccine inactivated); single-dose schedule (5-10% primary failure); accumulating susceptible cohort | Audit cold chain temperatures; give second dose; mass revaccination if cohort susceptibility >10% |
| Antibiotic resistance (once available) | Overuse; incomplete courses; agricultural use | Restrict to confirmed bacterial infection; complete full course; prohibit agricultural growth-promoter use; rotate antibiotic classes |
| Sepsis developing from small wound | Delayed debridement; virulent organism (Strep pyogenes, Staph aureus); immunocompromised host | Aggressive early debridement; vigilant wound monitoring; isolate streptococcal cases |
| Hospital-acquired infection (nosocomial) | Contaminated hands of staff; contaminated equipment; overcrowded ward | Mandatory handwashing between patients (reduces nosocomial rates 30-50%); sterilize shared equipment; isolate infected patients |

## Safety

- **Phenol toxicity:** Concentrated phenol is absorbed through intact skin, causing chemical burns and systemic toxicity (cardiac arrhythmia, methemoglobinemia). Handle ≥5% solutions with nitrile gloves and eye protection; never on large wounds. Chronic exposure causes hepatic and renal damage.
- **Glutaraldehyde:** Irritant to skin, eyes, and respiratory tract. Use only in ventilated areas (≤0.05 ppm ceiling, OSHA). Sensitizer — repeated exposure causes occupational asthma. Closed autoclave preferred over glutaraldehyde cold sterilization whenever possible.
- **Ethanol flammability:** 70% ethanol has flash point 21°C — ignites easily at room temperature. No open flames, cautery, or spark sources during use. Store in sealed metal or glass containers away from heat.
- **Hydrogen peroxide concentration hazard:** 30% H₂O₂ (stock before dilution to 3%) causes severe skin burns and ignites organic material. Dilute immediately on receipt; never store concentrated peroxide near metals (catalytic decomposition).
- **Mercury thermometer breakage (instruments/thermometers):** Mercury vapor IDLH 10 mg/m³ (NIOSH). Clean up spills with sulfur powder (binds mercury), ventilate, dispose as hazardous waste.
- **Blood-borne pathogen exposure during wound care:** Hepatitis B (10-30% needle-stick transmission), hepatitis C (1.8-3%), HIV (0.3%). Universal precautions: gloves, eye protection, sharps disposal.
- **Autoclave pressure vessel:** 15 psi over atmospheric — vessel failure is explosion risk. Inspect door seals and pressure relief valve annually; never open under pressure.

### Personal Protective Equipment

- Gloves (latex or nitrile) for all patient contact with blood or body fluids
- Eye protection for procedures with splash risk (wound irrigation, abscess drainage)
- Mask (cloth minimum; N95 for suspected TB or pandemic respiratory illness)
- Gown or apron for wound care with extensive body fluid exposure
- Puncture-resistant gloves when cleaning contaminated instruments

### Emergency Procedures

- **Phenol skin splash:** Flush with water 15+ min; wash with polyethylene glycol (PEG 300) or vegetable oil to dissolve residual phenol; treat systemic symptoms (cardiac monitoring).
- **Glutaraldehyde splash (eye):** Flush with water or saline 15+ min; ophthalmology referral.
- **Blood-borne pathogen exposure (needle-stick):** Wash wound, irrigate mucous membrane, post-exposure prophylaxis within 2 h if available (hepatitis B immunoglobulin, HIV antiretrovirals), baseline and 6-month serology.
- **Autoclave overpressure:** If relief valve lifts, DO NOT approach; allow to cool and depressurize through relief before inspecting. Never override the relief valve.
- **Chlorine gas release (from bleach + acid mixing):** Evacuate, ventilate; respiratory support for exposed; neutralize residual with sodium thiosulfate solution.

## Quality Control

### Acceptance Criteria

- **Sterility:** Autoclave biological indicator (Geobacillus stearothermophilus) — no growth after 24-48 h incubation at 55-60°C. Run at least one indicator per autoclave load containing implants or surgical instruments.
- **Antiseptic efficacy:** 3-log reduction in bacterial count on skin after application (verifiable by contact-plate sampling before and after — if laboratory capability exists).
- **Drug potency (quinine):** Cinchona bark or extracted quinine assayed by acid-base titration; therapeutic bark ≥5% quinine. Oral quinine dose 600 mg confirmed by weight or volume.
- **Water quality:** Free chlorine residual 0.2-0.5 mg/L at point of use (test with DPD reagent if available); zero coliforms per 100 mL (membrane filter culture).
- **Vaccination "take" rate:** ≥95% major reaction at 6-8 days for smallpox vaccine; investigate any rate below 90% (cold chain failure suspected).

### Testing Methods

- **Sterility confirmation:** Biological indicator (spore strip); chemical integrator (multi-parameter, responds to time + temperature + steam).
- **Water testing:** Membrane filtration on Endo agar (coliform count); MPN (most probable number) method if membrane filtration unavailable; H₂S strip test (presence/absence for fecal coliforms).
- **Malaria diagnosis:** Thick and thin blood smear, Giemsa stain, 1000× oil immersion. Sensitivity: ~5 parasites/µL (thick smear) by skilled reader.
- **TB diagnosis:** Sputum smear, Ziehl-Neelsen stain, 1000× oil immersion. Sensitivity: ~10,000 AFB/mL sputum. Three early-morning specimens increase yield by 15-20% over single specimen.
- **Cholera confirmation:** Stool culture on TCBS agar (yellow colonies); or hanging-drop motility (darting motility, inhibited by specific antiserum).
- **Antiseptic potency:** Iodine tincture titrated with sodium thiosulfate (iodometry) — confirm 4.5-5.5% w/v I₂.

### Sampling

- Wound infection rate: audit 1 in 20 closed wounds; track by procedure type and practitioner.
- Water quality: monthly sample from each water source and 5% of point-of-use taps/wells.
- Vaccination: monitor "take" rate per vaccine batch and vaccinator; investigate clusters of failures.

## Variations and Alternatives

- **Plant-derived antimicrobials (bootstrap default):** Cinchona (quinine), Artemisia (artemisinin), willow (salicin). Limited but effective for malaria, fever, pain. See [Pharmacology](pharmacology.md) for extraction.
- **Synthetic antibiotics (later stage, post-1935):** Sulfonamides (1935, Domagk), penicillin (1928 Fleming, mass-produced 1943), streptomycin (1943, Waksman — first-line for TB). Requires [industrial fermentation](../chemistry/index.md) capability for penicillin and streptomycin. Transform infectious disease mortality by 60-90%.
- **Sanitation (infrastructure):** [Clean water supply](sanitation.md), sewage disposal, handwashing stations. The most cost-effective infection-control intervention ever devised. Mortality reduction: 80-95% for waterborne disease.
- **Vaccination (programmatic):** Jenner smallpox vaccine (1796); Pasteur rabies (1885); typhoid (1896); cholera (1892); BCG for TB (1921). Requires cold chain for most modern vaccines (smallpox vaccine is the historical exception — stable as lyophilized powder).
- **Vector control:** Mosquito nets (reduces malaria incidence 50-70% in endemic areas when used consistently); draining standing water (destroys breeding sites); DDT if available (controversial — effective but persistent environmental damage).
- **Traditional and herbal medicine:** Many cultures have empirically effective plant medicines (e.g., Chinese Qinghao → artemisinin, Nobel Prize 2015). Respectful evaluation and integration where evidence supports. Not a substitute for sanitation or vaccination.
- **Honey wound dressings:** Hyperosmolar, low pH, produces H₂O₂. Effective against many bacteria including some antibiotic-resistant strains. Useful when no other antiseptic available. Medical-grade honey preferred (low water activity, no spores).
- **Maggot debridement:** Sterile Lucilia sericata larvae selectively consume necrotic tissue in chronic wounds. Effective for pressure ulcers and diabetic wounds; requires controlled fly cultivation.

### Disease Control Strategy Trade-off Comparison

| Strategy | Cost | Mortality reduction | Requires infrastructure | Best for |
|----------|------|---------------------|------------------------|----------|
| Clean water + sanitation | Medium | 80-95% (waterborne) | High (pipes, treatment) | Cities, towns |
| Handwashing + antiseptics | Very low | 30-50% (most infections) | Minimal | Any setting |
| ORS for diarrheal disease | Very low | 90% (diarrheal death) | Minimal | Any setting |
| Vaccination | Low-medium | 95-100% (vaccine-preventable) | Cold chain for most | Childhood programs |
| Antibiotics | Medium | 60-90% (bacterial) | Industrial fermentation | Post-bootstrap |
| Vector control | Low-medium | 50-70% (vector-borne) | Variable | Endemic areas |
| Quarantine / isolation | Low | Variable (epidemic control) | Enforcement | Outbreak response |

## References

- [Medicine & Surgery](medicine.md) — overview hub for all medical capabilities
- [Pharmacology](pharmacology.md) — drug extraction, preparation, dosing, and quality control
- [Surgery Basics](surgery-basics.md) — wound assessment, suturing, sterilization procedures
- [Emergency Care](emergency-care.md) — triage, hemorrhage control, burn and fracture management
- [Sanitation](sanitation.md) — clean water, sewage disposal, hygiene practices
- [Diagnostics](diagnostics.md) — physical examination, vital signs, laboratory testing
- [Pharmaceutical Production](pharmaceutical-production.md) — industrial-scale drug manufacturing including antibiotics
- [Water Treatment](water-treatment.md) — clean water for disease prevention
- [Chlor-Alkali Process](../chemistry/chlor-alkali.md) — chlorine and sodium hydroxide source for water disinfection

---

*Part of the [Bootciv Tech Tree](../index.md) • [Public Health, Sanitation & Medicine](./index.md) • [All Domains](../index.md)*
