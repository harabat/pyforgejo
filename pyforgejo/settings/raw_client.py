# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.general_api_settings import GeneralApiSettings
from ..types.general_attachment_settings import GeneralAttachmentSettings
from ..types.general_repo_settings import GeneralRepoSettings
from ..types.general_ui_settings import GeneralUiSettings


class RawSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_general_api_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GeneralApiSettings]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GeneralApiSettings]
            GeneralAPISettings
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/api",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GeneralApiSettings,
                    parse_obj_as(
                        type_=GeneralApiSettings,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_general_attachment_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GeneralAttachmentSettings]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GeneralAttachmentSettings]
            GeneralAttachmentSettings
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GeneralAttachmentSettings,
                    parse_obj_as(
                        type_=GeneralAttachmentSettings,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_general_repository_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GeneralRepoSettings]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GeneralRepoSettings]
            GeneralRepoSettings
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/repository",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GeneralRepoSettings,
                    parse_obj_as(
                        type_=GeneralRepoSettings,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_general_ui_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GeneralUiSettings]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GeneralUiSettings]
            GeneralUISettings
        """
        _response = self._client_wrapper.httpx_client.request(
            "settings/ui",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GeneralUiSettings,
                    parse_obj_as(
                        type_=GeneralUiSettings,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_general_api_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GeneralApiSettings]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GeneralApiSettings]
            GeneralAPISettings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/api",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GeneralApiSettings,
                    parse_obj_as(
                        type_=GeneralApiSettings,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_general_attachment_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GeneralAttachmentSettings]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GeneralAttachmentSettings]
            GeneralAttachmentSettings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/attachment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GeneralAttachmentSettings,
                    parse_obj_as(
                        type_=GeneralAttachmentSettings,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_general_repository_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GeneralRepoSettings]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GeneralRepoSettings]
            GeneralRepoSettings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/repository",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GeneralRepoSettings,
                    parse_obj_as(
                        type_=GeneralRepoSettings,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_general_ui_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GeneralUiSettings]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GeneralUiSettings]
            GeneralUISettings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "settings/ui",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GeneralUiSettings,
                    parse_obj_as(
                        type_=GeneralUiSettings,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
