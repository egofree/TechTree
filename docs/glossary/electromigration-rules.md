# Electromigration rules

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

Current flowing through metal wires causes atomic migration over time — the wire gradually thins until it opens (breaks) or hillocks (shorts to adjacent wire). Electromigration lifetime is modeled by Black's equation: MTTF ∝ J^(-n) × exp(Ea/kT), where J is current density, Ea is activation energy, and n ≈ 1-2. Rules specify maximum allowed current density per wire width, typically ensuring >10-year lifetime at maximum operating temperature. Wider wires required for higher currents. Copper is ...
