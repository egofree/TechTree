# Computational lithography at scale

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

A modern system-on-chip has 10^8-10^9 shapes per layer, with 30-50 mask layers. Full-chip OPC optimization requires evaluating every shape through the lithography model, computing corrections, and iterating until convergence. Runtime: hours to days per layer on compute clusters with 100-1000 CPUs. GPU-accelerated lithography simulation reduces this by 10-50×. The OPC-optimized mask data is enormous — a single layer's mask file can be 100 GB - 1 TB. Mask data preparation compresses and formats...
