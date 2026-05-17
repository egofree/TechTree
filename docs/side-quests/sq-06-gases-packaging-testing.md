# SQ 6: Specialty Gases, Consumables, Packaging &amp; Testing

**Starts**: Phase 5-8
**Priority**: Critical for semiconductor fabrication — the fab doesn't work without these.

## Problem

Semiconductor fabrication requires ultra-pure gases, specialized consumables, and packaging/testing infrastructure that are often overlooked in simplified tech trees. Without these, even perfect lithography produces non-functional chips.

## Technologies &amp; Systems

### Air Separation — Bulk Inert Gas Production

**Linde fractional distillation of liquid air**:
- **Principle**: Air is 78% N₂ (bp -196°C), 21% O₂ (bp -183°C), 0.93% Ar (bp -186°C). Cool air until it liquefies, then fractionally distill at cryogenic temperatures.
- **Air preparation**: Compress atmospheric air to 5-6 MPa. Remove water (desiccant beds — silica gel or activated alumina) and CO₂ (molecular sieve or NaOH scrubber — CO₂ would freeze and plug equipment at cryogenic temperatures). Filter particulates.
- **Cooling**: Compressed, cleaned air enters counter-current heat exchanger — cooled by outgoing cold nitrogen and oxygen product streams. Further cooled by expansion through throttle valve (Joule-Thomson effect: real gas cools when expanding at temperatures below its inversion temperature) or expansion engine (adiabatic expansion does work → larger temperature drop).
- **Distillation column**: Double-column design. Lower column at ~0.5 MPa (bp of N₂ at this pressure ~ -177°C). Upper column at ~0.1 MPa. Air enters between columns. N₂ (lower boiling point) rises as vapor, O₂ (higher boiling point) descends as liquid. Argon accumulates at an intermediate point — draw sidestream to separate argon column.
- **Products**:
  - **Nitrogen** (99-99.99%): Used as inert blanket gas, carrier gas, purge gas. Store as compressed gas or liquid N₂ in vacuum-insulated dewar (Dewar flask — double-walled vessel, vacuum between walls, silvered inner wall for radiation shielding. Evaporation rate: 0.5-2% per day).
  - **Oxygen** (95-99.5%): For steelmaking, welding, medical use, oxidation processes.
  - **Argon** (99-99.999%): Critical for CZ crystal growth (inert atmosphere prevents silicon oxidation and reactions with crucible). Also for welding shielding gas, sputtering.

### Hydrogen Production

**Electrolysis of water**:
- **Apparatus**: Electrolytic cell with nickel or platinum electrodes. Electrolyte: 20-30% KOH solution (better conductivity than pure water, prevents corrosion of electrodes). Steel cell body. Asbestos or polymer diaphragm separates anode and cathode compartments (prevents H₂ and O₂ mixing).
- **Reactions**: Cathode: 2H₂O + 2e⁻ → H₂ + 2OH⁻. Anode: 2OH⁻ → ½O₂ + H₂O + 2e⁻. Overall: 2H₂O → 2H₂ + O₂.
- **Conditions**: 1.8-2.2 V per cell, 50-80°C, 0.1-3 MPa pressure. Current density 200-400 mA/cm². Stack multiple cells in series for desired production rate.
- **Energy consumption**: ~4-5 kWh per Nm³ H₂ (theoretical minimum 3.0 kWh/Nm³). Production rate proportional to current (Faraday's law: 1 A produces ~0.42 L H₂/hour at STP).
- **Purification**: Pass through palladium membrane (Pd tube heated to 300-400°C — only H₂ diffuses through Pd lattice, all other gases excluded). Or catalytic recombination (remove O₂ traces by reacting with H₂ over platinum catalyst → water, remove water with desiccant). Achieve 99.999%+ purity.

**Steam reforming** (Phase 5+, if natural gas or methane available):
- CH₄ + H₂O → CO + 3H₂ (endothermic, 700-900°C, Ni catalyst, 2-3 MPa)
- CO + H₂O → CO₂ + H₂ (water-gas shift, 350-450°C, Fe/Cr oxide catalyst)
- Remove CO₂ with amine scrubber or pressure swing adsorption (PSA). Result: 95-99% H₂.
- Much cheaper than electrolysis if methane is available.

### Silane Production (SiH₄)

**Process route** (from MG-Si, Phase 7):
1. **Trichlorosilane synthesis**: MG-Si + 3HCl → SiHCl₃ + H₂ (fluidized bed reactor, 280-350°C, Cu catalyst). SiHCl₃ boils at 31.8°C — distill from higher-boiling SiCl₄ (bp 57.6°C) and lower-boiling gases.
2. **Redistribution reaction**: 4SiHCl₃ → 3SiCl₄ + SiH₄ (catalytic reactor, 60-80°C). Silane (SiH₄) boils at -112°C — cryogenically distill from SiCl₄.
3. **Purification**: Fractional distillation at cryogenic temperatures. Final purification through molecular sieves and catalytic getters (remove trace chlorosilanes, moisture, methane). Purity requirement: 99.9999%+ (6N+) for semiconductor use.

**Properties and handling**:
- Pyrophoric — spontaneously ignites on contact with air (auto-ignition temperature: room temperature or below for impure silane). Burns with intense flame.
- Storage and transport in stainless steel cylinders, under inert gas pressure. Piping: electropolished stainless steel, welded or VCR-type fittings (no threaded connections — leak potential). All lines purged with N₂ or Ar before introducing silane.
- Leak detection: silane sniffers (thermal conductivity sensors). If silane leaks and ignites, water spray to cool surroundings — do not attempt to extinguish burning silane (let it burn off, the alternative is accumulating explosive gas).
- **NEVER** allow silane to accumulate in confined spaces. Even 2-3% concentration in air can auto-detonate.

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
- From chlor-alkali electrolysis (Phase 5). Compress into steel cylinders. Purity 99.5%+ for semiconductor use (further purified by distillation — Cl₂ bp -34°C).
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

### Cleanroom Consumables

**HEPA/ULPA filter media**:
- **HEPA (High Efficiency Particulate Air)**: Remove 99.97% of particles ≥0.3 μm. Construction: fine fiberglass mat (fiber diameter 0.5-2 μm), folded into accordion pleats (increases surface area 20-50x). Separator: corrugated aluminum or hot-melt bead between pleats. Frame: wood, metal, or plastic. Air velocity through filter: 0.025 m/s. Pressure drop: 250 Pa at rated flow.
- **ULPA (Ultra-Low Penetration Air)**: Remove 99.999% of particles ≥0.12 μm. Even finer glass fibers. Higher pressure drop. Used in most critical zones (lithography bays).
- **Filter production**: Glass fiber production (melt borosilicate glass, attenuate into fine fibers by flame attenuation or rotary spinning). Form mat on moving belt with vacuum forming. Bond with acrylic resin binder (5-10% by weight). Cut, pleat, frame, test (challenge with DOP or PAO aerosol particles, measure penetration with photometer).

**Cleanroom garments**:
- Woven polyester or polyester-blend fabric (lint-free, low particle shedding). Coverall design: full body coverage, elastic cuffs, zip front with flap covering zipper. Hood covering head and neck, integrated face mask or separate. Booties over street shoes, low-particulate soles. Boot cover or change into cleanroom-dedicated shoes.
- **Laundering**: Wash in ultra-pure water (18 MΩ·cm) with non-ionic detergent. Dry in HEPA-filtered dryer. Package in cleanroom-compatible bags. Typical garment life: 40-50 washes before particle shedding exceeds spec.

**Wipers**: Polyester knit (cleanest) or non-woven polypropylene. Sealed edges (laser-cut or ultrasonically sealed) to prevent fiber shedding. Used dry or wetted with IPA for surface cleaning. Tested for particle generation, absorbency, and extractable ions.

**Gloves**: Nitrile rubber (synthetic rubber — acrylonitrile + butadiene copolymer, from SQ 14). 0.2-0.3 mm thickness for dexterity. Powder-free (powder contaminates cleanroom). Chlorinated inner surface for easy donning. Tested for pinholes (water-fill test), particle count, extractable ions. Change every 2 hours or when contaminated.

### Semiconductor Packaging

**Die preparation**:
- **Wafer backgrinding**: Grind back of completed wafer from ~725 μm to 200-350 μm (thinner die fit in thinner packages, better heat dissipation). Diamond-grit grinding wheel, water coolant. Multi-step: coarse grind (30 μm grit, ~600 μm/min removal) → fine grind (5 μm grit, ~100 μm/min) → polish (1 μm grit). Stress relief etch (brief HF dip to remove grinding damage).
- **Wafer mounting**: Adhere wafer to adhesive film (PVC or polyolefin with UV-release adhesive) on metal ring frame. Film holds wafer during dicing.
- **Die singulation (dicing)**: Diamond-impregnated blade (25-50 μm kerf) on high-speed spindle (20,000-40,000 RPM). Cut along scribe streets (pre-defined blank areas between die). Water coolant with surfactant. Feed rate 5-20 mm/second. Produce individual die ~5-20 mm on a side.

**Die attach**:
- **Eutectic bonding**: Au-Si eutectic (97.1% Au, 2.9% Si, mp 363°C). Place die on gold-plated package substrate. Heat to 400-425°C. Gold reacts with silicon die backside → liquid eutectic → bonds on cooling. Very reliable, high thermal conductivity.
- **Epoxy attachment** (more common, lower temperature): Silver-filled epoxy (80% Ag flakes by weight in epoxy resin — provides electrical and thermal conductivity). Dispense epoxy on substrate. Place die (pick-and-place tool — vacuum pickup needle, automated XY positioning). Cure at 150-175°C for 1-2 hours. Epoxy: bisphenol-A + hardener (amine or anhydride), loaded with silver flake 5-20 μm particle size.

**Wire bonding**:
- **Gold ball bonding**: 25 μm (1 mil) diameter gold wire. Form ball on wire tip by electric spark (flame-off). Bond ball to die pad by thermosonic bonding — apply heat (200-250°C), ultrasonic energy (60-120 kHz, 0.5-2 W), and force (0.3-0.8 N) simultaneously. Gold deforms and bonds to aluminum pad. Loop wire to lead frame pad. Bond second end by crescent (wedge) bond. Break wire, repeat. 10-20 bonds/second. Wire length 2-5 mm, loop height 0.2-0.5 mm.
- **Aluminum wedge bonding**: 25-50 μm Al wire. Ultrasonic energy only (room temperature). Wedge tool presses wire against pad. Lower cost but slower. Used for power devices (thicker wire carries more current).
- **Wire drawing for bonding wire**: Draw gold wire through successively smaller diamond dies. Start with 2 mm rod → draw through 20+ dies to 25 μm. Anneal between passes (heat to 500-600°C to restore ductility). Final tensile strength ~200-300 MPa, elongation 2-5%.

**Encapsulation**:
- **Transfer molding** (most common for plastic packages): Place die + wire-bonded lead frame in mold cavity. Inject molding compound (epoxy resin + silica filler 70-80% by weight + catalyst + mold release agent) at 175°C, 6-10 MPa pressure. Cure 2-5 minutes. Mold compound protects die from moisture, mechanical damage, contamination. Silica filler reduces thermal expansion coefficient (match silicon → less stress).
- **Ceramic hermetic packages** (high-reliability): Multi-layer ceramic (alumina) with tungsten metallization traces. Co-fired at 1500-1600°C. Seal lid to package with gold-tin eutectic solder (Au-20Sn, mp 280°C) in dry nitrogen atmosphere. Hermetic (gas-tight) — moisture cannot penetrate. For military, aerospace, high-temperature applications.

**Lead forming and finishing**:
- Trim and form lead frame leads (cut free from frame, bend to required shape — DIP, SOP, QFP lead shapes). Apply solder finish (dip in Sn-Pb or Sn-Ag-Cu solder bath at 230-260°C) for solderability. Mark package top with laser (part number, date code, lot code).

### Testing Infrastructure

**Wafer probing** (test before packaging):
- **Probe card**: Printed circuit board or ceramic substrate with precisely positioned probe needles (tungsten-rhenium or beryllium-copper, tip diameter 12-25 μm). Needles aligned to bond pad pattern. 50-500+ needles per card for complex ICs.
- **Probing station**: Precision XY stage positions wafer under probe card. Camera system for alignment. Z-axis actuator brings probe card into contact — needles scratch through oxide on aluminum pads. Contact resistance <1 Ω.
- **Tests**: DC parametric (Vt, Idsat, Ileakage, breakdown voltage) on test structures (PCMs — process control monitors, placed in scribe streets). Functional test on complete circuits. Speed/bin sort (test at multiple frequencies, bin by maximum operating speed).
- **Yield**: Map pass/fail across wafer → yield map. Typical early fab yields: 10-50%. Mature fab: 80-95%. Track yield by defect type, location, pattern → feedback to process engineering.

**Packaged part testing**:
- **Automated test equipment (ATE)**: Test head with socket for device under test (DUT). Pattern generator applies digital stimuli. Comparator checks outputs. Tests at speed (apply clock, verify timing margins). Temperature testing (hot/cold chuck, -55°C to +125°C for automotive/military grade).
- **Burn-in**: Subject devices to elevated temperature (125-150°C) and voltage (1.2-1.5× rated) for 24-168 hours. Accelerates early-life failures (infant mortality). Devices that survive burn-in have much lower field failure rate.
- **Final test**: Verify all specifications (speed, power, functionality at temperature extremes, I/O levels). Mark passing devices. Package, label, ship.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Phase 5 | Bulk gas production (Cl₂, H₂, O₂, N₂), purification infrastructure |
| Phase 6 | Vacuum technology for gas handling and distillation |
| Phase 7 | Gas supply for CZ growth (argon), CVD precursors (SiH₄, SiHCl₃) |
| Phase 8 | Complete gas/consumable supply chain for fab, packaging, testing |
| SQ 14 | Epoxy encapsulation, fiberglass filters, nitrile gloves, cleanroom garment materials |

## Key Deliverables

- High-purity argon (99.999%+), nitrogen, hydrogen production via air separation and electrolysis
- Silane production with full pyrophoric safety infrastructure
- Dopant gas supply (PH₃, AsH₃, B₂H₆) with exhaust abatement and monitoring
- Etch gas production (CF₄, SF₆, Cl₂, F₂)
- Gas distribution system (electropolished SS tubing, MFCs, valves)
- HEPA/ULPA filter production
- Cleanroom consumable supply chain (garments, wipers, gloves)
- Die packaging line (dice, attach, wire bond, encapsulate, form leads)
- Wafer probing and parametric test capability
- Burn-in and final test infrastructure

## Safety Concerns

- **Dopant gases (PH₃, AsH₃, B₂H₆)**: Among the most toxic substances used industrially. Lethal at ppm concentrations. Continuous gas monitoring, automated shutdown, emergency evacuation procedures. Always use diluted cylinders. Never store large quantities. Exhaust gas abatement mandatory.
- **Silane**: Pyrophoric. Can auto-detonate without ignition source. Leak detection, inert gas purge protocols, no confined spaces.
- **Fluorine gas**: Reacts with almost everything. Severe chemical burns. Handle only in nickel/Monel equipment. Full PPE including face shield and HF-rated gloves (F₂ penetration produces HF on contact with moisture).
- **Gas cylinder safety**: Secure all cylinders upright (chain or strap to wall). Valve caps on when not in use. Never drag cylinders. Proper labeling (color-coded + text). Separate incompatible gases (flammables from oxidizers). Ventilated cylinder storage.

[← Side Quests Index](index.md)
