# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BranchProtection(UniversalBaseModel):
    """
    BranchProtection represents a branch protection for a repository
    """

    apply_to_admins: typing.Optional[bool] = None
    approvals_whitelist_teams: typing.Optional[typing.List[str]] = None
    approvals_whitelist_username: typing.Optional[typing.List[str]] = None
    block_on_official_review_requests: typing.Optional[bool] = None
    block_on_outdated_branch: typing.Optional[bool] = None
    block_on_rejected_reviews: typing.Optional[bool] = None
    branch_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: true
    """

    created_at: typing.Optional[dt.datetime] = None
    dismiss_stale_approvals: typing.Optional[bool] = None
    enable_approvals_whitelist: typing.Optional[bool] = None
    enable_merge_whitelist: typing.Optional[bool] = None
    enable_push: typing.Optional[bool] = None
    enable_push_whitelist: typing.Optional[bool] = None
    enable_status_check: typing.Optional[bool] = None
    ignore_stale_approvals: typing.Optional[bool] = None
    merge_whitelist_teams: typing.Optional[typing.List[str]] = None
    merge_whitelist_usernames: typing.Optional[typing.List[str]] = None
    protected_file_patterns: typing.Optional[str] = None
    push_whitelist_deploy_keys: typing.Optional[bool] = None
    push_whitelist_teams: typing.Optional[typing.List[str]] = None
    push_whitelist_usernames: typing.Optional[typing.List[str]] = None
    require_signed_commits: typing.Optional[bool] = None
    required_approvals: typing.Optional[int] = None
    rule_name: typing.Optional[str] = None
    status_check_contexts: typing.Optional[typing.List[str]] = None
    unprotected_file_patterns: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
