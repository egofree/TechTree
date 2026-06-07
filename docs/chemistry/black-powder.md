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

**Safety & Handling**:

> **Safety warning**: Black powder is sensitive to spark, friction, and static electricity during manufacture. Grind ingredients separately, never mixed. Ground all metal equipment. Wear cotton clothing, not synthetic. Maintain humidity above 50% in work areas.

Storage requires a dry, cool, well-ventilated magazine away from other structures. Moisture degrades performance. Keep away from open flame and heat sources. Handle with non-sparking tools (bronze or beryllium copper). Black powder deflagrates rapidly but does not detonate. Even so, a kilogram of powder in a confined space produces a destructive pressure wave. Treat all quantities with respect. Never smoke within 50 m of powder storage or handling areas.

**Blasting procedure**: Drill hole (2.5-4 cm diameter, 0.5-2 m deep) with jumper drill. Clean hole with scraper. Fill bottom 1/3 with powder. Insert safety fuse (black powder core in tarred cotton sheath, cut to length for 30-60 second delay). Tamp remaining hole with clay or damp sand (NOT dry sand; sparks from tamping rod ignite powder). Light fuse, retreat. 1-2 kg powder breaks 2-10 m³ rock depending on placement. The blaster must ensure all personnel are clear of the blast area before lighting the fuse. A shouted warning ("Fire!") is the traditional signal. After the blast, wait several minutes for dust and fumes to clear before approaching the muck pile (broken rock). Check for misfires before allowing personnel to work in the area.

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
