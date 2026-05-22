# Specialty Alloys

> **Node ID**: metals.alloys
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`metals.steelmaking`](steelmaking.md), [`metals.non-ferrous`](non-ferrous.md), [`metals.iron-steel`](iron-steel.md)
> **Timeline**: Years 20-50
> **Outputs**: stainless steel, tool steel, superalloys, titanium alloys, specialty copper alloys

### Overview

Specialty alloys are engineered metallic systems where precise additions of alloying elements transform base metals into materials with exceptional corrosion resistance, high-temperature strength, wear resistance, or specific physical properties. Unlike plain carbon steels and basic bronzes (covered in [Iron & Steel](iron-steel.md) and [Copper & Bronze](copper-bronze.md)), specialty alloys require controlled-atmosphere melting, precise compositional analysis, and multi-step heat treatments. They represent the frontier of metallurgical capability — the materials that enable chemical processing equipment, gas turbines, medical implants, and precision tooling.

Alloy development depends on understanding phase diagrams, solid-state phase transformations, and the interplay between composition, processing, and microstructure. The key strengthening mechanisms — solid solution, precipitation, dispersion, and grain-boundary hardening — are combined to produce properties far beyond what any pure metal can achieve.

### Stainless Steels

Stainless steels are iron alloys containing ≥10.5% chromium, which forms a self-healing passive Cr₂O₃ film (~1-3 nm thick) on the surface. This invisible oxide layer provides corrosion resistance in oxidizing environments. The chromium content is non-negotiable — below 10.5%, the passive film is discontinuous and corrosion resistance collapses.

**[Austenitic stainless steels](../glossary/austenitic-stainless-steels.md)** (200 and 300 series):
- **Structure**: Face-centered cubic (FCC, γ-iron), stabilized by nickel. Non-magnetic, non-hardenable by heat treatment, strengthened only by cold work.
- **[Type 304](../glossary/type-304.md)** (18Cr-8Ni, the workhorse): ~18% Cr, ~8% Ni, ≤0.08% C. Excellent corrosion resistance in atmospheric and mildly corrosive environments. Used for food processing, chemical vessels, architectural applications. Tensile strength: 515-620 MPa (annealed), up to 1,200+ MPa (cold-worked). Maximum service temperature: ~870°C (intermittent), ~925°C (continuous, oxidation limit).
- **[Type 316](../glossary/type-316.md)** (17Cr-12Ni-2.5Mo): Addition of 2-3% molybdenum significantly improves pitting and crevice corrosion resistance in chloride environments. The go-to grade for marine, chemical processing, and pharmaceutical equipment. Molybdenum stabilizes the passive film against localized breakdown by Cl⁻ ions.
- **[L-grades](../glossary/l-grades.md)** (304L, 316L): Low carbon variants (≤0.03% C). Carbon content is critical because chromium carbides (Cr₂₃C₆) precipitate at grain boundaries when the steel is heated in the 425-815°C range — a process called **sensitization**. Carbide precipitation depletes chromium from the grain boundary region below the 10.5% threshold, creating a narrow zone susceptible to intergranular corrosion (weld decay). Low carbon delays sensitization; alternatively, **[stabilized grades](../glossary/stabilized-grades.md)** (321 with Ti, 347 with Nb) form stable TiC or NbC carbides preferentially, leaving chromium in solution.
- **[Type 201](../glossary/type-201.md)** (low-nickel): Replaces half the nickel with manganese (~7% Mn, ~5% Ni, 17% Cr). Lower cost but reduced corrosion resistance. Manganese acts as a cheaper austenite stabilizer.

**[Ferritic stainless steels](../glossary/ferritic-stainless-steels.md)** (400 series, magnetic):
- **Structure**: Body-centered cubic (BCC, α-iron), little or no nickel. Chromium 10.5-30%. Lower cost than austenitic grades (no nickel). Good stress corrosion cracking resistance (unlike austenitic grades, which are susceptible in chloride + tensile stress environments).
- **[Type 430](../glossary/type-430.md)** (17% Cr): General-purpose ferritic grade. Used for automotive trim, dishwasher liners, decorative applications. Inferior ductility and toughness compared to austenitic grades — limited by the ductile-brittle transition that BCC metals exhibit.
- **[Type 446](../glossary/type-446.md)** (27% Cr): High-chromium grade for high-temperature oxidation resistance. Used in furnace parts, burner nozzles.

**[Martensitic stainless steels](../glossary/martensitic-stainless-steels.md)** (400 series, magnetic, hardenable):
- **Structure**: Body-centered tetragonal (BCT, distorted martensite) after quenching. Higher carbon (0.1-1.2% C) with moderate chromium (11.5-18%).
- **[Type 410](../glossary/type-410.md)** (12% Cr, 0.15% C): General-purpose hardenable stainless. Quench from 950-1000°C, temper at 200-700°C depending on desired hardness/toughness balance. Used for cutlery, valves, pump shafts.
- **[Type 440C](../glossary/type-440c.md)** (17% Cr, 1.1% C): Highest hardness of any stainless steel (HRC 58-60 after quench + low-temperature temper). Massive chromium carbide volume provides wear resistance. Used for bearings, surgical instruments, high-quality knife blades. Limited corrosion resistance compared to austenitic grades — the high carbon reduces available chromium.

**Duplex stainless steels**:
- **Structure**: Approximately equal fractions of austenite and ferrite in a laminar microstructure. Achieved by balancing Cr, Ni, Mo, and N. Typical composition: 22-25% Cr, 5-7% Ni, 3-4% Mo, 0.1-0.3% N.
- **[Type 2205](../glossary/type-2205.md)** (22Cr-5Ni-3Mo-0.15N): Roughly twice the yield strength of austenitic grades (450 MPa vs. 205 MPa annealed). Excellent stress corrosion cracking resistance and pitting resistance (PREN > 34). Used in offshore, chemical tankers, heat exchangers. Nitrogen acts as a potent austenite stabilizer and strengthens both phases.
- The two-phase structure limits grain growth and provides superior resistance to chloride stress corrosion cracking, which is the Achilles' heel of austenitic stainless in hot chloride service.

**Precipitation-hardening (PH) stainless steels**:
- **[Type 17-4PH](../glossary/type-17-4ph.md)** (17Cr-4Ni-4Cu-0.3Nb): Solution-treated at 1040°C (single-phase martensite), then aged at 480-620°C. Cu-rich precipitates form during aging, providing strengthening. HRC 28-44 depending on aging temperature. Used for aerospace structural components, nuclear reactor parts, medical devices. Combines the corrosion resistance of austenitic stainless with the strength of martensitic grades.

### Tool Steels

Tool steels are specially alloyed and heat-treated steels designed for cutting, forming, and shaping other materials. They must maintain hardness at elevated temperatures (red-hardness), resist abrasion, and withstand cyclic mechanical and thermal loading. The AISI classification uses a single-letter prefix:

**Cold-work tool steels**:
- **[O-series](../glossary/o-series.md)** (Oil-hardening, e.g., O1): 0.9% C, 1.0% Mn, 0.5% Cr, 0.5% W. Moderate alloy content, deep hardening in oil quench. Low distortion during quenching — important for precision tooling. Used for gauges, dies, cutting tools. Hardness: HRC 57-62.
- **[D-series](../glossary/d-series.md)** (High carbon/high chromium, e.g., D2): 1.5% C, 12% Cr, 1.0% Mo. Massive volume of chromium carbides (Cr₇C₃) provides exceptional wear resistance. Air-hardening — minimal distortion. Used for stamping dies, forming rolls, blanking dies, shear blades. Hardness: HRC 58-62. Limited toughness — not for impact applications.
- **[A-series](../glossary/a-series.md)** (Air-hardening, e.g., A2): 1.0% C, 5% Cr, 1.0% Mo. Intermediate between O and D series. Air quench from 940-975°C gives HRC 57-62 with minimal size change. Used for punches, trim dies, plastic molds.

**Hot-work tool steels**:
- **[H-series](../glossary/h-series.md)** (e.g., H13): 0.4% C, 5% Cr, 1.5% Mo, 1.0% V. Designed for tools in contact with hot workpieces (>500°C). Must resist softening, thermal fatigue (cyclic heating/cooling causes surface cracking — "heat checking"), and erosion by molten metal. H13 is the dominant grade for die-casting dies, forging dies, extrusion tooling. Tempered at 540-650°C to produce a martensite matrix with fine alloy carbide dispersion. Service hardness: HRC 42-52 (lower than cold-work grades, but maintained at 500-600°C).

**[High-speed steels](../glossary/high-speed-steels.md)** (HSS):
- **[M-series](../glossary/m-series.md)** (Molybdenum HSS, e.g., M2): 0.85% C, 4% Cr, 5% Mo, 6% W, 2% V. The dominant cutting tool steel. Red-hardness to ~600°C — retains HRC 60+ at cutting edge temperatures that would soften plain carbon steel. The mechanism: secondary hardening during tempering. When tempered at 540-560°C, fine VC and Mo₂C precipitates form, replacing the hardness lost during the initial temper. Multiple tempers (2-3 cycles) are required to decompose retained austenite — each cycle converts some retained austenite to fresh martensite that must be tempered in the next cycle.
- **[T-series](../glossary/t-series.md)** (Tungsten HSS, e.g., T1): 0.75% C, 4% Cr, 18% W, 1% V. The original HSS composition (Taylor and White, 1901). Tungsten provides the same secondary hardening as molybdenum but at higher cost. M-series has largely replaced T-series except for special applications.
- Used for drill bits, lathe tools, milling cutters, taps, saw blades. Cutting speeds 3-5× higher than plain carbon steel tools.

**Shock-resistant tool steels**:
- **[S-series](../glossary/s-series.md)** (e.g., S7): 0.5% C, 3.25% Cr, 1.4% Mo. Lower carbon than other tool steels for maximum toughness. Used for chisels, punch pins, shear blades, jackhammer bits. Hardness: HRC 54-56. Can withstand repeated impact without fracturing.

### Manganese Steel (Hadfield Steel)

Hadfield steel (invented 1882) is the archetype of a work-hardening alloy:

- **Composition**: 12-14% Mn, 1.0-1.4% C. The high manganese and carbon are both essential — neither alone produces the effect.
- **As-quenched properties**: Solution-treated at 1050-1100°C and rapidly water-quenched to retain a fully austenitic structure. In this condition, the steel is surprisingly soft (HB ~200, tensile strength ~800 MPa, elongation 40-50%). The austenite is metastable.
- **Work hardening**: When cold-worked (impact, abrasion, plastic deformation), the surface transforms to martensite and mechanical twins form, creating an extremely hard surface layer (HB 500-550) while the core remains tough and ductile. This is unique — the harder you hit it, the harder the surface gets. The work-hardening rate is 10-15× that of plain carbon steel.
- **Applications**: Rock crusher jaws and cone liners, ball mill liners, railway track components (frogs, switches), excavator bucket teeth, armor plating. Any application requiring high impact resistance combined with abrasive wear resistance.
- **Machining difficulty**: Nearly impossible to machine conventionally — any cutting tool work-hardens the surface ahead of the cut. Must be ground, or machined with extreme care using sharp tools and minimal feed. Cast to near-net shape whenever possible.
- **Welding**: Requires careful preheat and post-weld solution treatment to restore austenitic structure in the heat-affected zone. Without re-solutionizing, the HAZ becomes embrittled by carbide precipitation and partial martensitic transformation.

### Superalloys

Superalloys are nickel, iron-nickel, or cobalt-based alloys designed for service at temperatures above 540°C, where most steels have lost their strength. They are the materials that make gas turbines, jet engines, and nuclear reactors possible.

**[Nickel-based superalloys](../glossary/nickel-based-superalloys.md)** (the dominant class):
- **[Inconel 718](../glossary/inconel-718.md)** (Ni-19Cr-18Fe-5Nb-3Mo-0.5Al-1Ti): The most widely used superalloy. Strengthened by γ" precipitates (Ni₃Nb, body-centered tetragonal) formed during aging at 720°C + 620°C (two-step heat treatment). Yield strength ~1,035 MPa at room temperature, ~860 MPa at 650°C. Used for gas turbine discs, shafts, casings, fasteners. Excellent weldability for a superalloy — the slow precipitation kinetics of γ" permit welding without post-weld cracking.
- **[Inconel 625](../glossary/inconel-625.md)** (Ni-22Cr-9Mo-3.5Nb): Solid-solution strengthened (no precipitation hardening). Exceptional corrosion resistance in seawater and acidic environments. Used for chemical processing, marine, nuclear. Tensile strength ~830 MPa. Service temperature to ~980°C for oxidation resistance.
- **[Hastelloy C-276](../glossary/hastelloy-c-276.md)** (Ni-16Cr-16Mo-5Fe-4W): Outstanding resistance to both oxidizing and reducing acids, including hydrochloric and sulfuric acid at concentrations and temperatures that destroy stainless steel. The tungsten and molybdenum provide pitting and crevice corrosion resistance. Used for flue gas desulfurization, chemical reactors, pollution control.
- **[Waspaloy](../glossary/waspaloy.md)** (Ni-20Cr-14Co-4Mo-3Ti-1.5Al): Higher-temperature capability than 718. Strengthened by γ' precipitates (Ni₃(Al,Ti), ordered FCC). Service temperature to ~760°C. Used for turbine blades in older engine designs.
- **[γ' precipitation](../glossary/precipitation-metals.md)** (Ni₃Al): The fundamental strengthening mechanism in Ni-superalloys. The ordered FCC γ' precipitate is coherent with the γ matrix — the crystallographic planes match with slight lattice misfit (~0.1-0.3%). Dislocations must either cut through the ordered precipitates (creating antiphase boundaries) or loop around them (Orowan mechanism). Both require enormous energy, providing high-temperature strength that increases with temperature up to ~800°C — unique among structural materials.

**Cobalt-based superalloys**:
- **[Stellite](../glossary/stellite.md)** (Co-30Cr-5W-1C, various grades): Cobalt matrix with massive chromium and tungsten carbide volume. Outstanding wear resistance, corrosion resistance, and hot-hardness. Used for hard-facing (weld overlay on worn parts), valve seats, cutting tools for high-speed machining of difficult materials, surgical prosthetics. Hardness: HRC 40-55 depending on grade.
- Co-based alloys rely on carbide strengthening rather than γ' precipitation. Cobalt has a higher melting point (1,495°C) than nickel (1,455°C) and superior hot corrosion resistance in sulfidizing environments.

**Single-crystal and directionally solidified turbine blades**:
- The performance-limiting factor for gas turbine efficiency is turbine inlet temperature, which is limited by the creep resistance of the blade material. Creep (time-dependent plastic deformation at high temperature) initiates at and propagates along grain boundaries.
- **Directional solidification (DS)**: Carefully controlled cooling from one end of the mold produces columnar grains aligned parallel to the blade's centrifugal stress axis. Eliminates transverse grain boundaries — the weakest orientation for creep. 10-20× improvement in creep life vs. equiaxed casting.
- **Single-crystal (SX) blades**: A helical grain selector at the base of the mold allows only one grain to propagate into the blade cavity. Zero grain boundaries. Further 2-3× improvement in creep life over DS. Used in modern jet engine and industrial gas turbine first-stage blades operating at >1,000°C (with internal air cooling channels and thermal barrier coatings).
- **[Investment casting](../glossary/investment-casting.md)** is the only practical method — the complex internal cooling passages are formed by ceramic cores that are leached out after casting.

### Specialty Copper Alloys

Beyond the basic brasses and bronzes covered in [Copper & Bronze](copper-bronze.md), several copper alloys serve critical specialized roles:

**Beryllium copper (Be-Cu)**:
- **Composition**: Cu-2% Be-0.3% Co (typical, C17200). Solution-treated at 780-800°C, quenched, then aged at 315-350°C.
- **Properties**: Precipitation-hardened to HRC 36-44 — the highest hardness of any copper alloy. Tensile strength up to 1,400 MPa. Non-sparking (essential for tools used in explosive atmospheres — oil refineries, mines, grain elevators). Non-magnetic. Excellent electrical and thermal conductivity (25-30% IACS in hardened condition). Fatigue endurance limit ~300 MPa — superior to all other copper alloys.
- **Applications**: Non-sparking hand tools, electrical spring contacts, safety tools, X-ray windows (beryllium is transparent to X-rays), precision instruments, plastic injection mold cores.
- **Health hazard**: Beryllium dust and fumes cause chronic beryllium disease (berylliosis) — a serious and potentially fatal lung condition. Machining requires strict dust control, ventilation, and respiratory protection. See Safety section.

**Phosphor bronze**:
- **Composition**: Cu-3.5-10% Sn-0.03-0.35% P. Tin provides solid-solution strengthening; residual phosphorus deoxidizes the melt.
- **Properties**: Excellent spring properties, fatigue resistance, and low friction coefficient. Tensile strength 550-700 MPa (cold-worked). Used for electrical connectors, spring contacts, bellows, bearings, marine propellers, musical instrument strings.
- Superior stress corrosion cracking resistance vs. brass in ammonia environments.

**[Cupronickel](../glossary/cupronickel.md)** (copper-nickel):
- **[90/10 Cu-Ni](../glossary/9010-cu-ni.md)** (C70600): 90% Cu, 10% Ni, 1.5% Fe, 0.5% Mn. Excellent seawater corrosion resistance — the nickel stabilizes the protective oxide film. Biofouling resistance (copper ions inhibit marine organism attachment). Used for seawater desalination tubing, ship hull cladding, offshore platform piping.
- **[70/30 Cu-Ni](../glossary/7030-cu-ni.md)** (C71500): Higher strength and slightly better corrosion resistance than 90/10, but more expensive. Used for condenser tubes in power plants, naval ship piping.

### Titanium Alloys

Titanium alloys occupy a critical niche: high strength-to-weight ratio (density 4.51 g/cm³, ~60% of steel), excellent corrosion resistance (TiO₂ passive film similar to stainless steel), and biocompatibility. The primary limitation is cost — titanium extraction (Kroll process, see [Aluminum](aluminum.md) for comparable electrolytic metal production) is energy-intensive and batch-process-based.

**Ti-6Al-4V (Grade 5, the workhorse)**:
- **Composition**: 6% Al, 4% V, balance Ti. α+β alloy — aluminum stabilizes the hexagonal close-packed α phase, vanadium stabilizes the body-centered cubic β phase.
- **Microstructure**: Dual-phase, with the α/β ratio controlled by thermomechanical processing. Two common microstructural conditions:
  - **[Mill-annealed](../glossary/mill-annealed.md)** (α + dispersed β): Equiaxed α grains in a β matrix. Good ductility, moderate strength. Tensile strength ~900-950 MPa, yield ~830 MPa, elongation 13-16%.
  - **[β-annealed](../glossary/annealed.md)** (lenticular α in prior-β grains): Slow cooling from above the β transus (~995°C) produces a Widmanstätten (basketweave) α+β structure. Higher fracture toughness and fatigue crack growth resistance, but lower ductility.
- **Heat treatment**: Solution-treated at 900-950°C (below β transus), water quenched, then aged at 480-650°C. Aged strength up to 1,100 MPa.
- **Applications**: Aerospace structural components (fan blades, landing gear, wing frames), medical implants (hip stems, bone plates, dental abutments — titanium's osseointegration ability is unique), chemical processing (heat exchangers in corrosive service), marine.
- **Limitations**: Poor tribological properties (galling, poor wear resistance) — requires surface treatments or coatings for bearing surfaces. Low thermal conductivity makes machining difficult (heat concentrates at the cutting edge). Reactive with oxygen above ~600°C — all hot working must be done in inert atmosphere or with protective coatings.

**β titanium alloys**:
- **Ti-10V-2Fe-3Al**: Near-β alloy, solution-treated above β transus and aged. Very high strength (up to 1,250 MPa), excellent fatigue performance, good fracture toughness. Used for aerospace forgings, landing gear components.
- Fully β-stabilized alloys (e.g., Ti-15V-3Cr-3Al-3Sn) can be cold-formed in the solution-treated condition (BCC β phase is ductile), then aged to high strength. Used for springs, fasteners.

**α titanium alloys**:
- Commercially pure titanium (CP Grades 1-4, varying oxygen content from 0.18% to 0.40%): Single-phase α. Oxygen is an interstitial strengthener — Grade 4 (0.40% O) has ~550 MPa yield vs. Grade 1 (0.18% O) at ~170 MPa. Used where corrosion resistance is paramount: chemical plant equipment, marine, architectural, heat exchanger tubing. Grade 1 is used for deep-drawing applications due to excellent formability.

### Aluminum Alloys

Primary aluminum production is covered in [Aluminum](aluminum.md). The major alloy systems are summarized here:

**[Wrought alloy designation](../glossary/wrought-alloy-designation.md)** (4-digit system):
- **1xxx**: ≥99% Al. Excellent corrosion resistance, conductivity. Not heat-treatable. Used for electrical conductors, foil.
- **[2xxx](../glossary/2xxx.md)** (Al-Cu, e.g., 2024): Precipitation-hardened (Al₂Cu). High strength (~470 MPa for 2024-T3) but poor corrosion resistance — usually clad with pure aluminum (alclad). The classic aircraft structural alloy (first developed in the 1930s).
- **[6xxx](../glossary/6xxx.md)** (Al-Mg-Si, e.g., 6061): Moderate strength (~310 MPa for 6061-T6), excellent formability and corrosion resistance, weldable. The most versatile aluminum alloy — used for structural shapes, machine parts, marine, automotive.
- **[7xxx](../glossary/7xxx.md)** (Al-Zn-Mg-Cu, e.g., 7075): Highest strength aluminum alloy (~570 MPa for 7075-T6). Zinc and magnesium form MgZn₂ precipitates (η phase). Used for aircraft frames, high-strength sporting goods. Susceptible to stress corrosion cracking in the peak-aged condition — overaged tempers (T73) sacrifice ~10-15% strength for full SCC resistance.

**Spring steels**:
- Spring steels are medium-to-high carbon steels (0.5-1.0% C) or alloy steels designed to withstand repeated elastic deformation without permanent set or fatigue failure. The key requirement: high elastic limit and high fatigue endurance limit relative to yield strength.
- **[Music wire](../glossary/music-wire.md)** (0.8-1.0% C): Patent-drawn (austenitized, quenched in lead bath at ~500°C to form fine pearlite, then cold-drawn). Tensile strength up to 3,000 MPa in the finest gauges — among the strongest steel products. Used for precision springs, piano wire, valve springs.
- **[Chrome-vanadium spring steel](../glossary/chrome-vanadium-spring-steel.md)** (0.5% C, 0.8% Cr, 0.15% V, e.g., AISI 6150): Oil-quenched and tempered to HRC 42-48. Vanadium refines grain size, improving fatigue life. Used for automotive leaf and coil springs, torsion bars.
- **[Chrome-silicon spring steel](../glossary/chrome-silicon-spring-steel.md)** (0.55% C, 0.7% Cr, 1.5% Si, e.g., AISI 9254): Silicon raises the elastic limit and improves temper resistance. Oil-quenched from 860-900°C, tempered at 400-450°C. Used for high-stress valve springs, clutch springs. Silicon also increases resistance to stress relaxation at elevated temperatures.

**[Casting alloys](../glossary/casting-alloys.md)** (e.g., A356 = Al-7Si-0.3Mg): Silicon improves castability (fluidity, reduced shrinkage). Heat-treatable via Mg₂Si precipitation. Used for engine blocks, transmission cases, wheels. Al-Si eutectic (12.6% Si) provides the best fluidity — hypereutectic alloys (e.g., A390, 17% Si) used for wear-resistant cylinder liners where primary Si particles provide abrasion resistance.

### Alloy Design Principles

The development of new alloys follows a systematic approach rooted in thermodynamics and kinetics:

**Phase diagrams**:
- Binary and ternary phase diagrams map the equilibrium phases as a function of composition and temperature. The iron-carbon diagram (see [Iron & Steel](iron-steel.md)) is the most important in metallurgy, but the Ni-Al, Ti-Al-V, Cu-Be, and Fe-Cr-Ni systems are essential for specialty alloy design.
- **[Solidus and liquidus](../glossary/solidus-and-liquidus.md)** define the melting range. Alloys with narrow melting ranges (eutectics, pure metals) cast well; wide ranges cause segregation.
- **[Phase boundaries](../glossary/phase-boundaries.md)** determine heat-treatment temperatures: solutionizing (above solvus), quenching, and aging (below solvus, in the two-phase region where precipitates nucleate and grow).

**Strengthening mechanisms**:
- **Solid solution strengthening**: Solute atoms (different size or valence than the host) distort the crystal lattice, creating stress fields that impede dislocation motion. Effect: ~Δσ ∝ √(concentration). Examples: Cr in Fe (stainless), Sn in Cu (bronze), Al in Ti.
- **[Precipitation hardening](../glossary/precipitation-hardening.md)** (age hardening): Supersaturated solute precipitates as fine, coherent particles during aging. Maximum strength occurs at the optimal precipitate size — too fine and dislocations cut through easily; too coarse (overaged) and spacing is too wide. The peak-aged condition represents the ideal precipitate size and volume fraction. Examples: Cu in Al (2xxx series), γ' in Ni-superalloys, Cu in Be-Cu.
- **Dispersion strengthening**: Hard, insoluble particles (oxides, carbides) introduced mechanically or by internal oxidation. Unlike precipitates, they do not coarsen at high temperature — making them suitable for creep-resistant alloys. Example: thoria-dispersed (TD) nickel, oxide-dispersion-strengthened (ODS) steels.
- **Grain boundary strengthening (Hall-Petch)**: σ_y = σ₀ + k·d^(-1/2), where d is grain diameter. Finer grains → higher yield strength AND better toughness — the only mechanism that improves both simultaneously. Achieved by controlled rolling, recrystallization, and grain-refining additions (Nb, Ti, Al form pinning particles that prevent grain growth). This relationship breaks down below ~10-20 nm (nanograins), where grain boundary sliding dominates.

**Selection criteria for engineering applications**:
- **Strength-to-weight ratio**: Critical for aerospace and transport. Ti-6Al-4V (σ/ρ ≈ 200 kN·m/kg) vs. 7075-T6 (≈ 200) vs. 4340 steel (≈ 80). Titanium and high-strength aluminum are comparable per unit mass, but steel is 3× denser.
- **Corrosion resistance**: Determine the specific environment (oxidizing vs. reducing, chlorides, acids, temperature). Select by PREN (pitting resistance equivalent number): PREN = %Cr + 3.3×%Mo + 16×%N. Higher PREN = better localized corrosion resistance.
- **Temperature capability**: Ferritic steels to ~500°C, austenitic stainless to ~750°C, Ni-superalloys to ~1,000°C (cooled components in gas turbines to ~1,100°C). Creep rate accelerates exponentially with temperature — a factor of 10× per 20-30°C increase in many alloys.
- **Fabricability**: Weldability, castability, machinability, formability. A high-performance alloy that cannot be fabricated into the required shape is useless. Welding is the most common limitation — high-strength alloys are often unweldable due to hot cracking, HAZ softening, or stress corrosion susceptibility.

### Safety & Hazards

**Beryllium and beryllium copper**:
- Beryllium dust, fumes, and oxide are extremely toxic. Inhalation of airborne Be particles (>0.1 μg/m³) can cause chronic beryllium disease (CBD, berylliosis) — a granulomatous lung disease that may manifest years after exposure and is potentially fatal. Sensitization occurs in ~2-5% of the exposed population regardless of exposure level — it is an immune-mediated response.
- Machining Be-Cu requires: local exhaust ventilation, wet machining (coolant suppresses dust), HEPA-filtered vacuum cleanup (never dry-sweep), respiratory protection (P100 or powered air-purifying respirator), and designated regulated areas with access controls.
- Beryllium oxide (BeO) ceramics, used for high-thermal-conductivity electrical insulators, present the same inhalation hazard when machined or abraded.

**Chromium and nickel**:
- Hexavalent chromium (Cr⁶⁺) is a carcinogen formed during welding of stainless steels (chromium in the weld fume oxidizes to Cr⁶⁺). Stainless welding requires local exhaust ventilation and respiratory protection.
- Nickel and nickel compounds are skin sensitizers and suspected carcinogens. Prolonged skin contact with nickel-containing alloys can cause allergic contact dermatitis.
- Grinding and polishing of stainless and nickel alloys generates fine metallic dust requiring ventilation.

**Titanium**:
- Titanium powder and fine chips are a severe fire hazard — titanium burns vigorously in air once ignited, and water cannot extinguish titanium fires (the reaction Ti + 2H₂O → TiO₂ + 2H₂ actually accelerates the fire). Class D fire extinguishers (dry powder) are required in titanium machining areas.
- Titanium smelting and melting must be done under vacuum or inert atmosphere to prevent violent oxidation.

**Cobalt**:
- Cobalt and cobalt compounds are suspected carcinogens (IARC Group 2B). Cobalt dust from grinding Stellite and other Co-based alloys requires respiratory protection and dust control.
- Hard metal disease (cobalt lung) affects workers exposed to cobalt-tungsten carbide (WC-Co) composite dust — associated with the cobalt binder phase dissolving in lung fluid.

**General heat treatment hazards**:
- Quenching oils present fire risk — oil can ignite if workpiece temperature exceeds flash point. Use tempered quench oils with adequate fire suppression. Never quench in water after heating in a salt bath — residual salt contacting water can cause explosive spattering.
- Protective atmospheres for heat treatment (hydrogen, argon, vacuum) present asphyxiation hazards in confined spaces. Hydrogen is also explosive (LEL 4% in air). Monitor atmospheres continuously.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Metals](./index.md) • [All Domains](../index.md)*
