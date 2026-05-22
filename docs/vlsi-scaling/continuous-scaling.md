# Continuous Scaling

> **Node ID**: vlsi-scaling.continuous-scaling
> **Domain**: [VLSI Scaling & Advanced Semiconductor](./)
> **Dependencies**: [`photolithography.fab-processes`](../photolithography/fab-processes.md)
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

### Scaling Transition Details

**10 μm → 3 μm (1970s)**: The first shrink. Contact printing gives way to 1:1 projection — a lens images the mask onto the wafer without physical contact, eliminating mask damage. Overlay tolerance relaxes from ±1 μm to ±0.5 μm with basic mechanical alignment stages. Wet etching still adequate. Yield challenge: defect density dominates — even 1 defect/cm² kills most die. Cleanroom discipline (Class 10,000) becomes essential. Equipment: mercury arc lamp sources (g-line 436 nm), basic optical projection lenses.

**3 μm → 1 μm (early 1980s)**: Step-and-repeat reduction projection (5:1) replaces 1:1 projection. A single small, high-quality reticle is stepped across the wafer — far cheaper than full-wafer masks and allows much better resolution. Requires precision wafer stage with interferometric position feedback (~0.1 μm accuracy). Dry (RIE) etching replaces wet etching for anisotropic profiles — critical at 1 μm where undercut becomes unacceptable. I-line (365 nm) sources introduced. Yield challenge: particle control tightens to Class 100-1000.

**1 μm → 350 nm (late 1980s–early 1990s)**: DUV lithography arrives. KrF excimer lasers at 248 nm wavelength enable sub-half-micron features. Chemically amplified resists (CAR) required — conventional novolac/DNQ resists lack sensitivity at DUV wavelengths. Ion implantation fully replaces thermal diffusion for doping (see [Advanced Processes](advanced-processes.md)). CMP enables multi-level metallization by planarizing topography. Yield challenge: gate oxide integrity at ~7 nm SiO₂ thickness — pinholes and breakdown become yield limiters.

**350 nm → 130 nm (mid-late 1990s)**: ArF excimer laser (193 nm) introduced. Shallow trench isolation (STI) replaces LOCOS. Gate oxide thins to ~2 nm — quantum mechanical tunneling leakage begins. Copper replaces aluminum interconnects (see below). 200 mm → 300 mm wafer transition begins. Yield challenge: across-wafer uniformity on 300 mm wafers requires fully automated wafer handling.

**130 nm → 65 nm and below (2000s+)**: Immersion lithography (water between lens and wafer) boosts numerical aperture above 1.0. Gate dielectric hits physical limit — SiO₂ at ~1.2 nm has intolerable leakage (see Gate Dielectric Scaling below). Strained silicon engineering introduced. Multiple patterning (double, quad) extends 193 nm lithography far beyond its natural resolution. Yield challenge: variability — random dopant fluctuations, line-edge roughness, systematic layout-dependent effects.

### Interconnect Scaling Roadmap

As transistors shrink, interconnects become the performance bottleneck — RC delay and power dissipation in wiring dominate over gate delay below ~250 nm.

**Aluminum → Copper transition (~180 nm node, ~1997)**:
- Aluminum (ρ = 2.65 μΩ·cm) with W (tungsten) vias was standard through the 350 nm node.
- Copper (ρ = 1.68 μΩ·cm, 37% lower resistance) cannot be plasma-etched — copper chlorides/fluorides are not volatile at reasonable temperatures. Instead, a damascene process etches trenches in dielectric, then fills with Cu by electroplating (see [Advanced Processes](advanced-processes.md) for full process details).
- Barrier layers: Ta/TaN (5-20 nm) line every trench to prevent Cu diffusion into SiO₂, which poisons devices. Barrier becomes a larger fraction of wire cross-section at each node, partially offsetting Cu's resistivity advantage.

**Low-κ dielectrics**: SiO₂ (κ ≈ 4.0) inter-layer dielectric causes high inter-wire capacitance. Replacement progression: F-doped SiO₂ (κ ≈ 3.5) → organosilicate glass (κ ≈ 2.5-3.0) → porous OSG (κ ≈ 2.0-2.5). Each step reduces RC delay but trades mechanical strength — porous dielectrics crack during CMP and packaging. Air gaps (κ ≈ 1.0) in research.

### Gate Dielectric Scaling

The gate oxide is the critical dimension controlling transistor switching. Scaling it thinner increases drive current but at a steep cost in leakage.

**SiO₂ scaling (10 μm → 130 nm nodes)**: Gate oxide scales from ~100 nm down to ~1.2 nm (about 5 atomic layers) over ~30 years. Each node thins the oxide by ~30%. Below ~3 nm, quantum tunneling through the oxide produces gate leakage current that increases ~10x for every 0.2 nm of thinning. At 1.2 nm SiO₂ (130 nm node), gate leakage reaches ~100 A/cm² — unacceptable for power consumption.

**SiON interlude (130 nm → 90 nm)**: Nitrogen-doped SiO₂ (silicon oxynitride) slightly raises dielectric constant (κ ≈ 5.0 vs 3.9 for SiO₂), allowing a physically thicker (lower leakage) film with equivalent electrical oxide thickness. A stopgap measure.

**High-κ + metal gate (45 nm and below)**: Hafnium oxide (HfO₂, κ ≈ 20-25) deposited by ALD replaces SiO₂. A 2 nm HfO₂ film has the same gate capacitance as ~0.4 nm SiO₂ ("equivalent oxide thickness" or EOT) but is physically thick enough to suppress tunneling leakage by orders of magnitude. Deposited by ALD for Angstrom-level thickness control (see [Advanced Processes](advanced-processes.md)).

The polysilicon gate electrode must also be replaced: HfO₂ traps at the poly-Si interface (Fermi-level pinning). Metal gates (TiN, TaN, or work-function-tuned metal stacks) solve this. The "gate-last" (replacement gate) process removes the poly-Si after source/drain formation and replaces it with metal, preserving the high-κ dielectric.

### Bootstrap Roadmap

Not every node requires every technology. A practical bootstrap sequence:

| Capability | Required For | Key Equipment |
|-----------|-------------|---------------|
| 10 μm–3 μm | First ICs, basic logic | Projection aligner, wet bench |
| 1 μm | Microprocessors, memory | Stepper (i-line), RIE, ion implanter |
| 350 nm | Complex SoCs, early GPUs | KrF stepper, CMP, multi-level metal |
| 130 nm | Modern-class CPUs | ArF stepper, Cu damascene, 300 mm fab |
| 65 nm and below | GPU-class silicon | Immersion scanner, high-κ/metal gate, ALD |

Each generation's equipment is built using the previous generation's ICs (for control electronics, alignment systems, sensors). This self-reinforcing feedback loop is why the bootstrap takes 70-200+ years from first transistor.

### Hazards & Safety

Continuous scaling does not introduce fundamentally new hazard categories beyond those already described in the upstream and downstream process files, but the hazard severity escalates with each technology node: higher voltages (ion implanters to 500 kV), more toxic process gases (AsH₃, PH₃), and more energetic radiation sources (DUV, EUV). Safety programs must scale accordingly. Refer to the specific hazard details in:
- [Advanced Lithography](advanced-lithography.md) — excimer laser high voltage, DUV radiation, fluorine gas handling.
- [Advanced Processes](advanced-processes.md) — CMP slurry, copper contamination, ion implantation and RIE gas hazards.
- [Core Fab Processes](../photolithography/fab-processes.md) — HF acid, furnace temperatures, forming gas.

---
*Part of the [Bootciv Tech Tree](../) • [VLSI Scaling](./) • [All Domains](../)*
