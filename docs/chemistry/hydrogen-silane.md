# Hydrogen & Silane Production

> **Node ID**: chemistry.hydrogen-silane
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.electrolysis`](electrolysis.md), [`gas-handling.basic`](../gas-handling/basic.md)
> **Enables**: [`metals.powder-metallurgy`](../metals/powder-metallurgy.md), [`silicon.purification`](../silicon/purification.md), [`semiconductor-chemicals`](semiconductor-chemicals.md)
> **Timeline**: Years 25-50
> **Outputs**: hydrogen, silane, trichlorosilane
> **Critical**: Yes — silane (SiH₄) is the primary silicon source for semiconductor CVD processes. Trichlorosilane (SiHCl₃) feeds the Siemens polysilicon process. Ultra-pure hydrogen is required for semiconductor fabrication and ammonia synthesis.

### Problem

Semiconductor manufacturing and ammonia synthesis both require ultra-pure hydrogen and silicon-bearing gases. Silane (SiH₄) is the primary silicon source for CVD deposition; trichlorosilane (SiHCl₃) feeds the Siemens polysilicon process. Neither gas occurs naturally — both must be synthesized from metallurgical-grade silicon through multi-step chemical processes with extreme purity requirements (<1 ppb impurities for semiconductor grade). The gases are pyrophoric, toxic, and corrosive, demanding inert-atmosphere handling at every stage.

### Prerequisites

- [Electrolysis](electrolysis.md) — alkaline water electrolysis for hydrogen production
- [Gas handling](../gas-handling/basic.md) — piping, valves, and inert-atmosphere systems
- [Silicon purification](../silicon/purification.md) — metallurgical-grade silicon as feedstock
- [Refractories and furnaces](../energy/electric-furnaces.md) — high-temperature reactors
- [Chemistry fundamentals](./index.md) — acid-base reactions, distillation, gas laws

### Hydrogen Production

**Electrolysis of water**:
- **Apparatus**: Electrolytic cell with nickel or platinum electrodes. Electrolyte: 20-30% KOH solution (better conductivity than pure water, prevents corrosion of electrodes). Steel cell body. Asbestos or polymer diaphragm separates anode and cathode compartments (prevents H₂ and O₂ mixing).
- **Reactions**: Cathode: 2H₂O + 2e⁻ → H₂ + 2OH⁻. Anode: 2OH⁻ → ½O₂ + H₂O + 2e⁻. Overall: 2H₂O → 2H₂ + O₂.
- **Conditions**: 1.8-2.2 V per cell, 50-80°C, 0.1-3 MPa pressure. Current density 200-400 mA/cm². Stack multiple cells in series for desired production rate.
- **Energy consumption**: ~4-5 kWh per Nm³ H₂ (theoretical minimum 3.0 kWh/Nm³). Production rate proportional to current (Faraday's law: 1 A produces ~0.42 L H₂/hour at STP).
- **Purification**: Pass through palladium membrane (Pd tube heated to 300-400°C — only H₂ diffuses through Pd lattice, all other gases excluded). Or catalytic recombination (remove O₂ traces by reacting with H₂ over platinum catalyst → water, remove water with desiccant). Achieve 99.999%+ purity.

**Strengths**: Produces carbon-free hydrogen when powered by renewable electricity; palladium membrane purification achieves 99.999%+ purity (semiconductor grade); modular — scale by adding cells; O₂ byproduct has value (medical, steelmaking); alkaline electrolysis is mature technology with 60,000+ hour stack lifetime.

**Weaknesses**: 4-5 kWh/Nm³ is 2-3× more expensive than SMR per kg H₂; Pd membrane is expensive and fragile; KOH electrolyte is corrosive; deionized water required (<5 µS/cm); 70% round-trip efficiency limits use as energy storage; Ir/Pt catalysts in PEM variant are scarce and expensive.

**[Steam reforming](../glossary/steam-reforming.md)** (if natural gas or methane available):
- CH₄ + H₂O → CO + 3H₂ (endothermic, 700-900°C, Ni catalyst, 2-3 MPa)
- CO + H₂O → CO₂ + H₂ (water-gas shift, 350-450°C, Fe/Cr oxide catalyst)
- Remove CO₂ with amine scrubber or pressure swing adsorption (PSA). Result: 95-99% H₂.
- Much cheaper than electrolysis if methane is available.

### Steam-Methane Reforming (SMR) — Detailed Process

When natural gas (methane, CH₄) is available, SMR is the dominant industrial route to hydrogen — responsible for ~95% of global H₂ production. The process operates in three main stages:

**Stage 1: Primary reforming (steam reforming)**
- **Reaction**: CH₄ + H₂O → CO + 3H₂ (strongly endothermic, ΔH = +206 kJ/mol)
- **Conditions**: 700-1000°C, 2-3 MPa pressure, Ni-based catalyst packed in vertical nickel-alloy tubes (Incoloy 800 or HK-40). Tubes are heated externally by burning natural gas or refinery off-gas in a top-fired or side-fired furnace.
- **Catalyst**: Nickel pellets or rings supported on ceramic (α-alumina). Sulfur poisons the catalyst — feed gas must be desulfurized to <0.1 ppm S using zinc oxide (ZnO) beds or hydrodesulfurization.
- **Steam-to-carbon ratio**: 3.0-3.5:1 (molar). Excess steam prevents carbon formation (coking) on the catalyst, which would deactivate it. Carbon deposition reaction: 2CO → C + CO₂ (Boudouard reaction) or CH₄ → C + 2H₂.
- **Exit gas composition**: ~10% CH₄ (unconverted), 10% CO, 70% H₂, 10% CO₂ + H₂O. The remaining methane is converted in the secondary reformer (if present) or tolerated in downstream PSA purification.

**Stage 2: Water-gas shift (two-stage)**
- Converts CO to additional H₂: CO + H₂O → CO₂ + H₂ (mildly exothermic, ΔH = -41 kJ/mol)
- **High-temperature shift (HTS)**: 350-450°C, Fe₂O₃/Cr₂O₃ catalyst. Converts bulk of CO. Exit: ~3% CO remaining. Iron-chrome catalyst is robust and tolerant of impurities.
- **Low-temperature shift (LTS)**: 200-250°C, Cu/ZnO/Al₂O₃ catalyst. Converts most remaining CO. Exit: ~0.2-0.3% CO. Copper catalyst is more active at lower temperature but sulfur-sensitive — requires clean feed from HTS.
- The two-stage approach exploits the trade-off: lower temperature favors CO conversion (equilibrium) but slower kinetics. HTS provides fast bulk conversion; LTS achieves deep conversion at lower temperature.

**Stage 3: Purification (Pressure Swing Adsorption)**
- Shift reactor exit gas contains: ~75% H₂, ~20% CO₂, ~0.3% CO, traces of CH₄ and H₂O.
- PSA unit operates at 20-30 atm using multiple (4-12) adsorber beds filled with molecular sieves, activated carbon, and silica gel. Each bed cycles through: adsorption (impurities trapped, pure H₂ passes through at 99.99%+ purity) → depressurization → purge (release adsorbed impurities) → repressurization.
- H₂ recovery: 85-90%. Product purity: >99.99% (4N), up to 99.999% (5N) with optimized cycles.
- Alternative: Amine scrubber (MEA or MDEA solution absorbs CO₂, regenerated by heating) followed by methanation (CO + 3H₂ → CH₄ + H₂O over Ni catalyst at 300°C).

**Overall SMR metrics**:
- Energy consumption: ~10 kWh/kg H₂ (including natural gas feedstock energy).
- CO₂ emissions: ~9 kg CO₂/kg H₂ (from process + combustion). This is the major environmental drawback of SMR — "grey hydrogen."
- With carbon capture (blue hydrogen): CO₂ captured from flue gas and shift reactor exhaust. Capture rate: 85-95%. Adds ~30-50% to cost.
- Scale: Minimum economical unit ~1000 Nm³/h H₂. Large plants produce 100,000+ Nm³/h.

**Alternative: Water electrolysis** (see [Electrolysis](electrolysis.md)):
- 50-55 kWh/kg H₂ (including compression). No CO₂ emissions if electricity is renewable.
- Currently 2-3× more expensive than SMR per kg H₂, but costs declining with cheaper renewable electricity.

### Water Electrolysis — Process Detail

When methane is unavailable or carbon-free hydrogen is required, water electrolysis is the alternative route:

- **[Alkaline electrolysis](../glossary/alkaline-electrolysis.md)** (most mature): 20-30% KOH electrolyte, nickel electrodes, asbestos or Zirfon (PSA-based composite) diaphragm. Cell voltage 1.8-2.2 V, temperature 60-80°C, pressure 1-30 bar. Current density 200-400 mA/cm². Stack lifetime: 60,000-90,000 hours. Production rate scales with electrode area and number of cells — a 1 MW electrolyzer produces ~200 Nm³/h H₂.
- **[PEM electrolysis](../glossary/pem-electrolysis.md)** (higher efficiency, more expensive): Solid polymer electrolyte (Nafion membrane — perfluorosulfonic acid). Platinum catalyst on cathode, iridium oxide on anode. Cell voltage 1.7-2.0 V, current density 1000-4000 mA/cm² (much higher than alkaline). Advantages: compact, rapid load-following (compatible with intermittent renewable electricity), very pure H₂ (no KOH contamination). Disadvantages: requires scarce catalyst materials (Ir, Pt), expensive membrane.
- **Energy**: Thermodynamic minimum for water splitting = 39.4 kWh/kg H₂ (HHV). Real systems: 50-55 kWh/kg including compression and system losses. This means ~70% round-trip efficiency from electricity to H₂ HHV.
- **Water quality**: Deionized water required (<1 µS/cm conductivity for PEM, <5 µS/cm for alkaline). Dissolved minerals cause scaling on electrodes and diaphragm blockage. Water consumption: ~9 L per kg H₂ (stoichiometric) + ~2 L/kg for purification system blowdown.

### Silane Alternative Production Routes

Beyond the standard trichlorosilane route, several alternative paths to silane exist with different trade-offs:

- **[Direct synthesis](../glossary/direct-synthesis.md)** (Si + 2H₂ → SiH₄): Thermodynamically unfavorable at most conditions — equilibrium lies far left. Requires specialized catalyst (none proven industrially). Not a practical route.
- **Disproportionation of dichlorosilane**: 2SiH₂Cl₂ → SiH₄ + SiCl₄ (similar to trichlorosilane route but starting from SiH₂Cl₂, bp 8.3°C). SiH₂Cl₂ itself is produced from SiHCl₃ redistribution. This is actually part of the standard route when optimized.
- **[Magnesium silicide route](../glossary/magnesium-silicide-route.md)** (laboratory): Mg₂Si + 4HCl → 2MgCl₂ + SiH₄. Produces impure silane with phosphine (PH₃) and arsine (AsH₃) contaminants — dangerous and unsuitable for semiconductor-grade material. Only for small-scale/non-electronic applications.
- **Union Carbide process**: Fluidized-bed reactor with metallurgical silicon and HCl at 300-350°C. The SiHCl₃ product undergoes multiple redistribution stages to maximize SiH₄ yield. Overall silicon-to-silane yield: ~15-20% per pass with recycle. This is the industrial standard adapted by major silane producers.

### Silane Production (SiH₄)

**[Process route](../glossary/process-route.md)** (from MG-Si, Silicon stage):
1. **Trichlorosilane synthesis**: MG-Si + 3HCl → SiHCl₃ + H₂ (fluidized bed reactor, 280-350°C, Cu catalyst). SiHCl₃ boils at 31.8°C — distill from higher-boiling SiCl₄ (bp 57.6°C) and lower-boiling gases.
2. **Redistribution reaction**: 4SiHCl₃ → 3SiCl₄ + SiH₄ (catalytic reactor, 60-80°C). Silane (SiH₄) boils at -112°C — cryogenically distill from SiCl₄.
3. **Purification**: Fractional distillation at cryogenic temperatures. Final purification through molecular sieves and catalytic getters (remove trace chlorosilanes, moisture, methane). Purity requirement: 99.9999%+ (6N+) for semiconductor use.

**Properties and handling**:
- Pyrophoric — spontaneously ignites on contact with air (auto-ignition temperature: room temperature or below for impure silane). Burns with intense flame.
- Storage and transport in stainless steel cylinders, under inert gas pressure. Piping: electropolished stainless steel, welded or VCR-type fittings (no threaded connections — leak potential). All lines purged with N₂ or Ar before introducing silane.
- Leak detection: silane sniffers (thermal conductivity sensors). If silane leaks and ignites, water spray to cool surroundings — do not attempt to extinguish burning silane (let it burn off, the alternative is accumulating explosive gas).
- **NEVER** allow silane to accumulate in confined spaces. Even 2-3% concentration in air can auto-detonate.

### Storage & Distribution

**Hydrogen storage**:
- **Compressed gas**: Steel or composite cylinders at 200-700 bar. Simple and widely used. Energy density: 0.8-2.7 MJ/L at 200-700 bar. Heavier than other options per unit energy stored.
- **Metal hydrides**: LaNi₅ (lanthanum-nickel) or FeTi (iron-titanium) alloys absorb H₂ at moderate pressure (2-10 bar), release on heating (50-100°C). Safe — no high-pressure gas. Heavy (2-5% H₂ by weight). Good for stationary storage.
- **Cryogenic liquid H₂**: Liquefy at −253°C (20 K). Density 0.071 kg/L (much higher than compressed gas). Requires vacuum-insulated dewar. Boil-off 0.5-1%/day. Energy cost to liquefy: ~30% of H₂ energy content.

**Silane storage and handling**:
- **Low pressure only**: Store SiH₄ at 2-50 psi (0.1-0.3 MPa) in stainless steel cylinders — NEVER at high pressure. Silane is pyrophoric; high-pressure storage dramatically increases the risk of auto-ignition or detonation if a leak occurs.
- **Cylinder construction**: 316L stainless steel, electropolished interior. Cylinder valve: diaphragm-sealed (no packing gland that could leak). Pressure relief devices designed to vent to safe location (outside, away from ignition sources).
- **Distribution piping**: Electropolished 316L stainless steel with VCR-type face-seal fittings. Welded joints wherever possible. All lines purged with N₂ or Ar before introducing silane — any air in the line will cause immediate ignition at the silane/air interface.
- **Vent systems**: All vent lines from silane equipment routed to a burn box or scrubber. Silane vented to atmosphere will auto-ignite; controlled burning in a vent stack is safer than risking accumulation and detonation.
- **Inventory minimization**: Store only the minimum quantity needed for current production. Silane cylinders in well-ventilated, fire-rated enclosures with continuous gas detection monitoring.

**Pipeline materials**:
- **Hydrogen**: Stainless steel 316L preferred. Carbon steel susceptible to hydrogen embrittlement (H₂ atoms diffuse into steel lattice, cause cracking under stress). Welded joints only — no threaded connections. Design for low stress. For low-pressure distribution: copper or polyethylene tubing acceptable.
- **Silane**: Electropolished stainless steel (316L or 304L) with PTFE-lined valves. VCR-type face-seal fittings — no elastomer O-rings (silane attacks many organics). All lines purged with N₂ or Ar before introducing silane. Minimum dead legs (pockets where gas can stagnate).
- **Leak detection**: Thermal conductivity sensors (silane has different thermal conductivity than air). Hydrogen: catalytic sensors or electrochemical cells. Ultrasonic leak detectors for high-pressure lines. Check all joints with helium mass spectrometer during commissioning.

### Hydrogen Purification Methods

**Pressure Swing Adsorption (PSA)**: The standard method for purifying SMR-derived hydrogen. Four to twelve adsorption vessels in parallel, filled with layered beds: activated carbon (removes H₂O, CO₂), zeolite 5A (removes CH₄, CO), and zeolite 13X (final polishing). Feed gas (SMR output shifted to maximize H₂, CO₂ removed) at 15-30 bar passes through beds — impurities adsorbed, H₂ passes through at 99.97-99.999% purity. Recovery: 75-90% of feed hydrogen. Cycle: 3-10 minutes per vessel. PSA tail gas (containing CO, CO₂, CH₄) used as fuel for the SMR furnace — improves overall thermal efficiency to 70-80%.

**Palladium membrane diffusion**: Hydrogen dissociates on a Pd or Pd-Ag alloy surface, diffuses through the metal lattice as atomic H, and recombines on the permeate side. Only hydrogen passes — impurities blocked. Purity: 99.99999% (7 nines). Flow: proportional to membrane area and √(pressure difference). Operating temperature: 300-400°C. Pd-Ag alloy (23% Ag) preferred — pure Pd suffers hydrogen embrittlement below 300°C. Membrane thickness: 20-100 µm (thinner = higher flux but mechanically fragile). Used for semiconductor-grade hydrogen where ultra-high purity is critical.

**Cryogenic separation**: Not common for H₂ purification alone, but used in syngas plants to recover H₂ and CO separately. Hydrogen (bp -253°C) is the most volatile component — remains as gas while CO, CH₄, CO₂ condense. Purity: 95-98% H₂. Used in refinery and methanol plants.

### Silane Production — Detailed Process Routes

**[Metallurgical-grade silicon route](../glossary/metallurgical-grade-silicon-route.md)** (dominant): (1) MG-Si (98-99% Si, produced from quartz + carbon in electric arc furnace at 1900°C) ground to powder <150 µm. (2) React with HCl gas at 300-400°C in a fluidized bed: Si + 3HCl → SiHCl₃ + H₂ (trichlorosilane, TCS). (3) Purify TCS by distillation (bp 31.8°C) — multiple distillation columns remove Fe, Al, B, P chlorides. (4) Reduce TCS with hydrogen in a Siemens reactor: SiHCl₃ + H₂ → Si + 3HCl. Polysilicon rods heated to 1100-1200°C by direct current; TCS + H₂ gas flows over rods; silicon deposits on rod surface. Rods grow from 8 mm to 150-200 mm over 5-7 days. Energy: 100-200 kWh/kg polysilicon (traditional Siemens).

**Fluidized bed reactor (FBR)**: Alternative to Siemens — TCS or silane gas injected into a fluidized bed of silicon seed particles at 600-800°C. Silicon deposits on seed particles, which grow from 0.1 mm to 1-2 mm and are continuously withdrawn. Energy: 15-30 kWh/kg — 5-10× more efficient than Siemens. REC Silicon, Hemlock Semiconductor operate FBR plants. Challenge: maintaining uniform particle size and avoiding agglomeration.

**Direct silane route**: TCS further converted to silane by catalytic disproportionation: 4SiHCl₃ → SiH₄ + 3SiCl₄ (over amine catalyst, 60-80°C). Silane purified by cryogenic distillation (bp -112°C). Silane is pyrophoric (ignites spontaneously in air) — handling requires extreme care. Used primarily in FBR polysilicon production and semiconductor CVD (chemical vapor deposition) for epitaxial silicon and silicon nitride (Si₃N₄) layers.

### Semiconductor-Grade Gases Beyond Silane

**Dopant gases**: Arsine (AsH₃) and phosphine (PH₃) — extremely toxic (IDLH 3 ppm and 50 ppm respectively). Used in ion implantation and epitaxial doping. Stored in cylinder cabinets with gas detectors, automatic shutoff valves, and scrubbers (thermal oxidation or wet chemical). Boron trifluoride (BF₃) — p-type dopant, less toxic but corrosive.

**Etch gases**: Perfluorocarbons (CF₄, C₂F₆, C₃F₈, C₄F₈) and chlorofluorocarbons (CHF₃, SF₆). Generate reactive fluorine radicals in plasma for silicon and silicon dioxide etching. Environmental concern: very high global warming potential (CF₄: 6500× CO₂). Nitrogen trifluoride (NF₃) increasingly used — can be abated in exhaust with higher destruction efficiency (>99%) than CF₄.

**CVD precursor gases**: Tungsten hexafluoride (WF₆) for tungsten metallization. Tetraethylorthosilicate (TEOS, Si(OC₂H₅)₄) for oxide deposition. Trimethylaluminum (TMA, Al(CH₃)₃) for Al₂O₃ dielectric — pyrophoric. Tetramethylammonium hydroxide (TMAH) for silicon etching.

### Safety

- **Hydrogen flammability**: H₂ has an extremely wide explosive range in air — 4-75% concentration (by volume). The lower explosive limit (LEL) of 4% is the primary concern; even small leaks can create explosive atmospheres in confined spaces. Hydrogen flames are nearly invisible in daylight — detect by thermal imaging, not visual observation. Minimum ignition energy: 0.017 mJ (10× lower than gasoline vapor — static electricity sparks can ignite H₂). All H₂ systems must be electrically bonded and grounded.
- **Silane pyrophoricity**: SiH₄ auto-ignites on contact with air at room temperature or below (if impure). Even 2-3% silane in air can auto-detonate without an ignition source. Silane fires burn intensely (producing SiO₂ fume and H₂). **Cannot be extinguished with water or CO₂** — water reacts with burning silane to produce more H₂; CO₂ provides no suppression effect. The only safe approach: let the fire burn itself out while cooling surrounding equipment with water spray. Stop the silane supply (close source valve) if possible.
- **Confined space hazards**: Both H₂ and SiH₄ pose severe confined-space risks. Silane leak in enclosed area → auto-ignition → pressure wave from rapid combustion. Continuous gas monitoring with automatic shutdown is mandatory for all indoor silane installations. Emergency ventilation at 20+ air changes/hour.
- **Trichlorosilane (SiHCl₃) hazards**: Corrosive liquid (bp 31.8°C — evaporates readily). Fumes are HCl on contact with atmospheric moisture. Skin and respiratory burns. Store in sealed, vented containers. Full chemical suit and self-contained breathing apparatus (SCBA) for spill response.

### Quality Analysis

- **Gas chromatography (GC)**: Separate gas mixture on packed column (molecular sieve or porous polymer), detect with thermal conductivity detector (TCD). Quantifies impurities to ppm levels. Essential for H₂ purity (N₂, O₂, CO, CO₂, CH₄ contaminants) and SiH₄ purity (Si₂H₆, Si₃H₈, chlorosilanes, hydrocarbons).
- **Dew point measurement**: Quantifies moisture content. Aluminum oxide or capacitive sensor. Moisture is critical contaminant — causes oxidation in semiconductor processes. H₂ dew point must be below −70°C (<2.6 ppm H₂O).
- **Oxygen analyzer**: Electrochemical or zirconia sensor. O₂ in H₂ must be <1 ppm for semiconductor use.
- **Purity grades**: Semiconductor-grade H₂ requires >99.9999% (6N) purity. Silane for CVD requires >99.9% (3N) minimum, preferably >99.99% (4N). Each "N" represents an order of magnitude reduction in total impurities.
- **Mass spectrometry**: For the most critical purity verification (especially SiH₄), quadrupole mass spectrometry detects impurities at ppb (parts per billion) levels. Can distinguish SiH₄ (mass 32) from O₂ (also mass 32) by fragmentation pattern. Required for semiconductor-grade qualification of silane batches.

### Silane Production — Expanded Process Routes

**[Metallurgical route](../glossary/metallurgical-route.md)** (dominant industrial path, from MG-Si to SiH₄):
- Step 1: React MG-Si powder (<150 µm) with anhydrous HCl gas at 300°C in a fluidized bed reactor over copper catalyst (1-5% Cu deposited from CuCl₂ solution onto silicon surface). Si + 3HCl → SiHCl₃ + H₂ (trichlorosilane, TCS). Copper promotes selective TCS formation over SiCl₄. Conversion: ~90% TCS, ~10% SiCl₄ by-product.
- Step 2: Purify TCS by fractional distillation (bp 31.8°C). Multiple columns remove metal chlorides (FeCl₃, AlCl₃, BCl₃, PCl₃) to below ppb levels. Boron and phosphorus chlorides are the most critical to eliminate because B and P are electrically active in silicon and would poison device performance at parts-per-trillion concentrations in the final wafer.
- Step 3: Redistribute TCS to silane. Two temperature regimes: catalytic redistribution over amine catalyst at 60-80°C (better selectivity, slower kinetics), or thermal redistribution at 400-500°C (no catalyst needed, faster but broader by-product spectrum). Reaction: 4SiHCl₃ → SiH₄ + 3SiCl₄. The SiCl₄ by-product recycles to the fluidized bed or sells as feedstock for fumed silica production.
- Step 4: Cryogenic distillation separates SiH₄ (bp -112°C) from SiCl₄ (bp 57.6°C) and residual chlorosilanes. Multiple stages achieve 6N+ purity (99.9999%).

**[Direct synthesis route](../glossary/direct-synthesis-route.md)** (simpler, lower yield): Si + 2H₂ → SiH₄ at 200-300°C and 200-300 bar pressure with copper catalyst. Thermodynamically unfavorable at standard conditions, but high pressure shifts the equilibrium toward the product. Yield: 5-15% per pass, requiring extensive recycle of unreacted hydrogen. Lower yield than the chlorosilane route but simpler equipment (no chlorosilane handling, no cryogenic distillation). The high compression energy cost (200-300 bar) is the main drawback. Potentially attractive for bootstrap production where chlorosilane infrastructure is unavailable.

### Silane Physical Properties and Safety

**Physical constants**: Molecular weight 32.12 g/mol. Boiling point -112°C. Melting point -185°C. Gas density at STP: 1.11 kg/m³ (slightly lighter than air). Liquid density at boiling point: 680 kg/m³. Pyrophoric: ignites spontaneously in air at concentrations below 1%. Auto-ignition occurs at room temperature or below for impure silane. The flame is pale blue and hard to see in daylight.

**Occupational exposure**: TLV (threshold limit value) 5 ppm TWA (8-hour time-weighted average). Chronic exposure above 5 ppm causes respiratory irritation and potential lung damage. At this concentration, silane is below its pyrophoric threshold, but the margin is thin.

**Explosive limits and detection**: LEL (lower explosive limit) 1.4% in air (14,000 ppm). UEL (upper explosive limit) near 100% in pure oxygen. The gap between the TLV (5 ppm) and the LEL (14,000 ppm) is large, but gas detection must trigger early because silane can accumulate rapidly from a leaking fitting. Flammable gas sensors (catalytic bead or infrared) set to alarm at 1% LEL (140 ppm) provide adequate warning time. Install sensors at ceiling level (silane is slightly lighter than air) and at known leak points (valve packing, VCR fittings, cylinder connections).

**Piping and containment**: Electropolished 316L stainless steel tubing with VCR face-seal fittings throughout. Flash-back arrestors (sintered metal elements that quench flame propagation) installed on all connections between silane supply and process tools. Lines nitrogen-purged before introducing silane and after shutting off flow. Any air in the line causes immediate ignition at the silane/air interface.

**Abatement systems**: Two options for silane exhaust treatment. Burn box: oxidizing furnace at 800-1000°C converts SiH₄ to SiO₂ fume and H₂O, which are then filtered. Used for continuous vent streams. Wet scrubber: 5-20% NaOH solution in a packed-column scrubber absorbs silane and any chlorosilane by-products, converting them to sodium silicate and sodium chloride. Used for batch venting and emergency relief. Most installations use both in series.

### Silane Storage and Distribution

**Cylinder storage**: Silane stored in 316L stainless steel cylinders at 150 bar (2,200 psi). Standard cylinder: 44 L water capacity, containing ~6 kg silane. Cylinders equipped with pressure relief devices (rupture disc) venting to the abatement system, not to atmosphere. Cylinder valve: diaphragm-sealed (no packing gland leak path).

**Gas cabinet requirements**: Cylinders housed in ventilated gas cabinet with 200 fpm (1 m/s) face velocity exhaust, constructed from non-combustible materials with self-closing doors and continuous gas monitoring. Quantity limited to 1-2 cylinders per cabinet to limit potential release volume. Cabinet exhaust routed to the abatement system, not to general building exhaust. Cylinder changeover uses dual-cylinder manifolds with pneumatic valves for automatic switchover, purging both connections with N₂ before opening silane valves.

**Fluidized bed reactor polysilicon deposition**: Silane is the preferred feedstock for FBR polysilicon production. SiH₄ injected into a fluidized bed of silicon seed particles at 600-700°C decomposes on contact: SiH₄ → Si + 2H₂. Seed particles grow from 0.1 mm to 1-2 mm and are continuously withdrawn as granular polysilicon. Energy consumption: 15-30 kWh/kg, compared to 100-200 kWh/kg for Siemens rod reactors. The granular product flows freely and loads easily into CZ crucibles, unlike the fragile rod segments from Siemens process.

### Silane Quality Grades and Analysis

**Purity requirements by application**: Semiconductor-grade silane requires 6N+ (99.9999%) purity. The most critical contaminants are oxygen (as SiH₃OCH₃ or SiH₃OH, target <100 ppb), moisture (H₂O, target <50 ppb), higher silanes (Si₂H₆, Si₃H₈, target <10 ppm total), and chlorosilanes (SiH₃Cl, SiH₂Cl₂, target <1 ppm). Metallic contaminants (Fe, Cu, Ni from piping) are controlled to <1 ppb each by electropolished 316L stainless steel delivery systems.

**Analytical methods**: Gas chromatography with thermal conductivity detection quantifies chlorosilanes and higher silanes to ppm levels. Fourier transform infrared spectroscopy (FTIR) detects moisture and oxygen-containing impurities to ppb levels in real time. Atmospheric pressure ionization mass spectrometry (APIMS) provides the ultimate sensitivity: sub-ppb detection of trace metallic and organic contaminants in silane gas streams. For bootstrap production, GC-TCD is sufficient for process control.

**Silane vs TCS for polysilicon production**: Silane offers higher silicon deposition rate per unit energy in FBR reactors because the decomposition reaction (SiH₄ → Si + 2H₂) is simpler than the TCS reduction (SiHCl₃ + H₂ → Si + 3HCl) and produces no corrosive by-products. However, silane's pyrophoric nature makes handling more hazardous. TCS is a liquid at room temperature (bp 31.8°C), easier to store and transport, but produces HCl during deposition, requiring corrosion-resistant reactor internals. The choice between silane and TCS feedstock depends on whether the polysilicon producer prioritizes energy efficiency (silane) or handling safety (TCS).

---

**Chlorosilane Handling Infrastructure**: The TCS route generates byproduct SiCl4 (1.0-1.5 kg per kg SiH4). SiCl4 is corrosive liquid (bp 57.6C, density 1.48 g/cm3) fuming in moist air. Storage: glass-lined or PTFE-lined tanks, N2 blanketed, secondary containment 110% tank volume. SiCl4 recycling: react with H2 at 1000-1200C to regenerate TCS, or hydrolyze to fumed silica (SiCl4 + 2H2O -> SiO2 + 4HCl). HCl byproduct absorbed in water for reuse in TCS synthesis.

**Safety Systems for Silane Facilities**: Continuous monitoring: catalytic bead sensor (0-100% LEL, LEL = 1.4% SiH4 in air) plus infrared (0-1000 ppm), alarm at 25% LEL. Emergency shutdown: automatic valve closure, ventilation boost to 10x normal flow. Fire suppression: dry chemical Purple K (potassium bicarbonate) - do NOT use water on silane fires. Abatement: burn box at 800-1000C decomposes SiH4 to Si + 2H2 then oxidizes H2. Emergency response: evacuate 100m radius for release, 300m for cylinder rupture.

**Bootstrap Gas Infrastructure**: Minimum semiconductor gases needed: (1) H2 at 6N purity via electrolysis plus Pd membrane purification, (2) SiH4 at 3N via TCS redistribution, (3) N2 at 5N via air separation PSA or cryogenic, (4) O2 at 4N co-produced with N2, (5) Ar at 4N from air at 0.93% concentration. Typical costs: H2 $5-10/kg, SiH4 $50-100/kg, N2 $0.10-0.30/m3, O2 $0.15-0.40/m3, Ar $2-5/m3. Total gas cost for small fab processing 1000 wafers/month: approximately $50,000-100,000/month.
**Trichlorosilane Purification Detail**: Raw TCS from the fluidized bed reactor contains impurities: methyltrichlorosilane (bp 66.4C), dichlorosilane (bp 8.2C), silicon tetrachloride (bp 57.6C), and boron/phosphorus chlorides (BCI3 bp 12.5C, PCl3 bp 76.1C). Fractional distillation in a multi-column system separates these: Column 1 removes lights (DCS, BCl3) at overhead temperature 8-30C, Column 2 removes heavies (SiCl4, PCl3) at bottom temperature 60-80C, Column 3 produces specification TCS at overhead 31.8C with purity >99.9%. Reflux ratio 10-20:1 required for sharp separation. Boron is the most critical impurity — target <0.1 ppb in final polysilicon, requiring BCl3 removal to <1 ppb in TCS feed.

**Silane Decomposition for Polysilicon**: SiH4 decomposes exothermically at 600-700C on heated silicon seed rods (similar to Siemens TCS process but at lower temperature): SiH4 -> Si + 2H2, deltaH = -34 kJ/mol. Deposition rate 3-8 micrometers/min, energy consumption 30-50 kWh/kg polysilicon (significantly lower than Siemens TCS route at 100-200 kWh/kg). The lower temperature reduces energy cost but silane's pyrophoric nature makes the process more hazardous. Fluidized bed reactor (FBR) alternative: decompose SiH4 on silicon seed particles 100-500 micrometers at 600-700C in a fluidized bed, producing granular polysilicon directly without rod cutting. FBR energy: 25-40 kWh/kg, continuous operation, but product purity slightly lower (metallic impurities 10-100x higher than rod-based deposition due to wall interactions).
**Argon Recovery and Recycling**: Argon is used in large quantities for CZ crystal pulling (20-60 L/min continuous flow) and as inert atmosphere for various high-temperature processes. At $2-5/m3, argon cost is significant for continuous operations. Recovery from CZ exhaust: cool exhaust gas, remove H2 and CO by catalytic oxidation, compress remaining gas (mostly Ar + N2), cryogenic distillation separates Ar (bp -186C) from N2 (bp -196C). Recovery efficiency 90-95%, energy cost for recovery $0.50-1.00/m3 Ar, versus $2-5/m3 for fresh argon. For bootstrap operations, simple once-through argon use is acceptable initially; recovery systems are justified at consumption >100 m3/day.

**Hydrogen Energy Applications Beyond Semiconductors**: Hydrogen has broader bootstrap applications: (1) reducing agent for metal ore processing (WO3 + 3H2 -> W + 3H2O at 700-1000C for tungsten production), (2) hydrogenation of vegetable oils and fats (H2 + unsaturated oil at 150-200C, 1-5 bar over Ni catalyst), (3) ammonia synthesis feedstock (N2 + 3H2 -> 2NH3 at 400-500C, 150-300 bar over Fe catalyst, consuming ~90% of industrial H2 production), (4) fuel cell power generation (H2 + 0.5O2 -> H2O, 0.7V per cell, 40-60% electrical efficiency, PEM type operates at 60-80C). Each application requires different purity grades: fuel cells need 99.99% (CO <10 ppm poisons Pt catalyst), ammonia needs 98%+ (N2 mixed anyway), metal reduction needs 99%+.
**Hydrogen Embrittlement**: Steel exposed to H2 at elevated temperature or pressure absorbs atomic hydrogen into the crystal lattice, causing embrittlement. High-strength steels (>700 MPa yield) are most susceptible. Prevention: use low-strength steels for H2 service (ASTM A106 Grade B for piping, maximum hardness 22 HRC for pressure vessels), avoid hardened welds (post-weld heat treatment at 620-650C for 1 hour per 25mm thickness), limit H2 exposure temperature to <200C for carbon steel. For high-pressure H2 storage (>100 bar), austenitic stainless steels (304L, 316L) are immune to hydrogen embrittlement but cost 3-5x more than carbon steel. Copper and aluminum are also immune to hydrogen embrittlement and are acceptable for low-pressure hydrogen distribution lines.

**Trichlorosilane vs Silane Route Summary**: The TCS-to-silane route involves more unit operations (fluidized bed chlorination, multi-column distillation, catalytic redistribution, cryogenic separation) but produces a feedstock (SiH₄) that deposits polysilicon more efficiently in FBR reactors. The direct TCS route (reducing TCS with H₂ in Siemens reactors) has fewer process steps but higher energy consumption per kg of polysilicon. For bootstrap semiconductor production starting with limited infrastructure, the direct TCS/Siemens route is the lower-capital starting point, with silane/FBR technology added later as production scales beyond ~500 tonnes/year.
**Water Electrolyzer Types**: Alkaline electrolysis (AEL) uses 25-30% KOH electrolyte at 60-90C, non-noble metal electrodes (Ni), produces H2 at 99.5-99.9% purity, energy consumption 4.5-5.5 kWh/Nm3, stack lifetime 60,000-90,000 hours. Proton exchange membrane (PEM) uses solid polymer electrolyte (Nafion membrane) at 50-80C, noble metal catalysts (Pt cathode, Ir/IrO2 anode), higher current density 1-3 A/cm2 vs 0.2-0.5 for AEL, produces H2 at 99.99% purity directly, energy 4.0-5.0 kWh/Nm3, but membrane cost $500-1000/m2 and limited Ir availability constrain scaling. Solid oxide electrolysis (SOEC) at 700-900C uses ceramic electrolyte (YSZ), can co-electrolyze H2O + CO2 for syngas production, electrical efficiency up to 90% (LHV) with waste heat integration, but thermal cycling degradation limits lifetime to 10,000-20,000 hours.
For bootstrapping, alkaline electrolysis is the clear choice: proven technology since 1800, no noble metal dependency, longest lifetime, lowest cost ($1000-2000/kW installed), and 99.5% purity sufficient for most applications (further purified with Pd membrane if needed for semiconductor use).

## Limitations

- **Pyrophoric hazards**: Silane (SiH₄) ignites spontaneously in air at concentrations above 2-3% — no ignition source needed. Trichlorosilane (TCS) also ignites on air contact. These materials demand inert-atmosphere handling (N₂ or Ar purged systems) at every stage: production, purification, transport, and use. A single SiH₄ leak can cause a facility-destroying explosion.
- **Polysilicon energy cost**: Siemens reactor polysilicon production consumes 80-120 kWh/kg of polysilicon — among the most energy-intensive manufacturing processes. Fluidized bed reactor (FBR) technology reduces this to 15-25 kWh/kg but produces lower-purity silicon with higher carbon content. For bootstrap semiconductor production, the energy demand is a major infrastructure challenge.
- **Ultra-purification difficulty**: Semiconductor-grade polysilicon requires impurity levels below 1 ppb for most elements (10⁻¹⁰ atomic fraction). Achieving this from metallurgical-grade silicon (98-99% purity) requires multiple chemical conversion and distillation steps. Each step introduces yield loss and contamination risk.
- **Chlorosilane corrosion**: TCS, DCS, and STC are corrosive and hydrolyze to HCl and silicic acid on contact with moisture. Equipment must be stainless steel 316L (minimum) with welded connections — no threaded fittings. Leaks produce HCl gas, attacking both equipment and personnel.

### Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| H₂ purity below 99.999% | Pd membrane failure or O₂ trace in product | Check Pd membrane integrity; verify catalytic recombination stage; replace desiccant |
| Silane leak (spontaneous ignition) | Fitting leak or seal failure | Evacuate area; shut supply valve; N₂ purge system; never use flame to detect leaks (use thermal camera) |
| TCS distillation poor separation | Column flooding or wrong reflux ratio | Reduce boil-up rate; increase reflux ratio; check for water ingress (corrosion source) |
| Siemens reactor silicon deposits non-uniform | Filament temperature too low or gas flow uneven | Increase filament current (target 1100°C); verify gas inlet distribution; clean reactor walls |
| Electrolyzer voltage rising | Electrode fouling or membrane degradation | Clean electrodes; replace diaphragm; check KOH concentration (target 25-30%) |
| Hydrogen embrittlement in steel piping | Carbon steel exposed to high-pressure H₂ | Replace with 304L/316L stainless steel; limit carbon steel to <200°C and low-pressure service |

## See Also

- [SEM Tech Water Electrolysis](sem-tech-water-electrolysis.md) — green hydrogen production for polysilicon manufacturing
- [Dopant and Etch Gases](dopant-etch-gases.md) — gas delivery and abatement systems for semiconductor fabs
- [Vacuum Systems](../gas-handling/vacuum.md) — vacuum technology for CVD deposition
- [Electrolysis](electrolysis.md) — alkaline water electrolysis for hydrogen production
- [Silicon Purification](../silicon/purification.md) — polysilicon production from TCS
- [Powder Metallurgy](../metals/powder-metallurgy.md) — hydrogen-reduction of metal powders

[← Back to Chemistry](index.md)
