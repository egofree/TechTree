# Mineral Acid Production

> **Node ID**: chemistry.acids
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.ammonia`](ammonia.md), [`glass.basic`](../glass/basic.md), [`mining.processing`](../mining/processing.md)
> **Enables**: [`chemistry.coatings`](coatings.md), [`chemistry.explosives`](explosives.md), [`electrochemistry.anodizing`](../electrochemistry/anodizing.md), [`electrochemistry.electrochemical-processes`](../electrochemistry/electrochemical-processes.md), [`electrochemistry.electroplating`](../electrochemistry/electroplating.md), [`health.occupational-health`](../health/occupational-health.md), [`metals.finishing`](../metals/finishing.md), [`metals.non-ferrous`](../metals/non-ferrous.md), [`silicon.basic-devices`](../silicon/basic-devices.md), [`transport.telegraph`](../transport/telegraph.md)
> **Timeline**: Years 20-35
> **Outputs**: sulfuric_acid, nitric_acid, hydrochloric_acid, hydrofluoric_acid, oleum
> **Critical**: Yes — sulfuric acid is the single most important industrial chemical; the contact process enables fertilizer production, metal pickling, petroleum refining, and semiconductor wafer processing. No chemical industry operates without mineral acids.

## Overview

Sulfuric acid (H₂SO₄) is the single most important industrial chemical. It is used in every subsequent phase: steel pickling, petroleum refining, fertilizer production, etching, and semiconductor processing. A civilization's industrial maturity can be measured by its sulfuric acid production.

## Prerequisites

**Materials**:
- [Elemental sulfur or pyrite](../mining/processing.md) — sulfur source for SO₂ generation
- [Sodium nitrate (Chile saltpeter)](../mining/processing.md) — NOx source for lead chamber process
- [Vanadium ore](../mining/processing.md) — V₂O₅ catalyst for contact process
- [Fluorite (CaF₂)](../mining/processing.md) — raw material for HF production
- [Glass vessels](../glass/basic.md) — acid-resistant containers for HNO₃ and HCl

**Tools and equipment**:
- [Lead sheet](../metals/non-ferrous.md) — chamber construction for lead chamber process
- Cast iron retorts and furnaces (900-1000°C capability)
- [Distillation apparatus](distillation.md) — for acid concentration and purification

**Infrastructure**:
- [Electrical power](../energy/electricity.md) — for pumps, blowers, and instrumentation
- [Compressed air](../gas-handling/basic.md) — for sulfur combustion and gas transport

## Bill of Materials

| Material | Quantity per tonne H₂SO₄ | Source | Alternatives |
|----------|--------------------------|--------|-------------|
| Elemental sulfur | 0.33 tonnes | [Mining](../mining/processing.md) | Iron pyrite (FeS₂), smelter off-gas SO₂ |
| Vanadium pentoxide (V₂O₅) catalyst | 0.1-0.5 kg (5-10 year life) | [Mining](../mining/processing.md) | Platinum (poisoned by arsenic) |
| Molecular sieve (13X zeolite) | 50-200 kg (3-7 year life) | [Chemistry](./index.md) | Activated alumina for drying |
| Lead sheet (3-6 mm) | 5-20 tonnes (one-time, chamber) | [Metals](../metals/non-ferrous.md) | Steel with acid-resistant brick lining |
| Cast iron pipe and valves | 1-5 tonnes (one-time) | [Metals](../metals/iron-steel.md) | Stainless steel 316L for concentrated acid |

## Process Description

## Lead Chamber Process (62-70% H₂SO₄)

**Principle**: SO₂ reacts with NO₂ (nitrogen dioxide catalyst), H₂O, and O₂ in large lead-lined chambers to produce H₂SO₄. Nitrogen oxides shuttle oxygen from air to sulfur dioxide — they are regenerated continuously, acting as homogeneous catalysts.

**Prerequisites**:
- [Elemental sulfur or iron pyrite](../mining/processing.md) — SO₂ source
- [Sodium nitrate](../mining/processing.md) — NOx source for initial catalyst charge
- [Lead sheet](../metals/non-ferrous.md) (3-6 mm) — chamber construction material
- [Glass or ceramic vessels](../glass/basic.md) — for acid concentration step

**Materials**:
- Lead sheet (3-6 mm thick, 99.9% Pb) for chamber walls
- Sulfur (99%+ purity) or pyrite (FeS₂, 48% S content)
- Sodium nitrate (NaNO₃, Chile saltpeter, 97%+ purity)
- Water (ambient temperature, low mineral content)

**Construction steps**:
1. Fabricate lead chambers: solder lead sheet (3-6 mm) into rectangular boxes (10×5×5 m each). Build 3-6 chambers in series. Solder all seams with lead-tin solder — test by filling with water, inspect for leaks.
2. Install Gay-Lussac tower (packing tower, 5-10 m tall, packed with acid-resistant ceramic rings) downstream of chambers to capture NOx from exhaust gas in 50-60% H₂SO₄.
3. Install Glover tower (denitration tower, 5-8 m tall) upstream of chambers — hot SO₂ gas enters here and releases captured NOx back into the process.
4. Build sulfur burner: brick-lined furnace with sulfur melting pan. Feed solid sulfur, ignite, maintain combustion at 800-1000°C. SO₂ exits at 7% concentration in air.
5. Connect gas path: sulfur burner → Glover tower → lead chambers → Gay-Lussac tower → exhaust. Install blower to maintain gas flow.
6. Install acid collection troughs at chamber bottoms. Pipe acid to concentration vessels (glass or lead-lined steel pots for evaporation).

**Calibration**: Start sulfur combustion and establish gas flow. Monitor SO₂ concentration at chamber inlet (target 5-7% by volume). Monitor NOx at Gay-Lussac tower outlet — if NOx loss exceeds 5-10 kg HNO₃ equivalent per tonne H₂SO₄, the Gay-Lussac/Glover towers need attention. Test product acid density with hydrometer (target 1.52-1.56 g/mL for 62-70% H₂SO₄). Adjust NOx makeup rate to maintain catalyst cycle.

**Expected performance**:
- H₂SO₄ concentration: 62-70% (chamber acid), up to 78% after evaporation
- SO₂-to-H₂SO₄ conversion: 70-85%
- Production rate (bootstrap plant): 1-10 tonnes H₂SO₄/day
- NOx makeup: 5-10 kg HNO₃ per tonne H₂SO₄
- Energy: 2-5 GJ per tonne H₂SO₄ (primarily sulfur combustion heat)

**Strengths**:
- No expensive catalyst — nitrogen oxides are regenerated in the cycle, only a small makeup quantity needed
- Operates at moderate temperature (30-50°C in chambers) — no high-temperature metallurgy required
- Lead construction is straightforward — lead resists H₂SO₄ up to 78% by forming protective PbSO₄ layer

**Weaknesses**:
- Maximum acid concentration limited to 78% — above this, NOx dissolves in acid instead of staying in gas phase, breaking the catalytic cycle
- Lead is toxic — construction and maintenance involve lead exposure risk
- Lower SO₂ conversion efficiency (70-85%) compared to contact process (98-99%) — more SO₂ emitted per tonne of acid

**Yield**: ~70-85% conversion of SO₂ to H₂SO₄.

**Throughput**: 1-10 tonnes H₂SO₄ per day per plant.

## Contact Process (96-98% H₂SO₄)

**Principle**: Catalytic oxidation of SO₂ to SO₃ over vanadium pentoxide (V₂O₅) catalyst at 400-600°C, followed by absorption of SO₃ in 98% H₂SO₄ (not water — direct absorption creates an impossible-to-condense acid mist).

**Prerequisites**:
- [Elemental sulfur](../mining/processing.md) — cleaner SO₂ source than pyrite (arsenic in pyrite poisons V₂O₅ catalyst)
- [V₂O₅ catalyst](../mining/processing.md) — vanadium pentoxide on silica support, promoted with K₂SO₄
- [Acid-resistant brick](refractories.md) — converter and tower linings
- Cast iron or [stainless steel](../metals/iron-steel.md) piping — for concentrated acid service

**Materials**:
- Vanadium pentoxide catalyst (V₂O₅, 7-10% on SiO₂ support, promoted with K₂O/Na₂O, pellet form 5-10 mm diameter × 10-20 mm length)
- Elemental sulfur (99.5%+ purity, low arsenic content)
- Silica gel or molecular sieve for gas drying
- Acid-resistant brick (silica brick, 95%+ SiO₂) for converter lining

**Construction steps**:
1. Install sulfur burner: brick-lined furnace with molten sulfur spray nozzles. Combustion temperature 800-1000°C. Gas exit: 7-10% SO₂ in dry air.
2. Install gas cleaning train: electrostatic precipitator (remove dust) → 98% H₂SO₄ drying tower (remove moisture — water poisons V₂O₅ catalyst) → mist eliminator.
3. Build converter vessel: steel shell (3-5 m diameter, 8-15 m tall), lined internally with acid-resistant brick. Load 4 catalyst beds (V₂O₅/SiO₂ pellets) with inter-stage cooling coils. First bed operates at 550-600°C (fast kinetics), subsequent beds at progressively lower temperatures (450-400°C, pushing equilibrium toward SO₃).
4. Install absorption tower: packed column (10-20 m tall, ceramic or acid-brick lined), circulating 98% H₂SO₄ counter-current to SO₃ gas. SO₃ + H₂SO₄ → H₂S₂O₇ (oleum). Dilute oleum with water to desired concentration.
5. For double-absorption (modern standard): install second absorber after 3rd catalyst bed, then reheat gas and pass through 4th catalyst bed. Achieves 99.5-99.9% SO₂ conversion, reducing emissions to <100 ppm.
6. Connect product system: 98% H₂SO₄ storage tanks (carbon steel — concentrated acid passivates steel), product piping (cast iron or 316L stainless).

**Calibration**: During startup, heat converter to 380°C minimum (V₂O₅ activation temperature) using electric or gas preheaters. Feed SO₂ gas at 7-10% concentration. Monitor catalyst bed temperatures — each bed should show a temperature rise from exothermic SO₂ oxidation (ΔH = -198 kJ/mol SO₂). Test product acid concentration by hydrometer (target 1.83-1.84 g/mL for 96-98% H₂SO₄). Check SO₂ in tail gas — if >200 ppm, check catalyst activity and absorption tower efficiency.

**Expected performance**:
- H₂SO₄ concentration: 96-98% (commercial grade), 20-65% oleum as co-product
- SO₂ conversion: 97-98% (single absorption), 99.5-99.9% (double absorption)
- Catalyst life: 5-10 years (V₂O₅ is robust, tolerates mild poisoning)
- Energy: net exporter — SO₂ oxidation releases heat recovered as steam (30-50 tonnes/hour steam from a 2000 t/d plant = 10-20 MW power generation)
- Production rate (bootstrap plant): 5-50 tonnes H₂SO₄/day

**Strengths**:
- Produces concentrated acid (96-98%) — suitable for nitrations, petroleum refining, and all demanding applications
- High SO₂ conversion efficiency (98-99.9%) — minimal sulfur dioxide emissions
- Process is net energy exporter — SO₂ oxidation exotherm generates steam for power or process heat

**Weaknesses**:
- Requires vanadium catalyst (V₂O₅) — vanadium is a mined resource, not universally available
- Sulfur feed must be clean — arsenic, selenium, and halogens poison the catalyst; pyrite requires extensive gas cleaning
- Higher capital cost than lead chamber — converter, absorption towers, gas cleaning train, and inter-stage cooling equipment

## Nitric Acid Production

**Principle**: Nitric acid (HNO₃) is produced from sodium nitrate (Chile saltpeter) and concentrated sulfuric acid via acid displacement, or from ammonia via the Ostwald process (see [Ammonia Production](ammonia.md) for detailed Ostwald description).

**Prerequisites**:
- [Sulfuric acid](#contact-process-9698-h₂so₄) (93%+) — for NaNO₃ route
- [Ammonia](ammonia.md) — for Ostwald route (requires Haber-Bosch)
- [Glass or ceramic apparatus](../glass/basic.md) — HNO₃ attacks most metals except aluminum and certain stainless alloys

**Materials**:
- Sodium nitrate (NaNO₃, Chile saltpeter, 97%+ purity) or ammonia (NH₃, 99%+)
- Concentrated sulfuric acid (H₂SO₄, 93-98%)
- Cast iron or glass retort (for NaNO₃ route)
- Glass condenser and receiver (HNO₃ attacks steel, copper, rubber)

**Construction steps (NaNO₃ route)**:
1. Set up cast iron or glass retort with gas-tight lid and distillation takeoff. Install water-cooled glass condenser (spiral or Liebig type, 40-60 cm length) leading to glass receiver flask.
2. Charge retort with NaNO₃ (100 parts by weight) and concentrated H₂SO₄ (85 parts). Heat gently to 120-150°C using sand bath or oil bath — do not exceed 150°C (HNO₃ decomposes above).
3. Collect HNO₃ vapor (boiling point 83°C for 68% azeotrope) in water-cooled glass receiver. Yield: ~0.8 kg HNO₃ per kg NaNO₃.
4. For higher concentrations (90-100%), add concentrated H₂SO₄ as dehydrating agent to 68% HNO₃ and re-distill under reduced pressure.

**Calibration**: Measure product acid density with hydrometer. 68% HNO₃: density 1.41 g/mL. 90% HNO₃: density 1.48 g/mL. Test with litmus or pH paper — should show strong acid reaction. Monitor retort temperature to stay below 150°C — brown NO₂ fumes indicate thermal decomposition.

**Expected performance**:
- HNO₃ concentration: 68% (azeotrope from simple distillation), 90-100% (with H₂SO₄ dehydration)
- Yield: 0.8 kg HNO₃ per kg NaNO₃ (NaNO₃ route)
- Ostwald process: 95-98% conversion of NH₃ to HNO₃, production rate 500-3000 tonnes/day
- Storage: aluminum tanks (HNO₃ passivates aluminum) or glass carboys

**Strengths**:
- NaNO₃ route uses simple distillation apparatus — no catalyst or high-pressure equipment needed
- Ostwald process converts ammonia to nitric acid at 95-98% efficiency — highly atom-economical
- HNO₃ is a strong oxidizer enabling nitrations (explosives, dyes), fertilizer production (NH₄NO₃), and metal etching

**Weaknesses**:
- NaNO₃ route limited by saltpeter deposits — not scalable beyond a few tonnes/day
- Ostwald process requires [ammonia from Haber-Bosch](ammonia.md) — itself a high-pressure, catalyst-dependent process
- HNO₃ is a powerful oxidizer — contact with organic materials causes fire; storage requires aluminum or glass, never steel

## Hydrochloric Acid Production

**Principle**: HCl gas is generated from NaCl + H₂SO₄ (Leblanc salt cake reaction) or by direct synthesis from H₂ + Cl₂ (burns in quartz combustion chamber). The gas is absorbed in water to produce 30-38% hydrochloric acid.

**Prerequisites**:
- [Sulfuric acid](#contact-process-9698-h₂so₄) (93%+) — for NaCl route
- [Electrolysis](electrolysis.md) — for H₂ + Cl₂ direct synthesis route
- Salt (NaCl, purified) — feedstock
- [Glass or ceramic absorption column](../glass/basic.md) — for HCl gas absorption

**Materials**:
- Sodium chloride (NaCl, purified, <0.1% Ca/Mg impurities)
- Concentrated sulfuric acid (H₂SO₄, 93-98%) or H₂ + Cl₂ from [electrolysis](electrolysis.md)
- Cast iron salt cake furnace (for NaCl + H₂SO₄ route)
- Quartz or graphite combustion chamber (for H₂ + Cl₂ direct synthesis)
- Glass-packed or ceramic-packed absorption column (2-5 m tall)

**Construction steps (NaCl route)**:
1. Build salt cake furnace: cast iron retort (0.5-1 m diameter, 1-2 m long, gas-fired). Charge with NaCl + H₂SO₄. First stage at 150-200°C produces NaHSO₄ + HCl. Second stage at 550-600°C (Mannheim furnace) converts NaHSO₄ + NaCl → Na₂SO₄ + HCl.
2. Connect HCl gas outlet from furnace to absorption column (glass or ceramic packed, counter-current water flow). HCl gas dissolves exothermically — cooling water jacket on absorber required.
3. Collect 30-38% HCl in glass carboys or rubber-lined steel tanks.

**Calibration**: Measure product density (36-38% HCl: 1.18-1.19 g/mL). Test for free Cl₂ contamination — HCl should be colorless. Yellow-green tint indicates dissolved Cl₂ (remove by air stripping). Monitor absorber temperature — should not exceed 40°C (higher temperature reduces HCl solubility).

**Expected performance**:
- HCl concentration: 30-38% (absorption of HCl gas in water, azeotrope at 20.2% HCl / bp 108.6°C)
- Direct synthesis: produces >99% pure HCl gas, absorbed to 31-33% acid
- Energy: NaCl route consumes 1.5-2.5 GJ/tonne HCl (furnace heat); direct synthesis consumes ~500 kWh/tonne HCl
- Storage: glass carboys, rubber-lined steel, or PVC tanks

**Strengths**:
- NaCl + H₂SO₄ route produces HCl as co-product of soda ash production — economically efficient
- Direct synthesis from H₂ + Cl₂ produces very pure acid — suitable for food and semiconductor grades
- HCl is the fastest pickling acid for steel (2-10 minutes vs. 5-30 minutes for H₂SO₄) with better surface finish

**Weaknesses**:
- HCl attacks most metals — storage limited to glass, rubber-lined steel, PVC, or PTFE containers
- Fuming above 25% concentration — HCl gas escapes, requiring ventilated storage and handling areas
- Cannot exceed 38% concentration by simple absorption — higher concentrations require pressurized absorption or chilled water

## Hydrofluoric Acid Production

**Principle**: Fluorite (CaF₂) reacts with concentrated sulfuric acid at 200-300°C to produce hydrogen fluoride gas (HF, bp 19.5°C). HF gas is absorbed in water to produce 48-50% aqueous HF, or distilled to produce anhydrous HF.

**Prerequisites**:
- [Fluorite (CaF₂)](../mining/processing.md) — acid-grade fluorspar (>97% CaF₂)
- [Sulfuric acid](#contact-process-9698-h₂so₄) (93-98%) — reactant
- [Lead or steel retort](../metals/iron-steel.md) — HF attacks glass, never use glass apparatus
- PTFE or polyethylene containers — for product storage

**Materials**:
- Acid-grade fluorspar (CaF₂, >97% purity, <1.5% SiO₂ — silica consumes HF as SiF₄)
- Concentrated sulfuric acid (H₂SO₄, 93-98%)
- Horizontal rotary kiln (steel shell, internally carbon-lined, 5-10 m long × 0.5-1 m diameter)
- Lead or PTFE condenser and absorption system
- PTFE or HDPE storage containers

**Construction steps**:
1. Build horizontal rotary kiln: steel shell (5-10 m × 0.5-1 m), internally lined with carbon blocks. Rotate at 1-3 RPM. Gas-fired or electrically heated to 200-300°C.
2. Charge fluorspar and sulfuric acid (1:1.25 mass ratio CaF₂:H₂SO₄). CaF₂ + H₂SO₄ → 2HF↑ + CaSO₄. Residence time: 30-60 minutes.
3. Collect HF gas (bp 19.5°C) from kiln outlet. Pass through dust separator (cyclone), then absorb in water in lead or PTFE absorption column. Product: 48-50% aqueous HF.
4. For anhydrous HF: distill from aqueous solution in steel column (HF passivates steel at anhydrous concentrations). Collect HF at 19.5°C boiling point. Store in steel cylinders.

**Calibration**: Measure product concentration by titration with standardized NaOH (target: 48-50% HF, density 1.15-1.17 g/mL). Test for sulfuric acid contamination by adding BaCl₂ — white precipitate indicates SO₄²⁻ carryover. Verify absence of SiF₆²⁻ (hexafluorosilicate, from silica impurity) by ammoniacal precipitation test.

**Expected performance**:
- HF concentration: 48-50% (aqueous, commercial grade), >99.9% (anhydrous)
- Yield: 0.95 tonnes HF per tonne CaF₂
- Energy: 1.5-3 GJ per tonne HF (kiln heating)
- Kiln throughput: 5-50 tonnes HF/day

**Strengths**:
- HF uniquely dissolves silica and glass (SiO₂ + 4HF → SiF₄ + 2H₂O) — essential for glass etching and silicon wafer processing
- Anhydrous HF is a powerful alkylation catalyst for petroleum refining and a precursor to fluoropolymers (PTFE, PVDF)
- Relatively simple production from two common minerals (fluorspar + sulfuric acid)

**Weaknesses**:
- HF is the most hazardous common acid — penetrates skin without pain, binds tissue calcium, causes systemic hypocalcemia and cardiac arrest at 2.5% body surface area exposure
- Attacks glass, ceramics, and all silica-containing materials — all equipment must be metal, PTFE, or polyethylene
- Calcium gluconate gel antidote must be staged at every HF handling location before any work begins

## Other Acid Types

#### Aqua Regia

A mixture of concentrated nitric acid and hydrochloric acid (typically 1:3 by volume HNO₃:HCl). The only common reagent that dissolves gold and platinum group metals. Critical for precious metal refining and electrorefining anode slime processing.

**Chemistry**: HNO₃ oxidizes HCl to generate chlorine (Cl₂) and nitrosyl chloride (NOCl) in situ. These reactive species attack gold: 2Au + 3Cl₂ → 2AuCl₃ (soluble as chloroauric acid H[AuCl₄] in excess HCl). Platinum dissolves similarly as H₂[PtCl₆]. The combination works because nitric acid provides the oxidizing power while chloride ions complex the dissolved metal ions, shifting equilibrium toward dissolution.

**Preparation**: Mix immediately before use — aqua regia loses potency within hours as chlorine and NOCl evaporate. Add HNO₃ to HCl slowly in a glass vessel under a fume hood. The mixture turns orange-yellow from dissolved Cl₂ and NOCl gases. **Never store aqua regia in sealed containers** — decomposition produces gas pressure that ruptures glass.

**Applications**: Dissolving gold from electronic scrap, recovering platinum from catalytic converters, processing anode slime from copper electrorefining. After dissolution, gold is recovered by precipitation with ferrous sulfate (FeSO₄) or sodium metabisulfite (Na₂S₂O₅), or by solvent extraction with dibutyl carbitol.

#### Phosphoric Acid

Phosphoric acid (H₃PO₄) bridges mineral acid production to fertilizer chemistry. Two production routes of very different complexity.

**Wet process** (fertilizer-grade, 85% of production):
- Phosphate rock (Ca₃(PO₄)₂, fluorapatite Ca₅(PO₄)₃F) reacted with concentrated sulfuric acid (93-98%) in a stirred tank at 70-80°C: Ca₃(PO₄)₂ + 3H₂SO₄ → 2H₃PO₄ + 3CaSO₄.
- Filter calcium sulfate (phosphogypsum) — massive byproduct (~5 tonnes per tonne P₂O₅ produced, often stacked in waste piles). The filtrate is 25-30% H₃PO₄ (green acid), concentrated to 40-54% P₂O₅ by vacuum evaporation.
- Impurities: fluorine (as HF and SiF₄ — recovered as Na₂SiF₆ for fluoride salts), cadmium, uranium, and rare earth elements (sometimes recovered). Wet-process acid is not pure enough for food or semiconductor use.

**Thermal process** (pure-grade, 15% of production):
- Burn elemental white phosphorus (P₄) in excess air → P₄O₁₀ (phosphorus pentoxide). P₄O₁₀ + 6H₂O → 4H₃PO₄.
- Produces very pure acid suitable for food additives, pharmaceuticals, and semiconductor etching. White phosphorus is produced by reducing phosphate rock with coke in an electric arc furnace at 1500°C: 2Ca₃(PO₄)₂ + 6SiO₂ + 10C → 6CaSiO₃ + 10CO + P₄. The P₄ vapor condenses under water (pyrophoric — ignites in air).

**Fertilizer bridge**: Phosphoric acid is reacted with ammonia to produce monoammonium phosphate (MAP, 11-52-0) and diammonium phosphate (DAP, 18-46-0) — the world's most important phosphate fertilizers. Reacted with phosphate rock to produce superphosphate (single: Ca(H₂PO₄)₂, or triple: higher P content).

## Pickling Acids

Steel pickling removes oxide scale (mill scale, rust) from steel surfaces before further processing (galvanizing, plating, cold rolling, welding).

**[Sulfuric acid pickling](../glossary/sulfuric-acid-pickling.md)** (traditional):
- 10-25% H₂SO₄ at 60-80°C. Soak steel 5-30 minutes. Scale dissolves: Fe₂O₃ + 3H₂SO₄ → Fe₂(SO₄)₃ + 3H₂O. Base metal also dissolves slowly: Fe + H₂SO₄ → FeSO₄ + H₂↑ (hydrogen embrittlement risk — bake out at 200°C after pickling).
- Spent acid: FeSO₄ concentration reaches 15-25%, acid depleted to <5%. Recovery: chill to crystallize FeSO₄·7H₂O (copperas), regenerate acid by adding concentrated H₂SO₄. Or spray roast: atomize spent acid into a furnace at 800-1000°C → Fe₂O₃ + SO₂ + H₂O. SO₂ captured for sulfuric acid production (closed loop). HCl roaster produces HCl gas for acid regeneration.

**[Hydrochloric acid pickling](../glossary/hydrochloric-acid-pickling.md)** (modern, dominant):
- 15-20% HCl at 35-40°C. Faster than sulfuric (2-10 minutes). Less base metal attack, less hydrogen embrittlement, better surface finish. Scale dissolves: Fe₂O₃ + 6HCl → 2FeCl₃ + 3H₂O.
- Spent acid recovery: spray roaster produces Fe₂O₃ (sellable pigment) and HCl gas (absorbed in water → regenerated acid). Closed-loop acid recovery is standard in modern steel plants.

## Semiconductor-Grade Acid Production

Semiconductor processing requires ultra-pure acids (trace metal impurities at ppb — parts per billion — levels). Standard industrial acids contain Fe, Cu, Pb, As at ppm levels — unsuitable for wafer processing.

**Purification methods**:
- **Distillation**: Fractional distillation in quartz or PTFE equipment removes most metal contaminants. H₂SO₄ boils at 337°C at atmospheric pressure but decomposes near its boiling point; distilled under reduced pressure at lower temperatures to avoid decomposition. HCl distilled as gas from azeotropic solution. HF distilled at 112°C (under pressure). Multi-pass distillation achieves <1 ppb metal content.
- **Sub-boiling distillation**: Heat acid below its boiling point in a PTFE or quartz still. Only the purest vapor fraction condenses on a cooled surface. Slow (days per batch) but achieves ultra-trace purity (<0.1 ppb for most metals). Used for ACS reagent-grade and semiconductor-grade acids.
- **Ion exchange**: Pass acid through chelating resin columns that selectively adsorb metal ions. Effective for HCl, HNO₃, and HF. Resin regenerated with acid or chelating solution.
- **Containers**: PTFE (Teflon) bottles for storage and transport. Quartz for distillation. Stainless steel only for concentrated HNO₃ (passivated) and H₂SO₄ (>90%). All wetted surfaces must not leach contaminants.

**Grade specifications**: SEMI Grade (semiconductor): <10 ppb each for 30+ trace metals. Trace metal analysis by ICP-MS (inductively coupled plasma mass spectrometry). Each batch certified with certificate of analysis.

## Historical Development Timeline

1. **Pre-1700 (alchemy)**: "Oil of vitriol" (dilute H₂SO₄) by distilling green vitriol (FeSO₄·7H₂O). "Aqua fortis" (HNO₃) from saltpeter + vitriol. "Spirit of salt" (HCl) from salt + vitriol.
2. **1746**: Joshua Ward's lead chamber process — first industrial H₂SO₄. Lead chambers, 6×6×6 feet.
3. **1791**: Leblanc process drives massive H₂SO₄ demand (for salt → soda ash). Lead chambers scaled to industrial size.
4. **1831**: Peregrine Phillips patents contact process (Pt catalyst). Not commercially viable until V₂O₅ catalyst (1920s) — platinum poisoned by arsenic in sulfur feed.
5. **1900s**: Haber-Bosch ammonia → Ostwald nitric acid. Transforms HNO₃ from scarce luxury chemical to bulk commodity.
6. **1930s**: Fluorite mining enables HF production → aluminum industry, petroleum alkylation, semiconductor etching.
7. **1960s**: Semiconductor-grade acid purification begins. Sub-boiling distillation, PTFE containers, ppb trace metal specifications.
8. **Present**: Global H₂SO₄ production ~250 million tonnes/year (largest-volume chemical). Most goes to fertilizer production (phosphoric acid, ammonium sulfate).

## Safety

- **Sulfuric acid (H₂SO₄)**: Concentrated acid (98%, density 1.84 g/mL) causes severe chemical burns and is intensely dehydrating — chars organic matter on contact. Heat of dilution: 880 kJ/kg. ALWAYS add acid to water, NEVER water to acid — adding water to concentrated acid creates a small volume of boiling, concentrated solution that violently spatters. PPE: acid-resistant gloves (neoprene), face shield, chemical apron. Emergency: flush with copious water for 15+ minutes. Store concentrated H₂SO₄ in carbon steel tanks (passivates steel at >85% concentration); dilute acid requires rubber-lined steel or 316L stainless steel.
- **Nitric acid (HNO₃)**: Concentrated HNO₃ (68%, density 1.41 g/mL) is a powerful oxidizer. Contact with organic materials (paper, wood, solvents) causes fire. Produces toxic NO₂ fumes (brown gas, TLV 3 ppm, IDLH 20 ppm — lung damage at low concentrations). Store in aluminum tanks (HNO₃ passivates aluminum, forming Al₂O₃ film) or glass carboys. NEVER store in carbon steel (vigorous reaction). PPE: face shield, acid-resistant gloves, chemical apron. Work under fume hood.
- **Hydrochloric acid (HCl)**: Fumes are corrosive to respiratory tract — detectable at 5 ppm, dangerous at 100 ppm, IDLH 50 ppm. Scrub vent gases through NaOH solution. Store in rubber-lined steel, glass, or PVC containers. Carbon steel is NOT suitable for HCl service. PPE: chemical splash goggles, neoprene gloves, face shield.
- **Hydrofluoric acid (HF)**: EXCEPTIONALLY DANGEROUS. Dissolves bone by binding calcium. Penetrates skin without immediate pain — the delay makes exposure more dangerous. Lethal at ~2.5% body surface area exposure to 50% HF (a hand-sized splash can kill via hypocalcemia-induced cardiac arrest). **Calcium gluconate gel (2.5%) MUST be on-site before any HF handling** — apply immediately to exposed skin, massage for 15+ minutes, seek emergency medical treatment. PPE: neoprene gloves (NOT latex — HF penetrates latex), face shield, chemical apron. Storage: PTFE or polyethylene containers ONLY. NEVER glass (HF etches SiO₂). Double-contained: primary container inside secondary containment tray.

## Quantitative Parameters

## Acid Concentration and Properties

| Acid | Concentration | Density (g/mL) | Boiling Point (°C) | Storage Material |
|------|--------------|----------------|--------------------|-----------------|
| H₂SO₄ (chamber) | 62-70% | 1.52-1.56 | 170-185 | Lead, glass |
| H₂SO₄ (concentrated) | 93-98% | 1.83-1.84 | 337 | Carbon steel |
| HNO₃ (azeotrope) | 68% | 1.41 | 122 | Aluminum, glass |
| HNO₃ (fuming) | 90-100% | 1.48-1.51 | 83 | Aluminum, glass |
| HCl (concentrated) | 36-38% | 1.18-1.19 | 108.6 (azeo) | Glass, rubber-lined steel |
| HF (commercial) | 48-50% | 1.15-1.17 | 112 (azeo) | PTFE, polyethylene |
| Oleum | 20-65% free SO₃ | 1.89-2.00 | — | Carbon steel |

## Materials of Construction for Acid Service

| Material | H₂SO₄ (dilute) | H₂SO₄ (conc.) | HCl | HNO₃ | HF | NaOH |
|----------|----------------|----------------|-----|------|----|------|
| Carbon steel | ✗ (corrodes) | ✓ (passivates >85%) | ✗ | ✗ | ✗ | ✓ (dilute) |
| Stainless 316 | ✓ (room temp) | ✓ (<60°C) | ✗ | ✓ | ✗ | ✓ |
| Lead | ✓ (to 78%) | ✗ (>85%) | ✗ | ✗ | ✗ | ✗ |
| Glass/ceramic | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (hot) |
| PTFE (Teflon) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| PVC/CPVC | ✓ (room temp) | ✗ (hot) | ✓ | ✓ (dilute) | ✓ | ✓ |

## Acid Azeotropes

| Acid | Azeotrope Concentration | Boiling Point at 1 atm |
|------|------------------------|----------------------|
| HCl | 20.2% | 108.6°C |
| HNO₃ | 68% | 122°C |
| H₂SO₄ | 98.3% (technical max) | 337°C |
| HF | 38% | 112°C |

## Semiconductor-Grade Acid Production

Semiconductor processing requires ultra-pure acids (trace metal impurities at ppb — parts per billion — levels). Standard industrial acids contain Fe, Cu, Pb, As at ppm levels — unsuitable for wafer processing.

**Purification methods**:
- **Distillation**: Fractional distillation in quartz or PTFE equipment removes most metal contaminants. H₂SO₄ boils at 337°C at atmospheric pressure but decomposes near its boiling point; distilled under reduced pressure at lower temperatures to avoid decomposition. Multi-pass distillation achieves <1 ppb metal content.
- **Sub-boiling distillation**: Heat acid below its boiling point in a PTFE or quartz still. Only the purest vapor fraction condenses on a cooled surface. Slow (days per batch) but achieves ultra-trace purity (<0.1 ppb for most metals). Used for semiconductor-grade acids.
- **Ion exchange**: Pass acid through chelating resin columns that selectively adsorb metal ions. Effective for HCl, HNO₃, and HF.
- **Containers**: PTFE (Teflon) bottles for storage and transport. Quartz for distillation. All wetted surfaces must not leach contaminants.

**Grade specifications**: SEMI Grade (semiconductor): <10 ppb each for 30+ trace metals. Trace metal analysis by ICP-MS. Each batch certified with certificate of analysis.

## Historical Development Timeline

1. **Pre-1700 (alchemy)**: "Oil of vitriol" (dilute H₂SO₄) by distilling green vitriol (FeSO₄·7H₂O). "Aqua fortis" (HNO₃) from saltpeter + vitriol. "Spirit of salt" (HCl) from salt + vitriol.
2. **1746**: Joshua Ward's lead chamber process — first industrial H₂SO₄.
3. **1791**: Leblanc process drives massive H₂SO₄ demand.
4. **1831**: Peregrine Phillips patents contact process (Pt catalyst). Not commercially viable until V₂O₅ catalyst (1920s).
5. **1900s**: Haber-Bosch ammonia → Ostwald nitric acid.
6. **1930s**: Fluorite mining enables HF production → aluminum industry, petroleum alkylation, semiconductor etching.
7. **1960s**: Semiconductor-grade acid purification begins. Sub-boiling distillation, PTFE containers, ppb trace metal specifications.
8. **Present**: Global H₂SO₄ production ~250 million tonnes/year (largest-volume chemical).

## References

- [Alkalis](alkalis.md) — complementary acid-base chemistry (NaOH, Na₂CO₃ production)
- [Electrolysis](electrolysis.md) — chlor-alkali process producing HCl and Cl₂
- [Solvents](solvents.md) — acid-catalyzed solvent synthesis
- [SEM Tech Electrodialysis](sem-tech-electrodialysis.md) — membrane-based acid recovery from waste streams
- [Distillation](distillation.md) — purification of volatile acids
- [Coatings](coatings.md) — acid etching and pickling of metal surfaces
- [Ammonia](ammonia.md) — ammonia as feedstock for Ostwald nitric acid process



[← Back to Chemistry](index.md)
