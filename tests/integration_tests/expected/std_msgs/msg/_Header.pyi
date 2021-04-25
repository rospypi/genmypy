import types
import typing

import genpy

class Header(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    seq: int
    stamp: genpy.Time
    frame_id: str

    def __init__(
        self,
        seq: int = ...,
        stamp: genpy.Time = ...,
        frame_id: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.StringIO) -> None: ...
    def deserialize(self, str: str) -> Header: ...
    def serialize_numpy(self, buff: typing.StringIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: str, numpy: types.ModuleType) -> Header: ...
