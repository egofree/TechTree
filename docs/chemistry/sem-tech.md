# Semiconductor-Grade Electrolysis

> **Node ID**: chemistry.electrolysis.sem-tech
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`Electrolysis`](electrolysis.md)
> **Enables**: Various downstream capabilities
> **Timeline**: Years 30-50
> **Outputs**: membrane_electrolysis, chlorine, caustic_soda
> **Critical**: No

## Overview

Membrane electrolysis cells producing ultra-pure chlorine and caustic soda for semiconductor manufacturing. Uses ion-exchange membranes instead of asbestos diaphragms, achieving higher purity required for wafer processing chemicals.

SEM Tech membrane technology uses off-the-shelf water softener resin beads, pulverized and dispersed in a PVC or CPVC binder matrix, to form ion exchange membranes at less than $1 per square foot. Conventional perfluorinated membranes (Nafion) cost $100-400 per square foot. The tradeoff is durability: SEM Tech membranes last months to a year at pH 0 and ORP above 1.5V, compared to 2-4 years for Nafion. For a bootstrapping civilization, the cost difference makes SEM Tech the practical starting point.

The SEM Tech approach was developed by Robert Karas (Rowow LLC) as an open-source method. The core idea is that pre-functionalized ion exchange resin beads already contain the charged groups (sulfonate for cation exchange, quaternary ammonium for anion exchange) that expensive polymer chemistry normally builds into membranes from scratch. By pulverizing these beads and dispersing them in a cheap PVC binder, you get a functional membrane using household equipment: a blender, a solvent, and a flat surface for casting.

Primary outputs: `membrane_electrolysis`, `chlorine`, `caustic_soda`. The chlorine feeds HCl synthesis and PVC production. The caustic soda (NaOH) is the workhorse base for wafer cleaning, etching, and pH control across the fab. Both must meet semiconductor-grade purity: trace metals below parts-per-billion, particle counts below 10 per mL at 0.2 μm.

The membranes work by Donnan exclusion. Cation exchange membranes carry negatively charged groups (sulfonate, carboxylate) that repel anions and allow cations through. Anion exchange membranes carry positively charged groups (quaternary ammonium) that do the reverse. Selectivity, electrical resistance, and chemical stability are the three performance metrics that matter.

Homogeneous membranes (charged groups bonded directly to the polymer backbone) offer better selectivity and lower resistance than heterogeneous types (resin particles in a binder), but they are harder to manufacture. SEM Tech membranes are a hybrid: the ion exchange resin particles are homogeneous in themselves, but they are embedded in a non-conductive PVC matrix. The current must hop between resin particles, adding resistance compared to a fully homogeneous sheet. The practical impact is modest at the cell thicknesses used in electrolysis.

## Prerequisites

### Materials

- Ion exchange resin beads (water softener grade, strong acid cation or strong base anion)
- PVC or CPVC resin and solvent (THF, cyclohexanone, or MEK)
- Saturated NaCl brine (purified to Ca²⁺ + Mg²⁺ below 20 ppb for membrane protection)
- Deionized water (resistivity above 1 MΩ·cm)
- Titanium or steel cell frames and current collectors (titanium for anode side in acidic conditions; steel acceptable for cathode side)
- Dimensionally stable anode (DSA) material: titanium mesh coated with RuO₂/IrO₂, or graphite as a cheaper but consumable alternative

### Equipment

- [Electrolysis](electrolysis.md) — tool dependency (DC power supply, cell frames, electrodes)

### Knowledge

- Ion exchange membrane fabrication: resin pulverization, dispersion in polymer binder, film casting
- Brine purification chemistry (CaCO₃ precipitation, Mg(OH)₂ precipitation, ion exchange polishing)
- Cell voltage monitoring and current efficiency calculation for membrane cell operation
- Trace metal analysis and particle counting for semiconductor-grade product verification

### Infrastructure

- Clean casting surface (glass or polished steel) for membrane film formation
- Ventilated solvent handling area for THF, cyclohexanone, or MEK
- Brine purification train (precipitation tanks, filters, ion exchange columns). Raw salt solution contains Ca²⁺, Mg²⁺, SO₄²⁻, and heavy metals that poison electrodes and destroy membranes. The purification sequence adds Na₂CO₃ (precipitates CaCO₃), NaOH (precipitates Mg(OH)₂), and BaCl₂ (precipitates BaSO₄ if sulfate exceeds 5 g/L), followed by filtration and ion exchange polishing.
- Dry, dust-free storage for finished membranes (must be kept hydrated in sealed bags with process brine)

## Process Description

SEM Tech membrane manufacturing starts with pulverizing commercial ion exchange resin beads to particle size below 200 μm using a blender or ball mill. The pulverized resin is mixed with PVC or CPVC dissolved in solvent (THF or cyclohexanone) to form a slurry. The slurry is spread onto a flat surface (glass sheet or polished steel plate) with a doctor blade to control thickness. The solvent evaporates at ambient temperature over several hours, leaving a flexible ion exchange membrane that peels off the casting surface.

For cation exchange membranes, use strong acid cation resin (sulfonated polystyrene, the same material in water softeners). For anion exchange membranes, use strong base anion resin (quaternary ammonium functionalized polystyrene). Bipolar membranes are made by laminating a cation layer and anion layer together with a thin catalyst interface between them.

Membrane degradation occurs through three mechanisms. Chemical degradation happens when oxidizing agents (peroxide radicals formed during electrolysis) attack the polymer binder. Mechanical degradation comes from swelling and shrinking during wet/dry cycles, which creates stress cracks. Fouling from organic or inorganic deposits blocks ion transport pathways. SEM Tech membranes are more susceptible to chemical degradation than Nafion because the PVC binder is less chemically inert than perfluorinated polymer. The mitigation strategy is simple: replace membranes when performance degrades, which is economically feasible when each membrane costs under $1 per square foot.

Faraday's law applied to chlor-alkali membrane cells: at 90% current efficiency, a cell drawing 10 kA produces 11.9 kg Cl₂ per hour (theoretical production rate: 1.324 kg Cl₂ per kA·hour from the reaction 2Cl⁻ → Cl₂ + 2e⁻). The same cell produces 13.4 kg NaOH per hour and 0.374 kg H₂ per hour as co-products. These production rates scale linearly with current, making capacity planning straightforward once cell performance is characterized. A cell drawing 5 kA produces exactly half as much.

The choice of solvent for membrane casting affects both the casting process and the final membrane quality. THF evaporates quickly (boiling point 66°C), producing a dense membrane in 4-8 hours but with higher risk of bubble formation from rapid solvent escape. Cyclohexanone evaporates slowly (boiling point 156°C), requiring 12-24 hours for complete drying but producing a more uniform film with fewer defects. MEK (methyl ethyl ketone, boiling point 80°C) is a middle ground. For initial experimentation, THF is convenient because of its fast evaporation. For production membranes where consistency matters, cyclohexanone produces better results despite the longer drying time.

All solvent handling requires adequate ventilation. THF vapor has a sweet odor and a TLV (threshold limit value) of 200 ppm. MEK has a sharp, acetone-like odor and a TLV of 200 ppm. Cyclohexanone has a peppermint-like odor and a lower TLV of 25 ppm, making it the most hazardous of the three by inhalation exposure.

The membrane is installed in an electrolysis cell frame between anode and cathode compartments. Saturated, purified brine feeds the anode side. The membrane allows Na⁺ ions to pass to the cathode compartment while blocking Cl⁻ and OH⁻. Chlorine gas evolves at the anode. Hydrogen gas and NaOH solution form at the cathode.

### Step-by-Step Procedure

1. Pulverize ion exchange resin beads in a ball mill or blender until particle size is below 200 μm. Sieve to remove oversize particles. Dry the powder at 60°C for 2 hours.
2. Dissolve PVC resin (10-15% by weight) in THF or cyclohexanone. Stir until fully dissolved (2-4 hours). Add pulverized ion exchange resin at 30-50% of total solids weight. Mix thoroughly to form a uniform slurry.
3. Cast the slurry onto a clean glass plate using a doctor blade set to 200-500 μm gap. Work in a well-ventilated area; THF vapor is flammable and a neurotoxin.
4. Allow solvent to evaporate at ambient temperature (6-12 hours). Peel the finished membrane from the glass surface. Trim to cell frame dimensions.
5. Hydrate the membrane in process brine for 12-24 hours before installation. Never let the membrane dry out after hydration; drying causes irreversible cracking and loss of ion exchange capacity.
6. Install the membrane in the cell frame with gaskets on both sides. Tighten cell bolts evenly to avoid pinching or tearing. Verify no leaks with a pressure test using deionized water before introducing brine.

7. Begin brine flow to the anode compartment and deionized water to the cathode compartment. Apply DC current at 25% of rated value and ramp up over 30 minutes. Monitor cell voltage (target 2.9-3.5V), current efficiency (target above 90%), and product purity (NaOH concentration, Cl₂ gas quality). Record all parameters for the first 4 hours of operation as the membrane conditions.

8. After 24 hours of operation, shut down and inspect the membrane for swelling, wrinkling, or delamination. These early signs of incompatibility between the membrane and the process conditions are easier to address before the membrane has been under load for weeks. Adjust binder composition (more PVC for mechanical strength, more resin for conductivity) based on observations.

9. For ongoing operation, maintain a membrane replacement schedule. SEM Tech membranes typically last 6-12 months. Track performance degradation (rising cell voltage, falling current efficiency) and replace proactively rather than waiting for membrane failure, which can cause Cl₂/NaOH cross-contamination.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Resin particle size | < 200 μm | Coarser particles create pinholes and weak spots |
| Membrane thickness (dry) | 200-500 μm | Thinner = lower resistance but mechanically fragile |
| Ion exchange capacity | 1.5-3.0 meq/g dry resin | Higher IEC = lower resistance but more swelling |
| Cell operating temperature | 80-95°C | Higher temperature reduces voltage but accelerates membrane degradation |
| Current density | 2-5 kA/m² | Above 5 kA/m² causes excessive heating and membrane damage |
| NaOH product concentration | 30-33% | Higher concentration requires evaporation; membrane cells produce this directly |
| Energy consumption | 2,100-2,400 kWh/tonne Cl₂ | Major electricity load; the chlor-alkali process is one of the most power-intensive chemical operations |

## Safety Considerations

- **Solvent hazards**: THF is flammable (flash point -14°C) and forms explosive peroxides on storage. Work in a ventilated area away from ignition sources. Add peroxide inhibitors to stored THF. Cyclohexanone is less flammable but a skin irritant. MEK has a flash point of -6°C. All three require respiratory protection during casting.
- **Chlorine gas**: The electrolysis cell produces Cl₂ at the anode. Cl₂ is toxic (IDLH 10 ppm) and heavier than air. Cell rooms require forced ventilation, continuous Cl₂ monitoring at floor level, and an emergency NaOH scrubber capable of absorbing the full cell room chlorine inventory.
- **Hydrogen gas**: Evolved at the cathode. Explosive in air at 4-75% concentration. Never allow Cl₂ and H₂ to mix; the mixture is explosive over a wide range (4-93% H₂ in Cl₂). Purge all gas lines with nitrogen before startup.
- **Caustic soda**: NaOH at 30-33% concentration causes severe chemical burns. Eye exposure can cause permanent blindness. Full chemical splash protection is mandatory when handling product NaOH.

### Personal Protective Equipment

- Chemical splash goggles and face shield when handling solvents, brine, or NaOH product
- Nitrile or neoprene gloves for solvent work; rubber gloves for NaOH handling
- Respirator with organic vapor cartridge during membrane casting (THF, MEK)
- Flame-resistant lab coat or apron when working near solvents or the electrolysis cell
- Emergency eyewash station and safety shower within 10 seconds of the work area

### Emergency Procedures

- **THF spill**: Evacuate ignition sources. Absorb with vermiculite or sand. Ventilate the area. Do not flush to drain (flammable). THF is a peroxide former; old THF that has been stored for months may contain explosive peroxide crystals. Test with peroxide test strips before handling aged stock.
- **Chlorine leak**: Activate emergency NaOH scrubber. Evacuate cell room (Cl₂ accumulates at floor level). Full-face supplied-air respirator for re-entry. Do not attempt repair without respiratory protection. Post a watch at the door to prevent unauthorized entry.
- **NaOH splash**: Flush skin with water for 15 minutes minimum. For eye contact, irrigate continuously and seek immediate medical attention. Remove contaminated clothing under the shower. NaOH burns may not be immediately painful because the nerve damage is delayed; flush regardless of whether pain is felt.
- **Membrane rupture during operation**: Shut off DC power immediately. Isolate the cell. The Cl₂/NaOH cross-contamination from a ruptured membrane produces heat and bleach (NaOCl). Drain both compartments before servicing. Replace the membrane and inspect the cell frame for the cause of the rupture (sharp edges, uneven gasket compression, foreign object).

## Quality Control

### Acceptance Criteria

- **Membrane Electrolysis**: Current efficiency above 90%. Cell voltage 2.9-3.5V at rated current density. No detectable Cl₂ in cathode compartment or H₂ in anode compartment (gas crossover indicates membrane failure). The presence of even 0.5% H₂ in the Cl₂ stream requires immediate investigation because the explosive limit is 4% H₂ in Cl₂.
- **Chlorine**: Purity above 99% by volume. Moisture below 50 ppm (after drying). H₂ content below 0.1% (explosive risk above 4%). The hydrogen from the cathode is also collected: H₂ purity above 99.5% with Cl₂ contamination below 10 ppm.
- **Caustic Soda**: NaOH concentration 30-33%. NaCl contamination below 50 ppm (for semiconductor grade, below 10 ppm for standard industrial grade). Trace metals (Fe, Ni, Ca, Mg) each below 10 ppb for semiconductor applications.

### Testing Methods

- **Membrane resistance**: Measure voltage drop across the membrane at known current density. Compare to specification (typically 0.1-0.5 Ω·cm²). Rising resistance indicates fouling or degradation.
- **Current efficiency**: Calculate from NaOH production rate vs. theoretical (Faraday's law). Efficiency below 90% indicates OH⁻ back-migration through the membrane. At 90% current efficiency, 10% of the electrical input is wasted on parasitic reactions (primarily oxygen evolution at the anode instead of chlorine evolution).
- **Chlorine purity**: Gas chromatography or wet chemistry (absorb in KI solution and titrate the liberated iodine with sodium thiosulfate). Moisture by dew point measurement or gravimetric drying tube.
- **NaOH trace metals**: ICP-MS (inductively coupled plasma mass spectrometry) for ppb-level metal analysis. Atomic absorption spectroscopy as a simpler alternative. For semiconductor-grade NaOH, the critical metals are Fe (<10 ppb), Ni (<5 ppb), Ca (<10 ppb), Mg (<10 ppb), and Cu (<5 ppb).
- **Particle counting**: Semiautomatic particle counter measuring particles above 0.2 μm in the NaOH product. Semiconductor-grade NaOH must have fewer than 10 particles per mL at this size. Particles originate from cell debris, gasket wear, and airborne contamination during packaging.

### Sampling Protocol

- Measure cell voltage and current hourly during operation. Plot trends; rising voltage signals membrane fouling or electrode degradation.
- Sample NaOH product daily for concentration and NaCl contamination. Sample weekly for trace metals.
- Test membrane resistance before installation and monthly during operation. Replace when resistance exceeds 150% of initial value or current efficiency drops below 85%.
- Monitor Cl₂ purity continuously with an in-line analyzer. Alarm on H₂ content above 0.5% in the chlorine stream (approaching the lower explosive limit of 4% H₂ in Cl₂).
- Track cumulative operating hours per membrane. SEM Tech membranes in chlor-alkali service typically show measurable degradation after 3,000-6,000 hours. Keep spare membranes cast and hydrated in storage to avoid unplanned downtime.

## Scaling Notes

- **Bench scale (single cell, 100 cm² membrane)**: Hand-cast membrane, laboratory DC power supply, glass or acrylic cell body. Produces grams of NaOH per hour. Validates membrane fabrication and measures performance parameters. One operator.
- **Pilot scale (10-50 cells, 0.1-0.5 m² per cell)**: Semi-automated membrane casting, purpose-built cell frames, dedicated rectifier. Produces kilograms of NaOH and Cl₂ per day. Reveals scaling issues with brine distribution, gas handling, and heat management.
- **Production scale (100+ cells, 1-4 m² per cell)**: Continuous membrane casting line, filter-press cell stack, industrial rectifier (200-400V DC, 5-30 kA). Produces tonnes per day. Requires full brine purification train, gas drying and compression, and NaOH evaporation if 50% product is needed.

The SEM Tech approach lowers the barrier at every scale because the membranes cost pennies per square foot instead of hundreds of dollars. Shorter membrane life (6-12 months vs. 2-4 years for Nafion) is acceptable when replacement cost is negligible.

At production scale, the cell room itself becomes a significant infrastructure investment. A membrane cell room with 100 cells, each at 2 m² active area, drawing 10 kA at 300V DC, produces roughly 350 tonnes of Cl₂ per year and 400 tonnes of NaOH. The rectifier, bus bars, brine purification train, gas handling systems, and cell room ventilation together represent an investment comparable to a small chemical plant. The SEM Tech membrane cost savings are most significant at this scale, where conventional Nafion membrane replacement would cost $200,000-400,000 every 2-4 years.

The cell room must be designed for chlorine safety. Forced ventilation at 6-12 air changes per hour. Chlorine detection at floor level (Cl₂ is 2.5× heavier than air). An emergency NaOH scrubber on automatic activation, sized to absorb the entire cell room chlorine inventory within 30 minutes. The cell room is maintained at slight negative pressure relative to surrounding areas. All electrical equipment must be rated for corrosive atmospheres (chlorine attacks copper wiring and steel enclosures).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Cell voltage rising above 4.0V | Membrane fouling from Ca²⁺/Mg²⁺ precipitation in membrane pores; or electrode coating degradation | Verify brine purification: Ca²⁺ + Mg²⁺ must be below 20 ppb. Polish brine with chelating ion exchange resin. Clean or replace electrodes. |
| NaOH product contaminated with NaCl (>100 ppm) | Membrane pinhole or tear allowing brine leakage; or membrane not properly sealed in cell frame | Pressure test the membrane before installation. Replace damaged membranes. Verify gasket compression is even across the cell. |
| Current efficiency below 85% | OH⁻ ions back-migrating through degraded membrane; or brine concentration too low (below 25%) | Replace membrane. Maintain brine at 25-28% NaCl. Check that membrane is correctly oriented (cation exchange layer facing anode). |
| Membrane cracks after storage | Membrane dried out during storage, causing irreversible shrinkage and stress cracking | Store membranes sealed in brine-filled bags. Never let hydrated membranes dry. Discard cracked membranes; they cannot be repaired. |
| Cl₂ gas contains >1% O₂ | Water oxidation competing with chloride oxidation at the anode, caused by low NaCl concentration or high current density | Increase brine concentration to 25%+. Reduce current density below 5 kA/m². Check for anode coating degradation. |

## Variations and Alternatives

- **Nafion (perfluorinated) membranes**: The industrial standard. Exceptional chemical stability in oxidizing, reducing, acidic, and basic environments. Requires mature fluoropolymer chemistry. Cost $500-2,000/m². The target to work toward, not the starting point.
- **Asbestos diaphragm cells**: The historical alternative. Deposited asbestos fiber on the cathode screen. Lower purity product (10-12% NaOH with 15% NaCl). Asbestos is a known carcinogen. phased out in most countries but technically simple.
- **Bipolar membrane electrodialysis (EDBM)**: A bipolar membrane splits water into H⁺ and OH⁻ directly, generating acid and base from a salt solution without electrodes. Used for organic acid production and acid-base recovery from waste salt streams.
- **Heterogeneous membranes**: Ion exchange resin particles embedded in an inert polymer matrix (polyethylene, PVC). Easier to manufacture than homogeneous membranes but lower selectivity and higher resistance. A middle ground between SEM Tech and Nafion.

- **Electrodialysis**: Instead of producing chlorine and NaOH, electrodialysis uses alternating cation and anion membranes to desalinate water or concentrate salts. Multiple cell pairs between a single set of electrodes multiply the throughput. Used for brackish water desalination and salt concentration. The SEM Tech membrane approach works for electrodialysis cells as well.

## References

- [Electrolysis](electrolysis.md) — parent capability
- [Chemistry Domain](./index.md) — domain overview and related capabilities
- [Electrolysis](electrolysis.md) — upstream dependency (tool)

### Material Handling

Ion exchange membranes must be kept hydrated at all times after initial wetting. Store spare membranes in sealed plastic bags with enough process brine to keep them immersed. Handle with wet, clean hands or nitrile gloves. Oil and grease from bare hands contaminate the membrane surface and increase resistance.

Pulverized ion exchange resin is a fine dust. Handle with a dust mask; inhalation irritates the respiratory tract. Store resin powder in sealed containers away from moisture (dry resin absorbs water and clumps, making uniform dispersion harder).

Spent membranes from industrial processes may be classified as hazardous waste depending on what chemicals they have contacted. Segregate spent membranes for proper disposal. Do not burn PVC-based membranes (releases HCl gas and dioxins).

THF and cyclohexanone are regulated solvents. Store in approved flammable liquid cabinets. Keep peroxide inhibitors in THF stock and test for peroxide accumulation monthly (peroxide test strips). Dispose of solvent waste through licensed channels. Never distill THF to dryness; concentrated peroxides can detonate.

The membrane industry is concentrated among a small number of manufacturers worldwide, making membrane technology a potential bottleneck for developing chemical processing capability. Building indigenous membrane manufacturing, even at the SEM Tech level, requires expertise in polymer handling, film casting, and ion exchange chemistry. These skills overlap with but are distinct from the chemical process engineering needed to operate the separation equipment. A civilization bootstrapping its chemical industry should develop membrane fabrication capability in parallel with electrolysis process capability, since the two reinforce each other.

The development trajectory from simple to advanced membranes is well established historically. Early heterogeneous membranes (1950s) had poor selectivity. Homogeneous membranes (1970s) improved performance dramatically. Perfluorinated membranes (1980s-1990s) enabled the modern chlor-alkali industry. A bootstrapping civilization can follow this same progression, starting with SEM Tech heterogeneous membranes and advancing to homogeneous and perfluorinated types as polymer chemistry capability matures over decades.

The economic case for SEM Tech membranes is compelling at every scale. At bench scale, a $1 membrane allows experimentation that would be prohibitively expensive with $500/m² Nafion. At pilot scale, the ability to replace membranes monthly for pennies means the process can be optimized with real operating data rather than theoretical projections. At production scale, the cumulative membrane cost over a plant lifetime is a rounding fraction of what Nafion would cost. The tradeoff is that SEM Tech membranes require more frequent shutdowns for replacement, but with proper cell design, a membrane change takes 1-2 hours per cell. which can be scheduled during planned maintenance outages.

The membrane casting process can be scaled up by replacing the batch doctor-blade method with a continuous roll-to-roll coater. A moving belt of release paper passes under a slot die that deposits a uniform wet film of the resin-PVC-solvent slurry. The belt carries the wet film through a drying tunnel (warm air, 40-60°C, 5-15 minutes residence time), and the dried membrane is peeled off and wound onto a roll. This continuous process is how industrial membrane manufacturers produce kilometers of membrane per day. At bench scale, the batch method (doctor blade on glass) is adequate for producing test membranes of 10-30 cm dimensions.

Membrane thickness is a critical parameter that affects both performance and durability. Thinner membranes (200-300 μm dry) have lower electrical resistance, reducing cell voltage and energy consumption. But thin membranes are mechanically fragile and more prone to pinhole defects that cause gas crossover. Thicker membranes (400-500 μm) are more robust but consume more power. The optimum depends on the application: for chlor-alkali where Cl₂/H₂ mixing is dangerous, thicker membranes with proven integrity are preferred over thin membranes with marginal gains in efficiency.

---
*Part of the [Bootciv Tech Tree](../../index.md) · [Chemistry](./index.md) · [All Domains](../../index.md)*
