# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .tag_archive_download_count import TagArchiveDownloadCount
from .annotated_tag_object import AnnotatedTagObject
from .commit_user import CommitUser
from .payload_commit_verification import PayloadCommitVerification
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AnnotatedTag(UniversalBaseModel):
    """
    AnnotatedTag represents an annotated tag
    """

    archive_download_count: typing.Optional[TagArchiveDownloadCount] = None
    message: typing.Optional[str] = None
    object: typing.Optional[AnnotatedTagObject] = None
    sha: typing.Optional[str] = None
    tag: typing.Optional[str] = None
    tagger: typing.Optional[CommitUser] = None
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
