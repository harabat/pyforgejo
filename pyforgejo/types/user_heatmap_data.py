# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .time_stamp import TimeStamp
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class UserHeatmapData(UniversalBaseModel):
    """
    UserHeatmapData represents the data needed to create a heatmap
    """

    contributions: typing.Optional[int] = None
    timestamp: typing.Optional[TimeStamp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
