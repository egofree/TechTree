# Finite difference method example

> **Type**: material | **Tier**: important | **Domains**: computing

To tabulate x² for x = 1, 2, 3..., start with value=1, first difference=3 (2²-1²), second difference=2 (constant for quadratics). Each step: add 2nd diff to 1st diff (3→5→7...), then add 1st diff to value (1→4→9...). Only additions required, no multiplication. Higher-order polynomials need more difference columns but the principle is identical.
