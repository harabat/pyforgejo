# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .commit_meta import CommitMeta
from .commit_user import CommitUser
from .payload_commit_verification import PayloadCommitVerification


class RepoCommit(UniversalBaseModel):
    author: typing.Optional[CommitUser] = None
    committer: typing.Optional[CommitUser] = None
    message: typing.Optional[str] = None
    tree: typing.Optional[CommitMeta] = None
    url: typing.Optional[str] = None
    verification: typing.Optional[PayloadCommitVerification] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
