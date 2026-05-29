# Process Control & Lot Tracking

> **Node ID**: automation.process-control
> **Domain**: [Automation & Robotics](./index.md)
> **Dependencies**: [`automation.equipment-communication`](equipment-communication.md), `quality-control`
> **Enables**: None (leaf capability)
> **Timeline**: Years 60-100+
> **Outputs**: recipe_management, lot_tracking, process_sequencing, fault_detection, run_to_run_control
> **Critical**: No — manual recipe execution and lot tracking are possible; automated control improves yield and consistency but does not enable fundamentally new capabilities

## Problem

A semiconductor wafer undergoes 400-700 individual process steps over 4-8 weeks of fabrication. Each step has precise recipe parameters (temperature ramp rates, gas flows, RF powers, etch times) that must be executed exactly. A single parameter deviation at step 200 may not produce a detectable defect until electrical test at step 600 — by which time 400 steps of value have been added to a wafer that must now be scrapped. Automated process control and lot tracking ensure every wafer receives the correct process at every step, with full traceability from raw silicon to finished die.

## Decision Framework: Process Control Architecture

| Process Characteristic | Recommended Control Method | Rationale |
|----------------------|--------------------------|-----------|
| Stable, well-characterized process | Standard recipe execution + SPC monitoring | Process is repeatable; detect drift via control charts |
| Systematic drift over time (pad wear, chamber seasoning) | Run-to-run (R2R) control with EWMA | Compensates gradual shifts between runs using post-process metrology feedback |
| Rapid within-run anomalies (MFC drift, plasma instability) | Fault Detection and Classification (FDC) | Real-time trace analysis detects anomalies within a single wafer processing |
| New process with unknown parameter sensitivities | Design of Experiments (DOE) + FMEA | Systematically explore parameter space before production commitment |
| Critical dimension with tight tolerance (±2 nm) | R2R + FDC + inline metrology | Layered defense: FDC catches acute faults, R2R compensates chronic drift |

## Implementation Steps

1. **Define process flows in MES**: Enter complete fabrication sequence (800-1,000 steps) with tool type, recipe, and qualification requirements for each operation
2. **Deploy recipe management**: Load approved recipes into MES with version control, approval workflows, and safety limit enforcement
3. **Enable lot tracking**: Configure RFID-based FOUP tracking at all load ports. Implement track-in/track-out verification against process flow
4. **Install FDC on critical tools**: Deploy real-time trace analysis on etch, CVD, and implant tools. Train multivariate models on 50-100 baseline runs per chamber
5. **Implement R2R control**: For CMP (thickness) and lithography (CD), connect post-process metrology to R2R controller with EWMA algorithm. Start with λ=0.2
6. **Establish equipment qualification**: Define IQ/OQ/PQ protocols for each tool type. Schedule monitor wafers at regular intervals (every 100 wafers or 24 hours)

## Process Control Trade-offs

| Method | Detection Speed | Implementation Cost | Skill Required | Best Application | Limitation |
|--------|----------------|--------------------|---------------|-----------------|------------|
| SPC monitoring | Hours to days | Low | Medium | Stable processes, long-term trend detection | Lagging indicator — detects after shift occurs |
| FDC (real-time) | Seconds | High | High | Critical tools with fast process dynamics | Requires baseline data and model training |
| R2R control | Per-run | Medium | Medium | Processes with systematic drift (CMP, litho) | Cannot compensate sudden shifts or random excursions |
| DOE optimization | Weeks (one-time) | Medium | High | New process development, yield improvement | Not a continuous control method; periodic application |

**SPC Monitoring**:

**Strengths**:
- Lowest implementation cost — control charts require only a spreadsheet and metrology data
- Well-understood statistical theory — standard rules (Western Electric, Nelson) for out-of-control detection
- Applicable to any process parameter — universal method for long-term stability monitoring
- Requires minimal computing infrastructure — paper charts still work
- Industry-standard training widely available — shortest learning curve of any control method

**Weaknesses**:
- Lagging indicator — detects process shifts only after affected lots have been processed
- Cannot identify root cause — only flags that a shift occurred, not why
- Slow response time (hours to days) — unsuitable for rapid processes where defects accumulate quickly
- Requires statistically significant sample sizes — false alarms erode operator confidence if control limits are poorly set
- Does not prevent defects — only detects them after the fact

**FDC (Real-Time Fault Detection and Classification)**:

**Strengths**:
- Fastest detection (seconds) — catches anomalies within a single wafer processing cycle
- Prevents defective wafers — can halt processing before damage accumulates across a lot
- Multivariate models capture correlated faults that univariate SPC misses
- Fault classification enables rapid root-cause response — directs maintenance to the right subsystem
- Highest return on investment for high-value wafers — one prevented scrap lot pays for months of FDC operation

**Weaknesses**:
- Highest implementation cost — requires real-time data infrastructure, model training, and dedicated servers
- Requires 50-100 baseline runs per chamber before models are reliable — not usable on day one
- Model maintenance burden — chamber cleans, part replacements, and recipe changes require model retraining
- False alarm risk — poorly tuned models alarm on normal process variation, causing unnecessary holds
- Complex to deploy — needs SECS/GEM data streaming, signal processing, and statistical expertise

**R2R (Run-to-Run) Control**:

**Strengths**:
- Compensates systematic drift proactively — keeps process centered on target between runs
- Moderate implementation cost — leverages existing metrology data, no real-time infrastructure needed
- Proven algorithms (EWMA) — well-understood control theory with predictable behavior
- Significant improvement for drift-prone processes — CMP thickness variation reduced 4× with R2R
- Works with existing equipment — only requires metrology feedback loop, no tool modifications

**Weaknesses**:
- Cannot compensate sudden shifts or random excursions — only addresses gradual, predictable drift
- Model-dependent — if the process gain (b) is wrong, R2R drives the process further from target
- Requires post-process metrology — feedback delay means some wafers processed with suboptimal recipe
- Safety risk if adjustments are unchecked — R2R must never modify safety limits, only process parameters
- Not applicable to all process steps — only useful where measurable output correlates to adjustable input

**DOE (Design of Experiments)**:

**Strengths**:
- Systematically explores parameter space — efficient alternative to one-factor-at-a-time experimentation
- Identifies interactions between factors — discovers non-obvious parameter dependencies
- One-time investment — optimized process recipe then runs without further DOE intervention
- Quantifies factor significance — statistical analysis ranks which parameters matter most
- Essential for new process development — no other method efficiently characterizes a multi-parameter process window

**Weaknesses**:
- Not a continuous control method — periodic application only, does not monitor ongoing production
- Requires statistical expertise — fractional factorial designs, ANOVA, and response surface methodology are specialized skills
- Time-consuming — full DOE on a process with 6 factors requires 16-32 experimental runs plus analysis time
- Experimental wafers are expensive — DOE consumes tool time and test wafers that could produce revenue
- Results may not generalize — DOE performed on one chamber may not transfer to another without re-qualification

## Recipe Management

## Recipe Structure

A process recipe defines the complete sequence of operations a tool must perform on a wafer. Recipes are the executable programs of semiconductor manufacturing.

**Recipe hierarchy**:
- **Process recipe**: Top-level recipe for a complete process step (e.g., "Gate Etch 7 nm Node"). Contains a sequence of recipe steps.
- **Recipe step**: Individual operation within a process. Each step has: duration (seconds), gas flows (sccm), chamber pressure (Torr), RF power (Watts), temperature (°C), and termination conditions (endpoint detection, time expiry).
- **Recipe parameter**: Individual control variable within a step. Each parameter has: setpoint value, tolerance band, ramp rate (units/second), and alarm limits (upper and lower).

**Example recipe — polysilicon gate etch**:
```
RECIPE: Gate_Poly_Etch_7nm_Rev3
  STEP 1: Stabilize
    Pressure: 10 mTorr, Ramp: 5 s
    RF1 Power: 0 W
    He Cooling: 10 Torr
    Duration: 10 s

  STEP 2: Breakthrough Oxide
    Gas: CF4 = 30 sccm, CHF3 = 20 sccm, Ar = 50 sccm
    Pressure: 15 mTorr
    RF1 Power: 150 W, 13.56 MHz
    RF2 Bias: 80 W, 2 MHz
    Duration: 8 s (or endpoint on 520 nm OES channel)

  STEP 3: Main Poly Etch
    Gas: Cl2 = 100 sccm, HBr = 50 sccm, O2 = 5 sccm
    Pressure: 8 mTorr
    RF1 Power: 250 W
    RF2 Bias: 120 W
    Endpoint: OES channel 840 nm (poly-Si emission line)
    Overetch: 15% after endpoint

  STEP 4: Strip Polymer
    Gas: O2 = 200 sccm
    Pressure: 50 mTorr
    RF1 Power: 100 W
    Duration: 10 s

  STEP 5: Cool-down
    Gas: N2 = 200 sccm
    Pressure: 100 mTorr
    RF1 Power: 0 W
    Duration: 15 s
```

## Recipe Version Control

- **Versioning**: Each recipe has a unique version identifier (e.g., `Gate_Poly_Etch_7nm_Rev3.2`). Minor revisions (parameter tuning) increment the decimal. Major revisions (new step sequence) increment the integer.
- **Approval workflow**: Recipe changes require approval from process engineer → section manager → quality assurance before release to production. Each approval recorded with timestamp and electronic signature (21 CFR Part 11 compliance for medical device fabs).
- **Change control**: When a recipe is modified, all previous production lots remain associated with the version used at the time of processing. Full audit trail: who changed what, when, and why.
- **Recipe download**: MES sends the approved recipe to the tool via SECS/GEM S7F3 (Process Program Send) before the lot arrives at the tool. The tool acknowledges recipe receipt and verifies checksum (CRC-32 or MD5). If checksum fails, the tool rejects the recipe and the lot is not processed.

## Recipe Parameter Limits

- **Safety limits**: Hard limits that cannot be exceeded regardless of recipe settings. Defined by equipment engineering based on physical constraints (e.g., maximum gas flow = 500 sccm because MFC full-scale range is 500 sccm; maximum RF power = 1000 W because matching network rating is 1000 W). Enforced at the tool controller level — recipe values exceeding safety limits are rejected at download.
- **Process window limits**: Soft limits defining the acceptable process parameter range for yield optimization. Width typically ±10-20% of setpoint. Violations trigger alarms but do not stop the process (the recipe continues, but the event is logged for investigation).
- **Interlocks**: Recipe cannot start unless all safety interlocks are satisfied (coolant flow ≥ minimum, exhaust vacuum within range, gas cabinet door closed, chamber match tuned). Interlock status read via SECS/GEM status variables before process start.

## Lot Tracking

## Lot Identification

- **Lot ID**: Unique identifier for a group of wafers processed together (typically 25 wafers per lot for 300 mm). Format: alphanumeric, typically 10-20 characters. Example: `A1234567.01` where `A` = fab code, `1234567` = sequence number, `.01` = split lot indicator.
- **Wafer ID**: Individual wafer within a lot. Typically `Lot_ID-W01` through `Lot_ID-W25`. Some fabs laser-serialize each wafer with a 2D DataMatrix code (≈1 mm²) on the wafer edge for individual traceability.
- **Cassette/FOUP mapping**: The MES knows which wafer occupies which slot in which FOUP. When a FOUP arrives at a tool, the MES sends the wafer map (SECS/GEM S6F11 event with slot/wafer ID association) to the tool controller.

## Track-In / Track-Out Flow

1. **Track-in**: When a lot arrives at a tool, the operator or automated system scans the FOUP RFID. MES verifies:
   - Correct lot for this tool and process step (prevent wrong-step processing).
   - Recipe is current and approved for this lot's product.
   - Tool is qualified for this recipe (tool has passed recent qualification wafer test).
   - No outstanding tool alarms that would affect process quality.
   - Required consumables are available (gas canisters, slurry, CMP pads within life limits).

2. **Processing**: MES records start time, tool ID, chamber ID, recipe version, and lot ID. During processing, trace data (temperatures, pressures, gas flows, RF power, OES signals) are collected via SECS/GEM S6F1 at 1-10 second intervals and stored in the process history database.

3. **Track-out**: When processing completes, MES records end time, process status (pass/fail/abort), and wafer-by-wafer results (if the tool provides per-wafer data such as etch rate uniformity or deposition thickness). MES updates the lot's route — the next process step is determined by the process flow definition.

## Wafer Genealogy

- **Forward traceability**: Given a starting lot, trace every process step, tool, chamber, recipe, and parameter it experienced. Used for yield analysis — identify common process conditions in high-yield vs. low-yield lots.
- **Backward traceability**: Given a finished die (identified by wafer ID and die X,Y coordinates), trace every process step that contributed to its fabrication. Used for failure analysis — when a customer reports a defective chip, identify which process step may have caused the defect.
- **Commonality analysis**: When multiple lots show the same defect, search for common equipment or process conditions. Example: "Lots A1234, A1238, and A1241 all ran on Chamber 3 of Tool Etch-12 during the same week — investigate Chamber 3 for drift or contamination."
- **Data volume**: A single lot generates 10-100 MB of trace data across its full process flow (hundreds of steps × dozens of parameters × time-series data). A fab producing 50,000 wafers/month generates 5-50 TB of process data per month. Data retention: 5-10 years for traceability compliance.

## Process Sequencing

## Route Management

- **Process flow**: A directed graph of process steps defining the complete fabrication sequence for a product. A typical 7 nm logic process has 800-1,000 steps organized into 50-70 loops (a loop is a group of steps that repeats for each metal layer).
- **Route definition**: Stored in MES as a sequence of operations, each operation specifying: required tool type, recipe, qualifying criteria, and next operation(s). Branching operations (test insertions, rework loops) have conditional next steps.
- **Dynamic routing**: MES selects the specific tool instance at runtime based on tool availability, qualification status, WIP balancing, and tool dedication rules (some tools are dedicated to specific layers or products to prevent cross-contamination).
- **Rework loops**: When inline inspection detects a defect that can be repaired (e.g., a lithography re-exposure, a re-etch to remove residue), the MES reroutes the lot through a rework sequence before returning it to the main flow. Rework percentage typically 2-10% of lots; higher indicates process instability.

## Dispatch Rules

MES uses dispatch rules to determine which lot should be processed next at each tool:

- **FIFO (First In, First Out)**: Simplest rule — process lots in arrival order. Prevents starvation but does not optimize throughput.
- **SRPT (Shortest Remaining Processing Time)**: Prioritize lots closest to completion. Maximizes throughput but may starve lots with many remaining steps.
- **Due date priority**: Lots with nearest due dates get priority. Used for customer commits.
- **Hot lot preemption**: Hot lots jump to the front of every queue, preempting normal lots. Necessary for development wafer fast-turn or critical customer orders.
- **Batch formation**: For batch tools (furnaces, wet benches), MES groups lots with compatible recipes into batches to fill the tool (typical batch = 4-6 lots = 100-150 wafers). Batch formation waits until enough compatible lots accumulate or a timeout expires.

## Fault Detection and Classification (FDC)

## Real-Time Signal Monitoring

FDC systems analyze equipment sensor data in real-time to detect process anomalies before they produce defective wafers.

**Data collection**:
- **Trace variables**: 20-200 sensor signals per tool, sampled at 1-10 Hz during processing. Signals include: RF forward/reflected power, chamber pressure, gas flows (each MFC), electrode temperature, chuck temperature, OES (optical emission spectroscopy) channels, V/I phase angle, throttle valve position.
- **Data pipeline**: Tool controller → SECS/GEM S6F1 trace data → FDC server. Latency from sensor to FDC alarm: <5 seconds. FDC must detect faults before the process step completes (typically 10-300 seconds per step).

**Fault detection methods**:
- **Univariate limits**: Simple upper/lower bounds on individual signals. If RF power exceeds 260 W when setpoint is 250 W ±10 W (±4%), trigger alarm. Fast, easy to implement, but misses complex faults involving correlated signals.
- **Multivariate statistical models**: Principal Component Analysis (PCA) or Partial Least Squares (PLS) model trained on historical "good" process runs. New traces projected into the model space — if the trace deviates from the normal cluster beyond a statistical threshold (typically T² > 99% confidence limit or Q residual > 95% limit), trigger alarm. Captures 90-95% of process anomalies with <1% false alarm rate.
- **Signature matching**: Compare current trace shape (trajectory over time) against a library of known fault signatures. If the current trace matches a known fault pattern, classify the fault type and suggest corrective action. Useful for recurring failure modes.

**Alarm actions**:
- **Warning**: Log alarm, continue processing. Process engineer reviews after lot completes.
- **Hold**: Stop processing after current wafer completes. Lot placed on hold for engineer disposition. Prevents processing remaining wafers in the lot through a suspect chamber.
- **Abort**: Immediately terminate the process. Used when sensor readings indicate imminent equipment damage (e.g., RF matching failure, pressure excursion).

## Fault Classification

When FDC detects an anomaly, classification identifies the root cause category:

- **Gas flow fault**: MFC drift, gas line leak, gas cylinder depletion. Signature: gradual drift in one gas flow reading, correlated pressure change.
- **RF fault**: Matching network drift, plasma instability, electrode contamination. Signature: increased reflected power, V/I phase shift, pressure fluctuation.
- **Chamber condition drift**: Wall polymer buildup, consumable wear (focus ring, ESC). Signature: slow trend in multiple parameters over many wafers (etch rate shift, uniformity change).
- **Wafer handling fault**: Misplaced wafer on chuck, incomplete vacuum clamp. Signature: abnormal thermal contact (temperature reading shift), helium leak rate increase.

Classification accuracy target: >80% correct classification. Remaining cases escalated to process engineer for manual diagnosis.

## Run-to-Run (R2R) Control

## Motivation

Even when each process run stays within spec, systematic drift (chamber wall film buildup, consumable wear, gas cylinder depletion) causes the process mean to shift over time. Run-to-run control compensates for this drift by adjusting recipe parameters between runs, keeping the process centered on target.

## Control Architecture

- **Pre-process metrology**: Measure wafer before processing (e.g., incoming film thickness). Provides input to the R2R controller.
- **Post-process metrology**: Measure wafer after processing (e.g., etched feature depth, deposited film thickness). Provides the controlled output.
- **R2R controller**: Computes recipe adjustments for the next run based on post-process metrology feedback. Standard algorithm: EWMA (Exponentially Weighted Moving Average) controller.
- **EWMA update**: θ̂(t) = λ × y(t) + (1 - λ) × θ̂(t-1). Where θ̂(t) is the estimated process disturbance, y(t) is the latest metrology measurement minus model prediction, and λ is the smoothing factor (typically 0.1-0.3). The recipe adjustment is b⁻¹ × [target - θ̂(t)], where b is the process gain (change in output per unit change in input).

## R2R Application Examples

- **CMP (Chemical Mechanical Polishing)**: Measure post-polish film thickness. Adjust polish time for next wafer to compensate for pad wear rate. Without R2R: thickness drifts ±200 Å over pad life. With R2R: thickness maintained within ±50 Å of target.
- **Lithography CD (Critical Dimension) control**: Measure post-etch CD on test structures. Adjust exposure dose for next lot to compensate for scanner drift and resist aging. CD control improves from ±5 nm to ±2 nm with R2R.
- **CVD deposition**: Measure post-deposition thickness. Adjust deposition time to compensate for chamber seasoning effects (first few wafers after chamber clean deposit slightly different rate than seasoned chamber).

## Safety & Hazards

- **Recipe corruption in R2R**: An R2R controller bug could compute an invalid recipe adjustment (e.g., negative gas flow, RF power exceeding hardware limits). All R2R adjustments must pass safety limit checks before being downloaded to the tool. Never allow R2R to modify safety limits — only process parameters within approved ranges.
- **Model divergence**: If the process changes fundamentally (new chamber hardware, different gas supplier, maintenance event), the R2R model may be invalid. Model mismatch causes R2R to make wrong adjustments, driving the process further from target. Implement model health monitoring (track prediction error over time) and automatic model reset when prediction error exceeds threshold.
- **Data integrity**: Lot tracking data must be tamper-proof and auditable. Any modification to historical process data (e.g., backdating a hold release) must be logged with justification. Regulatory requirements (FDA for medical device fabs, automotive IATF 16949) mandate full data traceability.
- **Oversight automation failure**: If FDC or R2R systems go offline, operators may not notice subtle process drift for hours. Implement FDC health monitoring — if the FDC server stops receiving trace data, trigger an alarm and consider holding further processing until FDC is restored.

## Equipment Qualification

## Tool Qualification for Production

Before a tool is authorized to run production wafers, it must pass qualification testing:

**Initial qualification (IQ)**:
- Verify mechanical installation: level, vibration isolation, utility connections (power, gas, water, exhaust).
- Verify software: SECS/GEM communication, recipe upload/download, alarm reporting, event notification.
- Verify safety interlocks: door interlock, gas detection, fire suppression, emergency stop.

**Operational qualification (OQ)**:
- Process qualification wafers (typically 3-5 test wafers) using the target recipe. Measure key output parameters: etch rate, deposition thickness, uniformity, selectivity, particle adders.
- Compare results against specification limits (e.g., etch rate 500 ±50 Å/min, uniformity ≤±3% across wafer). All parameters must pass.
- Chamber-to-chamber matching: For multi-chamber tools, verify all chambers produce equivalent results. Matching tolerance: ≤50% of the process spec width.

**Performance qualification (PQ)**:
- Run 3-5 consecutive lots with production wafers. Demonstrate that process results are stable and within spec over the qualification period.
- Process Capability Index (Cpk) must be ≥1.33 for all critical parameters during PQ. Cpk = min[(USL - μ), (μ - LSL)] / (3σ), where USL/LSL are spec limits, μ is the process mean, σ is the standard deviation.

## Ongoing Qualification

- **Monitor wafers**: Run a monitor wafer at regular intervals (e.g., every 100 wafers or every 24 hours) to track chamber performance trends. If monitor results drift beyond warning limits, schedule preventive maintenance. If beyond control limits, quarantine the tool and investigate.
- **Chamber matching re-verification**: After any maintenance event (chamber clean, parts replacement), re-run qualification wafers to verify chamber performance has not shifted.
- **Tool dedication**: Some tools are dedicated to specific process layers (e.g., "Chamber 3 is only for gate etch") to prevent cross-contamination and reduce qualification burden. Tool dedication is maintained in MES — the MES will not dispatch incompatible lots to a dedicated tool.

## Data Infrastructure

**Process data warehouse**:
- All trace data, event data, alarm data, metrology results, and lot tracking records flow into a central data warehouse (typically a time-series database like InfluxDB or a columnar store like Apache Parquet on HDFS).
- Query performance: typical analytical query (e.g., "show etch rate trend for Chamber 3 over the last 30 days") must return in <10 seconds over billions of data points.
- Data retention policy: raw trace data (1 Hz sensor readings) retained for 1-2 years. Aggregated data (per-wafer averages, per-lot summaries) retained for 5-10 years. Lot genealogy records retained indefinitely.

**Real-time dashboards**:
- **Tool status**: Current state of every tool (idle, processing, down, qualified, unqualified) displayed on large monitors in the fab control room. Color coding: green = processing, yellow = idle, red = down, blue = under maintenance.
- **WIP map**: Display of all lots in the fab, color-coded by process step and time-in-step. Bottleneck tools identified by WIP accumulation (many lots queuing = bottleneck).
- **FDC alarm summary**: Current active alarms, alarm rate trend, and fault classification breakdown. Escalation indicators for alarms not addressed within SLA time.



[← Back to Automation & Robotics](index.md)
