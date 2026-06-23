#!/usr/bin/env python3
"""Request a Nav2 ComputePathToPose action from explicit start/goal map poses."""

import argparse
import math

import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import ComputePathToPose
from rclpy.action import ActionClient


def yaw_to_quaternion(yaw):
    half = yaw * 0.5
    return {
        "z": math.sin(half),
        "w": math.cos(half),
    }


def make_pose(x, y, yaw, stamp):
    pose = PoseStamped()
    pose.header.frame_id = "map"
    pose.header.stamp = stamp
    pose.pose.position.x = x
    pose.pose.position.y = y
    q = yaw_to_quaternion(yaw)
    pose.pose.orientation.z = q["z"]
    pose.pose.orientation.w = q["w"]
    return pose


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute a Nav2 path using map-frame start and goal poses.")
    parser.add_argument("--start-x", type=float, required=True)
    parser.add_argument("--start-y", type=float, required=True)
    parser.add_argument("--start-yaw", type=float, default=0.0)
    parser.add_argument("--goal-x", type=float, required=True)
    parser.add_argument("--goal-y", type=float, required=True)
    parser.add_argument("--goal-yaw", type=float, default=0.0)
    parser.add_argument("--planner-id", default="GridBased")
    return parser.parse_args()


def main():
    args = parse_args()

    rclpy.init()
    node = rclpy.create_node("compute_nav2_path")
    client = ActionClient(node, ComputePathToPose, "compute_path_to_pose")

    if not client.wait_for_server(timeout_sec=10.0):
        node.get_logger().error("compute_path_to_pose action server not available")
        rclpy.shutdown()
        return 1

    stamp = node.get_clock().now().to_msg()
    goal_msg = ComputePathToPose.Goal()
    goal_msg.start = make_pose(
        args.start_x, args.start_y, args.start_yaw, stamp)
    goal_msg.goal = make_pose(args.goal_x, args.goal_y, args.goal_yaw, stamp)
    goal_msg.use_start = True
    goal_msg.planner_id = args.planner_id

    future = client.send_goal_async(goal_msg)
    rclpy.spin_until_future_complete(node, future)
    goal_handle = future.result()
    if not goal_handle.accepted:
        node.get_logger().error("path request rejected")
        rclpy.shutdown()
        return 1

    result_future = goal_handle.get_result_async()
    rclpy.spin_until_future_complete(node, result_future)
    result = result_future.result().result
    path = result.path

    node.get_logger().info(f"path poses: {len(path.poses)}")
    if path.poses:
        first = path.poses[0].pose.position
        last = path.poses[-1].pose.position
        node.get_logger().info(
            f"first=({first.x:.3f}, {first.y:.3f}) last=({last.x:.3f}, {last.y:.3f})")

    rclpy.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
