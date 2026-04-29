# Results (Example Measurements, Conservative Framing)

The following values come from measured local runs in one environment.
They are not universal guarantees.

## Storage footprint

- compressed model artifact (GGUF): `4,372,811,712` bytes
- virtual tile-bank file: `4,372,054,016` bytes
- dense FP16 counterfactual: `14,496,047,104` bytes
- reduction vs dense FP16: `~3.315x`

Interpretation: the virtual tile layout stays compact while enabling tiled routing behavior.

## Memory footprint probe

- sparse random tile touches: `512`
- RSS delta during probe: `~33,677,312` bytes (`~33.7 MB`)

Interpretation: sparse mmap access can keep active memory increment bounded relative to full dense load.

## Runtime bridge

- standard engine inference bridge: successful
- measured eval TPS (CPU run): `~3.4 tok/s`
- best runtime options in that run family were:
  - `num_thread=4`
  - `num_ctx=1024`
  - `num_batch=128`

## Quality proxy

- proxy perplexity-like metric (documented method): `~8.41`
- caveat fields:
  - `missing_in_topk=1`
  - `greedy_nll_fills=4`

Interpretation: this proxy can be useful for trend optimization, but it is not the same as canonical corpus perplexity with full logits.

## Goal checklist in sample run

- VH presentation of real weights: pass
- storage reduction vs FP16 dense: pass
- sparse memory story: pass
- real inference bridge: pass
- low-PPL proxy target: pass under defined caveat policy in this run

## Reproducibility notes

- publish raw JSON artifacts and scripts, not only summary values
- keep caveat text in reports
- do not mix toy-language-model PPL with real-model bridge metrics

