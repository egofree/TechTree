# Tire Manufacturing

> **Node ID**: transport.tire-manufacturing
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`polymers`](../polymers/index.md), [`textiles`](../textiles/index.md), [`chemistry`](../chemistry/index.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-40+
> **Outputs**: pneumatic_tires, solid_tires, tire_cord
> **Critical**: No

The tire is the only component of a wheeled vehicle that touches the ground. Every watt of engine power, every gram of braking force, and every degree of steering angle ultimately passes through four contact patches no larger than a postcard. Without a durable, compliant, high-traction pneumatic tire, the road vehicle, the railway wheel (in its rubber-cushished form), the aircraft landing gear, and the bicycle are each reduced to iron-on-stone sliding friction — noisy, destructive, and incapable of the speeds and comfort that define modern transport.

Tire manufacturing unites four industries at a single factory bench: **natural and synthetic rubber compounding** (polymers), **cord fabric weaving and calendering** (textiles), **chemical additives** — carbon black, silica, accelerators, antioxidants (chemistry), and **high-tensile steel belt wire** (metals.iron-steel). The vulcanization reaction itself — sulfur cross-linking of polymer chains — is treated in depth in the [Polymers](../polymers/index.md) domain; this article covers the tire as a manufactured product, not the underlying chemistry.

## Processes in this Capability

- [Rubber Compounding](tire-manufacturing.rubber-compounding.md) — Banbury mixing of rubber, carbon black, silica, and cure agents; calendering of cord fabric into rubberized ply stock.
- [Tire Building](tire-manufacturing.tire-building.md) — layer-by-layer assembly of the uncured (green) tire on a building drum.
- [Curing and Finishing](tire-manufacturing.curing-and-finishing.md) — press vulcanization in a heated mold, followed by trimming, balancing, and inspection.

## Historical Development

The pneumatic tire is a 19th-century invention that defined 20th-century mobility. The key milestones a bootstrap economy must re-traverse:

- **Vulcanization (1839)** — Charles Goodyear (US) and Thomas Hancock (UK), independently, discovered that heating natural rubber with sulfur cross-links the polymer chains, converting a sticky, thermoplastic, cold-brittle gum into a resilient, elastic, heat-stable elastomer. Without vulcanization, a tire would melt in summer and shatter in winter. The chemistry is covered in [Polymers](../polymers/index.md).
- **Pneumatic tire (1888)** — John Boyd Dunlop (Scotland) patented the pneumatic bicycle tire to cushion his son's tricycle rides on cobbled Belfast streets. The air-cushion principle cut rolling resistance and shock dramatically versus solid rubber. Originally clamped to the wheel; the detachable (clincher) bead came later.
- **Detachable pneumatic / bead (1891)** — Édouard Michelin patented a tire demountable from the rim by hand, enabling roadside repair. This made pneumatics practical for automobiles, which arrived the same decade.
- **Carbon black reinforcement (1912)** — adding furnace carbon black to tread compounds multiplied tread life 4-5× and tensile strength ~10×. Before this, tires lasted only a few thousand kilometers. Carbon black is why tires are black.
- **Cord fabric (1920s)** — replacing square-woven fabric with parallel cord plies (cords held in place by light weft threads, then calendered into rubber) eliminated inter-cord friction and chafing — a major durability and heat gain.
- **Synthetic rubber (1930s-40s)** — Germany (Buna-S) and the US (GR-S, later SBR) developed styrene-butadiene rubber under wartime rubber-supply crisis (Japanese occupation of Southeast Asian Hevea plantations, 1942). SBR remains the dominant passenger-tire elastomer.
- **Radial construction (1946)** — Michelin patented the radial-ply tire (body cords at 90 degrees, steel belts at the crown). The X tire (1949) delivered 2-3× the tread life and markedly better fuel economy and grip of the bias-ply standard. Europe converted by ~1970; the US lagged until the 1970s oil crisis made fuel economy decisive.
- **Tubeless tire (1955)** — the halobutyl inner liner replaced the separate inner tube, eliminating one failure mode (pinch flats between tube and tire) and reducing weight.
- **Green tire / silica (1992)** — Michelin's silica/silane tread compound broke the magic triangle (see below), cutting rolling resistance 20-30% without sacrificing wet grip — a fuel-economy landmark now standard across the industry.
- **TPMS mandate (2007)** — the US TREAD Act (post-Firestone/Ford Explorer rollover recalls of 2000) made direct tire-pressure monitoring systems mandatory on all new passenger vehicles.

## Manufacturing Flow

A tire moves through the factory in three stages, each corresponding to one of this capability's processes:

1. **Mixing and calendering** (rubber-compounding) — Raw elastomers (NR bales, SBR/BR bales), carbon black (pellets in 20-25 kg bags), silica, oils, and chemicals are weighed to ±0.1% and charged into an internal mixer (Banbury) in a sequenced recipe. The hot mixed compound is dumped onto a mill, sheeted, and cooled. A portion is calendered (forced between precision steel rolls) into thin sheets; the rest is frictioned onto textile cord fabric to make rubberized ply stock. Component-specific compounds (tread, sidewall, inner liner, bead filler) are each mixed separately and extruded into profiled strips (the tread, sidewall, apex) on hot-feed extruders.
2. **Building** (tire-building) — A tire builder (operator or automated machine) assembles the green tire on a rotating drum: inner liner, body plies, beads, turn-up, sidewalls, and (on the second-stage drum) steel belts and tread. Splices are stitched; the green tire is inspected for ply alignment and splice gaps before curing.
3. **Curing and finishing** (curing-and-finishing) — The green tire is loaded into a heated mold; an internal bladder inflates it against the engraved mold surfaces under pressure and heat for 8-20 minutes. The cured tire is cooled, post-cure-inflated, trimmed, balanced, and tested for uniformity before warehousing.

Total factory throughput for a single passenger tire is 2-4 hours of process time (mixing through finishing), with substantial work-in-progress inventory between stages. A modern tire plant produces 15,000-30,000 tires per day on a 24-hour schedule.

## Tire Construction: Radial vs Bias-ply

Two fundamental carcass architectures exist. Both predate the modern factory, but their industrial mass-production defines 20th-century mobility.

**Bias-ply (cross-ply)** — Body plies of nylon or polyester cord are laid at alternating angles of 30-40 degrees to the tire centerline (the "bias"). Each ply runs bead-to-bead (from one wheel-rim-anchoring bead up the sidewall, across the crown, and down the other sidewall). The tread is applied on top of this bias carcass. The entire structure flexes as a single unit: sidewall deformation directly squirms the tread contact patch.

- **Strengths**: simple construction, tolerant of rough roads, robust sidewalls, cheap tooling. Dominant until ~1970.
- **Weaknesses**: high rolling resistance (squirm generates heat), poor high-speed stability, rapid tread wear. The flexing tread scrubbs against the road, losing grip and material.

**Radial** (Michelin, 1946 — André and Édouard Michelin) — Body plies are laid at 90 degrees to the centerline (radially, like wheel spokes, from bead to bead). On top of this radial carcass sit 2-4 nearly inextensible **steel belts** laid at 15-25 degrees, which constrain the crown. The result decouples the sidewall (which flexes vertically over bumps) from the tread (which stays flat and stable on the road).

- **Strengths**: 20-30% lower rolling resistance (direct fuel savings), 50-100% longer tread life, superior wet and dry grip, stable contact patch at speed. Dominant worldwide since ~1980; standard on essentially all passenger cars.
- **Weaknesses**: stiffer sidewall (harsher ride), more complex manufacturing (belt layers require precise tension and a separate building stage), heavier bead construction.

The radial's superiority is so complete that bias-ply survives today only in low-speed off-road, agricultural, trailer, and some vintage-vehicle applications where ride softness or cost dominates. The transition from bias to radial is the single largest step-change in tire technology since pneumatics themselves.

## Tire Anatomy (Radial, Outside In)

A modern radial passenger tire contains 15-25 distinct components, layered from the inside out:

1. **Inner liner** — halobutyl rubber (impermeable to air), 1-2 mm thick. Replaces the separate inner tube of older tube-type tires. Holds inflation pressure for months, not days.
2. **Carcass ply (body ply)** — one or two layers of polyester, nylon, or rayon cord fabric, calendered (sandwiched) in rubber, laid at 90 degrees. Carries the inflation load — the tensile member of the pressure vessel.
3. **Beads** — bundles of high-tensile bronze-coated steel wire (4-8 mm diameter hoops), anchored at the rim seat. Each bead is 15-25 individual wires wound into a ring. The bead locks the tire onto the wheel rim against inflation pressure and cornering load.
4. **Bead filler (apex)** — hard triangular rubber extrusion above the bead, stiffening the lower sidewall for steering response.
5. **Sidewall** — abrasion- and ozone-resistant rubber compound (no carbon black needed for grip here — protected from wear). Carries the tire's identification markings.
6. **Steel belts (breaker)** — 2-4 layers of brass-coated high-tensile steel wire (0.15-0.30 mm filament diameter, 20-100 wires per cm of belt width), laid at 15-25 degrees to the centerline and calendered in rubber. Provide crown rigidity, puncture resistance, and a stable tread footprint.
7. **Nylon cap ply (overlays, optional)** — zero-degree nylon wound spirally over the belts, suppressing high-speed centrifugal growth and improving uniformity above ~180 km/h (H/V/Z speed ratings).
8. **Tread** — the wear-surface compound, the focus of the "magic triangle" trade-off below. 8-14 mm new-tread depth on passenger tires.
9. **Shoulder** — thick rubber block at the tread/sidewall junction, dissipating heat from the crown. The hottest point in a running tire.

### The contact patch

The contact patch (footprint) is the roughly elliptical area where the tire meets the road — typically 150-250 cm² per passenger-car tire, about the size of a postcard, carrying 300-500 kg. This patch transmits three forces simultaneously: longitudinal (acceleration/braking), lateral (cornering), and vertical (load). Its size and pressure distribution — not the rubber's intrinsic friction coefficient alone — set the absolute ceiling on vehicle grip. A wider, lower-pressure tire puts more rubber on the road, but increases rolling resistance and hydroplaning risk. The patch deforms as the tire rolls: it squirms laterally under cornering and elongates longitudinally under torque. This slip (creep), typically 5-20% under hard braking, is what generates the friction force — a rolling tire transmits force *through* controlled micro-slip, not static contact. The whole science of tire-vehicle handling (slip angle, cornering stiffness, self-aligning torque) flows from the contact patch's viscoelastic mechanics.

## Materials

### Rubber (the elastomer matrix)

Tire rubber is never a single polymer. A passenger-tire tread typically blends 2-4 elastomers:

- **Natural rubber (NR, polyisoprene)** — tapped from the *Hevea brasiliensis* tree (Southeast Asia plantations). High tensile strength, low heat build-up, excellent grip. Essential for truck and aircraft tires (high load, high deflection). The guayule shrub (*Parthenium argentatum*, desert Southwest US) and Russian dandelion (*Taraxacum kok-saghyz*) are alternative latex sources, developed as strategic reserves against Hevea supply disruption.
- **Styrene-butadiene rubber (SBR)** — the dominant synthetic, petroleum-derived. Tunable styrene content (15-40%) trades grip for wear resistance. The workhorse of passenger-tire treads.
- **Polybutadiene rubber (BR)** — high resilience (low rolling resistance, low heat build-up), blended with SBR in treads. Often 20-50% of the tread blend.
- **Butyl and halobutyl** — exceptionally impermeable to air and moisture. Used for the inner liner and (in tube-type tires) the inner tube. Halogenation (bromination/chlorination) improves co-vulcanization with other rubbers.
- **Ethylene-propylene rubber (EPDM)** — ozone and weather resistance, used in sidewalls and white-letter stripes.

See [Polymers — Rubber](../polymers/index.md) for natural latex tapping, coagulation, and mastication, and for synthetic rubber polymerization. **Vulcanization fundamentals** (sulfur cross-linking, the Goodyear-Hancock discovery, accelerator chemistry) are covered there; this article treats the cured compound as a given input and focuses on its tire-specific formulation.

### Reinforcement (the load-carrying cord)

The rubber matrix alone has almost no tensile strength; it tears and flows under load. All structural integrity comes from the cord reinforcement:

- **Polyester (PET)** — the dominant body-ply cord for passenger tires. High tenacity, good fatigue resistance, low cost. Cord denier 1000-2000.
- **Nylon 6,6** — used in bias-ply treads, cap plies, and aircraft tires. High strength and heat resistance, but "flat-spotting" (sets when parked cold, thumps for the first few km).
- **Rayon** — the original radial body ply (Michelin's X tire, 1949). Still used in high-performance European tires for its dimensional stability and ride comfort, despite higher cost.
- **Aramid (Kevlar)** — ultra-high tenacity, used in cap plies for Z-rated tires and in run-flat inserts. Expensive.
- **Steel wire** — brass-coated high-tensile (2500-3000 MPa) drawn wire, the belt cord. Produced from high-carbon steel rod (see [metals.iron-steel](../metals/iron-steel.md)), patenting (lead-bath patenting at 500-550 C), wet wire drawing to 0.15-0.30 mm, and brass electroplating for rubber adhesion.

The cord fabric itself — woven, dipped (resorcinol-formaldehyde-latex "RFL dip" for rubber adhesion), and wound onto beams — is the output of the [Textiles](../textiles/index.md) domain. The tire factory receives dipped cord fabric and calenders rubber onto it; it does not spin or weave the yarn.

#### Steel cord manufacturing (belt and bead wire)

Steel tire cord is the single most demanding steel product in the tire, and the reason this capability depends on [metals.iron-steel](../metals/iron-steel.md). The production chain, starting from high-carbon steel rod:

1. **Patenting** — the 5-8 mm diameter high-carbon (0.70-0.85% C) rod is heated to austenitizing temperature (~950 C) and rapidly quenched into a lead or salt bath at 500-550 C, transforming it to a fine pearlite (sorbitic) structure. This is the only microstructure that can be drawn to fine wire without breaking while retaining high tensile strength.
2. **Dry and wet drawing** — the patented rod is cold-drawn through a sequence of progressively smaller tungsten-carbide or diamond dies, first dry (to ~1 mm) then wet (in a soap emulsion, to final 0.15-0.30 mm). Each die reduces area ~15-25%; the wire strain-hardens to 2500-3000 MPa tensile — among the strongest steel products made.
3. **Brass plating** — the drawn wire is brass-electroplated (0.15-0.35 μm layer, ~63-70% Cu) in a continuous pass. The brass reacts with the sulfur in the rubber compound during vulcanization, forming copper-zinc sulfides that chemically bond the steel to the rubber matrix. Without brass (or with the wrong brass composition), belts debond under load and the tire separates.
4. **Cabling** — for belt cord, multiple filaments (e.g., 2+7, 3+9, 7×3×0.20 constructions) are stranded around each other into a cable on a bunching or tubular strander. Bead wire is used as a single larger wire (0.8-1.6 mm). The cabled cord is wound onto beams for calendering into belt plies.

### Fillers and additives (the chemistry)

The raw elastomer blend is weak, sticky, and cures too slowly for industrial use. The compounding chemist adds:

- **Carbon black** — furnace-process soot (10-100 nm particle size), 25-40% of compound by weight. Reinforces tensile and tear strength, abrasion resistance, and UV stability. Turns the tire black (the default color). See [chemistry](../chemistry/index.md).
- **Silica (precipitated)** — coupled to the rubber via a bifunctional silane coupling agent (e.g., TESPT). Reduces rolling resistance while maintaining wet grip — the basis of the "green tire" (Michelin, 1992). Harder to mix and cure than carbon black.
- **Processing oils** — naphthenic or aromatic extender oils, plasticize the compound for mixing and calendering, reduce cost.
- **Antioxidants and antiozonants** (6PPD, TMQ) — protect against oxygen and ozone degradation of the polymer chains. Without them, rubber cracks and hardens within a year. **6PPD-quinone** (the oxidation product) is an emerging environmental concern for waterways; replacement chemistries are under active development.
- **Accelerators** (MBT, MBTS, CBS, TBBS) — speed and control the sulfur vulcanization, allowing cure times of 8-15 minutes at 150-170 C rather than hours.
- **Sulfur and zinc oxide** — the cross-linking agent and activator. Sulfur 1-3 phr (parts per hundred rubber), zinc oxide 3-5 phr with stearic acid.

A representative modern silica-tread compound (green-tire style), expressed in **phr** (parts per hundred rubber), gives a sense of proportions:

| Ingredient | phr | Role |
|------------|-----|------|
| SBR 1502 | 70 | Tread base elastomer |
| Polybutadiene (BR) | 30 | Low-hysteresis modifier |
| Silica (precipitated) | 80 | Reinforcing filler (replaces carbon black) |
| Silane (TESPT) | 7 | Silica-polymer coupling agent |
| Aromatic oil | 5 | Processing plasticizer |
| Zinc oxide | 3 | Cure activator |
| Stearic acid | 2 | Cure activator / wetting |
| Antioxidant (6PPD) | 2 | Ozone/oxygen protection |
| Sulfur | 1.5 | Cross-linking agent |
| Accelerator (CBS) | 1.7 | Cure-speed control |

Note the high silica loading (80 phr) — more filler than rubber — and the silane coupling agent that bonds it. This recipe is mixed, sheeted, and (for the tread) extruded into the profiled strip that lands on the building drum.

## The Magic Triangle: Rolling Resistance, Wear, and Grip

Tire compound engineering is governed by an irreducible three-way trade-off, the **"magic triangle."** Improving one vertex typically costs the other two:

- **Rolling resistance** — energy lost as the tire deforms and recovers each revolution (hysteresis). 5-15% of vehicle fuel consumption is tire rolling loss. Low hysteresis (high rebound) compounds recover deformation energy instead of converting it to heat. Favors high-temperature vulcanization, silica/silane systems, high BR content. Directly measured as a force (N) or as a rolling-resistance coefficient (typically 0.007-0.015).
- **Wear resistance** — tread mileage before the tread wears to the wear-bar (2/32" / 1.6 mm). Favors hard, high-crosslink-density compounds, high carbon black loading, high styrene SBR. Trades against grip.
- **Wet grip** — braking and cornering on a wet surface, dominated by tread compound hysteresis at high frequencies and the tread pattern's water evacuation. Favors soft, tacky, high-hysteresis compounds (the same property that dissipates energy as rolling loss). Rated on the EU label A-G.

Silica/silane "green tire" technology (Michelin Energy, 1992 onward) partially breaks the triangle: by replacing carbon black with silica in the tread, rolling resistance drops 20-30% with no loss of wet grip — the coupling agent bonds the silica to the polymer network in a way that decouples the low-frequency (rolling) and high-frequency (grip) hysteresis responses. This is the single most important compound advance of the last 40 years.

## Tread Patterns

The tread's job is to maintain rubber-road contact while evacuating water, mud, and debris. Four pattern families:

- **Symmetric rib/block** — most passenger tires. Continuous circumferential ribs for low noise, with lateral grooves for water evacuation. Direction-agnostic, allowing tire rotation side-to-side.
- **Asymmetric** — different inner and outer tread zones. Stiffer outer shoulder blocks for dry cornering grip; more open inner pattern with deep grooves for wet braking. Common on performance tires. Tire has an "outside" marking; cannot be cross-rotated.
- **Directional (V-pattern)** — chevron grooves pointing in the direction of rotation. Pumps water out efficiently — the pattern for wet conditions and aquaplaning resistance. Mounts only in the correct rotation (arrow on sidewall).
- **Mud and snow (M+S) / winter lug** — deep, aggressive blocks with sipes (thin transverse cuts) that bite into snow and clear mud. Studs (tungsten carbide pins) for ice, where legal. High noise and rolling resistance on dry pavement — a seasonal compromise.

Tread void ratio (the fraction of the footprint that is groove, not rubber) ranges from ~20% (smooth racing slick) to ~50% (winter). More void = better water evacuation, less dry grip, more flex (higher wear).

### Aquaplaning (hydroplaning)

At a critical speed, the tire cannot evacuate water fast enough through its grooves, and the water pressure lifts the tread off the road — the tire "planes" on the water film, losing all grip (steering, braking, and acceleration go to zero). The aquaplaning threshold speed (km/h) is approximately √(10 × inflation pressure in kPa) for a smooth surface; tread grooves raise it by improving drainage. A passenger tire at 220 kPa begins to aquaplane around 47 km/h in deep standing water — far above typical wet-road speeds because real roads carry only a thin film. Wide, low-profile tires with shallow grooves are most prone (less drainage per unit footprint); this is why a worn tire (tread near the 1.6 mm minimum) aquaplanes at dramatically lower speeds than a new one.

### Sipes

Sipes are thin (0.3-0.8 mm wide), 4-8 mm deep transverse cuts molded into the tread blocks of winter and all-season tires. They open as the block contacts the road, presenting many micro-edges that grip snow, ice, and wet surfaces by friction and capillary wiping of the water film. A typical winter block carries 50-150 sipes. Their compliance also warms the tread. The trade-off: siped blocks are squirmier (higher rolling resistance, more dry-wear) — a reason winter tires feel vague on dry pavement.

## Sidewall Markings

A passenger tire sidewall carries a dense specification code. Example: **225/45 R17 91V**.

| Token | Meaning |
|-------|---------|
| 225 | Section width, millimeters (the widest point of the inflated tire, excluding raised lettering) |
| 45 | Aspect ratio (profile) = sidewall height / section width × 100. 45 = sidewall is 45% of 225 = 101 mm. Lower = lower profile, stiffer sidewall. |
| R | Construction: R = radial. "D" = bias (diagonal), "-" = bias belted. Nearly all passenger tires are R. |
| 17 | Rim (bead seat) diameter, inches. |
| 91 | **Load index** — maximum load per tire at max pressure, per a lookup table. 91 = 615 kg. |
| V | **Speed rating** — maximum sustained speed. L=120, Q=160, S=180, T=190, H=210, V=240, W=270, Y=300 km/h. (ZR = above 240.) |

Additional markings: DOT code (plant, size, week/year of manufacture — the "birthday" code, e.g., "2423" = 24th week of 2023), M+S or the three-peak-mountain-snowflake (3PMSF) for winter certification, E-mark (European homologation), treadwear/traction/temperature grades (US UTQG), and the ECE R75 approval number.

**Common load index values** (kg per tire): 82=475, 86=530, 90=600, 91=615, 92=630, 94=670, 96=710, 100=800, 104=900, 108=1000. Light-truck load ranges use a dual marking: "C"/"D"/"E" ply ratings (e.g., Load Range E ≈ 10-ply equivalent, ~1135 kg at 550 kPa single).

**Speed rating progression** (km/h, sustained): N=140 (spare/limited-use), P=150, Q=160 (winter studdable), R=170, S=180, T=190, U=200, H=210, V=240, W=270, Y=300, (Y)=300+. The "ZR" prefix (e.g., 225/45ZR17) denotes a tire capable of sustained speeds above 240 km/h. A speed rating above the vehicle's top speed provides a safety margin against heat-induced failure, not everyday operating permission.

## Tire Pressure Monitoring (TPMS)

A pneumatic tire loses 0.5-1.5% of its pressure per month by diffusion through the rubber. Under-inflation by 20% increases rolling resistance ~5%, wear ~25%, and dramatically raises failure risk from overheating. Direct TPMS — a battery-powered pressure sensor on each valve stem, transmitting 315/433 MHz RF to the vehicle — became mandatory in the US (TREAD Act, 2007, post-Firestone-Ford Explorer recalls), the EU (2012), and most major markets. Indirect TPMS uses wheel-speed sensors (from ABS) to detect the smaller rolling radius of a deflated tire. See [electronics](../electronics/index.md) and [computing](../computing/index.md) for the sensor and signal-processing foundations.

## Inflation Pressure and Load Capacity

The pneumatic tire is a pressure vessel: the vehicle's weight is carried almost entirely by the compressed air, with the carcass cords restraining the membrane. Load capacity rises roughly linearly with inflation pressure (a tire rated 615 kg at 220 kPa may carry 730 kg at 260 kPa), which is why truck and aircraft tires run at very high pressures (1-1.5 MPa). Two consequences dominate tire engineering:

- **Heat generation** — every flexure of the rotating tire converts some deformation energy to heat (hysteresis). Higher load or lower pressure means deeper flexure, more heat. Run an overloaded or under-inflated tire and the internal temperature climbs past ~120 C, degrading the rubber and the brass-steel-rubber bond until the belt separates or the carcass bursts. This is the failure mode behind the Firestone-Ford Explorer ATX/Wilderness recall of 2000.
- **Pressure-temperature coupling** — a tire's pressure rises ~10 kPa per 10 C of temperature rise as the gas inside heats. A cold-set pressure at 20 C will read higher at operating temperature; vehicle placards specify the cold-set value. Nitrogen fill (inert, dry, lower moisture content than compressed air) reduces the pressure swing and internal oxidation — standard for aircraft and performance tires, marketed but marginal for ordinary passenger use.

## Specialty: Solid, Aircraft, and Run-Flat Tires

**Solid tires** — no air cavity, the entire structure is dense molded rubber (or polyurethane). Puncture-proof, used on forklifts, industrial trucks, scooters, and slow casters. Heavy, hot-running, and harsh-riding; unsuited to high-speed road use. The simplest tire product, requiring only compounding and molding (no building drum or beads).

**Aircraft tires** — extreme-load pneumatics inflated to 1.0-1.5 MPa (10-15 bar, 5-10× passenger-car pressure). Bias-ply construction (radial aircraft tires exist but bias dominates for fatigue tolerance under the impact loads of landing). Natural rubber-rich for heat resistance. Filled with nitrogen (inert, dry, prevents pressure swing with altitude and ignition in a brake-fire). Manufactured by the same processes — not a separate capability, but a specialty application of this one.

**Run-flat tires** — reinforced sidewalls thick enough to support the vehicle at zero pressure for 80 km at 80 km/h (SSR, DSST, ZP, RFT trade names). Self-sealing tires (ContiSeal) coat the inner liner with a viscous sealant that flows into punctures up to 6 mm. Both add cost, weight, and ride harshness; both depend on functioning [TPMS](#tire-pressure-monitoring-tpms) so the driver knows the tire is flat.

## Major Manufacturers

The global tire industry is a tight oligopoly, ~75% of revenue held by the top five (in revenue order): **Bridgestone** (Japan, founded 1931), **Michelin** (France, 1889), **Goodyear** (US, 1898), **Continental** (Germany, 1871), and **Sumitomo/Pirelli** (Italy, 1872; Pirelli is now Sinochem-controlled). Their compound formulations, belt designs, and building-machine know-how represent over a century of accumulated process refinement — the kind of tacit knowledge that this project's bootstrap timeline (Years 20-40+) is calibrated to re-derive, not shortcut.

## Testing and Certification

A finished tire is a safety-critical component; every tire is individually inspected and a statistical sample is destructively tested. The principal tests:

- **Uniformity (force variation)** — the tire is run against a calibrated load wheel at speed and rated pressure. Radial and lateral force variations over one revolution must stay within tolerance (typically <30-50 N first harmonic). High force variation causes vehicle shake and uneven wear.
- **Dynamic balance** — measured on a spin balancer; correction weights applied to the rim flange. Residual static and couple imbalance must meet grade limits.
- **Plunger energy (puncture resistance)** — a steel plunger is forced into the crown; the energy to rupture must exceed a minimum, ensuring the tire withstands road hazards.
- **Bead unseating resistance** — the force required to push the bead off the rim seat under rated load, ensuring the tire stays seated in cornering.
- **High-speed durability** — run on a dynamometer at step-increasing speeds (e.g., 170, 180, 190, 200 km/h, 20 min each) past the speed rating; must not fail.
- **Endurance (low-pressure / overload)** — extended running at reduced pressure or overload, simulating abuse; must not separate or burst.
- **X-ray and shearography** — sample (non-destructive) inspection of steel-belt alignment, voids, and ply separations inside the cured tire.

Regulatory and consumer-information labeling schemes: the **US UTQG** (Uniform Tire Quality Grading — treadwear index, traction AA-C, temperature A-C), the **EU tire label** (rolling resistance A-G, wet grip A-G, external noise in dB), and the **DOT / ECE** type-approval markings. Winter tires carry the **3PMSF** (three-peak mountain snowflake) symbol, certifying snow performance beyond a generic M+S marking.

## End of Life and Recycling

A passenger tire is retired at 1.6 mm (2/32") remaining tread depth (the legal minimum in most jurisdictions) or at 6-10 years of age, whichever comes first. The discarded tire is one of the most voluminous and difficult solid-waste streams: cross-linked rubber does not melt, does not dissolve, and does not biodegrade on any useful timescale. Disposal routes:

- **Whole-tire reuse** — dock fenders, breakwaters, playground equipment, artificial reefs (marine).
- **Shredding and steel/fiber recovery** — magnetic separation of the steel bead and belt wire (10-15% of tire mass), and air classification of the textile cord fiber (5-10%). The remaining crumb rubber is 1-10 mm granulate.
- **Crumb rubber markets** — molded products (mats, speed bumps, playground tiles), asphalt modifier (rubber-modified asphalt, quieter and longer-lasting road surface), and artificial-turf infill (the largest single market, now under environmental scrutiny for microplastic and 6PPD-quinone runoff).
- **Devulcanization** — chemical or thermo-mechanical breaking of sulfur cross-links to recover a processable elastomer. Technically feasible but economically marginal; <5% of scrap tires are devulcanized today.
- **Tire-derived fuel (TDF)** — shredded tires burned in cement kilns, pulp-and-paper boilers, and power plants. The highest-volume disposal route (~40% of scrap in the US) — controversial, as it foregoes material recovery for one-time energy.
- **Pyrolysis** — anaerobic thermal decomposition (400-700 C) yields recovered carbon black (rCB), pyrolysis oil, and steel. rCB is a growing substitute for virgin furnace carbon black in non-tire rubber goods and, increasingly, in tire treads themselves.

The 6PPD antioxidant (in the tread compound) oxidizes in use to **6PPD-quinone**, which washes off roads into waterways and is acutely lethal to coho salmon at parts-per-trillion concentrations — an emerging regulatory driver for antioxidant chemistry reformulation.

## Prerequisites

- [Polymers](../polymers/index.md) — natural rubber and synthetic elastomers, and the vulcanization reaction
- [Textiles](../textiles/index.md) — high-tenacity cord fabric weaving and RFL dipping
- [Chemistry](../chemistry/index.md) — carbon black (furnace process), silica, accelerators, antioxidants, processing oils
- [Iron and Steel](../metals/iron-steel.md) — high-carbon rod, patenting, and brass-coated wire drawing for belt and bead cord
- [Internal combustion](../energy/internal-combustion.md) — the road vehicle that creates tire demand at scale
- [Machine tools](../machine-tools/index.md) — the precision-machined building drums, calender rolls, and curing molds

## See Also

- [Transport](./index.md) — parent domain
- [Road & Bridge Construction](./roads.md) — the surface a road tire runs on
- [Polymers — Rubber](../polymers/index.md) — vulcanization fundamentals

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transport](./index.md) • [All Domains](../index.md)*
