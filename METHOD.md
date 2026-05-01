# Method

HoloWeights is an experimental pipeline for studying weight layout, memory access patterns, and inference efficiency in software. It uses a standard runtime as a bridge for throughput and quality measurements, without requiring photonic hardware.

---

## Pipeline

1. Extract weights from a deployment artifact (GGUF or equivalent)
2. Pack into fixed `128×128` `uint8` tiles
3. Write tiles to a memory-mapped file
4. Run sparse probes to measure RSS delta under partial access
5. Bridge to a standard inference engine for throughput and quality measurements
6. Record throughput, memory footprint, bytes touched, and quality proxy

---

## Data layout

| Field | Value |
|-------|-------|
| dtype | `uint8` |
| Tile shape | `128×128` |
| Bytes per tile | `16,384` |
| Memmap mode | read-only for serving and probes |

---

## Core algorithm

Flatten weight tensors, pad to tile boundaries, reshape into `[n_tiles, 128, 128]`, serialize to a memory-mapped file. A top-k router selects active tiles per inference step during routing experiments.

---

## Control knobs

| Knob | Effect |
|------|--------|
| `top_k` | Number of active tiles per token |
| Quantization bits | Storage size and read bandwidth |
| Downsample factor | Readout cost and quality tradeoff |
| `num_thread`, `num_ctx`, `num_batch` | Runtime throughput behavior |

---

## Evaluation protocol

| Metric class | Measurement |
|--------------|-------------|
| Storage | Compressed artifact size vs dense FP16 counterfactual |
| Memory | RSS delta during sparse tile access |
| Throughput | Engine TPS from timed eval runs |
| Quality | Proxy metric with documented caveats |

---

## Reproducibility

Every number here is paired with the environment spec, runtime knobs, and raw output. Context that only exists at measurement time is not useful to anyone trying to reproduce the work.
