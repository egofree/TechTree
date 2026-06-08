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

![A doctor wearing personal protective equipment for treating patients with COVID-19](../images/ehs/ehs_ppe.jpg)

> *Image: Dr. Javed Anees, CC0*

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

### Glove Breakthrough Times for Common Chemicals

Breakthrough time is the elapsed time between initial contact of a chemical with the glove exterior surface and the detection of the chemical on the interior surface. These values assume room temperature (23°C). Higher temperatures reduce breakthrough time by 30-50%.

| Chemical (concentration) | Nitrile 0.3 mm | Neoprene 0.5 mm | Butyl 0.5 mm | Viton 0.4 mm |
|--------------------------|----------------|-----------------|---------------|--------------|
| Sulfuric acid (50%) | >8 hr | >8 hr | >8 hr | >8 hr |
| Sulfuric acid (98%) | 2-4 hr | >8 hr | 4-8 hr | >8 hr |
| Hydrofluoric acid (49%) | 2-4 hr | >8 hr | >8 hr | >8 hr |
| Hydrochloric acid (37%) | >8 hr | >8 hr | >8 hr | >8 hr |
| Sodium hydroxide (50%) | >8 hr | >8 hr | >8 hr | >8 hr |
| Acetone | <10 min | <30 min | >8 hr | <10 min |
| Isopropanol | >8 hr | >8 hr | >8 hr | >8 hr |
| Toluene | <30 min | <1 hr | <10 min | >8 hr |
| Xylene | <30 min | <1 hr | <10 min | >8 hr |
| Trichloroethylene | <10 min | <30 min | <30 min | >4 hr |
| Methanol | 1-4 hr | 4-8 hr | >8 hr | >8 hr |
| Gasoline | <1 hr | 1-2 hr | <30 min | >8 hr |

**Rule of thumb for glove replacement**: If the breakthrough time is less than 2× the intended wear duration, select a different glove material or increase thickness. For example, handling toluene with nitrile gloves (breakthrough <30 min) is unsafe for tasks longer than 15 minutes. Use Viton instead.

### Glove Sizing

Properly sized gloves are essential for both dexterity and protection. Oversized gloves allow chemical seepage into the cuff and reduce tactile sensitivity. Undersized gloves stretch the material thin, reducing breakthrough time by 30-50% and causing hand fatigue.

| Glove Size | Hand Circumference (cm) | Hand Length (cm) | Typical User |
|-----------|------------------------|------------------|-------------|
| XS (6) | 14-16 | 15-16 | Small adult hands |
| S (7) | 17-18 | 17-18 | Many women |
| M (8) | 19-20 | 18-19 | Average adults |
| L (9) | 21-22 | 19-20 | Many men |
| XL (10) | 23-25 | 20-21 | Large hands |
| XXL (11) | 25+ | 21+ | Very large hands |

Measure hand circumference at the widest point (across the knuckles, excluding the thumb). Measure hand length from the wrist crease to the tip of the middle finger. When between sizes, choose the larger size for chemical protection (better to have slight excess cuff than stretched material) and the smaller size for precision work requiring maximum dexterity.

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

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Half-face respirator fit test fails (fit factor <100) | Facial hair in seal area, wrong size, or glasses interfering with seal edge | Remove all facial hair in seal contact zone; try different size (S/M/L); ensure glasses temples do not break seal edge; retest with quantitative portacount method |
| Acid gas cartridge breakthrough undetected — worker smells acid | Change schedule not based on breakthrough time data; relying on subjective odor detection | Implement cartridge change schedule from manufacturer breakthrough data; for continuous acid exposure, change cartridges after each shift; post change schedule at every respirator storage location |
| PAPR battery depletes before 4-hour rated runtime | Battery not fully charged or battery nearing end of cycle life | Verify battery charger is functioning and reaches full-charge indicator; replace batteries that no longer hold rated capacity (typically 2-3 year battery life); maintain daily charging schedule |
| Neoprene glove for HF handling shows discoloration after single use | Chemical degradation — glove material reaching breakthrough time for 49% HF | Replace gloves immediately; neoprene (0.5 mm) breakthrough time for 49% HF is >8 hours but degrades with flexing; use double-gloving protocol (0.2 mm nitrile inner + 0.5 mm neoprene outer); inspect before each use |
| Full-face respirator lens fogs during wet bench operation | Exhaled moisture condensing on lens — anti-fog coating worn or no nose cup installed | Replace anti-fog coated lens or install nose cup to direct exhaled breath away from lens; verify nose cup is properly seated; clean lens only with manufacturer-approved anti-fog solution |
| SCBA cylinder fails monthly pressure check | Cylinder valve slow leak or O-ring seal deteriorated | Replace valve O-ring; perform soap-bubble test on all connections; if cylinder body leak is found, remove from service and send for hydrostatic testing (required every 5 years); never repair a cylinder body leak in-house |
| Chemical splash goggles do not seal against face | Wrong size or prescription glasses interfering with elastomer gasket | Select OTG (over-the-glass) model for prescription wearers; try alternative gasket material (PVC vs. silicone) for better contour fit; verify gasket is not torn or hardened from chemical exposure |
| Tyvek chemical suit tears at wrist seal during doffing | Improper removal technique — pulling suit off by gripping wrist seal material | Retrain on doffing procedure: roll suit down from shoulders, avoid pulling at sealed cuff areas; dispose of torn suits immediately — compromised barrier provides no protection |
| Respirator user experiences difficulty breathing after 1 hour | Filter cartridges loaded — breathing resistance increased from particulate accumulation | Replace cartridges when breathing resistance noticeably increases; for P100 particulate filters, do not exceed manufacturer-rated service life; schedule cartridge changes based on exposure duration, not subjective feel |
| Calcium gluconate gel in HF workstation kit is hardened/expired | Monthly inspection missed — gel has exceeded shelf life or tube seal was broken | Replace with fresh 2.5% calcium gluconate gel immediately; verify all tubes in kit are sealed and within expiration date; assign monthly PPE kit inspection with documented sign-off |

## Safety

PPE programs carry inherent hazards when equipment fails, degrades, or is misapplied:

- **Glove breakthrough without visible warning**: Chemical permeation through glove material is invisible. Nitrile (0.2 mm) handling 49% HF has a breakthrough time under 30 minutes — the glove appears intact while fluoride ions pass through. Neoprene (0.5 mm) degrades visibly after HF contact (discoloration, stiffening) but permeation begins 2-4 hours before visual signs appear. Enforce time-based glove changes derived from manufacturer permeation data, not visual inspection. Double-glove for all HF work (0.2 mm nitrile inner + 0.5 mm neoprene outer).
- **Respirator fit-testing hazards**: Qualitative fit testing uses saccharin or bitrex aerosol. Bitrex (denatonium benzoate) at test concentrations causes gagging and nausea in sensitive individuals — perform tests in a ventilated area with a sink available. Quantitative fit testing (portacount) requires the test subject to wear the respirator for 15-20 minutes performing exercises (bending, talking, turning head) — subjects with undiagnosed claustrophobia may experience panic attacks inside the full-face respirator hood. Medical clearance questionnaire (OSHA Appendix C) screens for cardiac and pulmonary conditions before respirator use.
- **SCBA cylinder and regulator failures**: Carbon-wrapped SCBA cylinders (4500 psi) develop stress corrosion cracking when exposed to chemical splashes containing strong acids. A cylinder struck by concentrated H₂SO₄ during a response scenario can rupture catastrophically. Inspect cylinder exteriors after every use in chemical environments — any discoloration, scoring, or chemical contamination requires removal from service and hydrostatic retest. Regulator free-flow failure (stuck open) empties a 45-minute cylinder in 8-10 minutes. Train users to recognize the vibration and sound of a free-flowing regulator and activate the bypass valve immediately.
- **Chemical suit heat stress**: Tyvek-Saranex laminate suits have zero moisture vapor transmission — the wearer's sweat cannot evaporate. At ambient temperatures above 25°C, core body temperature rises 1°C per 30 minutes of moderate activity inside a chemical suit. Limit chemical suit work to 20-minute intervals with 10-minute cooling breaks (remove suit, hydrate, fan cooling). Monitor for heat exhaustion symptoms: dizziness, nausea, cessation of sweating (heat stroke — medical emergency). Emergency responders in full chemical suits during summer months are at highest risk.

## See Also

- [Chemical Safety & Toxicology](chemical-safety.md) — Chemical hazards driving PPE selection
- [Emergency Response](emergency-response.md) — Emergency PPE and first aid
- [Occupational Health](../health/occupational-health.md) — General PPE principles and fit testing
- [Polymers](../polymers/index.md) — Rubber and polymer materials for glove and suit fabrication

## General Industrial PPE Specifications

Beyond semiconductor-specific operations, the following PPE specifications cover the most common industrial hazards encountered during civilization bootstrapping.

### Hard Hat Specifications

| Type | Impact Rating | Voltage Rating | Application | Material |
|------|-------------|---------------|-------------|----------|
| Type I (top impact) | 8 ft-lb impact | Class E (20,000 V) | Construction, mining, general industrial | HDPE, ABS, or fiberglass |
| Type II (top + lateral impact) | 8 ft-lb top + lateral | Class G (2,200 V) | Heavy construction, demolition | HDPE or ABS |

Replace hard hat if: cracked shell, faded color (UV degradation), suspension webbing torn or stretched, any impact that dents or deforms the shell, or after 5 years of use (UV degrades the polymer). Shell service life is typically 5 years from first use; suspension replacement every 12 months.

### Safety Footwear Ratings

| Standard | Impact Resistance | Compression Resistance | Metatarsal Protection | Application |
|----------|------------------|----------------------|----------------------|-------------|
| ASTM F2413 I/75 | 75 ft-lb impact | 2,500 lb compression | No | General industrial |
| ASTM F2413 I/75 Mt/75 | 75 ft-lb impact | 2,500 lb compression | 75 ft-lb metatarsal | Foundry, heavy construction |
| ASTM F2413 I/75 EH | 75 ft-lb impact | 2,500 lb compression | Electrical hazard (18 kV) | Electrical work |

Steel toe caps protect against impact and compression. Composite (carbon fiber or plastic) toe caps provide the same protection with less weight and no cold temperature conduction, but are more expensive. Metatarsal guards (internal or external) protect the upper foot from falling objects and are mandatory in foundries, heavy construction, and mining. Chemical-resistant boots for acid and solvent operations: PVC or nitrile over-boots worn over the safety boot, extending above the ankle minimum, mid-calf preferred for liquid handling.

### Fall Protection Equipment

Fall protection is required at heights above 1.8 m (6 feet) in general industry and above 2.4 m (8 feet) in construction. A fall arrest system has three components:

1. **Anchorage point**: Must support 2,270 kg (5,000 lb) per attached worker. Structural steel beams, engineered roof anchors, and concrete-embedded anchor bolts are acceptable. Pipe rails, conduit, and vent stacks are not.
2. **Body harness**: Full-body harness distributes fall forces across thighs, pelvis, chest, and shoulders. The dorsal D-ring between the shoulder blades is the attachment point. Harnesses must fit snugly; loose harnesses allow the worker to slip out during a fall. Inspect webbing for cuts, abrasion, UV fading, and broken stitching before each use.
3. **Lanyard or SRL**: Shock-absorbing lanyard limits maximum arrest force to 8 kN (1,800 lb) on the worker's body. Self-retracting lifeline (SRL) locks within 0.6 m of fall onset. Lanyard length plus deceleration distance plus worker height must be less than the distance to the ground (calculate total fall distance: lanyard length + 1.0 m deceleration + 1.8 m worker height + 1.0 m safety margin = minimum clearance required below anchorage).

**Why fall protection matters**: A fall from 3 meters onto a hard surface generates approximately 20 kN of force on the body, enough to cause fatal head injuries or spinal fracture. The shock absorber in a fall arrest lanyard tears open progressively, extending the stopping distance and reducing peak force to below 8 kN.

### Ventilation Requirements for PPE Areas

PPE storage, fit-testing, and donning/doffing areas need adequate ventilation to prevent accumulation of chemical vapors from contaminated equipment.

| Area | Minimum Air Changes/Hour (ACH) | CFM per Person | Notes |
|------|-------------------------------|----------------|-------|
| PPE storage room | 4-6 ACH | 20 CFM | Prevents buildup of chemical odors on stored equipment |
| Respirator fit-test area | 8-12 ACH | 30 CFM | Bitrex and saccharin aerosols require extraction during qualitative testing |
| Chemical suit donning/doffing | 12-15 ACH | 40 CFM | Doffing releases chemical vapors from suit exterior; high ventilation protects the worker during removal |
| SCBA charging room | 6-8 ACH | 25 CFM | Compressed air systems generate heat; prevents accumulation of lubricant vapors from compressors |
| Emergency shower/eyewash area | 6 ACH | 20 CFM | Moisture and diluted chemicals require ventilation to prevent slip hazards and vapor buildup |

Air changes per hour (ACH) is calculated as: ACH = (CFM × 60) / room volume in cubic feet. Example: a 10 × 12 × 8 foot room (960 ft³) needs 4 ACH × 960 / 60 = 64 CFM of supply air at minimum.

---
*Part of the [Bootciv Tech Tree](../index.md) • [EHS](./index.md) • [All Domains](../index.md)*
