# Electric Furnaces

> **Node ID**: energy.electric-furnaces
> **Domain**: [Energy](./)
> **Dependencies**: `energy.electricity`, `metals.iron-steel`, `machine-tools`
> **Enables**: `silicon.mg-si-production`, `metals.iron-steel` (recycled), `glass.advanced`
> **Timeline**: Years 20-30
> **Outputs**: electric_arc_furnaces, resistance_heaters, eaf_steel

### Overview

Electric furnaces convert electrical energy into high-temperature heat for smelting, melting, and heat treatment. They are the only practical route to temperatures above ~1500°C in a controlled atmosphere, making them indispensable for steel recycling, silicon reduction, ferroalloy production, and advanced ceramics. Three main families exist: **electric arc furnaces** (EAF), **submerged arc furnaces** (SAF), and **resistance heating furnaces**. For a broader electrical context, see [electricity.md](electricity.md); for silicon-specific EAF operation, see [mg-si-production.md](../silicon/mg-si-production.md).

---

### Electric Arc Furnace (EAF)

**Principle**: An electric arc struck between graphite electrodes and the charge material produces temperatures of **3000–3500°C** in the arc column, heating the charge by radiation, convection, and direct resistance.

**Construction**:
- **Shell**: Cylindrical steel vessel, 2–8 m diameter, water-cooled side panels and roof (pipe coils welded to steel plate). Bottom is refractory-lined.
- **Lining**: Basic refractory — magnesite (MgO) brick or rammed dolomite (CaO·MgO). Thickness 300–500 mm. Acidic linings (SiO₂) exist for special alloys but are uncommon. Neutral linings (Al₂O₃, chromite) used for specific slags.
- **Electrodes**: Three graphite electrodes (50–700 mm diameter), inserted through the roof in a delta arrangement. Electrodes are consumed at ~2–8 kg per tonne of steel (oxidation, tip erosion, breakage).
- **Electrode regulation**: Hydraulic or electric winch system raises/lowers each electrode independently to maintain arc length (~10–50 mm) and regulate current. Automatic impedance control is standard.

**Electrode manufacturing** (bootstrapping challenge):
1. Mix petroleum coke (or pitch coke) with coal tar pitch binder (~25% by weight).
2. Extrude into rods at ~100–150°C (pitch is thermoplastic).
3. Bake at 800–1200°C in a ring furnace over 2–4 weeks (carbonization — volatile matter driven off).
4. **Graphitize** at 2500–3000°C (requires an existing EAF or resistive furnace — circular dependency). Early electrodes can remain as amorphous carbon (lower conductivity, higher consumption rate, but functional).

**Operation — steelmaking**:
1. **Charge**: Load scrap steel (or direct-reduced iron) into the furnace via basket or conveyor. Charge weight 1–100 tonnes (typical 30–80 t).
2. **Melt down**: Lower electrodes, strike arc on the solid charge. Melt period ~20–40 minutes at full power.
3. **Refine**: Add flux (lime, fluorspar) to form slag. Blow oxygen (lance or burner) to decarburize. Adjust alloy additions.
4. **Tap**: Tilt furnace, pour molten steel (~1600–1650°C) into ladle. Slag remains behind.
5. **Cycle time**: 30–90 minutes per heat. Continuous operation: 20–30 heats/day.

**Power requirements**:
- Specific energy: **300–600 kWh per tonne of steel** (depends on scrap quality, preheating, oxygen use).
- Connected power: 10–80 MW for a modern furnace (three-phase AC, 100–800V secondary, 20–100 kA).
- Furnace transformer is a specialized item: high current, low voltage, with tap changer for power regulation.

---

### Submerged Arc Furnace (SAF)

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

**SAF vs EAF**: SAF is for **continuous smelting** (reduction of ores). EAF is for **batch melting** (steel recycling). They are not interchangeable.

---

### Resistance Heating Furnaces

**Principle**: Current passed through a resistive heating element generates heat: P = I²R. No arc, no electrodes consumed. Element temperature is controlled by regulating current.

**Heating element materials** (ordered by maximum operating temperature):

| Element | Composition | Max temp | Atmosphere | Notes |
|---------|-------------|---------|------------|-------|
| Nichrome | 80% Ni, 20% Cr | ~1150°C | Oxidizing | Forms protective Cr₂O₃ scale. Ductile, easy to wind into coils. |
| Kanthal (FeCrAl) | Fe-22Cr-5.8Al | ~1400°C | Oxidizing | Forms Al₂O₃ scale. Brittle after use. Higher resistivity than Nichrome. |
| Silicon carbide (SiC) | SiC rods | ~1600°C | Oxidizing | Non-metallic. Resistance changes with age (aging). Very long service life. |
| Molybdenum disilicide (MoSi₂) | MoSi₂ | ~1800°C | Oxidizing | Forms SiO₂ glass layer at high temp — self-healing. Brittle. |
| Graphite | C | ~2500°C | Reducing/inert | Oxidizes rapidly in air above ~500°C. Used in vacuum or inert gas furnaces. |
| Tungsten | W | ~2800°C | Vacuum/H₂ | Highest melting point metal (3422°C). Used in special furnaces. |

**Early-stage elements**: Before specialty alloys are available, **iron wire** can serve as a heating element in a reducing atmosphere (prevents oxidation) up to ~900°C. **Graphite rods** in a reducing or inert atmosphere extend the range considerably. **Charcoal or coke beds** with buried electrodes (resistive heating of the bed) can reach ~1200–1500°C without any metal element at all.

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

1. **Electricity generation** (generators, turbines) → provides power.
2. **Graphite electrodes** → requires baking ovens (resistance-heated or gas-fired), eventually graphitization at 2500–3000°C (chicken-and-egg with EAF). Amorphous carbon electrodes bridge the gap.
3. **Refractory brick** → requires mining (magnesite, dolomite, bauxite, silica) and firing at ~1500°C (can use gas-fired kilns initially).
4. **Steel shell** → requires plate steel (from blast furnace or early EAF).
5. **Furnace transformer** → requires copper wire, silicon steel laminations, oil cooling.

The EAF is a **bootstrapping bottleneck**: you need steel to build it, but you need it to make quality steel from scrap. Early EAFs can use lower-grade materials (carbon electrodes, thinner linings, smaller capacity) and upgrade as production improves.

---

*Part of the [Bootciv Tech Tree](../) · [All Domains](../)*
