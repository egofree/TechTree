# Vulcanization & Hardness Scales

> **Node ID**: polymers.rubber.vulcanization
> **Domain**: Polymers & Composites
> **Dependencies**: None
> **Enables**: [`polymers.rubber`](./rubber.md)
> **Timeline**: Years 5-50
> **Outputs**: vulcanized_elastomers, cured_seals, molded_rubber_parts
> **Critical**: No — vulcanization improves rubber performance but is not on the critical path to semiconductors

Vulcanization converts raw rubber (thermoplastic, sticky, temperature-sensitive) into a durable elastomer with stable mechanical properties. Discovered by Charles Goodyear in 1839, it enables every rubber application that matters: tires, seals, gaskets, hoses, belts, and vibration isolators. Sulfur atoms form covalent bridges (polysulfide chains —Sₓ—, x = 1–8) between adjacent polymer chains at allylic carbon positions, creating a three-dimensional molecular network that prevents permanent chain slippage. Modern cure packages add accelerators (speed the reaction, lower temperatures), activators (zinc oxide + stearic acid), antioxidants/antiozonants (environmental protection), and reinforcing fillers (carbon black, silica — improving tensile strength and abrasion resistance 5–10× over unfilled polymer). See [Rubber Production](./rubber.md) and [Natural Rubber](./natural.md).

## Compounding Ingredients

### Reinforcing Fillers

| Filler | Loading (phr) | Tensile (MPa) | Hardness Δ (Shore A) | Primary Use |
|---|---|---|---|---|
| None (gum stock) | 0 | 17–28 (NR) / 1–3 (SBR) | 30–40 baseline | Reference |
| Carbon black N110 | 40–50 | 25–32 | +20–30 | Tire treads (max abrasion) |
| Carbon black N330 | 30–50 | 20–28 | +15–25 | General purpose |
| Carbon black N660 | 30–50 | 18–25 | +12–20 | Carcass, sidewalls |
| Precipitated silica | 10–30 | 18–24 | +10–15 | Green tires (low roll resist.) |
| Calcium carbonate | 50–100 | 10–15 | +8–12 | Low-cost extension |
| Clay | 30–80 | 10–18 | +5–10 | Low-cost extension |

Carbon black particle size (N110–N990 grades) and structure (DBP absorption) determine reinforcement. Smaller particles give higher tensile strength but harder mixing. Processing oils (aromatic, naphthenic, or paraffinic — matched to polymer type) soften the compound for easier mixing and lower molding viscosity.

### Accelerator Systems

| Accelerator | Abbr. | Phr | Cure Rate | Scorch Safety | Cross-links |
|---|---|---|---|---|---|
| Mercaptobenzothiazole | MBT | 0.5–2.0 | Medium | Low | Polysulfide |
| MBT disulfide | MBTS | 0.5–2.0 | Medium-slow | Medium | Polysulfide |
| N-Cyclohexyl-2-benzothiazole sulfenamide | CBS | 0.5–1.5 | Delayed action | High | Polysulfide |
| N-tert-Butyl-2-benzothiazole sulfenamide | TBBS | 0.5–1.5 | Delayed action | High | Polysulfide |
| Tetramethylthiuram disulfide | TMTD | 0.2–0.5 | Ultra-fast | Low | Short (EV-like) |
| Diphenylguanidine | DPG | 0.3–1.0 | Slow (secondary) | High | Polysulfide |

### Antioxidants and Antiozonants

- **TMQ** (polymerized 2,2,4-trimethyl-1,2-dihydroquinoline): 1–2 phr. General-purpose antioxidant, prevents oxidative chain scission.
- **6PPD** (N-(1,3-dimethylbutyl)-N'-phenyl-p-phenylenediamine): 1–3 phr. Combined antioxidant/antiozonant. Migrates to surface to react with ozone before it attacks the polymer backbone.
- **Wax** (paraffin or microcrystalline, 1–2 phr): Blooms to surface forming a physical ozone barrier. Effective for static seals only (flexing breaks the film).

## Equipment

- **Banbury internal mixer**: Two counter-rotating rotors in a water-cooled chamber. Batch: 50–200 kg in 3–8 min. Generates enough shear to raise temperature to 160°C in under 5 min — why two-stage mixing (masterbatch first, curatives second) is essential.
- **Two-roll mill**: Counter-rotating steel rolls with adjustable gap. For sheeting, blending, and adding heat-sensitive curatives to warm compound without scorch.
- **[Compression molding press](../machine-tools/compression-press.md)**: [Hydraulic press](../machine-tools/hydraulic-press.md), 10–200 tons. Steam/oil/electric heated platens, ±2°C control. Load preform, close press, cure, demold. Cycle: 5–60 min depending on thickness (cure time scales ~ with square of thickest section).
- **Transfer molding**: Preform in pot above cavity; plunger forces rubber through runners. Better dimensional accuracy for complex shapes with inserts. Runner waste: 5–15%.
- **Injection molding**: Screw plasticates rubber at 60–90°C (scorch safety), injects at 50–200 MPa. Fastest cycle: 2–10 min total. Best consistency, lowest flash.
- **Autoclave (steam pan)**: 3–10 bar steam (134–180°C) for hoses, belts, extruded profiles. Batch: 30–120 min.

## Step-by-Step Procedure

1. **Weighing**: All ingredients per formulation card. A 10% error in accelerator shifts cure time by 30%. Typical: 10–20 ingredients per compound.
2. **Masterbatch mixing (Banbury)**: Load raw rubber, masticate 30–60 sec. Add fillers, oil, ZnO, stearic acid sequentially at 40–80 RPM. Temperature rises to 130–160°C from shear. Dump onto two-roll mill, sheet off. This non-curable masterbatch contains everything except curatives.
3. **Final mixing (two-roll mill or Banbury)**: Add masterbatch + sulfur, accelerators, heat-sensitive additives. Temperature must stay below scorch point (~110°C). Two-roll mill preferred for visual inspection of dispersion.
4. **Shaping**: Extrusion (profiles, hoses), calendering (sheet, fabric coating), or pre-forming (cutting blanks). Time-sensitive — scorch clock running. Shaping equipment must be near mixing area and presses.
5. **Curing (compression molding)**: Place blank in mold, close press at 10–20 MPa, heat to cure temperature (150–180°C), hold for calculated cure time. General rule: ~1 min/mm thickness at 160°C. Undercure = spongy center; overcure = reversion (NR) or excessive hardness.
6. **Demolding**: Remove cured part. Trim flash by hand, cryogenic deflashing (LN₂ at −80 to −120°C embrittles flash), or buffing.
7. **Post-cure (optional)**: Hot air oven, 4–24 hrs at 150–250°C. Standard for peroxide-cured parts, FKM, silicone, and seal applications requiring low compression set.

## Cure Systems

### Cross-link Types

| Cross-link Type | Sulfur Chain | Thermal Stability | Strength | Fatigue |
|---|---|---|---|---|
| Polysulfide (x ≥ 3) | Long | Low (breaks >130°C) | High tear | Excellent |
| Disulfide (—S₂—) | Medium | Medium | Good | Good |
| Monosulfide (—S—) | Short | High (stable to 160°C) | Lower tear | Moderate |
| Carbon-carbon (peroxide) | None | Very high (>200°C) | Moderate | Lower |

### Conventional Vulcanization (CV)

Sulfur 2.0–3.5 phr, accelerator 0.5–1.5 phr (CBS/TBBS), ZnO 5 phr, stearic acid 2 phr. Predominantly polysulfide cross-links (x = 4–8). Excellent fatigue resistance, high tear strength, lower thermal stability. Tire carcasses, sidewalls, conveyor belts. 140–160°C, 10–30 min.

### Efficient Vulcanization (EV)

Sulfur 0.4–0.8 phr, accelerator 3.0–5.0 phr. Predominantly mono-/disulfide. Superior thermal stability, lower reversion, lower fatigue. Engine mounts, high-temp seals, radiator hoses. 150–170°C, 8–20 min.

### Semi-Efficient Vulcanization (SEV)

Sulfur 1.0–1.8 phr, accelerator 1.5–3.0 phr. Mixed cross-links. Balance of CV and EV. General molded goods, O-rings, gaskets. 140–160°C, 10–25 min.

### Non-Sulfur Systems

- **Peroxide cure**: Dicumyl peroxide (DCP) 1–3 phr, decomposes at 150–175°C creating C–C cross-links. Stable >200°C. No sulfur odor. For silicone, EPDM, specialty compounds. Cannot cure in contact with air (use mold or N₂). Incompatible with many antioxidants. Peroxide-cured NR suffers chain scission.
- **Metal oxide cure**: ZnO 5 + MgO 4 phr for neoprene. MgO scavenges HCl. No sulfur needed.
- **Bisphenol cure**: Bisphenol AF + phosphonium salt for FKM. Requires post-cure 200–250°C, 4–24 hrs.
- **Radiation cure**: Electron beam or gamma radiation creates C–C cross-links without heat or chemicals. For wire/cable insulation. High capital cost, no byproducts.
- **Resin cure**: Alkylphenol-formaldehyde resins crosslink butyl rubber and EPDM. Non-staining, heat-resistant. Tire inner liners, curing bladders.

## Cure Parameters by Rubber Type

| Rubber Type | Cure Agent | Temp (°C) | Time (min) | Pressure (MPa) | Notes |
|---|---|---|---|---|---|
| NR | Sulfur 2–3 phr | 140–160 | 15–60 | 5–20 | CV; reversion above optimum |
| SBR | Sulfur 1.5–2.5 phr | 150–170 | 10–30 | 5–20 | Less reversion than NR |
| NBR | Sulfur 1.5–2.0 phr | 150–170 | 10–25 | 5–20 | Metal oxide co-cure possible |
| Neoprene (CR) | ZnO 5 + MgO 4 phr | 150–180 | 5–20 | 5–20 | Metal oxide cure |
| EPDM | Sulfur 1–2 phr or peroxide | 160–180 | 8–20 | 5–20 | Peroxide for better heat aging |
| Silicone (VMQ) | Peroxide 0.5–2% | 150–175 | 5–15 | 5–15 | Pt-catalyst for LSR |
| FKM (Viton) | Bisphenol or peroxide | 170–200 | 5–15 | 7–20 | Post-cure 200–250°C |
| Butyl (IIR) | Sulfur 1.5–2.5 phr | 150–170 | 15–30 | 5–20 | Halobutyl cures faster |

## Cure Monitoring and Control

**Oscillating Disc Rheometer (ODR) / Moving Die Rheometer (MDR)**: 5–10 g sample heated to test temperature in sealed die. Disc oscillates at ±0.5° or ±1°; torque measured continuously. Key readings:

- **Minimum torque (M_L)**: Compound viscosity before cure — processability indicator.
- **Scorch time (t_s2)**: Time for torque to rise 2 dNm above M_L — the safe processing window.
- **Cure time (t_90)**: Time to 90% of total rise (M_H − M_L) — practical production cure time.
- **Maximum torque (M_H)**: Related to cross-link density and final modulus.
- **Reversion**: Torque decrease after M_H (common with NR at high temperature) — cross-links breaking.

**Production cure time** = t_90 + 10–20% safety margin. For thick parts: add ~1 min/mm above 3 mm thickness.

## Hardness Scales

Rubber hardness = depth of indentation of a standardized indenter under specified force.

**Shore A** (soft to medium elastomers): Range 0–100 (practical: 20–95). Truncated cone indenter (35° apex, 0.79 mm flat tip). Spring force 0.55–8.05 N.

| Shore A Range | Feel / Application |
|---|---|
| 20–30 | Very soft: gel insoles, erasers |
| 40–50 | Soft: sponge rubber, rubber bands (~A35–A45) |
| 50–60 | Medium-soft: weatherstripping, shoe soles (~A50–A65) |
| 60–70 | Medium: general seals, O-rings, tire tread (~A60–A70) |
| 70–80 | Medium-hard: industrial O-rings, conveyor covers, drive belt teeth |
| 80–90 | Hard: bushings, printing rolls, shoe heels |
| 90–95 | Very hard: ebonite range, hard wheel materials |

**Shore D** (hard rubber and rigid plastics): Range 0–100 (practical: 30–85). Sharp cone (30° apex). Spring force 0–44.5 N.

**Scale overlap**: Shore A 95 ≈ D 35 · A 98 ≈ D 45 · A 100 ≈ D 55

**O-ring/seal hardness selection**:

| Application | Shore A | Reasoning |
|---|---|---|
| Low-pressure static seals | 40–50 | Conforms to irregular surfaces |
| General-purpose O-rings | 70 | AS568 standard default |
| High-pressure dynamic seals | 80–90 | Resists extrusion into gaps |
| Rotary shaft seals | 70–80 | Seal force vs. wear balance |
| Vibration isolators | 40–60 | Low stiffness for max isolation |
| Backup rings | 85–95 | High modulus prevents extrusion |

## Vulcanizate Properties

**Effect of carbon black loading on NR** (CV: 2.5 phr sulfur, 0.6 phr CBS):

| CB (phr) | Grade | Shore A | Tensile (MPa) | 300% Modulus (MPa) | Elong. (%) | Tear (kN/m) | Abrasion (mm³) |
|---|---|---|---|---|---|---|---|
| 0 (gum) | — | 35–40 | 20–28 | 1–2 | 700–800 | 20–30 | 300–500 |
| 20 | N330 | 45–50 | 25–30 | 4–6 | 600–700 | 35–45 | 150–250 |
| 40 | N330 | 55–60 | 28–32 | 8–12 | 500–600 | 45–55 | 80–150 |
| 60 | N330 | 65–72 | 25–30 | 12–18 | 400–500 | 40–50 | 60–120 |
| 80 | N330 | 75–82 | 22–28 | 16–22 | 300–400 | 35–45 | 80–140 |

Tensile peaks at 40–50 phr (optimal polymer-filler adsorption); above 60 phr, filler crowding creates stress concentrations reducing strength.

**Effect of crosslink density** (NR, 50 phr N330):

| Sulfur (phr) | CBS (phr) | Crosslink | Shore A | Tensile (MPa) | Elong. (%) | Comp. Set 22h/70°C (%) |
|---|---|---|---|---|---|---|
| 2.5 (CV) | 0.6 | Polysulfidic (x=4–6) | 60–65 | 28–32 | 500–600 | 20–30 |
| 1.5 (semi-EV) | 1.2 | Mixed (x=2–4) | 60–65 | 26–30 | 450–550 | 15–25 |
| 0.5 (EV) | 2.5 | Monosulfidic (x=1) | 60–65 | 24–28 | 400–500 | 10–20 |
| 0 (peroxide) | — | C–C direct | 60–65 | 22–26 | 350–450 | 8–15 |

Hardness stays constant because CB loading is fixed. CV gives best fatigue (flexible polysulfidic bridges); peroxide gives best compression set and heat resistance (C–C stable to 250°C).

## Cure Schedules by Part Thickness

Rubber is a thermal insulator (~0.15 W/m·K). Center of thick parts heats slowly — outer surface cures first and insulates the core.

| Thickness | 150°C | 160°C | 170°C | Notes |
|---|---|---|---|---|
| 2 mm | 4–6 min | 3–4 min | 2–3 min | Thin parts cure fast |
| 5 mm | 7–10 min | 5–7 min | 4–5 min | Standard O-ring |
| 10 mm | 12–18 min | 8–12 min | 6–8 min | ~1 min/mm at 160°C |
| 20 mm | 20–30 min | 15–20 min | 10–15 min | Engine mounts |
| 50 mm | 45–60 min | 30–45 min | 20–30 min | Large bushings |
| 100 mm | 90–120 min | 60–90 min | 45–60 min | Solid tires, rollers |

**Test for undercure**: Slice through thickest section; if center indents easily with a fingernail and feels tacky, it is undercured (reduces tensile 30–60%, compression set 50–80%).

## Reversion and Overcure

NR undergoes reversion when overcured — polysulfide cross-links thermally break, main chain undergoes scission. Indicators: decreasing rheometer torque after peak, soft/sticky demolded surface, reduced tensile strength, darkened color. **Prevention**: Use EV systems (lower sulfur, higher accelerator) for high-temperature applications. Tradeoff: EV has lower tear strength and fatigue resistance. Synthetic rubbers (SBR, BR, NBR) are less prone to reversion — one reason SBR is blended with NR in tires.

## Post-Cure Processing

- **Deflashing**: Manual trimming (labor-intensive), cryogenic deflashing (LN₂ at −80 to −120°C embrittles flash, tumbled with media), or buffing (abrasive wheel for precision surfaces).
- **Post-cure oven**: Essential for FKM (without it, compression set >50% vs. <25% after proper post-cure), silicone, and peroxide-cured compounds. 200–250°C, 4–24 hrs in circulating air. Drives off volatiles and completes residual cross-linking.

## Safety

- **Thermal burns**: Platens at 140–180°C, autoclave steam at 3–10 bar. Steam burns are severe due to latent heat (2260 kJ/kg). Thermal gloves, face shields, long sleeves mandatory.
- **Press crush hazard**: 10–20 MPa pressure. Two-hand trip systems, light curtains, or interlocking guards required.
- **Sulfur dioxide**: Released during cure, especially from sulfur-rich systems. Respiratory irritant. Local exhaust ventilation at each press (15–20 air changes/hr).
- **Accelerator sensitization**: Thiazoles and thiurams cause persistent allergic contact dermatitis. Gloves mandatory. Use nitrosamine-safe alternatives (TBzTD, ZBEC) where possible.
- **Carbon black dust**: IARC Group 2B (possible carcinogen). MEC ~35 g/m³ (sulfur), 50–100 g/m³ (CB). Ground equipment, LEV, respirators (N95/P100, fit-tested). Closed feed systems for Banbury mixers.
- **PPE**: Nitrile gloves (chemicals), Kevlar/aramid gloves (hot parts), safety glasses with side shields, steel-toe boots with metatarsal guards near presses.
- **Emergencies**: Press entrapment — emergency stop + means to open under load. Sulfur fire — dry chemical or CO₂ (not water on molten sulfur). Chemical spill — absorbent, hazardous waste collection.

## Quality Control

### Acceptance Criteria

- **Elastomers**: Tensile, elongation, Shore A hardness within spec. Compression set below max (typically 20–35% after 22h @ 70°C).
- **Seals**: Dimensions ±0.1–0.5 mm. No flash, porosity, or defects. Hardness ±5 Shore A.
- **Molded parts**: Complete cavity fill, no short-shots or knit lines.

### Testing Methods

- **Shore A durometer**: Quick, non-destructive. Three readings averaged. Min 6 mm thickness (ASTM D2240); stack thin parts.
- **Stress-strain (ASTM D412)**: Dumbbell specimen, pull to break. Tensile, elongation, modulus at 100/300%. Curve shape reveals filler reinforcement and crosslink density.
- **Compression set (ASTM D395)**: 25% compression, 22h at service temperature. Below 20% = well-cured; above 35% suggests undercure or poor bonding.
- **Cure rheometer (MDR, ASTM D5289)**: Uncured sample between oscillating dies. Defines scorch time, t_90, M_H. The gate between compounding and production.
- **Visual inspection**: Flash, porosity, short-shots, knit lines. Optical comparators or machine vision for high-volume.

### Sampling Protocol

- MDR on every batch before release to molding floor (~15 min test). Failed MDR = rejected or adjusted.
- Shore A on first 3 parts per mold at start of each shift. Control chart tracking.
- Tensile + compression set on one cured slab per batch per day.
- Visual inspection of every part (or statistical sampling with AQL limits for high volume).

## Scaling Notes

- **Bench**: 10–20 ton platen press, hand-loaded. ~dozen parts/hr. Prototyping, formulation development.
- **Pilot**: 50–200 ton press, multi-cavity, semi-automatic. 100–500 parts/hr.
- **Production (compression/transfer)**: 200–1000 ton battery, robotic extractors. Thousands of parts/hr per line.
- **Production (injection)**: 500–2000 ton machines, 1–5 min cycles. Best consistency, highest tooling cost.
- **Continuous vulcanization**: Extruded profiles through salt bath, microwave tunnel, or fluidized bed. Meters per minute.

Cure time is set by chemistry and thickness — it doesn't decrease with scale. Throughput comes from more cavities, more presses, or faster formulations. Compound shelf life (1–4 weeks with curatives, extendable to 8 weeks refrigerated at 10–15°C) means compounding and molding must be coordinated — ideally on the same site with just-in-time delivery.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Undercure (tacky, spongy) | Insufficient time/temp, aged accelerator | Check MDR; increase cure time; verify mold temp; check curative addition |
| Overcure (hard, brittle) | Excessive time/temp or sulfur | Reduce time; lower sulfur; use delayed-action accelerator |
| Reversion (NR softening) | Prolonged high temp breaking crosslinks | Reduce time/temp; switch to EV; consider SBR/BR blend |
| Porosity (bubbles) | Trapped air/moisture, poor venting | Pre-dry compound; add mold vents; increase press pressure; vacuum assist |
| Poor adhesion to insert | Contaminated surface, inadequate plating | Solvent clean; verify brass plating; apply bonding agent (Chemlok) |
| Blooming (white deposit) | Excess unreacted sulfur/accelerator | Reduce curative below solubility; use EV system |
| Flash too thick | Low pressure, worn mold faces | Increase pressure; refinish mold; check blank weight |
| Backrinding (parting-line tears) | Rubber expanding before crosslink stabilizes | Lower mold temp, extend cure; pre-warm blank; relocate parting line |
| Air trapping (thick-section voids) | Air sealed before vents clear | Add vents; use transfer molding; vacuum assist |
| Surface roughness (orange peel) | High viscosity, turbulent flow | Lower Mooney viscosity; raise mold temp; polish mold surface |

Start troubleshooting with the MDR trace: if compound is in spec, the problem is in molding (temp, pressure, venting). If MDR is out of spec, the problem is in compounding (weighing, mixing, raw material variation).

## See Also

- [Rubber Production](rubber.md) — overview of rubber and elastomers
- [Natural Rubber](natural.md) — raw rubber extraction and basic vulcanization
- [Synthetic Polymers](synthetic.md) — synthetic rubber types and their cure systems
- [Semiconductor Applications](rubber.semiconductor-apps.md) — elastomers in semiconductor equipment
- [Acids & Chemistry](../chemistry/acids.md) — sulfur production for vulcanization
- [Charcoal](../energy/charcoal.md) — carbon black from charcoal processes
- [Machine Tools / Joining](../machine-tools/joining.md) — press equipment for molding

---
*Part of the [Bootciv Tech Tree](../index.md) · [Polymers](./index.md) · [All Domains](../index.md)*
