# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user import User


class PullReviewComment(UniversalBaseModel):
    """
    PullReviewComment represents a comment on a pull request review
    """

    body: typing.Optional[str] = None
    commit_id: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    diff_hunk: typing.Optional[str] = None
    html_url: typing.Optional[str] = None
    id: typing.Optional[int] = None
    original_commit_id: typing.Optional[str] = None
    original_position: typing.Optional[int] = None
    path: typing.Optional[str] = None
    position: typing.Optional[int] = None
    pull_request_review_id: typing.Optional[int] = None
    pull_request_url: typing.Optional[str] = None
    resolver: typing.Optional[User] = None
    updated_at: typing.Optional[dt.datetime] = None
    user: typing.Optional[User] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
