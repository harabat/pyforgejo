# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .commit_user import CommitUser
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class WikiCommit(UniversalBaseModel):
    """
    WikiCommit page commit/revision
    """

    author: typing.Optional[CommitUser] = None
    commiter: typing.Optional[CommitUser] = None
    message: typing.Optional[str] = None
    sha: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
