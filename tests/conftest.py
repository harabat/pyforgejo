import os

import pytest
from dotenv import load_dotenv

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyforgejo.client import AuthenticatedClient

# Load environment variables from .env file
load_dotenv()

# Configuration for tests
BASE_URL = os.getenv("FORGEJO_API_BASE_URL")
API_TOKEN = os.getenv("FORGEJO_API_TOKEN")

if not BASE_URL or not API_TOKEN:
    raise ValueError("FORGEJO_API_BASE_URL and FORGEJO_API_TOKEN must be set in the .env file")


@pytest.fixture
def client():
    return AuthenticatedClient(base_url=BASE_URL, token=API_TOKEN)
