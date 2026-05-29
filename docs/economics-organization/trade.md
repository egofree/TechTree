# Trade & Barter

> **Node ID**: economics-organization.trade
> **Domain**: [Economics & Organization](./index.md)
> **Dependencies**: [`transport`](../transport/index.md), [`knowledge.writing`](../knowledge/writing.md)
> **Enables**: [`economics-organization.currency`](./currency.md), [`economics-organization.supply-chain`](./supply-chain.md)
> **Timeline**: Years 1-5
> **Outputs**: goods_exchange, market_systems, trade_networks
> **Critical**: No

Trade and barter is the direct exchange of surplus goods between specialists and communities. Where [division of labor](./division-of-labor.md) creates specialists who produce more of one thing than they need, trade provides the mechanism for those specialists to obtain everything else. Without trade, each specialist (or community) must remain self-sufficient, and the productivity gains from specialization cannot be fully realized.

Barter — the direct exchange of goods for goods — is the simplest form of trade. It requires no intermediary technology beyond the goods themselves and mutual agreement on relative value. However, barter suffers from the double-coincidence problem: to trade, both parties must want what the other has, at the same time, in agreeable quantities. This constraint limits barter to small communities with dense social networks where repeated interactions build trust and informal credit.

Trade depends on [transport](../transport/index.md) to move goods between locations and on [writing](../knowledge/writing.md) for contracts, inventories, and price records. The transport network defines the geographic reach of the market; writing defines the complexity of trade relationships that can be managed.


## Prerequisites

## Materials

- **Surplus goods**: At least one party must have goods beyond their own consumption needs. Minimum viable trade surplus: 10-20% of production above personal/family needs.

## Tools and Equipment

- [Transport infrastructure](../transport/index.md): Paths, roads, waterways, or pack animals. Trade range scales with transport capacity: foot paths (5-15 km), pack animals (30-80 km), water transport (100-500 km), carts on roads (50-200 km).
- [Writing systems](../knowledge/writing.md): Trade agreements, debt records, inventory lists, price documentation.

## Knowledge

- **Relative valuation**: The ability to compare the value of dissimilar goods (how many pots equal one knife?).
- **Route knowledge**: Awareness of which communities produce which goods, and where to find them.
- **Negotiation**: The social skill of reaching mutually acceptable exchange terms.

## Infrastructure

- Market spaces: Physical locations where traders meet. Can be informal (crossroads gathering) or formal (dedicated market square).
- Storage at trade points: Warehouses or secure areas for goods awaiting exchange.


## Bill of Materials (BOM)

Trade is an organizational capability. Physical inputs are minimal:

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Transport capacity (pack animal) | 1 donkey/ox per 80-120 kg cargo | [Animals](../animals/index.md) | Human porters (20-30 kg per person), carts (200-500 kg) |
| Writing surfaces for records | 10-50 clay tablets or 5-20 papyrus sheets per trading season | [Writing](../knowledge/writing.md) | Tally sticks, knotted cords, memory (limit: ~30 transactions) |
| Storage at market | 10-50 m³ covered storage per market day | [Construction](../construction/index.md) | Open-air stacking (weather risk) |
| Market space | 100-500 m² flat ground | Natural terrain | Dedicated market building (for permanent markets) |


## Process Description

## Establishing a Barter System

1. **Survey local surpluses and deficits**: Catalog what each specialist or community produces in surplus and what they need. A copper-producing village has surplus metal but needs grain; an agricultural village has surplus grain but needs tools.

2. **Establish relative values**: Create an informal exchange rate table. Start with a common reference good — grain is typical because everyone needs it. Examples: 1 iron knife = 10 kg grain; 1 copper pot = 25 kg grain; 1 woven cloak = 15 kg grain.

3. **Designate market times and locations**: Regular market days (weekly, biweekly, or monthly) at accessible locations — crossroads, river confluences, or central community spaces. Predictable timing enables specialists to plan production around market cycles.

4. **Conduct initial trades**: Begin with simple bilateral exchanges: potter trades 5 pots for 2 knives from the blacksmith. Record each trade in writing if possible, or use tally sticks for tracking.

5. **Introduce informal credit**: When double-coincidence fails (A wants B's pots but B doesn't need A's grain right now), record the debt. "Owed: 5 pots to household of A, to be delivered at next market day." This requires trust and written records.

**Decision criteria**: Start with direct barter when trading 2-5 goods among <10 parties. Introduce grain-reference pricing when goods exceed 10 types — all goods valued in grain equivalents reduces the N×(N-1)/2 pairwise valuation problem to N valuations. Introduce credit only when parties have established trust through repeated successful trades.

**Strengths**:
- Regular market days create predictable trading opportunities — specialists can plan production around market cycles
- Grain-reference pricing solves the valuation problem without currency — common denominator everyone understands
- Credit enables trade even when double-coincidence fails — extends trade volume beyond immediate exchanges

**Weaknesses**:
- Direct barter requires double-coincidence — many potential trades fail because parties don't simultaneously want each other's goods
- Grain-reference pricing depends on stable grain supply — crop failure destabilizes the entire price system
- Credit requires trust and enforcement — defaults destroy the credit system if not addressed

## Scaling to Multi-Party Trade

6. **Identify trade intermediaries**: Some individuals naturally facilitate exchange — they know who has what and who needs what. Encourage these individuals to act as brokers. Brokers take a small commission (5-10% of trade value) in goods.

7. **Establish trade routes**: When multiple communities trade regularly, standard routes emerge. Mark routes with waypoints, estimate travel times, and document hazards (bandits, river crossings, difficult terrain).

8. **Create periodic fairs**: Large-scale markets held seasonally (harvest fairs, solstice markets) that draw traders from 50-200 km radius. These fairs enable exchange of goods not available locally and establish inter-regional price convergence.

**Strengths**:
- Brokers reduce search costs — they know who has what and who needs what, matching buyers and sellers faster
- Trade routes create infrastructure benefitting all users — roads, way-stations, and river landings serve civilian and military traffic
- Seasonal fairs enable exchange of goods not locally available — inter-regional trade accesses resources beyond local reach

**Weaknesses**:
- Brokers charge commission (5-10%) — adds cost to every traded good
- Trade routes are vulnerable to banditry and conflict — armed escort increases transport cost
- Fairs are seasonal — goods needed between fairs must be stockpiled, increasing storage costs

## Trade Record-Keeping

9. **Standardize measures**: Use agreed-upon volume and weight units for trade. A "bushel" of grain, a "talent" of copper, a "cubit" of cloth. These standards reduce disputes. Link to [precision metrology](../measurement/precision-metrology.md) for standardized weights.

10. **Record all transactions**: Date, parties, goods exchanged, quantities, and any outstanding debts. Written records protect against memory disputes and enable credit-based trade.

**Strengths**:
- Standardized measures reduce disputes — agreed-upon units prevent arguments over quantity
- Written transaction records enable credit — debts can be tracked and enforced across market days
- Price documentation reveals trends — merchants can adjust production based on price signals

**Weaknesses**:
- Measure standardization requires [metrology](../measurement/precision-metrology.md) infrastructure — weights must be calibrated and maintained
- Record-keeping requires literacy — limits this approach to communities with scribes or widespread basic literacy
- Records are only as honest as the record-keeper — fraudulent entries undermine trust in the system

## Trade System Trade-offs

| System | Range | Goods Traded | Currency Required | Trust Required | Best For |
|--------|-------|-------------|-------------------|----------------|----------|
| Direct barter | 0-5 km | 2-5 types | No | Low (face-to-face) | Initial village exchange |
| Commodity-reference | 5-30 km | 5-20 types | No (grain reference) | Moderate | Inter-village trade |
| Broker-mediated | 30-200 km | 20-100 types | No | High (broker trust) | Regional trade with intermediaries |
| Currency-based | Unlimited | Unlimited | Yes | Moderate (coin trust) | Complex economies — see [currency](./currency.md) |
| Fair-based | 50-200 km draw | 100+ types | Optional | High (fair reputation) | Seasonal large-scale exchange |


## Quantitative Parameters

## Trade Route Parameters

| Route Type | Range (one-way) | Speed | Cargo Capacity | Cost per tonne-km |
|------------|-----------------|-------|----------------|-------------------|
| Human porter | 15-25 km/day | 3-4 km/h | 20-30 kg | High (labor-intensive) |
| Pack donkey | 20-30 km/day | 4-5 km/h | 80-120 kg | Moderate |
| Pack mule | 25-35 km/day | 4-6 km/h | 120-200 kg | Moderate |
| Ox cart (unpaved road) | 15-20 km/day | 3-4 km/h | 500-1,000 kg | Low |
| River transport (downstream) | 30-50 km/day | 3-5 km/h | 5-50 tonnes | Very low |
| River transport (upstream) | 15-25 km/day | 1-3 km/h (poling/towing) | 2-20 tonnes | Low |
| Sea coastal | 50-100 km/day | 5-8 km/h (sailing) | 10-100 tonnes | Very low |

## Market Frequency by Population

| Community Size | Market Frequency | Typical Traders per Market | Goods Categories |
|----------------|-----------------|---------------------------|------------------|
| 50-200 | Monthly or seasonal | 5-15 | 3-8 |
| 200-1,000 | Biweekly | 15-50 | 8-15 |
| 1,000-5,000 | Weekly | 50-200 | 15-30 |
| 5,000-50,000 | Daily (permanent market) | 200-2,000 | 30-100+ |

## Barter Exchange Ratios (Representative)

| Good A | Quantity | Good B | Quantity | Notes |
|--------|----------|--------|----------|-------|
| Iron knife | 1 | Grain | 8-12 kg | Basic tool, high demand |
| Copper pot (10 L) | 1 | Grain | 20-30 kg | Household essential |
| Woven wool cloak | 1 | Grain | 12-20 kg | Seasonal demand |
| Salt | 1 kg | Grain | 3-5 kg | Preservative value |
| Iron axe head | 1 | Grain | 25-40 kg | Production tool, high value |
| Leather sandals (pair) | 1 | Grain | 3-6 kg | Consumable, steady demand |


## Scaling Notes

- **Minimum viable trade**: Two specialists with complementary surpluses. The smallest trade loop has 2 parties; the smallest multilateral loop has 3 (A gives to B, B gives to C, C gives to A).
- **Transport bottleneck**: Trade volume is limited by transport capacity. A community producing 5 tonnes of surplus grain per year can only export what it can physically move. With human porters (25 kg each), this requires ~200 porter-trips per year.
- **Information bottleneck**: Traders need to know market conditions (supply, demand, prices) at their destination. Without rapid communication, price arbitrage opportunities persist for weeks. Written price lists carried by traders partially address this.
- **Trust radius**: Barter-based trade works within communities where repeated interaction creates trust (Dunbar's number: ~150 people). Beyond this, formal contracts and enforcement mechanisms are needed — see [governance](./governance.md).
- **Transition to currency**: When trade volume exceeds ~50-100 distinct goods with fluctuating relative values, maintaining a complete exchange rate matrix becomes impractical (N×(N-1)/2 pairs for N goods). Currency reduces this to N prices, each expressed in a single unit of account. See [currency](./currency.md).


## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| No trades occurring despite surplus | Double-coincidence problem; no mutual needs match | Introduce a common reference good (grain) as informal currency; expand trader network |
| Persistent disputes over exchange ratios | No agreed-upon measurement standards | Adopt standardized weights and measures; post price lists at market |
| Trade routes disrupted by bandits or conflict | No security on routes | Organize trade caravans (safety in numbers); establish [governance](./governance.md) enforcement along routes |
| Goods spoiling during transport | Transport too slow for perishable goods | Limit perishable trade to local range (<30 km); focus long-distance trade on durable goods (metal, pottery, salt, grain) |
| Credit defaults (debts not repaid) | No enforcement mechanism; debtor left community | Limit credit to known, trusted individuals; require collateral (goods held until debt repaid) |
| Market monopolies (single trader controls a good) | Geographic isolation or trade route control | Encourage competing trade routes; diversify supply sources |


## Safety

- **Travel hazards**: Trade routes expose traders to robbery, accidents, and exposure. Mitigate with armed caravans (minimum 5-10 people for routes >20 km from settlement), weather planning, and route marking.
- **Fraud and counterfeit goods**: Adulterated goods (grain mixed with sand, debased metal) undermine trust. Mitigate with quality inspection at point of trade and standardized measurement.
- **Debt slavery**: Unrepayable trade debts can lead to bondage. Establish debt limits (maximum debt = 50% of annual productive output) and seasonal debt forgiveness (e.g., at harvest).
- **Market crowd safety**: Markets with >200 people in confined spaces risk stampedes and disease transmission. Ensure adequate space (minimum 2 m² per person), ventilation, and waste disposal.


## Quality Control

- **Goods inspection**: Each good traded must meet minimum quality standards. Grain: <5% chaff, <2% foreign matter. Metal tools: functional (hold edge, no cracks). Pottery: no cracks, watertight.
- **Weight verification**: All traded goods measured against standardized weights at point of exchange. Discrepancies >5% trigger renegotiation.
- **Transaction recording**: Every trade documented with date, parties, goods, quantities. Records stored for minimum 1 year for dispute resolution.
- **Periodic market audits**: Monthly review of trade records to identify patterns of fraud, default, or market manipulation.


## Variations and Alternatives

| Trade System | Description | Scale | Complexity |
|-------------|-------------|-------|------------|
| Direct barter | Goods exchanged directly | 2-10 parties, local | Low |
| Commodity-reference barter | All goods valued against a reference (grain, cattle) | 10-100 parties, regional | Medium |
| Gift exchange | Goods given without immediate return; social obligation creates reciprocity | Small communities, kin networks | Low (but high social complexity) |
| Market brokerage | Professional intermediaries match buyers and sellers | 50-500+ parties, multi-regional | Medium-High |
| Fair-based trade | Seasonal large markets drawing distant traders | 100-10,000+ parties, inter-regional | High |
| Currency-based trade | Goods exchanged for standardized money | Unlimited | See [currency](./currency.md) |

## Bootstrap Trade Network Growth

Trade networks grow in predictable stages as production complexity increases:

| Stage | Range | Goods Traded | Participants | Organization |
|-------|-------|-------------|--------------|--------------|
| 1. Village barter | 0-5 km | Surplus food, simple tools | 2-5 households | Informal, face-to-face |
| 2. Inter-village trade | 5-30 km | Pottery, stone tools, salt, ores | 10-50 individuals | Regular market days, trusted intermediaries |
| 3. Regional trade | 30-200 km | Metals, luxury goods, timber, grain | 50-200 traders | Fixed trade routes, caravans, seasonal fairs |
| 4. Long-distance trade | 200-2,000 km | Tin, copper, obsidian, spices, silk | 200+ professional traders | Permanent trade posts, currency, written contracts |
| 5. Industrial supply chains | Unlimited | All manufactured inputs | Thousands | See [supply chain coordination](./supply-chain.md) |


## See Also

- [Division of Labor](./division-of-labor.md) — the specialization that creates the surplus goods for trade
- [Transport](../transport/index.md) — the infrastructure that moves traded goods
- [Writing](../knowledge/writing.md) — the recording system for trade agreements and debts
- [Currency](./currency.md) — the standardized exchange medium that solves barter's limitations
- [Supply Chain Coordination](./supply-chain.md) — the planned procurement that trade enables

[← Back to Economics & Organization](index.md)
