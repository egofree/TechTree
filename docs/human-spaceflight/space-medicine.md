# Space Medicine

> **Node ID**: human-spaceflight.space-medicine
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `health`, `ehs.radiation-safety`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 60+
> **Outputs**: crew_medical
> **Critical**: Yes

Space medicine is the discipline that keeps human beings alive and functional in the most hostile environment biology has ever encountered. Microgravity unloads the musculoskeletal system, redistributes two litres of fluid from the legs to the head, suppresses the immune system, and remodels the eye. Radiation pours through the hull at 50-100 mSv per six-month ISS increment, and a single coronal mass ejection can deliver a lethal dose in hours without warning. The vacuum outside is one millimetre of pressure vessel away. Space medicine is the sum of screening, monitoring, countermeasures, and emergency protocols that stand between a crew and death in that environment.

This article covers four process areas: [crew selection](./space-medicine.crew-selection.md) — who flies and why, [countermeasures](./space-medicine.countermeasures.md) — the 2.5-hour daily exercise and pharmaceutical arsenal that fights deconditioning, [microgravity physiology](./space-medicine.microgravity-physiology.md) — the catalogue of adaptations the body undergoes in weightlessness, and [decompression illness](./space-medicine.decompression-illness.md) — the bubble physics and treatment protocols for pressure transitions.

## Overview

The fundamental design reference for space medicine is the human body in microgravity. Every physiological system adapts, and most of those adaptations are maladaptive on return to 1g. The strategy is not to prevent adaptation — that is impossible — but to slow it, monitor it, and ensure that the crew member who lands after six months can still stand up, see clearly, and resist infection.

### Microgravity Adaptation Timeline

| Time Since Launch | Physiological Change | Countermeasure Response |
|-------------------|---------------------|------------------------|
| Hours | Cephalad fluid shift, facial edema | Monitor ICP, headache management |
| 1-3 days | Space motion sickness (SMS) | Promethazine 25-50 mg IM, scopolamine |
| 3-7 days | Fluid diuresis, plasma volume -10-15% | Hydration monitoring, orthostatic checks |
| 1-2 weeks | Calf muscle atrophy begins | ARED, T2, CEVIS exercise start |
| 2-4 weeks | Bone resorption markers elevated | Bisphosphonate loading (alendronate 70 mg/wk) |
| 1-3 months | Bone mineral density -1-2%/month | Resistive exercise at 270 kg peak load |
| 3-6 months | SANS optic disc edema in ~70% | OCT imaging, fundus photography |
| 6+ months | Cardiac atrophy, orthostatic intolerance | Leg cuff counterpressure, reconditioning plan |

## Crew Selection Standards

Astronaut selection begins with eliminating candidates who cannot tolerate the physiological stress of spaceflight. The governing standard is NASA-STD-3001 Volume 2 (Human Integration Design Handbook), supplemented by the Flight Crew Standard (NASA-STD-3001 Vol 1) and JAXA/ESA equivalents.

### NASA-STD-3001 Medical Requirements

| Requirement Category | Standard | Rationale |
|---------------------|----------|-----------|
| Distant visual acuity | 20/20 each eye, correctable | Cabin instrument and EVA visual tasks |
| Near visual acuity | Jaeger 2 each eye, correctable | Procedure book and screen reading |
| Hearing threshold | <= 25 dB HL at 500-4000 Hz | Comm clarity in noisy cabin |
| Anthropometric standing height | 157-190 cm (long-duration) | Soyuz/Falcon/CST-100 seat envelope |
| Anthropometric sitting height | 80-99 cm | Helmet clearance in launch suit |
| Blood pressure | Systolic <= 140, diastolic <= 90 | Cardiovascular reserve for 3-4g entry |
| Corrected refractive error | <= +/- 5.5 diopters sphere | SANS risk amplification beyond range |
| Radiation career exposure | <= 3 Sv career (35-year-old female) | Per NASA CARA dose limits |

### Anthropometric Envelope

| Dimension | Minimum (cm) | Maximum (cm) | Constraint Source |
|-----------|-------------|-------------|-------------------|
| Standing height | 157 | 190 | Soyuz descent module |
| Sitting height | 80 | 99 | Launch/entry suit helmet |
| Arm reach (functional) | 75 | 95 | SSRMS and EVA reach envelope |
| Body weight | 50 kg | 95 kg | Seat load limit / suit sizing |
| Interocular distance | 5.5 | 7.5 | Helmet visor optical centre |

### Disqualifying Conditions

- Active seizure disorder (within 5 years)
- Insulin-dependent diabetes mellitus
- Uncontrolled hypertension (> 140/90 despite medication)
- Coronary artery disease with revascularisation
- Malignancy within 5 years (except localised skin SCC/BCC)
- Bilateral renal calculi history
- Psychiatric hospitalisation within lifetime
- Corrective cardiac surgery (valvular, congenital repair)
- Chronic vestibular disorder (Meniere, BPPV recurrent)

## Microgravity Physiology

The body in microgravity is a system out of equilibrium. Without the 1g load that shaped its evolution, every tissue type begins to remodel.

### Bone Loss

Bone mineral density (BMD) loss in microgravity averages 1-2% per month at load-bearing sites — the lumbar spine, femoral neck, tibia, and calcaneus. This is roughly 10x the rate of postmenopausal osteoporosis. The mechanism is uncoupled remodelling: osteoclast-mediated resorption continues at preflight rates while osteoblast-mediated formation drops by 30-50%.

| Skeletal Site | Monthly BCD Loss | Countermeasure Efficacy |
|---------------|-----------------|------------------------|
| Lumbar spine | 1.0-1.5% | ARED reduces to 0.3-0.5% |
| Femoral neck | 1.5-2.0% | ARED + bisphosphonate reduces to < 0.5% |
| Tibia (cortical) | 0.7-1.0% | Partially mitigated by jump loads |
| Calcaneus (trabecular) | 2.0-2.5% | Most resistant to countermeasures |
| Radius (non-load-bearing) | 0.0-0.3% | Minimal change |

### Fluid Shifts and SANS

On reaching orbit, approximately 1.5-2.0 litres of fluid shift from the lower extremities to the thorax and head. Leg circumference decreases by 10-30% within 24 hours. The cephalad shift raises intracranial pressure (ICP) chronically and is the leading hypothesis for Spaceflight-Associated Neuro-ocular Syndrome (SANS).

| SANS Finding | Prevalence (ISS crew) | Severity |
|-------------|----------------------|----------|
| Optic disc edema (Frison grade >= 1) | ~ 70% | Mild to moderate |
| Globe flattening (posterior) | ~ 65% | Detectable on OCT |
| Choroidal folds | ~ 35% | Often asymptomatic |
| Cotton wool spots | ~ 15% | Nerve fibre layer infarcts |
| Hyperopic shift (> 0.5 D) | ~ 50% | Correctable with lenses |

### Muscle Atrophy

Without mechanical loading, skeletal muscle atrophies at 0.5-1.0% per day in the first week, stabilising at roughly 20% mass loss over 6 months for type I (slow-twitch) fibres. The calf (triceps surae) is most affected because it is normally the primary anti-gravity muscle.

| Muscle Group | Mass Loss (6-month ISS) | Function Impact |
|-------------|------------------------|-----------------|
| Soleus/gastrocnemius | 20-30% | EVA foot restraint, 1g walking |
| Quadriceps | 12-18% | Post-landing egress |
| Vastus lateralis Type I fibres | 15-25% | Endurance capacity |
| Erector spinae | 10-15% | Posture maintenance |
| Intrinsic back muscles | 8-12% | Lifting tasks |

### Cardiovascular Deconditioning

Plasma volume drops 10-15% within the first two weeks. Red blood cell mass decreases by 5-10% (space anaemia). Left ventricular mass decreases by ~10% over 6 months. The baroreflex sensitivity drops, resulting in orthostatic intolerance: ~30% of long-duration crew cannot stand for 10 minutes on landing day without presyncope.

## Countermeasures

Countermeasures are the daily regimen that slows adaptation. The ISS programme allocates 2.5 hours per crew member per day for exercise: 1.5 hours of structured exercise plus 1 hour of setup, checkout, and stowage.

### ARED (Advanced Resistive Exercise Device)

The ARED uses vacuum cylinders to provide resistive loads up to 270 kg (600 lbf) across squat, heel raise, bench press, deadlift, and rowing motions. It simulates free weights through two flywheel-and-cable mechanisms.

| ARED Exercise | Load Range | Reps/Sets | Target |
|---------------|-----------|-----------|--------|
| Squat | 145-270 kg | 8-12 x 3 | Femur, gluteals, erector spinae |
| Heel raises | 90-180 kg | 10-15 x 3 | Calf (soleus/gastrocnemius) |
| Bench press | 70-135 kg | 8-12 x 3 | Pectorals, triceps |
| Deadlift | 135-225 kg | 6-10 x 3 | Posterior chain, grip |
| Seated row | 55-110 kg | 10-12 x 3 | Latissimus, rhomboids |

### T2 Treadmill

The T2 (Treadmill 2) uses a subject load system (barness and bungee springs) to pull the runner onto the belt at 55-80% body weight equivalent. Speeds range from 4.8 to 20 km/h.

| Parameter | Value |
|-----------|-------|
| Subject load | 55-80% body weight equivalent |
| Speed range | 4.8-20 km/h |
| Daily session | 30-50 minutes |
| Target heart rate | 75-90% age-predicted max |
| Incline | 0% (simulated via bungee tuning) |

### CEVIS (Cycle Ergometer with Vibration Isolation)

CEVIS is a vibration-isolated stationary cycle with load control from 25 to 350 W. It is the primary cardiovascular conditioning device.

| Parameter | Value |
|-----------|-------|
| Work rate range | 25-350 W |
| Daily session | 30-45 minutes |
| Cadence | 60-95 rpm |
| Vibration isolation | < 1 Hz natural frequency |

### Pharmaceutical Countermeasures

| Drug | Dose | Purpose |
|------|------|---------|
| Alendronate (bisphosphonate) | 70 mg/week oral | Inhibit osteoclast bone resorption |
| Potassium citrate | 20 mEq/day oral | Buffer metabolic acidosis, reduce bone resorption |
| Promethazine | 25-50 mg IM/PRN | Space motion sickness |
| Scopolamine + dextroamphetamine | 0.4 mg + 5 mg PRN | SMS alternative |
| Melatonin | 3-5 mg PO | Circadian rhythm entrainment |

## Decompression Illness

Decompression sickness (DCS) occurs when dissolved inert gas (nitrogen) comes out of solution as bubbles in tissues or blood during a pressure reduction. In spaceflight, the primary DCS risk is during EVA prebreath and cabin depressurisation contingencies.

### Prebreath Protocols

The ISS uses a multi-step prebreath protocol before each EVA. The goal is to reduce tissue nitrogen to a level where the 4.3 psi (29.6 kPa) suit pressure will not produce symptomatic bubbles.

| Protocol Step | Pressure | Gas | Duration | Activity |
|---------------|----------|-----|----------|----------|
| 1. Cabin at 14.7 psi | 14.7 psi (101.3 kPa) | Air | -- | Normal ops |
| 2. Cabin depress | 10.2 psi (70.3 kPa) | Air (26.5% O2) | 24+ hours | Pre-EVA adaptation |
| 3. Mask prebreath | 14.7 psi | 100% O2 | 50 min | Resting |
| 4. Exercise prebreath | 14.7 psi | 100% O2 | 50 min | Cycle ergometer at 75% VO2max |
| 5. Suit don + prebreath | 14.7 psi | 100% O2 | 30 min | Donning EMU |
| 6. Depress to suit pressure | 4.3 psi (29.6 kPa) | 100% O2 | 30 min | In-suit prebreath (ISLE) |

### DCS Classification

| Type | Presentation | Mechanism | Treatment |
|------|-------------|-----------|-----------|
| Type I (mild) | Joint pain ("bends"), skin rash, lymphatic swelling | Tissue bubbles in periarticular tissue | 100% O2 + fluids + hyperbaric O2 |
| Type II (serious) | Neurologic, cardiopulmonary, vestibular | Arterial gas emboli or spinal cord bubbles | Hyperbaric recompression (USN Table 6) |
| Arterial gas embolism | Stroke-like symptoms | Pulmonary barotrauma → arterial bubbles | USN Table 6A (30 msw) |

### Hyperbaric Treatment Tables

| Table | Depth | Duration | Gas Profile | Indication |
|-------|-------|----------|-------------|------------|
| USN Table 6 | 18 msw (2.8 ATA) | 285 min total | 100% O2 with air breaks | Type II DCS, AGE |
| USN Table 6A | 30 msw (4.0 ATA) | 35 min + Table 6 | 100% O2 excursions | Severe AGE, treatment failure |
| USN Table 9 | 14 msw (2.4 ATA) | 35 min | 100% O2 | Type I DCS, asymptomatic |

## Radiation Context

Space medicine intersects with [radiation protection](./radiation-protection.md) through dose limits and health monitoring. NASA sets career exposure limits to keep the Risk of Exposure-Induced Death (REID) below 3% at the 95% confidence level.

| Exposure Category | 1-Year Limit (mSv) | Career Limit (mSv) |
|-------------------|--------------------|--------------------|
| 25-year-old female | 500 | 1,000 |
| 35-year-old female | 500 | 1,750 |
| 45-year-old female | 500 | 2,500 |
| 25-year-old male | 500 | 1,500 |
| 35-year-old male | 500 | 2,500 |
| 45-year-old male | 500 | 3,250 |
| LEO actual (6-month) | 50-100 | -- |
| Mars transit actual | 300-500 (one-way) | -- |

## ISS Medical Kit

The ISS Medical Kit is organised into packs by system and urgency:

| Pack | Contents | Indication |
|------|----------|------------|
| Advanced Life Support Pack | Defibrillator, IV supplies, airway adjuncts | Cardiac arrest, trauma |
| Ambulatory Medical Pack | Oral meds, topical agents, otoscope | Routine primary care |
| Crew Contingency Pack | Surgical instruments, chest tube | Emergency surgery |
| Radiation Pack | Potassium iodide, Prussian blue | Radionuclide contamination |
| Dental Pack | Extraction forceps, temporary fillings | Dental emergency |

## Key Parameters Summary

| Parameter | Value | Source |
|-----------|-------|--------|
| Daily exercise allocation | 2.5 hr/crew/day | ISS programme standard |
| ARED maximum load | 270 kg (600 lbf) | NASA ARED spec |
| Bone loss rate (unmitigated) | 1-2%/month | Quantitative CT data |
| Bone loss rate (with ARED) | 0.3-0.5%/month | ISS cohort 2009-2020 |
| SANS prevalence | ~ 70% optic disc edema | NASA OCULAR cohort |
| Plasma volume loss | 10-15% | Pre/post hemodilution studies |
| Orthostatic intolerance rate | ~ 30% on landing day | Stand test data |
| EVA suit pressure | 4.3 psi (29.6 kPa) | EMU spec |
| Prebreath duration (total) | ~ 240 min | Campout + ISLE protocol |
| DCS incidence (ISS EVAs) | < 0.5% symptomatic | NASA EVA medical records |
| Career radiation limit (30-y male) | 2,500 mSv | NASA CARA |
| LEO dose per 6-month increment | 50-100 mSv | ISS dosimetry data |

## Prerequisites

- [Health](../health/index.md) — terrestrial medicine, pharmacology, and diagnostic heritage
- [Radiation Safety](../ehs/index.md) — dose limits and dosimetry protocols

## See Also

- [ECLSS](./eclss.md) — atmosphere, water, and waste management for crew survival
- [Space Suits](./space-suits.md) — PLSS and pressure garment for EVA
- [Radiation Protection](./radiation-protection.md) — shielding and dosimetry for crewed missions
- [Crew Training](./crew-training.md) — simulator and analog training infrastructure
