# Surgery Basics

> **Node ID**: health.surgery-basics
> **Domain**: [Health](./index.md)
> **Dependencies**: [`health.medicine`](medicine.md), [`health.medical-instruments`](medical-instruments.md), [`health.sanitation`](sanitation.md)
> **Enables**: [`health.pharmacology`](pharmacology.md), [`health.diagnostics`](diagnostics.md)
> **Timeline**: Years 10-100+
> **Outputs**: surgical_capability, wound_management, sterile_technique
> **Critical**: Yes — without surgical capability, traumatic injuries and complicated births are routinely fatal

Surgery basics covers wound management, basic surgical techniques, sterilization, and anesthesia fundamentals for a bootstrap medical system. Before modern hospitals, the majority of preventable deaths came from infected wounds, uncontrolled bleeding, and obstructed labor. Establishing sterile technique, hemostasis (bleeding control), and reliable wound closure transforms a 50% mortality rate for serious wounds into a 5-10% rate.

The prerequisite chain runs: [sanitation](sanitation.md) → clean environment → [medical instruments](medical-instruments.md) → sterile tools → surgery. The leap from "cleaning wounds" to "opening a body cavity and repairing damage" requires each prior capability to be in place. Sterilization failures kill faster than the original injury — a dirty instrument introduces bacteria directly into tissue planes that the immune system cannot easily reach.

## Materials

- Sterile suture material: silk ([sericulture](../animals/sericulture.md)), catgut (sheep/cattle intestine), or cotton thread
- Bandaging: clean linen or cotton cloth, [wool](../animals/sheep.md) for absorbent padding
- Antiseptics: ethanol (60-70%), iodine tincture (2-7%), or carbolic acid (phenol 2-5%)
- Anesthetic agents: diethyl ether or chloroform (see [pharmacology](pharmacology.md))
- Clean water: boiled or filtered (see [sanitation](sanitation.md))

## Tools and Equipment

- [Surgical instruments](medical-instruments.md): scalpel, forceps, scissors, needle holder, retractors, hemostats
- Autoclave or pressure cooker for sterilization (121°C, 15 psi, 15+ minutes)
- Heat source: bunsen burner or spirit lamp for flame sterilization of instruments
- Clean workspace: dedicated room or area with washable surfaces
- Lighting: bright, shadow-free — surgical headlamp or positioned lamps

## Knowledge

- Anatomy: surface anatomy, major blood vessels, nerve locations, organ positions
- Wound healing: inflammatory phase (days 0-5), proliferative phase (days 3-21), remodeling (21+ days)
- Infection signs: rubor (redness), calor (heat), tumor (swelling), dolor (pain), functio laesa (loss of function)
- Fluid resuscitation principles: replace blood loss with 3× volume of crystalloid (saline or Ringer's solution)

## Infrastructure

- Clean water supply
- Waste disposal system for contaminated materials
- Sterilization equipment (autoclave, pressure cooker, or boiling vessel)

## Bill of Materials

| Material | Quantity per Procedure | Source | Alternatives |
|----------|----------------------|--------|-------------|
| Suture (silk, 3-0) | 2-4 packets (45 cm each) | [Sericulture](../animals/sericulture.md) | Catgut (absorbable), cotton thread, fishing line (nylon) |
| Gauze (sterile) | 10-20 squares (10×10 cm) | [Textiles](../textiles/index.md) — cotton/linen | Clean cloth, boiled and dried |
| Antiseptic (ethanol 70%) | 200-500 mL | [Fermentation + distillation](../chemistry/distillation.md) | Iodine tincture, chlorhexidine, boiled saline |
| Local anesthetic (if available) | 5-20 mL lidocaine 1-2% | [Pharmacology](pharmacology.md) | Ice for topical anesthesia, ether spray |
| Scalpel blades (#10 or #15) | 1-3 | [Medical Instruments](medical-instruments.md) | Razor blade (sterilized), sharp knife |
| Sterile gloves | 1 pair | [Polymers](../polymers/rubber.md) — latex | Thorough hand washing + sterile technique without gloves |
| Bandage (cotton/linen) | 1-3 m | [Textiles](../textiles/index.md) | Strips of clean cloth |
| Saline (0.9% NaCl) | 500-2000 mL | Salt + purified water, boiled | Clean boiled water |

## Wound Assessment and Preparation

1. **Assess the wound**: Determine depth, length, involvement of structures (tendons, nerves, vessels, bone), and contamination level. Clean wounds (<6 hours old, no debris) are primary closure candidates. Contaminated wounds (>6 hours, visible debris, bite wounds) require debridement and may need delayed closure.
2. **Control bleeding**: Apply direct pressure with sterile gauze for 10-15 minutes. If bleeding continues, apply a pressure dressing. For arterial bleeding, apply a tourniquet proximal to the wound (record time — release every 30 minutes for 5 minutes to prevent ischemia). Maximum tourniquet time: 2 hours.
3. **Clean the wound**: Irrigate with copious saline or clean water under pressure (use a 20-60 mL syringe with 18-gauge needle for ~8 psi irrigation pressure). Minimum volume: 100 mL per cm of wound length. Remove all visible debris with forceps.
4. **Debride dead tissue**: Excise necrotic (gray, non-bleeding) tissue and contaminated wound edges with scalpel or scissors. Healthy tissue bleeds when cut. Debridement converts a contaminated wound into a clean surgical wound.
5. **Disinfect the wound edges**: Paint the skin surrounding the wound with povidone-iodine (10% solution, diluted to 1% for open wounds) or 70% ethanol. Do not put disinfectant inside the wound itself — it damages healthy tissue and impairs healing.

**Verification**: After preparation, confirm that all visible debris has been removed, bleeding is controlled, and wound edges are clean and viable (pink, bleeding). Check distal neurovascular status (pulse, sensation, motor function). Document wound dimensions and classification (clean, clean-contaminated, contaminated, dirty).

**Expected outcome**: Proper wound preparation reduces bacterial load by >99% through combined mechanical irrigation and chemical antisepsis. Clean wounds prepared within 6 hours of injury have <5% infection rate with primary closure.

**Materials**: Syringe (20-60 mL) with 18-gauge needle for pressurized irrigation. Sterile saline or clean water (200-500 mL per wound). Povidone-iodine 10% solution (diluted to 1% for wound edges). Sterile gauze (10×10 cm squares). Scalpel or scissors for debridement. Forceps for debris removal.

**Strengths**:
- Pressurized irrigation mechanically removes bacteria and debris more effectively than any chemical antiseptic alone
- Debridement converts a contaminated irregular wound into a clean surgical wound with predictable healing
- Technique is achievable with basic equipment — syringe, clean water, and antiseptic

**Weaknesses**:
- Wound age >6 hours dramatically increases infection risk regardless of preparation quality
- Antiseptics (povidone-iodine, ethanol) damage healthy tissue in the wound bed — use only on intact skin surrounding the wound
- Irrigation fluid volume of 200-500 mL per wound requires significant clean water supply in mass casualty situations

## Suturing Technique

1. **Select suture material**: Non-absorbable (silk, nylon) for skin closure. Absorbable (catgut) for deep tissue and ligatures. Suture sizes: 3-0 or 4-0 for skin, 2-0 for fascia, 0 or 1 for deep tissue.
2. **Use sterile technique**: Wash hands with soap and water for 5 minutes. Wear sterile gloves if available. Touch only sterile surfaces. If gloves unavailable, use "no-touch" technique — handle the needle only with instruments, never bare fingers.
3. **Place sutures**: Use simple interrupted technique for most wounds. Enter the skin 3-5 mm from the wound edge, drive the needle through tissue in a curved arc, exit on the opposite side at equal distance and depth. Tie square knots (2 throws for silk, 3-4 for monofilament). Spacing: 5-8 mm between sutures.
4. **Check approximation**: Wound edges should be everted (slightly turned outward) — this produces a flat scar. Inverted edges heal with a depressed scar. If edges are under tension, use mattress sutures (vertical or horizontal) to distribute force.
5. **Dress the wound**: Apply thin layer of antiseptic ointment if available. Cover with sterile gauze. Secure with bandage. Change dressing at 24-48 hours, then every 2-3 days unless signs of infection develop.

**Verification**: After suturing, inspect wound approximation under good lighting — edges should be everted (slightly turned outward) with no gaps. Verify hemostasis (no bleeding through the suture line). Check distal neurovascular status (pulse, sensation, motor function). Document number of sutures placed and suture material used.

**Expected outcome**: Properly approximated wounds heal by primary intention with tensile strength reaching 20% at 3 weeks, 50% at 4 months, and 80% at 1 year. Infection rate for clean wounds closed with sterile technique: <5%. Suture marks (from leaving sutures too long) are avoidable by removing at the correct interval.

**Materials**: Suture material: silk 3-0 or 4-0 for skin (diameter 0.15-0.20 mm, breaking strength 1.0-2.5 kg). Needle holder (Mayo-Hegar, 6 inch). Tissue forceps (Adson, 1×2 teeth). Scalpel with #15 blade. Sterile gauze (10×10 cm). Antiseptic ointment (optional). Bandage material (cotton/linen, 1-3 m).

**Strengths**:
- Simple interrupted sutures allow individual removal and wound inspection without disrupting the entire closure
- Square knots (2 throws for silk, 3-4 for monofilament) provide reliable wound approximation without special instruments
- Technique is learnable in 10-20 practice sessions on pig feet or banana peels before patient contact

**Weaknesses**:
- Suturing under tension causes tissue ischemia and wound dehiscence — wound edges must approximate without force
- Needlestick injuries during suturing are a leading cause of bloodborne pathogen exposure for the operator
- Suture removal requires the correct timing per body area (5-7 days for face, 10-14 days for extremities) — missed removal causes scarring

## Sterilization Procedures

1. **Steam sterilization (autoclave)**: Wrap instruments in cloth or place in sterilization container. Process at 121°C (15 psi steam pressure) for 15 minutes (unwrapped) or 30 minutes (wrapped). For larger packs or porous loads: 132°C (27 psi) for 4 minutes (prevacuum) or 121°C for 30 minutes (gravity). Allow to dry before removing. Instruments remain sterile in sealed packs for up to 30 days.
2. **Boiling**: Submerge instruments in boiling water (100°C) for 30 minutes. Kills vegetative bacteria and most viruses. Does NOT kill bacterial spores (Clostridium tetani, C. perfringens). Boiling is a fallback method when no autoclave is available.
3. **Chemical sterilization**: Soak in 2% glutaraldehyde for 10 hours (full sterilization) or 70% ethanol for 30 minutes (high-level disinfection). Glutaraldehyde requires advanced chemical synthesis. Ethanol soak is the most practical bootstrap option for heat-sensitive items.
4. **Dry heat**: Bake instruments in oven at 160°C for 2 hours or 170°C for 1 hour. Kills all organisms including spores. Suitable for metal instruments and glass syringes. Does not corrode sharp edges (unlike steam).

**Verification**: For each autoclave load, include a biological indicator (Geobacillus stearothermophilus spore strip) in the most difficult-to-sterilize location (center of wrapped pack). Incubate at 55-60°C for 48 hours. No growth = sterile. Chemical indicators (autoclave tape) on every pack confirm temperature reached but do not confirm sterility.

**Expected outcome**: Autoclave at 121°C for 30 minutes achieves sterility assurance level (SAL) of 10⁻⁶. Boiling at 100°C for 30 minutes kills vegetative bacteria and most viruses but NOT bacterial spores (Clostridium tetani, C. perfringens). Instruments remain sterile in sealed cloth packs for up to 30 days.

**Materials**: Autoclave (pressure vessel rated to 30 psi, temperature gauge 0-150°C, safety relief valve set to 20 psi). Sterilization wrap (cotton muslin or paper pouches). Biological indicators (spore strips). Chemical indicators (autoclave tape, changes pattern at 121°C). Heat-resistant gloves for loading/unloading.

**Strengths**:
- Steam sterilization kills all organisms including spores — the only method that guarantees complete sterility
- Chemical indicators on every pack provide immediate visual confirmation that the cycle ran correctly
- Wrapped instruments remain sterile for 30 days, allowing advance preparation of instrument sets

**Weaknesses**:
- Autoclave requires a pressure vessel — construction demands competent welding and hydrostatic testing at 1.5× working pressure
- Boiling does not kill spores — instruments used for penetrating wounds (where tetanus risk is high) must be autoclaved or dry-heated
- Sterile technique breaks down if packs are touched with non-sterile hands or placed on contaminated surfaces

## Sterilization Parameters

| Method | Temperature | Time | Pressure | Kills Spores? | Suitable For |
|--------|------------|------|----------|--------------|-------------|
| Autoclave (gravity) | 121°C | 30 min | 15 psi | Yes | All instruments, textiles |
| Autoclave (prevacuum) | 132°C | 4 min | 27 psi | Yes | All instruments, fast cycle |
| Boiling | 100°C | 30 min | Ambient | No | Metal instruments (fallback) |
| Dry heat | 160°C | 120 min | Ambient | Yes | Metal, glass, powders |
| Dry heat | 170°C | 60 min | Ambient | Yes | Metal, glass, powders |
| Ethanol soak | 20-25°C | 30 min | Ambient | No | Heat-sensitive items |
| Glutaraldehyde 2% | 20-25°C | 10 hr | Ambient | Yes | Endoscopes, heat-sensitive |

## Suture Sizes and Applications

| Size | Diameter (mm) | Typical Use | Breaking Strength (kg) |
|------|--------------|-------------|----------------------|
| 0 | 0.35 | Fascia, deep tissue | 4.0-5.0 |
| 1 | 0.40 | Abdominal wall closure | 5.0-6.0 |
| 2-0 | 0.30 | Fascia, subcutaneous | 3.0-4.0 |
| 3-0 | 0.20 | Skin (body), muscle | 2.0-2.5 |
| 4-0 | 0.15 | Skin (face, hands), small vessels | 1.0-1.5 |
| 5-0 | 0.10 | Facial skin, nerve repair | 0.5-0.8 |

## Wound Healing Timeline

| Phase | Timeframe | Key Events | Clinical Significance |
|-------|-----------|------------|---------------------|
| Hemostasis | 0-6 hours | Clot formation, vasoconstriction | Bleeding stops; clot provides scaffold |
| Inflammation | 0-5 days | Neutrophils clear debris; macrophages arrive | Wound edges red, swollen, warm — normal up to day 5 |
| Proliferation | 3-21 days | Granulation tissue fills defect; epithelialization | Wound contracts; new tissue fragile — avoid stress |
| Remodeling | 21 days - 1 year | Collagen reorganization; scar matures | Scar gains tensile strength: 20% at 3 weeks, 50% at 4 months, 80% at 1 year |

## Skin Suture Removal Times

| Body Area | Removal Time | Reason |
|-----------|-------------|--------|
| Face | 5-7 days | Minimize scarring; rich blood supply heals fast |
| Scalp | 7-10 days | Good blood supply |
| Trunk | 7-10 days | Moderate tension |
| Extremities | 10-14 days | Higher tension, slower healing |
| Back | 12-16 days | High tension, slow healing |
| Joints (over) | 14-21 days | Maximum tension and motion |

## Scaling Notes

- **Individual wound care**: One trained person with basic instruments and antiseptics. Throughput: 5-15 simple wound closures per day.
- **Small surgical suite**: Dedicated room with operating table, autoclave, instrument set, and lighting. Requires 2-3 people (surgeon, assistant, instrument nurse). Throughput: 3-8 procedures per day.
- **Field hospital**: Multiple surgical stations running simultaneously. Requires instrument sterilization pipeline (autoclave running continuously), suture resupply, and post-operative recovery space. Minimum: 1 autoclave per 3 surgical stations.
- **Bottleneck**: Sterilization capacity. Each autoclave cycle takes 30-45 minutes (including load/unload). Plan instrument sets to match: if average procedure takes 30 minutes and sterilization cycle takes 45 minutes, maintain at least 3 complete instrument sets in rotation.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Wound dehiscence (reopens) | Suture too few, under tension, infection | Debride edges, relieve tension with mattress sutures, treat infection with antiseptic irrigation |
| Wound infection (redness, pus, fever after day 3) | Contaminated wound, inadequate debridement, non-sterile technique | Remove sutures to drain, irrigate with antiseptic, apply warm compresses, systemic treatment if available |
| Excessive bleeding during procedure | Inadequate hemostasis, cut vessel not ligated | Apply pressure, identify bleeding point, ligate with absorbable suture, or cauterize |
| Stitch abscess (localized redness at suture site) | Reaction to suture material or bacteria introduced along suture track | Remove the offending suture, express pus, apply antiseptic dressing |
| Hypertrophic scar | Excessive tension, wound orientation across skin lines | Prevent by proper wound approximation; treat with pressure therapy once healed |
| Tourniquet paralysis | Tourniquet left too long (>2 hours) | Release tourniquet every 30 min for 5 min; never exceed 2 hours total; note time of application |
| Ether anesthesia too deep | Over-administration, respiratory depression | Reduce ether concentration immediately; tilt head back to open airway; provide assisted ventilation (mouth-to-mask) |

## Safety

- **Sterile technique is non-negotiable**: A single contaminated instrument can introduce lethal infection. The transition from "dirty" surgery (50%+ mortality from infection) to aseptic surgery (<5% mortality) is the single greatest advance in surgical history. Follow Lister's principles: sterilize everything that touches the wound. The rationale is simple: the immune system cannot mount an effective response against bacteria introduced directly into deep tissue planes where white blood cells have limited access. Surface wounds (skin abrasions) are handled by the immune system routinely. Deep surgical wounds bypass this defense.
- **Hemorrhage control**: Major vessels bleed at 15-30 mL/second. A patient can exsanguinate from a femoral artery laceration in 3-5 minutes. Apply direct pressure immediately. Never clamp blindly — you may crush a nerve. Identify the vessel, isolate it, and ligate with suture. Blood volume in an adult is approximately 70 mL/kg (about 5 liters for a 70 kg adult). Loss of 15% (750 mL) causes tachycardia. Loss of 30% (1,500 mL) causes hypotension and tachycardia. Loss of 40% (2,000 mL) causes profound shock and is often fatal without transfusion.
- **Anesthesia hazards**: Ether is explosive — no flames, sparks, or electrical equipment that arcs in the operating area. Chloroform causes hepatotoxicity and cardiac arrhythmia at high concentrations. Always have suction and airway management ready. Monitor pulse and respirations continuously during anesthesia. Count respiratory rate by watching chest rise: if below 8 per minute, reduce anesthetic depth and assist ventilation. The most common cause of anesthesia death at bootstrap level is not the anesthetic itself but loss of airway from the tongue falling back in an unconscious patient. Place the patient in the recovery position (on their side, chin extended) after any general anesthetic.
- **Tourniquet risks**: Maximum application time 2 hours. Prolonged ischemia causes muscle necrosis (Volkmann's contracture) and nerve damage. Record time of application on the patient or tourniquet. Release every 30 minutes for 5 minutes. When releasing a tourniquet after a long case, expect transient hypotension from the sudden return of acidic, potassium-laden blood to the central circulation. Have IV fluids running.
- **Sharps handling**: Scalpel blades and suture needles are the most common source of operator injury. Never pass sharps hand-to-hand — use a "neutral zone" (kidney dish) for transfer. Dispose of used blades in a puncture-proof container. A needlestick injury from a patient with hepatitis B carries a 6-30% transmission risk; hepatitis C carries a 1.8% risk. At bootstrap level without post-exposure prophylaxis, sharps injuries carry serious long-term consequences.
- **Fluid overload**: During irrigation or IV fluid resuscitation, monitor for signs of fluid overload: crackles in lungs (auscultation), peripheral edema, shortness of breath. Maximum crystalloid resuscitation: 3 L in the first hour for an adult with severe hemorrhage. Over-resuscitation causes pulmonary edema (fluid in the lungs), which is fatal without mechanical ventilation.
- **Surgical fire risk with ether**: Ether vapor is heavier than air and pools on the floor. A spark from static electricity, an electric cautery unit, or a nearby flame ignites the pooled vapor explosively. The operating area must have no open flames within 6 meters. The floor should be conductive (or wet-mopped) to dissipate static charge. The ether mask and bottle must be kept below the level of the operating table to prevent dripping onto the patient's chest. If ether ignites on the mask, smother with a wet towel immediately and remove the mask from the patient's face.

## Quality Control

- **Sterility verification**: Use biological indicators (spore strips of Geobacillus stearothermophilus) in each autoclave load. Incubate at 55-60°C for 48 hours. No growth = sterile. Chemical indicators (autoclave tape that changes color) confirm temperature was reached but do NOT confirm sterility.
- **Suture integrity**: Pull-test each suture before use. It should withstand 50% of its rated breaking strength without stretching. Discard sutures that are frayed, brittle, or have been resterilized more than once.
- **Instrument condition**: Inspect scalpel blades for dullness (require less force = more control). Verify hemostats lock and release properly. Ensure needle holders grip the needle without rotation.
- **Wound evaluation criteria**: At each dressing change, document: wound edges (approximated or gapping), presence of drainage (clear/serous = normal; purulent/foul = infection), surrounding skin (redness extending >2 cm from wound = cellulitis), and pain level.
- **Outcome tracking**: Record all surgical procedures with: patient identifier, procedure type, duration, complications (infection, hemorrhage, dehiscence), and outcome at 7 and 30 days. Calculate infection rate: target <5% for clean wounds, <10% for clean-contaminated wounds.

## Wound Closure Methods

| Method | When to Use | Advantages | Disadvantages |
|--------|------------|------------|--------------|
| Suturing | Most lacerations, surgical incisions | Strong, precise approximation | Requires skill, leaves needle marks |
| Surgical staples | Scalp, trunk lacerations | Fast (3-5× faster than sutures) | Requires stapler, less precise |
| Tissue adhesive (cyanoacrylate) | Small clean lacerations (<5 cm) | No needles, waterproof | Requires advanced chemistry to produce |
| Adhesive strips (butterfly, Steri-Strip) | Superficial lacerations, low tension | Painless, no removal tools needed | Weak — only for low-tension areas |
| Secondary intention (leave open) | Heavily contaminated wounds, bites | Lowest infection risk | Slow healing, larger scar |
| Delayed primary closure | Contaminated wounds at 3-5 days | Allows infection to declare before closure | Requires two procedures |

## Anesthesia Options

| Method | Agents | Onset | Duration | Risks |
|--------|--------|-------|----------|-------|
| Local infiltration | Lidocaine 1-2% with epinephrine 1:100,000 | 2-5 min | 1-2 hr | Allergic reaction; never use epi on fingers/toes/nose/ears/penis |
| Regional nerve block | Lidocaine 1-2% near nerve trunk | 5-15 min | 2-4 hr | Nerve injury if injected into nerve; intravascular injection |
| General anesthesia (inhalation) | Ether or chloroform via mask | 3-10 min | Continuous | Explosive (ether), hepatotoxic (chloroform), airway loss |
| Ketamine (if available) | IM 5-10 mg/kg or IV 1-2 mg/kg | 1-3 min (IV), 3-5 min (IM) | 15-30 min | Emergence reactions, hypertension; preserves airway reflexes |

### Anesthesia Dosing Protocols

**Ether general anesthesia**: Induction requires 10-15% vapor concentration (volume percent in air) delivered via an open-drop mask. Place a wire frame over the patient's nose and mouth, drape with 6-8 layers of gauze, and drip ether onto the gauze at a rate of 1-2 drops per second for the first 2 minutes, then titrate to effect. Induction takes 5-10 minutes. Maintain at 3-5% vapor for surgical anesthesia. Signs of adequate depth: loss of eyelid reflex, regular deep breathing, no movement to surgical stimulus. Signs of overdose: shallow or irregular breathing, cyanosis (blue lips), dilated pupils. If overdose occurs, remove the mask immediately, tilt the head back, and provide assisted ventilation with a bellows or mouth-to-mask. Ether provides good muscle relaxation and a wide margin between surgical anesthesia and respiratory arrest (roughly 3.4% surgical vs 6% lethal concentration), which makes it the safest available inhalation agent for untrained providers.

**Chloroform general anesthesia**: More potent than ether, induction at 1-2% vapor, maintenance at 0.5-1.5%. The margin between surgical anesthesia and cardiac arrest is dangerously narrow. Chloroform causes direct myocardial depression and sensitizes the heart to catecholamines, triggering fatal ventricular fibrillation. Avoid chloroform if ether is available. Maximum safe dose: approximately 2-3 mL total liquid chloroform for an adult. If used, apply to the mask in drops (never pour), and watch for sudden pupillary dilation or pulse irregularity, either of which signals imminent cardiac arrest.

**Lidocaine local anesthesia**: Maximum safe dose is 4.5 mg/kg without epinephrine, 7 mg/kg with epinephrine (1:100,000 or 10 μg/mL). For a 70 kg adult: 315 mg (about 32 mL of 1% lidocaine) without epinephrine, or 490 mg (about 49 mL of 1% with epinephrine). Toxicity symptoms in order: perioral numbness, tongue tingling, tinnitus, blurred vision, muscle twitching, seizures, cardiac arrest. If toxicity occurs, stop injection, administer oxygen, and treat seizures with diazepam 5-10 mg IV if available. Prepare lidocaine by dissolving lidocaine hydrochloride powder in sterile water. A 1% solution contains 10 mg/mL. Always aspirate before injecting to avoid intravascular injection, which causes immediate systemic toxicity at a fraction of the topical dose.

**Morphine analgesia** (for fracture reduction, post-operative pain): 0.1-0.2 mg/kg IM or subcutaneous. Adult dose: 5-15 mg every 4-6 hours as needed. Reduce by 50% in elderly patients or those with reduced respiratory reserve. Overdose causes respiratory depression (breathing rate below 8/minute). Treatment: assist ventilation. Naloxone (specific antidote) 0.4-2.0 mg IV reverses opioid effects but may not be available at bootstrap stage.

## Specific Surgical Procedures

### Amputation (Guillotine Method)

Amputation is a last resort when a limb is crushed beyond salvage, infected with gas gangrene, or bleeding uncontrollably from a proximal vessel. The guillotine method is the simplest and fastest technique, requiring no tissue flaps.

1. **Preparation**: Apply tourniquet 10-15 cm above the planned amputation site. Tighten until distal pulse disappears. Note the time. Administer general anesthesia (ether) or high-dose morphine (15 mg IM for 70 kg adult) plus ethanol by mouth. Prepare instruments: scalpel with #10 blade, bone saw, amputation knife (or large scalpel), Kelly hemostats (6-8), silk ligatures (2-0 and 0), catgut suture (2-0), retractors (Army-Navy), bone rongeur or file.
2. **Incise skin and fascia**: Make a circumferential incision through skin and subcutaneous tissue down to fascia at the level of planned bone division. Allow the skin to retract proximally 2-3 cm. The skin retraction ensures the final stump will have adequate soft tissue coverage over the bone end.
3. **Divide muscles**: Divide all muscle groups at the level of the retracted skin edge. Use a scalpel for clean cuts (not cautery, which produces more necrotic tissue). As you divide each muscle layer, identify and clamp major vessels with Kelly hemostats before they retract.
4. **Ligate vessels**: Tie off each clamped vessel with 2-0 silk ligatures (square knot, 3 throws). Arteries larger than 3 mm diameter require double ligation (two separate ligatures 3-5 mm apart). The femoral artery requires suture ligature (pass a suture through the vessel wall, then tie) to prevent slippage.
5. **Divide bone**: Retract muscles proximally to expose bone. Use a bone saw to divide the bone at a level 2-3 cm proximal to the muscle division. File the bone end smooth with a bone file or rongeur to remove sharp edges that would erode through the skin. Bone bleeding stops with local pressure from surrounding tissue; the marrow bleeds into the soft tissue and tamponades itself.
6. **Close or leave open**: For clean amputations (trauma without infection), close the stump with catgut sutures in the fascia and interrupted silk sutures in the skin. For infected or contaminated amputations, leave the wound open with moist gauze packing and plan delayed closure at day 4-5.
7. **Post-operative care**: Apply a bulky dressing with moderate compression. Elevate the stump on pillows. Monitor for hemorrhage (check dressing every 15 minutes for the first 2 hours). Phantom limb pain occurs in most patients and resolves over weeks to months. Begin stump conditioning (wrapping with elastic bandage to shape the limb) at day 7-10 if healing is progressing.

**Why guillotine rather than flap method at bootstrap level**: The flap method produces a better functional stump but requires precise planning of skin and muscle flaps with specific length ratios (typically a longer posterior flap for below-knee amputations). The guillotine method is faster (15-30 minutes vs. 60-90 minutes), has lower blood loss, and can always be revised to a flap amputation once the patient stabilizes. In a resource-limited setting, speed and simplicity save lives.

### Abscess Drainage

An abscess is a localized collection of pus (dead white blood cells, bacteria, and tissue debris) walled off by the body's immune system. Antibiotics cannot penetrate the abscess wall effectively. Drainage is the definitive treatment.

1. **Confirm the diagnosis**: A fluctuant (boggy, fluid-filled) swelling with overlying erythema and warmth. The patient typically has pain, fever, and tenderness at the site. If the swelling is firm and non-fluctuant, the abscess has not yet matured. Apply warm compresses (40-42°C, 20 minutes every 2-4 hours) to promote localization. Re-examine daily until fluctuance develops.
2. **Anesthetize**: Inject 1% lidocaine with epinephrine in a field block around the abscess (inject in a ring around the perimeter, not into the abscess itself, which is already dead tissue and acidic, rendering local anesthetic ineffective). Wait 5 minutes for full effect.
3. **Incise**: Using a #11 scalpel blade, make a stab incision at the point of maximal fluctuance. The incision should be large enough to allow free drainage (typically 1-2 cm for a 3-5 cm abscess). Make the incision parallel to skin tension lines for minimal scarring. Insert a hemostat into the cavity, open the jaws, and spread to break up loculations (internal walls that partition the pus into separate chambers).
4. **Drain**: Express all pus manually. Irrigate the cavity with 100-200 mL sterile saline using a syringe. Send a sample of pus for Gram stain if laboratory capability exists.
5. **Pack and dress**: Pack the cavity loosely with iodoform gauze strip (1.25 cm width) or plain sterile gauze. The packing keeps the wound open, preventing premature skin closure while the cavity heals from the base upward. Change packing daily. Reduce packing volume each day as the cavity shrinks. Continue until the cavity fills with granulation tissue.
6. **Monitor**: The patient should have fever reduction within 24-48 hours. If fever persists, re-examine for loculated residual pus, a deeper abscess, or spreading cellulitis requiring systemic treatment.

**Why packing is necessary**: If the skin closes over an abscess cavity that has not yet filled with granulation tissue, the residual bacteria multiply in the dead space and the abscess recurs. Packing forces the wound to heal from the bottom up (secondary intention), which takes longer but prevents re-accumulation.

### Emergency Appendectomy (Open Method)

Appendicitis presents with periumbilical pain migrating to the right lower quadrant, anorexia, nausea, and low-grade fever. McBurney's point (one-third the distance from the anterior superior iliac spine to the umbilicus) is the classic location of maximal tenderness. Rebound tenderness, involuntary guarding, and fever >38°C suggest perforation, which carries 5-10× higher mortality than unperforated appendicitis.

1. **Diagnose clinically**: Right lower quadrant tenderness at McBurney's point, rebound tenderness, fever 37.5-38.5°C (unperforated) or >38.5°C (likely perforated), elevated white blood cell count (>10,000/μL with neutrophilia >75%). Without ultrasound or CT, diagnosis is clinical and has a 15-20% false positive rate (removing a normal appendix is far less dangerous than missing a ruptured one).
2. **Prepare**: General anesthesia with ether. Place patient supine. Shave and prep the right lower abdomen with povidone-iodine. Drape to expose a 15 × 15 cm field centered on McBurney's point. Instruments: scalpel (#10 blade), Kelly hemostats (6), DeBakey forceps, Richardson retractors (small), needle holder, silk 3-0 and catgut 2-0 sutures, Babcock clamp (for grasping the appendix without crushing), scissors, suction setup (or sponges for field drying).
3. **Incision**: Make a 5-8 cm oblique incision (McBurney incision) at right angles to a line from the umbilicus to the anterior superior iliac spine, centered on McBurney's point. Divide skin, subcutaneous fat, and external oblique aponeurosis in the direction of its fibers. Split the internal oblique and transversus muscles bluntly (spread with a hemostat along the muscle fibers rather than cutting, which reduces post-operative hernia risk). Open the peritoneum.
4. **Find the appendix**: Deliver the cecum into the wound by gently pulling with a moist sponge. The appendix is a tubular structure 6-12 cm long arising from the posteromedial wall of the cecum, 2-3 cm below the ileocecal junction. Grasp the appendix with a Babcock clamp. If the appendix is inflamed (red, swollen, fibrin-coated), proceed. If perforated (gangrenous tissue, foul-smelling pus), suction the pus and irrigate with 500-1000 mL saline.
5. **Divide the mesoappendix**: The mesoappendix carries the appendicular artery. Clamp, divide, and ligate the mesoappendix in sections using 2-0 silk ligatures. Each section is clamped with two hemostats, divided between them, and the proximal stump ligated.
6. **Remove the appendix**: Crush the base of the appendix with a hemostat, then ligate with 2-0 silk at the crush line. Cut the appendix 5 mm distal to the ligature. Some surgeons invert the appendiceal stump into the cecum using a purse-string suture (3-0 silk in the cecal wall around the stump), but simple ligation without inversion is acceptable and faster.
7. **Close**: Irrigate the peritoneal cavity with 200-500 mL saline. Close the peritoneum with running 2-0 catgut. Close the internal oblique and transversus muscles with interrupted 2-0 catgut. Close the external oblique aponeurosis with running 2-0 catgut. Close skin with interrupted 3-0 silk or nylon. For perforated appendicitis, leave the skin open (delayed primary closure at day 4-5) to prevent wound infection.
8. **Post-operative**: NPO (nothing by mouth) until bowel sounds return (12-24 hours). Then clear liquids, advancing to regular diet as tolerated. Remove skin sutures at 7-10 days. Ambulate on day 1 to prevent deep vein thrombosis.

**Expected outcome**: Unperforated appendicitis treated by appendectomy has <2% mortality and <5% wound infection rate. Perforated appendicitis carries 5-15% mortality and 20-40% wound infection rate without antibiotics. Without surgery, ruptured appendicitis leads to peritonitis and death in most cases.

### Hemorrhoid Ligation and Excision

External hemorrhoids that thrombose (form a painful clot) and internal hemorrhoids that bleed chronically can be treated surgically.

**Rubber band ligation** (for internal hemorrhoids): Using a ligator (a cylindrical device that fires a small rubber band), grasp the hemorrhoid tissue above the dentate line (where there are no pain fibers) and deploy the band. The banded tissue necroses and sloughs off in 5-7 days. Complications: bleeding (typically minor, occurs when the tissue separates), severe pain if band placed below the dentate line (remove immediately).

**Excision of thrombosed external hemorrhoid**: Inject 1% lidocaine with epinephrine around the thrombosed hemorrhoid. Make an elliptical incision over the swelling. Evacuate the clot. Excise the overlying skin edges to prevent re-accumulation. The wound is left open to heal by secondary intention. Apply pressure dressing for 4-6 hours, then Sitz baths (warm water, 40°C, 15 minutes, 3 times daily) for symptomatic relief.

## Surgical Decision-Making: Why These Rules Exist

**The 6-hour wound closure rule**: Bacteria multiply logarithmically in a wound. At 6 hours, a wound contaminated with 10³ organisms has roughly 10⁶ organisms per gram of tissue, which is the threshold above which infection risk rises sharply. Closing a wound with more than 10⁶ organisms seals the bacteria inside a warm, moist, nutrient-rich environment. The 6-hour rule is not absolute (some clean wounds can be closed at 8-12 hours, and heavily contaminated wounds should not be closed even at 2 hours), but it provides a reliable decision point for providers without microbiology lab access.

**Why square knots matter**: A granny knot (two identical throws) slips under tension, causing the suture to loosen and the wound to separate. A square knot (second throw reversed relative to the first) locks in place. For braided suture (silk), two throws form a stable square knot. For monofilament (nylon, Prolene), the smooth surface allows even square knots to slip with only two throws, so 3-4 throws are required. A wound that dehisces because a granny knot slipped is entirely preventable.

**Why wounds are everted during closure**: Skin heals by forming a flat scar that contracts over months. If the wound edges are inverted (tucked inward) at the time of closure, the scar contracts into a depressed trough. If everted (turned slightly outward), the contraction pulls the scar flat. Eversion is achieved by entering the skin with the needle tilted outward (away from the wound) and taking a slightly larger bite of the deep tissue than the superficial tissue. Vertical mattress sutures naturally evert wound edges.

**Why tourniquet time is limited to 2 hours**: Muscle tissue survives ischemia by switching to anaerobic metabolism, which produces lactic acid. After 2 hours of complete ischemia, intracellular pH drops below 6.5, causing irreversible mitochondrial damage. When circulation returns, the damaged cells release myoglobin and potassium into the bloodstream, causing acute kidney failure (myoglobinuria) and cardiac arrhythmias (hyperkalemia). This is reperfusion injury. Releasing the tourniquet every 30 minutes for 5 minutes flushes metabolites and restores brief aerobic metabolism, extending the safe window.

## Historical Methods

- **Cauterization**: Apply heated metal to bleeding vessels or wound edges. Effective for hemostasis but causes extensive tissue destruction and promotes infection. Use only as a last resort when suture ligation is impossible.
- **Ligature (historical)**: Hippocrates and Celsus described using linen thread to tie off bleeding vessels, but the technique was largely lost in Western medicine until Ambroise Paré reintroduced it in the 16th century. Before ligatures, boiling oil was poured into wounds — the shift to ligatures dramatically reduced mortality.
- **Tourniquet**: Earliest documented by Heliodorus (2nd century AD). A tightly wrapped band proximal to the surgical site provides a bloodless field. Essential for extremity surgery.

## See Also

- [Medicine & Surgery](medicine.md) — general medical practice, infection control
- [Medical Instruments](medical-instruments.md) — surgical tool fabrication
- [Pharmacology](pharmacology.md) — anesthetic agents, antiseptics, analgesics
- [Sanitation](sanitation.md) — clean water, sterile environment requirements
- [Occupational Health](occupational-health.md) — workplace injury prevention
- [Chemistry](../chemistry/index.md) — ethanol production, chemical sterilants
- [Textiles](../textiles/index.md) — bandage and suture material sourcing

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Public Health, Sanitation & Medicine](./index.md) • [All Domains](../../index.md)*

