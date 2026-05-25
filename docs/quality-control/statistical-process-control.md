# Statistical Process Control

> **Node ID**: quality-control.spc
> **Domain**: [Quality Control](./index.md)
> **Dependencies**: [`measurement`](../measurement/index.md), [`computing`](../computing/index.md)
> **Timeline**: Years 40-100+
> **Outputs**: spc_charts, cpk_indices, process_capability_analysis, six_sigma_metrics, control_limits

## Problem

Semiconductor manufacturing involves hundreds of sequential process steps, each introducing variability. Without statistical process control, defects accumulate undetected through the process chain, destroying yield. A single out-of-control diffusion furnace can ruin an entire batch of 25 wafers, each containing thousands of die worth tens of thousands of dollars. SPC provides the statistical framework to detect process shifts before they produce scrap, transforming manufacturing from reactive firefighting into proactive quality management.

Semiconductor yield runs 60-90% for mature process nodes but drops below 50% for leading-edge technology. At these yields, the difference between a Cpk of 1.0 and 1.33 can mean the difference between profit and loss on an entire fab. SPC is not optional — it is the operating system of manufacturing quality.

## Control Charts

Control charts are the primary SPC tool. They plot process measurements over time with statistically-derived control limits that distinguish common-cause variation (inherent noise) from special-cause variation (assignable problems requiring correction).

### X-bar and R Charts (Variables Data)

The most widely used control chart pair for continuous measurements (dimensions, temperatures, voltages, weights).

**X-bar chart** monitors the process mean:
- Subgroups of n = 2-10 items sampled at regular intervals (typically n = 5)
- Plot the subgroup mean x̄ for each sampling period
- Center line (CL) = grand mean x̄̄ (average of all subgroup means)
- Upper control limit (UCL) = x̄̄ + A₂ × R̄
- Lower control limit (LCL) = x̄̄ − A₂ × R̄

**R chart** monitors within-subgroup variability:
- Plot the subgroup range R = x_max − x_min for each subgroup
- Center line = R̄ (average range)
- UCL = D₄ × R̄
- LCL = D₃ × R̄

**Control chart constants** (for subgroup size n):

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

The constant d₂ converts the average range to an estimate of process standard deviation: σ̂ = R̄ / d₂. This estimate is critical for process capability calculations.

**Sampling frequency**: For semiconductor manufacturing, subgroups are typically taken every 1-4 hours for critical parameters (furnace temperature, implant dose, etch rate) and every shift for less critical parameters. Each wafer in a batch lot is a natural subgroup member; a lot of 25 wafers provides 5 subgroups of 5.

### p-Chart (Attribute Data — Proportion Defective)

Monitors the fraction of nonconforming items in each subgroup.

- Subgroup size n (typically 50-500 items inspected)
- p = number defective / n for each subgroup
- Center line p̄ = total defective / total inspected
- UCL = p̄ + 3√(p̄(1−p̄)/n)
- LCL = max(0, p̄ − 3√(p̄(1−p̄)/n))

The control limits vary with subgroup size if n changes between samples. When subgroup sizes vary by more than 20%, use standardized p-chart: z_i = (p_i − p̄) / √(p̄(1−p̄)/n_i), with UCL = 3, LCL = −3.

**Application**: Wafer sort yield (fraction of die passing electrical test per wafer), visual defect rate after photolithography steps, packaging defect rate.

### c-Chart (Count of Defects per Unit)

Monitors the number of defects per inspection unit when the opportunity for defects is constant.

- c = count of defects in each inspection unit
- Center line c̄ = average defects per unit
- UCL = c̄ + 3√c̄
- LCL = max(0, c̄ − 3√c̄)

Assumes Poisson distribution. Valid when defect occurrences are independent and the inspection area is constant.

**Application**: Particle count per wafer after cleanroom processing, scratches per panel, voids per solder joint under X-ray inspection.

### u-Chart (Defects per Unit, Variable Area)

Monitors defect density when the inspection area varies between samples.

- u = c / a (defects per unit area)
- Center line ū = total defects / total area
- UCL = ū + 3√(ū/a_i)
- LCL = max(0, ū − 3√(ū/a_i))

Where a_i is the area of the i-th sample.

**Application**: Defects per cm² across different wafer sizes (150 mm vs 200 mm vs 300 mm), contamination per batch with varying lot sizes.

## Western Electric Rules (Out-of-Control Detection)

The Western Electric rules supplement the basic 3-sigma limits by detecting non-random patterns that indicate process shifts, trends, or cycles — even when no point exceeds the 3-sigma limits. These rules are applied to zone-based charts divided into three zones on each side of the center line:

- **Zone A**: Between 2σ and 3σ from the center line
- **Zone B**: Between 1σ and 2σ from the center line
- **Zone C**: Within 1σ of the center line

### Detection Rules

| Rule | Pattern | Interpretation |
|------|---------|----------------|
| Rule 1 | Any single point beyond Zone A (beyond 3σ) | Large sudden shift |
| Rule 2 | 2 out of 3 consecutive points in Zone A (same side) | Moderate shift |
| Rule 3 | 4 out of 5 consecutive points in Zone B (same side) | Small sustained shift |
| Rule 4 | 8 consecutive points on one side of the center line | Process mean drift |
| Rule 5 | 6 consecutive points increasing or decreasing | Trend (tool wear, degradation) |
| Rule 6 | 14 consecutive points alternating up and down | Over-adjustment (stratification) |
| Rule 7 | 15 consecutive points in Zone C (either side) | Too little variation — stratification or data manipulation |

**False alarm rate**: Applying all rules simultaneously yields approximately 1 false alarm per 150 subgroup samples (compared to 1 per 370 for 3-sigma limits alone). The increased sensitivity is worth the occasional false alarm in semiconductor manufacturing where undetected process shifts are extremely costly.

## Process Capability Indices

Process capability compares the natural process spread to the specification limits, quantifying how well a centered, stable process meets requirements.

### Cp (Process Capability)

Measures potential capability — how the process spread relates to specification width, assuming perfect centering.

**Cp = (USL − LSL) / (6σ)**

Where USL = upper specification limit, LSL = lower specification limit, σ = process standard deviation (estimated from R̄/d₂ or from S chart).

A Cp of 1.0 means the process spread exactly fills the specification window (3σ on each side). A Cp of 1.33 means there is room for 4σ between the process mean and each specification limit.

### Cpk (Process Capability — Centered)

Accounts for process centering. The actual capability is limited by the specification limit closest to the process mean.

**Cpk = min[(USL − μ̄) / (3σ), (μ̄ − LSL) / (3σ)]**

Where μ̄ is the process mean. Cpk ≤ Cp always. Cpk = Cp only when the process is perfectly centered between the specification limits.

### Capability Targets

| Cpk Value | Sigma Level | Defect Rate (ppm) | Interpretation |
|-----------|-------------|-------------------|----------------|
| 0.67 | 2σ | 45,500 | Inadequate — process produces ~4.5% defective |
| 1.00 | 3σ | 2,700 | Marginal — barely within specification |
| 1.33 | 4σ | 63 | **Minimum acceptable** for semiconductor manufacturing |
| 1.50 | 4.5σ | 6.8 | Good — suitable for established processes |
| 1.67 | 5σ | 0.57 | Excellent — required for critical dimensions |
| 2.00 | 6σ | 0.002 | Six Sigma — near-zero defect goal |

**Semiconductor Cpk requirements** by process step:

| Process Step | Critical Parameter | Minimum Cpk | Typical Cpk Target |
|-------------|-------------------|-------------|-------------------|
| Gate lithography | CD (critical dimension) | 1.33 | 1.50 |
| Gate etch | Etch bias | 1.33 | 1.50 |
| Implant | Dose uniformity | 1.33 | 1.50 |
| CMP | Oxide thickness | 1.33 | 1.67 |
| Diffusion | Sheet resistance | 1.33 | 1.50 |
| Metal deposition | Thickness | 1.33 | 1.50 |
| Wafer sort | Probe yield | 1.00 | 1.33 |

### Pp and Ppk (Process Performance)

Used for preliminary process assessment or when the process is not yet in statistical control. Uses the overall (total) standard deviation instead of the within-subgroup estimate:

**Pp = (USL − LSL) / (6s_total)**

Where s_total is calculated from all individual measurements (not from R̄/d₂). Pp and Ppk account for both within-subgroup and between-subgroup variation. If Ppk ≈ Cpk, the process is stable. If Ppk << Cpk, significant between-subgroup variation exists (process not centered or drifting).

## Six Sigma Methodology

Six Sigma aims to reduce process variation to achieve defect rates below 3.4 defects per million opportunities (DPMO), corresponding to Cpk ≥ 1.50 with a 1.5σ mean shift assumption.

### DMAIC Cycle

The structured improvement methodology:

1. **Define**: Identify the quality problem, define the project scope and goals, map the process at high level (SIPOC: Supplier-Input-Process-Output-Customer). For semiconductor: define the yield-limiting step, target yield improvement (e.g., "improve gate CD Cpk from 1.10 to 1.50").

2. **Measure**: Collect baseline data. Validate measurement system (Gage R&R study — measurement variation must be <10% of total observed variation). Establish current process capability (Cpk baseline). Create initial control charts.

3. **Analyze**: Identify root causes using statistical tools — hypothesis testing (t-tests, ANOVA), regression analysis, correlation studies, multi-vari charts. Determine which input variables (factors) most strongly influence the output (response). Typical semiconductor analysis: "which of temperature, pressure, gas flow, and time most affects etch rate uniformity?"

4. **Improve**: Design and implement process changes using Design of Experiments (DOE). Full factorial or fractional factorial designs (2^k or 2^(k-p)) systematically vary factors to find optimal settings. Verify improvement with confirmation runs. Target: Cpk improvement of at least 0.33 (from 1.0 to 1.33, or from 1.33 to 1.67).

5. **Control**: Implement SPC on the improved process. Update control limits based on new process capability. Document standard operating procedures (SOPs). Establish response plans for out-of-control conditions. Hand off from improvement team to production team.

### Gage R&R (Repeatability & Reproducibility)

Before any SPC study, validate the measurement system. A Gage R&R study quantifies how much of the observed process variation comes from the measurement system itself.

**Study design**: 10 parts, measured by 3 operators, 2 trials each (10 × 3 × 2 = 60 measurements). Parts should span the expected process range.

**Components of variation**:
- **Repeatability** (equipment variation, EV): Same operator measures same part multiple times. Variation due to instrument resolution and stability.
- **Reproducibility** (appraiser variation, AV): Different operators measure same parts. Variation due to technique differences.
- **Part variation** (PV): True differences between parts — the signal we want to measure.

**Acceptance criteria**:
- Gage R&R < 10% of total variation: **Acceptable** measurement system
- Gage R&R 10-30%: **Marginal** — acceptable depending on application criticality
- Gage R&R > 30%: **Unacceptable** — measurement system must be improved before SPC is meaningful

**Semiconductor-specific**: For critical dimension (CD) measurement, the SEM (Scanning Electron Microscope) or CD-SEM Gage R&R must be <5% because the process tolerances are extremely tight (±2-5 nm on 20-40 nm gate lengths). This requires temperature-controlled metrology rooms and automated measurement routines that minimize operator influence.

## Implementation Requirements

### SPC Software Requirements

SPC in semiconductor manufacturing generates large volumes of data requiring automated analysis:

- **Data collection**: Automatic data feeds from process tools (SECS/GEM protocol in semiconductor fabs — SECS = Semiconductor Equipment Communication Standard, GEM = Generic Equipment Model). Every furnace run, etch chamber, and lithography exposure tool reports process parameters in real time.
- **Chart generation**: Real-time X-bar/R, p, c charts with automatic control limit calculation and Western Electric rule checking.
- **Alarm management**: Out-of-control detection triggers alarms routed to the appropriate process engineer. Alarm includes the parameter, the rule violated, the subgroup data, and the recommended response.
- **Cpk tracking**: Running Cpk calculations for all critical parameters, with trending and automatic reporting. Dashboards showing Cpk by process step, by tool, and by product.
- **Data storage**: Historical data retention for capability studies, customer audits, and continuous improvement. Minimum 2 years of data for most parameters; 5+ years for critical parameters.

### SPC Implementation Sequence

1. **Identify critical parameters** (CTQ — Critical to Quality): Work with product engineering to identify the 20-50 parameters most strongly correlated with yield and reliability. Focus SPC resources on these first.
2. **Validate measurement systems** (Gage R&R): Ensure each CTQ parameter has an adequate measurement system before attempting SPC.
3. **Establish baseline capability**: Collect 25-50 subgroups of data (minimum 125-250 individual measurements for n=5 subgroups). Calculate initial control limits and Cpk.
4. **Bring process into control**: Identify and eliminate special causes. Tighten process to achieve Cpk ≥ 1.33 on all CTQ parameters.
5. **Maintain and improve**: Ongoing monitoring with continuous improvement. Monthly Cpk reviews. Quarterly capability trending. Annual process audit.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Machine Tools | Basic SPC for dimensional tolerances on machined parts, gauge R&R for micrometers and calipers |
| Silicon | Wafer-level SPC for crystal growth parameters (pull rate, temperature gradient, rotation speed) |
| Photolithography | CD control charts, overlay registration SPC, defect density tracking per exposure tool |
| VLSI Scaling | Advanced SPC with multi-variate analysis, fault detection and classification (FDC), run-to-run control |
| Electronics | Solder paste volume SPC, component placement accuracy, reflow profile monitoring |

## Key Deliverables

- Control chart system for all critical process parameters (X-bar/R, p, c as appropriate)
- Cpk ≥ 1.33 for all CTQ parameters, trending toward Cpk ≥ 1.67
- Gage R&R < 10% for all measurement systems used in SPC
- Western Electric rule monitoring with alarm system
- SPC data collection infrastructure (SECS/GEM integration)
- DMAIC improvement methodology with trained practitioners

## Limitations

- **Data quality dependency**: SPC is only as good as its data. Incomplete data, measurement errors, and sampling bias all degrade chart effectiveness. Gage R&R must be validated before any SPC implementation.
- **Lagging indicator**: Control charts detect shifts after they occur, not before. Predictive models (run-to-run control, machine learning-based FDC) supplement SPC but require historical data and computing resources.
- **Subgroup rationality**: Control chart effectiveness depends on rational subgrouping — items within a subgroup should be produced under essentially the same conditions. Incorrect subgrouping (mixing tools, shifts, or material lots within a subgroup) inflates within-subgroup variation and masks between-subgroup shifts.
- **Normality assumption**: X-bar/R charts assume approximately normal data. Semiconductor processes sometimes produce non-normal distributions (skewed particle counts, bounded parameters like yield). Transformations (log, Box-Cox) or non-parametric methods may be needed.
- **Cost of measurement**: Every SPC measurement consumes production time and may require destructive testing. Sampling plans must balance measurement cost against detection sensitivity.

## See Also

- [Inspection & Sampling Plans](inspection-sampling.md) — acceptance sampling, AQL, MIL-STD-105E
- [Defect Analysis & Yield Modeling](defect-analysis.md) — Pareto, fishbone, FMEA, yield models
- [Measurement](../measurement/index.md) — metrology instruments and calibration
- [Computing](../computing/index.md) — SPC software and data analysis

---

*Part of the [Bootciv Tech Tree](../index.md) • [Quality Control](./index.md) • [All Domains](../index.md)*
