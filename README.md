# pyforgejo

A Python client library for accessing the [Forgejo](https://forgejo.org/) API.

**:warning: pyforgejo 2.0 introduces significant changes**

## Usage

1. Create an `.env` file in your project directory with the `BASE_URL` and your `API_KEY`:

``` dotenv
BASE_URL=https://codeberg.org/api/v1
API_KEY=your_api_key
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

The user experience and code architecture provided by `fern` correspond to what I was expecting to get while rewriting `pyforgejo` from scratch with `httpx`, so this is a suitable proof of concept.

During the testing phase, we want to identify any issues inherent to `fern` that prove limiting to `pyforgejo`: if we find such issues and cannot patch them upstream, I'll continue the `httpx`-based rewrite. Otherwise we'll adopt `fern` as the generator for `pyforgejo`.

As mentioned, the user experience of the current `fern`-generated client is what I was going for, so even in the case of a rewrite the vast majority of usecases should be preserved.

### Generating the client with `fern`

1. Install fern and init a new workspace:

``` shell
npm install -g fern-api

fern init --openapi https://code.forgejo.org/swagger.v1.json
# login with github
```

2. Edit the `fern/openapi/openapi.yml` file to keep only `AuthorizationHeaderToken` in `securityDefinitions` and `security`.

``` yml
securityDefinitions:
  AuthorizationHeaderToken:
    description: API tokens must be prepended with "token" followed by a space.
    type: apiKey
    name: Authorization
    in: header
security:
  - AuthorizationHeaderToken: []
```

3. Edit the `fern/generators.yml` file to use the Python generator.

``` yml
default-group: local
groups:
  local:
    generators:
      - name: fernapi/fern-python-sdk
        version: 4.2.7
        output:
          location: local-file-system
          path: ../sdks/pyforgejo
api:
  path: openapi/openapi.yml
```

4. Edit the `fern/fern.config.json` to specify `pyforgejo` as the organisation.

``` json
{
    "organization": "pyforgejo",
    "version": "0.44.1"
}
```

5. Generate the client (output will be in `sdks/pyforgejo`).

6. Create a `.env` file in `sdks/pyforgejo` with your `BASE_URL` and `API_KEY`.

``` yml
BASE_URL=https://codeberg.org/api/v1
API_KEY=your_api_key
```

7. Modify the `PyforgejoApi` and `AsyncPyforgejoApi` classes in `sdks/pyforgejo/pyforgejo/client.py` to use environment variables.

``` diff
+import os
+from dotenv import load_dotenv
# ...
+load_dotenv()

+BASE_URL = os.getenv('BASE_URL')
+API_KEY = os.getenv('API_KEY')
+
# ...
 class PyforgejoApi:
# ...
     base_url : typing.Optional[str]
-        The base url to use for requests from the client.
+        The base url to use for requests from the client. Defaults to the BASE_URL from .env file.
# ...
-    api_key : str
+    api_key : typing.Optional[str]
+        The API key to use for authentication. Defaults to the API_KEY from .env file.
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
+        if not base_url:
+            raise ValueError("base_url must be provided either in .env or as an argument")
+        if not api_key:
+            raise ValueError("api_key must be provided either in .env or as an argument")
# same for AsyncPyforgejoApi
```

8. Use the client as shown in the [Usage](#usage) section.

``` python
from pyforgejo import PyforgejoApi

client = PyforgejoApi()

repos = client.repository.repo_search(q='pyforgejo', mode='source')
```

