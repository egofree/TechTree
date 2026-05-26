# Weapons & Edged Tools

> **Node ID**: defense.weapons
> **Domain**: Defense & Military Engineering
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)
> **Timeline**: Years 0-30+
> **Outputs**: weapons, blades, spears, bows, small_arms, muskets

---

## Overview

Weapons and edged tools encompass the development of offensive and defensive instruments from stone-age knapping through black-powder firearms. This capability tracks the material science, engineering, and production techniques required to manufacture weapons at each technological tier — from flint hand-axes to rifled muskets.

Weapon development is a direct proxy for metallurgical capability. The progression from stone to bronze to iron to steel to firearms maps exactly onto the bootstrap chain's material science development. A community that can produce consistent 0.5% carbon steel and heat-treat it to HRC 50 has the industrial base for edged weapons, agricultural tools, and machine components alike. Firearms add the requirement for precision bore-drilling, consistent black powder manufacture, and lead casting — capabilities that also serve mining, construction, and chemical industries.

Weapon production scales from individual craftsmanship (a single smith making swords) to industrial arsenals (thousands of muskets per month with interchangeable parts). The resource demands are significant: a 1000-soldier force equipped with muskets consumes 30-120 kg of black powder and 60-70 kg of lead per minute of combat, requiring industrial-scale [chemistry](../chemistry/index.md) and [mining](../mining/index.md).

---

## Bill of Materials

| Weapon Type | Primary Material | Quantity per Unit | Secondary Materials | Source |
|-------------|-----------------|-------------------|---------------------|--------|
| Flint spear | Flint/chert | 150-300 g stone point | Ash shaft 1.5-2.5 m, birch tar 20 g, rawhide binding | [Foundations](../foundations/index.md) |
| Bronze sword | Cu-Sn alloy (90/10) | 800-1200 g bronze | Wood/bone grip plates, copper rivets | [Non-Ferrous Metals](../metals/index.md) |
| Iron spear | Wrought iron | 200-500 g head | Ash shaft 1.5-2.5 m, rivets | [Iron & Steel](../metals/iron-steel.md) |
| Steel sword | Medium-C steel (0.5-0.7%) | 2-5 kg steel bar stock | Leather grip, wood pommel, oil for quenching | [Iron & Steel](../metals/iron-steel.md) |
| Self bow | Yew/elm/osage orange | 1.5-1.8 m stave | Linen string 3-5 mm, 3 goose feathers per arrow, flint/bone points | [Foundations](../foundations/index.md) |
| Crossbow (steel prod) | Spring steel | 400-1200 lb prod | Iron/steel bolt 60-100 g, spanning mechanism | [Iron & Steel](../metals/iron-steel.md) |
| Matchlock musket | Wrought iron/low-C steel | 3-5 kg barrel stock | Saltpeter 15-25 g/shot, lead ball 25-35 g/shot, hemp match cord | [Explosives](../chemistry/explosives.md) |
| Arrows (war, per 12) | Iron/steel | 240-600 g total points | Ash shafts 60-80 cm, goose feathers 36, birch tar | [Textiles](../textiles/index.md) |

---

## Weapon Development by Era

### Stone-Age Weapons (Years 0-5)

**Chipped stone blades**: Flint, chert, and obsidian knapped to cutting edges. Hardness: flint Mohs 7, obsidian Mohs 5-5.5 (but produces edges under 1 um -- sharper than surgical steel scalpel at 3-5 um). Flint knapping techniques: hard hammer (bipolar percussion for initial reduction), soft hammer (antler or wood billet for thinner flakes), pressure flaking (antler tine for final edge shaping and serration). Edge durability: 10-30 minutes of active cutting before resharpening needed on hide/wood; breaks on bone contact.

**Spear points**: Hafted stone points attached to wooden shafts (1.5-2.5 m ash or hazel) using birch tar adhesive and rawhide binding. Thrusting spear: 2.0-2.5 m, 300-600 g head. Throwing spear/javelin: 1.5-2.0 m, 150-300 g head. Atlatl (spear thrower): 50-70 cm lever, multiplies throwing force 3-5x, effective range 20-30 m vs 10-15 m for hand-thrown.

**Club and mace**: Hardwood club (1.0-1.5 m, 0.8-1.5 kg). Stone-headed mace: rounded or flanged stone (0.5-1.5 kg) set in wooden handle with rawhide wrapping. Effective against unarmored opponents; glancing blow from stone mace fractures skull at 40-60 J impact energy.

**Bow and arrow**: Self bow from yew, elm, or osage orange (1.5-1.8 m, 25-50 lb draw weight at 28 inch draw). Arrow: 60-80 cm shaft, flint or bone point, fletched with 3 flight feathers (goose or turkey). Effective range: 20-30 m for accurate hunting shot, 50-80 m maximum. Arrow velocity: 45-55 m/s. Kinetic energy at impact: 25-40 J. Arrow penetration: 5-10 cm in soft tissue, stopped by 2-3 mm rawhide armor.

### Bronze-Age Weapons (Years 5-10)

**Bronze alloy for weapons**: Copper-tin alloy, 8-12% tin for weapons (harder than pure copper). Tin content tradeoff: higher tin = harder but more brittle. Optimal weapon bronze: 10% tin -> HB 120-150 (Brinell hardness), tensile strength 350-450 MPa. Cast in two-piece stone or clay molds.

**Bronze sword**: Leaf-shaped blade (Naue Type II), 60-80 cm blade length, 4-5 cm width at widest, 3-4 mm edge thickness tapering to <1 mm at cutting edge. Weight: 800-1200 g. Blade cast as single piece with integral hilt (riveted to wooden or bone grip plates). Edge sharpened by hammer-hardening and stone grinding. Superior to stone in durability: holds edge through 2-4 hours of combat before field resharpening.

**Bronze spear**: Socketed spearhead, 20-40 cm blade length, cast with integral socket for shaft attachment (riveted through shaft). Weight: 200-500 g head. Superior attachment vs hafted stone -- socket prevents head separation on impact.

**Bronze axe**: Socketed axe head, 10-20 cm cutting edge, 200-500 g. Edge angle: 25-35 degrees (compromise between sharpness and durability). Used as both tool and weapon.

### Iron-Age Weapons (Years 5-15)

**Wrought iron weapons**: Bloomery iron (0.02-0.08% carbon) hammered into bars and forged to shape. Hardness: HB 90-120 (softer than bronze weapons but more available material). Advantage: iron ore far more abundant than copper and tin. Wrought iron bends rather than shatters -- field-repairable by any smith.

**Carburized steel blades**: Iron bar packed in charcoal and heated to 900-950 degrees C for 1-4 hours -> surface absorbs carbon to 0.3-0.8%, forming steel layer. Forge-welded steel edge to wrought iron back (pattern welding: alternating steel and iron rods forge-welded, twisted, and re-forged produces composite blade with hard edge and flexible back).

**Heat treatment of steel blades**: Critical parameters depend on carbon content:
- **0.3-0.5% carbon**: Heat to cherry red (~780-830 degrees C), quench in water or brine. Temper at 250-350 degrees C for 30-60 minutes. Result: HRC 40-50 (sword blade -- tough, resists breaking).
- **0.6-0.8% carbon**: Heat to 750-800 degrees C, quench in warm oil (less thermal shock than water). Temper at 200-280 degrees C. Result: HRC 55-62 (knife edge, axe bit -- hard, holds edge).
- **Over-hardening danger**: Quenching without tempering produces brittle martensite -- blade shatters on first impact. Must temper.

**Iron-age sword**: Straight double-edged blade, 70-90 cm length, 4-5 cm width, 3-5 mm spine thickness tapering to edge. Weight: 1000-1500 g (steel blades lighter than bronze for equivalent length due to higher strength). Fullered blade (groove reduces weight 15-20% without significant strength loss). Center of percussion located 1/3 from tip -- impact at this point delivers maximum energy with minimum shock to wielder's hand.

**Polearms**: Spear (1.5-3.0 m shaft, iron or steel head). Halberd (1.5-2.0 m shaft, axe blade + spike + hook, 2-3 kg head). Pike (3.5-6.0 m shaft, small steel point, defensive formation weapon -- stop cavalry charge at 3-5 m range).

### Steel Weapons (Years 10-25)

**Crucible steel (Wootz method)**: Iron + carbon (1.0-2.0%) + trace elements (vanadium, chromium from specific ores) sealed in clay crucible, heated to 1300-1400 degrees C for 4-6 hours. Slow cooling produces cementite dendrites in pearlite matrix -> characteristic damascene pattern when etched. Hardness: HRC 55-65. Superior to pattern-welded blades -- more uniform carbon distribution.

**Medieval steel sword (high medieval)**: 0.5-0.7% carbon steel blade, differential heat treatment (edge quenched harder than spine). Blade: 80-95 cm, 1200-1600 g. Cutting performance: clean cut through 5-8 cm of softwood or 2-3 cm of green bone in single stroke. Thrusting: penetrates 15-25 cm of soft tissue, stopped by mail over padding at 4-6 cm penetration.

**Steel arrowheads**: Bodkin point (armor-piercing, 4-sided pyramidal cross-section, no cutting edges -> concentrates force on small area). At 60 lb draw, bodkin arrow (50 g, 55 m/s) delivers ~75 J kinetic energy. Penetrates mail at 20 m, but NOT plate armor -- defeated by 2+ mm tempered steel plate at oblique angle.

### Black Powder Firearms (Years 15-30)

**Matchlock musket**: Smoothbore barrel, 17.5-19 mm bore diameter (.69-.75 caliber), 90-120 cm barrel length. Barrel material: wrought iron or low-carbon steel, 3-5 mm wall thickness at chamber. Lock mechanism: smoldering slow match (saltpeter-impregnated hemp cord, ~10 cm/hr burn rate) lowered into flash pan by trigger lever. Propellant: black powder charge 15-25 g (see [Explosives](../chemistry/explosives.md) for propellant composition: 75% KNO3, 15% charcoal, 10% sulfur). Projectile: lead ball, 25-35 g (fitting loosely in bore -- windage 1-2 mm). Muzzle velocity: 350-450 m/s. Effective range: 50-80 m aimed, 150-200 m volley fire. Rate of fire: 1-2 rounds per minute. Misfire rate: 20-30% in damp conditions (slow match ignites powder in flash pan, which ignites main charge through touch hole).

**Flintlock mechanism** (improvement): Flint stone held in cock (hammer) strikes steel frizzen, producing sparks that ignite powder in flash pan. Eliminates smoldering match (fire hazard, reveals position at night). Misfire rate reduced to 10-15%. Rate of fire: 2-3 rounds per minute with trained infantryman. Standard infantry weapon 1650-1840.

**Percussion cap** (further improvement): Copper cap containing mercury fulminate (impact-sensitive primary explosive) placed on hollow nipple connecting to barrel chamber. Hammer strikes cap -> detonation -> flame through nipple ignites main charge. All-weather reliability: misfire rate <5%. Adopted militarily 1820s-1840s. Requires industrial chemistry for cap production (see [Explosives](../chemistry/explosives.md) for primary explosives).

**Rifled musket**: Spiral grooves cut into bore interior (3-7 grooves, 1 turn in 100-120 cm) impart spin to elongated bullet. Spin stabilizes projectile in flight -> dramatic accuracy improvement. Effective range: 300-500 m aimed (vs 50-80 m smoothbore). Muzzle velocity: 400-500 m/s with Minie ball (hollow-base bullet that expands into rifling on firing). Ammunition: .58 caliber (14.7 mm) Minie ball, 30-35 g, powder charge 50-60 g.

**Bayonet**: Blade (30-45 cm) attached to musket muzzle, converting firearm into short pike. Socket bayonet fits over barrel, allows simultaneous loading and bayonet fixing. Combined weapon length: 1.5-1.8 m. Bayonet charge effective at <30 m. Wound channel: 1-2 cm wide, 15-30 cm deep -- high lethality due to infection risk in pre-antibiotic era.

---

## Specialized Weapon Systems

### Crossbow

**Construction**: Prod (bow limb) from composite (horn + sinew + wood) or steel. Steel prod: 50-100 cm span, 400-1200 lb draw weight (requires spanning lever, cranequin, or windlass for cocking). Bolt: 30-50 cm, 60-100 g, iron or steel bodkin point. Muzzle velocity: 50-70 m/s. Kinetic energy: 100-200 J. Effective range: 40-60 m armor-piercing, 100-150 m unarmored target. Rate of fire: 1-2 bolts per minute (spanning mechanism adds significant reload time). Advantage over hand bow: requires less training for proficiency, higher armor penetration at close range.

### Polearms & Formation Weapons

**Spear (infantry)**: Universal weapon from stone-age through modern bayonet. Iron-age infantry spear: 1.5-2.5 m ash shaft (25-35 mm diameter), 20-40 cm iron spearhead with socket. Weight: 1.0-2.0 kg. Used in formation (shield wall, phalanx) -- mass of spear points creates impenetrable hedge. Individual spear combat: thrust and recover, don't overextend. Spear wins vs sword at range (first strike advantage), loses if swordsman closes past spear point.

**Halberd**: Combined axe + spike + hook on 1.5-2.0 m shaft. Head weight: 2-3 kg. Axe blade for chopping, spike for thrusting, hook (beak) for pulling mounted opponents from horse. Versatile polearm -- used by guards and elite infantry. Requires more training than spear but provides more tactical options. Effective against both infantry and cavalry.

**Pike**: Long spear (3.5-6.0 m ash shaft, small steel point). Weight: 2.5-5.0 kg. Defensive formation weapon -- pike square presents hedge of 100+ points to cavalry. Pikes planted at 45 degree angle (braced butt on ground, points at horse chest height) stop cavalry charge. Pike and shot tactics (1500-1700): pike block protects musketeers while they reload, musketeers provide firepower. Requires disciplined formation -- individual pike ineffective.

### Bow Types & Archery Mechanics

**Self bow**: Single piece of wood (yew, elm, osage orange, ash). Yew is optimal: heartwood (compression strength) on belly, sapwood (tensile strength) on back. Draw weight: 50-80 lb for war bow (Mary Rose longbows: 100-180 lb). Arrow velocity: 55-65 m/s. String: linen or hemp, 3-5 mm diameter, served (wrapped) at nocking point and loops. Bow stringer: essential for safe stringing -- prevents limb breakage and injury. Bow life: 6-12 months of regular use before replacement (compression set -- bow loses draw weight).

**Composite bow**: Horn (belly, compression), wood (core), sinew (back, tension) laminated with animal hide glue. Horn stores 3x more energy in compression than wood alone. Curing time: 6-12 months for full glue set. Draw weight: 80-160 lb. Superior to self bow in energy storage per unit mass -- shorter limbs (80-120 cm) produce equivalent performance to 180 cm self bow. Ideal for cavalry (short limbs don't catch on horse). Vulnerable to moisture -- hide glue softens in rain (must keep in waterproof case).

**Arrow mechanics**: Arrow spine (stiffness) must match bow draw weight -- underspined arrow flexes excessively and flies erratically, overspined arrow doesn't flex properly around bow shelf. Arrow weight: 30-60 g for war arrow. Fletching: 3 feathers (goose preferred), 5-10 cm length, slight helical twist for spin stabilization. Point types: broadhead (cutting, for unarmored targets), bodkin (armor-piercing), barbed (hunting, difficult to extract). Arrow production: 12-24 arrows per fletcher per day.

### Blade Geometry & Mechanics

**Cutting mechanics**: A blade cuts by concentrating force on a narrow edge. Edge performance depends on edge angle, steel hardness, and blade geometry. Edge angle (included angle): 20-30 degrees for cutting/slicing weapons (swords, knives), 40-60 degrees for chopping weapons (axes). Thinner edge = sharper but more fragile. Harder steel holds thin edge longer but chips more easily. Optimal for sword: edge angle 25-30 degrees, HRC 45-50, with fuller (groove) reducing blade weight 15-20%.

**Blade cross-sections**:
- **Lenticular** (convex both sides): Strong, durable, good cutting. Common in Viking and early medieval swords.
- **Diamond** (rhombic): Rigid, good for thrusting. Common in later medieval swords designed to defeat mail armor.
- **Hexagonal** (flat sides with central ridge): Compromise -- strong, reasonably light, good for both cutting and thrusting.
- **Hollow-ground** (concave sides): Very sharp, less durable. Used for razors and specialized cutting tools, not combat blades.

**Center of percussion**: The point on a blade (~1/3 from tip) where impact produces minimum shock to the wielder's hand. Determined by blade mass distribution and pivot point (grip). A well-designed sword aligns the center of percussion with the primary striking zone -- this is the "sweet spot" that maximizes energy transfer while minimizing discomfort.

### Sling & Thrown Weapons

**Sling**: Two cords (50-80 cm) attached to a pouch holding a stone or lead bullet (20-80 g). Spun overhead and one cord released. Sling bullet velocity: 60-80 m/s. Kinetic energy: 40-250 J (lead glandes bullets from Balearic slingers were reportedly lethal through simple helmets). Range: 100-200 m (exceeds bow range). Ammunition: any rounded stone or cast lead bullet. Advantage: virtually free ammunition, very lightweight, easy to learn basics (mastery takes years). Used by skirmishers to harass enemy formations from beyond bow range.

**Lead sling bullets (glandes)**: Cast in stone or clay molds, almond-shaped, 30-80 g. Sometimes inscribed with messages ("Take this," "Ouch"). Higher density than stone (11.3 g/cm3 vs 2.5 g/cm3) -> smaller projectile, same mass, less air resistance, flatter trajectory. Cast lead bullet production: 100-200 per hour with simple mold.

**Javelin**: Light throwing spear (1.5-2.0 m, 300-600 g total). Throwing range: 20-35 m. Enhanced by thong (ankyle): 30-50 cm leather strap wound around shaft -> imparts spin and additional lever arm, increasing range 20-30% and accuracy. Roman pilum: heavy javelin (1.5-2.0 kg, 1.5-2.0 m) with long iron shank (60-90 cm) and pyramidal point. Designed to penetrate shield and bend on impact (enemy cannot throw it back). Effective range: 15-25 m.

---

## Quantitative Parameters

### Weapon Performance Comparison

| Weapon | Blade/Projectile | Energy at Target (J) | Effective Range (m) | Rate of Fire |
|--------|-----------------|----------------------|---------------------|--------------|
| Flint spear | 200 g stone point | 40-80 (thrown) | 15-30 | N/A |
| Bow (50 lb) | 50 g flint arrow | 25-40 | 20-30 | 6-12/min |
| Bronze sword | 1000 g blade | 60-120 (swing) | 1-2 (melee) | N/A |
| Steel sword | 1200 g blade | 80-200 (swing) | 1-2 (melee) | N/A |
| Crossbow (800 lb) | 80 g bolt | 100-150 | 40-60 | 2-4/min |
| Matchlock musket | 30 g lead ball | 2000-3000 | 50-80 | 1-2/min |
| Flintlock musket | 30 g lead ball | 2000-3000 | 50-80 | 2-3/min |
| Rifled musket | 33 g Minie ball | 2600-4000 | 300-500 | 2-3/min |

### Material Hardness Reference

| Material/Alloy | Hardness Scale | Value | Application |
|---------------|----------------|-------|-------------|
| Obsidian | Mohs | 5-5.5 | Stone-age blades (sharpest edge) |
| Flint | Mohs | 7.0 | Stone-age blades, arrowheads |
| Pure copper | HB | 40-50 | Too soft for weapons |
| Bronze (10% Sn) | HB | 120-150 | Swords, spearheads, axes |
| Wrought iron | HB | 90-120 | Basic iron weapons |
| Medium-C steel (quenched) | HRC | 40-50 | Sword blades |
| High-C steel (quenched + tempered) | HRC | 55-62 | Knife edges, axe bits |
| Crucible steel (Wootz) | HRC | 55-65 | Premium blades |

### Firearm Ammunition Specifications

| Parameter | Matchlock Musket | Flintlock Musket | Rifled Musket |
|-----------|-----------------|-----------------|---------------|
| Bore diameter | 17.5-19 mm | 17.5-19 mm | 14.7 mm (.58 cal) |
| Projectile weight | 25-35 g | 25-35 g | 30-35 g |
| Powder charge | 15-25 g | 15-25 g | 50-60 g |
| Muzzle velocity | 350-450 m/s | 350-450 m/s | 400-500 m/s |
| Effective range (aimed) | 50-80 m | 50-80 m | 300-500 m |
| Misfire rate | 20-30% | 10-15% | <5% (percussion) |

---

## Weapon Maintenance

**Blade care**: Steel blades rust within hours in humid conditions. Field maintenance: wipe with oiled cloth (linseed or animal fat oil) after every use. Rust removal: fine sand or emery cloth, then oil. Edge maintenance: leather strop for fine sharpening, whetstone (coarse then fine grit) for resharpening damaged edges. A well-maintained sword blade lasts decades; neglected blade rusts to uselessness in months.

**Firearm maintenance**: Black powder residue is hygroscopic and corrosive. After firing, barrel must be cleaned with hot water (dissolves salt residue), dried, and oiled within 24 hours or rust begins. Cleaning kit: worm (corkscrew puller for stuck balls), brush, cleaning jag (fits patch), oil bottle. Touch hole (vent) must be kept clear -- blocked vent prevents ignition. Lock mechanism: disassemble and clean weekly in active service.

---

## Scaling Notes

- **Individual production (1-5 weapons/month)**: A single smith with forge, anvil, and hand tools produces 2-4 swords or 8-12 spearheads per month. Arrow production separate (fletcher craft). Sufficient for a village militia of 10-30 fighters.
- **Workshop production (20-50 weapons/month)**: Smithy with 2-4 workers, water-powered trip hammer for forging. Produces standardized spearheads, axe heads, and arrowheads. Can equip a warband of 100-200 fighters over 3-6 months.
- **Arsenal production (500+ weapons/month)**: Requires division of labor (barrel-makers, lock-filers, stock-makers, assemblers), water-powered boring mills, and consistent steel supply. A state arsenal with 50-100 workers produces 1000+ muskets per month. Prerequisites: [machine tools](../machine-tools/index.md) for barrel boring, [industrial chemistry](../chemistry/index.md) for powder, [mining](../mining/index.md) for lead and saltpeter.
- **Arrow production scaling**: 100 archers expend 2000-6000 arrows per battle. Fletchers must produce 100-300 arrows/day to sustain an archery corps. Requires organized supply of shafts, points, feathers, and glue.
- **Training time bottleneck**: Bow proficiency requires 2-5 years of muscle development. Musket drill: 4-8 weeks. When raising forces quickly, firearms are decisive despite higher material cost. Pike drill: 2-4 weeks for formation competence.

---

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Steel blade bends on impact | Low carbon content (<0.3%), insufficient quench | Recarburize edge in charcoal pack; use higher-carbon steel; ensure full quench to cherry red |
| Steel blade shatters | Over-hardened (quench without temper), or too high carbon (>0.8%) | Temper after quenching at 250-350 degrees C for 30-60 minutes; use medium-carbon steel |
| Edge dulls rapidly | Steel too soft (HRC <35), or edge angle too thin | Harden and temper to HRC 45-50; increase edge angle to 25-30 degrees |
| Musket misfire (repeated) | Damp powder, blocked touch hole, or spent slow match | Keep powder in wax-sealed containers; clear vent with pick; ensure match is lit and glowing |
| Inconsistent musket accuracy | Barrel bore irregular, loose ball fit (excessive windage) | Use tighter-fitting patched ball; inspect bore for erosion; replace barrel after 500-1000 shots |
| Bow string breaks | Worn or frayed string, dry shooting (no arrow) | Inspect string before each use; replace every 50-100 shots; never dry-fire a bow |
| Arrow flight erratic | Underspined arrow (too flexible for draw weight) | Match arrow spine to bow draw weight; use stiffer shafts for heavier draw |
| Crossbow prod cracks | Over-drawing, metal fatigue, or cold temperature embrittlement | Do not exceed rated draw length; store in moderate temperature; inspect prod before use |
| Bronze casting porosity | Insufficient mold venting, pour temperature too low | Add vent channels to mold; heat melt to 1100-1200 degrees C before pouring |
| Spearhead separates from shaft | Hafting failure (binding or adhesive) | Use socket construction when possible; ensure birch tar is fresh; rawhide binding must be wet-stretched then dried tight |

---

## Safety Considerations

- **Black powder handling**: Gunpowder is an explosive. Store in cool, dry location away from sparks and open flame. Maximum 25 kg in any single storage container. Transport in wax-sealed leather or ceramic containers. A single spark in a powder magazine destroys the building and kills everyone inside. No metal tools that can spark near powder -- use wooden mauls and copper implements.
- **Lead toxicity**: Chronic lead handling causes colic, neuropathy, and death. Melt lead outdoors or in well-ventilated area. Wash hands after casting bullets. Do not eat or drink while handling lead. Lead fumes are the primary hazard -- molten lead at 327 degrees C produces invisible toxic vapor.
- **Blade testing injuries**: Weapons must be tested for quality, but testing carries risk. Never test edge sharpness by drawing blade across skin. Test on wood or rawhide targets. Wear eye protection when testing blade hardness (chipping steel fragments can blind).
- **Bow dry-fire danger**: Firing a bow without an arrow (dry fire) releases all stored energy into the limbs, which can shatter the bow and send wooden splinters into the archer's face and arms. Always nock an arrow before drawing.
- **Firearm barrel obstruction**: Firing a musket with a blocked barrel (mud, snow, previous ball stuck) causes catastrophic barrel failure -- the barrel bursts, sending iron fragments in all directions. Always run the ramrod down the barrel to confirm clear bore before loading.
- **Quenching hazards**: Quenching hot steel in water or oil produces violent steam or oil spatter. Wear face shield and leather apron. Oil quench tanks can ignite if steel is too hot -- keep fire extinguishing sand nearby.
- **Heat treatment fumes**: Salt bath nitriding (advanced heat treatment) produces toxic fumes. Work in ventilated area. Standard forge work produces CO -- ensure chimney or cross-ventilation in smithy.

---

## Limitations

- **Metallurgical constraints**: Weapon quality depends entirely on available metal. Wrought iron weapons bend and cannot hold sharp edges. Consistent steel production is prerequisite for reliable weapon manufacture.
- **Black powder hygroscopy**: Gunpowder absorbs moisture, degrades performance. Must store in dry containers (ceramic jars with wax-sealed lids, leather pouches with oil treatment). Damp powder produces weak, inconsistent ignition -- reduced muzzle velocity and accuracy.
- **Barrel manufacturing bottleneck**: Early musket barrels hammered from flat iron bar wrapped around mandrel and forge-welded (weak longitudinal seam). Improved: drilled from solid billet (requires machine tools -- see [Machine Tools](../machine-tools/index.md)). Drilled bore: straighter, stronger, more accurate.
- **Supply chain**: Firearms consume powder and lead at 15-60 g per shot. A 1000-soldier regiment firing 2 volleys per minute expends 30-120 kg powder and 60-70 kg lead per minute of combat. Industrial-scale [chemistry](../chemistry/index.md) and [mining](../mining/index.md) are prerequisites for sustained firearm warfare.
- **Training requirements**: Effective use of any weapon requires sustained training. Bow: 2-5 years to reach military proficiency (muscle development for draw weight). Sword: 6-12 months for basic competence, years for mastery. Musket: 4-8 weeks drill for basic proficiency -- decisive advantage in raising armies quickly. Pike: 2-4 weeks for formation drill.
- **Logistics of edged weapons**: A sword requires 2-5 kg of steel, a spear requires 0.2-0.5 kg of iron, an arrow requires 20-50 g of iron. Arrows are consumable -- a battle expends 20-60 arrows per archer. Industrial iron production (see [Iron & Steel](../metals/iron-steel.md)) is prerequisite for equipping mass armies with metal weapons.
- **Standardization problem**: Pre-industrial weapons vary significantly between individual craftsmen. Interchangeable parts require precision machine tools (see [Machine Tools](../machine-tools/index.md)). Without standardization, each musket requires custom-fitted ammunition, spare parts do not interchange between weapons, and repair requires a skilled armorer rather than simple part replacement.
- **Wear and replacement**: A steel sword blade lasts 5-20 years with regular maintenance but can fail in a single combat if it strikes bone, stone, or another blade edge-on. Musket barrels erode after 500-1000 shots (black powder residue is corrosive, bore gradually enlarges -> reduced accuracy and velocity). Arrow shafts break on impact -- expect 30-50% loss per engagement. Weapon attrition in sustained campaigning requires continuous resupply from rear workshops.

- **Combined arms**: No single weapon dominates. Spears hold formation, bows provide ranged fire, swords and axes for close combat, polearms counter cavalry, firearms deliver decisive ranged lethality. Effective military organizations integrate multiple weapon types in mutual support.

---

## References

- **[Explosives & Propellants](../chemistry/explosives.md)** -- Black powder composition, smokeless powders, and propellant manufacture
- **[Iron & Steel Production](../metals/iron-steel.md)** -- Weapon-grade steel heat treatment and carburization
- **[Armor & Protective Systems](armor.md)** -- The defense against these weapons
- **[Foundations: Stone & Wood Tools](../foundations/index.md)** -- Earliest weapon-making materials
- **[Machine Tools](../machine-tools/index.md)** -- Barrel drilling and interchangeable parts
- **[Mining](../mining/index.md)** -- Iron ore, copper, tin, and lead extraction

---

 *Part of the [Bootciv Tech Tree](../index.md) • [Defense & Military](./index.md) • [All Domains](../index.md)*
