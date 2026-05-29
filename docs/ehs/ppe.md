# Personal Protective Equipment

> **Node ID**: ehs.ppe
> **Domain**: [Environmental Health & Safety](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)
> **Timeline**: Years 30-70
> **Outputs**: respiratory_protection, chemical_suits, glove_selection, eye_protection, ppe_programs
> **Critical**: No — basic improvised protection enables hazardous work; formal PPE programs dramatically reduce injury rates but are not a prerequisite for civilization-level capabilities


Semiconductor fabrication exposes workers to hydrofluoric acid, pyrophoric silane, toxic hydride gases, strong oxidizers, and organic solvents — often simultaneously in the same work area. PPE selection for semiconductor manufacturing must account for multiple hazard types, chemical compatibility with specific process chemicals, cleanroom compatibility (low particle generation), and the potential for rapid escalation (a silane leak can flash to fire within seconds). This document defines PPE requirements specific to semiconductor fab operations, supplementing the general PPE guidance in [Occupational Health](../health/occupational-health.md).

## Decision Framework: Respiratory Protection Selection

| Hazard Level | Concentration Range | Required Respirator | Protection Factor | Use Case |
|-------------|-------------------|--------------------|--------------------|----------|
| Below PEL | <PEL | None (or surgical mask for particulate) | N/A | Routine cleanroom work |
| Up to 10× PEL | PEL to 10× PEL | Half-face elastomeric with appropriate cartridge | 10× | Wet bench acid work, solvent handling |
| Up to 50× PEL | 10× PEL to 50× PEL | Full-face elastomeric with appropriate cartridge | 50× | Acid dispensing, piranha preparation |
| Up to 1,000× PEL | 50× PEL to 1,000× PEL | PAPR (tight-fitting full-face) or supplied air | 1,000× | HF bench maintenance, bulk chemical handling |
| IDLH or unknown | Any IDLH atmosphere | SCBA (45-min cylinder) | 10,000× | Gas leak response, confined space rescue |

## PPE Selection Trade-offs

| Factor | Half-Face Respirator | Full-Face Respirator | PAPR | SCBA |
|--------|---------------------|---------------------|------|------|
| Protection factor | 10× | 50× | 25-1,000× | 10,000× |
| Wear time (comfort) | 2-4 hours | 1-2 hours | 4-8 hours | 30-60 min (cylinder limit) |
| Mobility | Full | Full | Moderate (battery pack) | Limited (cylinder weight) |
| Communication | Clear | Muffled | Good (positive pressure) | Difficult |
| Cost per unit | $30-50 | $80-150 | $800-1,500 | $3,000-6,000 |
| Training required | Annual fit test | Annual fit test | Annual fit test + battery care | Monthly drill + medical clearance |

## Implementation Steps

1. **Conduct hazard assessment**: Document every chemical operation with exposure potential. For each, identify chemical(s), exposure route(s), and maximum foreseeable concentration.
2. **Select PPE by operation**: Use the PPE Selection Matrix below. Match cartridge type to chemical class (acid gas = yellow, organic vapor = black, P100 = magenta).
3. **Fit test all respirator users**: Qualitative (saccharin/bitrex taste test) or quantitative (portacount, fit factor ≥100 for half-face, ≥500 for full-face). Annual retest.
4. **Establish cartridge change schedule**: Based on breakthrough time data, not subjective detection. Post change schedule at every respirator storage location.
5. **Train on donning/doffing**: Practice prevents self-contamination during removal. Verify seal check before every use.
6. **Inspect and maintain**: Daily user inspection. Monthly SCBA inspection. Annual flow test for PAPR/SCBA.

## PPE Selection Matrix

## Chemical Handling PPE by Operation

| Operation | Respiratory | Hand | Eye/Face | Body |
|-----------|------------|------|----------|------|
| HF handling (<50%) | Full-face respirator with acid gas cartridge | Neoprene or nitrile (double-glove, 0.5 mm) | Full-face shield over goggles | Acid-resistant apron (neoprene), sleeve covers |
| HF handling (>50%) | Full-face SCBA if in enclosed area | Neoprene or nitrile (double-glove, 0.8 mm) + under-glove | Full-face shield + chemical goggles | Full acid suit (PVC/neoprene), boots, apron |
| Silane cylinder change | Supplied air (SCBA) in gas cabinet | Nitrile chemical gloves | Full-face shield + goggles | Flame-resistant coverall (Nomex) + chemical apron |
| Arsine/phosphine work | Supplied air (SCBA or airline) | Nitrile chemical gloves | Full-face respirator (if SCBA, integrated) | Chemical suit (Tyvek/Saranex) |
| Piranha solution preparation | Full-face respirator with acid/organic cartridge | Acid-resistant gloves (neoprene, 0.5 mm) | Full-face shield | Acid-resistant apron, sleeve covers, face shield |
| Wet bench operation | Half-face or full-face with acid gas cartridge | Nitrile gloves (0.2-0.3 mm) | Safety glasses with side shields | Lab coat (flame-resistant) |
| Solvent handling | Half-face with organic vapor cartridge | Nitrile gloves (0.2-0.3 mm) | Safety glasses or goggles | Flame-resistant lab coat |
| CMP operation | Half-face with P100 particulate | Nitrile gloves | Splash goggles | Waterproof apron |

## Respiratory Protection

## Respirator Types for Semiconductor Operations

**Half-face elastomeric respirator**:
- Protection factor: 10× (reduces exposure to 1/10th of ambient concentration)
- Use when: Airborne concentrations up to 10× PEL, adequate oxygen present, contaminant identified
- Cartridge selection by color code:
  - Magenta (P100): Particulate filtration (99.97% at 0.3 μm) — for dust, fume, mist
  - Black (organic vapor): Solvents, organic compounds — isopropanol, acetone, PGMEA, NMP
  - Yellow (acid gas): HF, HCl, Cl₂, HNO₃, SO₂ fumes
  - Green (ammonia): NH₃ gas
  - Multicolor/combo: P100 + acid gas, P100 + organic vapor — for mixed exposures in wet benches
- Cartridge change schedule: Based on breakthrough time, not subjective detection. For semiconductor applications, establish change schedule from manufacturer data or air sampling results. Typical: organic vapor cartridges changed after 8 hours of use or when odor detected (whichever first). Acid gas cartridges changed after each shift in continuous acid exposure.
- Fit testing: Required annually (OSHA 29 CFR 1910.134). Qualitative (taste test with saccharin or bitrex) or quantitative (portapcount, measured fit factor ≥100 for half-face). No facial hair in seal area

**Strengths**:
- Lowest cost respiratory protection ($30-50 per unit) for moderate exposure levels
- Lightweight and compact — minimal interference with vision, communication, and manual tasks
- Widest cartridge selection — color-coded cartridges for every chemical class encountered in fabs
- Compatible with safety glasses and hard hats — no interference with other PPE
- Comfortable for extended wear (2-4 hours) in non-IDLH environments
- Simple donning/doffing — quick seal check before each use

**Weaknesses**:
- Lowest protection factor (10×) — insufficient for exposures above 10× PEL
- No eye protection — separate goggles or face shield required for chemical splash protection
- Requires tight face seal — facial hair, glasses, or facial structure can prevent adequate fit
- Cartridge breakthrough is invisible — no warning when acid gas cartridges are exhausted
- Breathing resistance increases as filters load — fatiguing during heavy physical exertion
- Cannot be used in oxygen-deficient atmospheres (<19.5% O₂)

**Full-face elastomeric respirator**:
- Protection factor: 50× (reduces exposure to 1/50th ambient)
- Use when: Airborne concentrations up to 50× PEL, eye protection needed against gas/vapor, splash risk
- Integrated face shield protects eyes from chemical exposure
- Same cartridge selection as half-face
- Fit factor requirement: ≥500 (quantitative fit test)

**Strengths**:
- 5× higher protection factor than half-face (50× vs. 10×) — covers exposures up to 50× PEL
- Integrated face shield — simultaneous eye and respiratory protection from chemical splash
- Tighter seal than half-face — larger sealing surface improves fit reliability
- Same cartridge ecosystem as half-face — no separate supply chain
- Better for acid and solvent operations — splash protection combined with respiratory protection

**Weaknesses**:
- More fatiguing for extended wear (1-2 hours) — larger seal area causes facial pressure and sweat
- Muffled communication — full facepiece distorts speech, making verbal instructions difficult
- Fogging risk — exhaled moisture condenses on lens unless anti-fog coating or nose cup is used
- Higher cost than half-face ($80-150 per unit)
- Requires quantitative fit testing (more expensive than qualitative)
- Peripheral vision reduced — facepiece frame limits side vision compared to half-face with safety glasses

**Powered air-purifying respirator (PAPR)**:
- Protection factor: 25-1,000× depending on facepiece type (loose-fitting hood: 25×; tight-fitting full-face: 1,000×)
- Use when: Extended wear required, facial hair prevents tight-fitting respirator seal, higher protection factor needed
- Battery-powered blower draws air through filters/cartridges and delivers filtered air to headpiece at 4-6 CFM
- Advantage: No breathing resistance (positive pressure), cooling airflow, integrated head/face/neck protection
- Typical semiconductor use: HF bench maintenance, chemical spill cleanup, bulk chemical dispensing

**Strengths**:
- No breathing resistance — battery-powered blower pushes filtered air, reducing worker fatigue
- Higher protection factor with loose-fitting hood (25×) — accommodates facial hair and glasses
- Up to 1,000× protection with tight-fitting full-face PAPR
- Cooling airflow — positive pressure air circulation reduces heat stress during extended operations
- Most comfortable respirator for long-duration tasks (4-8 hours continuous wear)
- Integrated head, face, and neck protection with hood-style headpiece

**Weaknesses**:
- High cost ($800-1,500 per unit) — 10-20× more expensive than half-face respirator
- Battery management required — 4-8 hour runtime, batteries need daily charging and replacement scheduling
- Bulky — battery pack and blower unit add weight and limit mobility in confined spaces
- Motor and blower generate noise — may interfere with hearing warning alarms
- Moving parts require more maintenance — blower, filters, and battery all need periodic inspection
- Loose-fitting hoods offer lower protection (25×) than tight-fitting versions

**Self-contained breathing apparatus (SCBA)**:
- Protection factor: 10,000×
- Use when: IDLH atmosphere, unknown atmosphere, oxygen deficiency, emergency response
- 30-60 minute air supply (45-minute cylinder most common)
- Semiconductor applications: Gas cabinet entry for arsine/phosphine leak response, enclosed space entry with potential toxic gas, emergency evacuation support
- Monthly inspection, annual flow test, cylinder hydrostatic test every 5 years

**Supplied-air respirator (airline)**:
- Protection factor: 50-1,000× (depending on facepiece)
- Continuous breathable air from compressed air source through hose (maximum 300 ft hose length)
- Semiconductor applications: Extended work in gas cabinet areas, VMB maintenance, toxic gas system repair
- Air quality requirements: Grade D breathing air (O₂ 19.5-23.5%, hydrocarbon vapor <5 ppm, CO <10 ppm, CO₂ <1,000 ppm, no objectionable odor)
- Backup: 5-10 minute escape cylinder required if airline could be severed

## Hand Protection

## Chemical-Resistant Glove Selection

Semiconductor operations require gloves selected for the specific chemicals handled, with appropriate thickness for the exposure duration and dexterity requirements:

**Glove materials and chemical resistance**:

| Material | Effective Against | Not Effective Against | Typical Thickness |
|----------|-------------------|----------------------|-------------------|
| Nitrile (NBR) | Oils, solvents, most acids, HF (dilute), bases | Ketones (MEK, acetone), chlorinated solvents | 0.1-0.5 mm |
| Neoprene (CR) | Acids (including HF), bases, alcohols, some solvents | Aromatic hydrocarbons (toluene, xylene), ketones | 0.3-0.8 mm |
| Butyl rubber (IIR) | Ketones, esters, gases (HF, HCl vapor) | Hydrocarbons, chlorinated solvents | 0.3-0.5 mm |
| Viton (FKM) | Aromatic hydrocarbons, chlorinated solvents, acids | Ketones, amines, esters | 0.3-0.5 mm |
| PVC | Acids, bases, some organics | Most solvents, aromatic hydrocarbons | 0.2-0.5 mm |
| Natural rubber (latex) | Dilute acids, bases, aqueous solutions | Oils, solvents, HF (degrades) | 0.1-0.3 mm |

**HF-specific glove requirements**:
- Primary glove: Neoprene or thick nitrile (0.5-0.8 mm). Neoprene preferred — better HF resistance with longer breakthrough time.
- Double-gloving: Mandatory for HF handling. Inner glove: thin nitrile (0.2 mm) for dexterity. Outer glove: neoprene or heavy nitrile (0.5+ mm) for protection.
- Inspection: Check for pinholes, tears, discoloration before each use. Replace immediately after any splash or suspected contact.
- Breakthrough time: For 49% HF, neoprene (0.5 mm) breakthrough time >8 hours. Nitrile (0.5 mm) breakthrough time 2-4 hours. Thin nitrile (0.2 mm): breakthrough time <30 minutes — never use as sole protection for HF.

**Glove donning and removal procedure**:
1. Inspect gloves visually before donning — no cracks, tears, swelling, discoloration
2. Check sizing — gloves too large allow chemical seepage into cuff; too small risk tearing
3. For double-gloving: Don inner gloves first, then outer gloves over the cuff of the lab coat
4. Removal: Peel outer glove off inside-out (touching only the exterior surface). Then remove inner glove by sliding fingers under the cuff and peeling off inside-out. Never touch the outer surface of either glove to bare skin during removal

## Eye and Face Protection

## Selection Criteria

**Safety glasses** (impact rated, ANSI Z87.1+):
- For: General lab work, low splash risk, particulate protection
- Not for: Chemical splash, liquid acid handling, HF work
- Features required: Side shields, polycarbonate lenses, anti-fog coating

**Chemical splash goggles**:
- For: Any liquid chemical handling, wet bench work, acid dispensing, HF operations
- Type: Indirect-vented (allows air circulation to reduce fogging, but splash-tight) or non-vented (maximum splash protection, fog risk)
- Seal: Soft elastomer (PVC or silicone) gasket that seals against face contour
- Fit: Must be worn over prescription glasses if needed (OTG — over-the-glass design)

**Full-face shield**:
- For: Over-goggles protection during pouring, mixing, dispensing, any operation with high splash probability
- Material: Polycarbonate, anti-fog treated
- Coverage: Full face from forehead to below chin, ear to ear
- Worn OVER safety glasses or goggles (not a replacement for primary eye protection)

**HF-specific eye protection**:
- Full-face shield + chemical goggles mandatory for any HF handling
- Eyewash stations within 10 seconds travel distance (approximately 8 meters unobstructed path)
- Calcium gluconate drops (1%) available at every HF station for emergency eye treatment

## Body Protection

## Chemical Suits and Aprons

**Lab coats**:
- Flame-resistant (FR) treated cotton or Nomex blend for general fab operations
- Length: Knee-length minimum. Full button or snap front (no open front)
- Sleeves: Full-length, buttoned at wrist. Never rolled up during chemical work
- Change frequency: Daily, or immediately after contamination. No taking contaminated coats into non-fab areas

**Chemical aprons**:
- Material selection: Neoprene (acid resistance, including HF), PVC (general acid/base), rubber (cost-effective for mild chemicals)
- Length: From chest to below knee
- Features: Adjustable neck strap, waist ties, no metal fasteners (corrode in acid environments)
- For HF: Neoprene apron mandatory. No vinyl or thin PVC (HF permeates rapidly)

**Full chemical suits** (for emergency response, bulk chemical handling, spill cleanup):
- Material: Tyvek-Saranex-Tyvek laminate (chemical barrier + physical strength) or specialized HF suit material
- Coverage: Head to toe, sealed at wrists and ankles
- Worn over: FR undergarments and chemical boots
- Boot material: PVC or nitrile over-boot, steel toe/shank, acid-resistant sole, mid-calf height minimum
- Decontamination: After use, suits are decontaminated (rinsed with water, checked for residual contamination) before doffing to prevent secondary exposure

## Cleanroom-Compatible PPE

Semiconductor cleanrooms require PPE that generates minimal particles while providing chemical protection:

**Cleanroom garment system** (ISO Class 1-5 environments):
- Bouffant cap: Covers all hair
- Hood: Covers head and neck, snap closure under chin
- Coverall: Full-body suit with snap closure, elastic at wrists and ankles
- Booties: Over-shoe covers with conductive sole (ESD), cleanroom-compatible
- Face mask: Low-particulate, filtration ≥95% (surgical mask or higher grade)
- Material: Woven polyester or polyester-carbon blend (low particle shedding, ESD control)
- Laundered in ultrapure water after each use

**Compatibility with chemical PPE**: When chemical work is performed in the cleanroom (wet bench maintenance, chemical changeout), the chemical PPE goes over the cleanroom garment. Chemical aprons and gloves are donned just before the operation and removed immediately after, before leaving the wet bench area.

## PPE Program Management

## Written Program Requirements

OSHA 29 CFR 1910.132 requires a written PPE program covering:

1. **Hazard assessment**: Document workplace hazards requiring PPE. Update when processes change.
2. **PPE selection**: Specify the type of PPE required for each task, with rationale based on hazard assessment.
3. **Fit testing**: Respiratory fit testing annually (and for each respirator model/make/size the worker uses).
4. **Training**: Before initial use, when PPE changes, when worker demonstrates inadequate knowledge. Documented with sign-off.
5. **Inspection and maintenance**: Daily user inspection. Periodic detailed inspection of SCBA, PAPR, and emergency-use equipment.
6. **Storage**: Clean, dry, designated storage. Chemical PPE separated from general PPE. Contaminated PPE in designated waste containers.

## PPE Training Topics

Workers handling semiconductor chemicals must be trained on:

- Which PPE is required for each operation and why
- How to properly don and doff PPE (avoiding self-contamination during removal)
- Limitations of PPE (no PPE provides 100% protection; chemical breakthrough times are finite)
- How to inspect PPE before use (look for tears, discoloration, stiffness, cracked facepieces, expired cartridges)
- When to replace PPE (after contamination, at end of change schedule, when defects found)
- Emergency PPE locations (SCBA, escape respirators, emergency showers, eyewash)
- Medical contraindications for respirator use (respirator medical evaluation required before first use)

## Specialized PPE Configurations

## HF Work Station PPE Kit

Every HF handling station must have a dedicated PPE kit containing:

- Neoprene gloves (pair, 0.5 mm minimum) — 2 pairs
- Nitrile inner gloves (pair, 0.2 mm) — 2 pairs
- Chemical splash goggles (indirect vent) — 1
- Full-face shield — 1
- Neoprene apron — 1
- Neoprene sleeve covers — 1 pair
- Calcium gluconate gel (2.5%, 25 g tube) — 2 tubes
- Calcium gluconate eye drops (1%) — 1 bottle
- HF emergency procedure card (laminated)
- Spill absorbent (calcium carbonate-based — neutralizes HF to CaF₂)
- Hazard sign ("HF Area — Authorized Personnel Only")

## Gas Leak Response PPE Kit

Pre-positioned at strategic locations near gas cabinets and VMBs:

- SCBA (45-minute cylinder, fully charged)
- Chemical suit (Tyvek-Saranex laminate, size range available)
- Chemical boots (PVC, steel toe)
- Chemical gloves (butyl rubber, for broad gas protection)
- Hard hat
- Two-way radio (intrinsically safe rated)
- Emergency procedure binder (gas-specific response cards)

## See Also

- [Chemical Safety & Toxicology](chemical-safety.md) — Chemical hazards driving PPE selection
- [Emergency Response](emergency-response.md) — Emergency PPE and first aid
- [Occupational Health](../health/occupational-health.md) — General PPE principles and fit testing
- [Polymers](../polymers/index.md) — Rubber and polymer materials for glove and suit fabrication



[← Back to EHS](index.md)
