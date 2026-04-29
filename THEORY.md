# Theory

HoloWeights applies optical-style intuition inside a purely digital system.

The purpose of this document is to define the mathematical framing behind the representation and serving choices.

---

## 1. Complex-field intuition in software

Each tile can be interpreted as a phase-coded patch in a virtual medium:

`u_out(x, y) = u_in(x, y) * exp(j * phi(x, y))`

In this repository, this is a representation lens, not a claim that full model inference is physically optical.

---

## 2. Volumetric indexing model

A virtual tile address is:

`(angle, z_layer, tile_x, tile_y)`

where angle and depth are multiplexing axes, and tile coordinates are spatial partitions.

Total indexed tiles:

`N_tiles = N_angle * N_z * N_x * N_y`

---

## 3. Systems objective

The working objective is:

`J = NLL_proxy + lambda1*latency + lambda2*RAM + lambda3*bytes_touched`

This keeps the optimization grounded in quality, speed, resident memory, and active bandwidth.

---

## 4. Why sparse access matters

If dense serving touches all tiles, and routed serving touches only `k` tiles where `k` is much smaller than `N_tiles`, byte movement per token follows:

`bytes_per_token ~ O(k * tile_size)`  
instead of  
`O(N_tiles * tile_size)`

That reduction in active traffic is the primary systems benefit of routed tile access.

---

## 5. Storage interpretation

Storage should always be read against three baselines:

| Baseline | Meaning |
|----------|---------|
| Dense FP16 counterfactual | Full uncompressed weight storage |
| Compressed serving artifact | Practical deployment format |
| Virtual tile bank | Digital holographic-style layout |

In many runs, tile-bank size stays close to compressed artifact size while enabling better control over access behavior.

---

## 6. Quality recovery under pressure

Aggressive routing and compression can reduce quality. Recovery can be pursued through:

1. Distillation pressure
2. Residual correction
3. Consensus-style averaging

This forms a controllable quality-speed-memory operating surface.

