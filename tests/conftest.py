import os

import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest


def pytest_addoption(parser):
    # type: (Parser) -> None
    parser.addoption(
        "--ros-root",
        help="Root directory of a ROS distribution",
        default="/opt/ros/noetic",
    )
    parser.addoption(
        "--python-version",
        help="Python version for finding ROS libraries",
        default="3",
    )


@pytest.fixture
def ros_root_directory(request):
    # type: (SubRequest) -> str
    return str(request.config.getoption("--ros-root"))


@pytest.fixture
def ros_share_directory(ros_root_directory):
    # type: (str) -> str
    return os.path.join(ros_root_directory, "share")


@pytest.fixture
def ros_python_library_directory(request, ros_root_directory):
    # type: (SubRequest, str) -> str
    py_version = request.config.getoption("--python-version")
    return os.path.join(
        ros_root_directory, "lib/python{}/dist-packages".format(py_version)
    )


@pytest.fixture
def std_msgs_path(ros_share_directory):
    # type: (str) -> str
    return os.path.join(ros_share_directory, "std_msgs")


@pytest.fixture
def std_msgs_py_path(ros_python_library_directory):
    # type: (str) -> str
    return os.path.join(ros_python_library_directory, "std_msgs")


@pytest.fixture
def sensor_msgs_path(ros_share_directory):
    # type: (str) -> str
    return os.path.join(ros_share_directory, "sensor_msgs")


@pytest.fixture
def sensor_msgs_py_path(ros_python_library_directory):
    # type: (str) -> str
    return os.path.join(ros_python_library_directory, "sensor_msgs")


@pytest.fixture
def geometry_msgs_path(ros_share_directory):
    # type: (str) -> str
    return os.path.join(ros_share_directory, "geometry_msgs")


@pytest.fixture
def nav_msgs_path(ros_share_directory):
    # type: (str) -> str
    return os.path.join(ros_share_directory, "nav_msgs")
