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

### Safety & Hazards

- **Kiln temperatures (1450°C)**: Severe thermal burns. Insulated clothing, face shield, heat-resistant gloves.
- **Silica dust**: Raw material crushing generates crystalline silica dust causing silicosis. Respirators, wet methods.
- **Wet cement (pH 12-13)**: Caustic burns with prolonged skin contact. Waterproof gloves, eye protection. Wash immediately.
- **Lime (CaO)**: Reacts exothermically with moisture including sweat. Handle with gloves.

---

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
