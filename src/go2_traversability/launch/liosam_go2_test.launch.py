"""LIO-SAM odometry/SLAM test — go2_slam_2d_3d (felixokolo) fork.

DISTINCT from the TixiaoShan lio_sam test (liosam_odom_test.launch.py):
  - package:    lio_sam_go2   (renamed from lio_sam to avoid clash)
  - source:     src/go2_slam_2d_3d/src/LIO-SAM-ros2
  - config:     params_ouster.yaml (Ouster OS-1-64, /ouster/points, /ouster/imu)
  - nodes:      imageProjection + featureExtraction + mapOptimization
                + imuPreintegration (IMU fused into the factor graph for better
                  rotation; publishes odom->base_link)

Periodic map auto-save (on by default): every `save_interval` s the map is
written to $HOME/<save_dir> via /lio_sam/save_map. Robust to kill -9.
  WARNING: save_map does `rm -r $HOME/<save_dir>` each time -> use a dedicated
  folder (default /go2_maps/).

Run in your OWN terminal (RViz shares the same DDS env and displays):
  ros2 launch go2_traversability liosam_go2_test.launch.py
  ros2 launch go2_traversability liosam_go2_test.launch.py auto_save:=false
  ros2 launch go2_traversability liosam_go2_test.launch.py save_interval:=60.0 save_dir:=/my_maps/
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    auto_save = LaunchConfiguration('auto_save')
    save_interval = LaunchConfiguration('save_interval')
    save_dir = LaunchConfiguration('save_dir')

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
        # IMU preintegration: fuses IMU into the factor graph for better rotation
        # and publishes odom->base_link (distinct from mapOptimization's
        # odom->velodyne_base, so no TF clash). Safe because lidarFrame ==
        # baselinkFrame in params_ouster.yaml (no lidar<->base TF lookup).
        lnode('lio_sam_go2_imuPreintegration'),
        Node(package='rviz2', executable='rviz2', name='rviz2',
             arguments=['-d', rviz_cfg], output='screen'),
        # Periodic map auto-save via /lio_sam/save_map.
        Node(package='go2_traversability', executable='auto_save_map.py',
             name='lio_sam_auto_saver', output='screen',
             condition=IfCondition(auto_save),
             parameters=[{
                 'interval': ParameterValue(save_interval, value_type=float),
                 'destination': ParameterValue(save_dir, value_type=str),
                 'resolution': 0.0,
             }]),
    ]

    return LaunchDescription([
        DeclareLaunchArgument('auto_save', default_value='true',
                              description='Periodically save the map to disk'),
        DeclareLaunchArgument('save_interval', default_value='30.0',
                              description='Seconds between auto-saves'),
        DeclareLaunchArgument('save_dir', default_value='/go2_maps/',
                              description='$HOME-relative save folder (gets rm -r each save!)'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(ouster_launch),
            launch_arguments={'viz': 'false'}.items(),
        ),
        TimerAction(period=8.0, actions=lio_stack),
    ])
