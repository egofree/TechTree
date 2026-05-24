# Machining

> **Node ID**: machine-tools.machining
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 10-25
> **Outputs**: machined_parts
> **Dependencies**: machine-tools.iterative-bootstrap, machine-tools.bearings-abrasives

Machining removes material from a workpiece to achieve precise geometry, surface finish, and dimensional tolerance. This document covers the cutting operations themselves — for machine construction, see [Iterative Bootstrap](./iterative-bootstrap.md); for cutting tool materials and abrasives, see [Bearings & Abrasives](./bearings-abrasives.md).

## Lathe Operations

The lathe rotates the workpiece against a stationary single-point cutting tool. All cylindrical parts (shafts, bushings, pulleys, threads) originate here.

### Turning

Reduces the outer diameter of a rotating workpiece. The workpiece is held in a chuck or between centers; the tool moves parallel to the spindle axis.

- **Roughing cut**: 1.5-3 mm depth of cut, feed 0.3-0.6 mm/rev. Removes bulk material quickly. Surface finish ~5-10 μm Ra.
- **Finishing cut**: 0.25-0.5 mm depth, feed 0.05-0.15 mm/rev. Achieves ~1-3 μm Ra and ±0.02 mm tolerance on diameter.
- **Spindle speed**: Varies by workpiece diameter and material (see Feeds & Speeds below).

### Facing

Cuts across the end of the workpiece perpendicular to the spindle axis, producing a flat surface. Tool feeds from center outward (or periphery inward). Use slow feed near center where surface speed drops to zero. Achievable flatness: ~0.02 mm across a 50 mm face.

### Boring

Enlarges or trues an existing hole using a boring bar held in the toolpost. The workpiece rotates; the bar is fed into the bore. Essential for bearing housings and cylinder bores.

- **Boring bar overhang rule**: Maximum overhang ≤ 4× bar diameter to avoid chatter (vibration that ruins finish).
- **Tolerance**: ±0.01 mm achievable with rigid setup and sharp tool.
- **Chatter remedy**: Reduce overhang, slow speed, increase feed slightly, use heavier boring bar.

### Threading

Cuts helical grooves on the workpiece surface. See [Bearings & Abrasives](./bearings-abrasives.md) for thread standards and tap/die production.

- **External threading**: Tool shaped to thread profile (60° for ISO/Unified). Engage half-nut, take successive passes increasing depth 0.1-0.15 mm per pass. Total infeed ≈ 0.614 × pitch for 60° threads. Use thread dial indicator to re-engage on the same groove.
- **Internal threading**: Same principle with a threading tool mounted on a boring bar. More challenging — cannot see the cut. Use cutting oil liberally.
- **Feeds and speeds for threading**: Run at 25-50% of normal turning speed. The tool must be synchronized with the leadscrew, so slower speeds give more time for engagement/disengagement.

### Parting (Cutting Off)

Severs the finished part from the bar stock using a narrow parting tool (2-4 mm wide). Highest-risk lathe operation — tool is deeply embedded, prone to jamming and chatter.

- **Technique**: Feed steadily and slowly. Do not stop mid-cut (work hardens). Apply flood coolant. Reduce speed as tool approaches center.
- **RPM**: Use the lowest spindle speed setting. For 25 mm bar in steel: ~100-150 RPM.

## Milling Operations

The milling machine rotates a multi-tooth cutter while the workpiece moves on a programmable X-Y table. More versatile than the lathe for flat surfaces, slots, pockets, and complex profiles.

### Peripheral (Slab) Milling

Cutter axis is parallel to the machined surface. Teeth on the cutter periphery do the cutting. Used for squaring blocks and machining broad flats.

- **Up-cut (conventional)**: Cutter rotates against feed direction. Chips start thin, end thick. Tends to pull workpiece into cutter — secure clamping essential. Better for older machines with leadscrew backlash.
- **Down-cut (climb)**: Cutter rotation matches feed direction. Chips start thick, end thin. Better surface finish, less tool wear. Requires rigid machine with zero backlash in feed screws.
- **Depth of cut**: 1-5 mm for roughing, 0.25-1 mm for finishing.

### Face Milling

Cutter axis perpendicular to surface. Large-diameter face mill (50-100 mm) with inserted carbide or HSS tips machines broad flat surfaces efficiently. Preferred over slab milling for most flat work.

- **Cutting speed**: Same guidelines as turning for the given material.
- **Feed per tooth**: 0.1-0.3 mm for roughing, 0.05-0.15 mm for finishing.
- **Surface finish**: 1.5-3 μm Ra typical.

### End Milling

Small-diameter cutter (3-25 mm) for pockets, slots, profiles, and keyways. The workhorse of precision milling.

- **Slotting**: End mill diameter matches slot width. Cut full depth in multiple passes (1-3 mm per pass axially) rather than single deep pass.
- **Pocketing**: Helical or ramp entry. Clear chips with air blast or coolant. Stepover = 40-60% of cutter diameter for roughing.
- **Keyway cutting**: Mill a rectangular slot on a shaft for a square or rectangular key. Width per standard (e.g., 6 mm keyway on 30-38 mm shaft). Depth: approximately half the keyway width.

## Drilling, Boring & Reaming

### Drilling

Produces holes using a rotating twist drill. The drill press or lathe tailstock feeds the drill axially into the work.

- **Twist drill geometry**: 118° point angle (standard), 135° for harder materials. Two helical flutes evacuate chips.
- **Pilot hole**: For holes >10 mm, drill a pilot hole (3-5 mm) first to reduce cutting force and improve accuracy.
- **Peck drilling**: For holes deeper than 3× diameter, retract the drill every 1-2 mm to clear chips. Prevents binding and drill breakage.
- **Tolerance**: ±0.1 mm on diameter for a sharp drill in a rigid setup. Hole position accuracy ±0.15 mm on drill press.

### Boring (Milling Machine)

Uses a single-point boring head in the milling machine spindle to enlarge and true a drilled hole. Adjustable boring head allows precise diameter control via micrometer adjustment (0.01 mm resolution).

- **Tolerance**: ±0.01 mm achievable. Concentricity to existing features: ±0.02 mm.
- **Application**: Bearing pockets, cylinder bores, precision shaft holes.

### Reaming

Finishing operation that enlarges a drilled hole to precise diameter and smooth finish using a multi-flute reamer.

- **Preparation**: Drill 0.2-0.5 mm undersized (depending on diameter), then ream to final size.
- **Speed**: 1/3 to 1/2 of drilling speed for the same diameter. Too fast tears the surface.
- **Feed**: 0.3-0.5 mm/rev, steady and continuous. Never reverse the reamer while engaged.
- **Tolerance**: ±0.01 mm on diameter. Surface finish: 0.4-1.0 μm Ra.
- **Lubrication**: Use cutting oil — reaming dry causes galling and oversize holes.

## Grinding Operations

Uses abrasive wheels for precision finishing. The final machining step before lapping. Achieves tolerances and finishes impossible with cutting tools.

### Surface Grinding

Flat workpiece on a magnetic chuck (or clamped). Horizontal-spindle grinding wheel reciprocates across the surface.

- **Wheel speed**: 25-35 m/s (1500-2100 m/min peripheral speed). Do not exceed wheel rating.
- **Depth of cut (downfeed)**: 0.005-0.05 mm per pass. Light cuts — grinding removes very little per pass.
- **Table feed**: 15-30 m/min cross-feed rate.
- **Tolerance**: ±0.005 mm flatness, ±0.0025 mm parallelism. Surface finish 0.2-0.8 μm Ra.

### Cylindrical Grinding

Workpiece rotates between centers; grinding wheel contacts the OD. For precision shafts, bearing journals, and gauge surfaces.

- **Work speed**: 10-25 m/min (much slower than grinding wheel).
- **Infeed**: 0.005-0.025 mm per pass for roughing, 0.002-0.005 mm for finishing.
- **Tolerance**: ±0.003 mm on diameter. Surface finish 0.1-0.4 μm Ra.

## Feeds & Speeds Guidelines

Cutting speed (surface meters per minute) determines spindle RPM: **RPM = (1000 × cutting speed) / (π × diameter)**.

| Material | HSS Turning (m/min) | HSS Milling (m/min) | Drilling (m/min) | Grinding (m/min) |
|----------|--------------------|--------------------|------------------|-----------------|
| Aluminum | 150-300 | 150-250 | 50-80 | — |
| Brass    | 80-150 | 80-120 | 30-60 | — |
| Cast iron | 25-45 | 20-35 | 15-25 | 25-35 |
| Mild steel | 20-40 | 18-30 | 15-25 | 25-35 |
| Tool steel | 12-25 | 10-20 | 8-15 | 20-30 |
| Stainless steel | 12-20 | 10-18 | 8-15 | 18-28 |

**[Feed rates](../glossary/feed-rates.md)** (for HSS tools):
- Turning roughing: 0.3-0.6 mm/rev; finishing: 0.05-0.15 mm/rev
- Milling: 0.05-0.3 mm/tooth (smaller for harder materials)
- Drilling: 0.1-0.3 mm/rev (larger diameter = higher feed)

Carbon steel tool bits run at roughly 50% of HSS speeds. See [Bearings & Abrasives](./bearings-abrasives.md) for tool material properties.

## Tolerance Summary by Operation

| Operation | Typical Tolerance | Surface Finish | Best Achievable |
|-----------|------------------|----------------|-----------------|
| Turning (rough) | ±0.1-0.25 mm | 3-10 μm Ra | ±0.05 mm |
| Turning (finish) | ±0.02-0.05 mm | 1-3 μm Ra | ±0.01 mm |
| Facing | ±0.02 mm flatness | 1-3 μm Ra | ±0.01 mm |
| Milling (rough) | ±0.1 mm | 3-6 μm Ra | ±0.05 mm |
| Milling (finish) | ±0.025-0.05 mm | 1-2 μm Ra | ±0.015 mm |
| Drilling | ±0.1 mm | 3-6 μm Ra | ±0.05 mm |
| Boring | ±0.01-0.025 mm | 0.8-2 μm Ra | ±0.005 mm |
| Reaming | ±0.01 mm | 0.4-1 μm Ra | ±0.005 mm |
| Surface grinding | ±0.005 mm | 0.2-0.8 μm Ra | ±0.002 mm |
| Cylindrical grinding | ±0.003 mm | 0.1-0.4 μm Ra | ±0.001 mm |
| Lapping | ±0.001 mm | 0.025-0.1 μm Ra | ±0.0005 mm |

## Workholding

Secure workholding is essential — a loose workpiece is both inaccurate and dangerous.

- **[Lathe chuck](../glossary/lathe-chuck.md)** (3-jaw self-centering): Quick setup, ±0.05 mm repeatability. For round and hex stock.
- **[Lathe chuck](../glossary/lathe-chuck.md)** (4-jaw independent): Each jaw adjusts separately. Can hold irregular shapes, achieve ±0.01 mm concentricity with dial indicator alignment.
- **Between centers**: Workpiece supported by centers in headstock and tailstock. Best concentricity. Requires drive dog and faceplate. For long shafts.
- **Collet**: Spring-steel sleeve grips bar stock tightly. Best concentricity (±0.005 mm). Limited diameter range per collet.
- **Milling vise**: Kurt-style precision vise. Clamp workpiece on mill table. Indicate (dial indicator) jaw for alignment to ±0.01 mm.
- **Clamps and step blocks**: Direct clamping to mill table T-slots. For oversized or irregular workpieces. Use at least two clamps. Place clamping force over solid support (not overhanging).
- **[Magnetic chuck](../glossary/magnetic-chuck.md)** (surface grinder): Electromagnetic or permanent magnet. Holds ferrous workpieces flat without mechanical clamps. Demagnetize workpiece after grinding.
- **V-blocks and clamps**: Hold round stock for milling flats or drilling cross-holes. Indicate V-block alignment with dial indicator.

## Cutting Fluid Application

Cutting fluids cool the tool and workpiece, lubricate the chip-tool interface, and flush chips. See [Lubricants](../chemistry/lubricants.md) for full production details.

**Quick reference by operation**:

| Operation | Recommended Fluid | Application |
|-----------|-------------------|-------------|
| Turning (light) | Soluble oil emulsion (5-10%) | Flood or manual |
| Turning (heavy) | Sulfurized cutting oil | Flood |
| Milling | Soluble oil emulsion | Flood |
| Drilling | Soluble oil emulsion | Flood or through-spindle |
| Tapping/threading | Straight cutting oil or sulfurized oil | Flood or manual |
| Reaming | Lard oil or soluble oil | Flood |
| Grinding | Soluble oil or synthetic (heavily diluted) | Flood — high volume |

## Safety

- **[Eye protection mandatory](../glossary/eye-protection-mandatory.md)** for all machining. Chips are hot and sharp.
- **[No loose clothing, gloves, rings, or long sleeves](../glossary/no-loose-clothing-gloves-rings-or-long-sleeves.md)** near rotating machinery. Lathe chucks and drill presses are entanglement hazards.
- **Chip management**: Use chip hook or brush — never hands. Steel chips are razor-sharp and hot (blue = 300°C+).
- **Workpiece security**: Verify clamping before every cut. A thrown workpiece is lethal.
- **Abrasive wheels**: Ring test before mounting. Never exceed rated speed. Use wheel guards. Dress wheels regularly to maintain sharpness and concentricity.
- **Grinding dust**: Use extraction or dust collection. Inhaling fine metal dust causes lung damage. Grinding cast iron and steel produces respirable particles.

## References

- Machine tool construction sequence: [Iterative Bootstrap](./iterative-bootstrap.md)
- Cutting tool materials and abrasives: [Bearings & Abrasives](./bearings-abrasives.md)
- Cutting fluid production and properties: [Lubricants](../chemistry/lubricants.md)
- Precision achievement milestones: See [Iterative Bootstrap](./iterative-bootstrap.md) precision table

### Limitations

- **Material removal waste**: Machining converts 20-80% of raw material into chips (swarf). For expensive materials (copper, titanium), this waste is a significant cost factor. Chip recycling is energy-intensive.
- **Tool wear**: Cutting tools dull through abrasion, adhesion, diffusion, and fatigue. Tool life follows Taylor's equation: VTⁿ = C. Carbide tools last 15-60 minutes of cutting time depending on speed and material.
- **Thermal distortion**: Cutting generates heat (80% goes into chip, 15% into tool, 5% into workpiece). Thin workpieces distort from thermal expansion, requiring cool-down periods between roughing and finishing passes.
- **Vibration and chatter**: At certain depth-of-cut / speed combinations, the cutting process becomes unstable, causing chatter — self-excited vibration that degrades surface finish and can damage the tool. Requires stiffness analysis and parameter tuning.
- **Surface integrity**: Machining creates a worked surface layer (residual stress, microstructural changes, micro-cracks) 10-200 µm deep. Fatigue-critical parts may require post-machining treatments (shot peening, stress relief annealing).
- **Skill requirement**: Manual machining requires significant operator skill for setup, tool selection, and process control. CNC machining transfers this to programming but requires software expertise.

### See Also

- [Forming](forming.md) — Alternative shaping processes with less waste
- [Bearings & Abrasives](bearings-abrasives.md) — Abrasive finishing and precision grinding
- [Iterative Bootstrap](./iterative-bootstrap.md) — Precision improvement pathway
- [Iron & Steel](../metals/iron-steel.md) — Workpiece materials
- [Machine Tools Overview](./index.md) — Complete machine tools reference

---

*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
