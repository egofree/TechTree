# Vehicle Assembly

> **Node ID**: space-ground-ops.vehicle-assembly
> **Domain**: [Space Ground Operations](./index.md)
> **Dependencies**: `construction`, `metals`, `machine-tools`
> **Enables**: None
> **Timeline**: Years 50+
> **Outputs**: integrated_vehicles
> **Critical**: YES

Vehicle assembly is the discipline of stacking, integrating, and transporting an orbital-class launch vehicle — a structure that may stand 110m tall, weigh 2,500-3,000 tonnes fully fueled, and be precise enough that stage-to-stage alignment is held to within 6mm at the interstage interface. The Apollo/Saturn V program established the canonical pattern: stages built at remote factories (Michoud, Huntington Beach) are shipped to the integration site, stacked vertically in a 160m-tall assembly building, then rolled out to the pad on a 2,700-tonne crawler-transporter at 1.6 km/hr. The building is the Vehicle Assembly Building (VAB) at Kennedy Space Center — at 160m tall with a 218m × 158m footprint, one of the largest enclosed volumes ever constructed. The crawler is the Crawler-Transporter, two 6.6-million-kg vehicles built by Marion Power Shovel in 1965-1966 and still in service.

This capability covers two process areas: [Vertical Assembly Building](./vehicle-assembly.vab-facilities.md) and [Transporter/Erector & Crawler](./vehicle-assembly.transporter-erector.md).

## Overview

The fundamental constraint on launch vehicle assembly is that the vehicle is too tall, too heavy, and too fragile to be moved horizontally. A Saturn V at 110.6m long and 2,500 tonnes, with a thin-wall aluminum skin 2-6mm thick over a stringer/frame structure, has the aspect ratio of a soda can — it cannot be supported horizontally on its side without permanent deformation. The vehicle must be assembled vertically, transported vertically, and launched vertically. This dictates the design of every piece of ground support equipment downstream of stage delivery.

The assembly flow has four phases: (1) stage receiving and inspection at the integration facility, (2) vertical stacking in the VAB high bay, (3) integrated systems testing while vertical, and (4) rollout to the launch pad on the crawler-transporter. The full VAB-to-pad flow for an SLS-class vehicle takes 25-40 days from stacking to launch.

| Vehicle | Stacking Location | Integration Time | Transport Mode | Pad Distance | Rollout Duration |
|---------|-------------------|------------------|----------------|--------------|------------------|
| Saturn V / Saturn IB | KSC VAB | 30-45 days | Crawler-Transporter + MLP | 5.6 km (LC-39A/B) | 4-6 hours |
| Space Shuttle | KSC VAB | 20-30 days | Crawler + MLP | 5.6 km (LC-39A/B) | 4-6 hours |
| SLS / Artemis | KSC VAB | 35-50 days | Crawler-Transporter + ML | 6.4 km (LC-39B) | 8-12 hours |
| Falcon 9 / Heavy | Hangar at pad | 7-14 days | TEL on wheels | 300-500 m | 30 min |
| Starship / Super Heavy | Starbase High Bay | 20-40 days | Mechanized rail/launch mount | 0 m (OLM integration) | 0 (built at pad) |
| Ariane 5 / 6 | ELA-3 / ELA-4 integration bldg | 15-25 days | Rail flatcar to pad | 2.8 km | 60 min |
| Soyuz | Baikonur MIK 112 | 12-20 days | Rail, horizontal | 1.7 km | 2 hours (then erected at pad) |

The Russian/Soviet approach (Soyuz, Proton, Energia) historically favored horizontal integration — the vehicle is stacked on its side, transported horizontally on a rail car, then erected at the pad using a strongback rotated by hydraulic cylinders. This allows a smaller, simpler assembly building and a much faster rollout (Soyuz rollout is 2 hours vs 6+ hours for Saturn V). The trade is that horizontal integration places loads on the vehicle in an orientation it was not designed to sustain indefinitely, requiring dedicated support saddles along the tank walls.

## Vertical Assembly Building

The Vehicle Assembly Building at Kennedy Space Center is the defining artifact of vertical assembly. At 160m tall, 218m long, and 158m wide, it encloses 3,665,000 m³ of conditioned volume — one of the largest enclosed spaces in the world by volume. See [Vertical Assembly Building](./vehicle-assembly.vab-facilities.md) for the dedicated process article.

### Building Dimensions & Structure

| VAB Parameter | Value |
|---------------|-------|
| Total height | 160 m (525 ft) |
| Footprint | 218m × 158m (34,444 m²) |
| Enclosed volume | 3,665,000 m³ |
| Number of high bays | 4 (Bays 1, 2, 3, 4) |
| Number of low bays | 1 (Low Bay, transfer aisle) |
| High bay door aperture | 12.5m wide × 45m tall (each) |
| Structural frame mass | 98,500 t structural steel |
| Foundation depth | 49m (steel pipe piles to bedrock) |
| Floor loading | 2,400 kg/m² (high bay); 19,500 kg/m² (crawlerway entry) |
| Design wind load | 200 km/hr (Cat 5 hurricane) |

The VAB's structural steel frame is the largest single building frame ever erected for aerospace use — 98,500 tonnes of ASTM A-36 and A-441 steel, fabricated by the American Bridge Division of U.S. Steel and erected between 1962 and 1965. The frame is designed to withstand Category 5 hurricane winds (200 km/hr sustained) without yielding — a critical requirement, since a Saturn V stacked in the VAB represents a $185M (1969 dollars) investment that cannot be evacuated. The foundation consists of 4,225 steel pipe piles, each 40cm diameter × 49m long, driven to bedrock. The piles carry the combined weight of the building (98,500 t), the bridge cranes (10,000 t rated), and a stacked Saturn V (2,500 t) — a peak foundation loading of 2,400 kPa at the pile tips.

### Bridge Cranes

The VAB's lifting capability is anchored by two 175-tonne bridge cranes and one 325-tonne bridge crane, with a combined tandem lift capacity of **10,000 tonnes** (rated as a balanced dual-crane lift using custom equalizer beams). The Saturn V first stage (S-IC), at 84,400 kg dry, was the heaviest single lift; the S-II second stage at 36,000 kg was the most awkward due to its 10m diameter and 25m length.

| Crane Parameter | Value |
|----------------|-------|
| Main hook capacity (per crane) | 175 t (two cranes) + 325 t (one crane) |
| Tandem lift capacity | 10,000 t (balanced, equalizer beam) |
| Maximum lift height (high bay) | 141 m (from floor to hook at top position) |
| Hoist speed (full load) | 0.3-1.5 m/min (variable frequency) |
| Bridge travel speed | 1-15 m/min |
| Positioning accuracy | ±6 mm (laser-guided) |
| Crane runway mass | 2,200 t (per runway, 4 total) |

The cranes use laser-guided positioning — a fan-beam laser tracker mounted on the hook reads retroreflectors on the high bay walls at 10 Hz, enabling the operator to hold the load within ±6 mm of target position even at the top of the 141m lift envelope. This precision is required because stage-to-stage interface alignment tolerances on Saturn V were ±0.060 inches (1.5mm) radially at the interstage bolt circle.

### Environmental Controls

The VAB interior is climate-controlled to maintain 22°C ±5°C and 50% ±10% relative humidity. The high bay is divided into clean zones during stacking: the immediate work area around the vehicle is enclosed in a Class 100K (ISO 9) soft-wall cleanroom tent, with HEPA-filtered supply air providing 20 air changes per hour. The most contamination-sensitive operations (payload fairing installation, optics integration) are done at ISO 8 (Class 10K).

The 3,665,000 m³ volume requires 4 × 5,000 kW air handling units to maintain conditioning during Florida summers (35°C / 95% RH outside design). The total HVAC electrical draw is 12-18 MW during peak summer conditions — enough power for a town of 5,000 people.

## Transporter / Erector & Crawler

Once stacked and tested, the vehicle must be moved to the launch pad. For LC-39 operations, this is the **Crawler-Transporter (CT)** — two 6.6-million-kg tracked vehicles (CT-1 and CT-2) built by Marion Power Shovel in 1965-1966 and upgraded continuously through Artemis. Each CT carries a Mobile Launch Platform (MLP) on its back, with the fully-stacked vehicle on top, and rolls at 1.6 km/hr over a dedicated crawlerway to the launch pad. See [Transporter/Erector & Crawler](./vehicle-assembly.transporter-erector.md) for the dedicated process article.

### Crawler-Transporter Specs

| Crawler Parameter | CT-1 / CT-2 Value |
|------------------|-------------------|
| Empty mass | 2,700 t (2,721 t) |
| Maximum payload (MLP + vehicle) | 5,450 t (Saturn V) / 5,265 t (SLS Block 1) |
| Gross mass (loaded) | 8,150-8,200 t |
| Length × width | 40m × 35m |
| Height (deck to ground) | 6.1 m |
| Number of tracks | 4 (2 per side) |
| Shoes per track | 57 |
| Shoe dimensions | 0.45m × 2.3m, 1.1 t each |
| Maximum speed (empty) | 3.2 km/hr (2 mph) |
| Maximum speed (loaded) | 1.6 km/hr (1 mph) |
| Minimum turning radius | 152 m |
| Fuel consumption (diesel) | 350 L/km (125 gal/mi) |
| Power plant | 2 × 2,750 hp Alco diesel (4,100 kW total) |
| Traction motors | 16 × 1,000 hp DC (via diesel-electric drive) |
| Leveling system | Hydraulic, laser-guided, ±15 cm over 30m span |

### Crawlerway

The crawlerway is a dedicated 5.6 km road from the VAB to LC-39A/B (and a 6.4 km branch to LC-39B for SLS), built to support the 8,200-tonne gross vehicle weight without settlement. The construction is:

| Crawlerway Layer | Thickness | Material |
|------------------|-----------|----------|
| Surface (wear) | 10-20 cm | Alabama river gravel, 4-8 cm rounded |
| Base course | 1.2 m | Crushed aggregate, compacted in 4 lifts |
| Subbase | 0.6 m | Selected borrow, sandy clay |
| Subgrade | Native | Florida coquina / sandy clay, compacted |

The use of rounded river gravel (not crushed stone) on the surface is deliberate: crushed stone interlocks and shears under the crawler's shoe pressure (up to 1.0 MPa), while rounded gravel rearranges and reconsolidates, distributing the load. The crawlerway requires periodic re-grading — typically every 6-10 rollouts — to restore the surface crown and fill in the track ruts (5-10cm deep after each transit).

### Leveling System

The crawler's most critical feature is its leveling system. The MLP and vehicle must remain within ±0.3° of vertical at all times during transport — any tilt greater than this shifts the propellant in the tanks (if loaded) and places bending moments on the thin-wall tank structure that can exceed design limits. The crawler uses four hydraulic jacking cylinders (one at each corner), each 1.8m bore × 2.4m stroke, controlled by a laser-guided closed-loop system. The laser level reference sits at the MLP centroid; servo valves modulate each cylinder at 5 Hz to hold the deck within ±15 cm of nominal across the 40m × 35m footprint — an angular tolerance of ±0.2°.

### Transporter/Erector Launcher (TEL)

For non-CT operations (Falcon 9 at SLC-40, Starship at Starbase, Soyuz at Baikonur), the transporter/erector launcher (TEL) is the equivalent ground support equipment. The TEL is a strongback truss that carries the vehicle horizontally (or vertically, for Starship), rolls to the pad on wheels or rails, and erects the vehicle to vertical using hydraulic cylinders. The Falcon 9 TEL is a 70m-tall, 600-tonne steel truss built by Haas Automation and SpaceX; it carries the Falcon 9 horizontally out of the hangar, erects it at the pad in 30 minutes, and serves as the umbilical carrier during fueling and launch.

| TEL Parameter | Falcon 9 (SLC-40) | Starship (OLM) | Soyuz |
|---------------|-------------------|----------------|-------|
| TEL mass | 600 t | 1,400 t (launch tower) | 350 t |
| Transport orientation | Horizontal | Vertical (built on pad) | Horizontal |
| Erection time at pad | 30 min | N/A (vertical integration) | 60 min |
| Strongback structure | Box truss, 70m tall | Steel lattice tower, 146m | Box truss, 55m |
| Erecting cylinders | 2 × hydraulic, 1,200 t each | N/A | 2 × hydraulic, 400 t |
| Umbilical carrier | Yes (TELUmbilical arm) | Yes (QD arms) | Yes |

## Stacking Sequence

The Saturn V / SLS-class vertical stacking sequence in the VAB:

1. **Mobile Launch Platform (MLP) delivery** (Day 1): MLP rolled into High Bay 3 on the crawler. The MLP is a 4,900-tonne, 49m × 41m × 8m two-deck steel structure that serves as the launch table, umbilical tower base, and flame deflector. The crawler lowers it onto 6 support pedestals and withdraws.
2. **Core stage transfer and mate** (Day 3-4): Core stage (SLS: 65m, 213 t) received from Pegasus barge, lifted by the 325-t crane to vertical on the MLP, and bolted to the four hold-down posts (each post carries 850 t of liftoff thrust load).
3. **Solid rocket booster stacking** (Day 5-10): Two (SLS) or four (Shuttle) SRB segments lifted individually, stacked on the aft skirt, and pinned to the core stage at the forward attach point. Each 5-segment SLS booster is 27m × 3.7m × 730 t assembled.
4. **Interim Cryogenic Propulsion Stage (ICPS) mate** (Day 11-13): Upper stage lifted and bolted to the core stage forward skirt.
5. **Orion spacecraft integration** (Day 14-18): Orion crew module + service module + launch abort system (LAS), pre-integrated at the Neil Armstrong Operations and Checkout Building, lifted as a single 85-tonne assembly and bolted to the ICPS.
6. **Payload fairing closeout** (Day 19-21): Final fairing panel installation, ordnance connection, leak check.
7. **Integrated systems test** (Day 22-28): Wet dress rehearsal (WDR) — full propellant load, terminal count to T-10 seconds, no engine start. Validate all interfaces.
8. **Rollout** (Day 30-31): Crawler rolls under the MLP, lifts it 6.1m, and transits to LC-39B at 1.6 km/hr over 8-12 hours.

## Integration Tolerances & Metrology

Vertical stacking demands the highest precision of any ground operation. A launch vehicle is, in essence, a stack of pressurized cylinders aligned coaxially to within a few millimeters — any misalignment introduces bending moments during the max-Q aerodynamic load that can exceed the thin-wall tank's design margin. The Saturn V's 110m stack was held coaxial to ±1.5 mm at every stage interface; SLS tightens this to ±0.8 mm.

### Stage-to-Stage Interface

| Interface | Tolerance | Measurement Method |
|-----------|-----------|-------------------|
| Radial alignment at interstage bolt circle | ±1.5 mm (Saturn V), ±0.8 mm (SLS) | Laser tracker, 6 points at 60° spacing |
| Axial stack-up height (cumulative) | ±25 mm over 110m stack | Laser ranger, base reference to LAS tip |
| Angular coaxiality (stage to stage) | ±0.05° (0.9 mrad) | Theodolite cross-check at 4 azimuth positions |
| Bolt preload (interstage bolts) | 70% of yield, ±5% | Hydraulic tensioner, 1,000+ bolts per interface |
| Umbilical plate alignment | ±0.5 mm | Mechanical pin gauge, 4-point engagement |

### Laser Tracker Metrology

The VAB uses a Leica AT960 laser tracker — an absolute-distance-measuring interferometer with ±15 μm + 6 μm/m accuracy over a 40m range — to verify every dimensional interface during stacking. The tracker is mounted on a fixed pier at the transfer-aisle level (Z=70m); retroreflectors are attached to the vehicle at known coordinate points. The system records actual-vs-nominal coordinates for 200+ measurement points per stage mate, and the data is reviewed by a tolerance review board before the next stage is lifted.

### Bolted Joint Quality

Interstage joints on Saturn V/SLS use 1.0-1.5 inch (25-38mm) diameter A-286 stainless steel bolts in circular patterns of 144-216 bolts per joint. Each bolt is preloaded to 70% of yield (~750 kN for a 38mm bolt) using a hydraulic tensioner — the bolt is stretched hydraulically, the nut is spun down finger-tight, then the hydraulic pressure is released, transferring the stretch into clamp load. Bolt preload is verified by measuring bolt elongation with an ultrasonic gauge; bolts failing the ±5% tolerance window are re-tensioned.

## Mobile Launch Platform (MLP)

The MLP is the structural foundation of the entire stack during assembly, rollout, and launch. It is a two-deck steel box structure, 49m × 41m × 8m, massing 4,900 t (Saturn) to 5,300 t (Artemis Mobile Launcher 1). The MLP serves three functions simultaneously — it is launch table, flame deflector base, and umbilical tower mount, all in one structure.

### Structural Functions

| MLP Function | Requirement | Implementation |
|--------------|-------------|----------------|
| Launch table (vehicle support) | Carry 2,500-3,000 t vehicle + 8,000 kN liftoff thrust | 4 hold-down posts (850 t thrust each), cast steel, water-cooled |
| Flame deflector base | Route exhaust into trench below pad deck | Center opening, 14m × 14m, refractory-lined |
| Umbilical tower mount | Support 106m-tall FSS with 8 umbilical arms | Forward deck hardpoints, 1,200 t design load |
| Crawler interface | Distribute 8,200 t gross mass to 228 crawler shoes | Six 1.5m-tall support pedestals at deck perimeter |

### Hold-Down Posts

The four hold-down posts are the single most heavily-loaded individual mechanical elements at the launch complex. Each post is a 1.8m-tall forged steel column carrying one quarter of the vehicle's liftoff thrust (Saturn V: 8,500 kN per post; SLS Block 1: 9,800 kN per post) plus the dead weight of the vehicle. The post has a tapered top with a mechanical frangible bolt — a 7.6cm diameter explosive bolt that shears when commanded at T-0, releasing the vehicle. The post is water-cooled internally (60 L/min flow) during engine start to prevent the 2,500°C exhaust plume from melting the post top during the 5-7 seconds between engine ignition and frangible bolt release.

### MLP Refurbishment

Between launches, the MLP undergoes a 30-60 day refurbishment cycle: replacement of the four frangible bolts ($40,000 each), reapplication of ablative coating on the center opening, inspection of 4,000+ weld points in the umbilical tower, and replacement of any umbilical arm swing-arm hydraulic cylinders that show leakage. The MLP's service life is indefinite with periodic refurbishment — the three Saturn-era MLPs were retired after 30+ years; the Artemis Mobile Launcher 1 is designed for a 25-year / 20-launch service life.

## Quantitative Parameters

| Parameter | Value |
|-----------|-------|
| VAB height | 160 m |
| VAB footprint | 218m × 158m |
| VAB enclosed volume | 3,665,000 m³ |
| VAB structural steel mass | 98,500 t |
| VAB bridge crane capacity | 10,000 t (tandem, balanced) |
| VAB bridge crane lift height | 141 m |
| VAB crane positioning accuracy | ±6 mm |
| VAB high bay door aperture | 12.5m × 45m |
| VAB HVAC power draw | 12-18 MW peak |
| Crawler empty mass | 2,700 t (2,721 t) |
| Crawler maximum payload | 5,450 t (Saturn V stack) |
| Crawler gross mass (loaded) | 8,200 t |
| Crawler dimensions | 40m × 35m × 6.1m |
| Crawler maximum speed (loaded) | 1.6 km/hr (1 mph) |
| Crawler maximum speed (empty) | 3.2 km/hr (2 mph) |
| Crawler track shoes | 4 × 57 = 228 shoes |
| Crawler fuel consumption | 350 L/km |
| Crawler leveling accuracy | ±15 cm over 40m × 35m |
| Crawler power plant | 2 × 2,750 hp diesel-electric (4,100 kW) |
| Crawlerway length (VAB to LC-39A/B) | 5.6 km |
| Crawlerway length (VAB to LC-39B SLS) | 6.4 km |
| Crawlerway surface wear layer | 10-20 cm Alabama river gravel |
| MLP mass | 4,900 t (Saturn) / 5,300 t (Artemis ML) |
| MLP dimensions | 49m × 41m × 8m (two decks) |
| Falcon 9 TEL mass | 600 t |
| Falcon 9 TEL erection time | 30 min |
| Saturn V stacking tolerance | ±1.5 mm radial at interstage |
| Saturn V total stack height | 110.6 m |
| SLS Block 1 stack height | 98 m |
| Starship/Super Heavy stack height | 121 m |

## Strengths

- Vertical stacking in a 160m-tall VAB enables integration of any practical launch vehicle size
- 10,000-tonne tandem bridge crane lift capacity exceeds any foreseeable single-stage mass requirement
- Crawler-Transporter design (1965) remains serviceable through Artemis with upgrades — 60+ year service life
- Laser-guided crane positioning at ±6mm matches stage-to-stage interface tolerances
- Crawlerway with rounded gravel surface self-heals, distributing 8,200-tonne load without permanent deformation
- Horizontal integration (Soyuz, Falcon 9) trades stacking flexibility for 4-10× faster rollout

## Weaknesses

- VAB occupies 3.6M m³ of conditioned volume — 12-18 MW HVAC draw is a major operating cost
- Crawler-Transporter gross mass of 8,200 t limits crawlerway routing — bridge crossings and soft soils are infeasible
- 1.6 km/hr crawler speed means 8-12 hour rollout — weather must be forecast with high confidence across the full window
- Crawlerway refurbishment (re-grading) required every 6-10 rollouts — adds 2-3 weeks between flights
- VAB single-point-of-failure: damage to one high bay eliminates 25% of stacking capacity for months
- $185M+ stacked vehicle cannot be rapidly evacuated if hurricane strengthens beyond VAB's 200 km/hr design
- Horizontal integration limits vehicle length/aspect ratio — Soyuz at 49m is near the practical limit

## See Also

- [Vertical Assembly Building](./vehicle-assembly.vab-facilities.md) — VAB structure, cranes, environmental control
- [Transporter/Erector & Crawler](./vehicle-assembly.transporter-erector.md) — CT, TEL, crawlerway
- [Launch Complex](./launch-complex.md) — pad destination, MLP hard-down, umbilical interface
- [Construction](../construction/index.md) — structural steel and reinforced concrete heritage
- [Machine Tools](../machine-tools/index.md) — large gantry crane and precision alignment heritage
- [Metals](../metals/index.md) — steel for VAB frame, crawler chassis, MLP

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Ground Operations](./index.md) • [All Domains](../index.md)*
