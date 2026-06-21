"""Bring up the lower half of the traversability pipeline (verified working):

  Ouster driver  ->  /ouster/points (os_sensor), /ouster/imu (os_imu)
  FAST_LIO       ->  /Odometry (camera_init -> body) + TF
  bridge TF      ->  body -> os_sensor, so the full chain resolves:
                     camera_init -> body -> os_sensor -> {os_imu, os_lidar}

This is what elevation_mapping_cupy consumes: a point cloud plus a TF from a
fixed frame (camera_init) down to the sensor frame (os_sensor).

The body->os_sensor static transform is the inverse of the Ouster-published
os_sensor->os_imu transform (translation only; rotation is identity), because
FAST_LIO's `body` frame is the Ouster IMU (os_imu). Values come straight from
/tf_static (os_sensor->os_imu = -0.002441, -0.009725, +0.007533).
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    viz = LaunchConfiguration('viz')

    ouster_launch = os.path.join(
        get_package_share_directory('ouster_ros'), 'launch', 'driver.launch.py')
    fastlio_launch = os.path.join(
        get_package_share_directory('fast_lio'), 'launch', 'mapping_ouster64.launch.py')

    return LaunchDescription([
        DeclareLaunchArgument('viz', default_value='false',
                              description='Open RViz for the Ouster driver / FAST_LIO'),

        # 1) Ouster sensor driver -> /ouster/points, /ouster/imu
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(ouster_launch),
            launch_arguments={'viz': viz}.items(),
        ),

        # 2) FAST_LIO odometry -> /Odometry, TF camera_init -> body
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(fastlio_launch),
            launch_arguments={'rviz': viz}.items(),
        ),

        # 3) Bridge FAST_LIO body frame to the Ouster sensor frame so the TF
        #    tree is connected end to end (camera_init -> ... -> os_sensor).
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='body_to_os_sensor',
            arguments=[
                '--x', '0.002441', '--y', '0.009725', '--z', '-0.007533',
                '--roll', '0', '--pitch', '0', '--yaw', '0',
                '--frame-id', 'body', '--child-frame-id', 'os_sensor',
            ],
        ),
    ])
