import types
import typing

import genpy

class JoyFeedback(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Constants
    TYPE_LED: int
    TYPE_RUMBLE: int
    TYPE_BUZZER: int

    # Fields
    type: int
    id: int
    intensity: float

    def __init__(
        self,
        type: int = ...,
        id: int = ...,
        intensity: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> JoyFeedback: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> JoyFeedback: ...
