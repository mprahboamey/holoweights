# Results

These values come from measured local runs in one environment.

Treat them as reproducible examples, not universal guarantees.

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

Interpretation:

The representation stays compact, sparse access keeps active memory growth bounded, and throughput improves under tuned runtime settings.

The quality metric here is useful for trend optimization, but it is not identical to canonical corpus perplexity with full logit access.

---

## Notes to self on reruns

1. Tie raw blobs and scripts to every table above.
2. Leave caveat text clingy—it trips people less.
3. Don’t braid toy-model perplexity with bridge numbers without yelling about it first.

