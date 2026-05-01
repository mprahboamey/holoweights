# HoloWeights

**Digital AI weight representation using volumetric tile addressing.**

**Mprah-Boamey**

HoloWeights packs model weights into a memory-mapped tile structure organized after holographic storage geometry. The question it is designed to answer: does sparse, volumetric-style access actually change the memory pressure story? No photonics required.

All measurements are from one workstation. The optical framing is a conceptual model, not a physical claim. These are single-environment results.

For the full optical simulation and benchmark work, see [PHOTEX-clean](https://github.com/mprahboamey/PHOTEX-clean).

---

## At a glance

| Metric | Result |
|--------|--------|
| GGUF artifact size | `4,372,811,712` bytes |
| Virtual tile bank size | `4,372,054,016` bytes |
| Dense FP16 counterfactual | `14,496,047,104` bytes |
| Storage reduction vs FP16 | `~3.315×` |
| Sparse mmap RSS delta | `~33.7 MB` |
| Runtime bridge throughput | `~3.4 tok/s` |

---

## Core idea

Model weights are packed into fixed `128×128` `uint8` tiles inside a memory-mapped file. A router selects which tiles to load per inference step.

The optimization objective used for comparisons:

`NLL_proxy + λ₁·latency + λ₂·RAM + λ₃·bytes_touched`

This combines quality, latency, memory footprint, and bandwidth into a single surface for comparing operating points.

---

## Documentation

- `THEORY.md`: mathematical model and tile algebra
- `METHOD.md`: implementation details
- `CLAIMS.md`: precise technical statements with boundary conditions
- `RESULTS.md`: measured results from one environment, with reproduction notes

Source code lives under `snippets/`.

---

## Scope

**In scope:** tile layout design, sparse probing scripts, and a bridge into a standard inference runtime.

**Out of scope:** full transformer inference on photonic hardware.

Quality metrics remain proxy-based until richer logit evaluation is available.

---

## Quick start

Read `METHOD.md` for implementation context, `THEORY.md` for the mathematical model, then explore `snippets/`.

---

## FAQ

**What does "virtual holographic" mean here?**
Weights are organized into a partially-addressable tile structure modeled after volumetric holographic addressing: stacked planes accessed by position and angle index. The implementation is software-only; no physical optics are involved.

**How does this relate to optical computing?**
The addressing model borrows from holographic storage geometry. The actual computation runs on standard hardware. [PHOTEX-clean](https://github.com/mprahboamey/PHOTEX-clean) covers the full optical simulation work.

**Why memory-mapped tiles with sparse access?**
Tiles that are not accessed remain absent from RSS until requested. Sparse routing limits how much of the bank is loaded per step, reducing active memory pressure. Caveats are documented in `METHOD.md` and `RESULTS.md`.

---

## Static mirror

A GitHub Pages mirror with plain HTML is available. File references are in `STATIC_MIRROR_AND_CITATION.md`.

---

## License

MIT. See `LICENSE`.
