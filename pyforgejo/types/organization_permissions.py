# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class OrganizationPermissions(UniversalBaseModel):
    """
    OrganizationPermissions list different users permissions on an organization
    """

    can_create_repository: typing.Optional[bool] = None
    can_read: typing.Optional[bool] = None
    can_write: typing.Optional[bool] = None
    is_admin: typing.Optional[bool] = None
    is_owner: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow