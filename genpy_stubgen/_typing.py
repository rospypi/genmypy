TYPING_DISABLED = False
try:
    import typing

    TYPE_CHECKING = typing.TYPE_CHECKING
except ImportError:
    TYPING_DISABLED = True
    TYPE_CHECKING = False
