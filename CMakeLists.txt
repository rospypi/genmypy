cmake_minimum_required(VERSION 3.0.2)
project(genpyi)
find_package(catkin REQUIRED COMPONENTS genmsg genpy)

catkin_package(
  CATKIN_DEPENDS genmsg genpy
  CFG_EXTRAS genpyi-extras.cmake
)

add_subdirectory(scripts)

file(WRITE ${CATKIN_DEVEL_PREFIX}/${GENMSG_LANGS_DESTINATION}/genpyi "Python Stub")
install(FILES ${CATKIN_DEVEL_PREFIX}/${GENMSG_LANGS_DESTINATION}/genpyi
  DESTINATION ${GENMSG_LANGS_DESTINATION})

catkin_python_setup()
