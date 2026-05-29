# Railways

> **Node ID**: transport.railways
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`energy.steam-power`](../energy/steam-power.md), [`metals.forming`](../metals/forming.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-50+
> **Outputs**: railways
> **Critical**: No

## Railways

**Track construction**:
- **Subgrade**: Graded and compacted earth foundation. Ballast: crushed stone (10-15 cm layer) for drainage and load distribution.
- **Rails**: Initially iron straps on wooden stringers (strap rail — iron bar 2.5-5 cm wide × 1-1.5 cm thick nailed to timber). By the Energy stage: wrought iron or steel T-rails (inverted-T cross section, 15-30 kg/m, rolled in iron rolling mill). Rail length: 5-10 m sections, joined by fish plates (steel plates bolted through rail web holes).
- **Gauge**: Standard gauge 1435 mm (4 ft 8½ in). Standardize early — different gauges prevent network interoperability. This specific gauge is the global standard derived from Roman chariot wheel spacing.
- **Sleepers (ties)**: Timber (treated with creosote or tar), 2.4-2.7 m long × 20-25 cm wide × 12-15 cm thick. Spaced every 0.6-0.8 m. Rails spiked to sleepers with cut spikes (L-shaped iron spikes driven into wood).
- **Grade**: Maximum 2-3% for steam locomotives. Minimum curve radius 150-300 m. Gentle grades and curves = lower fuel consumption, higher speed, less wear.

**[Steam locomotive](../glossary/steam-locomotive.md)** (Energy):
- **Boiler**: Fire-tube boiler (fire tubes carry hot gas through water space). Pressure 0.7-1.5 MPa. Diameter 1-1.5 m, length 3-5 m. 50-200 fire tubes, 5 cm diameter each. Coal-fired firebox at one end, smokebox and chimney at other. Steam dome on top for dry steam collection.
- **Cylinders**: 2 cylinders, 30-50 cm bore, 40-60 cm stroke. Steam admitted alternately on each side of piston (double-acting). Slide valve or piston valve, actuated by Stephenson valve gear (link motion — adjustable cutoff for steam economy). Operating pressure: 0.7-1.0 MPa.
- **Power**: 50-200 HP. Speed: 30-80 km/h. Tractive effort: 2000-10000 kgf. Haul 50-200 tonnes on level track.
- **Driving wheels**: 4-8 driven wheels (coupled by connecting rods). Leading and trailing trucks (unpowered wheels) for stability.

**Strengths**:
- Hauls 50-200 tonnes on level track at 30-80 km/h — far beyond animal-drawn cart capacity
- Steam locomotives can be built with iron/steel and coal — no petroleum required
- Standard gauge (1435 mm) enables network interoperability across all connected lines

**Weaknesses**:
- Maximum 2-3% grade for steam locomotives — requires heavy earthwork for gentle gradients
- Iron or steel T-rails (15-30 kg/m) require a rolling mill — significant industrial investment
- Coal consumption ~2-5 kg/km per locomotive — logistics chain must keep pace

## Telegraph Communication

Railway signaling depends on telegraph circuits for block control and dispatch. See [Telegraph Communication](./telegraph.md) for the complete telegraph system. Key railway integration points: block instruments at each signal box, dispatcher circuits between stations, and point-to-point lines for train orders.

## Logistics Management

**Standardized containers**:
- Wooden crates in standard sizes (0.5 m³, 1.0 m³, 2.0 m³). Stackable. Labeled with contents, weight, destination, handling instructions. Enables efficient loading of carts, wagons, rail cars.

**Inventory management**:
- **Ledger system**: Double-entry bookkeeping. Track all materials in, out, and on hand. Perpetual inventory (update with every transaction). Periodic physical count to verify ledger accuracy.
- **Reorder points**: Minimum stock levels for critical materials. When stock falls below reorder point → trigger procurement. Prevents stockouts that halt production.
- **Buffer stocks**: Maintain 2-4 weeks of critical materials (coal, iron, copper, chemicals). Protects against supply disruption.

**Warehouse design**:
- Dry, well-ventilated building. Organized by material type. Heavy materials on ground floor (structural load). Flammables in separate fireproof building. Chemicals in ventilated, bunded (liquid-tight containment) area. Shelving for small items. Open floor for bulk materials. Loading dock for vehicle access. Inventory control at entry/exit.

## Signaling & Rolling Stock

**Railway signaling**:
- **Semaphore signals**: Blade (arm) pivoted on mast. Horizontal = stop (danger). Angled down 45° = proceed (clear). Night indication: red lamp (stop), green lamp (clear). Operated by wire pull from signal box (lever frame). Visible 300-500 m in daylight.
- **Block system**: Divide track into blocks (1-3 km sections). Only one train permitted in each block at a time. Block instruments (telegraph-based) at each block post — operator confirms train has cleared before allowing next entry. Prevents rear-end collisions. Absolute block: next train must wait for clear signal. Permissive block: following train may enter at restricted speed (lower capacity, used on lightly trafficked lines).
- **Interlocking**: Mechanical linkage between signals and points (switches) in lever frame. Prevents conflicting routes — operator physically cannot pull lever to set conflicting signal/point combination. Crush prevention built into the mechanism. Essential for junction safety.

**Freight and passenger car design**:
- **Flat car**: Simple wooden or steel deck on bogie (truck) frame. 10-20 tonne capacity. For timber, machinery, vehicles. Stake pockets for load securing.
- **Box car**: Enclosed wooden or steel body, sliding door. 15-30 tonne capacity. For bagged grain, manufactured goods, anything needing weather protection.
- **Tank car**: Cylindrical tank on frame. For liquids (water, oil, chemicals). Fill dome on top, drain valve at bottom. 15-30 m³ capacity.
- **Passenger coach**: Wooden or steel body with bench or individual seating. Sprung suspension (leaf springs or elliptic springs on bogies). 40-80 passengers per coach. Oil lamp lighting (later electric). Hardy vacuum or air brake system continuous through train — brake applies automatically if train parts or air pressure is lost.

## Track Engineering Detail

**Rail specifications**:
- Standard gauge 1435 mm (measured between inner faces of rail heads at 14 mm below the top surface). This gauge originated from the coal railways of northern England and became the global standard. Broad gauge (1676 mm, used in India, Argentina) offers better stability at speed. Narrow gauge (1000 mm, 1067 mm) is cheaper to build on difficult terrain but limits speed and axle load.
- Rail weight: 30-60 kg/m depending on traffic class. Light rail (30-40 kg/m) for branch lines and low-speed operations. Medium rail (40-50 kg/m) for main lines. Heavy rail (50-60 kg/m) for high-traffic, heavy-axle-load routes. Rail profile: the inverted-T cross-section has a wide flat foot (base, 100-140 mm wide) for stability, a narrow web (thin vertical section, 10-14 mm thick) for economy of metal, and a broad head (top, 60-70 mm wide) with a slightly crowned running surface for wheel contact.
- Rail steel: 0.5-0.8% carbon, 0.8-1.3% manganese. Yield strength 450-600 MPa. Hardness 250-320 HB on the running surface. The manganese content provides wear resistance and work-hardening: the rail surface gets harder under repeated wheel contact.

**Sleeper and ballast**:
- Timber sleepers: 2.4-2.7 m long × 20-25 cm wide × 12-15 cm thick. Softwood (pine, fir) creosote-treated, or naturally durable hardwood (oak, jarrah). Service life 20-40 years with treatment. Spacing 600-750 mm center-to-center (roughly 1300-1700 sleepers per km of track).
- Ballast: crushed stone (granite, basalt, or limestone), angular fragments 25-50 mm nominal size. Depth 150-300 mm below sleeper bottom. Functions: distribute wheel loads to the subgrade, drain water away from sleepers, hold sleepers in position laterally and longitudinally, allow tamping (lifting and leveling track by packing ballast under sleepers). Ballast must be clean: fines (material passing a 10 mm sieve) should not exceed 3% by weight, or drainage is impeded.
- Subgrade: the earth foundation below ballast. Compacted to 95% of maximum dry density. Top surface sloped 1:30 toward drainage ditches. Poor subgrade (clay, organic soil) requires a capping layer of granular material (sand or gravel, 150-300 mm thick) to prevent mud pumping into the ballast under repeated loading.

**Track geometry**:
- Maximum gradient: 2-3% for steam locomotives (1.5% preferred for heavy freight). Helper locomotives or pusher engines assist on steeper sections. Electric and diesel locomotives can handle 3-4% grades.
- Minimum curve radius: 150-300 m for conventional traffic (sharper curves increase flange wear and risk of derailment). Main line curves typically >500 m radius. Superelevation (banking of the track on curves): raise the outer rail 50-150 mm above the inner rail to counteract centrifugal force at design speed. Gauge widening on curves: add 5-20 mm to standard gauge on sharp curves to prevent wheel flanges binding against the rail.

**Points (turnouts)**:
- A pair of switch rails (tapered rails that move laterally) divert the train from one track to another. The switch rails are pivoted at the heel (one end) and moved by a lever (manual) or point motor (powered). A curved closure rail guides the wheels from the switch to the crossing (where the rails intersect at the "frog" — a gap in the rail that the wheel flanges pass through).
- Turnout radius: typically 150-300 m (sharper turnouts for low-speed yard work, gentler for main line diverging routes at speed). Number designation (No. 7, No. 10, No. 12): the ratio of the frog angle tangent. A No. 10 turnout has a frog angle of arctan(1/10) = 5.7°, suitable for 30-40 km/h diverging speed.

## Locomotive Engineering

**Firebox and boiler**:
- The firebox is a steel or copper chamber (copper conducts heat better, steel is stronger) where coal burns on a grate. Grate area 1.5-3.5 m². Coal consumption 2-5 kg/HP/hour (a 200 HP locomotive burns 400-1000 kg coal per hour at full power). The firebox is surrounded on three sides by water (the "water legs"), absorbing radiant heat directly from the fire. Firebox temperature: 1200-1400°C at the firebed.
- Boiler tubes: 50-200 tubes, 50 mm diameter each, running from the firebox tube plate to the smokebox tube plate. Length 3-5 m (matching the boiler barrel). Hot combustion gases pass through the tubes, heating the water surrounding them. Total heating surface area: 30-100 m² (firebox + tubes). The more heating surface, the more steam generated per hour.
- Smokebox: at the front of the boiler, downstream of the tubes. The blast pipe (a nozzle in the smokebox that directs exhaust steam upward up the chimney) creates a vacuum that draws hot gas through the tubes. The harder the locomotive works (more exhaust steam), the stronger the draft, and the harder the fire burns. This self-regulating draft makes the steam locomotive remarkably responsive to load changes.

**Steam circuit**:
- Steam generated in the boiler collects in the steam dome (the highest point, ensuring dry steam without water droplets). The regulator (throttle valve) in the dome controls steam flow to the cylinders. Steam passes through a pipe from the dome to the valve chest.
- Valve gear (Stephenson, Walschaerts, or Baker): controls the timing and duration of steam admission to each end of the cylinder. Cutoff: the fraction of the piston stroke during which steam is admitted. Early cutoff (15-25%) uses steam expansion for economy (less steam consumed per stroke). Late cutoff (50-80%) for maximum power (starting, climbing grades). The driver adjusts cutoff via a reversing lever (johnson bar) in the cab.
- Cylinder bore 300-500 mm, stroke 400-600 mm. At 10 bar boiler pressure, a 400 mm bore cylinder produces force = pressure × area = 10⁶ Pa × π × (0.2)² = 125,700 N (~12,800 kgf) on each stroke. Two cylinders, double-acting, at 2 strokes/revolution and 200 RPM: power output ~150 HP.

**Running gear**:
- Driving wheels: 4-8 coupled wheels connected by coupling rods. Wheel diameter 1.0-1.8 m. Larger wheels give higher speed (more ground covered per revolution) but lower tractive effort. Smaller wheels give better pulling power at lower speed. The Whyte classification system describes wheel arrangement: 4-4-0 (4 leading, 4 driving, 0 trailing), 2-6-2, 4-6-2 (Pacific), 2-8-0 (Consolidation).
- Valve gear linkage converts the rotary motion of the driving wheels into the back-and-forth motion of the slide valve (or piston valve) that admits steam to the cylinder. The Stephenson link motion uses two eccentrics per cylinder, connected by a curved link. Moving the link up or down changes which eccentric dominates, reversing the engine and adjusting cutoff in one motion.

## Rolling Stock Detail

**Freight wagons**:
- Capacity 15-20 tonnes per car (standard 2-axle design). Bogie (4-wheel truck) cars carry 30-50 tonnes. Underframe: steel I-beam or channel construction. Body: wood planking on steel frame (for box cars), flat steel deck (for flat cars), riveted steel plate (for tank cars).
- Couplers: link-and-pin (early, dangerous: operator must stand between cars to insert pin) replaced by automatic knuckle couplers (Janney coupler: cast steel coupler heads mate automatically when cars are pushed together, locked by a pin dropping into place. Uncouple by lifting the pin lever from the side of the car. Far safer).
- Brake evolution: hand brakes only (brakeman walks the roof of moving cars turning handwheels, one car at a time, extremely dangerous). Vacuum brake (train pipe evacuated by ejector on locomotive; applying brakes admits air to the pipe, releasing vacuum at each cylinder and applying brakes. Automatic: if the train parts, air enters the pipe and all brakes apply). Air brake (Westinghouse: compressed air at 5 bar in train pipe; applying brakes reduces pipe pressure, causing a triple valve on each car to direct air from a local reservoir to the brake cylinder. Faster response than vacuum. Automatic fail-safe).

**Passenger accommodation**:
- Coach length 15-22 m, width 2.8-3.2 m. Seating: bench seats (wooden slats, later padded) for 40-80 passengers per coach. Compartment design (European): 6-8 passengers per enclosed compartment opening to a side corridor. Open saloon design (American): rows of seats in an open body, aisles down the center.
- Heating: steam from the locomotive passed through pipes under the seats (effective but risks scalding). Later: hot water heating with a coal stove at one end of the coach.
- Lighting: oil lamps (kerosene, 1880s), then gas lighting (coal gas stored in pressure tanks under the coach, piped to mantle lamps inside), then electric lighting (dynamo on the car axle charging a battery bank, 32 V DC system).

## Railway Bridge Types

**Timber trestle**:
- Pile bents (driven timber piles, 25-35 cm diameter) with caps and bracing. Spans 5-10 m between bents. Stringers (timber beams, 25-40 cm depth) carry rail loads to the caps. Suitable for low-speed lines and temporary construction. Creosote-treated timber lasts 25-40 years. Height limit: 10-15 m (taller trestles become unstable under wind and lateral train loads).

**Iron and steel bridges**:
- Plate girder bridge: built-up I-beam (web plate 10-20 mm thick, flange angles and cover plates) spanning between stone or concrete abutments. Spans 15-30 m per girder. Multiple girders side by side carry twin tracks. The simplest metal railway bridge design.
- Truss bridge (through truss): the track runs through the truss (top chords overhead). Pratt or Warren truss configuration. Spans 30-100 m. Pin-connected for field erection without heavy riveting equipment. Member forces: bottom chord in tension, top chord in compression, diagonals carry shear. Design for Cooper's E-50 or E-60 loading (a standardized axle-load sequence representing a steam locomotive followed by loaded freight cars).
- Steel requires a rolling mill for structural shapes (I-beams, channels, angles, plates) and a riveting crew for assembly. Stone abutments carry the vertical and horizontal reactions. Foundation design must account for scour (water erosion around pier bases in rivers). Foundations to below the maximum scour depth, typically 3-8 m below riverbed.

## Locomotive Fuel and Water

**Coal supply**:
- A medium freight locomotive (150 HP) burns 2-4 kg coal per HP-hour at full working rate. At 150 HP, that is 300-600 kg/hour. For a 200 km main line run at 40 km/h (5 hours), coal consumption is 1500-3000 kg. Tender capacity: 5-10 tonnes of coal and 10,000-15,000 liters of water.
- Coal quality matters: bituminous coal with calorific value 25-30 MJ/kg is the standard locomotive fuel. Low-quality coal (high ash content) requires more frequent fire cleaning and produces less steam per shovel. Anthracite burns too slowly for locomotive fireboxes (low flame propagation rate). Coke (coal with volatiles driven off) burns clean and smokeless but costs more.

**Water requirements**:
- Steam locomotives consume water at 5-10 kg/HP/hour. A 150 HP locomotive evaporates 750-1500 kg (liters) of water per hour. At 5 hours running, that is 3750-7500 liters. Water stops every 50-80 km on main lines.
- Water quality: hard water (dissolved calcium and magnesium salts) causes scale buildup in boiler tubes. Scale thickness of 3 mm reduces heat transfer by 25% and can cause tube overheating and failure. Treat boiler water with soda ash (Na₂CO₃) to precipitate hardness, or blow down the boiler (drain a portion of water to remove concentrated dissolved solids) at every water stop. Soft water (rainwater, some rivers) is preferred.

**Water columns and coaling stages**:
- Water column: a vertical pipe with a swiveling funnel spout, fed from an elevated tank (timber trestle supporting a 50,000-100,000 liter wooden or steel tank). Gravity feeds water to the locomotive tender at 200-500 liters/minute. Filling a 10,000 liter tender takes 20-50 minutes.
- Coaling stage: an elevated platform (timber or steel) from which coal is shoveled or gravity-fed into the locomotive tender. A 5-tonne tender refill takes 15-30 minutes by hand. Mechanical coaling (bucket elevator or grab crane) reduces this to 5 minutes.

## Track Maintenance

**Inspection regime**:
- Daily visual inspection of main line track by section men walking their assigned 5-10 km section. Look for broken rails, loose bolts, displaced ballast, drainage blockages, and encroaching vegetation.
- Monthly geometry check: measure gauge (1435 mm ±3 mm tolerance on straight track, widened on curves), cross-level (difference in rail height across the track, 0 mm on tangent, superelevated on curves), and alignment (deviation from design centerline, ±10 mm on tangent, ±5 mm on curves). Use a track gauge bar and spirit level.
- Annual ultrasonic rail testing: detect internal cracks and defects not visible on the surface. A transducer sends ultrasonic pulses through the rail; reflections from cracks appear on a display. Replace rails with detected transverse defects before they propagate to a full break.

**Ballast tamping**:
- Track settles over time under repeated loading. Lift and level the track by pumping ballast under the sleepers. Manual tamping: use a lining bar (steel crowbar) to lift the rail, then pack crushed stone under the sleeper with a ballast fork. Mechanical tamper: vibrating tines insert into the ballast, compact it under the sleeper, and lift the track to the correct elevation in one operation.
- Tamping cycle: every 2-5 years on main line track, more frequently on heavy-traffic routes. Poorly maintained track develops geometry defects that cause rough riding, excessive wheel wear, and eventual derailment.

## Station Design and Yard Operations

**Station layout**:
- A through station has a main line with passing loops (sidings parallel to the main line, connected by points at each end). The passing loop allows faster trains to overtake slower ones, or trains to pass in opposite directions on single-track lines. Minimum loop length: longest expected train + 20 m clearance at each end. For 20-car freight trains (200 m), the loop needs 240 m.
- Platform height: 200-900 mm above rail head (low platforms require passengers to climb steps into coaches; high platforms allow level boarding). Platform length: matches the longest passenger train serving the station. A platform canopy (roof) protects waiting passengers from weather.

**Freight yard operations**:
- A classification yard sorts inbound cars by destination. The hump yard method: push a cut of cars to the top of a gentle incline (the hump, 2-4 m elevation above the classification tracks). Uncouple each car at the crest. Gravity rolls the car down the hump onto one of 10-30 classification tracks, switched by automated or manual points. Retarder devices (brakes on the rails) control car speed so it couples gently with cars already on the track.
- Flat switching: an alternative to hump yards for smaller operations. A switch engine (small locomotive) pulls cars onto a lead track, then shoves each car onto the correct classification track by moving back and forth. Slower than hump switching but requires less infrastructure. A small yard processes 100-200 cars per shift.

**Turntable and roundhouse**:
- A turntable is a steel bridge (10-20 m long) pivoting on a central bearing in a pit. The locomotive drives onto the bridge, which rotates to align with any stall track in the roundhouse (a semicircular engine shed with 5-15 stalls radiating from the turntable). Each stall has an inspection pit (a trench in the floor allowing access to the locomotive underside for maintenance).
- Turntable diameter must exceed the longest locomotive wheelbase (the distance between the outermost axles). For a 2-6-2 locomotive with 12 m rigid wheelbase, a 15 m turntable is required. The turntable is balanced: a single person can rotate it by hand with the locomotive centered on the pivot.

## Locomotive Maintenance

**Daily inspection (before each run)**:
- Boiler water level: visible in the gauge glass (two try-cocks as backup: top one blows steam, bottom one blows water, confirming level between them). If water is below the bottom try-cock, drop the fire immediately (boiler explosion risk from exposed crown sheet).
- Firebox inspection: open the firebox door and examine the crown sheet (the top of the firebox, surrounded by water) and the fusible plug (a brass plug filled with lead, screwed into the crown sheet. If water level drops below the crown sheet, the lead melts at 260°C and the plug blows, dumping water onto the fire and extinguishing it. A last-resort automatic safety device).
- Lubrication: oil all moving parts (connecting rod and coupling rod bearings, valve gear pins, spring hangers, axle boxes). Steam cylinder oil (compounded mineral oil with animal fat, 500-600 cSt viscosity) injected into the steam line lubricates the cylinder walls. Apply grease to all other bearings with a grease gun or oil can.

**Periodic maintenance**:
- Weekly: wash out the boiler (drain, flush with clean water to remove accumulated sludge and scale). Inspect firebox stays (threaded steel rods holding the inner and outer firebox plates together; a broken stay allows a leak and indicates local overheating). Inspect tubes for leaks (water weeping from tube ends into the smokebox).
- Monthly: examine all brake rigging, coupler pockets, draft gear, and spring hangers for cracks and wear. Measure flange thickness on driving wheels (minimum 18 mm, replace at 15 mm). Check track gauge under the locomotive (distance between wheel flanges; if gauge has spread, the wheels must be re-turned or replaced).
- Annual: hydraulic boiler test. Fill boiler with water, pressurize to 1.5× working pressure (e.g., 15 bar test for a 10 bar working boiler). Hold for 10 minutes. Inspect all joints, stays, and tube expansions for leaks. Any leak at test pressure requires repair before the locomotive returns to service. The boiler certificate is valid for one year.

## Railway Economics

**Operating costs**:
- Fuel: coal costs represent 15-25% of total operating costs for a steam railway. A 100 km main line with 10 trains per day consuming 2 tonnes of coal each burns 20 tonnes/day or 7300 tonnes/year. At bulk coal prices, this is a major ongoing expense.
- Labor: the largest single cost (40-50% of total). A steam locomotive needs a driver and a fireman. A station needs at least one operator (signalman, dispatcher, ticket agent). Track maintenance requires 1 section man per 2-3 km of track.
- Capital cost: locomotive (comparable to a small factory in cost and complexity), rolling stock, track, bridges, stations, and signaling. A 100 km single-track railway with 10 stations represents an investment equivalent to 5-10 years of regional economic output. The payoff comes from the 10-50× reduction in transport cost per tonne-km compared to road transport.

## Railway Gauge and Standards

**Gauge standardization**:
- The cost of gauge breaks (transferring cargo between different-gauge railways at junction points) is enormous: every item must be unloaded from one gauge car and loaded onto another, adding 12-24 hours and significant labor cost to each shipment. Standardize on one gauge from the start, even if it means building wider or narrower than local tradition dictates.
- Standard gauge (1435 mm) is the most common worldwide: Europe (most), North America, China, Australia (interstate). Broad gauge (1520 mm) in Russia and former Soviet states, (1676 mm) in India. Narrow gauge (1067 mm) in Japan, southern Africa, (1000 mm) in parts of South America and Southeast Asia. Choose based on expected traffic volume and terrain: broad gauge for high-capacity main lines, narrow gauge for mountainous terrain where construction cost is the binding constraint.

**Loading gauge**:
- The maximum permitted cross-section of a rail car (height and width above the rails). A standard British loading gauge is 3.9 m height × 2.7 m width. American loading gauge is larger (5.3 m × 3.3 m), allowing bigger cars and double-stack container trains. Tunnels, bridges, and station platforms must all provide clearance for the loading gauge plus a safety margin (typically 150-300 mm on each side).
- The structure gauge defines the minimum clearance envelope around the track that must be kept free of obstructions. Any bridge, tunnel lining, signal mast, or platform edge within this envelope is a fouling point and must be removed or the track realigned.

## Safety & Hazards

- **Boiler explosions**: Steam locomotive boilers can explode from low water, overpressure, or corrosion. Two safety valves, water gauge, regular inspection required.
- **Runaway trains**: Brake failure on gradients. Dead-man's control. Fail-safe brakes.
- **Coupling injuries**: Manual coupling crushes fingers. Use coupler bars. Never stand between cars on grade.
- **Derailment**: Speed, track condition, broken rails. Regular inspection. Speed limits.
- **Track worker safety**: Lookouts with flags or horns warn of approaching trains. Track workers must be able to clear the track within the sighting distance minus the stopping distance of the train. At 60 km/h, a 200-tonne freight train needs 300-500 m to stop. On single-track lines, use track warrants (authority to occupy a section of track, issued by dispatcher via signaling circuit).
- **Grade crossing collisions**: Trains cannot stop for obstacles. Install warning signs (crossbuck), bells, and gates at road crossings. Sight distance at crossing must allow a road vehicle to clear the track before an approaching train arrives.
- **Smoke and cinders**: Steam locomotives emit dense smoke and hot cinders from the chimney. Cinders start trackside fires in dry grass and timber trestles. Cinders in the eyes are a hazard for passengers in open coaches and for crew on the locomotive footplate. Issue goggles to footplate crew. Install spark arresters (a baffle or mesh screen in the smokebox) to reduce cinder emission.
- **Coal dust explosion**: In coal mines and coal handling facilities (coaling stages, tender loading), suspended coal dust explodes when ignited by a spark or flame. Keep coal dust concentrations below 50 g/m³ by ventilation and wet suppression. No smoking or open flames in coal handling areas. The same hazard applies to grain elevators (grain dust is explosively flammable above 40-60 g/m³).
- **Noise exposure**: Locomotive cabs exceed 100 dB at working speed (blast pipe, cylinder exhaust, wheel-rail noise). Prolonged exposure above 85 dB causes permanent hearing loss. Engine crews (driver, fireman) should use hearing protection (wax-impregnated cotton or malleable silicone ear plugs).
- **Asbestos exposure**: Steam locomotives used asbestos lagging (insulation) on boiler pipes, firebox crowns, and cylinder jackets. Asbestos fibers released during maintenance cause mesothelioma and asbestosis (latent period 20-40 years). Wet asbestos lagging before removal. Wear respiratory protection. Substitute with mineral wool or calcium silicate insulation where available.
- **Sand drying and handling**: Locomotives carry sand in a dome on top of the boiler, applied to the rails ahead of the driving wheels for adhesion on wet rails or steep grades. Sand must be dried (heated to 150-200°C in a sand dryer) to prevent freezing and clumping. Sand handling generates respirable silica dust. Wear dust masks when filling sand domes.
- **Hot water and steam burns**: Locomotive maintenance involves working near surfaces at 100-200°C. Steam at 10 bar has a temperature of 180°C and releases latent heat (2,260 kJ/kg) on condensation, causing far worse burns than dry heat at the same temperature. Insulate all exposed steam pipes. Wear leather gloves when handling boiler fittings. Never open a pressurized fitting; reduce pressure to atmospheric before disconnecting any joint.
- **Crane and lifting hazards**: Roundhouse and workshop cranes (overhead traveling cranes, 5-20 tonne capacity) lift locomotive components for repair. All crane lifts require a trained rigger. Never exceed the rated capacity. Use tag lines to control swinging loads. Inspect wire ropes and hooks before each shift.
- **Shunting (switching) injuries**: Yard crews coupling and uncoupling cars, operating hand-thrown points, and riding moving cars are at high risk for crushing, amputation, and fall injuries. The "hump man" who rides cars down the classification hump to apply hand brakes faces particular risk. All yard movements require positive communication between switch crew and engineer (hand signals or whistle codes). Never ride the leading car into a standing cut.
- **Slip and fall on ballast**: Walking on loose crushed stone ballast is inherently unstable. Rail workers frequently sprain ankles or fall, especially at night or when carrying equipment. Wear ankle-supporting boots with stiff soles. Walk between the rails (on the sleeper tops) rather than on the ballast shoulder. Use a lantern after dark.
- **Electrification hazard** (later stage): Once electric traction is introduced, overhead catenary wires carry 1500-25,000 V. Any contact with or near these wires is immediately lethal. Clearance below the wire: minimum 4.5 m at maximum wire sag (hot weather, maximum span). Maintenance on or near the catenary requires the section to be de-energized and grounded. Never raise any object (pole, ladder, scaffold) within 2 m of a live catenary wire.


## Materials

- **Rails**: Wrought iron (early) or steel T-rails, 0.5-0.8% carbon, 0.8-1.3% manganese, 30-60 kg/m. Produced in iron/steel rolling mills.
- **Sleepers (ties)**: Treated timber (creosote or tar), 2.4-2.7 m × 20-25 cm × 12-15 cm. Alternatively, concrete sleepers for longer service life.
- **Ballast**: Crushed stone (granite, basalt, limestone), angular fragments 25-50 mm, 150-300 mm depth.
- **Locomotive materials**: Steel boiler plate (firebox, tubes, barrel), copper or steel firebox, cast iron cylinder blocks, forged steel crankshafts, steel coupling rods.
- **Rolling stock**: Steel I-beam and channel underframes, wood or steel body panels, cast iron brake shoes, steel coupler heads.
- **Fuel**: Bituminous coal (25-30 MJ/kg) for steam locomotives. Water (treated for hardness) at 5-10 kg/HP/hour.

## Equipment

- **Track laying**: Rail lifts, spike mauls, track gauges, tamping bars, ballast forks, lining bars.
- **Maintenance**: Mechanical tampers, track geometry measurement tools, ultrasonic rail testing equipment, ballast regulators.
- **Yard operations**: Turntable (10-20 m), coaling stage, water columns with elevated tanks, classification hump with retarders.
- **Workshop**: Overhead traveling cranes (5-20 tonne), boiler shop with hydraulic test pump, wheel lathe for re-turning driving wheels, riveting equipment.

## Limitations

- **Capital intensity**: A 100 km single-track railway represents 5-10 years of regional economic output. Returns come over decades.
- **Fixed infrastructure**: Railways cannot reroute. Changes in industry or settlement patterns can strand railway investment.
- **Grade and curve constraints**: Maximum 2-3% gradient for steam, 150-300 m minimum curve radius. Mountainous terrain requires expensive tunnels and viaducts.
- **Coal and water logistics**: Steam locomotives consume 2-5 kg coal/HP/hour and 5-10 kg water/HP/hour. Water stops every 50-80 km, coaling every 200 km.
- **Boiler maintenance**: Annual hydraulic test, weekly washout, tube replacement every 5-10 years. Boiler failure is catastrophic.
- **Gauge standardization lock-in**: Once a gauge is chosen, all rolling stock, infrastructure, and maintenance facilities are locked to it. Changing gauge later is prohibitively expensive.

## See Also

- [Roads & Bridges](roads.md) — Complementary road transport network
- [Water Transport](shipping.md) — Alternative bulk transport
- [Steam Power](../energy/steam-power.md) — Steam engine principles and boiler design
- [Iron & Steel](../metals/iron-steel.md) — Rail and structural steel production
- [Telegraph](telegraph.md) — Railway signaling communication
- [Coal](../energy/coal.md) — Locomotive fuel supply
- [Machine Tools](../machine-tools/index.md) — Precision machining for locomotive components





[← Back to Transport](index.md)
