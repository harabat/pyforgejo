# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .gpg_key_email import GpgKeyEmail
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class GpgKey(UniversalBaseModel):
    """
    GPGKey a user GPG key to sign commit and tag in repository
    """

    can_certify: typing.Optional[bool] = None
    can_encrypt_comms: typing.Optional[bool] = None
    can_encrypt_storage: typing.Optional[bool] = None
    can_sign: typing.Optional[bool] = None
    created_at: typing.Optional[dt.datetime] = None
    emails: typing.Optional[typing.List[GpgKeyEmail]] = None
    expires_at: typing.Optional[dt.datetime] = None
    id: typing.Optional[int] = None
    key_id: typing.Optional[str] = None
    primary_key_id: typing.Optional[str] = None
    public_key: typing.Optional[str] = None
    subkeys: typing.Optional[typing.List["GpgKey"]] = None
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


update_forward_refs(GpgKey)