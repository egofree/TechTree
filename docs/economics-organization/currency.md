# Currency & Standardized Exchange

> **Node ID**: economics-organization.currency
> **Domain**: [Economics & Organization](./index.md)
> **Dependencies**: [`metals`](../metals/index.md), [`measurement.precision-metrology`](../measurement/precision-metrology.md)
> **Enables**: [`economics-organization.accounting`](./accounting.md)
> **Timeline**: Years 5-10
> **Outputs**: coinage, standardized_units_of_account, price_signals
> **Critical**: No

---

## 1. Overview

Currency is a standardized medium of exchange that solves the fundamental limitation of [barter](./trade.md): the double-coincidence problem. Instead of requiring two parties who simultaneously want each other's goods, currency introduces a universally accepted intermediary — money — that any party will accept because they know they can use it to buy what they need later.

Currency serves three functions simultaneously: medium of exchange (accepted for all transactions), unit of account (prices expressed in standard units), and store of value (holds purchasing power over time). Early commodity monies (grain, cattle, salt) served all three functions poorly — grain rots, cattle die, salt dissolves. Metal coinage, introduced once [metallurgy](../metals/index.md) provides reliable copper, silver, and gold, solves all three functions simultaneously: durable, divisible, portable, and intrinsically valuable.

The development of currency requires [metals](../metals/index.md) for producing coinage and [precision metrology](../measurement/precision-metrology.md) for standardized weights that ensure coins contain consistent metal content. Without standardized weights, coins cannot be trusted — and untrusted coinage fails as money.

---

## 2. Prerequisites

### Materials

- **Metal for coinage**: Copper, silver, or gold in workable quantities. Minimum: 50-100 kg of coinage metal to establish a viable currency system for a community of ~1,000 people.
- [Metals production](../metals/index.md): Reliable smelting and refining capability to produce metal of consistent purity.

### Tools and Equipment

- [Precision metrology](../measurement/precision-metrology.md): Standardized weight sets for verifying coin weight. Tolerance: ±1-2% of standard weight.
- Coin dies: Hardened metal or stone stamps for impressing designs on coin blanks. Each die produces 5,000-20,000 coins before wearing out.
- Balance scales: Sensitive to at least 0.1 g for weighing individual coins and detecting clipping or debasement.
- Furnace or forge: For melting and casting coin blanks (flans).

### Knowledge

- **Metallurgical purity assessment**: The ability to test metal purity (touchstone method for gold/silver, color and fracture inspection for copper).
- **Arithmetic**: Ability to calculate quantities, make change, and compute interest.
- **Diesinking**: The craft of engraving coin dies with designs that are hard to counterfeit.

### Infrastructure

- Minting facility: A secure, controlled space for coin production.
- Secure storage (vaults): Strong rooms for storing coinage reserves. Thick walls (≥0.5 m stone or 5 cm iron-reinforced wood), locked doors.

---

## 3. Bill of Materials (BOM)

### Coin Production (per 1,000 copper coins, ~5 g each)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Copper (≥95% purity) | 5.0-5.5 kg | [Copper-Bronze Production](../metals/copper-bronze.md) | Bronze alloy (Cu+Sn), silver (for higher denomination) |
| Charcoal (for melting) | 2-3 kg | [Charcoal Production](../energy/charcoal.md) | Coal, wood (less controlled heat) |
| Clay or stone molds (flan casting) | 1-2 sets | [Pottery](../ceramics/index.md) | Sand molds (less precise) |
| Coin dies (bronze or iron) | 1 pair (obverse + reverse) | [Iron-Steel Production](../metals/iron-steel.md) | Hardened stone (lower detail, faster wear) |
| Standardized weights (for calibration) | 1 set (1 g to 500 g) | [Precision Metrology](../measurement/precision-metrology.md) | Reference coins from trusted source |
| Hammer (1-3 kg) | 1 | [Basic Tools](../foundations/index.md) | Any heavy striking tool |

---

## 4. Process Description

### 4.1 Establishing the Currency Standard

1. **Select the monetary metal**: Choose based on availability and value density. Copper for small-denomination everyday coins (suitable for communities producing copper). Silver for larger denominations (requires silver mining). Gold for highest denominations (rare, high value density).

2. **Define the weight standard**: Establish a standard coin weight. Historical examples: Roman as (324 g copper initially, later reduced), Athenian drachma (4.3 g silver), Florentine florin (3.5 g gold). For a bootstrap community: 5-10 g copper coins for daily transactions.

3. **Define the denomination system**: Create 3-5 denominations spanning the range of common transactions. Example: 1 copper bit (2 g) = 1 loaf of bread; 1 copper unit (10 g) = 1 day's unskilled labor; 1 copper talent (100 g) = 1 month's skilled labor.

4. **Produce the first coin run**: Cast or cut coin blanks (flans) to the standard weight. Strike each flan between obverse and reverse dies with a hammer blow. Inspect each coin for weight (±2% tolerance) and design clarity.

### 4.2 Minting Operations

5. **Melt the metal**: Heat copper to 1,085°C (melting point) in a crucible. Skim slag and impurities from the surface. Pour into molds to create flans (coin blanks).

6. **Weigh and adjust flans**: Each flan must weigh within ±2% of the standard. Overweight flans are filed; underweight flans are remelted. This is the most time-consuming step in manual minting.

7. **Strike the coins**: Place a flan on the obverse die (fixed in an anvil or block). Position the reverse die on top. Strike with a 1-3 kg hammer in a single sharp blow. Inspect the result: full design impression, no cracks, proper weight.

8. **Weigh the finished coins**: Each struck coin is weighed against the standard. Coins outside ±2% tolerance are remelted. Target: <5% rejection rate for experienced minters.

### 4.3 Circulation Management

9. **Initial distribution**: Introduce coins by paying them to specialist workers, soldiers, or officials as wages. Accept coins back as payment for taxes, market fees, or state goods. This bootstraps circulation.

10. **Withdraw and remint debased coins**: Over time, coins in circulation lose weight through wear, clipping, and deliberate debasement. Schedule periodic recoinage: recall worn coins, remelt, and restrike at the standard weight. Charge a minting fee (seigniorage) of 2-5% to fund the operation.

---

## 5. Quantitative Parameters

### Coinage Parameters

| Parameter | Copper Coin | Silver Coin | Gold Coin |
|-----------|-------------|-------------|-----------|
| Typical weight | 3-12 g | 3-7 g | 3-8 g |
| Metal purity required | ≥95% | ≥90% (sterling: 92.5%) | ≥90% |
| Diameter | 15-30 mm | 15-25 mm | 15-25 mm |
| Flan thickness | 1-3 mm | 0.5-2 mm | 0.5-2 mm |
| Striking force | 50-200 N·m | 30-150 N·m | 30-150 N·m |
| Production rate (manual) | 100-300 coins/day per mint team | 100-300 coins/day per mint team | 100-300 coins/day per mint team |
| Die lifetime | 5,000-20,000 coins | 5,000-20,000 coins | 5,000-20,000 coins |
| Weight tolerance | ±1-2% | ±1-2% | ±1-2% |
| Wear rate (circulation) | 0.5-2% weight loss/year | 0.3-1% weight loss/year | 0.2-0.5% weight loss/year |

### Monetary Stock Estimates

| Community Size | Coinage Stock (copper equivalent) | Annual Minting Need | Denominations |
|----------------|-----------------------------------|---------------------|---------------|
| 200-500 people | 100-500 kg | 10-50 kg/year | 2-3 |
| 500-2,000 | 500-2,000 kg | 50-200 kg/year | 3-4 |
| 2,000-10,000 | 2,000-10,000 kg | 200-1,000 kg/year | 4-6 |
| 10,000-50,000 | 10,000-50,000 kg | 1,000-5,000 kg/year | 5-8 |

### Purchasing Power Reference (Copper-Based)

| Item | Price (copper coins, ~5 g each) |
|------|------|
| 1 kg grain | 1-2 coins |
| 1 loaf of bread | 1 coin |
| 1 iron knife | 10-20 coins |
| 1 copper pot (10 L) | 30-50 coins |
| 1 day unskilled labor | 2-5 coins |
| 1 day skilled labor (blacksmith) | 8-15 coins |
| 1 iron axe head | 30-60 coins |
| 1 sheep | 50-100 coins |
| 1 hectare agricultural land | 5,000-15,000 coins |

---

## 6. Scaling Notes

- **Minimum viable currency**: ~100 kg of coinage metal supports a community of 200-500 people. Below this, commodity money (grain, salt) is more practical.
- **Minting throughput**: A team of 3 (melter, flan preparer, striker) can produce 100-300 coins per day manually. This is sufficient for communities up to ~5,000 people. Larger communities need mechanized minting (screw press, water-powered trip hammer).
- **Counterfeit resistance**: The primary defense against counterfeiting is the coin design — complex, detailed imagery that requires skilled diesinking to replicate. Secondary defense: standardized weight and purity that makes substitution obvious. Tertiary: severe legal penalties.
- **Monetary velocity**: In a healthy economy, each coin circulates 3-10 times per year. If velocity drops below 2, the economy is hoarding — consider reducing coinage weight or increasing minting to stimulate circulation.
- **Transition from commodity money**: Introduce coinage alongside existing commodity money. Accept both at fixed exchange rates (e.g., 1 copper coin = 5 kg grain). Gradually phase out commodity money as coinage gains trust.

---

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Coins rejected in trade (lack of trust) | No established reputation; unfamiliar designs | Start with state/tax backing: announce taxes payable only in coin; pay official wages in coin |
| Persistent clipping (shaving metal from coin edges) | Coin edges unprotected; easy to shave undetected | Mint coins with raised rims; inscribe edge markings; switch to milled edges when technology permits |
| Counterfeit coins appearing | Design too simple; low-skilled die copies easily | Increase die complexity; use distinctive metal alloy (unique color/hardness); penalize counterfeiting severely |
| Deflation (prices falling, hoarding increases) | Insufficient money supply relative to goods | Increase minting; debase standard slightly (increase coin count per kg metal); lower taxes |
| Inflation (prices rising, coin value falling) | Excessive minting; debasement; loss of confidence | Reduce minting; restore weight standard; withdraw debased coins through recoinage |
| Gresham's Law (bad money drives out good) | Mixed-quality coins in circulation at same face value | Withdraw underweight coins; refuse to accept clipped/debased coins at face value;定期 recoinage |

---

## 8. Safety

- **Minting hazards**: Molten copper at 1,085°C causes severe burns. Silver at 962°C, gold at 1,064°C — similar burn risk. Mandatory: leather aprons, gauntlets, face shields, closed-toe boots. No loose clothing near furnaces.
- **Heavy metal exposure**: Copper, silver, and especially lead (common impurity) are toxic with chronic exposure. Mint workers must wash hands before eating; ventilation in minting areas to disperse metal fumes; rotate mint workers every 2-3 hours.
- **Security**: Mints are high-value targets for theft. Locate mint within or adjacent to a fortified structure. Minimum 2 guards during operations; sealed vault storage for finished coinage; daily accounting of metal inputs vs. coin outputs with <0.5% discrepancy tolerance.
- **Dies and tools**: Striking coins requires heavy hammer blows. Missed strikes can shatter dies, sending metal fragments at high velocity. Eye protection mandatory.

---

## 9. Quality Control

- **Weight verification**: Every coin weighed individually during production. Tolerance: ±1-2% of standard. Batch sample weight check in circulation: weigh 100 random coins, average must be within ±0.5% of standard.
- **Purity testing**: Touchstone method for gold/silver coins (streak color comparison against known-purity reference). For copper: fracture test (pure copper shows characteristic red fracture surface) or specific gravity test (8.96 g/cm³ for pure copper).
- **Die integrity**: Inspect dies every 500 strikes for cracking or wear. Replace at first sign of degradation — degraded dies produce blurry coins that erode trust.
- **Counterfeit detection**: Train merchants to check weight, ring (genuine coins have a characteristic resonant tone when struck), and design detail. Suspicious coins are weighed and compared against the standard.

---

## 10. Variations and Alternatives

| Currency Type | Description | Era of First Use | Advantages | Limitations |
|--------------|-------------|------------------|------------|-------------|
| Commodity money (grain, salt, cattle) | Intrinsic value goods used as medium | Stone-age | No minting needed; universal understanding | Perishable; bulky; non-divisible (cattle) |
| Shell money (cowrie, wampum) | Decorative shells as standardized units | Stone-age | Lightweight; durable; divisible by count | Limited supply depends on shell availability |
| Metal bullion (weighted metal) | Uncoined metal traded by weight | Copper-age | No minting infrastructure needed | Requires weighing every transaction; no standardization |
| Electrum coinage (natural Au-Ag alloy) | First coins, Lydia ~600 BCE | Bronze-age | First standardized coinage | Variable natural alloy composition |
| Copper/bronze coinage | Base metal coins for daily transactions | Bronze-age | Abundant metal; suitable for small denominations | Heavy for large values; subject to inflation |
| Silver coinage | Standard for medieval commerce | Iron-age | Good value density; durable; testable purity | Requires silver mining; hoarding tendency |
| Paper money (representative) | Paper notes backed by metal reserves | Medieval (China) | Lightweight; portable; scalable | Requires trust in issuing authority; counterfeiting risk |
| Fiat money | Currency with value by decree | Modern | Flexible supply; no metal backing needed | Requires strong governance; inflation risk |

---

## 11. References

- [Metals](../metals/index.md) — the source of coinage metal
- [Precision Metrology](../measurement/precision-metrology.md) — standardized weights for coin quality
- [Trade & Barter](./trade.md) — the exchange system that currency enhances
- [Accounting](./accounting.md) — the record-keeping system that currency enables
- [Division of Labor](./division-of-labor.md) — specialization creates the economic complexity that demands currency

---

*Part of the [Bootciv Tech Tree](../index.md) • [Economics & Organization](./index.md) • [All Domains](../index.md)*
