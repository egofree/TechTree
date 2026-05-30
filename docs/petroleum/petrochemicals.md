# Petrochemical Feedstocks

> **Node ID**: petroleum.petrochemicals
> **Domain**: [Petroleum Extraction & Refining](./index.md)
> **Dependencies**: `petroleum`, [`petroleum.refining`](refining.md)
> **Enables**: `petroleum.petrochemicals.steam-cracking`
> **Timeline**: Years 25-50+
> **Outputs**: ethylene, propylene, butadiene, benzene, toluene, xylene, styrene, ethylene_oxide
> **Critical**: No — petrochemicals are the cheapest route to organic chemicals but ethanol-to-ethylene and coal tar alternatives exist

## Why Petrochemicals Matter

The organic chemicals industry divides into two tiers: bulk chemicals (acids, alkalis, gases — covered under [Chemistry](../chemistry/index.md)) and petrochemicals (organic molecules derived from petroleum or natural gas that serve as building blocks for polymers, solvents, and specialty chemicals). The petrochemical industry produces seven "building block" chemicals — ethylene, propylene, butadiene, benzene, toluene, xylene, and methanol — from which virtually all synthetic organic materials are derived.

Without petrochemical feedstocks, a civilization can produce polymers only from coal tar (limited volumes of benzene and phenol) and fermentation (ethanol → ethylene route, covered in [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md)). Petroleum-derived feedstocks are 10-100× cheaper and more abundant, enabling plastics production at the scale needed for modern infrastructure, packaging, and semiconductor manufacturing.

## Steam Cracking (Olefin Production)

The most important petrochemical process. Steam cracking produces ethylene (C₂H₄) and propylene (C₃H₆) — the two highest-volume organic chemicals in the world. Global ethylene production exceeds 200 million tonnes/year. Together, ethylene and propylene are the building blocks for more than half of all petrochemical products.

## Principle

Hydrocarbon feedstock (ethane, propane, naphtha, or gas oil) is mixed with steam (diluent) and heated to 750-900°C in a tubular furnace for an extremely short residence time (0.1-0.5 seconds). The high temperature causes thermal decomposition (free-radical mechanism) of C-C and C-H bonds. The short residence time maximizes primary cracking products (ethylene, propylene) while minimizing secondary reactions (aromatization, coking).

## Feedstock Selection

| Feedstock | Ethylene Yield | Propylene Yield | BTX Yield | Typical Source |
|-----------|----------------|-----------------|-----------|----------------|
| Ethane (C₂H₆) | 80-84% | 1-2% | <1% | Natural gas NGL recovery |
| Propane (C₃H₈) | 42-46% | 14-18% | 2-4% | Natural gas NGL recovery |
| Naphtha (C₅-C₁₂) | 30-35% | 13-18% | 8-12% | Refinery atmospheric distillation |
| Gas oil (C₁₂-C₂₀) | 22-28% | 12-16% | 10-14% | Refinery VGO |

Ethane is the preferred feedstock where available (highest ethylene yield, simplest separations). The United States, with abundant natural gas, cracks predominantly ethane (75%+ of ethylene production). Europe and Asia, with less natural gas, crack predominantly naphtha (70%+ of ethylene production).

## Furnace Design

**Cracking coil**: Centrifugally cast HK-40 alloy (25Cr-20Ni-Fe, ASTM A297 Grade HK40) or HP-modified (35Cr-45Ni-Fe with microalloying additions of Nb, Ti, W). Inside diameter: 50-150 mm. Wall thickness: 8-15 mm. Tube length: 30-80 m per coil (arranged in multiple vertical passes within the furnace firebox). The high nickel-chrome alloy resists carburization and creep at operating temperatures.

**Heat flux**: 60-100 kW/m² of tube external surface. Furnace fuel: refinery gas, natural gas, or fuel oil. Thermal efficiency: 85-92% with air preheat and convection section heat recovery.

**Coking**: Carbon deposits build up on the inner tube wall over 20-60 days of operation, increasing tube wall temperature and pressure drop. When tube metal temperature approaches the design limit (typically 1,050-1,100°C), the furnace must be decoked: steam-air mixture at 800-900°C burns out the coke over 12-24 hours. Modern furnaces use online decoking (one coil at a time while others remain in production).

## Product Recovery & Separation

Cracked gas exits the furnace at 800-900°C and must be quenched within 0.02-0.05 seconds to stop secondary reactions. The transfer line exchanger (TLE, also called waste heat boiler) cools the gas to 300-400°C while generating high-pressure steam (10-14 MPa, saturated, for process use or power generation).

**Separation train**: After quenching, compression to 30-40 bar (5-6 stages with interstage cooling), acid gas removal (amine wash for CO₂), and drying (molecular sieve or glycol), the cracked gas enters the cold separation section:

1. **Demethanizer**: Separates methane and hydrogen (overhead, used as fuel gas) from C₂+ (bottoms). Operates at -100 to -140°C using ethylene or propylene refrigeration cascade.
2. **Deethanizer**: C₂ fraction (overhead) from C₃+ (bottoms). 
3. **C₂ splitter**: Separates ethylene product (overhead, 99.9% purity, polymer grade) from ethane (bottoms, recycled to furnace). Requires 80-130 actual trays or equivalent structured packing. This is the tallest column in the ethylene plant (60-90 m).
4. **Depropanizer**: C₃ fraction (overhead) from C₄+ (bottoms).
5. **C₃ splitter**: Separates propylene product (overhead, 99.5% chemical grade or 99.9% polymer grade) from propane (bottoms, recycled to furnace or sold as LPG).
6. **Debutanizer**: C₄ fraction (overhead, containing butadiene, isobutene, n-butenes) from C₅+ gasoline (bottoms, pyrolysis gasoline rich in BTX aromatics).

## Refrigeration System

The cryogenic separations require refrigeration at multiple temperature levels. The classic cascade uses three pure-component refrigeration cycles:

- **Propylene cycle**: +10°C to -40°C (provides cooling for depropanizer condenser, C₃ splitter reboiler, and intermediate cooling)
- **Ethylene cycle**: -60°C to -100°C (provides cooling for demethanizer condenser and C₂ splitter condenser)
- **Methane cycle**: -120°C to -160°C (provides cooling for demethanizer overhead, hydrogen purification)

Total refrigeration power: 15-30 MW for a 500,000 tonne/year ethylene plant. Refrigeration compressors are the largest rotating equipment in the plant — centrifugal machines driven by steam turbines or electric motors (20-40 MW each).

## Aromatics Production (BTX)

The three primary aromatics — benzene, toluene, and xylene (BTX) — are produced from two main sources: catalytic reforming (covered in [Refining](refining.md)) and pyrolysis gasoline (a byproduct of steam cracking naphtha/gas oil). Both routes produce a complex mixture that must be separated into pure components.

## BTX Separation Sequence

1. **Hydrotreating**: Raw reformate or pyrolysis gasoline contains di-olefins and styrene that polymerize and foul downstream equipment. Selective hydrogenation over Pd/Al₂O₃ at 40-80°C saturates di-olefins to mono-olefins while preserving aromatics.
2. **Extraction**: Aromatics are separated from non-aromatics (paraffins, naphthenes) by liquid-liquid extraction. Modern solvent: sulfolane (tetrahydrothiophene-1,1-dioxide). Aromatics are highly soluble in sulfolane; paraffins are not. Extract (aromatics + sulfolane) is separated in a recovery column where aromatics are distilled overhead and sulfolane is recycled.
3. **Clay treating**: Removes trace olefins from extracted aromatics (olefins would interfere with downstream chemical processes). Acid-treated clay at 180-220°C.
4. **Fractionation columns**: 
   - **Benzene column**: Benzene overhead (99.9% purity, bp 80.1°C)
   - **Toluene column**: Toluene overhead (99.8% purity, bp 110.6°C)
   - **Xylene column**: Mixed xylenes overhead (bp 138-144°C), C₉+ aromatics bottoms

## Xylene Isomer Separation

Mixed xylenes contain three isomers with very close boiling points: para-xylene (px, bp 138.4°C), meta-xylene (mx, bp 139.1°C), ortho-xylene (ox, bp 144.4°C), and ethylbenzene (eb, bp 136.2°C). Para-xylene is by far the most valuable (PET polyester feedstock) and must be separated to >99.7% purity.

**Separation methods**:

- **Adsorptive separation (Parex process)**: Molecular sieve adsorbent selectively adsorbs para-xylene from mixed xylenes in a simulated moving bed (SMB) system. Desorbed with para-diethylbenzene. Produces >99.7% pure para-xylene at 97% recovery per pass. The dominant commercial technology.

  **Strengths**:
  - Highest recovery per pass (97%) — minimizes recycle volume and isomerization energy
  - Product purity >99.7% meets PET feedstock specification directly
  - Continuous process — simulated moving bed operates 24/7 without batch cycling
  - Lower energy consumption than crystallization — operates near ambient temperature
  - Proven at scale — >90% of global para-xylene produced via Parex-type units

  **Weaknesses**:
  - Requires specialized molecular sieve adsorbent — not available in early bootstrap
  - Simulated moving bed system is mechanically complex — 24-36 rotary valves, adsorbent chambers 6-12 m diameter
  - Desorbent (para-diethylbenzene) must be recovered and recycled — adds distillation column and energy
  - Adsorbent degrades over time (5-7 year life) — replacement requires unit shutdown
  - Not selective between meta- and ortho-xylene — only separates para-xylene from the mixture

- **Crystallization**: Para-xylene has the highest freezing point (+13.3°C vs. -48°C for mx and -25°C for ox). Cool to -60 to -70°C; para-xylene crystallizes first. Filter or centrifuge. Lower recovery per pass (~60%) but simpler technology.

  **Strengths**:
  - Mechanically simpler — crystallizer, centrifuge, and refrigeration system (no adsorbent or desorbent)
  - No specialized materials — standard steel equipment with refrigeration compressor
  - Bootstrap-friendly — can be built with moderate industrial capability
  - Higher product purity achievable in single stage (crystals are physically separated from mother liquor)
  - No desorbent contamination risk in the product

  **Weaknesses**:
  - Low single-pass recovery (~60%) — requires 3-4 crystallize-melt-recrystallize cycles, increasing energy cost
  - High energy consumption — refrigeration to -60 to -70°C requires significant compressor power
  - Mother liquor handling — eutectic limits prevent crystallizing all para-xylene; remaining liquid must be isomerized and recycled
  - Slower throughput — batch or semi-batch operation limits production rate vs. continuous Parex
  - Crystal washing losses — adhering mother liquor on crystal surfaces reduces purity unless washed (which loses yield)

**Isomerization**: After extracting para-xylene, the remaining xylenes (now depleted in para-xylene) are isomerized back toward equilibrium over a Pt/zeolite catalyst at 250-400°C, regenerating para-xylene for another extraction cycle. Overall para-xylene yield from mixed xylenes: 85-90% after multiple extract-isomerize cycles.


## From Ethylene

**Polyethylene** (largest single plastics product, ~120 million tonnes/year):
- **HDPE** (high-density): Polymerized at 60-90°C, 5-30 bar using Ziegler-Natta (TiCl₄/AlEt₃) or chromium oxide catalyst. Linear chains, density 0.94-0.97 g/cm³. Used for: bottles, pipes, containers, geomembranes.
- **LDPE** (low-density): Polymerized at 1,000-3,000 bar, 150-300°C using organic peroxide initiators. Branched chains, density 0.91-0.93 g/cm³. Used for: films, bags, wire insulation.
- **LLDPE** (linear low-density): Copolymer of ethylene with 5-12% α-olefin (butene, hexene, octene) at 20-40 bar using Ziegler-Natta or metallocene catalyst. Combines LDPE flexibility with HDPE strength.

**Ethylene oxide / ethylene glycol**: Ethylene + ½O₂ over Ag/Al₂O₃ catalyst at 250-300°C, 10-20 bar → ethylene oxide (selectivity 80-90%). Ethylene oxide + H₂O → ethylene glycol (MEG, antifreeze, PET polyester feedstock).

**Vinyl chloride / PVC**: Ethylene + Cl₂ → 1,2-dichloroethane (EDC). EDC pyrolysis at 480-530°C → vinyl chloride monomer (VCM) + HCl. VCM polymerized via suspension process (VCM dispersed in water with peroxide initiator) → polyvinyl chloride (PVC). PVC + plasticizers → flexible PVC (cables, flooring, medical tubing). PVC without plasticizers → rigid PVC (pipes, window frames).

**Styrene**: From benzene + ethylene → ethylbenzene (acid catalyst, 80-95% yield). Ethylbenzene dehydrogenated to styrene over Fe₂O₃/Cr₂O₃/K₂O catalyst at 580-650°C, 0.4-1.0 bar, with steam diluent (80-90% conversion per pass). Styrene → polystyrene (via suspension or bulk polymerization with peroxide initiators). Expanded polystyrene (EPS): polystyrene beads containing pentane blowing agent, steam-expanded in molds. Insulation, packaging.

## From Propylene

**Polypropylene**: Propylene polymerized at 60-80°C, 10-35 bar using Ziegler-Natta (TiCl₄/MgCl₂ support with AlEt₃ cocatalyst) or metallocene catalyst. Isotactic polypropylene (stereoregular, >95% isotactic pentads) is the commercially useful form — crystalline, rigid, melting point 160-165°C. Used for: fibers, films, containers, automotive parts. Global production ~80 million tonnes/year.

**Acrylonitrile**: Propylene + NH₃ + 1.5O₂ → acrylonitrile (CH₂=CH-CN) over Bi-Mo oxide catalyst at 400-500°C (ammoxidation process, SOHIO process). Yield: 70-80%. Used for: acrylic fibers, ABS engineering plastic (acrylonitrile-butadiene-styrene), carbon fiber precursor (polyacrylonitrile (PAN) fibers oxidized and carbonized at 1,000-3,000°C).

**Propylene oxide**: Propylene + organic hydroperoxide (from isobutane or ethylbenzene) over Mo or Ti catalyst → propylene oxide + coproduct (tert-butanol or styrene). Co-product process economics depend on market for the coproduct. Chlorohydrin route (propylene + Cl₂ + Ca(OH)₂) is older, generates CaCl₂ waste.

## From BTX Aromatics

**Benzene derivatives**:
- **Cumene → phenol + acetone**: Benzene + propylene → cumene (isopropylbenzene). Cumene + O₂ → cumene hydroperoxide. Acid-catalyzed cleavage → phenol + acetone (Hock process, >99% purity). Phenol → phenolic resins (Bakelite, foundry resins), polycarbonate (via bisphenol-A), nylon-6 (via cyclohexane → caprolactam).
- **Cyclohexane**: Benzene + 3H₂ → cyclohexane (Ni catalyst, 150-200°C, 20-30 bar). Cyclohexane → adipic acid (oxidation with HNO₃) → nylon-6,6 (condensation with hexamethylenediamine).

**Toluene derivatives**:
- **Toluene → benzene**: Hydrodealkylation (HDA) at 600-650°C, 30-50 bar over Cr₂O₃/Al₂O₃: toluene + H₂ → benzene + CH₄. Used when benzene demand exceeds supply from reformate.
- **Toluene diisocyanate (TDI)**: Toluene → dinitrotoluene (HNO₃/H₂SO₄ nitration) → toluene diamine (H₂ reduction) → TDI (phosgenation with COCl₂). TDI + polyol → polyurethane foams (flexible foam for furniture, rigid foam for insulation).

**Xylene derivatives**:
- **Para-xylene → PTA → PET**: Para-xylene oxidized with air in acetic acid solvent over Co/Mn/Br catalyst at 190-210°C, 15-20 bar → purified terephthalic acid (PTA). PTA + ethylene glycol → polyethylene terephthalate (PET) via melt polycondensation at 270-290°C, <1 mbar. PET: polyester fibers (clothing, tire cord), bottles, food packaging. Global PET production ~80 million tonnes/year.
- **Ortho-xylene → phthalic anhydride**: Oxidation with air over V₂O₅ catalyst at 350-400°C → phthalic anhydride. Plasticizers for PVC (dioctyl phthalate, DOP), alkyd resins, unsaturated polyester resins.

## Methanol and Synthetic Feedstocks

While not strictly petroleum-derived, methanol production is closely integrated with natural gas processing and provides an alternative feedstock route:

**Methanol synthesis**: Natural gas (methane) → syngas (CO + 2H₂) via steam reforming at 800-900°C, 20-30 bar over Ni/Al₂O₃ catalyst. Syngas converted to methanol over Cu/ZnO/Al₂O₃ at 250-300°C, 50-100 bar. Yield: ~99% methanol selectivity.

**Methanol-to-olefins (MTO)**: Methanol → dimethyl ether → ethylene + propylene over SAPO-34 zeolite catalyst at 350-450°C. Ethylene yield: 40-50%. Propylene yield: 25-35%. Provides a non-petroleum route to olefins where natural gas is abundant but naphtha is scarce (China has invested heavily in MTO technology).

## Integration with the Refinery

Modern "refinery-petrochemical integration" combines the refinery and petrochemical complex on a single site to maximize feedstock utilization:

- **Refinery → petrochemicals**: Naphtha feed to steam cracker, reformate BTX to aromatics extraction, propylene from FCC to polypropylene, refinery hydrogen to petrochemical hydrotreaters.
- **Petrochemicals → refinery**: Pyrolysis gasoline from steam cracker to refinery gasoline pool, steam cracker byproduct fuel gas to refinery furnaces.
- **Utilities integration**: Shared steam system, power generation, cooling water, and hydrogen network reduce overall energy consumption by 10-20% compared to standalone facilities.

## Non-Petroleum Alternatives

The bootstrap civilization may not have access to petroleum. Alternative paths to the same petrochemical building blocks exist:

| Building Block | Petroleum Route | Alternative Route |
|---------------|-----------------|-------------------|
| Ethylene | Steam cracking naphtha | Ethanol dehydration over Al₂O₃ at 170°C (95-99% yield) |
| Benzene | Catalytic reforming | Coal tar distillation (limited volumes, ~0.5% of coal tar) |
| Methanol | Natural gas reforming → synthesis | Wood pyrolysis (1-2% yield) or CO₂ + H₂ electrolysis |
| Propylene | Steam cracking / FCC | Limited alternatives — primarily petroleum-derived |
| BTX | Reforming / steam cracking | Coal tar (very limited) |

The ethanol-to-ethylene route is the most important alternative: fermentation ethanol (from grain, sugar, or cellulosic biomass) dehydrated to ethylene at 95-99% yield enables polyethylene and PVC production without any petroleum. This is the critical bootstrap pathway for polymers in a petroleum-scarce scenario (covered in detail in [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md)).

## Cross-References

- **Refining**: Produces the naphtha and gas oil feedstocks — [Petroleum Refining](refining.md)
- **Extraction**: Provides the crude oil — [Crude Oil Extraction](extraction.md)
- **Polymers**: Converts feedstocks into materials — [Polymers & Composites](../polymers/index.md)
- **Alternative chemistry**: Coal tar and fermentation routes — [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md)
- **Distillation fundamentals**: Column design and operation — [Distillation](../chemistry/distillation.md)


## Toxic and Carcinogenic Exposures

- **Benzene**: Confirmed human carcinogen (leukemia, especially acute myeloid leukemia). TLV-TWA: 0.5 ppm. All benzene handling must be in closed systems with continuous atmospheric monitoring. Workers in aromatics units must wear personal benzene monitors. Substitute with toluene or xylene wherever chemically feasible.
- **1,3-Butadiene**: Probable human carcinogen. TLV-TWA: 1 ppm. Volatile gas (bp -4.4°C). Leak detection and repair (LDAR) programs for all valves, flanges, and connectors in butadiene service.
- **Ethylene oxide**: Carcinogen, mutagen, and reproductive toxin. TLV-TWA: 1 ppm. Used in sterilization and ethylene glycol production. Closed systems with negative pressure enclosure around handling areas.

## Process Safety

- **High-pressure systems**: Hydrocracking operates at 80-200 bar. Steam cracking furnaces at 0.3-0.5 bar gauge but with high-temperature gas at 800-900°C. Design all high-pressure equipment per ASME Boiler and Pressure Vessel Code Section VIII. Hydrostatic test at 1.3× MAWP.
- **Flammable gas handling**: Ethylene (LEL 2.7%, UEL 36%) and propylene (LEL 2.0%, UEL 11.1%) form explosive mixtures with air at low concentrations. All olefin processing equipment must be electrically classified Class I Division 1 or 2. Nitrogen purge before introducing hydrocarbons.
- **Runaway reactions**: Polymerization reactors (polyethylene, polypropylene) can experience runaway if temperature control fails. Emergency quench systems (inject inhibitor into reactor) and pressure relief to blowdown system.
- **Cryogenic hazards**: Ethylene plant cold section operates at -100 to -160°C. Skin contact with uninsulated cryogenic piping causes immediate frostbite. Oxygen condensation on uninsulated surfaces at these temperatures creates extreme fire hazard. Insulate all cold equipment. Monitor for oxygen enrichment in confined spaces.

## Environmental Management

- **VOC emissions**: Fugitive emissions from valves, flanges, pumps, and compressors are the largest source of VOCs in a petrochemical complex. LDAR programs reduce emissions by 60-80%.
- **Wastewater**: Process water from steam cracking, aromatic extraction, and polymerization contains hydrocarbons, phenols, and suspended solids. Treatment: API separator (gravity oil removal) → dissolved air flotation (DAF) → biological treatment (activated sludge) → discharge.
- **Plastic waste**: The petrochemical industry's products (plastics) create end-of-life waste. In a bootstrap civilization, plastic recycling (mechanical: wash, shred, re-extrude; or chemical: pyrolyze back to monomers) should be planned from the start to avoid accumulating persistent waste.

## Bootstrap Sequence for Petrochemical Capability

1. **Ethanol dehydration** (Year 15-25): Fermentation ethanol → ethylene over alumina catalyst at 350-400°C. Enables polyethylene and PVC without petroleum. Small scale (100-1,000 tonnes/year).
2. **Coal tar distillation** (Year 15-25): Coke ovens → coal tar → benzene, toluene, phenol. Limited volumes but sufficient for Bakelite, pharmaceuticals, and dye precursors.
3. **Petroleum naphtha steam cracking** (Year 25-35): Refinery naphtha feed → ethylene, propylene, BTX. Requires atmospheric distillation + FCC or reforming unit first. Industrial scale (10,000-1,000,000 tonnes/year).
4. **Integrated refinery-petrochemical complex** (Year 35+): Fully integrated site with FCC, hydrocracking, steam cracking, aromatics extraction, and polymerization units. Optimized energy and feedstock integration.

## Glossary of Key Terms

| Term | Definition |
|------|-----------|
| Olefin | A hydrocarbon with at least one carbon-carbon double bond (ethylene, propylene, butadiene) |
| Paraffin | A saturated hydrocarbon with only single bonds (ethane, propane, n-hexane) |
| Aromatic | A hydrocarbon containing one or more benzene rings (benzene, toluene, xylene) |
| Naphtha | A petroleum fraction boiling between 30-180°C, used as steam cracker feed or gasoline blending |
| LPG | Liquefied petroleum gas — propane and butane, stored under pressure as liquids |
| NGL | Natural gas liquids — ethane, propane, butane, and pentane recovered from natural gas |
| Polymer grade | Purity specification for monomers suitable for polymerization (ethylene >99.9%, propylene >99.5%) |
| Pyrolysis gasoline | Aromatic-rich byproduct of naphtha steam cracking (50-70% BTX) |
| Selectivity | Fraction of converted feedstock that becomes the desired product |
| Conversion | Fraction of feedstock that reacts (does not exit unchanged) |

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Steam cracking furnace tube metal temperature reaches 1,100°C before 20-day cycle | Coke buildup inside coils exceeding normal 20–60 day rate; high feedstock aromatic content accelerates coking | Initiate decoking: steam-air mixture at 800–900°C for 12–24 hours to burn out coke; consider switching to lighter feedstock (ethane gives 80–84% ethylene yield vs. 30–35% for naphtha) with lower coking tendency |
| C₂ splitter column cannot achieve 99.9% polymer-grade ethylene purity | Insufficient reflux ratio or structured packing HETP degraded below 0.15–0.25 m specification; column flooding at upper sections | Increase reflux ratio; verify structured packing condition (corrosion, fouling); check column pressure at design setpoint — the C₂ splitter is the tallest column (60–90 m) and most sensitive to upsets |
| Demethanizer overhead temperature drifts above −100°C | Ethylene refrigeration cascade underperforming — ethylene cycle not reaching −100°C due to compressor surge or refrigerant loss | Check ethylene compressor for surge conditions; verify refrigerant charge; inspect heat exchangers in cascade (propylene: +10 to −40°C; ethylene: −60 to −100°C; methane: −120 to −160°C) |
| Para-xylene purity below 99.7% from Parex adsorptive separation unit | Molecular sieve adsorbent degraded after 5–7 year life; desorbent (para-diethylbenzene) contaminated; rotary valve leaking | Replace adsorbent bed if beyond rated life; purify or replace desorbent; inspect 24–36 rotary valves for internal cross-leakage; verify simulated moving bed timing sequence |
| HDPE product contains gels (unmelted polymer particles) | Ziegler-Natta catalyst (TiCl₄/AlEt₃) hot spots in reactor at 60–90°C, 5–30 bar causing localized over-polymerization; insufficient mixing | Improve reactor mixing and temperature uniformity; dilute catalyst feed; verify reactor temperature stays within 60–90°C band; screen product through mesh filter during pelletizing |
| LDPE reactor pressure drops below 1,000 bar during peroxide-initiated polymerization | Organic peroxide initiator injection pump malfunction; compressor unable to maintain 1,000–3,000 bar operating pressure | Repair or replace initiator metering pump; verify compressor packing seals rated for 1,000–3,000 bar service; check for polymer fouling in compressor valves |
| VCM (vinyl chloride monomer) reactor shows runaway temperature above 530°C | EDC pyrolysis tube skin temperature exceeded 530°C design limit; coke deposit causing local hotspot and reduced heat transfer | Emergency shutdown of pyrolysis furnace; initiate decoking cycle; reduce feed rate to keep tube skin temperature below 530°C; verify coke is not approaching tube wall design limit of 1,050–1,100°C |
| BTX extraction column produces aromatics with >100 ppm non-aromatics | Sulfolane solvent contaminated with water or degraded; extract/recovery column reboiler temperature drift from design point | Dry or replace sulfolane solvent; verify recovery column temperature profile — aromatics distill overhead while sulfolane recycles from bottoms; check for water ingress from upstream hydrotreater |
| Polypropylene product isotacticity below 95% (tacky, amorphous product) | Ziegler-Natta catalyst (TiCl₄/MgCl₂ support) deactivated by catalyst poison (H₂O, CO, O₂) in propylene feed; AlEt₃ cocatalyst insufficient | Purify propylene feed to remove catalyst poisons; increase AlEt₃ cocatalyst ratio; verify feed gas meets polymer-grade purity (>99.5% for propylene) |
| Acrylonitrile yield drops below 70% in ammoxidation reactor | Bi-Mo oxide catalyst aged or poisoned by halides; propylene:NH₃:air ratio deviating from stoichiometric 1:1.1:7.5 | Replace or regenerate Bi-Mo catalyst; recalibrate gas flow controllers for propylene, NH₃, and air feeds; maintain reactor at 400–500°C per SOHIO process specification |

## See Also

- [Refining](refining.md) — petroleum distillation and fractionation that produce petrochemical feedstocks
- [Petroleum Alternatives](../chemistry/petroleum-alternatives.md) — ethanol-to-ethylene and coal tar routes without petroleum
- [Polymers / Synthetic](../polymers/synthetic.md) — polymerization of ethylene, propylene, and other monomers
- [Distillation](../chemistry/distillation.md) — fractionation column design fundamentals
- [Chemistry](../chemistry/index.md) — bulk inorganic chemical production

[← Back to Petroleum Extraction & Refining](index.md)
