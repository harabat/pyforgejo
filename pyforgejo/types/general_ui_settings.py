# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GeneralUiSettings(UniversalBaseModel):
    """
    GeneralUISettings contains global ui settings exposed by API
    """

    allowed_reactions: typing.Optional[typing.List[str]] = None
    custom_emojis: typing.Optional[typing.List[str]] = None
    default_theme: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
