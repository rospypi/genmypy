cmake_minimum_required(VERSION 3.0.2)
project(genpy_stubgen)
find_package(catkin REQUIRED COMPONENTS genmsg genpy)

catkin_package(
  CATKIN_DEPENDS genmsg genpy
  CFG_EXTRAS genpy-stubgen-extras.cmake
)

add_subdirectory(scripts)

file(WRITE ${CATKIN_DEVEL_PREFIX}/${GENMSG_LANGS_DESTINATION}/genpy_stubgen "Python stub")
install(FILES ${CATKIN_DEVEL_PREFIX}/${GENMSG_LANGS_DESTINATION}/genpy_stubgen
  DESTINATION ${GENMSG_LANGS_DESTINATION})

catkin_python_setup()
