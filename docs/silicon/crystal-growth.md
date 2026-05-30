# Crystal Growth & Wafering

> **Node ID**: silicon.crystal-growth
> **Domain**: [Silicon](./index.md)
> **Dependencies**: [`chemistry.air-separation`](../chemistry/air-separation.md), [`cryogenics.liquefaction-storage`](../cryogenics/liquefaction-storage.md), [`glass.advanced`](../glass/advanced.md), [`measurement.precision-metrology`](../measurement/precision-metrology.md)
> **Enables**: [`silicon.basic-devices`](basic-devices.md), [`silicon.crystal-growth.cz-pulling`](cz-pulling.md), [`silicon.wafering`](wafering.md)
> **Timeline**: Years 30-50
> **Outputs**: single_crystal_ingots, wafers, polished_wafers
> **Critical**: Yes — single-crystal silicon is required for all semiconductor devices and efficient solar cells


The CZ puller is the most mechanically demanding piece of equipment in the silicon path. It requires precision motion control, high-temperature furnace, and contamination control.

## Why Single Crystal Silicon

Polycrystalline silicon contains grain boundaries between individual crystal grains. These boundaries are electrically active: they act as recombination centers where electron-hole pairs recombine without contributing to current flow. In polycrystalline silicon, minority carrier lifetime drops from >1,000 μs (single crystal) to <10 μs. For solar cells, this means lower efficiency (10-12% for poly-Si vs. 15-20% for single crystal). For semiconductor devices, grain boundaries are fatal: they cause unpredictable leakage currents, threshold voltage shifts, and junction shorts.

Dislocations within the crystal have a similar effect. Even a single dislocation threading through a transistor's active region can cause device failure. This is why the Dash necking process (described below) is so critical: it eliminates dislocations from the growing crystal.

**Strengths**:
- Single-crystal silicon enables minority carrier lifetimes >1,000 μs — 100× better than polycrystalline, directly improving solar cell efficiency from 10-12% to 15-20%
- Grain-boundary-free material eliminates unpredictable leakage currents and threshold voltage shifts in MOS devices

**Weaknesses**:
- Single-crystal growth requires precision equipment (CZ puller or FZ system) that is far more complex and expensive than directional solidification for polycrystalline ingots
- CZ crystals incorporate 10-20 ppma oxygen from the quartz crucible, limiting electrical properties for certain high-power applications

## Crystal Growth Methods Overview

Three principal methods produce single crystal silicon ingots. Each trades off purity, cost, and complexity differently:

**Czochralski (CZ) pulling**: The dominant method, producing >90% of all single crystal silicon. Crystal is pulled from a melt in a fused silica crucible. For CZ machine design and hardware specifications, see [CZ Pulling](./cz-pulling.md). Key limitation: oxygen incorporation from the dissolving quartz crucible (10-20 ppma O). This oxygen is manageable for most devices but limits certain high-power and radiation-hard applications.

**Float zone (FZ)**: No crucible contact. Highest purity silicon. Described in detail below. Used for power devices where high resistivity (>10,000 Ω·cm) and low oxygen content are required.

**Bridgman**: Directional solidification in a shaped mold. Simpler but produces more defects. Described below. Common for III-V compound semiconductors (GaAs, InP) where CZ pulling is impractical.

**Strengths of CZ pulling**:
- Well-established process producing >90% of all semiconductor-grade silicon wafers
- Scalable to 300 mm diameter with high throughput (one 15-30 kg ingot per 24-48 hour cycle)

**Weaknesses of CZ pulling**:
- Quartz crucible dissolution introduces 10-20 ppma oxygen, limiting use for high-power and radiation-hard devices
- Single-use crucible is a significant consumable cost and supply chain bottleneck

**Strengths of FZ**:
- Oxygen content <1 ppma and resistivity >10,000 Ω·cm — the purest silicon available
- No crucible means no metallic contamination source

**Weaknesses of FZ**:
- Maximum diameter ~200 mm (surface tension cannot stabilize larger molten zones)
- Requires expensive RF generator and precise coil alignment

**Strengths of Bridgman**:
- Simple equipment — two-zone furnace and translation mechanism, no precision pull mechanism required
- Compatible with III-V compounds (GaAs, InP) that decompose at their melting point under open atmosphere

**Weaknesses of Bridgman**:
- Higher defect density than CZ or FZ due to contact with crucible walls during solidification
- Not used for silicon IC production — relegated to compound semiconductors and specialty applications

## Seed Crystal Preparation

The seed crystal initiates the single-crystal structure in all growth methods:
- **Source**: Cut from a previously grown high-quality ingot (initially obtained from a laboratory or produced by slow directional solidification and selection of single-grain regions).
- **Orientation**: Determine crystal orientation using X-ray Laue diffraction. Expose the seed to an X-ray beam; the diffraction pattern (spots on film) reveals the crystal orientation relative to the seed surface. For <100> orientation, the surface is cut perpendicular to the [100] direction. For <111>, perpendicular to the [111] direction.
- **Etching**: After cutting, chemically etch the seed in a CP4-type etch (HNO₃:HF:CH₃COOH mixture) to remove mechanical damage from the cutting process. Damaged crystal in the seed propagates dislocations into the growing crystal. Target surface: smooth, pit-free, and damage-free to a depth of at least 50 μm.
- **Dimensions**: Typically 5-10 mm square cross-section, 50-80 mm long. The seed must be large enough to handle without breaking but small enough that the Dash neck can effectively eliminate its dislocations.

**Strengths**:
- A single high-quality seed can initiate thousands of crystals through reuse — the Dash neck eliminates any dislocations from the seed
- X-ray Laue diffraction provides orientation accuracy within ±0.5° at minimal equipment cost

**Weaknesses**:
- Initial seed crystal requires either a laboratory source or slow directional solidification with grain selection — a bootstrap chicken-and-egg problem
- CP4 etch mixture contains HF, requiring full acid-resistant PPE and calcium gluconate on-site

## Czochralski Process Detail

The CZ process requires precision control of temperature, pull speed, and rotation. Machine hardware specifications (chamber, crucible, heater, pull mechanism) are detailed in [CZ Pulling](./cz-pulling.md).

**Growth process**:
1. **Charge**: Load polysilicon chunks into crucible. Add dopant: boron (B, for p-type) or phosphorus (P, for n-type). Typical doping: 10¹⁴-10¹⁶ atoms/cm³ (resistivity 0.1-100 Ω·cm).
2. **Melt**: Evacuate chamber, backfill with Ar. Heat to 1420-1430°C. Polysilicon melts completely (~3-6 hours for 10-30 kg charge).
3. **Seed insertion**: Lower seed crystal until it contacts melt surface. Melt a small amount of seed (establishes liquid-solid interface).
4. **Neck growth**: Pull slowly (3-5 mm/min) to form thin neck (~3 mm diameter). This eliminates dislocations from seed —Dash process. Neck must be 50-100 mm long.
5. **Shoulder growth**: Reduce pull speed, increase diameter to target (100-300 mm). Crown/shoulder region transitions from neck to full diameter.
6. **Body growth**: Maintain pull speed 0.8-1.5 mm/min. Constant rotation (5-15 RPM crucible counter-rotation). Temperature feedback controls diameter. Crystal grows 300-1000 mm long over 12-36 hours.
7. **Tail-out**: Reduce diameter gradually at end of pull to avoid thermal shock dislocations.
8. **Cooling**: Retract crystal into upper chamber. Cool under Ar atmosphere at 2-5°C/min to room temperature (12-24 hours).

**Crystal quality parameters**:
- **Resistivity uniformity**: ±5-10% axial, ±2-5% radial
- **Oxygen content**: 10-20 ppma (from crucible dissolution)
- **Carbon content**: <1 ppma (from heater/atmosphere)
- **Dislocation density**: <100/cm² (ideally zero — Dash process achieves this)
- **Crystal orientation**: Within ±0.5° of target

**Resource consumption per crystal** (typical 150 mm, 15 kg):
- Polysilicon: ~15 kg
- Argon: ~2-5 m³ (flow during growth)
- Electricity: ~200-400 kWh (heater + motors + cooling)
- Quartz crucible: 1 (consumed — partially dissolved)
- Graphite susceptor: lasts ~50-100 pulls before replacement

**Strengths**:
- Well-controlled process producing >90% of world semiconductor-grade silicon with diameter scalability to 300 mm
- Dash necking reliably produces zero-dislocation crystals suitable for all device types

**Weaknesses**:
- 10-20 ppma oxygen from quartz crucible dissolution limits electrical performance for power and radiation-hard applications
- Single-use quartz crucible is the highest consumable cost per run — each requires arc-fusion fabrication from high-purity SiO₂

## Float Zone (FZ) Crystal Growth

**Principle**: A narrow molten zone is passed along a solid polysilicon rod. No crucible contacts the silicon, so there is no oxygen contamination. The molten zone is supported entirely by surface tension of the silicon melt.

**Equipment**:
- **RF coil**: Water-cooled copper induction coil (single-turn or multi-turn) wrapped around the polysilicon rod. RF power (50-500 kHz, 20-100 kW) induces eddy currents in the silicon, heating the narrow zone to >1414°C. The coil geometry defines the molten zone width (~10-20 mm).
- **Rod mounting**: Polysilicon rod (50-200 mm diameter, 1-2 m long) held vertically, clamped at both ends in a stainless steel vacuum chamber. Top end rotates slowly (2-5 RPM) for thermal uniformity.
- **Atmosphere**: Argon at atmospheric pressure or slight overpressure. Some FZ processes use vacuum for impurity removal.
- **Seed crystal**: Affixed to the bottom of the polysilicon rod. When the molten zone first passes the seed, it recrystallizes as single crystal following the seed orientation.

**Process**:
- Pass the RF coil slowly along the rod from bottom to top at 1-3 mm/min. The molten zone travels with the coil. Each pass purifies the silicon (impurities segregate into the molten zone and are swept to one end). 10-15 passes for uniform doping distribution.
- Zone pass speed is critical. Too fast (>5 mm/min) and the solidification front cannot maintain single-crystal growth. Too slow (<0.5 mm/min) and the molten zone becomes unstable (drips from the rod).

**Results**:
- **Resistivity**: >10,000 Ω·cm achievable (ultra-high purity, essentially intrinsic silicon). This is 100× higher resistivity than CZ silicon.
- **Oxygen content**: <1 ppma (no crucible contact). Much lower than CZ's 10-20 ppma.
- **Carbon content**: <0.1 ppma.
- **Dislocation density**: Zero (with proper seed and stable zone).
- **Applications**: Power semiconductors (thyristors, IGBTs for high-voltage switching), radiation detectors, specialized devices requiring the highest purity.
- **Limitation**: Maximum diameter ~200 mm (molten zone stability limits diameter; surface tension cannot support larger melt columns). CZ is preferred for 200-300 mm production.

**Strengths**:
- Oxygen content <1 ppma and resistivity >10,000 Ω·cm achievable — 100× higher resistivity than CZ silicon
- Multiple zone passes (10-15) purify silicon by sweeping impurities to one end, producing 8-9N purity without chemical processing

**Weaknesses**:
- Maximum diameter limited to ~200 mm by molten zone surface tension stability
- RF induction coil and power supply (20-100 kW at 50-500 kHz) are expensive and require precise impedance matching

## Bridgman Growth

**Principle**: Directional solidification in a shaped mold. The entire charge is melted, then cooled from one end so that solidification proceeds directionally. A seed crystal at the cool end initiates single-crystal growth.

**Equipment**:
- **Ampoule/mold**: Quartz or graphite crucible with a pointed bottom (seed well). Sealed under vacuum or inert atmosphere. The pointed geometry ensures that only a single crystal grain survives the initial solidification (grain selection by competitive growth in the narrow tip).
- **Furnace**: Two-zone vertical furnace with independent temperature control. Hot zone above (holds melt at ~1420-1500°C for Si, higher for III-V materials), cold zone below (below melting point). A controlled temperature gradient between zones (10-50°C/cm) drives directional solidification.
- **Translation mechanism**: The ampoule moves slowly downward through the furnace (or the furnace moves upward over the ampoule). Speed: 0.5-5 mm/hour. Slower translation produces fewer defects.

**Applications for III-V compounds**:
- **GaAs (gallium arsenide)**: Melts at 1238°C. Bridgman growth in sealed quartz ampoules (arsenic overpressure prevents decomposition). Used for high-frequency devices, LEDs, laser diodes, and solar cells. The primary method for GaAs substrate production.
- **InP (indium phosphide)**: Melts at 1062°C. Similar sealed-ampoule Bridgman process. Used for photonics and high-frequency electronics.
- **Why not CZ for III-V?**: CZ pulling requires the crucible to rotate in the melt. For III-V compounds, the group V element (As, P) has high vapor pressure at the melting point and would evaporate if the melt were open to the atmosphere. The sealed Bridgman ampoule contains the vapor pressure.

**Strengths**:
- Sealed ampoule contains toxic, high-vapor-pressure group V elements (As, P) safely during growth
- Simple equipment — two-zone furnace with translation mechanism, no precision pull system required

**Weaknesses**:
- Higher defect density than CZ or FZ due to crucible wall contact during solidification
- Sealed quartz ampoules are single-use and risk explosion if internal pressure exceeds quartz strength at temperature

## Edge-Defined Film-Fed Growth (EFG)

**Principle**: A shaped die (usually graphite) is immersed in the silicon melt. Capillary action draws silicon up through a narrow slot in the die. A seed crystal contacts the silicon at the top of the die and is pulled upward, crystallizing the silicon in the shape defined by the die opening.

**Applications**:
- **Ribbons**: Thin silicon sheets (100-300 μm thick, 50-100 mm wide, meters long) produced directly without wafering. Eliminates the kerf loss of wire saw slicing (~40-50% of silicon in conventional wafering is lost as kerf). Ribbon silicon is lower quality (more grain boundaries and defects) but suitable for low-cost solar cells.
- **Tubes**: Hollow octagonal tubes pulled and then cut into wafers by laser slicing. Multiple wafers from one tube. Higher throughput than single-ribbon pulling.
- **Limitation**: Die material (graphite) slowly dissolves into the silicon, introducing carbon contamination. The silicon-carbon interaction limits crystal quality. EFG wafers typically achieve 12-15% solar cell efficiency, lower than CZ wafers (15-20%) but with much lower silicon consumption per watt of solar output.

**Strengths**:
- Eliminates ~40-50% kerf loss from wire saw wafering by producing thin ribbons (100-300 μm) directly
- Multiple ribbons or octagonal tubes can be pulled simultaneously from a single furnace for high throughput

**Weaknesses**:
- Carbon contamination from graphite die limits crystal quality to 12-15% solar cell efficiency
- Grain boundaries and defects from die contact restrict EFG silicon to solar applications — not suitable for IC fabrication

## Wafer Production


**Slicing (wire saw)**:
- **Equipment**: Wire saw — thin steel wire (140-180 μm diameter) wound on grooved wire guides in a web pattern. Wire travels at 5-15 m/s. Abrasive slurry (SiC or diamond particles 5-20 μm in oil or water-based carrier) fed onto wire.
- **Process**: Ingot mounted on ceramic plate, fed into wire web. Wire tension 15-30 N. Cut time 4-8 hours for 150 mm ingot. Produces 200-400 wafers per ingot.
- **Kerf loss**: ~150-200 μm per wafer (wire + slurry). ~40-50% of silicon lost as kerf.
- **Wafer thickness**: 200-350 μm for solar, 500-775 μm for semiconductor.
- **Alternative**: Inner-diameter (ID) saw — circular blade with diamond-coated inner edge. Cuts one wafer at a time. Slower but simpler. Blade thickness ~200 μm. Good for small-scale or prototype.

**Strengths**:
- CMP produces mirror-smooth surfaces with roughness <0.5 nm Ra — required for sub-micron photolithography depth of focus
- Double-sided lapping achieves 2-5 μm TTV (total thickness variation) across a 200 mm wafer

**Weaknesses**:
- Wire saw kerf loss wastes 40-50% of expensive single-crystal silicon
- CMP slurry (colloidal silica at pH 10-11) is a chemical burn and environmental hazard requiring special handling and disposal

**[Lapping](../glossary/lapping.md)** (mechanical flattening):
- **Process**: Place wafers on lapping machine (cast iron plate, 300-600 mm diameter). Add abrasive slurry (Al₂O₃ 5-15 μm in water/glycol). Rotate plate and carriers (wafer-holding rings). Remove ~20-50 μm per side. Duration 15-30 minutes.
- **Result**: Flat to ~2-5 μm total thickness variation (TTV). Surface roughness ~0.5-1 μm Ra. No subsurface damage if done correctly.
- **Double-side lapping**: Lap both sides simultaneously for better parallelism.

**Chemical-Mechanical Polishing (CMP)**:
- **Process**: Press wafer (face-down) against rotating polishing pad (polyurethane or felt). Feed polishing slurry: colloidal silica (SiO₂ particles 20-80 nm) in alkaline solution (NaOH or KOH, pH 10-11). Chemical etching + mechanical abrasion synergize.
- **Removal rate**: 0.5-2 μm/min. Remove ~10-30 μm total.
- **Result**: Mirror finish. Surface roughness <0.5 nm Ra. Flat to <1 μm TTV.
- **Post-CMP cleaning**: RCA clean (see below) to remove slurry residue and organic contamination.

**[RCA Clean](../glossary/rca-clean.md)** (standard wafer cleaning sequence):
1. **SC-1 (Standard Clean 1)**: NH₄OH:H₂O₂:H₂O = 1:1:5 at 75-80°C for 10-15 min. Removes organic contaminants and particles. Leaves thin chemical oxide.
2. **DI water rinse**: Overflow rinse, 5-10 min.
3. **[HF dip](../glossary/hf-dip.md)** (optional): Dilute HF (1-2%) for 15-30 seconds. Removes oxide (hydrogen-terminates surface). Skip if oxide desired.
4. **SC-2 (Standard Clean 2)**: HCl:H₂O₂:H₂O = 1:1:6 at 75-80°C for 10-15 min. Removes metallic contaminants (Fe, Au, Cu, Ni).
5. **DI water rinse + spin dry** or **[Marangoni dry](../glossary/marangoni-dry.md)** (IPA vapor, surface tension gradient pulls water off).

**Strengths**:
- Wire saw cuts all 800-900 wafers from a 300 mm ingot simultaneously in 8-20 hours — far higher throughput than ID blade sawing
- RCA clean sequence removes particles down to 0.1 μm and metallic contamination to <10¹⁰ atoms/cm²

**Weaknesses**:
- Wire saw kerf loss of 150-200 μm per wafer wastes ~40-50% of silicon as abrasive-laden sludge
- RCA clean uses hazardous chemicals (HF, H₂O₂) requiring dedicated fume hoods and PPE

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Crystal has dislocations (>100/cm²) | Dash neck too thick (>5 mm) or vibration during neck growth | Reduce neck diameter to ~3 mm by increasing pull speed to 3-5 mm/min; check vibration isolation (air springs, concrete inertia block); ensure floor vibration <1 μm at puller |
| Crystal diameter oscillates (±>2 mm) | PID control loop instability or thermocouple drift | Tune PID gains (reduce proportional gain, increase derivative); verify thermocouple is not degraded (type B thermocouples drift after ~500 hours at 1400°C); check pyrometer calibration |
| High oxygen content (>20 ppma) | Excessive crucible dissolution from high melt temperature or aggressive convection | Reduce melt temperature to minimum (1415-1420°C); increase argon flow to suppress convection; consider magnetic CZ (MCZ) if available to suppress melt flow |
| SiC precipitates in crystal (>5 ppma C) | CO contamination from graphite heater, poor argon purity, or insufficient purge | Use higher-purity argon (>99.999%, O₂+H₂O <1 ppm); extend 3× purge cycle; check chamber seals for leaks; replace aged graphite insulation that may be outgassing |
| Crystal cracks during cooling | Cooling rate too fast through 800-1200°C danger zone | Reduce cooling rate to 2-5°C/min; ensure argon atmosphere maintained during cooling; avoid mechanical disturbance during cool-down |
| Slip lines on etched wafers | Thermal stress from non-uniform cooling or steep radial temperature gradient | Improve radiation shield design for uniform thermal environment; reduce pull speed slightly (lower thermal gradient at interface); ensure susceptor is not cracked (causes asymmetric heating) |
| Wafer TTV >5 μm after lapping | Uneven slicing (wire saw vibration or inconsistent wire tension) | Check wire tension (15-30 N stable); verify wire guide grooves are not worn; ensure ingot is securely mounted and not shifting during cut |
| High particle count on finished wafers | Contaminated CMP slurry, dirty polishing pad, or inadequate RCA clean | Replace CMP slurry (check expiration); condition pad with diamond disk; verify UPW resistivity is 18.2 MΩ·cm; add megasonic clean step after CMP |

## Safety Hazards

Crystal growth and wafering involve extreme temperatures, toxic chemicals, and high-current electrical systems:
- **Molten silicon**: Pours and splashes at ~1420-1430°C. Contact causes instantaneous deep burns. Any moisture on crucible surfaces, tools, or charge material causes violent steam explosions. Pre-dry all tooling. No water in the furnace area during charging or tapping.
- **Quartz crucible softening**: Fused silica softens above 1600°C. If heater control fails and temperature overshoots, the crucible can deform or rupture, spilling 10-30 kg of molten silicon. Temperature interlocks with automatic power cutoff are mandatory.
- **Argon asphyxiation**: CZ pullers flow 10-30 L/min of argon continuously. In confined or poorly ventilated spaces, argon (heavier than air) pools at floor level and displaces oxygen. O₂ monitors with audible alarms required in puller rooms. Exhaust must vent outside. Never enter a puller enclosure after argon backfill without forced ventilation.
- **High-current electrical hazard**: Graphite heaters draw 500-3000 A at 10-40 V (20-100 kW). Bus bar connections must be shrouded. Arc flash risk during maintenance. Lock-out/tag-out procedures before any electrical work. Insulating gloves and face shield for bus bar inspection.
- **HF acid burns (RCA clean)**: Dilute HF (1-2%) used in wafer cleaning penetrates skin, attacks bone, causes systemic fluoride poisoning. **Calcium gluconate gel must be on-site before any HF use** — apply immediately to exposed skin and seek emergency treatment. Chemical-resistant gloves (neoprene or nitrile), face shield, and apron required for all HF work. Work in fume hood or with local exhaust ventilation.
- **Wire saw hazards**: 140-180 μm steel wire under tension (15-30 N) traveling at 5-15 m/s can snap and lash. Wire guard mandatory. Abrasive slurry (SiC or diamond) is an eye irritant — safety goggles required during slurry handling.
- **Dust inhalation**: Silicon dust from sawing, lapping, and crushing is a respiratory irritant. Local exhaust ventilation at cutting stations. P100 respirator in dusty areas.

## Wafer Specifications and Quality

**Standard wafer dimensions**:

| Diameter | Thickness | Primary Flat | Typical Weight |
|----------|-----------|-------------|----------------|
| 100 mm (4") | 500-525 μm | 32.5 mm | ~10 g |
| 150 mm (6") | 625-675 μm | 57.5 mm | ~28 g |
| 200 mm (8") | 725-775 μm | Notched | ~53 g |
| 300 mm (12") | 775 ± 25 μm (750-800) | Notched | ~128 g |

**Flat and notch**:
- **Primary flat**: Ground flat along one edge of the wafer, indicating crystal orientation. For <100> wafers, the flat is along the {110} plane. For <111> wafers, the flat indicates the <110> direction. Used for alignment in processing equipment.
- **Secondary flat**: A smaller flat on the opposite edge indicates wafer doping type. One secondary flat = n-type. Two secondary flats = p-type. No secondary flat = <111> n-type reference. This coding system allows operators to identify wafer type visually.
- **[Notch](../glossary/notch.md)** (200 mm and larger): V-shaped notch replaces flats on larger wafers, providing the same orientation information with less wasted silicon at the wafer edge.

**Wafer quality parameters**:
- **Total thickness variation (TTV)**: Maximum difference between thickest and thinnest points on the wafer. After lapping: 2-5 μm. After CMP: <1 μm. Excessive TTV causes focus problems in photolithography.
- **Bow and warp**: Deviation of the wafer center from a reference plane (bow) and the difference between maximum positive and negative deviations (warp). After polishing: bow <25 μm, warp <30 μm for 150 mm wafers. Thermal processing (oxidation, diffusion) can increase warp if thermal stress is non-uniform.
- **Surface particles**: After final clean, particle count target: <10 particles ≥0.3 μm per wafer (for 150 mm). Each particle is a potential device-killing defect. Particle inspection by laser scanning surface inspection system.
- **Surface metal contamination**: <10¹⁰ atoms/cm² for critical metals (Fe, Cu, Ni, Na). Measured by TXRF (total reflection X-ray fluorescence) or VPD-ICP-MS (vapor phase decomposition followed by ICP-MS). Metals at the surface degrade gate oxide integrity and minority carrier lifetime.

## Ingot Shaping and Cropping

**Ingot processing before wafering**:
- **Cropping**: Cut off the seed, neck, shoulder (crown), and tail portions of the pulled crystal with a band saw or diamond wire saw. These portions are either off-spec (neck too thin, tail has high impurity concentration) or not cylindrical (shoulder). Cropped sections are returned to the polysilicon recycle stream.
- **Grinding to diameter**: Grind the cylindrical body to the exact target diameter (e.g., 150.00 ±0.25 mm) on a centerless grinding machine. Diamond grinding wheel removes 0.5-2 mm from the surface. This also removes the outer layer of the crystal, which has higher impurity concentration from crucible contact and surface defects.
- **Orientation flat grinding**: Grind the primary and secondary orientation flats along the crystal length. X-ray diffraction aligns the crystal lattice before grinding to ensure the flat is within ±0.5° of the target crystallographic plane.

## Wafer Sorting and Packaging

**Ingot quality mapping**:
- **Resistivity mapping**: Four-point probe measurement at multiple positions along the ingot length (every 10-25 mm) before slicing. Identifies regions where resistivity is out of specification (high at the seed end due to initial dopant fluctuations, and at the tail end where impurity segregation concentrates dopants). These regions are cropped and discarded or recycled.
- **Minority carrier lifetime measurement**: Microwave photoconductance decay (μ-PCD) or surface photovoltage (SPV) scans the ingot surface. Low lifetime regions indicate high defect density or metallic contamination, which must be excluded from device-grade wafers.
- **Oxygen measurement**: FTIR mapping of the ingot cross-section at several positions along its length. Oxygen varies axially (higher at the seed end, lower at the tail due to progressive crucible thinning).

**Wafer packaging**:
- **Cleanroom packaging**: Wafers are cleaned (RCA clean), inspected, and packaged in a Class 100 (ISO 5) environment. Each wafer is placed in an individual slot of a fluoropolymer wafer carrier (25-wafer cassette is standard). The cassette is sealed in two nested bags (inner bag nitrogen-purged, outer bag for mechanical protection) with a desiccant packet and a cleanliness certificate.
- **Labeling**: Each cassette is labeled with: crystal number, wafer count, diameter, thickness, orientation, dopant type, resistivity range, oxygen range, and batch number for traceability.

**Wafer shipping and handling**:
- Wafers are extremely fragile (silicon is a brittle ceramic). Handle with wafer tweezers or vacuum wands only. Never stack wafers without separators (they scratch each other). Fluoropolymer wafer dividers separate wafers in cassettes. Transport cassettes in padded containers. Open cassette packaging only in a clean environment. Wafers that contact non-clean surfaces or bare hands are permanently contaminated and must be re-cleaned (or discarded if the contamination is embedded).

## Float Zone Detail for Higher Purity

The float zone process produces the purest silicon available, because nothing touches the molten zone. No crucible means no oxygen or carbon contamination from SiO₂ dissolution or graphite outgassing. This makes FZ silicon essential for devices where CZ silicon's 10-20 ppma oxygen is unacceptable.

**RF coil design**:
- 3-turn pancake coil wound from water-cooled copper tube (6-10 mm OD). Coil inner diameter matches the rod diameter with 5-15 mm clearance. Power: 8-15 kW at 2-4 MHz. The molten zone length is 15-25 mm, controlled by coil geometry and RF power. A shorter zone is more stable (less prone to dripping) but limits throughput. A longer zone increases throughput but risks zone collapse under surface tension failure.
- Multiple passes (10-15) are standard for uniform doping distribution. Each pass sweeps the molten zone from bottom to top. Impurities with segregation coefficient k < 1 (most metals) are swept to the top end of the rod with each pass. After all passes, the contaminated top is cropped off.

**Vacuum vs. inert gas operation**:
- Vacuum (10⁻⁵ mbar): volatile impurities (Na, K, S, some metals) evaporate from the molten zone and are pumped away. Best for achieving the highest purity. Requires a vacuum chamber and diffusion or turbomolecular pump capable of handling the outgassing load.
- Argon at 1-3 bar: controlled atmosphere that suppresses evaporation of silicon itself (Si has significant vapor pressure at 1414°C). Used when gas-phase doping is required. The argon pressure also stabilizes the molten zone against convection disturbances.

**Gas doping during FZ**:
- Add PH₃ (phosphine) or B₂H₆ (diborane) to the argon carrier gas flowing through the chamber. The dopant gas dissolves into the molten zone, incorporating into the recrystallized silicon. Concentration controlled by gas flow ratio: ppm-level dopant in argon gives ppm-level doping in the crystal.
- Precise resistivity control: ±5% variation along the rod length, better than CZ's ±10% for n-type. This is because FZ doping is set by gas flow rate (easily controlled) rather than segregation from a finite melt volume.

**FZ advantages over CZ**:
- No crucible contact means oxygen <1 ppma (vs. 10-20 ppma for CZ) and carbon <0.1 ppma (vs. <1 ppma for CZ). This purity translates directly into higher resistivity (up to 50,000 Ω·cm, vs. <100 Ω·cm for standard CZ) and longer minority carrier lifetime (>1000 μs, vs. 100-500 μs for CZ).
- Required for: power semiconductors (thyristors, IGBTs blocking >3 kV), radiation detectors (high purity needed for depletion widths of millimeters), and space-grade components (radiation-hard devices need low oxygen to prevent defect formation under particle bombardment).
- Limitation: maximum diameter ~200 mm. Surface tension cannot stabilize a molten zone larger than this without electromagnetic confinement or other assistance. CZ is used for all 300 mm production.

**Strengths**:
- Gas-phase doping (PH₃ or B₂H₆ in argon) provides ±5% resistivity variation along the rod — better than CZ's ±10% for n-type
- No crucible contact means no metallic contamination source, achieving carbon <0.1 ppma

**Weaknesses**:
- 3-turn pancake RF coil must maintain 5-15 mm clearance around the rod — complex coil geometry and alignment required
- Multiple zone passes (10-15) mean very slow throughput compared to CZ pulling

## Alternative Wafering Methods

**Inner diameter (ID) saw**:
- **Design**: Circular steel blade with diamond-coated inner edge (the blade is a ring, the cutting edge is on the inside of the hole). Blade rotates at 1500-3000 RPM. Ingot pushed through the blade center, one wafer cut at a time.
- **Advantages**: Simpler than wire saw. Each wafer is independent (no wire break ruins a whole batch). Good for small-scale or prototype production.
- **Disadvantages**: Slower than wire saw (1-2 wafers/hour for 150 mm). Kerf loss ~200-300 μm (thicker blade than wire). Blade wear requires periodic redressing. Surface damage layer slightly deeper than wire saw.

**[Laser slicing](../glossary/laser-slicing.md)** (advanced, later stage):
- **Principle**: High-power laser (typically Nd:YAG, 1064 nm) creates a stress crack along a defined plane in the ingot. Subsequent mechanical stress separates the wafer along the crack. No abrasive contact, so surface damage is minimal.
- **Status**: Still in development for mainstream silicon wafering. Used for some hard, brittle materials (SiC, sapphire) where wire saw cutting is extremely slow. Kerf loss is theoretically zero (no material removed by the laser, just a crack initiated).

**Strengths**:
- ID saw is mechanically simple — one blade, one wafer at a time, no complex wire management
- Laser slicing has near-zero kerf loss, potentially saving 40-50% of silicon compared to wire sawing

**Weaknesses**:
- ID saw produces only 1-2 wafers/hour for 150 mm — 10-20× slower than wire saw for total throughput
- Laser slicing is not yet production-ready for silicon, with higher equipment cost and limited throughput compared to wire sawing




## See Also

- [Air Separation](../chemistry/air-separation.md) — argon for inert atmosphere
- [Liquefaction & Storage](../cryogenics/liquefaction-storage.md) — cryogenic gas supply
- [Advanced Glass](../glass/advanced.md) — quartz crucibles for crystal pulling
- [Precision Metrology](../measurement/precision-metrology.md) — crystal orientation measurement
- [Czochralski Pulling](cz-pulling.md) — CZ crystal pulling equipment
- [Wafering](wafering.md) — ingot slicing and wafer polishing
- [Basic Devices](basic-devices.md) — device fabrication from wafers

[← Back to Silicon](index.md)
