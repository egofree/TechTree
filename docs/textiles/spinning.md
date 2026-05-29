# Spinning

> **Node ID**: textiles.spinning
> **Domain**: [Textiles](./index.md)
> **Dependencies**: [`textiles.weaving`](weaving.md)
> **Enables**: [`plants.fiber-plants`](../plants/fiber-plants.md), [`textiles.fibers`](fibers.md), [`textiles.rope-making`](rope-making.md)
> **Timeline**: Years 0-5
> **Outputs**: yarn, thread
> **Critical**: No

## Spinning (converting fiber to yarn/thread)

**[Drop spindle](../glossary/drop-spindle.md)** (Foundations stage, simplest):
- **Construction**: Round whorl (50-100 g, 3-5 cm diameter) on straight wooden shaft (20-30 cm). Whorl materials: fired clay (most common — shape on wheel, dry, fire to hardness), stone (sandstone or limestone, drilled center hole), or turned wood (hardwood, weighted with clay or lead if needed). Shaft: hardwood (ash, maple, oak), 10-20 g total weight for fine yarns, 30-50 g for heavier yarns. Notch or hook at top to secure yarn. Spindle must be balanced — whorl centered on shaft, or vibration wastes energy and produces uneven yarn.
- **Process**: Draft (pull thin stream of fiber from rolag), spin spindle (twist inserted by rotation — clockwise for Z-twist, counterclockwise for S-twist), wind spun yarn onto shaft. Speed: ~50-100 meters per hour. Can produce thread from very fine (sewing) to heavy (rope yarn).
- **Twist direction**: Z-twist (clockwise when viewed from above) is standard for single yarns. Plying (combining multiple singles) uses opposite twist (S-twist) to balance the yarn and prevent kinking.

**[Spinning wheel](../glossary/spinning-wheel.md)** (the Metallurgy-Machine Tools stage transition, 10x throughput):
- **Great wheel (walking wheel)**: Large (1-1.5 m) wheel turned by hand. Drive band (cord or leather belt) connects wheel groove to spindle assembly. Wheel rotation spins spindle at high speed — typical drive ratio 30:1 to 80:1. Spinner walks backward while drafting fiber away from spindle, then reverses direction to wind yarn onto spindle. No treadle — one hand turns wheel, other drafts fiber. Best for woolen spinning. Production: 200-500 m/hour.
- **Treadle wheel (Saxony/flax wheel)**: Foot treadle drives wheel via crank, leaving both hands free for fiber control. Flyer and bobbin assembly: flyer (U-shaped bracket with hooks) adds twist, bobbin winds yarn at slightly different speed (controlled by Scotch tension or double-drive band). Ratios 8:1 to 20:1 (spindle revolutions per wheel revolution). Fine linen requires high ratio. Production: 300-800 m/hour. Requires precision woodwork and iron fittings for bearings.
- **Charka (book charka)**: Small portable wheel, hand-cranked. For cotton. High speed, fine yarn.

**Strengths**:
- Drop spindle produces usable yarn with only a fired clay whorl and wooden shaft
- Treadle wheel leaves both hands free for fiber control — 300-800 m/hour vs 50-100 m/hour for drop spindle
- Z-twist/S-twist convention ensures consistent yarn direction across all spinners

**Weaknesses**:
- Drop spindle limited to 50-100 m/hour — a single garment needs days of spinning
- Treadle wheel requires precision woodwork and iron fittings for bearings
- Great wheel requires one hand to turn, reducing drafting control

## Spinning Wheel Construction

Building a treadle spinning wheel requires woodcraft skill and basic iron hardware. Key dimensions and components:

**Wheel assembly**:
- Wheel diameter: 45-60 cm for a compact wheel, 80-120 cm for a production wheel. Construct from 8-12 wooden spokes mortised into a central hub (hardwood, 5-8 cm diameter, iron axle journal). Rim segments steam-bent from ash or oak, 2-3 cm cross-section, joined with overlapping scarf joints and glue. Wheel must run true — wobble causes uneven twist insertion and vibration. Rim groove (3-5 mm deep) holds the drive band.
- Flyer assembly: U-shaped wooden or iron bracket rotating on a horizontal axis. Arms 12-18 cm long, with 4-8 metal hooks spaced along each arm to guide yarn onto the bobbin. The flyer rotates as a unit with the whorl (driven by the drive band), inserting twist into the fiber.
- Bobbin: Hollow wooden cylinder (8-12 cm long, 2-3 cm diameter, 1.5-2 cm bore) that slides onto the spindle shaft inside the flyer. Bobbin rotates independently of the flyer — the speed difference between flyer and bobbin winds yarn onto the bobbin. Bobbin must turn freely on the spindle; bush with brass tubing or polished iron washers at each end.
- Whorl: Pulley on the spindle shaft, driven by the drive band. Groove diameter determines the drive ratio. Most treadle wheels use a multi-groove whorl (2-3 grooves of different diameters) to offer different ratios. Smaller whorl groove = higher ratio = more twist per treadle.

**Tension mechanisms**:
- **Scotch tension**: A brake band (thin cord or leather) wraps around the bobbin flange and is tensioned by a spring or adjustable screw. The brake slows the bobbin relative to the flyer, causing yarn to wind on. Adjusting brake tension controls take-up speed. Simple, effective, easy to build. Preferred for beginners and most general spinning.
- **Double drive**: A single drive band loops twice — once around the wheel and flyer whorl, once around the wheel and bobbin whorl. The different whorl diameters create a speed differential. Produces more consistent yarn but requires precise adjustment. Common on traditional Saxony wheels.
- **[Irish tension](../glossary/irish-tension.md)** (bobbin-led): Drive band connects wheel to bobbin whorl; brake on the flyer. Less common, produces a softer take-up. Suitable for bulky yarns.

**Treadle mechanism**: Foot treadle (hardwood plank, 15-20 cm × 8-10 cm) connected to wheel crank via a pitman rod (wooden or iron connecting rod, 30-50 cm). Crank offset 3-5 cm from wheel axle — this converts rotary motion to the reciprocating treadle. The treadle pivots at its rear end on a metal pin or leather hinge. Iron bearings at the crank pitman joint reduce wear.

**Strengths**:
- Scotch tension mechanism uses only a brake cord and spring — simple to build and adjust
- Multi-groove whorl offers 2-3 drive ratios on one wheel — versatile for different yarn weights
- Treadle converts foot motion to continuous spindle rotation — both hands stay on the fiber

**Weaknesses**:
- Wheel must run true — wobble causes uneven twist and vibration
- Bobbin must turn freely on spindle; brass tubing or polished iron washers needed at each end
- Steam-bent rim segments with scarf joints require woodcraft skill to execute properly

## Thread Sizing Systems

Quantifying yarn thickness for consistent cloth production:

- **Tex system**: Grams per 1,000 meters of yarn. Direct measure — higher tex = thicker yarn. sewing thread ~10-30 tex; knitting yarn ~100-400 tex; rope yarn 500+ tex. The most intuitive system for bootstrap use.
- **English cotton count (Ne)**: Number of 840-yard hanks per pound. Inverse — higher Ne = finer yarn. Ne 10 (coarse), Ne 30 (medium), Ne 60 (fine), Ne 100+ (very fine). Standard for cotton.
- **Metric count (Nm)**: Number of 1,000-meter lengths per kilogram. Same inverse relationship. Nm 10 = coarse, Nm 40 = medium, Nm 100+ = fine. Common for linen and wool.

## Plying (making multi-strand yarn)

Spin two or more singles together in opposite twist direction. Creates balanced, stronger yarn:
- **2-ply** (most common): Two singles, S-twist plied from Z-twist singles. Balanced, relatively flat cross-section. General-purpose weaving yarn.
- **3-ply**: Three singles. Rounder cross-section, stronger, more abrasion-resistant. Preferred for knitting yarns and sewing thread.
- **4-ply and heavier**: For rope, carpet warp, and heavy industrial thread.
- **Plying procedure**: Wind singles onto separate bobbins. Mount bobbins on lazy kate (rack holding bobbins with tension). Feed singles through plying hook onto spinning spindle or wheel bobbin. Spin in opposite direction to singles twist. Aim for balanced yarn — hang a length; if it hangs straight without twisting on itself, it is balanced.

## Twist Angle and Yarn Strength

The amount of twist directly determines yarn properties. Twist angle (angle between fiber axis and yarn axis) is the key metric:
- **Low twist** (twist angle <15°): Fibers slide past each other → weak, fuzzy yarn. Suitable only for novelty yarns.
- **Medium twist** (15-25°): Standard weaving yarn. Good balance of strength, flexibility, and drape. Woolen yarns typically spun at lower twist than worsted.
- **High twist** (25-45°): Very strong, smooth, hard yarn. Used for warp (must withstand loom tension) and sewing thread. Crepe yarns use extremely high twist (60°+) to create lively, elastic fabrics.
- **Rule of thumb**: Finer fibers and finer yarns require more turns per inch. A 2-ply yarn for general weaving: 8-12 tpi for wool, 12-20 tpi for cotton, 15-25 tpi for linen.

## Fiber Preparation Before Spinning

Before fiber can be spun, it must be cleaned, opened, and aligned:

- **Wool**: Shear fleece → sort by quality (shoulder and back = finest, breech and belly = coarsest) → wash in warm water (40-50°C) with mild alkali (soap or ammonia) to remove lanolin (wool grease, ~10-30% of raw fleece weight) and dirt → rinse thoroughly → dry → tease (pull apart by hand to open locks). Lanolin recovered from wash water is useful for waterproofing and lubrication.
- **Cotton**: Ginned (seeds removed by roller gin or saw gin) → willowed (beaten to open compressed bales and remove trash) → carded (see below).
- **Flax (linen)**: Retted (soak stalks in water 5-14 days — bacteria dissolve pectin binding fibers to woody core) → break (crush woody core with flax brake) → scutch (beat with wooden blade to remove broken woody shives) → hackle (draw through iron combs to separate long line fibers from short tow). Line fibers produce fine, strong linen; tow produces coarse yarn for rope and sacking.

**[Carding](../glossary/carding.md)** (aligning fibers for spinning):
- **Hand cards**: Pair of rectangular paddles (10 × 20 cm) covered in card cloth (stiff wire teeth, 1-2 cm long, set in leather or rubber backing). Charge one card with teased fiber. Brush cards together — teeth pull fibers into parallel alignment. Transfer rolled rolag (cylindrical roll of carded fiber, 10-15 cm long, 3-5 cm diameter) from card. Each rolag feeds one spindle-full of yarn. Rate: 0.5-1 kg of carded fiber per hour.
- **[Drum carder](../glossary/drum-carder.md)** (Machine Tools): Rotating drum (20-40 cm diameter) covered with card cloth feeds against smaller roller. Continuous output as carded batt (flat sheet of aligned fiber). 5-10 kg/hour throughput. Significantly faster than hand carding.

## Troubleshooting Common Yarn Defects

- **Yarn breaks frequently**: Insufficient twist for the fiber staple length. Increase twist (higher wheel ratio or slower drafting). Fiber may be too short — ensure hackled flax (not tow) for fine linen, or carded (not combed) wool for short-staple breeds. Check for remaining vegetable matter causing weak spots.
- **Uneven thickness (slubs)**: Drafting technique issue. Practice maintaining consistent pull length. Draft slower relative to wheel speed. Pre-draft fiber into uniform strips before spinning. For drum-carded batts, peel off thin strips along the grain.
- **Overplied yarn (corkscrews)**: Plying twist exceeds singles twist. The plied yarn twists back on itself. Reduce plying time or remove some plying twist. Hang a test length — if it twists on itself, it is overplied.
- **Underplied yarn (floppy)**: Plying twist insufficient. Singles separate under tension. Add more plying twist. Underplied yarn is weaker and fuzzy.
- **Fuzzy yarn**: Low twist or short fiber. Increase twist. Use longer-staple fiber. Combed (worsted) preparation produces smoother yarn than carded (woolen).
- **Kinky yarn off the bobbin**: Yarn is "lively" — singles are overtwisted relative to the plying. Let bobbins rest 24 hours before plying to allow twist to relax. Or ply soon after spinning while energy is still active.

## Industrial Spinning (Machine Tools stage and beyond)

Mechanized spinning multiplies output by 10-100× over hand spinning:

**Water frame (Arkwright, 1769)**:
- Powered by water wheel (later steam). Rollers draw out fiber (replacing hand drafting) and a flyer inserts twist. Produces a firm, even yarn suitable for warp — the critical bottleneck that had limited hand spinning. Roller speeds are graduated: each successive pair rotates faster, drawing the roving thinner. Typical roller diameters: 25 mm, with surface speeds increasing by 4-8× from the first pair to the last. 4-8 spindles per frame initially; later frames carried 40-80 spindles. Requires precision-turned rollers (iron, ground smooth) and reliable bearings.

**Spinning mule (Crompton, 1779)**:
- Combines water frame roller drafting with hand mule carriage travel. Carriage moves outward (drawing and twisting simultaneously), then returns (winding yarn onto spindles). Produces the finest, most uniform yarn of any spinning system — fine enough to match hand-spun Indian muslin. Carriage travel: 1.5-2 m stroke. 300-1,300+ spindles per mule by the 1830s. Self-acting mule (1830s) automated the carriage return, eliminating the need for child labor to push the carriage. Dominated fine cotton spinning for a century.

**Ring spinning (Thorpe, 1828; commercialized 1830s)**:
- Traveler (small C-shaped wire) rotates around a ring at high speed (5,000-15,000 rpm in modern machines, 3,000-5,000 rpm in early versions). The traveler inserts twist and winds yarn onto the bobbin simultaneously — no carriage stroke needed. Simpler mechanism, faster, continuous motion. Lower yarn strength than mule but higher production rate. C-rings made from hardened steel (required precision manufacture). By 1900, ring spinning produced ~80% of the world's cotton yarn. Remains the dominant spinning method today (~70% of global short-staple spinning).

**Open-end (rotor) spinning (1967)**:
- Fibers fed into a rotating drum (rotor, 30,000-150,000 rpm) that assembles them into yarn by centrifugal force. No spindle or traveler — twist inserted by rotor rotation. 3-5× faster than ring spinning. Yarn is hairier and weaker than ring-spun — acceptable for denim, towels, and industrial fabrics. Rotor diameter 28-56 mm. Not applicable to long-staple fibers (flax, wool top).

**Strengths**:
- Water frame produces firm, even warp yarn — breaks the hand-spinning bottleneck
- Ring spinning is continuous motion (no carriage stroke) — simpler and faster than mule
- Spinning mule produces the finest, most uniform yarn — fine enough to match hand-spun muslin

**Weaknesses**:
- Water frame requires precision-turned iron rollers and reliable bearings
- Ring spinning traveler runs at 3000-15,000 rpm — hardened steel C-rings wear out
- Open-end rotor yarn is hairier and 10-20% weaker than ring-spun — limited to coarse fabrics


[← Back to Textiles](index.md)
