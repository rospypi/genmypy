import types
import typing

import genpy
import sensor_msgs.msg
import std_msgs.msg

class PointCloud2(genpy.Message):
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
    fields: typing.List[sensor_msgs.msg.PointField]
    is_bigendian: bool
    point_step: int
    row_step: int
    data: bytes
    is_dense: bool

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        height: int = ...,
        width: int = ...,
        fields: typing.List[sensor_msgs.msg.PointField] = ...,
        is_bigendian: bool = ...,
        point_step: int = ...,
        row_step: int = ...,
        data: bytes = ...,
        is_dense: bool = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> PointCloud2: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> PointCloud2: ...
