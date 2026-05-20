# Air Separation & Bulk Gas Production

> **Node ID**: chemistry.air-separation
> **Domain**: Chemistry
> **Timeline**: Years 20-40
> **Outputs**: argon, nitrogen, oxygen

### Air Separation — Bulk Inert Gas Production

**Linde fractional distillation of liquid air**:
- **Principle**: Air is 78% N₂ (bp -196°C), 21% O₂ (bp -183°C), 0.93% Ar (bp -186°C). Cool air until it liquefies, then fractionally distill at cryogenic temperatures.
- **Air preparation**: Compress atmospheric air to 5-6 MPa. Remove water (desiccant beds — silica gel or activated alumina) and CO₂ (molecular sieve or NaOH scrubber — CO₂ would freeze and plug equipment at cryogenic temperatures). Filter particulates.
- **Cooling**: Compressed, cleaned air enters counter-current heat exchanger — cooled by outgoing cold nitrogen and oxygen product streams. Further cooled by expansion through throttle valve (Joule-Thomson effect: real gas cools when expanding at temperatures below its inversion temperature) or expansion engine (adiabatic expansion does work → larger temperature drop).
- **Distillation column**: Double-column design. Lower column at ~0.5 MPa (bp of N₂ at this pressure ~ -177°C). Upper column at ~0.1 MPa. Air enters between columns. N₂ (lower boiling point) rises as vapor, O₂ (higher boiling point) descends as liquid. Argon accumulates at an intermediate point — draw sidestream to separate argon column.
- **Products**:
  - **Nitrogen** (99-99.99%): Used as inert blanket gas, carrier gas, purge gas. Store as compressed gas or liquid N₂ in vacuum-insulated dewar (Dewar flask — double-walled vessel, vacuum between walls, silvered inner wall for radiation shielding. Evaporation rate: 0.5-2% per day).
  - **Oxygen** (95-99.5%): For steelmaking, welding, medical use, oxidation processes.
  - **Argon** (99-99.999%): Critical for CZ crystal growth (inert atmosphere prevents silicon oxidation and reactions with crucible). Also for welding shielding gas, sputtering.

### Air Separation Process — Step-by-Step Linde Cycle

The Linde fractional distillation process separates air into its constituent gases through cryogenic distillation. The complete process involves six major steps:

**Step 1: Air intake and filtration**
- Atmospheric air is drawn through coarse particulate filters (removes dust, pollen, insects). Pre-treatment is critical — contaminants would freeze at cryogenic temperatures and plug the distillation column.
- **CO₂ removal**: Caustic soda (NaOH) scrubber or molecular sieve adsorbent beds. CO₂ freezes at -78°C (dry ice) and would accumulate on heat exchanger surfaces, blocking flow. A typical plant uses two molecular sieve beds in alternating cycles — one adsorbing while the other regenerates with heated purge gas.
- **Water vapor removal**: Molecular sieve desiccant (3Å or 4Å zeolite) or activated alumina beds. Water would freeze to ice at cryogenic temperatures and obstruct narrow passages in heat exchangers and expansion valves. Dew point after drying: below -60°C.
- **Hydrocarbon removal**: Trace acetylene (C₂H₂) is especially dangerous — it can accumulate in liquid oxygen and detonate. Activated carbon filters or catalytic oxidizers remove hydrocarbons before the cold box.

**Step 2: Compression**
- Multi-stage reciprocating compressor raises air pressure to 5-10 atm (0.5-1.0 MPa). Each stage compresses the air adiabatically, heating it significantly.
- Inter-stage cooling: Shell-and-tube heat exchangers cool the air back to near-ambient temperature (below 150°C, typically 30-40°C) between each compression stage. This is essential — cooler air entering the next stage requires less compression work (isothermal compression is the theoretical ideal; multi-stage with intercooling approximates it).
- 3-4 stages are typical for achieving 5-10 atm with reasonable efficiency. More stages approach isothermal conditions but add mechanical complexity and cost.
- After the final stage, an aftercooler brings compressed air to near-ambient temperature. Knockout drums remove condensed water.

**Step 3: Heat exchange (cold recovery)**
- This is the CORE of process efficiency — the regenerative cold recovery loop. Countercurrent heat exchangers (plate-fin or shell-and-tube) transfer cold from outgoing product streams to incoming warm compressed air.
- Cold product gases (O₂ at -183°C, N₂ at -196°C) flow counter-current to warm incoming compressed air. The temperature approach at the cold end is typically 2-5°C — meaning the incoming air leaves the heat exchanger within a few degrees of the product stream temperature.
- Effectiveness: 90-95% of the refrigeration produced in the cold box is recovered by these heat exchangers. Without countercurrent recovery, the process would be uneconomical — the compressor power to produce the necessary temperature drop would be prohibitive.
- Construction: Aluminum plate-fin (Brazed Aluminum Heat Exchanger, BAHX) is standard for large plants. Copper or stainless steel tubing for smaller units. All welded or brazed joints — no mechanical fittings in the cryogenic section.

**Step 4: Expansion (cryogenic cooling)**
- After pre-cooling in the main heat exchanger, the air stream splits: one portion (~70-80%) continues to the distillation column; the remaining portion is further cooled by expansion.
- **Joule-Thomson expansion valve**: Throttles high-pressure air to lower pressure through a restriction. Real gases cool when expanding below their inversion temperature (for air, ~330°C — always satisfied). Temperature drop is modest (~0.25°C/atm pressure drop) but reliable and simple (no moving parts in the cold box).
- **Expansion turbine** (more efficient): High-pressure air expands through a turbine wheel, doing work (driving a generator or assisting the main compressor). The air gives up internal energy as shaft work, producing a much larger temperature drop than J-T expansion alone. Turbine efficiency: 80-85% (isentropic). Typical temperature drop: 30-80°C per stage.
- After expansion, air temperature reaches cryogenic range: approximately -180°C. A portion begins to liquefy.

**Step 5: Double-column distillation**
- The heart of the process. Two distillation columns operate at different pressures to exploit the boiling point difference between nitrogen and oxygen.
- **Lower column** (at 5-6 atm): Air enters at the bottom. At this pressure, N₂ boils at ~-177°C and O₂ boils at a higher temperature. Nitrogen vapor rises to the top and condenses against the colder upper-column liquid. Liquid nitrogen (LN₂) accumulates at the top; oxygen-enriched liquid (~35-40% O₂, called "rich liquid") collects at the bottom.
- **Upper column** (at ~1 atm): Rich liquid from the lower column feeds into the upper column through a Joule-Thomson valve (pressure drop provides additional refrigeration). At atmospheric pressure, the boiling points separate more widely: pure liquid oxygen collects at the bottom (bp -183°C) and nitrogen gas exits the top (bp -196°C). The reboiler at the bottom of the upper column is thermally coupled to the condenser at the top of the lower column — the condensing N₂ vapor from the lower column provides heat to boil the O₂ liquid in the upper column. This thermal integration is the key to the double-column design's efficiency.
- Multiple sieve trays or structured packing in each column provide vapor-liquid contact for mass transfer. 40-70 theoretical stages in the upper column achieve high-purity separation.

**Step 6: Argon separation**
- Argon's boiling point (-186°C) falls between N₂ (-196°C) and O₂ (-183°C), so it accumulates at an intermediate point in the upper column — typically at 10-15% argon concentration in a side draw near the middle trays.
- **Argon side-draw**: Vapor is drawn from the upper column at the argon peak concentration point and fed to a separate argon column (a third distillation column). This column produces crude argon (~95-98% Ar, remainder mostly O₂ and N₂).
- **Argon purification**: Catalytic addition of hydrogen to the crude argon converts residual O₂ to H₂O (2H₂ + O₂ → 2H₂O over palladium catalyst at 400-500°C). Water removed by molecular sieve dryer. Final distillation removes N₂ (boils at lower temperature than Ar). Product: 99.999% argon (5N+).
- Argon production is typically 1-3% of the air input by volume — small but economically valuable, especially for semiconductor manufacturing.

**Product storage and distribution**:
- **Cryogenic storage**: Double-walled vacuum-insulated Dewar flasks. Inner vessel: stainless steel. Outer vessel: carbon steel. Vacuum space filled with perlite or multi-layer insulation (MLI — alternating aluminum foil and fiberglass). Evaporation losses: 0.5-2%/day depending on tank size and insulation quality.
- Liquid O₂ stored at -183°C, liquid N₂ at -196°C. For gaseous distribution: ambient vaporizers (ambient air heats cryogenic liquid through finned tubes) or steam-heated vaporizers for higher flow rates.
- **Production rates**: Small bootstrap plant: 1-10 tonnes/day O₂ (sufficient for a small steelmaking operation or welding shop). Medium industrial: 50-200 t/d. Large industrial (world-scale): 1000+ t/d O₂, requiring 20-50 MW electrical power.

### Plant Equipment Design

**Compressor**:
- **Type**: Multi-stage reciprocating (piston) compressor. 3-5 stages with intercoolers between each stage (cool compressed air back to near-ambient — reduces work of next stage and prevents overheating).
- **Pressure**: 5-20 bar (0.5-2 MPa) for Linde process. Higher pressure means more Joule-Thomson cooling but more compressor work.
- **Construction**: Cast iron or steel cylinders, steel pistons with piston rings, poppet or ring valves. Lubricated with mineral oil (must not contaminate process air — oil mist carries into downstream equipment). Later: oil-free compressors with PTFE piston rings for cleaner product.
- **Power**: Major electricity consumer — 0.3-0.5 kWh per Nm³ of air processed.

**Heat exchanger**:
- **Type**: Counter-current (countercurrent) shell-and-tube or plate-fin. Cold product gas streams (N₂, O₂) flow opposite to incoming warm compressed air. Temperature approach: 2-5°C at cold end.
- **Construction**: Copper or stainless steel tubing for good thermal conductivity at cryogenic temperatures. Insulated enclosure packed with perlite or mineral wool under slight positive nitrogen purge (prevents moisture ingress and ice formation). Welded joints — no threaded fittings at cryogenic temperatures (leak risk from thermal contraction).

**Construction sequence**: Compressor → aftercooler (initial air cooling) → molecular sieve traps (remove H₂O, CO₂) → main heat exchanger (cool to near-liquefaction) → expansion valve or turbine (final cooling to liquid) → lower distillation column → upper distillation column → product storage (compressed gas cylinders or vacuum-insulated dewars).

### Safety

- **Cryogenic burns**: LOX (−183°C) and LN₂ (−196°C) cause severe frostbite on skin contact. Insulated gloves, face shield, long sleeves mandatory. Never touch uninsulated cryogenic piping.
- **Oxygen-enriched fire hazard**: Materials burn vigorously in >25% O₂ atmospheres. Clothing saturated with LOX becomes explosive. Oil or grease on LOX-wetted surfaces can auto-ignite. Designate oxygen-safe zones — no petroleum products, no organic flooring.
- **Nitrogen asphyxiation**: LN₂ evaporates to 700× volume of gas. In confined spaces, N₂ displaces O₂ rapidly. Unconsciousness within seconds at <10% O₂, death within minutes. Continuous O₂ monitoring in all ASU enclosed areas. Ventilate before entry.

### Alternative: Pressure Swing Adsorption (PSA)

For smaller-scale nitrogen or oxygen production without cryogenic infrastructure:

- **Principle**: Zeolite molecular sieves (synthetic aluminosilicate crystals with uniform pore sizes ~3-10 Å) adsorb different gas molecules at high pressure and release them at low pressure. For N₂ production: carbon molecular sieve (CMS) adsorbs O₂ preferentially (kinetic diameter 3.46 Å vs N₂ at 3.64 Å — O₂ diffuses into pores faster). For O₂ production: 13X zeolite adsorbs N₂ preferentially (N₂ quadrupole moment interacts with zeolite cation sites).
- **Cycle**: Pressurize vessel with compressed air (~6-10 bar) → adsorbent captures target gas, desired gas passes through as product → depressurize vessel → adsorbed gas desorbs and is vented → repressurize. Two vessels operate in alternating cycles for continuous output. Cycle time 30-120 seconds.
- **Product purity**: N₂ at 95-99.5% (higher purity requires longer adsorption time = lower flow rate). O₂ at 90-95%. Not as pure as cryogenic distillation, but adequate for many industrial uses (inerting, combustion enhancement).
- **Advantages**: No cryogenic temperatures, simpler equipment, lower capital cost for small-medium volumes (10-500 Nm³/hour). Can be built with basic air compressors and pressure vessels.
- **Limitations**: Higher energy per unit N₂/O₂ than large cryogenic plants. Cannot produce argon (too similar in properties to O₂ for PSA separation). Product is gas only — no liquid output without additional liquefaction equipment.

### Rare Gas Recovery

Beyond the three main products, air contains trace noble gases recoverable with additional distillation stages:

- **Neon (Ne)**: 18 ppm in air. Boiling point -246°C (much lower than N₂). Accumulates at the top of the upper column as non-condensable gas. Extract from the nitrogen waste stream by additional cryogenic distillation stages. Uses: neon lighting, excimer lasers for semiconductor lithography. Very high value per unit volume.
- **Krypton (Kr)**: 1.1 ppm in air. Boiling point -153°C (between O₂ and methane). Accumulates in the liquid oxygen product. Extract by side-draw from the oxygen section followed by additional distillation. Uses: high-performance insulating window gas (low thermal conductivity), specialized lighting.
- **Xenon (Xe)**: 0.09 ppm in air. Boiling point -108°C (highest of the noble gases). Co-extracts with krypton. Additional distillation separates Kr from Xe. Uses: ion propulsion (spacecraft), anesthesia, high-intensity lamps. Extremely valuable — ~$10-50/L of pure Xe gas.
- **Helium (He)**: 5 ppm in air, but NOT economically recoverable from air separation (bp -269°C, far below everything else; requires temperatures unachievable in standard ASU). Helium is extracted from natural gas wells where it accumulates from radioactive decay of uranium/thorium in rock.

### Energy Balance and Efficiency

- **Specific energy consumption**: Modern cryogenic ASU — 0.35-0.55 kWh per Nm³ of O₂ produced (as gas). For liquid products: 0.8-1.2 kWh/Nm³ O₂ (additional energy for liquefaction). The compressor is the dominant energy consumer (>90% of total plant power).
- **Heat integration**: The countercurrent heat exchanger system recovers >90% of the refrigeration produced by expansion. Without this recovery, energy consumption would be ~5-10× higher. Additional cold is continuously needed only to compensate for heat leak through insulation and the enthalpy imbalance of the incoming/outgoing streams.
- **Carnot efficiency**: The theoretical minimum work to separate air into pure O₂ and N₂ at 1 atm is only ~0.06 kWh/Nm³ O₂. Real ASU efficiency is thus ~10-15% of theoretical — the remaining losses are from irreversibilities in heat exchangers (finite temperature differences), distillation trays (finite composition differences), and throttling (J-T valves). Expansion turbines recover some work and improve efficiency.
- **Benchmark**: A world-scale ASU (3000 t/d O₂) draws 25-40 MW electrical power and operates at >95% availability (planned maintenance shutdowns only). Small bootstrap plants sacrifice efficiency for simplicity.

### Scale Considerations

- Cryogenic ASU is economical above ~500 Nm³/hour output. Below this, PSA units are more cost-effective despite higher per-unit energy. For bootstrapping, a PSA unit can provide process nitrogen (for inerting furnaces, purging equipment) while cryogenic capability is developed for high-purity applications (argon for crystal growth, liquid oxygen for steelmaking). A small cryogenic plant producing 1-5 tonnes/day of liquid O₂ requires ~200-500 kW electrical power and represents the minimum viable scale for liquid gas production.

### Cryogenic Column Internals

**Double column system**: Modern air separation units (ASUs) use a double-column arrangement — a high-pressure column (operating at 5-6 bar) sitting directly above a low-pressure column (1.2-1.5 bar) with a common condenser-reboiler between them. The high-pressure column produces oxygen-enriched liquid (~35% O₂) at its bottom and nitrogen-rich vapor at its top. The nitrogen condenser provides heat to reboil the low-pressure column — thermal coupling reduces energy consumption by 30-40% vs single column.

**Low-pressure column**: Produces pure nitrogen gas (99.999%) at the top and pure liquid oxygen (99.5%+) at the bottom. Structured packing (corrugated metal sheets with specific surface area 250-500 m²/m³) replaces traditional sieve trays in modern columns — lower pressure drop (0.1-0.3 kPa per theoretical stage vs 0.7-1.0 kPa for trays), higher capacity, and better turndown ratio. Typical column: 40-70 theoretical stages, 2-4 m diameter, 25-40 m height.

**Argon side-draw**: A side stream from the low-pressure column (where argon concentration peaks at ~10-12%) feeds an additional argon column. Argon boils between oxygen (-183°C) and nitrogen (-196°C) at 1 atm (bp -186°C). The argon column produces crude argon (95-98% Ar, remainder O₂ and N₂), which is further purified by catalytic deoxidation (H₂ + O₂ → H₂O over Pd catalyst) and cryogenic distillation to remove nitrogen. Final purity: 99.999% Ar.

### Non-Cryogenic Alternatives

**Pressure Swing Adsorption (PSA) nitrogen**: Carbon molecular sieve (CMS) adsorbs O₂ faster than N₂. Compressed air (7-10 bar) passes through a CMS bed — O₂ is adsorbed, N₂ passes through as product. When bed saturates, switch to second bed while first regenerates by depressurizing. Cycle time: 60-120 seconds. Purity: 95-99.5% N₂. Flow: 1-3000 Nm³/h. Energy: 0.3-0.5 kWh/Nm³ N₂. Used for inerting, blanketing, food packaging.

**Vacuum Swing Adsorption (VSA) oxygen**: Lithium-exchanged zeolite (LiLSX) selectively adsorbs N₂ from air at near-ambient pressure (1.2-1.5 bar). Desorption by applying vacuum (50-100 mbar). Simpler than PSA (no compressor — blower only), lower energy. Purity: 90-93% O₂. Flow: 5-150 tonnes/day. Suitable for steelmaking, glass furnaces, wastewater treatment.

**Membrane separation**: Hollow fiber polymer membranes (polyimide or polysulfone) — O₂ permeates faster than N₂ due to smaller molecular size and higher solubility. Compressed air (7-12 bar) flows through fiber bores; O₂-rich permeate exits the shell side. No moving parts, modular, compact. N₂ purity: 95-99% (higher purity = lower recovery = higher energy). Typical: 500 Nm³/h N₂ at 97% purity, energy 0.4-1.0 kWh/Nm³. Used for tire inflation, fuel tank inerting, small-scale chemical processing.

### Bootstrap Sequence

For a civilization rebuilding industrial chemistry from scratch, air separation capability develops in stages:

1. **No ASU** — obtain O₂ from metal oxides (thermal decomposition), N₂ from combustion gas displacement. Very limited quantities.
2. **PSA unit** — build from air compressor + zeolite beds + pressure vessels. Provides 90-95% purity N₂ or O₂ at small scale. No cryogenic infrastructure needed. Adequate for inerting and basic oxidation.
3. **Small cryogenic ASU** — requires compressor, countercurrent heat exchanger (copper or stainless), insulated cold box (perlite-filled), and a double distillation column (copper or stainless sieve trays). Produces liquid O₂/N₂ and, with an additional column, crude argon. This is the entry point for semiconductor-capable gas production.
4. **Full-scale ASU** — with rare gas recovery (Ne, Kr, Xe), expansion turbines (not just J-T valves), and product liquefaction for distribution. Supports all downstream processes including CZ crystal growth, steelmaking, and chemical synthesis at scale.


---

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
