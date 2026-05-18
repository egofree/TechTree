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

