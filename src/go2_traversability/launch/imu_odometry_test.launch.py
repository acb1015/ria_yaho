"""Compatibility launch for the old test name.

This does NOT run an IMU-only dead-reckoning node. It forwards to the FAST_LIO
odometry-only test launch.
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    fastlio_odom_launch = os.path.join(
        get_package_share_directory('go2_traversability'),
        'launch',
        'fastlio_odom_test.launch.py')

    return LaunchDescription([
        LogInfo(msg='imu_odometry_test.launch.py now forwards to FAST_LIO odometry only.'),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(fastlio_odom_launch)),
    ])
