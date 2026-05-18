# Silicon Purification

> **Node ID**: silicon.purification
> **Domain**: Silicon
> **Timeline**: Years 30-50
> **Outputs**: purified_silicon, polysilicon, chlorosilanes

### Purification Pathways

#### Option A: Chemical Purification (Siemens-like Process)

This is the standard industrial route to semiconductor-grade polysilicon (99.9999999%+ purity).

**Step 1: Hydrochlorination** — Convert MG-Si powder to trichlorosilane:
- **Reaction**: Si + 3HCl → SiHCl₃ + H₂ (exothermic, ~300°C, Cu catalyst). Also produces SiCl₄, SiH₂Cl₂ as byproducts.
- **Equipment**: Fluidized bed reactor (Si powder suspended in HCl/H₂ gas stream). Copper catalyst (~1% Cu in Si powder). Temperature 280-350°C. Pressure 1-5 bar.
- **Product**: Mixed chlorosilane gases + H₂. Condense at -30 to 0°C to separate liquid chlorosilanes from H₂ gas.

**Step 2: Fractional distillation** — Purify SiHCl₃:
- **Principle**: SiHCl₃ boils at 31.8°C, SiCl₄ at 57.6°C, SiH₂Cl₂ at 8.2°C. Multiple distillation columns separate these. Purity requirement: impurities <1 ppb for electronic grade.
- **Columns**: 10-30 m tall, packed with structured packing or sieve trays. Reflux ratio 10-50:1. Multiple columns in series for progressive purification.
- **Key separations**: Remove boron (BCl₃, bp 12.5°C — very close to SiHCl₃, requires many theoretical plates), phosphorus (PCl₃, bp 76°C), metal chlorides.
- **Number of distillation passes**: 2-5 for solar grade, 5-10+ for electronic grade.

**Step 3: Chemical vapor deposition (CVD)** — Decompose purified SiHCl₃ on heated silicon rods:
- **Reaction**: SiHCl₃ + H₂ → Si (solid) + 3HCl (gas). Temperature 1050-1150°C.
- **Reactor**: Bell jar (quartz or stainless steel) containing inverted-U silicon seed rods (~5 mm diameter). Resistance-heated to ~1100°C by passing current through rods (rods are conductive when hot). H₂ + SiHCl₃ gas flows around rods.
- **Deposition rate**: ~5-10 μm/min. Rods grow from 5 mm to 100-200 mm diameter over 50-100 hours. Final rods weigh 50-200 kg each.
- **Energy**: ~100-200 kWh/kg polysilicon (electricity for heating + H₂ production).
- **Purity**: 9N-11N (99.9999999% - 99.999999999% Si). Electronic grade.

#### Option B: Physical Purification (Zone Refining / Directional Solidification)

Lower purity than Siemens, but much simpler chemistry. Sufficient for solar cells (~5-7N).

**Directional solidification**:
- **Principle**: Impurities preferentially stay in liquid phase. Slowly cool silicon melt from one end → impurities segregate to last-to-freeze region (Segregation coefficient k < 1 for most impurities in Si). Cut off and discard impure tail.
- **Process**: Melt MG-Si in coated quartz or graphite crucible. Cool from bottom at ~1 cm/hour. Total time 10-30 hours depending on ingot size. Ingot diameter 150-300 mm.
- **Effective segregation coefficients**: B: 0.8 (hard to remove — close to 1), P: 0.35, Al: 0.002, Fe: 6.4×10⁻⁶ (easy to remove). Boron is the problematic impurity — it barely segregates.
- **Result**: Solar-grade silicon (~5-6N). Multiple passes improve purity. Not sufficient for electronic devices.

**Zone refining** (for highest purity physical route):
- **Process**: Pass molten zone (narrow band of liquid) along solid silicon rod, repeatedly. Each pass sweeps impurities toward one end. 10-20 passes achieve ~8-9N purity.
- **Equipment**: RF induction coil or focused IR lamp creates moving molten zone. Rod rotates slowly. Under inert atmosphere (Ar) or vacuum. Very slow — ~1-5 cm/hour travel speed.
- **Limitation**: Still cannot remove boron effectively (k ≈ 0.8). Combine with another boron removal step (slag treatment: add CaO-Na₂O flux to molten Si, B partitions into slag).

### Czochralski (CZ) Crystal Growth

See [Crystal Growth & Wafering](crystal-growth.md) for CZ pulling details.
