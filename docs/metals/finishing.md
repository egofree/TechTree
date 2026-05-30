# Metal Finishing & Surface Treatment

> **Node ID**: metals.finishing
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`chemistry.acids`](../chemistry/acids.md), [`chemistry.coatings`](../chemistry/coatings.md), [`chemistry.electrolysis`](../chemistry/electrolysis.md), [`metals.non-ferrous`](non-ferrous.md)
> **Enables**: `electrochemistry`
> **Timeline**: Years 15-40
> **Outputs**: galvanized steel, plated parts, anodized aluminum, hardened surfaces, coated components


Metal finishing transforms the surface properties of metals without altering bulk chemistry. A thin surface layer — sometimes only micrometers thick — provides corrosion resistance, wear resistance, electrical conductivity, or decorative appearance that the base metal cannot. The economic importance is enormous: roughly half the steel produced globally receives some form of protective coating, and virtually every electronic device depends on electroplated connectors. Surface treatment processes range from simple acid dips (passivation) to complex electrochemical systems (hard chromium plating) and high-energy thermal processes (plasma spraying).

For a bootstrapping civilization, metal finishing unlocks the longevity of infrastructure. Uncoated carbon steel corrodes at 25-50 µm/year in moderate atmospheres — a 6 mm structural member loses half its cross-section within 30 years. Galvanizing extends service life to 50-100+ years. Case hardening transforms cheap low-carbon steel into gear and bearing surfaces that rival much more expensive alloy tool steels. Anodizing gives aluminum the wear resistance needed for mechanical components. These processes are the difference between infrastructure that lasts generations and infrastructure that rusts away in decades.

## Galvanizing

Galvanizing applies a zinc coating to steel for corrosion protection. Zinc is sacrificial — it has a more negative electrochemical potential than iron (-0.76 V vs. -0.44 V vs. SHE), so even when the coating is scratched and bare steel is exposed, the surrounding zinc corrodes preferentially, providing cathodic protection. A galvanized coating protects steel mechanically (barrier) and electrochemically (sacrificial anode).

**[Hot-dip galvanizing](../glossary/hot-dip-galvanizing.md)** (dominant process, >90% of galvanized steel):
- Steel is cleaned, pickled (HCl to remove mill scale), fluxed (ZnCl₂/NH₄Cl solution at 50-70°C), and immersed in a molten zinc bath at 440-465°C. Immersion time: 10-30 seconds for typical structural sections. Withdrawal rate: 0.5-2.0 m/min (controls coating thickness and drainage).
- The zinc-iron reaction produces a layered metallurgical bond: inner Γ (Fe₃Zn₁₀), δ (FeZn₇), and ζ (FeZn₁₃) intermetallic layers, topped by a layer of nearly pure η-phase zinc. The intermetallic layers are hard but brittle — excessive thickness (from prolonged immersion or reactive steel) leads to spalling.
- Coating thickness: 50-100 µm on typical structural steel. Coating weight: 275-610 g/m² depending on steel composition and bath conditions (ASTM A123 specifies minimum coating weights by steel thickness class).
- Steel composition affects reactivity: silicon and phosphorus promote excessively thick, dark coatings (Sandelin effect, 0.05-0.12% Si range). Steel with >0.25% Si produces thick but adherent coatings. Specifying "galvanizing grade" steel (Si <0.04% or 0.15-0.25%) avoids these problems.
- Bath additives: Aluminum (0.005-0.02%) suppresses ζ-layer growth for thinner, more ductile coatings. Nickel (0.04-0.09%) counteracts the Sandelin effect in reactive steels. Lead or bismuth (0.05-0.1%) improves drainage and spangle formation (being phased out for environmental reasons).

**Electro-galvanizing**:
- Zinc deposited by electrolysis from zinc sulfate or zinc cyanide bath. Current density: 10-40 mA/cm². Coating thickness: 2-20 µm (thinner than hot-dip). Produces a smooth, uniform coating ideal for automotive body panels where surface finish is critical.
- No intermetallic layer — the coating is pure zinc, mechanically bonded. No zinc-iron alloy layer means no spangle pattern and excellent paint adhesion after phosphating.
- Energy consumption: ~3-5 kWh per kg of zinc deposited. Slower and more expensive than hot-dip for heavy coatings, but superior for thin, cosmetic applications.

**Galvanneal**:
- Hot-dip galvanized steel is immediately heated above the zinc melting point (419°C) in an annealing furnace, allowing complete iron-zinc alloying. The entire coating becomes Fe-Zn intermetallic (δ₁ + Γ phases), with no free zinc layer.
- Coating composition: 8-12% Fe, remainder Zn. Surface is matte gray, harder than pure zinc, and has excellent weldability and paint adhesion. Dominates automotive exposed panels.

## Electroplating

Electroplating deposits a thin metallic layer on a substrate by reducing metal cations from solution at the cathode (workpiece). Requires DC power supply, electrolyte bath, anode (soluble or inert), and careful process control. See [Electrolysis](../chemistry/electrolysis.md) for fundamental electrochemistry.

**Core process parameters**:
- **Current density**: 10-500 mA/cm² depending on the metal and bath. Low current density produces fine-grained, dense deposits; high current density increases deposition rate but risks burning (rough, powdery deposits at edges and corners where current density is highest).
- **Efficiency**: Cathode current efficiency varies: Cu (acid copper) ~100%, Ni (Watts bath) ~95%, Cr (hard chrome) only 12-25% (most current goes to H₂ evolution). Low-efficiency processes generate large volumes of hydrogen gas — requires excellent ventilation.
- **Strike plating**: A thin initial layer (0.1-1 µm) deposited from a specialized strike bath at high current density and low metal concentration. Ensures adhesion on difficult substrates (stainless steel, aluminum). Without a strike, the main plated layer may peel. Common: Woods nickel strike (NiCl₂ + HCl, pH <1) for stainless steel; zincate dip + cyanide copper strike for aluminum.

**Zinc plating**: Corrosion protection for fasteners and small parts. Acid zinc (ZnSO₄ + brighteners) or alkaline zinc (Zn(CN)₂ + NaOH, cyanide-based — being replaced by non-cyanide alkaline zincate baths). Thickness: 5-25 µm. Chromate passivation (clear, blue, yellow, olive drab) adds 50-200+ hours salt spray resistance. Hexavalent chromium passivates are being phased out (RoHS) in favor of trivalent chromium.

**Chromium plating**:
- **Decorative chrome**: 0.2-0.8 µm over a nickel underlayer (Cu → Ni → Cr tri-layer). Provides a bright, tarnish-resistant finish on plumbing fixtures, automotive trim, and consumer goods. The chromium layer is microporous or microcracked (controlled by bath chemistry) to distribute corrosion currents evenly, preventing localized pitting.
- **[Hard chrome](../glossary/hard-chrome.md)** (functional): 10-500 µm of chromium deposited from chromic acid bath (CrO₃ 200-300 g/L + H₂SO₄ 2-3 g/L, CrO₃:SO₄ ratio ~100:1). Hardness: 850-1100 HV. Extremely low friction coefficient (0.05-0.12). Used on hydraulic cylinder rods, crankshafts, printing rolls. Cathode efficiency only 12-25% — generates massive hydrogen gas volume. Environmental concern: hexavalent chromium (Cr⁶⁺) is carcinogenic. Replacement technologies (electroless nickel, HVOF tungsten carbide) are growing but hard chrome remains unmatched for some applications.
- Bath temperature: 50-65°C. Current density: 150-500 mA/cm² for hard chrome. Anodes: insoluble lead-tin or lead-antimony alloy.

**[Nickel plating](../glossary/nickel-plating.md)** (Watts bath):
- Bath composition: NiSO₄·6H₂O (250-350 g/L) + NiCl₂·6H₂O (40-60 g/L) + H₃BO₃ (30-45 g/L, buffer) + organic brighteners (saccharin, allyl sulfonate, butynediol). Temperature: 50-65°C, pH 3.5-4.5, current density 20-50 mA/cm².
- Produces a dense, ductile deposit with excellent corrosion resistance. Watts nickel alone is semi-bright; brighteners produce mirror-finish deposits but introduce internal stress. Low-stress formulations use primary + secondary brighteners in balanced ratios.
- Sulfamate nickel bath (Ni(NH₂SO₃)₂) produces very low-stress deposits (20-50 MPa tensile vs. 150-250 MPa for Watts). Used for electroforming and thick builds. Current density up to 100 mA/cm².

**Copper plating**: Acid copper (CuSO₄ + H₂SO₄) for thick deposits and through-hole plating in PCBs. Cyanide copper for strike layers. Copper underlayer improves adhesion and provides a leveling base for nickel-chrome topcoats.

**Tin plating**: For food contact (tinplate), electronics (solderability), and corrosion protection. Acid stannous sulfate or alkaline stannate bath. Thickness: 0.5-15 µm. Tin whiskers (conductive crystalline filaments) are a reliability concern in lead-free electronics — mitigation requires post-bake annealing (150°C, 1 hour) or alloying with 2-3% bismuth.

**Cadmium plating**: Excellent corrosion resistance in marine environments, low contact resistance, galvanic compatibility with aluminum. Historically dominant in aerospace fasteners. Being phased out globally — cadmium is highly toxic (carcinogen, bioaccumulates). Replacements: zinc-nickel alloy (12-15% Ni, 500+ hours salt spray), ion vapor deposition aluminum.

**Gold and silver plating**: Gold for electronics (edge connectors, wire bonding, 0.05-2.5 µm) — excellent conductivity, tarnish resistance, wire bondability. Cyanide-based baths (KAu(CN)₂). Acid gold (pH 3.5-5.0) for hard gold (60-90 HK, 0.1-0.3% Co or Ni). Silver for electrical contacts and RF conductors. Cyanide or non-cyanide (methanesulfonate) baths.

## Electroless Plating

Electroless (autocatalytic) plating deposits metal from solution without external current. The reducing agent (sodium hypophosphite for Ni-P, formaldehyde or glyoxylic acid for Cu) reduces metal ions on the catalyzed surface. The deposit itself catalyzes further deposition — the reaction is autocatalytic and self-sustaining once initiated.

**[Electroless nickel (Ni-P alloy)](../glossary/electroless-nickel-ni-p-alloy.md)** — the most commercially important electroless process:
- Bath: Nickel sulfate (20-30 g/L) + sodium hypophosphite (NaH₂PO₂, 20-30 g/L) + complexing agents (lactic acid, glycolic acid, citrate) + stabilizers (thiourea or lead acetate, ppm levels). Temperature: 85-95°C, pH 4.5-5.0.
- Phosphorus content controlled by bath pH and hypophosphite ratio: low-P (1-4% P), mid-P (5-8% P), high-P (9-13% P). Higher phosphorus → more amorphous structure → better corrosion resistance (especially in high-P, which is non-crystalline and has no grain boundaries for corrosive attack).
- Hardness: 500-700 HV as-plated. Heat treatment at 400°C for 1 hour precipitates Ni₃P (nickel phosphide) particles, raising hardness to 900-1100 HV — comparable to hard chrome.
- Uniformity: The supreme advantage. Coating thickness is uniform on all surfaces — inside holes, on threads, in crevices — because no current distribution issues exist. On complex geometries, electroless nickel achieves ±2-5 µm uniformity where electroplating might vary by 50-200% across the part.
- Applications: Valve bodies, pump internals, oil field equipment (corrosion + wear), memory disks (as-plated smoothness), aerospace components. Replaces hard chrome in many applications for environmental reasons.

**Electroless copper**: Used for metallizing non-conductors (plated-through holes in PCBs, plastic plating). Bath: CuSO₄ + formaldehyde + EDTA + NaOH. Temperature 25-45°C. Thin initial deposits (0.5-2 µm) followed by electroplating for thickness. Requires catalytic surface preparation (SnCl₂/PdCl₂ sensitization/activation).

**Surface preparation for electroless**: The substrate must be catalytically active. Steel and nickel are self-catalytic for electroless nickel. Non-conductors (plastics, ceramics) require etch → sensitize → activate sequence: chromic acid etch (creates micro-roughness), SnCl₂ sensitization, PdCl₂ activation (palladium nuclei serve as catalytic sites). Aluminum requires zincate treatment (double zincate for best adhesion).

## Anodizing

Anodizing converts the aluminum surface to a controlled aluminum oxide (Al₂O₃) layer by electrochemical oxidation. The workpiece is the anode in an electrolytic cell — oxygen generated at the anode reacts with aluminum to form a dense, hard oxide. The resulting coating is integral to the substrate (not deposited), so it cannot peel or chip.

**[Sulfuric acid anodizing](../glossary/sulfuric-acid-anodizing.md)** (Type II, most common):
- Electrolyte: 150-200 g/L H₂SO₄, 15-22°C, 12-22 V DC. Current density: 10-20 mA/cm². Time: 20-60 minutes.
- Coating: 5-30 µm of Al₂O₃ (porous structure — hexagonal cells with central pores). The barrier layer at the metal-coating interface is thin (~10-30 nm per volt of applied potential).
- The porous structure readily absorbs dyes (organic and inorganic) before sealing, producing colored finishes in a wide range of hues. After dyeing, the coating is sealed by immersing in hot water (95-100°C) or nickel acetate solution. Sealing hydrates the Al₂O₃, converting it to boehmite (AlO(OH)), which swells and closes the pores, trapping the dye and sealing the surface.
- Coating hardness: 200-400 HV. Moderate wear and corrosion resistance.

**[Hard anodizing](../glossary/hard-anodizing.md)** (Type III):
- Electrolyte: 150-250 g/L H₂SO₄, -1 to +5°C (refrigerated bath), 25-75 V DC. Current density: 20-40 mA/cm². Time: 30-120 minutes. Low temperature suppresses acid dissolution of the oxide, allowing thicker buildup.
- Coating: 25-100 µm of dense Al₂O₃. Hardness: 400-600 HV (some sources report up to 700 HV on select alloys). The coating is dark gray to bronze/brown depending on alloy and thickness.
- Applications: Wear surfaces (piston heads, cylinder liners, sliding components), architectural hardware, military equipment. Can be precision-ground or lapped after anodizing.
- Alloy effects: 2000-series (Cu-bearing) anodize poorly — soft, dark coatings. 5000/6000-series (Mg/Si) anodize well. 7000-series (Zn) intermediate. Silicon particles in cast alloys appear as dark spots.

**Other anodizing variants**:
- **[Chromic acid](../glossary/chromic-acid.md)** (Type I): 30-50 g/L CrO₃, 40°C, 40-50 V. Thin coating (2-10 µm), excellent for fatigue-critical aerospace parts (minimal stress concentration from the thin, non-porous coating). Also used as a pre-prime treatment for aluminum aircraft skins. Environmental concern: Cr⁶⁺ in bath and rinse water.
- **Oxalic acid**: Used in Japan and Europe for architectural aluminum. Produces a yellowish, hard coating without dyeing. 30-50 µm at 30-60 V.
- **Phosphoric acid**: Used primarily as a surface preparation for adhesive bonding in aerospace (Boeing process). Creates a micro-porous oxide ideal for adhesive mechanical interlocking.

## Phosphating

Phosphating produces an insoluble crystalline phosphate conversion coating on steel, zinc, or aluminum by immersion in a dilute metal phosphate + phosphoric acid solution. The coating forms by chemical reaction with the substrate (no external current). The phosphate crystals are microscopically rough, providing excellent adhesion for paints and oils.

**[Zinc phosphate](../glossary/zinc-phosphate.md)** (most common for steel):
- Bath: ZnO dissolved in H₃PO₄, with accelerators (sodium nitrite, nitrate, or chlorate). Total acid 20-30 points, free acid 2-4 points (titration measurement). Temperature: 40-70°C depending on formulation. Immersion time: 3-10 minutes.
- Reaction: Steel dissolves in phosphoric acid → local pH rises at surface → zinc phosphate precipitates as hopeite (Zn₃(PO₄)₂·4H₂O) crystals on the surface. Crystal size: 2-10 µm. Coating weight: 1-5 g/m² (thin paint base) or 10-30 g/m² (heavy, for oil retention).
- Process sequence: Alkaline clean → water rinse → surface condition (colloidal titanium activator, refines crystal size) → zinc phosphate → water rinse → seal (chromic acid or reactive sealer) or oil. Each step is a separate immersion tank.

**[Manganese phosphate](../glossary/manganese-phosphate.md)** (Parkerizing):
- Bath: MnO or MnCO₃ dissolved in H₃PO₄ + Fe(H₂PO₄)₂. Temperature: 90-98°C (near-boiling). Immersion: 5-20 minutes.
- Produces a dark gray to black coating of hureaulite ((Mn,Fe)₅H₂(PO₄)₄·4H₂O) crystals. Coating weight: 5-30 g/m². Crystal structure is larger and more absorbent than zinc phosphate — retains oil effectively.
- Applications: Gun barrels, engine components, gears, fasteners. The oiled manganese phosphate coating provides excellent corrosion resistance (72-200+ hours salt spray with oil) and anti-galling properties for moving parts. Military specification MIL-DTL-16232.

**Iron phosphate**: Lightest conversion coating (0.2-1 g/m²). Used primarily as a paint base on architectural steel and appliances. Spray or immersion application. Simple chemistry, minimal sludge generation. Not suitable for severe corrosion environments.

## Case Hardening

Case hardening creates a hard, wear-resistant surface layer (the "case") on a ductile, tough core. Low-carbon steel (0.1-0.25% C) is processed so the surface reaches 0.6-1.0% carbon while the core remains at the original low carbon content — after quenching, the surface is hard martensite while the core is soft ferrite/pearlite.

**[Pack carburizing](../glossary/pack-carburizing.md)** (oldest method, still viable for bootstrapping):
- Parts packed in a carbon-rich compound (charcoal + 5-10% BaCO₃ or Na₂CO₃ energizer) in a sealed steel box. Heated to 900-950°C for 4-12 hours. The energizer decomposes to form CO gas, which dissociates at the steel surface (2CO → C[absorbed] + CO₂). Carbon diffuses into the steel surface.
- Case depth: Proportional to √(time). At 925°C, diffusion rate ≈ 0.5 mm/hour^0.5 → 4 hours gives ~1 mm case, 16 hours gives ~2 mm.
- After carburizing, parts are cooled, then re-heated to 800-830°C (above the case's austenitizing temperature but below the core's) and quenched in water or oil. This hardens the case while the core remains relatively soft and tough. Tempering at 150-200°C relieves quenching stress without significant softening.
- Advantages: Simple equipment (furnace + steel boxes + charcoal). No gas supply needed. Suitable for small batches and large parts.
- Disadvantages: Poor carbon control, soot on parts, labor-intensive, slow. Difficult to case-harden selectively (copper plating can mask areas to be kept soft).

**[Gas carburizing](../glossary/gas-carburizing.md)** (modern industrial standard):
- Endothermic gas carrier (N₂ + CO + H₂, from air-methane reaction) enriched with natural gas (CH₄) or propane provides carbon. Furnace temperature: 900-950°C. Carbon potential of the atmosphere is measured and controlled by oxygen probe or dew point, targeting 0.7-0.9% C at the surface.
- Faster than pack carburizing (better gas-solid contact). Easier to control case depth and carbon profile. Can be combined with direct quenching (parts quenched from carburizing temperature without cooling first) for higher throughput.

**Carbonitriding**:
- Carburizing with 1-5% ammonia (NH₃) added to the furnace atmosphere. Nitrogen absorbs into the steel surface alongside carbon. The nitrogen increases hardenability — allows effective case hardening of lower-cost, lower-alloy steels and permits oil quenching instead of water quenching (reduces distortion and cracking).
- Temperature: 800-870°C (lower than pure carburizing). Case depth: 0.05-0.75 mm (typically thinner than carburized cases).
- Applications: Small gears, shafts, fasteners, die components. Provides excellent wear resistance and a degree of improved corrosion resistance from the nitrogen.

**[Nitriding](../glossary/nitriding.md)** (gas nitriding):
- No carbon addition. Nitrogen is absorbed from dissociated ammonia (NH₃ → N + 3/2 H₂) at 500-550°C (below the steel's critical transformation temperature — no quenching required). Nitrogen combines with alloying elements (Cr, Al, Mo, V) to form hard nitride precipitates.
- Case hardness: 900-1200 HV (very hard, harder than carburized and quenched cases). Case depth: 0.1-0.7 mm (diffusion is slow at 500°C — 20-80 hours). A "white layer" (compound layer, Fe₂-₃N iron nitride) forms at the extreme surface: 5-25 µm thick, extremely hard but brittle. Often removed by grinding for precision parts.
- Nitriding steels: Must contain nitride-forming elements — Al (0.8-1.2%), Cr (1-3%), Mo (0.2-0.5%), V. "Nitralloy" steels (e.g., Nitralloy 135M: 1.0% Al, 1.6% Cr, 0.4% Mo) are specifically designed for nitriding.
- Advantages: No quenching → minimal distortion. Superior fatigue life (compressive residual stress in case). Excellent tempering resistance (hardness maintained to ~500°C). Disadvantages: Very slow process, requires special steel.

**Flame and induction hardening**:
- Localized surface hardening without changing chemistry. The surface of a medium- or high-carbon steel part (0.35-0.55% C) is rapidly heated above the austenitizing temperature (830-900°C) by an oxy-acetylene flame or high-frequency induction coil, then immediately quenched.
- Induction hardening: 10-500 kHz frequency (higher frequency → shallower case). Case depth: 0.5-5 mm. Heating time: 0.5-10 seconds. Extremely fast and repeatable — suited for mass production of shafts, gears, and bearing journals.
- Flame hardening: Progressive or spot heating with torch. Lower equipment cost than induction. Used for large parts (machine ways, large gear teeth) where induction coils would be impractical.
- Core properties depend on prior heat treatment — the core is not affected by the brief surface heating. Selective hardening possible by masking or directing the flame/induction to specific areas.

## Passivation

Passivation removes free iron from the surface of stainless steel and promotes the formation of a continuous, transparent chromium oxide (Cr₂O₃) passive film that provides corrosion resistance. Stainless steel self-passivates in air, but surface contamination (embedded iron particles from machining, grinding, or wire brushing) disrupts the passive film and initiates localized rusting. Passivation dissolves these contaminants.

**[Nitric acid passivation](../glossary/nitric-acid-passivation.md)** (traditional, ASTM A967):
- Immersion in 20-45% HNO₃ at 20-50°C for 15-60 minutes depending on grade. Nitric acid is an oxidizing acid — it dissolves free iron and iron oxides while passivating the chromium-rich surface. Rinse thoroughly in clean water.
- Type-specific treatments: Austenitic grades (304, 316) respond well to 20-25% HNO₃ at 20-40°C. Martensitic and ferritic grades (410, 430) require 20-45% HNO₃ at 50-60°C (higher free iron content, more aggressive treatment needed).
- ASTM A967 defines five passivation methods (nitric acid in various concentrations, nitric acid + sodium dichromate, and citric acid). Acceptance criteria: water immersion test, high-humidity test, salt spray test, or copper sulfate test (no copper plating on surface = pass).

**[Citric acid passivation](../glossary/citric-acid-passivation.md)** (modern alternative):
- 4-10% citric acid at 40-60°C for 15-30 minutes. Safer than nitric acid (non-oxidizing, biodegradable, lower fume hazard). Increasingly specified in aerospace and medical device industries (ASTM A967 Citric 1-5 methods).
- Removes free iron by chelation — citric acid binds Fe²⁺/Fe³⁺ ions. Does not attack the chromium oxide passive layer. Effective on all stainless grades.

**[Electropolishing](../glossary/electropolishing.md)** (ultimate passivation):
- The workpiece is the anode in a concentrated H₂SO₄ + H₃PO₄ electrolyte at 50-70°C. Controlled dissolution removes a thin layer (5-40 µm) of the surface, preferentially attacking peaks (micro-polishing) and enriching the surface in chromium (Cr dissolves slower than Fe in the electropolishing electrolyte). The result: a smooth, chromium-enriched, exceptionally passive surface.
- Used where both surface finish and maximum corrosion resistance are required: pharmaceutical equipment ( sanitary tubing), semiconductor process chambers, food processing equipment, and medical implants.

## Thermal Spraying

Thermal spraying deposits molten or semi-molten material onto a surface by propelling heated particles at high velocity. The particles impact, flatten ("splat"), and bond mechanically (and sometimes metallurgically) to the substrate. The coating is built up by overlapping splats — lamellar structure with some porosity (1-15% depending on process).

**Wire arc spraying**:
- Two consumable metal wires (the coating material) are fed to meet at a point where a DC arc (20-40 V, 100-300 A) melts the wire tips. Compressed air (or inert gas) atomizes and propels the molten droplets at 100-200 m/s onto the substrate.
- Deposition rate: 5-25 kg/hour. Coating thickness: 50-500 µm. Bond strength: 20-40 MPa.
- Primary application: Zinc and aluminum coatings on bridges, offshore structures, and water tanks (corrosion protection). Zn-Al 15/85 alloy combines sacrificial protection (zinc) with durability (aluminum).
- Substrate temperature remains low (<150°C) — no distortion or metallurgical damage. Surface preparation: grit blasting to Sa 2½-3 (near-white to white metal blast, 50-100 µm anchor profile).

**Flame spraying**:
- Oxy-acetylene or oxy-propane flame melts powder or wire feedstock. Combustion gas stream carries particles to the substrate. Lower particle velocity (50-100 m/s) than other methods → higher porosity, lower bond strength.
- Simple, portable, low equipment cost. Used for repair builds (shaft repair with steel or bronze), corrosion barriers, and ceramic coatings where high performance is not required.

**High-velocity oxy-fuel (HVOF)**:
- Fuel (kerosene, propane, hydrogen, or natural gas) and oxygen combust in a high-pressure chamber (0.3-1.0 MPa). The combustion gas stream accelerates through a de Laval nozzle to supersonic velocities (600-1000 m/s). Powder injected into the stream is heated and propelled at extreme velocity.
- Particle velocity > gas temperature in importance. High impact velocity → dense coatings (porosity <1%), high bond strength (>70 MPa), low oxide content. Coating properties approach wrought material.
- Key applications: Tungsten carbide-cobalt (WC-Co, 83-17% or 86-10% with 4% Cr) wear coatings — hardness 1000-1300 HV, used on turbine blades, valve stems, pump seals, and printing rolls. Chromium carbide-nickel chromium (Cr₃C₂-NiCr) for high-temperature wear (up to 900°C). Stellite and Inconel for corrosion-erosion resistance.
- Replaces hard chrome plating in many applications — no Cr⁶⁺, often superior coating properties.

**Plasma spraying**:
- DC arc (100-200 V, 300-800 A) between a tungsten cathode and copper anode ionizes argon or nitrogen gas into a plasma jet (10,000-15,000°C). Powder injected into the plasma melts instantly and is propelled at 200-400 m/s to the substrate.
- The only thermal spray process that can fully melt ceramics (melting points >2500°C). Primary application: **[Thermal barrier coatings (TBCs)](../glossary/thermal-barrier-coatings-tbcs.md)** — yttria-stabilized zirconia (YSZ, ZrO₂-8%Y₂O₃) on gas turbine blades and combustion liners. TBC thickness: 100-500 µm. Temperature drop across TBC: 100-300°C, allowing higher operating temperatures and improved efficiency.
- Bond coat: MCrAlY (M = Ni, Co, or NiCo) applied by plasma or HVOF before the YSZ topcoat. The bond coat provides oxidation/corrosion resistance and a rough surface for mechanical bonding of the ceramic. A thermally grown oxide (TGO, α-Al₂O₃) forms at the bond coat-topcoat interface during service — TGO growth is the ultimate life-limiting mechanism for TBCs.

## Pickling and Descaling

Pickling removes oxide scale (mill scale, heat tint, welding discoloration) from metal surfaces by chemical dissolution in acid. Descaling may refer to mechanical removal (shot blasting) or chemical (acid pickling). Pickling is a surface preparation step preceding galvanizing, plating, passivation, or welding.

**Carbon steel pickling**:
- **[Hydrochloric acid](../glossary/hydrochloric-acid.md)** (most common): 10-20% HCl at 20-40°C. Dissolves FeO, Fe₃O₄, and Fe₂O₃ mill scale. Fast action (5-15 minutes immersion for typical scale). Acid consumption: 30-50 kg HCl per tonne of steel. Fumes: HCl vapor — requires acid-resistant ventilation (PVC or FRP ductwork, scrubber).
- **[Sulfuric acid](../glossary/sulfuric-acid.md)** (older process): 5-15% H₂SO₄ at 50-80°C. Slower than HCl, requires heating. Lower fuming (H₂SO₄ has lower vapor pressure). Leaves iron sulfate scale on parts if not thoroughly rinsed. Largely replaced by HCl in continuous strip lines but still used for batch pickling.
- Hydrogen embrittlement risk: Acid pickling generates hydrogen at the steel surface (Fe + 2HCl → FeCl₂ + H₂). Atomic hydrogen can diffuse into the steel, causing embrittlement in high-strength steels (yield strength >1000 MPa). Baking at 150-200°C for 4-24 hours within 1 hour of pickling drives out absorbed hydrogen.
- Inhibitors: Added to pickling acid (0.1-0.5% organic inhibitors such as urotropine, thiourea derivatives) to reduce base metal attack after scale removal, reducing hydrogen generation and acid consumption.

**Stainless steel and titanium pickling**:
- **[Mixed acid](../glossary/mixed-acid.md)** (HF + HNO₃): The standard pickle for stainless steel. Typical bath: 8-15% HNO₃ + 1-5% HF at 20-50°C. Nitric acid dissolves iron and chromium oxides; hydrofluoric acid dissolves silicon oxides and complex chromium oxides. Immersion: 10-30 minutes. Produces a uniform, white, pickled finish.
- **Safety**: Hydrofluoric acid is extremely hazardous — penetrates skin rapidly, binds calcium and magnesium in tissue, causes deep tissue necrosis and potentially fatal systemic fluoride poisoning. Calcium gluconate gel must be available at every HF workstation. Full protective equipment: acid-resistant gloves (Neoprene or Nitrile over natural rubber), face shield, acid suit, and emergency shower.
- Titanium pickling: Similar HF + HNO₃ mixture, but higher HNO₃ (20-40%) to maintain a passive surface during pickling. Pure HF attacks titanium aggressively and generates hydrogen (embrittlement risk). The high HNO₃ ratio keeps the surface passivated while HF removes the oxide scale selectively.

**Fume control and waste treatment**:
- Pickling generates acid mist and hydrogen gas. Enclosed tanks with lip exhaust ventilation (15-20 m³/s per m² of tank surface) capture fumes. Scrubbers (packed tower with NaOH or Ca(OH)₂ solution) neutralize exhaust gases.
- Spent pickle liquor contains dissolved metals (Fe²⁺, Cr³⁺, Ni²⁺) and free acid. Treatment: neutralize with lime (Ca(OH)₂) to precipitate metal hydroxides, filter the sludge for landfill disposal. Acid recovery possible by crystallizing FeCl₂·4H₂O from HCl pickle liquor (Ruthner process: spray roasting — FeCl₂ + H₂O + O₂ → Fe₂O₃ + HCl, regenerated acid recycled).

## Metal Painting Considerations

Paint is the most widely used protective coating for metals, but paint performance depends critically on surface preparation and primer selection. Poor preparation is responsible for 80-90% of premature paint failures on metal structures.

**Surface preparation**:
- Abrasive blast cleaning to Sa 2½ (near-white metal, ISO 8501-1) is the standard for structural steel. Angular grit (steel grit, copper slag, aluminum oxide) at 0.4-0.7 MPa creates an anchor profile (surface roughness) of 50-100 µm for mechanical adhesion. Sa 3 (white metal blast) required for metallic spray coatings and immersion service.
- Hand and power tool cleaning (St 2/St 3) acceptable only for mild environments and maintenance painting. Never paint over mill scale — it will eventually spall, taking the paint with it.

**Primer systems**:
- **Zinc-rich primers**: Organic (epoxy binder) or inorganic (ethyl silicate binder) primers loaded with 75-90% metallic zinc dust by weight in the dry film. Provide galvanic (sacrificial) protection at scratches and damaged areas — the zinc particles are in electrical contact with each other and the steel substrate. Inorganic zinc silicate (IOZ) primers can standalone as a single-coat system for structural steel in moderate environments (50-100 µm dry film thickness, 15+ year life in rural/industrial atmospheres).
- **Epoxy primers**: Two-component (epoxy resin + polyamide or amine hardener). Excellent adhesion, chemical resistance, and barrier properties. Not UV-resistant — chalk on exposure. Used as intermediate/build coats under aliphatic polyurethane or acrylic topcoats.
- **Galvanized steel priming**: New galvanizing has a smooth, non-porous zinc surface that most paints will not adhere to. Weathering (3-6 months outdoor exposure) creates a natural zinc carbonate patina that improves adhesion. For immediate painting: wash primer (acid-based etching primer, vinyl butyral + H₃PO₄) or acrylic etch primer to promote adhesion.

**Coating systems for steel structures**:
- Moderate environments: IOZ primer (50-75 µm) + epoxy intermediate (100-150 µm) + polyurethane topcoat (50-75 µm) = 200-300 µm total. Service life: 15-25 years to first maintenance.
- Severe marine/industrial: IOZ primer + two epoxy intermediate coats + polysiloxane or fluoropolymer topcoat = 350-500 µm total. Service life: 25-40+ years.

## Safety & Hazards

**Acid handling** (pickling, passivation, anodizing):
- HCl, H₂SO₄, HNO₃, and HF require full acid-resistant PPE (face shield, chemical suit, gauntlet gloves, rubber boots). Emergency shower and eyewash within 10 seconds travel. HF-specific: calcium gluconate gel at every workstation — apply immediately to any skin contact, seek emergency medical attention even if pain is initially minimal.
- Acid baths generate hydrogen gas — no smoking, open flames, or spark-producing tools near pickling operations. Ventilation must prevent hydrogen accumulation above 1% (25% of LEL).

**Hexavalent chromium** (Cr⁶⁺):
- Present in chromic acid anodizing baths, hard chrome plating baths, and chromate conversion coatings. Confirmed human carcinogen (lung cancer) by inhalation of mists and dusts. Stringent exposure limits: OSHA PEL 5 µg/m³ (8-hour TWA). Engineering controls: tank enclosure, mist suppressants, local exhaust ventilation. Medical surveillance for exposed workers.
- Replacement with Cr³⁺ passivates, trivalent chromium plating (not yet equivalent to hard chrome), and non-chromium alternatives is an active industry priority driven by REACH, RoHS, and OSHA regulations.

**Cyanide** (electroplating baths):
- Cadmium cyanide, copper cyanide, zinc cyanide, and silver cyanide baths contain free cyanide (NaCN or KCN, 5-50 g/L). Fatal if ingested, inhaled as mist, or absorbed through skin. Cyanide acidification (mixing cyanide waste with acid) releases HCN gas — lethal at 100-200 ppm. Never store cyanide and acid in the same area. Cyanide destruction: alkaline chlorination (NaOCl + CN⁻ → OCN⁻ → CO₂ + N₂) before discharge.

**Thermal spray operations**:
- UV radiation from arc and plasma processes — face shield with appropriate shade (Shade 3-6 for arc spray, Shade 9-12 for plasma). Noise levels: 100-130 dB — hearing protection mandatory. Metal fume (zinc, chromium, nickel) — respiratory protection and fume extraction. Dust explosion risk from dry powder handling — housekeeping and explosion-proof equipment in powder rooms.

**General metal finishing hazards**:
- Heavy metal exposure: Cd, Cr⁶⁺, Ni, Pb, and Hg compounds are regulated carcinogens or systemic toxins. Engineering controls (enclosed processes, ventilation) preferred over PPE. Biological monitoring (blood/urine testing) for workers in high-exposure areas.
- Wastewater treatment: Plating and finishing shops generate wastewater containing heavy metals, cyanide, acids, and organic compounds. Treatment: cyanide destruction → chromium reduction (Cr⁶⁺ → Cr³⁺ by NaHSO₃ at pH 2-3) → metal hydroxide precipitation (lime or NaOH at pH 8-10) → settling/filtration → discharge to meet local effluent standards (typically <0.5 mg/L for Cr, Ni, Cu; <0.1 mg/L for Cd).


## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Hot-dip galvanized coating is dark, thick, and spalling | Steel has 0.05–0.12% Si (Sandelin effect) causing excessive Fe-Zn intermetallic growth | Specify galvanizing-grade steel (Si <0.04% or 0.15–0.25%); add 0.04–0.09% Ni to bath to counteract Sandelin reactivity |
| Hard chrome plating has rough, burned deposits at edges | Current density too high at part edges (>500 mA/cm²) causing powdery, non-adherent deposition | Use shields or robbers to distribute current; target 150–500 mA/cm² uniformly; verify bath at 50–65°C, CrO₃:SO₄ ratio ~100:1 |
| Electroless nickel thickness varies >10% on complex geometry | Bath agitation insufficient or temperature gradient >3°C across part | Increase bath agitation; verify uniform heating at 85–95°C ±1°C; electroless Ni should inherently achieve ±2–5 µm uniformity |
| Type II anodized coating fails salt spray test at <200 hours | Coating not sealed — porous Al₂O₃ structure remains open to corrosive ingress | Seal in hot DI water (95–100°C) or nickel acetate for 15–30 minutes to hydrate Al₂O₃ to boehmite (AlO(OH)), closing pores |
| Zinc phosphate coating weight <1 g/m² (too thin for paint base) | Free acid too high (wrong acid ratio) or bath temperature below 40°C | Titrate bath: adjust total acid to 20–30 points, free acid to 2–4 points; raise temperature to 40–70°C per formulation |
| Pack carburized case depth <0.5 mm after 4 hours at 925°C | Steel boxes not sealed (CO escaping) or BaCO₃ energizer depleted — insufficient carbon potential | Seal boxes with clay; refresh BaCO₃ energizer to 5–10% of pack; at 925°C, expect ~0.5 mm per √(hours) |
| Pickled high-strength steel bolts (yield >1000 MPa) crack in service | Hydrogen embrittlement from atomic hydrogen generated during acid pickling (Fe + 2HCl → FeCl₂ + H₂) | Add inhibitor (0.1–0.5% urotropine) to pickling acid; bake at 150–200°C for 4–24 hours within 1 hour of pickling to drive out hydrogen |
| Paint delaminates from structural steel within 2 years | Surface not blasted to Sa 2½ — mill scale or rust under paint (responsible for 80–90% of premature failures) | Reblast to Sa 2½ (near-white metal, ISO 8501-1) with 50–100 µm anchor profile; apply IOZ primer within 4 hours of blasting |
| Copper sulfate passivation test shows Cu plating on 304 stainless | Free iron particles embedded from grinding or wire brushing with carbon steel tools | Re-passivate in 20–25% HNO₃ at 20–40°C for 30 minutes; avoid carbon steel tools that contaminate stainless surfaces |
| HVOF tungsten carbide coating shows >2% porosity (should be <1%) | Spray stand-off distance too far or fuel pressure too low — particle velocity below 600 m/s | Reduce stand-off to 150–250 mm; verify fuel pressure at 0.3–1.0 MPa for supersonic gas velocity (600–1000 m/s) |

## See Also

- [Acids](../chemistry/acids.md) — pickling and etching solutions
- [Coatings](../chemistry/coatings.md) — paint, lacquer, and protective finishes
- [Electrolysis](../chemistry/electrolysis.md) — electroplating fundamentals
- [Non-Ferrous Metals](non-ferrous.md) — base metals for plating and coating
- [Metal Forming](forming.md) — shaping metal before finishing
- [Aluminum](aluminum.md) — anodizing and aluminum surface treatment
- [Electroplating](../electrochemistry/electroplating.md) — electrodeposition of metal coatings

[← Back to Metals](index.md)
