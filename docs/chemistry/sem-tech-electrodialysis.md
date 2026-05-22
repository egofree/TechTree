# SEM Tech Electrodialysis: Electrochemical Ion Separation

> **Node ID**: chemistry.electrodialysis
> **Domain**: Chemistry
> **Timeline**: Years 20-35
> **Outputs**: separated_ions, desalted_water, concentrated_brine
> **Tags**: materials=[chemicals, polymers], era=industrial

The low-cost ion exchange membranes developed by SEM Tech (see [SEM Tech](sem-tech.md)) enable electrodialysis (ED) as a practical separation technology well before conventional fluoropolymer membranes become available. While SEM Tech's primary application is chlor-alkali electrolysis, the same membrane manufacturing process — pulverizing pre-functionalized resin beads in a PVC/CPVC binder — produces membranes suitable for electrodialysis at less than $1 per square foot.

## Overview

Electrodialysis is an electrochemical separation process that uses ion exchange membranes and an electric field to transport ions from one solution to another. Unlike electrolysis, which drives redox reactions at electrodes to produce new chemical species, electrodialysis performs purely physical ion transport — no chemical reaction occurs at the electrodes beyond minor water splitting at the boundary membranes. The goal is separation, not synthesis.

The Rowow LLC Technical Volume (lines 82-84) describes the discovery of related electro-separation approaches, including electrodialysis and a multi-cell configuration that enables single-stage elemental separation. Combined with the SEM Tech patent's specialized ion resins for selectivity (patent line 105), this positions electrodialysis as a key downstream technology enabled by the SEM Tech membrane platform.

## Electrodialysis Principles

Electrodialysis works by applying a direct current across a stack of alternating cation and anion exchange membranes placed between two electrodes:

- **[Anode](../glossary/anodes.html)** (positively charged electrode): attracts anions (negatively charged ions)
- **[Cathode](../glossary/cathode.html)** (negatively charged electrode): attracts cations (positively charged ions)
- **Cation exchange membranes (CEM)**: permit passage of cations, block anions
- **Anion exchange membranes (AEM)**: permit passage of anions, block cations

When an electric field is applied, cations migrate toward the cathode and anions toward the anode. The alternating membrane stack creates two types of channels: **diluate** channels (where ions are removed, producing purified water) and **concentrate** channels (where ions accumulate, producing brine). Critically, no electrolysis of the feed solution occurs — the ions simply move through the membranes under electrical force.

The only electrode reactions are minor water splitting at the boundary membranes, which produces small amounts of hydrogen and oxygen gas. This means energy consumption is dominated by ion transport, not by electrochemical conversion, making ED inherently more energy-efficient than electrolysis for separation tasks.

## Multi-Cell Configuration

A practical electrodialysis stack consists of many membrane pairs arranged in series between two electrodes:

**Cell pair components** (one repeating unit):
1. Cation exchange membrane (CEM)
2. Diluate channel (feed solution losing ions)
3. Anion exchange membrane (AEM)
4. Concentrate channel (receiving ions)

A commercial stack may contain 100-600 cell pairs. The voltage drop across each pair is small (0.5-1.5V), so the total stack voltage scales linearly with the number of pairs. Current density typically ranges from 10-50 mA/cm² depending on feed concentration and membrane properties.

**Flow configuration**: Diluate and concentrate solutions flow through their respective channels in parallel, typically in a tortuous-path or sheet-flow spacer design. Solutions are recirculated until the desired level of ion removal or concentration is achieved.

**Spacer gaskets**: Thin polymeric mesh spacers (0.5-2mm thick) separate the membranes and create flow channels. These spacers also promote turbulent mixing at the membrane surface, reducing concentration polarization — the buildup of depleted or enriched ion layers that impede transport.

## SEM Tech Membrane in ED

The SEM Tech membrane manufacturing process (see [SEM Tech](sem-tech.md)) produces both membrane types needed for electrodialysis:

**Cation exchange membranes**: Manufactured from strong acid cation resin (sulfonic acid functional groups, R-SO₃H). These are the same resin beads used in SEM Tech chlor-alkali cells. The membrane selectively transports cations (Na⁺, K⁺, Ca²⁺, Mg²⁺, etc.) while blocking anion passage.

**Anion exchange membranes**: Manufactured from strong base anion resin (quaternary ammonium functional groups, R-N⁺(CH₃)₃). The same SEM Tech manufacturing process — pulverize, mix with PVC/CPVC binder, cast, dry — works with anion resin beads to produce anion-selective membranes.

**Specialized selectivity**: The SEM Tech patent describes specialized ion resins that can be tuned for selectivity toward specific ions (patent line 105). For electrodialysis, this enables membranes with preferential transport of target ions — for example, monovalent-selective membranes that pass Na⁺ while blocking Ca²⁺ and Mg²⁺, or proton-selective membranes for acid recovery.

**Speculative status**: While SEM Tech cation membranes have been demonstrated in chlor-alkali cells at TRL 5, complete electrodialysis stacks with matched cation-anion membrane pairs have not yet been built or tested. The theoretical performance is well-established from conventional ED practice, but SEM Tech membrane properties in multi-cell ED configurations (resistance per cell pair, ion selectivity in stacked geometry, long-term fouling behavior) remain to be characterized experimentally.

## Process Variants

### Conventional Electrodialysis (ED)

Standard ED for desalination and ion concentration. Feed solution passes through diluate channels; ions migrate to concentrate channels under applied voltage. Produces desalted water and concentrated brine simultaneously. See [SEM Tech Water Treatment](../water/sem-tech-water-treatment.md) for desalination applications.

Typical performance:
- Salt removal: 50-95% per pass (multiple passes for higher removal)
- Water recovery: 75-90%
- Energy consumption: 0.5-3.0 kWh per cubic meter of product water (feed dependent)

### Reverse Electrodialysis (RED)

Reverse ED generates electricity from the mixing of fresh and salt water — the inverse of conventional ED. Concentrated brine and fresh water flow through alternate channels; the salinity gradient drives ion transport through the membranes, generating electrical current. This is salinity-gradient power, also called **[blue energy](../energy/sem-tech-blue-energy.md)**. See [SEM Tech Blue Energy](../energy/sem-tech-blue-energy.md).

RED viability depends critically on membrane cost, since large membrane areas are needed for modest power output. SEM Tech membranes at less than $1/sq ft could make RED economically feasible for the first time.

### Bipolar Membrane Electrodialysis (BMED)

Bipolar membranes consist of a cation exchange layer bonded to an anion exchange layer. Under applied voltage, water splits at the junction into H⁺ and OH⁻ ions. In a BMED stack, this produces acid and base from their corresponding salts without electrolysis:

- NaCl + H₂O → HCl + NaOH
- Na₂SO₄ + 2H₂O → H₂SO₄ + 2NaOH

This is directly relevant to [SEM Tech Acid Regeneration](sem-tech-acid-regeneration.md), where spent acid streams are reconcentrated for reuse. BMED eliminates the need for electrode-driven electrolysis in acid-base production.

## Operating Parameters

| Parameter | Conventional ED | RED | BMED |
|-----------|----------------|-----|------|
| **Voltage per cell pair** | 0.5-1.5V | N/A (generates voltage) | 1.0-3.0V |
| **Current density** | 10-50 mA/cm² | 1-10 mA/cm² | 10-50 mA/cm² |
| **Feed TDS** | 1,000-10,000 mg/L | Seawater + fresh | Salt solutions |
| **[Temperature](../glossary/temperature.html)** | 20-40°C | 15-30°C | 25-45°C |
| **Flow velocity** | 5-15 cm/s | 1-5 cm/s | 5-10 cm/s |
| **Recovery rate** | 75-90% | N/A | 80-95% |
| **Energy (ED)** | 0.5-3.0 kWh/m³ | Generates 0.5-2.0 W/m² | 1.0-5.0 kWh/kg acid |

**Key operating considerations**:
- **Concentration polarization**: At high current densities, ion depletion at the membrane surface limits transport. Spacer design and flow velocity manage this effect.
- **Scaling**: Divalent ions (Ca²⁺, Mg²⁺) can precipitate as carbonates or hydroxides on membrane surfaces. Pre-treatment or periodic polarity reversal (electrodialysis reversal, EDR) mitigates scaling.
- **Membrane fouling**: Organic matter and colloids foul membranes over time. Cleaning-in-place (CIP) with acid and alkali solutions restores performance.

## Applications

**Desalination**: Brackish water desalination is the largest commercial ED application. ED excels at moderate salinity (1,000-10,000 mg/L TDS) where reverse osmosis becomes energy-intensive. See [SEM Tech Water Treatment](../water/sem-tech-water-treatment.md).

**Acid and base production**: BMED converts salt solutions into their constituent acids and bases. Useful for regenerating spent pickling acids, producing organic acids, and generating NaOH without chlor-alkali electrolysis. See [SEM Tech Acid Regeneration](sem-tech-acid-regeneration.md).

**Metal recovery**: ED concentrates metal ions from dilute waste streams (electroplating rinse water, mining leachate) for recovery by electrowinning or precipitation. Selective membranes enable separation of mixed metal streams.

**Food processing**: Demineralization of whey, deacidification of fruit juices, salt removal from soy sauce. ED preserves flavor compounds that thermal processes would destroy.

**Blue energy**: Reverse ED generates electricity from river-sea water mixing at estuaries. Global theoretical potential exceeds 2 TW. See [SEM Tech Blue Energy](../energy/sem-tech-blue-energy.md).

## Safety

- **Electrical safety**: ED stacks operate at high DC voltages (50-600V depending on cell pairs). Proper grounding, insulation, and lockout/tagout procedures are mandatory. Current leakage through improperly sealed cells can cause electrolysis and gas generation.
- **Chemical handling**: Concentrate streams may contain high concentrations of acids, bases, or salts. Standard chemical handling PPE (goggles, gloves, aprons) required when handling concentrate solutions.
- **Acid/base exposure**: BMED produces concentrated acid and base streams simultaneously. Cross-contamination from leaking membranes can cause vigorous neutralization reactions with heat generation. Pressure monitoring on product streams detects membrane failures.
- **Hydrogen gas**: Minor hydrogen evolution occurs at the cathode. Ensure adequate ventilation in enclosed stack installations to prevent flammable gas accumulation.
- **Membrane degradation**: Degraded membranes can release resin particles or binder material into product streams. Monitor product water quality with conductivity sensors.

## Limitations

**Speculative technology status**: SEM Tech membranes have been validated for chlor-alkali electrolysis (TRL 5), but full electrodialysis stacks using SEM Tech membranes have not been demonstrated. Key unknowns: membrane resistance in thin multi-cell stacks, long-term ion selectivity under continuous ED operation, fouling and cleaning behavior, and matched performance between cation and anion SEM Tech membranes.

**Not suitable for high-TDS feeds**: Conventional ED becomes uneconomical for seawater desalination (>35,000 mg/L TDS) because resistive losses increase with concentration. Reverse osmosis is preferred for seawater; ED excels at brackish water.

**Membrane replacement cost**: Although SEM Tech membranes are inexpensive, large ED stacks require hundreds of square meters. Membrane lifetime in ED service (months to years) determines operating cost.

**Divalent ion limitations**: Standard ion exchange membranes do not distinguish well between monovalent and divalent ions. Selective membranes (monovalent-selective) add complexity and cost, though SEM Tech's tunable resin approach may address this.

**No non-ionic contaminant removal**: ED removes only charged species. Suspended solids, organic molecules, and microorganisms pass through the channels unchanged. Pre-treatment (filtration, activated carbon) is needed for complete water purification.

## See Also

- [SEM Tech Ion Exchange Membrane](sem-tech.md) — parent article on SEM Tech membrane manufacturing and properties
- [Water Treatment](../water/sem-tech-water-treatment.md) — desalination and water purification applications
- [Acid Regeneration](sem-tech-acid-regeneration.md) — acid-base recovery via bipolar membrane electrodialysis
- [Blue Energy](../energy/sem-tech-blue-energy.md) — reverse electrodialysis for salinity-gradient power generation

---

*Part of the [Bootciv Tech Tree](../index.md) | [Chemistry](./index.md) | [All Domains](../index.md)*
