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
