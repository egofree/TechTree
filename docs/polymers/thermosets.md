# Thermosetting Polymers

> **Node ID**: polymers.thermosets
> **Domain**: [Polymers](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`chemistry.petroleum-alternatives`](../chemistry/petroleum-alternatives.md), [`machine-tools`](../machine-tools/index.md)
> **Enables**: [`chemistry.packaging-testing`](../chemistry/packaging-testing.md), [`electronics.assembly`](../electronics/assembly.md), [`photolithography.resists-masks`](../photolithography/resists-masks.md), [`polymers.composites`](composites.md)
> **Critical**: No — thermosets are valuable but alternatives (thermoplastics, ceramics, metals) exist for most applications

## Problem

Thermosetting polymers are plastics that undergo an irreversible chemical reaction (cross-linking) during curing, forming a three-dimensional molecular network. Unlike thermoplastics (which soften when heated and can be reprocessed), thermosets permanently set into their final shape — once cured, they cannot be melted, remolded, or recycled by simple reheating. This irreversible cross-linking is both their defining characteristic and their primary advantage: thermosets resist heat deformation, chemical attack, and creep far better than thermoplastics.

The major thermoset families — phenolic (Bakelite), epoxy, unsaturated polyester, polyurethane, and melamine-formaldehyde — serve distinct roles: phenolics for electrical insulation and heat-resistant components; epoxies for high-performance adhesives, coatings, and composite matrices; polyesters for fiberglass-reinforced structures (boats, tanks, pipes); polyurethanes for foams, elastomers, and coatings; and melamine for decorative laminates and dinnerware.

## Prerequisites

- [Chemistry](../chemistry/index.md) — organic synthesis and polymerization fundamentals
- [Petroleum alternatives](../chemistry/petroleum-alternatives.md) — feedstock chemicals for thermoset resins
- [Machine tools](../machine-tools/index.md) — molds, presses, and processing equipment
- [Glass fibers](../glass/fibers.md) — fiberglass reinforcement for polyester composites
- [Thermoplastics](thermoplastics.md) — complementary polymer processing knowledge

## Materials and Processes

## Phenol-Formaldehyde (Bakelite)

First synthetic plastic (commercialized 1909). Phenol + formaldehyde condensation polymerization, two distinct routes:

**[Novolac route](../glossary/novolac-route.md)** — acid catalyst (HCl or oxalic acid), excess phenol. Produces a thermoplastic prepolymer that remains uncured until mixed with hexamethylenetetramine (hexamine) hardener and heated. Two-step process: synthesize resin, then blend with filler and cure.

**[Resole route](../glossary/resole-route.md)** — base catalyst (NaOH or ammonia), excess formaldehyde. Self-curing prepolymer; continued heating drives cross-linking without added hardener.

- Process conditions: 80–150°C initial condensation reaction; 150–200°C compression molding with fillers (wood flour, mineral fillers, cotton flock)
- Pressure: 15–30 MPa in compression press
- Properties: hard, rigid, excellent electrical insulator, heat-resistant to ~200°C, chemically inert to most solvents
- Applications: electrical insulators, switchgear components, distributor caps, molded fittings, early plastic goods
- Note: novolac resins are also the basis for positive-tone photoresist binders in [Photolithography](../photolithography/resists-masks.md)

## Epoxy Resins

Bisphenol-A + epichlorohydrin yields diglycidyl ether of bisphenol-A (DGEBA), the workhorse epoxy prepolymer. The epoxy group (three-membered oxirane ring) is highly strained and reactive with nucleophiles (amines, acids, thiols). Cured with hardeners in a two-part formulation:

- **[Amine hardeners](../glossary/amine-hardeners.md)** (DETA, TETA): room temperature to 80°C cure, fast pot life (30-60 minutes). Aliphatic amines (DETA, TETA) cure at room temperature; cycloaliphatic amines (isophorone diamine, IPDA) require elevated temperature (60-80°C) but produce higher Tg.
- **Anhydride hardeners**: 100–150°C cure, better electrical properties (lower dielectric constant and dissipation factor — critical for electronic potting and encapsulation), longer pot life (4-8 hours at 25°C — more working time for large pours), lower exotherm (reduced risk of thermal runaway in thick sections). MTHPA (methyltetrahydrophthalic anhydride) is the most common.

Process conditions vary by application:

- Structural adhesive: mix resin/hardener, apply at room temp, post-cure 60–80°C for 2-4 hours. Lap shear strength on aluminum: 15-25 MPa. Gap filling: up to 0.5 mm without filler (thicker gaps require silica or glass microsphere filler to prevent resin-starved joints and excessive exotherm).
- Composite matrix: vacuum bag layup, cure 80–120°C under vacuum (0.8-0.95 bar negative pressure — the vacuum removes entrapped air and compacts the laminate). For high-performance aerospace composites: autoclave cure at 120-180°C under 0.3-0.7 MPa external pressure (autoclave pressure + vacuum produces the lowest void content, <0.5%).
- Potting and encapsulation: pour or transfer mold, cure 80–150°C. Potting compounds must have low viscosity (5,000-15,000 mPa·s at 25°C) for complete void-free filling of electronic assemblies, low exotherm (maximum temperature rise <100°C during cure — excessive exotherm can damage temperature-sensitive components), and matched CTE (coefficient of thermal expansion — epoxy CTE ~50-80 ppm/°C, must be managed with silica filler to reduce CTE to ~20-30 ppm/°C for reliability in thermal cycling).

Properties: high adhesive strength (tensile shear on Al-Al: 15-25 MPa for room-temperature-cured epoxy — one of the strongest structural adhesives available), excellent chemical resistance (resists water, oils, fuels, dilute acids and alkalis — cured epoxy is essentially insoluble in all common solvents), low shrinkage on cure (<2% — compared to 5-8% for polyester resin, the low shrinkage produces dimensionally accurate castings and minimal residual stress in bonded joints), good electrical insulation (volume resistivity 10¹³-10¹⁵ Ω·cm, dielectric strength 15-25 kV/mm — suitable for electronic potting and PCB substrate applications).

Applications: die attach adhesive ([Semiconductor Packaging](../chemistry/packaging-testing.md) — epoxy-silver adhesive attaches the silicon die to the lead frame with both mechanical bonding and thermal conductivity), IC encapsulation (transfer-molded epoxy with silica filler encapsulates the integrated circuit for mechanical and environmental protection — >95% of all ICs are packaged in epoxy molding compound), composite matrix resin (see [Composites](./composites.md)), structural adhesive (aircraft, automotive, and construction bonding — epoxy adhesives can replace rivets and bolts in many applications, distributing stress more evenly across the joint), PCB substrate bonding (copper-clad FR-4 laminate — the epoxy matrix bonds copper foil to the glass-fiber substrate), protective coatings (pipeline coatings, tank linings, marine anti-corrosion primers — epoxy provides the best adhesion to steel of any organic coating).

## Phenolic Laminates (FR-4 / G-10)

Phenolic or epoxy resin impregnated into paper (phenolic grades) or woven glass fabric (epoxy grades), then layered and hot-pressed. The resulting laminate is a rigid, dimensionally stable sheet with excellent electrical insulation properties.

- **G-10**: Epoxy-glass laminate, non-flame-retardant grade. Continuous glass fiber fabric (style 7628, 0.18 mm thick, 18 × 14 ends/picks per cm) impregnated with epoxy resin (resin content 35-45% by weight) to form "prepreg" (pre-impregnated fabric — partially cured B-stage resin that is dry and tacky). Multiple prepreg plies stacked to desired thickness (standard PCB: 1.6 mm = ~8 plies of 7628 fabric). Cured in heated platen press.
- **FR-4**: Brominated epoxy-glass laminate with flame retardancy (UL 94 V-0 — self-extinguishing within 10 seconds after flame removal, no dripping). The brominated epoxy contains tetrabromobisphenol A (TBBPA, 15-20% bromine by weight in the resin) reacted into the polymer backbone. FR-4 is the standard PCB substrate material worldwide — >90% of all rigid PCBs are manufactured on FR-4 laminate.

Process: stack resin-impregnated fabric sheets (prepreg), press at 150–170°C under 3–7 MPa for 60–90 minutes. Cool under pressure to prevent warpage (the laminate must remain under pressure until the resin is below its Tg of ~130-140°C — otherwise internal stresses from differential thermal contraction cause warpage). Post-cure at 180-200°C for 2-4 hours for maximum Tg and chemical resistance.

Properties: excellent electrical insulation (surface resistivity >10¹³ Ω), dimensional stability (water absorption <0.1% for FR-4 — critical for maintaining PCB trace impedance), moisture resistance, flame resistance (FR-4), mechanical strength (flexural strength 350-450 MPa longitudinal for G-10/FR-4 — one of the strongest laminate materials per unit weight).

Applications: **[PCB substrates](../glossary/pcb-substrates.md)** (critical dependency for [Photolithography](../photolithography/resists-masks.md) semiconductor path), electrical panels, terminal boards, brake linings, bearing retainers, structural insulating panels.

## Unsaturated Polyester Resin

Propylene glycol + maleic anhydride (unsaturated dibasic acid, provides the C=C double bonds for cross-linking) + phthalic anhydride (saturated modifier, adjusts rigidity and cost — more phthalic = more rigid, lower cost) condensed into a low-molecular-weight polyester prepolymer (1000-3000 g/mol). Dissolved in styrene monomer (~30–40% by weight) as reactive diluent and cross-linking co-monomer.

Cure mechanism: free-radical polymerization initiated by MEKP (methyl ethyl ketone peroxide) catalyst, typically with cobalt naphthenate accelerator (the cobalt²⁺ ion decomposes the peroxide O—O bond homolytically, generating free radicals that initiate chain-growth polymerization of styrene with the unsaturated polyester chains). Room-temperature cure is standard for hand layup — no oven needed.

- Process: apply gel coat (pigmented polyester resin, 0.4-0.6 mm thickness — provides the cosmetic surface finish and first barrier against water and chemicals) to mold surface, then hand layup of glass fiber mat + resin, roll out air with consolidation roller, cure at ambient temperature (20–30°C, 15-30 min gel, 24 hr full cure)
- Elevated temperature post-cure (60–80°C for 2-4 hours) improves mechanical properties by increasing the cross-link density — glass transition temperature rises from ~60°C (room temperature cure) to ~80-90°C (post-cured)
- Properties: good strength-to-weight ratio (specific tensile strength ~80-120 kN·m/kg — comparable to aluminum at ~100 kN·m/kg), corrosion resistant (no rust, no galvanic corrosion — fiberglass tanks are standard for chemical storage), easily molded into complex shapes
- Applications: fiberglass composite matrix (most common resin for hand layup — ~80% of all fiberglass production uses polyester resin), boat hulls (the largest single application — a 10 m sailboat hull requires ~500-800 kg of fiberglass/polyester composite), tanks, panels, corrosion-resistant equipment, structural enclosures, automotive body panels (Corvette body has been fiberglass-reinforced polyester since 1953)

## Polyurethane / Polyurea

Isocyanate chemistry is the foundation. Diisocyanates (TDI: toluene diisocyanate, density 1.22 g/cm³, boiling point 251°C; or MDI: methylene diphenyl diisocyanate, melting point 40°C for 4,4'-MDI) react with nucleophiles:

- **[Polyols](../glossary/polyols.md)** → polyurethane (foams, elastomers). The hydroxyl group (—OH) of the polyol attacks the electrophilic carbon of the isocyanate group (—N=C=O), forming a urethane linkage (—NH—CO—O—). Each polyol with 2+ hydroxyl groups creates a cross-link point.
- **[Polyamines](../glossary/polyamines.md)** → polyurea (fast-cure spray coatings). The amine group (—NH₂) reacts with isocyanate faster than hydroxyl (amine reaction rate ~100× faster than alcohol at 25°C), forming a urea linkage (—NH—CO—NH—). The extreme reaction speed of polyurea chemistry (gel time <10 seconds) allows vertical and overhead spray application without sagging.

Material forms:

**Flexible foam**: low-density molded cushions, padding, acoustic insulation (TDI + polyether polyol, water as blowing agent, 25–40°C mold temperature — the low mold temperature allows rapid demolding and high production rates). Density 18-40 kg/m³ (memory foam is viscoelastic PU foam with density 40-80 kg/m³ — the slow recovery after compression provides pressure distribution for mattresses). The CO₂ generated by the water-isocyanate reaction inflates the foam. Foam cell structure: open-cell (the cell walls rupture during expansion, creating interconnected air passages — this allows air movement, making flexible foam breathable and compressible). Used for: mattresses, furniture cushions, automotive seating, packaging (foam-in-place packaging molds around the product for shock protection).
- **Rigid foam**: structural insulation panels, refrigeration (MDI + polyester polyol, fluorocarbon or hydrocarbon blowing agent, 30–50°C mold temperature — the blowing agent is trapped in closed cells, providing the low thermal conductivity). Density 28-50 kg/m³. Foam cell structure: closed-cell (cell walls remain intact — the trapped blowing agent gas provides the low thermal conductivity; the closed cells also prevent water absorption). Used for: building insulation (spray foam, rigid board, sandwich panels — wall, roof, and floor insulation), refrigeration (refrigerator and freezer walls — rigid PU foam is the standard insulation material in household refrigerators, typically 50-80 mm thick), cold storage (walk-in freezers, refrigerated transport), pipe insulation (district heating, chemical plant piping).
- **Elastomers**: wheels (forklift and industrial caster wheels — cast PU outlasts rubber 5-10× on abrasive concrete floors; hardness Shore A 90-95 provides load capacity without marking floors), belts (timing belts, flat belts — PU teeth resist wear and maintain precise pitch for timing belt applications), bushings (suspension and pivot bushings — PU provides higher load capacity and better fatigue life than rubber in dynamic loading applications), wear pads (mining chute liners, excavator bucket edges — PU's abrasion resistance is 5-10× that of mild steel in slurry and granular material handling). Cast or injection molded.
- **Spray coatings**: Polyurea for fast-cure protective linings (reaction time <10 seconds — the amine-isocyanate reaction is so fast that the coating gels before it can sag on vertical surfaces). Applied by plural-component spray equipment (two heated hoses delivering isocyanate and amine components to a mixing gun at >2000 psi impingement pressure). Used for: truck bed liners (spray-on polyurea liners provide impact and chemical resistance), secondary containment linings (chemical spill containment — polyurea resists a wide range of chemicals), tank linings (water and wastewater tanks — seamless, pinhole-free lining), bridge deck waterproofing membranes (applied over concrete before asphalt overlay). Thickness: 1-6 mm in single pass. Return-to-service time: <1 hour (the ultra-fast cure allows traffic or equipment placement within minutes of application).

**Complexity warning**: Isocyanate production is non-trivial. The industrial route reacts primary amines with phosgene (COCl₂), which itself requires chlorine + carbon monoxide (CO + Cl₂ → COCl₂ over activated carbon at 200-300°C — the reaction is moderately exothermic and must be temperature-controlled). Phosgene is one of the most toxic industrial chemicals (immediately dangerous to life at 2 ppm — see Safety below). Non-phosgene routes exist (thermal cleavage of urethane to isocyanate + alcohol, or carbonylation of nitroaromatics with CO over Pd catalyst) but are less mature and more expensive. Isocyanates are also toxic respiratory sensitizers and require careful handling, ventilation, and PPE. The entire isocyanate supply chain — from phosgene production through final polymer — demands rigorous safety engineering at every step.

## Phenolic Resin Processing Detail

**[Resole route](../glossary/resole-route.md)** (base-catalyzed, one-stage): Phenol + formaldehyde at 1:1.5-2.0 molar ratio, NaOH catalyst (1-5% based on phenol weight). React at 70-90°C for 2-4 hours. The excess formaldehyde ensures methylol groups form on the phenol ring. The resulting resole is a viscous liquid or low-melting solid that self-cures on further heating without any added hardener. Cure schedule: 140-160°C for 5-30 minutes at 10-30 MPa in a compression mold. Resoles are used for: foundry binders (sand casting cores — phenolic resin coats sand grains, cured with ester hardener at room temperature), bonding 25-40% of all foundry sand cores worldwide.

**[Novolac route](../glossary/novolac-route.md)** (acid-catalyzed, two-stage): Phenol + formaldehyde at 1:0.8 molar ratio, oxalic or hydrochloric acid catalyst (0.5-2%). React at 95-100°C for 2-6 hours. The deficient formaldehyde leaves unreacted ring positions, producing a thermoplastic prepolymer that does not self-cure. To cure: blend with hexamethylenetetramine (hexamine, 10-15% by weight) as a latent hardener — hexamine decomposes on heating above 130°C to release formaldehyde in situ, completing the cross-linking. The two-stage nature provides excellent shelf stability (novolac + hexamine powder blend stores for months at room temperature) and processing safety — the material only cures when heated above 130°C.

**Molding compound preparation**: Blend novolac resin + hexamine hardener + wood flour filler (40-60% by weight — reduces cost and shrinkage) + hexamine (10-15%) + lime (CaO, 1-2% as acid scavenger) + lubricant (zinc stearate, 1%) + pigment (carbon black, iron oxide). Pelletize on a two-roll mill at 70-90°C (warm enough to soften resin but below cure temperature). Compression mold at 150-180°C, 15-30 MPa, 1-5 minutes per mm wall thickness.

## Epoxy Resin Processing Detail

**Resin synthesis**: Bisphenol A (BPA) + epichlorohydrin in molar ratio 1:2-10 (excess epichlorohydrin for higher molecular weight). NaOH (50% aqueous) added as both catalyst and to dehydrohalogenate the chlorohydrin intermediate. Reaction at 50-60°C for 2-4 hours. Product: DGEBA (diglycidyl ether of bisphenol A) — a viscous liquid (n ≈ 0.1-0.2, epoxy equivalent weight 180-190 g/eq). Higher molecular weight versions (n ≈ 2-30) are solid resins used in powder coatings.

**TETA hardener formulation**: Triethylenetetramine (TETA) at 10-14 phr (parts per hundred resin, by weight — calculated from amine hydrogen equivalent weight vs. epoxy equivalent weight). Pot life at 25°C: 30-60 minutes (working time before viscosity increases unworkably). Cure schedule: 24 hours at 25°C (room temperature cure, reaches ~60-70% of ultimate strength) or 2 hours at 80°C (elevated temperature cure, reaches >95% of ultimate strength). For maximum chemical resistance and heat resistance, post-cure at 100-120°C for 1-2 hours to complete conversion of remaining epoxy groups. Tensile shear strength (lap joint, Al-Al): 15-25 MPa. Tensile strength (neat resin): 50-70 MPa.

**[Anhydride hardeners](../glossary/anhydride-hardeners.md)** (methyltetrahydrophthalic anhydride, MTHPA, at 80-90 phr): Longer pot life (4-8 hours at 25°C) than amine hardeners. Cure schedule: 2 hours at 100°C + 4 hours at 150°C (requires elevated temperature — will not fully cure at room temperature). Superior electrical properties (higher dielectric strength, lower dissipation factor) — preferred for electrical potting and encapsulation.

## Polyester Resin Processing Detail

**Resin synthesis**: Propylene glycol + maleic anhydride (provides unsaturated C=C sites for cross-linking) + phthalic anhydride (saturated modifier, adjusts rigidity and cost). Molar ratio typically 1.1:0.5:0.5 (glycol:maleic:phthalic), with 10% excess glycol to control molecular weight. Condensation at 180-210°C under nitrogen blanket for 6-10 hours until acid number drops below 30 mg KOH/g. Dissolve in styrene monomer (30-40% by weight — styrene acts as reactive diluent and cross-linking co-monomer). Add hydroquinone (100-200 ppm) as inhibitor to prevent premature gelation during storage.

**Cure system**: MEKP (methyl ethyl ketone peroxide) catalyst at 1-2% by resin weight. Cobalt naphthenate or cobalt octoate accelerator at 0.2-0.5%. The cobalt ion decomposes the peroxide into free radicals, which initiate the chain-growth copolymerization of styrene with the unsaturated polyester chains. Gel time: 15-30 minutes at 25°C (adjustable by varying catalyst and accelerator concentration — more cobalt = faster gel). Peak exotherm temperature: 80-150°C depending on laminate thickness (thick sections generate more heat due to greater resin volume, which accelerates cure but risks thermal runaway and cracking — limit single-pour thickness to 10-15 mm).

## Urea-Formaldehyde and Melamine-Formaldehyde

**Urea-formaldehyde (UF)**: Urea (CO(NH₂)₂, produced from ammonia + CO₂ at 135-200°C, 100-200 atm) + formaldehyde at 1:1.5-2.0 molar ratio. Base-catalyzed methylolation at 50-60°C (urea + formaldehyde → methylol urea), then acid-catalyzed condensation to desired molecular weight. Primary use: wood adhesive for plywood, particleboard, and MDF (medium-density fiberboard — the world's largest industrial use of any thermoset resin by volume, >10 million tonnes/year globally). Cured in hot press at 100-120°C, 1-2 MPa, 3-5 minutes per mm board thickness. UF-bonded panels dominate interior-grade engineered wood products due to low cost (~$0.30-0.50/kg resin solids — the cheapest wood adhesive) and fast cure. Water resistance: limited — UF bonds degrade with prolonged moisture exposure (hydrolysis of the methylene ether and methylene bridges in the cured network). For exterior-grade panels, use melamine-fortified UF (MUF, 20-30% melamine replacement) or phenol-formaldehyde.

**Melamine-formaldehyde (MF)**: Melamine (C₃H₆N₆, produced from urea at 350-400°C, 70-150 atm — the high temperature causes urea to decompose and recombine into the triazine ring structure of melamine) + formaldehyde at 1:2-3 molar ratio. Base-catalyzed methylolation at 60-80°C, followed by acid cure. MF resins cure to hard, heat-resistant (continuous service to 150°C — higher than UF at ~80°C), scratch-resistant, and chemical-resistant surfaces. The fully cured melamine network has superior cross-link density compared to UF due to the three amino groups on the melamine ring (each capable of reacting with up to two formaldehyde molecules, giving a theoretical maximum of six methylol groups per melamine molecule vs. four per urea molecule). Applications: decorative laminates (Formica-type countertops — MF-impregnated decorative paper layered over phenolic-impregnated kraft paper core, pressed at 140°C, 7-10 MPa, 30-60 minutes — the MF surface provides scratch and stain resistance while the phenolic core provides structural strength), dinnerware (melamine plates and bowls — compression molded, lightweight, break-resistant, heat resistant to 150°C), textile treatment (permanent press finishes for cotton fabrics — MF resin cross-links cellulose fibers, providing wrinkle resistance).

## Safety Data

**Formaldehyde exposure**: OSHA PEL (permissible exposure limit) 0.75 ppm 8-hour TWA (time-weighted average). STEL (short-term exposure limit) 2 ppm for 15-minute exposure. IARC Group 1 carcinogen (nasopharyngeal cancer). Immediately detectable odor at 0.5-1.0 ppm (warning property — if you can smell it, you're near or above the TWA). Monitor with colorimetric detector tubes or electrochemical sensors. Ventilation: local exhaust at resin synthesis reactors and molding presses. Respiratory protection: full-face respirator with formaldehyde cartridge for exposures above PEL.

**Styrene exposure**: OSHA PEL 50 ppm 8-hour TWA. IARC Group 2A (probable carcinogen). CNS depressant at 100+ ppm (headache, dizziness, nausea, reduced reaction time). Strong, penetrating odor detectable at 0.1-0.5 ppm (warning property). Main exposure route during hand layup and spray-up of polyester composites — styrene evaporates from open molds. Control with local exhaust ventilation, low-styrene-emission resin formulations (reducing styrene content to 25-30%, adding wax additives that form a surface film), and respiratory protection.

**Epichlorohydrin**: Used in epoxy resin synthesis. OSHA PEL 2 ppm 8-hour TWA (skin notation — absorbed through skin). IARC Group 2A. Strong, irritating odor. Handle in closed systems with local exhaust. Skin contact causes delayed burns — wear chemical-resistant gloves and splash protection.

## Phenolic Molding Compounds

Phenolic molding compounds are the oldest industrial thermoset molding materials, still widely used for their heat resistance, dimensional stability, and electrical insulation.

**General purpose (GP) grade**: Novolac resin + hexamine + wood flour (50-60% by weight). Density 1.35-1.45 g/cm³. Molding temperature 150-180°C, pressure 15-30 MPa, cure time 30-60 seconds per mm wall thickness. Post-mold shrinkage 0.6-0.9%. Continuous service temperature 150-170°C. Tensile strength 45-55 MPa. Dielectric strength 10-16 kV/mm. Water absorption 0.3-0.5% (24 hours, cold water). Arc resistance 10-20 seconds (relatively poor — phenolics carbonize and track under arcing conditions, unlike ceramic insulators). Cost: lowest of all thermoset molding compounds ($1.50-3.00/kg). Applications: electrical insulators, switch housings, appliance handles, automotive distributor caps, fuse holders, pot handles (high heat resistance), bottle caps (universal bottle cap liner — phenolic disk with pulpboard facing provides chemical resistance and sealing).

**Heat resistant grade**: Novolac + hexamine + mineral filler (asbestos historically, now replaced by mineral wool, silica flour, or clay). Continuous service temperature to 200°C. Lower shrinkage (0.2-0.5%) and better dimensional stability at elevated temperature. Used for: motor commutator segments, high-temperature electrical connectors, heater components.

**Impact grade**: Novolac + hexamine + cotton flock or synthetic fiber (10-30% by weight). Impact strength 2-3× general purpose grade (Izod impact: 2.0-4.0 ft-lb/in vs. 0.3-0.5 ft-lb/in for GP). Tensile strength slightly lower (40-50 MPa). The cotton fibers bridge cracks and absorb impact energy through fiber pull-out. Used for: gearshift knobs, hammer handles, military equipment housings, impact-resistant electrical enclosures, washing machine agitators.

**Electrical grade**: Novolac + hexamine + mica powder (15-30%) or glass fiber (20-30%). Highest dielectric strength (16-20 kV/mm) and arc resistance (60-180 seconds — the mineral filler prevents carbon tracking). Tracking resistance is critical for high-voltage switchgear — phenolic compounds that track (form conductive carbon paths) across the surface under arcing conditions cause catastrophic flashover. Mica-filled grades have the best anti-tracking performance. Used for: high-voltage insulators, circuit breaker components, arc chutes, transformer terminal boards.

## Epoxy Coating and Flooring

Epoxy coatings are two-component systems (resin + hardener) that cure to tough, chemically resistant films. Applied by brush, roller, or spray.

**Solvent-based epoxy coatings**: DGEBA resin + polyamide hardener (40-60 phr, based on amine value). Reduced with xylene or MEK to working viscosity (30-60% solids). Dry film thickness: 50-100 μm per coat. Cure: touch dry 4-8 hours, hard dry 24 hours, full chemical resistance 7 days at 25°C. Used for: tank linings, chemical plant structural steel, marine coatings. The solvent evaporates during cure — ventilation required during application.

**100% solids epoxy**: No solvent — all applied material becomes the cured film. Applied by airless spray or plural-component spray equipment (resin and hardener mixed at the spray gun). Film thickness: 200-500 μm in single coat. Used for: secondary containment floors (chemical spill resistance), food processing plants (hygienic, seamless surface), pharmaceutical clean rooms.

## Polyurethane Foam in Construction

**[Rigid PU foam](../glossary/rigid-pu-foam.md)** is one of the most effective insulation materials available:

- Thermal conductivity: 0.020-0.025 W/(m·K) — the lowest of any common insulation material (compared to mineral wool 0.035-0.040, polystyrene 0.030-0.040, fiberglass 0.030-0.040)
- Closed-cell structure (90-95% closed cells): acts as both thermal insulation and vapor barrier
- Density: 28-50 kg/m³ for insulation applications
- Compressive strength: 100-400 kPa (sufficient for most structural loads when properly supported)
- Service temperature: -50 to +100°C (limited by onset of thermal degradation above 120°C)
- Fire performance: Burns readily — must be protected by thermal barriers (gypsum board, concrete) in building applications. Fire-retardant grades use halogenated or phosphorus-based additives but these reduce insulation performance

**Spray PU foam**: Applied on-site by plural-component spray equipment (two heated hoses — one for isocyanate component, one for polyol blend — meeting at a mixing gun that impingement-mixes the two streams at >2000 psi pressure differential). R-value ~6.5 per inch (RSI ~1.1 per 25 mm). Seals gaps and irregular cavities that batt insulation cannot fill. Used for: wall cavities, roof decks, rim joists, pipe insulation, tank insulation. Requires trained applicators — proper mixing ratio (typically 1:1 by volume, but varies by formulation) and ambient temperature (15-30°C) are critical for full cure and consistent density. Off-ratio spray produces soft, sticky foam (isocyanate-deficient) or brittle, crumbly foam (isocyanate-rich). Cure time: tack-free 10-30 seconds, can be trimmed after 2-5 minutes, full properties after 24 hours.

## Cyanate Ester and Bismaleimide (Advanced Thermosets)

These high-performance thermosets serve in extreme environments beyond the capability of standard epoxies:

**Cyanate ester resins**: Bisphenol A or bisphenol E dicyanate, cured by cyclotrimerization of the cyanate groups (—O—C≡N) into triazine rings at 180-250°C. No byproducts evolved during cure — zero void formation. Tg after cure: 250-290°C (post-cured). Low dielectric constant (2.7-3.2) and dissipation factor (0.001-0.005) — the best dielectric properties of any thermoset. Used for: high-frequency radar antenna radomes, satellite structural components, high-speed digital PCB substrates. Cost: 5-10× epoxy.

**Bismaleimide (BMI)**: Maleic anhydride + methylenedianiline → bismaleimide prepolymer. Cured by addition polymerization at 200-250°C. Tg after cure: 280-320°C. Excellent retention of mechanical properties at 250°C+ — used where epoxy would soften. Applications: military aircraft composite structures (F-22, F-35 airframe components operate at 180-230°C during supersonic flight), engine cowlings, high-temperature tooling. Processing similar to epoxy prepregs (layup + autoclave cure at 200-250°C, 0.3-0.7 MPa).

## Thermoset Processing Equipment

**Compression press**: The workhorse of thermoset molding. Hydraulic press with heated platens (electric cartridge heaters or steam). Capacity: 10-500+ tons clamping force. Platen temperature control: ±5°C uniformity across the platen surface (critical for consistent cure — hot spots cause overcure, cold spots cause undercure). Mold: two steel plates with machined cavity, guide pins, ejector pins. Cycle: load preform → close mold → apply pressure → cure (heat + time) → open mold → eject part. Cycle time: 2-10 minutes for small parts, 30-60+ minutes for large laminates.

**Autoclave curing**: For composite layups and prepregs. The part is vacuum-bagged (see [Composites](./composites.md)) and placed inside a pressure vessel (autoclave). The autoclave pressurizes with heated air or nitrogen to 0.3-0.7 MPa (3-7 bar) at 120-180°C. The combination of vacuum (removes volatiles and air from the laminate) and external pressure (consolidates the layup) produces void-free, high-quality composites. Cure cycle: heat-up at 1-3°C/min → hold at cure temperature for 1-4 hours → cool-down at 1-3°C/min under pressure. The slow, controlled temperature ramp prevents thermal shock and residual stress in thick laminates.

## Key Milestones

Ordered by approximate phase availability:

- ☐ **Chemistry stage**: Bakelite compression molding operational (electrical insulators, molded fittings)
- ☐ **Chemistry stage**: Phenolic resin synthesis (novolac and resole routes)
- ☐ **Chemistry stage**: Urea-formaldehyde molding compounds for housings and fixtures
- ☐ **Chemistry-Vacuum Optics stage**: Unsaturated polyester + fiberglass hand layup (panels, tanks, enclosures)
- ☐ **Vacuum & Optics stage**: Epoxy resin formulation for structural adhesives and composite matrix
- ☐ **Vacuum & Optics stage**: G-10 epoxy-glass laminate production (electrical insulation panels)
- ☐ **Vacuum & Optics stage**: Polyurethane flexible and rigid foam production
- ☐ **Silicon stage**: FR-4 brominated epoxy-glass laminate for PCB substrates
- ☐ **Silicon stage**: Polyurea spray coating capability
- ☐ **Photolithography stage**: Novolac-based photoresist resin for photolithography (same chemistry as Bakelite novolac route)
- ☐ **Photolithography stage**: Novolac-based photoresist resin for photolithography (same chemistry as Bakelite novolac route — the novolac resin is blended with a photoactive compound, typically DNQ, which acts as a dissolution inhibitor. UV exposure converts DNQ to indene carboxylic acid, making the exposed region soluble in aqueous developer — the basis for positive-tone photoresist)
- ☐ **Photolithography stage**: Epoxy die attach and IC encapsulation materials qualified for fab use (epoxy-silver adhesive for die attach, epoxy molding compound with fused silica filler for encapsulation — both materials must meet strict purity requirements: total ionic impurities <10 ppm, alpha particle emission <0.01 counts/cm²/hr to prevent soft errors in memory chips)

## Safety & Hazards

- **Formaldehyde (IARC Group 1 carcinogen)**: A confirmed human carcinogen used in both phenol-formaldehyde (Bakelite) and urea-formaldehyde resin production. Inhalation of formaldehyde vapor causes nasal and respiratory tract irritation at 0.5-1 ppm (detectable by odor — the pungent, suffocating smell is a good warning property); chronic exposure increases cancer risk (nasopharyngeal cancer — IARC classification based on epidemiological evidence from industrial workers with prolonged high-level exposure). Use in well-ventilated areas with local exhaust. Wear chemical splash goggles and a respirator with formaldehyde cartridge when handling formaldehyde solutions or during resin synthesis. Monitor airborne concentrations — OSHA PEL is 0.75 ppm (8-hour TWA), STEL 2 ppm (15-minute short-term exposure limit). Formaldehyde also off-gasses from cured UF-bonded particleboard and plywood — indoor air concentrations in structures with extensive UF-bonded paneling can reach 0.1-0.5 ppm, causing eye and respiratory irritation (this "sick building" issue led to the development of low-emission UF resins and formaldehyde-free alternatives). Phenol-formaldehyde bonded panels off-gas negligible formaldehyde due to the more stable cured network (the higher cross-link density of PF resins traps residual formaldehyde more effectively than UF).
- **Phenol (chemical burns, skin absorption)**: Causes severe chemical burns on contact — initially painless because it simultaneously anesthetizes tissue, leading to deeper injury before the victim notices (the local anesthetic effect is caused by phenol's disruption of nerve cell membranes). Absorbed rapidly through intact skin; systemic toxicity targets the liver and kidneys (phenol is metabolized to hydroquinone and other toxic intermediates in the liver). Fatal dose through skin absorption: ~50 g for an adult (a surprisingly small amount — a splash covering the palm of one hand could deliver a lethal dose if not immediately removed). Wear nitrile or neoprylene gloves (not latex — phenol penetrates latex in <10 minutes), chemical splash goggles, and a face shield during phenol handling. In case of skin contact, flush with large amounts of water immediately and seek medical attention — do not rely on pain as an indicator of exposure severity (by the time pain appears, significant tissue damage may have already occurred). Polyethylene glycol (PEG 400) is the preferred decontamination solution for phenol skin exposure — it complexes with phenol and enhances removal from skin more effectively than water alone.
- **Epoxy sensitization**: Repeated skin contact with uncured epoxy resin or amine hardeners causes allergic contact dermatitis that becomes permanent once sensitized — even trace future exposure triggers severe rash. Once sensitized, a worker may be unable to continue any epoxy-related work. The sensitization rate varies by hardener type: aliphatic amines (DETA, TETA) are the strongest sensitizers (10-20% of exposed workers develop sensitization within 1-2 years of regular contact); cycloaliphatic amines and anhydrides are moderate sensitizers; epoxy resin itself is a weak sensitizer. Wear nitrile gloves, change gloves if contaminated with resin or hardener, and minimize all skin contact. Use barrier creams as a supplement, never a substitute for gloves. The molecular size of the sensitizing agent matters — small amine molecules (MW ~100-200) penetrate skin easily; larger epoxy molecules (MW ~400-1000) penetrate less readily but can still cause sensitization over time.
- **Ammonia (respiratory irritant)**: Used as a base catalyst in the resole route for phenol-formaldehyde. Ammonia gas is a powerful respiratory and eye irritant — 300 ppm is immediately dangerous to life. Handle concentrated ammonia solutions in ventilated areas. Wear eye protection and a respirator if ventilation is insufficient.
- **Styrene (IARC Group 2A)**: Present as reactive diluent in unsaturated polyester resin at 30-40% by weight. CNS depressant at 100+ ppm. Possible carcinogen. OSHA PEL 50 ppm TWA. Room-temperature hand layup with open molds produces significant styrene emissions — typical worker exposure 20-80 ppm without local exhaust ventilation. Install local exhaust at mold work surfaces. Use low-styrene-emission resin grades (wax additives form a surface barrier, reducing emissions by 50-70%).



## Thermoset vs Thermoplastic Selection Guide

| Property | Thermosets | Thermoplastics |
|---|---|---|
| Heat resistance | Excellent (no melting) | Limited by melt temperature |
| Chemical resistance | Excellent (cross-linked network) | Variable (PE excellent, PVC good, nylon moderate) |
| Creep resistance | Excellent (no viscous flow) | Moderate (creeps under sustained load above Tg) |
| Processing | Irreversible cure — cannot be reprocessed | Reversible melting — can be recycled |
| Tooling cost | Lower pressures, simpler molds | Higher pressures, precision molds required |
| Impact resistance | Brittle (rigid cross-linked network) | Tough to brittle (depends on polymer) |
| Applications | Electrical insulation, adhesives, composites | Consumer products, packaging, engineering parts |

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Part blisters or has voids | Trapped air or volatile gases during cure | Degas resin before pouring; increase mold venting; reduce cure temperature ramp rate |
| Incomplete cure (tacky surface) | Insufficient catalyst, wrong ratio, or low temperature | Verify catalyst ratio; increase cure temperature or time; check resin shelf life |
| Part cracks during cure | Exotherm too fast (thick section) or thermal shock | Reduce section thickness; use staged cure (ramp temperature slowly); add inert filler to reduce exotherm |
| Poor adhesion (epoxy bond) | Surface contamination or inadequate surface prep | Clean with solvent; abrade surface; apply primer if specified |
| Shrinkage and warping | High cure shrinkage or uneven cooling | Use low-shrinkage formulation; add fillers (silica, talc); ensure uniform mold temperature |
| Phenolic mold sticking | Insufficient mold release or undercured surface | Apply mold release (silicone or wax); increase cure time; verify mold surface condition |

## See Also

- [Thermoplastics](thermoplastics.md) — reversibly meltable polymers, complementary processing
- [Composites](composites.md) — thermoset matrices (epoxy, polyester) in fiber-reinforced composites
- [Synthetic Polymers](synthetic.md) — synthetic elastomers and specialty polymers
- [Coatings](../chemistry/coatings.md) — thermoset-based paints and protective coatings
- [Electronics Assembly](../electronics/assembly.md) — epoxy encapsulation and PCB substrates
- [Photolithography Resists](../photolithography/resists-masks.md) — phenolic-based photoresists

[← Back to Polymers](index.md)
