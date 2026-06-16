# Lighter-than-Air Flight

> **Node ID**: aerospace.lighter-than-air
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`textiles`](../textiles/index.md),
> [`polymers`](../polymers/index.md),
> [`energy.fuels`](../energy/fuels.md),
> [`chemistry`](../chemistry/index.md)
> **Enables**: Surveillance, weather observation, remote cargo
> **Timeline**: Years 10-30
> **Outputs**: balloons, airships, aerostats, lifting_gas_envelopes
> **Critical**: No

Lighter-than-air (LTA) flight is the oldest and lowest-threshold path to controlled aerial travel. Where heavier-than-air aviation demands powerful engines, precision airframes, and high-speed runways, buoyant flight requires only a sealed envelope and a lifting medium — heated air, helium, or hydrogen. The Montgolfier brothers demonstrated this in 1783, 120 years before the Wright brothers' powered flight, using nothing more than paper-lined fabric and a straw fire. For a bootstrapping civilization, hot-air balloons represent the simplest achievable flying machine: a textile envelope, a heat source, and basic rigging.

This capability covers three processes: [hot-air balloons](lighter-than-air.hot-air-balloons.md) (thermal lift, unpowered), [gas airships](lighter-than-air.gas-airships.md) (helium/hydrogen lift, powered and steerable), and [tethered aerostats](lighter-than-air.tethered-aerostats.md) (anchored gas platforms for surveillance and communications). Each process builds on the same physics of buoyancy but differs dramatically in envelope material, gas management, and operational complexity.

## The Physics of Buoyancy

### Archimedes' Principle Applied to Air

A body immersed in a fluid experiences an upward force equal to the weight of the fluid it displaces. For a lighter-than-air envelope, the "fluid" is the atmosphere itself. A sealed envelope filled with a gas less dense than the surrounding air experiences a net upward force:

**Lift = (ρ_air − ρ_gas) × V_envelope × g**

where ρ_air is ambient air density (approximately 1.225 kg/m³ at sea level, 15°C), ρ_gas is the density of the lifting gas inside the envelope, V_envelope is the envelope volume, and g is gravitational acceleration (9.81 m/s²).

The net useful (payload) lift is the gross lift minus the weight of the envelope itself, the gas inside it, rigging, basket, and any fixed equipment. A well-designed modern hot-air balloon achieves 20-30% payload fraction (payload weight / total lifted weight), while a helium airship achieves 30-60% depending on envelope technology and structural type.

### Density and Lift Per Cubic Meter

The practical lifting capacity depends directly on the density difference between the displaced ambient air and the gas inside the envelope:

| Lifting Medium | Gas Density (kg/m³, 15°C, 1 atm) | Density Difference vs. Air | Gross Lift (kg/m³) | Notes |
|---------------|-----------------------------------|-----------------------------|---------------------|-------|
| **Vacuum** (theoretical) | 0.000 | 1.225 | 1.225 | Requires rigid envelope stronger than atmospheric pressure — not practical |
| **Hydrogen (H₂)** | 0.084 | 1.141 | 1.141 | Highest lift of any practical gas; extremely flammable |
| **Helium (He)** | 0.169 | 1.056 | 1.056 | Inert, safe; 92% of hydrogen's lift; expensive, finite supply |
| **Hot air (100°C)** | 0.946 | 0.279 | 0.279 | Simplest to produce; low lift per volume |
| **Hot air (120°C)** | 0.898 | 0.327 | 0.327 | Typical max for nylon/polyester envelopes; degrades fabric over time |

Hot air at 100°C provides only about 25% of helium's lift per cubic meter, meaning a hot-air balloon needs roughly four times the envelope volume to carry the same payload as a helium balloon. Hydrogen offers 8% more lift than helium — meaningful for large airships where every kilogram of additional lift translates to payload revenue, but offset by its catastrophic flammability risk.

### Temperature, Pressure, and the Ideal Gas Law

The density of a gas follows from the ideal gas law: ρ = P / (R_specific × T). For a fixed-pressure envelope open to the atmosphere (as in a hot-air balloon or non-rigid airship), density is inversely proportional to absolute temperature. Heating the internal air from 15°C (288 K) to 100°C (373 K) reduces its density by a factor of 288/373 = 0.77, yielding the density difference tabulated above.

At constant temperature, density is directly proportional to pressure, so lift decreases with altitude as ambient pressure drops. The interplay of temperature, pressure, and volume governs all LTA flight dynamics — from balloon ascent rates to airship pressure height management.

### Altitude Effects

Air density decreases with altitude. At 3,000 m, air density drops to about 0.91 kg/m³, reducing available lift by roughly 26%. An airship designed for sea-level operation loses lift as it climbs until it reaches **pressure height** — the altitude at which the gas expansion fills the envelope completely. Beyond this altitude, gas must be vented (valved) to prevent rupture, permanently reducing lift.

For sustained high-altitude operation, a **ballonet system** compensates for expansion and contraction. Ballonets are internal air bags inside the envelope that are inflated or deflated with air by a blower to maintain constant envelope shape and pressure as the lifting gas expands (on ascent) or contracts (on descent). This allows a non-rigid airship to change altitude without venting precious helium or taking on ballast.

## Lifting Gas Comparison

### Hydrogen (H₂)

Hydrogen offers the greatest lift of any practical gas and is the cheapest to produce — electrolysis of water or steam reforming of methane yields unlimited quantities. The [chemistry](../chemistry/index.md) domain provides both pathways. The hydrogen-filled Hindenburg (1936) carried 100+ passengers and 20,000+ kg of payload across the Atlantic at 125 km/h.

The critical drawback is flammability. Hydrogen forms explosive mixtures with air across a wide range (4-75% by volume), ignites with only 0.02 mJ of energy (a static spark suffices), and burns with an almost invisible pale-blue flame at 2,045°C. The Hindenburg disaster (May 6, 1937, Lakehurst NJ) killed 36 people and ended public confidence in hydrogen airships within a single newsreel. Despite this, hydrogen remains attractive for unmanned aerostats, cargo airships, and any application where human safety is less constraining or where helium is unavailable.

Hydrogen also leaks faster than helium through many materials — counterintuitively, because H₂ molecules are heavier but more chemically active and can permeate certain polymer films faster than inert He atoms. In practice, both gases require carefully engineered barrier layers; hydrogen systems additionally require strict bonding and grounding to prevent static ignition.

### Helium (He)

Helium is inert, non-flammable, and provides 92% of hydrogen's lift — making it the standard lifting gas for modern airships, aerostats, and sport balloons. The critical drawback is supply: helium is a non-renewable resource extracted from natural gas deposits, where it accumulates from radioactive alpha-particle decay of uranium and thorium in the Earth's crust. The US Federal Helium Reserve (Amarillo, Texas) was the world's primary source for decades; global supply remains concentrated in a few natural gas fields in the US, Qatar, Algeria, and Russia.

For a bootstrapping civilization, helium production requires cryogenic air separation or natural gas processing infrastructure — a significant capability threshold. Helium's small atomic size (the smallest noble gas) means it diffuses through envelope materials faster than nearly any other gas, requiring frequent topping-off and low-permeability barrier films. Despite these costs, helium is the only practical choice for manned gas-lift platforms where fire risk is unacceptable.

### Heated Air

Hot air is the simplest lifting medium: no gas production, no storage, no supply chain, no scarcity. A propane burner heating ambient air to 100-120°C generates sufficient lift for manned balloon flight. The trade-off is low lift density (0.25-0.33 kg/m³ vs. 1.0+ for helium), requiring very large envelopes — a typical 4-person hot-air balloon uses a 2,500-3,000 m³ envelope, compared to roughly 800 m³ of helium for the same payload.

The fuel must be carried aboard, and continuous heating is required throughout flight. A standard 20 kg propane cylinder lasts roughly 30-45 minutes of active burner use, limiting endurance to a few hours. Despite these limitations, hot air's simplicity — no gas handling, no permeability concerns, no cryogenic supply chain — makes it the clear bootstrap starting point.

## Envelope Materials

### Historical Materials

Early balloons used paper-lined fabric, oiled silk, or goldbeater's skin (cattle intestine membranes laminated with gelatin). The Montgolfier brothers' first envelopes were linen lined with paper to reduce porosity. Zeppelin rigid airships used cotton fabric doped with cellulose acetate or nitrate solutions to tighten the weave and make it gas-tight. These natural and early synthetic coatings were heavy, degraded in UV light, and had significant gas permeability — early hydrogen airships lost 5-15% of their gas per month through the envelope fabric alone.

### Modern Envelope Fabrics

Contemporary hot-air balloon envelopes are woven from high-tenacity nylon (ripstop construction) or polyester, coated with polyurethane or silicone for reduced porosity and UV resistance. A typical balloon fabric weighs 60-90 g/m² and retains useful strength up to 120°C continuous exposure. **Load tapes** — nylon or polyester webbing 25-50 mm wide — run vertically from the envelope mouth to the top crown, carrying the structural load from the fabric to the suspension cables and basket. The fabric itself carries only local pressure loads, not the gross lift.

Gas airship and aerostat envelopes require far lower gas permeability — measured in liters/m²/day rather than the porous tolerance of hot-air balloons. Modern designs use:

- **Mylar (biaxially-oriented PET) films** laminated to woven substrates for helium retention
- **Polyurethane-coated nylon or polyester** for moderate-cost blimp envelopes
- **Multi-layer laminates** combining a woven scrim (for tear strength), barrier films (for gas retention), and UV-resistant outer coatings (for durability)
- **Tedlar (PVF) outer layers** for exceptional UV and weather resistance on long-duration aerostats

The [textiles](../textiles/index.md) domain provides the base woven fabrics; [polymers](../polymers/index.md) provides the coatings, films, and adhesives that transform porous cloth into gas-tight envelopes. Envelope fabrication — pattern cutting, heat sealing, seam bonding, and leak testing — is the core manufacturing skill that all three processes share.

### Envelope Seam and Joint Design

Envelope integrity depends on seam quality as much as on the base fabric. In hot-air balloons, panels are joined by folded and sewn seams (lap-felled or double-lapped), with load tapes capturing the seam allowances. In gas envelopes, seams must be both gas-tight and structurally sound — typically achieved by heat welding or radio-frequency (RF) welding of thermoplastic-coated fabrics. A single defective seam can leak enough gas to ground an airship within days.

Leak testing uses pressure decay methods (pressurize the envelope, isolate, and measure the rate of pressure drop) or helium mass spectrometry (for trace gas detection at seam lines). Quality control in envelope manufacture directly determines operational endurance and gas replenishment costs.

## Gas Management Systems

### Ballast and Trim Control

Gas airships and large balloons use **ballast** — disposable weight (typically water or lead shot) — to compensate for gas loss and payload changes. When an airship loses helium through permeation or valve operations, it becomes lighter and ascends; the crew releases ballast to restore neutral buoyancy. When the airship must descend without venting gas, the crew releases gas through valves. This creates a fundamental operational constraint: every cycle of ascent and descent consumes both gas (a scarce resource) and ballast (limited supply). Historical rigid airships carried 10-20% of their gross lift as ballast.

### Valving and Pressure Relief

All gas-lift envelopes must include **pressure relief valves** (automatic or manual) to prevent envelope rupture when the gas expands beyond the envelope's volume — typically during ascent or solar heating. The Hindenburg's 16 gas cells each had a manual valve operable from the control car via cables, plus automatic pressure relief valves. Modern non-rigid airships use electrically actuated valves controlled by an automatic pressure management system. Every valving event permanently reduces lift, making altitude management a critical operational discipline.

### Ballonet Operation

In non-rigid airships (blimps) and semi-rigid designs, **ballonets** — internal air chambers — replace gas venting as the primary altitude control mechanism. Two ballonets (fore and aft) are inflated or deflated with air by electric blowers:

- **On ascent**: Gas expands, air is pushed out of the ballonets through automatic valves. The envelope maintains shape with no gas lost.
- **On descent**: Gas contracts, blowers pump air into the ballonets to maintain envelope pressure and prevent collapse.

Ballonet capacity is typically 25-40% of envelope volume, defining the operating altitude range (the difference between maximum and minimum pressure height) within which the airship can operate without venting gas. Trim is controlled by transferring air between fore and aft ballonets to adjust pitch.

## Mooring and Ground Handling

### Mooring Masts

Rigid and semi-rigid airships historically used **mooring masts** — tall steel structures (20-30 m) to which the airship's bow was attached, allowing it to swing freely into the wind like a weathervane. The Empire State Building was originally designed with a dirigible mooring mast on its roof (never used operationally). Modern airship designs use mobile mooring masts mounted on trucks, allowing remote-site operations.

### Ground Crew Requirements

Ground handling of large airships is labor-intensive. The Hindenburg required a crew of 100-200 ground handlers to walk the ship out of its hangar and to catch the mooring lines on arrival. Smaller modern blimps need 10-25 ground crew. The high wind-sail area of an inflated envelope makes ground operations dangerous in winds above 20-30 km/h — a critical operational limitation that has prevented airship adoption at many airports.

### Hangar Infrastructure

Airship hangars are among the largest enclosed structures ever built. The Hangar No. 1 at NAS Lakehurst (1921) is 274 m long, 90 m wide, and 60 m high — sufficient to house two rigid airships side by side. Modern airship operations require similar hangarage for envelope maintenance, gas topping-off, and weather shelter. Hangar construction cost is a significant capital barrier, estimated at $50-100M for a structure large enough to house a modern cargo airship.

## Historical Development

### The Montgolfier Era (1783-1800)

Joseph-Michel and Jacques-Étienne Montgolfier, paper manufacturers from Annonay, France, demonstrated the first unmanned hot-air balloon on June 4, 1783, and the first manned flight on November 21, 1783, when Pilâtre de Rozier and the Marquis d'Arlandes flew 8 km across Paris in a linen-and-paper envelope. Within months, Jacques Charles flew a hydrogen-filled balloon from the same city. The science of buoyant flight was established before the French Revolution — centuries of theory (Archimedes, Boyle, Charles) converged into a working flying machine.

The early balloon era also saw the first aviation fatalities: Pilâtre de Rozier died in 1785 attempting to cross the English Channel in a hybrid hydrogen/hot-air balloon (the "Rozière" design, still used today for long-distance records, separates the two gases into different compartments to avoid continuous fuel consumption).

### The Zeppelin Era (1900-1940)

Count Ferdinand von Zeppelin developed the rigid airship — an aluminum framework containing individual gas cells — achieving the first controlled airship flight in 1900. The LZ series (Luftschiff Zeppelin) grew progressively larger:

| Airship | Year | Length | Volume | Payload | Top Speed |
|---------|------|--------|--------|---------|-----------|
| LZ 1 | 1900 | 128 m | 11,300 m³ | — | 28 km/h |
| LZ 10 Schwaben | 1911 | 140 m | 17,800 m³ | 5,000 kg | 76 km/h |
| LZ 127 Graf Zeppelin | 1928 | 236 m | 105,000 m³ | 15,000 kg | 128 km/h |
| LZ 129 Hindenburg | 1936 | 245 m | 200,000 m³ | 21,000 kg | 135 km/h |

The Graf Zeppelin circumnavigated the globe in 1929 in 21 days and operated regular scheduled transatlantic passenger service. The Hindenburg offered the pinnacle of luxury airship travel: private cabins, a dining room serving the finest cuisine, a grand piano (made of aluminum to save weight), and a pressurized smoking room. The Hindenburg fire on May 6, 1937, at Lakehurst, New Jersey, destroyed the ship in 34 seconds and effectively ended the golden age of airships.

### Blimps and Goodyear (1925-present)

Non-rigid airships — "blimps" — use the internal gas pressure to maintain envelope shape, with no internal framework. The US Navy operated hundreds of patrol blimps for anti-submarine warfare and convoy escort during World War II, with a perfect record of zero ships lost to submarines while under airship escort. The Goodyear Tire and Rubber Company operated advertising blimps continuously from 1925, making the blimp one of the most recognized aircraft shapes in popular culture. Goodyear's current fleet uses helium-filled semi-rigid designs.

### Modern Airships (2000-present)

After a half-century of near-stagnation, lighter-than-air technology is experiencing a revival driven by advances in materials, hybrid lift concepts, and demand for low-carbon aviation:

- **Hybrid Air Vehicles Airlander 10**: A hybrid airship generating 40-60% of its lift aerodynamically from its ellipsoidal hull shape (acting as a wing) and the remainder from helium. Designed for 10-ton payloads, 5-day endurance, and surveillance, cargo, and passenger roles. First flew in 2016. The hull is a composite laminate with helium barrier films.
- **Lockheed Martin P-791 / Hybrid Airship**: A hybrid design using hovercraft-style landing pads for remote-area cargo delivery without runways. Demonstrated in 2006.
- **Atlas LTA / Flying Whales**: Modern rigid airship designs targeting heavy-lift cargo to remote areas without airport infrastructure.

## Applications

### Surveillance and Reconnaissance

Aerostats and airships can loiter at altitude for days or weeks — far longer than fixed-wing aircraft or multirotor drones. Tethered aerostats carrying radar and optical payloads are used for border surveillance, maritime patrol, and battlefield monitoring. The TARS (Tethered Aerostat Radar System) program has operated aerostats along the US southern border since the 1980s, detecting low-flying aircraft at ranges exceeding 300 km. A single aerostat at 4,500 m altitude provides radar coverage equivalent to dozens of ground-based towers.

### Weather and Atmospheric Research

Balloons remain the workhorse of operational meteorology. Over 800 radiosonde-bearing weather balloons are launched twice daily from stations worldwide, measuring temperature, pressure, humidity, and wind speed from the surface to 30 km altitude. No satellite or ground-based system has replicated the in-situ vertical profiling accuracy of a balloon-borne radiosonde. High-altitude research balloons (zero-pressure designs reaching 40+ km) carry scientific instruments for cosmic ray, atmospheric chemistry, and astronomy experiments at a fraction of satellite costs.

### Advertising and Aerial Promotion

The advertising blimp — pioneered by Goodyear but now operated by multiple companies worldwide — remains a visible and effective promotional platform. Night signs (LED arrays on the envelope, controlled by computer) display animated messages visible across an entire city. The long loiter time and large visible surface area make airships uniquely suited to event coverage and brand marketing at a fraction of the cost of broadcast advertising per impression.

### Remote Cargo Delivery

Airships can deliver heavy payloads to areas without runways — mining sites, disaster zones, offshore platforms, and Arctic research stations. The ability to land vertically and hover-load cargo makes them attractive for point-to-point heavy lift where no airport infrastructure exists. This is the primary commercial case for the modern airship revival: serving routes that neither aircraft nor ground transport can reach economically. Estimated costs for hybrid cargo airships are $0.10-0.30 per ton-kilometer — competitive with helicopters (5-10× more expensive) and capable of accessing terrain where no runway can be built.

## Bootstrap Relevance

For a bootstrapping civilization, lighter-than-air flight is the first achievable aerial capability. A hot-air balloon requires only three inputs: woven fabric (from the [textiles](../textiles/index.md) domain), a heat source (propane from [energy.fuels](../energy/fuels.md), or even an open flame), and a basket or gondola. No engine, no propeller, no precision airframe, no runway. The Montgolfier brothers built the first manned flying machine with the technology of a 1780s paper mill.

The progression is natural:

1. **Hot-air balloons** (Years 10-15) — Achievable with basic textile weaving and any combustible fuel. Provides reconnaissance, morale, and proof of the buoyancy principle. Limited to unpowered, wind-borne flight.
2. **Tethered aerostats** (Years 12-20) — Requires helium or hydrogen from the [chemistry](../chemistry/index.md) domain plus low-permeability envelope materials from [polymers](../polymers/index.md). Provides a stable elevated platform for antenna relay, observation, and weather monitoring.
3. **Gas airships** (Years 15-30) — Adds propulsion (internal combustion or electric motors), steering, and a pressure control system. The most complex LTA platform, but enables controlled point-to-point aerial transport.

The critical bottleneck for gas-lift platforms is the lifting gas supply. Helium requires sophisticated gas separation infrastructure; hydrogen is cheaper to produce but introduces fire risk. For early bootstrap, hot-air balloons avoid this problem entirely — they need no gas at all, just heat.

## Safety and Risk Management

### Fire and Explosion Risk

Hydrogen-lift airships require extraordinary fire-safety discipline. The Hindenburg employed a "water recovery" system that condensed exhaust water into ballast (to maintain weight as fuel burned) and ensured all metal framework components were bonded electrically to prevent static buildup. The outer envelope was treated with a doping solution containing aluminum powder and iron oxide — a combination later recognized as effectively thermite, contributing to the rapid spread of the fire. Modern hydrogen airship concepts emphasize double-wall envelopes with inert gas (nitrogen) between layers, strict grounding protocols, and electrically bonded structures.

Hot-air balloons carry an inherent fire risk from the open-flame propane burner. Envelope fabric is rated for 120-150°C continuous exposure; burner flames exceed 1,000°C. Burner malfunction, fuel leaks, and envelope overheating are the primary hazards. Modern balloon burners include multiple redundant fuel jets and pilot lights, and emergency shutoff valves accessible from the basket.

### Structural Failure Modes

- **Envelope rupture**: Catastrophic failure of a large panel or seam. For hot-air balloons, this causes rapid descent but the envelope remains partially inflated, allowing a survivable landing. For gas airships, a large tear can vent the lifting gas within seconds, causing uncontrolled descent.
- **Over-pressurization**: If the pressure relief valves fail or are overwhelmed, the envelope can exceed its burst pressure. Regular valve testing and redundancy are mandatory.
- **Fatigue and UV degradation**: Envelope fabric weakens over hundreds of hours of UV exposure and thermal cycling. Regular fabric strength testing (bite tests, tensile samples) determines retirement timing. A typical hot-air balloon envelope is retired after 400-600 flight hours.

### Weather Hazards

The single greatest risk to LTA operations is weather. Balloons and airships are vulnerable to:

- **Thermals and turbulence**: Convective updrafts can carry a balloon far above its intended altitude, into oxygen-depleted air or extreme cold.
- **Wind shear**: Sudden changes in wind direction or speed at different altitudes can drive an airship into terrain.
- **Thunderstorms**: Updrafts inside storm cells can exceed 20 m/s upward, far beyond any airship's descent capability. Lightning ignition is a severe hazard for hydrogen-filled envelopes.
- **Icing**: Supercooled water droplets accumulate as ice on the envelope, adding weight and reducing lift. De-icing is impractical for fabric envelopes.

## Integration Points

| Stage | Contribution |
|-------|-------------|
| [Textiles](../textiles/index.md) | Envelope fabric — woven nylon, polyester, or cotton substrate |
| [Polymers](../polymers/index.md) | Envelope coatings, barrier films, adhesives, and sealants for gas retention |
| [Fuels](../energy/fuels.md) | Propane for balloon burners; liquid fuels for airship engines |
| [Chemistry](../chemistry/index.md) | Helium extraction (air separation), hydrogen production (electrolysis or steam reforming) |
| [Aviation](aviation.md) | Shared aerodynamics, flight testing, and ground crew methodology |

## Limitations

- **Weather dependency**: All LTA aircraft are highly sensitive to wind and weather. Balloons cannot steer and rely entirely on wind direction at different altitudes. Airships cannot operate safely in high winds (>40 km/h) or thunderstorms. Ground handling in gusty conditions is hazardous — a partially inflated envelope acts as a sail with enormous wind resistance.
- **Low speed**: Even the fastest airships travel at 100-140 km/h — a fraction of jet aircraft speeds. This limits their commercial competitiveness for passenger transport on routes served by fixed-wing aircraft.
- **Large ground crew**: Historical rigid airships required 50-100 ground handlers for mooring. Modern designs with automated mooring masts reduce this but still need more ground infrastructure than fixed-wing aircraft.
- **Helium scarcity**: Global helium supply is finite and concentrated in a few geological deposits. Large-scale adoption of helium airships would face supply constraints and price volatility.
- **Hydrogen safety**: Hydrogen remains dangerous despite improved materials and operating procedures. No manned hydrogen airship has operated commercially since 1937.
- **Envelope degradation**: UV exposure, thermal cycling, ozone attack, and gas permeability limit envelope life to 5-20 years depending on material and operating conditions. Envelope replacement is the dominant lifecycle cost for gas airships.

## See Also

- [Hot-Air Balloons](lighter-than-air.hot-air-balloons.md) — thermal lift, envelope design, burner systems
- [Gas Airships](lighter-than-air.gas-airships.md) — helium/hydrogen lift, propulsion, rigid and non-rigid designs
- [Tethered Aerostats](lighter-than-air.tethered-aerostats.md) — anchored platforms for surveillance and communications
- [Aviation](aviation.md) — heavier-than-air aircraft development
- [Textiles](../textiles/index.md) — envelope fabric manufacturing
- [Polymers](../polymers/index.md) — coatings, films, and sealants

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
