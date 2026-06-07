# Statistical Process Control

> **Node ID**: quality-control.spc
> **Domain**: [Quality-Control](./index.md)
> **Dependencies**: [`Defect Analysis & Yield Modeling`](defect-analysis.md)
> **Enables**: [`Quality Control & Statistical Process Control`](quality-control.md), [`Measurement & Instrumentation`](measurement.md)
> **Timeline**: Years 40-100+
> **Outputs**: spc_charts, cpk_indices, process_capability_analysis, six_sigma_metrics, control_limits
> **Critical**: No

## Overview

Control charts (X-bar/R for variables, p and c charts for attributes), process capability analysis (Cpk/Ppk with target ≥1.33 minimum, ≥1.67 for critical dimensions), Western Electric out-of-control detection rules, Six Sigma DMAIC methodology, and Gage R&R measurement system validation. The operating system of manufacturing quality — transforms reactive firefighting into proactive defect prevention.

This technology is characteristic of the Semiconductor era of industrial development. It builds on earlier foundational techniques while enabling more precise and controlled manufacturing outcomes.

Primary outputs: `spc_charts`, `cpk_indices`, `process_capability_analysis`, `six_sigma_metrics`, `control_limits`. These materials or products serve as inputs for downstream manufacturing and processing steps.

Statistical process control answers a fundamental manufacturing question: "Is this process producing consistent output, or has something changed?" By sampling process output over time and plotting the results on control charts, operators can distinguish between normal random variation (common cause) and abnormal shifts (special cause). Reacting to common cause variation wastes effort; ignoring special cause variation produces defects. SPC provides the statistical framework to tell the difference.

Without SPC, manufacturing quality relies on 100% inspection (expensive and imperfect — inspectors miss defects) or on hope (no methodology at all). SPC replaces both with a statistical system that detects problems early, before defective products accumulate. The cost of implementing SPC is training and data collection; the cost of not implementing it is scrap, rework, warranty claims, and customer defection.

The transition from "inspect quality in" (inspect every part and discard bad ones) to "build quality in" (control the process so bad parts are never produced) is one of the most consequential shifts in manufacturing philosophy. SPC is the mathematical tool that makes this transition possible.

## Prerequisites

### Materials

- **Data collection forms**: Pre-printed control chart forms with scales, gridlines, and spaces for recording measurements, dates, and operator identification.
- **Measurement instruments**: Calibrated gauges, micrometers, scales, or instruments appropriate to the characteristic being charted. Instrument resolution must be at least 10× finer than the tolerance being controlled.
- **Reference standards**: Gauge blocks, reference weights, or calibration artifacts for verifying measurement instrument accuracy before each data collection session.

### Equipment

- **Measurement instruments**: Micrometers, calipers, gauges, scales, hardness testers, or any instrument appropriate to the measured characteristic. All instruments must be in calibration.
- **Data recording**: Paper chart forms or electronic data collection terminals. Electronic collection eliminates transcription errors and enables automated charting.
- **Calculator or computer**: For computing control limits, capability indices, and performing Gage R&R calculations. Statistical software packages automate these computations.
- **Gauge blocks and reference standards**: For verifying instrument calibration at the point of use.
- [Defect Analysis & Yield Modeling](defect-analysis.md) — tool dependency

### Knowledge

- Understanding of statistical distributions (normal distribution, binomial, Poisson) and which applies to each data type
- Familiarity with control chart construction and interpretation — how to calculate control limits and recognize out-of-control patterns
- Ability to perform Gage R&R studies and interpret the results
- Understanding of process capability indices (Cp, Cpk, Ppk) and their relationship to defect rates
- Training in the specific measurement instruments used for data collection

### Infrastructure

- **Data collection stations**: Located at the point of production. Operators must be able to measure, record, and chart data without leaving their work area.
- **Calibration laboratory**: For maintaining measurement instrument accuracy. Reference standards traceable to national standards.
- **Statistical support**: Access to a statistical engineer or quality engineer who can help with chart selection, control limit calculation, capability studies, and investigation of out-of-control conditions.
- **Records storage**: Organized filing system for quality records. SPC data must be retained for trend analysis and audit purposes.

## Process Description

SPC implementation involves selecting the appropriate control chart for the data type, collecting samples at defined intervals, plotting the results, and interpreting the chart patterns to detect process shifts. The methodology transforms raw measurement data into actionable process intelligence.

### Step-by-Step Procedure

1. **Select the quality characteristic**: Identify the measurable parameter that most directly indicates process performance. For machining: a critical dimension. For chemical processing: a concentration or purity. For assembly: a defect count.
2. **Choose the control chart type**: Match the chart to the data. Variables data (continuous measurements) use X-bar/R or X-bar/S charts. Attributes data (counts of defects) use p charts (proportion defective), np charts (number defective), c charts (count of defects per unit), or u charts (defects per unit of varying size).
3. **Collect baseline data**: Gather 20-30 subgroups of data (typically 4-5 measurements per subgroup for X-bar/R charts) from a process running under normal conditions. This establishes the process's natural variation.
4. **Calculate control limits**: Compute the center line (process mean), upper control limit (UCL), and lower control limit (LCL) from the baseline data. These limits represent the expected range of variation for a stable process — not specification limits, which define what the customer requires.
5. **Plot ongoing samples**: At defined intervals, collect a subgroup, compute the subgroup statistic (mean, range, proportion), and plot the point on the chart.
6. **Interpret the chart**: Apply detection rules to identify out-of-control conditions. The basic rule: a single point beyond the control limits. Western Electric rules add pattern detection: 2 of 3 points beyond 2-sigma, 4 of 5 points beyond 1-sigma, 8 consecutive points on one side of the center line, 6 consecutive points trending up or down.
7. **Investigate and act**: When an out-of-control signal is detected, investigate the cause. If special cause is found, correct it. If no special cause is found, the process may have shifted — recalculate control limits from recent data.

### Control Chart Types

| Chart | Data Type | Subgroup Statistic | Application |
|-------|----------|-------------------|-------------|
| X-bar/R | Variables (continuous) | Mean and range | Machining dimensions, weight, temperature |
| X-bar/S | Variables (continuous) | Mean and standard deviation | Large subgroups (n > 10) |
| p chart | Attributes (pass/fail) | Proportion defective | Assembly yields, inspection results |
| c chart | Attributes (count) | Count of defects per unit | Surface defects, imperfections per part |
| u chart | Attributes (count) | Defects per unit area/volume | Defect density on wafers, fabric |

### Process Capability Analysis

Process capability compares the natural spread of the process (6 sigma) to the specification tolerance:

- **Cp** = (USL - LSL) / (6σ): Measures potential capability — how wide the process spread is relative to the tolerance. Cp ≥ 1.33 is the minimum for capable processes.
- **Cpk** = min((USL - μ) / 3σ, (μ - LSL) / 3σ): Measures actual capability, accounting for process centering. Cpk ≤ Cp always. A process with Cpk = 1.33 produces about 6 defects per million opportunities.
- **Ppk** (preliminary process capability): Used during initial process qualification before long-term data is available. Same formula as Cpk but calculated from a shorter data set.

A process with Cpk < 1.0 is producing output outside specification limits. The process must be improved (reduce variation) or the specifications must be widened (if technically acceptable).

### Implementation Approach

Implementing SPC in a manufacturing operation follows a standard sequence:

1. **Identify critical parameters**: Which measurements most directly affect product performance? Start with the top 3-5 critical dimensions or characteristics.
2. **Validate the measurement system**: Perform a Gage R&R study before collecting any SPC data. If the measurement system cannot reliably distinguish between parts, the SPC data is meaningless.
3. **Establish baseline capability**: Collect data from a stable process. Calculate control limits. Determine initial Cpk.
4. **Deploy control charts at the point of production**: Operators maintain their own charts. The data must be current — yesterday's chart tells you yesterday's news.
5. **Train operators in chart interpretation**: Every operator must know the basic out-of-control rules and must know to stop production and call for investigation when a signal appears.
6. **Drive continuous improvement**: Use capability data to prioritize process improvement efforts. Low Cpk = high priority for variation reduction.

### Gage R&R Method

A Gage R&R (Repeatability and Reproducibility) study determines how much of the observed measurement variation comes from the measurement system itself:

- **Repeatability** (equipment variation): The same operator measures the same part multiple times. Variation between readings indicates instrument precision.
- **Reproducibility** (operator variation): Different operators measure the same parts. Variation between operators indicates differences in technique.
- **Study design**: Typically 10 parts × 3 operators × 3 trials = 90 measurements. Parts should span the expected range of variation.
- **Acceptance criteria**: Total Gage R&R should be less than 10% of total observed variation for critical measurements. 10-30% is conditionally acceptable. Above 30% is unacceptable — the measurement system cannot adequately distinguish between good and bad parts.

## Safety Considerations

This process involves specific hazards requiring trained personnel and protective measures:

- **Ergonomic strain**: Repetitive measurement tasks (hundreds of measurements per shift) cause hand and wrist strain. Vary measurement tasks; use ergonomically designed instruments.
- **Chemical exposure**: Some measurement processes involve contact with process chemicals or cleaning solvents. Use appropriate PPE.
- **Electrical hazards**: Electronic measurement instruments and data terminals carry electrical risk. Ensure proper grounding and maintenance.
- **Eye strain**: Visual inspection under magnification or in poor lighting. Ensure adequate task lighting and regular breaks.

### Personal Protective Equipment

- Safety glasses when using measurement instruments near production machinery
- Appropriate gloves when handling parts with sharp edges or chemical residues
- Respiratory protection when measuring in areas with chemical fumes or dust
- Hearing protection in noisy production environments
- Anti-static wrist strap when handling electronic measurement instruments

### Emergency Procedures

- Maintain first aid kit appropriate to the production environment where measurements are taken.
- Know locations of emergency shutoffs for any powered measurement equipment.
- Establish clear procedures for responding to out-of-control signals during emergency production situations — SPC should not be suspended during crises, as that is when defective output is most costly.
- Train all personnel on data integrity — falsifying SPC data is a serious quality system violation that can have safety consequences downstream.

## Quality Control

### Acceptance Criteria

- **SPC Charts**: Control limits correctly calculated from baseline data. All plotted points visible. Chart annotations include date, operator, and any special events.
- **Cpk Indices**: Calculated from sufficient data (minimum 30 subgroups). Confidence interval reported alongside point estimate.
- **Process Capability Analysis**: Includes both Cp and Cpk. Process stability verified before capability calculation — capability indices are meaningless if the process is not in statistical control.
- **Six Sigma Metrics**: DPMO (defects per million opportunities) calculated from actual defect data. Sigma level correctly derived from DPMO tables.

### Testing Methods

- **Gage R&R study**: Quantify measurement system variation before relying on SPC data. If the measurement system contributes more than 10% of total observed variation, the measurement system must be improved before SPC can be meaningful. A Gage R&R study uses multiple operators measuring the same parts multiple times to decompose total variation into repeatability (same operator, same part) and reproducibility (different operators).
- **Control chart audit**: Review charts weekly to verify they are being maintained and interpreted correctly. Charts that are not being used in real time provide no value.
- **Process audit**: Verify that out-of-control signals are being investigated and that corrective actions are documented and effective.

### Sampling Protocol

- Define sampling frequency based on process stability and production rate. Stable processes can be sampled less frequently; unstable or critical processes require continuous monitoring.
- Use rational subgroups — samples taken close together in time, representing the same process conditions. Subgroups that span shift changes, material changes, or setup changes mask rather than reveal variation.
- Record all measurements for trend analysis. Even when points are within control limits, trends and patterns provide early warning of developing problems.
- Reject and investigate any out-of-control signals immediately. The control chart is only valuable if signals trigger prompt investigation and corrective action.
- Maintain measurement logs: instrument identification, calibration date, and operator name for each data collection session.

## Scaling Notes

Transitioning from bench-scale to production involves these considerations:

- **Bench scale (single process)**: One control chart, one operator. Paper-based charting. The minimum viable SPC implementation. Suitable for critical dimensions on a single production line.
- **Pilot scale (production line)**: Multiple control charts covering key parameters across a production line. Dedicated quality technician maintaining charts and performing Gage R&R studies. Statistical support for chart interpretation.
- **Production scale (factory-wide)**: SPC applied across all critical processes. Real-time data collection. Automated charting. Statistical engineering group providing analysis, capability studies, and process improvement recommendations. Six Sigma DMAIC projects for systemic quality issues.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Too many false alarms on control chart | Control limits calculated incorrectly or subgroup size too small | Recalculate limits from stable baseline; increase subgroup size |
| Process shifts detected too late | Sampling interval too long or subgroup size insufficient | Sample more frequently; verify chart sensitivity |
| Cpk below 1.0 but no out-of-control signals | Process variation naturally exceeds tolerance | Reduce process variation (improve capability), or widen specification if technically justified |
| Gage R&R exceeds 30% | Measurement instrument inadequate or operators inconsistent | Improve measurement method; retrain operators; replace instrument |
| Charts not maintained in real time | Operators not trained or not given time | Make charting part of the standard work procedure; train all operators |
| Capability study shows unstable process | Multiple process streams mixed in one dataset | Stratify data by machine, operator, material lot, or shift; study each stream separately |

## Variations and Alternatives

- **Shewhart control charts (standard)**: The baseline method. X-bar/R, p, and c charts. Detects large shifts (≥1.5 sigma) reliably. Simple to implement and understand. The starting point for any SPC program.
- **CUSUM and EWMA charts**: Detect small, persistent shifts that Shewhart charts miss. Cumulative sum (CUSUM) charts accumulate deviations from target; exponentially weighted moving average (EWMA) charts weight recent data more heavily. More complex to implement but more sensitive to gradual drifts. Used for critical parameters where early detection of small shifts matters (semiconductor manufacturing, pharmaceutical production).
- **Pre-control**: A simplified method using specification zones rather than statistical control limits. Easier to implement than full SPC but less rigorous. Useful as a stepping stone or for low-volume production where insufficient data exists for control limit calculation.
- **Six Sigma DMAIC**: A project-based improvement methodology (Define, Measure, Analyze, Improve, Control) that uses SPC tools within a structured problem-solving framework. Suitable for systemic quality problems that require cross-functional investigation.

## References

- [Quality Control & Statistical Process Control](quality-control.md) — parent capability
- [Quality-Control Domain](./index.md) — domain overview and related capabilities
- [Defect Analysis & Yield Modeling](defect-analysis.md) — upstream dependency (tool)
- [Quality Control & Statistical Process Control](quality-control.md) — downstream capability
- [Measurement & Instrumentation](measurement.md) — downstream capability

SPC connects to every manufacturing domain in the tech tree. Any process that produces measurable output can benefit from SPC. The semiconductor industry was the primary driver of modern SPC methodology — with defect tolerances measured in parts per billion, statistical control of process variation is not optional but existential. The same principles apply at lower technology levels, where they provide the difference between artisanal inconsistency and reliable production.

Proper handling of input materials and products is essential for consistent results:

- Store SPC data (chart records, capability studies, Gage R&R reports) in an organized filing system. These are quality records that may be required for audits and process investigations.
- Use FIFO (first-in, first-out) inventory management for measurement standards and calibration reference materials.
- Label all inspection records with date, operator, lot number, and process conditions.
- Inspect measurement instruments before each use — verify calibration status and zero setting.
- Segregate non-conforming material identified by SPC alerts. Do not return it to the production flow without documented disposition.

---

*Part of the [Bootciv Tech Tree](../index.md) · [Quality-Control](./index.md) · [All Domains](../index.md)*
