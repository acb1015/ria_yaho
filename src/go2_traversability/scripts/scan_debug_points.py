#!/usr/bin/env python3
"""Visualize which 3D points become a 2D LaserScan.

Publishes:
  /scan_debug/filtered_points  all cloud points that pass the height/range filter
  /scan_debug/nearest_points   one closest point per scan angular bin
  /scan_debug/projected_scan   LaserScan computed from nearest_points
"""

import math

import numpy as np
import rclpy
from rclpy.duration import Duration
from rclpy.node import Node
from sensor_msgs.msg import LaserScan, PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
from tf2_ros import Buffer, TransformException, TransformListener


class ScanDebugPoints(Node):
    def __init__(self):
        super().__init__("scan_debug_points")

        self.declare_parameter("cloud_topic", "/ouster/points")
        self.declare_parameter("target_frame", "os_sensor")
        self.declare_parameter("min_height", -1.0)
        self.declare_parameter("max_height", 0.0)
        self.declare_parameter("angle_min", -3.14159)
        self.declare_parameter("angle_max", 3.14159)
        self.declare_parameter("angle_increment", 0.0087)
        self.declare_parameter("range_min", 0.3)
        self.declare_parameter("range_max", 10.0)
        self.declare_parameter("scan_time", 0.1)
        self.declare_parameter("publish_every_n", 1)
        self.declare_parameter("max_filtered_points", 50000)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        cloud_topic = self.get_parameter("cloud_topic").value
        self.sub = self.create_subscription(
            PointCloud2, cloud_topic, self.cloud_callback, 10)
        self.filtered_pub = self.create_publisher(
            PointCloud2, "/scan_debug/filtered_points", 10)
        self.nearest_pub = self.create_publisher(
            PointCloud2, "/scan_debug/nearest_points", 10)
        self.scan_pub = self.create_publisher(
            LaserScan, "/scan_debug/projected_scan", 10)

        self.frame_count = 0
        self.get_logger().info(
            f"Debugging {cloud_topic} -> /scan_debug/* using pointcloud_to_laserscan-style filters")

    def cloud_callback(self, msg: PointCloud2):
        self.frame_count += 1
        publish_every_n = max(1, int(self.get_parameter("publish_every_n").value))
        if self.frame_count % publish_every_n != 0:
            return

        try:
            points = pc2.read_points_numpy(
                msg, field_names=("x", "y", "z"), skip_nans=True)
        except Exception as exc:
            self.get_logger().warn(f"Failed to read point cloud: {exc}")
            return

        if points.size == 0:
            self.publish_cloud(msg.header, np.empty((0, 3), dtype=np.float32),
                               self.filtered_pub)
            self.publish_cloud(msg.header, np.empty((0, 3), dtype=np.float32),
                               self.nearest_pub)
            return

        target_frame = self.get_parameter("target_frame").value
        header = msg.header
        if target_frame and msg.header.frame_id != target_frame:
            try:
                transform = self.tf_buffer.lookup_transform(
                    target_frame, msg.header.frame_id, msg.header.stamp,
                    timeout=Duration(seconds=0.05))
                points = self.transform_points(points, transform)
                header = transform.header
                header.stamp = msg.header.stamp
            except TransformException as exc:
                self.get_logger().warn(
                    f"TF unavailable {msg.header.frame_id} -> {target_frame}: {exc}")
                return

        min_height = float(self.get_parameter("min_height").value)
        max_height = float(self.get_parameter("max_height").value)
        angle_min = float(self.get_parameter("angle_min").value)
        angle_max = float(self.get_parameter("angle_max").value)
        angle_increment = float(self.get_parameter("angle_increment").value)
        range_min = float(self.get_parameter("range_min").value)
        range_max = float(self.get_parameter("range_max").value)
        scan_time = float(self.get_parameter("scan_time").value)

        xy_range = np.hypot(points[:, 0], points[:, 1])
        angle = np.arctan2(points[:, 1], points[:, 0])
        mask = (
            (points[:, 2] >= min_height) &
            (points[:, 2] <= max_height) &
            (xy_range >= range_min) &
            (xy_range <= range_max) &
            (angle >= angle_min) &
            (angle <= angle_max)
        )

        filtered = points[mask]
        filtered_range = xy_range[mask]
        filtered_angle = angle[mask]

        max_filtered = int(self.get_parameter("max_filtered_points").value)
        if max_filtered > 0 and len(filtered) > max_filtered:
            step = int(math.ceil(len(filtered) / max_filtered))
            filtered_for_pub = filtered[::step]
        else:
            filtered_for_pub = filtered

        bin_count = int(math.ceil((angle_max - angle_min) / angle_increment))
        ranges = np.full(bin_count, np.inf, dtype=np.float32)
        nearest_points = np.full((bin_count, 3), np.nan, dtype=np.float32)

        if len(filtered):
            bins = ((filtered_angle - angle_min) / angle_increment).astype(np.int64)
            valid_bins = (bins >= 0) & (bins < bin_count)
            for point, distance, idx in zip(
                    filtered[valid_bins], filtered_range[valid_bins], bins[valid_bins]):
                if distance < ranges[idx]:
                    ranges[idx] = distance
                    nearest_points[idx] = point

        nearest_for_pub = nearest_points[np.isfinite(nearest_points[:, 0])]

        self.publish_cloud(header, filtered_for_pub, self.filtered_pub)
        self.publish_cloud(header, nearest_for_pub, self.nearest_pub)
        self.publish_scan(header, ranges, angle_min, angle_increment,
                          range_min, range_max, scan_time)

    def publish_cloud(self, header, points, publisher):
        points = np.asarray(points, dtype=np.float32)
        publisher.publish(pc2.create_cloud_xyz32(header, points.tolist()))

    def publish_scan(self, header, ranges, angle_min, angle_increment,
                     range_min, range_max, scan_time):
        msg = LaserScan()
        msg.header = header
        msg.angle_min = angle_min
        msg.angle_increment = angle_increment
        msg.angle_max = angle_min + angle_increment * (len(ranges) - 1)
        msg.scan_time = scan_time
        msg.range_min = range_min
        msg.range_max = range_max
        msg.ranges = ranges.tolist()
        self.scan_pub.publish(msg)

    @staticmethod
    def transform_points(points, transform):
        q = transform.transform.rotation
        t = transform.transform.translation
        rotation = ScanDebugPoints.quaternion_to_matrix(q.x, q.y, q.z, q.w)
        translation = np.array([t.x, t.y, t.z], dtype=np.float32)
        return points @ rotation.T + translation

    @staticmethod
    def quaternion_to_matrix(x, y, z, w):
        norm = x * x + y * y + z * z + w * w
        if norm < 1e-12:
            return np.eye(3, dtype=np.float32)
        scale = 2.0 / norm
        xx, yy, zz = x * x * scale, y * y * scale, z * z * scale
        xy, xz, yz = x * y * scale, x * z * scale, y * z * scale
        wx, wy, wz = w * x * scale, w * y * scale, w * z * scale
        return np.array([
            [1.0 - yy - zz, xy - wz, xz + wy],
            [xy + wz, 1.0 - xx - zz, yz - wx],
            [xz - wy, yz + wx, 1.0 - xx - yy],
        ], dtype=np.float32)


def main():
    rclpy.init()
    node = ScanDebugPoints()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
