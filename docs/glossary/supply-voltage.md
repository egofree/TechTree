# Supply voltage

> **Type**: noun | **Tier**: important | **Domains**: computing

TTL is strictly 5V ±0.25V. CMOS tolerates wider ranges but exceeding maximum VDD (7V for HC, 15V for 4000 series) causes latchup, a parasitic thyristor fires and shorts VDD to ground, destroying the chip instantly. Current-limited bench supplies (100-200 mA) limit damage during prototyping.
