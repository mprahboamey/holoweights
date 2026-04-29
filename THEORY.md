# Theory

This project borrows intuition from wave optics, then applies it in fully digital form.

Each tile can be read as a phase coded patch. A conceptual field transform is:

`u_out(x, y) = u_in(x, y) * exp(j * phi(x, y))`

In this repository, that expression is a modeling lens for representation design. It is not presented as a claim that full model inference is physically optical.

A virtual volumetric address is written as:

`(angle, z_layer, tile_x, tile_y)`

This gives a software index over a tiled bank, where angle and depth are multiplexing axes and tile coordinates are spatial partitions.

Total indexed tiles follow:

`N_tiles = N_angle * N_z * N_x * N_y`

The systems objective is straightforward:

`J = NLL_proxy + lambda1*latency + lambda2*RAM + lambda3*bytes_touched`

The core intuition is that bandwidth dominates many inference paths. If dense serving touches all tiles, but routed serving touches only `k` tiles where `k` is much smaller than `N_tiles`, per token byte movement drops from an all bank term to a routed term:

`bytes_per_token ~ O(k * tile_size)` instead of `O(N_tiles * tile_size)`

Storage should be interpreted with three references in view: a dense FP16 counterfactual, the compressed serving artifact, and the virtual tile bank. In practice, the tile bank can remain close to compressed artifact size while enabling routed access behavior.

When quality drops under aggressive compression or routing, recovery mechanisms such as distillation pressure, residual correction, and consensus style averaging can move the operating point back toward useful quality.

