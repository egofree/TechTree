# Powder Metallurgy & Advanced Materials

> **Node ID**: metals.powder-metallurgy
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`metals.alloys`](alloys.md), [`chemistry.hydrogen-silane`](../chemistry/hydrogen-silane.md), [`energy.electric-furnaces`](../energy/electric-furnaces.md)
> **Timeline**: Years 30-60
> **Outputs**: tungsten products, cemented carbides, PM structural parts, MIM components, additive manufactured parts

### Overview

Powder metallurgy (PM) encompasses all processes that form metal components from powdered feedstock rather than molten metal. This distinction is critical because many important metals — tungsten (mp 3422°C), molybdenum (mp 2623°C), tantalum (mp 3017°C) — have melting points so extreme that conventional casting is impractical or impossible. PM also enables near-net-shape manufacturing with minimal material waste (95-98% material utilization vs. 50-70% for machining from billet), compositional freedom (immiscible alloys, graded structures), and microstructural control impossible in ingot metallurgy.

The technology chain runs from powder production → blending → compaction → sintering → post-processing. Each stage is a distinct industrial process with its own equipment, quality parameters, and failure modes. The field has expanded dramatically from simple pressed-and-sintered iron bushings (1920s) to metal injection molded surgical instruments, hot isostatically pressed superalloy turbine disks, and laser-sintered titanium aerospace brackets.

### Powder Production

Every PM process begins with metal powder, and powder characteristics — particle size, shape, size distribution, chemistry, flowability, and apparent density — determine final part quality. The major production routes produce powders with fundamentally different morphologies:

**[Gas atomization](../glossary/gas-atomization.md)** (premium spherical powders):
- Molten metal stream (induction or arc melted under inert atmosphere) is disintegrated by high-pressure argon or nitrogen gas at 2-7 MPa through a converging-diverging nozzle. The gas kinetic energy overcomes the melt's surface tension, forming droplets that spheroidize during free fall.
- Particle size: 10-150 µm median (d₅₀), controlled by gas pressure, melt flow rate, and nozzle geometry. Higher gas-to-metal ratio (GMR, typically 2-5:1 by mass) produces finer powder at higher gas consumption cost.
- Spherical particle shape → excellent flowability (Hall flow < 25 s/50 g) and high tap density (60-65% of theoretical). Preferred for additive manufacturing (SLM, EBM) and hot isostatic pressing.
- Cooling rate: 10³-10⁵ K/s, producing fine dendritic microstructures. Argon atomization avoids oxygen pickup (<0.05% O₂ for Ti alloys); nitrogen atomization is acceptable for stainless steels and Ni alloys where dissolved N is tolerated.
- Yield: Only 30-50% of powder falls in the usable 15-45 µm range for SLM. Oversize is re-atomized; undersize fines (<10 µm) are health hazards and difficult to recycle.
- Production cost: $30-80/kg for stainless steel, $200-600/kg for titanium alloys, $150-400/kg for nickel superalloys.

**[Water atomization](../glossary/water-atomization.md)** (irregular powders, high volume, low cost):
- High-pressure water jets (10-100 MPa) atomize the melt stream. Water's higher momentum and rapid quench produce irregular, ragged particles with surface oxide.
- Particle size: 50-200 µm median, broader distribution than gas atomization. Water pressure is the primary size control: 50 MPa → ~100 µm median; 100 MPa → ~50 µm.
- Irregular shape → poor flowability but higher green strength after compaction (mechanical interlocking of jagged particles). Ideal for conventional press-and-sinter structural parts.
- Oxygen pickup: 0.2-0.5% O₂ (water reacts with hot metal surface). Acceptable for iron and copper-based powders; unacceptable for titanium, aluminum, or reactive metals.
- Production cost: $3-8/kg for iron powder, $5-15/kg for copper powder. Dominates volume production (80%+ of all PM structural parts use water-atomized iron powder).

**[Centrifugal atomization](../glossary/centrifugal-atomization.md)** (controlled-size, clean powders):
- Molten metal on a spinning disk or cup (rotating electrode process, REP) is flung outward by centrifugal force, forming droplets that solidify in free fall. Rotation speed: 10,000-50,000 rpm. Higher rpm → finer powder.
- Particle size distribution is narrower than gas or water atomization (geometric standard deviation σ = 1.2-1.5 vs. 1.8-2.2). Near-spherical shape.
- Plasma rotating electrode process (PREP): A plasma arc melts the end of a rotating bar electrode (typically Ti-6Al-4V or Ni alloy). No crucible contact → no ceramic inclusions. Critical for rotating-grade titanium powder in aerospace.
- Yield: 60-80% in usable size range. Production rate: 1-50 kg/h per electrode — lower throughput than gas atomization but higher quality.

**[Hydrogen reduction](../glossary/hydrogen-reduction.md)** (tungsten, molybdenum, cobalt, nickel):
- Metal oxides (WO₃, MoO₃, Co₃O₄, NiO) are reduced by flowing hydrogen gas in a pusher furnace or rotary kiln. The reduction proceeds topotactically — the metal crystal inherits the morphology of the oxide precursor, producing angular or sponge-like particles.
- **Tungsten**: WO₃ + 3H₂ → W + 3H₂O at 700-1000°C in a multi-zone furnace (4-6 zones, progressively higher temperature). Hydrogen flow: 5-20 L/min per kg WO₃. Reduction time: 2-8 hours depending on desired particle size. Particle size: 0.5-20 µm (controlled by oxide feedstock, temperature, and H₂ dew point). Fine tungsten powder (<5 µm) for cemented carbides; coarse powder (10-20 µm) for heavy alloys and sintered contacts.
- **Molybdenum**: MoO₃ + 3H₂ → Mo + 3H₂O at 600-1100°C in two stages (MoO₃ → MoO₂ at 600-700°C, MoO₂ → Mo at 900-1100°C). Two-stage reduction prevents volatilization of MoO₃ (sublimes at 700°C). Particle size: 2-10 µm.
- **Cobalt**: Co₃O₄ + 4H₂ → 3Co + 4H₂O at 400-600°C. Fine cobalt powder (1-2 µm, Fisher sub-sieve size) is critical as the binder phase in cemented carbides — cobalt particle size controls WC grain growth during sintering.

**[Electrolysis](../chemistry/electrolysis.md)** (copper, iron, silver powders):
- Direct electrolysis from aqueous sulfate or chloride solutions produces dendritic powder deposits that are scraped from the cathode. Current density: 1000-5000 A/m² (much higher than electrowinning for cathode production). High current density promotes dendritic growth rather than dense plating.
- **Copper powder**: Electrolyze CuSO₄ + H₂SO₄ solution at 2000-4000 A/m², 25-35°C. Dendritic particles with high surface area. Apparent density: 1.5-3.5 g/cm³ (vs. 8.96 g/cm³ for solid copper). Used in self-lubricating bearings (oil-impregnated porous Cu) and friction materials.
- **Iron powder**: Electrolyze FeSO₄ or FeCl₂ solution at 1000-3000 A/m². Product is brittle, high-purity (>99% Fe) sponge iron that is milled and annealed (600-800°C in H₂/NH₃) to soften and reduce oxide content.
- Electrolytic powders are more expensive than atomized but offer higher purity and controlled dendritic morphology.

**[Carbonyl process](../glossary/carbonyl-process.md)** (iron, nickel):
- Metal reacts with carbon monoxide to form volatile metal carbonyl: Fe + 5CO → Fe(CO)₅ at 150-200°C and 10-20 MPa (BASF process). The liquid carbonyl (boiling point 103°C) is distilled for purification, then decomposed by heating to 200-300°C at atmospheric pressure: Fe(CO)₅ → Fe + 5CO. The CO is recycled.
- Produces extremely fine (1-10 µm), high-purity (>99.5%) spherical powder. Carbonyl iron powder (CIP) is used in MIM feedstock, high-frequency magnetic cores, and microwave-absorbing materials.
- Carbonyl nickel (Ni(CO)₄, Mond process): Ni + 4CO → Ni(CO)₄ at 50-80°C, decompose at 200-250°C. Nickel carbonyl is extremely toxic (TLV 0.001 ppm) — the process requires sealed equipment with continuous CO monitoring and thermal afterburners on exhaust.

### Tungsten and Refractory Metals

Tungsten's melting point (3422°C, highest of all metals) makes conventional melting impossible — no practical crucible material exists above ~3000°C, and the energy requirements for sustained temperatures above 3000°C are extreme. Instead, tungsten is processed entirely by powder metallurgy: compact the hydrogen-reduced powder, then sinter at temperatures approaching but below the melting point.

**Tungsten processing chain**:
- **Powder preparation**: Hydrogen-reduced tungsten powder (0.5-10 µm) is blended with dopants. Potassium silicate (0.3-0.6% K₂O + SiO₂) is added for lamp filament wire — the potassium forms microscopic bubbles during sintering that create a "stacked brick" elongated grain structure during wire drawing, preventing grain boundary sliding and sag at 2000-3000°C operating temperature. This "AKS" (Aluminum-Potassium-Silicon) doping is essential for incandescent lamp filaments.
- **Compaction**: Powder is pressed into bars at 100-300 MPa in steel dies or isostatically at 200-400 MPa. Green density: 55-65% of theoretical (19.25 g/cm³). Binders (wax, glycerol, PVA at 0.5-2%) improve green strength for handling.
- **Pre-sintering**: Heat to 900-1200°C in flowing H₂ for 30-60 minutes. Partial inter-particle bonding increases handling strength. Hydrogen atmosphere prevents oxidation and reduces residual oxides.
- **Full sintering**: Heat to 2000-2300°C (direct sintering, resistive self-heating) or 2400-3000°C (indirect sintering in a resistance or induction furnace with W or Mo heating elements). Sintering time: 30 minutes to several hours at peak temperature. Shrinkage: 15-20% linear (40-50% volumetric). Final density: 93-98% of theoretical. Pore closure requires temperatures above 2500°C for extended times.
- **Working**: Sintered tungsten bars are swaged (rotary forging) at 1200-1600°C, then drawn to wire at 800-1200°C through tungsten carbide or diamond dies. Recrystallization occurs around 1300-1500°C — the AKS dopant controls recrystallized grain morphology to prevent brittle equiaxed grain formation.

**Applications**:
- **Incandescent filaments**: 8-50 µm wire coiled into single or double coil (coiled-coil), operating at 2400-3000°C in argon-nitrogen or argon-krypton fill gas. Filament life: 1,000-2,000 hours at 60-100 W. Tungsten evaporates slowly at operating temperature — the inert gas fill slows evaporation by a factor of 10-20 compared to vacuum.
- **TIG welding electrodes**: W-2% ThO₂ (thoriated, radioactive), W-2% CeO₂ (ceriated), W-1.5-2% La₂O₃ (lanthanated). Oxide additions lower work function, improve arc starting, and stabilize the arc. Tip diameter: 0.5-6 mm. Operating current: 5-400 A.
- **Rocket nozzles**: Sintered W or W-Re alloy (W-5%Re or W-26%Re) inserts for solid rocket motor throats. Temperature capability: >3000°C for seconds to minutes. The rhenium addition improves ductility at room temperature (pure tungsten is brittle below its ductile-brittle transition temperature of ~200-400°C).
- **Radiation shielding**: Tungsten's density (19.25 g/cm³, comparable to gold and uranium) makes it effective for X-ray and gamma shielding — used as collimators in medical imaging and radiotherapy. Preferred over lead (11.3 g/cm³) where space is constrained.

**[Molybdenum](../glossary/molybdenum.md)** (mp 2623°C):
- Processed similarly to tungsten: H₂-reduced powder → compact → sinter at 1700-2000°C → work by rolling, forging, or drawing at 1000-1400°C.
- TZM alloy (Mo-0.5%Ti-0.08%Zr-0.02%C): Titanium and zirconium carbide dispersion strengthens molybdenum to 1100-1300°C. Recrystallization temperature raised from ~1000°C (pure Mo) to ~1400°C (TZM). Used for furnace hardware, die-casting cores, and aerospace structural components at 800-1200°C.
- Applications: Glass melting electrodes (Mo resists molten glass corrosion at 1400-1600°C), X-ray tube targets (Mo target for mammography at 17-20 keV characteristic X-rays), heat sinks, and support structures in power electronics.

### Cemented Carbides

Cemented carbides (hardmetals) are composite materials consisting of tungsten carbide (WC) particles bonded with a ductile metal matrix, typically cobalt. They combine extreme hardness (1500-2000 HV30) with useful fracture toughness (8-15 MPa√m) — a combination impossible in single-phase ceramics or metals. The cemented carbide industry consumes ~50,000 tonnes of tungsten annually (50-60% of global tungsten demand).

**WC-Co production chain**:
- **Tungsten carbide synthesis**: Tungsten powder (1-5 µm) + carbon black (6.1-6.3% C by weight) → WC. Carburization at 1400-1600°C in H₂ atmosphere for 1-4 hours in pusher furnaces. Reaction: W + C → WC (ΔH = -35 kJ/mol, exothermic). Temperature control is critical: below 1350°C, incomplete carburization leaves W₂C (brittle eta-phase); above 1650°C, grain coarsening reduces hardness. Carbon content must be held to ±0.05% — sub-stoichiometric WC causes brittle η-phase (Co₃W₃C); excess carbon precipitates as free graphite, weakening the structure.
- **Milling**: WC + Co powder (6-25% Co by weight) milled together in ball mills or attritors for 24-72 hours with milling fluid (acetone, hexane, or water) and pressing aid (2% PEG or paraffin wax). Milling reduces WC grain size, coats WC particles with Co, and homogenizes the mixture. WC grain size after milling: 0.2-5 µm depending on starting powder and milling energy.
- **Compaction**: Uniaxial pressing at 50-200 MPa or cold isostatic pressing (CIP) at 100-300 MPa. Binder (paraffin or PEG) provides green strength for handling complex shapes. Green density: 55-65% of theoretical.
- **Dewaxing and pre-sintering**: Heat to 300-600°C in H₂ or vacuum to remove lubricant/binder. Ramp rate: 0.5-2°C/min to prevent cracking from rapid binder vaporization.
- **Liquid-phase sintering**: The critical step. Heat to 1350-1450°C (above the W-C-Co ternary eutectic at ~1280°C). Cobalt melts and flows by capillary action through the WC particle network, wetting WC particles (contact angle <5°). Liquid-phase sintering proceeds in three stages: rearrangement (Co melt draws WC particles together, 5-10% shrinkage in minutes), solution-reprecipitation (WC dissolves in Co melt at contact points and reprecipitates on larger WC grains — Ostwald ripening, 10-15% additional shrinkage over 30-60 minutes), and final densification (rigid WC skeleton with Co filling remaining pores). Total linear shrinkage: 17-22%. Final density: >99.5% theoretical (essentially pore-free).
- **Grain growth control**: WC grain size determines hardness (Hall-Petch relationship). Nano-grain (<0.2 µm) cemented carbides require grain growth inhibitors: VC (0.3-1.0%), Cr₃C₂ (0.3-0.8%), or TaC (0.5-1.5%). These carbides segregate to WC grain boundaries, pinning them against migration during liquid-phase sintering. Sub-micron grades (0.2-0.5 µm) achieve 1900-2100 HV30 hardness; coarse grades (2-5 µm) trade hardness (1300-1500 HV30) for improved toughness (13-18 MPa√m).

**[Coating systems](../glossary/coating-systems.md)** for cemented carbide cutting tools:
- **[TiN](../glossary/tin.md)** (titanium nitride): Gold-colored PVD coating, 2-5 µm thick. Hardness ~2100 HV. Reduces friction coefficient to 0.4-0.5 (vs. 0.6-0.8 for uncoated WC-Co). Operating temperature limit: ~600°C (TiN oxidizes above this).
- **[TiAlN](../glossary/tialn.md)** (titanium aluminum nitride): Purple/grey PVD coating, 2-4 µm. Hardness ~3200 HV. Al₂O₃ forms in-situ at high temperature, providing oxidation protection to ~900°C. The dominant coating for steel machining.
- **[Al₂O₃](../glossary/alo.md)** (aluminum oxide): CVD coating, 3-10 µm. Thermal barrier — low thermal conductivity protects the substrate from cutting heat. Temperature capability >1000°C. Applied in multilayer CVD: TiC base layer (adhesion) + Al₂O₃ (thermal barrier) + TiN top layer (friction reduction).
- **[DLC](../glossary/dlc.md)** (diamond-like carbon): PVD or PACVD, 1-3 µm. Hardness 2000-5000 HV. Extremely low friction coefficient (0.05-0.15). Used for non-ferrous machining (aluminum, copper) where carbon does not dissolve into the workpiece.

### PM Structural Parts

Conventional press-and-sinter PM produces net-shape or near-net-shape structural components from iron, steel, copper, and aluminum powders at high volume and low cost. The global PM structural parts market exceeds $30 billion annually, dominated by automotive components (60-70% of production).

**Iron-steel PM process**:
- **Powder blend**: Water-atomized iron powder (ASC 100.29, Hoeganäs or equivalent) + graphite powder (0.3-1.0% C) + die lubricant (0.5-0.8% zinc stearate or amide wax). Graphite provides carbon for steel matrix formation during sintering; lubricant reduces ejection force and tool wear during compaction.
- **Compaction**: Double-action mechanical or hydraulic press, 50-800 tonnes capacity, at 400-800 MPa. Fill depth, compaction ratio, and ejection stroke are set per part geometry. Green density: 6.4-7.2 g/cm³ (82-92% of theoretical 7.87 g/cm³ for iron). Higher compaction pressure → higher green density → higher sintered strength, but die wall friction limits uniform density in tall parts.
- **Sintering**: Mesh belt furnace at 1120-1150°C for 20-40 minutes in endothermic gas (70% N₂, 20-28% CO, 2-5% CO₂ + H₂ — produced by partial combustion of natural gas over Ni catalyst) or pure N₂/H₂ blends. Carbon diffusion from graphite into iron transforms the microstructure from ferrite to pearlite (0.3-0.8% C → UTS 350-650 MPa). Sintering in endo gas maintains carbon potential (prevents decarburization or excessive carburization).
- **Properties**: UTS 250-650 MPa, elongation 1-8%, hardness HRB 50-90. Residual porosity: 8-18% (open, interconnected pores). Pore structure limits fatigue strength to ~40% of UTS (vs. 50% for wrought steel of similar composition).
- **Secondary operations**: Sizing (re-pressing at 400-600 MPa for dimensional precision ±0.025 mm), machining (drilling, tapping, turning), steam treatment (400-550°C in superheated steam → Fe₃O₄ surface layer seals pores, increases hardness and corrosion resistance), oil impregnation (fill open pores with oil for self-lubricating bearings — 10-30% oil by volume).

**Copper infiltration**:
- Place copper alloy strips (Cu-5%Fe or Cu-10%Mn) on top of iron green compacts during sintering. At 1120-1150°C, copper melts (mp 1083°C) and infiltrates the interconnected pore network by capillary action. Infiltrated density: 7.3-7.6 g/cm³ (93-97% theoretical). The copper fills pores and creates a dual-phase Fe-Cu structure: UTS 550-850 MPa, improved toughness, and machinability. Used for gears, sprockets, and camshaft synchronizer rings.

**Copper-steel and bronze PM**:
- Bronze bushings (88-90% Cu, 10-12% Sn): Compact at 150-300 MPa, sinter at 780-830°C in H₂/N₂. Oil-impregnated bearings with 20-30% interconnected porosity. PV limit: 1.5-2.0 MPa·m/s. Self-lubricating — oil seeps from pores under load and is re-absorbed when load is removed.
- Copper-graphite electrical contacts: Cu + 5-50% graphite. Low contact resistance with self-lubricating graphite phase. Used in motor brushes, slip rings, and switches.

### Metal Injection Molding (MIM)

MIM combines the shape complexity of plastic injection molding with the material performance of powder metallurgy. It produces small (0.1-200 g), complex metal parts in volumes of 10,000 to several million units per year — the niche where casting is too imprecise and machining is too expensive.

**MIM process chain**:
- **Feedstock preparation**: Fine metal powder (<25 µm, preferably <15 µm, d₉₀ <22 µm) mixed with multi-component polymer binder system to 60-65 vol% powder loading (solid loading). Typical binder: paraffin wax (40-50% of binder) + polypropylene (30-40%) + stearic acid (5-10%) + backbone polymer. Mixing in twin-screw extruder at 150-200°C, 50-150 rpm. Pelletized feedstock is granulated to 1-4 mm pellets for injection molding.
- **Injection molding**: Standard reciprocating screw injection molding machine (25-100 ton clamp). Melt feedstock at 150-200°C, inject at 50-150 MPa into a steel mold at 20-40°C. Cycle time: 10-60 seconds depending on part thickness. Mold design must account for 15-20% linear shrinkage during sintering (volumetric shrinkage ~40-50%). Critical defects: weld lines (where flow fronts meet), short shots (incomplete fill), and voids (trapped air or binder pockets).
- **Debinding**: Remove the binder without disturbing the powder particle arrangement. Two-stage: (1) Solvent debinding — immerse in heptane or acetone at 40-60°C for 4-12 hours to dissolve the paraffin wax component (40-60% of total binder). Creates open pore channels for gas-phase removal of remaining binder. (2) Thermal debinding — heat slowly (0.5-3°C/min) to 400-600°C in H₂/N₂ or pure H₂ to pyrolyze the backbone polymer. Total debinding time: 6-24 hours. Incomplete debinding causes blistering, cracking, or carbon contamination during sintering.
- **Sintering**: Heat to 1200-1400°C (depending on alloy) in H₂, vacuum, or N₂/H₂ atmosphere. Hold 1-4 hours at peak temperature. Densification: 15-20% linear shrinkage, reaching >97% theoretical density (near-full density, unlike conventional PM). Shrinkage is isotropic if powder loading is uniform — this is why feedstock homogeneity is critical.

**MIM materials and properties**:
- **17-4PH stainless steel**: Most common MIM alloy. Sinter at 1260-1350°C, solution treat + age harden (H900: age at 482°C for 1 hour). UTS 1200-1400 MPa, HRC 38-44. Used for medical instruments, firearm components, orthodontic brackets.
- **316L stainless steel**: Sinter at 1360-1400°C in vacuum or H₂. Corrosion resistance comparable to wrought 316L. UTS 500-600 MPa. Used for surgical tools, watch cases, consumer electronics hardware.
- **MIM-4140 chrome-moly steel**: Sinter at 1260-1300°C. Heat treatable to HRC 28-50. UTS up to 1500 MPa after quench and temper.
- Dimensional tolerances: ±0.3-0.5% of dimension (±0.05 mm per 10 mm). Better than investment casting, worse than machining. Critical dimensions can be sized (coined) post-sinter.

### Hot Isostatic Pressing (HIP)

HIP applies simultaneous high temperature and high isostatic pressure (via inert gas, usually argon) to eliminate internal porosity and achieve full density in metal parts. The process exploits plastic yield under hydrostatic pressure: at sufficient pressure and temperature, pores collapse as the surrounding metal yields and diffuses to fill the void.

**HIP process**:
- **Loading**: Encapsulate parts in a sealed container (glass or metal can) if they contain surface-connected porosity. For castings with only internal porosity, no container needed — the skin is already gas-tight.
- **HIP cycle**: Load into a water-cooled pressure vessel with internal graphite or Kanthal (FeCrAl) heating elements. Pressurize with argon to 100-200 MPa (1000-2000 bar) while heating to 1000-1250°C (temperature depends on alloy). Typical cycle: 2-4 hours at temperature + pressure, then cool under pressure. Total cycle time: 8-16 hours including heat-up and cool-down.
- **Equipment**: Pressure vessel: forged steel or wire-wound vessel, 300-1500 mm bore diameter, rated to 200 MPa. Heating elements and insulation fit inside the pressure vessel. Argon gas supply: gas compressor or pump to 200 MPa. Capital cost: $2-10 million depending on vessel size.
- **Mechanisms**: At temperature, the metal's yield strength decreases. Under 100-200 MPa isostatic pressure, the stress around internal pores exceeds the material's yield strength → pore surfaces collapse. Subsequent diffusion bonding across collapsed pore surfaces permanently eliminates the void. Surface-connected porosity requires encapsulation to prevent gas from entering pores (which would equalize pressure and prevent collapse).

**Applications**:
- **Superalloy turbine disks**: HIP investment-cast Ni-base superalloy (IN718, René 88DT) disks at 1160-1220°C, 150 MPa for 4 hours. Eliminates casting microporosity (reduces pore volume from 0.5-2% to <0.01%), improving fatigue life by 3-10×. Cost savings: HIP allows conventional casting to replace directionally solidified or single-crystal casting for components that don't need the grain structure control.
- **Titanium aerospace castings**: Ti-6Al-4V investment castings HIPped at 920-960°C, 100-140 MPa. Eliminates internal shrinkage porosity, achieving near-wrought mechanical properties from castings (fatigue strength improves from ~60% to ~90% of wrought).
- **PM tool steels**: Gas-atomized tool steel powder (M2, M4, T15, CPM 10V) sealed in steel cans, HIPped at 1100-1200°C, 150 MPa for 4-6 hours. Produces fully dense billets with ultra-fine, uniformly distributed carbide microstructure (carbide size 1-5 µm vs. 10-30 µm in conventional ingot tool steel). Superior wear resistance and toughness — used for cold forming dies, powder compaction tooling, and high-performance cutting tools.
- **Diffusion bonding**: HIP can diffusion-bond dissimilar metals (e.g., Ti-to-stainless, Cu-to-Al) across prepared interfaces under pressure and temperature, without melting. Joint strength approaches parent metal.

### Additive Manufacturing (AM) of Metals

Metal AM builds parts layer-by-layer from digital models, eliminating tooling and enabling geometries impossible by any other process (internal channels, lattice structures, topology-optimized lightweight components). Three mature metal AM processes have industrial relevance:

**Selective Laser Melting (SLM) / Laser Powder Bed Fusion (LPBF)**:
- A laser (200-1000 W fiber laser, 1070 nm wavelength) selectively melts thin layers of metal powder (20-50 µm layer thickness) spread by a recoater blade across a build platform. The process occurs in an inert atmosphere (Ar or N₂, O₂ <0.1%) to prevent oxidation. Scan speed: 200-2000 mm/s. Hatch spacing: 0.05-0.15 mm. Build rate: 5-30 cm³/h.
- Powder requirements: Spherical gas-atomized powder, 15-45 µm size range. Powder recycling (sieving to remove spatter and partially melted particles) is necessary every 1-3 builds.
- Materials: Ti-6Al-4V (most common AM alloy, sinter at 1650-1800°C effective melt pool temperature, build platform 80-200°C), 316L/17-4PH stainless steel, AlSi10Mg (build platform 150-200°C, stress relief required), Inconel 718/625, CoCrMo.
- As-built surface roughness: Ra 5-20 µm (staircase effect from layer-by-layer building). Post-processing: support removal, stress relief heat treatment, HIP (mandatory for fatigue-critical aerospace parts), machining of mating surfaces.
- Residual stress: Large thermal gradients (10⁴-10⁶ K/m) during laser melting create residual stresses up to 50-80% of yield strength. Stress relief heat treatment (e.g., 600-650°C for Ti-6Al-4V, 1065°C for IN718) is mandatory before removal from build plate. Build plate preheating (80-300°C depending on alloy) reduces thermal gradients and residual stress.

**Electron Beam Melting (EBM)**:
- Electron beam (3000-6000 W, 60 kV accelerating voltage) melts powder layers (50-100 µm thick) in high vacuum (10⁻³-10⁻⁴ mbar). Beam deflection by electromagnetic coils — no moving mirrors, faster than laser scanning.
- Build temperature: 600-1000°C (the entire powder bed is preheated). High build temperature reduces residual stress and enables building of crack-prone alloys (TiAl intermetallics, CMSX-4 single-crystal superalloy).
- Powder: Spherical, 45-105 µm (coarser than SLM — higher layer thickness and beam diameter). Build rate: 30-80 cm³/h (faster than SLM due to higher power and thicker layers).
- Surface roughness: Ra 20-35 µm (rougher than SLM due to coarser powder and partially sintered powder adhering to surfaces). Niche applications: orthopedic implants (porous surface for bone ingrowth — the partially sintered surface is a feature, not a defect), aerospace brackets, turbine blades.

**Directed Energy Deposition (DED)**:
- Metal powder (or wire) is fed directly into a focused energy beam (laser, 1-10 kW, or electron beam) to build features on existing substrates. Build rate: 10-300 cm³/h (much faster than PBF). Resolution: 0.5-2 mm track width (much coarser than PBF).
- Applications: Large part repair (turbine blade tip repair — deposit ~1 mm of Ni alloy onto worn blade tips and machine back to dimension), feature addition (adding bosses, flanges onto forged or cast substrates), cladding (wear/corrosion resistant surface layers), and rapid prototyping of large structures (up to several meters).
- Materials: Same as PBF plus dissimilar material combinations (gradient structures). Stellite (CoCrW) hardfacing on valve seats, WC/Ni-based composite cladding on wear surfaces.

**Binder jetting**:
- Inkjet print head deposits liquid binder onto powder bed (metal powder, 15-45 µm). No melting during printing — the part is a fragile "green" body held together by binder. Post-process: cure at 200°C to cross-link binder, then sinter at 1200-1400°C in H₂ or vacuum to burn off binder and densify the metal. Shrinkage: 15-20% linear (same as MIM sintering).
- Advantages: No residual stress (no thermal gradients during printing), no support structures needed (unfused powder supports overhangs), fast build rate (100-500 cm³/h), scalable to large parts (build volumes up to 800 × 500 × 400 mm).
- Disadvantages: Lower density (97-99% vs. >99.5% for PBF), higher surface roughness (Ra 6-15 µm after sintering), and dimensional control limited by sintering shrinkage variability. Best suited for medium-volume production of complex parts where fatigue properties are not critical.

### Self-Propagating High-Temperature Synthesis (SHS)

SHS (also called combustion synthesis) exploits highly exothermic powder reactions to synthesize refractory compounds. Once ignited, the reaction front propagates through the powder compact at 1-100 mm/s, reaching temperatures of 2000-4000°C without external heating. The process is fast, energy-efficient (requires no furnace — the reaction provides its own heat), and produces extremely pure products because volatile impurities are vaporized at combustion temperatures.

**SHS process**:
- **Reactant preparation**: Blend elemental powders in stoichiometric ratio (e.g., Ti + C for TiC, Ti + B for TiB₂, Mo + 2Si for MoSi₂). Press into a green compact at 50-200 MPa or fill into a graphite die. Green density: 50-70% theoretical.
- **Ignition**: Heat one end of the compact with an electrically heated tungsten coil, laser, or exothermic chemical igniter to the ignition temperature (typically 800-1500°C, depending on system). The reaction initiates and the combustion front propagates through the compact.
- **Combustion wave**: The front temperature reaches 2000-4000°C depending on the thermodynamics of the reaction. Ti + C → TiC: adiabatic combustion temperature 3210°C, ΔH = -185 kJ/mol. Ti + 2B → TiB₂: T_ad = 3190°C, ΔH = -280 kJ/mol. Mo + 2Si → MoSi₂: T_ad = 1900°C, ΔH = -131 kJ/mol. The reaction is self-sustaining as long as heat generation at the front exceeds heat losses to the environment.
- **Product**: The synthesized compound forms in the combustion wave. Product is typically porous (30-50% porosity) due to the volume change from reactants to product and gas evolution from impurities. Dense products require simultaneous application of pressure (SHS + pressing: load compact into a hydraulic press immediately after combustion, apply 50-200 MPa while still hot) or hot pressing during synthesis.

**SHS products and applications**:
- **TiC**: Hardness 2800-3200 HV, used in cermets (TiC-Ni-Mo binder) for steel finishing tools. Combustion synthesis avoids the 2000°C+ furnace temperature required for conventional TiC sintering.
- **TiB₂**: Electrical conductor (resistivity ~15 µΩ·cm), hardness 2500-3500 HV, excellent wear resistance. Used as cathode coating in aluminum Hall-Héroult cells (resists molten Al and cryolite at 960°C) and as armor ceramics.
- **MoSi₂**: Intermetallic with excellent oxidation resistance (forms protective SiO₂ layer at 1000-1700°C). Used as heating elements in high-temperature furnaces (operating temperature up to 1700°C in air — higher than any metallic element). Brittle at room temperature (ductile above ~1000°C).
- **Cermets**: TiC or Ti(C,N) based composites with Ni-Mo binder. Combustion synthesis produces ultra-fine TiC grain (0.5-2 µm) in a single step. Hardness 1400-1800 HV, toughness 8-12 MPa√m. Used for high-speed finishing of steel — lower coefficient of friction than WC-Co, reducing built-up edge on the cutting tool.

### Safety & Hazards

**Metal powder handling**:
- Fine metal powders (<50 µm) are explosion hazards. Titanium, aluminum, and magnesium powders are pyrophoric (ignite spontaneously in air when suspended as dust clouds). Minimum ignition energy (MIE): Ti powder ~5 mJ, Al powder ~15 mJ — static discharge provides enough energy to ignite. Minimum explosive concentration (MEC): 30-100 g/m³ for most metal powders.
- Housekeeping: Eliminate powder accumulations on surfaces. Use wet cleaning methods or HEPA vacuum systems — never dry-sweep or blow with compressed air (creates dust clouds). Equipment must be grounded and bonded to prevent static accumulation.
- Inerting: Process reactive powders (Ti, Al, Zr, Ta) under argon or nitrogen atmosphere with O₂ monitoring (<5% O₂). Glove box operations for fine Ti powder handling.
- PPE: Respiratory protection (P100 or P3 filters minimum) for all powder handling — metal fume and powder inhalation causes metal fume fever (Zn), pulmonary fibrosis (Al), hard metal lung disease (WC-Co), and sensitization (Ni, Co, Be). Full-face respirator or powered air-purifying respirator (PAPR) for high-exposure tasks. Nitrile gloves and anti-static clothing.

**Sintering furnace hazards**:
- Hydrogen atmosphere furnaces: H₂ flammable range 4-75% in air, ignition energy 0.017 mJ. Furnace purge with N₂ before introducing H₂; purge with N₂ before opening to air. Continuous H₂ monitoring with automatic N₂ purge on H₂ leak detection. Flashback arrestors on all H₂ supply lines.
- Vacuum furnaces: Risk of rapid air ingress if water-cooled jacket leaks — water vaporizes, pressure spikes, vacuum seal fails. Install over-pressure relief and water leak detection systems. Water-moderated implosion hazard on large vacuum vessels.
- High-temperature burns: Furnace exterior surfaces at 50-200°C during operation. Interior refractory and heating elements at 1000-3000°C. Lock-out/tag-out procedures for furnace maintenance. Cool to <50°C before internal access.

**Cobalt and tungsten carbide exposure**:
- Hardmetal workers exposed to WC-Co dust have elevated risk of "hard metal lung disease" (giant cell interstitial pneumonia). Co alone is less toxic than the WC-Co combination — WC particles appear to act as carriers that enhance Co uptake by lung cells. Exposure limit: 0.02 mg/m³ (ACGIH TLV for Co in WC-Co). Wet grinding of cemented carbides is mandatory — dry grinding generates inhalable WC-Co dust.
- Cobalt skin sensitization: Co is a potent skin sensitizer (causes allergic contact dermatitis). Handle Co powder and WC-Co green compacts with gloves. Monitor personal exposure through biological sampling (urinary Co <15 µg/L).

**Carbonyl compounds**:
- Nickel carbonyl Ni(CO)₄: Extremely toxic gas (TLV 0.001 ppm). Colorless, volatile (bp 43°C), readily absorbed through lungs and skin. Symptoms: headache, nausea, chest pain at low exposure; pulmonary edema and death at high exposure. Carbonyl nickel plants require continuous air monitoring, sealed process equipment, and thermal destructors on exhaust streams. Emergency response: immediate evacuation, SCBA for rescue, chelation therapy (sodium diethyldithiocarbamate) for exposed personnel.
- Iron pentacarbonyl Fe(CO)₅: Less toxic than Ni(CO)₄ but still hazardous (TLV 0.1 ppm). Decomposes to fine iron oxide fume — both the carbonyl and decomposition products require exposure control.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Metals](./index.md) • [All Domains](../index.md)*