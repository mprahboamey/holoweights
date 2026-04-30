# HoloWeights

**Digital AI weight representation with optical intuition.**

**Mprah-Boamey**

HoloWeights is a small sandbox. I pack model weights into a virtual volumetric tile bank on disk, poke them through memory mapping, and stare at RSS when reads stay sparse. The optical wording is metaphor. The traces are boring files and simple counters.

No photonics bench sits in this folder. I publish numbers and caveat text and move on.

The louder optics scribbles live beside this in [PHOTEX-clean](https://github.com/mprahboamey/PHOTEX-clean).

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

Model bytes land in fixed `128x128` `uint8` tiles inside a memmap file. A toy router picks which slabs to touch each step.

When I compare setups I keep one scratch objective in mind:

`NLL_proxy + lambda1*latency + lambda2*RAM + lambda3*bytes_touched`

Quality, sluggishness, footprint, bandwidth. Same whiteboard doodle each time.

---

## Documentation

`THEORY.md` holds math intuition. `METHOD.md` walks what I actually tried. `CLAIMS.md` collects narrow statements plus hard boundary text I refuse to soften. `RESULTS.md` is one workstation’s telemetry and rerun hints.

Toy code sits under `snippets/`.

---

## Scope

Layouts, probing scripts, and a bridge into a vanilla runtime stay in scope because they keep comparisons honest.

Full transformer optics on an actual bench is out of scope for this tree.

Quality numbers may remain proxy-heavy until richer logit plumbing shows up somewhere else.

---

## Quick start

Skim `METHOD.md`, skim `THEORY.md`, poke anything under `snippets/` that sparks curiosity.

---

## Frequently asked questions

### What does virtual holographic mean here?

Stacks of patterned planes you can partially address. Digitally those planes are tiles. Nobody’s crystal is secretly training through your heatsink unless you bolted hardware I do not describe here.

### How does this relate to optical computing or optical neural networks?

Same grocery aisle of metaphors, staged on SSD instead of glass. PHOTEX carries the fluffier optics essay. Holoweights is mmap nagging and RSS curiosity.

### Why mmap tiles plus sparse touches?

Untouched slabs can stay politely absent from RSS until someone asks for them. Sparse masks blunt how much of the bank you slap per step. Caveats stay in `METHOD.md` and `RESULTS.md`.

---

## Static mirror

Optional GitHub Pages folder with plain HTML echoes this readme. File-level breadcrumbs live in `STATIC_MIRROR_AND_CITATION.md`.

---

## License

MIT. See `LICENSE`.
