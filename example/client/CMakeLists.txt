cmake_minimum_required(VERSION 4.0)
project(example_client)

find_package(ament_cmake REQUIRED)
find_package(asebaros REQUIRED)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()