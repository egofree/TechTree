# Layout vs. schematic (LVS) in P&R flow

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

After place and route completes, the final layout is extracted back to a netlist and compared to the original synthesized netlist. Any discrepancy (wrong connection, missing via, shorted nets) is flagged. This is a separate LVS check from the schematic-level one — it catches physical implementation errors specifically.
