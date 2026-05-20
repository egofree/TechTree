# Dopant & Etch Gases

> **Node ID**: chemistry.dopant-etch-gases
> **Domain**: Chemistry
> **Timeline**: Years 30-70
> **Outputs**: dopant_gases, etch_gases, fluorine

### Dopant Gases

**Phosphine (PH₃)**:
- **Synthesis**: White phosphorus + KOH + H₂O → PH₃ + KPH₂O (boiling phosphorus with strong base). Or Ca₃P₂ + 3H₂O → 2PH₃ + 3Ca(OH)₂ (calcium phosphide + water).
- **Purity**: Distill from reaction mixture (PH₃ bp -87.7°C). Dilute in H₂ or N₂ to ppm-level concentrations for semiconductor use. Use commercially-supplied cylinders with 100-1000 ppm PH₃ in H₂ (dramatically safer than handling pure phosphine).
- **Toxicity**: Lethal at 50-100 ppm. Immediately Dangerous to Life or Health (IDLH) at 50 ppm. Symptoms: headache, nausea, pulmonary edema at low exposure; death at higher concentrations. Detect with electronic PH₃ monitors (electrochemical sensors), colorimetric tubes, or paper impregnated with silver nitrate (turns black in PH₃). **Zero tolerance for leaks.**

**Arsine (AsH₃)**:
- **Synthesis**: Zn₃As₂ + 6HCl → 2AsH₃ + 3ZnCl₂. Or Na₃As + 3H₂O → AsH₃ + 3NaOH. Generate as needed, do not store.
- **Toxicity**: MORE toxic than PH₃. IDLH at 3 ppm. Causes hemolysis (destruction of red blood cells), kidney failure, death. Even brief exposure at 100+ ppm is rapidly fatal. Same handling protocols as PH₃ but more stringent.
- **Dilution strategy**: Always use pre-diluted cylinders (50-500 ppm AsH₃ in H₂). Minimize total inventory. Exhaust gas abatement: burn in dedicated combustion chamber → arsenic oxide particulates captured in HEPA + scrubber.

**Diborane (B₂H₆)**:
- **Synthesis**: 3NaBH₄ + 4BF₃ → 3NaBF₄ + 2B₂H₆ (sodium borohydride + boron trifluoride). Generate as needed.
- **Toxicity**: IDLH at 15 ppm. Flammable (pyrophoric in some concentrations). Same rigorous handling as PH₃/AsH₃.

**Exhaust gas abatement** (critical safety system):
- All dopant gas exhaust lines connect to dedicated abatement system. Burn exhaust gases at 800-1000°C (thermal oxidation). Resulting oxides captured: As₂O₃, P₂O₅, B₂O₃ — solid particulates trapped in HEPA filters, water-soluble compounds in wet scrubbers (NaOH solution). Scrubber water tested for heavy metals before discharge. Spent HEPA filters disposed as hazardous waste.

### Etch Gases

**Chlorine (Cl₂)**:
- From chlor-alkali electrolysis (Chemistry). Compress into steel cylinders. Purity 99.5%+ for semiconductor use (further purified by distillation — Cl₂ bp -34°C).
- Used for etching silicon, aluminum, and many metals. Dry etch: Cl₂ + Si → SiCl₄ (volatile, pumped away). Selective etching — Cl₂ etches silicon but not SiO₂ (or vice versa depending on conditions).

**Tetrafluoromethane (CF₄)** and **Sulfur hexafluoride (SF₆)**:
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

**Fluorine-based etching chemistry**: Silicon etching relies on generation of atomic fluorine radicals in plasma: CF₄ + e⁻ → CF₃· + F· + e⁻. Fluorine radicals react with silicon: Si + 4F· → SiF₄ (volatile, bp -86°C). Etch rate depends on F· concentration, ion energy, and substrate temperature. Selectivity (etching Si vs SiO₂) controlled by gas chemistry: adding O₂ to CF₄ increases F· concentration (etches Si faster), adding CHF₃ or C₄F₈ increases polymer deposition on SiO₂ (protecting oxide — selective oxide etch). **Bosch process** for deep silicon etching (MEMS, TSV): alternates etch step (SF₆ plasma → isotropic Si etch) and passivation step (C₄F₈ plasma → fluorocarbon polymer deposition) at 10-100 Hz cycling. Achieves vertical sidewalls with scalloping of 50-200 nm per cycle. Etch rate: 5-20 µm/min. Aspect ratio: up to 30:1.

**Chlorine-based etching**: Cl₂, BCl₃, HCl used for aluminum metallization etching. Chlorine radicals etch aluminum: 2Al + 6Cl· → 2AlCl₃ (volatile above 180°C). BCl₃ serves dual purpose: Cl source and native oxide (Al₂O₃) removal (BCl₃ + Al₂O₃ → AlCl₃ + B₂O₃). Aluminum etch requires heating the wafer chuck to 40-70°C to volatilize AlCl₃. Corrosion concern: residual Cl on etched surfaces attacks aluminum — post-etch passivation with CHF₃ or H₂O rinse required.

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

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
