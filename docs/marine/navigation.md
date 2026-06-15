# Marine Navigation

> **Node ID**: marine.navigation
> **Domain**: [Marine & Naval Engineering](./index.md)
> **Dependencies**: [`knowledge.writing`](../knowledge/writing.md),
> [`measurement.horology`](../measurement/horology.md), `metals`
> **Enables**: None
> **Timeline**: Years 0-50+
> **Outputs**: navigation instruments, nautical charts, position fixing
> **Critical**: No — specialized maritime capability, not required for land-based civilization

Crossing open ocean beyond sight of land requires knowing your position (latitude and longitude) and your heading. Without navigation, a vessel is lost as soon as land disappears over the horizon — unable to reach a destination, unable to return home, and at the mercy of winds and currents. Latitude can be determined from the sun or pole star with simple instruments, but longitude requires an accurate clock (chronometer) or complex lunar observations. The challenge is building instruments and knowledge systems precise enough to fix position within miles across thousands of miles of featureless ocean — getting it wrong by even 1° means being 60 nautical miles off course, which in coastal waters means shipwreck.

## Prerequisites

- [Writing systems](../knowledge/writing.md) — recording observations, charts, and navigation tables
- [Metals](../metals/index.md) — iron and steel for compass needles, sextant frames, and chronometer parts
- [Glass](../glass/index.md) — lenses for sextants, telescopes, and magnifying reading instruments
- [Measurement instruments](../measurement/index.md) — precision machining for sextant arcs and chronometer movements
- [Mathematics](../mathematics/core-mathematics.md) — trigonometry, spherical geometry, and logarithm tables

Marine navigation is the science and craft of determining position and directing a vessel's course across water. The progression from coastal piloting to celestial navigation to dead reckoning tracks the development of instruments, mathematics, and timekeeping.

For operational navigation procedures (tide calculations, cargo handling, pilotage methods), see [Water Transport](../transport/shipping.md). This document covers the instruments, techniques, and engineering specifications of navigation systems.

## Coastal Piloting

The earliest and most reliable form of navigation. Operates within sight of land using visual references.

**Landmark navigation**:
- Identify headlands, lighthouses, church towers, distinctive peaks by bearing and appearance
- Estimate distance from apparent height: a 30 m tower at 5 m observer height appears at horizon distance = 2.08 × (√30 + √5) = 11.4 + 4.7 = 16.1 nautical miles (29.8 km)
- Cross-bearing fix: take compass bearings on two identified landmarks. Plot both bearing lines on the chart. Intersection is the vessel's position. Accuracy: ±0.5-1.0 nautical mile depending on angle between bearings (optimal: 60-90° intersection angle).

**Depth sounding**:
- Lead line: 2-7 kg lead weight on a marked line. Lower to seabed, read depth from marks.
- Markings: leather tabs at 2, 3, 5, 7, 10, 13, 15, 17, 20 fathoms (1 fathom = 1.83 m). Distinctive markers at each depth (leather strips, cloth, knots).
- Bottom sampling: hollow in the lead base filled with tallow (animal fat). Picks up sand, mud, shells, gravel on contact. Bottom type confirms position on chart when depth alone is ambiguous.
- Sounding accuracy: ±0.5 fathoms in calm water, ±1.0 fathomes in rough seas.

**Running fix**:
- Take a bearing on a single landmark at time T1. Note the bearing and log the distance run.
- After running a known distance, take a second bearing on the same landmark.
- Plot both bearings on the chart. The distance run between bearings, transferred along the course line, gives the position at T2.

**Pilotage**:
- Local knowledge of harbor entrances, channels, shoals, and hazards. Passed orally between pilots.
- Leading marks: two fixed objects (towers, beacons) aligned on a specific bearing mark the safe channel centerline. When the marks appear in line, the vessel is in the channel.
- Clearing bearings: bearing to a landmark that must not be exceeded to avoid a hazard. "Do not allow the lighthouse to bear more than 045° or less than 030°."

**Strengths**:
- No instruments required beyond eyes and memory
- Reliable in all weather with visible landmarks
- Foundation skill for all other navigation methods

**Weaknesses**:
- Limited to sight of land (10-30 nm typical)
- Unusable in fog, darkness, or heavy rain
- Requires local knowledge — a stranger to the coast has none

## Celestial Navigation

Using celestial bodies to determine position on the open ocean, beyond sight of land.

**Latitude by Polaris (North Star)**:
- In the northern hemisphere, Polaris altitude above the horizon equals the observer's latitude
- At the equator (0°N): Polaris sits on the horizon (0° altitude)
- At London (51.5°N): Polaris is 51.5° above the horizon
- At the North Pole (90°N): Polaris is directly overhead (90° altitude)

**Why Polaris altitude equals latitude**: Polaris sits within 0.7° of the celestial north pole, the point directly above Earth's rotational axis. As you travel south from the pole, the celestial pole drops toward the horizon at the same rate your latitude decreases. The angle between the horizon and the celestial pole equals your latitude because the horizon plane is perpendicular to the local vertical, and the angle between the local vertical and Earth's rotational axis is (90° minus latitude). Polaris appears at 90° at the north pole, 0° at the equator, and your latitude everywhere in between. The 0.7° offset of Polaris from the true pole introduces a small correction that varies through the night as Earth rotates, but for handheld instruments (±0.5-1° accuracy), this offset is negligible.

- Instrument accuracy: astrolabe ±1° (60 nautical miles), quadrant ±0.5° (30 nm), sextant ±1 arcminute (1 nm)

**Latitude by noon sun**:
- Measure the sun's altitude at local apparent noon (highest point of the sun's daily arc)
- Solar declination (angle above/below celestial equator): varies +23.45° to -23.45° through the year
- Latitude = 90° - observed altitude + declination (when sun and observer are same hemisphere)
- Requires a nautical almanac of daily declination values (tabulated by date)
- Accuracy with a good sextant: ±15 arcminutes (±15 nautical miles)

**Longitude by time difference**:
- The Earth rotates 15° per hour (360° ÷ 24 hours). Longitude difference equals time difference.
- If local noon occurs 2 hours before Greenwich noon, the observer is 30° west of Greenwich
- **Why time gives longitude**: Earth completes one full rotation (360°) in approximately 24 hours relative to the sun. This means the sun appears to move 15° across the sky each hour, or 1° every 4 minutes. Two observers at different longitudes see the sun at different heights at the same absolute moment. If you know what time it is at a reference meridian (Greenwich) and observe local noon at your position, the time difference tells you how far east or west you are. One hour of time difference equals exactly 15° of longitude. This is why the chronometer was the "key to the oceans": without a portable clock that maintained Greenwich time to within seconds over months at sea, longitude could only be estimated by dead reckoning or the complex lunar distance technique.
- Requires: a chronometer set to Greenwich time, plus a method of determining local noon
- Chronometer accuracy requirement: ±0.5 seconds/day = ±7.5 arcminutes longitude error per day of running
- A chronometer losing 2 seconds/day accumulates 1° longitude error per 12 days — must be checked against known positions

**Sextant operation**:
- Split-image optics: one half shows the celestial body, the other half shows the horizon
- Adjust the index arm until the sun's lower limb (bottom edge) appears to touch the horizon
- Read the angle from the calibrated arc (0-120° range, 1 arcminute resolution)
- Apply corrections: index error (instrument calibration), dip (observer height above water), refraction (atmospheric bending), semi-diameter (sun/moon angular size)
- Total correction typically 5-15 arcminutes depending on conditions

**Why the sextant works at sea**: The sextant uses double reflection. Light from the celestial body bounces off the index mirror (on the moving arm) to the horizon mirror (fixed), then to the eye. Because the light reflects twice, the angle between the two mirrors is exactly half the angle between the celestial body and the horizon. This is why the 60° graduated arc measures up to 120° of altitude. Double reflection also makes the sextant tolerant of small tilts: if the instrument shifts slightly, both the direct and reflected images shift by the same amount and stay aligned. This is what makes the sextant practical aboard a rolling ship, unlike the astrolabe or quadrant, which require careful leveling.

**Strengths**:
- Works anywhere on the open ocean with no land references
- Provides absolute position (latitude directly, longitude with chronometer)
- Reliable for thousands of years of recorded use

**Weaknesses**:
- Requires clear sky — clouds block celestial bodies
- Complex calculations requiring nautical almanac and tables
- Chronometer method for longitude depends on precision timepiece (not available until 18th century)
- Accuracy limited to ±1-15 nm depending on instrument

## Navigation Instruments

**Magnetic compass**:
- Magnetized iron needle (or steel wire) pivoting on a jewel bearing, or floating in liquid
- Points to magnetic north (not true north — declination varies by location, ±20° in many areas)
- Deviation: iron and steel aboard ship deflect the compass. Compensate with soft iron corrector spheres (Flinders bars) and permanent magnets placed near the compass
- Swinging the ship: measure deviation at 8-12 headings, create a deviation table for correction
- Liquid-filled compass: needle immersed in alcohol-water mixture dampens oscillation, steadier reading
- Accuracy: ±1-2° after correction for deviation and variation

**Astrolabe (ancient/medieval)**:
- Bronze disk with a rotating alidade (sighting arm) and a suspended ring for vertical alignment
- Suspend the astrolabe by the ring. Sight the sun through pinholes in the alidade. Read the altitude from the graduated rim.
- Accuracy: ±1° (limited by the small size, typically 15-30 cm diameter, and difficulty of steady suspension aboard ship)
- Better suited for land use; mariner's astrolabe is a heavier, simplified version (2-4 kg) for stability at sea

**Quadrant**:
- Quarter-circle instrument (90° arc) with a plumb line and two sighting vanes
- Sight the celestial body through the vanes. The plumb line indicates the altitude on the graduated arc.
- Accuracy: ±0.5° (better than astrolabe due to simpler geometry)
- Davis quadrant (backstaff): allows sighting the sun without looking directly at it, using shadows. Accuracy ±1-2 arcminutes. Used 16th-18th centuries.

**Sextant**:
- The standard precision instrument for celestial navigation (invented 1731)
- Two mirrors: index mirror (on the movable arm) and horizon mirror (half-silvered, fixed)
- Light from the celestial body reflects off the index mirror to the horizon mirror, superimposing the body on the visible horizon
- Graduated arc: 60° of actual arc measures up to 120° of altitude (hence "sextant" — one-sixth of a circle)
- Vernier scale reads to 1 arcminute; drum sextants read to 0.2 arcminutes
- Typical accuracy: ±0.5-1.0 arcminutes under good conditions

**Chronometer**:
- Precision timekeeper maintaining Greenwich Mean Time to ±0.5 seconds/day
- Key requirements: temperature compensation (balance wheel adjusts for thermal expansion), anti-magnetic construction, shock resistance
- Harrison's H4 (1761): 13 cm diameter, 5 seconds error on a 81-day voyage to Jamaica
- Ship typically carries 3 chronometers — majority vote if one drifts
- Check against radio time signals when available (post-1905)

### Sextant Construction

**Principle**: Measures the angle between a celestial body and the horizon using two mirrors — an index mirror (on a rotating arm) and a fixed horizon mirror (half-silvered, splits the view).

**Materials**: Brass or aluminum sheet (2 mm thick for frame), front-surface mirrors (2 pieces, 25 × 40 mm — can be made by silvering glass), polarizing filter or shade glasses (3 pieces, welder's glass #5-#10), magnifying lens (20 mm diameter, 5×) for vernier reading.

**Construction steps**:
1. Cut the frame from 2 mm brass sheet: an arc spanning 60° of a circle with 150 mm radius. Mill a groove along the arc edge for the vernier scale.
2. Engrave degree markings every 1° along the arc from -5° to +125°. Use a dividing head or template.
3. Mount the index mirror at the pivot of the rotating arm (index arm). The mirror center must be exactly at the pivot point.
4. Mount the horizon mirror at the frame, angled so the user sees both the horizon and the reflected image from the index mirror.
5. Add a vernier scale on the index arm: 60 divisions spanning 59° on the main arc, giving 1 arcminute resolution.
6. Attach shade filters in a rotating rack between the mirrors for sun observations.
7. Add a telescope or sighting tube (5-10× magnification, 20 mm objective).

**Calibration**: Set the index arm to 0°. Both mirrors should be parallel. Sight a distant object (horizon or star) — the direct and reflected images must align perfectly. If offset, adjust the horizon mirror tilt screw. Check at 30°, 60°, 90° using known angles between stars.

**Expected accuracy**: ±1-2 arcminutes with vernier reading. Sufficient for latitude to ±1-2 nautical miles.

### Simplified Chronometry: Lunars and Solar Time

Before a chronometer is available, determine longitude using:
1. **Lunar distances**: Measure the angle between the moon and a reference star (e.g., Regulus, Antares). Compare to a pre-computed lunar distance table (requires an almanac — see [Knowledge Preservation](../knowledge/writing.md)). The difference between observed and tabulated lunar distance gives Greenwich Time. Accuracy: ±15-30 arcminutes of longitude with careful observation.
2. **Jupiter's moons**: Observe the eclipse times of Jupiter's Galilean satellites. Compare to predicted eclipse times in an almanac. Requires a 30-50× telescope (see [Optical Instruments](../measurement/optical-instruments.md)). Accuracy: ±10-15 minutes of longitude.
3. **Solar noon**: On land, note the exact time of local solar noon (sun at highest point) using a shadow board or transit instrument. Compare to expected noon at a reference meridian. Each 4 seconds of error = 1 arcminute of longitude.

## Dead Reckoning

Estimating current position from a known starting point by tracking course and distance sailed.

**Log (speed measurement)**:
- Chip log: wooden quadrant (25 cm) attached to a line with knots at 14.4 m intervals
- Throw the chip overboard, allow line to pay out. Count knots passing in 28 seconds (measured by sand glass)
- 1 knot = 1 nautical mile per hour (1.852 km/h)
- Accuracy: ±0.5 knots in moderate conditions

**Course tracking**:
- Record compass heading each watch (4-hour period on naval vessels, 1-2 hours on merchant vessels)
- Correct for leeway (angular drift due to wind: 3-10° depending on vessel and wind angle)
- Correct for current (tidal streams and ocean currents from pilot charts)
- Estimated position = last known position + (course × distance) corrections

**Error accumulation**:
- Dead reckoning errors are cumulative — each estimate builds on the previous one
- Typical accuracy: 2-5% of distance run under good conditions, 5-10% in rough weather
- A 1,000 nm voyage with 5% error: position uncertainty of ±50 nm (93 km) at arrival
- Requires periodic celestial fixes to reset the estimated position

**Why errors accumulate**: Every navigation input (heading, speed, time, leeway estimate, current estimate) carries a small error. The compass reads within ±1-2°. The log measures speed within ±0.5 knots. The helmsman steers within ±5° of the ordered course. The leeway estimate is approximate. These errors are independent and random, so they combine as a random walk: total position error grows roughly as the square root of the number of individual estimates. After 24 hours of dead reckoning with fixes every 30 minutes (48 individual estimates), the cumulative error reaches 2-5% of distance run. A navigator relying solely on dead reckoning for a 3,000 nm transatlantic crossing can arrive 60-150 nm from the intended landfall, a potentially fatal error if the coast has rocks or shoals.

## Chart Making

**Coastal surveying**:
- Station a theodolite or transit at a known point on shore. Measure angles to coastal features.
- Triangulation from multiple known stations fixes the position of every visible feature.
- Depth soundings taken at regular intervals (50-200 m spacing) along survey lines.
- Plot on a chart with consistent scale (1:10,000 to 1:100,000 for coastal charts)

**Open-ocean charting**:
- Plot positions determined by celestial navigation on a mercator projection
- Mercator projection: rhumb lines (constant compass heading) appear as straight lines — essential for navigation
- At latitude φ, the meridional distance stretches by sec(φ). A degree of longitude at 60°N covers half the ground distance of a degree at the equator, but the chart shows both as equal width.
- Limitation: high-latitude distortion makes polar regions unusable on mercator charts (use polar stereographic instead)

**Notation conventions**:
- Depths in fathoms or meters (chart title specifies which)
- Rocks and wrecks marked with danger symbols
- Tidal stream arrows show direction and rate (spring/neap)
- Light characteristics: flash pattern, color, range (in nautical miles)

**Strengths**:
- Permanent record that enables consistent route planning
- Allows knowledge transfer between navigators
- Mercator projection simplifies course plotting

**Weaknesses**:
- Coastal surveying requires significant labor and time
- Charts become outdated as coastlines and depths change
- Mercator distortion increases dramatically at high latitudes
- Printing and reproduction requires [printing capability](../knowledge/printing.md)

## Navigation Accuracy Specifications

| Instrument | Measurement | Accuracy | Position Error |
|-----------|-------------|----------|----------------|
| Astrolabe | Sun/star altitude | ±1° | ±60 nm latitude |
| Quadrant | Sun/star altitude | ±0.5° | ±30 nm latitude |
| Backstaff | Sun altitude | ±1-2 arcmin | ±1-2 nm latitude |
| Sextant | Angle measurement | ±0.5-1.0 arcmin | ±0.5-1.0 nm (latitude) |
| Chronometer | Time | ±0.5 sec/day | ±7.5 arcmin longitude/day |
| Magnetic compass | Bearing | ±1-2° (corrected) | ±1-2° course error |
| Chip log | Speed | ±0.5 knots | Distance ±2-5% |

## Ship Characteristics Affecting Navigation

A vessel's physical dimensions and handling characteristics directly affect navigation planning and accuracy.

**Hull speed and distance estimation**: A vessel's hull speed limits its maximum speed regardless of engine power. Hull speed (knots) is approximately 1.34 × √(waterline_length_in_feet). A 30 m (100 ft) vessel has a hull speed around 13.4 knots. A 15 m (50 ft) vessel maxes out near 9.5 knots. Knowing the vessel's realistic cruising speed is essential for dead reckoning. Overestimating speed by even 1 knot on a 10-day passage puts the estimated position 240 nm off at arrival.

**Turning characteristics**: A vessel's turning radius depends on waterline length and rudder area. A 30 m vessel at full rudder turns in a circle roughly 3-5 ship lengths in diameter (90-150 m). At 8 knots, a full 360° turn takes 3-5 minutes. This matters for course changes in pilotage waters: the navigator must account for the distance covered while turning, not just the angle change.

**Draft and depth clearance**: A vessel's draft (depth below waterline) determines which channels and harbors it can enter at various tide states. A ship drawing 4 m needs at least 4.5 m of water (10% safety margin) at the shallowest point on the intended track. The navigator calculates tide height at the time of passage using tide tables and the rule of twelfths: tide rises 1/12 in the first hour after low water, 2/12 in the second, 3/12 in the third, then reverses for the fall.

**Wind, leeway, and hull shape**: Sailing vessels experience leeway (sideways drift from wind) of 3-10° depending on wind angle, sail configuration, and hull shape. A vessel making 6 knots through the water with 5° leeway drifts sideways at about 0.5 knots. Over 24 hours, this puts the vessel 12 nm off the intended track if uncorrected. Motor vessels with deeper draft experience much less leeway (1-3°) but are still affected by strong beam winds. The navigator corrects for leeway by steering into the wind by the estimated leeway angle.

**Magnetic effects of the hull**: A steel-hulled vessel creates significant magnetic deviation. A 50 m steel ship can produce 10-20° of deviation on an uncorrected compass. The correction process (swinging the ship) involves measuring the compass error at 8-12 equally spaced headings, then installing compensating magnets and soft iron correctors. After correction, residual deviation should stay below 2-3° on all headings. Wooden and fiberglass vessels produce negligible deviation from the hull itself.

## Safety & Hazards

- **Navigation error**: A 1° error in celestial observation produces 60 nm position error. In coastal waters, this can put the vessel on rocks. Always cross-check with depth soundings and visual bearings when available.
- **Compass failure**: Carry a spare compass. In extremis, magnetize a sewing needle by stroking with silk or through a coil of wire, float it on water on a leaf.
- **Chronometer failure**: Without accurate time, longitude cannot be determined. Use lunar distance method (measure angle between moon and a reference star, consult nautical almanac) — complex but doesn't require a chronometer. Accuracy ±20-30 nm.
- **Fog and reduced visibility**: Sound fog signals (bell, horn) at regulated intervals. Reduce speed. Post extra lookouts. Use radar if available.
- **Hypothermia and exposure**: Navigation requires prolonged time on deck or in open bridges. Watchkeepers in cold climates risk hypothermia from wind chill. A navigator taking sextant sights on a rolling deck in freezing spray loses dexterity fast. Provide waterproof clothing, gloves, and rotate watchkeepers every 2 hours in conditions below 5°C.
- **Sun observation eye damage**: Using a sextant to observe the sun without proper shade filters causes permanent retinal damage. Always verify shade filters are in place before bringing the sun into the field of view. Never look at the sun through an unfiltered telescope or sighting tube.
- **Night navigation collision risk**: Operating in shipping lanes at night without adequate lighting risks collision. Post lookouts with night-adapted vision (no white light exposure for 20-30 minutes before watch). Maintain a listening watch for engine sounds from nearby vessels.
- **Over-reliance on any single method**: When electronic aids (radio, radar) become available, navigators risk losing celestial and dead reckoning skills. Practice manual navigation regularly. Equipment failures at sea are common: batteries die, antennas break, lightning disables electronics. A navigator who cannot fix position with a sextant when the electronics fail is a danger to the vessel.
- **Chart errors and datum shifts**: Charts may contain survey errors, outdated soundings, or be referenced to a different geodetic datum than the navigator assumes. A chart datum shift of even 0.01° puts positions 0.6 nm off. Always check the chart's datum and date of last survey. Prefer recent surveys for coastal navigation.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Position fix disagrees with dead reckoning | Celestial observation error or current drift | Re-shoot sights with fresh horizon; check DR for current leeway; cross-check with depth sounding |
| Compass reading unstable | Magnetic deviation from iron cargo or nearby lightning strike | Move compass away from ferrous objects; compensate with deviation table; use spare compass |
| Chronometer gaining/losing time | Temperature variation affecting balance spring | Keep chronometer in padded box at stable temperature; apply daily rate correction |
| Unable to shoot sun (overcast) | Weather blocking celestial observations | Use dead reckoning from last known fix; reduce speed near hazards; sound depth continuously |
| Latitude fix disagrees with chart | Wrong assumed latitude in sight reduction or almanac error | Recheck arithmetic; verify almanac date and page; shoot multiple stars for cross-check |
| Chip log underestimating speed | Line tangling or sandglass inaccurate | Ensure log line runs free; calibrate sandglass against chronometer; average multiple runs |
| Sextant index error | Mirrors misaligned from handling or temperature | Check index error by observing horizon; adjust mirrors or apply correction to all readings |
| Depth sounding inconsistent with chart | Vessel not at assumed position or chart outdated | Cross-check with multiple soundings; verify chart edition date; check for known chart corrections |
| Running fix position jumps between observations | Current or tidal stream stronger than estimated | Apply current correction from tidal atlas; recheck bearings for reading error; plot current vector on chart |
| Polaris observation gives wrong latitude | Observer south of equator (Polaris below horizon) | Use southern sky methods (Sigma Octantis for south celestial pole); use noon sun latitude method instead |
| Chronometer rate changes suddenly | Mechanical shock, temperature spike, or magnetization | Check for nearby magnetic cargo; compare against radio time signal; apply new rate correction from known position fix |
| Compass deviation changes from last voyage | New ferrous cargo loaded or structural steelwork repair near compass | Re-swing the ship on 8-12 headings; update deviation table; move compass or add compensating magnets |
| Noon sun latitude disagrees with DR by more than 30 nm | Wrong declination value (wrong date in almanac) or arithmetic error | Recheck almanac date; verify declination sign (+ or -); redo sight reduction with fresh numbers; shoot multiple stars for cross-check at twilight |
| Lead line tallow comes up clean (no bottom sample) | Seabed too hard (rock) or line not reaching bottom in deep water | Use deeper lead line; switch to mechanical depth sounder if available; note "hard bottom" on chart for future reference |

## See Also

- [Water Transport](../transport/shipping.md) — navigation operational procedures, piloting, tide calculations
- [Marine Infrastructure](infrastructure.md) — ports, lighthouses, and navigation aids
- [Knowledge](../knowledge/index.md) — writing systems for charts and logs, mathematics for calculations
- [Metals](../metals/index.md) — iron and steel for compass needles and instrument components
- [Glass](../glass/index.md) — lenses and optics for sextants and telescopes
- [Measurement](../measurement/index.md) — precision instruments and calibration
- [Telecom / Radio](../telecom/radio.md) — radio navigation and time signal reception

---
*Part of the [Bootciv Tech Tree](../index.md) • [Marine & Naval Engineering](./index.md) • [All Domains](../index.md)*
