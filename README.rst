=======
genmypy
=======

A Python stub generator from genmsg specs

Installation
============

If you use catkin and need CMake support for the ``genmypy`` generator, clone the repository and add it to your catkin workspace.

.. code:: sh

    cd /path/to/your/ws
    git clone https://github.com/rospypi/genmypy.git


If you don't need the cmake support, you can also install it from `pypi.org <https://pypi.org/>`_:

.. code:: sh

    pip install genmypy

Usage
=====

catkin
------

Add ``genmypy`` along with ``message_generation`` to ``find_package`` in
CMakeLists.txt. ``genmsg`` will find ``genmypy`` automatically when
building msg/srv files.

Also, keep in mind that your package should have the build dependency
for ``genmypy`` in ``package.xml`` to make sure that catkin finishes the
build of ``genmypy`` before building your package.

Examples:

- CMakeLists.txt
    .. code:: cmake

        find_package(catkin REQUIRED COMPONENTS std_msgs message_generation genmypy)
- package.xml
    .. code:: xml

        <build_depend>genmypy</build_depend>

CLI
---

::

    $ genmypy --help
    Usage: genmypy [-h] {msg,srv,module} ...
    positional arguments:
      {msg,srv,module}
        msg             Generate stub files from .msg files
        srv             Generate stub files from .srv files
        module          Generate __init__.pyi from a msg/srv directory

    optional arguments:
      -h, --help        show this help message and exit

Examples:
~~~~~~~~~

.. code:: sh

    # Message files
    $ genmypy msg custom_msgs custom_msgs/msg/Custom.msg
    $ genmypy msg std_msgs --out-dir out /opt/ros/noetic/share/std_msgs/msg/Header.msg
    $ genmypy msg sensor_msgs --out-dir out \
        -Istd_msgs:/opt/ros/noetic/share/std_msgs/msg \
        -Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/msg \
        /opt/ros/noetic/share/sensor_msgs/msg/PointCloud2.msg

    # Service files
    $ genmypy srv custom_msgs custom_msgs/srv/Custom.msg
    $ genmypy srv nav_msgs --out-dir out \
        -Istd_msgs:/opt/ros/noetic/share/std_msgs/msg \
        -Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/msg \
        /opt/ros/noetic/share/sensor_msgs/srv/SetCameraInfo.srv

    # Module files
    $ genmypy module custom_msgs/msg
    $ genmypy module --module-finder py --out out \
        /opt/ros/noetic/lib/python2.7/dist-packages/std_msgs/msg/

``genmypy msg`` / ``genmypy srv``:

.. code:: sh

    Usage: genmypy {msg,srv} [-h] [--out-dir OUT_DIR]
                            [--include-path INCLUDE_PATH]
                            package files [files ...]

    positional arguments:
      package               Package name of given files
      files                 Files to generate stubs

    optional arguments:
      -h, --help            show this help message and exit
      --out-dir OUT_DIR     Output directory. If the option is unset, each stub
                            file will be generated in the same directory as each
                            input.
      --include-path INCLUDE_PATH, -I INCLUDE_PATH
                            Include paths for processing given files

``genmypy module``:

.. code:: sh

    Usage: genmypy module [-h] [--out-dir OUT_DIR] package_dir

    Positional arguments:
      package_dir        Package directory to create __init__.pyi

    Optional arguments:
      -h, --help         show this help message and exit
      --out-dir OUT_DIR  Output directory. If the option is unset, __init__.pyi
                         will be generated in the same directory as package_dir.
