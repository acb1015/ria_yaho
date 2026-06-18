#!/usr/bin/env python3
"""Quantify elevation_map_raw quality: coverage, height range, tilt, roughness."""
import time
import numpy as np
import rclpy
from rclpy.node import Node
from grid_map_msgs.msg import GridMap


def grid_to_2d(layer_msg):
    dims = layer_msg.layout.dim
    if len(dims) >= 2:
        n_col, n_row = dims[0].size, dims[1].size
    else:
        n = int(np.sqrt(len(layer_msg.data)))
        n_col = n_row = n
    a = np.array(layer_msg.data, dtype=np.float32)
    # grid_map stores column-major
    return a.reshape((n_col, n_row)).T  # -> (rows, cols)


class C(Node):
    def __init__(self):
        super().__init__('elev_check')
        self.create_subscription(GridMap, '/elevation_mapping_node/elevation_map_raw', self.cb, 1)
        self.done = False

    def cb(self, m):
        res = m.info.resolution
        print(f"grid: {m.info.length_x}x{m.info.length_y} m @ {res} m, frame={m.info.header.frame_id}")
        for layer in ['elevation', 'traversability', 'variance']:
            if layer not in m.layers:
                continue
            idx = list(m.layers).index(layer)
            g = grid_to_2d(m.data[idx])
            fin = np.isfinite(g)
            n = int(fin.sum())
            if n == 0:
                print(f"  {layer:14s}: ALL NaN"); continue
            v = g[fin]
            line = (f"  {layer:14s}: cov={100*n/g.size:4.1f}%  "
                    f"min={np.min(v):+.2f} max={np.max(v):+.2f} mean={np.mean(v):+.2f} std={np.std(v):.3f}")
            print(line)
            if layer == 'elevation' and n > 50:
                rows, cols = np.where(fin)
                x = cols * res; y = rows * res
                A = np.c_[x, y, np.ones(n)]
                coef, *_ = np.linalg.lstsq(A, v, rcond=None)
                a, b, _ = coef
                tilt_deg = np.degrees(np.arctan(np.hypot(a, b)))
                resid = v - A @ coef
                print(f"  -> ground-plane fit: tilt={tilt_deg:.1f} deg, "
                      f"roughness(resid std)={np.std(resid):.3f} m")
        self.done = True


rclpy.init()
c = C()
t0 = time.time()
while rclpy.ok() and not c.done and time.time() - t0 < 12:
    rclpy.spin_once(c, timeout_sec=0.5)
print("RESULT:", "ok" if c.done else "NO MESSAGE")
rclpy.shutdown()
