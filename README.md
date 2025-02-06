# pyforgejo

A Python client library for accessing the [Forgejo](https://forgejo.org/) API.

**:warning: pyforgejo 2.0 introduces significant changes**

## Usage

1. Create an `.env` file in your project directory with the `BASE_URL` and your `API_KEY`:

``` yaml
BASE_URL=https://codeberg.org/api/v1
API_KEY='token your_api_key'  # your API token prepended with "token" followed by a space
```

2. Create a client and call an endpoint:

```python
from pyforgejo import PyforgejoApi

client = PyforgejoApi()

# get a specific repo
repo = client.repository.repo_get(owner='harabat', repo='pyforgejo')

repo
# Repository(allow_fast_forward_only_merge=False, allow_merge_commits=True, allow_rebase=True, ...)

repo.dict()
# {'allow_fast_forward_only_merge': False,
#  'allow_merge_commits': True,
#  'allow_rebase': True,
#  ...
# }

# list issues for the repo
issues = client.issue.list_issues(owner=repo.owner.login, repo=repo.name)

[issue.title for issue in issues]
# ['Normalize option model names',
#  'Calling methods from client',
#  '`parsed` is None for most methods',
#  '`openapi-python-client` does not support `text/plain` requests']
```

The client follows this pattern for calling endpoints:

``` python
client.<resource>.<operation_id>(args)
```
where:

- `<resource>`: the API resource (e.g., `repository`, `issue`, `user`)
- `<operation_id>`: the specific operation, derived from the OpenAPI spec's `operationId` (converted to snake_case)

You can find the `resource` and `operation_id` either in the [Swagger spec](https://codeberg.org/swagger.v1.json) or in the [API reference](https://codeberg.org/api/swagger). 

## Installation

1. Clone the repository and navigate to the project directory:

``` shell
git clone https://codeberg.org/harabat/pyforgejo.git
git checkout 2.0
```

2. Create a virtual environment:

``` shell
# using venv (built-in)
python -m venv venv
source venv/bin/activate

# or using conda
conda create --name pyforgejo_2.0 python=3.10 --yes
conda activate pyforgejo_2.0
```

3. Install the package:

``` shell
pip install ./pyforgejo
```

## Forgejo API Resources

- [API Usage | Forgejo](https://forgejo.org/docs/latest/user/api-usage/): user guide for the Forgejo API
- [Forgejo API | Codeberg](https://codeberg.org/api/swagger): API reference for Codeberg
- [Forgejo API Swagger spec | Codeberg](https://codeberg.org/swagger.v1.json): Codeberg's Forgejo API Swagger spec
- [About Swagger Specification | Documentation | Swagger](https://swagger.io/docs/specification/about/): docs for Swagger spec
- [The OpenAPI Specification Explained | OpenAPI Documentation](https://learn.openapis.org/specification/): docs for OpenAPI spec

## Development

### Using `fern`

`pyforgejo` 2.0 is generated with [fern](https://github.com/fern-api/fern), based on a slightly edited Forgejo OpenAPI spec.

The user experience and code architecture of the `fern`-generated client follow best practice. As the library is tested by users, we will identify any issues inherent to `fern` that prove limiting to `pyforgejo`: if we find such issues and cannot patch them upstream, the current codebase provides a good foundation for further development and any divergence from `fern` would not affect the vast majority of usecases.

### Generating the client with `fern`

1. Install fern, initialise a new workspace, and specify `pyforgejo` as the name of your organisation (= client).

``` shell
npm install -g fern-api

fern init --openapi https://code.forgejo.org/swagger.v1.json
# Please enter your organization pyforgejo
```

2. Edit the `fern/openapi/openapi.json` file to keep only `AuthorizationHeaderToken` in `securityDefinitions` and `security`.

``` json
"securityDefinitions": {
  "AuthorizationHeaderToken": {
    "description": "API tokens must be prepended with \"token\" followed by a space.",
    "type": "apiKey",
    "name": "Authorization",
    "in": "header"
  }
},
"security": [
  {
    "AuthorizationHeaderToken": []
  }
]
```

3. Add the Python SDK generator to `fern`.

``` shell
fern add fernapi/fern-python-sdk
```

4. Generate the client (output will be in `sdks/pyforgejo`).

``` shell
fern generate
# you'll have to login to GitHub
```

5. Create a `.env` file in `sdks/pyforgejo` with your `BASE_URL` and `API_KEY`.

``` yml
BASE_URL=https://codeberg.org/api/v1
API_KEY="token your_api_key"
```

6. Modify the `PyforgejoApi` and `AsyncPyforgejoApi` classes in `sdks/pyforgejo/pyforgejo/client.py` to use environment variables.

``` diff
# ...
from .user.client import AsyncUserClient
+import os
+from dotenv import load_dotenv
+
+load_dotenv()
+
+BASE_URL = os.getenv('BASE_URL')
+API_KEY = os.getenv('API_KEY')

 class PyforgejoApi:
# ...
     base_url : typing.Optional[str]
-        The base url to use for requests from the client.
+        The base url to use for requests from the client. Defaults to BASE_URL from .env file.
# ...
-    api_key : str
+    api_key : typing.Optional[str]
+        The API key to use for authentication. Defaults to API_KEY from .env file.
# ...
    def __init__(
# ...
-        api_key: str,
+        api_key: typing.Optional[str] = None,
# ...
     ):
+        base_url = base_url or BASE_URL
+        api_key = api_key or API_KEY
+
+        print(f"Using BASE_URL: {base_url if base_url else 'Not set'}")
+        print(f"Using API_KEY: {'*' * 40 if api_key else 'Not set'}")
+
+        if not base_url:
+            raise ValueError("base_url must be provided either as an .env variable or as an argument")
+        if not api_key:
+            raise ValueError("api_key must be provided either as an .env variable or as an argument")
# same for AsyncPyforgejoApi
```

7. Create a virtual environment and install the lib.

``` shell
conda create --name pyforgejo_dev
conda activate pyforgejo_dev
pip install /path/to/pyforgejo
```

8. Use the client as shown in the [Usage](#usage) section.

``` shell
conda install ipython
ipython
```

``` python
from pyforgejo import PyforgejoApi

client = PyforgejoApi()

user = client.user.get_current()
```
