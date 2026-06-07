# Equipment Article Template: Construction-Manual Standard

> **Purpose**: Reference template for writing standalone equipment construction articles. Defines the mandatory sections, optional sections, length guidance, and formatting conventions specific to equipment (machines, tools, furnaces, presses, pumps, etc.) — as distinct from process-oriented capability articles covered by the [content template](./content-template.md).
> **Audience**: Content authors writing equipment construction articles for the tech tree.
> **Status**: Normative — all new equipment articles MUST conform to this template.

---

## When to Write a Standalone Equipment Article

Not every piece of equipment deserves its own article. Use this decision flow:

1. **Is the item constructible in <5 steps from raw materials with no precision requirements?** → Write a named section within the parent capability article, not a standalone article. Examples: hand-forged tongs, clay crucible, wooden mallet.
2. **Is the item a bootstrap-level machine tool (lathe, mill, drill press, shaper)?** → Cross-reference [iterative-bootstrap.md](../machine-tools/iterative-bootstrap.md) rather than duplicating. These machines are covered in depth there.
3. **Does the item require multi-step construction, multiple materials, and/or calibration?** → Write a standalone equipment article using this template.

---

## File Header Convention

Every equipment article opens with a blockquote metadata block. Use this exact format — NOT YAML frontmatter:

```markdown
# Equipment Name

> **Node ID**: domain.equipment-name
> **Domain**: [Domain Name](../spec/README.md)
> **Dependencies**: [`upstream.capability`](../path/to/file.md), ...
> **Enables**: [`downstream.capability`](../path/to/file.md), ...
> **Timeline**: Years X-Y
> **Outputs**: primary_output_name
> **Critical**: Yes/No — one-line reason
```

Fields:
- **Node ID**: Dotted hierarchical kebab-case matching the entity JSON-LD file.
- **Domain**: Link to the domain index.
- **Dependencies**: Upstream capabilities required, with relative links.
- **Enables**: Downstream capabilities unlocked, with relative links.
- **Timeline**: Approximate bootstrap years when this equipment becomes available.
- **Outputs**: Primary product or capability the equipment provides.
- **Critical**: Whether this is a critical-path item, with a brief reason.

---

## Required Sections (all equipment articles)

These four sections are mandatory in every equipment article. Omitting any of them is a defect.

### 1. Principle

State what the equipment does and how it works. Include the governing physical principle or mechanism. If an equation governs the operation, state it with variable definitions.

Keep this to 1-3 paragraphs. The reader should understand the concept before reading construction steps.

Example openings from existing articles:
- "An electric arc struck between graphite electrodes and the charge material produces temperatures of 3000-3500°C in the arc column, heating the charge by radiation, convection, and direct resistance."
- "The downdraft design achieves higher temperatures and more uniform heat distribution than the updraft kiln. Hot gases rise from side fireboxes to the crown, then deflect downward through the ware, exit through floor-level flues, and are drawn up the chimney."

### 2. Materials

List every material needed to build one unit of the equipment. Use a table with these columns:

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Cast iron](../metals/iron-steel.md) | 100-200 kg | Grade 25 or higher, for bed and column | Foundry | Steel plate (welded construction) |

Rules:
- Every quantity needs units (kg, m, mm, litres).
- **Source** must be a relative Markdown link to the capability doc that produces this material.
- **Alternatives** column: what to substitute if the primary is unavailable, with the trade-off stated.
- Group materials by subsystem (frame, drive, controls) when the list is long.

### 3. Construction Steps

Numbered step-by-step instructions for building the equipment. Use imperative mood ("Cast the bed", not "The bed is cast"). Each step states WHAT to do and includes dimensions, tolerances, or measurable parameters.

Guidelines:
- Specify dimensions with units on every measurement.
- State tolerances where precision matters ("bore to 30.00 ±0.05 mm").
- Include decision points: "If the casting has porosity >5 mm, recast rather than patch."
- Cover the full build sequence: subassembly → integration → first test.
- If multiple variants exist (e.g., hand-powered vs. motorized), use `###` subsections within this section.

### 4. Expected Performance

A table of quantitative performance parameters. Every number needs a unit. Provide ranges where variation is expected.

| Parameter | Value |
|-----------|-------|
| Maximum force / temperature / speed | X-Y unit |
| Accuracy / tolerance | ±Z unit |
| Throughput | N units/hour |
| Power consumption | X kW |
| Duty cycle | continuous / X min on, Y min off |
| Service life (before major rebuild) | X firings / hours / cycles |

---

## Optional Sections (include when relevant)

These sections are not mandatory for all equipment but MUST be included when the stated condition applies.

### Prerequisites (include when the equipment needs significant upstream infrastructure)

List materials, tools, knowledge, and infrastructure required before construction can begin. Format as a bullet list grouped by category, with relative links.

Include when: the equipment requires more than 3 upstream capabilities that aren't obvious from context.

### Calibration / Verification (include when the equipment needs testing after construction)

Numbered procedure for verifying the equipment works correctly after construction. State reference instruments and acceptance criteria.

Include when: the equipment has adjustable parts, precision requirements, or safety-critical tolerances.

### Strengths / Weaknesses (include when competing alternatives exist)

Bullet lists. Strengths and weaknesses are mandatory when the article covers genuinely competing design alternatives. Omit them when the equipment has no practical alternative.

Include when: the equipment competes with other designs for the same function (e.g., downdraft kiln vs. updraft kiln; hydraulic press vs. screw press).

---

## Length Guidance

| Category | Target Length | Examples |
|----------|--------------|---------|
| **Major equipment** (multi-subsystem, precision-critical) | ~2000 words, 200-600 lines | EAF, blast furnace, lathe, tunnel kiln |
| **Standard equipment** (single purpose, moderate complexity) | ~1000 words, 100-300 lines | Updraft kiln, drill press, resistance furnace |
| **Minor items** (hand tools, simple jigs) | ~600 words, 60-150 lines (or section within parent article) | Tongs, sledge hammer, sharpening jig |

Do NOT pad to reach a word count. A thorough 250-line article covering one method is better than a 500-line article that repeats itself.

---

## Formatting Rules

1. **Blockquote headers only** — no YAML frontmatter. Format: `> **Field**: value`.
2. **Relative Markdown links** — all internal links use relative paths. No absolute URLs. No external links in the main body.
3. **Tables** — Markdown pipe tables with units in column headers or cells.
4. **Numbers** — always include units. SI primary; imperial in parentheses if relevant.
5. **Headings** — `##` for major sections, `###` for subsections. Never skip levels.
6. **Prose style** — direct, imperative, specific. No hedging language.
7. **Footer** — close every file with:
   ```
   ---
   *Part of the [Bootciv Tech Tree](../index.md) • [Domain Name](../spec/README.md) • [All Domains](../index.md)*
   ```
   Or, for a simpler back-link:
   ```
   [← Back to Domain Name](../spec/README.md)
   ```

---

## Recursion Anchor

For bootstrap-level equipment (lathe, mill, drill press), cross-reference [iterative-bootstrap.md](../machine-tools/iterative-bootstrap.md) rather than duplicating the construction sequence. The iterative bootstrap is the canonical reference for the Gingery-style machine tool chain. Equipment articles for these machines should describe the machine's capabilities and operation, not the bootstrap construction steps themselves.

---

## Hand Tools Threshold

Items constructible in <5 steps from raw materials with no precision requirements get a named section within the parent article, not a standalone article. Examples:

- **Clay crucible**: knead clay, form around mandrel, dry, fire. (4 steps, no precision) → section in [pottery.md](../ceramics/pottery.md)
- **Wooden mallet**: select hardwood block, bore handle hole, insert handle, wedge. (4 steps, no precision) → section in [tools-basic.md](../foundations/tools-basic.md)
- **Forge tongs**: forge two matching halves, rivet at pivot, dress jaws. (5 steps, low precision) → section in [forging.md](../metals/forming.md)

The threshold is deliberately conservative. When in doubt, write a standalone article — it can always be collapsed into a section later.

---

## Minor Item Template (Short Form)

For items that need more detail than a paragraph but don't warrant the full template:

```markdown
### Item Name

**Principle**: One-sentence description of what it does and how.

**Materials**:
- [Material](../path/to/source.md) — X units, specification

**Construction**:
1. Step one with dimensions.
2. Step two.
3. Step three.

**Performance**: X capacity, Y accuracy, Z lifetime.
```

This short form is appropriate for named sections within a parent capability article.

---

## Worked Example: Hydraulic Press

The following example demonstrates every required and optional section applied to a hypothetical hydraulic press article. This is a complete model — not a stub.

---

```markdown
# Hydraulic Press

> **Node ID**: machine-tools.hydraulic-press
> **Domain**: [Machine Tools](../spec/README.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/index.md), [`energy.hydraulics`](../water/positive-displacement-pump.md)
> **Enables**: [`metals.forming`](../metals/forming.md), [`chemistry.pressure-vessels`](../chemistry/reactor-vessel.md)
> **Timeline**: Years 15-25
> **Outputs**: formed_parts, stamped_parts, compressed_assemblies
> **Critical**: No — mechanical screw presses and fly presses can substitute for many operations, but the hydraulic press is the only practical route for high-force, slow-speed forming

## Principle

A hydraulic press uses Pascal's law — pressure applied to a confined fluid transmits equally in all directions — to multiply a small input force into a large output force. A small-diameter pump cylinder pressurizes hydraulic oil, which acts on a large-diameter ram cylinder. The force multiplication equals the ratio of ram area to pump area: F_out = F_in × (A_ram / A_pump). A typical shop press with a 200 mm diameter ram and a 20 mm diameter pump cylinder multiplies force 100×. The press produces controllable force at low speed, making it ideal for forming, pressing bearings, stamping, and laminating.

## Prerequisites

- [Steel plate](../metals/iron-steel.md) — for frame, bed, and ram (minimum 10 mm thick for structural members)
- [Seamless steel tubing](../metals/forming.md) — for hydraulic cylinder bore (or bored solid bar)
- [Hydraulic seals](../polymers/rubber.md) — O-rings, U-cup seals (nitrile or polyurethane)
- [Hydraulic oil](../chemistry/lubricants.md) — ISO VG 32 or 46 (or filtered vegetable oil as substitute)
- [Pressure gauge](../measurement/temperature-pressure.md) — 0-30 MPa range
- [Hand pump or powered pump](../water/positive-displacement-pump.md) — rated to 20+ MPa
- [Machining capability](../machine-tools/index.md) — for boring cylinder, machining ram, and facing mating surfaces

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (frame) | 100-200 kg | A36 or equivalent, 12-25 mm thick | [Iron & Steel](../metals/iron-steel.md) | Cast iron frame (heavier, no welding needed) |
| Steel bar (ram) | 20-50 kg | 1045 or 4140, 80-150 mm diameter, hardened to 45-50 HRC | [Iron & Steel](../metals/iron-steel.md) | Ground and polished mild steel (shorter life) |
| Seamless tubing (cylinder) | 5-15 kg | honed ID, 80-150 mm bore, 10 mm wall | [Forming](../metals/forming.md) | Bored solid bar (more machining) |
| Hydraulic seals | 1 set | U-cup or O-ring, matched to bore diameter | [Elastomers](../polymers/rubber.md) | Leather cup packing (lower pressure limit, ~7 MPa) |
| Hydraulic oil | 10-30 L | ISO VG 32 or 46, filtered to 25 μm | [Lubricants](../chemistry/lubricants.md) | Filtered vegetable oil (degrades faster) |
| Pressure gauge | 1 | 0-30 MPa, Bourdon tube type | [Measurement](../measurement/temperature-pressure.md) | None — pressure indication is safety-critical |
| Bolts and nuts | 2-5 kg | Grade 8.8 or higher, M12-M20 | [Fasteners](../metals/steelmaking.md) | Riveted joints (non-adjustable) |
| Welding consumables | 5-10 kg | E7018 electrodes or equivalent | [Joining](../machine-tools/welding-equipment.md) | Bolted flanges (heavier) |

## Construction Steps

### Frame

1. **Cut frame plates**: Cut two side plates (500 × 800 mm, 15 mm thick) and a bed plate (400 × 500 mm, 25 mm thick) from steel plate using a torch or saw. A C-frame design uses a single side with a deep throat; an H-frame uses two side plates with tie rods.
2. **Machine mating surfaces**: Mill the top and bottom faces of the side plates flat and parallel to 0.05 mm. The ram guide bore (if integrated into the frame) must be bored perpendicular to the bed within 0.02 mm per 100 mm.
3. **Weld or bolt frame**: For an H-frame press, weld the side plates to the bed plate with full-penetration fillet welds (E7018, 3.2 mm electrode). Alternatively, use bolted flanges with Grade 8.8 bolts for disassembly. Reinforce corners with gusset plates (10 mm, triangular, 100 mm legs).
4. **Install tie rods** (H-frame): Thread four tie rods (M20, 500-600 mm long) through the side plates. Tighten nuts alternately and evenly to 300 N·m. The tie rods preload the frame to resist the working force without joint separation.

### Cylinder and Ram

5. **Prepare cylinder bore**: If using seamless tubing, hone the bore to a 0.8 μm Ra finish or better. If boring from solid bar, bore to diameter, then hone. The bore must be round within 0.02 mm and straight within 0.05 mm over the full stroke length.
6. **Machine ram**: Turn the ram from 1045 or 4140 steel bar. Diameter is 0.05-0.10 mm smaller than the cylinder bore (clearance fit for the seal). Surface finish: 0.4 μm Ra or better (polished). Hardened to 45-50 HRC for wear resistance.
7. **Install seals**: Fit U-cup seals into the cylinder head (gland nut). Seal orientation: cup faces the pressure side. Install O-ring in the gland nut for static seal between cylinder head and cylinder body. Coat all seals with hydraulic oil before assembly.
8. **Assemble cylinder**: Insert ram into cylinder bore through the gland nut. Thread gland nut into cylinder body (or bolt on). The ram should slide smoothly under hand pressure with no binding.

### Hydraulic System

9. **Mount cylinder**: Bolt the cylinder to the top of the frame (H-frame) or the upper cross-member (C-frame). Align the ram axis perpendicular to the bed within 0.1 mm per 100 mm using a machinist's square.
10. **Connect pump**: Connect the hand pump (or power unit) to the cylinder via hydraulic hose rated to at least 1.5× the maximum working pressure. Install a pressure gauge in the line between pump and cylinder.
11. **Fill and bleed**: Fill the reservoir with filtered hydraulic oil. Cycle the pump 10-20 times with the ram unloaded to purge air from the system. Air in the system causes spongy feel and erratic force.

### Safety Features

12. **Install pressure relief valve**: Set to 110% of the rated maximum pressure. This prevents overloading the frame or bursting the cylinder. Verify by pumping to relief pressure and confirming the gauge reading.
13. **Add stroke limiter**: Install adjustable mechanical stops to prevent the ram from over-traveling. This protects the bed and workpiece from damage.

## Calibration and Verification

1. **Force calibration**: Place a calibrated load cell (or a known-weight test) between the ram and bed. Pump to the relief valve set pressure. Record the gauge reading and the measured force. Calculate the effective ram area: F = P × A. Verify the force matches the design calculation within ±5%.
2. **Parallelism check**: Place a precision straightedge across the bed. Lower the ram until it contacts the straightedge at two points. Measure gap between ram face and straightedge at four corners. Maximum deviation: 0.05 mm per 100 mm of ram face width. Adjust frame or shim as needed.
3. **Pressure test**: Pump to 1.25× the rated working pressure with no load. Hold for 10 minutes. Inspect all connections, seals, and welds for leaks. Zero leaks acceptable.
4. **Stroke test**: Cycle the ram through full stroke 20 times unloaded, then 10 times at 50% rated force. Verify smooth operation with no jerking, binding, or pressure drift.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Maximum force (20 MPa, 150 mm ram) | 350 kN (35 tonnes) |
| Maximum force (20 MPa, 100 mm ram) | 155 kN (16 tonnes) |
| Stroke length | 150-300 mm (design-dependent) |
| Ram speed (hand pump) | 5-20 mm/sec |
| Ram speed (powered pump, 5 L/min) | 0.5-2 mm/sec at full force |
| Frame deflection at rated load | <0.5 mm (H-frame), <1.0 mm (C-frame) |
| Bed flatness | ±0.05 mm |
| Hydraulic system pressure | 10-20 MPa (typical) |
| Duty cycle | Intermittent — 10 min on, 5 min off (thermal limit on pump) |
| Seal life | 6-12 months continuous use; inspect monthly |

## Strengths

- Enormous force in a compact frame — 35 tonnes from a 150 mm ram at 20 MPa
- Force is controllable and repeatable via pressure gauge — unlike a hammer or fly press
- Slow, steady motion avoids shock loading — suitable for delicate operations (bearing pressing, laminating)
- Simple hydraulic circuit — hand pump, cylinder, relief valve. No complex electronics required

## Weaknesses

- Slow operating speed — hydraulic presses are for high-force, low-speed work, not high-throughput stamping
- Hydraulic oil leaks are inevitable over time — seals wear, hoses age. Oil on the floor is a slip hazard
- Frame must be massively overbuilt — a 35-tonne press frame experiences 35 tonnes of force trying to spread it apart. Welds and tie rods must be sized accordingly
- Not suitable for impact forming — the slow ram speed means workpieces strain-rate harden rather than flow

## Safety

- **Pinch points**: The ram-to-bed gap is the primary hazard. Never place hands in the working zone. Use tongs, pliers, or jigs to position workpieces. Install two-hand anti-tie-down controls on powered presses.
- **Hydraulic injection**: Hydraulic oil at 20+ MPa can penetrate skin through a pinhole leak. Injection injuries require immediate surgical debridement — they do not heal on their own. Never use hands to search for leaks; use a piece of cardboard or paper.
- **Frame failure**: An overloaded frame can fail catastrophically, releasing stored energy from the pressurized oil. Never exceed rated force. Verify pressure relief valve function monthly.
- **Oil fire hazard**: Hydraulic oil ignites at 300-400°C if atomized (spray leak onto hot surface). Keep ignition sources away from hydraulic systems. Have a Class B fire extinguisher within 10 m.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Ram will not extend | Air lock in hydraulic line, or pump check valve stuck | Bleed air from system at the highest point; disassemble and clean pump check valve |
| Ram drifts down under load | Seal leak (internal bypass) or relief valve set too low | Inspect and replace cylinder seals; verify relief valve setting with gauge |
| Jerky ram motion | Air in system or contaminated oil | Re-bleed the system; drain and filter oil; replace if discolored or burnt-smelling |
| Insufficient force | Pump worn, pressure too low, or ram seal bypassing | Verify gauge pressure reaches rated value; test pump flow rate; inspect cylinder seals |
| Oil leaking from gland nut | Ram seal worn or gland nut loose | Tighten gland nut; if leak persists, replace U-cup seal (scheduled maintenance item) |

## Variations and Alternatives

- **C-frame vs. H-frame**: C-frame (open throat) allows loading wide workpieces from the side. H-frame (four-column) provides higher rigidity and parallelism. Choose H-frame for precision forming; C-frame for general-purpose shop use.
- **Hand pump vs. powered pump**: Hand pump is simpler, cheaper, and independent of power supply. Powered pump (electric motor + gear pump) enables faster cycling and consistent force. A powered press produces the same force but much faster throughput.
- **Screw press alternative**: A mechanical screw press uses a threaded shaft instead of hydraulics. Simpler (no oil, no seals) but force is less controllable and the mechanical advantage is lower. Suitable for light press work (<10 tonnes).
- **Fly press alternative**: A fly press stores energy in a rotating mass (the flywheel) and delivers it as an impact. Faster cycle time than hydraulic but less controllable force. Best for punching, bending, and coining.

## See Also

- [Iterative Machine Bootstrap](../machine-tools/iterative-bootstrap.md) — the bootstrap sequence that produces machine tools
- [Machining](../machine-tools/index.md) — cutting operations for cylinder and ram components
- [Forming](../metals/forming.md) — metal forming operations that use presses
- [Hydraulics](../water/positive-displacement-pump.md) — hydraulic power systems, fluid selection, pump types
- [Measurement / Pressure](../measurement/temperature-pressure.md) — pressure gauges and calibration
- [Joining](../machine-tools/welding-equipment.md) — welding and bolted joint design for the frame

---

*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](../spec/README.md) • [All Domains](../index.md)*
```

---

## Anti-Patterns

- **No YAML frontmatter**: The project uses blockquote-style metadata exclusively.
- **No unlinked references**: Every prerequisite and material must link to its source doc.
- **No unitless numbers**: Every quantitative value needs a unit.
- **No vague performance claims**: "High pressure" → "20 MPa". "Very accurate" → "±0.05 mm parallelism".
- **No hand-editing of auto-generated files**: Mermaid (`.mmd`) and D2 (`.d2`) files are regenerated by `make diagrams`. Never edit them directly.
- **No external URLs in the main body**: External references go in a References section only.
- **No recursion in bootstrap articles**: Link to [iterative-bootstrap.md](../machine-tools/iterative-bootstrap.md) instead of re-describing the Gingery sequence.

---

## Exemplar Files

These existing articles demonstrate the equipment construction standard:

| File | Lines | Strengths |
|------|-------|-----------|
| [Kilns](../ceramics/kilns.md) | 618 | Gold standard for equipment articles. Six kiln types, each with Principle/Materials/Procedure/Calibration/Performance/Strengths/Weaknesses. Comparison table. Quantitative throughout. |
| [Electric Furnaces](../energy/electric-furnaces.md) | 250 | Three furnace families (EAF, SAF, resistance), each with construction detail and operating parameters. Power requirements with units. |
| [Blast Furnace](../metals/blast-furnace.md) | 246 | Full construction and operation detail. BOM embedded in prose. Temperature zones, production rates, gas chemistry. |
| [Iterative Bootstrap](../machine-tools/iterative-bootstrap.md) | 245 | Canonical reference for the machine tool chain. Precision milestones table, timeline estimates, materials per level. |

Study the kilns article first. It demonstrates every section described in this template applied across six equipment variants.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Supporting Docs](./) • [All Domains](../index.md)*
