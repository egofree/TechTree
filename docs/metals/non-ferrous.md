# Non-Ferrous Metal Production

> **Node ID**: metals.non-ferrous
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`chemistry.acids`](../chemistry/acids.md), [`metals.copper-bronze`](copper-bronze.md), `mining`
> **Enables**: [`chemistry.soap`](../chemistry/soap.md), [`metals.alloys`](alloys.md), [`metals.finishing`](finishing.md), [`metals.precious-metals`](precious-metals.md)
> **Timeline**: Years 15-40
> **Outputs**: zinc, lead, tin, nickel, magnesium, titanium sponge

### Overview

Beyond iron and copper lies a family of metals whose properties — low melting points, corrosion resistance, extreme lightness, or exceptional strength-to-weight ratios — fill niches that steel and copper cannot. Zinc protects steel from rust. Lead stores energy in batteries. Tin enables solder. Nickel stabilizes stainless steel. Magnesium offers the lightest structural frame. Titanium survives where nothing else will. Each demands its own extraction chemistry, often more complex than iron or copper smelting.

These six non-ferrous metals collectively enable galvanizing, battery storage, electronics assembly, alloying, lightweight structures, and aerospace applications. Their production represents a significant step up in industrial complexity from [Copper & Bronze](copper-bronze.md) and [Iron & Steel](iron-steel.md), requiring controlled atmospheres, vacuum processes, and in some cases electrochemistry.

### Zinc

Zinc is the fourth most consumed metal worldwide (after iron, aluminum, and copper). Its primary use — galvanizing steel — consumes ~50% of production. Zinc melts at 420°C and boils at 907°C, a remarkably narrow liquid range that complicates smelting because metallic zinc vaporizes before it can be collected as a liquid by traditional methods.

**Ores**:
- **[Sphalerite](../glossary/sphalerite.md)** (ZnS, zinc blende): The dominant ore (~95% of primary production). Often found with galena (PbS) in hydrothermal veins. Color varies from yellow-brown to black depending on iron content — high-iron varieties are called "marmatite." Typical ore grade: 3-12% Zn.
- **[Smithsonite](../glossary/smithsonite.md)** (ZnCO₃) and **[hemimorphite](../glossary/hemimorphite.md)** (Zn₄Si₂O₇(OH)₂·H₂O): Oxide/carbonate ores, historically important ("calamine"), now largely depleted. Easier to reduce than sulfides but rare in economic concentrations.
- **Beneficiation**: Flotation is the standard method. Crush ore to ~150 μm, separate ZnS from PbS and FeS₂ using sequential flotation with copper sulfate activator, xanthate collector, and lime pH modifier. Concentrate grade: 50-60% Zn.

**[Pyrometallurgical extraction](../glossary/pyrometallurgical-extraction.md)** (Imperial Smelting Process):
- **Roast**: ZnS + 1.5O₂ → ZnO + SO₂ at 900-1000°C in fluidized-bed roasters. SO₂ is captured for sulfuric acid production (see [Mineral Acids](../chemistry/acids.md)). The "dead-roasted" calcine is >98% ZnO.
- **Reduction**: ZnO + CO → Zn(g) + CO₂ at 1000-1100°C. The Imperial Smelting Furnace (ISF) is a blast furnace charged with sintered ZnO calcine and preheated coke. Air blast at 1000°C. Zinc vapor exits the top and is shock-condensed in a lead splash condenser at 450-500°C — molten lead droplets absorb zinc vapor, preventing re-oxidation. The lead-zinc liquid is cooled to 440°C; zinc (immiscible, lighter) separates and is decanted.
- **ISF yield**: ~90% recovery. Simultaneously produces lead from co-smelted PbO. The process is energy-intensive (coke rate: 0.8-1.0 t coke per t Zn+Pb) and largely superseded by electrolytic zinc.

**[Electrolytic extraction](../glossary/electrolytic-extraction.md)** (roast-leach-electrowin, ~80% of production):
- **Roast**: ZnS → ZnO (as above).
- **Leach**: ZnO + H₂SO₄ → ZnSO₄ + H₂O. Neutral leach at pH 5.0-5.2 precipitates iron as jarosite (NaFe₃(SO₄)₂(OH)₆), goethite (FeOOH), or hematite (Fe₂O₃) — the choice of iron removal route is the major process design decision. Purify by cementation: add zinc dust to precipitate Cu, Cd, Co, Ni impurities.
- **Electrowinning**: Electrolyze purified ZnSO₄ solution at 30-38°C, 400-600 A/m², cell voltage 3.0-3.5 V. Aluminum cathodes, lead-silver anodes. Zn²⁺ + 2e⁻ → Zn deposits on cathode, stripped mechanically every 24-48 hours. Energy: 3.0-3.5 MWh per tonne Zn.
- **Product**: 99.99%+ pure zinc (SHG — Special High Grade). Current efficiency: 88-93%.

**Properties**:
- Density: 7.13 g/cm³. Melting point: 419.5°C. Boiling point: 907°C.
- Crystal structure: hexagonal close-packed (HCP). Moderately ductile above 100°C; brittle at room temperature if impure.
- Electrochemical: Standard electrode potential -0.76 V (vs. SHE) — more negative (anodic) than iron (-0.44 V), enabling sacrificial cathodic protection (galvanizing).

**Applications**:
- **[Galvanizing](../glossary/galvanizing.md)** (50%): Hot-dip zinc coating on steel (see [Iron & Steel](iron-steel.md)). Coating thickness 45-85 μm. Atmospheric corrosion protection: 20-100+ years depending on environment.
- **[Die-casting alloys](../glossary/die-casting-alloys.md)** (15%): Zamak (Zn-4Al-1Cu-0.05Mg). Melts at 380°C, excellent fluidity, dimensional accuracy ±0.05 mm. Used for automotive components, hardware, toys. Limited to <150°C service temperature.
- **[Brass](../glossary/brass.md)** (15%): Cu-Zn alloy (see [Copper & Bronze](copper-bronze.md)). Zinc as alloying element.
- **Sacrificial anodes**: Zinc blocks bolted to ship hulls, pipelines, storage tanks. Preferentially corrode, protecting the steel structure.

### Lead

Lead is the densest common metal (11.34 g/cm³), extraordinarily malleable, and resistant to sulfuric acid. Its toxicity has driven substitution in many applications, but batteries remain irreplaceable. Lead is the most recycled metal on Earth (>95% recycling rate for batteries in developed countries) — more lead is produced from recycling than from mining.

**Ores**:
- **[Galena](../glossary/galena.md)** (PbS): The primary ore. Lead-gray metallic luster, cubic cleavage. Often carries silver (0.01-0.5% Ag) — historically the main source of silver. Ore grade: 3-8% Pb in vein deposits; lower in Mississippi Valley-type deposits.
- **[Cerussite](../glossary/cerussite.md)** (PbCO₃) and **[anglesite](../glossary/anglesite.md)** (PbSO₄): Oxidation-zone minerals, secondary after galena.
- **Beneficiation**: Flotation to produce 60-75% Pb concentrate. Crush to 75-150 μm, xanthate collector, cyanide to depress iron sulfides.

**Smelting and refining**:
- **[Sintering and blast furnace](../glossary/sintering-and-blast-furnace.md)** (traditional): PbS concentrate is sintered on a Dwight-Lloyd sinter machine — roasted to PbO while agglomerating fines into porous lumps. Sinter + coke + fluxes (limestone, silica) charged into a blast furnace. PbO + CO → Pb + CO₂ at 1000-1200°C. Molten lead (Tm 327°C) collects in the hearth. Lead bullion: 95-98% Pb with Cu, Sn, As, Sb, Ag, Au impurities.
- **[Direct smelting](../glossary/direct-smelting.md)** (modern, ISASMELT/KIVCET): Oxygen-enriched smelting in a single vessel. Higher SO₂ capture (>95%), lower energy, less plant footprint. Replacing traditional sinter-blast furnace plants.
- **Refining**: Crude lead is refined by:
  - **Copper drossing**: Melt at 450-500°C, cool slowly. Copper separates as dross (skimmed off). Removes Cu to <0.005%.
  - **Softening**: Air or oxygen blown through molten lead at 600-700°C. As, Sb, Sn oxidize preferentially and skimmed as "speiss" and "matte."
  - **Parkes process (desilverization)**: Add zinc at 450-480°C. Silver (and gold) dissolve preferentially in zinc, which is immiscible in lead. Zinc-silver crust floats and is skimmed. Zinc is distilled off under vacuum; silver is refined electrolytically. Recovers >98% of silver.
  - **Betts electrolytic refining**: Anodes of lead bullion cast after softening. Electrolyte: lead fluosilicate (PbSiF₆) + H₂SiF₆. Pure lead deposits on cathode. Product: 99.99% Pb.

**Properties**:
- Density: 11.34 g/cm³. Melting point: 327.5°C. Boiling point: 1749°C.
- Extremely malleable — can be rolled to 0.1 mm foil by hand. Poor tensile strength (~12 MPa as cast).
- Corrosion resistance: Resists sulfuric acid, phosphoric acid, and many atmospheres. Forms protective PbSO₄/PbCO₃ layer.
- Toxic: Cumulative poison. Affects nervous system, kidneys, blood. Blood lead level threshold: 5 μg/dL (children).

**Applications**:
- **[Lead-acid batteries](../glossary/lead-acid-batteries.md)** (85% of consumption): Grids and active material (PbO₂ cathode, Pb sponge anode, H₂SO₄ electrolyte). See [Electrical Systems](../energy/electricity.md). Energy density: 30-40 Wh/kg. Cheap, reliable, >99% recycling rate.
- **Radiation shielding**: X-ray rooms, nuclear shielding. High density and atomic number (82) absorb gamma and X-ray radiation. 2 mm Pb ≈ 1 HVL (half-value layer) for 100 keV X-rays.
- **Ammunition**: Shot and bullets. High density gives short range but high kinetic energy delivery.
- **Sound insulation and vibration damping**: Lead sheet laminated in walls. High internal damping.

### Tin

Tin has been used since the Bronze Age — bronze is Cu-Sn alloy (see [Copper & Bronze](copper-bronze.md)). Pure tin is soft and ductile with a low melting point, making it essential for solder, tinplate, and bearing alloys. Global production is small (~300,000 tonnes/year) but strategically critical for electronics.

**Ores**:
- **[Cassiterite](../glossary/cassiterite.md)** (SnO₂): The only economically important tin mineral. Black to brown, very high specific gravity (6.8-7.1). Placer deposits (stream tin) were the historical source — mined by panning and sluicing. Hard-rock veins in Bolivia, Indonesia. Ore grade: 0.5-2% Sn in hard rock; 0.01-0.1% in placers.
- **Beneficiation**: Gravity separation (jigs, shaking tables, spiral concentrators) exploits the high density of cassiterite. No effective flotation — cassiterite is not easily floated. Magnetic separation removes ilmenite and magnetite. Concentrate: 60-75% Sn.

**Extraction and refining**:
- **Reduction smelting**: SnO₂ + 2C → Sn + 2CO at 1200-1300°C in a reverberatory or electric furnace. Two-stage smelting is common: first stage produces impure tin (95-99% Sn) with a high-tin slag; second stage re-smelts the slag at higher temperature with more carbon and flux (limestone) to recover remaining tin, producing a low-grade tin and a discard slag.
- **Refining**: Fire refining (liquation, boiling, tossing) removes Fe, Cu, As, Sb. Liquation: heat to 230-250°C (just above tin MP). Tin melts and drains away from higher-melting impurities. Electrolytic refining (for high purity): acidic stannous sulfate electrolyte or alkaline stannate bath. Product: 99.9-99.99% Sn.
- **Recovery**: Tin from tinplate scrap by chlorination (Sn + 2HCl → SnCl₂ + H₂) or electrolytic detinning. Over 30% of tin comes from recycling.

**Properties**:
- Density: 7.26 g/cm³. Melting point: 231.9°C — low enough to melt on a kitchen stove.
- Crystal structure: body-centered tetragonal (β-tin, "white tin") above 13.2°C; diamond cubic (α-tin, "gray tin") below 13.2°C. The α→β transformation ("tin pest") destroys the metal in cold climates over years — pure tin crumbles to gray powder. Alloying with Bi or Sb (0.1-0.5%) prevents tin pest.
- Non-toxic: Tin is one of the few metals considered non-toxic. Tinplate for food containers is safe.

**Applications**:
- **[Solder](../glossary/solder.md)** (35%): Sn-Pb solder (63Sn-37Pb eutectic, mp 183°C) was the standard for millennia. Lead-free solders (mandated by RoHS since 2006): SAC305 (96.5Sn-3.0Ag-0.5Cu, mp 217-220°C), Sn-Cu (99.3Sn-0.7Cu, mp 227°C). See [Electronics Assembly](../computing/index.md).
- **[Tinplate](../glossary/tinplate.md)** (30%): Electrolytic tin coating on steel sheet (0.5-2.0 μm Sn) for food and beverage cans. Provides non-toxic, corrosion-resistant, solderable surface.
- **Bronze and pewter**: Tin as alloying element in bronze (Cu-5-10% Sn), bearing metals (Babbitt: Sn-7-10%Sb-3-5%Cu), and pewter (Sn-1-8%Sb-0-3%Cu, lead-free modern formulation).
- **Glass coating**: Float glass production uses molten tin as the flat substrate — glass floats on tin bath at ~1000°C, producing optically flat surfaces (Pilkington process). This is the single largest industrial use of tin by volume of product enabled.

### Nickel

Nickel is the key alloying element that makes stainless steel stainless. It provides austenite stability, corrosion resistance, and high-temperature strength. Roughly 65% of world nickel production goes into stainless steel. Nickel-based superalloys enable jet turbine blades that operate at >1000°C — no other alloy system matches their creep resistance.

**Ores**:
- **[Sulfide ores](../glossary/sulfide-ores.md)** (~30% of production): Pentlandite ((Fe,Ni)₉S₈) with pyrrhotite (Fe₁₋ₓS) and chalcopyrite (CuFeS₂). Major deposits: Sudbury (Canada), Norilsk (Russia), Kambalda (Australia). Nickel grade: 1-3% Ni. These ores also carry Cu, Co, and platinum-group metals as valuable byproducts.
- **[Laterite ores](../glossary/laterite-ores.md)** (~70% of production): Nickeliferous limonite (Fe-Ni oxides, 1-1.8% Ni) and saprolite (Mg-Ni silicates, 1.5-2.5% Ni). Formed by tropical weathering of ultramafic rocks. Major deposits: Indonesia, Philippines, New Caledonia, Cuba. No valuable byproducts. Higher mining cost, lower grade, but much larger total resources than sulfides.

**Extraction — Sulfide ores**:
- **Beneficiation**: Flotation produces 10-20% Ni concentrate. Magnetic separation recovers pyrrhotite.
- **Smelting**: Flash smelting (Outokumpu process) or electric furnace smelting. Partial oxidation of sulfides provides heat (exothermic) and concentrates nickel in matte (Ni-Cu-Fe sulfides). Converter blowing removes iron and sulfur, producing Bessemer matte (~75% Ni+Cu). Slow cooling and flotation separate Cu₂S from Ni₃S₂.
- **Refining — Mond carbonyl process**: Ni + 4CO → Ni(CO)₄ at 50-60°C, atmospheric pressure. The volatile nickel carbonyl gas is distilled and decomposed at 200°C on nickel pellets (decomposition: Ni(CO)₄ → Ni + 4CO). CO is recycled. Produces 99.97% pure nickel. Highly toxic process — Ni(CO)₄ is one of the most poisonous industrial gases (TLV 0.001 ppm).
- **Alternative**: Electrolytic refining with sulfate or chloride electrolyte. Nickel anodes dissolve; pure nickel deposits on starter cathodes. 99.9% Ni.

**Extraction — Laterite ores**:
- **Pyrometallurgical route (saprolite)**: Rotary kiln calcination (600-900°C) to remove moisture and pre-reduce, then electric furnace smelting at 1500-1600°C with carbon reductant. Product: ferronickel (20-40% Ni + Fe) or nickel matte. Energy: 400-600 kWh per tonne dry ore. Used for stainless steel feed directly.
- **Hydrometallurgical route (limonite)**: High-pressure acid leach (HPAL). Ore slurry leached with sulfuric acid at 240-270°C, 4-5 MPa in titanium-lined autoclaves. Dissolves Ni and Co; iron precipitates as hematite. Solvent extraction or precipitation recovers Ni. Complex, capital-intensive, but growing.

**Properties**:
- Density: 8.90 g/cm³. Melting point: 1455°C. Boiling point: 2913°C.
- Crystal structure: FCC (face-centered cubic). Excellent ductility and toughness down to cryogenic temperatures.
- Magnetic: Ferromagnetic below 358°C (Curie temperature). Less strongly magnetic than iron.
- Corrosion resistance: Forms passive NiO film. Resists alkalis, many organic acids, and seawater.

**Applications**:
- **[Stainless steel](../glossary/stainless-steel.md)** (65%): Austenitic grades (304: 18Cr-8Ni, 316: 17Cr-12Ni-2.5Mo). Nickel stabilizes the austenite phase at room temperature, preventing the brittle martensite transformation. See [Iron & Steel](iron-steel.md).
- **[Superalloys](../glossary/superalloys.md)** (10%): Ni-Cr-Co base with Al, Ti, Mo, W, Ta additions. γ' precipitation hardening (Ni₃(Al,Ti)) provides creep resistance at 700-1100°C. Used in gas turbine blades, combustion chambers. Inconel, Hastelloy, Waspaloy.
- **[Electroplating](../glossary/electroplating.md)** (10%): Nickel plating provides hard, corrosion-resistant, bright surface. Undercoat for chromium plating. Watts bath: NiSO₄ + NiCl₂ + H₃BO₃ at 45-65°C, pH 3.5-4.5.
- **Coinage**: Cupronickel (Cu-25Ni) and pure nickel coin blanks.

### Magnesium

Magnesium is the lightest structural metal (1.74 g/cm³, 35% lighter than aluminum and 78% lighter than steel). It is the third most abundant element in seawater (1.3 kg/m³). Despite its abundance, extraction is energy-intensive, making magnesium 2-3× more expensive than aluminum per unit mass.

**Raw materials**:
- **[Dolomite](../glossary/dolomite.md)** (CaCO₃·MgCO₃): Widely available sedimentary rock. Calcine at 1100-1200°C to produce CaO·MgO (doloma).
- **Seawater/brine**: MgCl₂ extracted by precipitation with dolime: MgCl₂ + CaO → Mg(OH)₂ + CaCl₂. Mg(OH)₂ calcined to MgO, then chlorinated to MgCl₂.
- **[Magnesite](../glossary/magnesite.md)** (MgCO₃): Direct calcination to MgO.

**[Pidgeon process](../glossary/pidgeon-process.md)** (silicothermic reduction, dominant in China — ~85% of world production):
- **Calcination**: MgCO₃ → MgO + CO₂ at 1100-1200°C.
- **Briquetting**: MgO + ferrosilicon (FeSi 75%) + CaO flux mixed and pressed into briquettes.
- **Reduction**: MgO + FeSi → Mg(g) + iron silicates at 1150-1200°C under vacuum (1-10 Pa) in horizontal retorts (nickel-chromium steel, 250-300 mm diameter, 2.5-3 m long). Magnesium vapor condenses as crystalline crown in the water-cooled condenser section. Cycle time: 8-12 hours per batch.
- **Yield**: ~80% of MgO reduced per cycle. Energy: 10-12 MWh per tonne Mg (very energy-intensive). Labor-intensive batch process.
- **Product**: 99.5-99.9% Mg (primary magnesium). Further distilled for higher purity.

**[Electrolytic process](../glossary/electrolytic-process.md)** (ISF/Dow process):
- Feed: Anhydrous MgCl₂ (critical — water contamination generates HCl gas and hydrolyzes the cell).
- **Dow process**: Dehydrated MgCl₂·1.5H₂O fed directly to cell (partially hydrated — generates some HCl, managed by cell design). Electrolyte: NaCl-KCl-MgCl₂ melt at 700-750°C. Steel cathode, graphite anode. Mg²⁺ + 2e⁻ → Mg(l) (rises to surface, protected by inert gas blanket). 2Cl⁻ → Cl₂(g). Cell voltage 5-7 V, current 50-100 kA. Energy: 16-18 kWh/kg Mg.
- Product: 99.8-99.9% Mg. Chlorine byproduct is recycled to chlorination stage.

**Properties**:
- Density: 1.74 g/cm³. Melting point: 650°C. Boiling point: 1090°C.
- Crystal structure: HCP. Limited cold formability (few slip systems at room temperature — deforms primarily by basal slip and twinning). Hot forming above 200°C activates additional slip systems.
- Flammable: Magnesium burns in air with an intense white flame (3100°C). Difficult to extinguish — water accelerates burning (reacts to produce H₂). Class D fire extinguishers (dry powder: NaCl or graphite base) required.
- Galvanic: Highly anodic (standard potential -2.37 V). Must be insulated from steel, copper, and nickel in assemblies to prevent galvanic corrosion.

**Applications**:
- **[Die casting](../glossary/die-casting.md)** (35%): Mg-Al-Zn alloys (AZ91: Mg-9Al-0.7Zn, AM60: Mg-6Al-0.3Mn). Automotive: instrument panels, seat frames, steering wheels. Electronics: laptop frames, camera bodies. Extremely thin-wall casting possible (0.5 mm).
- **[Aluminum alloying](../glossary/aluminum-alloying.md)** (30%): Mg added to Al (0.5-5%) increases strength, weldability, and corrosion resistance. 5000-series (Al-Mg) and 6000-series (Al-Mg-Si) alloys. See [Aluminum](aluminum.md).
- **[Sacrificial anodes](../glossary/sacrificial-anodes.md)** (10%): Higher driving voltage than zinc anodes. Used for buried pipelines, hot water tanks, marine hulls. Consumed at ~4-8 kg/year per ampere of protection current.
- **Titanium production**: Kroll process consumes 1.1-1.2 tonnes Mg per tonne Ti. The single largest industrial consumer of magnesium in some regions.

### Titanium

Titanium is the ninth most abundant element in Earth's crust (0.6%) but among the most difficult and expensive structural metals to produce. Its exceptional strength-to-weight ratio (Ti-6Al-4V: ~950 MPa UTS at 4.43 g/cm³) and corrosion resistance make it irreplaceable in aerospace, medical implants, and chemical processing. The Kroll process — batch, laborious, unchanged since 1940 — remains the bottleneck.

**Ores**:
- **[Ilmenite](../glossary/ilmenite.md)** (FeTiO₃): The primary titanium ore. Black, heavy (SG 4.5-5.0). Beach sand deposits (India, Australia, South Africa) and hard-rock deposits (Norway, Canada). TiO₂ content: 45-65%. Also mined for titanium dioxide pigment.
- **[Rutile](../glossary/rutile.md)** (TiO₂): Higher grade (93-96% TiO₂) but rarer. Found as beach sand concentrates. Preferred feedstock for titanium metal due to lower impurity removal cost.
- **Beneficiation**: Magnetic separation (ilmenite is weakly magnetic, rutile is not), electrostatic separation, and spiral gravity concentration. Sufimed ilmenite is upgraded to synthetic rutile (90-95% TiO₂) by Becher process (reduction roasting + aeration leach) or Benelite process (HCl leach).

**[Kroll process](../glossary/kroll-process.md)** (virtually all primary titanium metal):
- **Step 1 — Chlorination**: TiO₂ + 2Cl₂ + C → TiCl₄ + CO₂ (or CO) at 900-1000°C in a fluidized-bed chlorinator. Titanium tetrachloride is a volatile liquid (bp 136°C) — distilled to high purity (>99.9%). Impurities (FeCl₃, SiCl₄, VOCl₃) removed by fractional distillation.
- **Step 2 — Reduction**: TiCl₄(l) + 2Mg(l) → Ti(s) + 2MgCl₂(l) at 800-900°C under argon atmosphere in a sealed steel retort. The reaction is exothermic (ΔH = -260 kJ/mol TiCl₄) — initiated by heating, then self-sustaining. Titanium deposits as a porous sponge ("titanium sponge") — not a molten metal because titanium's melting point (1668°C) far exceeds the reaction temperature.
- **Step 3 — Separation**: MgCl₂ is drained from the retort (molten at reaction temperature). Residual Mg and MgCl₂ removed by vacuum distillation (1000°C, <1 Pa, 20-40 hours) or acid leaching.
- **Sponge crushing and grading**: The titanium sponge mass is crushed, sorted by grade (based on hardness — a proxy for oxygen/nitrogen content). Top-grade sponge: <700 HV, <0.05% O₂. Lower grades blended for specific alloy grades.
- **Yield and cost**: 1.9-2.0 tonnes TiCl₄ + 1.0-1.1 tonnes Mg → 1.0 tonne Ti sponge. MgCl₂ byproduct is electrolyzed back to Mg and Cl₂ for recycle. Batch process: 2-5 tonnes per retort, 5-10 days cycle. Cost: $6-12/kg sponge (10-20× the cost of steel per kg).

**Melting and refining**:
- **Vacuum Arc Remelting (VAR)**: Sponge + alloying elements (Al, V, O, Fe) compacted into electrodes, welded together, and remelted in a water-cooled copper crucible under vacuum. DC arc (20-40 kA, 20-40 V). The melt pool solidifies directionally from bottom up, producing a homogeneous ingot with low dissolved gas content. Typically double- or triple-melted for aerospace grades.
- **Electron Beam Cold Hearth Remelting (EBCHR)**: Alternative for premium quality. Electron beam melts feedstock in a cold copper hearth; high-density inclusions (W, Ta) settle in the hearth lip before the clean melt overflows into the ingot mold. Better inclusion removal than VAR. Used for turbine disk material.
- **Ingot size**: 500-10,000 kg. Subsequent processing: forging, rolling, extrusion — all done above the α→β transus temperature (~995°C for Ti-6Al-4V) or in the α+β two-phase region, depending on desired microstructure.

**Properties**:
- Density: 4.51 g/cm³ (56% of steel, 1.7× aluminum). Melting point: 1668°C.
- Crystal structure: HCP (α) below 882°C; BCC (β) above 882°C. The allotropic transformation enables diverse microstructures and property combinations through alloying and heat treatment.
- **[Ti-6Al-4V](../glossary/ti-6al-4v.md)** (Grade 5, "workhorse alloy" — 50% of titanium consumption): 900-950 MPa UTS, 830-880 MPa yield, 10-14% elongation, 4.43 g/cm³. α+β alloy — aluminum stabilizes α phase, vanadium stabilizes β phase. Used in annealed or solution-treated-and-aged condition.
- Corrosion resistance: Passive TiO₂ film (2-10 nm thick) spontaneously forms in oxygen-containing environments. Resists seawater, chlorides, most acids (except HF and hot concentrated HCl/H₂SO₄). No pitting or crevice corrosion in seawater.
- Biocompatibility: Osseointegrates — bone grows directly into titanium surface. Non-toxic, non-allergenic. The standard for orthopedic and dental implants.

**Applications**:
- **[Aerospace](../glossary/aerospace.md)** (50% of mill products): Airframe components (landing gear, wing structures, engine pylons), jet engine compressor blades and disks. Ti-6Al-4V and Ti-6Al-2Sn-4Zr-2Mo (high-temperature creep resistance up to 540°C).
- **[Medical implants](../glossary/medical-implants.md)** (10%): Hip and knee replacements, bone plates, dental implants, pacemaker housings. Commercially pure Ti (Grades 1-4) and Ti-6Al-4V ELI (extra-low interstitial — reduced O₂ for improved fracture toughness).
- **Chemical process equipment**: Heat exchangers, reactor vessels, piping for aggressive media (chlor-alkali, desalination, offshore). Titanium condenser tubes in power plants — zero corrosion in seawater over 40+ year lifetime.
- **[Pigment](../glossary/pigments.md)** (TiO₂, not metal but 95% of titanium ore consumption): White pigment in paint, plastics, paper. Produced by chloride process (TiCl₄ oxidation) or sulfate process (TiO₂ dissolution in H₂SO₄). This is a separate industry from titanium metal — orders of magnitude larger.

### Interdependencies and Bootstrap Sequence

Non-ferrous metals have significant interdependencies:

- **[Zinc](../glossary/zinc.md)** is required for the Parkes process (lead desilverization) and for sacrificial protection of steel (galvanizing).
- **[Lead](../glossary/lead.md)** provides the initial battery storage essential before lithium systems exist (see [Electrical Systems](../energy/electricity.md)).
- **[Tin](../glossary/tin.md)** enables electronics solder — no tin, no reliable circuit assembly. Also critical for bronze production (see [Copper & Bronze](copper-bronze.md)).
- **[Nickel](../glossary/nickel.md)** makes stainless steel possible — without nickel, only ferritic (lower-chromium, magnetic, less corrosion-resistant) stainless steels can be produced.
- **[Magnesium](../glossary/magnesium.md)** is consumed by the Kroll process to produce titanium; conversely, titanium equipment serves in magnesium electrolysis cells.
- **[Titanium](../glossary/titanium.md)** production requires chlorine (from electrolysis of NaCl/KCl — see [Chemistry](../chemistry/index.md)), magnesium, and inert gas (argon from air separation).

**Suggested build order**:
1. **[Tin and lead](../glossary/tin-and-lead.md)** (Years 15-20): Lowest complexity — simple reduction smelting, low temperatures. Enables bronze, solder, batteries.
2. **[Zinc](../glossary/zinc.md)** (Years 18-25): Roast-leach-electrowin requires sulfuric acid and electrochemistry. Enables galvanizing and brass.
3. **[Nickel](../glossary/nickel.md)** (Years 20-30): Sulfide smelting is straightforward but laterite processing requires HPAL or electric furnaces. Enables stainless steel and superalloys.
4. **[Magnesium](../glossary/magnesium.md)** (Years 25-35): Pidgeon process requires ferrosilicon and vacuum capability. Electrolytic route requires large DC power.
5. **[Titanium](../glossary/titanium.md)** (Years 30-40): Kroll process demands chlorine chemistry, magnesium production, argon supply, and vacuum distillation. The capstone non-ferrous metal.

### Safety & Hazards

**Toxic metals**:
- **Lead**: Cumulative neurotoxin. Blood lead levels >5 μg/dL (children) cause cognitive impairment. Exposure routes: inhalation of dust/fume, ingestion (hand-to-mouth). Engineering controls: local exhaust ventilation, HEPA filtration, wet methods to suppress dust. Medical surveillance: blood lead monitoring every 6 months for workers. PPE: respirators (P100), gloves, dedicated work clothing laundered on-site. Do not eat, drink, or smoke in lead work areas.
- **Nickel carbonyl** (Mond process): One of the most toxic industrial gases. TLV-TWA: 0.001 ppm (1 ppb). Immediately fatal at 30 ppm. Colorless, odorless. Continuous air monitoring mandatory. Full-face SCBA for any potential exposure. Emergency evacuation if detectors alarm.
- **Nickel skin sensitization**: Nickel is the most common cause of contact allergic dermatitis (10-20% of population). EU restricts nickel release from skin-contact items (<0.5 μg/cm²/week).

**Magnesium fire**:
- Ignition temperature: ~473°C for fine powder, ~650°C for solid sections. Burns at 3100°C with intense white light (UV eye damage). **Never use water** — reacts to produce hydrogen gas, which then ignites explosively. Smother with dry sand, Class D powder (NaCl-based or graphite-based), or cast iron chips. Do not use CO₂ or halon — magnesium burns in CO₂. Firefighters must wear full PPE with face shield — the UV radiation from burning magnesium causes retinal damage.

**Zinc and titanium tetrachloride**:
- **Zinc fume fever** (metal fume fever): Inhalation of zinc oxide fume (from welding/brazing galvanized steel) causes influenza-like symptoms 4-8 hours post-exposure: chills, fever, muscle ache, metallic taste. Self-limiting (resolves in 24-48 hours) but repeated episodes cause lung damage. Prevention: local exhaust ventilation, respiratory protection when welding galvanized steel.
- **TiCl₄**: Reacts violently with moisture in air, producing dense white HCl fume and TiO₂ particulate. Severe burns to skin and eyes. All TiCl₄ handling must be in enclosed, dry systems. Leak response: water spray (from safe distance) to knock down HCl cloud, full acid-rated PPE. TiCl₄ spills on moisture generate massive exothermic reaction — approach upwind only.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Metals](./index.md) • [All Domains](../index.md)*
