"""Click START + GOAL on a 2D map and draw the planned path between them.

No robot, no sensors, no AMCL: just map_server + planner_server + the click_path
helper. In RViz use:
  - "2D Pose Estimate"  -> START
  - "Nav2 Goal"         -> GOAL  (path is drawn on /computed_path)

  ros2 launch go2_traversability plan_on_map.launch.py
  ros2 launch go2_traversability plan_on_map.launch.py map:=$HOME/go2_maps/map.yaml
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    go2_share = get_package_share_directory('go2_traversability')
    params = os.path.join(go2_share, 'config', 'nav2_params.yaml')
    rviz_cfg = os.path.join(go2_share, 'config', 'plan_on_map.rviz')
    map_yaml = LaunchConfiguration('map')

    return LaunchDescription([
        DeclareLaunchArgument(
            'map', default_value=os.path.expanduser('~/go2_maps/map_nav.yaml'),
            description='2D occupancy map (yaml) to plan on'),

        # The global costmap needs a robot pose; we only plan between clicked
        # points, so pin the robot at the map origin.
        Node(package='tf2_ros', executable='static_transform_publisher',
             name='stf_map_base',
             arguments=['--frame-id', 'map', '--child-frame-id', 'base_link']),

        Node(package='nav2_map_server', executable='map_server', name='map_server',
             output='screen',
             parameters=[{'yaml_filename': map_yaml, 'use_sim_time': False}]),

        # planner_server provides /compute_path_to_pose + the global costmap
        Node(package='nav2_planner', executable='planner_server', name='planner_server',
             output='screen', parameters=[params]),

        Node(package='nav2_lifecycle_manager', executable='lifecycle_manager',
             name='lifecycle_manager_plan', output='screen',
             parameters=[{'use_sim_time': False, 'autostart': True,
                          'node_names': ['map_server', 'planner_server']}]),

        # click START (/initialpose) + GOAL (/goal_pose) -> /computed_path
        Node(package='go2_traversability', executable='click_path.py',
             name='click_path', output='screen'),

        Node(package='rviz2', executable='rviz2', name='rviz2',
             arguments=['-d', rviz_cfg], output='screen'),
    ])
