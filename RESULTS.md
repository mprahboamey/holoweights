# Results

Straight out of measured local runs from one workstation.

Treat every table like a campfire story somebody else ought to rerun before quoting as gospel.

---

## Storage footprint

| Metric | Value |
|--------|-------|
| Compressed model artifact | `4,372,811,712` bytes |
| Virtual tile-bank file | `4,372,054,016` bytes |
| Dense FP16 counterfactual | `14,496,047,104` bytes |
| Reduction vs dense FP16 | `~3.315x` |

---

## Memory probe

| Metric | Value |
|--------|-------|
| Sparse random tile touches | `512` |
| RSS delta during probe | `~33,677,312` bytes (`~33.7 MB`) |

---

## Runtime bridge

| Metric | Value |
|--------|-------|
| Standard engine bridge | successful |
| Measured eval TPS in CPU run | `~3.4 tok/s` |
| Best runtime knobs in run family | `num_thread=4`, `num_ctx=1024`, `num_batch=128` |

---

## Quality proxy

| Metric | Value |
|--------|-------|
| Proxy perplexity-style score | `~8.41` |
| `missing_in_topk` | `1` |
| `greedy_nll_fills` | `4` |

The layout stayed compact enough for my amusement. Sparse prodding capped RAM growth politely in this pass. Turning runtime knobs fiddled throughput upward until fans complained politely.

Whatever proxy surfaced here compares trends against itself. It never pretends to be canonical corpus perplexity with full logits.

---

## Notes to self on reruns

Tie blobs plus scripts beside every headline. Paste caveat ribbons where eyes gloss over. Separate toy-model perplexity fairy tales from bridge numbers loudly before mixing.
