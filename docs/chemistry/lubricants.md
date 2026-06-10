# Lubricants, Oils & Fluid Mechanics

> **Node ID**: chemistry.lubricants
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`animals.animal-materials`](../animals/animal-materials.md), [`chemistry.petroleum-alternatives`](petroleum-alternatives.md), [`foundations.tools-basic`](../foundations/tools-basic.md)
> **Enables**: [`energy.gravity`](../energy/gravity.md), [`energy.wind`](../energy/wind.md), [`machine-tools.machining`](../machine-tools/machining.md)
> **Timeline**: Years 0-200+
> **Outputs**: lubricating_oil, grease, cutting_fluid, hydraulic_fluid, vacuum_oil
> **Critical**: No — lubricants extend machine life and reduce friction but are not prerequisites for core capabilities

Every machine with moving parts generates friction and heat. Two metal surfaces pressed together under load touch only at microscopic peaks called asperities. At those contact points, pressures exceed the yield strength of the metal. The surfaces weld together instantaneously, then tear apart as the parts move relative to each other. Each weld-and-tear cycle removes material, generates heat, and creates wear debris that grinds between the surfaces and accelerates further destruction. A plain steel-on-steel bearing running dry has a friction coefficient around 0.8. At moderate speed and load, it generates enough heat to discolor the metal within minutes and seize within hours.

Lubrication interrupts this destructive cycle by interposing a film of material between the surfaces. That film can be a molecular layer of adsorbed fatty acids (boundary lubrication), a thick cushion of fluid oil (hydrodynamic lubrication), a smear of semi-solid grease, or a coating of solid material that shears easily under load. Each approach works best for different combinations of speed, load, temperature, and environment. The friction coefficient drops from 0.8 (dry) to 0.1 (boundary) to 0.001 (hydrodynamic), a factor of 800 improvement that transforms a machine from self-destructing to long-lived.

A civilization rebuilding its industrial base needs lubricants from day one. The first cart axle, the first treadle lathe, the first water pump all need something to reduce friction. The progression runs from animal fats (available immediately) through vegetable oils (first year harvest) to refined mineral oils (once petroleum distillation is established) and finally synthetic fluids (requiring advanced chemical synthesis). Each tier enables more demanding machinery: animal fats suffice for slow, lightly loaded bearings, but high-speed engines, precision machine tools, and vacuum systems require progressively more sophisticated lubricants.

This article covers the lubrication theory shared across all types and links to four focused articles on specific lubricant categories.

## Lubrication Regimes

Diagrammatic sketch of the lubrication system of the Enfield engine*

### Boundary Lubrication

Thin molecular film (1-10 nm) of polar molecules adsorbed on metal surfaces. Fatty acids (from animal/vegetable fats) have a polar head that attaches to the metal oxide surface and a non-polar tail (hydrocarbon chain). The molecules orient perpendicular to the surface, forming a packed monolayer that prevents metal-to-metal contact. This regime dominates at low speed, high load, and intermittent motion, the conditions found in slow-moving machinery, sliding surfaces, and startup/shutdown of faster equipment.

**Effectiveness**: Reduces friction coefficient from ~0.8 (dry steel-on-steel) to ~0.1-0.15. Prevents galling and seizing. The film breaks down above ~150°C (fatty acids desorb and oxidize), which sets the temperature ceiling for organic boundary lubricants.

### Hydrodynamic Lubrication

A full fluid film separates the surfaces. No metal contact occurs. Friction is entirely viscous drag of the fluid. This regime requires three conditions: correct viscosity (thick enough to maintain the film under load, thin enough to flow), adequate speed (generates pressure in the converging wedge of lubricant), and proper bearing geometry (correct clearance and alignment).

**Reynolds equation** governs the film pressure distribution. Simplified for a plain journal bearing: minimum film thickness h_min ≈ (μ × U × d²) / (4 × W), where μ = viscosity, U = surface speed, d = bearing diameter, W = load. Maintain h_min > 3× surface roughness for full film separation.

**Friction coefficient**: ~0.001-0.01 (10-100x lower than boundary). This is why well-lubricated bearings run cool and last years.

**Oil viscosity grades** (ISO VG system): ISO VG 32 = kinematic viscosity 32 cSt at 40°C (light spindle oil). ISO VG 68 = 68 cSt (general machine oil). ISO VG 220 = 220 cSt (gear oil). ISO VG 460 = 460 cSt (heavy gear oil). Higher viscosity means thicker oil, more load capacity, but also more viscous friction and heat generation.

### Elastohydrodynamic Lubrication (EHL)

Occurs in rolling element bearings and gear teeth where contact pressures reach 1-3 GPa. The extreme pressure elastically deforms the metal surfaces and compresses the lubricant, dramatically increasing its viscosity (the pressure-viscosity effect). The result is a thin but extremely stiff film, 0.1-1 μm thick, that separates the surfaces. EHL requires a lubricant with a good pressure-viscosity coefficient. Mineral oils perform well in this regime; water-based lubricants perform poorly.

## Focused Articles

- **[Natural Lubricants: Animal Fats & Vegetable Oils](lubricants-natural.md)** — Rendering tallow and lard from animal fat, pressing vegetable oils (castor, rapeseed, olive, linseed, sunflower). Available from day one. For slow-speed bearings, slides, and cart wheels.
- **[Grease, Solid Lubricants & Bearing Lubrication](lubricants-grease-solid.md)** — Grease production from saponified fats (sodium, calcium, lithium soap thickeners), solid lubricants (graphite, MoS₂, PTFE, polymer bearings), and bearing lubrication methods (oil-ring, wick, splash, forced, grease-packed).
- **[Mineral Oil Lubricants, Cutting Fluids & Hydraulic Fluids](lubricants-mineral.md)** — Refined petroleum lubricants, ISO VG and SAE viscosity grading, cutting fluid formulations (straight oil, soluble oil emulsion, synthetic), hydraulic fluid types (mineral, vegetable, water-glycol).
- **[Synthetic Lubricants & Specialty Fluids](lubricants-synthetic.md)** — PAO, ester, silicone, and PFPE synthetics. Vacuum oils (mineral, silicone, PAO). Cleanroom-compatible PFPE lubricants for semiconductor manufacturing.

## Selection Guide

| Lubricant Type | Viscosity Range (cSt at 40°C) | Temperature Range | Load Capacity | Best Use |
|----------------|-------------------------------|-------------------|---------------|----------|
| Animal fat (tallow/lard) | Semi-solid to ~30 cSt (melted) | 10-60°C | Low to moderate | Slow-speed plain bearings, slides, cart wheels |
| Vegetable oil (rapeseed) | 30-40 cSt | -10 to +80°C | Low to moderate | General-purpose bearings, cutting fluid base |
| Castor oil | ~250 cSt | -10 to +120°C | Moderate to high | High-speed bearings, racing engines |
| Calcium soap grease | NLGI 1-3 | -20 to +90°C | Moderate | Wheel bearings, water pumps, marine equipment |
| Lithium soap grease | NLGI 1-3 | -30 to +190°C | Moderate to high | Multi-purpose: bearings, gears, chassis |
| Clay-thickened grease | NLGI 1-3 | -20 to +250°C | Moderate to high | High-temperature bearings, ovens, kilns |
| Straight cutting oil | 20-50 cSt | Ambient (recirculated) | High (chip-tool) | Tapping, threading, broaching |
| Soluble oil emulsion (5-10%) | ~1-5 cSt (mixed) | Ambient (recirculated) | Low to moderate | General machining, turning, milling |
| Mineral oil (ISO VG 32) | 32 cSt | -10 to +80°C | Moderate | Spindle oils, hydraulic fluid, general bearings |
| Mineral oil (ISO VG 68) | 68 cSt | -10 to +80°C | Moderate to high | General machine oil, moderate-speed gears |
| Mineral oil (ISO VG 220) | 220 cSt | 0 to +90°C | High | Gear oils, heavy-duty gearboxes |
| Hydraulic fluid (mineral) | 32-46 cSt | -10 to +70°C | Moderate to high | Hydraulic presses, machine tools |
| Water-glycol hydraulic fluid | 32-46 cSt | -20 to +60°C | Low to moderate | Fire-risk environments, foundries |
| PAO synthetic | 32-460 cSt | -50 to +175°C | High | Jet engines, Arctic machinery, long-drain oils |
| Ester synthetic | 32-100 cSt | -40 to +200°C | High | Jet engines, compressor oils, biodegradable hydraulics |
| Silicone oil | 10-100,000 cSt | -70 to +250°C | Low | Diffusion pumps, dampers, electrical insulation |
| PFPE | 20-500 cSt | -80 to +300°C | Moderate | Vacuum, semiconductor, oxygen service, spacecraft |
| MoS₂ (solid) | N/A | -180 to +350°C (air) | High (boundary) | Vacuum bearings, space mechanisms, extreme temperature |
| Graphite (solid) | N/A | Up to +450°C (air) | Moderate | High-temperature bearings, gaskets, mold release |
| PTFE (solid) | N/A | -200 to +260°C | Low | Bearing liners, bridge bearings, thread sealing |

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Foundations | Animal fat collection and rendering, basic axle grease for carts and simple machines |
| Metallurgy | Tallow-lubricated bearings for treadle lathes and bellows, vegetable oil extraction |
| Machine Tools | Cutting fluids and machine oils for precision machine tools, grease production |
| Energy | Cylinder oils for steam engines, high-temperature bearing lubrication, hydraulic fluid for presses |
| Chemistry | Chemical processing of oils, soap thickeners for grease, mineral oil refining, synthetic additives |
| Vacuum & Optics | Low-vapor-pressure oils for vacuum pump seals and diffusion pumps |
| Silicon | Ultraclean lubricants for crystal pullers and wafer handling equipment |
| Photolithography | Cleanroom-compatible lubricants and hydraulic fluids for fab equipment, PFPE greases |

## Key Deliverables

- **Tier 1** (Years 0-5): Rendered animal fat (tallow and lard) for slow-speed bearings and slides. Vegetable oil extraction from oilseed crops (rapeseed, castor, olive) for moderate-speed bearings. Linseed oil for protective coatings and paint binder. Basic lubrication practices: regular application, keeping lubricant clean, avoiding abrasive contamination. These natural lubricants suffice for the first workshops, treadle lathes, water wheels, and cart transport.

- **Tier 2** (Years 5-20): Grease production from saponification of fats with alkali (sodium, calcium, lithium soap thickeners). Cutting fluid formulations: soluble oil emulsion for general machining, straight oil for threading and tapping. Solid lubricants (graphite, MoS₂) for machine tool applications where liquid oil is impractical. These processed lubricants enable precision machine tools, threaded fastener production, and bearings that must operate under load for extended periods.

- **Tier 3** (Years 20-50): Mineral oil refining and viscosity grading (ISO VG system). Hydraulic fluid supply for presses and machine tools, transitioning from vegetable oil to mineral oil. Bearing lubrication engineering: PV limits, clearance design, and oil selection by Sommerfeld number. Additive technology (ZDDP, antioxidants, rust inhibitors) that tailors mineral oil performance for specific applications. These industrial fluids enable steam engines, high-speed machinery, hydraulic presses, and continuous-process equipment.

- **Tier 4** (Years 50-200+): Synthetic lubricants (PAO, ester, silicone) for demanding applications in aerospace and extreme environments. Vacuum-compatible oils (mineral for roughing pumps, silicone for diffusion pumps). Cleanroom-compatible PFPE lubricants for semiconductor manufacturing equipment. Oil analysis and condition monitoring programs for predictive maintenance. These advanced lubricants enable jet engines, vacuum systems, semiconductor fabrication, and space applications.

## General Safety & Hazards

- **Hot oil burns**: Lubricating oil at operating temperature can exceed 200°C. Severe splash burns result from contact. Wear face shields and long gloves when handling hot oil. Pour slowly to minimize splashing.
- **Oil fires**: NEVER use water on an oil fire. Water flashes to steam and scatters burning oil. Extinguish with sand, fire blanket, or smothering with a lid. Keep fire extinguishing materials near oil heating operations.
- **Oil mists**: Oil mist from machining operations and mist lubrication systems is a respiratory irritant. Prolonged inhalation can cause lipoid pneumonia. Use ventilation, mist extraction, or enclosures to control airborne oil.
- **Environmental disposal**: Used oil and grease must not be dumped on ground or in waterways. Collect in sealed containers. Re-refine mineral oils (vacuum distillation removes contaminants, additives are replenished). Animal and vegetable oils can be composted in small quantities. Used cutting fluid emulsions require treatment (break emulsion with acid or flocculant, separate oil phase, treat water phase before discharge). Even in a bootstrap economy, contaminating water supplies with oil has long-term consequences for agriculture and drinking water.

## Oil Analysis and Condition Monitoring

Industrial plants monitor lubricant condition to schedule oil changes based on actual condition rather than fixed intervals. Key tests:

1. **Viscosity**: Change >10% indicates oxidation, contamination, or wrong oil grade.
2. **Acid number**: Increase indicates oxidation. Acidic byproducts corrode bearings.
3. **Particle count**: ISO 4406 cleanliness code. Critical for hydraulic systems (target: 16/14/11 for servo valves).
4. **Spectrometric analysis**: ICP or atomic absorption detects wear metals (Fe, Cu, Pb, Sn, Cr) at ppm levels. Trending indicates which component is wearing.
5. **Water content**: Karl Fischer titration. Water causes rust, reduces film strength, and promotes microbial growth. Limits: <0.1% for most systems, <0.03% for turbine oils.

**Sampling**: Always sample from a live oil stream (not from the drain plug or static reservoir). Use clean sample bottles. Sample frequency: monthly for critical equipment (turbines, large gearboxes), quarterly for general plant equipment.

## Limitations

- **Oxidation stability**: Natural oils (animal and vegetable) oxidize much faster than mineral oils. Vegetable oils last 1-2 years in storage; animal fats last 6-12 months. Rancidity increases acidity (corrosion risk) and viscosity (pumping problems). Antioxidants extend shelf life but add cost and complexity.
- **Temperature range**: Every lubricant has a temperature window. Below the pour point, the lubricant is too thick to flow. Above the dropping point (grease) or flash point (oil), the lubricant fails catastrophically. No single lubricant covers the full range from Arctic cold to furnace heat. Equipment designers must select lubricants appropriate to their operating environment.
- **Material compatibility**: Lubricants interact with seals, paints, plastics, and elastomers. Mineral oil swells natural rubber and degrades some plastics. Silicone oil contaminates surfaces and prevents paint adhesion. Synthetic oils can shrink or swell seals designed for mineral oil. Always verify compatibility between lubricant and all materials it contacts.
- **Shelf life**: Store all lubricants in sealed, labeled containers away from heat, sunlight, and moisture. Mineral oils: 5+ year shelf life if uncontaminated. Vegetable oils: 1-2 years (oxidize and become acidic; check acid number before use). Animal fats: 6-12 months (rancidity; refrigeration extends to 2 years). Grease: 2-3 years in sealed containers (oil separation is the primary failure mode; if more than 10% free oil on the surface, discard). Cutting fluid concentrates: 2-5 years. Mixed emulsions: 3-6 months (biological growth is the limiting factor; add biocide and monitor pH weekly).
- **Lubricant degradation in service**: All lubricants degrade during use. Oxidation thickens the oil and deposits varnish. Thermal breakdown at high temperatures produces sludge. Contamination with wear particles, water, and process chemicals reduces lubrication effectiveness. Regular oil analysis and timely replacement are essential for equipment reliability.

## Lubrication Calculations

### Sommerfeld Number (Bearing Design)

The Sommerfeld number (S) is the key dimensionless parameter for journal bearing design. It determines whether a hydrodynamic film can be maintained:

**S = (r/c)² × (μ × N / P)**

Where: r = shaft radius (m), c = radial clearance (m), μ = dynamic viscosity (Pa·s), N = rotational speed (rev/s), P = bearing pressure (Pa) = W/(2×r×L), W = radial load (N), L = bearing length (m).

**Interpretation**: S > 1 indicates full hydrodynamic lubrication (reliable). S = 0.1-1 indicates mixed regime (some metal contact, increased wear). S < 0.1 indicates boundary regime (rapid wear unless boundary lubricants present).

**Example**: 50 mm diameter shaft, 50 mm bearing length, 500 N radial load, 1500 RPM, ISO VG 32 oil (μ ≈ 0.028 Pa·s at 40°C), clearance c = 0.025 mm:
- P = 500 / (0.025 × 0.050) = 400,000 Pa = 0.4 MPa
- S = (25/0.025)² × (0.028 × 25 / 400,000) = 1,000,000 × 0.00175 = 1,750
- S >> 1: Full hydrodynamic film. Bearing operates reliably.

**Same bearing at 100 RPM**: S = 1,750 × (100/1500) = 117. Still hydrodynamic.

**Same bearing at 10 RPM**: S = 1,750 × (10/1500) = 11.7. Still above 1 but approaching mixed regime. Consider higher viscosity oil (ISO VG 68) for very slow speeds.

### Minimum Film Thickness

**h_min ≈ c × (1 - ε)** where ε = eccentricity ratio (0 = concentric, 1 = contact).

For practical design: **h_min > 3× combined surface roughness (R_a)**. Typical surface roughness: ground shaft R_a = 0.4-0.8 μm, bored bearing R_a = 0.8-1.6 μm. Combined roughness ≈ √(R_a1² + R_a2²) ≈ 1.0-1.8 μm. Therefore h_min > 3-5 μm is the minimum for full film separation.

### PV Limit Check

**PV = P × V** (MPa × m/s). Each bearing material has a maximum PV:

| Material | Max PV (MPa·m/s) | Max P (MPa) | Max V (m/s) | Notes |
|----------|-------------------|-------------|-------------|-------|
| PTFE (unfilled) | 0.35 | 7 | 0.5 | Low load, low speed; cold flows above 7 MPa |
| Acetal (Delrin) | 0.15 | 10 | 1.0 | Good for gears and light bearings |
| Nylon 6/6 | 0.10 | 7 | 2.5 | General-purpose polymer bearing |
| Carbon-graphite | 0.50 | 4 | 10 | High temperature, self-lubricating |
| Bronze (phosphor) | 1.75 | 14 | 7.5 | Standard bearing bronze with oil lubrication |
| Babbitt metal | 1.05 | 7 | 7.5 | Soft overlay on steel backing, excellent embeddability |
| Cast iron | 0.35 | 4 | 2.5 | Low-cost, marginal lubrication required |

**Example**: A 50 mm shaft at 300 RPM carrying 2000 N on a 50 mm long bronze bearing:
- P = 2000 / (0.050 × 0.050) = 0.8 MPa
- V = π × 0.050 × 300/60 = 0.785 m/s
- PV = 0.8 × 0.785 = 0.63 MPa·m/s
- Bronze max PV = 1.75 MPa·m/s → OK, adequate margin.

### Oil Viscosity Selection Quick Guide

| Shaft Speed (RPM) | Load Level | ISO VG Grade | Typical Application |
|-------------------|------------|-------------|---------------------|
| >3000 | Light | VG 22-32 | Spindle bearings, turbines |
| 1500-3000 | Light-Moderate | VG 32-46 | Electric motors, pumps |
| 750-1500 | Moderate | VG 46-68 | Machine tools, general machinery |
| 300-750 | Moderate-Heavy | VG 68-100 | Gearboxes, moderate gears |
| 100-300 | Heavy | VG 100-150 | Slow gear drives, heavy bearings |
| <100 | Very Heavy | VG 220-460 | Large gear drives, crusher bearings |

Rule of thumb: select the lowest viscosity that maintains Sommerfeld number >1 at operating temperature. Higher viscosity than necessary wastes energy as viscous friction and generates excess heat.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Plain bearing seizes within hours of operation | Boundary lubrication regime (μ ~0.8 dry) not overcome; viscosity or speed too low for hydrodynamic film | Select oil viscosity to maintain h_min > 3× surface roughness; calculate using h_min ≈ (μ × U × d²)/(4 × W); for 50 mm shaft at 300 RPM use ISO VG 68, at 1500 RPM use ISO VG 32 |
| Animal fat (tallow) lubricant goes rancid in storage | Oxidation of unsaturated fatty acids produces acids and polymers; shelf life 6-12 months at room temperature | Store in sealed, opaque containers in cool, dark place (refrigeration extends to 2 years); clarify by re-melting with water before use; check acidity — discard if visibly moldy or strongly decomposed |
| Calcium soap grease softens and runs at operating temperature | Dropping point of calcium soap grease is only ~90°C — too low for hot-running bearings | Switch to lithium soap grease (dropping point ~190°C) or clay-thickened grease (no dropping point, usable to 250°C+); verify bearing operating temperature before selecting grease type |
| Soluble oil cutting emulsion smells rancid and causes skin irritation | Bacterial growth in 5-10% oil-in-water emulsion; pH has dropped below 8.5 indicating active biodegradation | Monitor emulsion pH weekly (target >8.5); add biocide to suppress bacterial growth; replace emulsion every 3-6 months; empty and clean sump tank before refilling |
| Hydraulic pump fails prematurely with erratic valve operation | Fluid contamination with particles >10 μm; contamination is the primary cause of hydraulic system failure | Install 10-25 μm absolute return-line filter; maintain ISO 4406 cleanliness code 16/14/11 for servo valve systems; flush system before first fill; analyze fluid for particle count quarterly |
| Vacuum pump cannot reach target pressure below 10⁻² Pa | Vacuum oil has high vapor pressure or is contaminated with dissolved gases and process chemicals | Switch to oil with appropriate vapor pressure (silicone vacuum oil ~10⁻⁶ Pa for diffusion pumps); purify oil by filtration (1-5 μm), degassing under vacuum, and adsorption through activated alumina |
| Grease-packed bearing overheats after regreasing | Bearing cavity overfilled (>50% fill causes churning heat); fresh grease mixed with degraded old grease | Fill only 30-50% of bearing cavity with grease; remove old grease completely before repacking; verify NLGI grade matches application (NLGI 2 is typical for general bearings) |
| Vegetable oil hydraulic fluid thickens and causes pump cavitation | Oxidative rancidity increases viscosity; vegetable oils have 1-2 year shelf life and narrow temperature range | Monitor acid number and viscosity regularly; replace fluid at first sign of thickening; switch to mineral oil (ISO VG 32-46) once petroleum refining is available for -10°C to +70°C range |
| Oil analysis shows viscosity increase >10% from baseline | Oil oxidation producing high-molecular-weight polymers and sludge; operating temperature too high for oil grade | Replace oil immediately; check for overheating (oil operating above 80°C accelerates oxidation 2× for every 10°C rise); consider synthetic (PAO, VI 130-150) for high-temperature service |
| MoS₂ solid lubricant coating wears through prematurely in vacuum | MoS₂ wears as a consumable film (0.5-2 μm sputtered coating); graphite is ineffective in vacuum (needs adsorbed water) | Reapply MoS₂ by sputtering (PVD) or bonded coating (MoS₂ + phenolic binder); verify MoS₂ (effective -180 to +350°C in vacuum, up to 800°C in vacuum) vs graphite (poor in vacuum, effective to 450°C in air) |

## See Also

- **[Natural Lubricants](lubricants-natural.md)**: Animal fats and vegetable oils
- **[Grease & Solid Lubricants](lubricants-grease-solid.md)**: Grease production and solid lubricant coatings
- **[Mineral Oil Lubricants](lubricants-mineral.md)**: Petroleum-derived lubricants, cutting fluids, hydraulic fluids
- **[Synthetic Lubricants](lubricants-synthetic.md)**: Engineered lubricants and specialty fluids
- **[Animal Materials](../animals/animal-materials.md)**: Fat and tallow supply for early lubricants
- **[Petrochemicals](petroleum-alternatives.md)**: Petroleum distillation for mineral oil production
- **[Acids](acids.md)**: Acid production for oil refining
- **[Machine Tools](../machine-tools/machining.md)**: Cutting fluid applications in machining
- **Soap Making**: Saponification chemistry for grease thickeners

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Chemistry](./index.md) • [All Domains](../../index.md)*
