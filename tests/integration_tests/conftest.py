import os

import pytest

INTEGRATION_TEST_DIR = os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture
def ros_share_directory():
    # type: () -> str
    return "/opt/ros/melodic/share/"


@pytest.fixture
def ros_python_library_directory():
    # type: () -> str
    return "/opt/ros/melodic/lib/python2.7/dist-packages/"


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


@pytest.fixture
def expected_dir():
    # type: () -> str
    return os.path.join(INTEGRATION_TEST_DIR, "expected")
