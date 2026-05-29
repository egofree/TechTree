# Waste Management

> **Node ID**: ehs.waste-management
> **Domain**: [Environmental Health & Safety](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)
> **Timeline**: Years 30-70
> **Outputs**: acid_waste_treatment, solvent_recovery, heavy_metal_precipitation, effluent_monitoring


Semiconductor manufacturing generates complex waste streams that differ fundamentally from general industrial waste: hydrofluoric acid waste containing dissolved silicon and fluoride ions, heavy metal waste from metallization processes (copper, aluminum, tungsten), mixed acid waste from etching and cleaning, solvent waste from photoresist processing, and toxic gas scrubber blowdown containing arsenic and phosphorus compounds. These waste streams cannot be discharged to municipal sewer systems without treatment — fluoride must be reduced from thousands of ppm to <10 ppm, heavy metals must be precipitated to <1 ppm, and solvent concentrations must be reduced to <50 ppm. This document defines waste treatment processes specific to semiconductor manufacturing.

## Decision Framework: Waste Treatment Selection

| Waste Stream | Primary Treatment | Polishing (if needed) | Discharge Limit | Key Risk |
|-------------|------------------|----------------------|----------------|---------|
| Fluoride (HF waste) | CaCl₂ precipitation → CaF₂ | Activated alumina adsorption or ion exchange | 10-30 mg/L F⁻ | pH must be 8-10 or F⁻ stays in solution |
| Acid (non-fluoride) | NaOH neutralization | Second-stage pH adjustment | pH 6.0-9.0 | Exothermic — temperature monitoring required |
| Heavy metals (Cu, Ni, Cr, Pb) | Hydroxide precipitation (pH 8.5-10) | Sulfide precipitation or ion exchange | 0.5-2.0 mg/L per metal | Amphoteric re-dissolution above pH 10.5 |
| Cr(VI) | Reduce to Cr(III) with Na₂S₂O₅ at pH 2-3 | Then precipitate as Cr(OH)₃ | 0.5-1.0 mg/L Cr total | Must verify complete reduction before precipitation |
| Solvents (IPA, acetone, NMP) | Distillation recovery | Activated carbon polishing for reuse | N/A (recovered) | Cross-contamination between solvent types |
| TMAH | Biological degradation (SBR) or Fenton oxidation | Activated carbon | <10 mg/L | Highly toxic — LD₅₀ 25-32 mg/kg oral rat |

## Implementation Steps

1. **Segregate at source**: Install separate collection tanks for fluoride, acid (non-fluoride), heavy metal, solvent, and caustic waste streams. Color-code piping and labels. Never mix incompatible streams.
2. **Install fluoride treatment**: Two-stage CaCl₂ precipitation system with automated pH control. Size for peak waste generation rate plus 50% safety margin.
3. **Deploy heavy metal treatment**: Hydroxide precipitation with automated pH control to 9.0-9.5. Add sulfide polishing stage if discharge limits require <0.5 mg/L metals.
4. **Set up solvent recovery**: Batch distillation units for IPA, acetone, and NMP. Vacuum distillation for high-boiling solvents (NMP bp 202°C).
5. **Install continuous effluent monitoring**: pH, fluoride, flow, and temperature at the discharge point. Daily composite samples for metals, COD, and TOC analysis by ICP-MS.
6. **Establish waste minimization program**: Track waste generation per process. Set reduction targets. Implement closed-loop rinse water recycling (50-80% water reuse).

## Waste Treatment Trade-offs

| Treatment Method | Removal Efficiency | Operating Cost | Capital Cost | Waste Residual | Complexity |
|-----------------|-------------------|---------------|-------------|---------------|------------|
| CaCl₂ precipitation (fluoride) | To 10-30 mg/L F⁻ | Low (reagent only) | Medium (tanks, mixer, clarifier) | CaF₂ sludge (hazardous) | Medium |
| Hydroxide precipitation (metals) | To <1 mg/L per metal | Low (NaOH) | Medium | Metal hydroxide sludge (hazardous) | Medium |
| Sulfide precipitation (metals) | To <0.1 mg/L per metal | Medium (Na₂S + safety controls) | Medium-High | Metal sulfide sludge (hazardous, H₂S risk) | High |
| Distillation recovery (solvents) | 90-98% recovery | Low-Medium (energy) | High (distillation unit) | Still bottoms (hazardous) | High |
| Ion exchange polishing (metals) | To <0.1 mg/L per metal | Medium (regeneration chemicals) | Medium | Spent regenerant (concentrated metal) | Medium |


## Semiconductor Waste Categories

| Waste Category | Sources | Primary Constituents | Treatment Method |
|---------------|---------|---------------------|-----------------|
| Fluoride waste | HF etching, BOE, glass etching | HF, H₂SiF₆, dissolved SiO₂, fluorosilicic acid | CaCl₂/Ca(OH)₂ precipitation → CaF₂ sludge |
| Acid waste (non-fluoride) | Sulfuric, nitric, hydrochloric, phosphoric acid processes | H₂SO₄, HNO₃, HCl, H₃PO₄ | Neutralization (NaOH/Ca(OH)₂) → salt solution |
| Mixed acid waste | RCA cleaning, piranha, multi-acid etching | H₂SO₄ + H₂O₂, HF + HNO₃, mixed acids | Segregated treatment: fluoride removal first, then neutralization |
| Solvent waste | Photoresist, stripping, cleaning | NMP, PGMEA, isopropanol, acetone, ethyl lactate | Distillation recovery or incineration |
| Heavy metal waste | Metallization, CMP, plating, etching | Cu, Al, W, Ti, Ta, Ni, Cr, Sn, Pb | Hydroxide/sulfide precipitation, ion exchange |
| Caustic waste | Developers, cleaning (SC-1 with NH₄OH) | NaOH, KOH, NH₄OH, TMAH | Neutralization (H₂SO₄/HCl) |
| Toxic gas scrubber blowdown | Hydride scrubbers, acid scrubbers | NaOH + Na₃AsO₄, Na₃PO₄, NaF, NaCl | Heavy metal precipitation (for arsenic), fluoride removal (for F) |
| Sludge | Wastewater treatment precipitation | CaF₂, metal hydroxides, metal sulfides | Dewatering, stabilization, landfill (hazardous) |
| Spent process chemicals | Spent etchants, spent cleaning solutions | Varies — see category above | Segregated by primary contaminant |
| Abatement system waste | Spent scrubber media, spent adsorbent | Impregnated carbon/alumina with adsorbed toxic gases | Hazardous waste disposal (sealed containers) |


## Fluoride Removal

Fluoride is the most challenging semiconductor waste constituent. Semiconductor HF waste contains 1,000-50,000 ppm fluoride (as F⁻). Discharge limits are typically 10-30 ppm fluoride. Treatment relies on calcium precipitation:

**Calcium fluoride precipitation**:
- Reaction: 2F⁻ + Ca²⁺ → CaF₂↓
- Solubility of CaF₂: 16 mg/L at 25°C (thermodynamic) — practical treatment achieves 10-30 mg/L fluoride residual
- Reagent: Calcium chloride (CaCl₂) or calcium hydroxide (Ca(OH)₂)
- CaCl₂ preferred for fluoride precipitation: faster reaction, better mixing, higher calcium ion availability
- Ca(OH)₂ (lime) used when simultaneous pH adjustment is needed

**Two-stage fluoride treatment system**:

Stage 1 — Co-precipitation:
1. Collect HF waste in holding tank (polyethylene or FRP-lined, never glass or concrete)
2. Add CaCl₂ solution (30% w/w) with rapid mixing (300+ RPM). Stoichiometric dose: 1.5-2.0× theoretical Ca:F molar ratio (excess calcium drives precipitation toward completion)
3. pH adjustment to 8-10 with NaOH (fluoride precipitation is pH-dependent; below pH 4, fluoride remains in solution as HF)
4. Add polymer coagulant (anionic polyacrylamide, 0.5-2.0 mg/L) to flocculate CaF₂ particles
5. Settle in clarifier (surface loading 1-2 m/h, retention 2-4 hours) or dissolved air flotation (DAF)

Stage 2 — Polishing (if needed to achieve <10 ppm fluoride):
- Second-stage precipitation with additional CaCl₂ at higher pH (10-11)
- Alternatively, ion exchange with calcium-form resin (selective fluoride removal)
- Or adsorption on activated alumina (pH 5-6 optimal, capacity 2-5 g F/kg alumina)

**CaF₂ sludge handling**:
- Sludge is 1-3% solids from clarifier. Dewater to 20-30% solids with filter press or centrifuge.
- Dewatered CaF₂ sludge is classified as hazardous waste in most jurisdictions (though CaF₂ itself is relatively inert, it contains entrained heavy metals and acids)
- Disposal: Stabilize with Portland cement or lime (solidification/stabilization) → hazardous waste landfill
- Potential recovery: High-purity CaF₂ sludge can be sold to fluoride chemical manufacturers as a feedstock for HF production (circular economy)

## General Acid Neutralization

**Non-fluoride acid waste** is neutralized with caustic:

- Reagent: 25-50% NaOH solution (most common) or Ca(OH)₂ slurry (lime, less expensive but generates more sludge)
- Target pH: 6.0-9.0 (typical discharge limit)
- Control: Automated pH control loop — pH probe in reaction tank controls NaOH feed pump via PID controller
- Reaction: exothermic (heat release up to 2 MJ per kg NaOH consumed). Temperature monitoring required — if temperature exceeds 50°C, reduce acid feed rate or add cooling
- Design: Minimum two-stage neutralization (rough adjustment in first tank, fine adjustment in second tank) to handle variable acid concentrations and avoid overshooting

**Sulfuric acid waste** (from piranha clean, H₂SO₄ processes):
- Neutralize with NaOH: H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O
- Spent piranha solution must cool to <60°C before neutralization (exothermic + residual peroxide reactivity)
- Result: Sodium sulfate solution (Na₂SO₄, soluble, non-hazardous) — dischargeable to sewer after pH confirmation

**Mixed nitric/hydrochloric acid waste**:
- Neutralize with NaOH: HNO₃ + NaOH → NaNO₃ + H₂O; HCl + NaOH → NaCl + H₂O
- Result: Sodium nitrate and sodium chloride solution — dischargeable to sewer
- Watch for nitrogen oxide (NOₓ) evolution during neutralization of concentrated nitric acid — ventilate treatment area


## Sources

- **Copper**: Damascene electroplating, CMP slurry, copper etching waste. Typical concentration: 50-5,000 mg/L Cu.
- **Aluminum**: Metallization etching, cleanroom construction waste. Typical: 10-500 mg/L Al.
- **Tungsten**: Contact plug etching, W-CMP waste. Typical: 10-1,000 mg/L W.
- **Nickel**: UBM (under-bump metallization), plating. Typical: 5-200 mg/L Ni.
- **Chromium**: Photomask fabrication, some etching processes. Typical: 1-50 mg/L Cr(VI).
- **Tin/Lead**: Soldering, bump formation. Typical: 5-100 mg/L Sn, 1-50 mg/L Pb.

## Treatment Methods

**Hydroxide precipitation** (primary method):
- Adjust pH to 8.5-10.0 with NaOH → metal hydroxide precipitates
- Solubility minima vary by metal:
  - Cu(OH)₂: minimum solubility at pH 9-10, achieves <1 mg/L Cu
  - Ni(OH)₂: minimum solubility at pH 10-11, achieves <1 mg/L Ni
  - Cr(OH)₃: minimum solubility at pH 8-9, achieves <0.5 mg/L Cr
  - Pb(OH)₂: minimum solubility at pH 9-10, achieves <0.5 mg/L Pb
- Caution: pH must be carefully controlled. Above pH 10.5, some metal hydroxides (Zn, Pb, Al, Cr) re-dissolve as soluble metal complexes (amphoteric dissolution)

**Strengths**:
- Lowest reagent cost — NaOH is inexpensive and widely available from chlor-alkali production
- Simple pH-based control — single parameter (pH 8.5-10) governs precipitation for most metals
- Well-established technology — decades of industrial operating data and design guidelines
- Compatible with standard clarification equipment — no special materials beyond corrosion-resistant tanks
- Metal hydroxide sludge is stable and non-reactive — safe for landfill after dewatering
- Simultaneous treatment of mixed metal waste streams — most metals precipitate in the same pH range

**Weaknesses**:
- Cannot achieve <0.1 mg/L for most metals — solubility limit of hydroxides sets floor at 0.5-1 mg/L
- Amphoteric re-dissolution above pH 10.5 — Zn, Pb, Al, Cr dissolve again if pH is not tightly controlled
- Large sludge volume — metal hydroxides are gelatinous and difficult to dewater (1-3% solids from clarifier)
- Not selective — all metals precipitate together, preventing metal-specific recovery for recycling
- Requires pH monitoring and control — automatic pH probe and chemical feed system needed for reliable operation

**Sulfide precipitation** (for metals with very low discharge limits):
- Add Na₂S or NaHS → metal sulfide precipitates
- Metal sulfides are orders of magnitude less soluble than metal hydroxides:
  - CuS: Ksp = 6 × 10⁻³⁷ (vs. Cu(OH)₂: Ksp = 2 × 10⁻²⁰)
  - PbS: Ksp = 3 × 10⁻²⁸ (vs. Pb(OH)₂: Ksp = 1 × 10⁻²⁰)
- Achieves effluent concentrations of <0.1 mg/L for most metals
- Disadvantage: H₂S gas evolution risk if pH drops below 7 (extremely toxic — H₂S IDLH 100 ppm). Must maintain pH >8 during sulfide treatment.
- Application: Polishing step after hydroxide precipitation to achieve stringent discharge limits

**Strengths**:
- Achieves effluent concentrations <0.1 mg/L — orders of magnitude lower than hydroxide precipitation
- Metal sulfide sludge is extremely stable — sulfides do not re-dissolve over wide pH range (2-12)
- More selective than hydroxide precipitation — can target specific metals by controlling sulfide dose and pH
- Smaller sludge volume — metal sulfides are denser and less gelatinous than metal hydroxides
- Effective for metals that hydroxide precipitation handles poorly (Cd, Hg, Ag)

**Weaknesses**:
- H₂S gas hazard — if pH drops below 7, hydrogen sulfide evolves (IDLH 100 ppm, lethal at 500+ ppm)
- Higher reagent cost than hydroxide — Na₂S and NaHS are more expensive than NaOH
- Requires strict pH control above 8 — H₂S monitoring and emergency ventilation mandatory
- Sulfide residual in effluent — excess sulfide consumes dissolved oxygen in receiving waters
- More complex operator training — sulfide chemistry and H₂S safety require specialized knowledge
- Metal sulfide sludge classified as hazardous — disposal costs higher than hydroxide sludge

**Chromium(VI) reduction**:
- Cr(VI) is highly toxic and cannot be precipitated directly — must be reduced to Cr(III) first
- Reducing agent: Sodium metabisulfite (Na₂S₂O₅) or ferrous sulfate (FeSO₄) at pH 2-3
- Reaction: 2CrO₄²⁻ + 3Na₂S₂O₅ + 6H⁺ → 2Cr³⁺ + 6SO₄²⁻ + 3H₂O
- After reduction, raise pH to 8-9 to precipitate Cr(III) as Cr(OH)₃
- Verify reduction completeness with diphenylcarbazide colorimetric test (Cr(VI) specific, detection limit 0.01 mg/L)

**Ion exchange polishing**:
- Chelating resin (iminodiacetate or aminophosphonic functional groups) selectively removes heavy metals from dilute wastewater
- Capacity: 20-40 g metal per liter of resin (depends on metal and competing ions)
- Used as a polishing step after precipitation to achieve <0.1 mg/L total metals
- Regeneration: Acid strip (5-10% H₂SO₄ or HCl) recovers concentrated metal solution for recycling or further treatment


## Solvent Waste Categories

**Photoresist solvents**: PGMEA (propylene glycol monomethyl ether acetate), ethyl lactate — from photoresist formulation and application
**Strippers**: NMP (N-methylpyrrolidone), DMSO (dimethyl sulfoxide), various amine-based formulations — for photoresist removal
**Cleaning solvents**: Isopropanol (IPA), acetone — for surface cleaning
**Miscellaneous**: Methanol, ethanol, toluene (rare in modern fabs), TCE (legacy — no longer used)

## Treatment Options

**Distillation recovery**:
- Batch distillation or fractional distillation recovers solvents for reuse
- IPA recovery: 95-98% recovery rate. Distill at 82°C (IPA boiling point). Residual water removed by molecular sieve drying
- Acetone recovery: 90-95% recovery. Distill at 56°C. Acetone losses due to volatility during handling
- NMP recovery: Distillation under vacuum (NMP bp 202°C — high boiling, vacuum distillation at 50-80°C prevents thermal degradation)
- PGMEA recovery: Distill at 146°C. Purity requirements for reuse in photoresist are very high — may require additional polishing (activated carbon treatment to remove color bodies)

**Strengths**:
- Recovers valuable solvents for reuse — 90-98% recovery reduces virgin solvent purchasing costs
- Reduces hazardous waste volume — recovered solvent is a product, not a waste
- Well-established separation technique — boiling point differences provide clean fractionation
- Compatible with multiple solvent types — same distillation unit handles IPA, acetone, NMP with different temperature settings
- Vacuum distillation handles high-boiling solvents (NMP, PGMEA) without thermal degradation

**Weaknesses**:
- Highest capital cost of any solvent treatment — distillation units cost $50,000-500,000 depending on capacity
- Energy-intensive — heating and condensation require 2-5 MJ per liter of solvent recovered
- Cannot handle highly mixed solvent waste — cross-contamination between solvent types requires separate distillation runs
- Purity may not meet semiconductor-grade specifications — recovered solvent often needs activated carbon polishing before reuse
- Fire and explosion risk — distilling flammable solvents requires explosion-proof equipment and inert atmosphere (N₂ blanket)

**Incineration** (for non-recoverable solvent waste):
- Rotary kiln or fixed-hearth incinerator at 800-1,200°C
- Complete combustion: CₓHᵧO₂ + O₂ → CO₂ + H₂O
- Scrubbing required for combustion gases (NOₓ, SO₂ if sulfur present)
- Halogenated solvents (if present) require special incineration with HCl scrubbing — typically sent to permitted hazardous waste incinerators
- Energy recovery: Heat from incineration used for process heating or steam generation

**Strengths**:
- Complete destruction of organic waste — 99.99% DRE for all non-halogenated solvents
- Handles mixed and contaminated solvents that cannot be recovered by distillation
- Energy recoverable from combustion exhaust — waste heat generates steam or process heating
- Smallest residual waste volume — combustion reduces solvent to CO₂ + H₂O (plus scrubber ash)
- No solvent purity concerns — destroys rather than recovers, eliminating quality control requirements

**Weaknesses**:
- No solvent recovery — destroys valuable material that could be reclaimed by distillation
- Requires combustion chamber rated for hazardous waste — rotary kiln or fixed-hearth at 800-1,200°C
- Generates combustion byproducts requiring scrubbing — NOₓ, SO₂, HCl (if halogens present)
- Higher regulatory burden — hazardous waste incineration requires permits, continuous emission monitoring, and compliance reporting
- Not cost-effective for high-volume recoverable solvents — waste of material value compared to distillation

## TMAH (Tetramethylammonium Hydroxide) Waste

TMAH is used as a photoresist developer and silicon etchant. It is highly toxic (LD₅₀ oral rat = 25-32 mg/kg — more toxic than many heavy metals) and causes rapid systemic poisoning through skin absorption:

- **Treatment**: Biological degradation (TMAH-degrading bacteria in sequencing batch reactors) achieving 95-99% removal. Or chemical oxidation (Fenton's reagent: H₂O₂ + Fe²⁺) breaking TMAH into trimethylamine and then further to CO₂ and NH₃.
- **Never discharge untreated** — even diluted TMAH is toxic to aquatic organisms at <10 mg/L
- Spill response: Absorb with inert material, treat as hazardous waste


## Continuous Monitoring Parameters

Semiconductor fab wastewater discharge is monitored continuously at the outfall:

| Parameter | Typical Discharge Limit | Monitoring Method |
|-----------|----------------------|-------------------|
| pH | 6.0-9.0 | Continuous pH probe |
| Fluoride (F⁻) | 10-30 mg/L | Ion-selective electrode, grab sample confirmation |
| Total suspended solids (TSS) | 30-50 mg/L | Gravimetric (daily composite) |
| Chemical oxygen demand (COD) | 100-300 mg/L | Dichromate method (daily composite) |
| Copper (Cu) | 0.5-2.0 mg/L | ICP-MS (daily composite) |
| Nickel (Ni) | 0.5-1.0 mg/L | ICP-MS (daily composite) |
| Chromium (Cr total) | 0.5-1.0 mg/L | ICP-MS (daily composite) |
| Lead (Pb) | 0.1-0.5 mg/L | ICP-MS (daily composite) |
| Arsenic (As) | 0.05-0.1 mg/L | ICP-MS (daily composite) |
| Total organic carbon (TOC) | 20-50 mg/L | TOC analyzer (continuous or daily) |

## Sampling Protocol

- **Continuous monitoring**: pH, flow, temperature — in-line sensors with data logging (minimum 1 reading per 15 minutes)
- **Daily composite**: 24-hour flow-proportioned composite sample collected by automatic sampler. Analyzed for metals, fluoride, TSS, COD, TOC.
- **Grab samples**: Collected during batch discharges, process upsets, or for parameters that cannot be composited (pH, residual chlorine, hexavalent chromium)
- **Quarterly comprehensive analysis**: Full scan of all metals, semi-volatile organics, and priority pollutants for permit compliance


## Source Reduction Strategies

- **Chemical substitution**: Replace NMP with less toxic alternatives (dibasic ester, propylene carbonate) where process allows
- **Process optimization**: Reduce chemical usage through improved process control — e.g., optimized rinse sequences reduce acid waste volume by 30-50%
- **Extended bath life**: Real-time monitoring of bath chemistry (concentration, dissolved metals) extends the useful life of process baths before disposal
- **Closed-loop recycling**: Reclaim and reuse rinse water (ion exchange + UV/oxidation treatment) — reduces freshwater consumption by 50-80% and wastewater volume proportionally
- **Point-of-use treatment**: Treat waste at the process tool (small volume, high concentration) rather than at end-of-pipe (large volume, diluted) — more efficient chemical usage in treatment

## Waste Segregation

Proper segregation at the source is critical for effective treatment:

- **Never mix** fluoride waste with non-fluoride acid waste (different treatment systems)
- **Never mix** solvent waste with aqueous waste (fire/explosion risk in treatment systems, interference with biological treatment)
- **Never mix** Cr(VI) waste with other heavy metal waste (Cr(VI) requires reduction before precipitation)
- **Segregate** copper waste from iron-bearing waste (copper poisons iron-based treatment reagents)
- **Separate** TMAH waste from all other streams (toxicity requires dedicated treatment)

## See Also

- [Chemical Safety & Toxicology](chemical-safety.md) — Properties of chemicals in waste streams
- [Ventilation & Exhaust Systems](ventilation-exhaust.md) — Scrubber blowdown handling
- [Emergency Response](emergency-response.md) — Spill response and contaminated material disposal
- [Acids & Bases](../chemistry/acids-bases.md) — Acid and alkali production for neutralization reagents
- [Sanitation](../health/sanitation.md) — General wastewater treatment principles
- [Semiconductor Chemicals](../chemistry/semiconductor-chemicals.md) — Chemical supply chain



[← Back to EHS](index.md)
