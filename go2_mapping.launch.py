#!/usr/bin/env python3
"""
Go2 + Ouster OS1 통합 매핑 launch
  - Ouster OS1 드라이버 (RViz 없음)
  - FAST-LIO2 (실시간 LIO 오도메트리 + 맵)
  - PGO (루프 클로저 / pose graph 최적화)

순차 기동(드라이버 → FAST-LIO → PGO)으로 초기화 타이밍 문제와 발산을 줄인다.

사용:
  ros2 launch ~/go2_ws/go2_mapping.launch.py
  ros2 launch ~/go2_ws/go2_mapping.launch.py rviz:=false   # RViz 끄기(CPU 절약)
"""
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    TimerAction,
    LogInfo,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    rviz = LaunchConfiguration("rviz")
    rviz_arg = DeclareLaunchArgument(
        "rviz", default_value="true",
        description="FAST-LIO RViz 시각화 표시 여부",
    )

    ouster_share = get_package_share_directory("ouster_ros")
    fastlio_share = get_package_share_directory("fast_lio")
    pgo_share = get_package_share_directory("pgo")

    # 1) Ouster OS1 드라이버 (자체 RViz는 끔)
    ouster_driver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ouster_share, "launch", "driver.launch.py")
        ),
        launch_arguments={"viz": "false"}.items(),
    )

    # 2) FAST-LIO2 (드라이버가 센서 연결을 잡을 시간을 준 뒤 기동)
    fastlio = TimerAction(
        period=4.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(fastlio_share, "launch", "mapping_ouster64.launch.py")
                ),
                launch_arguments={"rviz": rviz}.items(),
            )
        ],
    )

    # 3) PGO 루프 클로저 (FAST-LIO 초기화 이후 기동)
    pgo_node = TimerAction(
        period=8.0,
        actions=[
            LogInfo(msg="PGO(loop closure) 노드 기동..."),
            Node(
                package="pgo",
                executable="pgo_node",
                name="pgo_node",
                output="screen",
                parameters=[{
                    "config_path": os.path.join(pgo_share, "config", "pgo.yaml")
                }],
            ),
        ],
    )

    return LaunchDescription([
        rviz_arg,
        LogInfo(msg="=== Go2 + Ouster OS1 통합 매핑 시작 (driver -> FAST-LIO -> PGO) ==="),
        ouster_driver,
        fastlio,
        pgo_node,
    ])
