# Paints, Coatings & Inks

> **Node ID**: `chemistry.coatings`
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.acids`](acids.md), [`chemistry.petroleum-alternatives`](petroleum-alternatives.md)
> **Enables**: [`metals.finishing`](../metals/finishing.md), [`electronics.electrical-systems`](../electronics/electrical-systems.md)
> **Timeline**: Early Industrial
> **Outputs**: paints, coatings, inks, photoresists
> **Critical**: No — protective coatings extend infrastructure lifespan but do not enable new capabilities directly


Protective and decorative coatings prevent corrosion (the largest single cause of material degradation — estimated $2.5 trillion annual global cost), provide wear resistance, thermal insulation, electrical insulation, and aesthetic appearance. Inks enable printing — essential for marking, labeling, circuit board fabrication (screen-printed thick films), and photolithography (photoresists). This capability bridges basic chemistry (pigments, binders, solvents) with advanced materials engineering (semiconductor photoresists, thermal barrier coatings). Without coatings, steel structures rust, wood rots, and circuits cannot be patterned.

## Prerequisites

- [Acids](acids.md) — chemical processing and pigment production
- [Petroleum alternatives](petroleum-alternatives.md) — solvents and synthetic resin feedstocks
- [Metals](../metals/index.md) — substrates that require protection from corrosion
- [Polymers](../polymers/index.md) — synthetic resins for modern coatings
- [Ceramics](../ceramics/index.md) — pigments and mineral fillers

## Raw Materials

**[Binders (resins)](../glossary/binders-resins.md)** — form the continuous film that adheres to substrate and encapsulates pigment:
- **[Linseed oil](../glossary/linseed-oil.md)** (flax seed): Traditional drying oil — polymerizes by oxidation (cross-linking of unsaturated fatty acid chains catalyzed by air). Still used in artists' paints and wood finishes. Drying time: 2-7 days. Added metallic driers (cobalt, manganese naphthenates) accelerate oxidation to 4-12 hours.
- **Alkyd resins**: Polyester modified with fatty acids — the workhorse of architectural paints. Synthesized from phthalic anhydride, glycerol/pentaerythritol, and drying oil fatty acids at 230-250°C. Air-drying (oxidative cross-linking). Good adhesion, gloss, and weatherability. Solvent-borne alkyds being replaced by water-borne (emulsion) versions due to VOC regulations.
- **Acrylic emulsion**: Polymer particles (methyl methacrylate/butyl acrylate copolymers) dispersed in water — the dominant binder in modern house paints. Film forms by coalescence as water evaporates — polymer particles fuse into continuous film above minimum film-forming temperature (MFFT, typically 5-15°C). Fast drying (1-4 hours), low odor, excellent UV resistance, water cleanup.
- **Epoxy**: Two-component — resin (bisphenol A + epichlorohydrin) + hardener (polyamide or amine). Cures by chemical reaction (not drying). Superior adhesion, chemical resistance, hardness. Used for industrial and marine coatings, floor paints, metal primers. Limitation: poor UV resistance (chalks in sunlight) — topcoat with polyurethane for exterior use.
- **Polyurethane**: Isocyanate + polyol reaction. Two-component for high-performance coatings (automotive, aircraft, industrial flooring). Excellent abrasion resistance, gloss retention, UV resistance (aliphatic isocyanate types like HDI biuret). One-component moisture-cure urethanes react with atmospheric moisture — used for floor and marine coatings.
- **Phenolic resins**: Phenol + formaldehyde condensation. Excellent chemical and heat resistance — used for tank linings, chemical equipment, and as baking enamels for appliances. Dark color limits use to primers or functional coatings.

**[Pigments](../glossary/pigments.md)** — provide color, opacity, and corrosion inhibition:
- **Titanium dioxide (TiO₂)**: The most important white pigment — extreme opacity (refractive index 2.7, vs 1.5 for most binders) from light scattering. Rutile form preferred (higher RI than anatase). Global production: 7 million tonnes/year. Used in virtually every white and light-colored paint. Produced by chloride process (TiCl₄ oxidation at 1000°C) or sulfate process (ilmenite digestion with H₂SO₄).
- **Iron oxides**: Fe₂O₃ (red), Fe₃O₄ (black), FeOOH (yellow ochre). Natural or synthetic. The oldest pigments — used since cave paintings. Low cost, excellent lightfastness, non-toxic. Synthetic versions: precipitate FeSO₄ + NaOH, then oxidize at controlled temperature and pH to control particle size and color.
- **Carbon black**: Incomplete combustion of hydrocarbons (furnace black process — oil injected into 1400°C furnace, quenched, filtered). Particle size 10-100 nm — extreme tinting strength and UV absorption. Used in black inks, tire reinforcement, conductive coatings.
- **Zinc oxide (ZnO)**: White pigment with UV absorption and mildew resistance. Used in exterior paints. Also semiconductor — used in varistor devices and transparent conductive coatings (when doped with aluminum).
- **Zinc chromate / zinc phosphate**: Corrosion-inhibiting pigments for metal primers. Chromate highly effective but toxic (carcinogen) — being replaced by zinc phosphate, calcium ion exchange pigments, and organic corrosion inhibitors.

**Solvents and water**:
- **Water**: The carrier for emulsion (latex) paints — 30-50% of formulation. No VOC, no toxicity, low cost. Requires freeze-thaw stabilizers (propylene glycol), dispersants, and biocides (to prevent microbial growth in the can).
- **Mineral spirits / white spirit**: Petroleum distillate (bp 150-200°C) — solvent for alkyd paints. VOC: 450-550 g/L. Being phased out by regulations.
- **Toluene, xylene**: Aromatic solvents — strong solvency for epoxy and polyurethane. Toxic (neurotoxin) — replaced by oxygenated solvents (butyl acetate, methyl ethyl ketone) where possible.

## Paint Formulation

**[Architectural latex paint](../glossary/architectural-latex-paint.md)** (typical interior wall paint): Water 35%, TiO₂ 20%, calcium carbonate (extender) 15%, acrylic emulsion (binder, 50% solids) 25%, additives 5%. PVC (pigment volume concentration) = 55-70% — above CPVC (critical PVC, ~55%) the film is porous (matte finish). Below CPVC: glossy, washable. Additives: dispersant (polyacrylate — prevents pigment flocculation), defoamer (mineral oil + silica — prevents foam during manufacturing and application), thickener (HEUR associative thickener or HEC cellulose ether — controls viscosity and brushability), biocide (isothiazolinone blend — in-can preservation), coalescent (Texanol — helps polymer particles fuse into film, especially at low temperatures).

**[Industrial epoxy coating](../glossary/industrial-epoxy-coating.md)** (two-component): Part A (resin): epoxy resin 60%, TiO₂ 15%, barium sulfate (extender) 10%, xylene/butanol solvent 15%. Part B (hardener): polyamide curing agent 70%, xylene solvent 30%. Mix ratio A:B typically 4:1 by volume. Pot life after mixing: 4-8 hours. Cure: touch dry 4-8 hours, full cure 7 days. Dry film thickness: 75-200 µm per coat.

**[Alkyd enamel](../glossary/alkyd-enamel.md)** (traditional gloss paint): Alkyd resin (70% solids in mineral spirits) 65%, TiO₂ 25%, driers (Co/Mn/Zr naphthenates) 1%, mineral spirits 9%. Dry film thickness: 30-50 µm. Drying: touch dry 4-6 hours, hard dry 12-18 hours.

## Application Methods

**Brush and roller**: Simplest — manual application. Brush: natural (china bristle for solvent-borne) or synthetic (nylon/polyester for water-borne). Roller: woven or knitted fabric sleeve on a rotating core. Nap length 6-25 mm (shorter for smooth surfaces, longer for textured). Transfer efficiency: 40-60% (fraction of paint reaching the substrate — the rest stays on brush/roller or is lost to overspray).

**Spray coating**:
- **Air spray**: Compressed air (2-4 bar) atomizes paint at the nozzle. Transfer efficiency: 25-40%. High overspray — used where fine finish is critical (automotive topcoats). Requires spray booth with exhaust filtration.
- **Airless spray**: Hydraulic pressure (100-250 bar) forces paint through a small orifice (0.3-0.8 mm) — atomization by hydraulic force alone. Transfer efficiency: 40-60%. Faster application, thicker films per pass. Used for large surfaces (bridges, tanks, buildings).
- **Electrostatic spray**: Paint particles charged at the nozzle (80-100 kV) — attracted to grounded workpiece. Transfer efficiency: 60-95%. Paint wraps around edges and backside. Used for metal furniture, automotive, appliance panels. Water-borne electrostatic requires special isolation (electrically insulated paint supply).

**Dip coating**: Workpiece immersed in coating bath, withdrawn at controlled speed. Film thickness controlled by withdrawal speed and coating viscosity (Landau-Levich equation). Used for small metal parts, fasteners, springs. Requires drain time and drip-off collection. Automotive electrodeposition (E-coat): workpiece is cathode in an electrically charged bath of water-borne epoxy coating — coating deposits on the workpiece by electrophoresis. Gives uniform coverage including recessed areas. Film thickness: 15-30 µm. Worldwide standard for automotive body primers.

**Powder coating**: Dry thermosetting powder (epoxy, polyester, or hybrid) applied electrostatically, then cured in oven at 180-200°C for 10-20 minutes. No solvent — zero VOC. Transfer efficiency: 95-99% (overspray collected and reused). Film thickness: 50-150 µm. Used for metal furniture, appliances, automotive wheels, architectural aluminum. Limitation: only works on substrates that can withstand the curing temperature.

**Strengths**: Powder coating achieves near-zero VOC (no solvent); 95-99% material utilization (overspray recycled); E-coat provides uniform coverage including recessed/hidden areas; electrostatic spray wraps paint around edges and backside of workpiece.

**Weaknesses**: Powder coating requires 180-200°C cure (excludes wood, plastics, heat-sensitive substrates); E-coat needs large immersion bath and 200-350 V DC power supply; electrostatic spray requires electrically conductive substrate (metal only); dip coating has limited thickness control vs. spray.

## Specialty Coatings

**Anticorrosion systems for steel**: Multi-layer system: (1) **[Abrasive blast](../glossary/abrasive-blast.md)** to Sa 2.5 (near-white metal, ISO 8501-1). (2) **[Zinc-rich primer](../glossary/zinc-rich-primers.md)** (organic or inorganic) — galvanic protection (zinc corrodes preferentially, protecting steel). 50-75 µm. (3) **[Epoxy intermediate coat](../glossary/epoxy-intermediate-coat.md)** — barrier protection. 100-200 µm. (4) **[Polyurethane topcoat](../glossary/polyurethane-topcoat.md)** — UV resistance, color/gloss retention, weatherability. 50-75 µm. Total system: 200-350 µm. Service life: 15-25 years to first maintenance in moderate environment (ISO 12944 C3).

**Strengths**: 15-25 year service life in moderate environments; zinc-rich primer provides cathodic protection even at scratches; multi-layer system separates functions (galvanic → barrier → UV); well-standardized (ISO 12944) with predictable performance by corrosivity category.

**Weaknesses**: Surface preparation (abrasive blast to Sa 2.5) is 60-80% of the labor cost; zinc-rich primers require >80% zinc dust in dry film (heavy, expensive); epoxy intermediate chalks in UV — must be topcoated; multi-coat system requires 3+ application steps with inter-coat curing windows.

**[Thermal barrier coatings (TBCs)](../glossary/thermal-barrier-coatings-tbcs.md)** for gas turbine blades: (1) **Bond coat**: MCrAlY (M = Ni, Co) — 100-150 µm, applied by plasma spray or PVD. Forms Al₂O₃ thermally grown oxide (TGO) that bonds the ceramic topcoat. (2) **Topcoat**: Yttria-stabilized zirconia (YSZ, 6-8% Y₂O₃-ZrO₂) — 200-500 µm, applied by electron beam PVD (columnar microstructure, superior strain tolerance) or atmospheric plasma spray (lamellar structure). Enables gas turbine inlet temperatures 200-300°C above the melting point of the nickel superalloy substrate — dramatically increases engine efficiency. Used in jet engines and industrial gas turbines.

**Marine coatings**: Ship hulls face immersion in seawater, UV exposure, mechanical damage, and fouling. Antifouling coatings release biocides (copper oxide, zinc pyrithione — tributyltin banned since 2008) to prevent barnacle, algae, and tubeworm attachment. Modern self-polishing copolymers (SPC): acrylic polymer backbone with biocide chemically bonded — hydrolysis at the coating surface slowly releases biocide and exposes fresh surface. Antifouling coating life: 3-5 years between dry-docking.

## Inks

**Letterpress and offset inks**: High-viscosity paste inks (10-50 Pa·s). Formulation: pigment 15-20%, resin binder (rosin-modified phenolic or alkyd) 20-30%, mineral oil or vegetable oil solvent 40-50%, additives 5-10% (waxes for rub resistance, driers, gelling agents). Offset printing: ink transferred from plate to rubber blanket to paper — requires precise ink-water balance (lithographic principle: ink adheres to image areas, water to non-image areas).

**Screen printing inks**: Used for PCB solder paste, thick-film circuits, textile printing, signage. Heavy paste consistency (50-200 Pa·s). Printed through a mesh screen (40-150 threads/cm) with a squeegee. Wet film thickness: 20-100 µm. Thick-film conductive inks: silver or copper particles in glass frit binder — fired at 600-900°C to sinter metal and fuse glass. Resistor inks: ruthenium oxide (RuO₂) in glass matrix. Dielectric inks: glass-ceramic compositions. Printed electronics (emerging): silver nanoparticle or carbon-based inks printed on flexible substrates (PET, polyimide) — RFID antennas, flexible displays, printed sensors.

**Inkjet inks**: Low viscosity (2-20 mPa·s) — must flow through 10-50 µm nozzles at >10 kHz drop frequency. Dye-based (soluble dye in water/glycol) for vivid color but poor fade resistance. Pigment-based (sub-micron pigment particles dispersed in water) for archival quality. Industrial inkjet: UV-curable inks (acrylate oligomers + photoinitiators) cured by UV LED instantly on the substrate — enables printing on non-porous surfaces (plastic, metal, glass). Ceramic inkjet: sub-micron ceramic pigment particles dispersed in non-aqueous vehicle — printed directly onto ceramic tiles before firing.

## Photoresists (Semiconductor)

**Positive photoresist**: Novolac resin (phenol-formaldehyde) + diazonaphthoquinone (DNQ) photoactive compound. UV exposure converts DNQ to indene carboxylic acid — makes exposed regions soluble in aqueous alkaline developer (TMAH). Unexposed regions remain insoluble. Resolution: ~0.5× the exposure wavelength. 248 nm (KrF excimer) → ~130 nm features. 193 nm (ArF) → ~50 nm features (with immersion lithography and multiple patterning).

**Negative photoresist**: Epoxy or cross-linking chemistry — exposure causes polymerization/cross-linking, making exposed regions insoluble. Higher chemical resistance than positive resists but lower resolution (swelling during development limits feature size). Used for thick-film applications, PCB solder mask, and MEMS structures (SU-8 epoxy resist — single-coat thickness up to 500 µm, enabling high-aspect-ratio microstructures).

**Extreme ultraviolet (EUV) resist**: 13.5 nm exposure wavelength. Challenges: (1) Photon shot noise — at 13.5 nm, photon density is low enough that statistical variations cause line-edge roughness. (2) Outgassing — resist decomposition products contaminate EUV optics ($200M+ replacement cost). Chemically amplified resists (CAR): photoacid generator (PAG) releases acid upon exposure; acid catalyzes deprotection of polymer side groups during post-exposure bake (80-130°C) — one photon triggers 10-100 deprotection reactions, amplifying sensitivity. Metal-oxide resists (MOR): tin or zirconium oxide nanoparticles — higher EUV absorption than organic resists → higher sensitivity and potentially better resolution.

**Strengths**: Positive resist achieves resolution ~0.5× exposure wavelength (sub-50 nm with 193 nm immersion); chemically amplified resists provide 10-100× sensitivity amplification; positive-tone development uses benign aqueous TMAH (no organic solvents); SU-8 negative resist enables 500 µm thick structures for MEMS.

**Weaknesses**: EUV resists face fundamental photon shot noise limit at 13.5 nm; outgassing from resist can contaminate $200M+ EUV optics; chemically amplified resists sensitive to airborne base contamination (requires amine-free cleanroom); post-exposure bake window is narrow (±2°C tolerance for some resists).

## Safety & Hazards

- **Solvents**: VOC emissions contribute to smog formation. Chronic exposure to aromatic solvents (toluene, xylene): liver, kidney, neurological damage. Use ventilation, respiratory protection. Replace with water-borne alternatives where feasible.
- **[Isocyanates](../glossary/isocyanates.md)** (polyurethane component): Respiratory sensitizer — causes occupational asthma. Airborne exposure during spray application is the primary risk. Use supplied-air respirator for spray application, gloves and eye protection for brush/roller. Medical surveillance for workers regularly exposed.
- **Lead and chromate pigments**: Historically used (lead chromate yellow, lead oxide red) — now banned in most countries for consumer paints. Lead-based paint abatement remains a major public health issue in older buildings. Lead poisoning: neurological damage, especially in children.
- **Dust**: Pigment dust (TiO₂, silica, iron oxide) during weighing and mixing — respiratory irritant. IARC classifies TiO₂ as Group 2B (possibly carcinogenic by inhalation in nanoparticle form). Use local exhaust ventilation at mixing stations.
 - **Fire hazard**: Solvent-borne paints in spray booths — explosion risk if vapor concentration exceeds LEL. Fire suppression systems (water spray or dry chemical) required in spray booths. Non-sparking tools and electrical equipment (explosion-proof) mandatory.

## Pigment Volume Concentration

PVC (pigment volume concentration) is the fundamental concept in paint formulation. It is the ratio of pigment volume to total dry film volume (pigment + binder): PVC = V_pigment / (V_pigment + V_binder) × 100%.

**Critical PVC (CPVC)**: The pigment packing density at which there is exactly enough binder to fill all voids between pigment particles. Above CPVC, air voids appear in the dry film. This transition profoundly affects properties: below CPVC, films are glossy, impermeable, and washable; above CPVC, films become matte, porous, and less durable but have higher dry hiding (air-pigment interfaces scatter light). Interior flat wall paints operate above CPVC (PVC 55-75%). Gloss enamels operate well below CPVC (PVC 15-30%). Semigloss paints sit near CPVC.

**TiO₂ optimization**: At $3-4/kg, TiO₂ is the most expensive component in most paints. Formulators minimize TiO₂ content by using extender pigments (CaCO₃, clay, talc) to fill volume below CPVC while TiO₂ provides hiding. Spacing the TiO₂ particles (avoiding crowding) maximizes light scattering per unit of TiO₂ — properly spaced particles give 20-30% more hiding than the same TiO₂ content in a crowded formulation.

**Pigment particle size**: TiO₂ white pigment: 0.2-0.3 μm optimum diameter for visible light scattering (Mie scattering theory). Iron oxide red (Fe₂O₃): 0.1-1.0 μm. Carbon black: primary particle size 10-100 nm, but aggregates to 100-500 nm structures with surface area 15-25 m²/g (for furnace black grades). Smaller carbon black particles provide deeper black but are harder to disperse.

## Application Methods and Film Thickness

**Brush application**: Wet film thickness 80-120 μm per coat. Transfer efficiency 40-60% (rest remains on brush, can, or drips). Brush marks (ridges from bristle action) must level out before the film sets — higher viscosity paints hold brush marks longer. Brush selection: natural bristle for solvent-borne (swells in water), synthetic for water-borne. Brush width 50-100 mm for general work.

**Roller application**: Wet film thickness 100-150 μm. Nap length determines texture transfer: short nap (6-10 mm) for smooth surfaces, medium (12-18 mm) for lightly textured, long (20-25 mm) for rough or exterior surfaces. Roller sleeves are woven or knitted polyester/nylon. Transfer efficiency 40-60%.

**Airless spray**: Hydraulic pressure 1500-3000 psi (100-200 bar) forces paint through a tungsten carbide orifice (0.011-0.031 inch). No compressed air needed. Atomization by sudden pressure release. Wet film thickness 50-150 μm per pass. Transfer efficiency 40-60%. Tip wear is a maintenance concern (abrasive pigments erode the orifice). Used for large flat surfaces: walls, tanks, bridges.

**Conventional air spray**: Compressed air at 40-60 psi (3-4 bar) atomizes paint at the nozzle. Produces the finest atomization for smooth finishes. Transfer efficiency only 25-40% (high overspray). Requires spray booth with exhaust and filter. HVLP (high volume, low pressure) guns reduce overspray and increase transfer efficiency to 50-65%.

## Drying and Curing Mechanisms

**[Oxidative drying](../glossary/oxidative-drying.md)** (air-drying oils, alkyds): Unsaturated fatty acid chains (from linseed, soybean, or tung oil) cross-link by reaction with atmospheric oxygen, catalyzed by metal driers. Cobalt naphthenate or octoate (0.05-0.2% metal on resin) is the primary surface drier (promotes skin formation). Manganese naphthenate assists through-drying. Zirconium and calcium soaps act as auxiliary driers. Linseed oil: touch dry 4-8 hours with cobalt drier, through dry 12-24 hours, full cure 3-7 days as cross-linking continues.

**[Solvent evaporation](../glossary/solvent-evaporation.md)** (lacquers, latex paints): Film forms solely by solvent loss with no chemical reaction. Nitrocellulose lacquers (furniture finishes): dry to touch in 15-30 minutes as solvents (ethyl acetate, butyl acetate, toluene blend) evaporate. Fast recoat but thermoplastic (softens with heat or solvent). Acrylic latex: water evaporates, then polymer particles coalesce above the minimum film-forming temperature (MFFT, 5-15°C). Below MFFT, particles do not fuse and the film cracks. Coalescent solvents (Texanol, 2,2,4-trimethyl-1,3-pentanediol monoisobutyrate) temporarily soften particles to enable coalescence.

**[Thermoset curing](../glossary/thermoset-curing.md)** (epoxy, polyurethane): Two-component systems undergo irreversible chemical reaction. Epoxy-amine: mixed 4:1 to 10:1 (resin:hardener by volume), pot life 2-8 hours, touch dry 4-8 hours, full cure 7 days at 25°C. Accelerated curing at 60-80°C reduces full cure to 4-8 hours but shortens pot life. Polyurethane: isocyanate + polyol, pot life 2-6 hours, recoatable after 4-16 hours. Post-cure at elevated temperature may be required for chemical resistance development.

## Metal Coatings and Corrosion Protection

**Hot-dip galvanizing**: Steel cleaned (degrease, acid pickle, flux), then immersed in molten zinc bath at 440-460°C. Zinc-iron alloy layers form at the steel-zinc interface (Gamma, Delta, and Zeta phases), topped by a pure zinc layer. Coating thickness 40-100 μm (determined by immersion time, steel thickness, and bath composition). Zinc consumption rate in atmospheric exposure: ~0.5-2.0 μm/year in rural environments, 2-5 μm/year in urban/industrial, 2-4 μm/year in marine. At 1.5 μm/year, an 85 μm galvanized coating provides 50+ years of protection in rural environments.

**Phosphating**: Zinc or iron phosphate conversion coating applied by immersion or spray. Steel surfaces are cleaned, then exposed to phosphoric acid solution containing zinc dihydrogen phosphate and accelerators (nitrite or chlorate). Fe dissolution at the surface raises local pH, causing insoluble zinc phosphate crystals to precipitate on the steel surface. Coating weight 1-5 g/m². Provides excellent paint adhesion (phosphate crystals create microscopic anchor profile) and temporary corrosion resistance during storage. The standard pretreatment before automotive electrodeposition primer.

**Zinc-rich primers**: Organic (epoxy binder) or inorganic (ethyl silicate binder) primers loaded with zinc dust (>80% zinc in dry film). Zinc particles are in electrical contact with each other and the steel substrate, providing cathodic (galvanic) protection. Zinc corrodes preferentially, protecting the underlying steel even at scratches and edges. Coating thickness 50-75 μm dry film. Essential first coat in heavy-duty anticorrosion systems for bridges, offshore structures, and tanks.

## Coating Defects and Quality

**Adhesion testing**: Pull-off adhesion test (ASTM D4541): glue a dolly (20 mm diameter steel stub) to the coated surface, pull perpendicularly with a hydraulic adhesion tester until failure. Record failure stress (MPa) and failure mode (adhesive at substrate-primer interface, cohesive within a coat, or adhesive between coats). Minimum acceptable adhesion: 2.5 MPa for structural steel coatings, 5 MPa for high-performance systems.

**Dry film thickness (DFT) measurement**: Magnetic or eddy current gauges (ISO 2808) measure coating thickness on steel substrates. Typical specification: nominal DFT ±20% for each coat. Spot measurements at 5 locations per 10 m², each spot being the average of 3 readings within a 50 mm circle. Total system DFT verified by measuring before and after coating application, or by destructive cross-section measurement on a test panel.

**Common defects**: Orange peel (poor flow/leveling, caused by insufficient solvent or too-rapid drying). Runs and sags (excessive wet film thickness or too-slow drying). Pinholing (air entrapment during application, or solvent boil from too-rapid topcoat over primer). Cratering/fisheyes (surface contamination with silicone or oil causing the wet paint to de-wet). Dry spray (overspray landing as dry particles, caused by spray gun too far from surface or excessive solvent evaporation in hot weather).

## Industrial Coating Systems by Service Environment

**ISO 12944 corrosivity categories**: C1 (very low, heated interiors), C2 (low, rural atmospheres), C3 (moderate, urban/coastal), C4 (high, industrial/coastal), C5 (very high, aggressive industrial/marine), CX (extreme, offshore/splash zone). Each category specifies minimum DFT, number of coats, and expected time to first maintenance.

**C3 system (15-25 years)**: Zinc-rich primer (50 μm) + epoxy intermediate (150 μm) + polyurethane topcoat (50 μm) = 250 μm total. For building steel, bridges in moderate climate.

**C5 system (25+ years)**: Zinc-rich primer (75 μm) + epoxy intermediate (200 μm) + polyurethane topcoat (75 μm) = 350 μm total. For coastal, industrial, and high-humidity environments.

**CX system (thermal spray aluminum for extreme service)**: Abrasive blast to Sa 3. Thermal spray aluminum (200-300 μm) using arc wire spray or flame spray. Sealed with silicone or epoxy sealer. Provides both barrier and cathodic protection. Used on offshore platforms, splash zones, and chimney stacks. Service life 30-50 years with proper maintenance.

## Ink Technology

**Printing ink rheology**: Inks must have specific flow properties for each printing process. Offset inks: high viscosity (10-50 Pa·s) with yield stress to prevent spreading on the printing plate. Flexographic inks: low viscosity (0.05-0.5 Pa·s) for transfer from anilox roll. Inkjet inks: very low viscosity (2-20 mPa·s) with carefully controlled surface tension (28-35 mN/m) for proper drop formation. Thixotropy (shear thinning) is desirable in paste inks: viscosity drops under the high shear of the roller nip, then recovers on the substrate to prevent spreading.

**Pigment dispersion**: Pigments are agglomerated as manufactured and must be deagglomerated to primary particle size for optimal color development and transparency. Dispersion process: (1) pre-mix pigment into vehicle (binder + solvent) with high-speed disperser (1500-3000 RPM, 20-30 minutes), (2) pass through a bead mill or three-roll mill until fineness of grind reaches Hegman gauge reading 7-8 (particle size <10 μm). Bead mill: grinding media (0.3-3 mm yttria-stabilized zirconia or glass beads) agitated at 10-15 m/s tip speed, 3-5 passes. Energy consumption: 50-200 kWh per tonne of ink.

**UV curing**: UV-curable inks and coatings contain photoinitiators (α-hydroxyketones, acylphosphine oxides) that generate free radicals upon exposure to UV light (200-400 nm). The radicals initiate chain polymerization of acrylate oligomers and monomers, curing the film in 0.1-2 seconds. Mercury vapor lamps (100-200 W/cm intensity) or UV LED arrays (365, 385, or 395 nm) provide the UV source. Advantages: instant cure (enables high-speed printing on non-porous substrates), zero VOC, low energy consumption compared to thermal drying. Applications: packaging printing, wood coatings, optical fiber coatings, electronic conformal coatings.

**Color measurement**: CIELAB color space (L* = lightness, a* = red-green, b* = yellow-blue) quantifies color objectively. Spectrophotometer measures reflectance at 10 nm intervals across 400-700 nm. Color difference ΔE = √((ΔL*)² + (Δa*)² + (Δb*)²). A ΔE < 1.0 is imperceptible to most observers; ΔE 1-3 is a slight mismatch; ΔE > 3 is a visible color difference. Production color matching: target ΔE < 2.0 against the standard. Metamerism: two colors that match under one light source but not another (different spectral reflectance curves) is a common problem in pigment formulation, avoided by matching spectral curves rather than just tristimulus values.

## Coating Formulation by Function

**Primer coatings**: Primers provide adhesion to the substrate and corrosion protection. Metal primers: zinc-rich (galvanic protection), epoxy (barrier protection), or wash primer (etching primer: polyvinyl butyral + phosphoric acid, which etches the metal surface for adhesion). Wood primers: oil-based or acrylic, designed to seal the porous wood surface, raise the grain for sanding, and provide a base for topcoat adhesion. Concrete primer: penetrating sealer (low-viscosity acrylic or epoxy that soaks into the concrete surface, binding dust and providing a sealed substrate).

**Intermediate coats**: Build film thickness and provide the primary barrier against moisture and oxygen penetration. Epoxy mastic (high-build, 200-500 μm in a single coat) for heavy-duty steel protection. Micaceous iron oxide (MIO) pigment reinforces the epoxy barrier: platy MIO particles overlap like roof tiles in the dry film, creating a tortuous path for moisture and oxygen diffusion. MIO-epoxy intermediate coats are the standard for bridge and marine coating systems worldwide.

**Topcoat selection**: Polyurethane topcoats provide UV resistance, color retention, and gloss. Aliphatic polyurethane (HDI biuret or isocyanurate as crosslinker) has excellent weatherability and does not yellow. Aromatic polyurethane is cheaper but yellows and chalks in sunlight (limited to interior use). Fluoropolymer topcoats (PVDF or FEVE resin) provide the ultimate weatherability: 30+ year color and gloss retention. Used on architectural metal panels and stadium roofs. Silicone-acrylic topcoats: heat resistant to 250°C, used on exhaust stacks and boiler casings.

## Surface Preparation Standards

**Abrasive blast cleaning**: The single most important factor in coating performance. ISO 8501-1 defines four blast grades: Sa 1 (light blast, removes loose mill scale and paint), Sa 2 (thorough blast, removes most mill scale and rust), Sa 2.5 (near-white metal, removes all visible mill scale, rust, and coating — the standard for high-performance systems), Sa 3 (white metal, complete removal to bare, uniform metal). Surface profile (anchor pattern): 50-100 μm for zinc-rich primers, measured by replica tape or surface profile comparator. Blast media: steel grit (recyclable, aggressive, produces angular profile), copper slag (disposable, common for field blasting), aluminum oxide (sharp, reusable), garnet (environmentally friendly, low dust).

**Solvent cleaning**: Remove oil, grease, and drawing compounds before blasting (otherwise the blast media spreads contamination). Method: wipe with solvent-soaked rag (mineral spirits or acetone), or steam cleaning with alkaline detergent. Test for cleanliness: water break test (spray water on surface, if it sheets uniformly, surface is clean; if it beads, oil remains). ASTM D4258 covers solvent cleaning practices.

**Concrete surface preparation**: Remove laitance (weak surface layer of fine particles), curing compound, and form release agent. Methods: abrasive blast (shot blast or sand blast), acid etch (10% HCl or muriatic acid, 1:4 dilution with water, applied at 0.1-0.2 L/m², scrubbed, and thoroughly rinsed), or mechanical scarification (rotary milling machine with tungsten carbide teeth). Test for moisture: plastic sheet test (ASTM D4263, tape 460 mm × 460 mm polyethylene to concrete, wait 16 hours, inspect for condensation). Concrete moisture content must be <4% (by weight) before coating application. pH of concrete surface: typically 12-13 (highly alkaline), which can saponify oil-based coatings. Epoxy and acrylic coatings are alkali-resistant and suitable for direct application to concrete.

## Powder Coating Technology

**Powder formulation**: Thermosetting powder coatings contain: resin (epoxy, polyester, or hybrid, 50-60% by weight), curing agent (blocked isocyanate, TGIC, or primid, 3-5%), pigment (TiO₂, iron oxide, carbon black, 20-40%), flow agent (polyacrylate, 0.5-2%), and degassing agent (benzoin, 0.3-0.5%). All components are dry-blended, then extruded at 80-120°C (compounds the mixture, disperses pigment), cooled, crushed, and ground to particle size 10-100 μm (classified by air separation to remove fines <10 μm and coarse >100 μm). The extrusion step is critical: insufficient dispersion causes gel particles that create surface defects.

**Electrostatic application**: Powder is fluidized (suspended in an air stream) and conveyed to a spray gun where a high-voltage electrode (60-100 kV) imparts a negative charge to each particle. The charged particles are attracted to the grounded workpiece, wrapping around edges and reaching recessed areas. Transfer efficiency: 95-99% (overspray collected by a cartridge filter system and reprocessed). Film thickness control: 50-150 μm per pass, controlled by gun-to-part distance (150-250 mm), powder feed rate (100-300 g/min), and line speed. Multi-gun setups (4-16 guns) coat complex shapes uniformly. Faraday cage effect: powder has difficulty penetrating deep recesses (repelled field lines) — this is managed by reducing voltage, using angled nozzles, or triboelectric charging (friction charging instead of corona charging).

**Curing oven**: Convection oven at 180-200°C for 10-20 minutes (metal temperature, not air temperature). Infrared ovens cure faster (3-8 minutes) by direct radiant heating. Induction curing (for flat metal sheets): 1-3 minutes. The curing schedule must be precisely controlled: undercure causes poor chemical resistance and soft film, overcure causes yellowing and reduced flexibility. Cure verification: differential scanning calorimetry (DSC) to confirm >95% cure, or MEK double-rub test (100 rubs with methyl ethyl ketone-soaked cloth, no softening or removal of coating = fully cured).

**Market share**: Powder coating is the fastest-growing coating technology, now representing ~15% of the global industrial coatings market. Key advantage: zero VOC, no hazardous solvent emissions. Limitation: requires substrate that can withstand 150-200°C curing temperature (rules out wood, plastic, and heat-sensitive substrates unless UV-curable powder is used, which cures at 100-120°C with UV radiation).

## Coating Industry Environmental Regulations

**VOC regulations**: Volatile organic compound emissions from coatings are regulated in most developed regions. EU Paints Directive 2004/42/EC sets maximum VOC content by product category: matt interior wall paint 30 g/L, gloss trim paint 100 g/L, intumescent coating 500 g/L, industrial metal primer 250 g/L. US EPA ARCHES rule similarly restricts architectural coatings. These regulations have driven the shift from solvent-borne to water-borne coatings in the architectural segment (water-borne now >80% of architectural market in Europe and North America). Industrial coatings (marine, protective, automotive OEM) have been slower to transition due to performance requirements, but high-solids (VOC <250 g/L) and powder coating alternatives continue to gain market share.

**Heavy metal restrictions**: Lead: banned in consumer paints since the 1970s in most countries (US: 90 ppm limit on dried paint film). Hexavalent chromium (Cr⁶⁺): banned in the EU under REACH for most applications (chromate conversion coatings replaced by trivalent chromium or zirconium/titanium-based alternatives). Cadmium: banned as a pigment in most applications. These restrictions have driven significant reformulation efforts across the coatings industry, with modern corrosion inhibitors (calcium ion exchange pigments, organic zinc phosphate, rare earth salts) replacing legacy chromate chemistry.

**Microplastics concern**: Washed-off paint flakes contribute to microplastic pollution in waterways. The EU is considering restrictions on intentionally added microplastics in coatings and paints under REACH. This affects texture additives (polyethylene beads), certain rheology modifiers, and some polymer dispersions. The industry response includes developing biodegradable polymer alternatives and improving coating durability to reduce flaking and weathering loss.

## Coil Coating Process

**Continuous coil coating**: Metal coils (steel or aluminum, 0.2-2.0 mm thick, 600-1800 mm wide, coil weight 5-25 tonnes) are uncoiled, cleaned, pretreated, coated, cured, and recoiled in a continuous process at line speeds of 20-200 m/min. This is the most efficient method for coating flat metal sheet used in building panels, appliances, and automotive components.

**Pretreatment**: Alkaline cleaning (NaOH-based cleaner at 60-70°C, spray, 15-30 seconds) removes rolling oils and surface contamination. Rinse. Chemical conversion coating: chromate (traditional, being replaced) or zirconium/titanium-based (modern, Cr-free) pretreatment applied by spray or immersion, forming a 20-100 nm conversion layer that improves paint adhesion and corrosion resistance. Rinse with DI water. Dry-off oven at 80-120°C. Total pretreatment time: 30-60 seconds.

**Coating application**: Reverse roll coater applies paint to the top side (precision metering: wet film thickness controlled to ±2 μm). Bottom side coated simultaneously by a second roll coater. Typical coil coat film: primer 5-8 μm dry + topcoat 15-25 μm dry on the exterior side, backer 5-10 μm on the reverse. Paint types: polyester (most common, 10-15 year exterior durability), silicone-modified polyester (15-25 years), PVDF (70/30 PVDF/acrylic, 30+ year color retention), plastisol (PVC organosol, 100-200 μm, for harsh environments). Curing: PMT (peak metal temperature) 216-249°C for 20-60 seconds in a gas-fired convection oven. Line speed determines oven length: at 100 m/min with 30 second cure, the oven must be 50 m long.

## Marine Antifouling Coatings

**Self-polishing copolymer (SPC) technology**: The dominant antifouling mechanism for commercial ship hulls. The binder is a copolymer of tributyltin methacrylate (now banned) or copper acrylate with acrylic backbone. In seawater (pH 8.1), the surface layer of the binder hydrolyzes at a controlled rate (5-10 μm/month), releasing biocidal copper ions and continuously exposing fresh biocide-containing paint. The polishing rate is independent of ship speed within the normal operating range (10-25 knots). Coating thickness: 200-400 μm applied in 3-4 coats. Service life: 3-5 years (60 months) between dry-docking intervals. Tin-free SPC coatings now use copper(I) oxide (Cu₂O, 30-50% by weight) and zinc pyrithione or copper thiocyanate as biocides.

## Automotive OEM Coating Process

**Electrodeposition (E-coat)**: The automotive body is immersed in a bath of water-borne epoxy-amine coating (15-20% solids) at 28-32°C. The body serves as the cathode (or anode, depending on chemistry) with 200-350 V DC applied. Coating deposits by electrophoresis on all surfaces, including recessed areas, box sections, and the inside of rails. Deposition time: 2-3 minutes. Film thickness: 18-25 μm (self-limiting: deposited film is insulating, preventing further deposition). After rinsing, the body is baked at 180-200°C for 20-30 minutes for full cure. E-coat provides complete corrosion coverage and is the universal first coat for automotive bodies worldwide.

The coatings industry continues to evolve toward lower VOC, higher durability, and more sustainable raw materials, driven by regulation and customer demand for longer-lasting, more environmentally responsible products.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Paint not drying | High humidity, low temperature, or missing drier | Ensure ambient >10°C and <80% RH; add cobalt drier (0.05-0.1% metal on resin solids) |
| Coating blistering after application | Moisture on substrate or solvent entrapment | Clean and dry substrate; reduce film thickness per coat; extend flash-off time between coats |
| Poor adhesion (coating peels) | Surface contamination or wrong primer | Degrease with solvent; abrade surface; use appropriate primer for substrate |
| Color mismatch between batches | Pigment dispersion variation | Use standardized pigment dispersions; measure color with spectrophotometer; batch-adjust |
| E-coat film too thin | Low bath voltage or low solids | Increase voltage (200-350 V range); check bath solids (target 18-22%); verify bath temperature |
| Photoresist pattern not resolving | Underexposure, outdated resist, or poor mask contact | Increase exposure dose; check resist shelf life; verify mask-substrate contact |

## See Also

- [Solvents](solvents.md) — solvents for coating formulation
- [Polymers / Natural](../polymers/natural.md) — natural resin binders
- [Metal Finishing](../metals/finishing.md) — surface preparation and coating application
- [Textiles / Dyeing](../textiles/dyeing.md) — related dye chemistry
- [Electronics / Electrical Systems](../electronics/electrical-systems.md) — insulating coatings for wiring
- [Photolithography Resists](../photolithography/resists-masks.md) — photoresist chemistry for semiconductor patterning

[← Back to Chemistry](index.md)
