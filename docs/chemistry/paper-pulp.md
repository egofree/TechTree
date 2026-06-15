# Paper & Pulp Production

> **Node ID**: chemistry.paper-pulp
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.acids`](./acids.md)
> **Enables**: None
> **Timeline**: Years 15-35
> **Outputs**: paper
> **Critical**: Yes — paper enables record-keeping, technical drawings, filtration, and electrical insulation; chemical pulping is the gate from mechanical pulp to strong, durable fiber.

## Overview

Paper and pulp production converts wood fiber into cellulose pulp and then into continuous sheet paper. Two chemical pulping routes dominate industrial practice:

- **Kraft (sulfate) process** — cooks wood chips in white liquor (NaOH + Na₂S) at 160-180°C and 0.6-1.0 MPa. Achieves >90% lignin removal with chemical recovery via black liquor combustion in the recovery boiler. Produces the strongest fiber and tolerates many wood species, including resin-rich softwoods that defeat the sulfite process.
- **Sulfite process** — uses acid sulfite cooking liquor (Ca/Mg/Na bisulfite with free SO₂) at 125-145°C. Produces brighter pulp but is restricted to low-resin wood species (spruce, fir, hemlock).

Chemical pulping differs from mechanical pulping (groundwood): mechanical pulping physically tears fibers from wood, leaving lignin intact. The result is high-yield (90-95%) but weak, short-fibered pulp that yellows rapidly (lignin oxidizes in light). Chemical pulping dissolves lignin, leaving long, strong cellulose fibers at lower yield (45-55%) but with far superior strength, brightness stability, and longevity.

After pulping, the cellulose mat is formed, pressed, and dried on a Fourdrinier machine into a continuous paper sheet. The recovery boiler is the heart of a Kraft mill — it burns the spent pulping liquor (black liquor) to recover inorganic pulping chemicals (Na₂CO₃ + Na₂S) as a molten smelt, while generating process steam. This chemical recovery loop makes the Kraft process economically and environmentally viable — without it, pulping chemicals would be consumed at unsustainable cost.

## Prerequisites

### Materials

- [Wood chips](../foundations/sawmilling.md) — hardwood (eucalyptus, birch, aspen) or softwood (pine, spruce, fir) furnish, chipped to 15-25 mm
- [White liquor chemicals](./alkalis.md) — NaOH + Na₂S for Kraft process; prepared from soda ash, salt cake (Na₂SO₄), and lime
- [Sulfur dioxide / sulfurous acid](./acids.md) — for the sulfite cooking liquor base (Ca, Mg, Na, or ammonium bisulfite)
- [Bleaching chemicals](./chlor-alkali.md) — chlorine dioxide (ClO₂), oxygen (O₂), ozone (O₃), hydrogen peroxide (H₂O₂) for multi-stage bleaching to brightness

### Tools and Equipment

- [Pressure digester](reactor-vessel.md) — rated for 1.0+ MPa steam; batch (Kamyr) or continuous (Kamy continuous digester) types. Welded steel construction, acid-resistant lining for sulfite.
- [Recovery boiler](../energy/boiler.md) — burns black liquor to recover Na₂CO₃/Na₂S smelt; rated for 850-900°C smelt bed, 4-8 MPa steam generation
- [Causticizing plant](./alkalis.md) — converts recovered Na₂CO₃ to NaOH using CaO (CaCO₃ → CaO at 1000-1200°C in lime kiln, then Na₂CO₃ + Ca(OH)₂ → 2NaOH + CaCO₃)
- Fourdrinier paper machine — forming wire (80-100 mesh), press felt, dryer cans (steam-heated cast iron cylinders, 1.5-6 m diameter), calender stack
- [Evaporator](evaporator.md) — multi-effect evaporator to concentrate black liquor from 15% to 65-80% solids before combustion

### Knowledge

- Lignin-cellulose chemistry: lignin is a cross-linked phenolic polymer binding cellulose fibers. Kraft cooking with NaOH + Na₂S cleaves ether bonds in lignin (the hydrosulfide ion HS⁻ is the active nucleophile), dissolving it into alkali-soluble fragments.
- H-factor: a composite temperature-time integral used to control cook degree. H-factor = ∫exp(43.2 − 16113/T) dt, where T is in Kelvin. Target H-factor 800-2,000 for softwood Kraft.
- Kappa number: measures residual lignin in pulp. Kappa 25-35 for unbleached softwood Kraft (shipping sack, linerboard); Kappa 15-25 for bleachable grade; Kappa <5 after full bleaching.
- Stock approach flow dynamics: headbox consistency 0.3-1.0%, jet speed 300-1,200 m/min matching wire speed to within ±1% for optimal formation.

### Infrastructure

- Steam supply: a Kraft mill is energy-self-sufficient — the recovery boiler generates 4-8 MPa steam from black liquor combustion, driving turbogenerators for electricity and process steam.
- Water supply: 50-150 m³ water per tonne pulp (Kraft), 80-200 m³ per tonne pulp (sulfite — more washing required).
- Wastewater treatment: biological treatment for effluent BOD (5-20 kg/tonne pulp). Bleach plant effluent contains chlorinated organics (AOX) — reduced by elemental chlorine-free (ECF) or totally chlorine-free (TCF) bleaching.

## Bill of Materials

| Material | Quantity per tonne pulp | Source | Alternatives |
|----------|------------------------|--------|-------------|
| Wood chips (softwood) | 2.0-2.2 t (bone dry) | [Sawmilling](../foundations/sawmilling.md) — pine, spruce, fir | Hardwood chips (2.2-2.5 t, shorter fiber, lower strength) |
| White liquor (as Na₂O) | 0.15-0.20 t active alkali per t pulp | [Alkali production](alkalis.md) — NaOH + Na₂S | Recovered and recycled (>95% in Kraft) |
| Salt cake (Na₂SO₄ makeup) | 5-15 kg per t pulp | [Mining](../mining/index.md) — natural sulfate deposits | Recovered from flue gas |
| Lime (CaO) | 20-40 kg per t pulp (causticizing makeup) | [Limestone quarry](../mining/index.md) — calcined at 1000-1200°C | — |
| Process water | 50-150 m³ per t pulp | [Water treatment](water-treatment.md) — fresh water | Recycled process water (closed white water system reduces fresh intake 50-80%) |
| Steam | 8-15 GJ per t pulp | Recovery boiler (self-generated) | External boilers for startup/supplement |
| Bleaching chemicals (ClO₂) | 5-15 kg per t pulp (ECF) | [Chlor-alkali](chlor-alkali.md) — on-site ClO₂ generation | Oxygen delignification (2-5 kg O₂/t), peroxide (5-10 kg H₂O₂/t), ozone (2-5 kg O₃/t) for TCF |
| Electrical energy | 600-1,200 kWh per t pulp | Recovery boiler turbogenerator (self-generated) + grid | — |

## Process Description

### Kraft Pulping — Batch Digester

1. Screen wood chips to 15-25 mm; reject fines (used for fuel) and oversize (re-chip). Chip thickness uniformity is critical — over-thick chips undercook, producing shives (uncooked fiber bundles).
2. Fill the digester with screened chips. Impregnate with warm black liquor (120-130°C) for 15-30 minutes to pre-wet and begin lignin softening. Air is vented to allow liquor penetration.
3. Add white liquor (NaOH + Na₂S) to the digester. Target active alkali charge: 15-22% on wood (as Na₂O). Sulfidity (Na₂S / (NaOH + Na₂S)): 25-35% for softwood, 20-30% for hardwood.
4. Heat to 160-180°C at 0.6-1.0 MPa using direct steam injection or indirect heating coils. Heating rate: 0.5-1.5°C/minute. Temperature above 180°C degrades cellulose (peeling reaction).
5. Hold at target temperature for 1-3 hours. Cook to target H-factor (800-2,000 for softwood, 400-800 for hardwood). Monitor by sampling for Kappa number.
6. Discharge (blow) the contents to a blow tank at reduced pressure. The sudden pressure drop fluffs and separates the fibers. Relief vapors (turpentine, methanol, TRS gases) are condensed and collected.
7. Wash pulp counter-currently in rotary vacuum washers or diffusion washers. Target: residual soda in washed pulp <5 kg Na₂O per tonne pulp. The spent liquor (black liquor, 14-18% solids) goes to recovery.
8. Screen and clean the pulp: pressure screens remove shives and uncooked knots. Centrifugal cleaners remove dirt and dense contaminants.

### Kraft Chemical Recovery

9. Concentrate black liquor in multi-effect evaporators from 14-18% to 65-80% solids. Heavy black liquor is mixed with salt cake (Na₂SO₄ makeup) and sprayed into the recovery boiler.
10. Burn the concentrated black liquor in the recovery boiler at 850-1100°C. Organics burn for energy; inorganics form a molten smelt (Na₂CO₃ + Na₂S) at the furnace bottom. Smelt flows through spouts to the dissolving tank.
11. Dissolve smelt in weak white liquor (dilute NaOH) to form green liquor (Na₂CO₃ + Na₂S + NaOH). **SAFETY: smelt-water contact is explosive. Never allow water to contact molten smelt.**
12. Causticize green liquor: add slaked lime (Ca(OH)₂). Reaction: Na₂CO₃ + Ca(OH)₂ → 2NaOH + CaCO₃. The resulting white liquor (NaOH + Na₂S) is returned to step 3.
13. Filter CaCO₃ (lime mud), wash, and feed to the lime kiln. Calcine at 1000-1200°C: CaCO₃ → CaO + CO₂. Slake the quicklime: CaO + H₂O → Ca(OH)₂. Return to step 12.

### Paper Machine (Fourdrinier)

14. Dilute pulp stock to 0.3-1.0% consistency with recycled white water. Add refining energy (10-50 kWh/t in a conical or disc refiner) to develop fiber bonding.
15. Clean the stock with pressure screens and centrifugal cleaners. Add sizing agents (rosin-alum or AKD), fillers (clay, CaCO₃, TiO₂ at 5-25% of fiber weight), and retention aids.
16. Feed stock to the headbox; distribute uniformly across the machine width (2-10 m). Jet speed matches wire speed to within ±1% for good formation.
17. Drain on the forming wire (Fourdrinier table): gravity drainage, then suction from foil blades and vacuum boxes. Consistency increases from 0.5% to 15-22% at the couch roll.
18. Press the wet web in the press section: 2-3 press nips with felt blankets. Water is squeezed from the sheet into the felt. Sheet dryness after pressing: 40-50%.
19. Dry on steam-heated cylinders (dryer cans): 30-60 cylinders at 0.1-0.4 MPa steam pressure. Sheet dryness increases from 45% to 92-95% dry. Energy: 1.3-1.6 kg steam per kg water evaporated.
20. Calender the sheet (optional): pass through heated steel-nip rolls to smooth and densify the surface. Surface smoothness improves printability.
21. Reel the finished paper on a winder drum. Trim and slit to customer width. Core diameter: 75-150 mm. Roll weight: 10-40 tonnes.

## Quantitative Parameters

| Parameter | Kraft (Softwood) | Kraft (Hardwood) | Sulfite (Softwood) |
|-----------|------------------|-------------------|---------------------|
| Cooking temperature | 160-180°C | 160-170°C | 125-145°C |
| Cooking pressure | 0.6-1.0 MPa | 0.6-0.9 MPa | 0.5-0.7 MPa |
| Cooking time | 1-3 hours | 1-2 hours | 4-8 hours |
| Active alkali charge (% Na₂O on wood) | 15-22% | 14-18% | — |
| Sulfidity (%) | 25-35% | 20-30% | — |
| Total SO₂ charge (% on wood) | — | — | 15-25% |
| Pulp yield | 45-50% | 50-55% | 50-55% |
| Lignin removal | >90% | >85% | 80-90% |
| Unbleached Kappa number | 25-35 | 15-25 | 15-25 |
| Chemical recovery | >95% | >95% | 70-85% |
| Bleached brightness (ISO) | 88-92% | 88-92% | 85-90% |
| Fiber length (average) | 2.5-4.0 mm | 0.7-1.5 mm | 2.0-3.5 mm |
| Tensile index (Nm/g) | 60-90 | 40-60 | 50-70 |

### Fourdrinier Machine Parameters

| Parameter | Fine Paper | Newsprint | Linerboard |
|-----------|-----------|-----------|------------|
| Machine speed | 600-1,200 m/min | 900-1,800 m/min | 200-600 m/min |
| Trim width | 4-8 m | 5-10 m | 3-6 m |
| Basis weight range | 40-120 g/m² | 40-50 g/m² | 125-400 g/m² |
| Headbox consistency | 0.5-1.0% | 0.6-1.2% | 0.3-0.7% |
| Press exit dryness | 42-48% | 40-45% | 38-42% |
| Reel dryness | 92-95% | 90-93% | 92-94% |
| Steam per tonne paper | 1.5-2.5 t | 1.2-2.0 t | 1.8-3.0 t |
| Production rate | 100-300 t/day | 200-500 t/day | 150-400 t/day |

## Scaling Notes

- **Bench scale**: 5-50 kg/batch laboratory digesters (Parr reactor or rotating bombs). Used for wood species evaluation, cooking kinetics, and Kappa number optimization.
- **Pilot scale**: 1-10 tonnes/day batch digester with small recovery boiler (package boiler modified for black liquor). Validates chemical recovery and paper machine runnability. Typically produces 50-200 kg paper rolls.
- **Production scale**: 200-2,000 tonnes air-dry pulp/day. A modern Kraft mill produces 1,000-3,000 t/day from a single continuous digester line. Recovery boiler capacity: 2,000-7,000 t black liquor solids/day.

Key scaling considerations:

- **Heat transfer**: Digester heating scales with surface area, not volume. Large digesters use indirect heating (external heat exchangers with forced liquor circulation) rather than direct steam injection to avoid diluting the liquor.
- **Recovery boiler bottleneck**: The recovery boiler is typically the rate-limiting equipment in a Kraft mill. Mill capacity = recovery boiler solids capacity / black liquor solids per tonne pulp. Increasing paper machine speed beyond recovery boiler capacity requires purchasing market pulp.
- **Minimum economic scale**: ~200 tonnes/day for an integrated Kraft mill (pulp + paper). Below this, chemical recovery is uneconomic. Non-integrated mills (market pulp only) need 500+ t/day.
- **Paper machine width**: Machine width is the primary scale lever — wider machines produce more paper per meter of speed. Modern machines are 8-10 m wide; older machines are 3-5 m. Width scaling is linear; speed scaling is limited by drainage and drying capacity.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| High shive content in screened pulp | Chips over-thick or under-cooked; H-factor too low for wood species | Tighten chip screening: reject chips >8 mm thickness; increase cook time or temperature to raise H-factor by 10-20%; check chip moisture (target 40-55%) for uniform impregnation |
| Low pulp viscosity (fiber degradation) | Cooking temperature above 180°C; prolonged cook time; high alkali charge | Reduce maximum temperature to ≤178°C; verify H-factor target is appropriate for species; reduce active alkali charge to 18-20% on wood |
| Low paper strength (tensile, tear) | Under-refined stock; low fiber bonding; excessive filler content | Increase refiner energy to 30-50 kWh/t (develop fibrillation); reduce filler (clay, CaCO₃) loading to <15%; check freeness (CSF target 300-500 mL for most papers) |
| Recovery boiler smelt-water explosion | Water leak into furnace (boiler tube failure); improper emergency shutdown sequence | Interlock all water sources to furnace; install smelt-shutoff system; if water leak suspected, NEVER apply water — use dry sand or emergency shutdown procedure; inspect boiler tubes monthly for thinning |
| Black liquor viscosity too high for pumping | Liquor solids >80% or temperature below 110°C; high lignin molecular weight | Maintain liquor temperature at 110-120°C; control evaporator discharge solids at 65-72% (higher with specialist additives); if viscosity spikes, dilute with weak black liquor |
| TRS (total reduced sulfur) odor emissions | Malfunctioning black liquor oxidation system; recovery boiler operating below 850°C (incomplete combustion of sulfides) | Ensure recovery boiler operating temperature is 850-1100°C; verify direct contact evaporator or oxidation tower is converting Na₂S to stable thiosulfate; maintain indirect contact evaporator seal integrity |
| Sulfite cook pitch deposits | Resin acids and fatty acids from resinous softwoods (pine, Douglas fir) coagulating in the digester | Use only low-resin wood species for sulfite (spruce, fir, hemlock); add pitch dispersant (tall oil) to cook; switch to Kraft process for resinous species |
| Paper web breaks at press section | Wet web too weak; sheet too wet entering press; felt condition poor | Increase refining energy to improve wet web strength; verify press roll pressure is uniform (check crown); inspect and condition press felt (clean with felt shower); reduce machine speed 10-20% until runnability stabilizes |
| Unequal basis weight across machine width | Headbox flow distribution uneven; slice lip adjustment incorrect | Verify headbox manifold pressure is uniform; adjust slice lip micro-settings (100-500 μm adjustments per zone); check approach system for stock flocculation or air entrainment |

## Safety

- **Recovery boiler smelt-water explosion**: Molten smelt (Na₂CO₃/Na₂S) at 850°C contacting liquid water is violently explosive — the most catastrophic hazard in a Kraft mill. Boiler tube leaks must be detected immediately. Interlocks automatically shut down smelt flow and divert water on detection. NEVER use water to fight recovery boiler fires. Dry sand or steam smothering only.
- **Hydrogen sulfide (H₂S) and TRS gases**: Evolved from black liquor at low pH or high temperature. H₂S IDLH: 100 ppm. Rotting black liquor in drains or spill areas releases H₂S. Vent all collection points to the recovery boiler or a thermal oxidizer. H₂S gas detectors mandatory in basement and drain areas.
- **Sulfur dioxide (SO₂) exposure (sulfite process)**: IDLH 100 ppm. Vent digester and blow system to absorption tower or scrubber. SO₂ is a severe respiratory irritant causing pulmonary edema at high concentrations.
- **Chlorine dioxide (ClO₂) for bleaching**: Explosive gas at concentrations >10% in air. Generated on-site (cannot be transported). Decomposes explosively on contact with organics or mercury. Maintain ClO₂ concentration below 10% in generator and piping. PPE: respiratory protection, face shield.
- **Steam and pressure hazards**: Digesters at 1.0 MPa and recovery boilers at 4-8 MPa steam present severe scald and explosion risks. All pressure vessels require regular inspection (ultrasonic thickness, radiographic weld examination). Pressure relief devices must be tested annually.
- **Rotating equipment**: Paper machine drives at 600-1,800 m/min present entanglement hazard. Guard all nip points (press rolls, calender nips, reel spool). Lockout/tagout mandatory for machine maintenance.

### PPE

- Hard hat, safety glasses, and steel-toed boots in all mill areas
- Chemical splash goggles and face shield when handling white/black liquor or bleaching chemicals
- Heat-resistant gloves for digester and recovery boiler work
- H₂S personal monitor (clip-on, audible alarm at 10 ppm) in basement and drain areas

## Quality Control

### Acceptance Criteria

| Parameter | Unbleached Kraft (Linerboard) | Bleached Kraft (Printing) | Sulfite (Specialty) |
|-----------|-------------------------------|---------------------------|---------------------|
| Kappa number | 25-40 | <5 (after bleaching) | <5 (after bleaching) |
| Brightness (ISO) | — | 88-92% | 85-90% |
| Tensile index (Nm/g) | 60-90 | 50-70 | 40-60 |
| Tear index (mN·m²/g) | 8-14 | 6-10 | 5-9 |
| Viscosity (dm³/kg, cupriethylenediamine) | 700-1,200 | 600-1,000 | 500-900 |
| Dirt count (mm²/m²) | — | <5 | <10 |
| Moisture content (finished paper) | 4-7% | 4-6% | 4-6% |

### Testing Methods

- **Kappa number**: Treat 1 g dry pulp with 25 mL 0.1 N KMnO₄ in 0.1 N H₂SO₄ at 25°C for 10 minutes. Back-titrate excess permanganate with sodium thiosulfate. Kappa ≈ permanganate consumed × 10. Measures residual lignin.
- **Canadian Standard Freeness (CSF)**: Drain 1 L of 0.3% pulp suspension through a standard screen. CSF (mL) measures drainage rate — lower CSF = more refining = more bonding = stronger but denser paper. Target: 200-700 mL depending on paper grade.
- **Tensile testing**: Cut standard strips (15 mm wide, 100 mm span), condition at 23°C/50% RH for 24 hours, test on a tensile tester at 100 mm/min crosshead speed. Report breaking length or tensile index.
- **Burst strength (Mullen)**: Apply hydraulic pressure to a clamped sheet area until rupture. Reported as kPa. Measures combined tensile and tear resistance.

### Sampling Protocol

- Digester: sample at blow to a 500 mL jar; test for Kappa number and viscosity. Every batch.
- Bleach plant: sample after each bleaching stage (D₀, E, D₁). Test brightness and Kappa. Every 2 hours.
- Paper machine: sample from reel every 30-60 minutes. Test basis weight, moisture, tensile, and burst. Adjust machine setpoints based on results.

## Variations and Alternatives

| Process | Yield | Pulp Quality | Chemical Recovery | Wood Species | When to Use |
|---------|-------|-------------|-------------------|-------------|-------------|
| Kraft (sulfate) | 45-50% | Strongest, dark color | >95% (excellent) | Any species | Default choice; strongest fiber; most species |
| Sulfite (acid) | 50-55% | Brighter, softer | 70-85% (moderate) | Low-resin softwoods only | Specialty papers; dissolving pulp (rayon, cellophane) |
| Soda (NaOH only) | 45-50% | Weaker than Kraft | 80-90% | Hardwoods, straws, agricultural residues | Pre-Kraft process; agricultural fiber pulping |
| Organosolv (organic solvents) | 50-60% | Good, bright | Solvent distillation | Any species | Small-scale, low-capital mills; non-wood fiber |
| Mechanical (groundwood) | 90-95% | Weak, short fiber, yellows | N/A (no chemicals) | Softwoods | Newsprint, catalog paper; when cost matters more than strength |
| Chemi-thermomechanical (CTMP) | 85-92% | Stronger than groundwood | Minimal chemicals | Softwoods | Magazine paper, tissue, board |

### Regional and Material Adaptations

- **Agricultural residues** (bagasse, straw, bamboo): Soda pulping with NaOH at 160-170°C. Yields 40-45% pulp suitable for corrugating medium and board. Common in regions with limited forest resources (India, China). Silica in straw causes scaling in recovery boilers — limits chemical recovery.
- **Recycled fiber**: Deinking plants process old newspapers and office waste. Repulping at 4-6% consistency with NaOH (pH 9-10) and surfactants. Fiber loses ~15-25% strength per recycle cycle. Critical for regions with limited wood supply.
- **Non-wood fibers** (cotton linters, hemp, flax, kenaf): High cellulose, low lignin content. Used for specialty papers (banknotes, filter paper, cigarette paper, Bible paper). Cotton linter pulp is the benchmark for archival quality.

## References

- [Acid production](acids.md) — sulfurous acid and SO₂ for sulfite cooking liquor
- [Alkali production](alkalis.md) — white liquor (NaOH + Na₂S) and causticizing chemistry for Kraft
- [Acids & Bases](acids-bases.md) — overview of acid-base materials in pulping
- [Sawmilling](../foundations/sawmilling.md) — wood chip furnish preparation
- [Chlor-Alkali Process](chlor-alkali.md) — chlorine dioxide and bleaching chemicals
- [Soap](soap.md) — tall oil and rosin byproducts from Kraft pulping
- [Reactor vessels](reactor-vessel.md) — digester design and pressure ratings

---
*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
