# Aircraft Development

> **Node ID**: transport.aviation
> **Domain**: [Aircraft Development](./)
> **Dependencies**: `machine-tools`, `petrochemicals`, `textiles`
> **Timeline**: Years 10-50+
> **Outputs**: aircraft, aircraft_engines, propellers, aviation_fuel

## Problem

Without propulsion technology, civilization is limited to ground and water transport. Aircraft enable rapid reconnaissance, cargo delivery over difficult terrain, and serve as a powerful morale boost for the entire project. The Wright brothers flew in 1903 with bicycle-shop tools and a custom engine. With modern ultralight plans in hand, the challenge is manufacturing capability, not invention.

## Technologies &amp; Systems

### Internal Combustion Engine for Aircraft

**Engine design** (single-cylinder or twin-cylinder, air-cooled):
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
- **Magneto** (self-contained, no battery needed — critical for aircraft reliability):
  - Rotating magnet (mounted on engine camshaft or accessory drive) induces current in primary coil. Interrupter (points — mechanical switch, opened by cam on magneto shaft) breaks primary current → rapid magnetic field collapse → high voltage (10,000-30,000V) induced in secondary coil → current jumps spark plug gap → spark ignites mixture.
  - Spark plug: Steel shell with ceramic insulator (alumina). Center electrode (nickel alloy). Ground electrode (nickel alloy). Gap: 0.5-0.8 mm. Thread: 14 mm × 1.25 mm pitch (common size).
  - **Timing**: Spark occurs 20-35° before top dead center (BTDC) — flame front needs time to propagate across combustion chamber before piston reaches TDC for maximum pressure on power stroke. Adjustable via magneto-to-engine timing. Too advanced → detonation (knock — uncontrolled combustion, can destroy engine). Too retarded → loss of power, overheating.

**Fuel**:
- **Gasoline** (ideal): From petroleum distillation (Petrochemicals), 30-200°C fraction. Octane rating important — higher octane resists detonation at higher compression ratios. Early gasoline: 40-60 octane (limit compression to ~5:1). Tetraethyl lead (Pb(C₂H₅)₄) additive raises octane (lead deposits lubricate valves — but lead is toxic. Use only if necessary for engine reliability).
- **Ethanol** (alternative): From fermentation (Petrochemicals). Octane ~100 (excellent anti-knock). Energy density ~60% of gasoline by volume → larger fuel tank needed. Hygroscopic (absorbs water). Attacks some rubber and metals. Carburetor jets must be enlarged ~30% (ethanol requires richer mixture — 9:1 stoichiometric vs. 14.7:1 for gasoline).
- **Fuel consumption**: 200-300 g/HP/hour (specific fuel consumption). 40 HP engine burns 8-12 kg/hour gasoline. For 2-hour flight: 16-24 kg fuel.

**Lubrication**: Total-loss splash system (simplest for aircraft). Oil reservoir in crankcase. Splash from crankshaft dipping in oil or oil slinger throws oil onto cylinder walls, bearings, cam. Oil eventually burns or leaks out — add oil periodically. Use castor oil (high-temperature stability, excellent lubricity, doesn't break down at engine temperatures) or mineral engine oil (SAE 30 or 40 weight).

### Airframe Construction

**Design** (tube-and-fabric ultralight):
- **Wingspan**: 8-12 m. **Wing area**: 12-20 m². **Wing loading**: 20-40 kg/m² (lower = lower stall speed, gentler handling). **Empty weight**: 150-250 kg. **Gross weight**: 250-400 kg. **Stall speed**: 35-50 km/h. **Cruise speed**: 70-120 km/h. **Range**: 100-300 km.
- **Wing**: High-wing or low-wing configuration. High-wing: better ground clearance, better downward visibility, simpler strut bracing. Low-wing: shorter landing gear, better crash protection, easier fueling. Choose based on construction preference.
- **Lift**: L = ½ρv²SCL, where ρ = air density (1.225 kg/m³ at sea level), v = airspeed, S = wing area, CL = lift coefficient (0.5-1.5 depending on angle of attack and airfoil). At 80 km/h (22.2 m/s), 15 m² wing, CL = 0.8: L = ½ × 1.225 × 22.2² × 15 × 0.8 = ~3620 N (~370 kg force). Sufficient to lift ultralight aircraft.
- **Airfoil**: Clark Y or similar flat-bottom airfoil (easy to build — flat lower surface simplifies rib construction). Thickness 12-15% of chord. CLmax ~1.5 with plain flaps.

**Structure**:
- **Fuselage**: Steel tube (seamless mild steel or 4130 chromoly, 15-25 mm diameter × 0.9-1.5 mm wall) truss framework. Cut tubes to length, fit, weld joints (oxy-acetylene or oxy-propane brazing/welding). triangulated structure — every bay is a triangle for rigidity. Engine mount: heavier steel tubes (25-35 mm) at front, bolted to engine crankcase via rubber vibration isolators.
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

### Propeller

**Design**:
- **Diameter**: 1.5-2.0 m. **Pitch**: 800-1200 mm (theoretical forward travel per revolution). **Blades**: 2. **RPM**: 2000-3000 (direct drive from engine, or reduction gear for larger prop at lower RPM).
- **Blade design**: Airfoil cross-section (Clark Y or similar). Blade angle (pitch) decreases from hub to tip — outer portions travel faster and need lower angle of attack to maintain optimal lift (thrust). Width 100-150 mm at widest point, tapering toward tip.
- **Thrust**: T = (η × P) / v, where η = propeller efficiency (0.6-0.8 for well-designed prop), P = engine power (W), v = forward speed (m/s). At 40 HP (30 kW) and 25 m/s (90 km/h): T = 0.7 × 30000 / 25 = 840 N (~86 kgf thrust). This accelerates aircraft to cruise speed and maintains flight.

**Construction**:
- **Wood**: Hardwood (birch, maple, or oak). Laminate 5-7 layers of wood (alternating grain direction — prevents warping, increases strength) with waterproof glue (casein glue or, later, epoxy). Rough-carve on bandsaw. Finish-carve with drawknife, spokeshave, and rasp. Balance statically (hang on horizontal axle — heavy side drops → remove material until balanced) and dynamically (spin and check for vibration at operating RPM).
- **Protection**: Apply multiple coats of linseed oil or varnish (waterproof, prevent moisture absorption → weight change and imbalance). Leading edge protection: brass or copper tipping strip (screws + epoxy) — protects against stone/erosion damage.
- **Finish**: Sand smooth (120 → 220 → 400 grit). Final coat of clear varnish or paint. Check balance after finishing. Mark tracking marks (chalk on each blade tip — spin and observe marks should overlap perfectly from the side).

### Fabric Covering &amp; Finishing

**Fabric**:
- Cotton or linen fabric (Textiles), tightly woven, ~100-200 g/m². Grade A aircraft cotton (Mercerized — treated with NaOH to increase strength and dye affinity) or linen. Modern alternative: Dacron (polyester — much stronger, more durable, but requires the Chemistry stage+ polymer chemistry). Cut fabric panels with 5-10 cm overlap at edges.

**Covering process**:
1. **Attach fabric**: Lay fabric over airframe. Tack edges with copper rivets or fabric nails (small nails with broad heads). Pull fabric taut (hand-tension — no wrinkles). Overlap seams by 3-5 cm. Stitch through fabric and rib caps with waxed linen thread (rib-stitching — prevents fabric from billowing in flight). Stitch spacing: 25-50 mm.
2. **Shrinking**: Dampen cotton fabric with water → tightens as it dries (natural cotton shrinks ~5%). For Dacron: heat with iron (150-200°C) → fabric shrinks ~10% → drum-tight. Creates smooth aerodynamic surface.
3. **Dope application**: Apply nitrocellulose dope (see below) in multiple thin coats. First coat (clear dope): saturates fabric, bonds to structure. Subsequent coats: build film thickness, fill weave. Aluminum-pigmented dope (silver): UV barrier — prevents sunlight from degrading fabric. Final coat: colored dope for visibility and identification. Total: 6-10 coats, ~100 g/m² dope applied.

**Nitrocellulose dope**:
- **Chemistry**: Cellulose (cotton linters or wood pulp) + nitric acid + sulfuric acid → nitrocellulose (cellulose nitrate, 10-12% nitrogen). Dissolve nitrocellulose in acetone + butyl acetate (solvent blend) + plasticizer (dibutyl phthalate — prevents dope film from becoming brittle) + aluminum pigment (for UV barrier coat).
- **Manufacture**: Soak cellulose in mixed acid (HNO₃ + H₂SO₄) at 20-30°C for 30-60 minutes. Nitration is exothermic — cool to prevent runaway. Dump into large volume of water to quench. Wash extensively (remove all acid — residual acid degrades nitrocellulose). Boil in water (stabilization — removes unstable nitrated products). Dry. Dissolve in solvent blend. This is the SAME chemistry used for smokeless powder (gunpowder) — handle with care.
- **Properties**: Dope shrinks as solvent evaporates → further tightens fabric. Forms hard, waterproof, taut skin. Nitrocellulose is flammable — apply in well-ventilated area, no ignition sources. Acetone fumes are heavier than air — explosive mixture. Fire hazard is REAL — many early aircraft were lost to hangar fires from dope fumes.
- **Alternative dope**: Cellulose acetate butyrate (CAB) dope — less flammable than nitrocellulose. Requires cellulose acetate (from cellulose + acetic anhydride + acetic acid — see Petrochemicals, Polymers).

### Flight Testing

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

## Safety Concerns

- **Engine failure in flight**: Plan glide approaches (identify emergency landing spots). Aircraft must be able to glide without engine (glide ratio 8:1 typical for ultralight — at 50 m altitude, can glide 400 m to landing).
- **Structural failure**: Do not exceed design load limits (typically +4g / -2g). Avoid steep spirals, high-speed dives, abrupt control inputs. Progressive flight envelope expansion.
- **Fire**: Fuel + hot engine + air. Firewal (steel sheet between engine and cockpit). Fuel lines routed away from exhaust. No fuel leaks tolerated. Fire extinguisher accessible in cockpit.
- **Dope fumes**: Highly flammable. Apply outdoors or in well-ventilated hangar. No smoking, no sparks. Ground aircraft during doping (static electricity ignites fumes).
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
