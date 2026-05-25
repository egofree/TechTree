# Waste Management

> **Node ID**: ehs.waste-management
> **Domain**: [Environmental Health & Safety](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`ehs.chemical-safety`](chemical-safety.md)
> **Timeline**: Years 30-70
> **Outputs**: acid_waste_treatment, solvent_recovery, heavy_metal_precipitation, effluent_monitoring

## Problem

Semiconductor manufacturing generates complex waste streams that differ fundamentally from general industrial waste: hydrofluoric acid waste containing dissolved silicon and fluoride ions, heavy metal waste from metallization processes (copper, aluminum, tungsten), mixed acid waste from etching and cleaning, solvent waste from photoresist processing, and toxic gas scrubber blowdown containing arsenic and phosphorus compounds. These waste streams cannot be discharged to municipal sewer systems without treatment — fluoride must be reduced from thousands of ppm to <10 ppm, heavy metals must be precipitated to <1 ppm, and solvent concentrations must be reduced to <50 ppm. This document defines waste treatment processes specific to semiconductor manufacturing.

## Waste Stream Classification

### Semiconductor Waste Categories

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

## Acid Waste Treatment

### Fluoride Removal

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

### General Acid Neutralization

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

## Heavy Metal Waste Treatment

### Sources

- **Copper**: Damascene electroplating, CMP slurry, copper etching waste. Typical concentration: 50-5,000 mg/L Cu.
- **Aluminum**: Metallization etching, cleanroom construction waste. Typical: 10-500 mg/L Al.
- **Tungsten**: Contact plug etching, W-CMP waste. Typical: 10-1,000 mg/L W.
- **Nickel**: UBM (under-bump metallization), plating. Typical: 5-200 mg/L Ni.
- **Chromium**: Photomask fabrication, some etching processes. Typical: 1-50 mg/L Cr(VI).
- **Tin/Lead**: Soldering, bump formation. Typical: 5-100 mg/L Sn, 1-50 mg/L Pb.

### Treatment Methods

**Hydroxide precipitation** (primary method):
- Adjust pH to 8.5-10.0 with NaOH → metal hydroxide precipitates
- Solubility minima vary by metal:
  - Cu(OH)₂: minimum solubility at pH 9-10, achieves <1 mg/L Cu
  - Ni(OH)₂: minimum solubility at pH 10-11, achieves <1 mg/L Ni
  - Cr(OH)₃: minimum solubility at pH 8-9, achieves <0.5 mg/L Cr
  - Pb(OH)₂: minimum solubility at pH 9-10, achieves <0.5 mg/L Pb
- Caution: pH must be carefully controlled. Above pH 10.5, some metal hydroxides (Zn, Pb, Al, Cr) re-dissolve as soluble metal complexes (amphoteric dissolution)

**Sulfide precipitation** (for metals with very low discharge limits):
- Add Na₂S or NaHS → metal sulfide precipitates
- Metal sulfides are orders of magnitude less soluble than metal hydroxides:
  - CuS: Ksp = 6 × 10⁻³⁷ (vs. Cu(OH)₂: Ksp = 2 × 10⁻²⁰)
  - PbS: Ksp = 3 × 10⁻²⁸ (vs. Pb(OH)₂: Ksp = 1 × 10⁻²⁰)
- Achieves effluent concentrations of <0.1 mg/L for most metals
- Disadvantage: H₂S gas evolution risk if pH drops below 7 (extremely toxic — H₂S IDLH 100 ppm). Must maintain pH >8 during sulfide treatment.
- Application: Polishing step after hydroxide precipitation to achieve stringent discharge limits

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

## Solvent Waste Management

### Solvent Waste Categories

**Photoresist solvents**: PGMEA (propylene glycol monomethyl ether acetate), ethyl lactate — from photoresist formulation and application
**Strippers**: NMP (N-methylpyrrolidone), DMSO (dimethyl sulfoxide), various amine-based formulations — for photoresist removal
**Cleaning solvents**: Isopropanol (IPA), acetone — for surface cleaning
**Miscellaneous**: Methanol, ethanol, toluene (rare in modern fabs), TCE (legacy — no longer used)

### Treatment Options

**Distillation recovery**:
- Batch distillation or fractional distillation recovers solvents for reuse
- IPA recovery: 95-98% recovery rate. Distill at 82°C (IPA boiling point). Residual water removed by molecular sieve drying
- Acetone recovery: 90-95% recovery. Distill at 56°C. Acetone losses due to volatility during handling
- NMP recovery: Distillation under vacuum (NMP bp 202°C — high boiling, vacuum distillation at 50-80°C prevents thermal degradation)
- PGMEA recovery: Distill at 146°C. Purity requirements for reuse in photoresist are very high — may require additional polishing (activated carbon treatment to remove color bodies)

**Incineration** (for non-recoverable solvent waste):
- Rotary kiln or fixed-hearth incinerator at 800-1,200°C
- Complete combustion: CₓHᵧO₂ + O₂ → CO₂ + H₂O
- Scrubbing required for combustion gases (NOₓ, SO₂ if sulfur present)
- Halogenated solvents (if present) require special incineration with HCl scrubbing — typically sent to permitted hazardous waste incinerators
- Energy recovery: Heat from incineration used for process heating or steam generation

### TMAH (Tetramethylammonium Hydroxide) Waste

TMAH is used as a photoresist developer and silicon etchant. It is highly toxic (LD₅₀ oral rat = 25-32 mg/kg — more toxic than many heavy metals) and causes rapid systemic poisoning through skin absorption:

- **Treatment**: Biological degradation (TMAH-degrading bacteria in sequencing batch reactors) achieving 95-99% removal. Or chemical oxidation (Fenton's reagent: H₂O₂ + Fe²⁺) breaking TMAH into trimethylamine and then further to CO₂ and NH₃.
- **Never discharge untreated** — even diluted TMAH is toxic to aquatic organisms at <10 mg/L
- Spill response: Absorb with inert material, treat as hazardous waste

## Effluent Monitoring

### Continuous Monitoring Parameters

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

### Sampling Protocol

- **Continuous monitoring**: pH, flow, temperature — in-line sensors with data logging (minimum 1 reading per 15 minutes)
- **Daily composite**: 24-hour flow-proportioned composite sample collected by automatic sampler. Analyzed for metals, fluoride, TSS, COD, TOC.
- **Grab samples**: Collected during batch discharges, process upsets, or for parameters that cannot be composited (pH, residual chlorine, hexavalent chromium)
- **Quarterly comprehensive analysis**: Full scan of all metals, semi-volatile organics, and priority pollutants for permit compliance

## Waste Minimization

### Source Reduction Strategies

- **Chemical substitution**: Replace NMP with less toxic alternatives (dibasic ester, propylene carbonate) where process allows
- **Process optimization**: Reduce chemical usage through improved process control — e.g., optimized rinse sequences reduce acid waste volume by 30-50%
- **Extended bath life**: Real-time monitoring of bath chemistry (concentration, dissolved metals) extends the useful life of process baths before disposal
- **Closed-loop recycling**: Reclaim and reuse rinse water (ion exchange + UV/oxidation treatment) — reduces freshwater consumption by 50-80% and wastewater volume proportionally
- **Point-of-use treatment**: Treat waste at the process tool (small volume, high concentration) rather than at end-of-pipe (large volume, diluted) — more efficient chemical usage in treatment

### Waste Segregation

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

---

*Part of the [Bootciv Tech Tree](../index.md) · [EHS](./index.md) · [All Domains](../index.md)*
