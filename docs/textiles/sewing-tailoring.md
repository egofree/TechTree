# Sewing and Tailoring

> **Node ID**: textiles.sewing-tailoring
> **Domain**: [Textiles](./index.md)
> **Dependencies**: [`metals.copper-bronze`](../metals/copper-bronze.md), [`textiles`](./index.md), [`textiles.weaving`](weaving.md)
> **Enables**: [`construction`](../construction/index.md), [`transport.shipping`](../transport/shipping.md)
> **Timeline**: Years 5-10
> **Outputs**: garments, tents, sails, bags, belting
> **Critical**: No


Sewing transforms flat woven cloth into shaped, functional products: garments, tents, sails, bags, and belting. The craft demands precision — a needle eye with any burr shreds thread, a dull point tears fabric instead of piercing it, and a poorly constructed seam fails under load. Sewing technology bridges from hand stitching with bone needles to industrial lockstitch machines, enabling mass production of textile goods.

## Prerequisites

- [Weaving](weaving.md) — woven cloth as the primary material
- [Iron & Steel](../metals/iron-steel.md) — steel wire for needle manufacture
- [Copper & Bronze](../metals/copper-bronze.md) — early needle and thimble materials

## Needle Making

A sewing needle is a slender steel shaft with a point at one end and an eye (hole) at the other. The precision required is surprisingly high: the eye must be smooth-edged (any burr shreds the thread), the point must be sharp enough to pierce fabric without widening the hole, and the shaft must be straight and flexible enough to pass through the material without bending permanently.

**Hand needle manufacture**:
- Start with iron or low-carbon steel wire (0.5-1.5 mm diameter, depending on needle size). Wire is cut to length (30-70 mm for typical hand needles).
- The eye end is flattened by hammering or rolling, then pierced with a punch (hardened steel tool, 0.3-0.8 mm diameter) driven through the flattened section. The pierced hole is deburred by drawing the needle through a progressively smaller die.
- The point is ground on a stone wheel or formed by swaging (hammering the tip between shaped dies). Needle points vary by purpose: sharp (for woven fabrics), ball point (for knits, slides between yarns without cutting them), wedge point (for leather, cuts a small slit).
- Hardening: heat to 750-800°C (bright cherry red), quench in oil or water. Tempering at 300-400°C to reduce brittleness while maintaining hardness (Rockwell C 50-55 for standard needles).
- Polishing: needles are tumbled in a barrel with abrasive powder (emery or pumice) for 8-24 hours to achieve a smooth surface. Final polish with iron oxide (rouge) for corrosion resistance.

**Strengths**:
- Hand needle manufacture uses only iron/steel wire, a punch, and grinding stone — minimal tooling
- Ball-point needles slide between knit yarns without cutting them — prevents run damage
- Barrel polishing produces smooth, burr-free eyes that do not shred thread

**Weaknesses**:
- Eye must be deburred perfectly — any rough edge breaks thread repeatedly during sewing
- Hardening and tempering (750-800°C quench, 300-400°C temper) requires temperature control
- Tumbling polish takes 8-24 hours per batch — slow throughput

**Needle sizing**:
- Hand needles are sized by number (1-12 in the Singer system). A size 9 needle (most common for general sewing) is about 0.8 mm diameter × 40 mm long. A size 1 (heavy duty) is about 1.5 mm × 55 mm.
- Machine needles are sized in the metric system (60-130, where the number × 0.01 = shaft diameter in mm). A size 80 needle is 0.80 mm diameter. Needle choice depends on thread size and fabric weight: size 60-70 for silk and fine cotton, 80-90 for shirting, 100-110 for canvas, 120-130 for heavy leather.

## Thread

Thread must be strong enough to hold seams under stress, fine enough to pass through the needle eye without fraying, and smooth enough to slide through fabric without snagging.

**Linen thread**:
- Made from long flax fibers, wet-spun for maximum strength. Tensile strength: 400-600 MPa (comparable to mild steel by cross-sectional area). Linen thread is stiff, resists stretching, and is naturally resistant to rot and UV degradation.
- The standard for heavy-duty sewing (sails, canvas, leather) for centuries. Disadvantage: relatively thick for its strength compared to synthetic threads. Limited range of natural colors (gray, brown, blond).

**Cotton thread**:
- Spun from cotton fibers, mercerized for strength and luster. Tensile strength: 200-400 MPa. Softer and more flexible than linen. Takes dye well. Good for garment sewing.
- Absorbs moisture (up to 7% by weight), which weakens it slightly when wet. Degrades faster than linen under UV exposure.

**Silk thread**:
- Made from continuous silk filament (not spun staple). Tensile strength: 400-600 MPa. Extremely fine for its strength: a silk thread can be half the diameter of a linen thread with equivalent breaking strength.
- Naturally smooth, slides through fabric with minimal friction. Used where fineness and strength both matter: buttonholes, decorative topstitching, glove making, fine leatherwork.

**Thread construction**:
- Thread is usually 2 or 3 ply (two or three single yarns twisted together). The twist direction (S or Z) alternates between singles and plying twist to produce a balanced thread that does not kink or curl when relaxed.
- Thread size: numbered systems vary. In the ticket number system, higher numbers indicate finer thread. A No. 50 cotton thread has a breaking strength of about 8-10 N. A No. 10 linen thread has about 40-50 N.

## Seam Types and Strength

A seam is only as strong as its construction. Different seam types suit different applications, trading strength, bulk, fabrication time, and appearance.

**[Plain seam](../glossary/plain-seam.md)** (most common, simplest):
- Two pieces of fabric placed right sides together, stitched 10-15 mm from the raw edge, then opened flat. The seam allowance is pressed to one side.
- Strength retention: 80-90% of fabric tensile strength. The stitching line is the weak point (thread breaks before fabric tears). Raw edges fray unless finished (zigzag stitch, overlocked, or bound with tape).
- Used for most garment seams where appearance matters more than maximum strength.

**[Felled seam](../glossary/felled-seam.md)** (self-enclosed, strong):
- One seam allowance is folded over the other and stitched down. The raw edges are enclosed inside the fold, preventing fraying. Two rows of stitching visible on the outside.
- Strength retention: 90-95%. The double stitching and enclosed edges make it resistant to tearing and abrasion. Standard for jeans, military uniforms, tents, workwear.
- Adds bulk (four layers of fabric at the seam). Takes 2-3× longer to construct than a plain seam.

**[Flat-felled seam](../glossary/flat-felled-seam.md)** (strongest standard seam):
- Both seam allowances are trimmed, wrapped around each other, and topstitched flat. Creates a smooth, low-profile seam with no raw edges exposed on either side.
- Strength retention: 95-100% of fabric strength. The mechanical interlock of the folded edges distributes stress over a wider area. Standard for jeans inseams, sail panels, awnings, canvas goods.
- Construction requires precision folding. Industrial machines with felling attachments automate this; hand sewing requires careful basting before final stitching.

**[French seam](../glossary/french-seam.md)** (enclosed, for fine fabrics):
- Fabric is stitched wrong sides together (first pass, narrow seam allowance of 5-7 mm), then turned inside out and stitched right sides together (second pass, 8-10 mm from the folded edge), enclosing the raw edges.
- Strength retention: 85-90%. Two stitching lines share the load. Neat finish on both sides with no visible raw edges.
- Used for sheer fabrics (chiffon, organza), lingerie, and children's clothing where bulk and exposed edges are unacceptable.

**Strengths**:
- Felled and flat-felled seams retain 90-100% of fabric strength with self-enclosed edges
- French seam hides all raw edges in two-pass stitching — clean finish on both sides
- Plain seam is fast to construct and retains 80-90% fabric strength for most garments

**Weaknesses**:
- Felled seam adds four layers of bulk — unsuitable for fine or lightweight fabrics
- Flat-felled seam requires precision folding; hand sewing needs basting before final stitching
- Plain seam raw edges fray unless finished separately (zigzag, overlock, or binding)

## Garment Construction

**Pattern drafting**:
- A pattern is a 2D template for each fabric piece. Patterns are drafted from body measurements: chest, waist, hip, shoulder width, arm length, torso length, inseam. A basic bodice block (the foundation pattern) requires 8-12 measurements.
- Ease (the difference between body measurement and garment measurement) allows movement: 5-10 cm at the chest for a fitted garment, 15-25 cm for a loose work garment. Too little ease restricts movement; too much looks baggy and catches on equipment.
- Pattern pieces are arranged on the fabric (lay planning or marker making) to minimize waste. Tight nesting of pattern pieces achieves 80-90% fabric utilization for simple garments (T-shirts, trousers). Complex garments (jackets with multiple panels, collars, cuffs) achieve 70-80%.

**Cutting**:
- Fabric is spread flat (single layer for precision cutting, multiple layers up to 10-20 for production cutting). Pattern pieces traced or pinned to the fabric, then cut with shears or a rotary cutter.
- Marking: seam lines, notches (matching points between pieces), and dart lines are transferred to the fabric with tailor's chalk, tracing wheel and carbon paper, or thread basting. Accuracy at this stage determines fit quality.

## Specific Products

**Tents** (shelter):
- Canvas (cotton duck, 300-400 g/m²) is the standard tent fabric. Heavy but waterproof when wet (cotton fibers swell to close the pores), breathable (reduces condensation inside), and repairable with needle and thread in the field.
- Seams: double-stitched (two parallel rows, 6-8 mm apart) with heavy linen thread. Stress points (ridge, eaves, corner tie-outs) are reinforced with additional fabric patches (gussets) or webbing loops stitched through all layers.
- Waterproofing: canvas tents are naturally water-resistant after the first wetting (fiber swelling). Additional treatment with wax or oil-based waterproofing extends service life in prolonged rain.
- Typical sizes: 2-person patrol tent, 3-4 kg canvas, 2.0 × 2.0 m floor, ridge height 1.3 m. Large marquee tent, 40-60 kg canvas, 6 × 10 m floor area, ridge height 2.5 m.

**Sails** (marine propulsion):
- Canvas or sailcloth (tightly woven cotton or linen, 200-600 g/m² depending on sail size and position). Panel layout follows stress lines: panels are cut on the bias (45° to the warp) for stretch resistance in the direction of load.
- Bolt rope: a rope (6-12 mm diameter, manila or hemp) sewn into the edge of the sail (luff, foot, leech) distributes stress along the edge and provides an attachment point to the mast or boom. Sewn with a bolt rope stitch (a variant of flat-felled seam), using tarred linen thread for rot resistance.
- Reinforcement patches at corners (where rigging loads concentrate) add 3-5 layers of additional canvas, tapered to spread the load gradually. Reef points (grommets for tying down the sail in heavy weather) are hand-set brass or galvanized iron rings, sewn through all layers.

**Bags and sacks**:
- Heavy canvas (400-600 g/m²) or woven jute (burlap, 200-400 g/m²). Flat-felled seams for strength. Webbing handles (woven cotton or jute tape, 30-50 mm wide) are folded over the bag edge and stitched through all layers with a box-X stitch pattern (a rectangle with an X inside, distributing load across 8-12 stitch points).
- Grain sacks hold 25-100 kg. The weave must be tight enough to contain the grain (warp/weft spacing < 1.5× grain particle diameter for rice, wheat, or corn).

**Belts and strapping**:
- Leather belts are cut from heavy hides (3-5 mm thick, cattle or horse). Multiple layers are riveted together with copper or iron rivets (4-6 mm shank diameter) for extra strength. A 2-ply leather belt, 50 mm wide, can support 500-1000 N before permanent stretching.
- Buckles are cast brass or forged iron, with a tongue (prong) that engages holes punched in the belt at 20-25 mm spacing. The bar of the buckle must be wider than the belt and strong enough to resist deformation under load.

## Industrial Sewing Machine

The lockstitch machine (invented by Elias Howe, 1846; refined by Isaac Singer) creates a stitch that looks identical on both sides of the fabric. It uses two threads: a needle thread (top) and a bobbin thread (bottom), interlocked in the middle of the fabric.

**Lockstitch mechanism**:
- The needle carries the top thread down through the fabric. At the bottom of its stroke, a small loop forms on the back side of the needle (aided by the scarf, a small notch cut in the needle shaft above the eye).
- A rotary hook (or oscillating shuttle) catches this loop and carries it around the bobbin (a small spool of thread sitting in a case underneath the fabric). The loop encircles the bobbin thread. As the needle rises, the loop tightens around the bobbin thread, pulling the interlock into the fabric layer.
- Stitch length: 1.5-5 mm, controlled by the feed dog mechanism (toothed bars that advance the fabric between stitches). Speed: 3000-5000 stitches per minute (SPM) on industrial machines. Domestic machines run at 800-1500 SPM.

**Machine setup**:
- Needle size must match thread and fabric. A size 80 needle with No. 50 cotton thread for shirt-weight fabric. A size 120 needle with heavy linen thread for canvas. Mismatched combinations cause skipped stitches, thread breakage, or fabric damage.
- Thread tension must be balanced: the interlock should occur in the middle of the fabric thickness. If the interlock is visible on the top surface, bobbin tension is too tight (or top tension too loose). If it shows on the bottom, top tension is too tight.
- Feed dog height and pressure must be set for the fabric thickness. Too much pressure mars the fabric surface; too little causes uneven stitch length or the fabric slipping.

**Machine construction** (bootstrap overview):
- Frame: cast iron, providing the rigidity needed for high-speed operation without vibration. The main shaft runs in two bronze bearings. The needle bar, presser bar, and feed dog are all driven by cams on the main shaft.
- Power: originally treadle-driven (foot pedal, 60-100 W human power). Later, belt-driven from a line shaft or electric motor. Industrial machines use a clutch motor (100-500 W) that allows the operator to control speed by foot pedal pressure.

**Strengths**:
- Lockstitch produces identical appearance on both sides — professional finish
- Industrial machines run 3000-5000 SPM — 10-20× faster than hand sewing
- Cast iron frame eliminates vibration at high speed — consistent stitch quality

**Weaknesses**:
- Rotary hook and bobbin require precision machining — ±0.05 mm tolerance on hook timing
- Thread tension must be balanced per fabric/thread combination — setup skill required
- Bobbin runs out and must be replaced frequently during long seams

## Hand Sewing Stitches

Not all sewing is done by machine. Many construction steps and field repairs require hand stitching.

- **Running stitch**: needle passes in and out of the fabric at regular intervals (3-5 mm). Fast but weak. Used for basting (temporary hold) and gathering.
- **Back stitch**: each stitch overlaps the previous by half, creating a continuous line of stitching. Strong (90% of machine stitch strength). Used for seams in heavy fabrics and for repairs where a machine is unavailable.
- **Whip stitch (overcast)**: needle passes over the edge of the fabric at an angle. Used to finish raw edges and prevent fraying. Quick but adds bulk.
- **Slip stitch (ladder stitch)**: needle catches a thread on each side of the fold, creating an invisible join. Used to close stuffed items (pillows, cushions) and attach linings. Nearly invisible on the finished surface.

## Pressing Equipment

Pressing (ironing) sets seams, removes wrinkles, and shapes garments during construction. It is not cosmetic; it is structural. Unpressed seams are puffy, do not lie flat, and the garment does not hold its shape.

**[Flat iron](../glossary/flat-iron.md)** (sad iron):
- A solid cast iron slab, 2-4 kg, with a flat bottom and a handle on top. Heated on a stove or over a fire. Working temperature: 150-200°C. The iron is too hot if it scorches a test scrap; too cool if it does not set a crease.
- Temperature is tested by spitting on the iron: drops that dance and skitter indicate 150-200°C (the Leidenfrost effect). Drops that evaporate immediately indicate >250°C (too hot for most fabrics). Drops that just sit and steam indicate <120°C (too cool).

**[Tailor's ham](../glossary/tailors-ham.md)** (pressing curved seams):
- A firmly stuffed fabric cushion (sawdust or sand filling, approximately 30 × 20 × 10 cm) shaped like a ham. Curved seams (darts, princess seams, sleeve caps) are pressed over the ham to preserve their 3D shape. Pressing flat would flatten the curve and distort the fit.

**[Seam roll](../glossary/seam-roll.md)** (pressing open seams):
- A cylindrical stuffed cushion (about 30 cm long, 5 cm diameter). Seams are pressed open over the roll so the seam allowances lie flat on either side without impressing into the fabric surface.

**Pressing cloth**:
- A layer of muslin or linen placed between the iron and the fabric. Prevents shine (a glossy mark caused by the iron pressing the fabric surface too directly). Essential for dark fabrics, wool, and any fabric with a textured surface.

## Fasteners

**Buttons**:
- Flat disks (10-25 mm diameter) with two or four holes, sewn to the fabric with matching or contrasting thread. Materials: bone, wood, metal (brass, iron), mother-of-pearl, or pressed horn. A 4-hole button is sewn with an X pattern through the holes, creating a shank of thread between button and fabric that allows the buttonhole to close over the button without strain.

**Rivets**:
- Copper or iron rivets (4-6 mm shank diameter, 6-12 mm cap diameter) for high-stress joints. The rivet shank passes through all fabric layers, then is set (flattened) with a hammer and anvil set. Standard for jeans pockets, bag corners, and belt loops.
- Rivets do not loosen with vibration or flexing the way stitches can. They are permanent: removing a set rivet requires destroying it.

## Measuring and Fitting

Proper fit requires systematic body measurement and pattern adjustment. A poorly fitted garment is uncomfortable, restricts movement, and fails at its job (a loose cuff catches on machinery; a tight shoulder seam tears under load).

**Body measurement**:
- Take measurements over the undergarments the wearer will use with the finished garment. A measuring tape (flexible fiberglass or plastic-coated fabric, 150 cm length, marked in cm and mm) wraps snugly but not tight around the body.
- Key measurements for a basic work shirt: neck circumference (at the Adam's apple), chest (at the widest point, arms relaxed at sides), shoulder width (across the back, from shoulder point to shoulder point), arm length (from shoulder point to wrist, arm slightly bent), back length (from the prominent vertebra at the base of the neck to the desired hem length).
- Allowance for movement: add 10-15 cm to chest measurement for a work shirt, 15-25 cm for a work jacket (to accommodate layers underneath and arm range of motion).

**Fitting adjustments**:
- A muslin mockup (a quick-sewn prototype in cheap unbleached cotton) is fitted on the wearer before cutting into the final fabric. Adjustments are pinned and marked, then transferred back to the pattern. This catches fitting problems before they become expensive mistakes in the good fabric.
- Common adjustments: shoulder slope (most people have one shoulder slightly higher), back width (broader backs need more fabric across the upper back), and armhole depth (too tight restricts arm lift; too loose looks baggy).

## Thimbles and Sewing Accessories

**Thimble**:
- A small cap (15-25 mm diameter) worn on the middle finger of the pushing hand. The surface is dimpled or textured to catch the needle head and push it through thick fabric without the needle slipping and puncturing the finger.
- Materials: steel (most durable, lasts decades), brass (softer but adequate for light work), or leather (flexible, used for heavy canvas and leather sewing where a rigid thimble is uncomfortable).
- A skilled hand sewer can maintain 30-60 stitches per minute with a thimble, compared to 15-30 without (the thimble allows firm, consistent pressure on the needle without pain).

**Other essential tools**:
- Seam ripper: a small blade with a curved tip that cuts stitches without damaging the fabric. Used for correcting mistakes and opening basting stitches.
- Pincushion: a fabric pad stuffed with wool or hair, holding steel pins (25-35 mm long, 0.5-0.7 mm diameter) for temporary fabric alignment during construction. The wool stuffing keeps pins slightly lubricated and rust-free.
- Tailor's chalk: flat pieces of chalk (white, blue, or yellow) for marking seam lines, darts, and construction points on fabric. Brushes off easily after sewing. Available in triangular or square shapes; a sharp edge is maintained by breaking off a corner.

## Key Deliverables

- Needle manufacturing capability (hand and machine needles)
- Thread production and selection (linen, cotton, silk)
- Seam construction techniques with known strength properties
- Garment pattern drafting and cutting layout optimization
- Measuring, fitting, and muslin mockup process
- Specific products: tents, sails, bags, belts
- Industrial lockstitch sewing machine construction and operation
- Hand sewing stitches for construction and repair
- Pressing tools and techniques
- Thimbles and sewing accessories
- Fastener types and applications

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Thread shredding at needle eye | Burr on needle eye or wrong thread weight | Deburr eye with fine abrasive; match thread weight to needle size; replace worn needle |
| Skipped stitches (machine) | Needle bent, wrong needle type, or timing off | Replace needle; use ball-point for knits, sharp for wovens; check hook-to-needle timing |
| Seam puckering | Thread tension too high or fabric stretched during sewing | Reduce thread tension; let feed dogs move fabric naturally; use shorter stitch length |
| Needle breaking | Wrong needle for fabric thickness or hitting pin | Use heavier needle for thick fabric; remove pins before sewing; check needle alignment |
| Seam pulling apart under load | Stitch type wrong or seam allowance too narrow | Use backstitch or lockstitch for load-bearing seams; increase seam allowance to 15 mm minimum |
| Fabric stretching during cutting | Not using pattern weights or cutting on bias | Pin pattern to fabric or use weights; cut on grain (parallel to selvage); mark grain line |

## See Also

- [Weaving](weaving.md) — woven cloth production
- [Iron & Steel](../metals/iron-steel.md) — steel for needles and pins
- [Leather](../animals/leather.md) — leather for belts and accessories
- [Spinning](spinning.md) — thread and yarn production
- [Dyeing](dyeing.md) — colored fabrics for garments
- [Mining Equipment](../mining/index.md) — sewn products used in mining

[← Back to Textiles](index.md)
