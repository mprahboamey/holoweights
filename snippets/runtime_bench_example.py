#!/usr/bin/env python3
"""
Template: benchmark TPS from a local text-generation engine API.

This example assumes an endpoint returning fields similar to:
  eval_count, eval_duration (ns), response
"""

import json
import urllib.request


def bench(host: str = "127.0.0.1:11434", model: str = "mistral", n_predict: int = 48):
    body = {
        "model": model,
        "prompt": "In two sentences, explain virtual holographic AI weight representation.",
        "stream": False,
        "options": {
            "num_predict": n_predict,
            "temperature": 0.3,
            "num_thread": 4,
            "num_ctx": 1024,
            "num_batch": 128,
        },
    }
    req = urllib.request.Request(
        f"http://{host}/api/generate",
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        o = json.loads(resp.read().decode("utf-8"))
    ev = int(o.get("eval_count", 0) or 0)
    ed = float(o.get("eval_duration", 0) or 0) * 1e-9
    tps = (ev / ed) if ed > 0 and ev else 0.0
    return {
        "eval_tps": tps,
        "eval_count": ev,
        "eval_duration_s": ed,
        "response_preview": (o.get("response", "") or "")[:240],
    }


if __name__ == "__main__":
    print(bench())

