import os

from genpyi import cli

from .utils import assert_output_equals, message_path, service_path, temporary_directory


def test_std_msgs_msg(expected_dir, std_msgs_path, std_msgs_py_path):
    # type: (str, str, str) -> None
    package = "std_msgs"  # type: str
    package_dir = message_path(std_msgs_path)
    package_py_dir = message_path(std_msgs_py_path)
    expected_dir = os.path.join(expected_dir, package, "msg")

    with temporary_directory() as td:
        cli.run_module(package_dir, td, "genmsg")

        assert_output_equals(expected_dir, td, "__init__.pyi")

    with temporary_directory() as td:
        cli.run_module(package_py_dir, td, "py")

        assert_output_equals(expected_dir, td, "__init__.pyi")


def test_sensor_msgs_srv(
    expected_dir, std_msgs_path, sensor_msgs_path, sensor_msgs_py_path
):
    # type: (str, str, str, str) -> None
    package = "sensor_msgs"  # type: str
    package_dir = service_path(sensor_msgs_path)
    package_py_dir = service_path(sensor_msgs_py_path)
    expected_dir = os.path.join(expected_dir, package, "srv")

    with temporary_directory() as td:
        cli.run_module(package_dir, td, "genmsg")

        assert_output_equals(expected_dir, td, "__init__.pyi")

    with temporary_directory() as td:
        cli.run_module(package_py_dir, td, "py")

        assert_output_equals(expected_dir, td, "__init__.pyi")
