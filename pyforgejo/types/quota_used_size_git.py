# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class QuotaUsedSizeGit(UniversalBaseModel):
    """
    QuotaUsedSizeGit represents the size-based git (lfs) quota usage of a user
    """

    lfs: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="LFS")
    ] = pydantic.Field(default=None)
    """
    Storage size of the user's Git LFS objects
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