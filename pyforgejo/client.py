# This file was auto-generated by Fern from our API Definition.

import os
import typing

import httpx
from dotenv import load_dotenv

from .activitypub.client import ActivitypubClient, AsyncActivitypubClient
from .admin.client import AdminClient, AsyncAdminClient
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import PyforgejoApiEnvironment
from .issue.client import AsyncIssueClient, IssueClient
from .miscellaneous.client import AsyncMiscellaneousClient, MiscellaneousClient
from .notification.client import AsyncNotificationClient, NotificationClient
from .organization.client import AsyncOrganizationClient, OrganizationClient
from .package.client import AsyncPackageClient, PackageClient
from .repository.client import AsyncRepositoryClient, RepositoryClient
from .settings.client import AsyncSettingsClient, SettingsClient
from .user.client import AsyncUserClient, UserClient

# load environment variables at the beginning
load_dotenv()

# get environment variables with default values
BASE_URL = os.getenv("BASE_URL", "")
API_KEY = os.getenv("API_KEY", "")


class PyforgejoApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client. Defaults to BASE_URL from .env file.

    environment : PyforgejoApiEnvironment
        The environment to use for requests from the client. from .environment import PyforgejoApiEnvironment

        Defaults to PyforgejoApiEnvironment.DEFAULT

    api_key : typing.Optional[str]
        The API key to use for authentication. Defaults to API_KEY from .env file.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from pyforgejo import PyforgejoApi

    client = PyforgejoApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: PyforgejoApiEnvironment = PyforgejoApiEnvironment.DEFAULT,
        api_key: typing.Optional[str] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        base_url = base_url or BASE_URL
        api_key = api_key or API_KEY

        if not base_url:
            raise ValueError(
                "base_url must be provided either as an .env variable or as an argument"
            )
        if not api_key:
            raise ValueError(
                "api_key must be provided either as an .env variable or as an argument"
            )

        _defaulted_timeout = (
            timeout
            if timeout is not None
            else 60
            if httpx_client is None
            else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(
                timeout=_defaulted_timeout, follow_redirects=follow_redirects
            )
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.activitypub = ActivitypubClient(client_wrapper=self._client_wrapper)
        self.admin = AdminClient(client_wrapper=self._client_wrapper)
        self.miscellaneous = MiscellaneousClient(client_wrapper=self._client_wrapper)
        self.notification = NotificationClient(client_wrapper=self._client_wrapper)
        self.organization = OrganizationClient(client_wrapper=self._client_wrapper)
        self.package = PackageClient(client_wrapper=self._client_wrapper)
        self.issue = IssueClient(client_wrapper=self._client_wrapper)
        self.repository = RepositoryClient(client_wrapper=self._client_wrapper)
        self.settings = SettingsClient(client_wrapper=self._client_wrapper)
        self.user = UserClient(client_wrapper=self._client_wrapper)


class AsyncPyforgejoApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client. Defaults to BASE_URL from .env file.

    environment : PyforgejoApiEnvironment
        The environment to use for requests from the client. from .environment import PyforgejoApiEnvironment

        Defaults to PyforgejoApiEnvironment.DEFAULT

    api_key : typing.Optional[str]
        The API key to use for authentication. Defaults to API_KEY from .env file.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from pyforgejo import AsyncPyforgejoApi

    client = AsyncPyforgejoApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: PyforgejoApiEnvironment = PyforgejoApiEnvironment.DEFAULT,
        api_key: typing.Optional[str] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        base_url = base_url or BASE_URL
        api_key = api_key or API_KEY

        print(f"Using BASE_URL: {base_url if base_url else 'Not set'}")
        print(f"Using API_KEY: {'*' * 40 if api_key else 'Not set'}")

        if not base_url:
            raise ValueError(
                "base_url must be provided either as an .env variable or as an argument"
            )
        if not api_key:
            raise ValueError(
                "api_key must be provided either as an .env variable or as an argument"
            )

        _defaulted_timeout = (
            timeout
            if timeout is not None
            else 60
            if httpx_client is None
            else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(
                timeout=_defaulted_timeout, follow_redirects=follow_redirects
            )
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.activitypub = AsyncActivitypubClient(client_wrapper=self._client_wrapper)
        self.admin = AsyncAdminClient(client_wrapper=self._client_wrapper)
        self.miscellaneous = AsyncMiscellaneousClient(
            client_wrapper=self._client_wrapper
        )
        self.notification = AsyncNotificationClient(client_wrapper=self._client_wrapper)
        self.organization = AsyncOrganizationClient(client_wrapper=self._client_wrapper)
        self.package = AsyncPackageClient(client_wrapper=self._client_wrapper)
        self.issue = AsyncIssueClient(client_wrapper=self._client_wrapper)
        self.repository = AsyncRepositoryClient(client_wrapper=self._client_wrapper)
        self.settings = AsyncSettingsClient(client_wrapper=self._client_wrapper)
        self.user = AsyncUserClient(client_wrapper=self._client_wrapper)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: PyforgejoApiEnvironment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception(
            "Please pass in either base_url or environment to construct the client"
        )
