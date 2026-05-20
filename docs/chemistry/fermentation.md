# Fermentation Chemistry

> **Node ID**: chemistry.petroleum-alternatives.fermentation
> **Domain**: Chemistry
> **Timeline**: Years 5-20
> **Outputs**: ethanol, acetone, butanol, acetic_acid, methanol

### Ethanol Production

**Feedstocks**: Grain (barley, wheat, corn — starch → sugar via malt enzymes), sugar cane/beets (direct sugar), fruit (sugars), potatoes (starch). Starch must be converted to sugar first (malting/sprouting grain produces amylase enzymes that break starch into maltose).

**Malting**:
1. Soak grain in water 2-3 days. Drain and spread on malting floor.
2. Sprout 5-7 days, keep moist and at 15-20°C. Turn regularly to prevent matting and ensure even sprouting.
3. Grain produces amylase enzymes during germination — this is the key step. Amylase converts starch (long glucose polymer) into maltose and glucose (fermentable sugars).
4. Dry at 50-60°C to stop germination (kilning). Higher kilning temperatures produce darker, more roasted malt (affects flavor — irrelevant for industrial ethanol, relevant for distilled spirits).
5. Crush dried malt to coarse grist with roller mill.

**Mashing**:
- Mix grist with hot water (65-68°C) in insulated vessel (mash tun). Water-to-grist ratio ~3:1 by weight.
- Hold at 65-68°C for 1-2 hours. Amylase enzymes (alpha-amylase and beta-amylase) convert starch to maltose (C₁₂H₂₂O₁₁) and glucose (C₆H₁₂O₆).
- Test with iodine — blue = starch still present, no blue = conversion complete. Adjust temperature: 62-65°C favors beta-amylase (more maltose, more fermentable sugar). 68-72°C favors alpha-amylase (more dextrins, less fermentable sugar, fuller body).
- Strain liquid (wort) from spent grain. Spent grain is valuable livestock feed.

**Fermentation**:
- Cool wort to 20-30°C (yeast dies above ~40°C). Transfer to fermentation vessel.
- Add yeast (*Saccharomyces cerevisiae* — from previous batch or wild-captured). Pitching rate: ~1 g dry yeast per liter of wort.
- Ferment 3-7 days in closed vessel with airlock (CO₂ escapes, air cannot enter — wild microorganisms contaminate open vessels).
- C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂ (glucose → ethanol + carbon dioxide)
- Maximum ~12-15% ABV (alcohol kills yeast above ~15%). Fermentation is exothermic — temperature control critical. Active fermentation generates heat: monitor temperature, cool with water jacket or cold water bath if exceeding 30°C.

**Distillation**:
- Ethanol boils at 78.3°C (water at 100°C). Distill fermented wash in pot still or fractionating column.
- First distillation: ~40-50% ABV. Second distillation: ~70-80% ABV. Third distillation or fractionating column: ~95% ABV (azeotrope — cannot exceed 95.6% by simple distillation).
- For anhydrous ethanol (>99%): add quicklime (CaO) to absorb water, re-distill. Or use molecular sieves (zeolites — selectively adsorb water).
- Discard foreshots (first 50-100 mL — contains methanol and other low-boiling congeners, toxic). Discard fusel oils (last fraction — higher alcohols with unpleasant odor).

### Weizmann Acetone-Butanol Process

**Organism**: *Clostridium acetobutylicum* (anaerobic bacterium, Gram-positive, spore-forming). Can be isolated from soil or maintained as preserved culture on agar slants.

**Process**:
- Prepare starch substrate (corn, potato, or grain mash — same mashing process as ethanol).
- Sterilize mash by boiling (critical — competing bacteria will outcompete *Clostridium* if present).
- Cool to 35-37°C. Inoculate with *C. acetobutylicum* culture. Maintain strict anaerobic conditions (no oxygen — sparge with nitrogen or CO₂).
- Fermentation has two phases:
  - **Acidogenic phase** (first 18-24 hours): Bacteria produce acetic acid and butyric acid, pH drops to ~4.5.
  - **Solventogenic phase** (next 24-48 hours): Bacteria convert acids to solvents, pH stabilizes ~4.3.
- Products: acetone (~30%), n-butanol (~60%), ethanol (~10%) by volume, plus CO₂ and H₂ gases.
- **Distillation**: Separate by fractional distillation. Acetone bp 56°C, ethanol bp 78°C, n-butanol bp 118°C.

**Applications**: Acetone — solvent for resins, fats, plastics; key ingredient in nitrocellulose dope. n-Butanol — solvent, feedstock for butyl rubber and esters. This process was THE primary source of acetone for British cordite production during World War I.

### Acetic Acid Production

**Vinegar method** (biological):
- Expose ethanol solution to air with *Acetobacter* bacteria (present on fruit surfaces, in unpasteurized vinegar).
- Aerobic fermentation at 25-30°C for days to weeks. Provides continuous aeration (oxygen is required — unlike ethanol fermentation which is anaerobic).
- Produces 5-12% acetic acid. Slow but simple. No special equipment beyond vessels and air exposure.
- CH₃CH₂OH + O₂ → CH₃COOH + H₂O

**Chemical oxidation** (faster, higher yield):
- Pass ethanol vapor over heated copper catalyst (copper gauze at 300-400°C) with air.
- Ethanol oxidizes to acetaldehyde (CH₃CHO), then to acetic acid. Faster, higher concentration achievable.
- Applications: food preservation (vinegar), cellulose acetate (photographic film, synthetic fibers), acetic anhydride (aspirin synthesis, cellulose acetate production), metal etching, solvent.

### Methanol from Wood Pyrolysis

**Process**: Heat hardwood in closed iron retort to 400-500°C. Destructive distillation produces: charcoal (solid), wood tar (liquid), pyroligneous acid (aqueous condensate containing methanol, acetic acid, acetone).

- Distill pyroligneous acid — methanol boils at 64.7°C (lowest-boiling fraction, collected first).
- Yield: ~1-2% methanol by weight of wood. Low yield but works with basic metallurgy-stage technology.
- **Synthetic methanol**: React CO + 2H₂ over ZnO/Cr₂O₃ catalyst at 300-400°C, 20-30 MPa. Requires purified synthesis gas from coal gasification. Much higher yield and purity.

### Temperature Control

Fermentation is exothermic — uncontrolled temperature kills yeast or produces off-flavors:

- **Active fermentation peak**: 30-35°C generates maximum heat. Cool if exceeding 30°C for ale yeast, 15-20°C for lager yeast.
- **Methods**: Submerge fermentation vessel in cold water bath. Wrap with wet cloth (evaporative cooling). For large-scale: water jacket or cooling coil with circulating cold water. Monitor with thermometer twice daily minimum.
- **Kill temperature**: >45°C kills *Saccharomyces* within minutes. >35°C promotes production of fusel alcohols and esters (irrelevant for industrial ethanol, but wastes sugar carbon).

### Butanol and Biobutanol (ABE Fermentation)

The **Weizmann process** (Clostridium acetobutylicum) produces acetone, butanol, and ethanol in a 3:6:1 ratio. Butanol (C₄H₉OH) is a superior fuel to ethanol: higher energy density (29.2 MJ/L vs 21.2 MJ/L), miscible with gasoline at any ratio, lower hygroscopicity (doesn't absorb water), usable in unmodified engines. Feedstocks: corn starch, molasses, cellulose hydrolysate. Conditions: 30-37°C, anaerobic, pH controlled (switches from acidogenesis to solventogenesis at pH ~5). Yield: 10-20 g/L total solvents (low — product toxicity limits concentration). Modern strain improvement targets: higher tolerance (butanol inhibits growth above 12-15 g/L), continuous product removal by gas stripping or pervaporation membranes.

### Lactic Acid Fermentation

Lactic acid bacteria (Lactobacillus, Streptococcus, Pediococcus) convert sugars to lactic acid (C₃H₆O₃) via homofermentative pathway (2 mol lactic acid per mol glucose, yield >90%) or heterofermentative pathway (lactic acid + ethanol + CO₂). Industrial production: 30-45°C, pH 5-7 (neutralized with CaCO₃ or NaOH to prevent acid inhibition). Feedstock: glucose from corn starch or cane sugar. Downstream: calcium lactate filtered, acidified with H₂SO₄ to free lactic acid, purified. **Polylactic acid (PLA)**: Lactic acid oligomerized to lactide (cyclic dimer), then ring-opening polymerized to PLA — biodegradable thermoplastic for packaging, textiles, 3D printing filament. NatureWorks (USA) produces 150,000 tonnes/year PLA.

### Citric Acid Production

*Aspergillus niger* mold produces citric acid from sucrose or glucose at 25-30°C, pH 2-3 (acidic conditions suppress oxalic acid byproduct). The key industrial fermentation by volume (~2 million tonnes/year). Process: submerged fermentation in 100-200 m³ stirred tanks, 5-7 days. Yield: 80-95% of theoretical (1 mol citric acid per mol glucose). Downstream: filter mycelium, precipitate calcium citrate with Ca(OH)₂, redissolve with H₂SO₄, crystallize. Applications: food acidulant (60%), detergent builder (chelates Ca²⁺/Mg²⁺ — replaces phosphates), pharmaceutical effervescent tablets, metal cleaning.

### Biogas (Anaerobic Digestion)

Organic waste (manure, food waste, sewage sludge, agricultural residues) decomposed by mixed microbial consortium in the absence of oxygen. Four stages: (1) hydrolysis — complex polymers → monomers, (2) acidogenesis — monomers → volatile fatty acids, (3) acetogenesis — fatty acids → acetic acid + H₂ + CO₂, (4) methanogenesis — acetic acid → CH₄ + CO₂ (aceticlastic), H₂ + CO₂ → CH₄ (hydrogenotrophic). Product: biogas (55-70% CH₄, 30-45% CO₂, trace H₂S). Operating temperature: mesophilic (35-40°C, stable, most common) or thermophilic (50-60°C, faster, higher gas yield but less stable). Hydraulic retention time: 15-30 days (mesophilic). CSTR (completely stirred tank reactor) is standard design. Biogas upgraded to biomethane (>95% CH₄) by removing CO₂ (water scrubbing, PSA, or membrane separation) — can substitute for natural gas. Energy yield: 0.3-0.5 m³ biogas per kg volatile solids added. Small-scale: 2-50 kW digesters for farm or village use. Large-scale: 1-10 MW plants processing municipal waste.

### Fermentation Equipment Design

**Bioreactor types**: (1) **Stirred tank** — impeller (Rushton turbine or marine blade) provides mixing and O₂ transfer, baffles prevent vortexing. Standard for aerobic fermentations (citric acid, antibiotics). (2) **Air-lift** — rising bubbles in the riser section create circulation through the downcomer — no mechanical seals, lower shear. Used for shear-sensitive cells and large-scale single-cell protein. (3) **Bubble column** — simplest: sparge air at the bottom, bubbles rise through liquid. Low cost, good for viscous broths. (4) **Packed bed / fluidized bed** — immobilized cells on solid support (ceramic, alginate beads). Continuous operation. (5) **Anaerobic digester** — CSTR with gas-tight cover, heating jacket or heat exchanger (maintain 35°C), gas collection system.

**Sterilization**: Critical for pure-culture fermentations (contaminants compete for substrate and may produce toxins). Methods: (1) **Heat** — steam at 121°C for 15-30 minutes (batch sterilization of medium in the vessel). (2) **Continuous HTST** — 140°C for 5-10 seconds in a heat exchanger, then flash-cooled. More energy-efficient for large volumes. (3) **Filter sterilization** — 0.2 µm membrane filters for heat-sensitive components (vitamins, some growth factors). Equipment sterilization: steam all pipes, valves, and seals before filling — any dead leg or unsterilized pocket becomes a contamination source.

### Safety & Hazards

- **Ethanol fire**: Ethanol burns with nearly invisible blue flame. Cannot be seen in daylight. Keep away from open flames and sparks. Store in sealed metal containers. Fire extinguisher (CO₂ or dry chemical) required near distillation equipment.
- **Methanol toxicity**: Methanol is metabolized to formaldehyde and formic acid — causes blindness and death. As little as 10 mL can cause permanent blindness. Absorbed through skin. Label all containers clearly. NEVER store near food or drink. Use different-shaped containers than food/water vessels.
- **Distillation explosion**: NEVER distill in sealed vessels — pressure buildup causes explosion. Use open system with condenser vented to atmosphere. Never heat above boiling point of highest-boiling component. Pressure relief on all heated vessels.
- **CO₂ asphyxiation**: Fermentation produces large volumes of CO₂ (heavier than air, displaces oxygen). Never enter fermentation room without ventilation. CO₂ buildup in enclosed spaces causes rapid unconsciousness and death. Ensure adequate ventilation in all fermentation areas.

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
