# HoloWeights

**Digital AI weight representation with optical intuition.**

**Mprah-Boamey**

HoloWeights is a small sandbox where I pack model weights into a virtual volumetric tile bank on disk, poke them through memory mapping, and count what happens to active memory when reads stay sparse. Optical language is only the metaphor; the measurements are ordinary files and RSS checks.

It stays practical on purpose: no photonic bench in this folder, no melodramatic claims, just numbers and caveats.

Companion vibe check for the bigger optics notebook: [PHOTEX-clean](https://github.com/mprahboamey/PHOTEX-clean).

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

Treat model bytes as fixed `128x128` `uint8` tiles in a memmap file and only touch the tiles a toy router says matter for a step.

Toy objective I keep in mind when comparing tricks:

`NLL_proxy + lambda1*latency + lambda2*RAM + lambda3*bytes_touched`

So quality, sluggishness, footprint, and bandwidth stay in the same scratchpad.

---

## Documentation

| Document | Purpose |
|----------|---------|
| `THEORY.md` | Mathematical intuition and systems framing |
| `METHOD.md` | Representation and flow I actually tried |
| `CLAIMS.md` | Careful technical bullets with boundaries |
| `RESULTS.md` | One machine’s readings and how to rerun them |

Code toys live under `snippets/`.

---

## Scope

Demonstrates layouts, probing scripts, and a bridge into a conventional runtime so comparisons stay grounded.

Transformer-on-a-bench optics is explicitly out of scope for this codebase.

Quality numbers may stay proxy-ish until richer logit access shows up elsewhere.

---

## Quick start

1. Read `METHOD.md`
2. Read `THEORY.md`
3. Run the snippets that look interesting.

---

## Frequently asked questions

### What does virtual holographic mean here?

Borrowed multiplexing intuition: stacks of patterned planes you can poke through partially. Digitally it is bytes in tiles—not a literal crystal doing backprop behind your laptop.

### How does this relate to optical computing or optical neural networks?

Same metaphor grocery aisle as those topics, staged on disk instead of in glass. PHOTEX carries the fluffier optics essay; Holoweights is RAM and mmap nagging.

### Why mmap tiles plus sparse touches?

mmap lets untouched slabs stay politely absent from RSS until demanded; sparse masks trim how much of the slab you slap per step. Caveats spelled out in `METHOD.md` and `RESULTS.md`.

---

## Static mirror

There is an optional GitHub Pages folder with vanilla HTML summarizing what lives here (`docs/` plus `STATIC_MIRROR_AND_CITATION.md` for boring file-level notes).

---

## License

MIT. See `LICENSE`.
