"""Nav2 navigation on the pre-built 2D map, localized with AMCL.

TF / data flow:
  Ouster ─ /ouster/points ─┬─ LIO-SAM (odom->base_link)         [odometry]
                           └─ pointcloud_to_laserscan ─ /scan
  AMCL: /scan + /map  ─► map->odom                              [localization]
  map_server: map_clean.yaml ─► /map
  Nav2 planner/controller: /map + goal ─► path + cmd_vel        [navigation]

LIO-SAM here runs for ODOMETRY only (no static map->odom; AMCL owns map->odom).
The 2D map is static, so AMCL relocalizes the robot in it (set the initial pose
in RViz with "2D Pose Estimate", then send a goal with "Nav2 Goal").

Run:
  ros2 launch go2_traversability nav2_liosam.launch.py
  ros2 launch go2_traversability nav2_liosam.launch.py map:=$HOME/go2_maps/map.yaml
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription, TimerAction, DeclareLaunchArgument)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    go2_share = get_package_share_directory('go2_traversability')
    nav2_share = get_package_share_directory('nav2_bringup')
    lio_share = get_package_share_directory('lio_sam_go2')

    ouster_launch = os.path.join(
        get_package_share_directory('ouster_ros'), 'launch', 'driver.launch.py')
    lio_params = os.path.join(lio_share, 'config', 'params_ouster.yaml')
    nav2_params = os.path.join(go2_share, 'config', 'nav2_params.yaml')
    rviz_cfg = os.path.join(nav2_share, 'rviz', 'nav2_default_view.rviz')

    map_yaml = LaunchConfiguration('map')

    def lionode(exe):
        return Node(package='lio_sam_go2', executable=exe, name=exe,
                    parameters=[lio_params], output='screen')

    # LIO-SAM odometry (no static map->odom: AMCL provides map->odom)
    odom_stack = [
        lionode('lio_sam_go2_imageProjection'),
        lionode('lio_sam_go2_featureExtraction'),
        lionode('lio_sam_go2_mapOptimization'),
        lionode('lio_sam_go2_imuPreintegration'),
        # cloud frame relative to base (LIO-SAM treats the cloud as base_link)
        Node(package='tf2_ros', executable='static_transform_publisher',
             name='stf_base_os_sensor',
             arguments=['--frame-id', 'base_link', '--child-frame-id', 'os_sensor']),
        # 3D cloud -> 2D /scan for AMCL & costmaps
        Node(package='pointcloud_to_laserscan',
             executable='pointcloud_to_laserscan_node', name='pointcloud_to_laserscan',
             remappings=[('cloud_in', '/ouster/points'), ('scan', '/scan')],
             parameters=[{
                 'target_frame': 'os_sensor',
                 'transform_tolerance': 0.05,
                 # Heights are in the sensor frame; the floor is ~0.30 m BELOW
                 # the sensor. min_height must stay ABOVE the floor or the floor
                 # returns become a ring of false obstacles around the robot.
                 'min_height': 0.15, 'max_height': 1.2,
                 'angle_min': -3.14159, 'angle_max': 3.14159,
                 'angle_increment': 0.0087, 'scan_time': 0.1,
                 'range_min': 0.3, 'range_max': 10.0,
                 'use_inf': True,
             }]),
    ]

    nav2_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_share, 'launch', 'bringup_launch.py')),
        launch_arguments={
            'map': map_yaml,
            'params_file': nav2_params,
            'use_sim_time': 'false',
            'autostart': 'true',
            'use_composition': 'True',
        }.items(),
    )

    return LaunchDescription([
        DeclareLaunchArgument('map',
                              default_value=os.path.expanduser('~/go2_maps/map_clean.yaml'),
                              description='2D occupancy map (yaml) for Nav2'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(ouster_launch),
            launch_arguments={'viz': 'false'}.items()),
        # odometry first
        TimerAction(period=8.0, actions=odom_stack),
        # then Nav2 (needs odom->base_link + /scan up)
        TimerAction(period=14.0, actions=[nav2_bringup]),
        Node(package='rviz2', executable='rviz2', name='rviz2',
             arguments=['-d', rviz_cfg], output='screen'),
    ])
