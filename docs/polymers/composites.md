# Polymer Composites — Process Reference

> **Node ID**: polymers.composites
> **Dependencies**: [`glass.fibers`](../glass/fibers.md), `machine-tools`, [`polymers.thermosets`](thermosets.md)
> **Enables**: None (leaf capability)


Fiber-reinforced polymer composites combine high-strength fibers (glass, carbon, aramid) with a binding matrix resin (polyester, epoxy, vinyl ester) to produce materials stronger and lighter than either component alone. Composites dominate aerospace structures, marine hulls, chemical-resistant tanks, electrical enclosures, and sporting goods — anywhere the combination of high strength-to-weight ratio, corrosion resistance, and design flexibility justifies the manufacturing effort.

The key advantage of composites over metals is **anisotropy**: fibers can be oriented to carry load in the directions where strength is needed, without wasting material on directions that see little stress. A steel beam is equally strong in all directions (isotropic), but a composite laminate can be 5× stronger along the fiber direction than across it — enabling highly optimized structures. The trade-off is manufacturing complexity: composite properties depend on fiber type, fiber volume fraction, matrix selection, layup method, and cure cycle, all of which must be controlled simultaneously.

This article covers fiber properties, layup methods, matrix selection, manufacturing techniques, and phase-dependent milestones for composite production.

## Limitations

- **Anisotropic properties**: Composites are strong along the fiber direction but weak between plies (interlaminar shear). Delamination — separation of layers — is the primary failure mode under impact or cyclic loading. Design must account for through-thickness stresses that metals handle naturally.
- **Temperature limits**: Polyester and vinyl ester matrices soften above 80-120°C. Epoxy systems reach 120-180°C. High-temperature applications (engine components, reentry structures) require polyimide or bismaleimide resins (200-300°C service) — significantly more expensive and harder to process. None approach the 500-1000°C capability of metals.
- **Quality inspection difficulty**: Voids, delaminations, fiber misalignment, and dry spots (insufficient resin wetting) are internal defects invisible to visual inspection. Ultrasonic C-scan or X-ray inspection is required for structural parts — adding cost and complexity. Hand layup quality depends heavily on operator skill and is difficult to standardize.
- **Repair complexity**: Damaged composites cannot be welded like metals. Repair requires grinding out the damaged area, layering new fabric and resin, and curing — a skilled, time-consuming process. Repaired areas rarely match original strength (typically 60-80% of parent laminate).
- **Recycling challenge**: Thermoset matrix composites cannot be remelted. Recycling options are limited to grinding into filler (low-value), pyrolysis (burn off resin, recover fiber — degrades fiber properties 10-30%), or solvent dissolution (recovers clean fiber but requires harsh chemicals). Carbon fiber recycling is economically viable at scale; fiberglass recycling is not.
- **Moisture absorption**: Epoxy and polyester matrices absorb 0.5-2.0% moisture by weight over time. Moisture plasticizes the matrix, reducing Tg by 20-40°C and decreasing stiffness and strength. Composite structures in marine or humid environments must be designed with degraded "wet" properties, not dry-room values.
- **UV degradation**: Polyester and epoxy resins degrade under UV exposure (surface chalking, microcracking). UV-resistant gel coats or paint systems are required for outdoor exposure.


## Fiberglass Properties

| Property | E-glass | S-glass |
|---|---|---|
| Tensile strength (single filament) | 3400 MPa | 4600 MPa |
| Tensile modulus | 72 GPa | 86 GPa |
| Elongation at break | 4.8% | 5.4% |
| Density | 2.54 g/cm³ | 2.48 g/cm³ |
| Filament diameter | 10-25 μm | 10-25 μm |
| Softening point | 840°C | 970°C |
| Cost relative to E-glass | 1× | 3-5× |

E-glass (electrical grade, alumino-borosilicate) is the workhorse composite fiber — 90%+ of all fiberglass production. S-glass (structural grade, magnesia-alumina-silicate) provides 30-40% higher tensile strength at 3-5× the cost, used primarily in aerospace and ballistic applications.

## Carbon Fiber Properties

| Property | Standard Modulus | Intermediate Modulus | High Modulus |
|---|---|---|---|
| Tensile strength | 3500 MPa | 4500-7000 MPa | 2500-3500 MPa |
| Tensile modulus | 230 GPa | 290-300 GPa | 500-600 GPa |
| Density | 1.78 g/cm³ | 1.80 g/cm³ | 1.85 g/cm³ |
| Elongation at break | 1.5% | 1.7-2.0% | 0.5-0.7% |

All values are PAN-based carbon fiber (polyacrylonitrile precursor). Carbon fiber is 5× stronger than steel at roughly ¼ the weight (steel: tensile 400-800 MPa, density 7.8 g/cm³; standard modulus carbon: 3500 MPa, 1.78 g/cm³ — specific strength ~17× steel).

## Aramid Fiber Properties

| Property | Kevlar 29 | Kevlar 49 | Kevlar 149 |
|---|---|---|---|
| Tensile strength | 2900 MPa | 3600 MPa | 3400 MPa |
| Tensile modulus | 70 GPa | 130 GPa | 185 GPa |
| Density | 1.44 g/cm³ | 1.44 g/cm³ | 1.47 g/cm³ |
| Elongation at break | 3.6% | 2.5% | 1.5% |

Kevlar 49 is the standard composite reinforcement grade. Outstanding impact resistance — absorbs 3-5× more energy per unit weight than steel. Flame resistant (chars above 400°C, does not melt or drip). Negative coefficient of thermal expansion in fiber direction (contracts when heated) — useful for dimensional stability in space structures.


## Hand Layup

The simplest composite manufacturing method, achievable at minimal technology level. Sequence:

1. **Mold preparation**: Apply release agent (paste wax, PVA film, or silicone spray) to mold surface to prevent cured part from sticking.
2. **[Gel coat](../glossary/gel-coat.md)** (optional): Apply a thin layer (0.3-0.5 mm) of pigmented, unreinforced resin directly to the mold surface. This becomes the cosmetic outer surface of the finished part. Cure until tacky (30-60 minutes for polyester).
3. **Layup**: Cut fiberglass mat or fabric to shape. Place on mold. Apply resin by brush or roller. Work resin into the fiber with a consolidation roller (serrated aluminum or nylon roller) to wet out the fiber and remove entrapped air. Add additional layers, alternating fiber direction (0°/90°/±45° orientations typical), with resin between each layer.
4. **Cure**: Allow to cure at ambient temperature (20-30°C, 24 hours for full cure). Post-cure at 60-80°C for 2-4 hours to improve properties if oven is available.

Typical fiber volume fraction: 20-30% (random chopped strand mat) to 30-45% (woven fabric). Hand layup produces laminates with 2-5% void content (air bubbles trapped between layers) — acceptable for many applications but not for structural or aerospace use.

## Vacuum Bagging

Improves hand layup quality by applying uniform consolidation pressure and removing trapped air.

1. Complete hand layup as above on mold surface.
2. Place a porous release film (perforated nylon) over the wet laminate — allows air and excess resin to pass but prevents bag from sticking.
3. Place bleeder/breather cloth (non-woven polyester felt, 2-5 mm thick) over release film — provides a path for air evacuation and absorbs excess resin.
4. Seal vacuum bag (nylon film, 0.05-0.1 mm thick) around the mold perimeter with mastic sealant tape.
5. Attach vacuum pump to the bag via a fitting. Evacuate to 0.5-1.0 bar vacuum (85-95% of atmospheric pressure). This applies ~0.08-0.10 MPa consolidation pressure uniformly over the entire laminate.
6. Maintain vacuum during cure (room temperature 24 hours, or elevated temperature in an oven — the vacuum bag withstands 80-120°C).

Vacuum bagging reduces void content from 2-5% (hand layup) to <1%, improves fiber volume fraction to 50-55% (woven fabric), and produces consistent, repeatable laminate quality with minimal voids.

## Pultrusion

Continuous process for producing constant cross-section profiles (rods, tubes, angles, I-beams, channels). Product speeds 0.5-2.0 m/minute.

1. **Fiber creels**: Continuous roving or unidirectional tow pulled from racks of fiber spools. Additional fiber mats or fabrics added for transverse strength.
2. **Resin bath**: Fibers pass through an open bath of catalyzed polyester or vinyl ester resin. Rollers or pins guide the fibers through the bath, ensuring complete wetting. Resin content controlled by wiper dies or rollers after the bath.
3. **Preformer**: A series of guide plates that gradually shape the wet fiber bundle from a flat tape into the approximate final cross-section.
4. **Heated die**: Chrome-plated steel die with internal heating elements (electric cartridge heaters). Temperature profile: 90°C → 150°C → 180°C along die length (progressive cure). Resin gels and cures as the profile passes through the 0.5-1.0 m long die.
5. **Puller**: Reciprocating clamp or caterpillar belt that grips the cured profile and pulls it at constant speed (0.5-2 m/min).
6. **Cutoff saw**: Cuts continuous profile to desired length.

Fiber volume fraction: 60-70% (highest of any composite process due to unidirectional fiber alignment and die consolidation). Used for: structural profiles (grating, handrails, structural angles), electrical insulation rods, tent poles, fishing rods, reinforcing bars for concrete.

## Fiber Volume Fraction Optimization

The mechanical properties of a composite laminate are dominated by fiber volume fraction (Vf, the percentage of the laminate volume occupied by fiber rather than matrix resin).

| Fiber Format | Typical Vf | Notes |
|---|---|---|
| Random chopped strand mat | 20-30% | Lowest properties, easiest to process |
| Unidirectional tape (hand layup) | 50-60% | Maximum properties in fiber direction |
| Woven fabric (hand layup) | 40-50% | Balanced 0°/90° properties |
| Woven fabric (vacuum bag) | 50-55% | Improved by consolidation pressure |
| Pultruded unidirectional | 60-70% | Highest Vf achievable |
| Filament wound | 60-65% | High Vf on cylindrical shapes |

Rule of mixtures estimate (longitudinal tensile modulus): Ec = Vf × Ef + (1-Vf) × Em. For E-glass/Epoxy: Ec = 0.50 × 72 + 0.50 × 3.5 = 37.75 GPa (vs. aluminum 69 GPa, steel 200 GPa — but at 2.0 g/cm³ vs. 2.7 and 7.8, the specific stiffness is competitive).

## Matrix Selection Guide

| Matrix | Cost | Tensile Strength | Cure | Best Application |
|---|---|---|---|---|
| Polyester | Low ($2-4/kg) | 40-90 MPa | RT, MEKP | Marine, general purpose, tanks |
| Vinyl ester | Medium ($4-8/kg) | 70-80 MPa | RT, MEKP | Corrosion-resistant, chemical tanks |
| Epoxy | High ($8-20/kg) | 55-130 MPa | RT-80°C, amine | Aerospace, high-performance, tooling |
| Phenolic | Medium ($5-10/kg) | 30-60 MPa | Heat, acid | Fire-resistant panels, transit interiors |

Polyester: cheapest, most widely used, adequate for 90% of fiberglass applications. Room temperature cure with MEKP catalyst — no oven needed. Shrinkage during cure: 5-8% (higher than epoxy, can cause warpage in thin laminates). Styrene emission during open-mold layup is the primary health concern.

Epoxy: highest mechanical properties, lowest shrinkage (<2%), best adhesion to fibers, longest pot life flexibility. But 3-5× more expensive than polyester. Used where performance justifies cost: aerospace, high-performance sporting goods, tooling (molds for other composites), structural repairs.

Vinyl ester: hybrid chemistry — epoxy backbone with unsaturated ester end-groups. Combines epoxy's chemical resistance with polyester's room-temperature MEKP cure. Best choice for corrosion-resistant tanks, pipes, and chemical equipment. Cost: 2× polyester, 0.5× epoxy.


## Fiber Production

Raw materials: silica sand (~60%), limestone (~20%), borax (~10%), alumina,
soda ash. Batch melted at ~1400°C, drawn through platinum-rhodium bushings
into filaments 5–25 µm diameter, coated with sizing (silane coupling compound + film former) for protection and resin adhesion.
- **[E-glass](../glossary/e-glass.md)** (electrical): alumino-borosilicate, most common, cheaper
- **[S-glass](../glossary/s-glass.md)** (structural): magnesia-alumina-silicate, ~30% higher tensile
  strength, higher melt temperature
Forms: continuous roving, chopped strand mat (25–50 mm random fibers),
woven fabric (plain, twill, satin weave).

## Matrix Resins

| Resin | Cure | Notes |
|---|---|---|
| Polyester | Room temp, MEKP catalyst | Cheapest, most common |
| Epoxy | Room temp to 80°C, amine hardener | Higher strength, lower shrinkage |
| Vinyl ester | Room temp, MEKP | Best chemical/corrosion resistance |

## Layup and Molding Processes

**Hand layup.** Dry fiber over open mold, resin by brush/roller. Simple, low
capital cost. Chemistry stage achievable.
**Spray-up.** Chopped fiber + catalyzed resin sprayed from gun onto open mold.
Faster but lower fiber content. Chemistry stage achievable.
**Vacuum bagging.** Part covered with bagging film, evacuated with vacuum pump.
Consolidates laminate, removes air, improves fiber-to-resin ratio. Vacuum & Optics stage.
**Resin transfer molding (RTM).** Dry preform in closed two-part mold, resin
injected under pressure. Better surface finish, higher repeatability.

## Curing

Polyester/vinyl ester cure at room temp with MEKP (gel 20–60 min). Epoxy may
need 50–80°C for full crosslinking. Post-cure heat (up to 80°C) improves
properties across all systems.

## Applications

Storage tanks, chemical-resistant piping, boat hulls, architectural panels,
electrical enclosures, corrosion-resistant housings, vehicle body panels.

## Carbon Fiber

Requires sustained advanced petrochemical industry (PAN from acrylonitrile),
controlled-atmosphere furnaces at 1500°C+ under inert gas, multi-hour thermal
process control. Well beyond Chemistry-Vacuum Optics stages.

## PAN Precursor Route (Primary)

Polyacrylonitrile from acrylonitrile, wet- or dry-spun into precursor fibers.
Stabilization: 200–300°C in air, several hours. Carbonization: 1000–1500°C
in N₂, drives off non-carbon atoms. Optional graphitization: 2500–3000°C.
Surface treatment and sizing applied before winding.

## Pitch Precursor Route

Petroleum/coal tar pitch melt-spun, stabilized and carbonized. Lower cost,
less common for high-performance grades.

## Properties and Applications

5x stronger than steel at roughly 1/4 the weight. Excellent fatigue resistance.
Applications: aerospace frames, lightweight structural components, sporting
goods, robotic limbs.

## Aramid Fiber / Kevlar

Requires exotic aromatic monomers (paraphenylene diamine, terephthaloyl
chloride) from multi-step organic synthesis, plus NMP/CaCl₂ solvent recovery.
Well beyond Chemistry-Vacuum Optics stages chemical capabilities.

## Process

Low-temperature solution polycondensation of paraphenylene diamine with
terephthaloyl chloride in NMP/CaCl₂. Liquid-crystalline solution wet-spun
through spinneret. Fibers drawn, washed, thermally annealed under tension to
develop crystalline orientation.

## Properties and Applications

Very high tensile strength-to-weight ratio. Outstanding impact and abrasion
resistance. Flame resistant (chars above 400°C, does not melt). Low density.
Applications: ballistic panels, high-strength cordage, fire-resistant garments,
structural reinforcement in hybrid composites.

## Composite Manufacturing Techniques

| Technique | Phase | Equipment | Best For |
|---|---|---|---|
| Hand layup | 5 | Brushes, rollers, open mold | Low-volume, large parts |
| Spray-up | 5 | Chopper gun, open mold | Medium-area, moderate volume |
| Vacuum bagging | 6 | Vacuum pump, bagging film | Improved quality over hand layup |
| Filament winding | 6 | Winding machine, mandrel | Cylinders, pressure vessels |
| Pultrusion | 6–7 | Heated die, puller, creels | Constant cross-section profiles |
| Compression molding | 6–7 | Matched metal molds, press | Higher volume, tight tolerances |
| RTM | 6 | Closed mold, injection pump | Two-sided finish, medium volume |

## Key Milestones

1. **Chemistry stage**: E-glass production (furnace + platinum bushings). Hand layup
   and spray-up with polyester resin. Basic fiberglass tanks, panels,
   enclosures.
2. **Chemistry-Vacuum Optics stages**: S-glass production. Epoxy and vinyl ester resins. Vacuum
   bagging for improved laminate quality.
3. **Vacuum & Optics stage**: Filament winding for cylinders. RTM for repeatability.
   Pultrusion for profiles.
4. **Silicon**: Carbon fiber (PAN or pitch route). Aramid/Kevlar. Compression
   molding at scale. Hybrid composites combining fiber types.

## Safety & Hazards

- **Fiberglass dust**: Glass fiber fragments from cutting, sanding, or trimming are skin and respiratory irritants. Fine airborne fibers cause itching, rash, and long-term respiratory damage with chronic exposure. Wear gloves and long sleeves when handling fiberglass. Use a NIOSH-approved respirator (N95 minimum, P100 preferred) when cutting, sanding, or grinding cured fiberglass composites. Clean up dust with HEPA vacuum — never dry-sweep, which resuspends fibers.
- **Styrene from polyester resin**: The reactive diluent in unsaturated polyester resin (30-40% by weight). Styrene vapor is a central nervous system depressant (dizziness, headache, nausea at 100 ppm) and a possible human carcinogen (IARC Group 2A). Room-temperature layup with open molds produces significant styrene emissions. Use local exhaust ventilation at the work surface. Wear respiratory protection (organic vapor cartridge) during layup and until resin gels. Keep ignition sources away — styrene is flammable (flash point 31°C).
- **Epoxy sensitization**: Uncured epoxy resin and amine hardeners cause allergic contact dermatitis after repeated skin exposure. Once sensitized, the allergy is permanent. Wear nitrile gloves and change them immediately if contaminated with resin. Minimize all skin contact with uncured materials.
- **Carbon fiber dust**: Electrically conductive — airborne carbon fiber dust can short-circuit electronic equipment, including control systems and computers in the workshop. Also a respiratory irritant and potential lung hazard. Use respiratory protection when machining carbon fiber composites. Isolate carbon fiber cutting/sanding from electronic equipment. Clean with HEPA vacuum. Use sealed enclosures for CNC machining of carbon fiber parts.


## Cross-Domain Dependencies

- Fiber from [Glass Fibers](../glass/fibers.md) or [Textile Fibers](../textiles/fibers.md). Matrix from [Thermosets](../polymers/thermosets.md) or [Thermoplastics](../polymers/thermoplastics.md). [Coatings](../chemistry/coatings.md) for gel coat.

## See Also

- [Glass Fibers](../glass/fibers.md) — fiberglass reinforcement
- [Thermosets](thermosets.md) — epoxy and polyester matrix resins
- [Thermoplastics](thermoplastics.md) — thermoplastic matrix composites
- [Rubber](rubber.md) — elastomeric materials
- [Synthetic Polymers](synthetic.md) — polymer chemistry fundamentals
- [Coatings](../chemistry/coatings.md) — gel coats and protective finishes

[← Back to Polymers](index.md)
