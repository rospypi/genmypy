import os
from typing import Optional


def message_path(path, message_name=None):
    # type: (str, Optional[str]) -> str
    ret = os.path.join(path, "msg")
    if message_name is None:
        return ret

    return os.path.join(ret, "{}.msg".format(message_name))


def service_path(path, service_name=None):
    # type: (str, Optional[str]) -> str
    ret = os.path.join(path, "srv")
    if service_name is None:
        return ret

    return os.path.join(ret, "{}.srv".format(service_name))


def assert_output_equals(expeced_dir, actual_dir, filename):
    # type: (str, str, str) -> None
    expected_path = os.path.join(expeced_dir, filename)
    actual_path = os.path.join(actual_dir, filename)

    assert os.path.exists(expected_path), "Expected file not found"
    assert os.path.exists(actual_path), "File is not generated with the expected name"

    with open(expected_path) as f:
        expected = f.read()

    with open(actual_path) as f:
        actual = f.read()

    assert expected == actual
