"""LIO-SAM odometry TEST (alternative SLAM to compare against FAST_LIO).

Self-contained: does NOT use lio_sam/run.launch.py (which needs `xacro`, not
installed). LIO-SAM's robot.urdf.xacro has only identity fixed joints, so we
replace robot_state_publisher with identity static_transform_publishers.

TF tree: map -(static)-> odom -(LIO-SAM)-> base_link -(static)-> lidar_link, etc.

Drive the robot and judge odometry quality: sharp single-walled accumulated map
= good, smearing/ghosting = bad.

Run in your OWN terminal (so RViz shares the same DDS env and displays):
  ros2 launch go2_traversability liosam_odom_test.launch.py
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def stf(parent, child):
    """Identity static transform (replaces a fixed joint from the URDF)."""
    return Node(
        package='tf2_ros', executable='static_transform_publisher',
        name=f'stf_{parent}_to_{child}',
        arguments=['--frame-id', parent, '--child-frame-id', child],
    )


def lio_node(exe):
    return Node(package='lio_sam', executable=exe, name=exe,
                parameters=[LIO_PARAMS], output='screen')


LIO_PARAMS = os.path.join(
    get_package_share_directory('lio_sam'), 'config', 'params.yaml')


def generate_launch_description():
    ouster_launch = os.path.join(
        get_package_share_directory('ouster_ros'), 'launch', 'driver.launch.py')
    rviz_cfg = os.path.join(
        get_package_share_directory('lio_sam'), 'config', 'rviz2.rviz')

    lio_stack = [
        # map -> odom (LIO-SAM publishes odom -> base_link itself)
        stf('map', 'odom'),
        # URDF replacement (all identity joints in robot.urdf.xacro)
        stf('base_link', 'chassis_link'),
        stf('base_link', 'lidar_link'),
        stf('chassis_link', 'imu_link'),
        stf('imu_link', 'laser_sensor_frame'),
        stf('chassis_link', 'navsat_link'),
        # LIO-SAM nodes
        lio_node('lio_sam_imuPreintegration'),
        lio_node('lio_sam_imageProjection'),
        lio_node('lio_sam_featureExtraction'),
        lio_node('lio_sam_mapOptimization'),
        # RViz
        Node(package='rviz2', executable='rviz2', name='rviz2',
             arguments=['-d', rviz_cfg], output='screen'),
    ]

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(ouster_launch),
            launch_arguments={'viz': 'false'}.items(),
        ),
        # delay so the sensor is up and the robot settles before LIO-SAM init
        TimerAction(period=8.0, actions=lio_stack),
    ])
