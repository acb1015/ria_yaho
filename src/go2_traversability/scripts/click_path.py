#!/usr/bin/env python3
"""Click a START and a GOAL on the map in RViz, draw the planned path.

  - "2D Pose Estimate" tool (-> /initialpose)  sets the START
  - "Nav2 Goal" tool      (-> /goal_pose)       sets the GOAL and triggers planning

Calls Nav2's /compute_path_to_pose with use_start=True (so it plans between the
two clicked points, NO robot / NO localization needed) and republishes the
resulting path on /computed_path for an RViz Path display.
"""
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from nav_msgs.msg import Path
from nav2_msgs.action import ComputePathToPose


class ClickPath(Node):
    def __init__(self):
        super().__init__('click_path')
        self.start = None
        self.create_subscription(PoseWithCovarianceStamped, '/initialpose', self.on_start, 10)
        self.create_subscription(PoseStamped, '/goal_pose', self.on_goal, 10)
        self.pub = self.create_publisher(Path, '/computed_path', 1)
        self.client = ActionClient(self, ComputePathToPose, 'compute_path_to_pose')
        self.get_logger().info(
            "READY: click '2D Pose Estimate' = START, then 'Nav2 Goal' = GOAL.")

    def on_start(self, msg):
        self.start = PoseStamped()
        self.start.header = msg.header
        self.start.pose = msg.pose.pose
        p = self.start.pose.position
        self.get_logger().info(f"START set: ({p.x:.2f}, {p.y:.2f}) - now click 'Nav2 Goal'.")

    def on_goal(self, goal):
        if self.start is None:
            self.get_logger().warn("Set START first with '2D Pose Estimate'.")
            return
        if not self.client.wait_for_server(timeout_sec=3.0):
            self.get_logger().error("/compute_path_to_pose action not available.")
            return
        g = ComputePathToPose.Goal()
        g.start = self.start
        g.goal = goal
        g.use_start = True
        g.planner_id = 'GridBased'
        p = goal.pose.position
        self.get_logger().info(f"GOAL: ({p.x:.2f}, {p.y:.2f}) - planning...")
        self.client.send_goal_async(g).add_done_callback(self._accepted)

    def _accepted(self, fut):
        gh = fut.result()
        if not gh.accepted:
            self.get_logger().error("path request rejected.")
            return
        gh.get_result_async().add_done_callback(self._result)

    def _result(self, fut):
        path = fut.result().result.path
        n = len(path.poses)
        if n:
            path.header.frame_id = 'map'
            self.pub.publish(path)
            self.get_logger().info(f"PATH FOUND: {n} poses -> drawn on /computed_path")
        else:
            self.get_logger().warn(
                "NO PATH (start/goal on an obstacle, or no free route between them).")


def main():
    rclpy.init()
    try:
        rclpy.spin(ClickPath())
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
