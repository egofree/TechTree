# Precious Metal Production (Gold & Silver)

> **Node ID**: metals.precious-metals
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`metals.non-ferrous`](non-ferrous.md), [`metals.copper-bronze`](copper-bronze.md), [`chemistry.acids`](../chemistry/acids.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 15-50
> **Outputs**: gold, silver, semiconductor-grade gold wire, silver paste, refined precious metals
> **Critical**: true

### Overview

Gold and silver occupy a unique position in industrial metallurgy: both are ancient metals (worked since 6000 BCE) yet remain indispensable in modern semiconductor manufacturing. Gold wire (25 μm diameter) bonds silicon die to package leads. Silver paste screen-prints electrical contacts on solar cells. Platinum-group metals catalyze chemical processes from nitric acid production to petroleum refining. Despite their antiquity, producing these metals to semiconductor-grade purity (99.99%+) demands electrochemistry, controlled atmospheres, and precise acid management.

This capability covers the production chain from ore (or recycled electronic scrap) through extraction and refining to high-purity gold and silver suitable for electronics, coinage, and chemical applications.

### Gold

Gold (Au, atomic number 79) is the most noble metal — it does not oxidize in air at any temperature, resists attack by most acids, and retains its metallic luster indefinitely. These properties make it irreplaceable for corrosion-free electrical contacts and wire bonding in semiconductor packaging.

**Geological occurrence**:

Gold occurs almost exclusively as native metal (elemental Au) in geological deposits. Unlike most metals, gold rarely forms minerals with other elements — the exceptions are telluride ores (calaverite AuTe₂, sylvanite (Au,Ag)Te₂) which are economically important in some deposits (Kalgoorlie, Australia; Cripple Creek, Colorado). Gold is widely distributed at trace levels (0.003-0.005 ppm in Earth's crust) but economic concentrations require geological enrichment.

**Deposit types**:
- **Alluvial/placer deposits**: Gold particles (flour gold <0.5 mm, nuggets up to kg scale) concentrated by water in stream beds, river terraces, and beach sands. Specific gravity of gold (19.3) causes hydraulic sorting — gold settles where water velocity drops. These were the first gold sources mined historically and remain important today (Indonesia, Brazil, Russia). Grade: 0.1-5 g/m³ of gravel.
- **Hard-rock (lode) deposits**: Gold disseminated in quartz veins (mesothermal, epithermal) or associated with sulfide minerals (pyrite, arsenopyrite). Major deposits: Witwatersrand (South Africa — largest gold field ever discovered, ~40% of all gold ever mined), Carlin Trend (Nevada), Kalgoorlie (Australia). Grade: 2-15 g/t (grams per tonne) in modern operations.
- **Lateritic/saprolitic**: Tropical weathering of gold-bearing bedrock concentrates gold in the oxidized zone. Important in West Africa and South America. Grade: 0.5-3 g/t.

**Ore identification and beneficiation**:
- **Placer mining**: Gravity separation exploits gold's extreme density (19.3 g/cm³). Panning, sluice boxes, hydraulic mining, and dredging. Recovery rate: 70-90% for particles >100 μm. Fine gold (<50 μm) is lost to tailings without chemical extraction.
- **Hard-rock beneficiation**: Crush ore to 75-150 μm. Free-milling gold (coarse particles visible to the eye) recovered by gravity circuits (centrifugal concentrators like the Falcon or Knelson). Refractory gold (locked in sulfide mineral matrix) requires flotation to produce sulfide concentrate (30-100 g/t Au), then roasting or pressure oxidation to liberate gold before leaching. Recovery rate: 85-97%.

**Strengths**:
- Gold's extreme density (19.3 g/cm³) enables simple gravity separation from gangue — placer mining recovers 70-90% of particles >100 μm with no chemical reagents.
- Alluvial deposits require no hard-rock mining infrastructure — panning and sluicing can begin at the earliest stages of metallurgy.

**Weaknesses**:
- Hard-rock gold ore grades are very low (2-15 g/t), requiring processing of 50-500 tonnes of ore per kg of gold.
- Refractory gold (locked in sulfide matrix) requires roasting or pressure oxidation before leaching — adding significant process complexity.

### Gold Extraction Methods

**Mercury amalgamation** (ancient, hazardous, still used by artisanal miners):

Gold dissolves in liquid mercury forming an amalgam (Au-Hg alloy). Crush ore, mix with mercury in a sluice or pan. Gold particles contact mercury and dissolve; waste rock does not. The amalgam (40-60% Au) is squeezed through chamois leather to remove excess mercury, then retorted: heat to 500-600°C in a sealed iron retort. Mercury vaporizes (bp 357°C), condenses in a water-cooled tube, and is collected for reuse. Gold sponge remains in the retort.

- **Recovery**: 30-50% of gold in ore (poor — fine gold is lost).
- **Hazard**: Mercury is a cumulative neurotoxin. Vapor inhalation causes tremor, kidney damage, and cognitive decline. Artisanal gold mining releases ~1000 tonnes/year of mercury to the environment — the largest single-source mercury pollution globally. Modern industrial operations do NOT use mercury.
- **Product**: Sponge gold, 60-90% purity. Requires further refining.

**Cyanidation** (dominant industrial method, ~80% of primary gold production):

Gold dissolves in dilute sodium cyanide (NaCN) solution in the presence of oxygen. The Elsner equation: 4Au + 8NaCN + O₂ + 2H₂O → 4Na[Au(CN)₂] + 4NaOH. The gold-cyanide complex (aurous cyanide, extremely stable with Kf = 2 × 10³⁸) keeps dissolved gold in solution.

- **Heap leaching** (low-grade ore, 0.5-2 g/t): Crush ore to <12 mm, stack on impermeable pad (HDPE liner) in 5-10 m lifts. Sprinkle dilute NaCN solution (0.01-0.05% NaCN, pH 10-11 maintained with lime CaO) over the heap at 5-10 L/m²/hour. Solution percolates through ore over 30-120 days, dissolving gold. Pregnant solution collects in ponds. Recovery: 50-80%. Used for vast low-grade deposits (Carlin Trend).
- **Tank leaching** (VAT leaching, higher grade, 2-10 g/t): Crush ore to 75-150 μm, agitate in large tanks (500-5000 m³) with NaCN solution (0.05-0.1%) and air sparging. Leach time: 24-72 hours. Recovery: 90-97%.
- **Carbon adsorption**: Gold-cyanide complex is adsorbed onto activated carbon (2-6 mm granules) in counter-current columns. Loading: 3-10 kg Au per tonne of carbon. Loaded carbon is stripped with hot (90-95°C) NaOH/NaCN solution or pressurized ethanol.
- **Zinc precipitation (Merrill-Crowe process)**: De-aerate pregnant solution (oxygen interferes), add zinc dust (Zn + 2[Au(CN)₂]⁻ → 2Au + Zn(CN)₄²⁻). Gold precipitates as fine powder with zinc and other metals. Filter, melt with flux (borax, silica) to produce doré bullion (70-90% Au + Ag).
- **Safety**: Cyanide is acutely toxic (LD₅₀ 1-3 mg/kg HCN gas). Tailings ponds must be impermeable and monitored. Cyanide destruction by hydrogen peroxide (SO₂/air process: CN⁻ oxidized to CNO⁻) before discharge. International Cyanide Management Code governs best practices.

**Gravity concentration** (for free-milling ores):

Centrifugal concentrators (Falcon, Knelson) apply 60-300G to a fluidized bed of crushed ore. Dense gold particles penetrate the bed and are trapped in riffles while lighter gangue overflows. Recovery: 40-70% of gold from free-milling ores. Typically used as a pre-concentration step before cyanidation to recover coarse gold (which cyanidation handles poorly).

**Strengths**:
- Cyanidation achieves 90-97% gold recovery from crushed ore (tank leaching) — the highest recovery of any industrial gold extraction method.
- Heap leaching processes vast low-grade deposits (0.5-2 g/t) economically — enables mining ore that would be unprofitable by any other method.

**Weaknesses**:
- Mercury amalgamation recovers only 30-50% of gold and releases ~1000 tonnes/year of mercury to the environment — the largest single-source mercury pollution globally.
- Cyanide is acutely toxic (LD₅₀ 1-3 mg/kg HCN gas) — tailings ponds require double HDPE lining with leak detection, and cyanide destruction (SO₂/air process) before discharge.

### Gold Refining

**Miller chlorination process** (quick, produces 99.5% gold):

Melt doré bullion at 1100-1200°C in a silica or alumina crucible. Pass dry chlorine gas through the melt. Base metals (Cu, Zn, Fe) chlorinate first and volatilize or form a slag. Silver chloride (AgCl) forms and floats on the surface as a crust. Gold chloride (AuCl₃) volatilizes at 180°C but gold is the least reactive — it remains metallic while impurities are removed. Process takes 1-4 hours. Chlorine gas is extremely hazardous — must be handled in enclosed, ventilated systems.

- **Product**: 99.5% gold. Contains residual silver and platinum-group metals.
- **Silver recovery**: AgCl crust is processed separately — leach with Na₂S₂O₃ (sodium thiosulfate) or NaHSO₃ (sodium bisulfite) to dissolve AgCl, then precipitate metallic silver with zinc or electrolytic recovery.

**Wohlwill electrolytic refining** (produces 99.99%+ gold — semiconductor grade):

The highest-purity gold refining process, standard for producing investment-grade and electronics-grade gold.

- **Anode**: Cast impure gold bars (≥95% Au from Miller process), 5-15 kg each, hung in electrolytic cells.
- **Cathode**: Pure gold starter sheet.
- **Electrolyte**: Chloroauric acid solution: H[AuCl₄] in HCl (40-80 g/L Au, 50-100 g/L HCl). Prepared by dissolving gold in aqua regia (see [Mineral Acids](../chemistry/acids.md)) and evaporating to dryness, then redissolving in HCl.
- **Operating conditions**: 60-80°C, current density 500-1000 A/m², cell voltage 0.5-1.5 V. Current efficiency: >99.5%. Energy: ~0.5 kWh per kg Au.
- **Process**: Au → Au³⁺ + 3e⁻ at anode. Au³⁺ + 3e⁻ → Au at cathode. Impurities (Ag, Cu, Pt, Pd) either remain in the anode slime (Ag as AgCl, Pt/Pd as insoluble chlorides) or stay in solution at concentrations too low to co-deposit. Silver is the main interferent — if anode silver exceeds 5%, AgCl forms a passivating crust that blocks dissolution. This is why Miller chlorination (which removes most silver) typically precedes Wohlwill refining.
- **Product**: 99.99%+ gold (four-nines). For semiconductor-grade (five-nines 99.999%), additional zone refining or repeated electrolysis is applied.
- **Anode slime**: Contains platinum, palladium, and residual gold. Processed separately for PGM recovery — a significant revenue stream.

**Aqua regia dissolution and precipitation** (small-scale, analytical, and recycling):

Aqua regia (3:1 HCl:HNO₃ by volume) is the only common reagent that dissolves gold (see [Mineral Acids](../chemistry/acids.md)). Nitric acid oxidizes HCl to generate Cl₂ and NOCl in situ, which attack gold: Au + 3Cl₂ → AuCl₃ (soluble as H[AuCl₄]). Used for dissolving gold from electronic scrap, jewelry, and anode slime.

After dissolution, gold is recovered by:
- **Ferrous sulfate reduction**: FeSO₄ selectively precipitates gold from aqua regia solution. Fe²⁺ reduces Au³⁺ to Au⁰ while being oxidized to Fe³⁺. Other metals remain in solution if conditions are controlled (pH <2, dilute solution). Product: brown metallic gold powder, 99.5-99.9%.
- **Sodium metabisulfite (Na₂S₂O₅) reduction**: SO₂ generated in situ reduces Au³⁺. More selective than ferrous sulfate. Product: 99.9% gold powder.
- **Oxalic acid reduction**: Slow but highly selective. H₂C₂O₄ + 2Au³⁺ → 2CO₂ + 2Au + 2H⁺. Product: 99.99% gold.

**Strengths**:
- Wohlwill electrolytic refining produces 99.99%+ gold (four-nines) — semiconductor-grade purity for wire bonding.
- Miller chlorination is fast (1-4 hours per batch) and removes most base metals and silver in a single step.

**Weaknesses**:
- Wohlwill refining requires chloroauric acid electrolyte (prepared from aqua regia), stable DC power (0.5-1.5 V, 500-1000 A/m²), and anode silver <5% — significant infrastructure.
- Miller chlorination uses dry chlorine gas — extremely hazardous, requires enclosed ventilated systems with NaOH scrubbers.

### Gold Properties and Applications

**Physical properties**:
- Density: 19.32 g/cm³ (one of the densest elements — a 1 kg cube is only 3.7 cm per side)
- Melting point: 1064°C. Boiling point: 2856°C.
- Crystal structure: FCC. Exceptionally ductile — 1 gram of gold can be drawn into a wire 2.4 km long or hammered into a sheet of 0.1 μm thickness (gold leaf).
- Electrical conductivity: 45.2 × 10⁶ S/m (third after silver and copper). Does not oxidize, so contact resistance remains low indefinitely.

**Semiconductor applications**:
- **Wire bonding**: 25 μm (1 mil) diameter gold wire bonds silicon die to package leads. Gold ball bonding: melt wire tip with electric spark (EFO — electronic flame-off), form a ball, thermosonically bond to aluminum bond pad (ultrasonic energy + 200-250°C + pressure), loop wire to lead frame, stitch bond. Wire length: 2-8 mm. Bond strength: 5-10 grams-force. Gold wire is preferred over aluminum for its corrosion resistance and reliable ball formation.
- **Surface finish**: Electroless nickel / immersion gold (ENIG) on PCB pads. Gold layer 0.03-0.08 μm over 3-5 μm nickel. Protects copper from oxidation, provides solderable and wire-bondable surface.
- **Thin-film metallization**: Sputtered or evaporated gold films (0.1-2 μm) for specialized high-reliability contacts, MEMS devices, and RF circuits.

**Strengths**:
- Gold does not oxidize in air at any temperature — contact resistance remains low indefinitely, making it irreplaceable for corrosion-free electrical contacts.
- Exceptional ductility: 1 gram of gold can be drawn into 2.4 km of wire or hammered to 0.1 μm thickness (gold leaf).

**Weaknesses**:
- Gold's density (19.3 g/cm³) and cost limit use to thin-film and wire applications — bulk structural use is impractical.
- Gold is soft (HV ~25 annealed) — unsuitable for wear surfaces without alloying or hardening.

### Silver

Silver (Ag, atomic number 47) has the highest electrical conductivity (63 × 10⁶ S/m) and thermal conductivity of any element. Its primary industrial use is no longer coinage or jewelry (~25%) but photovoltaic solar cells (~30%), electrical contacts (~20%), and electronics (~15%). Modern solar cells consume ~100 mg of silver per cell — at current production rates, this exceeds 100 million ounces per year.

**Geological occurrence**:

Unlike gold, silver rarely occurs as native metal. Most silver is produced as a byproduct of lead-zinc and copper mining. Silver minerals include:
- **Argentite** (Ag₂S, acanthite): The most important silver mineral. Often associated with galena (PbS) in hydrothermal vein deposits. Decomposes to native silver above 179°C.
- **Proustite** (Ag₃AsS₃, "ruby silver") and **pyrargyrite** (Ag₃SbS₃): Deep red translucent minerals, historically prized as mineral specimens. Important in epithermal deposits.
- **Cerargyrite** (AgCl, "horn silver"): Chloride mineral, soft and waxy, found in oxidized zones of silver deposits.
- **Native silver**: Occurs in some deposits (Kongsberg, Norway; Cobalt, Ontario) but rare compared to sulfide minerals.

**Primary production sources**:
- **Lead-zinc byproduct (~35%)**: Galena (PbS) typically carries 0.01-0.5% Ag. Silver is recovered during lead refining via the Parkes process (see [Non-Ferrous Metals](non-ferrous.md)). This is the historically dominant silver source — the Roman economy ran on Spanish silver from lead mines.
- **Copper byproduct (~30%)**: Silver accumulates in copper anode slime during electrolytic copper refining. Anode slime contains 5-25% Ag + Au + PGM, making it the richest precious metal feedstock per unit mass.
- **Primary silver mines (~25%)**: Vein deposits with 200-1000 g/t Ag. Major producers: Mexico, Peru, Poland (Lubin mine), Australia. Typically mined underground.
- **Recycling (~10%)**: Electronic scrap, photographic waste (declining), jewelry, and industrial catalysts.

**Strengths**:
- Silver is overwhelmingly a byproduct metal (65% from lead-zinc and copper operations) — no dedicated silver mining infrastructure needed.
- Highest electrical conductivity (63 × 10⁶ S/m) and thermal conductivity (429 W/(m·K)) of any element.

**Weaknesses**:
- Silver tarnishes in air (Ag₂S from H₂S) — surface degradation affects electrical contact reliability over time.
- Primary silver ore grades (200-1000 g/t) are low relative to base metals, requiring large-scale mining operations.

### Silver Extraction

**Lead ore smelting and Parkes process** (dominant route, see [Non-Ferrous Metals](non-ferrous.md) for full lead smelting details):

Silver is recovered from lead bullion via the Parkes process, which exploits the immiscibility of zinc and silver in molten lead:
1. Add zinc (0.5-2% by weight) to molten lead at 450-480°C. Silver preferentially dissolves in zinc (distribution coefficient Ag:Zn/Pb ≈ 300:1 at 500°C). Gold also partitions into the zinc phase.
2. Zinc-silver-gold crust floats on lead (zinc is lighter, density 7.13 vs. lead 11.34). Skim the crust.
3. Distill zinc from the crust under vacuum at 800-950°C. Zinc vapor condenses and is recycled. Remaining metal is rich in silver and gold ("rich lead").
4. Cupel the rich lead: oxidize remaining lead in a reverberatory furnace at 950-1050°C with air blast. Lead oxidizes to PbO (litharge, which melts and flows away). Silver (and gold) do not oxidize and remain as metallic doré bullion.
5. Recovery: >98% of silver and gold from lead bullion.

**Strengths**:
- Parkes process achieves >98% silver recovery from lead bullion using zinc as a selective extractant — high yield with a simple reagent.
- Copper anode slime treatment recovers silver, gold, and PGM from a waste stream — turning a refinery byproduct into the highest-value feedstock.

**Weaknesses**:
- Parkes process requires zinc metal production and lead smelting — a two-metallurgy dependency chain.
- Copper anode slime processing involves multiple steps (decopperization, selenium removal, doré smelting, electrolysis) — each step requires specialized equipment.

### Silver Refining

**Electrolytic refining (Moebius process)** — the standard for high-purity silver:

- **Anodes**: Cast doré bullion bars in cloth bags (to catch anode slime containing gold and PGM).
- **Cathodes**: Stainless steel sheets (silver strips off mechanically).
- **Electrolyte**: Silver nitrate (AgNO₃) 40-60 g/L Ag in 2-5 g/L HNO₃ (nitric acid). Operating temperature: 25-40°C.
- **Operating conditions**: Current density 150-300 A/m², cell voltage 1.5-2.5 V. Energy: ~0.3 kWh/kg Ag.
- **Product**: 99.95-99.99% silver crystals deposited on cathode. Mechanically stripped every 24-48 hours.
- **Anode slime**: Enriched in gold, palladium, platinum — sent to precious metals refinery.

**Fire refining (for lower purity, 99.5-99.9%)**:

Melt impure silver at 1000-1100°C. Blow air or oxygen through the melt. Base metals oxidize preferentially (Cu, Pb, Zn) and are skimmed as slag. Silver remains metallic. Simple but cannot achieve four-nines purity. Used for jewelry and coinage grade.

**Zone refining** (for semiconductor-grade 99.999%+ silver):

Pass a molten zone along a silver bar (zone refining — same principle as for silicon purification). Impurities segregate to one end of the bar. Multiple passes achieve five-nines (99.999%) or higher purity. Slow and expensive but necessary for semiconductor-grade silver paste used in photovoltaic cells.

**Strengths**:
- Moebius electrolytic refining produces 99.95-99.99% silver at low energy cost (~0.3 kWh/kg Ag).
- Fire refining (99.5-99.9%) is simple and fast — melt and blow air — suitable for coinage and jewelry without electrolytic infrastructure.

**Weaknesses**:
- Zone refining for semiconductor-grade (99.999%+) is slow and expensive — multiple passes needed per bar.
- Moebius process generates anode slime containing gold and PGM that requires separate precious metals refining — adds processing complexity.

### Silver Properties and Applications

**Physical properties**:
- Density: 10.49 g/cm³. Melting point: 961.8°C. Boiling point: 2162°C.
- Crystal structure: FCC. Excellent ductility — can be drawn to wire below 10 μm diameter.
- Electrical conductivity: 63 × 10⁶ S/m — highest of any element. Thermal conductivity: 429 W/(m·K) — also highest.
- Tarnish: Reacts with atmospheric H₂S to form Ag₂S (black tarnish). Does not affect bulk properties but degrades electrical contact surface over time.

**Semiconductor applications**:
- **Photovoltaic metallization**: Screen-printed silver paste (70-85% Ag flakes in glass frit binder) forms the front-side electrical contacts on >95% of crystalline silicon solar cells. Fired at 700-850°C: glass frit etches through SiNₓ anti-reflection coating, silver sintering forms ohmic contact. Silver consumption: ~100 mg per cell (156 × 156 mm). This is the single largest industrial use of silver by volume.
- **Electrical contacts**: Silver and silver alloys (Ag-CdO, Ag-SnO₂, Ag-Ni) for relay and switch contacts. Low contact resistance, high current capacity.
- **Solder and brazing**: Silver-bearing solders (96.5Sn-3.0Ag-0.5Cu, SAC305) are the lead-free solder standard for electronics assembly (see [Non-Ferrous Metals](non-ferrous.md) tin section).
- **RF and high-frequency circuits**: Silver plating on copper traces reduces skin-effect losses at MHz-GHz frequencies. Plating thickness: 2-10 μm.

**Strengths**:
- Silver paste screen-printing metallizes >95% of crystalline silicon solar cells — the single largest industrial use of silver and irreplaceable at scale.
- Lead-free SAC305 solder (96.5Sn-3.0Ag-0.5Cu) provides reliable electronics assembly without toxic lead.

**Weaknesses**:
- Silver tarnish (Ag₂S) increases contact resistance over time — requires protective plating or atmospheres for long-term reliability.
- Solar cell silver consumption (~100 mg/cell) creates ~100 Moz/year demand — supply security concerns as photovoltaic production scales.

### Interdependencies and Bootstrap Sequence

Precious metal production depends heavily on existing metallurgical and chemical infrastructure:

- **Cyanidation** requires NaCN (from sodium carbonate + ammonia + charcoal — or from calcium cyanamide) and lime (CaO from limestone calcination — see [Ceramics](../ceramics/index.md)).
- **Aqua regia refining** requires both HCl and HNO₃ from mineral acid production (see [Mineral Acids](../chemistry/acids.md)).
- **Wohlwill and Moebius electrolytic refining** require stable DC power at controlled voltage and current density (see [Electricity Generation](../energy/electricity.md)).
- **Parkes process** requires zinc metal (see [Non-Ferrous Metals](non-ferrous.md)) and lead smelting infrastructure.
- **Copper anode slime** is only available from electrolytic copper refining (see [Copper & Bronze](copper-bronze.md)).

**Suggested build order**:
1. **Alluvial gold panning and mercury amalgamation** (Years 15-25): Simple gravity recovery and mercury processing. Produces gold for coinage and limited electrical use. Mercury hazard limits scale.
2. **Parkes process silver** (Years 20-30): Requires lead smelting and zinc production. Silver from lead ores becomes available as a byproduct. Enables solder, electrical contacts.
3. **Cyanidation and electrowinning** (Years 25-35): Requires NaCN, lime, activated carbon, and DC power. Industrial-scale gold extraction. Heap leaching for low-grade ores.
4. **Electrolytic refining (Wohlwill, Moebius)** (Years 30-40): Requires stable DC power, aqua regia, silver nitrate electrolyte. Produces four-nines gold and silver suitable for semiconductor packaging.
5. **Semiconductor-grade purity** (Years 40-50): Zone refining, specialized electrolyte management, cleanroom handling. Five-nines gold for wire bonding, five-nines silver paste for solar cells.

**Strengths**:
- Clear 30-year bootstrap sequence from panning to semiconductor-grade — each stage builds on the previous, enabling incremental capability growth.
- Byproduct recovery from lead and copper operations generates revenue from existing infrastructure — no standalone mine required.

**Weaknesses**:
- Cyanidation and electrolytic refining require chemical and electrical infrastructure (NaCN, DC power, HNO₃) not available until mid-bootstrap.
- Semiconductor-grade purity (99.999%+) requires zone refining or repeated electrolysis — slow, expensive, and energy-intensive.

### Safety & Hazards

**Cyanide**:
- NaCN and KCN are acutely toxic. HCN gas (formed when cyanide contacts acid) is lethal at 100-300 ppm in air. Symptoms: headache, dizziness, nausea, convulsions, death within minutes at high concentration.
- **Antidote**: Hydroxocobalamin (vitamin B₁₂ precursor) IV or sodium thiosulfate IV. Cyanide antidote kits must be staged at cyanidation plants.
- **Prevention**: Alkaline pH (>10) prevents HCN volatilization. Cyanide detectors with audible alarms. Full-face SCBA for any potential exposure. Tailings ponds lined with double HDPE with leak detection between layers.
- **Destruction**: SO₂/air process (INCO process) oxidizes CN⁻ to CNO⁻ (cyanate, 100× less toxic) using SO₂ and air with copper catalyst at pH 8-10. Hydrogen peroxide oxidation also effective.

**Mercury**:
- Cumulative neurotoxin. Vapor pressure: 0.0012 mmHg at 20°C — continuously evaporates from exposed surfaces. TLV-TWA: 0.025 mg/m³. Blood mercury >10 μg/dL indicates overexposure.
- **Exposure routes**: Vapor inhalation (most dangerous), ingestion, skin absorption. Methylmercury (formed by bacterial methylation in water) bioaccumulates in aquatic food chains — Minamata disease.
- **Prevention**: Enclosed retort systems with mercury condensers. Activated carbon vapor filters on ventilation. Biological monitoring (blood and urine mercury quarterly for workers). No eating, drinking, or smoking in mercury work areas. Dedicated work clothing laundered on-site.

**Chlorine gas** (Miller chlorination):
- Severe respiratory irritant. TLV-TWA: 0.5 ppm. Immediately dangerous to life at 10 ppm. Forms HCl on contact with moist mucous membranes.
- **Prevention**: Enclosed chlorination furnaces with chlorine gas detection and automatic isolation valves. Scrubber systems (NaOH solution) on exhaust. Full-face SCBA for emergency response.
- **Leak response**: Evacuate upwind. Chlorine is 2.5× denser than air — it accumulates in low-lying areas.

**Nitric acid and nitrogen oxides** (silver electrolysis, aqua regia):
- NO₂ (brown gas) causes delayed pulmonary edema. Symptoms may appear 4-12 hours post-exposure. TLV-TWA: 0.5 ppm (as NO₂).
- All precious metal refining involving nitric acid must be performed under fume extraction with NOx scrubbing.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Metals](./index.md) • [All Domains](../index.md)*
