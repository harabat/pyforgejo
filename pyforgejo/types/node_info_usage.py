# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from .node_info_usage_users import NodeInfoUsageUsers
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class NodeInfoUsage(UniversalBaseModel):
    """
    NodeInfoUsage contains usage statistics for this server
    """

    local_comments: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="localComments")
    ] = None
    local_posts: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="localPosts")
    ] = None
    users: typing.Optional[NodeInfoUsageUsers] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
