# Phase 7: Silicon Production, Crystals, Wafers & Basic Devices ★ EARLY WIN

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

**Process**: Carbothermic reduction of quartz in submerged arc electric furnace.
- **Reaction**: SiO₂ + 2C → Si + 2CO (endothermic, ΔH ≈ +690 kJ/mol)
- **Temperature**: ~1800-2100°C in the reaction zone
- **Raw materials**:
  - **Quartz**: High-purity SiO₂ (>98%). Crushed to 2-10 cm lumps. Impurities (Fe, Al, Ca) become contaminants in product silicon.
  - **Carbon reductant**: Mix of charcoal, coke, and wood chips (provides porosity for gas escape). Coal/coke alone produces dense charge that traps gas.
  - **Typical charge ratio**: ~2 tonnes quartz + 1 tonne carbon → ~1 tonne MG-Si (+ byproducts)
- **Furnace construction**:
  - **Shell**: Steel, 3-8 m diameter, lined with carbon refractory (prebaked carbon blocks or rammed carbon paste).
  - **Electrodes**: 1-3 prebaked graphite electrodes (Søderberg self-baking electrodes possible). Diameter 300-800 mm. Suspended from hydraulic hoists, adjustable height.
  - **Power**: 5-30 MW per furnace. Three-phase AC (for 3-electrode furnace). Voltage 100-250V, current 20,000-100,000 A.
  - **Tapping**: Molten silicon (density 2.33 g/cm³, lighter than slag) tapped from furnace bottom through taphole into cast iron molds or ladle. Tap every 1-4 hours.
- **Energy consumption**: ~11-13 kWh/kg MG-Si (this is enormous — a 1 tonne/day furnace needs ~500 kW continuous).
- **MG-Si purity**: ~97-99% Si. Major impurities: Fe (0.3-0.8%), Al (0.2-0.7%), Ca (0.1-0.5%), Ti, Mn, C. Not pure enough for electronics or efficient solar cells.
- **Crushing**: Break MG-Si ingots to 1-10 cm chunks with jaw crusher, then ball mill to 100-500 μm powder for chemical purification.

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

The CZ puller is the most mechanically demanding piece of equipment in the silicon path. It requires precision motion control, high-temperature furnace, and contamination control.

**Puller construction**:
- **Chamber**: Water-cooled stainless steel vacuum chamber. Diameter 300-600 mm. Viewport for observation. Sealed with Viton or copper gaskets.
- **Crucible**: Fused silica (SiO₂), 200-450 mm diameter, 200-300 mm tall. Supported by graphite susceptor (cylindrical sleeve). Crucible is CONSUMABLE — slowly dissolves into silicon melt (oxygen incorporation into crystal, ~10-20 ppma O). Rotates at 2-15 RPM.
- **Heater**: Graphite resistance heater (cylindrical, slotted for electrical path). Power 20-100 kW. Temperature control ±0.1-0.5°C at ~1420°C (silicon melts at 1414°C).
- **Pull mechanism**: Precision leadscrew + stepper or servo motor. Pull speed 0.5-3 mm/min. Rotation 5-20 RPM. Vibration isolation (concrete block or air-suspended base). Must maintain constant speed within ±0.5%.
- **Atmosphere**: Argon (Ar) at ~10-50 mbar, flowing at 10-30 L/min. Prevents SiO formation and graphite oxidation. Argon from air separation (Phase 5 fractional distillation of liquid air).
- **Seed crystal**: Small single-crystal silicon piece, oriented <100> or <111>. Inserted into melt to initiate growth.

**Growth process**:
1. **Charge**: Load polysilicon chunks into crucible. Add dopant: boron (B, for p-type) or phosphorus (P, for n-type). Typical doping: 10¹⁴-10¹⁶ atoms/cm³ (resistivity 0.1-100 Ω·cm).
2. **Melt**: Evacuate chamber, backfill with Ar. Heat to 1420-1430°C. Polysilicon melts completely (~3-6 hours for 10-30 kg charge).
3. **Seed insertion**: Lower seed crystal until it contacts melt surface. Melt a small amount of seed (establishes liquid-solid interface).
4. **Neck growth**: Pull slowly (3-5 mm/min) to form thin neck (~3 mm diameter). This eliminates dislocations from seed —Dash process. Neck must be 50-100 mm long.
5. **Shoulder growth**: Reduce pull speed, increase diameter to target (100-300 mm). Crown/shoulder region transitions from neck to full diameter.
6. **Body growth**: Maintain pull speed 0.8-1.5 mm/min. Constant rotation (5-15 RPM crucible counter-rotation). Temperature feedback controls diameter. Crystal grows 300-1000 mm long over 12-36 hours.
7. **Tail-out**: Reduce diameter gradually at end of pull to avoid thermal shock dislocations.
8. **Cooling**: Retract crystal into upper chamber. Cool under Ar atmosphere at 2-5°C/min to room temperature (12-24 hours).

**Crystal quality parameters**:
- **Resistivity uniformity**: ±5-10% axial, ±2-5% radial
- **Oxygen content**: 10-20 ppma (from crucible dissolution)
- **Carbon content**: <1 ppma (from heater/atmosphere)
- **Dislocation density**: <100/cm² (ideally zero — Dash process achieves this)
- **Crystal orientation**: Within ±0.5° of target

**Resource consumption per crystal** (typical 150 mm, 15 kg):
- Polysilicon: ~15 kg
- Argon: ~2-5 m³ (flow during growth)
- Electricity: ~200-400 kWh (heater + motors + cooling)
- Quartz crucible: 1 (consumed — partially dissolved)
- Graphite susceptor: lasts ~50-100 pulls before replacement

### Wafer Production

**Slicing (wire saw)**:
- **Equipment**: Wire saw — thin steel wire (140-180 μm diameter) wound on grooved wire guides in a web pattern. Wire travels at 5-15 m/s. Abrasive slurry (SiC or diamond particles 5-20 μm in oil or water-based carrier) fed onto wire.
- **Process**: Ingot mounted on ceramic plate, fed into wire web. Wire tension 15-30 N. Cut time 4-8 hours for 150 mm ingot. Produces 200-400 wafers per ingot.
- **Kerf loss**: ~150-200 μm per wafer (wire + slurry). ~40-50% of silicon lost as kerf.
- **Wafer thickness**: 200-350 μm for solar, 500-775 μm for semiconductor.
- **Alternative**: Inner-diameter (ID) saw — circular blade with diamond-coated inner edge. Cuts one wafer at a time. Slower but simpler. Blade thickness ~200 μm. Good for small-scale or prototype.

**Lapping** (mechanical flattening):
- **Process**: Place wafers on lapping machine (cast iron plate, 300-600 mm diameter). Add abrasive slurry (Al₂O₃ 5-15 μm in water/glycol). Rotate plate and carriers (wafer-holding rings). Remove ~20-50 μm per side. Duration 15-30 minutes.
- **Result**: Flat to ~2-5 μm total thickness variation (TTV). Surface roughness ~0.5-1 μm Ra. No subsurface damage if done correctly.
- **Double-side lapping**: Lap both sides simultaneously for better parallelism.

**Chemical-Mechanical Polishing (CMP)**:
- **Process**: Press wafer (face-down) against rotating polishing pad (polyurethane or felt). Feed polishing slurry: colloidal silica (SiO₂ particles 20-80 nm) in alkaline solution (NaOH or KOH, pH 10-11). Chemical etching + mechanical abrasion synergize.
- **Removal rate**: 0.5-2 μm/min. Remove ~10-30 μm total.
- **Result**: Mirror finish. Surface roughness <0.5 nm Ra. Flat to <1 μm TTV.
- **Post-CMP cleaning**: RCA clean (see below) to remove slurry residue and organic contamination.

**RCA Clean** (standard wafer cleaning sequence):
1. **SC-1 (Standard Clean 1)**: NH₄OH:H₂O₂:H₂O = 1:1:5 at 75-80°C for 10-15 min. Removes organic contaminants and particles. Leaves thin chemical oxide.
2. **DI water rinse**: Overflow rinse, 5-10 min.
3. **HF dip** (optional): Dilute HF (1-2%) for 15-30 seconds. Removes oxide (hydrogen-terminates surface). Skip if oxide desired.
4. **SC-2 (Standard Clean 2)**: HCl:H₂O₂:H₂O = 1:1:6 at 75-80°C for 10-15 min. Removes metallic contaminants (Fe, Au, Cu, Ni).
5. **DI water rinse + spin dry** or **Marangoni dry** (IPA vapor, surface tension gradient pulls water off).

### Basic Semiconductor Devices

#### Solar Cells (Primary Target — simplest useful semiconductor device)

**Structure**: Large-area (100-300 cm²) pn junction on single-crystal or multicrystalline silicon wafer.

**Process flow**:
1. **Starting wafer**: p-type (boron-doped), 1-10 Ω·cm, <100> orientation, 180-300 μm thick. Saw-damage etch in NaOH or KOH (20-40%, 80°C, 2-5 min) to remove ~10-20 μm of damaged surface.
2. **Texturing** (optional, improves light trapping): Anisotropic etch in KOH/IPA solution (2-5% KOH, 5-10% IPA, 70-80°C, 20-30 min). Pyramidal texture on <100> surface reduces reflection from ~35% to ~10%.
3. **Emitter diffusion**: Phosphorus diffusion to form n-type layer. POCl₃ gas in diffusion furnace at 800-900°C for 15-60 min. Target junction depth 0.3-1.0 μm. Sheet resistance 40-80 Ω/sq. Forms n+/p junction.
4. **Phosphorus glass removal**: HF dip (5-10%, 30-60 sec) removes PSG (phosphosilicate glass formed during diffusion).
5. **Anti-reflection coating**: Deposit SiNₓ (silicon nitride) by PECVD at 300-400°C. Thickness ~75 nm (quarter-wave for peak solar wavelength). Also serves as surface passivation.
6. **Metallization — front contacts**: Screen-print silver paste in grid pattern (finger width 50-100 μm, bus bar 1-2 mm). Dry at 150-200°C, fire at 700-800°C (fast ramp, belt furnace, ~30 sec at peak). Ag paste etches through SiNₓ to contact n+ emitter.
7. **Metallization — rear contact**: Screen-print Al paste (full area). Fire simultaneously with front. Al alloys with Si, forms p+ back surface field (BSF) — reduces recombination at rear surface.
8. **Edge isolation**: Laser scribe or plasma etch around wafer edge to prevent front-rear short circuit through junction that wraps around edges.
9. **Testing**: I-V curve under simulated sunlight (AM1.5, 1000 W/m²). Measure Voc, Isc, fill factor, efficiency.

**Expected performance**:
- First cells: 5-10% efficiency (poor passivation, simple contacts)
- Mature process: 15-18% efficiency (screen-printed, BSF, AR coating)
- Advanced: 20%+ (PERC, bifacial — Phase 9)

**Solar cell as energy amplifier**: Each cm² of 15% efficient solar cell produces ~15 mW peak. A 156×156 mm cell produces ~3.6 W peak. Over 20-year lifetime: ~50 kWh per cell. Energy payback time: 1-3 years. The solar cell feedback loop (solar → electricity → more silicon furnaces → more solar cells) is one of the most important positive feedback loops in the entire tech tree.

#### Diodes & Simple Transistors

**Point-contact diode**: Sharpened tungsten or phosphor-bronze wire whisker pressed against n-type silicon crystal. Forms small p-type region at contact point (metal-semiconductor junction). Simple, requires no processing. Used for: rectifiers, radio detectors.

**Alloy junction transistor**: Place indium dots on both sides of thin n-type germanium or silicon wafer (~100-200 μm). Heat to 500-600°C. Indium alloys into semiconductor, creating p-type regions. Result: pnp transistor. Simple but low performance (low frequency, high leakage). Historically important (first transistors, 1950s).

**Diffused transistor**: Phosphorus diffused into p-type wafer through oxide mask window to form base and emitter. More controlled geometry. Requires: oxidation furnace, photolithography (or shadow masking), diffusion furnace. Bridge to Phase 8 planar process.

### Metallization & Contacts

**Vacuum evaporation** (simplest deposition method):
- **Process**: Place metal source (Al, Au, Ti) in tungsten or molybdenum boat or basket in vacuum chamber. Pump to 10⁻⁵ to 10⁻⁶ Torr. Heat source resistively (current through boat) to metal's evaporation temperature (Al: 1200°C, Au: 1500°C). Metal vapor travels in straight lines to substrate. Deposit 0.1-2 μm film.
- **Rate monitoring**: Quartz crystal microbalance — crystal oscillation frequency decreases as metal deposits. Calibrated to thickness.
- **Uniformity**: Source-to-substrate distance 30-50 cm. Rotating planetary fixture for uniform thickness on multiple wafers.
- **Pattern definition**: Shadow mask (thin metal sheet with cutout pattern held against wafer during deposition) or lift-off (pattern photoresist before deposition, dissolve resist after — metal on resist lifts off, leaving patterned metal on wafer).

**Screen printing** (for solar cell contacts):
- Print conductive paste (Ag, Al, or carbon) through mesh screen with patterned emulsion. Squeegee forces paste through open areas onto wafer. Dry and fire. Simpler than evaporation, lower resolution (~50 μm minimum line width).

**Sputtering** (later, more versatile):
- **Process**: Argon plasma bombards target material → atoms ejected → deposit on substrate. Works for any material (metals, insulators, alloys). Better step coverage than evaporation. Requires: RF or DC power supply, vacuum system, target material, argon gas.
- **DC sputtering**: Conductive targets only (metals). 200-1000V, 0.1-10 Torr Ar.
- **RF sputtering**: Any target material (including insulators). 13.56 MHz standard frequency.

## Enables (Downstream)

| Output | Used By |
|--------|---------|
| MG-Si / purified polysilicon | Phase 8 (substrates for all ICs), continued solar cell production |
| Single-crystal wafers | Phase 8 (all IC fabrication — the starting material) |
| Solar cells | Phase 4+ (supplemental power — KEY FEEDBACK LOOP) |
| Basic transistors/diodes | Phase 8 (test structures, early logic, rectifiers) |
| Oxidation/diffusion capability | Phase 8 (core fab processes) |
| Vacuum evaporation | Phase 8 (metallization, contacts) |
| Wafer processing techniques | Phase 8 (CMP, cleaning, etching) |

## The Solar Cell Feedback Loop

```
Solar Cells → supplemental electricity → more power for silicon furnaces → more silicon → more solar cells → more power → ...
```

This positive feedback loop is one of the most important in the entire tech tree. Every kW of solar capacity installed reduces the strain on the primary power system and enables expansion of silicon production. Target: reach self-sustaining solar production (solar cells produce enough power to run their own manufacturing) as early as possible.

## Practical Bottlenecks

- **Quartz crucible quality**: Must be high-purity fused silica — impurities contaminate crystal. Crucibles are consumables (dissolve in molten silicon). Each CZ pull consumes one crucible. Steady crucible production from Phase 6 is essential.
- **Temperature control in CZ puller**: ±0.5°C stability needed for good crystals. PID controller with thermocouple feedback. Power line stability matters — even brief fluctuations cause growth striations.
- **Purity**: Even small impurity levels (ppb) degrade electronic properties. Boron is particularly hard to remove from silicon. Chemical purification (Siemens process) is energy-intensive but necessary for electronic grade.
- **Yield**: First crystals will be small and defective. Expect many iterations. CZ growth is as much art as science — thermal profiles, pull speed, rotation rate all affect quality.
- **Hydrogen for Siemens process**: Electrolysis-derived H₂ must be extremely pure. Moisture or O₂ in H₂ causes oxidation problems.

## Safety Concerns

- **Electric arc furnace**: Extreme heat, UV radiation, CO production. Full face shield, heat-resistant clothing, CO monitoring.
- **HF acid for wafer cleaning**: LETHAL — full protocols required. Calcium gluconate gel on-site. Never work alone with HF.
- **Molten silicon**: ~1415°C — severe burn hazard. Spill containment. Face shield, aluminized apron, gauntlet gloves.
- **Chlorosilane gases** (Siemens process): Flammable (auto-ignite in air at ~100-200°C), corrosive (HCl byproduct), toxic. Leak detection, ventilation, emergency scrubbing system (NaOH solution dump tank). Chlorosilane burns produce HCl + SiO₂ fume.
- **Hydrogen**: Explosion hazard. 4-75% explosive range in air. Ventilate, detect, eliminate ignition sources. Flashback arrestors on all H₂ lines.
- **Phosphine (PH₃), arsine (AsH₃)** — dopant gases: Extremely toxic (TLV 0.05 ppm for AsH₃). Use only with gas cabinets, continuous monitoring, and emergency abort systems. Cylinder change in ventilated enclosure.

## Resource Quantities

| Resource | Per Unit | Notes |
|----------|---------|-------|
| MG-Si energy | ~11-13 kWh/kg | Arc furnace |
| Siemens polysilicon | ~100-200 kWh/kg | Distillation + CVD deposition |
| CZ crystal growth | ~30-50 kWh/kg crystal | Puller heater + Ar + cooling |
| Wafering | ~2-5 kWh/wafer (150 mm) | Wire saw + slurry |
| RCA clean water | ~50-100 L UPW/wafer | Per cleaning cycle |
| Quartz crucible | 1 per pull | Consumable |
| Argon gas | ~10-30 L/min during growth | Continuous flow |

## Side Quest Dependencies

- **[SQ 6: Specialty Gases, Consumables & Packaging](../side-quests/sq-06-gases-packaging-testing.md)** — argon for CZ growth atmosphere, silane and dopant gases for CVD, etch gases for wafer processing. The silicon supply chain cannot operate at any scale without these gases.

[← Phase 6](phase-06-vacuum-optics.md) | [Overview](overview.md) | [Phase 8: Lithography →](phase-08-photolithography.md)
