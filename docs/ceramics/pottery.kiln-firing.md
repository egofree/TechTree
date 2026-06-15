# Kiln Firing

> **Node ID**: ceramics.pottery.kiln-firing
> **Domain**: [Ceramics](./index.md)
> **Dependencies**: See prerequisites
> **Enables**: [`Charcoal Production`](../energy/charcoal.md)
> **Timeline**: Years 0-10
> **Outputs**: fired_ceramics
> **Critical**: No

## Overview

Kiln firing transforms dried clay objects into permanent ceramic by driving them through a carefully controlled temperature schedule. The heat expels chemically bound water, burns out organic matter, and triggers sintering reactions that partially vitrify the clay body. Bisque firing, the first pass at pyrometric cone 08 through cone 04 (roughly 950 to 1060 degrees C), produces porous ware that can absorb glaze. Glaze firing, the second pass at cone 6 through cone 10 (1220 to 1300 degrees C), melts the glaze coating and matures the clay body to its final density.

The three traditional clay body categories, earthenware, stoneware, and porcelain, each fire to different temperature ranges and produce ceramics with distinct properties. Earthenware fires at the lowest temperature (cone 04 to cone 02) and remains porous after firing. It is the easiest to work with but the least durable. Stoneware fires at cone 6 to cone 10, vitrifying to a dense, non-porous body that holds water without glazing. Porcelain fires at cone 10 to cone 12 and vitrifies completely, becoming translucent at thin sections. Each body type requires its own family of glazes formulated to match the firing temperature and thermal expansion of the clay.

The temperature schedule matters more than most beginners expect. Heating too fast through the quartz inversion zone around 573 degrees C causes thermal shock that cracks pieces. The water-smoking phase between 100 and 300 degrees C must proceed slowly enough to drive off mechanical water without generating steam pressure inside the walls. A typical bisque schedule ramps at 60 to 100 degrees C per hour through the danger zones, then accelerates to 150 degrees C per hour above 600 degrees C. Soak time at peak temperature, usually 15 to 30 minutes, lets the kiln equalize and ensures uniform maturity across all pieces.

Atmosphere control separates functional pottery from decorative failure. An oxidation atmosphere, with excess oxygen, burns out carbon cleanly and produces bright, consistent glaze colors. A reduction atmosphere, achieved by restricting air intake, starves the flame and forces it to pull oxygen from the clay and glaze itself. This converts iron from Fe3+ to Fe2+, shifting glazes from brown-red to blue-green and producing the celebrated celadon and tenmoku effects. Wood-fired kilns naturally oscillate between oxidation and reduction as fuel is stoked, creating unpredictable surface variation that potters prize.

The body-glaze fit is another critical relationship. When the glaze and clay body have matched thermal expansion coefficients, the glaze adheres smoothly to the surface. If the glaze shrinks more than the body on cooling (high thermal expansion), it develops a network of fine cracks called crazing. If the glaze shrinks less (low thermal expansion), it is put into compression and can pop off in flakes, a defect called shivering. Achieving body-glaze fit requires matching the silica and flux content of the glaze to the composition and firing temperature of the clay body. This is why each clay body typically has a family of glaze recipes calibrated to it.

The type of kiln determines what is possible. An electric kiln in a studio can only fire in oxidation, which limits glaze effects but gives reliable, repeatable results. A gas downdraft kiln can shift between oxidation and reduction at will, giving the potter control over iron, copper, and celadon glazes. A wood-fired anagama kiln cannot be precisely controlled at all, but the ash that lands on the ware during a multi-day firing melts into a natural glaze that no other method can reproduce.

The chemical transformations during firing follow a predictable sequence. Below 100 degrees C, mechanical water evaporates. Between 200 and 450 degrees C, chemically bound water (the hydroxyl groups attached to clay mineral surfaces) is driven off. Around 350 degrees C, organic matter (humus, root fragments, carbon from decomposed plant material) oxidizes to CO2. Sulfur compounds decompose between 400 and 800 degrees C, releasing SO2. At 573 degrees C, the quartz inversion occurs. Above 600 degrees C, the clay minerals begin to decompose and reform into new crystalline phases (mullite begins to form above 1000 degrees C). At the peak firing temperature, partial melting produces a glassy phase that fills the pores between the remaining crystalline particles, a process called vitrification.

Even with modern programmable controllers, kiln firing retains an element of craft judgment. No two firings are identical. Atmospheric conditions, the moisture content of the ware, how tightly the kiln is stacked, and the age of the heating elements all affect the outcome. Experienced potters learn to read the color of the kiln interior through the spy hole, the sound of the burners, and the smell of the exhaust to make real-time adjustments that no program can replicate.

Primary outputs: `fired_ceramics`.

## Prerequisites

### Materials

- **Clay body**: A formulated blend of ball clay, kaolin, silica, and feldspar. Earthenware bodies mature around cone 04 to cone 02, stoneware at cone 6 to cone 10, porcelain at cone 10 to cone 12
- **Glaze materials**: Silica (glass former), feldspar (flux), whiting or dolomite (secondary flux), kaolin (suspending agent), plus colorants such as iron oxide, copper carbonate, cobalt carbonate, or rutile
- **Kiln wash**: Alumina hydrate mixed with kaolin, painted onto kiln shelves to prevent glaze drips from fusing ware permanently to the shelf. Kiln wash should be reapplied before each glaze firing. Old, cracked kiln wash should be scraped off and replaced
- **Fuel**: Wood, charcoal, propane, or natural gas. Electric kilns use resistance heating elements instead of combustion fuel. The choice of fuel affects both the maximum temperature achievable and the atmosphere inside the kiln

### Equipment

- **Kiln**: The furnace itself. Options range from a simple pit or bonfire for earthenware, through updraft and downdraft brick kilns for stoneware, to programmable electric kilns for precise glaze firing. Electric kilns are the most common in modern studios due to their ease of use and precise temperature control
- **Kiln furniture**: Cordierite or silicon carbide shelves, posts of various heights, and stilts that support ware inside the kiln. Shelves must be rated for the target temperature. Silicon carbide shelves are more expensive but conduct heat better and last longer at stoneware temperatures than cordierite
- **Pyrometric cones**: Small triangular pyramids of formulated ceramic that soften and bend at known temperatures. Cones measure heatwork, the combined effect of temperature and time, not just peak temperature. A cone 6 pack in the kiln confirms that the load received a full cone 6 firing. Orton cones (the dominant brand) are available in a full range from cone 022 (600 degrees C) to cone 42 (1500 degrees C)
- **Burner system**: For gas or oil kilns, venturi or forced-air burners with adjustable gas valves. Burner size and count determine maximum temperature and how finely the atmosphere can be controlled. Forced-air burners provide better control than venturi types because the air-fuel ratio can be adjusted independently
- **Thermocouple or pyrometer**: A digital readout from a thermocouple probe inside the kiln. Useful for tracking the firing schedule, though cones remain the gold standard for confirming maturity. Type K thermocouples are common and affordable but drift over time at high temperatures. Type S (platinum-rhodium) thermocouples are more accurate but far more expensive

### Knowledge

- Reading pyrometric cones and interpreting bend angle to judge heatwork
- Understanding clay body shrinkage and the quartz inversion at 573 degrees C that makes fast ramping through that zone dangerous
- Glaze chemistry basics: how silica, alumina, and flux ratios determine melting temperature and surface quality. The Stull chart maps glaze compositions onto a grid of mat, glossy, or running surfaces based on the alumina-to-silica ratio
- Atmosphere control: adjusting damper and burner settings to achieve oxidation or reduction at the right moment in the firing cycle
- Loading strategy: arranging ware to maximize kiln capacity while maintaining even heat circulation. Tight stacking blocks flame paths and creates cold spots

### Infrastructure

- A sheltered firing area with at least 3 meters of clearance from combustible structures. Kilns radiate intense heat and their exhaust contains carbon monoxide
- Ventilation for fuel-burning kilns: natural draft through a chimney, or forced ventilation. Indoor electric kilns also need ventilation to remove fumes from burning organics in the clay
- A dry storage area for unfired ware. Pieces entering the kiln must be bone dry. Even slight residual moisture causes steam explosions during early heating. In humid climates, pieces may need to be stored in a warm, dry area for several days before firing to ensure complete drying

## Clay Body Compositions

The three traditional clay body families differ in their raw material ratios, firing temperature, and fired properties. Each body is a blend of plastic clays (which provide workability), non-plastic fillers (silica, which controls shrinkage and thermal expansion), and fluxes (feldspar, which lowers the maturing temperature).

| Component | Earthenware (cone 04-02) | Stoneware (cone 6-10) | Porcelain (cone 10-12) |
|-----------|-------------------------|----------------------|----------------------|
| Ball clay | 40-50% | 25-35% | 0% |
| Kaolin | 0-10% | 20-30% | 45-55% |
| Silica (flint, 200 mesh) | 20-30% | 15-25% | 20-30% |
| Feldspar (potash or soda) | 10-15% | 15-20% | 20-30% |
| Red clay or fireclay | 10-20% | 0-15% | 0% |
| Grog (optional) | 0-10% | 0-15% | 0% |
| Firing range | 999-1120 degrees C | 1222-1305 degrees C | 1305-1325 degrees C |
| Fired absorption | 8-15% | 1-3% | Less than 1% |
| Total shrinkage (dry + fired) | 8-12% | 10-14% | 12-18% |
| Fired color | Red, tan, or buff | Gray, brown, or white | White, translucent when thin |

**Earthenware body (cone 04, ~1060 degrees C)**: 45% red clay or ball clay, 25% silica (200 mesh), 15% feldspar, 15% grog (fine, 80 mesh). The high proportion of plastic red clay makes this body easy to throw and handbuild. Iron oxide in the red clay (typically 5-8% Fe2O3) produces the characteristic terracotta color. The fired body remains porous (10-15% absorption), so functional earthenware needs glaze inside and out to hold liquids. White earthenware replaces red clay with ball clay and adds 5% calcium carbonate as a secondary flux.

**Stoneware body (cone 6, ~1222 degrees C)**: 30% ball clay, 25% kaolin, 20% silica (200 mesh), 15% feldspar (potash preferred), 10% grog (fine to medium, 40-80 mesh). This body vitrifies to a dense, non-porous state. The grog reduces drying shrinkage and improves thermal shock resistance for ovenware. Without grog, large stoneware pieces crack during drying. A cone 10 stoneware variant drops the grog to 5% and raises feldspar to 20%, achieving full vitrification at 1285 degrees C.

**Porcelain body (cone 10, ~1285 degrees C)**: 50% kaolin (low-iron grade such as Grolleg or New Zealand halloysite), 25% feldspar (potash), 25% silica (200 mesh). Porcelain is the most demanding body: pure kaolin has low plasticity, making it hard to throw. The 12-18% total shrinkage causes warping in large pieces. The reward is a white, dense, resonant ceramic that rings clearly when struck and shows glaze colors at full intensity. Translucent below 3 mm thickness.

## Pyrometric Cone Reference

Pyrometric cones measure heatwork (the combined effect of temperature and time), not just peak temperature. A cone bends 90 degrees when its formulated ceramic softens at the reference temperature for a standard heating rate of 150 degrees C per hour.

| Cone | Temperature (degrees C) | Typical Use |
|------|------------------------|-------------|
| 022 | 600 | Overglaze enamels, luster firing |
| 020 | 635 | Low-fire lusters |
| 018 | 715 | Low-fire glazes, decals |
| 016 | 790 | Low-fire glazes |
| 010 | 905 | Low bisque for earthenware |
| 08 | 955 | Standard bisque for earthenware |
| 06 | 999 | Upper bisque, earthenware glaze firing |
| 04 | 1060 | Standard bisque, earthenware glazes |
| 02 | 1120 | High earthenware, low stoneware |
| 2 | 1168 | Mid-range earthenware |
| 4 | 1196 | Transitional body range |
| 6 | 1222 | Standard stoneware, mid-range glazes |
| 8 | 1263 | High stoneware |
| 10 | 1285 | High-fire stoneware, porcelain |
| 12 | 1325 | High porcelain, some industrial ceramics |

Orton (the dominant cone manufacturer) makes large (senior) cones and small (junior) cones. Large cones are the reference standard. Small cones bend approximately one cone number lower than large cones of the same number. Always use large cones for witness cones in the kiln; small cones fit in kiln sitter devices.

## Detailed Firing Schedules

Below are specific temperature ramp schedules for the three standard clay body types. All rates assume an empty kiln or a well-ventilated fuel kiln. Adjust candling time upward for thick-walled pieces (over 1 cm) or humid conditions.

**Bisque firing schedule (earthenware, target cone 08, 955 degrees C)**:

| Phase | Temperature Range | Ramp Rate | Duration |
|-------|------------------|-----------|----------|
| Candling (optional) | Ambient to 100 degrees C | 30 degrees C/hr | ~3 hr |
| Water smoking | 100 to 300 degrees C | 60 degrees C/hr | ~3.5 hr |
| Organic burnout | 300 to 500 degrees C | 100 degrees C/hr | ~2 hr |
| Quartz inversion | 500 to 650 degrees C | 60 degrees C/hr | ~2.5 hr |
| Ramp to peak | 650 to 955 degrees C | 150 degrees C/hr | ~2 hr |
| Soak at peak | 955 degrees C | Hold | 20 min |
| Cooling | 955 to 200 degrees C | Natural (kiln closed) | 8-10 hr |
| **Total** | | | **~21-23 hr** |

**Bisque firing schedule (stoneware, target cone 04, 1060 degrees C)**:

| Phase | Temperature Range | Ramp Rate | Duration |
|-------|------------------|-----------|----------|
| Candling | Ambient to 100 degrees C | 40 degrees C/hr | ~2.5 hr |
| Water smoking | 100 to 300 degrees C | 60 degrees C/hr | ~3.5 hr |
| Organic burnout | 300 to 550 degrees C | 100 degrees C/hr | ~2.5 hr |
| Quartz inversion | 550 to 650 degrees C | 60 degrees C/hr | ~1.5 hr |
| Ramp to peak | 650 to 1060 degrees C | 150 degrees C/hr | ~2.5 hr |
| Soak at peak | 1060 degrees C | Hold | 20-30 min |
| Cooling | 1060 to 200 degrees C | Natural (kiln closed) | 10-12 hr |
| **Total** | | | **~23-25 hr** |

**Glaze firing schedule (stoneware, cone 6 oxidation, 1222 degrees C)**:

| Phase | Temperature Range | Ramp Rate | Duration |
|-------|------------------|-----------|----------|
| Initial ramp | Ambient to 300 degrees C | 100 degrees C/hr | ~3 hr |
| Moderate ramp | 300 to 1050 degrees C | 150 degrees C/hr | ~5 hr |
| Quartz inversion | 1050 to 650 degrees C (on cooling) | 100 degrees C/hr | (part of cool) |
| Final ramp | 1050 to 1222 degrees C | 100 degrees C/hr | ~1.5 hr |
| Soak at peak | 1222 degrees C | Hold | 15-20 min |
| Initial cool | 1222 to 600 degrees C | 150 degrees C/hr | ~4 hr |
| Controlled cool through 573 degrees C | 600 to 500 degrees C | 80 degrees C/hr | ~1.5 hr |
| Final cool | 500 to ambient | Natural (kiln closed) | 6-8 hr |
| **Total** | | | **~21-23 hr** |

**Glaze firing schedule (stoneware, cone 10 reduction, 1285 degrees C)**:

| Phase | Temperature Range | Ramp Rate | Notes |
|-------|------------------|-----------|-------|
| Initial ramp | Ambient to 1000 degrees C | 100 degrees C/hr | Oxidation atmosphere |
| Body reduction | 1000 to 1150 degrees C | 50 degrees C/hr | Close damper to 50%, push burners. Reduces iron in clay body from Fe3+ to Fe2+ |
| Clear | 1150 to 1200 degrees C | 100 degrees C/hr | Open damper to 75%, oxidation for 2-3 min to clear carbon |
| Glaze reduction | 1200 to 1285 degrees C | 60 degrees C/hr | Close damper to 40%. Iron, copper, and celadon glazes develop color |
| Soak at peak | 1285 degrees C | Hold 10 min | Maintain light reduction. Check cone bend through spy hole |
| Flash cool | 1285 to 1050 degrees C | 200 degrees C/hr | Open damper fully. Fast initial cool prevents glaze devitrification |
| Controlled cool | 1050 to 500 degrees C | 80-100 degrees C/hr | Natural cool rate in most kilns |
| Final cool | 500 to ambient | Natural | Kiln closed until below 200 degrees C |
| **Total** | | | **~20-24 hr** |

Reduction firing cannot be done in an electric kiln (no combustion gases to create a reducing atmosphere). Gas and wood kilns create reduction by restricting the air supply, causing the flame to seek oxygen from the ceramic materials themselves. The amount of reduction is controlled by the damper position and fuel flow. Heavy reduction (lots of smoke from the chimney) is not necessarily better than light reduction; over-reduction causes bloating, carbon trapping, and dull glaze surfaces.

## Glaze Recipes

Glazes are formulated around the triaxial relationship of silica (glass former), alumina (stabilizer that controls viscosity and prevents running), and flux (melter that lowers the softening temperature). Recipes below are given in batch weight percentages of raw materials.

**Clear base glaze, cone 6 (stoneware)**:

| Material | Weight % |
|----------|---------|
| Feldspar (potash, Custer or equivalent) | 35% |
| Silica (200 mesh) | 25% |
| Whiting (CaCO3) | 20% |
| Kaolin | 10% |
| Zinc oxide or talc | 10% |

Fires to a clear, glossy surface at cone 6 (1222 degrees C). Add colorants by weight: iron oxide 1-2% for amber to brown, copper carbonate 2-4% for turquoise to green, cobalt carbonate 0.5-1% for blue, rutile 3-5% for tan with mottled streaks, manganese dioxide 2-4% for plum brown.

**Leach 4-3-2-1 base (cone 6-10, versatile)**:

| Material | Weight % |
|----------|---------|
| Feldspar | 40% |
| Silica | 30% |
| Whiting (or half whiting, half dolomite) | 20% |
| Kaolin | 10% |

At cone 6, add 1-2% zinc oxide to ensure full melt. At cone 10, works as-is. An excellent starting point for developing a personal palette: add any oxide or carbonate at 1-5% for colored transparent glazes.

**Celadon, cone 10 reduction (stoneware)**:

| Material | Weight % |
|----------|---------|
| Feldspar (potash) | 40% |
| Silica | 25% |
| Whiting | 15% |
| Kaolin | 10% |
| Dolomite | 10% |
| Iron oxide (red) | 2% |

The classic East Asian jade-green glaze. Fires translucent green in reduction (Fe2+ in the glass matrix). In oxidation, the same recipe fires yellow-brown. Apply to 1-2 mm dry thickness. Thinner coating appears pale green; thicker appears deep green with visible depth.

**Tenmoku, cone 10 reduction (stoneware)**:

| Material | Weight % |
|----------|---------|
| Feldspar (potash) | 45% |
| Silica | 20% |
| Whiting | 15% |
| Kaolin | 10% |
| Bone ash (calcium phosphate) | 10% |
| Iron oxide (red) | 8-10% |

Dark brown to black with an iridescent surface. At thinner application, the glaze breaks to rust-brown on edges and ridges. The high iron content (8-10%) produces a nearly opaque coating. Bone ash adds phosphate, which promotes the oil-spot effect (crystalline iron oxide spots that float to the surface during peak temperature hold).

**Shino, cone 10 (stoneware)**:

| Material | Weight % |
|----------|---------|
| Feldspar (soda, Minerva or equivalent) | 70% |
| Silica | 20% |
| Clay (redart or local red clay) | 10% |

A high-soda, low-alumina glaze ranging from white to orange to carbon-trap gray. Apply thick (2-3 mm dry coating). In reduction, soda interacts with iron in the clay body to produce the characteristic orange blush. Thick areas trap carbon, creating gray-black patches. The thick application means this glaze runs: leave extra clearance at the pot's base and protect kiln shelves with fresh kiln wash.

**Low-fire earthenware glaze (cone 06, ~999 degrees C)**:

| Material | Weight % |
|----------|---------|
| Feldspar (soda) | 25% |
| Lead bisilicate or borax frit (for food-safe, use borax frit only) | 35% |
| Silica | 15% |
| Whiting | 15% |
| Kaolin | 10% |

Fires to a glossy surface at cone 06. Lead bisilicate produces brilliant, durable surfaces but is toxic. Use borax frit (ferro frit 3124 or equivalent) for all food-contact ware. Colorants: same range as the cone 6 clear base. Earthenware glazes run more readily at peak temperature than stoneware glazes because the lower firing temperature leaves a wider gap between the glaze's softening point and the point where it becomes too fluid.

## Process Description

### Bisque Firing

The first firing converts fragile, water-soluble greenware into porous, durable bisque ware.

1. **Loading**: Place fully dried pieces on kiln shelves with at least 1 cm clearance between pieces. Set pyrometric cones (typically cone 08, cone 06, and cone 04) at three locations: front, middle, and back of the kiln
2. **Candling** (optional, 12 to 24 hours at 80 to 100 degrees C): Hold the kiln at low temperature overnight to drive off residual moisture. Recommended for thick-walled pieces or humid conditions
3. **Water-smoking phase** (100 to 300 degrees C, ramp at 60 degrees C per hour): Mechanically trapped water evaporates from the clay. Vent the kiln (leave peep holes open or run the vent fan) to carry away steam. Rushing this phase is the most common cause of explosion
4. **Organic burnout** (300 to 500 degrees C, ramp at 100 degrees C per hour): Carbon and sulfur compounds in the clay oxidize and burn away. Venting remains necessary
5. **Quartz inversion** (530 to 600 degrees C, ramp at 60 to 80 degrees C per hour): Alpha quartz converts to beta quartz with an abrupt 2 percent volume expansion. Slow ramping prevents cracking from differential thermal stress between the interior and surface of each piece
6. **Ramp to peak** (600 degrees C to target, ramp at 150 degrees C per hour): Above quartz inversion the clay body expands uniformly and tolerates faster heating. Continue to the target cone
7. **Soak** (15 to 30 minutes at peak): Hold temperature to let the kiln equalize. Check cones. The target cone should be bent 90 degrees (tip touching the shelf)
8. **Cooling** (natural cool, 8 to 12 hours): Close all dampers and peeps. Do not open until the kiln is below 200 degrees C. Rapid cooling through quartz inversion on the way down can also crack pieces. For gas and wood kilns, the cooling rate is determined by the insulation of the kiln walls. For electric kilns, the controller can be programmed to manage the cooling rate. A controlled cool-down at 100 to 150 degrees C per hour is safe for most ware

### Glaze Firing

The second firing melts the applied glaze and matures the clay body to its final density.

1. **Wax resist**: Apply wax to the foot of each piece where glaze would bond it to the shelf, and to any areas meant to remain unglazed
2. **Glaze application**: Dip, pour, or brush glaze onto bisque ware. Bisque is porous and absorbs water from the glaze suspension, depositing a 1 to 2 mm coating of dry glaze material on the surface. Dipping produces the most even coat. Pouring allows two different glazes on the same piece. Brushing gives precise control but leaves brush marks that may or may not be visible after firing depending on the glaze's flow characteristics
3. **Loading**: Stilt glazed pieces on kiln shelves for low-fire work, or place on a bed of alumina for high-fire stoneware. Ensure no glaze drips will reach the shelf. Pieces must not touch each other or the kiln wall, since the glaze will fuse them together permanently at peak temperature
4. **Firing schedule**: Similar ramp rates as bisque, but the target temperature is higher. Cone 6 (1222 degrees C) for mid-range stoneware, cone 10 (1285 degrees C) for high-fire. Reduction atmosphere, if desired, is initiated at cone 08 to 06 by partially closing the damper and increasing fuel flow
5. **Soak and cool**: Soak 15 to 20 minutes at peak. Cool naturally. Cooling rate affects some glazes: rapid cooling promotes crystal formation, slow cooling produces glossy surfaces

7. **Post-cure (optional)**: Some glazes, particularly crystalline glazes and certain high-fire celadons, benefit from a controlled cooling profile rather than natural cooling. The kiln is programmed to hold at specific temperatures during cooling to allow crystals to grow (in crystalline glazes) or to develop specific color effects (in copper reds and Chun glazes). This requires a programmable controller and electric kiln or a gas kiln with fine damper control

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Bisque temperature | Cone 08 to 04 (950 to 1060 degrees C) | Earthenware on the low end, stoneware on the high end |
| Glaze temperature | Cone 6 to 10 (1220 to 1300 degrees C) | Depends on clay body and glaze formulation |
| Ramp rate (water-smoking) | 60 degrees C/hr | Must not exceed 100 degrees C/hr for thick pieces |
| Ramp rate (quartz inversion) | 60 to 80 degrees C/hr | 100+ degrees C/hr risks cracking |
| Ramp rate (above 600 degrees C) | 150 degrees C/hr | Safe to accelerate once past inversion |
| Soak time at peak | 15 to 60 min | Longer soaks equalize large kiln loads |
| Cooling | Natural, 8 to 12 hours | Forced cooling risks dunting cracks |

## Safety Considerations

- **Silica dust**: Clay dust contains crystalline silica. Dry scraping or sanding greenware generates respirable silica dust. Silicosis is irreversible. Wear a properly fitted N95 or P100 respirator when handling dry clay or cleaning kiln shelves. Keep floors wet-swept or use HEPA vacuum
- **Carbon monoxide**: Fuel-burning kilns produce CO as a combustion byproduct. Never fire a gas or wood kiln in an enclosed space without forced ventilation. CO is odorless and deadly at high concentrations
- **Thermal shock explosion**: Pieces with trapped moisture or air pockets can explode during the water-smoking phase. Shards become projectiles. Ensure all work is bone dry before loading and never exceed the recommended ramp rate below 300 degrees C
- **Glaze toxicity**: Some glaze colorants contain lead, cadmium, barium, or lithium. Lead and cadmium glazes can leach into food and should be restricted to decorative ware. Mix all glazes with a respirator and gloves
- **Burns**: Kiln surfaces reach hundreds of degrees C. The lid or door can remain hot enough for second-degree burns hours after firing appears complete. Use welding gloves and wait for the kiln to cool below 200 degrees C before unloading

### Personal Protective Equipment

- N95 or P100 respirator when mixing dry glaze materials, scraping kiln shelves, or sanding bisque
- Welding gloves or heavy leather gloves when adjusting damper or burner controls during firing
- Safety glasses when loading or unloading (ceramic shards are sharp)
- Long sleeves and closed-toe shoes near an operating kiln
- Leather apron when loading or unloading to protect against contact with hot kiln furniture

### Emergency Procedures

- If a piece explodes during firing, do not open the kiln. Debris is hot and opening causes thermal shock to remaining pieces. Let the firing continue
- Gas leak: shut off gas at the cylinder or main valve, evacuate, do not operate electrical switches, ventilate before reigniting
- Kiln fire (combustible too close): shut off fuel and power, use a Class ABC fire extinguisher. Never use water on a hot kiln
- Element failure (electric kiln): if an element breaks during firing, the kiln will heat unevenly. Finish the firing if possible, then replace the element. Kanthal A1 elements have a typical lifespan of 100 to 200 firings depending on temperature and atmosphere

## Quality Control

### Acceptance Criteria

- **Fired ceramics**: Bisque should ring with a clear ping when tapped, not a flat thud. Glazed ware should have an even, continuous glaze surface with no bare spots, pinholes, or crawling

The acceptance criteria differ between functional and decorative ware. Functional ware (plates, cups, bowls) must pass absorption and leach tests to be food-safe. Decorative ware can tolerate cosmetic defects that would be rejectable on a dinner plate. Engineering ceramics (refractory bricks, kiln furniture) have entirely different criteria: dimensional precision, thermal shock resistance, and compressive strength matter more than surface appearance.

### Testing Methods

- **Pyrometric cone bend**: The definitive test for firing maturity. A cone bent 90 degrees (tip touching shelf) indicates correct heatwork. Under-bent means underfired; melted flat means overfired

Cones are the traditional standard because they integrate temperature and time into a single measurement. A thermocouple reading of 1220 degrees C for 10 minutes produces a different result than 1220 degrees C for 30 minutes, and the cone captures this difference. Most potters fire with a set of three cones: the target cone, one cone below (underfired indicator), and one cone above (overfired guard). Watching the cones bend through the spy hole during the final stages of the firing is how experienced kiln operators decide when to shut down.

- **Ping test**: Tap the piece with a fingernail or metal tool. A clear ring indicates vitrified body. A dull thud suggests underfired or cracked
- **Absorption test**: Weigh a bisque-fired piece dry, submerge in water for 24 hours, reweigh. Weight gain percentage is the absorption rate. Earthenware: 10 to 15 percent, stoneware: 1 to 3 percent, porcelain: less than 1 percent. This test is one of the most informative quality checks because absorption correlates directly with the degree of vitrification. High absorption in a stoneware body means the firing was too low or too short
- **Visual glaze inspection**: Check for crawling (glaze pulled away, leaving bare patches), pinholing (small bubbles that burst and did not heal), crazing (fine crackle network in the glaze), or shivering (glaze flaking off in chips)
- **Acid leach test**: For food-contact ware, soaking in vinegar for 24 hours reveals whether toxic colorants migrate from the glaze. The piece is then examined for any change in glaze appearance or color loss

### Sampling Protocol

- Fire witness cones at top, middle, and bottom of the kiln load. A 20-degree variation from top to bottom is common in non-computerized kilns
- Tap-test every piece during unloading. Set aside anything that sounds dull for closer inspection
- Record cone results, firing schedule, and anomalies in a kiln log. Patterns emerge over dozens of firings that help diagnose recurring problems
- Keep glaze test tiles in every firing. Small test tiles with the standard glazes, placed in different kiln positions, serve as permanent records of how each glaze performed in each firing. Over time, this builds a reference library that helps predict glaze behavior

## Scaling Notes

Kiln firing scales through distinct stages, each with different fuel economics and control characteristics.

- **Pit firing**: Dig a pit, fill with pots and combustible material (sawdust, dung, wood), ignite. Reaches 800 to 900 degrees C. No temperature control. Produces low-fired earthenware with smoky, unpredictable surfaces. Fuel: a few kg of wood per firing
- **Updraft kiln**: A brick or clay cylinder with a firebox at the bottom and a flue at the top. Heat rises through the ware chamber. Reaches 1000 to 1200 degrees C. Simple to build, but the bottom is always hotter than the top. Fuel: 20 to 50 kg of wood per cubic meter of ware chamber
- **Downdraft kiln**: Firebox on the side, flue at the bottom. Hot gases travel up over the ware, then down through it to the chimney flue. Much more even heat distribution. Reaches 1300+ degrees C. Fuel: 50 to 100 kg of wood per cubic meter
- **Tunnel kiln**: A long continuous kiln with preheat, firing, and cooling zones. Ware on kiln cars moves through on rails. Several tons per day throughput. Fuel consumption drops to 1 to 2 MJ per kg of fired ware. Requires capital investment and continuous operation

Key scaling challenges: heat uniformity becomes harder as the kiln grows, fuel consumption scales faster than linear due to wall losses, and loading logistics for large kilns require planning to avoid wasted space.

Fuel choice also affects what is economically viable at each scale. Wood is universally available but labor-intensive to feed and produces inconsistent heat. Charcoal burns cleaner and hotter but requires a separate production step. Propane and natural gas offer the most precise temperature control but depend on fuel infrastructure. Electric kilns are the simplest to operate but demand reliable grid power. At the tunnel kiln scale, the fuel economics favor gas or heavy fuel oil, with electric boosting to handle peak loads.

The loading pattern inside the kiln also changes with scale. A small top-loading kiln can be stacked by hand with careful attention to air gaps between pieces. A large downdraft kiln requires the potter to think about airflow: pieces in the flame path fire differently from pieces in the shadow of a tall pot. Tunnel kilns solve this by keeping the ware on flat cars with standardized spacing, but the loading crew must be trained to pack each car consistently.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Cracking during firing | Fast ramp through quartz inversion (530 to 600 degrees C) | Slow to 60 degrees C/hr between 500 and 650 degrees C |
| Explosion in early firing | Trapped moisture in thick walls | Extend candling. Ensure pieces are bone dry before loading |
| Bloating (bubbles in clay body) | Incomplete carbon burnout before reduction applied | Hold in oxidation through 600 degrees C. Do not reduce until carbon is fully burned out |
| Crawling glaze (bare patches) | Dusty or oily bisque surface, or glaze too thick | Clean bisque with a damp sponge before glazing. Apply thinner coats |
| Crazing (crackled glaze) | Glaze has higher thermal expansion than the clay body | Increase silica in the glaze, decrease feldspar, or add talc to lower expansion |
| Shivering (glaze pops off) | Glaze has lower thermal expansion than the clay body | Decrease silica in the glaze or switch to a higher-shrinkage clay body |
| Pinholing | Trapped gases did not heal before glaze solidified | Extend soak time by 10 to 15 minutes. Or slow cooling through 1000 to 800 degrees C |
| Uneven firing (top/bottom variation) | Poor kiln design or burner placement | Add witness cones at multiple levels. Stagger shelf heights. Adjust damper to redirect gas flow |
| Color variation in glaze firing | Inconsistent reduction atmosphere across the kiln | Adjust damper position. Add reduction in stages rather than all at once. Check that all burner ports are firing evenly |
| Warped or slumped pieces | Overfiring, or ware not adequately supported at peak temperature | Lower the target cone by one number. Support wide, flat pieces with custom stilts. Ensure shelves are level |
| Kiln shelf cracking | Thermal cycling fatigue, or glaze drip fusing to shelf and creating stress point during cooling | Apply fresh kiln wash before every firing. Rotate shelves periodically. Replace shelves that show hairline cracks before they fail mid-firing |

## Variations and Alternatives

- **Wood-fired anagama**: A single-chamber tunnel kiln fired continuously for 3 to 7 days. Ash deposits melt into a natural glaze on the ware. Labor-intensive and unpredictable, producing surfaces prized in East Asian pottery traditions
- **Gas kiln**: Propane or natural gas burners feeding a downdraft or cross-draft chamber. Easier atmosphere control than wood. The standard for studio pottery producing reduction-fired stoneware
- **Electric kiln**: Resistance heating elements (Kanthal A1 wire or silicon carbide) in an insulated fiber or brick chamber. Always oxidation atmosphere. Precise temperature control via programmable controller. No combustion gases. Most common kiln type for small studios and schools
- **Raku**: Remove ware from the kiln at peak temperature (around 1000 degrees C) with tongs, place in a metal container with combustible material. Post-firing reduction creates dramatic crackle glazes and copper flash effects. Not food-safe or waterproof. A decorative technique
- **Pit firing**: The most basic approach, suitable only for low-fire earthenware. No glaze. Surfaces are decorated by smoke and fumes from the combustion
- **Sagger firing**: Pottery is enclosed in a clay container (sagger) along with combustible materials (sawdust, seaweed, copper wire, banana peels). The sagger is fired in a regular kiln, but the fumes inside the container create unique, localized reduction effects on the ware. Used for decorative pieces where unpredictable surface variation is desired
- **Obvara firing**: A Baltic technique where red-hot ware is dipped in a fermented flour-and-water mixture, then quickly plunged into water. The sugars in the mixture caramelize and scorch on the surface, producing patterns similar to raku but without the post-firing reduction chamber

## References

- [Pottery & Clay Products](pottery.md) — parent capability
- [Ceramics Domain](./index.md) — domain overview and related capabilities
- [Charcoal Production](../energy/charcoal.md) — downstream capability

---

*Part of the [Bootciv Tech Tree](../index.md) · [Ceramics](./index.md) · [All Domains](../index.md)*

