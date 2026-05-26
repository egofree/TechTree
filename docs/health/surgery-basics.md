# Surgery Basics

> **Node ID**: health.surgery-basics
> **Domain**: [Health](./index.md)
> **Dependencies**: [`health.medicine`](medicine.md), [`health.medical-instruments`](medical-instruments.md), [`health.sanitation`](sanitation.md)
> **Enables**: [`health.pharmacology`](pharmacology.md), [`health.diagnostics`](diagnostics.md)
> **Timeline**: Years 10-100+
> **Outputs**: surgical_capability, wound_management, sterile_technique
> **Critical**: Yes — without surgical capability, traumatic injuries and complicated births are routinely fatal

## Overview

Surgery basics covers wound management, basic surgical techniques, sterilization, and anesthesia fundamentals for a bootstrap medical system. Before modern hospitals, the majority of preventable deaths came from infected wounds, uncontrolled bleeding, and obstructed labor. Establishing sterile technique, hemostasis (bleeding control), and reliable wound closure transforms a 50% mortality rate for serious wounds into a 5-10% rate.

The prerequisite chain runs: [sanitation](sanitation.md) → clean environment → [medical instruments](medical-instruments.md) → sterile tools → surgery. The leap from "cleaning wounds" to "opening a body cavity and repairing damage" requires each prior capability to be in place. Sterilization failures kill faster than the original injury — a dirty instrument introduces bacteria directly into tissue planes that the immune system cannot easily reach.

## Prerequisites

### Materials

- Sterile suture material: silk ([sericulture](../animals/sericulture.md)), catgut (sheep/cattle intestine), or cotton thread
- Bandaging: clean linen or cotton cloth, [wool](../animals/sheep.md) for absorbent padding
- Antiseptics: ethanol (60-70%), iodine tincture (2-7%), or carbolic acid (phenol 2-5%)
- Anesthetic agents: diethyl ether or chloroform (see [pharmacology](pharmacology.md))
- Clean water: boiled or filtered (see [sanitation](sanitation.md))

### Tools and Equipment

- [Surgical instruments](medical-instruments.md): scalpel, forceps, scissors, needle holder, retractors, hemostats
- Autoclave or pressure cooker for sterilization (121°C, 15 psi, 15+ minutes)
- Heat source: bunsen burner or spirit lamp for flame sterilization of instruments
- Clean workspace: dedicated room or area with washable surfaces
- Lighting: bright, shadow-free — surgical headlamp or positioned lamps

### Knowledge

- Anatomy: surface anatomy, major blood vessels, nerve locations, organ positions
- Wound healing: inflammatory phase (days 0-5), proliferative phase (days 3-21), remodeling (21+ days)
- Infection signs: rubor (redness), calor (heat), tumor (swelling), dolor (pain), functio laesa (loss of function)
- Fluid resuscitation principles: replace blood loss with 3× volume of crystalloid (saline or Ringer's solution)

### Infrastructure

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

## Process Description

### Wound Assessment and Preparation

1. **Assess the wound**: Determine depth, length, involvement of structures (tendons, nerves, vessels, bone), and contamination level. Clean wounds (<6 hours old, no debris) are primary closure candidates. Contaminated wounds (>6 hours, visible debris, bite wounds) require debridement and may need delayed closure.
2. **Control bleeding**: Apply direct pressure with sterile gauze for 10-15 minutes. If bleeding continues, apply a pressure dressing. For arterial bleeding, apply a tourniquet proximal to the wound (record time — release every 30 minutes for 5 minutes to prevent ischemia). Maximum tourniquet time: 2 hours.
3. **Clean the wound**: Irrigate with copious saline or clean water under pressure (use a 20-60 mL syringe with 18-gauge needle for ~8 psi irrigation pressure). Minimum volume: 100 mL per cm of wound length. Remove all visible debris with forceps.
4. **Debride dead tissue**: Excise necrotic (gray, non-bleeding) tissue and contaminated wound edges with scalpel or scissors. Healthy tissue bleeds when cut. Debridement converts a contaminated wound into a clean surgical wound.
5. **Disinfect the wound edges**: Paint the skin surrounding the wound with povidone-iodine (10% solution, diluted to 1% for open wounds) or 70% ethanol. Do not put disinfectant inside the wound itself — it damages healthy tissue and impairs healing.

### Suturing Technique

1. **Select suture material**: Non-absorbable (silk, nylon) for skin closure. Absorbable (catgut) for deep tissue and ligatures. Suture sizes: 3-0 or 4-0 for skin, 2-0 for fascia, 0 or 1 for deep tissue.
2. **Use sterile technique**: Wash hands with soap and water for 5 minutes. Wear sterile gloves if available. Touch only sterile surfaces. If gloves unavailable, use "no-touch" technique — handle the needle only with instruments, never bare fingers.
3. **Place sutures**: Use simple interrupted technique for most wounds. Enter the skin 3-5 mm from the wound edge, drive the needle through tissue in a curved arc, exit on the opposite side at equal distance and depth. Tie square knots (2 throws for silk, 3-4 for monofilament). Spacing: 5-8 mm between sutures.
4. **Check approximation**: Wound edges should be everted (slightly turned outward) — this produces a flat scar. Inverted edges heal with a depressed scar. If edges are under tension, use mattress sutures (vertical or horizontal) to distribute force.
5. **Dress the wound**: Apply thin layer of antiseptic ointment if available. Cover with sterile gauze. Secure with bandage. Change dressing at 24-48 hours, then every 2-3 days unless signs of infection develop.

### Sterilization Procedures

1. **Steam sterilization (autoclave)**: Wrap instruments in cloth or place in sterilization container. Process at 121°C (15 psi steam pressure) for 15 minutes (unwrapped) or 30 minutes (wrapped). For larger packs or porous loads: 132°C (27 psi) for 4 minutes (prevacuum) or 121°C for 30 minutes (gravity). Allow to dry before removing. Instruments remain sterile in sealed packs for up to 30 days.
2. **Boiling**: Submerge instruments in boiling water (100°C) for 30 minutes. Kills vegetative bacteria and most viruses. Does NOT kill bacterial spores (Clostridium tetani, C. perfringens). Boiling is a fallback method when no autoclave is available.
3. **Chemical sterilization**: Soak in 2% glutaraldehyde for 10 hours (full sterilization) or 70% ethanol for 30 minutes (high-level disinfection). Glutaraldehyde requires advanced chemical synthesis. Ethanol soak is the most practical bootstrap option for heat-sensitive items.
4. **Dry heat**: Bake instruments in oven at 160°C for 2 hours or 170°C for 1 hour. Kills all organisms including spores. Suitable for metal instruments and glass syringes. Does not corrode sharp edges (unlike steam).

## Quantitative Parameters

### Sterilization Parameters

| Method | Temperature | Time | Pressure | Kills Spores? | Suitable For |
|--------|------------|------|----------|--------------|-------------|
| Autoclave (gravity) | 121°C | 30 min | 15 psi | Yes | All instruments, textiles |
| Autoclave (prevacuum) | 132°C | 4 min | 27 psi | Yes | All instruments, fast cycle |
| Boiling | 100°C | 30 min | Ambient | No | Metal instruments (fallback) |
| Dry heat | 160°C | 120 min | Ambient | Yes | Metal, glass, powders |
| Dry heat | 170°C | 60 min | Ambient | Yes | Metal, glass, powders |
| Ethanol soak | 20-25°C | 30 min | Ambient | No | Heat-sensitive items |
| Glutaraldehyde 2% | 20-25°C | 10 hr | Ambient | Yes | Endoscopes, heat-sensitive |

### Suture Sizes and Applications

| Size | Diameter (mm) | Typical Use | Breaking Strength (kg) |
|------|--------------|-------------|----------------------|
| 0 | 0.35 | Fascia, deep tissue | 4.0-5.0 |
| 1 | 0.40 | Abdominal wall closure | 5.0-6.0 |
| 2-0 | 0.30 | Fascia, subcutaneous | 3.0-4.0 |
| 3-0 | 0.20 | Skin (body), muscle | 2.0-2.5 |
| 4-0 | 0.15 | Skin (face, hands), small vessels | 1.0-1.5 |
| 5-0 | 0.10 | Facial skin, nerve repair | 0.5-0.8 |

### Wound Healing Timeline

| Phase | Timeframe | Key Events | Clinical Significance |
|-------|-----------|------------|---------------------|
| Hemostasis | 0-6 hours | Clot formation, vasoconstriction | Bleeding stops; clot provides scaffold |
| Inflammation | 0-5 days | Neutrophils clear debris; macrophages arrive | Wound edges red, swollen, warm — normal up to day 5 |
| Proliferation | 3-21 days | Granulation tissue fills defect; epithelialization | Wound contracts; new tissue fragile — avoid stress |
| Remodeling | 21 days - 1 year | Collagen reorganization; scar matures | Scar gains tensile strength: 20% at 3 weeks, 50% at 4 months, 80% at 1 year |

### Skin Suture Removal Times

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

- **Sterile technique is non-negotiable**: A single contaminated instrument can introduce lethal infection. The transition from "dirty" surgery (50%+ mortality from infection) to aseptic surgery (<5% mortality) is the single greatest advance in surgical history. Follow Lister's principles: sterilize everything that touches the wound.
- **Hemorrhage control**: Major vessels bleed at 15-30 mL/second. A patient can exsanguinate from a femoral artery laceration in 3-5 minutes. Apply direct pressure immediately. Never clamp blindly — you may crush a nerve. Identify the vessel, isolate it, and ligate with suture.
- **Anesthesia hazards**: Ether is explosive — no flames, sparks, or electrical equipment that arcs in the operating area. Chloroform causes hepatotoxicity and cardiac arrhythmia at high concentrations. Always have suction and airway management ready. Monitor pulse and respirations continuously during anesthesia.
- **Tourniquet risks**: Maximum application time 2 hours. Prolonged ischemia causes muscle necrosis (Volkmann's contracture) and nerve damage. Record time of application on the patient or tourniquet. Release every 30 minutes for 5 minutes.
- **Sharps handling**: Scalpel blades and suture needles are the most common source of operator injury. Never pass sharps hand-to-hand — use a "neutral zone" (kidney dish) for transfer. Dispose of used blades in a puncture-proof container.
- **Fluid overload**: During irrigation or IV fluid resuscitation, monitor for signs of fluid overload: crackles in lungs (auscultation), peripheral edema, shortness of breath. Maximum crystalloid resuscitation: 3 L in the first hour for an adult with severe hemorrhage.

## Quality Control

- **Sterility verification**: Use biological indicators (spore strips of Geobacillus stearothermophilus) in each autoclave load. Incubate at 55-60°C for 48 hours. No growth = sterile. Chemical indicators (autoclave tape that changes color) confirm temperature was reached but do NOT confirm sterility.
- **Suture integrity**: Pull-test each suture before use. It should withstand 50% of its rated breaking strength without stretching. Discard sutures that are frayed, brittle, or have been resterilized more than once.
- **Instrument condition**: Inspect scalpel blades for dullness (require less force = more control). Verify hemostats lock and release properly. Ensure needle holders grip the needle without rotation.
- **Wound evaluation criteria**: At each dressing change, document: wound edges (approximated or gapping), presence of drainage (clear/serous = normal; purulent/foul = infection), surrounding skin (redness extending >2 cm from wound = cellulitis), and pain level.
- **Outcome tracking**: Record all surgical procedures with: patient identifier, procedure type, duration, complications (infection, hemorrhage, dehiscence), and outcome at 7 and 30 days. Calculate infection rate: target <5% for clean wounds, <10% for clean-contaminated wounds.

## Variations and Alternatives

### Wound Closure Methods

| Method | When to Use | Advantages | Disadvantages |
|--------|------------|------------|--------------|
| Suturing | Most lacerations, surgical incisions | Strong, precise approximation | Requires skill, leaves needle marks |
| Surgical staples | Scalp, trunk lacerations | Fast (3-5× faster than sutures) | Requires stapler, less precise |
| Tissue adhesive (cyanoacrylate) | Small clean lacerations (<5 cm) | No needles, waterproof | Requires advanced chemistry to produce |
| Adhesive strips (butterfly, Steri-Strip) | Superficial lacerations, low tension | Painless, no removal tools needed | Weak — only for low-tension areas |
| Secondary intention (leave open) | Heavily contaminated wounds, bites | Lowest infection risk | Slow healing, larger scar |
| Delayed primary closure | Contaminated wounds at 3-5 days | Allows infection to declare before closure | Requires two procedures |

### Anesthesia Options

| Method | Agents | Onset | Duration | Risks |
|--------|--------|-------|----------|-------|
| Local infiltration | Lidocaine 1-2% with epinephrine 1:100,000 | 2-5 min | 1-2 hr | Allergic reaction; never use epi on fingers/toes/nose/ears/penis |
| Regional nerve block | Lidocaine 1-2% near nerve trunk | 5-15 min | 2-4 hr | Nerve injury if injected into nerve; intravascular injection |
| General anesthesia (inhalation) | Ether or chloroform via mask | 3-10 min | Continuous | Explosive (ether), hepatotoxic (chloroform), airway loss |
| Ketamine (if available) | IM 5-10 mg/kg or IV 1-2 mg/kg | 1-3 min (IV), 3-5 min (IM) | 15-30 min | Emergence reactions, hypertension; preserves airway reflexes |

### Historical Methods

- **Cauterization**: Apply heated metal to bleeding vessels or wound edges. Effective for hemostasis but causes extensive tissue destruction and promotes infection. Use only as a last resort when suture ligation is impossible.
- **Ligature (historical)**: Hippocrates and Celsus described using linen thread to tie off bleeding vessels, but the technique was largely lost in Western medicine until Ambroise Paré reintroduced it in the 16th century. Before ligatures, boiling oil was poured into wounds — the shift to ligatures dramatically reduced mortality.
- **Tourniquet**:最早 documented by Heliodorus (2nd century AD). A tightly wrapped band proximal to the surgical site provides a bloodless field. Essential for extremity surgery.

## References

- [Medicine & Surgery](medicine.md) — general medical practice, infection control
- [Medical Instruments](medical-instruments.md) — surgical tool fabrication
- [Pharmacology](pharmacology.md) — anesthetic agents, antiseptics, analgesics
- [Sanitation](sanitation.md) — clean water, sterile environment requirements
- [Occupational Health](occupational-health.md) — workplace injury prevention
- [Chemistry](../chemistry/index.md) — ethanol production, chemical sterilants
- [Textiles](../textiles/index.md) — bandage and suture material sourcing

---

*Part of the [Bootciv Tech Tree](../index.md) • [Health](./index.md) • [All Domains](../index.md)*
