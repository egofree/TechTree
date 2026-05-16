# Phase 7: Silicon Production, Crystals, Wafers &amp; Basic Devices ★ EARLY WIN

**Timeline**: Years 30–50  
**Goal**: Usable silicon and simple semiconductor devices. Solar cells first — they are far simpler than logic chips.  
**Dependencies**: [Phase 3](phase-03-machine-tools.md) (puller mechanics, saws), [Phase 4](phase-04-energy.md) (electric arc furnace), [Phase 5](phase-05-chemistry.md) (etchants, cleaning), [Phase 6](phase-06-vacuum-optics.md) (crucibles, inspection)

## Objectives

- Produce metallurgical-grade silicon (MG-Si)
- Purify to solar-grade or better
- Grow single crystals via Czochralski method
- Slice, lap, and polish wafers
- Fabricate basic solar cells and simple semiconductor devices

## Key Technologies

### Metallurgical-Grade Silicon (MG-Si) Production
- **Process**: Quartz (SiO₂) + carbon (charcoal/coke) in submerged arc electric furnace (~2000°C)
- **Reaction**: SiO₂ + 2C → Si + 2CO
- **Carbon electrodes**: Graphite from pitch + carbon, or early electrode production
- **Purity**: ~98-99% Si (metallurgical grade — not pure enough for electronics yet)
- **Energy requirement**: ~11-13 kWh/kg — significant power draw

### Purification Pathways

#### Option A: Chemical Purification (Siemens-like Process)
- React MG-Si with HCl → trichlorosilane (SiHCl₃)
- Fractional distillation of chlorosilanes (multiple passes for purity)
- Decompose purified SiHCl₃ on heated silicon rods → polycrystalline silicon
- **Pros**: Very high purity achievable
- **Cons**: Complex chemical engineering, corrosion-resistant equipment, hazardous gases

#### Option B: Physical Purification (Zone Refining / Directional Solidification)
- Directional solidification: slowly cool melt → impurities segregate to one end
- Zone refining: pass molten zone along silicon rod → sweep impurities
- **Pros**: Less complex chemistry, works for solar-grade
- **Cons**: Slower, may not reach electronic-grade alone

### Czochralski (CZ) Crystal Growth
- Melt polycrystalline Si in **fused quartz crucible** (from Phase 6)
- **Graphite resistance heater** for temperature control (~1415°C, just above Si melting point)
- Dip **oriented seed crystal** into melt
- Pull upward while rotating — slow, steady withdrawal grows single crystal
- **Atmosphere control**: Argon (or nitrogen) inert gas to prevent oxidation
- **Mechanical requirements**: Precision pull mechanism (from machine shop), vibration isolation, smooth rotation
- Temperature gradient control critical for defect-free crystal

### Wafer Production
- **Slicing**: Wire saws with abrasive slurry (SiC or diamond particles)
  - Multiple wires cut many wafers simultaneously
- **Lapping**: Mechanical flattening with abrasive compounds
- **Chemical-Mechanical Polishing (CMP)**: Final mirror finish
  - Slurry of fine abrasive (silica, alumina) + chemical etchant
- **Cleaning**: Sequential acid cleans (RCA clean — NH₄OH/H₂O₂, HCl/H₂O₂, HF dip)

### Basic Semiconductor Devices

#### Solar Cells (Primary Target)
- **Structure**: Large-area pn junction
- **Process**: Base wafer (p-type, boron-doped) → phosphorus diffusion for n-type layer → contacts (screen-printed or evaporated aluminum/silver) → anti-reflection coating (TiO₂ or SiNₓ)
- **Efficiency**: First cells may be 5-15% — still extremely valuable for power generation
- **Value**: Power feedback into the energy system — accelerates everything

#### Diodes &amp; Simple Transistors
- Point-contact or alloy junction transistors
- Simple diffusion-formed pn junctions
- Useful for: rectifiers, basic amplifiers, test circuits

### Metallization &amp; Contacts
- **Evaporation**: Heat metal (aluminum, gold) in vacuum → condenses on wafer
  - Requires vacuum chamber (Phase 6) and resistive or e-beam heating
- **Screen printing**: Simpler, for solar cell contacts — paste through patterned screen
- **Sputtering** (later): Ion bombardment of target → metal atoms deposit on wafer

## Enables (Downstream)

| Output | Used By |
|--------|---------|
| MG-Si / purified Si | Phase 8 (substrates for ICs) |
| Single-crystal wafers | Phase 8 (all IC fabrication) |
| Solar cells | Phase 4 (supplemental power — KEY FEEDBACK) |
| Basic transistors/diodes | Phase 8 (test structures, early logic) |
| Oxidation/diffusion capability | Phase 8 (core fab processes) |
| Vacuum evaporation | Phase 8 (metallization) |

## The Solar Cell Feedback Loop

```
Solar Cells → supplemental electricity → more power for silicon furnaces → more silicon → more solar cells → more power → ...
```

This positive feedback loop is one of the most important in the entire tech tree.

## Practical Bottlenecks

- **Quartz crucible quality**: Must be high-purity fused silica — impurities contaminate crystal
- **Temperature control in CZ puller**: ±0.5°C stability needed for good crystals
- **Purity**: Even small impurity levels (ppb) degrade electronic properties
- **Yield**: First crystals will be small and defective — expect many iterations

## Safety Concerns

- Electric arc furnace: extreme heat, UV, CO production
- HF acid for wafer cleaning: LETHAL — full protocols required
- Molten silicon: ~1415°C — severe burn hazard
- Chlorosilane gases (if chemical purification): flammable, corrosive, toxic

[← Phase 6](phase-06-vacuum-optics.md) | [Overview](overview.md) | [Phase 8: Lithography →](phase-08-photolithography.md)
