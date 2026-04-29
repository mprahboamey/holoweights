# HoloWeights

HoloWeights is a clean, digital method for storing and serving AI weights with optical style intuition and practical systems discipline.

The project focuses on software only. It does not require photonic hardware, and it does not make grand scientific claims. The point is simple: make weight storage and access more efficient while keeping the workflow compatible with normal inference engines.

## What this project does

Model bytes are repacked into fixed `128x128` phase style tiles, persisted as a memory mapped bank, and accessed with sparse routing patterns. Inference can stay on standard serving stacks such as GGUF based runtimes.

In short, this project treats the model as a virtual volumetric medium in software, then optimizes how much of that medium is touched per token.

## Working objective

The optimization target is practical and explicit:

`NLL_proxy + lambda1*latency + lambda2*RAM + lambda3*bytes_touched`

This keeps quality, speed, memory use, and bandwidth pressure in one frame.

## What you will find here

`THEORY.md` explains the math intuition.  
`METHOD.md` explains the representation and serving flow.  
`CLAIMS.md` captures technical statements in conservative language.  
`RESULTS.md` reports measured outcomes with caveats.  
`snippets/` contains small runnable examples for tile packing, mmap probing, and runtime bench wiring.

## Example run snapshot

One measured run reported the following:

GGUF size: `4,372,811,712` bytes  
Virtual tile bank size: `4,372,054,016` bytes  
Dense FP16 counterfactual: `14,496,047,104` bytes  
Reduction versus dense FP16: about `3.315x`  
Sparse mmap probe RSS delta for 512 touches: about `33.7 MB`  
Runtime bridge throughput in CPU test environment: about `3.4 tok/s`

The full context is in `RESULTS.md`, including caveats and reproducibility notes.

## Scope

This repository demonstrates representation, memory behavior, and serving integration. It is not a claim that full transformer inference is physically optical in this codebase. Quality tracking may use a proxy unless full logit evaluation is wired in.

## Quick start

Start with `METHOD.md`, then read `THEORY.md`, then run the snippets.

## License

MIT, see `LICENSE`.

