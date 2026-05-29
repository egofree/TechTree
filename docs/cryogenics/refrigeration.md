# Refrigeration Fundamentals

> **Node ID**: cryogenics.refrigeration
> **Domain**: Cryogenics
> **Dependencies**: None (root capability)
> **Enables**: [`cryogenics.air-separation`](air-separation.md), [`cryogenics.liquefaction-storage`](liquefaction-storage.md)
> **Timeline**: Years 20-30
> **Outputs**: refrigeration_cycles, cryogenic_cooling, expansion_engines
> **Critical**: No — refrigeration enables cryogenics and food preservation but is not a direct semiconductor process

### Overview

Refrigeration is the active removal of heat from a region to maintain its temperature below that of the surroundings. Every refrigeration system moves heat against its natural direction of flow (hot→cold) by expending work. This file covers the thermodynamic principles and cycle architectures that enable cooling from ambient temperature down to cryogenic temperatures (-150°C and below).

The progression from industrial refrigeration (0 to -40°C) to cryogenics (-150 to -270°C) is not merely a matter of "more of the same." Below approximately -150°C, the thermodynamic and material constraints change qualitatively: ordinary refrigerants condense or freeze, heat capacities drop, thermal contractions become severe, and insulation requirements become dominant. Understanding these transitions is essential for designing systems that operate reliably at cryogenic temperatures.

### Thermodynamic Principles

**Second Law and the Carnot limit**: A refrigerator is a heat engine operating in reverse. The minimum work required to extract heat Q_C from a cold reservoir at temperature T_C and reject it to a hot reservoir at T_H is given by the Carnot coefficient of performance: COP_Carnot = T_C / (T_H - T_C). For a freezer at -20°C (253 K) rejecting heat to a 30°C (303 K) environment: COP_Carnot = 253/50 = 5.06. For a cryogenic system at -180°C (93 K) rejecting to 303 K: COP_Carnot = 93/210 = 0.44. This 11× reduction in theoretical efficiency explains why cryogenic refrigeration is so energy-intensive — each degree of cooling below ambient becomes progressively more expensive in terms of work input.

**Enthalpy and entropy in refrigeration**: A refrigeration cycle exploits the enthalpy change of a working fluid as it undergoes phase changes (evaporation absorbs heat, condensation releases heat) and pressure changes (expansion cools, compression heats). The choice of working fluid determines the temperature range over which the cycle operates effectively. At cryogenic temperatures, the working fluids are gases (nitrogen, helium, hydrogen) rather than conventional refrigerants.

**Inversion temperature and Joule-Thomson effect**: Real gases do not obey the ideal gas law exactly. When a real gas expands through a throttle (porous plug or valve) at constant enthalpy (isenthalpic expansion), its temperature changes. Whether the gas cools or heats depends on whether the initial temperature is below or above the gas's Joule-Thomson inversion temperature:
- **Nitrogen**: Inversion temperature ~350°C (623 K). Below this, J-T expansion cools the gas. At room temperature, N₂ always cools on J-T expansion.
- **Oxygen**: Inversion temperature ~770°C (1043 K). Always cools from room temperature.
- **Hydrogen**: Inversion temperature ~-68°C (205 K). Must be pre-cooled below -68°C before J-T expansion will produce further cooling. This is why hydrogen liquefaction requires liquid nitrogen pre-cooling.
- **Helium**: Inversion temperature ~-233°C (40 K). Must be pre-cooled with liquid hydrogen before J-T expansion works. Helium liquefaction is the most demanding cryogenic process.

The magnitude of the J-T temperature drop is modest — typically 0.2-0.5°C per atmosphere of pressure drop for air at room temperature. J-T cooling alone cannot reach cryogenic temperatures in a single stage; it must be combined with heat exchangers in a countercurrent arrangement (the Linde cycle) to accumulate the temperature drop over many passes.

### Vapor-Compression Refrigeration Cycle

The workhorse of industrial refrigeration. Operates between approximately +10°C and -40°C (with special refrigerants, down to -80°C for cascade systems).

**The four stages**:

1. **Compression** (1→2): Low-pressure vapor refrigerant enters the compressor. Mechanical work raises the pressure from evaporator pressure P_low to condenser pressure P_high (typically 3-15 bar). The compression is approximately isentropic (adiabatic and reversible), so the gas heats significantly: from perhaps -10°C at the evaporator outlet to 60-80°C at the compressor discharge. Compressor types: reciprocating (piston) for small-medium systems, rotary screw for medium-large, centrifugal for large industrial (100 kW to 10+ MW).

2. **Condensation** (2→3): The hot, high-pressure vapor enters the condenser — a heat exchanger cooled by ambient air, cooling water, or evaporative cooling. The refrigerant condenses from vapor to liquid at constant pressure, rejecting its latent heat of condensation to the surroundings. Condensing temperature is typically 10-20°C above ambient: 40-50°C for air-cooled, 30-35°C for water-cooled. The refrigerant exits as a high-pressure subcooled liquid.

3. **Expansion** (3→4): The high-pressure liquid passes through a throttling device (expansion valve, capillary tube, or orifice). This is an isenthalpic expansion — the fluid does no work. The pressure drops from P_high to P_low, and the temperature drops correspondingly. A portion of the liquid flashes to vapor (flash evaporation). For example, ammonia at 12 bar and 35°C expanding to 2 bar produces a two-phase mixture at approximately -20°C.

4. **Evaporation** (4→1): The cold, low-pressure two-phase mixture enters the evaporator — the heat exchanger in the space being cooled. The liquid portion evaporates by absorbing heat from the surroundings (the refrigerated space, or brine, or process stream). The evaporation occurs at constant pressure and constant temperature (for a pure refrigerant). The refrigerant exits as a low-pressure superheated vapor and returns to the compressor.

**Coefficient of Performance**: For an ideal (Carnot) refrigerator operating between -20°C and 35°C: COP = 253/(308-253) = 4.6. Real vapor-compression systems achieve COP of 2.0-3.5 depending on temperature lift, compressor efficiency (60-80% isentropic), and heat exchanger effectiveness. The gap from Carnot is due to: finite temperature differences in heat exchangers (5-10°C approach), pressure drops in piping, compressor inefficiency, and throttling losses in the expansion valve.

**Strengths:**
- Mature technology with COP of 2.0-3.5 (20-35% of Carnot), proven reliable in millions of installations with 10-20 year service life
- Ammonia refrigerant (R-717) has excellent thermodynamic properties (high latent heat of vaporization at 1,370 kJ/kg) and low cost

**Weaknesses:**
- COP drops sharply as temperature lift increases — refrigerating to -40°C from 35°C ambient gives COP ~1.0-1.5 (high energy cost per unit of cooling)
- Ammonia is toxic (IDLH 300 ppm) and flammable at 15-28% in air; leaks in enclosed spaces are life-threatening

**Refrigerant selection**:
- **Ammonia (NH₃, R-717)**: Excellent thermodynamic properties (high latent heat, low molecular weight). Boiling point -33°C at 1 atm. Toxic and flammable but has a characteristic pungent odor that provides early warning. Standard for industrial refrigeration (cold storage, ice production, chemical plants). Cannot be used with copper (forms complexes) — steel piping required.
- **Carbon dioxide (CO₂, R-744)**: Boiling point -57°C at 5.2 bar (requires high-pressure operation). Non-flammable, non-toxic, environmentally benign (GWP = 1). Transcritical CO₂ systems achieve -50°C for frozen food. High operating pressure (40-100 bar transcritical) demands robust equipment.
- **Sulfur dioxide (SO₂, R-764)**: Historically important (early refrigeration), boiling point -10°C. Toxic and corrosive. Superseded by safer refrigerants but accessible in a bootstrap context as a byproduct of sulfuric acid production.

### Absorption Refrigeration

An alternative to vapor-compression that uses heat energy rather than mechanical work to drive the refrigeration cycle. Important because it can use waste heat, solar thermal, or geothermal energy — no electricity or mechanical compressor required.

**Principle**: A refrigerant is absorbed by an absorbent at low pressure, pumped to high pressure as a liquid (requires far less work than compressing a gas), then driven out of solution by heat at high pressure, condensed, expanded, and evaporated to produce cooling.

**Ammonia-water system (NH₃/H₂O)**:
- **Generator**: Heat the strong ammonia-water solution (40-60% NH₃) to 100-150°C. Ammonia vapor boils off at high pressure (~10-15 bar).
- **Condenser**: Ammonia vapor condenses to liquid at ~40°C (rejecting heat to ambient). High-pressure liquid NH₃.
- **Expansion valve**: Liquid NH₃ throttles to low pressure (~2 bar), temperature drops to ~-20°C.
- **Evaporator**: Cold liquid NH₃ evaporates, absorbing heat from the refrigerated space.
- **Absorber**: NH₃ vapor from the evaporator is absorbed by the weak solution returning from the generator. The absorption reaction is exothermic — heat must be removed (cooling water). The resulting strong solution is pumped back to the generator.
- **Solution pump**: Pumps liquid (not gas) from low to high pressure — requires only 1-2% of the total energy input (the rest is heat).
- **COP**: 0.5-0.7 (single-effect). Low but uses cheap heat. A double-effect system (using the condenser heat to drive a second generator) achieves COP 1.0-1.2.

**Strengths:**
- Uses waste heat (100-150°C) instead of mechanical work — the solution pump consumes only 1-2% of total energy input, enabling operation from solar thermal or geothermal sources
- No compressor means fewer moving parts, lower maintenance, and quieter operation than vapor-compression systems

**Weaknesses:**
- COP of 0.5-0.7 is far below vapor-compression (2.0-3.5), requiring 3-6× more heat energy for the same cooling effect
- Ammonia-water system operates with toxic ammonia refrigerant — leaks pose inhalation hazards and the generator operates at 100-150°C with associated burn risks

### Cascade Refrigeration

When a single refrigerant cannot span the required temperature range (too low evaporator pressure or too high condenser pressure), cascade systems couple two or more refrigeration cycles operating with different refrigerants.

**Two-stage cascade**:
- **High-temperature stage**: Standard vapor-compression cycle operating from, say, +40°C condensing to -15°C evaporating. Uses R-404A or similar.
- **Low-temperature stage**: Vapor-compression cycle operating from -10°C condensing to -60°C evaporating. Uses R-23 or ethylene (boiling point -104°C).
- **Cascade condenser**: The evaporator of the HT stage cools the condenser of the LT stage. Heat removed from the LT condenser is absorbed by the HT evaporator, creating a thermal bridge between the two independent cycles.
- **Temperature range**: Two-stage cascade covers +40°C to -60°C. Three-stage cascade (adding a methane cycle, bp -161°C) extends to -120°C. Four-stage (adding nitrogen) reaches -180°C.

**Autocascade (mixed-refrigerant) system**: A single compressor circulates a mixture of refrigerants with progressively lower boiling points. A series of phase separators separates the mixture by boiling point — the highest-boiling component condenses first and provides the warmest refrigeration stage, while the lowest-boiling component provides the coldest stage. Simpler mechanically (one compressor) but more complex thermodynamically. Used in small cryocoolers for laboratory and medical applications (reaching -150°C to -196°C with a single compressor).

**Strengths:**
- Each stage uses a refrigerant optimized for its temperature range, avoiding the poor performance of a single refrigerant pushed beyond its design envelope
- Three-stage cascade extends reach to -120°C; four stages reach -180°C, approaching cryogenic territory from conventional refrigeration technology

**Weaknesses:**
- Each additional stage adds a complete compressor-condenser-evaporator assembly, roughly doubling cost and complexity per stage
- The cascade condenser (thermal bridge between stages) is a single point of failure — loss of the high-temperature stage stops the entire system

### Joule-Thomson and Linde Cycle

The Joule-Thomson (J-T) effect alone produces only a small temperature drop per stage. The Linde cycle (developed by Carl von Linde, 1895) multiplies this drop by combining J-T expansion with countercurrent heat exchange.

**Linde-Hampson cycle (single-column)**:
1. Compress gas to high pressure (100-200 bar) at near-ambient temperature.
2. Pass through a countercurrent heat exchanger: warm high-pressure gas flows opposite to cold low-pressure gas returning from the expansion valve.
3. After pre-cooling in the heat exchanger, throttle the high-pressure gas through a J-T valve to low pressure (~1 bar). Temperature drops by ΔT ≈ μ_JT × ΔP.
4. The partially liquefied gas separates: liquid collects in a receiver, unliquefied cold vapor returns through the heat exchanger, cooling the incoming warm gas.
5. Over successive passes, the returning cold stream progressively cools the incoming gas until the temperature at the J-T valve reaches the gas's boiling point and liquid begins to accumulate.

**Linde dual-pressure cycle**: Improves efficiency by splitting the gas stream. Only a portion (~30-50%) is expanded from full pressure to atmospheric; the remainder is expanded to an intermediate pressure and recycled, reducing the compressor work per unit of liquefaction. Typical improvement: 30-50% reduction in specific energy consumption.

**Limitations of J-T cooling**: The temperature drop per unit pressure drop is small for most gases at practical pressures. The Linde cycle requires high pressures (100-200 bar) and achieves thermodynamic efficiencies of only 5-10% of Carnot. Despite this, it remains widely used because of its mechanical simplicity — the cold box has no moving parts.

**Strengths:**
- No moving parts in the cold box (only a throttle valve and heat exchanger) — extremely reliable for continuous unattended operation
- Countercurrent heat exchanger accumulates small J-T drops into a large total temperature reduction over many passes, enabling liquefaction from ambient temperature

**Weaknesses:**
- Requires 100-200 bar operating pressure — high-pressure equipment is expensive and poses significant safety hazards (stored energy in compressed gas)
- Thermodynamic efficiency of only 5-10% of Carnot means 10-20× more energy input than the theoretical minimum per kg of liquefied gas

### Claude Cycle and Expansion Engines

The Claude cycle (developed by Georges Claude, 1902) replaces (or supplements) J-T expansion with an expansion engine (expander). This dramatically improves efficiency.

**Principle**: When a gas expands adiabatically while doing work (turning a turbine wheel or driving a piston), it cools much more than in a simple J-T expansion (where no work is extracted). The isentropic expansion produces a temperature drop: T₂/T₁ = (P₂/P₁)^((γ-1)/γ), where γ is the ratio of specific heats (1.4 for air). For air expanding from 6 bar at -100°C to 1 bar: T₂ = 173 × (1/6)^(0.286) = 173 × 0.65 = 112 K (-161°C). The J-T expansion from the same conditions would cool only to about 150 K (-123°C) — the expansion engine produces nearly three times the temperature drop.

**Claude cycle configuration**:
1. Compress air to 20-40 bar (lower than Linde's 100-200 bar).
2. Pre-cool in countercurrent heat exchanger to approximately -100°C.
3. Split the stream: ~70-80% continues to the distillation column; ~20-30% enters the expansion turbine.
4. The expansion turbine expands this portion from ~20 bar to ~1 bar, cooling it to -160°C or below. The turbine shaft work drives a generator or assists the main compressor (energy recovery).
5. The cold expanded gas returns through the low-pressure side of the heat exchanger, providing refrigeration to cool the incoming high-pressure stream.

**Expansion turbine design**:
- **Radial inflow turbine** (most common): Gas enters at the periphery of the wheel and exits at the center. Compact, efficient, well-suited to the small flow rates and high pressure ratios of cryogenic service. Wheel diameter: 80-200 mm. Speed: 20,000-80,000 RPM. Isentropic efficiency: 80-88%.
- **Bearings**: Oil-lubricated (requires sealed bearings with shaft seals to prevent oil contamination of process gas) or gas-lubricated (the process gas itself forms the bearing film — no oil needed, but requires very tight clearances and precise balancing).
- **Power recovery**: The turbine produces 100-5000 kW depending on plant size. This power is typically used to drive a booster compressor on the main air feed, reducing the net power input to the plant by 5-10%.

**Comparison: Linde vs Claude cycles**:
| Parameter | Linde (J-T only) | Claude (expander) |
|-----------|-------------------|-------------------|
| Operating pressure | 100-200 bar | 20-40 bar |
| Specific energy (kWh/kg liquid air) | 3-5 | 0.8-1.5 |
| Moving parts in cold box | None (valves only) | Expansion turbine |
| Thermodynamic efficiency | 5-10% of Carnot | 15-25% of Carnot |
| Mechanical complexity | Low | Moderate |
| Cold start-up time | 8-24 hours | 4-12 hours |

The Claude cycle is standard for all modern air separation plants larger than ~50 tonnes/day. The Linde cycle remains used in small liquefiers and laboratory-scale systems where mechanical simplicity outweighs energy cost.

**Strengths:**
- Claude cycle achieves 15-25% of Carnot efficiency (vs. 5-10% for Linde), reducing specific energy by 60-70% for the same liquefaction output
- Lower operating pressure (20-40 bar vs. 100-200 bar for Linde) reduces equipment cost and safety risk

**Weaknesses:**
- Expansion turbine at 20,000-80,000 RPM requires precision machining and high-quality bearings — a significant manufacturing capability threshold
- Turbine wheel failure at operating speed releases fragments with high kinetic energy, requiring blast-resistant containment

### Stirling Cycle Cryocoolers

The Stirling cycle achieves cryogenic temperatures in a single closed-cycle machine with no valves. Used for small-scale cryogenic cooling (1-100 W at 20-80 K) — ideal for cooling infrared detectors, superconducting devices, and small cryostats.

**Configuration**: A displacer piston and a power piston driven by the same crankshaft, with a regenerator (porous matrix of fine wire mesh or packed spheres) between the compression and expansion spaces.

**Cycle**:
1. **Compression**: The power piston compresses gas in the compression space (near ambient temperature). Heat of compression is rejected to cooling water or fins.
2. **Transfer**: The displacer moves gas from the compression space through the regenerator to the expansion space. The regenerator stores heat from the gas, cooling it.
3. **Expansion**: The gas expands in the expansion space (at the cold end), doing work on the piston and producing cooling. The cold space absorbs heat from the load.
4. **Return transfer**: The displacer returns gas through the regenerator from expansion space to compression space. The regenerator returns stored heat to the gas.

**Performance**: Achieves 40-80 K (liquid nitrogen range) with COP of 5-10% of Carnot. Cooling capacity 1-100 W. Compact and reliable (some Stirling cryocoolers run 10,000+ hours continuously). Limited to relatively small cooling loads.

**Strengths:**
- Single closed-cycle machine with no valves — few wear surfaces and proven 10,000+ hour continuous operation
- Regenerator (porous matrix) stores and releases heat each cycle, providing effective heat pumping in a compact package

**Weaknesses:**
- Cooling capacity limited to 1-100 W — cannot liquefy bulk gases or cool large loads
- Displacer piston at the cold end generates vibration that can interfere with sensitive instrumentation (SQUIDs, infrared detectors)

### Pulse Tube Refrigerators

A refinement of the Stirling concept that eliminates the displacer piston from the cold end. Only the compression piston (at ambient temperature) moves — the "pulse tube" section has no moving parts at cryogenic temperature.

**Principle**: Pressure oscillations from the compressor drive gas oscillations in the pulse tube. Phase shifting between pressure and mass flow (achieved by orifice and reservoir) creates a net enthalpy flow from cold to hot end, producing refrigeration.

**Advantages over Stirling**: No displacer → no cold-end moving parts → lower vibration, higher reliability, longer mean time between failures. Critical for cooling sensitive instrumentation (space telescopes, MRI magnets).

**Performance**: Achieves temperatures down to 20-30 K (single stage) or 4 K (two-stage with helium). Cooling capacity 0.1-10 W. COP slightly lower than Stirling due to orifice losses.

**Strengths:**
- No moving parts at the cold end — eliminates cold-end wear and vibration, achieving MTBF >50,000 hours for space applications
- Cold head can be separated from the compressor by several meters of flexible hose, simplifying integration into existing systems

**Weaknesses:**
- COP slightly lower than Stirling due to orifice and reservoir losses — typically 3-7% of Carnot vs. 5-10% for Stirling
- Cooling capacity limited to 0.1-10 W — suitable only for instrument cooling, not bulk liquefaction

### Gifford-McMahon Cryocoolers

A variant using a pressure swing (valved) cycle rather than the continuous oscillation of Stirling/pulse tube systems. Uses a standard commercial compressor at room temperature connected by flexible hoses to the cold head.

**Cycle**: Pressurize the cold head from the compressor → displace gas to the cold end through the regenerator → close high-pressure valve, open low-pressure valve → gas expands in the cold space → open the exhaust valve, displace gas back through the regenerator to the warm end.

**Performance**: 10-80 K, 1-500 W cooling. Slower than Stirling (1-5 Hz valve cycling vs 30-60 Hz Stirling) but uses standard oil-lubricated compressors (much cheaper and more reliable). The cold head can be separated from the compressor by several meters of flexible hose, simplifying installation.

**Strengths:**
- Uses standard oil-lubricated compressors (commodity HVAC components) — far cheaper and more reliable than specialized gas bearings or dry-running compressors
- Cold head separated from compressor by flexible hoses allows installation in constrained spaces and simplifies maintenance

**Weaknesses:**
- Slower cycle rate (1-5 Hz) produces temperature oscillations of 1-5 K at the cold end, problematic for temperature-sensitive loads
- Valve sequencing mechanism adds mechanical complexity and is the most common failure point in G-M cryocoolers

### Kapitza Cycle and Further Optimizations

The Kapitza cycle (Peter Kapitza, 1939) further optimizes the Claude cycle by using a low-pressure ratio (4-6 bar to 1 bar) with a highly efficient expansion turbine and very effective countercurrent heat exchangers (temperature approach <2°C at the cold end). This reduces thermodynamic irreversibilities and brings the specific energy consumption closer to the Carnot limit.

**Key innovations**:
- Very tight temperature approach in heat exchangers (1-3°C vs 5-10°C in earlier designs)
- Use of turbocompressors (more efficient than reciprocating at large scale)
- Thermal coupling of the lower and upper distillation columns (the condenser-reboiler arrangement)
- Recovery of turbine shaft work to drive booster compressors

**Achievable performance**: Modern Kapitza-cycle air separation plants achieve specific energy consumption of 0.35-0.45 kWh/Nm³ O₂ (gas product) — within 10-15% of the theoretical minimum of 0.06 kWh/Nm³.

**Strengths:**
- Achieves 10-15% of Carnot limit — best-in-class for large-scale air separation, saving millions of kWh/year versus Claude cycle
- Recovery of turbine shaft work to drive booster compressors reduces net power input by 5-10%

**Weaknesses:**
- Requires turbocompressors and very tight heat exchanger approaches (<2°C), demanding precision manufacturing not available in early bootstrap stages
- Optimal only at large scale (>1,000 t/d O₂); small plants cannot justify the complexity

### Material Considerations at Low Temperatures

**Brittle transition**: Many common engineering metals become brittle at cryogenic temperatures. Mild steel becomes dangerously brittle below approximately -20°C. A mild steel vessel containing liquid nitrogen (-196°C) could shatter from a minor impact. Materials that remain ductile at cryogenic temperatures:
- **Austenitic stainless steel** (304, 304L, 316, 316L): Remain ductile to -270°C. The standard material for cryogenic vessels, piping, and internals. Thermal conductivity is relatively low (14-16 W/m·K at room temperature, dropping to ~8 W/m·K at 77 K), which helps limit heat leak.
- **Copper**: Excellent thermal conductor (400 W/m·K at room temperature, ~600 W/m·K at 20 K). Used for heat exchange surfaces, thermal straps, and thermal grounding. Becomes stronger at low temperatures. Expensive.
- **Aluminum** (6061-T6, 1100): Good thermal conductor (170 W/m·K at RT, ~300 W/m·K at 77 K). Lower density than steel. Good for heat exchanger fins. Weldability is excellent. However, 6061-T6 loses some strength below -200°C; 5083 and 1100 are preferred for the coldest applications.
- **9% nickel steel**: Developed specifically for cryogenic service. Retains toughness to -196°C at lower cost than stainless steel. Used for large cryogenic storage tanks (LOX, LIN, LNG). Requires careful welding with nickel-based filler metal.

**Thermal contraction**: Metals contract significantly when cooled from ambient to cryogenic temperatures:
- Stainless steel 304: 0.29% from 293 K to 77 K (approximately 3 mm per meter)
- Aluminum: 0.39% from 293 K to 77 K (approximately 4 mm per meter)
- Copper: 0.30% from 293 K to 77 K (approximately 3 mm per meter)

This contraction has major design implications: long runs of cryogenic piping must have expansion loops or bellows, supports must allow sliding, and differential contraction between dissimilar metals creates stresses at joints.

**Strengths:**
- Austenitic stainless steels (304L, 316L) remain ductile to -270°C with no ductile-to-brittle transition, enabling safe pressure vessel construction at all cryogenic temperatures
- Copper's thermal conductivity increases at low temperatures (~600 W/m·K at 20 K), making it ideal for thermal straps and heat exchange surfaces

**Weaknesses:**
- Carbon steel becomes brittle below -20°C — catastrophic brittle fracture risk makes it unsuitable for any cryogenic service
- Differential thermal contraction between dissimilar metals (e.g., stainless steel at 0.29% vs. aluminum at 0.39%) creates shear stresses at brazed or bolted joints that can cause fatigue failure over thermal cycles

### Thermometry at Cryogenic Temperatures

**Resistance temperature detectors (RTDs)**: Platinum RTDs (Pt100, Pt1000) are accurate from -200°C to +600°C. Below -200°C, sensitivity drops. Carbon-glass and rhodium-iron RTDs extend to 1 K.

**Thermocouples**: Type T (copper-constantan) works from -200°C to +350°C with ±0.5°C accuracy. Type E (chromel-constantan) provides higher sensitivity at low temperatures. Type K is unreliable below -180°C (inhomogeneity errors).

**Silicon diode thermometers**: Forward voltage drop of a silicon diode changes linearly with temperature below ~100 K. Accuracy ±0.5 K from 1 K to 400 K. Simple two-lead measurement. Standard for laboratory cryogenics.

**Strengths:**
- Platinum RTDs (Pt100) provide ±0.1°C accuracy from -200°C to +600°C with excellent long-term stability and no reference junction needed
- Silicon diode thermometers cover the full range from 1 K to 400 K with a simple two-lead measurement and ±0.5 K accuracy

**Weaknesses:**
- Thermocouples require a reference junction (ice point or electronic compensation) and are susceptible to inhomogeneity errors from cold-working of the wires
- No single sensor technology covers the entire range from 1 K to 600 K — multi-sensor installations are required for systems spanning wide temperature ranges

### Energy Requirements by Temperature Range

| Target Temperature | Typical Cycle | Specific Energy (kWh/kg) | COP (% of Carnot) |
|-------------------|---------------|-------------------------|--------------------|
| -20°C (253 K) | Vapor-compression (NH₃) | 0.02-0.05 | 30-40% |
| -80°C (193 K) | Two-stage cascade | 0.05-0.15 | 15-25% |
| -150°C (123 K) | Three-stage cascade | 0.2-0.5 | 8-15% |
| -183°C (90 K) LOX | Claude cycle ASU | 0.4-0.8 | 5-10% |
| -196°C (77 K) LIN | Claude cycle liquefier | 0.5-1.2 | 5-10% |
| -253°C (20 K) LH₂ | Pre-cooled Claude + J-T | 5-15 | 2-5% |
| -269°C (4 K) LHe | Collins cycle | 30-100 | 0.5-2% |

### Safety

**Cryogenic burns**: Contact with surfaces below -40°C causes tissue freezing identical to thermal burns. LN₂ (-196°C) causes instantaneous frostbite on skin contact. Always wear insulated gloves, face shield, and closed-toe shoes. Never touch uninsulated cryogenic piping.

**Oxygen deficiency**: LN₂ expands 694:1 on evaporation. One liter of LN₂ produces 694 liters of nitrogen gas, displacing oxygen. At <19.5% O₂, impaired judgment; at <10% O₂, unconsciousness within seconds. Continuous O₂ monitoring mandatory in all enclosed cryogenic work areas.

**Oxygen enrichment**: LOX (-183°C) boils at a lower temperature than LIN (-196°C). In an open dewar of liquid air, nitrogen boils off preferentially, concentrating oxygen in the remaining liquid. A partially evaporated dewar of liquid air can contain >50% liquid oxygen — a severe fire hazard if it contacts organic materials.

### See Also

- **[Cryogenic Air Separation](air-separation.md)**: Application of Claude cycle to produce N₂, O₂, Ar
- **[Gas Liquefaction & Storage](liquefaction-storage.md)**: Dewar design, cold boxes, insulation
- **[Cooling Systems & Refrigeration](../energy/index.md)**: Non-cryogenic industrial cooling
- **[Basic Gas Handling](../gas-handling/basic.md)**: Gas compression and purification infrastructure
- **[Air Separation & Bulk Gas Production](../chemistry/air-separation.md)**: ASU process and product specifications

---

*Part of the [Bootciv Tech Tree](../index.md) • [Cryogenics](./index.md) • [All Domains](../index.md)*
