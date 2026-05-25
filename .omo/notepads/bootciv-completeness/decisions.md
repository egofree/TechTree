# Decisions Log

## 2026-05-24: Electronics Domain — Standalone (not folded into Computing)

**Context:** docs/electronics/ had 2 orphaned content files (assembly.md, electrical-systems.md) with no nodes in nodes.json and no index.md.

**SIK Placement Test (schema-spec.md §6) applied:**

| Dimension | Electronics vs Computing | Threshold | Pass? |
|-----------|-------------------------|-----------|-------|
| Infrastructure overlap | ~15% (PCB fab, reflow ovens vs logic design tools) | >50% | No |
| Knowledge overlap | ~20% (soldering metallurgy, ESD control vs Boolean algebra) | >50% | No |
| Practitioner overlap | ~15% (assembly technicians vs computer architects) | >50% | No |

**Result:** All three dimensions below 50%. Electronics is a **standalone domain**.

**Justification:** Electronics assembly has completely distinct physical infrastructure (PCB fabrication lines, reflow ovens, pick-and-place machines, wave soldering), distinct knowledge base (PCB design rules, soldering metallurgy, conformal coating chemistry, ESD control), and distinct practitioners (PCB designers, soldering technicians, quality engineers). Computing focuses on logical architecture, programming, and algorithm design — an entirely different discipline.

**Minimum domain size:** 2 capabilities (assembly, electrical-systems) with 435 lines of substantive content. Exceeds minimum threshold.

**Organizing axis:** Functional — capabilities grouped by function (assembly of electronic systems vs. distribution of electrical power).

## 2026-05-24: Vacuum Technology Domain — Standalone (not merged with Gas-Handling)

**Context:** Vacuum content existed as a 215-line file at `docs/gas-handling/vacuum.md` with a capability node `gas-handling.vacuum`. Task: evaluate whether vacuum warrants its own domain.

**SIK Placement Test (schema-spec.md §6) applied:**

| Dimension | Vacuum vs Gas-Handling | Threshold | Pass? |
|-----------|----------------------|-----------|-------|
| Infrastructure overlap | ~25% (pumps, chambers, CF flanges vs regulators, MFCs, gas cabinets) | >50% | No |
| Knowledge overlap | ~30% (shared gas physics basics, but vacuum has deep UHV specialties) | >50% | No |
| Practitioner overlap | ~20% (vacuum engineers vs gas distribution/safety engineers) | >50% | No |

**Result:** All three dimensions below 50%. Vacuum Technology is a **separate domain**.

**Justification:** Vacuum engineering has completely distinct physical infrastructure (vacuum pumps, turbomolecular pumps, cryopumps, ion pumps, vacuum chambers, CF flanges, gate valves, viewports, RGAs, helium leak detectors), distinct knowledge base (kinetic theory, molecular flow regimes, outgassing physics, bake-out procedures, UHV sealing techniques, vacuum hygiene protocols), and distinct practitioners (vacuum engineers, leak detection specialists, UHV system designers). Gas handling focuses on positive-pressure gas distribution, purification, and safety — a fundamentally different discipline. The existing gas-handling/vacuum.md remains as a foundational reference.

**Minimum domain size:** 3 capabilities (pumps, chambers, measurement) with 664 lines of substantive content. Exceeds minimum threshold.

**Organizing axis:** Functional — capabilities grouped by vacuum system function (pumping systems, chamber design and sealing, measurement and diagnostics).

## 2026-05-25: Ultra-Pure Materials Domain — Standalone (not merged with Chemistry or Water)

**Context:** Semiconductor manufacturing requires 99.9999999% (9N) purity chemicals and 18.2 MΩ·cm water. Standard industrial chemistry produces 95-99.5% purity. This is a fundamentally different engineering discipline requiring distinct infrastructure, knowledge, and practitioners.

**SIK Placement Test (schema-spec.md §6) applied:**

### Ultra-Pure Materials vs Chemistry

| Dimension | Ultra-Pure vs Chemistry | Threshold | Pass? |
|-----------|------------------------|-----------|-------|
| Infrastructure overlap | ~15% (cleanrooms, PFA piping, sub-micron filters vs distillation columns, reactors, bulk storage) | >50% | No |
| Knowledge overlap | ~20% (ppt-level contamination physics, TOC analysis, ICP-MS vs bulk synthesis, % purity, reaction kinetics) | >50% | No |
| Practitioner overlap | ~15% (ultra-pure water specialists, cleanroom process engineers vs industrial chemists, plant operators) | >50% | No |

### Ultra-Pure Materials vs Water Infrastructure

| Dimension | Ultra-Pure vs Water | Threshold | Pass? |
|-----------|-------------------|-----------|-------|
| Infrastructure overlap | ~20% (RO membranes used in both, but ultra-pure adds mixed-bed DI, UV, ozonation, sub-micron filtration, cleanroom distribution) | >50% | No |
| Knowledge overlap | ~15% (basic water chemistry shared, but ultra-pure requires semiconductor contamination physics, trace metal analysis at ppt levels) | >50% | No |
| Practitioner overlap | ~10% (ultra-pure process engineers vs civil/water engineers) | >50% | No |

**Result:** All dimensions below 20% for both comparisons. Ultra-Pure Materials is a **standalone domain**.

**Justification:** Ultra-pure materials production represents a qualitatively different engineering discipline from both standard industrial chemistry and municipal water treatment. The purity gap is enormous — standard chemistry produces 95-99.5% purity (2-3N), while semiconductor fabrication demands 9N+ (99.9999999%) for chemicals and 18.2 MΩ·cm resistivity for water. This 6-7 order of magnitude difference in impurity tolerance requires:

1. **Distinct infrastructure**: Cleanroom-class facilities (ISO 4-6), PFA/PTFE piping systems, sub-micron membrane filtration, UV/ozonation systems, dedicated storage in fluoropolymer vessels — none of which exist in standard chemical plants or water treatment facilities.
2. **Distinct knowledge base**: Part-per-trillion (ppt) contamination physics, total organic carbon (TOC) analysis, inductively coupled plasma mass spectrometry (ICP-MS), trace metal speciation, dissolved oxygen control at ppb levels, bacterial endotoxin management.
3. **Distinct practitioners**: Ultra-pure water system engineers, cleanroom contamination control specialists, trace analytical chemists — these are semiconductor-industry roles, not industrial chemistry or civil engineering roles.

The existing [Water Treatment](../water/sem-tech-water-treatment.md) document covers ED desalination for brackish water to drinking water standards (<500 mg/L TDS). The existing [Solvents](../chemistry/solvents.md) document covers industrial solvents at ACS reagent grade (~99.5%). Neither addresses the 9N+ purity regime required for semiconductor wafer processing.

**Minimum domain size:** 3 capabilities (ultra-pure water, high-purity chemicals, analytical verification) exceeding 600 lines of substantive content. Exceeds minimum threshold.

**Organizing axis:** Process Chain — capabilities ordered by the material flow from water purification through chemical purification to analytical verification of purity levels.
