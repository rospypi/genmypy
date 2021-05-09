import types
import typing

import genpy
import std_msgs.msg

class Image(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    height: int
    width: int
    encoding: str
    is_bigendian: int
    step: int
    data: bytes

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        height: int = ...,
        width: int = ...,
        encoding: str = ...,
        is_bigendian: int = ...,
        step: int = ...,
        data: bytes = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Image: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Image: ...
