# Declare the version of the CMake API for forward-compatibility
cmake_minimum_required(VERSION 3.0)

# Declare the name of the CMake Project
project(project_name)

add_compile_options(-std=c++17 -Wall)

include_directories(${CMAKE_SOURCE_DIR} include src)

# Create library using appropriate header and source files
add_library(Hello include/Hello.hpp src/Hello.cpp)

# Define an executable target called executable_name
add_executable(executable_name src/main.cpp)

# Specify libraries or flags to use when linking a given target
target_link_libraries(executable_name Hello)

# Create binary files in a /bin folder
set(EXECUTABLE_OUTPUT_PATH  ${PROJECT_SOURCE_DIR}/bin/)

# install(TARGETS executable_name DESTINATION bin)