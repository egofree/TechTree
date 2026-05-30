# Thermal Efficiency by Kiln Type and Fuel

> **Type**: metric | **Tier**: important | **Domains**: ceramics, chemistry, energy

The fraction of fuel energy that actually reaches the kiln charge (the material being fired), expressed as a percentage. Kiln thermal efficiency varies dramatically by kiln design and fuel type — from 5-10% for simple open bonfires to 60-80% for modern tunnel kilns with heat recovery. This metric determines fuel consumption, firing cost, and the scale of fuel supply infrastructure needed to sustain ceramic and chemical production.

## Context in the Tech Tree

In [Kiln Design](../ceramics/kilns.md), thermal efficiency is the primary engineering constraint. A kiln that wastes 90% of its fuel heat requires 10× the fuel supply of one that captures 50%. For a bootstrap settlement, this difference determines whether pottery production is sustainable with local wood supplies or requires importing coal. In [Cement & Concrete](../chemistry/cement.md), rotary kiln thermal efficiency (40-55%) directly impacts the energy cost per tonne of clinker — one of the most energy-intensive industrial processes.

The fuel sequence (wood → charcoal → coal → coke → gas) affects thermal efficiency because each fuel has different combustion characteristics, flame temperature, and heat transfer properties. Gas fuels allow the most precise control and highest efficiency; solid fuels the least.

## Technical Details

Approximate thermal efficiencies by kiln type and fuel:

| Kiln Type | Fuel | Thermal Efficiency | Notes |
|-----------|------|-------------------|-------|
| Bonfire / open pit | Wood | 5-10% | No insulation, most heat lost to atmosphere |
| Clamp kiln (earth-covered) | Wood | 15-25% | Earth covering provides some insulation |
| Updraft bottle kiln | Wood/charcoal | 20-30% | Simple brick chamber, chimney draws heat through |
| Downdraft kiln | Wood/coal | 25-40% | Heat flows down through ware, better distribution |
| Beehive kiln (coal) | Coal | 25-35% | Side stoking, good for bricks |
| Hoffman kiln | Coal/gas | 30-45% | Continuous firing, heat recovery from cooling zone |
| Tunnel kiln | Gas/oil | 40-60% | Continuous, counter-current heat exchange |
| Rotary kiln (cement) | Coal/gas | 40-55% | Material tumbles through hot gas stream |
| Modern tunnel with recuperator | Gas | 55-80% | Heat exchangers preheat combustion air from exhaust |

Factors that improve thermal efficiency:
- **Insulation**: Refractory lining reduces heat loss through kiln walls. From no insulation (heat loss ≈ 50% of input) to modern ceramic fiber (heat loss ≈ 5%).
- **Heat recovery**: Using exhaust gas heat to preheat combustion air or dry incoming ware. Recuperators can add 10-20% efficiency.
- **Continuous operation**: Tunnel and Hoffman kilns maintain steady-state temperature, avoiding the repeated heating/cooling losses of batch kilns.
- **Fuel-air ratio control**: Excess air carries heat out the chimney. Too little air causes incomplete combustion. Optimal ratio maximizes heat release to the charge.

For bootstrapping, the progression is: bonfire → clamp kiln → updraft kiln → downdraft kiln → continuous kiln. Each step roughly doubles thermal efficiency, halving fuel requirements for the same output.

## Related Terms

- [Thermal Efficiency](./thermal-efficiency.md) — general thermal efficiency concepts beyond kilns
- [Temperature Control](./temperature-control.md) — controlling kiln temperature affects both efficiency and product quality
- [Temperature Zones](./temperature-zones.md) — kiln zone design for optimal heat distribution

## Appears In

- [Kiln Design](../ceramics/kilns.md)
- [Cement & Concrete](../chemistry/cement.md)
- [Fuel Production](../energy/fuels.md)
- [Glass Production](../glass/basic.md)
