# Explosives

> **Node ID**: chemistry.explosives
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.acids`](acids.md), [`chemistry.alkalis`](alkalis.md), [`energy.charcoal`](../energy/charcoal.md)
> **Enables**: [`mining.black-powder`](../mining/black-powder.md), [`metals.finishing`](../metals/finishing.md)
> **Timeline**: Years 5-30+
> **Outputs**: black_powder, nitrocellulose, dynamite, smokeless_powder
> **Critical**: No — explosives accelerate mining and construction but are not prerequisites for core capabilities


A civilization without explosives can dig with hand tools, but it cannot efficiently extract ore from hard rock, cut roads through mountains, or demolish structures larger than a hut. Mining with chisel and hammer advances inches per day in granite. Quarrying building stone without blasting wastes enormous labor. Tunneling through rock with manual tools takes years for modest distances. Explosives compress that work into seconds.

Explosives provide two distinct effects. *Brisance* (shattering force) pulverizes hard rock into fragments. *Heaving force* (gas expansion) moves the broken material aside and heaves soft strata like coal. Different explosives emphasize one or the other, and choosing the right tool for the job determines whether a blast produces useful fragmentation or wasted energy.

The progression runs from black powder, the simplest explosive made from three common materials, through nitration chemistry that yields nitrocellulose, nitroglycerin, and dynamite, to high explosives like TNT and RDX for military and industrial use. At the industrial scale, ANFO dominates mining worldwide because it is cheap, safe to handle, and effective in large boreholes. This article covers each explosive in manufacturing order, because each tier builds on the materials and capabilities established by the ones before it.

The article also covers the systems needed to use explosives safely and effectively: blasting caps and initiating systems to detonate high explosives, blasting design parameters to calculate charge sizes and patterns, and vibration and airblast control to protect nearby structures. Without these supporting systems, even the best explosive produces poor results, or worse, kills the people using it.

The history of explosives mirrors the history of industrial civilization. Black powder enabled the first large-scale mining operations in medieval Europe and China. Dynamite opened the possibility of major earthmoving projects: the transcontinental railroads, the Suez and Panama canals, the deep-level gold mines of South Africa. TNT and RDX enabled the mechanized warfare of the 20th century. ANFO made modern open-pit mining economically viable. At each stage, the availability of a new explosive reshaped what civilization could build, extract, and destroy.

## Tier 1: Black Powder Era

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


## Tier 2: Nitration Chemistry

## Nitrocellulose (Guncotton)

**Chemistry**: Cellulose (cotton linters or wood pulp) + nitric acid + sulfuric acid produces nitrocellulose (cellulose nitrate). Nitration substitutes -NO₂ groups onto cellulose hydroxyls. Degree of nitration determines properties:

- **[Guncotton](../glossary/guncotton.md)** (12.5-13.5% nitrogen): Highly nitrated. Burns rapidly without residue. Insoluble in common solvents. Used as propellant base and explosive.
- **[Pyroxylin / collodion cotton](../glossary/pyroxylin-collodion-cotton.md)** (10.5-12% nitrogen): Lower nitration. Soluble in ether-alcohol and acetone. Used for lacquers, film base, dope.

**Prerequisites**:
- [Mixed acid production](acids.md) (HNO₃ + H₂SO₄)
- Cotton linters or wood pulp (cellulose source)
- Temperature-controlled reaction vessel with cooling
- Large volume water supply for washing and quenching

**Materials**:
- [Nitric acid](acids.md) (concentrated, 90%+)
- [Sulfuric acid](acids.md) (concentrated, 96-98%)
- Cotton linters or wood pulp (clean, dry cellulose)
- Copious water supply for washing

**Manufacture**:

1. **Prepare mixed acid**: Combine HNO₃ + H₂SO₄ to the target composition. Typical mixed acid for guncotton: 21% HNO₃, 63% H₂SO₄, 16% H₂O by weight. The sulfuric acid acts as a dehydrating agent, absorbing the water produced by nitration and driving the reaction forward.
2. **Prepare cellulose**: Use clean, dry cotton linters (short fibers from ginning) or high-alpha wood pulp. Cut into manageable pieces. Dry thoroughly (residual water dilutes the mixed acid and reduces nitration). Moisture content must be below 2%.
3. **Soak cellulose** in mixed acid at 20-30°C for 30-60 minutes. Use approximately 15 parts mixed acid to 1 part cellulose by weight (excess acid ensures complete nitration and heat absorption). Nitration is strongly exothermic. Cool continuously to prevent runaway reaction (thermal decomposition leads to fire and explosion). Agitate gently to ensure uniform contact between acid and cellulose.
4. **Quench**: Dump the nitrated cellulose into a large volume of cold water (at least 20× the acid volume) to stop the reaction instantly. The dilution also begins the washing process.
5. **Wash extensively** with boiling water to remove all residual acid. Incomplete washing produces unstable product that can decompose spontaneously. Continue washing until the wash water tests neutral (pH 7) with litmus or pH paper. This may require dozens of wash cycles over several days.
6. **Stabilize**: Boil in water for hours (sometimes days for large batches) to remove unstable low-nitration products and dissolved degradation products. Some processes use multiple boiling stages with fresh water each time. The goal is to remove every trace of acid trapped in the cellulose fibers.
7. **Pulverize**: Beat or chop the nitrated cellulose into a uniform fibrous mass. This increases surface area for drying and improves uniformity.
8. **Dry** at moderate temperature (40-50°C) with good air circulation. Avoid overheating during drying. The dried product should be white and fluffy (guncotton) or slightly off-white.

**Properties**: Energy density 3× black powder. Burns rapidly without residue (cleaner than black powder). Properties tunable via degree of nitration (guncotton vs pyroxylin). Soluble forms (pyroxylin) enable lacquers, film base, and propellant gel formulation.

**Safety & Handling**:

> **Safety warning**: Nitration is strongly exothermic. Temperature control is critical. Runaway reaction causes fire and explosion. Residual acid in the product causes spontaneous decomposition. Wash and boil extensively until wash water tests neutral. Degradation products (NO₂) autocatalyze further decomposition in storage.

Mixed acid (HNO₃ + H₂SO₄) causes severe chemical burns. Wear acid-resistant gloves, face shield, and rubber apron. Have copious water supply for immediate flushing. Neutralize spills with limestone or sodium bicarbonate. Store nitrocellulose in cool, dry conditions. Old or discolored material may be unstable.

**Applications**: Propellant base for [single-base smokeless powder](../glossary/single-base.md), explosive, lacquers and film base (pyroxylin form), dope for fabric aircraft covering, early photographic film (celluloid, made from pyroxylin + camphor plasticizer). Nitrocellulose is the foundation of the entire smokeless powder industry. Without it, firearms remain limited to black powder performance: heavy smoke, limited range, and rapid barrel fouling. Pyroxylin's solubility in ether-alcohol also made it the first practical plastic (celluloid, 1860s), enabling photography, film, and early molded goods.

**Strengths**:
- Burns rapidly without residue (cleaner than black powder)
- Energy density 3× black powder
- Tunable properties via degree of nitration (guncotton for explosives and propellants, pyroxylin for lacquers and plastics)
- Soluble forms enable lacquers, film base, and propellant gel formulation
- Foundation of the smokeless powder industry and early plastics (celluloid)

**Weaknesses**:
- Strongly exothermic nitration requires precise temperature control
- Residual acid causes spontaneous decomposition, requires extensive washing and boiling
- Degradation products (NO₂) autocatalyze further decomposition in storage
- Mixed acid handling is extremely hazardous
- Long stabilization process (days of boiling) is labor and energy intensive


## Nitroglycerin

**Chemistry**: Glycerol + mixed acid (HNO₃ + H₂SO₄) at 10-15°C. The nitration substitutes three nitro groups onto the glycerol molecule. Overall: C₃H₅(OH)₃ + 3HNO₃ → C₃H₅(ONO₂)₃ + 3H₂O.

**Prerequisites**:
- [Mixed acid production](acids.md) (HNO₃ + H₂SO₄)
- Glycerol (99%+ purity, from [fat saponification](soap.md) or synthetic production)
- Lead-lined steel nitrator with cooling coils and agitator
- Emergency dump valve and drowning tank (water-filled, at least 20× the nitrator volume)
- Remote blast-resistant facility with blast shields between operator and reaction vessel
- Sodium carbonate for washing

**Materials**:
- Glycerol (99%+ purity, no water)
- [Nitric acid](acids.md) (90-98% concentrated)
- [Sulfuric acid](acids.md) (96-98% concentrated)
- Sodium carbonate (for washing)
- Copious water for washing

**Manufacture**:

1. **Prepare mixed acid**: Combine ~50% HNO₃ and ~50% H₂SO₄ by weight. The ratio is approximately 1 part glycerol to 6 parts mixed acid.
2. **Cool the nitrator** to 10-15°C. The nitrator vessel is lead-lined steel with cooling coils, an agitator, and a temperature-actuated emergency dump valve that discharges the contents into a large water-filled drowning tank if temperature exceeds 20°C.
3. **Add glycerol slowly** to the mixed acid with continuous agitation. The reaction is exothermic (ΔH ≈ -370 kJ/mol of glycerol). Temperature must stay below 15°C. If temperature exceeds 20-25°C, side reactions accelerate, producing unstable nitro compounds. Above 50°C, catastrophic runaway is possible.
4. **Continue nitration** for 30-60 minutes with temperature control.
5. **Settle and separate**: Allow the mixture to settle. Nitroglycerin (density 1.59 g/cm³) separates as the lower layer beneath the spent acid. Draw off the NG layer.
6. **Wash**: First with cold water (removes bulk acid), then with sodium carbonate solution (neutralizes residual acid), then with water again until the wash water tests neutral. Even trace residual acid makes NG unstable over time (acid-catalyzed decomposition).
7. **Final product**: Pale yellow, oily liquid.

**Properties**: Detonation velocity 7,700 m/s. Density 1.59 g/cm³. Energy 6.4 MJ/kg. Freezes at 13°C. Impact sensitivity: 2 J initiation energy. One of the most powerful liquid explosives, 1.5× black powder energy per unit mass.

**Safety & Handling**:

> **Safety warning**: Liquid nitroglycerin detonates from impact, friction, or rapid temperature change. A hammer blow on a hard surface can initiate it. Dropping a glass container of NG can detonate it. Synthesize only in remote blast-resistant facilities with blast shields between operator and reaction vessel. Never handle in quantities >10 mL without remote facilities. Commercial NG is never stored in quantities exceeding a few hundred grams outside a dedicated explosive manufacturing facility.

Headache from skin absorption is the first symptom of exposure. If a worker develops a headache near NG operations, it means NG vapor is present and skin contact has occurred. Remove the worker from the area, remove contaminated clothing, and wash skin with soap and water. The headache typically resolves within hours after exposure stops. In the historical dynamite industry, workers called it "NG head" and considered it a routine occupational hazard. Modern practice requires impermeable gloves, chemical splash suits, and continuous air monitoring.

Frozen NG (below 13°C) is even more sensitive than liquid. Crystal fractures from thermal stress can initiate detonation. Historically, NG was never allowed to freeze. Frozen NG was carefully thawed under warm (not hot) water, never near a flame or heat source. If NG is found frozen, do not attempt to break or chip it. Evacuate the area and consult explosive ordnance disposal procedures.

**Applications**: Primary ingredient in dynamite. Component of [double-base smokeless powder](../glossary/double-base.md). Rarely used as a standalone explosive due to extreme sensitivity, but in the early years (1847-1867, before Nobel invented dynamite) it was used directly for blasting with predictable and frequent catastrophic results. Sobrero, who first synthesized NG in 1847, was so horrified by its sensitivity that he recommended against any practical use. Nobel's genius was not inventing NG but finding a way to make it safe to handle.

**Strengths**:
- Extremely powerful (7,700 m/s detonation velocity, 6.4 MJ/kg)
- Key precursor for dynamite and double-base propellants
- Well-understood chemistry from 150+ years of industrial production
- The basis for Nobel's dynamite fortune, which funded the Nobel Prizes

**Weaknesses**:
- Extremely sensitive to impact, friction, and temperature change
- Liquid form nearly impossible to handle safely in bulk
- Freezes at 13°C, and frozen NG is more sensitive than liquid
- Headache from skin absorption limits worker exposure
- Requires dedicated remote manufacturing facility with blast shields and emergency dump
- No practical standalone use; must be absorbed into a carrier (dynamite) or combined with nitrocellulose (double-base powder)


## Dynamite

**Chemistry**: Alfred Nobel, 1867, discovered that absorbing nitroglycerin into diatomaceous earth (kieselguhr) produces a stable, handleable solid. The diatomaceous earth acts as an inert absorbent that desensitizes the NG while preserving its explosive power.

**Prerequisites**:
- [Nitroglycerin production](#nitroglycerin) capability (see Nitroglycerin section above)
- Diatomaceous earth (kieselguhr) or alternative absorbent (sawdust, wood meal)
- Cardboard tube cartridge production
- [Blasting caps](#blasting-caps--initiating-systems) for initiation

**Materials**:
- Nitroglycerin (75% by weight)
- Diatomaceous earth (25% by weight)
- Cardboard tubes (2-5 cm diameter × 10-30 cm long)
- Paraffin wax (for waterproofing cartridge exterior)

**Manufacture**:

1. **Absorb NG into kieselguhr**: Mix 75% nitroglycerin with 25% diatomaceous earth in a shallow pan. Knead until the mixture is uniform and all liquid is absorbed. The resulting paste should hold its shape and not weep liquid. Work behind a blast shield. Mix on a rubber mat (not concrete, which could cause friction initiation). All tools must be non-sparking (wood or brass).
2. **Load into cartridges**: Press the mixture into cardboard tubes (2-5 cm diameter × 10-30 cm long). Seal the ends with paraffin wax to waterproof. Standard cartridge sizes: 25 mm × 200 mm (150 g), 32 mm × 200 mm (250 g), 50 mm × 300 mm (600 g). The percentage designation (40%, 60%, 75%) refers to the NG content by weight. Higher percentage = more powerful but more sensitive.
3. **Quality check**: Weigh cartridges for consistency. Inspect for NG sweating (liquid on surface). Reject any cartridge showing exudation. Test a sample cartridge from each batch by dropping from 2 m onto a steel plate (should not detonate; this verifies adequate desensitization).
4. **Label and store**: Mark each cartridge with percentage and date of manufacture. Store in a cool magazine (below 30°C).

**Properties**: Detonation velocity 4,000-6,000 m/s (high explosive). Energy 4.0 MJ/kg. 5-10× black powder energy per unit mass. Produces mostly gas with minimal solid residue (clean break in rock). Stable to shock and friction. Can be dropped, thrown, and transported safely. Detonated with blasting cap (mercury fulminate or lead azide, initiated by safety fuse or electric current).

**Safety & Handling**:

> **Safety warning**: Nitroglycerin exudes from the absorbent over time ("sweating"), creating sensitive liquid pools on the cartridge surface. Inspect cartridges before use. If sweating is visible, handle as liquid NG (extremely dangerous). Frozen dynamite (below 13°C) is more sensitive than unfrozen. Store above 13°C but below 30°C. Headache from NG skin absorption is an early warning of exposure.

NG-based dynamites sweat in warm storage (above 30°C). Above 40°C, sweating accelerates and the surface NG creates a very dangerous situation. Magazine temperature control is essential. Never attempt to break or cut frozen dynamite. If dynamite has frozen, thaw it slowly in a warm room (20-25°C), never with direct heat. Do not handle thawing dynamite until it is fully pliable.

Inspect dynamite cartridges before each use. Look for oil stains on the packaging (signs of NG exudation), hard or brittle texture (frozen), or unusual odor. Reject any cartridge that shows signs of deterioration. Dispose of rejected dynamite by burning in small quantities on a hot plate (never in a fire, which can cause detonation). Burning dynamite produces toxic NO₂ fumes; perform disposal outdoors or under a fume hood.

**Applications**: Mining and construction blasting (replaced black powder for most uses), quarrying, tunneling, underwater blasting (gelatin dynamite variants with additional nitrocotton to waterproof). The workhorse explosive from the 1870s through the mid-20th century, now largely replaced by ANFO in mining but still used where higher energy density is needed. Dynamite cartridges fit into small-diameter boreholes (32-75 mm) where ANFO's critical diameter makes it impractical. Gelatin dynamite (NG + nitrocotton gel) resists water and is used in wet conditions.

Dynamite comes in several grades by NG content: 40% dynamite (lower power, less sensitive, good for soft rock), 60% dynamite (standard grade, good all-around blasting explosive), and 75%+ dynamite (high power for hard rock). The percentage refers to the nitroglycerin content by weight, with the remainder being the absorbent (kieselguhr) and additives. "Ammonia dynamites" replace some NG with ammonium nitrate to reduce cost and sensitivity. "Gelatin dynamites" add nitrocotton to the NG/absorbent mixture, forming a waterproof gel that does not exude NG. The choice of dynamite grade depends on the rock hardness, borehole diameter, and water conditions.

**Strengths**:
- 5-10× the energy of black powder per unit mass
- Stable to shock and friction (safe to transport and handle)
- Detonation velocity 4,000-6,000 m/s gives excellent shattering effect in rock
- Cardboard cartridges are easy to load into boreholes
- Available in multiple grades for different rock conditions

**Weaknesses**:
- Nitroglycerin exudes from absorbent over time, creating sensitive liquid pools
- Freezes at 13°C; frozen dynamite is more sensitive than liquid
- Headaches from NG skin absorption
- Requires mercury fulminate or lead azide blasting cap to initiate
- Being replaced by ANFO for most mining applications
- Shorter storage life than TNT or ANFO due to NG exudation


## Smokeless Powders

**Chemistry**: Smokeless powders are based on nitrocellulose, alone or combined with nitroglycerin. The gelatinized nitrocellulose burns progressively, with surface area controlling burn rate. Two main types:

- **[Single-base](../glossary/single-base.md)** (nitrocellulose only): Guncotton dissolved in ether-alcohol, then dried and extruded into cords or flakes. Burns progressively as surface area decreases.
- **[Double-base](../glossary/double-base.md)** (nitrocellulose + nitroglycerin): Nitroglycerin plasticizes nitrocellulose, increasing energy content. Burn rate controlled by grain geometry (perforations, flake thickness).

**Prerequisites**:
- [Nitrocellulose production](#nitrocellulose-guncotton) (guncotton)
- [Nitroglycerin production](#nitroglycerin) (for double-base only)
- Ether and alcohol solvents
- Extrusion press for shaping grains
- Solvent recovery system

**Materials**:
- Guncotton (nitrocellulose, 12.5-13.5% nitrogen)
- Nitroglycerin (for double-base only)
- Ether and ethyl alcohol (solvents)
- Stabilizers (diphenylamine)
- Plasticizers (for double-base)

**Manufacture (Single-base)**:

1. **Dissolve guncotton** in ether-alcohol mixture to form a gelatinous colloid (dough).
2. **Knead and mix** to ensure uniform consistency. Add stabilizer (diphenylamine, 1-2%) to scavenge decomposition products.
3. **Extrude** through dies to form cords, tubes, flakes, or perforated grains. Grain geometry determines burn rate: perforated grains burn from inside and outside simultaneously (progressive burning). Thin flakes burn fast (pistol powder). Thick cords burn slow (artillery powder). Seven-perforation grains provide progressive burning for large-caliber guns.
4. **Dry** at moderate temperature (40-60°C) for days to weeks, removing solvent slowly. Solvent recovery is important for economics.
5. **Coat** with graphite (glazing) to improve flow, reduce static sensitivity, and control moisture absorption.
6. **Sort by grain size** and test burn rate in a closed bomb (pressure vessel with piezo gauge). Each batch must meet ballistic specifications.

**Manufacture (Double-base)**:

1. **Mix nitrocellulose with nitroglycerin** plus solvent to form a uniform colloid. The NG plasticizes the NC, making a more energetic and more flexible propellant. The NG must be handled with extreme care during this step. Remote mixing behind blast shields is standard practice.
2. **Extrude** as for single-base, with grain geometry controlling burn rate. Double-base powders are typically extruded as longer cords or larger perforated grains because their higher energy allows smaller charges for the same ballistic performance.
3. **Dry and glaze** as for single-base. Double-base powders may require longer drying times due to the nitroglycerin content.

**Properties**: 2-3× energy density of black powder. No solid residue (no smoke to obscure vision). Cleaner burning (less barrel fouling). More consistent ballistics than black powder. Burn rate controlled by grain geometry (surface area), not just composition. Single-base: lower energy but cooler burning, extends barrel life. Double-base: higher energy but hotter combustion, more barrel erosion.

**Safety & Handling**:

> **Safety warning**: Smokeless powder burns violently if ignited in bulk, and can transition to detonation under heavy confinement. Store in small containers away from heat and ignition sources. Solvents (ether, alcohol) are highly flammable. Manufacture in well-ventilated areas with explosion-proof equipment.

Stabilizer (diphenylamine) content must be monitored. As the stabilizer is consumed by scavenging decomposition products, the powder approaches instability. Powder with depleted stabilizer must be destroyed. Test stabilizer content periodically with chemical analysis (colorimetric test or HPLC). Long-term storage requires cool, dry conditions. Typical shelf life with adequate stabilizer: 20-40 years at moderate temperatures. Heat accelerates stabilizer depletion: powder stored at 50°C loses stabilizer in months rather than decades.

**Applications**: Small arms ammunition (single-base), artillery and rifle ammunition (double-base), sporting ammunition, military propellants. Single-base powders dominate US military small arms (.30-06, 5.56 mm NATO). Double-base powders are standard for European military ammunition and most commercial hunting loads. Triple-base powders (nitrocellulose + nitroglycerin + nitroguanidine) are used in large-caliber artillery to reduce barrel erosion and flash.

**Strengths**:
- No solid residue (no smoke to obscure vision)
- 2-3× energy density (smaller cartridge for same power)
- Cleaner burning (less barrel fouling)
- More consistent ballistics than black powder

**Weaknesses**:
- Requires ether-alcohol solvents (flammable, requires recovery system)
- Stabilizer depletion limits storage life
- More complex manufacture than black powder
- Double-base requires nitroglycerin handling
- Solvent recovery is essential for economics (ether is expensive and highly flammable)
- Grain geometry must be precisely controlled for consistent ballistics


## Tier 3: Military & Industrial High Explosives

## TNT (Trinitrotoluene)

**Chemistry**: Toluene nitrated in three stages with mixed acid (HNO₃ + H₂SO₄), progressively increasing acid strength and temperature. Overall: C₇H₈ + 3HNO₃ → C₇H₅N₃O₆ + 3H₂O. Three stages:

1. **Toluene → mononitrotoluene (MNT)**: 30% HNO₃ / 55% H₂SO₄ / 15% H₂O at 30-50°C.
2. **MNT → dinitrotoluene (DNT)**: 45% HNO₃ / 50% H₂SO₄ at 60-80°C.
3. **DNT → trinitrotoluene (TNT)**: 60% HNO₃ / 35% H₂SO₄ at 100-110°C.

Each stage requires 1-2 hours of agitation in a cast iron or steel nitrator vessel with cooling jacket. Nitration is exothermic. Temperature must be controlled within ±5°C to prevent runaway. Overall yield ~90% based on toluene.

**Prerequisites**:
- [Toluene supply](petroleum-alternatives.md) (from petroleum or coal tar)
- [Mixed acid production](acids.md) at multiple concentrations
- Cast iron or steel nitrators with acid-resistant brick lining and cooling jackets
- Sodium sulfite for purification
- Crystallization equipment

**Materials**:
- Toluene (from [petrochemicals](petroleum-alternatives.md) or coal tar distillation)
- [Nitric acid](acids.md) at multiple concentrations (30%, 45%, 60%)
- [Sulfuric acid](acids.md) at multiple concentrations
- Sodium sulfite (5% solution for isomer removal)
- Water and ethanol for washing and crystallization

**Manufacture**:

1. **First nitration** (toluene → MNT): Add toluene to mixed acid (30% HNO₃, 55% H₂SO₄) at 30-50°C in a cast iron nitrator with acid-resistant brick lining. Agitate 1-2 hours. The nitrator must have a cooling jacket to remove heat from the exothermic reaction. Temperature control within ±5°C is essential. Separate the organic layer (MNT) from the spent acid. Wash the MNT with water.
2. **Second nitration** (MNT → DNT): Add MNT to stronger mixed acid (45% HNO₃, 50% H₂SO₄) at 60-80°C. Agitate 1-2 hours. The higher temperature drives the second nitration to completion. Separate organic layer. Wash with water.
3. **Third nitration** (DNT → TNT): Add DNT to the strongest mixed acid (60% HNO₃, 35% H₂SO₄) at 100-110°C. Agitate 1-2 hours. This is the most demanding stage: the combination of strong acid and high temperature requires careful temperature monitoring. A runaway at this stage can result in a violent decomposition. The nitrator must have an emergency dump valve that discharges into a drowning tank.
4. **Separate**: After each stage, the organic layer (nitrated product) is separated from the spent acid. The spent acid can be regenerated by vacuum distillation (recovering H₂SO₄ and HNO₃) and reused in earlier nitration stages.
5. **Purify**: Crude TNT contains unsymmetrical isomers (meta-nitrotoluene derivatives) that are oily and unstable. Wash with hot 5% sodium sulfite solution (sulfite selectively dissolves unsymmetrical isomers as colored sulfonates), followed by water wash. The sodium sulfite wash turns reddish-brown as it dissolves the impurities. Continue washing until the wash water runs clear. Crystallize the purified TNT from ethanol or water. The crystals are filtered, washed, and dried.
6. **Test purity**: Pure TNT melts at 80.8°C. Impurities lower the melting point. Verify by melting point test: place a few crystals in a capillary tube, heat slowly, and observe the melting point with a calibrated thermometer. Acceptable commercial TNT melts at 80.2-80.8°C. Material melting below 80.0°C needs additional purification.
7. **Melt-cast filling** (for munitions): Heat purified TNT to 85-90°C in a steam-jacketed melting kettle. Pour the clear yellow liquid into shell casings or bomb bodies. Insert a booster charge (tetryl or RDX pellet) while the TNT is still liquid. Cool slowly to allow proper crystallization and avoid internal voids. Rapid cooling creates shrinkage cavities that reduce performance and can trap air bubbles that are sensitive to shock.

**Properties**: Yellow crystalline solid. Melting point 80.8°C. Density 1.65 g/cm³. Can be safely melt-cast at 85-90°C into shells and shaped charges (one of TNT's great practical advantages). Detonation velocity 6,900 m/s at theoretical maximum density. Detonation pressure 21 GPa. Heat of explosion 4.6 MJ/kg. Oxygen balance: -74% (fuel-rich, produces CO and carbon soot). Burns without detonation if unconfined. Can be extinguished with water. Mechanically insensitive; requires a blasting cap or booster to initiate.

**Safety & Handling**:

> **Safety warning**: TNT yellow color stains skin and is toxic. Chronic exposure causes liver damage, aplastic anemia. Handle with gloves and protective clothing. Crude TNT contains unstable isomers requiring sulfite purification. Do not skip this step. Unpurified TNT can decompose spontaneously.

TNT is one of the safest high explosives to handle. It can be melted and poured (melt-cast at 85-90°C) without risk of detonation from heat alone. It burns without detonating if unconfined. This combination of properties made TNT the standard military explosive for over a century.

**Applications**: Military shells, bombs, demolition charges. Melt-cast filling: heat TNT to 85-90°C, pour into shell casing, insert booster charge, cool slowly. Industrial: mixed with ammonium nitrate as amatol (TNT shortage substitute, typically 50/50 or 80/20 AN/TNT). Composition B (60% RDX + 40% TNT) combines TNT's castability with RDX's higher power. TNT is also the reference standard for explosive power: the "TNT equivalent" of any explosive is expressed as the mass of TNT that would produce the same blast effect. Nuclear weapon yields are measured in kilotons and megatons of TNT equivalent.

**Strengths**:
- Mechanically insensitive, safe to handle, transport, and press into munitions
- Melt-cast at 85-90°C (low melting point simplifies shell filling)
- Burns without detonation if unconfined (can be extinguished with water)
- Well-characterized properties over 100+ years of use
- Can be mixed with RDX (Composition B) or ammonium nitrate (amatol)
- The universal reference standard for explosive power (TNT equivalent)

**Weaknesses**:
- Three-stage nitration requires progressively stronger acid and higher temperature, complex process control
- Crude TNT contains unstable isomers requiring sulfite purification
- Toluene feedstock depends on petroleum or coal tar
- Yellow color stains skin and is toxic (liver damage from chronic exposure)

**Quality control**: Each batch of TNT must pass the melting point test (mp 80.2-80.8°C for acceptable material). Lower melting point indicates residual isomers that must be removed by additional sulfite washing. Acidity test: dissolve a sample in warm water and titrate to verify no residual acid (acidic TNT is unstable). Moisture content is measured by drying a weighed sample and reweighing (must be below 0.1%). For military-grade TNT, additional tests include gap test (sensitivity to initiation through an air gap), sand test (brisance measurement by crushing standard sand), and ballistic mortar test (relative power compared to standard TNT).


## RDX (Cyclonite / Cyclotrimethylenetrinitramine)

**Chemistry**: Hexamine (hexamethylenetetramine) + nitric acid → RDX. Molecular formula C₃H₆N₆O₆. Also known as cyclonite, hexogen, T4. One of the most powerful conventional explosives, approximately 1.5× TNT by weight. Two main production routes:

- **Woolwich process**: Hexamine dinitrate + nitric acid at 30°C. Simpler but lower yield.
- **Bachmann process**: Hexamine + HNO₃ + NH₄NO₃ + acetic anhydride. Higher yield and more widely used industrially.

**Prerequisites**:
- Hexamine production (from [ammonia](ammonia.md) + formaldehyde)
- [Concentrated nitric acid](acids.md) (95-100%)
- Acetic anhydride (for Bachmann process, from acetic acid dehydration)
- Ammonium nitrate (for Bachmann process)
- Temperature-controlled jacketed reactor
- Vacuum filter and recrystallization equipment (acetone as solvent)

**Materials**:
- Hexamine (hexamethylenetetramine)
- [Nitric acid](acids.md) (concentrated, 95-100%)
- [Ammonium nitrate](#anfo-ammonium-nitrate--fuel-oil) (for Bachmann process)
- Acetic anhydride (for Bachmann process)
- Acetone (for recrystallization)
- Water and sodium carbonate (for washing)
- Paraffin wax (for phlegmatization)

**Manufacture (Woolwich process)**:

1. **Prepare hexamine dinitrate**: Dissolve hexamine (hexamethylenetetramine, produced from ammonia + formaldehyde) in nitric acid to form hexamine dinitrate. Hexamine is made by condensing formaldehyde with ammonia in a 3:2 molar ratio. The formaldehyde comes from methanol oxidation (itself from natural gas or syngas), and the ammonia from the Haber-Bosch process.
2. **Nitrate**: Add hexamine dinitrate to concentrated nitric acid (95-100%) at 30°C with continuous cooling and agitation. Maintain temperature below 35°C. The reaction is: hexamine dinitrate + HNO₃ → RDX + reaction byproducts. The Woolwich process produces RDX at roughly 60-70% yield, with significant byproduct formation.
3. **Precipitate**: RDX crystallizes from the reaction mixture as the temperature drops and the acid is diluted. The crude crystals contain occluded acid and unstable intermediates.
4. **Filter and wash**: Collect RDX crystals on a vacuum filter. Wash extensively with cold water to remove acid. Continue washing until the filtrate tests neutral.
5. **Recrystallize**: Dissolve in acetone (RDX is readily soluble in acetone) and recrystallize by adding cold water to the acetone solution. The recrystallized product is white crystalline powder with high purity. Acetone is recovered by distillation for reuse.

**Manufacture (Bachmann process)**:

1. **Combine reagents**: Add hexamine to a mixture of concentrated nitric acid, ammonium nitrate, and acetic anhydride. The acetic anhydride acts as a dehydrating agent, driving the reaction to completion. The ammonium nitrate provides additional nitro groups.
2. **Temperature control**: Maintain at 50-60°C during the reaction. The process is exothermic and requires continuous cooling with a jacketed reactor.
3. **Precipitate and filter**: RDX precipitates from the acetic acid mother liquor. Filter the crystals from the liquid.
4. **Wash**: Thoroughly with cold water, then with dilute sodium carbonate solution to neutralize residual acid. Any remaining acid causes instability.
5. **Recrystallize** from acetone for high purity. The recrystallized product is white crystalline powder. Yield is approximately 75-85% based on hexamine, significantly higher than the Woolwich process.
6. **Phlegmatize** (if needed for direct use): Coat RDX crystals with 5-10% paraffin wax in a tumbling mixer. The wax coating reduces sensitivity to impact and friction while preserving explosive power.

**Properties**: White crystalline solid. Melting point 204°C (decomposes). Density 1.82 g/cm³. Detonation velocity 8,750 m/s. Detonation pressure 34 GPa. Energy 5.6 MJ/kg. Approximately 1.5× the power of TNT by weight.

**Safety & Handling**:

> **Safety warning**: Pure RDX is too sensitive to impact and friction for safe use alone. Always phlegmatize (desensitize) by mixing with wax, or combine with TNT to form Composition B. Never handle pure RDX in bulk. Toxic if ingested or inhaled. Handle RDX-containing compositions with the same precautions as other high explosives.

RDX is toxic. Chronic exposure causes seizures, liver damage, and kidney damage. Workers in RDX production facilities must wear respirators, gloves, and protective clothing. Air monitoring for RDX dust is mandatory in production areas. The occupational exposure limit is very low (0.5 mg/m³ for 8-hour TWA in the US). Ingestion or inhalation of RDX dust causes central nervous system effects including seizures. If RDX is handled, wash hands before eating or drinking. Pure RDX crystals shatter easily under impact, creating hot spots that can initiate detonation. The phlegmatization process (coating with wax) reduces this sensitivity dramatically. Phlegmatized RDX can be handled, transported, and loaded into munitions with normal high-explosive precautions. C-4 demolition charge is safe enough to be handled, molded, and cut by hand, though it should never be ingested or burned (burning C-4 produces toxic fumes and can transition to detonation under confinement).
- **Composition B**: 60% RDX + 40% TNT. Castable (melts with the TNT component), widely used in military shells and bombs. Detonation velocity ~7,800 m/s. The TNT desensitizes the RDX while the RDX boosts the power above pure TNT.
- **C-4**: 91% RDX + 9% plasticizer (polyisobutylene + dioctyl adipate + processing oil). Malleable demolition charge that can be molded by hand. Detonation velocity ~8,040 m/s. Adheres to surfaces for shaped-charge and breaching applications.
- **Phlegmatized RDX**: RDX coated with 5-10% wax. Safer for storage and transport, used as a booster and base charge. The wax reduces sensitivity to impact and friction while preserving most of the explosive power.
- **Pentolite**: 50% PETN + 50% TNT. Not RDX-based, but serves a similar role as a castable booster. Detonation velocity 7,400-7,500 m/s. Used in cast boosters to initiate ANFO.

**Applications**: Military shells, bombs, shaped charge warheads (anti-tank), demolition charges (C-4), cast boosters for initiating insensitive explosives like ANFO. RDX-based compositions are the standard military high explosive in most nations. Shaped charge warheads for anti-tank missiles and rockets use Comp B or pure RDX liners to generate the high-velocity jet needed to penetrate armor. Demolition charges (C-4) are moldable, adhesive, and waterproof, making them ideal for combat engineering. Cast boosters (Comp B) bridge the sensitivity gap between blasting caps and ANFO.

**Strengths**:
- One of the most powerful conventional explosives (8,750 m/s, 5.6 MJ/kg)
- 1.5× TNT by weight
- Versatile in composite forms (Comp B, C-4, phlegmatized)
- Stable in storage when phlegmatized
- Essential for shaped charge warheads and military applications
- Higher detonation pressure than TNT makes it more effective in shaped charge jets

**Weaknesses**:
- Too sensitive to use alone; requires phlegmatization or combination with TNT
- Hexamine production requires ammonia and formaldehyde (additional supply chain)
- Bachmann process requires acetic anhydride (additional chemical production)
- Toxic if ingested or inhaled
- More complex manufacturing than TNT
- The supply chain (ammonia → formaldehyde → hexamine → RDX) requires significant industrial infrastructure

**Quality control**: RDX purity is verified by melting point (204°C with decomposition, so melting point is measured by capillary method with controlled heating rate). Acetone insolubles indicate contamination. Acidity test (pH of water extract must be neutral). Granulometry (particle size distribution) affects loading density and sensitivity. Military-grade RDX must meet minimum purity standards (typically >99% RDX by weight). The performance is verified by detonation velocity test and sensitivity tests (impact, friction).


## ANFO (Ammonium Nitrate / Fuel Oil)

The most widely used industrial explosive worldwide. Cheap, safe, and effective for mining and quarrying.

**Chemistry**: 94% ammonium nitrate (NH₄NO₃) + 6% fuel oil (diesel or No. 2 fuel oil). The AN provides oxygen (positive oxygen balance), the fuel oil provides carbon and hydrogen. Overall: 3NH₄NO₃ + CH₂ → 3N₂ + 7H₂O + CO₂ (simplified).

**Prerequisites**:
- [Ammonium nitrate production](ammonia.md) (from ammonia + nitric acid neutralization, then prilling)
- Prilled (porous spherical pellet) AN manufacturing capability (prilling tower)
- [Diesel fuel](petroleum-alternatives.md) or No. 2 fuel oil
- [Booster charge](#blasting-caps--initiating-systems) (dynamite, pentolite, or cast TNT/RDX booster, 100-500 g)
- Bulk mixing equipment (concrete mixer or purpose-built ANFO mixer)

**Materials**:
- Ammonium nitrate prills (porous spherical pellets, 2-4 mm diameter, bulk density 0.75-0.85 g/cm³)
- Diesel fuel or No. 2 fuel oil (6% by weight)
- Bulk mixing equipment (concrete mixer or purpose-built ANFO mixer)
- Polyethylene bags (25 kg) or pneumatic loading truck for borehole charging

**Manufacture**:

1. **Produce AN prills**: Melt ammonium nitrate (mp 169.6°C), spray through a prilling tower to form porous spherical pellets (2-4 mm). The prills fall through a countercurrent of cool air, solidifying into porous spheres. The porosity is critical: it allows fuel oil absorption and provides hot spots that help detonation initiation. Dense, non-porous prills (fertilizer grade) do not absorb enough oil and produce poor blasting performance.
2. **Mix on-site**: Combine AN prills with diesel fuel (6% by weight) in a concrete mixer or purpose-built ANFO mixer. AN prills absorb the oil into their porous structure. Mix thoroughly for 5-10 minutes until all prills are evenly coated. The oil should penetrate into the prill interior, not just coat the surface.
3. **Use within 24 hours**: Oil separates over time (drains to the bottom of the container). Alternatively, pre-package in polyethylene bags (25 kg) for immediate use, or bulk-load via pneumatic truck directly into boreholes for large-scale mining. Bulk loading is the standard in modern surface mining: an ANFO truck mixes and blows the explosive into the borehole in one operation.

**Properties**: Detonation velocity 2,500-4,000 m/s (density dependent). Density 0.8-0.85 g/cm³ (very low, limits energy density per unit volume). Very insensitive. Requires a booster charge (pentolite or cast TNT/RDX booster, 100-500 g) to initiate. Cannot be detonated by blasting cap alone. Safe to transport (classified as oxidizer, not explosive, until mixed with fuel). Energy: 3.7 MJ/kg. Gas volume: 980 L/kg (large heaving effect, good for moving soft rock and coal). Cost: 5-10× cheaper than dynamite per unit energy. Critical diameter: 50-100 mm (detonation dies in smaller holes). Poor water resistance. ANFO dissolves in wet boreholes.

**Heavy ANFO**: Blend of ANFO (55-80%) with emulsion matrix (20-45%). The emulsion fills voids between prills, increasing density to 1.0-1.3 g/cm³ and improving water resistance. Detonation velocity 3,500-5,000 m/s. Used in wet boreholes and where higher energy density is needed.

**Safety & Handling**:

> **Safety warning**: Pure ammonium nitrate can decompose explosively under confinement and intense heat. Texas City disaster (1947): 2,300 tonnes AN on ship caught fire and detonated, killing 581 people. Beirut explosion (2020): 2,750 tonnes AN stored unsafely, 218 dead. AN must be stored away from heat, fuels, and confined spaces. Contamination with organics or metals increases sensitivity. Never store AN in confined, hot locations.

AN prills absorb moisture and cake in storage, reducing sensitivity and performance. Store in dry, well-ventilated conditions. Bulk AN storage must be in buildings with fire walls and sprinkler systems. AN should never be stored with fuels, flammable liquids, or other combustible materials, as the combination can form a detonable mixture. ANFO classified as oxidizer until mixed with fuel, reducing transport restrictions, but this classification can lull workers into complacency. Treat bulk AN with the same respect as any explosive material.

Water-resistant versions (emulsions, water gels) use gelling agents and fuel phases to protect the AN. These are manufactured products, not field-mixed. Emulsion explosives consist of a water-in-oil emulsion: droplets of AN solution suspended in a continuous fuel phase. The fuel phase protects the AN from water ingress. Emulsion explosives have higher density (1.15-1.30 g/cm³) and higher detonation velocity (4,500-5,500 m/s) than ANFO. They are used in wet boreholes and where higher energy density is needed.

**Applications**: Large-scale mining and quarrying (the dominant industrial explosive worldwide), surface mining bench blasting (100-300 mm diameter boreholes, 50-500 kg/hole), foundation excavation for dams (1-100 tonnes total), coal stripping.

**Strengths**:
- Cheapest industrial explosive per unit energy (5-10× cheaper than dynamite)
- Extremely insensitive, classified as oxidizer, not explosive, until mixed with fuel
- Simple on-site mixing (AN prills + diesel in concrete mixer)
- No toxic fumes from complete detonation
- Ideal for large-scale mining and quarrying
- Bulk loading by pneumatic truck enables high daily throughput (50+ tonnes/day)
- Standard in surface mining worldwide (accounts for ~80% of all industrial explosive used)

**Weaknesses**:
- Very low density (0.8 g/cm³) limits energy per unit volume, requires large-diameter boreholes
- Critical diameter 50-100 mm (detonation dies in smaller holes)
- Poor water resistance, dissolves in wet boreholes
- Requires booster charge to initiate (blasting cap alone insufficient)
- AN prills absorb moisture and cake in storage

**Quality control**: ANFO performance depends on fuel oil content (6% ± 0.5%). Too much oil produces CO and reduces energy; too little produces NO₂ and reduces energy. Verify oil content by solvent extraction (dissolve the oil from a weighed sample with hexane, evaporate, and weigh the residue). Prill density and porosity affect oil absorption and detonation sensitivity. Measure prill bulk density (should be 0.75-0.85 g/cm³ for porous prills). Detonation velocity test: fire a charge with timing probes at known spacing and measure the shockwave transit time. ANFO that detonates below 2,500 m/s is underperforming and may indicate poor mixing, wet prills, or insufficient confinement.


## Supporting Sections

## Blasting Caps & Initiating Systems

High explosives (dynamite, TNT, ANFO) cannot be initiated by flame or spark alone. They require a strong shockwave from a primary explosive, delivered by a blasting cap. The cap contains a small charge of primary explosive that detonates from a fuse or electric current, producing a shockwave sufficient to initiate the main charge.

**Primary Explosives**:

**Mercury fulminate** (Hg(ONC)₂): The original primary explosive for blasting caps (Alfred Nobel, 1867). Prepared by dissolving mercury in excess nitric acid (forming Hg(NO₃)₂), then adding ethanol. The reaction produces a gray-white crystalline precipitate. Synthesis: mercury dissolved in nitric acid, then add ethanol. Precipitate filtered, washed, dried. Extremely friction and shock sensitive. Handle in tiny quantities (<1 g at a time). Detonation velocity: 4,500 m/s. Disadvantages: decomposes above 50°C in storage, mercury toxicity, poor compatibility with aluminum caps (mercury corrodes aluminum). Largely replaced by lead azide since the 1920s. Still encountered in military surplus ammunition.

**Lead azide** (Pb(N₃)₂): The standard primary explosive for modern blasting caps. Synthesized by reacting sodium azide (NaN₃) with lead nitrate (Pb(NO₃)₂) in aqueous solution: 2NaN₃ + Pb(NO₃)₂ → Pb(N₃)₂ + 2NaNO₃. Temperature controlled at 50-60°C, pH 5-6 (acetic acid buffer). Crystal form controlled by adding dextrin or polyvinyl alcohol (prevents formation of large, sensitive crystals). Large crystals of lead azide are extremely sensitive and can detonate from their own weight when dry. The dextrin or PVA additive produces small, rounded crystals that are safer to handle. Product: fine white to buff-colored crystals, density 4.8 g/cm³. Detonation velocity: 5,180 m/s at theoretical density. Extremely sensitive to impact (0.1-1 J) and friction. Handled wet (stored under water or water-alcohol mixture) until loaded into caps, then dried. Service temperature limit: 250°C. Not hygroscopic. More stable than mercury fulminate and higher initiating energy. Sometimes combined with lead styphnate as a "spotting charge" for more reliable ignition from flame. Standard blasting cap filling. Lead azide production requires sodium azide (from sodium amide + nitrous oxide, or from sodium nitrate + sodium amide) and lead nitrate (from lead metal + nitric acid). Both precursors are within the capabilities of a civilization that has mastered nitric acid production.

**Blasting Cap Evolution**:

1. **[Mercury fulminate caps](../glossary/mercury-fulminate-caps.md)** (1860s-1920s): Hg(ONC)₂ primary explosive pressed into copper or aluminum shell. Initiated by safety fuse. Unstable in hot climates (decomposes above 50°C). Mercury toxicity.
2. **[Lead azide caps](../glossary/lead-azide-caps.md)** (1920s-present): Pb(N₃)₂ primary explosive. More stable than mercury fulminate. Higher initiating energy. Slightly hygroscopic. Standard blasting cap filling.
3. **[Electric caps](../glossary/electric-caps.md)** (1900s-present): Bridge wire heated by electric current ignites primary charge. Precise timing with delay elements (pyrotechnic delay compositions providing 25 ms to 1000 ms delays) for sequential blasting. Enables controlled blasts with dozens of holes detonated in precise sequence.
4. **[Non-electric (shock tube)](../glossary/non-electric-shock-tube.md)** (1970s-present): Hollow plastic tube (3 mm OD) with thin coating of explosive dust (HMX + aluminum) on inner wall. Initiated by starter, propagates shock at ~2,000 m/s to detonator. Immune to radio frequency, static electricity, and stray currents. Safer than electric caps near power lines.

**Initiating Systems**:

**Safety fuse**: Black powder core (2-4 g/m) enclosed in textile wrapping with asphalt or plastic coating. Burn rate: 100-150 seconds per meter (±10% manufacturing tolerance). Cut to length for desired delay: 1 m fuse provides 100-150 seconds. Ignited with a fuse lighter (match-head type) or hot wire. Must be long enough for blaster to retreat to safe distance (minimum 1.2 m per second of burning time). Waterproof fuse required for wet boreholes. Test burn rate from each roll before use (variations between manufacturing lots are common and can be deadly if not accounted for). Cut the fuse squarely with a fuse cutter (not a knife, which can crush the powder core and cause a misfire). Insert the cut end fully into the blasting cap and crimp tightly with cap crimpers (a loose crimp allows moisture ingress and powder spillage). The fuse is lit at the exposed end; the black powder core burns at a steady rate from the lit end toward the cap.

**Detonating cord**: PETN (pentaerythritol tetranitrate) core (3-40 g/m) in textile/plastic sheath. Detonation velocity 6,000-7,000 m/s. Used to connect multiple boreholes in a surface pattern: one blast initiates the entire cord network simultaneously. Downlines: cord extends from surface to booster in the borehole, replacing a detonating cap in some designs. Detonating cord provides instantaneous initiation of all connected charges (at 7,000 m/s, a 100 m cord network detonates in 14 ms). This is both an advantage (simultaneous initiation for smooth-wall blasting) and a limitation (no delay capability without separate delay connectors). Cord is cut with a dedicated cutter (never with a knife on a hard surface, could initiate the PETN). Standard cord sizes: 3 g/m (light cord for trunklines), 10 g/m (standard), 25-40 g/m (heavy cord for initiating less sensitive explosives). The minimum initiating capability must detonate the booster charge used. Detonating cord produces a loud crack when fired (audible at several hundred meters) and a surface shock wave, which can be objectionable in populated areas. For this reason, shock tube systems have largely replaced surface detonating cord in urban blasting.

**Shock tube (Nonel)**: Hollow plastic tube (3 mm OD, 1.5 mm ID) with 0.5-1.0 mg/m of HMX/aluminum powder on inner wall. Initiated by a starter cap or mechanical clicker, the shock propagates at 2,000 ± 50 m/s through the tube (visible as a flash traveling through the translucent plastic). The shock tube output initiates a delay element and detonator at the borehole. Advantages over electric caps: immune to radio frequency, static electricity, and stray currents. Can be used near power lines and during thunderstorms. Tubing is cheap ($0.10-0.30/m) and cut to any length on site. Used with surface delay connectors (25, 50, 75, 100 ms delays) to create complex blasting patterns. The shock tube itself is not an explosive: the tiny quantity of powder per meter cannot detonate even in a confined space. It is classified as a flammable solid, not an explosive, which simplifies transport and storage. The shock tube system combines the safety advantages of non-electric initiation with the timing precision of delay caps. It has become the dominant initiating system for surface mining and construction blasting worldwide.

**Cast boosters**: Pentolite (50% PETN + 50% TNT) or Composition B (60% RDX + 40% TNT) cast into cylindrical charges (25-500 g). Detonation velocity 7,000-7,800 m/s. Required to initiate ANFO and other insensitive explosives. Placed at bottom of borehole, detonator inserted into molded cap well. The booster's high detonation pressure (15-25 GPa) shocks ANFO into stable detonation. Without a booster, ANFO may detonate incompletely, leaving toxic fumes and unexploded material.

**Electric blasting procedure**: Connect blasting caps in series circuit to blasting machine (magneto generator). Check circuit continuity with galvanometer BEFORE connecting to machine. Keep blasting machine locked until ready to fire. Verify circuit resistance matches expected value (open circuit = broken wire, short circuit = damaged cap, both require investigation).

**Blasting cap construction**: A typical modern cap is an aluminum or copper shell (6-8 mm diameter, 40-70 mm long) loaded in layers. The base charge (RDX or PETN, 0.5-1.0 g) provides the output detonation. Above it, a primary charge (lead azide, 0.1-0.3 g) bridges the gap between flame or electrical input and the base charge. The top contains either a fuse well (for safety fuse) or an electric match (bridge wire + pyrotechnic composition). Delay caps add a delay element (slow-burning pyrotechnic composition) between the electric match and the primary charge. The delay element burns for a precise time (25, 50, 75, 100, 150, 200, 250, 300, 400, 500 ms are common delays) before igniting the primary charge. This allows a single blasting machine to fire dozens of holes in precise sequence.

Loading blasting caps is the most dangerous operation in the explosive manufacturing chain. Primary explosives are handled in tiny quantities (grams) behind blast shields. Wet loading (slurry of primary explosive in water) reduces the risk of accidental initiation during the pressing operation. After loading, the caps are dried at moderate temperature (40-50°C). Each cap is tested for electrical continuity (electric caps) or physical integrity (fuse caps) before packaging. Production facilities for blasting caps must be isolated from other explosive manufacturing, with blast walls between workstations and earthen barricades around the building. No more than a few grams of primary explosive are allowed at any workstation at one time.

**Misfire procedure**: Wait minimum 30 minutes (black powder fuse) or 1 hour (electric caps) before approaching misfire. Do NOT pull the detonator from the charge. Carefully remove tamping from one side, insert new detonator, re-tamp, and fire. If unmovable, mark and evacuate area. Treat every misfire as live until proven otherwise.

**Explosive train design**: Every blast requires a chain of increasingly sensitive explosives, each initiated by the one before it. The typical train for an ANFO blast: electric current → bridge wire (hot wire in blasting cap) → primary charge (lead azide, 0.1-0.3 g) → base charge in cap (RDX or PETN, 0.5-1.0 g) → booster (Comp B or pentolite, 100-500 g) → main charge (ANFO, 50-500 kg). Each link in the chain amplifies the detonation energy. The blasting cap alone cannot initiate ANFO. The booster is the critical link: it generates enough detonation pressure (15-25 GPa) to shock the insensitive ANFO into stable detonation. Skipping the booster is the most common cause of ANFO misfires. For dynamite blasts, the booster is unnecessary: the blasting cap output directly initiates the dynamite cartridge. For TNT-filled munitions, a tetryl or RDX booster pellet bridges the gap between the cap and the main TNT charge. The explosive train must be designed with no weak links: every interface must have enough energy transfer to reliably initiate the next element.


## Demolition Explosives

**Shaped charges (hollow charges)**: A cone or hemisphere of high explosive (Composition B or RDX/wax) with a metal liner (copper, steel, or molybdenum, 1-3 mm thick) on the cavity side. Upon detonation, the liner collapses and forms a high-velocity jet of metal plasma (tip velocity 7,000-10,000 m/s, tail 2,000-4,000 m/s) that penetrates armor steel to a depth of 4-8× the charge diameter. The stand-off distance (distance from charge base to target) is critical: optimum stand-off is 2-6× charge diameter. Used in military anti-tank warheads, oil well perforating guns (penetrate steel casing and rock formation), and industrial metal cutting. The jet formation is governed by the Birkhoff-McDougall theory: the liner material is accelerated to different velocities along its length, stretching into a thin, fast-moving jet followed by a slower-moving slug.

**Cutter charges**: Linear shaped charges with a V-shaped liner, producing a planar cutting jet. Used for demolition of steel structures (bridges, offshore platforms, buildings). Cutting thickness: up to 100 mm steel plate with a single charge. Detonation velocity of the explosive filling: >7,000 m/s for effective jet formation. The cutting jet severs structural steel members in milliseconds, enabling controlled collapse of the structure. Linear cutter charges are specified by their cutting capacity (e.g., "cuts 25 mm steel" or "cuts 50 mm steel") and come in lengths of 0.5-3 m with detasheet or cast explosive filling.

**Explosive welding**: Two metal plates are joined by placing a layer of explosive on one plate and detonating it. The explosive force drives the plates together at high velocity (200-500 m/s) at a slight angle. The collision creates a jet of surface material that sweeps away oxides and contaminants, producing a metallurgical bond between the plates. Used to clad stainless steel or titanium onto carbon steel substrates (corrosion-resistant linings for chemical vessels). The explosive must produce a controlled, flat detonation wave (detasheet or sheet explosive). ANFO and dynamite are too powerful and irregular for this application.

**Explosive hardening**: High explosives can work-harden austenitic manganese steel (Hadfield steel, used in crusher jaws and railroad frogs). A layer of explosive (usually sheet explosive) is placed directly on the surface and detonated. The shock wave plastically deforms the surface layer, increasing hardness from ~200 HB to ~400 HB. This is a specialized application, but useful for extending the life of rock-crushing equipment in mining operations. The same principle applies to explosive compaction of powder metallurgy preforms.


## Detonation Physics

**Detonation velocity**: Speed of the supersonic shockwave through the explosive. Higher velocity = more brisant (shattering) effect. Key comparison:

| Explosive | Det. Velocity (m/s) | Density (g/cm³) | Energy (MJ/kg) |
|-----------|---------------------|-----------------|----------------|
| Black powder | 400 | 1.0-1.2 | 2.6 |
| ANFO | 2,500-4,000 | 0.8-1.0 | 3.7 |
| Dynamite (60%) | 4,500-5,500 | 1.3-1.5 | 4.0 |
| TNT | 6,900 | 1.6 | 4.6 |
| Nitroglycerin | 7,700 | 1.6 | 6.4 |
| RDX | 8,750 | 1.8 | 5.6 |

**Chapman-Jouguet (C-J) theory**: The detonation wave is a self-sustaining shockwave coupled to a chemical reaction zone. The C-J condition states that detonation products exit the reaction zone at the local speed of sound relative to the shock front. The C-J detonation velocity can be estimated: VOD = √(2Q(γ²-1)/(γ+1)) where Q is the heat of explosion per unit mass and γ is the ratio of specific heats of the detonation products. For TNT: Q = 4.6 MJ/kg, γ ≈ 1.24 for the product mixture (N₂, H₂O, CO, CO₂, C), giving VOD ≈ 6,800 m/s, close to the measured 6,900 m/s.

**Detonation pressure**: P_CJ = ρ₀ × VOD² / (γ + 1), where ρ₀ is the initial explosive density. For TNT at 1.60 g/cm³: P = 1600 × 6900² / (2.24) = 34 GPa. This extreme pressure (340,000 atm) is what gives detonation its shattering (brisant) effect. Higher density explosives with higher VOD produce higher detonation pressures: RDX at 1.80 g/cm³ produces P_CJ ≈ 39 GPa.

**Brisance vs heaving force**: Brisance is the shattering effect (ability to pulverize rock), related to detonation velocity and pressure. Heaving force is the gas expansion effect (ability to move/throw material), related to total gas volume produced. For hard rock: high brisance (TNT, RDX). For soft rock/coal: high heaving force (ANFO, black powder). Dynamite is a good compromise. Brisance matters when you need to fracture hard, dense material. Heaving force matters when you need to move large volumes of already-broken or soft material. The Sandos brisance test (sand crushing) and the Trauzl lead block test (cavity expansion) are standard comparative measures.

**Critical diameter**: Minimum diameter of explosive charge that sustains stable detonation. Below this diameter, the shockwave loses energy to the charge surface faster than the chemical reaction generates it, and detonation fails. ANFO: 50-100 mm (large boreholes). Dynamite: 10-25 mm. TNT: 5-10 mm. PETN: 1-3 mm. Lead azide: <1 mm (used in blasting caps). Critical diameter depends on density, confinement, and temperature. Higher density and stronger confinement reduce critical diameter. In practical terms, the critical diameter determines the minimum borehole size for each explosive. ANFO cannot be used in small-diameter holes (below 50 mm) because the detonation will die out.

**Sensitiveness and sensitivity**: These are distinct concepts. *Sensitiveness* is the susceptibility of an explosive to initiation by a small stimulus (impact, friction, spark). *Sensitivity* is the ability of an initiated explosive to propagate detonation reliably. Primary explosives (lead azide, mercury fulminate) have high sensitiveness. They initiate easily, which is why they are used in blasting caps. Secondary explosives (TNT, RDX) have low sensitiveness but high sensitivity once initiated. Tertiary explosives (ANFO) have both low sensitiveness and require a strong booster to initiate. This hierarchy is the basis of explosive train design: primary → secondary → tertiary (or main charge).

**Oxygen balance**: The oxygen balance of an explosive determines the composition of its detonation products. An explosive with perfect oxygen balance (e.g., ANFO) has just enough oxygen to fully oxidize all carbon to CO₂ and all hydrogen to H₂O. Fuel-rich explosives (TNT, oxygen balance -74%) produce CO and carbon soot along with CO₂. Oxygen-rich explosives produce excess O₂ and NO₂. Oxygen balance affects both energy release and toxic fume production. ANFO has a near-zero oxygen balance when mixed at the correct ratio (94% AN, 6% fuel oil), which is why it produces relatively clean detonation products. Deviations from the correct fuel ratio shift the oxygen balance and increase toxic fume production.

**Explosive testing and characterization**: Several standard tests characterize explosive performance:

- **Detonation velocity test**: probes (ionization pins or fiber optic sensors) placed at known spacing in a confined charge. A high-speed recorder measures the shockwave transit time. Velocity = distance / time. This is the most fundamental performance measurement.
- **Trauzl lead block test**: 10 g of explosive detonated in a cavity in a standard lead cylinder (200 mm diameter × 200 mm high). The volume expansion of the cavity after detonation measures relative power (heaving force). TNT produces about 290 mL of expansion (used as the 100% reference).
- **Sand test (brisance)**: 0.4 g of explosive detonated in contact with 200 g of standard Ottawa sand (20-30 mesh). The weight of sand passing through a 30-mesh sieve after detonation measures brisance (shattering effect). Lead azide crushes about 22 g of sand; TNT about 48 g; RDX about 60 g.
- **Impact sensitivity test**: a standard weight (2 kg) dropped from increasing heights onto a small sample (40 mg) of explosive between two steel surfaces. The height at which 50% of drops cause detonation is the impact sensitivity. Lead azide: 5-10 cm. Nitroglycerin: 10-15 cm. RDX: 30-40 cm. TNT: 100+ cm (very insensitive). ANFO: no detonation at maximum drop height (extremely insensitive).
- **Gap test**: measures the minimum distance through which the shockwave from a donor charge will initiate an acceptor charge through an air or water gap. Higher gap sensitivity means the explosive is easier to initiate. ANFO has very low gap sensitivity (requires direct contact with booster). TNT has moderate gap sensitivity. Detonating cord has high gap sensitivity (can initiate through several cm of air).


## Blasting Design Parameters

**Powder factor**: Mass of explosive per unit volume of rock broken (kg/m³) or per tonne of rock (kg/t). Typical values: hard granite quarrying 0.4-0.7 kg/m³ ANFO, limestone 0.2-0.4 kg/m³, coal stripping 0.1-0.3 kg/m³. Higher powder factor produces finer fragmentation but increases cost and vibration. Optimizing powder factor balances explosive cost against downstream processing (crusher throughput, loader productivity).

**Borehole spacing**: Burden (distance from borehole to nearest free face): 25-35× borehole diameter. Spacing (distance between adjacent holes in a row): 1.0-1.5× burden. Subdrilling (depth below intended floor level): 0.3× burden. Stemming (inert material packed above the charge): 0.7-1.0× burden length. Example: 100 mm diameter holes, burden 3.0 m, spacing 3.5 m, depth 12 m (10 m bench + 1 m subdrilling), stemming 2.5 m. Charge weight per hole: ~50 kg ANFO. Fragmentation size: P80 (80% passing) = 200-500 mm, depending on blasting pattern and rock properties.

The burden must be correctly calculated for each blasting situation. Too much burden and the explosive energy is absorbed by the rock without creating a free face, resulting in poor fragmentation and excessive ground vibration. Too little burden and the blast vents through the free face (blow-out), throwing flyrock and wasting explosive energy. Stemming length and material are critical for confinement: crushed stone (8-15 mm) is the best stemming material because it interlocks under pressure. Drill cuttings are less effective but commonly used for convenience. Water in the borehole reduces stemming effectiveness.

**Detonation timing**: Electronic delay detonators provide millisecond-precision timing between boreholes. Typical delays: 25 ms between holes in a row, 50-100 ms between rows. Sequential timing creates free faces for each successive row to break toward. The timing must be long enough for rock movement between rows (>8 ms per meter of burden) but short enough to maintain vibration control (cap the maximum instantaneous charge per delay period for regulatory vibration limits). Modern electronic detonators can be programmed individually with delays from 0 to 20,000 ms in 1 ms increments, allowing complex blasting patterns with hundreds of holes. Pyrotechnic delay caps (non-electric) offer fixed delays in standard increments (25, 50, 100, 150, 200, 250, 300, 400, 500 ms) at lower cost.

**Worked example**: A limestone quarry bench blast with the following parameters: bench height 12 m, borehole diameter 100 mm, burden 3.0 m, spacing 3.5 m, subdrilling 1.0 m, stemming 2.5 m, 3 rows × 5 holes per row = 15 holes total. ANFO at density 0.85 g/cm³. Charge length per hole = 12 m - 2.5 m stemming + 1.0 m subdrilling = 10.5 m. Charge volume per hole = π × (0.05)² × 10.5 = 0.0825 m³. Charge mass per hole = 0.0825 × 850 = 70 kg ANFO. Total charge = 15 × 70 = 1,050 kg. Rock volume broken = 3 rows × 5 holes × 3.0 m burden × 3.5 m spacing × 12 m height = 1,890 m³. Powder factor = 1,050 / 1,890 = 0.56 kg/m³ (within the 0.2-0.4 kg/m³ range for limestone, perhaps slightly high, indicating good fragmentation). Timing: 25 ms between holes in a row, 75 ms between rows. Maximum charge per delay = 70 kg (one hole per delay). Total blast duration = (5-1) × 25 + (3-1) × 75 = 100 + 150 = 250 ms.


## Blasting Vibration and Air Overpressure

**Ground vibration**: Detonation generates seismic waves that propagate through rock and soil. Peak particle velocity (PPV) is the standard measurement (mm/s). Damage thresholds: residential plaster cracks at PPV >5 mm/s, cosmetic cracking at >12.5 mm/s, structural damage at >50 mm/s. Vibration attenuation with distance: PPV = K × (D/√W)^-n, where D = distance, W = maximum charge per delay, K and n are site constants (K ≈ 500-2000, n ≈ 1.5-2.0 for typical rock). At 200 m distance, 50 kg per delay produces PPV of 2-8 mm/s (below damage threshold for most structures but perceptible and potentially objectionable).

Controlling vibration is critical for blasting near populated areas. The most effective method is reducing the maximum charge per delay period: if a 200 kg charge at 100 m produces unacceptable vibration, splitting it into four 50 kg charges with 25 ms delays between them reduces the instantaneous charge by 4× and the vibration by approximately 4^n (where n ≈ 1.5-2.0), giving roughly 8-16× reduction. Electronic detonators make this approach practical. Other vibration control methods include using lower-energy explosives (ANFO instead of dynamite for the same weight, since ANFO has lower detonation velocity), increasing burden (more rock mass absorbs energy), and using presplitting (creating a fracture plane between the blast area and adjacent structures that reflects seismic energy).

**Air overpressure (airblast)**: The shock wave transmitted through air from the blast. Measured in decibels (dB) or pressure (kPa). Typical values at 200 m: 110-130 dB for confined blasts, 130-150 dB for unconfined. Threshold for glass breakage: ~150 dB. Complaint threshold: 115-120 dB (audible as a low-frequency thump). Airblast is controlled by: (1) adequate stemming (prevents gas venting through borehole collar), (2) covering the blast with blasting mats (worn conveyor belts or steel mesh), (3) avoiding surface detonating cord (use shock tube instead).

**Flyrock control**: Rock fragments thrown beyond the expected blast area are the most dangerous blasting hazard. Flyrock range: 50-500 m for large blasts if uncontrolled. Control measures: (1) adequate burden and stemming (prevents gas from lifting rock vertically), (2) accurate drilling (burden errors cause flyrock), (3) delayed initiation pattern (allows rock to move into void created by earlier-delayed holes), (4) blasting mats for blasts near occupied areas (worn conveyor belts chained together or steel mesh mats), (5) exclusion zone (typically 300-500 m radius for personnel during blasting). The blaster in charge is responsible for calculating the expected flyrock range and setting the exclusion zone. A flyrock incident that injures someone outside the exclusion zone is a catastrophic safety failure. Within the exclusion zone, all personnel must be in blast shelters (reinforced earth berms or concrete bunkers) or at a safe distance during firing.


## Selection Guide

| Explosive | Det. Velocity (m/s) | Density (g/cm³) | Energy (MJ/kg) | Sensitivity | Best Use |
|-----------|---------------------|-----------------|----------------|-------------|----------|
| Black powder | 400 | 1.0-1.2 | 2.6 | High (spark, friction) | Early mining, firearms propellant |
| Nitrocellulose | 6,400 (bulk) | 1.0-1.3 | 3.7 | Moderate | Propellant base, guncotton |
| Nitroglycerin | 7,700 | 1.6 | 6.4 | Extreme | Dynamite precursor, not standalone |
| Dynamite (60%) | 4,500-5,500 | 1.3-1.5 | 4.0 | Moderate | Construction, small-diameter blasting |
| Single-base powder | 6,400 | 1.0 | 3.7 | Moderate | Small arms propellant |
| Double-base powder | 7,200 | 1.2 | 4.6 | Moderate | Artillery, rifle propellant |
| TNT | 6,900 | 1.6 | 4.6 | Low | Military shells, melt-cast filling |
| RDX (Comp B) | 7,800 | 1.7 | 5.1 | Low (phlegmatized) | Military warheads, shaped charges |
| ANFO | 2,500-4,000 | 0.8-1.0 | 3.7 | Very low | Large-scale mining, cheapest per joule |


## Applications by Sector

| Sector | Primary Explosive | Typical Charge | Notes |
|--------|-------------------|----------------|-------|
| Mining (quarrying) | ANFO | 50-500 kg/hole | Large-diameter boreholes (100-300 mm), bench blasting |
| Mining (underground) | ANFO or dynamite | 5-50 kg/hole | Smaller holes (50-100 mm), controlled fragmentation |
| Construction (tunneling) | Dynamite + ANFO | 20-200 kg/round | Sequential delay blasting for smooth walls |
| Construction (dams) | ANFO | 1-100 tonnes total | Mass blasts for foundation excavation |
| Military | TNT, RDX compositions | Variable | Shell filling, demolition charges, shaped charges |
| Demolition (building) | RDX compositions, dynamite | 1-50 kg total | Cutter charges for steel, linear charges for concrete |
| Seismic exploration | ANFO or dynamite | 1-50 kg/shot | Shallow boreholes, geophone arrays |
| Avalanche control | ANFO or dynamite | 1-5 kg per charge | Triggering controlled avalanches from safe positions |

## Explosive Selection for Common Tasks

Choosing the right explosive for a task requires matching the explosive's properties to the rock type, borehole size, water conditions, and regulatory requirements.

**Hard rock quarrying (granite, basalt)**: ANFO in large-diameter holes (150-300 mm) with cast boosters. The high burden requires high heaving force to move the broken rock away from the face. Powder factor 0.4-0.7 kg/m³. If the rock is very hard and abrasive, consider a denser explosive (Heavy ANFO or emulsion) to increase energy per unit volume in the borehole.

**Underground metal mining**: Dynamite or packaged emulsion in small-diameter holes (50-75 mm). ANFO can be used in dry conditions with a suitable booster. Underground mines require fume class 1 explosives, which excludes standard ANFO. Permitted explosives (special formulations with improved oxygen balance) are mandatory in gassy coal mines. Powder factor 0.3-0.6 kg/m³.

**Tunneling**: Combination of dynamite (for the cut, the initial opening that creates a free face) and ANFO (for the bulk of the perimeter holes). Smooth-wall blasting uses lightly loaded perimeter holes (decoupled charges: smaller-diameter cartridges in larger holes) with delay detonators to create a smooth tunnel wall with minimal overbreak. Typical advance per round: 3-5 m in hard rock, 5-8 m in soft rock.

**Demolition**: C-4 or other RDX-based plastic explosive for steel cutting (shaped charges) and concrete breaking (placed charges). Linear cutter charges for severing structural steel beams. Small-diameter dynamite cartridges for concrete column and wall demolition. The explosive is placed directly on or in the target structure, not in drilled boreholes. Quantity calculations are based on the cross-sectional area of the member being cut or demolished, typically 0.5-2.0 kg/m³ of material to be removed.

**Soil and soft rock excavation**: ANFO or black powder (in a bootstrapping context) in shallow, closely-spaced holes. Soft materials require high heaving force rather than high brisance. Powder factor is low (0.1-0.3 kg/m³) because the material breaks easily. The main purpose of the explosive is to lift and displace the material, not to shatter it.


## Integration Points

| Phase | Contribution |
|-------|-------------|
| Early Mining & Quarrying | Black powder for ore extraction, road building, and quarrying. Enables large-scale mining with hand drills. Safety fuse for controlled initiation. Mining productivity increases 10-50× over manual methods. |
| Chemistry & Acids | Nitration chemistry produces nitrocellulose, nitroglycerin, and TNT. Requires concentrated nitric and sulfuric acids from the Ostwald and contact processes. The entire nitration industry depends on reliable acid production at industrial scale. |
| Construction & Infrastructure | Dynamite and ANFO for tunneling, dam foundation excavation, canal building, and road construction through rock. Explosives enable earthmoving at scales impossible by hand. The Panama Canal, the Hoosac Tunnel, and Mount Rushmore are all products of industrial blasting. |
| Military & Defense | TNT, RDX, and smokeless powders for artillery, small arms, and demolition. Shaped charges for anti-armor warfare. Smokeless powders extend effective rifle range from 300 m to 1000+ m by eliminating smoke obscuration. TNT standardizes shell filling across all calibers. |
| Industrial Mining (Modern) | ANFO dominates surface mining worldwide. Cheap, safe, and effective in large boreholes. Heavy ANFO for wet conditions. Electronic delay detonators enable precise blasting near populated areas with minimal vibration. Bulk ANFO trucks mix and load 50 tonnes per day into boreholes. |
| Petroleum & Chemical | Ammonium nitrate (ANFO precursor) from ammonia + nitric acid. Toluene (TNT precursor) from petroleum refining or coal tar. Hexamine (RDX precursor) from ammonia + formaldehyde. The explosive industry is a major consumer of chemical industry outputs. |


## Key Deliverables

- **Tier 1** (Years 5-10): Black powder for mining, quarrying, and firearms propellant. Requires only saltpeter, charcoal, and sulfur. Sufficient for basic ore extraction and road construction through rock. Black powder blasting increases mining productivity by 10-50× over manual methods. A civilization with black powder can build roads through mountains, quarry building stone, and mine metallic ores at commercially useful rates.
- **Tier 2** (Years 10-20): Nitroglycerin, dynamite, and nitrocellulose for construction blasting and military applications. Requires mixed acid production (nitric + sulfuric) and glycerol. Dynamite transforms mining productivity again: higher energy density allows smaller boreholes, less drilling, and better fragmentation. Smokeless powders modernize firearms, giving military advantage and enabling modern small arms. Nitrocellulose also provides lacquers, film base, and dope for early aircraft. Safety fuse and blasting caps (mercury fulminate, then lead azide) are developed in parallel.
- **Tier 3** (Years 20-30+): TNT, RDX, smokeless powders, and ANFO for industrial and military use. TNT requires three-stage nitration and toluene (from petroleum or coal tar). RDX requires hexamine and acetic anhydride. ANFO requires ammonium nitrate prills and diesel fuel. These represent the mature industrial explosive palette. TNT becomes the reference standard for all explosive power comparisons. RDX enables shaped charge warheads and modern military munitions. ANFO becomes the cheapest and most widely used industrial explosive, dominating surface mining worldwide. Electronic delay detonators provide millisecond-precision timing for controlled blasting near populated areas.


## General Safety & Hazards

- **Explosion**: Black powder deflagrates rapidly. Nitroglycerin, dynamite, and guncotton detonate (supersonic shockwave). Respect the destructive potential of every explosive. Treat all materials as if they could initiate accidentally.
- **Acid burns**: Mixed acid (HNO₃ + H₂SO₄) for nitration causes severe chemical burns. Nitric acid stains skin yellow and causes deep tissue damage. Sulfuric acid dehydrates and chars organic tissue. Wear acid-resistant gloves (nitrile or neoprene, not latex), face shield, and rubber apron. Have copious water supply for immediate flushing (minimum 15 minutes continuous flushing for eye exposure). Neutralize spills with limestone or sodium bicarbonate. Emergency eyewash stations within 10 seconds of all nitration work areas.
- **Nitroglycerin exposure**: NG is absorbed through skin and inhaled as vapor. Headache is the first symptom. Chronic exposure causes tolerance (workers lose the headache response) but does not reduce the cardiovascular risk. Workers who have developed tolerance and then stop exposure experience "withdrawal" chest pain. Maintain strict exposure limits through engineering controls (ventilation, enclosed processes) and PPE (impermeable gloves and suits).
- **Static electricity**: Can initiate black powder and some primary explosives. Ground all metal equipment. Wear cotton clothing (not synthetic). Maintain humidity above 50% in work areas. Use conductive flooring in explosive handling areas. Test ground connections regularly.
- **Toxic fumes**: Explosion gases contain CO, NO₂, and other toxic products. Ventilate blast areas thoroughly before re-entry. NO₂ is invisible but causes pulmonary edema: coughing, chest tightness, and shortness of breath hours after exposure. Seek medical attention immediately. The delayed onset of symptoms makes NO₂ particularly dangerous: a worker may feel fine immediately after exposure and collapse hours later. ANFO produces ~15 L of NO₂ per kg detonated. Incomplete detonation leaves toxic residues (nitroglycerin, TNT, nitrocellulose) in blasted rock, contaminating groundwater.
- **Fume class limitations**: Underground mining permits only "permitted" explosives (fume class 1, producing <5 L toxic gas per kg). Many blasting agents (ANFO in particular) are fume class 3 and restricted to surface use unless heavily modified.
- **Non-sparking tools**: Bronze or beryllium copper tools (wrenches, hammers, scrapers) for all work with explosives and in magazines. Steel-on-steel impacts generate sparks capable of initiating sensitive primary explosives and black powder. Aluminum-bronze alloy (95% Cu, 5% Al) provides hardness without spark generation. Inspect non-sparking tools regularly for embedded steel particles that could cause sparking.
- **Storage magazine requirements**: Dry, cool, well-ventilated, earth-bermed building away from other structures. Separate storage for detonators and main charges (minimum 15 m between magazines). Inventory log for every item in, out, and on hand. Lock and key controlled. No smoking within 50 m of magazine. Floors should be spark-proof (wood or conductive rubber). Lighting should be explosion-proof. Magazines should be located away from inhabited buildings, public roads, and other magazines by distances specified in quantity-distance tables.
- **Magazine temperature control**: Store explosives below 30°C. Above 40°C, nitroglycerin-based dynamites sweat (NG exudes from absorbent), creating highly sensitive liquid pools. Above 50°C, mercury fulminate blasting caps decompose. Ventilated, earth-bermed magazine buildings with passive cooling (shade, insulation). Temperature monitoring with maximum-minimum thermometers, logged daily. In hot climates, magazine buildings may need active cooling or underground construction.
- **Quantity-distance tables**: Minimum safe distances between explosive storage and inhabited buildings, public roads, and other magazines. Based on blast overpressure scaling: safe distance ∝ (charge weight)^(1/3). For 1 tonne TNT equivalent: 180 m to inhabited buildings (for 5 kPa overpressure, the threshold for building damage). Underground magazines reduce surface distances by 50-70%. Regulatory tables (ATF 27 CFR Part 555, or equivalent national standards) specify distances by explosive type and quantity. These distances are not negotiable. A magazine that is too close to inhabited buildings puts the entire community at risk.
- **Transport**: Explosives are transported in dedicated vehicles with placards, fire extinguishers, and non-sparking interiors. Detonators and main charges are transported in separate compartments. The vehicle must never be left unattended. Routes avoid congested areas, tunnels, and bridges where possible. In a bootstrapping civilization, even basic transport precautions (separate containers for detonators and charges, careful driving, no smoking, no passengers) significantly reduce risk.
- **First aid**: For acid burns, flush immediately with copious water for at least 15 minutes. Remove contaminated clothing while flushing. Do not apply neutralizing agents directly to the burn (the heat of neutralization worsens tissue damage). For NO₂ inhalation, move the victim to fresh air immediately. Administer oxygen if available. Seek medical attention even if symptoms are mild, because pulmonary edema can develop hours later. For NG exposure (headache), remove from exposure area, remove contaminated clothing, wash skin, and rest. The headache usually resolves within hours. For explosive injuries, treat blast injuries (ruptured eardrums, lung damage) as priority. Do not move a blast victim with suspected spinal injuries. Apply tourniquets for traumatic amputations. Evacuate to medical facility.
- **Fire in a magazine**: If a fire breaks out in an explosives storage area, evacuate immediately to at least the quantity-distance and do not attempt to fight the fire. The transition from fire to detonation can occur without warning, especially if NG-based explosives are involved. The only safe response to a magazine fire is evacuation. Notify emergency services and establish a perimeter at the quantity-distance radius. Do not re-enter the area until the fire has been extinguished and the area has been declared safe by explosive ordnance disposal personnel.
- **Training and competency**: All personnel handling explosives must be trained and, in regulated environments, licensed. Training covers: explosive properties and hazards, safe handling and storage procedures, blasting cap and initiating system operation, misfire procedures, and emergency response. Untrained personnel must never handle explosives. In a bootstrapping civilization, this training must be developed from scratch, ideally by the people who developed the explosive manufacturing process. Institutional knowledge about safe practices is as important as the technical knowledge of how to manufacture the explosives. A single serious accident can destroy the confidence needed to operate an explosives program.


## Limitations

- **Storage stability**: Nitroglycerin-based explosives (dynamite) exude liquid NG over time, especially in warm storage. Exuded NG is extremely sensitive to shock. Ammonium nitrate absorbs moisture and cakes, reducing sensitivity and performance. Proper storage (cool, dry, ventilated magazines) is essential but not always available in field conditions. Black powder absorbs moisture and degrades, though it can be dried and reprocessed. TNT and RDX compositions are the most storage-stable, with decades of shelf life under proper conditions.
- **Regulatory complexity**: Explosives manufacturing, transport, storage, and use are heavily regulated (ATF, DOT, OSHA in the US, equivalent agencies globally). Licensing, background checks, magazine inspection, inventory tracking, and chain-of-custody documentation add administrative overhead that can exceed the technical challenges. In a bootstrapping civilization, these regulations do not yet exist, but the safety problems they address are real. Informal safety protocols, training standards, and magazine construction practices serve the same purpose.
- **Toxic detonation products**: NOₓ gases from commercial explosives are toxic and require ventilation in underground mines. Incomplete detonation leaves toxic residues in blasted rock, contaminating groundwater. ANFO is particularly problematic underground due to its fume class. Even surface blasting in confined areas (trenches, foundations near buildings) requires attention to wind direction and personnel exposure.
- **Fume class limitations**: Underground mining permits only "permitted" explosives (fume class 1, producing <5 L toxic gas per kg). Many blasting agents (ANFO in particular) are fume class 3 and restricted to surface use unless heavily modified with aluminum powder or other fuel adjustments that improve oxygen balance and reduce toxic fume production.
- **Water sensitivity**: ANFO dissolves in water and cannot be used in wet boreholes without emulsion wrapping or conversion to Heavy ANFO. Dynamite cartridges (standard grade) also degrade in prolonged water exposure. Only emulsion explosives and water gels are truly waterproof, and these require more complex manufacturing. For a bootstrapping civilization, dry boreholes or simple waterproofing (plastic bag wrapping of charges) may be the practical solution.
- **Supply chain depth**: Modern explosives like RDX require hexamine (ammonia + formaldehyde), acetic anhydride, and concentrated nitric acid. Each of these has its own supply chain. The full depth from raw materials to RDX touches ammonia synthesis (Haber-Bosch), methanol production, formaldehyde oxidation, acetic acid fermentation or synthesis, and nitric acid production (Ostwald process). This supply chain depth means RDX and other advanced explosives arrive late in the bootstrapping sequence, long after black powder and dynamite have served the civilization's explosive needs.
- **Environmental impact**: Large-scale blasting produces noise, vibration, dust, and nitrate contamination. Ammonium nitrate residue from ANFO blasting leaches into groundwater, contributing to nitrate pollution. In sensitive watersheds, blast site runoff must be contained and treated. Noise from quarry blasting travels several kilometers and is a common source of community complaints. Dust from blasting is controlled by water spraying and blast blankets, but cannot be eliminated entirely. Underground blasting in sulfide-bearing ore bodies can generate sulfuric acid when sulfide minerals are exposed to air and water in the fractured rock (acid mine drainage), a long-term environmental liability that persists long after the mine closes.


## See Also

- **[Black Powder](../mining/black-powder.md)**: Detailed gunpowder production
- **[Mining Extraction](../mining/extraction.md)**: Blasting in underground and surface mines
- **[Wood Gasification](wood-gasification.md)**: Charcoal production for black powder
- **[Petrochemicals](petroleum-alternatives.md)**: Hydrocarbon feedstocks for modern explosives
- **[Nitric Acid](acids.md)**: Ostwald process producing nitric acid for nitration
- **[Ammonia Production](ammonia.md)**: Haber-Bosch process for ammonia, the precursor to ammonium nitrate and hexamine



[← Back to Chemistry](index.md)
