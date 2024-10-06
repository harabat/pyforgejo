# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .repository import Repository
import typing
from .commit_status_state import CommitStatusState
from .commit_status import CommitStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class CombinedStatus(UniversalBaseModel):
    """
    CombinedStatus holds the combined state of several statuses for a single commit
    """

    commit_url: typing.Optional[str] = None
    repository: typing.Optional[Repository] = None
    sha: typing.Optional[str] = None
    state: typing.Optional[CommitStatusState] = None
    statuses: typing.Optional[typing.List[CommitStatus]] = None
    total_count: typing.Optional[int] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Repository, CombinedStatus=CombinedStatus)
