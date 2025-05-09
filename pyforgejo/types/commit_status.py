# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .commit_status_state import CommitStatusState
from .user import User


class CommitStatus(UniversalBaseModel):
    """
    CommitStatus holds a single status of a single Commit
    """

    context: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    creator: typing.Optional[User] = None
    description: typing.Optional[str] = None
    id: typing.Optional[int] = None
    status: typing.Optional[CommitStatusState] = None
    target_url: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
