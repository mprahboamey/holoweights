# Method

## Pipeline

1. **Ingest** model weights (for example GGUF bytes).
2. **Pack** bytes into fixed tiles (`128x128`, `uint8`).
3. **Persist** as memory-mapped tile-bank file.
4. **Probe** sparse random reads to quantify RAM behavior.
5. **Bridge** to standard inference engine for real generation.
6. **Evaluate** quality-throughput-memory tradeoffs with a unified objective.

## Data layout

- dtype: `uint8`
- tile shape: `128x128`
- bytes per tile: `16384`
- memmap mode: read-only for serving/probing

## Minimal algorithm

1. Flatten selected weight bytes.
2. Pad to tile boundary.
3. Reshape to `[n_tiles, 128, 128]`.
4. Save to `.memmap`.
5. At runtime, route token-conditioned requests to top-k tiles.

## Practical knobs

- `top_k` active tiles/token
- quantization bits (2/4/8 style experiments)
- downsample factor in tile readout path
- runtime serving knobs (`num_thread`, `num_ctx`, `num_batch`)

## Evaluation protocol

- **Storage**: compressed artifact bytes vs FP16 counterfactual
- **RAM**: RSS delta during sparse tile touches
- **Throughput**: engine TPS from measured eval window
- **Quality proxy**: constrained NLL/PPL-like proxy with explicit caveats

## Reporting requirements

Always publish:

- exact environment (CPU/GPU, engine version)
- exact knobs
- exact caveats (especially if proxy quality metric is used)
- all raw metrics and scripts

