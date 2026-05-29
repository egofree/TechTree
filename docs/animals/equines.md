# Equines (Horses and Donkeys)

> **Node ID**: animals.equines
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`animals.domestication`](domestication.md), [`foundations.tools-basic`](../foundations/tools-basic.md)
> **Enables**: [`animals.draft-power`](draft-power.md), [`transport`](../transport/index.md)
> **Timeline**: Years 2-30+
> **Outputs**: draft_power, transport, manure, hides
> **Critical**: Yes — primary large draft and transport animals for field work, hauling, and riding


Equines — horses (*Equus caballus*) and donkeys (*Equus africanus asinus*) — are the primary large draft and transport animals for a bootstrapping civilization. Horses provide the greatest pulling power per animal, while donkeys offer superior endurance, disease resistance, and ability to thrive on poor forage. Together they cover the full range of traction, packing, and riding needs from farm work to long-distance transport. Both species were domesticated by 3500-4000 BCE and have been central to every major agricultural and transport system since.

| Parameter | Horse (500 kg) | Donkey (200 kg) | Mule (400 kg) |
|-----------|----------------|-----------------|---------------|
| Mature weight | 350-900 kg | 180-250 kg | 350-550 kg |
| Pulling capacity (continuous) | 500-800 kg | 150-300 kg | 400-700 kg |
| Working speed | 4-5 km/h (draft) | 3-4 km/h | 4-5 km/h |
| Daily work duration | 4-6 hours | 5-8 hours | 5-7 hours |
| Feed (maintenance, dry matter) | 8-10 kg/day | 4-5 kg/day | 6-8 kg/day |
| Water (maintenance) | 30-50 L/day | 15-25 L/day | 25-40 L/day |
| Working lifespan | 15-20 years | 20-30 years | 20-30 years |
| Gestation | 335 days (320-350) | 365 days (340-390) | Sterile |
| Pasture requirement | 1.0-1.5 ha | 0.3-0.5 ha | 0.8-1.2 ha |

## Prerequisites

| Requirement | Source | Notes |
|-------------|--------|-------|
| Forage (grass hay or pasture) | [`agriculture`](../agriculture/index.md) | 1.5-2.5% body weight/day in dry matter |
| Grain supplement (oats, barley) | [`agriculture`](../agriculture/index.md) | 2-5 kg/day for working horses |
| Fencing (post-and-rail, 1.2-1.5 m) | [`foundations.tools-basic`](../foundations/tools-basic.md) | No barbed wire |
| Shelter (3-sided or stable) | [`construction`](../construction/index.md) | 15-25 m² per horse |
| Harness and collar | [`leather`](leather.md) | Full collar for heavy draft |
| Horseshoes and nails | [`metals`](../metals/index.md) | Reset every 6-8 weeks |
| Farrier tools (nippers, rasp, hammer) | [`metals`](../metals/index.md) | For shoeing and hoof trimming |

## Bill of Materials

Materials listed per 2-horse team per year.

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Grass hay | 5,500-7,300 kg | [`agriculture`](../agriculture/index.md) | Pasture substitute at 1.0-1.5 ha/horse |
| Grain (oats) | 1,500-2,500 kg | [`agriculture`](../agriculture/index.md) | Barley (rolled), corn (limited) |
| Horseshoes | 16-20 sets (32-40 shoes) | [`metals`](../metals/index.md) | Bar stock iron for forging |
| Shoe nails | 200-300 nails | [`metals`](../metals/index.md) | Mild steel, 6-8 per shoe |
| Harness leather | 1-2 sets, repairs as needed | [`leather`](leather.md) | Rope traces for light work |
| Salt | 20-30 kg loose salt | [`mining`](../mining/index.md) | Salt block, free-choice |
| Bedding (straw/shavings) | 2,000-4,000 kg | [`plants`](../plants/index.md) | For stabled horses |


## Draft Power

**Principle**: Horses convert chemical energy from forage and grain into mechanical pulling force. A single draft horse (700-900 kg) pulls 500-800 kg on level ground at 4-5 km/h for 4-6 hours. Two-horse teams double capacity. Donkeys provide less absolute power but sustain work longer on poorer feed.

**Prerequisites**: Trained draft horse or donkey (30-36 months minimum), fitted harness with collar, wagon or implement with singletree/whippletree.

**Materials**: Full collar harness, traces, breeching, lines, wagon or plow.

**Procedure**:
1. Groom horse and check for injuries or soreness from previous work.
2. Fit harness: collar first (check fit — two fingers width at throat), then hames, traces, breeching, belly band.
3. Attach traces to singletree, check equal length on both sides.
4. Hitch to implement. Check breeching position (10-15 cm below tail head).
5. Work in 50-minute sessions with 10-minute rest breaks. Water at every break.
6. After work: remove harness, groom, check for chafing or galls. Cool down by walking 10-15 minutes.
7. Feed grain supplement within 1 hour post-work. Hay available at all times.

**Expected yield**: A 700 kg draft horse plows 0.5-0.8 hectares per day (moldboard plow, 25-30 cm depth). Pulls 1,500-2,500 kg on wheels at 4-5 km/h.

**Strengths**:
- Draft horses produce 10-15 horsepower sustained — more than early steam engines
- Self-reproducing (unlike machines) — a mare produces 8-12 foals over a lifetime
- Donkeys thrive on scrub forage that starves cattle and horses — zero grain needed for maintenance
- Mules combine horse strength with donkey hardiness — preferred by experienced teamsters

**Weaknesses**:
- Feed costs 2,500-5,000 kg hay per horse per winter — significant storage requirement
- Horses cannot work at full capacity in temperatures above 30°C — heat exhaustion risk
- Shoeing required every 6-8 weeks — farrier skill takes years to develop
- Harness sores sideline animals for weeks if not caught immediately

## Breeding and Foaling

**Principle**: Mares breed seasonally (spring/summer), with 335-day gestation producing a single foal. Foals reach skeletal maturity at 4-5 years. Breeding management determines the quality and availability of future working stock.

**Prerequisites**: Healthy mare (4-15 years), stallion or access to one, foaling stall (4 × 4 m minimum), clean straw bedding.

**Materials**: Halter and lead rope, foaling kit (clean towels, iodine for navel, enema for foal), tail bandage, foal blanket for cold climates.

**Procedure**:
1. Breed mare to stallion in late spring (May-June in northern hemisphere). Observe mating.
2. Confirm pregnancy by ultrasound at 14-16 days or manual palpation at 40-45 days.
3. Vaccinate and deworm mare during pregnancy per veterinary schedule.
4. Move to foaling stall 2-4 weeks before due date. Monitor udder development and relaxation of tail head.
5. Foaling usually occurs at night. Normal delivery: 20-30 minutes from water breaking to foal delivery.
6. Treat navel with 7% iodine solution within 1 hour of birth. Ensure foal stands within 2 hours and nurses within 3 hours (colostrum is critical — foals are born without immune protection).
7. Wean at 4-6 months using gradual separation over 1-2 weeks.

**Expected yield**: One foal per mare per year (85-90% conception rate in healthy mares). Foal matured to working age at 4-5 years.

**Strengths**:
- Horses self-reproduce — each mare generates her own replacement over a working lifetime
- Foals imprint-handleable from birth — early training produces calmer adults
- Cross-breeding horses and donkeys produces mules (sterile but superior workers)

**Weaknesses**:
- 4-5 year investment before a foal reaches working age — longest maturation of any livestock
- Dystocia (difficult birth) is a life-threatening emergency — veterinary assistance often needed
- Twin pregnancies in horses rarely produce two surviving foals — manual reduction of one embryo at 14-16 days is standard practice

## Shoeing and Hoof Care

**Principle**: Equine hooves grow continuously (6-9 mm/month) and wear on hard surfaces. Domestic working equines need shoes to prevent excessive wear, cracking, and lameness. Shoes are reset every 6-8 weeks.

**Prerequisites**: Farrier tools (nippers, rasp, hoof knife, hammer, clincher, pincers), forge for hot shoeing, bar stock iron or pre-forged shoes.

**Materials**: Mild steel bar stock (20-25 mm × 6-8 mm), horseshoe nails (6-8 per shoe), forge fuel (charcoal or coal).

**Procedure**:
1. Remove old shoes with shoe pullers. Pull nails with pincers.
2. Clean hoof: pick out sole, trim overgrown wall with nippers.
3. Level and balance hoof with rasp — maintain correct angle (50-54° front, 55-58° hind for horses).
4. Heat shoe in forge, hold briefly against hoof to mark contact (hot shoeing). Or shape cold on anvil (cold shoeing).
5. Shape shoe to match trimmed hoof. Punch nail holes if forging from bar stock.
6. Nail shoe to hoof: drive nails through shoe and out through insensitive hoof wall, avoiding the quick. Bend nail ends over and clinch flat.
7. Check fit: shoe should be flush with hoof wall, no overhang, no gaps.

**Expected yield**: One shoeing session per animal every 6-8 weeks, 30-45 minutes per animal with practice.

**Strengths**:
- Hot shoeing provides the most precise fit — the burned mark shows exact contact
- Proper shoeing prevents lameness and extends working life by years
- Donkeys on soft ground may not need shoes — their hooves are harder than horses'

**Weaknesses**:
- Farrier work requires significant skill — misplaced nail into the quick causes bleeding and pain
- Shoes wear out: 2-4 sets per year per working horse, each requiring fresh bar stock
- Neglected shoeing (beyond 8 weeks) causes hoof imbalance, lameness, and long recovery

## Training

**Principle**: Equines learn through pressure-release and repetition. Training is a multi-year progression from imprint handling at birth to full work capacity at 4-5 years. Rushed training produces dangerous animals.

**Prerequisites**: Safe working area (round pen or small paddock), halter and lead rope, patience and consistent handling.

**Materials**: Halter, lead rope, longe line (10-12 m), surcingle, light saddle or harness, snaffle bit.

**Procedure**:
1. **0-6 months (foal)**: Imprint handling — touch all body parts, handle feet, introduce halter.
2. **6-18 months**: Halter breaking, leading, tying, picking up all four feet daily. Desensitize to unfamiliar objects.
3. **18-24 months**: Longeing on 10-12 m line at walk, trot, canter. 15-20 minute sessions. Introduce saddle or harness without load.
4. **24-30 months**: Introduce bit (mild snaffle). First mounting or first pulling (light drag, 10-20 kg). Short sessions, 10-15 minutes.
5. **30-36 months**: Light work — 100-200 kg pulls for 1-2 hours (draft), or light riding 30-60 minutes.
6. **4-5 years**: Full work capacity reached. Draft horses: 500-800 kg for 4-6 hours.

**Expected yield**: Fully trained working equine at 4-5 years, productive for 15-25 years.

**Strengths**:
- Imprint-trained foals remain calmer and easier to handle for life
- Donkeys trained with patience and food rewards are exceptionally reliable
- Mules learn faster than horses and retain training better

**Weaknesses**:
- 4-5 year training timeline — the longest of any livestock
- Donkeys' freeze-and-assess response ("stubbornness") frustrates force-based trainers
- Poorly trained equines are dangerous — a 500 kg frightened horse can kill


## Feed Requirements by Workload (500 kg Horse)

| Work Level | Dry Matter/day | Hay/Pasture | Grain Supplement | Water/day |
|------------|---------------|-------------|-----------------|-----------|
| Maintenance (idle) | 8-10 kg | 8-10 kg | None | 30-50 L |
| Light work (1-2 hr) | 10-12 kg | 8-10 kg | 1-2 kg oats | 40-60 L |
| Moderate work (2-4 hr) | 12-14 kg | 8-10 kg | 2-4 kg oats | 50-70 L |
| Heavy work (4-6 hr) | 14-16 kg | 8-10 kg | 4-5 kg oats | 60-80 L |

## Feed Requirements by Workload (200 kg Donkey)

| Work Level | Dry Matter/day | Forage | Grain Supplement | Water/day |
|------------|---------------|--------|-----------------|-----------|
| Maintenance | 4-5 kg | 4-5 kg poor hay | None | 15-25 L |
| Light work | 5-6 kg | 5-6 kg | 0-0.5 kg | 20-30 L |
| Heavy work | 6-8 kg | 5-6 kg | 1-2 kg | 30-45 L |

## Breeds by Use

| Breed | Weight | Use | Pulling Capacity |
|-------|--------|-----|------------------|
| Percheron | 700-900 kg | Heavy draft, road transport | 800-1,200 kg level ground |
| Shire | 800-1,100 kg | Maximum draft, logging | 2,000+ kg on wheels |
| Suffolk Punch | 700-900 kg | Farm plowing | Most efficient per kg feed |
| Arabian | 380-450 kg | Endurance riding, herding | 8-12 km/h for 50+ km |
| Standard donkey | 180-250 kg | Pack transport, light draft | 50-80 kg pack |
| Mammoth Jackstock | 400-550 kg | Mule breeding, draft | 100-150 kg pack |

## Scaling Notes

A 2-horse draft team requires 2-3 hectares of productive pasture or 5,500-7,300 kg stored hay per winter, plus 1,500-2,500 kg grain supplement per year. Two horses plow 1.0-1.6 hectares per day — sufficient for a 20-40 hectare farm with rotational use.

**Minimum viable scale**: One horse or mule provides draft power for a 10-15 hectare farm. Donkeys serve smallholdings under 5 hectares.

**Scale bottlenecks**: Feed production and storage capacity limit team size more than any other factor. Each additional draft horse requires 1.0-1.5 hectares of dedicated hay land.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Harness sores (shoulder galls) | Poorly fitted collar | Remove collar; treat sore with clean water and rest; refit collar — measure neck and match size |
| Colic (pawing, sweating, rolling) | Feed change, dehydration, sand ingestion | Walk gently; do not let horse roll violently; call vet immediately; transition feeds over 7-10 days to prevent |
| Lameness after shoeing | Nail in quick, or sole bruise | Remove offending nail; apply antiseptic; rest until sound |
| Refusal to work (donkey) | Fatigue, fear, or pain | Check for injury; rest; assess workload — donkeys stop rather than injure themselves |
| Weight loss despite adequate feed | Dental problems (sharp enamel points) | Float (rasp) teeth — check every 6-12 months; look for quidding (dropped feed) |
| Cribbing (biting wood, gulping air) | Boredom, stall confinement | Increase turnout time; provide companionship; anti-crib collar as last resort |

## Safety

**Handling**: Always alert an equine to your presence — speak calmly, approach from the side (not directly from behind). Equines have a blind spot directly behind them; startling triggers a kick reflex.

**Kick zones**: Direct rear kick reaches 2-3 m behind the animal with 1,000+ kg impact force from a 500 kg horse — lethal to humans. Mules kick with exceptional accuracy. Never stand directly behind any equine.

**Stallion management**: Stallions are aggressive and territorial, especially during spring breeding season. House separately from mares with double-fencing (1.5 m gap). Experienced handlers only. Geldings (castrated males) are safer and easier to manage.

**Barbed wire**: Never use barbed wire fencing with equines — legs catch in wire, causing severe lacerations that heal poorly. Use post-and-rail, woven wire, or high-tensile smooth wire.

**Riding**: Always wear a helmet. Concussions from falls are the most common serious riding injury.

**Colic**: The leading cause of death in domestic horses. Prevent with gradual feed transitions (7-10 days), constant clean water, regular exercise, and dental maintenance. Walking a colicking horse gently may help mild cases — never let a colicking horse roll violently (intestinal torsion is fatal without surgery).

## Quality Control

**Body condition scoring**: Use a 9-point scale (1 = emaciated, 9 = obese). Working horses should score 5-6. Ribs should be felt but not visible. Loss of condition despite adequate feed indicates dental or health problems requiring investigation.

**Hoof quality**: Healthy hoof wall is smooth, without cracks or rings. Frog is firm and rubbery. Sole is concave and clean. Schedule shoeing every 6-8 weeks without exception — overgrown hooves alter gait and cause lameness.

**Dental maintenance**: Float (rasp) teeth every 6-12 months. Signs of dental problems: dropping feed (quidding), undigested grain in manure, head-tossing while eating, weight loss. Wolf teeth (vestigial premolars in 50-70% of horses) must be removed before bitting.

## Variations and Alternatives

**Oxen alternative**: Cattle trained as draft animals (oxen) are slower than horses but pull heavier loads relative to body weight, require no grain, and have longer working lives. See [`cattle`](cattle.md).

**Mule production**: Cross a male donkey (jack) with a female horse (mare) to produce a mule. Mules are sterile but combine horse size with donkey intelligence and hardiness. Working lifespan 20-30 years. A mule is worth more than either parent in working value.

**Hot climate**: Donkeys tolerate heat and dehydration far better than horses — they can lose up to 30% body weight from dehydration and recover. Use donkeys for pack transport in arid regions.

**Cold climate**: Both species tolerate cold well with adequate forage — forage digestion generates internal heat. Provide windbreaks and ensure water is not frozen (horses drink 40% more warm water than ice-cold water in winter).

## Cross-Domain Links

- [`animals.draft-power`](draft-power.md) — hitch configurations, implements, and team management for equine draft power
- [`animals.domestication`](domestication.md) — equine domestication history and comparative livestock data
- [`transport`](../transport/index.md) — roads, vehicles, and logistics systems enabled by equine transport
- [`agriculture`](../agriculture/index.md) — plowing, cultivation, and harvesting with equine power
- [`leather`](leather.md) — equine hide processing and harness leather


[← Back to Animals](index.md)
