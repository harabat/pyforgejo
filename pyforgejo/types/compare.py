# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .commit import Commit
from .commit_affected_files import CommitAffectedFiles


class Compare(UniversalBaseModel):
    commits: typing.Optional[typing.List[Commit]] = None
    files: typing.Optional[typing.List[CommitAffectedFiles]] = None
    total_commits: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
