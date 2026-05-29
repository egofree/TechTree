# Cement & Concrete

> **Node ID**: chemistry.cement
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`ceramics.kilns`](../ceramics/kilns.md), [`mining.processing`](../mining/processing.md)
> **Enables**: [`construction.foundation`](../construction/index.md), [`machine-tools.machining`](../machine-tools/machining.md)
> **Timeline**: Years 20-35
> **Outputs**: cement, concrete, reinforced_concrete
> **Critical**: Yes — Portland cement is the second most consumed material on Earth after water. Reinforced concrete is the structural backbone of all industrial infrastructure: factory foundations, dams, roads, chemical plants, and semiconductor fabs.

## Portland Cement Manufacture

**Raw materials**:
- **[Limestone](../glossary/limestone.md)** (CaCO₃): 60-65% of raw mix. Provides CaO. Mine, crush to <20 mm.
- **[Clay](../glossary/clay.md)** or shale: 35-40%. Provides SiO₂ (silica), Al₂O₃ (alumina), Fe₂O₃ (iron oxide). Dug, dried, crushed.
- **Corrective additives**: Bauxite (boost Al₂O₃) or iron ore (boost Fe₂O₃) if clay composition is deficient.

**Process**:
1. **Raw grinding**: Crush limestone and clay together in ball mill to <75 μm powder (raw meal). Dry grinding or wet grinding (slurry). Proportion raw materials to target: 65% CaO, 21% SiO₂, 6% Al₂O₃, 3% Fe₂O₃ by mass.
2. **Preheater**: Hot kiln exhaust gases heat raw meal in cyclone preheater to 800-900°C. Partial calcination: CaCO₃ → CaO + CO₂ (decomposition begins at ~600°C, completes by 900°C).
3. **Rotary kiln**: Steel tube 30-60 m long, 2-4 m diameter, lined with refractory brick (magnesia or high-alumina). Rotates at 1-3 RPM, inclined 3-4°. Material moves counter to hot gas flow. Peak temperature **1450°C** in the burning zone. Fuel: coal, natural gas, or oil — 3-5 kg fuel per kg cement.
4. **Clinker formation**: At 1250-1450°C, raw materials undergo solid-state reactions producing nodules (1-30 mm) of four mineral phases:
   - **[Alite](../glossary/alite.md)** (Ca₃SiO₅ / C₃S): 45-65%. Main strength contributor. Hydrates rapidly.
   - **[Belite](../glossary/belite.md)** (Ca₂SiO₄ / C₂S): 15-30%. Hydrates slowly, contributes long-term strength.
   - **[Aluminate](../glossary/aluminate.md)** (Ca₃Al₂O₆ / C₃A): 8-12%. Causes flash set if uncontrolled. Hydrates fastest.
   - **[Ferrite](../glossary/ferrite.md)** (Ca₄Al₂Fe₂O₁₀ / C₄AF): 6-10%. Moderate hydration rate. Provides gray color.
5. **Cooling**: Rapid air quench from 1450°C to <100°C. Preserves reactive crystal forms. Hot cooling air returns to kiln (recovers heat).
6. **Finish grinding**: Grind clinker with **2-5% gypsum** (CaSO₄·2H₂O) in ball mill to Blaine fineness 300-400 m²/kg. Gypsum controls setting time — without it, C₃A hydrates instantly ("flash set") and the concrete is unworkable.

**Strengths**: Produces the most versatile construction material known; raw materials (limestone, clay) are abundant worldwide; 28-day compressive strength of 20-50 MPa exceeds most natural stone; compatible with steel reinforcement; fire-resistant (2-4 hour rating); low maintenance after curing.

**Weaknesses**: Extremely energy-intensive (3-5 GJ/t clinker, 1450°C kiln); responsible for ~8% of global CO₂ emissions; heavy and bulky — transport beyond 200-300 km is uneconomical; quality requires precise raw material proportioning and kiln temperature control; water/cement ratio must be tightly controlled for structural strength.

## Concrete Production

**[Mix design](../glossary/mix-design.md)** (by volume, typical structural concrete):
- **Cement**: 1 part
- **[Fine aggregate](../glossary/fine-aggregate.md)** (sand, 0-5 mm): 2 parts
- **[Coarse aggregate](../glossary/coarse-aggregate.md)** (gravel/crushed stone, 5-25 mm): 4 parts
- **Water**: water-cement ratio 0.4-0.7 by mass (lower = stronger but less workable; 0.45-0.55 for structural work)

**Water-cement ratio effects**:
- 0.40: High-strength (50+ MPa), stiff mix, may require plasticizers
- 0.50: Standard structural (30-40 MPa), good workability
- 0.60: Moderate strength (20-25 MPa), very workable
- 0.70+: Low strength (<15 MPa), porous — use only for non-structural fill

**Hydration reaction**: Cement minerals + water → calcium silicate hydrate (C-S-H) gel (the binding matrix) + calcium hydroxide (Ca(OH)₂). Heat of hydration raises concrete temperature significantly — critical for mass pours (dams, foundations). Roughly 25-35% water by weight of cement is consumed chemically; excess water creates capillary pores that reduce strength.

**Curing protocol**:
- **Initial set**: 2-4 hours after mixing. Concrete stiffens but has no strength.
- **Final set**: 6-8 hours. Can support light loads.
- **Early strength**: 1 day ≈ 20-30% of final. 7 days ≈ 65-70%. **28 days = design strength** (20-50 MPa depending on mix).
- **Moist curing is critical**: Keep concrete wet (cover with damp burlap, pond with water, or seal with plastic sheet) for minimum 7 days. Early drying causes capillary pores to empty → microcracks → dramatic strength loss (30-50% reduction). Concrete continues gaining strength for months/years if moisture is present.

## Reinforced Concrete

Concrete excels in compression but fails in tension at only 2-5 MPa (roughly 10% of compressive strength). Steel rebar handles the tension.

**Rebar placement**:
- **Tensile zones**: Bottom of beams (sags under load, bottom stretches), top of cantilevers, both faces of columns (bending in any direction).
- **Cover**: Minimum 25-40 mm of concrete between rebar surface and exterior (protects steel from moisture → corrosion). 50-75 mm for foundations and marine exposure.
- **Spacing**: Minimum bar spacing = 1.5× maximum aggregate size (ensures concrete flows between bars).
- **Splicing**: Overlap bars 30-40× bar diameter for tension lap splices. Wire-tie intersections.

**Corrosion protection**: Steel in alkaline concrete (pH 12-13) forms passive oxide film — naturally protected. Carbonation (CO₂ penetration) and chloride ions (de-icing salt, seawater) destroy passivation → rust → expansion → concrete spalls. Solutions: adequate cover, dense low-permeability concrete (low water-cement ratio), epoxy-coated rebar for aggressive environments.

## Alternative Cements

**[Lime mortar](../glossary/lime-mortar.md)** (pre-Portland, simplest):
- **Manufacture**: Heat limestone (CaCO₃) to 900-1000°C in lime kiln → quicklime (CaO). Slake with water → slaked lime (Ca(OH)₂). Mix with sand at 1:2.5-3 (lime:sand by volume).
- **Setting**: Carbonation — Ca(OH)₂ slowly absorbs CO₂ from air → CaCO₃. Very slow (weeks-months to full harden). Softer than Portland cement mortar — flexible, self-healing (microcracks heal as CO₂ continues carbonating). Ideal for historic restoration and soft stone masonry.

**Strengths**: Simplest possible cement technology (limestone + fire + water); self-healing microcracks through continued carbonation; flexible — accommodates building movement without cracking; breathable — allows moisture to escape from walls; ideal for soft stone and historic masonry.

**Weaknesses**: Very slow setting (weeks-months vs. hours for Portland); low compressive strength (1-5 MPa vs. 20-50 MPa); not suitable for structural concrete or reinforced concrete; requires CO₂ from air — cannot set underwater or in thick masses.

**[Pozzolanic cement](../glossary/pozzolanic-cement.md)** (Roman concrete):
- **Principle**: Mix slaked lime (Ca(OH)₂) with pozzolan (reactive silica — volcanic ash, diatomaceous earth, calcined clay). Silica reacts with lime + water → calcium silicate hydrate (same binding gel as Portland cement). Sets underwater — hydraulic cement.
- **Roman concrete**: Lime + volcanic ash (pozzolana from Pozzuoli, Italy) + aggregate. Pumice for lightweight. Structures still standing after 2000 years (Pantheon dome, aqueducts). Seawater exposure actually strengthens it (alkali-silica reaction forms additional C-A-S-H gel).
- **Modern pozzolans**: Fly ash (coal combustion), silica fume, metakaolin (calcined kaolin clay at 600-800°C). Replace 15-40% of Portland cement — reduces cost, heat of hydration, and improves long-term durability.

**Strengths**: Sets underwater (hydraulic cement) — enables marine and foundation construction; Roman concrete structures still standing after 2000 years; seawater exposure actually strengthens it; fly ash and slag pozzolans reduce Portland cement consumption 15-40%.

**Weaknesses**: Requires reactive silica source (volcanic ash deposits are geographically limited); slower early strength gain than pure Portland cement; fly ash supply depends on coal power plants; quality varies with pozzolan source.

**[Alumina cement](../glossary/alumina-cement.md)** (calcium aluminate cement):
- Bauxite + limestone, fused at 1400-1600°C. Primarily monocalcium aluminate (CaO·Al₂O₃). Sets rapidly (2-6 hours), high early strength. Heat-resistant — service to 1600°C with alumina aggregate. Used for refractory castables and emergency repairs.

**Strengths**: Rapid setting (2-6 hours) with high early strength; heat-resistant to 1600°C with alumina aggregate — ideal for refractory castables; useful for emergency concrete repairs; resistant to sulfate attack and acidic environments.

**Weaknesses**: Much more expensive than Portland cement (bauxite feedstock); loss of strength over time ("conversion" of hydrated phases) in warm, humid conditions; requires higher kiln temperature (1400-1600°C vs. 1450°C); limited to specialty applications due to cost and long-term durability concerns.

## Concrete Properties

| Property | Typical Range | Notes |
|----------|--------------|-------|
| Compressive strength | 20-50 MPa (28 days) | 100+ MPa achievable with special mixes |
| Tensile strength | 2-5 MPa | ~10% of compressive — steel rebar compensates |
| Elastic modulus | 25-35 GPa | Stiff but not brittle at service loads |
| Thermal expansion | 10-13 × 10⁻⁶/°C | Similar to steel (critical for reinforced concrete compatibility) |
| Density | 2300-2500 kg/m³ | Normal-weight concrete |
| Thermal conductivity | 1.0-1.8 W/(m·K) | Moderate — provides fire resistance (2-4 hour rating for structural members) |
| Shrinkage | 0.03-0.08% | Occurs over months as concrete dries. Reinforcement controls cracking |

## Key Applications

- **Factory foundations**: Heavy machine tools require massive, vibration-damping pads (1-3 m thick). Low water-cement ratio (0.45) for strength and minimal shrinkage.
- **Dams**: Gravity dams rely on mass concrete (millions of cubic meters). Low heat of hydration mixes (high pozzolan content) prevent thermal cracking.
- **Roads and runways**: Pavement-quality concrete (35-40 MPa), air-entrained (4-6% microscopic air bubbles) for freeze-thaw resistance.
- **Chemical plant flooring**: Acid-resistant concrete (use calcium aluminate cement + acid-resistant aggregate).
- **Vibration isolation**: Inertia blocks for precision equipment (silicon wafer processing stages, precision grinders). Heavy concrete masses on isolation pads.

## Raw Material Preparation

**Limestone quarrying**: Open-pit mining of high-calcium limestone (CaCO₃ >90%). Drill and blast, then load into trucks with excavators. Primary crushing to <150 mm (jaw crusher), secondary crushing to <25 mm (hammer or cone crusher). Typical limestone consumption: 1.3-1.5 tonnes per tonne of clinker.

**Clay/shale extraction**: Clay provides silica (SiO₂), alumina (Al₂O₃), and iron oxide (Fe₂O₃). Dug from nearby clay pits, crushed to <50 mm. Alternative raw materials: bauxite (alumina source), iron ore (Fe₂O₃), sand (silica) — added to adjust chemistry.

**Proportioning and grinding**: Raw materials weighed and mixed in correct proportions to achieve target clinker chemistry: CaO 60-67%, SiO₂ 17-25%, Al₂O₃ 3-8%, Fe₂O₃ 0.5-6%. The four main clinker phases are: C₃S (alite, 45-65%), C₂S (belite, 15-30%), C₃A (tricalcium aluminate, 6-14%), C₄AF (tetracalcium aluminoferrite, 6-10%). Raw mix ground in ball mill or vertical roller mill to fineness of 10-15% residue on 90 µm sieve (Blaine surface area 300-400 m²/kg). In the dry process, grinding produces raw meal (fine powder). In the wet process (older), water is added to form slurry (30-40% moisture).

**Homogenization**: Raw meal stored in silos with air-fluidized mixing to ensure chemical uniformity. Variations in CaCO₃ content cause kiln instability and clinker quality problems.

## Rotary Kiln Detail

**Kiln design**: The heart of cement production. A steel tube 50-80 m long, 3-5 m diameter, lined with refractory brick, rotating at 1-4 RPM (supported on rollers at 2-3 points), inclined 3-4° from horizontal. Feed enters the upper (cold) end, flame and combustion gases enter the lower (hot) end. Material moves through by gravity and rotation.

**Wet vs dry process**: Wet process pumps slurry (30-40% water) into kiln — simpler raw material handling but wastes 30-40% of fuel energy evaporating water. Dry process uses preheater tower (4-6 stages of cyclone heat exchangers): hot kiln exhaust gases preheat raw meal to 800°C before it enters the kiln, reducing fuel consumption 30-40%. Modern plants are all dry process with preheater + precalciner.

**[Temperature zones](../glossary/temperature-zones.md)** (material traveling from cold to hot end):
1. **[Drying zone](../glossary/drying-zone.md)** (100-200°C): Residual moisture evaporates (dry process: minimal; wet process: 30-40% water removed).
2. **[Preheating](../glossary/preheating.md)** (200-800°C): In preheater tower, not in kiln itself (dry process). Raw meal heated by countercurrent exhaust gases.
3. **[Calcination zone](../glossary/calcination-zone.md)** (800-1000°C): CaCO₃ → CaO + CO₂. This is the most energy-intensive step (ΔH = +178 kJ/mol). In modern precalciner kilns, 60-90% of calcination occurs in a separate vessel (precalciner) between preheater and kiln, burning additional fuel. This dramatically reduces kiln thermal load.
4. **[Burning zone / sintering zone](../glossary/burning-zone-sintering-zone.md)** (1400-1500°C): CaO reacts with SiO₂, Al₂O₃, Fe₂O₃ to form clinker minerals (C₃S, C₂S, C₃A, C₄AF). Material becomes partially liquid (20-30% melt) — nodules form by agglomeration. Residence time in burning zone: 10-20 minutes. Temperature controlled by fuel rate and raw meal feed rate.
5. **Cooling zone**: Clinker exits kiln at ~1300°C into a clinker cooler (grate cooler — ambient air blows upward through falling clinker bed). Clinker cooled to 100-200°C in 20-30 minutes. The heated air (800-1000°C) is recovered as combustion air for the kiln burner — essential for fuel efficiency.

**Fuel options**: Coal (pulverized, most common globally), natural gas, heavy fuel oil, petroleum coke, waste tires, municipal solid waste-derived fuel. Fuel consumption: 3.0-3.5 GJ/tonne clinker (modern dry process), 5.0-6.5 GJ/tonne (wet process). Kiln burner: 40-120 MW thermal input for a 3000 tonnes/day kiln.

## Clinker Grinding

Clinker is cooled, stored, then ground with 3-5% gypsum (CaSO₄·2H₂O) in a cement mill (ball mill or vertical roller mill). Gypsum controls setting time — without it, C₃A reacts rapidly with water, causing flash set (concrete hardens in minutes instead of hours). Grinding to Blaine fineness 300-400 m²/kg (ordinary Portland cement). Finer grinding (500+ m²/kg) produces rapid-hardening cement. Particle size distribution: 1-100 µm, median ~15 µm. Energy: 30-50 kWh/tonne cement.

## Concrete Technology

**[Admixtures](../glossary/admixtures.md)** (chemical additives mixed into concrete to modify properties):
- **[Plasticizers](../glossary/plasticizers.md)** (water reducers): Lignosulfonates or polycarboxylate ethers. Reduce water content 5-15% while maintaining workability → higher strength (lower water/cement ratio).
- **[Superplasticizers](../glossary/superplasticizers.md)** (high-range water reducers): Polycarboxylate ethers. Reduce water 20-40%. Enable self-compacting concrete (flows without vibration).
- **Accelerators**: Calcium chloride (CaCl₂) or calcium nitrate — speed up setting and early strength gain. Used in cold weather concreting.
- **Retarders**: Sucrose, citric acid, or lignosulfonates — slow setting for hot weather or long transport times.
- **Air-entraining agents**: Vinsol resin or synthetic surfactants — introduce 4-8% microscopic air bubbles. Critical for freeze-thaw resistance in cold climates.

**Curing**: Concrete gains strength by hydration of clinker minerals with water. C₃S + H₂O → C-S-H gel (calcium silicate hydrate — the binding phase) + Ca(OH)₂. Proper curing requires moisture retention for 7-28 days. Methods: water ponding, wet burlap, plastic sheeting, or spray-on curing compounds. Compressive strength development: 40% at 3 days, 65% at 7 days, 100% at 28 days (for OPC).

**Mix design**: Typical 25 MPa concrete: 350 kg cement, 180 kg water (w/c = 0.51), 700 kg fine aggregate (sand), 1100 kg coarse aggregate (gravel) per m³. Higher strength (50 MPa): reduce w/c to 0.35-0.40, increase cement to 400-450 kg/m³, use superplasticizer.

## Specialty Cements

- **Oil-well cement**: Retarded setting (downhole temperatures 50-200°C, pressures up to 100 MPa). Class G or H cement with retarders (lignosulfonate, cellulose derivatives).
- **White cement**: Made from pure white limestone and kaolin clay (low Fe₂O₃ <0.4%). Fired with natural gas or oil (no coal ash contamination). 3× cost of OPC. Architectural applications.
- **Rapid-hardening cement**: Finer grinding (Blaine 500+ m²/kg), higher C₃S content. Reaches 28-day strength in 3 days. For emergency repairs, precast concrete.
- **Sulfate-resistant cement**: Low C₃A content (<5%). Resists sulfate attack from groundwater and seawater. For foundations in sulfate-bearing soils.
- **Low-heat cement**: High C₂S, low C₃S and C₃A. Slower hydration generates less heat — prevents thermal cracking in mass concrete pours (dams, large foundations).

## Construction Applications

- **Foundations**: Machine pads (vibrate-isolated, precision-leveled), building footings, bridge abutments.
- **Dams**: Mass concrete (low-heat cement, aggregate cooling with ice water, post-cooling with embedded water pipes to control thermal cracking). Hoover Dam: 3.25 million m³ concrete.
- **Roads**: Rigid pavement — 200-300 mm slab on prepared subbase. Joints at 3-5 m intervals for thermal expansion.
- **Tanks and pipes**: Water tanks, sewage digesters, pressure pipes — often prestressed concrete (steel tendons under tension compress the concrete, preventing cracking under internal pressure).
- **Reinforced concrete**: Steel rebar embedded in concrete provides tensile strength (concrete alone has ~10× higher compressive than tensile strength). Rebar: 10-40 mm diameter deformed bars, yield strength 400-500 MPa. Cover depth: 25-50 mm (protects steel from corrosion).

## Environmental Impact

Cement production is responsible for ~8% of global CO₂ emissions. Sources: calcination (CaCO₃ → CaO + CO₂) produces ~50% of emissions (process-inherent, cannot be eliminated without alternative chemistry). Fuel combustion: ~40%. Electricity: ~10%. Mitigation strategies: (1) clinker substitution with fly ash (coal power plant waste), slag (steel mill waste), or limestone filler — reduces clinker factor from 0.95 to 0.60-0.70. (2) Alternative fuels (waste-derived). (3) Carbon capture and storage (CCS) on kiln exhaust — technically feasible but not yet economic. (4) Alternative cements (geopolymers, calcium sulfoaluminate) — lower temperature processing.

## Safety & Hazards

- **Kiln temperatures (1450°C)**: Severe thermal burns. Insulated clothing, face shield, heat-resistant gloves.
- **Silica dust**: Raw material crushing generates crystalline silica dust causing silicosis. Respirators, wet methods.
- **Wet cement (pH 12-13)**: Caustic burns with prolonged skin contact. Waterproof gloves, eye protection. Wash immediately.
- **Lime (CaO)**: Reacts exothermically with moisture including sweat. Handle with gloves.

 ---


## Hydration Chemistry

The four clinker minerals hydrate at different rates and contribute to concrete strength at different ages.

**Alite (C₃S) hydration**: Ca₃SiO₅ + 5.3H₂O → 3CaO·2SiO₂·4.3H₂O (C-S-H gel) + 1.3Ca(OH)₂. This is the dominant reaction, contributing 50-60% of total heat of hydration and most early strength (1-7 days). C₃S reacts rapidly: initial set within 2-4 hours, significant strength by 1 day. The C-S-H gel is the binding matrix that gives concrete its strength. Ca(OH)₂ (portlandite) is a crystalline byproduct that occupies ~20% of the hydrated cement paste volume but contributes little to strength. Portlandite is readily soluble in soft water and reacts with atmospheric CO₂ (carbonation).

**Belite (C₂S) hydration**: Ca₂SiO₄ + 4.3H₂O → 2CaO·SiO₂·4.3H₂O (C-S-H) + Ca(OH)₂. Similar reaction products to C₃S but much slower kinetics. C₂S contributes little to early strength but dominates long-term strength gain (28 days to years). Portland cement gains strength for months and years as C₂S slowly continues hydrating, which is why concrete strength increases with age beyond 28 days.

**Aluminate (C₃A) hydration**: Ca₃Al₂O₆ + 3CaSO₄·2H₂O + 26H₂O → 3CaO·Al₂O₃·3CaSO₄·32H₂O (ettringite). Without gypsum, C₃A reacts almost instantaneously with water, causing "flash set" (irreversible stiffening within minutes, making the concrete unworkable). Gypsum (CaSO₄·2H₂O) controls C₃A hydration by forming a protective ettringite layer around C₃A particles that slows further reaction. When gypsum is consumed (typically after 1-2 hours), the ettringite layer converts to monosulfoaluminate, and remaining C₃A hydrates directly. This conversion can cause delayed ettringite formation (DEF) in concrete exposed to high early temperatures (>70°C), a durability concern in precast and steam-cured concrete.

**Heat of hydration**: Type I (ordinary Portland cement) generates 350-500 kJ/kg total heat over 7 days. This heat is beneficial in cold weather (prevents freezing) but problematic in mass concrete (dams, large foundations) where temperature differentials between the hot interior and cool exterior cause thermal cracking. Type IV (low-heat cement) generates only 250-350 kJ/kg by reducing C₃S and C₃A content and increasing C₂S. Peak adiabatic temperature rise in a 2 m thick pour can reach 50-70°C above ambient for Type I cement, requiring embedded cooling pipes or ice-water mixing to control.

## Cement Testing

**Compressive strength testing**: 40×40×160 mm mortar prisms (cement + standard sand + water at 1:3:0.5 ratio by weight) cast in steel molds, cured in water at 20°C, and tested in compression at 1, 3, 7, and 28 days. Type I OPC typical strengths: 10-20 MPa at 3 days, 30-40 MPa at 7 days, 42-52 MPa at 28 days. The 28-day strength is the design strength used in all structural calculations. EN 197-1 standard requires minimum 42.5 MPa at 28 days for CEM I 42.5 class cement. Testing machine: constant loading rate 2.4 kN/s.

**Setting time (Vicat test)**: A 1 mm diameter needle penetrates a cement paste sample (500 g cement + water at standard consistency, typically 25-30% water by weight). Initial set: needle penetration ≤ 5 mm from the base plate (typically 45-120 minutes for OPC). Final set: needle makes no visible impression on the surface (typically 2-5 hours). EN 197-1 requires initial set >45 minutes. Accelerators (CaCl₂) reduce setting time; retarders (sugar, citric acid) extend it. Setting time is critical for construction logistics: concrete must be placed and finished before initial set.

**Soundness (Le Chatelier test)**: Detects excessive free lime (CaO) or magnesia (MgO) in cement that would cause delayed expansion and cracking in hardened concrete. Cement paste placed in a Le Chatelier mold, immersed in water at 20°C for 24 hours, then boiled for 3 hours. Expansion must not exceed 10 mm. Free CaO hydrates slowly (CaO + H₂O → Ca(OH)₂, volume increase ~100%) after the concrete has hardened, causing disruptive expansion.

## Special Cements

**White Portland cement**: Made from pure white limestone (CaCO₃ >97%) and kaolin clay (low Fe₂O₃, <0.4%). Fired at 1500-1600°C (higher temperature than grey OPC because the low iron content raises the liquid phase temperature). Cooled rapidly under reducing conditions (quenching with water) to prevent Fe²⁺ oxidation (which would cause grey-green discoloration). Fuel must be clean (natural gas or oil, not coal which introduces iron and carbon ash). Cost: 2-3× ordinary Portland cement. Used for architectural concrete, terrazzo flooring, and colored concrete (pigments show true colors against a white base).

**Oil well cement**: Class G or H Portland cement per API Spec 10A. Ground coarser than OPC (Blaine 260-320 m²/kg, lower surface area slows hydration). Very low C₃A content (<3%) for sulfate resistance against formation waters. Retarded with lignosulfonate or cellulose derivatives to prevent setting at downhole temperatures (50-200°C at depths of 1,000-5,000+ m) and pressures (up to 100 MPa). Thickening time (the working time before the cement becomes unpumpable) must exceed the placement time by a safety margin. After setting, the cement must develop compressive strength rapidly to support the casing.

**Expansive cement**: Forms ettringite (3CaO·Al₂O₃·3CaSO₄·32H₂O) or CaO hydration products that expand during early curing, compensating for the normal drying shrinkage of concrete. Type K expansive cement: an expansive clinker (containing free CaO, C₃A, and CaSO₄) is interground with OPC clinker and gypsum. Controlled expansion of 0.03-0.10% counteracts drying shrinkage of 0.03-0.08%, resulting in crack-free concrete with no net dimensional change. Used for water-retaining structures, industrial floors, and precast elements where dimensional stability is critical.

## Concrete Mix Design Calculations

**Absolute volume method**: The standard approach to designing a concrete mix. The sum of the absolute volumes of all components equals 1 m³ of concrete. Absolute volume = weight / (specific gravity × 1000). For a 25 MPa mix: cement 350 kg (SG 3.15, volume 0.111 m³), water 180 kg (SG 1.00, volume 0.180 m³), fine aggregate 700 kg (SG 2.65, volume 0.264 m³), coarse aggregate 1100 kg (SG 2.70, volume 0.407 m³), entrapped air 2% (0.020 m³), total = 0.982 m³ (adjust quantities to reach exactly 1.000 m³).

**Trial batch verification**: Calculate the mix design on paper, then produce a small trial batch (10-20 L) to verify workability (slump test: cone 300 mm tall × 200 mm top diameter × 100 mm base, fill in 3 layers, rod each 25 times, lift cone, measure slump. Target: 50-150 mm for most structural work), air content (pressure method: 1-6% depending on exposure), unit weight (density check: theoretical vs actual, discrepancy indicates air or batching error), and 28-day compressive strength (cast test cylinders, cure in water at 20°C, test at 7 and 28 days). Adjust water, aggregate proportions, or admixture dosages based on trial batch results before full production.

## Concrete Construction Practices

**Placement**: Concrete must be placed before initial set (typically 45-120 minutes after mixing, depending on temperature and admixtures). In hot weather (>30°C), set time shortens and workability decreases. In cold weather (<5°C), set time extends and early strength gain is slow. Pumping: concrete pumped through 100-150 mm diameter steel or rubber pipeline at 5-10 MPa pressure. Maximum horizontal distance: 300-500 m; vertical: 50-100 m. Pump mix design requires well-graded aggregate and sufficient fines (paste volume >30%) to lubricate the pipeline.

**Vibration**: Internal vibrators (poker vibrators, 25-75 mm diameter, 10,000-18,000 vibrations/min) consolidate concrete by eliminating air voids. Insert vibrator vertically, withdraw slowly (25-50 mm/s), overlap radius of influence (100-300 mm depending on vibrator size). Over-vibration causes segregation (heavy aggregate sinks, paste rises). Under-vibration leaves honeycombing (voids that weaken the structure and expose rebar to corrosion). Vibration time per insertion: 5-15 seconds. Surface vibrators (screed vibrators) used for slabs and flatwork.

**Curing methods**: Proper curing maintains moisture in the concrete during the critical first 7-28 days. Methods: (1) Water curing: ponding, spraying, or wet burlap continuously for 7 days. (2) Membrane curing: spray-on curing compound (wax or resin emulsion) that forms a vapor barrier on the surface, applied immediately after finishing. (3) Plastic sheeting: polyethylene film sealed at edges, trapping evaporation moisture. (4) Steam curing: for precast concrete, steam at 60-80°C accelerates strength gain to achieve 28-day strength in 16-24 hours (but may reduce ultimate strength by 10-15% compared to moist curing).

## Cement Testing Standards

**Blaine fineness**: Measured by air permeability (Wagner turbidimeter or Blaine apparatus). Air is drawn through a compacted bed of cement powder at controlled pressure; the time to pass a fixed volume of air is inversely proportional to specific surface area. OPC Type I: 300-500 m²/kg. Finer grinding (500+ m²/kg) produces rapid-hardening cement with higher early strength but also higher heat of hydration and faster workability loss.

**Setting time (Vicat needle)**: A 1 mm diameter needle with 300 g total load penetrates a cement paste sample at standard consistency. Initial set: penetration ≤ 5 mm from base plate. Final set: needle makes no visible impression. ASTM C150 / EN 197-1 require initial set ≥ 45 minutes and final set ≤ 375 minutes for Type I OPC. Accelerators (CaCl₂ at 1-2% by cement weight) reduce initial set to 15-30 minutes for cold weather concreting.

**Soundness (expansion testing)**: Le Chatelier method: cement paste placed in a split brass mold (indicator needles 170 mm apart), cured 24 hours in water at 20°C, then boiled 3 hours. Expansion must not exceed 10 mm. Autoclave method (ASTM C151): cement paste bars steamed at 2.0 MPa (215°C) for 3 hours; expansion must not exceed 0.8%. These tests detect excessive free lime (CaO) or periclase (MgO) that hydrate slowly in hardened concrete, causing delayed expansion and cracking months or years after placement.

## Limitations

- **CO₂ emissions**: Portland cement production releases ~0.6-0.9 tonnes CO₂ per tonne of clinker — roughly 60% from calcination (CaCO₃ → CaO + CO₂, an inherent chemical reaction) and 40% from fuel combustion. Cement production accounts for ~8% of global CO₂ emissions. Partial substitutes (fly ash, blast furnace slag, calcined clay — LC³ cement) can reduce clinker factor to 0.5-0.7, but the calcination CO₂ cannot be eliminated without fundamentally different chemistry.
- **Energy intensity**: Clinker formation requires 1,450°C kiln temperature. Total thermal energy consumption: 3.0-5.0 GJ per tonne of clinker. Electrical energy for grinding: 80-120 kWh per tonne of cement. The cement industry is one of the largest industrial energy consumers globally.
- **Weight and transport**: Cement is heavy (bulk density ~1.5 t/m³) and low value per tonne. Transport beyond 200-300 km by road becomes uneconomical. Cement plants must be located near both limestone quarries and markets, constraining siting options.
- **Alkali-silica reaction (ASR)**: Alkaline cement pore solution reacts with reactive silica in certain aggregates, forming an expansive gel that cracks concrete over years to decades. ASR is prevented by using low-alkali cement (<0.60% Na₂O equivalent) or non-reactive aggregates. Once started, ASR cannot be stopped — the concrete must be replaced.

## See Also

- **[Refractories](refractories.md)**: Kiln linings for cement manufacturing
- **[Mining](../mining/index.md)**: Limestone quarrying and raw material extraction
- **[Ceramics](../ceramics/index.md)**: Related high-temperature materials processing
- **[Lime](../ceramics/lime.md)**: Calcium oxide production, a precursor to cement chemistry
- **[Construction](../construction/index.md)**: Concrete and building applications



[← Back to Chemistry](index.md)
