# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GeneralRepoSettings(UniversalBaseModel):
    """
    GeneralRepoSettings contains global repository settings exposed by API
    """

    forks_disabled: typing.Optional[bool] = None
    http_git_disabled: typing.Optional[bool] = None
    lfs_disabled: typing.Optional[bool] = None
    migrations_disabled: typing.Optional[bool] = None
    mirrors_disabled: typing.Optional[bool] = None
    stars_disabled: typing.Optional[bool] = None
    time_tracking_disabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
