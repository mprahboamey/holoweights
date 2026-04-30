# Method

HoloWeights is a pipe-shaped diary. Useful when some ordinary runtime already lives on disk beside you and you want to perturb layouts without pretending you shipped silicon.

---

## Pipeline

Order stays boring on purpose. Pull bytes from whatever deployment artifact anchors the notebook, mash them through fixed `128x128` `uint8` tiles, freeze the slabs as a mmap bank, toss sparse probes so RSS tells its little story, let a standard inference bridge grunt when metrics matter, then grumble in one breath about throughput, footprint, churned bytes, jittery perplexity proxies.

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

Flatten the chosen slabs, pad cleanly, reshape into `[n_tiles, 128, 128]`, dump mmap bytes, slap a silly top-k router on token steps when experiments demand it.

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
| Quality | Documented proxy with caveats pasted nearby |

---

## Scratchpad honesty

When a digit lands anywhere public, tether environment notes, knobs, caveats, and raw blobs beside it so future me inherits context instead of fan fiction.
