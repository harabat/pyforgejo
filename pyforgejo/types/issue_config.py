# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .issue_config_contact_link import IssueConfigContactLink
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class IssueConfig(UniversalBaseModel):
    blank_issues_enabled: typing.Optional[bool] = None
    contact_links: typing.Optional[typing.List[IssueConfigContactLink]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
