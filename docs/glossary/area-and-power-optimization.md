# Area and power optimization

> **Type**: material | **Tier**: important | **Domains**: vlsi-scaling

After timing closure, the tool minimizes area (smaller die = more chips per wafer = lower cost) and power (dynamic power = C·V²·f, static power = leakage). Clock gating disables clock to idle blocks, reducing dynamic power 20-50%. Multi-Vt libraries offer tradeoffs: low-Vt cells are fast but leak more; high-Vt cells are slow but leak less.
