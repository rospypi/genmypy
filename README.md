# genpy\_stubgen

A Python stub generator from genmsg specs

## Installation

```sh
pip install genpy-stubgen
```

## Usage

### catkin

Add `genpyi` along with `message_generation` to `find_package` in CMakeLists.txt.
`genmsg` will find `genpyi` automatically when building msg/srv files.

Also, keep in mind that your package should have the build dependency for `genpyi` in `package.xml`
to make sure that catkin finishes the build of `genpyi` before building your package.

Examples:

- CMakeLists.txt
  ```cmake
  find_package(catkin REQUIRED COMPONENTS std_msgs message_generation genpyi)
  ```
- package.xml
  ```xml
  <build_depend>genpyi</build_depend>
  ```

### CLI

```
$ genpy_stubgen --help
Usage: genpy_stubgen [-h] {msg,srv,module} ...
positional arguments:
  {msg,srv,module}
    msg             Generate stub files from .msg files
    srv             Generate stub files from .srv files
    module          Generate __init__.pyi from a msg/srv directory

optional arguments:
  -h, --help        show this help message and exit
```

Examples:
```sh
# Message files
$ genpy_stubgen msg custom_msgs custom_msgs/msg/Custom.msg
$ genpy_stubgen msg std_msgs --out-dir out /opt/ros/melodic/share/std_msgs/msg/Header.msg
$ genpy_stubgen msg sensor_msgs --out-dir out \
    -Istd_msgs:/opt/ros/melodic/share/std_msgs/msg \
    -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/msg \
    /opt/ros/melodic/share/sensor_msgs/msg/PointCloud2.msg

# Service files
$ genpy_stubgen srv custom_msgs custom_msgs/srv/Custom.msg
$ genpy_stubgen srv nav_msgs --out-dir out \
    -Istd_msgs:/opt/ros/melodic/share/std_msgs/msg \
    -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/msg \
    /opt/ros/melodic/share/sensor_msgs/srv/SetCameraInfo.srv
```

- `genpy_stubgen msg` / `genpy_stubgen srv`
  ```sh
  Usage: genpy_stubgen {msg,srv} [-h] [--out-dir OUT_DIR]
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
  ```
- `genpy_stubgen module`
  ```sh
  Usage: genpy_stubgen module [-h] [--out-dir OUT_DIR] package_dir

  Positional arguments:
    package_dir        Package directory to create __init__.pyi

  Optional arguments:
    -h, --help         show this help message and exit
    --out-dir OUT_DIR  Output directory. If the option is unset, __init__.pyi
                       will be generated in the same directory as package_dir.
  ```
