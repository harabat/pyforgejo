# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateOAuth2ApplicationOptions(UniversalBaseModel):
    """
    CreateOAuth2ApplicationOptions holds options to create an oauth2 application
    """

    confidential_client: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    redirect_uris: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
