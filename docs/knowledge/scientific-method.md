# Scientific Method

> **Node ID**: knowledge.scientific-method
> **Domain**: [Knowledge Preservation & Education](./index.md)
> **Dependencies**: [`knowledge.writing`](writing.md), [`measurement`](../measurement/index.md), [`mathematics`](../mathematics/index.md)
> **Enables**: [`knowledge.standards-bodies`](standards-bodies.md), [`quality-control`](../quality-control/index.md), [`chemistry`](../chemistry/index.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Timeline**: Years 5-20
> **Outputs**: validated_knowledge, experimental_protocols, reproducible_results
> **Critical**: Yes — without systematic experimental methodology, all downstream engineering disciplines rely on trial-and-error rather than cumulative knowledge

## Prerequisites

- **Writing**: [Record-keeping](writing.md) for documenting procedures, observations, and results. The scientific method cannot function without written records — memory is unreliable, and unrecorded experiments are wasted effort.
- **Measurement**: [Measurement & Instrumentation](../measurement/index.md) for quantitative observation. Science requires numbers. "It got hotter" is anecdote; "temperature rose from 23.4°C to 67.1°C over 12 minutes" is data.
- **Mathematics**: [Mathematics & Formal Sciences](../mathematics/index.md) for statistical analysis, error propagation, and quantitative reasoning. Without mathematics, you cannot distinguish signal from noise.
- **Tools**: Basic laboratory glassware (see [Glass](../glass/index.md)), balances, thermometers, rulers, timing devices. Crude instruments suffice for early experiments; precision improves with each generation.

## Overview

![Scientific Method Graphic](../images/knowledge/knowledge_scientific-method.png)

> *This is a graphic showing the recursive scientific process.*

> *Image: Sarah Greenwood, CC BY 4.0*

The scientific method is a **systematic engineering process for producing reliable knowledge**. It is not philosophy — it is a quality-control system for empirical claims, analogous to how metrology is a quality-control system for manufactured parts. Every output (validated knowledge claim) is produced by a defined process (experiment), measured against standards (reproducibility), and subjected to verification (peer replication).

Without this process, civilizations rely on authority, tradition, and anecdote — all of which produce unreliable knowledge at scale. The scientific method is what converts individual observations into cumulative, trustworthy, transmissible knowledge.

## Core Process

### 1. Observation and Question

Identify a specific, bounded phenomenon that can be investigated empirically. Good questions are:
- **Specific**: "Why does copper conduct heat better than iron?" not "How does the world work?"
- **Measurable**: The answer can be expressed in numbers with units.
- **Falsifiable**: An experiment can prove the answer wrong.

Record all observations in a [laboratory notebook](writing.md) with date, conditions, and raw measurements. Never trust memory.

### 2. Hypothesis Formulation

State a **testable prediction** — a specific claim about what will happen under defined conditions. A hypothesis must:
- Make a **quantitative prediction**: "Increasing the carbon content of iron from 0.2% to 0.8% will increase hardness from 120 HV to 250 HV" — not "adding carbon makes iron harder."
- Be **falsifiable**: There must exist an experimental result that would prove it wrong.
- Be **minimal**: Explain the phenomenon with the fewest assumptions (Occam's razor). Complex hypotheses with many free parameters can fit any data and predict nothing.

**Bad hypothesis**: "The gods favor copper." (Not testable, not quantitative, not falsifiable.)
**Good hypothesis**: "Copper's electrical resistance increases linearly with temperature above 0°C." (Testable, quantitative, falsifiable — if resistance decreases with temperature, the hypothesis is wrong.)

### 3. Controlled Experimentation

Design an experiment that **isolates one variable** while holding all others constant. This is the core engineering challenge of experimental science.

**Variable isolation**:
- **Independent variable**: The one factor you deliberately change (e.g., carbon content).
- **Dependent variable**: The factor you measure (e.g., hardness).
- **Controlled variables**: Everything else that could affect the outcome (temperature, cooling rate, sample geometry, impurity levels). These must be held constant or their variation recorded and accounted for.

**Control groups**:
- Run a parallel experiment where the independent variable is NOT changed. The control group provides the baseline against which the experimental group is compared.
- Example: Testing whether a new steel heat treatment improves wear resistance. The control group receives the standard treatment; the experimental group receives the new treatment. All other factors (material composition, sample geometry, testing machine, test duration) are identical. If the experimental group shows measurably better wear resistance, the treatment works.

**Sample size and repetition**:
- Run each experiment multiple times (minimum 3 trials; 10+ for statistical confidence). Single experiments prove nothing — any one result could be a fluke.
- Record every trial, including failures. Selective reporting (only publishing successes) invalidates the entire process.

**Blinding** (when human judgment is involved):
- The person measuring the outcome should not know which sample is control vs. experimental. This eliminates experimenter bias — the unconscious tendency to see what you expect to see.

### 4. Measurement and Quantification

Every observation must be reduced to numbers with units. Use the [measurement infrastructure](../measurement/index.md) available:

| Measurement Type | Instrument | Typical Precision |
|-----------------|-----------|-------------------|
| Length | Ruler, caliper, micrometer | ±1 mm to ±0.01 mm |
| Mass | Balance | ±1 g to ±0.001 g |
| Temperature | Thermometer, thermocouple | ±1°C to ±0.1°C |
| Time | Sundial, clock, stopwatch | ±1 min to ±0.01 s |
| Electrical | Galvanometer, voltmeter | ±0.1 V to ±0.001 V |

**Error analysis**: Every measurement has uncertainty. Record the precision of each instrument and propagate errors through calculations. If you measure a cylinder's diameter as 25.3 ± 0.1 mm and height as 10.2 ± 0.1 mm, the volume is 5,100 ± 60 mm³ — not "5,092.7 mm³" (false precision from rounding).

**Units**: Use a consistent system of units for all measurements. Document the system used. See [Standards Bodies](standards-bodies.md) for unit standardization.

### 5. Data Analysis

Apply [mathematical](../mathematics/index.md) tools to extract meaning from measurements:

- **Descriptive statistics**: Mean, median, range, standard deviation. These summarize what was observed.
- **Comparison**: Is the experimental group measurably different from the control group? Calculate the difference and its uncertainty. If the difference is smaller than the measurement uncertainty, the effect is not detected — the experiment was inconclusive, not positive.
- **Graphical analysis**: Plot data (independent variable on x-axis, dependent variable on y-axis). Visual patterns (linear, exponential, threshold) suggest mathematical relationships.
- **Curve fitting**: Find the simplest mathematical function that describes the data. A straight line (y = mx + b) is preferred over a polynomial unless the data clearly requires higher-order terms. Each added parameter must be justified by a meaningful improvement in fit.

**Statistical significance**: A result is statistically significant if the probability of observing it by chance alone is below a threshold (conventionally p < 0.05, meaning less than 5% probability of a false positive). This requires [applied mathematics](../mathematics/index.md) — specifically probability and statistics.

### 6. Reproducibility

The **single most important** criterion for scientific validity. A result that only one person can produce, on one occasion, with one apparatus, is not scientific knowledge — it is an anecdote.

**Reproducibility standards**:
- **Documentation**: Every step of the experiment must be documented in sufficient detail that another person, reading only the written record, can replicate the experiment exactly. If the documentation is incomplete, the experiment must be repeated with better records.
- **Independent replication**: The result must be reproduced by someone other than the original experimenter, using different equipment. This eliminates experimenter bias, equipment artifacts, and idiosyncratic technique.
- **Quantitative agreement**: Replicated results should agree within experimental uncertainty. If Experimenter A measures 25.3 ± 0.5 mm and Experimenter B measures 26.1 ± 0.5 mm, the results agree (overlap within uncertainty). If B measures 30.2 ± 0.5 mm, they disagree — investigate why.

**When results don't reproduce**:
- Check whether the experimental conditions were truly identical (different temperature? different raw materials? different instrument calibration?).
- Check whether the original result was a statistical outlier (were enough trials run?).
- Check whether the original documentation was complete enough for true replication.
- Non-reproducible results are **not** failures — they identify hidden variables that were not controlled, which is valuable knowledge.

### 7. Peer Verification and Iterative Refinement

**Peer review process**:
1. Experimenter writes a complete report: hypothesis, experimental design, raw data, analysis, conclusions.
2. Independent reviewers examine the report for: logical consistency, adequate controls, appropriate statistical methods, honest reporting of all data (including unfavorable results), and whether the conclusions actually follow from the data.
3. Reviewers attempt replication. If replication succeeds, the result gains credibility. If it fails, the original experimenter must investigate the discrepancy.

**Iterative refinement**:
- Initial experiments are crude. Results are approximate. Hypotheses are refined based on what was learned.
- Each iteration improves: better instruments, tighter controls, larger sample sizes, more precise hypotheses.
- The process converges on increasingly reliable knowledge over time. No single experiment is definitive; cumulative evidence from many independent experiments builds confidence.

## Experimental Design Patterns

### Comparative Experiment

Test whether a change produces an effect. Standard pattern:
1. Control group (no change) vs. experimental group (change applied).
2. Measure the dependent variable in both groups.
3. Compare using statistical tests.
4. Example: "Does adding 2% chromium to steel improve corrosion resistance?" — prepare two batches (with and without chromium), expose both to identical corrosive conditions, measure mass loss after fixed time.

### Factorial Experiment

Test multiple variables simultaneously to discover interactions:
- Two factors (A and B), each at two levels (high/low) = 4 combinations.
- Reveals whether factors interact (e.g., carbon content affects hardness differently at different quench temperatures).
- More efficient than testing one variable at a time — but requires more samples and more careful record-keeping.

### Sequential Experiment

Each experiment informs the design of the next:
1. Broad screening experiment to identify which variables matter.
2. Focused experiments on the important variables at higher resolution.
3. Optimization experiments to find the best values.
- This is the most resource-efficient approach when experimenting is expensive (which it always is in a bootstrap context).

## Laboratory Notebook Standards

The laboratory notebook is the **primary document** of the scientific method. Without it, experiments cannot be reproduced, verified, or built upon.

**Format requirements**:
- Bound notebook with numbered pages (no loose sheets that can be lost or reordered).
- Entries in permanent ink (no pencil — erasure destroys the audit trail).
- Date and experimenter name on every entry.
- No blank pages or gaps (draw a line through unused space to prevent later additions).
- Errors crossed out with a single line (still legible) and initialed — never erased or obliterated.

**Content for each experiment**:
- Purpose: What question is being investigated?
- Hypothesis: What is the predicted outcome?
- Materials: Complete list of inputs with quantities, sources, and grades.
- Procedure: Step-by-step protocol, numbered, with all parameter values specified.
- Observations: Raw measurements recorded as they are taken (not from memory later).
- Calculations: All mathematical analysis shown in full.
- Conclusions: What does the data show? Does it support or refute the hypothesis?
- Next steps: What should be investigated next based on these results?

## Material Requirements

Scientific work requires physical materials for recording, measuring, and preserving results.

| Material | Specifications | Quantity (per investigator/year) | Source |
|----------|---------------|----------------------------------|--------|
| Laboratory notebooks | Bound, numbered pages, acid-free paper, hard covers | 2-4 volumes (200 pages each) | [Paper & Pulp](../chemistry/pulp-chemicals.md) |
| Writing instruments | Permanent ink (carbon-based or iron gall), fine-point | 10-20 pens or bottles of ink | [Ink](writing.md) |
| Rulers and straightedges | Steel or wood, 300 mm, graduated in mm | 2-3 | [Machine Tools](../machine-tools/index.md) |
| Balance | Beam or spring, 0.1-1 g precision, 0-500 g range | 1 | [Measurement](../measurement/index.md) |
| Thermometer | Liquid-in-glass, -10 to 200°C, 1°C graduations | 2-3 | [Glass](../glass/index.md) |
| Glass vessels | Beakers, flasks, tubes (borosilicate if available) | 10-20 pieces | [Glass](../glass/index.md) |
| Timer | Water clock, pendulum, or mechanical, ±1 s/min | 1 | [Measurement](../measurement/index.md) |
| Calipers | Wood or metal, 0-150 mm, ±0.5 mm | 1 pair | [Machine Tools](../machine-tools/index.md) |
| Storage containers | Wooden or ceramic boxes, tight-fitting lids, moisture-proof | 5-10 | [Pottery](../ceramics/pottery.md) |
| Reference masses | Standardized stone or metal weights, 1 g to 1 kg | 1 set | [Measurement](../measurement/index.md) |

## Preservation of Scientific Records

Scientific records are the output of the entire process. Without durable records, accumulated knowledge is lost within a single generation. Three preservation layers protect against loss:

**Primary record (laboratory notebook)**: Use acid-free paper with permanent ink. Store notebooks in a dry, cool location (below 25°C, relative humidity below 60%). Keep notebooks upright on shelves — stacking compresses bindings and accelerates page deterioration. Inspect stored notebooks annually for mold, insect damage, and ink fading. If ink is fading (common with iron gall ink on acidic paper), transcribe the content to a fresh notebook before the original becomes illegible.

**Secondary copy (transcription)**: At regular intervals (monthly or quarterly), copy critical experimental results, procedures, and conclusions into a separate duplicate notebook stored in a different building. This protects against fire, flood, or theft destroying the only copy. Transcription also catches documentation gaps — if a procedure cannot be understood when re-read weeks later, the original entry was incomplete.

**Reference shelf**: Maintain a dedicated shelf or cabinet for completed notebooks, indexed by date range and subject. A [library](libraries.md) system with catalog entries for each notebook ensures that later researchers can locate relevant prior work. A notebook that cannot be found is as useless as a notebook that was never written.

## Common Failure Modes

| Failure Mode | Description | Prevention |
|-------------|-------------|------------|
| Confirmation bias | Interpreting ambiguous data as supporting the hypothesis | Pre-register the hypothesis and analysis method before collecting data |
| Uncontrolled variables | Unknown factors affecting results | List all plausible variables and control or measure each one |
| Inadequate sample size | Too few trials to distinguish signal from noise | Calculate required sample size from expected effect size and measurement precision |
| Selective reporting | Publishing only favorable results | Record and report ALL trials, including failures |
| False precision | Reporting more significant figures than the instrument supports | Round all results to instrument precision; propagate measurement uncertainty |
| Missing documentation | Experiment cannot be reproduced because details were not recorded | Use standardized notebook format; review entries for completeness before closing |
| Experimenter bias | The experimenter unconsciously influences results | Use blinding, independent replication, and automated measurement where possible |

## Building Experimental Infrastructure

The scientific method requires physical infrastructure. Start crude and iterate:

**Phase 1 — Field observation** (Years 0-5):
- No specialized equipment. Use eyes, hands, and simple tools.
- Record observations systematically in [writing](writing.md).
- Identify patterns and generate hypotheses for later testing.

**Phase 2 — Bench experimentation** (Years 5-15):
- Simple laboratory: balance, thermometer, ruler, glass vessels, heat source.
- Basic controlled experiments with one variable at a time.
- Crude but reproducible measurements.

**Phase 3 — Systematic investigation** (Years 15-30):
- Calibrated instruments from [Measurement & Instrumentation](../measurement/index.md).
- Factorial experimental designs. Statistical analysis using [mathematics](../mathematics/index.md).
- Standardized protocols shared between investigators via [writing](writing.md) and [printing](printing.md).

**Phase 4 — Quantitative science** (Years 30+):
- Precision instruments with calibration chains.
- Mathematical modeling and prediction.
- Peer review and replication networks.

## Cross-Domain Dependencies

- All experimental data recorded via [Writing & Record-Keeping](writing.md).
- Quantitative measurement requires [Measurement & Instrumentation](../measurement/index.md).
- Data analysis depends on [Mathematics & Formal Sciences](../mathematics/index.md).
- Results disseminated through [Libraries](libraries.md) and [Printing](printing.md).
- Standardized units and protocols maintained by [Standards Bodies](standards-bodies.md).

## Safety

- **Chemical experiments**: Many substances are toxic, corrosive, or reactive. Work in well-ventilated areas. Know the hazards of every material before handling it. See [Chemistry](../chemistry/index.md) safety protocols.
- **Heat and pressure**: Furnaces, pressurized vessels, and steam can cause severe burns and explosions. Use appropriate shielding and pressure relief.
- **Electrical experiments**: Even low voltages can be dangerous with sufficient current. Insulate all connections. Never work alone with high-energy systems.
- **Documentation of hazards**: Record all safety incidents in the laboratory notebook. Near-misses are data — they identify hazards before someone is injured.

## Limitations

- **Resource constraints**: Proper controlled experiments require materials, instruments, and time — all scarce in a bootstrap context. Prioritize experiments that resolve the most consequential uncertainties.
- **Statistical literacy**: Without understanding of probability and statistics, experimenters cannot distinguish real effects from random variation. Mathematical education is a prerequisite.
- **Cultural resistance**: The scientific method challenges authority and tradition. Societies that value conformity over empirical evidence will resist — and slow — the adoption of systematic experimentation.
- **Complexity ceiling**: Some phenomena (weather, ecology, economics) involve too many interacting variables for simple controlled experiments. These require statistical methods, modeling, and long-term observational data.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Experimental results vary wildly between trials | Uncontrolled variable affecting outcome | List all plausible variables; measure and record each one; control temperature, humidity, raw material batch, and operator technique |
| Cannot reproduce published results from another workshop | Documentation was incomplete — critical step or parameter was omitted | Request full protocol from original experimenter; standardize documentation format to prevent omissions |
| Results show no effect when one was expected | Effect is real but smaller than measurement precision can detect | Improve instrument precision; increase sample size; or refine hypothesis to predict a smaller effect |
| Every trial produces a different result | Measurement instrument is unreliable or uncalibrated | Calibrate instrument against known standards; if no standards exist, compare multiple instruments measuring the same sample |
| Two experimenters get different results on identical samples | Experimenter bias or technique difference | Blind the measurement step; automate where possible; standardize technique through written protocol and training |
| Data analysis gives contradictory conclusions depending on method | Sample size too small for statistical power | Collect more data; use simpler analysis methods (descriptive statistics before inferential); report all analyses honestly |

## See Also

- [Writing & Record-Keeping](writing.md) — documentation of experiments and results
- [Mathematics & Formal Sciences](../mathematics/index.md) — statistical analysis and quantitative reasoning
- [Measurement & Instrumentation](../measurement/index.md) — calibrated quantitative observation
- [Standards Bodies](standards-bodies.md) — standardized units, protocols, and specifications
- [Technical Drawing](technical-drawing.md) — precise visual communication of apparatus and results
- [Education & Training](education.md) — teaching experimental methodology

---

*Part of the [Bootciv Tech Tree](../index.md) • [Knowledge](./index.md) • [All Domains](../index.md)*
