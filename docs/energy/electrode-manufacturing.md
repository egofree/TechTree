# Electrode Manufacturing

> **Node ID**: energy.electric-furnaces.electrode-manufacturing
> **Domain**: [Energy](./)
> **Dependencies**: `energy.electric-furnaces`, `energy.fuels.coke`, `chemistry`
> **Enables**: `energy.electric-furnaces` (graphite electrodes), `silicon.mg-si-production` (SAF electrodes)
> **Timeline**: Years 20-35
> **Outputs**: graphite_electrodes, carbon_electrodes, electrode_paste

### Overview

Electrodes are the critical consumable component of electric arc furnaces (EAF) and submerged arc furnaces (SAF). They conduct electrical current into the furnace, withstand temperatures of 3000°C in the arc zone, and resist oxidation and thermal shock while being slowly consumed at 2-8 kg per tonne of steel (EAF) or 30-60 kg per tonne of silicon (SAF). Manufacturing graphite electrodes is a multi-step process that requires baking and graphitization at extremely high temperatures — creating a bootstrapping challenge since those high temperatures are themselves typically produced by electric arc furnaces running on the very electrodes being produced. For the furnace context, see [electric-furnaces.md](electric-furnaces.md).

### Raw Materials

**Petroleum coke** (primary filler):
- Byproduct of petroleum refining — residual heavy oils are thermally cracked (coked) at ~500°C to drive off volatile hydrocarbons, leaving nearly pure carbon. Two main types:
  - **Needle coke**: From catalytic cracking of heavy gas oils. Has an elongated, needle-like crystal structure that gives high thermal conductivity and low electrical resistivity. Preferred for premium graphite electrodes (high power, low consumption). More expensive.
  - **Regular (sponge) coke**: From delayed coking of residual oil. Amorphous structure with lower thermal conductivity. Used for standard-grade electrodes and amorphous carbon electrodes.
- **Properties required**: Low sulfur (<1%, ideally <0.5%), low ash (<0.5%, ash causes electrode brittleness and contamination of the molten product), low heavy metals (vanadium, nickel — cause catalytic oxidation). Calcined before use.

**Coal tar pitch** (binder):
- Byproduct of coke oven gas condensation in coal carbonization. Black, brittle, thermoplastic solid at room temperature, softens at ~80-120°C, melts at ~120-150°C.
- **Function**: Binds the coke particles together into a coherent mass during forming, then carbonizes during baking to form a solid carbon matrix. The pitch must wet the coke surface adequately and provide sufficient green strength after forming.
- **Types**: Soft pitch (low softening point, 60-80°C) gives better mixing and extrusion but lower baked strength. Medium pitch (80-100°C) is standard. Hard pitch (>100°C) gives higher baked density but harder mixing.
- Typical binder content: 20-30% by weight of the total mix.

**Calcination** (pre-treatment of coke):
- Raw petroleum coke contains 5-15% volatile matter that must be removed before electrode manufacturing. Calcination heats the coke to 1200-1350°C in a rotary kiln, vertical shaft kiln, or rotary hearth furnace. Volatiles are driven off and either flared or recovered. The calcined coke shrinks, densifies, and gains electrical conductivity (resistivity drops from ~1000 to ~500 μΩ·m).
- **Quality metrics**: Real density >2.05 g/cm³, electrical resistivity <550 μΩ·m, moisture <0.3%, volatile matter <0.5%. Higher real density = denser, stronger electrode.

### Mixing and Milling

1. **Crushing and milling**: Calcined coke is crushed in jaw crushers and then ground in ball mills or rod mills to the target particle size distribution. A controlled mix of coarse (2-8 mm), medium (0.5-2 mm), and fine (fines, <0.15 mm) particles achieves maximum packing density in the final electrode. Typical distribution: 30-40% coarse, 20-30% medium, 30-40% fines.
2. **Drying**: All solid ingredients are dried to <0.5% moisture. Moisture causes steam formation during mixing and baking, creating pores and cracks.
3. **Heating**: Coke fractions are preheated to ~130-160°C in a heated silo or rotary dryer.
4. **Pitch addition**: Coal tar pitch (solid at room temperature) is added as hot liquid (~160-180°C). Pitch content: 20-30% by weight for extrusion, 22-28% for molding.
5. **Mixing**: Heated coke and liquid pitch are combined in a heated intensive mixer (sigma-blade or planetary type) at ~150-170°C. Mixing time: 20-60 minutes. The pitch must coat every coke particle uniformly. Under-mixing creates weak spots; over-mixing degrades pitch quality through oxidation.

### Forming

**Extrusion** (most common for cylindrical electrodes):
- The hot pitch-coke mix (green paste, ~120-140°C) is loaded into a heated hydraulic press chamber. A ram forces the paste through a die of the desired diameter (300-700 mm for large electrodes, 75-250 mm for smaller sizes).
- The extrusion process aligns the coke particles preferentially along the electrode axis — this gives extruded electrodes higher thermal conductivity and lower electrical resistivity along the length than across the diameter (anisotropic properties).
- Extrusion pressure: 100-200 bar. The paste must flow smoothly through the die without tearing or forming internal cracks. Temperature control is critical — too cold and the pitch is too viscous (high pressure, surface tearing); too hot and the pitch is too fluid (shape deformation, inadequate particle binding).
- The extruded electrode is cut to length, cooled on a cooling table, and inspected for surface cracks and voids.

**Vibro-molding** (alternative for very large diameters):
- The green paste is placed in a mold on a vibrating table. Vibration compacts the paste into the mold shape. Used for diameters >700 mm where extrusion forces become impractically high. Lower particle alignment (more isotropic properties) but suitable for applications where this is acceptable.

### Baking (Carbonization)

The green electrodes are baked to convert the pitch binder from thermoplastic to solid carbon:

- **Furnace type**: Ring furnace (most common) — freestanding pits surrounded by flue walls. Electrodes are packed in a bed of metallurgical coke (packing material) that supports them and transfers heat evenly. Fuel gas is fired in the flue walls, heating the pits indirectly.
- **Temperature cycle**:
  1. Warm-up: 0-350°C over 3-5 days. The pitch softens and the electrode body settles under its own weight. Controlled temperature rise prevents blistering (pitch outgassing too fast → bubbles trapped in the matrix).
  2. Carbonization: 350-800°C over 5-8 days. Volatile matter from the pitch decomposes, leaving solid carbon. This is the critical stage — the rate of volatile evolution must not exceed the permeability of the electrode body. Excessive rate causes cracking and internal pressure buildup.
  3. Final bake: 800-1200°C over 3-5 days. Residual carbonization completes. The electrode body is now a solid carbon-carbon composite (calcined coke particles in a carbonized pitch matrix).
- **Total cycle**: 2-4 weeks including loading, heating, cooling, and unloading. The furnace operates continuously — while one batch cools, the next heats. Typical throughput: 1-2 batches per pit per month.
- **Result**: Baked carbon electrode (amorphous carbon, not yet graphitized). Density: ~1.5-1.65 g/cm³. Electrical resistivity: ~40-60 μΩ·m. Functional for EAF use but with higher consumption rate than graphitized electrodes (3-5× higher due to lower conductivity and oxidation resistance).

### Graphitization

Graphitization transforms the baked carbon electrode into graphite by heating to 2500-3000°C:

- **Process**: Electrodes are stacked in a long refractory-lined pit with a surrounding bed of coke and graphite. Large electrical current (50-200 kA) is passed directly through the electrodes themselves — they serve as both the load and the heating element (resistive heating). The process takes 1-3 weeks per batch.
- **Temperature stages**:
  - 0-1500°C: Resistance heating (electrode itself is the resistor). Power consumption ~1000-2000 kWh per tonne.
  - 1500-2500°C: Graphitization begins. Crystal structure transforms from disordered turbostratic carbon to ordered hexagonal graphite. Volume expands ~2-3%. Power consumption: 2000-3000 kWh per tonne.
  - 2500-3000°C: Maximum graphitization. Electrical resistivity drops sharply. Thermal conductivity increases. Crystal size grows (measured by X-ray diffraction).
- **Total energy**: 3000-5000 kWh per tonne of electrode. This is an enormous energy input.
- **Result**: Graphite electrode. Density: ~1.6-1.75 g/cm³. Electrical resistivity: 5-12 μΩ·m (4-8× better than baked carbon). Thermal conductivity: 80-200 W/(m·K) along the axis. Mechanical strength at room temperature: lower than baked carbon (graphite is more brittle) but maintained at high temperatures (graphite actually gets stronger above 2000°C).

### The Bootstrapping Challenge

Graphitization at 2500-3000°C requires an existing electric furnace capable of delivering enormous power to a resistive load — which is exactly what the graphite electrodes being produced are used for. This circular dependency must be resolved:

1. **Start with amorphous carbon electrodes**: Baked carbon electrodes (baked only to ~1200°C, no graphitization step) are functional in EAFs and SAFs. They have higher electrical resistivity, higher consumption rate, and lower thermal shock resistance — but they work. Expect 3-5× higher electrode consumption per tonne of product compared to graphitized electrodes.
2. **Use the first EAF to graphitize**: Once a first EAF is operational with carbon electrodes, it can power the graphitization process. Build a simple graphitization pit, connect the EAF transformer output to electrodes stacked as the load, and graphitize a batch of electrodes. This first batch of graphitized electrodes is then used in the EAF, dramatically improving its efficiency and reducing electrode consumption.
3. **Positive feedback loop**: Better electrodes → more efficient furnace operation → more surplus power available for graphitization → better electrodes. The system converges rapidly once the first graphitized electrodes are available.
4. **Alternative path**: Resistive furnaces (silicon carbide or molybdenum disilicide heating elements) can reach ~1600°C in a controlled atmosphere. Not sufficient for full graphitization but adequate for carbon baking. Acheson furnace (graphite powder bed resistance heating) can reach 2500°C+ without pre-existing electrodes — but requires substantial power infrastructure.

### Amorphous Carbon Electrodes

When graphitization is not yet available, amorphous (baked carbon) electrodes serve as the functional intermediate:

- **Performance**: Electrical resistivity 40-60 μΩ·m (vs. 5-12 μΩ·m for graphite). This means higher voltage drop across the electrode, more I²R heating losses, and lower power delivered to the arc. The furnace must operate at higher current to compensate.
- **Consumption rate**: 5-15 kg per tonne of steel (EAF) vs. 2-8 kg for graphite electrodes. For SAF silicon production: 60-100 kg per tonne of silicon vs. 30-60 kg for graphite. The higher consumption rate is driven by oxidation (amorphous carbon oxidizes faster than graphite above ~500°C) and mechanical erosion (lower thermal shock resistance).
- **Mitigation**: Apply an antioxidant coating (silicon carbide or glaze) to the electrode sides (not the tip — the arc must strike bare carbon). Reduce oxidation by operating with shorter electrode columns exposed above the furnace roof. Use larger-diameter electrodes to reduce current density (lower I²R losses and lower tip erosion rate).
- **Søderberg self-baking electrodes** (SAF alternative): For submerged arc furnaces, a paste of calcined coke and coal tar pitch is continuously added to the top of a steel casing. As the casing descends into the furnace, the heat of the furnace bakes the paste in situ — no separate baking or graphitization step needed. The casing progressively softens and burns away at the lower end. This avoids the electrode manufacturing bottleneck entirely at the cost of lower electrode quality and higher consumption.

### Electrode Consumption Rates

| Furnace Type | Electrode | Consumption Rate | Notes |
|-------------|-----------|-----------------|-------|
| EAF steelmaking | Graphite (HP) | 2-3 kg/t steel | Premium needle coke, high-power operation |
| EAF steelmaking | Graphite (RP) | 3-5 kg/t steel | Regular coke, standard power |
| EAF steelmaking | Amorphous carbon | 5-15 kg/t steel | Pre-graphitization bootstrap phase |
| SAF silicon | Graphite | 30-60 kg/t Si | Continuous operation, high temperatures |
| SAF ferroalloys | Søderberg paste | 20-40 kg/t product | Self-baking, no pre-manufacture needed |
| SAF calcium carbide | Graphite | 25-40 kg/t CaC₂ | Abrasive charge, high tip erosion |

### Machining and Nipple Connection

Finished electrodes are machined to precise tolerances:
- **External threading**: Tapered threads are cut or machined into each end of the electrode. Thread profile: 3 or 4 pins per inch (large electrodes), 6-8 pins per inch (small electrodes). Threads must be accurate to ±0.1 mm for proper seating.
- **Nipples**: Short graphite pins with matching tapered threads on both ends connect two electrodes together. Nipples are machined from a single block of high-strength graphite. The nipple acts as the mechanical and electrical connection between electrode columns. Nipple breakage is a common failure mode — it must be stronger than the electrode body.
- **Column assembly**: Electrodes are screwed together into columns 3-15 m long (depending on furnace size and consumption rate). Each column is lowered into the furnace as the lower end is consumed, with new electrodes added at the top. A pin wrench or power tong tightens the connection (torque: 500-3000 N·m depending on electrode size).

### Safety and Hazards

- **Coal tar pitch fumes**: Coal tar pitch contains polycyclic aromatic hydrocarbons (PAHs), which are carcinogenic. Mixing, extrusion, and baking areas must be ventilated. Workers must wear respiratory protection. Skin contact with hot pitch causes severe burns and chemical absorption.
- **Dust explosions**: Fine carbon dust (coke fines, pitch dust) is combustible and can form explosive dust clouds. Ventilate all grinding, milling, and mixing areas. Eliminate ignition sources. Dust collection systems with explosion relief.
- **Carbon monoxide**: The baking and graphitization processes produce CO and other gases. Gas collection and flaring systems are essential for worker safety and environmental control.
- **Electrical hazards**: Graphitization pits operate at 50-200 kA and very low voltage (5-20V). The current is lethal. Barricade the area. Ground all equipment. Insulated tools only.
- **Thermal hazards**: Green electrodes are hot (~140°C) after extrusion. Baked electrodes come out of the furnace at 800-1200°C. Graphitized electrodes cool from 3000°C. Appropriate heat-resistant PPE and handling equipment (tongs, crane) required at every stage.

### Cross-References

- **Electric arc and submerged arc furnaces using electrodes**: [electric-furnaces.md](electric-furnaces.md)
- **Silicon production consuming electrodes**: [mg-si-production.md](../silicon/mg-si-production.md)
- **Coal tar pitch source**: [coke.md](coke.md)
- **Petroleum refining source for coke**: [fuels.md](fuels.md)

---

*Part of the [Bootciv Tech Tree](../) • [Energy](./) • [All Domains](../)*
