from typing import List, Tuple

from genpyi._compat import lru_cache
from genpyi.stub_element import ImportsElement


def test_lru_cache():
    # type: () -> None
    called = []  # type: List[Tuple[str, str, ImportsElement]]

    @lru_cache()
    def func(module, name, imports):
        # type: (str, str, ImportsElement) -> str
        called.append((module, name, imports))
        return "from {} import {}".format(module, name)

    session1 = ImportsElement()
    assert func("typing", "List", session1) == "from typing import List"
    assert called == [("typing", "List", session1)]

    assert func("typing", "List", session1) == "from typing import List"
    assert called == [("typing", "List", session1)]

    assert func("typing", "Optional", session1) == "from typing import Optional"
    assert called == [("typing", "List", session1), ("typing", "Optional", session1)]

    # Ensure that lru_cache doesn't care the contents of a reference object
    session1.add_system_module("typing", None)
    assert func("typing", "Optional", session1) == "from typing import Optional"
    assert called == [("typing", "List", session1), ("typing", "Optional", session1)]

    session2 = ImportsElement()
    assert func("typing", "Optional", session2) == "from typing import Optional"
    assert called == [
        ("typing", "List", session1),
        ("typing", "Optional", session1),
        ("typing", "Optional", session2),
    ]
