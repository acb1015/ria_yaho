cmake_minimum_required(VERSION 3.8)
project(go2_motion_ws)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(UNITREE_SDK2_DIR
  ${CMAKE_CURRENT_SOURCE_DIR}/include/go2_motion_ws/unitree_sdk2
)

if(CMAKE_SYSTEM_PROCESSOR MATCHES "^(aarch64|arm64)$")
  set(UNITREE_SDK2_ARCH aarch64)
elseif(CMAKE_SYSTEM_PROCESSOR MATCHES "^(x86_64|amd64|AMD64)$")
  set(UNITREE_SDK2_ARCH x86_64)
else()
  message(FATAL_ERROR "Unsupported architecture for unitree_sdk2: ${CMAKE_SYSTEM_PROCESSOR}")
endif()

add_executable(standandlie
  src/stand.cpp
)

target_include_directories(standandlie PRIVATE
  ${UNITREE_SDK2_DIR}/include
  ${UNITREE_SDK2_DIR}/thirdparty/include
  ${UNITREE_SDK2_DIR}/thirdparty/include/ddscxx
)

target_link_directories(standandlie PRIVATE
  ${UNITREE_SDK2_DIR}/lib/${UNITREE_SDK2_ARCH}
  ${UNITREE_SDK2_DIR}/thirdparty/lib/${UNITREE_SDK2_ARCH}
)

target_link_libraries(standandlie
  unitree_sdk2
  ddscxx
  ddsc
  pthread
)

set_target_properties(standandlie PROPERTIES
  BUILD_RPATH "${UNITREE_SDK2_DIR}/thirdparty/lib/${UNITREE_SDK2_ARCH}"
  INSTALL_RPATH "${UNITREE_SDK2_DIR}/thirdparty/lib/${UNITREE_SDK2_ARCH}"
)

ament_target_dependencies(standandlie
  rclcpp
)
# =============================================
add_executable(movefoward
  src/movefoward.cpp
)

target_include_directories(movefoward PRIVATE
  ${UNITREE_SDK2_DIR}/include
  ${UNITREE_SDK2_DIR}/thirdparty/include
  ${UNITREE_SDK2_DIR}/thirdparty/include/ddscxx
)

target_link_directories(movefoward PRIVATE
  ${UNITREE_SDK2_DIR}/lib/${UNITREE_SDK2_ARCH}
  ${UNITREE_SDK2_DIR}/thirdparty/lib/${UNITREE_SDK2_ARCH}
)

target_link_libraries(movefoward
  unitree_sdk2
  ddscxx
  ddsc
  pthread
)

set_target_properties(movefoward PROPERTIES
  BUILD_RPATH "${UNITREE_SDK2_DIR}/thirdparty/lib/${UNITREE_SDK2_ARCH}"
  INSTALL_RPATH "${UNITREE_SDK2_DIR}/thirdparty/lib/${UNITREE_SDK2_ARCH}"
)

ament_target_dependencies(movefoward
  rclcpp
)

# =============================================

# 새 cpp 파일을 추가할 때는 아래 예시를 복사해서 주석을 풀고,
# 실행 파일 이름과 src/파일이름.cpp만 원하는 이름으로 바꾸면 됩니다.
#
# 예: src/go2_motion_ws/src/walk.cpp 파일을 컴파일하고 싶을 때
#
# add_executable(walk
#   src/walk.cpp
# )
#
# target_include_directories(walk PRIVATE
#   ${UNITREE_SDK2_DIR}/include
#   ${UNITREE_SDK2_DIR}/thirdparty/include
#   ${UNITREE_SDK2_DIR}/thirdparty/include/ddscxx
# )
#
# target_link_directories(walk PRIVATE
#   ${UNITREE_SDK2_DIR}/lib/${UNITREE_SDK2_ARCH}
#   ${UNITREE_SDK2_DIR}/thirdparty/lib/${UNITREE_SDK2_ARCH}
# )
#
# target_link_libraries(walk
#   unitree_sdk2
#   ddscxx
#   ddsc
#   pthread
# )
#
# set_target_properties(walk PROPERTIES
#   BUILD_RPATH "${UNITREE_SDK2_DIR}/thirdparty/lib/${UNITREE_SDK2_ARCH}"
#   INSTALL_RPATH "${UNITREE_SDK2_DIR}/thirdparty/lib/${UNITREE_SDK2_ARCH}"
# )
#
# ament_target_dependencies(walk
#   rclcpp
# )
#
# 마지막으로 아래 install(TARGETS ...)에도 walk를 추가해야
# ros2 run go2_motion_ws walk 로 실행할 수 있습니다.

install(TARGETS
  standandlie
  movefoward
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
