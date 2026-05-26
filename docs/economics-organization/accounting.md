# Accounting & Record-Keeping

> **Node ID**: economics-organization.accounting
> **Domain**: [Economics & Organization](./index.md)
> **Dependencies**: [`mathematics.core-mathematics`](../mathematics/core-mathematics.md), [`knowledge.writing`](../knowledge/writing.md)
> **Enables**: [`economics-organization.supply-chain`](./supply-chain.md)
> **Timeline**: Years 5-15
> **Outputs**: financial_records, inventory_ledgers, cost_accounting
> **Critical**: No

---

## 1. Overview

Accounting is the systematic recording, classification, and summarization of economic transactions — production inputs consumed, goods produced, trades completed, debts incurred and settled, and inventories on hand. It provides the information infrastructure for rational economic decision-making: without accounting, a community cannot know whether it is producing at a profit or a loss, which activities generate the most value, or whether resources are being wasted.

Accounting emerges when the volume of economic activity exceeds what can be tracked mentally. This threshold is approximately 50 specialists or 200+ regular transactions per month — beyond this, the human mind cannot maintain an accurate running tally of who owes what to whom, what materials are in stock, and what production costs have been incurred.

The capability depends on [core mathematics](../mathematics/core-mathematics.md) for arithmetic operations (addition, subtraction, multiplication for quantities and values) and on [writing](../knowledge/writing.md) for permanent records that can be reviewed, audited, and referenced over time. Accounting transforms economic activity from a memory-based oral system into a document-based system that scales indefinitely.

---

## 2. Prerequisites

### Materials

- **Recording media**: Clay tablets (50-500 per year for active accounts), papyrus/paper (20-100 sheets per year), or wax tablets for temporary records. Quantity scales with transaction volume.

### Tools and Equipment

- [Writing implements](../knowledge/writing.md): Styluses for clay, pens/brushes for papyrus or paper.
- [Calculation tools](../mathematics/core-mathematics.md): Abacus or counting board for rapid arithmetic. An abacus reduces calculation time by 3-5x compared to mental arithmetic for multi-digit operations.
- Balance scales: For inventory verification (weighing stock against records).

### Knowledge

- **Arithmetic proficiency**: Addition, subtraction, multiplication, and division of quantities and values. Minimum: facility with 4-digit numbers for accumulated totals.
- **Double-entry principles**: Every transaction recorded in two places (debit and credit) so that the sum of all accounts always balances. This error-detection mechanism is the foundation of reliable accounting.
- **Classification systems**: The ability to group transactions into categories (materials purchased, labor costs, goods sold, overhead) for meaningful analysis.

### Infrastructure

- Secure records storage: Dry, fire-protected space for ledgers. Accounting records are irreplaceable — loss of records means loss of economic memory.
- Work surfaces: Tables or desks for writing and calculation.

---

## 3. Bill of Materials (BOM)

| Material | Quantity per Year (Community of 1,000) | Source | Alternatives |
|----------|----------------------------------------|--------|-------------|
| Clay tablets | 200-500 | [Pottery](../ceramics/index.md) | Papyrus sheets (50-100), paper (30-80 sheets) |
| Writing styluses (bone/wood) | 5-10 | [Basic Tools](../foundations/index.md) | Reed pens (for papyrus), quill pens (for paper) |
| Ink (if using papyrus/paper) | 1-2 L | [Chemistry](../chemistry/index.md) — iron gall or carbon ink | Charcoal + water (temporary, fades) |
| Abacus or counting board | 1-2 | [Woodworking](../foundations/index.md) | Pebbles on lined surface (less efficient) |
| Storage chests/shelves | 2-5 | [Woodworking](../foundations/index.md) | Niche in stone wall (fireproof) |

---

## 4. Process Description

### 4.1 Setting Up an Accounting System

1. **Define the unit of account**: Choose a standard value unit. If [currency](./currency.md) exists, use the monetary unit (e.g., "copper coins"). If not, use a commodity reference (e.g., "kg grain equivalent"). All transactions are recorded in this unit.

2. **Create the chart of accounts**: Establish account categories:
   - **Assets**: What the community owns (inventory, tools, buildings, cash/coinage)
   - **Liabilities**: What the community owes (debts to traders, unpaid wages)
   - **Income**: Value flowing in (goods sold, taxes received)
   - **Expenses**: Value flowing out (materials purchased, wages paid, overhead)

3. **Establish the ledger format**: Each account has its own page or section. Format:
   ```
   Date | Description | Debit (value in) | Credit (value out) | Balance
   ```

### 4.2 Recording Transactions

4. **Record each transaction in real-time**: Do not batch — record as transactions occur. For each trade, purchase, or production input consumed:
   - Identify the two accounts affected (e.g., "Inventory" and "Cash")
   - Record the debit in one account and the credit in the other
   - Verify that debits = credits for every transaction

5. **Maintain subsidiary ledgers**: For high-volume accounts (e.g., individual trader accounts), maintain separate sub-ledgers that roll up into the main ledger. One sub-ledger per trader, one per production workshop.

6. **Reconcile daily**: At end of each business day, sum all debits and all credits across all accounts. Total debits must equal total credits. Any discrepancy indicates a recording error.

### 4.3 Periodic Reporting

7. **Close the books monthly**: Sum each account's balance. Calculate key metrics:
   - Total inventory value
   - Total cash/coinage on hand
   - Net income (income minus expenses)
   - Accounts receivable (money owed to the community)
   - Accounts payable (money the community owes)

8. **Conduct physical inventory count**: Monthly, physically count and weigh all stored goods. Compare to ledger values. Discrepancies >2% trigger investigation (theft, spoilage, recording error).

9. **Prepare summary reports**: For the coordinator/governance, provide:
   - Balance sheet (assets vs. liabilities)
   - Income statement (revenue minus costs)
   - Inventory status (stock levels vs. minimum thresholds)

---

## 5. Quantitative Parameters

### Accounting Precision Requirements

| Metric | Bronze-Age (Clay Tablets) | Iron-Age (Papyrus/Paper) | Industrial (Bound Ledgers) |
|--------|---------------------------|--------------------------|----------------------------|
| Decimal precision | Whole numbers only | 1-2 decimal places | 2-4 decimal places |
| Calculation speed (abacus) | 20-50 operations/hour | 50-100 operations/hour | 100-200 operations/hour |
| Ledger entries per day | 10-30 | 30-100 | 100-500+ |
| Error rate (manual) | 2-5% per 100 entries | 1-3% per 100 entries | 0.5-2% per 100 entries |
| Reconciliation time (daily) | 1-2 hours | 30-60 minutes | 15-30 minutes |
| Record retention period | Permanent (baked clay) | 10-50 years (papyrus) | 7-30 years (paper) |
| Ledger capacity (entries per volume) | 50-200 per tablet | 500-2,000 per scroll | 5,000-20,000 per bound book |

### Key Financial Ratios for Bootstrap Communities

| Ratio | Formula | Healthy Range | Warning Threshold |
|-------|---------|---------------|-------------------|
| Inventory turnover | Cost of goods sold / Average inventory value | 4-12/year | <2/year (overstock) or >20/year (stockouts) |
| Current ratio | Current assets / Current liabilities | 1.5-3.0 | <1.0 (insolvency risk) |
| Labor cost fraction | Total wages / Total production cost | 30-60% | >70% (insufficient materials) or <20% (under-investment in skills) |
| Waste ratio | Spoilage + defects / Total production | <5% | >10% (process quality problem) |
| Debt-to-income | Total liabilities / Annual income | <0.5 | >1.0 (debt crisis) |

---

## 6. Scaling Notes

- **Minimum viable accounting**: A single clay tablet or sheet tracking 3-5 categories (food stores, tool inventory, trade debts, outstanding obligations). Viable for communities of 50-100 people.
- **Double-entry threshold**: At ~50 regular trading partners or ~200 monthly transactions, single-entry accounting (just recording inflows and outflows) becomes unreliable — errors accumulate undetected. Switch to double-entry at this point.
- **Specialization of accountants**: At ~500-1,000 transactions/month, a dedicated bookkeeper is needed. This person does not produce goods — they produce information. The cost is justified when accounting-identified savings (reduced waste, better purchasing decisions, fraud detection) exceed the bookkeeper's salary.
- **Archive growth**: Accounting records accumulate at 200-500 tablets/pages per year. Within 10 years, storage becomes a significant concern. Designate a records room with fire protection and climate control (dry conditions for clay; moderate humidity for paper).
- **Transition to computing**: Manual accounting limits practical transaction volume to ~500/day per bookkeeper. Beyond this, computing aids (mechanical calculators, then electronic computers) are needed. See [computing](../computing/index.md).

---

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Ledger does not balance (debits ≠ credits) | Recording error: transposition, omission, or double-entry | Trace back from last balanced point; check each entry for common errors (digit transposition, wrong account) |
| Inventory count disagrees with ledger | Theft, spoilage, unrecorded issues/receipts, counting error | Recount inventory; check receiving and issuing records; investigate discrepancies >2% |
| Duplicate payments detected | Same transaction recorded twice; no unique transaction IDs | Assign sequential transaction numbers; check for duplicates before posting |
| Records damaged (water, fire, mold) | Inadequate storage conditions | Restore from backup copies (maintain duplicate ledgers stored separately); improve storage environment |
| Accountant overwhelmed with volume | Transaction growth exceeded staffing | Hire additional bookkeeper; subdivide accounts by type; implement batch processing for routine transactions |
| Fraudulent entries discovered | Insider manipulation of records | Segregate duties (one person records, another approves); require dual signatures on payments; conduct surprise audits |

---

## 8. Safety

- **Fire risk**: Accounting records are typically stored on flammable media (papyrus, paper). A fire that destroys the ledgers erases the community's economic memory. Mitigate with fireproof storage (stone vaults), duplicate records stored in a separate building, and fire suppression (sand buckets, water access).
- **Ergonomic hazards**: Bookkeepers work hunched over ledgers for 6-10 hours/day, risking back pain, eye strain, and repetitive wrist injury. Mandate breaks every 60-90 minutes; provide proper seating and lighting; limit daily accounting work to 8 hours.
- **Ink toxicity**: Iron gall ink (common for permanent records) contains ferrous sulfate and tannins — mildly toxic with chronic skin exposure. Carbon ink is safer. Ensure adequate ventilation in writing areas.
- **Information security**: Accounting records reveal the community's financial position, inventories, and vulnerabilities. Restrict access to authorized personnel only. Maintain a log of who accesses the ledgers.

---

## 9. Quality Control

- **Daily reconciliation**: Total debits must equal total credits. Any imbalance halts further recording until resolved.
- **Monthly physical audit**: Count all inventory, weigh all stored metals/grain, and reconcile with ledger values. Acceptable discrepancy: <2% by value.
- **Independent review**: A second person (not the primary bookkeeper) reviews all entries monthly, looking for unusual patterns, missing documentation, or mathematical errors.
- **Transaction documentation**: Every ledger entry must reference a source document (receipt, invoice, tally stick). Entries without source documents are flagged for investigation.
- **Archival integrity**: Records older than 1 year are sealed and stored. Any access to archived records is logged and requires authorization.

---

## 10. Variations and Alternatives

| Accounting Method | Description | Best For | Limitations |
|-------------------|-------------|----------|-------------|
| Single-entry (cash book) | Simple record of money in/money out | Small operations (<50 transactions/month) | No error detection; no asset tracking |
| Double-entry bookkeeping | Every transaction recorded as balanced debit/credit | Any operation with >50 transactions/month | Requires trained bookkeeper; more complex to set up |
| Tally stick accounting | Notched wooden sticks split between parties | Tax collection, debt tracking | Limited data capacity; no complex analysis |
| Quipu (knotted cord) | Knot patterns encode numerical data | Communities without writing | Limited to numerical data; no narrative descriptions |
| Clay token accounting | Shaped clay tokens represent goods quantities | Earliest accounting (pre-writing) | No written detail; limited to simple counting |
| Spreadsheet (paper) | Tabular format with rows and columns | Multi-category analysis | Labor-intensive for large datasets |

### Accounting System Evolution by Era

| Era | Recording Medium | Calculation Tool | Typical Ledger Size | Key Innovation |
|-----|-----------------|-----------------|---------------------|----------------|
| Stone-age | Tally sticks, notched bones | Pebbles, fingers | 10-30 entries | First quantitative records |
| Copper-age | Clay tablets | Counting boards | 50-500 entries | Written numerical records |
| Bronze-age | Clay tablets, papyrus | Abacus | 500-5,000 entries | Double-entry bookkeeping |
| Iron-age | Papyrus, parchment | Abacus, counting table | 5,000-50,000 entries | Cost accounting, audits |
| Industrial | Paper ledgers | Mechanical calculator | 50,000-500,000 entries | Standardized financial statements |
| Modern | Electronic | Digital computer | Unlimited | Real-time accounting, automated reconciliation |

---

## 11. References

- [Core Mathematics](../mathematics/core-mathematics.md) — the arithmetic foundation for all accounting
- [Writing](../knowledge/writing.md) — the recording technology that makes permanent accounting possible
- [Currency](./currency.md) — the unit of account used in financial records
- [Division of Labor](./division-of-labor.md) — specialization creates the economic complexity that requires accounting
- [Supply Chain Coordination](./supply-chain.md) — the planning system that depends on accounting data

---

*Part of the [Bootciv Tech Tree](../index.md) • [Economics & Organization](./index.md) • [All Domains](../index.md)*
