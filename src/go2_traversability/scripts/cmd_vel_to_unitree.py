#!/usr/bin/env python3
"""Bridge Nav2 /cmd_vel (geometry_msgs/Twist) -> Unitree Go2 sport "Move".

Publishes unitree_api/msg/Request (api_id 1008 = Move, parameter
{"x":vx,"y":vy,"z":vyaw}) on /api/sport/request, which makes the Go2 walk.

⚠️ DDS: the Go2 control bus uses CycloneDDS on eno1. This node (and whatever
publishes /cmd_vel) must run in that same DDS env, e.g.:
    source ~/go2_ws/src/unitree_ros2/setup.sh   # RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
⚠️ SAFETY: the robot physically walks. Keep speeds low, area clear, e-stop ready,
and make sure the Go2 is standing in sport mode first.

Params: max_vx (0.6), max_vy (0.4), max_vyaw (0.8), timeout (0.5 s -> stop).
"""
import json
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from unitree_api.msg import Request

ROBOT_SPORT_API_ID_MOVE = 1008


class CmdVelToUnitree(Node):
    def __init__(self):
        super().__init__('cmd_vel_to_unitree')
        self.max_vx = float(self.declare_parameter('max_vx', 0.6).value)
        self.max_vy = float(self.declare_parameter('max_vy', 0.4).value)
        self.max_vyaw = float(self.declare_parameter('max_vyaw', 0.8).value)
        self.timeout = float(self.declare_parameter('timeout', 0.5).value)

        self.pub = self.create_publisher(Request, '/api/sport/request', 10)
        self.create_subscription(Twist, '/cmd_vel', self.on_cmd, 10)
        self.last = self.get_clock().now()
        self.create_timer(0.1, self.watchdog)
        self.get_logger().info(
            f"cmd_vel -> Go2 Move bridge ready (limits vx={self.max_vx} "
            f"vy={self.max_vy} vyaw={self.max_vyaw}).")

    @staticmethod
    def _clamp(v, m):
        return max(-m, min(m, float(v)))

    def _move(self, vx, vy, vyaw):
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_MOVE
        req.parameter = json.dumps({"x": vx, "y": vy, "z": vyaw})
        self.pub.publish(req)

    def on_cmd(self, t):
        self._move(self._clamp(t.linear.x, self.max_vx),
                   self._clamp(t.linear.y, self.max_vy),
                   self._clamp(t.angular.z, self.max_vyaw))
        self.last = self.get_clock().now()

    def watchdog(self):
        # No fresh /cmd_vel -> command a stop so the robot never runs away.
        if (self.get_clock().now() - self.last).nanoseconds * 1e-9 > self.timeout:
            self._move(0.0, 0.0, 0.0)


def main():
    rclpy.init()
    try:
        rclpy.spin(CmdVelToUnitree())
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
