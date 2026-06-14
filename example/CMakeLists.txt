cmake_minimum_required(VERSION 3.5)
project(example_package)

find_package(ament_cmake REQUIRED)
find_package(asebaros REQUIRED)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()