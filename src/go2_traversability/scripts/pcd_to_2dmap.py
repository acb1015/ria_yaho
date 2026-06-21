#!/usr/bin/env python3
"""Project a 3D LIO-SAM PCD map onto a 2D occupancy grid for Nav2.

Reads a binary/ascii PCD (FIELDS x y z ...), keeps points in a height band
above the estimated ground (= obstacles), and rasterizes them into an
occupancy grid saved as <out>.pgm + <out>.yaml (Nav2 map_server format).

  occupied (black, 0)   : cells with >= min_points in the obstacle band
  free     (white, 254) : cells that were observed (have points) but not occupied
  unknown  (gray, 205)  : never observed

Ground estimation (--ground-mode):
  local  (default) per-column low percentile of z. Robust to a tilted map,
                   pitch drift, ramps and multi-level. Use this for LIO-SAM maps
                   whose floor is not perfectly gravity-aligned.
  plane            single least-squares tilted plane through the low points.
                   Good when the whole map has one uniform tilt.
  global           single scalar height (legacy; assumes a flat horizontal map).

Usage:
  python3 pcd_to_2dmap.py ~/go2_maps/GlobalMap.pcd ~/go2_maps/map \
      --resolution 0.05 --min-h 0.15 --max-h 2.0
"""
import argparse
import struct
import numpy as np


def read_pcd_xyz(path):
    with open(path, 'rb') as f:
        data = f.read()
    # parse header (ascii) up to and including the DATA line
    header_end = data.find(b'DATA')
    header = data[:header_end].decode('ascii', errors='ignore')
    line_end = data.find(b'\n', header_end)
    data_type = data[header_end:line_end].decode().split()[1].strip()
    fields, sizes, types, counts = [], [], [], []
    npoints = None
    for ln in header.splitlines():
        p = ln.split()
        if not p:
            continue
        if p[0] == 'FIELDS':
            fields = p[1:]
        elif p[0] == 'SIZE':
            sizes = list(map(int, p[1:]))
        elif p[0] == 'TYPE':
            types = p[1:]
        elif p[0] == 'COUNT':
            counts = list(map(int, p[1:]))
        elif p[0] == 'POINTS':
            npoints = int(p[1])
    if not counts:
        counts = [1] * len(fields)
    if data_type == 'binary':
        buf = data[line_end + 1:]
        stride = sum(s * c for s, c in zip(sizes, counts))
        npoints = npoints or len(buf) // stride
        arr = np.frombuffer(buf[:npoints * stride], dtype=np.uint8).reshape(npoints, stride)
        out = {}
        off = 0
        for fld, s, t, c in zip(fields, sizes, types, counts):
            dt = {('F', 4): np.float32, ('F', 8): np.float64,
                  ('U', 4): np.uint32, ('I', 4): np.int32}.get((t, s), None)
            if c == 1 and dt is not None and fld in ('x', 'y', 'z'):
                out[fld] = arr[:, off:off + s].copy().view(dt).reshape(-1)
            off += s * c
        return np.stack([out['x'], out['y'], out['z']], axis=1).astype(np.float64)
    else:  # ascii
        rows = []
        for ln in data[line_end + 1:].decode(errors='ignore').splitlines():
            p = ln.split()
            if len(p) >= 3:
                rows.append([float(p[0]), float(p[1]), float(p[2])])
        return np.array(rows, dtype=np.float64)


def estimate_ground(x, y, z, mode, percentile, cell):
    """Return the estimated ground height *under each point* (same shape as z).

    'global' assumes a flat horizontal floor (one scalar); any tilt in the map
    then turns far floor/ceiling into false obstacles. 'plane' removes one
    uniform tilt. 'local' estimates the floor independently per `cell`-sized
    column, so it is robust to tilt, pitch drift, ramps and multiple levels.
    """
    if mode == 'global':
        return np.full(z.shape, np.percentile(z, percentile))
    if mode == 'plane':
        low = z < np.percentile(z, 20.0)            # ground candidates
        A = np.c_[x[low], y[low], np.ones(int(low.sum()))]
        a, b, c = np.linalg.lstsq(A, z[low], rcond=None)[0]
        return a * x + b * y + c
    # local: low percentile of z within each (cell x cell) column
    cx = np.floor((x - x.min()) / cell).astype(np.int64)
    cy = np.floor((y - y.min()) / cell).astype(np.int64)
    cid = cx * (cy.max() + 1) + cy                  # unique id per column
    uniq, inv = np.unique(cid, return_inverse=True)
    order = np.argsort(inv, kind='stable')          # group same-column points
    inv_s, z_s = inv[order], z[order]
    bounds = np.r_[0, np.flatnonzero(np.diff(inv_s)) + 1, len(inv_s)]
    ground_u = np.empty(len(uniq))
    for k in range(len(uniq)):                       # per column, robust low z
        ground_u[k] = np.percentile(z_s[bounds[k]:bounds[k + 1]], percentile)
    return ground_u[inv]                             # broadcast back to points


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pcd')
    ap.add_argument('out', help='output path prefix (writes <out>.pgm and <out>.yaml)')
    ap.add_argument('--resolution', type=float, default=0.05)
    ap.add_argument('--min-h', type=float, default=0.15, help='obstacle band min height above ground')
    ap.add_argument('--max-h', type=float, default=2.0, help='obstacle band max height above ground')
    ap.add_argument('--ground-mode', choices=['local', 'plane', 'global'],
                    default='local', help='how ground height is estimated (see top docstring)')
    ap.add_argument('--ground-cell', type=float, default=1.0,
                    help='[local mode] column size [m] for per-area ground estimate')
    ap.add_argument('--ground-percentile', type=float, default=5.0)
    ap.add_argument('--min-points', type=int, default=1, help='points per cell to call it occupied')
    ap.add_argument('--pad', type=float, default=1.0, help='border padding [m]')
    args = ap.parse_args()

    pts = read_pcd_xyz(args.pcd)
    pts = pts[np.isfinite(pts).all(axis=1)]
    x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
    ground = estimate_ground(x, y, z, args.ground_mode,
                             args.ground_percentile, args.ground_cell)
    h = z - ground
    print(f"points={len(pts)}  z:[{z.min():.2f},{z.max():.2f}]  "
          f"ground-mode={args.ground_mode} ground:[{np.min(ground):.2f},{np.max(ground):.2f}]  "
          f"height band=[{args.min_h},{args.max_h}] above ground")

    res = args.resolution
    xmin, xmax = x.min() - args.pad, x.max() + args.pad
    ymin, ymax = y.min() - args.pad, y.max() + args.pad
    W = int(np.ceil((xmax - xmin) / res))
    H = int(np.ceil((ymax - ymin) / res))
    print(f"grid {W}x{H} @ {res} m, origin=({xmin:.2f},{ymin:.2f})")

    col = ((x - xmin) / res).astype(int).clip(0, W - 1)
    row = ((y - ymin) / res).astype(int).clip(0, H - 1)

    obstacle = (h >= args.min_h) & (h <= args.max_h)
    occ = np.zeros((H, W), dtype=np.int32)
    np.add.at(occ, (row[obstacle], col[obstacle]), 1)
    observed = np.zeros((H, W), dtype=bool)
    observed[row, col] = True

    img = np.full((H, W), 205, dtype=np.uint8)      # unknown
    img[observed] = 254                              # free
    img[occ >= args.min_points] = 0                  # occupied
    img = np.flipud(img)                             # PGM origin is top-left; map origin bottom-left

    pgm = args.out + '.pgm'
    yaml = args.out + '.yaml'
    with open(pgm, 'wb') as f:
        f.write(f"P5\n{W} {H}\n255\n".encode())
        f.write(img.tobytes())
    import os
    with open(yaml, 'w') as f:
        f.write(f"image: {os.path.basename(pgm)}\n")
        f.write(f"resolution: {res}\n")
        f.write(f"origin: [{xmin:.4f}, {ymin:.4f}, 0.0]\n")
        f.write("negate: 0\noccupied_thresh: 0.65\nfree_thresh: 0.25\n")
    n_occ = int((img == 0).sum())
    n_free = int((img == 254).sum())
    print(f"wrote {pgm} ({W}x{H}), {yaml}")
    print(f"occupied cells={n_occ}  free cells={n_free}")


if __name__ == '__main__':
    main()
