# Defect Analysis & Yield Modeling

> **Node ID**: quality-control.defect-analysis
> **Domain**: [Quality Control](./index.md)
> **Dependencies**: `quality-control`, `quality-control.spc`
> **Enables**: None (leaf capability)
> **Timeline**: Years 40-100+
> **Outputs**: fmea, pareto_analysis, fishbone_diagrams, yield_models, defect_density, root_cause_analysis

## Problem

Semiconductor fabrication involves 500+ sequential process steps across photolithography, etch, deposition, implantation, and CMP. Each step introduces potential defects — particles, pattern distortions, contamination, thickness non-uniformity. A single killer defect on a die renders it non-functional, yet a modern 300 mm wafer contains hundreds of thousands of die. Understanding which defects matter, where they come from, and how to eliminate them is the central engineering challenge of semiconductor yield management.

Yield for mature semiconductor nodes typically runs 60-90%, meaning 10-40% of manufactured die are thrown away. For leading-edge nodes, yield drops below 50% during initial production. At a fab producing 50,000 wafers per month with each wafer worth $5,000-50,000, every percentage point of yield improvement translates to millions of dollars in revenue. Defect analysis provides the systematic methodology to identify, prioritize, and eliminate yield-limiting mechanisms.

## Pareto Analysis

The Pareto principle (80/20 rule) states that approximately 80% of defects come from 20% of the causes. Pareto analysis identifies the "vital few" defect types that dominate yield loss, enabling focused engineering effort on the highest-impact problems.

### Pareto Chart Construction

1. **Collect defect data**: From wafer sort results, in-process inspection, and final test. Categorize each defect by type (particle, scratch, pattern defect, electrical fail) and by process step (lithography, etch, deposition, CMP).

2. **Tabulate defect frequencies**: Count occurrences of each defect category over a representative period (typically 1-4 weeks of production).

3. **Sort by frequency**: Rank defect categories from most to least frequent.

4. **Calculate cumulative percentage**: Running total of defect percentage.

5. **Plot**: Bar chart of defect frequency (descending) with a line overlay showing cumulative percentage.

### Pareto Analysis Example: 28nm Logic Fab

| Defect Type | Count | % of Total | Cumulative % |
|------------|-------|-----------|-------------|
| Particle contamination (metal1 deposition) | 1,247 | 32.1 | 32.1 |
| Pattern bridging (metal1 lithography) | 892 | 23.0 | 55.1 |
| Etch residue (via etch) | 534 | 13.8 | 68.9 |
| CMP scratching (oxide CMP) | 421 | 10.8 | 79.7 |
| Particle contamination (gate lithography) | 287 | 7.4 | 87.1 |
| Gate oxide pinhole | 198 | 5.1 | 92.2 |
| Contact misalignment | 143 | 3.7 | 95.9 |
| Metal corrosion | 98 | 2.5 | 98.4 |
| Other (12 categories) | 62 | 1.6 | 100.0 |

**Analysis**: The top 4 defect types account for 79.7% of all defects. Focused effort on metal1 deposition particles and metal1 lithography bridging alone would address over 55% of the total yield loss. Resource allocation: assign your best engineers to the top 3 problems before attacking the remaining items.

### Stratified Pareto Analysis

Simple Pareto charts can mask important patterns. Stratify by:
- **Process tool**: Which specific tool generates the most defects? A single poorly maintained etch chamber may dominate.
- **Time period**: Is the defect rate constant, increasing, or intermittent? Increasing trends suggest tool degradation.
- **Product type**: Does the defect affect all products equally, or is it specific to certain designs?
- **Wafer position**: Do defects cluster at the wafer edge, center, or specific radial position? Edge defects suggest handling or chuck contamination; center defects suggest process non-uniformity.

## Fishbone (Ishikawa) Diagrams

The fishbone diagram (also called cause-and-effect diagram) systematically catalogs all potential root causes of a quality problem, organized by category. The diagram resembles a fish skeleton — the "head" is the effect (the defect), and the "bones" are the causes.

### Major Cause Categories (6M Framework)

For manufacturing defect analysis, causes are organized into six categories (the 6Ms):

1. **Man (Personnel)**: Operator skill, training, fatigue, procedure compliance, technique variation
2. **Machine**: Tool condition, calibration, maintenance schedule, wear, software version, consumable parts
3. **Material**: Raw material quality, supplier consistency, shelf life, storage conditions, contamination level
4. **Method**: Process recipe, parameter settings, sequence, handling procedures, cleanup between steps
5. **Measurement**: Inspection method resolution, gage R&R, sampling adequacy, calibration accuracy
6. **Mother Nature (Environment)**: Temperature, humidity, vibration, cleanroom class, electromagnetic interference, particle levels

### Fishbone Construction Process

1. **Define the effect**: Write the defect clearly at the "head" of the diagram (e.g., "Metal1 bridging defect rate >5%").

2. **Draw major category bones**: Create six branches labeled with the 6M categories.

3. **Brainstorm causes**: For each category, list all possible contributing factors. Use "5 Whys" technique — ask "why?" five times to drill from symptoms to root causes.

4. **Sub-branch specific causes**: Break each cause into more specific contributing factors.

5. **Prioritize**: Circle or highlight the causes most likely to contribute based on data (SPC charts, defect inspection data, tool maintenance logs).

6. **Validate**: Design experiments or collect additional data to confirm or eliminate hypothesized causes.

### Example: Metal1 Bridging Defect Fishbone

```
                    Man                    Machine
                 ┌─ Operator technique  ┌─ Focus offset
                 ├─ Training gaps       ├─ Lens contamination
                 └─ Fatigue (shift 3)   └─ Stage vibration
                        │                       │
    Material ──────────┤   Metal1 Bridging  ├─────── Method
  ┌─ Photoresist age   │     Defect >5%     │  ┌─ Exposure dose
  ├─ BARC thickness    │                    │  ├─ PEB time/temp
  └─ Developer conc.   │                    │  └─ Rinse duration
                        │                       │
                 ┌─ CD-SEM drift      ┌─ Humidity excursion
    Measurement ─┤                    ├─────── Environment
                 ├─ Sampling too small │  ├─ Particle spike
                 └─ Calibration lag    └─ EMI from new tool
```

**Root cause identified**: Cross-referencing fishbone analysis with SPC data showed that bridging defects correlated with humidity excursions above 45% RH in the lithography bay. Humidity affects photoresist coating uniformity and development rate. Solution: tighter humidity control (43% ± 2% RH) in the lithography area.

## FMEA (Failure Mode and Effects Analysis)

FMEA is a systematic, proactive method for identifying potential failure modes, assessing their risk, and prioritizing corrective actions before failures occur in production. It is performed during process design — before manufacturing begins — to build quality into the process.

### FMEA Structure

| Column | Description |
|--------|-------------|
| Process Step | The specific manufacturing operation (e.g., "Gate lithography exposure") |
| Potential Failure Mode | How the step could fail (e.g., "CD too large", "CD too small", "Pattern bridging") |
| Potential Effect of Failure | What happens to the product (e.g., "Slow circuit speed", "Leaky gate", "Short circuit") |
| Severity (S) | 1-10 scale. 1 = negligible effect, 10 = hazardous without warning |
| Potential Cause of Failure | Why the failure mode might occur (e.g., "Focus drift", "Dose error", "Contamination") |
| Occurrence (O) | 1-10 scale. 1 = remote likelihood, 10 = very high likelihood |
| Current Controls | Existing detection/prevention methods (e.g., "CD-SEM measurement", "In-line particle monitor") |
| Detection (D) | 1-10 scale. 1 = almost certain to detect, 10 = almost impossible to detect |
| RPN (Risk Priority Number) | S × O × D (range 1-1000) |
| Recommended Actions | Steps to reduce RPN (reduce severity, occurrence, or improve detection) |

### Severity Rating Scale (Semiconductor-Adapted)

| Rating | Effect | Example |
|--------|--------|---------|
| 1 | No effect | Minor cosmetic imperfection on non-functional area |
| 2-3 | Minor annoyance | Slight parametric shift, still within spec |
| 4-5 | Moderate degradation | Performance margin reduced, yield loss 1-5% |
| 6-7 | Significant degradation | Circuit fails speed bin, yield loss 5-20% |
| 8-9 | Severe failure | Circuit non-functional, yield loss >20% |
| 10 | Catastrophic | Safety hazard, complete wafer loss, fab shutdown |

### Occurrence Rating Scale

| Rating | Frequency | Approx. Defect Rate |
|--------|-----------|-------------------|
| 1 | Remote | <1 in 10⁶ |
| 2 | Very low | 1 in 100,000 |
| 3 | Low | 1 in 10,000 |
| 4-5 | Moderate | 1 in 1,000 to 1 in 500 |
| 6-7 | High | 1 in 100 to 1 in 50 |
| 8-9 | Very high | 1 in 20 to 1 in 10 |
| 10 | Almost certain | >1 in 10 |

### Detection Rating Scale

| Rating | Detection Capability |
|--------|---------------------|
| 1 | Almost certain (automated 100% inline inspection) |
| 2-3 | Very high (SPC with tight limits, frequent sampling) |
| 4-5 | Moderate (periodic sampling, standard inspection) |
| 6-7 | Low (sampling only, limited test coverage) |
| 8-9 | Very low (inspection at later step, delay in detection) |
| 10 | Almost impossible (no inspection, hidden defect) |

### FMEA Prioritization

- **RPN > 200**: Immediate action required. Process cannot proceed without corrective measures.
- **RPN 100-200**: Action required before production ramp. Schedule corrective actions.
- **RPN 50-100**: Improvement desirable. Address during continuous improvement cycle.
- **RPN < 50**: Acceptable risk. Monitor during production.

### Semiconductor Process FMEA Example (Excerpt)

| Step | Failure Mode | Effect | S | Cause | O | Control | D | RPN |
|------|-------------|--------|---|-------|---|---------|---|-----|
| Gate litho exposure | CD too large | Slow circuit, fails speed test | 7 | Focus drift | 4 | CD-SEM | 3 | 84 |
| Gate litho exposure | CD too small | Leaky gate, high leakage current | 8 | Overexposure | 3 | CD-SEM | 3 | 72 |
| Gate litho exposure | Pattern bridging | Short circuit, die fail | 9 | Particle on mask | 5 | Inline insp. | 4 | 180 |
| Gate etch | Undercut | Reduced gate width, speed variation | 7 | Over-etch | 3 | X-section SEM | 5 | 105 |
| Gate oxide growth | Pinhole defect | Gate oxide breakdown, die fail | 9 | Particle pre-oxidation | 4 | GOI test | 3 | 108 |
| CMP oxide polish | Scratch | Metal short after fill | 6 | Slurry particle | 6 | Visual insp. | 4 | 144 |
| Metal1 deposition | Particle contamination | Open/short circuits | 8 | Chamber contamination | 5 | Particle monitor | 3 | 120 |

**Priority actions**: Pattern bridging at gate lithography (RPN 180) — improve mask cleaning and particle monitoring. CMP scratching (RPN 144) — improve slurry filtration. Metal1 particle contamination (RPN 120) — increase chamber clean frequency.

## Yield Modeling

Yield models predict the fraction of functional die on a wafer based on defect density, die area, and process complexity. These models guide process development investment, product sizing decisions, and fab capacity planning.

### Murphy's Yield Model

The most commonly used yield model for semiconductor manufacturing:

**Y = [(1 − e^(−D₀A)) / (D₀A)]²**

Where:
- Y = yield (fraction of functional die)
- D₀ = defect density (defects per cm²)
- A = die area (cm²)

This model assumes a uniform spatial distribution of defects with a specific probability distribution for defect clustering.

**Murphy's yield table** (pre-computed values):

| D₀ (defects/cm²) | Die Area | Yield (Murphy) | Functional Die per 300mm Wafer |
|-------------------|----------|---------------|-------------------------------|
| 0.01 | 50 mm² | 99.8% | ~1,417 |
| 0.05 | 50 mm² | 99.0% | ~1,406 |
| 0.10 | 50 mm² | 97.6% | ~1,386 |
| 0.50 | 50 mm² | 88.9% | ~1,262 |
| 1.00 | 50 mm² | 79.5% | ~1,129 |
| 0.01 | 200 mm² | 99.0% | ~338 |
| 0.05 | 200 mm² | 95.2% | ~325 |
| 0.10 | 200 mm² | 90.9% | ~310 |
| 0.50 | 200 mm² | 69.3% | ~237 |
| 1.00 | 200 mm² | 52.2% | ~178 |

### Seeds Model

An alternative yield model that accounts for defect clustering more aggressively:

**Y = 1 / (1 + D₀A)^α**

Where α is the clustering parameter (typically α = 1-2 for semiconductor processes). With α = 1:

**Y = 1 / (1 + D₀A)**

The Seeds model predicts lower yields than Murphy's for the same D₀ and A when D₀A > 1, making it more conservative (and often more realistic for leading-edge processes with high defect densities).

### Composite Yield

For a process with N sequential steps, each with individual yield Y_i:

**Y_total = Y₁ × Y₂ × Y₃ × ... × Y_N = ∏Y_i**

This multiplicative relationship explains why semiconductor yield is so challenging — a 500-step process with 99.9% yield per step gives total yield of 0.999^500 = 60.6%. A 500-step process with 99.95% yield per step gives 77.8%. Small per-step improvements compound into large total yield gains.

**Defect budget allocation**: For a target total yield Y_target across N steps, allocate per-step defect density budget:

Y_target^(1/N) = minimum acceptable per-step yield

Example: Target yield 80% over 500 steps → per-step yield target = 0.80^(1/500) = 0.9996 (99.96%). Per-step defect density budget = −ln(0.9996) / A_die (for exponential defect model).

### Yield Learning Curve

Yield improves predictably over time following a learning curve:

**Y(t) = Y_∞ × (1 − e^(−t/τ))**

Where Y_∞ is the asymptotic (mature process) yield and τ is the learning time constant. Typical values:
- Mature node: Y_∞ = 85-95%, τ = 6-12 months
- Leading edge: Y_∞ = 70-85%, τ = 18-36 months

Yield learning is driven by systematic defect reduction: identify the top yield limiter (via Pareto analysis), eliminate it (via fishbone + FMEA + DOE), measure the improvement (via SPC), and move to the next yield limiter. Each cycle takes 2-6 weeks in a mature fab.

## Root Cause Analysis (RCA)

RCA is the structured methodology for investigating quality excursions — unexpected yield drops, out-of-control events, or customer returns. RCA goes beyond symptoms to identify the fundamental cause that, when corrected, prevents recurrence.

### 5 Whys Technique

Ask "why?" iteratively to drill from symptom to root cause:

1. **Why did yield drop 15%?** → Metal1 bridging defects increased from 2% to 17% of die
2. **Why did bridging increase?** → Photoresist pattern collapsed during development
3. **Why did pattern collapse?** → Photoresist aspect ratio exceeded 4:1 (too tall and thin)
4. **Why was aspect ratio too high?** → Resist thickness increased from 1.2 μm to 1.8 μm
5. **Why did resist thickness increase?** → Spin coater speed dropped from 3000 RPM to 2000 RPM due to worn motor bearings

**Root cause**: Worn spin coater motor bearings causing reduced spin speed. **Corrective action**: Replace bearings, add spin speed verification to daily tool qualification.

### Kepner-Tregoe Problem Analysis

A more formal RCA methodology for complex problems with multiple potential causes:

1. **Define the problem**: What is the defect? Where is it observed? When did it start? How extensive is it?
2. **Specify distinctions**: What is unique about the problem compared to normal operation? What changed?
3. **Generate possible causes**: Brainstorm all hypotheses consistent with the observed distinctions.
4. **Test causes against facts**: For each hypothesis, what additional evidence would confirm or refute it?
5. **Verify root cause**: Confirm the identified cause by reproducing the defect (if safe) or by observing that the corrective action eliminates the problem.

### Data Mining for Root Cause

In semiconductor fabs with extensive data collection (FDC — Fault Detection and Classification data from every tool, for every wafer, for every step), statistical correlation analysis can identify root causes:

- **Wafer map analysis**: Plot defect locations on wafer maps. Spatial patterns (edge ring, center spot, radial stripe) implicate specific tools or process conditions.
- **Tool commonality analysis**: Cross-reference defective wafers with the specific tools they passed through. If all defective wafers used Chamber 3 of the etch tool but good wafers used Chambers 1, 2, and 4, Chamber 3 is the likely source.
- **Time-series correlation**: Correlate defect rate with process parameter logs (temperature, pressure, gas flow). A step-change in etch temperature coinciding with the defect onset is strong evidence of a causal relationship.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Silicon | Crystal defect analysis (dislocation density, OSF — Oxidation-Induced Stacking Faults) |
| Photolithography | Pattern defect Pareto, overlay error analysis, mask defect classification |
| VLSI Scaling | Advanced yield modeling (critical area analysis), design-for-manufacturing (DFM) feedback |
| Electronics | Solder joint defect analysis, PCB via yield modeling, component-level FMEA |
| Computing | Automated defect classification (ADC), yield simulation, statistical analysis |

## Key Deliverables

- Pareto analysis for all yield-limiting defect types, updated weekly
- Fishbone diagrams for top 5 yield-limiting defects
- Process FMEA for all critical process steps (gate, contact, metal layers)
- Yield model calibrated to fab data (Murphy's or Seeds model with measured D₀)
- Defect density tracking database with trend analysis
- Root cause analysis reports for all significant yield excursions
- Defect learning curve tracking (yield vs. time, per product and per process step)

## Limitations

- **Model assumptions**: Yield models assume random defect distribution, but real defects cluster spatially and temporally. Model predictions are approximate guidelines, not precise forecasts.
- **FMEA completeness**: FMEA quality depends on the team's ability to anticipate all possible failure modes. Unknown failure modes (the "unknown unknowns") escape analysis until they manifest in production.
- **Data overload**: Modern fabs generate terabytes of process data. Distinguishing signal from noise requires statistical expertise and automated analysis tools.
- **Intermittent defects**: Some defects occur sporadically (e.g., particle from a rarely-actuated valve). These are the hardest to root-cause because the defect is not reproducible on demand.
- **Multi-factor interactions**: Defects often result from the interaction of multiple process variables, not a single root cause. A marginal photoresist combined with a slight temperature excursion may cause defects that neither condition alone would produce. DOE (Design of Experiments) is needed to detect interactions.

## See Also

- [Statistical Process Control](statistical-process-control.md) — control charts, Cpk, Six Sigma
- [Inspection & Sampling Plans](inspection-sampling.md) — AQL, MIL-STD-105E, incoming/in-process/final inspection
- [Measurement](../measurement/index.md) — metrology for defect characterization
- [Computing](../computing/index.md) — automated defect classification and yield simulation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Quality Control](./index.md) • [All Domains](../index.md)*
