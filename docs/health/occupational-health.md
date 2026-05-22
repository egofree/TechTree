# Occupational Health

> **Node ID**: health.occupational-health
> **Domain**: [Health](./)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`metals`](../metals/index.md), [`energy`](../energy/index.md)
> **Timeline**: Years 10-25
> **Outputs**: hazard_controls, exposure_monitoring, protective_equipment, safety_protocols

## Problem

Industrial processes generate hazards: toxic fumes from smelting, silica dust from mining and glassmaking, noise from forging and machining, chemical exposures from acid production and electroplating, radiation from welding and X-ray sources. Without systematic hazard identification and control, workers suffer chronic illness, disability, and premature death. Occupational health practice applies a control hierarchy (eliminate, substitute, engineer, administrate, protect) to reduce exposures to safe levels. This page covers the specific hazards encountered in bootstrapping an industrial civilization and the control measures for each.

## Hazard Identification

### Chemical Hazards

Airborne chemical exposures are regulated against Permissible Exposure Limits (PELs, OSHA) and Threshold Limit Values (TLVs, ACGIH). Both define the maximum airborne concentration a worker can breathe for an 8-hour time-weighted average (TWA) without adverse health effects. Key industrial substances:

| Substance | PEL (TWA) | TLV (TWA) | Health Effect | Primary Sources |
|-----------|-----------|-----------|---------------|-----------------|
| Lead (Pb) | 50 μg/m³ | 50 μg/m³ | Neurotoxicity, anemia, kidney damage | Smelting, battery production, soldering |
| Silica (SiO₂) | 50 μg/m³ | 25 μg/m³ | Silicosis (irreversible lung fibrosis) | Mining, stone cutting, glassmaking, foundry |
| Asbestos | 0.1 fiber/cm³ | 0.1 fiber/cm³ | Mesothelioma, asbestosis, lung cancer | Insulation, fireproofing, cement pipe |
| Carbon monoxide | 50 ppm | 25 ppm | Asphyxiation (binds hemoglobin 200× faster than O₂) | Combustion engines, furnaces, smelting |
| Hydrogen sulfide | 20 ppm (ceiling) | 5 ppm | Respiratory paralysis at high dose | Petroleum refining, sewage, tanning |
| Sulfur dioxide | 5 ppm | 0.25 ppm | Respiratory irritation, bronchospasm | Ore roasting, sulfuric acid production |
| Hydrofluoric acid | 3 ppm | 0.5 ppm | Severe chemical burns, systemic fluoride poisoning | Glass etching, silicon wafer processing |

Skin absorption adds another exposure route. Hydrofluoric acid penetrates skin rapidly and binds tissue calcium, causing deep tissue necrosis and potentially fatal hypocalcemia. A hand exposure to 2.5% body surface area with concentrated HF can deliver a lethal systemic dose. Phenol, aniline, and certain solvents (carbon tetrachloride, benzene) also absorb through skin in hazardous quantities.

### Physical Hazards

**Noise**: Continuous noise above 85 dB(A) as an 8-hour TWA requires a hearing conservation program (monitoring, audiometric testing, hearing protection). Above 90 dB(A), engineering controls or administrative limits on exposure time are mandatory. For reference: 85 dB is a milling machine at 1 meter; 95 dB is a forge hammer; 105 dB is a riveting machine. Every 3 dB increase halves the permissible exposure time: 90 dB = 8 hours, 93 dB = 4 hours, 96 dB = 2 hours, 99 dB = 1 hour. Noise-induced hearing loss is irreversible and cumulative.

**Vibration**: Hand-arm vibration from pneumatic tools (chipping hammers, grinders, jackhammers) at 2.5-5.0 m/s² causes vibration white finger (Raynaud's phenomenon): numbness, blanching, and reduced grip strength. The ISO 5349 standard limits daily exposure to 5 m/s² (8-hour energy-equivalent). Whole-body vibration from heavy vehicles and large presses causes lower back disorders. Isolation mounts and suspension seats reduce whole-body vibration transmission by 40-60%.

**Radiation**: Ionizing radiation follows the ALARA principle (As Low As Reasonably Achievable). Annual occupational dose limit: 20 mSv effective dose averaged over 5 years, with no single year exceeding 50 mSv (ICRP). Sources in bootstrapping include X-ray tubes (nondestructive testing of welds and castings), radioactive isotopes (thickness gauges, density measurement), and naturally occurring radioactive material (uranium and thorium in mineral processing). Non-ionizing UV radiation from welding arcs causes photokeratitis (welder's flash) within seconds of unprotected exposure. Infrared radiation from furnaces and molten metal causes cataracts with chronic exposure.

**Temperature extremes**: Heat stress (furnace areas, summer outdoor work) risks heat exhaustion and heat stroke. Wet-bulb globe temperature (WBGT) above 28°C requires work-rest cycles and hydration. Cold stress (outdoor winter work, cold storage) risks hypothermia and frostbite.

### Biological Hazards

Waterborne diseases (cholera, typhoid, dysentery) spread through contaminated water supplies, a constant threat during early infrastructure phases. Bloodborne pathogens (hepatitis B and C, HIV) are a risk in medical settings. Vector-borne diseases (malaria, dengue) depend on geography and sanitation. Industrial microbiology hazards include bacterial contamination of cutting fluids (Legionella, Mycobacterium) and fungal growth in poorly ventilated spaces.

### Ergonomic Hazards

The NIOSH lifting equation sets a recommended weight limit (RWL) based on horizontal distance, vertical position, frequency, and twisting angle. For a standard lift (75 cm height, close to body, occasional frequency, no twist), the RWL is 23 kg. Exceeding this increases the risk of musculoskeletal disorders (lumbar disc herniation, muscle strain). Repetitive motion tasks (assembly line work, grinding, hammering) cause cumulative trauma disorders: carpal tunnel syndrome, tendinitis, epicondylitis.

## Control Hierarchy

Controls are applied in order of effectiveness. Higher-level controls protect all workers passively; lower-level controls depend on individual compliance and behavior.

### Elimination

Remove the hazard entirely. Use a non-toxic solvent instead of benzene. Eliminate manual lifting with mechanical aids. Substitute a less hazardous material: water-based cleaners instead of chlorinated solvents, lead-free solder (tin-silver-copper) instead of tin-lead.

### Engineering Controls

Physical modifications to the workplace that isolate workers from hazards:

**Ventilation**: Local exhaust ventilation (LEV) captures contaminants at the source before they reach the breathing zone. Key design parameters: capture velocity (0.5-1.0 m/s for gases and vapors, 1.0-2.5 m/s for dusts, 2.5-10 m/s for heavy particles from grinding), hood design (enclosing hood > receiving hood > capturing hood), and duct velocity (minimum 10 m/s to prevent dust settling). General dilution ventilation provides 4-12 air changes per hour for comfortable occupancy, but is inadequate for toxic substance control. Fume hoods in chemistry labs maintain face velocity of 0.4-0.6 m/s.

**Enclosure**: Fully enclose noisy machinery (compressors, generators) with acoustic panels. Sound transmission loss: 20-30 dB with a sealed enclosure of 16-gauge sheet steel lined with 50 mm mineral wool. Enclosure must include vibration-isolated mounting and sealed access doors.

**Machine guarding**: Physical barriers preventing contact with moving parts. Point-of-operation guards cover the danger zone (blade, nip point, pinch point) while allowing the operator to feed material. Interlocked guards shut down the machine when opened. Fixed guards (bolted in place) for transmissions, flywheels, and shafts.

**Isolation**: Place hazardous processes in separate buildings or rooms with negative air pressure (air flows in, not out). Operators monitor from outside via windows or cameras. Remote handling tools for radioactive or highly toxic materials.

### Administrative Controls

Work procedures and policies that reduce exposure duration or number of exposed workers:

- **Time limits**: Rotate workers through hazardous tasks so no individual exceeds PEL. If a process generates 100 μg/m³ of lead (2× PEL), limit each worker to 4 hours per shift.
- **Training**: Hazard communication (knowing what chemicals are present, reading SDS, understanding PELs), safe work procedures, emergency response.
- **Housekeeping**: Regular cleaning prevents accumulation of toxic dusts (lead, silica) on surfaces. Wet methods (hosing, mopping) suppress dust resuspension. Dry sweeping disperses settled dust back into the air.
- **Medical surveillance**: Pre-employment and periodic medical examinations for workers in hazardous exposures. Blood lead level testing for lead workers (action level: 40 μg/dL, removal at 50 μg/dL). Spirometry for workers exposed to respiratory hazards. Audiometry for noise-exposed workers (annual testing, comparing to baseline).

### Personal Protective Equipment (PPE)

The last line of defense, used when higher-level controls cannot reduce exposure below acceptable limits. PPE must be selected for the specific hazard, fitted to the individual, and maintained in working condition.

**Respiratory protection**:
- **N95 disposable respirator**: Filters 95% of 0.3 μm particles (non-oil aerosols). For silica, metal fumes, general dust. Does not protect against gases or oxygen deficiency. Must form a tight seal against the face; facial hair breaks the seal. Fit-test annually.
- **Half-face elastomeric respirator**: Reusable rubber facepiece with replaceable cartridges. P100 particulate filters (99.97% efficiency) or chemical cartridges (organic vapor, acid gas, ammonia, depending on cartridge color coding). Protection factor: 10× (reduces exposure to 1/10th of ambient). For exposures up to 10× PEL.
- **Full-face respirator**: Same as half-face but with a face shield protecting eyes from splashes and irritants. Protection factor: 50×. For exposures up to 50× PEL.
- **Supplied air (SCBA or airline)**: For immediately dangerous to life or health (IDLH) atmospheres, oxygen deficiency, or unknown contaminants. SCBA: 30-60 minute air supply in a backpack. Airline: continuous supply from a compressed air source through a hose.

**Hearing protection**:
- **Foam earplugs**: Expandable polyurethane or PVC foam, rolled and inserted into the ear canal. Noise Reduction Rating (NRR): 25-33 dB. Actual protection is 50-75% of labeled NRR due to imperfect fit. Disposable, cheap.
- **Earmuffs**: Hard plastic cups with foam-filled cushions that seal around the ear. NRR: 15-30 dB. More consistent fit than earplugs. Can be combined with earplugs for 5-10 dB additional protection (not additive: 33 dB plugs + 25 dB muffs ≈ 38 dB, not 58 dB).

**Eye and face protection**:
- **Safety glasses**: Polycarbonate lenses (impact-rated to ANSI Z87.1), side shields. For flying particles, sparks. Do not seal against the face; liquids and dust can enter from the sides.
- **Chemical splash goggles**: Indirect-venting or non-venting goggle that seals against the face. For liquid chemical splashes (acid, caustic, solvents).
- **Face shield**: Clear polycarbonate shield covering the full face. Worn over safety glasses. For grinding, chipping, chemical pouring, and any operation with a splash risk.

**Hand protection**:
- **Leather or cut-resistant gloves**: For mechanical hazards (sharp edges, abrasion, moderate heat). Kevlar and Dyneema fibers provide cut resistance (ANSI cut levels A1-A9) with good dexterity.
- **Chemical-resistant gloves**: Nitrile (most versatile, resists oils, solvents, acids), butyl rubber (ketones, esters), neoprene (acids, bases, alcohols), Viton (chlorinated solvents, aromatic hydrocarbons). Glove thickness 0.1-0.5 mm. Breakthrough time (time for chemical to permeate the glove material) determines safe wear duration. Replace immediately after any visible degradation or when breakthrough time is exceeded.

## Mining-Specific Controls

**Methane monitoring**: Methane accumulates in coal mines and some hard-rock mines. Concentration above 1% triggers an alarm. Above 5% (lower explosive limit), the atmosphere is explosive. Above 15%, the mixture is too rich to ignite but will explode if diluted. Methane detectors use catalytic bead sensors (0-5% range) or infrared sensors. Continuous monitoring with alarms at 1% and evacuation at 5% is standard practice.

**Dust suppression**: Respirable coal mine dust (≤10 μm, reaches deep lung) is controlled by water sprays at the cutting face (10-30 L/min), ventilation (minimum 0.5 m/s air velocity at the face), and respiratory protection. Quartz content above 5% in the dust reduces the PEL proportionally (silica is more toxic than coal dust alone).

**Ventilation**: Mine ventilation systems provide fresh air, dilute gases (methane, CO, NOx from blasting), and remove dust. Main fans move 50-200 m³/s of air through the mine. Air quantities are calculated based on the maximum number of workers, diesel equipment horsepower, and expected gas emission rates.

## Industrial Process Controls

**Lockout/Tagout (LOTO)**: Before any maintenance on powered equipment, the energy source is locked out (physical padlock preventing switch activation) and tagged (warning label identifying the worker who applied the lock). Multiple workers each apply their own lock. Equipment cannot be re-energized until every lock is removed. LOTO prevents amputations, electrocutions, and crushing injuries from unexpected machine startup. Applies to electrical, hydraulic, pneumatic, thermal, and mechanical (spring tension, gravity) energy sources.

**Confined space entry**: Tanks, vessels, silos, sewers, and similar spaces have limited entry/exit, are not designed for continuous occupancy, and may contain hazardous atmospheres (oxygen deficiency, toxic gases, explosive mixtures). Entry procedure: test atmosphere before entry (O₂ ≥19.5%, flammable gas <10% LEL, toxic gases below PEL), ventilate continuously, post an attendant at the entry point, maintain communication, and have rescue equipment (tripod, winch, harness) immediately available. Confined space fatalities frequently involve multiple deaths as rescuers enter without proper equipment.

**Chemical storage and handling**: Store incompatible chemicals separately (acids from bases, oxidizers from organics, flammables in approved cabinets). Secondary containment (berms, drip trays) captures spills. Eyewash stations and emergency showers within 10 seconds travel distance (about 15 meters) of any chemical handling area. Flush for 15 minutes minimum after chemical eye or skin contact.

## Exposure Monitoring

### Air Sampling

Personal air sampling collects contaminants from the worker's breathing zone (within 30 cm of the nose and mouth). A battery-powered sampling pump draws air at a calibrated flow rate (1-2 L/min for particulates, 50-200 mL/min for gases) through a collection medium. For particulates: a pre-weighed filter cassette (37 mm diameter, 0.8 μm pore size mixed cellulose ester membrane) captures dust. Weigh the filter before and after sampling on a microbalance (0.01 mg resolution) to determine mass concentration. For silica analysis, the filter is digested and analyzed by X-ray diffraction or infrared spectrophotometry.

For gases and vapors: sorbent tubes (activated charcoal for organic vapors, silica gel for polar compounds) trap the contaminant. The tube is desorbed with solvent (carbon disulfide for charcoal) and analyzed by gas chromatography. Passive dosimeters (diffusion-based badges, no pump required) provide lower accuracy but are cheaper and simpler for routine monitoring.

Direct-reading instruments give real-time concentration data. Photoionization detectors (PID) measure volatile organic compounds with a UV lamp (10.6 eV). Electrochemical sensors detect specific gases (CO, H₂S, O₂, Cl₂) in the ppm range. Combustible gas indicators (catalytic bead sensors) measure flammable gas concentration as a percentage of the lower explosive limit (LEL).

### Noise Measurement

A sound level meter measures sound pressure level in dB(A) at a specific location. An integrating sound level meter (dosimeter) worn by the worker logs the 8-hour TWA exposure directly. Octave band analysis (measuring sound level in 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, and 16000 Hz bands) identifies dominant frequencies for engineering control design. A 1000 Hz dominant tone suggests a fan or motor problem; low-frequency rumble (63-250 Hz) suggests large machinery or ventilation ducts.

### Biological Monitoring

Blood and urine testing provides direct evidence of internal dose, complementing air sampling. Blood lead level (BLL) reflects lead exposure over the prior 30-60 days (lead half-life in blood is ~30 days). Urinary mercury reflects recent inorganic mercury exposure. Urinary arsenic speciation distinguishes toxic inorganic arsenic from harmless organic arsenic from seafood consumption. Biological monitoring accounts for all exposure routes (inhalation, ingestion, skin absorption) and individual differences in metabolism.

### Ventilation System Design

Effective local exhaust ventilation requires careful engineering beyond simply attaching a fan to a duct. The system consists of a hood (capture point), ductwork (transport), air cleaner (filtration or scrubbing), fan (motive force), and stack (discharge). Each component must be correctly sized. The fan must deliver the required airflow at the calculated system pressure drop. Undersized ducts increase velocity and pressure drop, wasting energy. Oversized ducts allow dust to settle, creating a fire or blockage risk.

Duct design: maintain transport velocity above the minimum for the material being conveyed (10 m/s for fine dust, 15-20 m/s for heavy particles, 5-10 m/s for gases and vapors). Use round ducts (better flow characteristics, less dust accumulation than rectangular). Minimize bends (use radius ≥2× duct diameter). Provide cleanout access ports every 3-6 meters for dust accumulation removal. Calculate total system static pressure (friction loss in ducts + dynamic losses at fittings + hood entry loss + filter/scrubber pressure drop) and select a fan rated to deliver the design airflow at this pressure with a 10-20% safety margin.

## Integration Points

| Bootstrapping Phase | Primary Hazards | Priority Controls |
|---------------------|-----------------|-------------------|
| Mining and quarrying | Silica dust, methane, noise, heavy lifting | Ventilation, dust suppression, rock bolts, hearing protection |
| Smelting and foundry | Lead fumes, CO, heat stress, noise | LEV at furnace, CO monitors, work-rest cycles, hearing protection |
| Glassmaking | Silica dust, heat, chemical burns (HF) | Dust control, heat shields, HF-specific PPE and calcium gluconate gel |
| Metal fabrication | Noise, welding fumes, UV radiation, amputation | Machine guards, welding ventilation, auto-darkening helmets |
| Chemical production | Toxic gases, acids, solvents, explosion | Process enclosure, gas detection, blast-resistant construction, emergency showers |
| Electrical generation | Electrocution, arc flash, noise | Lockout/tagout, arc-rated clothing, insulated tools, approach boundaries |
| Semiconductor manufacturing | HF, silane, arsine, cleanroom chemicals | Gas cabinets with exhaust, continuous monitoring, automatic shutoff valves |

## Emergency Response

### Chemical Exposure First Aid

**Skin contact**: Remove contaminated clothing immediately (clothing holds chemical against the skin, extending exposure). Flush with copious water for a minimum of 15 minutes. For hydrofluoric acid, apply calcium gluconate gel (2.5%) to the affected area after flushing: the calcium ions bind free fluoride ions, preventing deep tissue destruction. Keep calcium gluconate gel stocked wherever HF is handled; delay beyond 30 minutes allows fluoride to penetrate deeply, causing irreversible tissue necrosis and potentially fatal hypocalcemia.

**Eye contact**: Flush at eyewash station for 15-30 minutes, holding eyelids open. Acid burns cause immediate pain; alkali burns (NaOH, KOH, ammonia) may feel less painful initially but cause more severe damage because alkalis saponify cell membranes and penetrate deeper. All chemical eye exposures require ophthalmological evaluation after first aid.

**Inhalation**: Move the exposed person to fresh air. For CO exposure (which binds hemoglobin with 200× the affinity of oxygen), administer 100% oxygen by non-rebreather mask. The half-life of carboxyhemoglobin is 4-6 hours on room air, reduced to 60-90 minutes on 100% oxygen. Severe cases require hyperbaric oxygen therapy.

**Ingestion**: Do not induce vomiting for corrosive substances (acids, alkalis): re-exposure of the esophagus causes additional damage. Dilute with water or milk if the person is conscious and able to swallow. For suspected poisoning, identify the substance and consult poison control for substance-specific treatment.

### Fire and Explosion

Flammable liquid storage in approved cabinets (constructed of 18-gauge steel, with 1.5-inch air space at bottom, sides, and top for ventilation, self-closing doors). Class I flammable liquids (flash point below 37.8°C): store in approved safety cans with spring-loaded caps and flame arrestors. Bond and ground all containers during dispensing to prevent static discharge ignition. For gas cylinder storage: secure cylinders upright with chains or straps, separate fuel gases from oxidizers by 6 meters or a 30-minute fire-rated wall. Acetylene cylinders must never be stored or used on their side (acetone solvent can enter the regulator).

## Key Deliverables

- Hazard identification protocols for all industrial processes
- Local exhaust ventilation systems for smelting, chemical processing, grinding
- Respiratory protection program (N95 for particulates, half-face for gases)
- Hearing conservation program (monitoring, protection, audiometry)
- Machine guarding standards for all powered equipment
- Chemical safety program (SDS, storage, spill response)
- Lockout/tagout procedures for equipment maintenance
- Confined space entry procedures
- Mine ventilation and gas monitoring systems
- Medical surveillance programs (blood lead, spirometry, audiometry)
- Emergency response procedures (chemical exposure first aid, fire response)
- Flammable material storage standards (cabinets, grounding, ventilation)
- Emergency response procedures with specific first aid for HF, CO, and acid/alkali exposure
- Ventilation system design guidelines (duct sizing, fan selection, hood capture velocities)

## Recordkeeping and Documentation

Occupational health programs depend on accurate records. Exposure monitoring results are logged per worker, with date, task description, sampling duration, and measured concentration. Medical surveillance records (audiograms, spirometry results, blood lead levels) are maintained for the duration of employment plus 30 years (OSHA requirement). These longitudinal records detect trends: a worker whose audiogram shows a 10 dB shift at 4000 Hz relative to baseline has early noise-induced hearing loss, even if the absolute threshold is still within normal range. Similar logic applies to spirometry (FEV1 decline exceeding 15% per year indicates accelerated lung function loss, triggering investigation of exposure controls).

Injury and illness logs (OSHA 300 log or equivalent) track every recordable incident: any work-related injury requiring medical treatment beyond first aid, any work-related illness diagnosis, any lost workday. Analysis of these logs identifies patterns: a cluster of hand injuries on a particular machine points to a guarding deficiency; repeated chemical splash incidents at a specific workstation indicate a process design flaw.

Training records document who received what training, when, and from whom. Refresher training intervals: annual for hazard communication and respiratory protection, periodic for lockout/tagout (whenever procedures change or when audits reveal deficiencies), and initial for all new hires before they begin work with hazardous materials or equipment.

---

**Emergency Response**: Every industrial facility needs an emergency action plan covering fire (extinguisher types: ABC dry chemical for general, CO₂ for electrical, water for paper/wood only), chemical spill (absorbent materials, neutralization agents, evacuation distances for toxic releases — H₂SO₄ spill: evacuate 50 m radius minimum), medical emergency (first aid station location, AED placement within 3-minute walk of any point, emergency phone numbers posted), and rescue (confined space rescue team with SCBA, rope rescue capability for elevated work). Drill frequency: fire evacuation quarterly, chemical release annually, full response exercise annually.

*Part of the [Bootciv Tech Tree](../) · [Health](./) · [All Domains](../)*

[← Back to Health](index.md)
