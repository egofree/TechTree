# Range Safety

> **Node ID**: `space-ground-ops.range-safety`
> **Domain**: [Space Ground Ops](./index.md)
> **Dependencies**: [`defense`](../defense/index.md),
> [`optics`](../optics/index.md), [`telecom.radio`](../telecom/radio.md)
> **Enables**: Public-safety-acceptable launch operations, destruct-line compliance,
> impact-point prediction, post-flight trajectory reconstruction
> **Timeline**: Years 50+
> **Outputs**: range_services
> **Critical**: YES — a launch vehicle is an explosive ballistic object that can, if it
> departs its planned trajectory, reach a populated area in minutes. Range safety is the
> system that prevents that outcome. It is the one part of the ground segment whose failure
> kills people outside the fence.

Range safety is the public-safety function of a launch range. Its job is to guarantee that a
launch vehicle, from the moment its engines ignite until it has cleared the range, stays
inside a pre-approved flight envelope — and to **terminate the flight** the instant it does
not. The discipline draws on three pillars: a flight termination system that can end the
flight on command, a tracking network that measures where the vehicle actually is, and an
impact-prediction capability that decides whether the measured trajectory is still safe. This
article covers all three, with U.S. Eastern and Western Range practice as the reference.

## The Destruct Line and the Flight Envelope

Before a launch, the range safety engineer defines a set of **destruct lines** — boundaries
in the flight envelope beyond which the vehicle may not go without action. These are derived
from the vehicle's impact dispersion (where debris would fall if the vehicle broke up at that
point) and the population density downrange. The fundamental rule is simple: if the predicted
instantaneous impact point (IIP) — the place the vehicle would hit if thrust ceased now —
crosses into a populated area, the flight must be terminated.

The flight envelope is tracked in three dimensions and in time. A nominal trajectory is
approved before flight; the tracking network compares the measured trajectory against it,
continuously, in real time. Two outcomes trigger action:

1. **Track deviates destructively** — the vehicle is heading somewhere it must not.
2. **Loss of track** — the range can no longer see where the vehicle is. A vehicle the range
   cannot see is, by definition, uncontrolled, and may be terminated on that basis alone.

## Flight Termination System (FTS)

The FTS is the hardware that ends the flight. It is engineered to a different standard than
almost anything else in the launch stack because it must work exactly when called upon, after
a flight of minutes to hours of dormancy, and must **never** fire spuriously.

### Destruct Charges

The most common FTS action is a linear shaped charge or exploding bridgewire detonation that
physically ruptures the propellant tanks. The intent is not to "explode" the vehicle in the
Hollywood sense but to **disperse the propellant** — venting it so that it does not detonate
on ground impact as a single combined mass. A ruptured tank spreads the propellant over a
wide area, where it burns or evaporates harmlessly (relative to a tanked impact).

The charges are threaded along the length of the tanks and sized to cut the tank wall
reliably. Their initiation must sever the structure without scattering large intact pieces —
the goal is many small, light fragments whose ballistic coefficient makes them fall short of
populated areas.

### Command Destruct Receiver

The charge is fired by a command-destruct receiver carried on the vehicle. It listens on a
dedicated UHF uplink (the FTS band, separate from the vehicle's command uplink) for an
encrypted arm-and-fire sequence. The sequence is normally:

1. **Arm** — the receiver's safing is removed, the firing capacitors charge.
2. **Fire** — a second, distinct command releases the energy to the detonators.

The two-command architecture is the core of the fail-safe design: a single garbled command or
single-bit error cannot fire the system, because arming alone does nothing and firing alone
(without arm) does nothing.

### Dual-Redundant Fail-Safe Architecture

A modern FTS is **dual-string redundant** and engineered to be fail-safe on common-cause
failures:

- Two independent receivers, two independent batteries, two independent firing circuits, two
  independent sets of detonators. Either string can terminate the flight alone.
- The two strings are deliberately diverse — different receiver vendors, different crypto
  modules — so a design defect or environmental fault that disables one is unlikely to
  disable the other.
- The system is armed and safed by physical, mechanical means (latching pins, safe-and-arm
  devices rotated by motor or by hand) so that no software error can inadvertently fire it.

The reliability requirement is stark: the probability of "fail to terminate when commanded"
must be below roughly **1 in 10,000** (often far lower) per mission, and the probability of
inadvertent termination during normal flight must be comparably tiny. The architecture is
quantitatively analysed via fault-tree analysis before every mission.

### Autonomous Flight Termination

A newer variant, the Autonomous Flight Termination System (AFTS), moves the destruct
decision from the ground to the vehicle: an on-board computer compares GPS-measured position
and velocity against the pre-loaded envelope and arms/fires without ground command. AFTS
shrinks the ground footprint (no need for the ground command-transmit site or its operators)
and shortens reaction time, but it places enormous weight on the integrity of the on-board
navigation and rule-checking software — which is itself subject to a rigorous, independent
safety review.

## Range Tracking Network

### C-Band Tracking Radar

The primary metric tracking instrument for decades has been the **C-band skin-track radar**.
The exemplar is the **AN/FPS-16**, an instrumented tracking radar developed in the 1950s and
refined continuously since. It transmits at ~5.4–5.9 GHz, tracks the vehicle's skin echo
(no transponder required), and delivers metric data (range, azimuth, elevation) accurate to
a few metres and a fraction of a milliradian.

| Radar | Role | Notes |
|-------|------|-------|
| AN/FPS-16 | precision metric track | ~5.5 GHz, skin-track, the workhorse since the 1950s |
| AN/FPQ-6 / FPQ-16 | upgraded metric track | higher-accuracy successor families |
| Multi-object tracking radar | debris tracking | tracks breakup fragments after a termination |

Skin-track (listening for the reflection of the radar's own pulse off the vehicle hull) is
valuable because it needs no cooperation from the vehicle — it works on a dead or unresponsive
rocket just as well as a healthy one. The limitation is signal: the echo falls with the
fourth power of range, so long-range tracking is aided by a vehicle-borne C-band beacon
transponder.

### Tracking Algorithms and High-Acceleration Lock

Maintaining radar lock during ascent is non-trivial. The vehicle accelerates at several g,
executes pitch and yaw programmes, and may stage (a violent event that briefly doubles the
target as two objects). The tracking servo uses a Kalman-filter-based predictor to keep the
antenna pointed where the vehicle is expected to be a few milliseconds hence, updating the
predictor from each return. Loss of lock at staging is common and recovered within seconds
if the predictor holds the estimated trajectory through the gap.

### Trajectory Filtering and Impact Prediction

The radar's raw returns feed a real-time trajectory filter that fuses multiple radars (a
range typically fields two or more for redundancy and geometry) and produces a best estimate
of position and velocity. From that state vector the filter propagates the **instantaneous
impact point** forward — where would the vehicle be, in three dimensions, if thrust ceased
now? — and projects the predicted impact point along the planned flight.

The IIP is plotted against the destruct lines on the range safety display. If it touches or
crosses a line, the range safety officer (or, in autonomous systems, the on-board rule
checker) is committed to action. The decision is made in seconds; a vehicle flying at
kilometres per second gives the operator no time to deliberate.

## Optical Tracking

Optical tracking is the independent, non-RF measurement of ascent trajectory. It is
deliberately diverse from the radar — it cannot be jammed, spoofed, or affected by an RF
failure — and it produces metric-quality data from triangulation rather than timing.

### Cinetheodolites

A cinetheodolite is a precision theodolite (an instrument for measuring azimuth and elevation
angles) fitted with a camera — historically film, now digital sensors. The exemplar mount is
the **Contraves** cinetheodolite, a Swiss-designed precision instrument deployed at ranges
worldwide. A typical installation fields **two to six stations** spaced along the coast or
around the pad, each recording the ascending vehicle against a precision angle reference
(markers of known azimuth and elevation etched into the image).

### Triangulation

Each station yields a direction (azimuth, elevation) to the vehicle as a function of time.
With two or more stations observing the same event, the lines of sight intersect in three
dimensions to give the vehicle's position; with a sequence of frames the trajectory is
reconstructed. The accuracy is comparable to radar for the boost phase: the vehicle is close,
bright, and slow enough (relative to orbital velocity) for high-quality triangulation.

### Photogrammetry and Attitude

Beyond position, optical tracking yields **attitude** — the orientation of the vehicle —
which radar does not. The shape and aspect of the vehicle in the image, fitted against a
geometric model, give pitch, yaw, and roll throughout ascent. For a post-flight anomaly
investigation this is often the decisive evidence: a staging failure captured at 1000 fps
from two angles tells the story that telemetry could not.

### Modern Digital Tracking

Film has given way to high-frame-rate digital cameras (often with very long focal-length
optics on precision mounts), and the data reduction that once took days in a darkroom is now
automated photogrammetry. But the principle is unchanged: triangulate from multiple,
geometrically calibrated viewing angles.

## Reference Ranges

| Range | Operator | Launch azimuth / use |
|-------|----------|----------------------|
| Eastern Range (Cape Canaveral / KSC) | USSF Space Launch Delta 45 | eastward, LEO/GTO, crewed |
| Western Range (Vandenberg SFB) | USSF Space Launch Delta 30 | polar/sun-sync, westward |
| Wallops Flight Facility | NASA | small/medium, mid-Atlantic |
| Kourou / Guiana Space Centre | ESA / CNES | eastward, equatorial advantage |
| Baikonur | Roscosmos | historic; all azimuths |
| Jiuquan / Wenchang | CNSA | crewed, incl. lunar precursor |

Each operates on the same destruct-line discipline; the differences are in geometry, downrange
island chains used as tracking assets (e.g., Antigua, Ascension for the Eastern Range), and
the local regulatory authority.

## Debris Footprint and Casualty Expectation

The quantitative safety target is the **collective casualty expectation** — the expected
number of casualties to the public from a launch, integrated over the mission. U.S. range
regulation typically caps this at roughly **1×10⁻⁴** (one expected casualty per ten thousand
launches) for the collective risk, with additional per-event limits. Every destruct decision,
debris model, and flight-envelope boundary is ultimately justified against this number.

Debris modelling computes, for a breakup at any point along the trajectory, the size and mass
distribution of fragments, their ballistic coefficients, their dispersal under wind, and the
population density where they would land. The destruct lines are placed so that the residual
risk stays within the casualty-expectation budget. A range safety engineer who proposes a new
trajectory or a tighter envelope must re-run this analysis end to end.

## The Range Safety Officer

Behind the hardware is a person: the range safety officer (RSO) or, in modern terminology,
the flight control team responsible for the destruct decision. The RSO sits at the range
safety display during ascent, watches the IIP against the destruct lines, and holds the arm
and fire switches. The job is to make a life-or-death call in seconds, on the basis of
ambiguous data (is that a real deviation or a tracking glitch?), with the absolute authority
to terminate the flight and the absolute responsibility not to do so unless necessary. RSOs
are trained for years and certified by simulation before they sit a real launch.

## Collateral Instrumentation

Beyond the primary radar and optical chain, a range fields supporting instruments:

- **Telemetry-receiving sites** — receive the vehicle's own telemetry during ascent, used to
  confirm vehicle health (an engine-out is itself a termination criterion independent of
  trajectory).
- **Meteorological assets** — wind towers and balloons that feed the debris dispersal model;
  upper winds are measured minutes before flight so the destruct lines reflect actual
  conditions, not climatology.
- **Downrange optical and radar sites** — islands or ships that extend tracking beyond the
  horizon from the mainland, covering the full boost phase.
- **Debris-recovery and post-termination imaging** — for after-action analysis when a flight
  has been terminated.

## Dependencies

Range safety inherits from three established domains:

- **[defense](../defense/index.md)** — the destruct charges, command-destruct receivers, and
  safe-and-arm devices are continuous with military ordnance engineering. The whole
  discipline grew out of ballistic-missile range practice.
- **[optics](../optics/index.md)** — cinetheodolites and precision optical tracking mounts
  are direct descendants of optical-theodolite and instrument-optics heritage.
- **[telecom.radio](../telecom/radio.md)** — the command-destruct uplink, the tracking
  radars, and the telemetry that feeds the impact predictor are all radio engineering.

## See Also

- [Mission Control](./mission-control.md) — the post-ascent counterpart
- [Ground Stations](./ground-stations.md) — the spacecraft-tracking infrastructure
- [Flight Termination](./range-safety.flight-termination.md) — FTS design
- [Range Radar](./range-safety.range-radar.md) — C-band tracking
- [Optical Tracking](./range-safety.optical-tracking.md) — cinetheodolites
- [Defense](../defense/index.md) — ordnance engineering heritage
- [Optics](../optics/index.md) — theodolite and precision-mount heritage
