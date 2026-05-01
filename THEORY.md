# Theory

HoloWeights uses optical storage geometry as a conceptual model for organizing software weight representations. The constructs below describe the tile indexing model and the systems objective used for comparing operating points.

This document covers the software model only. Full optical physics derivations are in [PHOTEX-clean](https://github.com/mprahboamey/PHOTEX-clean).

---

## 1. Complex-field representation in software

Each tile can be interpreted as a phase-coded patch within a virtual volumetric slab:

`u_out(x, y) = u_in(x, y) · exp(j · φ(x, y))`

This is a software abstraction. No physical optics are involved in this repository.

---

## 2. Volumetric indexing model

Each tile is addressed by a four-dimensional index: `(angle, z_layer, tile_x, tile_y)`, where the angle and depth coordinates model the multiplexing dimensions of holographic storage, and the spatial axes partition the weight space into fixed tiles.

Total tile count: `N_tiles = N_angle × N_z × N_x × N_y`

---

## 3. Systems objective

Operating points are compared using a combined objective:

`J = NLL_proxy + λ₁·latency + λ₂·RAM + λ₃·bytes_touched`

This bundles quality, latency, memory footprint, and bandwidth into a single surface rather than optimizing each in isolation.

---

## 4. Why sparse access reduces bandwidth

Dense serving loads every tile regardless of relevance. Sparse routing loads only `k` tiles per token step, where `k ≪ N_tiles`. Bandwidth per token scales as:

`bytes_per_token ~ O(k · tile_size)` vs. `O(N_tiles · tile_size)`

Sparse routing is the primary mechanism for bandwidth reduction in this design.

---

## 5. Storage baselines

| Baseline | Description |
|----------|-------------|
| Dense FP16 counterfactual | Full uncompressed weight storage |
| Compressed serving artifact | Practical deployment format (e.g., GGUF) |
| Virtual tile bank | Tiled layout using volumetric addressing |

In most runs, the tile bank size is comparable to the compressed artifact while providing more granular access control.

---

## 6. Quality recovery under compression pressure

Aggressive routing or quantization reduces quality proxy scores. Recovery approaches include distillation, residual correction, and ensemble averaging. These provide a tunable tradeoff between efficiency and quality rather than a single fixed operating point.
