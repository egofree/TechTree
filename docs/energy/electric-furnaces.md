# Electric Furnaces

> **Node ID**: energy.electric-furnaces
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.electricity`](electricity.md), `machine-tools`
> **Enables**: [`energy.electric-furnaces.electrode-manufacturing`](electrode-manufacturing.md), `machine-tools.joining.diffusion-bonding`, [`metals.powder-metallurgy`](../metals/powder-metallurgy.md), [`silicon.mg-si-production`](../silicon/mg-si-production.md)
> **Timeline**: Years 20-30
> **Outputs**: electric_arc_furnaces, resistance_heaters, eaf_steel
> **Critical**: Yes — electric furnaces are the only route to temperatures above 1500°C in controlled atmosphere; essential for steel recycling, silicon reduction, and ferroalloy production

### Overview

Electric furnaces convert electrical energy into high-temperature heat for smelting, melting, and heat treatment. They are the only practical route to temperatures above ~1500°C in a controlled atmosphere, making them indispensable for steel recycling, silicon reduction, ferroalloy production, and advanced ceramics. Three main families exist: **[electric arc furnaces](../glossary/electric-arc-furnaces.md)** (EAF), **[submerged arc furnaces](../glossary/submerged-arc-furnaces.md)** (SAF), and **resistance heating furnaces**. For a broader electrical context, see [electricity.md](electricity.md); for silicon-specific EAF operation, see [mg-si-production.md](../silicon/mg-si-production.md).

---

### Electric Arc Furnace (EAF)

**Strengths**:
- Achieves 3,000-3,500°C in the arc column — the highest temperatures achievable in any industrial furnace
- Melts 100% scrap steel — enables steel recycling without virgin iron ore
- Quick heat cycles (30-60 minutes per batch) allow flexible scheduling
- No combustion gases — cleaner operation than coal-fired furnaces

**Weaknesses**:
- Enormous electrical demand (20-50 MW for a typical EAF) — requires grid-scale power
- Graphite electrodes are consumed at 2-8 kg per tonne of steel — ongoing consumable cost
- Bootstrapping challenge: graphitization of electrodes requires 2,500-3,000°C, typically produced by an existing EAF
- Arc instability and electromagnetic stirring require automatic impedance control systems

**Principle**: An electric arc struck between graphite electrodes and the charge material produces temperatures of **[3000–3500°C](../glossary/30003500c.md)** in the arc column, heating the charge by radiation, convection, and direct resistance.

**Construction**:
- **Shell**: Cylindrical steel vessel, 2–8 m diameter, water-cooled side panels and roof (pipe coils welded to steel plate). Bottom is refractory-lined.
- **Lining**: Basic refractory — magnesite (MgO) brick or rammed dolomite (CaO·MgO). Thickness 300–500 mm. Acidic linings (SiO₂) exist for special alloys but are uncommon. Neutral linings (Al₂O₃, chromite) used for specific slags.
- **Electrodes**: Three graphite electrodes (50–700 mm diameter), inserted through the roof in a delta arrangement. Electrodes are consumed at ~2–8 kg per tonne of steel (oxidation, tip erosion, breakage).
- **Electrode regulation**: Hydraulic or electric winch system raises/lowers each electrode independently to maintain arc length (~10–50 mm) and regulate current. Automatic impedance control is standard.

**[Electrode manufacturing](../glossary/electrode-manufacturing.md)** (bootstrapping challenge):
1. Mix petroleum coke (or pitch coke) with coal tar pitch binder (~25% by weight).
2. Extrude into rods at ~100–150°C (pitch is thermoplastic).
3. Bake at 800–1200°C in a ring furnace over 2–4 weeks (carbonization — volatile matter driven off).
4. **[Graphitize](../glossary/graphitize.md)** at 2500–3000°C (requires an existing EAF or resistive furnace — circular dependency). Early electrodes can remain as amorphous carbon (lower conductivity, higher consumption rate, but functional).

**Operation — steelmaking**:
1. **Charge**: Load scrap steel (or direct-reduced iron) into the furnace via basket or conveyor. Charge weight 1–100 tonnes (typical 30–80 t).
2. **Melt down**: Lower electrodes, strike arc on the solid charge. Melt period ~20–40 minutes at full power.
3. **Refine**: Add flux (lime, fluorspar) to form slag. Blow oxygen (lance or burner) to decarburize. Adjust alloy additions.
4. **Tap**: Tilt furnace, pour molten steel (~1600–1650°C) into ladle. Slag remains behind.
5. **Cycle time**: 30–90 minutes per heat. Continuous operation: 20–30 heats/day.

**Power requirements**:
- Specific energy: **[300–600 kWh per tonne of steel](../glossary/300600-kwh-per-tonne-of-steel.md)** (depends on scrap quality, preheating, oxygen use).
- Connected power: 10–80 MW for a modern furnace (three-phase AC, 100–800V secondary, 20–100 kA).
- Furnace transformer is a specialized item: high current, low voltage, with tap changer for power regulation.

---

### Submerged Arc Furnace (SAF)

**Strengths**:
- Continuous operation — runs 24/7 for months between maintenance, unlike batch EAF
- Energy efficient for reduction processes — heat generated directly within the charge material
- Handles raw materials (ore, carbon, flux) without pre-processing

**Weaknesses**:
- Continuous power demand — power interruptions cause charge solidification, ruining the furnace
- Electrode consumption 30-60 kg per tonne of silicon — major operating cost
- Limited to reduction smelting — not suitable for steel recycling or heat treatment

**Principle**: Similar to EAF, but electrodes are **submerged in the raw material charge**. Heat is generated primarily by the electrical resistance of the charge itself (not just the arc), making it more energy-efficient for continuous reduction processes.

**Applications**:
- **Silicon production**: SiO₂ + 2C → Si + 2CO at ~1800–2100°C (see [mg-si-production.md](../silicon/mg-si-production.md)). Energy consumption ~11–13 kWh/kg Si.
- **Ferroalloys**: Ferrosilicon (FeSi), ferromanganese (FeMn), ferrochromium (FeCr) — alloying elements for steel.
- **Calcium carbide**: CaO + 3C → CaC₂ + CO at ~2000°C. Critical feedstock for acetylene.
- **Phosphorus**: Apatite + coke + silica at ~1400–1500°C.

**Construction differences from EAF**:
- **Shell**: Larger diameter (3–12 m), lower height-to-width ratio. Often open-top or semi-covered.
- **Electrodes**: 1–3 electrodes, larger diameter (300–1500 mm). Søderberg self-baking electrodes common (paste continuously added at top, baked by furnace heat as they descend — avoids prebaking step).
- **Lining**: Carbon or graphite refractory (withstands reducing conditions and high temperatures). Not basic MgO (would be reduced by carbon at these temperatures).
- **Power**: 5–40 MW per furnace. Three-phase AC for 3-electrode designs. Continuous operation — charge fed from top, product tapped from bottom taphole every 1–4 hours.

**SAF vs EAF**: SAF is for **[continuous smelting](../glossary/continuous-smelting.md)** (reduction of ores). EAF is for **[batch melting](../glossary/batch-melting.md)** (steel recycling). They are not interchangeable.

---

### Resistance Heating Furnaces

**Strengths**:
- No electrode consumption — heating elements last thousands of hours
- Precise temperature control (±5°C) by regulating current — better than arc furnaces
- Lower power demand than EAF — suitable for smaller installations
- Clean operation — no combustion gases or electrode off-gassing

**Weaknesses**:
- Maximum temperature limited by element material (1,400°C for nichrome, 1,800°C for silicon carbide)
- Not suitable for smelting — primarily for heat treatment, melting, and sintering
- Heating elements are consumable — they oxidize and fail over time, requiring replacement
- Lower power density than arc furnaces — slower heating for the same furnace volume

**Principle**: Current passed through a resistive heating element generates heat: P = I²R. No arc, no electrodes consumed. Element temperature is controlled by regulating current.

**[Heating element materials](../glossary/heating-element-materials.md)** (ordered by maximum operating temperature):

| Element | Composition | Max temp | Atmosphere | Notes |
|---------|-------------|---------|------------|-------|
| Nichrome | 80% Ni, 20% Cr | ~1150°C | Oxidizing | Forms protective Cr₂O₃ scale. Ductile, easy to wind into coils. |
| Kanthal (FeCrAl) | Fe-22Cr-5.8Al | ~1400°C | Oxidizing | Forms Al₂O₃ scale. Brittle after use. Higher resistivity than Nichrome. |
| Silicon carbide (SiC) | SiC rods | ~1600°C | Oxidizing | Non-metallic. Resistance changes with age (aging). Very long service life. |
| Molybdenum disilicide (MoSi₂) | MoSi₂ | ~1800°C | Oxidizing | Forms SiO₂ glass layer at high temp — self-healing. Brittle. |
| Graphite | C | ~2500°C | Reducing/inert | Oxidizes rapidly in air above ~500°C. Used in vacuum or inert gas furnaces. |
| Tungsten | W | ~2800°C | Vacuum/H₂ | Highest melting point metal (3422°C). Used in special furnaces. |

**Early-stage elements**: Before specialty alloys are available, **[iron wire](../glossary/iron-wire.md)** can serve as a heating element in a reducing atmosphere (prevents oxidation) up to ~900°C. **[Graphite rods](../glossary/graphite-rods.md)** in a reducing or inert atmosphere extend the range considerably. **[Charcoal or coke beds](../glossary/charcoal-or-coke-beds.md)** with buried electrodes (resistive heating of the bed) can reach ~1200–1500°C without any metal element at all.

**Furnace construction for resistance heating**:
- **Chamber**: Refractory brick or ceramic fiber insulated box. Door or lid for access.
- **Element mounting**: Grooves in refractory walls, or suspended on ceramic insulators (alumina or mullite pegs).
- **Temperature control**: Thermocouple feedback → PID controller → thyristor (SCR) or variac power regulation.
- **Applications**: Annealing, stress-relief, tempering, sintering, crystal growth, glass melting (small scale), laboratory work, baking/curing.

---

### Furnace Linings

The refractory lining determines what the furnace can melt and how long it lasts:

- **Basic (MgO, CaO)**: Resists basic slags (lime-rich). Standard for EAF steelmaking. Magnesite brick or rammed dolomite. Life: 500–2000 heats before relining.
- **Acidic (SiO₂)**: Resists acidic slags. Used for cast iron, some copper alloys. Silica brick. Not suitable for steel (basic slag would dissolve it).
- **Neutral (Al₂O₃, Cr₂O₃, carbon)**: Broad compatibility. Alumina brick for general-purpose. Carbon/graphite for reducing environments (SAF silicon, calcium carbide).
- **Thermal conductivity tradeoff**: Denser refractories conduct more heat (more loss through walls) but resist erosion better. Insulating brick (low density) reduces heat loss but is mechanically weak.

---

### Power Supply Considerations

Electric furnaces are among the most demanding electrical loads in any industrial economy:
- **Flicker**: EAF arcs cause rapid current swings, creating voltage flicker on the grid. Requires dedicated supply or static VAR compensators.
- **Power factor**: Arc furnaces have poor power factor (0.65–0.85). Capacitor banks needed for correction.
- **Transformer**: Furnace transformers are custom-built — high current (tens of kA), low voltage (100–800V), with on-load tap changers. Not a standard distribution transformer.
- **Grounding**: Furnace shell must be solidly grounded. Leakage current through the lining is a constant hazard.

---

### Dependencies & Bootstrap Sequence

1. **[Electricity generation](../glossary/electricity-generation.md)** (generators, turbines) → provides power.
2. **[Graphite electrodes](../glossary/graphite-electrodes.md)** → requires baking ovens (resistance-heated or gas-fired), eventually graphitization at 2500–3000°C (chicken-and-egg with EAF). Amorphous carbon electrodes bridge the gap.
3. **[Refractory brick](../glossary/refractory-brick.md)** → requires mining (magnesite, dolomite, bauxite, silica) and firing at ~1500°C (can use gas-fired kilns initially).
4. **[Steel shell](../glossary/steel-shell.md)** → requires plate steel (from blast furnace or early EAF).
5. **[Furnace transformer](../glossary/furnace-transformer.md)** → requires copper wire, silicon steel laminations, oil cooling.

The EAF is a **bootstrapping bottleneck**: you need steel to build it, but you need it to make quality steel from scrap. Early EAFs can use lower-grade materials (carbon electrodes, thinner linings, smaller capacity) and upgrade as production improves.

### Safety & Hazards

- **Arc flash (30,000°C)**: Arc-rated face shield, FR clothing, leather gloves. 1m minimum boundary.
- **Electrocution (100-800V, kA)**: Ground equipment. Lock-out/tag-out. Insulated tools.
- **Molten metal splash**: Pre-dry all charge. Face shield, leather apron.
- **IR radiation cataracts**: Shaded lenses for furnace viewing.

### EAF Construction Details

**Shell geometry**: The EAF shell is a deep bowl-shaped cylindrical vessel, typically 3-8 m in diameter for commercial units. The bottom section is spherical or conical to collect molten steel. Shell construction is thick steel plate (25-50 mm) with external reinforcement rings. Water-cooled panels replace refractory on the upper sidewalls in modern designs: pipe coils (50-80 mm diameter copper or steel tube) welded to a steel backing plate, with water flowing through at 20-40 L/min per panel. These panels absorb the intense radiation from the arc zone and dramatically reduce refractory consumption.

**Roof and charging**: The roof is either a swing-away or lift-off design to allow scrap charging via overhead crane and drop-bottom charging basket. A typical charge involves 2-3 basket loads to fill the furnace. The roof contains three electrode ports (water-cooled copper or steel rings) and a fourth port for off-gas extraction. Roof life: 500-2000 heats for water-cooled panel roofs.

**Graphite electrodes**: Three electrodes, 200-700 mm diameter, suspended in a triangular (delta) arrangement from the roof. Electrode current: 20-80 kA at 200-800 V. Electrode consumption: 2-8 kg per tonne of steel, from oxidation, sublimation at the arc tip, and mechanical breakage. Electrodes are made in segments (1.5-2.5 m each) and joined with threaded nipples (carbon or graphite) as they are consumed from the bottom. Electrode regulation systems maintain arc impedance by adjusting electrode height at 2-5 mm/s response speed.

**Tap-to-tap cycle**: A complete heat cycle (tap-to-tap time) runs 45-90 minutes. Breakdown: charging (5-10 min), melting (20-40 min at full power), refining and temperature adjustment (5-15 min), tapping (3-5 min). Productivity: 20-30 heats per day for a well-run furnace. Modern high-power EAFs with scrap preheating and oxygen lancing approach 45-minute cycles.

### Submerged Arc Furnace Detail

**Shell and lining**: The SAF shell is a large-diameter (3-12 m), relatively shallow steel cylinder lined with carbon blocks or rammed carbon mass. The carbon lining withstands the strongly reducing environment and temperatures above 1800°C that would destroy MgO or Al₂O₃ refractories. Lining life: 2-5 years for the sidewalls, though the hearth may last 10+ years. The shell is often open-top or semi-covered, with fume extraction hoods above.

**Electrode systems**: Two main types. Söderberg self-baking electrodes: a steel casing (1-2 mm thick) is continuously filled with a paste of calcined anthracite, coal tar pitch, and petroleum coke. As the electrode descends through the furnace roof, the heat from the furnace bakes the paste into a solid carbon electrode in place. Diameter: 600-1500 mm. This avoids the expensive separate graphitization step. Prebaked electrodes: manufactured off-site like EAF electrodes, used for silicon and aluminum production where purity matters. Electrode consumption: 3-5 kg/MWh of electrical input for Söderberg systems in ferroalloy production.

**Electrical system**: Three-phase AC power at 50-60 Hz, with 1-3 electrodes arranged in a line or triangle. Furnace transformer secondary voltage: 100-250 V. Current: 20-150 kA. Power factor is low (0.65-0.85) due to the long arc and resistance path; capacitor banks are required for correction. Electrode positioning controls power distribution across the charge bed.

### Resistance Furnace Construction

**Heating element materials in detail**:

**[Nichrome 80/20](../glossary/nichrome-8020.md)** (80% nickel, 20% chromium): The workhorse for furnaces up to 1150°C. Forms a thin, adherent Cr₂O₃ scale that protects the underlying alloy from further oxidation. Ductile when new, easily wound into coils or bent into zigzag elements. Resistivity: 1.08 Ω·mm²/m at 20°C. Life at 1100°C in air: 5,000-20,000 hours depending on duty cycle. Element temperature should be kept 50-100°C above furnace chamber temperature to maintain heat transfer.

**[Kanthal APM](../glossary/kanthal-apm.md)** (Fe-22Cr-5.8Al, with additions): Operates to 1400°C in air. Forms a protective Al₂O₃ scale instead of Cr₂O₃, which is more stable at high temperature. Higher resistivity (1.45 Ω·mm²/m) than Nichrome, meaning shorter elements for the same power. Becomes brittle after prolonged high-temperature exposure due to aluminum precipitation, making element replacement the norm rather than repair.

**Molybdenum disilicide (MoSi₂)**: Operates to 1700-1800°C in oxidizing atmospheres. At high temperature, silicon oxidizes to form a viscous SiO₂ glass layer that self-heals cracks. This glassy coating is what makes MoSi₂ viable despite molybdenum's tendency to oxidize catastrophically. Brittle at all temperatures, requiring careful mounting and protection from mechanical shock. Often supplied as hairpin-shaped elements that hang from the furnace roof.

**Silicon carbide (SiC)**: Rod or tubular elements operating to 1600°C. Non-metallic. Electrical resistance increases with age (silicon oxidation changes the composition), requiring periodic voltage adjustment to maintain power output. Very long service life under proper conditions (10,000+ hours at 1400°C). Silicon carbide has high thermal conductivity, reducing thermal gradients in the element.

### Induction Heating

**Coreless induction furnace**: A water-cooled copper coil surrounds a ceramic crucible containing the metal charge. Alternating current in the coil generates an oscillating magnetic field, inducing eddy currents in the conductive charge. The eddy currents heat the metal by I²R losses. No electrodes, no combustion gases, no contamination of the melt.

**Frequency selection**: Lower frequency penetrates deeper into the charge. Mains frequency (50-60 Hz) suits large furnaces (1-30 tonnes) for iron and steel melting. Medium frequency (150-1000 Hz) suits smaller furnaces (0.1-5 tonnes) and provides better stirring. High frequency (1-10 kHz) for surface hardening and brazing of small parts.

**Skin depth formula**: The effective penetration depth of the induced current is δ = 5030 × √(ρ / (μ × f)) mm, where ρ is the resistivity of the charge (Ω·mm²/m), μ is the relative magnetic permeability, and f is the frequency (Hz). For mild steel at room temperature (ρ ≈ 0.17 Ω·mm²/m, μ ≈ 100) at 50 Hz: δ ≈ 5030 × √(0.17 / (100 × 50)) ≈ 2.9 mm. At 1000 Hz: δ ≈ 0.65 mm. The charge diameter should be at least 3-4× the skin depth for efficient coupling.

**Power density**: Coreless furnaces operate at 200-800 kW per tonne of capacity. A 1-tonne steel furnace at 500 kW melts cold scrap to 1600°C in roughly 45-60 minutes. Electrical efficiency: 60-75% (coil losses, thermal losses account for the rest).

### EAF Shell and Electrode Construction

**Shell geometry**: The EAF shell is a deep bowl-shaped cylindrical vessel, typically 3-8 m diameter for commercial units. The bottom section is spherical or conical to collect molten steel. Shell construction is thick steel plate (25-50 mm) with external reinforcement rings. Water-cooled panels replace refractory on the upper sidewalls: pipe coils (50-80 mm diameter copper or steel tube) welded to a steel backing plate, with water flowing at 20-40 L/min per panel. These panels absorb intense radiation from the arc zone and reduce refractory consumption.

**Roof and charging**: The roof swings away or lifts off for scrap charging via overhead crane and drop-bottom basket. A typical charge involves 2-3 basket loads. The roof contains three electrode ports (water-cooled copper rings) and a fourth port for off-gas extraction. Roof life: 500-2000 heats for water-cooled panel roofs.

**Graphite electrodes**: Three electrodes, 200-700 mm diameter, suspended in a delta arrangement. Electrode current: 20-80 kA at 200-800 V. Consumption: 2-8 kg per tonne of steel from oxidation and sublimation. Electrodes are made in segments (1.5-2.5 m each) joined with threaded nipples. Electrode regulation systems adjust height at 2-5 mm/s to maintain arc impedance.

**Tap-to-tap cycle**: A complete heat cycle runs 45-90 minutes. Breakdown: charging (5-10 min), melting (20-40 min at full power), refining (5-15 min), tapping (3-5 min). Productivity: 20-30 heats per day.

### Submerged Arc Furnace Detail

**Shell and lining**: The SAF shell is a large-diameter (3-12 m), shallow steel cylinder lined with carbon blocks or rammed carbon. The carbon lining withstands the reducing environment and temperatures above 1800°C that would destroy MgO or Al₂O₃ refractories. Lining life: 2-5 years for sidewalls, 10+ years for the hearth.

**Söderberg self-baking electrodes**: A steel casing (1-2 mm thick) is continuously filled with paste of calcined anthracite, coal tar pitch, and petroleum coke. As the electrode descends through the furnace roof, heat bakes the paste into solid carbon in place. Diameter: 600-1500 mm. Electrode consumption: 3-5 kg/MWh of electrical input for ferroalloy production. This avoids the expensive separate graphitization step required for prebaked electrodes.

**Electrical system**: Three-phase AC at 50-60 Hz, with 1-3 electrodes. Furnace transformer secondary: 100-250 V, 20-150 kA. Power factor is low (0.65-0.85); capacitor banks required for correction.

### Resistance Heating Elements in Detail

**[Nichrome 80/20](../glossary/nichrome-8020.md)** (80% nickel, 20% chromium): Workhorse for furnaces up to 1150°C. Forms a thin Cr₂O₃ scale protecting the alloy from further oxidation. Ductile when new, easily wound into coils. Resistivity: 1.08 Ω·mm²/m at 20°C. Life at 1100°C in air: 5,000-20,000 hours.

**[Kanthal APM](../glossary/kanthal-apm.md)** (Fe-22Cr-5.8Al): Operates to 1400°C in air. Forms protective Al₂O₃ scale, more stable than Cr₂O₃ at high temperature. Resistivity: 1.45 Ω·mm²/m. Becomes brittle after prolonged high-temperature exposure.

**Molybdenum disilicide (MoSi₂)**: Operates to 1700-1800°C in oxidizing atmospheres. At high temperature, silicon oxidizes to form a viscous SiO₂ glass layer that self-heals cracks. Brittle at all temperatures, requiring careful mounting.

**Silicon carbide (SiC)**: Rod elements operating to 1600°C. Non-metallic. Resistance increases with age, requiring periodic voltage adjustment. Service life: 10,000+ hours at 1400°C.

### Induction Heating

**Skin depth formula**: δ = 5030 × √(ρ / (μ × f)) mm.

### Limitations

- **Electrode consumption**: Graphite electrodes erode during EAF operation at 2-5 kg per tonne of steel. Electrode manufacturing is a specialized, energy-intensive process.
- **Power quality impact**: EAFs are heavy intermittent loads causing voltage flicker and harmonic distortion on the electrical grid. Requires power factor correction and harmonic filtering.
- **Refractory wear**: Furnace linings erode from slag attack and thermal cycling. Refractory life: 500-2000 heats depending on severity of service. Relining is a major maintenance event.
- **Capital cost**: Electric furnaces require substantial electrical infrastructure (transformers, rectifiers, bus bars) in addition to the furnace vessel itself.
- **Water cooling complexity**: EAF walls and roofs use water-cooled panels. A cooling water failure leads to rapid equipment damage. Redundant pumping and emergency water storage required.

### See Also

- [Electricity Generation](electricity.md) — Power supply for electric furnaces
- [Electrode Manufacturing](electrode-manufacturing.md) — Carbon electrode production
- [Iron & Steel](../metals/iron-steel.md) — Steel production using electric furnaces
- [Refractories](../chemistry/refractories.md) — Furnace lining materials
- [Cooling Systems](cooling.md) — Industrial process cooling

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
