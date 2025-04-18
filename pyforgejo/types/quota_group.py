# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quota_rule_info import QuotaRuleInfo


class QuotaGroup(UniversalBaseModel):
    """
    QuotaGroup represents a quota group
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the group
    """

    rules: typing.Optional[typing.List[QuotaRuleInfo]] = pydantic.Field(default=None)
    """
    Rules associated with the group
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
