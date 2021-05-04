import functools

from ._typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Callable, Dict, TypeVar

    TResult = TypeVar("TResult")

try:
    from functools import lru_cache  # type: ignore
except ImportError:
    # Provide a simple cache for Python2
    def lru_cache():
        # type: (...) -> Callable[..., Callable[..., TResult]]
        def _lru_cache(func):
            # type: (Callable[..., TResult]) -> Callable[..., TResult]
            cache = {}  # type: Dict[Any, Any]

            @functools.wraps(func)
            def wrapper(*args):
                # type: (Any) -> TResult
                key = tuple(args)
                if key not in cache:
                    ret = func(*args)
                    cache[key] = ret
                else:
                    ret = cache[key]

                return ret

            return wrapper

        return _lru_cache
