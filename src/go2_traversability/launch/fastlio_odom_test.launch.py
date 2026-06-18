"""FAST_LIO odometry-only TEST (not the final pipeline).

Brings up Ouster + FAST_LIO, then opens RViz with only FAST_LIO odometry
outputs visible:
  - /Odometry
  - /path
  - TF camera_init -> body

FAST_LIO still consumes /ouster/points and /ouster/imu internally. This launch
only hides the 3D point cloud displays in RViz so odometry can be checked alone.

Run in your OWN terminal (so RViz shares the same DDS env and displays):
  ros2 launch go2_traversability fastlio_odom_test.launch.py
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    fastlio_delay = LaunchConfiguration('fastlio_delay')
    ouster_launch = os.path.join(
        get_package_share_directory('ouster_ros'), 'launch', 'driver.launch.py')
    fastlio_share = get_package_share_directory('fast_lio')
    fastlio_launch = os.path.join(fastlio_share, 'launch', 'mapping_ouster64.launch.py')
    rviz_cfg = os.path.join(fastlio_share, 'rviz_cfg', 'fastlio_odom_only.rviz')

    return LaunchDescription([
        DeclareLaunchArgument(
            'fastlio_delay',
            default_value='8.0',
            description='Delay FAST_LIO startup so the robot can finish standing still first.'),

        # Ouster driver -> /ouster/points, /ouster/imu
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(ouster_launch),
            launch_arguments={'viz': 'false'}.items(),
        ),

        # FAST_LIO computes odometry with LiDAR+IMU; RViz shows odometry only.
        # Keep the robot still when this starts because FAST_LIO initializes
        # gravity and gyro bias from the first IMU/lidar packets.
        TimerAction(
            period=fastlio_delay,
            actions=[
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(fastlio_launch),
                    launch_arguments={'rviz': 'true', 'rviz_cfg': rviz_cfg}.items(),
                ),
            ],
        ),
    ])
