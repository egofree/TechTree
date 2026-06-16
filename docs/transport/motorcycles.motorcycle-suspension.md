# Motorcycle Suspension Systems

> **Node ID**: transport.motorcycles.motorcycle-suspension
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.motorcycles`](motorcycles.md)
> **Timeline**: Years 20-40+
> **Outputs**: motorcycle_suspensions
> **Critical**: No

Motorcycle suspension isolates the chassis from road irregularities, maintains tire contact with the surface, and controls the pitch and ride-height dynamics under braking and acceleration. Proper suspension is the single largest contributor to handling quality after frame geometry.

## Front Suspension

**Telescopic fork**: The dominant front suspension since the 1930s. Two tubes slide within outer stanchions, carrying the front wheel and brake. Internal coil spring (7-15 N/mm) and oil-bath damper. Conventional forks have the thicker stanchion on top; **upside-down (inverted) forks** reverse this, putting the larger-diameter tube in the triple clamp for reduced unsprung weight and greater bending stiffness — standard on sport bikes. Travel: 100-130 mm (sport), 200-300 mm (dual-sport).

**Anti-dive**: Under braking, weight transfers forward and the fork compresses (dive). Excessive dive changes geometry and reduces available cornering clearance. Anti-dive mechanisms (mechanical linkage or hydraulic restriction tied to brake pressure) limit compression during braking, keeping the geometry stable.

## Rear Suspension

**Twin-shock**: Two shock absorbers flanking the swingarm — the classic arrangement (pre-1980s). Simple, robust, but heavier and prone to binding under asymmetric loading.

**Mono-shock**: A single shock absorber actuated through linkage (rising-rate linkage makes the suspension progressively stiffer as it compresses). Lighter unsprung weight, better control, no side-to-side binding. Standard on all modern sport and dual-sport motorcycles since Yamaha Monocross (1970s).

## Steering Damper

A hydraulic cylinder between frame and fork, resisting rapid steering movement. Essential on sport bikes with low trail (90-100 mm) to prevent **tank-slappers** — violent handlebar oscillation at high speed. The damper allows deliberate rider input while suppressing involuntary high-frequency movement.

## Tuning Parameters

- **Spring rate**: matched to rider weight and use (street vs. track)
- **Compression damping**: controls dive and bump absorption
- **Rebound damping**: controls extension speed after compression
- **Preload**: sets ride height and static sag (typically 25-35 mm front, 30-40 mm rear)

## Prerequisites

- [Iron & Steel](../metals/iron-steel.md) — fork tubes, springs, damper pistons
- [Machine Tools](../machine-tools/index.md) — precision boring, surface hardening
- [Motorcycles](motorcycles.md) — parent capability

## See Also

- [Motorcycles](motorcycles.md) — parent capability
- [Motorcycle Frame Design](motorcycles.motorcycle-frames.md) — chassis and swingarm pivot

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
