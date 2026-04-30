# Technical statements

Things I still believe after rereading the measurement notes against the actual traces.

Nothing here is legal advice. Nothing here is pretending to be a patent draft.

---

## Statement 1

AI weights can be represented as a tiled, phase-style volumetric address space in software using deterministic `uint8` packing.

## Statement 2

A memory mapped tile bank with routed sparse reads can reduce active RAM pressure and active memory traffic compared with dense full-bank access.

## Statement 3

This representation can sit next to ordinary inference stacks for experiments without ripping out whichever runtime you already use.

## Statement 4

A unified objective over quality proxy, latency, RAM, and bytes touched gives a principled knob for comparing operating points:

`NLL_proxy + lambda1*latency + lambda2*RAM + lambda3*bytes_touched`

## Statement 5

When aggressive efficiency settings reduce quality, recovery levers such as distillation, residual correction, and consensus passes can restore useful quality regions while retaining part of the efficiency gain.

---

## Boundary conditions

This repository does not claim full transformer inference is physically optical in this codebase.

This repository does not claim canonical benchmark perplexity without full-logit evaluation.

This repository does not claim universal superiority across all models and hardware.
