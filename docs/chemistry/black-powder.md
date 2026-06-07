# Black Powder

> **Node ID**: chemistry.explosives.black-powder
> **Domain**: [Chemistry](./index.md)
> **Parent**: [Explosives & Propellants](explosives.md)
> **Dependencies**: [`energy.charcoal`](../energy/charcoal.md)
> **Enables**: [`mining.black-powder`](../mining/black-powder.md)
> **Timeline**: Years 5-10
> **Outputs**: black_powder
> **Critical**: No


## Black Powder

**Chemistry**: 75% KNO₃ (potassium nitrate), 15% charcoal, 10% sulfur. The three components serve distinct roles: nitrate provides oxygen for rapid combustion, charcoal is the fuel, sulfur lowers ignition temperature and increases burn rate.

The combustion proceeds in two stages. Sulfur ignites first (ignition temperature ~190°C, vs ~340°C for charcoal alone with KNO₃). The burning sulfur heats the surrounding mixture enough to decompose KNO₃ into KNO₂ + ½O₂. The released oxygen gas then reacts with carbon from the charcoal: C + O₂ → CO₂ (ΔH = -393 kJ/mol) and 2C + O₂ → 2CO (ΔH = -221 kJ/mol). The overall reaction for the standard 75:15:10 mixture produces roughly 40% gaseous products (CO₂, CO, N₂, H₂O vapor, and some H₂S from sulfur) and 60% solid residue (K₂CO₃, K₂SO₄, K₂S). The solid residue is the white smoke characteristic of black powder. The gas volume at STP is approximately 280 L/kg, generating peak pressures of 2,000-6,000 bar in confined spaces depending on grain size and loading density.

**Prerequisites**:
- [Potassium nitrate (saltpeter)](../mining/black-powder.md) production or collection (from nitre beds, bat guano caves, or synthetic production via ammonia oxidation)
- [Charcoal](../energy/charcoal.md) production from hardwood (willow and alder preferred for fastest burn rate; softwoods produce more ash but are usable)
- Sulfur collection (volcanic deposits, native sulfur, or recovery from [sulfide ore roasting](../metals/non-ferrous.md))
- Stone burr mill or [ball mill](../machine-tools/forming.md) for grinding ingredients separately
- Corning mill or screw press for granulation
- Sieves for grain size classification

**Materials**:
- Potassium nitrate (KNO₃), dried and crushed
- [Charcoal](../energy/charcoal.md) (willow or alder preferred, softwood acceptable)
- Sulfur, powdered
- Water or alcohol for moistening

**Manufacture**:

1. **Pulverize each ingredient separately** to fine powder (~100 mesh). Grind with stone burr mill or ball mill. NEVER grind mixed ingredients. Friction can ignite black powder.
2. **Mix thoroughly**: layer ingredients on cloth, roll and tumble for 30+ minutes. Or use a wheel mill (heavy stone wheels rotating in a pan, dampened with water, safer than dry mixing). The wheel mill was the standard method for centuries: two granite wheels (each 500-1000 kg) rotate in a circular pan (2-3 m diameter) containing the dampened ingredients. The wheels crush, mix, and incorporate the materials in a single operation. Water dampening prevents ignition during mixing. The wheel mill operator must be experienced: too much water makes the mixture muddy and hard to granulate; too little water risks ignition.
3. **Moisten slightly** with water (or alcohol), press into cakes in a corning mill or screw press at 5-10 MPa. The pressure compacts the mixture into a solid cake that will hold together for granulation. Corning is the process of breaking the pressed cakes into grains of specific size. The term comes from "corn" (grain), referring to the grain-like particles produced.
4. **Dry cakes carefully** in a well-ventilated room at 30-40°C. Never use direct heat or open flame for drying. The drying room should have conductive flooring (to prevent static buildup) and be separated from other buildings by at least 30 m.
5. **Crush and sieve** to desired grain size:
   - **[Coarse grain](../glossary/coarse-grain.md)** (2-4 mm): slower burn, more lifting power. Used for mining and quarrying.
   - **[Fine grain](../glossary/fine-grain.md)** (<1 mm): faster burn, more shattering. Used for firearms and blasting.
   - **[FFFg](../glossary/fffg.md)** (extra fine): fast-burning sporting powder for small arms.
6. **Polish (glaze)**: tumble grains with graphite powder in a rotating drum. The graphite coating reduces static sensitivity, improves flow characteristics, and provides a measure of moisture resistance.

**Properties**: Burn rate 300-600 m/second (deflagration, not detonation). Produces large volume of gas (~40% of solid mass converts to gas) and solid residue (~60%, smoke and ash). Velocity of detonation: ~400 m/s (low for an explosive, this is a low explosive). Energy: 2.6 MJ/kg. Sensitive to spark, friction, and static electricity.

**Grain size and burn rate**:

| Grade | Grain Size (mm) | Burn Rate (relative) | Application | Typical Use |
|-------|-----------------|---------------------|-------------|-------------|
| Fg (coarse) | 2.0-4.0 | Slow | Mining, quarrying, cannon | Heavy blasting charges |
| FFg | 1.0-2.0 | Moderate | Large-bore firearms | Muskets, rifles >0.50 cal |
| FFFg | 0.5-1.0 | Fast | Small-bore firearms | Pistols, rifles <0.50 cal |
| FFFFg (extra fine) | <0.5 | Very fast | Flash pan, priming | Flintlock priming, fuse composition |
| Meal powder | Dust | Extremely fast (uncontrolled) | Intermediate, not used directly | Feed stock for corning |

Finer grains burn faster because the surface area per unit mass is larger. The corning process (pressing, crushing, sieving) controls grain geometry to produce uniform, predictable burn rates. Uncorned meal powder burns erratically and is far more sensitive to accidental ignition.

**Saltpeter production parameters**:

| Method | Feedstock | Yield (KNO₃) | Cycle Time | Notes |
|--------|-----------|---------------|------------|-------|
| Nitre bed | Animal waste + wood ash + soil | 1-5 kg/m²/year | 6-12 months | Traditional method, needs warm climate |
| Bat guano leaching | Cave bat guano | 10-30% by weight | Days (extraction) | Limited to guano caves, high yield |
| Synthetic (ammonia oxidation) | NH₃ + O₂ over Pt catalyst | 90-95% conversion | Hours | Requires [ammonia production](ammonia.md) and platinum catalyst |
| Calcium nitrate + K₂CO₃ | Limestone + potassium carbonate | 80-85% yield | Hours | Double displacement, precipitates CaCO₃ |

**Safety & Handling**:

> **Safety warning**: Black powder is sensitive to spark, friction, and static electricity during manufacture. Grind ingredients separately, never mixed. Ground all metal equipment. Wear cotton clothing, not synthetic. Maintain humidity above 50% in work areas.

Storage requires a dry, cool, well-ventilated magazine away from other structures. Moisture degrades performance. Keep away from open flame and heat sources. Handle with non-sparking tools (bronze or beryllium copper). Black powder deflagrates rapidly but does not detonate. Even so, a kilogram of powder in a confined space produces a destructive pressure wave. Treat all quantities with respect. Never smoke within 50 m of powder storage or handling areas.

**Specific hazards during manufacture**:
- **Ignition during grinding**: Stone burr mills generate friction heat. If KNO₃, charcoal, and sulfur are present together, friction or a spark between mill stones ignites the mixture. The accident record from historical powder mills is grim: explosions killed operators and leveled buildings. The rule is absolute: grind each ingredient alone, in separate equipment if possible, and clean the mill between batches.
- **Static discharge during mixing**: Wheel mills and screening operations generate static electricity on dry days. A 0.1 mJ spark (imperceptible to humans) ignites black powder. Ground the mill frame to a copper rod driven into damp earth. Maintain 65% relative humidity by misting the work area with water. Operators must wear conductive wrist straps grounded to the mill frame.
- **Dust explosion**: Airborne black powder dust at concentrations above 40 g/m³ is explosive. This concentration is easily reached during crushing and sieving. Use wet methods wherever possible (dampened ingredients in wheel mill). If dry sieving is necessary, do it in small batches with local exhaust ventilation.
- **Sulfur dioxide exposure**: Burning black powder produces SO₂ (IDLH 100 ppm, immediately dangerous to life and health). Enclosed spaces (tunnel blasting, mine galleries) become lethal within minutes of a large powder ignition. Ventilate for at least 15-30 minutes after blasting before re-entry. Test with a CO/SO₂ detector.

**Blasting procedure**: Drill hole (2.5-4 cm diameter, 0.5-2 m deep) with jumper drill. Clean hole with scraper. Fill bottom 1/3 with powder. Insert safety fuse (black powder core in tarred cotton sheath, cut to length for 30-60 second delay). Tamp remaining hole with clay or damp sand (NOT dry sand; sparks from tamping rod ignite powder). Light fuse, retreat. 1-2 kg powder breaks 2-10 m³ rock depending on placement. The blaster must ensure all personnel are clear of the blast area before lighting the fuse. A shouted warning ("Fire!") is the traditional signal. After the blast, wait several minutes for dust and fumes to clear before approaching the muck pile (broken rock). Check for misfires before allowing personnel to work in the area.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Powder burns slowly, produces weak blast | Moisture contamination (>1% water content) or under-mixed ingredients | Store in sealed containers with desiccant; dry powder at 40-50°C before use; ensure wheel mill runs 2-4 hours per batch for thorough incorporation |
| Powder fails to ignite from fuse | Sulfur content too low, or fuse not in contact with powder | Maintain 10% sulfur in mixture; ensure fuse extends into powder charge, not just above it; test fuse ignition reliability by burning 1 m of fuse and timing (should be 60-90 seconds per meter) |
| Powder ignites during wheel milling | Excessive friction from dry mixture or foreign object (stone, metal) between wheels | Maintain moisture at 3-5% during milling (damp but not muddy); inspect wheel path for foreign objects before each batch; never mill dry |
| Inconsistent burn rate between batches | Grain size variation from improper corning or sieving | Use standardized sieves with verified mesh sizes; press cakes at consistent pressure (5-10 MPa); crush and sieve in controlled batches |
| Powder cakes into solid lump in storage | Moisture absorption from humid air (KNO₃ is hygroscopic) | Store in airtight containers (sealed clay jars or metal cans with gasket); add silica gel desiccant packets; inspect monthly and re-sieve if caked |
| Excessive smoke and fouling in firearm | Sulfur too high (>12%) or charcoal from softwood (more volatiles) | Reduce sulfur to 10%; use hardwood charcoal (willow, alder) which burns cleaner; ensure complete mixing to avoid sulfur-rich pockets |
| Saltpeter (KNO₃) contaminated with NaCl | Impure nitrate bed leaching or incomplete recrystallization | Dissolve crude KNO₃ in hot water, filter, and recrystallize by cooling; NaCl remains in solution while KNO₃ crystallizes at lower temperature |
| Pressed cakes crumble instead of holding together | Insufficient moisture during pressing or pressure too low | Add 3-5% water (or 2-3% alcohol) before pressing; increase press pressure to 5-10 MPa; hold pressure for 30-60 seconds to allow binder action |
| Misfire in borehole (charge fails to ignite) | Damp hole flooded charge, or fuse severed during tamping | Protect charge with waterproof paper wrapper; use clay stemming, not water; verify fuse integrity after tamping by gentle pull test |
| Powder produces orange/yellow flame instead of white flash | Charcoal from softwood or insufficient grinding of charcoal | Use hardwood charcoal ground to <100 mesh; softwood charcoal produces more volatile organics that color the flame yellow |

## Quantitative Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Standard composition | 75% KNO₃, 15% charcoal, 10% sulfur | By weight |
| Ignition temperature | ~270-300°C | Lowered from ~340°C by sulfur |
| Deflagration velocity | 300-600 m/s | Depends on grain size and confinement |
| Gas volume produced | ~280 L/kg at STP | 40% of mass converts to gas |
| Peak pressure (confined) | 2,000-6,000 bar | In sealed vessel, depends on loading density |
| Energy density | 2.6-3.0 MJ/kg | Roughly 1/5 that of dynamite |
| Sensitivity to impact | 1.5 J (50% probability) | Moderate; less sensitive than NG |
| Sensitivity to friction | Variable, ignites at ~120 N on ceramic plate | Highly sensitive to friction when dry |
| Shelf life | 10+ years when kept dry (<0.5% moisture) | Indefinite in sealed containers |
| Freezing point of NG dynamite | 13°C | Solidified NG is shock-sensitive; thaw carefully |

**Applications**: Mining and quarrying (historical primary explosive before dynamite), firearms propellant, fireworks, fuse composition. Black powder doubles as propellant and blasting explosive. It remained the sole explosive available to civilization for centuries, from its discovery in China (~800 AD) through the introduction of nitroglycerin in the 1840s. Even after dynamite replaced black powder for most blasting, it continued as the standard firearms propellant until the adoption of smokeless powder in the 1890s. In a bootstrapping civilization, black powder is the first explosive available and the foundation upon which all later nitration chemistry builds.

**Strengths**:
- Simplest explosive to manufacture from basic materials (saltpeter, charcoal, sulfur)
- Stable in storage when kept dry (can last decades in sealed containers)
- Burn rate tunable by grain size (coarse for lifting, fine for shattering)
- Low-cost for quarrying and mining
- Doubles as propellant for firearms
- Well-understood after 1200 years of use

**Weaknesses**:
- Low brisance (400 m/s detonation velocity, poor shattering effect)
- Produces 60% solid residue (heavy smoke obscures vision and fouls gun barrels)
- Hygroscopic; moisture degrades performance and can cause misfires
- Sensitive to spark, friction, and static electricity during manufacture
- Much less powerful than nitroglycerin-based explosives (1/5 the energy per unit mass of dynamite)

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [Explosives & Propellants](explosives.md)*
