# Pasteurization

> **Node ID**: food-processing.pasteurization
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: [`energy`](../energy/index.md), [`health.sanitation`](../health/sanitation.md), [`metals`](../metals/index.md)
> **Enables**: None (leaf capability)
> **Critical**: No — pasteurization improves food safety but is not the sole method for achieving it
> **Timeline**: Years 15-25
> **Outputs**: pasteurized_food

Pasteurization is heat treatment that destroys pathogenic microorganisms without sterilizing the food. Named after Louis Pasteur (1864), it is critical for milk, juice, beer, and other liquid foods. Unlike canning, which achieves complete sterilization, pasteurization targets specific pathogens while preserving flavor, color, and nutritional quality.

For complete sterilization in sealed containers, see [Canning & Thermal Sterilization](canning.md). For an overview of all preservation methods, see [Food Preservation](preservation.md).

## Materials

- **Stainless steel plates** (for plate heat exchanger): Food-grade 304 or 316 stainless steel. Thickness 0.5-1.0 mm. Source: [Metals](../metals/iron-steel.md).
- **Food-grade gaskets**: EPDM or silicone rubber gaskets between heat exchanger plates. Source: [Polymers](../polymers/thermoplastics.md) or natural rubber.
- **Steam**: For heating via heat exchanger at 5-15 bar. Source: [Energy](../energy/engine.md) — requires boiler.
- **Cooling water**: For final cooling stage. Potable water. Source: [Water](../water/index.md).
- **Thermometers**: Mercury or digital, calibrated to ±0.5°C. Recording thermometers provide continuous documentation.

## Pasteurization Methods

### Low-Temperature Long-Time (LTLT)

63°C for 30 minutes. Traditional batch method. Gentle on flavor but requires careful time-temperature control.

- Batch process in vat or tank with agitation and steam jacket
- Suitable for small-scale dairy operations
- Requires constant monitoring to ensure temperature hold

### High-Temperature Short-Time (HTST)

72°C for 15 seconds. Continuous flow method. Industry standard for milk. Requires plate heat exchanger.

- Continuous flow through plate heat exchanger
- Throughput: 5,000-20,000 L/hour with a single unit
- Divert valve activates if temperature drops below setpoint
- Regenerative heat recovery recovers 80-90% of thermal energy — fuel cost of only 0.1-0.3 MJ/L

### Ultra-High Temperature (UHT)

135-150°C for 2-8 seconds. Produces shelf-stable milk (6+ months without refrigeration). Requires aseptic packaging. Common outside North America.

- Highest temperature, shortest time
- Aseptic packaging required to maintain sterility
- Flavor changes (cooked note) compared to HTST

## Verification and Quality Control

- **Phosphatase test**: Confirms adequate milk pasteurization. Alkaline phosphatase is destroyed at the same temperature as *Mycobacterium tuberculosis* (the target pathogen). Negative test = properly pasteurized.
- **Temperature monitoring**: Mercury or digital thermometers calibrated to ±0.5°C. Recording thermometers provide continuous documentation. Divert valve activates if temperature drops below setpoint.
- **Post-pasteurization contamination**: The leading cause of spoilage. Any breach in sanitary handling re-introduces pathogens. Clean and sanitize all equipment after pasteurization. Cool rapidly to 4°C.

## Pasteurization Parameters

| Method | Temperature | Hold Time | Target Products | Shelf Life | Energy |
|--------|:-----------:|:---------:|:---------------:|:----------:|:------:|
| LTLT (batch) | 63°C | 30 min | Milk, cream | 5-7 days (refrigerated) | 0.3-0.5 MJ/L |
| HTST (continuous) | 72°C | 15 sec | Milk, juice | 5-7 days (refrigerated) | 0.1-0.3 MJ/L |
| UHT | 135-150°C | 2-8 sec | Milk, cream | 6+ months (ambient) | 0.3-0.5 MJ/L |

## Heat Exchanger Operation (HTST)

1. **Raw product inlet**: Cold raw product (4°C) enters the heat exchanger.
2. **Regenerative heating**: Hot outgoing product preheats incoming cold product through counterflow plates. Recovers 80-90% of thermal energy.
3. **Final heating**: Steam or hot water on one side of plates heats product to 72°C.
4. **Hold tube**: Product flows through insulated tube sized for 15-second residence time at temperature. Tube length = flow rate × hold time. Temperature monitored at tube exit.
5. **Regenerative cooling**: Outgoing hot product preheats incoming cold product (same step as #2, counterflow).
6. **Final cooling**: Cold water or chilled glycol cools product to 4°C.
7. **Divert valve**: If temperature at hold tube exit drops below 72°C, flow is diverted back to raw product tank — under-pasteurized product never reaches packaging.

**Strengths**:
- HTST pasteurization (72°C for 15 seconds) achieves 5-log pathogen reduction while preserving flavor, color, and nutritional quality
- Regenerative heat recovery in plate heat exchangers recovers 80-90% of thermal energy — fuel cost of only 0.1-0.3 MJ/L
- Phosphatase test provides simple verification: negative result confirms adequate heat treatment

**Weaknesses**:
- Pasteurized milk still requires refrigeration (0-4°C) with shelf life of only 5-7 days — does not eliminate cold chain dependency
- Plate heat exchanger requires stainless steel construction and food-grade gaskets — not available in early bootstrap
- Post-pasteurization contamination is the leading cause of spoilage: any breach in sanitary handling re-introduces pathogens

## Scaling Notes

- **Small-scale** (100-500 L/day): Batch pasteurizer (vat with steam jacket and agitator). LTLT method. Manual temperature monitoring. Labor: 2-3 hours per batch.
- **Community-scale** (1,000-5,000 L/day): Small plate heat exchanger with HTST. Semi-continuous. Requires boiler and stainless steel fabrication.
- **Industrial-scale** (10,000-100,000+ L/day): Large plate heat exchangers, automated controls, continuous operation. HTST or UHT. Throughput: 5,000-20,000 L/hour per unit.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Pasteurized milk spoils early | Post-pasteurization contamination, temperature abuse during storage | Clean and sanitize all equipment after pasteurization. Cool rapidly to 4°C. Maintain cold chain |
| Phosphatase test positive | Temperature too low, hold time insufficient, thermometer miscalibrated | Check and calibrate thermometers. Verify hold tube length and flow rate. Increase temperature or hold time |
| Cooked flavor (HTST) | Temperature too high, extended hold time | Reduce temperature to 72°C. Verify hold tube length matches flow rate. Check divert valve operation |

## Safety

- **Post-pasteurization contamination**: The greatest risk. Any breach in sanitary handling re-introduces pathogens. All equipment must be cleaned and sanitized between batches.
- **Divert valve failure**: Mechanical or electrical failure sends under-pasteurized product to packaging. Test divert valve regularly.
- **Temperature monitoring**: Calibrate thermometers to ±0.5°C. Recording thermometers provide documentation and traceability.

## See Also

- [Food Preservation](preservation.md) — overview hub for all preservation methods
- [Canning & Thermal Sterilization](canning.md) — complete sterilization in sealed containers
- [Dairy Processing](dairy.md) — pasteurization of milk and dairy products
- [Brewing & Distilling](brewing.md) — pasteurization of beer and wine
- [Refrigeration](refrigeration.md) — cold storage for pasteurized products
- [Traditional Preservation](traditional-preservation.md) — drying, salting, smoking
- [Energy](../energy/index.md) — steam for heat exchangers

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Food Processing](./index.md) • [All Domains](../../index.md)*
