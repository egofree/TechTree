# Vulcanization & Hardness

> **Node ID**: polymers.rubber.vulcanization
> **Domain**: [Polymers](./index.md)
> **Dependencies**: [`Rubber Production`](rubber.md)
> **Enables**: Various downstream capabilities
> **Timeline**: Years 5-50
> **Outputs**: vulcanized_elastomers, cured_seals, molded_rubber_parts
> **Critical**: No

## Overview

Vulcanization is the chemical process that converts raw, thermoplastic rubber into a durable, elastic, crosslinked elastomer. Raw natural rubber is sticky, softens in heat, and deforms permanently under load. Charles Goodyear discovered in 1839 that heating rubber with sulfur produces a material that snaps back to its original shape, tolerates temperature swings, and resists solvents. The sulfur atoms form bridges (crosslinks) between adjacent polymer chains, tying the tangled mass of long molecules into a three-dimensional network. This network can stretch and recover but cannot flow, because the chains are permanently connected at the crosslink points.

Modern vulcanization uses sophisticated cure packages that go far beyond sulfur alone. Accelerators (MBT, TMTD, CBS, TBBS) speed up the reaction and allow lower cure temperatures. Activators (zinc oxide and stearic acid) form a complex with the accelerator that dramatically increases its effectiveness. Antioxidants and antiozonants protect the cured rubber from environmental degradation. Fillers (carbon black, silica) reinforce the rubber, improving tensile strength, abrasion resistance, and tear resistance by factors of 5 to 10 over the unfilled polymer.

The degree of crosslinking determines the hardness of the finished rubber. Shore A hardness, measured by pressing a spring-loaded indenter into the rubber surface, is the standard scale for elastomers. A rubber band registers about 30 Shore A, a tire tread about 70, and a hard shoe sole about 90. The target hardness is achieved by adjusting the amount of curative, the filler loading, and the cure time. For rubber-to-metal bonded parts (engine mounts, suspension bushings), the hardness must be precisely controlled because it determines the stiffness of the finished assembly.

Crosslink density also affects other properties besides hardness. Higher crosslink density increases modulus (stiffness at a given extension), improves compression set (better elastic recovery after prolonged compression), and reduces elongation at break. Lower crosslink density gives a softer, more extensible rubber with better fatigue resistance in dynamic applications. The compound designer must balance these competing properties to meet the application requirements.

The choice of accelerator also affects the crosslink type and the aged properties of the rubber. Thiazoles (MBT) and sulfenamides (CBS) produce mostly polysulfidic crosslinks that are flexible and give good fatigue resistance but degrade at elevated temperature. Thiurams (TMTD) and dithiocarbamates produce shorter crosslinks that are more thermally stable. The compound designer selects the accelerator system based on the balance of processing safety, cure speed, and aged properties required by the application.

Primary outputs: `vulcanized_elastomers`, `cured_seals`, `molded_rubber_parts`.

## Prerequisites

### Materials

- **Raw rubber**: Natural rubber (NR, polyisoprene) or synthetic rubber (SBR, NBR, EPDM, CR, etc.). The base polymer. Arrives as bales or crumb from the rubber plantation or synthetic rubber plant
- **Sulfur**: The original and still most common crosslinking agent. Forms polysulfidic bridges (C-Sx-C, where x = 1 to 6) between polymer chains. Typical loading: 1.5 to 3.0 phr (parts per hundred rubber). Insoluble sulfur (a polymeric allotrope) is used in tire compounds to prevent sulfur blooming to the surface of uncured calendared sheets
- **Accelerators**: Organic compounds that speed the sulfur vulcanization reaction by orders of magnitude. Without accelerators, sulfur vulcanization requires hours at 140 degrees C; with them, cure times of minutes are achievable. Common types:
  - **MBT** (2-mercaptobenzothiazole): A thiazole accelerator. Broadly used, moderate speed
  - **TMTD** (tetramethylthiuram disulfide): A thiuram accelerator. Fast cure, used as primary or secondary accelerator
  - **CBS** (N-cyclohexyl-2-benzothiazole sulfenamide): A sulfenamide accelerator. Delayed action, gives longer scorch safety (processing time before cure begins)
- **Zinc oxide**: The primary activator. Reacts with stearic acid and the accelerator to form the active crosslinking complex. Typical loading: 3 to 5 phr
- **Stearic acid**: Co-activator with zinc oxide. Also aids dispersion of fillers and acts as a lubricant during mixing. Typical loading: 1 to 3 phr
- **Carbon black**: The dominant reinforcing filler. Particle size (N110 to N990 grades) and structure (DBP absorption) determine the degree of reinforcement. Smaller particles give higher tensile strength and abrasion resistance but make mixing harder. Typical loading: 30 to 80 phr. The N-series designations indicate the nominal surface area: N110 has the smallest particles and highest reinforcement, N990 has the largest particles and is used as a low-cost extender
- **Processing oils**: Plasticizers that soften the compound for easier mixing and lower the viscosity for molding. Aromatic, naphthenic, or paraffinic oils selected for compatibility with the polymer. The oil type must be matched to the polymer: aromatic oils plasticize NBR well but are less effective in EPDM, which prefers paraffinic oils

### Equipment

- **Banbury internal mixer**: A high-shear, batch mixer with two counter-rotating rotors in a confined chamber. The workhorse for rubber compounding. Mixing generates heat, so the rotors and chamber walls are water-cooled. A typical batch is 50 to 200 kg, mixed in 3 to 8 minutes. The Banbury mixer can generate enough shear heat to raise the compound temperature from ambient to 160 degrees C in under 5 minutes, which is why the two-stage mixing process (masterbatch first, curatives second) is essential
- **Two-roll mill**: Two counter-rotating steel rolls with an adjustable gap. Used for sheeting, blending additives into smaller batches, and feeding calenders or extruders. Also useful for adding heat-sensitive curatives to a warm compound without premature cure
- **Compression press or transfer mold**: A heated hydraulic press with mold plates. Compression molding places a pre-cut blank in the open mold, closes the press, and applies heat and pressure. Transfer molding pushes the compound through a runner system into the closed mold cavity. Transfer molding produces less flash and better dimensional consistency than compression molding, but the mold is more complex and expensive
- **Injection molding machine**: For high-volume production of precision rubber parts. A reciprocating screw plasticizes the compound, then injects it into a heated mold. Faster cycle times than compression molding. Injection molding also produces better dimensional consistency because the compound fills the cavity under high pressure, reducing voids and ensuring complete fill of complex geometries
- **Autoclave or hot air oven**: For curing extruded profiles, hoses, and large parts that cannot be molded in a press. The part is wrapped on a mandrel or laid on a bed and cured in a pressurized steam or hot air environment. Autoclave cure is slower than press cure (typically 30 to 90 minutes) but can handle shapes that would be impossible to mold

### Knowledge

- Cure rheology: how to read a moving die rheometer (MDR) curve and interpret scorch time (ts2), optimum cure time (t90), and maximum torque (MH). The MDR curve is the single most important quality control tool in a rubber molding operation. It tells the operator exactly how long to cure the compound and whether the batch is within specification
- Scorch safety: the delay between mixing (when the compound first encounters heat) and the onset of crosslinking. A compound with too little scorch safety begins curing in the mixer or extruder, clogging the equipment
- Accelerator selection: conventional cure systems (high sulfur, low accelerator) give flexible polysulfidic crosslinks. Efficient cure systems (low sulfur, high accelerator) give thermally stable monosulfidic crosslinks. The trade-off is fatigue life versus heat resistance
- Shore hardness and how filler loading, crosslink density, and polymer type interact to determine the final value
- Mixing sequence: why the masterbatch (fillers and plasticizers) is mixed separately from the curatives, and how the two-stage mixing process prevents premature cure during compounding

### Infrastructure

- A mixing room with dust extraction. Carbon black and other fine powders are respiratory hazards and create difficult housekeeping problems. The dust extraction system must be designed with explosion relief vents, because carbon black dust is combustible and can form explosive dust clouds in confined spaces
- A curing area with ventilation for the sulfur dioxide, amine, and other volatiles released during vulcanization. The typical rubber molding shop smells strongly of sulfur compounds. Local exhaust ventilation at each press captures the fumes at the source before they disperse into the workspace. General room ventilation provides backup dilution
- Mold storage and maintenance facilities. Rubber molds require regular cleaning and polishing to maintain surface finish on molded parts. A mold maintenance shop equipped with a bead blaster, polishing bench, and mold repair welding station extends mold life from thousands of cycles to hundreds of thousands
- Temperature-controlled storage for compounded rubber stock. A compound with curatives added has a shelf life of 1 to 4 weeks at room temperature. Refrigerated storage (10 to 15 degrees C) can extend this to 8 weeks. The storage area must be organized by compound batch and production date to ensure FIFO rotation

## Process Description

### Step-by-Step Procedure

1. **Weighing**: Weigh all ingredients per the formulation card. Accuracy matters: a 10 percent error in accelerator loading can shift cure time by 30 percent. Typical compound formulations list 10 to 20 ingredients. Automated weighing systems improve accuracy and reduce dust exposure, but small operations still weigh by hand using calibrated scales
2. **Masterbatch mixing (Banbury)**: Load the raw rubber into the Banbury mixer first. Masticate for 30 to 60 seconds to soften the polymer and increase its plasticity. Add fillers (carbon black, silica), processing oil, zinc oxide, and stearic acid in sequence. Mix at 40 to 80 RPM. The batch temperature rises to 130 to 160 degrees C from shear heating. Dump the batch onto a two-roll mill and sheet it off. This is the masterbatch: a non-curable compound containing everything except the curatives. The two-stage mixing process (masterbatch plus final mix) is essential because the curatives would begin reacting during the high-temperature masterbatch stage
3. **Final mixing (two-roll mill or Banbury)**: Add the masterbatch back to the mill or mixer along with sulfur, accelerators, and any heat-sensitive additives. The temperature must stay below the scorch point of the cure system, typically below 110 degrees C. This step requires care because the compound can begin curing if the temperature gets too high. In large-scale production, the final mix is done on a two-roll mill at lower temperatures rather than in the Banbury, specifically to avoid scorch. The mill also allows the operator to visually inspect the compound for undispersed filler lumps
4. **Shaping**: The compounded rubber is formed to approximate the final shape by extrusion (for profiles, hoses, and tubes), calendering (for sheet and fabric coating), or pre-forming (cutting blanks for compression molding). The shaping step is time-sensitive because the compound is warm from mixing and the scorch clock is running. The shaped preform must reach the mold before scorch begins. In practice, this means the shaping equipment must be located close to the mixing area and the presses
5. **Curing (compression molding)**: Place the pre-formed blank in the mold cavity. Close the press at the set pressure (10 to 20 MPa). Heat the mold to the cure temperature (typically 150 to 180 degrees C). Hold for the calculated cure time. For a 6 mm thick part, a typical cure cycle is 10 minutes at 160 degrees C. Thicker parts need longer because heat must penetrate to the center. The general rule is about 1 minute per mm of thickness at 160 degrees C. Undercure leaves the center soft and spongy. Overcure causes reversion (in natural rubber) or excessive hardness (in synthetics)
6. **Demolding**: Open the press and remove the cured part. The part is hot and still completing crosslinking. Minor flash (rubber that squeezed into the mold parting line) is trimmed by hand or cryogenic deflashing. Cryogenic deflashing uses liquid nitrogen to embrittle the flash, which is then removed by tumbling the parts in a barrel with media. This method is preferred for high-volume production because it is faster and more consistent than hand trimming
7. **Post-cure (optional)**: Some parts, especially those requiring low compression set or high heat resistance, undergo a post-cure in a hot air oven (4 to 24 hours at 150 to 200 degrees C) to complete crosslinking and drive off residual volatiles. Post-cure is standard for peroxide-cured parts, seal applications, and any rubber that will operate at elevated temperature in service. Skipping post-cure on these parts risks outgassing of volatiles during service, which can contaminate sealed systems

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Cure temperature | 140 to 180 degrees C | Higher temperature = faster cure, shorter mold cycle |
| Cure time | 5 to 60 min | Depends on section thickness and cure system |
| Mold pressure | 10 to 20 MPa | Compression molding. Ensures complete cavity fill |
| Sulfur loading | 1.5 to 3.0 phr | Conventional cure systems |
| Accelerator loading | 0.5 to 2.5 phr | Varies by type and desired cure speed |
| Zinc oxide loading | 3 to 5 phr | Activator |
| Carbon black loading | 30 to 80 phr | Reinforcing filler. Higher loading = harder, stiffer compound |
| Scorch time (ts2) | 3 to 10 min at cure temperature | Must exceed processing time at elevated temperature |

The scorch time is the single most critical processing parameter. If ts2 is too short, the compound begins curing during mixing or shaping, clogging equipment and producing scrap. If ts2 is too long, the mold cycle time increases, reducing throughput. The target ts2 for compression molding is typically 3 to 5 minutes at the cure temperature, giving the operator enough time to load the blank and close the press. For injection molding, where the compound is heated by the screw and injected rapidly, ts2 can be shorter (1 to 2 minutes) because the processing time before mold filling is brief.

### Vulcanizate Properties by Compound Design

The properties of vulcanized rubber are determined by the interaction of polymer type, filler loading, crosslink density, and cure system. The tables below show how these variables affect the final material.

**Effect of carbon black loading on natural rubber properties** (conventional sulfur cure, 2.5 phr sulfur, 0.6 phr CBS):

| Carbon Black (phr) | N330 Grade | Shore A Hardness | Tensile Strength (MPa) | 300% Modulus (MPa) | Elongation at Break (%) | Tear Strength (kN/m) | Abrasion Loss (mm³) |
|---------------------|-----------|-----------------|----------------------|--------------------|-----------------------|---------------------|-------------------|
| 0 (gum) | — | 35-40 | 20-28 | 1-2 | 700-800 | 20-30 | 300-500 |
| 20 | N330 | 45-50 | 25-30 | 4-6 | 600-700 | 35-45 | 150-250 |
| 40 | N330 | 55-60 | 28-32 | 8-12 | 500-600 | 45-55 | 80-150 |
| 60 | N330 | 65-72 | 25-30 | 12-18 | 400-500 | 40-50 | 60-120 |
| 80 | N330 | 75-82 | 22-28 | 16-22 | 300-400 | 35-45 | 80-140 |

The tensile strength peaks at 40-50 phr carbon black because the filler reinforcement mechanism relies on polymer chains adsorbing onto the high-surface-area carbon black particles. At moderate loadings, this adsorption creates physical crosslinks that distribute stress across many chains simultaneously. At very high loadings (80 phr), the carbon black particles crowd each other, creating stress concentrations that actually reduce strength. The abrasion loss follows a similar pattern: moderate filler loading gives the best wear resistance because the carbon black particles shield the polymer from direct abrasive contact.

**Effect of crosslink density on properties** (natural rubber, 50 phr N330 carbon black):

| Sulfur (phr) | CBS Accelerator (phr) | Crosslink Type | Shore A Hardness | Tensile Strength (MPa) | Elongation at Break (%) | Compression Set, 22 hr @ 70°C (%) |
|--------------|----------------------|---------------|-----------------|----------------------|-----------------------|----------------------------------|
| 2.5 (CV) | 0.6 | Polysulfidic (x=4-6) | 60-65 | 28-32 | 500-600 | 20-30 |
| 1.5 (semi-EV) | 1.2 | Mixed (x=2-4) | 60-65 | 26-30 | 450-550 | 15-25 |
| 0.5 (EV) | 2.5 | Monosulfidic (x=1) | 60-65 | 24-28 | 400-500 | 10-20 |
| 0 (peroxide) | — | C-C direct | 60-65 | 22-26 | 350-450 | 8-15 |

Note that hardness stays roughly constant across these formulations because the carbon black loading is held at 50 phr in all cases. What changes is the elasticity and heat resistance. The conventional cure (high sulfur, polysulfidic crosslinks) gives the best fatigue resistance because the long, flexible polysulfidic bridges can slide and rearrange under cyclic stress. The peroxide cure (direct C-C bonds) gives the best compression set and heat resistance because carbon-carbon bonds are thermally stable to 250°C, while polysulfidic bonds begin breaking at 120-130°C.

**Cure system selection by application**:

| Application | Cure System | Crosslink Type | Sulfur (phr) | Accelerator (phr) | Key Property |
|-------------|-----------|---------------|-------------|-------------------|-------------|
| Tire tread | CV | Polysulfidic | 2.0-2.5 | 0.5-1.0 (CBS/TBBS) | Fatigue life, flex resistance |
| Tire sidewall | CV | Polysulfidic | 2.0-2.5 | 0.5-1.0 (CBS) | Flex fatigue, cut resistance |
| O-ring, oil seal | Semi-EV | Mixed | 1.0-1.5 | 1.0-2.0 (TMTD+CBS) | Compression set, oil resistance |
| Engine mount | EV | Monosulfidic | 0.3-0.8 | 2.0-3.0 (TMTD+CBS) | Heat aging, dynamic properties |
| High-temp hose | Peroxide | C-C direct | 0 | DCP 1.5-3.0 phr | Temperature resistance |
| Silicone seal | Peroxide or Pt | C-C or Si-H | 0 | Peroxide or Pt complex | Wide temperature range |
| Neoprene wetsuit | Metal oxide | Ionic (Cl bridges) | 0 | MgO 4 + ZnO 5 phr | Flame resistance, flexibility |

**Typical cure schedules by part thickness**:

Cure time scales with section thickness because heat must penetrate to the center. Rubber is a thermal insulator (thermal conductivity ~0.15 W/m·K, similar to wood), so the center of a thick part heats slowly.

| Section Thickness | Cure at 150°C | Cure at 160°C | Cure at 170°C | Notes |
|-------------------|--------------|--------------|--------------|-------|
| 2 mm | 4-6 min | 3-4 min | 2-3 min | Thin parts cure fast |
| 5 mm | 7-10 min | 5-7 min | 4-5 min | Standard O-ring thickness |
| 10 mm | 12-18 min | 8-12 min | 6-8 min | Rule: ~1 min/mm at 160°C |
| 20 mm | 20-30 min | 15-20 min | 10-15 min | Thick seals, engine mounts |
| 50 mm | 45-60 min | 30-45 min | 20-30 min | Large bushings, dock fenders |
| 100 mm | 90-120 min | 60-90 min | 45-60 min | Solid tires, large rollers |

Undercure is the most common defect in thick rubber parts. The outer surface cures first and acts as insulation, slowing heat penetration to the center. A part that feels firm on the outside may have a spongy, uncured core. Test by slicing through the thickest section and pressing the cut surface with a fingernail: if the center indents easily and feels tacky, it is undercured. Undercure reduces tensile strength by 30-60% and compression set by 50-80%.

## Safety Considerations

- **Sulfur dioxide fumes**: Vulcanization releases SO2, especially from sulfur-rich cure systems. SO2 is a respiratory irritant that causes coughing and bronchospasm at moderate concentrations. Curing areas must have local exhaust ventilation at the press. The characteristic rotten-egg smell of a rubber factory comes from trace sulfur compounds released during curing. At the concentrations typically encountered in a well-ventilated molding shop, SO2 is an irritant but not a acute health hazard. Chronic exposure at higher concentrations can cause bronchitis
- **Accelerator sensitization**: Many rubber accelerators (especially thiazoles and thiurams) are skin sensitizers that cause allergic contact dermatitis after repeated exposure. The allergy is persistent and may last for years after exposure ceases. Workers handling accelerators must wear gloves and avoid skin contact. Once sensitized, the affected worker cannot handle the chemical again without a reaction. This is one of the most common occupational health issues in the rubber industry
- **Hot rubber burns**: Demolded parts are at 150+ degrees C. The rubber itself, the mold, and the flash are all burn hazards. Insulated gloves and tools are mandatory during demolding. The mold surface can exceed 180 degrees C. Burns from contact with the mold or freshly demolded parts are deep because rubber is a poor thermal conductor, meaning the surface stays hot for a long time
- **Molding press crush hazard**: Hydraulic presses generate 10 to 20 MPa of pressure. A hand caught in a closing mold will be crushed. Two-hand trip systems, light curtains, or interlocking guards must prevent press operation while hands are in the mold area
- **Dust from carbon black and fillers**: Carbon black is classified as IARC Group 2B (possible carcinogen). The fine dust is a respiratory hazard. Weighing and mixing operations must use local exhaust ventilation, and workers must wear respirators. Silica filler dust presents a silicosis hazard similar to that in ceramics and mining. The Banbury mixer should be charged with fillers using a closed feed system rather than hand-weighing and manual dumping

### Personal Protective Equipment

- **Nitrile gloves when weighing and handling accelerators, sulfur, and other compounding chemicals. The gloves should be replaced frequently because some accelerators can permeate nitrile over time
- **Heat-resistant gloves (Kevlar or aramid) for demolding hot parts. The gloves should be long enough to protect the forearms from contact with the hot mold platen
- **Safety glasses with side shields in the mixing and molding areas. Rubber compound can splash during mixing and hot rubber can fly during demolding of pressure-filled parts
- **N95 or P100 respirator when handling carbon black, silica, or other dusty fillers. The respirator must be fit-tested for each worker. Facial hair prevents a proper seal and is generally prohibited in rubber compounding areas
- **Steel-toe boots with metatarsal protection near presses and heavy molds. The metatarsal guard protects the foot from falling mold components and heavy rubber bales

### Emergency Procedures

- Press entrapment: all presses must have an emergency stop and a means to open the press under load. Workers must be trained in the emergency release procedure
- Sulfur fire: sulfur burns to produce SO2. Fight with dry chemical or CO2. Do not use water on molten sulfur (steam explosion risk). Evacuate and ventilate
- Chemical spill (accelerator or solvent): contain with absorbent, collect for hazardous waste. Avoid skin contact during cleanup

## Quality Control

### Acceptance Criteria

- **Vulcanized elastomers**: Tensile strength, elongation at break, and Shore A hardness within specification for the compound grade. Compression set below the maximum specified value (typically 20 to 35 percent after 22 hours at 70 degrees C)
- **Cured seals**: Dimensional conformance to drawing tolerances (typically plus or minus 0.1 to 0.5 mm). No visible flash, porosity, or surface defects. Durometer hardness within 5 Shore A points of target
- **Molded rubber parts**: Complete fill of all mold cavities. No short-shots (incomplete fill) or knit lines (visible seams where flow fronts meet). Hardness and tensile properties on grade

The rubber industry uses statistical process control (SPC) extensively because rubber compound properties are sensitive to small variations in mixing time, ingredient weighing accuracy, and cure conditions. A control chart tracking Shore A hardness across shifts will reveal gradual drift before it produces out-of-specification parts. Tensile strength and elongation at break are tested less frequently (typically one slab per batch per day) but serve as the definitive confirmation that the compound and cure schedule are correct.

### Testing Methods

- **Shore A durometer**: Press the spring-loaded indenter into a flat surface of the cured rubber. Read hardness directly. The most common daily quality check. Take readings at three points and average

Hardness testing with a durometer is quick, non-destructive, and can be performed on the actual production part. However, the reading is sensitive to the thickness of the sample (thin parts read harder because the indenter hits the backing surface), the flatness of the test area, and the force applied. ASTM D2240 specifies a minimum sample thickness of 6 mm for reliable readings. When testing thin parts, the sample must be stacked to reach the minimum thickness.

- **Stress-strain testing (ASTM D412)**: Die-cut a dumbbell specimen from a cured sheet. Pull in a tensile tester until break. Report tensile strength (MPa), elongation at break (percent), and modulus at 100 and 300 percent elongation. The fundamental mechanical test for rubber. The shape of the stress-strain curve reveals information about the filler reinforcement and crosslink density. A well-filled, properly cured rubber shows a steeply rising curve (strain-induced crystallization in natural rubber compounds) while an undercured or unfilled compound shows a flat, extensible curve
- **Compression set (ASTM D395)**: Compress a cylindrical specimen to 25 percent of its original height, hold at elevated temperature for 22 hours, release, and measure the permanent deformation. Low compression set means the seal will spring back after long-term compression. Critical for O-rings and gaskets. The test temperature is chosen to match the service temperature: 70 degrees C for general-purpose seals, 100 degrees C for underhood automotive, 150 degrees C for engine and transmission seals. A compression set below 20 percent indicates a well-cured, properly formulated compound. Values above 35 percent suggest undercure, insufficient crosslink density, or poor filler-polymer bonding
- **Cure rheometer (MDR, ASTM D5289)**: A small sample of uncured compound is heated between two oscillating dies. The torque increases as crosslinking proceeds. The MDR curve shows scorch time (onset of cure), t90 (time to 90 percent of maximum crosslink density), and MH (maximum torque, related to crosslink density). This test defines the cure schedule for production molding
- **Visual inspection**: Check molded parts for flash, porosity, short-shots, knit lines, and surface blemishes. Optical comparators or machine vision systems for high-volume production

### Sampling Protocol

- Test every compound batch with the MDR before release to the molding floor. A failed MDR (cure time outside the specification window) means the batch is rejected or adjusted. The MDR test takes about 15 minutes and is the gate between compounding and production
- Measure Shore A hardness on the first three parts from each mold at the start of every shift. Record the values on a control chart. Trends in hardness reveal gradual changes in compound formulation or cure conditions before they produce out-of-spec parts
- Perform tensile testing and compression set testing on one cured slab per compound batch per day. These tests take longer than hardness testing (30 to 60 minutes for tensile, 22 hours for compression set) but provide the definitive confirmation that the compound and cure schedule are producing the intended properties
- Visual inspection of every molded part (or statistical sampling for high-volume items, with AQL limits). Automated optical inspection is increasingly common for high-volume parts, but experienced inspectors can detect subtle defects that machines miss, particularly knit lines and incomplete fill at the ends of the runner system

## Scaling Notes

Vulcanization scales from hand-pressed prototypes to fully automated injection lines. The key difference between scales is not the chemistry (which is the same at every scale) but the tooling investment, automation level, and throughput per operator.

- **Bench scale**: A small heated platen press (10 to 20 tons) with hand-loaded molds. Cure cycles of 10 to 20 minutes. Output: a few dozen parts per hour. Suitable for prototyping, formulation development, and low-volume specialty seals
- **Pilot scale**: A 50 to 200 ton hydraulic press with multiple cavities. Semi-automatic operation (operator loads blanks, press closes on timer, operator demolds). Output: 100 to 500 parts per hour depending on part size and cure time
- **Production scale (compression/transfer molding)**: A battery of 200 to 1000 ton presses, each running multi-cavity molds. Automatic loading and demolding by robotic extractors. Output: thousands of parts per hour per press line
- **Production scale (injection molding)**: Rubber injection machines (500 to 2000 tons) with screw pre-plasticization. Cycle times of 1 to 5 minutes for small parts. Highest throughput and best dimensional consistency. Tooling cost is higher than compression molds
- **Continuous vulcanization**: For extruded profiles (weatherstripping, hoses), the extrudate passes directly into a salt bath, microwave tunnel, or fluidized bed for continuous cure. No mold. Throughput: meters per minute. The standard for seal and gasket profiles

Key scaling challenges: cure time does not decrease with scale (it is set by chemistry and section thickness). Throughput increases come from more cavities, more presses, or faster curing formulations, not from running the same cure faster. Heat transfer to the center of thick parts is the fundamental rate-limiting step.

Mold design is an underappreciated scaling factor. A single-cavity mold for a prototype O-ring is straightforward to machine from tool steel. A 64-cavity mold for mass-producing the same O-ring requires precise cavity-to-cavity dimensional control (within 0.05 mm), balanced runner systems that deliver equal compound volume to each cavity, and uniform heating across the entire mold face. The runner system in a multi-cavity mold must be designed so that the compound reaches all cavities at the same time and pressure. If one cavity fills before the others, it begins curing while the rest are still filling, producing parts with different crosslink densities from the same molding cycle.

Compound shelf life limits production flexibility. A compounded rubber stock (with curatives added) begins to crosslink at room temperature, a process called scorch progression. The shelf life of a typical compound is 1 to 4 weeks depending on the cure system. This means that compounding and molding must be coordinated: the compound must be produced and shipped to the molding floor within its scorch window. Large factories solve this by compounding and molding on the same site, with just-in-time delivery of compound to the presses. Smaller operations buy pre-compounded material from a custom compounder and must plan their production schedule around the delivery date. A single-cavity mold for a prototype O-ring is straightforward to machine. A 64-cavity mold for mass-producing the same O-ring requires precise cavity-to-cavity dimensional control, balanced runner systems that deliver equal compound volume to each cavity, and uniform heating across the entire mold face. The mold cost can exceed the press cost for high-volume production. Mold design for rubber is a specialized skill because the compound flows as a non-Newtonian fluid during filling, and the cure generates volatiles that must be vented.

Compound shelf life limits production flexibility. A compounded rubber stock (with curatives added) begins to crosslink at room temperature, a process called scorch. The shelf life of a typical compound is 1 to 4 weeks depending on the cure system. This means that compounding and molding must be coordinated: the compound must be produced and shipped to the molding floor within its scorch window. Large factories solve this by compounding and molding on the same site, with just-in-time delivery of compound to the presses. Refrigerated storage (10 to 15 degrees C) can extend shelf life to 8 weeks, but the compound must be warmed to room temperature before processing, adding a 24-hour delay.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Porosity (bubbles in molded part) | Trapped air or moisture in the compound. Insufficient mold venting | Dry compound before use. Add vent grooves to the mold. Increase press closing speed to push air out. Pre-warm the blank |
| Undercure (spongy, weak parts) | Cure time too short, mold temperature too low, or insufficient curative | Check MDR cure curve. Increase cure time by 2 to 5 minutes. Verify mold thermocouple calibration. Check that curative was actually added during final mixing |
| Reversion (overcure of natural rubber) | Natural rubber degrades at prolonged high temperature, breaking crosslinks and softening | Reduce cure time or temperature. Switch to an efficient vulcanization (EV) system with more stable monosulfidic crosslinks. Consider using synthetic rubber (SBR or BR) which is less prone to reversion |
| Flash too thick | Mold closing pressure too low, or mold faces worn | Increase press pressure. Inspect mold parting faces for wear and refinish if needed. Check blank weight (overfilling forces excess flash) |
| Blooming (white powder on surface) | Excess sulfur or accelerator that did not react during cure migrates to the surface | Reduce curative loading. Ensure adequate cure time for complete reaction. Use soluble accelerators that stay in solution |
| Poor bonding to metal inserts | Contaminated insert surface or inadequate adhesive | Clean inserts with solvent or abrasive blasting. Apply a brass plating or rubber-to-metal bonding agent (Chemlok or similar primer/cement system) |
| Backrinding (tears at the mold parting line) | Rubber expanding during the early stages of cure before crosslinking stabilizes the structure | Reduce the molding temperature and extend the cure time. Pre-warm the blank to reduce the thermal shock. Redesign the parting line to position it in a low-stress area |
| Air trapping (voids in thick sections) | Air cannot escape from the mold cavity before the rubber cures and seals the vent channels | Redesign the mold with additional vents. Use transfer molding instead of compression molding to push air out ahead of the flowing compound. Apply vacuum assist to the mold during closing |
| Surface roughness (orange peel texture) | Compound viscosity too high for the mold temperature, causing turbulent flow and trapped air at the cavity surface | Lower the compound Mooney viscosity by adjusting the formulation. Increase the mold temperature to reduce compound viscosity during filling. Ensure the mold surface is polished and clean |

Troubleshooting rubber molding problems requires a systematic approach because the same defect can have multiple root causes. The starting point is always the cure rheometer (MDR) trace: if the MDR shows the compound is in specification, the problem is likely in the molding process (temperature, pressure, venting, or loading). If the MDR is out of specification, the problem is in the compound (ingredient weighing error, mixing problem, or raw material variation). Changing the molding parameters to compensate for a compound problem is a temporary fix at best.

## Variations and Alternatives

- **Conventional vulcanization (CV)**: High sulfur (2 to 3.5 phr), low accelerator. Produces polysulfidic crosslinks (C-Sx-C, x = 4 to 6). Flexible, good fatigue life, but poor heat aging. Used for tires, belts, and dynamic applications where the rubber must flex millions of times without cracking. The long polysulfidic crosslinks can slide and rearrange under stress, distributing the load and resisting fatigue initiation
- **Efficient vulcanization (EV)**: Low sulfur (0.3 to 0.8 phr), high accelerator. Produces mostly monosulfidic crosslinks (C-S-C). Thermally stable, good compression set, but less flexible. Used for seals, O-rings, and static applications requiring heat resistance
- **Semi-efficient vulcanization (semi-EV)**: Moderate sulfur (1.0 to 1.5 phr), moderate accelerator. A compromise between CV and EV. The most common system for general-purpose molded goods
- **Peroxide cure**: Organic peroxides (dicumyl peroxide, DBPH) generate carbon-centered radicals that form direct C-C crosslinks. No sulfur needed. Excellent heat aging and compression set. Used for silicone rubber, EPDM, and specialty elastomers. Cannot be used with natural rubber (causes chain scission instead of crosslinking). Peroxide-cured compounds have a characteristic odor during molding from the decomposition products of the peroxide
- **Radiation cure**: Electron beam or gamma radiation crosslinks rubber without heat or chemicals. Used for wire and cable insulation where a clean, peroxide-free cure is needed. High capital cost for the radiation source, but no cure byproducts and very fast throughput. The crosslinks produced by radiation are direct C-C bonds, giving excellent thermal stability
- **Metal oxide cure**: Magnesium oxide or zinc oxide crosslinks chlorine-containing rubbers (neoprene, chlorosulfonated polyethylene). The metal oxide reacts with the chlorine to form crosslinks. Specific to halogenated polymers. Neoprene compounds typically use a combination of magnesium oxide and zinc oxide, with MgO providing scorch resistance and ZnO providing cure activity
- **Urethane cure (DIAS/MDI systems)**: Quinonedioxime or diphenylmethane diisocyanate systems produce crosslinks with good heat aging and excellent dynamic properties. Used in high-performance automotive bushings and engine mounts where the sulfur cure would not survive the underhood temperatures. The urethane crosslinks are more thermally stable than polysulfidic sulfur crosslinks but less stable than peroxide C-C crosslinks
- **Resin cure (phenolic resin)**: Alkylphenol-formaldehyde resins crosslink butyl rubber (IIR) and EPDM. The resin cure produces non-staining, heat-resistant crosslinks. Used for tire inner liners and curing bladders where the sulfur system would stain adjacent white sidewall compound. The phenolic resin is typically used at 3 to 10 phr and requires a tin chloride or other Lewis acid activator

The choice of cure system is driven by the application requirements and the rubber type. Natural rubber is compatible with all sulfur cure systems. Synthetic rubbers vary: EPDM requires a sulfur or peroxide cure (its saturated backbone has no double bonds for sulfur to attack directly, so the cure relies on the small amount of diene monomer incorporated as a crosslink site). Silicone rubber is always peroxide-cured or platinum-cured. Neoprene uses a metal oxide cure. Using the wrong cure system for a given polymer results in undercure, poor properties, or no cure at all. The cure system selection is therefore one of the first decisions in compound design, made before any other formulation work begins.

## References

- [Rubber Production](rubber.md) — parent capability
- [Polymers Domain](./index.md) — domain overview and related capabilities
- [Rubber Production](rubber.md) — upstream dependency (tool) - the raw rubber and compounding knowledge from the parent capability are prerequisites for all vulcanization work



---

*Part of the [Bootciv Tech Tree](../index.md) · [Polymers](./index.md) · [All Domains](../index.md)*

![polymers vulcanization](../images/polymers/polymers_vulcanization.jpg)
