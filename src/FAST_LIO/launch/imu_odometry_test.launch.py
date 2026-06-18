"""Compatibility launch for the old test name.

This does NOT run an IMU-only dead-reckoning node. It runs FAST_LIO itself and
opens the odometry-only RViz config.
"""

import os.path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    fastlio_share = get_package_share_directory('fast_lio')
    mapping_launch = os.path.join(fastlio_share, 'launch', 'mapping_ouster64.launch.py')
    rviz_cfg = os.path.join(fastlio_share, 'rviz_cfg', 'fastlio_odom_only.rviz')

    return LaunchDescription([
        LogInfo(msg='imu_odometry_test.launch.py now runs FAST_LIO odometry only.'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(mapping_launch),
            launch_arguments={'rviz': 'true', 'rviz_cfg': rviz_cfg}.items(),
        ),
    ])
