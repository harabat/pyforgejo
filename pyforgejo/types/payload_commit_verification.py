# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payload_user import PayloadUser


class PayloadCommitVerification(UniversalBaseModel):
    """
    PayloadCommitVerification represents the GPG verification of a commit
    """

    payload: typing.Optional[str] = None
    reason: typing.Optional[str] = None
    signature: typing.Optional[str] = None
    signer: typing.Optional[PayloadUser] = None
    verified: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
