"""Start only the Nav2 pieces needed to compute a path on a static map.

Example:
  ros2 launch go2_traversability nav2_planner_only.launch.py
  ros2 launch go2_traversability nav2_planner_only.launch.py map:=$HOME/go2_maps/map_nav.yaml
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    go2_share = get_package_share_directory("go2_traversability")
    params_file = os.path.join(
        go2_share, "config", "nav2_planner_only_params.yaml")

    map_yaml = LaunchConfiguration("map")
    use_rviz = LaunchConfiguration("rviz")

    return LaunchDescription([
        DeclareLaunchArgument(
            "map",
            default_value=os.path.expanduser("~/go2_maps/map_nav.yaml"),
            description="2D occupancy map yaml for Nav2 planning",
        ),
        DeclareLaunchArgument(
            "rviz",
            default_value="true",
            description="Start RViz with the Nav2 default view",
        ),
        Node(
            package="nav2_map_server",
            executable="map_server",
            name="map_server",
            output="screen",
            parameters=[params_file, {"yaml_filename": map_yaml}],
        ),
        Node(
            package="nav2_planner",
            executable="planner_server",
            name="planner_server",
            output="screen",
            parameters=[params_file],
        ),
        Node(
            package="nav2_lifecycle_manager",
            executable="lifecycle_manager",
            name="lifecycle_manager_planner",
            output="screen",
            parameters=[params_file],
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
            condition=IfCondition(use_rviz),
        ),
    ])
