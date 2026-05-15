cmake_minimum_required(VERSION 3.8)
project(object_recognition_interfaces)

# --------------------------------------------------
# Compiler warnings
# --------------------------------------------------
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# --------------------------------------------------
# DEPENDENCIES
# --------------------------------------------------
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# --------------------------------------------------
# INTERFACES
# --------------------------------------------------
rosidl_generate_interfaces(${PROJECT_NAME}

  "srv/DetectObject.srv"
  "srv/AddObject.srv"

)

# --------------------------------------------------
# EXPORT
# --------------------------------------------------
ament_export_dependencies(rosidl_default_runtime)

# --------------------------------------------------
# TESTS (opcional)
# --------------------------------------------------
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)

  ament_lint_auto_find_test_dependencies()
endif()

# --------------------------------------------------
# PACKAGE
# --------------------------------------------------
ament_package()