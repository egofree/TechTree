# Glass Fibers

> **Node ID**: glass.fibers
> **Domain**: [Glass](./index.md)
> **Dependencies**: [`glass`](./index.md), [`glass.advanced`](advanced.md)
> **Enables**: [`electronics.assembly`](../electronics/assembly.md), [`polymers.composites`](../polymers/composites.md)
> **Timeline**: Years 30-45
> **Outputs**: fiberglass, insulation_wool, optical_fiber, composite_reinforcement
> **Critical**: No — glass fibers improve composites and insulation but alternatives (metal, ceramic wool) exist

## Problem

Glass fibers are filaments of glass drawn to diameters of 5-25 μm (a human hair is 50-100 μm). At these dimensions, glass becomes flexible: it can be woven, felted, or chopped and embedded in a polymer matrix to make composite materials. The three main product families are continuous fiberglass (for structural composites), glass wool (for thermal insulation), and optical fiber (for signal transmission).

Each product family uses a different glass composition, forming process, and post-processing, but they all start from the same fundamental principle: molten glass, attenuated to fine filaments by mechanical force, then cooled below its glass transition temperature fast enough to prevent crystallization (devitrification), which would make the fibers brittle and opaque.

The ratio of glass surface area to volume increases by a factor of 10,000-100,000 when going from bulk glass to fiber form. This enormous surface area makes glass fibers chemically active (vulnerable to moisture attack) and is the reason sizing (protective coating) must be applied immediately after forming.

## Prerequisites

- [Glass production](./index.md) — basic glass melting and forming
- [Advanced glass](advanced.md) — specialty glass compositions (E-glass, fused silica)
- [Polymers](../polymers/index.md) — sizing coatings and resin matrices for composites
- [Energy / furnaces](../energy/index.md) — high-temperature melting (1400-1600°C for E-glass)
- [Machine tools](../machine-tools/index.md) — bushing manufacturing and fiber-handling equipment

### Fiberglass Production (Continuous Filament)

Continuous fiberglass begins with molten glass, similar to conventional glassmaking, but the melt composition and forming process differ significantly from container or window glass.

**Glass composition for fiber**:
- **[E-glass](../glossary/e-glass.md)** (electrical grade, the workhorse of fiberglass): 54% SiO₂, 14% Al₂O₃, 22% CaO, 0.5% MgO, 7% B₂O₃, 1% Na₂O/K₂O by weight. The low alkali content gives good electrical resistivity and moisture resistance. Melting point: ~1200°C; working temperature: 1200-1400°C.
- **[S-glass](../glossary/s-glass.md)** (structural grade, higher strength): 65% SiO₂, 25% Al₂O₃, 10% MgO. Tensile strength 40-50% higher than E-glass, but requires higher melting temperature (~1500°C) and more energy to produce. Used in aerospace and ballistic armor.
- The boron in E-glass (B₂O₃) lowers the working temperature and improves fiber-forming properties, but boron is a relatively expensive raw material. Boron-free formulations (called E-CR glass) exist for cost-sensitive applications where the slightly higher working temperature is acceptable.

**[Direct melt process](../glossary/direct-melt-process.md)** (standard industrial method):
- Raw batch materials (silica sand, limestone, alumina, boric acid) are melted in a refractory furnace at 1400-1600°C. The molten glass is refined (bubbles rise and escape over 6-12 hours) and conditioned (temperature stabilized and homogenized) as it flows through channels to the fiber-forming station.
- The melt enters a platinum alloy bushing (the fiber-forming plate). A bushing is a rectangular block of platinum-rhodium alloy (Pt-10% Rh, approximately 100 × 300 mm, 5 mm thick) perforated with 200-8000 precisely sized holes (nozzles or tips), each 0.8-2.0 mm diameter.
- Platinum is used because it withstands molten glass at 1300-1400°C without degrading or contaminating the glass, and it can be precisely machined to maintain nozzle tolerances over months of continuous operation. A single bushing costs tens of thousands of dollars in platinum alone. Platinum is also electrically conductive, allowing the bushing to be heated by passing electric current through it (Joule heating), which provides precise temperature control at the fiber-forming point.
- Gravity and pressure force the molten glass through the nozzles, forming fine streams. These are drawn down (attenuated) to the target diameter by a high-speed winder. Attenuation speed: 50-100 m/s. The glass cools from ~1250°C to below its glass transition temperature (~600°C for E-glass) within a few centimeters of the bushing tip, solidifying into continuous filaments.
- Fiber diameter is controlled by the nozzle diameter, glass flow rate (temperature and head pressure), and winder speed. Typical E-glass fiber: 10-17 μm diameter. The diameter-to-nozzle ratio is roughly 1:100 (a 1.0 mm nozzle produces a 10 μm fiber after attenuation).

**Sizing application**:
- Immediately after forming, fibers pass through a water-based sizing (coating) applicator, typically a roller partially immersed in sizing solution that transfers a thin film to the filaments.
- Sizing serves three purposes: it protects the fragile fibers from abrasion during handling (bare glass fibers abrade each other and lose 50-80% of their strength during weaving), it lubricates the fibers for subsequent processing (weaving, chopping), and it bonds the fiber to the polymer matrix in the final composite through a coupling agent.
- Sizing composition: film-forming polymer (polyvinyl acetate, epoxy, or polyurethane, 2-5% solids), coupling agent (organosilane, 0.2-0.5%), lubricant, and antistatic agent. The specific formulation depends on the intended end use: polyester resin, epoxy, or thermoplastic matrix.
- Without sizing, fiberglass is too fragile for textile processing. The unprotected filaments abrade each other and break during weaving or chopping. Sizing is the critical enabling technology that makes continuous fiberglass commercially viable.

**Collection forms**:
- **Direct roving**: all filaments from one bushing gathered into a single strand and wound onto a spool (5-20 kg per package). Used for pultrusion, filament winding, and weaving.
- **Assembled roving**: multiple strands from different bushings plied together after forming. Thicker, stronger, used for heavy structural composites and gun roving (choppable for spray-up).
- **Chopped strand**: filaments chopped to 3-50 mm length. Mixed into thermoplastic or thermoset compounds for injection molding. Fiber content in the final compound: 10-40% by weight.
- **Chopped strand mat (CSM)**: randomly oriented chopped fibers (25-50 mm long) held together by a powder binder (polyester resin, 3-7% by weight). Supplied in rolls 1-2 m wide. Used in hand lay-up composites. Fiber content in the final laminate: 20-35% by weight. CSM is the cheapest and easiest form of fiberglass to work with.
- **Yarn**: continuous filaments twisted together into a textile yarn (similar to wool or cotton yarn, but made of glass). Can be woven into fine fabrics (100-300 g/m²) for printed circuit board substrates, electrical insulation, and filter fabrics.

### Glass Wool Insulation

Glass wool is a mass of randomly oriented glass fibers, formed into blankets or batts for thermal and acoustic insulation. It is produced by a fundamentally different process than continuous filament, using a centrifugal spinning method that produces short fibers rather than continuous ones.

**Rotary (spinning) process**:
- Molten glass flows into a rotating drum (spinner, 200-400 mm diameter) with thousands of small peripheral holes (1-2 mm diameter). The drum spins at 2000-4000 RPM. Centrifugal force throws the glass through the holes as fine streams.
- The emerging streams are immediately hit by high-velocity air jets (150-300 m/s) and hot combustion gases, which attenuate the glass further into fibers 3-10 μm diameter. A binder spray (aqueous phenolic resin, 5-8% by weight of final product) coats the fibers as they form.
- The fibrous mat falls onto a moving conveyor belt. The conveyor passes through a curing oven at 200-250°C for 2-5 minutes, where the phenolic resin crosslinks (cures), bonding the fibers into a cohesive blanket. The oven also evaporates the water carrier from the binder.

**Properties**:
- Density: 8-50 kg/m³ (lighter grades for wall insulation, denser for pipe insulation, acoustic panels, and HVAC ducts). The density is controlled by the conveyor speed (slower conveyor compresses the mat more, producing a denser product) and the amount of binder applied.
- Thermal conductivity: 0.030-0.040 W/m·K at 25°C (among the best practical insulators; only closed-cell polyurethane foam at 0.020-0.025 W/m·K is significantly better). The insulation works by trapping still air in the inter-fiber spaces; the glass itself conducts heat, but the trapped air cannot convect. Lower density (more trapped air per volume) generally gives lower thermal conductivity, down to about 10 kg/m³, below which convection within the open fiber matrix increases heat transfer.
- Acoustic absorption: glass wool absorbs sound across the 500-4000 Hz frequency range (the range of human speech and most industrial noise). Noise reduction coefficient (NRC) of 0.75-0.95 for 50-100 mm thick panels mounted on a wall. The sound energy is converted to heat by friction as air oscillates in the fiber matrix.
- Maximum service temperature: 250-350°C (limited by the phenolic binder, which begins to oxidize and lose strength). Unbonded glass wool (no resin binder) can withstand 500-600°C and is used in industrial furnace insulation.

**[Phenolic resin production](../glossary/phenolic-resin-production.md)** (bootstrap path):
- Phenol + formaldehyde → phenolic resin (Bakelite-type), catalyzed by acid (HCl or oxalic acid) or base (NaOH). Molar ratio phenol:formaldehyde of 1:1.5-2.0 for resole-type resin (heat-curable, one-stage).
- The resin is diluted to 5-10% solids in water for spray application during wool forming. Acid catalyst (p-toluenesulfonic acid, 1-3% of resin solids) may be added to promote curing in the oven.
- Phenolic resin is the oldest synthetic thermoset polymer (1907). It is fire-resistant (char formation rather than melting), dimensionally stable, and relatively low cost.

### Optical Fiber Basics

Optical fiber transmits light through a thin glass core by total internal reflection. A cladding layer of lower refractive index surrounds the core, keeping the light confined. The physics is straightforward; the manufacturing precision required to achieve it is extreme.

**Preform fabrication (MCVD, Modified Chemical Vapor Deposition)**:
- A high-purity silica tube (20-30 mm ID, 25-35 mm OD, 1-1.5 m long) is mounted in a glass-working lathe that rotates it slowly (10-50 RPM). Reactive gases flow through the tube: SiCl₄ (silicon tetrachloride, carried by oxygen or helium) and GeCl₄ (germanium tetrachloride, for core doping). An external oxy-hydrogen torch traverses the tube length at 100-200 mm/min, heating a narrow zone to 1400-1600°C.
- The gases react at the hot zone: SiCl₄ + O₂ → SiO₂ + 2Cl₂ and GeCl₄ + O₂ → GeO₂ + 2Cl₂. The SiO₂ and GeO₂ deposit on the inner tube wall as a fine soot layer, which sinters to a clear glass as the torch passes. The germanium dopant increases the refractive index of the deposited layer relative to pure silica.
- Multiple passes (50-200) build up the core layers to the target thickness. After deposition, the tube is collapsed by heating to 2000-2200°C in a single pass, so it shrinks inward and fuses into a solid rod: the preform. The preform contains the core-cladding structure at full scale (20-30 mm diameter, same as the original tube OD).
- Preform purity requirements: transition metal contaminants (Fe, Cu, Cr, Ni) must be below 1 ppb because they absorb light at the operating wavelengths (1310 nm and 1550 nm). Hydroxyl ions (OH⁻) must be below 10 ppb because they cause a broad absorption peak near 1383 nm. This drives the use of ultra-pure chemical precursors (distilled SiCl₄, GeCl₄ at 99.9999% purity) and dry oxygen carrier gas.

**Fiber drawing**:
- The preform is loaded into a drawing tower (a vertical furnace assembly, 15-30 m tall). The preform tip is heated to 2000-2200°C in a high-purity graphite resistance furnace (inert argon atmosphere prevents graphite oxidation at these temperatures). The glass softens and a thin strand is pulled downward by a capstan (traction roller).
- Draw speed: 5-20 m/s. The fiber diameter is monitored by a laser micrometer (measuring at 1000+ Hz) with feedback to the furnace temperature and capstan speed. Diameter tolerance: 125 ± 0.5 μm for standard single-mode fiber. A 1 μm error at the preform scale translates to a 0.01 μm error at the fiber scale because the preform is roughly 100× the fiber diameter.
- Core diameter: 8-10 μm (single-mode fiber, for long-distance telecom) or 50-62.5 μm (multimode fiber, for short-distance data links). Cladding: 125 μm outer diameter for both types.
- Immediately after drawing, the fiber passes through a coating applicator. A dual-layer UV-curable acrylate coating is applied (inner soft layer: modulus ~1 MPa, 25-35 μm thick; outer hard layer: modulus ~1000 MPa, 20-30 μm thick) and cured by UV lamps in 0.5-2 seconds. The coating protects the pristine glass surface from moisture and mechanical damage. Bare glass fiber is incredibly strong (tensile strength ~5 GPa, proof-tested at 100 kpsi / ~700 MPa) but degrades rapidly if left uncoated due to moisture-assisted surface flaw growth.

**Signal characteristics**:
- Attenuation: 0.2-0.35 dB/km at 1550 nm wavelength (single-mode). A signal can travel 80-120 km before requiring amplification. For comparison, copper twisted pair attenuates 10-20 dB/km at 1 MHz.
- Bandwidth: single-mode fiber carries >10 Tbps per fiber using wavelength-division multiplexing (WDM, where 80-160 different wavelength channels each carry 10-100 Gbps). Multimode fiber: 1-10 Gbps over 300-500 m.
- Dispersion: different wavelengths travel at slightly different speeds in the fiber (chromatic dispersion). At 1550 nm, standard single-mode fiber has dispersion of ~17 ps/(nm·km). This limits the maximum data rate at a given distance unless dispersion-compensating fiber or electronic equalization is used.

**Alternative preform fabrication methods**:
- **OVDD (Outside Vapor Deposition)**: soot deposited on the outside of a rotating bait rod, then consolidated. Higher throughput than MCVD for large preforms. Used for high-volume single-mode fiber production.
- **VAD (Vapor Axial Deposition)**: soot deposited on the end of a growing porous rod, then consolidated. Allows continuous preform fabrication (no tube size limitation). Developed in Japan, now widely used.

### Specialty Glass Fibers

Beyond standard E-glass and S-glass, several specialty glass fiber types serve niche applications.

**[AR-glass](../glossary/ar-glass.md)** (alkali-resistant):
- Contains ~16% zirconia (ZrO₂) in the glass composition. Standard E-glass degrades in alkaline environments (pH > 12) because the CaO and Al₂O₃ dissolve. Zirconia is chemically inert in alkali, protecting the fiber from attack.
- Primary use: reinforcement of Portland cement (glass fiber reinforced concrete, GFRC). Untreated E-glass in concrete loses 50-80% of its strength within 1-2 years due to alkali attack from the cement paste (pH 12.5-13.5). AR-glass retains >80% strength after 20+ years.

**High-silica and quartz fibers**:
- High-silica fiber: ordinary glass fiber (typically E-glass) is leached in hot hydrochloric acid (HCl, 3-6 mol/L, 60-80°C, 4-12 hours). The acid dissolves the CaO, Al₂O₃, B₂O₃, and alkali oxides, leaving a porous silica skeleton (>95% SiO₂). The leached fiber retains its fibrous form but has lower density (1.5-1.8 g/cm³ vs. 2.5-2.6 for E-glass) and withstands temperatures up to 1000-1100°C (vs. 600°C for E-glass).
- Quartz fiber: drawn from high-purity fused silica (99.99% SiO₂) at extremely high temperatures (>1800°C). Diameter: 9-14 μm. Tensile strength: ~3.6 GPa at room temperature, retains significant strength up to 1000°C. Used in aerospace thermal protection, high-temperature filtration, and radar-transparent radomes.

**Basalt fiber**:
- Made from natural basalt rock (volcanic, typically 45-52% SiO₂, 12-16% Al₂O₃, 6-12% CaO, 6-12% FeO/Fe₂O₃). Crushed basalt is melted at 1400-1500°C and extruded through a platinum-rhodium bushing (similar to E-glass production, but no raw batch mixing required because the rock provides all oxides in roughly the right proportions).
- Tensile strength: 3.0-4.8 GPa (comparable to S-glass). Better alkali resistance than E-glass (but not as good as AR-glass). Operating temperature range: -260 to +700°C. Density: 2.65-2.80 g/cm³ (slightly heavier than E-glass at 2.54-2.60 g/cm³).
- Advantage: single raw material (basalt quarry rock), no chemical additives. Simpler supply chain than E-glass, which requires separate supplies of silica sand, limestone, alumina, and boric acid. Disadvantage: basalt composition varies between quarries and even between layers in the same quarry, causing inconsistent fiber properties and melting behavior.

### Fiber Products for Composites

**Woven roving**:
- Continuous roving woven into a coarse fabric (plain or twill weave, 200-800 g/m² areal weight). Used in hand lay-up and vacuum bagging for boat hulls, tanks, and structural panels. Higher fiber content than CSM (50-60% by weight in the finished laminate), giving better mechanical properties per unit weight.

**Unidirectional tape**:
- All fibers aligned in one direction, held together by a small amount of binder or pre-impregnated with resin (prepreg, typically 30-40% resin by weight). Maximum strength in the fiber direction, minimal strength transverse. Used in aerospace for tailoring stiffness in specific directions (e.g., wing skins with fiber direction aligned to primary load paths).

**Mat and fabric combinations**:
- Some composite laminates alternate layers of CSM (isotropic, cheap, easy to wet out) and woven roving (strong, directional). A typical boat hull laminate: gel coat (surface finish, 0.5-0.8 mm) + CSM + woven roving + CSM + woven roving, built up to 3-8 mm total thickness.
- Fiber content in hand lay-up: 25-35% by weight. In vacuum-bagged lay-up: 40-55%. In pultrusion: 60-70% (the highest of any process). Higher fiber content means stronger and lighter laminate, but harder to achieve because the resin must still wet all fibers completely.

**Veil mat**:
- A very thin (30-50 g/m²) mat of randomly oriented fine glass fibers (10-13 μm diameter), held together with a small amount of binder. Used as a surface layer in composites to create a smooth, resin-rich surface that hides the fiber pattern of the underlying reinforcement. Also used in corrosion-resistant linings for chemical tanks and pipes.

### Health and Safety

Glass fibers pose specific hazards during manufacture and handling that differ from bulk glass.

**Respiratory hazard (during manufacturing)**:
- Fibers smaller than 3 μm diameter and longer than 5 μm are respirable (reach deep lung tissue). Glass wool and special-purpose fine fiberglass can generate such fibers during production. The International Agency for Research on Cancer (IARC) classifies certain refractory ceramic fibers as possibly carcinogenic (Group 2B). Standard E-glass and glass wool are classified as not classifiable as to carcinogenicity (Group 3).
- Protection during manufacturing and cutting: P100 respirator (99.97% filtration at 0.3 μm). Local exhaust ventilation at cutting and trimming stations to capture airborne fibers at source.

**Skin irritation**:
- Glass fibers 5-15 μm diameter do not penetrate skin but cause mechanical irritation (itching, redness, rash) by abrading the skin surface during handling. The irritation is temporary (resolves in 12-48 hours after exposure stops) but severe enough to reduce worker productivity if unprotected.
- Protection: loose-fitting clothing that covers all skin (fibers pass through tight-weave fabrics at the wrist and neck openings). Barrier cream applied to exposed skin (wrists, neck) before handling. Gloves (leather or rubber-coated) for direct handling of raw fiberglass. Wash work clothes separately from other laundry; fibers transfer to other clothing in the wash and cause irritation on subsequent wear.
- Chronic skin exposure can cause contact dermatitis (persistent inflammation). Workers who handle fiberglass daily should use dedicated work clothing that is laundered separately and never worn outside the workplace.

**Eye protection**:
- Safety glasses with side shields when cutting, trimming, or sanding fiberglass. Fibers in the eye cause intense irritation and are difficult to flush out because the sharp fiber ends embed in the conjunctiva. Do not rub the eye; flush with clean water for 15 minutes minimum and seek medical attention if irritation persists.

**Environmental considerations**:
- Glass fiber waste (offcuts, trimmings, production scrap) is inert and non-hazardous in landfill. However, large quantities of glass fiber waste in landfill are bulky and do not decompose. Recycling options: grinding scrap back into cullet for glass melting (requires clean, uncontaminated fiber) or shredding for use as a filler in asphalt and concrete.
- Phenolic binder in glass wool releases formaldehyde during the curing oven step and at low levels throughout the product's life. Modern phenolic resins are formulated for low formaldehyde emission (< 0.05 mg/m³ in standard chamber testing), but older formulations emitted significantly more. Formaldehyde is a known carcinogen (IARC Group 1).

### Quality Control in Fiber Production

Consistent fiber quality is essential for both composite applications (where fiber diameter and strength determine laminate properties) and optical fiber (where diameter tolerance determines splice loss and signal integrity).

**Diameter measurement**:
- Laser diffraction or laser micrometer scanning measures fiber diameter at line speed (50-100 m/s for fiberglass, 5-20 m/s for optical fiber). For continuous filament, diameter must be controlled to ±5% of target. For optical fiber, tolerance is ±0.5 μm on a 125 μm cladding diameter (±0.4%).
- Diameter feedback control: for fiberglass, the winder speed is adjusted based on the laser measurement (faster winder = thinner fiber, slower = thicker). For optical fiber, the furnace temperature and capstan speed are adjusted based on the laser micrometer reading at 1000+ Hz sampling rate.

**Tensile testing**:
- Single filament tensile test: a 20-50 mm gauge length of fiber is loaded in a micro-tensile tester at a strain rate of 1-5%/min. E-glass fibers at 10-17 μm diameter typically show tensile strength of 2.0-3.5 GPa (variability comes from surface flaws; smaller diameter fibers are stronger because they have fewer critical flaws, following Weibull statistics). S-glass: 3.5-4.5 GPa.
- Strand tensile test: a bundle of filaments (typically 100-200 fibers) is tested as a unit. More representative of real-world performance because it includes fiber-to-fiber variability and the effect of sizing on load transfer between filaments.
- Proof testing for optical fiber: the entire fiber length is passed over a pair of small rollers (capstans) under controlled tension (typically 100 kpsi / ~700 MPa). Any section with a critical flaw breaks during proof testing. The break is detected, and the fiber is re-spliced. Proof testing guarantees a minimum strength level for the entire shipped length.

### Composite Manufacturing with Fiberglass

Fiberglass is rarely used as bare fiber. Its value is as reinforcement in a polymer matrix, where the glass fibers carry the mechanical load and the polymer matrix transfers stress between fibers and protects them from damage.

**[Hand lay-up](../glossary/hand-lay-up.md)** (simplest composite method):
- A mold (wood, metal, or existing plug) is coated with mold release wax. A gel coat (pigmented polyester resin, 0.5-0.8 mm thick) is brushed onto the mold surface to create a smooth, colored exterior.
- Layers of CSM or woven roving are laid onto the wet gel coat. Polyester resin (with 1-2% methyl ethyl ketone peroxide catalyst) is brushed or rolled into the fiberglass, saturating the fabric and expelling air bubbles. A washer roller (ridged metal roller) works the resin deep into the fabric and removes entrapped air.
- Layer buildup continues until the target thickness is reached (3-8 mm typical for boat hulls). Cure at room temperature: 2-4 hours for gel, 24 hours for full cure. Post-cure at 60-80°C for 2-4 hours improves mechanical properties by 15-25%.
- Fiber content in hand lay-up: 25-35% by weight. The rest is resin. This is the lowest fiber fraction of any composite process, meaning hand lay-up is resin-heavy and not as strong per unit weight as other methods.

**[Vacuum bag molding](../glossary/vacuum-bag-molding.md)** (higher fiber content, stronger laminates):
- The dry fiberglass layup is placed in the mold, and resin is applied. A flexible plastic bag (nylon film, 50-75 μm thick) is sealed over the entire layup with mastic tape. A vacuum pump (80-95 kPa vacuum) draws the bag down onto the layup, compressing the laminate and squeezing out excess resin and air.
- The vacuum pressure (approximately 1 atm, or 100 kPa) compacts the laminate uniformly, increasing fiber content to 40-55% by weight. The result is a stronger, lighter laminate than hand lay-up. Vacuum also eliminates voids (trapped air pockets) that act as stress concentrators and weaken the laminate.
- Bleeder fabric (polyester felt) and breather fabric (nylon mesh) are placed between the laminate and the bag to absorb excess resin and provide a path for air evacuation to the vacuum port.

**[Pultrusion](../glossary/pultrusion.md)** (continuous profile production):
- Fiberglass rovings are pulled through a resin bath (polyester or epoxy), then through a heated die (chromium-plated steel, 150-200°C, 0.5-1.0 m long) that shapes the composite into a constant cross-section (rod, tube, angle, channel, I-beam). The die cures the resin continuously as the profile passes through at 0.5-3 m/min.
- Pull speed: 0.5-3 m/min. Fiber content: 60-70% by weight (the highest of any composite process, because the die compresses the fiber bundle and squeezes out nearly all excess resin). Produces structural profiles with higher specific strength than steel (strength-to-weight ratio 3-5× steel) and excellent corrosion resistance.
- Pultruded profiles are used as structural members in bridges, building frames, walkways, and chemical plant infrastructure where steel would corrode. A pultruded glass-polyester I-beam (100 × 50 mm) has a flexural strength of 300-500 MPa at a density of 1.8-2.0 g/cm³ (vs. steel at 7.8 g/cm³).

### Key Deliverables

- Continuous fiberglass production (E-glass, direct melt process, platinum bushing)
- Glass wool insulation (rotary process, phenolic binder, thermal properties)
- Optical fiber preform fabrication (MCVD) and fiber drawing
- Fiber products for composite reinforcement (roving, mat, woven fabric, unidirectional tape)
- Composite manufacturing methods (hand lay-up, vacuum bag, pultrusion)
- Sizing chemistry for fiber protection and matrix bonding
- Health and safety protocols for glass fiber manufacturing and handling
- Quality control methodology for fiber diameter and tensile strength

### Cross-References

- **Glass melting furnaces**: [Glass Production](basic.md)
- **Platinum for bushings**: platinum bushings (see [Metals](../metals/non-ferrous.md))
- **Phenolic resin for wool binder**: phenolic resin (see [Polymers](../polymers/thermosets.md))
- **Composite manufacturing with fiberglass**: [composites](../polymers/composites.md)
- **Chemical precursors (SiCl₄, GeCl₄)**: [silicon processing](../silicon/index.md)
- **Silica raw material**: [Glass Composition](basic.md)

### Fiberglass Composite Manufacturing Detail

**Hand layup procedure (step-by-step)**:
1. Prepare the mold surface: apply mold release wax (2 coats, buffed smooth) to prevent the cured laminate from bonding to the mold.
2. Apply gel coat: brush or spray pigmented polyester resin to 0.4-0.6 mm thickness on the mold surface. This forms the smooth, cosmetic exterior of the finished part. Let cure to a tack-free state (30-60 minutes at 20-25°C). The gel coat must be partially cured (tacky, not fully hard) before laying fiberglass — a fully cured gel coat will not bond to the subsequent layers.
3. Lay the first layer of fiberglass (typically CSM, 300-450 g/m²) onto the tacky gel coat. Brush or roll polyester resin (mixed with 1-2% MEKP catalyst by weight) into the mat at approximately 250-400 g resin per m² of fiberglass per layer. Work from the center outward to push air out ahead of the resin.
4. Consolidate with a washer roller (aluminum roller with overlapping disc washers): roll firmly over the wet laminate in overlapping passes to remove trapped air bubbles. Incomplete consolidation leaves voids that reduce laminate strength by 20-40%.
5. Repeat layers: alternate CSM and woven roving layers until the desired thickness is reached (2-10 mm typical for boat hulls, tanks, and panels). Each CSM layer adds approximately 1-1.5 mm; each woven roving layer adds 1-2 mm.
6. Cure at 20-25°C for 24 hours for full room-temperature cure. For improved mechanical properties (15-25% strength gain), post-cure at 60-80°C for 2-4 hours in a warm room or under heat lamps. The elevated temperature drives the polyester crosslinking reaction to completion.

**Typical laminate properties**: A hand layup laminate of 30% E-glass fiber / 70% polyester resin by weight yields tensile strength 80-150 MPa, flexural strength 150-250 MPa, flexural modulus 5-10 GPa, and density 1.4-1.6 g/cm³. By comparison, mild steel has tensile strength 250-400 MPa but density 7.85 g/cm³ — the fiberglass laminate has 4-5× better specific strength (strength per unit weight) than steel.

**Vacuum bag improvements**: Applying vacuum (80-95 kPa) over the hand layup compresses the laminate, squeezing out excess resin and increasing fiber content from 25-35% to 40-55% by weight. The resulting laminate has 30-50% higher flexural strength and 20-30% lower weight than a hand layup of the same thickness. The vacuum also eliminates voids (trapped air) that concentrate stress and initiate cracks.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Fibers breaking during draw | Viscosity too low (glass too hot) or devitrification in bushing | Reduce furnace temperature 10-20°C; clean bushing tips; verify glass composition |
| Fiber diameter inconsistent | Bushing tip wear or temperature gradient across bushing | Replace worn bushing tips; ensure uniform heating across bushing plate |
| Poor resin wetting in composite | Fiber sizing degraded or contaminated | Store fiberglass in dry conditions; use within shelf life (sizing degrades after 12-18 months) |
| Laminate voids (white spots) | Insufficient consolidation — trapped air | Use washer roller thoroughly; apply vacuum bag for critical parts |
| Insulation wool settles over time | Binder content too low or moisture ingress | Increase phenolic binder to 5-8%; install vapor barrier in building envelopes |
| Gel coat not curing | Insufficient MEKP catalyst or cold temperature | Increase catalyst to 2%; ensure workspace ≥18°C; check resin expiration date |

## See Also

- [Basic glass](basic.md) — glass melting and composition fundamentals
- [Advanced glass](advanced.md) — specialty glass compositions
- [Polymers / Composites](../polymers/composites.md) — fiberglass-reinforced polymer materials
- [Electronics / Assembly](../electronics/assembly.md) — PCB substrate materials (fiberglass-epoxy)
- [Ceramics](../ceramics/index.md) — ceramic fiber insulation alternatives
- [Inspection](../optics/inspection.md) — fiber diameter and quality measurement

[← Back to Glass](index.md)
