# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .issue import Issue
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TrackedTime(UniversalBaseModel):
    """
    TrackedTime worked time for an issue / pr
    """

    created: typing.Optional[dt.datetime] = None
    id: typing.Optional[int] = None
    issue: typing.Optional[Issue] = None
    issue_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    deprecated (only for backwards compatibility)
    """

    time: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time in seconds
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    deprecated (only for backwards compatibility)
    """

    user_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow