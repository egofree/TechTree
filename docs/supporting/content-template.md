# Content Template: Workshop-Manual Standard

> **Purpose**: Reference template for expanding tech-tree capability documents from stubs to workshop-manual depth. Defines the mandatory structure, minimum quality standard, and formatting conventions for all expanded content.
> **Audience**: Content authors expanding capability files across all domains.
> **Status**: Normative — all new and expanded content MUST conform to this template.

---

## Minimum Standard for Expanded Content

An expanded capability file must meet ALL of the following criteria before it is considered complete:

1. **All 11 mandatory sections** present with substantive content (not just headers).
2. **At least one quantitative table** with real numbers — temperatures, pressures, yields, material ratios, speeds, tolerances, or comparable operating data. "Quantitative" means measured values with units, not qualitative descriptors.
3. **Minimum 200 lines** of content (excluding the metadata blockquote header and the footer navigation link).
4. **Blockquote-style metadata** at the top of the file. No YAML frontmatter. Format: `> **Field**: value` (see header convention below).
5. **Cross-references** to at least two other capability docs in the project, using relative Markdown links.
6. **Safety section** with specific hazards and mitigation measures — not generic warnings.

Stubs (placeholder files) remain acceptable as long as they are clearly marked. The 200-line standard applies only to files flagged for expansion.

---

## File Header Convention

Every capability file opens with a blockquote metadata block. Use this exact format:

```markdown
# Title of the Capability

> **Node ID**: domain.capability-name
> **Domain**: [Domain Name](./index.md)
> **Dependencies**: [`other.domain.capability`](../path/to/file.md), ...
> **Enables**: [`downstream.capability`](../path/to/file.md), ...
> **Timeline**: Years X-Y
> **Outputs**: output_material_name
> **Critical**: Yes/No — one-line reason
```

Fields:
- **Node ID**: Dotted hierarchical kebab-case matching `nodes.json`.
- **Domain**: Link to the domain index.
- **Dependencies**: Upstream capabilities required, with links.
- **Enables**: Downstream capabilities unlocked, with links.
- **Timeline**: Approximate bootstrap years when this capability becomes available.
- **Outputs**: Primary material or product from `nodes.json` output list.
- **Critical**: Whether this is a critical-path node, with a brief reason.

---

## The 11 Mandatory Sections

### 1. Overview

What to include:
- What this capability IS — a concise definition of the process, material, or technology.
- Why it MATTERS — its role in the bootstrap chain. What downstream capabilities depend on it?
- Position in the dependency chain — what must exist before this, and what becomes possible after.
- Scale of impact — how much of the final goal (semiconductor manufacturing, solar cells, etc.) depends on this node.

Keep the overview to 2-4 paragraphs. It should give a reader enough context to understand why they're reading this file without duplicating the process description.

### 2. Prerequisites

What to include:
- **Materials** required before starting, with purity or grade specifications where relevant.
- **Tools and equipment** required — link to their capability docs, not just names.
- **Knowledge** required — what skills or understanding the operators need.
- **Infrastructure** — power, water, buildings, ventilation, etc.
- Cross-reference each prerequisite to its doc using relative Markdown links.

Format as a bullet list or table grouped by category (materials / tools / knowledge / infrastructure).

### 3. Bill of Materials (BOM)

What to include:
- A table with columns: Material, Quantity (per unit of output), Source, Alternatives.
- Quantities must have units (kg, tonnes, liters, m³, kWh).
- Source column: where this material comes from in the bootstrap chain (link to doc).
- Alternatives column: what can substitute if the primary material is unavailable.
- If the capability operates at multiple scales, provide BOM rows per scale.

<!-- EXAMPLE: Filled BOM table from metallurgical-grade silicon production -->

Example (from MG-Si production):

| Material | Quantity per tonne MG-Si | Source | Alternatives |
|----------|--------------------------|--------|-------------|
| Quartz (SiO₂ >98%) | 2.7-3.0 tonnes | [Mining](../mining/index.md) — high-purity quartzite or vein quartz | Lower-purity quartz possible but increases downstream refining burden |
| Carbon reductant (petroleum coke, fixed C >95%) | 1.0-1.4 tonnes | [Petroleum](../chemistry/petroleum-alternatives.md) — calcined petroleum coke | Charcoal (higher ash), coal (higher impurities) |
| Wood chips (porosity agent) | 0.5-1.0 tonnes | [Forestry](../plants/index.md) — hardwood or softwood chips | No substitute — charge permeability is critical |
| Electrode carbon (Søderberg paste) | 300-400 kg | [Electric Furnaces](../energy/electric-furnaces.md) — petroleum coke + coal tar pitch | Prebaked graphite electrodes (400-500 kg, higher cost, lower impurity) |
| Electrical energy | 11-13 MWh | [Power Generation](../energy/index.md) — continuous baseload required | No alternative — arc furnace cannot run on intermittent power |

<!-- END EXAMPLE -->

### 4. Process Description

What to include:
- **Numbered step-by-step procedure** — the core of the workshop manual.
- Each step should state WHAT to do, not just what happens. Use imperative mood ("Heat the retort to 400°C", not "The retort is heated").
- Specify temperatures, times, pressures, flow rates, or other measurable parameters at each step.
- Include decision points: "If smoke turns blue, seal all vents."
- Separate distinct methods or process variants into their own subsections.
- Cover the full process cycle: startup → steady-state operation → shutdown.

### 5. Quantitative Parameters

What to include:
- Tables of operating parameters organized by parameter type (temperature, pressure, speed, yield, etc.).
- Provide ranges, not just single values — real processes operate within bands.
- If the capability operates at multiple scales (bench / pilot / production), provide a parameter table per scale.
- Include units on every number. Use SI units as primary; imperial in parentheses if relevant.
- Energy consumption, material consumption rates, and throughput figures are mandatory.

<!-- EXAMPLE: Filled parameter table from charcoal production -->

Example — pyrolysis parameters by method:

| Parameter | Pit Method | Simple Kiln | Mound Kiln | Retort |
|-----------|-----------|-------------|------------|--------|
| Temperature range | 400-600°C | 400-600°C | 400-600°C | 400-600°C |
| Cycle time (firing) | 12-48 hours | 8-24 hours | 2-5 days | 6-12 hours |
| Cooling time | 24-48 hours | 12-24 hours | 24-48 hours | 6-12 hours |
| Yield by weight | 20-35% | 30-40% | 25-35% | 35-45% |
| Batch size | 50-200 kg | 100-500 kg | 1-5 tonnes | 50-500 kg |
| Charcoal quality | Variable | Good | Good | Best |
| Byproduct recovery | None | Minimal | None | Full (tar, vinegar, gas) |
| Reusability | None (one-time pit) | Hundreds of cycles | One-time mound | Indefinite (equipment) |

<!-- END EXAMPLE -->

### 6. Scaling Notes

What to include:
- How to move from experimental / bench scale to pilot to production throughput.
- What changes when scaling — are parameters linear, or do new phenomena emerge?
- Equipment sizing rules of thumb.
- Bottlenecks that appear at larger scales (heat transfer, material handling, power supply).
- Minimum economic scale — the smallest operation that produces useful output.
- Examples of scale breakpoints: "A single bloomery produces ~10 kg iron per run; a small blast furnace produces 1 tonne/day — the jump requires mechanized air supply."

### 7. Troubleshooting

What to include:
- Table format: Problem | Probable Cause | Solution.
- Draw from real failure modes of the process.
- Include both process problems (low yield, poor quality, equipment failure) and product problems (wrong composition, wrong dimensions, defects).
- Prioritize by frequency or severity — common problems first.

<!-- EXAMPLE: Filled troubleshooting table from machining operations -->

Example — common machining problems:

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Chatter (vibration marks on surface) | Tool overhang too long, insufficient rigidity | Reduce overhang to ≤4× tool diameter; use heavier boring bar; reduce RPM |
| Poor surface finish | Dull tool, excessive feed rate | Sharpen or replace insert; reduce feed to 0.05-0.15 mm/rev for finishing |
| Drill binding in deep hole | Chip packing in flutes | Use peck drilling — retract every 1-2 mm to clear chips; apply flood coolant |
| Workpiece slipping in chuck | Insufficient clamping force or worn jaws | Tighten chuck; use 4-jaw independent chuck; check jaw condition |
| Dimensional drift over batch | Tool wear changing effective cut depth | Measure parts frequently; index or replace inserts per schedule (every 15-60 min cutting time for carbide) |

<!-- END EXAMPLE -->

### 8. Safety

What to include:
- Specific hazards of THIS process — not generic workshop safety. Name the chemical, temperature, voltage, or mechanical danger.
- Severity and exposure route: "CO is colorless, odorless, lethal at 0.1% in air for 1 hour. Off-gas system leaks are the primary risk."
- Personal protective equipment (PPE) required — specify the rating or standard, not just "wear gloves."
- Emergency procedures: what to do when something goes wrong (spill, fire, exposure, equipment failure).
- Environmental hazards: toxic releases, waste disposal, air/water contamination.
- Use direct language. "CO detectors mandatory. Evacuate at >50 ppm." Not "It is advisable to consider monitoring for carbon monoxide."

### 9. Quality Control

What to include:
- Acceptance criteria: measurable specifications the output must meet (composition, dimensions, performance).
- Testing methods: how to measure each criterion. Include both simple/low-tech methods and advanced methods.
- Sampling procedure: how many samples, from where, how often.
- Standards or grades if applicable (e.g., "Grade 553 MG-Si: Si ≥98.5%, Fe ≤0.5%").
- Quick field tests that don't require lab equipment.

### 10. Variations and Alternatives

What to include:
- Alternative methods for achieving the same output — when and why to choose each.
- Regional adaptations: what changes in different climates, with different raw material availability.
- Material substitutions: what to use when the ideal input is unavailable.
- Historical methods: how this was done before modern technology, and whether those methods are viable for bootstrapping.
- Trade-offs table comparing alternatives on key metrics (cost, quality, throughput, complexity).

### 11. References

What to include:
- Cross-references to other capability docs in the project (relative Markdown links).
- Glossary terms defined in the project's glossary.
- External sources: textbooks, standards, industry references — but keep these minimal. The primary purpose is internal navigation.
- Format: bullet list with brief annotations explaining why each reference is relevant.

---

## Formatting Rules

1. **Prose style**: Direct, imperative, specific. Avoid hedging language ("it is important to note that", "generally speaking", "in most cases"). State the parameter, the range, and the reason.
2. **Tables**: Use Markdown pipe tables. Include units in column headers or cells. Keep tables narrow enough to render well in standard Markdown viewers.
3. **Numbers**: Always include units. Use SI as primary. Ranges are preferred over single values when the parameter varies.
4. **Links**: All internal links are relative Markdown paths. No absolute URLs. No external links in the main body (external references go in Section 11 only).
5. **Sections**: Use `##` for the 11 mandatory sections. Use `###` for subsections within a section. Never skip heading levels.
6. **File naming**: lowercase, hyphenated (kebab-case). Matches the Node ID convention.
7. **Footer**: Close every file with the standard navigation link:
   ```
   ---
   *Part of the [Bootciv Tech Tree](../index.md) • [Domain Name](./index.md) • [All Domains](../index.md)*
   ```

---

## Anti-Patterns (What NOT to Write)

- **No AI-slop**: Avoid vague qualifiers ("important", "crucial", "it should be noted"), generic filler paragraphs, and restatement of the obvious. If a sentence can be removed without losing information, remove it.
- **No YAML frontmatter**: Project uses blockquote-style metadata exclusively.
- **No unlinked references**: If you mention another capability, link to it. Unlinked names are dead ends.
- **No unitless numbers**: Every quantitative value needs a unit. "Temperature: 1800" is meaningless. "Temperature: 1800°C in the reaction zone" is correct.
- **No purely qualitative descriptions where quantitative data exists**: "The furnace gets very hot" → "Reaction zone temperature: 1800-2100°C".
- **No marketing language**: This is a workshop manual, not a product brochure. State what the process does, its limitations, and its failure modes with equal directness.

---

## Format Variants

The 11 mandatory sections define the universal structure. But not every capability is a furnace process. The thermostat article (1,460 lines, 22 types across 4 tiers) revealed that different subject matter needs different internal organization. The format variant you choose determines how you populate the mandatory sections, especially Process Description (Section 4).

Choose the variant that matches your subject. When a capability spans multiple variants, pick the dominant one and borrow elements from others as needed.

### 1. Physical-Process (Workshop Manual)

The default variant. Use for any capability where the reader builds, operates, or maintains a physical process or device.

**Characteristics**: Construction steps with dimensions and tolerances, calibration procedures, expected performance numbers, per-method comparison tables.

**Process Description structure**: Group by method or variant. Each method gets its own subsection with:
- Principle (how it works, with governing equations where relevant)
- Prerequisites (linked to their capability docs)
- Materials (linked to their capability docs, with dimensions and quantities)
- Construction (numbered steps, imperative mood)
- Calibration or testing procedure
- Expected performance (accuracy, throughput, yield, with units)
- Applications (when to use this method vs. others)
- Strengths
- Weaknesses

**Examples**: [`metals/iron-steel.md`](../metals/iron-steel.md), [`glass/advanced.md`](../glass/advanced.md), [`measurement/thermostat.md`](../measurement/thermostat.md)

**When in doubt, use this variant.** It is the most general format and the one the existing template was designed around.

### 2. Conceptual/Organizational

Use for capabilities that are frameworks, decision criteria, or organizational systems, not physical construction processes.

**Characteristics**: Decision trees, comparison matrices, implementation criteria, organizational patterns. No dimensions or tolerances.

**Process Description structure**: Group by framework element or decision point. Each element gets:
- Principle (what it is and why it matters)
- Prerequisites (linked, as with Physical-Process)
- Implementation steps (what to do, not what to build)
- Decision criteria (how to choose between alternatives)
- Expected outcomes
- Strengths
- Weaknesses

**Examples**: [`economics-organization/governance.md`](../economics-organization/governance.md), [`knowledge/education.md`](../knowledge/education.md)

**Key difference from Physical-Process**: "Construction" becomes "Implementation." No dimensions, no tolerances. Focus on criteria, trade-offs, and decision support tables.

### 3. Biological/Agricultural

Use for capabilities involving living organisms, cultivation, or species-specific processes.

**Characteristics**: Species-specific data tables, seasonal timing, yield data, climate adaptation notes, propagation procedures.

**Process Description structure**: Group by species or cultivation method. Each entry gets:
- Principle (the biological mechanism)
- Prerequisites (linked to capability docs for tools, infrastructure)
- Materials (linked, with quantities per unit area or per animal)
- Cultivation or rearing procedure (seasonal calendar, step-by-step)
- Expected yield (with units, ranges, and conditions)
- Applications (products and uses)
- Strengths
- Weaknesses

**Examples**: [`animals/beekeeping.md`](../animals/beekeeping.md), [`agriculture/crop-rotation.md`](../agriculture/crop-rotation.md)

**Key difference from Physical-Process**: Time scales are weeks to years, not hours. Weather, season, and climate are first-class parameters. Yield data replaces throughput data.

### 4. Informational/Knowledge

Use for capabilities that reproduce, preserve, or transmit information rather than produce physical goods.

**Characteristics**: Reproduction procedures (how to copy), material requirements for the medium, preservation methods, quality metrics for the output.

**Process Description structure**: Group by method or medium. Each entry gets:
- Principle (how the reproduction or transmission works)
- Prerequisites (linked to capability docs)
- Materials (linked, the physical medium and tools)
- Procedure (step-by-step, imperative mood)
- Expected output quality (legibility, durability, error rate, with metrics)
- Applications (what this method is good for)
- Strengths
- Weaknesses

**Examples**: [`knowledge/printing.md`](../knowledge/printing.md), [`knowledge/writing.md`](../knowledge/writing.md)

**Key difference from Physical-Process**: The product is information on a medium. Quality metrics emphasize accuracy of reproduction, durability of the record, and speed of transmission rather than dimensional tolerances.

---

## Per-Subsection Elements

When Process Description (Section 4) contains multiple methods, types, or variants organized as subsections, each subsection MUST include the following elements. The thermostat article demonstrated this pattern across 22 types and it produced consistently useful, scannable content.

### Mandatory per subsection

| Element | Purpose | Present in thermostat as |
|---------|---------|--------------------------|
| **Principle** | How this method works, with governing equation or mechanism | Each type opens with "Principle:" and the physics |
| **Prerequisites** | What you need before starting (linked) | Bullet list with `[name](../path/to/doc.md)` links |
| **Materials** | Physical inputs with quantities (linked) | Bullet list with linked material names and specs |
| **Procedure** | Step-by-step instructions (Construction, Cultivation, Implementation, or Reproduction) | Numbered steps, imperative mood |
| **Calibration / Verification** | How to test that it works correctly | Numbered steps with reference instruments |
| **Expected performance** | Quantitative output specs (accuracy, yield, throughput) | "Expected accuracy:" paragraph with ranges and units |
| **Applications** | When to use this method and what it is good for | "Applications:" paragraph |
| **Strengths** | Bullet list of advantages | "Strengths:" bullet list |
| **Weaknesses** | Bullet list of limitations | "Weaknesses:" bullet list |

**Strengths and Weaknesses are mandatory.** Every subsection must list them. This is the single biggest improvement the thermostat article makes over the original template. Without Strengths and Weaknesses, the reader cannot make informed trade-off decisions between methods. A subsection that only lists advantages is a sales pitch, not a workshop manual.

---

## Writing Rules

Three rules extracted from the thermostat article. These apply to all format variants.

### Self-Containment Rule

Every subsection must be fully self-contained. A reader who jumps directly to subsection 12 (Pneumatic Thermostat) must understand it without reading subsections 1-11.

This means:
- Do NOT write "same prerequisites as Type 3 above." List the prerequisites again.
- Do NOT write "the construction method is similar to the rod-and-tube." Describe the construction fully.
- Do NOT write "see the previous section for calibration." Give the calibration procedure.

Repetition between subsections is acceptable. Linking to shared prerequisite capability docs is expected. But each subsection must stand alone as a complete reference for that method.

**Why**: Readers rarely read linearly. They jump to the method they need. If that method references material three pages up, the article has failed its purpose as a workshop manual.

### Linking Rule

Every prerequisite and every material entry must be a working relative Markdown link to its capability doc.

**Correct**:
```
- [Iron rod](../metals/iron-steel.md) (10-15 mm diameter, 400-600 mm length)
- [Glassblowing capability](../glass/glassblowing.md)
```

**Wrong**:
```
- Iron rod (10-15 mm diameter, 400-600 mm length)
- Glassblowing capability
```

Unlinked names are dead ends. The reader cannot navigate from your article to the capability they need. This defeats the purpose of a tech tree.

The linking rule applies to Prerequisites (Section 2), BOM (Section 3), and all per-subsection prerequisite/material lists. It does NOT require linking every casual mention of a technology in prose, though that is good practice when feasible.

### Citation Rule

Specific quantitative claims must cite their source or state the basis for the number inline.

**What counts as a "specific claim"**:
- Exact temperatures, pressures, dimensions, voltages, concentrations
- Performance numbers (accuracy, yield, throughput, lifetime)
- Safety thresholds (IDLH concentrations, exposure limits, pressure ratings)
- Material properties (thermal expansion coefficients, resistivity, melting points)

**How to cite**:
- For well-known physical constants: state the value and the source principle. "Mercury boiling point: 357°C at 1 atm." No further citation needed.
- For empirical process data: state the range and the source. "Charcoal yield by weight: 20-35% for pit method (tested values from [Charcoal](../energy/charcoal.md))."
- For safety thresholds: state the standard or authority. "Mercury IDLH: 10 mg/m³ (NIOSH)." "CO lethal at 0.1% in air for 1 hour."

**What does NOT need citation**: General descriptions, qualitative observations, procedural instructions ("heat until the metal glows cherry red"), and common knowledge within the domain.

---

## Scaled Detail Guidance

Not every capability needs 1,460 lines. The thermostat article covers 22 distinct types across a 55-year technology span, which justifies its length. A capability with a single method and no variants will be much shorter.

### Core (mandatory for all articles)

The 11 mandatory sections plus the per-subsection elements defined above. For a single-method capability with no variants, this typically produces 200-400 lines.

### Scaled detail (depth proportional to complexity)

Add scaled detail when the capability has any of:

| Complexity indicator | What to add | Example |
|----------------------|-------------|---------|
| Multiple methods or variants | Full per-subsection treatment for each method (Principle through Weaknesses) | Thermostat: 22 types, each fully documented |
| Wide operating range | Parameter tables split by range or scale | Thermostat: selection guide table covering -200 to 3000°C |
| Tiered technology progression | Organize methods into tiers (primitive to advanced), with a progression narrative | Thermostat: 4 tiers from pre-industrial to semiconductor |
| Integration with many other capabilities | Integration points table or "Key Deliverables by Phase" section | Thermostat: integration points across 7 bootstrap phases |
| Safety hazards varying by method | Per-method safety warnings (in addition to the Safety section) | Thermostat: mercury safety warnings embedded in Types 5 and 6 |

**Do NOT pad to reach a line count.** A 250-line article covering one method thoroughly is better than a 500-line article that repeats itself. The 200-line minimum exists to prevent stubs, not to encourage filler.

---

## Exemplar Files

These existing files demonstrate the workshop-manual standard at or above 200 lines:

| File | Lines | Strengths |
|------|-------|-----------|
| [Thermostat](../measurement/thermostat.md) | 1460 | Gold standard. 22 types across 4 tiers, every prerequisite/material linked, per-type Strengths/Weaknesses, inline citations for all numerical claims, self-contained subsections, selection guide table |
| [MG-Si Production](../silicon/mg-si-production.md) | 207 | Reaction chemistry, energy balance, electrode consumption rates, off-gas handling |
| [Charcoal](../energy/charcoal.md) | 202 | Four methods with comparison data, byproduct recovery, scale estimates table |
| [Adhesives & Coatings](../chemistry/adhesives-coatings.md) | 262 | Decision-support selection tables, chemical resistance matrix, cure parameters |
| [Machining](../machine-tools/machining.md) | 228 | Feeds & speeds table, tolerance summary by operation, troubleshooting table |

Study the thermostat article first. It demonstrates every rule and pattern described in this template. The other files show the target density for simpler capabilities: specific numbers, practical procedures, safety with severity data, and decision-support tables.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Supporting Docs](./) • [All Domains](../index.md)*
