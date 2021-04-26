import os
import tempfile
from typing import Dict, List

from genpy_stubgen.cli import run_module_stubgen

from .utils import assert_output_equals, message_path, service_path


def test_std_msgs_msg(expected_dir, std_msgs_path):
    # type: (str, str) -> None
    package = "std_msgs"  # type: str
    package_dir = message_path(std_msgs_path)
    expected_dir = os.path.join(expected_dir, package, "msg")

    with tempfile.TemporaryDirectory() as td:
        run_module_stubgen(package_dir, td)

        assert_output_equals(expected_dir, td, "__init__.pyi")


def test_sensor_msgs_srv(expected_dir, std_msgs_path, sensor_msgs_path):
    # type: (str, str, str) -> None
    package = "sensor_msgs"  # type: str
    package_dir = service_path(sensor_msgs_path)
    expected_dir = os.path.join(expected_dir, package, "srv")

    with tempfile.TemporaryDirectory() as td:
        run_module_stubgen(package_dir, td)

        assert_output_equals(expected_dir, td, "__init__.pyi")
