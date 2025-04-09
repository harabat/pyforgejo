# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payload_commit import PayloadCommit


class Branch(UniversalBaseModel):
    """
    Branch represents a repository branch
    """

    commit: typing.Optional[PayloadCommit] = None
    effective_branch_protection_name: typing.Optional[str] = None
    enable_status_check: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    protected: typing.Optional[bool] = None
    required_approvals: typing.Optional[int] = None
    status_check_contexts: typing.Optional[typing.List[str]] = None
    user_can_merge: typing.Optional[bool] = None
    user_can_push: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
