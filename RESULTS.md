# Results

All measurements are from a single workstation. Reproduce them in your own environment before citing.

---

## Storage footprint

| Metric | Value |
|--------|-------|
| Compressed model artifact | `4,372,811,712` bytes |
| Virtual tile-bank file | `4,372,054,016` bytes |
| Dense FP16 counterfactual | `14,496,047,104` bytes |
| Reduction vs dense FP16 | `~3.315×` |

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

The tile layout kept storage compact. Sparse access bounded RSS growth to the tiles actually touched. Throughput improved with tuned runtime parameters.

This quality metric is suitable for comparing operating points within this experimental setup. It is not equivalent to canonical corpus perplexity computed with full logit access.

---

## Reproducibility notes

Publish raw artifacts and scripts alongside any reported number. Keep caveat text visible in summaries. Do not mix toy-model perplexity estimates with bridge throughput figures.
