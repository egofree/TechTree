# Marine Navigation

> **Node ID**: marine.navigation
> **Domain**: [Marine & Naval Engineering](./index.md)
> **Dependencies**: [`knowledge.writing`](../knowledge/writing.md), [`metals`](../metals/index.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 0-50+
> **Outputs**: navigation instruments, nautical charts, position fixing
> **Critical**: No — specialized maritime capability, not required for land-based civilization

Marine navigation is the science and craft of determining position and directing a vessel's course across water. The progression from coastal piloting to celestial navigation to dead reckoning tracks the development of instruments, mathematics, and timekeeping.

For operational navigation procedures (tide calculations, cargo handling, pilotage methods), see [Water Transport](../transport/shipping.md). This document covers the instruments, techniques, and engineering specifications of navigation systems.

### Coastal Piloting

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

### Celestial Navigation

Using celestial bodies to determine position on the open ocean, beyond sight of land.

**Latitude by Polaris (North Star)**:
- In the northern hemisphere, Polaris altitude above the horizon equals the observer's latitude
- At the equator (0°N): Polaris sits on the horizon (0° altitude)
- At London (51.5°N): Polaris is 51.5° above the horizon
- At the North Pole (90°N): Polaris is directly overhead (90° altitude)
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
- Requires: a chronometer set to Greenwich time, plus a method of determining local noon
- Chronometer accuracy requirement: ±0.5 seconds/day = ±7.5 arcminutes longitude error per day of running
- A chronometer losing 2 seconds/day accumulates 1° longitude error per 12 days — must be checked against known positions

**Sextant operation**:
- Split-image optics: one half shows the celestial body, the other half shows the horizon
- Adjust the index arm until the sun's lower limb (bottom edge) appears to touch the horizon
- Read the angle from the calibrated arc (0-120° range, 1 arcminute resolution)
- Apply corrections: index error (instrument calibration), dip (observer height above water), refraction (atmospheric bending), semi-diameter (sun/moon angular size)
- Total correction typically 5-15 arcminutes depending on conditions

**Strengths**:
- Works anywhere on the open ocean with no land references
- Provides absolute position (latitude directly, longitude with chronometer)
- Reliable for thousands of years of recorded use

**Weaknesses**:
- Requires clear sky — clouds block celestial bodies
- Complex calculations requiring nautical almanac and tables
- Chronometer method for longitude depends on precision timepiece (not available until 18th century)
- Accuracy limited to ±1-15 nm depending on instrument

### Navigation Instruments

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

### Dead Reckoning

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

### Chart Making

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

### Navigation Accuracy Specifications

| Instrument | Measurement | Accuracy | Position Error |
|-----------|-------------|----------|----------------|
| Astrolabe | Sun/star altitude | ±1° | ±60 nm latitude |
| Quadrant | Sun/star altitude | ±0.5° | ±30 nm latitude |
| Backstaff | Sun altitude | ±1-2 arcmin | ±1-2 nm latitude |
| Sextant | Angle measurement | ±0.5-1.0 arcmin | ±0.5-1.0 nm (latitude) |
| Chronometer | Time | ±0.5 sec/day | ±7.5 arcmin longitude/day |
| Magnetic compass | Bearing | ±1-2° (corrected) | ±1-2° course error |
| Chip log | Speed | ±0.5 knots | Distance ±2-5% |

### Safety & Hazards

- **Navigation error**: A 1° error in celestial observation produces 60 nm position error. In coastal waters, this can put the vessel on rocks. Always cross-check with depth soundings and visual bearings when available.
- **Compass failure**: Carry a spare compass. In extremis, magnetize a sewing needle by stroking with silk or through a coil of wire, float it on water on a leaf.
- **Chronometer failure**: Without accurate time, longitude cannot be determined. Use lunar distance method (measure angle between moon and a reference star, consult nautical almanac) — complex but doesn't require a chronometer. Accuracy ±20-30 nm.
- **Fog and reduced visibility**: Sound fog signals (bell, horn) at regulated intervals. Reduce speed. Post extra lookouts. Use radar if available.

### See Also

- [Water Transport](../transport/shipping.md) — navigation operational procedures, piloting, tide calculations
- [Knowledge](../knowledge/index.md) — writing systems for charts and logs, mathematics for calculations
- [Metals](../metals/index.md) — iron and steel for compass needles and instrument components
- [Glass](../glass/index.md) — lenses and optics for sextants and telescopes
- [Measurement](../measurement/index.md) — precision instruments and calibration

---

*Part of the [Bootciv Tech Tree](../index.md) · [Marine & Naval](./index.md) · [All Domains](../index.md)*
