# Method

HoloWeights is a compact pipeline-shaped scratchpad—handy whenever you already have a conventional runtime and feel like probing alternate layouts beside it.

---

## Pipeline

1. Ingest model bytes from a deployment artifact
2. Repack bytes into fixed `128x128` `uint8` tiles
3. Persist tiles as a memory mapped bank
4. Probe sparse reads to measure active memory behavior
5. Run inference through a standard engine bridge
6. Evaluate quality, throughput, RAM, and active bandwidth together

---

## Data layout

| Field | Value |
|-------|-------|
| dtype | `uint8` |
| Tile shape | `128x128` |
| Bytes per tile | `16384` |
| Memmap mode | read-only for serving and probes |

---

## Minimal algorithm

1. Flatten selected weight bytes
2. Pad to tile boundary
3. Reshape to `[n_tiles, 128, 128]`
4. Write memmap file
5. Route token-time requests to top-k tiles

---

## Main control knobs

| Knob | Effect |
|------|--------|
| `top_k` | Active tiles per token |
| Quantization bits | Storage and read bandwidth pressure |
| Downsample factor | Readout cost and quality pressure |
| `num_thread`, `num_ctx`, `num_batch` | Runtime throughput behavior |

---

## Evaluation protocol

| Metric class | Measurement |
|--------------|-------------|
| Storage | Compressed artifact size vs dense FP16 counterfactual |
| Memory | RSS delta during sparse tile touches |
| Throughput | Engine TPS from measured eval windows |
| Quality | Documented proxy with explicit caveats |

---

## Scratchpad honesty

When a number lands in README or RESULTS, I try to keep env details, knobs, caveats, and raw artifacts tethered nearby so Past Me doesn’t dunk on Present Me later.

