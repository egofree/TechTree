# Electrolysis

> **Node ID**: chemistry.electrolysis
> **Domain**: Chemistry
> **Dependencies**: `chemistry.electrodialysis`, `chemistry.lithium-separation`, `chemistry.water-electrolysis`, [`energy.electricity`](../energy/electricity.md), `energy.fuel-cell`, `energy.redox-flow-battery`
> **Enables**: [`chemistry.ammonia`](ammonia.md), [`chemistry.dopant-etch-gases`](dopant-etch-gases.md), [`chemistry.hydrogen-silane`](hydrogen-silane.md), [`chemistry.pulp-chemicals`](pulp-chemicals.md), `electrochemistry`, [`electronics.electrical-systems`](../electronics/electrical-systems.md), [`metals.aluminum`](../metals/aluminum.md), [`metals.finishing`](../metals/finishing.md)
> **Timeline**: Years 20-30
> **Outputs**: electrolysis, chlorine, hydrogen, oxygen, aluminum, caustic_soda, pure_copper

### Electrolysis Scale-Up

**[Chlor-alkali process](../glossary/chlor-alkali-process.md)** (most important industrial electrolysis):
- **Cell types**:
  - **Diaphragm cell**: Asbestos or polymer diaphragm separates anode and cathode compartments. Prevents Cl₂ and NaOH from mixing (would form NaOCl — bleach). Products: Cl₂ gas, H₂ gas, 10-12% NaOH solution (requires evaporation to 50%).
  - **[Membrane cell](../glossary/membrane-cell.md)** (modern): Ion-exchange membrane (Nafion or equivalent — perfluorinated polymer chemistry). More efficient, produces directly 30-35% NaOH. But membrane requires PTFE-like fluoropolymer.
- **Anode**: Dimensionally stable anode (DSA) — titanium coated with RuO₂/IrO₂. Or graphite (cheaper, consumed slowly ~2-5 kg/tonne Cl₂). Carbon anodes work for startup.
- **Cathode**: Steel or nickel. Hydrogen evolves at cathode: 2H₂O + 2e⁻ → H₂ + 2OH⁻.
- **Operating conditions**: 3.2-3.8V per cell, 2-5 kA/m² current density. Temperature 80-90°C. NaCl concentration ~25%.
- **Energy consumption**: ~2,100-2,500 kWh per tonne of Cl₂. Major power load.

**Chlor-alkali diaphragm cell — detailed construction and operation**:

The chlor-alkali process produces three critical products simultaneously: chlorine gas, hydrogen gas, and sodium hydroxide (caustic soda). The overall reaction is 2NaCl + 2H₂O → Cl₂ + 2NaOH + H₂.

- **Cell body**: Rectangular steel or concrete tank, typically 1-2 m wide × 0.5-1 m deep × 2-3 m long. Steel is preferred for durability; concrete is acceptable for initial construction. The cell must be electrically insulated from ground.
- **Anode compartment**: Saturated brine (NaCl solution, ~310 g/L at 25°C, maintained at 25-26% by weight) fed continuously to the anode side. Anodes are vertical plates of graphite (50-100 mm thick, 300-600 mm wide, 600-1200 mm tall) or dimensionally stable anodes (DSA — titanium substrate coated with 5-15 µm layer of RuO₂/IrO₂ mixed metal oxide). DSA anodes last 5-8 years; graphite anodes consume at 2-5 kg per tonne of Cl₂ produced. Multiple anode plates mounted in parallel on a copper or titanium bus bar.
- **Diaphragm**: Deposited asbestos fiber layer (1-3 mm thick) on the cathode mesh, or modern polymer membrane (perfluorinated sulfonic acid, 100-200 µm thick). The diaphragm allows Na⁺ ions and water to pass but retards back-migration of OH⁻ ions and prevents Cl₂ and H₂ from mixing. Asbestos diaphragm deposited by vacuum-drawing an asbestos slurry onto the cathode screen. Service life: 6-12 months before replating needed.
- **Cathode compartment**: Perforated steel mesh or screen (2-3 mm wire, 3-5 mm openings) acts as both cathode and diaphragm support. Hydrogen gas evolves at the cathode surface: 2H₂O + 2e⁻ → H₂↑ + 2OH⁻. The NaOH solution (10-12% from diaphragm cell) drains from the cathode compartment by gravity.
- **Gas handling**: Cl₂ gas (anode) is hot, wet, and contains traces of oxygen and carbon dioxide. Route through titanium or glass-fiber-reinforced plastic (FRP) ducting to a cooling tower (water-cooled, condenses water vapor), then through a drying tower (concentrated H₂SO₄, 93-98%, as desiccant), then to compressors for liquefaction (compress to 5-8 bar, cool to -10 to -20°C) or direct pipeline use. H₂ gas (cathode) is separately collected, cooled, and can be used as fuel or chemical feedstock. **Never allow Cl₂ and H₂ to mix — the mixture is explosive over a wide range (4-93% H₂ in Cl₂).**
- **Cell stacking**: Individual cells produce at 3.5-4.0V. Stack 50-100 cells in electrical series (bipolar configuration) to match available DC supply voltage (200-400V). Each cell operates independently hydraulically. A single electrolyzer may draw 50-200 kA total current.
- **NaOH concentration**: Diaphragm cell effluent is only 10-12% NaOH (contaminated with 15-17% unreacted NaCl). Evaporate in triple-effect vacuum evaporators to 50% NaOH (NaCl crystallizes out during evaporation and is recycled to brine feed). Membrane cells produce 30-35% NaOH directly with minimal salt contamination — a major advantage.
- **Brine purification**: Raw salt solution contains Ca²⁺, Mg²⁺, SO₄²⁻, and heavy metals that poison electrodes and clog diaphragms. Treatment: add Na₂CO₃ to precipitate CaCO₃, add NaOH to precipitate Mg(OH)₂, add BaCO₃ or BaCl₂ to precipitate BaSO₄ if sulfate exceeds 5 g/L. Filter through sand or leaf filters before feeding cells.

**Water electrolysis**:
- **Alkaline electrolyzer**: 25-30% KOH electrolyte. Nickel electrodes. Temperature 60-80°C. Cell voltage 1.8-2.2V. Current efficiency ~95-99%.
- **Products**: Ultra-pure H₂ and O₂. H₂ purity critical for semiconductor processes (see [Hydrogen & Silane Production](hydrogen-silane.md)).
- **Energy**: ~50-55 kWh per kg H₂ (thermodynamic minimum 33 kWh/kg).

**Water electrolysis — detailed procedures**:

- **Alkaline electrolysis (most practical for bootstrap)**:
  - **Cell construction**: Two nickel-plated steel or pure nickel electrode plates separated by 2-5 mm gap. Diaphragm of asbestos or polymer fabric (polypropylene, polysulfone) prevents gas mixing. Electrolyte: 25-30% KOH in deionized water (specific gravity ~1.23-1.28). Cell body: carbon steel (KOH is less corrosive than NaOH to steel at operating temperature). Gasket: EPDM rubber.
  - **Operating conditions**: 1.8-2.2V per cell, current density 2-4 kA/m², temperature 60-90°C. Higher temperature reduces cell voltage (thermodynamic advantage) but increases corrosion and electrolyte vaporization. Pressure: atmospheric or slightly elevated (1-30 bar for pressurized systems — reduces downstream compression energy).
  - **Reactions**: Cathode: 2H₂O + 2e⁻ → H₂ + 2OH⁻. Anode: 2OH⁻ → ½O₂ + H₂O + 2e⁻. Net: H₂O → H₂ + ½O₂. Thermoneutral voltage: 1.48V at 25°C.
  - **Gas quality**: H₂ >99.5% pure (main impurity: traces of O₂ and KOH mist). O₂ >99.0% pure. Further purification by catalytic recombination (remove trace O₂ from H₂ by passing over Pt catalyst with excess H₂) and molecular sieve drying.
  - **Stack design**: 50-200 cells in filter-press configuration (bipolar plates between cells). Active area per cell: 0.5-4 m². Total stack: 100-400V DC input, 2-20 kA. Production rate: ~0.4-0.5 Nm³ H₂ per kWh.
  - **Electrolyte management**: KOH is not consumed — only water is split. Feed deionized or distilled water continuously to maintain electrolyte level. Monitor KOH concentration (refractometer or density measurement). Replace electrolyte every 5-10 years due to impurity accumulation.
- **PEM (proton exchange membrane) electrolysis**:
  - **Principle**: Solid polymer electrolyte (Nafion membrane, 50-175 µm thick) conducts protons (H⁺) from anode to cathode. No liquid electrolyte needed. Platinum catalyst (0.5-2 mg/cm²) on both electrodes as thin-film coating on the membrane (catalyst-coated membrane, CCM).
  - **Advantages**: Higher current density (5-20 kA/m² — 3-5× alkaline), more compact, produces very high purity H₂ (>99.99%), operates under differential pressure (H₂ at 30-80 bar, O₂ at atmospheric), rapid response to variable power input (good for renewable integration).
  - **Disadvantages**: Requires Nafion or equivalent perfluorinated membrane (complex fluoropolymer chemistry — not available until polymer industry is mature). Platinum catalyst is expensive and scarce. Titanium current collectors and flow fields required for anode side (acidic environment). Membrane degradation: 40,000-80,000 hours typical life.
  - **Operating conditions**: 1.8-2.2V per cell, 50-80°C, water fed to anode side.
  - **Verdict for bootstrap**: Alkaline electrolysis is the only practical route until fluoropolymer chemistry is established. PEM is documented here as the advanced target.

**[Aluminum production](../metals/aluminum.md)** (Hall-Héroult process — enormous power consumer):
- **Feedstock**: Purified alumina (Al₂O₃) from bauxite via Bayer process: dissolve bauxite in hot NaOH (150-250°C, 5-30 bar), filter impurities (red mud), precipitate Al(OH)₃, calcine at 1100-1200°C → Al₂O₃.
- **Electrolysis**: Dissolve Al₂O₃ in molten cryolite (Na₃AlF₆, melting point 1012°C) at 950-1000°C. Carbon anodes, carbon-lined steel cathode. Al³⁺ + 3e⁻ → Al (liquid aluminum pools at bottom, tapped periodically). Carbon consumed: 2O²⁻ + C → CO₂.
- **Operating conditions**: 4.0-4.5V, 150-400 kA per cell, ~13-15 kWh/kg Al.
- **Power requirement**: A small aluminum plant (10,000 tonnes/year) needs ~15 MW continuous. This is why aluminum was more expensive than gold before cheap electricity.

**Hall-Héroult process — detailed cell construction and operation**:

The overall cell reaction is 2Al₂O₃ + 3C → 4Al + 3CO₂. The carbon anode is consumed as a reactant, not merely as an electrode.

- **Cell shell**: Rectangular steel box (10-15 mm plate), typically 8-12 m long × 3-4 m wide × 1-1.5 m deep. Externally reinforced with steel cradle. Shell sits on electrically insulated supports. Thermal insulation (firebrick, calcium silicate board) between shell and carbon lining to reduce heat loss.
- **Cathode lining**: Bottom and lower sides lined with prebaked carbon cathode blocks (anthracite + 25-30% coal tar pitch, baked at 1000-1200°C). Blocks typically 400-700 mm × 400-600 mm × 1200-2500 mm, joined with carbonaceous ramming paste. Steel current-collector bars (100-200 mm diameter round or rectangular) embedded in grooves in the cathode blocks, sealed with cast iron or carbonaceous paste. Cathode life: 3-8 years before relining required (failure mode: sodium penetration cracks blocks, bath leaks to steel shell).
- **Anodes**: Prebaked carbon anodes (petroleum coke + 13-16% coal tar pitch, baked at 1100-1200°C for 2-3 weeks). Typical dimensions: 400-800 mm wide × 500-600 mm tall × 1500-2000 mm long, each weighing 800-1200 kg. Multiple anodes per cell (12-40 anodes), each suspended from an anode bus bar by steel stubs (rodded into the anode with cast iron). Anodes are consumed at 0.4-0.5 kg carbon per kg Al produced. Lowered continuously (hydraulic or jack mechanism, 10-20 mm/day) to maintain 40-50 mm anode-cathode distance (ACD) as they burn away.
- **Bath composition**: Primary solvent: cryolite (Na₃AlF₆), 80-90% of bath by weight. Additives: 5-10% excess AlF₃ (lowers melting point from 1012°C to 960°C, reduces sodium co-deposition), 2-5% CaF₂ (further lowers melting point, reduces bath volatility). Alumina feed maintained at 2-5% dissolved in bath (must not exceed ~8% — forms a frozen sludge on cell bottom; must not fall below ~1.5% — triggers "anode effect" where voltage spikes to 20-40V, CF₄ and C₂F₆ greenhouse gases evolve). Bath temperature: 960-980°C.
- **Alumina feeding**: Automatic point feeders (crust breaker + alumina hopper) punch through the frozen bath crust and dump 1-2 kg alumina per feed event every 1-5 minutes. Alternatively, batch feeding (larger additions, less frequent) for simpler cells. Alumina must be well-calcined (α-Al₂O₃, <0.04% moisture) — moisture in the bath causes HF generation.
- **Metal tapping**: Molten aluminum (density 2.3 g/cm³ at 960°C) pools beneath the bath (density ~2.1 g/cm³). Tap every 24-48 hours by inserting a steel or refractory siphon tube through the crust and vacuum-siphoning 1-5 tonnes of aluminum into a refractory-lined ladle. Typical cell holds 5-15 tonnes of molten aluminum at steady state.
- **Electrical**: 4.0-5.0V per cell at 100-500 kA (modern cells). Cells connected in series (potline) — 200-300 cells per potline. Total potline voltage: 800-1200V DC. Current supplied by silicon diode rectifiers from AC power. Energy consumption: 13-15 kWh/kg Al (theoretical minimum: 6.3 kWh/kg for Al₂O₃ → Al, but carbon anode reduces electrical energy needed — total energy includes anode combustion heat). Heat balance: ~50% of electrical input is heat — must be dissipated to maintain 960-980°C bath temperature. Cell designed so heat loss through sides, bottom, and top crust matches internal heat generation.
- **Emissions**: CO₂ from anode consumption (~1.5 t CO₂ per t Al), plus CO₂ from electricity generation (if fossil-fueled). Fluoride emissions (HF, CF₄, C₂F₆) controlled by dry scrubbing (alumina absorbs HF, then fed to cells — closing the fluoride loop). CF₄ and C₂F₆ are extremely potent greenhouse gases (GWP 6,620 and 11,100 respectively) — minimize anode effects.

**[Copper electrorefining](../glossary/copper-electrorefining.md)** (produces 99.99% pure Cu from impure anodes):
- **Cell**: Impure copper cast anode (from smelter, ~98-99% Cu). Pure copper starter sheet cathode (thin Cu foil). Electrolyte: CuSO₄ (150-200 g/L) + H₂SO₄ (150-200 g/L) in aqueous solution. Temperature 50-65°C.
- **Reaction**: Cu (anode) → Cu²⁺ + 2e⁻ (dissolution). Cu²⁺ + 2e⁻ → Cu (cathode, pure deposit). Cell voltage only 0.2-0.3 V (very low — most energy goes to pumping electrolyte, not overcoming thermodynamics). Current density: 200-300 A/m².
- **Impurities**: Ag, Au, Pt, Se, Te do not dissolve — settle as "anode slime" (valuable byproduct, recovered for precious metals). Ni, Fe, Zn dissolve but do not plate at cathode with proper voltage control. As, Sb, Bi must be controlled — can co-deposit.
- **Anode slime recovery**: Collect slime, treat with H₂SO₄ + oxidant → dissolve Cu, Se, Te. Melt residual → Doré metal (Ag + Au). Electrorefine silver. Gold and PGMs recovered from silver cell slimes. Revenue from precious metals often exceeds cost of copper refining.

**Copper electrorefining — detailed cell design and operation**:

- **Tank construction**: Concrete or polymer-lined (PVC, polyethylene) rectangular tank, typically 3-5 m long × 1-1.2 m wide × 1.2-1.5 m deep. Multiple anodes and cathodes hang in parallel, alternating, with 80-120 mm gap between anode and cathode surfaces. A single tank holds 30-50 anode-cathode pairs.
- **Anode**: Cast blister copper slabs (~98-99% Cu, containing Ag, Au, Ni, Se, Te, As, Sb, Bi, Fe, Zn, Pb, Sn as impurities). Dimensions: 800-1000 mm × 800-1000 mm × 30-50 mm thick, weighing 250-400 kg each. Suspended from copper bus bars by cast-in lugs. Anode life: 20-28 days (dissolved to ~15% residual — "anode scrap" recycled to smelter).
- **Cathode**: Thin copper starter sheet (0.5-1 mm thick) produced on titanium or stainless steel blanks (deposit copper for 1-2 days, strip off). Alternatively, stainless steel blanks (reusable — copper deposits on both sides, stripped off mechanically after 7-14 days). Cathode dimensions similar to anode but slightly wider to prevent edge growth short-circuiting. Pure copper deposits over 7-14 days to 5-10 mm thickness, weighing 80-160 kg per cathode.
- **Electrolyte circulation**: CuSO₄ + H₂SO₄ solution continuously pumped through tanks (20-30 L/min per tank) to maintain uniform temperature (50-65°C — warmed by steam heat exchangers) and composition, and to prevent stratification. Additives (glue, thiourea, chloride ions at 20-40 mg/L) promote smooth, dense cathode deposits and suppress dendritic growth that causes short circuits.
- **Tankhouse layout**: Hundreds to thousands of tanks arranged in rows. Electrical connection: tanks in series, anodes and cathodes within each tank in parallel. Total tankhouse voltage: 100-200V DC at 10,000-30,000 A. Current per cathode: 200-350 A/m² × cathode area (~0.8-1 m²) = 160-350 A per cathode.
- **Anode slime processing**: Slime (0.1-0.5% of anode weight) settles to tank bottom, collected every anode change cycle (3-4 weeks). Composition: 10-30% Ag, 0.5-5% Au, plus Se, Te, Pt, Pd. Processing: pressure-leach with H₂SO₄ + O₂ to dissolve Cu, Se, Te. Smelt residual in precious metals furnace → Doré bullion (95%+ Ag + Au). Electrorefine silver in Balbach-Thum cells (Ag → 99.99% pure). Gold and PGMs recovered from silver refining slimes by aqua regia dissolution and selective precipitation.
- **Energy**: Very low — only 250-350 kWh per tonne of refined copper (vs. ~13,000-15,000 kWh/t for aluminum). The dominant cost is labor and working capital (metal tied up in process), not electricity.

### Electrode Materials & Cell Design

**Electrode materials by process**:

| Process | Anode | Cathode | Notes |
|---------|-------|---------|-------|
| Chlor-alkali | DSA (Ti + RuO₂/IrO₂) or graphite | Steel or nickel | Graphite consumed ~2-5 kg/t Cl₂ |
| Water electrolysis | Nickel or Ni-coated steel | Nickel or Ni-coated steel | Inert — neither electrode consumed |
| Aluminum | Carbon (consumed: C + O → CO₂) | Carbon-lined steel | Carbon is both electrode and reactant |
| Copper refining | Impure Cu (consumed) | Pure Cu starter sheet | Consumable anode — impurities left behind |

- **Selection criteria**: Inert electrodes (Pt, graphite, DSA) for processes where the electrode must not participate. Consumable electrodes (Cu, Zn, C) where anode dissolution is the desired reaction. Cost and availability dominate — graphite is cheap and versatile, DSA requires titanium and ruthenium.

**Cell configurations**:
- **Tank cell**: Simple rectangular tank (concrete or steel-lined). Electrodes hang in electrolyte. Batch or semi-continuous. Used for copper refining. Easy to build and maintain, but large footprint per unit production.
- **Filter press cell**: Flat electrodes and separators clamped together like a stack. Electrolyte flows through channels between plates. Continuous operation, compact, good heat removal. Used for chlor-alkali and advanced water electrolysis. Higher manufacturing precision required.
- **[Membrane cell](../glossary/membrane-cell.md)** (chlor-alkali specific): Ion-exchange membrane (Nafion) replaces diaphragm. Allows Na⁺ through but blocks Cl⁻ and OH⁻. Produces higher-purity NaOH directly at 30-35% concentration. Requires fluoropolymer chemistry.

### Power Supply for Electrolysis

All electrolysis processes require **direct current (DC)**. The conversion from AC grid power to DC is itself a significant engineering challenge.

- **Rectifiers**: Modern systems use silicon diode or thyristor (SCR) rectifiers. For bootstrap: mercury-arc rectifiers (historical, 1920s-1960s) or mechanical rotary converters (AC motor driving DC generator). Simplest: DC generator directly driven by steam engine or water wheel (low efficiency but workable).
- **Voltage and current**: Different processes need different supplies:
  - Chlor-alkali: 200-400V DC at 50-200 kA
  - Aluminum potline: 800-1200V DC at 100-500 kA
  - Water electrolysis: 100-400V DC at 2-20 kA
  - Copper refining: 100-200V DC at 10,000-30,000 A
- **Bus bar design**: Massive copper or aluminum bus bars carry current between rectifier and cells. At 200 kA, even 0.001 Ω resistance dissipates 40 kW as heat. Bus bars must be short, thick, and well-cooled. Typical cross-section: 200-1000 mm² per 1000 A.

### Safety

- **Chlorine gas**: Toxic (IDLH 10 ppm). Fatal at 1000 ppm. Chlor-alkali plants require gas detection, ventilation, emergency scrubbers (NaOH solution absorbs Cl₂), and full-face supplied-air respirators for emergency response. Chlorine is heavier than air — accumulates in low points.
- **Hydrogen gas**: Explosive in air at 4-75% concentration. Ignition energy very low (0.017 mJ). All hydrogen systems must be purged with inert gas (N₂) before introduction of H₂. No open flames, sparks, or static discharge near hydrogen equipment.
- **Molten salt hazards** (aluminum): Bath at 960°C — severe burn risk. Molten aluminum contacting moisture causes explosive steam generation. Carbon dust (anode manufacturing) is a respiratory hazard and explosion risk. Magnetic fields around potlines (100-500 kA) can affect pacemakers and steel tools.
- **Electrical**: All electrolysis uses high DC currents at potentially lethal voltages. Insulation, grounding, and lockout/tagout procedures mandatory. Electrolyte is conductive — wet surfaces near cells are shock hazards.
- **Asbestos** (diaphragm cells): Known carcinogen. Handling asbestos fiber for diaphragm deposition requires respiratory protection, enclosure, and wet methods. Modern plants have replaced asbestos with polymer diaphragms.

### Other Electrolysis Processes

**Sodium production (Downs cell)**:
- Molten NaCl electrolysis at 580-600°C (NaCl-CaCl₂ eutectic mixture lowers melting point from 801°C). Steel cell, carbon anode, iron or copper cathode. 4-6V, 30-40 kA. Products: sodium metal (cathode) + chlorine gas (anode). Na rises to surface (density 0.97 g/cm³), collected under inert atmosphere. CaCl₂ addition (58-59% NaCl / 41-42% CaCl₂) reduces operating temperature below Na boiling point (883°C), preventing sodium vapor loss. Sodium metal used for titanium reduction (Kroll process), organic synthesis, and as coolant in fast breeder nuclear reactors.

**Electroplating**:
- **Principle**: Same as electrorefining but deposits metal onto a substrate for coating (decorative, corrosion-resistant, or functional). Workpiece is the cathode; metal anode dissolves to replenish electrolyte. Common plating metals: chromium (decorative/hard wear, from CrO₃ + H₂SO₄ bath), nickel (corrosion barrier, from NiSO₄ + NiCl₂ + H₃BO₃ bath), zinc (galvanizing, from cyanide or acid zinc baths), copper (electronics, from CuSO₄ + H₂SO₄ or CuCN + KCN baths), gold and silver (electronics, jewelry).
- **Operating conditions**: Low current density (10-500 A/m² depending on metal), near-ambient temperature (25-60°C most baths), cell voltage 0.5-6V. Plating thickness controlled by time and current (Faraday's law: 1 Faraday = 96,485 coulombs deposits 1 equivalent weight of metal).
- **Surface preparation**: Critical step — poor adhesion results from oily or oxidized surfaces. Sequence: degrease (alkaline soak or solvent), acid pickle (remove oxide), acid dip (activate surface), rinse between each step, then plate immediately.

**[Electrowinning](../glossary/electrowinning.md)** (extracting metal from leach solutions):
- Used when metal is dissolved in solution (heap leaching of copper ores, zinc roaster leach). Electrolyte contains metal ions (Cu²⁺, Zn²⁺) in H₂SO₄ solution. Inert anode (Pb-Sn-Ca alloy, oxygen-evolving). Cathode: aluminum or stainless steel blank. Metal plates on cathode, O₂ evolves at anode. Higher voltage than electrorefining (1.8-3.5V per cell vs. 0.3V) because the anode reaction is water oxidation rather than metal dissolution.

### Scale and Economics

Electrolysis is among the most electricity-intensive industrial processes. Approximate energy costs per kg of product:

| Product | Energy (kWh/kg) | Primary Cost Driver |
|---------|-----------------|---------------------|
| Aluminum | 13-15 | Electricity (60-70% of production cost) |
| Chlorine | 2.1-2.5 (per kg Cl₂) | Electricity + brine |
| Hydrogen (alkaline) | 50-55 | Electricity (~70% of cost) |
| Refined copper | 0.25-0.35 | Electricity is minor; labor and capital dominate |
| Sodium | 10-12 | Electricity + heat maintenance |
| Chromium plate | 30-70 | Electricity + chemicals (inefficient deposition) |

Cheap, abundant electricity is the prerequisite for all electrolysis. Without reliable power at competitive rates, none of these processes are economically viable. This constraint is why aluminum smelting historically locates near hydroelectric dams, and why the chlor-alkali industry tracks electricity prices closely.

 ---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*

## Chlor-Alkali Membrane Cell: Detailed Parameters

The membrane cell is the modern standard for chlor-alkali electrolysis, replacing both diaphragm and mercury cells.

**Feed preparation**: Saturated NaCl brine (25-28% NaCl, 310-340 g/L) must be ultra-purified before entering the membrane cell. Calcium and magnesium ions (even at ppm levels) irreversibly damage the Nafion membrane by forming insoluble hydroxides within the membrane structure. Purification sequence: (1) Na₂CO₃ addition to precipitate CaCO₃, (2) NaOH addition to precipitate Mg(OH)₂, (3) BaCO₃ addition if sulfate >5 g/L to precipitate BaSO₄, (4) leaf filter or precoat filter to remove all precipitates, (5) ion exchange polishing (chelating resin) to reduce Ca²⁺ and Mg²⁺ to <20 ppb. Final brine specification: Ca²⁺ + Mg²⁺ < 0.02 mg/L, SO₄²⁻ < 5 g/L, free Cl₂ < 1 mg/L.

**Anode**: Dimensionally stable anode (DSA) — titanium substrate (expanded metal or mesh) coated with 5-15 μm mixed metal oxide layer (RuO₂/IrO₂/TiO₂, typically 60-80 mol% RuO₂). The coating catalyzes chlorine evolution: 2Cl⁻ → Cl₂ + 2e⁻ at ~1.36 V (reversible potential at 25°C). Overpotential on DSA: 30-80 mV at 2-5 kA/m². DSA lifetime: 5-8 years before recoating. Graphite anodes (historical alternative) consume at 2-5 kg per tonne Cl₂ produced (anode carbon oxidizes to CO₂), requiring frequent gap adjustment as the anode thins.

**Cathode**: Nickel or low-carbon steel mesh with catalytic coating (Ni-Al or Raney nickel) to reduce hydrogen overpotential. Hydrogen evolution: 2H₂O + 2e⁻ → H₂ + 2OH⁻ at -0.83 V (reversible). Cathode overpotential on activated Ni: 50-150 mV at 2-5 kA/m². The cathode compartment produces NaOH solution (30-33% concentration) and H₂ gas.

**Membrane**: Perfluorinated sulfonic acid membrane (Nafion or Flemion), 100-200 μm thick. The membrane is a cation exchanger: Na⁺ ions pass through the hydrated sulfonic acid groups, while Cl⁻ and OH⁻ anions are blocked. This selectivity prevents NaCl contamination of the NaOH product and Cl₂/H₂ mixing. Operating temperature 85-95°C (higher temperature reduces cell voltage by improving kinetics and membrane conductivity, but accelerates membrane degradation). Membrane life: 2-4 years, limited by mechanical damage, Ca/Mg fouling, and chemical degradation. Cost: $500-2000 per m² of active area.

**Cell operating conditions**: Cell voltage 2.9-3.5 V (decomposition voltage 2.2 V + overpotentials + membrane resistance + solution resistance + hardware resistance). Current density 2-5 kA/m². Operating temperature 85-95°C. Current efficiency 95-97% (3-5% of current produces O₂ at the anode instead of Cl₂, and some OH⁻ back-migrates through the membrane). Energy consumption: 2,100-2,400 kWh per tonne Cl₂. Individual cell area 1-4 m². Electrolyzer with 50-150 cells in series, drawing 5-30 kA total current at 200-400 V DC.

## SEM Tech Membrane Cell

**[SEM Tech](../glossary/sem-tech.md)** (Salt Electro Mining Technology) is an open-source approach to ion exchange membrane manufacturing, developed by **Robert Karas** (Rowow LLC). The core innovation uses off-the-shelf water softener resin beads, pulverized and dispersed in a PVC/CPVC binder matrix, to form homogeneous ion exchange membranes at **less than $1/sq ft** — compared to $100-400/sq ft for conventional perfluorinated membranes (Nafion).

**Key differences from conventional membrane cells**:
- **Membrane composition**: Pulverized pre-functionalized ion exchange resin (particle size <200μm) in PVC or CPVC matrix. No post-functionalization (sulfonation, amination) required.
- **Manufacturing**: Blender/ball mill to pulverize resin → dissolve PVC/CPVC in solvent (THF, cyclohexanone, or MEK) → mix → spread on surface → dry → peel. All at ambient conditions with household equipment.
- **Membrane cost**: <$1/sq ft (thin spray films can achieve <$1/sq yard) vs $500-2,000/m² for Nafion.
- **Durability**: Months to nearly a year of continuous use at pH 0, ORP >1.5V. Shorter than Nafion (2-4 years) but far cheaper to replace.
- **Applications beyond chlor-alkali**: Closed-loop mining (53 elements extractable), redox flow batteries, fuel cells, water treatment.

**Performance**: >99% metal recovery for many targets. Energy consumption $50-400/ton of ore processed. Lab-demonstrated at 10-50 lb scale (TRL 5). Patent application (not granted), released under CC0 1.0 Universal.

For complete technical details including membrane manufacturing process, cell architecture (CMU/CRU), operating parameters, all 10 patent claims, and comparison tables, see **[SEM Tech: Full Technical Details](sem-tech.md)**.

## Copper Electrorefining: Detailed Parameters

**Electrolyte composition**: CuSO₄·5H₂O (150-200 g/L Cu²⁺, equivalent to 38-50 g/L Cu) + H₂SO₄ (150-200 g/L) in aqueous solution. Temperature 50-55°C (reduces viscosity and resistance, improves Cu²⁺ diffusion). The sulfuric acid increases solution conductivity and prevents CuSO₄ precipitation. Electrolyte density ~1.2 g/mL.

**Current density and voltage**: 200-300 A/m² (cathode current density). Cell voltage only 0.2-0.3 V (very low because the thermodynamic potentials of anode dissolution and cathode deposition are nearly equal). Energy consumption: 250-350 kWh per tonne of refined copper — among the lowest of all electrolytic processes. Daily cathode production: ~0.8 kg Cu per m² of cathode area at 250 A/m².

**Cathode purity**: 99.99%+ Cu. Impurity limits for Grade A copper (LME standard): Ag <15 ppm, As <3 ppm, Sb <2 ppm, Bi <1 ppm, Se <1 ppm, Te <1 ppm, Fe <5 ppm, Pb <5 ppm, Ni <5 ppm, Sn <3 ppm, S <15 ppm, O <20 ppm (for cathode, before melting). Higher purity (99.999%, 5N) achievable with careful anode selection and electrolyte purification, required for electronic applications.

## Faraday's Law Applications

Faraday's first law of electrolysis: the mass of substance deposited or dissolved at an electrode is proportional to the quantity of electricity passed. m = Q × M / (n × F), where m = mass (g), Q = total charge (coulombs), M = molar mass (g/mol), n = number of electrons transferred per ion, F = Faraday constant = 96,485 C/mol.

**Production rate calculations**: For chlor-alkali: Cl₂ production rate = I × M / (n × F) = current × 35.45 / (2 × 96485) = 1.839 × 10⁻⁴ g Cl₂ per ampere-second = 0.662 kg Cl₂ per kA·hour. A cell drawing 200 kA produces 132.4 kg Cl₂ per hour, or 3,178 kg/day. For aluminum: Al production rate = I × 27.0 / (3 × 96485) = 9.328 × 10⁻⁵ g Al per ampere-second = 0.336 kg Al per kA·hour. A potline drawing 300 kA produces 100.7 kg Al per hour, or 2,417 kg/day per cell.

**Energy consumption**: Specific energy = n × F × V_cell / M, where V_cell is the operating voltage. For aluminum at 4.2V: (3 × 96485 × 4.2) / 27.0 = 45,054 J/g = 12.5 kWh/kg. For chlorine at 3.2V: (2 × 96485 × 3.2) / 35.45 = 17,414 J/g = 4.8 kWh/kg Cl₂. These calculations allow direct comparison of process efficiency across different electrolytic industries.

## Electrolysis Plant Design Considerations

**Rectifier selection**: Silicon diode rectifiers are standard for modern electrolysis plants. Input: 3-phase AC at 6-35 kV. Output: DC at the required voltage and current. Rectifier transformer steps down to the cell operating voltage (200-1200V DC depending on process). Rectifier efficiency: 97-99%. Cooling: water-cooled diode heat sinks. Harmonic filtering required on the AC side (rectifiers draw non-sinusoidal current, creating harmonics that affect power quality). Thyristor (SCR) rectifiers provide variable DC output voltage by controlling firing angle, but have lower power factor at partial load.

**Bus bar design**: Current-carrying bus bars (copper or aluminum flat bars) connect rectifier to cell stack and between cells. At 200 kA, even 0.001 Ω resistance dissipates 40 kW as heat. Bus bars must be short, thick, and well-cooled. Copper bus bar: current density 1.0-1.5 A/mm² (above this, excessive heating). Aluminum bus bar: 0.6-0.8 A/mm². Typical cross-section for 200 kA: 200,000 mm² copper (approximately 200 × 1000 mm bar, or multiple bars in parallel). Bolted joints with silver-plated contact surfaces to minimize contact resistance. Thermal expansion accommodated with flexible connectors.

**Cell room ventilation**: Chlor-alkali cell rooms require forced ventilation to prevent chlorine accumulation. Air changes: 6-12 per hour. Chlorine detection: continuous monitoring at low points (Cl₂ is 2.5× heavier than air, accumulates at floor level). Emergency scrubber: standby NaOH scrubber on automatic activation by Cl₂ detector, capable of absorbing the entire cell room chlorine inventory in 30 minutes. The cell room is maintained at slight negative pressure relative to surrounding areas to prevent chlorine escape.

## Electrolysis Environmental Considerations

**Mercury cell legacy**: The mercury cell process (cathode: flowing mercury amalgam, Na-Hg) was historically a major source of mercury pollution. Each tonne of Cl₂ produced lost 2-50 g of mercury to wastewater and air. The Minamata Convention (2017) mandates phaseout of mercury cell chlor-alkali plants. Conversion to membrane cells eliminates mercury emissions entirely. Contaminated sites require soil remediation (activated carbon, ion exchange, or excavation).

**Chlor-alkali hydrogen utilization**: The H₂ byproduct (0.028 tonnes H₂ per tonne Cl₂) is a valuable co-product. Uses: HCl synthesis (H₂ + Cl₂ → 2HCl), fuel for boiler or furnace (lower heating value 120 MJ/kg), hydrogenation reactions in chemical synthesis, or purified for semiconductor use. In many plants, H₂ provides a significant portion of the total site fuel requirement. Failure to utilize H₂ wastes energy and creates a flammable gas disposal problem (flaring).

**Aluminum smelter fluoride emissions**: HF, CF₄, and C₂F₆ emissions from Hall-Héroult cells are controlled by dry scrubbing: alumina (Al₂O₃) is injected into the cell exhaust gas, where it reacts with HF to form aluminum fluoride (AlF₃). The fluoridated alumina is then fed to the cells (closing the fluoride loop). CF₄ and C₂F₆ are formed during anode effects (voltage spikes from low alumina concentration) and are extremely potent greenhouse gases (GWP₁₀₀: CF₄ = 6,630, C₂F₆ = 11,100). Modern potlines minimize anode effects through automated alumina feeding and computer control, reducing PFC emissions to <0.1 kg CF₄ per tonne Al.

## Limitations

- **High electricity consumption**: Electrolysis is inherently energy-intensive. Chlor-alkali membrane cells consume 2,100-2,400 kWh/tonne Cl₂. Aluminum Hall-Héroult cells consume 13,000-15,000 kWh/tonne Al. Copper electrorefining consumes 250-350 kWh/tonne Cu. These processes are viable only where cheap electricity is available.
- **Membrane lifetime and cost**: Perfluorinated membranes (Nafion) for chlor-alkali cost $500-1,000/m² and last 3-7 years. SEM Tech membranes reduce this to <$10/m² but with shorter projected lifetime (0.5-1 year). Membrane failure causes product contamination and requires immediate plant shutdown for replacement.
- **Product purity constraints**: Membrane cell NaOH contains 30-32% NaOH with ~50 ppm NaCl. For some applications (rayon production, certain chemical syntheses), even this low NaCl level is unacceptable, requiring further purification. Diaphragm cells produce 10-12% NaOH with 15% NaCl — far less pure.
- **Anode and cathode degradation**: Dimensionally stable anodes (DSA, RuO₂/IrO₂ on Ti) last 5-8 years in chlor-alkali service. Nickel cathodes last 10+ years but develop roughness that increases hydrogen overvoltage. Electrode replacement is a scheduled maintenance event requiring full cell disassembly.

## See Also

- **[SEM Tech](sem-tech.md)**: Low-cost ion exchange membranes for electrolysis cells
- **[SEM Tech Water Electrolysis](sem-tech-water-electrolysis.md)**: PEM hydrogen production with SEM Tech membranes
- **[Alkalis](alkalis.md)**: NaOH production and applications
- **[Acids](acids.md)**: HCl and acid production linked to chlor-alkali process
- **[Hydrogen and Silane](hydrogen-silane.md)**: Hydrogen as a feedstock for silane and semiconductor gases
- **[Aluminum Production](../metals/aluminum.md)**: Hall-Héroult electrolysis for aluminum
