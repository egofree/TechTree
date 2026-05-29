# Water Treatment (Health & Sanitation)

> **Node ID**: health.water-treatment
> **Domain**: [Health](./index.md)
> **Dependencies**: [`health.sanitation`](sanitation.md), [`chemistry.electrolysis`](../chemistry/electrolysis.md)
> **Enables**: [`health.medicine`](medicine.md), [`health.surgery-basics`](surgery-basics.md)
> **Timeline**: Years 5-15
> **Outputs**: potable_water, sanitized_water
> **Critical**: Yes — safe drinking water is the single most impactful public health intervention

## Overview

Water treatment for health and sanitation focuses on making water safe for human consumption: settling, sand filtration, boiling, chlorination, and UV treatment. Access to clean drinking water is the single most impactful public health intervention, preventing waterborne diseases (cholera, typhoid, dysentery) that would otherwise devastate a nascent industrial workforce.

## Waterborne Diseases and Their Prevention

**Major waterborne pathogens**:

| Disease | Pathogen | Source | Incubation | Mortality (untreated) | Prevention |
|---------|----------|--------|------------|----------------------|------------|
| Cholera | *Vibrio cholerae* | Fecal contamination | 2-5 days | 30-50% | Chlorination, boiling |
| Typhoid | *Salmonella typhi* | Fecal contamination | 7-14 days | 10-20% | Chlorination, filtration |
| Dysentery | *Shigella* spp. | Fecal contamination | 1-3 days | 5-15% | Chlorination, hygiene |
| Giardiasis | *Giardia lamblia* | Animal/human feces | 7-14 days | <1% | Filtration (5 μm), boiling |
| Cryptosporidiosis | *Cryptosporidium* | Animal feces | 2-10 days | <1% (low), high (immunocompromised) | Boiling, UV |
| Hepatitis A | HAV | Fecal contamination | 15-50 days | <1% | Chlorination, boiling |
| Leptospirosis | *Leptospira* | Animal urine | 7-12 days | 5-30% | Avoid contaminated water |
| Polio | Poliovirus | Fecal contamination | 6-20 days | 5-10% (paralytic) | Chlorination, vaccination |

**Impact of clean water**: In 19th-century London, Dr. John Snow's removal of the Broad Street pump handle (1854) ended a cholera outbreak that had killed 616 people. Modern WHO estimates: 1.4 million deaths/year from diarrheal diseases attributable to inadequate water, sanitation, and hygiene. Providing potable water reduces diarrheal disease by 25-40%. Combined with sanitation and hygiene: 50-65% reduction.

## Settling and Coagulation

**Plain sedimentation**: Allow water to stand undisturbed in a tank or basin. Particles >50 μm settle by gravity at a rate proportional to the square of their diameter (Stokes' law: v = gd²(ρ_p - ρ_w)/18μ). Settling velocity for 50 μm sand particle: ~2 mm/s. For 10 μm silt: ~0.08 mm/s. For 1 μm clay: ~0.001 mm/s (impractically slow — takes days). Detention time: 2-6 hours removes particles >25-50 μm. Basin design: depth 3-5 m, length 15-30 m, width 3-10 m. Surface loading rate: 1-2 m/hour.

**Coagulation with alum**: Add aluminum sulfate (Al₂(SO₄)₃·14H₂O) at 10-50 mg/L to raw water. Rapid mix (300-500 RPM for 1-3 minutes) disperses the coagulant. Al³⁺ ions neutralize the negative charge on colloidal particles (clays, bacteria, organic matter), allowing them to aggregate. Slow mix (20-40 RPM for 15-30 minutes) forms floc (gelatinous aluminum hydroxide aggregates, 0.1-3.0 mm diameter). Optimal pH: 6.5-7.5. Temperature effect: cold water (<5°C) slows floc formation — increase dose by 50-100% in winter. Alum dose determined by jar test: 6 beakers with varying doses, mix, settle 30 min, measure turbidity. Select dose giving lowest residual turbidity.

**Ferric chloride coagulation**: FeCl₃ at 5-30 mg/L. Works over wider pH range (4-11) than alum. Forms dense, fast-settling floc. Effective in cold water. Downside: more corrosive to dosing equipment, stains surfaces brown. Also removes arsenic by co-precipitation (As(III) oxidized to As(V) by chlorine, then adsorbed onto Fe(OH)₃ floc — 90-99% arsenic removal).

**Lime softening**: Add Ca(OH)₂ at 50-200 mg/L to remove calcium and magnesium hardness. Ca²⁺ precipitates as CaCO₃; Mg²⁺ precipitates as Mg(OH)₂ at pH >10.5. Raises pH to 10.5-11.0 (must recarbonate with CO₂ to lower pH to 8-9 before distribution). Side benefit: kills bacteria (pH >11 is bactericidal — 99.9% kill in 2-6 hours).

**Strengths**:
- Alum coagulation removes 90-95% of turbidity and 50-90% of bacteria in a single treatment step
- Jar test allows dose optimization for varying raw water quality — no fixed dose is universally correct
- Lime softening simultaneously softens water and kills bacteria at pH >11

**Weaknesses**:
- Alum dose must be determined by jar testing for each water source and adjusted seasonally — incorrect dose produces poor floc or restabilized colloids
- Coagulation produces sludge (aluminum hydroxide or ferric hydroxide) that requires disposal — 0.3-1.0% of treated water volume as sludge
- Cold water (<5°C) slows floc formation — dose must increase 50-100% in winter, and settling time must double

## Sand Filtration

**Slow sand filtration**: Filter bed: 0.6-1.2 m depth of fine sand (effective size 0.15-0.35 mm, uniformity coefficient 1.5-2.5) over 0.3-0.5 m gravel support layer. Filtration rate: 0.1-0.2 m/hour (very slow). A biological layer (schmutzdecke) forms on the sand surface within 1-2 weeks, providing biological treatment — bacteria, protozoa, and other microorganisms consume pathogens and organic matter. Pathogen removal: 95-99.5% bacteria, 99% Giardia, >90% viruses. Turbidity reduction: to <1 NTU. No chemical inputs required. Run time: 20-60 days before cleaning (scrape top 1-2 cm of sand, replace when bed depth drops below 0.5 m). Area requirement: 0.5-1.0 m² per person served (50-200 L/day/person).

**Rapid sand filtration**: Coarser sand (effective size 0.4-0.8 mm) at higher filtration rate (5-10 m/hour). Must be preceded by coagulation — the sand captures pre-formed floc, not raw particles. Run time: 12-48 hours between backwashing. Backwash: reverse flow at 30-50 m/hour for 5-10 minutes expands the bed by 20-30% and flushes accumulated solids. Water waste: 2-5% of production. Pathogen removal: 90-99% when preceded by proper coagulation. Turbidity: <0.5 NTU effluent. Footprint: 10-20× smaller than slow sand for same throughput.

**Strengths**:
- Slow sand filtration removes 95-99.5% of bacteria without any chemical inputs — the biological layer is the treatment mechanism
- Rapid sand filtration is 10-20× more compact than slow sand for the same throughput — fits in constrained spaces
- Both methods use readily available sand and gravel — no imported consumables

**Weaknesses**:
- Slow sand requires 0.5-1.0 m² per person served — impractical for large communities without abundant land
- Rapid sand requires coagulation pretreatment — without proper alum dosing and flocculation, rapid filters clog rapidly and produce poor quality effluent
- Both methods require periodic maintenance (sand scraping for slow sand, backwashing for rapid sand) — neglected filters fail silently

## Disinfection

**Boiling**: Heat water to a rolling boil (100°C at sea level). Maintained for 1 minute kills all bacteria, viruses, and protozoan cysts. 3 minutes at altitudes above 2000 m (boiling point drops ~1°C per 300 m elevation). Fuel consumption: ~0.3 kg wood per liter of water (heating 15°C water to 100°C requires ~355 kJ/L; wood energy content ~15 MJ/kg, 15% stove efficiency). For a family of 6 consuming 6 L/day of drinking water: 1.8 kg wood/day. Let boiled water cool covered to prevent recontamination. Store in clean, covered containers. Boiling does not remove chemical contaminants (heavy metals, pesticides, dissolved organics).

**Chlorination**: Add chlorine (as sodium hypochlorite NaOCl, calcium hypochlorite Ca(OCl)₂, or chlorine gas Cl₂) to achieve a free chlorine residual of 0.2-0.5 mg/L after 30 minutes contact time. Chlorine kills by oxidizing cell membranes and enzymes. Effectiveness: >99.9% bacteria, 99% viruses, 90-95% Giardia (requires higher dose: 1-2 mg/L and longer contact: 60 min). Does NOT kill Cryptosporidium (resistant to chlorine — requires filtration, boiling, or UV).

Dose calculation: For a 10,000 L storage tank requiring 1.0 mg/L chlorine dose: add 10 g of chlorine (as Cl₂ equivalent). If using 5% sodium hypochlorite (household bleach, 50,000 mg/L as Cl₂): add 10,000 mg / 50,000 mg/L = 200 mL of bleach. Dilute bleach in a bucket of water before adding to tank for even distribution. Test residual after 30 minutes with DPD color comparator or test strips (target 0.2-0.5 mg/L free chlorine). If residual is below 0.2 mg/L, dose was insufficient (water had high chlorine demand from organic matter) — retreat.

**Chlorine production on-site**: Electrolyze brine (NaCl solution, 3-5% concentration) with 12V DC power supply at 2-5 A for 30-60 minutes to produce NaOCl in situ. Reaction: 2NaCl + 2H₂O → Cl₂ + H₂ + 2NaOH (at electrodes), then Cl₂ + 2NaOH → NaOCl + NaCl + H₂O (in bulk solution). Production rate: ~0.5-1.0 g Cl₂ per ampere-hour. A 5A cell running for 1 hour produces ~3-5 g Cl₂, enough to treat 3,000-15,000 L of water at 0.3-1.0 mg/L dose. Requires [chlor-alkali knowledge](../chemistry/electrolysis.md).

**UV disinfection**: Pass water through a chamber containing a low-pressure mercury vapor UV lamp (254 nm wavelength). UV damages microbial DNA, preventing reproduction. Dose: 30-40 mJ/cm² for 99.9% bacteria kill, 40-60 mJ/cm² for 99% virus kill, 80-100 mJ/cm² for 99.9% Cryptosporidium/Giardia inactivation. Water must be pre-filtered to <10 NTU turbidity (suspended particles shield microorganisms from UV). Lamp output: 15-80 W. Flow rate: proportional to lamp power and required dose. Lamp life: 8,000-12,000 hours (output degrades ~20% over life). Advantage: no chemical residual, no taste/odor, effective against chlorine-resistant organisms. Disadvantage: no residual protection in distribution system (post-treatment contamination possible), requires electricity.

**Solar disinfection (SODIS)**: Fill clear PET plastic bottles (1-2 L) with clear water. Expose to full sunlight for 6 hours (or 2 days if cloudy). UV-A radiation (320-400 nm) and thermal heating (water reaches 45-55°C) inactivate pathogens. Effectiveness: >99.9% bacteria, >99% viruses. Does not work with turbid water (>30 NTU) or bottles larger than 2 L (insufficient UV penetration). Simple, free, no chemicals or energy required — suitable as an emergency measure. Limitations: slow, weather-dependent, small batch sizes.

**Strengths**:
- Boiling kills all pathogens including Cryptosporidium and Giardia — the most reliable single-method disinfection
- Chlorination provides residual protection in distribution pipes — treated water remains safe for hours to days after treatment
- SODIS requires zero consumables and zero energy — effective as a backup when all other methods fail

**Weaknesses**:
- Boiling consumes ~0.3 kg wood per liter — unsustainable at community scale without managed forestry
- Chlorine does not kill Cryptosporidium at normal doses, and high turbidity shields bacteria from chlorine contact
- SODIS produces only 1-2 L per bottle per 6-hour cycle — insufficient for household-scale drinking water needs without dozens of bottles

## Water Quality Standards

**WHO drinking water guidelines** (key parameters):

| Parameter | Guideline value | Health basis |
|-----------|----------------|-------------|
| E. coli / 100 mL | 0 | Fecal contamination indicator |
| Turbidity | <4 NTU (ideally <1) | Aesthetic, disinfection efficiency |
| Free chlorine residual | 0.2-0.5 mg/L | Disinfection |
| Total dissolved solids | <1000 mg/L | Taste, corrosion |
| Nitrate (as NO₃⁻) | <50 mg/L | Methemoglobinemia (blue baby syndrome) |
| Fluoride | <1.5 mg/L | Dental/skeletal fluorosis |
| Arsenic | <0.01 mg/L | Cancer, skin lesions |
| Lead | <0.01 mg/L | Neurological damage, especially children |
| Iron | <0.3 mg/L | Taste, staining |
| Manganese | <0.1 mg/L | Taste, staining |
| pH | 6.5-8.5 | Corrosion, disinfection effectiveness |
| Hardness (as CaCO₃) | No health guideline | Scale formation, soap consumption |

**Testing methods**: Portable test kits measure pH (colorimetric, ±0.2 pH units), turbidity (turbidity tube — black disk at bottom of graduated tube, read NTU from depth), free chlorine (DPD test kit — pink color proportional to concentration, read against color chart to ±0.1 mg/L), nitrate (test strips, semi-quantitative), and coliform bacteria (presence/absence: add sample to nutrient broth, incubate 24-48 hours at 35°C, color change indicates coliforms). For precise measurement: laboratory analysis by atomic absorption (metals at ppb levels), ion chromatography (anions), and membrane filtration (bacterial counts).

## Water Supply Systems

**Well construction**: Dug well: 1.0-1.5 m diameter, lined with stone or concrete rings, depth 5-30 m to water table. Drilled well: 100-200 mm diameter borehole, steel or PVC casing, depth 10-200+ m. Hand pump (Afridev-type): lifts water from up to 45 m depth, output 0.3-0.5 L/stroke, 10-15 L/min sustained pumping rate. Serves 200-300 people. Motorized pump: submersible electric pump at 0.5-5 kW, delivers 5-50 m³/hour depending on depth and pump size. Protect wellhead from contamination: concrete apron (1.5-2.0 m radius, sloped outward), sealed casing, fenced enclosure.

**Spring protection**: Collect water at the spring eye (where groundwater emerges) in a concrete collection box (1 × 1 × 1 m), sealed on three sides with an open front fitted with a screened overflow pipe. Backfill behind the collection box with gravel and clay to prevent surface water infiltration. Outlet pipe delivers water by gravity to a distribution point or storage tank. Yield: 0.1-50 L/s depending on the spring. Spring water is typically bacteriologically safe if the collection point is protected from surface contamination.

**Storage tanks**: Elevated storage tank (gravity distribution): steel or concrete tank on tower, height 10-30 m above service area, provides 10-30 psi (0.7-2.0 bar) distribution pressure. Volume: 50-500 m³ (sized for 1-2 days of demand plus fire reserve). Chlorine dosing point at the tank inlet. Distribution pipes: galvanized steel, PVC, or HDPE, 50-300 mm diameter, buried below frost line (0.5-1.5 m depth depending on climate). Minimum residual pressure at consumer tap: 1.0 bar (10 m head). Maximum: 6.0 bar (above this, pressure reducing valves needed).

## Sanitation

**Latrines**: Pit latrine: 1.0 × 1.0 × 3-5 m deep pit, concrete slab with drop hole and seat. Vent pipe (100-150 mm diameter PVC, screened top) reduces odors and fly breeding. Life: 5-15 years for a family of 6 at 0.5 m³/person/year fill rate. When pit is within 0.5 m of the slab, cover with earth and dig a new pit. Pour-flush latrine: adds a water seal (U-trap with 2-3 L water per flush) to prevent odors and flies. Requires 1-3 L water per use. VIP (ventilated improved pit) latrine adds screened vent pipe and superstructure for privacy.

**Septic tank**: Concrete or fiberglass tank (2,000-5,000 L for a household, 2-3 days hydraulic retention time). Settles solids (sludge accumulates at bottom, 30-50 L/person/year). Anaerobic digestion reduces sludge volume by 30-50%. Effluent (still contaminated — BOD 100-200 mg/L, pathogens present) discharges to drain field (perforated pipes in gravel trenches, 0.5-1.0 m below grade, 10-30 m of trench per bedroom). Soil provides final treatment through filtration and microbial action. Pump sludge every 3-5 years. Minimum distance from well: 30 m (to prevent groundwater contamination).

**Wastewater treatment** (community scale): Primary treatment: screening (bars at 20 mm spacing) → grit removal (velocity 0.3 m/s, detritus settles) → primary sedimentation (2-hour detention, removes 50-60% TSS, 25-35% BOD). Secondary treatment: activated sludge (aeration 4-8 hours, return sludge 25-100% of flow, waste sludge 1-5% of flow) or trickling filter (rock or plastic media, hydraulic loading 0.5-4.0 m³/m²/day, BOD removal 80-90%). Disinfection of effluent: chlorination (1-5 mg/L, 30 min contact) or UV (30-40 mJ/cm²). Effluent standards: BOD <30 mg/L, TSS <30 mg/L, fecal coliforms <200/100 mL.

## Hygiene Practices

**Handwashing**: Wash hands with soap (or wood ash if soap unavailable) and running water: after defecation, before food preparation, before eating, after handling animals, after treating sick persons. Reduces diarrheal disease by 30-50%. Soap requires [alkali production](../chemistry/alkalis.md) — fat + NaOH → soap + glycerol. Where soap is not available, scrubbing with wood ash (alkaline, contains K₂CO₃) provides some disinfection.

**Food safety**: Cook food to ≥70°C core temperature (kills most pathogens). Reheat leftovers to ≥70°C. Wash raw produce with treated water. Keep food covered to prevent fly contamination. Separate raw and cooked foods. Do not store cooked food at room temperature for >4 hours (bacteria double every 20-30 minutes at 20-40°C — a single bacterium becomes 1 million in 7 hours).

**Waste management**: Collect household waste in covered bins. Compost organic waste (food scraps, garden waste) at 55-65°C for 3+ days to kill pathogens. Bury non-compostable waste in sanitary landfill (minimum 0.6 m soil cover per day's waste). Minimum distance from water sources: 500 m for landfill, 30 m for latrines, 15 m from well to septic drain field.

## Emergency Water Treatment

**Household water treatment options** ranked by effectiveness:
1. Boiling (most reliable — kills all pathogens)
2. Chlorination with household bleach (5.25% NaOCl): 2 drops per liter, wait 30 min
3. Filtration through ceramic candle filter (0.5-1.0 μm pore size, 1-4 L/hour flow rate, 99.9% bacteria removal)
4. Solar disinfection (SODIS): clear PET bottle, 6 hours full sun
5. Coagulation-flocculation-disinfection (PUR sachets): aluminum sulfate + calcium hypochlorite in pre-measured sachet, treats 10 L in 30 minutes, removes turbidity and disinfects

**Cholera response**: When cholera is suspected, immediately switch all drinking water to boiled or chlorinated water. Dose: 1.0-2.0 mg/L free chlorine residual (higher than normal — cholera is highly infectious, ID₅₀ ~10⁶ organisms). Oral rehydration solution (ORS): 1 L clean water + 3.5 g NaCl + 2.5 g NaHCO₃ + 1.5 g KCl + 20 g glucose. Treats dehydration from cholera diarrhea (mortality reduced from 30-50% to <1% with prompt ORS). Volume: 200-400 mL after each loose stool. See [Medicine](medicine.md).

## Point-of-Use Treatment Technologies

**Ceramic pot filter**: Porous ceramic bowl (10-15 mm wall thickness, 30 cm diameter, 25 cm deep) sits inside a larger receptacle. Water poured into the ceramic bowl percolates through the pores (0.5-1.5 μm effective pore size) into the clean receptacle below. Flow rate: 1-3 L/hour. Removes 95-99% bacteria, 90-95% protozoan cysts. Does not remove viruses (too small, 0.02-0.1 μm). Manufacturing: mix clay (60-70%) with sawdust or rice husks (30-40%), press into mold, fire at 900-1000°C for 8-12 hours. The organic filler burns out, leaving interconnected pores. Impregnate with colloidal silver (0.1-0.5 mg Ag/L capacity) for enhanced bacterial removal (>99.9%). Cost: $2-5 per filter unit. Lifetime: 2-5 years with regular cleaning (scrub with brush and clean water weekly). Handles 20-30 L/day per unit.

**Biosand filter**: Concrete or plastic container (60 cm tall, 30 cm square) filled with layers: drainage gravel (6 cm, 5-12 mm), separation gravel (4 cm, 0.7-6 mm), filter sand (55 cm, 0.15-0.35 mm effective size). Standing water layer (5 cm) above the sand maintains a biological layer (biolayer) at the sand surface. Flow rate: 0.4-1.0 L/minute initially, declining to 0.1-0.3 L/minute as the biolayer matures and sand clogs (clean when flow drops below design rate by agitating the top 2-3 cm of sand). Pathogen removal: 95-99% bacteria, 95-99.9% protozoa, 70-95% viruses (variable). Also removes 50-90% turbidity and 50-95% iron. Volume treated: 20-60 L/day per filter. No consumables required after construction. Suitable for household or small community use.

**Cloth filtration (for guinea worm)**: Guinea worm (Dracunculus medinensis) larvae are carried by copepods (water fleas, 0.5-2.0 mm long) in stagnant surface water. Filtering through fine-mesh cloth (100 μm pore size, e.g., tightly woven cotton or nylon) removes copepods and prevents infection. This single intervention nearly eradicated guinea worm disease (from 3.5 million cases/year in 1986 to <30 cases/year in 2020). Cloth must be thoroughly dried or boiled between uses to kill any trapped copepods.

**Solar pasteurization**: Heat water to 65°C for 6 minutes, 70°C for 1 minute, or 75°C for 30 seconds to achieve 99.9% bacterial and 99% viral inactivation (WHO pasteurization thresholds). Use a solar cooker (parabolic reflector or box cooker) to heat a black-painted container of water. Monitor temperature with a wax indicator (carnauba wax melts at 82°C, beeswax at 62°C — use as a visual "safe temperature reached" indicator). Volume: 5-20 L per batch, depending on solar cooker size and insolation. Works best between 10:00-14:00 in tropical and subtropical latitudes (solar flux >600 W/m²).

## Removal of Specific Contaminants

**Arsenic removal**: Arsenic occurs naturally in groundwater in many regions (Bangladesh, West Bengal, parts of South America and the western US). WHO guideline: 10 μg/L. Long-term exposure causes skin lesions, cancers (skin, bladder, lung), and cardiovascular disease. Removal methods: (1) Oxidation from As(III) to As(V) using chlorine or potassium permanganate, then co-precipitation with ferric chloride (FeCl₃ dose 5-30 mg/L, pH 5-7, 95-99% removal). (2) Adsorption onto activated alumina (Al₂O₃) columns: capacity 2-10 g As per kg alumina, regenerated with NaOH. (3) Sono filter (Bangladesh): iron filings + sand + brick chips + wood charcoal in a household bucket — iron filings oxidize and adsorb arsenic, gravel and sand filter the iron-arsenic floc, charcoal removes organic matter. Cost: $5-10 per filter, treats 20 L/day for 6-12 months.

**Fluoride removal**: Excess fluoride (>1.5 mg/L) causes dental fluorosis (mottled teeth) at moderate levels and crippling skeletal fluorosis at high levels (>4 mg/L). Affected regions: East Africa Rift Valley, parts of India, China, and the western US. Removal methods: (1) Activated alumina adsorption (effective at pH 5.5-6.5, capacity 1-5 g F per kg alumina). (2) Bone char: crushed and charred animal bones (hydroxyapatite, Ca₁₀(PO₄)₆(OH)₂) adsorb fluoride through ion exchange. Pack into a column: 1-2 kg bone char treats 100-500 L at 5 mg/L F to below 1.5 mg/L. Regenerate with NaOH. (3) Nalgonda technique: add alum (Al₂(SO₄)₃) and lime (Ca(OH)₂) to water, stir, settle, filter. Fluoride co-precipitates with aluminum hydroxide floc. Removes 60-80% of fluoride. Dose: 100-500 mg/L alum + 20-100 mg/L lime depending on initial fluoride level.

**Iron and manganese removal**: Dissolved Fe²⁺ and Mn²⁺ are common in groundwater (anaerobic conditions keep them in solution). Aeration (cascade or spray) oxidizes Fe²⁺ to Fe³⁺, which precipitates as Fe(OH)₃ at pH >7. Then filter through sand. Manganese requires stronger oxidation: add chlorine (1-2 mg/L) or potassium permanganate (0.5-2.0 mg/L) to oxidize Mn²⁺ to Mn⁴⁺, which precipitates as MnO₂. Sand filter removes the precipitate. Greensand (glauconite sand coated with MnO₂) provides catalytic oxidation — the coated sand surface catalyzes the oxidation of dissolved Mn²⁺ and Fe²⁺ on contact.

**Nitrate removal**: Nitrate (>50 mg/L as NO₃⁻) causes methemoglobinemia in infants ("blue baby syndrome" — nitrate converts hemoglobin to methemoglobin, which cannot carry oxygen). Sources: fertilizer runoff, septic systems, animal waste. Removal: (1) Ion exchange using strong-base anion resin (removes 90-95% nitrate, regenerates with NaCl brine). (2) Biological denitrification: heterotrophic bacteria reduce NO₃⁻ → NO₂⁻ → N₂ gas using a carbon source (methanol, ethanol, or acetate added at 2-3 g C per g NO₃⁻-N). Anoxic conditions required (no dissolved oxygen). Hydraulic residence time: 2-6 hours. (3) Reverse osmosis: 90-98% nitrate rejection, but requires high-pressure pump (10-20 bar) and produces 25-50% reject water.

## Monitoring and Surveillance

**Routine water quality monitoring**: Test source water, treatment plant output, and distribution system points weekly for: turbidity (target <1 NTU), free chlorine residual (0.2-0.5 mg/L), pH (6.5-8.5), and monthly for: total coliforms and E. coli (0 per 100 mL). Sampling frequency: 1 sample per 1,000 population per month (minimum), or 1 sample per 5,000 population per month for small systems.

**Sanitary survey**: Inspect water source and surrounding area for contamination risks: latrines within 30 m uphill of well, livestock access to source, unprotected wellhead, cracked casing, backflow potential. Score each risk factor. Prioritize corrective actions based on risk score. Conduct annually or after flooding events.

## Small Community Water Systems

**Gravity-fed systems**: Where a spring or surface water source exists at elevation above the community, pipe water by gravity through HDPE or PVC pipes (25-100 mm diameter) to a reservoir tank (5-50 m³) at the village center, then to public tap stands (each serving 150-250 people). Design flow: 20-50 L/person/day for rural communities (vs. 100-200 L/person/day for urban piped systems). Pipe velocity: 0.5-2.0 m/s (too fast = erosion and water hammer; too slow = sediment deposition). Air valves at high points, washout valves at low points. Typical cost: $15-40 per person served. No pumps or energy required — gravity does the work. System lifespan: 20-40 years with periodic pipe replacement.

**Hand pump programs**: India Mark II hand pump (most widely deployed globally, >3 million units): lifts water from 15-50 m depth. Pump cylinder diameter 63.5 mm, stroke length 125 mm, displacement 400 mL/stroke. Output at 40 strokes/minute: ~16 L/min (960 L/hour). Serves 250-300 people at 25 L/person/day. Pump body: cast iron cylinder, brass liner, nitrile rubber check valves. Above-ground: galvanized steel rising main (32-50 mm), cast iron pump head, steel handle. Maintenance: replace cup seals and check valves every 6-18 months (cost $2-5). Village-level maintenance training requires 3-5 days. Spare parts supply chain critical — 30-50% of hand pumps in sub-Saharan Africa are non-functional at any given time due to lack of spare parts.

**Rainwater harvesting**: Collect roof runoff in storage tanks. Annual yield (L) = roof area (m²) × annual rainfall (mm) × runoff coefficient (0.8-0.9 for metal/tile roofs) × filter efficiency (0.9). Example: 50 m² roof in a region with 1000 mm annual rainfall: 50 × 1000 × 0.85 × 0.9 = 38,250 L/year (105 L/day average). Storage sizing: 2-6 months of dry-season demand. For a family of 6 at 20 L/person/day during a 4-month dry season: 6 × 20 × 120 = 14,400 L storage needed. Tank options: ferrocement (reinforced mortar, $0.5-1.0 per liter of storage), polyethylene (rotomolded, $0.8-1.5/L), or brick/plaster ($0.3-0.8/L). First flush diverter (discard first 1-2 mm of rainfall, which washes dust and bird droppings off the roof) is essential for water quality.

**Solar-powered pumping**: Photovoltaic panels (300-1500 W peak) power a submersible DC pump (brushless, 24-48V) in a borehole. Pump output proportional to solar irradiance: peak output at solar noon, zero at night. Typical daily output (at 5 kWh/m²/day insolation): 5-30 m³/day from 10-50 m depth. Water stored in an elevated tank (10-20 m³) for use during non-pumping hours. Controller includes maximum power point tracking (MPPT) to optimize pump speed for available solar power. System cost: $3,000-8,000 (panels, pump, controller, wiring, tank). Operating cost: near zero (no fuel). Payback vs. diesel pump: 2-4 years at current diesel prices. See [Solar Power](../energy/solar-thermal.md).

## Desalination (Emergency and Small-Scale)

**Solar still**: Basin-type solar still: shallow black basin (1-2 m²) filled with 2-5 cm of saline or contaminated water, covered with a sloped glass or clear plastic cover. Solar radiation heats the water; evaporated pure water condenses on the cooler cover and runs down to a collection trough. Output: 2-5 L/day per m² of basin area (depending on insolation and ambient temperature). Efficiency: 30-50% of incident solar energy used for evaporation. Multiple-effect basin stills (stacked basins, reusing condensation heat) achieve 8-12 L/day per m². Suitable for individual households in arid coastal areas.

**Distillation (fuel-fired)**: Boil saline water, condense the steam. Simple pot still: 50 L pot on a wood fire, copper or steel condenser coil cooled in a bucket of water. Output: 10-20 L of distilled water per hour. Fuel consumption: 0.5-1.0 kg wood per liter of distilled water (inefficient — most heat escapes with the flue gases). Multi-stage flash distillation (industrial scale) achieves 6-10 kg distilled water per kg of steam but requires complex pressure vessels and heat exchangers. Distilled water is pure (TDS <10 mg/L) but lacks beneficial minerals — long-term consumption without dietary mineral supplementation may contribute to trace element deficiencies.

## Pipe Materials and Distribution

**Pipe selection by scale**: Household plumbing: galvanized steel (15-50 mm, 50-year life in neutral pH water), copper (10-25 mm, 70+ year life, antimicrobial surface kills 99.9% bacteria in 6 hours), or PEX/PVC plastic (simplest to install, 25-50 year life). Community distribution: HDPE (high-density polyethylene, 50-200 mm, fusion-welded joints, 50+ year life, flexible enough for trench-laying without elbows), PVC (50-300 mm, solvent-welded joints, 50-year life, rigid), or ductile iron (80-500 mm, mechanical or flanged joints, 50-100 year life with cement mortar lining).

**Leak detection**: Unaccounted-for water (UFW) in developing-world distribution systems: 30-60% of treated water is lost to leaks, illegal connections, and under-billing. Pressure management: reduce night-time pressure (when demand is low) to 2-3 bar to minimize leak flow rates — a 10 mm hole at 5 bar loses 6.4 m³/day; at 2 bar, only 4.0 m³/day. Leak detection methods: acoustic listening stick (mechanical, $10-50, detects leak sound at 200-800 Hz within 1-3 m), step testing (isolate sections of network, measure flow — if flow persists with all consumers shut off, there is a leak), and tracer gas (inject helium or hydrogen into empty pipe, detect escaping gas above ground with sensitive detector).

**Water metering**: Positive displacement meters (for small connections, 15-25 mm, accuracy ±2% above 15 L/hour) measure every drop, encouraging conservation — metered households use 15-25% less water than unmetered flat-rate households. Ultrasonic meters (no moving parts, 50-300 mm pipe, ±1% accuracy) for large connections. Reading: manual (visual read monthly) or automated (radio pulse transmitted to data collector, 300 m range). Revenue: water tariff of $0.30-1.50 per m³ (typical for developing countries) — a household consuming 6 m³/month pays $1.80-9.00/month.

## Water Treatment for Healthcare Facilities

**Health center water requirements**: A rural health center (50-100 beds) requires 200-400 L/patient/day of treated water for drinking, cooking, bathing, laundry, and clinical procedures. Minimum quality: WHO drinking water standards (0 E. coli/100 mL, turbidity <1 NTU, free chlorine 0.2-0.5 mg/L). Surgical scrub sinks: 20-30 L per scrub, elbow-operated taps (hands-free to prevent recontamination). Autoclave feed water: must be softened (hardness <50 mg/L as CaCO₃) to prevent scale buildup on heating elements — distilled or deionized water preferred for autoclave life.

**Dialysis water**: Hemodialysis requires ultrapure water (endotoxin <0.25 EU/mL, bacteria <100 CFU/mL, total dissolved solids <10 mg/L). A single dialysis session uses 120-200 L of water. Production: carbon filter (remove chlorine/chloramine) → water softener → reverse osmosis (RO, rejects 95-99% of dissolved ions at 10-20 bar) → deionization (DI, mixed-bed resin, polished to <1 μS/cm conductivity) → UV sterilization → 0.22 μm final filter. Weekly disinfection of the entire water treatment loop with hot water (85°C for 30 minutes) or peracetic acid (0.2-0.5% for 15-30 minutes).

**Dental unit water lines**: Dental handpieces and air/water syringes spray water directly into patients' open mouths — water quality must meet drinking water standards (<500 CFU/mL heterotrophic bacteria, per ADA guideline). Biofilm rapidly colonizes the narrow-bore tubing (1-3 mm ID) of dental units: flush lines for 30-60 seconds between patients to reduce bacterial counts by 90-99%. Weekly shock treatment with 0.5-1.0% sodium hypochlorite for 10-30 minutes, followed by thorough flushing.

## Ice Production and Cold Chain

**Ice for medical use**: Ice preserves vaccines (most require 2-8°C storage — ice-lined refrigerator maintains this range for 24-48 hours during power outages), organ transport (0-4°C perfusion), and fever reduction (external cooling). Produce ice in a brine-cooled tank: submerged aluminum or steel cans (5-20 L each) filled with clean water, immersed in -10 to -15°C calcium chloride brine (29% CaCl₂ by weight, freezing point -21°C). A 1 kW compressor produces ~15-25 kg of ice per hour. Store in insulated cabinet (100-200 mm expanded polystyrene walls) — ice melts at 1-3% per hour depending on ambient temperature and cabinet quality. Cold chain for vaccines: insulated vaccine carrier (1-5 L capacity, 2-8°C for 48-72 hours with ice packs) for transport from depot to clinic. Temperature monitoring: digital data logger (±0.5°C accuracy, records every 5-10 minutes) — discard vaccines exposed to >8°C for >2 hours or <0°C (freezing destroys most vaccines).

**Waterborne outbreak investigation**: When >2 cases of acute diarrheal disease occur in a community within 1 week: (1) Confirm diagnosis (stool culture for Vibrio, Salmonella, Shigella; rapid test for cholera: Crystal VC dipstick, result in 15 minutes, sensitivity 93-97%). (2) Identify water source — interview all cases about water consumed in past 5 days. (3) Collect water samples from suspected source (100 mL in sterile bottle with sodium thiosulfate to neutralize chlorine). (4) Test for E. coli (membrane filtration: filter 100 mL through 0.45 μm membrane, place on chromogenic agar, incubate 18-24 hours at 44°C, count blue colonies — each blue colony = 1 E. coli per 100 mL). (5) Issue boil-water advisory immediately if any E. coli detected in treated water. (6) Super-chlorinate suspected source (dose to 5-10 mg/L free chlorine, flush all pipes, retest after 24 hours).

## Quantifying Public Health Impact

**DALYs averted**: The disability-adjusted life year (DALY) combines years of life lost (YLL) from premature mortality and years lived with disability (YLD). Diarrheal diseases cause 40-50 million DALYs per year globally. Water, sanitation, and hygiene (WASH) interventions avert 5-10 million DALYs per year. Cost-effectiveness: improved water supply averts DALYs at $5-50 per DALY (very cost-effective by WHO threshold of <1× GDP per capita per DALY). Household water treatment averts DALYs at $0.50-10 per DALY. For comparison: oral rehydration therapy costs $50-200 per DALY averted; antiretroviral therapy for HIV costs $500-2000 per DALY averted.

**Morbidity tracking**: Establish baseline diarrheal disease incidence before water treatment intervention (typically 2-8 episodes per child per year in untreated settings). After intervention, track weekly: number of diarrhea cases (≥3 loose stools in 24 hours) per 1,000 population, stratified by age (<5 years, 5-15, >15). Expect 25-40% reduction within 6 months of clean water provision. Use community health workers to conduct monthly household surveys (diarrhea prevalence in last 2 weeks, number of episodes, treatment sought). Monitor clinic visits for dysentery (bloody diarrhea), cholera, and typhoid — these should decrease by 50-80% with effective water treatment.

## Water Reuse and Recycling

**Greywater reuse**: Water from bathing, laundry, and kitchen sinks (greywater, as opposed to blackwater from toilets) can be treated for non-potable reuse. Greywater characteristics: BOD 100-300 mg/L, TSS 50-200 mg/L, turbidity 20-100 NTU, fecal coliforms 10³-10⁵/100 mL. Simple treatment: coarse screen (1 mm mesh) → small grease trap (20-50 L, 30-minute retention, skim floating fats) → mulch basin or gravel trench (1-2 m deep, 0.5-1.0 m wide) for subsurface irrigation of non-food crops. Yield: a household of 6 generates 60-180 L/day of greywater — sufficient to irrigate 10-30 m² of garden. Do NOT store greywater >24 hours (bacterial growth causes odors and health risks). Do NOT use for food crop irrigation without disinfection (chlorinate to 0.5 mg/L free chlorine residual if food crops are irrigated).

**Blackwater treatment**: Toilet waste (blackwater) contains 10⁶-10⁸ fecal coliforms per 100 mL, BOD 200-600 mg/L, TSS 200-500 mg/L. Composting toilet: aerobic decomposition at 40-60°C for 6-12 months reduces pathogens to safe levels (thermophilic composting at >55°C for >3 days kills >99.9% of all pathogens including Ascaris eggs, which are among the most heat-resistant). Averaging 0.12-0.18 kg feces and 1.0-1.5 L urine per person per day. Carbon source (sawdust, straw, or dried leaves) added at 1-2 cups per use to maintain C:N ratio of 20-30:1 and absorb moisture. Vault capacity: 1-2 m³ per person per year (combined liquid and solid with carbon cover material).

## Materials

### Treatment Chemicals

| Material | Purpose | Typical Dose | Source |
|----------|---------|-------------|--------|
| Aluminum sulfate (alum) | Coagulation | 10-50 mg/L | Chemical manufacturing |
| Ferric chloride | Coagulation, arsenic removal | 5-30 mg/L | Chemical manufacturing |
| Calcium hydroxide (lime) | Softening, pH adjustment | 50-200 mg/L | Limestone kiln |
| Sodium hypochlorite (bleach) | Disinfection | 0.2-0.5 mg/L residual | Chlor-alkali electrolysis |
| Calcium hypochlorite | Disinfection (dry storage) | 0.2-0.5 mg/L residual | Chemical manufacturing |
| Activated alumina | Arsenic/fluoride adsorption | Column media | Chemical manufacturing |
| Bone char | Fluoride removal | Column media | Animal bones, charred |
| Colloidal silver | Ceramic filter enhancement | 0.1-0.5 mg/L capacity | Chemical supply |

### Filtration Media

| Material | Specification | Purpose |
|----------|--------------|---------|
| Fine sand | 0.15-0.35 mm effective size | Slow sand filtration |
| Coarse sand | 0.4-0.8 mm effective size | Rapid sand filtration |
| Gravel | 5-30 mm graded | Support layer, drainage |
| Ceramic clay | 60-70% clay + 30-40% sawdust | Pot filters (fired at 900-1000°C) |
| Activated charcoal | Granular, 0.5-2.0 mm | Taste/odor removal, organic adsorption |

### Construction Materials

| Material | Use | Notes |
|----------|-----|-------|
| Concrete | Tank construction, well aprons, latrine slabs | Portland cement + sand + gravel + water |
| HDPE pipe | Distribution mains (50-200 mm) | Fusion-welded joints |
| PVC pipe | Distribution, plumbing (50-300 mm) | Solvent-welded joints |
| Galvanized steel | Service connections (15-50 mm) | 50-year life in neutral pH |
| Ferrocement | Storage tanks, small reservoirs | Cement mortar over wire mesh |

## Equipment

| Equipment | Scale | Estimated Cost | Notes |
|-----------|-------|---------------|-------|
| Hand pump (Afridev/India Mark II) | Community | $500-1,500 | Lifts from 15-50 m depth |
| Submersible electric pump | Community | $200-1,000 | 0.5-5 kW, 5-50 m³/hour |
| Solar pump system | Community | $3,000-8,000 | 300-1500 W PV + pump + controller |
| Slow sand filter (50 m²) | Community (500 people) | $2,000-5,000 | Concrete tank, sand, gravel |
| Rapid sand filter | Community | $5,000-15,000 | Requires coagulation pretreatment |
| Chlorine dosing pump | Community | $100-500 | Metering pump or gravity drip |
| DPD test kit | Any | $10-30 | Free chlorine residual testing |
| Turbidity tube | Any | $5-15 | Simple visual turbidity measurement |
| Coliform test kit (P/A) | Any | $20-50 | Presence/absence bacteria test |
| Ceramic pot filter | Household | $2-5 | 1-3 L/hour, 2-5 year life |
| Biosand filter | Household | $10-30 | Concrete container, sand media |
| UV disinfection unit | Household/community | $50-200 | Requires electricity, 15-80 W lamp |

## Safety

- **Chlorine handling**: Sodium hypochlorite solutions are corrosive and irritate skin and eyes. Wear gloves and eye protection when handling concentrated bleach. Mix in well-ventilated area. Never mix bleach with acid (produces toxic chlorine gas). Store in cool, dark place — bleach degrades in heat and light.
- **Boiling water**: Risk of scald burns from steam and hot water. Use thick cloth or gloves when handling hot containers. Keep children away from boiling operations. Cover pots to reduce steam exposure.
- **Well construction safety**: Dug wells deeper than 1.5 m require shoring (temporary wall support) to prevent collapse. Never work alone in a deep excavation. Gas hazards (methane, hydrogen sulfide) can accumulate in deep wells — ventilate before entering and use a candle test (if flame dies, do not enter).
- **UV lamp hazards**: UV-C radiation at 254 nm damages skin and eyes. Never look directly at an operating UV lamp. Enclose the UV chamber completely. Disconnect power before lamp maintenance. Dispose of spent mercury vapor lamps properly — they contain mercury.
- **Alum and coagulant handling**: Aluminum sulfate and ferric chloride are acidic and corrosive. Avoid skin contact, wear gloves. Ferric chloride stains surfaces and clothing brown. Store in corrosion-resistant containers (HDPE, not steel for FeCl₃).
- **Alkalinity testing chemicals**: Phenol red and bromothymol blue indicators are low hazard. DPD reagent is a mild irritant. Keep all test reagents away from drinking water supplies to avoid accidental consumption.
- **SODIS bottles**: Do not use scratched or discolored PET bottles (reduced UV transmission). Replace bottles every 6-12 months. Do not use PVC bottles (may leach plasticizers).

## Limitations

- **No single treatment removes all contaminants**: Boiling kills pathogens but does not remove chemicals, heavy metals, or turbidity. Filtration removes particles and microbes but not dissolved chemicals. Chlorination kills most bacteria and viruses but not Cryptosporidium. A multi-barrier approach (settling → filtration → disinfection) is necessary for comprehensive treatment.
- **Infrastructure dependency**: Piped water systems require pumps, pipes, power, and ongoing maintenance. In developing-world settings, 30-50% of water infrastructure is non-functional at any given time due to pump failure, pipe breaks, or power outages. Simpler technologies (hand pumps, household filters) are more sustainable where maintenance capacity is limited.
- **Chlorine limitations**: Chlorine is ineffective against Cryptosporidium and Giardia at normal doses. High turbidity shields microorganisms from chlorine contact. Organic matter in source water creates chlorine demand, requiring higher doses and producing disinfection byproducts (trihalomethanes, haloacetic acids) at elevated levels.
- **Scale constraints**: Household-level treatment (boiling, ceramic filters, SODIS) serves individual families but cannot address community-scale contamination. Community-scale systems (piped distribution, central treatment) require capital investment, trained operators, and institutional support.
- **Water quality testing gaps**: Field test kits provide approximate results. Precise measurement of heavy metals (arsenic, lead, fluoride) requires laboratory equipment (atomic absorption, ion chromatography) that may not be available in early bootstrap stages. In the absence of testing, use multiple treatment barriers as a precaution.
- **Climate dependence**: Solar disinfection requires adequate sunlight (6+ hours). Rainwater harvesting depends on rainfall patterns. Surface water availability varies seasonally. Groundwater may be deep or contaminated with naturally occurring arsenic or fluoride.

## See Also

- [Medicine & Surgery](medicine.md) — disease treatment, pharmaceutical production, surgical capability
- [Sanitation](sanitation.md) — sewage disposal, latrine design, hygiene practices
- [Industrial Water Treatment](../chemistry/water-treatment.md) — deionized and ultrapure water for industrial processes
- [SEM Tech Water Treatment](../water/sem-tech-water-treatment.md) — electrodialysis desalination using ion exchange membranes
- [Electrolysis](../chemistry/electrolysis.md) — chlorine production for water disinfection
- [Alkali Production](../chemistry/alkalis.md) — soap production for hygiene
- [Food & Agriculture](../foundations/food-agriculture.md) — irrigation water quality and food safety
- [Energy](../energy/index.md) — energy requirements for pumping, boiling, and UV treatment

---

*Part of the [Bootciv Tech Tree](../index.md) • [Health](./index.md) • [All Domains](../index.md)*
