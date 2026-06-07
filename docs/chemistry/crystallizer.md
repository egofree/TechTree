# Crystallizer

> **Node ID**: chemistry.crystallizer
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`chemistry.heat-exchanger`](heat-exchanger.md), [`chemistry.filter-press`](filter-press.md)
> **Enables**: [`chemistry.acids`](acids.md), [`chemistry.alkalis`](alkalis.md), [`chemistry.solvents`](solvents.md)
> **Timeline**: Years 15-30
> **Outputs**: crystals
> **Critical**: No — crystallization is the primary purification method for solid chemical products but distillation and extraction can substitute for liquid products

## Overview

A crystallizer produces solid crystals from a solution by creating supersaturation — the thermodynamic driving force for crystal nucleation and growth. Supersaturation is achieved by cooling the solution (cooling crystallization), evaporating solvent (evaporative crystallization), or adding an antisolvent that reduces solute solubility (antisolvent crystallization). Once supersaturated, the solution nucleates new crystals or grows existing seed crystals. Controlled crystallization produces large, pure crystals (0.1-5 mm) that are easily filtered and washed.

The governing relationship is the solubility curve: solubility (g solute per 100 g solvent) as a function of temperature. For substances with steep solubility curves (e.g., KNO₃: 13 g/100 g at 0°C to 247 g/100 g at 100°C), cooling crystallization is highly effective. For substances with flat solubility curves (e.g., NaCl: 35.7 g/100 g at 0°C to 39.1 g/100 g at 100°C), evaporative crystallization is preferred. The key design parameter is the supersaturation ratio (S = C/C*, where C is the actual concentration and C* is the equilibrium solubility). Typical operating range: S = 1.02-1.10. Too low: no crystallization. Too high: excessive nucleation produces fine powder ("fines") instead of coarse crystals.

The crystallizer must provide gentle agitation (to keep crystals suspended without breaking them), temperature control (to maintain the desired supersaturation level), and a means of removing crystals (classified product discharge or batch harvest). Three principal designs serve chemical processing: cooling crystallizers (batch, for steep solubility curves), forced-circulation evaporative crystallizers (continuous, for flat solubility curves), and draft-tube baffle (DTB) crystallizers (continuous, with fines destruction for narrow crystal size distribution).

Crystal size is controlled by the balance between nucleation rate (new crystal formation) and growth rate (enlargement of existing crystals). High supersaturation promotes nucleation over growth, producing many small crystals. Low supersaturation favors growth over nucleation, producing fewer but larger crystals. The crystal growth rate for most inorganic salts is 0.1-1.0 mm/hr under controlled supersaturation. At this rate, a 2 mm crystal requires 2-20 hours of growth time — explaining why crystallization batch cycles are typically 4-24 hours.

Crystal purity depends on the exclusion of impurities from the crystal lattice (most impurities are rejected during crystal growth) and the removal of mother liquor from the crystal surfaces after filtration. A single crystallization step typically achieves 95-99.9% purity. Higher purity requires re-crystallization (dissolve and re-crystallize) or careful washing of the filtered crystals to remove the mother liquor film.

Energy consumption for crystallization is dominated by the cooling duty (for cooling crystallizers, 5-50 kWh/m³) or the evaporation duty (for evaporative crystallizers, 100-400 kWh/m³). Multiple-effect evaporation reduces the energy cost of evaporative crystallization by 60-80% compared to single-effect operation.

## Prerequisites

- **[Heat exchanger](heat-exchanger.md)**: Jacket or external shell-and-tube for cooling or heating duty
- **[Filter press](filter-press.md)** or **[centrifuge](centrifuge.md)**: For crystal recovery from mother liquor
- **[Stainless steel](../metals/iron-steel.md)**: 316L for vessel and wetted parts (corrosion resistance)
- **[Temperature measurement](../measurement/index.md)**: Pt100 RTD, ±0.5°C accuracy, for supersaturation control
- **[Agitator drive](../energy/electricity.md)**: Motor with gear reducer for 20-100 RPM impeller speed

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (vessel) | 200-2,000 kg | 316L SS or carbon steel, 6-12 mm thick | [Iron & Steel](../metals/iron-steel.md) | Rubber-lined steel (abrasive crystals) |
| [Steel shaft](../metals/iron-steel.md) (agitator) | 20-50 kg | 316L SS, 40-60 mm diameter | [Iron & Steel](../metals/iron-steel.md) | — |
| [Electric motor](../energy/electricity.md) | 1 unit | 0.5-10 kW, 3-phase, with gear reducer for 20-100 RPM | [Electricity](../energy/electricity.md) | — |
| [Heat exchanger](heat-exchanger.md) | 1 unit | Shell-and-tube or jacket, sized for cooling or heating duty | [Heat Exchanger](heat-exchanger.md) | Coil (simpler, less surface area) |
| [Insulation](../construction/building-materials.md) | 10-30 m² | Mineral wool 50 mm, aluminum cladding | [Construction](../construction/building-materials.md) | — |
| [Thermowell and RTD](../measurement/index.md) | 1-2 units | Pt100, ±0.5°C accuracy | [Measurement](../measurement/index.md) | Thermocouple (less accurate) |

## Process Description

### Cooling Crystallizer (Batch)

1. **Fabricate the vessel**: Construct a jacketed cylindrical vessel from 316L stainless steel (for most chemical products) or carbon steel (for non-corrosive products like sugar). Vessel dimensions: 0.5-3 m diameter, height-to-diameter ratio 1:1 to 1.5:1. Working volume: 200-10,000 L. The jacket provides cooling (chilled water or brine at −10°C to 20°C flows through the annular space). Follow pressure vessel construction per [Reactor Vessel](reactor-vessel.md) — the crystallizer vessel is structurally similar.

2. **Install the agitator**: Mount a slow-speed agitator (20-100 RPM) on the vessel top head. Use a pitched-blade turbine or anchor impeller. The agitator must keep crystals suspended without excessive shear that breaks crystals. Anchor impellers (sweeping the vessel wall) also prevent crystal buildup on the cooled wall — a common fouling problem. Shaft diameter and bearing sizing per [Reactor Vessel](reactor-vessel.md).

3. **Connect jacket cooling**: Pipe chilled water or brine to the jacket inlet (bottom) and outlet (top). Install a temperature control valve modulating coolant flow to maintain the vessel temperature at the setpoint. Temperature control accuracy: ±1°C. For large vessels (>5,000 L), an external shell-and-tube heat exchanger with a circulation pump provides more cooling area than a jacket alone.

4. **Install seeding port**: Provide a 50-80 mm nozzle on the top head for adding seed crystals. Seed crystals (0.1-0.5 mm size, 0.1-1% of expected crystal mass) provide controlled nucleation sites, preventing spontaneous nucleation that produces fine powder.

5. **Install discharge valve**: Mount a large-bore discharge valve (80-150 mm) at the vessel bottom. The valve must pass the largest expected crystal size without clogging. Ball valve or butterfly valve with full-port design. For abrasive crystals (salt, sugar), use a wear-resistant valve (316L SS or rubber-lined).

  6. **Operate the cooling cycle**: Charge the vessel with hot saturated solution. Start the agitator. Begin cooling at 0.5-2°C/min. When the solution reaches the seeding temperature (2-5°C below the saturation point, within the metastable zone), add seed crystals through the seeding port. Continue cooling at a rate that maintains supersaturation ratio S = 1.02-1.10 until the target final temperature is reached. Hold at final temperature for 1-4 hours to allow crystal growth to complete. Discharge the crystal slurry to the filter or centrifuge.

  **Strengths:**
  - Simplest crystallizer design — jacketed vessel with agitator, no external circulation loop required
  - Precise temperature control enables tight supersaturation management for large, uniform crystals
  - Suitable for heat-sensitive products by operating at low temperature (0-50°C)
  - Low capital cost — standard jacketed vessel with agitator drive

  **Weaknesses:**
  - Batch operation limits throughput — each cycle requires charging, cooling, seeding, growing, and discharging
  - Jacket heat transfer limits scale — above 5,000 L, jacket area is insufficient, requiring external heat exchanger
  - Cooling duty consumes 5-50 kWh/m³ of product slurry, dependent on the solubility curve slope
  - Wall fouling (encrustation) on cooled surfaces requires periodic cleaning or anchor impeller to sweep walls

### Forced-Circulation Evaporative Crystallizer (Continuous)

7. **Construct the crystallizer body**: Fabricate a vertical cylindrical vessel (0.5-3 m diameter, 2-6 m tall) from 316L stainless. This vessel operates at or near the boiling point of the solution. It does not require a jacket — heat is supplied by an external heat exchanger through which the slurry is pumped in a forced-circulation loop.

8. **Install circulation pump and heater**: Connect a circulation pump (centrifugal, corrosion-resistant, rated for slurry service) to draw slurry from the crystallizer bottom, push it through a shell-and-tube heat exchanger (steam or hot oil on the shell side, slurry in the tubes), and return it to the crystallizer body. The heater adds just enough energy to evaporate solvent at the surface, maintaining supersaturation. Heating rate is controlled by steam pressure or flow. Circulation rate: 3-5× the feed rate.

9. **Install vapor outlet and condenser**: The crystallizer top head has a large vapor outlet (150-300 mm) connected to a condenser. Solvent vapor (typically water) condenses and is collected. The condenser also creates a slight vacuum that reduces the boiling point, lowering the operating temperature and reducing thermal degradation of heat-sensitive products.

10. **Install crystal discharge**: A classified product discharge system removes only crystals above a target size. A settling leg (vertical pipe, 80-150 mm diameter, 1-3 m long) allows crystals to settle by gravity. An overflow weir at the top of the settling leg returns fines (small crystals) to the crystallizer for further growth. Only coarse crystals settle to the bottom and are discharged through a valve.

  11. **Install fines destruction system**: A stream of hot feed or steam is injected near the crystallizer surface to dissolve fine crystals that would otherwise reduce average crystal size. This "fines destruction" stream selectively dissolves the smallest crystals (highest surface-area-to-volume ratio) while leaving the larger product crystals unaffected.

  **Strengths:**
  - Continuous operation eliminates batch cycling — steady-state feed and product discharge
  - Handles substances with flat solubility curves (e.g., NaCl) where cooling crystallization is ineffective
  - Higher throughput than batch designs — 1-100 tonnes crystals/day in a single unit
  - Forced circulation prevents crystal settling and maintains uniform slurry concentration

  **Weaknesses:**
  - Higher energy consumption (100-400 kWh/m³) than cooling crystallization — must supply latent heat of evaporation
  - Circulation pump and external heater add capital cost and maintenance points
  - Crystal size control is less precise than batch cooling — relies on fines destruction and classified discharge
  - Not suitable for heat-sensitive products that degrade at elevated temperature

### Draft-Tube Baffle (DTB) Crystallizer

12. **Install draft tube**: Weld a cylindrical draft tube (diameter = 50-70% of vessel diameter) concentrically inside the vessel. The draft tube creates a controlled circulation path: slurry flows upward inside the draft tube (propelled by the agitator) and downward in the annular space between the draft tube and the vessel wall.

13. **Install baffle and fines withdrawal**: A cylindrical baffle (diameter = 80-90% of vessel diameter) surrounds the draft tube, creating a settling annulus. Clear mother liquor flows upward in this annulus. Fine crystals that are too small to settle are withdrawn from the top of the annulus and sent to a fines dissolution loop (heated to dissolve fines), then returned to the crystallizer.

14. **Classified product discharge**: Settled coarse crystals accumulate at the vessel bottom and are discharged through a classifying leg. The DTB design produces crystals with a narrow size distribution (coefficient of variation 30-50%) compared to forced-circulation designs (CV 50-80%).

15. **Install overflow and fines return**: The overflow from the settling annulus carries fine crystals and clarified mother liquor. Route this stream to a fines dissolution heater (shell-and-tube heat exchanger heated with steam or hot feed). The fines dissolve in the heater. Return the now-clear supersaturated solution to the crystallizer body, where it provides supersaturation for growth of the remaining crystals.

  16. **Install product discharge valve and slurry pump**: The classified product leg terminates in a large-bore discharge valve (80-150 mm). Below the valve, install a slurry pump to transfer the crystal slurry to the [filter press](filter-press.md) or [centrifuge](centrifuge.md) for crystal recovery. The slurry pump must handle abrasive crystal slurries — use a recessed-impeller centrifugal pump or a diaphragm pump with wear-resistant wetted parts.

  **Strengths:**
  - Produces narrowest crystal size distribution (CV 30-50%) of any crystallizer design — fines destruction and classified discharge remove small crystals
  - Continuous operation with controlled crystal size — ideal for consistent product quality
  - Combines crystallization and classification in one vessel, eliminating separate classification equipment
  - Scalable to very large production (5-200 tonnes/day) with consistent crystal quality

  **Weaknesses:**
  - Most mechanically complex crystallizer — draft tube, baffle, fines dissolution loop, and classified discharge
  - Highest capital cost of the three designs due to internal components and external fines loop
  - Requires careful hydraulic design — draft tube flow rate, baffle gap, and overflow rate must be balanced
  - Fines dissolution heater adds energy consumption and a heat exchanger to maintain

## Calibration and Verification

1. **Cooling curve test** (batch crystallizer): Charge the vessel with a solution of known concentration. Start cooling at the design rate (0.5-2°C/min). Record the temperature-concentration profile. The point where the temperature drops below the solubility curve without crystal formation indicates the metastable zone width (the temperature range where the solution is supersaturated but has not yet nucleated). Seed crystals should be added just inside the metastable zone. For most salts, the metastable zone width is 2-15°C below the saturation point.

2. **Crystal size distribution**: Process a batch and sample the crystal product. Sieve the crystals through standard mesh sizes (ISO 3310). Record the weight fraction retained on each sieve. Plot cumulative distribution. Median crystal size (D50) should be in the target range (0.5-3 mm for most applications). If too many fines (<0.1 mm): reduce supersaturation, increase seeding, add fines destruction. If too few crystals: increase supersaturation, reduce fines destruction. The coefficient of variation (CV = (D84 − D16) / (2 × D50)) should be <50% for a well-controlled crystallization.

3. **Yield verification**: Weigh the dry crystal product. Compare to the theoretical yield calculated from the initial solute mass, solubility curve, and final temperature. Yield = actual mass / theoretical mass × 100%. Target: 60-90% for cooling crystallization, 80-95% for evaporative. Low yield may indicate excessive solute remaining in the mother liquor — recycle the mother liquor to the next batch.

3. **Crystal purity**: Dissolve a sample of crystals in fresh solvent. Analyze the solution for impurities (ICP-OES for metals, ion chromatography for ionic contaminants). Compare to product specification. Crystal purity >99.5% is typical for a single crystallization step. Lower purity indicates the mother liquor is trapped in the crystal mass — improve washing after filtration, or re-crystallize.

4. **Supersaturation verification**: During operation, measure the solution concentration (by density or refractive index) and the temperature. Compare to the solubility curve to calculate the actual supersaturation ratio S = C/C*. S should remain between 1.02 and 1.10 throughout the batch. If S > 1.15, spontaneous nucleation is likely — reduce the cooling rate. If S < 1.02, crystal growth stalls — increase the cooling rate or add more antisolvent.

## Operating Procedure (Batch Cooling Crystallizer)

1. **Charge and heat**: Fill the vessel with feed solution to 70-80% of working volume. Heat to 5-10°C above the saturation temperature (to ensure all solute is dissolved). Verify the solution is clear (no undissolved solids) by visual inspection through the sight glass.
2. **Cool to seeding point**: Start the agitator at design speed (20-100 RPM). Begin cooling at 0.5-2°C/min. Monitor temperature with the Pt100 RTD. As the solution cools below the saturation temperature, it enters the metastable zone — supersaturated but not yet nucleating.
3. **Seed the batch**: When the temperature is 2-5°C below saturation (within the metastable zone), add seed crystals through the seeding port. Seed crystal mass: 0.1-1% of expected crystal yield. Seed size: 0.1-0.5 mm. Close the seeding port immediately to prevent evaporation.
4. **Controlled cooling**: Continue cooling at the design rate. The cooling rate must be slow enough that supersaturation remains within the metastable zone (S = 1.02-1.10). If the cooling rate is too fast, spontaneous nucleation produces fines. If too slow, the batch takes excessively long.
5. **Hold at final temperature**: When the target final temperature is reached, hold for 1-4 hours to allow crystal growth to approach completion. Sample the mother liquor and measure concentration (density or refractive index). Compare to the solubility at the final temperature to estimate yield.
6. **Discharge**: Open the bottom discharge valve. Transfer the crystal slurry to the [filter press](filter-press.md) or [centrifuge](centrifuge.md) for crystal recovery. Rinse the vessel with a small amount of cold solvent to recover residual crystals.
7. **Wash crystals**: Wash the filter cake or centrifuge cake with cold clean solvent (at the crystallization temperature or below) to remove mother liquor from the crystal surfaces. Wash ratio: 0.1-0.3 kg wash solvent per kg wet cake.
8. **Dry**: Transfer washed crystals to a drying oven or tray dryer. Dry at 50-80°C (below the crystal decomposition temperature) for 4-24 hours to <0.5% residual moisture.

## Quantitative Parameters

| Parameter | Cooling Crystallizer (Batch) | Evaporative Crystallizer (Continuous) | DTB Crystallizer |
|-----------|------------------------------|--------------------------------------|------------------|
| Working volume | 200-10,000 L | 500-50,000 L | 1,000-100,000 L |
| Operating temperature | −10°C to 80°C | 40-120°C (at or near boiling) | 30-100°C |
| Cooling/heating rate | 0.5-2°C/min | Continuous — heat input matched to evaporation rate | Continuous |
| Crystal size (median) | 0.3-2 mm | 0.5-3 mm (with fines destruction) | 0.5-2.5 mm (narrow distribution) |
| Crystal growth rate | 0.1-1.0 mm/hr | 0.1-0.5 mm/hr | 0.2-1.0 mm/hr |
| Supersaturation ratio (S) | 1.02-1.10 | 1.01-1.05 | 1.02-1.08 |
| Crystal purity | 95-99.9% (single pass) | 95-99.5% (single pass) | 95-99.8% |
| Yield (fraction recovered) | 60-90% | 80-95% | 75-95% |
| Cycle time (batch) | 4-24 hours | Continuous | Continuous |
| Agitator speed | 20-100 RPM | 20-100 RPM | 20-80 RPM |
| Energy consumption | 5-50 kWh/m³ (cooling) | 100-400 kWh/m³ (evaporation) | 50-200 kWh/m³ |
| Throughput | 0.1-5 tonnes crystals/batch | 1-100 tonnes crystals/day | 5-200 tonnes crystals/day |

## Scaling Notes

- **Batch crystallizer scaling**: Vessel volume scales cubically with diameter, but jacket heat transfer area scales only with diameter × height. Above 5,000 L, jacket area becomes insufficient — switch to an external heat exchanger with a circulation pump.
- **Evaporative crystallizer scaling**: Circulation rate must maintain slurry velocity >2 m/s in the heater tubes to prevent crystal deposition and tube plugging. Scale by adding parallel heater tubes and increasing pump capacity.
- **Nucleation rate scaling**: Nucleation rate is proportional to supersaturation²⁻³ (power law). Small changes in supersaturation produce large changes in the number of crystals formed. At production scale, tighter temperature control (±0.5°C) is required compared to laboratory scale (±2°C acceptable).
- **Minimum economic scale**: A 200 L batch cooling crystallizer produces 20-100 kg crystals per batch. A forced-circulation evaporative crystallizer at 2,000 L produces 1-10 tonnes/day. Below these scales, simple open-pan evaporation followed by filtration is more practical.
- **Re-crystallization for higher purity**: If a single crystallization pass does not achieve the target purity (e.g., >99.5%), dissolve the crystals in fresh hot solvent and re-crystallize. Each pass rejects impurities to the mother liquor. Typical yield loss per re-crystallization: 5-15% of the product remains in the mother liquor.
- **Seeding technique**: The seeding point and seed quality are the single largest factors determining crystal size distribution. Over-seeding produces many small crystals; under-seeding leads to spontaneous nucleation and fines. Keep seed crystals dry and free-flowing (store in a sealed container with desiccant). Weigh the seed charge precisely (±5% of target mass).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Excessive fines (D50 <0.2 mm) | Supersaturation too high causing spontaneous nucleation; insufficient seeding; agitator speed too high causing crystal breakage | Reduce cooling rate to 0.3-0.5°C/min; add seed crystals at 0.5-1% of expected mass; reduce agitator speed to 20-40 RPM; install fines destruction loop |
| No crystal formation despite supersaturation | Solution in metastable zone (supersaturated but no nucleation); impurities inhibiting nucleation; temperature measurement error | Add seed crystals; introduce a small rough surface (scratch the vessel wall with a glass rod); verify temperature calibration; check for surfactants or colloids inhibiting nucleation |
| Crystals coating vessel walls and agitator | Localized high supersaturation at the cooled wall surface; insufficient wall agitation; temperature gradient too steep | Switch from jacket cooling to external heat exchanger (eliminates wall cooling); increase agitator speed; use an anchor impeller that sweeps the vessel wall |
| Crystal size decreasing over successive batches | Crystal deposits from previous batch acting as uncontrolled seed (too many nuclei); incomplete cleaning between batches | Clean vessel thoroughly between batches; wash walls with hot solvent to dissolve residual crystals; reduce seed crystal loading |
| Plugged discharge valve | Crystals larger than valve bore; crystal agglomerates bridging the valve opening; valve partially closed during discharge | Install a larger-bore valve (≥100 mm); add a flush connection to dissolve blockages; use a full-port ball valve; add a vibration pad to the discharge pipe |
| Low yield (<60% recovery) | Supersaturation insufficient to drive crystallization to completion; crystal losses in mother liquor during filtration | Extend cooling to lower final temperature; add antisolvent to reduce solubility further; improve washing efficiency on filter; recycle mother liquor to next batch |
| Crystal habit change (unexpected crystal shape) | Impurity in the feed altering crystal growth kinetics; solvent composition change; temperature profile different from normal | Verify raw material purity (incoming QC); check solvent composition (water content, contamination); reproduce the standard cooling profile; screen for new impurities by HPLC |
| Encrustation on vessel walls (>5 mm thick) | Localized high supersaturation at the cooled wall; insufficient agitation near the wall; temperature gradient too steep | Increase agitator speed; use an anchor impeller that sweeps the wall; reduce cooling rate; switch to external heat exchanger (eliminates wall cooling); add periodic wall washing with hot solvent |
| Foaming in evaporative crystallizer | Surfactant impurities in feed; high boiling rate creating foam; entrainment of fine crystals in vapor | Add antifoam agent (silicone-based, 5-50 ppm); reduce boilup rate; install or clean the demister pad in the vapor outlet; verify feed does not contain detergents or surfactants |

## Safety

- **Hot solutions**: Solutions at 50-120°C cause thermal burns on contact. Insulate the vessel and piping. Emergency shower within 10 m. Use thermal gloves and face shield for sampling.
- **Vacuum collapse**: Evaporative crystallizers operating under vacuum risk shell collapse if the vacuum system fails and atmospheric pressure pushes inward. Design shell for full vacuum (external pressure). Install vacuum relief valve.
- **Crystal slurry handling**: Crystal slurries are abrasive and can erode pumps and piping over time. Use wear-resistant materials (316L SS minimum, hardened alloys for abrasive crystals). Never restrict slurry flow — crystal blockages cause pressure buildup.
- **Solvent vapors**: Evaporative crystallizers release solvent vapors (water, organics). Condense vapors to recover solvent. Vent non-condensables. For organic solvents: explosion-proof equipment, nitrogen purge, flame arrestors.
- **Seeding with dry powders**: Adding seed crystals generates airborne dust. Wear dust mask or respirator. Use a closed seeding port with a funnel to minimize dust release.
- **Hot feed splash**: Charging hot saturated solution (>80°C) into the vessel can cause splashing. Charge through a bottom or mid-height nozzle, not through the open top head. If top charging is unavoidable, use a funnel with a long spout that reaches below the liquid surface.
- **Pressure vessel safety**: Evaporative crystallizers operating under pressure or vacuum are pressure vessels. Follow the same hydrostatic testing and relief valve requirements as [reactor vessels](reactor-vessel.md). Design for full vacuum (external pressure) if operating below atmospheric pressure.
- **Solvent fire hazard**: Organic solvent crystallizations (ethanol, acetone, toluene) create flammable vapor atmospheres. Use nitrogen blanket, explosion-proof equipment, and ground all metal components. Install flame arrestors on all vent lines.

## Quality Control

- **Crystal size distribution**: Sieve analysis per ISO 3310. Sample 200-500 g from each batch. Record D10, D50, D90 (the sizes at which 10%, 50%, and 90% of crystals pass). Target: D50 = 0.5-3 mm, coefficient of variation <50%.
- **Crystal purity test**: Dissolve 10 g crystals in fresh solvent, analyze by titration or spectroscopy. Target: >99.5% purity for single-pass crystallization. Recrystallize if below specification.
- **Mother liquor concentration**: Measure density or refractive index of the mother liquor after filtration. Compare to the solubility curve at the final temperature to estimate yield. Target: >80% of theoretical yield for evaporative crystallization.
- **Visual inspection**: Crystals should be well-formed (faceted for most inorganic salts, prismatic for organic compounds). Excessive rounding indicates dissolution-regrowth cycles. Needles or plates indicate preferential growth from excessive supersaturation.
- **Polymorph screening**: For organic compounds that can crystallize in multiple forms (polymorphs), verify the correct polymorph by X-ray diffraction or melting point. The wrong polymorph may have different solubility, bioavailability, or stability. Polymorph control is achieved by precise temperature control during seeding and growth.
- **Encrustation monitoring**: Inspect the vessel walls, agitator, and baffles for crystal encrustation (scale buildup). Light encrustation (<2 mm) is normal. Heavy encrustation (>5 mm) reduces effective vessel volume and heat transfer. If encrustation is excessive, reduce the cooling rate, increase agitator tip speed, or use a wall-wiping impeller.

## Variations and Alternatives

- **Melt crystallization**: Crystallize from the melt (no solvent) by cooling below the freezing point. Used for ultra-pure organics (p-xylene, naphthalene). No solvent handling or recovery. Requires precise temperature control near the melting point.
- **Antisolvent crystallization**: Add a second solvent in which the solute has low solubility (e.g., add water to an ethanol solution of a water-insoluble compound). Rapid mixing required to achieve uniform supersaturation. The mixed solvent must be separated (by distillation) for recycling.
- **Open-pan crystallization**: The simplest method — evaporate a solution in an open pan by solar or waste heat. Zero energy input. Very slow (days to weeks). Crystal size and purity are poor. Used for salt production where purity requirements are low.
- **[Evaporator](evaporator.md)**: Concentrates a solution without reaching supersaturation. The evaporator is the predecessor step — concentrate the feed to near-saturation, then transfer to the crystallizer for the final supersaturation and crystal growth.
- **Pressure crystallization**: Apply high pressure (10-100 MPa) to induce crystallization without temperature change. Used for polymorphic compounds where pressure selects a specific crystal form. Requires specialized high-pressure equipment — limited to high-value products.
- **Reaction crystallization**: Combine two reactant solutions in the crystallizer. The reaction product has low solubility and precipitates as crystals. Example: (NH₄)₂SO₄ production from NH₃ + H₂SO₄. The heat of reaction supplies part of the evaporation energy. Control supersaturation by the reactant addition rate.
- **Oiling-out crystallization**: Some organic compounds separate as a liquid oil phase before crystallizing. The oil phase eventually solidifies into crystals. This is an unpredictable phenomenon that makes process control difficult. If oiling-out occurs, try adding an antisolvent or adjusting the temperature profile to induce direct crystallization instead.

## References

- [Reactor Vessel](reactor-vessel.md) — vessel construction shared with crystallizer body
- [Heat Exchanger](heat-exchanger.md) — cooling jacket and circulation heater design
- [Evaporator](evaporator.md) — evaporation without crystallization (concentration)
- [Filter Press](filter-press.md) — crystal recovery by filtration
- [Centrifuge](centrifuge.md) — crystal recovery by centrifugation
- [Distillation Column](distillation-column.md) — alternative purification for liquid products
- [Evaporator](evaporator.md) — concentration before crystallization
- [Water Treatment](water-treatment.md) — salt recovery from brine by crystallization
- [Chemical Recovery](chemical-recovery.md) — crystallization for product and byproduct recovery
- [Solvents](solvents.md) — solvent selection for crystallization (solubility, recovery)
- [Acids](acids.md) — acid production processes that use crystallization for product recovery
- [Alkalis](alkalis.md) — caustic soda and potash purification by crystallization

## Solubility Data for Common Compounds

| Compound | Solubility at 0°C (g/100 g H₂O) | Solubility at 100°C (g/100 g H₂O) | Recommended Method |
|----------|---------------------------------|-----------------------------------|-------------------|
| NaCl | 35.7 | 39.1 | Evaporative (flat curve) |
| KNO₃ | 13.0 | 247.0 | Cooling (steep curve) |
| Na₂SO₄ | 4.8 (decahydrate) → 42.0 (at 32°C) | 42.0 (anhydrous, decreases above 32°C) | Cooling below 32°C |
| CuSO₄·5H₂O | 23.1 | 203.3 | Cooling |
| (NH₄)₂SO₄ | 70.6 | 103.8 | Evaporative (moderate curve) |
| Sugar (sucrose) | 179.2 | 487.2 | Evaporative (multiple-effect) |
| Na₂CO₃ | 7.0 | 45.5 | Cooling |

## Crystal Size Distribution Control

The crystal size distribution (CSD) is the single most important product quality parameter. It affects downstream filtration rate, washing efficiency, drying behavior, and final product handling (flowability, dustiness, bulk density). Three mechanisms control CSD:

1. **Supersaturation control**: Supersaturation (ΔC = C − C*) is the driving force for both nucleation and crystal growth. At low supersaturation (ΔC < 0.5 g/L for most salts), existing crystals grow without new nuclei forming. At high supersaturation (ΔC > 2 g/L), spontaneous nucleation creates a flood of fine crystals. The operating window between these limits is called the metastable zone. Maintain ΔC in the lower half of the metastable zone for large, uniform crystals.
2. **Seeding**: Add pre-grown seed crystals (0.1-1.0 wt% of expected crystal yield) to provide growth surfaces. This suppresses spontaneous nucleation and gives predictable crystal size. Seed size and size distribution directly determine product crystal size — product crystals are typically 5-10× the seed size after one batch cycle.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
