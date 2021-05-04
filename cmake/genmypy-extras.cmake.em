@[if DEVELSPACE]@
# location of scripts in develspace
set(GENMYPY_DIR "@(CMAKE_CURRENT_SOURCE_DIR)/scripts")
@[else]@
# location of scripts in installspace
set(GENMYPY_DIR "${genmypy_DIR}/../../../@(CATKIN_PACKAGE_BIN_DESTINATION)")
@[end if]@

set(GENMYPY_BIN ${GENMYPY_DIR}/genmypy)

macro(_generate_genmypy ARG_KIND ARG_PKG ARG_FILE ARG_IFLAGS ARG_MSG_DEPS ARG_GEN_OUTPUT_DIR)
  file(MAKE_DIRECTORY ${ARG_GEN_OUTPUT_DIR})

  # in order to get output file path
  get_filename_component(FILE_NAME ${ARG_FILE} NAME)
  get_filename_component(FILE_SHORT_NAME ${ARG_FILE} NAME_WE)

  set(GENERATED_FILE_NAME _${FILE_SHORT_NAME}.pyi)
  set(GEN_OUTPUT_FILE ${ARG_GEN_OUTPUT_DIR}/${GENERATED_FILE_NAME})

  add_custom_command(OUTPUT ${GEN_OUTPUT_FILE}
    DEPENDS ${GENMYPY_BIN} ${ARG_FILE} ${ARG_MSG_DEPS}
    COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMYPY_BIN} ${ARG_KIND} ${ARG_PKG}
      --out-dir ${ARG_GEN_OUTPUT_DIR}
      ${ARG_IFLAGS}
      ${ARG_FILE}
    COMMENT "Generating Python Stub from ${ARG_PKG}/${FILE_SHORT_NAME}"
    WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
  )

  list(APPEND ALL_GEN_OUTPUT_FILES_mypy ${GEN_OUTPUT_FILE})

endmacro()

macro(_generate_msg_mypy ARG_PKG ARG_MSG ARG_IFLAGS ARG_MSG_DEPS ARG_GEN_OUTPUT_DIR)
  _generate_genmypy("msg" ${ARG_PKG} ${ARG_MSG} "${ARG_IFLAGS}" "${ARG_MSG_DEPS}" "${ARG_GEN_OUTPUT_DIR}/msg")
endmacro()

macro(_generate_srv_mypy ARG_PKG ARG_SRV ARG_IFLAGS ARG_MSG_DEPS ARG_GEN_OUTPUT_DIR)
  _generate_genmypy("srv" ${ARG_PKG} ${ARG_SRV} "${ARG_IFLAGS}" "${ARG_MSG_DEPS}" "${ARG_GEN_OUTPUT_DIR}/srv")
endmacro()

macro(_generate_module_mypy ARG_PKG ARG_GEN_OUTPUT_DIR ARG_GENERATED_FILES)
  # place an empty __init__.pyi in the parent folder of msg/srv
  if(NOT EXISTS ${ARG_GEN_OUTPUT_DIR}/__init__.pyi)
    file(WRITE ${ARG_GEN_OUTPUT_DIR}/__init__.pyi "")
  endif()

  # place py.typed in order to mark this package as PEP561 compatible
  if(NOT EXISTS ${ARG_GEN_OUTPUT_DIR}/py.typed)
    file(WRITE ${ARG_GEN_OUTPUT_DIR}/py.typed "")
  endif()

  foreach(type "msg" "srv")
    set(GEN_OUTPUT_DIR "${ARG_GEN_OUTPUT_DIR}/${type}")
    set(GEN_OUTPUT_FILE ${GEN_OUTPUT_DIR}/__init__.pyi)

    if(IS_DIRECTORY ${GEN_OUTPUT_DIR})
      add_custom_command(OUTPUT ${GEN_OUTPUT_FILE}
        DEPENDS ${GENMYPY_BIN}
        COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMYPY_BIN} module
          --module-finder py
          --out-dir ${GEN_OUTPUT_DIR}
          ${GEN_OUTPUT_DIR}
        COMMENT "Generating Python Stub ${type} __init__.pyi for ${ARG_PKG}"
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
      )
      list(APPEND ALL_GEN_OUTPUT_FILES_mypy ${GEN_OUTPUT_FILE})
    endif()

  endforeach()

endmacro()

# {lang}_INSTALL_DIR is to control ARG_GEN_OUTPUT_DIR
# See: https://github.com/ros/genmsg/blob/7d8b6ce6f43b6e39ea8261125d270f2d3062356f/cmake/pkg-genmsg.cmake.em#L85-L96
if(NOT EXISTS @(PROJECT_NAME)_SOURCE_DIR)
  set(genmypy_INSTALL_DIR ${PYTHON_INSTALL_DIR})
endif()
