import os
from typing import Dict, List

from genpyi import cli

from .utils import assert_output_equals, message_path, service_path, temporary_directory


def test_sensor_msgs(expected_dir, std_msgs_path, sensor_msgs_path):
    # type: (str, str, str) -> None
    package = "sensor_msgs"  # type: str
    package_files = [
        service_path(sensor_msgs_path, "SetCameraInfo"),
    ]  # type: List[str]
    search_paths = {
        "std_msgs": [message_path(std_msgs_path)],
        "sensor_msgs": [message_path(sensor_msgs_path)],
    }  # type: Dict[str, List[str]]
    expected_dir = os.path.join(expected_dir, package, "srv")

    with temporary_directory() as td:
        cli.run_service(package, package_files, td, search_paths)

        assert_output_equals(expected_dir, td, "_SetCameraInfo.pyi")


def test_nav_msgs(
    expected_dir, std_msgs_path, sensor_msgs_path, geometry_msgs_path, nav_msgs_path
):
    # type: (str, str, str, str, str) -> None
    package = "nav_msgs"  # type: str
    package_files = [
        service_path(nav_msgs_path, "SetMap"),
    ]  # type: List[str]
    search_paths = {
        "std_msgs": [message_path(std_msgs_path)],
        "sensor_msgs": [message_path(sensor_msgs_path)],
        "geometry_msgs": [message_path(geometry_msgs_path)],
        "nav_msgs": [message_path(nav_msgs_path)],
    }  # type: Dict[str, List[str]]
    expected_dir = os.path.join(expected_dir, package, "srv")

    with temporary_directory() as td:
        cli.run_service(package, package_files, td, search_paths)

        assert_output_equals(expected_dir, td, "_SetMap.pyi")
