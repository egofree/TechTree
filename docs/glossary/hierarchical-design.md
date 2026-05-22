# Hierarchical design

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

Large designs decompose into blocks → sub-blocks → leaf cells. A GPU may have 50-200 blocks, each containing 10,000-10,000,000 gates. Hierarchy enables team parallelism — separate teams work on different blocks independently, integrating at the top level. Block interfaces defined by timing budgets, area budgets, and pin lists.
