# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .quota_used_attachment_contained_in import QuotaUsedAttachmentContainedIn
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class QuotaUsedAttachment(UniversalBaseModel):
    """
    QuotaUsedAttachment represents an attachment counting towards a user's quota
    """

    api_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    API URL for the attachment
    """

    contained_in: typing.Optional[QuotaUsedAttachmentContainedIn] = pydantic.Field(
        default=None
    )
    """
    Context for the attachment: URLs to the containing object
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filename of the attachment
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the attachment (in bytes)
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
