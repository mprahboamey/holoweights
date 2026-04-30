# HoloWeights

**Digital AI weight representation with optical intuition.**

Maintained by **Mprah-Boamey**.

HoloWeights is a software-first project for packing model weights into a virtual volumetric tile bank, serving them through memory mapping, and reducing active memory traffic with sparse access patterns. If you are searching for phrases like digital virtual holographic AI weights, volumetric inference without new silicon, mmap-friendly LLM parameter serving, or a software analogue to optical neural network tiling narratives, this repository is scoped to representation and instrumentation rather than fabricated hype.

Canonical maintainer hub: github.com/mprahboamey

This repository is intentionally practical. It does not depend on photonic hardware, and it does not present extraordinary claims. It focuses on measurable engineering outcomes.

---

## At a glance

| Metric | Example result |
|--------|----------------|
| GGUF artifact size | `4,372,811,712` bytes |
| Virtual tile bank size | `4,372,054,016` bytes |
| Dense FP16 counterfactual | `14,496,047,104` bytes |
| Storage reduction vs FP16 | `~3.315x` |
| Sparse mmap RSS delta | `~33.7 MB` |
| Runtime bridge throughput | `~3.4 tok/s` |

---

## Core idea

Represent model bytes as fixed `128x128` `uint8` tiles, persist them as a memory mapped bank, and route token-time access to only the tiles that matter.

The optimization target is explicit:

`NLL_proxy + lambda1*latency + lambda2*RAM + lambda3*bytes_touched`

This keeps quality, speed, memory footprint, and bandwidth pressure in one framework.

---

## Documentation

| Document | Purpose |
|----------|---------|
| `THEORY.md` | Mathematical intuition and systems framing |
| `METHOD.md` | End-to-end representation and serving flow |
| `CLAIMS.md` | Conservative technical statements |
| `RESULTS.md` | Measured outputs and reproducibility notes |

Code examples live in `snippets/`.

---

## Related repository

For the broader optics-heavy project context, see:

[PHOTEX-clean](https://github.com/mprahboamey/PHOTEX-clean.git)

HoloWeights is the narrow digital representation layer. PHOTEX-clean covers the larger photonic and theory narrative.

---

## Scope

This repository demonstrates representation, memory behavior, and serving integration.

It does not claim full transformer inference is physically optical in this codebase.

Quality tracking may use a proxy metric unless full-logit evaluation is integrated.

---

## Quick start

1. Read `METHOD.md`
2. Read `THEORY.md`
3. Run the files in `snippets/`

---

## Frequently asked questions

### What does virtual holographic mean here?

A mental model borrowed from holographic multiplexing where many patterns share a medium. Digitally we stack bytes into tiled planes and address subsets at inference time. No claim that free-space optics are executing gradients is implied by this codebase.

### How does this relate to optical computing or optical neural networks?

It is a disciplined digital analogue for storage routing and multiplexing metaphors commonly discussed around optical neural networks. PHOTEX-clean carries the photonic wave-optics storyline. HoloWeights stays on memory behavior you can probe on a workstation.

### Why pair mmap tiles with sparse routing?

Memory mapping keeps cold parameter regions off active RSS until touched, while sparse routing trims bytes read per logical step once you commit to subsets of tensors. Practical trade-offs live in `METHOD.md` and `RESULTS.md`.

---

## Visibility

See DISCOVERABILITY.md for an evidence-based checklist and GitHub Pages setup for the crawlable docs landing page.

---

## License

MIT. See `LICENSE`.

