# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .user import User
from .team import Team
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class RepoTransfer(UniversalBaseModel):
    """
    RepoTransfer represents a pending repo transfer
    """

    doer: typing.Optional[User] = None
    recipient: typing.Optional[User] = None
    teams: typing.Optional[typing.List[Team]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow