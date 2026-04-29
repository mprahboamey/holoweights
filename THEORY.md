# Theory (Digital Virtual Holography)

## 1) Representation as complex field intuition

Treat each tile as a phase-coded slice of a virtual optical medium:

- tile values are stored in `uint8` and decoded to phase `phi(x, y)`
- virtual field transform (conceptual):

`u_out(x, y) = u_in(x, y) * exp(j * phi(x, y))`

This is a **representation lens** in digital compute, not a claim that full model inference is physically optical in this repo.

## 2) Volumetric indexing in software

A volumetric address can be thought of as:

`(angle, z_layer, tile_x, tile_y)`

where:

- `angle` and `z_layer` represent virtual multiplexing axes
- `(tile_x, tile_y)` represent spatial partitioning

Total indexed tiles:

`N_tiles = N_angle * N_z * N_x * N_y`

## 3) Memory objective

Inference efficiency is largely bandwidth-limited, so optimize:

`J = NLL_proxy + lambda1 * latency + lambda2 * RAM + lambda3 * bytes_touched`

where:

- `NLL_proxy` captures quality trend under practical measurement constraints
- `bytes_touched` captures active tile bandwidth, not full model size

## 4) Why sparse routing matters

If full dense access touches `N_tiles` tiles/token and routed access touches `k << N_tiles`:

`bytes_per_token ~ O(k * tile_size)`

instead of:

`O(N_tiles * tile_size)`

This is the primary mechanism behind runtime and memory traffic reduction.

## 5) Storage framing

Compare three quantities:

1. dense FP16 counterfactual (`2 bytes * n_params`)
2. compressed serving artifact (for example GGUF)
3. virtual tile-bank layout

The tile-bank is often close to compressed artifact size, and both can be much smaller than dense FP16.

## 6) Noise and recovery framing

When aggressive sparsity/quantization introduces quality loss, recover via:

- distillation pressure
- residual correction channels
- consensus/averaging passes

This forms a controllable quality-speed-memory tradeoff surface.

