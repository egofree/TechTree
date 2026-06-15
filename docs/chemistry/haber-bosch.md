# Haber-Bosch Ammonia Synthesis

> **Node ID**: chemistry.haber-bosch
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.electrolysis`](./electrolysis.md)
> **Enables**: None
> **Timeline**: Years 25-50
> **Outputs**: ammonia
> **Critical**: Yes — synthetic ammonia feeds roughly half the world's population via nitrogen fertilizer; the catalytic synthesis loop is the irreplaceable gate from atmospheric N₂ to fixed nitrogen.

## Overview

The Haber-Bosch process synthesizes ammonia from nitrogen and hydrogen:

> N₂ + 3H₂ → 2NH₃   (ΔH = −92 kJ/mol)

The reaction is exothermic and equilibrium-limited. The triple bond in N₂ (945 kJ/mol) is one of the strongest in chemistry, requiring a catalyst to dissociate it at accessible temperatures. High pressure shifts conversion toward ammonia (Le Chatelier's principle — 4 moles of gas become 2 moles). High temperature speeds kinetics but reduces equilibrium conversion. The industrial compromise is 400-500°C at 15-30 MPa (150-300 bar) over a promoted iron catalyst.

The synthesis loop operates with only 15-25% single-pass conversion. The unreacted synthesis gas is cooled to condense ammonia product, then recycled to the converter inlet. A small purge stream prevents accumulation of inert gases (argon, methane) that enter with the feedstock. Overall conversion with recycle exceeds 95%.

Historically this capability was documented within the broader [Ammonia & Fertilizer Production](./ammonia.md) article; it is extracted here as its own capability node because the synthesis step is a distinct process family with its own prerequisites (high-pressure reactor design, catalyst preparation, hydrogen feedstock) separate from downstream fertilizer chemistry. The [ammonia.md](./ammonia.md) article covers the full ammonia-to-fertilizer chain including Ostwald nitric acid, urea, and ammonium nitrate; this article focuses on the synthesis loop itself.

## Prerequisites

### Materials

- [Hydrogen feedstock](./electrolysis.md) — high-purity H₂ from water electrolysis or steam methane reforming. Purity requirement: CO+CO₂ <10 ppm, H₂O dew point <−50°C, O₂ <1 ppm. Catalyst poisons must be removed to parts-per-million levels.
- Atmospheric nitrogen — from an [air separation unit](./air-separation.md). Purity: >99.999% N₂. Oxygen is a catalyst poison; argon is inert but accumulates in the recycle loop.
- Iron catalyst — promoted magnetite (Fe₃O₄, reduced in-situ to porous metallic iron). Promoters: K₂O (1-2%), Al₂O₃ (2-4%), CaO (1-2%). Particle size 1.5-5 mm.
- [Synthesis gas compressor](../gas-handling/compressor.md) lubricant — oil-free; trace oil contaminates the catalyst.

### Tools and Equipment

- [High-pressure synthesis reactor](./reactor-vessel.md) — forged Cr-Mo or Cr-Mo-V alloy steel, rated 30+ MPa at 400-500°C. Multi-bed design (quench, tube-cooled, or radial-flow). Wall thickness 100-200 mm for large converters.
- [Compressor](../gas-handling/compressor.md) — multi-stage centrifugal (for large plants >500 t/day) or reciprocating (smaller). Synthesis gas compression: atmospheric to 15-30 MPa with inter-stage cooling. Recycle compressor: adds 3-5 MPa to overcome loop pressure drop.
- [Heat exchangers](./heat-exchanger.md) — feed-effluent exchanger (preheats feed using hot converter product), ammonia condenser (chills product gas to −20 to −33°C), inter-stage coolers on compressor.
- [Ammonia condenser/separator](./crystallizer.md) — chill product gas to −20 to −33°C to liquefy ammonia. Water-cooled or refrigerated. High-pressure separator vessel.

### Knowledge

- Heterogeneous catalysis: N₂ dissociative adsorption on the iron surface is rate-determining. The catalyst must be reduced from Fe₃O₄ to metallic Fe in-situ by H₂ flow at 350-450°C for 24-72 hours.
- Chemical equilibrium: at 450°C and 20 MPa with 3:1 H₂:N₂ feed, equilibrium NH₃ concentration is ~16%. At 30 MPa, ~27%. The gap between equilibrium and actual conversion represents kinetic limitation.
- Hydrogen embrittlement: H₂ dissociates on steel surfaces and diffuses into the metal lattice at high pressure (>10 MPa) and temperature (>200°C), causing crack initiation and propagation. Cr-Mo and Cr-Mo-V low-alloy steels are resistant; plain carbon steel is not.
- Ammonia condensation: at 20 MPa, NH₃ condenses at ~50°C. Cooling to 0°C recovers 85-90% of product as liquid. Lower temperature (−33°C) achieves >95% recovery but requires refrigeration.

### Infrastructure

- Reliable baseload power: 0.6-1.0 MWh per tonne NH₃ for the synthesis loop alone (excluding feedstock production). Total plant energy: 28-35 GJ per tonne NH₃.
- Instrument air and cooling water: synthesis loop instruments require dry, oil-free compressed air; intercoolers and condensers need 20-50 m³ cooling water per tonne NH₃.
- Emergency systems: ammonia leak detection (electrochemical sensors at 25 ppm alarm), emergency deluge water spray, self-contained breathing apparatus at converter access points.

## Bill of Materials

| Material | Quantity per tonne NH₃ | Source | Alternatives |
|----------|----------------------|--------|-------------|
| Nitrogen (N₂) | 820-830 kg (0.66 t) | [Air separation](air-separation.md) — cryogenic distillation of air | From SMR secondary reformer air injection (no separate ASU needed for SMR route) |
| Hydrogen (H₂) | 175-180 kg (stoichiometric) | [Electrolysis](electrolysis.md) — water electrolysis (50-55 kWh/kg H₂) | Steam methane reforming (SMR): CH₄ + 2H₂O → CO₂ + 4H₂ at 700-850°C |
| Iron catalyst | 0.05-0.15 kg (amortized over 5-10 year life) | On-site manufacture: Fe₃O₄ melted with K₂O/Al₂O₃/CaO promoters at 1600°C | Ruthenium catalyst (10-20× higher activity, but $500-1000/oz Ru — only for top bed) |
| Process water | 1.5-2.5 t (for steam generation and cooling) | [Water treatment](water-treatment.md) — boiler feedwater (demineralized) | Air cooling (reduces water intake 50-80% but increases capital cost) |
| Steam (for compression drivers and heating) | 1.0-1.5 t | On-site boiler or recovery from converter waste heat | Electric motor drives (if electricity is cheap) |
| Electrical energy (synthesis loop) | 0.6-1.0 MWh | [Energy](../energy/index.md) — baseload required | — |

## Process Description

### Catalyst Activation (In-Situ Reduction)

1. Charge the converter with unreduced magnetite catalyst (Fe₃O₄ granules, 1.5-5 mm). Seal the vessel and purge with N₂ to <0.5% O₂.
2. Introduce H₂/N₂ synthesis gas at 350-400°C. Reduction proceeds: Fe₃O₄ + 4H₂ → 3Fe + 4H₂O. Water exits in the product gas — monitor H₂O content to track reduction progress.
3. Ramp temperature slowly (10-20°C/hour) to 450°C over 24-72 hours. Maintain space velocity (gas flow per volume catalyst) at 5,000-10,000 h⁻¹. Excessive temperature rise indicates runaway reduction — reduce H₂ feed.
4. When H₂O in product gas drops below 50 ppm, reduction is complete. The reduced iron catalyst is pyrophoric — never expose to air.

### Synthesis Loop Operation

5. Compress the 1:3 N₂:H₂ synthesis gas (syngas) to 15-30 MPa in a multi-stage centrifugal compressor with inter-stage cooling (each stage compresses ~3:1 ratio, gas cooled to 40°C between stages).
6. Combine compressed fresh syngas with recycle gas from the loop. The combined feed enters the feed-effluent heat exchanger, where hot converter product preheats it to 380-420°C.
7. Pass the preheated gas over the iron catalyst bed(s) in the synthesis converter. Maintain 400-500°C: below 350°C the catalyst is inactive; above 530°C the catalyst sinters (loses surface area irreversibly). Single-pass conversion: 15-25% depending on converter design.
8. Cool the converter effluent (NH₃ + unreacted syngas) to 30-40°C in a water-cooled heat exchanger. Further chill to −20 to −33°C in the ammonia condenser using refrigerated ammonia or propane.
9. Separate liquid ammonia in the high-pressure separator vessel. Product: liquid NH₃ at −33°C, containing <0.5% dissolved gas. Withdraw to atmospheric-pressure storage or pressurized storage (10-17 bar at ambient temperature).
10. Return unreacted syngas from the separator top to the recycle compressor inlet. The recycle compressor adds 3-5 MPa to overcome pressure losses through the converter, heat exchangers, and piping.
11. Purge a small bleed stream (5-10% of recycle flow) to prevent accumulation of inerts (CH₄ from SMR, Ar from air separation). Inert concentration must stay below 10-15% of recycle gas composition. Route purge gas to fuel or hydrogen recovery unit.

### Shutdown

12. Reduce gas feed flow gradually (10-20%/hour). Maintain temperature above 350°C until pressure drops below 5 MPa to prevent ammonia condensation in the catalyst bed.
13. Isolate the converter. Purge with N₂ to remove NH₃ and H₂. Cool to ambient temperature under N₂ blanket.
14. If catalyst removal is required, passivate by controlled exposure to 1-2% O₂ in N₂ over 24-48 hours. Never expose hot reduced catalyst to air — it will ignite (pyrophoric).

## Quantitative Parameters

| Parameter | Quench Converter | Tube-Cooled Converter | Radial-Flow Converter |
|-----------|-----------------|----------------------|----------------------|
| Operating temperature | 400-500°C (bed inlets 400-430°C) | 400-500°C (near-isothermal) | 400-500°C (bed inlets 400-430°C) |
| Operating pressure | 15-30 MPa | 15-25 MPa | 15-20 MPa |
| Catalyst particle size | 3-5 mm | 3-5 mm | 1.5-2.0 mm (higher activity) |
| Single-pass conversion | 10-13% | 12-17% | 14-18% |
| Catalyst bed pressure drop | 0.05-0.10 MPa | 0.05-0.10 MPa | 0.2-0.5 MPa (lower than axial despite smaller particles) |
| Temperature control method | Cold-shot quench between beds | Internal cooling tubes | Indirect inter-bed cooling |
| Catalyst loading | Simple (gravity fill) | Complex (tubes obstruct loading) | Requires careful radial distribution |
| Typical plant capacity | 100-1,000 t NH₃/day | 200-600 t/day | 1,000-3,000 t/day |
| Capital cost | Lowest | Medium | Highest |

### Synthesis Loop Energy Balance

| Energy Item | Value (per tonne NH₃) | Notes |
|-------------|----------------------|-------|
| Syngas compression (atmospheric to 20 MPa) | 0.5-0.8 MWh | Multi-stage centrifugal with inter-cooling |
| Recycle compression (3-5 MPa boost) | 0.05-0.15 MWh | Overcomes loop pressure drop |
| Ammonia refrigeration/condensation | 0.10-0.20 MWh | Chill to −20 to −33°C |
| Catalyst bed heat release | +3.16 GJ (exothermic) | ΔH = −92 kJ/mol × 58,824 mol/t NH₃ |
| Total energy for synthesis loop | 0.6-1.0 MWh (net) | Waste heat generates 1.0-1.5 MPa steam for CO₂ removal or other uses |
| Total plant energy (incl. H₂ production) | 28-35 GJ (SMR route) | SMR is dominant energy consumer |

### Catalyst Composition

| Component | Content (%) | Function |
|-----------|------------|----------|
| Fe₃O₄ (magnetite, reduced to Fe) | 90-95% | Active catalyst — dissociates N₂ |
| K₂O | 1.0-2.0% | Electronic promoter — donates electrons, facilitates N₂ hydrogenation |
| Al₂O₃ | 2.0-4.0% | Structural promoter — prevents iron sintering at 400-500°C |
| CaO | 1.0-2.0% | Additional structural promoter — improves high-temperature stability |
| MgO, SiO₂ (trace) | 0.1-0.5% | Impurities from manufacturing; tolerated |

## Scaling Notes

- **Bench scale**: Laboratory fixed-bed micro-reactor (10-50 mL catalyst). Produces 1-10 g NH₃/hour. Used for catalyst evaluation, kinetic studies, and poison screening.
- **Pilot scale**: Single converter with 1-10 L catalyst, producing 1-20 kg NH₃/hour. Validates converter heat management, catalyst reduction procedure, and recycle loop operation. Compression is typically reciprocating at this scale.
- **Production scale**: 100-3,000 tonnes NH₃/day. Modern single-train plants produce 1,000-3,000 t/day. The Haldor Topsøe S-300, KBR KAAP, and ThyssenKrupp Uhde processes represent state-of-the-art designs.

Key scaling considerations:

- **Compression technology break**: Below ~500 t/day, reciprocating compressors are used (higher maintenance, lower capital). Above 500 t/day, centrifugal compressors driven by steam turbines are standard (lower maintenance, higher efficiency, but require 100+ bar steam).
- **Converter diameter**: Scale is primarily achieved by increasing converter diameter, not height. A 1,500 mm diameter converter serves ~100 t/day; a 3,000 mm diameter converter serves ~1,500 t/day. Wall thickness increases disproportionately with diameter at 30 MPa — this is the fundamental limit on single-vessel capacity.
- **Minimum economic scale**: ~100 tonnes NH₃/day for a coal-gasification or SMR-based plant. Below this, hydrogen production cost dominates and small-scale electrolysis becomes competitive. Modular electrolysis-based ammonia plants of 10-50 t/day are viable where cheap renewable electricity is available (<$0.02/kWh).
- **Heat integration**: At production scale, the exothermic heat of reaction generates 1.0-1.5 MPa steam, which drives the syngas compressor turbine or powers CO₂ removal reboiler. This integration is essential for the 28-35 GJ/t energy target — without it, energy consumption would be 40-50 GJ/t.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Single-pass conversion below 10% | Catalyst temperature outside 400-500°C window; catalyst poisoned by O₂, H₂O, CO, or CO₂; pressure below 15 MPa | Verify catalyst temperature: inactive below 350°C. Check syngas purity: CO+CO₂ must be <10 ppm (verify methanation step). Confirm loop pressure ≥15-20 MPa |
| Catalyst temperature runaway (hot spot >530°C) | Exothermic reaction accelerating in localized zone; inadequate quench or cooling; feed temperature too high | Increase quench gas flow (quench converter) or reduce feed temperature. Hot spots above 530°C cause irreversible catalyst sintering — act immediately. Monitor with multiple bed thermocouples |
| Synthesis loop inert (CH₄ + Ar) accumulation above 15% | Purge stream too small; excessive CH₄ from SMR methanation; Ar from air separation feed | Increase purge rate from 5-10% to restore inert level below 10-15%. Route purge to hydrogen recovery (cryogenic or membrane). Verify secondary reformer air feed is not introducing excess Ar |
| Ammonia condensation recovery below 85% | Chiller temperature above 0°C at separator; refrigeration compressor failure; heat exchanger fouling | Reduce chiller temperature to −20 to −33°C. Service refrigeration compressors. Clean product condenser heat exchanger. Verify separator liquid level control is not carrying over into recycle gas |
| Reduced iron catalyst igniting on air exposure | Catalyst not properly passivated before vessel opening; N₂ purge incomplete | ALWAYS purge with N₂ before opening converter. Passivate by controlled exposure to 1-2% O₂ in N₂ over 24-48 hours. Never expose hot reduced catalyst (>100°C) to air |
| Recycle compressor drawing excessive power (pressure drop >5 MPa) | Catalyst bed pressure drop increased from fine particle migration or carbon deposition; converter internal damage | Monitor loop pressure drop — normal is 3-5 MPa total. If ΔP exceeds design, reduce throughput and schedule catalyst change. Inspect radial-flow converter for flow maldistribution from uneven loading |
| Hydrogen detected in converter cooling water | Cr-Mo steel vessel wall crack from hydrogen embrittlement; internal cooling tube leak | Shut down immediately — vessel rupture risk is catastrophic. Ultrasonic wall thickness inspection. Replace affected vessel section. Use only approved Cr-Mo or Cr-Mo-V alloys for H₂ service >10 MPa |
| Fresh syngas compressor vibration alarm | Compressor surge (flow below surge point); inter-stage cooler fouling increasing back-pressure; molecular seal failure | Check compressor operating point against surge curve — increase anti-surge recycle. Clean inter-stage cooler. If vibration persists, shut down for bearing inspection — high-pressure H₂ compressor failure is explosive |

## Safety

- **High-pressure synthesis gas (H₂ + N₂ at 15-30 MPa)**: Catastrophic rupture risk. Forged steel vessels designed with 2-3× safety factor at operating temperature. Periodic inspection for hydrogen embrittlement: ultrasonic thickness, wet fluorescent magnetic particle inspection of welds, and acoustic emission monitoring. Vessel wall temperature must not exceed 450°C at the pressure shell — cold feed gas flows along the inner wall as a cooling jacket.
- **Hydrogen embrittlement**: H₂ diffuses into steel at high pressure (>10 MPa) and temperature (>200°C), causing intergranular cracking. Low-alloy Cr-Mo and Cr-Mo-V steels are resistant; plain carbon steel is not. Wall thickness monitoring is mandatory every 2-5 years. Acceptable hydrogen partial pressure for carbon steel: <0.1 MPa at 300°C.
- **Ammonia toxicity**: IDLH 300 ppm. Detectable by odor at ~5 ppm (pungent, suffocating). Olfactory fatigue occurs rapidly — do not rely on smell alone. Ammonia attacks moist tissues (eyes, lungs, mucous membranes). Fatal at ~5,000-10,000 ppm. Liquid ammonia causes severe frostbite (boiling point −33°C) and chemical burns simultaneously.
- **Pyrophoric catalyst**: Reduced iron catalyst (metallic Fe) ignites spontaneously in air. Store and handle under N₂ blanket. Passivate before vessel entry by controlled O₂ exposure (1-2% O₂ in N₂ over 24-48 hours).
- **Fire and explosion**: Synthesis gas (H₂ + N₂) is flammable/explosive when mixed with air. H₂ flammable range: 4-75% in air. Purge with N₂ before introducing H₂. Purge with N₂ before opening to air.

### PPE

- Full-face respirator or self-contained breathing apparatus (SCBA) for converter area entry during ammonia release
- Butyl rubber gloves (double-gloved) and face shield for liquid ammonia handling — ammonia dissolves many glove materials (not butyl or neoprene)
- Flame-retardant coveralls for all plant areas (H₂ service)
- Personal ammonia monitor: clip-on electrochemical sensor, audible alarm at 25 ppm

### Emergency Procedures

- Ammonia release: evacuate downwind immediately. Activate emergency water spray systems (ammonia is extremely water-soluble — 1 L water absorbs ~700 L NH₃ gas at 20°C). Full-face SCBA for response team. Do NOT attempt to isolate the leak from inside the gas cloud — use remote-operated isolation valves.
- Converter temperature runaway: increase quench gas flow immediately. If hot spot exceeds 540°C, initiate emergency shutdown (reduce feed flow by 50%, inject cold N₂ purge). Sustained high temperature causes irreversible catalyst sintering and vessel wall weakening.
- Vessel leak or rupture: evacuate all personnel to upwind assembly point. Activate emergency isolation valves (fail-close). Do NOT approach the vessel — high-pressure H₂/N₂ mixture can cut through steel piping and human tissue.
- Catalyst fire (pyrophoric ignition): smother with N₂ or dry sand. NEVER use water or CO₂ extinguisher on burning iron catalyst — water produces H₂ (worsens fire), CO₂ can decompose.

## Quality Control

### Acceptance Criteria

| Parameter | Specification | Test Method |
|-----------|--------------|-------------|
| Ammonia purity (anhydrous, commercial grade) | ≥99.5% NH₃ | Titration with standard acid; or density measurement (0.682 kg/L at −33°C for pure NH₃) |
| Water content | ≤0.2-0.5% | Karl Fischer titration (coulometric for trace levels) |
| Oil content | ≤5-10 ppm (compressor carryover) | Infrared spectrophotometry or gravimetric |
| Non-condensable gases | ≤0.5 mL/g | Gas chromatography on vaporized sample |
| Synthesis gas H₂:N₂ ratio | 2.8-3.2:1 (stoichiometric 3:1) | Mass spectrometer or thermal conductivity GC |
| Syngas CO+CO₂ | <10 ppm total | Infrared analyzer (continuous on-line) |
| Syngas H₂O | Dew point <−50°C | Chilled-mirror dew point hygrometer |

### Catalyst Performance Monitoring

- **Catalyst activity**: measured as NH₃ concentration in converter effluent at standard space velocity. Baseline at start-of-run: 15-20% NH₃. Replace catalyst when activity drops 30% from baseline (effluent <10-12% NH₃). Typical catalyst life: 5-10 years.
- **Pressure drop**: monitor daily. Baseline 0.3-0.5 MPa per bed. Increase indicates catalyst crushing, channeling, or carbon deposition. Schedule changeout when ΔP doubles from baseline.
- **Catalyst poisons**: monitor syngas for sulfur (<0.1 ppm), chlorine (<0.01 ppm), and phosphorus. These cause irreversible poisoning. Sulfur accumulates on iron surface, blocking active sites.

### Sampling Protocol

- Converter effluent: sample at each bed outlet every 8 hours. Analyze NH₃ content (absorption in standard acid, back-titrate) to build the bed temperature-conversion profile.
- Liquid ammonia product: sample daily from the separator. Analyze water and oil content.
- Syngas feed: continuous on-line analysis for CO+CO₂ (infrared), H₂O (dew point).

## Variations and Alternatives

### Converter Design Comparison

| Converter Type | Single-Pass Conversion | Capital Cost | Scale | Catalyst Loading | When to Use |
|---------------|----------------------|-------------|-------|-----------------|-------------|
| Quench (cold-shot) | 10-13% | Lowest | 100-1,000 t/day | Simple gravity fill | Bootstrap or small-scale; easiest to build and maintain |
| Tube-cooled (TVA) | 12-17% | Medium | 200-600 t/day | Complex (tubes obstruct) | Medium-scale; best temperature control |
| Radial-flow | 14-18% | Highest | 1,000-3,000 t/day | Careful radial distribution | Large-scale; highest efficiency; modern standard |

### Catalyst Alternatives

| Catalyst | Activity | Operating Conditions | Cost | When to Use |
|----------|----------|---------------------|------|-------------|
| Promoted iron (Fe₃O₄ + K₂O/Al₂O₃/CaO) | Baseline | 400-500°C, 15-30 MPa | Low | Standard for all beds in most plants |
| Ruthenium on graphite (Ba/K promoted) | 10-20× iron | 350-450°C, 7-10 MPa | Very high ($500-1,000/oz Ru) | Top bed only in KBR KAAP process; enables lower-pressure operation |
| Cobalt-molybdenum (Co-Mo) | Research stage | 300-400°C, 10-20 MPa | Medium | Not yet commercialized at scale |

### Hydrogen Source Comparison

| H₂ Source | Energy per t NH₃ | CO₂ Emissions | Capital | When to Use |
|-----------|-----------------|---------------|---------|-------------|
| Steam methane reforming (SMR) | 28-35 GJ | ~1.6 t CO₂/t NH₃ | High (reformer furnace) | Where natural gas is available; dominant global route |
| Coal gasification | 35-48 GJ | ~2.5 t CO₂/t NH₃ | Very high (gasifier + cleanup) | Where coal is abundant and gas is scarce (China) |
| Water electrolysis | 9-10 MWh (36-40 GJ) | Zero (renewable) | Medium (electrolyzer) | Where renewable electricity is cheap (<$0.02/kWh); sustainable long-term |
| Biomass gasification | 30-40 GJ | Near-zero (carbon neutral) | High | Where biomass is abundant; small-scale sustainable |

### Regional Adaptations

- **Natural gas regions** (Middle East, Russia, US Gulf): SMR-based Haber-Bosch is the economic default. Single-train plants of 1,500-3,000 t/day are standard.
- **Coal-rich regions** (China): Coal gasification provides syngas (H₂ + CO). CO is shifted to H₂ via water-gas shift. Higher energy intensity and CO₂ emissions but energy-secure.
- **Renewable energy regions** (Iceland, Norway, Australia): Electrolysis-based ammonia is viable at hydroelectric or geothermal tariffs of $0.02-0.04/kWh. Modular plants of 10-100 t/day. Green ammonia for export.

## References

- [Electrolysis](electrolysis.md) — hydrogen feedstock from water electrolysis
- [Air separation](air-separation.md) — nitrogen feedstock from cryogenic distillation
- [Ammonia & fertilizer](ammonia.md) — downstream fertilizer chemistry: Ostwald nitric acid, urea, ammonium nitrate, ammonium phosphate
- [Reactor vessels](reactor-vessel.md) — high-pressure vessel design and materials of construction
- [Iron & Steel](../metals/iron-steel.md) — Cr-Mo alloy steel forgings for converter shells and compressor casings
- [Compressors](../gas-handling/compressor.md) — multi-stage centrifugal and reciprocating gas compressors
- [Acids & Bases](acids-bases.md) — ammonia as feedstock for nitric acid (Ostwald process)

---
*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
