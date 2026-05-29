# Diagnostics

> **Node ID**: health.diagnostics
> **Domain**: [Health](./index.md)
> **Dependencies**: [`health.medicine`](medicine.md), [`health.medical-instruments`](medical-instruments.md), [`chemistry`](../chemistry/index.md)
> **Enables**: [`health.surgery-basics`](surgery-basics.md), [`health.pharmacology`](pharmacology.md)
> **Timeline**: Years 10-100+
> **Outputs**: diagnostic_capability, vital_signs_monitoring, laboratory_testing, imaging_capability
> **Critical**: No — enhances treatment outcomes but medicine can function at a basic level without formal diagnostics


Diagnostics covers physical examination, vital signs measurement, basic laboratory testing, and fundamental imaging. In a bootstrap medical system, diagnosis relies primarily on clinical observation and hands-on examination — the same approach that served medicine from Hippocrates through the 19th century. The stethoscope, thermometer, pulse oximeter (if electronics available), and basic blood/urine tests provide the majority of diagnostic information needed to guide treatment decisions.

The diagnostic chain progresses from simple observation (vital signs, inspection, palpation) through instrumented examination (stethoscope, reflex hammer, otoscope) to laboratory analysis (blood smear, urine dipstick, cultures). Each level adds precision but requires progressively more infrastructure. A competent diagnostician with a stethoscope, thermometer, and basic lab supplies can correctly identify 70-80% of common conditions.


## Materials

- Glass thermometers (mercury or alcohol): 0-50°C range, 0.1°C graduations
- Stethoscope: see [medical-instruments](medical-instruments.md) for fabrication
- Sphygmomanometer (blood pressure cuff): requires rubber bladder, cloth cuff, manometer
- Reagents for basic laboratory tests: Benedict's solution (urine glucose), nitric acid (protein precipitation), Wright's or Giemsa stain (blood smears)
- Glass slides and cover slips for microscopy
- Litmus paper or pH indicator strips
- Clean collection containers (glass jars, urine cups)

## Tools and Equipment

- Microscope (see [medical-instruments](medical-instruments.md)): 100× to 1000× magnification
- Centrifuge (hand-cranked or electric): 1000-3000 RPM for separating blood components
- Scale: 0.1 g sensitivity for reagent preparation
- Timer or clock with second hand: for pulse and respiration counting
- Heat source: for preparing stains and reagents

## Knowledge

- Anatomy and physiology: organ systems, normal function, common pathology
- Vital sign ranges: know normal values by age group
- Physical examination technique: inspection, palpation, percussion, auscultation
- Basic microbiology: Gram stain interpretation, common pathogen morphology

## Bill of Materials

| Material | Quantity per Patient Exam | Source | Alternatives |
|----------|--------------------------|--------|-------------|
| Thermometer | 1 (reusable) | [Glass production](../glass/index.md) + mercury or alcohol | Hand on forehead (crude: detects >1°C deviation) |
| Stethoscope | 1 (reusable) | [Medical Instruments](medical-instruments.md) | Ear directly on chest (unhygienic, limited) |
| Blood pressure cuff | 1 (reusable) | [Rubber](../polymers/rubber.md) + [textiles](../textiles/index.md) | Palpation of pulse pressure (systolic only, rough estimate) |
| Glass slides | 2-5 | [Glass](../glass/index.md) | None for blood smear examination |
| Wright's stain | 10 mL (many uses) | [Chemistry](../chemistry/index.md) — methylene blue + eosin | Simple methylene blue (less differential detail) |
| Urine collection jar | 1 | [Glass](../glass/index.md) or [ceramics](../ceramics/index.md) | Any clean container |
| Lancets (blood collection) | 1-3 | [Medical Instruments](medical-instruments.md) | Sterilized needle |


## Vital Signs Assessment

1. **Measure temperature**: Place thermometer under the tongue (oral) for 3-5 minutes with mouth closed. Axillary (armpit) reading: add 0.5°C to approximate core temperature. Rectal: most accurate core temperature, add 0.3°C for oral equivalent. Normal: 36.5-37.5°C (oral). Fever: >38.0°C. Hypothermia: <35.0°C.
2. **Count pulse (heart rate)**: Place two fingers (index and middle) on the radial artery at the wrist. Count beats for 30 seconds and multiply by 2 (or count for 60 seconds for irregular rhythms). Note rhythm (regular vs. irregular) and quality (strong, weak, thready).
3. **Measure respiratory rate**: Count breaths for 60 seconds by observing chest rise. Do this before the patient is aware you are counting — conscious control alters rate. One breath = one inspiratory-expiratory cycle.
4. **Measure blood pressure**: Wrap cuff around upper arm at heart level. Inflate to 30 mmHg above palpated systolic pressure. Place stethoscope over brachial artery (antecubital fossa). Deflate at 2-3 mmHg per second. First sound = systolic pressure. Sound disappears = diastolic pressure. Record as systolic/diastolic (e.g., 120/80 mmHg).
5. **Assess pulse oximetry (if available)**: Clip sensor to fingertip. Normal SpO₂: 95-100%. Below 90% = significant hypoxemia requiring supplemental oxygen. Below 85% = severe hypoxemia, risk of cardiac arrest.

**Verification**: Compare measured values to the normal ranges table below. Any value outside the normal range for the patient's age group warrants repeat measurement to exclude technique error. Document all five vital signs (temperature, pulse, respiratory rate, blood pressure, SpO₂) with the time of measurement.

**Expected accuracy**: Thermometer ±0.1°C (mercury) or ±0.5°C (alcohol). Blood pressure ±3 mmHg (aneroid gauge, calibrated). Pulse count ±2 bpm (60-second count). Respiratory rate ±1 breath/min (60-second count). SpO₂ ±2% (pulse oximeter).

**Strengths**:
- Provides objective, repeatable measurements that track disease progression over time
- Requires minimal equipment (thermometer, stethoscope, BP cuff) that is reusable for years with no consumables
- All measurements can be performed in under 5 minutes per patient

**Weaknesses**:
- Blood pressure reading varies with cuff size, arm position, and operator technique — single readings may be misleading
- Rectal and axillary temperatures require correction factors that introduce uncertainty
- Pulse oximetry requires electronics and may not be available at earliest bootstrap stages

## Basic Physical Examination

1. **General inspection**: Observe the patient before touching. Note: level of consciousness (alert, confused, unresponsive), posture, skin color (pale, flushed, cyanotic, jaundiced), distress level (comfortable, mild, moderate, severe), nutritional state.
2. **Head and neck**: Examine pupils (equal, round, reactive to light). Inspect conjunctiva for pallor (anemia) or jaundice (liver disease). Examine throat for redness, exudate, or swelling. Palpate neck lymph nodes (enlarged = infection or malignancy).
3. **Chest examination**: Inspect for symmetrical expansion. Palpate for tenderness or masses. Percuss: resonant (normal lung), dull (consolidation, fluid), hyperresonant (pneumothorax). Auscultate with stethoscope: vesicular breath sounds (normal), crackles/rales (fluid, pneumonia), wheezes (asthma, bronchitis), absent sounds (pneumothorax, pleural effusion).
4. **Cardiovascular**: Auscultate heart at four valve positions. Normal: two heart sounds (S1 "lub," S2 "dub"). Murmurs = turbulent flow through valves (pathology grading I-VI by intensity). Assess jugular venous distension (elevated >3 cm = right heart failure or fluid overload).
5. **Abdominal examination**: Inspect for distension, scars. Auscultate bowel sounds (present = normal; absent >2 min = ileus or peritonitis). Percuss for shifting dullness (ascites). Palpate all quadrants — tenderness, guarding, rigidity, masses. Rebound tenderness = peritoneal irritation (appendicitis, peritonitis).

**Verification**: A complete physical examination should take 10-15 minutes and cover all four examination techniques (inspection, palpation, percussion, auscultation) for each body region. Findings should be documented immediately — memory degrades within minutes for subtle details.

**Expected accuracy**: Physical examination has variable sensitivity and specificity by finding. Rebound tenderness for appendicitis: sensitivity 50-70%, specificity 60-80%. Reduced breath sounds for pneumothorax: sensitivity 70-85%, specificity 80-90%. Clinical examination combined with vital signs identifies the correct diagnosis in 70-80% of common conditions.

**Strengths**:
- Requires no equipment beyond a stethoscope — can be performed anywhere
- Provides immediate diagnostic information without waiting for laboratory results
- Combines multiple examination techniques to cross-validate findings

**Weaknesses**:
- Highly operator-dependent — diagnostic accuracy varies with examiner experience and thoroughness
- Many findings have low specificity (e.g., abdominal tenderness occurs in appendicitis, cystitis, mesenteric adenitis, and constipation)
- Obese patients, uncooperative patients, and those with altered consciousness limit examination reliability

## Basic Laboratory Tests

1. **Urine dipstick (if reagent strips available)**: Dip strip in fresh urine, read at specified times. Test for: glucose (diabetes), protein (kidney disease), blood (stones, infection, tumor), leukocytes (UTI), nitrites (bacterial infection), pH, specific gravity.
2. **Urine examination without reagents**: Visual inspection — color (pale yellow = normal; dark = dehydration; red = blood; brown = old blood or bilirubin). Odor (foul = infection; sweet/fruity = ketones/diabetes). Cloudiness (bacteria, crystals, or blood cells).
3. **Blood smear preparation**: Prick fingertip with sterile lancet. Place a small drop of blood on one end of a glass slide. Using a second slide as a spreader at 30-45° angle, spread the blood into a thin film. Air dry. Fix with methanol for 2 minutes. Stain with Wright's stain (1-3 minutes), rinse with buffered water, air dry. Examine under oil immersion (1000×).
4. **Blood smear interpretation**: Red blood cells: normal size and color (normocytic, normochromic), small/pale (iron deficiency), large (B12/folate deficiency). White blood cells: neutrophils (bacterial infection — elevated), lymphocytes (viral infection — elevated), eosinophils (parasites, allergy — elevated). Platelets: estimate quantity (low = bleeding risk, high = thrombosis risk).
5. **Hemoglobin estimation**: Sahli method — add blood to HCl, dilute with water until color matches standard. Reading in g/dL. Normal: male 13-17 g/dL, female 12-15 g/dL. Anemia: <12 g/dL (female), <13 g/dL (male).

**Verification**: Run a control blood smear from a known healthy donor alongside patient samples to confirm stain quality and microscope function. Compare Sahli hemoglobin readings on duplicate samples — results should agree within ±1 g/dL. For urine dipsticks, test with a known glucose solution (positive control) and distilled water (negative control) when opening a new bottle of strips.

**Expected accuracy**: Blood smear differential count: ±5% for major cell types when counted by an experienced technician. Hemoglobin (Sahli method): ±1 g/dL compared to reference methods. Urine dipstick: semi-quantitative, detects glucose ≥0.25%, protein ≥30 mg/dL, blood ≥10 RBC/μL. Microscope resolution at 1000× (oil immersion): resolves structures down to 0.2 μm.

**Materials specifications**: Wright's stain: methylene blue-eosin mixture in methanol, pH 6.4-6.8. Glass slides: 75 × 25 mm, 1 mm thickness, cleaned with ethanol before use. Lancets: sterile, 2-3 mm blade depth for capillary blood collection. Sahli hemoglobin tube: graduated 4-20 g/dL, ±0.5 g/dL accuracy.

**Strengths**:
- Provides objective laboratory data that confirms or refutes clinical impressions
- Blood smear differentiates bacterial from viral infection, guiding treatment decisions
- Hemoglobin estimation identifies anemia requiring treatment, with equipment that lasts years

**Weaknesses**:
- Requires microscope, centrifuge, stains, and trained technician — significant infrastructure investment
- Wright's stain has a shelf life of 6-12 months once opened; fresh stain produces better results
- Sahli hemoglobin method is less accurate than cyanmethemoglobin method (±1 g/dL vs ±0.3 g/dL)


## Vital Signs — Normal Ranges by Age

| Parameter | Adult | Child (6-12 yr) | Child (1-5 yr) | Infant (0-1 yr) | Critical Values (Adult) |
|-----------|-------|-----------------|----------------|-----------------|----------------------|
| Heart rate (bpm) | 60-100 | 70-120 | 80-130 | 100-160 | <40 or >150 |
| Respiratory rate (breaths/min) | 12-20 | 18-30 | 20-30 | 30-60 | <8 or >35 |
| Systolic BP (mmHg) | 90-140 | 80-120 | 70-110 | 60-90 | <80 or >200 |
| Diastolic BP (mmHg) | 60-90 | 50-80 | 40-70 | 30-60 | <40 or >120 |
| Temperature (°C, oral) | 36.5-37.5 | 36.5-37.5 | 36.5-37.5 | 36.5-37.7 | <35.0 or >40.5 |
| SpO₂ (%) | 95-100 | 95-100 | 95-100 | 95-100 | <90% |

## Common Laboratory Reference Values

| Test | Normal Range | Unit | Low Indicates | High Indicates |
|------|-------------|------|--------------|---------------|
| Hemoglobin (male) | 13-17 | g/dL | Anemia, hemorrhage | Polycythemia, dehydration |
| Hemoglobin (female) | 12-15 | g/dL | Anemia, hemorrhage | Polycythemia, dehydration |
| White blood cell count | 4,500-11,000 | /μL | Viral infection, bone marrow suppression | Bacterial infection, leukemia |
| Neutrophils | 54-75 | % of WBC | — | Bacterial infection |
| Lymphocytes | 20-40 | % of WBC | — | Viral infection |
| Platelet count | 150,000-400,000 | /μL | Bleeding risk, DIC | Thrombosis risk |
| Urine specific gravity | 1.005-1.030 | — | Overhydration | Dehydration |
| Urine pH | 4.5-8.0 | — | Acidosis | UTI, alkalosis |

## Diagnostic Sensitivity and Specificity (Common Tests)

| Test | Condition | Sensitivity | Specificity | Notes |
|------|-----------|-------------|-------------|-------|
| Fever (>38°C) | Bacterial infection | 60-80% | 50-70% | Many non-bacterial causes of fever |
| Elevated WBC (>11,000) | Bacterial infection | 65-80% | 55-75% | Stress, steroids, and other causes elevate WBC |
| Urine nitrites | Urinary tract infection | 20-50% | 95-99% | High specificity: if positive, UTI is likely |
| Urine leukocytes | Urinary tract infection | 70-90% | 50-70% | Better for ruling out UTI when negative |
| Rebound tenderness | Appendicitis | 50-70% | 60-80% | Part of clinical assessment, not diagnostic alone |
| Reduced breath sounds | Pneumothorax | 70-85% | 80-90% | Confirm with chest exam; percussion hyperresonant |

## Scaling Notes

- **Basic clinical exam only**: No equipment beyond hands, eyes, and ears. Can perform inspection, palpation, percussion, and basic auscultation (ear to chest). Accurate for obvious conditions (fractures, large wounds, severe respiratory distress). Misses subtle conditions.
- **Vital signs + stethoscope**: Adds quantitative measurement. Thermometer, BP cuff, stethoscope. Provides objective tracking over time. Required for safe anesthesia monitoring. Cost: low (instruments are reusable for years).
- **Basic laboratory**: Adds blood smear, urine exam, hemoglobin. Requires microscope, stains, glass slides, centrifuge. Provides objective data on anemia, infection, kidney function, diabetes. Throughput: 10-20 tests per day with one technician.
- **Advanced laboratory**: Full chemistry panel, microbiology cultures, electrolytes. Requires spectrophotometer, incubator, extensive reagent supply. Requires industrial chemistry capability for reagent production. Throughput: 50-100 tests per day.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| BP reading unobtainable | Cuff too small/large, improper placement, severe hypotension | Use correct cuff size (bladder covers 80% of arm circumference); try forearm or palpate systolic only |
| Thermometer reading inconsistent | Incomplete equilibration time, oral intake of hot/cold fluids | Wait 15 min after eating/drinking; use axillary route with 5-min equilibration |
| Blood smear too thick | Drop too large, spreader angle too steep | Use a smaller drop (3-4 mm diameter); spread at 30° angle |
| Urine test results unreliable | Sample contamination, improper storage (>2 hours old) | Collect midstream clean-catch; test within 1 hour or refrigerate |
| Heart sounds difficult to hear | Room too noisy, stethoscope earpieces reversed, patient obese | Quiet environment; verify stethoscope orientation; use bell for low-frequency sounds |
| Microscope image blurry | Dirty lens, incorrect focus, coverslip missing | Clean objective lens with lens paper; focus with coarse then fine adjustment; ensure coverslip is in place |

## Safety

- **Infection control during examination**: Wash hands before and after every patient contact. Wear gloves when examining wounds, mucous membranes, or when blood contact is possible. Sterilize thermometers between patients (alcohol wipe minimum, autoclave preferred for rectal thermometers).
- **Blood-borne pathogen risk**: Every blood sample carries risk of hepatitis, HIV, or other blood-borne pathogens. Use universal precautions: treat all blood as infectious. Lancets and needles are single-use — dispose in puncture-proof containers. Never recap needles.
- **Mercury thermometer hazards**: Mercury is a neurotoxin. If a thermometer breaks, collect mercury with a card or dropper into a sealed container. Do not vacuum (vaporizes mercury). Dispose as hazardous waste. Alcohol thermometers are safer but less accurate.
- **Radiation safety** (if X-ray available): See [radiation-safety](../ehs/radiation-safety.md). Minimum distance 2 m from X-ray tube during exposure. Wear lead apron if available. No pregnant women in X-ray room. Maximum exposure: follow ALARA principle (As Low As Reasonably Achievable).

## Quality Control

- **Thermometer calibration**: Verify against known standards (ice water = 0°C, boiling water = 100°C) monthly. Discard thermometers that deviate >0.5°C from standard.
- **Blood pressure cuff calibration**: Verify manometer reading against a mercury column standard (if available) or a reference cuff. Cuff should read within ±3 mmHg of standard.
- **Microscope maintenance**: Clean objectives daily with lens paper. Cover microscope when not in use. Check condenser alignment weekly. Oil immersion objective: clean after every use with lens paper moistened with xylene or alcohol.
- **Reagent quality**: Test reagents with known positive and negative controls. Benedict's solution should be clear blue (negative); turns green-yellow-orange-red with increasing glucose. Discard discolored reagents.
- **Laboratory accuracy checks**: Run duplicate samples on 10% of specimens. Results should agree within ±5% for quantitative tests. If not, recalibrate equipment and retest.


## Diagnostic Methods by Technology Level

| Level | Methods Available | Conditions Diagnosable | Accuracy |
|-------|-------------------|----------------------|----------|
| Stone-age (no instruments) | Inspection, palpation, pulse by touch, urine appearance | Obvious fractures, large wounds, severe dehydration, pregnancy | 30-40% |
| Bronze-age (thermometer, stethoscope) | All above + temperature, heart/lung auscultation, basic percussion | Pneumonia, heart murmurs, fever, bowel obstruction | 50-60% |
| Industrial (lab tests, BP cuff) | All above + blood smear, urine analysis, hemoglobin, blood pressure | Anemia, infection type, kidney disease, diabetes, hypertension | 70-80% |
| Electronic (X-ray, ECG) | All above + plain radiography, electrocardiography | Fractures (radiographic), pneumonia extent, heart rhythm, cardiac ischemia | 85-90% |

## Imaging Fundamentals

- **X-ray (plain radiography)**: Requires vacuum tube, high-voltage power supply, photographic film or phosphor screen. Ionizing radiation — see [radiation-safety](../ehs/radiation-safety.md). Useful for: fractures, pneumonia, pleural effusion, bowel obstruction (air-fluid levels), foreign bodies. Typical dose: chest X-ray = 0.1 mSv (10 days of natural background radiation).
- **Ultrasound**: Requires piezoelectric crystals and electronics. Non-ionizing — safe for pregnancy. Useful for: abdominal masses, cardiac function (echocardiography), pregnancy (fetal monitoring), vascular assessment, guiding needle aspiration. Resolution: 1-2 mm for superficial structures, decreasing with depth.
- **ECG (electrocardiography)**: Records electrical activity of the heart. Requires electrodes, amplifier, and recording device. 12-lead ECG: standard diagnostic. Single-lead (portable): screening. Detects: arrhythmias, myocardial infarction, conduction blocks, electrolyte abnormalities (peaked T waves in hyperkalemia). Paper speed: 25 mm/s. Calibration: 10 mm/mV.

## Neurological Assessment

1. **Level of consciousness**: Use AVPU scale — Alert (awake, talking), responds to Voice, responds to Pain, Unresponsive. Document baseline at admission and reassess with any change. More detailed: Glasgow Coma Scale (GCS) — Eye opening (1-4), Verbal response (1-5), Motor response (1-6). GCS 15 = normal. GCS ≤8 = intubation required (cannot protect airway).
2. **Pupil examination**: Shine light into each eye separately. Normal: equal, round, reactive to light (3-5 mm, constrict to 1-2 mm). Unequal pupils (anisocoria >1 mm): consider intracranial pressure elevation, brain herniation, or direct orbital trauma. Fixed and dilated: ominous — cranial nerve III compression.
3. **Motor examination**: Test grip strength in both hands simultaneously (have patient squeeze your fingers). Compare side to side. Asymmetric weakness suggests stroke or spinal cord lesion. Test plantar flexion/dorsiflexion of feet. Babinski sign (toes extend upward when sole stroked): abnormal in adults — upper motor neuron lesion.
4. **Sensory examination**: Test light touch (cotton wisp), pinprick (sterile needle), and vibration (tuning fork 128 Hz) in all four extremities. Map any area of sensory loss to dermatome level to localize spinal cord or nerve root lesion.

## Emergency Triage Assessment

Rapid assessment framework for sorting patients by severity when resources are limited:

| Category | Criteria | Color Code | Action |
|----------|----------|------------|--------|
| Immediate | Airway compromise, uncontrolled hemorrhage, tension pneumothorax, GCS <9 | Red | Treat immediately — life-threatening |
| Urgent | Open fractures, major burns (>20% BSA), severe abdominal pain, GCS 9-13 | Yellow | Treat within 1-2 hours |
| Delayed | Closed fractures, minor burns, stable lacerations, GCS 14-15 | Green | Treat within 4-6 hours |
| Expectant | Unsurvivable injuries (massive head trauma, >80% full-thickness burns) | Blue | Comfort measures only |
| Minor | Walking wounded, minor wounds, sprains | White | Self-care or minimal treatment |

## Fluid and Electrolyte Assessment

Dehydration severity guides fluid resuscitation:

| Severity | Signs | Weight Loss (adult) | Fluid Deficit | Treatment |
|----------|-------|--------------------|--------------|-----------|
| Mild | Thirst, dry mouth, decreased urine | 3-5% | 1-2 L | Oral rehydration (ORS: 3.5 g NaCl, 2.5 g NaHCO₃, 1.5 g KCl, 20 g glucose per liter) |
| Moderate | Tachycardia, decreased skin turgor, sunken eyes, oliguria | 5-10% | 2-4 L | IV fluids: NS or RL 20-30 mL/kg over first hour |
| Severe | Hypotension, altered consciousness, anuria, shock | >10% | >4 L | Aggressive IV: 40-60 mL/kg over first hour; monitor for fluid overload |

## See Also

- [Medicine & Surgery](medicine.md) — clinical decision-making based on diagnostic findings
- [Medical Instruments](medical-instruments.md) — stethoscope, thermometer, microscope fabrication
- [Pharmacology](pharmacology.md) — therapeutic agents guided by diagnostic results
- [Surgery Basics](surgery-basics.md) — pre-operative diagnostic assessment
- [Chemistry](../chemistry/index.md) — reagent production, laboratory supplies
- [Glass](../glass/index.md) — thermometer, microscope slide, laboratory glassware
- [Toxicology](../ehs/toxicology.md) — diagnostic testing for toxic exposures



[← Back to Health](index.md)
