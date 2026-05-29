# Supply Chain Coordination

> **Node ID**: economics-organization.supply-chain
> **Domain**: [Economics & Organization](./index.md)
> **Dependencies**: [`transport`](../transport/index.md), [`knowledge.writing`](../knowledge/writing.md), [`economics-organization.accounting`](./accounting.md), [`economics-organization.trade`](./trade.md)
> **Enables**: [`defense.siege-warfare`](../defense/siege-warfare.md), [`photolithography.fab-processes`](../photolithography/fab-processes.md)
> **Timeline**: Years 10-25
> **Outputs**: procurement_planning, inventory_management, logistics_coordination
> **Critical**: Yes — semiconductor manufacturing is impossible without supply chain coordination involving hundreds of specialist inputs

---

## 1. Overview

Supply chain coordination is the planning and management of multi-step production sequences, procurement of inputs from diverse sources, and inventory management across distributed operations. It extends [trade](./trade.md) from simple bilateral exchange to planned, multi-party procurement networks; it extends [accounting](./accounting.md) from passive record-keeping to active planning and optimization.

This capability becomes essential when production involves more than 3 sequential specialist steps. A single blacksmith working alone needs no supply chain — he mines his own ore, smelts it, and forges tools. But a blast furnace operation requires coordinated inputs of iron ore, limestone flux, charcoal, firebrick, and specialized labor from at least 5 different sources, timed to arrive at the furnace in the correct sequence and quantity. Coordinating this flow is supply chain management.

At the highest end of the tech tree, semiconductor fabrication requires supply chain coordination across hundreds of specialist inputs: ultra-pure silicon, photolithographic chemicals, specialty gases, precision optics, clean-room equipment, and dozens of other materials sourced from globally distributed producers. This is why supply chain coordination is marked critical — without it, the tree's pinnacle capabilities cannot exist.

---

## 2. Prerequisites

### Materials

- **Writing/recording media**: Supply chain documentation is extensive — purchase orders, shipping manifests, inventory reports, production schedules. Estimate: 500-2,000 pages/tablets per year for a moderate operation.

### Tools and Equipment

- [Transport infrastructure](../transport/index.md): The physical means to move materials between production stages. Without transport, supply chain planning is purely theoretical.
- [Writing systems](../knowledge/writing.md): For all documentation — orders, manifests, schedules, inventory records.
- [Accounting systems](./accounting.md): Supply chain decisions require cost data. Without accounting, procurement cannot be cost-optimized.
- [Trade networks](./trade.md): Supply chains procure inputs through trade mechanisms.

### Knowledge

- **Network planning**: The ability to map multi-step production sequences, identify all input requirements, and schedule procurement and delivery.
- **Inventory theory**: Understanding buffer stock, safety stock, reorder points, and the trade-offs between inventory cost and stockout risk.
- **Logistics optimization**: Routing, scheduling, and load planning for material transport.
- **Supplier evaluation**: Assessing supplier reliability, quality, lead time, and cost.

### Infrastructure

- Warehouses at each production stage: Buffer storage to decouple sequential operations.
- Communication channels between supply chain nodes: Messengers, signal systems, or written correspondence for order transmission and status updates.

---

## 3. Bill of Materials (BOM)

Supply chain coordination is an organizational capability. The "materials" are documentation and communication:

| Material | Quantity per Year (Mid-Scale Operation) | Source | Alternatives |
|----------|----------------------------------------|--------|-------------|
| Writing media (paper/parchment) | 500-2,000 sheets | [Paper Making](../knowledge/writing.md) | Clay tablets (heavy, bulky), wax tablets (temporary) |
| Ink | 2-5 L | [Chemistry](../chemistry/index.md) | Carbon-based ink |
| Storage shelving | 10-50 m of shelf space for records | [Woodworking](../foundations/index.md) | Stone niches, stacked chests |
| Warehouse space | 50-500 m³ per production stage | [Construction](../construction/index.md) | Open-air covered storage (weather risk) |
| Messenger/communication system | 1-5 dedicated messengers or signal stations | [Transport](../transport/index.md) | Semaphore, courier relay |

---

## 4. Process Description

### 4.1 Mapping the Supply Chain

1. **Identify the end product and its bill of materials**: For each product, create a complete BOM listing all inputs, their quantities, and their sources. Example for a blast furnace producing 1 tonne iron/day:

   | Input | Quantity/Day | Source | Lead Time |
   |-------|-------------|--------|-----------|
   | Iron ore | 2.0-2.5 tonnes | Mining operation, 10 km | 1-2 days transport |
   | Charcoal | 1.5-2.0 tonnes | [Charcoal production](../energy/charcoal.md), 5 km | 2-3 days (including burn cycle) |
   | Limestone flux | 0.3-0.5 tonnes | Quarry, 8 km | 1 day transport |
   | Firebrick (replacement) | 50-100 kg | [Ceramics](../ceramics/index.md), 3 km | 5-7 days (production + delivery) |
   | Skilled labor | 10-15 workers | Village, 2 km | Continuous |

2. **Map the dependency graph**: Draw the complete sequence from raw material extraction to finished product. Identify critical path inputs (those with the longest lead times or most fragile supply). Mark single points of failure (inputs with only one source).

3. **Calculate buffer stock requirements**: For each input, determine the safety stock needed to absorb supply variability. Formula:

    Safety stock = (Maximum lead time − Average lead time) × Daily consumption rate × Safety factor (1.5-2.0)

    Example: If charcoal lead time varies from 2-5 days and daily consumption is 1.75 tonnes, safety stock = (5-2) × 1.75 × 1.5 = 7.9 tonnes of charcoal buffer.

**Decision criteria**: Map the supply chain when production involves >3 sequential specialist steps or >5 distinct input materials. For simpler operations (single-step, <3 inputs), informal coordination suffices. Identify single points of failure — any input with only one source must have a contingency plan (alternative source, strategic stockpile, or substitute material).

**Strengths**:
- Visual mapping reveals hidden dependencies — the dependency graph shows critical path inputs
- Safety stock calculation is quantitative — buffer sizes based on measured lead-time variability, not guesswork
- Single-point-of-failure identification enables proactive risk mitigation before disruption occurs

**Weaknesses**:
- Dependency mapping requires detailed knowledge of every input — missing inputs create blind spots
- Safety stock formula assumes stable lead-time distribution — new suppliers or routes invalidate historical data
- Map maintenance is ongoing — supply chains change as suppliers and routes evolve; outdated maps are misleading

### 4.2 Procurement Planning

4. **Establish reorder points**: For each input, define the inventory level that triggers a new procurement order.

   Reorder point = Average lead time × Daily consumption rate + Safety stock

5. **Create purchase orders**: Written orders specifying material, quantity, quality standard, delivery date, and agreed price. Send to supplier via messenger or next trade caravan.

6. **Track order status**: Maintain an order tracking log: order placed date, expected delivery date, actual delivery date, quantity received, quality on arrival. Identify late deliveries immediately.

**Strengths**:
- Reorder points automate procurement decisions — no need for daily judgment on when to order
- Purchase orders create enforceable agreements — quantity, quality, and price documented before delivery
- Order tracking enables supplier performance measurement — identifies unreliable suppliers for replacement

**Weaknesses**:
- Reorder points assume constant consumption — demand spikes cause stockouts despite safety stock
- Purchase order lead time — written orders sent by messenger add 1-3 days to procurement cycle
- Tracking requires discipline — missed log entries create gaps in delivery history

### 4.3 Inventory Management

7. **Implement first-in-first-out (FIFO)**: Use oldest stock first to prevent spoilage and degradation. Physically organize storage so that incoming stock is placed behind existing stock.

8. **Conduct cycle counts**: Count a portion of inventory daily (rotating through all categories over 1-2 weeks) rather than doing a complete count. This spreads the counting workload and detects problems early.

9. **Report discrepancies immediately**: Any discrepancy between physical count and ledger value >2% triggers an investigation: recount, check receiving records, check issuing records, inspect for theft or spoilage.

**Strengths**:
- FIFO prevents spoilage — oldest stock used first, reducing waste from expiration
- Cycle counting spreads workload — continuous verification instead of disruptive full inventory counts
- Early discrepancy detection enables rapid investigation — theft or spoilage caught before compounding

**Weaknesses**:
- FIFO requires organized storage — incoming stock must be placed behind existing; disorganized warehouses defeat the system
- Cycle counting assumes accurate records — if base records are wrong, cycle counts perpetuate errors
- 2% threshold may miss slow, small-scale theft — pilferage below the threshold accumulates over time

### 4.4 Logistics Coordination

10. **Schedule transport**: Coordinate material movements to minimize empty return trips and maximize load factors. Target: >70% load factor on all transport movements.

11. **Stage materials for production**: Deliver inputs to the production point in the sequence they are needed, not all at once. This reduces the staging area required and ensures fresh materials.

**Strengths**:
- Transport scheduling reduces empty return trips — >70% load factor cuts transport costs
- Staged delivery matches material flow to production sequence — reduces staging area requirements
- Coordinated scheduling prevents production idle time from material stockouts

**Weaknesses**:
- Requires reliable transport — delayed delivery disrupts the entire production schedule
- Staging depends on accurate production forecasting — wrong sequence creates bottlenecks
- Coordination overhead increases with number of supply chain nodes — complexity grows non-linearly

### Supply Chain Model Trade-offs

| Model | Flexibility | Reliability | Cost | Inventory Required | Best For |
|-------|:-:|:-:|:-:|:-:|----------|
| Direct procurement | High | Low (single source) | Low | None (buy as needed) | Small-scale, local operations |
| Market-based | High | Moderate | Moderate | Low | Active markets with many suppliers |
| Contract-based | Low | High (guaranteed supply) | Moderate | Moderate | Predictable, high-volume demand |
| Vertical integration | Very Low | Very High (self-controlled) | High | Variable | Strategic, supply-critical inputs |
| Just-in-time (JIT) | Low | Low (fragile) | Low | Minimal | Highly reliable transport and supply |
| Strategic stockpiling | Moderate | Very High | High | Very High | Unreliable supply or strategic materials |

---

## 5. Quantitative Parameters

### Supply Chain Performance Metrics

| Metric | Manual System (Stone/Bronze) | Organized System (Iron Age) | Industrial System | Semiconductor-Grade |
|--------|------------------------------|----------------------------|-------------------|---------------------|
| Number of managed SKUs | 20-50 | 50-200 | 200-2,000 | 2,000-50,000+ |
| Supplier count | 5-15 | 15-50 | 50-500 | 500-5,000+ |
| Inventory turns per year | 2-6 | 4-10 | 6-20 | 8-30+ |
| Order fulfillment rate | 70-85% | 85-95% | 95-99% | 99.0-99.9% |
| Lead time accuracy | ±50% | ±25% | ±10% | ±2-5% |
| Forecast accuracy | ±40% | ±25% | ±15% | ±5-10% |
| Inventory carrying cost | 30-50% of value/year | 20-35% | 15-25% | 10-20% |
| Stockout frequency | 10-20% of items/month | 5-10% | 2-5% | <1% |

### Buffer Stock Calculations

| Material | Daily Consumption | Lead Time (avg/max) | Safety Factor | Safety Stock | Reorder Point |
|----------|-------------------|---------------------|---------------|-------------|---------------|
| Charcoal (blast furnace) | 1,750 kg | 3/5 days | 1.5 | 5,250 kg | 10,500 kg |
| Iron ore | 2,250 kg | 1/3 days | 1.5 | 6,750 kg | 9,000 kg |
| Copper ingots (foundry) | 200 kg | 5/10 days | 2.0 | 2,000 kg | 3,000 kg |
| Grain (city of 5,000) | 7,500 kg | 7/14 days | 1.5 | 78,750 kg | 131,250 kg |
| Timber (construction) | 500 board-feet | 3/7 days | 1.5 | 3,000 bd-ft | 4,500 bd-ft |

### Transport Throughput Requirements

| Operation | Material Flow (tonnes/month) | Distance | Transport Mode | Trips Required |
|-----------|----------------------------|----------|----------------|----------------|
| Ore to furnace | 60-75 | 10 km | Ox cart (0.5 t) | 120-150 trips |
| Charcoal to furnace | 45-60 | 5 km | Ox cart (0.5 t) | 90-120 trips |
| Grain to city (5,000 pop.) | 225 | 20 km | River barge (10 t) | 23 barge loads |
| Copper to market | 5-10 | 50 km | Pack mule (150 kg) | 33-67 mule trips |
| Brick to construction site | 30 | 3 km | Hand cart (200 kg) | 150 cart trips |

---

## 6. Scaling Notes

- **Minimum viable supply chain**: A single production operation with 3-5 inputs from 2-3 suppliers. Manageable with a clay tablet and weekly review.
- **Complexity inflection point**: At ~10 inputs from 5+ suppliers, informal coordination fails. A dedicated supply chain coordinator (quartermaster, procurement officer) becomes necessary.
- **Geographic scaling**: Supply chains spanning >50 km require intermediate warehousing (way-stations) to buffer against transport delays. Estimate one way-station per 30-50 km of supply route.
- **Multi-tier supply chains**: When inputs themselves require multi-step production (e.g., firebrick requires clay + kiln + fuel), the supply chain becomes multi-tier. Each tier adds lead time and variability. Track each tier independently.
- **Information latency**: The time between a supply disruption and the coordinator's awareness of it determines the buffer stock needed. Messenger-based systems have 1-7 day latency. Signal systems (semaphore) reduce this to hours. Electronic communication reduces it to seconds.
- **Semiconductor-grade supply chains**: Modern semiconductor fabrication involves 300-500+ distinct chemical and material inputs, each requiring purity levels of 99.999-99.9999999%. The supply chain for each input is itself a multi-tier network. Total managed relationships: 1,000-5,000+.

---

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Chronic stockouts of key inputs | Underestimated demand variability; insufficient safety stock | Recalculate safety stock with higher safety factor (2.0-2.5); identify alternative suppliers |
| Excess inventory (warehouses full) | Overestimated demand; poor forecast accuracy; bulk purchasing without consumption planning | Implement consumption-based ordering; sell surplus through [trade](./trade.md); reduce reorder quantities |
| Late deliveries disrupting production | Transport bottleneck; unreliable supplier; weather delays | Identify backup transport routes; qualify secondary suppliers; increase buffer stock for unreliable inputs |
| Quality variation in supplied materials | No quality specifications; no incoming inspection | Define written quality standards for each input; inspect every incoming shipment; reject non-conforming material |
| Supply chain cost exceeding budget | Hidden costs (transport, storage, waste) not captured in planning | Implement full cost accounting (include transport, storage, spoilage, handling); identify cost reduction opportunities |
| Single-source dependency (critical input from one supplier) | No alternative developed; geographic constraint | Qualify at least 2 suppliers for every critical input; invest in alternative source development |

---

## 8. Safety

- **Warehouse hazards**: Stored materials can collapse, catch fire, or release toxic substances. Stack heavy materials no higher than 2 m; separate flammable materials from ignition sources; ventilate chemical storage areas.
- **Transport hazards**: Materials in transit are vulnerable to accidents, spillage, and contamination. Secure all loads; inspect containers before loading; transport hazardous materials in dedicated vehicles with appropriate signage.
- **Information integrity**: Supply chain data is safety-critical when it involves food, medicine, or hazardous materials. Incorrect inventory records can lead to consuming spoiled food or expired chemicals. Implement date tracking (expiry dates) and first-expired-first-out (FEFO) for perishable and degradable items.
- **Ergonomic risks**: Loading and unloading operations cause back injuries. Limit individual lift to 25 kg; use mechanical aids (carts, pulleys, ramps) for heavier loads; train workers in proper lifting technique.

---

## 9. Quality Control

- **Incoming inspection**: Every incoming shipment inspected against the purchase order specification. Check: quantity (±2%), quality (visual/physical test), and packaging integrity.
- **Supplier performance tracking**: Rate each supplier monthly on: on-time delivery rate, quality rejection rate, and responsiveness. Review suppliers scoring below 80% on any metric.
- **Inventory accuracy**: Monthly physical count vs. ledger. Target: >98% accuracy at the item level.
- **Forecast accuracy review**: Compare monthly forecasts to actual consumption. Track forecast error and adjust methods when error exceeds ±25%.
- **Document control**: All supply chain documents (orders, receipts, inspections) filed and retrievable for minimum 2 years. Audit trail must be complete and unbroken.

---

## 10. Variations and Alternatives

| Supply Chain Model | Description | Era | Best For |
|-------------------|-------------|-----|----------|
| Direct procurement | Buyer goes to source, selects and transports goods | Stone-age | Small-scale, local operations |
| Market-based procurement | Buyer purchases from market intermediaries | Bronze-age onwards | When markets are active and reliable |
| Contract-based supply | Written agreements specifying quantity, quality, delivery schedule, price | Iron-age onwards | High-volume, predictable demand |
| Vertical integration | Production organization owns its own supply sources (mines, forests, farms) | Industrial | When supply security outweighs flexibility |
| Just-in-time (JIT) | Materials arrive exactly when needed, minimal buffer stock | Advanced | When transport and supply are highly reliable |
| Buffer-heavy (strategic stockpiling) | Large inventories maintained as insurance against disruption | Any era | When supply is unreliable or strategically critical |

---

## 11. References

- [Transport](../transport/index.md) — the physical infrastructure that moves materials through the supply chain
- [Writing](../knowledge/writing.md) — the documentation system for orders, manifests, and records
- [Accounting](./accounting.md) — the cost tracking system that informs procurement decisions
- [Trade](./trade.md) — the exchange mechanism through which inputs are procured
- [Defense: Siege Warfare](../defense/siege-warfare.md) — a downstream dependent requiring military logistics
- [Photolithography: Fab Processes](../photolithography/fab-processes.md) — the pinnacle downstream dependent requiring hundreds of coordinated inputs

---

*Part of the [Bootciv Tech Tree](../index.md) • [Economics & Organization](./index.md) • [All Domains](../index.md)*
