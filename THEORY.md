# Theory

HoloWeights borrows optical-style intuition inside software.

This file stacks the metaphors that keep the tile algebra legible while I scribble layouts. Nobody should mistake it for a textbook chapter somebody peer reviewed yesterday.

---

## 1. Complex-field intuition in software

Each tile can be read like a phase-coded patch in some imaginary slab:

`u_out(x, y) = u_in(x, y) * exp(j * phi(x, y))`

Lens language only. Nobody here asserts that the full transformer forward pass magically became physical optics inside this repository.

---

## 2. Volumetric indexing model

A pretend tile stamp looks like `(angle, z_layer, tile_x, tile_y)` where angle plus depth imitate multiplex knobs and the tile axes chop space into squares.

Population count stays `N_tiles = N_angle * N_z * N_x * N_y`.

---

## 3. Systems objective

Keeping score with one bundle works for me:

`J = NLL_proxy + lambda1*latency + lambda2*RAM + lambda3*bytes_touched`

So quality proxies, sluggishness indicators, footprint, bandwidth pressure share one doodle rather than shouting past each other.

---

## 4. Why sparse access matters

Assume dense dumb serving slaps every tile while routed stupidity touches only `k` tiles far below `N_tiles`. Bytes per token then scale like `bytes_per_token ~ O(k * tile_size)` rather than blanketing `O(N_tiles * tile_size)`. Routed traffic dominates the intuition I cared about here.

---

## 5. Storage interpretation

Store every headline mentally against three baselines:

| Baseline | Meaning |
|----------|---------|
| Dense FP16 counterfactual | Full uncompressed weight storage |
| Compressed serving artifact | Practical deployment format |
| Virtual tile bank | Digital holographic-style layout |

In many runs, tile-bank size stays close to compressed artifact size while enabling better control over access behavior.


---

## 6. Quality recovery under pressure

Crank routing or quantization too hard and the proxy screams. Gentle recovery paths I fiddle with resemble distillation pressure, leftover residual patching, crude consensus averages. Enough knobs exist to carve a workable surface instead of pretending one golden preset exists offline.
