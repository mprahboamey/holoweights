# Results

These numbers come from measured local runs in one environment. They should be treated as reproducible examples, not universal guarantees.

Storage footprint in the sample run:

compressed model artifact `4,372,811,712` bytes  
virtual tile bank file `4,372,054,016` bytes  
dense FP16 counterfactual `14,496,047,104` bytes  
reduction versus dense FP16 about `3.315x`

Memory probe in the sample run:

sparse random tile touches `512`  
RSS delta during probe about `33,677,312` bytes, roughly `33.7 MB`

Runtime bridge in the sample run:

standard engine inference bridge completed successfully  
measured eval TPS in CPU run about `3.4 tok/s`  
best runtime options in that run family were `num_thread=4`, `num_ctx=1024`, and `num_batch=128`

Quality proxy in the sample run:

documented perplexity style proxy about `8.41`  
caveat fields `missing_in_topk=1` and `greedy_nll_fills=4`

Interpretation:

the representation can stay compact, sparse access can keep active memory growth bounded, and throughput can improve under tuned runtime settings. Quality tracking here is useful for trend optimization, but it is not equivalent to canonical corpus perplexity with full logit access.

Reproducibility expectations:

publish raw artifacts and scripts, keep caveat text visible, and avoid mixing toy language model perplexity with real bridge metrics.

