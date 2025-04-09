# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.notification_count import NotificationCount
from ..types.notification_thread import NotificationThread
from .types.notify_get_list_request_subject_type_item import \
    NotifyGetListRequestSubjectTypeItem
from .types.notify_get_repo_list_request_subject_type_item import \
    NotifyGetRepoListRequestSubjectTypeItem


class RawNotificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def notify_get_list(
        self,
        *,
        all_: typing.Optional[bool] = None,
        status_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        subject_type: typing.Optional[
            typing.Union[
                NotifyGetListRequestSubjectTypeItem,
                typing.Sequence[NotifyGetListRequestSubjectTypeItem],
            ]
        ] = None,
        since: typing.Optional[dt.datetime] = None,
        before: typing.Optional[dt.datetime] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NotificationThread]]:
        """
        Parameters
        ----------
        all_ : typing.Optional[bool]
            If true, show notifications marked as read. Default value is false

        status_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned.

        subject_type : typing.Optional[typing.Union[NotifyGetListRequestSubjectTypeItem, typing.Sequence[NotifyGetListRequestSubjectTypeItem]]]
            filter notifications by subject type

        since : typing.Optional[dt.datetime]
            Only show notifications updated after the given time. This is a timestamp in RFC 3339 format

        before : typing.Optional[dt.datetime]
            Only show notifications updated before the given time. This is a timestamp in RFC 3339 format

        page : typing.Optional[int]
            page number of results to return (1-based)

        limit : typing.Optional[int]
            page size of results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[NotificationThread]]
            NotificationThreadList
        """
        _response = self._client_wrapper.httpx_client.request(
            "notifications",
            method="GET",
            params={
                "all": all_,
                "status-types": status_types,
                "subject-type": subject_type,
                "since": serialize_datetime(since) if since is not None else None,
                "before": serialize_datetime(before) if before is not None else None,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationThread],
                    parse_obj_as(
                        type_=typing.List[NotificationThread],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def notify_read_list(
        self,
        *,
        last_read_at: typing.Optional[dt.datetime] = None,
        all_: typing.Optional[str] = None,
        status_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        to_status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        last_read_at : typing.Optional[dt.datetime]
            Describes the last point that notifications were checked. Anything updated since this time will not be updated.

        all_ : typing.Optional[str]
            If true, mark all notifications on this repo. Default value is false

        status_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.

        to_status : typing.Optional[str]
            Status to mark notifications as, Defaults to read.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "notifications",
            method="PUT",
            params={
                "last_read_at": serialize_datetime(last_read_at)
                if last_read_at is not None
                else None,
                "all": all_,
                "status-types": status_types,
                "to-status": to_status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def notify_new_available(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NotificationCount]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationCount]
            Number of unread notifications
        """
        _response = self._client_wrapper.httpx_client.request(
            "notifications/new",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationCount,
                    parse_obj_as(
                        type_=NotificationCount,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def notify_get_thread(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NotificationThread]:
        """
        Parameters
        ----------
        id : str
            id of notification thread

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationThread]
            NotificationThread
        """
        _response = self._client_wrapper.httpx_client.request(
            f"notifications/threads/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationThread,
                    parse_obj_as(
                        type_=NotificationThread,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def notify_read_thread(
        self,
        id: str,
        *,
        to_status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            id of notification thread

        to_status : typing.Optional[str]
            Status to mark notifications as

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"notifications/threads/{jsonable_encoder(id)}",
            method="PATCH",
            params={
                "to-status": to_status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def notify_get_repo_list(
        self,
        owner: str,
        repo: str,
        *,
        all_: typing.Optional[bool] = None,
        status_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        subject_type: typing.Optional[
            typing.Union[
                NotifyGetRepoListRequestSubjectTypeItem,
                typing.Sequence[NotifyGetRepoListRequestSubjectTypeItem],
            ]
        ] = None,
        since: typing.Optional[dt.datetime] = None,
        before: typing.Optional[dt.datetime] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[NotificationThread]]:
        """
        Parameters
        ----------
        owner : str
            owner of the repo

        repo : str
            name of the repo

        all_ : typing.Optional[bool]
            If true, show notifications marked as read. Default value is false

        status_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned

        subject_type : typing.Optional[typing.Union[NotifyGetRepoListRequestSubjectTypeItem, typing.Sequence[NotifyGetRepoListRequestSubjectTypeItem]]]
            filter notifications by subject type

        since : typing.Optional[dt.datetime]
            Only show notifications updated after the given time. This is a timestamp in RFC 3339 format

        before : typing.Optional[dt.datetime]
            Only show notifications updated before the given time. This is a timestamp in RFC 3339 format

        page : typing.Optional[int]
            page number of results to return (1-based)

        limit : typing.Optional[int]
            page size of results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[NotificationThread]]
            NotificationThreadList
        """
        _response = self._client_wrapper.httpx_client.request(
            f"repos/{jsonable_encoder(owner)}/{jsonable_encoder(repo)}/notifications",
            method="GET",
            params={
                "all": all_,
                "status-types": status_types,
                "subject-type": subject_type,
                "since": serialize_datetime(since) if since is not None else None,
                "before": serialize_datetime(before) if before is not None else None,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationThread],
                    parse_obj_as(
                        type_=typing.List[NotificationThread],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def notify_read_repo_list(
        self,
        owner: str,
        repo: str,
        *,
        all_: typing.Optional[str] = None,
        status_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        to_status: typing.Optional[str] = None,
        last_read_at: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        owner : str
            owner of the repo

        repo : str
            name of the repo

        all_ : typing.Optional[str]
            If true, mark all notifications on this repo. Default value is false

        status_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.

        to_status : typing.Optional[str]
            Status to mark notifications as. Defaults to read.

        last_read_at : typing.Optional[dt.datetime]
            Describes the last point that notifications were checked. Anything updated since this time will not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"repos/{jsonable_encoder(owner)}/{jsonable_encoder(repo)}/notifications",
            method="PUT",
            params={
                "all": all_,
                "status-types": status_types,
                "to-status": to_status,
                "last_read_at": serialize_datetime(last_read_at)
                if last_read_at is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawNotificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def notify_get_list(
        self,
        *,
        all_: typing.Optional[bool] = None,
        status_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        subject_type: typing.Optional[
            typing.Union[
                NotifyGetListRequestSubjectTypeItem,
                typing.Sequence[NotifyGetListRequestSubjectTypeItem],
            ]
        ] = None,
        since: typing.Optional[dt.datetime] = None,
        before: typing.Optional[dt.datetime] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NotificationThread]]:
        """
        Parameters
        ----------
        all_ : typing.Optional[bool]
            If true, show notifications marked as read. Default value is false

        status_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned.

        subject_type : typing.Optional[typing.Union[NotifyGetListRequestSubjectTypeItem, typing.Sequence[NotifyGetListRequestSubjectTypeItem]]]
            filter notifications by subject type

        since : typing.Optional[dt.datetime]
            Only show notifications updated after the given time. This is a timestamp in RFC 3339 format

        before : typing.Optional[dt.datetime]
            Only show notifications updated before the given time. This is a timestamp in RFC 3339 format

        page : typing.Optional[int]
            page number of results to return (1-based)

        limit : typing.Optional[int]
            page size of results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[NotificationThread]]
            NotificationThreadList
        """
        _response = await self._client_wrapper.httpx_client.request(
            "notifications",
            method="GET",
            params={
                "all": all_,
                "status-types": status_types,
                "subject-type": subject_type,
                "since": serialize_datetime(since) if since is not None else None,
                "before": serialize_datetime(before) if before is not None else None,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationThread],
                    parse_obj_as(
                        type_=typing.List[NotificationThread],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def notify_read_list(
        self,
        *,
        last_read_at: typing.Optional[dt.datetime] = None,
        all_: typing.Optional[str] = None,
        status_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        to_status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        last_read_at : typing.Optional[dt.datetime]
            Describes the last point that notifications were checked. Anything updated since this time will not be updated.

        all_ : typing.Optional[str]
            If true, mark all notifications on this repo. Default value is false

        status_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.

        to_status : typing.Optional[str]
            Status to mark notifications as, Defaults to read.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "notifications",
            method="PUT",
            params={
                "last_read_at": serialize_datetime(last_read_at)
                if last_read_at is not None
                else None,
                "all": all_,
                "status-types": status_types,
                "to-status": to_status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def notify_new_available(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NotificationCount]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationCount]
            Number of unread notifications
        """
        _response = await self._client_wrapper.httpx_client.request(
            "notifications/new",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationCount,
                    parse_obj_as(
                        type_=NotificationCount,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def notify_get_thread(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NotificationThread]:
        """
        Parameters
        ----------
        id : str
            id of notification thread

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationThread]
            NotificationThread
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"notifications/threads/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationThread,
                    parse_obj_as(
                        type_=NotificationThread,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def notify_read_thread(
        self,
        id: str,
        *,
        to_status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            id of notification thread

        to_status : typing.Optional[str]
            Status to mark notifications as

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"notifications/threads/{jsonable_encoder(id)}",
            method="PATCH",
            params={
                "to-status": to_status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def notify_get_repo_list(
        self,
        owner: str,
        repo: str,
        *,
        all_: typing.Optional[bool] = None,
        status_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        subject_type: typing.Optional[
            typing.Union[
                NotifyGetRepoListRequestSubjectTypeItem,
                typing.Sequence[NotifyGetRepoListRequestSubjectTypeItem],
            ]
        ] = None,
        since: typing.Optional[dt.datetime] = None,
        before: typing.Optional[dt.datetime] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[NotificationThread]]:
        """
        Parameters
        ----------
        owner : str
            owner of the repo

        repo : str
            name of the repo

        all_ : typing.Optional[bool]
            If true, show notifications marked as read. Default value is false

        status_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned

        subject_type : typing.Optional[typing.Union[NotifyGetRepoListRequestSubjectTypeItem, typing.Sequence[NotifyGetRepoListRequestSubjectTypeItem]]]
            filter notifications by subject type

        since : typing.Optional[dt.datetime]
            Only show notifications updated after the given time. This is a timestamp in RFC 3339 format

        before : typing.Optional[dt.datetime]
            Only show notifications updated before the given time. This is a timestamp in RFC 3339 format

        page : typing.Optional[int]
            page number of results to return (1-based)

        limit : typing.Optional[int]
            page size of results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[NotificationThread]]
            NotificationThreadList
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"repos/{jsonable_encoder(owner)}/{jsonable_encoder(repo)}/notifications",
            method="GET",
            params={
                "all": all_,
                "status-types": status_types,
                "subject-type": subject_type,
                "since": serialize_datetime(since) if since is not None else None,
                "before": serialize_datetime(before) if before is not None else None,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationThread],
                    parse_obj_as(
                        type_=typing.List[NotificationThread],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def notify_read_repo_list(
        self,
        owner: str,
        repo: str,
        *,
        all_: typing.Optional[str] = None,
        status_types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        to_status: typing.Optional[str] = None,
        last_read_at: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        owner : str
            owner of the repo

        repo : str
            name of the repo

        all_ : typing.Optional[str]
            If true, mark all notifications on this repo. Default value is false

        status_types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.

        to_status : typing.Optional[str]
            Status to mark notifications as. Defaults to read.

        last_read_at : typing.Optional[dt.datetime]
            Describes the last point that notifications were checked. Anything updated since this time will not be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"repos/{jsonable_encoder(owner)}/{jsonable_encoder(repo)}/notifications",
            method="PUT",
            params={
                "all": all_,
                "status-types": status_types,
                "to-status": to_status,
                "last_read_at": serialize_datetime(last_read_at)
                if last_read_at is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
