# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .commit_date_options import CommitDateOptions
from .identity import Identity


class UpdateFileOptions(UniversalBaseModel):
    """
    UpdateFileOptions options for updating files
    Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)
    """

    author: typing.Optional[Identity] = None
    branch: typing.Optional[str] = pydantic.Field(default=None)
    """
    branch (optional) to base this file from. if not given, the default branch is used
    """

    committer: typing.Optional[Identity] = None
    content: str = pydantic.Field()
    """
    content must be base64 encoded
    """

    dates: typing.Optional[CommitDateOptions] = None
    from_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    from_path (optional) is the path of the original file which will be moved/renamed to the path in the URL
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    message (optional) for the commit of this file. if not supplied, a default message will be used
    """

    new_branch: typing.Optional[str] = pydantic.Field(default=None)
    """
    new_branch (optional) will make a new branch from `branch` before creating the file
    """

    sha: str = pydantic.Field()
    """
    sha is the SHA for the file that already exists
    """

    signoff: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Add a Signed-off-by trailer by the committer at the end of the commit log message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
