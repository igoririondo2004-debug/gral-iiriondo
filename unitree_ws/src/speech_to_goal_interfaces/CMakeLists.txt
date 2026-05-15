cmake_minimum_required(VERSION 3.8)
project(speech_to_goal_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# ---------------------------------------
# DEPENDENCIES
# ---------------------------------------
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# ---------------------------------------
# INTERFACES
# ---------------------------------------
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Waypoint.msg"
  "srv/LLMQuery.srv"
  "srv/DetectIntent.srv"
)

# ---------------------------------------
# RUNTIME EXPORT (IMPORTANT)
# ---------------------------------------
ament_export_dependencies(rosidl_default_runtime)

# ---------------------------------------
# PACKAGE
# ---------------------------------------
ament_package()