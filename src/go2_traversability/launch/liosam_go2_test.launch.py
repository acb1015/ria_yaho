"""LIO-SAM odometry test — go2_slam_2d_3d (felixokolo) fork.

DISTINCT from the TixiaoShan lio_sam test (liosam_odom_test.launch.py):
  - package:    lio_sam_go2   (renamed from lio_sam to avoid clash)
  - source:     src/go2_slam_2d_3d/src/LIO-SAM-ros2
  - config:     params_ouster.yaml (Ouster OS-1-64, /ouster/points, /ouster/imu)
  - nodes:      imageProjection + featureExtraction + mapOptimization ONLY
                (this fork drops imuPreintegration and robot_state_publisher,
                 which avoids the xacro + TF-extrapolation issues seen before)

Run in your OWN terminal (RViz shares the same DDS env and displays):
  ros2 launch go2_traversability liosam_go2_test.launch.py
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    ouster_launch = os.path.join(
        get_package_share_directory('ouster_ros'), 'launch', 'driver.launch.py')
    lio_share = get_package_share_directory('lio_sam_go2')
    params = os.path.join(lio_share, 'config', 'params_ouster.yaml')
    rviz_cfg = os.path.join(lio_share, 'config', 'rviz2.rviz')

    def lnode(exe):
        return Node(package='lio_sam_go2', executable=exe, name=exe,
                    parameters=[params], output='screen')

    lio_stack = [
        Node(package='tf2_ros', executable='static_transform_publisher',
             name='stf_map_odom',
             arguments=['--frame-id', 'map', '--child-frame-id', 'odom']),
        lnode('lio_sam_go2_imageProjection'),
        lnode('lio_sam_go2_featureExtraction'),
        lnode('lio_sam_go2_mapOptimization'),
        Node(package='rviz2', executable='rviz2', name='rviz2',
             arguments=['-d', rviz_cfg], output='screen'),
    ]

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(ouster_launch),
            launch_arguments={'viz': 'false'}.items(),
        ),
        TimerAction(period=8.0, actions=lio_stack),
    ])
