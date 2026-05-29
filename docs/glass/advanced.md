# Advanced Glass Production

> **Node ID**: glass.advanced
> **Domain**: [Glass](./index.md)
> **Dependencies**: [`glass.basic`](basic.md)
> **Enables**: [`glass.advanced.glassblowing`](advanced-glassblowing.md), [`glass.fibers`](fibers.md), [`glass.photomask-substrates`](photomask-substrates.md), [`silicon.crystal-growth`](../silicon/crystal-growth.md)
> **Timeline**: Years 25-40
> **Outputs**: borosilicate_glass, fused_silica, quartz_crucibles, glass_tubing, glass_apparatus
> **Critical**: Yes — borosilicate enables laboratory glassware for all chemistry; fused silica crucibles are consumables for CZ crystal growth (semiconductor-grade silicon).


Advanced glass production extends basic glassmaking ([basic glass](basic.md)) into specialty compositions and precision forming methods required for scientific apparatus, optical components, and semiconductor manufacturing. Three product families define this capability:

- **Borosilicate glass** (Pyrex-type): thermal-shock-resistant laboratory ware and chemical apparatus.
- **Fused silica / quartz glass**: ultra-low expansion, high-purity glass for CZ crystal growth crucibles, UV optics, and high-temperature windows.
- **Optical glass**: precisely controlled refractive index and dispersion for lenses, prisms, and mirrors.

Downstream, [silicon crystal growth](../silicon/crystal-growth.md) consumes quartz crucibles as a consumable. [Glass fibers](fibers.md) draw from the same melting expertise. [Photomask substrates](photomask-substrates.md) require ultra-flat, high-purity fused silica blanks.

## Prerequisites

**Materials**:
- [Basic glass](basic.md) production capability (soda-lime glass melting, annealing)
- [Silica sand](../mining/processing.md) (>99% SiO₂ for fused silica; >98% for borosilicate)
- Borax (Na₂B₄O₇·10H₂O) or boric acid (H₃BO₃) from dry lake deposits
- [Alumina](../chemistry/acids-bases.md) (Al₂O₃, 2-7% of borosilicate batch)
- [Sodium carbonate](../chemistry/solvay.md) (Na₂CO₃, soda ash)

**Tools and equipment**:
- [Electric furnace](../energy/electric-furnaces.md) capable of 1700-2000°C (fused silica)
- Gas or oil-fired furnace with forced air, 1500-1600°C (borosilicate)
- Hydrogen-oxygen torch system (~2800°C flame) for fused silica working
- Platinum-lined tank or crucible (optical glass)

**Infrastructure**:
- [Electrical power](../energy/electricity.md) for electric furnaces (50-200 kW for small-scale)
- Ventilation for glass batch mixing and furnace operation
- Compressed gas supply (O₂, H₂) for oxy-hydrogen torches

## Bill of Materials

| Material | Quantity per 100 kg batch | Source | Alternatives |
|----------|---------------------------|--------|-------------|
| Silica sand (SiO₂ >99%) | 70-80 kg | [Mining](../mining/processing.md) — vein quartz or quartzite | Lower-purity sand (increases bubble count) |
| Borax or boric acid (B₂O₃ source) | 15-25 kg | Dry lake deposits (Turkey, California, Tibet) | Colemanite mineral (Ca₂B₆O₁₁·5H₂O) |
| Soda ash (Na₂CO₃) | 5-10 kg | [Solvay process](../chemistry/solvay.md) | Natural trona ore |
| Alumina (Al₂O₃) | 3-8 kg | [Bauxite processing](../chemistry/alkalis.md) | Feldspar mineral (KAlSi₃O₈) |
| Electrical energy | 100-400 kWh | [Power generation](../energy/electricity.md) — baseload required | Gas-fired furnace (lower temperature ceiling) |
| Hydrogen gas (H₂) | 10-50 L/hour for torch work | [Electrolysis](../chemistry/electrolysis.md) | No alternative for fused silica working |
| Oxygen gas (O₂) | 5-25 L/hour for torch work | [Air separation](../chemistry/air-separation.md) | Compressed air (insufficient for fused silica) |


## Borosilicate Glass

**Principle**: Adding B₂O₃ (7-13%) to a soda-lime glass base reduces the thermal expansion coefficient from ~9×10⁻⁶/°C to ~3×10⁻⁶/°C, making the glass 3× more resistant to thermal shock. The alumina content (2-7%) improves chemical durability.

**Prerequisites**:
- [Basic glass](basic.md) melting furnace (gas or oil-fired, 1500-1600°C)
- Borax or boric acid supply
- Covered clay or platinum crucible

**Materials**:
- Silica sand (SiO₂), 70-80% by weight, >98% purity
- Borax (Na₂B₄O₇·10H₂O) or boric acid (H₃BO₃), 7-13% B₂O₃ equivalent
- Sodium carbonate (Na₂CO₃), 4-8% Na₂O equivalent
- Alumina (Al₂O₃), 2-7% by weight

**Construction steps**:
1. Weigh batch components to ±0.5% accuracy. Typical batch: 75 kg SiO₂, 15 kg borax, 7 kg soda ash, 3 kg alumina per 100 kg glass.
2. Dry-mix all components in a ceramic or steel container until uniform color (10-15 minutes of hand mixing).
3. Load batch into covered clay or platinum crucible. Cover reduces volatilization of B₂O₃ (boron losses of 5-15% occur at melt temperature).
4. Place crucible in furnace. Heat to 1500-1600°C at 200-300°C/hour. Hold at peak temperature for 12-24 hours.
5. Stir the melt with a fired clay rod every 2-3 hours to homogenize. B₂O₃ tends to stratify — inadequate stirring produces compositional layering.
6. After homogenization, reduce temperature to working range 800-1100°C. Form by blowing, pressing, or casting.
7. Anneal at 560°C for 30-60 minutes (1 hour per 25 mm wall thickness). Cool at 1-2°C/minute to below 510°C (strain point). Below strain point, cool at 5-10°C/minute to room temperature.

**Calibration**: Test thermal shock resistance by heating a 3 mm thick sample to 200°C and quenching in 20°C water. Borosilicate survives ≥5 cycles without cracking. Soda-lime glass fails on the first cycle.

**Expected performance**:
- Thermal expansion coefficient: 3.0-3.3 × 10⁻⁶/°C (measured by dilatometer, 20-300°C range)
- Maximum service temperature: 500°C (continuous), 600°C (short-term)
- Chemical resistance: resists all acids except HF and hot H₃PO₄; moderate alkali resistance above 100°C

**Strengths**:
- Thermal shock resistance 3× better than soda-lime — survives rapid temperature changes that shatter ordinary glass
- Chemical durability suitable for laboratory ware — resists most acids, bases at moderate temperature
- Workable with standard glassblowing torches (gas-oxygen, ~2000°C)

**Weaknesses**:
- Higher melting temperature (1500-1600°C) than soda-lime (1000-1200°C) — requires gas/oil-fired or electric furnace
- Stiffer working consistency than soda-lime — requires more force for blowing and shaping
- B₂O₃ volatilization during melt causes compositional drift if not monitored

## Fused Silica / Quartz Glass

**Principle**: Pure SiO₂ (>99.5%) melted at 1700-2000°C produces a glass with near-zero thermal expansion (0.5 × 10⁻⁶/°C) and transmission from UV (180 nm) through visible to IR (3.5 μm). No flux is used — the silica softens gradually rather than melting sharply.

**Prerequisites**:
- [Electric furnace](../energy/electric-furnaces.md) capable of 1700-2000°C
- High-purity quartz crystal (>99.5% SiO₂) from pegmatite veins or high-grade quartzite
- Hydrogen-oxygen torch (~2800°C flame)
- [Oxygen supply](../chemistry/air-separation.md) and [hydrogen supply](../chemistry/electrolysis.md)

**Materials**:
- Quartz crystal or high-purity quartzite, >99.5% SiO₂ (for Type I fused quartz)
- Quartz powder, 100-300 μm particle size (for Type II flame-fused silica)
- SiCl₄ and H₂/O₂ (for synthetic fused silica — requires [silicon chemistry](../silicon/purification.md))
- Graphite tools for shaping (won't stick to silica)

**Construction steps — Type I (electric furnace fused quartz)**:
1. Crush quartz crystal to 5-20 mm pieces. Wash in dilute HCl (10%) to remove surface iron contamination, rinse with deionized water, dry at 110°C.
2. Load quartz pieces into graphite or tungsten crucible inside the electric furnace. Evacuate furnace chamber to <1 Pa (vacuum degassing prevents bubble formation).
3. Heat to 1700-2000°C at 100-200°C/hour. Hold at peak temperature for 8-24 hours. Bubbles rise and dissolve under vacuum.
4. Cool to working range 1800-2100°C (fused silica is very viscous even at working temperature).
5. Shape using graphite tools (rods, paddles). Do NOT use metal tools — they contaminate the silica.
6. Anneal at 1100-1200°C for 1-2 hours. Cool at 5-10°C/minute. Fused silica has very low thermal expansion, so annealing is less critical than for other glasses.

**Construction steps — Type II (flame-fused silica)**:
1. Grind quartz crystal to powder, 100-300 μm particle size. Wash and dry as above.
2. Feed quartz powder into hydrogen-oxygen flame (~2000°C) using a vibratory feeder or screw auger. Powder rate: 0.5-2 kg/hour.
3. Particles fuse and deposit as a clear boule on a rotating graphite mandrel. Mandrel speed: 5-15 RPM. Boule builds up over 4-24 hours.
4. Flame volatilizes some impurities (Na, K), improving purity relative to Type I.

**Construction steps — Synthetic fused silica (highest purity, 99.9999%+)**:
1. Vaporize SiCl₄ in a carrier gas stream. Feed into H₂/O₂ flame.
2. SiCl₄ + 2H₂O → SiO₂ + 4HCl. SiO₂ deposits as amorphous soot on a rotating target.
3. Consolidate the soot preform at 1500°C in a furnace. Shrinkage ~30%.
4. Requires [chlorosilane chemistry](../silicon/purification.md) from the Silicon stage.

**Calibration**: Measure thermal expansion by heating a 100 mm rod from 20°C to 300°C and measuring length change with a dial gauge (0.01 mm resolution). Expected: ΔL = 0.014 mm (0.5 × 10⁻⁶/°C × 100 mm × 280°C). If ΔL > 0.04 mm, the glass contains impurities or is partially crystallized.

**Expected performance**:
- Thermal expansion: 0.5 × 10⁻⁶/°C (20-300°C)
- Softening point: ~1600°C. Working range: 1800-2100°C
- UV transmission: 180 nm cutoff (vs. 300 nm for borosilicate)
- Service temperature: 1000°C continuous (short-term to 1200°C)
- Purity: 99.5% SiO₂ (Type I), 99.9% (Type II), 99.9999% (synthetic)

**Strengths**:
- Virtually immune to thermal shock — can be heated red-hot and quenched in water without cracking
- Highest chemical purity of any glass — critical for semiconductor crucibles where impurities dope the silicon melt
- UV-transparent — essential for photolithography optics and UV spectroscopy

**Weaknesses**:
- Extremely high working temperature (1800-2100°C) — requires hydrogen-oxygen torch and electric furnace, no gas-air alternative
- Very viscous even at working temperature — slow forming, requires patience and graphite tooling
- Quartz crucibles are consumable in CZ growth — they dissolve slowly in molten silicon, limiting crystal pull duration to 24-72 hours per crucible

## Optical Glass Production

**Principle**: Optical glass requires exceptional homogeneity (no striae, bubbles, or compositional variation) and precisely controlled refractive index. Raw materials must be batched to ±0.01% accuracy (vs. ±2% for container glass) and the melt must be stirred continuously to eliminate compositional layering.

**Prerequisites**:
- [Platinum-lined tank furnace](../metals/precious-metals.md) (platinum introduces no contamination, unlike clay crucibles)
- Precision weighing equipment (±0.01% accuracy)
- [Silicon carbide](../metals/non-ferrous.md) or cerium oxide polishing supplies

**Materials**:
- Raw materials batched to ±0.01%: SiO₂, PbO (for flint glass), B₂O₃, Na₂O, K₂O, BaO, La₂O₃
- Antimony trioxide (Sb₂O₃), 0.1-0.3% as fining agent
- Platinum stirrer paddle

**Construction steps**:
1. Weigh each raw material to ±0.01% accuracy using an analytical balance. A 0.1% weighing error shifts the refractive index outside specification.
2. Mix batch in a platinum-lined tank furnace (100-500 L capacity for optical grades).
3. Melt at 1400-1500°C. Begin mechanical stirring with platinum paddle at 5-20 RPM immediately.
4. Stir continuously for 8-24 hours. Stirring eliminates striae (compositional layers that refract light unevenly).
5. Add fining agent (Sb₂O₃ at 0.1-0.3%). Hold at 1500-1600°C for 4-6 hours to allow bubbles to rise and dissolve.
6. Cast into molds or press into blanks.
7. Anneal for optical glass: hold at annealing point for days to weeks. Cool at 0.1-1°C/hour through the strain point. A 100 mm lens blank requires 2-4 weeks of annealing.

**Calibration**: Measure refractive index with an Abbe refractometer (accuracy ±0.0001). Test for striae by projecting a point light source through the glass blank onto a screen — striae appear as bright or dark streaks.

**Expected performance**:
- Refractive index tolerance: ±0.001 for standard optical glass, ±0.0001 for precision grades
- Bubble specification: zero bubbles >50 μm in diameter per 100 cm³
- Striae: none visible under 10× magnification with collimated light

**Strengths**:
- Precisely controlled optical properties enable lens systems for microscopes, telescopes, and cameras
- Platinum crucibles introduce no contamination — consistent glass composition batch to batch
- Continuous stirring produces homogeneity impossible in hand-stirred melts

**Weaknesses**:
- Platinum is extremely expensive and rare — platinum-lined furnaces represent a major capital investment
- Annealing times of weeks to months per batch create long production lead times
- Weighing accuracy of ±0.01% requires analytical balances not available at earlier bootstrap stages

## Quartz Crucible Manufacturing

**Principle**: High-purity quartz crucibles (>99.99% SiO₂) are formed by slip casting or isostatic pressing quartz powder, then sintering at 1700-1800°C under vacuum or inert atmosphere. Impurities (especially Al, Fe, Na) must remain below ppm levels — they dissolve into molten silicon during CZ growth and dope the crystal uncontrollably.

**Prerequisites**:
- Refined quartz powder (>99.99% SiO₂, <50 μm particle size)
- [Electric furnace](../energy/electric-furnaces.md) capable of 1800°C under vacuum
- Porous plaster molds (for slip casting) or rubber bags + hydraulic press (for isostatic pressing)

**Materials**:
- Quartz powder, SiO₂ >99.99%, particle size 1-50 μm
- Deionized water + deflocculant (sodium silicate, 0.1-0.3% by weight) for slip
- Plaster of Paris for molds
- High-purity argon gas or vacuum pump for sintering atmosphere

**Construction steps — Slip casting**:
1. Prepare quartz slurry: mix quartz powder with deionized water and 0.1-0.3% sodium silicate deflocculant. Specific gravity: 1.8-2.0 g/mL. Stir for 30 minutes.
2. Pour slurry into porous plaster mold shaped as crucible interior. Water absorbed by plaster leaves dense powder shell.
3. Demold after 1-4 hours (wall thickness builds at ~1 mm/hour). Air dry 24-48 hours.
4. Load dried green body into electric furnace. Evacuate to <10 Pa.
5. Heat to 1700-1800°C at 100°C/hour. Hold 2-8 hours. Shrinkage 15-20%.
6. Cool at 50-100°C/hour under vacuum or argon to below 500°C, then air-cool.

**Construction steps — Isostatic pressing**:
1. Fill quartz powder into rubber bag shaped as crucible exterior. Seal bag.
2. Apply hydraulic pressure 100-200 MPa uniformly in an oil-filled pressure vessel. Hold 1-5 minutes.
3. Remove pressed green body from rubber bag. Dimensions are closer to final (shrinkage ~10-15% vs. 15-20% for slip casting).
4. Sinter as in steps 4-6 above.

**Calibration**: Illuminate crucible wall with bright light. Bubbles appear as bright spots. For semiconductor-grade: reject any crucible with bubbles >50 μm in inner wall. Measure inside diameter with calipers: ±1 mm for 300 mm crucible. Ovality <1 mm. Wall thickness variation <0.5 mm.

**Expected performance**:
- Wall thickness: 5-10 mm (thicker walls last longer in CZ pull but reduce thermal responsiveness)
- Diameter: 200-450 mm for semiconductor use
- Purity: Al <10 ppm, Fe <1 ppm, Na <0.5 ppm (semiconductor grade)
- Service life: 24-72 hours in molten silicon before wall thinning requires replacement

**Strengths**:
- Slip casting requires only plaster molds and simple mixing — low equipment cost
- Isostatic pressing produces denser, more uniform green body than slip casting
- Transparency of finished crucible directly indicates purity — visual QC is straightforward

**Weaknesses**:
- Quartz crucibles are consumable in CZ crystal growth — they dissolve slowly in molten silicon
- Surface contamination from handling transfers to silicon melt — requires clean gloves and clean-room handling
- Shrinkage during sintering (15-20%) makes dimensional control difficult — molds must be oversized accordingly

## Glass Tubing Production (Danner Process)

**Principle**: Molten glass flows from the furnace forehearth onto a rotating, inclined refractory mandrel. Air blown through the hollow mandrel inflates the glass ribbon into a continuous tube, drawn off by tractor belts.

**Prerequisites**:
- [Glass melting furnace](basic.md) with forehearth
- Refractory mandrel (hollow ceramic cylinder)
- Tractor belts or roller drawing mechanism

**Materials**:
- Borosilicate or soda-lime glass melt, homogeneous, at working temperature
- Compressed air supply (0.01-0.1 MPa through mandrel bore)

**Construction steps**:
1. Set mandrel inclination to ~15° from horizontal. Start mandrel rotation at 5-20 RPM.
2. Allow molten glass to flow from forehearth onto the rotating mandrel. Glass wraps around mandrel forming a ribbon.
3. Begin air flow through hollow mandrel center at 0.01-0.05 MPa. Air pressure inflates the glass ribbon into a tube.
4. Start tractor belt drawing at 1-20 m/min. Draw speed controls wall thickness — faster draw produces thinner walls.
5. Adjust air pressure to control inner diameter. Mandrel diameter sets minimum bore.
6. Tube cools during 10+ meters of travel. Cut to length by scoring and snapping.
7. Pass tube through annealing lehr at appropriate temperature before packaging.

**Calibration**: Measure tubing OD with calipers at 1 m intervals along a 10 m sample. Target: ±0.1 mm wall thickness with good process control. Bore diameter measured by inserting precision pin gauges.

**Expected performance**:
- Tubing OD range: 3-50 mm continuous production
- Wall thickness tolerance: ±0.1 mm with good process control
- Production speed: 1-20 m/min depending on diameter
- Length: continuous, cut to order

**Strengths**:
- Continuous production — no batch cycle, tube produced as long as furnace is fed
- Good dimensional control (±0.1 mm wall thickness) achievable with steady-state operation
- Produces standard tubing sizes for scientific glassware directly

**Weaknesses**:
- Requires a dedicated forehearth and drawing mechanism — not a hand process
- Wall thickness varies with any change in melt temperature, air pressure, or draw speed — steady-state operation is essential
- Refractory mandrel wears over time and must be replaced periodically (100-500 hours depending on glass type)

## Glass Fiber Production

**Principle**: Molten glass is forced through small holes (0.5-2 mm) in a platinum bushing or spinning disk. The emerging strands are attenuated by centrifugal force or high-speed winding, reducing diameter to 5-24 μm. Surface flaw elimination during drawing gives fiber tensile strengths far exceeding bulk glass.

**Prerequisites**:
- [Glass melting furnace](basic.md) with precise temperature control (±5°C)
- Platinum bushing (200-4000 holes) or spinner disk (0.5-1 mm holes)
- High-speed winder (1000-3000 m/min)

**Materials**:
- E-glass composition batch (54% SiO₂, 14% Al₂O₃, 22% CaO, 10% B₂O₃)
- Phenolic resin binder (5-10% by weight for insulation wool)
- Sizing compound (polymer + coupling agent for structural fiber)

**Construction steps — Glass wool (insulation)**:
1. Melt E-glass or soda-lime batch to 1300-1400°C.
2. Feed melt to spinner disk (0.5-1 mm holes, 2000-4000 RPM).
3. Centrifugal force extrudes glass into fibers 5-15 μm diameter, 5-15 cm long.
4. Spray phenolic resin binder (5-10% by weight) onto fibers.
5. Collect fibrous mat on conveyor belt. Cure at 200°C for 10-30 minutes. Cut to size.

**Construction steps — Continuous fiber (structural)**:
1. Melt E-glass batch to 1350-1450°C in platinum-lined tank.
2. Feed melt through platinum bushing (200-4000 holes, 0.8-2.0 mm diameter) under gravity.
3. Draw emerging strands with high-speed winder at 1000-3000 m/min, reducing diameter to 5-24 μm.
4. Apply sizing immediately to protect fiber surface and improve resin bonding.
5. Wind onto spools for storage and transport.

**Calibration**: Measure fiber diameter with optical microscope at 100-200× magnification. Target: 5-24 μm ±10%. Test tensile strength of single fibers: 3000-3800 MPa for E-glass (ASTM D3379).

**Expected performance**:
- Fiber diameter: 5-24 μm (structural), 5-15 μm (insulation)
- Tensile strength (single fiber): 3000-3800 MPa (E-glass)
- Insulation thermal conductivity: 0.03-0.04 W/(m·K)
- Insulation density: 10-50 kg/m³

**Strengths**:
- Drawn fibers are flaw-free on the surface — tensile strength 50× higher than bulk glass
- Glass wool provides excellent thermal insulation (0.03-0.04 W/(m·K)) at low density
- Continuous fiber production enables fiberglass-reinforced composites for structural applications

**Weaknesses**:
- Platinum bushing is a major capital cost and rare material
- Fiber diameter sensitive to melt temperature (±5°C causes measurable diameter change)
- Sizing chemistry adds complexity — bare glass fibers abrade each other and lose strength rapidly


## Glass Composition Comparison

| Parameter | Soda-lime | Borosilicate | Fused silica | Optical crown | Optical flint |
|-----------|-----------|-------------|-------------|---------------|---------------|
| SiO₂ (%) | 70-74 | 70-80 | 100 | 70-75 | 45-55 |
| Thermal expansion (×10⁻⁶/°C) | 8.5-9.5 | 3.0-3.3 | 0.5 | 7-9 | 8-10 |
| Softening point (°C) | 700-730 | 820 | 1600 | 650-720 | 600-680 |
| Annealing point (°C) | 510 | 560 | 1100-1200 | 480-530 | 430-480 |
| Working range (°C) | 700-1000 | 800-1100 | 1800-2100 | 700-1000 | 650-900 |
| Refractive index | 1.51 | 1.47 | 1.46 | 1.50-1.54 | 1.58-1.72 |

## Glass Fiber Properties

| Property | Glass wool | Continuous E-glass fiber |
|----------|-----------|------------------------|
| Fiber diameter (μm) | 5-15 | 5-24 |
| Tensile strength (MPa) | N/A (non-structural) | 3000-3800 |
| Thermal conductivity (W/(m·K)) | 0.03-0.04 | N/A |
| Density (kg/m³) | 10-50 | 2500-2600 (solid glass) |
| Production rate | 1-5 tonnes/hour | 1-10 kg/hour per bushing hole |

## Scaling Notes

- **Borosilicate**: 10-100 kg batches in clay crucibles are the minimum scale. Scaling to continuous tank furnaces (1-10 tonnes/day) reduces per-unit energy by 30-50%.
- **Fused silica**: Type I production starts at 5-20 kg batches. Synthetic fused silica (from SiCl₄) requires chemical plant infrastructure and is only economical above 1 tonne/year.
- **Optical glass**: Minimum viable scale is a 100 L platinum-lined tank. Below this, per-unit platinum cost is prohibitive.
- **Quartz crucibles**: Slip casting 1-5 crucibles per batch is feasible for bootstrap. Isostatic pressing requires a hydraulic press (100-200 MPa capacity).
- **Glass tubing**: Danner process requires minimum 50-100 kg/hour throughput to maintain steady-state. Below this, batch drawing methods are used.
- **Glass fiber**: Insulation wool production starts at ~100 kg/hour. Continuous fiber requires a platinum bushing and steady melt supply.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Bubbles in borosilicate melt | Insufficient hold time at peak temperature or inadequate stirring | Extend hold time to 18-24 hours. Stir every 2 hours with clay rod. |
| B₂O₃ loss (compositional drift) | Uncovered crucible, excessive hold time at peak temperature | Use covered crucible. Reduce hold time. Monitor by measuring CTE on test sample. |
| Fused silica devitrification (cristobalite crystals) | Held too long above 1470°C during sintering or working | Limit time above 1470°C. Cool through 1470°C range quickly. Check with X-ray diffraction. |
| Quartz crucible cracks during sintering | Too-rapid heating or cooling, or uneven powder density in green body | Heat at ≤100°C/hour. Ensure uniform green body density. Check for air pockets in slip-cast body. |
| Striae in optical glass | Inadequate stirring or temperature gradients in melt | Increase stirrer RPM. Extend stirring time. Check furnace for hot spots. |
| Fiber diameter variation | Melt temperature fluctuation or winder speed instability | Control melt temperature to ±3°C. Check winder motor drive for speed regulation. |
| Glass tubing ovality | Uneven cooling or air pressure fluctuation in Danner process | Check mandrel alignment. Install air pressure regulator. Ensure uniform furnace temperature across ribbon width. |

## Safety

- **Extreme-temperature glassworking**: Borosilicate melts at 1500-1600°C; fused silica requires 1700-2100°C working temperatures. Hydrogen-oxygen torches produce flame temperatures of ~2800°C. Severe burns occur on brief skin contact with hot glass or flame. Wear Kevlar or leather heat-resistant gloves, arm guards, face shield, and closed-toe boots. Use welding-grade shaded lenses (#5-#7 for fused silica oxy-hydrogen work) — intense visible and infrared radiation from molten silica causes retinal damage.
- **Chlorosilane hazards in synthetic fused silica**: SiCl₄ is corrosive, reacts violently with moisture to produce HCl fumes, and causes severe respiratory damage at concentrations >5 ppm (OSHA PEL). Handle only in closed, well-ventilated systems with acid-resistant equipment. Emergency: flood exposed skin with water for 15+ minutes; move to fresh air if inhaled.
- **Hydrogen gas explosion risk**: Hydrogen forms explosive mixtures with air at 4-75% concentration (LEL 4%). Ignites with very low energy (0.017 mJ). Leak-test all connections with soap solution before each use. Flashback arrestors mandatory on both gas lines. Store cylinders away from heat and ignition sources. Never use hydrogen in unventilated spaces.
- **Lead and heavy metal toxicity**: Lead oxide (PbO) used in flint glass and glazes is toxic by inhalation (dust) and ingestion. Cumulative neurological, renal, and reproductive damage. Lead IDLH: 100 mg/m³ (NIOSH). Handle all batch powders containing lead, cobalt, or barium with gloves and N100 respirator. Weigh and mix in ventilated areas.
- **Glass dust (silica)**: Cutting, grinding, and drilling glass produces fine silica dust. Inhalation causes silicosis (lung scarring, irreversible). OSHA PEL for respirable silica: 50 μg/m³. Wet-grind when possible. Wear P100 respirator for dry grinding operations.

## Quality Control

**Borosilicate glass**:
- Thermal expansion test: dilatometer measurement, 20-300°C range. Accept: 3.0-3.3 × 10⁻⁶/°C.
- Thermal shock test: heat 3 mm sample to 200°C, quench in 20°C water. Accept: ≥5 cycles without crack.
- Visual inspection: no visible bubbles >0.5 mm, no seeds, no cord.

**Fused silica / quartz crucibles**:
- Bubble inspection: illuminate wall with bright light. Semiconductor grade: no bubbles >50 μm in inner wall.
- Dimensional tolerance: ID ±1 mm for 300 mm crucible. Ovality <1 mm. Wall thickness variation <0.5 mm.
- Purity: ICP-MS or GDMS analysis. Semiconductor: Al <10 ppm, Fe <1 ppm, Na <0.5 ppm. Solar grade: Al <20 ppm, Fe <5 ppm.
- Cristobalite check: X-ray diffraction. Reject if >5% cristobalite by volume.

**Optical glass**:
- Refractive index: Abbe refractometer. Standard: ±0.001. Precision: ±0.0001.
- Striae: collimated light test at 10×. Accept: no visible streaks.
- Bubble count: zero bubbles >50 μm per 100 cm³.
- Stress birefringence: crossed polarizer test. Accept: uniform dark field.

**Glass tubing**:
- OD measurement: calipers at 1 m intervals along 10 m sample. Accept: ±0.1 mm.
- Wall thickness: micrometer at 3 points per cross-section. Accept: ±0.1 mm.
- Straightness: roll on flat surface. Maximum bow: 2 mm per meter.


## Glass Ceramics (Vycor-Type)

Melt a borosilicate glass with specific composition (75% SiO₂, 20% B₂O₃, 5% Na₂O). Form into desired shape by conventional glass forming. Heat treat at 500-600°C to induce phase separation. Leach in hot acid (HCl or H₂SO₄) to dissolve the sodium-borate phase, leaving a porous silica skeleton (~70% of original volume, pore size 2-10 nm). Heat to 900-1000°C to consolidate. Result: 96% SiO₂ glass with CTE 0.75 × 10⁻⁶/°C. Can be formed at conventional glassworking temperatures (before leaching), unlike fused silica which requires 1800-2100°C.

**When to use**: Complex shapes in high-silica glass without oxy-hydrogen torch capability.

## Tempered Glass

Heat soda-lime glass to 620-650°C, then quench both surfaces with compressed air jets. Surfaces cool and contract first; interior contracts later, pulling surfaces into compression (~100 MPa). Net tensile strength: 150-250 MPa (vs. 30-90 MPa annealed). Cannot be cut, drilled, or ground after tempering. Used for safety glass (shatters into small cubes rather than sharp shards).

**When to use**: Safety glazing, tabletops, shower doors — any application requiring impact resistance and safe failure mode.

## Chemical Strengthening

Immerse thin glass (1-3 mm) in molten KNO₃ at 400-450°C for 4-16 hours. Large K⁺ ions (0.133 nm) replace smaller Na⁺ ions (0.095 nm) in the surface, creating compressive stress of 300-700 MPa. Surface layer depth: 20-50 μm. Unlike thermal tempering, the glass can be cut after treatment.

**When to use**: Thin glass (1-3 mm) that cannot be thermally tempered — smartphone screens, aircraft windshields.

## See Also

- [Basic Glass Production](basic.md) — soda-lime glass melting, the prerequisite for all advanced glass
- [Glassblowing & Scientific Apparatus](glassblowing.md) — lampworking and furnace glassblowing techniques using borosilicate
- [Silicon Crystal Growth](../silicon/crystal-growth.md) — CZ process that consumes quartz crucibles
- [Glass Fibers](fibers.md) — structural and insulation fiber production
- [Air Separation](../chemistry/air-separation.md) — oxygen and hydrogen supply for oxy-hydrogen torches
- [Electric Furnaces](../energy/electric-furnaces.md) — furnace requirements for fused silica and optical glass
- [Electrolysis](../chemistry/electrolysis.md) — hydrogen production for oxy-hydrogen torch systems



[← Back to Glass](index.md)
