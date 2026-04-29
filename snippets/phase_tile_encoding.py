#!/usr/bin/env python3
"""
Minimal phase-tile packing example.

Input: arbitrary bytes
Output: uint8 memmap with shape [n_tiles, 128, 128]
"""

from pathlib import Path
import numpy as np


def pack_bytes_to_tiles(raw: bytes, tile_h: int = 128, tile_w: int = 128):
    arr = np.frombuffer(raw, dtype=np.uint8)
    tile_bytes = tile_h * tile_w
    n_tiles = int(np.ceil(len(arr) / tile_bytes))
    pad = n_tiles * tile_bytes - len(arr)
    if pad > 0:
        arr = np.pad(arr, (0, pad), mode="constant")
    return arr.reshape(n_tiles, tile_h, tile_w)


def write_memmap(tiles: np.ndarray, out_path: Path):
    mm = np.memmap(out_path, mode="w+", dtype=np.uint8, shape=tiles.shape)
    mm[:] = tiles[:]
    mm.flush()
    del mm


if __name__ == "__main__":
    demo = bytes(range(256)) * 1000
    tiles = pack_bytes_to_tiles(demo)
    out = Path("vh_tiles_u8.memmap")
    write_memmap(tiles, out)
    print(f"wrote {out} shape={tiles.shape} bytes={out.stat().st_size}")

