# Medicine & Surgery

> **Node ID**: health.medicine
> **Domain**: [Health](./index.md)
> **Dependencies**: [`animals.beekeeping`](../animals/beekeeping.md), [`health.sanitation`](sanitation.md), [`knowledge.writing`](../knowledge/writing.md)
> **Enables**: [`health.pharmacology`](pharmacology.md), [`health.surgery-basics`](surgery-basics.md), [`health.diagnostics`](diagnostics.md)
> **Timeline**: Years 5-100+
> **Outputs**: surgical_capability, medical_treatment
> **Critical**: Yes — basic medical capability reduces preventable death more than any other single intervention


Medicine and surgery in a bootstrap civilization encompasses pharmaceutical production from plant and synthetic sources, basic surgical capability (wound management, fracture reduction, amputation), diagnostic examination, emergency procedures, and infection control. The foundational tier relies on plant-derived medicines and manual techniques; later stages add synthetic pharmaceuticals, laboratory diagnostics, and increasingly sophisticated surgical interventions.

Access to even basic medical capability — wound irrigation, fracture immobilization, antiseptic practice, and a handful of essential drugs (ether for anesthesia, morphine for pain, quinine for malaria) — dramatically reduces preventable death. Lister's introduction of antisepsis in 1867 alone cut surgical mortality from ~50% to ~15%. The gap between "no medical capability" and "basic wound care + essential drugs" is larger than the gap between "basic care" and "modern hospital medicine" in terms of lives saved.


## Pharmaceutical Materials

| Material | Source | Use |
|----------|--------|-----|
| Willow bark (Salix spp.) | Wild harvest | Salicin → salicylic acid (pain/fever) |
| Opium poppy latex | Cultivation | Morphine, codeine (analgesic) |
| Cinchona bark | Tropical cultivation | Quinine (anti-malarial) |
| Ephedra stems | Arid region harvest | Ephedrine (bronchodilator) |
| Digitalis (foxglove) leaves | Cultivation | Cardiac glycosides (heart failure) |
| Ethanol | Fermentation + distillation | Solvent, antiseptic, anesthetic adjunct |
| Sulfuric acid | Chemical manufacturing | Pharmaceutical synthesis |
| Acetic anhydride | Chemical manufacturing | Aspirin synthesis |
| Iodine | Seaweed ash or caliche | Antiseptic tincture |
| Gypsum (CaSO₄·2H₂O) | Mineral deposit | Plaster of Paris for casts |

## Surgical Materials

| Material | Use | Notes |
|----------|-----|-------|
| Catgut (sheep intestine) | Absorbable sutures | 7-14 day absorption |
| Silk thread | Non-absorbable sutures | Remove after 7-14 days |
| Cotton gauze | Wound dressings | Sterilized by boiling or autoclaving |
| Plaster bandages | Fracture immobilization | Dip in water, apply 5-12 layers |
| Adhesive tape | Wound closure, dressings | Fabric or paper backing with adhesive |
| Guttapercha | Dental fillings | Softens at 70°C, sets rigid at body temperature |

## Equipment

| Equipment | Purpose | Bootstrap Level |
|-----------|---------|----------------|
| Scalpel (forged steel) | Incisions, debridement | Basic metalworking |
| Forceps (toothed, smooth) | Tissue handling | Basic metalworking |
| Needle holder | Suturing | Basic metalworking |
| Hemostatic forceps | Vessel clamping | Basic metalworking |
| Retractors | Wound exposure | Basic metalworking |
| Syringe (glass/metal) | Irrigation, injection | Glass + metalworking |
| Stethoscope (wooden/metal tube) | Auscultation | Basic turning |
| Mercury thermometer | Temperature measurement | Glass blowing + mercury |
| Centrifuge (hand-cranked) | Blood separation | Metalworking |
| Compound microscope (100×, 400×, 1000×) | Diagnostics | Lens grinding |
| Autoclave / pressure cooker | Sterilization | Metal vessel + heat source |
| Bone saw | Amputation | Steel + woodworking tools |
| Tourniquet | Hemorrhage control | Cloth + stick windlass |


## Performing Wound Irrigation and Closure

1. **Assess the wound**: Determine depth, length, contamination level, and neurovascular status distal to the wound. Check for foreign bodies. Assess tetanus immunization status.
2. **Anesthetize if needed**: For large or deep wounds, provide local anesthesia (ether inhalation for general effect) or regional block if available.
3. **Irrigate**: Using a syringe (20-60 mL) with an 18-gauge needle, forcefully express clean (boiled then cooled) water or saline into the wound under pressure. Use 200-500 mL total volume. Direct the stream at the wound surface from 2-3 cm distance.
4. **Debride**: Remove necrotic tissue (gray/brown, no bleeding) with scalpel or scissors. Preserve viable tissue (bleeds when cut, muscle contracts when touched).
5. **Close or leave open**: Clean wounds <6 hours old → primary closure with sutures or adhesive strips. Contaminated wounds or >6 hours old → leave open for delayed closure at day 4-5, or heal by secondary intention.
6. **Dress**: Apply sterile cotton gauze over the wound. Secure with bandage. Change daily or when soaked.
7. **Monitor for infection**: Check daily for spreading redness, increasing pain, swelling, warmth, red streaks (lymphangitis), or fever. If infected → open wound, re-irrigate, apply antiseptic.

**Verification**: After wound closure, verify hemostasis (no active bleeding), approximation (wound edges touching without gaps), and neurovascular integrity distal to the wound (pulse present, sensation intact, motor function preserved). Document wound length, depth, and structures involved.

**Expected outcome**: Clean wounds closed within 6 hours heal by primary intention with <5% infection rate. Contaminated wounds left open for delayed closure at day 4-5 have <10% infection rate.

**Materials**: Syringe 20-60 mL with 18-gauge needle (generates ~8 psi irrigation pressure). Sterile saline or clean water, 200-500 mL per wound. Scalpel or scissors for debridement. Suture material (silk 3-0 or 4-0 for skin, catgut 2-0 for deep tissue).

**Strengths**:
- Pressurized irrigation removes >90% of wound bacteria mechanically — more effective than any antiseptic rinse
- Primary closure of clean wounds restores skin integrity within hours, reducing infection risk and speeding healing
- Technique requires only basic instruments and clean water — achievable at the earliest medical capability stage

**Weaknesses**:
- Wound closure timing is a judgment call — closing a contaminated wound seals bacteria inside, converting a treatable situation into a life-threatening infection
- Irrigation requires a syringe capable of generating adequate pressure — pouring water over a wound is ineffective
- Without antibiotics, post-closure infection requires reopening the wound, negating the benefit of primary closure

## Setting a Fracture (Closed Reduction)

1. **Assess**: Confirm fracture by deformity, crepitus, abnormal mobility, and pain. Check distal pulse, sensation, and motor function. If open fracture, treat as wound emergency first.
2. **Provide analgesia**: Administer morphine, ethanol, or ether anesthesia before manipulation.
3. **Apply traction**: Pull along the axis of the bone to disimpact fragments. Maintain steady longitudinal traction.
4. **Restore alignment**: Adjust angular and rotational deformity while maintaining traction. Compare to the uninjured limb for length, alignment, and rotation.
5. **Immobilize**: Apply plaster of Paris cast or wooden splints with cloth wrapping. For plaster: pad bony prominences with cotton, dip plaster bandages in water (20-25°C, 3-5 seconds), squeeze out excess, apply 5-12 layers, mold smoothly without wrinkles. Immobilize the joint above and below the fracture.
6. **Monitor**: Check distal circulation (pulse, capillary refill, sensation, warmth) after cast application. Instruct patient to report immediately if numbness, severe pain, or coldness develops distally (compartment syndrome).
7. **Follow up**: Recheck alignment at 1 week and 3 weeks. Typical healing: 6-8 weeks for simple fractures, 12+ weeks for weight-bearing bones.

**Verification**: After reduction and immobilization, verify five things: (1) distal pulse present, (2) capillary refill <2 seconds, (3) sensation intact distally, (4) toe/finger movement preserved, (5) no worsening pain. Recheck at 24 hours and 1 week. Persistent severe pain or absent pulse = compartment syndrome requiring immediate cast removal.

**Expected outcome**: Closed reduction achieves acceptable alignment in 80-90% of simple fractures. Clinical union (stable on gentle stress) at 6-8 weeks for upper extremity, 10-14 weeks for lower extremity. Full functional recovery at 3-6 months with rehabilitation.

**Materials**: Plaster of Paris bandages (gypsum plaster CaSO₄·½H₂O on cotton gauze, 10 cm width), dipped in water at 20-25°C. Cotton padding for bony prominences. Wooden splints (2.5 × 30 cm) as alternative when plaster is unavailable. Elastic or cloth bandage for wrapping.

**Strengths**:
- Closed reduction avoids surgical wound infection risk — no skin incision means no surgical site infection
- Plaster of Paris sets in 5-8 minutes and reaches full strength in 24-48 hours, providing rigid immobilization
- Technique requires no imaging — alignment verified by clinical examination and comparison to the uninjured limb

**Weaknesses**:
- Without X-ray verification, malalignment up to 15° angulation may go undetected, causing permanent deformity
- Plaster casts cause compartment syndrome if applied too tightly — this is a limb-threatening emergency
- Fracture reduction is painful — adequate analgesia (morphine, ether) is required before manipulation

## Performing START Triage

1. **Clear walking wounded**: Ask everyone who can walk to move to a designated area. Tag these patients **green (minor/delayed)**.
2. **Assess respirations** (non-ambulatory patients, <30 seconds each): Not breathing after airway repositioning → **black (expectant)**. Breathing >30/minute → **red (immediate)**. Breathing <30/minute → proceed.
3. **Assess perfusion**: Capillary refill >2 seconds or no radial pulse → **red (immediate)**. Adequate perfusion → proceed.
4. **Assess mental status**: Cannot follow simple commands → **red (immediate)**. Can follow commands → **yellow (urgent)**.
5. **Tag all patients**: Use colored tape, cloth strips, or marker. Re-triage every 30-60 minutes as conditions change.

**Verification**: After initial triage, reassess all patients in the immediate (red) and urgent (yellow) categories every 30 minutes. Patients who deteriorate get upgraded; patients who stabilize get downgraded. Document triage category and time on each patient.

**Expected outcome**: START triage categorizes 20-30 patients per minute per triage officer. Accuracy: correctly identifies >90% of patients needing immediate intervention. Over-triage rate (labeling stable patients as immediate): 15-25%, acceptable because the cost of under-triage (missing a dying patient) is much higher.

**Materials**: Colored tags or tape (red, yellow, green, black/white). Pen or marker for documenting time and category on each patient. Clipboard with triage reference card.

**Strengths**:
- Processes one patient in under 30 seconds — scales to mass casualty events with hundreds of patients
- Decision tree uses only three checks (respiration, perfusion, mental status) — no diagnostic equipment needed
- Walking wounded self-segregate in the first step, clearing the scene for immediate assessment of the non-ambulatory

**Weaknesses**:
- Sacrifices individual accuracy for throughput — some patients will be over-triaged or under-triaged
- Does not account for injuries that worsen over time (e.g., slow intracranial bleeding may not show mental status changes initially)
- Requires re-triage at regular intervals — initial categorization becomes stale within 30-60 minutes

## Safety & Hazards

**[Plant-derived medicines](../glossary/plant-derived-medicines.md)** (Foundations+):
- **Willow bark (salicin → salicylic acid → aspirin)**: Harvest bark from willow (Salix species) in spring when sap flows. Dry bark. Extract by boiling 30 g bark in 500 mL water for 15 minutes. Strain. Dose: 1 cup of decoction for pain/fever. Contains salicin (prodrug of salicylic acid). Later (Chemistry), synthesize acetylsalicylic acid (aspirin) from salicylic acid + acetic anhydride.
  - **[Aspirin synthesis](../glossary/aspirin-synthesis.md)** (Chemistry): Salicylic acid (from willow or Kolbe-Schmitt synthesis: phenol + CO₂ + NaOH at 125°C, 1 MPa → sodium salicylate → acidify) + acetic anhydride (from acetic acid + acetic acid → acetic anhydride) at 85°C for 15 minutes → acetylsalicylic acid + acetic acid. Crystallize from water. Filter, dry. Tablet with starch binder.
- **Opium poppy (morphine)**: Score unripe seed pods. Collect dried latex (opium). Contains morphine (potent analgesic) and codeine (mild analgesic, cough suppressant). Extremely valuable for surgery and severe pain. Highly addictive — controlled use only.
  - **[Morphine extraction](../glossary/morphine-extraction.md)** (Chemistry): Dissolve opium in hot water. Filter. Precipitate with NaOH → crude morphine base. Re-dissolve in HCl → morphine hydrochloride (water-soluble). Recrystallize for purity.
- **Cinchona bark (quinine)**: Anti-malarial. Extract by boiling bark in water. Quinine also treats arrhythmias. 8-10 g bark daily as decoction for malaria treatment.
- **Ephedra (ephedrine)**: Bronchodilator (asthma treatment), decongestant, vasoconstrictor. Extract by water decoction. Later synthesized chemically.
- **Digitalis (foxglove)**: Heart medication (increases contractility, slows rate). VERY narrow therapeutic window — easy to overdose. Use only under experienced guidance. Extract by steeping leaves in alcohol.

**Synthetic pharmaceuticals**:
- **Ether (diethyl ether)**: Anesthetic. Synthesize from ethanol + sulfuric acid at 130-140°C.
  - C₂H₅OH + H₂SO₄ → C₂H₅OSO₃H + H₂O (ethanol + sulfuric acid → ethyl hydrogen sulfate)
  - C₂H₅OSO₃H + C₂H₅OH → (C₂H₅)₂O + H₂SO₄ (ethyl hydrogen sulfate + ethanol → diethyl ether + sulfuric acid)
  - Distill ether off at 34.6°C. Collect in cold receiver. Store in dark, cool place (forms explosive peroxides on storage with air exposure). Use as general anesthetic via inhalation — induces unconsciousness in 5-10 minutes. Dose carefully — overdose causes respiratory arrest.
- **Chloroform (CHCl₃)**: Alternative anesthetic. Synthesize from acetone or ethanol + bleaching powder (Ca(OCl)₂) or from methane + chlorine (UV light catalyzed). Boiling point 61°C. Anesthetic by inhalation. Safer handling than ether (not flammable) but toxic to liver with repeated exposure.
- **Phenol (carbolic acid)**: First surgical antiseptic (Lister, 1867). From coal tar distillation (see Petrochemicals). Dilute to 2-5% solution for wound irrigation and instrument sterilization. Pure phenol causes chemical burns — handle with care.
- **Iodine tincture**: Extract iodine from seaweed ash (kelp) or caliche deposits (Chilean saltpeter). Dissolve in ethanol + KI solution (5% iodine, 10% KI in 70% ethanol). Apply to wounds as antiseptic. Stains brown — normal.
- **Hydrogen peroxide (H₂O₂)**: Antiseptic, wound cleaning. Produce by electrolysis of cold dilute sulfuric acid → peroxydisulfuric acid → hydrolysis → H₂O₂ + H₂SO₄. Distill under vacuum (bp 150°C at 1 atm — decomposes; distill at reduced pressure ~10 kPa, bp ~70°C). 3% solution for wound care. Store in dark bottle (decomposes in light).

## PPE Fabrication

**Eye protection**:
- **Safety glasses**: Flat glass lenses (from glass production) in wire or stamped metal frames. Side shields from leather or sheet metal. For grinding and cutting operations — prevent flying particles.
- **Goggles**: Soft leather or rubber frame with glass lenses. Seal against face. For chemical splash protection. Ventilated (small holes) to prevent fogging, but holes small enough to block splashes.
- **Welding goggles**: Very dark glass (didymium glass or smoke-tinted glass). Shields eyes from UV and intense visible light during welding/brazing.

**Respiratory protection**:
- **Simple cloth mask**: Multiple layers of tightly woven cotton over nose and mouth. Tie behind head. Reduces inhalation of dust and large particles. Not adequate for toxic gases or fine particulates.
- **Charcoal filter respirator**: Canister filled with activated charcoal granules (wood charcoal heated to 800-900°C in steam → porous, enormous surface area). Charcoal adsorbs organic vapors and many toxic gases. Rubber or leather face mask with exhale valve. Replace canister when breathing becomes difficult or odor detected inside mask.
- **HF-specific protection**: Full-face shield + rubber apron + neoprene or nitrile gloves (from Polymers polymer production). Respiratory protection mandatory. Calcium gluconate gel (2.5%) stations at every HF work area — apply immediately to any skin exposure, massaging into affected area for 15+ minutes. HF penetrates skin, binds calcium → cardiac arrest. Even small exposures can be lethal without treatment.

**Hand protection**:
- **Leather gloves**: Chrome-tanned or oil-tanned leather for mechanical protection (handling sharp metal, hot objects). Welding gloves: heavy leather, gauntlet length to elbow.
- **Chemical-resistant gloves**: Rubber (natural rubber latex or synthetic nitrile — see Polymers). Thickness 0.2-0.5 mm for dexterity, 0.5-1.0 mm for chemical handling. Check for pinholes before each use (inflate with air, submerge in water — bubbles indicate holes).

**Body protection**:
- **Leather aprons**: For blacksmithing, foundry work, welding. Heavy cowhide, waist to knee length.
- **Rubber aprons**: For chemical handling. Sheet rubber with neck loop and waist ties.
- **[Cleanroom garments](../glossary/cleanroom-garments.md)** (Photolithography): Woven synthetic coveralls, hoods, booties (from synthetic polymer fibers — see Polymers). Lint-free. Washed in ultra-pure water. Worn over street clothes. Changed every entry to cleanroom.

## Surgical Capability

**Wound treatment**:
- **Cleaning**: Irrigate wound with clean water (boiled then cooled). Remove debris. For deep wounds, irrigate under pressure (syringe with 18-gauge needle, 5-10 mL).
- **Closure**: Simple lacerations — bring edges together with adhesive strips (butterfly bandages from adhesive tape) or sutures (sterilized catgut or silk thread + curved needle). Catgut: made from sheep intestine, stretched, twisted, dried. Absorbs over 7-14 days. Silk: non-absorbable, remove after 7-14 days.
- **Dressing**: Sterile cloth (cotton gauze, autoclaved or boiled). Bandage to secure. Change daily or when soaked.
- **Infection signs**: Redness spreading from wound, increasing pain, swelling, warmth, red streaks (lymphangitis), fever. If infected — open wound, irrigate, apply antiseptic, consider honey (natural antibacterial — medical-grade honey has low water activity and produces hydrogen peroxide).

**Fracture management**:
- **Reduction**: Align bone ends manually (painful — administer ethanol or ether anesthesia first). Pull along axis of bone, restore alignment.
- **Immobilization**: Wooden splints + cloth wrapping, or plaster cast (gypsum plaster (CaSO₄·½H₂O) + water → sets hard in 10-15 minutes, full strength in 24-48 hours). Pad bony prominences with cotton before plaster application. Immobilize joint above and below fracture. X-ray verification unavailable — rely on clinical alignment and repeat examination.
- **Healing time**: 6-8 weeks for simple fractures, 12+ weeks for weight-bearing bones.

**[Basic surgery](../glossary/basic-surgery.md)** (with anesthesia):
- **Setup**: Clean room. Boil all instruments 20+ minutes (sterilization). Surgeon washes hands and forearms with soap and water, then soaks in 70% ethanol or 2% phenol solution. Sterile drapes over patient. Good lighting (focused oil lamp or, later, electric light).
- **Anesthesia**: Ether inhalation via mask (wire frame with cloth pad, drip ether onto pad). Monitor breathing — maintain steady depth. Too deep → respiratory arrest. Have bellows ready for assisted ventilation.
- **Procedures**: Amputation (last resort — guillotine method, tie off major vessels with catgut ligatures, flap skin over stump), abscess drainage (incise, pack with iodoform gauze), wound debridement (remove dead tissue), foreign body removal.
- **Post-operative**: Monitor for hemorrhage and infection. Keep wound clean and dry. Antibiotics not available until advanced microbiology — rely on antisepsis and natural healing.

## Gas Detection & Monitoring

**Simple detectors**:
- **Candle/flame test**: If flame flickers, dims, or extinguishes → oxygen displacement or toxic gas. Evacuate.
- **Canary/finch in cage**: Birds more sensitive to toxic gases (higher metabolic rate). Unconscious or dead bird → evacuate immediately. Morbid but effective.
- **Smell**: H₂S (rotten eggs), Cl₂ (pungent, bleach-like), NH₃ (sharp, irritating). BUT many dangerous gases are odorless (CO, CH₄ at low concentrations) or paralyze olfactory nerve at high concentrations (H₂S).

**Chemical detectors**:
- **Lead acetate paper**: Turns black in H₂S. Tape to hard hat or clip at breathing zone.
- **Draeger-style tubes**: Glass tube filled with chemical reagent, calibrated markings. Draw known air volume through tube with hand pump. Color change length indicates gas concentration. Available for CO, H₂S, Cl₂, NH₃, NO₂, SO₂, and many others.
- **Palladium chloride paper for CO**: Palladium chloride paper turns dark when CO present. Imprecise but gives warning.

## Dental Care

**Basic procedures**:
- **Extraction**: Extraction forceps (forged steel, angled jaws shaped to grip tooth root). Rock tooth buccolingually to widen socket, then lift. Control bleeding with gauze pressure pack. Indicated for gross decay, abscess, or crowding.
- **Fillings**: Clean decayed cavity with hand instruments (excavators, probes). Fill with softened gutta-percha (trans-polyisoprene from Palaquium gutta trees — a hard, non-elastic natural thermoplastic, not to be confused with elastic natural latex, softens at 70°C, sets rigid at body temperature) or beeswax (temporary). For permanent fillings: tin foil or gold foil (malleted into cavity — requires precision). Amalgam (mercury + silver-tin alloy) available at advanced Chemistry stage — durable but mercury toxicity requires careful handling.
- **Prevention**: Twigs of neem or willow for chewing (antibacterial, mechanical cleaning). Salt water rinse (9 g/L NaCl, warm) reduces gum inflammation.

## Basic Diagnostics

**Vital signs**:
- **Pulse**: Rate (beats/minute), rhythm (regular/irregular), strength (thready/bounding). Normal resting: 60-80 bpm. Fast (>100) = fever, blood loss, shock. Slow (<50) = hypothermia, certain poisonings. Irregular = heart disease.
- **Temperature**: Hand on forehead for rough check. Mercury thermometer: 35-42°C range, 0.1°C graduations. Normal: 36.5-37.5°C (oral). >38°C = fever. >40°C = hyperthermia (cool immediately — wet sheets, fanning). <35°C = hypothermia (warm gradually).
- **Urine analysis**: Color (dark = dehydration, red = blood, cloudy = infection). Odor. Volume. Dipstick tests: pH, protein, glucose, blood, nitrites. Sweet-smelling urine = diabetes (glucose — test with Benedict's solution, turns orange-red if sugar present).

**Triage categories**:
- **[Immediate](../glossary/immediate.md)** (red): Airway obstruction, massive hemorrhage, severe burns (>20% body surface), shock, tension pneumothorax. Treat within minutes.
- **[Urgent](../glossary/urgent.md)** (yellow): Fractures (open), moderate burns, significant bleeding (controlled), severe pain. Treat within 1-2 hours.
- **[Delayed](../glossary/delayed.md)** (green): Minor fractures, minor burns, superficial lacerations. Treat within 4-6 hours.
- **[Expectant](../glossary/expectant.md)** (black): Injuries incompatible with survival given available resources. Comfort measures only. Difficult but necessary when resources are limited.

## Diagnostic Examination Techniques

**Pulse examination**:
- **Rate**: Normal resting pulse 60-100 beats per minute in adults. Rate >100 bpm (tachycardia) indicates fever, blood loss, shock, pain, or anxiety. Rate <50 bpm (bradycardia) suggests hypothermia, heart block, or certain poisonings (opiates, organophosphates). Count for a full 60 seconds for accuracy, or 15 seconds and multiply by 4 if rhythm is regular.
- **Rhythm**: Regular rhythm is normal. Irregularly irregular suggests atrial fibrillation (common in elderly, valve disease). Regularly irregular suggests premature beats. Note any pauses or dropped beats.
- **Character (quality)**: Bounding pulse (strong, full) in fever, hyperthyroidism, anxiety. Thready pulse (weak, difficult to palpate) in shock, severe blood loss, heart failure. Wiry pulse (tense, narrow) in hypertension. Asymmetrical pulses between arms suggest aortic dissection (emergency).

**Percussion**:
- **Technique**: Press the distal phalanx of the middle finger of one hand firmly against the body surface. Strike this finger with the middle finger of the other hand, using a quick wrist flick (not arm motion). Listen to the produced sound.
- **Sound interpretation**: Resonant (low-pitched, hollow) over normal air-filled lung. Dull (high-pitched, flat) over consolidated lung (pneumonia), fluid (pleural effusion), or solid organs (liver, heart). Tympanitic (drum-like) over air-filled stomach or bowel. Stony dull over large pleural effusion.
- **Clinical utility**: Map the borders of the liver (normally spans 6-12 cm in the midclavicular line). Detect pleural effusion (dullness at the base that shifts with patient position). Identify consolidated lung segments in pneumonia.

**[Auscultation](../glossary/auscultation.md)** (requires stethoscope or improvised tube):
- **Heart sounds**: S1 (lubb, AV valve closure) and S2 (dubb, semilunar valve closure) are normal. S3 (ventricular gallop) indicates heart failure or volume overload. S4 (atrial gallop) indicates stiff ventricle (hypertension, aortic stenosis). Murmurs graded I (barely audible) through VI (audible with stethoscope off the chest). Timing: systolic (between S1 and S2) or diastolic (between S2 and S1). Location and radiation help identify the affected valve.
- **Breath sounds**: Vesicular (soft, rustling) normal over peripheral lung fields. Bronchial (harsh, tubular) over consolidated lung (pneumonia) — abnormal when heard in the periphery. Wheezing (high-pitched musical sounds) in asthma, bronchitis. Crackles/rales (discrete popping sounds) in pneumonia, pulmonary edema, fibrosis. Absent breath sounds in pleural effusion or pneumothorax.
- **Bowel sounds**: Normal active gurgling (5-35 per minute). Absent (ileus, peritonitis — listen for 2 full minutes before declaring absent). High-pitched tinkling (early bowel obstruction).

**Blood examination techniques**:
- **Hematocrit**: Draw capillary blood into a heparinized glass tube (75 mm length, 1 mm inner diameter). Seal one end with clay. Centrifuge at 10,000-15,000 RPM for 5 minutes. Read the packed cell layer as a fraction of total column length. Normal: 40-54% (males), 36-48% (females). Low hematocrit = anemia (blood loss, iron deficiency, chronic disease). High hematocrit = dehydration, polycythemia.
- **White blood cell count**: Fill hemocytometer chamber with diluted blood (1:20 dilution in white cell diluting fluid, which lyses red cells). Count cells in the four corner squares under microscope. Multiply by dilution factor and chamber factor. Normal: 4,000-11,000/μL. Elevated (leukocytosis) in bacterial infection, inflammation. Low (leukopenia) in viral infection, bone marrow suppression, severe sepsis.
- **Peripheral blood smear**: Drop of blood on glass slide, spread into thin film by a second slide held at 30° angle. Air dry. Stain with Wright's or Giemsa stain. Examine under oil immersion (1000×). Assess red cell morphology (size, shape, color), white cell differential (neutrophils, lymphocytes, monocytes, eosinophils, basophils), and platelet estimate.

## Wound Management in Detail

**Wound irrigation**:
- **Technique**: Use a syringe (20-60 mL) with an 18-gauge needle to irrigate under pressure. Apply 8-12 psi by forcefully expressing the syringe. Use 200-500 mL of clean (boiled then cooled) water or sterile saline. Direct the stream at the wound surface from 2-3 cm distance. Irrigation pressure matters more than solution type — mechanical removal of bacteria and debris does the heavy lifting.
- **Solutions**: Clean water is nearly as effective as sterile saline for wound irrigation. Dilute povidone-iodine solution (1%) adds antibacterial activity. Do NOT use hydrogen peroxide for wound irrigation (it damages healthy tissue and has minimal antimicrobial benefit in wounds).

**Debridement**:
- **Purpose**: Remove necrotic (dead) tissue, foreign material, and contaminated tissue from wounds. Dead tissue is a breeding ground for bacteria and prevents healing.
- **Technique**: Sharp debridement with scalpel or scissors. Excise non-viable tissue (gray/brown color, no bleeding when cut, dull consistency) until healthy bleeding tissue is reached. Preserve viable muscle (contracts when touched) and tendon. Autolytic debridement (moist dressings that allow the body's own enzymes to dissolve dead tissue) is slower but less painful.

**Wound closure timing**:
- **[Primary closure](../glossary/primary-closure.md)** (within 6 hours of injury, "primary intention"): Clean wounds with sharp edges (surgical incisions, fresh lacerations from clean objects). Irrigate, debride if needed, suture or staple. Approximate wound edges without tension. Success depends on thorough cleaning.
- **[Delayed primary closure](../glossary/delayed-primary-closure.md)** (4-5 days after injury): For contaminated wounds that have been cleaned and observed for signs of infection. If no infection develops by day 4-5, close the wound. Combines safety of open wound management with cosmetic/functional benefit of closure.
- **[Secondary intention](../glossary/secondary-intention.md)** (leave open to heal by granulation): For heavily contaminated wounds, bites, crush injuries, or wounds older than 6-8 hours. Wound fills with granulation tissue from the base upward. Slower but safer for high-infection-risk wounds.

## Fracture Management Detail

**Reduction**:
- **Closed reduction**: Manipulate bone ends externally to restore alignment. Apply longitudinal traction (pull along the bone axis) to disimpact fragments. Then adjust angular and rotational alignment. Check alignment by comparing to the uninjured limb (length, alignment, rotation). Provide analgesia (ether, morphine, or ethanol) before reduction.
- **[Open reduction](../glossary/open-reduction.md)** (requires surgical capability): Expose fracture site surgically, realign bone ends under direct vision. Required for fractures where closed reduction fails, where bone fragments are interposed with soft tissue, or where the fracture involves a joint surface. Higher risk of infection.

**Plaster of Paris immobilization**:
- **Material**: Gypsum plaster (CaSO₄·½H₂O), produced by heating gypsum (CaSO₄·2H₂O) to 120-180°C to drive off three-quarters of the water. When mixed with water, it rehydrates and sets hard (exothermic, reaches ~50°C during setting).
- **Application**: Roll plaster-impregnated bandages (or dip dry plaster bandages in water at 20-25°C for 3-5 seconds, squeeze out excess). Apply 5-8 layers for upper extremity casts, 8-12 layers for lower extremity. Mold smoothly without wrinkles (wrinkles cause pressure sores). Pad all bony prominences (elbow, wrist, heel, ankle) with cotton or felt before plaster application.
- **Setting time**: Initial set in 5-8 minutes. Full strength in 24-48 hours (keep cast dry during this period). Patients must be warned about compartment syndrome (severe pain, numbness, pallor, pulselessness distal to cast) — requires immediate cast removal or bivalving.

## Infection Management

**Wound antisepsis**:
- **Ethanol**: 70% concentration (by weight) is optimal. Applied to intact skin before procedures. Denatures bacterial proteins and disrupts cell membranes. Not effective against spores or some viruses. Fast-acting (15-30 seconds contact). Flammable.
- **Povidone-iodine (Betadine)**: 2.5% iodine in a polymer carrier (povidone). Broad-spectrum: bacteria (including MRSA), fungi, viruses, spores (with prolonged contact). Applied to intact skin and mucous membranes. Less irritating than tincture of iodine. Inactivated by blood and organic material — clean wound before applying. Do not use on large open wounds or burns (systemic iodine absorption causes thyroid dysfunction).
- **Chlorhexidine 4%**: Persistent antimicrobial activity (remains effective on skin for hours after application). More effective than povidone-iodine for surgical hand scrubs. Not effective against spores. Rare allergic reactions. Less inactivated by blood than iodine. Used for surgical site preparation and hand hygiene.


## Safety & Hazards

- **Infection risk**: Surgical and wound care procedures carry infection risk. Sterilize instruments (boil 20+ minutes minimum, or autoclave at 121°C for 15 minutes). Wash hands before any wound contact. Clean wounds thoroughly before dressing.
- **Drug overdose**: Many pharmaceutical compounds have narrow therapeutic windows. Weigh all drugs on accurate scales. Start with lowest effective dose. Digitalis, morphine, and ether have particularly dangerous overdose profiles.
- **Surgical complications**: Amputation and major procedures risk hemorrhage and shock. Apply tourniquet before amputation (release every 30 minutes to prevent tissue death). Have ligatures ready for major vessels. Monitor for shock (pale, cold, rapid pulse — treat with warmth, head-down position, fluid replacement).
- **Mercury toxicity**: If mercury compounds are used (topical antiseptics, syphilis treatment), they are cumulative neurotoxins. Limit exposure. Never heat mercury. Use in ventilated areas.
- **Ether explosion risk**: Ether is highly flammable and forms explosive peroxides on storage. No flames, sparks, or electrical equipment in anesthesia area. Ventilate to prevent vapor accumulation.

## Emergency Procedures

**Hemorrhage control**:
- **Direct pressure**: Apply firm manual pressure to the wound with a clean cloth or gauze pad. Maintain continuous pressure for at least 10-15 minutes without lifting to check (lifting disrupts the forming clot). This stops 90% of external hemorrhage.
- **Tourniquet**: Apply only when direct pressure fails (typically for arterial hemorrhage of a limb). Place 5-10 cm above the wound, never over a joint. Tighten until bleeding stops. Note the application time prominently on the patient. Do not remove in the field. Tourniquet ischemia time: safe for 2 hours with minimal risk; increasing muscle damage after 4-6 hours. Loosen tourniquet periodically (every 30 minutes for 30 seconds) if evacuation will take more than 2 hours, but only if direct pressure can control bleeding during loosening.
- **Pressure points**: Compress the supplying artery against underlying bone. Femoral artery (groin crease, for thigh/leg wounds). Brachial artery (medial upper arm, for forearm/hand wounds). Temporal artery (in front of ear, for scalp wounds). Maintain pressure point compression while also applying direct wound pressure.

**Burn management**:
- **Classification**: First degree (erythema, pain, no blisters — sunburn). Second degree (partial-thickness, blisters, intense pain, moist wound bed). Third degree (full-thickness, white/brown/black eschar, painless because nerve endings destroyed).
- **[Fluid resuscitation](../glossary/fluid-resuscitation.md)** (Parkland formula for burns >20% body surface area): 4 mL lactated Ringer's (or 0.9% NaCl) × kg body weight × %BSA burned. Give half in the first 8 hours from the time of burn, the remaining half over the next 16 hours. Monitor urine output (target 0.5-1.0 mL/kg/hour as indicator of adequate resuscitation).
- **Wound care**: Cool burn with running water (15-20°C) for 20 minutes (effective up to 3 hours post-burn). Do NOT apply ice (causes frostbite on top of the burn). Apply non-adherent dressing (petrolatum gauze). Do NOT burst blisters (intact blister is a sterile biological dressing). Escharotomy (longitudinal incisions through burned skin) for circumferential burns of limbs or chest that restrict circulation or breathing.

**Shock management**:
- **Signs**: Tachycardia (>100 bpm), hypotension (systolic <90 mmHg), cool clammy skin, delayed capillary refill (>2 seconds), reduced urine output, anxiety/confusion.
- **Position**: Lay patient flat with legs elevated 30° (Trendelenburg position) to increase venous return to the heart. Keep warm with blankets (shocked patients lose thermoregulation).
- **Fluid resuscitation**: If IV access is available, administer lactated Ringer's or 0.9% NaCl rapidly (1-2 L in the first hour). If no IV capability, oral rehydration with salt-sugar solution (1 L water + 6 level teaspoons sugar + ½ level teaspoon salt) if the patient is conscious and can swallow.
- **Cause identification**: Hypovolemic (blood loss, dehydration — most common), cardiogenic (heart failure), septic (infection), anaphylactic (allergic reaction). Treatment differs by cause; fluid resuscitation is the universal first step for hypovolemic and septic shock.

## Basic Laboratory Setup

**Equipment for a rudimentary medical laboratory**:
- **Microscope**: Brightfield compound microscope with 10×, 40×, and 100× (oil immersion) objectives. Eyepiece 10× gives total magnifications of 100×, 400×, and 1000×. Used for: blood smears (malaria parasites, blood cell morphology), urine sediment (cells, crystals, casts), sputum (acid-fast bacteria for TB), stool (parasites, ova). Illumination: mirror (daylight) or LED/lamp. Requires glass slides and coverslips.
- **Centrifuge**: Hand-cranked or electric, 3,000-5,000 RPM. For separating blood cells from plasma (hematocrit tubes), concentrating urine sediment, and separating serum for chemistry tests. Balance tubes by weight before spinning (unequal loading causes vibration and tube breakage).
- **Incubator**: Maintain 35-37°C for bacterial cultures. Simple design: insulated box with thermometer and heat source (electric lamp or hot water bottle). Temperature stability ±1°C. Used for urine culture, blood culture, water testing.
- **Autoclave or pressure cooker**: 121°C at 15 psi for 15 minutes sterilizes instruments, culture media, and glassware. Essential for sterile technique in any laboratory or surgical setting.
- **Reagents**: Benedict's solution (glucose detection in urine — blue to orange-red on heating), iodine solution (starch detection), Gram stain reagents (crystal violet, iodine, safranin, ethanol for bacterial classification), Wright's stain (blood smear differential count).

**Simple chemistry tests**:
- **Urine glucose**: Add 8 drops Benedict's solution to 5 mL urine. Heat in boiling water bath for 5 minutes. Blue (negative) → green (trace) → yellow (+) → orange (++) → red-orange (+++) → brick red (++++). Quantitative estimate: trace ~0.25%, + ~0.5%, ++ ~1.0%, +++ ~2.0%, ++++ >2.0% glucose.
- **Urine protein**: Add 1 mL 20% sulfosalicylic acid to equal volume of clear urine. Cloudiness indicates protein present. Grade 0 (clear, negative) to 4+ (dense precipitate). Persistent proteinuria suggests kidney disease.
- **Hemoglobin**: Add a drop of blood to guaiac-impregnated paper, then add hydrogen peroxide. Blue color indicates hemoglobin (blood in stool — occult blood screening for gastrointestinal bleeding). False positives from red meat and certain vegetables; restrict diet before testing.

## Medical Instrument Sterilization

**Methods by capability level**:
- **Boiling**: Submerge instruments in boiling water for 20+ minutes. Kills most bacteria and viruses. Does NOT kill bacterial spores (Clostridium tetani, C. perfringens, B. anthracis). Acceptable for instruments used in low-risk procedures (wound care, injections) when no better method is available.
- **Pressure cooking (autoclaving)**: 121°C at 15 psi for 15 minutes. Kills all microorganisms including spores. Wrap instruments in cloth or place in sterilization pouches before autoclaving. The gold standard for sterilization. Verify effectiveness with indicator tape (changes color at sterilization temperature) or biological indicators (spore strips cultured after autoclaving — no growth = successful sterilization).
- **Chemical sterilization**: Soak clean instruments in 2% glutaraldehyde solution for 10 hours (kills all microorganisms including spores). Rinse thoroughly with sterile water before use. Glutaraldehyde is toxic and irritating to skin and respiratory tract — use in a fume hood with gloves. Alternative: 6-8% hydrogen peroxide solution for 6 hours.
- **Dry heat**: 160°C for 2 hours or 170°C for 1 hour in a dry oven. Suitable for oils, powders, and instruments that corrode in steam. No corrosion risk, but takes much longer than autoclaving. Must use glass or metal containers (paper and cloth char at these temperatures).

## Mass Casualty Triage

**START (Simple Triage and Rapid Treatment) protocol**:
- **Step 1**: Ask everyone who can walk to move to a designated area. Those who comply are tagged **green (minor/delayed)**. This clears the immediate scene and identifies the walking wounded in seconds.
- **Step 2**: Assess remaining non-ambulatory patients using three rapid checks, spending no more than 30 seconds per patient:
  - **Respirations**: Not breathing after airway repositioning → **black (expectant/deceased)**. Breathing >30 per minute → **red (immediate)**. Breathing <30 per minute → proceed to next check.
  - **Perfusion**: Capillary refill >2 seconds, or no palpable radial pulse → **red (immediate)**. Adequate perfusion → proceed to next check.
  - **Mental status**: Unable to follow simple commands (e.g., "squeeze my hand") → **red (immediate)**. Can follow commands → **yellow (urgent/delayed)**.
- **Key principle**: START sorts patients into four categories in under 30 seconds each. It sacrifices individual accuracy for throughput. Re-triage periodically as conditions change and resources shift. Tag all patients with color-coded markers (colored tape, cloth strips, or marker on forehead) so all responders share a common system.

## Limitations

- **No antibiotics**: Until advanced microbiology and industrial fermentation are established, bacterial infections cannot be treated systemically. Reliance on antisepsis, wound drainage, and the body's immune response limits treatable conditions. A wound infection that would be cured with a course of penicillin in modern medicine may become lethal.
- **No blood transfusion**: Without blood banking (anticoagulant preservation, typing, cross-matching, refrigerated storage), severe hemorrhage can only be managed with fluid replacement (saline, oral rehydration). Blood loss exceeding 30% of total blood volume (approximately 1.5 L in an adult) is likely fatal without transfusion.
- **No imaging**: X-ray, ultrasound, CT, and MRI are unavailable until advanced electronics and physics capabilities are established. Fracture alignment is assessed clinically (not radiographically). Internal injuries are diagnosed by physical examination alone. Tumors, abscesses, and foreign bodies are located by palpation and percussion.
- **Narrow pharmaceutical range**: Plant-derived medicines provide analgesics (morphine, salicin), anti-malarials (quinine), and a few cardiac drugs (digitalis). Synthetic pharmaceuticals require an established chemical industry. Many diseases (diabetes, hypertension, most cancers, autoimmune disorders) have no effective treatment in the bootstrap period.
- **Anesthesia risks**: Ether and chloroform anesthesia have narrow therapeutic windows. Overdose causes respiratory arrest. Ether is highly flammable — no flames or sparks in the anesthesia area. Chloroform causes liver toxicity with repeated exposure. Without mechanical ventilation, assisted breathing relies on manual bellows.
- **Infection control limits**: Aseptic technique reduces surgical infection rates dramatically, but sterility is never absolute. Without antibiotics, post-operative infection remains a leading cause of surgical mortality. Wound care in field conditions (dust, flies, contaminated water) is inherently higher risk than in a controlled surgical theater.
- **Dental care limitations**: Without modern filling materials (composite resins, ceramics) and radiography, dental treatment is limited to extraction and temporary fillings. Preventive care (cleaning, fluoride) and endodontics (root canal) are not available at the bootstrap level.

## See Also

- [Water Treatment (Health)](water-treatment.md) — clean water for disease prevention
- [Sanitation](sanitation.md) — sewage disposal, hygiene practices, waste management
- [Medical Instruments](medical-instruments.md) — diagnostic and surgical instrument fabrication
- [Pharmacology](pharmacology.md) — drug extraction, preparation, dosing, and quality control
- [Occupational Health](occupational-health.md) — workplace hazard identification and control
- [Acids and Bases](../chemistry/acids-bases.md) — sulfuric acid, hydrochloric acid production for pharmaceutical synthesis
- [Energy](../energy/index.md) — power for autoclaves, centrifuges, microscopes



[← Back to Health](index.md)
