# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class QuotaUsedSizeRepos(UniversalBaseModel):
    """
    QuotaUsedSizeRepos represents the size-based repository quota usage of a user
    """

    private: typing.Optional[int] = pydantic.Field(default=None)
    """
    Storage size of the user's private repositories
    """

    public: typing.Optional[int] = pydantic.Field(default=None)
    """
    Storage size of the user's public repositories
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
