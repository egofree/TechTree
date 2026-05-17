# Polymers & Composites

> **Node ID**: `polymers`
> **Domain**: [Polymers & Composites](./)
> **Dependencies**: `foundations`
> **Timeline**: Years 5-70+
> **Outputs**: rubber, elastomers, thermoset_resins, thermoplastics, epoxy, ptfe, fr4_laminate, fiberglass, injection_molded_parts

## Problem

Modern civilization runs on polymers. Rubber seals keep fluids where they belong. Epoxy holds structural joints together. Fiberglass panels provide lightweight, corrosion-resistant enclosures. Without synthetic polymers, every seal is leather or metal, every adhesive is animal glue, and every structural panel is wood or sheet metal. [Petrochemicals](../petrochemicals/petroleum-alternatives.md) produces the raw feedstocks: phenol, formaldehyde, ethylene, propylene, styrene, butadiene. This quest converts those feedstocks into elastomers, thermosets, thermoplastics, and composite materials that underpin nearly every downstream technology.

The polymer timeline is forgiving. Natural rubber vulcanization dates to 1839. Bakelite was commercialized in 1909. Polyethylene arrived in the 1930s. None required semiconductor-era precision. The challenge is scaling up reactor vessels, extruder screws, and molding presses using the machine tools already available from the Machine Tools stage.

## Technologies &amp; Systems

### Natural Rubber &amp; Vulcanization

**Latex collection**:
- **Hevea brasiliensis** (tropical): Tap tree by making diagonal cut in bark (1-2 mm deep) with tapping knife. Latex flows from cut into collection cup. Yield: 30-50 g dry rubber per tree per tapping, every 2-3 days. Requires tropical climate.
- **Guayule shrub** (temperate, arid): Harvest entire shrub, crush stems and roots. Extract rubber by flotation — rubber particles float, plant material sinks. Yield: 5-10% dry weight. Native to southwestern North America.
- **Russian dandelion** (temperate, cold): Root contains 5-15% rubber. Harvest roots, grind, extract rubber with solvent or mechanical pressing. Annual crop — faster production cycle than trees or shrubs.

**Coagulation and drying**:
- Add dilute acetic acid or formic acid to latex (pH ~4.5) → emulsion breaks → rubber coagulates as soft crumb. Wash with water to remove acid and proteins. Sheet through two-roll mill (1-2 mm thickness). Air dry in smokehouse (smoke acts as preservative — prevents mold) at 40-60°C for 1-2 weeks → "ribbed smoked sheet" (RSS) grade.

**Mastication** (softening):
- Pass raw rubber through two-roll mill (cast iron rolls, 150-300 mm diameter, adjustable gap, friction ratio 1:1.2 — one roll turns 20% faster than other, creating shearing action). Or use Banbury internal mixer (enclosed chamber with two counter-rotating rotors). Mechanical shearing at 40-80°C breaks polymer chains → reduces molecular weight → softens, increases plasticity. 10-30 minutes milling. Without mastication, raw rubber is too tough to compound.

**Compounding** (mixing in additives):
- On two-roll mill or in Banbury mixer, blend masticated rubber with:
  - **Sulfur** (1.5-3 phr — parts per hundred rubber by weight): Crosslinking agent. More sulfur = harder, less elastic product (ebonite/hard rubber at 30-50 phr).
  - **Accelerators** (0.5-1.5 phr): Mercaptobenzothiazole (MBT) or diphenylguanidine (DPG). Speed up vulcanization, lower cure temperature, improve properties. Without accelerators, vulcanization takes hours at 140°C; with accelerators, minutes at 150°C.
  - **Zinc oxide** (3-5 phr): Activator — works with accelerators.
  - **Stearic acid** (1-2 phr): Co-activator and processing aid.
  - **Carbon black** (20-50 phr): Reinforcing filler. Dramatically increases tensile strength, tear resistance, abrasion resistance. Particle size 20-100 nm. Produced by incomplete combustion of petroleum or natural gas in furnace (furnace black) or channel process. Different grades (N110, N330, N550, N660 — decreasing surface area, decreasing reinforcement).
  - **Antioxidants** (1-2 phr): Amine or phenolic antioxidants prevent oxidative aging (cracking, hardening in sunlight).

**Vulcanization** (curing):
- **Compression molding**: Place compounded rubber blank in heated steel mold. Close mold in hydraulic press (50-200 tonnes, steam-heated or electrically-heated platens at 140-180°C). Pressure 5-20 MPa. Cure time: 5-30 minutes depending on thickness and accelerator system. Open mold, remove cured part. Flash (excess rubber squeezed out at mold parting line) trimmed with knife.
- **Steam autoclave**: For continuous profiles (hose, tubing) — extrude rubber compound through die, then cure in steam autoclave (pressure vessel, 3-10 bar steam, 130-180°C, 30-90 minutes).
- **Properties after cure**: Tensile strength 17-28 MPa (with carbon black reinforcement), elongation at break 400-650%, Shore A hardness 40-90 (depending on sulfur and filler content). Service temperature -50°C to +100°C (degrades above ~120°C).

### Synthetic Rubbers

**Nitrile rubber (NBR, Buna-N)**:
- **Monomers**: Butadiene (C₄H₆, from Petrochemicals petroleum cracking or fermentation) + acrylonitrile (CH₂=CHCN, from propylene ammoxidation: CH₂=CHCH₃ + NH₃ + 1.5O₂ → CH₂=CHCN + 3H₂O over Bi-Mo oxide catalyst at 400-500°C).
- **Polymerization**: Emulsion polymerization in water. Monomers + surfactant (sodium dodecyl sulfate) + free-radical initiator (potassium persulfate, 0.1-0.5%). React at 30-50°C ("cold NBR" — better properties) for 6-12 hours to ~70-80% conversion. Add short-stopping agent (hydroquinone) to terminate. Coagulate with salt/acid → rubber crumb. Wash, dry.
- **Compounding and cure**: Same sulfur vulcanization as natural rubber. 150-180°C, 5-20 minutes.
- **Properties**: Oil and fuel resistance (acrylonitrile content 18-50% — higher = more oil resistant but less flexible at low temperature). Tensile strength 10-25 MPa. THE rubber for fuel hoses, O-rings, oil seals, chemical-resistant gloves.
- **Critical application**: Nitrile gloves for cleanroom (SQ 06) and HF acid handling (SQ 05).

**Neoprene (polychloroprene, CR)**:
- **Monomer**: Chloroprene (CH₂=CCl-CH=CH₂). From butadiene + Cl₂ at ~250°C → dichlorobutene → dehydrochlorination with NaOH → chloroprene.
- **Polymerization**: Emulsion polymerization at 40-50°C, 2-8 hours. Sulfur-modified grades use sulfur co-monomer.
- **Cure**: Metal oxide cure (zinc oxide + magnesium oxide — no sulfur needed). 150-180°C, 5-20 min.
- **Properties**: Moderate oil resistance, excellent weather/ozone resistance, flame retardant (self-extinguishing — chlorine content). Tensile strength 10-25 MPa.
- **Applications**: Wire/cable insulation, conveyor belts, adhesive, gaskets, wetsuits.

**Silicone elastomers**:
- **Precursors**: Silicon metal (from the Silicon stage MG-Si) + methyl chloride (CH₃Cl, from methanol + HCl) → dimethyl dichlorosilane (CH₃)₂SiCl₂ via Rochow-Müller process (Cu catalyst, 250-300°C). Hydrolyze: (CH₃)₂SiCl₂ + 2H₂O → [(CH₃)₂SiO]ₙ + 2HCl. Cyclic and linear siloxanes → polymerize to polydimethylsiloxane (PDMS).
- **Crosslinking**:
  - **Peroxide cure**: Mix PDMS gum with dicumyl peroxide (0.5-2%). Heat to 150-175°C, 5-15 min. Peroxide decomposes to free radicals → crosslink methyl groups. Simple but leaves peroxide decomposition byproducts.
  - **Platinum-catalyzed addition cure**: Vinyl-functional PDMS + Si-H crosslinker + Pt catalyst (~10 ppm). Cures at 100-150°C (or RT for RTV grades). Cleaner, no byproducts. Pt catalyst is expensive but used at very low concentration.
- **Filler**: Fumed silica (10-40 phr) for reinforcement (SiO₂ nanoparticles, 7-40 nm, produced by flame hydrolysis of SiCl₄). Extends tensile strength from ~0.5 MPa (unfilled) to 6-10 MPa.
- **Properties**: Service temperature -60°C to +250°C. Excellent electrical insulation (dielectric constant ~3, dissipation factor ~0.001). Chemically inert. Low toxicity.
- **Applications**: High-temperature seals, medical tubing, mold-making, electronic potting/encapsulation, bake-ware, food-grade tubing.

### Thermosetting Polymers

**Phenol-formaldehyde (Bakelite)** — first synthetic plastic (1909):
- **Novolac route** (two-step): Acid catalyst (HCl or oxalic acid), excess phenol, 80-120°C. Produces thermoplastic novolac prepolymer. Grind to powder. Mix with hexamine hardener (hexamethylenetetramine, from formaldehyde + ammonia) + wood flour filler (50-70% by weight). Compression mold at 150-200°C, 15-30 MPa, 2-10 minutes. Hexamine decomposes → releases formaldehyde → crosslinks novolac → hard, infusible thermoset.
- **Resole route** (one-step): Base catalyst (NaOH or NH₃), excess formaldehyde, 70-90°C. Produces self-curing resole prepolymer. Heat further → crosslinks without added hardener.
- **Properties**: Hard, rigid, excellent electrical insulator (dielectric strength 10-15 kV/mm), heat-resistant to ~200°C, chemically inert to most solvents. Dimensionally stable.
- **Applications**: Electrical insulators, switchgear, distributor caps, molded fittings, handles, early plastic goods. Novolac resins are the basis for positive-tone photoresist binders (Photolithography — the SAME chemistry, just purified to semiconductor grade).

**Epoxy resins**:
- **Synthesis**: Bisphenol-A (from phenol + acetone, acid catalyst) + epichlorohyrin (from propylene + Cl₂ → allyl chloride + HOCl → epichlorohydrin) → diglycidyl ether of bisphenol-A (DGEBA), the workhorse epoxy prepolymer. Viscous liquid.
- **Cure**: Two-part system — mix resin with hardener immediately before use:
  - **Amine hardeners** (diethylenetriamine DETA, triethylenetetramine TETA): Room temperature gel, full cure 24-72 hours at RT or 1-4 hours at 60-80°C. Fast, strong, flexible.
  - **Anhydride hardeners** (methyltetrahydrophthalic anhydride MTHPA): 100-150°C cure, 2-4 hours. Better electrical properties, longer pot life (working time before gel). Preferred for electronics encapsulation.
- **Properties**: High adhesive strength (lap shear 15-30 MPa), excellent chemical resistance, low shrinkage on cure (<2%), excellent electrical insulation.
- **Applications**: Structural adhesive, composite matrix resin (fiberglass, carbon fiber), PCB substrate bonding, die attach adhesive (SQ 06 — silver-filled epoxy), IC encapsulation (SQ 06 — molding compound), protective coatings, potting and encapsulation of electronic components.

**Phenolic/epoxy laminates (FR-4, G-10)**:
- **Process**: Impregnate woven glass fabric (from fiberglass production) or paper with phenolic or epoxy resin solution (prepreg — pre-impregnated). Dry to B-stage (partially cured — still tacky and moldable). Stack layers to desired thickness. Hot-press at 150-170°C under 3-7 MPa for 60-90 minutes. Cool under pressure to prevent warpage. Result: rigid laminate board.
- **G-10**: Epoxy-glass laminate, non-flame-retardant.
- **FR-4**: Brominated epoxy-glass laminate (add tetrabromobisphenol-A to epoxy for flame retardancy — UL 94 V-0 rating). THE standard PCB substrate material.
- **Properties**: Excellent electrical insulation (dielectric constant ~4.5 at 1 MHz), dimensional stability, moisture resistance, flame resistance (FR-4). Mechanical strength.
- **Applications**: PCB substrates (critical for Photolithography+), electrical panels, terminal boards, structural insulating panels.

**Unsaturated polyester resin**:
- **Synthesis**: Propylene glycol + maleic anhydride (unsaturated) + phthalic anhydride (saturated modifier) → condensation polymerization at 200-220°C for 6-12 hours → low-MW polyester prepolymer. Dissolve in styrene monomer (30-40% by weight) as reactive diluent (styrene copolymerizes with unsaturated sites → crosslinks).
- **Cure**: Free-radical polymerization. Add MEKP catalyst (methyl ethyl ketone peroxide, 1-2% by weight) + cobalt naphthenate accelerator (0.1-0.5%). Cures at room temperature (20-30°C). Gel time 20-60 minutes. Full cure 24 hours. Post-cure at 60-80°C improves properties.
- **THE most common fiberglass matrix resin** — cheap, room-temperature cure, easy to work with.

**Polyurethane**:
- **Chemistry**: Diisocyanate (TDI: toluene diisocyanate, or MDI: methylene diphenyl diisocyanate) + polyol (polyether or polyester type). React at room temperature to 80°C.
  - Isocyanate production: Amine + phosgene (COCl₂, from CO + Cl₂) → isocyanate + 2HCl. Phosgene is extremely toxic — production requires sealed equipment, leak detection, full PPE. Non-phosgene routes exist but less mature.
- **Forms**:
  - **Flexible foam**: TDI + polyether polyol + water (blowing agent — generates CO₂). Density 20-60 kg/m³. Cushions, padding, acoustic insulation.
  - **Rigid foam**: MDI + polyester polyol + fluorocarbon/hydrocarbon blowing agent. Density 30-80 kg/m³. Structural insulation panels. Excellent thermal insulation (λ = 0.02-0.03 W/(m·K)).
  - **Elastomers**: Cast or injection molded. Wheels, belts, bushings, wear pads.

### Thermoplastic Polymers

**Polyethylene (PE)**:
- **LDPE** (low-density): Ethylene polymerization at very high pressure (1000-3000 atm, 100-300 MPa) in tubular or autoclave reactor. Peroxide initiator (benzoyl peroxide). 100-300°C. Branched chain structure → flexible, transparent. Melt index 0.2-50 g/10 min (controls viscosity for processing). **Requires extremely robust pressure vessel** — forge-welded or autofrettaged steel tube.
- **HDPE** (high-density): Ethylene + Ziegler-Natta catalyst (TiCl₄ + Al(C₂H₅)₃ on MgCl₂ support). Low pressure (1-20 atm, 0.1-2 MPa). 50-80°C in solvent (hexane) or gas-phase fluidized bed reactor. Linear chain → stiffer, stronger, higher crystallinity, higher melting point (130°C vs. 110°C for LDPE).
- **Processing**: Extrusion (screw pushes molten PE through die → pipe, sheet, film). Blow molding (extrude tube, inflate with air inside mold → bottles, containers). Injection molding (inject melt into steel mold → shaped parts).
- **Properties**: Chemically resistant (most acids, alkalis, solvents), excellent electrical insulator, easy processing, inexpensive. LDPE: flexible films, bags, squeeze bottles, wire insulation. HDPE: rigid containers, pipe, chemical tanks, cutting boards.

**Polyvinyl chloride (PVC)**:
- **Monomer**: Ethylene + Cl₂ → 1,2-dichloroethane (EDC) → pyrolyze at 450-550°C → vinyl chloride monomer (VCM) + HCl. VCM is a carcinogen — closed system handling required.
- **Polymerization**: Suspension process — VCM dispersed as droplets in water with suspending agent (gelatin or PVA). Peroxide initiator (lauroyl peroxide). 40-70°C, 8-12 hours to ~90% conversion. PVC precipitates as porous white granules. Centrifuge, wash, dry.
- **Compounding**: PVC degrades at processing temperature (>150°C) — MUST add heat stabilizers (lead salts, tin compounds, or calcium-zinc systems at 2-5 phr). Without stabilizers, PVC degrades → HCl evolution → autocatalytic degradation → black/brown discoloration, structural failure.
- **Rigid PVC (uPVC)**: No plasticizer. Pipes, fittings, valves, ductwork. Chemical resistant. Tensile strength 40-55 MPa.
- **Flexible PVC**: Add plasticizers (dioctyl phthalate DOP at 20-50 phr) → soft, flexible material. Tubing, wire insulation, flooring, sheet goods, gloves.

**Nylon (polyamide)**:
- **Nylon 6,6**: Adipic acid (from cyclohexane oxidation) + hexamethylenediamine → nylon salt (pH-adjusted aqueous solution). Melt polymerize in autoclave at 250-280°C under nitrogen. Apply vacuum in final stage to remove water and drive molecular weight up.
- **Nylon 6**: Caprolactam ring-opening polymerization at ~260°C, water-initiated. Simpler single-monomer route.
- **Properties**: High tensile strength (70-85 MPa), low friction coefficient, excellent abrasion resistance. Absorbs moisture (affects dimensions — design bearings with moisture allowance).
- **Applications**: Bearings, gears, rope, fishing line, tire cord, engineering components, fasteners, monofilament.

**Polystyrene (PS)**:
- **Polymerization**: Styrene + peroxide initiator (or thermal self-initiation). 80-120°C, bulk (no solvent) or suspension process. Simplest thermoplastic to produce.
- **Crystal PS**: Transparent, rigid, brittle. Good optical clarity. Disposable labware, CD cases, lighting diffusers.
- **Expanded PS (EPS)**: Impregnate PS beads with pentane blowing agent (3-8%). Steam-expand in closed mold at ~100°C. Lightweight insulation foam (λ = 0.03-0.04 W/(m·K)). Packaging, insulation board.

**PTFE (Teflon)**:
- **Precursor chain**: Chloroform + HF (SbF₅ catalyst) → chlorodifluoromethane (R-22). Pyrolyze R-22 at 650-700°C → tetrafluoroethylene (TFE) + HCl. Tight temperature control critical — hexafluoropropylene and perfluoroisobutylene byproducts are extremely toxic.
- **Polymerization**: TFE + persulfate initiator (ammonium persulfate) in aqueous dispersion. 20-80°C. Very high MW achieved rapidly. PTFE is waxy white powder.
- **Processing**: PTFE does NOT melt-flow (melt viscosity ~10¹¹ Pa·s at 380°C). Must sinter: compress powder in mold at 20-35 MPa, then heat to 380°C in controlled cycle (ramp 1-2°C/min, hold 1-4 hours, slow cool). Or paste-extrude with lubricant carrier (petroleum naphtha) → evaporate lubricant → sinter.
- **Properties**: Chemically inert (resists virtually everything including HF, aqua regia). Very low friction coefficient (0.04-0.10 — one of the slipperiest solids). Service temperature -200°C to +260°C. Excellent dielectric (dielectric constant 2.1, dissipation factor <0.0003).
- **Applications**: Chemically inert seals/gaskets, non-stick coatings, wire insulation, bearing surfaces, diaphragm pump membranes, high-frequency electrical insulation.

### Polymer Processing Equipment

**Extruder** (for thermoplastics and rubber):
- **Construction**: Hardened steel barrel (internally ground and polished, 30-150 mm bore × 1-3 m length). Hardened steel screw (single-flighted, L/D ratio 20:1 to 30:1, compression ratio 2:1 to 4:1 — screw channel depth decreases from feed to die). Three zones: feed zone (deep channel, accepts granules), compression zone (channel shallows — melt and compress), metering zone (shallow channel — homogenize and pump at constant rate). Heater bands on barrel (electric resistance heaters, 3-5 zones, each with thermocouple and temperature controller).
- **Operation**: Feed polymer granules into hopper. Screw rotates (50-200 RPM). Granules conveyed forward, heated, melted, compressed, mixed, pumped through die. Die shapes extrudate: tube die, sheet die, film die, profile die. Downstream: cooling (water bath or air cooling), haul-off (rollers pull extrudate at controlled speed), cutting or winding.
- **Capacity**: 5-500 kg/hour depending on screw diameter. the Machine Tools stage can produce the screw (thread milling) and barrel (deep-hole boring).

**Injection molding machine**:
- **Construction**: Two-part system — injection unit (extruder screw that also reciprocates) + clamping unit (hydraulic or mechanical press that opens/closes steel mold). Clamping force: 50-500 tonnes. Shot size: 10-2000 cm³.
- **Operation**: Close mold → clamp under high force. Screw rotates to melt and meter polymer → retracts to accumulate shot. Screw rams forward → inject molten polymer into mold cavity at 50-150 MPa → pack (hold pressure to compensate for shrinkage) → cool (wait for part to solidify, 5-60 seconds depending on thickness) → open mold → eject part. Cycle time: 10-120 seconds.
- **Mold**: Tool steel (hardened), polished cavity surface. Complex geometry possible. Cooling channels for water circulation. Ejector pins to push part out. Gates (small openings where polymer enters cavity) and runners (channels distributing melt to multiple cavities). Mold cost is high (Machine Tools machining required) but amortized over thousands-millions of parts.

**Compression molding press**:
- Hydraulic press (Energy+ hydraulic system) or mechanical toggle press. Heated platens (steam or electric, 150-250°C). 50-200 tonnes clamping force. Place pre-weighed polymer blank or preform in mold cavity. Close press. Heat + pressure → polymer flows to fill cavity → cures (thermosets) or cools (thermoplastics). Open, remove part. Simpler than injection molding for thermosets.

**Calender** (for sheet/film):
- 3-4 hardened steel rolls in stack (200-500 mm diameter × 0.5-2 m wide). Polymer fed between top rolls, passes through successive nip points, exits as thin sheet (0.1-5 mm). Roll gap adjustable. Rolls heated internally (steam or hot oil). For rubber sheet, PVC flooring, PE film.

### Composite Materials

**Fiberglass (glass fiber reinforced polymer, GFRP)**:
- **Glass fiber production**: Melt batch (silica ~60%, limestone ~20%, borax ~10%, alumina, soda ash) at ~1400°C in platinum-rhodium bushing. Draw filaments through bushing tips (5-25 μm diameter, 200-4000 filaments simultaneously). Coat immediately with sizing (silane coupling agent + film former — improves fiber-matrix adhesion and protects fiber surface). Wind on spool. Forms: continuous roving, chopped strand mat (25-50 mm fibers, randomly oriented), woven fabric (plain/twill/satin weave).
  - **E-glass** (electrical grade): Alumino-borosilicate. Most common, cheapest. Tensile strength ~3.5 GPa.
  - **S-glass** (structural): Magnesia-alumina-silicate. ~30% stronger, higher melt temperature. For high-performance applications.
- **Hand layup** (simplest technique): Apply gel coat (pigmented polyester resin) to waxed mold surface. Lay dry fiber mat/fabric on mold. Brush or roll catalyzed polyester resin onto fiber. Roll with consolidation roller to wet out fiber and remove air bubbles. Build up layers to desired thickness (typical laminate: 3-8 layers, 2-6 mm thick). Cure at room temperature (24 hours full cure). Post-cure at 60-80°C for improved properties. Fiber volume fraction: 25-40% by hand layup.
- **Vacuum bagging**: Cover hand-laid laminate with plastic film (nylon or polyethylene). Seal edges. Connect vacuum pump. Evacuate to 0.5-0.9 bar vacuum → atmospheric pressure consolidates laminate → removes air → better fiber-to-resin ratio (40-55% fiber). Better mechanical properties than hand layup alone.
- **Resin transfer molding (RTM)**: Place dry fiber preform in closed two-part mold. Close mold. Inject catalyzed resin under pressure (0.1-0.5 MPa) → resin flows through fiber preform, wetting it. Cure. Open mold, remove part. Better surface finish (both sides smooth), higher repeatability, higher fiber content (50-60%). For medium-volume production.
- **Filament winding**: Continuous fiber roving passed through resin bath, then wound onto rotating mandrel in prescribed pattern (helical, circumferential, polar). Computer-controlled or cam-controlled winding machine. For cylinders, pressure vessels, pipes. Very high fiber content (60-70%), excellent strength in fiber direction.
- **Properties of fiberglass laminate**: Tensile strength 100-300 MPa (depending on fiber type, orientation, and volume fraction). Density 1.5-2.0 g/cm³ (lighter than steel at 7.8, stronger per unit weight). Electrically insulating (glass fibers don't conduct). Corrosion resistant.
- **Applications**: Chemical tanks, pipes, boat hulls, architectural panels, electrical enclosures, vehicle body panels, structural components.

**Carbon fiber** (Silicon+ aspiration):
- **PAN precursor route** (primary): Polyacrylonitrile (PAN) spun into precursor fibers. Stabilize: heat to 200-300°C in air for several hours (prevents melting in next step). Carbonize: heat to 1000-1500°C in N₂ atmosphere (drives off non-carbon atoms → ~95% carbon fiber). Optional graphitize: heat to 2500-3000°C (increases modulus, ~99% carbon). Surface treatment and sizing. Tensile strength 3.5-7.0 GPa. 5× stronger than steel at ¼ the weight. Requires sustained advanced petrochemical industry (acrylonitrile from propylene), controlled-atmosphere furnaces. Well beyond Chemistry-Vacuum Optics stages.

### Polymer Feedstock Chain

[Petrochemicals](../petrochemicals/petroleum-alternatives.md) produces ethylene, propylene, styrene, butadiene, phenol, formaldehyde. This quest starts where Petrochemicals leaves off: monomer in, polymer out. Key intermediate steps:
- Ethylene → LDPE, HDPE, PVC (via EDC → VCM), polystyrene
- Propylene → polypropylene, acrylonitrile (via ammoxidation) → NBR, PAN → carbon fiber
- Butadiene → SBR, NBR, neoprene (via chloroprene)
- Phenol + formaldehyde → Bakelite, epoxy (via bisphenol-A)
- Styrene → polystyrene, polyester resin diluent, SBR
- Chlorosilanes → silicone elastomers

## Integration Points

| Phase/SQ | Contribution |
|----------|-------------|
| Machine Tools | Machine tools for extruder screws, injection molds, compression press platens, two-roll mills |
| Energy | Steam and electric power for reactors, extruders, autoclaves, hydraulic presses |
| Chemistry | Bulk chemicals: sulfuric acid, chlorine, solvents, catalysts; natural rubber vulcanization |
| Vacuum & Optics | Glass fiber production for fiberglass composite; vacuum technology for bagging/degassing |
| Silicon | Silicon metal for silicone elastomers; carbon fiber (aspiration) |
| Photolithography | Photoresist polymers (novolac), IC packaging materials, cleanroom consumables |
| SQ 06 | Specialty gas seals, tubing, consumable containers, nitrile gloves |
| SQ 09 | Fiber reinforcement for composites |
| Lubricants | Mold release agents, processing lubricants |
| Petrochemicals | Monomer feedstocks: ethylene, propylene, phenol, formaldehyde, styrene, butadiene |

## Key Deliverables

- Vulcanized rubber production: gaskets, belts, seals, O-rings, tires
- Nitrile rubber (NBR): oil-resistant seals, chemical gloves, fuel hoses
- Silicone elastomers: high-temperature seals, medical tubing, electronic encapsulation
- Bakelite: electrical insulators, molded components
- Epoxy resins: structural adhesives, composite matrix, die attach, IC encapsulation
- FR-4 laminate: PCB substrates
- Polyester resin + fiberglass hand layup: panels, tanks, enclosures
- Polyethylene: films, containers, pipe, wire insulation
- PVC: rigid pipe, flexible tubing
- PTFE: chemically inert seals, non-stick surfaces
- Nylon: bearings, gears, engineering components
- Injection molding and extrusion capability for thermoplastic parts production
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
