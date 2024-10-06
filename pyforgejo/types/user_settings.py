# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UserSettings(UniversalBaseModel):
    """
    UserSettings represents user settings
    """

    description: typing.Optional[str] = None
    diff_view_style: typing.Optional[str] = None
    enable_repo_unit_hints: typing.Optional[bool] = None
    full_name: typing.Optional[str] = None
    hide_activity: typing.Optional[bool] = None
    hide_email: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Privacy
    """

    language: typing.Optional[str] = None
    location: typing.Optional[str] = None
    pronouns: typing.Optional[str] = None
    theme: typing.Optional[str] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
