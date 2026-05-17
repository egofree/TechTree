# Continuous Scaling

> **Node ID**: `vlsi-scaling.continuous-scaling`
> **Domain**: [VLSI Scaling & Advanced Semiconductor](./)
> **Dependencies**: `photolithography.fab-processes`
> **Timeline**: Years 70-200+
> **Outputs**: larger_wafers, finer_features, higher_yield

### Continuous Scaling

The progression from the Photolithography stage's first ICs to the VLSI Scaling stage's complex chips follows Moore's Law-like scaling — each generation doubles transistor count, shrinks features, and improves yield.

**Wafer size progression**:
| Wafer Size | Area | Typical Era | Key Challenge |
|-----------|------|-------------|---------------|
| 2" (50 mm) | ~20 cm² | First ICs | Handling, uniformity |
| 4" (100 mm) | ~79 cm² | 1970s | Crystal growth scale |
| 6" (150 mm) | ~177 cm² | 1980s | Equipment scaling |
| 8" (200 mm) | ~314 cm² | 1990s | Flatness, process uniformity |
| 12" (300 mm) | ~707 cm² | 2000s | Cost, automation requirement |

Each jump requires: larger crystal pullers, bigger processing equipment, more material throughput, and better process uniformity across the wafer. Transition only when yield at current size justifies the capital investment.

**Feature size progression**:
| Node | Gate Length | Lithography | Challenges |
|------|-----------|-------------|------------|
| 10 μm | ~10 μm | Contact/proximity | Basic alignment |
| 3 μm | ~3 μm | Projection (1:1) | Overlay accuracy ±0.5 μm |
| 1 μm | ~1 μm | Step-and-repeat (5:1) | Phase-shift masks, OPC |
| 0.35 μm | ~0.25 μm | DUV KrF (248 nm) | Deep UV resist chemistry |
| 0.13 μm | ~0.07 μm | DUV ArF (193 nm) | Immersion lithography |
| 7 nm | ~7 nm | EUV (13.5 nm) | Everything is hard |

**Metal layer progression**:
- 1-2 layers: Simple logic (SSI-MSI)
- 3-4 layers: Microprocessors (LSI)
- 6-8 layers: Complex SoCs (VLSI)
- 10+ layers: Modern GPUs, CPUs
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
