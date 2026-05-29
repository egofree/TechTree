# Technical Drawing

> **Node ID**: knowledge.technical-drawing
> **Domain**: [Knowledge Preservation & Education](./index.md)
> **Dependencies**: [`knowledge.writing`](writing.md), [`knowledge.printing`](printing.md), [`measurement`](../measurement/index.md)
> **Enables**: [`knowledge.standards-bodies`](standards-bodies.md)
> **Timeline**: Years 5-50+
> **Outputs**: engineering_drawings, blueprints, assembly_diagrams
> **Critical**: Yes — without standardized drawing conventions, no two workshops can exchange manufacturing specifications

## Overview

Technical drawing is the graphical language of engineering. It translates three-dimensional objects and assemblies into unambiguous two-dimensional representations that any trained reader can interpret to manufacture the described part exactly as designed. A machinist who has never met the designer must produce a part that fits precisely with parts made in other workshops — the engineering drawing is the contract between design intent and manufactured reality.

This capability covers manual drafting (pencil, ink, T-square, compass) as the bootstrap entry point, and the conventions that make drawings universally readable: projection methods, dimensioning systems, line types, section views, tolerances, and title blocks. The transition to computer-aided design (CAD) occurs later in the bootstrap sequence and requires [Computing](../computing/index.md) infrastructure. The drawing conventions themselves are technology-independent — the same standards apply whether the drawing is made with a pencil or a computer.

## Prerequisites

- **Materials**: Drawing paper (smooth, dimensionally stable — vellum or kraft paper), pencils (H through B grades), ink ([Writing](writing.md))
- **Tools**: T-square or parallel straightedge, set square (30-60-90° and 45°), compass, dividers, ruling pen, protractor, French curves, eraser, drawing board
- **Knowledge**: Geometry (planar constructions, projection theory), arithmetic, basic algebra, [Measurement](../measurement/precision-metrology.md) systems (units, tolerances)
- **Infrastructure**: Drawing board (minimum A2 size: 420 × 594 mm), well-lit drafting station, flat storage for finished drawings

## Bill of Materials

| Material | Quantity per Drawing | Source | Alternatives |
|----------|---------------------|--------|-------------|
| Drawing paper (A2) | 1-3 sheets | [Printing](printing.md) | Vellum (more durable, more expensive) |
| Pencils (HB, 2H, 4H) | Consumable — resharpen every 2-3 drawings | [Metals](../metals/index.md) (graphite-clay composite) | Charcoal stick (lower precision) |
| Ink (India/carbon) | 5-10 mL per inked drawing | [Writing](writing.md) | Pencil-only drawings (lower reproducibility) |
| Drafting tape | 4-8 strips per sheet | [Chemistry](../chemistry/index.md) (adhesive) | Pins (damages paper) |
| Eraser (rubber/art gum) | Consumable | [Polymers](../polymers/index.md) | Bread crumbs (historical eraser) |

## Process Description

### Manual Drafting Procedure

1. **Mount paper**: Tape drawing paper to board at all four corners with drafting tape. Verify T-square rides flat across the full sheet width.
2. **Layout border and title block**: Draw border rectangle 10-15 mm from all edges. Draw title block in lower right corner (typical size: 180 × 56 mm for A2 sheet). Title block fields: part name, drawing number, scale, date, drawn-by, checked-by, material, tolerances, revision letter.
3. **Plan views**: Determine which views are needed to fully describe the part. Minimum: two orthographic views (front + top or side). Complex parts require three views plus auxiliary or section views.
4. **Construct geometry in pencil**: Using light construction lines (4H pencil, ~0.1 mm line weight), lay out the views to scale. Start with centerlines (long-dash-short-dash), then outline visible edges, hidden edges, and surfaces.
5. **Dimension**: Add dimension lines, extension lines, and arrowheads. Place dimensions to avoid crossing other lines. Use standard dimensioning conventions: linear dimensions in mm, angular in degrees, tolerances on all critical dimensions.
6. **Add annotations**: Surface finish symbols, welding symbols, material callouts, heat treatment specifications, notes.
7. **Check**: Verify all dimensions are present, no double-dimensioning (same dimension stated twice — creates tolerance conflicts), all features are fully defined (not under- or over-constrained).
8. **Ink (if required)**: Trace pencil lines with ruling pen and India ink. Line weights: visible outlines 0.5-0.7 mm, hidden lines 0.3-0.35 mm, centerlines and dimension lines 0.18-0.25 mm. Allow ink to dry fully before erasing pencil construction lines.
9. **Review and release**: Checker reviews drawing against design intent. Approved drawings receive a revision letter and are logged in the drawing register.

**Strengths**:
- Manual drafting requires no powered equipment — a drawing board, T-square, pencils, and ink suffice for producing complete engineering drawings
- Nine-step procedure is fully defined — a trained drafter can produce a complete, unambiguous drawing without consulting the designer
- Standardized title block (part name, drawing number, scale, tolerances, revision) provides all metadata needed for filing and retrieval

**Weaknesses**:
- A skilled drafter produces only 2-5 finished drawings per week for moderately complex parts — slower than CAD by 3-10×
- Inking requires steady hand and careful technique — errors in ink require scraping with a knife and re-drawing, unlike pencil which erases cleanly
- Paper is dimensionally unstable — humidity changes cause expansion/contraction that can shift dimensions by 0.1-0.5 mm on large sheets

### Section View Construction

When internal features cannot be shown clearly with hidden lines, cut the imaginary object along a plane and draw the exposed interior. Section views use hatching (parallel lines at 45°, 2-4 mm spacing) to indicate cut material. Different materials use different hatch patterns: steel (45° parallel lines), cast iron (45° lines with alternating dots), copper alloys (45° lines alternating direction), and wood (grain pattern). Label the cutting plane with letters (A-A, B-B) and annotate the section view accordingly.

**Strengths**: Reveals internal geometry (bores, chambers, wall thickness) that hidden lines cannot show clearly. Material-specific hatch patterns convey additional information without labels.

**Weaknesses**: Incorrect section plane selection can obscure rather than clarify — the drafter must understand which internal features are most important to show. Hatching adds significant drawing time for complex multi-part assemblies.

### Dimensioning Rules

Follow these rules to produce unambiguous dimensioned drawings:
- Dimension to visible outlines, never to hidden lines (hidden lines represent uncertain geometry).
- Place dimensions outside the view where possible, connected by extension lines.
- Do not cross dimension lines with other dimension lines. If crossing is unavoidable, break one line.
- Stagger parallel dimension lines so arrowheads do not align vertically (prevents misreading).
- Dimension from a common datum (one edge or feature) rather than chain-dimensioning (each dimension from the previous), to avoid tolerance accumulation.
- Include a general tolerance note in the title block for dimensions without explicit tolerances (e.g., "General tolerances: ±0.5 mm linear, ±1° angular").

**Strengths**: Datum-based dimensioning (all dimensions from a common reference) eliminates tolerance accumulation — worst-case stack-up equals the single largest tolerance, not the sum of all tolerances. General tolerance note covers all dimensions that don't need explicit tolerances, reducing drawing clutter.

**Weaknesses**: Dimension placement is the most time-consuming part of drafting — a complex part with 50+ dimensions requires careful planning to avoid crossing lines and crowding. Dimensioning errors (double-dimensioning, missing dimensions) are the most common drawing defect found during checking.

## Quantitative Parameters

### Standard Sheet Sizes (ISO A-series)

| Size | Dimensions (mm) | Typical Use |
|------|-----------------|-------------|
| A0 | 841 × 1189 | Master assembly drawings, large-scale site plans |
| A1 | 594 × 841 | General arrangement drawings, large part drawings |
| A2 | 420 × 594 | Most mechanical part drawings, process flow diagrams |
| A3 | 297 × 420 | Small parts, detail drawings, workshop reference copies |
| A4 | 210 × 297 | Sketches, parts lists, small component drawings |

### Line Type Specifications

| Line Type | Style | Weight (mm) | Application |
|-----------|-------|-------------|-------------|
| Continuous thick | ———— | 0.5-0.7 | Visible outlines, borders |
| Continuous thin | ———— | 0.18-0.25 | Dimension lines, extension lines, hatching |
| Dashed thick | — — — — | 0.5-0.7 | Hidden outlines (alternative convention) |
| Dashed thin | — — — — | 0.18-0.25 | Hidden outlines (standard) |
| Chain thin | —·—·— | 0.18-0.25 | Centerlines, lines of symmetry |
| Chain thin-double-dash | —··—··— | 0.18-0.25 | Outlines of adjacent parts (context) |
| Wavy thin | ~~~~~~ | 0.18-0.25 | Break lines (long uniform sections) |

### Standard Scale Ratios

| Category | Ratios | Application |
|----------|--------|-------------|
| Full size | 1:1 | Small parts, detail features |
| Reduction | 1:2, 1:5, 1:10, 1:20, 1:50, 1:100 | Most mechanical drawings |
| Enlargement | 2:1, 5:1, 10:1 | Small features, watchmaking, instrument parts |
| Preferred | 1:1, 1:2, 1:5, 1:10, 1:20, 1:50 | Use first; avoid odd scales |

### Dimensioning Tolerance Classes

| Tolerance Class | Tolerance (mm) | Typical Application | Manufacturing Method |
|----------------|----------------|--------------------|--------------------|
| Very coarse | ±1.0 | Structural steel, castings | Cutting, rough machining |
| Coarse | ±0.5 | General engineering | Drilling, milling |
| Medium | ±0.1 | Fitted parts, shafts | Turning, milling |
| Fine | ±0.05 | Bearings, precision fits | Precision turning, grinding |
| Very fine | ±0.01 | Gauge blocks, instrument parts | Grinding, lapping |
| Ultra-fine | ±0.005 or less | Semiconductor tooling | Lapping, honing, polishing |

## Scaling Notes

- **Minimum viable drafting**: One drawing board, one set of instruments, one trained drafter can produce 2-5 finished drawings per week for moderately complex parts. A small workshop needs ~50-100 unique part drawings to document its product line.
- **Blueprint reproduction**: Once a master drawing exists, it can be reproduced via blueprint process (ferroprussiate paper, UV exposure — requires chemistry capability) or by manual tracing. Blueprinting produces 10-50 copies per hour, enabling distribution of the same drawing to multiple workshops.
- **CAD transition**: Computer-aided drafting (requires [Computing](../computing/index.md) and display technology) increases drawing production speed by 3-10× and enables parametric design, but the underlying conventions (projection, dimensioning, tolerancing) remain identical. CAD is a productivity multiplier, not a conceptual replacement.
- **Drawing management**: For more than 100 unique drawings, implement a numbering system and drawing register. Drawing number format: domain-series-sequence (e.g., M-001-042 = Machine Tools, Series 001, Drawing 042). Revision control: every change increments the revision letter (A → B → C).
- **Assembly drawings**: For multi-part assemblies, produce a separate assembly drawing showing all components in their assembled positions with item numbers (balloon references). Include a parts list (bill of materials) on the drawing or on an attached sheet, listing: item number, part name, quantity required, material, and drawing number of each component. An assembly drawing enables a workshop to produce all parts and fit them together without the designer present.
- **Reproduction methods**: Blueprints (ferroprussiate process: UV-sensitive paper exposed through translucent original, developed in water — produces white lines on blue background) allow rapid distribution. One master drawing can produce 50-100 blueprint copies per hour with sunlight exposure. Alternative: diazo process (ammonia-developed, white lines on dark background — requires chemical supply).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Drawings misinterpreted by shop | Ambiguous projection method, unclear dimensioning | Standardize on one projection method (third-angle recommended); use unambiguous dimension placement |
| Parts don't fit together | Tolerances too loose, or tolerance stack-up not analyzed | Assign tolerances based on manufacturing method capability; analyze worst-case tolerance stack-ups for mating parts |
| Drawing crowded and unreadable | Too many dimensions in one view, poor view selection | Move dimensions to the clearest view; add auxiliary views for complex features; use enlarged detail views |
| Scale error in reproduction | Paper shrinks/stretches with humidity, or reproduction distortion | Draw scale reference bar on each sheet; verify scale after reproduction; use dimensionally stable media |
| Dimension conflict | Same feature dimensioned twice with different values | Check for double-dimensioning during review; one dimension per feature, one tolerance |
| Outdated drawing used in production | No revision control system | Implement drawing register with revision history; withdraw and destroy superseded drawings; color-code current revisions |

## Safety

- **Eye strain**: Prolonged close work at a drawing board causes eye fatigue. Follow the 20-20-20 rule: every 20 minutes, look at something 20 feet (6 m) away for 20 seconds. Ensure drafting station lighting is 500-750 lux, shadow-free.
- **Ink solvents**: Some drawing inks contain volatile solvents (alcohol, xylene). Use in well-ventilated areas. Cap ink bottles when not in use.
- **Sharp instruments**: Compass points, ruling pen blades, and drawing knives are sharp. Store in protective cases. Cut away from the body when trimming paper or using cutting tools.
- **Repetitive strain**: Prolonged drafting with poor posture causes wrist and shoulder strain. Adjust board angle to 15-30° from horizontal. Support forearm on the board edge. Take 5-minute breaks every hour.

## Quality Control

- **Completeness check**: Every drawing must fully define the part geometry, dimensions, tolerances, material, surface finish, and any required processing (heat treatment, coating). A machinist should be able to produce the part from the drawing alone, without asking the designer questions.
- **Accuracy check**: Verify all dimensions against the design calculation. Check arithmetic for derived dimensions. Verify that tolerances are achievable with the specified manufacturing method.
- **Standard compliance**: Verify drawing conforms to the adopted standard (projection method, dimensioning style, line types, title block format). Non-standard drawings cause confusion and errors.
- **Peer review**: Every drawing is checked by a second person before release. The checker uses a different color pencil to mark corrections. The original drafter incorporates all corrections before final approval.

## Variations and Alternatives

### First-Angle vs. Third-Angle Projection

Two conventions exist for arranging orthographic views on the sheet. Third-angle (used in North America, increasingly global standard): the top view is placed above the front view, the right-side view to the right. First-angle (European historical): the top view is placed below, the right-side view to the left. Either works; the critical requirement is to standardize on one and label every drawing with the projection symbol (truncated cone).

**Strengths**: Both conventions are equally expressive — once standardized, any trained reader can interpret drawings without ambiguity. The truncated cone projection symbol on each drawing makes the convention explicit, preventing misinterpretation.

**Weaknesses**: Mixing conventions within a single workshop or between trading partners causes manufacturing errors — a part built from first-angle drawings read as third-angle will be mirrored. Switching conventions after adoption requires retraining all drafters and machinists.

### Isometric and Pictorial Views

Orthographic projections are unambiguous but require training to read. Isometric views (30° axes, no foreshortening) and oblique views provide a three-dimensional appearance that helps non-specialists understand the part shape. Use as supplementary views, never as the sole representation for manufacturing — isometric dimensions are distorted and cannot convey tolerances.

**Strengths**: Non-specialists (managers, clients, less-trained workers) can understand the part shape immediately without training in orthographic projection. Useful as assembly instructions alongside orthographic manufacturing drawings.

**Weaknesses**: Isometric dimensions are foreshortened and distorted — dimensions measured from an isometric view are unreliable for manufacturing. Cannot convey tolerances or GD&T requirements.

### Freehand Sketching

Before committing to a formal drawing, designers sketch freehand to explore concepts. Graph paper (5 mm grid) aids proportion. Sketching is faster than formal drawing for iteration — a designer should produce 10-50 sketches for every finished drawing. No instruments required beyond pencil and paper.

**Strengths**: 10-50× faster than formal drawing — enables rapid design iteration before committing to the time investment of a finished drawing. No instruments required — pencil and paper suffice.

**Weaknesses**: Freehand sketches lack dimensional precision — they convey concept but not manufacturing specification. Sketches are not archival quality and fade or smudge over time.

### Drawing Storage and Handling

Engineering drawings are master documents — loss of a master drawing means loss of the design. Storage requirements:
- Flat storage in shallow drawers (never rolled — rolling causes permanent curl and crease damage at fold points).
- Acid-free interleaving paper between drawings to prevent ink transfer.
- Drawing register (numbered log) tracking: drawing number, title, revision, location (drawer number), date received, responsible person.
- Fireproof cabinet or vault for master originals. Day-to-day workshop use employs blueprint copies, not originals.
- Handle originals with clean, dry hands. Never mark on an original drawing with anything other than the official revision stamp.
- Maximum of 50 drawings per drawer to prevent compression damage and enable retrieval within 2 minutes.

### Geometric Dimensioning and Tolerancing (GD&T)

For precision parts, simple ±tolerances are insufficient because they do not control the *geometry* of features — only their size. GD&T provides a symbolic language for controlling:
- **Flatness**: The surface must lie between two parallel planes separated by the tolerance value (e.g., 0.05 mm flatness).
- **Straightness**: A line element on a surface must lie between two parallel lines separated by the tolerance.
- **Parallelism**: One surface must be parallel to a datum surface within the stated tolerance (e.g., 0.02 mm parallel to datum A).
- **Perpendicularity**: One surface must be perpendicular to a datum within the stated tolerance.
- **Concentricity**: The axis of one cylindrical feature must lie within a cylinder of stated diameter centered on the datum axis.
- **Position**: The center of a feature (typically a hole) must lie within a tolerance zone (typically a circle of stated diameter) centered at the true position.

GD&T symbols are placed in a feature control frame (rectangular box) attached to the feature being controlled. The frame contains: the symbol, the tolerance value, and any datum references. While GD&T adds complexity to drawings, it is essential for precision assemblies where geometric relationships between features matter as much as dimensions.

### CAD (Computer-Aided Design)

Replaces manual drafting tools with a computer program. Advantages: parametric models (change one dimension, all related features update automatically), 3D modeling, interference checking, automated dimensioning, instant revision tracking. Requires [Computing](../computing/index.md) hardware, display technology, and software development. The drafting conventions (line types, dimensioning, tolerancing, title blocks) remain identical to manual practice.

### Surface Finish Specification

Surface texture is specified using Ra (roughness average) values in micrometers (μm). The standard machining processes produce characteristic surface finish ranges:

| Process | Typical Ra (μm) | Application |
|---------|-----------------|-------------|
| Flame cutting | 25-50 | Structural steel, rough openings |
| Sawing | 6.3-25 | Stock preparation |
| Drilling | 3.2-6.3 | Clearance holes, non-critical bores |
| Milling (roughing) | 3.2-6.3 | General machining |
| Milling (finishing) | 0.8-3.2 | Bearing surfaces, mating faces |
| Turning (roughing) | 3.2-6.3 | General turning |
| Turning (finishing) | 0.4-1.6 | Shaft bearing journals |
| Grinding | 0.1-0.8 | Precision fits, gauge surfaces |
| Lapping | 0.025-0.1 | Gauge blocks, optical flats |

Surface finish is indicated on drawings with a checkmark symbol (√) followed by the Ra value. The symbol points to the surface being specified. A machining symbol without a number indicates "standard finish" as defined in the title block general note.

## References

- [Writing & Record-Keeping](writing.md) — ink, paper, and writing instruments foundational to drafting
- [Printing & Book Production](printing.md) — paper production and reproduction of drawing standards
- [Measurement](../measurement/precision-metrology.md) — the measurement system that drawing dimensions reference
- [Machine Tools](../machine-tools/index.md) — the primary consumer of engineering drawings
- [Education Pathways](education-pathways.md) — training sequences for draftsmen
- [Standards Bodies](standards-bodies.md) — standardization of drawing conventions
- [Computing](../computing/index.md) — the computing infrastructure needed for CAD transition

---

*Part of the [Bootciv Tech Tree](../index.md) · [Knowledge Preservation & Education](./index.md) · [All Domains](../index.md)*
