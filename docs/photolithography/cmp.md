# Chemical Mechanical Planarization (CMP)

> **Node ID**: photolithography.fab-processes.cmp
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Parent**: [Core Fab Processes](fab-processes.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`polymers`](../polymers/index.md), [`precision-motion`](../precision-motion/index.md), [`ultra-pure.upw`](../ultra-pure/upw.md)
> **Timeline**: Years 45-70
> **Outputs**: planarized_surfaces, tungsten_plugs, copper_damascene
> **Critical**: No — enables multi-level interconnect but single-layer ICs are possible without it

Chemical Mechanical Planarization (CMP) produces atomically flat surfaces by combining chemical dissolution with mechanical abrasion. A wafer is pressed face-down against a rotating polyurethane pad while abrasive slurry flows between them. The slurry chemistry softens the target material; the pad and slurry particles mechanically remove the reaction products. CMP is the enabling technology for multi-level metal interconnect in integrated circuits — without planarization, each successive deposited layer follows the topography of the layer beneath, accumulating steps that make photolithography impossible at feature sizes below a few microns.

## Process Principle

The Preston equation governs material removal: **RR = Kp × P × V**, where RR is removal rate (nm/min), Kp is the Preston coefficient (material- and slurry-dependent), P is downforce pressure (psi), and V is relative velocity between wafer and pad (m/min). Removal rate is linearly proportional to both pressure and velocity, allowing precise control by adjusting either parameter.

**Equipment configuration**:
- **Polishing platen**: 600-800 mm diameter cast aluminum or stainless steel disk, rotating at 30-80 RPM, surfaced with a polishing pad
- **Carrier head**: Holds wafer face-down against the pad, applies controlled downforce (2-7 psi), rotates at 20-60 RPM (typically counter-rotating to platen for uniform removal)
- **Slurry delivery**: Dispensed onto pad surface at 100-300 mL/min through a nozzle arm that sweeps across the pad
- **Pad conditioner**: Diamond-embedded disk (200-300 grit in nickel bond, 150-200 mm diameter) pressed against the pad surface periodically to regenerate pad texture

## Oxide CMP (SiO₂ Planarization)

Oxide CMP is the most common application, used to planarize inter-layer dielectric (ILD) between metal layers.

**Slurry composition**:
- **Abrasive**: Colloidal silica (SiO₂ particles, 20-100 nm diameter) at 10-30% solids by weight. Particle size distribution tightly controlled — larger particles cause scratches, smaller particles reduce removal rate
- **Chemistry**: KOH or ammonium hydroxide (NH₄OH) solution, pH 10-11. The alkaline environment softens the SiO₂ surface by forming a hydrated layer (silicic acid, Si(OH)₄) that the abrasive particles can mechanically remove
- **Stabilizer**: Small amounts of hydrogen peroxide (H₂O₂) or surfactants prevent particle agglomeration and control selectivity

**Process parameters and removal rates**:

| Parameter | Oxide CMP | Tungsten CMP | Copper CMP |
|---|---|---|---|
| Abrasive | Colloidal silica (20-100 nm) | Alumina Al₂O₃ (50-200 nm) | Colloidal silica (30-80 nm) |
| Chemistry | KOH/NH₄OH, pH 10-11 | Fe(NO₃)₃ or H₂O₂-based, pH 2-4 | Glycine + H₂O₂ + BTA, pH 3-5 |
| Removal rate | 100-300 nm/min | 200-400 nm/min | 200-500 nm/min |
| Downforce | 2-5 psi | 3-5 psi | 1-3 psi |
| Platen speed | 30-80 RPM | 30-60 RPM | 30-60 RPM |
| Selectivity to oxide | — | >10:1 (W:SiO₂) | >20:1 (Cu:SiO₂) |
| Selectivity to resist | 3-5:1 | 2-4:1 | 2-3:1 |

**Endpoint detection**: Motor current monitoring detects when the oxide layer clears (removal rate changes as underlying material is exposed). Optical endpoint uses interference fringes from the thinning oxide — the periodic reflectance signal corresponds to film thickness changes. Both methods provide ~10 nm accuracy in determining when to stop polishing.

## Tungsten CMP (W Plug Formation)

After tungsten CVD fills contact holes and vias, excess tungsten on the field areas must be removed to leave only the plugs in the holes.

**Slurry composition**:
- **Abrasive**: Alumina (Al₂O₃) particles, 50-200 nm diameter, at 3-10% solids
- **Oxidizer**: Iron(III) nitrate (Fe(NO₃)₃) or hydrogen peroxide (H₂O₂) at 1-5% concentration. The oxidizer converts tungsten to WO₃ or soluble tungstate species; the alumina abrasive then removes the oxide layer
- **pH**: 2-4 (acidic). Tungsten oxidizes rapidly in acidic oxidizer solutions

**Removal rates**: 200-400 nm/min for tungsten. Oxide removal during W CMP: <20 nm/min (selectivity >10:1). This high selectivity ensures the surrounding oxide is not significantly thinned while removing the excess tungsten.

## Copper CMP (Damascene Process)

Copper CMP enables the dual-damascene interconnect process used in modern ICs: copper is electroplated into patterned trenches and vias, then CMP removes the excess copper and barrier layer to leave copper lines embedded in the dielectric.

**Slurry composition**:
- **Abrasive**: Colloidal silica (30-80 nm), 5-15% solids
- **Oxidizer**: Hydrogen peroxide (H₂O₂) at 1-3%, forming CuO and Cu₂O on the surface
- **Complexing agent**: Glycine (NH₂CH₂COOH) at 0.1-1.0%, forms soluble copper-glycine complexes that dissolve the oxidized copper
- **Corrosion inhibitor**: Benzotriazole (BTA, C₆H₄N₃H) at 0.01-0.1%, adsorbs on copper surface to protect recessed areas from chemical dissolution (provides selectivity between raised and recessed features)

**Two-step process**: First step (bulk removal): aggressive slurry removes most copper at 300-500 nm/min. Second step (buff): mild slurry with higher BTA concentration removes the final copper and barrier layer (TaN/Ta) at 50-100 nm/min with minimal dishing of the copper lines.

## Polishing Pads

The polishing pad is as critical as the slurry in determining CMP performance. Pad properties control the pressure distribution, slurry transport, and mechanical abrasion characteristics.

**Pad materials and construction**:
- **Material**: Cast or sheet polyurethane — chosen for its controlled hardness, chemical resistance to alkaline and acidic slurries, and consistent mechanical properties over thousands of polishing cycles
- **Hardness**: Shore D 40-60 for oxide CMP pads, Shore D 50-70 for metal CMP pads. Softer pads conform better to wafer topography (better planarization); harder pads provide more uniform removal across the wafer (better within-wafer uniformity)
- **Construction**: Typical two-layer pad — top layer (1.0-1.5 mm cast polyurethane with engineered pores or grooves for slurry transport) bonded to a sub-pad (1-2 mm compressed felt or foam that provides compliance and absorbs wafer-level pressure variations)

**Pad conditioning**: The pad surface degrades during polishing — pores compress closed (glazing), and the surface texture smooths out. A diamond-conditioner disk is pressed against the rotating pad every 30-60 seconds during polishing (or continuously on a separate conditioning zone) to regenerate the surface texture. Without conditioning, removal rate drops 50-80% over 30 minutes. Pad lifetime: 500-2000 wafer polishings per pad before replacement.

**Groove patterns**: Pads are grooved (concentric circles, XY grid, or spiral patterns) to improve slurry distribution across the pad surface and carry away spent slurry and debris. Groove depth: 0.3-0.8 mm, width: 0.3-1.0 mm, pitch: 2-5 mm.

## Downforce and Rotation Mechanics

CMP removal uniformity depends on precise control of pressure distribution and relative velocity across the wafer surface.

**Pressure control**: The carrier head uses a pneumatic or electromagnetic system to apply uniform downforce across the wafer. Multi-zone carrier heads (3-5 independently controlled pressure zones) compensate for edge effects — the wafer edge naturally polishes faster due to higher relative velocity and pad deformation. Zone pressures are tuned to achieve <3% within-wafer non-uniformity (WIWNU).

**Rotation mechanics**: The relative velocity between wafer and pad is the product of platen rotation and carrier rotation. Counter-rotation (wafer rotates opposite to platen) maximizes relative velocity and improves removal uniformity. Retaining ring on the carrier head prevents the wafer from sliding out during rotation.

**Wafer backside pressure**: Some carrier heads apply controlled pressure to the wafer backside (behind the wafer) to compensate for wafer bow and warp, ensuring uniform contact pressure on the front (polishing) side.

## Endpoint Detection

Accurate endpoint detection prevents over-polishing (which thins underlying layers) and under-polishing (which leaves residual material).

**Motor current monitoring**: The spindle motor current changes measurably when the polishing interface transitions from one material to another (different friction coefficients). The current signal is filtered and compared to a model of expected behavior to detect the endpoint.

**Optical (reflectance) endpoint**: A laser or broadband light source illuminates the wafer through a window in the polishing pad. As the film thins, interference fringes cause periodic oscillations in the reflected light intensity. The endpoint corresponds to the final fringe pattern before the underlying layer is exposed. Accuracy: ±5-10 nm.

**In-situ film thickness**: Spectroscopic ellipsometry through a pad window measures remaining film thickness in real time. This is the most accurate method but requires specialized pad and carrier head designs.

## Post-CMP Cleaning

After polishing, wafers carry slurry particles, pad debris, chemical residues, and metallic contaminants that must be completely removed before further processing. A single slurry particle left on the wafer surface can cause a device-killing defect.

**Cleaning sequence**:
1. **PVA brush scrub**: Soft polyvinyl alcohol (PVA) brush rolls across the wafer surface under [ultra-pure water](../ultra-pure/upw.md) flow (UPW, 18.2 MΩ·cm). The PVA sponge lifts particles mechanically without scratching. Brush pressure: 50-200 g-force
2. **Dilute HF rinse**: 0.5% hydrofluoric acid for 30-60 seconds removes chemical residues (metal hydroxides, oxide slurry particles) and any native oxide contaminated with embedded particles. The brief HF dip does not significantly attack the underlying oxide film (<5 nm removal)
3. **Megasonic clean**: 800-2000 kHz acoustic energy in dilute SC-1 solution (NH₄OH:H₂O₂:H₂O at 1:1:50) at 50-60°C gently dislodges sub-micron particles from patterned features without damaging delicate structures
4. **[Ultra-pure water](../ultra-pure/upw.md) rinse**: Final rinse in UPW at 18.2 MΩ·cm resistivity to remove all chemical residues
5. **Spin dry or Marangoni dry**: Wafer spun at 2000-3000 RPM with N₂ blow, or slowly withdrawn from UPW through an IPA vapor zone (Marangoni effect pulls water off the surface)

**Particle targets**: <50 added particles ≥0.16 μm per wafer (200 mm) or <30 added particles ≥0.12 μm (300 mm). Metallic contamination after post-CMP clean: Fe, Cu, Ni each <5 × 10⁹ atoms/cm².

## Defects and Process Control

**Dishing**: Copper in wide features polishes faster than the surrounding oxide, creating a shallow dish (depression). Dishing depth: 20-100 nm for features >10 μm wide. Controlled by slurry selectivity, downforce, and over-polish time.

**Erosion**: The oxide between dense copper lines polishes away faster than in field areas, thinning the oxide. Controlled by selectivity optimization and reducing over-polish.

**Scratches**: Caused by slurry particle agglomerates (particles stuck together forming a larger, sharp-edged cluster), pad debris, or foreign particles. Prevention: slurry filtration (0.1-0.2 μm filters), pad conditioning, cleanroom environment.

**Within-wafer uniformity (WIWNU)**: Target <3% (1σ) thickness variation across the wafer. Controlled by multi-zone carrier head pressure, retainer ring adjustment, and slurry flow optimization.

**Wafer-to-wafer uniformity (WTWNU)**: Target <5% variation between wafers in a lot. Controlled by pad conditioning consistency, slurry delivery rate stability, and consumable life tracking.

## CMP for Wafer Polishing

CMP is also used during [wafer manufacturing](../silicon/wafering.md) to produce mirror-polished silicon substrates. Wafer-level CMP uses colloidal silica slurry on large polyurethane pads to achieve surface roughness <0.3 nm RMS. This application predates IC-level CMP by decades and establishes the fundamental process knowledge.

## Hazards & Safety

- **CMP slurries**: Alkaline oxide slurries (pH 10-11) cause skin and eye irritation. Wear chemical-resistant gloves and eye protection. Acidic metal CMP slurries (pH 2-4) are corrosive. Handle in ventilated areas
- **Dilute HF in post-CMP clean**: Even at 0.5% concentration, HF requires calcium gluconate gel (2.5%) immediately available at the station. Wear acid-resistant gloves and face shield
- **Mechanical hazards**: CMP tools have rotating platens (30-80 RPM) and carrier heads with pinch points. Interlocks must be maintained. Never reach into the polishing area during operation

## See Also

- [Core Fab Processes](fab-processes.md) — parent capability for all IC fabrication
- [Wafering](../silicon/wafering.md) — CMP used for initial wafer polishing
- [Ultra-Pure Water](../ultra-pure/upw.md) — essential for post-CMP cleaning
- [Cleanrooms](cleanrooms.md) — contamination-controlled processing environment
- [Advanced Processes](../vlsi-scaling/advanced-processes.md) — advanced node CMP challenges

[← Back to Photolithography](index.md)
