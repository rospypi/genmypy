import types
import typing

import genpy
import geometry_msgs.msg
import nav_msgs.msg

class SetMapRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    map: nav_msgs.msg.OccupancyGrid
    initial_pose: geometry_msgs.msg.PoseWithCovarianceStamped

    def __init__(
        self,
        map: nav_msgs.msg.OccupancyGrid = ...,
        initial_pose: geometry_msgs.msg.PoseWithCovarianceStamped = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SetMapRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetMapRequest: ...

class SetMapResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    success: bool

    def __init__(self, success: bool = ..., *args: typing.Any, **kwds: typing.Any) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SetMapResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetMapResponse: ...

class SetMap(object):
    _type: str
    _md5sum: str
    _request_class = SetMapRequest
    _response_class = SetMapResponse
