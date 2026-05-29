# Anodizing

> **Node ID**: electrochemistry.anodizing
> **Domain**: [Electrochemistry & Plating](./index.md)
> **Dependencies**: [`chemistry.acids`](../chemistry/acids.md), [`metals.aluminum`](../metals/aluminum.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 25-60
> **Outputs**: anodized_aluminum, hard_anodized_surfaces, anodized_titanium, oxide_coatings
> **Critical**: No — anodizing produces durable oxide coatings for semiconductor equipment but alternative surface treatments exist

### Overview

Anodizing is an electrochemical oxidation process that converts a metal surface into a durable, controlled oxide layer. Unlike electroplating (which deposits metal onto a surface from an external source), anodizing grows the oxide from the substrate itself — the coating is integral to the metal and cannot peel, chip, or delaminate. The workpiece is the anode (hence "anodizing") in an electrolytic cell, and oxygen generated at the anode reacts with the metal to form a dense oxide.

For semiconductor manufacturing, anodizing serves two critical roles: (1) producing aluminum components with hard, corrosion-resistant oxide surfaces for process chamber internals, wafer carriers, and robotic end-effectors, and (2) titanium anodizing for voltage-controlled oxide thickness in specialty applications including medical implants and aerospace fasteners. The porous anodic aluminum oxide (AAO) membrane is also a template material for nanowire and nanotube fabrication.

The fundamental physics of anodizing differs from plating. In plating, metal cations in solution are reduced at the cathode to form the deposit. In anodizing, the metal itself is oxidized at the anode, consuming the substrate to build the oxide. The oxide thickness is proportional to the applied voltage (1.2-1.4 nm/V for aluminum barrier oxide), giving precise control over coating properties.

### Aluminum Anodizing — Type II (Sulfuric Acid)

Type II sulfuric acid anodizing is the most common anodizing process, producing 5-30 μm of porous aluminum oxide. The porous structure readily absorbs dyes for coloring and can be sealed for improved corrosion resistance.

**Bath composition and operating conditions**:
- **Electrolyte**: 150-200 g/L H₂SO₄ (sulfuric acid) in deionized water. Specific gravity 1.10-1.15.
- **Temperature**: 20-22°C (±1°C). Higher temperature increases oxide dissolution rate, producing softer, more porous coatings. Lower temperature produces harder, denser coatings but requires more voltage for the same current density.
- **Voltage**: 12-22 V DC (constant voltage mode). Ramp from 0V to set voltage over 30-60 seconds to prevent burning (thermal runaway at high initial current). Current density at steady state: 10-20 mA/cm² (approximately 1.0-2.0 A/dm² or 10-20 A/ft²).
- **Anode**: The aluminum workpiece.
- **Cathode**: Lead or aluminum alloy plates (inert — not consumed). Cathode-to-anode area ratio ≥2:1 for uniform current distribution.
- **Agitation**: Compressed air or mechanical stirring to maintain uniform temperature and remove hydrogen bubbles from cathode surface.
- **Time**: 20-60 minutes depending on desired coating thickness. Coating growth rate: approximately 0.4-0.6 μm/minute at 15 mA/cm².

**Oxide structure**:
- The anodic oxide has a unique hexagonal cell structure, each cell containing a central pore perpendicular to the surface. Pore diameter: 10-30 nm depending on electrolyte and voltage. Cell wall thickness: approximately equal to pore diameter.
- **Barrier layer**: A thin, dense, non-porous Al₂O₃ layer at the metal-oxide interface. Thickness: 1.0-1.4 nm per volt of applied potential (the "anodizing ratio"). At 15V: barrier layer ~18 nm. The barrier layer is an electrical insulator (dielectric strength ~10 V/μm) and is responsible for the dielectric properties of the anodic coating.
- **Porous layer**: Above the barrier layer, the oxide is porous (10-15% porosity by volume). The pores form because the sulfate electrolyte dissolves the oxide at the pore tips, establishing a steady-state balance between oxide growth at the barrier layer and oxide dissolution at the pore tips. The equilibrium thickness depends on voltage, temperature, and time.

**Dyeing and sealing**:
- The porous structure absorbs organic and inorganic dyes before sealing. Dye absorption: 0.5-5 minutes at 50-60°C in dye solution (1-10 g/L). Common colors: black, red, blue, green, gold, and combinations.
- **Sealing** converts the porous Al₂O₃ to boehmite (AlO(OH)) by hydration: Al₂O₃ + H₂O → 2AlO(OH). Boehmite occupies 33% more volume than Al₂O₃, swelling to close the pores and trap the dye.
  - Hot water seal: 95-100°C deionized water, pH 5.5-6.5, 2-3 minutes per μm of coating thickness. Simplest method, no chemicals added.
  - Nickel acetate seal: 5 g/L Ni(CH₃COO)₂ at 85-95°C, pH 5.5-6.0. Nickel ions fill residual pores, improving seal quality and corrosion resistance. Provides a slight greenish tint to clear coatings.
  - Mid-temperature seal: 80-85°C with proprietary additives. Faster than hot water, less smut (sealing bloom).

**Coating properties**:
- Hardness: 200-400 HV (Vickers). Softer than Type III due to higher porosity.
- Dielectric strength: 15-30 V/μm (breakdown voltage 200-600V for typical coatings).
- Corrosion resistance: 200-500+ hours salt spray (ASTM B117) when sealed. Unsealed: <24 hours.
- Maximum service temperature: 200°C (above this, the sealed coating dehydrates and loses corrosion resistance).

### Aluminum Anodizing — Type III (Hard Anodizing)

Hard anodizing produces a thick, dense, wear-resistant aluminum oxide coating (25-100 μm) by operating at low temperature and higher voltage. The coating is significantly harder and more abrasion-resistant than Type II.

**Bath composition and operating conditions**:
- **Electrolyte**: 150-250 g/L H₂SO₄ (higher concentration than Type II for better conductivity at low temperature).
- **Temperature**: -1 to +5°C (refrigerated bath). The low temperature suppresses the acid dissolution of the oxide, allowing thicker buildup. Cooling capacity: 1-2 kW per m² of anodizing area. Titanium heat exchangers or lead-lined cooling coils.
- **Voltage**: 25-75 V DC. Voltage is ramped from ~5V to final voltage over 5-15 minutes to control heat generation. At high voltage, the high current (30-40 mA/cm²) generates substantial heat: P = V × I = 50V × 0.035 A/cm² = 1.75 W/cm². This heat must be removed by the chilled electrolyte to prevent burning.
- **Current density**: 25-40 mA/cm² (2.5-4.0 A/dm²). Higher current density produces harder coatings but increases burning risk.
- **Time**: 30-120 minutes. Growth rate: approximately 0.5-1.0 μm/minute at 30 mA/cm².
- **Additives**: Oxalic acid (5-15 g/L) may be added to suppress burning at high voltage. Oxalate anions adsorb at high-current-density sites, locally reducing current density and preventing thermal runaway.

**Coating properties**:
- Hardness: 400-600 HV (up to 700 HV on select 6000-series alloys). Significantly harder than Type II. Wear resistance: 10-50× untreated aluminum.
- Thickness: 25-100 μm. Thicker coatings (>75 μm) may develop microcracking due to high internal compressive stress.
- Color: Dark gray to bronze/brown depending on alloy and thickness. Cannot be dyed as effectively as Type II due to smaller pore diameter.
- Surface finish: Coating replicates the substrate finish but with a slight texture increase (1-2 μm Ra roughness addition). Precision-ground or lapped surfaces should be finished to one grade better than the final requirement.

**Alloy effects on anodizing quality**:
- **5000-series** (Al-Mg): Excellent anodizing response. Clear, bright oxide. Best for architectural and marine applications.
- **6000-series** (Al-Mg-Si): Good anodizing response. Most common alloy for hard-anodized engineering components (6061-T6, 6082-T6).
- **7000-series** (Al-Zn): Intermediate response. Hard anodizing possible but coating is less uniform.
- **2000-series** (Al-Cu): Poor anodizing response. Copper particles cause soft, dark, non-uniform coatings. Not recommended for Type III. Alloy 2024 can be hard anodized with special procedures (low temperature, reduced current density) but coating quality is inferior.
- **Cast alloys** (Al-Si): Silicon particles appear as dark spots in the anodized coating. High-silicon casting alloys (A356, 356) produce visibly mottled coatings.

### Titanium Anodizing

Titanium anodizing produces a thin oxide layer (TiO₂) whose thickness is precisely controlled by the applied voltage. Unlike aluminum anodizing, the titanium oxide is non-porous (barrier-type) and thin (typically <200 nm). The optical interference of the thin oxide layer produces vivid colors without dyes.

**Type II titanium anodizing** (color anodizing):
- **Electrolyte**: Trisodium phosphate (TSP, Na₃PO₄) 30-50 g/L, or phosphoric acid (H₃PO₄) 30-50 g/L, or ammonium bifluoride (NH₄HF₂) 30-50 g/L in deionized water.
- **Temperature**: 20-30°C. **Voltage**: 15-110 V DC (voltage determines color). No current density control needed — the oxide is a barrier layer that self-limits thickness.
- **Time**: 5-30 seconds (very fast — oxide grows to equilibrium thickness almost instantly at each voltage step).

**Voltage-color relationship**:
| Voltage | Color | Oxide Thickness (approx.) |
|---------|-------|--------------------------|
| 15-20 V | Light bronze | 30-40 nm |
| 25-30 V | Tan / gold | 50-60 nm |
| 35-40 V | Purple / magenta | 70-80 nm |
| 45-55 V | Blue | 90-110 nm |
| 60-70 V | Light blue / sky blue | 120-140 nm |
| 75-85 V | Greenish yellow | 150-170 nm |
| 90-100 V | Pink / rose gold | 180-200 nm |
| 105-110 V | Teal | 210-220 nm |

The colors result from thin-film optical interference — light reflected from the oxide surface and the metal-oxide interface constructively and destructively interfere at different wavelengths depending on oxide thickness. The oxide grows at 1.5-2.0 nm/V.

**Type III titanium anodizing** (wear-resistant):
- **Electrolyte**: Phosphoric acid (H₃PO₄) 200-300 g/L or mixed acid (H₂SO₄ + H₃PO₄).
- **Temperature**: 0-10°C. **Voltage**: 80-200 V DC.
- **Current density**: 20-50 mA/cm² initially, decreasing as oxide thickens.
- Produces a thick, abrasion-resistant TiO₂ layer (1-5 μm). Hardness: 500-800 HV.
- Applications: Medical implants (orthopedic, dental — TiO₂ is biocompatible and promotes osseointegration), aerospace fasteners, chemical process equipment.

### Porous Anodic Aluminum Oxide (AAO) Templates

A specialized application of aluminum anodizing produces highly ordered nanopore arrays used as templates for nanowire and nanotube fabrication. Two-step anodizing in oxalic acid (0.3 M, 40V, 5°C) produces hexagonally close-packed pores with 50-200 nm diameter and 20-500 nm pitch, extending through membranes up to 100 μm thick. The AAO membrane serves as a template for electrodepositing metal nanowires (Cu, Ni, Au, Fe) by filling the pores from one side. After deposition, the aluminum substrate and oxide are dissolved, releasing free-standing nanowires. Applications: magnetic storage media, sensors, catalysis supports, and nanostructured electrodes for batteries.

### Process Control

**Voltage-current monitoring**: The anodizing voltage-current curve indicates coating quality. In constant-voltage mode, the current should decrease gradually as the oxide thickens (increasing resistance). A sudden current spike indicates burning (thermal runaway). In constant-current mode, the voltage should increase gradually. A voltage plateau or decrease indicates excessive dissolution or poor contact.

**Coating thickness measurement**:
- Eddy current thickness gauge: non-destructive, measures oxide thickness on aluminum to ±1 μm. Standard production tool.
- Cross-section microscopy: destructive, most accurate. Samples are mounted, polished, and measured under optical or SEM microscopy. Used for process qualification.
- Weight gain method: Weigh before and after anodizing. Coating weight (mg/dm²) correlates with thickness. Assumes known oxide density (Al₂O₃: 3.95 g/cm³ for barrier, 2.5-3.0 g/cm³ for porous).

**Seal quality testing**:
- Dye spot test: Apply a dye solution (anthraquinone-based) to the sealed surface for 5 minutes, rinse, and visually inspect. Any visible dye absorption indicates incomplete sealing.
- Admittance test: Measures electrical admittance of the sealed coating at 1 kHz. Lower admittance = better seal. Standard: ISO 2931.

### Dimensional Considerations

Anodizing changes the part dimensions because the aluminum oxide occupies more volume than the aluminum consumed. The Pilling-Bedworth ratio for Al₂O₃/Al is approximately 1.6 — meaning 1 volume unit of aluminum converts to 1.6 volume units of oxide. However, the oxide grows both inward (consuming aluminum) and outward (building above the original surface):

- **Inward growth**: Approximately 50-60% of the coating thickness is below the original surface.
- **Outward growth**: The remaining 40-50% extends above the original surface.
- For a 25 μm Type II coating: ~13 μm grows inward (removed from the aluminum substrate), ~12 μm grows outward (above original surface). The net dimensional increase on each surface is ~12 μm. This must be accounted for in tolerance stack-ups.
- For a 50 μm Type III hard coat: ~26 μm inward, ~24 μm outward. Net increase: ~24 μm per surface.

**Pre-anodize machining tolerances**: Parts must be machined undersize by the expected outward growth. For Type II (25 μm): machine 12 μm undersize per surface. For Type III (50 μm): machine 24 μm undersize per surface. Threads and close-tolerance fits require particular attention — the oxide on thread flanks changes the effective pitch diameter.

### Color Matching and Quality Control

**Dye color consistency**: Achieving consistent color across batches requires controlling:
- Coating thickness (±2 μm): Thicker coatings absorb more dye, appearing darker. Controlled by anodizing time and current.
- Dye concentration (±5%): Measured by spectrophotometer. Replenished based on work throughput.
- Dye temperature (±1°C): Higher temperature increases absorption rate.
- Dye pH (±0.2): Affects dye molecule charge and adsorption on the oxide surface.
- Sealing time and temperature: Affects how much dye is retained in the pores after sealing.

**Color measurement**: Spectrophotometer (CIE L*a*b* color space) measures color coordinates. Tolerance: ΔE <2.0 for most applications, ΔE <1.0 for automotive trim. L* = lightness (0=black, 100=white), a* = red/green axis, b* = yellow/blue axis.

### Anodizing in Semiconductor Manufacturing

Anodizing serves several specific functions in semiconductor equipment fabrication:

**Process chamber components**:
- Aluminum (6061-T6 or 6082-T6) etch chamber bodies are Type III hard anodized for plasma resistance. The Al₂O₃ surface resists attack by chlorine-based (Cl₂, BCl₃, HBr) and fluorine-based (CF₄, SF₆, NF₃) plasmas used in silicon etching. Unprotected aluminum would be rapidly etched, contaminating the wafer with aluminum particles and altering the chamber geometry.
- Anodized aluminum wafer carriers (200 mm and 300 mm) and robotic end-effectors provide a hard, non-contaminating surface for wafer handling. Surface roughness Ra <0.5 μm prevents particle generation during wafer transport.

**Anodic bonding** (silicon-glass wafer bonding):
- A specialized anodizing process bonds a silicon wafer to a borosilicate glass wafer (Pyrex 7740 or Schott Borofloat) at 300-450°C and 500-1000 V DC. The glass wafer is the anode. Sodium ions (Na⁺) in the glass migrate toward the cathode, creating a depleted zone at the silicon-glass interface. The resulting electrostatic force and chemical bonding create a hermetic seal. Used for MEMS packaging, pressure sensors, and solar cells.

**Porous AAO for nanostructure templates**:
- Two-step anodizing in oxalic acid (0.3 M, 40 V, 5°C) produces highly ordered hexagonal pore arrays:
  - Step 1: Anodize for 12-24 hours to develop long-range pore ordering. Dissolve the oxide in chromic-phosphoric acid (H₃PO₄ 6% + H₂CrO₄ 1.8%, 60°C, 2-4 hours).
  - Step 2: Re-anodize under identical conditions. The pre-textured aluminum surface produces a perfectly ordered pore array with <5% defect density.
  - Pore diameter: 50 nm (40V oxalic acid). Pore pitch: 100 nm. Pore depth: up to 100 μm (aspect ratio >1000:1).
- AAO membranes are used as templates for electrodeposition of nanowires (Cu, Ni, Au, Fe, Co), nanotubes (TiO₂, ZnO), and polymer nanostructures. After deposition, the aluminum substrate and oxide are dissolved (NaOH or H₃PO₄), releasing the nanostructures.

### Anodizing Equipment

**DC power supply**:
- Silicon diode or thyristor rectifier with constant-voltage (CV) or constant-current (CC) mode. CV mode is standard for Type II anodizing (set voltage, current varies as oxide grows). CC mode is standard for Type III hard anodizing (set current, voltage increases as oxide grows — prevents burning during the critical initial phase).
- Ripple: <5% AC ripple on DC output. Excessive ripple causes periodic current reversals that degrade oxide structure.
- Voltage range: 0-30V for Type II, 0-100V for Type III. Current capacity: 500-10,000 A depending on production scale (typical: 1-5 A/dm² × total workpiece area).
- Ramp control: Programmable voltage ramp (0→set voltage over 1-15 minutes) essential for Type III to prevent burning.

**Cooling system** (critical for Type III):
- Refrigeration: 5-20 kW chiller capacity per 1000 L of bath volume. Titanium or lead-lined heat exchangers (H₂SO₄ attacks copper and most metals). Bath temperature must be maintained within ±2°C during operation despite heat generation from the anodizing current.
- Heat generation: P = V × I × (1 - η), where η is the fraction of energy stored in the oxide (very small). At 50V and 3 A/dm² on 10 dm²: P = 50 × 30 = 1500 W. This heat must be continuously removed.

**Racking and fixturing**:
- Aluminum or titanium racks with spring-loaded contacts. The rack material must be the same alloy family as the workpiece (or titanium, which anodizes to a thin insulating oxide that prevents unwanted plating). Contact points leave small marks on the finished part — position contacts on non-visible or non-critical surfaces.
- Tank material: Polypropylene, PVDF-lined steel, or lead-lined steel. H₂SO₄ attacks most metals — stainless steel is not suitable for long-term anodizing tank use.

### Alloy-Specific Procedures

**Anodizing 6061-T6 aluminum** (most common engineering alloy):
- Pre-treatment: Alkaline clean (NaOH 5-10%, 50-60°C, 5-10 min) → rinse → deoxidize (Na₂SO₄ + H₂SO₄ or HNO₃ dip, 1-3 min) → rinse → anodize.
- Type II: 15-20V, 20°C, 15 mA/cm², 30-45 min → dye (if required) → seal. Coating: 15-25 μm, 200-300 HV.
- Type III: Ramp to 50V over 10 min, then hold at 50V, 0-2°C, 35 mA/cm², 60 min → seal in nickel acetate. Coating: 40-60 μm, 400-550 HV.

**Anodizing 7075-T6 aluminum** (high-strength aerospace alloy):
- The zinc content (5.1-6.1%) produces a slightly darker, less transparent oxide than 6000-series alloys. Type III hardness: 350-500 HV (lower than 6061 due to zinc interference with oxide growth).
- Pre-treatment must remove all zinc from the surface before anodizing — residual zinc causes "spangling" (iridescent patches) in the oxide. Double deoxidize in nitric acid if necessary.

### Common Defects and Troubleshooting

- **Burning**: Dark, rough, powdery areas caused by excessive local current density. Occurs at sharp edges, corners, and contact points. Prevention: use shielding (plastic shields to redirect current), reduce overall current density, ensure good fixturing contact.
- **Pitting**: Small holes in the oxide. Caused by chloride contamination in the bath (>50 ppm Cl⁻ from tap water or drag-in). Prevention: use deionized water for bath makeup, monitor chloride with ion-selective electrode.
- **Soft coating**: Oxide hardness below specification. Caused by bath temperature too high, acid concentration too low, or insufficient current density. Remedy: verify temperature control, check acid concentration by titration, confirm current density with ammeter.
- **Powdering / chalking**: White, powdery surface after sealing. Caused by sealing at too-high pH (>7.0) or insufficient rinsing between anodize and seal. Remedy: adjust seal bath pH to 5.5-6.0, add intermediate rinse step.
- **Galvanic burning**: Localized burning at contact points between dissimilar metals. Prevention: ensure only aluminum-to-aluminum or aluminum-to-titanium contacts in the anodizing bath.

### Safety

**Sulfuric acid burn hazard**: Type II and Type III anodizing baths contain 150-250 g/L H₂SO₄ (approximately 15-25% by weight). Skin contact causes immediate chemical burns; eye contact causes permanent corneal damage. Wear chemical splash goggles (not safety glasses — goggles seal against the face), face shield, acid-resistant apron (PVC or neoprene), and nitrile gloves (double-gloved for Type III where acid concentration and current density are higher). Emergency eyewash and safety shower within 10 seconds travel time from all anodizing stations.

**Electrical hazard**: Anodizing operates at 12-75 V DC with currents of 500-10,000 A. At 50+ V DC (Type III hard anodizing), the voltage exceeds the physiological threshold for electrical shock through wet skin. The electrolyte is conductive — immersion of hands in the bath while the power is on can deliver a lethal shock through the current path: power supply → rack → workpiece → electrolyte → hands → body → ground. De-energize power supply before inserting or removing workpieces. Never reach into the bath while current is flowing.

**Hydrogen gas evolution**: Hydrogen gas is generated at the cathode during anodizing at a rate proportional to the current. For a 5000 A Type III bath, hydrogen evolution is approximately 2.1 L/min at STP. In an enclosed tank area, hydrogen accumulates above the LEL (4% in air) and ignites from any spark. Ensure adequate ventilation (minimum 1 m³/min per m² of bath surface area). No smoking, open flames, or spark-generating tools near anodizing tanks.

**Oxalic acid additive toxicity**: Oxalic acid (5-15 g/L) used as a burning suppressant in Type III baths is toxic if ingested (LD₅₀ ~375 mg/kg) and causes kidney damage from calcium oxalate crystal formation. Avoid skin contact. Do not eat or drink in the anodizing area.

### See Also

- **[Electroplating](electroplating.md)**: Copper damascene, nickel, gold, tin plating processes
- **[Electrochemical Surface Processes](electrochemical-processes.md)**: Electropolishing for ultrapure surfaces
- **[Metal Finishing](../metals/finishing.md)**: Overview of anodizing in the context of metal surface treatments
- **[Aluminum Production](../metals/aluminum.md)**: Aluminum alloy properties and heat treatment

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electrochemistry & Plating](./index.md) • [All Domains](../index.md)*
