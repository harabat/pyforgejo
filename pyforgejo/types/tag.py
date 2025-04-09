# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .commit_meta import CommitMeta
from .tag_archive_download_count import TagArchiveDownloadCount


class Tag(UniversalBaseModel):
    """
    Tag represents a repository tag
    """

    archive_download_count: typing.Optional[TagArchiveDownloadCount] = None
    commit: typing.Optional[CommitMeta] = None
    id: typing.Optional[str] = None
    message: typing.Optional[str] = None
    name: typing.Optional[str] = None
    tarball_url: typing.Optional[str] = None
    zipball_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
