# Dopant & Etch Gases

> **Node ID**: chemistry.dopant-etch-gases
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.electrolysis`](electrolysis.md), [`chemistry.hydrogen-silane`](hydrogen-silane.md)
> **Enables**: [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`silicon.crystal-growth`](../silicon/crystal-growth.md), [`vlsi-scaling.eda-design`](../vlsi-scaling/eda-design.md)
> **Timeline**: Years 30-70
> **Outputs**: dopant_gases, etch_gases, fluorine
> **Critical**: Yes — dopant gases (PH₃, AsH₃, B₂H₆) enable semiconductor doping, and etch gases (CF₄, Cl₂, SF₆) enable pattern transfer in photolithography. Without these gases, semiconductor manufacturing is impossible.

### Dopant Gases

**Phosphine (PH₃)**:
- **Synthesis**: White phosphorus + KOH + H₂O → PH₃ + KH₂PO₂ (boiling phosphorus with strong base). Or Ca₃P₂ + 6H₂O → 2PH₃ + 3Ca(OH)₂ (calcium phosphide + water).
- **Purity**: Distill from reaction mixture (PH₃ bp -87.7°C). Dilute in H₂ or N₂ to ppm-level concentrations for semiconductor use. Use commercially-supplied cylinders with 100-1000 ppm PH₃ in H₂ (dramatically safer than handling pure phosphine).
- **Toxicity**: Lethal at 50-100 ppm. Immediately Dangerous to Life or Health (IDLH) at 50 ppm. Symptoms: headache, nausea, pulmonary edema at low exposure; death at higher concentrations. Detect with electronic PH₃ monitors (electrochemical sensors), colorimetric tubes, or paper impregnated with silver nitrate (turns black in PH₃). **[Zero tolerance for leaks.](../glossary/zero-tolerance-for-leaks.md)**

**Arsine (AsH₃)**:
- **Synthesis**: Zn₃As₂ + 6HCl → 2AsH₃ + 3ZnCl₂. Or Na₃As + 3H₂O → AsH₃ + 3NaOH. Generate as needed, do not store.
- **Toxicity**: MORE toxic than PH₃. IDLH at 3 ppm. Causes hemolysis (destruction of red blood cells), kidney failure, death. Even brief exposure at 100+ ppm is rapidly fatal. Same handling protocols as PH₃ but more stringent.
- **Dilution strategy**: Always use pre-diluted cylinders (50-500 ppm AsH₃ in H₂). Minimize total inventory. Exhaust gas abatement: burn in dedicated combustion chamber → arsenic oxide particulates captured in HEPA + scrubber.

**Diborane (B₂H₆)**:
- **Synthesis**: 3NaBH₄ + 4BF₃ → 3NaBF₄ + 2B₂H₆ (sodium borohydride + boron trifluoride). Generate as needed.
- **Toxicity**: IDLH at 15 ppm. Flammable (pyrophoric in some concentrations). Same rigorous handling as PH₃/AsH₃.

**[Exhaust gas abatement](../glossary/exhaust-gas-abatement.md)** (critical safety system):
- All dopant gas exhaust lines connect to dedicated abatement system. Burn exhaust gases at 800-1000°C (thermal oxidation). Resulting oxides captured: As₂O₃, P₂O₅, B₂O₃ — solid particulates trapped in HEPA filters, water-soluble compounds in wet scrubbers (NaOH solution). Scrubber water tested for heavy metals before discharge. Spent HEPA filters disposed as hazardous waste.

### Etch Gases

**Chlorine (Cl₂)**:
- From chlor-alkali electrolysis (Chemistry). Compress into steel cylinders. Purity 99.5%+ for semiconductor use (further purified by distillation — Cl₂ bp -34°C).
- Used for etching silicon, aluminum, and many metals. Dry etch: Cl₂ + Si → SiCl₄ (volatile, pumped away). Selective etching — Cl₂ etches silicon but not SiO₂ (or vice versa depending on conditions).

**[Tetrafluoromethane (CF₄)](../glossary/tetrafluoromethane-cf.md)** and **Sulfur hexafluoride (SF₆)**:
- CF₄: C + 2F₂ → CF₄ (carbon + fluorine gas, 300-400°C). Or chloroform + HF → CF₄ (catalytic fluorination over Cr₂O₃ catalyst).
- SF₆: S + 3F₂ → SF₆ (sulfur + fluorine gas). Burn sulfur in fluorine atmosphere.
- Both used as plasma etch gases. In RF plasma, CF₄ dissociates → CF₃• + F•. Fluorine radicals etch SiO₂: SiO₂ + 4F• → SiF₄↑ + O₂. Adding O₂ to CF₄ plasma increases fluorine radical concentration (etches silicon faster). Adding CHF₂ to CF₄ plasma increases polymer deposition (selectively etches oxide over silicon).
- Fluorine gas (F₂) itself is also needed — produce by electrolysis of KF·2HF (potassium bifluoride melt) at 70-100°C in Monel or nickel cell. F₂ is the most reactive element — attacks almost everything. Handle in nickel or Monel metal equipment only.

**Gas purification techniques**:
- **Catalytic getters**: Heated metal (zirconium, titanium, or nickel alloy) pellets react with impurity gases (O₂, H₂O, CO, CO₂). Gas passes over heated getter bed → impurities chemically bound. For removing trace oxygen and moisture from inert gases.
- **Molecular sieves**: Synthetic zeolite beads (3Å, 4Å, 5Å, 13X pore sizes). Adsorb molecules smaller than pore diameter. 3Å removes water. 4Å removes H₂O, CO₂, H₂S. 13X removes larger molecules. Regenerate by heating to 200-300°C under vacuum or dry gas purge. Use in pairs — one adsorbing, one regenerating (twin-tower system).
- **Cryogenic trapping**: Cool gas stream to very low temperature (liquid N₂ temperature, -196°C). Impurities condense/freeze out while target gas remains volatile. For final ultra-purification.
- **Palladium membrane**: For H₂ purification only. Pd alloy tube heated to 300-400°C. Only hydrogen diffuses through Pd lattice — produces 99.999999% pure H₂.

### Gas Distribution System

**Piping**: Electropolished 316L stainless steel tubing. Internal surface roughness <0.5 μm Ra (electropolishing removes micro-roughness where particles and contaminants could trap). Orbital-welded joints (automated TIG welding in inert atmosphere — no internal weld beads or discoloration). VCR-type face-seal fittings for connections to equipment. Minimum dead legs (no T-connections pointing down where gas stagnates).

**Valves**: Stainless steel diaphragm valves or bellows valves (no packed glands — packing wears and leaks). pneumatic-actuated for automated control. Manual override for emergency.

**Mass flow controllers (MFCs)**: Thermal measurement of gas flow. Heated sensor tube — gas flowing carries heat downstream. Temperature difference between upstream and downstream sensors proportional to mass flow. Control valve adjusts to maintain setpoint. Accuracy ±1% of full scale. Calibrate for each specific gas (heat capacity differs). Essential for semiconductor process control — gas flow determines deposition rates, etch rates, doping levels.

### Dopant Gases — Detailed Chemistry

**Arsine (AsH₃)**: Used for n-type doping of silicon in ion implantation (10¹⁴-10¹⁶ atoms/cm² dose) and epitaxial deposition. Molecular weight 77.95, boiling point -62.5°C. Pyrophoric but the primary hazard is extreme toxicity — hemolytic agent that destroys red blood cells. IDLH (immediately dangerous to life and health): 3 ppm. TLV-TWA: 0.005 ppm (5 ppb). Detrimental effects appear hours after exposure — insidious. Stored at <1000 ppm concentration in H₂ or N₂ balance in dedicated gas cabinets with continuous AsH₃ monitoring (electrochemical sensors, detection limit <10 ppb). Exhaust abatement: thermal oxidation (combustion chamber at 900°C) or wet scrubbing (NaOCl solution oxidizes AsH₃ to soluble arsenate, AsO₄³⁻). Arsenic-containing waste classified as hazardous — requires specialized disposal.

**Phosphine (PH₃)**: n-type dopant, less toxic than arsine (IDLH 50 ppm, TLV-TWA 0.3 ppm) but still very hazardous. Boiling point -87.7°C. Used in ion implantation and as a phosphorus source in InP and GaAs epitaxy. Auto-ignition temperature: 38°C (can spontaneously ignite at room temperature if concentration in air >1.8%). Stored diluted (100-1000 ppm in H₂). Abatement: similar wet scrubbing with NaOCl or H₂O₂. Smells like decaying fish at low concentrations — serves as warning but olfactory fatigue occurs rapidly.

**Boron trifluoride (BF₃)**: p-type dopant gas. Molecular weight 67.81, boiling point -100.3°C. Non-flammable but highly corrosive — reacts violently with water producing HF and boric acid. Used in ion implantation for p-type wells and in borophosphosilicate glass (BPSG) reflow processes. BF₃ + 3H₂O → H₃BO₃ + 3HF. The HF byproduct is itself extremely hazardous. Stored in stainless steel or Monel cylinders. Delivery lines: electropolished 316L stainless steel with VCR fittings. Abatement: dry scrubbing (activated alumina or calcium hydroxide) — dry process avoids generating HF-laden wastewater.

**Diborane (B₂H₆)**: p-type dopant for epitaxial silicon and polysilicon deposition. Pyrophoric (ignites spontaneously in air). Highly toxic (TLV-TWA 0.1 ppm). Decomposes at room temperature — must be used promptly after generation or stored diluted. Generated on-site by reacting NaBH₄ with H₃PO₄ when needed, or purchased as 1-5% in H₂. Used in PECVD (plasma-enhanced CVD) for boron-doped films.

### Etch Gases — Process Details

**Fluorine-based etching chemistry**: Silicon etching relies on generation of atomic fluorine radicals in plasma: CF₄ + e⁻ → CF₃· + F· + e⁻. Fluorine radicals react with silicon: Si + 4F· → SiF₄ (volatile, bp -86°C). Etch rate depends on F· concentration, ion energy, and substrate temperature. Selectivity (etching Si vs SiO₂) controlled by gas chemistry: adding O₂ to CF₄ increases F· concentration (etches Si faster), adding CHF₃ or C₄F₈ increases polymer deposition on SiO₂ (protecting oxide — selective oxide etch). **[Bosch process](../glossary/bosch-process.md)** for deep silicon etching (MEMS, TSV): alternates etch step (SF₆ plasma → isotropic Si etch) and passivation step (C₄F₈ plasma → fluorocarbon polymer deposition) at 10-100 Hz cycling. Achieves vertical sidewalls with scalloping of 50-200 nm per cycle. Etch rate: 5-20 µm/min. Aspect ratio: up to 30:1.

**Chlorine-based etching**: Cl₂, BCl₃, HCl used for aluminum metallization etching. Chlorine radicals etch aluminum: 2Al + 6Cl· → 2AlCl₃ (volatile above 180°C). BCl₃ serves dual purpose: Cl source and native oxide (Al₂O₃) removal (2BCl₃ + Al₂O₃ → 2AlCl₃ + B₂O₃). Aluminum etch requires heating the wafer chuck to 40-70°C to volatilize AlCl₃. Corrosion concern: residual Cl on etched surfaces attacks aluminum — post-etch passivation with CHF₃ or H₂O rinse required.

### Gas Distribution Systems

**Piping**: Electropolished 316L stainless steel tubing, orbital-welded joints (no mechanical connections in gas lines). Internal surface roughness Ra <0.25 µm to prevent particle generation and gas adsorption. Tube bends: minimum 3× OD radius to prevent flow restriction and particulate generation. All lines passivated with fluorine or oxygen before service.

**Mass flow controllers (MFCs)**: Thermal MFCs (measure heat transfer from a heated sensor tube — flow rate proportional to heat carried away). Range: 1 sccm to 300 slm. Accuracy: ±1% of full scale. Response time: <1 second. For corrosive gases (Cl₂, HCl, WF₆): all-wetted parts in Hastelloy C-276 or Inconel. For pyrophorics (SiH₄, B₂H₆): MFCs with purge capability (N₂ purge before/after gas flow to prevent residue buildup).

**Gas cabinet safety**: Automatic shutoff valve (normally closed pneumatic valve — closes on power loss, gas detection alarm, or fire alarm). Exhaust ventilation: 100+ ft³/min flow through cabinet. Continuous gas monitoring: toxic gas sensors at cabinet exhaust, room ambient, and exhaust stack (three-tier monitoring). Flashback arrestors on hydrogen lines. Excess flow valves (shut off if flow exceeds setpoint — indicates line break). Emergency abort button (closes all cylinder valves, purges lines with N₂).

### Safety & Hazards

- **Hydrofluoric acid (HF)**: Dissolves bone. Lethal at low exposure. ANTIDOTE: Calcium gluconate gel — must be on hand before ANY HF handling.
- **Phosgene (COCl₂)**: WWI weapon. Lethal at 3 ppm, delayed onset. Sealed systems only.
- **Silane (SiH₄)**: Pyrophoric, ignites in air. Cannot extinguish with water/CO₂.
- **Arsine (AsH₃)**: TLV 50 ppb; lethal at low ppm concentrations. Continuous monitoring required.


---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*

## Silane and CVD Precursor Gases

**Silane (SiH₄)**: The primary silicon source for chemical vapor deposition (CVD) of polysilicon and silicon dioxide thin films. Pyrophoric: ignites spontaneously on contact with air (auto-ignition temperature below room temperature for pure silane). Stored at 1-5% concentration in N₂ or H₂ balance for safety, or handled as pure gas in dedicated, purged stainless steel lines with continuous leak monitoring. Thermal decomposition on heated surfaces (575-700°C): SiH₄ → Si + 2H₂. Used for polysilicon gate deposition, amorphous silicon (a-Si) solar cells, and silicon nitride (with NH₃) PECVD films. Purity: 99.9999% (6N) for semiconductor-grade, with <1 ppb each metallic impurity.

**Dopant gas concentrations**: Phosphine (PH₃) provides n-type doping. Typical ion implantation doses: 10¹⁵-10²⁰ atoms/cm³. PH₃ diluted to 100-1000 ppm in H₂ for CVD doping. Diborane (B₂H₆) for p-type: same concentration range. Arsine (AsH₃) for n-type with higher activation efficiency than PH₃ in some applications. All three are regulated to TLV values measured in ppb, requiring continuous monitoring with electrochemical sensors or FTIR gas analyzers.

## Etch Gas Chemistry in Detail

**Silicon etching with CF₄ plasma**: In a 13.56 MHz RF plasma, CF₄ dissociates: CF₄ + e⁻ → CF₃· + F· + e⁻. Fluorine radicals attack silicon: Si + 4F· → SiF₄ (volatile, bp -86°C). Base etch rate ~100 nm/min. Adding O₂ (10-30%) to CF₄ increases F· concentration by reacting with CF₃· to form COF₂ and CO₂, releasing additional fluorine. Etch rate increases 2-5×. Adding H₂ or CHF₃ to CF₄ decreases F· concentration (HF formation) and increases CFₓ polymer deposition, which selectively protects Si over SiO₂. This chemistry enables oxide-selective etching.

**Deep silicon etching (Bosch process)**: Alternating etch/passivate cycles for high-aspect-ratio structures (MEMS, through-silicon vias). Etch step: SF₆ plasma generates F· radicals for isotropic Si etch (etch rate 5-20 μm/min). Passivation step: C₄F₈ plasma deposits a thin (~10 nm) fluorocarbon polymer (CF₂)ₙ on all surfaces. Next etch step's ion bombardment removes polymer from horizontal surfaces while protecting sidewalls. Cycle frequency 5-20 Hz. Result: vertical sidewalls with periodic scallops (50-200 nm roughness per cycle). Aspect ratios up to 30:1 achievable.

**Aluminum etching**: Cl₂ and BCl₃ plasma etching of aluminum interconnects. Cl₂ at 200-500 W RF power generates Cl· radicals: 2Al + 6Cl· → 2AlCl₃ (volatile above 180°C). BCl₃ serves as both Cl source and oxide scavenger: 2BCl₃ + Al₂O₃ → 2AlCl₃ + B₂O₃ removes the native aluminum oxide that would otherwise block etching. Wafer chuck heated to 40-70°C to promote AlCl₃ volatilization. Post-etch corrosion from residual chlorine is a critical concern, requiring immediate passivation (CHF₃ plasma or H₂O rinse) before air exposure.

## Gas Delivery Infrastructure

**Tubing specifications**: Electropolished 316L stainless steel tubing, 1/4 inch OD (6.35 mm) standard for gas distribution. Internal surface electropolished to Ra <0.25 μm to minimize particle generation and gas adsorption. Orbital-welded joints (automated TIG welding in argon purge) ensure smooth, crevice-free internal surfaces with no weld beads. VCR (metal gasket face seal) fittings for connections to valves, MFCs, and process equipment. All tubing passivated by flowing fluorine or high-purity oxygen before first use to create a stable chromium oxide surface layer.

**Mass flow controllers (MFCs)**: Thermal-type MFCs measure gas flow by detecting heat transfer from a heated sensor tube. Two resistance temperature detectors (RTDs) wrap the sensor tube upstream and downstream of a microheater. Gas flow carries heat downstream; the temperature difference is proportional to mass flow. A control valve (solenoid or piezoelectric) adjusts to maintain the setpoint. Accuracy ±1% of full scale, repeatability ±0.2%. Calibrated for specific gases (each gas has different heat capacity). Range: 1 sccm to 300 slm full scale. Response time <1 second.

**Gas cabinet design**: Each toxic or pyrophoric gas cylinder housed in a dedicated gas cabinet with: (1) automatic shutoff valve (normally closed pneumatic, failsafe on power loss or gas detection alarm); (2) exhaust ventilation at 100+ ft³/min through HEPA and scrubber; (3) continuous toxic gas monitoring (electrochemical sensors at cabinet exhaust, room ambient, and building exhaust stack); (4) fire suppression system; (5) excess flow valve that shuts off supply if flow exceeds setpoint (indicates line break); (6) emergency abort button that closes all cylinder valves and purges lines with N₂.

## Exhaust Gas Abatement

**Burn box (thermal oxidation)**: Exhaust gases containing silane, phosphine, diborane, or arsine pass through a combustion chamber at 900-1000°C (hydrogen flame or electrically heated). Silane oxidizes to SiO₂ particulate: SiH₄ + 2O₂ → SiO₂ + 2H₂O. Dopant hydrides oxidize to their respective oxides: PH₃ → P₂O₅, AsH₃ → As₂O₃, B₂H₆ → B₂O₃. Solid oxide particulates captured in HEPA filters (99.97% efficient at 0.3 μm). Water-soluble oxides (P₂O₅, B₂O₃) removed in downstream wet scrubbers.

**Wet scrubbers**: Packed-bed scrubbers using NaOH solution (5-15%) remove acid gases (HF, HCl, Cl₂, SiF₄) from exhaust streams. Gas flows upward through packing material while scrubbing solution flows downward. Mass transfer: acid gas + NaOH → sodium salt + water. For fluorine-containing gases: HF + NaOH → NaF + H₂O. Scrubber solution monitored for pH (maintain >10 for efficient absorption) and fluoride concentration. Spent scrubber solution treated for fluoride removal before discharge.

**Catalytic abatement**: Perfluorocarbons (CF₄, C₂F₆, SF₆) are extremely stable and resist thermal decomposition below 1000°C. Catalytic abatement at 900-1000°C over a proprietary catalyst (often platinum-group metal on alumina support) with added fuel gas (H₂ or CH₄) decomposes these compounds. Destruction efficiency >95%. Required because CF₄ has a global warming potential (GWP) of 7,390 over 100 years. Alternative: plasma abatement using RF or microwave plasma to fragment CFₓ molecules at lower bulk temperature.

## Process Integration: Gas Panel Design

A typical semiconductor etch or CVD tool requires 6-12 gas lines converging at the process chamber. The gas panel (gas box) is a densely packed assembly of valves, MFCs, filters, and pressure regulators mounted on an electropolished stainless steel panel.

**Gas line layout**: Each gas follows the path: cylinder → gas cabinet (with automatic shutoff valve) → stainless steel trunk line → gas panel inlet valve → particle filter (0.003 μm sintered metal) → mass flow controller → check valve (prevent backflow) → process chamber. All lines are heat-traced (electric heating cable, 60-80°C) for gases that condense at room temperature (TEOS bp 168°C, TMA boils at -3°C but can decompose to solids in cold lines).

**Leak testing**: After installation or maintenance, the entire gas distribution system is leak-tested. Helium leak detection: pressurize the system with helium at 1.5× operating pressure, scan all joints, welds, and fittings with a helium mass spectrometer sniffer. Acceptable leak rate: <1×10⁻⁹ atm·cc/sec for toxic gas lines. Pressure decay test: pressurize system, isolate, monitor pressure for 24 hours. Any decay indicates a leak.

**Material compatibility**: 316L stainless steel is standard for most gases. Hastelloy C-276 (nickel-molybdenum-chromium alloy) for halogen gases (Cl₂, HCl, HF, HBr) that cause pitting corrosion in stainless steel. Monel (nickel-copper alloy) for fluorine gas. PTFE or PFA (perfluoroalkoxy) gaskets and diaphragms for corrosive service. Nickel or nickel-plated components for silane service (silane can react with copper).

## Safety Systems for Toxic Gas Handling

**Gas detection hierarchy**: (1) Point detectors (electrochemical cells) at each gas cabinet exhaust, room ambient locations, and building exhaust stack. Response time <30 seconds for arsine and phosphine at TLV concentrations. (2) Area monitoring: open-path infrared detectors spanning the gas storage room ceiling. (3) Personal monitoring: badge dosimeters or portable monitors worn by personnel entering gas areas.

**Emergency response**: Toxic gas alarm triggers three automatic actions: (1) close the emergency shutoff valve at the gas cabinet (isolates the cylinder), (2) activate exhaust scrubbers at maximum capacity, (3) sound audible/visual alarms in the affected area. Personnel evacuate immediately. Trained responders in supplied-air respirators (SCBA) investigate and mitigate. Cyanide antidote kits (amyl nitrite, sodium nitrite, sodium thiosulfate) staged near HCN areas. Calcium gluconate gel staged near HF areas.

**Electrostatic discharge (ESD) protection**: Silane and hydrogen gas lines must be grounded to prevent static accumulation that could ignite a leak. All-metal connections with confirmed electrical continuity. No plastic tubing in pyrophoric gas service. Gas cabinets and panels electrically bonded to building ground grid.

## Gas Purity Specifications

**Semiconductor-grade gas purity**: Each process gas has specific impurity limits defined by SEMI standards. For silane (SiH₄) used in polysilicon deposition: SiH₄ >99.9999% (6N purity), with maximum impurity levels: O₂ <0.5 ppm, H₂O <1.0 ppm, hydrocarbons <1.0 ppm, heavy metals (Fe, Cu, Ni) <1 ppb each, particulates <10 particles/mL ≥0.1 μm. Impurities in the gas translate directly to defects in the deposited film: oxygen and water cause SiO₂ inclusions in polysilicon, metals cause electronic traps, particles cause pinholes.

**Moisture contamination**: Water vapor is the most pervasive contaminant in gas systems. Even 1 ppm H₂O in silane causes SiO₂ formation in CVD films. Moisture sources: residual water adsorbed on internal surfaces of tubing and fittings (desorbed when gas flows), permeation through elastomer seals, and leaks (air ingress brings moisture). Prevention: electropolished internal surfaces (reduces adsorption sites), heated lines (prevents condensation), all-metal seals (VCR copper or nickel gaskets, no elastomers), and thorough purging with dry N₂ before introducing process gas.

**Particle contamination**: Particles in gas streams cause device defects (shorts, opens, or pattern distortion in lithography). Particle sources: mechanical wear of valves and regulators, corrosion products, and gas-phase particle formation (silane can decompose to form Si particles in heated lines). Filtration: 0.003 μm sintered nickel or stainless steel filters at the point of use (last component before the process chamber). Filter integrity verified by bubble point test (pressure at which gas first passes through the wetted filter pore). All gas system components cleaned in a cleanroom-compatible process: solvent degrease, ultrasonic clean in DI water, dry in HEPA-filtered N₂, double-bag in cleanroom-compatible packaging.

## Wafer Fab Gas Distribution Architecture

**Bulk gas vs specialty gas**: Bulk gases (N₂, O₂, Ar, H₂, He) are produced on-site by air separation or electrolysis and distributed through a central manifold to all process tools. Distribution at 0.5-1.0 MPa through 1/2 to 1 inch OD stainless steel header pipes. Specialty gases (SiH₄, PH₃, CF₄, SF₆, Cl₂) are supplied in cylinders (size 44L, containing 5-20 kg of gas at 2-10 MPa) located in dedicated gas cabinets, one cylinder per gas per tool.

**Automatic gas cabinet operation**: The cylinder valve is opened by a pneumatically actuated stem. Gas flows through the cabinet's pressure regulator, shutoff valve, MFC, and into the trunk line to the tool. When the cylinder empties (pressure drops below setpoint), the cabinet automatically switches to the reserve cylinder and triggers an alarm for cylinder change. Changeover time: <30 seconds, maintaining uninterrupted gas supply. Cylinder change procedure: close empty cylinder valve, vent cabinet, disconnect empty cylinder, connect full cylinder, purge with N₂ (3× volume purge), open new cylinder valve, verify gas purity before returning to service.

## Chemical Vapor Deposition Gases

**TEOS (tetraethyl orthosilicate, Si(OC₂H₅)₄)**: Liquid source for SiO₂ CVD deposition. Delivered as a liquid in stainless steel bubbler (0.5-2.0 L). Carrier gas (N₂ or Ar) bubbles through the heated liquid (kept at 40-60°C to maintain sufficient vapor pressure, ~2-5 Torr at 40°C). TEOS decomposes on the heated wafer surface at 650-750°C: Si(OC₂H₅)₄ → SiO₂ + 4C₂H₄ + 2H₂O. Advantages over SiH₄ + O₂ CVD: excellent step coverage (conformal deposition in high-aspect-ratio features), lower stress in the deposited film, and non-pyrophoric (safer handling). Used for inter-metal dielectric (IMD) in semiconductor manufacturing.

**Tungsten hexafluoride (WF₆)**: Source gas for tungsten CVD, used for contact and via filling in semiconductor interconnect. WF₆ is a liquid at room temperature (bp 17°C), stored in stainless steel cylinders. Reduced by silane (2WF₆ + 3SiH₄ → 2W + 3SiF₄ + 6H₂, nucleation step) then by hydrogen (WF₆ + 3H₂ → W + 6HF, bulk fill). Deposition temperature 300-400°C. WF₆ is highly corrosive: all wetted parts must be Monel or Inconel. HF byproduct scrubbed in NaOH wet scrubber.

**Organometallic sources**: Metal-organic CVD (MOCVD) for compound semiconductors uses liquid or solid organometallic precursors stored in temperature-controlled bubblers. Trimethylgallium (TMGa, (CH₃)₃Ga) for GaAs and GaN. Trimethylaluminum (TMAl, (CH₃)₃Al) for AlGaAs and AlN. Trimethylindium (TMIn, (CH₃)₃In) for InGaAsP. MOCVD growth of GaN for LEDs: TMGa + NH₃ at 1000-1100°C on sapphire or SiC substrate. Growth rate: 1-3 μm/hour. Precise control of gas flow rates (via MFCs) and bubbler temperatures (±0.1°C) determines layer composition and thickness.

## Plasma Etch System Integration

**RF power delivery**: 13.56 MHz is the standard industrial, scientific, and medical (ISM) frequency for plasma generation. An RF generator (300-3000 W for single-wafer etch tools) delivers power through an impedance matching network (automatically tuned to maintain <5% reflected power) to the cathode (wafer chuck). The matching network contains a variable capacitor and inductor that transform the plasma impedance to the 50 Ω output impedance of the RF generator. Poor matching causes reflected power that damages the RF generator and produces unstable plasma.

**Wafer chuck temperature control**: The electrostatic chuck (ESC) holds the wafer by Coulombic attraction (dielectric layer on the chuck surface, 500-1500 V DC applied between chuck electrode and wafer). Helium backside cooling: He gas (2-10 Torr) flows between the wafer backside and chuck surface, providing thermal contact for heat removal. Chuck temperature controlled at -20°C to +80°C (depending on the etch process) by recirculating heat transfer fluid through internal channels. Temperature uniformity across the wafer: ±1°C, critical for etch uniformity.

**Endpoint detection**: Optical emission spectroscopy (OES) monitors plasma light emission during etching. As the etch reaches the interface between layers, the emission intensity of key species changes (e.g., CO emission at 483 nm drops when photoresist etch is complete, or SiF emission at 440 nm drops when silicon etch reaches the buried oxide). Real-time endpoint detection stops the etch at the precise moment, preventing overetch damage to underlying layers. Accuracy: ±2-5% of the remaining film thickness at the endpoint signal onset.

## Etch Process Parameters

**Etch rate measurement**: Film thickness measured before and after etching using spectroscopic ellipsometry or reflectometry. Typical etch rates: polysilicon in CF₄/O₂ plasma: 100-300 nm/min; SiO₂ in CHF₃/CF₄ plasma: 50-150 nm/min; photoresist in O₂ plasma: 200-500 nm/min; aluminum in Cl₂/BCl₃ plasma: 300-800 nm/min. Etch uniformity across a 300 mm wafer: ±3-5% (center-to-edge variation controlled by gas distribution, electrode design, and temperature uniformity).

**Selectivity**: The ratio of etch rate of the target material to the etch rate of the mask or underlying layer. Critical selectivity values: SiO₂-to-photoresist selectivity 3-6:1 in fluorocarbon plasma (resist erodes slower than oxide due to fluorocarbon polymer protection). Si-to-SiO₂ selectivity 10-50:1 in Cl₂/HBr plasma (chlorine etches silicon much faster than oxide). Aluminum-to-SiO₂ selectivity >20:1 in Cl₂/BCl₃ plasma. Higher selectivity allows thinner mask layers and less risk of damaging underlying structures during overetch.

**Aspect ratio dependent etching (ARDE)**: As feature aspect ratio (depth/width) increases, etch rate decreases because reactive species have difficulty diffusing into and reaction products have difficulty diffusing out of high-aspect-ratio features. A via with 10:1 aspect ratio etches 30-60% slower than an open-field area. ARDE is managed by: (1) ion-enhanced etching (directional ion bombardment assists vertical transport), (2) pulsed plasma (allows time for product outgassing between pulses), (3) high-temperature etching (increases volatile product desorption). The Bosch process (alternating etch/passivate) was specifically developed to manage ARDE in deep silicon etching.

## Plasma Etch System Configuration

**Etch chamber construction**: The process chamber is typically fabricated from aluminum (6061-T6 or similar alloy) with internal surfaces anodized or coated with ceramics (Al₂O₃, Y₂O₃) for corrosion resistance. Chamber volume: 10-50 liters for single-wafer tools. Pumping port connects to a turbo-molecular pump (500-2000 L/s throughput) backed by a dry scroll pump, achieving base pressure <1×10⁻⁶ Torr. Pressure during etching: 5-100 mTorr, controlled by a throttle valve between the chamber and the turbo pump. Pressure measurement: capacitance manometer (0-1000 mTorr range, ±0.5% accuracy).

**Gas panel integration**: Each etch process uses 4-8 gases, each with its own MFC and shutoff valve. The gas panel (gas box) is a separate enclosure, typically 0.5-1.0 m³ volume, housing all MFCs, valves, filters, and pressure transducers. Gas lines from the panel to the chamber are 1/4" OD electropolished 316L stainless steel, heated to 80-120°C for gases that condense at room temperature. Gas switching time: <2 seconds from one gas to another (critical for the Bosch process, which alternates SF₆ and C₄F₈ every 5-10 seconds). The gas panel is purged with N₂ when not in active use to prevent contamination and moisture accumulation.

**Chamber cleaning**: After each wafer, the chamber walls accumulate polymer deposits (from fluorocarbon etch gases) that must be removed. In-situ plasma cleaning: O₂ plasma (500 W, 30 seconds) oxidizes organic polymer deposits to CO₂ and H₂O, which are pumped away. Periodic wet cleaning (every 500-2000 wafers or when etch rates drift): vent the chamber, wipe internal surfaces with IPA-dampened cleanroom wipers, inspect for buildup, and replace consumable parts (showerhead, focus ring, chamber liner). Chamber condition is monitored by tracking etch rate, uniformity, and particle counts over time.

## Chemical Mechanical Polishing Gases and Slurries

**CMP slurry chemistry**: Not a gas, but a critical wet chemical process in semiconductor manufacturing. CMP (chemical mechanical polishing) planarizes wafer surfaces between metal deposition and etching steps. Oxide CMP slurry: colloidal silica (SiO₂ particles 30-70 nm) suspended in KOH solution (pH 10-11), used for SiO₂ planarization. Metal CMP slurry: alumina (Al₂O₃) or silica abrasives in oxidizing solution (H₂O₂, Fe(NO₃)₃, or KIO₃) for copper, tungsten, or aluminum polishing. The chemical component softens the metal surface, the abrasive mechanically removes it. Removal rate: 100-500 nm/min for oxide CMP, 200-1000 nm/min for copper CMP. Planarization is essential for multilayer interconnect: without CMP, each metal layer would amplify the topography of the layer below, making photolithography impossible beyond 2-3 metal layers.

**Post-CMP cleaning**: After polishing, the wafer surface is contaminated with slurry particles and metal ions that must be completely removed. Cleaning sequence: (1) PVA brush scrubbing with dilute NH₄OH (1-2%) at 20-40°C to remove particles, (2) megasonic cleaning (0.8-1.6 MHz acoustic energy in DI water) to dislodge sub-micron particles, (3) Marangoni drying (isopropanol vapor condenses on wafer surface, creating surface tension gradient that pulls water off the surface, leaving a particle-free, water-mark-free surface). Post-CMP clean is a critical yield-limiting step: a single remaining slurry particle can cause a short circuit between adjacent metal lines.

## Ion Implantation Gases

**Implantation process**: Dopant gases (PH₃, AsH₃, B₂H₆, BF₃) are ionized in a plasma source, accelerated through a magnetic mass analyzer (selects the desired ion species by charge-to-mass ratio), then accelerated to high energy (1 keV to several MeV) and scanned across the wafer surface. Implant dose: 10¹¹-10¹⁶ atoms/cm² (determines dopant concentration in the semiconductor). Implant energy: 1 keV to 5 MeV (determines the depth of the implanted layer, from 10 nm to several μm). Beam current: 1 μA to 30 mA (higher current = higher throughput but more wafer heating).

**Photoresist outgassing**: During ion implantation, the photoresist mask is bombarded by high-energy ions, breaking polymer chains and releasing volatile organic species (H₂, CO, CO₂, CH₄, low molecular weight hydrocarbons). This outgassing can deposit carbon films on the ion source electrodes, destabilizing the plasma and reducing beam current. High-current implants (>5 mA) require frequent source cleaning. Hardened photoresist (deep UV crosslinked) produces less outgassing than standard novolac resist. After implantation, the resist is stripped by oxygen plasma ashing (O₂ plasma at 200-300°C, 5-30 minutes) followed by wet clean (H₂SO₄/H₂O₂ piranha or RCA clean).

## Vacuum System Requirements

**Etch chamber pumping**: A typical plasma etch chamber requires 500-2000 L/s pumping speed to maintain process pressure (5-100 mTorr) while gas flows at 50-500 sccm. Turbo-molecular pump (TMP): rotor spinning at 40,000-60,000 RPM with multiple blade stages that transfer momentum to gas molecules, preferentially directing them toward the exhaust. Backed by a dry scroll pump (15-30 L/s) that maintains the TMP foreline pressure below 0.5 Torr. Pump-down time from atmosphere to base pressure (<1×10⁻⁶ Torr): 15-30 minutes. Leak rate specification: <1×10⁻⁹ Torr·L/s (verified by rate-of-rise test: isolate the pump, measure pressure increase per minute).

## Contamination Control in Gas Systems

**Particles in gas lines**: Particles generated by valve actuation (metal wear from diaphragm valves), gas-phase nucleation (silane decomposition forming Si particles), and corrosion products can transport to the process chamber and cause device defects. Point-of-use filtration: 0.003 μm sintered metal filter as the last component before the chamber. Filter integrity verified by bubble point test. Gas line purging protocol: before introducing a new gas, flow N₂ at 10× pipe volume to sweep out residual gas and particles. After maintenance, bake-out gas lines at 100-150°C under N₂ purge for 4-8 hours to desorb moisture from internal surfaces.

## Limitations

- **Ultra-high purity requirements**: Semiconductor-grade gases require purity of 99.999-99.9999% (5N-6N), with metallic impurities below 1 ppb. Achieving this purity demands multiple purification stages (distillation, adsorption, membrane separation, gettering) and ultra-clean cylinder preparation. The purification infrastructure rivals the gas production plant in cost and complexity.
- **Toxic gas handling infrastructure**: PH₃, AsH₃, B₂H₆, and SiH₄ require dedicated, segregated gas cabinets with continuous monitoring, automated emergency shutdown, exhaust gas abatement, and emergency scrubber systems. The safety infrastructure can cost $50,000-200,000 per gas cabinet — often exceeding the cost of the gas delivery system itself.
- **Exotic materials of construction**: Fluorine, ClF₃, NF₃, and WF₆ require nickel, Monel, or Hastelloy piping and components — standard stainless steel corrodes rapidly. Cylinder valves use nickel-plated or PTFE-packed stems. Gas panels for corrosive gases are 3-10× more expensive than for inert gases.
- **Supply chain concentration**: Many specialty gases are produced by a small number of suppliers (2-4 globally for electronic-grade silane, germane, and dopant hydrides). Supply disruptions affect all semiconductor fabs simultaneously.

## See Also

- **[Hydrogen and Silane](hydrogen-silane.md)**: Silane production and pyrophoric safety
- **[Vacuum Systems](../gas-handling/vacuum.md)**: Vacuum pumps for etch and deposition chambers
- **[Gas Handling Basics](../gas-handling/basic.md)**: Piping, valves, and gas distribution infrastructure
- **[Packaging and Testing](packaging-testing.md)**: Post-fabrication IC testing and reliability
- **[SEM Tech](sem-tech.md)**: Membrane technology for gas purification applications

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
