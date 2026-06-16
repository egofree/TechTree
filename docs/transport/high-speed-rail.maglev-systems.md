# Magnetic Levitation Systems

> **Node ID**: transport.high-speed-rail.maglev-systems
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.high-speed-rail`](high-speed-rail.md)
> **Timeline**: Years 50-70+
> **Outputs**: high_speed_trains
> **Critical**: No

Magnetic levitation eliminates wheel-rail contact, removing the kinematic constraints of hunting and the tractive-effort cap of adhesion. Two technologies dominate: electromagnetic suspension (EMS, attractive, 8–10 mm gap, active control) and electrodynamic suspension (EDS, repulsive, 100 mm gap, superconducting coils). Maglev enables 500–600+ km/h cruising — beyond the economic ceiling of wheel-rail — at the cost of guideway precision and capital intensity 3–5× conventional HSR.

## Electromagnetic Suspension (EMS) — Transrapid

Electromagnets on the train underside pull upward against a steel guideway rail, levitating 8–10 mm below the guideway. The gap is unstable: control must correct disturbances within milliseconds or the train touches down. Active gap sensors sample at 100 kHz and adjust magnet current to hold the gap at 10 mm ± 1 mm. Propulsion: linear synchronous motor integrated into the guideway (track is the stator). The Shanghai Transrapid (2004) reaches 430 km/h in commercial service; design speed 500 km/h.

## Electrodynamic Suspension (EDS) — JR-Maglev

Superconducting electromagnets on the train (NbTi coils in liquid helium at 4 K, persistent-mode, 700 kA-turns) induce repulsive currents in aluminum coils embedded in the guideway walls above 100 km/h. Below takeoff speed the train runs on retractable wheels. The 100 mm gap is inherently stable and far more tolerant of guideway irregularity than EMS. The JR-Maglev L0 series set the world rail speed record of 603 km/h (2015); commercial Tokyo–Nagoya service targets 500 km/h.

## Guideway Precision

- **EMS**: ±0.6 mm over 3 m measurement chord. Requires laser alignment during construction and periodic re-survey. Thermal expansion controlled by white paint (low solar absorption) and expansion joints at 20–30 m intervals.
- **EDS**: ±2 mm over 10 m chord. More relaxed than EMS due to larger gap, but still an order of magnitude tighter than conventional railway.

## Cost and Maturity

Maglev guideway cost: 50–100 M USD/km (3–5× conventional HSR). Justified only where population density and trip volume are extreme. The Chuo Shinkansen (Tokyo–Nagoya–Osaka, under construction) is the only large-scale commercial deployment in progress. Cryogenic systems (EDS) and active control electronics (EMS) add vehicle cost and maintenance burden.

## Prerequisites

- [High-Speed Rail](high-speed-rail.md) — parent capability and system context
- [Electricity](../energy/electricity.md) — power supply for guideway motors and magnets
- [Electronics](../electronics/index.md) — active gap control and power converters
- [Iron & Steel](../metals/iron-steel.md) — guideway structural steel and reinforcement

## See Also

- [High-Speed Rail](high-speed-rail.md) — parent capability overview
- [Aerodynamic Trainset Design](high-speed-rail.aerodynamic-design.md) — vehicle shaping (maglev needs even more aerodynamic optimization at 500+ km/h)
- [High-Speed Track Geometry](high-speed-rail.track-geometry.md) — conventional track counterpart

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
