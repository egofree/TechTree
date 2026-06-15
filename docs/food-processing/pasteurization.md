# Pasteurization

> **Node ID**: food-processing.pasteurization
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: `energy`, [`health.sanitation`](../health/sanitation.md), `metals`
> **Enables**: None
> **Critical**: No — pasteurization improves food safety but is not the sole method for achieving it
> **Timeline**: Years 15-25
> **Outputs**: pasteurized_food

## Overview

Pasteurization is heat treatment that destroys pathogenic microorganisms without sterilizing the food. Named after Louis Pasteur (1864), it is critical for milk, juice, beer, and other liquid foods. Unlike [canning](canning.md), which achieves complete commercial sterility at 121°C, pasteurization operates at lower temperatures (63-150°C) to target specific pathogens while preserving flavor, color, and nutritional quality. The process reduces the microbial load by a defined number of log cycles (typically 5-12 log reduction) rather than eliminating all microorganisms.

Three methods dominate: LTLT (Low-Temperature Long-Time, 63°C for 30 minutes, batch), HTST (High-Temperature Short-Time, 72°C for 15 seconds, continuous), and UHT (Ultra-High Temperature, 135-150°C for 2-8 seconds, producing shelf-stable product). The governing concept is thermal death kinetics: the D-value (decimal reduction time) is the time required to kill 90% of the target organism at a given temperature. The z-value is the temperature increase needed to reduce the D-value by 90%. These two parameters define the lethality of any time-temperature combination.

Pasteurization depends on [energy](../energy/index.md) for steam, [metals](../metals/index.md) for stainless steel heat exchangers, and [health sanitation](../health/sanitation.md) knowledge of germ theory. It appears in the bootstrap chain after steam boilers and metal fabrication are established (Years 15-25). Pasteurized products — especially milk — require refrigeration ([Refrigeration](refrigeration.md)) to achieve their 5-7 day shelf life. UHT products are the exception: packaged aseptically, they last 6+ months at ambient temperature.

For complete sterilization in sealed containers, see [Canning & Thermal Sterilization](canning.md). For an overview of all preservation methods, see [Food Preservation](preservation.md).

## Prerequisites

### Materials

- **Stainless steel plates** (for plate heat exchanger): Food-grade 304 or 316 stainless steel. Thickness 0.5-1.0 mm. Source: [Metals](../metals/iron-steel.md). 316 preferred for corrosive products (acidic juices).
- **Food-grade gaskets**: EPDM or silicone rubber gaskets between heat exchanger plates. Source: [Polymers](../polymers/thermoplastics.md) or natural rubber.
- **Steam**: For heating via heat exchanger at 5-15 bar. Source: [Energy](../energy/engine.md) — requires boiler.
- **Cooling water**: For final cooling stage. Potable water. Source: [Water](../water/index.md).
- **Thermometers**: Mercury or digital, calibrated to ±0.5°C. Recording thermometers provide continuous documentation.

### Equipment

- [Plate heat exchanger](../chemistry/heat-exchanger.md) (HTST/UHT) or jacketed vat (LTLT)
- [Steam boiler](../energy/boiler.md) — 5-15 bar, sized to heat exchanger load
- Hold tube — insulated stainless steel tubing, length matched to flow rate for required residence time
- Divert valve — fails-open to redirect under-temperature product back to raw tank
- Temperature recorder — chart or digital, calibrated daily

### Knowledge

- Thermal death kinetics: D-value (time for 1-log / 90% reduction at given temperature) and z-value (temperature increase for 10× decrease in D-value). These define the lethality of any heat treatment.
- Phosphatase test: Alkaline phosphatase enzyme is destroyed at the same temperature-time as *Mycobacterium tuberculosis* (the historical target pathogen for milk pasteurization). Negative phosphatase = adequate pasteurization.
- [Germ theory and sanitation](../health/sanitation.md) — post-pasteurization contamination is the leading cause of spoilage; requires hygienic handling after treatment

### Infrastructure

- Clean, sanitary processing area — smooth washable surfaces, no wood in product contact zones
- Potable water supply — for cooling, cleaning, and product makeup
- Refrigerated storage — pasteurized product must be cooled to 4°C and held cold (except UHT)

## Bill of Materials

| Material | Specification | Quantity per 1,000 L product | Source | Alternatives |
|----------|---------------|:----------------------------:|--------|-------------|
| Raw liquid food | Milk, juice, beer | 1,000 L | [Agriculture](../foundations/food-agriculture.md), [Dairy](dairy.md) | — |
| Steam (heating) | 5-15 bar saturated | 50-150 kg (HTST), 200-400 kg (LTLT) | [Energy/Boiler](../energy/boiler.md) | Direct-fired heating jacket (less efficient) |
| Cooling water | Potable, 10-20°C inlet | 1,000-3,000 L | [Water](../water/index.md) | Chilled glycol (-5°C) for faster cooling |
| SS316 plate stock | 0.5-1.0 mm, food grade | 5-20 m² heat transfer area | [Metals](../metals/iron-steel.md) | SS304 (lower corrosion resistance) |
| EPDM gaskets | Food-grade, 2-3 mm | Full set per heat exchanger | [Polymers](../polymers/thermoplastics.md) | Silicone gaskets (higher cost, higher temp) |

## Process Description

### LTLT (Low-Temperature Long-Time) Batch Pasteurization

Traditional batch method. Gentle on flavor but slow and labor-intensive. Used for small-scale dairy and specialty products.

1. Fill a jacketed stainless steel vat with raw liquid product (milk, juice, cream).
2. Start agitation — continuous stirring ensures uniform temperature and prevents protein scorching on the heat transfer surface.
3. Open steam valve to the jacket. Heat product to 63°C at a rate of approximately 1-2°C per minute.
4. Once 63°C is reached, start the hold timer. Maintain 63°C ±0.5°C for exactly 30 minutes. Record temperature every 5 minutes.
5. After hold period, switch jacket from steam to cooling water. Cool product to 4°C as rapidly as possible (target: within 30 minutes).
6. Transfer cooled product to sanitized packaging under sanitary conditions.
7. Clean and sanitize the vat, agitator, and all contact surfaces before next batch.

### HTST (High-Temperature Short-Time) Continuous Pasteurization

Industry standard for milk. Continuous flow through plate heat exchanger with regenerative heat recovery.

1. **Raw product inlet**: Cold raw product (4°C) enters the heat exchanger via a balance tank with float valve to maintain constant feed.
2. **Regenerative heating**: Hot outgoing pasteurized product preheats incoming cold product through counterflow plates. Recovers 80-90% of thermal energy.
3. **Final heating**: Steam or hot water on one side of plates heats product to 72°C.
4. **Hold tube**: Product flows through insulated stainless steel tube sized for 15-second residence time. Tube length = flow rate × hold time. Temperature monitored at tube exit by recording thermometer.
5. **Divert valve**: If temperature at hold tube exit drops below 72°C, flow is diverted back to raw product tank — under-pasteurized product never reaches packaging.
6. **Regenerative cooling**: Outgoing hot product preheats incoming cold product (counterflow, same step as #2).
7. **Final cooling**: Cold water or chilled glycol cools product to 4°C.
8. Transfer to sanitized packaging. Maintain cold chain at 0-4°C.

### UHT (Ultra-High Temperature) Aseptic Processing

Produces shelf-stable milk (6+ months without refrigeration). Requires aseptic packaging to maintain sterility after treatment.

1. Preheat product to 80°C via regenerative heat exchange.
2. Inject high-pressure steam directly into product (direct UHT) or heat via indirect heat exchanger (indirect UHT) to 135-150°C.
3. Hold at 135-150°C for 2-8 seconds.
4. Flash-cool by sudden pressure release (direct UHT) or via heat exchanger (indirect UHT) to 80°C, then continue regenerative cooling to 20-30°C.
5. Package aseptically in pre-sterilized containers (tetra-pak or sterilized bottles) inside an aseptic filling chamber. Any post-treatment contamination destroys shelf-stability.

## Quantitative Parameters

### Pasteurization Method Comparison

| Method | Temperature | Hold Time | Target Products | Shelf Life | Energy | Log Reduction |
|--------|:-----------:|:---------:|:---------------:|:----------:|:------:|:-------------:|
| LTLT (batch) | 63°C | 30 min | Milk, cream | 5-7 days (refrigerated) | 0.3-0.5 MJ/L | 5-log |
| HTST (continuous) | 72°C | 15 sec | Milk, juice | 5-7 days (refrigerated) | 0.1-0.3 MJ/L | 5-log |
| UHT | 135-150°C | 2-8 sec | Milk, cream | 6+ months (ambient) | 0.3-0.5 MJ/L | 9-12-log |
| Flash pasteurization (beer) | 71-74°C | 15-30 sec | Beer, wine | 3-6 months | 0.1-0.2 MJ/L | 5-log (yeast, bacteria) |

### Thermal Death Kinetics — D-Values for Key Pathogens

| Organism | D-value at 60°C (min) | D-value at 63°C (min) | z-value (°C) | Target in |
|----------|:----------------------:|:----------------------:|:------------:|:---------:|
| *Mycobacterium tuberculosis* | 2.5 | 0.5 | 5.5 | Milk (historical) |
| *Coxiella burnetii* (Q fever) | 4.0 | 1.0 | 4.5 | Milk (HTST target) |
| *Salmonella* spp. | 0.2 | 0.05 | 5.5 | Eggs, juice |
| *Listeria monocytogenes* | 5.0 | 1.5 | 6.0 | Dairy |
| *C. botulinum* (type E) | 3.0 (at 65°C) | — | 10 | Low-acid (UHT target) |

D-value = decimal reduction time: time for 1-log (90%) reduction in microbial population. A 5-log reduction reduces population by a factor of 100,000. z-value = temperature increase needed to reduce D-value by 90% (10×).

## Scaling Notes

- **Small-scale** (100-500 L/day): Batch pasteurizer (jacketed vat with steam supply and agitator). LTLT method (63°C/30 min). Manual temperature monitoring with calibrated thermometer. Labor: 2-3 hours per batch. Minimum economic scale: one batch of 100 L justifies the labor.
- **Community-scale** (1,000-5,000 L/day): Small plate heat exchanger with HTST (72°C/15 sec). Semi-continuous. Requires boiler (5-10 bar) and stainless steel fabrication capability. Divert valve and temperature recorder essential.
- **Industrial-scale** (10,000-100,000+ L/day): Large plate heat exchangers, automated controls, continuous operation. HTST or UHT. Throughput: 5,000-20,000 L/hour per unit. Multiple units in parallel for larger capacity. UHT line requires aseptic packaging capability.
- **Energy efficiency**: Regenerative heat recovery in HTST plate heat exchangers recovers 80-90% of thermal energy, making the net fuel cost only 0.1-0.3 MJ/L. Without regeneration, the cost is 3-5× higher. This makes regenerative HTST the energy-efficient choice for any scale above 1,000 L/day.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Pasteurized milk spoils early (sour, curdled) | Post-pasteurization contamination, temperature abuse during storage, slow cooling | Clean and sanitize all equipment after pasteurization. Cool rapidly to 4°C within 30 min. Maintain cold chain at 0-4°C |
| Phosphatase test positive (under-pasteurization) | Temperature too low, hold time insufficient, thermometer miscalibrated | Check and calibrate thermometers to ±0.5°C. Verify hold tube length and flow rate. Increase temperature or hold time to spec |
| Cooked or sulfurous flavor (HTST) | Temperature too high, extended hold time, protein denaturation | Reduce temperature to 72°C spec. Verify hold tube length matches flow rate. Check divert valve operation |
| UHT product not shelf-stable (spoils at ambient) | Post-UHT contamination during aseptic filling, insufficient holding temperature | Check aseptic chamber integrity (HEPA filters, steam sterilization). Verify UHT temperature ≥135°C for full 2-8 sec. Check package seal |
| Divert valve cycling frequently | Boiler steam pressure unstable, heat exchanger fouling, flow rate too high | Stabilize steam supply. Clean heat exchanger plates (CIP — clean in place). Reduce flow rate to match heating capacity |
| Protein fouling on heat exchanger plates | High heating rate, high protein milk, low pH | Reduce initial heating rate. Pre-heat gradually. Clean plates with caustic (NaOH 2%) then acid (HNO₃ 1%) on CIP cycle |

## Safety

- **Post-pasteurization contamination**: The greatest risk. Any breach in sanitary handling re-introduces pathogens. All equipment must be cleaned and sanitized between batches. Pasteurization kills pathogens once; it does not protect against re-contamination.
- **Divert valve failure**: Mechanical or electrical failure sends under-pasteurized product to packaging. Test divert valve before every production run. If product reaches packaging at <72°C (HTST), the entire batch must be re-pasteurized or discarded.
- **Steam pressure hazard**: Boilers operate at 5-15 bar (150-200°C). Steam burns are severe — superheated steam is invisible and can cause third-degree burns before the victim is aware of contact. Follow [boiler safety protocols](../energy/boiler.md).
- **Temperature monitoring failure**: A miscalibrated thermometer produces under-pasteurized product that appears normal. Calibrate thermometers daily against a 0°C ice-water reference and a 100°C boiling-water reference.

### Personal Protective Equipment

- Heat-resistant gloves when operating steam valves and cleaning heat exchangers
- Face shield when opening steam lines or inspecting pressurized equipment
- Food-grade gloves and hairnet during packaging operations

## Quality Control

### Acceptance Criteria

- **Phosphatase test**: Negative result confirms adequate milk pasteurization. Alkaline phosphatase is destroyed at 72°C/15 sec — same lethality as for *M. tuberculosis*. Test every batch of pasteurized milk.
- **Temperature record**: Continuous chart or digital log showing product temperature at hold tube exit ≥72°C for the entire production run, with no divert-valve activations.
- **Coliform count**: Pasteurized product should have <10 coliforms/mL. Post-pasteurization contamination is indicated by coliform presence.
- **Standard plate count**: Pasteurized milk should have <20,000 CFU/mL. Higher counts indicate post-pasteurization contamination or temperature abuse.

### Testing Methods

- **Phosphatase test**: Add disodium phenyl phosphate to milk sample. If phosphatase enzyme is present (under-pasteurization), it liberates phenol, which produces a blue color with 2,6-dibromoquinonechloroimide (BQC). Negative = no blue color = properly pasteurized.
- **Temperature verification**: Calibrated recording thermometer at hold tube exit. Calibrate daily against ice-water (0°C) reference.
- **Microbial testing**: Standard plate count (SPC) and coliform count on samples taken after pasteurization and after 24 hours of refrigerated storage.

### Sampling Procedure

- Sample every batch of LTLT product; sample every 2 hours of continuous HTST operation.
- Sample at the packaging filler outlet (not the hold tube) — this captures any post-pasteurization contamination.
- Hold reserve samples for 7 days at 4°C for retrospective quality analysis if spoilage is reported.

## Variations and Alternatives

- **LTLT (batch, 63°C/30 min)**: Gentlest on flavor. Best for small-scale operations and specialty dairy (cream, high-fat products). Slow throughput limits use to <1,000 L/day. No plate heat exchanger required.
- **HTST (continuous, 72°C/15 sec)**: Industry standard for milk and juice. Requires plate heat exchanger with regenerative recovery. Throughput 5,000-20,000 L/hour. Best balance of quality, energy efficiency, and throughput.
- **UHT (135-150°C/2-8 sec)**: Produces shelf-stable product (6+ months ambient). Requires aseptic packaging. Flavor change (cooked note) compared to HTST. Best for distribution without cold chain or for long-term storage reserves.
- **Flash pasteurization (beer/wine, 71-74°C/15-30 sec)**: Targets yeast and spoilage bacteria without destroying desired flavor compounds. Stops fermentation in beer and wine.
- **Pulsed electric field (PEF)**: Non-thermal alternative. High-voltage pulses (20-80 kV/cm) rupture microbial cell membranes. Preserves flavor better than heat. Emerging technology — requires specialized equipment not readily bootstrappable.

### Method Selection Table

| Criterion | LTLT | HTST | UHT |
|-----------|:----:|:----:|:---:|
| Flavor quality | Best | Good | Lower (cooked note) |
| Shelf life | 5-7 days (cold) | 5-7 days (cold) | 6+ months (ambient) |
| Cold chain required | Yes | Yes | No |
| Throughput | Low (batch) | High | High |
| Energy efficiency | Low | Highest | Moderate |
| Capital cost | Lowest | Medium | Highest |
| Best for | Small dairy | All-purpose | Long distribution / storage reserve |

## References

- [Food Preservation](preservation.md) — overview hub for all preservation methods
- [Canning & Thermal Sterilization](canning.md) — complete sterilization at 121°C in sealed containers
- [Dairy Processing](dairy.md) — pasteurization of milk and dairy products
- [Brewing & Distilling](brewing.md) — flash pasteurization of beer and wine
- [Refrigeration](refrigeration.md) — cold storage for pasteurized products
- [Traditional Preservation](traditional-preservation.md) — drying, salting, smoking
- [Energy / Boiler](../energy/boiler.md) — steam supply for heat exchangers
- [Heat Exchanger](../chemistry/heat-exchanger.md) — plate heat exchanger design
- [Metals / Iron-Steel](../metals/iron-steel.md) — stainless steel for food-grade equipment
- [Health & Sanitation](../health/sanitation.md) — germ theory, post-pasteurization hygiene

---

*Part of the [Bootciv Tech Tree](../index.md) • [Food Processing](./index.md) • [All Domains](../index.md)*
