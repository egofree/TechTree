# Power analysis and signoff

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

Dynamic power dissipation calculated from switching activity (toggle rates per net) × capacitance × V². Leakage power modeled per-cell based on state, voltage, and temperature. Total power budget determines package thermal design — exceeding thermal limits causes timing degradation and eventual failure. Power grids (VDD and VSS) must have low enough resistance to deliver current without excessive IR drop (>5-10% of supply voltage is a violation) and low enough inductance to prevent simultaneo...
