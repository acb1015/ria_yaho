cmake_minimum_required(VERSION 3.8)
project(go2_traversability)

find_package(ament_cmake REQUIRED)

# Launch files, configs (GridMap->OccupancyGrid node and Nav2 params land here later)
install(DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
