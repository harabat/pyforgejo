# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CreateLabelOption(UniversalBaseModel):
    """
    CreateLabelOption options for creating a label
    """

    color: str
    description: typing.Optional[str] = None
    exclusive: typing.Optional[bool] = None
    is_archived: typing.Optional[bool] = None
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
