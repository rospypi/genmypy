import os

import pytest

INTEGRATION_TEST_DIR = os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture
def expected_dir():
    # type: () -> str
    return os.path.join(INTEGRATION_TEST_DIR, "expected")
