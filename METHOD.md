# Method

The workflow is intentionally simple.

First ingest model bytes, then repack those bytes into fixed `128x128` `uint8` tiles. Persist the result as a memory mapped tile bank. Measure sparse read behavior directly. Keep inference on a standard engine for real generation. Finally evaluate quality, throughput, memory use, and active bandwidth as one tradeoff surface.

The default data layout is:

dtype `uint8`  
tile shape `128x128`  
bytes per tile `16384`  
memmap mode read only for serving and probe runs

The minimal algorithm is:

flatten bytes, pad to tile boundary, reshape to `[n_tiles, 128, 128]`, write memmap, route token conditioned requests to top k tiles at runtime.

The main control knobs are `top_k`, quantization bits, downsample factor in tile readout, and runtime settings such as `num_thread`, `num_ctx`, and `num_batch`.

Evaluation is reported along four lines. Storage compares compressed artifact size with a dense FP16 counterfactual. Memory tracks RSS delta during sparse touches. Throughput uses measured eval windows from the serving engine. Quality uses a documented proxy with caveats when full logit paths are unavailable.

For reproducibility, always publish environment details, runtime knobs, caveats, and raw artifacts.

