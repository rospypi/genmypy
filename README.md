# genpy\_stubgen

A Python stub generator from genmsg specs

## Installation

```sh
pip install genpy-stubgen
```

## Usage

### CLI

```
$ genpy_stubgen --help
Usage: genpy_stubgen [-h] [--out-dir OUT_DIR] [--include-path INCLUDE_PATH]
                     {srv,msg} package files [files ...]

positional arguments:
  {srv,msg}             Type of given files
  package               Package name of given files
  files                 Files to generate stubs

optional arguments:
  -h, --help            show this help message and exit
  --out-dir OUT_DIR     Output directory.If the option is unset, each stub
                        file will be generated in the same directory as each
                        input.
  --include-path INCLUDE_PATH, -I INCLUDE_PATH
                        Include paths for processing given files
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

### CMake

**TODO**

Call `generate_genpy_stub` along with `generate_messages` and `add_service_files`.

Examples:
```cmake
generate_genpy_stub(
  DEPENDENCIES
  std_msgs
  geometry_msgs
  MESSAGES
  Custom.msg
  SERVICES
  CustomService.srv
)
```
