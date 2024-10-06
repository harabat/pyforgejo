import json

from pyforgejo.api.issue import issue_list_issues
from pyforgejo.api.miscellaneous import get_version
from pyforgejo.api.organization import org_get
from pyforgejo.api.repository import repo_get, repo_search
from pyforgejo.api.user import user_get_current


def test_user_get_current(client):
    response = user_get_current.sync_detailed(client=client)
    assert response.status_code == 200
    assert json.loads(response.content)['login'] is not None


def test_repo_search(client):
    response = repo_search.sync_detailed(client=client)
    assert response.status_code == 200
    assert isinstance(json.loads(response.content)['data'], list)


def test_repo_get(client):
    owner = "harabat"
    repo = "pyforgejo"
    response = repo_get.sync_detailed(client=client, owner=owner, repo=repo)
    assert response.status_code == 200
    assert json.loads(response.content)['name'] == repo


def test_issue_list_issues(client):
    owner = "harabat"
    repo = "pyforgejo"
    response = issue_list_issues.sync_detailed(client=client, owner=owner, repo=repo)
    assert response.status_code == 200
    assert isinstance(json.loads(response.content), list)


def test_org_get(client):
    org = "codeberg"
    response = org_get.sync_detailed(client=client, org=org)
    assert response.status_code == 200
    assert json.loads(response.content)['username'].lower() == org


def test_get_version(client):
    response = get_version.sync_detailed(client=client)
    assert response.status_code == 200
    assert 'version' in json.loads(response.content)
