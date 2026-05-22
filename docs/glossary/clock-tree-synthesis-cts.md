# Clock tree synthesis (CTS)

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

Distribute the clock signal from the pad to every flip-flop with minimal skew (all flip-flops see the clock edge at nearly the same time). Target skew: < 50 ps for high-performance designs. Buffer chains and mesh structures balance delays across the die. Clock tree power can be 20-40% of total dynamic power — minimizing buffer count matters.
