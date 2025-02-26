# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .commit_user import CommitUser
import datetime as dt
from .commit_meta import CommitMeta
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class FileCommitResponse(UniversalBaseModel):
    author: typing.Optional[CommitUser] = None
    committer: typing.Optional[CommitUser] = None
    created: typing.Optional[dt.datetime] = None
    html_url: typing.Optional[str] = None
    message: typing.Optional[str] = None
    parents: typing.Optional[typing.List[CommitMeta]] = None
    sha: typing.Optional[str] = None
    tree: typing.Optional[CommitMeta] = None
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
