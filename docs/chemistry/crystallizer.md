# Crystallizer

> **Node ID**: chemistry.crystallizer
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`chemistry.heat-exchanger`](heat-exchanger.md), [`chemistry.filter-press`](filter-press.md)
> **Enables**: [`chemistry.acids`](acids.md), [`chemistry.alkalis`](alkalis.md), [`chemistry.solvents`](solvents.md)
> **Timeline**: Years 15-30
> **Outputs**: crystals
> **Critical**: No — crystallization is the primary purification method for solid chemical products but distillation and extraction can substitute for liquid products

## Principle

A crystallizer produces solid crystals from a solution by creating supersaturation — the driving force for crystal nucleation and growth. Supersaturation is achieved by cooling the solution (cooling crystallization), evaporating solvent (evaporative crystallization), or adding an antisolvent that reduces solute solubility (antisolvent crystallization). Once supersaturated, the solution nucleates new crystals (homogeneous nucleation) or grows existing crystals (seeded growth). Controlled crystallization produces large, pure crystals (0.1-5 mm) that are easily filtered and washed.

The governing relationship is the solubility curve: solubility (g solute per 100 g solvent) as a function of temperature. For substances with steep solubility curves (e.g., KNO₃: 13 g/100 g at 0°C to 247 g/100 g at 100°C), cooling crystallization is highly effective. For substances with flat solubility curves (e.g., NaCl: 35.7 g/100 g at 0°C to 39.1 g/100 g at 100°C), evaporative crystallization is preferred.

The crystallizer must provide gentle agitation (to keep crystals suspended without breaking them), temperature control (to maintain the desired supersaturation level), and a means of removing crystals (classified product discharge or batch harvest). The key design parameter is the supersaturation ratio (S = C/C\*, where C is the actual concentration and C\* is the equilibrium solubility). Typical operating range: S = 1.02-1.10. Too low: no crystallization. Too high: excessive nucleation produces fine powder ("fines") instead of coarse crystals.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (vessel) | 200-2,000 kg | 316L SS or carbon steel, 6-12 mm thick | [Iron & Steel](../metals/iron-steel.md) | Rubber-lined steel (abrasive crystals) |
| [Steel shaft](../metals/iron-steel.md) (agitator) | 20-50 kg | 316L SS, 40-60 mm diameter | [Iron & Steel](../metals/iron-steel.md) | — |
| [Electric motor](../energy/electricity.md) | 1 unit | 0.5-10 kW, 3-phase, with gear reducer for 20-100 RPM | [Electricity](../energy/electricity.md) | — |
| [Heat exchanger](heat-exchanger.md) | 1 unit | Shell-and-tube or jacket, sized for cooling or heating duty | [Heat Exchanger](heat-exchanger.md) | Coil (simpler, less surface area) |
| [Insulation](../construction/building-materials.md) | 10-30 m² | Mineral wool 50 mm, aluminum cladding | [Construction](../construction/building-materials.md) | — |
| [Thermowell and RTD](../measurement/index.md) | 1-2 units | Pt100, ±0.5°C accuracy | [Measurement](../measurement/index.md) | Thermocouple (less accurate) |

## Construction Steps

### Cooling Crystallizer (Batch)

1. **Fabricate the vessel**: Construct a jacketed cylindrical vessel from 316L stainless steel (for most chemical products) or carbon steel (for non-corrosive products like sugar). Vessel dimensions: 0.5-3 m diameter, height-to-diameter ratio 1:1 to 1.5:1. Working volume: 200-10,000 L. The jacket provides cooling (chilled water or brine at −10°C to 20°C flows through the annular space). Follow pressure vessel construction per [Reactor Vessel](reactor-vessel.md) — the crystallizer vessel is structurally similar.

2. **Install the agitator**: Mount a slow-speed agitator (20-100 RPM) on the vessel top head. Use a pitched-blade turbine or anchor impeller. The agitator must keep crystals suspended without excessive shear that breaks crystals. Anchor impellers (sweeping the vessel wall) also prevent crystal buildup on the cooled wall — a common fouling problem. Shaft diameter and bearing sizing per [Reactor Vessel](reactor-vessel.md).

3. **Connect jacket cooling**: Pipe chilled water or brine to the jacket inlet (bottom) and outlet (top). Install a temperature control valve modulating coolant flow to maintain the vessel temperature at the setpoint. Temperature control accuracy: ±1°C.

4. **Install seeding port**: Provide a 50-80 mm nozzle on the top head for adding seed crystals. Seed crystals (0.1-0.5 mm size, 0.1-1% of expected crystal mass) provide controlled nucleation sites, preventing spontaneous nucleation that produces fine powder.

5. **Install discharge valve**: Mount a large-bore discharge valve (80-150 mm) at the vessel bottom. The valve must pass the largest expected crystal size without clogging. Ball valve or butterfly valve with full-port design. For abrasive crystals (salt, sugar), use a wear-resistant valve (316L SS or rubber-lined).

### Forced-Circulation Evaporative Crystallizer (Continuous)

6. **Construct the crystallizer body**: Fabricate a vertical cylindrical vessel (0.5-3 m diameter, 2-6 m tall) from 316L stainless. This vessel operates at or near the boiling point of the solution. It does not require a jacket — heat is supplied by an external heat exchanger through which the slurry is pumped in a forced-circulation loop.

7. **Install circulation pump and heater**: Connect a circulation pump (centrifugal, corrosion-resistant, rated for slurry service) to draw slurry from the crystallizer bottom, push it through a shell-and-tube heat exchanger (steam or hot oil on the shell side, slurry in the tubes), and return it to the crystallizer body. The heater adds just enough energy to evaporate solvent at the surface, maintaining supersaturation. Heating rate is controlled by steam pressure or flow.

8. **Install vapor outlet and condenser**: The crystallizer top head has a large vapor outlet (150-300 mm) connected to a condenser. Solvent vapor (typically water) condenses and is collected. The condenser also creates a slight vacuum that reduces the boiling point, lowering the operating temperature and reducing thermal degradation of heat-sensitive products.

9. **Install crystal discharge**: A classified product discharge system removes only crystals above a target size. A settling leg (vertical pipe, 80-150 mm diameter, 1-3 m long) allows crystals to settle by gravity. An overflow weir at the top of the settling leg returns fines (small crystals) to the crystallizer for further growth. Only coarse crystals settle to the bottom and are discharged through a valve.

10. **Install fines destruction system**: A stream of hot feed or steam is injected near the crystallizer surface to dissolve fine crystals that would otherwise reduce average crystal size. This "fines destruction" stream selectively dissolves the smallest crystals (highest surface-area-to-volume ratio) while leaving the larger product crystals unaffected.

## Calibration and Verification

1. **Cooling curve test** (batch crystallizer): Charge the vessel with a solution of known concentration. Start cooling at the design rate (0.5-2°C/min). Record the temperature-concentration profile. The point where the temperature drops below the solubility curve without crystal formation indicates the metastable zone width (the temperature range where the solution is supersaturated but has not yet nucleated). Seed crystals should be added just inside the metastable zone.

2. **Crystal size distribution**: Process a batch and sample the crystal product. Sieve the crystals through standard mesh sizes (ISO 3310). Record the weight fraction retained on each sieve. Plot cumulative distribution. Median crystal size (D50) should be in the target range (0.5-3 mm for most applications). If too many fines (<0.1 mm): reduce supersaturation, increase seeding, add fines destruction. If too few crystals: increase supersaturation, reduce fines destruction.

3. **Crystal purity**: Dissolve a sample of crystals in fresh solvent. Analyze the solution for impurities (ICP-OES for metals, ion chromatography for ionic contaminants). Compare to product specification. Crystal purity >99.5% is typical for a single crystallization step. Lower purity indicates the mother liquor is trapped in the crystal mass — improve washing after filtration, or re-crystallize.

## Expected Performance

| Parameter | Cooling Crystallizer (Batch) | Evaporative Crystallizer (Continuous) |
|-----------|------------------------------|--------------------------------------|
| Working volume | 200-10,000 L | 500-50,000 L (crystallizer + circulation) |
| Operating temperature | −10°C to 80°C | 40-120°C (at or near boiling) |
| Cooling/heating rate | 0.5-2°C/min | Continuous — heat input matched to evaporation rate |
| Crystal size (median) | 0.3-2 mm | 0.5-3 mm (with fines destruction) |
| Crystal purity | 95-99.9% (single pass) | 95-99.5% (single pass) |
| Yield (fraction of dissolved solute recovered) | 60-90% | 80-95% |
| Cycle time (batch) | 4-24 hours | Continuous |
| Agitator speed | 20-100 RPM | 20-100 RPM |
| Energy consumption | 5-50 kWh/m³ (cooling) | 100-400 kWh/m³ (evaporation, depends on solvent) |
| Throughput | 0.1-5 tonnes crystals/batch | 1-100 tonnes crystals/day |

## Safety

- **Hot solutions**: Solutions at 50-120°C cause thermal burns on contact. Insulate the vessel and piping. Emergency shower within 10 m. Use thermal gloves and face shield for sampling.
- **Vacuum collapse**: Evaporative crystallizers operating under vacuum risk shell collapse if the vacuum system fails and atmospheric pressure pushes inward. Design shell for full vacuum (external pressure). Install vacuum relief valve.
- **Crystal slurry handling**: Crystal slurries are abrasive and can erode pumps and piping over time. Use wear-resistant materials (316L SS minimum, hardened alloys for abrasive crystals). Never restrict slurry flow — crystal blockages cause pressure buildup.
- **Solvent vapors**: Evaporative crystallizers release solvent vapors (water, organics). Condense vapors to recover solvent. Vent non-condensables. For organic solvents: explosion-proof equipment, nitrogen purge, flame arrestors.

## See Also

- [Reactor Vessel](reactor-vessel.md) — vessel construction shared with crystallizer body
- [Heat Exchanger](heat-exchanger.md) — cooling jacket and circulation heater design
- [Evaporator](evaporator.md) — evaporation without crystallization (concentration)
- [Filter Press](filter-press.md) — crystal recovery by filtration
- [Centrifuge](centrifuge.md) — crystal recovery by centrifugation

[← Back to Chemistry](index.md)
