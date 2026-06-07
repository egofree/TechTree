# Nitroglycerin & Dynamite

> **Node ID**: chemistry.explosives.nitroglycerin-dynamite
> **Domain**: [Chemistry](./index.md)
> **Parent**: [Explosives & Propellants](explosives.md)
> **Dependencies**: [`chemistry.acids`](acids.md), [`chemistry.soap`](soap.md)
> **Enables**: Construction blasting, tunneling, double-base propellants
> **Timeline**: Years 10-20
> **Outputs**: nitroglycerin, dynamite
> **Critical**: No


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
- [Blasting caps](detonation-blasting.md) for initiation

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

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [Explosives & Propellants](explosives.md)*
