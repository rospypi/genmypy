======
genpyi
======

A Python stub generator from genmsg specs

Installation
============

.. code:: sh

    pip install genpyi

Usage
=====

catkin
------

Add ``genpyi`` along with ``message_generation`` to ``find_package`` in
CMakeLists.txt. ``genmsg`` will find ``genpyi`` automatically when
building msg/srv files.

Also, keep in mind that your package should have the build dependency
for ``genpyi`` in ``package.xml`` to make sure that catkin finishes the
build of ``genpyi`` before building your package.

Examples:

-  CMakeLists.txt
    .. code:: cmake

        find_package(catkin REQUIRED COMPONENTS std_msgs message_generation genpyi)
-  package.xml
    .. code:: xml
    
        <build_depend>genpyi</build_depend>

CLI
---

::

    $ genpyi --help
    Usage: genpyi [-h] {msg,srv,module} ...
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
    $ genpyi msg custom_msgs custom_msgs/msg/Custom.msg
    $ genpyi msg std_msgs --out-dir out /opt/ros/melodic/share/std_msgs/msg/Header.msg
    $ genpyi msg sensor_msgs --out-dir out \
        -Istd_msgs:/opt/ros/melodic/share/std_msgs/msg \
        -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/msg \
        /opt/ros/melodic/share/sensor_msgs/msg/PointCloud2.msg

    # Service files
    $ genpyi srv custom_msgs custom_msgs/srv/Custom.msg
    $ genpyi srv nav_msgs --out-dir out \
        -Istd_msgs:/opt/ros/melodic/share/std_msgs/msg \
        -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/msg \
        /opt/ros/melodic/share/sensor_msgs/srv/SetCameraInfo.srv

    # Module files
    $ genpyi module custom_msgs/msg
    $ genpyi module --module-finder py --out out \
        /opt/ros/melodic/lib/python2.7/dist-packages/std_msgs/msg/

``genpyi msg`` / ``genpyi srv``:

.. code:: sh 

    Usage: genpyi {msg,srv} [-h]
       [--out-dir OUT\_DIR] [--include-path INCLUDE\_PATH] package files
       [files ...]

    positional arguments: package Package name of given files files Files to
    generate stubs

    optional arguments: -h, --help show this help message and exit --out-dir
    OUT\_DIR Output directory. If the option is unset, each stub file will
    be generated in the same directory as each input. --include-path
    INCLUDE\_PATH, -I INCLUDE\_PATH Include paths for processing given files

``genpyi module``:

.. code:: sh

    Usage: genpyi module [-h] [--out-dir OUT\_DIR]
    package\_dir

    Positional arguments: package\_dir Package directory to create
    **init**.pyi

    Optional arguments: -h, --help show this help message and exit --out-dir
    OUT\_DIR Output directory. If the option is unset, **init**.pyi will be
    generated in the same directory as package\_dir. 