# Cement & Concrete

> **Node ID**: chemistry.cement
> **Domain**: Chemistry
> **Timeline**: Years 20-35
> **Outputs**: cement, concrete, reinforced_concrete

### Portland Cement Manufacture

**Raw materials**:
- **Limestone** (CaCO₃): 60-65% of raw mix. Provides CaO. Mine, crush to <20 mm.
- **Clay** or shale: 35-40%. Provides SiO₂ (silica), Al₂O₃ (alumina), Fe₂O₃ (iron oxide). Dug, dried, crushed.
- **Corrective additives**: Bauxite (boost Al₂O₃) or iron ore (boost Fe₂O₃) if clay composition is deficient.

**Process**:
1. **Raw grinding**: Crush limestone and clay together in ball mill to <75 μm powder (raw meal). Dry grinding or wet grinding (slurry). Proportion raw materials to target: 65% CaO, 21% SiO₂, 6% Al₂O₃, 3% Fe₂O₃ by mass.
2. **Preheater**: Hot kiln exhaust gases heat raw meal in cyclone preheater to 800-900°C. Partial calcination: CaCO₃ → CaO + CO₂ (decomposition begins at ~600°C, completes by 900°C).
3. **Rotary kiln**: Steel tube 30-60 m long, 2-4 m diameter, lined with refractory brick (magnesia or high-alumina). Rotates at 1-3 RPM, inclined 3-4°. Material moves counter to hot gas flow. Peak temperature **1450°C** in the burning zone. Fuel: coal, natural gas, or oil — 3-5 kg fuel per kg cement.
4. **Clinker formation**: At 1250-1450°C, raw materials undergo solid-state reactions producing nodules (1-30 mm) of four mineral phases:
   - **Alite** (Ca₃SiO₅ / C₃S): 45-65%. Main strength contributor. Hydrates rapidly.
   - **Belite** (Ca₂SiO₄ / C₂S): 15-30%. Hydrates slowly, contributes long-term strength.
   - **Aluminate** (Ca₃Al₂O₆ / C₃A): 8-12%. Causes flash set if uncontrolled. Hydrates fastest.
   - **Ferrite** (Ca₄Al₂Fe₂O₁₀ / C₄AF): 6-10%. Moderate hydration rate. Provides gray color.
5. **Cooling**: Rapid air quench from 1450°C to <100°C. Preserves reactive crystal forms. Hot cooling air returns to kiln (recovers heat).
6. **Finish grinding**: Grind clinker with **2-5% gypsum** (CaSO₄·2H₂O) in ball mill to Blaine fineness 300-400 m²/kg. Gypsum controls setting time — without it, C₃A hydrates instantly ("flash set") and the concrete is unworkable.

### Concrete Production

**Mix design** (by volume, typical structural concrete):
- **Cement**: 1 part
- **Fine aggregate** (sand, 0-5 mm): 2 parts
- **Coarse aggregate** (gravel/crushed stone, 5-25 mm): 4 parts
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

### Reinforced Concrete

Concrete excels in compression but fails in tension at only 2-5 MPa (roughly 10% of compressive strength). Steel rebar handles the tension.

**Rebar placement**:
- **Tensile zones**: Bottom of beams (sags under load, bottom stretches), top of cantilevers, both faces of columns (bending in any direction).
- **Cover**: Minimum 25-40 mm of concrete between rebar surface and exterior (protects steel from moisture → corrosion). 50-75 mm for foundations and marine exposure.
- **Spacing**: Minimum bar spacing = 1.5× maximum aggregate size (ensures concrete flows between bars).
- **Splicing**: Overlap bars 30-40× bar diameter for tension lap splices. Wire-tie intersections.

**Corrosion protection**: Steel in alkaline concrete (pH 12-13) forms passive oxide film — naturally protected. Carbonation (CO₂ penetration) and chloride ions (de-icing salt, seawater) destroy passivation → rust → expansion → concrete spalls. Solutions: adequate cover, dense low-permeability concrete (low water-cement ratio), epoxy-coated rebar for aggressive environments.

### Alternative Cements

**Lime mortar** (pre-Portland, simplest):
- **Manufacture**: Heat limestone (CaCO₃) to 900-1000°C in lime kiln → quicklime (CaO). Slake with water → slaked lime (Ca(OH)₂). Mix with sand at 1:2.5-3 (lime:sand by volume).
- **Setting**: Carbonation — Ca(OH)₂ slowly absorbs CO₂ from air → CaCO₃. Very slow (weeks-months to full harden). Softer than Portland cement mortar — flexible, self-healing (microcracks heal as CO₂ continues carbonating). Ideal for historic restoration and soft stone masonry.

**Pozzolanic cement** (Roman concrete):
- **Principle**: Mix slaked lime (Ca(OH)₂) with pozzolan (reactive silica — volcanic ash, diatomaceous earth, calcined clay). Silica reacts with lime + water → calcium silicate hydrate (same binding gel as Portland cement). Sets underwater — hydraulic cement.
- **Roman concrete**: Lime + volcanic ash (pozzolana from Pozzuoli, Italy) + aggregate. Pumice for lightweight. Structures still standing after 2000 years (Pantheon dome, aqueducts). Seawater exposure actually strengthens it (alkali-silica reaction forms additional C-A-S-H gel).
- **Modern pozzolans**: Fly ash (coal combustion), silica fume, metakaolin (calcined kaolin clay at 600-800°C). Replace 15-40% of Portland cement — reduces cost, heat of hydration, and improves long-term durability.

**Alumina cement** (calcium aluminate cement):
- Bauxite + limestone, fused at 1400-1600°C. Primarily monocalcium aluminate (CaO·Al₂O₃). Sets rapidly (2-6 hours), high early strength. Heat-resistant — service to 1600°C with alumina aggregate. Used for refractory castables and emergency repairs.

### Concrete Properties

| Property | Typical Range | Notes |
|----------|--------------|-------|
| Compressive strength | 20-50 MPa (28 days) | 100+ MPa achievable with special mixes |
| Tensile strength | 2-5 MPa | ~10% of compressive — steel rebar compensates |
| Elastic modulus | 25-35 GPa | Stiff but not brittle at service loads |
| Thermal expansion | 10-13 × 10⁻⁶/°C | Similar to steel (critical for reinforced concrete compatibility) |
| Density | 2300-2500 kg/m³ | Normal-weight concrete |
| Thermal conductivity | 1.0-1.8 W/(m·K) | Moderate — provides fire resistance (2-4 hour rating for structural members) |
| Shrinkage | 0.03-0.08% | Occurs over months as concrete dries. Reinforcement controls cracking |

### Key Applications

- **Factory foundations**: Heavy machine tools require massive, vibration-damping pads (1-3 m thick). Low water-cement ratio (0.45) for strength and minimal shrinkage.
- **Dams**: Gravity dams rely on mass concrete (millions of cubic meters). Low heat of hydration mixes (high pozzolan content) prevent thermal cracking.
- **Roads and runways**: Pavement-quality concrete (35-40 MPa), air-entrained (4-6% microscopic air bubbles) for freeze-thaw resistance.
- **Chemical plant flooring**: Acid-resistant concrete (use calcium aluminate cement + acid-resistant aggregate).
- **Vibration isolation**: Inertia blocks for precision equipment (silicon wafer processing stages, precision grinders). Heavy concrete masses on isolation pads.

### Raw Material Preparation

**Limestone quarrying**: Open-pit mining of high-calcium limestone (CaCO₃ >90%). Drill and blast, then load into trucks with excavators. Primary crushing to <150 mm (jaw crusher), secondary crushing to <25 mm (hammer or cone crusher). Typical limestone consumption: 1.3-1.5 tonnes per tonne of clinker.

**Clay/shale extraction**: Clay provides silica (SiO₂), alumina (Al₂O₃), and iron oxide (Fe₂O₃). Dug from nearby clay pits, crushed to <50 mm. Alternative raw materials: bauxite (alumina source), iron ore (Fe₂O₃), sand (silica) — added to adjust chemistry.

**Proportioning and grinding**: Raw materials weighed and mixed in correct proportions to achieve target clinker chemistry: CaO 60-67%, SiO₂ 17-25%, Al₂O₃ 3-8%, Fe₂O₃ 0.5-6%. The four main clinker phases are: C₃S (alite, 45-65%), C₂S (belite, 15-30%), C₃A (tricalcium aluminate, 6-14%), C₄AF (tetracalcium aluminoferrite, 6-10%). Raw mix ground in ball mill or vertical roller mill to fineness of 10-15% residue on 90 µm sieve (Blaine surface area 300-400 m²/kg). In the dry process, grinding produces raw meal (fine powder). In the wet process (older), water is added to form slurry (30-40% moisture).

**Homogenization**: Raw meal stored in silos with air-fluidized mixing to ensure chemical uniformity. Variations in CaCO₃ content cause kiln instability and clinker quality problems.

### Rotary Kiln Detail

**Kiln design**: The heart of cement production. A steel tube 50-80 m long, 3-5 m diameter, lined with refractory brick, rotating at 1-4 RPM (supported on rollers at 2-3 points), inclined 3-4° from horizontal. Feed enters the upper (cold) end, flame and combustion gases enter the lower (hot) end. Material moves through by gravity and rotation.

**Wet vs dry process**: Wet process pumps slurry (30-40% water) into kiln — simpler raw material handling but wastes 30-40% of fuel energy evaporating water. Dry process uses preheater tower (4-6 stages of cyclone heat exchangers): hot kiln exhaust gases preheat raw meal to 800°C before it enters the kiln, reducing fuel consumption 30-40%. Modern plants are all dry process with preheater + precalciner.

**Temperature zones** (material traveling from cold to hot end):
1. **Drying zone** (100-200°C): Residual moisture evaporates (dry process: minimal; wet process: 30-40% water removed).
2. **Preheating** (200-800°C): In preheater tower, not in kiln itself (dry process). Raw meal heated by countercurrent exhaust gases.
3. **Calcination zone** (800-1000°C): CaCO₃ → CaO + CO₂. This is the most energy-intensive step (ΔH = +178 kJ/mol). In modern precalciner kilns, 60-90% of calcination occurs in a separate vessel (precalciner) between preheater and kiln, burning additional fuel. This dramatically reduces kiln thermal load.
4. **Burning zone / sintering zone** (1400-1500°C): CaO reacts with SiO₂, Al₂O₃, Fe₂O₃ to form clinker minerals (C₃S, C₂S, C₃A, C₄AF). Material becomes partially liquid (20-30% melt) — nodules form by agglomeration. Residence time in burning zone: 10-20 minutes. Temperature controlled by fuel rate and raw meal feed rate.
5. **Cooling zone**: Clinker exits kiln at ~1300°C into a clinker cooler (grate cooler — ambient air blows upward through falling clinker bed). Clinker cooled to 100-200°C in 20-30 minutes. The heated air (800-1000°C) is recovered as combustion air for the kiln burner — essential for fuel efficiency.

**Fuel options**: Coal (pulverized, most common globally), natural gas, heavy fuel oil, petroleum coke, waste tires, municipal solid waste-derived fuel. Fuel consumption: 3.0-3.5 GJ/tonne clinker (modern dry process), 5.0-6.5 GJ/tonne (wet process). Kiln burner: 40-120 MW thermal input for a 3000 tonnes/day kiln.

### Clinker Grinding

Clinker is cooled, stored, then ground with 3-5% gypsum (CaSO₄·2H₂O) in a cement mill (ball mill or vertical roller mill). Gypsum controls setting time — without it, C₃A reacts rapidly with water, causing flash set (concrete hardens in minutes instead of hours). Grinding to Blaine fineness 300-400 m²/kg (ordinary Portland cement). Finer grinding (500+ m²/kg) produces rapid-hardening cement. Particle size distribution: 1-100 µm, median ~15 µm. Energy: 30-50 kWh/tonne cement.

### Concrete Technology

**Admixtures** (chemical additives mixed into concrete to modify properties):
- **Plasticizers** (water reducers): Lignosulfonates or polycarboxylate ethers. Reduce water content 5-15% while maintaining workability → higher strength (lower water/cement ratio).
- **Superplasticizers** (high-range water reducers): Polycarboxylate ethers. Reduce water 20-40%. Enable self-compacting concrete (flows without vibration).
- **Accelerators**: Calcium chloride (CaCl₂) or calcium nitrate — speed up setting and early strength gain. Used in cold weather concreting.
- **Retarders**: Sucrose, citric acid, or lignosulfonates — slow setting for hot weather or long transport times.
- **Air-entraining agents**: Vinsol resin or synthetic surfactants — introduce 4-8% microscopic air bubbles. Critical for freeze-thaw resistance in cold climates.

**Curing**: Concrete gains strength by hydration of clinker minerals with water. C₃S + H₂O → C-S-H gel (calcium silicate hydrate — the binding phase) + Ca(OH)₂. Proper curing requires moisture retention for 7-28 days. Methods: water ponding, wet burlap, plastic sheeting, or spray-on curing compounds. Compressive strength development: 40% at 3 days, 65% at 7 days, 100% at 28 days (for OPC).

**Mix design**: Typical 25 MPa concrete: 350 kg cement, 180 kg water (w/c = 0.51), 700 kg fine aggregate (sand), 1100 kg coarse aggregate (gravel) per m³. Higher strength (50 MPa): reduce w/c to 0.35-0.40, increase cement to 400-450 kg/m³, use superplasticizer.

### Specialty Cements

- **Oil-well cement**: Retarded setting (downhole temperatures 50-200°C, pressures up to 100 MPa). Class G or H cement with retarders (lignosulfonate, cellulose derivatives).
- **White cement**: Made from pure white limestone and kaolin clay (low Fe₂O₃ <0.4%). Fired with natural gas or oil (no coal ash contamination). 3× cost of OPC. Architectural applications.
- **Rapid-hardening cement**: Finer grinding (Blaine 500+ m²/kg), higher C₃S content. Reaches 28-day strength in 3 days. For emergency repairs, precast concrete.
- **Sulfate-resistant cement**: Low C₃A content (<5%). Resists sulfate attack from groundwater and seawater. For foundations in sulfate-bearing soils.
- **Low-heat cement**: High C₂S, low C₃S and C₃A. Slower hydration generates less heat — prevents thermal cracking in mass concrete pours (dams, large foundations).

### Construction Applications

- **Foundations**: Machine pads (vibrate-isolated, precision-leveled), building footings, bridge abutments.
- **Dams**: Mass concrete (low-heat cement, aggregate cooling with ice water, post-cooling with embedded water pipes to control thermal cracking). Hoover Dam: 3.25 million m³ concrete.
- **Roads**: Rigid pavement — 200-300 mm slab on prepared subbase. Joints at 3-5 m intervals for thermal expansion.
- **Tanks and pipes**: Water tanks, sewage digesters, pressure pipes — often prestressed concrete (steel tendons under tension compress the concrete, preventing cracking under internal pressure).
- **Reinforced concrete**: Steel rebar embedded in concrete provides tensile strength (concrete alone has ~10× higher compressive than tensile strength). Rebar: 10-40 mm diameter deformed bars, yield strength 400-500 MPa. Cover depth: 25-50 mm (protects steel from corrosion).

### Environmental Impact

Cement production is responsible for ~8% of global CO₂ emissions. Sources: calcination (CaCO₃ → CaO + CO₂) produces ~50% of emissions (process-inherent, cannot be eliminated without alternative chemistry). Fuel combustion: ~40%. Electricity: ~10%. Mitigation strategies: (1) clinker substitution with fly ash (coal power plant waste), slag (steel mill waste), or limestone filler — reduces clinker factor from 0.95 to 0.60-0.70. (2) Alternative fuels (waste-derived). (3) Carbon capture and storage (CCS) on kiln exhaust — technically feasible but not yet economic. (4) Alternative cements (geopolymers, calcium sulfoaluminate) — lower temperature processing.

### Safety & Hazards

- **Kiln temperatures (1450°C)**: Severe thermal burns. Insulated clothing, face shield, heat-resistant gloves.
- **Silica dust**: Raw material crushing generates crystalline silica dust causing silicosis. Respirators, wet methods.
- **Wet cement (pH 12-13)**: Caustic burns with prolonged skin contact. Waterproof gloves, eye protection. Wash immediately.
- **Lime (CaO)**: Reacts exothermically with moisture including sweat. Handle with gloves.

---

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
