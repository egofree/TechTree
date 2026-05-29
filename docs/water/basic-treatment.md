# Basic Water Treatment

> **Node ID**: water.basic-treatment
> **Domain**: [Water](./index.md)
> **Dependencies**: [`water.procurement`](procurement.md)
> **Enables**: [`water.sem-tech-water-treatment`](sem-tech-water-treatment.md), [`health.sanitation`](../health/sanitation.md)
> **Timeline**: Years 5-25
> **Outputs**: potable_water, filtered_water
> **Critical**: Yes — waterborne diseases are among the greatest killers in pre-industrial civilizations; treatment reduces mortality by 50-80%

## 1. Overview

Purifying raw water for safe human consumption. Waterborne diseases — cholera (Vibrio cholerae), typhoid (Salmonella typhi), dysentery (Shigella spp.), and giardiasis (Giardia lamblia) — are among the greatest killers in all pre-industrial civilizations. The 1854 Broad Street cholera outbreak in London killed 616 people in two weeks from a single contaminated well. Simple treatment methods dramatically reduce disease burden and are achievable with minimal technology.

Water treatment operates on a spectrum from coarse to fine:

1. **Settling** — remove large particles by gravity (10-20 micron threshold)
2. **Filtration** — remove smaller particles and microorganisms (0.15-5 micron threshold)
3. **Disinfection** — kill or inactivate remaining pathogens (99.99%+ reduction)

Each stage is valuable on its own. The combination provides safe drinking water. This capability covers methods available from stone-age conditions through early industrial development.

## 2. Prerequisites

### Materials
- [Raw water](procurement.md) from any source
- Sand (0.15-0.35 mm effective size for slow sand filters)
- Gravel (15-30 cm graded layer)
- Concrete or ferrocement for filter tanks — from [Chemistry: Cement](../chemistry/cement.md)
- Chlorine compounds for disinfection — from [Chemistry](../chemistry/acids-bases.md)

### Tools
- Basic construction tools for tank and filter construction
- Containers for boiling and chemical storage
- Turbidity tube for water quality testing

### Knowledge
- Understanding of biological contamination pathways
- Basic chemistry for disinfection dosing

### Infrastructure
- Level ground for filter construction
- Water-tight tank or basin (1-50 m² depending on scale)

## 3. Bill of Materials

| Material | Quantity per filter (serving 200 people) | Source | Alternatives |
|----------|----------------------------------------|--------|-------------|
| Fine sand (0.15-0.35 mm) | 3-8 m³ | River or quarry | Crushed quartz, crushed limestone |
| Gravel (5-30 mm) | 0.5-1.5 m³ | River or quarry | Crushed stone |
| Concrete or ferrocement for tank | 2-5 m³ | [Chemistry: Cement](../chemistry/cement.md) | Stone or brick with waterproof lining |
| Drainage pipe (perforated) | 5-15 m | [Metals](../metals/index.md) or [Ceramics](../ceramics/index.md) | Bamboo (short-lived) |
| Chlorine (calcium hypochlorite) | 0.5-2 kg/month | [Chemistry](../chemistry/acids-bases.md) | Boiling (requires 10× fuel) |

## 4. Process Description

### Slow Sand Filtration

The most important low-technology water treatment method. Developed in Scotland in 1804, slow sand filtration produces safe drinking water with no chemicals and minimal maintenance. Used by London from 1829 to eliminate cholera from the water supply.

**Prerequisites**: Sand (0.15-0.35 mm effective size), gravel, water-tight tank or basin, [cement](../chemistry/cement.md) or stone for construction.

**Materials**: Fine sand (0.6-1.5 m depth), graded gravel (15-30 cm), concrete or ferrocement tank, perforated drainage pipe.

**Construction**:
1. Build a rectangular or circular tank from concrete, ferrocement, stone, or brick with waterproof lining. Internal dimensions: 1 m² filter area per 50-200 people served. Tank depth: 1.5-2.0 m (sand bed + water depth + freeboard).
2. Install perforated drainage pipes at the bottom of the tank. Cover with 15-30 cm of graded gravel (coarse at bottom, fine at top).
3. Fill with sand in 15 cm layers. Wash each layer to remove fines before adding the next. Target effective size 0.15-0.35 mm, uniformity coefficient 1.5-3.0.
4. Install inlet and outlet overflow weirs. Maintain 5-10 cm water above sand surface at all times — the biological layer dies if it dries out.
5. Cover the tank to prevent algae growth and contamination. Leave ventilation for gas exchange.

**Calibration**: After construction, run water through the filter at design flow rate (0.1-0.4 m/hour). The biological layer (schmutzdecke) develops over 1-4 weeks. During this ripening period, the output is not safe — continue alternative treatment. Test output turbidity weekly: target <1 NTU. Bacterial removal >95% once mature.

**Expected performance**: Removes 95-99.9% of bacteria, 99-99.99% of viruses, and nearly all protozoan parasites. Turbidity reduced to <1 NTU from input of 10-100 NTU. Flow rate: 0.1-0.4 m/hour hydraulic loading. Service life: 5-10 years between full sand replacements.

**Strengths**:
- No chemicals required
- Extremely reliable — removes pathogens without chemical dosing
- Low maintenance (periodic sand scraping every 1-3 months)
- Long service life
- Can be built with local materials

**Weaknesses**:
- Large area required (1 m² per 50-200 people)
- Slow flow rate — not suitable for high-demand intermittent use
- Biological layer takes 1-4 weeks to develop after construction or cleaning
- Cannot handle very turbid water (>50 NTU) without pre-sedimentation
- Ineffective against dissolved chemical contaminants (heavy metals, salts)

### Settling and Clarification

The simplest treatment: let water sit still so particles sink by gravity.

**Prerequisites**: Tank or basin, [raw water supply](procurement.md).

**Materials**: Excavated basin or concrete tank.

**Procedure**:
1. Fill tank or basin with raw water.
2. Allow 2-4 hours for particles larger than 10-20 microns to settle (sand, silt, some bacteria).
3. Draw clarified water from the upper portion without disturbing settled sludge.
4. Pre-sedimentation basins (4-12 hour residence time) placed before filtration reduce filter loading by 50-90%.

**Expected performance**: Removes 50-80% of suspended solids, minimal pathogen removal. Not sufficient alone — must be combined with filtration or disinfection.

**Strengths**:
- Zero technology and zero energy input
- Immediate improvement in water clarity
- Reduces load on downstream filters

**Weaknesses**:
- Does not remove dissolved contaminants or most pathogens
- Requires large tank volume relative to throughput
- Sludge accumulation requires periodic cleaning

### Boiling

The oldest and most universal disinfection method.

**Prerequisites**: Fuel (wood, charcoal, or gas), container (metal pot preferred), [heat source](../energy/index.md).

**Materials**: Fuel (0.1-0.3 kg wood per liter boiled), metal or clay pot.

**Procedure**:
1. Place water in a clean container. If water is turbid, filter through cloth first.
2. Bring to a rolling boil. At sea level, water boils at 100°C. At 2,000 m elevation, boiling point drops to approximately 93°C — boil for 3 minutes instead of 1.
3. Maintain rolling boil for 1 minute at sea level (3 minutes above 2,000 m elevation).
4. Cover and allow to cool before storing in a clean, covered container.

**Calibration**: A rolling boil is unmistakable — vigorous bubbling across the entire surface. If you cannot achieve a rolling boil (insufficient heat), maintain the highest temperature achievable for 10+ minutes.

**Expected performance**: 99.9999% pathogen kill. Kills bacteria, viruses, and protozoan cysts. Does NOT remove chemical contaminants, turbidity, or heavy metals.

**Strengths**:
- 99.9999% effective against all biological pathogens
- No special equipment — any heat source and container
- Immediate — no waiting period
- Well-understood and universally accepted

**Weaknesses**:
- High fuel cost: 0.1-0.3 kg wood per liter boiled
- Does not remove chemical contaminants or turbidity
- Recontamination risk if stored in dirty containers
- Impractical for community-scale supply (fuel consumption prohibitive)
- Time-consuming at household scale for large volumes

### Solar Disinfection (SODIS)

UV radiation and thermal energy from sunlight inactivate pathogens.

**Prerequisites**: Clear PET or glass bottles, sunlight exposure (6+ hours).

**Materials**: Clear PET bottles (1-2 L), black surface or background (optional, increases temperature).

**Procedure**:
1. Fill clear PET or glass bottles with water. If turbid (>30 NTU), filter through cloth first.
2. Lay bottles horizontally on a reflective or dark surface in direct sunlight.
3. Expose for 6+ hours in full sun, or 2 consecutive days if cloudy.
4. UV-A radiation (320-400 nm wavelength) damages pathogen DNA. Thermal effects synergize above 45°C — water in dark bottles reaches 50-60°C on sunny days.

**Expected performance**: 99.9% bacterial inactivation, 99-99.9% viral inactivation. Less effective on protozoan cysts (require higher UV dose). Requires clear bottles and relatively clear water.

**Strengths**:
- Zero fuel cost
- Minimal technology — only requires bottles
- Low effort after setup
- Effective on most bacteria and viruses

**Weaknesses**:
- Ineffective on very cloudy days or in shaded locations
- Requires clear bottles (colored or opaque bottles block UV)
- Turbid water must be pre-filtered
- Small batch size (1-2 L per bottle)
- Does not remove chemical contaminants

### Chlorination

The most widely used disinfection method worldwide since the early 1900s.

**Prerequisites**: Chlorine compound (calcium hypochlorite, sodium hypochlorite, or chlorine gas), [basic chemistry capability](../chemistry/index.md) for production.

**Materials**: Calcium hypochlorite granules (HTH, 65-70% available chlorine) or sodium hypochlorite solution (5-15% concentration), dosing equipment (measuring spoon or drip feeder), mixing tank.

**Procedure**:
1. Calculate dose based on water volume and chlorine demand. Starting dose: 1-5 mg/L free chlorine.
2. Dissolve calcium hypochlorite in a small volume of water to make a stock solution (1% = 10,000 mg/L). For sodium hypochlorite, dilute as needed.
3. Add dose to water and mix. Ensure 30 minutes contact time at pH <8. Higher pH requires longer contact or higher dose.
4. After 30 minutes, measure residual: target 0.2-0.5 mg/L free chlorine residual. If below 0.2 mg/L, increase dose. If above 0.5 mg/L, decrease dose.

**Calibration**: Use a DPD (N,N-diethyl-p-phenylenediamine) colorimetric test kit to measure free chlorine residual. The test turns the water sample pink — compare color intensity to the calibrated chart.

**Expected performance**: 99.99% bacterial kill, 99.9% viral inactivation at correct dose and contact time. Provides residual protection in distribution system (chlorine remains active for hours to days).

**Strengths**:
- Residual protection — chlorine continues to kill pathogens in storage and distribution
- Scalable from household to municipal
- Well-understood dosing and monitoring
- Relatively low cost (calcium hypochlorite: $1-3/kg)

**Weaknesses**:
- Requires chemistry capability for chlorine production or procurement
- Chlorine gas is toxic (IDLH 10 ppm) — handling requires ventilation and PPE
- Sodium hypochlorite degrades over time (50% loss in 6 months at 25°C)
- Taste and odor complaints at doses above 1 mg/L
- Forms disinfection byproducts (trihalomethanes) if organic matter is present — not a concern at early-stage development but worth monitoring

### Simple Household Filters

Intermediate methods between boiling nothing and building a slow sand filter.

**Ceramic candle filters**: Porous ceramic elements (pore size 0.5-5 microns) remove bacteria by mechanical filtration. Silver-impregnated ceramic provides additional antimicrobial action. Flow rate: 1-4 L/hour. Requires [ceramics capability](../ceramics/index.md).

**Cloth filtration**: Folded cotton cloth removes larger pathogens (guinea worm larvae, some bacteria). 4-8 layers of fine woven cloth reduce cholera bacteria by 50-99%. Effective for specific threats (guinea worm) but not general-purpose disinfection.

**Charcoal filtration**: Granular activated charcoal removes taste, odor, and some organic chemicals. Does NOT reliably remove pathogens. Useful as a polishing step after other treatment.

**Strengths**:
- Low cost and simple to use
- No energy input required
- Ceramic filters have documented 50-99% bacterial removal

**Weaknesses**:
- Flow rates are slow (1-4 L/hour for ceramic)
- Ceramic elements are fragile
- Cloth and charcoal filters do not provide reliable pathogen removal
- Requires periodic cleaning or replacement

## 5. Quantitative Parameters

| Method | Pathogen removal | Flow rate | Cost per 1000L | Energy required |
|--------|-----------------|-----------|---------------|----------------|
| Slow sand filter | 95-99.99% bacteria | 100-400 L/m²/hour | $0.01-0.05 | None (gravity) |
| Boiling | 99.9999% all | Limited by pot size | $0.50-1.50 (fuel) | 0.1-0.3 kg wood/L |
| SODIS | 99.9% bacteria | 1-2 L per bottle per day | $0.00 (after bottle) | Solar radiation |
| Chlorination | 99.99% bacteria | Unlimited | $0.01-0.05 | None (mixing only) |
| Ceramic filter | 50-99% bacteria | 1-4 L/hour | $0.10-0.50 | None (gravity) |

## 6. Scaling Notes

- **Household scale** (1-5 people): Boiling, SODIS, or ceramic candle filter. Cost: $0-10. No infrastructure needed.
- **Community scale** (50-500 people): Slow sand filter (2-10 m² filter bed) plus chlorination. Requires construction materials and basic chemistry for chlorine. Cost: $50-500.
- **Municipal scale** (5,000+ people): Rapid sand filtration with chemical coagulation plus chlorination. Requires [chemistry capability](../chemistry/index.md) for alum production. Alternatively, multiple parallel slow sand filters. Cost: $5,000-50,000.

The key scaling breakpoint is the jump from household to community scale: this requires shared infrastructure and organizational capacity for maintenance.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Slow sand filter flow rate dropping below 0.1 m/hour | Biological layer (schmutzdecke) too thick; sand clogged with sediment | Drain water. Scrape 1-2 cm of sand from the top surface. Refill with clean water. Biological layer re-establishes in 1-3 days. |
| Filtered water still turbid (>5 NTU) | Input water too turbid for filter capacity; sand too coarse; biological layer not established | Add pre-sedimentation basin before filter. Check sand grain size (target 0.15-0.35 mm). Wait for biological layer to develop (1-4 weeks). |
| Chlorine residual too high (>1 mg/L) — strong taste | Overdosing | Reduce dose by 25-50%. Re-test residual after 30 minutes. |
| Chlorine residual too low (<0.2 mg/L) | Underdosing; high chlorine demand from organic matter in water | Increase dose by 25-50%. Pre-filter water to remove organic matter. Test pH — chlorine less effective above pH 8. |
| Boiled water making people sick | Recontamination from dirty storage container | Store boiled water in clean, covered containers. Use narrow-mouth containers to prevent hand contact. Apply chlorine residual after boiling if recontamination persists. |
| SODIS not effective | Cloudy weather; turbid water; colored bottles | Filter water through cloth first. Use only clear PET or glass bottles. Increase exposure time to 2 full days during cloudy periods. |

## 8. Safety

- **Chlorine gas**: Toxic at 10 ppm IDLH (immediately dangerous to life and health). Calcium hypochlorite dust is corrosive to skin, eyes, and respiratory tract. Handle with gloves, goggles, and in a ventilated area. Store in sealed containers away from organic materials and acids — mixing chlorine with acid releases lethal chlorine gas.
- **Hot water scalds**: Boiling water at 100°C causes third-degree burns in 1 second of skin contact. Use insulated containers. Keep children away from boiling operations.
- **Alum (aluminum sulfate)**: Used as coagulant in rapid sand filtration. Mildly acidic (pH 3-4 in solution). Irritant to skin and eyes. Handle with gloves and eye protection.
- **Chemical contamination**: Boiling, filtration, and chlorination do NOT remove heavy metals (lead, arsenic, mercury), pesticides, or industrial chemicals from water. If chemical contamination is suspected, additional treatment (activated carbon, ion exchange, or distillation) is required.

## 9. Quality Control

- **Turbidity tube**: Fill a transparent tube with treated water. Look down through the water at a black-and-white disc at the bottom. The depth at which the disc becomes invisible indicates turbidity. Treated water should be visible at >20 cm depth (<5 NTU).
- **Chlorine residual test**: DPD colorimetric test kit. Add DPD reagent to water sample — turns pink in proportion to chlorine concentration. Compare to color chart. Target: 0.2-0.5 mg/L free chlorine after 30 minutes contact.
- **Hydrogen sulfide test**: Simple presence/absence test for fecal contamination. Water sample turns black if contaminated. No laboratory equipment needed. Use weekly as a screening test.
- **Sanitary inspection**: Monthly visual inspection of treatment system — check for cracks in filter tanks, clogged drainage, contamination sources upstream, and proper cover integrity.

## 10. Variations and Alternatives

- **Rapid sand filtration**: 50× faster flow rate than slow sand (5-15 m/hour) but requires chemical coagulation (alum or ferric chloride) as pretreatment. Depends on [chemistry capability](../chemistry/index.md). Less biological removal than slow sand but higher throughput.
- **UV disinfection**: Low-pressure mercury vapor lamp (254 nm) at 40 mJ/cm² provides effective disinfection without chemicals. Requires clear water and reliable electricity. No residual protection.
- **Distillation**: Boil water and condense the steam. Removes all contaminants (biological, chemical, dissolved solids). Energy-intensive: 620 kWh per 1,000 L (latent heat of vaporization). Practical only for small volumes or where energy is abundant.
- **Biosand filter**: A household-scale adaptation of slow sand filtration using a concrete or plastic container (~0.3 m² filter area). Intermittent operation (pour water through, collect from outlet). Removes 95-99% bacteria after biological layer develops. Flow rate: 0.5-1.0 L/minute.

## 11. References

- [Water Procurement](procurement.md) — raw water must be collected before treatment
- [Ceramics](../ceramics/index.md) — ceramic filter elements, tank construction
- [Chemistry](../chemistry/acids-bases.md) — chlorination chemicals, coagulants for rapid filtration
- [Health: Sanitation](../health/sanitation.md) — clean water is fundamental to sanitation
- [SEM Tech Water Treatment](sem-tech-water-treatment.md) — advanced desalination and purification

---
*Part of the [Bootciv Tech Tree](../index.md) • [Water](./index.md) • [All Domains](../index.md)*
