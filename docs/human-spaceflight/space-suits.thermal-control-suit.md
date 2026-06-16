# Thermal Control Suit

> **Node ID**: `human-spaceflight.space-suits.thermal-control-suit`
> **Domain**: [Human Spaceflight](./index.md)
> **Parent**: [Space Suits](./space-suits.md)
> **Dependencies**: [`human-spaceflight.space-suits`](./space-suits.md)
> **Outputs**: thermal_control_garments, liquid_cooling_garments, multi_layer_insulation
> **Timeline**: Years 50-200+

## Overview

The thermal control suit manages body temperature and removes metabolic heat in vacuum, where
there is no convective or conductive heat sink — only radiation. Two systems work together:
the Liquid Cooling and Ventilation Garment (LCVG) worn against the skin, and the multi-layer
insulation (MLI) blanket built into the suit's Thermal Micrometeoroid Garment (TMG).

## Liquid Cooling and Ventilation Garment (LCVG)

The LCVG is a full-body spandex mesh undergarment laced with roughly 300 metres of 1.6 mm PVC
capillary tubing. Chilled water circulates at 1.5-2.5 L/min, directly absorbing body heat at
the skin. The LCVG removes **100-300 W of metabolic heat** (the output of a human doing
moderate to hard work), with peak capacity for 500 W short bursts. Without it, the suit's
insulation would trap metabolic heat and overheat the wearer within minutes. Ventilation
ducting along the limbs draws exhaled, humid oxygen back toward the PLSS for CO2 scrubbing.

## Multi-Layer Insulation (MLG)

The TMG inner blanket is 10-14 layers of aluminised Mylar separated by Dacron scrim. Each
Mylar layer reflects ~97% of radiative heat; stacked layers drop the effective radiative
conductance to near-zero, isolating the wearer from the +120°C sunlit lunar surface and the
-150°C shade. The Dacron scrim prevents conductive contact between layers.

## Heat Rejection Path

Skin → LCVG water → PLSS sublimator → vacuum. The sublimator exposes a controlled flow of
feedwater to vacuum; the water freezes to ice, then sublimes directly to vapour, carrying
the latent heat of sublimation (2,830 kJ/kg) away.

## See Also

- [Space Suits](./space-suits.md) — parent capability
- [Portable Life Support System](./space-suits.plss-design.md) — sublimator and water loop
- [Pressure Garment Design](./space-suits.pressure-garment.md) — outer suit shell

---

*Part of the [Bootciv Tech Tree](../index.md) • [Human Spaceflight](./index.md) • [All Domains](../index.md)*
