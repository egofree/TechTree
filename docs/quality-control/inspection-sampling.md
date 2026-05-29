# Inspection & Sampling Plans

> **Node ID**: quality-control.inspection-sampling
> **Domain**: [Quality Control](./index.md)
> **Dependencies**: [`measurement.precision-metrology`](../measurement/precision-metrology.md), `quality-control`
> **Enables**: None (leaf capability)
> **Timeline**: Years 40-100+
> **Outputs**: sampling_plans, aql_tables, inspection_procedures, acceptance_criteria, switching_rules

## Problem

Every manufactured part cannot be inspected 100% in volume production — the cost and time would be prohibitive. A 300 mm wafer may contain 100,000+ die; inspecting every die on every wafer through 500+ process steps is impossible. Acceptance sampling provides a statistically rigorous method to evaluate batch quality by inspecting a small, representative sample, accepting conforming lots and rejecting nonconforming ones. The challenge is designing sampling plans that reliably detect bad lots while minimizing the cost of inspection.

In semiconductor manufacturing, incoming inspection validates raw materials (photoresist, etching gases, silicon wafers), in-process inspection monitors critical steps, and final test verifies functional die. Each stage requires a different sampling strategy with appropriate AQL (Acceptable Quality Level) targets.

## Acceptance Sampling Fundamentals

### Decision Framework: Choosing a Sampling Plan

| Scenario | Recommended Plan | Rationale |
|----------|-----------------|-----------|
| High-volume production, destructive testing | Variables sampling (known sigma) | 30-50% fewer samples than attribute plans for equivalent protection |
| Multiple defect types, pass/fail classification | Single attribute sampling (MIL-STD-105E) | Simple to administer, well-standardized |
| Expensive inspection, need to reduce average sample size | Double sampling | Accept/reject clearly good/bad lots quickly; second sample only for borderline lots |
| Supplier with proven quality history (>20 lots accepted) | Skip-lot sampling | Reduces inspection cost by 50-75% while maintaining statistical protection |
| Continuous flow production (no discrete lots) | Continuous sampling (CSP-1) | Starts at 100% inspection, transitions to sampling after clearance number |
| Critical safety items (AQL <0.1%) | Tightened inspection with 100% final test | Maximum consumer protection; accept on zero defects only |

### Implementation Steps

1. **Classify all incoming materials** by criticality: Assign AQL values based on failure consequence (0.10% for safety-critical, 0.65% for standard semiconductor materials)
2. **Establish sampling procedures**: Document lot size determination, sample size selection, and accept/reject criteria for each material category using MIL-STD-105E tables
3. **Train inspection personnel**: Qualify inspectors on measurement equipment ([Precision Metrology](../measurement/precision-metrology.md)), defect recognition, and switching rules
4. **Deploy switching rule logic**: Implement normal → tightened → reduced transitions in quality management system, tracking consecutive lot accept/reject history automatically
5. **Integrate with [SPC](statistical-process-control.md)**: Feed inspection results into control charts for trend detection before lots reach action limits
6. **Review quarterly**: Assess supplier quality trends, adjust AQL targets, and evaluate skip-lot eligibility

### Operating Characteristic (OC) Curve

Every sampling plan has an OC curve that plots the probability of accepting a lot against the actual defect rate. Two key points define the curve:

- **AQL (Acceptable Quality Level)**: The defect rate considered acceptable. Lots at AQL quality have high probability of acceptance (typically 95%). This is the producer's risk point — good lots are rejected only 5% of the time (α = 0.05).
- **LTPD (Lot Tolerance Percent Defective)**: The defect rate considered unacceptable. Lots at LTPD quality have low probability of acceptance (typically 10%). This is the consumer's risk point — bad lots are accepted only 10% of the time (β = 0.10).

The gap between AQL and LTPD defines the discrimination ability of the sampling plan. A narrow gap requires large sample sizes but provides sharper accept/reject decisions.

### Types of Sampling

**Single sampling**: Draw one sample of size n from the lot. If the number of defects d ≤ acceptance number c, accept the lot. If d > c, reject. Simplest plan, easiest to administer.

**Strengths**:
- Simplest plan to administer — one sample, one decision, no ambiguous intermediate states
- Easiest for inspector training — clear accept/reject criterion with no follow-up needed
- Predictable sample size — every lot requires exactly n units regardless of quality
- Minimum handling damage risk — units inspected only once
- Straightforward OC curve — easy to calculate and verify producer/consumer risk

**Weaknesses**:
- Largest average sample size for equivalent statistical protection — all lots get full sample
- No second chance for borderline lots — a lot with d = c+1 is rejected despite being nearly acceptable
- Highest total inspection cost in high-volume operations — every lot inspected at full sample size
- Sharp accept/reject boundary — small changes in defect count cause large changes in lot disposition
- Less discrimination between marginally good and marginally bad lots

**Double sampling**: Draw a first sample of n₁. If d₁ ≤ c₁, accept. If d₁ > r₁, reject. If c₁ < d₁ ≤ r₁, draw a second sample of n₂. Combine: if d₁ + d₂ ≤ c₂, accept; otherwise reject. Reduces average sample size for lots that are clearly good or clearly bad, at the cost of occasional second samples and more complex administration.

**Strengths**:
- Smaller average sample size than single sampling — clearly good or bad lots resolved on first sample
- Second chance for borderline lots — avoids rejecting marginally acceptable lots on a small sample
- Lower total inspection cost when most lots are clearly good or clearly bad (common in mature production)
- Better discrimination — the two-stage decision provides more statistical information per unit inspected

**Weaknesses**:
- Variable sample size — some lots require two samples, making labor planning unpredictable
- More complex administration — inspectors must track first sample results and calculate combined counts
- Longer decision time for borderline lots — second sample delays lot disposition
- Risk of "force to conclusion" bias — inspectors may unconsciously adjust second sample expectations
- Requires more training than single sampling — switching criteria must be understood and followed

**Multiple (sequential) sampling**: Extend the double sampling concept to 5-7 stages. Each stage has accept/reject/continue criteria. Minimum average sample number (ASN) for any given OC curve, but most complex to administer.

**Strengths**:
- Minimum average sample number (ASN) of any plan with equivalent OC curve
- Maximum discrimination — multiple decision points provide finest resolution between good and bad lots
- Earliest possible rejection of clearly bad lots — can stop after first few samples
- Best statistical efficiency per unit inspected — most information extracted from each sample

**Weaknesses**:
- Most complex to administer — 5-7 stages with different accept/reject criteria at each stage
- Variable and unpredictable sample size — lot disposition could require 1 sample or maximum samples
- Highest inspector training burden — must understand multi-stage switching rules
- Record-keeping intensive — cumulative defect counts must be tracked across all stages
- Rarely worth the administrative overhead unless inspection is very expensive or destructive

**Continuous sampling**: For flow production (no discrete lots). Start with 100% inspection. After i consecutive conforming units (clearance number, typically i = 15-50), switch to sampling at frequency f (typically f = 1/5 to 1/20). If a defective unit is found during sampling, resume 100% inspection and restart the count.

**Strengths**:
- Only method suitable for continuous flow production — no lot formation required
- Automatically adapts to quality level — 100% inspection during quality lapses, sampling during stability
- Minimal average inspection when process is stable — sampling frequency as low as 1/20
- Built-in feedback loop — defect discovery triggers immediate return to full inspection

**Weaknesses**:
- Not suitable for batch or lot-based production — requires continuous flow of individual units
- Complex switching logic — tracking consecutive conforming units requires careful counting
- Risk of producing defective units between sampling inspections — defects caught only at sample frequency
- Does not provide lot-level quality statistics — individual unit tracking complicates supplier quality records
- Clearance number (i = 15-50) creates delay before sampling begins after process restart

## MIL-STD-105E Sampling Tables

MIL-STD-105E (also known as ANSI/ASQ Z1.4, ISO 2859-1) is the standard attribute sampling system for inspection by attributes. It provides sampling plans indexed by lot size and AQL.

### Lot Size Determination

The lot is the collection of units offered for inspection at one time. Lot size determines the sample size code letter:

| Lot Size | Code Letter (Normal Inspection) |
|----------|-------------------------------|
| 2-8 | A |
| 9-15 | B |
| 16-25 | C |
| 26-50 | D |
| 51-90 | E |
| 91-150 | F |
| 151-280 | G |
| 281-500 | H |
| 501-1,200 | J |
| 1,201-3,200 | K |
| 3,201-10,000 | L |
| 10,001-35,000 | M |
| 35,001-150,000 | N |
| 150,001-500,000 | P |
| 500,001+ | Q |

### Sample Size Code Letter to Sample Size

| Code | Sample Size (Single Normal) |
|------|---------------------------|
| A | 2 |
| B | 3 |
| C | 5 |
| D | 8 |
| E | 13 |
| F | 20 |
| G | 32 |
| H | 50 |
| J | 80 |
| K | 125 |
| L | 200 |
| M | 315 |
| N | 500 |
| P | 800 |
| Q | 1,250 |

### AQL Selection by Application

| Application | Typical AQL | Rationale |
|-------------|------------|-----------|
| Critical safety items | 0.065% - 0.10% | Failure consequences severe |
| Semiconductor incoming materials (gases, chemicals) | 0.10% - 0.25% | Contamination destroys entire wafers |
| Semiconductor incoming wafers | 0.25% - 0.65% | Wafer defects propagate through all process steps |
| IC assembly (wire bond, package) | 0.40% - 1.0% | Moderate defect impact, rework possible |
| PCB assembly (SMT solder joints) | 0.65% - 1.5% | Many joints, moderate criticality |
| General mechanical parts | 1.0% - 2.5% | Standard industrial quality |
| Cosmetic defects | 2.5% - 4.0% | Functional quality unaffected |
| Non-critical packaging | 4.0% - 6.5% | Low impact |

### Worked Example: Incoming Wafer Inspection

A fab receives a lot of 500 silicon wafers. AQL = 0.25%, normal inspection, single sampling.

1. Lot size = 500 → Code letter H (from lot size table)
2. Code H → Sample size = 50 (from sample size table)
3. AQL = 0.25%, Code H → Ac = 0, Re = 1 (from MIL-STD-105E Table 2-A)

Interpretation: Inspect 50 wafers. If zero defective wafers are found, accept the lot. If one or more defective wafers are found, reject the lot. The probability of accepting a lot that is actually at 0.25% defective is 88%. The probability of accepting a lot at 1% defective is 61%.

### Switching Rules

MIL-STD-105E defines a dynamic system that adjusts inspection severity based on supplier quality history:

**Normal → Tightened**: If 2 out of 5 consecutive lots are rejected on normal inspection, switch to tightened. Tightened plans have smaller acceptance numbers (stricter criteria) for the same sample size.

**Tightened → Normal**: If 5 consecutive lots are accepted on tightened inspection, switch back to normal.

**Normal → Reduced**: If all of the following conditions are met, switch to reduced (smaller sample size, same acceptance number):
- 10 consecutive lots accepted on normal inspection
- Total defects in those 10 lots ≤ applicable limit number
- Production is steady (no changes in process, material, or supplier)
- Responsible authority agrees

**Reduced → Normal**: If any lot is rejected on reduced inspection, or if production becomes irregular, or if other conditions warrant, immediately switch back to normal.

This dynamic switching creates a feedback loop: consistently good suppliers earn reduced inspection (saving time and money), while problematic suppliers face tightened scrutiny (protecting the consumer).

## Inspection Types

### Incoming Inspection

Validates raw materials and components before they enter the production process. In semiconductor manufacturing:

**Photoresist**: Viscosity measurement (±0.5 cSt), particle count (<10 particles/mL ≥ 0.2 μm), spectral absorption at exposure wavelength, shelf life verification. Sample: 1 bottle per batch (destructive testing of viscosity and particle count).

**Process gases (N₂, O₂, Ar, SiH₄, NF₃)**: Purity analysis by gas chromatography. Semiconductor-grade gases: 99.999% (5N) minimum, with specific limits on H₂O (<1 ppm), O₂ (<1 ppm), and total hydrocarbons (<1 ppm). Sample: 1 cylinder per delivery lot.

**Silicon wafers**: Crystal orientation (X-ray diffraction, ±0.5°), resistivity (four-point probe, ±5%), flatness (laser interferometry, ≤2 μm TTV — Total Thickness Variation), particle count (laser surface scanner, ≤10 particles ≥ 0.16 μm per wafer). Sample: per MIL-STD-105E, AQL 0.25%.

**Etchants and cleaning chemicals**: Concentration (titration, ±0.1%), metallic contamination (ICP-MS, ≤1 ppb for critical metals: Fe, Cu, Ni, Zn, Cr), particle count. Sample: 1 bottle per batch.

### In-Process Inspection

Monitors critical process steps during manufacturing. Distinguished from SPC monitoring by focusing on pass/fail decisions on production material rather than statistical trend analysis.

**Post-lithography inspection**: Verify CD (critical dimension) on test structures using CD-SEM. Sample: first wafer, last wafer, and one wafer per 5-wafer interval in each lot. Acceptance: CD within ±10% of target for the technology node.

**Post-etch inspection**: Visual inspection for etch residue, undercut, and feature profile. Sample: 100% inspection of test wafers, sample of production wafers. Optical microscopy at 200-500× magnification.

**Post-CMP inspection**: Measure remaining oxide thickness (spectroscopic ellipsometry, ±2 nm). Sample: 5-point map per wafer (center + 4 quadrant points), 3 wafers per lot of 25. Acceptance: thickness within ±5% of target.

**Metal deposition inspection**: Sheet resistance (four-point probe, ±1%), step coverage on cross-sectioned test structures (SEM, ≥50% of nominal thickness on vertical sidewalls). Sample: monitor wafer per deposition run.

### Final Test

The last quality gate before product shipment. For semiconductor die:

**Wafer sort (probe test)**: Electrical test of every die on every wafer — this is one area where 100% inspection is standard because defective die must be identified and excluded from packaging. Test includes continuity, leakage, parametric (Vth, Idsat, breakdown voltage), and functional patterns. Typical test time: 1-5 seconds per die.

**Burn-in**: Subject packaged parts to elevated temperature (125-150°C) and voltage stress for 24-168 hours to accelerate infant mortality failures. Sample: 100% for Class S (space), Class B (military); sample per MIL-STD-883 for commercial grades.

**Final electrical test (ATE)**: Automated test equipment verifies full specification compliance (speed, power, functionality across temperature range — typically tested at −40°C, +25°C, +85°C or +125°C). 100% of packaged parts.

## Sampling Plan Design

### Variables Sampling

When measurements are on a continuous scale (dimensions, voltages, weights), variables sampling plans are more efficient than attribute plans — they require smaller sample sizes for equivalent protection.

**Known sigma plan (sigma known)**:
- Sample size: n = [(Z_α + Z_β) × σ / (USL − μ_AQL)]²
- Accept criterion: x̄ ≤ USL − k × σ (upper spec) or x̄ ≥ LSL + k × σ (lower spec)
- k is the acceptability constant, typically k = 1.4-2.0 depending on AQL

**Unknown sigma plan (sigma estimated from sample)**:
- Uses t-distribution instead of normal. Sample size slightly larger.
- Accept criterion: x̄ + k × s ≤ USL (where s is the sample standard deviation)

**Advantage over attribute sampling**: For the same OC curve, variables sampling typically requires 30-50% fewer samples. Critical in semiconductor where each measurement may be expensive (destructive testing, SEM time, wafer consumption).

### Skip-Lot Sampling

When a supplier has demonstrated consistent quality over an extended period (20+ consecutive lots accepted), skip-lot sampling inspects only a fraction of lots:

- **Skip-lot frequency**: Inspect 1 lot in 2, or 1 lot in 3, or 1 lot in 4 depending on quality history.
- **Skipping criteria**: 20 consecutive lots accepted, no quality complaints, no process changes at supplier.
- **Return to normal**: Any skipped-lot failure or supplier quality issue immediately returns to 100% lot inspection.

## Semiconductor-Specific Inspection Standards

### MIL-STD-883 (Microcircuit Test Methods)

The foundational standard for integrated circuit testing, defining test methods, inspection procedures, and quality conformance requirements:

- **Method 2010**: Internal visual inspection (die surface, bonding, metallization defects)
- **Method 2012**: External visual inspection (package integrity, marking, lead condition)
- **Method 2020**: Particle impact noise detection (PIND) for loose particles inside hermetic packages
- **Method 2032**: X-ray radiographic inspection (wire bonds, die attach quality)
- **Method 5004**: Screening procedures (burn-in, temperature cycling, centrifuge, fine/gross leak)

### JEDEC Standards

- **JESD22**: Reliability test methods for packaged devices
- **JESD51**: Thermal measurement standards
- **JP001**: Foundry process qualification guidelines

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Metals | Incoming inspection of raw ores and alloys (composition, impurity analysis) |
| Silicon | Wafer incoming inspection (orientation, resistivity, flatness, particles) |
| Photolithography | Post-exposure CD inspection, overlay registration check |
| VLSI Scaling | Advanced inspection: e-beam inspection, optical overlay metrology, defect review |
| Electronics | PCB incoming component inspection, solder joint quality (X-ray, AOI) |

## Key Deliverables

- MIL-STD-105E sampling tables implemented in SPC software
- AQL targets defined for all incoming materials (0.10% - 0.65%)
- Incoming inspection procedures for photoresist, gases, wafers, chemicals
- In-process inspection sampling plans for lithography, etch, CMP, deposition
- Wafer sort (100%) and final test (100%) procedures
- Switching rules (normal/tightened/reduced) operational in quality management system
- Skip-lot program for qualified suppliers

## Limitations

- **Sampling risk**: Any sampling plan has inherent risk — good lots can be rejected (producer's risk) and bad lots can be accepted (consumer's risk). The OC curve quantifies these risks but cannot eliminate them.
- **Lot homogeneity**: Sampling assumes the lot is homogeneous — defects are randomly distributed. If defects cluster (common in semiconductor — particle contamination from a single tool can affect consecutive wafers), random sampling may miss the affected subgroup. Stratified sampling within lots mitigates this.
- **Inspection fatigue**: Human visual inspectors miss 10-20% of defects due to fatigue, especially in repetitive tasks. Automated optical inspection (AOI) and automated X-ray inspection (AXI) reduce but do not eliminate this.
- **Destructive testing**: Some inspections are destructive (cross-sectioning for step coverage, chemical analysis of etchants). Destructive samples are consumed and cannot be retested. Sampling plans for destructive tests must be carefully optimized.
- **Cost of over-inspection**: Excessive inspection increases cost without proportional quality improvement. The optimal inspection level depends on the cost of a defective unit escaping versus the cost of inspection.

## See Also

- [Statistical Process Control](statistical-process-control.md) — control charts, Cpk, Western Electric rules
- [Defect Analysis & Yield Modeling](defect-analysis.md) — Pareto, FMEA, yield models
- [Measurement](../measurement/index.md) — instruments and calibration for inspection
- [Optics](../optics/index.md) — optical inspection and microscopy

---

*Part of the [Bootciv Tech Tree](../index.md) • [Quality Control](./index.md) • [All Domains](../index.md)*
