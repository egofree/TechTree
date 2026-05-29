# Air Separation & Bulk Gas Production

> **Node ID**: chemistry.air-separation
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`cryogenics.air-separation`](../cryogenics/air-separation.md), [`energy.electricity`](../energy/electricity.md), [`gas-handling.basic`](../gas-handling/basic.md)
> **Enables**: [`chemistry.ammonia`](ammonia.md), [`machine-tools.joining`](../machine-tools/joining.md), [`silicon.crystal-growth`](../silicon/crystal-growth.md)
> **Timeline**: Years 20-40
> **Outputs**: argon, nitrogen, oxygen
> **Critical**: Yes — high-purity argon is the inert atmosphere for CZ silicon crystal growth; bulk oxygen is required for steelmaking and welding; nitrogen is the universal inert blanket gas for chemistry and metallurgy.

## Overview

Air separation produces bulk quantities of nitrogen (N₂), oxygen (O₂), and argon (Ar) from atmospheric air by cryogenic fractional distillation. Air is 78% N₂ (boiling point -196°C), 21% O₂ (bp -183°C), and 0.93% Ar (bp -186°C). The Linde double-column distillation process cools air until it liquefies, then separates the components by exploiting their different boiling points.

Three methods span the capability range:

- **Cryogenic distillation** (Linde cycle): produces high-purity N₂ (99.999%), O₂ (99.5%+), and Ar (99.999%) as gases or liquids. The only method that produces argon. Energy-intensive but produces the highest purities.
- **Pressure Swing Adsorption (PSA)**: produces N₂ (95-99.5%) or O₂ (90-95%) at small-medium scale without cryogenic temperatures. No argon production possible.
- **Membrane separation**: produces N₂ (95-99%) using hollow fiber polymer membranes. Simplest equipment, lowest capital cost, lowest purity.

Downstream, [ammonia synthesis](ammonia.md) requires N₂; [steelmaking](../metals/steelmaking.md) requires O₂; [CZ crystal growth](../silicon/crystal-growth.md) requires Ar as an inert atmosphere.

## Prerequisites

**Materials**:
- [Compressed air supply](../gas-handling/basic.md) — atmospheric air at 5-10 bar
- [Electrical power](../energy/electricity.md) — 200-500 kW for small cryogenic plant, 20-50 MW for large plant
- Molecular sieve adsorbent (3Å or 4Å zeolite for H₂O removal, 13X zeolite for CO₂ removal)
- [Copper](../metals/copper-bronze.md) or [stainless steel](../metals/iron-steel.md) tubing for heat exchangers

**Tools and equipment**:
- Multi-stage reciprocating air compressor (5-10 bar, 3-5 stages)
- Counter-current heat exchanger (shell-and-tube or plate-fin, copper or stainless steel)
- Insulated cold box (steel enclosure, perlite or mineral wool fill)
- Distillation columns (copper or stainless sieve trays, 40-70 theoretical stages)
- Expansion turbine or Joule-Thomson valve

**Infrastructure**:
- [Electrical power distribution](../energy/power-distribution.md) — baseload supply (ASU runs continuously)
- Vacuum-insulated storage dewars for liquid products
- Compressed gas cylinders for gaseous products

## Bill of Materials

| Material | Quantity per tonne O₂ produced | Source | Alternatives |
|----------|-------------------------------|--------|-------------|
| Atmospheric air | 4.5-5.0 tonnes | Ambient | No alternative |
| Electrical energy (cryogenic) | 200-400 kWh | [Power generation](../energy/electricity.md) | PSA uses 200-350 kWh/Nm³ O₂ |
| Molecular sieve (13X zeolite) | 0.1-0.5 kg (consumable, 3-7 year life) | [Chemistry](../chemistry/index.md) — synthetic aluminosilicate | Activated alumina for water removal |
| Copper tubing (heat exchanger) | 50-200 kg (one-time) | [Copper production](../metals/copper-bronze.md) | Stainless steel (lower thermal conductivity) |
| Perlite insulation | 5-20 m³ (cold box fill) | [Mining](../mining/processing.md) — expanded volcanic glass | Mineral wool, multi-layer insulation |
| Palladium catalyst (argon polishing) | 0.1-1 kg (5-10 year life) | [Precious metals](../metals/precious-metals.md) | No alternative for O₂ removal from crude argon |

## Process Description

## Cryogenic Distillation (Linde Double-Column Cycle)

**Principle**: Air is compressed, cleaned of H₂O and CO₂, cooled to cryogenic temperatures by counter-current heat exchange with outgoing product streams, then liquefied and fractionally distilled in a double-column system. The lower column operates at 5-6 bar (N₂ bp ~-177°C); the upper column at ~1.2 bar (N₂ bp ~-196°C, O₂ bp ~-183°C). The pressure difference between columns creates the temperature differential needed for thermal coupling of the lower column condenser to the upper column reboiler.

**Prerequisites**:
- [Multi-stage compressor](../energy/steam-power.md) (5-10 bar, 3-5 stages with intercoolers)
- [Counter-current heat exchanger](../gas-handling/basic.md) (copper or stainless, welded construction)
- Insulated cold box with perlite fill
- [Electrical power](../energy/electricity.md) supply (200-500 kW minimum for bootstrap plant)

**Materials**:
- Copper or stainless steel tubing for heat exchangers (6-25 mm OD, 1-2 mm wall)
- Stainless steel distillation column shell (2-4 m diameter, 25-40 m height for upper column)
- Sieve trays or structured packing (40-70 theoretical stages)
- Perlite insulation (5-20 m³ for cold box)
- Molecular sieve adsorbent (13X zeolite + activated alumina)

**Construction steps — plant assembly**:
1. Install multi-stage reciprocating compressor. Connect 3-5 stages with inter-stage shell-and-tube coolers (cool compressed air to 30-40°C between stages). Pressure: 5-10 bar output.
2. Install two molecular sieve adsorber vessels (3-5 m diameter × 5-10 m tall each). Fill with activated alumina (bottom layer, water removal) and 13X zeolite (top layer, CO₂ removal). Connect in alternating cycle — one adsorbing while the other regenerates with heated N₂ at 200-300°C for 2-4 hours.
3. Construct counter-current heat exchanger: arrange copper or stainless tubes in shell-and-tube configuration. Cold product streams (N₂, O₂) flow counter-current to warm incoming compressed air. All joints welded — no threaded fittings at cryogenic temperatures (thermal contraction causes leaks).
4. Build distillation columns. Lower column: 1.5-2.5 m diameter, 10-15 m height, 20-30 sieve trays, operates at 5-6 bar. Upper column: 2-4 m diameter, 25-40 m height, 40-70 sieve trays, operates at 1.2-1.5 bar.
5. Install condenser-reboiler between the two columns. The condensing N₂ from the lower column top provides heat to boil O₂ at the upper column bottom. This thermal coupling reduces energy consumption by 30-40% vs. single column.
6. Enclose all cryogenic equipment (heat exchangers, columns, expansion valve/turbine) in a steel cold box. Fill with perlite insulation under slight N₂ purge atmosphere to prevent moisture ingress.
7. Connect product lines: gaseous O₂ and N₂ to compressors for cylinder filling (150-200 bar) or pipeline (15-40 bar). Liquid products to vacuum-insulated dewar tanks.

**Calibration**: Start the plant from ambient temperature. Monitor temperature at cold end of heat exchanger. Full production requires 24-72 hours to cool the cold box to operating temperature (-180°C). When upper column reaches steady state, test product purity: O₂ analyser on oxygen stream (target >99.5%), N₂ analyser on nitrogen stream (target >99.99%). Adjust reflux ratio and feed point until purity targets are met.

**Expected performance**:
- O₂ purity: 99.5%+ (gaseous), 99.7%+ (liquid)
- N₂ purity: 99.99% (standard), 99.999% (with additional stages)
- Ar purity: 99.999% (5N) with argon column and catalytic polishing
- Specific energy: 0.35-0.55 kWh per Nm³ O₂ (gaseous), 0.8-1.2 kWh/Nm³ (liquid)
- Production rate (bootstrap plant): 1-10 tonnes O₂/day
- Availability: >95% (planned shutdowns every 2-4 years)

**Strengths**:
- Produces all three main gases (N₂, O₂, Ar) at high purity from a single process
- Argon production is unique to cryogenic distillation — PSA and membrane methods cannot separate argon
- Double-column thermal coupling achieves 30-40% energy savings vs. single-column design
- Product available as liquid (for storage and transport) or gas (for pipeline distribution)

**Weaknesses**:
- High capital cost and complexity — compressor, heat exchanger, distillation columns, insulated cold box
- 24-72 hour start-up time from ambient temperature — not suitable for intermittent operation
- Economical only at scale >50 tonnes O₂/day — smaller operations should use PSA
- Cold box has zero maintenance access during operation — any internal failure requires full warm-up (24-48 hours)

## Pressure Swing Adsorption (PSA)

**Principle**: Zeolite molecular sieves adsorb different gas molecules at high pressure and release them at low pressure. For O₂ production: 13X zeolite adsorbs N₂ preferentially (N₂ quadrupole moment interacts with zeolite cation sites). For N₂ production: carbon molecular sieve (CMS) adsorbs O₂ faster (kinetic diameter 0.346 nm vs. N₂ at 0.364 nm — O₂ diffuses into pores faster).

**Prerequisites**:
- [Air compressor](../gas-handling/basic.md) (3-10 bar, oil-free preferred)
- Two pressure vessels (0.5-2 m diameter, 1-3 m tall) for adsorbent beds
- Switching valves (4-way or multiple solenoid valves) for cycle control

**Materials**:
- 13X zeolite molecular sieve (for O₂ production): 50-500 kg per bed
- Carbon molecular sieve CMS (for N₂ production): 50-500 kg per bed
- Pressure vessels: carbon steel or stainless steel, rated to 10 bar
- Solenoid or pneumatic switching valves

**Construction steps — PSA nitrogen generator**:
1. Fill two pressure vessels with carbon molecular sieve (CMS). Install stainless steel mesh screens at top and bottom of each bed to contain the adsorbent. Bed depth: 1-2 m.
2. Connect vessels in parallel with switching valves. Compressed air (7-10 bar) enters the top of Bed A. O₂ is adsorbed by the CMS. N₂ passes through as product.
3. When Bed A reaches O₂ saturation (60-120 seconds), switch feed to Bed B. Bed A depressurizes to atmospheric — O₂ desorbs and vents.
4. Purge Bed A with a small fraction (10-15%) of product N₂ to fully clean residual O₂. Re-pressurize Bed A to feed pressure over 30-60 seconds.
5. Repeat cycle continuously. Two beds in alternating cycles produce continuous N₂ output.
6. Install product buffer tank (0.5-2 m³) downstream to smooth pressure fluctuations during bed switching.

**Calibration**: Install O₂ analyser on product stream. Target: <0.5% O₂ for 99.5% N₂ purity. If O₂ exceeds target, extend adsorption time or reduce feed flow rate. Higher purity requires longer cycle time = lower flow rate.

**Expected performance**:
- N₂ purity: 95-99.5% (higher purity = lower flow rate)
- O₂ purity: 90-95% (from 13X zeolite PSA)
- Flow rate: 1-3000 Nm³/hour depending on bed size
- Energy: 0.3-0.5 kWh/Nm³ N₂, 0.4-0.8 kWh/Nm³ O₂
- Cycle time: 30-120 seconds per bed
- Adsorbent life: 3-7 years

**Strengths**:
- No cryogenic temperatures — operates at ambient temperature, no cold box or insulated equipment
- Fast start-up: full production within minutes (vs. 24-72 hours for cryogenic)
- Lower capital cost for small-medium volumes (10-500 Nm³/hour)
- Simpler maintenance — no cryogenic seals, no vacuum insulation to maintain

**Weaknesses**:
- Cannot produce argon — argon co-separates with O₂ on zeolite (similar properties)
- Maximum purity limited: N₂ to 99.5%, O₂ to 95% — not sufficient for semiconductor-grade applications
- Higher energy per unit gas than large cryogenic plants at equivalent purity
- Adsorbent beds require periodic replacement (3-7 year life) at $50,000-200,000 per bed changeout

## Membrane Separation

**Principle**: Hollow fiber polymer membranes (polyimide or polysulfone) separate gases by solution-diffusion mechanism. O₂ (kinetic diameter 0.346 nm) permeates through the fiber wall faster than N₂ (0.364 nm). Compressed air flows through the fiber bores; O₂-rich permeate exits the shell side; N₂-rich product exits the bore at the opposite end.

**Prerequisites**:
- [Air compressor](../gas-handling/basic.md) (7-12 bar)
- Hollow fiber membrane module (commercially available as cartridge units)

**Materials**:
- Polyimide or polysulfone hollow fiber membrane module (0.1 mm ID fibers, thousands per module)
- Compressed air supply (7-12 bar, oil-free, dry)
- Pressure regulator and flow control valves

**Construction steps**:
1. Install membrane module vertically. Connect compressed air inlet to the bore (fiber) side at the top.
2. Connect product (N₂-rich) outlet at the bottom bore side.
3. Connect permeate (O₂-rich) outlet at the shell side.
4. Set feed pressure to 7-12 bar using pressure regulator. Higher pressure increases throughput but also energy consumption.
5. Adjust product flow rate with the outlet valve. Lower flow rate = higher N₂ purity (longer residence time in fibers).

**Calibration**: Measure O₂ content in product stream with an O₂ analyser. For 97% N₂, O₂ content should be <3%. Adjust feed pressure and product flow rate to meet target. Higher purity reduces recovery (more N₂ lost to permeate).

**Expected performance**:
- N₂ purity: 95-99% (higher purity = lower recovery = higher energy)
- Flow rate: 10-500 Nm³/hour per module
- Energy: 0.4-1.0 kWh/Nm³ N₂ at 97% purity
- O₂/N₂ selectivity: 4-8 depending on membrane material and temperature
- No moving parts in the membrane module — maintenance limited to air filters

**Strengths**:
- Simplest equipment of all methods — no cryogenic, no adsorbent beds, no switching valves
- No moving parts in the separation module — minimal maintenance
- Modular and compact — easy to scale by adding parallel modules
- Instant start-up — product available as soon as compressed air flows

**Weaknesses**:
- Lowest purity of all methods (95-99% N₂) — not sufficient for chemical synthesis or semiconductor applications
- Cannot produce argon or liquid products
- Higher energy consumption than PSA or cryogenic for equivalent N₂ purity
- Membrane modules degrade over time (5-10 year life) and require replacement

## Argon Purification

**Principle**: Argon's boiling point (-186°C) falls between N₂ (-196°C) and O₂ (-183°C), causing it to accumulate at an intermediate point in the upper distillation column at ~10-15% concentration. A side-draw feeds a separate argon column that produces crude argon (95-98% Ar). Catalytic deoxidation and final distillation produce 99.999% Ar.

**Prerequisites**:
- Cryogenic ASU with upper distillation column in steady-state operation
- Hydrogen supply for catalytic deoxidation
- Palladium catalyst (0.1-1 kg)
- Additional distillation column (60-80 theoretical stages)

**Materials**:
- Crude argon from ASU side-draw (95-98% Ar, 2-3% O₂, 1-2% N₂)
- Hydrogen gas (2-4% relative to O₂ content in crude argon)
- Palladium catalyst on alumina support
- Molecular sieve dryer (3Å zeolite)

**Construction steps**:
1. Draw vapor side-stream from upper column at the point where argon concentration peaks (typically tray 25-40 of a 70-tray column, where Ar reaches 10-15%).
2. Feed side-stream to crude argon column (60-80 theoretical stages, structured packing, operates at ~1.2 bar). Crude argon (95-97% Ar) exits at the top. Oxygen-enriched liquid returns to the upper column at the bottom.
3. Mix crude argon with hydrogen (2-4% H₂ relative to O₂ content). Pass over palladium catalyst at 400-500°C. Reaction: 2H₂ + O₂ → 2H₂O. Oxygen reduced to <1 ppm.
4. Remove water by passing through molecular sieve dryer (3Å zeolite).
5. Final distillation in pure argon column removes residual N₂ (N₂ boils at lower temperature than Ar). Product: 99.999% Ar (5N grade).

**Calibration**: Analyze product argon with gas chromatograph or mass spectrometer. Semiconductor-grade argon: O₂ <1 ppm, N₂ <5 ppm, H₂O <1 ppm, total impurities <10 ppm. Test catalytic converter efficiency by measuring O₂ in the gas stream before and after the Pd catalyst bed.

**Expected performance**:
- Crude argon purity: 95-97% Ar from side-draw column
- Final purity: 99.999% Ar (5N) after catalytic deoxidation and distillation
- Argon yield: 1-3% of air input by volume
- Semiconductor grade (6N, 99.9999%): requires additional getter purification beyond standard process

**Strengths**:
- Produces the only viable inert atmosphere for CZ crystal growth — argon cannot be substituted
- Catalytic deoxidation is efficient — reduces O₂ from 2-3% to <1 ppm in a single pass
- Argon is a byproduct of air separation — no additional raw material cost

**Weaknesses**:
- Argon constitutes only 0.93% of air — large air throughput needed for modest argon production
- Crude argon column adds 60-80 theoretical stages of distillation equipment
- Palladium catalyst is expensive and sourced from [precious metals](../metals/precious-metals.md)
- Hydrogen supply required for catalytic deoxidation — adds infrastructure dependency

## Quantitative Parameters

## Method Comparison

| Parameter | Cryogenic ASU | PSA | Membrane |
|-----------|--------------|-----|----------|
| N₂ purity (%) | 99.99-99.999 | 95-99.5 | 95-99 |
| O₂ purity (%) | 99.5+ | 90-95 | N/A (O₂ in permeate) |
| Ar production | Yes (99.999%) | No | No |
| Liquid products | Yes | No | No |
| Energy (kWh/Nm³ N₂) | 0.2-0.4 | 0.3-0.5 | 0.4-1.0 |
| Start-up time | 24-72 hours | Minutes | Minutes |
| Min. economic scale | 50 t/d O₂ | 10 Nm³/h | 5 Nm³/h |
| Capital cost | High | Medium | Low |
| Maintenance complexity | High (cryogenic) | Medium (valve switching) | Low (filter replacement) |

## Cryogenic Operating Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Compressor discharge pressure | 5-10 bar | Multi-stage with intercooling |
| Lower column pressure | 5-6 bar | N₂ bp: -177°C at this pressure |
| Upper column pressure | 1.2-1.5 bar | O₂ bp: -183°C, N₂ bp: -196°C |
| Cold end temperature approach | 2-5°C | In main heat exchanger |
| Expansion turbine inlet temperature | -100 to -130°C | Pre-cooled by main heat exchanger |
| Expansion turbine temperature drop | 30-80°C per stage | Isentropic efficiency 80-85% |
| Expansion turbine speed | 20,000-60,000 RPM | Wheel diameter 80-200 mm |
| Upper column theoretical stages | 40-70 | Structured packing or sieve trays |
| Molecular sieve regeneration temperature | 200-300°C | Heated N₂ purge for 2-4 hours |
| Cold box warm-up time | 24-48 hours | From -180°C to +20°C |

## Product Storage Parameters

| Product | Storage temp (°C) | Density (kg/L) | Expansion ratio (liquid:gas) | Evaporation loss (%/day) |
|---------|-------------------|-----------------|------------------------------|--------------------------|
| Liquid O₂ | -183 | 1.14 | 860:1 | 0.5-2.0 |
| Liquid N₂ | -196 | 0.81 | 694:1 | 0.5-2.0 |
| Liquid Ar | -186 | 1.40 | 840:1 | 0.5-1.5 |

## Scaling Notes

- **Cryogenic ASU**: Economical above ~500 Nm³/hour output (50 tonnes O₂/day). Below this, PSA is more cost-effective. Small bootstrap cryogenic plant: 1-5 tonnes/day O₂ requires 200-500 kW electrical power. World-scale: 3000 t/d O₂ draws 25-40 MW.
- **PSA**: Scales linearly from 1 to 3000 Nm³/hour by adding adsorbent beds in parallel. Each bed pair produces the same purity regardless of total flow rate.
- **Membrane**: Scales linearly by adding parallel membrane modules. Each module is independent — no interaction between modules.
- **Argon production**: Requires the full cryogenic ASU infrastructure. Argon yield is 1-3% of air input — a 100 t/d O₂ plant produces only 1-3 t/d Ar. Argon demand for CZ crystal growth is typically 10-50 Nm³/hour per puller.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| O₂ purity below 99.5% | Upper column flooding, insufficient reflux, or feed point wrong | Reduce boil-up rate. Check reflux ratio. Verify feed tray location. Inspect sieve trays for damage or plugging. |
| CO₂ freeze-up in heat exchanger | Molecular sieve adsorber exhausted or regeneration incomplete | Switch to spare adsorber. Regenerate saturated bed at 250-300°C for 4 hours. Check adsorbent age — replace if >5 years old. |
| High product temperature (cold end) | Insufficient cold production — expansion turbine or J-T valve malfunction | Check turbine speed and outlet temperature. If J-T valve: check for blockage from frozen contaminants. Verify turbine bearings not worn. |
| Excessive boiloff from liquid storage | Vacuum loss in dewar insulation or MLI degradation | Check dewar vacuum gauge (target <10 mPa). If vacuum lost: evacuate and re-seal. Replace damaged MLI during maintenance. |
| PSA O₂ breakthrough early | Adsorbent saturated or degraded; feed air too humid | Check adsorbent age. Regenerate at higher temperature. Verify air pre-dryer is functioning (dew point below -40°C). |
| Argon purity below specification | Crude Ar column upset or Pd catalyst deactivated | Check crude Ar column reflux ratio. Test Pd catalyst: measure O₂ before and after catalyst bed. Replace catalyst if O₂ removal <90%. |
| Cold box pressure rise | Air leak into cold box (moisture ingress) or internal process leak | Check N₂ purge flow to cold box (maintain slight positive pressure). Monitor cold box internal pressure. If internal leak suspected: warm up and inspect. |

## Safety

- **Cryogenic burns**: LOX (-183°C) and LN₂ (-196°C) cause severe frostbite on skin contact — tissue damage identical to third-degree thermal burns. Insulated gloves (cryogenic-rated), face shield, long sleeves, closed-toe boots mandatory. Never touch uninsulated cryogenic piping or vessels.
- **Oxygen-enriched fire hazard**: Materials that barely burn in air ignite violently in >25% O₂ atmospheres. LOX-soaked clothing becomes explosive — a static spark can cause ignition. Oil or grease on LOX-wetted surfaces can auto-ignite. Designate oxygen-safe zones: no petroleum products, no organic flooring, no oily tools. LOX spills on asphalt require exclusion until evaporation is complete.
- **Nitrogen asphyxiation**: LN₂ evaporates to ~700× its liquid volume. In confined spaces, N₂ displaces O₂ rapidly. At <19.5% O₂: impaired judgment and coordination. At <10% O₂: unconsciousness within seconds, death within minutes. Continuous O₂ monitoring (electrochemical sensor, alarm at 19.5% O₂) mandatory in all enclosed areas. Ventilate before entry. Two-person rule for confined space entry.
- **Acetylene accumulation in LOX**: Trace acetylene (C₂H₂) from air inlet can accumulate in liquid oxygen and detonate. Acetylene is soluble in LOX and can reach explosive concentrations if LOX is stored for extended periods. Remove hydrocarbons at air inlet with activated carbon filters. Monitor LOX for acetylene content. Do not store LOX for >30 days without analysis.
- **Hydrogen in argon polishing**: Hydrogen mixed with crude argon for catalytic deoxidation creates a flammable mixture if H₂ concentration exceeds 4% in air. Keep H₂ addition rate precisely controlled (2-4% relative to O₂ content). Install H₂ leak detector and automatic shutoff. Flashback arrestors on H₂ supply line.

## Quality Control

**Oxygen product**:
- Purity analysis: paramagnetic O₂ analyser (accuracy ±0.1%). Target: 99.5%+ (cryogenic), 90-95% (PSA).
- Moisture content: dew point analyser. Target: <-60°C dew point (<10 ppm H₂O).
- Hydrocarbon content: gas chromatograph. Acetylene in LOX: <0.1 ppm.

**Nitrogen product**:
- Purity analysis: thermal conductivity detector or GC. Target: 99.99% (standard), 99.999% (high-purity).
- O₂ content: electrochemical sensor. Target: <10 ppm for 99.999% N₂.
- Moisture: dew point analyser. Target: <-70°C dew point (<3 ppm H₂O).

**Argon product**:
- Purity analysis: gas chromatograph with discharge ionisation detector (DID). Target: 99.999% (5N).
- Key impurities: O₂ <1 ppm, N₂ <5 ppm, H₂O <1 ppm, H₂ <1 ppm.
- For semiconductor grade (6N): additional getter purification required, total metallic impurities <0.1 ppm.

**Molecular sieve adsorber monitoring**: Track CO₂ breakthrough time. If CO₂ appears at adsorber outlet before the scheduled switch, the bed is exhausted and requires regeneration or replacement.

## Variations and Alternatives

## Vacuum Swing Adsorption (VSA)

Lithium-exchanged zeolite (LiLSX) selectively adsorbs N₂ from air at near-ambient pressure (1.2-1.5 bar). Desorption by applying vacuum (50-100 mbar). Simpler than PSA — uses a blower instead of a compressor. Purity: 90-93% O₂. Flow: 5-150 tonnes/day. Lower energy than PSA for O₂ production.

## Bootstrap Sequence

1. **No ASU**: Obtain O₂ from thermal decomposition of metal oxides (limited quantities). N₂ from combustion gas displacement.
2. **PSA unit**: Air compressor + zeolite beds + pressure vessels. Provides 90-95% purity O₂ or 95-99.5% N₂ at small scale. No cryogenic infrastructure needed.
3. **Small cryogenic ASU**: Compressor + countercurrent heat exchanger + insulated cold box + double distillation column. Produces liquid O₂/N₂ and crude argon. Entry point for semiconductor-capable gas production.
4. **Full-scale ASU**: Rare gas recovery (Ne, Kr, Xe), expansion turbines (not just J-T valves), product liquefaction. Supports all downstream processes at scale.

## References

- [Cryogenics](../cryogenics/air-separation.md) — cryogenic engineering fundamentals
- [Gas Handling](../gas-handling/basic.md) — compressed gas systems, piping, cylinders
- [Ammonia Synthesis](ammonia.md) — major consumer of N₂ (Haber-Bosch process)
- [Silicon Crystal Growth](../silicon/crystal-growth.md) — requires high-purity Ar as inert atmosphere
- [Steelmaking](../metals/steelmaking.md) — O₂ lancing and BOF process requiring tonnage oxygen
- [Glass Melting](../glass/basic.md) — O₂-enriched combustion for glass furnaces
- [Hydrogen and Silane](hydrogen-silane.md) — H₂ used in argon polishing catalytic deoxidation
- [Electrolysis](electrolysis.md) — H₂ supply for argon purification



[← Back to Chemistry](index.md)
