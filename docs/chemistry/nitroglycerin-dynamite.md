# Nitroglycerin & Dynamite

> **Node ID**: chemistry.explosives.nitroglycerin-dynamite
> **Domain**: [Chemistry](./index.md)
> **Parent**: [Explosives & Propellants](explosives.md)
> **Dependencies**: [`chemistry.acids`](acids.md), [`chemistry.soap`](soap.md)
> **Enables**: Construction blasting, tunneling, double-base propellants
> **Timeline**: Years 10-20
> **Outputs**: nitroglycerin, dynamite
> **Critical**: No

## Prerequisites & Dependencies

Nitroglycerin and dynamite production require a specialized chemical infrastructure:

- **[Mixed acid production](acids.md)**: Concentrated nitric acid (90-98%) and sulfuric acid (96-98%). The mixed acid ratio is approximately 50:50 HNO₃:H₂SO₄ by weight. The sulfuric acid acts as a dehydrating agent, absorbing water produced during nitration and driving the reaction to completion.
- **[Glycerol](soap.md)** (99%+ purity): Primary feedstock for NG. Produced as a byproduct of fat saponification (soap making) or synthesized from propylene. Glycerol must be anhydrous (water-free) — even 1% water in the glycerol dilutes the mixed acid and reduces yield. Glycerol from soap making contains water, salt, and soap residues that must be removed by distillation before use in NG production.
- **Lead-lined steel nitrator**: NG production requires a specialized reaction vessel. Lead lining resists mixed acid corrosion. The vessel must have cooling coils (NG nitration generates ~370 kJ/mol), an agitator for uniform temperature, and a temperature-actuated emergency dump valve that discharges into a drowning tank.
- **Emergency drowning tank**: A large water-filled tank (at least 20× the nitrator volume) positioned below the nitrator. If temperature exceeds 20°C, the dump valve opens and dumps the entire batch into cold water, diluting the acid and quenching the reaction. This is the primary safety system.
- **Remote blast-resistant facility**: NG synthesis must be conducted in a separate building with reinforced concrete walls (≥30 cm), blast-resistant doors, and blast shields between the operator and the reaction vessel. The operator views the process through a periscope or thick armored glass. No personnel in the nitrator room during the reaction.
- **Diatomaceous earth (kieselguhr)**: The absorbent that makes dynamite possible. A naturally occurring siliceous sediment composed of fossilized diatom shells. Mined, dried, and ground to 10-50 μm particle size. The high porosity and surface area absorb NG into a stable, handleable solid. Alternative absorbents: sawdust, wood meal, or other porous materials.
- **[Blasting caps](detonation-blasting.md)**: Mercury fulminate or lead azide blasting caps to initiate dynamite. Nobel's first blasting cap (1867) used mercury fulminate. Modern caps use lead azide as the primary charge with PETN or RDX as the secondary charge.

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

**Applications**: Primary ingredient in dynamite. Component of double-base smokeless powder. Rarely used as a standalone explosive due to extreme sensitivity, but in the early years (1847-1867, before Nobel invented dynamite) it was used directly for blasting with predictable and frequent catastrophic results. Sobrero, who first synthesized NG in 1847, was so horrified by its sensitivity that he recommended against any practical use. Nobel's genius was not inventing NG but finding a way to make it safe to handle.

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

## Scaling Notes

Nitroglycerin and dynamite production scale from artisanal to industrial:

- **Pilot scale** (100 g NG per batch, 10-50 dynamite cartridges): A single lead-lined nitrator (5-10 L) with hand-operated agitator and ice bath cooling. Manual separation in a glass separatory funnel. Hand-mixing NG with kieselguhr in a shallow pan behind a blast shield. One highly trained operator. Production rate: 20-50 cartridges per day. This is the minimum viable scale for initial blasting operations in mining and construction.

- **Factory scale** (1-5 kg NG per batch, 500-2,500 dynamite cartridges/day): Multiple nitrators (50-200 L) with mechanical agitation, cooling jackets, and automatic dump valves. Separate washing and neutralization tanks. Mixing house for NG + kieselguhr with remote mechanical kneader. Cartridge loading machine (hand-fed press). Magazine storage with temperature control (13-25°C). 10-20 workers. This was the scale of Nobel's original dynamite factories (1867-1900).

- **Industrial scale** (50+ kg NG per batch, continuous dynamite production): Continuous NG synthesis with inline washing and neutralization. Automated mixing, extrusion, and cartridge packaging. Temperature-controlled magazine with inventory rotation. Gelatin dynamite production line (NG + nitrocotton). 50+ workers. This scale supplies a regional mining industry.

**Critical safety constraint**: NG production cannot be safely scaled beyond ~50 kg per batch regardless of facility size. The risk of accidental detonation scales with batch size. Industrial-scale NG plants use multiple small nitrators (not one large one) running in parallel, each in a separate blast-resistant bay. The Biazzi continuous process (developed in the 1920s) minimizes the quantity of NG in process at any moment to <5 kg, with continuous flow through nitration, separation, and washing stages.

## Quality Control

**Nitroglycerin quality tests**:
1. **Appearance**: Pale yellow, clear, oily liquid. Brown or dark yellow discoloration indicates decomposition products from overheating during nitration. Discolored NG should be destroyed (burned in small quantities), not used.
2. **Nitrogen content**: Should be 18.3-18.5% N by weight. Measured by Lunge nitrometer or Devarda method. Lower nitrogen indicates incomplete nitration; higher indicates residual mixed acid.
3. **Acidity test**: Shake NG with water, test the water layer with pH paper. Must be neutral (pH 6.5-7.5). Acidic NG (pH <6) is unstable and must be re-washed with sodium carbonate solution.
4. **Abel heat test**: Heat a sample at 82.2°C and measure the time until brown NO₂ fumes appear (the "induction period"). Fresh, well-washed NG: >10 minutes at 82.2°C. Below 5 minutes indicates residual acid or unstable decomposition products. This is the most important stability test for NG.

**Dynamite quality tests**:
1. **Weight consistency**: Weigh each cartridge. Tolerance: ±3% of nominal weight. Underweight cartridges have insufficient NG content; overweight may have excess NG or incomplete absorption.
2. **NG content verification**: Calculate from weigh-out records (kg NG per kg dynamite). For 60% dynamite: NG must be 59-61% by weight. Extract NG from a sample with ethanol, evaporate, and weigh the residue to verify.
3. **Drop test**: Drop a cartridge from 2 m onto a steel plate. Should not detonate. This verifies adequate desensitization by the kieselguhr absorbent. Failure indicates insufficient absorbent or poor mixing.
4. **Exudation test**: Store sample cartridges at 35°C for 7 days. Inspect for NG liquid on the surface. Any visible exudation indicates poor absorption or excess NG content. Reject the batch.
5. **Gap test for sensitivity**: Place a blasting cap against the cartridge with varying air gaps. Measure the maximum gap at which detonation transfers. Too sensitive (<5 mm gap) indicates under-absorption; too insensitive (>50 mm gap) suggests degraded NG.

## Variations and Alternatives

| Explosive | Det. Velocity (m/s) | Density (g/cm³) | Energy (MJ/kg) | Sensitivity | Water Resistant | Best For |
|-----------|---------------------|-----------------|-----------------|-------------|-----------------|----------|
| Black powder | 400-600 | 1.0-1.4 | 2.6-3.0 | Low (ignites) | No | Fuses, fireworks, primitive firearms |
| Nitroglycerin (liquid) | 7,700 | 1.59 | 6.4 | Extremely high | N/A | Never used alone; precursor for dynamite |
| Dynamite (40%) | 3,200-4,000 | 1.2-1.3 | 2.8-3.2 | Low | Poor | Soft rock, light construction blasting |
| Dynamite (60%) | 4,500-5,500 | 1.3-1.4 | 3.5-4.0 | Low | Moderate | Standard blasting, quarrying |
| Dynamite (75%+) | 5,500-6,500 | 1.4-1.5 | 4.0-4.5 | Moderate | Moderate | Hard rock, deep mining |
| Gelatin dynamite | 5,000-6,500 | 1.4-1.6 | 4.0-5.0 | Low | Excellent | Underwater blasting, wet boreholes |
| ANFO | 2,500-4,000 | 0.8-0.85 | 3.7 | Very low | No | Large-scale mining, cheapest per unit energy |
| TNT | 6,900 | 1.65 | 4.6 | Very low | Excellent | Military shells, melt-cast filling |

## See Also

- **[Explosives & Propellants](explosives.md)**: Parent overview and nitration chemistry
- **[Black Powder](explosives.black-powder.md)**: Predecessor explosive
- **[Nitrocellulose & Smokeless Powders](nitrocellulose.md)**: Propellants using NG in double-base formulations
- **[High Explosives](high-explosives.md)**: TNT, RDX, ANFO
- **[Detonation & Blasting](detonation-blasting.md)**: Blasting caps, fuses, and initiation systems
- **[Acids](acids.md)**: Nitric and sulfuric acid production
- **[Soap Making](soap.md)**: Glycerol byproduct from saponification

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Nitroglycerin turns brown or dark yellow during synthesis | Temperature exceeded 20°C during nitration, producing unstable nitrogen oxide byproducts | Maintain 10-15°C with continuous cooling; if temperature exceeds 20°C, dump batch into drowning tank immediately; do not attempt to recover overheated NG |
| NG separates poorly from spent acid | Acid:glycerol ratio too low, or insufficient settling time | Increase mixed acid ratio to 6:1 (acid:glycerol by weight); allow 30 minutes settling time; NG (density 1.59) sinks below spent acid (density ~1.7) |
| Dynamite cartridge sweats liquid NG on surface | Storage temperature above 30°C, or absorbent (kieselguhr) saturated beyond capacity | Store below 25°C; handle sweating cartridges with rubber gloves as liquid NG; destroy heavily sweating cartridges by burning in small quantities on a hot plate outdoors |
| Dynamite fails to detonate from blasting cap | Frozen dynamite (NG crystals desensitized), or cap not inserted properly into cartridge | Store above 13°C; if frozen, thaw slowly at 20-25°C (never with direct heat); insert blasting cap at least 10 cm into cartridge body; ensure cap is oriented with explosive end toward the charge |
| NG wash water still acidic after 5 washes | Insufficient sodium carbonate in neutralization wash, or NG emulsified in wash water | Increase Na₂CO₃ concentration to 5% in wash; add brine to break NG/water emulsion; continue washing until pH of wash water tests 7.0-7.5 |
| Dynamite blast produces excessive NO₂ fumes (orange-brown cloud) | NG-to-absorbent ratio too high (>80%) or incomplete detonation | Use correct grade dynamite (40-60% NG); ensure adequate confinement (stemming above charge); use strong enough blasting cap (standard #6 or #8 strength) |
| Nitration vessel temperature rises above 20°C despite cooling | Glycerol added too fast for cooling capacity, or cooling water flow insufficient | Stop glycerol addition immediately; maximize cooling water flow; if temperature exceeds 25°C, actuate emergency dump valve into drowning tank; reduce glycerol feed rate to 1 drop per 2-3 seconds |
| Dynamite cartridges crack or crumble when handled | Insufficient NG content, or absorbent (kieselguhr) too coarse | Increase NG to at least 40% by weight; use fine-grade kieselguhr (particle size 10-50 μm) that absorbs NG uniformly; reject crumbling cartridges and reprocess |
| Worker develops severe headache near dynamite operations | NG vapor inhaled or absorbed through skin; headache is early warning of exposure | Remove worker to fresh air; wash exposed skin with soap and water; remove contaminated clothing; if headache persists >6 hours, seek medical attention; monitor all workers for "NG head" as an exposure indicator |
| Blasting cap fires but dynamite does not detonate (misfire) | Cap too weak for the dynamite grade, or gap between cap and charge body | Use #8 strength cap for 60%+ dynamite; insert cap fully into cartridge (no air gap); ensure cap is in firm contact with explosive material; wait 30 minutes before approaching a suspected misfire |

## Safety & Hazards

- **NG skin absorption**: Nitroglycerin is absorbed through intact skin and by inhalation of vapor. A headache beginning 30 minutes to 2 hours after exposure is the first symptom. The headache is caused by vasodilation (NG is a potent vasodilator, used medically at microgram doses for angina). Chronic exposure causes tolerance that disappears after 2-3 days away, leading to "Monday morning headache" when workers return after a weekend. Treat by removing from exposure; symptoms resolve in 2-6 hours. Aspirin provides relief.
- **NG impact sensitivity**: Pure NG detonates from a 2 J impact (a hammer blow on a hard surface). For comparison, a 100 g hammer dropped 2 cm onto NG on an anvil delivers enough energy to initiate detonation. Never pour NG from one container to another at height. Never handle NG in glass containers (breakage risk). All NG handling tools must be wood, rubber, or brass.
- **Dynamite magazine fire**: If dynamite in storage catches fire, evacuate to at least 500 m. Do not attempt to fight the fire. Dynamite burns to detonation: the fire heats the NG above its autoignition point, and the burning mass transitions from deflagration to detonation. The transition can take seconds to minutes depending on the quantity and confinement. Call emergency services and evacuate.
- **Disposal of deteriorated dynamite**: Dynamite that has sweated heavily, frozen and thawed repeatedly, or exceeded its shelf life (typically 1-2 years for standard dynamite) must be destroyed. The safest disposal method is burning: place cartridges individually on a hot plate or metal sheet in the open, ignite with a long fuse, and retreat to 100+ m. Never burn more than one cartridge at a time. Burning produces toxic NO₂ fumes; stay upwind.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [Explosives & Propellants](explosives.md)*
