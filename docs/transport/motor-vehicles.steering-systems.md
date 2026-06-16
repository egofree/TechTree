# Steering Systems

> **Node ID**: transport.motor-vehicles.steering-systems
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.motor-vehicles`](./motor-vehicles.md)
> **Timeline**: Years 20-40+
> **Outputs**: steering_systems
> **Critical**: No

The steering system converts the driver's rotational input at the steering wheel into directional change of the front wheels, with appropriate mechanical advantage and road feedback. A good steering system is precise (minimal play), stable (self-centring after a turn), and communicates tire grip to the driver.

## Mechanism Types

**Rack and pinion**: A pinion gear on the end of the steering column meshes with a linear rack (a toothed steel bar). Rotating the steering wheel pushes the rack left or right, which moves the steering arms via tie rods. Simple, direct, and rigid — the dominant design on passenger cars since the 1970s. Gear ratio 15:1 to 20:1 (steering wheel turns : rack travel ratio). Steering wheel lock-to-lock: 2.5–3.5 turns.

**Recirculating ball**: A worm gear on the steering shaft engages a nut with steel ball bearings recirculating in the thread grooves (reducing friction). The nut moves a sector gear that rotates the Pitman arm, pushing a drag link and tie rods. Used on trucks and older cars — robust, handles heavy loads, but has more play and less road feel than rack and pinion.

## Ackermann Steering Geometry

In a turn, the inner wheel travels a tighter circle than the outer wheel. **Ackermann geometry** angles the inner wheel more sharply than the outer, so both wheels trace their respective turning circles without scrubbing. The geometry is built into the steering arms — the tie-rod ends are angled inward so that the steering pivots are on a line connecting the wheel contact points and the rear axle centre. Without Ackermann, the tires fight each other in every turn, scrubbing rubber and increasing rolling resistance.

## Power Steering

**Hydraulic power steering (HPS)**: An engine-driven pump (vane pump, 5–10 MPa) sends pressurized fluid to a control valve in the steering gear. The valve opens proportionally to steering input, assisting the rack with hydraulic pressure. Reduces parking effort from ~50 N to ~10 N at the steering wheel rim. Continuous pump draw costs 0.3–0.8 kW of engine power regardless of steering demand.

**Electric power steering (EPS)**: An electric motor (column-mounted or rack-mounted) provides assist, controlled by an ECU reading steering torque and vehicle speed. No hydraulic pump or fluid. Assist varies with speed — light at parking, firm at highway. Uses energy only when steering (saves 2–5% fuel vs. HPS). Enables lane-keep and autonomous steering when integrated with the vehicle network.

## Steering Feel

Road feedback — the forces transmitted back through the steering wheel to the driver's hands — is critical for vehicle control. Too little feedback (over-assisted EPS) feels numb and disconnected; too much transmits every road imperfection as wheel kickback. Hydraulic systems provide natural feedback; EPS requires careful calibration to simulate it.

## See Also

- [Motor Vehicle Fundamentals](./motor-vehicles.md) — parent capability overview
- [Suspension Systems](./motor-vehicles.suspension-systems.md) — front suspension geometry integrates with steering
- [Chassis & Frame Construction](./motor-vehicles.chassis-frame-construction.md) — steering rack mounts to the chassis

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
