import os

import pytest
from dotenv import load_dotenv

from pyforgejo.client import \
    PyforgejoApi  # Replace with your actual client import
from pyforgejo.types import (Activity, Attachment, Branch, ChangedFile,
                             CombinedStatus, Comment, Commit, CommitStatus,
                             ContentsResponse, GeneralApiSettings,
                             GeneralAttachmentSettings, GeneralRepoSettings,
                             GeneralUiSettings, GitignoreTemplateInfo, Issue,
                             Label, LabelTemplate, LicensesTemplateListEntry,
                             LicenseTemplateInfo, Organization, PullRequest,
                             Release, Repository, ServerVersion, User,
                             WikiPage, WikiPageMetaData)

# load environment variables at the beginning
load_dotenv()

# get environment variables with default values
BASE_URL = os.getenv("BASE_URL", "")
API_KEY = os.getenv("PYTEST_API_KEY", "")


@pytest.fixture
def client():
    # Replace with your actual client initialization for testing
    return PyforgejoApi(
        base_url=BASE_URL,
        api_key=API_KEY,
    )


# Miscellaneous Client Tests
def test_miscellaneous_list_gitignores_templates(client: PyforgejoApi):
    try:
        templates = client.miscellaneous.list_gitignores_templates()
        assert isinstance(templates, list)
        assert all(isinstance(item, str) for item in templates)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_miscellaneous_get_gitignore_template_info(client: PyforgejoApi):
    try:
        template = client.miscellaneous.get_gitignore_template_info(name="Python")
        assert isinstance(template, GitignoreTemplateInfo)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_miscellaneous_list_label_templates(client: PyforgejoApi):
    try:
        templates = client.miscellaneous.list_label_templates()
        assert isinstance(templates, list)
        assert all(isinstance(item, str) for item in templates)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_miscellaneous_get_label_template_info(client: PyforgejoApi):
    try:
        template = client.miscellaneous.get_label_template_info(name="Default")
        assert isinstance(template, list)
        assert all(isinstance(item, LabelTemplate) for item in template)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_miscellaneous_list_license_templates(client: PyforgejoApi):
    try:
        licenses = client.miscellaneous.list_license_templates()
        assert isinstance(licenses, list)
        assert all(isinstance(item, LicensesTemplateListEntry) for item in licenses)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_miscellaneous_get_license_template_info(client: PyforgejoApi):
    try:
        license_info = client.miscellaneous.get_license_template_info(name="MIT")
        assert isinstance(license_info, LicenseTemplateInfo)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_miscellaneous_get_signing_key(client: PyforgejoApi):
    try:
        signing_key = client.miscellaneous.get_signing_key()
        assert signing_key is not None
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_miscellaneous_get_version(client: PyforgejoApi):
    try:
        version = client.miscellaneous.get_version()
        assert isinstance(version, ServerVersion)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


# User Client Tests
def test_user_get_current(client: PyforgejoApi):
    try:
        user = client.user.get_current()
        assert isinstance(user, User)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_user_get(client: PyforgejoApi):
    try:
        user = client.user.get(username="forgejo")
        assert isinstance(user, User)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


# Issue Client Tests
def test_issue_list_labels(client: PyforgejoApi):
    try:
        labels = client.issue.list_labels(owner="forgejo", repo="forgejo")
        assert isinstance(labels, list)
        assert all(isinstance(item, Label) for item in labels)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_issue_get_label(client: PyforgejoApi):
    try:
        label = client.issue.get_label(owner="forgejo", repo="forgejo", id=181598)
        assert isinstance(label, Label)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_issue_search_issues(client: PyforgejoApi):
    try:
        issues = client.issue.search_issues(q="pyforgejo")
        assert isinstance(issues, list)
        assert all(isinstance(item, Issue) for item in issues)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_issue_list_issues(client: PyforgejoApi):
    try:
        issues = client.issue.list_issues(owner="forgejo", repo="forgejo")
        assert isinstance(issues, list)
        assert all(isinstance(item, Issue) for item in issues)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


# Repository Client Tests
def test_repository_repo_get(client: PyforgejoApi):
    try:
        repo = client.repository.repo_get(owner="forgejo", repo="forgejo")
        assert isinstance(repo, Repository)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_contents(client: PyforgejoApi):
    try:
        contents = client.repository.repo_get_contents(
            owner="harabat", repo="pyforgejo", filepath="README.md"
        )
        assert isinstance(contents, ContentsResponse)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"

    try:
        contents = client.repository.repo_get_contents(
            owner="harabat", repo="pyforgejo", filepath="tests"
        )
        assert isinstance(contents, list)
        assert all(isinstance(item, ContentsResponse) for item in contents)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_list_branches(client: PyforgejoApi):
    try:
        branches = client.repository.repo_list_branches(owner="forgejo", repo="forgejo")
        assert isinstance(branches, list)
        assert all(isinstance(item, Branch) for item in branches)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_branch(client: PyforgejoApi):
    try:
        branch = client.repository.repo_get_branch(
            owner="forgejo", repo="forgejo", branch="forgejo"
        )
        assert isinstance(branch, Branch)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_list_collaborators(client: PyforgejoApi):
    try:
        collaborators = client.repository.repo_list_collaborators(
            owner="forgejo", repo="forgejo"
        )
        assert isinstance(collaborators, list)
        assert all(isinstance(item, User) for item in collaborators)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_all_commits(client: PyforgejoApi):
    try:
        commits = client.repository.repo_get_all_commits(
            owner="forgejo", repo="forgejo"
        )
        assert isinstance(commits, list)
        assert all(isinstance(item, Commit) for item in commits)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_list_releases(client: PyforgejoApi):
    try:
        releases = client.repository.repo_list_releases(owner="forgejo", repo="forgejo")
        assert isinstance(releases, list)
        assert all(isinstance(item, Release) for item in releases)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_release_by_tag(client: PyforgejoApi):
    try:
        release = client.repository.repo_get_release_by_tag(
            owner="forgejo", repo="forgejo", tag="v10.0.0"
        )
        assert isinstance(release, Release)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_release(client: PyforgejoApi):
    try:
        release = client.repository.repo_get_release(
            owner="forgejo", repo="forgejo", id=2741327
        )
        assert isinstance(release, Release)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_list_release_attachments(client: PyforgejoApi):
    try:
        attachments = client.repository.repo_list_release_attachments(
            owner="forgejo", repo="forgejo", id=2741327
        )
        assert isinstance(attachments, list)
        assert all(isinstance(item, Attachment) for item in attachments)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_list_stargazers(client: PyforgejoApi):
    try:
        stargazers = client.repository.repo_list_stargazers(
            owner="forgejo", repo="forgejo"
        )
        assert isinstance(stargazers, list)
        assert all(isinstance(item, User) for item in stargazers)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_combined_status_by_ref(client: PyforgejoApi):
    try:
        combined_status = client.repository.repo_get_combined_status_by_ref(
            owner="forgejo", repo="forgejo", ref="test_ref"
        )
        assert isinstance(combined_status, CombinedStatus)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_list_statuses_by_ref(client: PyforgejoApi):
    try:
        statuses = client.repository.repo_list_statuses_by_ref(
            owner="forgejo", repo="forgejo", ref="test_ref"
        )
        assert isinstance(statuses, list)
        assert all(isinstance(item, CommitStatus) for item in statuses)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_pull_request(client: PyforgejoApi):
    try:
        pull_request = client.repository.repo_get_pull_request(
            owner="forgejo", repo="forgejo", index=6577
        )
        assert isinstance(pull_request, PullRequest)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_pull_request_files(client: PyforgejoApi):
    try:
        files = client.repository.repo_get_pull_request_files(
            owner="forgejo", repo="forgejo", index=6577
        )
        assert isinstance(files, list)
        assert all(isinstance(item, ChangedFile) for item in files)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_wiki_pages(client: PyforgejoApi):
    try:
        wiki_pages = client.repository.repo_get_wiki_pages(
            owner="codeberg", repo="pages-server"
        )
        assert isinstance(wiki_pages, list)
        assert all(isinstance(item, WikiPageMetaData) for item in wiki_pages)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_get_wiki_page(client: PyforgejoApi):
    try:
        wiki_page = client.repository.repo_get_wiki_page(
            owner="codeberg", repo="pages-server", page_name="Overview"
        )
        assert isinstance(wiki_page, WikiPage)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


# Organization Client Tests
def test_organization_org_get(client: PyforgejoApi):
    try:
        org = client.organization.org_get(org="forgejo")
        assert isinstance(org, Organization)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_organization_org_list_activity_feeds(client: PyforgejoApi):
    try:
        activities = client.organization.org_list_activity_feeds(org="forgejo")
        assert isinstance(activities, list)
        assert all(isinstance(item, Activity) for item in activities)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


# Settings Client Tests
def test_settings_get_general_api_settings(client: PyforgejoApi):
    try:
        settings = client.settings.get_general_api_settings()
        assert isinstance(settings, GeneralApiSettings)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_settings_get_general_attachment_settings(client: PyforgejoApi):
    try:
        settings = client.settings.get_general_attachment_settings()
        assert isinstance(settings, GeneralAttachmentSettings)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_settings_get_general_repository_settings(client: PyforgejoApi):
    try:
        settings = client.settings.get_general_repository_settings()
        assert isinstance(settings, GeneralRepoSettings)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_settings_get_general_ui_settings(client: PyforgejoApi):
    try:
        settings = client.settings.get_general_ui_settings()
        assert isinstance(settings, GeneralUiSettings)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


# POST Tests
def test_repository_create_current_user_repo(client: PyforgejoApi):
    try:
        repo = client.repository.create_current_user_repo(name="test_repo")
        assert isinstance(repo, Repository)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_issue_create_issue(client: PyforgejoApi):
    try:
        issue = client.issue.create_issue(
            owner="harabat", repo="test_repo", title="Test Issue"
        )
        assert isinstance(issue, Issue)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_issue_create_comment(client: PyforgejoApi):
    try:
        comment = client.issue.create_comment(
            owner="harabat", repo="test_repo", index=1, body="Test Comment"
        )
        assert isinstance(comment, Comment)
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_issue_delete_comment(client: PyforgejoApi):
    try:
        comments = client.issue.get_comments(owner="harabat", repo="test_repo", index=1)
        comment = comments[0]
        client.issue.delete_comment(owner="harabat", repo="test_repo", id=comment.id)
        comments = client.issue.get_comments(owner="harabat", repo="test_repo", index=1)
        assert comment.id not in [i.id for i in comments]
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_issue_delete_issue(client: PyforgejoApi):
    try:
        client.issue.delete(owner="harabat", repo="test_repo", index=1)
        issues = client.issue.list_issues(owner="harabat", repo="test_repo")
        assert len(issues) == 0
    except Exception as e:
        assert False, f"Test failed with exception: {e}"


def test_repository_repo_delete(client: PyforgejoApi):
    try:
        client.repository.repo_delete(owner="harabat", repo="test_repo")
        repos = client.user.list_repos(username="harabat")
        assert "test_repo" not in [i.name for i in repos]
    except Exception as e:
        assert False, f"Test failed with exception: {e}"
