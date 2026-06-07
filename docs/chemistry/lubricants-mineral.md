# Mineral Oil Lubricants, Cutting Fluids & Hydraulic Fluids

> **Node ID**: chemistry.lubricants-mineral
> **Domain**: [Chemistry](./index.md)
> **Parent**: [Lubricants, Oils & Fluid Mechanics](lubricants.md)
> **Dependencies**: [`chemistry.petroleum-alternatives`](petroleum-alternatives.md), [`chemistry.lubricants-natural`](lubricants-natural.md)
> **Enables**: [`chemistry.lubricants-synthetic`](lubricants-synthetic.md)
> **Timeline**: Years 20-50
> **Outputs**: mineral_lubricating_oil, cutting_fluid, hydraulic_fluid
> **Critical**: No — mineral oils displace natural lubricants for most applications but are not prerequisites for core capabilities


Refined petroleum oils displace animal and vegetable lubricants for most industrial applications once petroleum distillation is established. Mineral oils offer better oxidation stability (2-5x longer service life), wider viscosity range, and consistent quality. This tier enables high-speed machinery, precision machine tools, hydraulic presses, and continuous-process equipment that would be impractical with natural lubricants alone.


## Mineral Oil Lubricants

**Composition**: Refined petroleum oil from fractional distillation. Hydrocarbon mixtures (paraffinic, naphthenic, or aromatic) selected and treated for lubricant service. The workhorse of industrial lubrication, displacing animal and vegetable oils for most applications due to better oxidation stability, wider viscosity range, and consistent quality.

**Prerequisites**:
- [Petroleum distillation](petroleum-alternatives.md) capability
- Solvent refining or acid treating for quality improvement
- Additive manufacturing capability (ZDDP, antioxidants, rust inhibitors)

**Materials**:
- Crude petroleum or oil shale
- Solvents for refining (if available)

**Production**:

1. **Distill** crude petroleum to collect lubricant boiling range fractions (typically 350-500°C boiling range, heavier than diesel and lighter than bitumen).
2. **Refine** the distillate to remove aromatics, sulfur, and nitrogen compounds. Methods include solvent extraction (furfural or phenol removes aromatics), acid treating (sulfuric acid removes unstable compounds), and hydrofinishing (hydrogenation removes sulfur and nitrogen, saturates aromatics).
3. **Dewax** (if paraffinic base) to lower the pour point. Mix with methyl ethyl ketone (MEK) solvent, chill to -20°C, filter wax crystals. The wax-free oil has a lower pour point and flows at colder temperatures.
4. **Blend** to target viscosity by mixing distillate fractions. Add viscosity index improvers (polymer additives that thicken oil more at high temperature than at low temperature) for multi-grade oils.
5. **Add additives**: anti-wear agents (ZDDP: zinc dialkyldithiophosphate, forms protective film on metal surfaces under boundary conditions), antioxidants (prevent oxidation, extend oil life), rust inhibitors (form protective film on metal, prevent corrosion from moisture), anti-foam agents (silicone compounds that prevent foam formation in circulating systems), and detergents/dispersants (keep sludge and varnish suspended in the oil so they drain out with oil changes rather than depositing on surfaces).

**Viscosity grading**:

**ISO VG system** (industrial oils, viscosity at 40°C): ISO VG 32 (32 cSt, light spindle oil), ISO VG 46 (46 cSt, general hydraulic oil), ISO VG 68 (68 cSt, general machine oil), ISO VG 100 (100 cSt, light gear oil), ISO VG 150 (150 cSt, medium gear oil), ISO VG 220 (220 cSt, gear oil), ISO VG 320 (320 cSt, heavy gear oil), ISO VG 460 (460 cSt, extra-heavy gear oil). Each grade has ±10% tolerance.

**SAE viscosity grades** (engine oils, viscosity at 100°C): SAE 30 (9.3-12.5 cSt at 100°C, general-purpose engine oil for moderate climate), SAE 40 (12.5-16.3 cSt at 100°C, heavy-duty engine oil for hot climate). Multi-grade oils: SAE 10W-30 has a 10W winter rating (meets cold-cranking requirements at -25°C) and SAE 30 hot rating. Higher viscosity grades provide thicker films for heavier loads but increase viscous friction and heat generation. Select the lowest viscosity that maintains adequate film thickness under operating conditions.

**Properties**: Flash point typically 180-240°C (varies with grade). Pour point -10 to -30°C (paraffinic oils) or -40°C (naphthenic oils). Viscosity index 95-105 (conventional mineral oil) to 130+ (with VI improvers). Good oxidation stability (2-5x better than vegetable oils). Compatible with most seal materials (nitrile rubber, viton). Shelf life: 5+ years if uncontaminated and sealed.

**Safety & Handling**:

> **Safety warning**: Mineral oil at operating temperature (60-80°C in running machinery) can cause burns. Oil fires burn vigorously. NEVER use water on an oil fire; use sand, fire blanket, or smother with lid. Used mineral oil is an environmental contaminant and must not be dumped on ground or in waterways.

**Applications**: Every industrial application that needs lubrication: bearings, gears, hydraulic systems, engines, compressors, turbines. ISO VG 32 and 46 dominate general machinery. ISO VG 68-220 cover gear applications. SAE grades cover internal combustion engines.

**Strengths**:
- Better oxidation stability than animal or vegetable oils (longer service life)
- Available in a wide range of viscosity grades for every application
- Compatible with standard seal and bearing materials
- Can be re-refined (vacuum distillation removes contaminants, additives replenished)
- Additive technology tailors performance for specific applications

**Weaknesses**:
- Requires petroleum distillation infrastructure
- Petroleum is a finite resource
- Some additive compounds (ZDDP) contain heavy metals with environmental concerns
- Mineral oils are not biodegradable; spills persist in the environment
- Pour point limits cold-weather use without heaters or low-viscosity grades


## Cutting Fluids

**Principle**: Cutting fluids serve four functions simultaneously: lubricate the chip-tool interface (reduce cutting force, improve surface finish), cool the tool and workpiece (remove heat, the primary function), flush chips from the cutting zone, and prevent rust on the workpiece and machine.

**Prerequisites**:
- Base oil (mineral, lard, or vegetable) or chemical lubricant base
- Emulsifier (for soluble oil): sulfonate or soap
- Biocide (for emulsions): prevents bacterial growth
- Pump, sump tank, hose, and nozzle (for flood coolant)
- Filter (mesh or paper) for chip removal

**Materials**:
- Mineral oil or lard oil (for straight oil)
- Mineral oil + emulsifier (for soluble oil)
- Chemical lubricants (for synthetic fluid)
- Water (for emulsion and synthetic types)

**Types and Production**:

**Straight cutting oil**: Mineral oil or lard oil, undiluted. Best lubrication, poorest cooling (low heat capacity). Used for tapping, threading, broaching, and heavy turning where lubrication matters more than cooling. Can be enhanced with sulfur or chlorine compounds (extreme pressure additives that react with the metal surface at high temperature to form a solid lubricating film, preventing welding of chip to tool).

**Soluble oil (emulsion)**: Mineral oil + emulsifier (sulfonate or soap) + water. Mix 5-10% oil in water by volume. Milky white emulsion. Water provides excellent cooling (high heat capacity); oil provides lubrication and rust protection. This is the most common cutting fluid for general machining. Replace regularly because bacteria grow in the emulsion, causing a rancid smell and skin irritation. Add biocide to extend sump life.

**Synthetic cutting fluid**: Water + chemical lubricants (no mineral oil). Clear or tinted. Best cooling, good rust protection, longest sump life. More expensive. Used for grinding (where maximum cooling and clean fluid are needed) and high-speed machining.

**Application methods**:

- **Flood coolant**: Pump fluid from sump tank through hose/nozzle, direct at cutting zone. Flow rate 5-20 liters/minute. Most common method. Filter fluid (mesh or paper filter) to remove chips and fines. Settle tank allows chips to settle before recirculation.
- **Mist coolant**: Atomize fluid into fine spray using compressed air. Lower volume, less mess. For operations where flood is impractical.
- **Manual application**: Brush or squeeze bottle. For intermittent cutting, hand operations, and small jobs.

**Properties**: Straight oil: excellent lubricity, flash point 150-200°C, poor cooling. Emulsion: good balance of cooling and lubrication, 5-10% concentration, milky appearance, limited sump life (3-6 months with biocide). Synthetic: best cooling, clear appearance, longest sump life, highest cost.

**Safety & Handling**:

> **Safety warning**: Oil mist from mist coolant systems is a respiratory hazard. Inhaled oil mist can cause lipoid pneumonia and chronic respiratory irritation. Use mist coolant only with adequate ventilation or enclosure with mist extraction. Bacteria in soluble oil emulsions cause skin irritation and rancid odors. Monitor emulsion pH weekly; a drop below 8.5 indicates bacterial growth. Sulfureted (sulfurized) cutting oils cause skin irritation with prolonged contact.

**Applications**: General machining (emulsion), tapping and threading (straight oil), grinding (synthetic), broaching (straight oil with EP additives), hand operations (manual application).

**Strengths**:
- Soluble oil emulsion provides the best balance of cooling and lubrication for general machining
- Straight oil excels at lubrication for difficult cutting operations
- Synthetic fluids offer the longest sump life and best cooling for grinding
- Flood coolant is simple to implement and effective for most operations

**Weaknesses**:
- Emulsions require regular maintenance (biocide addition, pH monitoring, periodic replacement)
- Oil mist from coolant systems is a respiratory hazard
- Straight oil creates slippery floors and fire risk
- Disposal of used cutting fluid requires treatment (break emulsion, separate oil and water phases)
- Bacterial growth in emulsions limits practical sump life to 3-6 months



## Hydraulic Fluids

**Principle**: Hydraulic systems transmit force through incompressible fluid. The fluid must transmit force efficiently (incompressible), flow readily through valves and pumps (correct viscosity), resist chemical degradation (no oxidation, no corrosion), and be compatible with seals (does not swell or shrink rubber or leather). Fire resistance is desirable but not always achievable.

**Prerequisites**:
- Fluid supply (vegetable oil, mineral oil, or water-glycol mixture)
- Seals compatible with the chosen fluid (rubber, leather, or polymeric)
- Filtration capability (10-25 μm absolute for return line)

**Materials**:
- Varies by fluid type (see below)

**Fluid types**:

**Vegetable oil-based**: Rapeseed or castor oil. Biodegradable with good lubricity. Limited temperature range: thickens when cold, thins when hot. Oxidizes over time. Suitable for the Metallurgy-Machine Tools stage transition hydraulic presses, where petroleum is not yet available.

**Mineral oil-based**: Refined petroleum oil (see [Petrochemicals](petroleum-alternatives.md)). ISO VG 32 or 46 most common. Contains anti-wear agents (ZDDP), antioxidants, rust inhibitors, and anti-foam agents. Operating temperature range -10°C to +70°C. The most common hydraulic fluid in industrial use.

**[Water-glycol](../glossary/water-glycol.md)** (fire-resistant): Water + glycol (40-60%) + thickener + additives. Fire-resistant due to water content. Lower lubricity than oil, so harder pump and valve materials are needed. Used in locations with fire risk (furnaces, welding areas, foundries).

**Hydraulic system design**:

Pump (gear pump: 10-200 bar, or piston pump: 200-400 bar) feeds control valves (directional, pressure relief, flow control), which direct fluid to actuators (cylinder for linear motion, motor for rotary). Return line carries fluid back to reservoir. A filter in the return line (10-25 μm absolute) removes contaminants, the primary cause of hydraulic system failure. The reservoir holds 2-3x the pump flow rate capacity, allowing fluid time to de-aerate and settle.

**Properties**: Mineral oil hydraulic fluid: ISO VG 32-46, flash point 180-200°C, operating range -10°C to +70°C. Vegetable oil: similar viscosity but narrower temperature range and shorter service life. Water-glycol: non-flammable, lower lubricity, limited to moderate pressure systems.

**Safety & Handling**:

> **Safety warning**: High-pressure hydraulic fluid (200-400 bar) can inject through skin from a pinhole leak, causing catastrophic tissue damage that may require amputation. Never search for leaks with bare hands; use a piece of cardboard or paper. Mineral oil hydraulic fluid is flammable; a leak onto a hot surface can ignite. Water-glycol fluids reduce fire risk but are toxic if ingested.

**Applications**: Hydraulic presses for metalworking, machine tool hydraulics, hydraulic jacks and lifts, construction equipment, aircraft hydraulic systems.

**Strengths**:
- Mineral oil fluid provides excellent lubrication, corrosion protection, and wide temperature range
- Vegetable oil fluid is biodegradable and available before petroleum
- Water-glycol provides fire resistance for hazardous locations
- Hydraulic systems deliver high force with precise control

**Weaknesses**:
- Contamination is the primary failure mode; filtration is critical and often neglected
- Mineral oil fluid is flammable; leaks onto hot surfaces can ignite
- High-pressure injection injuries are severe and often underestimated
- Vegetable oil fluid oxidizes and has a short service life
- Water-glycol has poor lubricity, requiring harder pump components


## See Also

- **[Lubricants Overview](lubricants.md)**: Theory, selection guide, and cross-cutting topics
- **[Natural Lubricants](lubricants-natural.md)**: Animal fats and vegetable oils
- **[Grease & Solid Lubricants](lubricants-grease-solid.md)**: Grease production and solid lubricant coatings
- **[Synthetic Lubricants](lubricants-synthetic.md)**: Engineered lubricants for demanding applications

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [Lubricants](lubricants.md)*
