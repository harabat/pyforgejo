# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .issue_form_field_type import IssueFormFieldType
from .issue_form_field_visible import IssueFormFieldVisible


class IssueFormField(UniversalBaseModel):
    """
    IssueFormField represents a form field
    """

    attributes: typing.Optional[
        typing.Dict[str, typing.Dict[str, typing.Optional[typing.Any]]]
    ] = None
    id: typing.Optional[str] = None
    type: typing.Optional[IssueFormFieldType] = None
    validations: typing.Optional[
        typing.Dict[str, typing.Dict[str, typing.Optional[typing.Any]]]
    ] = None
    visible: typing.Optional[typing.List[IssueFormFieldVisible]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
