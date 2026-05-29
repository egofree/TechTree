# Aircraft Development

> **Node ID**: transport.aviation
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`chemistry.petroleum-alternatives`](../chemistry/petroleum-alternatives.md), [`energy.engine`](../energy/engine.md), [`machine-tools`](../machine-tools/index.md), [`metals.aluminum`](../metals/aluminum.md), [`textiles`](../textiles/index.md)
> **Enables**: [`transport.light-aircraft`](light-aircraft.md), [`marine.navigation`](../marine/navigation.md)
> **Timeline**: Years 10-50+
> **Outputs**: aircraft, aircraft_engines, propellers, aviation_fuel
> **Critical**: No


Without propulsion technology, civilization is limited to ground and water transport. Aircraft enable rapid reconnaissance, cargo delivery over difficult terrain, and serve as a powerful morale boost for the entire project. The Wright brothers flew in 1903 with bicycle-shop tools and a custom engine. With modern ultralight plans in hand, the challenge is manufacturing capability, not invention.

## Technologies & Systems

## Internal Combustion Engine for Aircraft

**[Engine design](../glossary/engine-design.md)** (single-cylinder or twin-cylinder, air-cooled):
- **Configuration**: Horizontally opposed twin (boxer) — compact, good balance, air cooling. Displacement 500-1200 cc. Power target 20-65 HP at 2000-3500 RPM. Weight target <30 kg (power-to-weight >0.5 HP/kg).
- **Bore and stroke**: Bore 80-100 mm, stroke 70-90 mm. Undersquare (stroke < bore) favors higher RPM. Compression ratio 6:1 to 8:1 (limited by fuel octane — see fuel section).

**Cylinder and head**:
- **Cylinder barrel**: Cast iron liner (3-5 mm wall) pressed into aluminum finned barrel (aluminum fins increase cooling surface area 10-20x). Alternately, machine fins directly into cast iron cylinder. Inside diameter bored and honed to ±0.01 mm tolerance. Surface finish 0.2-0.4 μm Ra (honed crosshatch pattern retains oil film).
- **Cylinder head**: Aluminum alloy casting (Al + 8-12% Si — aluminum-silicon alloy, good fluidity for casting, good thermal conductivity for cooling). Cast in sand mold. Machine combustion chamber, valve seats, spark plug hole, and bolt holes. Large cooling fins cast integral with head. Bolt to cylinder barrel via studs (steel studs threaded into barrel, nuts on top of head — allows thermal expansion).
- **Combustion chamber**: Hemispherical or wedge shape. Spark plug positioned near center for even flame propagation. Valve arrangement: overhead valves (OHV) — intake and exhaust valves in cylinder head, operated by pushrods from camshaft in crankcase.

**Crankshaft and connecting rod**:
- **Crankshaft**: Forge from medium-carbon steel (0.4-0.5% C). Machine main bearing journals and crankpins to ±0.01 mm tolerance, surface finish <0.2 μm Ra. Induction harden journal surfaces (heat surface layer to 850°C with induction coil, quench → hard surface, tough core). Balance dynamically (add or remove metal from counterweights until no vibration at operating RPM).
- **Connecting rod**: Forge from steel. I-beam cross-section (stiff, light). Big end (crankpin end): split, with bearing cap bolted on. Bearing: replaceable babbitt-lined bearing shells (babbitt = Sn + Cu + Sb alloy — soft, embeds particles, conformable) or bronze bushings. Small end (piston pin end): bronze bushing. Piston pin: hardened steel, 15-20 mm diameter, floating (rotates in both piston and rod).

**Piston and rings**:
- **Piston**: Cast iron or aluminum alloy. Aluminum lighter (reciprocating weight matters at high RPM) but expands more (require larger clearance: 0.05-0.10 mm at skirt vs. 0.02-0.05 mm for cast iron). Machine ring grooves (2-3 compression rings + 1 oil control ring). Crown shape matches combustion chamber.
- **Piston rings**: Cast iron split rings (expand against cylinder wall). Compression rings (top 1-2): rectangular or barrel-faced cross-section, 2-3 mm thick, gap 0.3-0.5 mm when installed. Seal combustion pressure. Oil control ring (bottom): slotted, scrapes excess oil off cylinder wall, vents oil back to crankcase through holes in piston.
- **Cylinder bore clearance**: 0.05-0.10 mm (aluminum piston in iron liner). Too tight → seizure when hot. Too loose → piston slap (noise, blow-by gas, oil consumption).

**Valve train**:
- **Valves**: Intake valve — stainless steel or nickel alloy (lower temperature, ~300-400°C). Exhaust valve — high-nickel alloy (Inconel-type, withstands 700-900°C exhaust gas). Stem diameter 7-9 mm. Head diameter: intake 30-40 mm (larger — more flow area for intake), exhaust 25-35 mm. Face angle 45°. Seat width 1.5-2.5 mm. Machine seat and face to gas-tight fit (grind with lapping compound).
- **Valve springs**: Steel wire coil springs (spring steel: 0.6-0.7% C, heat-treated). Keep valves closed and following cam profile at maximum RPM. Spring force 100-300 N at installed height. Prevent valve float (spring cannot follow cam at excessive RPM → valves don't close → loss of compression → engine damage).
- **Camshaft**: Cast iron or forged steel. Cam lobes hardened (induction hardening). Machine cam profile on lathe with template follower (or grind on cam grinder). Profile designed for specified valve timing: open intake at 5-25° before top dead center (BTDC), close 40-60° after bottom dead center (ABDC). Open exhaust 40-60° BBDC, close 5-25° ATDC. Duration ~240-280° of crank rotation.
- **Pushrods and rockers**: Steel pushrods (6-8 mm diameter, tubular for lightness). Rocker arms: stamped or forged steel, ratio 1.2-1.5:1 (multiply cam lift for valve lift). Valve clearance (lash): 0.15-0.30 mm cold (allows for thermal expansion — too tight → valve doesn't close, too loose → noisy, reduced lift).

**Carburetor**:
- **Principle**: Venturi effect — air flows through constriction (venturi), velocity increases, pressure drops. Fuel nozzle at venturi throat — low pressure draws fuel from float bowl. Fuel atomizes in air stream → combustible mixture.
- **Construction**: Aluminum or zinc alloy body. Brass venturi (20-30 mm throat diameter). Float chamber (brass float maintains constant fuel level). Main jet (brass orifice, 0.8-1.5 mm diameter — controls fuel flow at full throttle). Idle circuit (separate small orifice for idle mixture). Throttle plate (butterfly valve — controls airflow). Choke (restricts airflow when cold → richer mixture for starting).
- **Tuning**: Adjust main jet size for correct air-fuel ratio (stoichiometric: 14.7:1 for gasoline, slightly rich 12-13:1 for maximum power). Read spark plug color: white/gray = too lean (hot, engine damage), dark brown = correct, black/sooty = too rich (wasteful, fouls plugs). Adjust idle mixture screw for smooth idle.

**Ignition system**:
- **[Magneto](../glossary/magneto.md)** (self-contained, no battery needed — critical for aircraft reliability):
  - Rotating magnet (mounted on engine camshaft or accessory drive) induces current in primary coil. Interrupter (points — mechanical switch, opened by cam on magneto shaft) breaks primary current → rapid magnetic field collapse → high voltage (10,000-30,000V) induced in secondary coil → current jumps spark plug gap → spark ignites mixture.
  - Spark plug: Steel shell with ceramic insulator (alumina). Center electrode (nickel alloy). Ground electrode (nickel alloy). Gap: 0.5-0.8 mm. Thread: 14 mm × 1.25 mm pitch (common size).
  - **Timing**: Spark occurs 20-35° before top dead center (BTDC) — flame front needs time to propagate across combustion chamber before piston reaches TDC for maximum pressure on power stroke. Adjustable via magneto-to-engine timing. Too advanced → detonation (knock — uncontrolled combustion, can destroy engine). Too retarded → loss of power, overheating.

**Fuel**:
- **[Gasoline](../glossary/gasoline.md)** (ideal): From petroleum distillation (Petrochemicals), 30-200°C fraction. Octane rating important — higher octane resists detonation at higher compression ratios. Early gasoline: 40-60 octane (limit compression to ~5:1). Tetraethyl lead (Pb(C₂H₅)₄) additive raises octane (lead deposits lubricate valves — but lead is toxic. Use only if necessary for engine reliability).
- **[Ethanol](../glossary/ethanol.md)** (alternative): From fermentation (Petrochemicals). Octane ~100 (excellent anti-knock). Energy density ~60% of gasoline by volume → larger fuel tank needed. Hygroscopic (absorbs water). Attacks some rubber and metals. Carburetor jets must be enlarged ~30% (ethanol requires richer mixture — 9:1 stoichiometric vs. 14.7:1 for gasoline).
- **Fuel consumption**: 200-300 g/HP/hour (specific fuel consumption). 40 HP engine burns 8-12 kg/hour gasoline. For 2-hour flight: 16-24 kg fuel.

**Lubrication**: Total-loss splash system (simplest for aircraft). Oil reservoir in crankcase. Splash from crankshaft dipping in oil or oil slinger throws oil onto cylinder walls, bearings, cam. Oil eventually burns or leaks out — add oil periodically. Use castor oil (high-temperature stability, excellent lubricity, doesn't break down at engine temperatures) or mineral engine oil (SAE 30 or 40 weight).

**Strengths**:
- Horizontally opposed twin (boxer) configuration provides natural balance and compact form
- Air cooling eliminates radiator, water pump, and coolant — fewer failure points
- Power-to-weight ratio >0.5 HP/kg achievable with 1930s-era materials and tolerances

**Weaknesses**:
- Requires ±0.01 mm tolerance on cylinder bores and crankshaft journals — precision machining essential
- Aluminum cylinder heads demand aluminum-silicon casting capability (8-12% Si alloy)
- Valve springs must prevent valve float at 2000-3500 RPM — requires spring steel (0.6-0.7% C, heat-treated)

## Airframe Construction

**Design** (tube-and-fabric ultralight):
- **Wingspan**: 8-12 m. **Wing area**: 12-20 m². **Wing loading**: 20-40 kg/m² (lower = lower stall speed, gentler handling). **Empty weight**: 150-250 kg. **Gross weight**: 250-400 kg. **Stall speed**: 35-50 km/h. **Cruise speed**: 70-120 km/h. **Range**: 100-300 km.
- **Wing**: High-wing or low-wing configuration. High-wing: better ground clearance, better downward visibility, simpler strut bracing. Low-wing: shorter landing gear, better crash protection, easier fueling. Choose based on construction preference.
- **Lift**: L = ½ρv²SCL, where ρ = air density (1.225 kg/m³ at sea level), v = airspeed, S = wing area, CL = lift coefficient (0.5-1.5 depending on angle of attack and airfoil). At 80 km/h (22.2 m/s), 15 m² wing, CL = 0.8: L = ½ × 1.225 × 22.2² × 15 × 0.8 = ~3620 N (~370 kg force). Sufficient to lift ultralight aircraft.
- **Airfoil**: Clark Y or similar flat-bottom airfoil (easy to build — flat lower surface simplifies rib construction). Thickness 12-15% of chord. CLmax ~1.5 with plain flaps.

**Structure**:
- **Fuselage**: Steel tube (seamless mild steel or 4130 chromoly, 15-25 mm diameter × 0.9-1.5 mm wall) truss framework. Cut tubes to length, fit, weld joints (oxy-acetylene or oxy-propane brazing/welding). Triangulated structure — every bay is a triangle for rigidity. Engine mount: heavier steel tubes (25-35 mm) at front, bolted to engine crankcase via rubber vibration isolators.
- **Wing spars**: Wood (Sitka spruce or Douglas fir — high strength-to-weight ratio, straight grain). Main spar: 50-80 mm × 25-40 mm rectangular cross-section (dimensions sized by bending load — must support aircraft weight + 3-4g maneuver loads). Rear spar: smaller (40-60 mm × 20-30 mm). Spars run full wingspan. Plywood shear web between spars (transfers loads between top and bottom spar caps → box spar construction, stronger than solid spar for same weight).
- **Wing ribs**: Thin plywood (2-3 mm) or built-up wood (capstrips + gussets). Airfoil shape cut into rib. Spars pass through notches in ribs. Ribs spaced 200-400 mm along span. Maintain airfoil shape between spars. Attach fabric covering to rib flanges.
- **Struts and bracing**: Steel tube lift struts (20-25 mm diameter) from fuselage to wing spar — carry wing loads to fuselage. Flying wires (steel piano wire, 3-5 mm diameter, in tension) brace wings against positive and negative g-loads. Landing wires brace against negative loads. Turnbuckles on all wires for tension adjustment and rigging (set wing incidence and dihedral angle).

**Control surfaces**:
- **Ailerons**: On outer portion of trailing edge, one on each wing. Move differentially (one up, other down) → roll the aircraft. Construction: wood or aluminum frame, fabric-covered. Hinged to wing rear spar. Cable-and-pulley linkage to control stick.
- **Elevator**: On horizontal tail, trailing edge. Move together (both up or both down) → pitch nose up or down. Construction similar to ailerons. Pushrod or cable linkage to control stick.
- **Rudder**: On vertical tail, trailing edge. Moves left/right → yaw the aircraft. Cable linkage to foot pedals.
- **Control forces**: 20-50 N stick force for normal maneuvers. Cable-and-pulley system: 2-3 mm steel cables run in nylon or brass sheaves (low friction pulleys). Cables tensioned to 100-200 N (prevents slack and sloppy response).

**Landing gear**:
- **Tricycle or tailwheel**: Tailwheel simpler, lighter, more demanding to ground-handle (tends to ground-loop — uncontrolled swerve on landing). Tricycle: steerable nosewheel, more stable, easier to land. Choose based on pilot experience.
- **Main gear**: Steel tube struts with bungee cord or rubber spring shock absorption (bungee cord: multiple wraps of rubber rope absorbing vertical impact). Axle: steel tube, 20-25 mm diameter. Wheels: 350-500 mm diameter, spoked or solid disc. Tires: pneumatic, 2-4 bar pressure, 150-250 mm wide. Brake: drum brake on main wheels (mechanical — cable operated, differential braking for steering on tailwheel type).

## Propeller

**Design**:
- **Diameter**: 1.5-2.0 m. **Pitch**: 800-1200 mm (theoretical forward travel per revolution). **Blades**: 2. **RPM**: 2000-3000 (direct drive from engine, or reduction gear for larger prop at lower RPM).
- **Blade design**: Airfoil cross-section (Clark Y or similar). Blade angle (pitch) decreases from hub to tip — outer portions travel faster and need lower angle of attack to maintain optimal lift (thrust). Width 100-150 mm at widest point, tapering toward tip.
- **Thrust**: T = (η × P) / v, where η = propeller efficiency (0.6-0.8 for well-designed prop), P = engine power (W), v = forward speed (m/s). At 40 HP (30 kW) and 25 m/s (90 km/h): T = 0.7 × 30000 / 25 = 840 N (~86 kgf thrust). This accelerates aircraft to cruise speed and maintains flight.

**Construction**:
- **Wood**: Hardwood (birch, maple, or oak). Laminate 5-7 layers of wood (alternating grain direction — prevents warping, increases strength) with waterproof glue (casein glue or, later, epoxy). Rough-carve on bandsaw. Finish-carve with drawknife, spokeshave, and rasp. Balance statically (hang on horizontal axle — heavy side drops → remove material until balanced) and dynamically (spin and check for vibration at operating RPM).
- **Protection**: Apply multiple coats of linseed oil or varnish (waterproof, prevent moisture absorption → weight change and imbalance). Leading edge protection: brass or copper tipping strip (screws + epoxy) — protects against stone/erosion damage.
- **Finish**: Sand smooth (120 → 220 → 400 grit). Final coat of clear varnish or paint. Check balance after finishing. Mark tracking marks (chalk on each blade tip — spin and observe marks should overlap perfectly from the side).

## Fabric Covering & Finishing

**Fabric**:
- Cotton or linen fabric (Textiles), tightly woven, ~100-200 g/m². Grade A aircraft cotton (Mercerized — treated with NaOH to increase strength and dye affinity) or linen. Modern alternative: Dacron (polyester — much stronger, more durable, but requires advanced polymer chemistry). Cut fabric panels with 5-10 cm overlap at edges.

**Covering process**:
1. **Attach fabric**: Lay fabric over airframe. Tack edges with copper rivets or fabric nails (small nails with broad heads). Pull fabric taut (hand-tension — no wrinkles). Overlap seams by 3-5 cm. Stitch through fabric and rib caps with waxed linen thread (rib-stitching — prevents fabric from billowing in flight). Stitch spacing: 25-50 mm.
2. **Shrinking**: Dampen cotton fabric with water → tightens as it dries (natural cotton shrinks ~5%). For Dacron: heat with iron (150-200°C) → fabric shrinks ~10% → drum-tight. Creates smooth aerodynamic surface.
3. **Dope application**: Apply nitrocellulose dope (see below) in multiple thin coats. First coat (clear dope): saturates fabric, bonds to structure. Subsequent coats: build film thickness, fill weave. Aluminum-pigmented dope (silver): UV barrier — prevents sunlight from degrading fabric. Final coat: colored dope for visibility and identification. Total: 6-10 coats, ~100 g/m² dope applied.

**Nitrocellulose dope**:
- **Chemistry**: Cellulose (cotton linters or wood pulp) + nitric acid + sulfuric acid → nitrocellulose (cellulose nitrate, 10-12% nitrogen). Dissolve nitrocellulose in acetone + butyl acetate (solvent blend) + plasticizer (dibutyl phthalate — prevents dope film from becoming brittle) + aluminum pigment (for UV barrier coat).
- **Manufacture**: Soak cellulose in mixed acid (HNO₃ + H₂SO₄) at 20-30°C for 30-60 minutes. Nitration is exothermic — cool to prevent runaway. Dump into large volume of water to quench. Wash extensively (remove all acid — residual acid degrades nitrocellulose). Boil in water (stabilization — removes unstable nitrated products). Dry. Dissolve in solvent blend. This is the SAME chemistry used for smokeless powder (gunpowder) — handle with care.
- **Properties**: Dope shrinks as solvent evaporates → further tightens fabric. Forms hard, waterproof, taut skin. Nitrocellulose is flammable — apply in well-ventilated area, no ignition sources. Acetone fumes are heavier than air — explosive mixture. Fire hazard is REAL — many early aircraft were lost to hangar fires from dope fumes.
- **Alternative dope**: Cellulose acetate butyrate (CAB) dope — less flammable than nitrocellulose. Requires cellulose acetate (from cellulose + acetic anhydride + acetic acid — see Petrochemicals, Polymers).

## Flight Testing

**Ground testing first**:
- **Engine test stand**: Bolt engine to heavy wooden or steel test stand. Run at varying throttle for hours. Monitor temperature (cylinder head <250°C for air-cooled), oil pressure, fuel consumption, spark plug condition. Fix all issues before installing on aircraft.
- **Taxi tests**: With aircraft fully assembled, taxi at increasing speeds on smooth runway. Check control surface response, engine performance under load (prop provides thrust and load — engine must maintain RPM), braking effectiveness, structural integrity (no excessive vibration, no loose wires or fittings).
- **Ground resonance**: Run engine at full power, aircraft held by ground crew. Check for resonance vibrations in structure. If resonant frequency of structure matches engine RPM → catastrophic vibration → stiffen structure or add damping.

**First flight**:
- Choose calm day (wind <10 km/h). Long, smooth runway (grass or packed earth, 300+ m). Emergency landing fields along expected flight path. Pilot experienced (ideally — but in a bootstrapping scenario, this may be the first pilot. Accept the risk. The Wright brothers taught themselves).
- **Flight plan**: Take off, climb to 30-50 m altitude, fly one circuit of the field, land. Total flight time: 1-5 minutes. If anything feels wrong → land immediately.
- **Post-flight inspection**: Check every bolt, wire, weld, and fabric attachment. Look for cracks, loose fittings, elongated bolt holes, fretting marks. Fix everything before next flight. Progressive envelope expansion: longer flights, higher altitude, steeper turns, with careful inspection between each expansion.

## Integration Points

| Stage | Contribution |
|----------|-------------|
| Metallurgy | Steel tubing and wire for airframe structure |
| Machine Tools | Machine tools for precision engine parts, propeller carving |
| Energy | Internal combustion engine development, spark ignition |
| Chemistry | Nitrocellulose dope for fabric, aluminum for later airframes |
| Textiles | Fabric for aircraft covering (cotton, linen) |
| Lubricants | Castor oil and mineral oil for engine lubrication |
| Petrochemicals | Gasoline fuel, acetone for dope, solvents for finishes |

## Key Deliverables

- Flyable ultralight airframe (tube-and-fabric or wood-and-fabric)
- Reliable small internal combustion engine (20-65 HP, air-cooled)
- Carved and balanced wooden propeller
- Doped fabric covering system
- Fuel supply chain (gasoline or ethanol)
- Ground test infrastructure (engine test stand, runway)
- Progressive flight test program with inspection protocol

## Flight Instruments & Navigation

## Basic Instruments

**[Altimeter](../glossary/altimeter.md)** (barometric):
- An aneroid barometer calibrated in altitude. A sealed metal capsule (thin-walled brass or beryllium copper, partially evacuated) expands as atmospheric pressure decreases with altitude. A mechanical linkage converts capsule expansion to needle rotation on a dial marked 0-3000 m (or higher). Sensitivity: 10 m per hPa pressure change near sea level.
- Setting: the altimeter reads correctly only if set to the local barometric pressure at the departure airfield before flight (QFE setting gives height above the airfield; QNH setting gives altitude above mean sea level). Forgetting to set the altimeter is a leading cause of controlled-flight-into-terrain accidents. Altimeter error in non-standard temperatures: cold air (denser than standard) causes the altimeter to over-read (aircraft is lower than indicated). Rule of thumb: 4% error per 10°C deviation from standard temperature.

**[Airspeed indicator](../glossary/airspeed-indicator.md)** (pitot-static):
- A pitot tube (open-ended tube facing forward into the airstream) measures total pressure (static + dynamic). A static port (flush opening on the fuselage side) measures ambient static pressure. The instrument subtracts static from total pressure to obtain dynamic pressure: q = ½ρv². The dial is calibrated in km/h (or knots) assuming standard sea-level air density (1.225 kg/m³).
- At altitude, air density is lower than at sea level, so the indicated airspeed reads lower than true airspeed. At 2000 m altitude (ρ = 1.0 kg/m³), an indicated airspeed of 80 km/h corresponds to a true airspeed of 80 × √(1.225/1.0) = 89 km/h. The pilot must apply a density altitude correction to get groundspeed for navigation.
- Stalling speed, maneuvering speed, and structural limits are all functions of indicated airspeed, not true airspeed. The pilot flies by indicated airspeed regardless of altitude.

**Magnetic compass**:
- A magnetized needle or card pivoting on a jewel bearing in a fluid-filled case (mineral oil dampens oscillation). Reads magnetic heading relative to Earth's magnetic field. Errors: deviation (magnetic fields from the engine and steel airframe distort the compass reading; compensate with small corrector magnets, and record residual deviation on a correction card mounted next to the compass, e.g., "for N steer 358°, for E steer 092°").
- Acceleration error: on east/west headings, accelerating makes the compass swing toward north, decelerating toward south. Turning error: during a banked turn, the compass lags on northerly headings and leads on southerly headings. The rule "north lags, south leads" reminds pilots to roll out of turns early on cardinal headings.

## Navigation Calculations

**Wind triangle**:
- Three vectors: heading/airspeed (the direction the aircraft points and its speed through the air), wind direction/speed (the movement of the air mass), and track/groundspeed (the actual path over the ground). The heading vector plus the wind vector equals the track vector.
- Wind correction angle (WCA): the angular difference between heading and track. If wind blows from the left, the pilot steers into the wind (right of the desired track) to maintain the desired ground track. WCA = arcsin(wind_speed × sin(wind_angle) / true_airspeed). For a 30 km/h crosswind component at 90 km/h true airspeed: WCA = arcsin(30/90 × sin(90°)) = arcsin(0.33) = 19°.
- Groundspeed: true airspeed adjusted for the headwind or tailwind component along the track. Groundspeed = √(TAS² + wind_speed² - 2 × TAS × wind_speed × cos(wind_angle_to_track)). A 15 km/h headwind at 90 km/h TAS gives 75 km/h groundspeed. Over a 150 km leg, flight time = 150/75 = 2.0 hours. A 15 km/h tailwind gives 105 km/h groundspeed and 1.43 hours for the same leg.

**Dead reckoning for aircraft**:
- Plot the intended course on a map. Measure distance and true heading. Apply magnetic variation (difference between true north and magnetic north, varies by location, shown on aviation charts) to get magnetic heading. Apply compass deviation from the correction card to get compass heading.
- Calculate groundspeed from TAS and wind. Divide leg distance by groundspeed to get estimated time en route (ETE). Multiply fuel consumption rate (8-12 kg/hour for a 40 HP engine) by ETE to get fuel required. Add 30 minutes reserve fuel (mandatory for VFR flight).

## Doped Fabric Construction

**Fabric shrinkage and tensioning**:
- Cotton and linen fabric shrinks when treated with nitrocellulose dope. The dope solvent (acetone + butyl acetate) evaporates and the nitrocellulose film contracts, pulling the fabric drum-tight. Cotton shrinks approximately 5-10% overall through the doping process. This tension is what gives the fabric covering its aerodynamic smoothness and structural contribution (a doped fabric panel resists air loads in the same way a drum head resists a drumstick).
- A typical covering sequence: 2 coats of clear dope (saturates fabric, bonds to airframe), 2-3 coats of aluminum-pigmented dope (UV barrier), 2-3 coats of colored finish dope. Total applied weight: 80-120 g/m² of dope on top of 100-200 g/m² of base fabric. A 15 m² wing panel therefore carries 3-5 kg of doped fabric.
- Inspection: tap the fabric with a light fingertip. A drum-tight "ping" sound indicates good tension. A dull "thud" means the fabric has lost tension (dope aging, moisture damage) and needs re-doping or replacement. Fabric tension test: a standard probe (3 mm diameter rod under 1.5 kg load) should not depress the fabric more than 15 mm at mid-bay between ribs.

**Wood spar design considerations**:
- Spruce and Douglas fir are the preferred spar materials because of their high specific strength (strength-to-weight ratio). Sitka spruce: density 450 kg/m³, bending strength 75 MPa, modulus of elasticity 11 GPa. Specific strength = 75 × 10⁶ / 450 = 167 kN·m/kg. By comparison, mild steel: density 7850 kg/m³, bending strength 250 MPa, specific strength = 32 kN·m/kg. Spruce is 5× better than steel per unit mass in bending.
- I-beam spar: two flanges (top and bottom, bearing the bending loads) separated by a web (bearing shear loads). Flange area sized by maximum bending moment: M = (load × span²) / 8 for a uniformly loaded beam. For a 10 m wing spar carrying 2000 N/m lift load: M = 2000 × 10² / 8 = 25,000 N·m. Required section modulus Z = M / σ_allowable = 25,000 / (10 × 10⁶) = 0.0025 m³ (using allowable stress of 10 MPa with safety factor applied to the 75 MPa ultimate).
- Box spar: two vertical plywood webs between upper and lower spruce cap strips. The plywood web carries shear; the cap strips carry bending. Box spars resist torsion better than I-beams because the closed cross-section has much higher torsional stiffness. Glue joints between web and caps are critical: any gap or poor glue bond creates a stress concentration and potential failure origin.

## Safety Concerns

- **Engine failure in flight**: Plan glide approaches (identify emergency landing spots). Aircraft must be able to glide without engine (glide ratio 8:1 typical for ultralight — at 50 m altitude, can glide 400 m to landing).
- **Structural failure**: Do not exceed design load limits (typically +4g / -2g). Avoid steep spirals, high-speed dives, abrupt control inputs. Progressive flight envelope expansion.
- **Fire**: Fuel + hot engine + air. Firewall (steel sheet between engine and cockpit). Fuel lines routed away from exhaust. No fuel leaks tolerated. Fire extinguisher accessible in cockpit.
- **Dope fumes**: Highly flammable. Apply outdoors or in well-ventilated hangar. No smoking, no sparks. Ground aircraft during doping (static electricity ignites fumes).
- **Spatial disorientation**: Without visual reference to the horizon (clouds, fog, darkness), pilots lose sense of up and within 60 seconds. Trust instruments, not sensations. If caught in cloud, maintain wings-level attitude by reference to the turn needle (or compass rate of change) and descend gently straight ahead. Do not turn without visual reference.
- **Carburetor icing**: Moist air passing through the venturi cools by expansion (adiabatic cooling). At temperatures between -5°C and +25°C with high humidity, ice can form in the carburetor throat, gradually choking the airflow until the engine stops. Indicated by a gradual RPM decrease. Preventive action: apply carburetor heat (duct warm air from around the exhaust manifold into the carburetor intake) before ice forms in suspected conditions. Carb heat causes a temporary RPM drop (less dense warm air) but prevents engine failure.
- **Weather minimums**: Fly only in visual meteorological conditions (VMC): visibility ≥1.5 km, clear of clouds, in sight of the ground. Cloud base above 300 m for safe terrain clearance. Do not launch into fog, low overcast, heavy rain, or thunderstorms. Ultralight aircraft have no de-icing capability and minimal structural margin for turbulence. A cumulonimbus (thunderstorm) can produce updrafts and downdrafts exceeding 20 m/s, far beyond the structural capability of a light airframe.
- **Fuel exhaustion**: The most preventable cause of forced landings. Calculate fuel required for each leg plus 30-minute reserve. Visually verify fuel quantity before flight (dip the tank with a calibrated stick or sight gauge). Do not rely on memory of the last refueling. A 40 HP engine at cruise consumes 8-12 kg/hour. A 20 kg fuel tank gives 1.5-2.5 hours endurance.
- **Midair collision**: See and avoid other aircraft. Scan the sky in 10° sectors, pausing at each sector for 1-2 seconds to detect traffic. Blind spots below the nose and behind the tail. Fly standard traffic patterns (left-hand circuits at 300-400 m altitude, downwind leg parallel to runway) at designated airfields to maintain predictable separation.
- **Bird strike**: Birds can shatter propellers, puncture fabric covering, or jam control surfaces. A 1 kg bird at 90 km/h relative speed delivers 312 J of kinetic energy, enough to dent sheet metal or tear fabric. Avoid flying at dawn and dusk when birds are most active near rivers and coastlines. If a bird strikes the propeller, land and inspect before continuing flight (hairline cracks in wooden propellers propagate to catastrophic failure under centrifugal load).

## Aviation Fuel Specifications

**Avgas 80/87**: The standard low-lead aviation gasoline for low-compression engines. Octane rating 80 (lean mixture) / 87 (rich mixture). Leaded with tetraethyl lead (TEL) at 0.5 mL/L to boost octane and lubricate valves. Color: red dye. Suitable for engines with compression ratios up to 7:1. Phased out in many countries but still the simplest aviation fuel to refine from petroleum.

**Aviation kerosene (Jet A / Jet A-1)**: The standard turbine fuel. Flash point 38°C minimum (safe handling). Freeze point: -40°C for Jet A, -47°C for Jet A-1 (the lower freeze point enables long-range high-altitude flight where fuel temperatures drop below -30°C). Energy density: 43.15 MJ/kg (higher than gasoline at 43.0 MJ/kg by mass, though lower by volume due to higher density). Specific gravity: 0.775-0.840 at 15°C. Distillation range: 150-300°C boiling fraction from petroleum crude.


## Limitations

- **Weather dependency**: Ultralight aircraft have no de-icing capability and minimal structural margin for turbulence. Visual flight rules only — no instrument flying capability.
- **Range and payload**: 100-300 km range with 250-400 kg gross weight. Not competitive with ground transport for heavy cargo.
- **Engine reliability**: Air-cooled piston engines require frequent maintenance (every 25-50 hours). Magneto ignition provides redundancy but carburetor icing remains a hazard.
- **Fuel supply**: Aviation requires high-octane gasoline or ethanol. Fuel quality directly affects engine reliability and safety.
- **Manufacturing precision**: Cylinder bores ±0.01 mm, crankshaft journals ±0.01 mm, valve seats gas-tight. Requires functioning machine tool capability.
- **Pilot training**: In a bootstrapping scenario, pilot training is a significant challenge. The Wright brothers taught themselves over years of glider experiments.
- **Structural fatigue**: Wood and fabric airframes have finite fatigue lives. Fabric covering degrades from UV exposure and must be replaced every 5-10 years.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Engine rough running or misfiring | Fouled spark plug, carburetor icing, or fuel contamination | Clean or replace spark plug; apply carb heat; drain and replace fuel; check fuel filter |
| Loss of climb performance | Dirty airframe (drag), low compression, or overloaded | Clean airframe surface; check cylinder compression; verify weight within limits; check density altitude |
| Excessive vibration in flight | Propeller imbalance or engine mount looseness | Dynamically balance propeller; check engine mount bolts; inspect propeller for damage |
- Fabric covering tearing or sagging | UV degradation or moisture damage to dope finish | Re-dope affected area; replace fabric section if torn; store aircraft under cover when not flying |
| Oil pressure dropping in flight | Low oil level, oil cooler blockage, or bearing wear | Land immediately; check oil level; clear oil cooler; inspect engine for metal in oil |
| Magneto drop exceeds 175 RPM during runup | Fouled plug or defective magneto | Clean or replace spark plugs; check magneto timing; verify mag switch contacts |

## See Also

- [Internal Combustion Engines](../energy/engine.md) — engine design and manufacturing
- [Roads & Bridges](roads.md) — ground transport infrastructure
- [Railways](railways.md) — rail transport alternative
- [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md) — aviation fuel production
- [Textiles](../textiles/index.md) — fabric for aircraft covering
- [Machine Tools](../machine-tools/index.md) — precision machining for engine parts
- [Light Aircraft](light-aircraft.md) — specific ultralight construction details
- [Navigation](../marine/navigation.md) — aerial and marine navigation methods

[← Back to Transport](index.md)
