# PEM Water Electrolysis with SEM Tech Membranes

> **Node ID**: chemistry.sem-tech-water-electrolysis
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.sem-tech`](sem-tech.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`chemistry.hydrogen-silane`](hydrogen-silane.md), [`chemistry.ammonia`](ammonia.md)
> **Timeline**: Years 20-35
> **Outputs**: hydrogen, oxygen
> **Critical**: No — SEM Tech membranes enable lower-cost PEM water electrolysis but are an alternative to alkaline electrolysis, not a unique enabler


Water electrolysis splits water into hydrogen and oxygen using electrical energy. When powered by renewable electricity, the resulting hydrogen is called "green hydrogen" -- produced with zero carbon emissions. Proton Exchange Membrane (PEM) electrolysis is the most promising route for green hydrogen production due to its compact design, rapid response to variable power input, and high-purity output.

The SEM Tech cation exchange membrane described in [SEM Tech](sem-tech.md) could serve as a low-cost alternative to perfluorinated sulfonic acid membranes (such as Nafion) in PEM water electrolysis cells. However, this application has **not yet been demonstrated** with SEM Tech membranes -- all PEM-specific performance claims in this article are theoretical projections based on the membrane's demonstrated properties in chlor-alkali electrolysis. The Rowow SEM Tech Technical Overview describes the entropy management principle underlying these membranes: ion exchange membranes manage entropy across charge and discharge cycles by selectively transporting ions while blocking electron flow and molecular mixing.

The parent article on [Electrolysis](electrolysis.md) covers all industrial electrolysis processes including alkaline water electrolysis.

## PEM Electrolysis vs Alkaline

Two main technologies exist for water electrolysis:

**[Alkaline water electrolysis](../glossary/alkaline-water-electrolysis.md)** (mature, widely deployed):
- Uses a liquid electrolyte (20-40% KOH solution) with a porous diaphragm separator
- Nickel-based electrodes (non-precious metal catalysts)
- Operating temperature: 60-90C
- Current density: 200-500 mA/cm²
- Cell voltage: 1.8-2.4V
- Hydrogen purity: 99.5-99.9% (requires downstream purification for sensitive applications)
- Advantages: proven technology, no precious metal catalysts, long stack lifetime (60,000-90,000 hours)
- Disadvantages: slow dynamic response (minutes to ramp), gas crossover at low loads, corrosive liquid electrolyte handling

**PEM water electrolysis** (emerging, growing rapidly):
- Uses a solid polymer electrolyte (ion exchange membrane) instead of liquid electrolyte
- Platinum and iridium oxide catalysts on electrodes
- Operating temperature: 50-80C
- Current density: 1,000-3,000 mA/cm² (much higher than alkaline)
- Cell voltage: 1.8-2.2V
- Hydrogen purity: 99.99%+ directly from the cell
- Advantages: compact (high current density), rapid dynamic response (sub-second), no liquid electrolyte, high purity, operates under pressure
- Disadvantages: expensive membrane ($100-400/sq ft for Nafion), precious metal catalysts, acidic environment demands corrosion-resistant materials

**Strengths**: PEM electrolysis produces 99.99%+ pure H₂ directly (no downstream purification needed for most applications); sub-second dynamic response matches intermittent renewable electricity perfectly; 5-10× higher current density than alkaline means compact footprint; no corrosive liquid electrolyte (KOH) to handle; operates under pressure (reduces compression cost for H₂ storage).

**Weaknesses**: Nafion membrane costs $100-400/ft² (dominant capital cost); Ir and Pt catalysts are scarce and expensive; acidic environment requires titanium or gold-coated cell components; membrane degradation from peroxide radical attack limits lifetime; SEM Tech PVC-based membrane has NOT yet been demonstrated for PEM water electrolysis — performance is theoretical.

The critical barrier to PEM adoption is membrane cost. SEM Tech membranes, at less than $1 per square foot, could eliminate this barrier entirely -- but only if they perform adequately in the PEM water electrolysis environment.


## Theoretical Application

The SEM Tech membrane uses strong acid cation exchange resin beads (sulfonic acid functional groups) embedded in a PVC/CPVC matrix -- the same type of functional groups found in Nafion membranes. In principle, this membrane could serve as the solid polymer electrolyte in a PEM water electrolysis cell, selectively conducting protons (H⁺ ions) from anode to cathode while preventing gas crossover.

The Rowow LLC Technical Volume notes that these membranes were originally developed for electrochemical applications beyond chlor-alkali, including fuel cells and electrodialysis. The demonstrated chemical durability (months of operation at pH 0, ORP >1.5V) suggests the acidic environment of a PEM cell (pH 2-4 at the anode) should be within the membrane's tolerance range.

## Key Differences from Chlor-Alkali Use

Using the SEM Tech membrane for water electrolysis differs from its demonstrated chlor-alkali application in several important ways:

- **Proton transport vs sodium ion transport**: In chlor-alkali, Na⁺ ions cross the membrane. In PEM water electrolysis, H⁺ (protons) must cross. Proton transport through sulfonic acid groups is well-established, but the proton conductivity of the SEM Tech membrane has not been characterized.
- **Water management**: PEM cells require precise water management -- the membrane must remain hydrated but not flooded. The PVC/CPVC binder matrix in SEM Tech membranes may behave differently than perfluorinated polymer matrices in terms of water uptake and transport.
- **Gas crossover**: Hydrogen and oxygen must not mix across the membrane. The SEM Tech membrane's gas barrier properties in a thin-film PEM configuration have not been tested. Gas crossover is a safety concern (explosive H₂/O₂ mixtures) and an efficiency concern.
- **Operating temperature**: PEM cells typically run at 50-80C. SEM Tech membranes are demonstrated at ambient temperature. Performance at elevated PEM operating temperatures is unknown.

## Cell Architecture

A PEM water electrolysis cell using SEM Tech membranes would follow the standard PEM cell design with modifications to accommodate the membrane's properties:

**Basic cell structure** (four layers compressed between end plates):
- **Anode**: Porous titanium or graphite electrode with iridium oxide (IrO₂) catalyst. Water is oxidized: 2H₂O → O₂ + 4H⁺ + 4e⁻
- **SEM Tech membrane**: Cation exchange membrane conducts H⁺ ions from anode to cathode. Separator preventing gas mixing.
- **Cathode**: Porous carbon or titanium electrode with platinum catalyst. Protons are reduced: 4H⁺ + 4e⁻ → 2H₂
- **End plates and flow fields**: Titanium or coated steel end plates with machined flow channels for water delivery and gas collection. Gaskets or PVC/CPVC cement for sealing (matching SEM Tech's solvent-welding approach).

**Modifications vs chlor-alkali cells**:
- **Two-compartment design**: Unlike the three-compartment chlor-alkali cell, water electrolysis needs only anode and cathode compartments separated by the membrane.
- **Water feed**: Deionized water is fed to the anode side (or both sides in some designs). Water quality matters -- minerals and impurities poison catalysts and foul the membrane.
- **No brine**: No salt solution is involved, eliminating chloride-related corrosion concerns but removing the chlorine production stream.
- **Thinner membrane**: PEM water electrolysis typically uses thin membranes (50-200 microns) to minimize proton transport resistance. SEM Tech membranes can be produced at various thicknesses via spray application.

**Stack design**: Multiple cells connected in series (bipolar plate arrangement) form a stack. Typical stacks range from 10-100+ cells. SEM Tech's low membrane cost could make large stacks economically viable.


## Demonstrated Range (Chlor-Alkali)

SEM Tech membranes are demonstrated at:
- **Temperature**: Ambient (20-30C)
- **Current density**: Not specifically characterized for water electrolysis; chlor-alkali operation at 50A laboratory scale
- **pH tolerance**: pH 0 continuous operation
- **ORP tolerance**: >1.5V continuous
- **Pressure**: Atmospheric

## Projected PEM Operating Range

Based on membrane properties and general PEM electrolysis principles, projected operating parameters are:

- **Cell voltage**: 1.8-2.2V (thermodynamic minimum is 1.23V at 25C; practical cells require higher voltage due to overpotentials)
- **Current density**: Uncertain. PEM cells with Nafion operate at 1,000-3,000 mA/cm². SEM Tech membrane resistance may limit achievable current density -- **not yet characterized for proton transport**.
- **Temperature**: Ambient operation is most likely compatible with SEM Tech membranes, given their demonstrated ambient-temperature performance. Elevated temperature (50-80C) would improve kinetics but membrane stability at these temperatures in the PEM environment is unproven.
- **Pressure**: Atmospheric operation is most conservative. Pressurized operation (up to 30 bar) is common in commercial PEM systems but adds mechanical stress on the membrane.

## Performance

**The following performance projections are speculative. SEM Tech membranes have NOT been tested in PEM water electrolysis. Actual performance may differ significantly.**

## Projected Performance Characteristics

- **Hydrogen purity**: PEM cells typically produce 99.99%+ pure hydrogen. The SEM Tech membrane's gas barrier properties would determine whether this purity level is achievable. Higher gas crossover would reduce purity and create safety concerns.
- **Energy consumption**: Theoretical minimum is 39.4 kWh/kg H₂ (thermoneutral voltage). Practical PEM systems consume 50-65 kWh/kg H₂. SEM Tech membrane resistivity may increase this -- the membrane's ionic resistance in proton conduction mode is unknown.
- **Production rate**: Determined by current density and cell area. A 100 cm² cell at 1,000 mA/cm² would produce approximately 0.04 normal liters of H₂ per minute.
- **Membrane lifetime**: Demonstrated at months to ~1 year in chlor-alkali service (pH 0, ORP >1.5V). PEM water electrolysis operates under milder chemical conditions but potentially higher current densities. Projected lifetime is uncertain.
- **Faradaic efficiency**: PEM cells typically achieve 95-99% Faradaic efficiency. SEM Tech membrane performance in this regard is unknown.

## Comparison: PEM Water Electrolysis Technologies

| Parameter | Conventional PEM (Nafion) | SEM Tech PEM (Projected) | Alkaline |
|-----------|--------------------------|--------------------------|----------|
| **Membrane cost** | $100-400/sq ft | <$1/sq ft | N/A (diaphragm) |
| **Current density** | 1,000-3,000 mA/cm² | Unknown | 200-500 mA/cm² |
| **Operating temp** | 50-80C | Ambient (projected) | 60-90C |
| **H₂ purity** | 99.99%+ | Unknown | 99.5-99.9% |
| **Dynamic response** | Sub-second | Likely similar | Minutes |
| **Membrane lifetime** | 5-10 years | Months to ~1 year (projected) | N/A (diaphragm 6-12 months) |
| **TRL** | 8-9 | 2-3 (for water electrolysis) | 9 |

## Hydrogen Applications

Green hydrogen produced by water electrolysis serves multiple downstream processes in industrial civilization:

**Ammonia synthesis**: The Haber-Bosch process (N₂ + 3H₂ → 2NH₃) is the largest consumer of hydrogen globally. Green hydrogen from electrolysis enables ammonia production without fossil fuel feedstock. See [Ammonia Production](ammonia.md).

**e-Methanol synthesis**: Hydrogen combined with captured CO₂ over a catalyst produces methanol (CH₃OH). This power-to-liquids pathway stores renewable energy as a liquid fuel. See [SEM Tech e-Methanol](sem-tech-e-methanol.md).

**Fuel cells**: Hydrogen fuels PEM fuel cells for electricity generation. The same SEM Tech membrane platform could potentially serve in both electrolysis (producing H₂) and fuel cells (consuming H₂). See [SEM Tech Fuel Cells](../energy/sem-tech-fuel-cells.md).

**Metal reduction**: Hydrogen can replace carbon (coke) as the reducing agent in steelmaking and other metallurgical processes, eliminating CO₂ emissions: Fe₂O₃ + 3H₂ → 2Fe + 3H₂O.

**Chemical feedstock**: Hydrogen for hydrogenation reactions in petrochemical processing, fat hardening, and specialty chemical synthesis.

## Safety

Water electrolysis involves specific hazards that require careful management:

- **Hydrogen flammability and explosion risk**: Hydrogen forms flammable mixtures with air at 4-75% concentration and explosive mixtures at 18-59%. Hydrogen flames are nearly invisible in daylight. All hydrogen handling areas require ventilation (natural or forced), hydrogen gas detectors, elimination of ignition sources, and bonding/grounding to prevent static discharge. Enclosed spaces where hydrogen can accumulate are particularly dangerous.
- **Oxygen enrichment**: The oxygen byproduct enriches ambient air if released in enclosed spaces, dramatically increasing fire risk. Materials that are normally difficult to ignite burn vigorously in oxygen-enriched atmospheres. Oxygen should be vented outdoors or collected for use.
- **Gas crossover**: The most serious safety concern in PEM cells. If H₂ and O₂ mix within the cell (due to membrane failure or excessive gas crossover), the resulting mixture is explosive. Gas monitoring on both product streams is essential. Commercial PEM systems shut down automatically if gas purity drops below safe thresholds.
- **Electrical safety**: Electrolysis cells operate at high current (hundreds to thousands of amps) and low voltage (1.8-2.2V per cell, but stacks can reach 200-400V). DC current at these levels causes severe burns and cardiac arrest. All electrical connections must be insulated, and maintenance must follow lockout/tagout procedures.
- **Deionized water handling**: While not hazardous itself, deionized water feed systems must be kept free of contaminants that could damage the membrane or catalysts.
- **Pressure hazards**: If the cell operates under pressure (common in commercial systems), hydrogen and oxygen lines must be rated for the operating pressure. Pressure relief devices are mandatory on all pressurized gas lines and vessels.


## Technology Readiness

SEM Tech membranes are at **TRL 5 for chlor-alkali applications**. For PEM water electrolysis specifically, the technology is at approximately **TRL 2-3** (conceptual, with basic laboratory characterization needed). Key gaps:

- **No proton conductivity data**: The membrane's proton transport properties have not been measured. This is the single most critical parameter for PEM electrolysis viability.
- **No gas crossover data**: Hydrogen and oxygen permeation rates through the membrane are unknown. Gas crossover must be below safety thresholds for practical use.
- **No water uptake data**: PEM membranes must absorb water to conduct protons. The PVC/CPVC binder may limit water absorption compared to perfluorinated polymers.
- **No elevated temperature data**: PEM cells benefit from temperatures above ambient. SEM Tech membrane performance at 50-80C is uncharacterized.
- **No long-term durability data in PEM environment**: Months of operation in chlor-alkali conditions does not guarantee equivalent lifetime in continuous PEM water electrolysis.

## Economic Considerations

Even if technically successful, SEM Tech PEM electrolysis would face challenges:

- **Precious metal catalysts**: PEM cells still require platinum (cathode) and iridium oxide (anode) catalysts, regardless of membrane choice. These materials are expensive and scarce.
- **Stack balance of plant**: Membrane cost is one component of total system cost. Bipolar plates, pumps, power electronics, and gas processing equipment also contribute significantly.
- **Scale**: SEM Tech is demonstrated at laboratory scale only. Industrial PEM electrolysis plants produce thousands of tonnes of hydrogen per year.


## Step-by-Step Procedure

The following procedure describes construction and operation of a bench-scale PEM water electrolysis cell using a SEM Tech membrane. This is a **projected procedure** — SEM Tech membranes have not been tested in PEM water electrolysis. Parameters are adapted from conventional PEM practice and SEM Tech's demonstrated chlor-alkali properties.

## Phase 1: Fabricate PEM Membrane

1. **Source cation exchange resin**: Strong acid cation resin (sulfonated polystyrene, IEC 1.8-2.2 meq/g, gel-type preferred for higher conductivity). Pulverize by ball milling to <150 μm. Sieve to remove >200 μm particles.
2. **Prepare binder solution**: Dissolve PVC or CPVC (K-value 55-65) in THF at 12-18% w/v. Stir 2-4 hours until homogeneous. CPVC preferred for higher temperature tolerance in PEM service.
3. **Mix PEM membrane slurry**: Combine resin powder at 50-60% by volume with binder solution. Mix on planetary mixer for 30-60 minutes. Target: uniform dispersion, no agglomerates >300 μm. Degas under vacuum 10 minutes.
4. **Cast thin membrane**: Using a precision drawdown bar, cast slurry onto clean glass at 100-200 μm wet thickness. **Thinner is better** for PEM — target dry thickness 50-100 μm to minimize proton transport resistance. Multiple thin coats (2-3 layers at 50-80 μm wet) give better uniformity than one thick coat.
5. **Dry and condition**: Air-dry 2-4 hours. Peel from glass. Condition in 0.5M H₂SO₄ for 12 hours (protonates all sulfonic acid sites). Rinse with deionized water. Store in DI water — never let dry.

## Phase 2: Prepare Electrodes

6. **Anode preparation (oxygen evolution)**: For bench-scale testing, use porous titanium felt or sintered titanium fiber (1-3 mm thick, porosity 70-80%). If catalyst coating is available, apply IrO₂ by thermal decomposition: paint with H₂IrCl₆ solution in isopropanol, dry at 100°C, calcine at 400°C for 10 minutes. Repeat 5-10 times for loading of 1-3 mg Ir/cm². For lowest-cost testing, use uncoated graphite plate — it will erode over days/weeks but suffices for proof-of-concept.
7. **Cathode preparation (hydrogen evolution)**: Carbon cloth or carbon paper (toray paper, 200-400 μm thick). If catalyst is available, apply Pt/C catalyst ink (40% Pt on Vulcan XC-72 carbon, dispersed in Nafion solution + isopropanol) by brush painting or spray coating. Target: 0.5-2.0 mg Pt/cm². For lowest-cost testing, uncoated carbon cloth works — higher overpotential but functional.
8. **Cut to size**: Cut membrane and both electrodes to identical active area (e.g., 50 mm × 50 mm for bench-scale cell). Mark electrode sides clearly (anode vs cathode).

## Phase 3: Assemble the Cell

9. **Prepare end plates**: Two titanium or stainless steel plates (10-15 mm thick) with machined flow fields (parallel channels, 1-2 mm wide × 1-2 mm deep, at 2-3 mm pitch). Drill inlet and outlet ports (3-6 mm) for water feed and gas exit on each plate. Install O-ring gaskets (Viton or EPDM) around the active area perimeter on each plate.
10. **Assemble sandwich**: Place components on bottom end plate in order: (a) anode electrode (Ti felt or graphite, facing up), (b) SEM Tech membrane (hydrated, centered), (c) cathode electrode (carbon cloth, facing down), (d) top end plate. Ensure membrane completely covers both electrodes — any exposed electrode area causes direct gas mixing.
11. **Clamp**: Bolt end plates together with 4-8 bolts in a symmetric pattern. Tighten gradually in a cross pattern to 2-5 N·m torque. Over-compression damages the membrane; under-compression causes leaks.
12. **Seal test**: Pressurize the water feed channel with DI water at 0.1-0.3 bar. Check for cross-leakage (water appearing on the gas side). Verify electrical isolation between end plates (no short circuit through the assembly).

## Phase 4: Connect Systems and Commission

13. **Connect water feed**: Plumb a DI water reservoir to the anode inlet using PTFE or PVC tubing. Use a peristaltic pump at 5-20 mL/min (low flow rate for bench-scale). Water flows through the anode chamber, contacts the anode, and carries away produced oxygen gas.
14. **Connect gas collection**: Connect anode gas outlet to an inverted water-filled graduated cylinder (to collect and measure O₂ volume). Connect cathode gas outlet to a separate cylinder (to collect H₂). Ensure both gas paths vent to a well-ventilated area or fume hood.
15. **Connect power supply**: Connect a DC power supply (0-5V, 0-20A for bench-scale) — positive to anode, negative to cathode. Verify polarity with multimeter before connecting.
16. **Start water flow**: Turn on the peristaltic pump. Verify water fills the anode chamber and exits the gas outlet without leaking. Check cathode side is dry initially — water will appear there as protons drag water through the membrane during operation.
17. **Energize at low current**: Set power supply to constant current mode. Start at 50 mA/cm² (125 mA for a 2.5 cm² cell). Record cell voltage — should read 1.5-2.5V. If voltage exceeds 3.0V, check for poor electrical contact or membrane dehydration.
18. **Ramp to operating current**: Gradually increase current density over 30-60 minutes. Target: 200-500 mA/cm² for SEM Tech membrane (conservative; conventional PEM operates at 1000-3000 mA/cm²). Monitor voltage at each step — voltage should increase linearly with current (ohmic behavior). A sudden voltage spike indicates membrane drying or gas blockage.
19. **Monitor gas production**: H₂ should appear at the cathode gas outlet within seconds of applying current. Measure H₂ flow rate — at 100% Faradaic efficiency, 1 A produces 0.21 L/h of H₂ at STP. Compare measured vs theoretical to estimate Faradaic efficiency. Check H₂ purity with a gas analyzer if available — target >99.5%.
20. **Steady-state operation**: Once stable at target current, log voltage, current, gas production rate, and temperatures every 15-30 minutes. A well-functioning cell maintains stable voltage for hours. Gradual voltage increase over days/weeks indicates membrane degradation or catalyst deactivation.

## Phase 5: Shutdown and Maintenance

21. **Shutdown**: Reduce current to zero. Turn off power supply. Continue water flow for 5 minutes to flush gases. Turn off pump. Drain water from both sides.
22. **Membrane storage**: Remove membrane from cell. Store in DI water in a sealed container. Label with date and operating hours. Do not allow to dry — dried SEM Tech membranes may crack.
23. **Performance tracking**: Record cumulative operating hours, average cell voltage, and Faradaic efficiency. Replace membrane when voltage at operating current increases >20% from initial value (indicating degradation). For SEM Tech membranes, projected replacement interval: 1,000-5,000 operating hours (versus 40,000-80,000 for Nafion).

## Membrane Fabrication for PEM Cells

The SEM Tech membrane for water electrolysis would use the same fabrication process as for chlor-alkali cells, with specific adaptations. Strong acid cation resin beads (sulfonated polystyrene, ion exchange capacity 1.8-2.2 meq/mL) are pulverized to below 200 microns and dispersed at 40-60% loading by volume in PVC or CPVC binder dissolved in THF. The mixture is cast at 50-150 microns wet thickness using a drawdown bar or spray coating — thinner than chlor-alkali membranes to minimize proton transport resistance.

A 100-micron-thick SEM Tech membrane at 50% resin loading contains approximately 100 g of active resin per square meter, providing ion exchange capacity of 1.0-1.1 meq/g × 100 g = 100-110 meq/m². For comparison, Nafion 117 at 183 microns provides approximately 90-100 meq/m² of sulfonic acid groups. The theoretical proton conductivity of the SEM Tech membrane depends on water uptake: fully hydrated sulfonated polystyrene conducts protons at 0.01-0.10 S/cm, while the PVC/CPVC binder is electrically insulating. The effective membrane conductivity is therefore determined by the volume fraction and connectivity of the resin particles, estimated at 0.003-0.03 S/cm for 40-60% loading — lower than Nafion (0.1 S/cm) but potentially adequate for operation at reduced current density.

## Cost Impact on Hydrogen Production

The membrane cost reduction from SEM Tech directly affects the levelized cost of hydrogen (LCOH). For a 10 MW PEM electrolyzer operating at 2.0V per cell with 500 m² of active membrane area:

| Cost Component | Nafion Membrane | SEM Tech Membrane |
|---------------|----------------|-------------------|
| Membrane purchase (500 m²) | $250,000-1,000,000 | $500-5,000 |
| Membrane replacement (every 2 years) | $125,000-500,000/year | $250-2,500/year |
| Stack capital cost | $4,000-8,000/kW | $2,500-5,000/kW (projected) |
| LCOH contribution from membrane | $0.30-1.20/kg H₂ | $0.001-0.006/kg H₂ |
| Total LCOH (all components) | $4.00-6.00/kg H₂ | $3.00-4.50/kg H₂ |

Even with a conservative 50% reduction in stack cost (not the full 95% membrane cost reduction, since bipolar plates, electrodes, and balance-of-plant are also significant), the LCOH decreases by $0.50-1.50/kg — meaningful when the target is $2.00/kg for cost-competitive green hydrogen. The electrolyzer stack represents 30-50% of total system cost; SEM Tech membranes reduce this to 20-30%, shifting the cost burden toward electricity and balance of plant.

## Scaling and Deployment

**Residential scale (1-5 kg H₂/day)**: A single ED cell with 100-500 cm² active area operating at 500 mA/cm² and 2.0V produces approximately 0.02-0.10 kg H₂/hour. Requires 0.2-1.0 kW DC power — compatible with a single solar panel. Membrane cost: $0.10-0.50. Suitable for home energy storage (H₂ → fuel cell → electricity) or small welding operations.

**Commercial scale (50-500 kg H₂/day)**: A 10-100 cell stack with 1,000-5,000 cm² active area per cell at 1,000 mA/cm². Requires 20-200 kW DC power. Membrane cost: $10-100. Suitable for fleet vehicle refueling, industrial hydrogen consumers, and small ammonia production.

**Industrial scale (1,000-50,000 kg H₂/day)**: Multiple parallel stacks totaling 100-5,000 m² membrane area at 1,000-3,000 mA/cm². Requires 2-100 MW DC power. Membrane cost: $1,000-50,000 (compared to $500,000-20,000,000 for Nafion). Suitable for refinery hydrogen, large-scale ammonia synthesis, and steel direct reduction.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Cell voltage exceeds 3.0V at low current density | Membrane dehydration — DI water flow insufficient to maintain hydration of sulfonic acid groups for proton conduction | Verify DI water feed at 5-20 mL/min for bench-scale; ensure membrane was conditioned in 0.5M H₂SO₄ for 12 hours before use |
| Hydrogen purity below 99.5% (O₂ detected in H₂ stream) | Gas crossover through pinholes or excessively thin membrane (<50 μm) allowing O₂ to permeate to cathode side | Inspect membrane for pinholes before assembly; increase membrane thickness to 100-150 μm; ensure membrane fully covers both electrodes |
| Cell voltage gradually increasing over days of operation | Membrane degradation (PVC binder oxidation) or catalyst deactivation increasing internal resistance | Track voltage trend continuously; replace membrane when voltage at operating current increases >20% from initial baseline value |
| No hydrogen production at cathode despite applied current | Electrode polarity reversed — anode connected to negative terminal, cathode to positive | Verify polarity with multimeter before energizing: positive terminal to anode (O₂ evolution), negative to cathode (H₂ evolution) |
| Sudden voltage spike during current ramp-up | Gas bubbles blocking flow channels at high current density, creating localized dry spots on membrane | Reduce current density; verify water flows freely through anode chamber; clear gas blockage by increasing water flow rate temporarily |
| Membrane cracks or delaminates after removal from cell | Membrane allowed to dry out — PVC/CPVC binder matrix loses flexibility and cracks when dehydrated | Store membrane in DI water in sealed container at all times; never allow SEM Tech membrane to dry during or after operation |
| Anode electrode eroding within days | Uncoated graphite anode in acidic PEM environment (pH 2-4 at anode) — graphite oxidizes under oxygen evolution conditions | Apply IrO₂ catalyst coating by thermal decomposition (1-3 mg Ir/cm²) or switch to porous titanium felt anode for longer life |
| Excessive water accumulation on cathode side | Electro-osmotic drag — protons (H⁺) dragging water molecules through membrane during operation | Expected behavior at current densities above 200 mA/cm²; ensure cathode gas path has drainage for liquid water removal |
| Faradaic efficiency below 90% (less H₂ produced than theoretical) | Electrical short circuit between end plates, or parasitic side reactions consuming current | Verify electrical isolation between end plates (no contact through assembly); check all gaskets are properly seated preventing internal shorts |
| Membrane performance degrades at 50-80°C operating temperature | PVC binder softening above its glass transition temperature (~80°C), causing dimensional changes in membrane matrix | Use CPVC binder (higher Tg ~100-120°C) instead of PVC for elevated-temperature PEM operation; or restrict operation to ambient temperature |

## See Also

- [SEM Tech](sem-tech.md) -- the membrane technology that enables this application
- [Electrolysis](electrolysis.md) -- parent article covering all industrial electrolysis processes
- [Alkali Production](alkalis.md) -- NaOH production via electrolysis (chlor-alkali context)
- [SEM Tech Fuel Cells](../energy/sem-tech-fuel-cells.md) -- consuming hydrogen in fuel cells (forthcoming)
- [SEM Tech e-Methanol](sem-tech-e-methanol.md) -- converting hydrogen to liquid fuel (forthcoming)



[← Back to Chemistry](index.md)
