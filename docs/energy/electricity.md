# Electricity Generation & Distribution

> **Node ID**: energy.electricity
> **Also covers**: `chemistry.electrolysis`, `machine-tools.joining`
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`machine-tools`](../machine-tools/index.md), [`metals.iron-steel`](../metals/iron-steel.md), [`chemistry.petroleum-alternatives`](../chemistry/petroleum-alternatives.md)
> **Enables**: [`energy.electric-furnaces`](electric-furnaces.md), [`chemistry.electrolysis`](../chemistry/electrolysis.md), [`machine-tools.joining`](../machine-tools/joining.md), [`silicon.mg-si-production`](../silicon/mg-si-production.md), [`chemistry.air-separation`](../chemistry/air-separation.md), [`chemistry.dopant-etch-gases`](../chemistry/dopant-etch-gases.md), [`chemistry.hydrogen-silane`](../chemistry/hydrogen-silane.md)
> **Timeline**: Years 15-30
> **Outputs**: generators, motors, transformers, wire_cables, electricity, insulated_wire, electric_arc_furnaces, resistance_heaters, eaf_steel, internal_combustion_engines, ...

### Electricity Generation

**[Voltaic piles / batteries](../glossary/voltaic-piles-batteries.html)** (first electrical source):
- **Construction**: Stack alternating disks: copper plate → cardboard soaked in brine (or sulfuric acid) → zinc plate → repeat. 10-20 cells produce 10-20V DC at low current.
- **Output**: ~1V per cell, ~50-100 mA. Sufficient for early electroplating experiments, telegraph operation, electrochemistry exploration. Not sufficient for industrial power.
- **[Daniell cell](../glossary/daniell-cell.html)** (improved): Copper electrode in CuSO₄ solution, separated by porous pot from zinc electrode in ZnSO₄ or dilute H₂SO₄. 1.1V, more stable voltage, longer life. Standard for telegraph systems.

**[Wire drawing](../glossary/wire-drawing.html)** (essential for all electrical work):
- **Starting material**: Cast copper ingot, hot-forged to rod (~10 mm diameter), then cold-drawn.
- **Drawing process**: Pull copper rod through successively smaller hardened steel dies (tungsten carbide or tool steel). Each pass reduces diameter ~20-30%. Anneal between passes (heat to 400-600°C to restore ductility lost from cold work). Repeat until target gauge reached.
- **Common gauges**: 1 mm diameter for winding (≈ 18 AWG), 0.1 mm for fine coils (≈ 38 AWG). Length from 1 kg of copper: ~130 m at 1 mm diameter.
- **Lubrication**: Tallow or soap solution on wire as it enters die. Essential — without it, wire galls and snaps.
- **Insulation**: Dip drawn wire in rubber solution (natural rubber dissolved in naphtha), wrap with cotton thread, or varnish with shellac. Multiple layers for higher voltage. Gutta-percha (natural thermoplastic) for underwater/underground cables.

**[Generators](../glossary/generators.html)** (Faraday principle — rotating coil in magnetic field):
- **First generator (magneto)**: Permanent magnets (lodestones or magnetized steel bars) provide field. Rotating coil (armature) wound on iron core, turned by hand, water wheel, or steam engine. Output: pulsed DC.
- **Winding**: Copper wire, enamel or shellac insulated. Number of turns determines voltage. Wire gauge determines current capacity. Typical early generator: 500-2000 turns of 0.5-1 mm wire on iron core.
- **Commutator**: Split copper ring with brushes (carbon or copper gauze) to convert AC to DC. For AC generators (alternators): slip rings instead.
- **[Self-exciting generator](../glossary/self-exciting-generator.html)** (dynamo): Electromagnets (iron core + coil) replace permanent magnets for stronger field. Uses residual magnetism in iron to bootstrap, then feeds some output current back to field coils → positive feedback → full excitation.
- **Performance targets**: First generators: 100W-1kW. Mature dynamo: 1-50 kW. Efficiency 70-90%.

**[Motors](../glossary/motors.html)** (reverse of generators):
- **DC motor**: Current through armature coils in magnetic field creates torque. Commutator reverses current direction each half-turn for continuous rotation.
- **Series-wound**: Field and armature in series. High starting torque, speed varies with load. Good for traction (trams, trains, starter motors).
- **Shunt-wound**: Field and armature in parallel. More constant speed, lower starting torque. Good for machine tools, fans, pumps.
- **Construction**: Identical mechanical parts to generators — a dynamo run backwards as a motor.

**[Transformers](../glossary/transformers.html)** (voltage step-up/step-down):
- **Principle**: Two coils on shared iron core. Alternating current in primary creates changing magnetic flux, inducing voltage in secondary. Turns ratio determines voltage ratio (V₂/V₁ = N₂/N₁).
- **Construction**: Laminated iron core (thin iron sheets, 0.3-0.5 mm, insulated with shellac or paper — prevents eddy current losses). Primary and secondary windings of insulated copper wire.
- **Essential for**: Power distribution (step up voltage for transmission → lower current → less I²R loss in wires, step down at destination).

**Power distribution**:
- **[DC system](../glossary/dc-system.html)** (Edison): 110V DC. Limited range (~1-2 km) due to voltage drop in wires. Requires many small generators.
- **[AC system](../glossary/ac-system.html)** (Westinghouse/Tesla): 110-220V AC, stepped up to 1000-10000V for transmission, stepped down at load. Much longer range. Requires alternators and transformers. Eventually wins.
- **Wire sizing**: Copper wire, sized by current capacity. Rule of thumb: 3-5 A per mm² of cross-section for acceptable heating. Example: 10 A load at 110V over 100 m needs ~6 mm² wire (≈ 2.8 mm diameter) to keep voltage drop under 5%.

### Electric Furnaces

Electric arc furnaces, submerged arc furnaces, and resistance heating furnaces are covered in detail in [electric-furnaces.md](electric-furnaces.md), including construction, operation, power requirements, and electrode manufacturing. Electrode manufacturing specifics are in [electrode-manufacturing.md](electrode-manufacturing.md).

### Internal Combustion Engines

Otto-cycle piston engines, diesel engines, and their critical components (cylinders, pistons, crankshafts, carburetors, ignition systems) are covered in detail in [engine.md](engine.md). Power-to-weight ratios and aviation applications are discussed in [aviation.md](../transport/aviation.md).

### Electrolysis Foundations

**Electrolytic cells**:
- **Principle**: Pass DC current through ionic solution or molten salt → chemical decomposition at electrodes. Anode (+) attracts anions (oxidation). Cathode (-) attracts cations (reduction).
- **Power requirements**: DC supply (battery, dynamo, or rectified AC). Voltage 2-5V per cell (depends on reaction). Current 100-10,000+ A for industrial scale.
- **Cell construction**: Tank (lead-lined wood, concrete, or plastic), electrodes (carbon, lead, titanium), electrolyte (aqueous solution or molten salt), bus bars (copper or aluminum connecting electrodes to power supply).
- **Applications**:
  - **Chlor-alkali**: NaCl brine → Cl₂ (anode) + H₂ + NaOH (cathode). Diaphragm or membrane cell. Voltage ~3.5-4V. Current efficiency ~90-95%.
  - **Water electrolysis**: H₂O → H₂ (cathode) + ½O₂ (anode). Electrolyte: 25-30% KOH. Voltage ~1.8-2.2V. Produces ultra-pure gases.
  - **[Aluminum](../metals/aluminum.md)** (Hall-Héroult, later): Al₂O₃ dissolved in molten cryolite (Na₃AlF₆) at 950-1000°C. Carbon anodes. Aluminum deposits at carbon-lined cathode. 4-5V, 100,000+ A. ~13-15 kWh/kg Al. Requires enormous power.
  - **Copper refining**: Impure copper anode → pure copper cathode (99.99%) in CuSO₄/H₂SO₄ electrolyte. Voltage ~0.3V. Gold, silver, platinum collect in anode slimes — valuable byproducts.

### Wire Drawing Bootstrap

- **Chicken-and-egg problem**: you need wire for generators, but hardened steel dies for drawing that wire require decent steel, which itself needs powered machinery
- First wire: hammered or swaged copper rod pulled through hand-punched holes in hardened steel plates, iterating through successively smaller die openings
- Lubrication is critical at every pass (tallow or soap solution; see [Lubricants](../chemistry/lubricants.md)); without it the wire galls and snaps
- Wire annealing between passes restores ductility lost from cold working
- Insulation (rubber, varnished cloth, gutta-percha) is applied after drawing, not during

### Electrical Engineering Reference

**[Copper wire gauge table](../glossary/copper-wire-gauge-table.html)** (practical reference for all electrical work):
| Diameter (mm) | Cross-section (mm²) | Resistance (Ω/km) | Max current (A) | Typical use |
|---------------|---------------------|--------------------|-----------------|-------------|
| 0.1 | 0.008 | 2,200 | 0.05 | Fine coils, instruments |
| 0.2 | 0.031 | 560 | 0.15 | Meter movements |
| 0.5 | 0.20 | 88 | 1.0 | Small transformers |
| 1.0 | 0.79 | 22 | 5 | Motor windings, generator coils |
| 1.5 | 1.8 | 12 | 10 | Lighting circuits |
| 2.0 | 3.1 | 7.0 | 15 | Power outlets |
| 2.5 | 4.9 | 4.5 | 20 | Branch circuits |
| 4.0 | 12.6 | 1.7 | 40 | Sub-main feeds |
| 6.0 | 28.3 | 0.77 | 70 | Main distribution |
| 10.0 | 78.5 | 0.28 | 130 | Service entrance, bus bars |

- Max current assumes 3-5 A/mm² for enclosed wiring (derate for bundling or high ambient temperature). Open air or short runs can carry more.
- Voltage drop: ΔV = I × R = I × (ρ × L / A), where ρ = 0.0175 Ω·mm²/m for copper, L = length (m), A = cross-section (mm²). Keep voltage drop under 3-5% for efficient operation.
 - Example: 10 A load, 100 m run, 110V supply, max 5% drop (5.5V): Wire resistance = 5.5V / 10A = 0.55Ω. R per conductor = 0.275Ω for 100m = 2.75 Ω/km. From table: ~2.0 mm diameter wire (1.8 mm² cross-section, 12 Ω/km × 0.1 km = 1.2 Ω per conductor... need 2 conductors → 2.4 Ω total, voltage drop = 24V. Too much. Need 6 mm wire: 0.77 Ω/km × 0.1 km = 0.077 Ω per conductor → 0.154 Ω total → 1.54V drop = 1.4%. OK.)

**Motor and generator sizing**:
- **Motor power**: Mechanical power P = T × ω (torque × angular velocity). At 1500 RPM (157 rad/s), 1 Nm torque = 157W. A 1 kW motor at 1500 RPM delivers ~6.4 Nm.
- **Motor current**: I = P / (V × η × PF), where η = efficiency (0.7-0.9), PF = power factor (1.0 for DC, 0.7-0.85 for AC induction motors). Example: 1 kW motor at 220V AC, η=0.8, PF=0.8: I = 1000/(220 × 0.8 × 0.8) = 7.1A.
- **Generator sizing**: Must match peak load + 20% margin. If total connected load = 5 kW with 60% diversity factor (not all running simultaneously), generator needs 5 × 0.6 × 1.2 = 3.6 kW minimum. Round up to nearest available size.

**Fuse and circuit breaker selection**:
- **Fuse**: Short piece of wire or strip that melts at a known current, breaking the circuit. Lead-tin alloy for low-current fuses (1-15A), copper or silver for higher currents. Enclose in ceramic or glass tube with filler (sand) to quench arc when fuse blows. Rating: fuse should carry 100% rated current indefinitely, blow within 1 hour at 135% rated current, blow quickly at 200%+ rated current.
- **Fuse sizing**: Fuse rating ≥ full-load current of device, but ≤ ampacity of wiring. Example: motor drawing 7A on 2.5 mm² wire (20A capacity) → use 10A fuse. The fuse protects the WIRE, not the device.
- **Circuit breaker**: Bimetallic strip heated by current bends and trips latch, opening contacts. Resettable. More convenient than fuses. Calibrate by adjusting strip tension.

**[Battery sizing](../glossary/battery-sizing.html)** (lead-acid, see Energy Storage):
- **Capacity**: C = P × t / V, where P = load (W), t = backup time (hours), V = system voltage. Example: 500W load, 4-hour backup, 48V system: C = 500 × 4 / 48 = 41.7 Ah. Add 50% margin for depth-of- discharge limit: 62.5 Ah bank.
- **Charging current**: C/10 rate (capacity ÷ 10 hours) for maximum battery life. For 62.5 Ah bank: charge at ~6.25A, 48V = 300W charger needed. Charge time: ~12-14 hours from fully discharged.

### Permanent Magnets

- **[Lodestone](../glossary/lodestone.html)** (naturally magnetized magnetite) for early compasses and basic magnetic experiments
- **Magnetized iron/steel bars**: Stroke with lodestone or place in Earth's magnetic field yields magnets for early generator field poles and galvanometers. For stronger magnets: place steel bar inside coil, pass DC current (electromagnet method) — steel retains magnetism after current removed.
- **Keeper**: Store magnets with soft iron bar across poles (keeper) to prevent demagnetization over time.
 - **[Later materials](../glossary/later-materials.html)** (Alnico, ferrite) arrive with Chemistry stage alloy development

### Elastomer Processing

- **Natural rubber vulcanization**: latex from *Hevea brasiliensis* or temperate alternatives (guayule, Russian dandelion) is coagulated, masticated on a two-roll mill, then compounded with sulfur (1.5-3 phr) and zinc oxide as activator
- **[Heat curing](../glossary/heat-curing.html)** at 140-180°C in electric vulcanizing presses or steam autoclaves (3-10 bar) using the Energy stage electric heating and boiler steam; cycle times 5-30 minutes depending on thickness
- **Applications beyond wire insulation**: shaft seals, gaskets, flat belts and V-belts for power transmission, hoses, vibration dampers, and tire construction for wheeled vehicles
- **[Synthetic rubbers](../polymers/synthetic.md)** (nitrile, neoprene) require petrochemical feedstocks from [Petrochemicals](../chemistry/petroleum-alternatives.md); see [Polymers](../polymers/index.md) for the full elastomer development roadmap

### Advanced Welding

Oxy-acetylene welding and cutting, arc welding (stick/SMAW), joint preparation, and welding safety are covered in detail in [joining.md](../machine-tools/joining.md).

### Safety & Hazards

- **Electrocution**: Electrical current through the body causes death at surprisingly low levels — 100 mA across the chest can cause ventricular fibrillation. Even "low" voltages (50V+) can be lethal under wet conditions. ALWAYS de-energize circuits before working on them (lock-out/tag-out). Use insulated tools. One-hand rule when working near live circuits (keep one hand in pocket — prevents current across chest).
- **Arc flash**: Short circuits can produce arcs reaching 20,000°C. Arc blast pressure can throw a person across a room. Arc-rated face shield and flame-resistant clothing for any work on energized panels. Minimum approach distances based on voltage level.
- **High voltage**: Transformers and distribution systems operate at thousands of volts. Treat all high-voltage equipment as energized until proven otherwise. Grounding sticks for discharge before approach. Warning signs and barriers. Only qualified personnel near HV equipment.
- **Fire risk**: Electrical faults (short circuits, overloaded wiring, poor connections) are a leading cause of industrial fires. Proper fusing and circuit breakers on all circuits. No overloaded outlets. Inspect wiring for damage regularly.
- **Generator mechanical hazards**: Generators have rotating shafts and belts. Guard all moving parts. Entanglement hazard — no loose clothing near running generators.

### Power Transmission

Long-distance power transmission requires stepping voltage up at the generating station and back down at the load center. The physics is straightforward: power loss in transmission lines scales as I²R (current squared times resistance). For a given power delivery (P = V × I), doubling the voltage halves the current, and quartering the current reduces losses by a factor of 16. This makes high-voltage transmission essential for any plant more than a few kilometers from its load.

**Step-up transformer**: At the generating station, a transformer raises the generator output voltage (typically 2.4-13.8 kV) by a ratio of 10-15:1 to a transmission voltage of 11-400 kV. The transformer turns ratio determines the voltage ratio (V₂/V₁ = N₂/N₁). A 10:1 step-up on a 4.16 kV generator output produces 41.6 kV for transmission. Transformer efficiency at full load: 97-99%.

**Transmission line design**: Conductor material is almost always aluminum conductor steel reinforced (ACSR), where aluminum strands carry the current and a steel core provides tensile strength. Copper is too heavy and expensive for long spans. Conductor size is specified by cross-sectional area (25-400 mm² aluminum). Larger conductors carry more current with less loss but cost more and require stronger towers.

**Line loss calculation**: Power loss in a three-phase transmission line: P_loss = 3 × I² × R, where I is line current and R is the resistance of one conductor. For a 50 km line with 100 mm² ACSR conductor (R = 0.28 Ω/km per conductor) carrying 10 MW at 33 kV: I = 10,000,000 / (√3 × 33,000) = 175 A. P_loss = 3 × 175² × 0.28 × 50 = 1.29 MW. That is a 12.9% loss, high but tolerable for early systems. At 110 kV with the same power: I = 52.5 A, P_loss = 116 kW (1.2%), far more efficient.

**Transmission voltages**: 11 kV for short local distribution (<5 km), 33 kV for regional distribution (5-30 km), 66-110 kV for sub-transmission (20-80 km), 220-400 kV for long-distance bulk transmission (>50 km). Higher voltage requires taller towers, larger insulators, and greater clearance from vegetation and structures, but the reduction in conductor losses is dramatic.

**Voltage regulation**: Line voltage drops under load (I × R drop plus I × X reactive drop). At the load center, a step-down transformer reduces transmission voltage to distribution levels (3.3-11 kV), then further to utilization voltage (110-415 V). On-load tap changers on transformers adjust the turns ratio under load to compensate for voltage drop, maintaining ±5% voltage at the consumer.

### Electrical Insulation Classes

Electrical insulation degrades with temperature. The thermal class rating of insulation determines the maximum operating temperature and thus the power density achievable in motors, generators, and transformers:

| Insulation Class | Max Temperature | Common Materials | Typical Application |
|-----------------|----------------|------------------|-------------------|
| Class A | 105°C | Cotton, silk, paper, varnish | Small motors, instrument windings |
| Class E | 120°C | Enameled wire, polyester film | General-purpose motors |
| Class B | 130°C | Mica, glass fiber, polyester | Industrial motors, transformers |
| Class F | 155°C | Mica, glass fiber, silicone resin | High-performance motors |
| Class H | 180°C | Silicone elastomer, mica, glass | Traction motors, furnace motors |
| Class C | >220°C | Ceramics, PTFE, quartz | Specialized high-temp applications |

Hot-spot temperature must not exceed the class rating by more than 10°C for rated life (typically 20,000 hours). Every 8-10°C above rated temperature approximately halves insulation life (the "10-degree rule"). A Class B motor running at 145°C hotspot will survive roughly half as long as one running at 130°C.

### Ground Fault Protection

Ground faults occur when current leaks from a conductor to ground through an unintended path (damaged insulation, moisture, equipment frame contact). Left undetected, ground faults cause fires, equipment damage, and electrocution:

- **Residual current device (RCD/GFCI)**: Compares current in the line (outgoing) and neutral (return) conductors. If the difference exceeds a threshold (typically 30 mA for personnel protection, 300 mA for equipment protection), the device trips within 30-40 ms. Any current difference means current is returning through an alternative path (ground, human body, equipment frame).
- **Equipment grounding**: All exposed metal parts of electrical equipment are connected to a grounding conductor, which is bonded to earth at the service entrance (ground rod driven into soil, resistance <25 Ω to earth). A ground fault that energizes the equipment frame creates a low-impedance return path, causing high fault current that trips the overcurrent protective device (fuse or breaker) quickly.
- **Ground fault indicators**: For industrial systems with insulated neutrals (IT systems), a ground fault does not cause immediate trip but is indicated by a monitoring relay. This allows continued operation while the fault is located and repaired, important for continuous processes.

### Transmission Line Construction

Overhead transmission lines consist of conductors suspended from insulators on poles or towers. For the bootstrap, wooden pole construction is the most accessible:

- **Wooden poles**: Treated timber poles (preservative: creosote or pentachlorophenol) in lengths of 8-15 m, set 1.5-2.5 m into the ground. Span between poles: 40-100 m depending on conductor weight and terrain. Pole class is determined by the horizontal force at the top from conductor tension and wind loading.
- **Insulators**: Pin-type insulators (porcelain or glass, rated 11-33 kV) for lower voltages. Suspension insulators (discs of porcelain or tempered glass, each disc rated ~15 kV, linked in strings of 2-20 discs) for higher voltages. The number of discs in a string increases with voltage: 2 discs for 33 kV, 4-6 for 110 kV, 8-12 for 220 kV. Insulators must maintain dielectric strength under wet conditions (rain, fog, pollution).
- **Conductor sag and tension**: Conductors hang in a catenary between supports. Sag depends on span length, conductor weight, temperature, and ice/wind loading. Maximum sag occurs at maximum temperature (thermal expansion) and maximum ice loading. Minimum clearance from ground must be maintained at maximum sag: 5-6 m for roads, 7-8 m for railways, 3-4 m over agricultural land. Tension must not exceed the rated breaking strength of the conductor divided by the safety factor (typically 2.0-2.5).
- **Lightning protection**: Overhead ground wire (steel or ACSR) strung above the phase conductors intercepts lightning strikes, conducting them to ground through pole grounding. Ground resistance at each pole: <25 Ω in normal soil, <10 Ω in high-resistivity soil with driven ground rods or counterpoise wires. Lightning arresters (gap-type or metal oxide varistor) at transformer terminals divert surge energy to ground.

### Power Factor and Reactive Power

AC electrical systems carry two components of power: real power (watts, W) that does useful work, and reactive power (volt-amperes reactive, VAR) that oscillates between source and load without doing net work. The apparent power (volt-amperes, VA) is the vector sum. Power factor (PF) is the ratio of real to apparent power (0.0 to 1.0). A purely resistive load (heating elements, incandescent lamps) has PF = 1.0. Inductive loads (motors, transformers, welders) have PF = 0.6-0.85, meaning 15-40% of the current capacity is wasted on reactive power.

Low power factor penalties: A factory drawing 100 kW at PF = 0.7 requires 143 kVA of transformer and conductor capacity. At PF = 1.0, only 100 kVA is needed. The additional 43 kVA heats conductors and ties up transformer capacity without delivering useful energy.

Correction: Install capacitor banks (static capacitors, 10-100 kVAR each) in parallel with inductive loads. Capacitors draw leading reactive current that cancels the lagging reactive current from motors. Target PF = 0.90-0.95. Capacitor sizing: Q_cap = P × (tan θ_before - tan θ_target), where θ = arccos(PF). For a 50 kW motor load at PF = 0.75 corrected to 0.95: Q_cap = 50 × (0.882 - 0.329) = 27.6 kVAR.

### Three-Phase Power Systems

Three-phase AC power is the standard for industrial generation and distribution. Three conductors carry AC voltage waveforms offset by 120° from each other. Advantages over single-phase: 1.5× the power delivery for the same conductor material (three conductors vs. two for single-phase), constant instantaneous power delivery (single-phase pulsates at twice the line frequency), and naturally rotating magnetic fields in motors (no starting capacitor or split-phase winding needed).

- **Voltage relationships**: Line-to-line voltage (V_LL) = √3 × line-to-neutral voltage (V_LN). For a 400V three-phase system: V_LN = 400/√3 = 231V. Equipment nameplates specify both: "400V/231V" means 400V line-to-line, 231V line-to-neutral.
- **Star (wye) connection**: Each phase winding connects to a common neutral point. Provides both line-to-line and line-to-neutral voltages. Neutral carries only the unbalanced current between phases. Used for distribution transformers and generator windings.
- **Delta connection**: Phase windings connect in a closed loop (triangle). No neutral point. Only line-to-line voltage available. Used for transformer primary windings and some motor configurations. Delta-wye transformer configurations (delta primary, wye secondary) provide a neutral for distribution while blocking zero-sequence fault currents from passing through.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
