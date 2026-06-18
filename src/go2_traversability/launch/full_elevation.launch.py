"""One-shot launch for the whole 2.5D elevation pipeline + RViz.

Brings up, all in the SAME environment (so DDS/RMW always matches and RViz
sees the topics):
  Ouster driver  ->  FAST_LIO odom + TF  ->  body->os_sensor bridge TF
  ->  elevation_mapping_cupy (go2 config)  ->  RViz (elevation map view)

Usage:
  ros2 launch go2_traversability full_elevation.launch.py
  ros2 launch go2_traversability full_elevation.launch.py use_rviz:=false

NOTE: the toggle is 'use_rviz' (NOT 'rviz'). FAST_LIO's included launch already
declares a 'rviz' argument; reusing that name here makes the included 'rviz:=false'
leak into this file's scope and silently disable our RViz. 'use_rviz' avoids that.
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription, DeclareLaunchArgument, TimerAction,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch_ros.actions import Node


def generate_launch_description():
    use_rviz = LaunchConfiguration('use_rviz')

    go2_share = get_package_share_directory('go2_traversability')
    emc_share = get_package_share_directory('elevation_mapping_cupy')

    bringup_launch = os.path.join(go2_share, 'launch', 'sensor_odom_bringup.launch.py')
    emc_launch = os.path.join(emc_share, 'launch', 'elevation_mapping.launch.py')
    rviz_config = os.path.join(go2_share, 'config', 'elevation.rviz')

    return LaunchDescription([
        DeclareLaunchArgument('use_rviz', default_value='true',
                              description='Launch RViz with the elevation map view'),

        # Sensor + FAST_LIO odom + bridge TF (starts immediately)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(bringup_launch),
            launch_arguments={'viz': 'false'}.items(),
        ),

        # elevation_mapping_cupy — delayed so the Ouster sensor and FAST_LIO TF
        # are up first (sensor init ~12s, IMU init a bit more).
        TimerAction(period=10.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(emc_launch),
                launch_arguments={'robot_config': 'go2/base.yaml'}.items(),
            ),
        ]),

        # RViz (same environment as the nodes above -> always sees the topics)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen',
            condition=IfCondition(use_rviz),
        ),
    ])
