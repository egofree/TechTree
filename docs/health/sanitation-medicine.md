# Public Health, Sanitation & Medicine

> **Node ID**: `health`
> **Domain**: [Public Health, Sanitation & Medicine](./)
> **Dependencies**: `chemistry`, `foundations`
> **Timeline**: Years 0-200+
> **Outputs**: clean_water, sanitation, pharmaceuticals, ppe, surgical_capability, gas_detection, quarantine_protocols

## Problem

Industrial work is dangerous. Chemical processing (Chemistry+) involves lethal substances (HF acid, toxic gases, heavy metals). Mining, metalworking, and construction carry injury risks. Epidemics can decimate specialist populations. Losing experienced practitioners sets the project back years.

## Technologies &amp; Systems

### Water Supply &amp; Purification

**Well construction**:
- **Dug wells**: Hand-dug 1-2 m diameter, 5-20 m deep. Line with stone or brick (dry-laid, mortar at top to prevent surface contamination). Cover with wooden or stone cap. Rope and bucket for drawing. Locate uphill and ≥30 m from latrines, graves, animal pens.
- **Driven wells** (Machine Tools+): Drive steel pipe (3-5 cm diameter) with pointed screen tip into ground using sledge hammer or drop weight. Fast, works in sandy/gravelly soil. Depth 5-15 m. Attach hand pump.
- **Water testing**: Simple clarity test (clear jar — no cloudiness). Boil sample — no unusual smell. Soap test — if soap lathers easily, water is relatively soft (low calcium/magnesium). If scum forms, water is hard (not dangerous but affects washing and boiler operation).

**Filtration**:
- **Slow sand filter**: Large watertight tank (2-4 m deep). Bottom layer: graded gravel (30 cm). Top layer: fine sand (1-1.5 m). Pour raw water on top. Water percolates down through sand. Biological layer (schmutzdecke) forms on sand surface — microorganisms consume bacteria and organic matter. Flow rate: 0.1-0.4 m/hour. Output: 2-4 liters/minute per m² of filter surface. Very effective — removes 95-99% of bacteria. Clean periodically by scraping top 1-2 cm of sand, wash and replace.
- **Rapid sand filter** (Chemistry+): Coarser sand, higher flow rate (5-15 m/hour). Requires chemical pre-treatment (coagulation with alum — aluminum sulfate, then settling). Less biological, more physical filtration. Backwash with compressed air and water to clean.

**Chlorination** (Chemistry+):
- **Bleach production**: Pass chlorine gas (from electrolysis of NaCl — chlor-alkali process) through cold NaOH solution → sodium hypochlorite (NaOCl, bleach). 5-15% concentration.
- **Dosage**: 1-3 mg/L free chlorine residual. Test with starch-iodide paper or orthotolidine reagent (turns yellow in presence of chlorine). Contact time ≥30 minutes. Chlorine kills bacteria and most viruses.
- **Alternative**: Boil water vigorously for 1+ minute (5+ minutes at altitude >2000 m). Simple, effective, fuel-intensive.

### Sewage &amp; Waste Disposal

**Latrines**:
- **Pit latrine**: Dig pit 1 m diameter × 3-5 m deep. Platform with hole on top. Privacy enclosure. Add lime or ash after each use to reduce odor and flies. When pit is ½ full, fill with soil, relocate. Simple, effective for small populations.
- **Aqua privy**: Watertight tank with water seal. Waste drops into water, anaerobically decomposes. Effluent drains to soakaway. Better odor control. Requires water supply.

**Sewage treatment** (larger settlements):
- **Settling tanks (primary treatment)**: Large tank, 2-4 hour retention. Solids settle to bottom as sludge. Remove sludge periodically via valve at bottom. Sludge dries on sand beds, used as fertilizer (after composting to kill pathogens — 6+ months).
- **Biological treatment (secondary)**: Trickling filter — wastewater sprinkled over bed of rocks (1-3 m deep). Biofilm on rocks consumes organic matter. Or activated sludge — aerate wastewater in tank (blow air through diffusers). Microorganisms consume organics. Settle, return some sludge to tank, discharge clear effluent.

**Industrial waste**:
- **Acid/alkali neutralization**: Acid waste + limestone (CaCO₃) or lime (CaO) → neutral salt + CO₂. Alkaline waste + dilute acid → neutral salt. Always add acid TO water, never water TO acid (violent boiling/splashing).
- **Heavy metals**: Precipitate with NaOH or Na₂S → metal hydroxide or sulfide sludge. Collect, store, potentially recover metal.
- **Never discharge** HF, cyanide, or strong oxidizers to waterways. Neutralize or contain in sealed vessels.

### Hygiene &amp; Prevention

**Handwashing**: Soap + running water. Scrub all surfaces for 20+ seconds. Dry with clean cloth or air dry. Required before eating, after latrine use, before wound care, before food preparation. Soap making: animal fat + lye (NaOH from leached wood ash — see Chemistry) → soap + glycerol. Saponification at 60-80°C for 1-2 hours. Pour into molds. Cure 4-6 weeks.

**Quarantine protocols**:
- Isolate symptomatic individuals immediately. Separate shelter, dedicated caretaker (wearing mask and gloves). 14-40 day quarantine period depending on disease. Monitor contacts for symptoms. Burn or boil contaminated materials.
- **Entry screening**: For any new person joining the settlement — 14-day observation period before integration. Check for fever, cough, rash, diarrhea.

**Food safety**:
- **Preservation**: Salting (20-25% salt by weight — dehydrates bacteria), smoking (antimicrobial compounds in smoke, drying effect), drying (sun-dry fruit, meat, grain — moisture content below 15%), fermentation (lactic acid in sauerkraut, vinegar pickling), cooling (underground root cellars at 5-10°C).
- **Water for food prep**: Always use treated/boiled water. Cook meat thoroughly (internal temperature ≥70°C). Keep food covered. Consume prepared food within 4-6 hours or reheat to ≥70°C.
- **Storage**: Dry, cool, pest-proof (sealed clay jars, raised platforms). Rotate stock (first in, first out).

### Pharmaceutical Production

**Plant-derived medicines** (Foundations+):
- **Willow bark (salicin → salicylic acid → aspirin)**: Harvest bark from willow (Salix species) in spring when sap flows. Dry bark. Extract by boiling 30 g bark in 500 mL water for 15 minutes. Strain. Dose: 1 cup of decoction for pain/fever. Contains salicin (prodrug of salicylic acid). Later (Chemistry), synthesize acetylsalicylic acid (aspirin) from salicylic acid + acetic anhydride.
  - **Aspirin synthesis** (Chemistry): Salicylic acid (from willow or Kolbe-Schmitt synthesis: phenol + CO₂ + NaOH at 125°C, 1 MPa → sodium salicylate → acidify) + acetic anhydride (from acetic acid + acetic acid → acetic anhydride) at 85°C for 15 minutes → acetylsalicylic acid + acetic acid. Crystallize from water. Filter, dry. Tablet with starch binder.
- **Opium poppy (morphine)**: Score unripe seed pods. Collect dried latex (opium). Contains morphine (potent analgesic) and codeine (mild analgesic, cough suppressant). Extremely valuable for surgery and severe pain. Highly addictive — controlled use only.
  - **Morphine extraction** (Chemistry): Dissolve opium in hot water. Filter. Precipitate with NaOH → crude morphine base. Re-dissolve in HCl → morphine hydrochloride (water-soluble). Recrystallize for purity.
- **Cinchona bark (quinine)**: Anti-malarial. Extract by boiling bark in water. Quinine also treats arrhythmias. 8-10 g bark daily as decoction for malaria treatment.
- **Ephedra (ephedrine)**: Bronchodilator (asthma treatment), decongestant, vasoconstrictor. Extract by water decoction. Later synthesized chemically.
- **Digitalis (foxglove)**: Heart medication (increases contractility, slows rate). VERY narrow therapeutic window — easy to overdose. Use only under experienced guidance. Extract by steeping leaves in alcohol.

**Synthetic pharmaceuticals** (Chemistry+):
- **Ether (diethyl ether)**: Anesthetic. Synthesize from ethanol + sulfuric acid at 130-140°C.
  - C₂H₅OH + H₂SO₄ → C₂H₅OSO₃H + H₂O (ethanol + sulfuric acid → ethyl hydrogen sulfate)
  - C₂H₅OSO₃H + C₂H₅OH → (C₂H₅)₂O + H₂SO₄ (ethyl hydrogen sulfate + ethanol → diethyl ether + sulfuric acid)
  - Distill ether off at 34.6°C. Collect in cold receiver. Store in dark, cool place (forms explosive peroxides on storage with air exposure). Use as general anesthetic via inhalation — induces unconsciousness in 5-10 minutes. Dose carefully — overdose causes respiratory arrest.
- **Chloroform (CHCl₃)**: Alternative anesthetic. Synthesize from acetone or ethanol + bleaching powder (Ca(OCl)₂) or from methane + chlorine (UV light catalyzed). Boiling point 61°C. Anesthetic by inhalation. Safer handling than ether (not flammable) but toxic to liver with repeated exposure.
- **Phenol (carbolic acid)**: First surgical antiseptic (Lister, 1867). From coal tar distillation (see Petrochemicals). Dilute to 2-5% solution for wound irrigation and instrument sterilization. Pure phenol causes chemical burns — handle with care.
- **Iodine tincture**: Extract iodine from seaweed ash (kelp) or caliche deposits (Chilean saltpeter). Dissolve in ethanol + KI solution (5% iodine, 10% KI in 70% ethanol). Apply to wounds as antiseptic. Stains brown — normal.
- **Hydrogen peroxide (H₂O₂)**: Antiseptic, wound cleaning. Produce by electrolysis of cold dilute sulfuric acid → peroxydisulfuric acid → hydrolysis → H₂O₂ + H₂SO₄. Distill under vacuum (bp 150°C at 1 atm — decomposes; distill at reduced pressure ~10 kPa, bp ~70°C). 3% solution for wound care. Store in dark bottle (decomposes in light).

### PPE Fabrication

**Eye protection**:
- **Safety glasses**: Flat glass lenses (from the Metallurgy stage glass production) in wire or stamped metal frames. Side shields from leather or sheet metal. For grinding and cutting operations — prevent flying particles.
- **Goggles**: Soft leather or rubber frame with glass lenses. Seal against face. For chemical splash protection. Ventilated (small holes) to prevent fogging, but holes small enough to block splashes.
- **Welding goggles**: Very dark glass (didymium glass or smoke-tinted glass). Shields eyes from UV and intense visible light during welding/brazing.

**Respiratory protection**:
- **Simple cloth mask**: Multiple layers of tightly woven cotton over nose and mouth. Tie behind head. Reduces inhalation of dust and large particles. Not adequate for toxic gases or fine particulates.
- **Charcoal filter respirator** (Chemistry+): Canister filled with activated charcoal granules (wood charcoal heated to 800-900°C in steam → porous, enormous surface area). Charcoal adsorbs organic vapors and many toxic gases. Rubber or leather face mask with exhale valve. Replace canister when breathing becomes difficult or odor detected inside mask.
- **HF-specific protection**: Full-face shield + rubber apron + neoprene or nitrile gloves (from Polymers polymer production). Respiratory protection mandatory. Calcium gluconate gel (2.5%) stations at every HF work area — apply immediately to any skin exposure, massaging into affected area for 15+ minutes. HF penetrates skin, binds calcium → cardiac arrest. Even small exposures can be lethal without treatment.

**Hand protection**:
- **Leather gloves**: Chrome-tanned or oil-tanned leather for mechanical protection (handling sharp metal, hot objects). Welding gloves: heavy leather, gauntlet length to elbow.
- **Chemical-resistant gloves** (Chemistry+): Rubber (natural rubber latex or synthetic nitrile — see Polymers). Thickness 0.2-0.5 mm for dexterity, 0.5-1.0 mm for chemical handling. Check for pinholes before each use (inflate with air, submerge in water — bubbles indicate holes).

**Body protection**:
- **Leather aprons**: For blacksmithing, foundry work, welding. Heavy cowhide, waist to knee length.
- **Rubber aprons** (Chemistry+): For chemical handling. Sheet rubber with neck loop and waist ties.
- **Cleanroom garments** (Photolithography): Woven synthetic coveralls, hoods, booties (from Polymers polymer fibers). Lint-free. Washed in ultra-pure water. Worn over street clothes. Changed every entry to cleanroom.

### Surgical Capability

**Wound treatment**:
- **Cleaning**: Irrigate wound with clean water (boiled then cooled). Remove debris. For deep wounds, irrigate under pressure (syringe with 18-gauge needle, 5-10 mL).
- **Closure**: Simple lacerations — bring edges together with adhesive strips (butterfly bandages from adhesive tape) or sutures (sterilized catgut or silk thread + curved needle). Catgut: made from sheep intestine, stretched, twisted, dried. Absorbs over 7-14 days. Silk: non-absorbable, remove after 7-14 days.
- **Dressing**: Sterile cloth (cotton gauze, autoclaved or boiled). Bandage to secure. Change daily or when soaked.
- **Infection signs**: Redness spreading from wound, increasing pain, swelling, warmth, red streaks (lymphangitis), fever. If infected — open wound, irrigate, apply antiseptic, consider honey (natural antibacterial — medical-grade honey has low water activity and produces hydrogen peroxide).

**Fracture management**:
- **Reduction**: Align bone ends manually (painful — administer ethanol or ether anesthesia first). Pull along axis of bone, restore alignment.
- **Immobilization**: Wooden splints + cloth wrapping, or plaster cast (gypsum plaster (CaSO₄·½H₂O) + water → sets hard in 10-15 minutes, full strength in 24-48 hours). Pad bony prominences with cotton before plaster application. Immobilize joint above and below fracture. X-ray verification unavailable — rely on clinical alignment and repeat examination.
- **Healing time**: 6-8 weeks for simple fractures, 12+ weeks for weight-bearing bones.

**Basic surgery** (with anesthesia):
- **Setup**: Clean room. Boil all instruments 20+ minutes (sterilization). Surgeon washes hands and forearms with soap and water, then soaks in 70% ethanol or 2% phenol solution. Sterile drapes over patient. Good lighting (focused oil lamp or, later, electric light).
- **Anesthesia**: Ether inhalation via mask (wire frame with cloth pad, drip ether onto pad). Monitor breathing — maintain steady depth. Too deep → respiratory arrest. Have bellows ready for assisted ventilation.
- **Procedures**: Amputation (last resort — guillotine method, tie off major vessels with catgut ligatures, flap skin over stump), abscess drainage (incise, pack with iodoform gauze), wound debridement (remove dead tissue), foreign body removal.
- **Post-operative**: Monitor for hemorrhage and infection. Keep wound clean and dry. Antibiotics not available until advanced microbiology — rely on antisepsis and natural healing.

### Gas Detection &amp; Monitoring

**Simple detectors**:
- **Candle/flame test**: If flame flickers, dims, or extinguishes → oxygen displacement or toxic gas. Evacuate.
- **Canary/finch in cage**: Birds more sensitive to toxic gases (higher metabolic rate). Unconscious or dead bird → evacuate immediately. Morbid but effective.
- **Smell**: H₂S (rotten eggs), Cl₂ (pungent, bleach-like), NH₃ (sharp, irritating). BUT many dangerous gases are odorless (CO, CH₄ at low concentrations) or paralyze olfactory nerve at high concentrations (H₂S).

**Chemical detectors** (Chemistry+):
- **Lead acetate paper**: Turns black in H₂S. Tape to hard hat or clip at breathing zone.
- **Draeger-style tubes**: Glass tube filled with chemical reagent, calibrated markings. Draw known air volume through tube with hand pump. Color change length indicates gas concentration. Available for CO, H₂S, Cl₂, NH₃, NO₂, SO₂, and many others.
- **Limulus paper for CO**: Palladium chloride paper turns dark when CO present. Imprecise but gives warning.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Foundations | Basic hygiene, clean water, herbal medicine, wound care |
| Metallurgy | Mining injuries, burn treatment, metal fume fever, glass for eye protection |
| Machine Tools | Machine shop safety (entanglement, eye protection), precision instruments for medicine |
| Energy | Boiler safety, electrical injury treatment, steam sterilization (autoclave) |
| Chemistry | HF acid protocols, toxic gas safety, chemical burn treatment, synthetic pharmaceuticals |
| the Silicon-Photolithography stage transition | Cleanroom health protocols, toxic dopant gas safety, ultra-pure water |

## Key Deliverables

- Clean water supply (wells + filtration + chlorination) for all settlements
- Sewage and waste disposal systems
- Basic hospital/infirmary with surgical capability and anesthesia
- PPE standards and supply chain for all hazardous work
- HF acid emergency protocol with calcium gluconate gel at every workstation
- Pharmaceutical production: aspirin, ether/chloroform anesthesia, antiseptics, morphine
- Gas detection capability at all industrial sites
- Quarantine protocols for infectious disease

## Safety Concerns

- **HF acid**: The single most dangerous chemical in the entire tech tree. Penetrates skin painlessly, binds calcium → hypocalcemia → cardiac arrest. ALWAYS have calcium gluconate gel within arm's reach. Full PPE. Buddy system — never work with HF alone.
- **Heavy metals**: Lead, mercury, arsenic, cadmium — accumulate in body, cause chronic neurological and organ damage. Minimize exposure. Use gloves. Do not eat/drink in work areas. Wash hands before meals.
- **Anesthesia**: Ether is flammable (flash point -45°C) — no open flames, no static sparks. Chloroform causes liver damage with repeated exposure. Monitor breathing continuously during administration.
- **Infection control**: Sterilize everything. Wash hands. Isolate infectious patients. One wound infection can kill a specialist worker who took 20 years to train.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
