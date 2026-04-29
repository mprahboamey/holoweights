# HoloWeights (Digital-Only)

A practical, digital representation of AI weights inspired by optical/volumetric intuition.

This project is about a **software representation** (not hardware optics):

- model bytes are repacked into `128x128` phase-like tiles
- tiles are served from a memory-mapped "volumetric" bank
- sparse access patterns reduce active memory traffic
- inference remains on standard engines (for example, GGUF + Ollama)

This is **not** a physical photonic implementation and does not claim a new law of physics.

## Why this exists

Large-model inference is often memory-bandwidth bound. A representation that:

1. keeps storage compact,
2. keeps RAM residency low via mmap + sparse reads,
3. preserves quality in practical operating regions,
4. and stays compatible with standard inference stacks,

can be useful as an engineering approach.

## Core idea (conservative version)

Represent dense weight bytes in a virtual phase tile-bank:

- logical model weights -> byte stream
- byte stream -> fixed-size tile packing (`uint8`, `128x128`)
- tile-bank -> mmap-backed file
- retrieval -> routed sparse tile reads at inference-time

A useful objective is:

`minimize NLL_proxy + lambda1*latency + lambda2*RAM + lambda3*bytes_touched`

subject to quality and compatibility constraints.

## What is included

- `THEORY.md`: equations + intuition (ASM-inspired, complex fields, interference framing)
- `METHOD.md`: concrete representation and serving flow
- `CLAIMS.md`: technical claims (open-source articulation, not legal advice)
- `RESULTS.md`: measured reductions and caveats
- `snippets/`: runnable Python snippets for:
  - tile packing
  - mmap sparse probe
  - runtime bench call pattern

## Example measured numbers

From one measured run:

- GGUF size: `4,372,811,712` bytes
- virtual tile-bank: `4,372,054,016` bytes
- dense FP16 counterfactual: `14,496,047,104` bytes
- reduction vs FP16: `~3.315x`
- mmap sparse probe RSS delta (512 random tiles): `~33.7 MB`
- runtime bridge TPS (CPU test env): `~3.4 tok/s`

See `RESULTS.md` for details and caveats. Reproduce before making strong claims.

## Scope and caveats (important)

- This repository demonstrates a representation, memory behavior, and serving bridge.
- It does **not** claim full end-to-end transformer forward pass through physical optics.
- "Low perplexity" here may be a proxy unless full-logit evaluation is used.
- Treat this as an open engineering method, not legal/scientific proof of novelty.

## Quick start

1. Read `METHOD.md` and `THEORY.md`.
2. Run snippets in `snippets/`.
3. Compare your own model with the same report schema.

## License

Apache-2.0 (see `LICENSE`).

