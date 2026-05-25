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
