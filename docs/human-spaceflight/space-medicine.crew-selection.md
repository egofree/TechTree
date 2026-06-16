# Crew Selection

> **Node ID**: human-spaceflight.space-medicine.crew-selection
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.space-medicine`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 60+
> **Outputs**: crew_medical
> **Critical**: No

Crew selection is the medical and psychological screening process that identifies candidates physically and mentally suited for the spaceflight environment. The governing standard is NASA-STD-3001 (Volumes 1 and 2), which defines anthropometric envelopes, visual and auditory thresholds, cardiovascular reserve, and psychological suitability criteria. Each candidate undergoes a multi-day evaluation including graded exercise stress testing, ophthalmologic examination with OCT imaging, dual-energy X-ray absorptiometry (DEXA) bone density scan, and a structured psychiatric interview battery.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Standing height range | 157-190 cm | Soyuz/Falcon seat envelope |
| Sitting height range | 80-99 cm | Launch/entry suit helmet clearance |
| Visual acuity (distance) | 20/20 each eye, correctable | Cabin and EVA instrument tasks |
| Hearing threshold | <= 25 dB HL (500-4000 Hz) | Comm clarity |
| Blood pressure | <= 140/90 mmHg | Cardiovascular reserve |
| Career radiation limit | 1,000-3,250 mSv (age/gender dependent) | NASA CARA |
| Disqualifying conditions | ~ 15 categories | See Space Medicine article |

## Prerequisites

- [Space Medicine](./space-medicine.md) — parent capability

## See Also

- [Space Medicine](./space-medicine.md) — parent capability
- [Microgravity Physiology](./space-medicine.microgravity-physiology.md) — what the selected crew will face
- [Crew Training](./crew-training.md) — post-selection training pipeline
