# PCB Fabrication

> **Node ID**: electronics.pcb-fabrication
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`glass.fibers`](../glass/fibers.md), [`polymers.thermosets`](../polymers/thermosets.md), [`chemistry.acids`](../chemistry/acids.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`electronics.assembly`](assembly.md), [`computing.electronic`](../computing/electronic.md)
> **Timeline**: Years 25-45
> **Outputs**: pcb_bare_boards, copper_clad_laminate, etched_circuits
> **Critical**: Yes — PCBs are the universal interconnection substrate for all electronic assemblies from simple controllers to multi-GHz computers


Printed circuit board (PCB) fabrication transforms copper-clad insulating substrates into precise patterned circuit interconnects. The PCB provides mechanical support, electrical connections between components, thermal management, and electromagnetic shielding. Every electronic device — from a 555-timer circuit to a GPU — mounts on a PCB.

PCB fabrication occupies a critical position in the electronics chain. It requires [glass fiber](../glass/fibers.md) production (for FR-4 substrate), [epoxy resin](../polymers/thermosets.md) chemistry (for laminate bonding), [copper foil](../chemistry/electrolysis.md) (for conductive traces), and [photochemical](../chemistry/acids.md) processes (for etching). It enables [electronics assembly](assembly.md) (soldering components onto boards) and ultimately all [computing](../computing/electronic.md) hardware.

This document covers the full PCB fabrication process from laminate production through finished bare board, with emphasis on the chemical and mechanical processes at each stage. Component placement and soldering are covered separately in [Electronics Assembly](assembly.md).


## Materials
- **Copper foil**: Electrodeposited (ED) or rolled, 17.5 μm (½ oz) or 35 μm (1 oz) thickness, >99.8% purity. From [copper electrorefining](../chemistry/electrolysis.md).
- **Fiberglass cloth**: Woven E-glass fabric (thickness 0.05-0.35 mm, styles 106, 1080, 2113, 2116, 7628). From [glass fiber](../glass/fibers.md) production.
- **Epoxy resin**: Difunctional or multifunctional bisphenol-A/epichlorohydrin epoxy, flame-retardant grade (FR-4 = Flame Retardant 4). From [thermoset polymer](../polymers/thermosets.md) chemistry.
- **Photoresist**: Dry film (25-50 μm) or liquid, negative-acting (crosslinks on UV exposure) or positive-acting (degrades on exposure).
- **Etchant chemicals**: Ferric chloride (FeCl₃), ammonium persulfate ((NH₄)₂S₂O₈), or cupric chloride (CuCl₂) with hydrogen peroxide.
- **Drill bits**: Tungsten carbide micro-drills, 0.1-6.5 mm diameter.

## Tools
- [CNC drilling machine](../machine-tools/edm-cnc.md) with 50,000-200,000 RPM spindle
- UV exposure unit (365 nm wavelength, 100-500 mJ/cm²)
- Chemical processing tanks (etch, develop, strip, plating)
- Hydraulic laminating press (170-200°C, 200-400 psi)
- [Precision measurement](../measurement/precision-metrology.md) tools for dimensional verification

## Knowledge
- Photolithography fundamentals: exposure → development → pattern transfer
- Copper etching chemistry: oxidation-reduction reactions
- Lamination parameters: temperature, pressure, vacuum, cure cycle
- IPC standards: IPC-6012 (rigid PCB qualification), IPC-A-600 (acceptability)

## Bill of Materials

| Material | Quantity (per m² of 1.6mm FR-4 PCB) | Source | Alternatives |
|----------|--------------------------------------|--------|-------------|
| Copper foil (35 μm, both sides) | 0.62 kg | [Electrolysis](../chemistry/electrolysis.md) | Rolled copper (more expensive, better flexibility) |
| Fiberglass cloth (7628 style, 0.18 mm) | 6-8 plies = 1.1-1.4 kg | [Glass Fibers](../glass/fibers.md) | Paper/phenolic (lower cost, lower performance — FR-2) |
| Epoxy resin + hardener (B-stage prepreg) | 1.0-1.5 kg | [Thermosets](../polymers/thermosets.md) | Polyimide (higher Tg, aerospace), BT epoxy (high-frequency) |
| Dry film photoresist (38 μm) | 2 sheets × 0.5 m² | Photochemical supply | Liquid photoresist (screen-printed, lower resolution) |
| Ferric chloride etchant (42° Baumé) | 2-4 L | [Chemical industry](../chemistry/acids.md) | Ammonium persulfate (slower, cleaner), CuCl₂/H₂O₂ (regenerable) |
| Sodium carbonate (Na₂CO₃, developer) | 50-100 g | [Alkalis](../chemistry/alkalis.md) | Sodium hydroxide (more aggressive) |
| Sodium hydroxide (NaOH, resist strip) | 50-100 g | [Alkalis](../chemistry/alkalis.md) | Acetone (for some resist types) |
| Solder mask ink (photoimageable) | 100-200 mL | [Polymers](../polymers/thermosets.md) | Screen-printed epoxy mask |
| Tungsten carbide drill bits (0.3-1.0 mm) | 5-20 bits per m² | [Machine tools](../machine-tools/index.md) | — |


## Laminate Production (Copper-Clad Laminate)

1. **Weave fiberglass cloth**: E-glass fibers (5-13 μm diameter) woven into fabric. Common weave: plain or twill. Yarn count: 42-60 ends/inch.
2. **Impregnate with B-stage epoxy**: Pass fiberglass cloth through epoxy resin bath. Epoxy is partially cured (B-staged) to a tacky, non-flowing state. Resin content: 35-55% by weight. Volatile content: <0.5%. This produces "prepreg" (pre-impregnated) sheets.
3. **Lay up stack**: For a 1.6 mm FR-4 panel, stack 6-8 sheets of prepreg. Place copper foil (17.5-35 μm) on top and bottom of the stack. Insert stainless steel caul plates (1.5-3.0 mm) on outside for smooth surface finish.
4. **Laminate in press**: Load into vacuum hydraulic press. Cycle: evacuate to <50 mbar → heat to 170-185°C at 2-5°C/min → apply 200-400 psi (14-28 bar) → hold 60-90 minutes at temperature → cool to <50°C under pressure → release. Total cycle: 2-4 hours.
5. **Inspect laminate**: Check thickness (1.60 ± 0.16 mm for standard), copper peel strength (>1.0 N/mm), glass transition temperature (Tg = 130-140°C standard, 170-180°C high-Tg). Warpage: <0.8% for 1.6 mm board.

**Strengths**:
- Vacuum lamination produces void-free, uniform dielectric — critical for controlled impedance and reliable plated through-holes
- B-stage prepreg process allows storage of partially cured sheets for on-demand laminate production, decoupling resin preparation from PCB manufacturing
- Multi-layer capability: stacking multiple prepreg/core combinations enables complex interconnect (2-32+ layers) from the same basic process

**Weaknesses**:
- High capital investment: vacuum hydraulic press ($50K-$500K) with precise temperature and pressure control is the single most expensive piece of equipment
- Long cycle time: each lamination cycle takes 2-4 hours regardless of panel count — lamination is the throughput bottleneck in multi-layer production
- Moisture sensitivity: B-stage prepreg absorbs humidity from air during storage, requiring refrigerated storage (2-10°C) and limited shelf life (3-6 months)

## Single-Sided PCB (Photoimageable Method)

1. **Cut panels**: Shear laminate to panel size (typically 300 × 300 mm or 450 × 600 mm). Deburr edges.
2. **Drill holes**: CNC drill at 50,000-150,000 RPM with carbide bits. Hit rate: 100-300 holes/minute. Entry/exit material (aluminum sheet, phenolic board) prevents burrs and reduces bit breakage. For non-plated holes: drill after etching. For plated through-holes: drill before plating.
3. **Clean surface**: Pumice scrub (volcanic pumice slurry, 1-3 μm, 2-3 bar spray pressure) or chemical microetch (Na₂S₂O₈ at 30-40 g/L, 35-45°C, 1-2 min). Removes oxidation and improves photoresist adhesion. Surface roughness target: 0.3-0.5 μm Ra.
4. **Apply photoresist**: Laminate dry film resist (25-50 μm) at 100-115°C, 2-4 bar pressure, 0.5-2.0 m/min speed. Or screen-print liquid resist (10-20 μm dry film thickness), dry at 80-90°C for 10-20 min.
5. **Expose**: UV light (365 nm, 100-300 mJ/cm² for dry film) through photomask/phototool (film or glass). Contact exposure: vacuum frame draws phototool against resist. Exposure time: 5-30 seconds depending on intensity. For simple boards, direct toner transfer (laser print onto paper, iron onto copper) avoids the phototool step entirely.
6. **Develop**: Spray 1% Na₂CO₃ at 28-32°C for 30-60 seconds (negative resist). Removes unexposed (un-crosslinked) resist, revealing copper to be etched. Rinse with DI water.
7. **Etch copper**: Spray ferric chloride (30-42° Baumé, 45-55°C) at 1-3 bar. Etch rate: 15-30 μm/min for FeCl₃. For 35 μm copper: etch time 70-140 seconds. Or use ammonium persulfate (20-25%, 40-50°C, slower etch rate of 5-10 μm/min but cleaner). Cupric chloride + HCl + H₂O₂ is regenerable: CuCl₂ + Cu → 2CuCl; CuCl + HCl + H₂O₂ → CuCl₂ + H₂O.
8. **Strip resist**: Spray 3-5% NaOH at 50-60°C for 30-60 seconds. Removes crosslinked resist. Rinse thoroughly.
9. **Inspect circuit pattern**: Check for shorts (copper bridges between traces), opens (missing copper in traces), over-etch (traces narrower than specified), under-etch (copper residue between traces). Minimum trace/space: 0.15 mm for standard process, 0.05 mm for HDI.

**Strengths**:
- Dry film photoresist + UV exposure achieves fine resolution (0.10-0.15 mm trace/space) with good process tolerance — exposure dose window of ±30% still yields acceptable results
- Spray etching provides uniform, repeatable copper removal across the panel — etch rate controlled to ±10% by temperature and Baume concentration
- Toner transfer bypass eliminates phototool cost entirely for simple prototypes — a laser printer and household iron produce functional boards in under 30 minutes

**Weaknesses**:
- Undercut during etching limits minimum trace width — side etch attacks copper beneath resist at a 1:1 to 2:1 ratio, requiring wider resist openings than the desired finished trace
- Multiple wet chemical processing steps (develop, etch, strip) each require temperature-controlled tanks, rinse stages, and waste treatment — chemical handling infrastructure is significant
- Single-sided boards have no plated through-holes, requiring manual wire links or jumpers for any cross-board connections — limits circuit complexity

## Plated Through-Hole (Double-Sided)

1. **Drill all holes** on CNC drill before plating.
2. **Deburr and clean**: Mechanical deburr + chemical clean.
3. **Electroless copper deposition**: Catalytic activation (Pd-Sn colloid catalyst → accelerator removes Sn, exposes Pd) → electroless Cu plating (CuSO₄ + formaldehyde + NaOH + EDTA at 20-30°C, 2-5 μm/hour). Target: 0.5-2.0 μm copper inside holes. This thin copper layer makes holes conductive for subsequent electrolytic plating.
4. **Apply photoresist, expose, develop** (both sides simultaneously).
5. **Electrolytic copper plating**: Plate additional 20-25 μm copper in exposed areas (traces and hole barrels) at 15-30 mA/cm², 20-30°C, using CuSO₄ + H₂SO₄ electrolyte with organic additives (brightener, carrier, leveler). Plating time: 30-90 minutes.
6. **Strip resist, etch**: Strip off photoresist. Etch original base copper (the foil that was under the resist) using the same process as single-sided. The plated copper is protected by tin (tin plating applied before strip as etch resist) or the photoresist pattern.
7. **Result**: Through-holes plated with 20-25 μm copper. Hole resistance: <5 mΩ per hole.

**Strengths**:
- Electroless copper + electrolytic plating produces reliable, low-resistance hole barrels (<5 mΩ per hole) — enables true double-sided circuit routing with automatic layer-to-layer connections
- Electrolytic plating deposits copper at 20-25 μm in a single 30-90 minute cycle — produces robust mechanical connection that survives 1000+ thermal cycles
- The process extends naturally to multi-layer boards — same plating chemistry connects any number of internal copper layers

**Weaknesses**:
- Electroless copper bath uses formaldehyde (carcinogen, 5-15 g/L concentration) as reducing agent — requires ventilated process area with continuous air monitoring and OSHA exposure limit compliance (0.75 ppm TWA)
- Palladium-tin catalyst is expensive and sensitive to contamination — a single contaminated panel can poison an entire catalyst bath, requiring costly replacement
- Process has 7+ sequential wet chemistry steps (deburr, catalyst, accelerator, electroless, electrolytic, strip, etch) — each step is a potential yield loss point and requires separate chemical management

## Multi-Layer PCB

1. **Produce inner layer cores**: Etch circuit patterns on both sides of thin cores (0.1-0.8 mm) using the single-sided process on each side.
2. **Inspection (AOI)**: Automated optical inspection of inner layer patterns before lamination — defects sealed inside a multi-layer board are impossible to repair.
3. **Black oxide treatment**: Oxidize inner layer copper surfaces (NaOH + NaClO₂ at 80-90°C, 1-3 min) to improve adhesion to prepreg during lamination.
4. **Lay up**: Stack inner cores + prepreg sheets + outer copper foil in registration (alignment pins or optical targets). Typical 4-layer stack: Cu foil / prepreg / inner core L2-L3 / prepreg / Cu foil.
5. **Laminate**: Vacuum press at 170-185°C, 200-400 psi, 60-120 min. Cool under pressure.
6. **Drill, plate, etch outer layers**: Same as double-sided process. Through-holes connect all copper layers.
7. **Blind and buried vias** (advanced): Sequential lamination — drill and plate subsets of layers, then laminate together. Blind via: outer layer to inner layer (does not pass through entire board). Buried via: inner layer to inner layer.

**Strengths**:
- Enables impedance-controlled signal routing (±3-5% tolerance) required for high-speed digital buses (USB, HDMI, DDR memory) — inner reference planes provide consistent return paths
- Power and ground planes on dedicated layers provide low-inductance power distribution, reducing voltage ripple and EMI by 10-50× compared to routed power traces
- Increased routing density: 4-8 layer boards provide 2-4 signal layers plus dedicated power/ground planes, enabling complex circuits (microprocessors with 500+ pins) that are impossible on 2-layer boards

**Weaknesses**:
- Inner layer defects (shorts, opens) sealed during lamination are impossible to repair — a single defective inner layer scraps the entire multi-layer panel, reducing yield to 85-95% vs. 95-99% for double-sided
- Registration accuracy across layers must be <0.05 mm for 4+ layers — requires optical alignment systems and controlled-environment lamination to prevent thermal expansion misalignment
- Sequential lamination for blind/buried vias multiplies process time: each sub-lamination requires a full 2-4 hour press cycle, making HDI boards 3-5× more expensive than standard multi-layer

## Solder Mask, Legend, and Surface Finish

1. **Solder mask**: Apply photoimageable solder mask (LPI — liquid photoimageable) by screen printing or curtain coating (15-30 μm dry). Expose through mask (UV, 300-600 mJ/cm²). Develop with Na₂CO₃. Cure: 150°C for 30-60 min (thermal) or UV post-cure. Color: green (standard), blue, red, black, yellow, white. Purpose: prevents solder bridges, protects traces from oxidation and contamination, provides electrical insulation.
2. **Silkscreen legend**: Screen-print white epoxy ink for component reference designators (R1, C2, U3), polarity marks, test point labels, and board identification. Cure at 150°C for 15-20 min.
3. **Surface finish** (protects copper pads for soldering):
   - **HASL** (Hot Air Solder Leveling): Dip board in molten Sn/Pb (63/37) at 235-260°C. Blow hot air knives to level solder. Thickness: 1-30 μm (uneven). Cheap, robust.
   - **ENIG** (Electroless Nickel / Immersion Gold): 3-5 μm nickel + 0.03-0.08 μm gold. Flat, excellent for fine-pitch components. Gold prevents nickel oxidation; nickel is the solderable surface.
   - **OSP** (Organic Solderability Preservative): Benzimidazole or imidazole coating, 0.2-0.5 μm. Thinnest, cheapest, shortest shelf life (6-12 months). Multiple reflow cycles degrade OSP.
   - **Immersion Silver**: 0.1-0.3 μm Ag. Good solderability, moderate shelf life. Tarnishes in high-sulfur environments.
   - **Immersion Tin**: 0.8-1.2 μm Sn. Flat surface. Tin whisker risk for high-reliability applications.

**Strengths**:
- Photoimageable solder mask provides precise pad openings (±0.05 mm) and reliable solder dam between fine-pitch component pads (0.5 mm pitch QFP) — prevents solder bridges during reflow
- ENIG surface finish provides flat, coplanar pads (0.03-0.08 μm Au over 3-5 μm Ni) essential for BGA and fine-pitch component soldering — gold surface remains solderable for 12+ months
- Multiple surface finish options allow cost/performance optimization: HASL (cheapest, $0.05/board), OSP ($0.10/board, shortest shelf life), ENIG ($0.50/board, best for fine-pitch)

**Weaknesses**:
- Solder mask curing at 150°C for 30-60 minutes adds significant process time — the entire panel must dwell in a thermal oven, creating a production bottleneck
- HASL produces uneven solder coating (1-30 μm) that is incompatible with fine-pitch components (<0.5 mm pitch) — the thickness variation causes coplanarity issues
- ENIG process uses nickel sulfate and potassium gold cyanide — both are toxic, and the cyanide gold bath requires emergency antidote kits and strict handling protocols, adding cost and safety burden

## Electrical Test and Profiling

1. **Electrical test**: Flying probe (movable pin heads contact each net) or bed-of-nails (fixed fixture with spring pins for every net). Test all nets: continuity (every connection <10 Ω), isolation (every isolation >10 MΩ at 250-500V). Test time: flying probe 2-10 min/board, bed-of-nails 10-60 sec/board.
2. **Route/profile**: CNC router cuts individual boards from panel. Tool: 2.0-3.2 mm carbide router bit at 20,000-30,000 RPM, feed 10-30 mm/sec. Scoring (V-groove) for snap-apart panels: score 1/3 board thickness from each side.
3. **Final inspection**: Visual check for defects. Dimensional check (±0.1 mm for routed edges, ±0.05 mm for drilled holes). Surface quality. Pack with desiccant for moisture protection.

**Strengths**:
- Flying probe test requires no fixture — programs are generated directly from CAD data, enabling same-day test setup for prototype and low-volume boards (test time: 2-10 min/board)
- Bed-of-nails fixture provides high-speed production testing (10-60 sec/board) with >99% fault coverage — detects all shorts, opens, and incorrect net connections
- Electrical test catches defects invisible to visual inspection: high-resistance connections (>10 Ω) from incomplete plating and near-shorts (<10 MΩ isolation) from residual copper between traces

**Weaknesses**:
- Flying probe test is slow (2-10 min/board) — unsuitable for production volumes >100 boards/day where bed-of-nails fixtures are required (fixture cost: $500-$5000 per board design)
- Electrical test verifies only connectivity, not signal integrity — impedance mismatches, excessive trace length, and crosstalk are not detected without dedicated TDR or network analyzer testing
- CNC routing generates fiberglass dust and requires carbide tooling that wears rapidly — a 2.0-3.2 mm router bit lasts 50-200 linear meters of cutting in FR-4 before edge quality degrades


## Laminate Properties (FR-4)

| Parameter | Standard FR-4 | High-Tg FR-4 | Polyimide |
|-----------|--------------|--------------|-----------|
| Glass transition temperature (Tg) | 130-140°C | 170-180°C | 250-260°C |
| Dielectric constant (εᵣ) at 1 MHz | 4.2-4.8 | 4.2-4.5 | 4.0-4.3 |
| Dissipation factor (tan δ) at 1 MHz | 0.01-0.02 | 0.01-0.015 | 0.005-0.01 |
| Thermal conductivity | 0.3-0.4 W/m·K | 0.3-0.4 W/m·K | 0.1-0.2 W/m·K |
| Coefficient of thermal expansion (CTE) | 14-17 ppm/°C (x-y) | 12-15 ppm/°C (x-y) | 12-14 ppm/°C (x-y) |
| CTE (z-axis) | 50-70 ppm/°C | 30-50 ppm/°C | 25-35 ppm/°C |
| Copper peel strength | >1.0 N/mm | >1.0 N/mm | >1.2 N/mm |
| Water absorption | 0.1-0.3% | 0.05-0.15% | 0.3-0.5% |
| Flammability rating | UL 94 V-0 | UL 94 V-0 | UL 94 V-0 |

## Etching Parameters

| Parameter | Ferric Chloride | Ammonium Persulfate | Cupric Chloride/H₂O₂ |
|-----------|----------------|--------------------|--------------------|
| Concentration | 30-42° Baumé | 20-25% w/w | CuCl₂ 150-200 g/L + HCl 2-3 M |
| Temperature | 45-55°C | 40-50°C | 30-45°C |
| Etch rate (35 μm Cu) | 15-30 μm/min | 5-10 μm/min | 10-20 μm/min |
| Etch factor (side:depth) | 1:1 to 2:1 | 1.5:1 to 2.5:1 | 1:1 to 1.5:1 |
| Minimum trace/space | 0.15 mm | 0.10 mm | 0.15 mm |
| Regeneration | Not practical | Not practical | Continuous (add H₂O₂ + HCl) |
| Waste handling | Heavy metal disposal | Oxidizer disposal | Copper recovery by electrowinning |
| Copper capacity | 30-50 g/L before exhaustion | 15-25 g/L | >100 g/L (regenerable) |

## Drilling Parameters

| Hole Diameter | Spindle Speed | Feed Rate | Hit Rate | Bit Life |
|---------------|--------------|-----------|----------|----------|
| 0.2 mm | 100,000-200,000 RPM | 0.5-1.5 m/min | 100-200/min | 500-2000 hits |
| 0.3 mm | 80,000-150,000 RPM | 1.0-2.5 m/min | 150-250/min | 1000-3000 hits |
| 0.6 mm | 50,000-100,000 RPM | 1.5-3.0 m/min | 200-300/min | 2000-5000 hits |
| 1.0 mm | 30,000-60,000 RPM | 2.0-4.0 m/min | 250-350/min | 3000-8000 hits |
| 3.0 mm | 15,000-30,000 RPM | 2.0-5.0 m/min | 100-200/min | 5000-15,000 hits |

## PCB Design Capability by Layer Count

| Feature | 1 Layer | 2 Layers | 4 Layers | 6-8 Layers | 10+ Layers |
|---------|---------|----------|----------|------------|------------|
| Minimum trace width | 0.20 mm | 0.15 mm | 0.10 mm | 0.08 mm | 0.05 mm |
| Minimum trace spacing | 0.20 mm | 0.15 mm | 0.10 mm | 0.08 mm | 0.05 mm |
| Minimum hole diameter | 0.6 mm | 0.3 mm | 0.2 mm | 0.15 mm | 0.10 mm |
| Minimum annular ring | 0.15 mm | 0.10 mm | 0.08 mm | 0.06 mm | 0.05 mm |
| Board thickness | 0.6-3.2 mm | 0.6-3.2 mm | 0.8-3.2 mm | 1.0-4.0 mm | 1.0-6.0 mm |
| Impedance control | No | ±10% | ±5% | ±5% | ±3% |
| Typical applications | Simple controllers | Most electronics | Computers, telecom | Servers, medical | Aerospace, supercomputers |


## From Bench to Factory

- **Bench scale (prototyping)**: Toner transfer method — laser-print circuit pattern onto glossy paper, iron onto copper-clad laminate, soak off paper in water, etch in FeCl₃ tray. Output: 1-5 boards per day. Trace/space: 0.3-0.5 mm. No plated through-holes. Suitable for simple, single-sided prototypes.
- **Workshop scale**: UV exposure unit, spray etcher, manual drill press. Output: 10-50 boards per day. Trace/space: 0.15-0.25 mm. Double-sided with through-hole plating possible. Sufficient for small-batch production.
- **Production scale**: Fully automated line (CNC drill, automatic dry film laminator, dual-sided exposure, conveyorized spray etch/plating, AOI, electrical test). Output: 100-10,000 boards per day. Trace/space: 0.05-0.10 mm. Multi-layer (2-32+). Automated optical inspection on every layer.

## Critical Scale Transitions

- **Single to double-sided**: Requires electroless copper plating capability — the most chemistry-intensive step. The Pd-Sn catalyst and formaldehyde-based electroless copper bath are sensitive to contamination and require regular analysis and replenishment.
- **Double to multi-layer**: Requires vacuum laminating press and inner-layer AOI. Registration accuracy must be <0.05 mm across the panel for 4+ layers. Lamination is the bottleneck — each cycle takes 2-4 hours regardless of panel count.
- **Standard to HDI (High-Density Interconnect)**: Requires laser drilling (UV or CO₂ laser, 0.05-0.15 mm microvias), sequential lamination, and fine-line etching capability. This is a major capability jump — essentially a different manufacturing process.

## Minimum Economic Scale

A workshop with UV exposure, spray etch tank, and drill press can produce functional PCBs at $5-20 per board (single-sided, 100 × 100 mm) in batches of 10-50. A full production line requires $500K-$5M capital investment and needs >1,000 boards/week to amortize.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Under-etch (copper residue between traces) | Insufficient etch time, low temperature, exhausted etchant | Extend etch time by 20-30%; replace etchant; increase temperature to 50-55°C |
| Over-etch (traces too thin) | Excessive etch time, high temperature, agitated spray too aggressive | Reduce etch time; lower temperature; check spray nozzle pressure |
| Poor photoresist adhesion | Contaminated copper surface, insufficient surface roughening | Clean with pumice scrub or microetch; ensure surface roughness 0.3-0.5 μm Ra |
| Resist lifting during etch | Underexposure, insufficient lamination temperature/pressure | Increase UV exposure by 20-30%; increase lamination temperature to 110-115°C |
| Shorts between traces | Photoresist defect, dust on phototool, resist scumming | Clean phototool; clean exposure glass; ensure proper development |
| Open circuits (missing traces) | Over-etch, scratch in photoresist, phototool defect | Reduce etch time; handle panels carefully; inspect phototool before use |
| Plated holes non-conductive | Electroless copper catalyst failure, contamination in plating bath | Check catalyst activity; analyze plating bath chemistry; filter bath |
| Hole barrel cracking | Excessive Z-axis CTE, thermal shock during assembly | Use high-Tg laminate (170°C+); pre-bake before assembly to remove moisture |
| Delamination during soldering | Moisture absorbed in laminate vaporizes at reflow temperatures | Bake at 125°C for 4-24 hours before assembly; store in dry pack |
| Warped boards | Asymmetric layer stack, uneven cooling, moisture | Balance copper distribution across layers; ensure symmetric stack-up |
| Solder mask peeling | Insufficient surface preparation, undercure | Roughen surface slightly before mask application; verify cure temperature and time |
| Misregistration between layers | Pin alignment error, laminate movement during press | Use optical alignment targets; check press platen flatness; verify pin fit |

## Safety

- **Etchant chemicals**: Ferric chloride is corrosive (pH <1), stains skin and clothing brown (iron hydrolysis to Fe(OH)₃), and generates HCl fumes. Wear splash goggles, nitrile gloves, and acid-resistant apron. Work in ventilated area. Ammonium persulfate is a strong oxidizer — contact with organic materials can cause fire. Cupric chloride solutions contain dissolved copper — treat as heavy metal waste.
- **Photoresist chemicals**: Dry film resist contains acrylic polymers, photoinitiators, and solvents (MEK, acetone). Developer and stripper solutions are alkaline (Na₂CO₃, NaOH at 30-60°C). Hot alkali causes chemical burns, especially to eyes. Chemical splash goggles required (not just safety glasses). Monomers in some liquid resists are skin sensitizers.
- **Drilling hazards**: Carbide micro-drills at 50,000-200,000 RPM are explosion hazards if bits break — fragments travel at high velocity. Safety glasses mandatory. FR-4 fiberglass dust from drilling is a mechanical irritant (glass fibers embed in skin and respiratory tract). Use dust extraction at drill head; wear N95 respirator when cleaning drill area.
- **Electroless and electrolytic plating**: Copper plating baths contain CuSO₄ (toxic if ingested, irritant), H₂SO₄ (corrosive, causes severe burns), and formaldehyde (electroless bath — carcinogen, sensitizer). The formaldehyde concentration in electroless copper baths is 5-15 g/L. Use in ventilated area with local exhaust. Formaldehyde exposure limit: 0.75 ppm TWA (OSHA). The ENIG process uses potassium gold cyanide — extremely toxic. Cyanide exposure requires emergency antidote kit (amyl nitrite, sodium nitrite, sodium thiosulfate) at the workstation.
- **Lamination press**: Hydraulic press at 200-400 psi (14-28 bar) with heated platens at 170-185°C. Pinch hazard from press closure. Burn hazard from heated platens and freshly pressed laminate. Use thermal gloves. Never reach into press during operation. Two-hand safety controls required on production presses.
- **Laser drilling** (HDI/advanced): UV and CO₂ lasers are Class 4 laser hazards — eye and skin damage. Enclose beam path. Laser safety goggles matched to wavelength. Warning signs and interlocked enclosure doors.


## Incoming Material Inspection
- **Laminate**: Measure thickness (micrometer at 9+ points across panel, ±10% of nominal). Visual check for pits, dents, scratches, inclusions in copper. Copper peel strength test (peel 25 mm strip at 90° angle, >1.0 N/mm). Glass transition temperature by TMA or DSC.
- **Copper foil**: Measure thickness by cross-section (35 ± 3.5 μm for 1 oz). Surface roughness: Rz = 3-10 μm (determines adhesion to laminate).

## In-Process Controls
- **Exposure dose**: Measure UV intensity with radiometer before each shift. Verify exposure time gives 100-300 mJ/cm². Stouffer 21-step sensitivity guide on every panel: target step 6-8 developed clear for dry film.
- **Etch rate check**: Measure copper thickness before and after etch with eddy-current thickness gauge. Verify etch uniformity across panel: ±10% of target trace width.
- **Plating thickness**: Cross-section and measure plated copper in holes (target 20-25 μm). X-ray fluorescence (XRF) for non-destructive plating thickness measurement on surface.
- **Registration**: Measure alignment marks on each layer. Misregistration must be <0.05 mm for 4+ layer boards.

## Final Board Inspection
- **Dimensional**: Routed edges ±0.1 mm, hole diameter ±0.05 mm, board outline ±0.13 mm.
- **Visual**: No shorts, opens, nail heads (drill smear), burrs, delamination, measling (micro-cracks in glass-epoxy), blistering.
- **Electrical**: 100% net connectivity and isolation test (flying probe or bed-of-nails). Continuity <10 Ω per net, isolation >10 MΩ at 250-500V between all isolated nets.
- **Microsection** (cross-section): Cut a plated through-hole, mount in epoxy, polish, examine under microscope at 100-500×. Measure: inner copper foil thickness, plated copper thickness, hole wall quality, laminate integrity, drill smear. Perform once per lot or per 100 panels.
- **Solder float test**: Float specimen on 288°C solder bath for 10 seconds. No delamination or blistering. Tests laminate thermal integrity.

## Standards
- IPC-6012: Qualification and performance specification for rigid PCBs
- IPC-A-600: Acceptability of printed circuit boards (visual acceptance criteria)
- IPC-4101: Specification for base materials (laminate and prepreg)


## Substrate Materials

| Material | εᵣ | Tg | Cost | Application |
|----------|-----|-----|------|-------------|
| FR-4 (standard) | 4.5 | 135°C | $ | General purpose — 90%+ of all PCBs |
| FR-4 (high-Tg) | 4.3 | 175°C | $$ | Lead-free assembly, higher reliability |
| Polyimide | 4.1 | 260°C | $$$$ | Aerospace, military, high-temperature |
| Rogers RO4350B | 3.48 | 280°C | $$$$ | RF/microwave (controlled impedance) |
| PTFE (Teflon) | 2.1 | 327°C | $$$$$ | High-frequency RF, microwave, radar |
| Aluminum core | — | — | $$ | High-power LED, motor drives (thermal) |
| Paper/phenolic (FR-2) | 4.5 | — | ¢ | Consumer electronics, calculators, toys |

## PCB Types by Complexity

| Type | Layers | Typical Use | Bootstrap Sequence |
|------|--------|-------------|-------------------|
| Single-sided | 1 | Simple controllers, LED drivers | First achievable — toner transfer method |
| Double-sided PTH | 2 | Arduino-class boards, power supplies | Requires electroless copper plating |
| 4-layer | 4 | Computers, instrumentation | Requires multi-layer press + inner AOI |
| 6-8 layer | 6-8 | Servers, telecom, medical | Standard industrial capability |
| HDI (microvia) | 4-12+ | Smartphones, tablets | Requires laser drilling |
| Flexible (polyimide) | 1-4 | Wearables, connectors | Requires polyimide film and adhesive |
| Metal core (MCPCB) | 1-2 | LED lighting, motor drives | Aluminum substrate + dielectric layer |

## Bootstrap Path for PCB Fabrication

1. **Toner transfer** (Year 25): Laser printer + iron + FeCl₃ etch. Single-sided, 0.3-0.5 mm traces. No plated holes — use wire links for double-sided connections. Adequate for simple microcontroller circuits.
2. **Photoimageable, single-sided** (Year 28): Dry film resist + UV exposure. Better resolution (0.15-0.20 mm traces). Solder mask. Professional appearance.
3. **Double-sided PTH** (Year 32): Electroless copper + electrolytic plating. True double-sided boards with plated through-holes. Enables complex digital circuits.
4. **Multi-layer** (Year 38): Vacuum laminating press + inner layer AOI. 4-8 layer boards. Required for high-speed digital (impedance control) and complex computing.
5. **HDI** (Year 50+): Laser drilling + sequential lamination. Fine-line (0.05 mm) with microvias. Required for advanced computing and high-density packaging.

## See Also

- **[Electronics Assembly](assembly.md)**: component placement and soldering onto fabricated PCBs
- **[Passive Components](passive-components.md)**: components mounted on PCBs
- **[Electrical Systems](electrical-systems.md)**: power distribution that PCBs interconnect
- **[Glass Fibers](../glass/fibers.md)**: fiberglass cloth for FR-4 substrate
- **[Thermoset Polymers](../polymers/thermosets.md)**: epoxy resin for laminate bonding
- **[Electrolysis](../chemistry/electrolysis.md)**: copper production for traces and plating
- **[CNC Machine Tools](../machine-tools/edm-cnc.md)**: drilling and routing equipment
- **[Cleanrooms](../photolithography/cleanrooms.md)**: controlled environment for fine-line PCB production



[← Back to Electronics](index.md)
