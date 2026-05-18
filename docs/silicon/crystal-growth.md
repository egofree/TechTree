# Crystal Growth & Wafering

> **Node ID**: silicon.crystal-growth
> **Domain**: Silicon
> **Timeline**: Years 30-50
> **Outputs**: single_crystal_ingots, wafers, polished_wafers


The CZ puller is the most mechanically demanding piece of equipment in the silicon path. It requires precision motion control, high-temperature furnace, and contamination control.

**Puller construction**:
- **Chamber**: Water-cooled stainless steel vacuum chamber. Diameter 300-600 mm. Viewport for observation. Sealed with Viton or copper gaskets.
- **Crucible**: Fused silica (SiO₂), 200-450 mm diameter, 200-300 mm tall. Supported by graphite susceptor (cylindrical sleeve). Crucible is CONSUMABLE — slowly dissolves into silicon melt (oxygen incorporation into crystal, ~10-20 ppma O). Rotates at 2-15 RPM.
- **Heater**: Graphite resistance heater (cylindrical, slotted for electrical path). Power 20-100 kW. Temperature control ±0.1-0.5°C at ~1420°C (silicon melts at 1414°C).
- **Pull mechanism**: Precision leadscrew + stepper or servo motor. Pull speed 0.5-3 mm/min. Rotation 5-20 RPM. Vibration isolation (concrete block or air-suspended base). Must maintain constant speed within ±0.5%.
- **Atmosphere**: Argon (Ar) at ~10-50 mbar, flowing at 10-30 L/min. Prevents SiO formation and graphite oxidation. Argon from air separation (Chemistry stage fractional distillation of liquid air).
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
---

