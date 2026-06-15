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

**Mineral oil lubricant grades and applications**:

| ISO VG | Viscosity at 40°C (cSt) | Typical Application | Speed Range | Load Range |
|--------|-------------------------|---------------------|-------------|------------|
| VG 22 | 19.8-24.2 | High-speed spindle bearings | >3000 RPM | Light |
| VG 32 | 28.8-35.2 | Hydraulic systems, turbine bearings | 1500-3000 RPM | Light-moderate |
| VG 46 | 41.4-50.6 | General machine tools, hydraulic presses | 750-1500 RPM | Moderate |
| VG 68 | 61.2-74.8 | Gearboxes, moderate-speed bearings | 300-750 RPM | Moderate-heavy |
| VG 100 | 90.0-110 | Enclosed gear drives, worm gears | 100-300 RPM | Heavy |
| VG 150 | 135-165 | Heavy gear drives, rolling mill bearings | 50-100 RPM | Very heavy |
| VG 220 | 198-242 | Industrial gearboxes, crusher bearings | <50 RPM | Extreme |
| VG 320 | 288-352 | Large gear drives, journal bearings (slow) | <25 RPM | Extreme |
| VG 460 | 414-506 | Extra-heavy gear drives | <10 RPM | Extreme |

**Refining process parameters**:

| Step | Temperature (°C) | Pressure | Key Parameter | Purpose |
|------|-------------------|----------|---------------|---------|
| Vacuum distillation | 350-500 | 10-50 mmHg | Cut point control | Separate lube fractions from fuel and residuum |
| Solvent extraction (furfural) | 50-100 | 1-3 atm | Solvent:oil ratio 2:1 to 4:1 | Remove aromatics (low VI, poor oxidation stability) |
| Solvent dewaxing (MEK) | -20 to -10 | 1-2 atm | Chill rate 1-2°C/min | Remove paraffin wax (raises pour point) |
| Hydrofinishing | 280-340 | 50-100 bar H₂ | LHSV 0.5-1.5 h⁻¹ | Remove S, N; saturate aromatics; improve color and stability |
| Clay contacting | 150-250 | 1 atm | 1-3% clay by weight | Final polishing, remove color bodies and residual acids |

**Properties**: Flash point typically 180-240°C (varies with grade). Pour point -10 to -30°C (paraffinic oils) or -40°C (naphthenic oils). Viscosity index 95-105 (conventional mineral oil) to 130+ (with VI improvers). Good oxidation stability (2-5x better than vegetable oils). Compatible with most seal materials (nitrile rubber, viton). Shelf life: 5+ years if uncontaminated and sealed.

**Safety & Handling**:

> **Safety warning**: Mineral oil at operating temperature (60-80°C in running machinery) can cause burns. Oil fires burn vigorously. NEVER use water on an oil fire; use sand, fire blanket, or smother with lid. Used mineral oil is an environmental contaminant and must not be dumped on ground or in waterways.

**Specific hazards**:
- **Oil mist inhalation**: Machining operations with flood coolant generate airborne oil mist droplets (1-5 μm diameter). Chronic inhalation causes lipoid pneumonia (oil droplets accumulate in lung tissue, causing inflammation and fibrosis). Exposure limit: 5 mg/m³ total particulate (OSHA PEL). Use mist collectors or enclosures on machines running flood coolant. If the operator can taste or smell oil in the air, the concentration is too high.
- **Skin contact and dermatitis**: Prolonged skin contact with mineral oil removes natural skin oils, causing defatting dermatitis (dry, cracked, inflamed skin). Soluble oil emulsions are worse because the alkaline additives (pH 8.5-9.5) and biocides irritate skin. Wear nitrile gloves when handling cutting fluids. Apply barrier cream before shift. Wash with soap and water after contact, not solvents.
- **Used oil carcinogenicity**: Repeated skin contact with used motor oil and cutting fluids has been associated with increased skin cancer risk (IARC Group 1 for untreated mineral oils, Group 3 for highly refined oils). The risk comes from polycyclic aromatic hydrocarbon (PAH) contamination that accumulates during service. Wear gloves, wash thoroughly, and do not allow used oil to remain on skin.
- **Hydraulic injection injury**: Hydraulic fluid at 200-400 bar (3,000-6,000 psi) can inject through skin from a pinhole leak in a hose or fitting, causing catastrophic tissue destruction that often requires amputation. The injection wound may look small (pinhole) but the injected fluid spreads along fascial planes, causing widespread necrosis within hours. Never search for hydraulic leaks with bare hands; use a piece of cardboard or paper held at a distance. If injection occurs, seek emergency surgery immediately (not first aid: this requires surgical debridement).

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

**Water-glycol** (fire-resistant): Water + glycol (40-60%) + thickener + additives. Fire-resistant due to water content. Lower lubricity than oil, so harder pump and valve materials are needed. Used in locations with fire risk (furnaces, welding areas, foundries).

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

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Hydraulic pump noisy, erratic operation | Oil viscosity too high (wrong grade) or contaminated with air (foaming) | Verify oil grade matches pump spec (typically ISO VG 32-46); check reservoir level (minimum 2x pump flow rate); inspect suction line for air leaks; add anti-foam agent (silicone, 10-50 ppm) |
| Bearing runs hot (>80°C) with mineral oil | Oil viscosity too low for load/speed, or insufficient oil delivery | Increase viscosity by one ISO VG grade; verify oil delivery rate (guide: 0.5-1.0 L/min per cm of shaft diameter for plain bearings); check for bearing misalignment |
| Oil turns dark and thick within weeks of service | Oxidation from high operating temperature or lack of antioxidants | Keep oil temperature below 70°C (install cooler if needed); add antioxidant (0.5-1.0% BHT or aromatic amine); replace oil and clean system |
| Emulsion cutting fluid separates (oil and water layers) | Emulsifier depleted by bacterial action or hard water minerals | Test water hardness (>200 ppm CaCO₃ degrades emulsions); use deionized water for mixing; add fresh emulsifier concentrate; if bacteria present (rancid smell), drain, clean sump with 2% NaOH, and refill |
| Gearbox oil foams excessively | Contamination with water, wrong viscosity, or overfilling | Check for water (oil appears milky; test by heating sample to 100°C — crackling indicates water); drain and refill with correct grade; do not overfill (fill to sight glass middle, not top) |
| Hydraulic system pressure drops under load | Internal leakage from worn pump or valve spools, or oil viscosity too low at operating temperature | Check pump case drain flow (should be <5% of rated flow); measure oil temperature at reservoir (should be <65°C); if overheating, install oil cooler or increase reservoir capacity |
| Soluble oil emulsion causes skin rash on operators | pH too high (>10) from alkaline additives, or biocide concentration too strong | Maintain pH 8.5-9.5; dilute biocide to manufacturer's recommendation; provide nitrile gloves and barrier cream; install splash guards on machine |
| Vacuum pump oil turns cloudy, pump loses vacuum | Water contamination from pumping wet gases or from humid air backstreaming | Install moisture trap (cold trap or molecular sieve) before pump; change oil immediately when cloudy; use hygroscopic oil for humid applications |
| Cutting tool wears rapidly despite flood coolant | Coolant not reaching cutting zone, or wrong fluid type for operation | Reposition nozzle to aim directly at chip-tool interface (within 5 cm); increase flow to 10-20 L/min for heavy cuts; switch to straight oil with EP additives for difficult materials |
| Oil filter clogs rapidly after oil change | Contaminated reservoir (sludge, wear particles, or rust) not cleaned during change | Flush reservoir with kerosene or fresh oil before refilling; install bypass filtration (10-25 μm) on return line; sample oil for particle count (target <20/18/15 ISO 4406) |

## Scaling Notes

Mineral oil lubricant production scales with petroleum refining capacity:

- **Pilot scale** (1-10 tonnes/year): Small batch still for vacuum distillation of lubricant fractions. Hand-blending of viscosity grades. Acid treating in glass-lined vessels. Adequate for a single workshop or small factory. Quality is variable; adequate for non-critical applications. One operator with basic chemistry training.
- **Commercial scale** (100-1,000 tonnes/year): Continuous vacuum distillation column with multiple side-draws for different viscosity grades. Solvent extraction unit (furfural or phenol) for aromatic removal. Solvent dewaxing unit (MEK) for pour point control. Blending facility with additive injection. This scale supplies a regional industrial economy. 10-20 workers. Product quality approaches modern standards.
- **Industrial scale** (10,000+ tonnes/year): Fully integrated refinery with dedicated lube oil train. Hydrofinishing (catalytic hydrogenation at 280-340°C, 50-100 bar H₂) for final quality improvement. Automated blending and filling lines. Quality control laboratory with viscometers, flash point testers, and spectrometric analysis. This scale supplies a national market with consistent, specification-grade lubricants.

**Critical bottleneck**: Solvent supply for extraction and dewaxing. Furfural is produced from oat hulls or corn cobs (agricultural waste). MEK is produced from butylene (petroleum derivative) or fermentation. Without these solvents, acid treating (sulfuric acid) is the fallback, but it produces lower-quality oil and large quantities of acid sludge that must be disposed of. Hydrofinishing requires high-pressure hydrogen (50-100 bar), which in turn requires a hydrogen production facility (steam methane reforming or electrolysis).

**Additive production**: ZDDP (zinc dialkyldithiophosphate) requires zinc, phosphorus, and organic alcohols. Antioxidants (BHT, aromatic amines) require organic synthesis capability. Rust inhibitors (calcium sulfonates) require sulfonic acid production. Additive packages are typically 5-15% of the finished oil by volume but represent a disproportionate share of the chemical complexity.

## Quality Control

Mineral oil lubricant quality is verified by standardized tests:

1. **Kinematic viscosity** (ASTM D445): Measure flow time through a calibrated glass capillary at 40°C and 100°C. Report in centistokes (cSt). Must fall within ±10% of the ISO VG nominal value (e.g., ISO VG 68 = 61.2-74.8 cSt at 40°C). This is the most fundamental specification test.

2. **Viscosity index** (ASTM D2270): Calculated from viscosities at 40°C and 100°C. Higher VI means less viscosity change with temperature. Conventional mineral oil: VI 95-105. Solvent-refined: VI 80-100. Hydrotreated: VI 100-130. With VI improvers: VI 130-200+. Low VI oils thin out excessively at high temperature, reducing load capacity.

3. **Flash point** (ASTM D92, Cleveland Open Cup): Minimum flash point ensures fire safety. ISO VG 32: minimum 180°C. ISO VG 68: minimum 200°C. ISO VG 220: minimum 220°C. Below-spec flash point indicates contamination with volatile fractions or light ends.

4. **Pour point** (ASTM D97): Lowest temperature at which the oil flows. Paraffinic oils: -10 to -15°C. Naphthenic oils: -30 to -40°C. Dewaxed paraffinic oils: -20 to -30°C. Must be at least 10°C below the lowest expected startup temperature.

5. **Acid number** (ASTM D974): Measures acidic oxidation products. Fresh mineral oil: <0.05 mg KOH/g. In-service oil: replace when acid number exceeds 1.0-2.0 mg KOH/g (indicates advanced oxidation).

6. **Particle count** (ISO 4406): Contamination level reported as three numbers (e.g., 16/14/11) representing particle counts at 4, 6, and 14 μm. Hydraulic systems: target 16/14/11 or cleaner. Turbine oils: target 18/16/13. General machine oils: 20/18/15 acceptable.

7. **Quick field tests**: (a) Visual inspection: fresh mineral oil is clear and pale yellow. Dark color indicates oxidation. Cloudy appearance indicates water contamination. (b) Crackle test: place a drop on a hot plate at 150°C. Bubbling/crackling indicates water >0.1%. (c) Blotter test: place a drop on filter paper. A uniform spread indicates normal oil; a dark center ring indicates soot or oxidation products.

## Variations and Alternatives

| Lubricant Type | Viscosity at 40°C | Temp Range | Oxidation Life | Cost | Best For |
|---------------|-------------------|------------|----------------|------|----------|
| Animal fat (tallow) | Semi-solid to ~30 | 10-60°C | 6-12 months | Very low | Early bootstrap, slow bearings |
| Vegetable oil (rapeseed) | 30-40 cSt | -10 to 80°C | 1-2 years | Low | General-purpose before petroleum |
| Mineral oil (conventional) | 22-460 cSt | -10 to 80°C | 3-5 years | Moderate | General industrial use |
| Mineral oil (hydrotreated) | 22-460 cSt | -20 to 90°C | 5-8 years | Higher | Extended drain, demanding service |
| PAO synthetic | 32-460 cSt | -50 to 175°C | 8-15 years | High | Extreme conditions, long drain |
| Ester synthetic | 32-100 cSt | -40 to 200°C | 5-10 years | High | Biodegradable, jet engines |
| Water-glycol hydraulic | 32-46 cSt | -20 to 60°C | 1-2 years | Moderate | Fire-risk locations |

## Safety & Hazards

- **Oil mist inhalation**: Machining operations with flood coolant generate airborne oil mist (1-5 μm diameter). Chronic inhalation causes lipoid pneumonia. Exposure limit: 5 mg/m³ total particulate (OSHA PEL). Use mist collectors or enclosures on machines running flood coolant.
- **Skin contact and dermatitis**: Prolonged skin contact with mineral oil removes natural skin oils, causing defatting dermatitis. Soluble oil emulsions are worse due to alkaline additives (pH 8.5-9.5) and biocides. Wear nitrile gloves. Apply barrier cream before shift.
- **Used oil carcinogenicity**: Repeated skin contact with used motor oil is associated with increased skin cancer risk (IARC Group 1 for untreated mineral oils). PAH contamination accumulates during service. Wear gloves, wash thoroughly.
- **Hydraulic injection injury**: Hydraulic fluid at 200-400 bar can inject through skin from a pinhole leak, causing catastrophic tissue destruction. Never search for hydraulic leaks with bare hands; use cardboard or paper. If injection occurs, seek emergency surgery immediately.
- **Oil fires**: NEVER use water on an oil fire — it flashes to steam and scatters burning oil. Extinguish with sand, fire blanket, or smothering. Keep fire suppression materials near oil heating operations.
- **Environmental disposal**: Used mineral oil is an environmental contaminant. Collect in sealed containers. Re-refine by vacuum distillation. Never dump on ground or in waterways.

## See Also

- **[Lubricants Overview](lubricants.md)**: Theory, selection guide, and cross-cutting topics
- **[Natural Lubricants](lubricants-natural.md)**: Animal fats and vegetable oils
- **[Grease & Solid Lubricants](lubricants-grease-solid.md)**: Grease production and solid lubricant coatings
- **[Synthetic Lubricants](lubricants-synthetic.md)**: Engineered lubricants for demanding applications

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [Lubricants](lubricants.md)*
