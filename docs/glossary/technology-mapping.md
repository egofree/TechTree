# Technology mapping

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

The synthesizer maps generic Boolean operations to available standard cells in the target process library. Different cells have different drive strengths (1x, 2x, 4x, 8x inverter sizes) — the tool selects cells that meet timing with minimum area. A NAND gate might be mapped to a single library cell or built from smaller cells depending on fanout requirements.
