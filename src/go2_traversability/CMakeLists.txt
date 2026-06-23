cmake_minimum_required(VERSION 3.8)
project(go2_traversability)

find_package(ament_cmake REQUIRED)

# Launch files, configs (GridMap->OccupancyGrid node and Nav2 params land here later)
install(DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)

# Python helper scripts run as nodes (e.g. periodic map auto-saver)
install(PROGRAMS
  scripts/auto_save_map.py
  scripts/compute_nav2_path.py
  scripts/click_path.py
  scripts/cmd_vel_to_unitree.py
  scripts/pcd_to_2dmap.py
  scripts/scan_debug_points.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
