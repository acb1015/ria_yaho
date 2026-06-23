#!/usr/bin/env python3
"""Periodically call LIO-SAM's /lio_sam/save_map service so the map is always
persisted to disk. Robust to kill -9 (the last periodic save survives).

WARNING: the save_map service does `rm -r $HOME/<destination>` before each save,
so 'destination' MUST be a dedicated folder name (default ~/go2_maps/).

Params:
  interval    (float, s)  how often to save                 [default 30.0]
  destination (str)       $HOME-relative folder, starts '/'  [default /go2_maps/]
  resolution  (float)     voxel downsample (0 = full res)    [default 0.0]
"""
import rclpy
from rclpy.node import Node
from lio_sam_go2.srv import SaveMap


class AutoSaver(Node):
    def __init__(self):
        super().__init__('lio_sam_auto_saver')
        self.interval = float(self.declare_parameter('interval', 30.0).value)
        self.destination = str(self.declare_parameter('destination', '/go2_maps/').value)
        self.resolution = float(self.declare_parameter('resolution', 0.0).value)
        self.cli = self.create_client(SaveMap, '/lio_sam/save_map')
        self.n = 0
        self.get_logger().info(
            f"Auto-save every {self.interval}s -> $HOME{self.destination} "
            f"(resolution={self.resolution})")
        self.create_timer(self.interval, self.save)

    def save(self):
        if not self.cli.service_is_ready():
            self.get_logger().warn('/lio_sam/save_map not available yet; skipping')
            return
        req = SaveMap.Request()
        req.resolution = self.resolution
        req.destination = self.destination
        future = self.cli.call_async(req)
        self.n += 1
        m = self.n
        future.add_done_callback(
            lambda f: self.get_logger().info(
                f"auto-save #{m}: success={getattr(f.result(), 'success', '?')}"))


def main():
    rclpy.init()
    node = AutoSaver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
