# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .attachment_type import AttachmentType
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Attachment(UniversalBaseModel):
    """
    Attachment a generic attachment
    """

    browser_download_url: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    download_count: typing.Optional[int] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    size: typing.Optional[int] = None
    type: typing.Optional[AttachmentType] = None
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow