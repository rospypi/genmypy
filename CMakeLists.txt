cmake_minimum_required(VERSION 3.0.2)
project(genmypy)
find_package(catkin REQUIRED COMPONENTS genmsg genpy)

catkin_package(
  CATKIN_DEPENDS genmsg genpy
  CFG_EXTRAS genmypy-extras.cmake
)

add_subdirectory(scripts)

file(WRITE ${CATKIN_DEVEL_PREFIX}/${GENMSG_LANGS_DESTINATION}/genmypy "Python Stub")
install(FILES ${CATKIN_DEVEL_PREFIX}/${GENMSG_LANGS_DESTINATION}/genmypy
  DESTINATION ${GENMSG_LANGS_DESTINATION})

catkin_python_setup()
