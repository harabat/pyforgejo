# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class GeneralAttachmentSettings(UniversalBaseModel):
    """
    GeneralAttachmentSettings contains global Attachment settings exposed by API
    """

    allowed_types: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    max_files: typing.Optional[int] = None
    max_size: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow