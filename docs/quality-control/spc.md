# Statistical Process Control

> **Node ID**: `quality-control.spc`
> **Domain**: [Quality Control](./index.md)
> **Dependencies**: `measurement`, `quality-control`
> **Enables**: [`quality-control.defect-analysis`](./defect-analysis.md)
> **Outputs**: spc_charts, cpk_indices, process_capability_analysis, six_sigma_metrics, control_limits
> **Timeline**: Years 40-100+
> **Critical**: No

## Overview

Statistical Process Control (SPC) is the discipline of using measurement data to detect when a manufacturing process has drifted out of its controlled state, before it produces defective output. Instead of inspecting finished goods and sorting good from bad, SPC samples the process while it runs, plots the measurements on a control chart, and flags statistically improbable variation so the operator can adjust the process immediately. The shift from reactive inspection to proactive control is the single biggest lever a civilization has for raising manufacturing yield after basic machining capability exists.

SPC was formalized by Walter Shewhart at Western Electric in the 1920s. Shewhart's key insight was the distinction between **common-cause variation** (the inherent noise of a stable process, due to many small random sources) and **special-cause variation** (drift, shifts, or anomalies due to a specific assignable cause — tool wear, material batch change, operator error). The control chart is the instrument that tells them apart: a point outside three sigma limits, or a non-random pattern within limits, signals special-cause variation and demands investigation. Roughly 85% of quality problems are common-cause (management / system problems) and 15% are special-cause (operator-level fixable) — a distinction misunderstood by most novice users, who react to common-cause noise as if it were special-cause and make the process worse.

The capability matters because downstream of SPC sits everything that depends on high-yield manufacturing: semiconductor fabrication (where a 1% defect rate compounds across hundreds of process steps to >90% final yield loss), precision machining, chemical process control, and pharmaceutical consistency. Without SPC, a process either runs to generous tolerances (wasting material and performance) or ships a high defect rate (wasting downstream effort). With SPC, a process runs close to its natural capability and the defect rate is measurable and manageable. SPC is the prerequisite for [Defect Analysis](./defect-analysis.md), [Inspection & Sampling](./inspection-sampling.md), and the Six Sigma methodology that dominates modern manufacturing quality.

This article covers the four core control chart types (X̄-R for variables, p-charts and c-charts for attributes), process capability indices (Cp, Cpk, Pp, Ppk) with the ≥1.33 minimum standard, the Western Electric out-of-control detection rules, Gage R&R for measurement system validation, and the step-by-step implementation of an SPC program on a real production line.

## Prerequisites

### Materials

- A measurable process output: continuous variable data (dimensions, weights, temperatures, concentrations) or attribute data (pass/fail, defect counts)
- Calibrated measurement instruments — see [Measurement & Precision Metrology](../measurement/index.md)
- Paper, graph paper, or electronic data logging for charting

### Tools and Equipment

- [Measurement](../measurement/index.md) capability — calipers, micrometers, scales, gauges with resolution at least 10× finer than the tolerance band (the "10:1 rule": if the tolerance is ±0.05 mm, the gauge must resolve to ±0.005 mm or better)
- [Computing](../computing/index.md) capability for large datasets — initially paper and pencil suffice; electronic spreadsheets or dedicated SPC software take over at high part volumes
- Sampling containers, gauge fixtures, or sample transport kits to bring parts to the measurement station consistently
- Control chart forms (pre-printed with the 3σ limit lines) or plotting software

### Knowledge

- Descriptive statistics: mean (X̄), range (R), standard deviation (σ or s). The standard deviation is the root-mean-square deviation of individual values from the mean; for a normal distribution, ~99.73% of values fall within ±3σ.
- The normal distribution and the Central Limit Theorem — sample means are approximately normal even when individuals are not, provided the sample size n ≥ 4. This is why X̄-charts work on non-normal processes.
- Distinction between common-cause and special-cause variation — the core conceptual hurdle. Reacting to common-cause variation as if it were special-cause (tampering) increases variation by ~40% per Deming's funnel experiment.
- Probability concepts for the control limits: 3σ limits give a false-alarm rate of ~0.27% (one point in 370 outside limits by chance alone on a stable process).

### Infrastructure

- A production line running at measurable rate (≥100 units/hour for meaningful subgroups)
- Time and authority for operators to stop the process and investigate when a chart signals
- Calibration system for measurement instruments (gauge R&R, periodic recalibration)

## Bill of Materials

BOM for implementing SPC on a single critical dimension of a machined part (e.g., shaft diameter, target Ø10.000 ±0.020 mm).

| Material / Resource | Quantity per process control loop | Source | Alternatives |
|---------------------|-----------------------------------|--------|--------------|
| Calibrated digital caliper (0.001 mm resolution) | 1 per measurement station | [Measurement](../measurement/index.md) | Micrometer (more accurate, slower); gauge fixture with dial indicator (faster, fixed dimension) |
| Steel reference gauge blocks (Grade 0, ±0.05 µm) | 1 set (9-112 pieces) | [Machine Tools](../machine-tools/machining.md) precision grinding | Calibration-grade ring gauges (single-point check) |
| Control chart forms (pre-printed, A3 pads) | ~50 charts per part per year | Paper + printing | Electronic SPC software (requires [Computing](../computing/index.md)); whiteboard + manual plot |
| Sampling tray / parts tote | 1 per station | [Polymers](../polymers/index.md) molded tray | Cloth-lined basket; labeled cardboard box |
- | Operator time per subgroup sample | 5-10 min per subgroup of n=5 parts | Labor | Automated in-line gauging (eliminates operator sampling time, high capital cost) |
| Calibration standard reference part | 1 per part family, measured to ±0.001 mm | [Measurement](../measurement/index.md) metrology lab | Gauge blocks of equivalent dimension |
| Training materials (Shewhart rules, chart plotting) | 4-8 hours per operator | [Knowledge](../knowledge/index.md) documentation | On-the-job mentoring by quality engineer |

## Process Description

### Step-by-Step: Implementing X̄-R Control Charts on a Production Line

1. **Select the critical characteristic.** Choose the dimension or property most strongly correlated with product function (e.g., shaft diameter for fit, tensile strength for a load-bearing part). If multiple characteristics matter, start with the one most often out of tolerance historically.

2. **Choose the subgroup size and sampling frequency.** For variables data, subgroup size n = 4 to 5 is standard. Smaller subgroups (n=2-3) detect large shifts faster; larger (n=8-10) detect small shifts but cost more sampling time. Frequency depends on production rate and the speed of drift: typically every 30 min to 2 hours for machining, every 15-30 min for high-volume stamping. Rule of thumb: sample often enough that a process shift is caught before many defective parts are made between samples.

3. **Collect 20-30 subgroups of initial data (~100-150 measurements).** This is the baseline period used to compute the control limits. The process must be running stably during this period — if it is not, identify and remove special causes first.

4. **Compute the subgroup means (X̄) and ranges (R).** For each subgroup, X̄ = (x₁+x₂+...+xₙ)/n. R = max(x) − min(x) within the subgroup. Record on the chart form.

5. **Compute the grand mean (X̄̄) and average range (R̄).** X̄̄ = mean of all subgroup means. R̄ = mean of all subgroup ranges. These are the centerlines of the X̄ and R charts respectively.

6. **Calculate the control limits using Shewhart constants.** The limits are NOT ±3σ of individuals; they are ±3σ of the subgroup means, computed from the average range via:
   - Upper Control Limit (X̄ chart): UCL = X̄̄ + A₂·R̄
   - Lower Control Limit (X̄ chart): LCL = X̄̄ − A₂·R̄
   - Upper Control Limit (R chart): UCL = D₄·R̄
   - Lower Control Limit (R chart): LCL = D₃·R̄

   Shewhart constants for common subgroup sizes (n=4: A₂=0.729, D₃=0, D₄=2.282; n=5: A₂=0.577, D₃=0, D₄=2.114; n=10: A₂=0.308, D₃=0.223, D₄=1.777).

7. **Draw the centerlines and control limits on the chart.** Plot the initial 20-30 subgroup means and ranges. Any point outside the limits, or any Western Electric rule violation (see below), indicates the baseline was not stable — investigate, fix, and re-collect the baseline.

8. **Continue plotting subsequent subgroups in real time.** The operator plots each new subgroup's X̄ and R on the chart as the line runs. The chart is a living document, displayed at the workstation.

9. **Respond to signals, not noise.** When a point falls outside the limits OR a Western Electric rule triggers, STOP the process and investigate. Look for assignable causes: tool wear, material batch change, coolant temperature drift, fixture loosening, operator technique shift. Do NOT adjust the process for points that are within limits and show no pattern — that is tampering with a stable process and will increase variation.

10. **Recompute limits periodically.** Control limits describe the process's recent stable performance, not the specification. After process improvements (new tooling, method change), collect a new baseline and recompute. A common error is to leave stale limits in place long after the process has improved.

### Attribute Charts: p-Charts and c-Charts

When the measured output is pass/fail or a defect count, attribute charts apply:

- **p-chart (fraction defective):** Tracks the proportion of defective units in each subgroup. Subgroup size n = 50-500 parts (must be large enough that ≥1 defect is expected; if defect rate is 1%, n ≥ 500). Control limits: UCL = p̄ + 3·√(p̄(1−p̄)/n), LCL = p̄ − 3·√(p̄(1−p̄)/n), where p̄ is the average fraction defective. Used for visual inspection pass/fail data.
- **c-chart (defect count per unit):** Tracks the count of defects per inspected unit (e.g., scratches per panel, bubbles per glass sheet). Assumes a Poisson distribution. Control limits: UCL = c̄ + 3·√c̄, LCL = c̄ − 3·√c̄, where c̄ is the average defect count per unit. Used when a unit can have multiple defects and still pass.

## Quantitative Parameters

### X̄-R Chart Constants and Sample Sizes

| Subgroup size n | A₂ (X̄ limits) | D₃ (R LCL) | D₄ (R UCL) | d₂ (σ estimator) | Detects shift of 1σ in | Detects shift of 2σ in |
|-----------------|---------------|------------|------------|-------------------|------------------------|------------------------|
| 2 | 1.880 | 0 | 3.267 | 1.128 | ~5 samples | ~1.5 samples |
| 3 | 1.023 | 0 | 2.574 | 1.693 | ~3 samples | ~1 sample |
| 4 | 0.729 | 0 | 2.282 | 2.059 | ~2 samples | ~1 sample |
| 5 | 0.577 | 0 | 2.114 | 2.326 | ~2 samples | ~1 sample |
| 10 | 0.308 | 0.223 | 1.777 | 3.078 | ~1 sample | <1 sample |

### Process Capability Indices

| Index | Formula | Interpretation | Minimum acceptable |
|-------|---------|----------------|--------------------|
| Cp (capability) | (USL − LSL) / (6σ̂) | Process spread vs. tolerance spread; assumes centered process | ≥1.33 |
| Cpk (capability, centered) | min(USL−X̄̄, X̄̄−LSL) / (3σ̂) | Actual capability accounting for mean offset from target | ≥1.33 (≥1.67 for critical / safety dimensions) |
| Pp (performance) | (USL − LSL) / (6s) | Uses long-term standard deviation s (all individual data) | ≥1.33 |
| Ppk (performance, centered) | min(USL−X̄, X̄−LSL) / (3s) | Long-term performance including drift | ≥1.33 |

Where USL/LSL = upper/lower specification limits, σ̂ = R̄/d₂ (short-term, within-subgroup standard deviation), s = standard deviation of all individual measurements (long-term).

Cpk translates directly to defect rate (one-sided, assuming normal distribution): Cpk 1.00 → 0.135% defective (1,350 ppm); Cpk 1.33 → 0.0032% (32 ppm); Cpk 1.67 → 0.000006% (0.06 ppm); Cpk 2.00 → 0.0000001% (Six Sigma, accounting for 1.5σ long-term shift → 3.4 ppm).

### Western Electric Out-of-Control Rules

Applied to points within the 3σ control limits; any one rule triggering signals a probable special cause.

| Rule | Pattern | Probability on stable process | Typical cause |
|------|---------|-------------------------------|---------------|
| Rule 1 | Any single point beyond 3σ (outside UCL or LCL) | 0.27% | Large sudden shift (broken tool, missing operation) |
| Rule 2 | 2 of 3 consecutive points beyond 2σ (same side) | 0.35% | Moderate process shift |
| Rule 3 | 4 of 5 consecutive points beyond 1σ (same side) | 0.45% | Small sustained shift (gradual wear, temperature drift) |
| Rule 4 | 8 consecutive points on one side of centerline | 0.39% | Mean shift, new material batch |
| Rule 5 | 6 consecutive points steadily increasing or decreasing | Rare | Tool wear, drift, progressive fixture loosening |
| Rule 6 | 14 consecutive points alternating up and down | Rare | Two alternating machines / operators / fixtures |
| Rule 7 | 15 consecutive points within 1σ (hugging centerline) | Rare | Reduced variability (improvement) OR stratified sampling from different populations |
| Rule 8 | 8 consecutive points beyond 1σ (both sides) | Rare | Bimodal distribution — mixture of two processes |

## Scaling Notes

- **Single-station SPC (1 process, 1 characteristic):** Paper chart at the workstation, operator samples n=5 every 30-60 min. Minimum investment: caliper + chart forms. Suitable for any shop with ≥1 trained operator. Catches >90% of significant shifts within 2-3 subgroups.

- **Multi-station SPC (5-50 characteristics across a line):** Electronic data collection at each station; a quality technician reviews charts daily. Software computes limits and flags violations automatically. Requires [Computing](../computing/index.md) infrastructure. Sample frequency set so a shift is detected before >50 defective parts accumulate between samples.

- **Plant-wide SPC (100+ characteristics):** Networked gauges feed a central database. Real-time dashboards flag out-of-control conditions to supervisors. Capability indices tracked monthly; process improvement projects prioritized by lowest Cpk. This is the entry point for Six Sigma DMAIC (Define, Measure, Analyze, Improve, Control) methodology.

- **Minimum economic scale:** SPC on a single critical characteristic of a single product pays for itself if it catches even one batch of defects per year that would otherwise ship. The cost of 5 minutes operator time per subgroup is trivial compared to the cost of scrap, rework, or warranty claims.

- **Non-linear scaling:** A process with Cpk 1.0 has a defect rate ~2,700 ppm (combined both tails). Doubling Cpk to 2.0 reduces defects to ~0.002 ppm — a million-fold improvement. The first jump (1.0 → 1.33) cuts defects by ~85×. The effort to improve Cpk grows roughly with the square of the target — going from 1.33 to 1.67 typically costs 2-3× the engineering effort of going from 1.00 to 1.33.

- **Bottleneck:** Measurement system capability (Gage R&R) limits SPC. If the gauge contributes ≥30% of the observed variation, the chart measures gauge noise more than process variation. A Gage R&R below 10% of tolerance is required for meaningful SPC; 10-30% is marginal; >30% means the gauge must be improved before SPC can work.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Many points outside control limits (frequent false alarms) | Control limits too tight (computed from too few subgroups or non-stable baseline), OR gauge resolution insufficient, OR process genuinely unstable | Recompute limits from 20-30 stable subgroups; verify gauge resolution ≤1/10 of tolerance; investigate and remove special causes before recomputing baseline |
| No points outside limits for many subgroups (chart "too quiet") | Process improved since limits were set; OR limits too wide (subgroup size too small to detect real shifts); OR stratification — sampling from different populations averages out real variation | Recompute limits from recent data; increase subgroup size n; ensure all samples in a subgroup come from the same process within a short time window |
| R-chart out of control but X̄-chart stable | Change in process variability — different material batch, worn bearing, loose fixture, inconsistent operator technique | Investigate variability source: check material certificates, bearing preload, fixture clamp force; train operator on consistent technique |
| X̄-chart shows steady upward/downward trend | Tool wear, thermal drift, fixture creep, material uniformity drift | Add periodic tool offset compensation (recurring adjustment every N parts); install temperature compensation on precision measurement; tighten fixture maintenance schedule |
| Gauge R&R >30% of tolerance | Gauge worn, uncalibrated, or inadequate resolution; fixture does not locate part repeatably; operator technique varies | Recalibrate gauge against reference standard; replace gauge with higher-resolution unit; redesign fixture for better locating repeatability; train operators with gauge handling protocol |
| Cpk acceptable but customer reports field failures | Specification limits wrong (do not capture real functional requirement); OR process mean offset from target even though within spec; OR long-term drift not captured by short-term Cpk | Review specification derivation; target the process mean to nominal (not just within spec); monitor Ppk (long-term) alongside Cpk (short-term); apply 1.5σ shift factor for field prediction |
| C-chart lower control limit negative | c̄ < 9 (average defect count too low for c-chart to have a meaningful LCL) | Set LCL = 0 (defect counts cannot be negative); consider u-chart (defects per unit area) if inspection unit varies; or accept that low-defect processes cannot detect decreases |
| Operators stop responding to chart signals | Too many false alarms (tampering fatigue), OR no authority to act on signals, OR signals are ignored by management | Reduce false-alarm rate (Western Electric rules are stricter than 3σ alone — pick a subset); empower operators to stop the line; visibly act on the first few signals so operators see the system works |
| Chart shows regular cycles (daily, weekly) | Temperature / humidity swings, shift changes, material delivery cycles, operator fatigue | Plot time-of-day on the chart x-axis to expose cycles; install environmental control; standardize shift handoff procedure |

## Safety

SPC is a data and paper activity; direct physical hazards are minimal. The relevant risks are:

- **Misinterpretation hazard (process safety):** Acting on common-cause variation as if it were special-cause (tampering) increases process variation by ~40% (Deming funnel experiment). Operators and engineers must understand the distinction before being given chart authority. Training certification is mandatory.
- **Gauge-handling hazards:** Precision measurement instruments (micrometers, gauge blocks) are delicate steel. Sharp edges on caliper jaws and gauge block wringing burrs can cut skin. Heavy steel reference parts can drop on feet. Use gloves when handling gauge block stacks; keep measuring stations clear of clutter.
- **Statistical overconfidence:** A Cpk of 1.33 means 32 ppm defects expected — not zero. For safety-critical characteristics (aircraft fasteners, medical implants, pressure vessel welds), target Cpk ≥1.67 and add 100% inspection for the critical characteristic, not just sampling.
- **Stop-authority hazard:** If an operator is empowered to stop the line on a chart signal, ensure there is a defined escalation path — repeatedly stopping the line without investigation burns production time and erodes trust in the system. Define maximum stops per shift before engineering介入.

### Personal Protective Equipment

- Standard shop PPE (safety glasses, steel-toe boots) when entering the production area to sample parts
- Cotton gloves when handling gauge blocks (prevents rust from fingerprints and skin oils)

## Quality Control

### Acceptance Criteria for the SPC System Itself

- **Gage R&R:** ≤10% of tolerance (acceptable); 10-30% (marginal, may be acceptable for non-critical characteristics); >30% (unacceptable — gauge must be improved before SPC data is trusted).
- **Control chart coverage:** 100% of critical-to-quality (CTQ) characteristics have active control charts.
- **Response time:** Out-of-control signals are investigated within one subgroup interval (≤1 hour for machining, ≤30 min for high-volume production).
- **Capability reporting:** Cpk calculated and reported for every CTQ characteristic at least monthly.

### Testing Methods

- **Gage R&R study (ANSI/ASQ Z1.9 / AIAG MSA):** 10 parts, 3 operators, 3 trials each (90 measurements total). Decomposes total observed variation into part-to-part (real process variation), repeatability (same operator, same part), and reproducibility (operator-to-operator). Total Gage R&R % = √(repeatability² + reproducibility²) / tolerance × 100.
- **Measurement system bias check:** Measure a reference standard 10+ times; compare mean to certified value. Bias should be ≤5% of tolerance.
- **Stability check:** Plot measurements of the same reference standard on an X̄-R chart over days/weeks; confirms the measurement system itself is stable.
- **Linearity check:** Measure 5+ reference standards spanning the operating range; bias should not vary significantly with magnitude.

### Sampling Procedure

- Subgroup = n consecutive parts (n=4-5 for variables) taken from the process within a short window (≤15 min for machining). NOT random samples from a bin of accumulated parts — that destroys the time-ordering that makes control charts work.
- Subgroup interval set by drift rate: if tool wear causes a 0.01 mm shift per hour and tolerance is ±0.05 mm, sample at least every 30 min.
- Attribute sampling: inspect n=50-500 parts per subgroup; compute p (fraction defective) or c (defects per unit).

## Variations and Alternatives

- **Shewhart X̄-R charts (default):** The standard variables charts. Simple, robust, detect large shifts (≥1.5σ) quickly. Weak at detecting small sustained shifts (<1.5σ). Covered above as the baseline method.
- **Individuals and Moving Range (I-MR) chart:** For processes where subgroup sampling is impossible (one batch per day, chemical batch processes). Charts individual measurements and the moving range (|xᵢ − xᵢ₋₁|). Less sensitive than X̄-R but applicable where subgroups do not exist.
- **Cumulative Sum (CUSUM) chart:** Plots the cumulative sum of deviations from target. Detects small sustained shifts (0.5-1.5σ) much faster than Shewhart charts. More complex to compute and interpret; requires a trained user.
- **Exponentially Weighted Moving Average (EWMA) chart:** Weights recent data more heavily than old. Tunable sensitivity to small shifts. Common in chemical and semiconductor processes where gradual drift dominates.
- **Pre-control chart:** Simplified chart that divides the tolerance band into green / yellow / red zones. Operators respond to color changes; no statistical limits to compute. Faster to deploy in low-skill environments; less statistically rigorous.
- **Six Sigma DMAIC:** The full methodology (Define, Measure, Analyze, Improve, Control) that wraps SPC in a project-management framework. Targets Cpk ≥2.0 (Six Sigma, 3.4 ppm defective accounting for long-term drift). Requires [Computing](../computing/index.md) and trained statisticians.
- **Acceptance sampling (ANSI/ASQ Z1.4):** A non-SPC alternative — inspect a random sample of a finished lot, accept or reject the lot based on the defect count found. Cheaper than 100% inspection, but reactive (finds defects after they are made, does not prevent them). Use when SPC is not feasible (low-volume, batch chemical, supplier inspection). See [Inspection & Sampling](./inspection-sampling.md).

### Trade-off Comparison

| Method | Detects small shifts | Detects large shifts | Complexity | Best for |
|--------|---------------------|----------------------|------------|----------|
| Shewhart X̄-R | Slow | Fast | Low | General machining, default choice |
| I-MR | Slow | Medium | Low | Low-volume, batch processes |
| CUSUM | Fast | Medium | Medium | Chemical, precision processes |
| EWMA | Fast | Medium | Medium | Semiconductor, gradual drift |
| Pre-control | Medium | Fast | Very low | Low-skill deployment, quick setup |
| Acceptance sampling | Does not detect (lot-level) | N/A | Low | Incoming inspection, supplier lots |

## References

- [Quality Control Domain](./index.md) — overview of QC capabilities
- [Defect Analysis](./defect-analysis.md) — downstream capability for root-cause analysis of defects found by SPC
- [Inspection & Sampling](./inspection-sampling.md) — sampling standards (ANSI/ASQ Z1.4), measurement system analysis, gauge R&R
- [Measurement & Precision Metrology](../measurement/index.md) — calibrated measurement instruments prerequisite for SPC
- [Computing](../computing/index.md) — required for electronic SPC data collection and large-dataset analysis
- [Statistical Process Control (overview)](./statistical-process-control.md) — companion overview article covering the same topic at a conceptual level

---
*Part of the [Bootciv Tech Tree](../index.md) • [Quality Control](./index.md) • [All Domains](../index.md)*
