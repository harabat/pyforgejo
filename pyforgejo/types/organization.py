# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Organization(UniversalBaseModel):
    """
    Organization represents an organization
    """

    avatar_url: typing.Optional[str] = None
    description: typing.Optional[str] = None
    email: typing.Optional[str] = None
    full_name: typing.Optional[str] = None
    id: typing.Optional[int] = None
    location: typing.Optional[str] = None
    name: typing.Optional[str] = None
    repo_admin_change_team_access: typing.Optional[bool] = None
    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    deprecated
    """

    visibility: typing.Optional[str] = None
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