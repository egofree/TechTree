# Statistical Process Control

> **Node ID**: quality-control.spc
> **Domain**: [Quality Control](./index.md)
> **Dependencies**: [`measurement`](../measurement/index.md), [`computing`](../computing/index.md)
> **Enables**: [`quality-control.defect-analysis`](defect-analysis.md)
> **Timeline**: Years 40-100+
> **Outputs**: spc_charts, cpk_indices, process_capability_analysis, six_sigma_metrics, control_limits
> **Critical**: No — manufacturing can operate without SPC but yields will be lower and defect costs higher

## Overview

Statistical process control answers a fundamental manufacturing question: "Is this process producing consistent output, or has something changed?" By sampling process output over time and plotting results on control charts, operators distinguish between normal random variation (common cause) and abnormal shifts (special cause). Reacting to common cause wastes effort; ignoring special cause produces defects.

Without SPC, manufacturing relies on 100% inspection (expensive — inspectors miss defects) or hope (no methodology). SPC replaces both with a statistical system that detects problems before defective products accumulate. The transition from "inspect quality in" to "build quality in" is one of the most consequential shifts in manufacturing philosophy, and SPC is the mathematical tool that makes it possible.

Semiconductor manufacturing involves hundreds of sequential process steps, each introducing variability. A single out-of-control diffusion furnace can ruin 25 wafers containing thousands of die worth tens of thousands of dollars. Semiconductor yield runs 60-90% for mature nodes but drops below 50% for leading-edge technology. At these yields, the difference between Cpk 1.0 and 1.33 can mean profit or loss on an entire fab. SPC is not optional — it is the operating system of manufacturing quality.

## Prerequisites

- [Measurement and metrology](../measurement/index.md) — calibrated instruments with resolution ≥10× finer than the tolerance being controlled
- [Computing](../computing/index.md) — data recording, statistical calculation, and chart generation
- [Applied mathematics](../mathematics/applied-mathematics.md) — probability, statistics, normal distribution theory
- Data collection forms, reference standards, and a calibration system traceable to national standards
- Understanding of statistical distributions (normal, binomial, Poisson) and which applies to each data type

## Safety

No physical hazards — SPC is an analytical discipline. Workstation ergonomics apply: proper posture, adequate lighting, and regular breaks during extended data analysis sessions. Repetitive measurement tasks can cause hand and wrist strain; vary tasks and use ergonomically designed instruments.

## Control Charts

Control charts plot process measurements over time with statistically-derived control limits that distinguish common-cause variation from special-cause variation.

### Selecting the Right Chart

| Data Type | Distribution | Chart | Application |
|-----------|-------------|-------|-------------|
| Continuous (dimensions, temperatures) | Normal | X-bar and R | Gate CD, oxide thickness, etch rate, machining dimensions |
| Proportion defective | Binomial | p-chart | Wafer sort yield, visual defect rate |
| Count of defects per unit | Poisson | c-chart | Particles per wafer, scratches per panel |
| Defect density (variable area) | Poisson | u-chart | Defects per cm² across different wafer sizes |
| Individual measurements | Normal | I-MR | Furnace temperature, one reading per run |

### Control Limit Formulas

| Chart | Center Line | UCL | LCL |
|-------|-----------|-----|-----|
| X-bar | X̄ (grand mean) | X̄ + A₂ × R̄ | X̄ − A₂ × R̄ |
| R | R̄ (average range) | D₄ × R̄ | D₃ × R̄ |
| p | p̄ | p̄ + 3√(p̄(1−p̄)/n) | max(0, p̄ − 3√(p̄(1−p̄)/n)) |
| c | c̄ | c̄ + 3√c̄ | max(0, c̄ − 3√c̄) |
| u | ū | ū + 3√(ū/aᵢ) | max(0, ū − 3√(ū/aᵢ)) |

### Control Chart Constants

| n | A₂ | D₃ | D₄ | d₂ |
|---|----|----|----|----|
| 2 | 1.880 | 0 | 3.267 | 1.128 |
| 3 | 1.023 | 0 | 2.575 | 1.693 |
| 4 | 0.729 | 0 | 2.282 | 2.059 |
| 5 | 0.577 | 0 | 2.114 | 2.326 |
| 6 | 0.483 | 0 | 2.004 | 2.534 |
| 7 | 0.419 | 0.076 | 1.924 | 2.704 |
| 8 | 0.373 | 0.136 | 1.864 | 2.847 |
| 9 | 0.337 | 0.184 | 1.816 | 2.970 |
| 10 | 0.308 | 0.223 | 1.777 | 3.078 |

d₂ converts average range to estimated standard deviation: σ̂ = R̄ / d₂.

### Sampling Plans

**Variables sampling for continuous production (X-bar/R charts):**

| Production Rate | Subgroup Size | Frequency | Rationale |
|----------------|--------------|-----------|-----------|
| < 50 parts/hr | 3-5 | Every 1-2 hours | Low-volume; each subgroup represents one lot |
| 50-500 parts/hr | 5 | Every 30-60 min | Standard production; detects shifts within 1 hour |
| 500-5000 parts/hr | 5 | Every 15-30 min | High-volume; fast detection required |
| > 5000 parts/hr | 5-10 | Every 5-15 min | Real-time monitoring needed |
| Critical semiconductor params | 5 wafers | Every lot | Cpk tracked per lot |

**Lot-by-lot acceptance sampling (ANSI/ASQ Z1.4):**

| Lot Size | Sample (AQL 1.0%) | Ac | Sample (AQL 0.65%) | Ac |
|----------|-------------------|----|---------------------|----|
| 26-50 | 8 | 0 | 8 | 0 |
| 51-90 | 13 | 0 | 13 | 0 |
| 91-150 | 20 | 0 | 20 | 0 |
| 151-280 | 32 | 1 | 32 | 0 |
| 281-500 | 50 | 1 | 50 | 1 |
| 501-1200 | 80 | 2 | 80 | 1 |
| 1201-3200 | 125 | 3 | 125 | 2 |
| 3201-10,000 | 200 | 5 | 200 | 3 |

Ac = maximum defective units allowed before rejecting the lot.

### Western Electric Rules

The rules detect non-random patterns indicating shifts, trends, or cycles — even when no point exceeds 3σ limits. Zones: A (2σ-3σ), B (1σ-2σ), C (within 1σ).

| Rule | Pattern | Interpretation |
|------|---------|----------------|
| 1 | 1 point beyond Zone A (beyond 3σ) | Large sudden shift |
| 2 | 2 of 3 consecutive in Zone A (same side) | Moderate shift |
| 3 | 4 of 5 consecutive in Zone B (same side) | Small sustained shift |
| 4 | 8 consecutive on one side of center line | Process mean drift |
| 5 | 6 consecutive increasing or decreasing | Trend (tool wear, degradation) |
| 6 | 14 consecutive alternating up and down | Over-adjustment or stratification |
| 7 | 15 consecutive in Zone C | Too little variation — data manipulation or stratification |

Applying all rules yields ~1 false alarm per 150 subgroups (vs 1 per 370 for 3σ alone). The increased sensitivity is worthwhile in semiconductor manufacturing where undetected shifts are extremely costly.

## Process Capability

Process capability compares the natural process spread to specification limits.

**Cp** = (USL − LSL) / (6σ) — potential capability assuming perfect centering.

**Cpk** = min[(USL − μ̄) / (3σ), (μ̄ − LSL) / (3σ)] — actual capability accounting for centering. Cpk ≤ Cp always; Cpk = Cp only when perfectly centered.

**Pp/Ppk** use overall (total) standard deviation instead of within-subgroup estimate. Used for preliminary assessment or when process is not yet in statistical control. If Ppk ≈ Cpk, the process is stable. If Ppk << Cpk, significant between-subgroup variation exists.

### Capability Targets

| Cpk | Sigma Level | Defect Rate (ppm) | Assessment |
|-----|-------------|-------------------|------------|
| 0.50 | 1.5σ | 133,614 | Inadequate: significant out-of-spec output |
| 0.67 | 2.0σ | 45,500 | Poor: ~4.5% defective |
| 1.00 | 3.0σ | 2,700 | Marginal: barely within specification |
| 1.10 | 3.3σ | 967 | Below minimum; must improve |
| 1.33 | 4.0σ | 63 | Minimum acceptable for semiconductor |
| 1.50 | 4.5σ | 6.8 | Good: general precision target |
| 1.67 | 5.0σ | 0.6 | Excellent: critical dimensions |
| 2.00 | 6.0σ | 0.002 | Six Sigma: near-zero defect goal |

### Cpk Worked Example

Given shafts with diameter spec 25.000 ± 0.025 mm (USL = 25.025, LSL = 24.975):

From 30 subgroups of n = 5 (150 readings): X̄ = 25.003 mm, R̄ = 0.018 mm, σ̂ = R̄/d₂ = 0.018/2.326 = 0.00774 mm

- **Cp** = (25.025 − 24.975) / (6 × 0.00774) = 0.050/0.0464 = **1.08**
- **Cpk** = min((25.025 − 25.003)/0.0232, (25.003 − 24.975)/0.0232) = min(0.95, 1.21) = **0.95**

Cpk = 0.95 means not capable. The process mean must shift toward spec center, or variation must be reduced. Expected defect rate: ~5,200 ppm (0.52%).

### Semiconductor Cpk Requirements

| Process Step | Critical Parameter | Minimum Cpk | Target Cpk |
|-------------|-------------------|-------------|-----------|
| Gate lithography | Critical dimension | 1.33 | 1.50 |
| Gate etch | Etch bias | 1.33 | 1.50 |
| Implant | Dose uniformity | 1.33 | 1.50 |
| CMP | Oxide thickness | 1.33 | 1.67 |
| Diffusion | Sheet resistance | 1.33 | 1.50 |
| Metal deposition | Thickness | 1.33 | 1.50 |
| Wafer sort | Probe yield | 1.00 | 1.33 |

## CUSUM and EWMA Charts

Shewhart charts detect large shifts (≥1.5σ) reliably. For detecting small, persistent shifts, two alternatives offer superior sensitivity:

- **CUSUM (Cumulative Sum)**: Accumulates deviations from target. Detects sustained shifts of 0.5-1.5σ that Shewhart charts miss. More complex to set up (requires choosing reference value k and decision interval h) but significantly more sensitive to gradual drifts.
- **EWMA (Exponentially Weighted Moving Average)**: Weights recent data more heavily than older data. Provides a smoothed estimate of the process mean. The smoothing parameter λ (typically 0.05-0.25) controls sensitivity vs stability trade-off.

Both are used for critical parameters where early detection of small shifts matters: semiconductor manufacturing, pharmaceutical production, and chemical process control.

**Pre-control** is a simplified alternative using specification zones rather than statistical limits. Easier to implement than full SPC but less rigorous — useful as a stepping stone or for low-volume production where insufficient data exists for control limit calculation.

## Six Sigma and DMAIC

Six Sigma aims to reduce variation to below 3.4 DPMO, corresponding to Cpk ≥ 1.50 with a 1.5σ mean shift assumption. Compounding gains are powerful: improving per-step yield from 99.9% to 99.95% increases 500-step total yield from 60.6% to 77.8%.

### DMAIC Cycle

1. **Define**: Identify the quality problem, define scope and goals, map the process (SIPOC). For semiconductor: define the yield-limiting step (e.g., "improve gate CD Cpk from 1.10 to 1.50").

2. **Measure**: Collect baseline data. Validate measurement system (Gage R&R — measurement variation must be <10% of total). Establish Cpk baseline and initial control charts.

3. **Analyze**: Identify root causes using hypothesis testing (t-tests, ANOVA), regression, correlation, multi-vari charts. Determine which input variables most strongly influence the output. Example: "which of temperature, pressure, gas flow, and time most affects etch rate uniformity?"

4. **Improve**: Design and implement changes using Design of Experiments (DOE). Full or fractional factorial designs (2^k or 2^(k-p)) systematically vary factors to find optimal settings. Target: Cpk improvement ≥ 0.33.

5. **Control**: Implement SPC on the improved process. Update control limits. Document SOPs. Establish response plans for out-of-control conditions. Hand off to production team.

**Limitations**: DMAIC cycle time of 2-6 weeks per project — too slow for rapid process development. Requires extensive data infrastructure (SECS/GEM, FDC systems). Assumes approximately normal data distributions — non-normal processes require transformations.

## Gage R&R

Before any SPC study, validate the measurement system. Gage R&R quantifies how much observed variation comes from the measurement system itself.

**Study design**: 10 parts × 3 operators × 2 trials = 60 measurements. Parts should span the expected process range.

**Components**: Repeatability (equipment variation — same operator, same part), Reproducibility (appraiser variation — different operators), Part variation (the signal we want to measure).

| Gage R&R | Assessment | Action |
|----------|-----------|--------|
| < 10% | Acceptable | Adequate for SPC |
| 10-30% | Marginal | Acceptable for non-critical; improve for critical |
| > 30% | Unacceptable | Must improve before collecting SPC data |

**Improvement strategies**: Repeatability >10% → instrument resolution too coarse (need 10× finer than tolerance) or fixture allows positioning variation. Reproducibility >10% → operators use different technique; write detailed procedure with photos and retrain. Both high → instrument is inadequate; replace before attempting SPC.

**Semiconductor-specific**: For critical dimension measurement, CD-SEM Gage R&R must be <5% because tolerances are extremely tight (±2-5 nm on 20-40 nm gate lengths). Requires temperature-controlled metrology rooms and automated routines that minimize operator influence.

## SPC Software Requirements

Semiconductor SPC generates large data volumes requiring automated analysis:

- **Data collection**: Automatic feeds from process tools via SECS/GEM protocol (SECS = Semiconductor Equipment Communication Standard, GEM = Generic Equipment Model). Every furnace, etch chamber, and lithography tool reports parameters in real time.
- **Chart generation**: Real-time X-bar/R, p, c charts with automatic control limit calculation and Western Electric rule checking.
- **Alarm management**: Out-of-control triggers routed to process engineers with parameter, rule violated, subgroup data, and recommended response.
- **Cpk tracking**: Running calculations for all critical parameters with trending dashboards by process step, tool, and product.
- **Data storage**: Minimum 2 years retention; 5+ years for critical parameters. Required for capability studies, customer audits, and continuous improvement.

## SPC Implementation Sequence

1. **Identify CTQ parameters** (Critical to Quality): The 20-50 parameters most strongly correlated with yield and reliability.
2. **Validate measurement systems** (Gage R&R): Ensure each CTQ has an adequate measurement system.
3. **Establish baseline capability**: 25-50 subgroups (minimum 125-250 measurements for n=5). Calculate initial control limits and Cpk.
4. **Bring process into control**: Eliminate special causes. Target Cpk ≥ 1.33 on all CTQ parameters.
5. **Maintain and improve**: Ongoing monitoring. Monthly Cpk reviews, quarterly trending, annual process audit.

## Scaling Notes

- **Bench scale (single process)**: One chart, one operator, paper-based charting. Minimum viable SPC for critical dimensions on a single production line.
- **Pilot scale (production line)**: Multiple charts covering key parameters. Dedicated quality technician. Statistical support for chart interpretation.
- **Production scale (factory-wide)**: SPC across all critical processes. Real-time data collection, automated charting. Statistical engineering group providing analysis and improvement recommendations. Six Sigma DMAIC projects for systemic quality issues.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Machine Tools | Basic SPC for dimensional tolerances, gauge R&R for micrometers and calipers |
| Silicon | Wafer-level SPC for crystal growth (pull rate, temperature gradient, rotation) |
| Photolithography | CD control charts, overlay registration SPC, defect density per exposure tool |
| VLSI Scaling | Multi-variate analysis, fault detection and classification (FDC), run-to-run control |
| Electronics | Solder paste volume SPC, placement accuracy, reflow profile monitoring |

## Key Deliverables

- Control chart system for all CTQ parameters
- Cpk ≥ 1.33, trending toward ≥ 1.67
- Gage R&R < 10% for all measurement systems
- Western Electric rule monitoring with alarm system
- SECS/GEM data collection infrastructure
- DMAIC improvement methodology with trained practitioners

## Limitations

- **Data quality dependency**: SPC is only as good as its data. Incomplete data, measurement errors, and sampling bias degrade effectiveness.
- **Lagging indicator**: Charts detect shifts after they occur. Predictive models (run-to-run control, ML-based FDC) supplement SPC but require historical data and computing resources.
- **Subgroup rationality**: Effectiveness depends on rational subgrouping — items within a subgroup should be produced under the same conditions. Mixing tools, shifts, or lots masks shifts.
- **Normality assumption**: X-bar/R charts assume approximately normal data. Non-normal distributions (skewed particle counts, bounded yield) require transformations (log, Box-Cox) or non-parametric methods.
- **Measurement cost**: Every measurement consumes production time. Sampling plans must balance cost against detection sensitivity.

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Frequent OOC signals (>1/20) but yield acceptable | Too few baseline subgroups; high Gage R&R; irrational subgrouping | Recalculate from ≥25 stable subgroups; fix measurement system; restructure subgroups by tool/shift/lot |
| Trend (Rule 5: 6 points trending) | Tool wear, material lot change, controller drift | Check maintenance logs; verify material certification; recalibrate sensors |
| Cpk < 1.33, no OOC on X-bar | Mean shifted toward one spec; specs tightened; R chart shows increased variability | Check both X-bar and R charts; recalculate from last 25 subgroups; compare mean to spec midpoint |
| Gage R&R > 30% | Instrument resolution insufficient; operator inconsistency; environmental effects | Upgrade to 10× finer resolution; standardize measurement procedure; stabilize environment |
| p-chart limits vary wildly | Subgroup sizes vary >20%; p̄ near 0 or 1 | Use standardized p-chart (z-scores); consider c/u chart for low p̄ |
| Rule 7 (15 points in Zone C) | Data rounding; subgrouping across multiple tools; data manipulation | Check recording resolution; restructure subgroups for single tool/stream; audit for selection bias |
| Ppk << Cpk | Between-subgroup variation (batch-to-batch, tool-to-tool) | Decompose by tool, shift, lot using multi-vari; ANOVA to identify outlier tool; tool-specific limits |
| Rule 6 (14 points alternating) | Over-adjustment; two input streams mixed | Stop manual adjustments; split chart by stream (tool/shift/supplier) |
| Cpk nonsensical (negative or >5) | Non-normal data; wrong spec limits; mixing σ types | Test normality (Anderson-Darling); apply Box-Cox transform; verify specs; confirm σ̂ = R̄/d₂ |

## See Also

- [Inspection & Sampling Plans](inspection-sampling.md) — acceptance sampling, AQL, MIL-STD-105E
- [Defect Analysis & Yield Modeling](defect-analysis.md) — Pareto, fishbone, FMEA, yield models
- [Measurement](../measurement/index.md) — metrology instruments and calibration
- [Computing](../computing/index.md) — SPC software and data analysis

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Quality Control](./index.md) • [All Domains](../../index.md)*
