import os
import sys
from pathlib import Path

import pytest
from dotenv import load_dotenv

project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

from pyforgejo.client import AuthenticatedClient

load_dotenv()

BASE_URL = os.getenv("FORGEJO_API_BASE_URL")
API_TOKEN = os.getenv("FORGEJO_API_TOKEN")

if not BASE_URL or not API_TOKEN:
    raise ValueError("FORGEJO_API_BASE_URL and FORGEJO_API_TOKEN must be set in the .env file")


@pytest.fixture
def client():
    return AuthenticatedClient(base_url=BASE_URL, token=API_TOKEN)
