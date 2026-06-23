"""View a 2D occupancy map (PGM/YAML) in RViz — no sensors, no Nav2 stack.

Just nav2_map_server (loads + publishes /map) + lifecycle activation + RViz
(top-down view, fixed frame = map). Quick way to inspect a converted map.

  ros2 launch go2_traversability view_2dmap.launch.py
  ros2 launch go2_traversability view_2dmap.launch.py map:=$HOME/go2_maps/map.yaml
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    go2_share = get_package_share_directory('go2_traversability')
    map_yaml = LaunchConfiguration('map')
    rviz_cfg = os.path.join(go2_share, 'config', 'view_2dmap.rviz')

    return LaunchDescription([
        DeclareLaunchArgument(
            'map', default_value=os.path.expanduser('~/go2_maps/map_clean.yaml'),
            description='2D occupancy map yaml to view'),

        Node(package='nav2_map_server', executable='map_server', name='map_server',
             output='screen',
             parameters=[{'yaml_filename': map_yaml, 'use_sim_time': False}]),

        # map_server is a lifecycle node -> configure + activate so it publishes /map
        Node(package='nav2_lifecycle_manager', executable='lifecycle_manager',
             name='lifecycle_manager_mapview', output='screen',
             parameters=[{'use_sim_time': False, 'autostart': True,
                          'node_names': ['map_server']}]),

        Node(package='rviz2', executable='rviz2', name='rviz2',
             arguments=['-d', rviz_cfg], output='screen'),
    ])
