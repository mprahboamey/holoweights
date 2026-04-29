#!/usr/bin/env python3
"""
Sparse mmap probe for virtual tile-bank memory behavior.
"""

from pathlib import Path
import random
import time
import numpy as np


def rss_bytes_linux():
    try:
        with open("/proc/self/status", "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if line.startswith("VmRSS:"):
                    return int(line.split()[1]) * 1024
    except OSError:
        pass
    return 0


def probe(path: Path, n_touches: int = 512):
    t0 = time.perf_counter()
    rss0 = rss_bytes_linux()
    m = np.memmap(path, dtype=np.uint8, mode="r")
    n = m.shape[0]
    s = 0.0
    for _ in range(n_touches):
        i = random.randrange(0, n)
        s += float(m[i].sum())
    rss1 = rss_bytes_linux()
    dt = time.perf_counter() - t0
    del m
    return {
        "ok": True,
        "rss_before": rss0,
        "rss_after": rss1,
        "rss_delta": max(0, rss1 - rss0),
        "n_touches": n_touches,
        "wall_s": dt,
        "checksum": s,
    }


if __name__ == "__main__":
    p = Path("vh_tiles_u8.memmap")
    if not p.is_file():
        raise SystemExit(f"missing {p}; run phase_tile_encoding.py first")
    print(probe(p))

