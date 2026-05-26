# Pre-Electric Communication

> **Node ID**: telecom.pre-electric
> **Domain**: [Telecommunications](./index.md)
> **Dependencies**: `foundations`, [`knowledge.writing`](../knowledge/writing.md)
> **Enables**: [`telecom.electric-telegraph`](electric-telegraph.md)
> **Timeline**: Years 10-25
> **Outputs**: visual_signaling, semaphore_networks, beacon_systems

## Overview

Before electrical communication, civilizations developed optical and acoustic signaling systems for transmitting information across distances. These systems range from simple signal fires visible for 5-50 km to sophisticated semaphore networks capable of relaying complex messages at 150-300 km/h across hundreds of kilometers. Every pre-electric signaling system encodes information into a physical medium (light, sound, smoke) that propagates through the environment.

**Fundamental constraint**: Pre-electric systems are line-of-sight limited. The curvature of the Earth restricts visibility from a tower of height *h* to approximately sqrt(2Rh) meters, where R is Earth's radius (6,371 km). A 10 m tower sees ~11 km; a 30 m tower sees ~20 km; a 100 m tower on a hill 200 m above surroundings sees ~60 km.

### Signal Fires and Beacons

The oldest long-distance signaling technology. A controlled fire on a hilltop or tower, visible for 5-50 km depending on height and atmospheric conditions.

**Construction**:
- **Fire platform**: Stone or earth platform, 2-3 m diameter, on hilltop or tower. Stone ring retains fuel, prevents uncontrolled spread. Minimum elevation: 50 m above surrounding terrain for 25 km visibility.
- **Fuel**: Dry wood, brush, or charcoal. A signal fire burns 10-30 minutes on 20-50 kg of fuel. Tar barrels or pitch-soaked straw produce dense smoke for daytime signaling and bright flames for night.
- **Encodings**: One fire = one pre-arranged message (e.g., "enemy sighted"). Multiple fires = different messages. Timing (interval between lighting) adds variation. Complexity limit: 4-8 distinct messages without code books.

**Range**: 5-50 km. A chain of beacon hills can relay a signal across 500+ km in under 1 hour if each station is manned and prepared. The beacon chain along the English coast in 1588 warned of the Spanish Armada's approach across 400 km in under 30 minutes.

**Limitations**: Binary (lit/unlit) with limited encoding. Weather-dependent (fog, heavy rain obscure visibility). No confirmation of receipt. Cannot transmit arbitrary text.

**Beacon chain logistics**: A line of 20 beacon stations covering 500 km requires 20 teams of 2-4 people each, stationed permanently or on alert. Fuel must be pre-positioned and kept dry. Each station needs shelter for the watch team. Manning cost: 40-80 people full-time for a single chain.

### Semaphore Lines (Chappe Telegraph)

The first practical telecommunication network. Developed by Claude Chappe in France (1792). A mechanical apparatus on tower rooftops encodes messages as the angular positions of articulated arms, visible through telescopes at the next station 10-20 km away.

**Apparatus**:
- **Regulator**: A horizontal beam (4 m long, painted black) mounted on a vertical pivot at the top of a mast. Rotates in the horizontal plane.
- **Indicators**: Two shorter beams (2 m each) hinged to the ends of the regulator. Each indicator rotates independently through 45 degree increments (0, 45, 90, 135 degrees from the regulator axis).
- **Total positions**: The regulator has 4 positions. Each indicator has 7 positions. Theoretical combinations: 2 x 7 x 7 = 98 distinct symbols. Of these, 92 were assigned to characters, numbers, and code words.
- **Control mechanism**: A winch system with pulleys and cables allows the operator to set the arm positions from the base of the tower. Transition time between positions: 30-60 seconds.

**Station construction**:
- **Tower**: Stone or timber, 10-15 m tall, on the highest ground available. Cost: 3,000-5,000 francs per station. Requires a clear line of sight to both adjacent stations.
- **Telescope**: Refracting telescope, 30-60x magnification, for reading the adjacent station's arm positions.
- **Operator**: Two operators per station (one observes incoming, one sets outgoing). Literate and trained on the code book.

**Network parameters**:
- **Station spacing**: 10-20 km (limited by telescope resolution and atmospheric clarity).
- **Transmission speed**: 1 symbol per minute (30-60 seconds to observe, decode, set arms). A 20-word message takes 15-30 minutes end-to-end across 10 stations.
- **Propagation rate**: ~200-300 km/hour for a single symbol. A message crossing 500 km (25 stations) arrives in 2-3 hours.
- **Operating hours**: Daylight only, clear weather. Typically 8-10 hours/day. Fog, heavy rain, or darkness halts all traffic.
- **Uptime**: ~60-70% of daylight hours in temperate climates.

**Code book**: The semaphore did not transmit individual letters for most traffic. Instead, it used a code book with 92 pages, each containing 92 code words. A transmission of two symbols (page number, line number) selected one of 8,464 pre-assigned phrases.

**Napoleonic network**: The Paris-to-Lille line (230 km, 15 stations) became operational in 1794. By 1850, the French network extended over 5,000 km with 500+ stations. Cost to build: ~150,000 francs per 100 km. Operating cost: ~50,000 francs/year per 100 km.

### Heliograph (Mirror Signaling)

Uses reflected sunlight to send Morse code (or similar pulse-coded signals) to a distant station. Effective range: 10-160 km depending on mirror size and atmospheric conditions.

**Construction**:
- **Mirror**: Polished metal (silvered copper or speculum metal), 10-30 cm diameter. Flat mirror for short range, slightly concave mirror (focal length 5-10 km) for long range.
- **Mounting**: Two-axis gimbal on a tripod. The operator aims the reflected sunbeam at the target station. A sighting rod or telescopic sight assists aiming.
- **Shutter**: A flat disc or flap that blocks/unblocks the reflected beam. Short exposure = dot, long exposure = dash.
- **Beam divergence**: A 15 cm mirror produces a beam ~0.5 degrees wide, illuminating a 130 m diameter spot at 15 km. At 100 km, the spot is ~870 m.

**Operating parameters**:
- **Mirror size vs. range**: 10 cm mirror: 10-30 km. 15 cm: 20-50 km. 20 cm: 30-80 km. 30 cm: 50-160 km (clear mountain air).
- **Signal rate**: 5-15 words per minute (Morse code via shutter).
- **Operating hours**: Sunlight only. Typically 6-10 hours/day. Clouds halt communication.
- **Power**: Zero electrical power required.

**Military use**: The British Army used heliographs extensively in India and Africa (1870s-1900s). In the Second Boer War (1899-1902), the British heliograph network covered 1,500+ km of signaling lines.

### Flag Signaling

**Naval flag codes**: Ships communicate via encoded flag hoists. Each flag represents a letter, number, or pre-assigned meaning. The international maritime signal code uses 40 flags (26 letters, 10 numbers, 3 substitutes, 1 answering pennant). Range: 2-8 km for visual flag reading.

**Wig-wag (terrestrial flag signaling)**:
- A single flag on a staff, waved to left or right to encode dots and dashes (Morse code).
- **Flag size**: 60 x 60 cm (infantry) to 120 x 120 cm (long-range stations).
- **Range**: 2-5 km unaided, 8-15 km with telescopes.
- **Speed**: 5-10 words per minute for a skilled signaler.

### Acoustic Signaling

**Drums**: Hollow-log or skin drums transmit coded messages 3-10 km through forested terrain. The "talking drums" of West Africa encode tonal language patterns into drum rhythms. Low-frequency drums (bass tones ~60-80 Hz) carry 5-10 km in forest. Propagation speed through relay villages: 8-15 km/h.

**Horns and trumpets**: Animal horns, conch shells, and brass trumpets carry coded signals 2-8 km. Roman army tuba (4 m straight horn, fundamental ~130 Hz) for battlefield commands. Maximum practical range: 3-5 km in open terrain.

**Bell towers**: Community alert systems. Specific bell patterns encode the alarm nature (fire, invasion, celebration). Range: 3-10 km depending on bell size and wind. The Great Tom of Lincoln (5.5 tonnes) could be heard 8 km in calm conditions.

## Bill of Materials

### Signal Fire Station

| Material | Quantity per Station | Specification | Source |
|----------|---------------------|---------------|--------|
| Stone for platform | 500-1,000 kg | Flat stones for 2-3 m diameter platform ring | [Quarrying](../mining/index.md) |
| Fuel (dry wood/brush) | 50-100 kg (pre-positioned) | Seasoned hardwood, tar barrels for smoke | [Forestry](../plants/index.md) |
| Pitch or tar | 5-10 kg | For smoke production in daytime | [Chemistry](../chemistry/index.md) |
| Shelter for watch team | 1 small hut | Windproof, 2-4 person capacity | [Construction](../construction/index.md) |

### Semaphore Station

| Material | Quantity per Station | Specification | Source |
|----------|---------------------|---------------|--------|
| Timber (tower) | 5-15 m3 | Oak or pine, 10-15 m height | [Forestry](../plants/index.md) |
| Iron hardware (bolts, brackets) | 50-100 kg | Pivot bearings, pulleys, cables | [Metals](../metals/index.md) |
| Paint (black) | 5-10 L | For regulator and indicator arms | [Chemistry](../chemistry/index.md) |
| Rope/cable (control mechanism) | 50-100 m | Hemp rope or wire cable for winch | [Textiles](../textiles/index.md) |
| Refracting telescope | 1 | 30-60x magnification, brass tube | [Glass](../glass/index.md) |
| Code book | 1 per operator | 92-page code book, updated periodically | [Writing](../knowledge/writing.md) |

### Heliograph Station

| Material | Quantity per Station | Specification | Source |
|----------|---------------------|---------------|--------|
| Mirror (polished metal) | 1 | Silvered copper or speculum metal, 10-30 cm | [Metals](../metals/index.md) |
| Tripod and gimbal mount | 1 | Iron or brass, two-axis adjustment | [Metals](../metals/index.md) |
| Shutter mechanism | 1 | Flat disc or flap, spring-loaded | [Metals](../metals/index.md) |
| Sighting rod or scope | 1 | For aiming at target station | [Glass](../glass/index.md) |

## Quantitative Parameters

### Signal Propagation Comparison

| System | Range (km) | Speed (msg/hr) | Bandwidth (distinct messages/hr) | Operating Conditions | Power Required |
|--------|-----------|----------------|--------------------------------|---------------------|----------------|
| Signal fires | 5-50 | 1-2 (binary) | 4-8 (limited encoding) | Night, clear weather | 20-50 kg wood per signal |
| Semaphore | 10-20/station | 3-5 words/min | 50-100 messages/day | Daylight, clear weather | Human (winch operation) |
| Heliograph | 10-160 | 5-15 WPM | 200-500 messages/day | Sunlight, clear weather | Solar (zero fuel) |
| Flag (wig-wag) | 2-15 | 5-10 WPM | 100-300 messages/day | Daylight, clear weather | Human (flag waving) |
| Naval flags | 2-8 | 2-4 code groups/min | 50-100 messages/day | Daylight | Human (hoisting) |
| Drums | 3-10 | 1-2 phrases/min | 30-60 messages/day | Any (limited by wind) | Human (drumming) |
| Horns | 2-8 | 1-2 calls/min | 10-20 distinct calls | Any (limited by wind) | Human (blowing) |

### Line-of-Sight Range vs. Tower Height

| Tower Height (m) | Horizon Distance (km) | With 5 m Target Height (km) | Notes |
|------------------|-----------------------|-----------------------------|-------|
| 5 | 8 | 14 | Short watchtower |
| 10 | 11 | 19 | Standard semaphore station |
| 15 | 14 | 23 | Tall semaphore station on hill |
| 30 | 20 | 28 | Major signal tower |
| 50 | 25 | 34 | Hilltop beacon with tall mast |
| 100 | 36 | 44 | Elevated fortress or hilltop tower |

### Acoustic Signal Attenuation

| Frequency (Hz) | Range in Open Terrain (km) | Range in Forest (km) | Atmospheric Absorption Rate |
|----------------|---------------------------|---------------------|---------------------------|
| 60-80 (bass drum) | 5-10 | 3-8 | Low (bass carries far) |
| 130 (horn/tuba) | 3-5 | 2-4 | Moderate |
| 500-1000 (bell) | 3-10 | 2-5 | Moderate to high |
| 2000+ (whistle) | 1-3 | 0.5-2 | High (absorbed rapidly) |

## Scaling Notes

### Local Communication (1-10 km)

Signal fires, drums, horns, and flags cover local needs. Single stations, no relay infrastructure needed. Staffing: 2-4 people for continuous watch. Cost: minimal (a few hundred francs for a permanent signal fire platform or drum). Suitable for military camp coordination, village alerts, and harbor signaling.

### Regional Network (50-200 km)

Semaphore line or heliograph chain. Requires 5-15 relay stations for semaphore, each with 2 operators, telescopes, and tower maintenance. A 100 km semaphore line needs ~8 stations, 16 operators, and costs ~50,000 francs to build. Heliograph chains are cheaper per station (20-50 francs) but require sunlight. Staffing is the dominant ongoing cost.

### Continental Network (500+ km)

Only semaphore networks achieved this scale pre-electrically. The French network reached 5,000+ km with 500+ stations. Staffing: 1,000+ operators full-time. Construction cost: ~7.5 million francs. Operating cost: ~2.5 million francs/year. Such networks were government-only investments — no commercial return justified the cost. A 500 km semaphore line transmits a message in 2-3 hours; an electrical telegraph covers the same distance in minutes. The performance gap made pre-electric networks uneconomic once telegraph lines arrived.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Semaphore arms unreadable at adjacent station | Fog, haze, or atmospheric distortion | Halt traffic until visibility improves; use larger arm indicators or additional telescopes |
| Semaphore arm mechanism jammed | Pivot bearing corrosion, cable fraying, ice accumulation | Lubricate bearings quarterly; inspect cables monthly; clear ice immediately with warm water (not direct heat on frozen metal) |
| Heliograph beam not reaching target | Mirror misaligned, atmospheric haze, wrong focal length | Re-aim using ground spot method; check mirror surface for tarnish (repolish with soft cloth and mild abrasive); switch to shorter-range mirror if haze is persistent |
| Signal fire not visible at distance | Insufficient height, fuel too wet, ambient light interference | Increase platform elevation; use dry fuel pre-stored under cover; add pitch or tar barrels for brighter flame |
| False alarm (signal fire lit accidentally) | Unattended fire, lightning strike, animal interference | Clear 10 m radius of flammable vegetation; station watch team at all times; confirm received signals with a return signal before acting |
| Drum message garbled at relay | Operator error, wind noise masking tones | Use only trained drummers at relay points; repeat message three times for confirmation; use distinctive rhythm patterns that are hard to confuse |
| Telescope damaged or clouded | Moisture ingress, lens fungus, physical shock damage | Store telescopes in sealed cases when not in use; clean lenses with soft cloth only; replace damaged optics immediately (a station without a telescope is useless) |
| Code book synchronization failure | Different editions of code book at different stations | Distribute new code books simultaneously to all stations; destroy old editions upon replacement; include edition number and date in every code book |

## Safety Considerations

- **Fire hazards**: Signal fires on hilltops risk wildfire, especially in dry seasons. Clear a 10 m radius of flammable vegetation around each beacon site. Keep sand or water for emergency extinguishing. Never leave a signal fire unattended until fully extinguished.
- **Tower falls**: Semaphore tower construction requires sound masonry or timber framing. A 15 m tower collapse kills or injures anyone on or near it. Inspect tower foundations annually. Replace rotting timber promptly.
- **Eye strain**: Semaphore operators spend hours observing distant signals through telescopes. This causes severe eye fatigue and headaches. Rotate operators every 2-3 hours. Provide shade for the telescope station.
- **Sun exposure**: Heliograph operators face the sun continuously. Eye damage from direct solar observation is a real risk. Never look directly at the sun through the aiming sight — use the projected spot method to confirm aim.
- **Cold weather operation**: Winter operation on exposed tower tops causes frostbite and hypothermia. Provide windproof shelters with heating for operators. Semaphore networks in northern climates lose 30-50% of operating days in winter to fog and snow.
- **Lightning strikes**: Semaphore towers on hilltops attract lightning. Install lightning rods (sharp copper point on the mast top, connected by copper strip to a ground rod driven 2-3 m into moist earth).
- **Structural fatigue**: Semaphore arm mechanisms cycle hundreds of times per day. Pivot bearings wear, cables fray, and wooden arms crack under wind loading. Inspect and replace pivot bearings quarterly. Replace frayed cables immediately — a snapped cable under tension whips with lethal force.
- **Heliograph aiming hazard**: A misaligned heliograph can accidentally signal other stations or blind nearby observers with reflected sunlight. Always confirm the beam direction before removing the shutter.

## Transition to Electrical Systems

Every pre-electric system has the same fundamental limitations:
1. **Line-of-sight requirement**: Visual systems cannot operate in fog, heavy rain, or darkness. Acoustic systems are masked by wind and terrain.
2. **Weather dependence**: Uptime rarely exceeds 60-70% of daylight hours.
3. **Limited bandwidth**: At most a few dozen words per minute, using trained operators at every relay point.
4. **High staffing costs**: Each relay station requires 2-4 people, permanently stationed. A 500 km semaphore line needs 25-50 stations = 50-200 full-time staff.
5. **No confirmation**: The sender cannot verify that the message was received correctly.

The electrical telegraph solved all five problems simultaneously. When telegraph lines reached a city, the semaphore and heliograph links to that city were dismantled within months.

### See Also

- [Electrical Telegraph Networks](electric-telegraph.md) — The electrical successor that overcame all pre-electric limitations
- [Writing & Record-Keeping](../knowledge/writing.md) — Encoding systems that pre-electric signaling borrows from
- [Telegraph Communication](../transport/telegraph.md) — The electrical telegraph hardware details

---
*Part of the [Bootciv Tech Tree](../index.md) • [Telecommunications](./index.md) • [All Domains](../index.md)*
